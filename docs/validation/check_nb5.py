"""PR28-02: kontrak NB-5 (N1–N6) — fixture terikat butir, pemindaian konsumen W5–W6, uji mutasi, F-51 W3."""
import glob, re, sys, yaml
from pathlib import Path
from lib import CUR, load, nb5, nb5_content_errors, Report

def find(file, ident):
    d = load(file)
    if 'variants' in d and d['variants'] and 'checks' in d['variants'][0]:
        for var in d['variants']:
            for c in var['checks']:
                if c['check_id'] == ident:
                    return c['accepted_answers'], d['normalization']
    for v in d['variants']:
        if v.get('variant_id') == ident:
            return v['accepted_answers'], v['normalization']
    raise KeyError(ident)

# Pemeriksaan non-NB-5 di lab W6 (BN-6, B01, pilihan) — R7-02: kini hanya acuan regresi; konsumen diturunkan dari deklarasi normalization
W6_NOT_NB5 = {'act-01': {'c05', 'c06', 'c07'}, 'act-02': {'c01', 'c02', 'c03', 'c04', 'c06'}, 'act-03': {'c01', 'c02', 'c03', 'c04', 'c05'}}
WORD = {'satu': 1, 'dua': 2, 'tiga': 3}

# R7-02: konsumen lab dikenali dari deklarasi `normalization` berkas (segmen "cNN[–cMM], …: <kontrak>";
# teks sebelum segmen pertama = kontrak bawaan), BUKAN dari isi accepted_answers.
_SEG = re.compile(r'(?:^|(?<=\. ))((?:c\d\d(?:–c\d\d)?)(?:, c\d\d(?:–c\d\d)?)*): ')

def lab_contracts(norm):
    ms = list(_SEG.finditer(norm)); default = norm[:ms[0].start()] if ms else norm; per = {}
    for i, m in enumerate(ms):
        seg = norm[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(norm)]
        for part in m.group(1).split(', '):
            a, _, b = part.partition('–'); b = b or a
            for n in range(int(a[1:]), int(b[1:]) + 1): per[f'c{n:02d}'] = seg
    return default, per

def consumers(modules=('05', '06'), root=CUR):
    """Kumpulkan konsumen NB-5. R6-05: tidak ada akses tanpa pemeriksaan ke accepted_answers[0];
    konsumen dengan konten cacat tetap dikembalikan agar audit melaporkannya sebagai CONTENT_ERROR."""
    out = []
    for m in modules:
        for f in sorted(glob.glob(str(root / f'mod-w{m}/theory/items/*.yaml'))):
            rel = f[len(str(root)) + 1:]
            for v in (yaml.safe_load(open(f, encoding='utf-8')) or {}).get('variants') or []:
                if 'NB-5' in str(v.get('normalization', '')):
                    out.append((v.get('variant_id', '?'), str(v.get('stem', '')), v.get('accepted_answers'), str(v.get('normalization', '')), None, rel))
        for f in sorted(glob.glob(str(root / f'mod-w{m}/lab/act-0*/checks.yaml'))):
            rel = f[len(str(root)) + 1:]
            d = yaml.safe_load(open(f, encoding='utf-8')) or {}
            default, per = lab_contracts(str(d.get('normalization', '')))
            for var in d.get('variants') or []:
                for c in var.get('checks') or []:
                    cid = str(c.get('check_id', '?'))
                    if 'NB-5' not in per.get(cid[-3:], default):
                        continue   # pemeriksaan bukan NB-5 menurut deklarasi berkas
                    acc = c.get('accepted_answers')   # hilang/kosong/cacat → CONTENT_ERROR di audit
                    out.append((cid, str(c.get('question', '')), acc, str(d.get('normalization', '')),
                                str(d.get('answer_validation', '')) + ' ' + str(d.get('infrastructure', '')), rel))
    return out

def audit(items):
    find_ = []
    for it in items:
        iid, stem, acc, norm, val = it[:5]; rel = it[5] if len(it) > 5 else '?'
        ce = nb5_content_errors(acc)
        if ce:   # R6-05: konten divalidasi sebelum menurunkan kanonik, presisi, atau afiks
            find_.append((iid, f'CONTENT_ERROR [{rel}]: ' + '; '.join(ce))); continue
        acc = [str(a) for a in acc]
        if 'N1–N6' not in norm:
            find_.append((iid, 'teks normalisasi belum kontrak N1–N6')); continue
        canon = acc[0]
        if not re.fullmatch(r'-?(?:0|[1-9]\d*)(?:,\d+)?', canon.replace('−', '-')):
            find_.append((iid, f'bentuk kanonik pertama bukan angka polos: {canon}'))
        for a in acc:
            r = nb5(a, acc)
            if r != 'ACCEPT':
                find_.append((iid, f'accepted_answers "{a}" tidak lolos N1–N6 ({r})'))
        dec = len(canon.split(',')[1]) if ',' in canon else 0
        mm = re.search(r'\*\*(satu|dua|tiga)\*\* angka|(satu|dua|tiga) angka (di belakang koma|desimal)', stem)
        req = WORD[(mm.group(1) or mm.group(2))] if mm else 0
        if req != dec:
            find_.append((iid, f'presisi: soal meminta {req}, kanonik {dec}'))
        neg = canon.startswith(('-', '−'))
        for a in acc:
            if re.sub(r'^Rp ?', '', a).startswith(('-', '−')) != neg:
                find_.append((iid, f'tanda tidak konsisten: {a}'))
            num = re.fullmatch(r'(?:Rp ?)?([-−]?[\d.,]+).*', a).group(1)
            if '.' in num and not re.fullmatch(r'[-−]?[1-9]\d{0,2}(?:\.\d{3})+(?:,\d+)?', num):
                find_.append((iid, f'pengelompokan ribuan salah: {a}'))
        rp = [a for a in acc if a.startswith('Rp')]
        if rp and not re.search(r'Rp|rupiah', stem):
            find_.append((iid, 'Rp diterima tetapi soal tidak menyebut rupiah'))
        for a in rp:
            if nb5(a.replace('Rp', 'rp', 1), acc) == 'ACCEPT':
                find_.append((iid, '`rp` huruf kecil diterima (harus ditolak)'))
        sufs = {re.fullmatch(r'(?:Rp ?)?[-−]?[\d.,]+ ?(.*)', a).group(1) for a in acc} - {''}
        for s in sufs:
            if s not in ('%', 'g', 'gram', 'persen') and not re.search(re.escape(s), stem, re.I):
                find_.append((iid, f'akhiran "{s}" tidak tertulis di soal'))
        if val is not None and 'EVALUATION_ERROR' not in val:
            find_.append((iid, 'lab tanpa pembeda EVALUATION_ERROR'))
    return find_

def scan(root):
    """Pemindaian ujung-ke-ujung: kembalikan (konsumen, temuan) tanpa exception tak tertangani."""
    items = consumers(root=root)
    return items, audit(items)

def scanner_mutation_tests(r):
    """R6-05: salin W5–W6 ke direktori sementara, suntikkan konten cacat, jalankan pemindai dan CLI."""
    import shutil, tempfile, subprocess
    cases = [('kosong', 'theory', lambda v: v.__setitem__('accepted_answers', [])),
             ('hilang', 'theory', lambda v: v.pop('accepted_answers')),
             ('bukan daftar', 'theory', lambda v: v.__setitem__('accepted_answers', '204000')),
             ('entri cacat', 'theory', lambda v: v.__setitem__('accepted_answers', [None, '204000'])),
             ('kanonik tidak sah', 'theory', lambda v: v.__setitem__('accepted_answers', ['0204000'])),
             ('lab hilang', 'lab', lambda c: c.pop('accepted_answers')),
             ('lab kosong', 'lab', lambda c: c.__setitem__('accepted_answers', [])),
             ('lab jawaban pertama teks', 'lab', lambda c: c.__setitem__('accepted_answers', ['lima ribu', '5000'])),
             ('lab null', 'lab', lambda c: c.__setitem__('accepted_answers', None)),
             ('lab tipe tak terduga', 'lab', lambda c: c.__setitem__('accepted_answers', {'a': '5000'})),
             ('lab entri dict', 'lab', lambda c: c.__setitem__('accepted_answers', [{'x': 1}]))]
    n = 0
    for name, kind, mut in cases:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / 'curriculum'
            for m in ('05', '06'): shutil.copytree(CUR / f'mod-w{m}', root / f'mod-w{m}')
            if kind == 'theory':
                f = root / 'mod-w05/theory/items/s15.yaml'; d = yaml.safe_load(open(f, encoding='utf-8')); mut(d['variants'][0]); want = 'mod-w05.theory.s15.vA'
            else:
                f = root / 'mod-w05/lab/act-01/checks.yaml'; d = yaml.safe_load(open(f, encoding='utf-8'))
                c = [c for c in d['variants'][0]['checks'] if c['check_id'].endswith('.c01')][0]; mut(c); want = c['check_id']
            yaml.safe_dump(d, open(f, 'w', encoding='utf-8'), allow_unicode=True, sort_keys=False)
            try:
                items, fnd = scan(root); exc = None
            except Exception as e:  # noqa
                fnd, exc = [], e
            ok = exc is None and any(i == want and t.startswith('CONTENT_ERROR [') for i, t in fnd)
            ok &= not any(t.startswith(('WRONG', 'INVALID')) for _, t in fnd)
            r.check(ok, f'pemindai: konten cacat "{name}" → CONTENT_ERROR terkendali ({exc!r})', 'REGRESI'); n += 1
            if name == 'kosong':   # CLI: kegagalan terkendali, exit 1, tanpa traceback
                p = subprocess.run([sys.executable, __file__, '--scan-root', str(root)], capture_output=True, text=True)
                r.check(p.returncode == 1 and 'Traceback' not in p.stderr and 'CONTENT_ERROR' in p.stdout, f'pemindai CLI: exit {p.returncode}, traceback {"Traceback" in p.stderr}', 'REGRESI'); n += 1
    # pemeriksaan non-NB-5 yang sah tetap dikecualikan (W5 c06 nama hari; W6 B01/BN-6/pilihan)
    ids = {i[0] for i in consumers()}
    r.check('mod-w05.lab.act-01.vA.c06' not in ids, 'pemindai: pemeriksaan teks W5 act-01 c06 tetap dikecualikan', 'REGRESI'); n += 1
    w6 = {i[0].split('.')[2] + '.' + i[0][-3:] for i in consumers(('06',))}
    r.check(not any(f'{a}.{c}' in w6 for a, cs in W6_NOT_NB5.items() for c in cs), 'pemindai: pemeriksaan non-NB-5 W6 tetap dikecualikan', 'REGRESI'); n += 1
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / 'curriculum'
        for m in ('05', '06'): shutil.copytree(CUR / f'mod-w{m}', root / f'mod-w{m}')
        p = subprocess.run([sys.executable, __file__, '--scan-root', str(root)], capture_output=True, text=True)
        r.check(p.returncode == 0 and 'Traceback' not in p.stderr, f'pemindai CLI: salinan sah exit {p.returncode}', 'REGRESI'); n += 1
    return n

def main():
    r = Report('NB-5')
    fx = yaml.safe_load(open(__file__.replace('check_nb5.py', 'fixtures/nb5_fixtures.yaml'), encoding='utf-8'))
    for f in fx:
        if 'synthetic' in f:
            got = nb5(f['input'], f['synthetic'])
        else:
            acc, norm = find(f['file'], f['id'])
            r.check('N1–N6' in norm, f"{f['id']}: kontrak N1–N6 tidak ada di teks normalisasi")
            got = nb5(f['input'], acc)
        r.check(got == f['expected'], f"{f.get('id', 'sintetis')} {f['input']!r}: {got} ≠ {f['expected']}", 'REGRESI')
    print(f'  fixture NB-5: {len(fx)}')
    # R5-04: konten cacat tidak boleh menghasilkan exception atau WRONG/INVALID
    bad_acc = [None, 5, 'x', [], [None], [[]], [True], ['', '5'], ['5', None], ['Rp'], ['1.2.3'], ['5', '6'], ['5,0', '5'], ['−0']]
    bad_raw = [None, 5, 5.0, b'5', ['5'], '', ' ', '5']
    for acc_ in bad_acc:
        for raw_ in bad_raw:
            try:
                got = nb5(raw_, acc_)
            except Exception as e:  # noqa
                got = f'EXCEPTION {type(e).__name__}'
            r.check(got == 'CONTENT_ERROR', f'konten cacat {acc_!r} / {raw_!r}: {got}', 'REGRESI')
    print(f'  kombinasi konten cacat: {len(bad_acc) * len(bad_raw)}')
    for f in yaml.safe_load(open(__file__.replace('check_nb5.py', 'fixtures/f51_fixtures.yaml'), encoding='utf-8')):
        acc, norm = find(f['file'], f['id'])
        r.check('peka huruf' in norm and 'N1–N6' not in norm, f"{f['id']}: kontrak F-51 berubah")
        got = 'ACCEPT' if f['input'].strip() in [str(a) for a in acc] else 'INVALID'
        r.check(got == f['expected'], f"F-51 {f['input']!r}: {got} ≠ {f['expected']}", 'REGRESI')
    items = consumers()
    nt = sum('.theory.' in i[0] for i in items); nl = sum('.lab.' in i[0] for i in items)
    print(f'  konsumen NB-5 W5–W6: {len(items)} (teori {nt}, lab {nl})')
    findings = audit(items)
    for x in findings:
        print('  TEMUAN', *x)
    r.check(not findings, f'{len(findings)} temuan pada konsumen NB-5')
    ce = [(i[0], e) for i in items for e in nb5_content_errors(i[2])]
    for x in ce: print('  KONTEN', *x)
    r.check(not ce, f'{len(ce)} konsumen NB-5 dengan konten cacat (CONTENT_ERROR)')
    # uji mutasi: pemeriksa harus menangkap cacat yang disuntikkan
    base = [i for i in items if i[0].endswith('mod-w05.theory.s15.vA')][0]
    s18 = [i for i in items if i[0].endswith('mod-w05.theory.s18.vA')][0]
    mut = [('MUT-presisi', s18[1], ['3,50'], s18[3], None), ('MUT-ribuan', base[1], ['204000', '20.4000'], base[3], None),
           ('MUT-tanda', base[1], ['204000', '-204000'], base[3], None), ('MUT-galat', 'x', ['5'], base[3], 'tanpa pembeda'),
           ('MUT-kontrak', base[1], ['204000'], 'cocokkan persis', None)]
    caught = {m[0] for m in audit(mut)}
    r.check(caught == {m[0] for m in mut}, f'uji mutasi tidak semua tertangkap: {caught}')
    print(f'  uji mutasi tertangkap: {len(caught)}/{len(mut)}')
    ns = scanner_mutation_tests(r)
    print(f'  uji pemindai ujung-ke-ujung R6-05/R7-02: {ns} (11 konten cacat, 2 pengecualian non-NB-5, 2 CLI)')
    return r.done()

if __name__ == '__main__':
    if '--scan-root' in sys.argv:
        _items, _f = scan(Path(sys.argv[sys.argv.index('--scan-root') + 1]))
        for x in _f: print('  TEMUAN', *x)
        print(f'konsumen {len(_items)}; temuan {len(_f)}')
        sys.exit(1 if _f else 0)
    sys.exit(0 if main() else 1)
