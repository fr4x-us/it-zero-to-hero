---
lesson_id: mod-w06.les-01
practice_id: mod-w06.prac-01
module_id: mod-w06
content_version: "1.0"
title: "Bit, Basis 2, dan Biner ke Desimal"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w06-repr-01, comp-w06-bin2dec-01]
prerequisites: [mod-w05]
accessibility:
  diagrams:
    - id: dg-w06-01
      alt: "Tabel bobot posisi delapan bit."
      long_description: >
        Delapan kotak berjajar. Di atas kotak, dari kanan ke kiri, tertulis
        posisi 0 sampai 7. Di bawahnya bobot: 1, 2, 4, 8, 16, 32, 64, 128.
        Setiap bobot dua kali bobot di kanannya.
    - id: dg-w06-01b
      alt: "Tiga kotak berlabel bilangan biner, bilangan desimal, nilai Boolean."
      long_description: >
        Kotak pertama: bilangan biner 10111 subskrip 2, nilainya dua puluh
        tiga. Kotak kedua: bilangan desimal 10111 subskrip 10, dibaca sepuluh
        ribu seratus sebelas. Kotak ketiga: nilai Boolean 1 berarti benar,
        nilai Boolean 0 berarti salah.
  tables_with_core_data: ["Tabel basis 10 vs basis 2", "Tabel bobot posisi", "Tabel biner vs desimal vs Boolean"]
  english_terms: [bit, binary, base, place value, weight, least significant bit, most significant bit, Boolean value]
---

# Pelajaran 1 — Bit, Basis 2, dan Biner ke Desimal

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan **bit** dan **basis 2**.
2. Menentukan **bobot posisi** setiap bit.
3. Mengubah bilangan **biner ke desimal**.
4. Membedakan **bilangan biner**, **bilangan desimal**, dan **nilai
   Boolean**.

## Mengapa ini penting?

Di dalam komputer, semua data — angka, huruf, gambar — disimpan sebagai
deretan dua keadaan: ada arus/tidak, magnet arah ini/itu. Dua keadaan itu
ditulis **0** dan **1**. Memahami biner membantu kamu membaca ukuran data
(W1), alamat jaringan (W3), dan logika program (W8 dan seterusnya).

## 1. Basis 10 dan basis 2

Bilangan sehari-hari memakai **basis 10** (desimal): digit 0–9, dan setiap
posisi bernilai 10 kali posisi di kanannya.

| Basis | Digit | Bobot posisi dari kanan |
|---|---|---|
| 10 (desimal) | 0–9 | 1, 10, 100, 1.000, … |
| 2 (biner) | 0 dan 1 | 1, 2, 4, 8, 16, … |

Satu digit biner disebut **bit** (*binary digit*). Delapan bit disebut
**byte**.

Untuk membedakan basis, W6 menulis subskrip: `10111₂` (biner) dan
`10111₁₀` (desimal). Keduanya tampak sama, tetapi nilainya sangat berbeda.

## 2. Bobot posisi

Posisi dihitung **dari kanan, mulai 0**. Bobot = **2^posisi**.

*Deskripsi diagram dg-w06-01:* delapan bit, posisi 7 sampai 0, bobot 128,
64, 32, 16, 8, 4, 2, 1.

| Posisi | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Bobot | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Bit paling kanan (posisi 0) disebut **bit paling tidak berarti** (*LSB*);
bit paling kiri disebut **bit paling berarti** (*MSB*).

## 3. Biner ke desimal

**Langkah:** tulis bobot di atas setiap bit, ambil bobot yang bitnya **1**,
lalu jumlahkan.

**Contoh 1.** `10111₂`

| Bit | 1 | 0 | 1 | 1 | 1 |
|---|---|---|---|---|---|
| Bobot | 16 | 8 | 4 | 2 | 1 |

16 + 4 + 2 + 1 = **23**.

**Contoh 2 (8 bit).** `00101011₂`: bobot bit 1 adalah 32, 8, 2, 1 →
32 + 8 + 2 + 1 = **43**. **Nol di depan tidak menambah nilai:**
`00101011₂` = `101011₂`.

**Cara periksa cepat:** bilangan biner yang berakhiran 1 selalu ganjil
(posisi 0 berbobot 1); berakhiran 0 selalu genap.

## 4. Biner, desimal, dan nilai Boolean

*Deskripsi diagram dg-w06-01b:* `10111₂` = dua puluh tiga; `10111₁₀` =
sepuluh ribu seratus sebelas; Boolean 1 = benar, 0 = salah.

| Yang ditulis | Jenis | Artinya |
|---|---|---|
| `110₂` … | **Bilangan biner** | Jumlah yang ditulis dengan basis 2 |
| `110₁₀` | **Bilangan desimal** | Seratus sepuluh |
| `1` pada logika | **Nilai Boolean** | **Benar** (bukan "satu buah") |
| `0` pada logika | **Nilai Boolean** | **Salah** |

Nilai Boolean hanya punya dua kemungkinan dan **tidak dijumlahkan** seperti
bilangan. Di Pelajaran 3, `1` dan `0` dipakai untuk benar dan salah.

## 5. Contoh terbimbing

**Soal:** Berapa nilai desimal `111001₂`?

1. Bobot dari kanan: 1, 2, 4, 8, 16, 32.
2. Bit 1 ada di bobot 32, 16, 8, 1.
3. 32 + 16 + 8 + 1 = 57 … *periksa:* berakhiran 1 → ganjil ✓.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "`10₂` dibaca sepuluh" | `10₂` = 2 |
| "Posisi dihitung mulai 1" | Mulai 0, sehingga bit paling kanan berbobot 2⁰ = 1 |
| "Nol di depan membuat nilai lebih besar" | Nol di depan tidak mengubah nilai |
| "Boolean 1 + 1 = 2" | Nilai Boolean tidak dijumlahkan; operatornya AND/OR/NOT (Pelajaran 3) |

## 7. Latihan terbimbing (`mod-w06.prac-01`, tidak dinilai)

1. Bobot posisi 5?
2. `11100₂` = … (desimal).
3. `11000₁₀` dibaca apa? Dan `11000₂` bernilai berapa?
4. `00010111₂` = … (desimal).

## 8. Cek pemahaman (tidak dinilai)

- Mengapa bilangan biner yang berakhiran 0 selalu genap?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 2⁵ = 32.
2. 16 + 8 + 4 = 28.
3. `11000₁₀` = sebelas ribu; `11000₂` = 16 + 8 = 24.
4. 16 + 4 + 2 + 1 = 23 (sama dengan `10111₂`; nol di depan tidak
   mengubah nilai).

Cek pemahaman: semua bobot selain posisi 0 adalah kelipatan 2; bila bit
posisi 0 = 0, jumlahnya genap.

## Ringkasan

- Bit = 0 atau 1; byte = 8 bit.
- Bobot = 2^posisi, posisi dari kanan mulai 0.
- Biner → desimal: jumlahkan bobot bit 1.
- Bilangan biner ≠ nilai Boolean.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Bit | bit | Digit biner, 0 atau 1 |
| Byte | byte | 8 bit |
| Basis | base | Banyak digit dan faktor bobot sistem bilangan |
| Bobot posisi | place value, weight | Nilai yang dikalikan dengan digit pada posisi itu |
| Nilai Boolean | Boolean value | Benar (1) atau salah (0) |
