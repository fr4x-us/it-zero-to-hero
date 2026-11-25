"""R4-08: uji positif/negatif mode resmi run_all.py pada klon sementara dari commit HEAD (tidak mengubah repositori asli).
Jalankan setelah perubahan di-commit:  python3 docs/validation/test_provenance.py"""
import shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

def run(clone, *args):
    p = subprocess.run([sys.executable, 'docs/validation/run_all.py', *args], cwd=clone, capture_output=True, text=True)
    return p.returncode, p.stdout

def main():
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    tmp = Path(tempfile.mkdtemp(prefix='prov-'))
    ok = True
    try:
        clone = tmp / 'repo'
        subprocess.check_call(['git', 'clone', '-q', '--no-hardlinks', str(ROOT), str(clone)])
        subprocess.check_call(['git', 'checkout', '-q', head], cwd=clone)
        cases = []
        rc, out = run(clone, '--official'); cases.append(('positif: snapshot bersih', rc == 0 and 'Provenance: snapshot bersih' in out, rc))
        def mutate(path, text, label, append=True):
            f = clone / path; orig = f.read_text(encoding='utf-8') if f.exists() else None
            f.write_text((orig or '') + text if append else text, encoding='utf-8')
            rc, out = run(clone, '--official')
            cases.append((label, rc == 2 and 'BUKTI RESMI DITOLAK' in out, rc))
            if orig is None: f.unlink()
            else: f.write_text(orig, encoding='utf-8')
        mutate('curriculum/mod-w05/theory/items/s03.yaml', '\n# ubah\n', 'negatif: berkas kurikulum berubah')
        mutate('docs/validation/fixtures/nb5_fixtures.yaml', '\n# ubah\n', 'negatif: fixture berubah')
        mutate('docs/validation/check_nb5.py', '\n# ubah\n', 'negatif: skrip validasi berubah')
        mutate('docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md', '\nubah\n', 'negatif: dokumen relevan berubah')
        mutate('curriculum/mod-w05/baru.yaml', 'a: 1\n', 'negatif: berkas baru tak terlacak')
        f = clone / 'curriculum/mod-w05/theory/items/s03.yaml'; orig = f.read_text(encoding='utf-8')
        f.write_text(orig + '\n# ubah\n', encoding='utf-8')
        rc, out = run(clone)
        cases.append(('diagnostik: tree kotor tetap dijalankan tetapi ditandai TIDAK TERVERIFIKASI (bukan bukti)', rc == 0 and 'TIDAK TERVERIFIKASI' in out and 'Mode: DIAGNOSTIK' in out, rc))
        f.write_text(orig, encoding='utf-8')
        shutil.rmtree(clone / '.git')
        rc, out = run(clone, '--official'); cases.append(('negatif: git/HEAD tidak tersedia', rc == 2 and 'tidak dapat diverifikasi' in out, rc))
        for label, good, rc in cases:
            print(f'  {"OK   " if good else "GAGAL"} {label} (exit {rc})'); ok &= good
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f'[provenance] kasus {len(cases)}: {"ALL OK" if ok else "GAGAL"}')
    return ok

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
