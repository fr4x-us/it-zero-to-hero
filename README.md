# IT ZERO → HERO

Offline-first Android IT Learning Academy: aplikasi Android native
(Kotlin, Jetpack Compose, Material 3, Room) untuk belajar dasar IT selama
16 minggu, sepenuhnya offline.

> **Status: PERSIAPAN.** Implementasi aplikasi **belum diizinkan**.
> Repositori ini hanya berisi dokumentasi perencanaan, template GitHub,
> dan skill Claude Code. Belum ada kode, proyek Gradle, workflow CI, atau
> APK.

## Mulai dari sini

| Urutan | Dokumen | Isi |
|---|---|---|
| 1 | [`CLAUDE.md`](CLAUDE.md) | Aturan proyek dan aturan NO AUTO-MERGE |
| 2 | [`docs/BLUEPRINT_LOCKED.md`](docs/BLUEPRINT_LOCKED.md) | Keputusan produk terkunci (sumber kebenaran) |
| 3 | [`docs/HANDOFF_STATE.md`](docs/HANDOFF_STATE.md) | Status terkini, blocker, langkah berikutnya |
| 4 | [`docs/OWNER_DECISION_CHECKLIST.md`](docs/OWNER_DECISION_CHECKLIST.md) | Keputusan P0 yang menunggu owner |
| 5 | [`docs/BATCH_01_10_UNFINISHED_AUDIT.md`](docs/BATCH_01_10_UNFINISHED_AUDIT.md) | Register pekerjaan belum selesai |
| 5a | [`docs/PLANNING_ROADMAP.md`](docs/PLANNING_ROADMAP.md) | Roadmap perencanaan tersisa (jalur P/M/G/V) |
| 6 | [`docs/DECISIONS_LOG.md`](docs/DECISIONS_LOG.md) | Sumber keputusan per batch dan daftar dokumen batch |
| 7 | [`docs/GITHUB_BRIDGE.md`](docs/GITHUB_BRIDGE.md) | Alur kerja owner, ChatGPT, Claude, dan GitHub |

## Dokumen perencanaan

| Topik | Dokumen |
|---|---|
| Suplemen perencanaan (Batch 01, OWNER-APPROVED WITH CONDITIONS — D-01) | [`PLANNING_COMPLETION_BATCH.md`](PLANNING_COMPLETION_BATCH.md) |
| Keputusan teknis (Batch 02) | [`docs/TECHNICAL_DECISIONS_BATCH_02.md`](docs/TECHNICAL_DECISIONS_BATCH_02.md) |
| Python offline (Batch 03) | [`docs/PYTHON_OFFLINE_FEASIBILITY_PLAN.md`](docs/PYTHON_OFFLINE_FEASIBILITY_PLAN.md) |
| Toolchain (Batch 04) | [`docs/ANDROID_TOOLCHAIN_DECISION_SHEET.md`](docs/ANDROID_TOOLCHAIN_DECISION_SHEET.md) |
| Penilaian (Batch 05) | [`docs/ASSESSMENT_STATE_MACHINE_SPEC.md`](docs/ASSESSMENT_STATE_MACHINE_SPEC.md) |
| Presisi angka penilaian (UW-22, diputuskan D-12) | [`docs/NUMERIC_PRECISION_DECISION_SHEET.md`](docs/NUMERIC_PRECISION_DECISION_SHEET.md) |
| Struktur komponen per modul (CU-2, diputuskan D-13) | [`docs/CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md`](docs/CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md) |
| Kontras palet dan dark mode (UO-1/UO-2, diputuskan D-14/D-15) | [`docs/ACCESSIBILITY_COLOR_DECISION_SHEET.md`](docs/ACCESSIBILITY_COLOR_DECISION_SHEET.md) |
| Kriptografi backup (OD-1, diputuskan D-16; verifikasi NOT VERIFIED) | [`docs/OD1_BACKUP_CRYPTO_DECISION_SHEET.md`](docs/OD1_BACKUP_CRYPTO_DECISION_SHEET.md) |
| Pemalsuan backup dan integritas akademik (OD-2, diputuskan D-17) | [`docs/OD2_BACKUP_INTEGRITY_DECISION_SHEET.md`](docs/OD2_BACKUP_INTEGRITY_DECISION_SHEET.md) |
| Konsistensi path Batch 01 (UW-43, diputuskan D-18) | [`docs/UW43_PATH_CONSISTENCY_DECISION_SHEET.md`](docs/UW43_PATH_CONSISTENCY_DECISION_SHEET.md) |
| Backup (Batch 06) | [`docs/ENCRYPTED_BACKUP_RESTORE_SPEC.md`](docs/ENCRYPTED_BACKUP_RESTORE_SPEC.md) |
| Kalender Jepang (Batch 07) | [`docs/JAPAN_CALENDAR_HOLIDAY_SPEC.md`](docs/JAPAN_CALENDAR_HOLIDAY_SPEC.md) |
| UI dan aksesibilitas (Batch 08) | [`docs/UI_ACCESSIBILITY_VISUAL_SPEC.md`](docs/UI_ACCESSIBILITY_VISUAL_SPEC.md) |
| Kurikulum dan lab (Batch 09) | [`docs/CURRICULUM_OFFLINE_LAB_SPEC.md`](docs/CURRICULUM_OFFLINE_LAB_SPEC.md) |
| Readiness review (Batch 10) | [`docs/FINAL_PLANNING_READINESS_REVIEW.md`](docs/FINAL_PLANNING_READINESS_REVIEW.md) |
| Quality gates | [`docs/QUALITY_GATES.md`](docs/QUALITY_GATES.md) |
| Lingkungan dan rencana CI | [`docs/ENVIRONMENT.md`](docs/ENVIRONMENT.md) |
| Riwayat perencanaan (snapshot) | [`docs/PLANNING_HISTORY.md`](docs/PLANNING_HISTORY.md) |
| Penilaian penjelasan konsep (OP-4, diputuskan D-23) | [`docs/OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md`](docs/OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md) |
| Penilaian lab (CU-6, diputuskan D-24, D-35, D-36) | [`docs/CU6_LAB_SCORING_DECISION_SHEET.md`](docs/CU6_LAB_SCORING_DECISION_SHEET.md) |
| Rencana produksi kurikulum (UW-37) | [`docs/CURRICULUM_PRODUCTION_PLAN.md`](docs/CURRICULUM_PRODUCTION_PLAN.md) |
| Ujian teori, pengumpulan, unlock, remedial, autosave (diputuskan D-26, D-27) | [`docs/ASSESSMENT_FLOW_DECISION_SHEETS.md`](docs/ASSESSMENT_FLOW_DECISION_SHEETS.md) |
| XP, level, streak, validasi restore (diputuskan D-28, D-29, D-37) | [`docs/XP_PROGRESS_DECISION_SHEET.md`](docs/XP_PROGRESS_DECISION_SHEET.md) |
| Format konten, varian, lab SQL/HTML/Git, jam, W9/W10 (diputuskan D-30–D-32) | [`docs/CURRICULUM_CONTENT_DECISION_SHEETS.md`](docs/CURRICULUM_CONTENT_DECISION_SHEETS.md) |
| Rubrik mini-project dan capstone (diputuskan D-33) | [`docs/PROJECT_RUBRIC_DECISION_SHEETS.md`](docs/PROJECT_RUBRIC_DECISION_SHEETS.md) |
| Risiko kunci jawaban offline (diputuskan D-34) | [`docs/CU10_ANSWER_KEY_RISK_DECISION_SHEET.md`](docs/CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) |
| Standar produksi kurikulum CB-0 (kebijakan lengkap; menunggu review dan penerimaan owner) | [`docs/CURRICULUM_TEMPLATES_CB0.md`](docs/CURRICULUM_TEMPLATES_CB0.md) |
| Konten modul W1 (diproduksi, menunggu review) | [`curriculum/mod-w01/`](curriculum/mod-w01/module.yaml) |
| Tinjauan konsistensi lintas spesifikasi | [`docs/CROSS_SPEC_CONSISTENCY_REVIEW.md`](docs/CROSS_SPEC_CONSISTENCY_REVIEW.md) |

## Cara berkontribusi

Satu batch = satu branch = satu Pull Request ke `main`, memakai
[template PR](.github/pull_request_template.md). PR tidak pernah di-merge
otomatis; merge hanya setelah persetujuan eksplisit per PR
([`docs/GITHUB_BRIDGE.md`](docs/GITHUB_BRIDGE.md) §5).
