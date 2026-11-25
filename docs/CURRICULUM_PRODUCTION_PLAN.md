# IT ZERO → HERO — Rencana Produksi Kurikulum (UW-37)

Status: **RENCANA** · dokumentasi saja · **belum ada konten yang
diproduksi** kecuali W1–W8. UW-37 tetap **OPEN** (8/16 modul diproduksi; 4/16 diterima owner secara historis — W1 W01-ACC, W2–W4 W02-ACC–W04-ACC; 16 varian revisi (D-39 + putaran 6) di W1–W4 PENDING (TPL-01a); W5–W8 diproduksi pada CB-2, menunggu review independen dan penerimaan owner; W9–W16 NOT STARTED / NOT AUTHORIZED). Tanggal: **2026-11-24**
(status aktif diperbarui pada CB-2). Basis: `main` = `846051f` (merge PR #27).
Standar produksi CB-0 (semua kebijakan terputuskan setelah D-36; tidak ada keputusan penerimaan owner terpisah untuk CB-0; review independen terbatas; **bukan** final global): [CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md). Modul acuan: [curriculum/mod-w01/](../curriculum/mod-w01/module.yaml).

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
penyusun (TPL-19); W1–W4 **diterima** owner (W01-ACC, §4.2; W02-ACC–W04-ACC, §4.3);
W5–W8 **belum** diterima (CB-2, menunggu review independen dan penerimaan owner);
**NOT STARTED** = belum ada konten. Templat tidak dihitung.

Ketergantungan: **Q** = CU-6-Q13 (umpan balik test tersembunyi lab kode) —
**sudah diputuskan D-36** (HF-A); tersisa verifikasi implementasi; **R** = runtime Python (O-04, NOT VERIFIED — tidak
memblokir penerimaan perencanaan, RM:RV-1). Semua keputusan produksi lain
sudah diputuskan (D-23–D-36).

| Modul | Theory 30% | Laboratory 40% | Mini-project 20% | Concept 10% |
|---|---|---|---|---|
| W1 Hardware/software | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W2 OS & file | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W3 Jaringan | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W4 Keamanan siber | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W5 Dasar matematika | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W6 Biner & Boolean | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W7 Berpikir komputasional | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
| W8 Algoritma & flowchart | **PRODUCED** (40 soal) | **PRODUCED** (6 spesifikasi) | **PRODUCED** (1) | **PRODUCED** (12 soal) |
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
| Modul | 8/16 (W1–W8) | 4/16 (W1–W4, terbatas) | 4/16 (W01-ACC–W04-ACC) | Tidak berlaku untuk W1–W8; 0 untuk modul kode |
| Komponen penilaian | 32/64 | 16/64 (terbatas) | 16/64 | — |
| Jam nominal tercakup | 64/128 | 32/128 (terbatas) | 32/128 | — |
| Soal teori | 320/620 | 160 (terbatas) | 160 | — |
| Soal concept | 96/192 | 48 (terbatas) | 48 | — |
| Spesifikasi lab | 48/96 | 24 (terbatas) | 24 | — |
| Spesifikasi mini-project | 8/16 | 4 (terbatas) | 4 | — |

Persentase: diproduksi 32/64 = 50%; diterima owner 16/64 = 25% (**historis**: isi pada saat W01-ACC–W04-ACC; 16 varian revisi (D-39 + putaran 6) di W1–W4 PENDING (TPL-01a), lihat blok `acceptance` di `module.yaml` W1–W4).

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
| CB-0 | Standar produksi ([CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md)) | Dipakai untuk W1–W4; semua kebijakan terputuskan (D-36); tidak ada keputusan penerimaan owner terpisah; review independen terbatas — **tidak** dinyatakan final global |
| CB-1a | W1 modul acuan ([curriculum/mod-w01/](../curriculum/mod-w01/module.yaml)) | **ACCEPTED** (W01-ACC, 2026-11-24; penerimaan terbatas, §4.2) |
| CB-1b | W2–W4 (12 komponen) | **ACCEPTED** (W02-ACC–W04-ACC, 2026-11-24; PR #27 merged `846051f`; review terarah dengan batas yang diungkapkan, §4.3) |
| CB-2 | W5–W8 (16 komponen) | **PRODUCED** (CB-2, satu PR baru); menunggu review independen dan penerimaan owner |
| CB-3 | W9–W12 (16 komponen); diterima sebagai perencanaan, runtime NOT VERIFIED (RM:RV-1–RV-3) | NOT STARTED / NOT AUTHORIZED; umpan balik test tersembunyi mengikuti D-36 |
| CB-4 | W13–W16 (16 komponen), termasuk capstone | NOT STARTED / NOT AUTHORIZED; lab kode W16 mengikuti D-36 |
| CB-R | Review dan penerimaan seluruh 64 komponen oleh owner | NOT STARTED |

Setiap batch = satu PR dokumentasi; status sel §4 menjadi "diterima" hanya
setelah review dan otorisasi owner.

### 6.1 Rencana CB-1b (W2–W4) — catatan historis (pra-produksi)

*Historis: bagian ini ditulis sebelum CB-1. W2–W4 sekarang diproduksi dan
dikoreksi (§4.3); pernyataan "belum diproduksi" dan "CU-6-Q13" di bawah
mencerminkan keadaan saat itu (CU-6-Q13 kini D-36).*

**Pelajaran dari produksi W1:**

| # | Pelajaran | Perbaikan untuk modul berikutnya |
|---|---|---|
| 1 | Tujuh kompetensi awal tidak dapat dicakup oleh 6 slot concept | Rancang tepat 6 LO per modul (1 LO ↔ 1 kompetensi ↔ 1 slot concept) |
| 2 | Soal teori dan lab sempat memakai angka yang sama | Daftar angka/skenario per modul dicek silang antarkomponen sebelum ditulis |
| 3 | Durasi ujian 34 menit pada komposisi awal (> 33) | Hitung durasi dari blueprint **sebelum** menulis soal; batas W1–W15 = 33 menit agar review 12 menit muat |
| 4 | Pemeriksaan lab kecil (≤ 5 poin) memudahkan integer total | Pakai kelipatan 3 atau 5 per pemeriksaan agar jumlah tepat 30/30/40 |
| 5 | Mini-project dengan banyak solusi valid butuh enumerasi | Verifikasi katalog/fixture dengan enumerasi lengkap dan catat jumlah solusi valid |
| 6 | Validasi YAML konsisten (ID unik, kunci di opsi, poin) efektif menemukan galat | Jalankan pemeriksa dokumen yang sama untuk setiap modul (dokumentasi, bukan prototipe) |
| 7 | Review PR #25: kunci menumpuk di posisi a/b, beberapa varian tidak setara, contoh proyek membocorkan jawaban, F8 tanpa pemeriksaan kebenaran | Cek posisi kunci, isi matriks kesetaraan, dan pastikan contoh untuk pelajar tidak memuat jawaban **sebelum** PR; setiap isian angka punya pemeriksaan kebenaran |
| 8 | Latihan dan contoh terbimbing sempat sama dengan butir bernilai | Cocokkan silang skenario/angka latihan dengan bank soal sebelum PR |
| 9 | Review PR #25 putaran 2: maksimum yang dinyatakan tidak dapat dicapai (act-02), arah konversi terbalik di remedial, asumsi model tidak tertulis, nama field tidak seragam | Terapkan QC-01–QC-10 (CB-0 §3b) pada setiap modul sebelum PR |

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
(D-30), CU-7 (D-31), CU2-O3/CU-11 (D-32), CU2-O4/CU-9 (D-33), CU-10 (D-34),
CU-6-Q13 (D-36).

| Masih terbuka | Dampak |
|---|---|
| Verifikasi implementasi D-36 (umpan balik test tersembunyi) | Field TPL-10 untuk lab kode W9–W12, W16; kebijakan sudah diputuskan |
| Runtime Python (O-04, UW-12, NOT VERIFIED) | Tidak memblokir penerimaan perencanaan (RM:RV-1) |

Peta lengkap: [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §5.3.

### 4.2 Catatan penerimaan W1 (2026-11-24)

"Terbatas" = lolos review akhir PR #25 dengan batas review independen yang
diungkapkan owner (lihat [review.md](../curriculum/mod-w01/review.md) §11).
W1 diterima sebagai modul acuan (W01-ACC). *Historis (saat W01-ACC):* W2–W16
belum dimulai. Status aktif: W2–W4 diterima (§4.3), W5–W8 diproduksi (§4.4), W9–W16 NOT STARTED.

### 4.3 Catatan produksi CB-1 (W2–W4, 2026-11-24)

| Modul | Teori (timer / review / TA-B) | Lab (aktivitas) | Concept maks. | Proyek | Bukti |
|---|---|---|---|---|---|
| W2 | 56 poin; 33 / 12 / 50 menit (S = 1.680) | 30 + 30 + 40 | 20 | Menata folder proyek (1 keadaan bernilai penuh) | [`mod-w02/review.md`](../curriculum/mod-w02/review.md) |
| W3 | 56 poin; 32 / 13 / 48 menit (S = 1.635) | 30 + 40 + 30 | 21 | Rencana alamat /24 (78.485.511.600 rencana bernilai penuh) | [`mod-w03/review.md`](../curriculum/mod-w03/review.md) |
| W4 | 56 poin; 32 / 13 / 48 menit (S = 1.635) | 30 + 40 + 30 | 20 | Rencana keamanan akun (163.840 rencana bernilai penuh) | [`mod-w04/review.md`](../curriculum/mod-w04/review.md) |

Pelajaran dari CB-1 untuk modul berikutnya: (1) pemindai kebocoran V-L
otomatis menemukan kebocoran nyata di setiap modul (judul tabel, pertanyaan
Ya/Tidak, contoh pelajaran) — jalankan sebelum PR; (2) verifikasi
aritmetika dengan pustaka independen (mis. `ipaddress`) menemukan satu
salah tulis; (3) posisi kunci perlu diseimbangkan ulang setiap modul;
(4) W3 dibatasi mask /24 agar tidak bergantung pada W6 — modul jaringan
lanjutan (bila ada) memerlukan biner.

**Koreksi konsolidasi CB-1 (PR #27, 2026-11-24).** Review PR #27 = REQUEST
CHANGES (F-28–F-70). Disposisi per temuan ada di `review.md` masing-masing
modul (§ register koreksi). Skor maksimum, durasi, dan XP tidak berubah
(tabel di atas tetap). *Historis (putaran 1):* F-55–F-57 dan F-59 BLOCKED — rincian temuan asli
tidak tersedia. Status: diproduksi dan dikoreksi; **belum diterima**.

**Koreksi terarah putaran 2 (delta review PR #27).** Deskripsi F-55–F-57
dan F-59 dipulihkan owner dan ditangani; temuan baru F-71 (W2) dan F-72
(W4) diperbaiki; F-51 mengubah normalisasi satuan kecepatan W3 menjadi peka
huruf. Register 45 ID (F-28–F-72), tanpa BLOCKED. Skor maksimum, durasi, dan
XP tetap. Status: dikoreksi; **belum diterima**.

**Penerimaan W2–W4 (2026-11-24).** Owner: "PR #27 telah direview ChatGPT
dan disetujui untuk merge." Verdict review independen: *PASS — targeted
delta review with disclosed limitations* (F-49–F-59 dan F-71–F-72 lolos
review terarah; integritas register F-28–F-72 diverifikasi; 16 simulasi
normalisasi independen lolos; regresi historis penuh, skrip validasi
sementara, uji pelajar, dan verifikasi runtime Android **tidak** diulang
secara independen). Dicatat sebagai W02-ACC, W03-ACC, W04-ACC; penerimaan
ini **bukan** verifikasi menyeluruh.

### 4.4 Catatan produksi CB-2 (W5–W8, 2026-11-24)

| Modul | Teori (timer / review / TA-B) | Lab (aktivitas) | Concept maks. | Proyek | Bukti |
|---|---|---|---|---|---|
| W5 | 56 poin; 33 / 12 / 50 menit (S = 1.665) | 30 + 40 + 30 | 20 | Tabel anggaran belajar | [`mod-w05/review.md`](../curriculum/mod-w05/review.md) |
| W6 | 56 poin; 33 / 12 / 50 menit (S = 1.665) | 30 + 40 + 30 | 20 | Logika alarm rumah | [`mod-w06/review.md`](../curriculum/mod-w06/review.md) |
| W7 | 56 poin; 33 / 12 / 50 menit (S = 1.650) | 30 + 40 + 30 | 20 | Dekomposisi tugas jadwal belajar (6 urutan valid) | [`mod-w07/review.md`](../curriculum/mod-w07/review.md) |
| W8 | 56 poin; 33 / 12 / 50 menit (S = 1.650) | 30 + 40 + 30 | 20 | Flowchart nilai maksimum (2 kombinasi blok benar) | [`mod-w08/review.md`](../curriculum/mod-w08/review.md) |

Aturan bentuk jawaban yang dipakai (di bawah EB-4/D-24, **bukan** kebijakan
baru): NB-5 (bilangan: koma desimal, titik pemisah ribuan berkelompok 3),
BN-6 (biner 0/1 tanpa awalan, tak bertanda), B01 (nilai Boolean 0/1), BX
(ekspresi Boolean: variabel, AND/OR/NOT, kurung). Flowchart W8 ditulis
sebagai tabel blok bernomor; format editor flowchart di aplikasi (M-10)
dan bentuk entri ekspresi Boolean tetap **OPEN** untuk owner.

Pelajaran dari CB-2: (1) pemindai V-L dan tinjauan manual menemukan
tumpang-tindih contoh pelajaran ↔ butir bernilai di setiap modul; (2)
pemeriksa bentuk angka perlu uji mutasi (regex awal salah mengurai `18.8`);
(3) generator `module.yaml` mencegah salah sambung templat; (4) alternatif
jawaban setara (urutan topologis, ekspresi ekuivalen, `>`/`≥`) harus
dienumerasi dan ditulis eksplisit di rubrik.

### 4.5 Cakupan kompetensi hibrida D-39 (2026-11-25)

Owner memilih opsi C (D-39) untuk PR28-06. Audit W1–W8 terhadap 156 konsep
wajib: 15 GAP sebelum koreksi (W1 1, W2 8, W3 2, W4 3, W6 1), 0 sesudah
koreksi terarah (hasil penulis) pada 14 varian butir (`item_version: '2.0'`). Kandidat W5/W6
yang semula dicatat PASS tanpa perubahan. Matriks:
[CURRICULUM_COVERAGE_MATRIX_W01_W08.md](CURRICULUM_COVERAGE_MATRIX_W01_W08.md).
Penerimaan W01-ACC–W04-ACC tetap tercatat untuk isi yang diterima; butir
W1–W4 yang diubah **belum** diterima dan memerlukan review delta
independen. Angka produksi/penerimaan (32/64, 16/64 historis) tidak berubah.

Putaran 4 (review `4ddc993`): R3-03 (keselamatan prosedur W2 concept s05
vA/vB), R3-05–R3-07 (W3 concept s02 vB, W4 concept s02 vB, s05 vA)
direvisi; R3-04 koreksi bukti saja. Status penerimaan terstruktur TPL-01a:
14 varian W1–W4 PENDING (putaran 6: 16). Paket validasi dokumentasi: `docs/validation/`.

**Putaran 5 (review `796043c`)**: cakupan = **hasil penulis** 153 PASS, 3 OPEN (bukti semantik lemah: W3 peran router/switch, W4 OTP), 0 GAP; kesetaraan varian 43 PASS, 5 OPEN (W3 s03, W4 s01, s03, W7 s02, s03); usulan koreksi menunggu otorisasi owner (matriks §7). PR28-06 tetap OPEN.

**Putaran 6 (koreksi terarah, otorisasi owner terbatas)**: diterapkan hanya W3 concept s03 vB, W4 concept s03 vB, W7 concept s02 vB, W7 concept s03 vB (versi 2.0; posisi kunci tetap). Cakupan = **hasil penulis** 153 PASS, 3 OPEN (W3 router/switch, W4 OTP — usulan §7 tidak diotorisasi), 0 GAP; kesetaraan 47 PASS, 1 OPEN (W4 concept s01). R5-01 elemen bernilai tepat, R5-04 NB-5 konten cacat, R5-05 field slot bersama di validator penerimaan; 16 varian W1–W4 PENDING. CB-2 belum diterima; PR28-06 tetap OPEN.
