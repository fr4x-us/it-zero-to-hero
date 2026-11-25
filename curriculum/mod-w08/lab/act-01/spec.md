---
activity_id: mod-w08.lab.act-01
component: mod-w08.lab
content_version: "1.0"
variants: [mod-w08.lab.act-01.vA, mod-w08.lab.act-01.vB]
competencies: [comp-w08-symbol-01, comp-w08-branch-01, comp-w08-algo-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W8 · Aktivitas 1 — Percabangan pada Flowchart

## Tujuan

Menelusuri flowchart bercabang bertingkat untuk beberapa input, termasuk nilai tepat di batas, menentukan jalur blok, dan memahami domain input.

## Prasyarat

Pelajaran 1, Pelajaran 2.

## Asumsi (model modul)

Flowchart ditulis sebagai **tabel blok bernomor** (Pelajaran 2 §2): setiap blok punya bentuk, isi, dan blok berikutnya; keputusan punya cabang Ya dan Tidak. `←` berarti "beri nilai". Jalankan blok persis seperti tertulis. Jawaban bilangan menurut NB-5 (W5). Input di luar domain tidak dijamin menghasilkan output bermakna.

**Contoh terlihat (0 poin): flowchart lain "jika x > 0 output x, selain itu output 0": input −2 → 0**

## Data (fixture): flowchart sebagai tabel blok

**Varian A — Biaya parkir** · Domain input: j = lama parkir dalam jam, bilangan bulat ≥ 1

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | `Mulai` | B2 |
| B2 | Jajar genjang | `Input j` | B3 |
| B3 | Belah ketupat | `j ≤ 2?` | Ya → B4; Tidak → B5 |
| B4 | Persegi panjang | `biaya ← 5000` | B8 |
| B5 | Belah ketupat | `j ≤ 5?` | Ya → B6; Tidak → B7 |
| B6 | Persegi panjang | `biaya ← 5000 + (j − 2) × 3000` | B8 |
| B7 | Persegi panjang | `biaya ← 15000` | B8 |
| B8 | Jajar genjang | `Output biaya` | B9 |
| B9 | Oval | `Selesai` | — |

**Varian B — Harga tiket museum** · Domain input: u = usia dalam tahun, bilangan bulat ≥ 0

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | `Mulai` | B2 |
| B2 | Jajar genjang | `Input u` | B3 |
| B3 | Belah ketupat | `u < 5?` | Ya → B4; Tidak → B5 |
| B4 | Persegi panjang | `harga ← 0` | B8 |
| B5 | Belah ketupat | `u ≤ 17?` | Ya → B6; Tidak → B7 |
| B6 | Persegi panjang | `harga ← 10000` | B8 |
| B7 | Persegi panjang | `harga ← 25000` | B8 |
| B8 | Jajar genjang | `Output harga` | B9 |
| B9 | Oval | `Selesai` | — |

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | Output untuk input **j = 1**? | Output untuk input **u = 4**? |
| 02 | Output untuk input **j = 2**? | Output untuk input **u = 5**? |
| 03 | Output untuk input **j = 5**? | Output untuk input **u = 17**? |
| 04 | Output untuk input **j = 6**? | Output untuk input **u = 18**? |
| 05 | Untuk input j = 4, blok mana saja yang dilewati, berurutan? (a) B1 B2 B3 B4 B8 B9, (b) B1 B2 B3 B5 B6 B8 B9, (c) B1 B2 B3 B5 B7 B8 B9, (d) B1 B2 B5 B6 B8 B9 | Untuk input u = 30, blok mana saja yang dilewati, berurutan? (a) B1 B2 B3 B4 B8 B9, (b) B1 B2 B3 B5 B6 B8 B9, (c) B1 B2 B5 B7 B8 B9, (d) B1 B2 B3 B5 B7 B8 B9 |
| 06 | Input j = 0 (di luar domain). Pernyataan yang benar? (a) Flowchart pasti memberi biaya yang benar, (b) Hasilnya tidak dijamin bermakna karena domain menyatakan j ≥ 1; input seperti ini harus ditolak atau ditangani terpisah, (c) Biaya pasti 0, (d) Flowchart tidak berhenti | Input u = −3 (di luar domain). Pernyataan yang benar? (a) Hasilnya tidak dijamin bermakna karena domain menyatakan u ≥ 0; input seperti ini harus ditolak atau ditangani terpisah, (b) Harga pasti 0 dan itu benar, (c) Flowchart tidak berhenti, (d) Harga pasti 25000 |

## Yang diserahkan

Bilangan untuk 1–4 (boleh diawali `Rp`); huruf opsi untuk 5–6.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, bentuk angka yang tidak sesuai NB-5, atau huruf di luar a–d → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-ALGO, R-SYMBOL, R-BRANCH.
