---
module_id: mod-w02
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-1. Belum direview ChatGPT; belum diterima owner"
---

# W2 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-1) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review ChatGPT | **BELUM** |
| Diterima owner | **BELUM** |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim (W2 tanpa runtime; aplikasi belum ada) |
| Durasi diuji dengan pelajar | **TIDAK** |

Acuan struktur: W1 (W01-ACC), dengan batas review independen W1 yang
diungkapkan tetap berlaku ([`../mod-w01/review.md`](../mod-w01/review.md) §11).
Isi W2 tidak menyalin isi W1.

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah |
|---|---|
| Pelajaran / set latihan | 4 / 4 (40 + 40 + 55 + 45 = 180 menit) |
| Soal teori | **40** (20 slot × 2) |
| Soal concept | **12** (6 slot × 2) |
| Spesifikasi lab | **6** (3 aktivitas × 2) |
| Mini-project | **1** (rubrik MR-A, 16 contoh reviewer) |
| Materi remedial | 6 bagian (R-OS, R-PROC, R-FS, R-PATH, R-OPS, R-PERM) |

Pemeriksa dokumen (skrip di luar repositori; membaca YAML/MD konten; bukan
prototipe aplikasi): **186 ID unik**, 0 duplikat; kunci ada di opsi;
`distractor_rationale` mencakup tepat setiap opsi salah; urutan diterima
memuat semua item dan berbeda dari urutan tampil; pemetaan CE-S4
satu-ke-satu; P CE-S5 genap; jumlah poin = maksimum di setiap varian lab
dan kriteria proyek; nama field kanonik (CB-0 §3a); 0 galat.

## 3. Tujuan belajar (6 LO ↔ 6 kompetensi ↔ 6 slot concept)

| LO | Kompetensi | Pelajaran | Teori | Lab | Proyek | Concept |
|---|---|---|---|---|---|---|
| LO1 fungsi OS | `comp-w02-os-01` | les-01 | s01–s03 | — (alasan di `module.yaml`) | K4.q4 | s01 |
| LO2 program/proses | `comp-w02-proc-01` | les-02 | s04–s06 | act-03.c08 | K4.q2 | s02 |
| LO3 berkas/ekstensi/pohon | `comp-w02-fs-01` | les-03 | s07–s10 | act-01 | K1.c01–c10, K4.q1 | s03 |
| LO4 path | `comp-w02-path-01` | les-03 | s11–s14 | act-02, act-03.c01/c05 | K1.c11–c13 | s04 |
| LO5 operasi berkas | `comp-w02-ops-01` | les-04 | s15–s17 | act-03.c01–c05 | K1.c01–c09, c14, K3.c03–c04, K4.q3 | s05 |
| LO6 izin | `comp-w02-perm-01` | les-04 | s18–s20 | act-03.c06–c07 | K4.q5 | s06 |

Sumber LO: topik CUR §2 baris 2 ("fungsi OS, proses, sistem file";
lab "simulasi struktur folder/path") dalam kerangka D-01 M-02. Rumusan rinci
disusun penyusun seperti W1 (CU-1: tujuan rinci per minggu tetap PROPOSED).
Tidak ada materi yang bergantung pada modul berikutnya; W1 (software
sistem, driver, RAM volatil, satuan desimal) menjadi prasyarat.

## 4. Skor yang dapat dicapai dan aritmetika

### 4.1 Maksimum yang dinyatakan vs yang dapat dicapai (QC-01)

| Komponen / pemeriksaan | Dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori (setiap varian) | 56 | **56** | 8 × D1 (2) + 8 × D2 (3) + 4 × D3 (4); setiap soal semua-atau-tidak dengan kunci/jawaban diterima yang sah |
| Lab act-01 | 30 | **30** | 10 × 3; setiap berkas tepat satu kategori benar |
| Lab act-02 | 30 | **30** | 6 × 5; setiap path tepat satu bentuk kanonik (+ awalan `./` untuk relatif) |
| Lab act-03 | 40 | **40** | 8 × 5; keadaan akhir disimulasikan (§4.3) |
| **Lab komponen** | 100 | **100** | 30 + 30 + 40 |
| Proyek | 100 | **100** | E01 (keadaan akhir wajib + jawaban acuan) memenuhi semua pemeriksaan K1–K3 bersamaan + K4 benar (simulasi §4.4) |
| Concept (setiap varian) | 20 | **20** | CE-S4 4 + CE-S1 4 + CE-S2 (k = 3) 3 + CE-S5 4 + CE-S3 (n = 4) 3 + CE-S2 (k = 2) 2 |

Contoh CE-S3 (concept s05 vA, dua urutan diterima ABCD dan ABDC, dinilai
per urutan tanpa digabung): jawaban A, B, D, C → 1 pasangan terhadap ABCD,
3 terhadap ABDC → **3**; jawaban B, A, C, D → 1 terhadap ABCD (C→D), 0
terhadap ABDC → **1**.

### 4.2 Durasi teori, XP, jadwal

| Hal | Hasil |
|---|---|
| Komposisi teori | TF-1 × 9 (6 D1, 1 D2, 2 D3), TF-2 × 2 (D2), TF-3 × 5 (2 D1, 2 D2, 1 D3), TF-4 × 3 (2 D2, 1 D3), TF-5 × 1 (D2) |
| Rumus A.4 | dasar 9·45 + 2·75 + 5·60 + 3·90 + 1·75 = **1.200**; tambahan 8·0 + 8·30 + 4·60 = **480**; S = 1.680 → S_buffer = ⌈1.848⌉ = 1.848 → ⌈30,8⌉ + 2 = **33 menit** |
| Timer teori / review umpan balik | **33** / 45 − 33 = **12** menit; TA-B ⌈49,5⌉ = **50** menit (di luar nominal, TA-3) |
| Catatan | Durasi dihitung dari blueprint W2; sama dengan W1 karena jumlah detik dasar kebetulan sama (1.200), bukan disalin |
| XP W2 | 4·5 + 4·10 + 50 + 70 + 50 + 25 + 50 = **305** (identitas `mod-w02.*`, sekali per identitas, XE-B) |
| Jadwal | M 180 + U 45 + L 90 (25 + 30 + 35) + P 90 + C 30 + R 45 = **480 menit** |

### 4.3 Simulasi deterministik (QC-02, QC-10)

Operasi berkas disimulasikan dengan aturan OP-1–OP-4:

| Butir | Keadaan akhir / hasil | Cocok dengan kunci |
|---|---|---|
| Lab act-03 vA | Masuk = `menu.xlsx` (1); Acara = `brosur-final.pdf`; Acara/Foto = `foto-acara.jpg`; Lama = `menu.xlsx`; Sampah = `brosur.pdf`; ditolak = langkah 4 | Ya (c01–c05) |
| Lab act-03 vB | Unggah = `jadwal.pdf`, `catatan.txt` (2); Lomba = `poster-lomba.png`; Lomba/Data = `daftar-anggota.csv`; Arsip = `jadwal.pdf`; Sampah = `poster.png`; ditolak = langkah 3 | Ya |
| Teori s17 vA / vB | `/foto` 1, `/cadangan` 2 (langkah 1 ditolak) / `/tugas` 2, `/kirim` 1 (langkah 1 ditolak) | Ya (kunci a / b) |
| Pelajaran 4 §2 | Masuk kosong; Arsip = `denah-lama.png`, `resep-kue.txt`; Sampah = `denah.png` | Ya |
| Latihan prac-04 no. 1 | `/kerja/A` 1, `/kerja/B` 1 | Ya |
| Remedial R-OPS | `/p` 1, `/q` 0 (langkah 1 dan 2 ditolak) | Ya |

Path relatif terpendek dihitung dengan algoritma tertulis di rubrik
(`path_correct`: naik `u` kali + sisa sasaran) untuk **semua** path di
teori s13–s14, lab act-02 c04–c06, concept s04, Pelajaran 3, remedial
R-PATH, dan proyek F3/F4: 0 selisih.

Fixture batas: act-03 memuat operasi yang **ditolak** (OP-2) dan berkas yang
dihapus lalu tidak dipulihkan; vB memuat berkas yang tidak tersentuh
(`catatan.txt`) sehingga hitungan berbeda dari vA (1 vs 2). Proyek memuat
jebakan PDF bukan-proyek dan pemeriksaan salin-vs-pindah (E03, E04).

### 4.4 Proyek: enumerasi dan contoh reviewer

Tepat **1** keadaan akhir memenuhi semua pemeriksaan K1 dan K3 (nama folder
tetap; lokasi setiap berkas ditentukan N2/N3; tanpa folder/berkas
tambahan); urutan operasi bebas. Contoh E01–E16 di `project/rubric.yaml`
dihitung ulang dengan evaluator dokumentasi (aturan `field_rules` dan
`criteria`): **16/16 cocok** (K1, K2, K3, total).

| Contoh | K1 | K2 | K3 | Total (K4 = 10) |
|---|---|---|---|---|
| E01 acuan | 60 | 20 | 10 | 100 |
| E02 `Dokumen` (huruf besar) | 48 | 20 | 5 | 83 |
| E03 disalin, bukan dipindah | 8 | 20 | 8 | 46 |
| E06 F3 ditulis absolut | 55 | 16 | 10 | 91 |
| E10 pohon tidak diubah, kosong | 0 | 0 | 0 | K4 saja |
| E11 pohon tidak diubah, path acuan disalin dari spesifikasi | 0 | 16 | 0 | 16 + K4 |

E11 menunjukkan bahwa path yang benar tanpa pekerjaan nyata tidak
mendapat poin K1 (`depends_on`), sementara K2 hanya menilai bentuk sesuai
definisi MR-A.

### 4.5 Skenario kelulusan (NP-4; `280·W = 150·T + 112·L + 56·P + 140·C`; lulus W ⇔ ≥ 22.400)

| ID | T/56 | L/100 | P/100 | C/20 | `280·W` | Hasil |
|---|---|---|---|---|---|---|
| SC-1 | 48 | 85 | 80 | 17 | 23.580 | PASSED (84,21…) |
| SC-2 | 42 | 75 | 80 | 15 | 21.280 | NOT_PASSED (W 76) |
| SC-3 | 56 | 90 | 95 | 14 | 25.760 | NOT_PASSED (C: 4·14 = 56 < 60) |
| SC-4 | 42 | 75 | 90 | 19 | 22.400 | **PASSED** (W tepat 80; T tepat 75%: 168 ≥ 168) |
| SC-5 | 28 | 100 | 100 | 10 | 22.400 | NOT_PASSED (W tepat 80, tetapi T 112 < 168 dan C 40 < 60) |
| SC-6 | 47 | 75 | 86 | 15 | 22.366 | NOT_PASSED (79,8785…; tampilan "79,87" atau "79,88" tidak mengubah keputusan eksak) |

Ambang komponen: teori 4·e ≥ 168 (e ≥ 42); lab/proyek e ≥ 75; concept
4·e ≥ 60 (e ≥ 15). Tidak ada keputusan berbasis pembulatan.

## 5. Posisi kunci jawaban

Urutan opsi tetap (tanpa pengacakan). Pilihan tunggal teori (TF-1, TF-4),
CE-S1, perbaikan CE-S5, dan K4 proyek: **a 8 · b 7 · c 9 · d 9** (33 kunci;
setelah penyeimbangan ulang dari a 5 · b 11 · c 11 · d 6). Opsi kategori
berurutan alami (s03, s07, s18) tidak diubah. Pilihan ganda: teori s02
{a,c,d}/{a,c,e}, s09 {a,c,e}/{b,c,d}; concept s03 {a,b,d}/{b,c,e}, s06
{a,c}/{b,d}.

## 6. Matriks kesetaraan varian (QC-04)

| Slot | Kompetensi | Konsep wajib | Tuntutan | Format | Kesulitan | Maks. | Detik | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|---|
| theory.s01 | os | OS vs aplikasi | Mengenali | TF-1 | D1 | 2 | 45 | Satu OS (Linux / iOS) di antara 3 aplikasi, termasuk 1 aplikasi bawaan di kedua varian |
| theory.s02 | os | lima fungsi OS | Memahami | TF-2 | D2 | 3 | 105 | 5 pernyataan, 3 fungsi OS benar (A: proses, perangkat, antarmuka; B: file, memori, antarmuka), 2 pengecoh tugas pengguna/hardware |
| theory.s03 | os | fungsi OS dari kejadian | Menerapkan | TF-1 | D1 | 2 | 45 | Opsi sama (4 fungsi); A perangkat (webcam), B file (menyimpan berkas) |
| theory.s04 | proc | program vs proses | Mengingat | TF-1 | D1 | 2 | 45 | A mencari "proses", B "program"; pengecoh istilah W2 lain |
| theory.s05 | proc | akibat mengakhiri proses | Menafsirkan tabel | TF-4 | D2 | 3 | 120 | Tabel 4 proses, satu "Tidak menanggapi"; kunci = RAM dikembalikan + proses lain tetap; B menambah "belum disimpan hilang" yang juga diajarkan; pengecoh sama jenisnya |
| theory.s06 | proc | multitasking 1 core vs banyak core | Menganalisis skenario | TF-1 | D3 | 4 | 105 | Kedua stem menulis asumsi model (1 core = 1 proses, tanpa SMT); A bergiliran (1 core), B bersamaan (4 core) |
| theory.s07 | fs | ekstensi → jenis | Mengingat | TF-1 | D1 | 2 | 45 | Opsi sama; mp3 / png |
| theory.s08 | fs | ekstensi dari titik terakhir | Menerapkan | TF-3 | D1 | 2 | 60 | Nama dengan 3 titik; jawaban `csv` / `docx` |
| theory.s09 | fs | ekstensi + folder | Memahami | TF-2 | D2 | 3 | 105 | Masing-masing 2 pernyataan ekstensi + 3 pernyataan folder/nama; 3 benar |
| theory.s10 | fs | membaca pohon, berkas vs folder | Menganalisis | TF-3 | D3 | 4 | 120 | Pohon 3 tingkat; A 5 berkas/3 folder, B 6 berkas/4 folder; aturan "tanpa ekstensi = folder" di kedua stem |
| theory.s11 | path | absolut vs relatif | Mengenali | TF-1 | D1 | 2 | 45 | A cari absolut, B cari relatif; pengecoh lawannya |
| theory.s12 | path | menyusun path absolut | Menerapkan | TF-3 | D2 | 3 | 90 | Pohon 5 komponen; jawaban satu path |
| theory.s13 | path | `..` satu tingkat | Menerapkan | TF-3 | D2 | 3 | 90 | Naik 1 + nama berkas |
| theory.s14 | path | naik 2 + turun 2 | Menerapkan | TF-3 | D3 | 4 | 120 | `../../X/Y/f` di kedua varian |
| theory.s15 | ops | salin vs pindah | Mengingat | TF-1 | D1 | 2 | 45 | Opsi sama; A salin, B pindah |
| theory.s16 | ops | urutan operasi yang dapat dikerjakan | Menerapkan | TF-5 | D2 | 3 | 105 | 4 langkah buat → salin/pindah → ganti nama → buka; urutan unik (ketergantungan keberadaan) |
| theory.s17 | ops | menelusuri 4 operasi dengan OP-2 | Menganalisis | TF-4 | D3 | 4 | 150 | Satu operasi ditolak, satu penghapusan, satu langkah Tempat Sampah; 3 pengecoh = 3 kesalahan khas (abaikan OP-2, salin = pindah, abaikan hapus/pulihkan) |
| theory.s18 | perm | arti baca/tulis/jalankan | Mengingat | TF-1 | D1 | 2 | 45 | Opsi sama; A tulis, B jalankan |
| theory.s19 | perm | membaca tabel izin | Menerapkan | TF-4 | D2 | 3 | 120 | Tabel 3 akun × baca/tulis; satu pernyataan benar |
| theory.s20 | perm | hak minimum | Menerapkan | TF-1 | D2 | 3 | 75 | A izin aplikasi (kamera+mikrofon saat dipakai), B izin akun (baca saja); pengecoh: berlebihan, terlalu sedikit untuk fungsi, admin |

| Slot | Kompetensi | Konsep wajib | Tuntutan | Format | Maks. | Menit | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|
| concept.s01 | os | 4 dari: proses, memori, perangkat, file, antarmuka, kernel | Memahami definisi | CE-S4 (k 4, r 5) | 4 | 5 | Masing-masing 4 istilah OS + 1 pengecoh = definisi fungsi yang tidak dipasangkan |
| concept.s02 | proc | RAM per proses; mengakhiri proses | Memahami | CE-S1 | 4 | 5 | A: mengapa yang belum disimpan hilang; B: mengapa proses lain tetap berjalan — keduanya dijawab "proses terpisah dengan RAM sendiri" |
| concept.s03 | fs | titik terakhir; ekstensi memilih aplikasi; isi tidak berubah | Memahami | CE-S2 (k 3) | 3 | 5 | Skenario ganti ekstensi (A) dan ekstensi tersembunyi (B); 3 benar + 2 pengecoh "isi berubah/pasti PDF" |
| concept.s04 | path | absolut `/`; `..`; relatif dari folder kerja | Menemukan kesalahan | CE-S5 (P 4) | 4 | 5 | Satu baris path relatif salah di antara 4 aturan benar; 4 opsi perbaikan |
| concept.s05 | ops | Tempat Sampah; pulihkan; salin dulu, periksa, baru hapus | Mengurutkan | CE-S3 (n 4) | 3 | 5 | A pemulihan + cadangan (2 urutan diterima); B salin–periksa–hapus–kosongkan (1 urutan) |
| concept.s06 | perm | hak minimum; izin sesuai fungsi; akun biasa vs admin | Memahami | CE-S2 (k 2) | 2 | 5 | Satu akibat/tindakan + satu prinsip di kedua varian |

| Aktivitas lab | Kompetensi | Konsep wajib | Maks. | Menit | Bukti kesetaraan |
|---|---|---|---|---|---|
| act-01 | fs | ekstensi titik terakhir; 7 kategori | 30 | 25 | Distribusi sama (DOK 2, TAB 1, GBR 2, AUD 1, VID 1, ARS 1, PRG 2); masing-masing 4 nama menyesatkan (titik ganda atau kata kategori lain di nama dasar) |
| act-02 | path | absolut; relatif turun; `..`; `../..` | 30 | 30 | Pohon isomorfik (home/nama/3 folder, kedalaman sama), pertanyaan berstruktur sama |
| act-03 | ops, perm, proc | 6 operasi dengan 1 penolakan, hapus, ganti nama; tabel izin; manajer tugas | 40 | 35 | Jenis operasi sama, urutan berbeda (langkah ditolak 4 vs 3); jumlah berkas akhir berbeda (1 vs 2); baris jawaban izin di posisi berbeda; c07 A "baca dan tulis", B "baca saja" |

## 7. Model sederhana vs kenyataan (QC-05)

| Model W2 | Kenyataan (ditulis di pelajaran) |
|---|---|
| Lima fungsi OS | Buku lain membagi berbeda (keamanan, jaringan) |
| 1 core = 1 proses pada satu waktu | *Hyper-threading* (SMT); penjadwalan nyata lebih rumit |
| Model path W2: `/`, peka huruf, tanpa `/` di akhir | Windows `C:\…`; Windows dan macOS bawaan umumnya tidak peka huruf |
| OP-2 nama sama → ditolak | OS bertanya (ganti/lewati/simpan keduanya) |
| Hapus → Tempat Sampah | Flashdisk/kartu memori sering tanpa Tempat Sampah; data terhapus kadang masih dapat dipulihkan alat khusus |
| Tulis = ubah, simpan, hapus | Izin folder, grup, ACL |
| Ekstensi menunjukkan jenis | Ekstensi hanya label; dapat menyesatkan (dibahas W4) |

## 8. Tumpang-tindih contoh vs butir bernilai (QC-06, QC-11)

Pemindaian otomatis: teks opsi benar > 35 karakter, jawaban singkat
bernilai (> 12 karakter atau ≥ 3 digit), path bernilai, perbaikan CE-S5,
dan opsi benar K4 dibandingkan dengan semua berkas V-L (pelajaran,
remedial, `spec.md` lab dan proyek).

| Temuan | Tindakan |
|---|---|
| `lab/act-03/spec.md` judul tabel izin memuat path versi akhir (= jawaban c05) | **Diperbaiki**: judul diganti "berkas brosur/poster versi akhir" |
| `lab/act-01` vA memakai `hadiah.jpg.exe`, contoh yang dijelaskan di Pelajaran 3 | **Diperbaiki**: diganti `kupon.png.exe` |
| Opsi benar concept s06 vB sama kalimat dengan tabel miskonsepsi Pelajaran 4 | **Diperbaiki**: dirumuskan ulang |
| PID 6027/7131 muncul di `spec.md` act-03 | Diterima: tabel manajer tugas adalah fixture yang harus dibaca pelajar (seperti opsi) |
| `../Musik` (concept s04 vA) adalah bagian dari `../../Musik/...` di Pelajaran 3 | Diterima: skenario berbeda (Tia vs Sari), keterampilan yang diajarkan |

| Contoh/latihan | Butir bernilai terdekat | Penilaian |
|---|---|---|
| les-03 pohon Sari (path) | teori s12–s14, lab act-02, proyek | Pohon dan jawaban berbeda |
| les-04 §2 telusur `/data` | teori s17, lab act-03 | Keadaan dan operasi berbeda; contoh dipakai sebagai contoh terlihat 0 poin |
| les-02 tabel manajer tugas | teori s05, lab act-03 c08 | Proses dan angka berbeda |
| les-04 tabel izin `jadwal-piket.xlsx` | teori s19, lab act-03 c06 | Berkas dan akun berbeda |
| les-04 izin aplikasi (tabel) | teori s20 vA (panggilan video), concept s06 vB (senter) | Aplikasi berbeda |
| Proyek: contoh bentuk isian | Jawaban F2–F5 | Memakai pohon `/home/contoh`; tidak memuat jawaban |

## 9. QC-01–QC-12 dan CQ-01–CQ-20

| QC | Hasil | Bukti |
|---|---|---|
| QC-01 maksimum dapat dicapai | PASS | §4.1, §4.4 |
| QC-02 contoh skor cocok aturan | PASS | §4.1 (CE-S3), §4.4 (16/16), §4.5 |
| QC-03 konversi satuan | NOT APPLICABLE (tidak ada konversi satuan di W2; MB pada tabel proses hanya dibaca) | — |
| QC-04 kesetaraan varian | PASS | §6 |
| QC-05 model sederhana dilabeli | PASS | §7; asumsi tertulis di stem s06, s10, s16, s17 |
| QC-06 contoh ≠ butir bernilai | PASS setelah 3 perbaikan | §8 |
| QC-07 instruksi vs metadata | PASS | `spec.md` vs `checks.yaml`: nama berkas, pohon, operasi, tabel, poin dicek; rubrik vs `project/spec.md` (N1–N4, F1–F6) |
| QC-08 normalisasi dan ketergantungan | PASS | `normalization` path (peka huruf, `./`), angka, ekstensi; rubrik `path_form`, `number_rule_F5`, `depends_on` dengan contoh diterima/ditolak |
| QC-09 nama field kanonik | PASS | 0 `needs`/`answer_normalization`/`expected_sequence` |
| QC-10 fixture batas | PASS | §4.3; batas komponen §4.5 (SC-4 tepat 80) |
| QC-11 kontrak visibilitas VC-1–VC-5 | PASS setelah perbaikan | §8; fixture urutan (s16, concept s05) ditulis dalam urutan tampil ≠ urutan diterima; contoh aturan skor memakai skenario tidak berkaitan |
| QC-12 desimal vs biner | PASS | Satuan hanya MB pada tabel proses (desimal, W1); tidak ada GiB |

CQ-01–CQ-20 (urutan TPL-19): kebenaran teknis (PASS, §7 + perbaikan
macOS/SMT) · ramah pemula (PASS: istilah dijelaskan + glosarium) · LO
terukur (PASS) · prasyarat (PASS: W1) · cakupan (PASS, §3) · tidak menilai
yang belum diajarkan (PASS: semua ekstensi/aturan path/OP di pelajaran) ·
kelengkapan (PASS, §2) · kesetaraan varian (PASS) · kunci (PASS) ·
aritmetika (PASS) · fixture deterministik (PASS) · rubrik objektif (PASS)
· concept D-23 (PASS) · XP unik (PASS) · aksesibilitas (PASS: setiap
diagram/pohon punya deskripsi teks) · versi (PASS: 1.0) · 480 menit (PASS) ·
offline (PASS) · konsistensi D-01–D-38 (PASS) · kunci tidak tampil sebelum
umpan balik (PASS, §8).

## 10. Regresi F-01–F-23 (penerapan ke W2)

| Temuan W1 | Pemeriksaan di W2 | Status |
|---|---|---|
| F-01/F-02/F-19 rubrik tanpa gerbang nol; isian angka punya pemeriksaan kebenaran; peran K1/K2/K3 | F5 diperiksa K1.c14; K2 bentuk saja; MR-2 per pemeriksaan; E10/E11 | PASS |
| F-03 bias posisi kunci | §5 | PASS (diseimbangkan) |
| F-04/F-12/F-13 kesetaraan | §6 | PASS |
| F-05/F-21 enumerasi | §4.4 (1 keadaan sah; 16 contoh dihitung ulang) | PASS |
| F-07/F-14/F-23 kebocoran | §8 | PASS setelah perbaikan |
| F-09 maksimum tak tercapai | §4.1 | PASS |
| F-10 arah konversi | Tidak ada konversi satuan | NOT APPLICABLE |
| F-11/F-15 asumsi model | §7 | PASS |
| F-16/F-20 field kanonik | §9 QC-09 | PASS |
| F-17 label ambigu | Folder vs berkas di pohon soal (aturan "tanpa ekstensi = folder"); "Tidak menanggapi" | PASS |
| F-22 satuan | QC-12 | PASS |
| F-24–F-27 (hardening CB-0.5) | Tidak ada perubahan `.claude/` di W2 | Dipertahankan |

## 11. Batas penilaian objektif

Pemeriksaan membuktikan jawaban/isian sesuai kunci dan aturan pada versi
soal yang dikerjakan; tidak membuktikan pemahaman penuh atau kompetensi
tersertifikasi (D-17, D-34). Simulator pohon folder adalah kebutuhan konten;
mekanismenya di aplikasi belum ada (tidak ada klaim implementasi).

## 12. Bukti reviewer dan metrik efisiensi (observasi pertama CB-0.5)

| Field | Isi |
|---|---|
| Reviewer | Claude (penyusun), review mandiri |
| Tanggal | 2026-11-24 |
| Basis | `main` = `ab0103e` |
| Temuan terbuka | Tidak ada yang diketahui. Butuh review ChatGPT dan penerimaan owner |

Metrik W2 (dihitung dari transkrip sesi; perkiraan ±2 untuk hitungan
panggilan): panggilan alat ≈ 40 untuk produksi + validasi W2; berkas unik
yang dibaca untuk persiapan ≈ 30 (sebagian besar dipakai ulang untuk W3–W4,
TE-13); baca ulang berkas yang sama: 0 (W1 `review.md` dibaca dalam 3 bagian
berbeda); aksi gagal 2 (pemeriksa crash saat uji kontrol W1 karena field
yang tidak ada di W1; satu positif palsu di pemindai karena `lstrip`);
kegagalan identik berulang 0; aktivasi skill 0 tambahan (planning-with-files
dan verification-before-completion sudah dimuat di Fase B); pembaruan
checkpoint 1; operasi validasi 10 (pemeriksa struktur 5, simulasi 3,
pemindai V-L 2); pemulihan sesi 0. TOKEN USAGE: **NOT MEASURABLE**.
