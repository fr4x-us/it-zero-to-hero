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
| Presisi angka penilaian (UW-22, menunggu owner) | [`docs/NUMERIC_PRECISION_DECISION_SHEET.md`](docs/NUMERIC_PRECISION_DECISION_SHEET.md) |
| Backup (Batch 06) | [`docs/ENCRYPTED_BACKUP_RESTORE_SPEC.md`](docs/ENCRYPTED_BACKUP_RESTORE_SPEC.md) |
| Kalender Jepang (Batch 07) | [`docs/JAPAN_CALENDAR_HOLIDAY_SPEC.md`](docs/JAPAN_CALENDAR_HOLIDAY_SPEC.md) |
| UI dan aksesibilitas (Batch 08) | [`docs/UI_ACCESSIBILITY_VISUAL_SPEC.md`](docs/UI_ACCESSIBILITY_VISUAL_SPEC.md) |
| Kurikulum dan lab (Batch 09) | [`docs/CURRICULUM_OFFLINE_LAB_SPEC.md`](docs/CURRICULUM_OFFLINE_LAB_SPEC.md) |
| Readiness review (Batch 10) | [`docs/FINAL_PLANNING_READINESS_REVIEW.md`](docs/FINAL_PLANNING_READINESS_REVIEW.md) |
| Quality gates | [`docs/QUALITY_GATES.md`](docs/QUALITY_GATES.md) |
| Lingkungan dan rencana CI | [`docs/ENVIRONMENT.md`](docs/ENVIRONMENT.md) |
| Riwayat perencanaan (snapshot) | [`docs/PLANNING_HISTORY.md`](docs/PLANNING_HISTORY.md) |

## Cara berkontribusi

Satu batch = satu branch = satu Pull Request ke `main`, memakai
[template PR](.github/pull_request_template.md). PR tidak pernah di-merge
otomatis; merge hanya setelah persetujuan eksplisit per PR
([`docs/GITHUB_BRIDGE.md`](docs/GITHUB_BRIDGE.md) §5).
