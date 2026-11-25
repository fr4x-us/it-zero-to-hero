---
activity_id: mod-w06.lab.act-03
component: mod-w06.lab
content_version: "1.0"
variants: [mod-w06.lab.act-03.vA, mod-w06.lab.act-03.vB]
competencies: [comp-w06-table-01, comp-w06-model-01, comp-w06-ops-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W6 · Aktivitas 3 — Ekspresi Boolean dan Pemodelan

## Tujuan

Mengevaluasi ekspresi tiga variabel, mengubah kalimat syarat menjadi ekspresi, mengenali ekspresi ekuivalen dengan tabel kebenaran, dan menghitung kombinasi yang membuat ekspresi bernilai 1.

## Prasyarat

Pelajaran 3, Pelajaran 4.

## Asumsi (model modul)

Nilai Boolean 1 = benar, 0 = salah. Prioritas `NOT` → `AND` → `OR`; kurung lebih dulu. Dua ekspresi **ekuivalen** bila bernilai sama di **semua** baris tabel kebenaran. Kata "dan" dalam syarat berarti kedua kondisi harus terpenuhi; "atau" berarti sedikitnya satu.

**Contoh terlihat (0 poin): "kipas menyala bila tombol A atau tombol B" → `A OR B`**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | `A AND (B OR C)` pada A = 1, B = 1, C = 0 | `(A OR B) AND C` pada A = 0, B = 1, C = 1 |
| 02 | `NOT A AND NOT C` pada A = 0, B = 1, C = 1 | `NOT B AND C` pada A = 1, B = 0, C = 0 |
| 03 | Kunci pintu terbuka bila **kartu benar (K = 1) dan PIN benar (P = 1)**. Ekspresinya? (a) `K OR P`, (b) `K AND P`, (c) `NOT K AND P`, (d) `K AND NOT P` | Mesin fotokopi bekerja bila **daya hidup (D = 1) dan kertas tersedia (K = 1)**. Ekspresinya? (a) `D AND K`, (b) `D OR K`, (c) `NOT D AND K`, (d) `D AND NOT K` |
| 04 | Lampu darurat menyala bila **listrik padam (L = 1) atau tombol uji ditekan (U = 1)**. Ekspresinya? (a) `L AND U`, (b) `NOT L`, (c) `L OR U`, (d) `L AND NOT U` | Bel berbunyi bila **tombol depan (F = 1) atau tombol belakang (G = 1)** ditekan. Ekspresinya? (a) `F AND G`, (b) `F OR G`, (c) `NOT F`, (d) `F AND NOT G` |
| 05 | Ekspresi yang ekuivalen dengan `A OR (A AND B)` di semua baris? (a) `B`, (b) `A AND B`, (c) `NOT A`, (d) `A` | Ekspresi yang ekuivalen dengan `A AND (A OR B)` di semua baris? (a) `A OR B`, (b) `B`, (c) `A`, (d) `NOT B` |
| 06 | Berapa kombinasi (A, B, C) dari 8 yang membuat `A AND (B OR C)` bernilai 1? | Berapa kombinasi (A, B, C) dari 8 yang membuat `(A OR B) AND C` bernilai 1? |

## Yang diserahkan

Digit 0/1 untuk 1–2; huruf opsi untuk 3–5; bilangan desimal untuk 6 (boleh diikuti kata `kombinasi`).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, huruf di luar a–d, atau bentuk yang tidak sesuai → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-TABLE, R-MODEL, R-OPS.
