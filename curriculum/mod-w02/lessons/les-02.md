---
lesson_id: mod-w02.les-02
practice_id: mod-w02.prac-02
module_id: mod-w02
content_version: "1.0"
title: "Program, Proses, dan Multitasking"
language: id
duration_minutes: 40        # materi 30 + latihan terbimbing 10
competencies: [comp-w02-proc-01]
prerequisites: [mod-w02.les-01]
accessibility:
  diagrams:
    - id: dg-w02-02
      alt: "Diagram program di penyimpanan dimuat ke RAM menjadi proses."
      long_description: >
        Di kiri ada kotak Penyimpanan berisi berkas program. Panah berlabel
        "dibuka" menuju kotak RAM di tengah, berisi dua proses dengan nomor
        PID. Di kanan ada kotak CPU. Panah bolak-balik antara RAM dan CPU
        berlabel "OS membagi giliran".
  tables_with_core_data: ["Tabel program vs proses", "Tabel contoh manajer tugas"]
  english_terms: [program, process, process ID (PID), multitasking, task manager, not responding, end task]
---

# Pelajaran 2 — Program, Proses, dan Multitasking

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Membedakan **program** dan **proses**.
2. Menjelaskan bagaimana sistem operasi menjalankan banyak proses
   (**multitasking**).
3. Membaca tabel **manajer tugas** (*task manager*) dan memilih tindakan
   yang tepat untuk aplikasi yang macet, beserta akibatnya.

## Mengapa ini penting?

Saat ponsel terasa lambat atau sebuah aplikasi "tidak menanggapi",
jawabannya hampir selalu ada di daftar proses. Dengan memahami proses, kamu
dapat menutup yang bermasalah tanpa kehilangan pekerjaan yang lain.

## 1. Program vs proses

```
[ PENYIMPANAN ]          [ RAM ]                 [ CPU ]
 berkas program  ─dibuka─►  proses (PID 812)  ◄──►  menjalankan
                           proses (PID 815)        instruksi
                                ▲   OS membagi giliran   │
                                └────────────────────────┘
```

*Deskripsi diagram dg-w02-02:* berkas program tersimpan di penyimpanan.
Saat dibuka, sistem operasi memuatnya ke RAM sebagai proses yang diberi
nomor (PID). CPU menjalankan instruksi proses-proses itu secara bergiliran.

| | Program | Proses |
|---|---|---|
| Arti | Berkas berisi instruksi, tersimpan di penyimpanan | Program **yang sedang berjalan** |
| Tempat | SSD/HDD (non-volatil, W1) | RAM (volatil, W1) + giliran di CPU |
| Kapan ada | Selama berkasnya tidak dihapus | Sejak dibuka sampai ditutup/diakhiri |
| Identitas | Nama berkas | Nomor proses (**PID**, *process ID*) yang diberikan OS |

Satu program dapat menjadi **beberapa proses** sekaligus. Browser modern,
misalnya, sering membuat proses terpisah untuk beberapa tab agar satu tab
yang bermasalah tidak menjatuhkan semuanya.

**Analogi:** program seperti **resep di buku masak**; proses seperti
**kegiatan memasak resep itu** di dapur sekarang. Resep yang sama dapat
dimasak dua kali bersamaan di dua kompor.

## 2. Multitasking

Komputer tampak menjalankan banyak program sekaligus. Caranya:

- Sistem operasi **membagi waktu CPU** menjadi potongan yang sangat
  singkat dan bergiliran memberikannya ke setiap proses. Pergantiannya
  begitu cepat sehingga semuanya terlihat berjalan bersamaan.
- Pada CPU **banyak core** (W1), beberapa proses benar-benar dapat
  berjalan bersamaan, satu di setiap core.
- Setiap proses mendapat **bagian RAM sendiri**. Sistem operasi menjaga
  agar satu proses tidak menimpa RAM proses lain.

*Model sederhana W2:* di sini kita hanya membedakan "berjalan" dan
"menunggu giliran", dan menganggap satu core menjalankan satu proses pada
satu waktu. Sistem operasi nyata memakai lebih banyak keadaan proses dan
aturan penjadwalan yang rumit, dan sebagian CPU punya teknologi seperti
*hyper-threading* (SMT) yang membuat satu core fisik dapat mengerjakan dua
alur instruksi sekaligus.

## 3. Manajer tugas

**Manajer tugas** (*Task Manager* di Windows, *Activity Monitor* di macOS,
*System Monitor* di Linux) menampilkan proses yang berjalan. Contoh
(angka fiktif):

| Nama proses | PID | CPU | Memori (RAM) | Status |
|---|---|---|---|---|
| Kalkulator | 2210 | 0% | 25 MB | Berjalan |
| Pengolah kata | 2234 | 1% | 310 MB | Berjalan |
| Pemutar musik | 2251 | 2% | 120 MB | Berjalan |
| Editor foto | 2288 | 0% | 1.400 MB | **Tidak menanggapi** |

*Deskripsi tabel:* empat proses dengan PID, persentase pemakaian CPU,
pemakaian RAM dalam MB (desimal, W1), dan status. Hanya editor foto
berstatus "Tidak menanggapi".

**Mengakhiri tugas** (*end task*) menghentikan proses secara paksa:

- RAM milik proses itu dikembalikan ke sistem operasi.
- Pekerjaan yang **belum disimpan** di proses itu hilang (isinya hanya di
  RAM — W1).
- Proses lain **tidak** ikut berhenti.

Langkah yang aman saat aplikasi macet: tunggu sebentar → simpan pekerjaan
di aplikasi **lain** yang masih berjalan → baru akhiri proses yang macet.

## 4. Contoh terbimbing

**Soal (memakai tabel §3):** Kamu sedang menulis di pengolah kata dan
belum menyimpan. Editor foto macet. Proses mana yang diakhiri, dan apa
akibatnya bagi tulisanmu?

| Langkah berpikir | Jawaban |
|---|---|
| Proses mana yang bermasalah? | Editor foto (status "Tidak menanggapi") |
| Apakah tulisan ada di proses yang sama? | Tidak, tulisan ada di proses pengolah kata (PID 2234) |
| Apa yang dilakukan dulu? | Simpan tulisan di pengolah kata |
| Apa akibat mengakhiri editor foto? | Editor foto berhenti; perubahan foto yang belum disimpan hilang; pengolah kata tetap berjalan |

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Menutup jendela sama dengan menghapus program." | Program (berkas) tetap ada di penyimpanan; yang berhenti hanya prosesnya |
| "Mengakhiri satu proses mematikan semua aplikasi." | Proses lain tetap berjalan |
| "Proses yang diakhiri menyimpan pekerjaan otomatis." | Yang belum disimpan hilang, kecuali aplikasi punya simpan otomatis |
| "Multitasking berarti CPU satu core mengerjakan semuanya pada detik yang sama persis." | Satu core bergiliran sangat cepat; banyak core baru benar-benar bersamaan |

## 6. Latihan terbimbing (`mod-w02.prac-02`, tidak dinilai)

1. Tulis **program** atau **proses**: (a) berkas pemasang aplikasi yang
   baru diunduh dan belum dibuka, (b) aplikasi peta yang sedang menunjukkan
   arah, (c) dua jendela aplikasi catatan yang terbuka bersamaan.
2. Memakai tabel §3: proses mana yang memakai RAM paling sedikit?
3. Apa yang terjadi pada RAM setelah sebuah proses diakhiri?

## 7. Cek pemahaman (tidak dinilai)

- Mengapa pekerjaan yang belum disimpan hilang saat prosesnya diakhiri?
- Mengapa musik dapat terus berputar saat kamu mengetik pesan?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) program, (b) proses, (c) dua proses dari satu program.
2. Kalkulator (25 MB).
3. RAM milik proses itu dikembalikan ke sistem operasi dan dapat dipakai
   proses lain.

## Ringkasan

- **Program** = berkas instruksi di penyimpanan; **proses** = program
  yang sedang berjalan di RAM, punya **PID**.
- **Multitasking**: OS bergiliran memberi waktu CPU; banyak core
  menjalankan beberapa proses benar-benar bersamaan.
- **Mengakhiri tugas** menghentikan satu proses, mengembalikan RAM-nya,
  dan menghilangkan pekerjaan yang belum disimpan di proses itu saja.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Program | program | Berkas berisi instruksi |
| Proses | process | Program yang sedang berjalan |
| Nomor proses | process ID (PID) | Nomor unik yang diberikan OS untuk setiap proses |
| Multitugas | multitasking | Menjalankan beberapa proses dalam waktu yang sama |
| Manajer tugas | task manager | Alat untuk melihat dan mengakhiri proses |
| Tidak menanggapi | not responding | Proses tidak memproses perintah pengguna |
| Akhiri tugas | end task | Menghentikan proses secara paksa |
