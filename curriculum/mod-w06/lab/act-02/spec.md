---
activity_id: mod-w06.lab.act-02
component: mod-w06.lab
content_version: "1.0"
variants: [mod-w06.lab.act-02.vA, mod-w06.lab.act-02.vB]
competencies: [comp-w06-ops-01, comp-w06-table-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W6 · Aktivitas 2 — Tabel Kebenaran

## Tujuan

Mengisi baris tabel kebenaran ekspresi dua variabel dan menganalisis tabel lengkap tiga variabel.

## Prasyarat

Pelajaran 3.

## Asumsi (model modul)

Nilai Boolean ditulis **1 (benar)** atau **0 (salah)** — bukan bilangan. Prioritas: `NOT` lebih dulu, lalu `AND`, lalu `OR`; kurung mengubah urutan. Tabel lengkap n variabel memiliki 2ⁿ baris berurutan dari semua 0 sampai semua 1.

**Contoh terlihat (0 poin): `NOT A` pada A = 1 → 0; tabel lengkap 2 variabel = 4 baris**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | `NOT A OR B` pada A = 0, B = 0 | `A AND NOT B` pada A = 0, B = 0 |
| 02 | `NOT A OR B` pada A = 0, B = 1 | `A AND NOT B` pada A = 0, B = 1 |
| 03 | `NOT A OR B` pada A = 1, B = 0 | `A AND NOT B` pada A = 1, B = 0 |
| 04 | `NOT A OR B` pada A = 1, B = 1 | `A AND NOT B` pada A = 1, B = 1 |
| 05 | Pada tabel kebenaran lengkap `(A AND B) OR C` (8 baris), berapa baris bernilai 1? | Pada tabel kebenaran lengkap `(A AND C) OR B` (8 baris), berapa baris bernilai 1? |
| 06 | `(A AND B) OR C` pada A = 1, B = 0, C = 0 | `(A AND C) OR B` pada A = 0, B = 0, C = 1 |

## Yang diserahkan

Satu digit 0 atau 1 untuk 1–4 dan 6; bilangan desimal untuk 5 (boleh diikuti kata `baris`).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, kata (`benar`, `true`), atau angka lain pada nilai Boolean → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-OPS, R-TABLE.
