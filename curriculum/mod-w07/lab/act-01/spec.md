---
activity_id: mod-w07.lab.act-01
component: mod-w07.lab
content_version: "1.0"
variants: [mod-w07.lab.act-01.vA, mod-w07.lab.act-01.vB]
competencies: [comp-w07-decomp-01, comp-w07-order-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W7 · Aktivitas 1 — Dekomposisi dan Urutan Tugas

## Tujuan

Mengelompokkan tugas ke sub-masalah menurut hasilnya, menyusun urutan yang memenuhi prasyarat, menghitung banyak urutan valid, dan menemukan tugas yang dapat dikerjakan bersamaan.

## Prasyarat

Pelajaran 1.

## Asumsi (model modul)

Kelompok ditentukan oleh **hasil** tugas sesuai arti kode. "X sebelum Y" berarti Y membutuhkan hasil X. Urutan valid = setiap prasyarat terpenuhi; **setiap urutan valid diterima**. Dua tugas dapat dikerjakan bersamaan bila tidak ada yang membutuhkan hasil yang lain (langsung atau lewat tugas lain).

**Contoh terlihat (0 poin): tugas "membeli spidol (hasil: spidol)" untuk proyek lain → kelompok Barang**

## Data (fixture)

**Varian A — Mading kelas**

| Kode kelompok | Arti |
|---|---|
| `K` | Koordinasi — menghasilkan kesepakatan kelompok |
| `I` | Isi — menghasilkan teks atau foto |
| `T` | Tampilan — menghasilkan papan yang tertata |

| Tugas | Isi |
|---|---|
| `M1` | Rapat pembagian tugas (hasil: daftar siapa mengerjakan apa) |
| `M2` | Menulis artikel kegiatan (hasil: teks artikel) |
| `M3` | Memilih foto kegiatan (hasil: 4 foto terpilih) |
| `M4` | Mendesain tata letak papan (hasil: sketsa posisi artikel dan foto) |
| `M5` | Menempel artikel dan foto di papan sesuai sketsa (hasil: mading jadi) |

Prasyarat: M1 sebelum M2; M1 sebelum M3; M2 sebelum M4; M3 sebelum M4; M4 sebelum M5.

**Varian B — Bakti sosial**

| Kode kelompok | Arti |
|---|---|
| `K` | Koordinasi — menghasilkan kesepakatan kelompok |
| `B` | Barang — mengumpulkan atau mengemas barang |
| `P` | Publikasi — menghasilkan pengumuman |

| Tugas | Isi |
|---|---|
| `B1` | Rapat menentukan jenis bantuan (hasil: daftar barang yang diterima) |
| `B2` | Membuat poster pengumuman (hasil: poster) |
| `B3` | Mengumpulkan barang dari siswa (hasil: barang terkumpul) |
| `B4` | Mengemas barang per paket (hasil: paket siap kirim) |
| `B5` | Menyerahkan paket ke panitia (hasil: tanda terima) |

Prasyarat: B1 sebelum B2; B1 sebelum B3; B3 sebelum B4; B4 sebelum B5.

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | Kelompok untuk M2? | Kelompok untuk B2? |
| 02 | Kelompok untuk M4? | Kelompok untuk B4? |
| 03 | Kelompok untuk M1? | Kelompok untuk B1? |
| 04 | Tulis satu urutan M1–M5 yang memenuhi semua prasyarat. | Tulis satu urutan B1–B5 yang memenuhi semua prasyarat. |
| 05 | Berapa banyak urutan M1–M5 yang memenuhi semua prasyarat? | Berapa banyak urutan B1–B5 yang memenuhi semua prasyarat? |
| 06 | Dua tugas mana yang dapat dikerjakan **bersamaan** oleh dua orang berbeda? (a) M1 dan M2, (b) M2 dan M3, (c) M3 dan M4, (d) M4 dan M5 | Dua tugas mana yang dapat dikerjakan **bersamaan** oleh dua orang berbeda? (a) B1 dan B2, (b) B3 dan B4, (c) B2 dan B3, (d) B4 dan B5 |

## Yang diserahkan

Kode untuk 1–3; urutan ID dipisah spasi atau koma untuk 4 (setiap ID tepat sekali); bilangan untuk 5; huruf opsi untuk 6.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, kode di luar daftar, urutan dengan ID hilang/ganda/tak dikenal, atau urutan yang melanggar prasyarat → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-DECOMP, R-ORDER.
