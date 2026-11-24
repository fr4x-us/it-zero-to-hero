---
module_id: mod-w01
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24"
---

# W1 — Review Kualitas, Skenario Penilaian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai | Arti |
|---|---|---|
| Dokumentasi diproduksi | **YA** | Semua bagian TPL-01–TPL-18 terisi dengan konten nyata |
| Dokumentasi direview | **Review mandiri penyusun** | §3–§6; belum direview ChatGPT |
| Diterima owner | **TIDAK** | Menunggu review ChatGPT dan otorisasi eksplisit owner |
| Runtime diverifikasi | **Tidak berlaku / tidak diklaim** | W1 tidak memakai runtime Python; aplikasi belum ada; tidak ada pemeriksaan otomatis yang dijalankan sebagai prototipe aplikasi |
| Durasi diuji dengan pelajar | **TIDAK** | Estimasi durasi belum divalidasi dengan pelajar nyata |

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah | Berkas |
|---|---|---|
| Pelajaran | 4 (180 menit) | `lessons/les-01.md`–`les-04.md` |
| Set latihan tidak dinilai | 4 | Di dalam pelajaran (`prac-01`–`prac-04`) |
| Slot ujian teori | 20 | `theory/blueprint.yaml` |
| Soal teori (2 varian per slot) | **40** | `theory/items/s01.yaml`–`s20.yaml` |
| Aktivitas lab | 3 | `lab/act-01`–`act-03` |
| Spesifikasi lab (2 varian per aktivitas) | **6** | `lab/*/spec.md`, `checks.yaml` |
| Mini-project | **1** | `project/spec.md`, `rubric.yaml` |
| Slot penjelasan konsep | 6 | `concept/items/s01.yaml`–`s06.yaml` |
| Soal penjelasan konsep | **12** | idem |
| Materi remedial | 6 bagian (per LO) | `remedial/remedial.md` |
| Refleksi tanpa skor (CE-D) | 1 | `module.yaml` → `unscored_reflection` |

Pemeriksaan konsistensi dokumen (skrip pemeriksa di luar repositori, membaca
YAML konten; bukan prototipe aplikasi): 212 ID unik, 0 duplikat; setiap kunci
pilihan ada di daftar opsi; setiap urutan diterima memuat semua item; setiap
pemetaan pencocokan satu-ke-satu; P soal CE-S5 genap; jumlah poin setiap
varian sama dengan maksimum komponen.

## 3. Penilaian dan aritmetika

### 3.1 Maksimum poin per komponen

| Komponen | Bobot | Maks. poin | Komposisi | Ambang komponen (`4·e ≥ 3·m`) |
|---|---|---|---|---|
| Theory | 30% | 56 | 8 × 2 + 8 × 3 + 4 × 4 | e ≥ 42 (4·42 = 168 = 3·56) |
| Laboratory | 40% | 100 | act-01 30 + act-02 30 + act-03 40 | e ≥ 75 |
| Mini-project | 20% | 100 | K1 60 + K2 20 + K3 10 + K4 10 | e ≥ 75 |
| Concept | 10% | 21 | 4 + 2 + 4 + 4 + 4 + 3 | e ≥ 16 (4·16 = 64 ≥ 63; 4·15 = 60 < 63) |

Kedua varian setiap slot/aktivitas memiliki format, kesulitan, kompetensi,
dan poin maksimum yang sama (diperiksa: teori 56/56, concept 21/21, lab
100/100).

### 3.2 Durasi ujian teori dihitung dari komposisi akhir

| Langkah | Nilai |
|---|---|
| Komposisi | TF-1 × 10 (7 D1, 1 D2, 2 D3) · TF-2 × 2 (D2) · TF-3 × 3 (D1, D2, D3) · TF-4 × 3 (2 D2, 1 D3) · TF-5 × 2 (D2) |
| D1/D2/D3 | 8 / 8 / 4 |
| Waktu dasar | 10·45 + 2·75 + 3·60 + 3·90 + 2·75 = 450 + 150 + 180 + 270 + 150 = 1.200 |
| Tambahan kesulitan | 8·30 + 4·60 = 480 |
| `S` | 1.680 detik |
| `S_buffer = ⌈1.680 × 11/10⌉` | 1.848 |
| `⌈1.848/60⌉ + 2` | ⌈30,8⌉ + 2 = **33 menit** (10 ≤ 33 ≤ 45) |
| Review umpan balik terjadwal | 45 − 33 = **12 menit** |
| Aksesibilitas TA-B | ⌈33 × 3/2⌉ = **50 menit** (tambahan 17 menit di luar nominal) |

### 3.3 Skenario kelulusan (NP-4, perbandingan pecahan eksak)

Rumus: `W = 30·T/56 + 40·L/100 + 20·P/100 + 10·C/21` (persen). Bentuk bulat
dengan penyebut 420: `420·W = 225·T + 168·L + 84·P + 200·C`; lulus bobot bila
`225·T + 168·L + 84·P + 200·C ≥ 33.600`.

| ID | T/56 | L/100 | P/100 | C/21 | `420·W` | W eksak | Komponen | Hasil |
|---|---|---|---|---|---|---|---|---|
| SC-1 Semua lulus | 48 | 85 | 80 | 18 | 35.400 | 590/7 = 84,2857… | Semua ≥ 75 | **PASSED** |
| SC-2 Semua ≥ 75, W < 80 | 42 | 75 | 80 | 16 | 31.970 | 3.197/42 = 76,1190… | Semua ≥ 75 | **NOT_PASSED** (W) |
| SC-3 W ≥ 80, satu < 75 | 56 | 90 | 95 | 15 | 38.700 | 645/7 = 92,1428… | C: 4·15 = 60 < 63 | **NOT_PASSED** (C) |
| SC-4 Tepat ambang komponen | 42 | 84 | 84 | 18 | 34.218 | 5.703/70 = 81,4714… | T tepat 75 (168 = 168) | **PASSED** |
| SC-5 W tepat 80 | 28 | 88 | 99 | 21 | 33.600 | 80 | T: 4·28 = 112 < 168 | **NOT_PASSED** (T) |
| SC-6 Tepat di bawah 80 | 47 | 75 | 86 | 16 | 33.599 | 33.599/420 = 79,9976… | Semua ≥ 75 | **NOT_PASSED**; tampilan dibulatkan ke bawah "79,99" |

Catatan SC-5: dengan maksimum 56/100/100/21, kombinasi bilangan bulat yang
memberi W tepat 80 **selalu** memiliki komponen < 75 (diperiksa menyeluruh:
208 kombinasi, semuanya gagal komponen). Jadi di W1 "tepat 80 dan lulus"
tidak dapat terjadi; SC-6 menunjukkan mengapa pembulatan tidak boleh dipakai
untuk keputusan.

### 3.4 Remedial, seri, XP, gangguan sistem

| ID | Riwayat | Hasil |
|---|---|---|
| SC-7 Remedial | Lab attempt 1 = 70 (varian A); attempt 2 = 85 (varian B, VA-2) | Skor terbaik 85; kedua attempt tersimpan |
| SC-8 Seri | Theory attempt 1 = 48/56 (vA), attempt 2 = 48/56 (vB) | Skor terbaik 48 dari **attempt 1** (paling awal, D-12) |
| SC-9 XP pertama saat remedial | Theory 40/56 (4·40 = 160 < 168) → tanpa XP; attempt 2 = 44/56 (176 ≥ 168) → **50 XP** (`mod-w01.theory`, XE-2); attempt 3 = 50/56 → tanpa XP | Tepat satu award |
| SC-10 Tanpa XP ganda | Setelah award, attempt varian lain atau perbaikan setelah lulus (PI-A) | Tidak ada award; `xp_id` sudah ada (XL-1) |
| SC-11 Restore dengan ledger rusak | Backup memuat dua entri `mod-w01.theory` | XV-1 → restore ditolak (RX-A, D-29); data aktif tetap |
| SC-12 Gangguan evaluasi lab | Proses aplikasi dihentikan sistem saat act-02 dievaluasi | `EVALUATION_ERROR`; evaluasi diulang dari submission yang sama; tanpa attempt baru dan tanpa penalti (D-24 IE-2) |
| SC-13 Penyimpanan gagal saat ujian | Tulis jawaban s07 gagal karena penyimpanan penuh | Status "Gagal menyimpan"; attempt ditandai `PERSISTENCE_FAILURE`; dinilai dengan jawaban tersimpan (SF-A, D-26) |

### 3.5 XP W1

`4·5 + 4·10 + 50 + 70 + 50 + 25 + 50 = 305` XP. 13 `xp_id` unik; aktivitas
lab individual, varian, latihan lab, dan refleksi bukan identitas XP.

## 4. Checklist kualitas (TPL-19) — hasil review mandiri

| ID | Pemeriksaan | Hasil | Catatan |
|---|---|---|---|
| CQ-01 | Kebenaran teknis | Lulus | Fakta dicek terhadap pengetahuan umum yang mapan; angka GiB dihitung (512 GB ≈ 476,8 GiB; 64 GB ≈ 59,6 GiB; 1 TB ≈ 931,3 GiB). Aturan daya ditandai sebagai penyederhanaan belajar |
| CQ-02 | Ramah pemula | Lulus | Analogi (dapur/resep, meja/lemari, juru masak, restoran), contoh terbimbing, miskonsepsi |
| CQ-03 | Tujuan belajar terukur | Lulus | LO1–LO6 dengan kata kerja terukur |
| CQ-04 | Prasyarat | Lulus | Tidak memakai Python, SQL, HTML/CSS, Git; biner hanya sebagai satuan (W6 dirujuk); OS hanya sebagai kategori (W2 dirujuk) |
| CQ-05 | Cakupan kompetensi | Lulus | Setiap LO: pelajaran, latihan, teori, mini-project, concept. Lab untuk LO1, LO3 (act-03.c08), LO4, LO5 (act-02.c06), LO6; LO2 (core/GHz) tidak punya pemeriksaan lab yang bermakna di W1 — dinilai di teori, proyek (K1.c03, K4.q5), dan concept |
| CQ-06 | Tidak menilai yang belum diajarkan | Lulus | Setiap soal dipetakan ke bagian pelajaran |
| CQ-07 | Kelengkapan bank soal | Lulus | 40 teori, 12 concept, 6 lab, 1 proyek |
| CQ-08 | Kesetaraan varian | Lulus | Format, kesulitan, poin, dan kompetensi sama; isi berbeda |
| CQ-09 | Kunci benar dan tidak ambigu | Lulus dengan catatan | s05 vB memakai "kemungkinan paling cepat" dan syarat generasi sama, karena kecepatan nyata dipengaruhi faktor lain |
| CQ-10 | Aritmetika skor | Lulus | §3 |
| CQ-11 | Fixture lab dan hasil deterministik | Lulus | Jawaban tunggal per pemeriksaan; aturan normalisasi tertulis |
| CQ-12 | Rubrik proyek objektif | Lulus | Semua pemeriksaan berbasis isian; 46 kombinasi valid diterima (bukan satu jawaban) |
| CQ-13 | Penilaian concept | Lulus | D-23 CE-S1–CE-S5, CE-V1–CE-V7 |
| CQ-14 | XP unik | Lulus | §3.5 |
| CQ-15 | Metadata aksesibilitas | Lulus | Setiap diagram punya `alt` + deskripsi panjang; tabel inti punya deskripsi; istilah Inggris ditandai |
| CQ-16 | Versi konten | Lulus | `content_version` 1.0 di semua berkas; `item_version` per soal |
| CQ-17 | Alokasi 8 jam | Lulus | 180 + 45 + 90 + 90 + 30 + 45 = 480 menit |
| CQ-18 | Dapat dipakai offline | Lulus | Tidak ada tautan eksternal; tidak ada video wajib |
| CQ-19 | Konsistensi D-01–D-35 | Lulus | Bobot, ambang, varian, XP, rubrik MR-A, FB-A |
| CQ-20 | Kunci tidak tampil sebelum tahap umpan balik | Lulus | Kunci hanya di berkas YAML; pelajaran hanya memuat pembahasan latihan tidak dinilai |

Temuan yang diperbaiki selama review: (1) contoh soal teori s11 dan lab
act-03 semula sama-sama "3 GB" → lab diganti 7 GB/12 GB agar tidak berbagi
soal; (2) concept s03 dan teori s17 semula sama-sama urutan boot/cetak →
concept memakai boot dan membuka aplikasi, teori memakai lapisan cetak dan
musik; (3) tujuh kompetensi awal digabung menjadi enam LO agar setiap LO
punya soal concept; (4) urutan tampilan soal pengurutan dipisahkan dari teks
soal (`display_order`).

## 5. Batas penilaian objektif (wajib dibaca bersama hasil)

| Yang dibuktikan pemeriksaan | Yang **tidak** dibuktikan |
|---|---|
| Jawaban yang diserahkan sesuai kunci atau memenuhi aturan | Bahwa pelajar memahami semua alasannya (bisa menebak pilihan) |
| Rakitan memenuhi syarat dan perhitungan benar | Bahwa pelajar memakai cara berpikir tertentu untuk menemukannya |
| Kemampuan pada versi soal yang dikerjakan | Kompetensi tersertifikasi secara independen; hasil adalah catatan belajar mandiri (D-17, D-34) |

Pada modul pemrograman kelak, test yang lulus membuktikan **perilaku** yang
teramati pada input yang diuji, bukan pemakaian konstruksi atau algoritma
tertentu, dan bukan pemahaman penuh.

## 6. Bukti reviewer (TPL-20)

| Field | Isi |
|---|---|
| Reviewer | Claude (penyusun), review mandiri |
| Tanggal | 2026-11-24 |
| Basis | `main` = `40ca205` (merge PR #24) |
| Hasil | CQ-01–CQ-20 lulus (CQ-09 dengan catatan) |
| Review berikutnya | ChatGPT (PR), lalu penerimaan owner |
| Diterima owner | Belum |
