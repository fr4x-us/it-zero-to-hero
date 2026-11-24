---
activity_id: mod-w05.lab.act-02
component: mod-w05.lab
content_version: "1.0"
variants: [mod-w05.lab.act-02.vA, mod-w05.lab.act-02.vB]
competencies: [comp-w05-pct-01, comp-w05-round-01, comp-w05-expr-01]
max_points: 40
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W5 · Aktivitas 2 — Persentase, Pembulatan, dan Rata-rata

## Tujuan

Menghitung persentase dari nilai dasar yang benar, persen kenaikan, nilai awal dari persentase, membulatkan sesuai aturan, menghitung rata-rata, dan membulatkan ke atas untuk kebutuhan.

## Prasyarat

Pelajaran 3, Pelajaran 4 §1–§3.

## Asumsi (model modul)

Persen selalu dihitung dari **nilai dasar** yang disebut (nilai awal bila tidak disebut lain). Pembulatan W5: lihat satu angka setelah tempat pembulatan; 5 atau lebih → naik, kurang dari 5 → tetap (hanya bilangan positif). Jumlah benda/orang/wadah adalah bilangan bulat. Bilangan ditulis menurut **aturan angka NB-5** (Pelajaran 3 §1): koma untuk desimal (`12,5`); titik hanya pemisah ribuan berkelompok tiga digit (`1.250`); tanpa nol di depan; tanda minus untuk bilangan negatif; satuan yang disebut di soal boleh ditulis di belakang angka (mis. `menit`, `%`, `Rp` di depan rupiah).

**Contoh terlihat (0 poin): 50% dari 18 = 9; 2,34 dibulatkan ke satu desimal = 2,3**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | Berapa **15%** dari **260**? | Berapa **35%** dari **140**? |
| 02 | Harga **Rp75.000** diskon **20%**. Harga setelah diskon (rupiah)? | Harga **Rp84.000** diskon **25%**. Harga setelah diskon (rupiah)? |
| 03 | Nilai naik dari **50** menjadi **65**. Persen kenaikan terhadap nilai awal? | Harga naik dari **Rp40.000** menjadi **Rp46.000**. Persen kenaikan terhadap harga awal? |
| 04 | **Rp96.000** adalah **80%** dari harga awal. Berapa harga awal (rupiah)? | **Rp54.000** adalah **90%** dari harga awal. Berapa harga awal (rupiah)? |
| 05 | Bulatkan **18,75** ke **satu** angka di belakang koma. | Bulatkan **24,35** ke **satu** angka di belakang koma. |
| 06 | Bulatkan **6,449** ke **satu** angka di belakang koma. | Bulatkan **9,849** ke **satu** angka di belakang koma. |
| 07 | Rata-rata **7, 9, 10, 8, 9** (tepat, satu angka di belakang koma)? | Rata-rata **6, 9, 8, 10, 8** (tepat, satu angka di belakang koma)? |
| 08 | **73 peserta** duduk di meja berisi paling banyak **6 orang**. Meja paling sedikit? | **95 peserta** naik bus berisi paling banyak **40 orang**. Bus paling sedikit? |

## Yang diserahkan

Bilangan untuk 1–8, dengan jumlah angka desimal tepat seperti yang diminta.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c08 | 5 poin per jawaban benar | 8 × 5 = 40 |
| **Maksimum aktivitas** | | **40** |

## Kasus gagal

Kosong, titik sebagai desimal (`3.5`), jumlah angka desimal berbeda (`3,50`), kata (`dua ribu`), atau bentuk rupiah yang tidak sesuai NB-5 (`12,000`) → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-PCT, R-ROUND, R-EXPR.
