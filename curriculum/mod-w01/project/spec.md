---
component: mod-w01.project
content_version: "1.0"
competencies: [comp-w01-ipos-01, comp-w01-cpu-01, comp-w01-mem-01, comp-w01-unit-01, comp-w01-sw-01, comp-w01-spec-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan dan kunci K4; tidak ditampilkan sebelum dinilai
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
| F8 | RAM total (GB) | Bilangan bulat |
| F9 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Instruksi

1. Pilih CPU yang memenuhi N1.
2. Pilih motherboard dengan **soket yang sama**.
3. Pilih RAM dengan **jenis yang sama** dengan motherboard; tentukan jumlah
   keping agar N2 terpenuhi dan jumlah keping ≤ slot.
4. Pilih SSD yang memenuhi N3.
5. Hitung kebutuhan daya (F7) dan pilih PSU yang memenuhi N5.
6. Hitung total harga (F6) dan pastikan N6 terpenuhi. Bila tidak, ganti
   komponen dan hitung ulang.
7. Isi RAM total (F8) dan jawab lima soal penjelasan (F9).
8. Periksa semua isian, lalu tekan **Serahkan** (dengan konfirmasi).

## Contoh keluaran yang dapat diterima

| Isian | Nilai |
|---|---|
| F1–F5 | CPU-2, MB-1, RAM-1 × 2, STO-3, PSU-1 |
| F6 | 5400000 (= 2400000 + 1300000 + 2 × 350000 + 650000 + 350000) |
| F7 | 165 (= 65 + 100) |
| F8 | 16 |

Ini **bukan satu-satunya** jawaban benar: penilaian memeriksa syarat, bukan
mencocokkan satu kombinasi. Contoh lain yang juga memenuhi: CPU-4, MB-3,
RAM-2 × 1, STO-3, PSU-1 (total 5450000).

## Contoh keluaran yang tidak dapat diterima

| Isian | Masalah |
|---|---|
| CPU-4 + MB-1 | Soket B vs Soket A (N4 gagal) |
| MB-1 + RAM-3 | DDR5 di motherboard DDR4 (N4 gagal) |
| MB-1 + RAM-1 × 4 | 4 keping melebihi 2 slot (format K3 dan N4 gagal) |
| CPU-1 | 4 core (N1 gagal) |
| STO-1 | HDD, bukan SSD (N3 gagal) |
| CPU-3 + MB-1 + RAM-2 × 1 + STO-3 + PSU-1 | Kompatibel, tetapi total 6850000 > 6500000 (N6 gagal) |
| F6 ditulis "Rp 5.400.000" | Bukan bilangan bulat tanpa titik/huruf (K3) |
| Centang "sudah saya periksa" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | 9 pemeriksaan syarat dan perhitungan |
| K2 Kelengkapan deliverable | 20 | F1–F8 terisi dengan bentuk valid |
| K3 Struktur dan format | 10 | Uang dan kapasitas bilangan bulat; jumlah keping valid |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Kredit parsial per pemeriksaan; isian yang hilang membuat pemeriksaan yang
bergantung padanya bernilai 0 (MR-2).

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
