---
activity_id: mod-w03.lab.act-01
component: mod-w03.lab
content_version: "1.0"
variants: [mod-w03.lab.act-01.vA, mod-w03.lab.act-01.vB]
competencies: [comp-w03-ip-01]
max_points: 30
estimated_minutes: 25
checks_file: checks.yaml
---

# Lab W3 · Aktivitas 1 — Klasifikasi Alamat IPv4

## Tujuan

1. Memeriksa apakah sebuah alamat IPv4 valid (model W3).
2. Menentukan apakah alamat yang valid termasuk **privat** atau **publik**.

## Prasyarat

Pelajaran 2 §1–§2.

## Asumsi jaringan (model W3)

- Valid: tepat 4 oktet desimal 0–255, tanpa nol di depan.
- Privat: `10.x.x.x`, `172.16.x.x`–`172.31.x.x`, `192.168.x.x`.
- Publik: alamat valid lain (bukan `127.x.x.x`). Soal ini tidak memakai
  rentang khusus lain.
- Alamat hanya diklasifikasi; tidak ada perangkat yang perlu dihubungi.

## Instruksi

Untuk setiap alamat, pilih satu kode: `P` privat (valid), `U` publik
(valid), atau `X` tidak valid. Tekan **Serahkan** (dengan konfirmasi).

**Contoh terlihat (tidak dinilai):** `192.168.99.99` → `P`.

## Data (fixture, urutan tampil tetap)

| ID | Varian A | Varian B |
|---|---|---|
| A1 | `192.168.1.15` | `10.1.1.1` |
| A2 | `8.8.8.8` | `172.15.9.9` |
| A3 | `172.16.40.2` | `192.168.0.256` |
| A4 | `256.10.1.1` | `172.31.255.10` |
| A5 | `10.200.3.4` | `1.1.1.1` |
| A6 | `172.32.0.5` | `192.168.10.20` |
| A7 | `192.168.1` | `100.20.30` |
| A8 | `36.89.12.5` | `52.14.8.200` |
| A9 | `192.168.200.9` | `10.255.0.1` |
| A10 | `10.0.0.300` | `12.300.4.5` |

*Deskripsi tabel:* sepuluh baris; kolom kedua alamat varian A, kolom
ketiga alamat varian B. Pelajar hanya melihat kolom variannya.

## Yang diserahkan

Sepuluh kode (`P`, `U`, atau `X`).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c10 | 3 poin per kode benar | 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong atau kode di luar `P`/`U`/`X` → 0 untuk pemeriksaan itu; lainnya
tetap dinilai. Gangguan sistem → evaluasi diulang tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per alamat dan alasan (rentang atau aturan validitas) untuk
varian yang kamu kerjakan.

## Remedial

Varian lain menurut VA-2; ulangi Pelajaran 2 §1–§2; materi remedial R-IP.
