# IT ZERO → HERO — Decision Sheets Alur Penilaian (OP-5, OP-7, OP-9, OP-10, OP-11)

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode,
skema database, atau prototipe. Tanggal: **2026-11-24**. Basis: `main` =
`928e278` (merge PR #23). Kode rujukan: `AF:`.

Semua rekomendasi adalah saran, **bukan** keputusan. Lembar ini tidak
mengubah [BLUEPRINT_LOCKED.md](BLUEPRINT_LOCKED.md), D-01–D-25, atau aturan
penilaian terkunci. Bagian yang berlaku untuk semua lembar:

| ID | Batasan yang sudah disetujui | Sumber |
|---|---|---|
| AF-R1 | Bobot 30/40/20/10; modul lulus bila nilai tertimbang ≥ 80 **dan** setiap komponen ≥ 75; perbandingan eksak tanpa pembulatan dini | BL:27–32, D-04, D-12 |
| AF-R2 | Poin mentah bilangan bulat; maks. 10.000 per komponen per attempt; skor terbaik per komponen; tie → attempt paling awal | D-12 |
| AF-R3 | Remedial tanpa batas; semua attempt disimpan (append-only) | BL:33–34, ASM:P-07 |
| AF-R4 | Ujian teori berwaktu dengan tenggat persisten; timer berjalan saat aplikasi ditutup; status autosave terlihat | BL:36, D-01 M-07 |
| AF-R5 | Lab dan mini-project **tidak berwaktu**; jeda/lanjut; autosave dan pemulihan | BL:37, D-01 M-08 |
| AF-R6 | Unlock linear per modul; pratinjau materi modul berikutnya boleh; latihan/ujian terkunci sampai prasyarat lulus; modul lulus tetap dapat diakses | BL:21, D-01 M-04, D-04 |
| AF-R7 | Penilaian objektif offline tanpa AI | BL:38 |
| AF-R8 | Penjelasan konsep: D-23 (CE-B, CE-S1–S5, CE-V1–V6). Lab: D-24 (LW-B, LR-A, RA-1, TB-B/TB-A, LA-1–LA-4, IE-1–IE-5) | D-23, D-24 |
| AF-R9 | Waktu kejadian disimpan sebagai instant UTC; tanggal lokal dan tampilan Asia/Tokyo | ASM:D-07, CAL:Z-01–Z-02 |
| AF-R10 | Tanpa tenggat kalender wajib; jadwal fleksibel mengikuti shift | D-01 M-03 |

---

## A. OP-5 — Ujian teori dan durasi ujian (UW-27)

AC UW-27: **ASM:D-08 terisi** (rumus durasi dan format soal tertulis dan
diputuskan owner).

### A.1 Jumlah soal per modul

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| TQ-A Tetap 20 soal semua modul | Sama di W1–W16 | Sederhana | W16 (capstone 5 jam) terlalu berat |
| **TQ-B Blueprint per modul** | W1–W15: 20 soal; W16: 10 soal (ujian integrasi); setiap kompetensi modul ≥ 2 soal | Cakupan kompetensi terjamin; sesuai beban W16 | Blueprint harus ditulis per modul |
| TQ-C Per kompetensi | 2 soal × jumlah kompetensi | Proporsional | Durasi bervariasi besar antar modul |

### A.2 Format soal teori

| ID | Format | Penilaian |
|---|---|---|
| TF-1 | Pilihan tunggal (4 opsi) | Semua-atau-tidak (sama dengan CE-S1) |
| TF-2 | Pilihan ganda (beberapa benar) | Opsi TP di A.3 |
| TF-3 | Jawaban singkat eksak (angka, biner, kata kunci) | Cocok eksak setelah normalisasi yang ditulis per soal (spasi tepi dibuang; aturan huruf besar/kecil eksplisit); jawaban alternatif eksplisit (selaras CE-K2) |
| TF-4 | Membaca/menelusuri kode, flowchart, tabel | Pilihan tunggal atau jawaban singkat eksak |
| TF-5 | Mengurutkan / mencocokkan | Opsi TP di A.3 |

Esai bebas **tidak** dipakai (BL:38). Validasi jawaban mengikuti CE-V1–CE-V6
(D-23): kosong = 0; ID asing/ganda/bentuk salah = 0 dengan
`INVALID_ANSWER`.

### A.3 Alokasi poin dan tingkat kesulitan

Tingkat kesulitan: **D1** mengingat/memahami, **D2** menerapkan, **D3**
menganalisis.

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| TP-A | Setiap soal 1 poin, semua-atau-tidak | Paling sederhana | Soal analisis bernilai sama dengan soal hafalan |
| **TP-B** | Poin per kesulitan D1 = 2, D2 = 3, D3 = 4; setiap soal teori semua-atau-tidak (termasuk TF-2 dan TF-5) | Bobot mencerminkan kesulitan; deterministik; integer | Berbeda dari kredit parsial concept explanation (D-23) — perbedaan disengaja: teori mengukur ketepatan, concept explanation mengukur pemahaman bertahap |
| TP-C | Seperti TP-B, tetapi TF-2/TF-5 memakai kredit parsial CE-S2/CE-S3/CE-S4 dengan maks. struktural | Konsisten dengan D-23 | Maks. soal tidak lagi sama dengan poin kesulitan; perlu aturan skala tambahan |

Distribusi kesulitan (usulan): **40% D1, 40% D2, 20% D3** (jumlah soal).
W1–W15: 8/8/4 → maks. `8·2 + 8·3 + 4·4 = 56` poin. W16: 4/4/2 → maks.
`28` poin. Keduanya jauh di bawah batas 10.000 (D-12).

### A.4 Rumus durasi (memenuhi D-01 M-07: dari jumlah, jenis, dan kompleksitas)

Waktu dasar per soal (detik): TF-1 = 45, TF-2 = 75, TF-3 = 60, TF-4 = 90,
TF-5 = 75. Tambahan kesulitan: D1 = 0, D2 = 30, D3 = 60.

```
S        = Σ (dasar(format) + tambahan(kesulitan))           [detik, bilangan bulat]
S_buffer = ⌈S × 11 / 10⌉                                     [+10% membaca ulang]
durasi   = ⌈S_buffer / 60⌉ + 2                               [menit; +2 menit instruksi]
durasi   = max(10, durasi)                                   [batas bawah]
syarat   : durasi ≤ 45, bila tidak blueprint ditolak saat review konten (bukan dipotong)
```

Contoh (diperiksa dengan aritmetika bilangan bulat 2026-11-24):

| Blueprint | Komposisi | S | S_buffer | Durasi |
|---|---|---|---|---|
| Standar W1–W15 (20 soal, 8/8/4) | TF-1: 5×D1, 4×D2, 1×D3; TF-2: 1×D1, 1×D2, 1×D3; TF-3: 2×D1, 1×D2, 1×D3; TF-4: 1×D2, 1×D3; TF-5: 1×D2 | 1.650 | 1.815 | ⌈30,25⌉ + 2 = **33 menit** |
| W16 (10 soal, 4/4/2) | TF-1: 3×D1, 2×D2; TF-3: 1×D1, 1×D2; TF-4: 1×D2, 1×D3; TF-2: 1×D3 | 840 | 924 | ⌈15,4⌉ + 2 = **18 menit** |
| 5 soal TF-1 D1 | — | 225 | 248 | 7 → batas bawah **10 menit** |
| 30 soal TF-4 D3 | — | 4.500 | 4.950 | 85 > 45 → **blueprint ditolak** |

Opsi lain: TD-B durasi tetap per modul (tidak memenuhi M-07 "bukan timer
global tunggal"); TD-C durasi = jumlah soal × 90 detik (mengabaikan jenis
dan kompleksitas). Keduanya tidak direkomendasikan.

### A.5 Tenggat, jawaban kosong, pengumpulan otomatis, interupsi

| ID | Aturan (usulan) | Dasar |
|---|---|---|
| EX-1 | Tenggat absolut = `startedAt + durasi`, disimpan (instant UTC) dalam satu transaksi **sebelum** soal pertama tampil | ASM:T1, D-01 |
| EX-2 | Timer tidak pernah dijeda: ditutup, process death, restart, mati baterai | D-01 M-07, ASM:T3 |
| EX-3 | Sisa waktu selalu dihitung dari tenggat tersimpan | ASM:D-03 |
| EX-4 | Soal tidak dijawab = 0 poin; bukan `INVALID_ANSWER`; tidak mencegah pengumpulan | CE-V1 (analog) |
| EX-5 | Saat tenggat tercapai dengan aplikasi terbuka: attempt dikunci dan dinilai dengan jawaban yang tersimpan **sebelum** tenggat (cap waktu simpan dibandingkan tenggat dalam satu transaksi) | ASM:T6, E-06 |
| EX-6 | Dibuka kembali setelah tenggat: dikunci dan dinilai dengan jawaban tersimpan (T7). Status saat ini PROPOSED (RECOVERED) — **butuh persetujuan eksplisit** (OP-5-Q5) | ASM:T7, ASM:D-04, ASM:D-05 |
| EX-7 | Pengumpulan manual sebelum tenggat butuh konfirmasi; dialog menampilkan jumlah soal belum dijawab | OP-7 (B) |
| EX-8 | Tidak ada perpanjangan waktu otomatis karena interupsi; remedial tanpa batas dengan skor terbaik membuat interupsi tidak merugikan secara permanen | AF-R3 |
| EX-9 | Kegagalan penilaian karena konten rusak/kunci hilang (bukan kesalahan pelajar): attempt berstatus `EVALUATION_ERROR`, tidak dihitung untuk skor terbaik, dinilai ulang setelah konten valid, **tanpa** penalti dan tanpa attempt baru | D-23, D-24 (IE-2 analog) |
| EX-10 | Manipulasi jam dan toleransi NTP mengikuti keputusan OP-6 (UW-28), tidak diputuskan di sini | ASM:E-01–E-04 |
| EX-11 | Jam tenang hanya mengatur notifikasi; tidak menghentikan timer | ASM:E-08, BL:57 |

Opsi aksesibilitas (baru, butuh keputusan): **TA-A** tanpa perpanjangan;
**TA-B** pengaturan aksesibilitas "waktu ujian ×1,5" yang dipilih sebelum
attempt dimulai dan dicatat pada attempt (durasi = `⌈durasi × 3 / 2⌉`).
TA-B mendukung BL:71 (UI aksesibel); risikonya hanya terhadap catatan
belajar pribadi (D-17).

### A.6 Varian remedial dan umpan balik

| ID | Aturan (usulan) |
|---|---|
| EX-12 | Setiap slot blueprint (kompetensi × format × kesulitan) punya varian setara; jumlah minimum dan pemilihan deterministik: CU-5 ([CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md) §B) |
| EX-13 | Attempt remedial membuat tenggat baru; tenggat attempt lama tidak berubah (ASM:D-06) |

| Opsi umpan balik | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **FB-A** | Setelah `GRADED`: skor, rincian per kompetensi, soal benar/salah, kunci dan pembahasan per soal | Nilai belajar tertinggi | Varian dapat dihafal bila bank kecil |
| FB-B | Hanya rincian per kompetensi | Melindungi bank soal | Pelajar tidak tahu kesalahannya |
| FB-C | Pembahasan penuh hanya setelah modul lulus | Kompromi | Remedial tanpa umpan balik spesifik |

### A.7 Rekomendasi OP-5 dan alasan

**TQ-B + TF-1–TF-5 + TP-B + 40/40/20 + rumus A.4 + EX-1–EX-13 + TA-B +
FB-A.** Alasan pendidikan: blueprint kompetensi menjamin cakupan; poin per
kesulitan menghargai penalaran; pembahasan langsung adalah umpan balik
formatif terpenting untuk pelajar mandiri. Implikasi teknis: blueprint dan
durasi dihitung saat review konten (deterministik, tanpa runtime); attempt
menyimpan durasi, tenggat, opsi TA, varian, dan versi soal.

Ketergantungan: CU-5 (varian), OP-6 (UW-28, jam), CU-3 (format konten),
CU2-O3 (alokasi jam; ujian 33 menit muat dalam 0,75 jam penilaian teori).

### A.8 Acceptance criteria OP-5

| ID | Kriteria |
|---|---|
| AF-AC-01 | Rumus durasi tertulis dan contoh A.4 dapat dihitung ulang manual dengan hasil sama |
| AF-AC-02 | Setiap blueprint modul memenuhi `durasi ≤ 45` menit dan setiap kompetensi ≥ 2 soal |
| AF-AC-03 | Maks. poin teori per attempt ≤ 10.000 dan bilangan bulat |
| AF-AC-04 | Aturan EX-1–EX-13 tidak bertentangan dengan ASM §3.1, §5 |
| AF-AC-05 | Keputusan owner OP-5-Q1–Q7 tercatat → ASM:D-08 terisi (AC UW-27) |

---

## B. OP-7 — Pengumpulan dan interupsi (UW-29)

AC UW-29: **ASM:L5 terisi**.

### B.1 Opsi pengumpulan lab (dalam RA-1, D-24)

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **SB-A Serah per aktivitas** | Dalam satu attempt komponen, setiap aktivitas diserahkan sendiri (mengunci aktivitas itu dan memicu evaluasi); attempt komponen selesai setelah semua aktivitas selesai (LA-1, LA-2) | Sesuai LA-1 "aktivitas selesai = diserahkan dan dievaluasi"; umpan balik bertahap | Pelajar perlu memahami dua tingkat (aktivitas dan komponen) |
| SB-B Serah sekaligus | Semua aktivitas diserahkan bersama | Satu langkah | Umpan balik terlambat; tidak menafsirkan LA-1 secara langsung |

### B.2 Aturan (usulan)

| ID | Aturan |
|---|---|
| SB-1 | **Draf**: setiap perubahan tersimpan otomatis (OP-11); state `IN_PROGRESS`/`SAVED` (ASM:L2–L4) |
| SB-2 | **Jalankan (latihan)**: pelajar boleh menjalankan kode terhadap test **terlihat** tanpa batas; tidak dinilai, tidak memberi XP, tidak membuat attempt (eksekusi tetap NOT VERIFIED) |
| SB-3 | **Serahkan**: tindakan eksplisit dengan dialog konfirmasi yang menyebut: aktivitas akan dikunci, test tersembunyi dijalankan, dan jumlah aktivitas tersisa |
| SB-4 | Satu attempt aktif per komponen; attempt baru hanya setelah attempt aktif selesai (LA-2) |
| SB-5 | Aplikasi ditutup / process death / restart sebelum diserahkan: pekerjaan pulih dari draf terakhir yang tercatat tersimpan (ASM:L3–L4, P-05–P-06) |
| SB-6 | Proses mati **saat evaluasi**: kegagalan infrastruktur IF-2; evaluasi aktivitas diulang utuh dari submission yang sama saat dibuka kembali; tidak ada attempt baru (IE-2, D-24) |
| SB-7 | Evaluasi ulang tidak pernah mengubah submission; hasil hanya dicatat sekali per evaluasi yang selesai (IE-3) |
| SB-8 | Pekerjaan dalam attempt yang belum selesai tidak kedaluwarsa (tanpa batas waktu, AF-R5) |
| SB-9 | Attempt tidak dapat dihapus atau dibatalkan; attempt yang belum selesai tetap tercatat apa adanya (append-only) |
| SB-10 | **Mini-project**: deliverable dibuat di aplikasi (kode, jawaban terstruktur, tabel, berkas teks, keadaan simulasi Git); diserahkan sekali per attempt dengan konfirmasi; dinilai otomatis dengan rubrik objektif (CU2-O4, CU-9). Tidak ada reviewer manusia di aplikasi; centang "sudah selesai" oleh pelajar tidak memberi poin |
| SB-11 | Attempt remedial mini-project boleh dimulai dari salinan submission sebelumnya (MPV-A, CU-5); attempt lama tidak berubah |
| SB-12 | Restore saat attempt `IN_PROGRESS`: mengikuti OD-9 (UW-33), tidak diputuskan di sini |

### B.3 Rekomendasi OP-7

**SB-A + SB-1–SB-12.** Alasan pendidikan: umpan balik per aktivitas
mendukung belajar bertahap; latihan tanpa nilai mendorong eksperimen. Implikasi
teknis: dua tingkat penyelesaian (aktivitas, komponen); evaluasi dapat
diulang secara idempoten. Ketergantungan: OP-11 (autosave), OD-9 (UW-33),
CU-5 (MPV-A), CU2-O4/CU-9 (rubrik).

AC OP-7: AF-AC-06 — ASM:L5 terisi dengan SB-1–SB-12; AF-AC-07 — skenario
SB-5, SB-6 tertulis sebagai Given–When–Then; AF-AC-08 — tidak ada aturan
yang menambah batas waktu pada lab/mini-project.

---

## C. OP-9 — Unlock modul (UW-31)

AC UW-31: **ASM:C6 terisi**.

| ID | Aturan (usulan) | Status dasar |
|---|---|---|
| UL-1 | Saat mulai: W1 terbuka penuh; pratinjau materi W2 terbuka | D-01 M-04 |
| UL-2 | Modul `Wn+1` terbuka penuh saat `Wn` berstatus `PASSED` (AF-R1) | D-04 |
| UL-3 | Pratinjau: hanya materi pelajaran modul **berikutnya** (baca saja); latihan, lab, mini-project, concept, dan ujian terkunci | D-01 M-04 |
| UL-4 | Di dalam modul terbuka tidak ada urutan wajib antarkomponen; aplikasi menampilkan urutan yang disarankan (materi → latihan → lab → mini-project → concept → ujian) | AF-R10 (fleksibel) |
| UL-5 | Modul `PASSED` tetap dapat diakses penuh (materi, latihan, riwayat) | D-01 M-04 |
| UL-6 | Remedial tersedia di modul yang sedang dikerjakan dan modul yang sudah lulus (cakupan: OP-10) | BL:33 |
| UL-7 | W16 (capstone) terbuka setelah W15 `PASSED`; karena linear, W1–W15 sudah lulus | BL:21, D-13 |
| UL-8 | Status unlock **diturunkan** dari attempt dan aturan unlock, tidak disimpan sebagai sumber kebenaran terpisah (ASM:RM-08); setelah restore dihitung ulang dari data yang dipulihkan | ASM:P-08, CUR:RM-08 |
| UL-9 | Revisi konten tidak mencabut status `PASSED`; attempt dinilai menurut versi konten saat dikerjakan | ASM §2.3 (OPEN), CUR §4.1 |
| UL-10 | Tidak ada unlock lewat XP, level, atau pembelian; tidak ada unlock tanpa lulus | BL:49 |

Opsi pratinjau: **PV-A** hanya modul berikutnya (sesuai D-01 M-04,
direkomendasikan); PV-B semua modul berikutnya (memperluas D-01 M-04 → butuh
revisi owner). Opsi UL-9: **RV-A** `PASSED` permanen (direkomendasikan);
RV-B dinilai ulang terhadap versi baru (melanggar ASM:P-07 semangat
append-only dan membingungkan pelajar).

Rekomendasi: **UL-1–UL-10 + PV-A + RV-A.** Alasan: urutan konsep tetap
terjaga (prasyarat W6 → W8 → W9) sementara fleksibilitas di dalam modul
mendukung jadwal shift. AC: AF-AC-09 — ASM:C6 terisi; AF-AC-10 — status
unlock dapat dihitung ulang dari attempt saja (skenario restore).

---

## D. OP-10 dan OP-11 — Cakupan remedial dan autosave (UW-32)

AC UW-32: **OP-10 dan OP-11 terisi**.

### D.1 OP-10 — Komponen yang boleh diulang

| Opsi | Isi | Konsekuensi |
|---|---|---|
| **RE-A** | Saat modul `NOT_PASSED`, **setiap** komponen boleh diulang, termasuk yang sudah ≥ 75 | Wajib agar tidak buntu: contoh ASM:B-02 (75/75/75/75 → W = 75 < 80) tidak punya komponen < 75; dengan RE-B pelajar terkunci selamanya. RE-A satu-satunya opsi yang konsisten dengan BL:33 |
| RE-B | Hanya komponen < 75 | **Konflik**: menimbulkan kebuntuan di B-02 dan B-06 |

| Opsi setelah lulus | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **PI-A** | Modul `PASSED`: attempt perbaikan boleh untuk komponen mana pun; skor terbaik dapat naik; status `PASSED` tidak dapat turun (skor terbaik tidak pernah turun); tanpa XP baru untuk identitas yang sama | Mendukung penguasaan; remedial tanpa batas | Rapor dapat berubah naik |
| PI-B | Tidak boleh mengulang setelah lulus | Rapor stabil | Membatasi belajar ulang |

Aturan bersama: attempt remedial = catatan baru dari `NOT_STARTED`
(ASM §3.3); attempt lama tidak berubah; skor terbaik per komponen; tie →
attempt paling awal (D-12); tidak ada batas jumlah attempt.

### D.2 OP-11 — Autosave dan debounce

Fakta platform (dokumentasi resmi Android, tidak diverifikasi di perangkat):
crash atau kill proses tidak selalu memberi callback siklus hidup; `onPause`
/`onStop` tidak dijamin saat crash. Karena itu "tidak kehilangan apa pun
setelah crash" hanya dapat dijamin untuk data yang sudah ditulis ke database.

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| AS-A Setiap perubahan | Tulis transaksi pada setiap ketukan/perubahan | Kehilangan minimum | Penulisan sangat sering saat mengetik kode |
| **AS-B Bertingkat** | (1) Perubahan diskret (pilih opsi, urutan, pemetaan) disimpan **segera**; (2) teks/kode disimpan setelah jeda ketik **500 ms**, maksimum **5 detik** saat mengetik terus-menerus; (3) flush segera saat `onPause`/`onStop`, sebelum "Jalankan"/"Serahkan", dan saat berpindah aktivitas; (4) indikator "Tersimpan" hanya tampil setelah penulisan berhasil | Seimbang; indikator jujur | Jendela kehilangan ≤ 5 detik pengetikan hanya pada crash/kill tanpa callback |
| AS-C Periodik 30 detik | Simpan berkala | Sederhana | Jendela kehilangan besar |

State kritis yang selalu ditulis segera dan transaksional (tanpa debounce):
mulai attempt + tenggat (EX-1), serahkan, hasil penilaian `GRADED`, award XP
(ASM:X-04), status unlock turunan, pemilihan varian.

**Konflik yang perlu diputuskan:** ASM:P-03 (PROPOSED) menulis "tidak boleh
membuat kehilangan pekerjaan yang sudah terlihat oleh pengguna setelah
process death". AS-B memenuhi ini untuk pekerjaan yang **ditampilkan sebagai
tersimpan** (M-07: status autosave terlihat), bukan untuk ketikan dalam
jendela debounce saat crash. AS-A memenuhi lebih ketat dengan biaya penulisan.

Rekomendasi: **RE-A + PI-A + AS-B** (P-03 ditafsirkan sebagai "pekerjaan
yang ditandai tersimpan tidak pernah hilang"). Alasan pendidikan: pelajar
dapat memperbaiki komponen mana pun untuk mencapai W ≥ 80. Implikasi teknis:
tidak ada skema yang ditetapkan; pengukuran beban tulis termasuk verifikasi
setelah implementasi diizinkan (NOT VERIFIED).

AC: AF-AC-11 — tidak ada kombinasi skor yang membuat modul buntu (diperiksa
terhadap ASM:B-01–B-10); AF-AC-12 — jendela kehilangan maksimum tertulis dan
disetujui owner; AF-AC-13 — daftar state kritis tertulis.

---

## E. Pertanyaan untuk owner

| ID | Pertanyaan | Rekomendasi |
|---|---|---|
| OP-5-Q1 | Jumlah soal: TQ-B (20 soal W1–W15, 10 soal W16, setiap kompetensi ≥ 2)? | TQ-B |
| OP-5-Q2 | Format soal TF-1–TF-5 tanpa esai? | Ya |
| OP-5-Q3 | Poin: TP-B (D1/D2/D3 = 2/3/4, semua-atau-tidak) dan distribusi 40/40/20? | TP-B |
| OP-5-Q4 | Rumus durasi A.4 (batas bawah 10 menit; blueprint > 45 menit ditolak)? | Ya |
| OP-5-Q5 | EX-1–EX-11, termasuk menyetujui ASM:T7/ASM:D-04/ASM:D-05 (dibuka setelah tenggat → dinilai dengan jawaban tersimpan)? | Ya |
| OP-5-Q6 | Perpanjangan waktu aksesibilitas TA-B (×1,5, dipilih sebelum mulai)? | TA-B |
| OP-5-Q7 | Umpan balik FB-A (kunci dan pembahasan setelah dinilai)? | FB-A |
| OP-7-Q1 | SB-A (serah per aktivitas dalam attempt RA-1) dan SB-1–SB-12? | Ya |
| OP-9-Q1 | UL-1–UL-10 dengan PV-A dan RV-A (`PASSED` tidak dicabut oleh revisi konten)? | Ya |
| OP-10-Q1 | RE-A (semua komponen boleh diulang saat `NOT_PASSED`)? | RE-A |
| OP-10-Q2 | PI-A (perbaikan setelah lulus, tanpa XP baru, status tidak turun)? | PI-A |
| OP-11-Q1 | AS-B (500 ms / maks. 5 detik / flush siklus hidup) dan tafsiran P-03 untuk pekerjaan yang ditandai tersimpan? | AS-B |

Status: **AWAITING OWNER**. UW-27, UW-29, UW-31, UW-32 tetap BLOCKED.
