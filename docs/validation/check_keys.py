"""Kunci yang diubah PR #28 dihitung ulang secara independen (W8 F4, D-39, putaran 2 & 4) + distribusi posisi kunci."""
import glob, itertools, random, sys, yaml
from collections import Counter
from lib import CUR, load, Report

# ---- W8: interpreter tingkat-blok templat flowchart (kolom "Berikutnya" diikuti blok demi blok) ----
INIT = {'a': lambda L: 0, 'b': lambda L: L[0], 'c': lambda L: len(L), 'd': lambda L: L[-1]}
LOOPC = {'a': lambda i, n: i < n, 'b': lambda i, n: i <= n, 'c': lambda i, n: i >= n, 'd': lambda i, n: i == n}
CMP = {'a': lambda x, m: x > m, 'b': lambda x, m: x < m, 'c': lambda x, m: x == m, 'd': lambda x, m: x >= m}
TGT = {'a': 'B3', 'b': 'B4', 'c': 'B5', 'd': 'B9'}

def run_w8(L, f1, f2, f3, f4, limit=500):
    n = len(L); b = 'B3'; maks = i = None; trace = []; checks = 0
    for _ in range(limit):
        if b == 'B3': maks = INIT[f1](L); i = 2; b = 'B4'
        elif b == 'B4': checks += 1; b = 'B5' if LOOPC[f2](i, n) else 'B9'
        elif b == 'B5':
            if not 1 <= i <= n: return 'INDEX_ERROR', trace, checks
            b = 'B6' if CMP[f3](L[i - 1], maks) else 'B7'
        elif b == 'B6': maks = L[i - 1]; b = 'B7'
        elif b == 'B7': trace.append(maks); i += 1; b = 'B8'
        elif b == 'B8': b = TGT[f4]
        elif b == 'B9': return maks, trace, checks
    return 'NO_TERMINATION', trace, checks

def score_w8(rb, F):
    """Skor K1–K3 W8 dari aturan pemeriksaan rubrik (pilihan F1–F4 saja; isian lain acuan)."""
    K = rb['constants']['key']; s = 0
    for k, ck in zip(('F1', 'F2', 'F3', 'F4'), ('c01', 'c02', 'c03', 'c04')):
        pts = {c['id'][-3:]: c['points'] for c in rb['criteria']['K1']['checks']}
        if F[k] in 'abcd':
            s += {c['id'][-3:]: c['points'] for c in rb['criteria']['K2']['checks']}[f'c0{int(ck[-1])}']
            if F[k] in K[k]: s += pts[ck]
    rest = sum(c['points'] for c in rb['criteria']['K1']['checks'] if c['id'][-3:] not in ('c01', 'c02', 'c03', 'c04'))
    rest += sum(c['points'] for c in rb['criteria']['K2']['checks'] if c['id'][-3:] not in ('c01', 'c02', 'c03', 'c04'))
    rest += rb['criteria']['K3']['points'] + rb['criteria']['K4']['points']
    return s + rest

def key_positions(m):
    c = Counter()
    for f in sorted(glob.glob(str(CUR / f'mod-w{m}/**/*.yaml'), recursive=True)):
        d = yaml.safe_load(open(f, encoding='utf-8'))
        for v in d.get('variants', []) if isinstance(d, dict) else []:
            if isinstance(v.get('key'), str) and v['key'] in 'abcd': c[v['key']] += 1
            if isinstance(v.get('correction_key'), str): c[v['correction_key']] += 1
        if isinstance(d, dict) and 'criteria' in d and 'K4' in d['criteria']:
            for q in d['criteria']['K4'].get('items', []): c[q['key']] += 1
    return dict(sorted(c.items()))

def main():
    r = Report('kunci')
    rb = load('mod-w08/project/rubric.yaml'); K = rb['constants']['key']
    A, B = rb['constants']['list_A'], rb['constants']['list_B']
    tests = [A, B, [4], [1, 9], [9, 1], [-5, -5], [2, 7, 7, 1], [-1, -4, -2], [0], [3, 8, 8], [-9, -1], [6, 6, 6], [-2, 0, 2], [10, -10]]
    good = [c for c in itertools.product('abcd', repeat=4) if all(run_w8(L, *c)[0] == max(L) for L in tests)]
    r.check(good == [('b', 'b', 'a', 'b'), ('b', 'b', 'd', 'b')], f'W8: kombinasi benar {good}')
    r.check(K['F4'] == ['b'] and sorted(K['F3']) == ['a', 'd'] and K['F1'] == ['b'] and K['F2'] == ['b'], 'W8: kunci F1–F4 rubrik')
    t = run_w8(A, 'b', 'b', 'a', 'b')
    r.check(t[0] == max(A) and t[1] == [K['F5'][x] for x in ('i2', 'i3', 'i4', 'i5', 'i6')] and t[2] == K['F8'], 'W8: F5/F8')
    r.check(run_w8(B, 'b', 'b', 'a', 'b')[0] == K['F6'] and run_w8(B, 'a', 'b', 'a', 'b')[0] == K['F7'], 'W8: F6/F7')
    r.check(run_w8(A, 'b', 'b', 'a', 'c')[0] == 'INDEX_ERROR' and run_w8(A, 'b', 'b', 'a', 'a')[0] == 'NO_TERMINATION', 'W8: F4 c/a gagal')
    ref = {'F1': 'b', 'F2': 'b', 'F3': 'a'}
    got = {f4: score_w8(rb, {**ref, 'F4': f4}) for f4 in 'abcde'}
    r.check(got == {'b': 100, 'a': 94, 'c': 94, 'd': 94, 'e': 92}, f'W8: skor F4 {got}')
    ex = {e['id']: e['total'] for e in rb['reviewer_examples']}
    r.check((ex['E01'], ex['E05'], ex['E18'], ex['E19'], ex['E20']) == (100, 94, 94, 94, 92), 'W8: contoh reviewer E01/E05/E18–E20')
    # W8 pelajaran 3 latihan 3 (PR28-11)
    tt, k, chk, it = 1, 1, 0, 0
    while True:
        chk += 1
        if not k <= 3: break
        tt *= 2; k += 1; it += 1
    r.check((it, chk, tt, k) == (3, 4, 8, 4), 'W8 latihan 3: 3 putaran, 4 pemeriksaan, t=8, k=4')
    # W7 K4.q2 (PR28-07): tukar bersebelahan sah ⇔ depan bukan prasyarat belakang
    valid = lambda o, E: all(o.index(a) < o.index(b) for a, b in E)
    r.check(valid(['A', 'B', 'C'], [('A', 'B')]) and not valid(['C', 'B', 'A'], [('A', 'B')]), 'W7: kontraeksempel')
    rnd = random.Random(7); n_sw = 0
    for _ in range(200):
        n = rnd.randint(3, 6); E = [(a, b) for a in range(n) for b in range(n) if a < b and rnd.random() < 0.35]
        for o in itertools.permutations(range(n)):
            if not valid(o, E): continue
            for i in range(n - 1):
                s = list(o); s[i], s[i + 1] = s[i + 1], s[i]
                if valid(s, E) != ((o[i], o[i + 1]) not in E): r.check(False, f'W7 tukar {o} {i}')
                n_sw += 1
    print(f'  W7 tukar bersebelahan diuji: {n_sw}')
    q = load('mod-w07/project/rubric.yaml')['criteria']['K4']['items'][1]
    r.check(q['key'] == 'b' and 'bersebelahan' in q['stem'] and q['points'] == 2, 'W7 K4.q2 struktur')
    # D-39 dan putaran 4: butir yang diubah
    V = lambda f, i: load(f)['variants'][i]
    r.check(V('mod-w01/theory/items/s10.yaml', 1)['accepted_answers'][0] == str(16 // 8), 'W1 t-s10 vB = 2')
    r.check(V('mod-w03/theory/items/s08.yaml', 1)['accepted_answers'][0] == str(2 ** 8 - 2 - 1), 'W3 t-s08 vB = 253')
    fs = {'/tugas': {'esai.docx', 'peta.png'}, '/kirim': {'peta.png'}}; trash = []
    def op(src, f, dst, copy=False):
        if f in fs[dst]: return False
        fs[dst].add(f); (None if copy else fs[src].discard(f)); return True
    r1 = op('/tugas', 'peta.png', '/kirim'); op('/tugas', 'esai.docx', '/kirim', copy=True)
    fs['/kirim'].discard('peta.png'); trash.append(('/kirim', 'peta.png')); s_, f_ = trash.pop(); fs[s_].add(f_)
    v = V('mod-w02/theory/items/s17.yaml', 1); kt = [o['text'] for o in v['options'] if o['id'] == v['key']][0]
    r.check(not r1 and kt == f"/tugas {len(fs['/tugas'])} berkas, /kirim {len(fs['/kirim'])} berkas", f'W2 t-s17 vB: {kt}')
    for i in (0, 1):
        v = V('mod-w02/concept/items/s05.yaml', i)
        r.check(v['accepted_sequences'] == [['A', 'B', 'C', 'D']], f'W2 c-s05 v{"AB"[i]} urutan A B C D')
        txt = ' '.join(x['text'] for x in v['items'])
        r.check('seluruh' in txt and 'Tempat Sampah' in txt and 'Simulasi' in v['stem'], f'W2 c-s05 v{"AB"[i]}: periksa seluruh isi Tempat Sampah (simulasi)')
    for f, i, key in [('mod-w02/theory/items/s02.yaml', 1, ['a', 'c', 'e']), ('mod-w02/theory/items/s09.yaml', 1, ['b', 'c', 'd']),
                      ('mod-w02/concept/items/s06.yaml', 1, ['b', 'd']), ('mod-w03/concept/items/s02.yaml', 1, ['a', 'c', 'd']),
                      ('mod-w04/concept/items/s02.yaml', 1, ['b', 'c', 'e']), ('mod-w04/concept/items/s05.yaml', 0, ['a', 'c']),
                      ('mod-w06/concept/items/s05.yaml', 1, ['b', 'c', 'e'])]:
        r.check(sorted(V(f, i)['key']) == key, f'{f} v{"AB"[i]}: kunci {key}')
    rows = [''.join(map(str, b)) for b in itertools.product([0, 1], repeat=3)]
    r.check(rows[:3] == ['000', '001', '010'] and rows[-1] == '111', 'W6 c-s05 vB opsi e benar')
    exp = yaml.safe_load(open(__file__.replace('check_keys.py', 'expected/key_positions.yaml'), encoding='utf-8'))
    for m in ('01', '02', '03', '04', '05', '06', '07', '08'):
        r.check(key_positions(m) == exp[f'W{m}'], f'posisi kunci W{m}: {key_positions(m)} ≠ {exp[f"W{m}"]}')
    return r.done()

if __name__ == '__main__':
    if '--snapshot' in sys.argv:
        print(yaml.safe_dump({f'W{m}': key_positions(m) for m in ('01', '02', '03', '04', '05', '06', '07', '08')}, sort_keys=True))
    else:
        sys.exit(0 if main() else 1)
