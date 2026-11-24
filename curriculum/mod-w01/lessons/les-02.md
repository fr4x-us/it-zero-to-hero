---
lesson_id: mod-w01.les-02
practice_id: mod-w01.prac-02
module_id: mod-w01
content_version: "1.0"
title: "Komponen Hardware: CPU, RAM, Penyimpanan, dan Perangkat Input/Output"
language: id
duration_minutes: 55        # materi 40 + latihan terbimbing 15
competencies: [comp-w01-cpu-01, comp-w01-mem-01, comp-w01-unit-01, comp-w01-ipos-01]
prerequisites: [mod-w01.les-01]
accessibility:
  diagrams:
    - id: dg-w01-02
      alt: "Diagram hubungan CPU, RAM, dan penyimpanan di motherboard."
      long_description: >
        Kotak besar bertuliskan Motherboard berisi tiga kotak: CPU di tengah,
        RAM di kanan, dan Penyimpanan (SSD/HDD) di bawah. Panah dari
        Penyimpanan ke RAM bertuliskan "program dan data dimuat", panah dua
        arah antara RAM dan CPU bertuliskan "data yang sedang dipakai".
        Kotak PSU di luar motherboard dengan panah "listrik" ke motherboard.
  tables_with_core_data: [tbl-units]
  english_terms: [CPU, core, clock speed, RAM, volatile, storage, SSD, HDD, motherboard, PSU, GPU, port, USB, HDMI]
---

# Pelajaran 2 — Komponen Hardware

## Tujuan pelajaran

1. Menjelaskan peran **CPU**, **RAM**, **penyimpanan**, **motherboard**,
   **PSU**, dan **GPU**.
2. Membedakan memori **volatil** (RAM) dan penyimpanan **non-volatil**
   (SSD/HDD), serta SSD dan HDD.
3. Memakai satuan data **bit, byte, KB, MB, GB, TB** dan satuan kecepatan
   **GHz**.
4. Mengelompokkan perangkat menjadi input, output, input-dan-output,
   penyimpanan, atau pemrosesan, serta mengenali port umum.

## Mengapa ini penting?

Saat membeli laptop, memperbaiki ponsel yang lambat, atau kelak menulis
program, kamu perlu tahu **komponen mana yang mengerjakan apa**. Program
yang berat bergantung pada CPU dan RAM; berkas yang hilang setelah listrik
padam berkaitan dengan beda RAM dan penyimpanan.

## 1. Gambaran besar

```
┌──────────────────── MOTHERBOARD ────────────────────┐
│                                                      │
│            ┌───────┐  data yang    ┌───────┐         │
│            │  CPU  │◄─────────────►│  RAM  │         │
│            └───────┘  sedang dipakai└───▲───┘         │
│                                        │ program dan  │
│                                        │ data dimuat  │
│                                  ┌─────┴──────┐       │
│                                  │ SSD / HDD  │       │
│                                  └────────────┘       │
└──────────────────────────▲───────────────────────────┘
                           │ listrik
                       ┌───┴───┐
                       │  PSU  │
                       └───────┘
```

*Deskripsi diagram dg-w01-02:* lihat metadata di atas.

## 2. CPU — otak pengolah instruksi

**CPU** (*Central Processing Unit*, prosesor) menjalankan instruksi
program: menghitung, membandingkan, dan memindahkan data.

| Spesifikasi | Arti | Contoh |
|---|---|---|
| **Core** | Unit pengolah di dalam CPU. CPU 6 core dapat mengerjakan beberapa tugas secara bersamaan | 4 core, 6 core, 8 core |
| **Kecepatan clock** | Jumlah siklus kerja per detik. 1 GHz = 1 miliar siklus per detik. Clock **bukan** jumlah instruksi per detik: berapa instruksi selesai per siklus bergantung rancangan CPU | 3,6 GHz |

**Analogi:** core seperti **juru masak** di dapur. Empat juru masak dapat
menyiapkan empat hidangan bersamaan, tetapi **satu** hidangan yang harus
dimasak berurutan tidak otomatis selesai empat kali lebih cepat.

Penting: lebih banyak core membantu bila pekerjaan **dapat dibagi** (misalnya
banyak aplikasi terbuka bersamaan). Program yang mengerjakan langkahnya satu
per satu tidak menjadi lebih cepat hanya karena core bertambah. Kecepatan
juga dipengaruhi faktor lain (generasi CPU, RAM, penyimpanan), sehingga
angka GHz saja tidak cukup untuk membandingkan dua CPU yang berbeda generasi.

## 3. RAM — meja kerja sementara

**RAM** (*Random Access Memory*) menyimpan program dan data **yang sedang
dipakai** agar CPU dapat mengaksesnya dengan sangat cepat.

- RAM bersifat **volatil** (*volatile*): isinya **hilang saat listrik
  mati**.
- Pada laptop dan komputer meja, bila RAM penuh, sistem operasi memakai
  sebagian penyimpanan sebagai cadangan yang jauh lebih lambat, sehingga
  komputer terasa lambat. Ponsel biasanya menutup aplikasi di latar
  belakang. *(Model sederhana; rinciannya bergantung sistem operasi.)*

**Analogi:** RAM adalah **meja kerja**; penyimpanan adalah **lemari arsip**.
Berkas diambil dari lemari ke meja agar mudah dikerjakan. Meja yang lebih
luas memungkinkan lebih banyak pekerjaan terbuka. Saat pulang (listrik
mati), meja dibersihkan — yang tidak dikembalikan ke lemari akan hilang.

## 4. Penyimpanan — lemari arsip (non-volatil)

Penyimpanan (*storage*) bersifat **non-volatil**: data tetap ada walau
listrik mati. Non-volatil **tidak** berarti kebal: data tetap dapat rusak
atau hilang karena kerusakan media, terhapus tidak sengaja, atau program
jahat — karena itu berkas penting perlu dicadangkan (*backup*).

| | SSD (*Solid State Drive*) | HDD (*Hard Disk Drive*) |
|---|---|---|
| Cara kerja | Chip memori flash, **tanpa** bagian yang bergerak | Piringan magnetis yang **berputar** dan lengan baca yang bergerak |
| Kecepatan | Jauh lebih cepat membuka program dan berkas | Lebih lambat karena menunggu piringan berputar dan lengan bergerak |
| Ketahanan terhadap guncangan | Lebih tahan | Lebih rentan karena ada bagian mekanis |
| Harga per GB | Umumnya lebih mahal | Umumnya lebih murah |

Flashdisk USB dan kartu memori juga penyimpanan non-volatil.

**Mengapa dokumen yang belum disimpan hilang saat listrik padam?** Karena
dokumen itu baru ada di **RAM**. Menekan "Simpan" menyalinnya ke
**penyimpanan**.

## 5. Motherboard, PSU, dan GPU

| Komponen | Peran |
|---|---|
| **Motherboard** (papan induk) | Papan sirkuit utama tempat CPU, RAM, dan penyimpanan terpasang dan saling berkomunikasi. Menentukan jenis CPU dan RAM yang dapat dipakai (Pelajaran 4) |
| **PSU** (*Power Supply Unit*) | Mengubah listrik dari stopkontak menjadi listrik yang sesuai untuk komponen. Kapasitasnya dalam **watt (W)** |
| **GPU** (*Graphics Processing Unit*) | Prosesor khusus untuk mengolah gambar dan tampilan. Bisa terpadu di dalam CPU (*integrated graphics*) atau berupa kartu terpisah |

## 6. Satuan data dan kecepatan

Komputer menyimpan data sebagai **bit** (*binary digit*), yaitu 0 atau 1.
Cara kerja angka biner dipelajari di modul W6; di sini cukup mengenal
satuannya.

<a id="tbl-units"></a>

| Satuan | Nilai (aturan desimal yang dipakai di modul ini) |
|---|---|
| 1 **byte** (B) | 8 bit |
| 1 **kilobyte** (KB) | 1.000 byte |
| 1 **megabyte** (MB) | 1.000 KB |
| 1 **gigabyte** (GB) | 1.000 MB |
| 1 **terabyte** (TB) | 1.000 GB |

*Deskripsi tabel tbl-units:* setiap satuan bernilai 1.000 kali satuan di
bawahnya, kecuali 1 byte = 8 bit.

**Arah konversi:**

| Dari → ke | Operasi | Contoh |
|---|---|---|
| Satuan besar → satuan kecil (mis. GB → MB) | × 1.000 per tingkat | 2 GB = 2 × 1.000 = 2.000 MB |
| Satuan kecil → satuan besar (mis. MB → GB) | ÷ 1.000 per tingkat | 5.000 MB = 5.000 ÷ 1.000 = 5 GB |
| Dua tingkat (TB → MB) | × 1.000 × 1.000 | 1 TB = 1 × 1.000 × 1.000 = 1.000.000 MB |
| Dua tingkat (KB → GB) | ÷ 1.000 ÷ 1.000 | 3.000.000 KB = 3.000.000 ÷ 1.000 ÷ 1.000 = 3 GB |

**Catatan penting:** produsen penyimpanan memakai aturan desimal di atas.
Sebagian sistem operasi menghitung dengan kelipatan **1.024** dan menamainya
KiB, MiB, GiB. Karena itu SSD "1 TB" (1.000.000.000.000 byte) dapat tampil
sekitar **931 GiB** — kapasitasnya tidak berkurang, hanya cara hitungnya
berbeda. **Semua latihan dan soal W1 memakai aturan desimal.**

### Contoh terbimbing: konversi dan kapasitas

1. **2 GB berapa MB?** 2 × 1.000 = **2.000 MB**.
2. **Berapa foto 4 MB muat di kartu 64 GB?** 64 GB = 64.000 MB;
   64.000 ÷ 4 = **16.000 foto** (abaikan ruang yang dipakai sistem).
3. **Kecepatan:** CPU 3,6 GHz menjalankan 3,6 miliar siklus per detik.

## 7. Perangkat input, output, dan port

| Kelompok | Contoh |
|---|---|
| Input | Keyboard, mouse, touchpad, mikrofon, webcam, scanner |
| Output | Monitor, speaker, earphone, printer yang hanya mencetak, proyektor |
| Input dan output | Layar sentuh, headset dengan mikrofon, printer multifungsi yang juga memindai |
| Penyimpanan | SSD, HDD, flashdisk, kartu memori |
| Pemrosesan | CPU, GPU |

**Port** adalah colokan untuk menghubungkan perangkat:

| Port | Kegunaan umum |
|---|---|
| USB | Keyboard, mouse, flashdisk, pengisian daya, banyak perangkat lain |
| HDMI | Mengirim gambar dan suara ke monitor/TV/proyektor |
| Audio 3,5 mm | Earphone, speaker, mikrofon |

## 8. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "RAM 16 GB berarti saya bisa menyimpan 16 GB berkas." | RAM tidak menyimpan berkas setelah listrik mati; kapasitas berkas ditentukan penyimpanan |
| "GHz lebih tinggi pasti lebih cepat." | Generasi CPU, jumlah core, RAM, dan penyimpanan juga berpengaruh |
| "SSD menyimpan data hanya selama listrik menyala." | SSD non-volatil; yang volatil adalah RAM |
| "8 core selalu dua kali lebih cepat dari 4 core." | Hanya membantu bila pekerjaan dapat dibagi |

## 9. Latihan terbimbing (`mod-w01.prac-02`, tidak dinilai)

1. Mengapa membuka banyak tab browser terasa lambat pada laptop dengan RAM
   kecil?
2. Hitung: 3 GB = … MB; 500 GB ÷ video 2.000 MB = … video.
3. Kelompokkan: pemindai kode batang (*barcode scanner*), plotter (printer
   gambar teknik), harddisk eksternal, prosesor ponsel, kacamata VR yang
   menampilkan gambar dan membaca gerakan kepala.
4. Port apa yang dipakai untuk menyambungkan laptop ke proyektor?

## 10. Cek pemahaman (tidak dinilai)

- Jelaskan dengan analogi meja dan lemari mengapa RAM dan penyimpanan
  berbeda.
- Sebutkan dua alasan SSD lebih cepat daripada HDD.

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Setiap tab memakai RAM; pada laptop, bila RAM penuh, sistem operasi
   memakai penyimpanan sebagai cadangan yang jauh lebih lambat.
2. 3.000 MB; 500 GB = 500.000 MB, 500.000 ÷ 2.000 = 250 video.
3. Pemindai kode batang → input; plotter → output; harddisk eksternal →
   penyimpanan; prosesor ponsel → pemrosesan; kacamata VR → input dan
   output.
4. HDMI (atau port video lain yang tersedia).

## Ringkasan

- CPU menjalankan instruksi; core = unit pengolah; GHz = siklus per detik.
- RAM cepat tetapi **volatil**; penyimpanan (SSD/HDD) **non-volatil**.
- SSD tanpa bagian bergerak sehingga lebih cepat; HDD memakai piringan
  berputar.
- Motherboard menghubungkan komponen; PSU memberi listrik (watt); GPU
  mengolah gambar.
- 1 byte = 8 bit; 1 KB = 1.000 byte, 1 MB = 1.000 KB, 1 GB = 1.000 MB,
  1 TB = 1.000 GB (aturan modul ini). Dari satuan besar ke kecil kalikan
  1.000 per tingkat; dari satuan kecil ke besar bagi 1.000 per tingkat.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Prosesor | CPU, *Central Processing Unit* | Komponen yang menjalankan instruksi |
| Inti prosesor | core | Unit pengolah di dalam CPU |
| Kecepatan clock | clock speed | Jumlah siklus per detik (GHz) |
| Memori akses acak | RAM | Memori kerja sementara yang volatil |
| Volatil | volatile | Isi hilang saat listrik mati |
| Penyimpanan | storage | Media yang menyimpan data tanpa listrik (non-volatil) |
| Papan induk | motherboard | Papan sirkuit utama |
| Catu daya | PSU, *Power Supply Unit* | Pemasok listrik komponen |
| Prosesor grafis | GPU | Pengolah gambar dan tampilan |
| Colokan | port | Titik sambung perangkat |
