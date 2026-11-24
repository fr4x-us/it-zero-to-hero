---
activity_id: mod-w01.lab.act-01
component: mod-w01.lab
content_version: "1.0"
variants: [mod-w01.lab.act-01.vA, mod-w01.lab.act-01.vB]
competencies: [comp-w01-ipos-01]
max_points: 30
estimated_minutes: 30
checks_file: checks.yaml   # kunci dan poin; tidak ditampilkan sebelum evaluasi
---

# Lab W1 · Aktivitas 1 — Klasifikasi Perangkat

## Tujuan

Mengelompokkan perangkat ke tahap kerja komputer yang tepat: **Input**,
**Output**, **Input dan output**, **Penyimpanan**, atau **Pemrosesan**.

## Prasyarat

Pelajaran 1 (model IPOS) dan Pelajaran 2 §5–§7 (komponen dan perangkat).

## Skenario

Sekolah tempatmu belajar menerima kiriman perangkat baru. Kamu diminta
menempelkan label kelompok pada setiap perangkat sebelum dibagikan ke
laboratorium.

## Instruksi

1. Baca daftar 10 perangkat.
2. Untuk setiap perangkat pilih **tepat satu** kelompok dari daftar
   kelompok.
3. Bila sebuah perangkat menjalankan input **dan** output, pilih kelompok
   "Input dan output", bukan salah satunya. Kelompok mengikuti fungsi
   perangkat seperti yang tertulis (mis. "Printer (hanya mencetak)"; printer
   multifungsi yang juga memindai adalah input dan output).
4. Periksa kembali, lalu tekan **Serahkan** (aktivitas akan dikunci dan
   dievaluasi).

**Contoh terlihat (tidak dinilai):** Joystick → Input.

## Data (fixture)

| Varian A (`vA`) | Varian B (`vB`, remedial setara) |
|---|---|
| d01 Stylus (pena digital) | d01 Scanner |
| d02 Monitor | d02 Proyektor |
| d03 Printer (hanya mencetak) | d03 Webcam |
| d04 Pemindai sidik jari | d04 Headset dengan mikrofon |
| d05 Layar sentuh | d05 HDD |
| d06 SSD | d06 GPU (prosesor grafis) |
| d07 CPU | d07 Kamera CCTV |
| d08 Mikrofon | d08 Earphone tanpa mikrofon |
| d09 Speaker tanpa mikrofon | d09 Kartu memori SD |
| d10 Keping DVD (cakram) | d10 Printer (hanya mencetak) |

Sebagian perangkat tidak tercantum di tabel Pelajaran 2; tentukan kelompoknya
dengan menerapkan pertanyaan IPOS (data masuk? hasil keluar? disimpan?
diolah?).

Kelompok: `I` Input · `O` Output · `IO` Input dan output · `S`
Penyimpanan · `P` Pemrosesan.

## Yang diserahkan

Satu kode kelompok untuk setiap `d01`–`d10`.

## Penilaian (rinci di `checks.yaml`)

| Pemeriksaan | Poin |
|---|---|
| 10 perangkat × 3 poin (benar = 3, selain itu 0) | 30 |
| **Maksimum aktivitas** | **30** |

Kesetaraan varian: kedua varian berisi 3 input, 3 output, 1 input-dan-output,
2 penyimpanan, 1 pemrosesan; poin sama.

## Kasus gagal

| Kasus | Perlakuan |
|---|---|
| Perangkat tidak diberi kelompok | 0 poin untuk perangkat itu |
| Kode kelompok tidak dikenal atau dua kode untuk satu perangkat | 0 poin untuk perangkat itu (`INVALID_ANSWER`) |
| Aplikasi tertutup saat evaluasi | Evaluasi diulang dari jawaban yang sama, tanpa attempt baru (D-24) |

## Umpan balik (setelah evaluasi)

Benar/salah per perangkat dan alasan singkat (mis. "Layar sentuh menampilkan
gambar dan menerima sentuhan").

## Remedial

Attempt komponen lab berikutnya memakai varian lain menurut aturan VA-2
(bergiliran A ↔ B). Ulangi Pelajaran 2 §7 dan materi remedial
`remedial/remedial.md` bagian R-IPOS.
