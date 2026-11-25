# IT ZERO → HERO — Audit Pekerjaan Belum Selesai Batch 01–10

Status: AUDIT DOKUMENTASI · tidak ada keputusan yang ditutup · tidak ada
izin implementasi. Tanggal: **2026-11-23**. Basis: `main` = `9804a05`
(merge PR #15).

Audit ini dijalankan ulang dari isi repositori, bukan dari ringkasan
[`FINAL_PLANNING_READINESS_REVIEW.md`](FINAL_PLANNING_READINESS_REVIEW.md).
"Dokumen sudah dibuat" **tidak** disamakan dengan "pekerjaan selesai".

## 0. Executive summary

- Semua dokumen Batch 01–10 ada di `main` (PR #5, #7–#15), tetapi **tidak
  satu pun batch** yang tujuannya selesai penuh kecuali Batch 02
  (pencatatan keputusan) dan bagian NO AUTO-MERGE di Batch 10.
- **54** pekerjaan belum selesai: **P0 = 11, P1 = 14, P2 = 16, P3 = 13**
  (§3).
- **PLANNING CLEAR: NO.** 11 keputusan P0 menunggu owner, dua konflik
  perencanaan kritis belum diselesaikan (restore, DataStore), dan sumber
  Batch 01 masih berstatus DRAFT.
- **IMPLEMENTATION VERIFIED: NO.** Belum ada implementasi; tidak ada
  build, runtime, keamanan, UI, atau konten yang teruji.

Pemeriksaan yang dijalankan ulang untuk audit ini:

| Pemeriksaan | Hasil |
|---|---|
| Tautan Markdown relatif di seluruh file `.md` yang dilacak git | 0 rusak |
| Rujukan path dalam backtick | `docs/PLANNING_COMPLETION_BATCH.md` (file ada di root) |
| Status PR #1–#15 di GitHub | Semua merged; PR #15 merged oleh owner 2026-11-23T15:23:13Z |
| Baris status PR di dokumen | 2 baris basi: HANDOFF baris PR Batch 10 dan FINAL REVIEW §1 baris 17 masih "Terbuka" → diperbaiki di PR ini (UW-42) |
| Header Batch 01 | Masih `DRAFT FOR OWNER REVIEW`; 4 kotak kriteria §6 belum dicentang |
| Isi repositori | Hanya dokumentasi, template GitHub, skill; tidak ada kode/Gradle/workflow/APK |

## 1. Status per batch

Catatan: PR #1–#4 dan #6 adalah pekerjaan fondasi sebelum penomoran batch;
dilaporkan di §1.0.

### 1.0 Fondasi (PR #1–#4, #6)

| Item | Status | Selesai | Belum/sebagian | Bukti | Tindakan |
|---|---|---|---|---|---|
| Skill Android (PR #1) | COMPLETE | 5 skill terpasang, uji aktivasi `android-dev`/`compose` PASS | Skill yang dirujuk tetapi tidak terpasang; default skill bertentangan dengan Batch 02 (KS-10) | `.claude/skills/SOURCES.md` | Catat saat skill dipakai |
| ENVIRONMENT (PR #2) | COMPLETE | Audit lingkungan, rencana CI | CI belum dibuat (sengaja) | `ENVIRONMENT.md` §1–4 | — |
| QUALITY_GATES (PR #3) | PARTIAL | Gate EV/AB/OF/GR/LB/CL/SC/AP | 8 gate bertanda OPEN; GR-10 lebih lama dari TD:21 (K-5) | `QUALITY_GATES.md` | UW-48 |
| PLANNING_HISTORY (PR #4) | COMPLETE (snapshot) | Register L/O/M per `260800d` | Sengaja tidak diperbarui (TD:69) | `PLANNING_HISTORY.md` | — |
| GITHUB_BRIDGE (PR #6, #15) | PARTIAL | Peran, template, handoff, NO AUTO-MERGE | §2 menggambarkan alur berbasis Issue, praktik nyata berbasis prompt; daftar "Dokumen terkait" tidak memuat dokumen Batch 03–10; label `documentation` di template Issue belum dicek keberadaannya | `GITHUB_BRIDGE.md` §2, §6 | UW-46, UW-51 |

### 1.1 Tabel status Batch 01–10

| Batch | Tujuan awal | Status | PR |
|---|---|---|---|
| 01 | Memulihkan detail perencanaan M-01–M-19 tanpa mengarang | **PARTIAL / BLOCKED** (persetujuan owner) | #5 |
| 02 | Mencatat keputusan teknis owner-approved | **COMPLETE** (pencatatan); konflik terbuka | #7 |
| 03 | Rencana uji kelayakan Python offline | **PARTIAL** | #8 |
| 04 | Lembar keputusan toolchain kompatibel | **PARTIAL / NOT VERIFIED** | #9 |
| 05 | Kriteria state machine penilaian + persistensi | **PARTIAL** | #10 |
| 06 | Threat model backup + kriteria restore | **PARTIAL** | #11 |
| 07 | Spesifikasi dataset hari libur + kalender | **PARTIAL / BLOCKED** (sumber eksternal) | #12 |
| 08 | Spesifikasi UI, aksesibilitas, visual | **PARTIAL** | #13 |
| 09 | Spesifikasi kurikulum + lab offline | **PARTIAL** (konten NOT STARTED) | #14 |
| 10 | Readiness review + aturan NO AUTO-MERGE | **PARTIAL** (NO AUTO-MERGE COMPLETE) | #15 |

### 1.2 Rincian per batch

#### Batch 01 — Planning Completion (`PLANNING_COMPLETION_BATCH.md`, PR #5)

| Aspek | Isi |
|---|---|
| Tujuan | Memindahkan detail perencanaan yang disepakati ke satu dokumen untuk direview owner |
| Selesai | Matriks M-01–M-19, invariant produk, register O-01–O-17, urutan risiko |
| Belum selesai | Persetujuan owner (§6: 4 kotak belum dicentang); header masih DRAFT |
| Sebagian | 18 dari 19 butir M berstatus PARTIAL; M-09 OPEN |
| OPEN | O-01–O-17 (sebagian kemudian diputuskan arah oleh Batch 02) |
| Konflik/kesalahan | File di root, dirujuk sebagai `docs/…` (KS-01); M-16 "no automatic merging" vs BL:63–64 (KS-05); nama tab berbeda dari blueprint (KS-03) |
| Bukti | `PLANNING_COMPLETION_BATCH.md` baris 3, §2, §6 |
| Tindakan | Owner: setujui/revisi (UW-01); putuskan lokasi file (UW-43) |

#### Batch 02 — Technical Decisions (`TECHNICAL_DECISIONS_BATCH_02.md`, PR #7)

| Aspek | Isi |
|---|---|
| Tujuan | Menyimpan keputusan teknis yang disetujui owner tanpa perubahan |
| Selesai | File disalin verbatim (SHA-256 cocok); DECISIONS_LOG mencatat 10 arah APPROVED dan 10 OPEN |
| Belum selesai | — (untuk tujuan pencatatan) |
| OPEN | O-01, O-02, O-04, O-06–O-11, O-16; detail di dalam O-03, O-05, O-15, O-17 |
| Konflik/kesalahan | TD:26 menyebut DataStore sebagai baseline blueprint (KS-02); TD:5/TD:68 path `docs/PLANNING_COMPLETION_BATCH.md` (KS-01); TD:25 menyebut palet Batch 01 "approved" padahal Batch 01 masih DRAFT (UW-19) |
| Bukti | TD:5, TD:23–26, TD:68; `DECISIONS_LOG.md` K-1–K-3 |
| Tindakan | Owner: DataStore (UW-05), status palet (UW-19) |

#### Batch 03 — Python Offline Feasibility (PR #8)

| Aspek | Isi |
|---|---|
| Tujuan (TD:60) | Rencana uji: kandidat runtime, kriteria sukses/gagal, batas keamanan, target Android |
| Selesai | Perbandingan 4 kandidat dari sumber resmi; risiko PY:R1–R8; matriks PY:F-01–F-15; 7 kondisi eskalasi |
| Sebagian | Kriteria PASS untuk PY:F-03/F-04/F-11–F-13 belum berangka (batas waktu, memori, ukuran, start); target perangkat belum dipilih |
| Belum | Uji kelayakan (butuh izin) |
| OPEN | O-04; batas uji; mekanisme IPC |
| Konflik/kesalahan | Situs resmi diblokir; sumber dibaca dari repo resmi (transparan, §1) |
| Bukti | `PYTHON_OFFLINE_FEASIBILITY_PLAN.md` §3, §6, §8 |
| Tindakan | Owner: batas uji + izin prototipe (UW-10); Test: PY:F-01–F-15 (UW-12) |

#### Batch 04 — Toolchain Decision Sheet (PR #9)

| Aspek | Isi |
|---|---|
| Tujuan (TD:61) | Lembar kombinasi versi kompatibel dari dokumentasi resmi |
| Selesai | Kombinasi PROPOSED, matriks kompatibilitas, alternatif, checklist CI |
| Sebagian | Beberapa pasangan berlabel V (BOM mapping, Room↔KSP, built-in Kotlin↔KSP/Compose, platform API 37 di runner); DataStore belum punya versi |
| Belum | Persetujuan owner; bukti CI |
| OPEN | O-01, minSdk |
| Konflik/kesalahan | Versi bisa basi; TD:47 meminta pemilihan "immediately before first scaffold" |
| Bukti | `ANDROID_TOOLCHAIN_DECISION_SHEET.md` §2–3, §7 |
| Tindakan | Owner: setujui (UW-03) + minSdk (UW-04); cek ulang versi sebelum scaffold (UW-52); Test: CI (UW-13) |

#### Batch 05 — Assessment State Machine (PR #10)

| Aspek | Isi |
|---|---|
| Tujuan (TD:62) | Kriteria state machine, persistensi, timer/process death, aturan lulus tanpa pembulatan |
| Selesai | Model state, tabel transisi, ASM:P-01–P-10, ASM:D-01–D-08, rumus + kasus batas (dicek aritmetika eksak), ledger XP |
| Sebagian | Banyak aturan berlabel RECOVERED (bergantung Batch 01) |
| OPEN | OP-1–OP-12 |
| Konflik/kesalahan | ID `ASM:B-01…B-10` (kasus batas) mirip nomor blocker `HS:B-n` (KS-07) |
| Bukti | `ASSESSMENT_STATE_MACHINE_SPEC.md` §1–9 |
| Tindakan | Owner: OP-1/OP-2 (UW-11), OP-3 (UW-22), OP-4–OP-11 (UW-26–UW-32) |

#### Batch 06 — Encrypted Backup (PR #11)

| Aspek | Isi |
|---|---|
| Tujuan (TD:63) | Threat model, kriteria restore, tanpa memilih parameter kripto secara asal |
| Selesai | Aset, batas kepercayaan, BKP:T-01–T-13, ketersediaan primitif Android (dibaca dari tabel resmi), alur BKP:R1–R11, BKP:F-01–F-12, BKP:G-01–G-12 |
| Sebagian | RFC/NIST tidak terbaca; parameter OWASP berlaku untuk *password storage*, penerapan ke KDF backup adalah inferensi |
| OPEN | OD-1–OD-10 (O-06, O-07) |
| Konflik/kesalahan | Mode restore vs BL:63–64 (KS-05); minSdk 24 vs PBKDF2-SHA256 API 26+ |
| Bukti | `ENCRYPTED_BACKUP_RESTORE_SPEC.md` §1, §4, §6.2, §11 |
| Tindakan | Owner: OD-3 (UW-09), OD-4 (UW-06), OD-2 (UW-16), OD-1 (UW-15) |

#### Batch 07 — Japan Calendar (PR #12)

| Aspek | Isi |
|---|---|
| Tujuan (TD:64) | Spesifikasi dataset hari libur + kriteria kalender |
| Selesai | Lapisan L1/L2, format dataset, validasi CAL:V-01–V-06, aturan JST/jam tenang, AC/skenario |
| Belum | Dataset dari sumber resmi; tidak ada tanggal VERIFIED |
| OPEN | CO-1–CO-7 |
| Konflik/kesalahan | Contoh tanggal dari cuplikan pencarian (ditandai wajib verifikasi) |
| Bukti | `JAPAN_CALENDAR_HOLIDAY_SPEC.md` §2–3, §9 |
| Tindakan | Verifikasi eksternal `syukujitsu.csv` (UW-14); owner CO-1/CO-2 (UW-23) |

#### Batch 08 — UI & Accessibility (PR #13)

| Aspek | Isi |
|---|---|
| Tujuan (TD:64) | Kriteria aksesibilitas dan screenshot UI |
| Selesai | Ambang resmi Android (48dp, 4,5:1/3:1), hitung kontras palet, navigasi, UI state, rencana screenshot |
| Belum | Desain token, tipografi, aset; screenshot (butuh implementasi) |
| OPEN | UO-1–UO-10 |
| Konflik/kesalahan | Palet ditandai PROPOSED padahal TD:25 menyebut "approved palette" (UW-19); dark mode vs BL:12 (UW-18) |
| Bukti | `UI_ACCESSIBILITY_VISUAL_SPEC.md` §1–2, §11 |
| Tindakan | Owner: UO-1 (UW-17), UO-2 (UW-18), status palet (UW-19) |

#### Batch 09 — Curriculum & Offline Lab (PR #14)

| Aspek | Isi |
|---|---|
| Tujuan | Audit cakupan, matriks mingguan, format konten, lab objektif, remedial, gap M |
| Selesai | 128 jam konsisten; peta domain; ketergantungan O-04 per minggu; ID stabil; CC-01–CC-11; audit M |
| Belum | Naskah, bank soal, test case, rubrik (**NOT STARTED**) |
| OPEN | CU-1–CU-11 |
| Konflik/kesalahan | Tujuan per minggu hanya kerangka; tumpang-tindih minggu 9/10 |
| Bukti | `CURRICULUM_OFFLINE_LAB_SPEC.md` §2, §6, §9–10 |
| Tindakan | Owner: CU-1 (UW-20); konten (UW-37) |

#### Batch 10 — Readiness Review + NO AUTO-MERGE (PR #15)

| Aspek | Isi |
|---|---|
| Tujuan | Audit kesiapan + aturan merge permanen |
| Selesai | NO AUTO-MERGE di `GITHUB_BRIDGE.md` §5 dan `CLAUDE.md` (**COMPLETE**); KS-01–KS-10; kategori blocker; checklist |
| Sebagian | Daftar delapan skill tambahan PENDING SOURCE |
| Konflik/kesalahan | Baris status PR Batch 10 basi di HANDOFF dan FINAL REVIEW §1 (UW-42, diperbaiki di PR ini); checklist FIN:C-4 "PASS" hanya berarti dokumen ada, bukan pekerjaan selesai |
| Bukti | `FINAL_PLANNING_READINESS_REVIEW.md` §1, §8, §10 |
| Tindakan | Owner: daftar skill (UW-41) |

## 2. Audit keputusan

### 2.1 Ringkasan status

| Kategori | Butir |
|---|---|
| **Disetujui (APPROVED)** | Semua butir blueprint; Batch 02: O-12 (DI manual), O-13 (Navigation Compose), O-14 (satu modul), O-15 (StateFlow; detail effect OPEN), arah O-03 (bulat hanya tampilan), arah O-05 (dataset offline + pembaruan terkontrol), arah O-17 (XP sekali per identitas), CI di GitHub Actions, UI Colorful Academy lima tab; NO AUTO-MERGE |
| **Diusulkan (PROPOSED, belum disetujui)** | Kombinasi toolchain; minSdk 24; seluruh tabel transisi/persistensi Batch 05; envelope/restore Batch 06; format dataset Batch 07; peran palet/navigasi/komponen Batch 08; format konten/ID/remedial Batch 09; rekomendasi FINAL REVIEW §7 |
| **Menunggu owner** | B-3, B-7, O-01, minSdk, O-02, O-07/OD-4, O-16, OD-3, OP-1/OP-2, batas uji O-04, OD-2, UO-1, UO-2, palet vs TD:25, CU-1, CU-10, daftar skill |
| **Butuh bukti teknis** | O-04 (PY:F-01–F-15), O-01 (build CI), OD-1 (ukur KDF), CU-7 (WebView/HTML), dataset hari libur (CO-3) |
| **Tidak boleh sebelum izin implementasi** | Scaffold proyek, workflow CI, prototipe runtime/kripto, screenshot, APK |

### 2.2 Per keluarga ID

| Keluarga | Total | APPROVED (arah) | Masih OPEN | Catatan |
|---|---|---|---|---|
| O-01–O-17 | 17 | 7 (O-03, O-05, O-12–O-15, O-17; detail sebagian OPEN) | 10 | DECISIONS_LOG |
| OP-1–OP-12 | 12 | 0 | 12 | OP-12 = duplikat B-3 |
| OD-1–OD-10 | 10 | 0 | 10 | OD-10 = duplikat minSdk |
| CO-1–CO-7 | 7 | 0 | 7 | CO-7 = duplikat B-3 |
| UO-1–UO-10 | 10 | 0 | 10 | UO-10 = duplikat B-3 |
| CU-1–CU-11 | 11 | 0 | 11 | CU-4 tumpang-tindih OP-8/O-17 |
| M-01–M-19 | 19 | 0 tertutup | 19 (18 PARTIAL, M-09 OPEN) | Batch 03–09 hanya menambah kriteria |
| Blocker HANDOFF | 13 aktif (B-1, B-3–B-14) | — | 13 | B-2 selesai (PR #7) |

## 3. Master unfinished work register

Kolom "Oleh": **O** = Owner, **C** = Claude (dokumentasi), **T** = butuh
pengujian/verifikasi teknis. Duplikasi lintas batch digabung; referensi
asli dipertahankan.

### P0 — wajib sebelum PLANNING CLEAR / implementasi tahap pertama

| ID | Batch | Pekerjaan | Status | Penyebab | Ketergantungan | Oleh | Langkah | Acceptance criteria | Referensi |
|---|---|---|---|---|---|---|---|---|---|
| UW-01 | 01 | Status persetujuan Batch 01 | BLOCKED | Header DRAFT; §6 belum dicentang | — | O | Owner menyetujui/merevisi | Header/keputusan tertulis di repo | B-3, OP-12, CO-7, UO-10 |
| UW-02 | — | Izin implementasi | BLOCKED | Tahap persiapan | UW-01–UW-11 | O | Owner memberi izin eksplisit | Instruksi tertulis owner | B-1, CLAUDE.md |
| UW-03 | 04 | Persetujuan kombinasi toolchain | BLOCKED | Menunggu owner | UW-04 | O | Review sheet | Kombinasi APPROVED di DECISIONS_LOG | O-01, AB-3 |
| UW-04 | 04/06/03 | minSdk final | BLOCKED | Saling terkait | M-19, O-04, OD-1 | O | Pilih 24/26/lainnya | Nilai tercatat | B-9, OD-10 |
| UW-05 | 02 | DataStore di baseline | BLOCKED | TD:26 vs BL:11 | — | O | Konfirmasi | Keputusan tertulis | B-7, K-1, KS-02 |
| UW-06 | 06 | Kebijakan Auto Backup | BLOCKED | Default aktif | UW-09 | O | Pilih BKP:AB-1/2/3 | Keputusan tertulis | O-07, OD-4 |
| UW-07 | 02/07 | Izin `INTERNET` | BLOCKED | Video opsional, isolasi lab | — | O | Putuskan | Keputusan tertulis | O-02, OF-3 |
| UW-08 | 04/08 | Stack test minimal | BLOCKED | Belum dipilih | UW-03 | O (C dapat menyiapkan opsi) | Pilih alat unit/UI/screenshot | Keputusan tertulis | O-16, UO-8 |
| UW-09 | 06 | Mode restore | BLOCKED | Konflik BL:63–64 vs B01 M-16 | UW-01 | O | Pilih BKP:M-1/M-2/M-3 | Keputusan tertulis | OD-3, KS-05 |
| UW-10 | 03 | Batas uji + izin prototipe O-04 | BLOCKED | Angka belum ada | — | O | Tetapkan batas, beri/tolak izin | Batas tertulis; izin eksplisit | O-04, PY:F-03/F-04/F-11–F-13 |
| UW-11 | 05 | Agregasi skor + basis lulus | BLOCKED | Tidak boleh ditebak (TD:32) | UW-01 | O | Putuskan | Aturan tertulis | OP-1, OP-2, CU-2 |

### P1 — tinggi; sebelum milestone terkait / risiko besar

| ID | Batch | Pekerjaan | Status | Penyebab | Ketergantungan | Oleh | Langkah | Acceptance criteria | Referensi |
|---|---|---|---|---|---|---|---|---|---|
| UW-12 | 03 | Uji kelayakan Python PY:F-01–F-15 | NOT STARTED | Butuh izin | UW-10 | T | Prototipe terbatas | PY:F-01–F-15 PASS dengan bukti EV | O-04 |
| UW-13 | 04 | Bukti toolchain di GitHub Actions | NOT VERIFIED | Belum ada proyek | UW-02, UW-03 | T | Build CI pertama | Checklist toolchain §7 PASS | AB-5 |
| UW-14 | 07 | Verifikasi dataset hari libur resmi | BLOCKED | `www8.cao.go.jp` diblokir | Akses jaringan/owner | T (eksternal) | Unduh `syukujitsu.csv`, cocokkan | CAL:AC-02 PASS | CO-3, HS:B-12, FIN:C-13 |
| UW-15 | 06 | Pilih KDF/AEAD + ukur di perangkat | BLOCKED | Butuh pengukuran | UW-04 | O + T | Ukur kandidat BKP:C-1–C-4 | Parameter tertulis + bukti | OD-1, O-06 |
| UW-16 | 06 | Penerimaan risiko pemalsuan nilai oleh pemilik kata sandi | BLOCKED | Tidak dapat dimitigasi kripto offline | — | O | Terima/ubah kebijakan | Keputusan tertulis | OD-2, BKP:T-03 |
| UW-17 | 08 | Solusi kontras palet | BLOCKED | Semua warna < 4,5:1 dengan putih | UW-19 | O | Pilih KC-1/2/3 | Token memenuhi U1 | UO-1 |
| UW-18 | 08 | Dark mode | BLOCKED | BL:12 terang | — | O | Putuskan | Keputusan tertulis | UO-2, KS-04 |
| UW-19 | 02/08 | Status palet & guardrail (TD:25 "approved" vs B01 DRAFT) | BLOCKED | Dua sumber berbeda | UW-01 | O → C | Owner konfirmasi; Claude menyelaraskan label | Label konsisten di semua dokumen | TD:25, UI-07, UI-09 |
| UW-20 | 09 | Persetujuan garis besar 16 minggu | BLOCKED | Hanya RECOVERED | UW-01 | O | Setujui/revisi | Keputusan tertulis | CU-1, M-02 |
| UW-21 | 09 | Alternatif minggu 9–12 bila O-04 gagal | BLOCKED (kondisional) | Bergantung UW-12 | UW-12 | O | Putuskan bila perlu | Keputusan tertulis | CU-8 |
| UW-22 | 05 | Representasi angka/presisi/seri | BLOCKED | TD:21 menyisakan detail | UW-11 | O (C dapat menyiapkan opsi) | Putuskan | Kasus batas ASM:B-01–B-10 lolos secara eksak | OP-3 |
| UW-23 | 07 | Rentang dan mekanisme pembaruan dataset | BLOCKED | Menunggu owner | UW-07 | O | Pilih | Keputusan tertulis | CO-1, CO-2 |
| UW-24 | — | Runner emulator/perangkat | BLOCKED | Tidak ada KVM di cloud | — | O | Pilih | Runner tersedia | O-09 |
| UW-25 | 09 | Penerimaan risiko kunci jawaban dapat diekstrak | BLOCKED | Konsekuensi offline | — | O | Terima/ubah | Keputusan tertulis | CU-10 |

### P2 — sedang; dapat ditunda sampai milestone terkait

| ID | Batch | Pekerjaan | Status | Oleh | Langkah | Acceptance criteria | Referensi |
|---|---|---|---|---|---|---|---|
| UW-26 | 05/09 | Rubrik + bank tugas penjelasan konsep | NOT STARTED | O + konten | Rancang rubrik objektif | CC-08 | OP-4, M-06 |
| UW-27 | 05 | Rumus durasi ujian, format soal | BLOCKED | O | Putuskan | ASM:D-08 terisi | OP-5, M-07 |
| UW-28 | 05 | Kebijakan manipulasi jam, toleransi NTP | BLOCKED | O | Putuskan | ASM:E-01–E-04 punya kebijakan | OP-6 |
| UW-29 | 05 | Aturan pengumpulan/interupsi lab-proyek | BLOCKED | O | Putuskan | L5 terisi | OP-7, M-08 |
| UW-30 | 05/09 | Identitas XP, rumus, level, streak, revisi konten | BLOCKED | O | Putuskan | ASM:X-07 terisi | OP-8, CU-4, O-17, M-11 |
| UW-31 | 05 | Aturan unlock rinci | BLOCKED | O | Putuskan | C6 terisi | OP-9, M-04 |
| UW-32 | 05 | Komponen yang boleh diulang; debounce autosave | BLOCKED | O | Putuskan | OP-10, OP-11 terisi | OP-10, OP-11 |
| UW-33 | 06 | Detail backup: format payload, aturan kata sandi, batas ukuran, retensi snapshot, attempt berjalan | BLOCKED | O | Putuskan | OD-5–OD-9 terisi | OD-5–OD-9, M-15, M-16 |
| UW-34 | 07 | Kalender perusahaan, label era, perilaku notifikasi jam tenang | BLOCKED | O | Putuskan | CO-4–CO-6 terisi | M-12–M-14 |
| UW-35 | 08 | Tipografi, aset, breakpoint, tab bar, performa, field layar | BLOCKED | O | Putuskan | UO-3–UO-9 terisi | M-17–M-19 |
| UW-36 | 09 | Penempatan ujian/proyek, format konten, varian, batas lab, bentuk lab SQL/HTML/Git, capstone, minggu 9/10 | BLOCKED | O | Putuskan | CU-2, CU-3, CU-5–CU-7, CU-9, CU-11 terisi | M-09, M-10 |
| UW-37 | 09 | Menulis konten 16 modul (naskah, diagram, glosarium, bank soal, test case) | NOT STARTED | O + konten (C dapat menyusun draf setelah UW-20) | Tulis per modul | CC-01–CC-11 | M-02, M-03 |
| UW-38 | — | R8/minify, signing, distribusi | BLOCKED | O | Putuskan saat rilis | AP-3–AP-5 | O-08, O-10 |
| UW-39 | — | Android SDK di cloud (opsional) | BLOCKED | O | Opsional | — | O-11, B-6 |
| UW-40 | 02 | Detail mekanisme effect UI | BLOCKED | Implementasi | Putuskan saat UI | — | O-15 |
| UW-41 | 10 | Daftar delapan skill tambahan | BLOCKED (PENDING SOURCE) | O | Owner menyerahkan daftar | Prosedur SE-1–SE-6 | FINAL REVIEW §10 |

### P3 — rendah; perapian dokumentasi

| ID | Batch | Pekerjaan | Status | Oleh | Langkah | Acceptance criteria | Referensi |
|---|---|---|---|---|---|---|---|
| UW-42 | 10 | Baris status PR Batch 10 basi | **Diperbaiki di PR ini** | C | Perbarui HANDOFF dan FINAL REVIEW §1 | Status = merged | HANDOFF, FINAL REVIEW §1 |
| UW-43 | 01/02 | Path `docs/PLANNING_COMPLETION_BATCH.md` | BLOCKED | O | Pindahkan file atau terima | Rujukan valid | B-4, KS-01 |
| UW-44 | 05–09 | ID lokal dipakai ulang | NOT STARTED | C (setelah persetujuan) | Prefiks per dokumen atau aturan rujukan | Tidak ada ID ambigu | KS-07, K-4 |
| UW-45 | 05–09 | Label sumber Batch 01 tidak seragam (RECOVERED vs PROPOSED) | NOT STARTED | C (setelah UW-01) | Seragamkan | Satu label per sumber | AUD:D-05 |
| UW-46 | fondasi | `GITHUB_BRIDGE.md` §2 (alur Issue) vs praktik; daftar dokumen terkait kurang | NOT STARTED | C | Perbarui | Alur dan daftar sesuai praktik | §1.0 |
| UW-47 | fondasi | DECISIONS_LOG tidak menunjuk dokumen Batch 03–10 | NOT STARTED | C | Tambah tabel rujukan | Semua dokumen batch terdaftar | DECISIONS_LOG |
| UW-48 | fondasi | QUALITY_GATES: GR-10 dan gate OPEN tanpa rujukan ke dokumen batch | NOT STARTED | C (dengan izin) | Tambah rujukan | Setiap gate OPEN menunjuk dokumen terkait | K-5 |
| UW-49 | — | Urutan/agregasi blocker HANDOFF (HS:B-10 sebelum HS:B-9; HS:B-5 menggabung banyak butir) | NOT STARTED | C | Rapikan | Blocker terurut | HANDOFF |
| UW-50 | — | README hanya 2 baris | NOT STARTED | C | Tambah ringkasan + tautan dokumen | README menunjuk dokumen inti | README.md |
| UW-51 | fondasi | Label `documentation` di template Issue belum dicek | NOT VERIFIED | C | Cek label repo | Label ada atau dihapus dari template | `.github/ISSUE_TEMPLATE/` |
| UW-52 | 04 | Kesegaran versi toolchain | NOT STARTED | C | Cek ulang tepat sebelum scaffold | Sumber resmi bertanggal baru | TD:47 |
| UW-53 | 03/06/07/08 | Sumber resmi yang tidak terbaca (RFC, NIST, W3C, M3, CAO, e-Gov) | BLOCKED | O (akses) / T | Buka host atau baca di lingkungan lain | Klaim terkait diverifikasi | B-8 |
| UW-54 | 04 | Butir V toolchain (BOM mapping, KSP 2.3.14, Room↔KSP, API 37 runner) | NOT VERIFIED | T | Bagian dari UW-13 | Log CI | Toolchain §3 |

## 4. Pemeriksaan konsistensi

Catatan ID (UW-44, ditambahkan kemudian): ID `D-01`–`D-10` di tabel ini
adalah pemeriksaan konsistensi audit dan dirujuk sebagai `AUD:D-xx`. Di
bagian lain, `D-01`–`D-11` berarti keputusan owner.

| ID | Jenis | Temuan | Status |
|---|---|---|---|
| D-01 | Referensi file salah | `docs/PLANNING_COMPLETION_BATCH.md` di TD:5, TD:68, DECISIONS_LOG | OPEN (UW-43) |
| D-02 | Tautan rusak | Tidak ditemukan | PASS |
| D-03 | Status PR tidak sinkron | HANDOFF baris PR Batch 10 dan FINAL REVIEW §1 baris 17 "Terbuka" padahal merged | Diperbaiki di PR ini (UW-42) |
| D-04 | Konflik blueprint vs dokumen teknis | DataStore (TD:26 vs BL:11); dark mode vs BL:12 (hanya permintaan, belum keputusan) | OPEN (UW-05, UW-18) |
| D-05 | Keputusan ganda/bertentangan | Palet: TD:25 "approved" vs UI spec "PROPOSED" vs B01 DRAFT; label sumber B01 berbeda antardokumen (RECOVERED/PROPOSED) | OPEN (UW-19, UW-45) |
| D-06 | Konflik aturan | Restore: BL:63–64 vs B01 M-16 | OPEN (UW-09) |
| D-07 | Klaim VERIFIED | Backup: tabel Android + OWASP (dibaca) — memadai. Calendar: hanya `JapaneseCalendar` (dibaca) — memadai; tanggal tidak diklaim VERIFIED. UI: ambang 48dp/4,5:1 (dibaca) — memadai; rasio kontras berlabel "VERIFIED — hasil hitung" memakai rumus luminans WCAG yang sumber W3C-nya tidak terbaca → **sebaiknya dibaca sebagai hasil hitung yang dapat diulang, bukan verifikasi sumber** | Catatan |
| D-08 | DRAFT dianggap final | TD:25 (owner-approved) merujuk palet/guardrail Batch 01 sebagai "approved" padahal Batch 01 DRAFT; dokumen Claude tidak menganggap B01 final | OPEN (UW-01, UW-19) |
| D-09 | Ditandai selesai padahal belum diuji | FIN:C-4 "PASS" berarti dokumen ada, bukan teruji; tidak ditemukan klaim build/test/UI/keamanan PASS | Catatan |
| D-10 | Snapshot historis | PLANNING_HISTORY, QG GR-10 lebih lama dari Batch 02 (disengaja, TD:69) | Diterima |

Tidak ada keputusan terkunci yang diubah oleh audit ini.

## 5. Keputusan owner (urut prioritas)

1. **UW-01** — Status Batch 01 (setujui / revisi / tolak sebagian).
2. **UW-05** — DataStore masuk baseline atau tidak.
3. **UW-09** — Mode restore (BKP:M-1 / M-2 / M-3).
4. **UW-11** — Agregasi skor dan basis lulus (skor terbaik?).
5. **UW-10** — Batas uji O-04 dan izin prototipe kelayakan.
6. **UW-03 + UW-04** — Toolchain dan minSdk.
7. **UW-06, UW-07, UW-08** — Auto Backup, `INTERNET`, stack test.
8. **UW-19, UW-17, UW-18** — Status palet, kontras, dark mode.
9. **UW-20, UW-16, UW-25** — Garis besar kurikulum; penerimaan dua risiko integritas offline.
10. **UW-41** — Daftar delapan skill.

## 6. Risiko kritis

| Risiko | Mengapa kritis | Referensi |
|---|---|---|
| Runtime Python offline tidak layak/terisolasi | Lab minggu 9–12 (BL:19, BL:41) tidak dapat dijalankan | UW-10, UW-12, UW-21 |
| Banyak aturan bersumber dari dokumen DRAFT | Fondasi Batch 05–09 bisa berubah | UW-01 |
| Konflik mode restore | Riwayat percobaan bisa hilang | UW-09 |
| Integritas nilai offline tidak dapat dijamin (backup + kunci jawaban) | Pemalsuan oleh pengguna mahir | UW-16, UW-25 |
| Sumber resmi diblokir | Dataset hari libur dan beberapa klaim belum terverifikasi | UW-14, UW-53 |
| Konten belum ditulis | Tidak ada materi untuk 16 minggu | UW-37 |

## 7. Urutan penyelesaian

| Kelompok | Butir | Catatan |
|---|---|---|
| 1. Claude sekarang, tanpa coding | UW-42 (dikerjakan di PR ini); setelah persetujuan owner: UW-46, UW-47, UW-48, UW-49, UW-50, UW-51, UW-44; menyiapkan lembar opsi untuk UW-08 dan UW-22 | Tidak mengubah keputusan |
| 2. Keputusan owner | UW-01 → UW-05, UW-09, UW-11 → UW-03/UW-04 → UW-06, UW-07, UW-08, UW-10 → UW-16–UW-20, UW-22–UW-25 → P2 | UW-01 lebih dulu karena paling banyak ketergantungan |
| 3. Verifikasi sumber eksternal | UW-14, UW-53 | Butuh akses host atau owner menyediakan file |
| 4. Prototipe/uji teknis (butuh izin) | UW-12, UW-15 (pengukuran), CU-7 bagian WebView | Hanya setelah UW-10 / izin eksplisit |
| 5. Saat implementasi Android | UW-13, UW-54, UW-52, UW-37 (penulisan konten berjalan paralel), UW-38, UW-40, semua gate EV/GR/OF/LB/CL/SC/AP | Bukan syarat menyelesaikan dokumentasi |

## 8. Checklist PLANNING CLEAR

| # | Kriteria | Status | Bukti |
|---|---|---|---|
| PC-1 | Sumber keputusan Batch 01 disetujui | NO | Header DRAFT (UW-01) |
| PC-2 | Konflik kritis selesai: restore, DataStore | NO | UW-09, UW-05 |
| PC-3 | Toolchain + minSdk disetujui | NO | UW-03, UW-04 |
| PC-4 | Kebijakan manifest awal (Auto Backup, `INTERNET`) | NO | UW-06, UW-07 |
| PC-5 | Stack test minimal dipilih | NO | UW-08 |
| PC-6 | Aturan model data penilaian (agregasi, basis lulus) | NO | UW-11 |
| PC-7 | Keputusan O-04 (izin uji + batas) | NO | UW-10 |
| PC-8 | Dokumentasi konsisten (path, status PR, label) | PARTIAL | AUD:D-01, AUD:D-05 OPEN; AUD:D-03 diperbaiki di PR #16 |
| PC-9 | Tidak ada tautan rusak | YES | AUD:D-02 |
| PC-10 | Aturan kerja dan merge tersimpan | YES | `GITHUB_BRIDGE.md` §5, `CLAUDE.md` |

**PLANNING CLEAR: NO** — PC-1 sampai PC-7 belum terpenuhi.

## 9. IMPLEMENTATION VERIFIED

**NO.** Tidak ada implementasi. Hal yang memang harus menunggu
implementasi: build CI dan toolchain (UW-13, UW-54), uji runtime Python
pada build nyata (UW-12), uji KDF/restore (UW-15, BKP:G-01–G-12), screenshot
dan uji aksesibilitas (UI §8–10), uji kalender dengan dataset terverifikasi
(CAL:AC-01–AC-08), uji penilaian (ASM:S-01–S-10), APK dan uji perangkat (AP-1–AP-5).

## 10. Pembaruan status — audit cleanup (2026-11-23)

Basis: `main` = `5931ece` (merge PR #16). Status di tabel §3 di atas
adalah status per audit awal; tabel ini adalah status terbaru.

| ID | Status baru | Bukti |
|---|---|---|
| UW-42 | **COMPLETE** | PR #16 (merged `5931ece`): baris status PR #15 diperbaiki di HANDOFF dan FINAL REVIEW §1 |
| UW-46 | **COMPLETE** | `GITHUB_BRIDGE.md` §2 menggambarkan alur berbasis prompt + STOP + merge berizin; §6 memuat seluruh dokumen inti |
| UW-47 | **COMPLETE** | `DECISIONS_LOG.md` §Dokumen batch: Batch 03–10, audit, checklist |
| UW-48 | **COMPLETE** | `QUALITY_GATES.md` §10: setiap gate OPEN (AB-3, OF-3, GR-10, LB-2, CL-3, SC-1, SC-6, AP-5) menunjuk dokumen terkait; isi gate tidak diubah |
| UW-49 | **COMPLETE** | `HANDOFF_STATE.md` §Blocker dikelompokkan (keputusan owner / izin / verifikasi eksternal), nomor `B-n` dipertahankan, rujukan ke checklist dan register |
| UW-50 | **COMPLETE** | `README.md` menjadi pintu masuk: status, urutan baca, daftar dokumen, aturan PR |
| UW-51 | **COMPLETE** | Label `documentation` ada di repo (GitHub API: warna `0075ca`, "Improvements or additions to documentation"); template tidak perlu diubah |
| UW-44 | **PARTIAL** | `DECISIONS_LOG.md` §Aturan rujukan lintas dokumen (kode dokumen untuk ID lokal). ID lama **tidak** diganti; dokumen lama belum memakai kode itu. Penggantian ID memerlukan persetujuan owner |
| UW-43 | **BLOCKED** | Usulan: (a) pindahkan file ke `docs/` dan perbarui tautan, atau (b) pertahankan di root dan catat di Batch 02 sebagai errata. Keduanya butuh owner karena menyentuh dokumen Batch 02 yang disalin verbatim |
| UW-45 | **BLOCKED** | Penyeragaman label (RECOVERED/PROPOSED/APPROVED) bergantung D-01 di [`OWNER_DECISION_CHECKLIST.md`](OWNER_DECISION_CHECKLIST.md) |

Butir P0 UW-01–UW-11 kini dipetakan ke D-01–D-11 di
[`OWNER_DECISION_CHECKLIST.md`](OWNER_DECISION_CHECKLIST.md); status tetap
BLOCKED (AWAITING OWNER).

### Jumlah per status (54 butir)

| Status | Jumlah | Butir |
|---|---|---|
| COMPLETE dengan bukti | 7 | UW-42, UW-46–UW-51 |
| OPEN (NOT STARTED / PARTIAL, tidak menunggu pihak lain) | 5 | UW-12, UW-26, UW-37 (NOT STARTED); UW-44 (PARTIAL); UW-52 (NOT STARTED) |
| BLOCKED | 40 | UW-01–UW-11, UW-14–UW-25, UW-27–UW-36, UW-38–UW-41, UW-43, UW-45, UW-53 |
| NOT VERIFIED | 2 | UW-13, UW-54 |

Catatan: UW-12 berstatus NOT STARTED, tetapi praktis menunggu D-10.

**PLANNING CLEAR: NO** — PC-1 sampai PC-7 (§8) belum berubah karena tidak
ada keputusan owner baru. PC-8 tetap PARTIAL (UW-43, UW-45).

## 11. Pembaruan status — D-01 (2026-11-23)

Basis: `main` = `4eacaa0` (merge PR #17). Owner menyetujui M-01–M-19
dengan ketentuan; rincian di
[`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) §7 dan
[`OWNER_DECISION_CHECKLIST.md`](OWNER_DECISION_CHECKLIST.md) D-01.

| ID | Status baru | Bukti |
|---|---|---|
| UW-01 | **COMPLETE** — berlaku saat PR pencatatan D-01 di-merge | Keputusan owner 2026-11-23; header Batch 01 dan §7 diperbarui; checklist D-01 terisi |

Dampak yang **belum** diterapkan di sini (perlu tindak lanjut terpisah):
UW-19 (palet dikonfirmasi M-17; label dokumen UI belum diselaraskan),
UW-20 (kerangka 16 minggu disetujui M-02), UW-45 (penyeragaman label kini
tidak lagi menunggu D-01). Statusnya dibiarkan seperti §10 sampai
diperbarui dalam PR berikutnya.

### Jumlah per status (54 butir)

| Status | Jumlah | Perubahan |
|---|---|---|
| COMPLETE dengan bukti | 8 | + UW-01 |
| OPEN | 5 | — |
| BLOCKED | 39 | − UW-01 |
| NOT VERIFIED | 2 | — |

PLANNING CLEAR checklist §8: **PC-1 → YES** (setelah PR ini di-merge).
PC-2 sampai PC-7 tetap NO; PC-8 tetap PARTIAL.

**PLANNING CLEAR: NO** — D-02 sampai D-11 masih AWAITING OWNER.
**IMPLEMENTATION VERIFIED: NO.**

## 12. Pembaruan status — keputusan owner D-02–D-11 (2026-11-23)

Basis: `main` = `777f5dc` (merge PR #18). Sumber keputusan:
[`OWNER_DECISION_CHECKLIST.md`](OWNER_DECISION_CHECKLIST.md). Status di
bawah berlaku saat PR pencatatan D-02–D-11 di-merge. Sebuah butir hanya
menjadi COMPLETE bila acceptance criteria-nya di §3 terpenuhi; persetujuan
arah saja tidak cukup.

| ID | Status baru | Alasan / bukti |
|---|---|---|
| UW-03 | **COMPLETE** (keputusan) | AC "Kombinasi APPROVED di DECISIONS_LOG": D-06 tercatat sebagai baseline sementara. Verifikasi tetap di UW-13, UW-52, UW-54 |
| UW-04 | **COMPLETE** | AC "Nilai tercatat": minSdk 29 (D-05); referensi 24 ditandai SUPERSEDED |
| UW-05 | **COMPLETE** (keputusan) | AC "Keputusan tertulis": D-02. Versi DataStore dilacak di UW-52 |
| UW-06 | **COMPLETE** (keputusan) | AC "Keputusan tertulis": D-07 BKP:AB-1. Verifikasi transfer antarperangkat → UW-55 (baru) |
| UW-07 | **COMPLETE** (keputusan) | AC "Keputusan tertulis": D-08 opsi (b). Isolasi jaringan lab tetap di UW-12 (PY:F-09) |
| UW-08 | **COMPLETE** (keputusan) | AC "Keputusan tertulis": D-09 opsi (b). Verifikasi terhadap toolchain di UW-13 |
| UW-09 | **COMPLETE** (keputusan) | AC "Keputusan tertulis": D-03. Detail OD-8 tetap di UW-33 |
| UW-10 | **BLOCKED** | AC "Batas tertulis; izin eksplisit": batas tertulis (D-10) ✓, izin eksekusi ✗ |
| UW-11 | **BLOCKED** | AC "Aturan tertulis": basis lulus dan kelulusan per modul ✓ (D-04); agregasi numerik program ✗ |
| UW-02 | **BLOCKED** | D-11 DEFERRED |
| UW-19 | **COMPLETE** | AC "Label konsisten": palet APPROVED (D-01 M-17) di UI spec UI-07 dan §11; TD:25 kini konsisten |
| UW-20 | **COMPLETE** | AC "Keputusan tertulis": kerangka 16 minggu disetujui (D-01 M-02, PR #18); dicatat di Curriculum §11 |
| UW-45 | **NOT STARTED** (tidak lagi BLOCKED) | D-01 sudah diputuskan; penyeragaman label lintas dokumen belum dikerjakan |
| UW-36 | **BLOCKED** (diperbarui) | Ditambah: implikasi D-04 bahwa setiap modul memiliki empat komponen (CU-2) perlu konfirmasi owner |
| UW-55 | **NOT VERIFIED** (baru) | Verifikasi perilaku transfer antarperangkat dengan `allowBackup=false`, termasuk pengecualian per produsen (D-07). Oleh: T, setelah izin implementasi. AC: hasil uji per jalur (cloud, D2D) terdokumentasi dengan bukti EV |

UW-52 kini juga mencakup pemilihan dan verifikasi versi DataStore (D-02).
UW-12 tetap NOT STARTED: ambang PY:F-01–F-15 sudah disetujui (D-10), tetapi
eksekusi tidak diizinkan; PY:F-01–F-15 **NOT VERIFIED**.

### Jumlah per status (55 butir)

| Status | Jumlah | Butir |
|---|---|---|
| COMPLETE dengan bukti | 17 | UW-01, UW-03–UW-09, UW-19, UW-20, UW-42, UW-46–UW-51 |
| OPEN (NOT STARTED / PARTIAL) | 6 | UW-12, UW-26, UW-37, UW-45, UW-52 (NOT STARTED); UW-44 (PARTIAL) |
| BLOCKED | 29 | UW-02, UW-10, UW-11, UW-14–UW-18, UW-21–UW-25, UW-27–UW-36, UW-38–UW-41, UW-43, UW-53 |
| NOT VERIFIED | 3 | UW-13, UW-54, UW-55 |

### Checklist PLANNING CLEAR (pembaruan §8)

| # | Kriteria | Status | Bukti |
|---|---|---|---|
| PC-1 | Sumber Batch 01 disetujui | YES | D-01, PR #18 |
| PC-2 | Konflik kritis: restore, DataStore | YES | D-03, D-02 |
| PC-3 | Toolchain + minSdk | YES (provisional, NOT VERIFIED) | D-06, D-05 |
| PC-4 | Kebijakan manifest awal (Auto Backup, `INTERNET`) | YES | D-07, D-08 |
| PC-5 | Stack test minimal | YES | D-09 |
| PC-6 | Aturan model data penilaian | PARTIAL | D-04; agregasi program dan representasi angka OPEN |
| PC-7 | Keputusan O-04 | PARTIAL | Ambang disetujui (D-10); eksekusi tidak diizinkan |
| PC-8 | Dokumentasi konsisten | PARTIAL | UW-43, UW-44, UW-45 |
| PC-9 | Tidak ada tautan rusak | YES | Skrip cek |
| PC-10 | Aturan kerja dan merge tersimpan | YES | `GITHUB_BRIDGE.md` §5 |

Owner menambahkan syarat (D-11): seluruh butir perencanaan Batch 01–10
yang belum selesai harus diselesaikan dan direview sebelum PLANNING CLEAR
dinyatakan YES.

**PLANNING CLEAR: NO** — PC-6, PC-7, PC-8 belum terpenuhi dan 38 butir
register belum COMPLETE. **IMPLEMENTATION VERIFIED: NO.**

## 13. Pembaruan status — cleanup UW-45, UW-22, UW-44 (2026-11-23)

Basis: `main` = `2114ca8` (merge PR #19). Berlaku saat PR cleanup ini
di-merge.

| ID | Status baru | AC (§3) | Bukti |
|---|---|---|---|
| UW-45 | **COMPLETE** | "Satu label per sumber" | Lima dokumen Batch 05–09 (ASM, BKP, CAL, UI, CUR) memakai legenda yang sama: RECOVERED = asal-usul saja; OWNER APPROVED WITH CONDITIONS (D-01 M-xx) = disetujui sesuai B01 §7.1; PROPOSED = belum disetujui (termasuk B01 §3 di luar M-01–M-19); NOT VERIFIED = menunggu bukti. Pemindaian `grep` tidak menemukan lagi "RECOVERED" sebagai status persetujuan atau label "menunggu B-3". Rincian yang tidak tercantum di D-01 (mis. penilaian otomatis setelah tenggat, ASM:T7/ASM:D-04/ASM:D-05; konsekuensi kata sandi hilang, BKP:A-6; B01 §3 di CUR:K-10–K-12, CUR:RM-03) tetap PROPOSED |
| UW-22 | **BLOCKED** (menunggu owner) | "Kasus batas lolos secara eksak" + keputusan owner | Lembar keputusan [NUMERIC_PRECISION_DECISION_SHEET.md](NUMERIC_PRECISION_DECISION_SHEET.md) dibuat: 4 opsi, bukti hitungan (19 kombinasi skor bulat diputuskan salah oleh float naif), rekomendasi NP-4. Belum ada keputusan owner |
| UW-44 | **COMPLETE** | "Tidak ada ID ambigu" | Rujukan lintas dokumen ke ID lokal yang dipakai ulang kini memakai kode dokumen (`PY:`, `BKP:`, `ASM:`, `CAL:`, `UI:`, `FIN:`, `AUD:`, `HS:`). Konvensi diperluas di DECISIONS_LOG (termasuk `D-01`–`D-11` = keputusan owner, `BKP:AB-x` vs gate `AB-x`). Catatan ID ditambahkan di ASM §0 (kriteria tenggat lokal `D-xx`) dan audit §4 (`AUD:D-xx`). Pemindaian otomatis tersisa 12 kecocokan, semuanya bukan ambigu: rujukan gate QG `AB-3`, kelanjutan rentang `BKP:M-1 / M-2 / M-3`, dan teks penjelasan konvensi. ID historis tidak dinomori ulang; dokumen verbatim/terkunci (BL, TD, PLANNING_HISTORY) tidak diubah dan tidak memiliki rujukan ambigu yang memerlukan perubahan |

### Jumlah per status (55 butir)

| Status | Jumlah | Perubahan dari §12 |
|---|---|---|
| COMPLETE dengan bukti | 19 | + UW-44, UW-45 |
| OPEN (NOT STARTED / PARTIAL) | 4 | − UW-44, UW-45 |
| BLOCKED | 29 | UW-22 tetap BLOCKED (menunggu owner) |
| NOT VERIFIED | 3 | — |

OPEN tersisa: UW-12 (menunggu izin D-10), UW-26, UW-37, UW-52.

### Checklist PLANNING CLEAR

PC-8 (dokumentasi konsisten): UW-44 dan UW-45 selesai; **UW-43** (path
`PLANNING_COMPLETION_BATCH.md`) tetap BLOCKED karena menyentuh dokumen
Batch 02 yang verbatim → PC-8 tetap **PARTIAL**.

**PLANNING CLEAR: NO.** **IMPLEMENTATION VERIFIED: NO.** D-10: eksekusi
prototipe **NOT AUTHORIZED**. D-11: implementasi **DEFERRED**.

## 14. Pembaruan status — persiapan keputusan owner (2026-11-23)

Basis: `main` = `6a805a1` (merge PR #20). Lembar keputusan disiapkan;
**tidak ada** butir yang menjadi COMPLETE karena keputusan owner belum ada.

| ID | Status | Catatan |
|---|---|---|
| UW-22 | **BLOCKED** (menunggu owner) | [NUMERIC_PRECISION_DECISION_SHEET.md](NUMERIC_PRECISION_DECISION_SHEET.md) §8: verifikasi ulang matematika (0 perbedaan dari 200.000 uji acak NP-4 vs pecahan eksak); **koreksi** batas overflow (contoh semula "≤ 10⁶" salah, batas aman `Long` M ≤ 17.426; usulan `max ≤ 10.000`); usulan tie dan tampilan; pertanyaan UW-22-Q1–Q4 |
| UW-36 (CU-2) | **BLOCKED** (menunggu owner) | [CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md](CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md): Opsi A vs B; rekomendasi Opsi A; pertanyaan CU-2-Q1–Q3. Bagian lain UW-36 (CU-3, CU-5–CU-7, CU-9, CU-11) tetap OPEN |
| UW-17 (UO-1) | **BLOCKED** (menunggu owner) | [ACCESSIBILITY_COLOR_DECISION_SHEET.md](ACCESSIBILITY_COLOR_DECISION_SHEET.md): tabel kontras, varian turunan, pasangan teks–latar; pertanyaan UO-1-Q1–Q3 |
| UW-18 (UO-2) | **BLOCKED** (menunggu owner) | idem: DM-1/DM-2/DM-3, fakta Force Dark dan dynamic color dari dokumentasi resmi; pertanyaan UO-2-Q1–Q2 |

### Jumlah per status (55 butir) — tidak berubah dari §13

| Status | Jumlah |
|---|---|
| COMPLETE dengan bukti | 19 |
| OPEN (NOT STARTED / PARTIAL) | 4 (UW-12, UW-26, UW-37, UW-52) |
| BLOCKED | 29 |
| NOT VERIFIED | 3 (UW-13, UW-54, UW-55) |

**PLANNING CLEAR: NO.** **IMPLEMENTATION VERIFIED: NO.** D-10: eksekusi
prototipe **NOT AUTHORIZED**. D-11: implementasi **DEFERRED**.
PY:F-01–F-15: **NOT VERIFIED**.

## 15. Pembaruan status — D-12–D-15, OD-1/OD-2/UW-43 (2026-11-24)

Basis: `main` = `b789e9a` (merge PR #21). Berlaku saat PR pencatatan
D-12–D-15 di-merge.

### 15.1 Perubahan status

| ID | Status baru | AC (§3) | Bukti / sisa |
|---|---|---|---|
| UW-22 | **COMPLETE** | "Putuskan" + "Kasus batas ASM:B-01–B-10 lolos secara eksak" | Keputusan D-12 (NP-4). **Setiap** kasus ASM:B-01–B-10 dievaluasi secara eksplisit dengan aturan integer NP-4 dan cocok dengan tabel ASM §6.3 (NUM §10; 10/10). Uji acak NUM §8.1 hanya bukti pelengkap. Catatan: nilai asli ASM:B-08 (74,999) tidak dapat direpresentasikan dalam `max ≤ 10.000`; diuji dengan varian 74,975 dan 74,99. Verifikasi pada implementasi → UW-56 (NOT VERIFIED) |
| UW-17 | **COMPLETE** | "Token memenuhi U1" | Keputusan D-14; semua pasangan yang disetujui memenuhi ambang menurut hitungan (ACC §2, §4). Verifikasi perangkat → UW-56 |
| UW-18 | **COMPLETE** | "Keputusan tertulis" | Keputusan D-15 (DM-1, Force Dark nonaktif, dynamic color nonaktif). Perilaku perangkat → UW-56 |
| UW-36 | **BLOCKED** (diperbarui) | CU-2, CU-3, CU-5–CU-7, CU-9, CU-11 terisi | CU-2 diputuskan (D-13); CU-9 sebagian (capstone = mini-project modul 16). Sisa: CU-3, CU-5, CU-6, CU-7, CU-11, rubrik capstone |
| UW-11 | **BLOCKED** (diperbarui) | "Aturan tertulis" | Kelulusan modul (D-04), representasi (D-12), penggabungan aktivitas dalam komponen (D-13) tertulis. Sisa: UW-11-Q1 — perlukah skor numerik tingkat program (D-04 melarang rata-rata baru) |
| UW-15 | **BLOCKED** (menunggu owner) | "Parameter tertulis + bukti" | Lembar [OD1_BACKUP_CRYPTO_DECISION_SHEET.md](OD1_BACKUP_CRYPTO_DECISION_SHEET.md); OD-1-Q1–Q6 (rujukan dikoreksi 2026-11-24; diputuskan D-16, lihat §16) |
| UW-16 | **BLOCKED** (menunggu owner) | "Keputusan tertulis" | Lembar [OD2_BACKUP_INTEGRITY_DECISION_SHEET.md](OD2_BACKUP_INTEGRITY_DECISION_SHEET.md); OD-2-Q1–Q5 |
| UW-43 | **BLOCKED** (menunggu owner) | "Rujukan valid" | Lembar [UW43_PATH_CONSISTENCY_DECISION_SHEET.md](UW43_PATH_CONSISTENCY_DECISION_SHEET.md); rekomendasi Opsi B. **Koreksi:** hanya TD:5 yang memuat path salah (bukan TD:68) |
| UW-56 | **NOT VERIFIED** (baru) | Bukti EV untuk NUM:NA-1–NA-6 dan ACC:AT-1–AT-6 di implementasi | Verifikasi keputusan D-12–D-15 di aplikasi nyata. Oleh: T, setelah izin implementasi |

### 15.2 Jumlah per status (56 butir)

| Status | Jumlah | Butir |
|---|---|---|
| COMPLETE dengan bukti | 22 | UW-01, UW-03–UW-09, UW-17–UW-20, UW-22, UW-42, UW-44–UW-51 |
| OPEN (NOT STARTED / PARTIAL) | 4 | UW-12, UW-26, UW-37, UW-52 |
| BLOCKED | 26 | UW-02, UW-10, UW-11, UW-14–UW-16, UW-21, UW-23–UW-25, UW-27–UW-36, UW-38–UW-41, UW-43, UW-53 |
| NOT VERIFIED | 4 | UW-13, UW-54, UW-55, UW-56 |

### 15.3 Pemisahan jalur: perencanaan vs gerbang vs verifikasi

*Dikoreksi 2026-11-24 setelah review: izin eksekusi prototipe (UW-10)
bukan lagi syarat PLANNING CLEAR.*

Klasifikasi di bawah adalah **usulan** dan menunggu konfirmasi owner
(PL-Q1–PL-Q3 di [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md)).
Tidak ada acceptance criteria yang dihapus; setiap butir tetap memakai AC
di §3.

Untuk prototipe Python (O-04) dibedakan tiga hal:

| Aspek | Jalur | Status |
|---|---|---|
| Rencana prototipe, acceptance criteria (ambang F-03/F-04/F-11–F-13, target uji), dan persyaratan keamanan (isolasi proses, penolakan jaringan, perlindungan data aplikasi) | **P — perencanaan** | Disetujui sebagai rencana (D-10; PY §4, §6, §9; D-08) |
| Izin eksplisit untuk **mengeksekusi** prototipe | **G — gerbang owner setelah PLANNING CLEAR** | UW-10, belum diberikan |
| Eksekusi prototipe dan kelayakan runtime final (PY:F-01–F-15, pemilihan runtime) | **V — verifikasi setelah izin** | UW-12, NOT VERIFIED |

Klasifikasi seluruh 34 butir yang belum COMPLETE:

| Jalur | Butir | Jumlah | Syarat untuk |
|---|---|---|---|
| **P — Perencanaan** (keputusan owner, dokumentasi, akses sumber) | UW-11, UW-14, UW-15, UW-16, UW-23, UW-24, UW-25, UW-26, UW-27, UW-28, UW-29, UW-30, UW-31, UW-32, UW-33, UW-34, UW-35, UW-36, UW-37 (cakupan menunggu PL-Q2), UW-41, UW-43, UW-53 | 22 | PLANNING CLEAR |
| **M — Ditunda ke milestone** (usulan, menunggu PL-Q3) | UW-21, UW-38, UW-40 | 3 | Milestone terkait |
| **G — Gerbang owner setelah PLANNING CLEAR** | UW-10 (izin eksekusi prototipe), UW-02 (izin implementasi) | 2 | Membuka jalur V |
| **V — Verifikasi setelah izin** | UW-12, UW-13, UW-39, UW-52, UW-54, UW-55, UW-56 | 7 | IMPLEMENTATION VERIFIED |

Total 22 + 3 + 2 + 7 = 34 = 4 OPEN + 26 BLOCKED + 4 NOT VERIFIED.

Ketergantungan melingkar yang dihindari: pemilihan runtime Python final
membutuhkan hasil PY:F-01–F-15, sedangkan eksekusi prototipe (D-10)
mensyaratkan kebutuhan perencanaan selesai lebih dulu. Dengan pemisahan
di atas, PLANNING CLEAR hanya mensyaratkan rencana, ambang, dan persyaratan
keamanan prototipe; izin eksekusi adalah gerbang sesudahnya; runtime final
adalah hasil verifikasi. D-10 dan D-11 tidak berubah.

### 15.4 Checklist PLANNING CLEAR

| # | Kriteria | Status |
|---|---|---|
| PC-1–PC-5 | (lihat §12) | YES (PC-3 provisional, NOT VERIFIED) |
| PC-6 | Aturan model data penilaian | PARTIAL — sisa UW-11-Q1 |
| PC-7 | O-04: rencana uji, ambang penerimaan, dan persyaratan keamanan prototipe disetujui (izin eksekusi = gerbang UW-10 sesudah PLANNING CLEAR, bukan syarat) | YES — D-10, PY §4/§6/§9, D-08 |
| PC-8 | Dokumentasi konsisten | PARTIAL — UW-43 |
| PC-9, PC-10 | — | YES |
| PC-11 | Seluruh butir jalur P selesai atau ditetapkan owner sebagai tidak wajib | NO — 22 butir P belum COMPLETE |

**PLANNING CLEAR: NO.** **IMPLEMENTATION VERIFIED: NO.** D-10: eksekusi
prototipe **NOT AUTHORIZED**. D-11: implementasi **DEFERRED**.
PY:F-01–F-15: **NOT VERIFIED**.

## 16. Pembaruan status — D-16–D-22 (2026-11-24)

Basis: `main` = `bcecdae` (merge PR #22). Berlaku saat PR pencatatan
D-16–D-22 di-merge. Keputusan owner tidak otomatis menutup butir; setiap
perubahan diperiksa terhadap AC di §3.

### 16.1 Perubahan status

| ID | Sebelum | Sesudah | AC (§3) | Bukti / alasan |
|---|---|---|---|---|
| UW-11 | BLOCKED | **COMPLETE** | "Aturan tertulis" | D-19: tanpa skor/rata-rata/ambang program; program = 16 modul lulus + capstone memenuhi rubrik; aturan modul (D-04, D-12, D-13) tertulis |
| UW-16 | BLOCKED | **COMPLETE** | "Keputusan tertulis" | D-17 (I-1, risiko residual diterima) |
| UW-43 | BLOCKED | **COMPLETE** | "Rujukan valid" | D-18 Opsi B; erratum ER-1 di DECISIONS_LOG; TD tidak diubah; file di root; tautan relatif 0 rusak (UW43 §5) |
| UW-15 | BLOCKED | **NOT VERIFIED** (jalur V, usulan — RM-Q1) | "Parameter tertulis + bukti" (tetap) | Keputusan algoritma/KDF/batas minimum tertulis (D-16). Sisa: nilai parameter final dan batas maksimum + bukti dari pengukuran perangkat yang **diizinkan terpisah** (D-16 Q3). Sisa **perencanaan** OD-1 dipindah eksplisit ke UW-33 (OD-11–OD-14, §16.5). Restore produksi nonaktif sampai RR-1–RR-8 (OD1 §11) |
| UW-21 | BLOCKED | **DEFERRED** (M) | "Keputusan tertulis" (tetap) | D-22; bukan penyelesaian |
| UW-38 | BLOCKED | **DEFERRED** (M) | AP-3–AP-5 (tetap) | D-22 |
| UW-40 | BLOCKED | **DEFERRED** (M) | (tetap) | D-22 |
| UW-26 | OPEN | OPEN | CUR:CC-08 | Lembar OP-4 dibuat; keputusan belum ada |
| UW-36 | BLOCKED | BLOCKED | CU terkait terisi | Lembar CU-6 dibuat; CU-3, CU-5, CU-6, CU-7, CU-9, CU-11 belum diputuskan |
| UW-37 | OPEN | OPEN (NOT STARTED) | CUR:CC-01–CC-11 | Wajib di jalur P (D-21); rencana produksi dibuat, konten 0/64 |
| UW-33 | BLOCKED | BLOCKED | OD-5–OD-9 **dan** OD-11–OD-14 (perluasan, RM-Q1) | Ditambah: retensi dan penyimpanan log restore (D-17); serialisasi envelope (OD-11), kebijakan KDF cadangan (OD-12), protokol pengukuran (OD-13), review dependensi BC (OD-14) |

Tidak ada butir baru di batch ini.

### 16.2 Jumlah per status (56 butir)

| Status | §15.2 (sebelum) | §16.2 (sesudah) | Butir |
|---|---|---|---|
| COMPLETE | 22 | **25** | UW-01, UW-03–UW-09, UW-11, UW-16–UW-20, UW-22, UW-42–UW-51 |
| OPEN | 4 | **4** | UW-12, UW-26, UW-37, UW-52 |
| BLOCKED | 26 | **19** | UW-02, UW-10, UW-14, UW-23–UW-25, UW-27–UW-36, UW-39, UW-41, UW-53 |
| DEFERRED | — | **3** | UW-21, UW-38, UW-40 |
| NOT VERIFIED | 4 | **5** | UW-13, UW-15, UW-54, UW-55, UW-56 |
| **Total** | 56 | **56** | |

### 16.3 Jalur (D-20, D-21, D-22)

| Jalur | Butir belum selesai | Jumlah |
|---|---|---|
| P | UW-14, UW-23, UW-24, UW-25, UW-26, UW-27, UW-28, UW-29, UW-30, UW-31, UW-32, UW-33, UW-34, UW-35, UW-36, UW-37, UW-41, UW-53 | 18 |
| M | UW-21, UW-38, UW-40 | 3 |
| G | UW-02, UW-10 | 2 |
| V | UW-12, UW-13, UW-15, UW-39, UW-52, UW-54, UW-55, UW-56 | 8 |

Kemajuan jalur P: 25 selesai dari 43 butir P (dihitung per butir, bukan
per beban; konten UW-37 = 0/64 komponen). Rincian per butir:
[PLANNING_ROADMAP.md](PLANNING_ROADMAP.md).

### 16.4 Checklist PLANNING CLEAR

| # | Kriteria | Status |
|---|---|---|
| PC-1–PC-5 | (lihat §12) | YES (PC-3 provisional, NOT VERIFIED) |
| PC-6 | Aturan model data penilaian | **YES** — D-04, D-12, D-13, D-19 |
| PC-7 | Rencana, ambang, dan keamanan prototipe O-04 | YES — D-10, D-08 |
| PC-8 | Dokumentasi konsisten | **YES** — UW-43 selesai (D-18), UW-44/UW-45 selesai; tautan 0 rusak |
| PC-9, PC-10 | — | YES |
| PC-11 | Seluruh butir jalur P selesai (D-20, D-21) | **NO** — 18 butir P belum selesai, termasuk UW-37 (0/64 komponen) |

**PLANNING CLEAR: NO.** **IMPLEMENTATION VERIFIED: NO.** D-10: eksekusi
prototipe **NOT AUTHORIZED**. D-11: implementasi **DEFERRED**.
PY:F-01–F-15: **NOT VERIFIED**.

### 16.5 Revisi setelah review PR #23 (F-01–F-06)

| Temuan | Perbaikan |
|---|---|
| F-01 | Ketergantungan melingkar kurikulum dicabut: konten W9–W12 dapat diterima sebagai perencanaan sebelum runtime dieksekusi; eksekusi tetap NOT VERIFIED; UW-21 tidak memblokir penerimaan itu; bila runtime gagal setelah izin, implementasi terdampak dihentikan, kurikulum diubah hanya atas keputusan owner, lalu divalidasi ulang ([PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §5.2, RM:RV-1–RV-6). D-21 tidak dikurangi |
| F-02 | OD-1 dipisah: keputusan D-16; sisa perencanaan → UW-33 (OD-5–OD-9, OD-11–OD-14); verifikasi → UW-15; syarat rilis restore RR-1–RR-8 ([OD1_BACKUP_CRYPTO_DECISION_SHEET.md](OD1_BACKUP_CRYPTO_DECISION_SHEET.md) §11). Pemindahan UW-15 ke V menunggu RM-Q1 |
| F-03 | Lembar OP-4: aturan skor deterministik CE-S1–CE-S5, adjacency maksimum terhadap satu urutan diterima lengkap, validasi CE-V1–CE-V6, contoh diperiksa ulang; contoh pencocokan lama dikoreksi |
| F-04 | Lembar CU-6: anggaran eksekusi vs ambang D-10, kode hasil, penyebab pelajar vs infrastruktur, output > 64 KB selalu gagal, eksekusi tidak lengkap, pelestarian poin, penyelesaian attempt dan XP, ketergantungan OP-7/OP-8/OP-10 |
| F-05 | Seluruh 56 butir (termasuk COMPLETE) diklasifikasi P/M/G/V dengan alasan ([PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §2); diperiksa otomatis: 56 ID unik, tanpa duplikat/hilang |
| F-06 | Ketergantungan produksi kurikulum lengkap di roadmap §5.3; alokasi jam tetap PROPOSED (CU2-O3) |

Jumlah per status **tidak berubah** dari §16.2: 25 COMPLETE, 4 OPEN,
19 BLOCKED, 3 DEFERRED, 5 NOT VERIFIED (56).

Klasifikasi jalur seluruh register (56):

| Jalur | COMPLETE | Belum | Total |
|---|---|---|---|
| P | 25 | 18 | 43 |
| M | 0 | 3 | 3 |
| G | 0 | 2 | 2 |
| V | 0 | 8 | 8 |

- Kemajuan register: 25/56 butir COMPLETE (44,6%).
- Kemajuan jalur P: 25/43 butir (58,1%); bila RM-Q1(a) ditolak, 25/44 (56,8%).
- Seluruh 25 butir COMPLETE ada di jalur P dan dipenuhi keputusan owner atau
  pekerjaan dokumentasi; tidak ada verifikasi teknis aplikasi yang dihitung
  sebagai penyelesaian perencanaan.
- Kedua angka adalah jumlah butir, **bukan** beban kerja dan **bukan**
  kesiapan aplikasi. UW-37 = 0/64 komponen.

**PLANNING CLEAR: NO.** **IMPLEMENTATION VERIFIED: NO.** D-10: eksekusi
prototipe **NOT AUTHORIZED**. D-11: implementasi **DEFERRED**.
PY:F-01–F-15: **NOT VERIFIED**.

## 17. Pembaruan status — D-23–D-25 dan batch keputusan kurikulum (2026-11-24)

Basis: `main` = `928e278` (merge PR #23). Berlaku saat PR pencatatan
D-23–D-25 di-merge. Dihitung ulang dari bukti di repositori; keputusan owner
tidak otomatis menutup butir.

### 17.1 Perubahan per butir

| ID | Status | Perubahan | Alasan tidak COMPLETE |
|---|---|---|---|
| UW-15 | NOT VERIFIED | Jalur V **disetujui D-25**; izin pengukuran = prasyarat | AC "bukti" butuh pengukuran yang belum diizinkan; CT-1–CT-12 NOT VERIFIED |
| UW-26 | OPEN | OP-4 **diputuskan D-23** | AC CUR:CC-08 butuh bank soal penjelasan konsep 16 modul (belum ditulis) |
| UW-36 | BLOCKED | CU-6 **diputuskan D-24**; cakupan + CU2-O3, CU2-O4 (D-25); lembar CU-3, CU-5, CU-7, CU-9, CU-11, CU2-O3, CU2-O4 disiapkan | 7 keputusan CU masih OPEN |
| UW-33 | BLOCKED | Cakupan + OD-11–OD-14 **disetujui D-25** | OD-5–OD-9, OD-11–OD-14 belum diputuskan |
| UW-25 | BLOCKED | Lembar CU-10 disiapkan | Keputusan owner belum ada |
| UW-27 | BLOCKED | Lembar OP-5 disiapkan | Keputusan owner belum ada (ASM:D-08 kosong) |
| UW-29 | BLOCKED | Lembar OP-7 disiapkan | Keputusan owner belum ada (ASM:L5) |
| UW-30 | BLOCKED | Lembar OP-8/CU-4 disiapkan | Keputusan owner belum ada (ASM:X-07) |
| UW-31 | BLOCKED | Lembar OP-9 disiapkan | Keputusan owner belum ada (ASM:C6) |
| UW-32 | BLOCKED | Lembar OP-10/OP-11 disiapkan | Keputusan owner belum ada |
| UW-37 | OPEN | Templat CB-0 provisional; matriks diperbarui | 0/64 komponen |
| UW-21, UW-38, UW-40 | DEFERRED | Tidak berubah (D-22) | Ditunda, bukan selesai |

### 17.2 Jumlah (rekonsiliasi terhadap baseline PR #23)

| Status | Baseline §16 | Sesudah batch ini |
|---|---|---|
| COMPLETE | 25 | 25 |
| OPEN | 4 | 4 (UW-12, UW-26, UW-37, UW-52) |
| BLOCKED | 19 | 19 |
| DEFERRED | 3 | 3 |
| NOT VERIFIED | 5 | 5 (UW-13, UW-15, UW-54, UW-55, UW-56) |
| **Total** | 56 | 56 |

Jalur (D-20, D-25): P 43 (25 COMPLETE, 18 belum) · M 3 · G 2 · V 8.

### 17.3 Laporan kemajuan (terpisah; jumlah butir, bukan beban kerja atau kesiapan aplikasi)

| # | Ukuran | Nilai |
|---|---|---|
| 1 | Register keseluruhan | 25/56 COMPLETE (44,6%) |
| 2 | Jalur P wajib | 25/43 (58,1%) |
| 3 | Komponen kurikulum | 0/64 (templat tidak dihitung) |
| 4 | Keputusan owner | D-01–D-25 tercatat; **45** pertanyaan baru AWAITING OWNER setelah revisi §17.4 (OP-5, OP-7, OP-8/CU-4, OP-9, OP-10, OP-11, OD-15, CU-3, CU-5, CU-7, CU-9, CU-10, CU-11, CU2-O3, CU2-O4, CU2-O5, LX CU-6) |
| 5 | Ketergantungan kritis | Gelombang 1 untuk CB-0: CU-3, CU-5, CU2-O5, OP-5, CU2-O3, CU2-O4, OP-8-Q1–Q3/CU-4, OP-7, OP-10; lalu CB-1–CB-4 (UW-37, UW-26) |

**PLANNING CLEAR: NO.** **IMPLEMENTATION VERIFIED: NO.** D-10: eksekusi
prototipe **NOT AUTHORIZED**. D-11: implementasi **DEFERRED**.
PY:F-01–F-15: **NOT VERIFIED**. CT-1–CT-12: **NOT VERIFIED**.

### 17.4 Revisi setelah review PR #24 (F-01–F-09)

| Temuan | Perbaikan |
|---|---|
| F-01 | Klaim bahwa XE-C (dua slot) otomatis sesuai aturan satu-award dicabut; rekomendasi diganti XE-B (satu award per `xp_id` saat pertama ≥ 75); identitas komponen vs aktivitas lab, aktivitas tidak dinilai, milestone terpisah; contoh dihitung ulang (4.660 XP → level 10; tanpa milestone 3.760 → level 9) |
| F-02 | Restore M-1 dapat menurunkan XP/level/streak (penggantian snapshot, bukan penalti); M-2 tidak membuktikan ledger lengkap; validasi XV-1–XV-6; identitas pensiun vs rusak; tanpa perbaikan diam-diam; perlakuan → OD-15 di UW-33 (usulan); minggu JST setengah terbuka (SK-1–SK-6) |
| F-03 | Batas 45 menit = durasi standar; TA-B pengecualian eksplisit, maks. 68 menit; dicatat sebelum mulai; tenggat aktif tidak diubah; di luar 128 jam |
| F-04 | Ujian memakai tulis segera DL-1–DL-9; urutan transaksi tulis vs penguncian; `PERSISTENCE_FAILURE` vs input belum tersimpan; tanpa jaminan durabilitas tanpa syarat; skenario DG-1–DG-8 |
| F-05 | LX-1–LX-9: per eksekusi vs agregat (nilai OPEN), urutan deterministik, isolasi state, tanpa klaim kesetaraan, pencatatan mode/versi, review sebelum aktivasi TB-A |
| F-06 | Contoh A.4 dihitung ulang langkah demi langkah dari komposisi (hasil sama: 33, 18, 10, ditolak); ujian + review muat di U; OP-5-Q5 kini mencakup EX-1–EX-13 |
| F-07 | Poin Git integer (CR-5 3/3/2/2; W15 K1 6 × 10); pemetaan CE-S ke anggaran 10 lewat komposisi; validasi berkas final vs commit; klaim tanda tangan fungsi dicabut; skema SQL dengan tabel `modul`; tie-break Q3; aturan real dan `ORDER BY`; CP-6 capstone tetap dapat diulang |
| F-08 | PB-A direvisi: konversi dasar di W9; W10 tanpa percabangan/exception; prasyarat tiap proyek diperiksa |
| F-09 | Matriks 45 pertanyaan dengan ID unik yang cocok dengan lembar; asumsi 6 soal concept dan 3 aktivitas lab diajukan (CU2-O5-Q1); CB-0 tetap provisional; 64 komponen NOT STARTED |

Jumlah status tidak berubah (§17.2): 25 / 4 / 19 / 3 / 5 = 56. Jalur P
25/43. Kurikulum 0/64.

## 18. Pembaruan status — D-26–D-35, CB-0, dan konten W1 (2026-11-24)

Basis: `main` = `40ca205` (merge PR #24). Berlaku saat PR batch ini di-merge.
Dihitung ulang dari bukti di repositori; keputusan yang disetujui tidak
otomatis menutup butir.

### 18.1 Perubahan per butir

| ID | Sebelum | Sesudah | AC (§3) | Bukti / alasan |
|---|---|---|---|---|
| UW-25 | BLOCKED | **COMPLETE** | Keputusan tertulis | D-34 (CU-10, AK-A) |
| UW-27 | BLOCKED | **COMPLETE** | ASM:D-08 terisi | D-26 (rumus durasi A.4, format TF-1–TF-5) |
| UW-29 | BLOCKED | **COMPLETE** | ASM:L5 terisi | D-27 (SB-A, SB-1–SB-12) |
| UW-30 | BLOCKED | **COMPLETE** | ASM:X-07 terisi | D-28 (identitas, kelayakan, jumlah, level, streak, achievement/mastery, revisi). Tanpa batas atas XP selain "sekali per identitas" |
| UW-31 | BLOCKED | **COMPLETE** | ASM:C6 terisi | D-27 (UL-1–UL-10) |
| UW-32 | BLOCKED | **COMPLETE** | OP-10, OP-11 terisi | D-27 (RE-A, PI-A, AS-B) |
| UW-36 | BLOCKED | BLOCKED | CU-2, CU-3, CU-5–CU-7, CU-9, CU-11 (+ CU2-O3–O5) terisi | Semua diputuskan kecuali bagian CU-6 "kebijakan umpan balik test tersembunyi" (CUR §10) → **CU-6-Q13** |
| UW-33 | BLOCKED | BLOCKED | OD-5–OD-9, OD-11–OD-14 (+ OD-15) terisi | OD-15-Q1 diputuskan (D-29); OD-15-Q2 diajukan; OD lain belum |
| UW-26 | OPEN | OPEN | CUR:CC-08 (bank 16 modul) | Bank concept W1 diproduksi (12 soal), belum diterima; W2–W16 belum |
| UW-37 | OPEN | OPEN | CUR:CC-01–CC-11 | W1 diproduksi (4/64 komponen), belum diterima owner |
| UW-15 | NOT VERIFIED | NOT VERIFIED | Parameter + bukti | Tidak berubah; CT-1–CT-12 NOT VERIFIED |
| UW-21, UW-38, UW-40 | DEFERRED | DEFERRED | — | D-22 |

### 18.2 Jumlah per status (56 butir)

| Status | §17 (sebelum) | §18 (sesudah) | Butir |
|---|---|---|---|
| COMPLETE | 25 | **31** | + UW-25, UW-27, UW-29, UW-30, UW-31, UW-32 |
| OPEN | 4 | 4 | UW-12, UW-26, UW-37, UW-52 |
| BLOCKED | 19 | **13** | UW-02, UW-10, UW-14, UW-23, UW-24, UW-28, UW-33, UW-34, UW-35, UW-36, UW-39, UW-41, UW-53 |
| DEFERRED | 3 | 3 | UW-21, UW-38, UW-40 |
| NOT VERIFIED | 5 | 5 | UW-13, UW-15, UW-54, UW-55, UW-56 |
| **Total** | 56 | **56** | |

Jalur: P 43 (31 COMPLETE, 12 belum: UW-14, UW-23, UW-24, UW-26, UW-28,
UW-33, UW-34, UW-35, UW-36, UW-37, UW-41, UW-53) · M 3 · G 2 · V 8.

### 18.3 Kemajuan (dilaporkan terpisah; jumlah butir, bukan kesiapan aplikasi)

| Ukuran | Nilai |
|---|---|
| Register | 31/56 (55,4%) |
| Jalur P | 31/43 (72,1%) |
| Kurikulum diproduksi | 1/16 modul · 4/64 komponen · 8/128 jam · 40/620 soal teori · 12/192 soal concept · 6/96 spesifikasi lab · 1/16 mini-project |
| Kurikulum direview (ChatGPT) | 0 |
| Kurikulum diterima owner | 0 |
| Runtime diverifikasi | Tidak ada (D-10, D-11) |
| Keputusan owner | D-01–D-35 tercatat; terbuka: CU-6-Q13, OD-15-Q2, penerimaan W1; lembar belum disiapkan: OP-6, CO-1/2, O-09, OD-5–OD-9, OD-11–OD-14, CO-4–CO-6, UO-3–UO-9 |

**PLANNING CLEAR: NO.** **IMPLEMENTATION VERIFIED: NO.** D-10: eksekusi
prototipe **NOT AUTHORIZED**. D-11: implementasi **DEFERRED**.
PY:F-01–F-15: **NOT VERIFIED**. CT-1–CT-12: **NOT VERIFIED**.

### 18.4 Rekonsiliasi setelah review PR #25 (F-08)

AC asli §3 diperiksa ulang terhadap bukti:

| ID | AC asli (§3) | Bukti | Tetap COMPLETE? |
|---|---|---|---|
| UW-25 | "Keputusan tertulis" (penerimaan risiko kunci jawaban, CU-10) | D-34 tercatat di DECISIONS_LOG, checklist, dan CU10 §7 | Ya |
| UW-27 | "ASM:D-08 terisi" (rumus durasi, format soal) | D-26: rumus A.4 + TF-1–TF-5 tertulis dan disetujui; diterapkan pada W1 (33 menit dihitung dari komposisi) | Ya |
| UW-29 | "L5 terisi" (aturan pengumpulan/interupsi) | D-27: SB-A, SB-1–SB-12 | Ya |
| UW-30 | "ASM:X-07 terisi" (identitas, jumlah, batas, level, streak, achievement, mastery, revisi) | D-28: XI-1–XI-9, XE-B, jumlah §5, level §6, ST-C, XA-1–XA-3; "batas" = sekali per identitas, tanpa batas atas level (tertulis) | Ya |
| UW-31 | "C6 terisi" (unlock rinci) | D-27: UL-1–UL-10, PV-A, RV-A | Ya |
| UW-32 | "OP-10, OP-11 terisi" | D-27: RE-A, PI-A, AS-B | Ya |

AC keenam butir adalah **keputusan tertulis**, bukan konten atau
verifikasi; bukti terpenuhi. Kurikulum diproduksi (W1), review ChatGPT,
penerimaan owner, dan verifikasi teknis tetap dilacak terpisah (§18.3).
Jumlah per status **tidak berubah**: 31 / 4 / 13 / 3 / 5 = 56; jalur P
31/43. W1: diproduksi dan direvisi; belum lolos review ChatGPT; **belum**
diterima owner. CB-0: dapat dipakai W1–W8; finalisasi global menunggu
CU-6-Q13.

### 18.5 Revisi kualitas W1 putaran 2 (review PR #25, F-09–F-18)

Perbaikan konten W1: maksimum lab act-02 kini dapat dicapai (4 poin per
pasangan; komponen lab 100, sebelumnya hanya 97 yang dapat dicapai); arah
konversi satuan remedial diperbaiki; presisi soal teori s03/s05/s07/s09/s17;
kesetaraan concept s02/s03/s06; contoh pelajaran 1 tidak lagi sama dengan
lab; penyederhanaan teknis diberi label; field kanonik dan aturan angka
deterministik; label perangkat tidak ambigu; CB-0 ditambah QC-01–QC-10.
Rincian: [curriculum/mod-w01/review.md](../curriculum/mod-w01/review.md).

Jumlah status **tidak berubah**: 31 / 4 / 13 / 3 / 5 = 56; jalur P 31/43.
Kurikulum: diproduksi 4/64, lolos review ChatGPT 0/64, diterima owner 0/64.
CU-6-Q13 (calon D-36) dan OD-15-Q2 (calon D-37) tetap AWAITING OWNER;
W01-ACC tertunda.

### 18.6 Revisi kecil W1 putaran 3 (review PR #25, F-19–F-21)

K2 rubrik proyek diselaraskan dengan definisi MR-A yang disetujui ("ada dan
valid secara bentuk") tanpa kebijakan baru; metadata lab per aktivitas;
bukti enumerasi lengkap 3.840 kombinasi
(`curriculum/mod-w01/project/evidence/catalog_enumeration.csv`) dan review
S09, Pelajaran 2–3, maksimum yang dapat dicapai, konsistensi instruksi, dan
regresi F-01–F-18 (`curriculum/mod-w01/review.md` §9). Jumlah status tidak
berubah: 31 / 4 / 13 / 3 / 5 = 56; jalur P 31/43; kurikulum diproduksi 4/64,
diterima 0/64. CU-6-Q13, OD-15-Q2, W01-ACC tetap AWAITING OWNER.

### 18.7 D-36, D-37 dan revisi W1 putaran 4 (2026-11-24)

| ID | Perubahan | Status | Alasan |
|---|---|---|---|
| UW-36 | Bagian CU-6 "umpan balik test tersembunyi" diputuskan D-36 | **BLOCKED** (tidak otomatis COMPLETE) | Semua kebijakan CU kini terisi; tersisa nilai angka batas agregat LX-2 yang menurut D-35 menunggu pengukuran. Pertanyaan **RM-Q2**: catat angka itu sebagai keluaran verifikasi UW-12 (jalur V) agar UW-36 dapat dinilai lengkap. Tanpa jawaban owner, status tidak diubah (D-20: tidak memindahkan persyaratan tanpa persetujuan) |
| UW-33 | OD-15-Q2 diputuskan D-37 (XV-7–XV-14, RX-A) | **BLOCKED** | OD-5–OD-9 dan OD-11–OD-14 belum diputuskan |
| UW-30 | D-37 melengkapi validasi restore XP | COMPLETE (tidak berubah) | — |

Jumlah status **tidak berubah**: 31 / 4 / 13 / 3 / 5 = 56; jalur P 31/43.
Kurikulum: diproduksi 4/64, lolos review independen 0/64, diterima owner
0/64. W01-ACC dan RM-Q2 AWAITING OWNER. Persetujuan D-36/D-37 bukan
verifikasi implementasi.

## 19. Pembaruan status — merge PR #25, D-38, W01-ACC, CB-0.5 (2026-11-24)

PR #25 di-merge pada head `f4cb17335c65489b165d2214e309ff2f00a765ee`
(merge commit `df76c5fbf946e6e8d2ca9e8e87505454041623a3`) atas otorisasi
eksplisit owner.

### 19.1 Perubahan per butir

| ID | Sebelum | Sesudah | AC | Bukti |
|---|---|---|---|---|
| UW-36 | BLOCKED | **COMPLETE** | CU-2, CU-3, CU-5–CU-7, CU-9, CU-11 (+ CU2-O3–O5) terisi | D-13, D-24, D-30–D-36 mengisi semua kebijakan; D-38 menetapkan angka batas agregat LX-2 sebagai keluaran verifikasi UW-12 (jalur V), sehingga tidak ada sisa AC perencanaan. Tidak ada pengukuran yang dilakukan |
| UW-12 | OPEN | OPEN (tidak berubah) | PY:F-01–F-15 PASS + angka LX-2 | Ditambah keluaran angka LX-2 (D-38). Tetap menunggu UW-10 dan izin (D-10 NOT AUTHORIZED) |
| UW-37 | OPEN | OPEN (tidak berubah) | CUR:CC-01–CC-11 | W1 diterima owner (W01-ACC); W2–W16 belum diproduksi |
| UW-26 | OPEN | OPEN (tidak berubah) | Rubrik concept per modul | Menunggu konten W2–W16 |

### 19.2 Jumlah per status (56 butir; dihitung ulang)

| Status | §18 | §19 | Butir |
|---|---|---|---|
| COMPLETE | 31 | **32** | + UW-36 |
| OPEN | 4 | 4 | UW-12, UW-26, UW-37, UW-52 |
| BLOCKED | 13 | **12** | UW-02, UW-10, UW-14, UW-23, UW-24, UW-28, UW-33, UW-34, UW-35, UW-39, UW-41, UW-53 |
| DEFERRED | 3 | 3 | UW-21, UW-38, UW-40 |
| NOT VERIFIED | 5 | 5 | UW-13, UW-15, UW-54, UW-55, UW-56 |
| **Total** | 56 | **56** | |

Jalur P 32/43 (74,4%); belum: UW-14, UW-23, UW-24, UW-26, UW-28, UW-33,
UW-34, UW-35, UW-37, UW-41, UW-53. Register 32/56 (57,1%).

### 19.3 Kurikulum dan review

| Ukuran | Nilai |
|---|---|
| Diproduksi | 1/16 modul · 4/64 komponen |
| Lolos review independen | W1 (PR #25), dengan batas di bawah |
| Diterima owner | 1/16 modul · 4/64 komponen (W01-ACC) |
| Runtime diverifikasi | Tidak ada (D-10, D-11) |

Batas review independen: F-22 dan F-23 menerima review akhir terarah; pencatatan D-36/D-37 diperiksa; enumerasi independen mengonfirmasi 3.840 kombinasi dan 46 build valid. **Tidak** setiap baris CSV terbaru, setiap butir penilaian yang berubah, atau setiap penerapan kontrak visibilitas diaudit ulang secara independen.

### 19.4 CB-0.5 (terpisah dari register UW)

CB-0.5 (alur kerja agen dan efisiensi token) **tidak** dipetakan ke butir UW
mana pun dan tidak mengubah jumlah di atas. Status dan bukti:
[AGENT_SKILL_REGISTRY.md](AGENT_SKILL_REGISTRY.md).

PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10: NOT AUTHORIZED ·
D-11: DEFERRED · PY:F-01–F-15 NOT VERIFIED · CT-1–CT-12 NOT VERIFIED.

## 20. Pembaruan status — merge PR #26, CB-0.5 diterima, CB-1 (W2–W4) (2026-11-24)

PR #26 di-merge pada head `691ae87ecc6507ea16a7051872729b4986345b4d`
(merge commit `ab0103e4954ead4ded6343d105d73a2729916cd6`) atas otorisasi
eksplisit owner. Owner menerima CB-0.5 (saat itu V03 NOT VERIFIED); V03
kemudian PASS di sesi baru. Owner mengotorisasi CB-1 (W2–W4).

### 20.1 Perubahan per butir

| ID | Sebelum | Sesudah | AC | Bukti |
|---|---|---|---|---|
| UW-37 | OPEN | OPEN (tidak berubah) | CUR:CC-01–CC-11 untuk 64 komponen + penerimaan | Diproduksi 16/64 (W1–W4); W2–W4 belum direview independen dan belum diterima owner; W5–W16 belum diproduksi. **Tidak** COMPLETE |
| UW-26 | OPEN | OPEN (tidak berubah) | Rubrik/bank concept per modul (16 modul) | Bank concept W1–W4 ada (4/16 modul, 48/192 soal); 12 modul belum |
| Lainnya | — | Tidak berubah | — | CB-1 hanya konten kurikulum + dokumen status |

### 20.2 Jumlah per status (56 butir; dihitung ulang dari §19.2 + §20.1)

| Status | §19 | §20 | Butir |
|---|---|---|---|
| COMPLETE | 32 | 32 | — |
| OPEN | 4 | 4 | UW-12, UW-26, UW-37, UW-52 |
| BLOCKED | 12 | 12 | UW-02, UW-10, UW-14, UW-23, UW-24, UW-28, UW-33, UW-34, UW-35, UW-39, UW-41, UW-53 |
| DEFERRED | 3 | 3 | UW-21, UW-38, UW-40 |
| NOT VERIFIED | 5 | 5 | UW-13, UW-15, UW-54, UW-55, UW-56 |
| **Total** | 56 | **56** | |

Jalur P 32/43 (74,4%); register 32/56 (57,1%).

### 20.3 Kurikulum (dilaporkan terpisah: produksi, review, penerimaan)

| Ukuran | Diproduksi | Review independen | Diterima owner |
|---|---|---|---|
| Modul | 4/16 (W1–W4) | 1/16 (W1, terbatas) | 1/16 (W1) |
| Komponen penilaian | **16/64** | 4/64 | **4/64** |
| Soal teori | 160/620 | 40 | 40 |
| Soal concept | 48/192 | 12 | 12 |
| Spesifikasi lab | 24/96 | 6 | 6 |
| Mini-project | 4/16 | 1 | 1 |
| Jam nominal | 32/128 | 8 | 8 |

Batas review independen W1 (§19.3) tetap berlaku. W2–W4: review mandiri
penyusun saja ([`curriculum/mod-w02/review.md`](../curriculum/mod-w02/review.md),
[`mod-w03`](../curriculum/mod-w03/review.md), [`mod-w04`](../curriculum/mod-w04/review.md)).

PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10: NOT AUTHORIZED ·
D-11: DEFERRED · PY:F-01–F-15 NOT VERIFIED · CT-1–CT-12 NOT VERIFIED.

## 21. Pembaruan status — koreksi konsolidasi CB-1 (PR #27, F-28–F-70) (2026-11-24)

Review PR #27 (head `a9241d33c2cf32e177ca92618df458b78dd6cb98`, base
`ab0103e4954ead4ded6343d105d73a2729916cd6`) = **REQUEST CHANGES**. Koreksi
diterapkan pada PR #27 yang sama; tidak ada PR baru, tidak ada merge.
Register disposisi per temuan: `review.md` W2/W3/W4 (§ register koreksi).
F-55, F-56, F-57, F-59: **BLOCKED — ORIGINAL FINDING DETAILS REQUIRED**.

### 21.1 Perubahan per butir

Tidak ada perubahan status butir. UW-26 **OPEN**, UW-37 **OPEN**: koreksi
konten tidak menambah modul yang diterima.

### 21.2 Jumlah per status (56 butir; sama dengan §20.2)

COMPLETE 32 · OPEN 4 · BLOCKED 12 · DEFERRED 3 · NOT VERIFIED 5 = **56**.
Jalur P 32/43.

### 21.3 Kurikulum

| Ukuran | Diproduksi | Diterima owner |
|---|---|---|
| Modul | 4/16 (W1–W4) | 1/16 (W1) |
| Komponen penilaian | 16/64 | 4/64 |
| Soal teori / concept | 160/620 · 48/192 | 40 · 12 |
| Spesifikasi lab / mini-project | 24/96 · 4/16 | 6 · 1 |
| Jam nominal | 32/128 | 8/128 |

W2–W4: diproduksi dan dikoreksi; menunggu re-review independen dan
penerimaan owner. W5–W16: NOT STARTED / NOT AUTHORIZED. Skor maksimum,
durasi, dan XP tidak berubah (305 XP/modul; 915 untuk W2–W4).

PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10: NOT AUTHORIZED ·
D-11: DEFERRED · PY:F-01–F-15 NOT VERIFIED · CT-1–CT-12 NOT VERIFIED.

## 22. Pembaruan status — koreksi terarah putaran 2 (PR #27, F-28–F-72) (2026-11-24)

Delta review PR #27 (head `145bb5693320c322eda4d7ea0d08b0a284018c9e`) =
**REQUEST CHANGES**. Register diperluas menjadi 45 ID (F-28–F-72). Deskripsi
F-55, F-56, F-57, F-59 dipulihkan owner; catatan BLOCKED di §21 kini
historis. Disposisi per ID: `review.md` W2/W3/W4.

Tidak ada perubahan status butir: COMPLETE 32 · OPEN 4 · BLOCKED 12 ·
DEFERRED 3 · NOT VERIFIED 5 = **56**; jalur P 32/43; UW-26 dan UW-37 OPEN.
Kurikulum: diproduksi 4/16 modul (16/64 komponen); diterima owner W1 saja
(4/64). W2–W4 menunggu re-review independen dan penerimaan owner; W5–W16
NOT STARTED / NOT AUTHORIZED.

PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10: NOT AUTHORIZED ·
D-11: DEFERRED · PY:F-01–F-15 NOT VERIFIED · CT-1–CT-12 NOT VERIFIED.

## 23. Pembaruan status — merge PR #27, W02-ACC–W04-ACC, CB-2 (W5–W8) (2026-11-24)

PR #27 di-merge pada head `1a58338bcc863320ff4eafbb0f407cee4b2a9f59`
(merge commit `846051f66ee4d1e36e9b34e0c9d1787fb713617b`) atas otorisasi
eksplisit owner. Owner menerima W2–W4 (W02-ACC–W04-ACC) berdasarkan review
independen "PASS — targeted delta review with disclosed limitations";
penerimaan ini **bukan** verifikasi menyeluruh. Owner mengotorisasi CB-2
(W5–W8).

### 23.1 Perubahan per butir

| ID | Sebelum | Sesudah | AC | Bukti |
|---|---|---|---|---|
| UW-37 | OPEN | OPEN (tidak berubah) | CUR:CC-01–CC-11 untuk 64 komponen + penerimaan | Diproduksi 32/64 (W1–W8); diterima owner 16/64 (W1–W4); W5–W8 belum direview independen; W9–W16 belum diproduksi. **Tidak** COMPLETE |
| UW-26 | OPEN | OPEN (tidak berubah) | Rubrik/bank concept per modul (16 modul) | Bank concept W1–W8 ada (8/16 modul, 96/192 soal); 8 modul belum |
| Lainnya | — | Tidak berubah | — | CB-2 hanya konten kurikulum + metadata penerimaan + dokumen status |

### 23.2 Jumlah per status (56 butir)

COMPLETE 32 · OPEN 4 (UW-12, UW-26, UW-37, UW-52) · BLOCKED 12 ·
DEFERRED 3 · NOT VERIFIED 5 = **56** (tidak berubah dari §22). Jalur P
32/43 (74,4%); register 32/56 (57,1%).

### 23.3 Kurikulum (dilaporkan terpisah: produksi, review, penerimaan)

| Ukuran | Diproduksi | Review independen | Diterima owner |
|---|---|---|---|
| Modul | 8/16 (W1–W8) | 4/16 (W1–W4, terbatas) | 4/16 (W1–W4) |
| Komponen penilaian | **32/64** (50%) | 16/64 | **16/64** (25%) |
| Soal teori | 320/620 | 160 | 160 |
| Soal concept | 96/192 | 48 | 48 |
| Spesifikasi lab | 48/96 | 24 | 24 |
| Mini-project | 8/16 | 4 | 4 |

W9–W16: NOT STARTED / NOT AUTHORIZED. Format editor flowchart (M-10) dan
bentuk entri ekspresi Boolean tetap OPEN untuk owner; W6/W8 memakai bentuk
jawaban terstruktur di bawah EB-4 (D-24).

PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10: NOT AUTHORIZED ·
D-11: DEFERRED · PY:F-01–F-15 NOT VERIFIED · CT-1–CT-12 NOT VERIFIED.

## 24. Pembaruan status — D-39 dan koreksi PR #28 putaran 3–4 (2026-11-25)

Owner menyetujui D-39 (HYBRID COMPETENCY COVERAGE). Audit cakupan W1–W8 dan
koreksi terarah tercatat di
[CURRICULUM_COVERAGE_MATRIX_W01_W08.md](CURRICULUM_COVERAGE_MATRIX_W01_W08.md).
Tidak ada perubahan status butir: COMPLETE 32 · OPEN 4 · BLOCKED 12 ·
DEFERRED 3 · NOT VERIFIED 5 = **56**; jalur P 32/43; UW-26 dan UW-37 OPEN.
Kurikulum: diproduksi 8/16 modul (32/64 komponen); diterima owner 4/16
(16/64) **secara historis** — 21 varian W1–W4 (14 sebelum putaran 6; 16 sebelum putaran 7; 20 sebelum putaran 8) yang direvisi setelah
penerimaan berstatus PENDING (TPL-01a). W9–W16 NOT STARTED / NOT AUTHORIZED.

PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10: NOT AUTHORIZED ·
D-11: DEFERRED.

**Putaran 5 (review `796043c`)**: cakupan = **hasil penulis** 153 PASS, 3 OPEN (bukti semantik lemah: W3 peran router/switch, W4 OTP), 0 GAP; kesetaraan varian 43 PASS, 5 OPEN (W3 s03, W4 s01, s03, W7 s02, s03); usulan koreksi menunggu otorisasi owner (matriks §7). PR28-06 tetap OPEN. Status butir audit dan angka kurikulum tidak berubah (32/4/12/3/5 = 56; P 32/43; 8/16 dan 32/64 diproduksi; 4/16 dan 16/64 diterima historis; 14 varian W1–W4 PENDING).

**Putaran 6 (koreksi terarah, otorisasi owner terbatas)**: diterapkan hanya W3 concept s03 vB, W4 concept s03 vB, W7 concept s02 vB, W7 concept s03 vB (versi 2.0; posisi kunci tetap). Cakupan = **hasil penulis** 153 PASS, 3 OPEN (W3 router/switch, W4 OTP — usulan §7 tidak diotorisasi), 0 GAP; kesetaraan 47 PASS, 1 OPEN (W4 concept s01). R5-01 elemen bernilai tepat, R5-04 NB-5 konten cacat, R5-05 field slot bersama di validator penerimaan; 16 varian W1–W4 PENDING. CB-2 belum diterima; PR28-06 tetap OPEN.

**Putaran 7 (koreksi konsolidasi, otorisasi owner bersyarat)**: direvisi W3 concept s01 vA/vB, W4 concept s01 vA, W4 teori s10 vA (versi 2.0; kunci tetap); 4 revisi putaran 6 tidak diubah. Cakupan = **hasil penulis** 156 PASS, 0 OPEN, 0 GAP; kesetaraan 48 PASS, 0 OPEN — belum diverifikasi independen. R6-01 jangkar baseline penerimaan tepercaya, R6-02 identitas lokasi varian, R6-03 integritas kunci, R6-04 kombinasi afiks NB-5, R6-05 pemindai NB-5 tahan konten cacat, R6-06 akurasi dokumentasi; VA-2/R3-04 CONDITIONAL PASS (pencatatan atomik varian semua slot belum dinyatakan eksplisit; SB-12/OD-9). 20 varian W1–W4 PENDING. CB-2 belum diterima; PR28-06 tetap OPEN.

**Putaran 8 (koreksi terarah final, otorisasi owner O-1/O-2)**: hanya stem W4 teori s10 vA (3.0) dan vB (2.0) diubah; kontrak desain atomik VA-4a dicatat (CCD §B.2, DECISIONS_LOG); R7-02 pemindai NB-5 mengenali konsumen dari deklarasi normalization. Cakupan 156/0/0 dan kesetaraan 48/0 (hasil penulis); R3-04 CONDITIONAL PASS (implementasi dan OD-9/UW-33 tertunda). 21 varian W1–W4 PENDING. CB-2 belum diterima; PR28-06 tetap OPEN.
