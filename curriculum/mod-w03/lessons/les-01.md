---
lesson_id: mod-w03.les-01
practice_id: mod-w03.prac-01
module_id: mod-w03
content_version: "1.0"
title: "Apa Itu Jaringan? Perangkat dan Peranannya"
language: id
duration_minutes: 40        # materi 30 + latihan terbimbing 10
competencies: [comp-w03-net-01]
prerequisites: [mod-w02]
accessibility:
  diagrams:
    - id: dg-w03-01
      alt: "Jaringan rumah: perangkat terhubung ke router Wi-Fi, router terhubung ke internet."
      long_description: >
        Di kiri ada tiga perangkat: laptop (kabel LAN), ponsel (Wi-Fi), dan
        printer (kabel LAN). Ketiganya terhubung ke kotak "router Wi-Fi
        rumah" yang di dalamnya tertulis: switch, access point, router.
        Dari router ada garis ke kotak modem, lalu ke awan bertuliskan
        Internet (ISP). Garis putus-putus mengelilingi perangkat dan router
        dengan label LAN.
  tables_with_core_data: ["Tabel LAN vs WAN", "Tabel peran perangkat jaringan"]
  english_terms: [network, LAN, WAN, internet, ISP, router, switch, access point, modem, client, server, Wi-Fi, Ethernet]
---

# Pelajaran 1 — Apa Itu Jaringan? Perangkat dan Peranannya

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan apa itu **jaringan komputer** dan membedakan **LAN**,
   **WAN**, dan **internet**.
2. Menjelaskan peran **router**, **switch**, **access point**, dan
   **modem**.
3. Membedakan **klien** (*client*) dan **server**.

## Mengapa ini penting?

Hampir semua yang kamu lakukan di ponsel — mengirim pesan, menonton video,
menyimpan foto ke awan — melewati jaringan. Saat "internet tidak jalan",
kamu perlu tahu bagian mana yang mungkin bermasalah: perangkatmu, jaringan
rumah, atau penyedia internet.

## 1. Jaringan komputer

**Jaringan komputer** adalah dua atau lebih perangkat yang terhubung
sehingga dapat **bertukar data** dan **berbagi sumber daya** (printer,
berkas, koneksi internet). Sambungannya dapat berupa **kabel** (mis. kabel
LAN/Ethernet) atau **nirkabel** (mis. Wi-Fi).

| | LAN (*Local Area Network*) | WAN (*Wide Area Network*) |
|---|---|---|
| Cakupan | Satu lokasi: rumah, kelas, kantor kecil | Wilayah luas: antarkota, antarnegara |
| Pemilik/pengelola | Biasanya pemilik lokasi | Biasanya perusahaan telekomunikasi |
| Contoh | Wi-Fi rumah | Jaringan yang menghubungkan cabang bank di banyak kota |

**Internet** adalah jaringan dari banyak sekali jaringan di seluruh dunia
yang saling terhubung. Rumahmu tersambung ke internet lewat **penyedia
layanan internet** (*Internet Service Provider*, **ISP**).

## 2. Perangkat jaringan

```
 [Laptop]──kabel──┐
 [Ponsel]~~Wi-Fi~~┤  [ ROUTER Wi-Fi RUMAH:      ]
 [Printer]─kabel──┘  [ switch + access point     ]──[Modem]──( Internet / ISP )
                     [ + router                  ]
 └──────────────────── LAN ──────────────────────┘
```

*Deskripsi diagram dg-w03-01:* laptop dan printer tersambung dengan kabel,
ponsel dengan Wi-Fi, ke satu kotak "router Wi-Fi rumah" yang berisi
switch, access point, dan router. Kotak itu tersambung ke modem, lalu ke
internet. Perangkat dan router berada di dalam LAN.

| Perangkat | Peran utama | Analogi |
|---|---|---|
| **Switch** | Menghubungkan banyak perangkat **di dalam satu LAN** lewat kabel dan meneruskan data ke perangkat tujuan di LAN itu | Meja resepsionis yang meneruskan surat ke ruangan di gedung yang sama |
| **Access point** (AP) | Memancarkan **Wi-Fi** agar perangkat nirkabel bergabung ke LAN | Pintu masuk tanpa kabel ke gedung |
| **Router** | Menghubungkan **jaringan yang berbeda** (mis. LAN rumah dengan internet) dan memilih jalur paket antarjaringan | Kantor pos yang mengirim surat ke kota lain |
| **Modem** | Mengubah sinyal agar cocok dengan saluran ISP (kabel tembaga, kabel TV, seluler). Pada internet **serat optik**, perannya dijalankan perangkat bernama **ONT/ONU** yang mengubah sinyal cahaya menjadi sinyal listrik; orang sering tetap menyebutnya "modem" | Penerjemah antara rumah dan jalur ISP |

Di rumah, satu kotak "router Wi-Fi" sering berisi **router + switch +
access point** sekaligus, kadang juga modem/ONT. Fungsinya tetap dapat
dibedakan walaupun bendanya satu. Karena itu soal W3 menanyakan
**fungsi** (mis. "fungsi yang memancarkan Wi-Fi" = access point), bukan
nama kotak yang dibeli di toko.

*Model sederhana W3:* peran di atas adalah peran utama untuk belajar.
Perangkat nyata dapat menjalankan peran tambahan (mis. switch tertentu juga
dapat meneruskan paket antarjaringan).

## 3. Klien dan server

| | Klien (*client*) | Server |
|---|---|---|
| Peran | **Meminta** layanan atau data | **Menyediakan** layanan atau data |
| Contoh | Browser di ponselmu | Komputer yang menyimpan halaman situs sekolah |

Satu perangkat dapat menjadi klien untuk satu layanan dan server untuk
layanan lain. Contoh: laptop yang membagikan folder ke anggota keluarga
menjadi server berkas untuk mereka, sekaligus klien saat membuka situs.

## 4. Contoh terbimbing

**Soal:** Di kelas, ada 20 komputer yang tersambung kabel ke satu kotak
dengan banyak port. Kotak itu juga tersambung ke perangkat yang menuju
internet sekolah. Guru membuka situs ujian yang disimpan di komputer
pusat sekolah. Tentukan perannya.

| Hal | Pertanyaan bantu | Jawaban |
|---|---|---|
| Kotak dengan banyak port di kelas | Menghubungkan perangkat **di dalam** satu LAN? | Switch |
| Perangkat yang menuju internet sekolah | Menghubungkan **jaringan berbeda**? | Router |
| Komputer pusat yang menyimpan situs ujian | **Menyediakan** layanan? | Server |
| Komputer guru yang membuka situs | **Meminta** layanan? | Klien |
| Jaringan di dalam sekolah | Satu lokasi? | LAN |

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Wi-Fi sama dengan internet." | Wi-Fi adalah cara bergabung ke LAN tanpa kabel. LAN dapat tetap berjalan (mis. mencetak ke printer) walaupun sambungan internet putus |
| "Router dan switch sama saja." | Switch menghubungkan perangkat di satu LAN; router menghubungkan jaringan yang berbeda |
| "Server pasti komputer raksasa." | Server adalah peran; laptop biasa pun dapat menjadi server |
| "Internet dimiliki satu perusahaan." | Internet terdiri dari banyak jaringan milik banyak pihak |

## 6. Latihan terbimbing (`mod-w03.prac-01`, tidak dinilai)

1. LAN atau WAN: (a) jaringan di satu laboratorium komputer,
   (b) jaringan yang menghubungkan kantor pusat di Jakarta dengan cabang
   di Makassar.
2. Perangkat apa: (a) membuat tablet dapat bergabung ke jaringan rumah
   tanpa kabel, (b) menghubungkan jaringan kantor dengan internet.
3. Saat kamu memutar video dari layanan streaming, mana klien dan mana
   server?

## 7. Cek pemahaman (tidak dinilai)

- Mengapa printer rumah masih dapat dipakai saat internet putus?
- Apa beda peran switch dan router?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) LAN, (b) WAN.
2. (a) access point, (b) router.
3. Ponselmu (aplikasi streaming) klien; komputer penyedia video server.

## Ringkasan

- **Jaringan** = perangkat yang terhubung untuk bertukar data; **LAN**
  satu lokasi, **WAN** wilayah luas, **internet** = jaringan dari
  jaringan-jaringan.
- **Switch** (di dalam LAN), **access point** (Wi-Fi ke LAN), **router**
  (antarjaringan), **modem** (ke saluran ISP).
- **Klien** meminta, **server** menyediakan.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Jaringan komputer | computer network | Perangkat yang terhubung untuk bertukar data |
| Jaringan area lokal | LAN (Local Area Network) | Jaringan di satu lokasi |
| Jaringan area luas | WAN (Wide Area Network) | Jaringan yang mencakup wilayah luas |
| Penyedia layanan internet | ISP | Perusahaan yang menyambungkan pelanggan ke internet |
| Router | router | Penghubung antarjaringan |
| Switch | switch | Penghubung perangkat di dalam satu LAN |
| Titik akses | access point | Pemancar Wi-Fi untuk bergabung ke LAN |
| Modem | modem | Pengubah sinyal ke saluran ISP |
| Klien | client | Pihak yang meminta layanan |
| Server | server | Pihak yang menyediakan layanan |
