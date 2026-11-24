# IT ZERO → HERO — Final Planning Readiness Review (Batch 10)

Status: PERSIAPAN · audit dokumentasi saja · **tidak** memberi izin
implementasi. Tanggal: **2026-11-23**. Basis: `main` = `caa9d8a`
(merge PR #14).

Sumber keputusan terkunci: [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md).
Dokumen ini tidak mengubah keputusan apa pun dan tidak menutup butir OPEN.
Rekomendasi di sini adalah **saran untuk owner**, bukan keputusan.

## 1. Inventaris dokumen dan PR

| # | Dokumen | Peran | PR | Status |
|---|---|---|---|---|
| 1 | [`CLAUDE.md`](../CLAUDE.md) | Instruksi proyek | — / Batch 10 (rujukan NO AUTO-MERGE) | Aktif |
| 2 | [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) | Keputusan produk terkunci | — | LOCKED |
| 3 | `.claude/skills/*` (5 skill) | Panduan teknis pihak ketiga | #1 | Merged |
| 4 | [`ENVIRONMENT.md`](ENVIRONMENT.md) | Audit lingkungan, rencana CI | #2 | Merged |
| 5 | [`QUALITY_GATES.md`](QUALITY_GATES.md) | Gate verifikasi | #3 | Merged |
| 6 | [`PLANNING_HISTORY.md`](PLANNING_HISTORY.md) | Inventaris keputusan berbasis repo (snapshot) | #4 | Merged |
| 7 | [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) | Batch 01, suplemen perencanaan (root repo) | #5 | Merged; header *DRAFT FOR OWNER REVIEW* (B-3) |
| 8 | [`GITHUB_BRIDGE.md`](GITHUB_BRIDGE.md), template Issue/PR, [`HANDOFF_STATE.md`](HANDOFF_STATE.md), [`DECISIONS_LOG.md`](DECISIONS_LOG.md) | Alur kerja | #6 | Merged |
| 9 | [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md) | Keputusan teknis owner-approved | #7 | Merged |
| 10 | [`PYTHON_OFFLINE_FEASIBILITY_PLAN.md`](PYTHON_OFFLINE_FEASIBILITY_PLAN.md) | Batch 03, O-04 | #8 | Merged |
| 11 | [`ANDROID_TOOLCHAIN_DECISION_SHEET.md`](ANDROID_TOOLCHAIN_DECISION_SHEET.md) | Batch 04, O-01 | #9 | Merged |
| 12 | [`ASSESSMENT_STATE_MACHINE_SPEC.md`](ASSESSMENT_STATE_MACHINE_SPEC.md) | Batch 05 | #10 | Merged |
| 13 | [`ENCRYPTED_BACKUP_RESTORE_SPEC.md`](ENCRYPTED_BACKUP_RESTORE_SPEC.md) | Batch 06, O-06/O-07 | #11 | Merged |
| 14 | [`JAPAN_CALENDAR_HOLIDAY_SPEC.md`](JAPAN_CALENDAR_HOLIDAY_SPEC.md) | Batch 07, O-05 | #12 | Merged |
| 15 | [`UI_ACCESSIBILITY_VISUAL_SPEC.md`](UI_ACCESSIBILITY_VISUAL_SPEC.md) | Batch 08 | #13 | Merged |
| 16 | [`CURRICULUM_OFFLINE_LAB_SPEC.md`](CURRICULUM_OFFLINE_LAB_SPEC.md) | Batch 09 | #14 | Merged |
| 17 | Dokumen ini | Batch 10 | #15 | Merged oleh owner 2026-11-23 (`9804a05`) |

Isi repositori saat audit: hanya dokumentasi, template GitHub, dan skill.
Tidak ada kode aplikasi, proyek Gradle, workflow CI, atau APK.

## 2. Audit konsistensi

Pemeriksaan otomatis yang dijalankan (2026-11-23):

| Pemeriksaan | Hasil |
|---|---|
| Tautan Markdown relatif di semua `.md` | PASS — tidak ada tautan rusak |
| Rujukan nama file dalam backtick | 1 temuan: `docs/PLANNING_COMPLETION_BATCH.md` (file ada di root) |
| Daftar ID keputusan per keluarga | O-01–O-17, OP-1–OP-12, OD-1–OD-10, CO-1–CO-7, UO-1–UO-10, CU-1–CU-11 lengkap tanpa celah |

Temuan:

| ID | Temuan | Jenis | Dampak | Rekomendasi |
|---|---|---|---|---|
| KS-01 | `TECHNICAL_DECISIONS_BATCH_02.md` dan `DECISIONS_LOG.md` menyebut `docs/PLANNING_COMPLETION_BATCH.md`; file sebenarnya di root. | Path | Rendah | Owner memutuskan memindahkan file atau menerima path saat ini (B-4). Batch 02 tidak diubah tanpa izin. |
| KS-02 | DataStore disebut "existing blueprint baseline" (TD:26) tetapi tidak ada di blueprint. | Konflik sumber | Sedang | Konfirmasi owner (B-7). |
| KS-03 | Nama tab B01 ("Learning Journey, IT Lab, Schedule/Calendar") ≠ blueprint ("Learn, Lab, Calendar"). | Istilah | Rendah | Blueprint berlaku (DECISIONS_LOG K-3). |
| KS-04 | Blueprint: *bright/light theme*; dark mode belum diputuskan. | Potensi konflik | Sedang | UO-2. |
| KS-05 | Restore: pelestarian riwayat (BL:63–64) vs tanpa merge otomatis (B01 M-16). | Konflik aturan | Tinggi | OD-3. |
| KS-06 | Banyak aturan bersumber dari Batch 01 yang header-nya masih DRAFT. Dokumen Batch 05–09 menandainya RECOVERED/PROPOSED. | Status sumber | Tinggi | Konfirmasi B-3. |
| KS-07 | ID lokal dipakai ulang antardokumen: `A-xx` (Assessment & UI), `B-0x` (kasus batas Assessment vs blocker HANDOFF `B-x`), `F-xx` (Python plan & Backup), `G-xx`, `K-xx`, `P-xx`, `R-xx`, `S-xx`, `AC-xx`, serta `M-1…M-3` (mode restore) vs `M-01…M-19` (gap). | Duplikasi istilah | Sedang (salah rujuk) | Saat merujuk lintas dokumen, sertakan nama dokumen (mis. "Backup M-1", "Assessment B-03"). Penamaan ulang opsional dan butuh persetujuan. |
| KS-08 | `QUALITY_GATES.md` GR-10 masih menyatakan pembulatan OPEN, padahal TD:21 menyetujui "bulatkan hanya untuk tampilan". | Dokumen lebih lama | Rendah | Bukan konflik: TD:21 lebih baru. Agregasi/representasi tetap OPEN. Perbarui QG hanya bila owner meminta. |
| KS-09 | `PLANNING_HISTORY.md` menandai O-03, O-05, O-12–O-15, O-17 OPEN; Batch 02 menyetujui arahnya. | Snapshot historis | Rendah | Sesuai TD:69, dokumen historis tidak ditulis ulang; status terkini di DECISIONS_LOG. |
| KS-10 | Skill `android-dev` memakai default (Hilt, Retrofit, Coil, Navigation 3) yang bertentangan dengan Batch 02 (DI manual, Navigation Compose, tanpa jaringan). | Panduan vs keputusan | Sedang | Batch 02 berlaku; catat saat skill dipakai. |

## 3. Register keputusan OPEN

### 3.1 O-01–O-17 (status per Batch 02 + dokumen batch)

| ID | Topik | Status | Dokumen |
|---|---|---|---|
| O-01 | Toolchain | OPEN — kombinasi PROPOSED | Toolchain sheet |
| O-02 | `INTERNET` / video opsional | OPEN | CAL:U-3, CUR |
| O-03 | Presisi skor | Arah APPROVED; agregasi/representasi OPEN | Assessment OP-1–OP-3 |
| O-04 | Python offline | OPEN — rencana uji | Python plan |
| O-05 | Hari libur Jepang | Arah APPROVED; sumber/rentang/pembaruan OPEN | Calendar CO-1–CO-3 |
| O-06 | Enkripsi backup | OPEN | Backup OD-1 |
| O-07 | Backup OS Android | OPEN | Backup OD-4 |
| O-08 | R8/minify | OPEN | — |
| O-09 | Runner emulator/perangkat | OPEN | Environment |
| O-10 | Signing/distribusi | OPEN | — |
| O-11 | SDK di cloud | OPEN (opsional) | Environment |
| O-12 | DI | APPROVED (manual) | TD:17 |
| O-13 | Navigasi | APPROVED (Navigation Compose) | TD:18 |
| O-14 | Struktur Gradle | APPROVED (satu modul) | TD:19 |
| O-15 | UI state | APPROVED; mekanisme effect OPEN | TD:20 |
| O-16 | Library test | OPEN | UI UO-8 |
| O-17 | XP farming | Arah APPROVED; identitas OPEN | ASM:X-07, CU-4 |

### 3.2 Keluarga OPEN per dokumen

| Keluarga | Jumlah | Dokumen |
|---|---|---|
| OP-1–OP-12 | 12 | Assessment |
| OD-1–OD-10 | 10 | Backup |
| CO-1–CO-7 | 7 | Calendar |
| UO-1–UO-10 | 10 | UI |
| CU-1–CU-11 | 11 | Curriculum |
| M-01–M-19 | 19 gap, tidak ada yang tertutup | Curriculum §9 |
| Blocker HANDOFF | B-1, B-3–B-14 | HANDOFF_STATE |

## 4. Ketergantungan teknis utama

```
B-3 (status Batch 01) ──► palet, guardrail, garis besar 16 minggu, aturan tenggat, lab tanpa batas waktu
minSdk (B-9) ◄── O-04 (Chaquopy ≥ 24) ◄── OD-1 (PBKDF2-SHA256 platform API 26+) ◄── M-19
O-01 toolchain ──► Navigation 2.10 butuh compileSdk 37 + AGP ≥ 9.2 ──► ketersediaan API 37 di runner (V)
O-04 runtime ──► lab minggu 9–12 (+ capstone) ──► CU-8 alternatif bila gagal
OP-1 agregasi ──► CU-2 penempatan ujian/mini-project ──► model data penilaian
OD-3 mode restore ──► model data attempt (ID stabil) ──► ASM:P-07–P-10
O-02 INTERNET ──► video opsional, CAL:U-3, PY:F-09
```

## 5. Kategori blocker

### 5.1 Wajib selesai sebelum implementasi tahap pertama

| ID | Butir | Alasan |
|---|---|---|
| RB-1 | Izin implementasi eksplisit (B-1) | `CLAUDE.md` |
| RB-2 | Status Batch 01 (B-3) | Banyak aturan bergantung padanya (KS-06) |
| RB-3 | Persetujuan kombinasi toolchain (O-01) dan minSdk (B-9) | Kerangka proyek tidak bisa dibuat tanpa ini |
| RB-4 | DataStore (B-7) | Menentukan dependensi baseline |
| RB-5 | Kebijakan `allowBackup`/aturan ekstraksi (O-07/OD-4) | Harus ada sebelum build pertama yang menyimpan data pengguna |
| RB-6 | Izin `INTERNET` (O-02) | Manifest awal dan prinsip offline |
| RB-7 | Stack test minimal (O-16) | Gate EV dan test-first |

### 5.2 Memerlukan prototipe/uji kelayakan dengan izin owner

| ID | Butir | Bukti yang dibutuhkan |
|---|---|---|
| PF-1 | Runtime Python offline + isolasi (O-04) | PY:F-01–F-15 |
| PF-2 | Kombinasi toolchain di GitHub Actions (O-01) | Checklist toolchain §7 |
| PF-3 | KDF/AEAD di perangkat target (OD-1) | Waktu/memori KDF, uji vektor, uji restore |
| PF-4 | Lab HTML/CSS (render/WebView) dan simulasi Git (CU-7) | Uji perilaku offline |
| PF-5 | Verifikasi dataset hari libur dari `syukujitsu.csv` (CO-3) | Butuh akses `www8.cao.go.jp` (bukan prototipe kode) |

### 5.3 Dapat ditunda sampai milestone terkait

| Milestone | Butir |
|---|---|
| Model data penilaian | OP-1–OP-3, OP-10, OD-3, CU-4, OP-8 |
| UI pertama | UO-1–UO-6, UO-9, CO-5 |
| Lab Python | O-04 (setelah PF-1), CU-6, CU-8 |
| Backup | OD-1, OD-2, OD-5–OD-10 |
| Kalender | CO-1, CO-2, CO-4, CO-6 |
| Konten | CU-1–CU-3, CU-5, CU-9–CU-11, M-02, M-06, M-09 |
| Rilis | O-08, O-10, AP-* |

## 6. Matriks prioritas

Skor: Risiko × Dampak (1–3), ditambah jumlah butir yang bergantung.

| Prioritas | Butir | Risiko | Dampak | Bergantung | Catatan |
|---|---|---|---|---|---|
| P1 | B-3 status Batch 01 | 3 | 3 | Sangat banyak | Murah diputuskan, dampak luas |
| P1 | O-04 kelayakan Python | 3 | 3 | Lab minggu 9–12, minSdk | Risiko teknis terbesar |
| P1 | O-01 + minSdk | 2 | 3 | Semua build | Prasyarat kerangka |
| P2 | OD-3 mode restore | 2 | 3 | Model data attempt | Konflik aturan (KS-05) |
| P2 | OP-1/OP-2 agregasi & basis lulus | 2 | 3 | Model data penilaian, CU-2 | |
| P2 | O-07/OD-4 Auto Backup | 3 | 2 | Manifest | Default aktif |
| P2 | UO-1 kontras palet | 2 | 2 | Semua layar | Hasil hitung sudah ada |
| P3 | B-7 DataStore, O-02, O-16 | 1–2 | 2 | Baseline | |
| P3 | CO-1–CO-3 dataset kalender | 2 | 2 | Tab Calendar | |
| P4 | UO-2, UO-4–UO-10, CU konten | 1–2 | 1–2 | Milestone UI/konten | |

## 7. Alternatif dan rekomendasi untuk owner (bukan keputusan)

| Keputusan | Alternatif | Rekomendasi (saran) | Alasan |
|---|---|---|---|
| B-3 | (a) Setujui Batch 01 apa adanya; (b) setujui dengan revisi; (c) tolak sebagian | (b) bila ada butir yang perlu diperbaiki, selain itu (a) | Membuka banyak butir RECOVERED |
| minSdk | 24 / 26 / lebih tinggi | **26** dipertimbangkan | Menyediakan `PBKDF2withHmacSHA256` platform (Backup §4.1) dan memenuhi Chaquopy (≥ 24); dampak ke jangkauan perangkat perlu dicek terhadap M-19 |
| O-04 | Izinkan prototipe kelayakan terbatas PY:F-01–F-15 | Izinkan, dengan batas uji ditetapkan dulu | Tanpa bukti, minggu 9–12 tidak bisa direncanakan |
| OD-3 | BKP:M-1 ganti + snapshot / BKP:M-2 tolak / BKP:M-3 gabung ID | BKP:M-2 sebagai default aman, BKP:M-1 sebagai opsi eksplisit | Tidak ada riwayat hilang tanpa merge otomatis |
| OD-4 | BKP:AB-1 / BKP:AB-2 / BKP:AB-3 | BKP:AB-1 atau BKP:AB-2, diputuskan bersama OD-3 | Menghindari salinan cloud tak terkendali |
| UO-1 | KC-1 / KC-2 / KC-3 | KC-1 (teks gelap) + KC-2 bila perlu teks putih | Semua warna palet ≥ 4,5:1 dengan hitam |
| UO-2 | Tetap terang / tambah tema gelap | Tetap terang untuk V1 kecuali owner menambah keputusan | Sesuai BL:12 |
| B-7 | DataStore masuk baseline / tidak | Konfirmasi eksplisit | Hindari dependensi tanpa dasar |
| O-02 | Tanpa `INTERNET` (video dibuka aplikasi eksternal) / dengan | Tanpa `INTERNET` di V1 | Prinsip offline + isolasi lab (PY:F-09) |

## 8. Checklist kesiapan implementasi

| # | Butir | Status | Bukti |
|---|---|---|---|
| C-1 | Blueprint terkunci tersedia | PASS | `BLUEPRINT_LOCKED.md` |
| C-2 | Aturan kerja + NO AUTO-MERGE tersimpan | PASS | `CLAUDE.md`, `GITHUB_BRIDGE.md` §5 (Batch 10) |
| C-3 | Quality gates dan aturan bukti EV | PASS | `QUALITY_GATES.md` |
| C-4 | Spesifikasi batch §4 Batch 02 lengkap (langkah 1–5) | PASS | Dokumen 10–15 di §1 |
| C-5 | Izin implementasi | BLOCKED | B-1 |
| C-6 | Status Batch 01 | BLOCKED | B-3 |
| C-7 | Toolchain disetujui | BLOCKED | O-01 PROPOSED |
| C-8 | Toolchain terbukti di CI | NOT RUN | Belum ada proyek |
| C-9 | minSdk diputuskan | BLOCKED | B-9 |
| C-10 | Runtime Python terbukti | NOT RUN | PY:F-01–F-15 belum dijalankan |
| C-11 | Keamanan backup terbukti | NOT RUN | Belum ada implementasi |
| C-12 | UI/aksesibilitas teruji | NOT RUN | Belum ada UI |
| C-13 | Dataset hari libur terverifikasi | FAIL | Sumber resmi tidak dapat diakses (B-12) |
| C-14 | Konten pelajaran tersedia | FAIL | Belum ditulis (M-02) |
| C-15 | Android SDK di cloud | FAIL (tidak menghalangi) | B-6; build direncanakan di GitHub Actions |
| C-16 | Tidak ada secret di repo | PASS | Repo hanya berisi dokumentasi dan skill |

Kesimpulan: **belum siap implementasi.** Dokumentasi persiapan lengkap,
tetapi C-5, C-6, C-7, dan C-9 BLOCKED oleh keputusan owner.

## 9. Pekerjaan yang belum selesai

| Jenis | Pekerjaan |
|---|---|
| Konten | Naskah 16 modul, diagram, glosarium, bank soal + varian, test case lab, tugas penjelasan konsep + rubrik, spesifikasi capstone |
| Dokumentasi | Keputusan untuk butir OPEN; aturan unlock rinci; rumus durasi ujian; rumus XP; field layar; kebijakan notifikasi |
| Data | Dataset hari libur terverifikasi dari sumber resmi |
| Pengujian | Prototipe PY:F-01–F-15; build CI pertama; uji KDF; semua gate EV/GR/OF/LB/CL/SC/AP setelah implementasi |

## 10. Rencana evaluasi delapan skill tambahan

Daftar delapan skill yang dimaksud owner **belum ada di repositori**
(PENDING SOURCE). Kandidat yang dirujuk skill `android-dev` tetapi belum
terpasang (dari audit skill sebelumnya), hanya sebagai bahan pertimbangan:
`android-ux`, `kotlin-flows`, `datastore`, `android-debugging`,
`android-source-search`, `android-gradle-logic`,
`gradle-build-performance`, `modularization`. Daftar final ditentukan owner.

Prosedur evaluasi per skill (PROPOSED, sama dengan PR #1):

| Tahap | Pemeriksaan | Lulus bila |
|---|---|---|
| SE-1 Asal-usul | Repo sumber, commit, lisensi | Sumber jelas, lisensi kompatibel |
| SE-2 Isi | Hanya Markdown; tanpa script, binary, symlink, karakter Unicode tersembunyi | Bersih |
| SE-3 Relevansi | Cocok dengan Android-only, offline, Kotlin/Compose | Ada manfaat untuk milestone dekat |
| SE-4 Konflik | Bandingkan default skill dengan blueprint dan Batch 02 | Konflik dicatat; tidak mengubah keputusan |
| SE-5 Aktivasi | Skill terdeteksi dan dapat dipanggil; referensi terbaca | PASS seperti uji `android-dev`/`compose` |
| SE-6 Pemasangan | Satu PR dokumentasi; `SOURCES.md` diperbarui | Di-review owner, tanpa auto-merge |

## 11. Status akhir

| Item | Status |
|---|---|
| Dokumentasi persiapan | Lengkap untuk urutan Batch 02 §4 |
| Implementasi | **Belum diizinkan** |
| Keputusan owner paling mendesak | B-3, O-04 (izin prototipe + batas uji), O-01 + minSdk, OD-3, O-07 |

## 12. Catatan status terkini (ditambahkan 2026-11-24)

Bagian §1–§11 adalah snapshot Batch 10 dan dipertahankan sebagai catatan
historis. Status terkini ada di
[BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) §18 dan
[PLANNING_ROADMAP.md](PLANNING_ROADMAP.md): keputusan owner D-01–D-35
tercatat; jalur P 31/43; kurikulum diproduksi 4/64 komponen (W1), diterima
0/64. **PLANNING CLEAR: NO; IMPLEMENTATION VERIFIED: NO.**
