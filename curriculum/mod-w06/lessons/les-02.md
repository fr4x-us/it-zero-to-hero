---
lesson_id: mod-w06.les-02
practice_id: mod-w06.prac-02
module_id: mod-w06
content_version: "1.0"
title: "Desimal ke Biner dan Rentang n Bit"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w06-dec2bin-01]
prerequisites: [mod-w06.les-01]
accessibility:
  diagrams:
    - id: dg-w06-02
      alt: "Tangga pembagian berulang dengan 2 untuk bilangan 29."
      long_description: >
        Baris-baris: 29 dibagi 2 = 14 sisa 1; 14 dibagi 2 = 7 sisa 0; 7
        dibagi 2 = 3 sisa 1; 3 dibagi 2 = 1 sisa 1; 1 dibagi 2 = 0 sisa 1.
        Panah naik dari sisa terakhir ke sisa pertama membaca 11101.
  tables_with_core_data: ["Tabel metode bobot", "Tabel pembagian berulang", "Tabel rentang n bit"]
  english_terms: [decimal to binary, repeated division, remainder, leading zeros, bit width, unsigned, range]
---

# Pelajaran 2 — Desimal ke Biner dan Rentang n Bit

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Mengubah **desimal ke biner** dengan dua metode.
2. Menulis hasil **tanpa nol di depan** atau **tepat n bit**.
3. Menentukan **nilai terbesar** dan **banyak nilai** yang dapat ditulis
   dengan n bit **tak bertanda**.

## Mengapa ini penting?

Banyak hal di komputer punya lebar bit tetap: satu byte = 8 bit, setiap
oktet alamat IPv4 = 8 bit (W3). Lebar bit menentukan nilai terbesar yang
muat — karena itu satu oktet tidak pernah lebih dari 255.

## 1. Metode bobot (mengurangi bobot terbesar)

1. Cari bobot terbesar yang **tidak melebihi** bilangan.
2. Tulis 1 di posisinya; kurangi bilangan dengan bobot itu.
3. Ulangi untuk sisanya; posisi yang tidak terpakai diisi 0.

**Contoh: 50.** Bobot terbesar ≤ 50 adalah 32 → sisa 18 → 16 → sisa 2 → 2 →
sisa 0.

| Bobot | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|
| Bit | 1 | 1 | 0 | 0 | 1 | 0 |

50 = **110010₂**. Periksa: 32 + 16 + 2 = 50.

## 2. Metode pembagian berulang dengan 2

Bagi dengan 2, catat **sisa** (0 atau 1, ingat W5), ulangi pada hasil bagi
sampai hasil baginya 0, lalu **baca sisa dari bawah ke atas**. Kasus
khusus: bilangan **0** tidak perlu dibagi — biner kanoniknya `0` (dalam
tepat 8 bit: `00000000`).

*Deskripsi diagram dg-w06-02:* 29 → sisa 1, 0, 1, 1, 1 dari atas ke bawah;
dibaca dari bawah: 11101.

| Bilangan | ÷ 2 = hasil bagi | Sisa |
|---|---|---|
| 29 | 14 | 1 |
| 14 | 7 | 0 |
| 7 | 3 | 1 |
| 3 | 1 | 1 |
| 1 | 0 | 1 |

29 = **11101₂** (sisa dibaca dari bawah). Periksa: 16 + 8 + 4 + 1 = 29.

## 3. Tanpa nol di depan vs tepat n bit

| Instruksi | Artinya | 24 ditulis |
|---|---|---|
| Tanpa nol di depan | Digit pertama 1; bilangan 0 ditulis `0` | `11000` |
| Tepat 8 bit | Tepat 8 digit; tambahkan nol di **depan** | `00011000` |

Nol ditambahkan di **depan** (kiri), tidak pernah di belakang, karena nol
di belakang menggeser semua bit dan mengubah nilai (`110000₂` = 48).

## 4. Rentang n bit tak bertanda

W6 hanya memakai bilangan **tak bertanda**: nol dan positif. (Cara menulis
bilangan negatif dalam biner di luar cakupan W6.)

| Lebar | Nilai terkecil | Nilai terbesar | Banyak nilai |
|---|---|---|---|
| 3 bit | 0 (`000`) | 7 (`111`) | 8 |
| n bit | 0 | 2ⁿ − 1 | 2ⁿ |
| 8 bit (1 byte) | 0 | 255 | 256 |

Bilangan yang lebih besar dari 2ⁿ − 1 **tidak muat** dalam n bit; butuh
lebih banyak bit. Contoh: 8 butuh 4 bit (`1000₂`) karena 3 bit hanya sampai 7.

## 5. Contoh terbimbing

**Soal:** Tulis **35** dalam biner tepat 8 bit.

1. 35 = 32 + 2 + 1 → `100011`.
2. Enam digit; tambah dua nol di depan → `00100011`.
3. Periksa: 32 + 2 + 1 = 35 ✓; tepat 8 digit ✓.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Sisa dibaca dari atas ke bawah" | Dari bawah ke atas (sisa terakhir = bit paling kiri) |
| "Nol boleh ditambah di belakang" | Hanya di depan |
| "5 bit paling besar 32" | 2⁵ − 1 = 31; 32 adalah banyaknya nilai |
| "Bilangan negatif cukup diberi tanda − di depan bit" | Bukan cara komputer; di luar cakupan W6 |

## 7. Latihan terbimbing (`mod-w06.prac-02`, tidak dinilai)

1. Ubah **34** ke biner (tanpa nol di depan).
2. Ubah **3** ke biner **tepat 6 bit**.
3. Nilai terbesar dan banyak nilai untuk 3 bit?
4. Berapa bit (tanpa nol di depan) yang dibutuhkan untuk menulis 33?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa satu oktet alamat IPv4 tidak pernah lebih dari 255?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 34 = 32 + 2 → `100010`.
2. 3 = 2 + 1 → `11` → `000011`.
3. 7 dan 8.
4. 33 = `100001` → 6 bit.

Cek pemahaman: satu oktet = 8 bit; nilai terbesar 2⁸ − 1 = 255.

## Ringkasan

- Desimal → biner: kurangi bobot terbesar, atau bagi 2 berulang dan baca
  sisa dari bawah.
- Nol hanya ditambahkan di depan.
- n bit tak bertanda: 0 sampai 2ⁿ − 1, sebanyak 2ⁿ nilai.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Pembagian berulang | repeated division | Membagi dengan 2 terus-menerus sambil mencatat sisa |
| Nol di depan | leading zeros | Nol di sebelah kiri yang tidak mengubah nilai |
| Lebar bit | bit width | Banyak bit yang tersedia |
| Tak bertanda | unsigned | Hanya nol dan bilangan positif |
| Rentang | range | Dari nilai terkecil sampai terbesar |
