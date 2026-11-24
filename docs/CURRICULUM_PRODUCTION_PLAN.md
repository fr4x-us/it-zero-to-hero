# IT ZERO → HERO — Rencana Produksi Kurikulum (UW-37)

Status: **RENCANA** · dokumentasi saja · **belum ada konten yang
diproduksi** kecuali W1. UW-37 tetap **OPEN** (1/16 modul diproduksi, 0 diterima). Tanggal: **2026-11-24**
(diperbarui batch D-26–D-35). Basis: `main` = `40ca205` (merge PR #24).
Standar produksi CB-0 (FINAL, dokumentasi): [CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md). Modul acuan: [curriculum/mod-w01/](../curriculum/mod-w01/module.yaml).

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
topik capstone menunggu CU-9). Pembagian W9/W10: usulan PB-A revisi (konversi
angka dasar di W9; W10 tanpa percabangan/exception; tidak ada `try`/`except`
di W9–W12 maupun capstone)
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

Status: **PRODUCED** = konten lengkap ditulis dan lolos review mandiri
penyusun (TPL-19), **belum** direview ChatGPT dan **belum** diterima owner;
**NOT STARTED** = belum ada konten. Templat tidak dihitung.

Ketergantungan yang masih terbuka: **Q** = CU-6-Q13 (umpan balik test
tersembunyi lab kode); **R** = runtime Python (O-04, NOT VERIFIED — tidak
memblokir penerimaan perencanaan, RM:RV-1). Semua keputusan produksi lain
sudah diputuskan (D-23–D-35).

| Modul | Theory 30% | Laboratory 40% | Mini-project 20% | Concept 10% |
|---|---|---|---|---|
| W1 Hardware/software | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W2 OS & file | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W3 Jaringan | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W4 Keamanan siber | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W5 Dasar matematika | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W6 Biner & Boolean | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W7 Berpikir komputasional | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W8 Algoritma & flowchart | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W9 Dasar Python | NOT STARTED | NOT STARTED (R, Q) | NOT STARTED (R) | NOT STARTED |
| W10 Variabel & tipe data | NOT STARTED | NOT STARTED (R, Q) | NOT STARTED (R) | NOT STARTED |
| W11 Kondisi | NOT STARTED | NOT STARTED (R, Q) | NOT STARTED (R) | NOT STARTED |
| W12 Loop, fungsi, debugging | NOT STARTED | NOT STARTED (R, Q) | NOT STARTED (R) | NOT STARTED |
| W13 Database & SQL | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W14 HTML/CSS | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W15 Git/GitHub | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| W16 Capstone | NOT STARTED | NOT STARTED (R, Q) | NOT STARTED (R) | NOT STARTED |

### 4.1 Kemajuan produksi (dihitung dari berkas; jumlah butir, bukan kesiapan aplikasi)

| Ukuran | Diproduksi | Direview (ChatGPT) | Diterima owner | Runtime diverifikasi |
|---|---|---|---|---|
| Modul | 1/16 (W1) | 0/16 | 0/16 | Tidak berlaku untuk W1; 0 untuk modul kode |
| Komponen penilaian | 4/64 | 0/64 | 0/64 | — |
| Jam nominal tercakup | 8/128 | 0/128 | 0/128 | — |
| Soal teori | 40/620 | 0 | 0 | — |
| Soal concept | 12/192 | 0 | 0 | — |
| Spesifikasi lab | 6/96 | 0 | 0 | — |
| Spesifikasi mini-project | 1/16 | 0 | 0 | — |

Inventaris target D-30 (dua butir nyata per slot/aktivitas): teori
(15 × 20 + 10) × 2 = 620; concept 16 × 6 × 2 = 192; lab 16 × 3 × 2 = 96;
mini-project 15 + capstone 1 = 16.

Catatan R: konten lab, fixture, dan rencana test minggu 9–12 (dan bagian
Python capstone) ditulis lengkap dan **dapat diterima sebagai perencanaan**
sebelum runtime dieksekusi (RM:RV-1–RV-3, [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §5.2).
Eksekusi tetap NOT VERIFIED (D-10). UW-21 (D-22) tidak memblokir penerimaan
itu (RM:RV-4). Bila runtime gagal setelah izin: implementasi terdampak
dihentikan dan kurikulum hanya diubah atas keputusan eksplisit owner, lalu
divalidasi ulang (RM:RV-5, RM:RV-6).

## 5. Alokasi jam belajar (diputuskan D-32, HA-A)

Alokasi per modul dan total program: [CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md)
§D (M 40,25 · U 11,75 · L 32,5 · P 27,5 · C 8 · R 8 = 128 jam). U setiap
modul = ujian standar + review umpan balik terjadwal (W1: 33 + 12 menit).
Perpanjangan aksesibilitas, remedial, dan review opsional berada di luar
128 jam nominal. Usulan lama bagian ini (2,5/1,5/2,5/1,0/0,5) digantikan.

## 6. Batch produksi

| Batch | Isi | Status |
|---|---|---|
| CB-0 | Standar produksi ([CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md)) | **FINAL (dokumentasi)**, 1 field terbuka (CU-6-Q13, lab kode); belum diterima owner |
| CB-1a | W1 modul acuan ([curriculum/mod-w01/](../curriculum/mod-w01/module.yaml)) | **PRODUCED**, menunggu review dan penerimaan owner |
| CB-1b | W2–W4 (12 komponen) | NOT STARTED — mulai setelah W1 diterima |
| CB-2 | W5–W8 (16 komponen) | NOT STARTED |
| CB-3 | W9–W12 (16 komponen); diterima sebagai perencanaan, runtime NOT VERIFIED (RM:RV-1–RV-3) | NOT STARTED; lab kode butuh CU-6-Q13 |
| CB-4 | W13–W16 (16 komponen), termasuk capstone | NOT STARTED; lab kode W16 butuh CU-6-Q13 |
| CB-R | Review dan penerimaan seluruh 64 komponen oleh owner | NOT STARTED |

Setiap batch = satu PR dokumentasi; status sel §4 menjadi "diterima" hanya
setelah review dan otorisasi owner.

### 6.1 Rencana CB-1b (W2–W4) — disiapkan, belum diproduksi

**Pelajaran dari produksi W1:**

| # | Pelajaran | Perbaikan untuk modul berikutnya |
|---|---|---|
| 1 | Tujuh kompetensi awal tidak dapat dicakup oleh 6 slot concept | Rancang tepat 6 LO per modul (1 LO ↔ 1 kompetensi ↔ 1 slot concept) |
| 2 | Soal teori dan lab sempat memakai angka yang sama | Daftar angka/skenario per modul dicek silang antarkomponen sebelum ditulis |
| 3 | Durasi ujian 34 menit pada komposisi awal (> 33) | Hitung durasi dari blueprint **sebelum** menulis soal; batas W1–W15 = 33 menit agar review 12 menit muat |
| 4 | Pemeriksaan lab kecil (≤ 5 poin) memudahkan integer total | Pakai kelipatan 3 atau 5 per pemeriksaan agar jumlah tepat 30/30/40 |
| 5 | Mini-project dengan banyak solusi valid butuh enumerasi | Verifikasi katalog/fixture dengan enumerasi lengkap dan catat jumlah solusi valid |
| 6 | Validasi YAML konsisten (ID unik, kunci di opsi, poin) efektif menemukan galat | Jalankan pemeriksa dokumen yang sama untuk setiap modul (dokumentasi, bukan prototipe) |

**Perkiraan volume per modul (dari W1):** 4 pelajaran (≈ 750 baris
Markdown), 40 soal teori, 12 soal concept, 6 spesifikasi lab, 1
mini-project, materi remedial, review; ±40 berkas. CB-1b ≈ 3 × itu (±120
berkas) — disarankan satu PR per modul agar review tetap teliti.

**Ketergantungan konten W2–W4:** W2 (OS & file) memakai konsep software
sistem dari W1; lab W2 = simulasi struktur folder/path (bukan lab kode);
W3 (jaringan) lab simulasi alamat/subnet; W4 (keamanan) lab studi kasus.
Tidak ada lab kode → CU-6-Q13 tidak memblokir. Brief mini-project W2–W4
sudah ditetapkan (RB A.3, D-33).

**Risiko kualitas:** (1) W3 rentan kesalahan teknis (subnet, alamat
IPv4) — wajib aritmetika diperiksa; (2) W4 harus menghindari instruksi
berbahaya dan tetap pada praktik aman; (3) beban review besar — satu PR per
modul; (4) kesetaraan varian lab studi kasus W4 sulit — pakai struktur
skenario yang sama dengan data berbeda.

**Checkpoint review:** (a) W1 diterima owner → (b) W2 PR → review → (c) W3
PR → review → (d) W4 PR → review → (e) perbarui matriks §4.

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
| CA-09 | Estimasi durasi sesuai HA-A (D-32); total modul 480 menit; total program tetap 128 jam (CC-09) |
| CA-10 | Tanpa AI grading/tutor; tanpa server wajib (BL:38) |
| CA-11 | Review manusia dan penerimaan owner tercatat |

## 8. Ketergantungan produksi

Semua keputusan produksi diputuskan: OP-4 (D-23), CU-6 (D-24, D-35), OP-5
(D-26), OP-7/OP-9/OP-10/OP-11 (D-27), OP-8/CU-4 (D-28), CU-3/CU-5/CU2-O5
(D-30), CU-7 (D-31), CU2-O3/CU-11 (D-32), CU2-O4/CU-9 (D-33), CU-10 (D-34).

| Masih terbuka | Dampak |
|---|---|
| CU-6-Q13 umpan balik test tersembunyi | Field TPL-10 untuk lab kode W9–W12, W16 |
| Runtime Python (O-04, UW-12, NOT VERIFIED) | Tidak memblokir penerimaan perencanaan (RM:RV-1) |

Peta lengkap: [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §5.3.
