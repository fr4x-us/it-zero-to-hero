"""R3-01/R3-02 + PR28-06: bangun (atau --check) docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md dari data cakupan
dan butir nyata. Bukti QC-13: (a) satu lokasi wajib menilai di semua varian / proyek; (b) bukti deterministik setara
atas semua jalur sah (varian berkorelasi antarslot dalam satu komponen menurut VA-2)."""
import re, sys
from pathlib import Path
from lib import ROOT, load, Report
from coverage_data import D
from equivalence_notes import N

P = '*'
VARS = {'concept': {'A', 'B'}, 'theory': {'A', 'B'}, 'lab': {'A', 'B'}, 'project': {P}}
OUT = ROOT / 'docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md'

def covers(c):
    return set('AB') if c == 'AB' else ({P} if c == P else set(c))

def verdict(ccov, alts):
    comp = {}
    if ccov: comp.setdefault('concept', []).append(('slot concept', covers(ccov)))
    for c, loc, v in alts: comp.setdefault(c, []).append((loc, covers(v)))
    single = [(c, l) for c, ls in comp.items() for l, s in ls if s >= VARS[c]]
    if single: return 'PASS', '(a) ' + '; '.join(f'{c} {l}' for c, l in single)
    corr = [c for c, ls in comp.items() if set().union(*[s for _, s in ls]) >= VARS[c]]
    if corr: return 'PASS', '(b) berkorelasi VA-2 dalam komponen: ' + ', '.join(corr)
    return 'GAP', 'tidak ada bukti (a) atau (b)'

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
    rows_md, tot, gaps, nb = [], {}, [], 0
    for m, rows in D.items():
        M = load(f'mod-w{m}/module.yaml'); c2lo = {lo['competency']: lo['id'] for lo in M['learning_objectives']}
        for s, c, k, cc, alts, note in rows:
            comp = load(f'mod-w{m}/concept/items/{s}.yaml')['competency']
            v, why = verdict(cc, alts)
            nb += why.startswith('(b)')
            tot.setdefault(m, [0, 0]); tot[m][0] += 1; tot[m][1] += v == 'PASS'
            if v != 'PASS': gaps.append((m, s, c))
            loc = '; '.join(f'{a} {l} ({"vA+vB" if x == "AB" else ("tanpa varian" if x == P else "v" + x)})' for a, l, x in alts) or '—'
            rows_md.append(f'| W{int(m)} | {c2lo[comp]} | {s} | {c} | {k} | {dict(AB="vA+vB", A="vA", B="vB").get(cc, "—")} | {loc} | {why} | sama (VA-2 bergiliran) | {note or "pembacaan butir"} | {v} |')
    # register kesetaraan 48 slot
    eq, eq_open = [], []
    for m in D:
        M = load(f'mod-w{m}/module.yaml'); c2lo = {lo['competency']: lo['id'] for lo in M['learning_objectives']}
        for i in range(1, 7):
            s = f's0{i}'; d = load(f'mod-w{m}/concept/items/{s}.yaml'); A, B = d['variants']
            sa, sb = structure(d['format'], A), structure(d['format'], B)
            wa, wb = words(A), words(B); ratio = max(wa, wb) / min(wa, wb)
            note = N[m][s]; cores = {r[3] for r in D[m] if r[0] == s and r[2] == 'inti'}
            core_ok = all(any(x in (r[3] or '') for r in D[m] if r[0] == s and r[2] == 'inti') for x in 'AB')
            why = []
            if sa != sb: why.append('struktur berbeda')
            if ratio > 1.6: why.append(f'beban baca berbeda ({wa} vs {wb} kata)')
            if not core_ok: why.append('konsep inti tidak dinilai di kedua varian')
            if note.startswith('OPEN'): why.append('tuntutan kognitif')
            st = 'OPEN' if why else 'PASS'
            if st == 'OPEN': eq_open.append((m, s, why))
            rev = ', '.join(f'v{x["variant_id"][-1]} {x["item_version"]}' for x in (A, B) if str(x['item_version']) != '1.0') or '—'
            eq.append(f'| W{int(m)} {s} | {c2lo[d["competency"]]} / `{d["competency"]}` | {d["format"]}, {d["max_points"]} poin (slot) | '
                      f'vA: {A["stem"][:90].strip()}… — {sa} | vB: {B["stem"][:90].strip()}… — {sb} | {note} | '
                      f'{wa} vs {wb} kata (rasio {ratio:.2f}); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | {rev} | {st}{": " + "; ".join(why) if why else ""} |')
    N_ = sum(x[0] for x in tot.values()); Pn = sum(x[1] for x in tot.values())
    head = open(Path(__file__).with_name('matrix_header.md'), encoding='utf-8').read()
    summ = ['| Modul | Konsep wajib | PASS | GAP | OPEN |', '|---|---|---|---|---|']
    summ += [f'| W{int(m)} | {n} | {p} | {n - p} | 0 |' for m, (n, p) in tot.items()]
    summ.append(f'| **Total** | **{N_}** | **{Pn}** | **{N_ - Pn}** | **0** |')
    head = head.replace('{{DECISIONS_LOG_LINK}}', '[DECISIONS_LOG.md](DECISIONS_LOG.md)')
    txt = head.replace('{{SUMMARY}}', '\n'.join(summ)).replace('{{NB}}', str(nb)).replace('{{GAPS}}', str(len(gaps)))
    txt = txt.replace('{{EQ_PASS}}', str(48 - len(eq_open))).replace('{{EQ_OPEN}}', str(len(eq_open)))
    txt += '\n## 5. Matriks per konsep\n\n| Modul | LO | Slot | Konsep wajib | Kelas | Concept | Lokasi wajib lain | Jaminan jalur (QC-13) | Remedial | Bukti/catatan | Status |\n|---|---|---|---|---|---|---|---|---|---|---|\n'
    txt += '\n'.join(rows_md) + '\n'
    txt += ('\n## 6. Register kesetaraan kompetensi inti (48 slot concept, R3-02)\n\n'
            'Perilaku bernilai dikutip dari stem dan struktur butir; tuntutan kognitif dinilai penyusun. '
            'Format dan poin maksimum ditetapkan per slot (sama untuk kedua varian). Bank concept tidak memiliki field '
            'kesulitan atau waktu per varian; beban baca (jumlah kata stem + teks pilihan) dipakai sebagai proksi, '
            'bukan bukti waktu pelajar.\n\n'
            '| Slot | LO / kompetensi | Format, poin | Perilaku bernilai vA | Perilaku bernilai vB | Tuntutan kognitif | Kesulitan/waktu | Versi revisi | Status |\n'
            '|---|---|---|---|---|---|---|---|---|\n' + '\n'.join(eq) + '\n')
    return rep, txt, gaps, eq_open

def main():
    rep, txt, gaps, eq_open = build()
    if '--write' in sys.argv:
        OUT.write_text(txt, encoding='utf-8')
    else:
        rep.check(OUT.read_text(encoding='utf-8') == txt, 'dokumen matriks tidak sesuai hasil generator (jalankan --write)')
    print(f'  konsep {sum(len(v) for v in D.values())}; GAP {len(gaps)} {gaps}; kesetaraan OPEN {len(eq_open)} {eq_open}')
    return rep.done()

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
