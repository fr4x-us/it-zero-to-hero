---
lesson_id: mod-w07.les-03
practice_id: mod-w07.prac-03
module_id: mod-w07
content_version: "1.0"
title: "Abstraksi dan Generalisasi"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w07-abstract-01]
prerequisites: [mod-w07.les-02]
accessibility:
  diagrams:
    - id: dg-w07-03
      alt: "Foto jalan di samping denah sederhana yang sama."
      long_description: >
        Kiri: gambar kota dengan banyak rumah, pohon, dan kendaraan. Kanan:
        denah sederhana yang hanya berisi garis jalan dan tiga titik halte
        bernama. Panah dari kiri ke kanan berlabel abstraksi.
  tables_with_core_data: ["Tabel relevan vs tidak relevan", "Tabel khusus vs umum"]
  english_terms: [abstraction, relevant information, detail, model, generalization, parameter]
---

# Pelajaran 3 — Abstraksi dan Generalisasi

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Memilih informasi yang **relevan** untuk tujuan tertentu.
2. Menjelaskan mengapa model sederhana (peta, denah) berguna.
3. **Menggeneralisasi** perhitungan khusus menjadi rumus bervariabel.

## Mengapa ini penting?

Dunia penuh detail. Program yang baik hanya menyimpan dan memproses detail
yang dibutuhkan. Aplikasi ojek tidak perlu tahu warna rumahmu, tetapi butuh
lokasimu.

## 1. Relevan menurut tujuan

**Abstraksi** = memilih informasi yang penting untuk **tujuan tertentu** dan
mengabaikan detail yang tidak berpengaruh. Pertanyaan kuncinya:
**"Bila informasi ini berubah, apakah hasilnya berubah?"**

Tujuan: menentukan **ongkos kirim** paket.

| Informasi | Mengubah ongkos? | Relevan? |
|---|---|---|
| Berat paket | Ya | Ya |
| Jarak kirim | Ya | Ya |
| Warna kardus | Tidak | Tidak |
| Nama pengirim | Tidak | Tidak |

Informasi yang sama dapat relevan untuk tujuan lain: nama pengirim tidak
relevan untuk ongkos, tetapi relevan untuk label paket.

## 2. Model sederhana

*Deskripsi diagram dg-w07-03:* gambar kota yang rinci → denah berisi jalan
dan halte.

Denah, peta jalur, dan tabel jadwal adalah **model**: versi sederhana
kenyataan yang hanya memuat yang penting bagi pemakainya. Model yang baik
tidak "salah" karena kurang detail; ia **cukup** untuk tujuannya.

## 3. Generalisasi

Perhitungan **khusus** memakai angka tertentu; rumus **umum** mengganti angka
yang dapat berubah dengan **variabel** (W5).

| Khusus | Umum |
|---|---|
| Luas kebun 8 m × 5 m = 40 m² | `luas = p × l` |
| Ongkos 4 kg × Rp9.000 | `ongkos = berat × tarif` |
| Waktu 120 km ÷ 60 km/jam | `waktu = jarak ÷ kecepatan` |

Rumus umum dapat dipakai berkali-kali untuk nilai yang berbeda — persis yang
dilakukan program.

## 4. Contoh terbimbing

**Soal:** Tujuan: menentukan **berapa kotak** yang diperlukan untuk membawa
buku perpustakaan. Informasi: banyak buku, isi satu kotak, warna kotak, judul
buku. Mana yang relevan? Tulis rumus umumnya.

1. Banyak buku dan isi satu kotak mengubah jawaban → relevan.
2. Warna kotak dan judul buku tidak mengubah jumlah kotak → tidak relevan.
3. Rumus: `kotak = banyak buku ÷ isi kotak`, dibulatkan **ke atas** (W5).

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Makin banyak informasi makin baik" | Informasi tidak relevan mengaburkan masalah |
| "Informasi tidak relevan selamanya tidak berguna" | Relevan atau tidak bergantung pada tujuan |
| "Rumus dengan angka khusus sudah umum" | Umum bila angka yang dapat berubah diganti variabel |

## 6. Latihan terbimbing (`mod-w07.prac-03`, tidak dinilai)

1. Tujuan: menentukan **jam selesai** menonton film. Informasi: jam mulai,
   durasi film, judul film, harga tiket. Mana yang relevan?
2. Generalisasi: "keliling persegi bersisi 6 cm = 4 × 6".
3. Mengapa jadwal kereta tidak mencantumkan warna kursi?

## 7. Cek pemahaman (tidak dinilai)

- Sebutkan satu informasi yang relevan untuk satu tujuan tetapi tidak
  relevan untuk tujuan lain.

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Jam mulai dan durasi film.
2. `keliling = 4 × s`.
3. Penumpang memakai jadwal untuk memilih waktu berangkat; warna kursi tidak
   mengubahnya.

## Ringkasan

- Abstraksi: pilih yang mengubah hasil untuk tujuan ini.
- Model sederhana cukup untuk tujuannya.
- Generalisasi: ganti angka khusus dengan variabel.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Abstraksi | abstraction | Memilih yang penting untuk tujuan tertentu |
| Relevan | relevant | Dapat mengubah hasil |
| Model | model | Versi sederhana kenyataan |
| Generalisasi | generalization | Membuat aturan khusus berlaku umum |
