---
activity_id: mod-w05.lab.act-03
component: mod-w05.lab
content_version: "1.0"
variants: [mod-w05.lab.act-03.vA, mod-w05.lab.act-03.vB]
competencies: [comp-w05-unit-01, comp-w05-expr-01, comp-w05-divmod-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W5 · Aktivitas 3 — Satuan, Rumus, dan Pembelian dalam Anggaran

## Tujuan

Mengonversi satuan waktu dan massa, memakai hasil bagi dan sisa untuk jam–menit, mensubstitusi nilai ke rumus biaya, dan menentukan jumlah maksimal yang dapat dibeli.

## Prasyarat

Pelajaran 1 §4, Pelajaran 2.

## Asumsi (model modul)

1 jam = 60 menit; 1 kg = 1.000 g. Barang hanya dapat dibeli utuh; uang tidak boleh kurang. Bilangan ditulis menurut **aturan angka NB-5** (Pelajaran 3 §1): koma untuk desimal (`12,5`); titik hanya pemisah ribuan berkelompok tiga digit (`1.250`); tanpa nol di depan; tanda minus untuk bilangan negatif; satuan yang disebut di soal boleh ditulis di belakang angka (mis. `menit`, `%`, `Rp` di depan rupiah).

**Contoh terlihat (0 poin): 1 jam 10 menit = 70 menit; 0,5 kg = 500 g**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | **4 jam 15 menit** = … menit | **3 jam 45 menit** = … menit |
| 02 | **390 menit** = berapa **jam penuh**? | **500 menit** = berapa **jam penuh**? |
| 03 | **390 menit** diubah menjadi jam penuh dan sisa menit. Berapa **sisa menitnya**? | **500 menit** diubah menjadi jam penuh dan sisa menit. Berapa **sisa menitnya**? |
| 04 | Rumus `biaya = 2.500 × n + 3.000` (rupiah). Bila `n = 8`, berapa biaya? | Rumus `biaya = 4.000 × n + 2.000` (rupiah). Bila `n = 6`, berapa biaya? |
| 05 | **2,4 kg** = … g (1 kg = 1.000 g) | **3,75 kg** = … g (1 kg = 1.000 g) |
| 06 | Uang **Rp50.000**; harga buku **Rp7.500** per buku. Paling banyak berapa buku? | Uang **Rp40.000**; harga buku **Rp6.500** per buku. Paling banyak berapa buku? |

## Yang diserahkan

Bilangan untuk 1–6.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, bentuk yang tidak sesuai NB-5, atau satuan lain (`5 kg` untuk soal gram) → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-UNIT, R-EXPR, R-DIVMOD.
