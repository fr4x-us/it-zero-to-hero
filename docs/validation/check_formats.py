"""PR28-03/04/05: BN-6, B01, BX — fixture + konsistensi teks kontrak di butir W6 (terpisah dari NB-5)."""
import itertools, re, sys, yaml
from lib import load, bn6, b01, bx_parse, truth_table, Report

def main():
    r = Report('BN-6/B01/BX')
    fx = yaml.safe_load(open(__file__.replace('check_formats.py', 'fixtures/format_fixtures.yaml'), encoding='utf-8'))
    for f in fx['bn6']:
        got = bn6(f['input'], f['value'], f['mode'])
        r.check(got == f['expected'], f"BN-6 {f}: {got}")
    for s in ('s08', 's09'):
        for v in load(f'mod-w06/theory/items/{s}.yaml')['variants']:
            val = int(re.search(r'\*\*(\d+)\*\*', v['stem']).group(1))
            mode = 'canonical' if s == 's08' else 8
            r.check(bn6(v['accepted_answers'][0], val, mode) == 'ACCEPT', f'{v["variant_id"]}: kunci tidak sah BN-6')
            r.check('bilangan 0 ditulis `0`' in v['normalization'], f'{v["variant_id"]}: pengecualian nol tidak tertulis')
    r.check('bilangan 0 ditulis `0`' in load('mod-w06/lab/act-01/checks.yaml')['normalization'], 'lab act-01: pengecualian nol')
    for f in fx['b01']:
        r.check(b01(f['input']) == f['expected'], f"B01 {f['input']!r}")
    for a in ('act-02', 'act-03'):
        r.check('B01: buang spasi/tab di tepi' in load(f'mod-w06/lab/{a}/checks.yaml')['normalization'], f'lab {a}: kontrak B01')
    V = ['P', 'J', 'M']
    key = [int(m and (p or j)) for p, j, m in itertools.product([0, 1], repeat=3)]
    rb = load('mod-w06/project/rubric.yaml')
    r.check(rb['constants']['key']['F2_truth_table'] == key, 'kunci F2 W6 ≠ aturan tertulis')
    r.check('NOT NOT M' in rb['field_rules']['expression_readable'], 'NOT berulang tidak tertulis di rubrik')
    for f in fx['bx']:
        fn = bx_parse(f['expr'], V)
        got = 'INVALID' if fn is None else ('EQUIV' if truth_table(fn, V) == key else 'VALID_NOT_EQUIV')
        r.check(got == f['expected'], f"BX {f['expr']!r}: {got}")
        r.check((bx_parse(f['expr'], V, strict=True) is not None) == f['strict'], f"BX strict {f['expr']!r}")
    print(f"  fixture BN-6 {len(fx['bn6'])}, B01 {len(fx['b01'])}, BX {len(fx['bx'])}")
    return r.done()

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
