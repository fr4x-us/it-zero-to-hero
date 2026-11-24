---
lesson_id: mod-w05.les-04
practice_id: mod-w05.prac-04
module_id: mod-w05
content_version: "1.0"
title: "Desimal, Pembulatan, dan Menyusun Anggaran"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w05-round-01, comp-w05-pct-01, comp-w05-divmod-01]
prerequisites: [mod-w05.les-02, mod-w05.les-03]
accessibility:
  diagrams:
    - id: dg-w05-04
      alt: "Garis bilangan antara 4,6 dan 4,7."
      long_description: >
        Garis dari 4,60 sampai 4,70 dengan titik tengah 4,65. Titik 4,63
        lebih dekat ke 4,6; titik 4,68 lebih dekat ke 4,7; titik 4,65 tepat
        di tengah dan menurut aturan W5 dibulatkan ke atas menjadi 4,7.
  tables_with_core_data: ["Tabel aturan pembulatan", "Tabel ke atas/ke bawah", "Tabel anggaran contoh"]
  english_terms: [rounding, decimal place, round half up, round up, round down, budget, subtotal, percentage share]
---

# Pelajaran 4 — Desimal, Pembulatan, dan Menyusun Anggaran

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Membulatkan bilangan desimal ke **n angka di belakang koma** dan ke
   **bilangan bulat** menurut aturan W5.
2. Memilih **pembulatan ke atas** atau **ke bawah** sesuai kebutuhan
   (wadah, pembelian).
3. Menyusun **tabel anggaran**: subtotal, total, sisa, dan persen bagian.

## Mengapa ini penting?

Hasil bagi sering tidak bulat: 7 ÷ 3 = 2,333… Komputer dan laporan harus
memutuskan berapa angka yang ditampilkan dan ke arah mana dibulatkan.
Keputusan yang salah membuat bus kurang satu atau anggaran tampak cukup
padahal tidak.

## 1. Tempat desimal

Pada `25,374`: 3 = persepuluhan (satu angka di belakang koma), 7 =
perseratusan (dua angka), 4 = perseribuan (tiga angka).

## 2. Aturan pembulatan W5

1. Tentukan tempat pembulatan (mis. satu angka di belakang koma).
2. Lihat **satu** angka tepat setelah tempat itu.
3. Bila angka itu **5 atau lebih → naik**; bila **kurang dari 5 → tetap**.
4. Buang angka di belakangnya.

*Deskripsi diagram dg-w05-04:* 4,63 → 4,6; 4,68 → 4,7; 4,65 → 4,7.

| Bilangan | Dibulatkan ke | Angka yang dilihat | Hasil |
|---|---|---|---|
| 4,63 | 1 desimal | 3 | 4,6 |
| 4,65 | 1 desimal | 5 | 4,7 |
| 7,96 | 1 desimal | 6 | 8,0 |
| 15,2 | bilangan bulat | 2 | 15 |
| 2,135 | 2 desimal | 5 | 2,14 |

**Jangan membulatkan bertahap.** 5,347 ke satu desimal: lihat angka 4 →
5,3. Bila salah dibulatkan dulu ke 5,35 lalu ke 5,4, hasilnya keliru.

**Pertahankan nol yang diminta.** 7,96 ke satu desimal ditulis `8,0`, bukan
`8`, karena soal meminta satu angka di belakang koma.

*Catatan cakupan:* aturan ini dipakai W5 untuk bilangan **positif**.
Pembulatan bilangan negatif dan cara pembulatan lain yang dipakai beberapa
program tidak dinilai di W5.

## 3. Ke atas atau ke bawah?

Kadang yang ditanya bukan "terdekat", tetapi "cukup" atau "terjangkau".

| Pertanyaan | Arah | Contoh |
|---|---|---|
| Berapa wadah/kendaraan paling sedikit agar semua tertampung? | **Ke atas** | 50 orang, mobil 8 orang: 50 ÷ 8 = 6,25 → 7 mobil |
| Berapa barang paling banyak yang dapat dibeli dengan uang ini? | **Ke bawah** (hasil bagi) | Rp30.000, harga Rp4.000: 30.000 ÷ 4.000 = 7,5 → 7 barang |

## 4. Menyusun tabel anggaran

| Langkah | Rumus |
|---|---|
| Subtotal setiap baris | banyaknya × harga satuan (dikurangi diskon baris bila ada) |
| Total | jumlah semua subtotal |
| Sisa | anggaran − total |
| Persen terpakai | total ÷ anggaran × 100% |
| Persen bagian baris | subtotal ÷ total × 100% (nilai dasar = **total**) |

**Contoh anggaran kecil** (anggaran Rp100.000):

| Baris | Banyaknya × harga | Subtotal | Persen bagian (1 desimal) |
|---|---|---|---|
| Spidol | 3 × Rp9.000 | 27.000 | 27.000 ÷ 64.000 = 42,1875% → 42,2 |
| Map plastik | 5 × Rp2.600 | 13.000 | 20,3125% → 20,3 |
| Kertas HVS | 1 × Rp24.000 | 24.000 | 37,5% → 37,5 |
| **Total** | | **64.000** | 100,0 |

Sisa = 36.000; persen terpakai = 64.000 ÷ 100.000 = 64,0%.

Persen bagian dibulatkan **masing-masing**, sehingga jumlahnya **bisa**
99,9 atau 100,1 pada data lain. Itu wajar, bukan tanda salah hitung.

## 5. Contoh terbimbing

**Soal:** Dari sisa Rp36.000 di atas, berapa paket fotokopi Rp5.000 paling
banyak yang dapat dibayar, dan berapa sisa uangnya?

1. 36.000 ÷ 5.000: 5.000 × 7 = 35.000 ≤ 36.000 → 7 paket (ke bawah).
2. Sisa 36.000 − 35.000 = 1.000.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Pembulatan selalu ke bawah" | Ke angka terdekat, kecuali soal meminta ke atas/ke bawah |
| "`8,0` sama dengan `8`, jadi boleh ditulis `8`" | Nilainya sama, tetapi soal meminta satu desimal |
| "Bulatkan setiap langkah agar mudah" | Bulatkan hasil akhir saja |
| "Persen bagian dihitung terhadap anggaran" | Terhadap total belanja bila soal meminta bagian belanja |

## 7. Latihan terbimbing (`mod-w05.prac-04`, tidak dinilai)

1. Bulatkan 6,85 ke satu desimal.
2. Bulatkan 0,994 ke dua desimal.
3. 38 kursi dibutuhkan; satu baris berisi 9 kursi. Berapa baris paling
   sedikit?
4. Rp45.000 untuk membeli tiket Rp8.000. Berapa tiket paling banyak?
5. Anggaran Rp80.000, total belanja Rp52.000. Persen terpakai (1 desimal)?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa 50 orang dengan mobil berisi 8 butuh 7 mobil walaupun 6,25
  "lebih dekat" ke 6?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Angka berikutnya 5 → 6,9.
2. Angka berikutnya 4 → 0,99.
3. 38 ÷ 9 = 4,22… → 5 baris (ke atas).
4. 45.000 ÷ 8.000 = 5,625 → 5 tiket (ke bawah).
5. 52.000 ÷ 80.000 = 0,65 → 65,0%.

Cek pemahaman: 6 mobil hanya memuat 48 orang; 2 orang tertinggal.

## Ringkasan

- Lihat satu angka setelah tempat pembulatan; ≥ 5 naik.
- Tulis banyak desimal sesuai permintaan (`8,0`).
- Kebutuhan wadah → ke atas; pembelian maksimal → ke bawah.
- Anggaran: subtotal → total → sisa → persen.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Pembulatan | rounding | Menyederhanakan bilangan ke tempat tertentu |
| Ke atas | round up | Ke bilangan bulat berikutnya bila ada sisa |
| Ke bawah | round down | Membuang bagian pecahan |
| Subtotal | subtotal | Jumlah satu baris |
| Anggaran | budget | Batas uang yang direncanakan |
