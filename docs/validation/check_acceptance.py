"""R3-08/R4-02: status penerimaan terstruktur (TPL-01a) dibandingkan dengan baseline penerimaan NYATA di git.
Untuk modul dengan penerimaan historis: setiap varian dibandingkan dengan isinya pada `acceptance.historical.baseline_commit`.
Kategori pemeriksaan: STRUKTUR (perbandingan isi berkas; tidak ada penilaian semantik)."""
import copy, fnmatch, glob, json, re, subprocess, sys
from pathlib import Path
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

# ---- R6-01: jangkar penerimaan historis tepercaya ----
ANCHORS = Path(__file__).parent / 'trust/acceptance_anchors.yaml'

class Git:
    def subject(self, sha):
        r = subprocess.run(['git', 'log', '-1', '--format=%s', f'{sha}^{{commit}}', '--'], cwd=ROOT, capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None
    def ancestor(self, sha):
        return subprocess.run(['git', 'merge-base', '--is-ancestor', sha, 'HEAD'], cwd=ROOT, capture_output=True).returncode == 0

def load_anchors():
    return yaml.safe_load(open(ANCHORS, encoding='utf-8'))

def trust_errors(m, M, anchors, decision_log, git):
    """Kembalikan (kesalahan, baseline tepercaya|None). Baseline TIDAK diambil dari module.yaml."""
    err = []; an = anchors.get(m)
    st = M.get('status', {}).get('owner_accepted'); accepted = st is True or st == 'YES'
    hist = (M.get('acceptance') or {}).get('historical') or {}
    if not an:
        if accepted or hist: err.append(f'W{m}: penerimaan historis tanpa jangkar tepercaya (promosi tidak sah)')
        return err, None
    sha = str(an.get('baseline_commit', ''))
    if not re.fullmatch(r'[0-9a-f]{40}', sha): err.append(f'W{m}: jangkar baseline bukan SHA penuh')
    if not accepted or not hist: err.append(f'W{m}: jangkar ada tetapi modul tidak mencatat penerimaan historis')
    if hist.get('id') != an.get('acceptance_id'): err.append(f'W{m}: id historis {hist.get("id")} ≠ jangkar {an.get("acceptance_id")}')
    if str(hist.get('baseline_commit')) != sha: err.append(f'W{m}: baseline_commit modul {str(hist.get("baseline_commit"))[:12]} ≠ jangkar {sha[:12]} (penggantian baseline ditolak)')
    subj = git.subject(sha)
    if subj is None: err.append(f'W{m}: commit baseline {sha[:12]} tidak ada di repositori')
    else:
        # basis 'accepted_review_head' (W5–W8, PR #28): HEAD review yang diterima owner, bukan merge commit
        if an.get('basis') != 'accepted_review_head' and not subj.startswith(f'Merge pull request #{an.get("pr")} '): err.append(f'W{m}: commit {sha[:12]} bukan merge PR #{an.get("pr")} ({subj})')
        if not git.ancestor(sha): err.append(f'W{m}: commit {sha[:12]} bukan leluhur HEAD')
    if f'| {an.get("decision_log")} | OWNER ACCEPTED' not in decision_log: err.append(f'W{m}: catatan keputusan owner {an.get("decision_log")} tidak ditemukan di DECISIONS_LOG')
    return err, (sha if not err else None)

def revision_trust(m, M, anchors, decision_log, git):
    """Penerimaan owner atas varian revisi (PR #28 ACC): dipercaya hanya bila cocok dengan jangkar terpisah."""
    ra = (anchors.get(m) or {}).get('revision_acceptance'); ma = (M.get('acceptance') or {}).get('revision_acceptance')
    if not ra:
        return ([f'W{m}: revision_acceptance tanpa jangkar tepercaya'] if ma else []), None
    err = []
    if not ma or ma.get('id') != ra.get('id') or str(ma.get('reviewed_head')) != ra.get('reviewed_head'):
        err.append(f'W{m}: revision_acceptance modul tidak cocok dengan jangkar {ra.get("id")} @ {str(ra.get("reviewed_head"))[:12]}')
    if git.subject(ra.get('reviewed_head', '')) is None or not git.ancestor(ra.get('reviewed_head', '')): err.append(f'W{m}: reviewed_head tidak ada/bukan leluhur HEAD')
    if f'| {ra.get("decision_log")} | OWNER ACCEPTED' not in decision_log: err.append(f'W{m}: catatan keputusan owner {ra.get("decision_log")} tidak ditemukan')
    return err, (ra if not err else None)

# ---- R6-02: identitas lokasi varian ----
def expected_prefix(rel):
    mm = re.fullmatch(r'mod-w(\d\d)/(theory|concept)/items/(s\d\d)\.yaml', rel)
    if mm: return f'mod-w{mm.group(1)}.{mm.group(2)}.{mm.group(3)}'
    mm = re.fullmatch(r'mod-w(\d\d)/lab/(act-0\d)/checks\.yaml', rel)
    if mm: return f'mod-w{mm.group(1)}.lab.{mm.group(2)}'
    return None

def location_errors(m, cur, base, cur_sh):
    err = []
    FB = {v['variant_id']: (f, v) for f, v in base}
    for f, v in cur:
        vid = v.get('variant_id', '?'); pre = expected_prefix(f)
        if pre is None or not f.startswith(f'mod-w{m}/'): err.append(f'{vid}: berkas {f} bukan lokasi penilaian modul W{m}'); continue
        if not re.fullmatch(re.escape(pre) + r'\.v[A-Z]', vid): err.append(f'{vid}: identitas tidak cocok dengan lokasi {f} (harus {pre}.vX)')
        sl = (cur_sh.get(f) or {}).get('slot_id')
        if sl is not None and sl != pre: err.append(f'{f}: slot_id {sl} ≠ lokasi {pre}')
        if vid in FB:
            bf, bv = FB[vid]
            if bf != f: err.append(f'{vid}: dipindah dari {bf} ke {f}')
            if bv.get('item_id') != v.get('item_id'): err.append(f'{vid}: item_id berubah {bv.get("item_id")} → {v.get("item_id")}')
    return err

def body(v):
    return json.dumps({k: x for k, x in v.items() if k != 'item_version'}, sort_keys=True, ensure_ascii=False)

def vnum(x):
    return tuple(int(p) for p in str(x).split('.'))

def validate(m, cur, base, acc, cur_sh=None, base_sh=None, rev=None, rev_variants=None):
    """Kembalikan daftar kesalahan (kosong = sah). cur/base: [(berkas, varian)]; acc: blok acceptance;
    cur_sh/base_sh: {berkas: field bersama}. Perubahan field bersama memengaruhi SEMUA varian berkas itu."""
    err = []
    cur_sh = cur_sh or {}; base_sh = base_sh or {}
    err += location_errors(m, cur, base, cur_sh)
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
    changed, accepted = [], []
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
        st = (e.get('independent_review'), e.get('owner_acceptance'))
        if st == ('PENDING', 'PENDING'):
            continue
        ma = acc.get('revision_acceptance') or {}
        if st == ('TARGETED_LIMITED', 'ACCEPTED') and rev and ma.get('id') == rev.get('id') and str(ma.get('reviewed_head')) == rev.get('reviewed_head'):
            RV = {x['variant_id']: x for _, x in (rev_variants or [])}
            if vid not in RV or body(RV[vid]) != body(v) or str(RV[vid].get('item_version')) != str(cv):
                err.append(f'{vid}: diterima pada HEAD review, tetapi isi/versi kini berbeda dari HEAD review')
            accepted.append(vid)
        else:
            err.append(f'{vid}: status revisi harus PENDING, atau TARGETED_LIMITED/ACCEPTED dengan penerimaan revisi tepercaya')
    for vid in sorted(set(E) - set(C)): err.append(f'{vid}: entri revisi untuk varian yang tidak ada')
    want = 'ACCEPTED_AS_IS' if not changed else ('REVISED_ACCEPTED' if sorted(accepted) == sorted(changed) else 'REVISED_PENDING')
    if acc.get('current_content') != want: err.append(f'current_content harus {want}')
    return err, changed

def mutation_tests(r):
    """Uji mutasi pada salinan data W2 di memori; setiap mutasi harus terdeteksi."""
    M = load('mod-w02/module.yaml'); real = M['acceptance']; commit = real['historical']['baseline_commit']
    cur, base = current_variants('02'), baseline_variants('02', commit)
    # jalur PENDING diuji pada salinan dengan status PENDING (sebelum penerimaan revisi)
    acc = copy.deepcopy(real); acc.pop('revision_acceptance', None); acc['current_content'] = 'REVISED_PENDING'
    for e in acc['revised_variants']: e['independent_review'] = e['owner_acceptance'] = 'PENDING'
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
    # R6-02: lokasi varian
    c17 = copy.deepcopy(cur); c17[k] = ('mod-w02/theory/items/s04.yaml', c17[k][1])
    r.check(any('dipindah' in e for e in run(c=c17)), 'mutasi: varian dipindah ke berkas lain (isi dan versi sama)')
    c18 = copy.deepcopy(cur); c18[k] = ('mod-w02/concept/items/s03.yaml', c18[k][1])
    r.check(any('identitas tidak cocok' in e for e in run(c=c18)), 'mutasi: varian dipindah ke komponen lain')
    cs19 = copy.deepcopy(csh); cs19[f0]['slot_id'] = 'mod-w02.theory.s99'
    r.check(any('slot_id' in e for e in validate('02', cur, base, acc, cs19, bsh)[0]), 'mutasi: asosiasi slot diubah')
    c20 = copy.deepcopy(cur); c20[k][1]['item_id'] = 'item-x'
    r.check(any('item_id berubah' in e for e in run(c=c20)), 'mutasi: item_id diubah')
    r.check(not validate('02', cur, base, acc, csh, bsh)[0], 'mutasi: lokasi asli tidak berubah harus sah')
    # versi historis > 1.0 didukung
    b9 = copy.deepcopy(base); j = [i for i, (_, v) in enumerate(b9) if v['variant_id'] == 'mod-w02.theory.s03.vA'][0]
    b9[j][1]['item_version'] = '2.0'; c9 = copy.deepcopy(cur); c9[k][1]['item_version'] = '2.0'
    r.check(not run(c=c9, b=b9), 'mutasi: versi historis 2.0 tanpa perubahan harus sah')
    c10 = copy.deepcopy(c9); c10[k][1]['stem'] += ' (diubah)'; c10[k][1]['item_version'] = '3.0'
    a10 = copy.deepcopy(acc); a10['revised_variants'].append({'variant_id': 'mod-w02.theory.s03.vA', 'accepted_version': '2.0', 'current_version': '3.0', 'independent_review': 'PENDING', 'owner_acceptance': 'PENDING'})
    r.check(not run(c=c10, b=b9, a=a10), 'mutasi: revisi 2.0 → 3.0 tercatat harus sah')
    # penerimaan revisi PR #28 ACC (jalur penerimaan)
    an = load_anchors()['02']['revision_acceptance']; RVv = baseline_variants('02', an['reviewed_head'])
    def runr(a=real, c=None, rv=an):
        return validate('02', c if c is not None else cur, base, a, rev=rv, rev_variants=RVv)[0]
    r.check(not runr(), 'penerimaan revisi: data asli (21 varian ACCEPTED, jangkar cocok) sah')
    r.check(any('harus PENDING' in e for e in runr(rv=None)), 'penerimaan revisi: ACCEPTED tanpa jangkar tepercaya ditolak')
    a21 = copy.deepcopy(real); a21['revision_acceptance']['reviewed_head'] = '0' * 40
    r.check(any('harus PENDING' in e for e in runr(a=a21)), 'penerimaan revisi: reviewed_head modul berbeda dari jangkar ditolak')
    c22 = copy.deepcopy(cur); j2 = [i for i, (_, v) in enumerate(c22) if v['variant_id'] == real['revised_variants'][0]['variant_id']][0]; c22[j2][1]['stem'] += ' (diubah setelah review)'
    r.check(any('berbeda dari HEAD review' in e for e in runr(c=c22)), 'penerimaan revisi: isi berubah setelah HEAD review ditolak')
    a23 = copy.deepcopy(real); a23['revised_variants'][0]['independent_review'] = 'PASS'
    r.check(any('harus PENDING' in e for e in runr(a=a23)), 'penerimaan revisi: klaim review independen PASS per varian ditolak')
    a24 = copy.deepcopy(real); a24['current_content'] = 'REVISED_PENDING'
    r.check(any('current_content' in e for e in runr(a=a24)), 'penerimaan revisi: current_content tidak sesuai ditolak')
    a11 = copy.deepcopy(a10); a11['revised_variants'][-1]['accepted_version'] = '1.0'
    r.check(any('accepted_version' in e for e in run(c=c10, b=b9, a=a11)), 'mutasi: accepted_version 1.0 untuk baseline 2.0')

def trust_tests(r):
    """R6-01: uji positif/negatif jangkar penerimaan."""
    A = load_anchors(); DL = (ROOT / 'docs/DECISIONS_LOG.md').read_text(encoding='utf-8'); G = Git()
    M2 = load('mod-w02/module.yaml'); M1 = load('mod-w01/module.yaml'); M5 = load('mod-w05/module.yaml')
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    r.check(not trust_errors('02', M2, A, DL, G)[0], 'jangkar: baseline historis sah diterima')
    m = copy.deepcopy(M2); m['acceptance']['historical']['baseline_commit'] = head
    r.check(any('penggantian baseline' in e for e in trust_errors('02', m, A, DL, G)[0]), 'jangkar: baseline diganti commit revisi terbaru ditolak')
    a = copy.deepcopy(A); a['02']['baseline_commit'] = 'f' * 40; m = copy.deepcopy(M2); m['acceptance']['historical']['baseline_commit'] = 'f' * 40
    r.check(any('tidak ada di repositori' in e for e in trust_errors('02', m, a, DL, G)[0]), 'jangkar: commit historis tidak ada ditolak')
    m = copy.deepcopy(M1); m['acceptance']['historical']['baseline_commit'] = A['02']['baseline_commit']
    r.check(any('penggantian baseline' in e for e in trust_errors('01', m, A, DL, G)[0]), 'jangkar: baseline modul lain (W1 ← PR #27) ditolak')
    a = copy.deepcopy(A); a['02']['baseline_commit'] = head; m = copy.deepcopy(M2); m['acceptance']['historical']['baseline_commit'] = head
    r.check(any('bukan merge PR' in e for e in trust_errors('02', m, a, DL, G)[0]), 'jangkar: jangkar dan modul sama-sama diganti → bukan merge PR, ditolak')
    m = copy.deepcopy(M5); m['status']['owner_accepted'] = 'YES'; m['acceptance'] = {'historical': {'id': 'W09-ACC', 'baseline_commit': head}}
    r.check(any('tanpa jangkar' in e for e in trust_errors('09', m, A, DL, G)[0]), 'jangkar: promosi penerimaan modul tanpa jangkar (W9) ditolak')
    r.check(any('catatan keputusan owner' in e for e in trust_errors('02', M2, A, DL.replace('| W02-ACC | OWNER ACCEPTED', '| W02-ACC | PROPOSED'), G)[0]), 'jangkar: catatan keputusan owner hilang ditolak')
    a = copy.deepcopy(A); a['02']['baseline_commit'] = '846051f'
    m = copy.deepcopy(M2); m['acceptance']['historical']['baseline_commit'] = '846051f'
    r.check(any('SHA penuh' in e for e in trust_errors('02', m, a, DL, G)[0]), 'jangkar: SHA pendek ditolak')
    return 8

def main():
    r = Report('penerimaan')
    pend = acc_n = 0
    A = load_anchors(); DL = (ROOT / 'docs/DECISIONS_LOG.md').read_text(encoding='utf-8'); G = Git()
    for m in ('01', '02', '03', '04', '05', '06', '07', '08'):
        M = load(f'mod-w{m}/module.yaml'); st = M['status']['owner_accepted']
        terr, trusted = trust_errors(m, M, A, DL, G)
        for e in terr: r.check(False, e)
        r.check(True, f'W{m}: jangkar penerimaan')
        if (st is True or st == 'YES') and trusted is None:
            print(f'  W{m}: jangkar penerimaan GAGAL — perbandingan baseline dilewati'); continue
        if st is True or st == 'YES':
            a = M.get('acceptance')
            if not r.check(a is not None and a['historical'].get('baseline_commit'), f'W{m}: blok acceptance/baseline_commit'): continue
            r.check(a['historical']['id'] == f'W{m}-ACC', f'W{m}: id historis')
            bc = trusted   # R6-01: baseline dari jangkar tepercaya, bukan dari module.yaml
            rerr, rev = revision_trust(m, M, A, DL, G)
            for e in rerr: r.check(False, e)
            rv = baseline_variants(m, rev['reviewed_head']) if rev else None
            err, changed = validate(m, current_variants(m), baseline_variants(m, bc), a, current_shared(m), baseline_shared(m, bc), rev, rv)
            ents = a.get('revised_variants') or []
            pend += sum(e.get('owner_acceptance') == 'PENDING' for e in ents); acc_n += sum(e.get('owner_acceptance') == 'ACCEPTED' for e in ents)
            for e in err: r.check(False, f'W{m}: {e}')
            r.check(True, f'W{m}: perbandingan baseline')
            kind = 'HEAD review' if A[m].get('basis') == 'accepted_review_head' else 'merge'
            print(f'  W{m}: baseline tepercaya {bc[:7]} ({kind} PR #{A[m]["pr"]}, {A[m]["acceptance_id"]}); varian berubah {len(changed)}; revisi PENDING {sum(e.get("owner_acceptance") == "PENDING" for e in ents)}, ACCEPTED {sum(e.get("owner_acceptance") == "ACCEPTED" for e in ents)}')
        else:
            r.check(not (M.get('acceptance') or {}).get('historical'), f'W{m}: belum diterima, tidak boleh ada penerimaan historis')
            print(f'  W{m}: belum diterima owner')
    print(f'  total varian revisi W1–W4: PENDING {pend}, ACCEPTED {acc_n}')
    mutation_tests(r)
    print('  uji validator: 33 kasus — 27 mutasi terdeteksi, 6 kasus sah diterima (data PENDING; versi historis 2.0; revisi 2.0 → 3.0; field bersama berubah + semua varian tercatat; lokasi asli; penerimaan revisi PR #28 ACC)')
    nt = trust_tests(r)
    print(f'  uji jangkar R6-01: {nt} kasus — 7 penolakan, 1 penerimaan (baseline sah)')
    return r.done()

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
