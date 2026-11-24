---
component: mod-w01.project
content_version: "1.0"
competencies: [comp-w01-ipos-01, comp-w01-cpu-01, comp-w01-mem-01, comp-w01-unit-01, comp-w01-sw-01, comp-w01-spec-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W1 — Spesifikasi Komputer untuk Belajar Pemrograman

## Skenario

Sepupumu, Rina, akan mulai belajar pemrograman dan ingin merakit komputer
meja. Ia sering membuka editor kode, browser dengan banyak tab, dan video
pembelajaran sekaligus. Rina memintamu menyusun rakitan dari katalog toko
berikut dan menuliskan perhitungannya.

## Tujuan belajar

Menerapkan seluruh tujuan W1: tahap IPOS (LO1), core CPU (LO2), RAM vs
penyimpanan (LO3), satuan kapasitas (LO4), peran sistem operasi (LO5), dan
kompatibilitas serta kebutuhan (LO6).

## Kebutuhan Rina

| ID | Syarat |
|---|---|
| N1 | CPU minimal **6 core** |
| N2 | RAM total minimal **16 GB** |
| N3 | Penyimpanan **SSD** minimal **512 GB** |
| N4 | Semua komponen **kompatibel** (soket, jenis RAM, jumlah keping ≤ slot) |
| N5 | Daya PSU ≥ kebutuhan daya (= daya CPU + 100 W) |
| N6 | Total harga ≤ **Rp 6.500.000** |

## Katalog (informasi awal; harga fiktif)

| ID | Jenis | Spesifikasi | Daya | Harga (Rp) |
|---|---|---|---|---|
| CPU-1 | CPU | Soket A, 4 core, 3,6 GHz | 65 W | 1600000 |
| CPU-2 | CPU | Soket A, 6 core, 3,9 GHz | 65 W | 2400000 |
| CPU-3 | CPU | Soket A, 8 core, 4,2 GHz | 105 W | 3900000 |
| CPU-4 | CPU | Soket B, 6 core, 4,0 GHz | 65 W | 2300000 |
| CPU-5 | CPU | Soket B, 10 core, 4,5 GHz | 125 W | 4800000 |
| MB-1 | Motherboard | Soket A, DDR4, 2 slot RAM | — | 1300000 |
| MB-2 | Motherboard | Soket A, DDR5, 4 slot RAM | — | 2100000 |
| MB-3 | Motherboard | Soket B, DDR4, 4 slot RAM | — | 1500000 |
| MB-4 | Motherboard | Soket B, DDR5, 2 slot RAM | — | 1900000 |
| RAM-1 | RAM | DDR4, 8 GB per keping | — | 350000 per keping |
| RAM-2 | RAM | DDR4, 16 GB per keping | — | 650000 per keping |
| RAM-3 | RAM | DDR5, 8 GB per keping | — | 450000 per keping |
| RAM-4 | RAM | DDR5, 16 GB per keping | — | 800000 per keping |
| STO-1 | Penyimpanan | HDD 1000 GB | — | 600000 |
| STO-2 | Penyimpanan | SSD 256 GB | — | 400000 |
| STO-3 | Penyimpanan | SSD 512 GB | — | 650000 |
| STO-4 | Penyimpanan | SSD 1000 GB | — | 1100000 |
| PSU-1 | PSU | 300 W | — | 350000 |
| PSU-2 | PSU | 450 W | — | 500000 |
| PSU-3 | PSU | 650 W | — | 800000 |

*Deskripsi tabel:* 20 komponen dalam lima jenis; setiap baris memuat ID,
spesifikasi, daya (khusus CPU), dan harga dalam rupiah tanpa titik.

## Deliverable (formulir di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1 | ID CPU | Satu ID katalog |
| F2 | ID motherboard | Satu ID katalog |
| F3 | ID RAM dan jumlah keping | Satu ID katalog + bilangan bulat |
| F4 | ID penyimpanan | Satu ID katalog |
| F5 | ID PSU | Satu ID katalog |
| F6 | Total harga (Rp) | Bilangan bulat tanpa titik/huruf |
| F7 | Kebutuhan daya (W) | Bilangan bulat |
| F8 | RAM total (GB) = kapasitas per keping × jumlah keping | Bilangan bulat |
| F9 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Instruksi

1. Pilih CPU yang memenuhi N1.
2. Pilih motherboard dengan **soket yang sama**.
3. Pilih RAM dengan **jenis yang sama** dengan motherboard; tentukan jumlah
   keping (bilangan bulat 1–4) agar N2 terpenuhi dan jumlah keping ≤ slot.
4. Pilih SSD yang memenuhi N3.
5. Hitung kebutuhan daya (F7) dan pilih PSU yang memenuhi N5.
6. Hitung total harga (F6) dan pastikan N6 terpenuhi. Bila tidak, ganti
   komponen dan hitung ulang.
7. Isi RAM total (F8) dan jawab lima soal penjelasan (F9).
8. Periksa semua isian, lalu tekan **Serahkan** (dengan konfirmasi).

## Contoh bentuk isian (bukan jawaban proyek)

Contoh ini memakai **katalog latihan Pelajaran 4** (ID `X-…`), bukan katalog
proyek, sehingga tidak memberi jawaban.

| Isian | Contoh bentuk yang benar |
|---|---|
| F1–F5 | `X-CPU2`, `X-MB2`, `X-RAM2` dengan jumlah keping `4`, `X-SSD1`, `X-PSU1` |
| F6 | `8360000` (= 3600000 + 2000000 + 4 × 440000 + 640000 + 360000) |
| F7 | `205` (= 105 + 100) |
| F8 | `32` (= 8 GB per keping × 4 keping) |

**Aturan menulis angka.** Bentuk terbaik: angka saja, tanpa titik, spasi,
"Rp", atau satuan (mendapat poin format). Bentuk `5.400.000`,
`Rp 5.400.000`, `165 W`, atau `16 GB` tetap dibaca untuk pemeriksaan
perhitungan, tetapi kehilangan poin format. Tidak dapat dibaca sama sekali:
titik di tempat salah (`5.40.000`), spasi di dalam angka (`5 400 000`),
koma/desimal (`16,5`), tanda `+`/`−`, satuan lain (`16 MB`), atau kata.

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Soket CPU dan motherboard berbeda | Pemeriksaan soket gagal |
| Jenis RAM (DDR4/DDR5) tidak sama dengan motherboard | Pemeriksaan jenis RAM gagal |
| Jumlah keping RAM melebihi slot motherboard | Rakitan tidak mungkin dipasang: pemeriksaan RAM total dan anggaran gagal; format jumlah keping gagal |
| Jumlah keping bukan bilangan bulat 1–4 (mis. `0`, `2,5`) | Pemeriksaan yang memakai jumlah keping gagal |
| Kebutuhan tidak terpenuhi (core, RAM, SSD, daya) atau total melebihi anggaran | Pemeriksaan syarat itu gagal |
| F6, F7, atau F8 tidak sama dengan hasil hitung dari pilihanmu | Pemeriksaan perhitungan itu gagal |
| Menulis `Rp 5.000.000` atau `16 GB` | Poin format hilang; perhitungan tetap diperiksa |
| Menulis `5.00.000`, `16,5`, atau `16 MB` | Angka tidak dapat dibaca: poin kelengkapan, perhitungan, dan format untuk isian itu hilang |
| Mengosongkan F6, F7, F8, atau jumlah keping | Poin kelengkapan, perhitungan, dan format untuk isian itu hilang |
| ID salah tulis atau tidak ada di katalog | Isian itu tidak sah; pemeriksaan yang membutuhkannya gagal, yang lain tetap dinilai |
| Centang "sudah saya periksa" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | 10 pemeriksaan: soket, jenis RAM, core, RAM total, SSD, daya PSU, anggaran, kebenaran F6, F7, dan F8 |
| K2 Kelengkapan deliverable | 20 | F1–F8 dan jumlah keping terisi **dengan bentuk yang sah** (ID dari katalog; angka yang dapat dibaca; jumlah keping 1–4). Kebenaran nilai dinilai di K1, bentuk paling ketat di K3 |
| K3 Struktur dan format | 10 | Uang dan angka hanya digit; jumlah keping bilangan bulat 1–4 dan ≤ slot |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Kredit parsial per pemeriksaan. Isian yang tidak sah atau kosong membuat
pemeriksaan yang membutuhkannya bernilai 0; pemeriksaan lain tetap dinilai
(MR-2).

## Bukti yang dinilai

Hanya isian F1–F9. Pernyataan "sudah selesai" atau catatan bebas tidak
dinilai (MR-6).

## Remedial

Attempt baru boleh dimulai dari salinan isian sebelumnya (MPV-A). Perbaiki
pemeriksaan yang gagal sesuai umpan balik. Attempt lama tetap tersimpan;
skor terbaik dipakai (D-12).

## Durasi

90 menit (memilih komponen 40, menghitung 25, memeriksa 10, soal
penjelasan 15).
