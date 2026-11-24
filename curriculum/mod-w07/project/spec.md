---
component: mod-w07.project
content_version: "1.0"
competencies: [comp-w07-decomp-01, comp-w07-pattern-01, comp-w07-abstract-01, comp-w07-algo-01, comp-w07-order-01, comp-w07-test-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W7 — Dekomposisi Tugas Jadwal Belajar

## Skenario

Dina dan kelompoknya harus mempresentasikan "Sampah Plastik di Sekolah" pada
hari **Jumat**. Dina ingin menyusun rencana kerja yang rapi. Semua tokoh dan
data fiktif.

## Tujuan belajar

Menerapkan dekomposisi (LO1), pola (LO2), abstraksi (LO3), langkah yang
jelas (LO4), urutan berprasyarat (LO5), dan pemeriksaan (LO6).

## Data (fixture)

**Kelompok sub-masalah** (ditentukan oleh **hasil** tugas):

| Kode | Kelompok |
|---|---|
| `K` | Koordinasi — menghasilkan kesepakatan atau pembagian kerja kelompok |
| `R` | Riset bacaan — menghasilkan bahan dari sumber bacaan topik (buku, artikel) |
| `D` | Data — menghasilkan data pengamatan atau olahannya |
| `P` | Presentasi — menghasilkan atau menyampaikan presentasi |

**Tugas:**

| ID | Tugas | Hasil | Lama (menit) |
|---|---|---|---|
| T1 | Rapat kelompok membahas panduan tugas dari guru | Kesepakatan kelompok tentang kriteria penilaian | 20 |
| T2 | Mencari tiga sumber bacaan di perpustakaan | Tiga sumber bacaan | 60 |
| T3 | Mencatat jumlah botol plastik di kantin selama tiga hari | Tabel data tiga hari | 45 |
| T4 | Membuat grafik dari tabel data | Grafik batang | 30 |
| T5 | Menulis ringkasan dari sumber bacaan | Ringkasan satu halaman | 40 |
| T6 | Menyusun slide presentasi | Slide presentasi | 50 |
| T7 | Berlatih presentasi | Presentasi siap ditampilkan | 35 |
| T8 | Membagi tugas antaranggota | Daftar siapa mengerjakan apa | 20 |

**Prasyarat** ("X sebelum Y" = Y membutuhkan hasil X): T1 sebelum T8; T8
sebelum T2; T8 sebelum T3; T2 sebelum T5; T3 sebelum T4; T4 sebelum T6; T5
sebelum T6; T6 sebelum T7.

**Data botol plastik di kantin** (bertambah tetap): hari 1: 12, hari 2: 15,
hari 3: 18.

**Informasi yang dimiliki Dina:**

| ID | Informasi |
|---|---|
| I1 | Tenggat presentasi: hari Jumat |
| I2 | Perkiraan lama setiap tugas |
| I3 | Prasyarat antartugas |
| I4 | Waktu belajar yang tersedia setiap hari: 70 menit |
| I5 | Warna latar slide yang disukai Dina |
| I6 | Nama kucing peliharaan Dina |
| I7 | Merek laptop kelompok |

## Deliverable (formulir di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1 | Kode kelompok untuk setiap tugas T1–T8 | Satu huruf `K`, `R`, `D`, atau `P` |
| F2 | Satu urutan kedelapan tugas yang memenuhi **semua** prasyarat | ID dipisah spasi atau koma |
| F3 | Menurut pola data, perkiraan jumlah botol pada **hari ke-6** | Bilangan bulat |
| F4 | Informasi yang **relevan untuk menyusun jadwal kerja**: yang dapat mengubah **kapan** atau **dalam urutan apa** tugas dikerjakan | Centang dari I1–I7 |
| F5 | Total lama semua tugas | Bilangan bulat (menit) |
| F6 | Banyak hari **paling sedikit** yang dibutuhkan bila setiap hari hanya tersedia 70 menit (tugas boleh dilanjutkan hari berikutnya) | Bilangan bulat |
| F7 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Aturan isian

- **Urutan:** setiap ID T1–T8 tepat sekali; huruf besar/kecil bebas.
  **Setiap urutan yang memenuhi semua prasyarat diterima** — tidak ada
  satu urutan "resmi".
- **Kode:** bentuk terbaik huruf besar (`K`); huruf kecil tetap dibaca,
  tetapi kehilangan poin format.
- **Bilangan:** bentuk terbaik digit saja (`7`); `7 menit`, `7 hari`, atau
  `7 botol` tetap dibaca, tetapi kehilangan poin format.
- **F4:** pilih semua yang relevan; setiap informasi tidak relevan yang
  ikut dipilih mengurangi kredit pemeriksaan itu (tidak pernah negatif).

## Contoh bentuk isian (bukan jawaban proyek)

Contoh memakai proyek **lain** (tugas `A`, `B`, `C` dengan prasyarat A
sebelum C):

| Isian | Contoh bentuk terbaik |
|---|---|
| Urutan | `A B C` atau `B A C` (keduanya valid) |
| Kode | `D` |
| Bilangan | `7` |

## Instruksi

1. Kelompokkan setiap tugas menurut hasilnya (F1).
2. Susun urutan yang memenuhi semua prasyarat; periksa setiap prasyarat
   satu per satu (F2).
3. Temukan pola data dan perkirakan hari ke-6 (F3).
4. Pilih informasi yang relevan untuk jadwal (F4).
5. Hitung total lama dan banyak hari paling sedikit (F5, F6).
6. Jawab lima soal penjelasan, lalu tekan **Serahkan** (dengan
   konfirmasi).

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Mengelompokkan menurut tempat atau orang, bukan hasil | F1 salah |
| Satu prasyarat terlewat | F2 tidak valid |
| ID terlewat atau ditulis dua kali | F2 tidak dapat dibaca |
| Memilih informasi yang tidak mengubah jadwal | Kredit F4 berkurang |
| Membulatkan banyak hari ke bawah | F6 salah (tugas tidak selesai) |
| Centang "sudah selesai" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | Setiap kode F1; F2 memenuhi semua prasyarat; F3; F4; F5; F6 |
| K2 Kelengkapan deliverable | 20 | Semua isian terisi dalam bentuk yang dapat dibaca |
| K3 Struktur dan format | 10 | Bilangan digit saja; kode huruf besar |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Setiap isian dinilai terhadap data proyek (bukan terhadap isian kamu yang
lain). Isian yang tidak dapat dibaca membuat pemeriksaan yang
membutuhkannya bernilai 0; isian lain tetap dinilai (MR-2).

## Bukti yang dinilai

Hanya isian F1–F7 (MR-6).

## Remedial

Attempt baru boleh dimulai dari salinan isian sebelumnya (MPV-A). Attempt
lama tetap tersimpan; skor terbaik dipakai (D-12).

## Durasi

90 menit (memahami data 10, kelompok 15, urutan 20, pola dan informasi 15,
hitungan 10, memeriksa 5, soal penjelasan 15).
