---
component: mod-w03.project
content_version: "1.0"
competencies: [comp-w03-net-01, comp-w03-ip-01, comp-w03-subnet-01, comp-w03-proto-01, comp-w03-layer-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W3 — Rencana Alamat Jaringan Rumah

## Skenario

Keluarga Pak Hadi memasang router Wi-Fi baru. Ponsel tamu dan anggota
keluarga akan memakai alamat otomatis dari DHCP, tetapi lima perangkat
harus memakai **alamat statis** agar selalu mudah ditemukan. Kamu diminta
menyusun tabel alamatnya. Semua ini adalah **rencana di atas kertas**;
tidak ada perangkat atau jaringan nyata yang perlu diubah.

## Tujuan belajar

Menerapkan tujuan W3: peran perangkat (LO1), alamat IPv4 dan privat
(LO2), jaringan /24 (LO3), DHCP (LO4), dan lapisan TCP/IP (LO5).
Perhitungan kecepatan (LO6) dinilai di teori, lab, dan concept.

## Informasi awal

| Hal | Nilai |
|---|---|
| Jaringan | `192.168.50.0`, mask `255.255.255.0` (/24) |
| Rentang DHCP router (termasuk kedua ujung) | `192.168.50.100` – `192.168.50.199` |
| Perangkat statis | D1 Komputer kerja · D2 Printer · D3 Kamera CCTV · D4 TV pintar · D5 Penyimpanan bersama (NAS) |

## Kebutuhan

| ID | Syarat |
|---|---|
| N1 | Router (gateway) memakai **host pertama** jaringan |
| N2 | Setiap perangkat D1–D5 memakai alamat valid di jaringan `192.168.50.0/24`, bukan alamat jaringan/broadcast, dan **di luar** rentang DHCP |
| N3 | Keenam alamat (router + D1–D5) **unik** |
| N4 | Setiap perangkat memakai mask jaringan ini dan gateway = alamat router |
| N5 | Alamat ditulis empat oktet tanpa nol di depan; mask ditulis bentuk desimal bertitik |

## Deliverable (formulir di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1 | Alamat IP router (gateway) | Alamat IPv4 |
| F2 | Tabel D1–D5: alamat IP, mask, gateway setiap perangkat | 5 baris × 3 isian |
| F3 | Alamat jaringan | Alamat IPv4 |
| F4 | Alamat broadcast | Alamat IPv4 |
| F5 | Bila rencana memenuhi N1–N4, berapa alamat host yang **masih tersedia** untuk perangkat statis baru (di luar rentang DHCP)? | Bilangan bulat |
| F6 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Instruksi

1. Tentukan alamat router (N1).
2. Tentukan wilayah alamat yang boleh dipakai perangkat statis (N2).
3. Isi tabel D1–D5 dengan alamat unik, mask, dan gateway (N3, N4).
4. Isi alamat jaringan, broadcast, dan hitungan F5.
5. Periksa setiap baris dengan aturan RA-1–RA-5 (Pelajaran 4 §3).
6. Jawab lima soal penjelasan, lalu tekan **Serahkan** (dengan
   konfirmasi).

## Contoh bentuk isian (bukan jawaban proyek)

Memakai jaringan **lain** (`10.9.8.0/24`, rentang DHCP `.50`–`.99`), jadi
tidak memberi jawaban.

| Isian | Contoh bentuk yang benar |
|---|---|
| Alamat IP | `10.9.8.20` |
| Mask | `255.255.255.0` |
| Gateway | `10.9.8.1` |
| Bilangan bulat | `57` atau `57 alamat` (bentuk saja) |

**Aturan menulis.** Alamat: empat oktet, tanpa nol di depan (`10.9.8.020`
tidak dapat dibaca), tanpa spasi. Akhiran `/24` pada alamat dan mask
bentuk `/24` masih dibaca untuk pemeriksaan kebenaran, tetapi kehilangan
poin format.

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Alamat statis di dalam rentang DHCP | Pemeriksaan perangkat itu gagal |
| Memakai `.0` atau `.255` | Pemeriksaan perangkat itu gagal |
| Dua perangkat beralamat sama | Pemeriksaan keunikan gagal |
| Gateway berbeda dari alamat router | Pemeriksaan gateway gagal |
| Alamat di jaringan lain (mis. `192.168.51.x`) | Pemeriksaan perangkat itu gagal |
| Menghitung rentang DHCP tanpa kedua ujung | Hitungan F5 salah |
| Menulis `192.168.050.010` | Alamat tidak dapat dibaca: poin kelengkapan dan pemeriksaan yang membutuhkannya hilang |
| Menulis mask `/24` atau alamat `…/24` | Poin format hilang; kebenaran tetap diperiksa |
| Centang "sudah selesai" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | Router (N1); setiap perangkat (N2); keunikan (N3); mask dan gateway (N4); F3, F4, F5 |
| K2 Kelengkapan deliverable | 20 | Semua isian terisi dengan **bentuk yang dapat dibaca**. Kebenaran nilai dinilai di K1 |
| K3 Struktur dan format | 10 | Bentuk ketat N5: alamat tanpa akhiran `/24`, mask desimal bertitik, F5 hanya digit |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Kredit parsial per pemeriksaan; isian yang tidak sah membuat pemeriksaan
yang membutuhkannya bernilai 0, yang lain tetap dinilai (MR-2). Ada banyak
rencana yang benar; semua dinilai dengan aturan yang sama (MR-3).

## Bukti yang dinilai

Hanya isian F1–F6. Pernyataan "sudah selesai" tidak dinilai (MR-6).

## Remedial

Attempt baru boleh dimulai dari salinan isian sebelumnya (MPV-A). Attempt
lama tetap tersimpan; skor terbaik dipakai (D-12).

## Durasi

90 menit (memahami kebutuhan 15, menentukan wilayah alamat 15, mengisi
tabel 30, menghitung 10, memeriksa 5, soal penjelasan 15).
