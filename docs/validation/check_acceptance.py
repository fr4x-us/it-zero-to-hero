"""R3-08: status penerimaan terstruktur (TPL-01a). Setiap varian yang berubah setelah penerimaan historis harus
tercatat tepat di module.yaml → acceptance.revised_variants dengan versi yang sama dan status PENDING."""
import glob, sys, yaml
from lib import CUR, load, Report

def variant_versions(m):
    out = {}
    for f in sorted(glob.glob(str(CUR / f'mod-w{m}/**/*.yaml'), recursive=True)):
        def walk(o):
            if isinstance(o, dict):
                if 'variant_id' in o and 'item_version' in o: out[o['variant_id']] = str(o['item_version'])
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for x in o: walk(x)
        walk(yaml.safe_load(open(f, encoding='utf-8')))
    return out

def main():
    r = Report('penerimaan')
    for m in ('01', '02', '03', '04', '05', '06', '07', '08'):
        M = load(f'mod-w{m}/module.yaml'); st = M['status']['owner_accepted']; vv = variant_versions(m)
        changed = {k: v for k, v in vv.items() if v != '1.0'}
        if st is True or st == 'YES':
            a = M.get('acceptance')
            if not r.check(a is not None, f'W{m}: owner_accepted YES tanpa blok acceptance'): continue
            r.check(a['historical']['id'] == f'W{m}-ACC', f'W{m}: id historis')
            rv = {x['variant_id']: x for x in a.get('revised_variants') or []}
            r.check(set(rv) == set(changed), f'W{m}: revised_variants ≠ varian berubah {sorted(set(rv) ^ set(changed))}')
            for k, x in rv.items():
                r.check(x['current_version'] == vv.get(k) and x['accepted_version'] == '1.0', f'{k}: versi')
                r.check(x['independent_review'] == 'PENDING' and x['owner_acceptance'] == 'PENDING', f'{k}: status harus PENDING')
            r.check(a['current_content'] == ('REVISED_PENDING' if changed else 'ACCEPTED_AS_IS'), f'W{m}: current_content')
            print(f'  W{m}: historis {a["historical"]["id"]}; varian revisi PENDING {len(rv)}')
        else:
            r.check('acceptance' not in M or not M['acceptance'].get('historical'), f'W{m}: belum diterima, tidak boleh ada penerimaan historis')
            print(f'  W{m}: belum diterima owner (owner_accepted {st})')
    return r.done()

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
