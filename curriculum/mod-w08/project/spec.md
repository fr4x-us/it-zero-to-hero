---
component: mod-w08.project
content_version: "1.0"
competencies: [comp-w08-algo-01, comp-w08-symbol-01, comp-w08-branch-01, comp-w08-loop-01, comp-w08-trace-01, comp-w08-correct-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W8 — Flowchart Nilai Maksimum

## Skenario

Panitia lomba sains (fiktif) mencatat skor perubahan suhu dari beberapa
percobaan. Skornya bisa **negatif** dan bisa **sama**. Panitia butuh
algoritma yang menemukan skor **terbesar**. Kamu melengkapi flowchart,
lalu menelusurinya.

## Tujuan belajar

Menerapkan seluruh tujuan W8: algoritma dan domain input (LO1), simbol
flowchart (LO2), percabangan (LO3), perulangan (LO4), tabel penelusuran
(LO5), dan kebenaran algoritma (LO6).

## Domain input

Daftar `A` berisi **n ≥ 1** bilangan bulat (boleh negatif, boleh sama).
`A[1]` adalah nilai pertama, `A[n]` nilai terakhir.

## Flowchart templat (tabel blok)

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | Mulai | B2 |
| B2 | Jajar genjang | Input daftar A berisi n nilai | B3 |
| B3 | Persegi panjang | **[F1]**; `i ← 2` | B4 |
| B4 | Belah ketupat | **[F2]** | Ya → B5; Tidak → B9 |
| B5 | Belah ketupat | **[F3]** | Ya → B6; Tidak → B7 |
| B6 | Persegi panjang | `maks ← A[i]` | B7 |
| B7 | Persegi panjang | `i ← i + 1` | B8 |
| B8 | Penghubung | kembali ke **[F4]** | **[F4]** |
| B9 | Jajar genjang | Output maks | B10 |
| B10 | Oval | Selesai | — |

**Pilihan untuk blok kosong:**

| Isian | a | b | c | d |
|---|---|---|---|---|
| F1 (B3) | `maks ← 0` | `maks ← A[1]` | `maks ← n` | `maks ← A[n]` |
| F2 (B4) | `i < n?` | `i ≤ n?` | `i ≥ n?` | `i = n?` |
| F3 (B5) | `A[i] > maks?` | `A[i] < maks?` | `A[i] = maks?` | `A[i] ≥ maks?` |
| F4 (B8 kembali ke) | B3 | B4 | B5 | B9 |

Bila ada lebih dari satu pilihan yang membuat flowchart benar untuk
**semua** daftar dalam domain, setiap pilihan yang benar itu diterima.

## Data (fixture)

- Daftar **A** = `[−7, −2, −2, 5, 3, −9]` (n = 6)
- Daftar **B** = `[−8, −3, −5]` (n = 3)

## Deliverable (formulir di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1–F4 | Pilihan untuk blok B3, B4, B5, B8 | Huruf a–d |
| F5 | Tabel penelusuran untuk daftar A: nilai `maks` setelah blok B5/B6 pada putaran i = 2, 3, 4, 5, 6 | Lima bilangan bulat |
| F6 | Output flowchart yang benar untuk daftar B | Bilangan bulat |
| F7 | Output untuk daftar B **bila** B3 memakai pilihan F1 = a (`maks ← 0`), blok lain benar | Bilangan bulat |
| F8 | Berapa kali keputusan B4 **diperiksa** untuk daftar A (termasuk pemeriksaan terakhir yang bernilai Tidak) | Bilangan bulat |
| F9 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Aturan isian

- Bilangan menurut NB-5 (W5): tanda `-` atau `−` untuk negatif.
- Bentuk terbaik bilangan saja (`-4`). Bentuk `maks = -4` atau `4 kali`
  tetap dibaca, tetapi kehilangan poin format.

## Contoh bentuk isian (bukan jawaban proyek)

Contoh memakai algoritma **lain** (menjumlahkan daftar `[2, 3]`):

| Baris penelusuran | Nilai `total` (bentuk terbaik) |
|---|---|
| Putaran i = 1 | `2` |
| Putaran i = 2 | `5` |

## Instruksi

1. Lengkapi B3, B4, B5, B8; pastikan flowchart benar untuk **semua**
   daftar dalam domain (termasuk semua negatif dan nilai sama).
2. Telusuri daftar A dan isi F5.
3. Hitung F6, F7, dan F8.
4. Jawab lima soal penjelasan, lalu tekan **Serahkan** (dengan
   konfirmasi).

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Nilai awal yang bukan anggota daftar | Salah untuk sebagian daftar |
| Syarat perulangan yang melewatkan nilai terakhir | Nilai terakhir tidak pernah diperiksa |
| Kembali ke blok yang mengatur ulang variabel | Perulangan tidak berhenti |
| Tidak menghitung pemeriksaan terakhir yang bernilai Tidak | F8 salah |
| Centang "sudah selesai" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | F1–F4 (pilihan benar, alternatif setara diterima); setiap sel F5; F6; F7; F8 |
| K2 Kelengkapan deliverable | 20 | Semua isian terisi dalam bentuk yang dapat dibaca |
| K3 Struktur dan format | 10 | Bilangan tanpa tulisan tambahan |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Setiap isian dinilai terhadap flowchart acuan dan daftar fixture (bukan
terhadap pilihan blokmu sendiri). Isian yang tidak dapat dibaca membuat
pemeriksaan yang membutuhkannya bernilai 0; isian lain tetap dinilai (MR-2).

## Bukti yang dinilai

Hanya isian F1–F9 (MR-6).

## Remedial

Attempt baru boleh dimulai dari salinan isian sebelumnya (MPV-A). Attempt
lama tetap tersimpan; skor terbaik dipakai (D-12).

## Durasi

90 menit (memahami templat 10, blok kosong 20, penelusuran 25, F6–F8 10,
memeriksa 10, soal penjelasan 15).
