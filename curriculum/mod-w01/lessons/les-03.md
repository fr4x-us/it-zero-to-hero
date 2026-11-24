---
lesson_id: mod-w01.les-03
practice_id: mod-w01.prac-03
module_id: mod-w01
content_version: "1.0"
title: "Software: Sistem Operasi, Firmware, Driver, Aplikasi, dan Proses Boot"
language: id
duration_minutes: 40        # materi 30 + latihan terbimbing 10
competencies: [comp-w01-sw-01]
prerequisites: [mod-w01.les-01, mod-w01.les-02]
accessibility:
  diagrams:
    - id: dg-w01-03
      alt: "Diagram lapisan dari pengguna sampai hardware."
      long_description: >
        Lima lapisan bertumpuk dari atas ke bawah: Pengguna, Aplikasi,
        Sistem operasi, Driver, Hardware. Panah ke bawah menunjukkan
        permintaan mengalir dari pengguna ke hardware; panah ke atas
        menunjukkan hasil kembali ke pengguna.
    - id: dg-w01-04
      alt: "Diagram urutan proses boot."
      long_description: >
        Lima kotak berurutan dari kiri ke kanan: Tombol daya ditekan,
        Firmware menjalankan POST, Firmware mencari perangkat boot,
        Bootloader memuat sistem operasi, Sistem operasi siap dipakai.
  english_terms: [system software, application software, operating system, firmware, BIOS, UEFI, driver, utility, boot, bootloader, POST]
---

# Pelajaran 3 — Software

## Tujuan pelajaran

1. Membedakan **software sistem** dan **software aplikasi** dengan contoh.
2. Menjelaskan peran **sistem operasi**, **firmware**, **driver**, dan
   **utilitas**.
3. Menjelaskan lapisan **pengguna → aplikasi → sistem operasi → driver →
   hardware**.
4. Mengurutkan langkah utama **proses boot** (menyalakan komputer).

## Mengapa ini penting?

Ketika printer "tidak terdeteksi", aplikasi tidak dapat dipasang, atau
komputer gagal menyala, penyebabnya sering ada pada lapisan software yang
berbeda. Mengetahui lapisan membantu kamu mencari sumber masalah dengan
tepat.

## 1. Dua kelompok besar software

| | Software sistem | Software aplikasi |
|---|---|---|
| Tujuan | Menjalankan dan mengelola komputer | Membantu pengguna menyelesaikan tugas tertentu |
| Contoh | Sistem operasi, firmware, driver, utilitas (pembersih disk, antivirus) | Pengolah kata, lembar kerja, browser, aplikasi peta, game, pemutar musik |
| Tanpa ini | Komputer tidak dapat dipakai | Komputer tetap menyala, tetapi tugas tertentu tidak bisa dikerjakan |

### Sistem operasi (*operating system*, OS)

Software sistem utama yang mengelola hardware (CPU, RAM, penyimpanan,
perangkat) dan menjalankan aplikasi. Contoh: Windows, macOS, Linux,
Android, iOS. Rincian cara kerja OS dan berkas dipelajari di **W2**.

### Firmware

Program dasar yang tersimpan di chip pada perangkat. Di komputer, firmware
pada motherboard disebut **BIOS** atau **UEFI**; ia bekerja pertama kali
saat komputer dinyalakan. Printer, router, dan SSD juga punya firmware.

### Driver

Software yang membantu sistem operasi **berkomunikasi dengan perangkat
keras tertentu**, misalnya driver printer atau driver kartu grafis.
**Driver bukan kabel atau alat fisik.**

### Utilitas (*utility*)

Software sistem untuk merawat komputer: pembersih disk, pencadangan,
antivirus. *(Pengelompokan umum di modul ini; sebagian buku menyebut
utilitas sebagai kelompok tersendiri di samping sistem operasi dan driver.)*

## 2. Lapisan dari pengguna sampai hardware

```
   Pengguna
      │  ▲
      ▼  │
   Aplikasi          (mis. pengolah kata)
      │  ▲
      ▼  │
   Sistem operasi    (mengatur CPU, RAM, berkas, perangkat)
      │  ▲
      ▼  │
   Driver            (penerjemah untuk perangkat tertentu)
      │  ▲
      ▼  │
   Hardware          (printer, layar, SSD, …)
```

*Deskripsi diagram dg-w01-03:* lihat metadata di atas.

**Analogi:** kamu (pengguna) memesan di restoran melalui **pelayan**
(aplikasi). Pelayan menyerahkan pesanan ke **kepala dapur** (sistem
operasi) yang membagi tugas. Untuk alat khusus seperti oven pizza, ada
**petunjuk alat** (driver) agar dapur tahu cara memakainya. **Oven** adalah
hardware.

### Contoh terbimbing: mencetak dokumen

| Urutan | Yang terjadi | Lapisan |
|---|---|---|
| 1 | Kamu menekan "Cetak" | Pengguna → aplikasi |
| 2 | Aplikasi meminta sistem operasi mencetak | Aplikasi → OS |
| 3 | Sistem operasi meneruskan data ke driver printer | OS → driver |
| 4 | Driver menerjemahkan data menjadi perintah yang dipahami printer | Driver |
| 5 | Printer mencetak di kertas | Hardware (output) |

Bila driver tidak terpasang, langkah 3–4 gagal dan printer tidak dapat
dipakai walaupun kabel tersambung dengan benar. Tetapi printer yang "tidak
terdeteksi" dapat punya **banyak penyebab** (printer mati, kabel/port
bermasalah, pengaturan, driver); driver adalah salah satu kemungkinan, bukan
diagnosis pasti.

*Diagram lapisan dan urutan boot di pelajaran ini adalah **model sederhana
W1**. Sistem nyata memiliki lebih banyak lapisan dan langkah, dan perilaku
firmware berbeda antarperangkat.*

## 3. Proses boot (menyalakan komputer)

```
[Tombol daya] → [Firmware: POST] → [Firmware: cari perangkat boot] → [Bootloader memuat OS] → [OS siap]
```

*Deskripsi diagram dg-w01-04:* lihat metadata di atas.

1. **Tombol daya ditekan** — PSU mengalirkan listrik.
2. **Firmware (BIOS/UEFI) menjalankan POST** (*Power-On Self-Test*):
   memeriksa hardware penting seperti RAM.
3. **Firmware mencari perangkat boot** (biasanya SSD/HDD).
4. **Bootloader** (program kecil di perangkat boot) **memuat sistem
   operasi** dari penyimpanan ke RAM.
5. **Sistem operasi siap dipakai** — layar masuk atau desktop muncul.

Mengapa OS harus dimuat ke RAM? Karena CPU bekerja dengan data di RAM
(Pelajaran 2), sedangkan OS tersimpan di penyimpanan non-volatil.

## 4. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Driver itu kabel penghubung." | Driver adalah software |
| "Browser adalah sistem operasi karena dipakai setiap hari." | Browser adalah software aplikasi |
| "Firmware sama dengan hardware karena ada di chip." | Firmware adalah software yang tersimpan di chip |
| "Komputer langsung menjalankan OS saat dinyalakan." | Firmware bekerja lebih dulu (POST, mencari perangkat boot), lalu bootloader memuat OS |

## 5. Latihan terbimbing (`mod-w01.prac-03`, tidak dinilai)

1. Kelompokkan: iOS, aplikasi kalender, driver kartu grafis, aplikasi
   presentasi, firmware router, aplikasi pencadangan (*backup*).
2. Printer baru sudah menyala dan tersambung dengan kabel USB yang benar,
   tetapi tidak muncul di daftar printer. Menurut model lapisan W1, lapisan
   software mana yang perlu diperiksa?
3. Urutkan lapisan saat kamu memutar video dan gambar tampil di layar:
   sistem operasi; layar; pengguna; driver grafis; aplikasi pemutar video.

## 6. Cek pemahaman (tidak dinilai)

- Mengapa aplikasi tidak langsung "berbicara" dengan printer?
- Apa yang terjadi pada langkah POST?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Software sistem: iOS (OS), driver kartu grafis, firmware router,
   aplikasi pencadangan (utilitas). Software aplikasi: kalender, presentasi.
2. Driver printer (software) — kemungkinan belum terpasang atau tidak
   sesuai. Penyebab lain tetap mungkin (port, pengaturan), jadi ini
   pemeriksaan pertama, bukan diagnosis pasti.
3. Pengguna → aplikasi pemutar video → sistem operasi → driver grafis →
   layar.

## Ringkasan

- **Software sistem** menjalankan komputer; **software aplikasi** membantu
  tugas pengguna.
- **OS** mengelola hardware dan aplikasi; **firmware** program dasar di chip;
  **driver** penerjemah untuk perangkat tertentu; **utilitas** merawat
  sistem.
- Permintaan mengalir **pengguna → aplikasi → OS → driver → hardware**.
- Boot: daya → POST → cari perangkat boot → bootloader memuat OS → OS siap.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Software sistem | system software | Software yang menjalankan dan mengelola komputer |
| Software aplikasi | application software | Software untuk tugas pengguna |
| Sistem operasi | operating system (OS) | Pengelola hardware dan aplikasi |
| Firmware | firmware | Program dasar yang tersimpan di chip perangkat |
| BIOS/UEFI | BIOS/UEFI | Firmware motherboard |
| Driver | driver | Software penghubung OS dengan perangkat tertentu |
| Utilitas | utility | Software perawatan sistem |
| Menyalakan sistem | boot | Proses dari daya menyala sampai OS siap |
| Pemuat boot | bootloader | Program yang memuat OS ke RAM |
| Uji mandiri saat menyala | POST | Pemeriksaan hardware oleh firmware |
