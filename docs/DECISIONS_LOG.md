# IT ZERO → HERO — Log Sumber Keputusan

Status: PERSIAPAN. Implementasi aplikasi belum diizinkan.

Dokumen ini hanya **menunjuk** ke sumber keputusan per batch. Isi keputusan
tetap berada di dokumen sumbernya. Dokumen ini tidak menambah, mengubah,
atau menggantikan [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) dan
[`CLAUDE.md`](../CLAUDE.md).

| Status sumber | Arti |
|---|---|
| AVAILABLE | Dokumen ada di `main`. |
| PENDING SOURCE | Dokumen disebut owner tetapi belum ada di repositori; isinya tidak boleh dibuat ulang dari ingatan atau dugaan. |

## Daftar batch

| Batch | Dokumen sumber | Status sumber | Status persetujuan | Catatan |
|---|---|---|---|---|
| Baseline | [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md), [`CLAUDE.md`](../CLAUDE.md) | AVAILABLE | LOCKED | Sumber tertinggi. |
| Inventaris | [`PLANNING_HISTORY.md`](PLANNING_HISTORY.md) | AVAILABLE | Di-merge (PR #4) | Snapshot berbasis repo per `260800d`. |
| Batch 01 | [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) | AVAILABLE (di root repo, bukan `docs/`) | **OWNER-APPROVED WITH CONDITIONS** (D-01, 2026-11-23): M-01–M-19 disetujui; detail OPEN/PARTIAL tercatat di §7 dokumen | Matriks §2 historis; §7.1 berlaku. Merge PR #5 sendiri bukan persetujuan. |
| Batch 02 | [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md) | AVAILABLE | OWNER-APPROVED (header dokumen, TD:3) | Disalin tanpa perubahan dari lampiran owner (SHA-256 `0a27420e…a980b`). |

## Keputusan owner D-01–D-35 (2026-11-23 / 2026-11-24)

Sumber: [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) (kolom
"Keputusan final"). Status Batch 02 di bawah tetap dicatat apa adanya;
tabel ini menunjukkan keputusan owner yang lebih baru.

| ID | Status | Ringkasan | Menyelesaikan / memperbarui | Masih OPEN / NOT VERIFIED |
|---|---|---|---|---|
| D-01 | APPROVED (PR #18) | M-01–M-19 disetujui dengan ketentuan | B-3, K-3 | Detail per M (`PLANNING_COMPLETION_BATCH.md` §7.1) |
| D-02 | OWNER APPROVED | DataStore untuk preferensi aplikasi; Room sumber kebenaran data akademik | K-1 / B-7 (DataStore kini keputusan owner, bukan klaim blueprint) | Versi DataStore |
| D-03 | OWNER APPROVED | Restore BKP:M-2 default; BKP:M-1 eksplisit + peringatan + konfirmasi + snapshot pra-restore; tanpa auto-merge | OD-3; konflik BL:63–64 vs B01 M-16 | Retensi snapshot, batas penyimpanan, detail rollback, parameter kripto (OD-1, OD-8) |
| D-04 | OWNER APPROVED | Skor terbaik per komponen; kelulusan per modul (≥ 80 dan tiap komponen ≥ 75, tanpa pembulatan); unlock linear; program = 16 modul lulus + capstone | OP-2; OP-1 sebagian (tingkat modul) | Agregasi numerik tingkat program, representasi angka (OP-3), rubrik capstone (CU-9), implikasi komponen per modul (CU-2) |
| D-05 | OWNER APPROVED | minSdk 29 | B-9, OD-10; usulan 24 dan rekomendasi 26 SUPERSEDED | — |
| D-06 | OWNER APPROVED (provisional) | Baseline toolchain sementara | O-01 (arah) | Cek ulang sebelum scaffold; verifikasi CI setelah izin implementasi; versi DataStore |
| D-07 | OWNER APPROVED | BKP:AB-1: Auto Backup dinonaktifkan | O-07, OD-4 | Perilaku transfer antarperangkat (NOT VERIFIED) |
| D-08 | OWNER APPROVED | `INTERNET` diizinkan untuk fitur opsional; lab Python tanpa jaringan | O-02 | Isolasi jaringan lab (PY:F-09 NOT VERIFIED) |
| D-09 | OWNER APPROVED | JUnit, kotlinx-coroutines-test, Compose UI Test, Robolectric | O-16 (baseline) | Alat screenshot (milestone UI); verifikasi terhadap D-06 |
| D-10 | PLANNING APPROVED; EXECUTION NOT AUTHORIZED | Ambang PY:F-01–F-15 disetujui sebagai rencana | Batas uji O-04 | Izin eksekusi; runtime; PY:F-01–F-15 NOT VERIFIED |
| D-11 | DEFERRED; NOT AUTHORIZED | Implementasi ditunda sampai perencanaan selesai dan izin baru | — | Izin implementasi |
| D-12 | OWNER APPROVED (2026-11-24) | UW-22: NP-4; `max ≤ 10.000`; tie = attempt paling awal; tampilan 2 desimal dibulatkan ke bawah + status eksplisit | UW-22, OP-3 | OP-4, CU-6, alokasi poin; verifikasi implementasi (UW-56) |
| D-13 | OWNER APPROVED (2026-11-24) | CU-2: keempat komponen di semua 16 modul; capstone = mini-project modul 16 dengan rubrik khusus; aktivitas digabung dengan menjumlah poin | CU-2 (bagian UW-36), CU-9 sebagian | Rubrik rinci, alokasi poin dan jam |
| D-14 | OWNER APPROVED (2026-11-24) | UO-1: pasangan kontras sesuai ACC §4; `#000000` untuk teks kecil di atas ungu; turunan aksesibel diizinkan; teks putih di atas ungu hanya teks besar | UO-1 (UW-17) | Verifikasi perangkat (UW-56) |
| D-15 | OWNER APPROVED (2026-11-24) | UO-2: DM-1 tema terang saja, Force Dark otomatis nonaktif; dynamic color nonaktif | UO-2 (UW-18) | Perilaku perangkat NOT VERIFIED (UW-56) |
| D-16 | OWNER APPROVED (2026-11-24), bersyarat verifikasi teknis | OD-1: AES-256-GCM; Argon2id (BC, bersyarat) + cadangan PBKDF2 ≥ 600.000; minimum 19 MiB/t=2/p=1; envelope OD1 §5; H-1–H-7, KV-1–KV-8; restore produksi nonaktif sampai batas maksimum disetujui dan terverifikasi | OD-1 (keputusan) | Parameter final dan batas maksimum lewat pengukuran yang diizinkan; CT-1–CT-12 NOT VERIFIED (UW-15) |
| D-17 | OWNER APPROVED (2026-11-24) | OD-2: I-1 + risiko residual diterima; penanda asal-usul + log restore persisten (informatif); tanpa I-2 dan I-3 di V1; rapor = catatan belajar mandiri | OD-2, UW-16 | Retensi/penyimpanan log restore (UW-33) |
| D-18 | OWNER APPROVED (2026-11-24) | UW-43 Opsi B: file Batch 01 tetap di root; erratum TD:5 | UW-43, K-2 | — |
| D-19 | OWNER APPROVED (2026-11-24) | Tanpa skor numerik/rata-rata/ambang tingkat program; program = 16 modul lulus + capstone memenuhi rubrik | UW-11 | Rubrik capstone (CU-9) |
| D-20 | OWNER APPROVED (2026-11-24) | Klasifikasi P/M/G/V diadopsi; UW-02/UW-10 gerbang setelah PLANNING CLEAR; PLANNING CLEAR tidak mengizinkan implementasi | PL-Q1 | — |
| D-21 | OWNER APPROVED (2026-11-24) | Kurikulum lengkap (64 komponen) wajib sebelum PLANNING CLEAR | PL-Q2 | UW-37 |
| D-22 | OWNER APPROVED (2026-11-24) | UW-21, UW-38, UW-40 ditunda ke milestone; AC tetap; bukan penyelesaian | PL-Q3 | Ketiga butir |
| D-23 | OWNER APPROVED (2026-11-24) | OP-4: CE-B; CE-S1–CE-S5, CE-S3a–S3c; CE-C ditolak; CE-D refleksi tanpa skor; CE-K1–CE-K4; CE-V1–CE-V6; malformed ≠ kegagalan infrastruktur/konten (CE-V7) | OP-4 (OP-4-Q1–Q5) | UW-26 tetap OPEN sampai bank soal 16 modul ada |
| D-24 | OWNER APPROVED (2026-11-24) | CU-6: LW-B, LR-A, RA-1, TB-B (TB-A cadangan bersyarat), EB-1–EB-5, LA-1–LA-4, IE-1–IE-5; 3.000 ms kode pelajar per latihan; D-10 tetap | CU-6 (CU-6-Q1–Q6) | Klarifikasi LX-1–LX-9 (CU-6-Q7–Q12); runtime NOT VERIFIED; UW-36 tetap BLOCKED |
| D-25 | OWNER APPROVED (2026-11-24) | RM-Q1(a–d): UW-15 di jalur V (AC tetap); OD-11–OD-14 di UW-33 bersama OD-5–OD-9; CU2-O3 dan CU2-O4 di UW-36; izin pengukuran kripto = prasyarat UW-15 | RM-Q1 | Tidak ada pengukuran/benchmark/prototipe/implementasi yang diizinkan |
| D-26 | OWNER APPROVED (2026-11-24) | OP-5: TQ-B, TF-1–TF-5, TP-B, 40/40/20, rumus durasi A.4 (10–45 menit), EX-1–EX-13, TA-B (×1,5, maks. 68) + TA-1–TA-4, FB-A, DL-1–DL-9 + SF-A | OP-5-Q1–Q8; UW-27 | OP-6 (UW-28) |
| D-27 | OWNER APPROVED (2026-11-24) | OP-7 SB-A + SB-1–SB-12; OP-9 UL-1–UL-10, PV-A, RV-A; OP-10 RE-A, PI-A; OP-11 AS-B | OP-7-Q1, OP-9-Q1, OP-10-Q1–Q2, OP-11-Q1; UW-29, UW-31, UW-32 | — |
| D-28 | OWNER APPROVED (2026-11-24) | OP-8/CU-4: XI-1–XI-9, XE-B + XE-1–XE-6, UG-A, jumlah XP, level `50·n·(n−1)`, ST-C + SK-1–SK-6, XA-1–XA-3, XL-1–XL-3, milestone | OP-8-Q1–Q7; UW-30 | — |
| D-29 | OWNER APPROVED (2026-11-24) | OD-15: XV-1–XV-6 + RX-A (restore ditolak bila ledger tidak valid) | OD-15-Q1; UW-33 (sebagian) | OD-15-Q2 (XV-7–XV-14); OD-5–OD-9, OD-11–OD-14 |
| D-30 | OWNER APPROVED (2026-11-24) | CU-3 CF-A + UP-A; CU-5 VR-B, MPV-A, VA-1–VA-6; CU2-O5 (6 soal concept, 3 aktivitas lab per modul) | CU-3-Q1–Q2, CU-5-Q1–Q2, CU2-O5-Q1; UW-36 | — |
| D-31 | OWNER APPROVED (2026-11-24) | CU-7: SQ-1–SQ-9, HV-A/HT-1–HT-5, GS-A/GT-1–GT-4 | CU-7-Q1–Q3; UW-36 | Mekanisme eksekusi NOT VERIFIED |
| D-32 | OWNER APPROVED (2026-11-24) | CU2-O3 HA-A (128 jam); CU-11 PB-A revisi | CU2-O3-Q1, CU-11-Q1; UW-36 | — |
| D-33 | OWNER APPROVED (2026-11-24) | CU2-O4 MR-A + MR-1–MR-8; CU-9 tema, deliverable, skema SQL, CR-1–CR-6, MC-1–MC-4, CG-B, CP-1–CP-6 | CU2-O4-Q1–Q2, CU-9-Q1–Q4; UW-36 | — |
| D-34 | OWNER APPROVED (2026-11-24) | CU-10: terima risiko, AK-A | CU-10-Q1–Q2; UW-25 | — |
| D-35 | OWNER APPROVED (2026-11-24) | CU-6 LX-1–LX-9: TB-B utama, TB-A cadangan dengan otorisasi, tanpa klaim kesetaraan | CU-6-Q7–Q12 | Nilai batas agregat (UW-12); CU-6-Q13 umpan balik test tersembunyi |

Status Batch 02 "Tetap OPEN" yang terdampak: O-01 → provisional (D-06);
O-02 → diputuskan (D-08); O-07 → diputuskan (D-07); O-16 → baseline
diputuskan (D-09). O-04, O-06, O-08, O-09, O-10, O-11 tetap OPEN.

## Dokumen batch (spesifikasi, bukan sumber keputusan)

Dokumen berikut menjabarkan kriteria dan usulan. Isinya **bukan**
keputusan kecuali butir yang berlabel APPROVED dengan rujukan ke
blueprint atau Batch 02.

| Batch | Dokumen | PR | Topik OPEN utama |
|---|---|---|---|
| 03 | [PYTHON_OFFLINE_FEASIBILITY_PLAN.md](PYTHON_OFFLINE_FEASIBILITY_PLAN.md) | #8 | O-04 |
| 04 | [ANDROID_TOOLCHAIN_DECISION_SHEET.md](ANDROID_TOOLCHAIN_DECISION_SHEET.md) | #9 | O-01, minSdk |
| 05 | [ASSESSMENT_STATE_MACHINE_SPEC.md](ASSESSMENT_STATE_MACHINE_SPEC.md) | #10 | OP-1–OP-12 |
| 06 | [ENCRYPTED_BACKUP_RESTORE_SPEC.md](ENCRYPTED_BACKUP_RESTORE_SPEC.md) | #11 | OD-1–OD-10 (O-06, O-07); OD-11–OD-14 ditambah di #23 (sisa perencanaan OD-1) |
| 07 | [JAPAN_CALENDAR_HOLIDAY_SPEC.md](JAPAN_CALENDAR_HOLIDAY_SPEC.md) | #12 | CO-1–CO-7 (O-05) |
| 08 | [UI_ACCESSIBILITY_VISUAL_SPEC.md](UI_ACCESSIBILITY_VISUAL_SPEC.md) | #13 | UO-1–UO-10 |
| 09 | [CURRICULUM_OFFLINE_LAB_SPEC.md](CURRICULUM_OFFLINE_LAB_SPEC.md) | #14 | CU-1–CU-11, M-01–M-19 |
| 10 | [FINAL_PLANNING_READINESS_REVIEW.md](FINAL_PLANNING_READINESS_REVIEW.md) | #15 | Ringkasan kesiapan |
| Audit | [BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) | #16 | UW-01–UW-54 |
| Checklist | [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) | #17, #18, #19 | D-01–D-11 (lihat §Keputusan owner) |
| UW-22 | [NUMERIC_PRECISION_DECISION_SHEET.md](NUMERIC_PRECISION_DECISION_SHEET.md) | #20, #21 | OP-3 / UW-22 — diputuskan D-12 |
| CU-2 | [CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md](CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md) | #21 | CU-2 — diputuskan D-13 |
| UO-1/UO-2 | [ACCESSIBILITY_COLOR_DECISION_SHEET.md](ACCESSIBILITY_COLOR_DECISION_SHEET.md) | #21 | UO-1, UO-2 — diputuskan D-14, D-15 |
| OD-1 | [OD1_BACKUP_CRYPTO_DECISION_SHEET.md](OD1_BACKUP_CRYPTO_DECISION_SHEET.md) | #22 | OD-1 — diputuskan D-16 (verifikasi teknis tetap wajib) |
| OD-2 | [OD2_BACKUP_INTEGRITY_DECISION_SHEET.md](OD2_BACKUP_INTEGRITY_DECISION_SHEET.md) | #22 | OD-2 — diputuskan D-17 |
| UW-43 | [UW43_PATH_CONSISTENCY_DECISION_SHEET.md](UW43_PATH_CONSISTENCY_DECISION_SHEET.md) | #22 | UW-43 — diputuskan D-18 |
| OP-4 | [OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md](OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md) | #23 | OP-4 / UW-26 — menunggu owner |
| CU-6 | [CU6_LAB_SCORING_DECISION_SHEET.md](CU6_LAB_SCORING_DECISION_SHEET.md) | #23 | CU-6 (bagian UW-36) — menunggu owner |
| Roadmap | [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) | #23 | Sisa jalur P/M/G/V; RM:RV-1–RV-6; RM-Q1 |
| Kurikulum | [CURRICULUM_PRODUCTION_PLAN.md](CURRICULUM_PRODUCTION_PLAN.md) | #23 | UW-37 (rencana produksi; konten belum dibuat) |
| OP-5, OP-7, OP-9, OP-10, OP-11 | [ASSESSMENT_FLOW_DECISION_SHEETS.md](ASSESSMENT_FLOW_DECISION_SHEETS.md) | #24 | UW-27, UW-29, UW-31, UW-32 — diputuskan D-26, D-27 |
| OP-8, CU-4 | [XP_PROGRESS_DECISION_SHEET.md](XP_PROGRESS_DECISION_SHEET.md) | #24 | UW-30 — diputuskan D-28, D-29; OD-15-Q2 menunggu owner |
| CU-3, CU-5, CU-7, CU2-O3, CU-11 | [CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md) | #24 | UW-36 — diputuskan D-30–D-32 |
| CU2-O4, CU-9 | [PROJECT_RUBRIC_DECISION_SHEETS.md](PROJECT_RUBRIC_DECISION_SHEETS.md) | #24 | UW-36 — diputuskan D-33 |
| CU-10 | [CU10_ANSWER_KEY_RISK_DECISION_SHEET.md](CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) | #24 | UW-25 — diputuskan D-34 |
| Templat CB-0 | [CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md) | #24, #25 | UW-37 — CB-0 dapat dipakai W1–W8; finalisasi global menunggu CU-6-Q13; bukan konten |
| Konten W1 | [curriculum/mod-w01/module.yaml](../curriculum/mod-w01/module.yaml) | #25 | UW-37, UW-26 — W1 diproduksi, belum diterima owner |
| Konsistensi | [CROSS_SPEC_CONSISTENCY_REVIEW.md](CROSS_SPEC_CONSISTENCY_REVIEW.md) | #24 | Pemeriksaan usulan terhadap D-01–D-25 |

## Aturan rujukan lintas dokumen (editorial, UW-44)

Beberapa dokumen memakai ID lokal yang sama (mis. `B-01` kasus batas vs
blocker `B-1`; `M-1` mode restore vs gap `M-01`). ID yang ada **tidak**
diganti. Saat merujuk ID lokal dari dokumen lain, tulis kode dokumennya:

| Kode | Dokumen |
|---|---|
| `BL:n` / `TD:n` | Blueprint / Batch 02 (nomor baris) |
| `B01 M-xx` | Batch 01 |
| `PY:` | Python plan |
| `TC:` | Toolchain sheet |
| `ASM:` | Assessment spec |
| `BKP:` | Backup spec |
| `CAL:` | Calendar spec |
| `UI:` | UI spec |
| `CUR:` | Curriculum spec |
| `HS:B-n` | Blocker di HANDOFF_STATE |
| `FIN:` | FINAL_PLANNING_READINESS_REVIEW (mis. `FIN:C-4`) |
| `AUD:D-xx` | Pemeriksaan konsistensi audit §4 |
| `NUM:` | NUMERIC_PRECISION_DECISION_SHEET |
| `CU2:` | CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET |
| `ACC:` | ACCESSIBILITY_COLOR_DECISION_SHEET |
| `OD1:` / `OD2:` / `UW43:` | Lembar keputusan OD-1, OD-2, UW-43 |
| `OP4:` / `CU6:` / `RM:` / `CPP:` | Lembar OP-4, CU-6, roadmap perencanaan, rencana produksi kurikulum |
| `AF:` / `XP:` / `CCD:` / `RB:` / `CU10:` / `TPL:` / `XS:` / `W01:` | Lembar alur penilaian, XP, konten kurikulum, rubrik proyek, CU-10, templat CB-0, tinjauan konsistensi, konten modul W1 (`curriculum/mod-w01/`) |
| `UW-nn` | Register audit (ID global, unik) |
| `D-01`–`D-35` (tanpa kode) | Keputusan owner (global) — [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) |
| `O-`, `OP-`, `OD-`, `CO-`, `UO-`, `CU-`, `KS-`, gate QG (`AB-`, `OF-`, `GR-`, `LB-`, `CL-`, `SC-`, `AP-`, `EV-`) | ID global unik, tanpa kode. Pengecualian: opsi Auto Backup `AB-1`–`AB-3` di BKP §7 bentrok dengan gate `AB-1`–`AB-8`, sehingga ditulis `BKP:AB-x` |

Contoh: `ASM:B-03` (kasus batas skor), `BKP:M-1` (mode restore),
`HS:B-3` (blocker status Batch 01).

## Batch 02 — Keputusan teknis

Sumber: [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md)
(rujukan `TD:n` = nomor baris). Tabel ini hanya meringkas; bila berbeda,
dokumen sumber yang berlaku. Status **APPROVED** berarti *arah* desain
disetujui, belum tentu setiap detail implementasi (TD:69).

### APPROVED (arah disetujui)

| ID | Area | Keputusan | Masih OPEN di dalamnya | Sumber |
|---|---|---|---|---|
| O-12 | Dependency injection | DI manual untuk V1; Hilt hanya bila kompleksitas menuntut dan didokumentasikan. | — | TD:17 |
| O-13 | Navigasi | Navigation Compose untuk lima tab. | Kompatibilitas library diverifikasi sebelum implementasi. | TD:18 |
| O-14 | Struktur Gradle | Satu modul `app` di V1; dipecah hanya bila ada kebutuhan terbukti. | — | TD:19 |
| O-15 | State UI | UI state immutable + StateFlow; effect sekali jalan eksplisit; koleksi lifecycle-aware. | Detail mekanisme effect. | TD:20 |
| O-03 | Presisi skor | Hitung dengan presisi penuh; pembulatan hanya untuk tampilan, bukan untuk ambang lulus. | Representasi numerik, agregasi, aturan seri. | TD:21, TD:30 |
| O-17 | XP farming | XP diberikan sekali per identitas aktivitas yang sama; pengulangan/remedial tidak memberi XP lagi; tanpa penalti. | Definisi identitas, batas, kasus tepi. | TD:22, TD:38 |
| O-05 | Hari libur Jepang | Dataset hari libur offline + proses pembaruan terkontrol; libur pengganti dan *citizens' holidays*. | Sumber data, rentang tahun, mekanisme pembaruan. | TD:23 |
| CI | Verifikasi build | GitHub Actions sebagai lingkungan build/lint/unit test/APK utama. | Tidak ada workflow sebelum izin implementasi. | TD:24 |
| UI | Desain visual | Colorful Academy, Compose native; lima tab Home, Learn, Lab, Calendar, Progress; palet dan guardrail Batch 01. | Aset, tipografi, target terukur. | TD:25 |
| Arsitektur | Baseline | Kotlin + Compose + M3, Room/SQLite, DataStore, MVVM/Repository, offline-first. | — | TD:26 |

### Tetap OPEN

| ID | Topik | Bukti yang dibutuhkan sebelum dipilih | Sumber |
|---|---|---|---|
| O-04 | Eksekusi Python offline | Kelayakan runtime, packaging offline, isolasi kode, batas memori/waktu, uji perangkat. | TD:45 |
| O-06 | Backup terenkripsi | Threat model, envelope berversi, AEAD, KDF + parameter, uji restore. AES-GCM/Argon2id hanya kandidat. | TD:46 |
| O-01 | Versi toolchain, min/target SDK | Kombinasi kompatibel dari dokumentasi resmi tepat sebelum scaffold pertama. | TD:47 |
| O-07 | Kebijakan backup OS Android | Aturan `allowBackup`/ekstraksi data. | TD:48 |
| O-02 | Video opsional / izin `INTERNET` | Strategi buka eksternal yang aman offline, izin minimal. | TD:49 |
| O-08 | R8/minify, ukuran APK | Profil rilis dan dampak test. | TD:50 |
| O-09 | Infrastruktur emulator/perangkat | Runner yang layak dan tersedia. | TD:51 |
| O-10 | Penandatanganan/distribusi | Manajemen kunci dan kanal rilis. | TD:52 |
| O-11 | Akses SDK di cloud | Opsional; tidak memblokir rencana GitHub Actions. | TD:53 |
| O-16 | Library testing | Stack unit/integrasi/UI/screenshot yang kompatibel. | TD:54 |

Celah rincian M-01–M-19 yang belum terselesaikan tetap mengacu ke matriks
Batch 01 (TD:56).

### Catatan konsistensi

| # | Temuan | Status |
|---|---|---|
| K-1 | Catatan historis: TD:26 menyebut **DataStore** sebagai bagian "existing blueprint baseline", padahal `BLUEPRINT_LOCKED.md` hanya menyebut Room/SQLite (BL:11). DataStore bukan bagian blueprint awal. Owner kemudian menyetujuinya melalui D-02 (2026-11-23) sebagai keputusan baru, khusus untuk preferensi aplikasi; Room/SQLite tetap sumber kebenaran data akademik dan versi DataStore masih OPEN. TD:26 tidak diubah. Blocker terkait: B-7 (HANDOFF_STATE). | Selesai oleh D-02 |
| K-2 | TD:5 merujuk `docs/PLANNING_COMPLETION_BATCH.md`, sedangkan file tersebut berada di root repo. *Koreksi 2026-11-24:* catatan semula juga menyebut TD:68, tetapi TD:68 merujuk `docs/TECHNICAL_DECISIONS_BATCH_02.md`. **Diselesaikan D-18 (Opsi B):** lihat erratum di bawah. | Selesai oleh D-18 |
| K-3 | (Diselesaikan oleh D-01 M-18: nama tab blueprint berlaku.) Batch 01 M-18 memakai label tab "Learning Journey, IT Lab, Schedule/Calendar"; blueprint (BL:69) dan TD:25 memakai "Learn, Lab, Calendar". Blueprint yang berlaku. | Informasi |
| K-4 | ID lokal dipakai ulang antardokumen (mis. `A-xx`, `B-0x`, `F-xx`, `M-1…M-3` vs `M-01…M-19`). Rujukan lintas dokumen harus menyebut nama dokumen. Detail: FINAL_PLANNING_READINESS_REVIEW KS-07. | Informasi |
| K-5 | `QUALITY_GATES.md` GR-10 lebih lama dari TD:21; arah "bulatkan hanya untuk tampilan" sudah APPROVED (TD:21), agregasi/representasi tetap OPEN. | Informasi |

## Erratum (D-18, 2026-11-24)

| ID | Dokumen | Teks asli | Dibaca sebagai | Catatan |
|---|---|---|---|---|
| ER-1 | `docs/TECHNICAL_DECISIONS_BATCH_02.md` baris 5 (TD:5) | `docs/PLANNING_COMPLETION_BATCH.md` | `PLANNING_COMPLETION_BATCH.md` (root repositori) | Dokumen Batch 02 adalah salinan verbatim keputusan owner dan **tidak diubah**. File Batch 01 tidak dipindahkan (D-18 Opsi B) |

