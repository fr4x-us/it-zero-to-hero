"""Pustaka bersama paket validasi DOKUMENTASI kurikulum (bukan evaluator produksi, bukan kode aplikasi).
Hanya membaca berkas YAML/Markdown di curriculum/ dan docs/. Dependensi: Python >= 3.10, PyYAML."""
import itertools, re, subprocess
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
CUR = ROOT / 'curriculum'

def load(rel):
    return yaml.safe_load(open(CUR / rel, encoding='utf-8'))

def content_sha():
    """SHA commit dan tree curriculum/ yang diuji; tanda bila working tree kotor."""
    try:
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
        tree = subprocess.check_output(['git', 'rev-parse', 'HEAD:curriculum'], cwd=ROOT, text=True).strip()
        dirty = subprocess.check_output(['git', 'status', '--porcelain', '--', 'curriculum'], cwd=ROOT, text=True).strip()
        return head, tree, bool(dirty)
    except Exception:
        return 'unknown', 'unknown', True

CATS = {
    'HITUNG': 'jawaban dihitung ulang secara independen dari isi soal/aturan',
    'REGRESI': 'dibandingkan dengan nilai harapan tetap (fixture, kunci tetap, snapshot) — bukan perhitungan ulang',
    'STRUKTUR': 'pemeriksaan struktur/keberadaan/konsistensi berkas',
}

class Report:
    """Pencatat hasil. Setiap pemeriksaan diberi kategori klaim (R4-10). Penilaian SEMANTIK penulis tidak dihitung di sini."""
    def __init__(self, name):
        self.name, self.bad, self.n, self.cat = name, 0, 0, {}
    def check(self, cond, msg, cat='STRUKTUR'):
        assert cat in CATS, cat
        self.n += 1; self.cat[cat] = self.cat.get(cat, 0) + 1
        if not cond:
            self.bad += 1
            print('  GAGAL', f'[{cat}]', msg)
        return cond
    def done(self):
        status = 'ALL OK' if not self.bad else f'GAGAL {self.bad}'
        cats = ', '.join(f'{k} {v}' for k, v in sorted(self.cat.items()))
        print(f'[{self.name}] pemeriksaan {self.n} ({cats}): {status}')
        return self.bad == 0

# ---------- NB-5 (kontrak N1–N6, teks normalisasi butir W5–W8) ----------
NUM = r'-?(?:0|[1-9]\d{0,2}(?:\.\d{3})+|[1-9]\d*)(?:,\d+)?'

def _canon_num(s):
    s = s.replace('−', '-')
    if not re.fullmatch(NUM, s) or re.fullmatch(r'-0(,0+)?', s):
        return None
    return s.replace('.', '')

def nb5_content_errors(accepted):
    """R5-04: validasi konten accepted_answers sebelum evaluasi. Kembalikan daftar alasan (kosong = sah)."""
    if not isinstance(accepted, (list, tuple)) or not accepted:
        return ['accepted_answers kosong atau bukan daftar']
    errs, canon, parsed = [], None, []
    for i, a in enumerate(accepted):
        if isinstance(a, bool) or not isinstance(a, (str, int)):
            errs.append(f'entri {i} bukan teks/angka: {a!r}'); continue
        a = str(a)
        m = re.fullmatch(r'(Rp ?)?([-−]?[\d.,]+)( ?)(.*)', a)
        if not m or a != a.strip():
            errs.append(f'entri {i} tidak berbentuk angka+afiks: {a!r}'); continue
        pre, num, sp, suf = m.groups()
        n = _canon_num(num)
        if n is None:
            errs.append(f'entri {i} angka tidak sah: {a!r}'); continue
        if pre and suf:
            errs.append(f'entri {i} memakai awalan Rp dan akhiran sekaligus: {a!r}')
        if suf and (re.search(r'\d', suf) or suf != suf.strip()):
            errs.append(f'entri {i} akhiran tidak sah: {a!r}')
        if sp and not suf:
            errs.append(f'entri {i} spasi tanpa akhiran: {a!r}')
        parsed.append((i, a, pre, n, suf))
    plain = [x for x in parsed if not x[2] and not x[4]]
    if not plain:
        errs.append('tidak ada bentuk kanonik (angka polos)')
    elif plain[0][0] != 0:
        errs.append('entri pertama bukan bentuk kanonik')
    else:
        canon = plain[0][3]
    if canon is not None:
        dec = lambda x: len(x.split(',')[1]) if ',' in x else 0
        for i, a, pre, n, suf in parsed:
            if n != canon:
                errs.append(f'entri {i} nilai/presisi berbeda dari kanonik {canon}: {a!r}')
            elif dec(n) != dec(canon):
                errs.append(f'entri {i} presisi berbeda: {a!r}')
    return errs

def nb5(raw, accepted):
    """Kembalikan ACCEPT / WRONG / INVALID untuk satu isian terhadap accepted_answers butir.
    N1 trim; N2 bentuk angka; N3 afiks: awalan `Rp` (hanya butir rupiah) dan akhiran dari accepted_answers;
    N4 huruf diabaikan hanya pada akhiran; N5 kanonisasi; N6 bandingkan dengan angka kanonik (presisi sama).
    R6-04: kombinasi (awalan, akhiran) isian harus sama dengan salah satu entri accepted_answers.
    R5-04: konten cacat → CONTENT_ERROR; isian bukan teks → EVALUATION_ERROR (bukan WRONG/INVALID; tanpa exception)."""
    try:
        if nb5_content_errors(accepted):
            return 'CONTENT_ERROR'
        if not isinstance(raw, str):
            return 'EVALUATION_ERROR'
        acc = [str(a) for a in accepted]
        sufs, rp, canon, combos = set(), False, None, set()
        for a in acc:
            m = re.fullmatch(r'(Rp ?)?([-−]?[\d.,]+) ?(.*)', a)
            if m.group(1):
                rp = True
            if m.group(3):
                sufs.add(m.group(3))
            # R6-04: kombinasi afiks yang sah hanya yang tertulis di accepted_answers (tidak dirakit dari awalan + akhiran terpisah)
            combos.add((bool(m.group(1)), m.group(3).lower()))
            if canon is None and not m.group(1) and not m.group(3):
                canon = _canon_num(m.group(2))
        s = raw.strip(' \t')
        m = re.fullmatch(r'(Rp ?)?([-−]?[\d.,]+)( ?)(.*)', s)
        if not m:
            return 'INVALID'
        pre, num, _sp, suf = m.groups()
        if pre and not rp:
            return 'INVALID'
        if suf and suf.lower() not in {x.lower() for x in sufs}:
            return 'INVALID'
        if (bool(pre), suf.lower()) not in combos:
            return 'INVALID'
        n = _canon_num(num)
        if n is None:
            return 'INVALID'
        dec = lambda x: len(x.split(',')[1]) if ',' in x else 0
        if dec(n) != dec(canon):
            return 'INVALID'
        return 'ACCEPT' if n == canon else 'WRONG'
    except Exception:  # pragma: no cover — jaring pengaman deterministik
        return 'EVALUATION_ERROR'

# ---------- BN-6 dan B01 ----------
def bn6(raw, value, mode):
    s = raw.strip(' \t')
    if not re.fullmatch(r'[01]+', s):
        return 'INVALID'
    # Validitas bentuk tidak bergantung pada nilai kunci: kanonik = `0` atau diawali 1; lebar tetap = tepat n digit.
    ok = (s == '0' or s[0] == '1') if mode == 'canonical' else len(s) == mode
    if not ok:
        return 'INVALID'
    return 'ACCEPT' if int(s, 2) == value else 'WRONG'

def b01(raw):
    s = raw.strip(' \t')
    return s if s in ('0', '1') else None

# ---------- BX (tata bahasa ekspresi Boolean W6) ----------
def bx_parse(s, variables, strict=False):
    toks = re.findall(r'\(|\)|[^\s()]+', s)
    pos = [0]
    def peek():
        if pos[0] >= len(toks):
            return None
        t = toks[pos[0]]
        return t if strict else t.upper()
    def eat():
        pos[0] += 1
    def or_expr():
        f = and_expr()
        while f and peek() == 'OR':
            eat(); g = and_expr()
            if not g: return None
            f = (lambda a, b: lambda e: a(e) or b(e))(f, g)
        return f
    def and_expr():
        f = unary()
        while f and peek() == 'AND':
            eat(); g = unary()
            if not g: return None
            f = (lambda a, b: lambda e: a(e) and b(e))(f, g)
        return f
    def unary():
        t = peek()
        if t == 'NOT':
            eat(); g = unary()
            return (lambda a: lambda e: not a(e))(g) if g else None
        if t == '(':
            eat(); g = or_expr()
            if not g or peek() != ')': return None
            eat(); return g
        if t in variables:
            eat(); return (lambda v: lambda e: e[v])(t)
        return None
    if not toks:
        return None
    f = or_expr()
    return f if f and pos[0] == len(toks) else None

def truth_table(f, variables):
    return [int(bool(f(dict(zip(variables, bits))))) for bits in itertools.product([0, 1], repeat=len(variables))]
