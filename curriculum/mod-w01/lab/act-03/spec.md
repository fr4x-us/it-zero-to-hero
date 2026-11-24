---
activity_id: mod-w01.lab.act-03
component: mod-w01.lab
content_version: "1.0"
variants: [mod-w01.lab.act-03.vA, mod-w01.lab.act-03.vB]
competencies: [comp-w01-unit-01, comp-w01-spec-01, comp-w01-mem-01]
max_points: 40
estimated_minutes: 30
checks_file: checks.yaml
---

# Lab W1 · Aktivitas 3 — Satuan Data dan Kompatibilitas

## Tujuan

1. Mengonversi satuan data dan menghitung kapasitas dengan satuan desimal
   (bawaan).
2. Menjelaskan perbedaan GB (desimal, 1.000) dan GiB (biner, 1.024).
3. Memeriksa kompatibilitas soket, jenis RAM, dan slot.
4. Menghitung kebutuhan daya dan total RAM.

## Prasyarat

Pelajaran 2 §6 dan Pelajaran 4.

## Aturan yang dipakai

- Satuan desimal (bawaan): 1 GB = 1.000 MB; 1 MB = 1.000 KB. Satuan biner
  (KiB, MiB, GiB) memakai 1.024; di aktivitas ini hanya muncul pada c03
  sebagai pilihan penjelasan, tanpa hitungan angka.
- Kebutuhan daya = daya CPU + 100 W (model belajar W1, bukan standar
  pembelian).
- Dari satuan besar ke satuan kecil kalikan 1.000 per tingkat; dari satuan
  kecil ke satuan besar bagi 1.000 per tingkat.

## Data (fixture, sama untuk kedua varian)

| ID | Jenis | Soket | RAM | Slot | Daya |
|---|---|---|---|---|---|
| L-CPU1 | CPU | Soket A | — | — | 95 W |
| L-CPU2 | CPU | Soket B | — | — | 125 W |
| L-MB1 | Motherboard | Soket A | DDR4 | 2 | — |
| L-MB2 | Motherboard | Soket B | DDR5 | 4 | — |

**Contoh terlihat (tidak dinilai):** 2 GB = 2.000 MB.

## Soal

| No. | Varian A | Varian B |
|---|---|---|
| c01 | 7 GB = … MB | 12 GB = … MB |
| c02 | SSD 256 GB untuk video 800 MB per video; berapa video maksimum? | Kartu memori 32 GB untuk lagu 5 MB per lagu; berapa lagu maksimum? |
| c03 | SSD berlabel 512 GB tampil sekitar 477 GiB. Pilih penjelasan (a)–(d) | Flashdisk berlabel 64 GB tampil sekitar 59,6 GiB. Pilih penjelasan (a)–(d) |
| c04 | L-CPU1 kompatibel dengan L-MB1? (Ya/Tidak) | L-CPU2 kompatibel dengan L-MB1? |
| c05 | RAM DDR5 dapat dipasang di L-MB1? | RAM DDR4 dapat dipasang di L-MB1? |
| c06 | 4 keping RAM DDR4 sekaligus di L-MB1? | 2 keping RAM DDR5 sekaligus di L-MB2? |
| c07 | Kebutuhan daya dengan L-CPU1 (W) | Kebutuhan daya dengan L-CPU2 (W) |
| c08 | 3 keping × 4 GB = … GB | 2 keping × 16 GB = … GB |

Pilihan c03 varian A: (a) SSD rusak; (b) sistem operasi menghitung dengan
kelipatan 1.024 (GiB), produsen dengan kelipatan 1.000 (GB); (c) RAM
memakai sebagian SSD secara permanen; (d) produsen salah mencetak label.
Varian B: (a) flashdisk rusak; (b) RAM memakai sebagian flashdisk secara
permanen; (c) sistem operasi menghitung dengan kelipatan 1.024 (GiB),
produsen dengan kelipatan 1.000 (GB); (d) produsen salah mencetak label.

## Yang diserahkan

Delapan jawaban: bilangan bulat (c01, c02, c07, c08), satu huruf (c03),
Ya/Tidak (c04–c06).

## Penilaian

8 pemeriksaan × 5 poin = **40 poin** (setiap pemeriksaan bernilai 0 atau 5;
maksimum 40 tercapai bila semua benar). Jawaban dicocokkan dengan daftar
jawaban diterima setelah spasi tepi dibuang dan huruf diabaikan besar/kecilnya.
Contoh bentuk (angka tidak berkaitan dengan soal): diterima `4000`, `4.000`,
`4000 MB`, `4.000MB`, `150`, `150 W`, `150W`; ditolak `4.00.0`
(pengelompokan salah), `4 000` (spasi di dalam angka), `4000,0` (desimal),
`+150` (tanda), `4 GB` bila yang diminta MB (satuan lain).

## Kasus gagal

Kosong atau bukan angka → 0 untuk pemeriksaan itu; jawaban desimal yang
bukan bilangan bulat → 0; gangguan sistem → evaluasi diulang tanpa attempt
baru.

## Umpan balik

Setelah evaluasi: jawaban benar dan cara hitung untuk setiap pemeriksaan,
dengan gaya seperti contoh terlihat (mis. "2 GB = 2 × 1.000 = 2.000 MB").

## Remedial

Varian lain menurut VA-2; ulangi Pelajaran 2 §6 dan Pelajaran 4 §1;
materi remedial R-UNIT dan R-SPEC.
