---
module_id: mod-w02
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-1 + koreksi F-28–F-72 (dua putaran). Review independen PR #27: REQUEST CHANGES (dua kali) → dikoreksi → delta review PASS (terarah, dengan batas yang diungkapkan); diterima owner W02-ACC (2026-11-24)"
---

# W2 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-1) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review independen (ChatGPT) | PR #27: **REQUEST CHANGES** (F-28–F-70, lalu delta F-28–F-72) → dikoreksi → **delta review PASS** — targeted delta review with disclosed limitations (lihat bagian penerimaan) |
| Diterima owner (W02-ACC) | **YA** (2026-11-24, PR #27 merge `846051f`) — lihat bagian penerimaan di akhir dokumen |
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
tambahan); urutan operasi bebas. Contoh E01–E21 di `project/rubric.yaml`
dihitung ulang dengan evaluator dokumentasi (aturan `field_rules` dan
`criteria`): **22/22 cocok** setelah koreksi (K1, K2, K3, total; termasuk E05b dan E16–E21).

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
| QC-02 contoh skor cocok aturan | PASS | §4.1 (CE-S3), §4.4 (22/22), §4.5 |
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
| Temuan terbuka | Tidak ada BLOCKED (deskripsi F-55–F-57, F-59 dipulihkan owner, putaran 2); *historis (sebelum penerimaan):* butuh re-review independen dan penerimaan owner; **status aktif:** delta review PASS dan diterima owner W02-ACC (lihat bagian penerimaan). Register: bagian koreksi konsolidasi di akhir dokumen |

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

## 13. Koreksi konsolidasi CB-1 (PR #27, F-28–F-70; 2026-11-24)

Review PR #27 = **REQUEST CHANGES**. Sebelum mengedit diverifikasi: head
`a9241d33c2cf32e177ca92618df458b78dd6cb98`, base
`ab0103e4954ead4ded6343d105d73a2729916cd6` (cocok). Koreksi diterapkan pada
PR #27 yang sama. *Historis (saat koreksi):* status modul **diproduksi dan dikoreksi; menunggu re-review
independen dan penerimaan owner** — belum diterima.

### 13.1 Register F-28–F-72 (45 ID; diperbarui pada koreksi terarah putaran 2)

| ID | Lingkup | Disposisi | Bukti |
|---|---|---|---|
| F-28 | W3 | CONFIRMED — FIXED | `project/rubric.yaml` K1.c02–c06 membandingkan dengan konstanta `192.168.50.1` (bukan isian F1) + `f1_dependency`; F1 salah tidak lagi menjatuhkan pemeriksaan lain; fixture E18–E21 |
| F-29 | W4 | CONFIRMED — FIXED | `lab/act-02` `verdict_rule`: A = tidak ada indikator dalam model W4, **bukan** jaminan aman; spesifikasi diselaraskan |
| F-30 | W4 | CONFIRMED — FIXED | act-01 vA S6 + halaman yang meminta sandi email (bukti perilaku fiktif); label `WIF` = bukti perilaku; les-01: nama mirip saja bukan bukti; proyek S4 diperkuat |
| F-31 | W3 | NOT REPRODUCED | Blueprint dan review W3 pada commit produksi awal `9a562ce` dan pada head koreksi: TF-3 = 7 slot (s05, s08, s09, s10, s18, s19, s20) di keduanya; review mencantumkan "TF-3 × 7" di keduanya (dihitung ulang dari `git show`) |
| F-32 | W2 ◀ | CONFIRMED — FIXED | theory s05 vB dan concept s02 vA menyatakan "tidak punya simpan otomatis/pemulihan"; les-02 menjelaskan pengecualian simpan otomatis |
| F-33 | W2 ◀ | CONFIRMED — FIXED | theory s09 vA opsi a; concept s03 vA opsi d + umpan balik isi/ekstensi/pengaitan; les-03 membedakan isi, ekstensi, pengaitan aplikasi |
| F-34 | W3 | CONFIRMED — FIXED | theory s01 vA/vB dan act-03 c01: "Model peran W3 … **fungsi**" + rasional kotak router Wi-Fi; les-01 fungsi vs kotak |
| F-35 | W3 | CONFIRMED — FIXED | concept s04 (R5/R2): TCP mengirim ulang data hilang dan menyusun berurutan **selama sambungan berjalan**; les-03 diselaraskan |
| F-36 | W4 | CONFIRMED — FIXED | concept s04 opsi/umpan balik: HTTPS = sambungan terenkripsi ke nama domain, bukan bukti organisasi/kejujuran; les-03 tabel empat pertanyaan; remedial R-PHISH |
| F-37 | W4 | CONFIRMED — DOCUMENTATION CLARIFIED | Klarifikasi asumsi skenario (putaran 2): stem menyatakan model hentikan → amankan dan A prasyarat B; dua urutan diterima per varian **bukan** cacat. Isi putaran 1: concept s06 vA ditulis ulang: model "hentikan → amankan" dinyatakan di stem; A prasyarat B; 2 urutan diterima (ABCD, ABDC) — setara dengan vB (2 urutan); petunjuk "Setelah …" yang membocorkan urutan dihapus |
| F-38 | W4 | CONFIRMED — FIXED | s09/s11, act-03 c03, concept s03, les-02, remedial: digit 0–9, boleh diawali 0 dan berulang, yang dihitung jumlah PIN berbeda; jawaban diverifikasi `10**n` |
| F-39 | W4 | CONFIRMED — FIXED | `collection_validity` (kode tak dikenal/ganda → koleksi INVALID, pemeriksaan yang bergantung 0, lainnya tetap); fixture E14–E17 |
| F-40 | W2 ◀ | CONFIRMED — FIXED | `tree_valid` (6 syarat); pohon rusak → pemeriksaan bergantung F1 = 0, K2.c02–c05 tetap; gangguan aplikasi → EVALUATION_ERROR; fixture E17–E20 |
| F-41 | W2 ◀ | CONFIRMED — FIXED | act-01: "jenis isi yang **diharapkan** dari ekstensi"; umpan balik "→ diharapkan …"; les-03: ekstensi bukan bukti isi |
| F-42 | W2–W4 ◀ | CONFIRMED — FIXED | Aturan normalisasi eksplisit di setiap TF-3 dan lab (nol di depan ditolak; pemisah ribuan hanya bila diizinkan, pola `1.234`); `normalization_examples` di checks lab; diperiksa konsisten otomatis |
| F-43 | W3 | CONFIRMED — FIXED | act-01 `network_assumptions` menyebut rentang khusus (loopback, link-local, dll.) di luar model; les-02: publik "umumnya unik"; status publik hanya dari fixture |
| F-44 | W4 | CONFIRMED — FIXED | les-02: pembatasan percobaan PIN menurunkan risiko, **tidak** membuat tebakan mustahil; MFA "jauh lebih sulit", bukan mustahil |
| F-45 | W2 ◀ | CONFIRMED — DOCUMENTATION CLARIFIED | `final_state_only`: hanya keadaan akhir pohon dinilai; spesifikasi N4; fixture E21 (dihapus lalu dipulihkan → 100) |
| F-46 | W3 | CONFIRMED — DOCUMENTATION CLARIFIED | `suffix_24_rule` dan catatan IPN (lab vs proyek); fixture E20 (F1 `/24`) |
| F-47 | W4 | CONFIRMED — DOCUMENTATION CLARIFIED | T1 diberi catatan "aturan simulasi"; les-02: panjang saja tidak cukup (sandi umum/bocor tetap lemah) |
| F-48 | W2 ◀ | CONFIRMED — DOCUMENTATION CLARIFIED | s19 vB rasional = model W2; les-04 membedakan model tulis/hapus W2 dari izin folder nyata |
| F-49 | W3 | CONFIRMED — FIXED | Putaran 2 (deskripsi asli): s07 vA opsi a dan pembahasan tidak lagi menganggap router pasti beralamat publik; alamat privat tidak dirutekan langsung di internet publik; CGNAT disebut; vB menyatakan skenario tanpa CGNAT; les-02 diselaraskan. Kunci tetap a/c. Koreksi putaran 1 dipertahankan: les-02: alamat IP milik **antarmuka**, bukan perangkat |
| F-50 | W3 | CONFIRMED — FIXED | Putaran 2: s13 vA memberi asumsi (halaman sama tanpa peringatan sertifikat; pesan "alamat server untuk nama itu tidak ditemukan"); rasional HTTPS dan pembahasan menyebut DNS sebagai dugaan terkuat, bukan bukti pasti. Kunci tetap b. Putaran 1 dipertahankan: les-03 cek pemahaman: DNS/IP "kadang" (cache, alamat langsung) — tidak dinyatakan selalu |
| F-51 | W3 | CONFIRMED — FIXED | Putaran 2 (koreksi penilaian): satuan kecepatan peka huruf — s18 (`NUMR`, normalization_examples), lab act-03 c05 (head lama menerima `12 mb/s` dan `12 Mb/s`), spesifikasi lab, les-04; 8 fixture owner + 107 contoh lolos `norm_check.py`. Putaran 1 dipertahankan: les-04: reservasi DHCP sebagai alternatif alamat statis di luar rentang; aturan RA tidak berubah |
| F-52 | W4 | CONFIRMED — FIXED | Putaran 2: aturan kategori utama dijadikan **berurutan** (aturan pertama yang cocok) karena WIF dan PHI tumpang-tindih pada Wi-Fi tiruan yang menampilkan halaman peminta sandi (act-01 vA S6, vB S7; proyek S4); kunci tidak berubah, setiap skenario tepat satu kunci. Putaran 1: Aturan **kategori utama** (s07 stem, act-01 `primary_classification_rule`, proyek Bagian A, les-01); s07 vB E2 diperjelas |
| F-53 | W4 | CONFIRMED — FIXED | Putaran 2: s08 vB pembahasan, concept s01 (R2, L4) dan s03 vB baris 3, les-02, remedial: OTP = bukti sementara akses ke autentikator/rahasianya, dapat dicuri/diteruskan; tanpa klaim "membuktikan pemilik/memegang ponsel". Putaran 1 (rumusan "bukti memegang ponsel" kini diganti): s08 vB; concept s03 baris autentikator; les-02: autentikasi = pembuktian, OTP = faktor "yang dimiliki" |
| F-54 | W4 | CONFIRMED — FIXED | Putaran 2: s16 vA/vB pembahasan mendefinisikan lima jenis media model W4 (CB-2) dan menghitung media tiap rencana; folder lain di perangkat sama bukan media baru. Kunci dan aturan 3-2-1 tetap. Putaran 1: les-04 CB-1 "salinan terpisah"; model W4 menganggap salinan utuh, dunia nyata perlu uji pemulihan; aturan 3-2-1 dan penilaian tidak berubah |
| F-55 | W4 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): s19 vA kini menyatakan Nia masih dapat masuk dengan sandi lama dari perangkat aman; pembahasan menyebut urutan berlaku untuk skenario ini (bila akses hilang: pemulihan lewat kanal resmi; melapor sedini mungkin). Urutan tetap tunggal BDAC |
| F-56 | W2 ◀ | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner: concept s04 vB opsi d `../../foto/sampul.png` mencapai tujuan tetapi bukan terpendek. Diperbaiki di putaran 1 (baris salah menuntut "path relatif **terpendek**"; rasional d). Inspeksi independen terarah: PASS; dipertahankan |
| F-57 | W2 ◀ | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): concept s05 vB langkah B kini memeriksa jumlah/nama berkas **dan** membuka setiap berkas untuk memastikan isinya lengkap dan terbaca sebelum menghapus asal (tanpa hash); umpan balik dan les-04 diselaraskan. Format CE-S3 dan urutan ABCD tetap |
| F-58 | W4 | CONFIRMED — FIXED | Putaran 2 (deskripsi asli): concept s01 vB L2 "dibaca orang lain **tanpa izin pemiliknya**"; skenario CIA terkait diperketat (s01 vB L1, theory s02 vB K2/K3/K4, s03 vB). Koreksi putaran 1 tentang tanda vs bukti malware dipertahankan sebagai koreksi tambahan, bukan pengganti: s05 stem: gejala = **tanda peringatan**, bukan bukti pasti; klasifikasi unik hanya dengan bukti perilaku fiktif (act-01, les-01) |
| F-59 | W4 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): label AMN = tindakan pengguna tepat / bukti ancaman tidak cukup, **bukan** jaminan tidak ada ancaman — spec, checks (`codes`, `primary_classification_rule`), skenario vB S10 (yang diklasifikasikan = tindakan memeriksa lewat aplikasi resmi), umpan balik. ID AMN dan poin tetap |
| F-60 | W2 ◀ | CONFIRMED — FIXED | les-01: "aplikasi biasa" berjalan di atas OS + catatan perangkat tanpa OS (bare-metal) |
| F-61 | W2 ◀ | CONFIRMED — FIXED | les-02 latihan 1c: satu aplikasi dapat punya dua proses (dua PID) + pembahasan; jendela ≠ proses |
| F-62 | W3 | CONFIRMED — FIXED | les-01: modem vs ONT/ONU (fiber) |
| F-63 | W3 | CONFIRMED — FIXED | les-03: contoh TCP/UDP sebagai "pemakaian umum" + catatan QUIC (HTTP/3 di atas UDP) |
| F-64 | W3 | CONFIRMED — FIXED | les-04: RA-5 (gateway) berlaku untuk klien LAN |
| F-65 | W4 | CONFIRMED — FIXED | Inspeksi independen terarah PASS; dipertahankan (pengecualian `@`, port, `?`, `#`). les-03: UR-1 hanya untuk bentuk alamat W4 (tanpa port, userinfo, alamat IP) |
| F-66 | W4 | CONFIRMED — FIXED | les-04 dan concept s06: laporkan sedini mungkin (boleh bersamaan); tidak harus menunggu langkah terakhir |
| F-67 | W2–W4 ◀ | CONFIRMED — FIXED | Remedial W2–W4: VA-1–VA-6 (pemakaian paling sedikit → bukan varian sebelumnya → indeks terkecil; VA-3) |
| F-68 | W4 | CONFIRMED — FIXED | Remedial R-AUTH: MFA = **dua faktor atau lebih** dari jenis berbeda |
| F-69 | docs | CONFIRMED — FIXED | `CURRICULUM_PRODUCTION_PLAN.md` header/legenda/§4/§6.1 (historis)/§8; `CURRICULUM_OFFLINE_LAB_SPEC.md` K-13 historis + status aktif |
| F-70 | docs | CONFIRMED — FIXED | Baris CB-0: semua kebijakan terputuskan, tanpa penerimaan terpisah, review independen terbatas, **bukan** final global; CB-1a ACCEPTED (W01-ACC) |
| F-71 | W2 ◀ | CONFIRMED — FIXED | Baru (putaran 2): setiap depends_on yang memakai F1 kini `F1 (tree_valid)`, termasuk K1.c11–c14 (head lama tanpa F1); dependency_rule diperjelas. `sim_w02.py`: 19 pemeriksaan bergantung tree_valid, independen tepat K2.c02–c05; E17–E20 = 0/16/0 · 26; E21 = 100 |
| F-72 | W4 | CONFIRMED — FIXED | Baru (putaran 2): depends_on K1.c01–c17, K2.c01–c06, K3.c01–c03 mensyaratkan isian sah (collection_validity); K2.c07–c08 tetap independen; akun tak dikenal dan struktur luar rusak diperjelas dengan kontrak yang ada; fixture E19, E20; `sim_w04.py` 34 asersi dependensi + uji mutasi |

Ringkasan (45 ID, satu disposisi per ID; bukan 45 cacat aktif): FIXED 39 · NOT REPRODUCED 1 · DOCUMENTATION CLARIFIED 5. ◀ = berlaku untuk modul ini.

### 13.2 Matriks bukti per butir

Kolom 1–10 = kriteria re-audit: 1 kompetensi/LO · 2 akurasi akademik ·
3 asumsi model eksplisit · 4 kunci benar dan tunggal · 5 pengecoh sah ·
6 skor deterministik · 7 maksimum tercapai · 8 kesetaraan varian ·
9 umpan balik · 10 visibilitas. **A** = diperiksa otomatis (pemeriksa
struktur: ID unik, kunci di opsi, rasional per pengecoh, poin, kompetensi;
pemindai V-L); **S** = jawaban dihitung ulang independen (simulasi, mis.
`ipaddress`, `urlsplit`, `10**n`); **M** = dibaca manual oleh penyusun;
— = tidak berlaku. Semua sel lolos pada putaran ini; kolom "Koreksi" =
temuan yang menyentuh butir itu. Ini review mandiri, bukan review independen.

| Butir | Komp. | Format · D | Kunci vA / vB | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Koreksi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-s01 | os-01 | TF-1 · D1 · 2 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s02 | os-01 | TF-2 · D2 · 3 | `a,c,d` / `a,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s03 | os-01 | TF-1 · D1 · 2 | `d` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s04 | proc-01 | TF-1 · D1 · 2 | `d` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s05 | proc-01 | TF-4 · D2 · 3 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A | F-32 |
| T-s06 | proc-01 | TF-1 · D3 · 4 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s07 | fs-01 | TF-1 · D1 · 2 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s08 | fs-01 | TF-3 · D1 · 2 | `csv,.csv` / `docx,.docx` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s09 | fs-01 | TF-2 · D2 · 3 | `a,c,e` / `b,c,d` | A | M | M | A | A+M | A | A | M | A | A | F-33 |
| T-s10 | fs-01 | TF-3 · D3 · 4 | `5,5 berkas,5berkas` / `6,6 berkas,6berkas` | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| T-s11 | path-01 | TF-1 · D1 · 2 | `b` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s12 | path-01 | TF-3 · D2 · 3 | `/home/raka/Kuliah/Fisika` / `/home/lina/Hobi/Resep/so` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s13 | path-01 | TF-3 · D2 · 3 | `../jadwal.pdf,./../jadwa` / `../ringkasan.txt,./../ri` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s14 | path-01 | TF-3 · D3 · 4 | `../../Musik/Gamelan/gend` / `../../Proyek/Robot/ranca` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s15 | ops-01 | TF-1 · D1 · 2 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s16 | ops-01 | TF-5 · D2 · 3 | `C,D,A,B` / `D,B,C,A` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s17 | ops-01 | TF-4 · D3 · 4 | `a` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s18 | perm-01 | TF-1 · D1 · 2 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s19 | perm-01 | TF-4 · D2 · 3 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A | F-48 |
| T-s20 | perm-01 | TF-1 · D2 · 3 | `d` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| C-s01 | os-01 | CE-S4 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s02 | proc-01 | CE-S1 · 4 | `b` / `d` | A | M | M | A+M | M | A | A | M | A | A | F-32 |
| C-s03 | fs-01 | CE-S2 · 3 | `a,b,d` / `b,c,e` | A | M | M | A+M | M | A | A | M | A | A | F-33 |
| C-s04 | path-01 | CE-S5 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A | CE-S5 (audit) |
| C-s05 | ops-01 | CE-S3 · 3 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s06 | perm-01 | CE-S2 · 2 | `a,c` / `b,d` | A | M | M | A+M | M | A | A | M | A | A |  |
| L-act-01.vA | fs-01 | 10 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-41 |
| L-act-01.vB | fs-01 | 10 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-41 |
| L-act-02.vA | path-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vB | path-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vA | ops-01, perm-01, proc-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| L-act-03.vB | ops-01, perm-01, proc-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| P (spec+rubrik) | semua LO | MR-A | contoh 22 | A | M | M | S | — | A+S | A+S | — | A | A | F-40, F-45 |
| les-01 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-60 |
| les-02 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-32, F-61 |
| les-03 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-33, F-41 |
| les-04 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-48 |
| remedial | semua LO | TPL-14 | — | M | M | M | M | — | — | — | — | M | A | F-67, F-32, F-33, F-48 |

CE-S5 (s04): baris salah kini menuntut "path relatif **terpendek**", sehingga koreksi alternatif yang sah tetapi lebih panjang tidak lagi menjadi jawaban benar kedua; rasional opsi d vB disesuaikan. CE-S3 (s05): vA 2 urutan diterima, vB 1; skor = pasangan berurutan dalam **satu** urutan diterima (tanpa penggabungan); urutan tampilan bukan urutan jawaban (vA D,B,A,C; vB C,A,D,B).

### 13.3 Fixture evaluator baru (dokumentasi, bukan evaluator produksi)

| Fixture | Input | Diharapkan | K1/K2/K3 · total | Alasan |
|---|---|---|---|---|
| E17 | Folder `dokumen` ada tanpa induk `ProyekSains`; F2–F5 acuan | F1 INVALID_ANSWER | 0/16/0 · 26 | `tree_valid` (2); bentuk F2–F5 tetap dinilai (kredit independen) |
| E18 | `sains-catatan.txt` dua kali di folder yang sama | F1 INVALID_ANSWER | 0/16/0 · 26 | `tree_valid` (3); salinan di folder **berbeda** tetap sah (E03) |
| E19 | Folder di bawah berkas (`lagu-favorit.mp3/x`) | F1 INVALID_ANSWER | 0/16/0 · 26 | `tree_valid` (5) |
| E20 | Folder `Proyek Sains` (spasi) | F1 INVALID_ANSWER | 0/16/0 · 26 | `tree_valid` (1)/(6) |
| E21 | Berkas dihapus lalu dipulihkan; keadaan akhir = acuan | Dinilai penuh | 60/20/10 · 100 | `final_state_only` (F-45) |

Gangguan aplikasi saat membaca pohon → EVALUATION_ERROR (D-24 IE-2), bukan 0 poin. Contoh rubrik: **22/22** (E01–E21 + E05b) cocok dengan evaluator dokumentasi; E16 (MR-6) kini juga diperiksa otomatis. Jumlah keadaan akhir bernilai penuh tetap **1** (ruang solusi tidak berubah).

### 13.4 Regresi skor dan durasi

W2: teori 56 (D1 8×2 = 16, D2 8×3 = 24, D3 4×4 = 16; TP-B 40/40/20); S = 1.680 → S_buffer 1.848 → timer **33**, review 12, TA-B 50; lab 30 + 30 + 40 = 100; concept 20; proyek 100. Tidak ada perubahan maksimum, durasi, atau XP (305 XP/modul; 915 untuk
W2–W4). Aturan lulus tetap: 4·e ≥ 3·m per komponen (skor terbaik) dan
Σ bobot·e/m ≥ 80% eksak; pembulatan hanya untuk tampilan.

### 13.5 Visibilitas dan keamanan (QC-06, QC-11, VC-1–VC-5)

Pemindai V-L dijalankan ulang: semua temuan termasuk kategori yang sudah
diterima di bagian visibilitas di atas (fakta yang diajarkan dan diuji
sebagai ingatan; data input fixture yang tampil di spesifikasi; positif palsu
substring). Tidak ada judul pembuka jawaban, urutan tampilan CE-S3 = urutan
jawaban, rasional pengecoh sebelum dinilai, atau contoh rubrik yang membuka
jawaban proyek. D-34 dipertahankan (tanpa enkripsi/proteksi kunci palsu).
Semua skenario fiktif dan defensif; tidak ada kredensial nyata, kode
berbahaya, sistem tanpa izin, atau latihan ofensif.

### 13.6 Pedagogi

Penjelasan mendahului penilaian; koreksi putaran ini menambah koreksi
miskonsepsi pada pelajaran yang tersentuh (kolom "Koreksi" di §13.2) tanpa
menambah menit (anggaran 480 menit tetap). Latihan terbimbing berbeda dari
butir bernilai (dicek silang). Tidak ada ketergantungan pada W5–W16. Tidak
diklaim setara universitas atau efektivitas belajar tervalidasi.

### 13.7 Regresi F-01–F-27

F-01–F-23 (kebenaran rubrik dan kredit independen, distribusi kunci,
kesetaraan varian, enumerasi solusi sah, asumsi akademik, field kanonik,
maksimum tercapai, normalisasi, visibilitas, satuan desimal/biner, kualitas
bukti): diperiksa ulang lewat pemeriksa struktur, simulasi, dan pemindai yang
sama — lolos. F-24–F-27 (pengerasan alur kerja) dipertahankan: tidak ada
perubahan pada `.claude/`, izin, hooks, allowed-tools, asal skill, atau
kontrak alur kerja. V03 tetap verifikasi sesi baru yang dilaporkan
sebelumnya; **tidak** dijalankan ulang di putaran ini.

### 13.8 Batas dan metrik putaran koreksi

*Historis (putaran 1):* temuan F-55, F-56, F-57, F-59 saat itu **BLOCKED** — penutupan penuh register tidak
diklaim. Metrik (perkiraan dari transkrip, ±10%): satu putaran koreksi untuk
W2–W4 bersama; aksi gagal yang tercatat: patch multi-pasangan yang gagal
total (dijalankan ulang per pasangan) dan beberapa total fixture hitungan
tangan yang salah (dikoreksi dari evaluator dokumentasi); pemulihan sesi 1
(konteks diringkas). TOKEN USAGE: **NOT MEASURABLE**.

## 14. Koreksi terarah putaran 2 (delta review PR #27; 2026-11-24)

Delta review independen = **REQUEST CHANGES**. Sebelum mengedit
diverifikasi: PR #27 terbuka, belum di-merge; head
`145bb5693320c322eda4d7ea0d08b0a284018c9e`, base
`ab0103e4954ead4ded6343d105d73a2729916cd6`, branch `planning/cb1-w02-w04`.
Register di §13.1 kini memuat **45 ID** (F-28–F-72) dengan satu disposisi
per ID; deskripsi F-55, F-56, F-57, F-59 dipulihkan owner, sehingga tidak
ada lagi yang BLOCKED karena rincian hilang. F-49–F-51 mengikuti deskripsi
asli; koreksi putaran 1 yang tercatat di bawah ID itu dipertahankan.

### 14.1 Perubahan dan bukti modul ini

| ID | Perubahan putaran 2 | Bukti terjalankan |
|---|---|---|
| F-57 | `concept/items/s05.yaml` vB langkah B: cek jumlah/nama **dan** buka setiap berkas (isi lengkap, terbaca) sebelum menghapus asal; umpan balik; `lessons/les-04.md` catatan pemeriksaan salinan | `validate.py mod-w02` → NO ERRORS; format CE-S3 dan urutan ABCD tidak berubah |
| F-71 | `project/rubric.yaml`: semua depends_on yang memakai F1 menjadi `F1 (tree_valid)`, termasuk K1.c11–c14; `dependency_rule` diperjelas | Head lama: K1.c11–c14 tanpa F1 di depends_on (dibaca dengan `git show`). `sim_w02.py`: 23 pemeriksaan K1–K3, 19 bergantung tree_valid, independen tepat K2.c02–c05; E17, E18, E19, E20 = K1 0 · K2 16 · K3 0 · total 26; E21 = 60/20/10 · 100; 22/22 contoh cocok |
| F-56 | Tidak ada perubahan (putaran 1 dipertahankan; inspeksi independen terarah PASS) | — |

### 14.2 Prosedur validasi (skrip dokumentasi sementara di scratchpad sesi, tidak di-commit)

| Prosedur | Hasil teramati |
|---|---|
| `validate.py mod-w01` … `mod-w04` (struktur, ID unik, kunci di opsi, poin, durasi A.4, field kanonik) | NO ERRORS × 4 |
| `sim_w02.py`, `sim_w03.py`, `sim_w04.py` (evaluator dokumentasi; dihitung ulang tanpa memakai total yang dinyatakan) | W2 22/22 + F-71 OK; W3 21/21; W4 20/20 + 34 asersi dependensi |
| `norm_check.py` (F-51 dan seluruh `normalization_examples`) | 8/8 fixture owner; 107 contoh; ALL OK |
| `scan_vl.py` (V-L) | Hit W2 3 · W3 23 · W4 12 — sama dengan putaran 1, semua kategori yang sudah diterima |
| Inspeksi dokumen | Pembacaan manual penyusun untuk butir yang diubah (bukan review independen) |

Baseline tetap (diverifikasi dari isi): teori 56/56/56; lab 100/100/100;
proyek 100/100/100; concept 20/21/20; timer 33/32/32 menit; TP-B 8/8/4
slot; XP 305 per modul (915); 480 menit per modul; bobot 30/40/20/10, lulus
≥ 75 per komponen dan ≥ 80 berbobot (eksak). Tidak ada runtime yang
diverifikasi; tidak ada evaluator produksi.

### 14.3 Regresi F-01–F-27

Pemeriksa yang sama dengan putaran 1 lolos (kunci, kesetaraan varian,
maksimum, normalisasi, visibilitas, satuan desimal/biner, enumerasi solusi:
W2 1, W3 78.485.511.600, W4 163.840 — tidak berubah). F-24–F-27
dipertahankan: tidak ada perubahan `.claude/`, izin, hooks, allowed-tools,
asal skill, atau kontrak alur kerja; W1 tidak diubah. V03 tidak dijalankan
ulang. TOKEN USAGE: **NOT MEASURABLE**.


## Penerimaan W2 (W02-ACC) dan batas review independen

PR #27 di-merge (head `1a58338bcc863320ff4eafbb0f407cee4b2a9f59`, merge commit `846051f66ee4d1e36e9b34e0c9d1787fb713617b`). Owner menerima W2 (W02-ACC, 2026-11-24).

Verdict independen: **PASS — targeted delta review with disclosed limitations.** Batas review independen (dinyatakan owner): delta review terarah PASS — F-49–F-59 dan F-71–F-72 lolos review terarah; integritas register F-28–F-72 diverifikasi; 16 simulasi normalisasi independen lolos. Regresi historis penuh, semua skrip validasi sementara, uji dengan pelajar, dan verifikasi runtime Android **tidak** diulang secara independen.

Register F-01–F-72 dan disposisinya di atas tetap sebagai catatan historis (39 FIXED, 5 DOCUMENTATION CLARIFIED, F-31 NOT REPRODUCED pada F-28–F-72). Penerimaan ini **bukan** verifikasi menyeluruh, verifikasi runtime, atau uji durasi dengan pelajar; temuan baru tetap boleh diangkat. Bukti aktivasi V03 tetap dari sesi segar sebelumnya.

## Penyelarasan kebijakan D-39 (2026-11-25) — bukan perubahan disposisi historis

Owner menyetujui **D-39 HYBRID COMPETENCY COVERAGE**. Audit cakupan
([CURRICULUM_COVERAGE_MATRIX_W01_W08.md](../../docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md))
menemukan celah **di bawah kontrak baru** (bukan kegagalan terhadap kontrak
saat W2 diterima). Koreksi minimum (format, poin, kesulitan,
kompetensi, dan distribusi posisi kunci tetap; `item_version: '2.0'`):

| Butir | Perubahan | Konsep yang dijamin |
|---|---|---|
| concept s01 vA | L1 `Manajemen proses` → `Kernel`; R3 = definisi kernel | kernel (concept s01) |
| teori s02 vB | opsi c (giliran CPU) dan e (driver) menggantikan memori/antarmuka; kunci a, c, e tetap | manajemen proses, manajemen perangkat |
| teori s05 vA | stem menyebut suntingan belum disimpan; kunci a memuat akibatnya | yang belum disimpan hilang |
| teori s09 vB | opsi b → ekstensi memilih aplikasi pembuka; kunci tetap | ekstensi memilih aplikasi pembuka |
| teori s17 vB | langkah 4 → pulihkan; hasil /tugas 2, /kirim 2; opsi b/d ditukar sehingga kunci tetap b | pulihkan |
| concept s05 vA | urutan pulihkan → periksa → kosongkan Tempat Sampah; satu urutan diterima | periksa sebelum menghapus permanen |
| concept s06 vB | opsi c → akun administrator untuk sehari-hari (salah); kunci tetap | akun biasa vs admin |

Penerimaan W02-ACC tetap tercatat untuk isi yang diterima. Varian yang
diubah di atas **tidak** tercakup penerimaan itu dan memerlukan **review
delta independen** terarah. Register F-01–F-72 tidak berubah.

### Putaran 4 (review `4ddc993`, REQUEST CHANGES) — tindak lanjut D-39

| ID | Tindakan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R3-03 | concept s05 vA (3.0) dan vB (2.0): simulasi; periksa **seluruh** sisa isi Tempat Sampah dan pulihkan yang masih dibutuhkan sebelum mengosongkan; urutan A B C D tetap | CONFIRMED — FIXED | YA | BELUM |
| R3-04 | Bukti "salin mempertahankan asal": teori s17 vA (salin ditolak) tidak sah; dijamin proyek K4.q3 dan teori s15 vA + s17 vB — tanpa perubahan butir | CONFIRMED (bukti) — matriks dikoreksi | YA | BELUM |
| R3-08 | Status penerimaan terstruktur TPL-01a di `module.yaml` → `acceptance` (historis tetap; varian revisi PENDING) | CONFIRMED — FIXED | YA | BELUM |

Register kesetaraan dan cakupan: [CURRICULUM_COVERAGE_MATRIX_W01_W08.md](../../docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md).
Penerimaan W02-ACC tetap historis; varian revisi belum diterima.

### Putaran 5 (review `796043c`, REQUEST CHANGES)

| ID | Tindakan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R4-02 | Validator penerimaan kini membandingkan isi setiap varian dengan `baseline_commit` git (field baru di blok `acceptance`); varian revisi tetap PENDING | CONFIRMED — FIXED | YA | BELUM |
| R4-03 | Bukti "salin mempertahankan asal": proyek K4.q3 dihapus (salin hanya pengecoh); bukti (b) teori s15 vA + s17 vB, berlaku karena VA-2 memberi indeks varian yang sama di semua slot (disimulasikan) | CONFIRMED — FIXED (bukti) | YA | BELUM |

Butir W2 yang diterima tidak diubah pada putaran ini.

