---
lesson_id: mod-w05.les-02
practice_id: mod-w05.prac-02
module_id: mod-w05
content_version: "1.0"
title: "Hasil Bagi, Sisa, Satuan, dan Perbandingan"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w05-divmod-01, comp-w05-unit-01]
prerequisites: [mod-w05.les-01]
accessibility:
  diagrams:
    - id: dg-w05-02
      alt: "23 titik dikelompokkan per 5."
      long_description: >
        Empat kelompok berisi lima titik dan satu kelompok kecil berisi tiga
        titik. Label: hasil bagi 4 (kelompok penuh), sisa 3 (titik yang
        tidak membentuk kelompok penuh).
    - id: dg-w05-02b
      alt: "Lingkaran tujuh hari."
      long_description: >
        Tujuh kotak membentuk lingkaran: Senin, Selasa, Rabu, Kamis, Jumat,
        Sabtu, Minggu, lalu kembali ke Senin. Panah menunjukkan bahwa maju
        tujuh hari kembali ke hari yang sama.
  tables_with_core_data: ["Tabel hasil bagi dan sisa", "Tabel konversi satuan"]
  english_terms: [quotient, remainder, divisible, modulo, unit conversion, ratio, proportion]
---

# Pelajaran 2 — Hasil Bagi, Sisa, Satuan, dan Perbandingan

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menentukan **hasil bagi** dan **sisa** pembagian bilangan bulat.
2. Memakai sisa untuk **keterbagian** dan **siklus** (hari, kelompok).
3. **Mengonversi satuan** waktu, massa, dan volume.
4. Memakai **perbandingan senilai** (resep, harga satuan).

## Mengapa ini penting?

Di komputer, banyak perhitungan memakai hasil bagi dan sisa: membagi data ke
halaman (20 data per halaman), menentukan hari dalam minggu, atau mengubah
detik menjadi menit dan detik. Satuan yang tertukar menyebabkan kesalahan
besar — 1 jam bukan 100 menit.

## 1. Hasil bagi dan sisa

Saat 23 dibagi 5 **tanpa pecahan**, kita bertanya: berapa kelompok penuh
berisi 5, dan berapa yang tersisa?

*Deskripsi diagram dg-w05-02:* 23 titik membentuk 4 kelompok penuh dan
sisa 3.

| Bilangan | Pembagi | Hasil bagi | Sisa | Periksa |
|---|---|---|---|---|
| 23 | 5 | 4 | 3 | 4 × 5 + 3 = 23 |
| 30 | 6 | 5 | 0 | 5 × 6 + 0 = 30 |
| 7 | 9 | 0 | 7 | 0 × 9 + 7 = 7 |

Aturan W5 (bilangan bulat tidak negatif, pembagi positif):

- **hasil bagi × pembagi + sisa = bilangan yang dibagi**;
- sisa selalu **0 sampai pembagi − 1**.

Cara mencari: cari kelipatan pembagi **terbesar** yang tidak melebihi
bilangannya. Untuk 61 ÷ 8: 8 × 7 = 56 ≤ 61, 8 × 8 = 64 > 61 → hasil bagi 7,
sisa 61 − 56 = 5.

**Keterbagian.** Bilangan **habis dibagi** bila sisanya 0. Bilangan
**genap** bersisa 0 bila dibagi 2; **ganjil** bersisa 1.

## 2. Sisa untuk siklus

*Deskripsi diagram dg-w05-02b:* tujuh hari membentuk lingkaran.

Hari berulang setiap 7 hari, jadi untuk "hari apa n hari lagi" cukup lihat
**sisa** n ÷ 7. Contoh: hari ini Selasa, 30 hari lagi? 30 = 7 × 4 + 2 → maju
2 hari: Kamis.

Contoh lain: 75 detik = 1 menit (hasil bagi 75 ÷ 60) lebih 15 detik (sisa).

## 3. Konversi satuan

| Besaran | Hubungan | Catatan |
|---|---|---|
| Waktu | 1 jam = 60 menit; 1 menit = 60 detik | **Bukan** sistem 100 |
| Massa | 1 kg = 1.000 g | |
| Volume | 1 liter = 1.000 mL | |

**Ke satuan lebih kecil → kali; ke satuan lebih besar → bagi.**

Contoh: 1 jam 50 menit = 60 + 50 = 110 menit. 0,25 kg = 0,25 × 1.000 = 250 g.
200 menit = 3 jam (hasil bagi 200 ÷ 60) lebih 20 menit (sisa).

**Rantai konversi.** Keran 200 mL per detik mengisi ember 12 liter:
12 liter = 12.000 mL; 12.000 ÷ 200 = 60 detik = 1 menit. Ubah ke satuan
yang sama **sebelum** membagi.

## 4. Perbandingan senilai

Bila satu besaran dikali, besaran lain ikut dikali dengan angka yang sama.
Cara aman: hitung **satu satuan** dulu.

Contoh: 5 pensil Rp10.000 → satu pensil Rp2.000 → 8 pensil Rp16.000.
Contoh: 3 sendok gula untuk 2 gelas → 12 gelas = 6 kali → 18 sendok.

## 5. Contoh terbimbing

**Soal:** 92 siswa dibagi ke kelompok berisi 8. Berapa kelompok penuh,
dan berapa siswa yang belum masuk kelompok penuh?

1. 8 × 11 = 88 ≤ 92; 8 × 12 = 96 > 92 → 11 kelompok penuh.
2. Sisa 92 − 88 = 4 siswa.
3. Periksa: 11 × 8 + 4 = 92.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Sisa boleh lebih besar dari pembagi" | Bila sisa ≥ pembagi, masih ada satu kelompok penuh lagi |
| "2 jam 30 menit = 2,3 jam" | 30 menit = 0,5 jam → 2,5 jam |
| "1,5 kg = 1 kg 5 g" | 0,5 kg = 500 g → 1.500 g |
| "Perbandingan senilai = menambah selisih" | Senilai berarti **dikali** dengan angka yang sama |

## 7. Latihan terbimbing (`mod-w05.prac-02`, tidak dinilai)

1. 58 ÷ 9: hasil bagi dan sisa?
2. Hari ini Sabtu. Hari apa 20 hari lagi?
3. 1 jam 35 menit = … menit.
4. 4 botol jus Rp18.000 (harga per botol sama). Harga 10 botol?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa maju 14 hari selalu kembali ke hari yang sama?
- Mengapa satuan harus disamakan sebelum membagi?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 9 × 6 = 54 ≤ 58 → hasil bagi 6, sisa 4.
2. 20 = 7 × 2 + 6 → maju 6 hari dari Sabtu: Jumat.
3. 60 + 35 = 95 menit.
4. Satu botol 4.500 → 10 botol Rp45.000.

Cek pemahaman: 14 = 7 × 2, sisa 0; satuan berbeda tidak dapat dibandingkan
atau dibagi langsung.

## Ringkasan

- Hasil bagi × pembagi + sisa = bilangan; sisa 0 sampai pembagi − 1.
- Sisa ÷ 7 untuk hari; sisa ÷ 60 untuk menit/detik.
- Ke satuan kecil kali, ke satuan besar bagi; samakan satuan dulu.
- Perbandingan senilai: hitung satu satuan dulu.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Hasil bagi | quotient | Banyaknya kelompok penuh |
| Sisa | remainder | Bagian yang tidak membentuk kelompok penuh |
| Habis dibagi | divisible | Sisa 0 |
| Konversi satuan | unit conversion | Mengubah satuan tanpa mengubah besarnya |
| Perbandingan senilai | direct proportion | Dua besaran naik atau turun dengan faktor yang sama |
