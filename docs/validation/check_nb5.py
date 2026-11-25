"""PR28-02: kontrak NB-5 (N1–N6) — fixture terikat butir, pemindaian konsumen W5–W6, uji mutasi, F-51 W3."""
import glob, re, sys, yaml
from lib import CUR, load, nb5, Report

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

# Pemeriksaan non-NB-5 di lab W6 (BN-6, B01, pilihan) — dipisah dari NB-5
W6_NOT_NB5 = {'act-01': {'c05', 'c06', 'c07'}, 'act-02': {'c01', 'c02', 'c03', 'c04', 'c06'}, 'act-03': {'c01', 'c02', 'c03', 'c04', 'c05'}}
WORD = {'satu': 1, 'dua': 2, 'tiga': 3}

def consumers(modules=('05', '06')):
    out = []
    for m in modules:
        for f in sorted(glob.glob(str(CUR / f'mod-w{m}/theory/items/*.yaml'))):
            for v in yaml.safe_load(open(f, encoding='utf-8'))['variants']:
                if 'NB-5' in v.get('normalization', ''):
                    out.append((v['variant_id'], v['stem'], v['accepted_answers'], v['normalization'], None))
        for f in sorted(glob.glob(str(CUR / f'mod-w{m}/lab/act-0*/checks.yaml'))):
            d = yaml.safe_load(open(f, encoding='utf-8')); act = f.split('/')[-2]
            for var in d['variants']:
                for c in var['checks']:
                    if 'accepted_answers' not in c:
                        continue
                    if m == '06' and c['check_id'][-3:] in W6_NOT_NB5.get(act, set()):
                        continue
                    if not re.fullmatch(r'[-−]?[\d.,]+', str(c['accepted_answers'][0])):
                        continue
                    out.append((c['check_id'], c.get('question', ''), c['accepted_answers'], d['normalization'],
                                d.get('answer_validation', '') + ' ' + d.get('infrastructure', '')))
    return out

def audit(items):
    find_ = []
    for iid, stem, acc, norm, val in items:
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
        r.check(got == f['expected'], f"{f.get('id', 'sintetis')} {f['input']!r}: {got} ≠ {f['expected']}")
    print(f'  fixture NB-5: {len(fx)}')
    for f in yaml.safe_load(open(__file__.replace('check_nb5.py', 'fixtures/f51_fixtures.yaml'), encoding='utf-8')):
        acc, norm = find(f['file'], f['id'])
        r.check('peka huruf' in norm and 'N1–N6' not in norm, f"{f['id']}: kontrak F-51 berubah")
        got = 'ACCEPT' if f['input'].strip() in [str(a) for a in acc] else 'INVALID'
        r.check(got == f['expected'], f"F-51 {f['input']!r}: {got} ≠ {f['expected']}")
    items = consumers()
    nt = sum('.theory.' in i[0] for i in items); nl = sum('.lab.' in i[0] for i in items)
    print(f'  konsumen NB-5 W5–W6: {len(items)} (teori {nt}, lab {nl})')
    findings = audit(items)
    for x in findings:
        print('  TEMUAN', *x)
    r.check(not findings, f'{len(findings)} temuan pada konsumen NB-5')
    # uji mutasi: pemeriksa harus menangkap cacat yang disuntikkan
    base = [i for i in items if i[0].endswith('mod-w05.theory.s15.vA')][0]
    s18 = [i for i in items if i[0].endswith('mod-w05.theory.s18.vA')][0]
    mut = [('MUT-presisi', s18[1], ['3,50'], s18[3], None), ('MUT-ribuan', base[1], ['204000', '20.4000'], base[3], None),
           ('MUT-tanda', base[1], ['204000', '-204000'], base[3], None), ('MUT-galat', 'x', ['5'], base[3], 'tanpa pembeda'),
           ('MUT-kontrak', base[1], ['204000'], 'cocokkan persis', None)]
    caught = {m[0] for m in audit(mut)}
    r.check(caught == {m[0] for m in mut}, f'uji mutasi tidak semua tertangkap: {caught}')
    print(f'  uji mutasi tertangkap: {len(caught)}/{len(mut)}')
    return r.done()

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
