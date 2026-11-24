---
module_id: mod-w01
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24; direvisi setelah review PR #25 (F-01–F-08)"
---

# W1 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai | Arti |
|---|---|---|
| Dokumentasi diproduksi | **YA** | Semua bagian TPL-01–TPL-18 berisi konten nyata |
| Review mandiri penyusun | **YA, direvisi** | §4–§7 (setelah temuan ChatGPT PR #25) |
| Review ChatGPT | **Belum lolos** | Putaran pertama REQUEST CHANGES; revisi ini menunggu review ulang |
| Diterima owner | **TIDAK** | Menunggu review dan otorisasi owner (W01-ACC) |
| Runtime diverifikasi | **Tidak berlaku / tidak diklaim** | W1 tanpa runtime Python; aplikasi belum ada |
| Durasi diuji dengan pelajar | **TIDAK** | Estimasi belum divalidasi dengan pelajar nyata |

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah | Berkas |
|---|---|---|
| Pelajaran / set latihan | 4 / 4 (180 menit) | `lessons/les-01.md`–`les-04.md` |
| Soal teori | **40** (20 slot × 2) | `theory/items/s01.yaml`–`s20.yaml` |
| Spesifikasi lab | **6** (3 aktivitas × 2) | `lab/act-01`–`act-03` |
| Mini-project | **1** | `project/spec.md`, `project/rubric.yaml` |
| Soal concept | **12** (6 slot × 2) | `concept/items/s01.yaml`–`s06.yaml` |
| Materi remedial | 6 bagian (per LO) | `remedial/remedial.md` |

Pemeriksa dokumen (skrip di luar repositori; membaca YAML konten; bukan
prototipe aplikasi): ID unik tanpa duplikat; kunci ada di opsi; urutan
diterima memuat semua item; pemetaan satu-ke-satu; P CE-S5 genap; poin varian
= maksimum komponen.

## 3. Aritmetika yang dihitung ulang

| Hal | Hasil |
|---|---|
| Teori: komposisi | TF-1 × 10 (7 D1, 1 D2, 2 D3) · TF-2 × 2 (D2) · TF-3 × 3 (D1, D2, D3) · TF-4 × 3 (2 D2, 1 D3) · TF-5 × 2 (D2); D1/D2/D3 = 8/8/4 |
| Teori: durasi | Dasar 1.200 + tambahan 480 = `S` 1.680 → ⌈1.848⌉ → ⌈30,8⌉ + 2 = **33 menit**; review terjadwal 12 menit; TA-B ⌈49,5⌉ = 50 menit (di luar nominal) |
| Teori: maks. | 8·2 + 8·3 + 4·4 = **56** (kedua varian) |
| Lab: maks. | 30 + 30 + 40 = **100** (kedua varian setiap aktivitas) |
| Proyek: maks. | K1 60 + K2 20 + K3 10 + K4 10 = **100** |
| Concept: maks. | 4 + 2 + 4 + 4 + 4 + 3 = **21** (kedua varian) |
| Ambang komponen | Teori e ≥ 42 (168 = 168); concept e ≥ 16 (64 ≥ 63; 60 < 63); lab/proyek e ≥ 75 |
| Katalog proyek | 3.840 kombinasi; **46** rakitan memenuhi semua syarat (tidak berubah oleh revisi rubrik; rubrik tidak mengubah syarat) |
| XP W1 | 4·5 + 4·10 + 50 + 70 + 50 + 25 + 50 = **305** (13 `xp_id`) |
| Jadwal | 180 + 45 + 90 + 90 + 30 + 45 = **480 menit** |

### 3.1 Skenario kelulusan (NP-4; `420·W = 225·T + 168·L + 84·P + 200·C`; lulus bobot bila ≥ 33.600)

| ID | T/56 | L/100 | P/100 | C/21 | `420·W` | W eksak | Hasil |
|---|---|---|---|---|---|---|---|
| SC-1 | 48 | 85 | 80 | 18 | 10.800 + 14.280 + 6.720 + 3.600 = 35.400 | 84,2857… | PASSED |
| SC-2 | 42 | 75 | 80 | 16 | 9.450 + 12.600 + 6.720 + 3.200 = 31.970 | 76,1190… | NOT_PASSED (W) |
| SC-3 | 56 | 90 | 95 | 15 | 12.600 + 15.120 + 7.980 + 3.000 = 38.700 | 92,1428… | NOT_PASSED (C: 60 < 63) |
| SC-4 | 42 | 84 | 84 | 18 | 9.450 + 14.112 + 7.056 + 3.600 = 34.218 | 81,4714… | PASSED (T tepat 75) |
| SC-5 | 28 | 88 | 99 | 21 | 6.300 + 14.784 + 8.316 + 4.200 = 33.600 | 80 tepat | NOT_PASSED (T: 112 < 168) |
| SC-6 | 47 | 75 | 86 | 16 | 10.575 + 12.600 + 7.224 + 3.200 = 33.599 | 79,9976… (tampil "79,99") | NOT_PASSED |

Pemeriksaan menyeluruh: 208 kombinasi bilangan bulat memberi W tepat 80;
semuanya memiliki komponen < 75. SC-7–SC-13 (remedial, seri, XP pertama
saat remedial, tanpa XP ganda, restore ledger rusak, gangguan evaluasi,
penyimpanan gagal) tidak terpengaruh revisi dan tetap berlaku seperti
dicatat di versi sebelumnya:

| ID | Riwayat | Hasil |
|---|---|---|
| SC-7 | Lab 70 (vA) lalu 85 (vB) | Skor terbaik 85; dua attempt tersimpan |
| SC-8 | Teori 48/56 (vA) lalu 48/56 (vB) | Terbaik dari attempt 1 (paling awal, D-12) |
| SC-9 | Teori 40 → 44 → 50 | XP 50 sekali pada attempt 2 (176 ≥ 168), tidak pada attempt 3 |
| SC-10 | Attempt varian lain setelah award | Tanpa XP (XL-1) |
| SC-11 | Backup dengan dua entri `mod-w01.theory` | XV-1 → restore ditolak (RX-A) |
| SC-12 | Proses dihentikan saat act-02 dievaluasi | `EVALUATION_ERROR`, evaluasi ulang tanpa attempt baru |
| SC-13 | Tulis jawaban gagal saat ujian | `PERSISTENCE_FAILURE`, SF-A |

## 4. Posisi kunci jawaban (F-03)

Kebijakan: **urutan opsi tetap** seperti ditulis penyusun (tanpa
pengacakan), karena pengacakan adalah kebijakan penilaian baru yang belum
disetujui owner dan mengubah pengalaman aksesibilitas (urutan baca yang dapat
diprediksi pembaca layar). Opsi kategori dan baris tabel memakai urutan
alami. ID opsi (`a`–`e`) = posisi tampilan; kunci memakai ID yang sama.

| Bank | Distribusi kunci (sesudah) | Sebelum |
|---|---|---|
| Teori pilihan tunggal (TF-1, TF-4; 26 butir) | a 6 · b 6 · c 7 · d 7 | a 11 · b 10 · c 5 · d 0 |
| Teori pilihan ganda (TF-2; 4 butir, 3 dari 5 benar) | {a,c,e}, {b,c,d}, {b,d,e}, {a,c,d} | {a,b,d} × 2, {a,b,e}, {a,b,d} |
| Teori urutan (TF-5) | Urutan tampil ≠ urutan benar di 4 butir | Sama |
| Concept CE-S1 / CE-S5 | b, d / c, b | a, a / a, a |
| Concept CE-S2 | {b,d}, {a,c}, {a,c,e}, {b,c,d} | {a,b} × 2, {a,b,c} × 2 |
| Proyek K4 | c, a, d, b, c | a × 5 |
| Lab pilihan (act-02 c06; act-03 c03) | d, c; b, c | b, b; a, a |

Pengecoh yang kurang masuk akal diganti dengan miskonsepsi nyata (mis.
"memori kerja sementara yang dipakai CPU", "fungsi motherboard: memasok
listrik", "agar CPU dan motherboard dapat dibeli dari toko yang sama").

## 5. Matriks kesetaraan varian (F-04)

Poin yang sama **bukan** bukti kesetaraan; setiap pasangan diperiksa pada
kompetensi, konsep wajib, tuntutan kognitif, format, poin, dan waktu.

| Slot | Kompetensi | Konsep wajib | Tuntutan kognitif | Format | Kesulitan | Maks. | Waktu (dtk) | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|---|
| theory.s01 | comp-w01-ipos-01 | hardware vs software | Mengingat/mengenali | TF-1 | D1 | 2 | 45 | Keduanya memilih satu benda dari kategori yang diminta di antara 3 contoh kategori lain |
| theory.s02 | comp-w01-ipos-01 | tahap IPOS | Memahami | TF-1 | D1 | 2 | 45 | Keduanya memetakan satu tindakan ke satu tahap dengan opsi yang sama |
| theory.s03 | comp-w01-ipos-01 | urutan IPOS dalam skenario baru | Menerapkan | TF-5 | D2 | 3 | 105 | Skenario baru (ATM / catatan suara), 4 kejadian, petunjuk "setelah" pada langkah penyimpanan |
| theory.s04 | comp-w01-cpu-01 | peran CPU | Mengingat/memahami | TF-1 | D1 | 2 | 45 | Keduanya menanyakan komponen yang menjalankan instruksi; B memakai konteks kalkulator |
| theory.s05 | comp-w01-cpu-01 | core vs clock untuk jenis pekerjaan | Menganalisis tabel (menerapkan) | TF-4 | D2 | 3 | 120 | Tabel sama; A pekerjaan terbagi → core, B pekerjaan berurutan → clock |
| theory.s06 | comp-w01-cpu-01 | core hanya membantu pekerjaan terbagi | Menganalisis skenario | TF-1 | D3 | 4 | 105 | Skenario sebaliknya (tidak lebih cepat / lebih lancar), penalaran sama |
| theory.s07 | comp-w01-mem-01 | volatil vs non-volatil | Mengingat | TF-1 | D1 | 2 | 45 | A mencari yang volatil, B yang non-volatil; 3 pengecoh dari kelompok sebaliknya |
| theory.s08 | comp-w01-mem-01 | SSD vs HDD (cara kerja, kecepatan, ketahanan, harga, volatilitas) | Memahami | TF-2 | D2 | 3 | 105 | 5 pernyataan, 3 benar, topik sama dari sudut SSD (A) dan HDD (B) |
| theory.s09 | comp-w01-mem-01 | akibat RAM volatil vs penyimpanan non-volatil | Menganalisis skenario | TF-1 | D3 | 4 | 105 | Keduanya: data hanya di RAM hilang, data di penyimpanan tetap |
| theory.s10 | comp-w01-unit-01 | definisi satuan dasar | Mengingat | TF-3 | D1 | 2 | 60 | Satu fakta dari tabel satuan (byte–bit / GB–MB) |
| theory.s11 | comp-w01-unit-01 | konversi GB→MB satu langkah | Menerapkan | TF-3 | D2 | 3 | 90 | Satu perkalian ×1.000 |
| theory.s12 | comp-w01-unit-01 | kapasitas: samakan satuan lalu bagi | Menerapkan (2 langkah) | TF-3 | D3 | 4 | 120 | GB→MB lalu bagi ukuran berkas; hasil bulat |
| theory.s13 | comp-w01-ipos-01 | klasifikasi perangkat | Mengingat | TF-1 | D1 | 2 | 45 | Satu perangkat, opsi kategori sama |
| theory.s14 | comp-w01-ipos-01 | perangkat input dan output | Memahami | TF-1 | D2 | 3 | 75 | Satu perangkat dua arah di antara 3 perangkat satu arah |
| theory.s15 | comp-w01-sw-01 | kategori software dari fungsinya | Memahami | TF-1 | D1 | 2 | 45 | Keduanya menyebut fungsi lalu meminta kategori (OS / driver) |
| theory.s16 | comp-w01-sw-01 | software sistem vs aplikasi | Memahami | TF-2 | D2 | 3 | 105 | 5 opsi, 3 benar, satu kategori diminta |
| theory.s17 | comp-w01-sw-01 | lapisan pengguna→aplikasi→OS→driver→hardware | Menerapkan | TF-5 | D2 | 3 | 105 | 5 lapisan, skenario perangkat berbeda (scanner/speaker) |
| theory.s18 | comp-w01-spec-01 | kompatibilitas soket + jenis RAM | Menerapkan tabel | TF-4 | D2 | 3 | 120 | Tabel sama; A ada satu jawaban, B jawaban "tidak ada"; keduanya memeriksa dua syarat |
| theory.s19 | comp-w01-spec-01 | semua syarat + anggaran | Menganalisis tabel | TF-4 | D3 | 4 | 150 | 4 rakitan, tiap pengecoh gagal satu syarat berbeda |
| theory.s20 | comp-w01-spec-01 | peran komponen dalam rakitan | Mengingat | TF-1 | D1 | 2 | 45 | Fungsi PSU / motherboard dengan 3 pengecoh fungsi komponen lain |

| Slot | Kompetensi | Konsep wajib | Tuntutan kognitif | Format | Maks. | Waktu (menit) | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|
| concept.s01 | comp-w01-mem-01 | RAM volatil; penyimpanan non-volatil; akibat listrik mati | Memahami | CE-S1 | 4 | 5 | Alasan volatil vs alasan non-volatil; 3 pengecoh miskonsepsi |
| concept.s02 | comp-w01-cpu-01 | core; pekerjaan yang dapat dibagi vs berurutan | Memahami | CE-S2 | 2 | 5 | Pekerjaan terbagi vs berurutan pada CPU 8 core; masing-masing 2 dari 4 pernyataan benar |
| concept.s03 | comp-w01-sw-01 | firmware bekerja sebelum sistem operasi; POST; perangkat boot; bootloader memuat ke RAM | Mengingat urutan + memahami | CE-S3 | 4 | 5 | Kedua varian kini memuat firmware, POST, perangkat boot, bootloader, muat ke RAM (B: boot dari flashdisk instalasi). Varian B lama (membuka aplikasi) diganti karena tidak mencakup konsep wajib |
| concept.s04 | comp-w01-ipos-01 | dua tahap IPOS; dua istilah dasar (hardware/software atau data/informasi) | Memahami definisi | CE-S4 | 4 | 5 | Masing-masing 2 tahap IPOS + 2 istilah dasar; 1 pengecoh definisi tetangga |
| concept.s05 | comp-w01-unit-01 | 1 byte = 8 bit; aturan desimal ×1.000; konversi GB–MB | Menganalisis (menemukan kesalahan) | CE-S5 | 4 | 5 | 5 pernyataan satuan, 1 salah faktor ×1.000; 4 opsi perbaikan |
| concept.s06 | comp-w01-spec-01 | soket; jenis RAM dan slot; daya PSU; semua syarat dan anggaran | Memahami | CE-S2 | 3 | 5 | Masing-masing 5 pernyataan, 3 benar tentang kompatibilitas dan syarat |

| Aktivitas lab | Kompetensi | Konsep wajib | Tuntutan kognitif | Format | Maks. | Waktu (menit) | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|
| lab.act-01 | ipos-01 | klasifikasi I/O/IO/S/P | Memahami | 10 klasifikasi | 30 | 30 | Distribusi kategori identik (3 I, 3 O, 1 IO, 2 S, 1 P); perangkat berbeda |
| lab.act-02 | ipos-01, sw-01 | urutan IPOS, label tahap, driver | Menerapkan | urutan + label + pilihan | 30 | 30 | Skenario ponsel berbeda (tiket / foto); keduanya bertanya driver sensor |
| lab.act-03 | unit-01, spec-01, mem-01 | konversi, kapasitas, GB vs GiB, soket/DDR/slot, daya, RAM total | Menerapkan | 8 pemeriksaan | 40 | 30 | Angka berbeda, langkah hitung sama; pola Ya/Tidak berbeda (Y,T,T vs T,Y,Y) dengan tuntutan sama |

Perubahan karena tidak setara: theory s04 vB (dulu satuan GHz → kini peran
CPU), s08 (dulu klasifikasi vs pernyataan SSD → kini SSD vs HDD dari dua
sisi), s09 vB (dulu RAM penuh → kini volatilitas setelah restart), s15 vA
(dulu dari contoh → kini dari fungsi), s20 vB (dulu definisi kompatibel →
kini fungsi motherboard); concept s02 vB (dulu GHz → kini core), s03 vB (dulu
membuka aplikasi → kini boot dari flashdisk), s04 (dulu IPOS vs istilah →
kini campuran setara), s06 (dulu kompatibilitas vs pemilihan → kini
campuran setara).

## 6. Review per butir (F-07)

| Berkas / butir | Diperiksa | Temuan | Status |
|---|---|---|---|
| `lessons/les-01.md` | Kebenaran, analogi, contoh, miskonsepsi, aksesibilitas | Latihan 2 semula hampir sama dengan teori s03 vB (catatan suara) → diganti skenario kode QR. Contoh terbimbing (lembar kerja) tidak lagi sama dengan lab act-02 vA (kini tiket kereta) | Diperbaiki |
| `les-01` contoh terbimbing | IPOS lembar kerja | Benar; 245/3 = 81,666… ditampilkan "81,67" sebagai informasi, bukan nilai akademik | Lulus |
| `lessons/les-02.md` | CPU, RAM, SSD/HDD, satuan, I/O | (1) "RAM penuh → memakai penyimpanan" berlaku untuk laptop/PC; ponsel biasanya menutup aplikasi → ditandai model sederhana. (2) Printer multifungsi ditambahkan sebagai I/O. (3) Latihan 3 semula memakai perangkat lab act-01 vB → diganti perangkat lain | Diperbaiki |
| `les-02` contoh terbimbing satuan | 2 GB, 64 GB ÷ 4 MB, 3,6 GHz | Contoh 64 GB ÷ 4 MB semula sama persis dengan teori s12 vA → soal teori diganti 128 GB ÷ 8 MB | Diperbaiki (di soal) |
| `les-02` GiB | 1 TB ≈ 931 GiB | 10¹² ÷ 2³⁰ = 931,32 | Lulus |
| `lessons/les-03.md` | Jenis software, lapisan, boot | (1) Contoh terbimbing "mencetak" semula sama dengan teori s17 vA → soal diganti pemindai. (2) Latihan 1 semula memakai 3 opsi teori s16 → diganti. (3) Latihan 3 semula sama dengan concept s03 vA (urutan boot) → diganti urutan lapisan video. (4) Pengelompokan utilitas ditandai sebagai konvensi modul | Diperbaiki |
| `lessons/les-04.md` | Kompatibilitas, aturan daya, contoh lengkap | Aturan daya ditandai penyederhanaan. Contoh terbimbing memakai katalog X- yang berbeda dari proyek; total 4.580.000 > 4.500.000 dihitung ulang benar | Lulus |
| Latihan `prac-01`–`prac-04` | Jawaban dan tumpang-tindih | Setelah perbaikan, tidak ada latihan yang sama dengan butir bernilai | Lulus |
| Teori s01–s20 (40 butir) | Kunci, pengecoh, kesetaraan, posisi | Bias posisi kunci diperbaiki (§4); 5 pasangan tidak setara diperbaiki (§5); s05 vB memakai "kemungkinan" + catatan penyederhanaan; s14 "Printer (hanya mencetak)"; s18 vB kini "Tidak ada" sebagai jawaban sah | Diperbaiki |
| Concept s01–s06 (12 butir) | D-23 CE-S1–S5, kesetaraan, posisi | s03 vB tidak mencakup konsep wajib → diganti; s02, s04, s06 diselaraskan; posisi kunci disebar | Diperbaiki |
| `lab/act-01` | Fixture, kategori | "Printer" ambigu (multifungsi) → "Printer (hanya mencetak)"; distribusi kategori sama | Diperbaiki |
| `lab/act-02` | Skenario, adjacency, driver | vA semula sama dengan contoh pelajaran 1 → tiket kereta; kunci lapisan disebar | Diperbaiki |
| `lab/act-03` | Angka, GiB | 512 GB ≈ 476,84 GiB ("sekitar 477"), 64 GB ≈ 59,60 GiB; 256.000 ÷ 800 = 320; 32.000 ÷ 5 = 6.400; kunci c03 disebar | Lulus setelah perbaikan posisi |
| `project/spec.md` | Jawaban tidak bocor | Semula menampilkan rakitan lengkap yang benar dan daftar jebakan berbasis ID katalog → diganti contoh bentuk dari katalog Pelajaran 4 dan kesalahan umum tanpa ID katalog; contoh nyata dipindah ke `rubric.yaml` | Diperbaiki |
| `project/rubric.yaml` | Poin, F8, ketergantungan | F8 semula tanpa pemeriksaan kebenaran → K1.c10; aturan jumlah keping, ID, angka; konfigurasi mustahil; contoh E01–E16 dihitung | Diperbaiki |
| `remedial/remedial.md` | Kebenaran latihan tambahan | 9 GB = 9.000; 128.000 ÷ 4 = 32.000; 65 + 100 = 165 > 150 | Lulus |
| `module.yaml` | Pemetaan LO, XP, jadwal | LO2 tanpa pemeriksaan lab (dicatat jujur); LO4 kini juga K1.c10 | Diperbaiki |
| Umpan balik | D-26 (FB-A setelah GRADED), D-34 | Kunci hanya di YAML; pembahasan latihan tidak dinilai di pelajaran; tidak ada klaim kunci tidak dapat diekstrak | Lulus |
| Aksesibilitas | Diagram, tabel, istilah | Setiap diagram punya `alt` + deskripsi panjang; urutan opsi tetap (§4) | Lulus |

### 6.1 Model sederhana vs aturan umum (ditandai di konten)

| Model sederhana di W1 | Kenyataan yang lebih luas |
|---|---|
| Kebutuhan daya = daya CPU + 100 W | Perhitungan nyata memakai daya semua komponen dan cadangan; aturan ini hanya untuk latihan |
| RAM penuh → memakai penyimpanan | Laptop/PC: memori virtual; ponsel: aplikasi latar belakang ditutup |
| Aturan desimal 1.000 untuk semua satuan | Sebagian sistem operasi memakai kelipatan 1.024 (GiB) |
| Generasi sama → clock lebih tinggi kemungkinan lebih cepat untuk pekerjaan berurutan | Kinerja juga bergantung arsitektur, cache, RAM, penyimpanan |
| Utilitas = software sistem | Sebagian buku memisahkannya sebagai kelompok sendiri |

## 7. Batas penilaian objektif

| Yang dibuktikan pemeriksaan | Yang **tidak** dibuktikan |
|---|---|
| Jawaban sesuai kunci / isian memenuhi aturan | Pemahaman penuh (dapat menebak) |
| Rakitan memenuhi syarat dan hitungan benar | Cara berpikir yang dipakai pelajar |
| Hasil pada versi soal yang dikerjakan | Kompetensi tersertifikasi independen (D-17, D-34) |

## 8. Bukti reviewer (TPL-20)

| Field | Isi |
|---|---|
| Reviewer | Claude (penyusun), review mandiri, direvisi setelah temuan ChatGPT F-01–F-08 |
| Tanggal | 2026-11-24 |
| Basis | `main` = `40ca205` (merge PR #24) |
| Hasil | Temuan dan perbaikan tercatat per berkas di §6 (11 baris berstatus Diperbaiki); tidak ada temuan terbuka yang diketahui penyusun |
| Review berikutnya | ChatGPT (ulang), lalu penerimaan owner |
| Diterima owner | Belum |
