---
activity_id: mod-w06.lab.act-01
component: mod-w06.lab
content_version: "1.0"
variants: [mod-w06.lab.act-01.vA, mod-w06.lab.act-01.vB]
competencies: [comp-w06-bin2dec-01, comp-w06-dec2bin-01, comp-w06-repr-01]
max_points: 40
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W6 · Aktivitas 1 — Konversi Biner dan Desimal

## Tujuan

Mengubah bilangan biner (termasuk 8 bit dengan nol di depan) ke desimal, mengubah desimal ke biner tanpa nol di depan maupun tepat n bit, dan menentukan rentang nilai n bit.

## Prasyarat

Pelajaran 1, Pelajaran 2.

## Asumsi (model modul)

Semua bilangan **tak bertanda** (nol dan positif). Bit diberi nomor posisi dari kanan mulai 0; bobot = 2^posisi. **Aturan BN-6:** jawaban biner hanya 0 dan 1, tanpa spasi atau awalan (`0b`) atau subskrip; "tanpa nol di depan" berarti bilangan 0 ditulis `0` dan bilangan positif diawali digit 1; "tepat n bit" berarti tepat n digit, nol di depan dipakai untuk mengisi lebar (0 dalam 8 bit = `00000000`). Jawaban desimal ditulis dengan digit biasa tanpa nol di depan (NB-5).

**Contoh terlihat (0 poin): `11₂` = 3; 2 → biner `10`; 1 → tepat 4 bit `0001`**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | `110₂` = … (desimal) | `101₂` = … (desimal) |
| 02 | `10010₂` = … (desimal) | `11001₂` = … (desimal) |
| 03 | `11110000₂` = … (desimal) | `10000001₂` = … (desimal) |
| 04 | `01010101₂` = … (desimal) | `00111100₂` = … (desimal) |
| 05 | Ubah **22** ke biner (tanpa nol di depan). | Ubah **27** ke biner (tanpa nol di depan). |
| 06 | Ubah **9** ke biner **tepat 8 bit**. | Ubah **6** ke biner **tepat 8 bit**. |
| 07 | Ubah **100** ke biner (tanpa nol di depan). | Ubah **75** ke biner (tanpa nol di depan). |
| 08 | Nilai desimal **terbesar** untuk **4 bit** tak bertanda? | Nilai desimal **terbesar** untuk **6 bit** tak bertanda? |

## Yang diserahkan

Desimal untuk 1–4 dan 8; biner untuk 5–7 sesuai aturan panjang di soal.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c08 | 5 poin per jawaban benar | 8 × 5 = 40 |
| **Maksimum aktivitas** | | **40** |

## Kasus gagal

Kosong, digit selain 0/1 pada jawaban biner, panjang yang tidak sesuai instruksi (mis. nol di depan pada soal "tanpa nol di depan"), awalan `0b`, atau jawaban biner pada soal desimal → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-REPR, R-BIN2DEC, R-DEC2BIN.
