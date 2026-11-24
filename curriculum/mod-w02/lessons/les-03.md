---
lesson_id: mod-w02.les-03
practice_id: mod-w02.prac-03
module_id: mod-w02
content_version: "1.0"
title: "File, Folder, Ekstensi, dan Path"
language: id
duration_minutes: 55        # materi 40 + latihan terbimbing 15
competencies: [comp-w02-fs-01, comp-w02-path-01]
prerequisites: [mod-w02.les-01]
accessibility:
  diagrams:
    - id: dg-w02-03
      alt: "Pohon folder milik Sari dengan root di puncak."
      long_description: >
        Root (garis miring) berada di puncak. Di bawahnya folder home, lalu
        folder sari. Folder sari berisi tiga folder: Musik, Sekolah, dan
        Foto. Musik berisi berkas lagu-pagi.mp3. Sekolah berisi berkas
        catatan.txt dan folder Tugas; Tugas berisi esai.docx. Foto berisi
        pantai.jpg.
  tables_with_core_data: ["Tabel ekstensi umum", "Tabel path absolut dan relatif", "Tabel model path W2 vs Windows"]
  english_terms: [file, folder, directory, file name, extension, root, parent folder, subfolder, path, absolute path, relative path, working directory, case-sensitive]
---

# Pelajaran 3 — File, Folder, Ekstensi, dan Path

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan **file** (berkas), **folder** (direktori), **nama
   berkas**, dan **ekstensi**.
2. Membaca **pohon folder**: root, folder induk, dan subfolder.
3. Menulis dan membaca **path absolut** dan **path relatif**, termasuk
   `.` dan `..`.

## Mengapa ini penting?

Setiap kali kamu mencari berkas, mengunggah tugas, atau nanti menulis
program (W9–W12) dan memakai Git (W15), kamu harus menunjuk berkas dengan
tepat. Path adalah "alamat" berkas: satu huruf salah, berkasnya tidak
ditemukan.

## 1. File dan ekstensi

**File** (berkas) adalah kumpulan data yang diberi nama dan disimpan di
penyimpanan (W1). Nama berkas biasanya terdiri dari **nama dasar** dan
**ekstensi** yang dipisahkan titik terakhir:

```
laporan-akhir.pdf
└─ nama dasar ─┘└ ekstensi
```

*Deskripsi:* pada `laporan-akhir.pdf`, nama dasar adalah `laporan-akhir`
dan ekstensinya `pdf` (bagian setelah titik terakhir).

| Ekstensi | Jenis isi | Contoh aplikasi pembuka |
|---|---|---|
| `.txt` | Teks polos | Editor teks |
| `.docx`, `.pdf` | Dokumen | Pengolah kata, pembaca PDF |
| `.xlsx`, `.csv` | Tabel/data | Lembar kerja |
| `.jpg`, `.png` | Gambar | Galeri, penampil gambar |
| `.mp3` | Audio | Pemutar musik |
| `.mp4` | Video | Pemutar video |
| `.zip` | Arsip terkompresi (beberapa berkas digabung dan diperkecil) | Pengelola arsip |
| `.exe` (Windows), `.apk` (Android) | Program/pemasang aplikasi | Dijalankan atau dipasang oleh OS |

Hal penting tentang ekstensi:

- Bedakan tiga hal: **isi** berkas (data sebenarnya), **ekstensi** (label
  di nama), dan **pengaitan aplikasi** (pengaturan OS yang menentukan
  aplikasi pembuka untuk tiap ekstensi). Ekstensi **tidak** mengubah isi:
  mengganti `foto.jpg` menjadi `foto.txt` tidak mengubah gambar menjadi
  teks; OS hanya memilih aplikasi lain untuk membukanya.
- Ekstensi menunjukkan jenis isi yang **diharapkan**, bukan bukti isi
  sebenarnya: berkas bernama `.pdf` bisa saja rusak atau berisi data lain.
- Pengaitan aplikasi dapat berbeda di tiap perangkat. Mengembalikan
  ekstensi yang benar tidak menjamin berkas terbuka bila aplikasi yang
  sesuai tidak terpasang.
- Sebagian OS **menyembunyikan ekstensi** secara bawaan. Berkas
  `hadiah.jpg.exe` dapat tampil sebagai `hadiah.jpg`, padahal sebenarnya
  program. Kita bahas bahayanya di W4.
- Ekstensi dihitung dari **titik terakhir**: `arsip.tugas.zip` berekstensi
  `zip`.

## 2. Folder dan pohon folder

**Folder** (direktori) adalah wadah yang dapat berisi berkas dan folder
lain (**subfolder**). Folder yang berisi folder lain disebut **folder
induk** (*parent*). Folder paling atas disebut **root**.

```
/                           ← root
└── home
    └── sari
        ├── Musik
        │   └── lagu-pagi.mp3
        ├── Sekolah
        │   ├── catatan.txt
        │   └── Tugas
        │       └── esai.docx
        └── Foto
            └── pantai.jpg
```

*Deskripsi diagram dg-w02-03:* root di puncak; `home` → `sari`; `sari`
berisi folder `Musik` (berisi `lagu-pagi.mp3`), `Sekolah` (berisi
`catatan.txt` dan folder `Tugas` yang berisi `esai.docx`), dan `Foto`
(berisi `pantai.jpg`).

Dalam satu folder, **nama harus unik**: tidak boleh ada dua berkas atau
folder bernama sama persis di folder yang sama. Berkas bernama sama boleh
ada di folder yang **berbeda**.

## 3. Model path W2

Pelajaran ini memakai **model path W2**, yang mengikuti gaya Linux dan
Android:

| Aturan model W2 | Contoh |
|---|---|
| Pemisah folder adalah garis miring `/` | `/home/sari/Foto` |
| Root ditulis `/` | `/` |
| Huruf besar dan kecil **dibedakan** (*case-sensitive*) | `Foto` ≠ `foto` |
| Path ke folder **tidak** diakhiri `/` (kecuali root) | `/home/sari/Foto`, bukan `/home/sari/Foto/` |
| Nama boleh memuat huruf, angka, tanda hubung `-`, dan titik; tanpa spasi | `lagu-pagi.mp3` |

*Perbandingan dengan sistem lain:* Windows memakai huruf drive dan garis
miring terbalik, mis. `C:\Users\Sari\Foto\pantai.jpg`. macOS memakai `/`
seperti model W2. Pada pengaturan bawaannya, Windows dan macOS umumnya
**tidak** membedakan huruf besar/kecil nama berkas. Soal dan lab W2 selalu
memakai model W2.

## 4. Path absolut

**Path absolut** menunjuk lokasi **mulai dari root**, jadi selalu diawali
`/`. Path absolut sama dari mana pun kamu melihatnya.

Cara menyusunnya: telusuri pohon dari root ke sasaran, tulis setiap nama
folder dipisah `/`, lalu nama berkas.

| Sasaran | Path absolut |
|---|---|
| Folder Musik | `/home/sari/Musik` |
| Berkas esai | `/home/sari/Sekolah/Tugas/esai.docx` |

## 5. Path relatif, `.` dan `..`

**Path relatif** menunjuk lokasi **mulai dari folder kerja saat ini**
(*working directory*), jadi **tidak** diawali `/`.

| Simbol | Arti |
|---|---|
| `.` | Folder saat ini |
| `..` | Folder induk (naik satu tingkat) |

Cara menyusunnya: dari folder kerja, **naik** dengan `..` sampai mencapai
folder yang juga menjadi "leluhur" sasaran, lalu **turun** ke sasaran.
Tulis jalur **terpendek** (tanpa naik-turun yang tidak perlu).

| Folder kerja | Sasaran | Path relatif | Penjelasan |
|---|---|---|---|
| `/home/sari/Sekolah` | `esai.docx` | `Tugas/esai.docx` | Turun ke Tugas |
| `/home/sari/Sekolah/Tugas` | `catatan.txt` | `../catatan.txt` | Naik ke Sekolah |
| `/home/sari/Musik` | `pantai.jpg` | `../Foto/pantai.jpg` | Naik ke sari, turun ke Foto |

`./Tugas/esai.docx` sama artinya dengan `Tugas/esai.docx` (`.` = folder
saat ini).

## 6. Contoh terbimbing

**Soal:** Folder kerja `/home/sari/Sekolah/Tugas`. Tulis path relatif ke
`lagu-pagi.mp3`.

| Langkah | Posisi | Ditulis |
|---|---|---|
| Naik dari Tugas ke Sekolah | `/home/sari/Sekolah` | `..` |
| Naik dari Sekolah ke sari | `/home/sari` | `../..` |
| Turun ke Musik | `/home/sari/Musik` | `../../Musik` |
| Tunjuk berkas | — | `../../Musik/lagu-pagi.mp3` |

Periksa: path absolutnya `/home/sari/Musik/lagu-pagi.mp3`; dari Tugas
memang perlu naik dua tingkat sampai `sari`.

## 7. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Ekstensi menentukan isi berkas." | Ekstensi hanya label: menunjukkan jenis yang diharapkan dan dipakai OS untuk memilih aplikasi; isi tidak berubah saat ekstensi diganti |
| "Path relatif selalu dimulai dari root." | Path relatif dimulai dari folder kerja; yang dimulai dari root adalah path absolut |
| "`..` berarti kembali ke root." | `..` hanya naik **satu** tingkat |
| "`Foto` dan `foto` sama." | Di model W2 (dan Linux/Android) keduanya berbeda |
| "Dua berkas bernama sama tidak boleh ada di komputer." | Boleh, asalkan di folder yang berbeda |

## 8. Latihan terbimbing (`mod-w02.prac-03`, tidak dinilai)

Gunakan pohon folder milik Sari (§2).

1. Apa ekstensi `catatan.txt` dan `arsip.lama.zip`?
2. Tulis path absolut berkas `pantai.jpg`.
3. Folder kerja `/home/sari`. Tulis path relatif ke `catatan.txt`.
4. Folder kerja `/home/sari/Foto`. Tulis path relatif ke folder `Sekolah`.

## 9. Cek pemahaman (tidak dinilai)

- Mengapa path absolut selalu sama dari folder kerja mana pun?
- Apa beda `../catatan.txt` dan `catatan.txt` bila folder kerjanya
  `/home/sari/Sekolah/Tugas`?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. `txt` dan `zip` (titik terakhir).
2. `/home/sari/Foto/pantai.jpg`.
3. `Sekolah/catatan.txt`.
4. `../Sekolah`.

## Ringkasan

- **Berkas** = data bernama; **ekstensi** = bagian setelah titik
  terakhir, petunjuk jenis dan aplikasi pembuka.
- **Folder** membentuk **pohon** dengan **root** di puncak; nama unik di
  dalam satu folder.
- **Path absolut** dimulai `/` dari root; **path relatif** dimulai dari
  folder kerja; `..` naik satu tingkat, `.` folder saat ini.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Berkas | file | Kumpulan data bernama di penyimpanan |
| Folder / direktori | folder / directory | Wadah berkas dan folder lain |
| Ekstensi | extension | Bagian nama setelah titik terakhir |
| Root | root | Folder paling atas dalam pohon |
| Folder induk | parent folder | Folder yang berisi folder lain |
| Subfolder | subfolder | Folder di dalam folder lain |
| Path absolut | absolute path | Alamat dari root |
| Path relatif | relative path | Alamat dari folder kerja |
| Folder kerja | working directory | Folder tempat kamu "berada" saat ini |
| Peka huruf besar/kecil | case-sensitive | `A` dan `a` dianggap berbeda |
