"""R3-01/R3-02 + PR28-06: bangun (atau --check) docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md dari data cakupan
dan butir nyata. Bukti QC-13: (a) satu lokasi wajib menilai di semua varian / proyek; (b) bukti deterministik setara
atas semua jalur sah (varian berkorelasi antarslot dalam satu komponen menurut VA-2)."""
import re, sys
from pathlib import Path
from lib import ROOT, load, Report
from coverage_data import D
from equivalence_notes import N
from coverage_elements import EL, ALT_EL

P = '*'
VARS = {'concept': {'A', 'B'}, 'theory': {'A', 'B'}, 'lab': {'A', 'B'}, 'project': {P}}
OUT = ROOT / 'docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md'

def covers(c):
    return set('AB') if c == 'AB' else ({P} if c == P else set(c))

def _proof(ccov, alts):
    comp = {}
    if ccov: comp.setdefault('concept', []).append(('slot concept', covers(ccov)))
    for a in alts: comp.setdefault(a[0], []).append((a[1], covers(a[2])))
    single = [(c, l) for c, ls in comp.items() for l, s in ls if s >= VARS[c]]
    if single: return '(a) ' + '; '.join(f'{c} {l}' for c, l in single)
    corr = [c for c, ls in comp.items() if set().union(*[s for _, s in ls]) >= VARS[c]]
    if corr: return '(b) berkorelasi VA-2 dalam komponen: ' + ', '.join(corr)
    return None

def verdict(ccov, alts):
    """Bukti JALUR (matematis) dari anotasi. Status PASS hanya bila bukti jalur terpenuhi memakai lokasi
    berbukti semantik 'kuat'; bila hanya terpenuhi dengan lokasi 'lemah' → OPEN."""
    strong = [a for a in alts if (a[3] if len(a) > 3 else 'kuat') == 'kuat']
    p = _proof(ccov, strong)
    if p: return 'PASS', p
    p = _proof(ccov, alts)
    if p: return 'OPEN', p + ' — hanya dengan bukti semantik lemah'
    return 'GAP', 'tidak ada bukti (a) atau (b)'

# ---- validasi referensi lokasi (STRUKTUR) ----
import re as _re
def _expand(prefix, a, b):
    return [f'{prefix}c{i:02d}' for i in range(int(a), int(b) + 1)]

def resolve(m, comp, loc, var):
    """Pastikan lokasi ada dan merupakan kriteria bernilai; kembalikan jenis kriteria."""
    if comp == 'theory':
        d = load(f'mod-w{m}/theory/items/{loc}.yaml')
        ids = {v['variant_id'][-2:] for v in d['variants']}
        need = {'v' + x for x in var} if var != P else set()
        if not need <= ids: raise KeyError(f'{loc}: varian {need - ids}')
        fmt = d['format']
        return {'TF-1': 'kunci pilihan tunggal', 'TF-2': 'setiap opsi dinilai', 'TF-3': 'isian', 'TF-4': 'kunci pilihan', 'TF-5': 'urutan'}[fmt]
    if comp == 'lab':
        mm = _re.fullmatch(r'(act-0\d)\.c(\d\d)(?:–c(\d\d))?', loc)
        act, a, b = mm.group(1), mm.group(2), mm.group(3) or mm.group(2)
        d = load(f'mod-w{m}/lab/{act}/checks.yaml')
        for x in var:
            v = [v for v in d['variants'] if v['variant_id'].endswith('.v' + x)][0]
            have = {c['check_id'].split('.')[-1] for c in v['checks']}
            for c in _expand('', a, b):
                if c not in have: raise KeyError(f'{act} v{x} {c}')
        return 'pemeriksaan lab'
    if comp == 'project':
        rb = load(f'mod-w{m}/project/rubric.yaml')
        ids = {c['id'].split('project.')[1] for K in ('K1', 'K2', 'K3') for c in rb['criteria'][K]['checks']}
        ids |= {q['id'].split('project.')[1] for q in rb['criteria']['K4']['items']}
        mm = _re.fullmatch(r'(K\d)\.c(\d\d)(?:–c(\d\d))?', loc)
        if mm:
            for c in _expand(mm.group(1) + '.', mm.group(2), mm.group(3) or mm.group(2)):
                if c not in ids: raise KeyError(c)
            return 'pemeriksaan proyek'
        if loc not in ids: raise KeyError(loc)
        return 'kunci K4'
    raise KeyError(comp)


# ---- R5-01: elemen bernilai tepat (STRUKTUR; makna = anotasi manual penulis) ----
def _var(d, x):
    return [v for v in d['variants'] if v['variant_id'].endswith('.v' + x)][0]

def concept_elements(m, s, idx, concept, cc, el_table=None):
    """Kembalikan (deskripsi, kesalahan) elemen bernilai slot concept untuk varian di `cc`."""
    el_table = EL if el_table is None else el_table
    d = load(f'mod-w{m}/concept/items/{s}.yaml'); fmt = d['format']
    ann = (el_table.get(m, {}).get(s) or [None] * 99)[idx] or {}
    vars_ = set(cc) if cc else set(); desc, err = [], []
    if fmt in ('CE-S1', 'CE-S5'):
        if ann: err.append(f'{s}: {fmt} tidak boleh memakai anotasi elemen (CE-S1 hanya kunci; CE-S5 hanya baris salah + koreksi) {ann}')
        for x in sorted(vars_):
            v = _var(d, x)
            desc.append(f'v{x} kunci {v["key"]}' if fmt == 'CE-S1' else f'v{x} baris salah {v["error_line"]} + koreksi {v["correction_key"]}')
        return desc, err
    if set(ann) != vars_: err.append(f'{s} "{concept}": varian anotasi {sorted(ann)} ≠ cakupan {sorted(vars_)}')
    for x, ids in sorted(ann.items()):
        v = _var(d, x)
        pool = {'CE-S2': [o['id'] for o in v.get('options', [])], 'CE-S3': [i['id'] for i in v.get('items', [])],
                'CE-S4': [l['id'] for l in v.get('left', []) if l['id'] in v.get('key_mapping', {})]}[fmt]
        bad = [i for i in ids if i not in pool]
        if not ids or bad: err.append(f'{s} v{x}: elemen tidak ada/tidak dinilai {bad or ids}')
        kind = {'CE-S2': 'opsi dinilai', 'CE-S3': 'item urutan', 'CE-S4': 'pasangan'}[fmt]
        desc.append(f'v{x} {kind} {",".join(ids)}')
    return desc, err

def alt_elements(m, concept, comp, loc, var, alt_table=None):
    alt_table = ALT_EL if alt_table is None else alt_table
    err, desc = [], []
    if comp == 'theory':
        d = load(f'mod-w{m}/theory/items/{loc}.yaml'); fmt = d['format']; ann = alt_table.get((m, concept, comp, loc))
        for x in sorted(set(var)):
            v = _var(d, x)
            if fmt in ('TF-1', 'TF-4'):
                if ann: err.append(f'{loc}: {fmt} pilihan tunggal — hanya kunci yang dihitung; anotasi pengecoh ditolak {ann}')
                desc.append(f'v{x} kunci {v["key"]}')
            elif fmt == 'TF-2':
                ids = (ann or {}).get(x)
                pool = [o['id'] for o in v['options']]
                if not ids or any(i not in pool for i in ids): err.append(f'{loc} v{x}: opsi TF-2 tidak dianotasi/tidak ada {ids}')
                else: desc.append(f'v{x} opsi dinilai {",".join(ids)}')
            elif fmt == 'TF-3':
                if not v.get('accepted_answers'): err.append(f'{loc} v{x}: isian tanpa jawaban')
                desc.append(f'v{x} isian {v["accepted_answers"][0]}')
            else:
                desc.append(f'v{x} {fmt}')
    elif comp == 'lab':
        mm = _re.fullmatch(r'(act-0\d)\.c(\d\d)(?:–c(\d\d))?', loc)
        act, a, b = mm.group(1), mm.group(2), mm.group(3) or mm.group(2)
        d = load(f'mod-w{m}/lab/{act}/checks.yaml')
        for x in sorted(set(var)):
            v = _var(d, x); have = {c['check_id'].split('.')[-1]: c for c in v['checks']}
            for c in _expand('', a, b):
                ck = have.get(c)
                if not ck or not ck.get('points') or not (ck.get('accepted_answers') or ck.get('expected') or ck.get('accepted_sequences')):
                    err.append(f'lab {act} v{x} {c}: pemeriksaan tidak ada/tidak dinilai')
            desc.append(f'v{x} {act}.c{a}' + (f'–c{b}' if b != a else ''))
    elif comp == 'project':
        rb = load(f'mod-w{m}/project/rubric.yaml')
        pts = {c['id'].split('project.')[1]: c['points'] for K in ('K1', 'K2', 'K3') for c in rb['criteria'][K]['checks']}
        pts.update({q['id'].split('project.')[1]: (q['points'] if q.get('key') else 0) for q in rb['criteria']['K4']['items']})
        mm = _re.fullmatch(r'(K\d)\.c(\d\d)(?:–c(\d\d))?', loc)
        ids = _expand(mm.group(1) + '.', mm.group(2), mm.group(3) or mm.group(2)) if mm else [loc]
        for i in ids:
            if not pts.get(i): err.append(f'proyek {i}: kriteria tidak ada/tanpa poin')
        desc.append(('kriteria ' if mm else 'kunci ') + ','.join(ids))
    return desc, err

def element_mutation_tests(rep):
    """Uji positif/negatif validator elemen (R5-01)."""
    ok = lambda r: not r[1]
    rep.check(ok(concept_elements('05', 's02', 0, 'variabel', 'AB')), 'elemen: CE-S2 sah diterima')
    rep.check(not ok(concept_elements('05', 's02', 0, 'variabel', 'AB', {'05': {'s02': [{'A': ['z'], 'B': ['a']}]}})), 'elemen: ID opsi tidak ada ditolak')
    rep.check(not ok(concept_elements('05', 's04', 0, 'x', 'AB', {'05': {'s04': [{'A': ['a'], 'B': ['a']}]}})), 'elemen: pengecoh CE-S1 sebagai bukti ditolak')
    rep.check(not ok(concept_elements('05', 's03', 0, 'x', 'AB', {'05': {'s03': [{'A': ['1'], 'B': ['1']}]}})), 'elemen: baris benar CE-S5 sebagai bukti ditolak')
    rep.check(not ok(concept_elements('05', 's02', 0, 'variabel', 'AB', {'05': {'s02': [{'A': ['a']}]}})), 'elemen: varian tanpa elemen ditolak')
    rep.check(not ok(concept_elements('05', 's01', 0, 'x', 'AB', {'05': {'s01': [{'A': ['L9'], 'B': ['L1']}]}})), 'elemen: pasangan tidak ada ditolak')
    rep.check(not ok(alt_elements('02', 'x', 'theory', 's03', 'AB', {('02', 'x', 'theory', 's03'): {'A': ['a']}})), 'elemen: pengecoh TF-1 sebagai bukti ditolak')
    rep.check(not ok(alt_elements('02', 'x', 'theory', 's02', 'AB', {})), 'elemen: TF-2 tanpa opsi ditolak')
    rep.check(not ok(alt_elements('03', 'x', 'lab', 'act-02.c09', 'AB')), 'elemen: pemeriksaan lab tidak ada ditolak')
    rep.check(not ok(alt_elements('03', 'x', 'project', 'K1.c99', P)), 'elemen: kriteria proyek tidak ada ditolak')
    rep.check(ok(alt_elements('03', 'x', 'lab', 'act-02.c06–c08', 'AB')), 'elemen: pemeriksaan lab sah diterima')

def va2_correlated(n_slots=20, attempts=8):
    """Simulasi VA-2 (D-30): per slot, pilih varian dengan pemakaian paling sedikit dalam riwayat komponen;
    seri → bukan varian attempt sebelumnya; masih seri → indeks terkecil. Setiap attempt komponen memuat semua
    slot (blueprint teori 20 slot; concept 6 slot; lab RA-1 seluruh komponen), sehingga riwayat semua slot sama."""
    hist = {s: [] for s in range(n_slots)}; seq = []
    for _ in range(attempts):
        pick = {}
        for s, h in hist.items():
            use = {v: h.count(v) for v in 'AB'}; low = min(use.values())
            cand = [v for v in 'AB' if use[v] == low]
            if len(cand) > 1 and h: cand = [v for v in cand if v != h[-1]] or cand
            pick[s] = sorted(cand)[0]
        for s in hist: hist[s].append(pick[s])
        seq.append(set(pick.values()))
    return all(len(x) == 1 for x in seq), [x.pop() for x in seq]

def structure(fmt, v):
    if fmt == 'CE-S4': return f"{len(v['left'])} pasangan, {len(v['right'])} pilihan kanan"
    if fmt == 'CE-S3': return f"{len(v['items'])} langkah, {len(v['accepted_sequences'])} urutan diterima"
    if fmt == 'CE-S5': return f"{len(v['lines'])} baris, {len(v['correction_options'])} perbaikan"
    if fmt == 'CE-S2': return f"{len(v['options'])} pernyataan, {len(v['key'])} benar"
    if fmt == 'CE-S1': return f"{len(v['options'])} pilihan, 1 kunci"
    return '?'

def words(v):
    t = [v['stem']]
    for k in ('options', 'left', 'right', 'items', 'lines', 'correction_options'):
        t += [x['text'] for x in v.get(k, [])]
    return len(' '.join(t).split())

def build():
    rep = Report('cakupan')
    # RC tidak dihapus/diubah; uji metode
    for m, rows in D.items():
        for i in range(1, 7):
            s = f's0{i}'; rc = load(f'mod-w{m}/concept/items/{s}.yaml')['required_concepts']
            rep.check([r[1] for r in rows if r[0] == s] == rc, f'W{m} {s}: konsep wajib data ≠ berkas')
    rep.check(verdict('A', [])[0] == 'GAP', 'uji negatif: hanya varian A')
    rep.check(verdict('A', [('theory', 'sX', 'A')])[0] == 'GAP', 'uji negatif: varian A di dua komponen')
    rep.check(verdict('B', [('lab', 'c01', 'AB')])[0] == 'PASS', 'uji positif: lab kedua varian')
    rep.check(verdict('', [('theory', 's1', 'A'), ('theory', 's2', 'B')])[1].startswith('(b)'), 'uji bukti (b) berkorelasi')
    rep.check(verdict('', [('project', 'K4.q1', P, 'lemah')])[0] == 'OPEN', 'uji: hanya bukti semantik lemah → OPEN')
    element_mutation_tests(rep)
    ok, seq = va2_correlated()
    rep.check(ok and seq == ['A', 'B'] * 4, f'VA-2: indeks varian sama untuk semua slot di setiap attempt {seq}')
    rows_md, tot, gaps, nb, opens = [], {}, [], 0, []
    for m, rows in D.items():
        M = load(f'mod-w{m}/module.yaml'); c2lo = {lo['competency']: lo['id'] for lo in M['learning_objectives']}
        for s, c, k, cc, alts, note in rows:
            comp = load(f'mod-w{m}/concept/items/{s}.yaml')['competency']
            ci = [r[1] for r in rows if r[0] == s].index(c)
            cdesc, cerr = concept_elements(m, s, ci, c, cc)
            for e in cerr: rep.check(False, f'W{m} {e}')
            rep.check(True, 'elemen concept')
            adesc = []
            for a in alts:
                dsc, er = alt_elements(m, c, a[0], a[1], a[2])
                for e in er: rep.check(False, f'W{m} {c}: {e}')
                adesc.append('; '.join(dsc))
            kinds = []
            for a in alts:
                try:
                    kinds.append(resolve(m, a[0], a[1], a[2])); rep.check(True, 'referensi lokasi')
                except Exception as ex:
                    rep.check(False, f'W{m} {s} {c}: referensi tidak valid {a}: {ex}'); kinds.append('?')
            v, why = verdict(cc, alts)
            nb += why.startswith('(b)')
            tot.setdefault(m, [0, 0]); tot[m][0] += 1; tot[m][1] += v == 'PASS'
            if v == 'GAP': gaps.append((m, s, c))
            if v == 'OPEN': opens.append((m, s, c))
            loc = '; '.join(f'{a[0]} {a[1]} [{ad}] ({kd}; semantik {a[3] if len(a) > 3 else "kuat"})' for a, kd, ad in zip(alts, kinds, adesc)) or '—'
            rows_md.append(f'| W{int(m)} | {c2lo[comp]} | {s} | {c} | {k} | {"; ".join(cdesc) or "—"} | {loc} | {why} | sama (VA-2 bergiliran) | {note or "pembacaan butir"} | {v} |')
    # register kesetaraan 48 slot (penilaian penulis; rasio kata hanya penyaring)
    eq, eq_open = [], []
    for m in D:
        M = load(f'mod-w{m}/module.yaml'); c2lo = {lo['competency']: lo['id'] for lo in M['learning_objectives']}
        for i in range(1, 7):
            s = f's0{i}'; d = load(f'mod-w{m}/concept/items/{s}.yaml'); A, B = d['variants']
            sa, sb = structure(d['format'], A), structure(d['format'], B)
            wa, wb = words(A), words(B); ratio = max(wa, wb) / min(wa, wb)
            comp_txt, ba, bb, cmp_txt, st = N[m][s]
            rep.check(st in ('PASS', 'OPEN'), f'W{m} {s}: status register')
            screen = 'perlu ditinjau' if ratio > 1.6 else 'tidak ditandai'
            if st == 'OPEN': eq_open.append((m, s))
            rev = ', '.join(f'v{x["variant_id"][-1]} {x["item_version"]}' for x in (A, B) if str(x['item_version']) != '1.0') or '—'
            eq.append(f'| W{int(m)} {s} | {c2lo[d["competency"]]} — {comp_txt} | {d["format"]}, {d["max_points"]} poin (slot) | '
                      f'vA: {ba} ({sa}) | vB: {bb} ({sb}) | {cmp_txt} | {wa} vs {wb} kata, rasio {ratio:.2f} → {screen}; '
                      f'tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | {rev} | {st} |')
    N_ = sum(x[0] for x in tot.values()); Pn = sum(x[1] for x in tot.values())
    head = open(Path(__file__).with_name('matrix_header.md'), encoding='utf-8').read()
    summ = ['| Modul | Konsep wajib | PASS | GAP | OPEN |', '|---|---|---|---|---|']
    summ += [f'| W{int(m)} | {n} | {p} | {sum(1 for g in gaps if g[0] == m)} | {sum(1 for o in opens if o[0] == m)} |' for m, (n, p) in tot.items()]
    summ.append(f'| **Total** | **{N_}** | **{Pn}** | **{len(gaps)}** | **{len(opens)}** |')
    head = head.replace('{{DECISIONS_LOG_LINK}}', '[DECISIONS_LOG.md](DECISIONS_LOG.md)')
    txt = head.replace('{{SUMMARY}}', '\n'.join(summ)).replace('{{NB}}', str(nb)).replace('{{GAPS}}', str(len(gaps)))
    txt = txt.replace('{{EQ_PASS}}', str(48 - len(eq_open))).replace('{{EQ_OPEN}}', str(len(eq_open))).replace('{{COV_OPEN}}', str(len(opens)))
    txt += '\n## 5. Matriks per konsep\n\n| Modul | LO | Slot | Konsep wajib | Kelas | Concept (elemen bernilai) | Lokasi wajib lain [elemen bernilai] | Jaminan jalur (QC-13) | Remedial | Bukti/catatan | Status |\n|---|---|---|---|---|---|---|---|---|---|---|\n'
    txt += '\n'.join(rows_md) + '\n'
    txt += ('\n## 6. Register kesetaraan kompetensi inti (48 slot concept, R3-02)\n\n'
            'Register ini adalah **penilaian semantik penulis** (`equivalence_notes.py`), bukan bukti otomatis. '
            'Format dan poin maksimum ditetapkan per slot (sama untuk kedua varian); struktur dihitung dari butir. '
            'Kesamaan ID kompetensi, format, atau rasio kata **tidak** dipakai sebagai bukti kesetaraan; rasio kata hanya '
            'penyaring. Bank concept tidak memiliki field kesulitan atau waktu per varian; durasi tidak diuji pelajar.\n\n'
            '| Slot | LO — kompetensi bernilai bersama | Format, poin | Perilaku bernilai vA | Perilaku bernilai vB | Perbandingan tuntutan kognitif | Penyaring kompleksitas/waktu | Versi revisi | Status |\n'
            '|---|---|---|---|---|---|---|---|---|\n' + '\n'.join(eq) + '\n')
    return rep, txt, gaps, eq_open, opens

def main():
    rep, txt, gaps, eq_open, opens = build()
    if '--write' in sys.argv:
        OUT.write_text(txt, encoding='utf-8')
    else:
        rep.check(OUT.read_text(encoding='utf-8') == txt, 'dokumen matriks tidak sesuai hasil generator (jalankan --write)')
    print(f'  konsep {sum(len(v) for v in D.values())}; PASS {sum(len(v) for v in D.values()) - len(gaps) - len(opens)}; OPEN (semantik lemah) {len(opens)} {opens}; GAP {len(gaps)}; kesetaraan PASS {48 - len(eq_open)}, OPEN {len(eq_open)} {eq_open}')
    print('  SEMANTIK: bukti "lokasi menilai konsep" dan register kesetaraan = penilaian penulis (tidak diverifikasi otomatis)')
    return rep.done()

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
