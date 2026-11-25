"""Jalankan semua pemeriksaan dokumentasi dan bandingkan keluaran dengan expected/run_all.txt.
Pemakaian (dari akar repositori):  python3 docs/validation/run_all.py
Keluar 0 bila semua lolos DAN keluaran sama dengan yang diharapkan."""
import io, contextlib, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib import content_sha
import check_nb5, check_formats, check_keys, check_acceptance, build_matrix

def main():
    head, tree, dirty = content_sha()
    print(f'Konten diuji: commit {head}; tree curriculum/ {tree}{" (WORKING TREE KOTOR)" if dirty else ""}')
    buf = io.StringIO(); ok = True
    with contextlib.redirect_stdout(buf):
        for mod in (check_nb5, check_formats, check_keys, check_acceptance, build_matrix):
            ok &= mod.main()
    out = buf.getvalue(); print(out, end='')
    exp = (Path(__file__).parent / 'expected/run_all.txt').read_text(encoding='utf-8')
    same = out == exp
    print('KELUARAN = expected/run_all.txt' if same else 'KELUARAN BERBEDA dari expected/run_all.txt')
    return ok and same

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
