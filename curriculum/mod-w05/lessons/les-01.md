---
lesson_id: mod-w05.les-01
practice_id: mod-w05.prac-01
module_id: mod-w05
content_version: "1.0"
title: "Urutan Operasi, Bilangan Negatif, dan Rumus"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w05-arith-01, comp-w05-expr-01]
prerequisites: [mod-w04]
accessibility:
  diagrams:
    - id: dg-w05-01
      alt: "Tangga urutan operasi dengan empat anak tangga."
      long_description: >
        Empat kotak bertingkat dari atas ke bawah. Kotak 1: kurung. Kotak 2:
        pangkat. Kotak 3: kali dan bagi, setara, dikerjakan dari kiri ke
        kanan. Kotak 4: tambah dan kurang, setara, dikerjakan dari kiri ke
        kanan. Panah menunjuk dari atas ke bawah.
    - id: dg-w05-01b
      alt: "Garis bilangan dari −10 sampai 10."
      long_description: >
        Garis mendatar dengan titik 0 di tengah. Bilangan negatif di kiri,
        positif di kanan. Contoh panah: dari −2 bergerak 7 langkah ke kanan
        berhenti di 5; dari 5 bergerak 9 langkah ke kiri berhenti di −4.
  tables_with_core_data: ["Tabel urutan operasi", "Tabel istilah rumus"]
  english_terms: [order of operations, parentheses, exponent, negative number, variable, expression, formula, substitution, average]
---

# Pelajaran 1 — Urutan Operasi, Bilangan Negatif, dan Rumus

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menghitung ekspresi dengan **urutan operasi** yang benar.
2. Menjumlah dan mengurangkan **bilangan negatif** dengan garis bilangan.
3. Menjelaskan **variabel**, **ekspresi**, dan **rumus**, lalu
   **mensubstitusi** nilai ke rumus, termasuk **pangkat** dan
   **rata-rata**.

## Mengapa ini penting?

Komputer menghitung persis sesuai aturan. Bila kamu menulis `5 + 3 × 2`,
komputer menghitung 11, bukan 16. Programmer, analis data, dan teknisi
jaringan selalu harus tahu **urutan** sebuah perhitungan dikerjakan. Rumus
dengan variabel adalah cikal bakal program: satu rumus dipakai berkali-kali
dengan nilai yang berbeda.

## 1. Urutan operasi

Ekspresi dihitung menurut tangga berikut. Selesaikan anak tangga atas
sebelum turun.

| Tingkat | Operasi | Aturan |
|---|---|---|
| 1 | Kurung `( )` | Isi kurung dihitung lebih dulu; kurung di dalam kurung dari yang terdalam |
| 2 | Pangkat (`²`, `³`) | `5²` = 5 × 5 |
| 3 | Kali `×` dan bagi `÷` | **Setara**: dikerjakan dari **kiri ke kanan** |
| 4 | Tambah `+` dan kurang `−` | **Setara**: dikerjakan dari **kiri ke kanan** |

*Deskripsi diagram dg-w05-01:* empat anak tangga seperti tabel di atas,
dari kurung di atas sampai tambah/kurang di bawah.

**Contoh bertahap.** Hitung `14 − 2 × (3 + 1)²`.

1. Kurung: 3 + 1 = 4 → `14 − 2 × 4²`
2. Pangkat: 4² = 16 → `14 − 2 × 16`
3. Kali: 2 × 16 = 32 → `14 − 32`
4. Kurang: 14 − 32 = −18

**Kiri ke kanan itu penting.** Pada `24 ÷ 6 × 2`, kali dan bagi setara:
24 ÷ 6 = 4, lalu 4 × 2 = 8. Bila salah mengalikan dulu (6 × 2 = 12) hasilnya
24 ÷ 12 = 2 — berbeda. Hal yang sama berlaku untuk `15 − 4 + 3`: 15 − 4 = 11,
lalu 11 + 3 = 14 (bukan 15 − 7 = 8).

*Catatan notasi:* W5 memakai tanda matematika `×` dan `÷`. Di bahasa
pemrograman tandanya berbeda (dipelajari mulai W9), tetapi urutannya sama.

## 2. Bilangan negatif

Bilangan negatif menunjukkan nilai di bawah nol: suhu −4 °C, lantai
basement −1, atau perubahan yang berkurang.

*Deskripsi diagram dg-w05-01b:* garis bilangan −10 sampai 10; menambah
berarti bergerak ke kanan, mengurangi berarti bergerak ke kiri.

| Bentuk | Cara berpikir | Contoh |
|---|---|---|
| Menambah bilangan positif | Geser ke kanan | −2 + 7 = 5 |
| Mengurangi bilangan positif | Geser ke kiri | 5 − 9 = −4 |
| Positif × negatif | Hasil negatif | 3 × (−4) = −12 |
| Negatif × negatif | Hasil positif | (−3) × (−4) = 12 |

**Contoh bertahap.** Suhu −2 °C naik 7 °C lalu turun 10 °C:
−2 + 7 = 5; 5 − 10 = −5 °C.

## 3. Variabel, ekspresi, dan rumus

| Istilah | Arti | Contoh |
|---|---|---|
| **Variabel** | Nama untuk nilai yang dapat berbeda-beda | `p`, `harga`, `n` |
| **Konstanta** | Nilai tetap | `2` dalam `2 × (p + l)` |
| **Ekspresi** | Gabungan bilangan, variabel, dan operasi | `3 × n + 5` |
| **Rumus** | Aturan yang memberi nama pada hasil | `luas = p × l` |
| **Substitusi** | Mengganti variabel dengan nilainya | `p = 6`, `l = 4` → `luas = 24` |

**Pangkat.** `a²` berarti `a × a`; `a³` berarti `a × a × a`. Jadi `2³ = 8`,
**bukan** `2 × 3 = 6`. Pangkat dikerjakan sebelum kali: `5 × 2²` = 5 × 4 = 20,
tetapi `(5 × 2)²` = 10² = 100.

**Contoh substitusi.** Hitung `3 × m² − k` bila `m = 2` dan `k = 5`:
m² = 4; 3 × 4 = 12; 12 − 5 = 7.

## 4. Rata-rata sebagai rumus

`rata-rata = jumlah semua nilai ÷ banyaknya nilai`

Contoh: nilai 60, 70, 95 → jumlah 225; 225 ÷ 3 = 75.

Rumus dapat dibalik: **jumlah = rata-rata × banyaknya nilai**. Bila
rata-rata tiga hari pengunjung perpustakaan 40 orang dan dua hari pertama 35
dan 48, hari ketiga = 3 × 40 − (35 + 48) = 120 − 83 = 37.

## 5. Contoh terbimbing

**Soal:** Biaya sewa sepeda `biaya = 4.000 × j + 1.500` rupiah, dengan `j`
jam. Berapa biaya 3 jam?

1. Substitusi: `4.000 × 3 + 1.500`
2. Kali dulu: 12.000
3. Tambah: 12.000 + 1.500 = 13.500 rupiah.

Kesalahan umum: menjumlah dulu (3 + 1.500) lalu mengalikan.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Selalu dari kiri ke kanan" | Kiri ke kanan hanya untuk operasi **setara** setelah kurung dan pangkat |
| "Kali selalu sebelum bagi" | Kali dan bagi setara; kiri ke kanan |
| "`3²` = 6" | `3²` = 3 × 3 = 9 |
| "Mengurangi selalu membuat hasil positif lebih kecil, jadi tidak mungkin negatif" | 5 − 9 = −4 |
| "Nama variabel memengaruhi hasil" | Hasil hanya bergantung pada nilainya |

## 7. Latihan terbimbing (`mod-w05.prac-01`, tidak dinilai)

1. Hitung `9 + 12 ÷ 4 × 2`.
2. Hitung `(5 − 11) × 2 + 20`.
3. Hitung `2 × k² + 1` bila `k = 5`.
4. Rata-rata empat nilai = 70. Tiga nilai: 64, 72, 69. Nilai keempat?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa `20 ÷ 2 × 5` bernilai 50, bukan 2?
- Apa beda konstanta dan variabel dalam `keliling = 4 × s`?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 12 ÷ 4 = 3; 3 × 2 = 6; 9 + 6 = 15.
2. 5 − 11 = −6; −6 × 2 = −12; −12 + 20 = 8.
3. k² = 25; 2 × 25 = 50; 50 + 1 = 51.
4. Jumlah = 4 × 70 = 280; 64 + 72 + 69 = 205; nilai keempat = 75.

Cek pemahaman: kali dan bagi setara, jadi 20 ÷ 2 = 10 lalu 10 × 5 = 50; `4`
konstanta, `s` variabel.

## Ringkasan

- Urutan: kurung → pangkat → kali/bagi (kiri ke kanan) → tambah/kurang
  (kiri ke kanan).
- Bilangan negatif: geser pada garis bilangan.
- Variabel = nama nilai; substitusi = mengganti dengan nilai; rata-rata =
  jumlah ÷ banyak.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Urutan operasi | order of operations | Aturan mana yang dihitung lebih dulu |
| Pangkat | exponent | Perkalian berulang dengan bilangan yang sama |
| Variabel | variable | Nama untuk nilai yang dapat berbeda-beda |
| Substitusi | substitution | Mengganti variabel dengan nilainya |
| Rata-rata | average, mean | Jumlah nilai dibagi banyaknya nilai |
