---
activity_id: mod-w02.lab.act-03
component: mod-w02.lab
content_version: "1.0"
variants: [mod-w02.lab.act-03.vA, mod-w02.lab.act-03.vB]
competencies: [comp-w02-ops-01, comp-w02-perm-01, comp-w02-proc-01]
max_points: 40
estimated_minutes: 35
checks_file: checks.yaml
---

# Lab W2 · Aktivitas 3 — Simulasi Operasi Berkas, Izin, dan Proses

## Tujuan

1. Menelusuri enam operasi berkas berurutan dan menentukan keadaan akhir.
2. Membaca tabel izin dan memilih izin minimum.
3. Menentukan proses yang perlu diakhiri dari tabel manajer tugas.

## Prasyarat

Pelajaran 2 §3, Pelajaran 4 §1–§5.

## Aturan simulasi (model operasi W2)

| ID | Aturan |
|---|---|
| OP-1 | Menyalin/memindahkan folder membawa seluruh isinya |
| OP-2 | Nama sama persis sudah ada di folder tujuan → operasi **ditolak**, tidak ada yang berubah |
| OP-3 | Operasi dijalankan berurutan dari keadaan hasil operasi sebelumnya |
| OP-4 | Berkas di Tempat Sampah tidak dihitung sebagai isi folder mana pun |

**Contoh terlihat (tidak dinilai):** contoh terbimbing Pelajaran 4 §2
(keadaan `/data`).

## Data (fixture)

**Varian A — folder bersama panitia acara**

Keadaan awal:

```
/bersama
├── Masuk
│   ├── brosur.pdf
│   ├── menu.xlsx
│   └── foto-acara.jpg
├── Acara
└── Lama
    └── menu.xlsx
```

*Deskripsi:* `Masuk` berisi tiga berkas; `Acara` kosong; `Lama` berisi
`menu.xlsx`.

| Langkah | Operasi |
|---|---|
| 1 | Buat folder `/bersama/Acara/Foto` |
| 2 | Pindah `/bersama/Masuk/foto-acara.jpg` ke `/bersama/Acara/Foto` |
| 3 | Salin `/bersama/Masuk/brosur.pdf` ke `/bersama/Acara` |
| 4 | Pindah `/bersama/Masuk/menu.xlsx` ke `/bersama/Lama` |
| 5 | Hapus `/bersama/Masuk/brosur.pdf` |
| 6 | Ganti nama `/bersama/Acara/brosur.pdf` menjadi `brosur-final.pdf` |

Tabel izin berkas brosur versi akhir (pemilik `panitia`):

| Akun | Baca | Tulis |
|---|---|---|
| panitia (pemilik) | Ya | Ya |
| relawan | Ya | Tidak |
| tamu | Tidak | Tidak |

Tabel manajer tugas (angka fiktif):

| Nama proses | PID | Memori | Status |
|---|---|---|---|
| Pengolah kata | 6012 | 310 MB | Berjalan |
| Pengelola berkas | 6027 | 95 MB | Tidak menanggapi |
| Pemutar musik | 6040 | 140 MB | Berjalan |

**Varian B — folder klub**

Keadaan awal:

```
/klub
├── Unggah
│   ├── poster.png
│   ├── jadwal.pdf
│   ├── daftar-anggota.csv
│   └── catatan.txt
├── Lomba
└── Arsip
    └── jadwal.pdf
```

*Deskripsi:* `Unggah` berisi empat berkas; `Lomba` kosong; `Arsip` berisi
`jadwal.pdf`.

| Langkah | Operasi |
|---|---|
| 1 | Buat folder `/klub/Lomba/Data` |
| 2 | Salin `/klub/Unggah/poster.png` ke `/klub/Lomba` |
| 3 | Pindah `/klub/Unggah/jadwal.pdf` ke `/klub/Arsip` |
| 4 | Pindah `/klub/Unggah/daftar-anggota.csv` ke `/klub/Lomba/Data` |
| 5 | Ganti nama `/klub/Lomba/poster.png` menjadi `poster-lomba.png` |
| 6 | Hapus `/klub/Unggah/poster.png` |

Tabel izin berkas poster versi akhir (pemilik `ketua`):

| Akun | Baca | Tulis |
|---|---|---|
| ketua (pemilik) | Ya | Ya |
| publik | Tidak | Tidak |
| anggota | Ya | Tidak |

Tabel manajer tugas (angka fiktif):

| Nama proses | PID | Memori | Status |
|---|---|---|---|
| Browser | 7105 | 850 MB | Berjalan |
| Kalkulator | 7118 | 20 MB | Berjalan |
| Pengelola berkas | 7131 | 110 MB | Tidak menanggapi |

## Pertanyaan

| No. | Varian A | Varian B |
|---|---|---|
| 1 | Path absolut `foto-acara.jpg` setelah langkah 6 | Path absolut `daftar-anggota.csv` setelah langkah 6 |
| 2 | Jumlah berkas **langsung** di `/bersama/Masuk` setelah langkah 6 (tanpa subfolder dan Tempat Sampah) | Jumlah berkas **langsung** di `/klub/Unggah` setelah langkah 6 |
| 3 | Nomor langkah yang ditolak | Nomor langkah yang ditolak |
| 4 | Nama berkas di Tempat Sampah | Nama berkas di Tempat Sampah |
| 5 | Path absolut versi akhir brosur | Path absolut versi akhir poster |
| 6 | Akun yang dapat membuka `brosur-final.pdf` tetapi tidak dapat mengubahnya (`panitia` / `relawan` / `tamu`) | Akun yang dapat membuka `poster-lomba.png` tetapi tidak dapat mengubahnya (`ketua` / `publik` / `anggota`) |
| 7 | Relawan baru bertugas memperbarui harga di `menu.xlsx`. Izin minimum yang cukup: (a) baca saja, (b) baca dan tulis, (c) jalankan saja, (d) jadikan administrator | Anggota baru hanya perlu melihat `daftar-anggota.csv`. Izin minimum yang cukup: (a) baca saja, (b) baca dan tulis, (c) jalankan saja, (d) jadikan administrator |
| 8 | PID proses yang perlu diakhiri agar pengelola berkas dapat dibuka ulang | PID proses yang perlu diakhiri agar pengelola berkas dapat dibuka ulang |

## Yang diserahkan

Delapan jawaban: path (1, 5), bilangan bulat (2, 3, 8), nama berkas (4),
nama akun (6), huruf opsi (7).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c08 | 5 poin per jawaban yang benar | 8 × 5 = 40 |
| **Maksimum aktivitas** | | **40** |

## Kasus gagal

Kosong, bentuk ditolak (path dengan `\`, angka dengan desimal, huruf
besar/kecil nama berkas berbeda), atau pilihan di luar daftar → 0 untuk
pemeriksaan itu. Pemeriksaan lain tetap dinilai. Gangguan sistem → evaluasi
diulang tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan, keadaan akhir pohon, dan penjelasan izin serta
proses untuk varian yang kamu kerjakan.

## Remedial

Varian lain menurut VA-2; ulangi Pelajaran 4 §1–§5 dan Pelajaran 2 §3;
materi remedial R-OPS, R-PERM, R-PROC.
