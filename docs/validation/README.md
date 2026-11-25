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
| `lib.py` | Pemuatan berkas; `Report` berkategori; kontrak NB-5 N1–N6 (`nb5`; R5-04: `nb5_content_errors`; R6-04: kombinasi afiks hanya yang tertulis), BN-6, B01, tata bahasa BX |
| `check_docs.py` + `expected/doc_baseline.yaml` | R4-01: 43 dokumen wajib tidak hilang, tidak kosong, tidak menyusut di bawah 50% panjang tercatat, berjudul |
| `check_nb5.py` + `fixtures/nb5_fixtures.yaml`, `fixtures/f51_fixtures.yaml` | 67 fixture: 38 terikat butir (35 sebelum putaran 7 + 3 R6-04) dan 29 sintetis (4 awal + 16 konten cacat putaran 6 + 9 afiks R6-04); sebelum putaran 7 = 55 (35 + 4 + 16). 112 kombinasi konten cacat tanpa exception; 82 konsumen NB-5 W5–W6 tanpa konten cacat; R6-05: 9 uji pemindai ujung-ke-ujung (7 mutasi konten, 2 CLI); uji mutasi 5; F-51 W3 tetap peka huruf |
| `check_formats.py` + `fixtures/format_fixtures.yaml` | BN-6, B01, BX (terpisah dari NB-5) |
| `check_keys.py` + `expected/key_positions.yaml` | W8 F4, W8 latihan 3, W7 K4.q2, kunci butir D-39/putaran 4, posisi kunci (snapshot = baseline `4ddc993`) |
| `check_acceptance.py` | R4-02: setiap varian dibandingkan dengan isinya pada `acceptance.historical.baseline_commit` (git; R6-01 baseline dari jangkar tepercaya; R6-02 lokasi varian); R5-05: field slot bersama tingkat berkas juga dibandingkan, perubahan bersama menandai semua varian berkas; 27 uji validator (22 mutasi) + 8 uji jangkar |
| `coverage_data.py`, `coverage_elements.py`, `equivalence_notes.py`, `matrix_header.md`, `build_matrix.py` | Cakupan D-39 (bukti jalur QC-13 a/b, validasi referensi lokasi, simulasi VA-2; R5-01 elemen bernilai tepat per varian divalidasi keberadaan dan kelayakan dinilai, 11 uji positif/negatif; R6-03 integritas kunci 28 uji; simulasi VA-2 6 skenario) dan register kesetaraan 48 slot |
| `run_all.py`, `expected/run_all.txt` | Menjalankan semua pemeriksaan; mode resmi |
| `test_provenance.py` | R4-08: uji mode resmi pada klon sementara |

## Arti hasil NB-5/BN-6/B01

`ACCEPT` = bentuk sah dan nilai benar; `WRONG` = bentuk sah, nilai salah;
`INVALID` = INVALID_ANSWER (bentuk tidak sah). Perilaku yang diuji
(R5-04/R6-05): `nb5()` mengembalikan `CONTENT_ERROR` bila `accepted_answers`
cacat (kosong, bukan daftar, entri bukan teks/angka, tanpa bentuk kanonik di
posisi pertama, nilai/presisi berbeda, awalan + akhiran sekaligus, akhiran
tidak sah) — pemeriksaan konten didahulukan, apa pun isiannya; mengembalikan
`EVALUATION_ERROR` bila konten sah tetapi isian bukan teks, atau bila terjadi
exception tak terduga. Pemindai konsumen melaporkan `CONTENT_ERROR [path]` per
ID dan keluar dengan exit 1, bukan WRONG/INVALID. Ini model dokumentasi,
bukan evaluator aplikasi; EVALUATION_ERROR di teks kontrak lab tetap
diperiksa keberadaannya. Kebijakan huruf `Rp` (saat ini peka huruf) belum
diputuskan owner; fixture hanya merekam perilaku saat ini (REGRESI).

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
kosong pada ketiga commit itu (R4-01). Bukti resmi terkini (putaran 7)
ada di [`OFFICIAL_RUN.md`](OFFICIAL_RUN.md); catatan putaran 5 dan 6 digantikan.

## Batas kepercayaan penerimaan (R6-01)

`check_acceptance.py` mengambil baseline dari `trust/acceptance_anchors.yaml`
(bukan dari `module.yaml` yang divalidasi) dan memeriksa silang setiap jangkar
dengan merge PR di git (#25 untuk W1, #27 untuk W2–W4), status leluhur HEAD,
dan baris `OWNER ACCEPTED` di `docs/DECISIONS_LOG.md`. Ini validasi lokal
repositori, **bukan** bukti kriptografis otorisasi owner: jangkar, log, dan
commit dapat diubah oleh siapa pun yang dapat menulis ke repositori, sehingga
perubahan jangkar harus terlihat di diff PR dan direview.

## Batasan

- Pembacaan "konsep dinilai" dan register kesetaraan adalah penilaian
  penulis (SEMANTIK); skrip membuktikan jangkauan jalur dari anotasi itu,
  memvalidasi referensi, dan memastikan daftar konsep sama dengan berkas.
- Tidak ada uji pelajar, runtime Android, atau evaluator produksi.
