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

