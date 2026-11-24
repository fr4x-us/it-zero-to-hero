---
lesson_id: mod-w02.les-01
practice_id: mod-w02.prac-01
module_id: mod-w02
content_version: "1.0"
title: "Sistem Operasi: Pengelola Komputer"
language: id
duration_minutes: 40        # materi 30 + latihan terbimbing 10
competencies: [comp-w02-os-01]
prerequisites: [mod-w01]
accessibility:
  diagrams:
    - id: dg-w02-01
      alt: "Diagram lapisan: pengguna, aplikasi, sistem operasi, hardware."
      long_description: >
        Empat kotak bertumpuk dari atas ke bawah: Pengguna, Aplikasi,
        Sistem operasi, Hardware. Di samping kotak Sistem operasi tertulis
        lima tugasnya: mengelola proses, memori, file, perangkat, dan
        menyediakan antarmuka pengguna. Panah dari Aplikasi ke Hardware
        selalu melewati Sistem operasi.
  tables_with_core_data: ["Tabel lima fungsi sistem operasi", "Tabel contoh sistem operasi"]
  english_terms: [operating system, kernel, user interface, GUI, CLI, driver, multitasking]
---

# Pelajaran 1 — Sistem Operasi: Pengelola Komputer

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan apa itu **sistem operasi** (*operating system*, OS) dan
   menyebut contohnya.
2. Menjelaskan lima fungsi utama sistem operasi.
3. Membedakan sistem operasi dari **aplikasi**, dan menentukan fungsi OS
   yang bekerja pada sebuah kejadian sehari-hari.

## Mengapa ini penting?

Di W1 kamu belajar bahwa sistem operasi termasuk **software sistem**. Di
W2 kita melihat lebih dekat **apa yang dikerjakannya**. Hampir semua
masalah sehari-hari — aplikasi macet, berkas "hilang", izin kamera ditolak
— adalah urusan sistem operasi. Memahami perannya membuatmu tahu harus
mencari jawaban di mana.

## 1. Apa itu sistem operasi?

**Sistem operasi** adalah software sistem yang **mengelola hardware** dan
**menyediakan layanan untuk aplikasi**, sehingga aplikasi tidak perlu
mengatur hardware sendiri.

**Analogi:** bayangkan sebuah gedung perkantoran. Hardware adalah
gedungnya (ruangan, lift, listrik). Aplikasi adalah perusahaan yang menyewa
ruangan. Sistem operasi adalah **pengelola gedung**: membagi ruangan,
mengatur jadwal lift, memberi kunci kepada penghuni yang berhak, dan
menjaga agar penyewa tidak saling mengganggu.

| Perangkat | Contoh sistem operasi |
|---|---|
| Komputer meja/laptop | Windows, macOS, Linux (mis. Ubuntu) |
| Ponsel/tablet | Android, iOS/iPadOS |
| Lainnya | Sistem operasi di TV pintar, jam pintar, mesin ATM |

Bagian inti sistem operasi yang paling dekat dengan hardware disebut
**kernel**. Android, misalnya, dibangun di atas kernel Linux.

## 2. Lima fungsi utama sistem operasi

```
        [ PENGGUNA ]
             │
        [ APLIKASI ]
             │
   [ SISTEM OPERASI ]  ── proses · memori · file · perangkat · antarmuka
             │
        [ HARDWARE ]
```

*Deskripsi diagram dg-w02-01:* pengguna memakai aplikasi; aplikasi
meminta layanan sistem operasi; sistem operasi yang mengatur hardware.
Lima fungsinya tertulis di samping kotak sistem operasi.

| Fungsi | Artinya | Contoh yang kamu lihat |
|---|---|---|
| **Manajemen proses** | Menjalankan program dan membagi waktu CPU di antara program yang berjalan | Musik tetap berputar saat kamu membuka aplikasi pesan |
| **Manajemen memori** | Membagi RAM untuk setiap program dan mengambilnya kembali saat program ditutup | RAM yang terpakai turun setelah aplikasi besar ditutup |
| **Manajemen file** | Menyimpan, menamai, dan menata berkas dan folder di penyimpanan | Kamu dapat membuat folder dan memindahkan foto |
| **Manajemen perangkat** | Mengatur hardware lewat **driver** (W1) | Flashdisk yang dicolokkan dikenali dan muncul di layar |
| **Antarmuka pengguna** | Cara pengguna memberi perintah: **GUI** (ikon, jendela, sentuhan) atau **CLI** (mengetik perintah teks) | Layar utama ponsel; jendela "Terminal" atau "Command Prompt" |

Sistem operasi modern juga mengatur **keamanan**: akun pengguna, kata
sandi, dan izin akses. Topik izin dibahas di Pelajaran 4; keamanan
lebih luas dibahas di W4.

*Model sederhana W2:* lima fungsi ini adalah cara mengelompokkan tugas OS
untuk belajar. Buku lain dapat membaginya sedikit berbeda (mis. memisahkan
"keamanan" atau "jaringan" sebagai fungsi tersendiri).

## 3. Sistem operasi vs aplikasi vs firmware

| | Sistem operasi | Aplikasi | Firmware (W1) |
|---|---|---|---|
| Tujuan | Mengelola hardware dan melayani aplikasi | Membantu pengguna menyelesaikan tugas tertentu | Menjalankan perangkat sebelum OS aktif, atau mengendalikan perangkat sederhana |
| Contoh | Android, Windows | Peta, pengolah kata, game | BIOS/UEFI di motherboard |
| Bila tidak ada | Aplikasi tidak dapat berjalan | Komputer tetap menyala, tetapi tugas itu tidak dapat dikerjakan | Komputer tidak dapat memulai OS |

Aplikasi **meminta** sistem operasi untuk menyimpan berkas, memakai
kamera, atau menampilkan jendela. Aplikasi tidak mengatur hardware secara
langsung.

## 4. Contoh terbimbing

**Soal:** Kamu mencolokkan flashdisk, membuka aplikasi pengelola berkas,
lalu menyalin satu foto ke flashdisk. Fungsi OS mana yang bekerja pada
setiap langkah?

| Langkah | Pertanyaan bantu | Fungsi OS |
|---|---|---|
| Flashdisk dikenali | Apakah OS mengatur sebuah **perangkat**? | Manajemen perangkat |
| Aplikasi pengelola berkas dibuka dan mendapat jatah RAM | Apakah OS **menjalankan program** dan **membagi RAM**? | Manajemen proses dan manajemen memori |
| Ikon foto dan folder tampil di layar untuk diklik | Apakah ini **cara pengguna memberi perintah**? | Antarmuka pengguna |
| Foto ditulis ke flashdisk dengan nama yang sama | Apakah OS **menyimpan dan menamai berkas**? | Manajemen file |

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Sistem operasi itu sama dengan aplikasi yang sudah terpasang dari pabrik." | Aplikasi bawaan (kalkulator, kamera) tetap aplikasi. OS adalah pengelola di bawahnya |
| "Aplikasi langsung mengatur kamera atau printer." | Aplikasi meminta OS; OS memakai driver untuk mengatur perangkat |
| "Antarmuka OS harus berupa ikon dan jendela." | CLI (mengetik perintah teks) juga antarmuka pengguna |
| "Satu perangkat hanya dapat memakai satu OS selamanya." | OS dapat diperbarui atau diganti; firmware tetap ada di chip perangkat |

## 6. Latihan terbimbing (`mod-w02.prac-01`, tidak dinilai)

1. Tulis **OS** atau **aplikasi**: (a) iOS, (b) aplikasi kamus,
   (c) Ubuntu, (d) aplikasi pemutar video.
2. Fungsi OS mana yang paling terlihat? (a) Setelah kamu memasang
   *mouse* baru, kursornya langsung bergerak. (b) Kamu menekan ikon untuk
   membuka aplikasi. (c) Kamu mengganti nama folder "Baru" menjadi
   "Resep".
3. Sebutkan satu perbedaan GUI dan CLI.

## 7. Cek pemahaman (tidak dinilai)

- Mengapa aplikasi tidak perlu tahu cara kerja setiap jenis printer?
- Apa yang terjadi bila komputer punya hardware dan aplikasi, tetapi
  tidak punya sistem operasi?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) OS, (b) aplikasi, (c) OS, (d) aplikasi.
2. (a) manajemen perangkat (driver *mouse*), (b) antarmuka pengguna
   (lalu manajemen proses saat aplikasi dijalankan), (c) manajemen file.
3. GUI memakai ikon/jendela/sentuhan; CLI memakai perintah teks yang
   diketik.

## Ringkasan

- **Sistem operasi** mengelola hardware dan melayani aplikasi; intinya
  disebut **kernel**.
- Lima fungsi utama (model W2): **proses, memori, file, perangkat,
  antarmuka pengguna**; ditambah keamanan akun.
- Aplikasi meminta layanan OS; OS memakai driver untuk mengatur
  perangkat.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Sistem operasi | operating system (OS) | Software sistem yang mengelola hardware dan melayani aplikasi |
| Kernel | kernel | Inti sistem operasi yang paling dekat dengan hardware |
| Antarmuka pengguna grafis | graphical user interface (GUI) | Antarmuka berupa ikon, jendela, dan sentuhan |
| Antarmuka baris perintah | command-line interface (CLI) | Antarmuka dengan mengetik perintah teks |
| Driver | driver | Software yang menghubungkan OS dengan satu perangkat (W1) |
| Multitugas | multitasking | Menjalankan beberapa program dalam waktu yang sama (Pelajaran 2) |
