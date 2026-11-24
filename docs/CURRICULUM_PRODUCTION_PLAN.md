# IT ZERO → HERO — Rencana Produksi Kurikulum (UW-37)

Status: **RENCANA** · dokumentasi saja · **belum ada konten yang
diproduksi**. UW-37 tetap **NOT STARTED**. Tanggal: **2026-11-24**
(diperbarui batch D-23–D-25). Basis: `main` = `928e278` (merge PR #23).
Templat provisional CB-0 rinci: [CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md).

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
W16 (capstone memakai Python); W13 dan W15 → W16 (usulan capstone memakai
SQL dan Git, [PROJECT_RUBRIC_DECISION_SHEETS.md](PROJECT_RUBRIC_DECISION_SHEETS.md) §B;
topik capstone menunggu CU-9). Pembagian W9/W10: usulan PB-A
([CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md) §E).

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
| Tipe | Format soal TF-1–TF-5 (usulan OP-5, UW-27, OPEN) |
| Teks soal | |
| Kunci + jawaban diterima | Himpunan eksplisit |
| Poin | Bilangan bulat |
| Varian setara | ID varian untuk remedial (usulan VR-B: 2 per slot; CU-5, OPEN) |

### 3.2 Spesifikasi lab

| Field | Isi |
|---|---|
| Instruksi + kode/skema awal | |
| Keluaran yang diharapkan | |
| Rencana test case | ID, input, keluaran, poin integer (LW-B, LR-A — D-24), timeout `tᵢ` ms (TB-B, `Σ tᵢ ≤ 3.000` — D-24), terlihat/tersembunyi |
| Fixture | Data uji (mis. database latihan SQL terpisah, QG LB-6) |
| Batas eksekusi | Mengacu ambang D-10 (rencana; NOT VERIFIED) |
| Catatan runtime | Lab minggu 9–12 dan bagian Python capstone dapat diterima sebagai perencanaan sebelum eksekusi (RM:RV-1–RV-3); eksekusi runtime O-04 tetap NOT VERIFIED |

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
| Aturan kredit | CE-S1–CE-S5, CE-V1–CE-V7 (D-23) |
| Poin | Bilangan bulat |

## 4. Matriks cakupan 64 komponen

Status setiap sel: **NOT STARTED** (tidak ada konten lengkap yang memenuhi
CA-01–CA-11). Kode ketergantungan yang **masih OPEN**:
T = OP-5 format/durasi ujian (UW-27); P = rubrik mini-project CU2-O4;
X = rubrik capstone CU-9; K = format konten CU-3; V = jumlah varian CU-5;
M = varian/remedial mini-project (CU-5 MPV); F = bentuk lab SQL/HTML/Git
CU-7; S = pembagian W9/W10 CU-11; R = runtime Python (O-04, NOT VERIFIED —
**tidak** memblokir penerimaan perencanaan, RM:RV-1). Semua sel juga
bergantung pada CU2-O3 (jam), OP-7 (pengumpulan), OP-8 (identitas XP).

Sudah diputuskan (tidak lagi memblokir): Concept explanation → D-23;
Laboratory → D-24 (klarifikasi LX-1–LX-5 masih OPEN, tidak memblokir
penulisan konten karena konten menulis `tᵢ` per test).

| Modul | Theory 30% | Laboratory 40% | Mini-project 20% | Concept 10% |
|---|---|---|---|---|
| W1 Hardware/software | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W2 OS & file | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W3 Jaringan | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W4 Keamanan siber | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W5 Dasar matematika | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W6 Biner & Boolean | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W7 Berpikir komputasional | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W8 Algoritma & flowchart | NOT STARTED (T, K, V) | NOT STARTED (K, V) | NOT STARTED (K, M, P) | NOT STARTED (K, V) |
| W9 Dasar Python | NOT STARTED (T, K, V, S) | NOT STARTED (K, V, R, S) | NOT STARTED (K, M, P, R, S) | NOT STARTED (K, V) |
| W10 Variabel & tipe data | NOT STARTED (T, K, V, S) | NOT STARTED (K, V, R, S) | NOT STARTED (K, M, P, R, S) | NOT STARTED (K, V) |
| W11 Kondisi | NOT STARTED (T, K, V) | NOT STARTED (K, V, R) | NOT STARTED (K, M, P, R) | NOT STARTED (K, V) |
| W12 Loop, fungsi, debugging | NOT STARTED (T, K, V) | NOT STARTED (K, V, R) | NOT STARTED (K, M, P, R) | NOT STARTED (K, V) |
| W13 Database & SQL | NOT STARTED (T, K, V) | NOT STARTED (K, V, F) | NOT STARTED (K, M, P, F) | NOT STARTED (K, V) |
| W14 HTML/CSS | NOT STARTED (T, K, V) | NOT STARTED (K, V, F) | NOT STARTED (K, M, P, F) | NOT STARTED (K, V) |
| W15 Git/GitHub | NOT STARTED (T, K, V) | NOT STARTED (K, V, F) | NOT STARTED (K, M, P, F) | NOT STARTED (K, V) |
| W16 Capstone | NOT STARTED (T, K, V) | NOT STARTED (K, V, R) | NOT STARTED (K, M, X, R, F) | NOT STARTED (K, V) |

16 modul × 4 komponen = **64 komponen**: 0 selesai, 0 sebagian diterima,
64 NOT STARTED.

Catatan R: konten lab, fixture, dan rencana test minggu 9–12 (dan bagian
Python capstone) ditulis lengkap dan **dapat diterima sebagai perencanaan**
sebelum runtime dieksekusi (RM:RV-1–RV-3, [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §5.2).
Eksekusi tetap NOT VERIFIED (D-10). UW-21 (D-22) tidak memblokir penerimaan
itu (RM:RV-4). Bila runtime gagal setelah izin: implementasi terdampak
dihentikan dan kurikulum hanya diubah atas keputusan eksplisit owner, lalu
divalidasi ulang (RM:RV-5, RM:RV-6).

## 5. Estimasi jam belajar

Usulan alokasi lama di bagian ini (2,5/1,5/2,5/1,0/0,5) **digantikan** oleh
usulan CU2-O3 di [CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md)
§D (M/U/L/P/C/R per fase; total 128,0 jam; diperiksa aritmetika). Keduanya
**PROPOSED**; berlaku setelah owner memutuskan CU2-O3 (UW-36, D-25). Total
128 jam (BL:15) dan 16 modul × 4 komponen tetap wajib. Waktu remedial
tambahan yang bergantung pada pelajar berada di luar 128 jam nominal.

## 6. Batch produksi (PROPOSED)

| Batch | Isi | Prasyarat keputusan |
|---|---|---|
| CB-0 | Finalisasi templat ([CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md), PROVISIONAL) dan aturan konten | OP-5, CU-3, CU-5, CU2-O3, CU2-O4, OP-7, OP-8, OP-10 (OP-4 → D-23, CU-6 → D-24 sudah diputuskan) |
| CB-1 | Modul W1–W4 (16 komponen) | CB-0 |
| CB-2 | Modul W5–W8 (16 komponen) | CB-0 |
| CB-3 | Modul W9–W12 (16 komponen); diterima sebagai perencanaan, runtime NOT VERIFIED (RM:RV-1–RV-3) | CB-0, CU-11 |
| CB-4 | Modul W13–W16 (16 komponen), termasuk rubrik capstone | CB-0, CU-7, CU-9, CU-10 (desain bank soal) |
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
| CA-09 | Estimasi durasi sesuai alokasi CU2-O3 yang diputuskan; total modul 8,0 jam; total program tetap 128 jam (CC-09) |
| CA-10 | Tanpa AI grading/tutor; tanpa server wajib (BL:38) |
| CA-11 | Review manusia dan penerimaan owner tercatat |

## 8. Ketergantungan produksi

| ID | Keputusan | Status | Memblokir |
|---|---|---|---|
| OP-4 | Aturan kredit penjelasan konsep | **Diputuskan D-23** | — |
| CU-6 | Penilaian lab | **Diputuskan D-24**; LX-1–LX-5 OPEN | — (konten); LX untuk implementasi |
| OP-5 (UW-27) | Format soal, poin, durasi ujian | OPEN — [ASSESSMENT_FLOW_DECISION_SHEETS.md](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A | Kolom Theory |
| CU2-O4 (UW-36) | Rubrik mini-project W1–W15 | OPEN — [PROJECT_RUBRIC_DECISION_SHEETS.md](PROJECT_RUBRIC_DECISION_SHEETS.md) §A | Kolom Mini-project |
| CU-9 (UW-36) | Rubrik capstone | OPEN — idem §B | W16 Mini-project |
| CU-3 (UW-36) | Format konten | OPEN — [CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md) §A | CB-0, semua sel |
| CU-5 (UW-36) | Varian remedial | OPEN — idem §B | Semua sel |
| CU-7 (UW-36) | Lab SQL/HTML/Git | OPEN — idem §C | W13–W15 (dan bagian SQL/Git capstone) |
| CU2-O3 (UW-36) | Alokasi jam | OPEN — idem §D | Durasi semua modul |
| CU-11 (UW-36) | Pembagian W9/W10 | OPEN — idem §E | CB-3 |
| OP-7 (UW-29) | Pengumpulan dan interupsi | OPEN — AF §B | Instruksi lab/mini-project |
| OP-8, CU-4 (UW-30) | Identitas XP | OPEN — [XP_PROGRESS_DECISION_SHEET.md](XP_PROGRESS_DECISION_SHEET.md) | `activity_id` |
| OP-9 (UW-31) | Unlock rinci | OPEN — AF §C | Prasyarat modul |
| OP-10, OP-11 (UW-32) | Remedial dan autosave | OPEN — AF §D | Materi remedial |
| CU-10 (UW-25) | Risiko kunci jawaban | OPEN — [CU10_ANSWER_KEY_RISK_DECISION_SHEET.md](CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) | Desain bank soal |

Peta lengkap: [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §5.3. Templat dan
rencana ini bukan konten; status 64 sel tetap NOT STARTED.
