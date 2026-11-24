# IT ZERO → HERO — Rencana Produksi Kurikulum (UW-37)

Status: **RENCANA** · dokumentasi saja · **belum ada konten yang
diproduksi**. UW-37 tetap **NOT STARTED**. Tanggal: **2026-11-24**. Basis:
`main` = `bcecdae`.

Dasar: D-21 (kurikulum lengkap wajib sebelum PLANNING CLEAR, 64 komponen),
D-13 (empat komponen per modul; capstone = mini-project modul 16), D-19,
D-12 (poin mentah, maks. 10.000 per komponen per attempt), urutan kurikulum
terkunci BL:15–24 dan kerangka D-01 M-02. Templat dan rencana ini **tidak**
menjadikan konten COMPLETE.

## 1. Peta ketergantungan kurikulum

Urutan terkunci, unlock linear per modul (BL:21, D-04):

```
Fase 1 IT foundations:      W1 Hardware/software → W2 OS & file → W3 Jaringan → W4 Keamanan siber
Fase 2 Matematika & CT:     W5 Dasar matematika → W6 Biner & Boolean → W7 Berpikir komputasional → W8 Algoritma & flowchart
Fase 3 Python:              W9 Dasar Python → W10 Variabel & tipe data → W11 Kondisi → W12 Loop, fungsi, debugging
Fase 4 DB, web, Git, final: W13 Database & SQL → W14 HTML/CSS → W15 Git/GitHub → W16 Capstone
```

Ketergantungan konsep utama (PROPOSED): W6 → W8 (logika untuk algoritma);
W8 → W9–W12 (algoritma ke kode); W2 → W15 (file/folder ke Git); W9–W12 →
W16 (capstone memakai Python); W13–W14 → W16 bila capstone memakainya
(topik capstone OPEN).

## 2. Templat dokumen modul (wajib untuk setiap modul)

| # | Bagian | Isi minimum (D-21) |
|---|---|---|
| 1 | Identitas | ID modul (`mod-wNN`), fase, versi konten |
| 2 | Tujuan belajar | Tujuan terukur per kompetensi |
| 3 | Prasyarat | Modul/kompetensi sebelumnya |
| 4 | Penjelasan pelajaran | Teks Bahasa Indonesia, diagram (dengan deskripsi teks), glosarium, ringkasan |
| 5 | Persyaratan offline | Semua materi inti tersedia offline; video hanya opsional (BL:24) |
| 6 | Estimasi durasi | Jam per bagian; total modul sesuai §5 |
| 7 | Komponen Theory | Soal ujian teori + kunci + varian remedial (templat §3.1) |
| 8 | Komponen Laboratory | Instruksi, keluaran yang diharapkan, rencana test case dan fixture (templat §3.2) |
| 9 | Komponen Mini-project | Instruksi + rubrik (templat §3.3); modul 16 = capstone dengan rubrik khusus |
| 10 | Komponen Concept explanation | Soal terstruktur + kunci + aturan kredit (templat §3.4) |
| 11 | Alokasi poin | Poin bilangan bulat per soal/test/kriteria; total per komponen ≤ 10.000 |
| 12 | Materi remedial | Penjelasan ulang dan latihan tambahan per kompetensi lemah |
| 13 | Catatan review | Reviewer, tanggal, hasil checklist §7 |

## 3. Templat penilaian

### 3.1 Soal Theory

| Field | Isi |
|---|---|
| ID soal + versi | `item-…`, `item_version` |
| Kompetensi | `comp-…` |
| Tipe | Format soal (OPEN, UW-27) |
| Teks soal | |
| Kunci + jawaban diterima | Himpunan eksplisit |
| Poin | Bilangan bulat |
| Varian setara | ID varian untuk remedial (jumlah minimum: CU-5, OPEN) |

### 3.2 Spesifikasi lab

| Field | Isi |
|---|---|
| Instruksi + kode/skema awal | |
| Keluaran yang diharapkan | |
| Rencana test case | ID, input, keluaran, poin (aturan bobot: CU-6, OPEN), terlihat/tersembunyi |
| Fixture | Data uji (mis. database latihan SQL terpisah, QG LB-6) |
| Batas eksekusi | Mengacu ambang D-10 (rencana; NOT VERIFIED) |
| Catatan runtime | Lab minggu 9–12 dan bagian Python capstone bergantung O-04 (NOT VERIFIED) |

### 3.3 Mini-project / capstone

| Field | Isi |
|---|---|
| Tujuan dan lingkup | Lingkup sesuai jam modul (§5) |
| Deliverable | |
| Rubrik | Kriteria yang dapat diperiksa objektif, poin per kriteria (rubrik: CU2-O4, CU-9 untuk capstone, OPEN) |
| Acceptance test terencana | Spesifikasi, tidak dijalankan |

### 3.4 Concept explanation

| Field | Isi |
|---|---|
| Format | Memilih alasan / mengurutkan / mencocokkan / menemukan kesalahan (D-01 M-06) |
| Konsep wajib | |
| Jawaban diterima dan alternatif | |
| Aturan kredit | Mengikuti keputusan OP-4 (OPEN) |
| Poin | Bilangan bulat |

## 4. Matriks cakupan 64 komponen

Status setiap sel: **NOT STARTED**. Kode ketergantungan:
T = UW-27 (format/durasi ujian), L = CU-6, P = rubrik mini-project (CU2-O4),
C = OP-4, X = capstone rubrik (CU-9), R = runtime Python (O-04, NOT VERIFIED),
F = bentuk lab SQL/HTML/Git (CU-7), S = pembagian minggu 9/10 (CU-11).

| Modul | Theory 30% | Laboratory 40% | Mini-project 20% | Concept 10% |
|---|---|---|---|---|
| W1 Hardware/software | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W2 OS & file | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W3 Jaringan | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W4 Keamanan siber | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W5 Dasar matematika | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W6 Biner & Boolean | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W7 Berpikir komputasional | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W8 Algoritma & flowchart | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (P) | NOT STARTED (C) |
| W9 Dasar Python | NOT STARTED (T, S) | NOT STARTED (L, R, S) | NOT STARTED (P, R) | NOT STARTED (C) |
| W10 Variabel & tipe data | NOT STARTED (T, S) | NOT STARTED (L, R, S) | NOT STARTED (P, R) | NOT STARTED (C) |
| W11 Kondisi | NOT STARTED (T) | NOT STARTED (L, R) | NOT STARTED (P, R) | NOT STARTED (C) |
| W12 Loop, fungsi, debugging | NOT STARTED (T) | NOT STARTED (L, R) | NOT STARTED (P, R) | NOT STARTED (C) |
| W13 Database & SQL | NOT STARTED (T) | NOT STARTED (L, F) | NOT STARTED (P) | NOT STARTED (C) |
| W14 HTML/CSS | NOT STARTED (T) | NOT STARTED (L, F) | NOT STARTED (P) | NOT STARTED (C) |
| W15 Git/GitHub | NOT STARTED (T) | NOT STARTED (L, F) | NOT STARTED (P) | NOT STARTED (C) |
| W16 Capstone | NOT STARTED (T) | NOT STARTED (L) | NOT STARTED (X, R) — capstone | NOT STARTED (C) |

16 modul × 4 komponen = **64 komponen**, 0 selesai.

Catatan R: konten lab dan spesifikasi test minggu 9–12 dapat ditulis
sebagai dokumentasi; eksekusinya tetap NOT VERIFIED sampai uji kelayakan
diizinkan (D-10). Alternatif bila runtime gagal ditunda ke milestone
(UW-21, D-22).

## 5. Estimasi jam belajar (PROPOSED — alokasi per komponen OPEN, CU2-O3)

| Modul | Teori & bacaan | Latihan, kuis, ujian teori | Lab | Mini-project | Concept | Total |
|---|---|---|---|---|---|---|
| W1–W15 (masing-masing) | 2,5 | 1,5 | 2,5 | 1,0 | 0,5 | **8,0** |
| W16 | 1,0 | 0,5 | 1,0 | 5,0 (capstone) | 0,5 | **8,0** |
| **Program** | | | | | | **15 × 8 + 8 = 128** |

Sesuai BL:15 dan D-01 M-03 (128 jam). Capstone berada di dalam 128 jam
(D-13).

## 6. Batch produksi (PROPOSED)

| Batch | Isi | Prasyarat keputusan |
|---|---|---|
| CB-0 | Finalisasi templat §2–§3 dan aturan konten (format markup/diagram, CU-3; jumlah varian, CU-5) | OP-4, CU-6, UW-27, CU-3, CU-5, CU2-O4 |
| CB-1 | Modul W1–W4 (16 komponen) | CB-0 |
| CB-2 | Modul W5–W8 (16 komponen) | CB-0 |
| CB-3 | Modul W9–W12 (16 komponen) | CB-0, CU-11 |
| CB-4 | Modul W13–W16 (16 komponen), termasuk rubrik capstone | CB-0, CU-7, CU-9 |
| CB-R | Review dan acceptance seluruh 64 komponen oleh owner | CB-1–CB-4 |

Setiap batch = satu PR dokumentasi; status sel matriks §4 diperbarui
hanya setelah checklist §7 lolos dan owner menerima.

## 7. Checklist review dan acceptance per modul

| ID | Kriteria |
|---|---|
| CA-01 | Seluruh 13 bagian templat §2 terisi |
| CA-02 | Keempat komponen ada; alokasi poin bilangan bulat; total per komponen ≤ 10.000 |
| CA-03 | Kunci jawaban, jawaban alternatif, dan aturan kredit eksplisit (CC-04, CC-06) |
| CA-04 | Rencana test case lab deterministik dengan fixture (CC-07); tidak ada klaim sudah dijalankan |
| CA-05 | Varian remedial tersedia sesuai jumlah minimum yang diputuskan (CU-5) |
| CA-06 | Materi inti offline; video hanya opsional (CC-02) |
| CA-07 | Bahasa Indonesia; istilah teknis Inggris dijelaskan (CC-03) |
| CA-08 | Diagram punya deskripsi teks (CC-10) |
| CA-09 | Estimasi durasi sesuai §5; total program tetap 128 jam (CC-09) |
| CA-10 | Tanpa AI grading/tutor; tanpa server wajib (BL:38) |
| CA-11 | Review manusia dan penerimaan owner tercatat |

## 8. Ketergantungan yang belum diputuskan

| ID | Keputusan | Memblokir |
|---|---|---|
| OP-4 | Aturan kredit penjelasan konsep ([OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md](OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md)) | Kolom Concept |
| CU-6 | Bobot test lab dan remedial ([CU6_LAB_SCORING_DECISION_SHEET.md](CU6_LAB_SCORING_DECISION_SHEET.md)) | Kolom Laboratory |
| CU-9 | Rubrik capstone | W16 Mini-project |
| CU2-O4 | Rubrik mini-project | Kolom Mini-project |
| UW-27 (OP-5) | Format soal dan rumus durasi ujian | Kolom Theory |
| CU-3, CU-5, CU-7, CU-11 | Format konten, jumlah varian, bentuk lab SQL/HTML/Git, pembagian W9/W10 | CB-0, CB-3, CB-4 |
| UW-29, UW-30, UW-31 | Aturan submission, identitas XP, unlock rinci | Penandaan aktivitas dan XP di konten |
