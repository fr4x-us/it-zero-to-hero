# Paket Validasi Dokumentasi Kurikulum (PR #28)

Paket ini adalah **alat review dokumentasi**: membaca berkas YAML/Markdown di
`curriculum/` dan `docs/`, lalu memeriksa kontrak yang tertulis. Paket ini
**bukan** evaluator produksi, **bukan** kode aplikasi Android, dan **tidak**
dijalankan oleh CI. Disusun oleh penulis PR (Claude); hasilnya adalah hasil
penulis, **bukan** verifikasi independen.

## Cara menjalankan

Prasyarat: Python ≥ 3.10, PyYAML, dan `git` (diuji dengan Python 3.13.18,
PyYAML 6.0.3). Tidak ada dependensi lain.

```bash
# dari akar repositori, pada commit yang di-checkout bersih
python3 docs/validation/run_all.py --official   # BUKTI RESMI (exit 0 = lolos; 2 = provenance ditolak; 1 = pemeriksaan gagal)
python3 docs/validation/run_all.py              # DIAGNOSTIK pengembangan (working tree boleh kotor; bukan bukti)
python3 docs/validation/test_provenance.py      # uji positif/negatif mode resmi pada klon sementara
```

Mode **resmi** menolak menjalankan pemeriksaan bila commit tidak dapat
ditentukan atau ada perubahan/berkas baru di `curriculum/`, `docs/`
(termasuk skrip, fixture, dan hasil yang diharapkan di `docs/validation/`),
atau `CLAUDE.md`. Ia mencetak commit dan tree `curriculum/`, `docs/`, dan
`docs/validation/`. Hasil mode diagnostik tidak boleh dipakai sebagai bukti
penerimaan.

## Kategori klaim (R4-10)

| Kategori | Arti |
|---|---|
| HITUNG | Jawaban dihitung ulang dari isi soal/aturan (interpreter flowchart W8, simulasi operasi berkas W2, aritmetika, enumerasi tukar W7, biner dari nilai di stem, tabel kebenaran dari aturan tertulis) |
| REGRESI | Dibandingkan dengan nilai harapan tetap (fixture, kunci tetap, snapshot posisi kunci, contoh reviewer) — **bukan** perhitungan ulang |
| STRUKTUR | Keberadaan, bentuk, dan konsistensi berkas (referensi lokasi, versi, status penerimaan, teks kontrak, integritas dokumen) |
| SEMANTIK | Penilaian penulis yang **tidak** diverifikasi otomatis: "lokasi ini benar-benar menilai konsep" (`coverage_data.py`) dan register kesetaraan varian (`equivalence_notes.py`) |

## Isi paket

| Berkas | Fungsi |
|---|---|
| `lib.py` | Pemuatan berkas; `Report` berkategori; kontrak NB-5 N1–N6 (`nb5`), BN-6, B01, tata bahasa BX |
| `check_docs.py` + `expected/doc_baseline.yaml` | R4-01: 43 dokumen wajib tidak hilang, tidak kosong, tidak menyusut di bawah 50% panjang tercatat, berjudul |
| `check_nb5.py` + `fixtures/nb5_fixtures.yaml`, `fixtures/f51_fixtures.yaml` | 39 fixture terikat butir; 82 konsumen NB-5 W5–W6; uji mutasi 5; F-51 W3 tetap peka huruf |
| `check_formats.py` + `fixtures/format_fixtures.yaml` | BN-6, B01, BX (terpisah dari NB-5) |
| `check_keys.py` + `expected/key_positions.yaml` | W8 F4, W8 latihan 3, W7 K4.q2, kunci butir D-39/putaran 4, posisi kunci (snapshot = baseline `4ddc993`) |
| `check_acceptance.py` | R4-02: setiap varian dibandingkan dengan isinya pada `acceptance.historical.baseline_commit` (git); 12 uji validator |
| `coverage_data.py`, `equivalence_notes.py`, `matrix_header.md`, `build_matrix.py` | Cakupan D-39 (bukti jalur QC-13 a/b, validasi referensi lokasi, simulasi VA-2) dan register kesetaraan 48 slot |
| `run_all.py`, `expected/run_all.txt` | Menjalankan semua pemeriksaan; mode resmi |
| `test_provenance.py` | R4-08: uji mode resmi pada klon sementara |

## Arti hasil NB-5/BN-6/B01

`ACCEPT` = bentuk sah dan nilai benar; `WRONG` = bentuk sah, nilai salah;
`INVALID` = INVALID_ANSWER (bentuk tidak sah). EVALUATION_ERROR (kegagalan
konten/aplikasi) dibedakan di teks kontrak dan diperiksa keberadaannya di
setiap lab, bukan disimulasikan.

## Provenance (R4-07)

Rekonsiliasi putaran 4 (diperiksa dengan `git rev-parse`):

| Commit | Isi | Tree `curriculum/` |
|---|---|---|
| `f8e028b8c08b0683837dc6beb961813295948348` | Konten putaran 4 dan paket validasi | `ad5c61377401aae5e565e2df710f19aec518d15b` |
| `4aea70228a10753eb82cde8b216d18a1297a9c1d` | Hanya README (mengisi SHA) | sama |
| `796043cf459602b8f6187114bf7ec6376fbb589e` | Hanya `.gitignore` | sama |

README putaran 4 mencatat commit **yang memperkenalkan** konten (`f8e028b`);
deskripsi PR mencatat commit **tempat `run_all.py` dijalankan** (`4aea702`,
lalu juga pada `796043c`). Ketiganya memiliki tree `curriculum/` yang sama,
tetapi eksekusi putaran 4 bukan mode resmi (belum ada) dan `PROJECT_MAP.md`
kosong pada ketiga commit itu (R4-01). Bukti resmi putaran 5:
[`OFFICIAL_RUN.md`](OFFICIAL_RUN.md).

## Batasan

- Pembacaan "konsep dinilai" dan register kesetaraan adalah penilaian
  penulis (SEMANTIK); skrip membuktikan jangkauan jalur dari anotasi itu,
  memvalidasi referensi, dan memastikan daftar konsep sama dengan berkas.
- Tidak ada uji pelajar, runtime Android, atau evaluator produksi.
