---
module_id: mod-w08
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-2. Belum direview independen; belum diterima owner"
---

# W8 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-2) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review independen (ChatGPT) | **BELUM** |
| Diterima owner | **BELUM** |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim (W8 tanpa runtime; aplikasi belum ada) |
| Durasi diuji dengan pelajar | **TIDAK** |

Acuan struktur: W1–W4 (W01-ACC–W04-ACC), dengan batas review independen
yang diungkapkan tetap berlaku. Isi W8 tidak menyalin isi modul lain.

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah |
|---|---|
| Pelajaran / set latihan | 4 / 4 (40 + 35 + 40 + 35 = 150 menit) |
| Soal teori | **40** (20 slot × 2) |
| Soal concept | **12** (6 slot × 2) |
| Spesifikasi lab | **6** (3 aktivitas × 2 varian) |
| Mini-project | 1 (`spec.md` + `rubric.yaml`, 20 contoh evaluasi) |
| Remedial / review | 1 / 1 |

## 3. Tujuan belajar (6 LO ↔ 6 kompetensi ↔ 6 slot concept)

| LO | Kompetensi | Pelajaran | Teori | Lab | Proyek | Concept |
|---|---|---|---|---|---|---|
| LO1 | `comp-w08-algo-01` | les-01 | s01, s02, s03 | act-01.c06 |  | s01 |
| LO2 | `comp-w08-symbol-01` | les-02 | s04, s05, s06, s16 | act-01.c05 | K1.c04, K4.q4 | s02 |
| LO3 | `comp-w08-branch-01` | les-02 | s07, s08, s09 | act-01.c01–c04 | K1.c03, K4.q3 | s03 |
| LO4 | `comp-w08-loop-01` | les-03 | s10, s11, s12, s13 | act-02.c06–c08 | K1.c02, K1.c12, K4.q2 | s04 |
| LO5 | `comp-w08-trace-01` | les-03 | s14, s15, s20 | act-02.c01–c05, act-03.c01–c03 | K1.c05–c09, K4.q5 | s05 |
| LO6 | `comp-w08-correct-01` | les-04 | s17, s18, s19 | act-03.c04–c06 | K1.c01, K1.c10, K1.c11, K4.q1 | s06 |

## 4. Skor yang dapat dicapai, durasi, dan XP

| Komponen | Maks. dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori | 56 | **56** | Kunci setiap slot ada di opsi / accepted_answers (validator); D1 8 × 2 + D2 8 × 3 + D3 4 × 4 = 16 + 24 + 16 |
| Lab | 100 | **100** | 30 + 40 + 30; setiap pemeriksaan berkunci tunggal |
| Proyek | 100 | **100** | Contoh E01 dihitung evaluator = 100 |
| Concept | 20 | **20** | Jumlah maksimum slot; CE-S2 maks = jumlah kunci; CE-S3 maks = n − 1 |

Durasi teori (rumus A.4, dihitung ulang dari blueprint W8, bukan
disalin): S = 1650 detik → S_buffer = ⌈S × 11/10⌉ = 1815 →
standar ⌈1815/60⌉ + 2 = **33 menit**; review = 45 − 33 = 12;
TA-B = ⌈33 × 3/2⌉ = 50 (di luar 480). Format: {'TF-1': 8, 'TF-2': 1, 'TF-4': 2, 'TF-5': 1, 'TF-3': 8}; kesulitan {'D1': 8, 'D2': 8, 'D3': 4}
(TP-B 40/40/20). Alokasi HA-A fase 2: M 150 · U 45 · L 120 · P 90 · C 30 ·
R 45 = 480. XP = 305 (13 identitas, katalog sama dengan W1–W4).

Validator (`validate2.py mod-w08`):

```
theory: S=1650 Sb=1815 std=33 review=12 TA-B=50 max=56 formats={'TF-1': 8, 'TF-2': 1, 'TF-4': 2, 'TF-5': 1, 'TF-3': 8}
concept max=20 formats=['CE-S2:3', 'CE-S4:4', 'CE-S5:4', 'CE-S1:4', 'CE-S3:3', 'CE-S2:2']
unique ids=178
key positions (TF-1/TF-4 MC, CE-S1, CE-S5 corr, K4): {'a': 8, 'b': 7, 'c': 7, 'd': 7}
NO ERRORS
```

## 5. Verifikasi independen

Kunci dihitung ulang secara independen dengan **menjalankan** setiap
algoritma/flowchart sebagai simulasi langkah demi langkah di generator
(`gen_w08.py` 15 pernyataan assert/29 perbandingan `==`; `gen_w08_lab.py`
5/14; `gen_w08_proj.py` 3/5), lalu diperiksa ulang manual dari **teks
soal/fixture**.

| Pemeriksaan | Hasil teramati |
|---|---|
| Penelusuran perulangan dan tabel (s10–s15, s20, lab act-02, act-03, proyek F5–F8) | Disimulasikan; banyak putaran dan banyak pemeriksaan syarat dihitung terpisah |
| Percabangan dan batas (s07–s09, lab act-01) | Disimulasikan termasuk nilai tepat di batas |
| Isian blok proyek F1–F4 | **Enumerasi semua 4⁴ = 256 kombinasi** dengan interpreter **tingkat-blok** (mengikuti kolom "Berikutnya" blok demi blok) pada 14 daftar uji (negatif, positif, campuran, nilai sama, satu nilai): tepat **2** kombinasi benar (F1 b, F2 b, F3 `>` atau `≥`, F4 **b** = kembali ke B4); keduanya diterima. *Koreksi PR #28:* kunci F4 semula `c` (B5) akibat simulator generator yang salah memetakan target lompatan; F4 = c melewati penjaga B4 dan mengakses A[n + 1] |
| Jawaban tunggal yang dapat dipertahankan | Bentuk simbol (s04–s06) mengikuti tabel simbol yang diajarkan; domain (s03) dibatasi pada pembagi; urutan blok (s16) hanya satu urutan sah |
| Bentuk angka NB-5 (`nb5_check.py`) | ALL OK |


### 5.1 Evaluator dokumentasi proyek (dihitung, bukan ditulis tangan)

| Contoh | Kasus | K1 | K2 | K3 | Total (K4 = 10) |
|---|---|---|---|---|---|
| E01 | Isian acuan (F3 = a, `>`) | 60 | 20 | 10 | 100 |
| E02 | F3 = d (`≥`), lainnya acuan | 60 | 20 | 10 | 100 |
| E03 | F1 = a (`maks ← 0`) | 54 | 20 | 10 | 94 |
| E04 | F2 = a (`i < n?`) | 54 | 20 | 10 | 94 |
| E05 | F4 = a (kembali ke B3) | 54 | 20 | 10 | 94 |
| E06 | F5.i2 = `-7` (lupa mengganti maks) | 56 | 20 | 10 | 96 |
| E07 | F6 = `0` (menelusuri dengan nilai awal 0) | 54 | 20 | 10 | 94 |
| E08 | F5 ditulis `maks = …` | 60 | 20 | 6 | 96 |
| E09 | F8 = `5` (pemeriksaan terakhir tidak dihitung) | 55 | 20 | 10 | 95 |
| E10 | F8 = `6 kali` | 60 | 20 | 7 | 97 |
| E11 | Semua isian kosong | 0 | 0 | 0 | 0 untuk K1–K3 (MR-6); K4 sesuai jawaban |
| E12 | F3 = `e` (di luar a–d) | 54 | 18 | 10 | 92 |
| E13 | F5.i4 = `5,0` (desimal) | 56 | 14 | 6 | 86 |
| E14 | F5 tanpa baris i6 | 56 | 14 | 6 | 86 |
| E15 | F5 berisi baris tak dikenal i9 di samping i2–i6 acuan | 60 | 20 | 10 | 100 |
| E16 | Struktur luar F5 rusak (daftar, bukan tabel baris) | 40 | 14 | 6 | 70 |
| E17 | F6 memakai tanda minus `−` (U+2212) | 60 | 20 | 10 | 100 |
| E18 | F4 = c (kembali ke B5: melewati penjaga B4, A[n + 1] di luar daftar) | 54 | 20 | 10 | 94 |
| E19 | F4 = d (kembali ke B9: keluar setelah satu putaran) | 54 | 20 | 10 | 94 |
| E20 | F4 = `e` (di luar a–d) | 54 | 18 | 10 | 92 |

Prosedur: `sim_w08.py` membaca konstanta, pilihan blok, fixture, dan aturan
skor dari `rubric.yaml`, menjalankan flowchart acuan, mengevaluasi 20
submission contoh, dan membandingkan dengan harapan yang dihitung tangan
lebih dulu: semua cocok. Evaluator juga menurunkan ulang kunci F1–F8 dari
interpreter tingkat-blok independen (`w08_blocks.py`), bukan dari salinan
kunci rubrik. E18–E20 (F4 = c, d, `e`) ditambahkan pada koreksi PR #28.
Uji mutasi: pemeriksa yang hanya menerima F3 = a
(`>`) memberi E02 (F3 = d, `≥`) skor 94 alih-alih 100 — tertangkap; karena
itu alternatif setara ditulis eksplisit di rubrik. Ruang solusi bernilai
penuh: 2 kombinasi blok. F5–F8 dinilai terhadap flowchart acuan, bukan
terhadap pilihan blok pelajar (MR-2, tanpa kesalahan berantai).

## 6. Matriks kesetaraan varian (QC-04)

| Butir | Konsep wajib | Bukti kesetaraan vA ↔ vB |
|---|---|---|
| s01–s03 | peran input/output; domain; ciri algoritma | peran data dalam algoritma sehari-hari; pembagi tidak boleh 0; pernyataan benar tentang algoritma |
| s04–s06, s16 | simbol; urutan blok | satu simbol per butir; 5 blok, satu urutan sah |
| s07–s09 | percabangan tunggal; bertingkat; langkah bersyarat berurutan | satu keputusan dekat batas; aturan bertingkat; tiga langkah bersyarat |
| s10–s13 | putaran, tidak berhenti, akumulator, perulangan bersyarat | batas 6 vs 9 (6 vs 7 putaran); langkah +1 vs +2; 5 putaran di kedua varian s13 |
| s14, s15, s20 | penelusuran 4 langkah; ulangi 4 kali; hitung bersyarat | struktur identik, angka berbeda |
| s17–s19 | nilai awal; kasus uji pengungkap; posisi nilai sama | jumlah vs perkalian; `kecil ← 0` vs `kecil ← 100`; s19 vA `<` (posisi pertama) vs vB `≤` (posisi terakhir) — operator berbeda, keterampilan penelusuran sama |
| Concept s01–s06 | sama per slot | domain; pencocokan bentuk; catatan penelusuran salah; perubahan pengendali; urutan baris tabel; nilai awal/kasus uji |
| Lab act-01 | tabel blok bercabang | vA tarif parkir (3 cabang), vB harga tiket (3 cabang); 4 penelusuran + bentuk + domain |
| Lab act-02–03 | penelusuran perulangan; nilai terkecil | struktur sama per pemeriksaan; fixture berbeda (termasuk negatif dan nilai sama) |

## 7. Model sederhana vs kenyataan (QC-05)

| Model W8 | Kenyataan | Tempat disebut |
|---|---|---|
| Flowchart sebagai tabel blok bernomor | Flowchart nyata digambar; banyak gambar setara | les-02 §2, `module.yaml` |
| Notasi `←`, `A[i]` mulai 1 | Python (W9+) memakai `=` dan indeks mulai 0 | les-01 §2, `module.yaml` notation |
| Input di luar domain "tidak dijamin" | Aplikasi nyata memvalidasi input | les-01 §3, lab act-01 c06 |

## 8. Tumpang-tindih dan visibilitas (QC-06, QC-11, VC-1–VC-5)

Pemindai V-L (`scan_vl.py mod-w08`): 10 hit, semuanya substring atau
**konstanta blok** fixture lab act-01 (mis. `biaya ← 5000`, `harga ← 25000`)
yang memang harus terlihat agar flowchart dapat ditelusuri, atau substring
angka contoh pelajaran (150000/200000/250000). Tinjauan manual:

| Temuan | Tindakan |
|---|---|
| Lab act-03 c06 semula membuka jawaban proyek (banyak pemeriksaan pada daftar maksimum) | **Diperbaiki**: diganti "banyak pemeriksaan B4" untuk fixture lab sendiri |
| K4 proyek semula membuka/menunjuk jawaban F1, F2, F3, F4, F7, F8 (PR #28) | **Diperbaiki**: kelima soal K4 ditulis ulang ke tingkat konsep (kasus uji, kemajuan perulangan, alur B5, simbol, tabel penelusuran); LO, kunci a–d, dan poin tetap |
| Latihan les-03 no. 3 sama struktur dan jawaban dengan s12 vA | **Diperbaiki**: diganti perulangan perkalian (output 8) |
| Latihan les-04 no. 3 sama pola dengan s18 vA | **Diperbaiki**: diganti kasus uji algoritma perkalian |
| les-04 §1 mengajarkan mengapa `kecil ← 0` salah | Diterima sebagai materi inti LO6 (metode); butir s18 tetap menuntut memilih di antara 4 daftar |
| les-04 §3 mengajarkan `<` posisi pertama / `≤` posisi terakhir (s19 menuntut penelusuran daftar) | Diterima sebagai metode; daftar dan jawaban s19 tidak muncul di pelajaran |
| les-04 mengajarkan algoritma nilai **terkecil**; proyek nilai **terbesar** | Diterima: proyek menuntut transfer ke kebalikannya dengan fixture berbeda |

Kunci, pembahasan, dan contoh evaluasi hanya di YAML penilai. D-34
dipertahankan.

## 9. Matriks bukti per butir

Kolom 1–10: 1 kompetensi/LO · 2 akurasi akademik · 3 asumsi eksplisit ·
4 kunci benar dan tunggal · 5 pengecoh sah · 6 skor deterministik ·
7 maksimum tercapai · 8 kesetaraan varian · 9 umpan balik · 10 visibilitas.
**A** = diperiksa otomatis (validator struktur, pemindai); **S** = jawaban
dihitung ulang independen (asersi generator, evaluator, pemeriksa bentuk);
**M** = dibaca manual penyusun; — = tidak berlaku. Ini review mandiri,
bukan review independen.

| Butir | Komp. | Format · D | Kunci vA / vB | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Koreksi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-s01 | algo-01 | TF-1 · D1 · 2 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s02 | algo-01 | TF-1 · D2 · 3 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s03 | algo-01 | TF-2 · D1 · 2 | `a,b,d` / `b,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s04 | symbol-01 | TF-1 · D1 · 2 | `d` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s05 | symbol-01 | TF-1 · D1 · 2 | `a` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s06 | symbol-01 | TF-4 · D2 · 3 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s07 | branch-01 | TF-3 · D1 · 2 | `57` / `10` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s08 | branch-01 | TF-4 · D2 · 3 | `b` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s09 | branch-01 | TF-3 · D3 · 4 | `4` / `16` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s10 | loop-01 | TF-3 · D1 · 2 | `6` / `7` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s11 | loop-01 | TF-1 · D2 · 3 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s12 | loop-01 | TF-3 · D2 · 3 | `10` / `20` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s13 | loop-01 | TF-3 · D3 · 4 | `5` / `5` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s14 | trace-01 | TF-3 · D1 · 2 | `5` / `13` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s15 | trace-01 | TF-3 · D2 · 3 | `31` / `122` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s16 | symbol-01 | TF-5 · D2 · 3 | `A,B,C,D,E` / `A,B,C,D,E` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s17 | correct-01 | TF-1 · D1 · 2 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s18 | correct-01 | TF-1 · D2 · 3 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s19 | correct-01 | TF-1 · D3 · 4 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s20 | trace-01 | TF-3 · D3 · 4 | `13` / `3` | A | M | M | A+S | — | A | A | M | A | A |  |
| C-s01 | algo-01 | CE-S2 · 3 | `a,b,c` / `a,c,d` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s02 | symbol-01 | CE-S4 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s03 | branch-01 | CE-S5 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s04 | loop-01 | CE-S1 · 4 | `b` / `d` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s05 | trace-01 | CE-S3 · 3 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s06 | correct-01 | CE-S2 · 2 | `a,c` / `b,c` | A | M | M | A+M | M | A | A | M | A | A |  |
| L-act-01.vA | symbol-01, branch-01, algo-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-01.vB | symbol-01, branch-01, algo-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vA | loop-01, trace-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vB | loop-01, trace-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vA | correct-01, trace-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vB | correct-01, trace-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| P (spec+rubrik) | semua LO | MR-A | contoh 20 | A | M | M | S | — | A+S | A+S | — | A | A |  |
| les-01 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-02 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-03 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-04 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| remedial | semua LO | TPL-14 | — | M | M | M | M | — | — | — | — | M | A |  |

## 10. QC-01–QC-12

| QC | Hasil | Bukti |
|---|---|---|
| QC-01 | PASS | §4; E01 = 100 |
| QC-02 | PASS | §5.1 (20/20 dihitung evaluator; kunci diturunkan ulang dari interpreter tingkat-blok) |
| QC-03 | NOT APPLICABLE | Tidak ada konversi satuan |
| QC-04 | PASS | §6 |
| QC-05 | PASS | §7 |
| QC-06 | PASS setelah perbaikan | §8 |
| QC-07 | PASS | `spec.md` lab dibuat dari `checks.yaml` (termasuk fixture tabel blok); proyek spec ↔ rubrik |
| QC-08 | PASS | Normalisasi NB-5 untuk bilangan negatif (− atau -), huruf pilihan, bentuk `maks = …` |
| QC-09 | PASS | Validator |
| QC-10 | PASS | Batas: nilai tepat di batas (lab act-01), perulangan 0 kali, pemeriksaan terakhir bernilai Tidak (F8), nilai sama (F3 alternatif) |
| QC-11 | PASS | §8 |
| QC-12 | NOT APPLICABLE | Tidak ada satuan data |

## 11. Regresi F-01–F-72 (penerapan pada modul baru)

Makna dan disposisi historis tidak diubah; tabel ini hanya mencatat
penerapannya pada W8.

| Temuan | Makna historis | Berlaku? | Artefak | Metode | Hasil teramati | Batas |
|---|---|---|---|---|---|---|
| F-01–F-06 | Kebenaran fungsional, penanganan dependensi, batas skor | Berlaku | `project/rubric.yaml` | Setiap isian proyek punya pemeriksaan kebenaran; depends_on eksplisit; kredit independen (MR-2); tanpa gerbang nol global; contoh batas dihitung evaluator | E01–E20 dihitung `sim_w08.py`; kredit independen F5–F8 terhadap flowchart acuan | Evaluator dokumentasi |
| F-07–F-08 | Bukti per butir dan visibilitas jawaban | Berlaku | pelajaran, spec | Matriks bukti per butir (§9); pemindai V-L + tinjauan konteks (§8) | 10 hit pemindai = konstanta/substring; 3 tumpang-tindih diperbaiki | Konteks dinilai manual |
| F-09–F-23 | Maksimum dapat dicapai, satuan, normalisasi, kesetaraan varian, validasi deterministik, input rusak | Berlaku | semua komponen | Validator struktur (maksimum, poin, kunci, ID); pemeriksa NB-5 / bentuk jawaban; matriks kesetaraan (§6); fixture input rusak | Maksimum 56/100/100/20; 256 kombinasi blok dienumerasi | Kesetaraan dinilai manual |
| F-24–F-27 | Keamanan skill dan bukti aktivasi yang jujur | Berlaku (proses) | `.claude/`, registry | `.claude/`, izin, hooks, allowed-tools, asal skill tidak diubah; V03 tidak diklaim ulang | Tidak ada perubahan | V03 tidak dijalankan ulang |
| F-28–F-48 | Asumsi eksplisit, akurasi akademik, kredit independen, kontrak validitas | Berlaku | stem, spec, rubrik | Asumsi model di stem/spec (§7); konstanta kunci proyek tidak bergantung isian lain; aturan validitas di rubrik | Domain input n ≥ 1, penomoran mulai 1, arti `←` tertulis eksplisit | — |
| F-49–F-59 | Temuan asli yang dipulihkan (asumsi topologi, diagnosis, satuan peka huruf, klasifikasi utama, autentikasi, media, prasyarat urutan, path terpendek, verifikasi salinan, otorisasi, AMN) | Berlaku | proyek F1–F4, s16 | Pola yang relevan diperiksa: asumsi skenario eksplisit; jawaban tunggal yang dapat dipertahankan; prasyarat urutan; satuan peka huruf bila ada bit/byte | Pola F-37/F-55 (semua jawaban sah diterima) diterapkan pada F3 `>`/`≥` | — |
| F-60–F-70 | Akurasi pelajaran, pemilihan varian remedial, konsistensi dokumen | Berlaku | `remedial.md`, dokumen status | Remedial menyebut VA-1–VA-6; angka pelajaran dihitung ulang; dokumen status disinkronkan | VA-1–VA-6 disebut | — |
| F-71 | Dependensi validitas eksplisit | Berlaku | `project/rubric.yaml` | Setiap depends_on menyebut syarat terbaca/sah isian yang dipakai; evaluator dokumentasi memastikan isian tak terbaca → pemeriksaan terkait 0 | Isian tak terbaca → hanya pemeriksaan yang membutuhkannya 0 (E12–E14, E16) | — |
| F-72 | Koleksi rusak dan kredit independen | Berlaku | `project/rubric.yaml` validity | Struktur luar rusak dan ID tak dikenal punya aturan dan fixture | E11 (centang tanpa isian → hanya K4), E16 (F5 bukan lima bilangan → 70) | — |

## 12. Batas penilaian objektif dan bukti reviewer

Pemeriksaan membuktikan pilihan blok dan penelusuran sesuai flowchart acuan pada fixture tertulis. Menggambar flowchart bebas tidak dinilai otomatis (format editor flowchart M-10 tetap OPEN; tanpa evaluator graf, tanpa penilaian subjektif atau AI).

| Field | Isi |
|---|---|
| Reviewer / tanggal / basis | Claude (penyusun), 2026-11-24, `main` = `846051f` |
| Temuan terbuka | Tidak ada yang diketahui penyusun; butuh review independen dan penerimaan owner |

Metrik W8 (dari transkrip, perkiraan): panggilan alat ≈ 30; aksi gagal 0; temuan tinjauan yang benar 3 (tumpang-tindih lab act-03 c06, latihan les-03, latihan les-04) plus koreksi hitungan asersi review W6 (67/19 → 64/18); restart worker 1; checkpoint 1. TOKEN USAGE: **NOT MEASURABLE**.

## Register koreksi PR #28 (review independen: REQUEST CHANGES, SHA `ca73981`)

Ledger otoritatif F-73–F-94 **tidak tersedia** di repositori maupun di PR #28
(komentar/review kosong). Karena itu temuan dicatat dengan ID sementara
`PR28-nn`; nomor F yang disebut owner hanya sebagai "dikaitkan sebelumnya"
dan **belum direkonsiliasi**. F-01–F-72 dan disposisinya tidak diubah.
Status modul tetap: **diproduksi, belum diterima owner**.

| ID sementara | Dikaitkan | Temuan | Disposisi | Bukti / kriteria |
|---|---|---|---|---|
| PR28-01 | F-76 | W8 proyek: kunci F4 = `c` (B5) salah; seharusnya `b` (B4). Akar: simulator generator memetakan target lompatan bergeser | CONFIRMED — FIXED | Kunci, K1.c04, reference_strict, analisis solusi diperbaiki; interpreter tingkat-blok: 256 kombinasi → 2 benar (F4 = b); F4 b/a/c/d/e = 100/94/94/94/92 (E01, E05, E18–E20) |
| PR28-02 | F-79 | NB-5: teks "cocokkan persis" bertentangan dengan "huruf satuan bebas" | CONFIRMED — FIXED (kontrak N1–N6) | 70 teks normalisasi + 6 aturan proyek diganti; 37 fixture (termasuk W3 F-51 tak berubah) lolos; contoh positif/negatif di butir |
| PR28-07 | F-78/F-92 (deskripsi asli tidak tersedia) | K4 proyek membuka jawaban isian yang masih dapat diedit | CONFIRMED — FIXED (W6 q2–q4, W7 q1–q4, W8 q1–q5) | Soal ditulis ulang ke tingkat konsep; LO, posisi kunci, dan poin K4 tetap; W5 K4 = QUALITY NOTE (rumus definisi dari spesifikasi, bukan nilai jawaban) |
| PR28-11 | — | W8 akademik: syarat tidak berhenti; nilai akhir vs output; "0 hanya untuk menjumlah" bertentangan dengan penghitung; prasyarat daftar tidak kosong | CONFIRMED — FIXED | Pelajaran 3 dan 4 |
| PR28-12 | F-69/F-70 (pola) | Status aktif tidak sinkron (roadmap UW-26/UW-37, PROJECT_MAP §19, header review W2–W4) | CONFIRMED — FIXED | Metadata aktif diperbarui; catatan historis ditandai, tidak dihapus |

Batas: kontrak normalisasi diverifikasi dengan skrip dokumentasi sementara
(tidak di-commit), bukan evaluator produksi atau runtime Android.
Status koreksi: menunggu review delta independen; tidak ada klaim PASS.

### Putaran 2 (review delta REQUEST CHANGES, SHA `9bf2285`)

ID tetap; tidak ada ID baru. Bukti dari `r2_check.py` (skrip dokumentasi sementara).

| ID | Koreksi putaran 2 | Bukti |
|---|---|---|
| PR28-11 | W8 pelajaran 3 latihan 3: nilai akhir t = 8, k = 4; tidak ada output | Telusur independen: 3 putaran, 4 pemeriksaan, t = 8, k = 4; konsisten dengan §2 |
| PR28-12 | HANDOFF B-10, status D-26–D-35, ringkasan tugas terakhir; PROJECT_MAP R-02 | W1–W4 diterima; W5–W8 menunggu; W9–W16 NOT STARTED; 32/64, 16/64, 32/4/12/3/5 = 56, 32/43 tetap |

### Putaran 3 (keputusan owner D-39, HYBRID COMPETENCY COVERAGE)

ID tetap; tidak ada ID baru. Bukti: `cov_check.py`, `cov_keys.py`, `nb5_full.py` (skrip dokumentasi sementara).

| ID | Hasil | Bukti |
|---|---|---|
| PR28-06 | **RESOLVED (D-39)**: 19/19 PASS tanpa perubahan | Matriks `docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md` |
