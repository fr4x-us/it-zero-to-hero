# IT ZERO → HERO — Decision Sheets Alur Penilaian (OP-5, OP-7, OP-9, OP-10, OP-11)

Status: **DIPUTUSKAN OWNER — D-26, D-27 (2026-11-24)**, lihat §F · dokumentasi saja · tanpa kode,
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

Contoh — dihitung ulang secara independen dari komposisi soal (revisi
review PR #24, F-06; aritmetika bilangan bulat, hasil sama dengan versi
sebelumnya, tidak ditemukan inkonsistensi):

| Langkah | Standar W1–W15 | W16 | 5 × TF-1 D1 | 30 × TF-4 D3 |
|---|---|---|---|---|
| Komposisi | TF-1: 5×D1, 4×D2, 1×D3 · TF-2: 1×D1, 1×D2, 1×D3 · TF-3: 2×D1, 1×D2, 1×D3 · TF-4: 1×D2, 1×D3 · TF-5: 1×D2 | TF-1: 3×D1, 2×D2 · TF-2: 1×D3 · TF-3: 1×D1, 1×D2 · TF-4: 1×D2, 1×D3 | TF-1: 5×D1 | TF-4: 30×D3 |
| Jumlah soal | 10 + 3 + 4 + 2 + 1 = **20** | 5 + 1 + 2 + 2 = **10** | 5 | 30 |
| Distribusi D1/D2/D3 | (5+1+2) / (4+1+1+1+1) / (1+1+1+1) = **8/8/4** | (3+1) / (2+1+1) / (1+1) = **4/4/2** | 5/0/0 | 0/0/30 |
| Waktu dasar | 10·45 + 3·75 + 4·60 + 2·90 + 1·75 = 450 + 225 + 240 + 180 + 75 = **1.170** | 5·45 + 1·75 + 2·60 + 2·90 = 225 + 75 + 120 + 180 = **600** | 5·45 = **225** | 30·90 = **2.700** |
| Tambahan kesulitan | 8·30 + 4·60 = 240 + 240 = **480** | 4·30 + 2·60 = 120 + 120 = **240** | 0 | 30·60 = **1.800** |
| `S` | **1.650** | **840** | **225** | **4.500** |
| `S_buffer = ⌈S·11/10⌉` | ⌈1.815⌉ = **1.815** | ⌈924⌉ = **924** | ⌈247,5⌉ = **248** | ⌈4.950⌉ = **4.950** |
| `⌈S_buffer/60⌉` | ⌈30,25⌉ = 31 | ⌈15,4⌉ = 16 | ⌈4,13…⌉ = 5 | ⌈82,5⌉ = 83 |
| `+ 2` menit | 33 | 18 | 7 | 85 |
| Batas | 10 ≤ 33 ≤ 45 | 10 ≤ 18 ≤ 45 | 7 < 10 → **10** | 85 > 45 → **blueprint ditolak** |
| **Durasi** | **33 menit** | **18 menit** | **10 menit** | — |
| Maks. poin (TP-B) | 8·2 + 8·3 + 4·4 = **56** | 4·2 + 4·3 + 2·4 = **28** | 10 | — |

Kecocokan dengan alokasi jam (CU2-O3, usulan): U W1–W15 = 0,75 jam = 45
menit = ujian 33 menit + review umpan balik terencana 12 menit; U W16 = 0,5
jam = 30 menit = ujian 18 menit + review 12 menit. Blueprint modul lain yang
menghasilkan durasi berbeda (≤ 45) tetap harus muat dalam U modulnya bersama
review; bila tidak, alokasi diubah lewat keputusan owner, tidak diam-diam.

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

### A.5a Aksesibilitas waktu ujian (revisi F-03)

Batas **45 menit** berlaku untuk **durasi standar** hasil rumus A.4
(syarat review blueprint). Perpanjangan aksesibilitas, bila disetujui, adalah
**pengecualian eksplisit** terhadap durasi standar, bukan perubahan rumus.

| Opsi | Isi | Durasi maksimum | Kelebihan | Kekurangan |
|---|---|---|---|---|
| TA-A | Tanpa perpanjangan | 45 menit | Paling sederhana | Pelajar dengan kebutuhan aksesibilitas tidak terakomodasi |
| **TA-B** | Pengaturan aksesibilitas "waktu ujian ×1,5": durasi diperpanjang = `⌈durasi_standar × 3 / 2⌉` | `⌈45 × 3 / 2⌉` = **68 menit** | Proporsional terhadap panjang ujian | Ujian standar 33 menit menjadi `⌈49,5⌉` = 50 menit |
| TA-C | Tambahan tetap +15 menit | 60 menit | Mudah dipahami | Tidak proporsional (ujian 10 menit mendapat +150%) |

Aturan bersama TA-B/TA-C (usulan):

| ID | Aturan |
|---|---|
| TA-1 | Pengaturan dipilih **sebelum** attempt dimulai; durasi standar, faktor/tambahan, dan durasi diperpanjang dicatat pada attempt dalam transaksi EX-1 |
| TA-2 | Tenggat attempt yang sedang berjalan **tidak pernah** diubah, termasuk bila pengaturan diubah di tengah ujian; perubahan berlaku untuk attempt berikutnya |
| TA-3 | Waktu tambahan berada **di luar** 128 jam nominal (sama seperti remedial); tidak mengurangi alokasi materi, lab, atau aktivitas lain |
| TA-4 | Riwayat attempt menampilkan bahwa perpanjangan dipakai (catatan belajar pribadi, D-17); tidak mengubah skor |

Hubungan dengan 128 jam: durasi ujian standar + review umpan balik ≤ U
modul (A.4). Waktu remedial dan perpanjangan aksesibilitas bergantung pada
pelajar dan berada di luar nominal.

### A.5b Persistensi jawaban di sekitar tenggat (revisi F-04)

Ujian teori **tidak** memakai debounce AS-B. Jawaban ujian pendek (pilihan,
urutan, jawaban singkat), sehingga setiap perubahan ditulis segera (AS-A
untuk ujian).

| ID | Aturan (usulan) |
|---|---|
| DL-1 | Setiap perubahan jawaban ujian menjadi satu permintaan tulis yang masuk antrean tulis tunggal per attempt (urutan FIFO) |
| DL-2 | Transaksi tulis jawaban membaca tenggat dan waktu commit di dalam transaksi; jawaban dengan waktu commit **≥ tenggat** ditolak (tenggat tidak termasuk, interval `[startedAt, tenggat)`) |
| DL-3 | UI menonaktifkan input saat sisa waktu tampilan mencapai 0; ini hanya kenyamanan. Penentu sah tetap DL-2 |
| DL-4 | Serahkan manual: (1) input dikunci, (2) permintaan tulis yang sudah antre diselesaikan (flush), (3) transaksi penguncian `SUBMITTED` dijalankan setelah antrean kosong; tulis yang datang sesudah penguncian ditolak |
| DL-5 | Tenggat tercapai saat aplikasi terbuka: penguncian dijalankan di antrean yang sama; tulis yang belum commit sebelum tenggat tidak dihitung (DL-2) |
| DL-6 | Input yang diketik tetapi belum ter-commit saat tenggat, process death, atau restart = **input belum tersimpan**: tidak dihitung, dan status UI saat itu tidak pernah menampilkan "Tersimpan" untuknya |
| DL-7 | Status autosave jujur: "Menyimpan…" saat permintaan antre, "Tersimpan" hanya setelah commit berhasil, "Gagal menyimpan" bila tulis gagal (dengan percobaan ulang otomatis selama sebelum tenggat) |
| DL-8 | **Kegagalan penyimpanan** (tulis ditolak sistem berkas/database, bukan karena tenggat) dicatat pada attempt sebagai `PERSISTENCE_FAILURE` beserta waktu kejadian; ini kegagalan infrastruktur, bukan input pelajar yang belum tersimpan |
| DL-9 | Tidak ada jaminan durabilitas tanpa syarat: jaminan "jawaban yang ditandai Tersimpan tidak hilang" hanya berlaku untuk commit yang berhasil; bila penyimpanan gagal atau tertunda, jaminan tidak berlaku dan DL-8 berlaku |

Perlakuan attempt dengan `PERSISTENCE_FAILURE` (butuh keputusan):

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **SF-A** | Dinilai dengan jawaban yang tersimpan; ditandai; tetap dihitung | Riwayat utuh; skor terbaik tidak pernah turun, sehingga attempt rendah tidak merugikan; remedial tanpa batas | Attempt itu mungkin tidak mencerminkan kemampuan |
| SF-B | Disimpan tetapi **tidak dihitung** untuk skor terbaik (seperti `EVALUATION_ERROR`) | Paling netral terhadap kegagalan sistem | Attempt dengan skor sah ikut hilang dari perhitungan; menambah state |

Skenario (Given–When–Then; dokumentasi, bukan test yang dijalankan):

| ID | Given | When | Then |
|---|---|---|---|
| DG-1 | Tenggat 10:00:00; jawaban soal 5 diubah 09:59:59,8; commit 09:59:59,9 | Tenggat tercapai | Jawaban soal 5 dihitung |
| DG-2 | Tenggat 10:00:00; jawaban diubah 09:59:59,9; commit tercatat 10:00:00,1 | Transaksi tulis berjalan | Ditolak (DL-2); nilai sebelumnya yang tersimpan dipakai |
| DG-3 | Pelajar menekan "Kumpulkan" 09:58; dua tulis masih antre | Penguncian | Dua tulis selesai lebih dulu, lalu `SUBMITTED` (DL-4) |
| DG-4 | Ujian berjalan; 3 jawaban berstatus "Tersimpan" | Process death, dibuka 09:59 | 3 jawaban kembali; sisa waktu dihitung dari tenggat |
| DG-5 | Ujian berjalan; jawaban terakhir berstatus "Menyimpan…" | Process death sebelum commit | Jawaban terakhir tidak ada (DL-6); tidak pernah ditampilkan "Tersimpan" |
| DG-6 | Ujian berjalan | Restart perangkat, dibuka setelah tenggat | Attempt dikunci dan dinilai dengan jawaban tersimpan (EX-6, bila disetujui) |
| DG-7 | Penyimpanan penuh; tulis gagal 09:50 | Percobaan ulang gagal sampai tenggat | Status "Gagal menyimpan"; attempt ditandai `PERSISTENCE_FAILURE`; perlakuan SF-A/SF-B |
| DG-8 | Tulis gagal 09:50, berhasil pada percobaan ulang 09:51 | Tenggat tercapai | Jawaban dihitung; kejadian kegagalan tetap tercatat |

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

**TQ-B + TF-1–TF-5 + TP-B + 40/40/20 + rumus A.4 + EX-1–EX-13 + TA-B
(TA-1–TA-4) + DL-1–DL-9 + SF-A + FB-A.** Alasan pendidikan: blueprint kompetensi menjamin cakupan; poin per
kesulitan menghargai penalaran; pembahasan langsung adalah umpan balik
formatif terpenting untuk pelajar mandiri. Implikasi teknis: blueprint dan
durasi dihitung saat review konten (deterministik, tanpa runtime); attempt
menyimpan durasi, tenggat, opsi TA, varian, dan versi soal.

Ketergantungan: CU-5 (varian), OP-6 (UW-28, jam), CU-3 (format konten),
CU2-O3 (alokasi jam; ujian 33 menit + review 12 menit = 0,75 jam
penilaian teori; W16: 18 + 12 menit = 0,5 jam).

### A.8 Acceptance criteria OP-5

| ID | Kriteria |
|---|---|
| AF-AC-01 | Rumus durasi tertulis dan contoh A.4 dapat dihitung ulang manual dengan hasil sama |
| AF-AC-02 | Setiap blueprint modul memenuhi `durasi ≤ 45` menit dan setiap kompetensi ≥ 2 soal |
| AF-AC-03 | Maks. poin teori per attempt ≤ 10.000 dan bilangan bulat |
| AF-AC-04 | Aturan EX-1–EX-13 tidak bertentangan dengan ASM §3.1, §5 |
| AF-AC-05 | Keputusan owner OP-5-Q1–Q8 tercatat → ASM:D-08 terisi (AC UW-27) |
| AF-AC-05a | Skenario DG-1–DG-8 tertulis dan konsisten dengan DL-1–DL-9 |

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
| **AS-B Bertingkat** | (1) Perubahan diskret (pilih opsi, urutan, pemetaan) disimpan **segera**; (2) teks/kode lab, mini-project, dan concept disimpan setelah jeda ketik **500 ms**, maksimum **5 detik** saat mengetik terus-menerus; (3) flush segera saat `onPause`/`onStop`, sebelum "Jalankan"/"Serahkan", dan saat berpindah aktivitas; (4) status DL-7. **Ujian teori memakai DL-1–DL-9 (tanpa debounce)** | Seimbang; indikator jujur | Saat penyimpanan sehat, input yang belum ter-commit pada crash/kill tanpa callback ≤ 5 detik pengetikan. **Bukan jaminan tanpa syarat**: bila tulis gagal atau tertunda, berlaku DL-8/DL-9 |
| AS-C Periodik 30 detik | Simpan berkala | Sederhana | Jendela kehilangan besar |

State kritis yang selalu ditulis segera dan transaksional (tanpa debounce):
mulai attempt + tenggat (EX-1), serahkan, hasil penilaian `GRADED`, award XP
(ASM:X-04), status unlock turunan, pemilihan varian.

**Konflik yang perlu diputuskan:** ASM:P-03 (PROPOSED) menulis "tidak boleh
membuat kehilangan pekerjaan yang sudah terlihat oleh pengguna setelah
process death". AS-B memenuhi ini untuk pekerjaan yang **ditampilkan sebagai
tersimpan** (M-07: status autosave terlihat), bukan untuk ketikan dalam
jendela debounce saat crash. AS-A memenuhi lebih ketat dengan biaya penulisan.

Kegagalan penyimpanan di lab/mini-project/concept: status "Gagal
menyimpan", percobaan ulang, dan pencatatan kejadian seperti DL-7–DL-8;
tidak ada batas waktu sesi sehingga tidak ada kehilangan karena tenggat.

Rekomendasi: **RE-A + PI-A + AS-B** (P-03 ditafsirkan sebagai "pekerjaan
yang ditandai tersimpan setelah commit berhasil tidak hilang"). Alasan pendidikan: pelajar
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
| OP-5-Q5 | EX-1–EX-13 (termasuk EX-12 varian per slot dan EX-13 tenggat baru untuk remedial), serta menyetujui ASM:T7/ASM:D-04/ASM:D-05 (dibuka setelah tenggat → dinilai dengan jawaban tersimpan)? | Ya |
| OP-5-Q6 | Aksesibilitas: TA-A / TA-B (×1,5, maks. 68 menit) / TA-C (+15 menit), dengan TA-1–TA-4 (dicatat sebelum mulai, tenggat aktif tidak diubah, di luar 128 jam)? | TA-B |
| OP-5-Q7 | Umpan balik FB-A (kunci dan pembahasan setelah dinilai)? | FB-A |
| OP-5-Q8 | Persistensi di sekitar tenggat DL-1–DL-9 dan perlakuan `PERSISTENCE_FAILURE` (SF-A/SF-B)? | DL-1–DL-9 + SF-A |
| OP-7-Q1 | SB-A (serah per aktivitas dalam attempt RA-1) dan SB-1–SB-12? | Ya |
| OP-9-Q1 | UL-1–UL-10 dengan PV-A dan RV-A (`PASSED` tidak dicabut oleh revisi konten)? | Ya |
| OP-10-Q1 | RE-A (semua komponen boleh diulang saat `NOT_PASSED`)? | RE-A |
| OP-10-Q2 | PI-A (perbaikan setelah lulus, tanpa XP baru, status tidak turun)? | PI-A |
| OP-11-Q1 | AS-B untuk lab/mini-project/concept (500 ms / maks. 5 detik saat penyimpanan sehat / flush siklus hidup / status jujur), ujian memakai DL-1–DL-9, dan tafsiran P-03 untuk commit yang berhasil? | AS-B |

~~Status: **AWAITING OWNER**. UW-27, UW-29, UW-31, UW-32 tetap BLOCKED.~~ *(Historis — dijawab owner 2026-11-24; lihat bagian keputusan di bawah.)*

## F. Keputusan owner — D-26, D-27 (2026-11-24)

Pernyataan owner: "Saya menyetujui rekomendasi D-26, D-27, D-28, D-29, D-30, D-31, D-32, D-33, D-34, D-35."

| Keputusan | Pertanyaan | Opsi yang disetujui | Sumber | AC terdampak |
|---|---|---|---|---|
| D-26 | OP-5-Q1–Q8 | TQ-B (20 soal W1–W15, 10 soal W16, ≥ 2 per kompetensi); TF-1–TF-5; TP-B (2/3/4) dan distribusi 40/40/20; rumus A.4 (standar 10–45 menit); EX-1–EX-13; TA-B (×1,5, maks. 68 menit) dengan TA-1–TA-4; FB-A; DL-1–DL-9 dengan SF-A | §A | ASM:D-08 terisi → UW-27 |
| D-27 | OP-7-Q1 | SB-A dan SB-1–SB-12 | §B | ASM:L5 terisi → UW-29 |
| D-27 | OP-9-Q1 | UL-1–UL-10, PV-A, RV-A | §C | ASM:C6 terisi → UW-31 |
| D-27 | OP-10-Q1, Q2 | RE-A, PI-A | §D.1 | OP-10 terisi → UW-32 |
| D-27 | OP-11-Q1 | AS-B (500 ms; target ≤ 5 detik saat penyimpanan sehat; state kritis segera; status Tersimpan/Menyimpan/Gagal jujur; tanpa jaminan durabilitas tanpa syarat); ujian memakai DL-1–DL-9 | §D.2 | OP-11 terisi → UW-32 |

Contoh durasi terverifikasi (A.4): standar 33 menit, W16 18 menit, batas
bawah 10, > 45 ditolak. Penerapan W1: 33 menit + review 12 menit = 45
menit ([curriculum/mod-w01/review.md](../curriculum/mod-w01/review.md) §3.2).
OP-6 (manipulasi jam, UW-28) tetap OPEN.
