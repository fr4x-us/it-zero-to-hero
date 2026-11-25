---
lesson_id: mod-w07.les-02
practice_id: mod-w07.prac-02
module_id: mod-w07
content_version: "1.0"
title: "Pengenalan Pola"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w07-pattern-01]
prerequisites: [mod-w07.les-01]
accessibility:
  diagrams:
    - id: dg-w07-02
      alt: "Tiga susunan batang berbentuk huruf L yang membesar."
      long_description: >
        Susunan 1 berupa 3 kotak membentuk huruf L. Susunan 2 berupa 5 kotak,
        susunan 3 berupa 7 kotak; setiap susunan menambah satu kotak di
        lengan tegak dan satu di lengan datar.
  tables_with_core_data: ["Tabel jenis pola", "Tabel rumus suku ke-n"]
  english_terms: [pattern recognition, sequence, term, common difference, ratio, repeating pattern, period, loop]
---

# Pelajaran 2 — Pengenalan Pola

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Mengenali pola **bertambah/berkurang tetap**, **berlipat**, **berulang**,
   dan **pola gambar**.
2. Menghitung **suku ke-n** pola bertambah tetap.
3. Memakai pola untuk **menyederhanakan instruksi** (gagasan perulangan).

## Mengapa ini penting?

Komputer sangat baik mengulang. Bila kamu melihat bagian yang berulang,
kamu cukup menjelaskannya sekali dan berkata "ulangi". Pola juga membantu
memperkirakan nilai yang belum diamati.

## 1. Jenis pola bilangan

| Jenis | Cara mengenali | Contoh | Berikutnya |
|---|---|---|---|
| Bertambah tetap | Selisih berurutan sama | 3, 8, 13, 18 (selisih 5) | 23 |
| Berkurang tetap | Selisih sama, negatif | 100, 94, 88 (selisih −6) | 82 |
| Berlipat | Hasil bagi berurutan sama | 5, 10, 20, 40 (× 2) | 80 |
| Berulang | Urutan yang sama muncul lagi | ganjil, genap, ganjil, genap | ganjil |

**Selalu periksa lebih dari dua suku.** 2, 4 bisa "+2" atau "×2"; suku
ketiga membedakan kedua dugaan ini (6 atau 8).

*Catatan:* pola yang cocok dengan data hanyalah **dugaan yang masuk akal**,
bukan bukti. Data yang terbatas selalu dapat dilanjutkan dengan lebih dari
satu cara. Karena itu soal W7 menyebut jenis polanya (mis. "bertambah
tetap") atau meminta "menurut pola" yang paling sederhana dan cocok dengan
semua suku yang diberikan.

## 2. Suku ke-n pola bertambah tetap

`suku ke-n = suku pertama + beda × (n − 1)`

Pola 3, 8, 13, 18: suku pertama 3, beda 5. Suku ke-20 = 3 + 5 × 19 = 98.

Mengapa (n − 1)? Dari suku pertama ke suku ke-n ada n − 1 langkah.

## 3. Pola berulang dan sisa bagi

Pola berulang dengan **periode** p (banyak anggota sebelum berulang) memakai
sisa pembagian (W5). Contoh "ganjil, genap" periode 2: suku ke-n ganjil bila
sisa n ÷ 2 = 1.

Contoh periode 4: musim tanam di kebun sekolah berganti `tanam, siram,
pupuk, panen, tanam, …`. Kegiatan ke-11? 11 ÷ 4 = 2 sisa 3 → anggota ke-3:
pupuk. (Bila sisa 0, ambil anggota **terakhir**.)

## 4. Pola gambar

*Deskripsi diagram dg-w07-02:* huruf L dari 3, 5, 7 kotak.

Hitung banyak benda di setiap susunan, lalu cari pola bilangannya: 3, 5, 7
bertambah 2 → susunan ke-10 = 3 + 2 × 9 = 21 kotak.

## 5. Pola dalam instruksi

Langkah "ambil satu buku, beri label, letakkan di rak" untuk 40 buku cukup
ditulis sekali, lalu "ulangi untuk setiap buku". Ini gagasan **perulangan**
yang dipakai di W8 dan W12.

## 6. Contoh terbimbing

**Soal:** Tabungan Rudi: Rp7.000, Rp11.000, Rp15.000, … (bertambah tetap).
Berapa tabungan pada minggu ke-9?

1. Selisih 4.000 (periksa: 11.000 − 7.000 = 15.000 − 11.000).
2. Suku ke-9 = 7.000 + 4.000 × 8 = 39.000.

## 7. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Suku ke-n = beda × n" | Suku pertama + beda × (n − 1) |
| "Dua suku cukup untuk menentukan pola" | Periksa minimal tiga; pola tetap dugaan kecuali jenisnya disebut |
| "Pola berulang dihitung dengan membagi biasa" | Pakai sisa bagi; sisa 0 = anggota terakhir |

## 8. Latihan terbimbing (`mod-w07.prac-02`, tidak dinilai)

1. 11, 14, 17, 20, … suku ke-15?
2. 3, 9, 27, … suku berikutnya?
3. Pola `A, B, C, A, B, C, …` huruf ke-30?
4. Susunan kotak 4, 7, 10, … susunan ke-6?

## 9. Cek pemahaman (tidak dinilai)

- Bagaimana pola membantu menulis instruksi yang lebih pendek?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 11 + 3 × 14 = 53.
2. × 3 → 81.
3. 30 ÷ 3 = 10 sisa 0 → anggota terakhir: C.
4. 4 + 3 × 5 = 19.

Cek pemahaman: bagian berulang ditulis sekali lalu diulang.

## Ringkasan

- Bertambah/berkurang tetap: suku ke-n = suku pertama + beda × (n − 1).
- Berlipat: dikali angka yang sama.
- Berulang: sisa bagi dengan periode.
- Bagian berulang dalam instruksi → perulangan.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Suku | term | Anggota pola |
| Beda | common difference | Selisih tetap antarsuku |
| Periode | period | Panjang bagian yang berulang |
| Perulangan | loop | Langkah yang diulang |
