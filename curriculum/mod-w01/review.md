---
module_id: mod-w01
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24; direvisi setelah review PR #25 putaran 1 (F-01–F-08) dan putaran 2 (F-09–F-18)"
---

# W1 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** |
| Review mandiri penyusun | **YA**, direvisi dua kali setelah temuan ChatGPT |
| Review ChatGPT | **Belum lolos** (putaran 2: REQUEST CHANGES; revisi ini menunggu review ulang) |
| Diterima owner (W01-ACC) | **TIDAK** |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim (W1 tanpa runtime; aplikasi belum ada) |
| Durasi diuji dengan pelajar | **TIDAK** |

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah |
|---|---|
| Pelajaran / set latihan | 4 / 4 (180 menit) |
| Soal teori | **40** (20 slot × 2) |
| Spesifikasi lab | **6** (3 aktivitas × 2) |
| Mini-project | **1** |
| Soal concept | **12** (6 slot × 2) |
| Materi remedial | 6 bagian |

Pemeriksa dokumen (skrip di luar repositori; membaca YAML konten; bukan
prototipe aplikasi): 213 ID unik; kunci ada di opsi; urutan diterima memuat
semua item dan berbeda dari urutan tampil; pemetaan satu-ke-satu; P CE-S5
genap; jumlah poin = maksimum; nama field kanonik (CB-0 §3a).

## 3. Skor yang dapat dicapai dan aritmetika

### 3.1 Maksimum yang dinyatakan vs yang dapat dicapai (QC-01)

| Komponen / pemeriksaan | Dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori (setiap varian) | 56 | **56** | Setiap soal semua-atau-tidak dengan kunci tunggal yang sah |
| Lab act-01 | 30 | **30** | 10 perangkat × 3; setiap perangkat punya tepat satu kategori benar |
| Lab act-02 c01 (urutan) | 12 | **12** | 4 poin × 3 pasangan; urutan A→B→C→D memberi 3 pasangan. *Sebelum revisi: 3 poin × 3 = 9 (tidak dapat mencapai 12) — diperbaiki* |
| Lab act-02 | 30 | **30** | 12 + 4 × 3 + 6 |
| Lab act-03 | 40 | **40** | 8 × 5, masing-masing 0 atau 5 |
| **Lab komponen** | 100 | **100** | 30 + 30 + 40 (sebelum revisi: 97) |
| Proyek | 100 | **100** | E01 memenuhi semua pemeriksaan K1–K3 bersamaan + K4 benar |
| Concept (setiap varian) | 21 | **21** | CE-S1 kunci; CE-S2 himpunan kunci; CE-S3 urutan diterima; CE-S4 pemetaan kunci; CE-S5 baris + perbaikan |

Contoh adjacency lab act-02 (urutan diterima A → B → C → D):

| Jawaban | Pasangan benar | Poin |
|---|---|---|
| D, C, B, A | 0 | 0 |
| A, B, D, C | 1 (A→B) | 4 |
| C, D, A, B | 2 (C→D, A→B) | 8 |
| A, B, C, D | 3 | 12 |

### 3.2 Durasi, XP, jadwal

| Hal | Hasil |
|---|---|
| Teori | Komposisi TF-1 × 10 (7 D1, 1 D2, 2 D3), TF-2 × 2 (D2), TF-3 × 3 (D1/D2/D3), TF-4 × 3 (2 D2, 1 D3), TF-5 × 2 (D2): 1.200 + 480 = 1.680 → ⌈1.848⌉ → ⌈30,8⌉ + 2 = **33 menit** + review 12 = 45; TA-B 50 |
| XP W1 | 4·5 + 4·10 + 50 + 70 + 50 + 25 + 50 = **305** |
| Jadwal | 180 + 45 + 90 + 90 + 30 + 45 = **480 menit** |

### 3.3 Katalog proyek (enumerasi lengkap)

3.840 kombinasi → 2.880 (keping ≤ slot) → 720 (soket dan DDR cocok) → 240
(core, RAM, SSD, PSU) → **46** (≤ 6.500.000). Rincian per CPU+motherboard:
CPU-4+MB-3 21, CPU-2+MB-1 16, CPU-4+MB-4 6, CPU-2+MB-2 3. Daftar lengkap
46 rakitan dan 19 contoh evaluasi (E01–E19): `project/rubric.yaml`.

### 3.4 Pemeriksaan ulang semua angka (QC-02, QC-03)

| Tempat | Perhitungan | Hasil |
|---|---|---|
| les-01 contoh | 245 ÷ 3 | 81,666… (tampil 81,67) |
| les-02 konversi | 2 × 1.000; 5.000 ÷ 1.000; 1 × 1.000 × 1.000; 3.000.000 ÷ 1.000 ÷ 1.000 | 2.000 MB; 5 GB; 1.000.000 MB; 3 GB |
| les-02 kapasitas / GiB | 64.000 ÷ 4; 10¹² ÷ 2³⁰ | 16.000; 931,32 |
| les-02 latihan | 3 × 1.000; 500.000 ÷ 2.000 | 3.000; 250 |
| les-04 contoh / latihan | 1.700.000 + 1.200.000 + 680.000 + 640.000 + 360.000; 105 + 100; 4 × 8 | 4.580.000; 205; 32 |
| remedial R-UNIT | 9 × 1.000; 7.000 ÷ 1.000; 2 × 1.000 × 1.000; 5.000.000 ÷ 1.000 ÷ 1.000; 128.000 ÷ 4 | 9.000; 7; 2.000.000; 5; 32.000 |
| teori s10–s12 | 1 byte; 1 GB; 6 × 1.000; 16 × 1.000; 128.000 ÷ 8; 250.000 ÷ 1.000 | 8; 1.000; 6.000; 16.000; 16.000; 250 |
| lab act-03 | 7 × 1.000; 12 × 1.000; 256.000 ÷ 800; 32.000 ÷ 5; 512·10⁹ ÷ 2³⁰; 64·10⁹ ÷ 2³⁰; 95 + 100; 125 + 100; 3 × 4; 2 × 16 | 7.000; 12.000; 320; 6.400; 476,84; 59,60; 195; 225; 12; 32 |
| proyek | contoh bentuk 3.600.000 + 2.000.000 + 4 × 440.000 + 640.000 + 360.000; E01 | 8.360.000; 5.400.000 |

**Kesalahan yang ditemukan dan diperbaiki:** R-UNIT semula menulis "naik
satu tingkat (KB → MB …) = × 1.000", yang membalik arah konversi nilai. Kini
ditulis eksplisit: besar → kecil kalikan, kecil → besar bagi, dengan contoh
dua arah dan dua tingkat. Ringkasan les-02 juga diperjelas.

### 3.5 Skenario kelulusan (NP-4; `420·W = 225·T + 168·L + 84·P + 200·C`)

| ID | T/56 | L/100 | P/100 | C/21 | `420·W` | Hasil |
|---|---|---|---|---|---|---|
| SC-1 | 48 | 85 | 80 | 18 | 35.400 | PASSED |
| SC-2 | 42 | 75 | 80 | 16 | 31.970 | NOT_PASSED (W 76,12…) |
| SC-3 | 56 | 90 | 95 | 15 | 38.700 | NOT_PASSED (C: 60 < 63) |
| SC-4 | 42 | 84 | 84 | 18 | 34.218 | PASSED (T tepat 75) |
| SC-5 | 28 | 88 | 99 | 21 | 33.600 | NOT_PASSED (W tepat 80, T: 112 < 168) |
| SC-6 | 47 | 75 | 86 | 16 | 33.599 | NOT_PASSED (79,9976…, tampil "79,99") |

SC-7–SC-13 (remedial, seri, XP pertama saat remedial, tanpa XP ganda,
restore ledger rusak, gangguan evaluasi, penyimpanan gagal) tidak berubah.

## 4. Posisi kunci jawaban

Urutan opsi tetap (tanpa pengacakan); ID opsi = posisi tampil. Teori
pilihan tunggal a 6 · b 6 · c 7 · d 7; pilihan ganda {a,c,e}, {b,c,d},
{b,d,e}, {a,c,d}; concept CE-S1 b, d; CE-S5 c, b; CE-S2 {b,d}, {a,c},
{a,c,e}, {b,c,d}; K4 c, a, d, b, c; lab act-02 c06 d, c; act-03 c03 b, c.

## 5. Matriks kesetaraan varian (QC-04)

| Slot | Kompetensi | Konsep wajib | Tuntutan kognitif | Format | Kesulitan | Maks. | Waktu (dtk) | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|---|
| theory.s01 | comp-w01-ipos-01 | hardware vs software | Mengingat/mengenali | TF-1 | D1 | 2 | 45 | Keduanya memilih satu benda dari kategori yang diminta di antara 3 contoh kategori lain |
| theory.s02 | comp-w01-ipos-01 | tahap IPOS | Memahami | TF-1 | D1 | 2 | 45 | Keduanya memetakan satu tindakan ke satu tahap dengan opsi yang sama |
| theory.s03 | comp-w01-ipos-01 | urutan IPOS dalam skenario baru | Menerapkan | TF-5 | D2 | 3 | 105 | Skenario baru (ATM / catatan suara), 4 kejadian, petunjuk "setelah"; kedua stem menyebut model IPOS sederhana W1 |
| theory.s04 | comp-w01-cpu-01 | peran CPU | Mengingat/memahami | TF-1 | D1 | 2 | 45 | Keduanya menanyakan komponen yang menjalankan instruksi; B memakai konteks kalkulator |
| theory.s05 | comp-w01-cpu-01 | core vs clock untuk jenis pekerjaan | Menganalisis tabel (menerapkan) | TF-4 | D2 | 3 | 120 | Tabel sama; kedua stem menyatakan asumsi model (generasi, arsitektur, komponen lain sama) dan bahwa core/clock saja tidak menentukan peringkat kinerja nyata; A pekerjaan terbagi → core, B berurutan → clock |
| theory.s06 | comp-w01-cpu-01 | core hanya membantu pekerjaan terbagi | Menganalisis skenario | TF-1 | D3 | 4 | 105 | Skenario sebaliknya (tidak lebih cepat / lebih lancar), penalaran sama |
| theory.s07 | comp-w01-mem-01 | volatil vs non-volatil | Mengingat | TF-1 | D1 | 2 | 45 | A mencari yang volatil (pengecoh: SSD, HDD, flashdisk), B yang non-volatil (pengecoh: RAM, CPU, PSU — tanpa pengecoh ganda bermakna RAM) |
| theory.s08 | comp-w01-mem-01 | SSD vs HDD (cara kerja, kecepatan, ketahanan, harga, volatilitas) | Memahami | TF-2 | D2 | 3 | 105 | 5 pernyataan, 3 benar, topik sama dari sudut SSD (A) dan HDD (B) |
| theory.s09 | comp-w01-mem-01 | akibat RAM volatil vs penyimpanan non-volatil | Menganalisis skenario | TF-1 | D3 | 4 | 105 | Kedua stem menetapkan asumsi eksplisit: A — tidak pernah disimpan dan tanpa simpan otomatis/pemulihan; B — daftar tab hanya disimpan di RAM. Penalaran: yang hanya di RAM hilang, yang di penyimpanan tetap |
| theory.s10 | comp-w01-unit-01 | definisi satuan dasar | Mengingat | TF-3 | D1 | 2 | 60 | Satu fakta dari tabel satuan (byte–bit / GB–MB) |
| theory.s11 | comp-w01-unit-01 | konversi GB→MB satu langkah | Menerapkan | TF-3 | D2 | 3 | 90 | Satu perkalian ×1.000 |
| theory.s12 | comp-w01-unit-01 | kapasitas: samakan satuan lalu bagi | Menerapkan (2 langkah) | TF-3 | D3 | 4 | 120 | GB→MB lalu bagi ukuran berkas; hasil bulat |
| theory.s13 | comp-w01-ipos-01 | klasifikasi perangkat | Mengingat | TF-1 | D1 | 2 | 45 | Satu perangkat, opsi kategori sama |
| theory.s14 | comp-w01-ipos-01 | perangkat input dan output | Memahami | TF-1 | D2 | 3 | 75 | Satu perangkat dua arah di antara 3 perangkat satu arah |
| theory.s15 | comp-w01-sw-01 | kategori software dari fungsinya | Memahami | TF-1 | D1 | 2 | 45 | Keduanya menyebut fungsi lalu meminta kategori (OS / driver) |
| theory.s16 | comp-w01-sw-01 | software sistem vs aplikasi | Memahami | TF-2 | D2 | 3 | 105 | 5 opsi, 3 benar, satu kategori diminta |
| theory.s17 | comp-w01-sw-01 | lapisan pengguna→aplikasi→OS→driver→hardware | Menerapkan | TF-5 | D2 | 3 | 105 | 5 lapisan, skenario perangkat berbeda (scanner/speaker); kedua stem menyebut model lapisan sederhana W1 |
| theory.s18 | comp-w01-spec-01 | kompatibilitas soket + jenis RAM | Menerapkan tabel | TF-4 | D2 | 3 | 120 | Tabel sama; A ada satu jawaban, B jawaban "tidak ada"; keduanya memeriksa dua syarat |
| theory.s19 | comp-w01-spec-01 | semua syarat + anggaran | Menganalisis tabel | TF-4 | D3 | 4 | 150 | 4 rakitan, tiap pengecoh gagal satu syarat berbeda |
| theory.s20 | comp-w01-spec-01 | peran komponen dalam rakitan | Mengingat | TF-1 | D1 | 2 | 45 | Fungsi PSU / motherboard dengan 3 pengecoh fungsi komponen lain |

| Slot | Kompetensi | Konsep wajib | Tuntutan kognitif | Format | Maks. | Waktu (menit) | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|
| concept.s01 | comp-w01-mem-01 | RAM volatil; penyimpanan non-volatil; akibat listrik mati | Memahami | CE-S1 | 4 | 5 | vA: mengapa RAM volatil (kunci: isi hilang saat listrik mati); vB: mengapa SSD tetap menyimpan (kunci: non-volatil). Pengecoh keduanya miskonsepsi kapasitas/kecepatan/penyimpan lain |
| concept.s02 | comp-w01-cpu-01 | core; pekerjaan yang dapat dibagi vs berurutan | Memahami | CE-S2 | 2 | 5 | vA benar: (1) mekanisme — pekerjaan banyak aplikasi dikerjakan bersamaan di core berbeda; (2) syarat — manfaat bergantung pada pekerjaan yang dapat dibagi. vB benar: (1) akibat — program berurutan tidak otomatis lebih cepat; (2) syarat — core hanya membantu pekerjaan yang dapat dibagi. Pengecoh keduanya: core menambah SSD/RAM, program pasti 2× lebih cepat |
| concept.s03 | comp-w01-sw-01 | firmware bekerja sebelum sistem operasi; POST; perangkat boot; bootloader memuat ke RAM | Mengingat urutan + memahami | CE-S3 | 4 | 5 | vA: daya → POST → cari perangkat boot → bootloader memuat OS ke RAM → OS siap. vB: daya → POST → firmware memakai flashdisk yang **sudah dipilih** sebagai perangkat boot → bootloader memuat program instalasi ke RAM → layar instalasi. Konsep wajib (firmware sebelum OS, POST, perangkat boot, bootloader, muat ke RAM) ada di kedua varian; keduanya berlabel "model boot sederhana W1" |
| concept.s04 | comp-w01-ipos-01 | dua tahap IPOS; dua istilah dasar (hardware/software atau data/informasi) | Memahami definisi | CE-S4 | 4 | 5 | vA: Input, Proses, Hardware, Informasi; vB: Output, Penyimpanan, Software, Data — masing-masing 2 tahap IPOS + 2 istilah dasar; pengecoh = definisi istilah pasangan |
| concept.s05 | comp-w01-unit-01 | 1 byte = 8 bit; aturan desimal ×1.000; konversi GB–MB | Menganalisis (menemukan kesalahan) | CE-S5 | 4 | 5 | vA: baris "1 GB = 100 MB"; vB: baris "500 GB = 50.000 MB" — keduanya kesalahan faktor ×1.000 di antara 4 pernyataan benar; 4 opsi perbaikan |
| concept.s06 | comp-w01-spec-01 | soket; jenis RAM; jumlah slot; daya PSU; semua syarat dan anggaran | Memahami | CE-S2 | 3 | 5 | vA benar: soket, jenis RAM, daya PSU; pengecoh: slot, semua-syarat. vB benar: soket, slot, semua-syarat; pengecoh: jenis RAM, daya PSU. Kelima konsep wajib (soket, jenis RAM, slot, daya PSU, syarat+anggaran) muncul di kedua varian |

| Aktivitas lab | Kompetensi | Konsep wajib | Tuntutan | Maks. | Menit | Bukti kesetaraan |
|---|---|---|---|---|---|---|
| act-01 | ipos-01 | klasifikasi I/O/IO/S/P | Menerapkan | 30 | 30 | vA: stylus, monitor, printer (hanya mencetak), pemindai sidik jari, layar sentuh, SSD, CPU, mikrofon, speaker tanpa mikrofon, keping DVD; vB: scanner, proyektor, webcam, headset dengan mikrofon, HDD, GPU, kamera CCTV, earphone tanpa mikrofon, kartu memori SD, printer (hanya mencetak). Distribusi sama (3 I, 3 O, 1 IO, 2 S, 1 P); masing-masing memuat perangkat yang tidak ada di tabel pelajaran (penerapan, bukan hafalan) |
| act-02 | ipos-01, sw-01 | urutan IPOS, label tahap, driver | Menerapkan | 30 | 30 | Skenario ponsel berbeda (tiket / foto); pertanyaan driver sensor (layar sentuh / kamera) |
| act-03 | unit-01, spec-01, mem-01 | konversi, kapasitas, GB vs GiB, soket/DDR/slot, daya, RAM total | Menerapkan | 40 | 30 | Angka berbeda, langkah hitung sama; pola Ya/Tidak berbeda dengan tuntutan sama |

## 6. Review per butir

### 6.1 Temuan putaran 2 (F-09–F-18)

| Temuan | Berkas | Perbaikan |
|---|---|---|
| F-09 maksimum lab tidak dapat dicapai | `lab/act-02/*` | 4 poin per pasangan; nilai dapat dicapai 0/4/8/12 (`reachable_values`); lab komponen kembali dapat mencapai 100 |
| F-10 arah konversi terbalik | `remedial/remedial.md`, `lessons/les-02.md` | Aturan dua arah + contoh dua tingkat |
| F-11 presisi soal teori | `theory/items/s03, s05, s07, s09, s17` | Asumsi model sederhana ditulis di stem; pengecoh s07 vB diganti PSU; s09 menetapkan asumsi penyimpanan secara eksplisit |
| F-12 kesetaraan concept | `concept/items/s02, s06` | s02: pernyataan benar = mekanisme/akibat + syarat; s06: kelima konsep wajib muncul di kedua varian |
| F-13 asumsi boot | `concept/items/s03` | vB: flashdisk **sudah dipilih** sebagai perangkat boot; kedua varian berlabel model sederhana |
| F-14 tumpang-tindih | `lessons/les-01.md` | Contoh memotret (= lab act-02 vB) diganti jam tangan pintar; lab act-03 c07/c08 dan contoh proyek diubah agar tidak sama dengan contoh pelajaran (§6.3) |
| F-15 penyederhanaan teknis | `lessons/les-02–04.md`, `remedial` | Model kompatibilitas W1 vs kenyataan (chipset, firmware, daftar dukungan produsen); daya = model belajar; clock ≠ instruksi per detik; non-volatil ≠ kebal; printer: banyak penyebab |
| F-16 metadata dan angka | `project/rubric.yaml`, lab, teori, CB-0 | `depends_on` satu-satunya; `normalization` dan `accepted_sequences` seragam; aturan angka deterministik dengan contoh diterima/ditolak |
| F-17 perangkat ambigu | `lab/act-01/*`, `theory/items/s14` | "Earphone tanpa mikrofon", "Speaker tanpa mikrofon", "GPU (prosesor grafis)", "Printer (hanya mencetak)" |
| F-18 kriteria CB-0 | `docs/CURRICULUM_TEMPLATES_CB0.md` §3b | QC-01–QC-10 |

### 6.2 Model sederhana vs kenyataan (QC-05)

| Model W1 | Kenyataan |
|---|---|
| Kompatibel = soket, jenis RAM, slot, daya (katalog fiktif) | Juga chipset, versi firmware, daftar kompatibilitas produsen |
| Kebutuhan daya = daya CPU + 100 W | Model latihan; bukan standar membeli PSU |
| Clock = siklus per detik | Instruksi per siklus bergantung rancangan CPU |
| Core/clock pada generasi sama | Kinerja juga bergantung arsitektur, cache, RAM, penyimpanan |
| RAM penuh → memakai penyimpanan | Laptop/PC; ponsel biasanya menutup aplikasi |
| Penyimpanan non-volatil | Tetap dapat rusak/hilang; perlu cadangan |
| Model IPOS, lapisan software, urutan boot | Sistem nyata punya lebih banyak tahap; firmware berbeda antarperangkat |
| Printer tidak terdeteksi → periksa driver | Salah satu kemungkinan penyebab |
| Utilitas = software sistem | Sebagian buku memisahkannya |

### 6.3 Tumpang-tindih contoh vs butir bernilai (QC-06)

| Contoh/latihan | Butir bernilai terdekat | Penilaian |
|---|---|---|
| les-01 jam tangan pintar (IPOS) | teori s03 (ATM, catatan suara), lab act-02 (tiket, foto) | Skenario berbeda — latihan keterampilan sama, bukan duplikasi |
| les-01 latihan kode QR | teori s03 vB (catatan suara) | Berbeda |
| les-02 tabel perangkat | lab act-01 | Lab kini memuat perangkat di luar tabel (stylus, sidik jari, DVD, CCTV, earphone/speaker tanpa mikrofon); sisanya adalah pengetahuan yang memang diajarkan |
| les-02 64 GB ÷ 4 MB; latihan 3 GB, 500 GB ÷ 2.000 MB | teori s11 (6 GB, 16 GB), s12 (128 GB ÷ 8 MB, 250 GB ÷ 1.000 MB); lab act-03 (7 GB, 12 GB, 256 GB ÷ 800 MB, 32 GB ÷ 5 MB) | Angka berbeda |
| les-02 SSD 1 TB ≈ 931 GiB | lab act-03 c03 (512 GB, 64 GB) | Berbeda |
| les-03 mencetak (lapisan) | teori s17 (scanner, speaker) | Berbeda |
| les-03 latihan lapisan video | teori s17 | Berbeda perangkat |
| les-03 urutan boot (materi) | concept s03 vA | Konsep yang diajarkan diuji ulang (wajar); latihan pelajaran tidak lagi memakai urutan boot |
| les-04 daya 65 W → 165; 105 W → 205; X-RAM 2 × 8 = 16; 4 × 8 = 32 | lab act-03 c07 (95 → 195; 125 → 225), c08 (3 × 4 = 12; 2 × 16 = 32) | c07 dan vA c08 kini berbeda dari contoh; vB c08 = 32 sama hasil dengan latihan les-04 tetapi soal berbeda (2 × 16 vs 4 × 8) |
| proyek: contoh bentuk isian | Jawaban proyek | Memakai katalog X- (F7 = 205, tidak mungkin untuk rakitan proyek yang sah); tidak membocorkan jawaban |
| remedial R-UNIT 128 GB ÷ 4 MB | teori s12 vA 128 GB ÷ 8 MB | Angka berbeda; latihan keterampilan sama |

### 6.4 Hasil QC-01–QC-10

| QC | Hasil |
|---|---|
| QC-01 | Lulus setelah perbaikan act-02 (§3.1) |
| QC-02 | Lulus (§3.1, §3.4, rubrik E01–E19 dihitung ulang dengan aturan angka baru) |
| QC-03 | Lulus setelah perbaikan R-UNIT |
| QC-04 | Lulus (§5) |
| QC-05 | Lulus (§6.2) |
| QC-06 | Lulus (§6.3) |
| QC-07 | Lulus: spec.md lab/proyek dicek terhadap YAML (perangkat, angka, poin, opsi, aturan angka) |
| QC-08 | Lulus: `normalization`, aturan angka, `depends_on` |
| QC-09 | Lulus: tidak ada lagi `needs`, `answer_normalization`, `expected_sequence` |
| QC-10 | Lulus: batas anggaran tepat dinyatakan tidak dapat dicapai oleh rakitan sah; batas yang dapat dicapai (E02, E03, E04, E05) didokumentasikan |

### 6.5 Temuan putaran 1 (tetap berlaku)

Bias posisi kunci, varian tidak setara, contoh proyek yang membocorkan
jawaban, F8 tanpa pemeriksaan, tumpang-tindih latihan — semuanya diperbaiki
pada revisi sebelumnya dan tetap dipertahankan.

## 7. Batas penilaian objektif

Pemeriksaan membuktikan jawaban/isian sesuai kunci dan aturan pada versi soal
yang dikerjakan; tidak membuktikan pemahaman penuh, cara berpikir, atau
kompetensi tersertifikasi (D-17, D-34).

## 8. Bukti reviewer

| Field | Isi |
|---|---|
| Reviewer | Claude (penyusun), review mandiri setelah dua putaran temuan ChatGPT |
| Tanggal | 2026-11-24 |
| Basis | `main` = `40ca205` |
| Temuan terbuka yang diketahui | Tidak ada pada konten W1. Keputusan owner terbuka: CU-6-Q13 (D-36 bila disetujui), OD-15-Q2 (D-37 bila disetujui), W01-ACC |
| Diterima owner | Belum |
