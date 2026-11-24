---
module_id: mod-w07
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-2. Belum direview independen; belum diterima owner"
---

# W7 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-2) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review independen (ChatGPT) | **BELUM** |
| Diterima owner | **BELUM** |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim (W7 tanpa runtime; aplikasi belum ada) |
| Durasi diuji dengan pelajar | **TIDAK** |

Acuan struktur: W1–W4 (W01-ACC–W04-ACC), dengan batas review independen
yang diungkapkan tetap berlaku. Isi W7 tidak menyalin isi modul lain.

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
| LO1 | `comp-w07-decomp-01` | les-01 | s01, s02, s03 | act-01.c01–c03 | K1.c01–c08, K4.q1 | s01 |
| LO2 | `comp-w07-pattern-01` | les-02 | s04, s05, s06, s07 | act-02.c01–c08 | K1.c10, K4.q4 | s02 |
| LO3 | `comp-w07-abstract-01` | les-03 | s08, s09, s10 |  | K1.c11, K4.q3 | s03 |
| LO4 | `comp-w07-algo-01` | les-04 | s11, s12, s13 | act-03.c01, act-03.c02 | K1.c12, K1.c13 | s04 |
| LO5 | `comp-w07-order-01` | les-01 | s14, s15, s16 | act-01.c04–c06 | K1.c09, K4.q2 | s05 |
| LO6 | `comp-w07-test-01` | les-04 | s17, s18, s19, s20 | act-03.c03–c06 | K4.q5 | s06 |

## 4. Skor yang dapat dicapai, durasi, dan XP

| Komponen | Maks. dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori | 56 | **56** | Kunci setiap slot ada di opsi / accepted_answers (validator); D1 8 × 2 + D2 8 × 3 + D3 4 × 4 = 16 + 24 + 16 |
| Lab | 100 | **100** | 30 + 40 + 30; setiap pemeriksaan berkunci tunggal |
| Proyek | 100 | **100** | Contoh E01 dihitung evaluator = 100 |
| Concept | 20 | **20** | Jumlah maksimum slot; CE-S2 maks = jumlah kunci; CE-S3 maks = n − 1 |

Durasi teori (rumus A.4, dihitung ulang dari blueprint W7, bukan
disalin): S = 1650 detik → S_buffer = ⌈S × 11/10⌉ = 1815 →
standar ⌈1815/60⌉ + 2 = **33 menit**; review = 45 − 33 = 12;
TA-B = ⌈33 × 3/2⌉ = 50 (di luar 480). Format: {'TF-1': 9, 'TF-2': 2, 'TF-3': 6, 'TF-4': 2, 'TF-5': 1}; kesulitan {'D1': 8, 'D2': 8, 'D3': 4}
(TP-B 40/40/20). Alokasi HA-A fase 2: M 150 · U 45 · L 120 · P 90 · C 30 ·
R 45 = 480. XP = 305 (13 identitas, katalog sama dengan W1–W4).

Validator (`validate2.py mod-w07`):

```
theory: S=1650 Sb=1815 std=33 review=12 TA-B=50 max=56 formats={'TF-1': 9, 'TF-2': 2, 'TF-3': 6, 'TF-4': 2, 'TF-5': 1}
concept max=20 formats=['CE-S2:3', 'CE-S5:4', 'CE-S1:4', 'CE-S4:4', 'CE-S3:3', 'CE-S2:2']
unique ids=177
key positions (TF-1/TF-4 MC, CE-S1, CE-S5 corr, K4): {'a': 7, 'b': 7, 'c': 9, 'd': 8}
NO ERRORS
```

## 5. Verifikasi independen

Kunci dihitung ulang secara independen: asersi di generator
(`gen_w07.py` 8 pernyataan assert/16 perbandingan; `gen_w07_lab.py` 4/6;
`gen_w07_proj.py` 3/4), enumerasi **semua permutasi** untuk urutan valid
(`ctlib.valid_orders`), dan pemeriksaan ulang urutan lab dari **teks
prasyarat fixture** (vA 2 urutan, vB 4 urutan — sama dengan kunci).

| Pemeriksaan | Hasil teramati |
|---|---|
| Urutan valid teori (s15, s16), concept s05, lab act-01, proyek F2 | Dienumerasi dari prasyarat; proyek 6 dari 8! = 40.320 permutasi |
| Pola (s04–s07, lab act-02, proyek F3) | Asersi aritmetika; pola berulang memakai sisa bagi dengan periode |
| Jawaban tunggal yang dapat dipertahankan | Dekomposisi (s03, concept s01) dibatasi oleh **kebutuhan yang disebutkan**; kelompok tugas ditentukan oleh **hasil tertulis** (lab act-01, proyek F1); relevansi (s09, proyek F4) dibatasi oleh aturan "mengubah hasil/jadwal" |
| Alternatif sah | Diterima eksplisit: semua urutan valid; CE-S3 s05 dua urutan; dua ekspresi ekuivalen tidak relevan di W7 |
| Bentuk angka NB-5 (`nb5_check.py`) | ALL OK |


### 5.1 Evaluator dokumentasi proyek (dihitung, bukan ditulis tangan)

| Contoh | Kasus | K1 | K2 | K3 | Total (K4 = 10) |
|---|---|---|---|---|---|
| E01 | Isian acuan (urutan valid pertama) | 60 | 20 | 10 | 100 |
| E02 | F2 = urutan valid lain `T1 T8 T3 T4 T2 T5 T6 T7` | 60 | 20 | 10 | 100 |
| E03 | F2 = `T1 T2 T8 T3 T5 T4 T6 T7` (T2 sebelum T8: melanggar prasyarat) | 48 | 20 | 10 | 88 |
| E04 | F2 tanpa T7 (7 ID) | 48 | 15 | 10 | 83 |
| E05 | F2 dengan T5 dua kali | 48 | 15 | 10 | 83 |
| E06 | F4 = {I1, I2, I3, I4, I5} (satu tidak relevan ikut dipilih) | 58 | 20 | 10 | 98 |
| E07 | F4 = {I1, I2} (dua relevan terlewat) | 56 | 20 | 10 | 96 |
| E08 | F4 = {I5, I6, I7} (semua tidak relevan) | 52 | 20 | 10 | 92 |
| E09 | F4 berisi ID tak dikenal I9 | 52 | 16 | 10 | 88 |
| E10 | F1.T1 = `R` (salah kelompok) | 57 | 20 | 10 | 97 |
| E11 | F1 huruf kecil semua | 60 | 20 | 7 | 97 |
| E12 | F6 = `4` (300 ÷ 70 dibulatkan ke bawah) | 55 | 20 | 10 | 95 |
| E13 | F5 = `300 menit`, F6 = `5 hari` | 60 | 20 | 6 | 96 |
| E14 | Semua isian kosong | 0 | 0 | 0 | 0 untuk K1–K3 (MR-6); K4 sesuai jawaban |
| E15 | F2 memakai koma dan huruf kecil `t1, t8, t2, t3, t4, t5, t6, t7` | 60 | 20 | 10 | 100 |
| E16 | Struktur luar F1 rusak (daftar, bukan tabel tugas) | 36 | 15 | 7 | 68 |

Prosedur: `sim_w07.py` membaca konstanta, prasyarat, dan aturan skor dari
`rubric.yaml`, mengevaluasi 16 submission contoh, dan membandingkan dengan
harapan yang dihitung tangan lebih dulu: semua cocok. Evaluator juga
mengenumerasi ulang semua permutasi T1–T8 (6 valid, sama dengan kunci).
Uji mutasi: pemeriksa yang hanya mengecek satu prasyarat menerima E03
(T2 sebelum T8) dengan skor 100 alih-alih 88 — tertangkap. Ruang solusi
bernilai penuh: 6 (hanya F2 yang punya alternatif). F4 memakai skor bersih
pola CE-S2 (tidak pernah negatif).

## 6. Matriks kesetaraan varian (QC-04)

| Butir | Konsep wajib | Bukti kesetaraan vA ↔ vB |
|---|---|---|
| s01–s03 | definisi dan contoh dekomposisi; ciri; lengkap tanpa tumpang-tindih | 3 kebutuhan, 4 opsi dengan pengecoh "hilang", "tumpang-tindih", "belum dipecah" |
| s04–s07 | pola tetap, suku ke-n, perulangan, pola tak linear | beda +3 vs −5; n = 10 vs 8; pola instruksi berulang; kuadrat vs berlipat |
| s08–s10 | definisi/contoh abstraksi; relevan; generalisasi | 3 relevan dari 5; angka khusus → variabel |
| s11–s13 | ciri algoritma; langkah ambigu; menelusuri | 4 langkah operasi dasar |
| s14–s16 | urutan tunggal; urutan tidak valid; banyak urutan | 4 langkah berantai; satu pelanggaran; 6 urutan di kedua varian (struktur berbeda) |
| s17–s20 | kasus uji; pengungkap kesalahan; batas; hasil langkah salah | kesalahan pada langkah "selain itu"; batas ≥ vs >; satu hitungan |
| Concept s01–s06 | sama per slot | 3 kebutuhan; baris pola salah; alasan abstraksi; 4 penilaian instruksi; 2 urutan diterima; > vs ≥ |
| Lab act-01 | kelompok, urutan, banyak urutan, bersamaan | vA 2 urutan, vB 4 urutan: struktur setara (satu pasangan/satu tugas bebas), hitungan sedikit berbeda — dicatat sebagai batas kesetaraan |
| Lab act-02–03 | pola; algoritma dan pengujian | struktur sama per pemeriksaan |

## 7. Model sederhana vs kenyataan (QC-05)

| Model W7 | Kenyataan | Tempat disebut |
|---|---|---|
| Kelompok tugas ditentukan oleh hasil tertulis | Di dunia nyata pengelompokan dapat berbeda dan didiskusikan | les-01 §2, spec |
| Lama tugas tetap dan tugas boleh dilanjutkan hari berikutnya | Lama nyata berubah; ada tugas yang tidak dapat dipotong | spec proyek F6 |
| Pola bertambah tetap untuk perkiraan data | Data nyata tidak selalu mengikuti pola | spec proyek F3 ("menurut pola") |
| Satu dekomposisi dinilai terhadap kebutuhan yang disebut | Ada banyak dekomposisi yang sama baiknya | les-01 §2, s03 |

## 8. Tumpang-tindih dan visibilitas (QC-06, QC-11, VC-1–VC-5)

Pemindai V-L (`scan_vl.py mod-w07`): 0 hit. Tinjauan manual:

| Temuan | Tindakan |
|---|---|
| Proyek: T1 "membaca panduan" dapat dikira Riset bacaan | **Diperbaiki**: hasil T1 = kesepakatan kelompok; definisi R dipersempit ke sumber bacaan topik |
| Contoh pelajaran (urutan A–E, pola 3, 8, 13, aturan ≥ 120) | Berbeda dari butir bernilai; mengajarkan metode, bukan jawaban |
| Contoh terlihat lab act-01 ("membeli spidol → Barang") | Diterima: contoh bentuk untuk proyek lain; arti kode sudah tertulis di fixture |

Kunci, urutan valid, pembahasan, dan contoh evaluasi hanya di YAML penilai.
D-34 dipertahankan.

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
| T-s01 | decomp-01 | TF-1 · D1 · 2 | `b` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s02 | decomp-01 | TF-2 · D1 · 2 | `a,c,d` / `b,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s03 | decomp-01 | TF-1 · D2 · 3 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s04 | pattern-01 | TF-3 · D1 · 2 | `16` / `30` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s05 | pattern-01 | TF-3 · D2 · 3 | `41` / `52` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s06 | pattern-01 | TF-1 · D2 · 3 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s07 | pattern-01 | TF-3 · D3 · 4 | `144` / `192` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s08 | abstract-01 | TF-1 · D1 · 2 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s09 | abstract-01 | TF-2 · D2 · 3 | `a,c,e` / `a,c,d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s10 | abstract-01 | TF-1 · D3 · 4 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s11 | algo-01 | TF-1 · D1 · 2 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s12 | algo-01 | TF-4 · D2 · 3 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s13 | algo-01 | TF-3 · D1 · 2 | `1` / `20` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s14 | order-01 | TF-5 · D1 · 2 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s15 | order-01 | TF-1 · D2 · 3 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s16 | order-01 | TF-3 · D3 · 4 | `6` / `6` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s17 | test-01 | TF-1 · D1 · 2 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s18 | test-01 | TF-4 · D2 · 3 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s19 | test-01 | TF-1 · D3 · 4 | `c` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s20 | test-01 | TF-3 · D2 · 3 | `5` / `12` | A | M | M | A+S | — | A | A | M | A | A |  |
| C-s01 | decomp-01 | CE-S2 · 3 | `a,b,c` / `b,c,e` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s02 | pattern-01 | CE-S5 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s03 | abstract-01 | CE-S1 · 4 | `b` / `d` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s04 | algo-01 | CE-S4 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s05 | order-01 | CE-S3 · 3 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s06 | test-01 | CE-S2 · 2 | `a,c` / `b,d` | A | M | M | A+M | M | A | A | M | A | A |  |
| L-act-01.vA | decomp-01, order-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-01.vB | decomp-01, order-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vA | pattern-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vB | pattern-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vA | algo-01, test-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vB | algo-01, test-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
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
| QC-03 | NOT APPLICABLE | Tidak ada konversi satuan baru (menit/hari memakai pembulatan W5) |
| QC-04 | PASS (dengan catatan) | §6: lab act-01 vA 2 vs vB 4 urutan valid |
| QC-05 | PASS | §7 |
| QC-06 | PASS setelah perbaikan | §8 |
| QC-07 | PASS | `spec.md` lab dibuat dari `checks.yaml` (termasuk fixture); proyek spec ↔ rubrik |
| QC-08 | PASS | Normalisasi urutan (ID, pemisah, huruf), kode, angka; depends_on proyek |
| QC-09 | PASS | Validator |
| QC-10 | PASS | Batas: 300 ÷ 70 dibulatkan ke atas (E12), urutan yang melanggar satu prasyarat (E03), ID hilang/ganda (E04, E05) |
| QC-11 | PASS | §8 |
| QC-12 | NOT APPLICABLE | Tidak ada satuan data |

## 11. Regresi F-01–F-72 (penerapan pada modul baru)

Makna dan disposisi historis tidak diubah; tabel ini hanya mencatat
penerapannya pada W7.

| Temuan | Makna historis | Berlaku? | Artefak | Metode | Hasil teramati | Batas |
|---|---|---|---|---|---|---|
| F-01–F-06 | Kebenaran fungsional, penanganan dependensi, batas skor | Berlaku | `project/rubric.yaml` | Setiap isian proyek punya pemeriksaan kebenaran; depends_on eksplisit; kredit independen (MR-2); tanpa gerbang nol global; contoh batas dihitung evaluator | E01–E16 dihitung `sim_w07.py`; kredit independen (E10 hanya c01; E12 hanya c13) | Evaluator dokumentasi |
| F-07–F-08 | Bukti per butir dan visibilitas jawaban | Berlaku | pelajaran, spec | Matriks bukti per butir (§9); pemindai V-L + tinjauan konteks (§8) | 0 hit pemindai; 1 ambiguitas klasifikasi diperbaiki | Konteks dinilai manual |
| F-09–F-23 | Maksimum dapat dicapai, satuan, normalisasi, kesetaraan varian, validasi deterministik, input rusak | Berlaku | semua komponen | Validator struktur (maksimum, poin, kunci, ID); pemeriksa NB-5 / bentuk jawaban; matriks kesetaraan (§6); fixture input rusak | Maksimum 56/100/100/20; urutan dienumerasi | Kesetaraan dinilai manual |
| F-24–F-27 | Keamanan skill dan bukti aktivasi yang jujur | Berlaku (proses) | `.claude/`, registry | `.claude/`, izin, hooks, allowed-tools, asal skill tidak diubah; V03 tidak diklaim ulang | Tidak ada perubahan | V03 tidak dijalankan ulang |
| F-28–F-48 | Asumsi eksplisit, akurasi akademik, kredit independen, kontrak validitas | Berlaku | stem, spec, rubrik | Asumsi model di stem/spec (§7); konstanta kunci proyek tidak bergantung isian lain; aturan validitas di rubrik | Kebutuhan, hasil tugas, aturan relevansi, prasyarat tertulis eksplisit | — |
| F-49–F-59 | Temuan asli yang dipulihkan (asumsi topologi, diagnosis, satuan peka huruf, klasifikasi utama, autentikasi, media, prasyarat urutan, path terpendek, verifikasi salinan, otorisasi, AMN) | Berlaku | lab act-01, proyek F1, s03 | Pola yang relevan diperiksa: asumsi skenario eksplisit; jawaban tunggal yang dapat dipertahankan; prasyarat urutan; satuan peka huruf bila ada bit/byte | Pola F-52 (satu kunci per skenario) dan F-37/F-55 (prasyarat urutan eksplisit; semua urutan sah diterima) diterapkan | — |
| F-60–F-70 | Akurasi pelajaran, pemilihan varian remedial, konsistensi dokumen | Berlaku | `remedial.md`, dokumen status | Remedial menyebut VA-1–VA-6; angka pelajaran dihitung ulang; dokumen status disinkronkan | VA-1–VA-6 disebut | — |
| F-71 | Dependensi validitas eksplisit | Berlaku | `project/rubric.yaml` | Setiap depends_on menyebut syarat terbaca/sah isian yang dipakai; evaluator dokumentasi memastikan isian tak terbaca → pemeriksaan terkait 0 | E04/E05: F2 tak terbaca → c09 dan K2.c02 = 0, lainnya tetap | — |
| F-72 | Koleksi rusak dan kredit independen | Berlaku | `project/rubric.yaml` validity | Struktur luar rusak dan ID tak dikenal punya aturan dan fixture | E09 (ID info tak dikenal → F4 tak terbaca), E16 (F1 bukan tabel → 68) | — |

## 12. Batas penilaian objektif dan bukti reviewer

Pemeriksaan membuktikan jawaban sesuai aturan tertulis pada skenario fiktif (kebutuhan, hasil, prasyarat, relevansi). Ini tidak menilai kreativitas atau kualitas dekomposisi bebas; bentuk itu sengaja tidak dinilai otomatis (tanpa penilaian subjektif atau AI).

| Field | Isi |
|---|---|
| Reviewer / tanggal / basis | Claude (penyusun), 2026-11-24, `main` = `846051f` |
| Temuan terbuka | Tidak ada yang diketahui penyusun; butuh review independen dan penerimaan owner |

Metrik W7 (dari transkrip, perkiraan): panggilan alat ≈ 22; aksi gagal 0; temuan tinjauan yang benar 2 (ambiguitas T1, bias posisi kunci); generator `module.yaml` baru dipakai agar tidak mengulang kesalahan sambung templat W6; checkpoint 1. TOKEN USAGE: **NOT MEASURABLE**.
