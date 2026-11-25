---
activity_id: mod-w07.lab.act-02
component: mod-w07.lab
content_version: "1.0"
variants: [mod-w07.lab.act-02.vA, mod-w07.lab.act-02.vB]
competencies: [comp-w07-pattern-01]
max_points: 40
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W7 · Aktivitas 2 — Pengenalan Pola

## Tujuan

Menemukan aturan pola bertambah tetap, berkurang tetap, berlipat, pola gambar, dan pola berulang; menghitung suku ke-n dan jumlah beberapa suku.

## Prasyarat

Pelajaran 2.

## Asumsi (model modul)

Pola bertambah/berkurang tetap: suku ke-n = suku pertama + beda × (n − 1). Pola berulang dengan periode p: pakai sisa pembagian (W5). Bilangan ditulis menurut NB-5 (W5).

**Contoh terlihat (0 poin): `2, 4, 6, …` suku berikutnya 8**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | `7, 11, 15, 19, …` suku berikutnya? | `5, 12, 19, 26, …` suku berikutnya? |
| 02 | `7, 11, 15, 19, …` suku ke-12? | `5, 12, 19, 26, …` suku ke-10? |
| 03 | `64, 56, 48, …` suku berikutnya? | `90, 81, 72, …` suku berikutnya? |
| 04 | `2, 6, 18, 54, …` suku berikutnya? | `1, 4, 16, 64, …` suku berikutnya? |
| 05 | Susunan segitiga titik berisi `1, 3, 6, 10, …` titik. Susunan berikutnya berisi berapa titik? | Susunan persegi titik berisi `1, 4, 9, 16, …` titik. Susunan berikutnya berisi berapa titik? |
| 06 | Lampu berganti warna `merah, kuning, hijau, merah, kuning, hijau, …`. Warna **ke-20**? | Jadwal piket berulang `pagi, siang, malam, pagi, siang, malam, …`. Jadwal **ke-17**? |
| 07 | Baris ke-1 berisi 6 kursi; setiap baris berikutnya bertambah 2 kursi. Baris **ke-9** berisi berapa kursi? | Baris ke-1 berisi 10 kursi; setiap baris berikutnya bertambah 3 kursi. Baris **ke-7** berisi berapa kursi? |
| 08 | Pada pola kursi yang sama, berapa **jumlah** kursi baris ke-1 sampai ke-4? | Pada pola kursi yang sama, berapa **jumlah** kursi baris ke-1 sampai ke-4? |

## Yang diserahkan

Bilangan untuk 1–5, 7, 8; satu kata untuk 6.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c08 | 5 poin per jawaban benar | 8 × 5 = 40 |
| **Maksimum aktivitas** | | **40** |

## Kasus gagal

Kosong, bentuk yang tidak sesuai NB-5, atau kata yang tidak ada di pola → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-PATTERN.
