# IT ZERO → HERO — Spesifikasi Kurikulum dan Konten Lab Offline

Status: PERSIAPAN · dokumentasi saja · silabus rinci **belum** disetujui.
Tanggal: **2026-11-23**.

Dokumen ini memetakan kurikulum terhadap blueprint dan menyiapkan format
konten serta lab. Dokumen ini tidak menulis materi pelajaran, bank soal,
atau test case, dan tidak mengubah [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md).

## 0. Label

| Label | Arti |
|---|---|
| **APPROVED** | Blueprint (`BL:n`) atau Batch 02 (`TD:n`). |
| **RECOVERED** | Hanya asal-usul historis: butir berasal dari [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) (B01). Bukan status persetujuan. |
| **OWNER APPROVED WITH CONDITIONS** | Disetujui owner melalui D-01 (PR #18) sebagaimana tertulis di kolom "Disetujui owner" B01 §7.1. Detail di kolom "Masih OPEN / PARTIAL" **tidak** ikut disetujui. Ditulis `OWNER APPROVED WITH CONDITIONS (D-01 M-xx)`. |
| **NOT VERIFIED** | Klaim yang masih menunggu bukti (uji, build, atau sumber resmi). |
| **PROPOSED** | Usulan dokumen ini; perlu persetujuan owner. |
| **OPEN** | Belum diputuskan. |

Label sumber Batch 01 diseragamkan (UW-45, 2026-11-23): persetujuan
sumber Batch 01 melalui D-01 **tidak** otomatis menyetujui setiap rincian
teknis yang diusulkan dokumen ini. Butir B01 di luar M-01–M-19 (mis. B01
§3) tetap PROPOSED kecuali disetujui keputusan lain.

Dokumen terkait: [`ASSESSMENT_STATE_MACHINE_SPEC.md`](ASSESSMENT_STATE_MACHINE_SPEC.md),
[`PYTHON_OFFLINE_FEASIBILITY_PLAN.md`](PYTHON_OFFLINE_FEASIBILITY_PLAN.md),
[`QUALITY_GATES.md`](QUALITY_GATES.md) (GR, LB),
[`PLANNING_HISTORY.md`](PLANNING_HISTORY.md).

## 1. Audit cakupan kurikulum

| ID | Butir | Status | Sumber |
|---|---|---|---|
| K-01 | 16 minggu, nominal 128 jam | APPROVED | BL:15 |
| K-02 | Empat fase: (1) IT foundations; (2) Mathematics and computational thinking; (3) Python programming; (4) Database, web basics, Git, capstone | APPROVED | BL:16–20 |
| K-03 | Modul dibuka linear | APPROVED | BL:21 |
| K-04 | Teori akademik, diagram, lab, latihan, kuis, proyek, ujian, ringkasan | APPROVED | BL:22–23 |
| K-05 | Video YouTube online opsional | APPROVED | BL:24 |
| K-06 | Mulai Januari 2027 | OWNER APPROVED WITH CONDITIONS (D-01 M-14) | B01 M-14 |
| K-07 | 8 jam/minggu; default Sabtu 4 jam + Minggu 4 jam; dapat dipindah karena shift | OWNER APPROVED WITH CONDITIONS (D-01 M-03, M-14) | B01 M-03, M-14 |
| K-08 | Empat fase × empat modul (satu modul per minggu) | OWNER APPROVED WITH CONDITIONS (D-01 M-02, M-04) | B01 M-02, M-04 |
| K-09 | Garis besar 16 minggu (lihat §2) | OWNER APPROVED WITH CONDITIONS (D-01 M-02) | B01 M-02 |
| K-10 | Audiens: pemula berbahasa Indonesia yang bersiap kuliah IT; materi utama Bahasa Indonesia | PROPOSED (RECOVERED, B01 §3; di luar M-01–M-19) | B01 §3 |
| K-11 | Tambahan: ilustrasi interaktif, simulasi, glosarium, studi kasus | PROPOSED (RECOVERED, B01 §3; di luar M-01–M-19) | B01 §3 |
| K-12 | Latihan adaptif berbasis aturan; blueprint kompetensi tetap untuk ujian formal | PROPOSED (RECOVERED, B01 §3; di luar M-01–M-19) | B01 §3 |
| K-13 | Naskah pelajaran, contoh, diagram, bank soal | **Belum ditulis** | B01 M-02 |

Cek konsistensi (PROPOSED):

- 16 minggu × 8 jam = **128 jam** → konsisten dengan BL:15.
- Urutan garis besar B01 (§2) mengikuti urutan fase BL:16–20 → konsisten.
- Perkiraan: bila minggu 1 dimulai akhir pekan pertama Januari 2027 tanpa
  penjadwalan ulang, fase Python (minggu 9) dimulai sekitar akhir Februari
  2027. Tanggal pasti bergantung jadwal pengguna (A).

## 2. Matriks per minggu

Topik minggu = OWNER APPROVED WITH CONDITIONS (D-01 M-02); asal RECOVERED. Kolom lain = **PROPOSED** sebagai
kerangka; isi rinci (tujuan terukur, materi, soal) **OPEN**.

Kolom "Runtime" menunjukkan apakah lab minggu itu bergantung pada O-04
(eksekusi Python offline).

| Mg | Fase | Topik (B01) | Tujuan belajar (PROPOSED, ringkas) | Teori | Latihan/kuis | Lab (jenis) | Runtime |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Hardware dan software | Menjelaskan komponen komputer dan peran software | ✓ | ✓ | Identifikasi/klasifikasi komponen | Tidak |
| 2 | 1 | OS dan file | Menjelaskan fungsi OS, proses, sistem file | ✓ | ✓ | Simulasi struktur folder/path | Tidak |
| 3 | 1 | Jaringan | Menjelaskan alamat, protokol dasar, model lapisan | ✓ | ✓ | Simulasi alamat/subnet sederhana | Tidak |
| 4 | 1 | Keamanan siber | Mengenali ancaman umum dan praktik aman | ✓ | ✓ | Studi kasus/skenario pilihan | Tidak |
| 5 | 2 | Dasar matematika | Operasi dan notasi yang dipakai di pemrograman | ✓ | ✓ | Latihan numerik bernilai pasti | Tidak |
| 6 | 2 | Biner dan logika Boolean | Konversi basis; tabel kebenaran | ✓ | ✓ | Konversi biner; evaluator ekspresi Boolean | Tidak |
| 7 | 2 | Berpikir komputasional | Dekomposisi, pola, abstraksi | ✓ | ✓ | Penyusunan langkah/urutan | Tidak |
| 8 | 2 | Algoritma dan flowchart | Menyusun dan menelusuri algoritma | ✓ | ✓ | Flowchart dan *trace table* | Tidak |
| 9 | 3 | Dasar Python | Menulis dan menjalankan program pertama | ✓ | ✓ | Python | **Ya (O-04)** |
| 10 | 3 | Variabel dan tipe data | Memakai variabel dan tipe dasar | ✓ | ✓ | Python | **Ya (O-04)** |
| 11 | 3 | Kondisi | Percabangan | ✓ | ✓ | Python | **Ya (O-04)** |
| 12 | 3 | Loop, fungsi, debugging | Perulangan, fungsi, menemukan bug | ✓ | ✓ | Python | **Ya (O-04)** |
| 13 | 4 | Database dan SQL | Query dasar | ✓ | ✓ | SQL di database latihan terpisah | Tidak (SQLite; lihat §6) |
| 14 | 4 | HTML/CSS | Struktur dan gaya halaman | ✓ | ✓ | HTML/CSS | Tidak Python; penilaian render **OPEN** (§6) |
| 15 | 4 | Git/GitHub | Konsep versi, commit, branch | ✓ | ✓ | Simulasi alur Git | Tidak Python; bentuk simulasi **OPEN** (§6) |
| 16 | 4 | Capstone | Menggabungkan keterampilan | ✓ | — | Proyek akhir | **Kemungkinan (OPEN)** |

Komponen penilaian per minggu/modul:

| Komponen (BL:27–30) | Penempatan (PROPOSED) |
|---|---|
| Theory 30% | Ujian teori berwaktu per modul atau per fase — **OPEN** (OP-1 agregasi) |
| Laboratory 40% | Lab per modul |
| Mini-project 20% | Satu per fase atau per modul — **OPEN** (B01 M-09) |
| Concept explanation 10% | Tugas terstruktur objektif per modul (B01 M-06), rubrik **OPEN** |

Catatan gap: topik minggu 9 ("dasar Python") dan 10 ("variabel dan tipe
data") berpotensi tumpang-tindih; pembagian rinci **OPEN**.

## 3. Pemetaan domain ke fase

| Domain | Minggu | Fase BL | Status |
|---|---|---|---|
| IT fundamentals (hardware, OS, jaringan, keamanan) | 1–4 | 1 | OWNER APPROVED WITH CONDITIONS (D-01 M-02) |
| Matematika, logika, berpikir komputasional, algoritma | 5–8 | 2 | OWNER APPROVED WITH CONDITIONS (D-01 M-02) |
| Python | 9–12 | 3 | OWNER APPROVED WITH CONDITIONS (D-01 M-02) |
| SQL | 13 | 4 | OWNER APPROVED WITH CONDITIONS (D-01 M-02) |
| HTML/CSS | 14 | 4 | OWNER APPROVED WITH CONDITIONS (D-01 M-02) |
| Git | 15 | 4 | OWNER APPROVED WITH CONDITIONS (D-01 M-02) |
| Capstone | 16 | 4 | OWNER APPROVED WITH CONDITIONS (D-01 M-02, M-09); isi OPEN |

## 4. Format konten offline dan identitas stabil (PROPOSED)

### 4.1 Hierarki dan ID

| Entitas | Contoh ID (ilustrasi) | Aturan |
|---|---|---|
| Fase | `phase-1` | Tetap selamanya |
| Modul | `mod-w01` | Satu per minggu; tetap |
| Pelajaran | `mod-w01.les-01` | Tetap; urutan terpisah dari ID |
| Aktivitas | `mod-w01.les-01.act-quiz-01` | Jenis: bacaan, latihan, kuis, lab, ujian, proyek, penjelasan konsep |
| Soal/item | `item-<id unik>` + `item_version` | Varian soal punya ID sendiri dan menunjuk kompetensi yang sama |
| Kompetensi | `comp-w06-boolean-01` | Dipakai blueprint ujian dan latihan adaptif |
| Attempt | UUID per attempt | Menunjuk `activity_id` + `content_version` |

Aturan:

- ID tidak pernah dipakai ulang untuk konten berbeda.
- Perbaikan konten menaikkan versi, bukan mengganti ID.
- Attempt menyimpan versi konten saat dikerjakan, agar riwayat tetap
  dapat ditafsirkan setelah konten direvisi.
- Hubungan identitas aktivitas dengan identitas XP (TD:38) dan perlakuan
  konten yang direvisi (TD:39): **OPEN**.

### 4.2 Paket konten

| Bagian | Isi (PROPOSED) |
|---|---|
| Manifest | Versi paket, bahasa, daftar modul, checksum setiap file |
| Modul | Metadata, daftar pelajaran, kompetensi |
| Pelajaran | Teks (format markup ringan, OPEN), diagram (format OPEN), glosarium, ringkasan |
| Aktivitas | Definisi soal/lab, jawaban kunci, test case |
| Media opsional | Tautan YouTube (tidak dibundel; butuh jaringan) |

Konten dibundel dalam APK dan divalidasi checksum saat dimuat (selaras
dataset kalender). Mekanisme pembaruan konten: **OPEN**.

Risiko: kunci jawaban dan test case tersembunyi yang dibundel di APK
dapat diekstrak pengguna yang mahir. Ini konsekuensi penilaian offline
dan sejalan dengan temuan BKP:T-03 di [`ENCRYPTED_BACKUP_RESTORE_SPEC.md`](ENCRYPTED_BACKUP_RESTORE_SPEC.md);
penerimaan risikonya **OPEN** (owner).

## 5. Spesifikasi lab objektif (PROPOSED)

| Elemen | Spesifikasi |
|---|---|
| Input | Instruksi, kode/skema awal, data contoh |
| Output yang diharapkan | Nilai, teks, tabel hasil query, struktur dokumen, atau jalur flowchart yang dapat dibandingkan secara deterministik |
| Test case | Terlihat (contoh) dan tersembunyi; deterministik; tanpa waktu nyata/acak kecuali di-seed (LB-5) |
| Skor | Persentase bobot test case yang lulus → skor 0–100 tanpa pembulatan untuk keputusan (TD:21) |
| Rubrik | Hanya kriteria yang dapat diperiksa mesin; tanpa AI (BL:38); rubrik proyek **OPEN** (B01 M-09) |
| Batas eksekusi | Waktu, memori, ukuran output — nilai **OPEN** (O-04, PY:F-11–F-13) |
| Penyimpanan | Autosave pekerjaan; jeda/lanjut; attempt append-only (ASSESSMENT §3.2, §4) |
| Pengumpulan | Mengunci attempt lalu menilai; aturan rinci **OPEN** (B01 M-08) |
| Umpan balik | Test yang gagal ditampilkan tanpa membocorkan seluruh test tersembunyi (kebijakan OPEN) |

## 6. Lab tanpa vs dengan runtime Python

| Jenis lab | Minggu | Butuh Python runtime (O-04) | Catatan |
|---|---|---|---|
| Klasifikasi, simulasi IT dasar | 1–4 | Tidak | Evaluator jawaban di aplikasi |
| Numerik, biner, Boolean | 5–6 | Tidak | Evaluator pasti (konversi, tabel kebenaran) |
| Urutan langkah, flowchart, trace table | 7–8 | Tidak | Penilaian objektif (LB-7); format editor flowchart **OPEN** |
| Python | 9–12 | **Ya** | Bergantung hasil PY:F-01–F-15; **belum terbukti** |
| SQL | 13 | Tidak (SQLite platform) | Database latihan terpisah dan sementara (LB-6); dialek dan dataset **OPEN** (B01 M-10); B01 meminta tidak mengasumsikan sandbox SQL sebelum diuji |
| HTML/CSS | 14 | Tidak | Penilaian struktur (parsing) vs render visual; render butuh WebView, yang menurut B01 tidak boleh diasumsikan sebelum diuji → **OPEN** |
| Git | 15 | Tidak | Tidak ada Git CLI di Android; lab berupa simulasi konsep → bentuk **OPEN** |
| Capstone | 16 | Kemungkinan | Isi **OPEN** (B01 M-09) |

Temuan: **minggu 1–8 dan 13–15 tidak bergantung pada O-04**. Hanya
minggu 9–12 dan kemungkinan 16 yang terblokir bila runtime Python gagal.

Bila O-04 gagal (kondisi eskalasi di `PYTHON_OFFLINE_FEASIBILITY_PLAN.md`
§7), alternatif untuk minggu 9–12 harus diputuskan owner karena memengaruhi
kurikulum terkunci (BL:19, BL:41). Dokumen ini tidak memilih alternatif.

## 7. Remedial, variasi soal, progres tanpa XP farming

| ID | Aturan | Status |
|---|---|---|
| RM-01 | Remedial tanpa batas | APPROVED (BL:33) |
| RM-02 | Setiap attempt disimpan; skor terbaik per komponen dipertahankan | APPROVED (BL:34) |
| RM-03 | Ujian formal memakai blueprint kompetensi tetap; latihan adaptif berbasis aturan | PROPOSED (RECOVERED, B01 §3) |
| RM-04 | Bank soal berisi beberapa varian setara per kompetensi agar remedial tidak sekadar menghafal; jumlah varian minimum **OPEN** | PROPOSED |
| RM-05 | Remedial ujian teori memilih varian berbeda dari attempt sebelumnya bila tersedia | PROPOSED |
| RM-06 | Latihan adaptif mengulang kompetensi yang lemah; aturan pemilihan **OPEN** | PROPOSED |
| RM-07 | XP sekali per identitas aktivitas; remedial dan pengulangan latihan tidak memberi XP itu lagi; tanpa penalti | APPROVED (TD:22, BL:35) |
| RM-08 | Progres modul (dibuka/selesai/lulus) dihitung dari attempt dan aturan unlock, bukan dari XP | APPROVED arah (BL:49); aturan unlock **OPEN** (B01 M-04) |
| RM-09 | Varian soal yang berbeda tidak menjadi identitas aktivitas baru untuk XP (mencegah farming lewat varian) | PROPOSED; definisi identitas **OPEN** (TD:22) |

## 8. Acceptance criteria konten

| ID | Kriteria | Gate |
|---|---|---|
| CC-01 | Setiap modul memuat teori, diagram, latihan, kuis, lab, ringkasan (BL:22–23) dan glosarium | K-04 |
| CC-02 | Materi inti dapat dipakai tanpa internet; video hanya pelengkap | OF-1, OF-2 |
| CC-03 | Bahasa Indonesia untuk penjelasan; istilah teknis Inggris dijelaskan | K-10 |
| CC-04 | Setiap soal terhubung ke satu kompetensi dan punya kunci jawaban yang dapat diperiksa mesin | GR-7 |
| CC-05 | Setiap kompetensi ujian punya ≥ N varian setara (N **OPEN**) | RM-04 |
| CC-06 | Tidak ada soal ambigu: satu jawaban benar atau aturan penilaian eksplisit; direview manusia | GR-7 |
| CC-07 | Setiap lab punya test case terlihat dan tersembunyi yang deterministik | LB-5 |
| CC-08 | Tugas penjelasan konsep berbentuk terstruktur (mis. pilihan, urutan, pencocokan, isian terbatas) dan dinilai tanpa AI | BL:38, B01 M-06 |
| CC-09 | Total estimasi waktu per minggu ≈ 8 jam; total 128 jam | BL:15, K-07 |
| CC-10 | Diagram punya deskripsi teks (aksesibilitas) | UI:A-10 |
| CC-11 | Checksum paket konten valid saat dimuat | §4.2 |

Skenario (Given–When–Then, bukan test executable):

| ID | Given | When | Then |
|---|---|---|---|
| S-01 | Mode pesawat | Buka modul minggu 3 | Teori, diagram, latihan, lab tampil; video ditandai tidak tersedia |
| S-02 | Ujian modul gagal | Mulai remedial | Varian soal berbeda (bila tersedia); attempt baru tersimpan; XP tidak bertambah untuk identitas yang sama |
| S-03 | Lab biner minggu 6 | Kirim jawaban benar | Skor 100 tanpa runtime Python |
| S-04 | Lab SQL minggu 13 | Jalankan `DELETE` | Hanya database latihan berubah; database aplikasi utuh (LB-6) |
| S-05 | Konten direvisi ke versi baru | Lihat riwayat attempt lama | Attempt menunjuk versi konten saat dikerjakan |
| S-06 | Runtime Python belum lolos uji | Buka lab minggu 9 | Perilaku sesuai keputusan owner (OPEN); tidak ada klaim eksekusi |

## 9. Audit gap M-01–M-19

Status B01 sebagaimana tertulis; kolom "Tambahan Batch 03–08" hanya
menunjuk dokumen yang menjabarkan kriteria, **bukan** menutup gap.

| ID | Topik | Status B01 | Tambahan Batch 03–08 | Gap tersisa |
|---|---|---|---|---|
| M-01 | Riwayat perencanaan | PARTIAL | — | Transkrip asli tidak ada; status B01 diselesaikan D-01 (M-01: ringkasan, bukan transkrip) |
| M-02 | Isi pelajaran | PARTIAL | Matriks §2 (kerangka) | Naskah, contoh, diagram, bank soal |
| M-03 | Alokasi jam | PARTIAL | CC-09 | Alokasi per pelajaran |
| M-04 | Aturan unlock | PARTIAL | ASM:C6, OP-9 | Aturan partial/remedial/pratinjau |
| M-05 | Rumus penilaian | PARTIAL | ASSESSMENT §6 | Agregasi, representasi angka (OP-1–OP-3) |
| M-06 | Penjelasan konsep | PARTIAL | CC-08 | Bank tugas dan rubrik |
| M-07 | Ujian teori | PARTIAL | ASSESSMENT §5 | Rumus durasi, format soal |
| M-08 | Lab/proyek fleksibel | PARTIAL | ASSESSMENT §3.2, §5 di sini | Aturan pengumpulan/interupsi |
| M-09 | Mini-project/capstone | OPEN | — | Topik, rubrik, fixture, uji |
| M-10 | Spesifikasi lab | PARTIAL | §5–6 di sini; Python plan | Library Python, dialek/dataset SQL, batas eksekusi; O-04 |
| M-11 | XP/gamifikasi | PARTIAL | ASSESSMENT §7; RM-07–RM-09 | Rumus, batas, level, badge, identitas |
| M-12 | Presentasi kalender | PARTIAL | Calendar spec | Label era, format |
| M-13 | Kalender perusahaan | PARTIAL | Calendar spec §4 | Sumber/impor, default |
| M-14 | Jadwal dan pengingat | PARTIAL | CAL:Z-04–Z-05 | Perilaku notifikasi, izin, Doze |
| M-15 | Snapshot lokal | PARTIAL | Backup spec OD-8 | Frekuensi, retensi |
| M-16 | Backup/restore | PARTIAL | Backup spec | Algoritma/parameter, mode restore |
| M-17 | Visual | PARTIAL | UI spec §2 | Kontras palet, tipografi, aset |
| M-18 | Layar | PARTIAL | UI spec §3 | Field tiap layar |
| M-19 | Aksesibilitas/perangkat | PARTIAL | UI spec §4–5; toolchain sheet | minSdk, breakpoint, target terukur |

## 10. Keputusan OPEN

| ID | Keputusan | Rujukan |
|---|---|---|
| CU-1 | *(Kerangka disetujui D-01 M-02.)* Tujuan belajar per minggu tetap PROPOSED | §2, §11 |
| CU-2 | Penempatan ujian teori dan mini-project (per modul/per fase) | §2, OP-1 |
| CU-3 | Format konten (markup teks, diagram) dan mekanisme pembaruan konten | §4.2 |
| CU-4 | Identitas aktivitas untuk XP dan perlakuan konten direvisi | §4.1, TD:38–39 |
| CU-5 | Jumlah varian minimum per kompetensi dan aturan latihan adaptif | RM-04, RM-06 |
| CU-6 | Batas eksekusi lab dan kebijakan umpan balik test tersembunyi | §5 |
| CU-7 | Dialek dan dataset SQL; bentuk lab HTML/CSS (parsing vs render); bentuk simulasi Git | §6 |
| CU-8 | Alternatif minggu 9–12 bila O-04 gagal | §6 |
| CU-9 | Topik, rubrik, dan fixture mini-project/capstone | M-09 |
| CU-10 | Penerimaan risiko kunci jawaban dapat diekstrak dari APK | §4.2 |
| CU-11 | Pembagian topik minggu 9 dan 10 | §2 |

## 11. Keputusan owner terkait (2026-11-23)

| Keputusan | Dampak | Status butir |
|---|---|---|
| D-01 M-02 | Kerangka kurikulum 16 minggu disetujui; materi lengkap belum selesai | CU-1: kerangka **disetujui**; tujuan rinci per minggu tetap PROPOSED |
| D-01 M-04 | Pratinjau modul berikutnya boleh; latihan/ujian terkunci sampai prasyarat lulus; modul lulus tetap dapat diakses | RM-08 diperjelas |
| D-04 | Kelulusan per modul (empat komponen); program = 16 modul lulus + capstone | CU-2: implikasi bahwa setiap modul memiliki keempat komponen **perlu dikonfirmasi owner**; CU-9 tetap OPEN |
| D-08 | `INTERNET` diizinkan untuk fitur opsional | CC-02 tetap: materi inti harus offline |
| D-10 | Ambang uji Python disetujui; eksekusi tidak diizinkan | Lab minggu 9–12 tetap bergantung pada O-04 (NOT VERIFIED) |
