---
module_id: mod-w06
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-2. Belum direview independen; belum diterima owner"
---

# W6 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-2) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review independen (ChatGPT) | **BELUM** |
| Diterima owner | **BELUM** |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim (W6 tanpa runtime; aplikasi belum ada) |
| Durasi diuji dengan pelajar | **TIDAK** |

Acuan struktur: W1–W4 (W01-ACC–W04-ACC), dengan batas review independen
yang diungkapkan tetap berlaku. Isi W6 tidak menyalin isi modul lain.

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah |
|---|---|
| Pelajaran / set latihan | 4 / 4 (40 + 35 + 40 + 35 = 150 menit) |
| Soal teori | **40** (20 slot × 2) |
| Soal concept | **12** (6 slot × 2) |
| Spesifikasi lab | **6** (3 aktivitas × 2 varian) |
| Mini-project | 1 (`spec.md` + `rubric.yaml`, 16 contoh evaluasi) |
| Remedial / review | 1 / 1 |

## 3. Tujuan belajar (6 LO ↔ 6 kompetensi ↔ 6 slot concept)

| LO | Kompetensi | Pelajaran | Teori | Lab | Proyek | Concept |
|---|---|---|---|---|---|---|
| LO1 | `comp-w06-repr-01` | les-01 | s01, s02, s03 | act-01.c08 | K1.c12, K4.q3 | s01 |
| LO2 | `comp-w06-bin2dec-01` | les-01 | s04, s05, s06, s07 | act-01.c01–c04 | K1.c12 | s02 |
| LO3 | `comp-w06-dec2bin-01` | les-02 | s08, s09, s10, s11 | act-01.c05–c08 | F5 (konteks) | s03 |
| LO4 | `comp-w06-ops-01` | les-03 | s12, s13, s14 | act-02.c01–c04, act-03.c01, act-03.c02 | K1.c11, K4.q4 | s04 |
| LO5 | `comp-w06-table-01` | les-03 | s15, s16, s17, s19 | act-02.c05, act-02.c06, act-03.c06 | K1.c01–c08, K1.c10, K4.q1, K4.q5 | s05 |
| LO6 | `comp-w06-model-01` | les-04 | s18, s20 | act-03.c03–c05 | K1.c09, K1.c11, K4.q2 | s06 |

## 4. Skor yang dapat dicapai, durasi, dan XP

| Komponen | Maks. dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori | 56 | **56** | Kunci setiap slot ada di opsi / accepted_answers (validator); D1 8 × 2 + D2 8 × 3 + D3 4 × 4 = 16 + 24 + 16 |
| Lab | 100 | **100** | 30 + 40 + 30; setiap pemeriksaan berkunci tunggal |
| Proyek | 100 | **100** | Contoh E01 dihitung evaluator = 100 |
| Concept | 20 | **20** | Jumlah maksimum slot; CE-S2 maks = jumlah kunci; CE-S3 maks = n − 1 |

Durasi teori (rumus A.4, dihitung ulang dari blueprint W6, bukan
disalin): S = 1665 detik → S_buffer = ⌈S × 11/10⌉ = 1832 →
standar ⌈1832/60⌉ + 2 = **33 menit**; review = 45 − 33 = 12;
TA-B = ⌈33 × 3/2⌉ = 50 (di luar 480). Format: {'TF-1': 7, 'TF-2': 1, 'TF-3': 9, 'TF-4': 2, 'TF-5': 1}; kesulitan {'D1': 8, 'D2': 8, 'D3': 4}
(TP-B 40/40/20). Alokasi HA-A fase 2: M 150 · U 45 · L 120 · P 90 · C 30 ·
R 45 = 480. XP = 305 (13 identitas, katalog sama dengan W1–W4).

Validator (`validate2.py mod-w06`):

```
theory: S=1665 Sb=1832 std=33 review=12 TA-B=50 max=56 formats={'TF-1': 7, 'TF-2': 1, 'TF-3': 9, 'TF-4': 2, 'TF-5': 1}
concept max=20 formats=['CE-S4:4', 'CE-S3:3', 'CE-S5:4', 'CE-S1:4', 'CE-S2:3', 'CE-S2:2']
unique ids=175
key positions (TF-1/TF-4 MC, CE-S1, CE-S5 corr, K4): {'a': 6, 'b': 7, 'c': 8, 'd': 6}
NO ERRORS
```

## 5. Verifikasi independen

Kunci dihitung ulang dengan tiga cara terpisah: (1) asersi di generator
(`gen_w06.py` 22 pernyataan assert/64 perbandingan `==`; `gen_w06_lab.py` 9/18;
`gen_w06_proj.py` 1/4), memakai `int(x, 2)`, `format(n, '0Nb')`, dan
evaluator BX yang mengenumerasi semua kombinasi; (2) `bin_check.py`
mengurai angka **dari teks soal** lalu menghitung ulang biner/desimal dan
aturan panjang BN-6; (3) `bool_check.py` mengurai ekspresi dan nilai input
**dari teks soal** lalu mengevaluasi ulang.

| Pemeriksaan | Hasil teramati |
|---|---|
| Konversi biner ↔ desimal (`bin_check.py`) | butir biner diperiksa 24 ALL OK |
| Evaluasi Boolean dan hitungan baris (`bool_check.py`) | butir Boolean diperiksa 22 ALL OK |
| Bentuk desimal NB-5 (`nb5_check.py`) | ALL OK |
| Kelengkapan tabel kebenaran | Setiap tabel kunci dihasilkan dengan `itertools.product` (2ⁿ baris); s20 dan lab c05: semua opsi pengecoh dibuktikan berbeda pada baris yang disebut di rasional |
| Posisi bit, nol di depan, lebar bit | Posisi dari kanan mulai 0; "tanpa nol di depan" vs "tepat n bit" dinyatakan di setiap soal; hanya tak bertanda (tanpa negatif/overflow) |
| Biner vs desimal vs Boolean | Subskrip ₂/₁₀ di soal; nilai Boolean ditulis 0/1 dengan arti benar/salah (s03, concept s01, proyek F5/K4.q3) |
| Prioritas operator | NOT → AND → OR dinyatakan di Pelajaran 3, spec lab, tata bahasa BX; s16/s17 dan proyek E03 menguji pengaruh kurung |
| Uji tepi tata bahasa BX | `NOT NOT P`, `((P))`, `NOT(P)`, huruf kecil terbaca; `P AND`, kosong, `) P (`, `P OR OR J`, `P AND J M`, `P xor J` tidak terbaca; mode strict menolak huruf kecil |


### 5.1 Evaluator dokumentasi proyek (dihitung, bukan ditulis tangan)

| Contoh | Kasus | K1 | K2 | K3 | Total (K4 = 10) |
|---|---|---|---|---|---|
| E01 | Isian acuan | 60 | 20 | 10 | 100 |
| E02 | F2 = `(P AND M) OR (J AND M)` (ekuivalen, bentuk berbeda) | 60 | 20 | 10 | 100 |
| E03 | F2 = `M AND P OR J` (tanpa kurung → dibaca `(M AND P) OR J`) | 48 | 20 | 10 | 88 |
| E04 | F2 dan F4 huruf kecil (`m and (p or j)`, `not m and (p or j)`) | 60 | 20 | 6 | 96 |
| E05 | F1.R4 = 0 (satu sel salah) | 57 | 20 | 10 | 97 |
| E06 | F2 = `M && (P || J)` (simbol tak dikenal) | 48 | 15 | 6 | 79 |
| E07 | F2 memakai variabel X: `X AND (P OR J)` | 48 | 15 | 6 | 79 |
| E08 | F3 = `3 baris` | 60 | 20 | 7 | 97 |
| E09 | F5 = `110` (ditulis biner, bukan desimal) | 54 | 20 | 10 | 94 |
| E10 | Semua isian kosong | 0 | 0 | 0 | 0 untuk K1–K3 (MR-6); K4 sesuai jawaban |
| E11 | F1.R2 = `benar` (kata, bukan 0/1) | 57 | 14 | 10 | 91 |
| E12 | F2 = `M AND (P OR J` (kurung tidak berpasangan) | 48 | 15 | 6 | 79 |
| E13 | F1 tanpa baris R8 | 57 | 14 | 10 | 91 |
| E14 | F4 = salinan F2 (ekspresi alarm) | 48 | 20 | 10 | 88 |
| E15 | F1 berisi baris tak dikenal R9 = 1 di samping R1–R8 acuan | 60 | 20 | 10 | 100 |
| E16 | Struktur luar F1 rusak (daftar, bukan tabel baris) | 36 | 14 | 10 | 70 |

Prosedur: `sim_w06.py` membaca konstanta dan aturan dari `rubric.yaml`,
memakai evaluator BX untuk ekuivalensi di 8 kombinasi, mengevaluasi 16
submission contoh, dan membandingkan dengan harapan yang dihitung tangan
lebih dulu: semua cocok. Uji mutasi: pemeriksa yang hanya mencoba satu
baris (111) akan keliru menerima E03 (`M AND P OR J`), sehingga pemeriksaan
8 baris memang diperlukan. Ruang solusi: tabel F1 tunggal (1 dari 256);
F2 dan F4 masing-masing satu fungsi Boolean dengan tak hingga penulisan
ekuivalen — semua diterima (E02).

## 6. Matriks kesetaraan varian (QC-04)

| Butir | Konsep wajib | Bukti kesetaraan vA ↔ vB |
|---|---|---|
| s01–s03 | bit/basis; bobot; biner vs desimal vs Boolean | definisi; bobot digit paling kiri (5 vs 7 digit); 3 pernyataan benar dari 5 |
| s04–s07 | biner → desimal | 4 bit; 8 bit dengan nol di depan; 7 bit; satu baris salah pada tabel bobot |
| s08–s11 | desimal → biner, rentang | tanpa nol di depan (4 vs 5 bit); tepat 8 bit; 2ⁿ − 1 vs 2ⁿ (pengecoh saling silang); batas 7 bit |
| s12–s14 | AND/OR/NOT | satu baris AND vs OR; NOT dari kurung; deskripsi operator |
| s15–s17, s19 | tabel kebenaran | 2³ vs 2⁴; satu baris bernilai 1; ekspresi 3 variabel dengan kurung + NOT; 4 langkah dengan kolom bantu |
| s18, s20 | memodelkan, ekuivalensi | "dan" vs "atau"; NOT di depan kurung AND vs OR |
| Concept s01–s06 | sama per slot | pencocokan basis/Boolean; 4 langkah konversi; satu baris konversi 8 bit salah; alasan AND vs OR; 3 pernyataan tabel; 2 ekspresi ekuivalen |
| Lab act-01–03 | sama per pemeriksaan | 8 konversi berpola sama; tabel 2 variabel + hitungan 3 variabel (5 vs 5); evaluasi, pemodelan, ekuivalensi absorpsi, hitungan (3 vs 3) |

## 7. Model sederhana vs kenyataan (QC-05)

| Model W6 | Kenyataan | Tempat disebut |
|---|---|---|
| Hanya bilangan tak bertanda | Komputer juga menyimpan bilangan negatif (mis. komplemen dua) | les-02 §4, module.yaml |
| Lebar bit hanya bila soal menyebut | Perangkat nyata punya lebar tetap dan dapat overflow | les-02 §4 |
| Operator AND/OR/NOT saja | Ada operator lain (XOR, NAND, …) | les-03 §2 |
| Tata bahasa BX dengan kata kunci | Bahasa pemrograman memakai simbol berbeda (`and`, `&&`, …) | les-03 §3, spec proyek |
| Alarm sebagai logika di kertas | Perangkat nyata punya sensor, jeda waktu, dan keamanan lain | spec proyek |

## 8. Tumpang-tindih dan visibilitas (QC-06, QC-11, VC-1–VC-5)

Pemindai V-L (`scan_vl.py mod-w06`): 7 hit, semuanya cocokan **substring**
(mis. `1101` di dalam `11101`); pencarian token persis tidak menemukan
satu pun. Tinjauan manual menemukan dan memperbaiki tumpang-tindih yang
tidak tertangkap pemindai:

| Temuan | Tindakan |
|---|---|
| les-01 contoh `110011₂` = 51 (= s05 vB), latihan `10100₂` (membuka s02 vA), `1111₂` = 15 (= lab c08 vA) | **Diperbaiki** (`111001₂`, `11000₂`, `11100₂`) |
| les-02 latihan 11 → `001011` (membuka s04 vA), tabel 20 = `10100` | **Diperbaiki** (3 → `000011`; 24 = `11000`) |
| les-03 latihan `NOT X AND Y` (= s16 vB) | **Diperbaiki** (`X OR NOT Y`) |
| les-04 contoh terbimbing berstruktur sama dengan ekspresi lampu kuning proyek | **Diperbaiki** (`(R AND NOT S) OR D`) |
| Fakta byte 0–255 dan bobot 128 di pelajaran vs lab c03 (`11111111₂`, `10000000₂`) | **Diperbaiki di lab** (`11110000₂` = 240, `10000001₂` = 129) agar fakta dasar boleh diajarkan |
| Remedial `01100100₂` = 100 (membuka lab c07 vA) | **Diperbaiki** (`01011000₂`) |
| spec proyek: petunjuk "kurung di sekitar pintu atau jendela" | **Diperbaiki** (dibuat umum) |
| Tabel AND/OR/NOT dasar di pelajaran | Diterima: fakta yang diajarkan dan diuji sebagai ingatan/penerapan |

Kunci, pembahasan, rasional, ekspresi acuan, dan contoh evaluasi hanya di
YAML penilai. D-34 dipertahankan.

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
| T-s01 | repr-01 | TF-1 · D1 · 2 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s02 | repr-01 | TF-1 · D1 · 2 | `d` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s03 | repr-01 | TF-2 · D2 · 3 | `a,c,e` / `b,c,d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s04 | bin2dec-01 | TF-3 · D1 · 2 | `11` / `14` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s05 | bin2dec-01 | TF-3 · D1 · 2 | `70` / `51` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s06 | bin2dec-01 | TF-3 · D2 · 3 | `101` / `87` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s07 | bin2dec-01 | TF-4 · D3 · 4 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s08 | dec2bin-01 | TF-3 · D1 · 2 | `1101` / `10011` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s09 | dec2bin-01 | TF-3 · D2 · 3 | `00101101` / `01011010` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s10 | dec2bin-01 | TF-1 · D2 · 3 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s11 | dec2bin-01 | TF-3 · D3 · 4 | `64` / `127` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s12 | ops-01 | TF-1 · D1 · 2 | `a` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s13 | ops-01 | TF-3 · D1 · 2 | `0` / `1` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s14 | ops-01 | TF-1 · D2 · 3 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s15 | table-01 | TF-3 · D2 · 3 | `8` / `16` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s16 | table-01 | TF-4 · D2 · 3 | `c` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s17 | table-01 | TF-3 · D3 · 4 | `0` / `1` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s18 | model-01 | TF-1 · D1 · 2 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s19 | table-01 | TF-5 · D2 · 3 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s20 | model-01 | TF-1 · D3 · 4 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| C-s01 | repr-01 | CE-S4 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s02 | bin2dec-01 | CE-S3 · 3 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s03 | dec2bin-01 | CE-S5 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s04 | ops-01 | CE-S1 · 4 | `b` / `d` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s05 | table-01 | CE-S2 · 3 | `a,b,d` / `b,c,e` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s06 | model-01 | CE-S2 · 2 | `a,b` / `b,c` | A | M | M | A+M | M | A | A | M | A | A |  |
| L-act-01.vA | bin2dec-01, dec2bin-01, repr-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-01.vB | bin2dec-01, dec2bin-01, repr-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vA | ops-01, table-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vB | ops-01, table-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vA | table-01, model-01, ops-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vB | table-01, model-01, ops-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| P (spec+rubrik) | semua LO | MR-A | contoh 16 | A | M | M | S | — | A+S | A+S | — | A | A |  |
| les-01 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-02 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-03 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-04 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| remedial | semua LO | TPL-14 | — | M | M | M | M | — | — | — | — | M | A |  |

## 10. QC-01–QC-12

| QC | Hasil | Bukti |
|---|---|---|
| QC-01 | PASS | §4; E01 = 100 |
| QC-02 | PASS | §5.1 (16/16 dihitung evaluator) |
| QC-03 | PASS | Konversi basis dua arah (biner → desimal, desimal → biner tanpa nol di depan dan tepat n bit) |
| QC-04 | PASS | §6 |
| QC-05 | PASS | §7 |
| QC-06 | PASS setelah perbaikan | §8 |
| QC-07 | PASS | `spec.md` lab dibuat dari `checks.yaml` yang sama; proyek spec ↔ rubrik (variabel, urutan baris, tata bahasa) |
| QC-08 | PASS | BN-6, B01, BX + `normalization_examples`; uji tepi BX |
| QC-09 | PASS | Validator: tidak ada field non-kanonik |
| QC-10 | PASS | Batas: 2ⁿ − 1 vs 2ⁿ (s10), terkecil 7 bit (s11), 8 bit dengan banyak nol di depan (lab c06) |
| QC-11 | PASS | §8 |
| QC-12 | NOT APPLICABLE | Tidak ada satuan data (KB/MB) di W6; byte hanya sebagai 8 bit |

## 11. Regresi F-01–F-72 (penerapan pada modul baru)

Makna dan disposisi historis tidak diubah; tabel ini hanya mencatat
penerapannya pada W6.

| Temuan | Makna historis | Berlaku? | Artefak | Metode | Hasil teramati | Batas |
|---|---|---|---|---|---|---|
| F-01–F-06 | Kebenaran fungsional, penanganan dependensi, batas skor | Berlaku | `project/rubric.yaml` | Setiap isian proyek punya pemeriksaan kebenaran; depends_on eksplisit; kredit independen (MR-2); tanpa gerbang nol global; contoh batas dihitung evaluator | E01–E16 dihitung `sim_w06.py`; kredit independen (E09: hanya c12 hilang) | Evaluator dokumentasi, bukan evaluator produksi |
| F-07–F-08 | Bukti per butir dan visibilitas jawaban | Berlaku | pelajaran, remedial, spec | Matriks bukti per butir (§9); pemindai V-L + tinjauan konteks (§8) | 8 tumpang-tindih diperbaiki (§8); matriks §9 | Pemindai substring; konteks manual |
| F-09–F-23 | Maksimum dapat dicapai, satuan, normalisasi, kesetaraan varian, validasi deterministik, input rusak | Berlaku | semua komponen | Validator struktur (maksimum, poin, kunci, ID); pemeriksa NB-5 / bentuk jawaban; matriks kesetaraan (§6); fixture input rusak | Maksimum 56/100/100/20; 24 butir biner + 22 Boolean dihitung ulang dari teks soal | Kesetaraan dinilai manual |
| F-24–F-27 | Keamanan skill dan bukti aktivasi yang jujur | Berlaku (proses) | `.claude/`, registry | `.claude/`, izin, hooks, allowed-tools, asal skill tidak diubah; V03 tidak diklaim ulang | Tidak ada perubahan | V03 tidak dijalankan ulang |
| F-28–F-48 | Asumsi eksplisit, akurasi akademik, kredit independen, kontrak validitas | Berlaku | stem, spec, rubrik | Asumsi model di stem/spec (§7); konstanta kunci proyek tidak bergantung isian lain; aturan validitas di rubrik | Tak bertanda, lebar bit, prioritas, BX tertulis; kunci proyek dari aturan, bukan dari isian | — |
| F-49–F-59 | Temuan asli yang dipulihkan (asumsi topologi, diagnosis, satuan peka huruf, klasifikasi utama, autentikasi, media, prasyarat urutan, path terpendek, verifikasi salinan, otorisasi, AMN) | Sebagian | BX, spec proyek | Pola yang relevan diperiksa: asumsi skenario eksplisit; jawaban tunggal yang dapat dipertahankan; prasyarat urutan; satuan peka huruf bila ada bit/byte | Kepekaan huruf dinyatakan eksplisit (BX: huruf kecil terbaca, strict huruf besar) — pola F-51; satu jawaban per skenario | Tidak ada satuan bit/byte per detik |
| F-60–F-70 | Akurasi pelajaran, pemilihan varian remedial, konsistensi dokumen | Berlaku | `remedial.md`, dokumen status | Remedial menyebut VA-1–VA-6; angka pelajaran dihitung ulang; dokumen status disinkronkan | VA-1–VA-6 disebut; angka remedial dihitung ulang | — |
| F-71 | Dependensi validitas eksplisit | Berlaku | `project/rubric.yaml` | Setiap depends_on menyebut syarat terbaca/sah isian yang dipakai; evaluator dokumentasi memastikan isian tak terbaca → pemeriksaan terkait 0 | depends_on menyebut "terbaca"; E06/E07/E12: ekspresi tak terbaca → c09, K2.c02, K3.c01 = 0, lainnya tetap | — |
| F-72 | Koleksi rusak dan kredit independen | Berlaku | `project/rubric.yaml` validity | Struktur luar rusak dan ID tak dikenal punya aturan dan fixture | E13 (baris hilang), E15 (baris tak dikenal diabaikan), E16 (F1 bukan tabel → seluruh F1 tak terbaca, 70) | — |

## 12. Batas penilaian objektif dan bukti reviewer

Pemeriksaan membuktikan jawaban cocok dengan fungsi Boolean dan nilai biner yang benar pada skenario fiktif; tidak menguji perangkat nyata dan tidak memvalidasi durasi dengan pelajar. Tata bahasa BX adalah format jawaban konten di bawah EB-4 (D-24); bentuk editor ekspresi di aplikasi belum diputuskan.

| Field | Isi |
|---|---|
| Reviewer / tanggal / basis | Claude (penyusun), 2026-11-24, `main` = `846051f` |
| Temuan terbuka | Tidak ada yang diketahui penyusun; butuh review independen dan penerimaan owner |

Metrik W6 (dari transkrip, perkiraan): panggilan alat ≈ 30; restart worker 1 (dilanjutkan dari berkas, tanpa mengulang); aksi gagal 2 (salah sambung templat `module.yaml` menghasilkan YAML rusak — tertangkap validator; `DM` belum terdefinisi di generator); temuan pemeriksa/tinjauan yang benar 9 (8 tumpang-tindih, 1 bias posisi kunci); checkpoint 1. TOKEN USAGE: **NOT MEASURABLE**.

## Register koreksi PR #28 (review independen: REQUEST CHANGES, SHA `ca73981`)

Ledger otoritatif F-73–F-94 **tidak tersedia** di repositori maupun di PR #28
(komentar/review kosong). Karena itu temuan dicatat dengan ID sementara
`PR28-nn`; nomor F yang disebut owner hanya sebagai "dikaitkan sebelumnya"
dan **belum direkonsiliasi**. F-01–F-72 dan disposisinya tidak diubah.
Status modul tetap: **diproduksi, belum diterima owner**.

| ID sementara | Dikaitkan | Temuan | Disposisi | Bukti / kriteria |
|---|---|---|---|---|
| PR28-02 | F-79 | NB-5: teks "cocokkan persis" bertentangan dengan "huruf satuan bebas" | CONFIRMED — FIXED (kontrak N1–N6) | 70 teks normalisasi + 6 aturan proyek diganti; 37 fixture (termasuk W3 F-51 tak berubah) lolos; contoh positif/negatif di butir |
| PR28-03 | F-89 | BN-6: lab act-01 tanpa pengecualian nol; teori dengan pengecualian | CONFIRMED — FIXED (kontrak) | Teori s08/s09, lab act-01 checks + spec, module.yaml disatukan; 11 fixture lolos; kunci positif yang ada tetap sah |
| PR28-04 | F-77 | BX: NOT berulang dan unary vs binary tidak tertulis eksplisit | DOCUMENTATION CLARIFIED | Tata bahasa formal di rubrik; spec, module, pelajaran 3; 14 fixture lolos (`NOT NOT M` sah, = M); evaluator dokumentasi tidak berubah |
| PR28-05 | F-90 (belum dikonfirmasi) | B01: trim tidak tertulis di lab act-02/03 | DOCUMENTATION CLARIFIED | Lab dan proyek: trim tepi lalu tepat satu digit 0/1; 9 fixture lolos |
| PR28-06 | F-82 | `required_concepts`: sebagian varian tidak menilai setiap konsep slot (W5 concept s01 vA, s04 vB; W6 s03 vB, s04) | OPEN — keputusan owner | TPL-13 mendefinisikan `required_concepts` per slot; VA-1 tidak menyebutnya. Kunci semua benar; butir tidak diubah |
| PR28-07 | F-78/F-92 (deskripsi asli tidak tersedia) | K4 proyek membuka jawaban isian yang masih dapat diedit | CONFIRMED — FIXED (W6 q2–q4, W7 q1–q4, W8 q1–q5) | Soal ditulis ulang ke tingkat konsep; LO, posisi kunci, dan poin K4 tetap; W5 K4 = QUALITY NOTE (rumus definisi dari spesifikasi, bukan nilai jawaban) |
| PR28-09 | — | W6 akademik: nol pada konversi; NOT berulang; "NOT (X OR Y) vs NOT X OR NOT Y: belum tentu"; pembahasan tabel latihan tidak lengkap | CONFIRMED — FIXED | Pelajaran 2–4; pernyataan diganti "tidak ekuivalen" dengan baris pembeda |
| PR28-12 | F-69/F-70 (pola) | Status aktif tidak sinkron (roadmap UW-26/UW-37, PROJECT_MAP §19, header review W2–W4) | CONFIRMED — FIXED | Metadata aktif diperbarui; catatan historis ditandai, tidak dihapus |

Batas: kontrak normalisasi diverifikasi dengan skrip dokumentasi sementara
(tidak di-commit), bukan evaluator produksi atau runtime Android.
Status koreksi: menunggu review delta independen; tidak ada klaim PASS.

### Putaran 2 (review delta REQUEST CHANGES, SHA `9bf2285`)

ID tetap; tidak ada ID baru. Bukti dari `r2_check.py` (skrip dokumentasi sementara).

| ID | Koreksi putaran 2 | Bukti |
|---|---|---|
| PR28-12 | HANDOFF B-10, status D-26–D-35, ringkasan tugas terakhir; PROJECT_MAP R-02 | W1–W4 diterima; W5–W8 menunggu; W9–W16 NOT STARTED; 32/64, 16/64, 32/4/12/3/5 = 56, 32/43 tetap |

### Putaran 3 (keputusan owner D-39, HYBRID COMPETENCY COVERAGE)

ID tetap; tidak ada ID baru. Bukti: `cov_check.py`, `cov_keys.py`, `nb5_full.py` (skrip dokumentasi sementara).

| ID | Hasil | Bukti |
|---|---|---|
| PR28-06 | **RESOLVED (D-39)**: 19/19 PASS; satu celah terbukti diperbaiki (concept s05 vB opsi e: urutan baris standar; kunci b, c, e tetap). Kandidat s03 nilai terbesar → lab act-01.c08 kedua varian; s04 NOT → lab act-02.c01–c04 dan teori s13 kedua varian, proyek K1.c11 | Matriks `docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md` |
| PR28-02 | Tindak lanjut NB-5: termasuk dalam 82 butir W5–W6 — 0 temuan; butir B01/BN-6 dikecualikan dari NB-5 | Matriks `docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md` |

### Putaran 4 (review `4ddc993`, REQUEST CHANGES; temuan sementara R3-01–R3-08)

AUTHOR RESOLVED ≠ INDEPENDENT VERIFIED. PR28-06 **tidak** ditutup independen hanya karena D-39 dicatat.

| ID | Hasil penulis | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|
| R3-01 | QC-13 diperjelas: bukti (a) cukup, bukti deterministik setara (b) juga sah | YA | BELUM |
| R3-02 | Register kesetaraan 48 slot (matriks §6): 44 PASS, 4 OPEN (W1 s03, W4 s01, s03, s06) — butir yang sudah diterima tidak diubah tanpa otorisasi | YA | BELUM |
| R3-03–R3-07 | Lihat `review.md` W2–W4 putaran 4 | YA | BELUM |
| R3-08 | TPL-01a `acceptance` (14 varian W1–W4 PENDING) | YA | BELUM |
| PR28-02 | Paket reproduksi `docs/validation/` (82 konsumen NB-5, 39 fixture, mutasi 5/5) — hasil penulis | YA | BELUM |
| PR28-06 | Cakupan 156/156 PASS menurut data penulis; 0 GAP | YA | BELUM |

### Putaran 5 (review `796043c`, REQUEST CHANGES; temuan sementara R4-01–R4-10)

Baris putaran 4 di atas adalah catatan historis; status aktif di bawah ini. Cakupan dan kesetaraan = **hasil penulis**.

| ID | Hasil penulis | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|
| PR28-06 | **OPEN** (lihat W5) | TIDAK | BELUM |
| R4-04–R4-09 | Kesetaraan W6: 6/6 PASS; s06 sesuai review independen | YA | BELUM |
