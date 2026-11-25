---
module_id: mod-w05
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-2. Belum direview independen; belum diterima owner"
---

# W5 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-2) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review independen (ChatGPT) | **BELUM** |
| Diterima owner | **BELUM** |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim (W5 tanpa runtime; aplikasi belum ada) |
| Durasi diuji dengan pelajar | **TIDAK** |

Acuan struktur: W1–W4 (W01-ACC–W04-ACC), dengan batas review independen
yang diungkapkan tetap berlaku. Isi W5 tidak menyalin isi modul lain.

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah |
|---|---|
| Pelajaran / set latihan | 4 / 4 (40 + 35 + 40 + 35 = 150 menit) |
| Soal teori | **40** (20 slot × 2) |
| Soal concept | **12** (6 slot × 2) |
| Spesifikasi lab | **6** (3 aktivitas × 2 varian) |
| Mini-project | 1 (`spec.md` + `rubric.yaml`, 13 contoh evaluasi) |
| Remedial / review | 1 / 1 |

## 3. Tujuan belajar (6 LO ↔ 6 kompetensi ↔ 6 slot concept)

| LO | Kompetensi | Pelajaran | Teori | Lab | Proyek | Concept |
|---|---|---|---|---|---|---|
| LO1 | `comp-w05-arith-01` | les-01 | s01, s02, s03, s04 | act-01.c01–c03 | K1.c01 (diskon dalam rumus), K4.q4 | s01 |
| LO2 | `comp-w05-expr-01` | les-01 | s05, s06, s07 | act-02.c07, act-03.c04 | K1.c01–c06, K4.q4 | s02 |
| LO3 | `comp-w05-divmod-01` | les-02 | s08, s09, s10 | act-01.c04–c06, act-03.c02, act-03.c03, act-03.c06 | K1.c14, K1.c15, K4.q3 | s03 |
| LO4 | `comp-w05-unit-01` | les-02 | s11, s12, s13 | act-03.c01, act-03.c05 | K4.q5 | s04 |
| LO5 | `comp-w05-pct-01` | les-03 | s14, s15, s16, s17 | act-02.c01–c04 | K1.c08–c13, K4.q1 | s05 |
| LO6 | `comp-w05-round-01` | les-04 | s18, s19, s20 | act-02.c05, act-02.c06, act-02.c08 | K1.c08–c13 (pembulatan), K3.c02, K4.q2 | s06 |

## 4. Skor yang dapat dicapai, durasi, dan XP

| Komponen | Maks. dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori | 56 | **56** | Kunci setiap slot ada di opsi / accepted_answers (validator); D1 8 × 2 + D2 8 × 3 + D3 4 × 4 = 16 + 24 + 16 |
| Lab | 100 | **100** | 30 + 40 + 30; setiap pemeriksaan berkunci tunggal |
| Proyek | 100 | **100** | Contoh E01 dihitung evaluator = 100 |
| Concept | 20 | **20** | Jumlah maksimum slot; CE-S2 maks = jumlah kunci; CE-S3 maks = n − 1 |

Durasi teori (rumus A.4, dihitung ulang dari blueprint W5, bukan
disalin): S = 1665 detik → S_buffer = ⌈S × 11/10⌉ = 1832 →
standar ⌈1832/60⌉ + 2 = **33 menit**; review = 45 − 33 = 12;
TA-B = ⌈33 × 3/2⌉ = 50 (di luar 480). Format: {'TF-1': 6, 'TF-3': 11, 'TF-4': 2, 'TF-2': 1}; kesulitan {'D1': 8, 'D2': 8, 'D3': 4}
(TP-B 40/40/20). Alokasi HA-A fase 2: M 150 · U 45 · L 120 · P 90 · C 30 ·
R 45 = 480. XP = 305 (13 identitas, katalog sama dengan W1–W4).

Validator (`validate2.py mod-w05`):

```
theory: S=1665 Sb=1832 std=33 review=12 TA-B=50 max=56 formats={'TF-1': 6, 'TF-3': 11, 'TF-4': 2, 'TF-2': 1}
concept max=20 formats=['CE-S4:4', 'CE-S2:3', 'CE-S5:4', 'CE-S1:4', 'CE-S3:3', 'CE-S2:2']
unique ids=180
key positions (TF-1/TF-4 MC, CE-S1, CE-S5 corr, K4): {'a': 6, 'b': 6, 'c': 7, 'd': 6}
NO ERRORS
```

## 5. Verifikasi independen

Semua kunci angka dihitung ulang secara independen dengan `fractions.Fraction`
dan `decimal.Decimal` (pembulatan `ROUND_HALF_UP`) sebagai asersi di
generator sebelum berkas ditulis (`gen_w05.py` 24 pernyataan assert berisi 55
perbandingan untuk teori dan concept; `gen_w05_lab.py` 9/36; `gen_w05_proj.py` 5/9); satu asersi gagal saat pertama dijalankan karena **asersinya**
salah tulis (Jumat + 45 hari = Senin; kunci butir sudah benar) — diperbaiki.
Angka pelajaran, latihan, dan remedial dihitung ulang manual baris demi baris.

| Pemeriksaan | Hasil teramati |
|---|---|
| Basis persen (s15, s16, s17, lab act-02 c02–c04, proyek F4/F5) | Nilai dasar dinyatakan di setiap stem; F4 terhadap anggaran, F5 terhadap total |
| Satuan dan konversi (s11, s13, lab act-03) | Dua arah dan dua tingkat (L → mL → detik → menit) |
| Urutan operasi (s01–s04, concept s01, lab act-01) | Kiri ke kanan untuk ÷/× dan −/+ diuji di kedua varian |
| Bulat vs desimal | Jumlah benda/wadah selalu bulat; pembulatan ke atas (s19, lab c08) vs ke bawah (lab act-03 c06, proyek F6) dinyatakan |
| Pembulatan | Setengah ke atas, bilangan positif; jebakan pembulatan bertahap (lab act-02 c06, concept s06) |
| Nol dan negatif | Suhu negatif (s03), kurung bernilai negatif (lab act-01 c02); sisa 0 (s10, concept s03); pembulatan negatif dinyatakan di luar cakupan |
| Bentuk angka NB-5 (`nb5_check.py`) | mod-w05: butir angka diperiksa 58; contoh ditolak yang akan lolos bila titik dianggap desimal (mutasi tertangkap): 3 — ALL OK |


### 5.1 Evaluator dokumentasi proyek (dihitung, bukan ditulis tangan)

| Contoh | Kasus | K1 | K2 | K3 | Total (K4 = 10) |
|---|---|---|---|---|---|
| E01 | Isian acuan (bentuk strict) | 60 | 20 | 10 | 100 |
| E02 | F5.P1 ditulis `18` (tanpa desimal); lainnya acuan | 60 | 20 | 7 | 97 |
| E03 | Lupa diskon buku: P1 = 50.000, lalu semua turunan dihitung konsisten dari total 232.000 | 16 | 20 | 10 | 56 |
| E04 | F4 = `44%` (dibulatkan ke bilangan bulat) | 55 | 20 | 7 | 92 |
| E05 | F5.P1 = `18.0` (titik sebagai desimal) | 57 | 15 | 7 | 89 |
| E06 | F6 = `39,7` (desimal) | 55 | 18 | 7 | 90 |
| E07 | Semua rupiah ditulis dengan `Rp` (mis. `Rp40.000`) | 60 | 20 | 6 | 96 |
| E08 | Semua rupiah tanpa titik ribuan (mis. `40000`) | 60 | 20 | 6 | 96 |
| E09 | Semua isian kosong | 0 | 0 | 0 | 0 untuk K1–K3 (MR-6); K4 sesuai jawaban |
| E10 | F7 = `6.000` (salah hitung sisa) | 55 | 20 | 10 | 95 |
| E11 | F2 = `222,000` (koma sebagai pemisah ribuan) | 54 | 18 | 6 | 88 |
| E12 | F1 berisi baris tak dikenal P9 = `1.000` di samping P1–P5 acuan | 60 | 20 | 10 | 100 |
| E13 | Struktur luar F5 rusak (daftar, bukan tabel P1–P5) | 45 | 15 | 7 | 77 |

Prosedur: `sim_w05.py` membaca `field_rules` dan konstanta kunci dari
`rubric.yaml`, mengevaluasi 13 submission contoh, dan membandingkan hasil
dengan harapan yang dihitung tangan sebelumnya: semua cocok. Uji mutasi
(pengurai menerima titik sebagai desimal) mengubah E05 dari 89 menjadi 97,
sehingga pemeriksa mendeteksi aturan yang dilonggarkan. Baris terakhir
keluaran: `ALL OK`.

Kebijakan yang perlu diperhatikan reviewer: **tanpa kredit kesalahan
berantai** (E03: lupa diskon lalu konsisten → 56). Ini mengikuti brief A.3
"nilai eksak" dan MR-2 (setiap isian dibandingkan dengan nilai benar data,
bukan isian lain). Ruang solusi: 1 himpunan nilai bernilai penuh.

## 6. Matriks kesetaraan varian (QC-04)

| Butir | Konsep wajib | Bukti kesetaraan vA ↔ vB |
|---|---|---|
| s01 | operasi yang didahulukan | × vs + ; ÷ vs − |
| s02 | kurung lalu ×, lalu ± | struktur sama (satu kurung, satu ×, satu ±) |
| s03 | negatif berantai | dua langkah, hasil negatif di kedua varian |
| s04 | langkah salah | kiri-ke-kanan dilanggar (± vs ×/÷) |
| s05–s07 | variabel; substitusi + pangkat; rata-rata terbalik | peran variabel; satu pangkat + satu ×; n = 4 vs 5 dengan satu nilai hilang |
| s08–s10 | sisa; siklus 7; keterbagian | sisa 5 vs 4; siklus 7 hari; 3 dari 5 bilangan habis dibagi |
| s11–s13 | jam→menit; perbandingan; rantai satuan | dua langkah sama; satu satuan dulu; L → mL → detik → menit |
| s14–s17 | persen dari; diskon; persen perubahan; perubahan berurutan | struktur sama; nilai dasar berubah di s17 kedua varian |
| s18–s20 | pembulatan; ke atas; rata-rata + pembulatan | angka berikutnya ≥ 5 di kedua varian; sisa membutuhkan wadah tambahan; angka penentu 5 |
| Concept s01–s06 | sama per slot | pasangan ekspresi setara (kiri-ke-kanan + kurung/pangkat); 3 kunci CE-S2; baris salah sisa; konversi waktu vs massa; dua urutan diterima di kedua varian CE-S3; 2 kunci CE-S2 |
| Lab act-01–03 | sama per pemeriksaan | struktur dan banyak langkah sama; angka berbeda |

## 7. Model sederhana vs kenyataan (QC-05)

| Model W5 | Kenyataan | Tempat disebut |
|---|---|---|
| Pembulatan setengah ke atas untuk bilangan positif | Program/lembar kerja dapat memakai aturan lain (mis. setengah ke genap); bilangan negatif tidak dinilai | les-04 §2, stem s18/lab |
| Hasil bagi dan sisa hanya bilangan bulat tidak negatif, pembagi positif | Bahasa pemrograman berbeda-beda untuk bilangan negatif | les-02 §1, spec act-01 |
| Aliran keran/pompa tetap | Aliran nyata berubah | stem s13 ("model ideal") |
| Notasi `×`, `÷`, `²` | Sintaks pemrograman berbeda (W9+) | les-01 §1, module.yaml |
| NB-5: titik hanya pemisah ribuan | Sebagian perangkat/aplikasi memakai titik desimal | les-03 §1 |

## 8. Tumpang-tindih dan visibilitas (QC-06, QC-11, VC-1–VC-5)

Pemindai V-L (`scan_vl.py mod-w05`) dan pemindai konteks lab dijalankan.

| Temuan | Tindakan |
|---|---|
| Pertanyaan act-03 c03 menyebut "6 jam" (= jawaban c02) | **Diperbaiki**: c03 kini "jam penuh dan sisa menit … berapa sisa menitnya" |
| "Kasus gagal" spec lab memakai `18.8`, `enam`, `2,4 kg` (membuka kunci) | **Diperbaiki**: contoh netral `3.5`, `tiga`, `5 kg` |
| Contoh terlihat act-02 memakai 30 dan 15 (sama dengan kunci) | **Diperbaiki**: `50% dari 18 = 9` |
| Contoh terbimbing les-02 = 100 ÷ 7 sisa 2 (perhitungan kunci s09 vA) | **Diperbaiki**: 92 ÷ 8 |
| Latihan les-03 80 → 68 (= s16 vB) | **Diperbaiki**: 90 → 72 |
| les-03 nilai awal 60.000 (tipe sama dengan lab act-02 vB c04) dan contoh proyek `6.000` | **Diperbaiki**: 39.000 → 52.000; contoh `7.500` |
| Sisa hit (205, 225 di les-01; angka satu digit sebagai operand di spec lab) | Diterima: kebetulan nilai antara dalam konteks lain; tidak membuka jawaban |

Kunci, pembahasan, rasional pengecoh, dan contoh evaluasi hanya di YAML
penilai (V-E) dan tampil setelah dinilai (V-P). D-34 dipertahankan.

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
| T-s01 | arith-01 | TF-1 · D1 · 2 | `d` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s02 | arith-01 | TF-3 · D1 · 2 | `16` / `14` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s03 | arith-01 | TF-3 · D2 · 3 | `-6` / `-3` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s04 | arith-01 | TF-4 · D3 · 4 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s05 | expr-01 | TF-1 · D1 · 2 | `d` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s06 | expr-01 | TF-3 · D2 · 3 | `31` / `11` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s07 | expr-01 | TF-3 · D3 · 4 | `73` / `6000` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s08 | divmod-01 | TF-3 · D1 · 2 | `5` / `4` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s09 | divmod-01 | TF-3 · D2 · 3 | `Rabu` / `Senin` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s10 | divmod-01 | TF-2 · D2 · 3 | `a,c,e` / `b,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s11 | unit-01 | TF-3 · D1 · 2 | `205` / `160` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s12 | unit-01 | TF-1 · D1 · 2 | `b` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s13 | unit-01 | TF-3 · D3 · 4 | `6` / `3` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s14 | pct-01 | TF-1 · D1 · 2 | `a` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s15 | pct-01 | TF-3 · D2 · 3 | `204000` / `117000` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s16 | pct-01 | TF-3 · D2 · 3 | `25` / `15` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s17 | pct-01 | TF-1 · D3 · 4 | `d` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s18 | round-01 | TF-3 · D1 · 2 | `3,5` / `12,35` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s19 | round-01 | TF-1 · D2 · 3 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s20 | round-01 | TF-4 · D2 · 3 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| C-s01 | arith-01 | CE-S4 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s02 | expr-01 | CE-S2 · 3 | `a,b,d` / `b,c,e` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s03 | divmod-01 | CE-S5 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s04 | unit-01 | CE-S1 · 4 | `d` / `c` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s05 | pct-01 | CE-S3 · 3 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s06 | round-01 | CE-S2 · 2 | `a,c` / `a,b` | A | M | M | A+M | M | A | A | M | A | A |  |
| L-act-01.vA | arith-01, expr-01, divmod-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-01.vB | arith-01, expr-01, divmod-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vA | pct-01, round-01, expr-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-02.vB | pct-01, round-01, expr-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vA | unit-01, expr-01, divmod-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| L-act-03.vB | unit-01, expr-01, divmod-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A |  |
| P (spec+rubrik) | semua LO | MR-A | contoh 13 | A | M | M | S | — | A+S | A+S | — | A | A |  |
| les-01 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-02 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-03 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| les-04 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A |  |
| remedial | semua LO | TPL-14 | — | M | M | M | M | — | — | — | — | M | A |  |

## 10. QC-01–QC-12

| QC | Hasil | Bukti |
|---|---|---|
| QC-01 | PASS | §4; E01 = 100 |
| QC-02 | PASS | §5.1 (13/13 dihitung evaluator) |
| QC-03 | PASS | s11, s13, lab act-03: dua arah dan dua tingkat |
| QC-04 | PASS | §6 |
| QC-05 | PASS | §7 |
| QC-06 | PASS setelah perbaikan | §8 |
| QC-07 | PASS | `spec.md` lab dibuat dari `checks.yaml` yang sama (pertanyaan tanpa kunci); proyek spec ↔ rubrik |
| QC-08 | PASS | NB-5 + `normalization_examples`; `nb5_check.py`; depends_on proyek |
| QC-09 | PASS | Validator: tidak ada field non-kanonik |
| QC-10 | PASS | Batas: angka penentu tepat 5 (s20, lab c05), sisa 0, pembulatan ke atas dengan sisa 1 (lab vA c08) |
| QC-11 | PASS | §8 |
| QC-12 | NOT APPLICABLE | Tidak ada satuan data di W5 |

## 11. Regresi F-01–F-72 (penerapan pada modul baru)

Makna dan disposisi historis tidak diubah; tabel ini hanya mencatat
penerapannya pada W5.

| Temuan | Makna historis | Berlaku? | Artefak | Metode | Hasil teramati | Batas |
|---|---|---|---|---|---|---|
| F-01–F-06 | Kebenaran fungsional, penanganan dependensi, batas skor | Berlaku | `project/rubric.yaml` | Setiap isian proyek punya pemeriksaan kebenaran; depends_on eksplisit; kredit independen (MR-2); tanpa gerbang nol global; contoh batas dihitung evaluator | E01–E13 dihitung `sim_w05.py`; cocok dengan harapan; kredit independen (E10: hanya c15 hilang) | Evaluator dokumentasi, bukan evaluator produksi |
| F-07–F-08 | Bukti per butir dan visibilitas jawaban | Berlaku | pelajaran, spec lab, spec proyek | Matriks bukti per butir (§9); pemindai V-L + tinjauan konteks (§8) | 6 tumpang-tindih diperbaiki; sisa kebetulan dicatat (§8); matriks §9 | Pemindai berbasis string; konteks dinilai manual |
| F-09–F-23 | Maksimum dapat dicapai, satuan, normalisasi, kesetaraan varian, validasi deterministik, input rusak | Berlaku | semua komponen | Validator struktur (maksimum, poin, kunci, ID); pemeriksa NB-5 / bentuk jawaban; matriks kesetaraan (§6); fixture input rusak | Maksimum 56/100/100/20 tercapai; 58 butir angka satu nilai; 1 mutasi tertangkap | Kesetaraan varian dinilai manual |
| F-24–F-27 | Keamanan skill dan bukti aktivasi yang jujur | Berlaku (proses) | `.claude/`, registry | `.claude/`, izin, hooks, allowed-tools, asal skill tidak diubah; V03 tidak diklaim ulang | Tidak ada perubahan berkas skill/izin | V03 tidak dijalankan ulang |
| F-28–F-48 | Asumsi eksplisit, akurasi akademik, kredit independen, kontrak validitas | Berlaku | stem, spec, rubrik | Asumsi model di stem/spec (§7); konstanta kunci proyek tidak bergantung isian lain; aturan validitas di rubrik | Asumsi NB-5, pembulatan, model ideal tertulis; kunci proyek konstanta data | — |
| F-49–F-59 | Temuan asli yang dipulihkan (asumsi topologi, diagnosis, satuan peka huruf, klasifikasi utama, autentikasi, media, prasyarat urutan, path terpendek, verifikasi salinan, otorisasi, AMN) | Sebagian | stem s03, s13, s19; spec proyek | Pola yang relevan diperiksa: asumsi skenario eksplisit; jawaban tunggal yang dapat dipertahankan; prasyarat urutan; satuan peka huruf bila ada bit/byte | Asumsi skenario eksplisit; satuan peka huruf tidak relevan (tanpa bit/byte) | Tidak ada satuan data |
| F-60–F-70 | Akurasi pelajaran, pemilihan varian remedial, konsistensi dokumen | Berlaku | `remedial.md`, dokumen status | Remedial menyebut VA-1–VA-6; angka pelajaran dihitung ulang; dokumen status disinkronkan | VA-1–VA-6 disebut; angka remedial dihitung ulang | — |
| F-71 | Dependensi validitas eksplisit | Berlaku | `project/rubric.yaml` | Setiap depends_on menyebut syarat terbaca/sah isian yang dipakai; evaluator dokumentasi memastikan isian tak terbaca → pemeriksaan terkait 0 | Setiap depends_on K1 menyebut "terbaca"; E06/E11: isian tak terbaca → K1 dan K2 terkait 0, lainnya tetap | — |
| F-72 | Koleksi rusak dan kredit independen | Berlaku | `project/rubric.yaml` validity | Struktur luar rusak dan ID tak dikenal punya aturan dan fixture | E12 (baris P9 tak dikenal → diabaikan, 100); E13 (F5 bukan tabel → F5 tak terbaca, 77) | — |

## 12. Batas penilaian objektif dan bukti reviewer

Pemeriksaan membuktikan jawaban cocok dengan nilai benar pada data fiktif menurut aturan W5; tidak mengukur kefasihan berhitung di luar soal, dan tidak memvalidasi durasi dengan pelajar.

| Field | Isi |
|---|---|
| Reviewer / tanggal / basis | Claude (penyusun), 2026-11-24, `main` = `846051f` |
| Temuan terbuka | Tidak ada yang diketahui penyusun; butuh review independen dan penerimaan owner |

Metrik W5 (dari transkrip, perkiraan): panggilan alat ≈ 40; berkas acuan dibaca ulang 0 (struktur W4 sudah dimuat); aksi gagal 3 (asersi salah tulis, `F` tidak terdefinisi di generator lab, regex pemeriksa bentuk yang salah mengurai `18.8`) — semuanya tertangkap pemeriksa sebelum commit; temuan pemeriksa yang benar 7 (6 tumpang-tindih/visibilitas, 1 bias posisi kunci); checkpoint 1. TOKEN USAGE: **NOT MEASURABLE**.

## Register koreksi PR #28 (review independen: REQUEST CHANGES, SHA `ca73981`)

Ledger otoritatif F-73–F-94 **tidak tersedia** di repositori maupun di PR #28
(komentar/review kosong). Karena itu temuan dicatat dengan ID sementara
`PR28-nn`; nomor F yang disebut owner hanya sebagai "dikaitkan sebelumnya"
dan **belum direkonsiliasi**. F-01–F-72 dan disposisinya tidak diubah.
Status modul tetap: **diproduksi, belum diterima owner**.

| ID sementara | Dikaitkan | Temuan | Disposisi | Bukti / kriteria |
|---|---|---|---|---|
| PR28-02 | F-79 | NB-5: teks "cocokkan persis" bertentangan dengan "huruf satuan bebas" | CONFIRMED — FIXED (kontrak N1–N6) | 70 teks normalisasi + 6 aturan proyek diganti; 37 fixture (termasuk W3 F-51 tak berubah) lolos; contoh positif/negatif di butir |
| PR28-06 | F-82 | `required_concepts`: sebagian varian tidak menilai setiap konsep slot (W5 concept s01 vA, s04 vB; W6 s03 vB, s04) | OPEN — keputusan owner | TPL-13 mendefinisikan `required_concepts` per slot; VA-1 tidak menyebutnya. Kunci semua benar; butir tidak diubah |
| PR28-07 | F-78/F-92 (deskripsi asli tidak tersedia) | K4 proyek membuka jawaban isian yang masih dapat diedit | CONFIRMED — FIXED (W6 q2–q4, W7 q1–q4, W8 q1–q5) | Soal ditulis ulang ke tingkat konsep; LO, posisi kunci, dan poin K4 tetap; W5 K4 = QUALITY NOTE (rumus definisi dari spesifikasi, bukan nilai jawaban) |
| PR28-08 | — | W5 akademik: "sisa ÷ 7" dapat dibaca membagi sisa; NB-5 dicampur dengan notasi matematika | CONFIRMED — FIXED (kata-kata) | Pelajaran 2 ringkasan, remedial R-DIVMOD, pelajaran 3 §1 |
| PR28-12 | F-69/F-70 (pola) | Status aktif tidak sinkron (roadmap UW-26/UW-37, PROJECT_MAP §19, header review W2–W4) | CONFIRMED — FIXED | Metadata aktif diperbarui; catatan historis ditandai, tidak dihapus |

Batas: kontrak normalisasi diverifikasi dengan skrip dokumentasi sementara
(tidak di-commit), bukan evaluator produksi atau runtime Android.
Status koreksi: menunggu review delta independen; tidak ada klaim PASS.

### Putaran 2 (review delta REQUEST CHANGES, SHA `9bf2285`)

ID tetap; tidak ada ID baru. Bukti dari `r2_check.py` (skrip dokumentasi sementara).

| ID | Koreksi putaran 2 | Bukti |
|---|---|---|
| PR28-08 | W5 pelajaran 3: `4,200` tidak lagi disebut salah secara umum; dibedakan bulat 4200 vs desimal tiga angka (4,2) | N1–N6: butir bulat → `4.200`/`4200` diterima, `4,200` tidak sah; butir tiga desimal → `4,200` diterima, `4,2`/`4,20` tidak sah |
| PR28-12 | HANDOFF B-10, status D-26–D-35, ringkasan tugas terakhir; PROJECT_MAP R-02 | W1–W4 diterima; W5–W8 menunggu; W9–W16 NOT STARTED; 32/64, 16/64, 32/4/12/3/5 = 56, 32/43 tetap |

### Putaran 3 (keputusan owner D-39, HYBRID COMPETENCY COVERAGE)

ID tetap; tidak ada ID baru. Bukti: `cov_check.py`, `cov_keys.py`, `nb5_full.py` (skrip dokumentasi sementara).

| ID | Hasil | Bukti |
|---|---|---|
| PR28-06 | **RESOLVED (D-39)**: kontrak dicatat; 21/21 konsep wajib W5 PASS tanpa perubahan (kandidat concept s01 pangkat → teori s06 dan lab act-01.c03 kedua varian; s04 60 menit → teori s11 dan lab act-03.c01 kedua varian) | Matriks `docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md` |
| PR28-02 | Tindak lanjut NB-5: 82 butir NB-5 W5–W6 (teori 30, lab 52) diperiksa — afiks per butir, presisi, kanonik, tanda, ribuan, `Rp` peka huruf, pembeda EVALUATION_ERROR lab: **0 temuan**; uji mutasi (presisi, ribuan, tanda, galat evaluasi) tertangkap | Matriks `docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md` |
