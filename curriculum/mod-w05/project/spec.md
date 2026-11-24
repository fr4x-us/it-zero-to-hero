---
component: mod-w05.project
content_version: "1.0"
competencies: [comp-w05-arith-01, comp-w05-expr-01, comp-w05-divmod-01, comp-w05-unit-01, comp-w05-pct-01, comp-w05-round-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W5 — Tabel Anggaran Belajar

## Skenario

Rina, siswi kelas 10, mendapat **anggaran belajar Rp500.000** untuk satu
bulan. Ia mencatat rencana belanja kebutuhan belajarnya dan ingin tahu
berapa yang terpakai, berapa sisanya, dan bagaimana pembagian
pengeluarannya. Semua tokoh dan harga fiktif.

## Tujuan belajar

Menerapkan seluruh tujuan W5: urutan operasi (LO1), rumus dan variabel
(LO2), hasil bagi dan sisa (LO3), satuan dan perbandingan (LO4), persentase
(LO5), serta pembulatan (LO6) pada satu tabel anggaran.

## Data (fixture)

| Baris | Barang | Banyaknya | Harga satuan | Diskon untuk baris ini |
|---|---|---|---|---|
| P1 | Buku catatan | 4 | Rp12.500 | 20% |
| P2 | Pulpen | 6 | Rp3.500 | — |
| P3 | Kuota internet belajar | 1 | Rp75.000 | — |
| P4 | Fotokopi materi (per lembar) | 120 | Rp250 | — |
| P5 | Transport ke perpustakaan (per perjalanan) | 8 | Rp7.000 | — |

Diskon hanya berlaku untuk baris yang disebut, dihitung dari nilai baris
itu (banyaknya × harga satuan).

## Deliverable (formulir di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1 | Subtotal setiap baris P1–P5 (setelah diskon bila ada) | Rupiah |
| F2 | Total belanja | Rupiah |
| F3 | Sisa anggaran (anggaran − total belanja) | Rupiah |
| F4 | Persen anggaran yang terpakai, dibulatkan ke **satu** angka di belakang koma | Persen |
| F5 | Persen setiap baris P1–P5 **terhadap total belanja**, masing-masing dibulatkan ke **satu** angka di belakang koma | Persen |
| F6 | Banyaknya perjalanan transport **tambahan** (Rp7.000 per perjalanan) paling banyak yang dapat dibayar penuh dari sisa anggaran | Bilangan bulat |
| F7 | Sisa uang setelah membayar perjalanan tambahan F6 | Rupiah |
| F8 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Aturan menulis angka (NB-5, Pelajaran 3 §1)

- **Rupiah:** bentuk terbaik memakai titik ribuan tanpa `Rp` (`12.345`).
  Bentuk `12345` atau `Rp12.345` tetap dibaca, tetapi kehilangan poin
  format.
- **Persen:** bentuk terbaik tepat satu angka di belakang koma tanpa
  tanda (`12,3`). Bentuk `12,3%` atau `12` tetap dibaca (nilainya
  dibandingkan persis), tetapi kehilangan poin format.
- **Bilangan bulat F6:** digit saja (`12`).
- Titik **bukan** tanda desimal: `12.3` tidak dapat dibaca. Koma bukan
  pemisah ribuan: `12,345` sebagai rupiah tidak dapat dibaca.

## Contoh bentuk isian (bukan jawaban proyek)

Contoh memakai barang **lain** (rautan 3 × Rp2.500 dari anggaran
Rp25.000), sehingga tidak memberi jawaban.

| Isian | Contoh bentuk terbaik |
|---|---|
| Subtotal | `7.500` |
| Persen terpakai | `30,0` |
| Bilangan bulat | `7` |

## Instruksi

1. Hitung subtotal setiap baris dengan rumus yang tepat (perhatikan
   diskon P1 dan urutan operasi).
2. Hitung total, sisa, dan persen anggaran terpakai.
3. Hitung persen setiap baris terhadap total belanja, lalu bulatkan
   **masing-masing** ke satu angka di belakang koma.
4. Hitung perjalanan tambahan dan sisa uang dengan hasil bagi dan sisa.
5. Jawab lima soal penjelasan, lalu tekan **Serahkan** (dengan
   konfirmasi).

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Diskon dikurangkan sebagai angka biasa, bukan persen | Subtotal P1 salah; isian lain yang bergantung padanya juga salah nilainya |
| Persen baris dihitung terhadap anggaran, bukan total belanja | F5 salah |
| Persen dibulatkan bertahap | Nilai dapat bergeser satu angka |
| Perjalanan tambahan dibulatkan ke atas | F6 salah (tidak dapat dibayar penuh) |
| Titik sebagai desimal | Isian tidak dapat dibaca |
| Centang "sudah selesai" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | Nilai setiap isian F1–F7 dibandingkan persis dengan nilai benar dari data proyek |
| K2 Kelengkapan deliverable | 20 | Semua isian terisi dalam bentuk yang dapat dibaca |
| K3 Struktur dan format | 10 | Bentuk terbaik rupiah, persen, dan bilangan bulat |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Setiap isian dinilai terhadap nilai benar dari data proyek (bukan terhadap
isian kamu yang lain). Isian yang tidak dapat dibaca membuat pemeriksaan
yang membutuhkannya bernilai 0; isian lain tetap dinilai (MR-2).

## Bukti yang dinilai

Hanya isian F1–F8. Coretan perhitungan tidak dinilai (MR-6), tetapi
membantu kamu memeriksa ulang.

## Remedial

Attempt baru boleh dimulai dari salinan isian sebelumnya (MPV-A). Attempt
lama tetap tersimpan; skor terbaik dipakai (D-12).

## Durasi

90 menit (memahami data 10, subtotal dan total 25, persen dan pembulatan
25, perjalanan tambahan 10, memeriksa 5, soal penjelasan 15).
