"""Jalankan semua pemeriksaan dokumentasi dan bandingkan keluaran dengan expected/run_all.txt.

  python3 docs/validation/run_all.py              # DIAGNOSTIK pengembangan (working tree boleh kotor)
  python3 docs/validation/run_all.py --official   # BUKTI RESMI: wajib commit diketahui dan snapshot bersih

Mode resmi gagal (exit 2) bila provenance tidak dapat diverifikasi: git/HEAD tidak tersedia, atau ada perubahan
(termasuk berkas baru) di curriculum/, docs/ (termasuk docs/validation/), atau CLAUDE.md."""
import io, contextlib, platform, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import yaml
from lib import ROOT
import check_docs, check_nb5, check_formats, check_keys, check_acceptance, build_matrix

SNAPSHOT_PATHS = ['curriculum', 'docs', 'CLAUDE.md']

def provenance(root=ROOT):
    """Kembalikan (ok, info, alasan). ok=False bila commit tidak diketahui atau snapshot input tidak bersih."""
    def git(*a):
        return subprocess.check_output(['git', *a], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
    try:
        info = {'commit': git('rev-parse', 'HEAD'),
                'tree_curriculum': git('rev-parse', 'HEAD:curriculum'),
                'tree_docs_validation': git('rev-parse', 'HEAD:docs/validation'),
                'tree_docs': git('rev-parse', 'HEAD:docs')}
        dirty = git('status', '--porcelain', '--untracked-files=all', '--', *SNAPSHOT_PATHS)
    except Exception as ex:
        return False, {}, f'provenance tidak dapat diverifikasi ({type(ex).__name__})'
    if dirty:
        return False, info, 'snapshot tidak bersih: ' + '; '.join(dirty.splitlines()[:10])
    return True, info, ''

def main(official=False):
    ok_p, info, why = provenance()
    print(f'Mode: {"RESMI" if official else "DIAGNOSTIK"}')
    print(f'Python {platform.python_version()}; PyYAML {yaml.__version__}')
    for k, v in info.items(): print(f'{k}: {v}')
    if not ok_p:
        print(f'Provenance: TIDAK TERVERIFIKASI — {why}')
        if official:
            print('BUKTI RESMI DITOLAK: jalankan pada commit yang diketahui dengan snapshot bersih.')
            return 2
    else:
        print('Provenance: snapshot bersih')
    buf = io.StringIO(); ok = True
    with contextlib.redirect_stdout(buf):
        for mod in (check_docs, check_nb5, check_formats, check_keys, check_acceptance, build_matrix):
            ok &= mod.main()
    out = buf.getvalue(); print(out, end='')
    exp = (Path(__file__).parent / 'expected/run_all.txt').read_text(encoding='utf-8')
    same = out == exp
    print('KELUARAN = expected/run_all.txt' if same else 'KELUARAN BERBEDA dari expected/run_all.txt')
    print('Catatan: penilaian SEMANTIK penulis (coverage_data.py, equivalence_notes.py) tidak diverifikasi otomatis.')
    return 0 if ok and same else 1

if __name__ == '__main__':
    sys.exit(main('--official' in sys.argv))
