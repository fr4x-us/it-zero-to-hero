---
activity_id: mod-w08.lab.act-03
component: mod-w08.lab
content_version: "1.0"
variants: [mod-w08.lab.act-03.vA, mod-w08.lab.act-03.vB]
competencies: [comp-w08-correct-01, comp-w08-trace-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W8 · Aktivitas 3 — Kebenaran Algoritma: Nilai Awal, Nilai Sama, Nilai Negatif

## Tujuan

Menelusuri algoritma nilai terkecil pada daftar berisi nilai negatif dan nilai sama, membandingkan `<` dan `≤`, serta menemukan kasus uji yang mengungkap nilai awal yang salah.

## Prasyarat

Pelajaran 4.

## Asumsi (model modul)

Flowchart ditulis sebagai **tabel blok bernomor** (Pelajaran 2 §2): setiap blok punya bentuk, isi, dan blok berikutnya; keputusan punya cabang Ya dan Tidak. `←` berarti "beri nilai". Jalankan blok persis seperti tertulis. Jawaban bilangan menurut NB-5 (W5). `A[i]` = nilai ke-i daftar (mulai 1).

**Contoh terlihat (0 poin): daftar [2] (satu nilai) → output 2; perulangan tidak berjalan karena 2 ≤ 1 salah**

## Data (fixture): flowchart sebagai tabel blok

**Varian A — Nilai terkecil** · Domain input: daftar A berisi n ≥ 1 bilangan bulat (boleh negatif, boleh sama) · Daftar fixture: `[4, −6, 2, −6, 9]`

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | `Mulai` | B2 |
| B2 | Jajar genjang | `Input daftar A (n nilai)` | B3 |
| B3 | Persegi panjang | `kecil ← A[1]; i ← 2` | B4 |
| B4 | Belah ketupat | `i ≤ n?` | Ya → B5; Tidak → B8 |
| B5 | Belah ketupat | `A[i] < kecil?` | Ya → B6; Tidak → B7 |
| B6 | Persegi panjang | `kecil ← A[i]` | B7 |
| B7 | Persegi panjang | `i ← i + 1` | B4 |
| B8 | Jajar genjang | `Output kecil` | B9 |
| B9 | Oval | `Selesai` | — |

**Varian B — Nilai terkecil** · Domain input: daftar A berisi n ≥ 1 bilangan bulat (boleh negatif, boleh sama) · Daftar fixture: `[7, 3, 9, 3, −1]`

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | `Mulai` | B2 |
| B2 | Jajar genjang | `Input daftar A (n nilai)` | B3 |
| B3 | Persegi panjang | `kecil ← A[1]; i ← 2` | B4 |
| B4 | Belah ketupat | `i ≤ n?` | Ya → B5; Tidak → B8 |
| B5 | Belah ketupat | `A[i] < kecil?` | Ya → B6; Tidak → B7 |
| B6 | Persegi panjang | `kecil ← A[i]` | B7 |
| B7 | Persegi panjang | `i ← i + 1` | B4 |
| B8 | Jajar genjang | `Output kecil` | B9 |
| B9 | Oval | `Selesai` | — |

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | Output untuk daftar fixture? | Output untuk daftar fixture? |
| 02 | Berapa kali blok B6 dikerjakan untuk daftar fixture? | Berapa kali blok B6 dikerjakan untuk daftar fixture? |
| 03 | Bila B5 diganti `A[i] ≤ kecil?`, berapa kali B6 dikerjakan untuk daftar fixture? | Bila B5 diganti `A[i] ≤ kecil?`, berapa kali B6 dikerjakan untuk daftar fixture? |
| 04 | Bila B3 diganti `kecil ← 0` dan perbandingan dimulai dari A[1], output untuk daftar [3, 8, 5]? | Bila B3 diganti `kecil ← 0` dan perbandingan dimulai dari A[1], output untuk daftar [6, 4, 10]? |
| 05 | Daftar mana yang mengungkap kesalahan nilai awal `kecil ← 0`? (a) [−2, 5, 1], (b) [0, 3, 7], (c) [6, 9, 4], (d) [−8, −1, −3] | Daftar mana yang mengungkap kesalahan nilai awal `kecil ← 0`? (a) [11, 5, 8], (b) [−4, 2, 0], (c) [0, 1, 2], (d) [−3, −9, −2] |
| 06 | Untuk daftar fixture (5 nilai), berapa kali keputusan B4 diperiksa? | Untuk daftar fixture (5 nilai), berapa kali keputusan B4 diperiksa? |

## Yang diserahkan

Bilangan untuk 1–4 dan 6 (2, 3, 6 boleh diikuti kata `kali`); huruf opsi untuk 5.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, bentuk yang tidak sesuai NB-5, atau huruf di luar a–d → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-CORRECT, R-TRACE.
