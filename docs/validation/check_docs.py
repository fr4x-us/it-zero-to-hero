"""R4-01: integritas dokumen proyek. Mendeteksi dokumen wajib yang hilang, kosong, atau menyusut drastis
dibanding catatan `expected/doc_baseline.yaml` (STRUKTUR)."""
import sys
from pathlib import Path
import yaml
from lib import ROOT, Report

BASE = Path(__file__).with_name('expected') / 'doc_baseline.yaml'

def inspect(text):
    lines = text.splitlines()
    return len(lines), any(l.startswith('# ') for l in lines[:5])

def evaluate(baseline, reader):
    """baseline: {path: min_lines}; reader(path) → teks atau None. Kembalikan daftar kesalahan."""
    err = []
    for path, min_lines in sorted(baseline.items()):
        t = reader(path)
        if t is None: err.append(f'{path}: hilang'); continue
        n, head = inspect(t)
        if n == 0: err.append(f'{path}: kosong')
        elif n < min_lines: err.append(f'{path}: {n} baris < minimum {min_lines} (kemungkinan terhapus tidak sengaja)')
        if n and not head: err.append(f'{path}: judul tingkat 1 tidak ada di 5 baris pertama')
    return err

def read(path):
    p = ROOT / path
    return p.read_text(encoding='utf-8') if p.exists() else None

def main():
    r = Report('dokumen')
    base = yaml.safe_load(open(BASE, encoding='utf-8'))
    for e in evaluate(base, read): r.check(False, e)
    r.check(True, f'{len(base)} dokumen wajib diperiksa')
    # uji negatif/positif di memori
    r.check(evaluate({'docs/PROJECT_MAP.md': 50}, lambda p: '') == ['docs/PROJECT_MAP.md: kosong'], 'uji: dokumen kosong terdeteksi')
    r.check(evaluate({'docs/X.md': 5}, lambda p: None) == ['docs/X.md: hilang'], 'uji: dokumen hilang terdeteksi')
    r.check(len(evaluate({'docs/X.md': 50}, lambda p: '# X\n' + 'a\n' * 10)) == 1, 'uji: penyusutan drastis terdeteksi')
    r.check(evaluate({'docs/X.md': 5}, lambda p: '# X\n' + 'a\n' * 10) == [], 'uji: dokumen sehat lolos')
    print(f'  dokumen wajib: {len(base)}; uji negatif 3, positif 1')
    return r.done()

if __name__ == '__main__':
    if '--record' in sys.argv:   # catat ulang minimum (50% baris saat ini, minimal 5) — hanya untuk dokumen yang sudah diperiksa manusia
        import subprocess
        files = subprocess.check_output(['git', 'ls-files', 'CLAUDE.md', 'docs/*.md'], cwd=ROOT, text=True).split()
        rec = {f: max(5, inspect(read(f))[0] // 2) for f in files if read(f)}
        BASE.write_text('# Minimum baris dokumen wajib (50% panjang saat dicatat, minimal 5). Dicatat setelah PROJECT_MAP dipulihkan.\n'
                        + yaml.safe_dump(rec, sort_keys=True, allow_unicode=True), encoding='utf-8')
        print(len(rec))
    else:
        sys.exit(0 if main() else 1)
