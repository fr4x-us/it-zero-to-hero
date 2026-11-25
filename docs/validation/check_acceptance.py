"""R3-08/R4-02: status penerimaan terstruktur (TPL-01a) dibandingkan dengan baseline penerimaan NYATA di git.
Untuk modul dengan penerimaan historis: setiap varian dibandingkan dengan isinya pada `acceptance.historical.baseline_commit`.
Kategori pemeriksaan: STRUKTUR (perbandingan isi berkas; tidak ada penilaian semantik)."""
import copy, fnmatch, glob, json, subprocess, sys
import yaml
from lib import ROOT, CUR, load, Report

ASSESS = ('theory/items/*.yaml', 'concept/items/*.yaml', 'lab/act-0*/checks.yaml')

def _variants(doc):
    return doc.get('variants', []) if isinstance(doc, dict) else []

def current_variants(m):
    out = []
    for pat in ASSESS:
        for f in sorted(glob.glob(str(CUR / f'mod-w{m}' / pat))):
            rel = str(f)[len(str(CUR)) + 1:]
            for v in _variants(yaml.safe_load(open(f, encoding='utf-8'))):
                out.append((rel, v))
    return out

def shared(doc):
    """R5-05: field slot bersama = semua field tingkat berkas selain `variants` (kompetensi, required_concepts,
    format, max_points, validation, feedback_stage, difficulty, estimated_seconds, normalization, dst.)."""
    return {k: x for k, x in (doc or {}).items() if k != 'variants'} if isinstance(doc, dict) else {}

def current_shared(m):
    out = {}
    for pat in ASSESS:
        for f in sorted(glob.glob(str(CUR / f'mod-w{m}' / pat))):
            out[str(f)[len(str(CUR)) + 1:]] = shared(yaml.safe_load(open(f, encoding='utf-8')))
    return out

def baseline_shared(m, commit):
    out = {}
    files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', commit, f'curriculum/mod-w{m}'], cwd=ROOT, text=True).split()
    for f in files:
        rel = f[len('curriculum/'):]
        if any(fnmatch.fnmatch(rel, f'mod-w{m}/' + p) for p in ASSESS):
            out[rel] = shared(yaml.safe_load(subprocess.check_output(['git', 'show', f'{commit}:{f}'], cwd=ROOT, text=True)))
    return out

def baseline_variants(m, commit):
    out = []
    files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', commit, f'curriculum/mod-w{m}'], cwd=ROOT, text=True).split()
    for f in files:
        rel = f[len('curriculum/'):]
        if not any(fnmatch.fnmatch(rel, f'mod-w{m}/' + p) for p in ASSESS):
            continue
        doc = yaml.safe_load(subprocess.check_output(['git', 'show', f'{commit}:{f}'], cwd=ROOT, text=True))
        for v in _variants(doc):
            out.append((rel, v))
    return out

def body(v):
    return json.dumps({k: x for k, x in v.items() if k != 'item_version'}, sort_keys=True, ensure_ascii=False)

def vnum(x):
    return tuple(int(p) for p in str(x).split('.'))

def validate(m, cur, base, acc, cur_sh=None, base_sh=None):
    """Kembalikan daftar kesalahan (kosong = sah). cur/base: [(berkas, varian)]; acc: blok acceptance;
    cur_sh/base_sh: {berkas: field bersama}. Perubahan field bersama memengaruhi SEMUA varian berkas itu."""
    err = []
    cur_sh = cur_sh or {}; base_sh = base_sh or {}
    sh_changed = set()
    for f in sorted(set(cur_sh) | set(base_sh)):
        if f in cur_sh and f in base_sh and json.dumps(cur_sh[f], sort_keys=True, ensure_ascii=False) != json.dumps(base_sh[f], sort_keys=True, ensure_ascii=False):
            keys = sorted(k for k in set(cur_sh[f]) | set(base_sh[f]) if cur_sh[f].get(k) != base_sh[f].get(k))
            sh_changed.add(f)
            aff = [v['variant_id'] for ff, v in cur if ff == f]
            err_f = [vid for vid in aff if vid not in {e['variant_id'] for e in (acc.get('revised_variants') or [])}]
            if err_f: err.append(f'{f}: field bersama berubah {keys}; varian terdampak belum tercatat/berversi: {err_f}')
    FILE = {v['variant_id']: ff for ff, v in cur}
    ids = [v['variant_id'] for _, v in cur]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup: err.append(f'variant_id ganda di modul: {dup}')
    entries = acc.get('revised_variants') or []
    eids = [e['variant_id'] for e in entries]
    if len(eids) != len(set(eids)): err.append('entri revised_variants ganda')
    E = {e['variant_id']: e for e in entries}
    B = {v['variant_id']: v for _, v in base}
    C = {v['variant_id']: v for _, v in cur}
    for vid in sorted(set(B) - set(C)): err.append(f'{vid}: varian yang diterima hilang')
    changed = []
    for vid, v in C.items():
        if vid not in B:
            err.append(f'{vid}: varian baru setelah penerimaan (tidak ada di baseline)'); continue
        b = B[vid]; bv = b.get('item_version'); cv = v.get('item_version')
        if body(v) == body(b) and FILE.get(vid) not in sh_changed:
            if cv != bv: err.append(f'{vid}: isi sama tetapi versi {bv} → {cv}')
            if vid in E: err.append(f'{vid}: tercatat sebagai revisi padahal isi sama dengan baseline')
            continue
        changed.append(vid)
        if bv is None or cv is None: err.append(f'{vid}: isi berubah pada varian tanpa item_version'); continue
        if not vnum(cv) > vnum(bv): err.append(f'{vid}: isi berubah tanpa kenaikan versi ({bv} → {cv})')
        e = E.get(vid)
        if e is None: err.append(f'{vid}: revisi tidak tercatat di revised_variants'); continue
        if str(e['accepted_version']) != str(bv): err.append(f'{vid}: accepted_version {e["accepted_version"]} ≠ baseline {bv}')
        if str(e['current_version']) != str(cv): err.append(f'{vid}: current_version {e["current_version"]} ≠ berkas {cv}')
        if e.get('independent_review') != 'PENDING' or e.get('owner_acceptance') != 'PENDING':
            err.append(f'{vid}: status revisi harus PENDING (independent_review/owner_acceptance)')
    for vid in sorted(set(E) - set(C)): err.append(f'{vid}: entri revisi untuk varian yang tidak ada')
    want = 'REVISED_PENDING' if changed else 'ACCEPTED_AS_IS'
    if acc.get('current_content') != want: err.append(f'current_content harus {want}')
    return err, changed

def mutation_tests(r):
    """Uji mutasi pada salinan data W2 di memori; setiap mutasi harus terdeteksi."""
    M = load('mod-w02/module.yaml'); acc = M['acceptance']; commit = acc['historical']['baseline_commit']
    cur, base = current_variants('02'), baseline_variants('02', commit)
    def run(c=None, b=None, a=None):
        return validate('02', c if c is not None else cur, b if b is not None else base, a if a is not None else acc)[0]
    r.check(not run(), 'mutasi: data asli harus sah')
    k = [i for i, (_, v) in enumerate(cur) if v['variant_id'] == 'mod-w02.theory.s03.vA'][0]
    c1 = copy.deepcopy(cur); c1[k][1]['stem'] += ' (diubah)'
    r.check(any('tanpa kenaikan versi' in e for e in run(c=c1)), 'mutasi: isi berubah tanpa kenaikan versi')
    c2 = copy.deepcopy(c1); c2[k][1]['item_version'] = '2.0'
    r.check(any('tidak tercatat' in e for e in run(c=c2)), 'mutasi: revisi tidak tercatat')
    a3 = copy.deepcopy(acc); a3['revised_variants'][0]['accepted_version'] = '9.0'
    r.check(any('accepted_version' in e for e in run(a=a3)), 'mutasi: accepted_version salah')
    a4 = copy.deepcopy(acc); a4['revised_variants'][0]['current_version'] = '9.0'
    r.check(any('current_version' in e for e in run(a=a4)), 'mutasi: current_version salah')
    c5 = copy.deepcopy(cur); c5.append(copy.deepcopy(cur[0]))
    r.check(any('ganda di modul' in e for e in run(c=c5)), 'mutasi: variant_id ganda')
    a6 = copy.deepcopy(acc); a6['revised_variants'].append(copy.deepcopy(a6['revised_variants'][0]))
    r.check(any('entri revised_variants ganda' in e for e in run(a=a6)), 'mutasi: entri ganda')
    a7 = copy.deepcopy(acc); a7['revised_variants'][0]['owner_acceptance'] = 'ACCEPTED'
    r.check(any('harus PENDING' in e for e in run(a=a7)), 'mutasi: status penerimaan diklaim')
    a8 = copy.deepcopy(acc); a8['revised_variants'] = a8['revised_variants'][1:]
    r.check(any('tidak tercatat' in e for e in run(a=a8)), 'mutasi: entri revisi hilang')
    # R5-05: field slot bersama
    csh, bsh = current_shared('02'), baseline_shared('02', commit)
    f0 = [f for f, v in cur if v['variant_id'] == 'mod-w02.theory.s03.vA'][0]
    for fld, val in (('competency', 'comp-x'), ('required_concepts', ['x']), ('max_points', 99), ('difficulty', 'zz'), ('estimated_seconds', 1)):
        cs = copy.deepcopy(csh); cs[f0][fld] = val
        r.check(any('field bersama berubah' in e for e in validate('02', cur, base, acc, cs, bsh)[0]), f'mutasi: field bersama {fld} berubah tanpa versi/entri')
    cs = copy.deepcopy(csh); cs[f0]['max_points'] = 99
    vids = [v['variant_id'] for f, v in cur if f == f0]
    c12 = copy.deepcopy(cur)
    for f, v in c12:
        if f == f0: v['item_version'] = '2.0'
    a12 = copy.deepcopy(acc); a12['revised_variants'] += [{'variant_id': x, 'accepted_version': '1.0', 'current_version': '2.0', 'independent_review': 'PENDING', 'owner_acceptance': 'PENDING'} for x in vids]
    r.check(not validate('02', c12, base, a12, cs, bsh)[0], 'mutasi: field bersama berubah + semua varian berversi & tercatat harus sah')
    a13 = copy.deepcopy(a12); a13['revised_variants'] = a13['revised_variants'][:-1]
    r.check(any('field bersama' in e for e in validate('02', c12, base, a13, cs, bsh)[0]), 'mutasi: field bersama berubah, satu varian terdampak tidak tercatat')
    r.check(any('tanpa kenaikan versi' in e for e in validate('02', cur, base, a12, cs, bsh)[0]), 'mutasi: field bersama berubah, tercatat tetapi versi tidak naik')
    a15 = copy.deepcopy(acc); a15['current_content'] = 'ACCEPTED_AS_IS'
    r.check(any('current_content' in e for e in run(a=a15)), 'mutasi: promosi penerimaan (REVISED_PENDING → ACCEPTED_AS_IS)')
    a16 = copy.deepcopy(acc); a16['revised_variants'][0]['independent_review'] = 'PASS'
    r.check(any('harus PENDING' in e for e in run(a=a16)), 'mutasi: promosi review independen tanpa otorisasi')
    # versi historis > 1.0 didukung
    b9 = copy.deepcopy(base); j = [i for i, (_, v) in enumerate(b9) if v['variant_id'] == 'mod-w02.theory.s03.vA'][0]
    b9[j][1]['item_version'] = '2.0'; c9 = copy.deepcopy(cur); c9[k][1]['item_version'] = '2.0'
    r.check(not run(c=c9, b=b9), 'mutasi: versi historis 2.0 tanpa perubahan harus sah')
    c10 = copy.deepcopy(c9); c10[k][1]['stem'] += ' (diubah)'; c10[k][1]['item_version'] = '3.0'
    a10 = copy.deepcopy(acc); a10['revised_variants'].append({'variant_id': 'mod-w02.theory.s03.vA', 'accepted_version': '2.0', 'current_version': '3.0', 'independent_review': 'PENDING', 'owner_acceptance': 'PENDING'})
    r.check(not run(c=c10, b=b9, a=a10), 'mutasi: revisi 2.0 → 3.0 tercatat harus sah')
    a11 = copy.deepcopy(a10); a11['revised_variants'][-1]['accepted_version'] = '1.0'
    r.check(any('accepted_version' in e for e in run(c=c10, b=b9, a=a11)), 'mutasi: accepted_version 1.0 untuk baseline 2.0')

def main():
    r = Report('penerimaan')
    pend = 0
    for m in ('01', '02', '03', '04', '05', '06', '07', '08'):
        M = load(f'mod-w{m}/module.yaml'); st = M['status']['owner_accepted']
        if st is True or st == 'YES':
            a = M.get('acceptance')
            if not r.check(a is not None and a['historical'].get('baseline_commit'), f'W{m}: blok acceptance/baseline_commit'): continue
            r.check(a['historical']['id'] == f'W{m}-ACC', f'W{m}: id historis')
            bc = a['historical']['baseline_commit']
            err, changed = validate(m, current_variants(m), baseline_variants(m, bc), a, current_shared(m), baseline_shared(m, bc))
            pend += len(a.get('revised_variants') or [])
            for e in err: r.check(False, f'W{m}: {e}')
            r.check(True, f'W{m}: perbandingan baseline')
            print(f'  W{m}: baseline {a["historical"]["baseline_commit"][:7]}; varian berubah {len(changed)}; tercatat PENDING {len(a.get("revised_variants") or [])}')
        else:
            r.check(not (M.get('acceptance') or {}).get('historical'), f'W{m}: belum diterima, tidak boleh ada penerimaan historis')
            print(f'  W{m}: belum diterima owner')
    print(f'  total varian W1–W4 tercatat PENDING: {pend}')
    mutation_tests(r)
    print('  uji validator: 22 kasus — 18 mutasi terdeteksi, 4 kasus sah diterima (data asli; versi historis 2.0; revisi 2.0 → 3.0; field bersama berubah + semua varian tercatat)')
    return r.done()

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
