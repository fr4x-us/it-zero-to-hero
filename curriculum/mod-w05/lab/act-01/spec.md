---
activity_id: mod-w05.lab.act-01
component: mod-w05.lab
content_version: "1.0"
variants: [mod-w05.lab.act-01.vA, mod-w05.lab.act-01.vB]
competencies: [comp-w05-arith-01, comp-w05-expr-01, comp-w05-divmod-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W5 · Aktivitas 1 — Urutan Operasi, Bilangan Negatif, Hasil Bagi dan Sisa

## Tujuan

Menghitung ekspresi dengan urutan operasi yang benar (termasuk kurung, pangkat, dan bilangan negatif), serta menentukan hasil bagi dan sisa pembagian bilangan bulat.

## Prasyarat

Pelajaran 1 §1–§3, Pelajaran 2 §1–§2.

## Asumsi (model modul)

Urutan operasi W5: kurung → pangkat → kali/bagi (kiri ke kanan) → tambah/kurang (kiri ke kanan). Hasil bagi dan sisa hanya untuk bilangan bulat tidak negatif dengan pembagi positif; sisa selalu 0 sampai pembagi − 1. Bilangan ditulis menurut **aturan angka NB-5** (Pelajaran 3 §1): koma untuk desimal (`12,5`); titik hanya pemisah ribuan berkelompok tiga digit (`1.250`); tanpa nol di depan; tanda minus untuk bilangan negatif; satuan yang disebut di soal boleh ditulis di belakang angka (mis. `menit`, `%`, `Rp` di depan rupiah).

**Contoh terlihat (0 poin): `2 + 6 ÷ 2` = 5; 23 dibagi 5 → hasil bagi 4, sisa 3**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | Hitung `12 + 18 ÷ 3 × 2`. | Hitung `40 − 24 ÷ 6 × 3`. |
| 02 | Hitung `(7 − 15) × 3 + 30`. | Hitung `(4 − 13) × 2 + 25`. |
| 03 | Hitung `5² − 4 × (6 − 2)`. | Hitung `3² + 2 × (10 − 7)`. |
| 04 | 125 dibagi 9: berapa **hasil bagi** (bilangan bulat)? | 143 dibagi 8: berapa **hasil bagi** (bilangan bulat)? |
| 05 | 125 dibagi 9: berapa **sisa**? | 143 dibagi 8: berapa **sisa**? |
| 06 | Hari ini **Rabu**. Hari apa **60 hari** lagi? | Hari ini **Kamis**. Hari apa **50 hari** lagi? |

## Yang diserahkan

Bilangan (1–5) dan nama hari (6). Tulis hanya hasil akhir; langkah boleh dikerjakan di kertas.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, angka desimal untuk jawaban bulat, nol di depan, kata (`tiga`), atau singkatan hari → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-ARITH, R-EXPR, R-DIVMOD.
