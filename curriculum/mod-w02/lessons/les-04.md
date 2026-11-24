---
lesson_id: mod-w02.les-04
practice_id: mod-w02.prac-04
module_id: mod-w02
content_version: "1.0"
title: "Operasi Berkas, Akun Pengguna, dan Izin Akses"
language: id
duration_minutes: 45        # materi 33 + latihan terbimbing 12
competencies: [comp-w02-ops-01, comp-w02-perm-01]
prerequisites: [mod-w02.les-03]
accessibility:
  diagrams:
    - id: dg-w02-04
      alt: "Perbandingan salin dan pindah pada dua folder."
      long_description: >
        Dua baris gambar. Baris pertama, Salin: folder A berisi berkas X;
        setelah operasi, folder A tetap berisi X dan folder B juga berisi X.
        Baris kedua, Pindah: folder A berisi X; setelah operasi, folder A
        kosong dan folder B berisi X.
  tables_with_core_data: ["Tabel operasi berkas model W2", "Tabel izin baca/tulis/jalankan", "Tabel izin aplikasi Android"]
  english_terms: [create, copy, move, rename, delete, trash / recycle bin, restore, user account, administrator, owner, permission, read, write, execute, least privilege]
---

# Pelajaran 4 — Operasi Berkas, Akun Pengguna, dan Izin Akses

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan dan memprediksi hasil operasi **buat, salin, pindah, ganti
   nama, hapus**, dan **pulihkan** pada pohon folder.
2. Menjelaskan **akun pengguna**, **pemilik berkas**, dan izin **baca,
   tulis, jalankan**.
3. Memilih izin yang paling kecil tetapi cukup (**prinsip hak minimum**),
   termasuk izin aplikasi di ponsel.

## Mengapa ini penting?

Salah memilih "salin" atau "pindah" dapat membuat berkas ganda atau
"hilang". Izin yang terlalu longgar membuat orang atau aplikasi lain dapat
mengubah atau membaca data pribadimu. Keduanya urusan sehari-hari dan
pondasi keamanan di W4.

## 1. Operasi berkas (model W2)

| Operasi | Hasil | Berkas asal |
|---|---|---|
| **Buat** | Berkas/folder baru muncul di folder yang dipilih | — |
| **Salin** (*copy*) | Salinan bernama sama muncul di folder tujuan | **Tetap ada** |
| **Pindah** (*move*) | Berkas muncul di folder tujuan | **Hilang** dari folder asal |
| **Ganti nama** (*rename*) | Nama berubah, folder tetap sama | Berganti nama |
| **Hapus** (*delete*) | Berkas masuk **Tempat Sampah** (*Trash/Recycle Bin*) | Hilang dari folder asal, masih dapat **dipulihkan** |
| **Pulihkan** (*restore*) | Berkas kembali ke folder asalnya | — |
| **Kosongkan Tempat Sampah** | Berkas di Tempat Sampah dihapus permanen | Tidak dapat dipulihkan lewat Tempat Sampah |

```
SALIN  : A[X]  ──►  A[X]   B[X]
PINDAH : A[X]  ──►  A[ ]   B[X]
```

*Deskripsi diagram dg-w02-04:* pada salin, X tetap di A dan muncul di B;
pada pindah, X hilang dari A dan muncul di B.

Aturan tambahan **model W2** (dipakai di semua soal dan lab W2):

| ID | Aturan |
|---|---|
| OP-1 | Menyalin atau memindahkan **folder** ikut membawa **seluruh isinya** |
| OP-2 | Bila di folder tujuan sudah ada nama yang sama persis, operasi **ditolak** dan tidak ada yang berubah |
| OP-3 | Operasi dijalankan **berurutan**; setiap operasi memakai keadaan hasil operasi sebelumnya |
| OP-4 | Berkas di Tempat Sampah tidak dihitung sebagai isi folder mana pun |

*Model sederhana vs kenyataan:* OS nyata biasanya **bertanya** saat ada
nama sama (ganti, lewati, atau simpan keduanya dengan nama baru). Berkas
yang dihapus dari flashdisk atau kartu memori sering **tidak** masuk
Tempat Sampah. Dan berkas yang sudah dihapus permanen kadang masih dapat
dipulihkan dengan alat khusus — jadi "hapus" tidak sama dengan "aman
dimusnahkan".

*Sebelum menghapus berkas asal setelah menyalin:* periksa salinannya —
jumlah dan nama berkas sama, dan setiap berkas **dapat dibuka** dengan
isi yang lengkap. Berkas yang tampak ada belum tentu terbaca utuh (mis.
penyalinan terputus atau flashdisk rusak).

## 2. Contoh terbimbing: menelusuri operasi

**Keadaan awal** (folder kerja tidak dipakai; semua path absolut):

```
/data
├── Masuk
│   ├── resep-kue.txt
│   └── denah.png
└── Arsip
```

**Operasi:**

1. Salin `/data/Masuk/denah.png` ke `/data/Arsip`.
2. Pindah `/data/Masuk/resep-kue.txt` ke `/data/Arsip`.
3. Ganti nama `/data/Arsip/denah.png` menjadi `denah-lama.png`.
4. Hapus `/data/Masuk/denah.png`.

| Setelah langkah | Isi `/data/Masuk` | Isi `/data/Arsip` | Tempat Sampah |
|---|---|---|---|
| 1 | `resep-kue.txt`, `denah.png` | `denah.png` | — |
| 2 | `denah.png` | `denah.png`, `resep-kue.txt` | — |
| 3 | `denah.png` | `denah-lama.png`, `resep-kue.txt` | — |
| 4 | (kosong) | `denah-lama.png`, `resep-kue.txt` | `denah.png` |

Hasil: `/data/Arsip` berisi **2** berkas; `/data/Masuk` kosong; satu berkas
dapat dipulihkan dari Tempat Sampah.

## 3. Akun pengguna dan pemilik berkas

Sistem operasi membedakan siapa yang memakai komputer lewat **akun
pengguna**. Setiap berkas punya **pemilik** (biasanya akun yang
membuatnya).

| Jenis akun | Boleh melakukan |
|---|---|
| **Pengguna biasa** | Memakai aplikasi dan mengelola berkas miliknya sendiri |
| **Administrator** (*admin*) | Ditambah: memasang software sistem, mengubah pengaturan OS, mengubah izin berkas pengguna lain |

Kebiasaan aman: pakai akun **pengguna biasa** untuk kegiatan sehari-hari;
pakai akun admin hanya saat memang perlu.

## 4. Izin baca, tulis, jalankan

| Izin | Untuk berkas berarti | Contoh |
|---|---|---|
| **Baca** (*read*) | Boleh membuka dan melihat isi | Membaca jadwal piket |
| **Tulis** (*write*) | Boleh mengubah dan menyimpan perubahan; di model W2 juga menghapus | Mengedit jadwal piket |
| **Jalankan** (*execute*) | Boleh menjalankan berkas sebagai program | Menjalankan pemasang aplikasi |

Contoh tabel izin (model W2; berkas `jadwal-piket.xlsx` milik akun `guru`):

| Akun | Baca | Tulis |
|---|---|---|
| `guru` (pemilik) | Ya | Ya |
| `siswa` | Ya | Tidak |

*Deskripsi tabel:* pemilik boleh membaca dan menulis; akun siswa hanya
boleh membaca.

Artinya: siswa dapat **melihat** jadwal tetapi tidak dapat **mengubahnya**.

*Model sederhana W2:* sistem nyata punya aturan lebih rinci (grup,
izin folder, daftar kontrol akses). Di W2 kita hanya memakai tabel
akun × izin seperti di atas, dan menganggap **izin tulis pada berkas**
cukup untuk mengubah **dan** menghapusnya. Di sistem nyata (mis. Linux),
boleh-tidaknya **menghapus** berkas sering ditentukan izin **folder
induknya**, bukan izin berkas itu sendiri.

## 5. Prinsip hak minimum dan izin aplikasi

**Prinsip hak minimum** (*least privilege*): berikan izin **sekecil
mungkin** yang masih cukup untuk tugasnya. Bila akun atau aplikasi
bermasalah, kerusakannya terbatas.

Di ponsel, aplikasi meminta **izin aplikasi** kepada sistem operasi:

| Izin | Masuk akal untuk | Patut dicurigai untuk |
|---|---|---|
| Kamera | Aplikasi pemindai dokumen | Aplikasi kalkulator |
| Lokasi | Aplikasi peta | Aplikasi kamus luring |
| Mikrofon | Aplikasi perekam suara | Aplikasi wallpaper |
| Kontak | Aplikasi pesan | Aplikasi game sederhana |

Pilihan seperti "Izinkan **hanya saat aplikasi digunakan**" lebih kecil
daripada "Izinkan sepanjang waktu".

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Menyalin berkas membuat berkas asal pindah." | Salin: asal tetap ada; pindah: asal hilang dari folder asal |
| "Berkas yang dihapus langsung hilang selamanya." | Di model W2 berkas masuk Tempat Sampah dan dapat dipulihkan sampai Tempat Sampah dikosongkan |
| "Izin baca juga membolehkan mengedit." | Mengubah isi butuh izin tulis |
| "Akun admin lebih baik dipakai setiap hari." | Admin punya kuasa besar; kesalahan atau malware ikut berkuasa besar |
| "Aplikasi perlu semua izin agar berjalan baik." | Aplikasi hanya perlu izin yang sesuai fungsinya |

## 7. Latihan terbimbing (`mod-w02.prac-04`, tidak dinilai)

1. Keadaan awal: `/kerja/A` berisi `puisi.txt`; `/kerja/B` kosong.
   Operasi: (1) salin `puisi.txt` ke `/kerja/B`; (2) hapus
   `/kerja/A/puisi.txt`; (3) pulihkan `puisi.txt` dari Tempat Sampah.
   Berapa berkas `puisi.txt` di `/kerja/A` dan di `/kerja/B` setelahnya?
2. Memakai tabel izin §4: bolehkah akun `siswa` menghapus
   `jadwal-piket.xlsx`?
3. Aplikasi resep masakan meminta izin lokasi "sepanjang waktu". Pilihan
   apa yang paling sesuai prinsip hak minimum?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa memakai akun pengguna biasa sehari-hari lebih aman?
- Apa yang terjadi pada isi folder saat folder itu dipindah?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Satu di `/kerja/A` (dipulihkan) dan satu di `/kerja/B` (salinan).
2. Tidak; di model W2 menghapus butuh izin tulis (di sistem nyata juga
   bergantung pada izin folder).
3. Tolak izin lokasi; resep tidak membutuhkan lokasi. (Bila ada fitur
   yang benar-benar butuh lokasi, izinkan hanya saat aplikasi digunakan.)

## Ringkasan

- **Salin** mempertahankan asal; **pindah** memindahkan; **hapus** ke
  Tempat Sampah; folder dibawa beserta isinya; nama sama di tujuan →
  ditolak (model W2).
- Setiap berkas punya **pemilik**; izin **baca, tulis, jalankan**
  menentukan apa yang boleh dilakukan setiap akun.
- **Hak minimum**: beri izin sekecil mungkin yang masih cukup — untuk
  akun maupun aplikasi.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Salin | copy | Membuat salinan; asal tetap ada |
| Pindah | move | Memindahkan; asal hilang dari folder asal |
| Ganti nama | rename | Mengubah nama di folder yang sama |
| Tempat Sampah | trash / recycle bin | Tempat berkas terhapus sebelum dihapus permanen |
| Pulihkan | restore | Mengembalikan berkas dari Tempat Sampah |
| Akun pengguna | user account | Identitas pemakai komputer |
| Administrator | administrator (admin) | Akun dengan kuasa mengubah pengaturan sistem |
| Pemilik | owner | Akun yang memiliki berkas |
| Izin | permission | Hak untuk membaca, menulis, atau menjalankan |
| Hak minimum | least privilege | Memberi izin sekecil mungkin yang cukup |
