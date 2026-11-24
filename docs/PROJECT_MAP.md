# IT ZERO → HERO — Peta Proyek (navigasi)

**Indeks navigasi, bukan sumber kebijakan.** Bila isi peta ini berbeda dari
dokumen yang dirujuk, dokumen yang dirujuk yang berlaku. Urutan prioritas
sumber ada di §2. Path diperiksa terhadap `git ls-files` (CB-0.5, 2026-11-24).

## 1. Fase saat ini dan titik masuk

| Item | Nilai | Sumber |
|---|---|---|
| Fase | PERSIAPAN (dokumentasi perencanaan + kurikulum). Implementasi **tidak diizinkan** | [`CLAUDE.md`](../CLAUDE.md) |
| Titik masuk sesi | [`HANDOFF_STATE.md`](HANDOFF_STATE.md) — §Checkpoint aktif | — |
| Gerbang | PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10 NOT AUTHORIZED · D-11 DEFERRED | [`BATCH_01_10_UNFINISHED_AUDIT.md`](BATCH_01_10_UNFINISHED_AUDIT.md) §19 |

## 2. Prioritas sumber (bila bertentangan)

1. Instruksi owner terbaru dalam percakapan (dalam lingkup otorisasi).
2. [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) — keputusan produk terkunci.
3. [`CLAUDE.md`](../CLAUDE.md) dan [`GITHUB_BRIDGE.md`](GITHUB_BRIDGE.md) §5 — aturan kerja dan merge.
4. Keputusan owner: [`DECISIONS_LOG.md`](DECISIONS_LOG.md) ↔ [`OWNER_DECISION_CHECKLIST.md`](OWNER_DECISION_CHECKLIST.md) (kolom "Keputusan final").
5. Spesifikasi dan decision sheet (bagian yang diputuskan).
6. Register audit dan roadmap (status).
7. Dokumen alur kerja agen (peta ini, protokol token, registry skill).
8. Instruksi skill eksternal di `.claude/skills/` — **selalu kalah** dari 1–7 (TE-11).

## 3. Dokumen otoritatif dan tanggung jawabnya

| Dokumen | Tanggung jawab |
|---|---|
| [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) | Produk terkunci (tidak diubah) |
| [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md), [`../PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) | Salinan verbatim historis (tidak diubah) |
| [`DECISIONS_LOG.md`](DECISIONS_LOG.md) | Indeks keputusan D-01–D-38, W01-ACC, otorisasi |
| [`OWNER_DECISION_CHECKLIST.md`](OWNER_DECISION_CHECKLIST.md) | Pertanyaan owner, rekomendasi, keputusan final |
| [`BATCH_01_10_UNFINISHED_AUDIT.md`](BATCH_01_10_UNFINISHED_AUDIT.md) | Register UW-01–UW-56; jumlah status (bagian terakhir = berlaku) |
| [`PLANNING_ROADMAP.md`](PLANNING_ROADMAP.md) | Jalur P/M/G/V, AC per butir, pertanyaan roadmap |
| [`HANDOFF_STATE.md`](HANDOFF_STATE.md) | Riwayat PR, blocker, checkpoint aktif, langkah berikutnya |
| [`GITHUB_BRIDGE.md`](GITHUB_BRIDGE.md) | Siklus PR, NO AUTO-MERGE, kalimat otorisasi |
| [`QUALITY_GATES.md`](QUALITY_GATES.md) | Gerbang mutu dan bukti (EV) |
| [`CROSS_SPEC_CONSISTENCY_REVIEW.md`](CROSS_SPEC_CONSISTENCY_REVIEW.md) | Ketegangan lintas spesifikasi (XS-C*) |
| [`AGENT_SKILL_REGISTRY.md`](AGENT_SKILL_REGISTRY.md) | Skill agen: asal, versi, status aktivasi, rollback |
| [`AGENT_TOKEN_EFFICIENCY_PROTOCOL.md`](AGENT_TOKEN_EFFICIENCY_PROTOCOL.md) | TE-01–TE-14, routing skill, kontrak checkpoint |

## 4. Kurikulum

| Path | Isi |
|---|---|
| [`CURRICULUM_OFFLINE_LAB_SPEC.md`](CURRICULUM_OFFLINE_LAB_SPEC.md) | Spesifikasi kurikulum 16 minggu (CU-1–CU-11) |
| [`CURRICULUM_CONTENT_DECISION_SHEETS.md`](CURRICULUM_CONTENT_DECISION_SHEETS.md) | CU-3, CU-5, CU-7, CU2-O3, CU-11 (D-30–D-32) |
| [`CURRICULUM_TEMPLATES_CB0.md`](CURRICULUM_TEMPLATES_CB0.md) | Standar produksi CB-0: TPL-01–TPL-20, §1a visibilitas, §3a field, §3b QC-01–QC-12 |
| [`CURRICULUM_PRODUCTION_PLAN.md`](CURRICULUM_PRODUCTION_PLAN.md) | Matriks 64 komponen, kemajuan produksi |
| `curriculum/mod-w02/`, `mod-w03/`, `mod-w04/` | W2 OS & berkas, W3 jaringan, W4 keamanan siber (CB-1; diproduksi, **belum** direview/diterima). Struktur sama dengan W1, tanpa `project/evidence/` (enumerasi dicatat di `rubric.yaml` → `solution_analysis`) |
| `curriculum/mod-w01/` | Modul acuan W1 (W01-ACC): `module.yaml`, `lessons/les-01..04.md`, `theory/blueprint.yaml` + `theory/items/s01..s20.yaml`, `concept/items/s01..s06.yaml`, `lab/act-01..03/{spec.md,checks.yaml}`, `project/{spec.md,rubric.yaml,evidence/catalog_enumeration.csv}`, `remedial/remedial.md`, `review.md` |

## 5. Spesifikasi penilaian

| Dokumen | Cakupan |
|---|---|
| [`ASSESSMENT_STATE_MACHINE_SPEC.md`](ASSESSMENT_STATE_MACHINE_SPEC.md) | State attempt, persistensi |
| [`ASSESSMENT_FLOW_DECISION_SHEETS.md`](ASSESSMENT_FLOW_DECISION_SHEETS.md) | Teori, pengumpulan, unlock, remedial, autosave (D-26, D-27) |
| [`CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md`](CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md) | Empat komponen per modul (D-13) |
| [`NUMERIC_PRECISION_DECISION_SHEET.md`](NUMERIC_PRECISION_DECISION_SHEET.md) | Aritmetika integer NP (D-12) |
| [`OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md`](OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md) | Concept (D-23) |
| [`CU6_LAB_SCORING_DECISION_SHEET.md`](CU6_LAB_SCORING_DECISION_SHEET.md) | Lab (D-24, D-35, D-36, D-38) |
| [`PROJECT_RUBRIC_DECISION_SHEETS.md`](PROJECT_RUBRIC_DECISION_SHEETS.md) | Rubrik mini-project MR-A, capstone (D-33) |
| [`CU10_ANSWER_KEY_RISK_DECISION_SHEET.md`](CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) | Kunci jawaban offline (D-34) |
| [`XP_PROGRESS_DECISION_SHEET.md`](XP_PROGRESS_DECISION_SHEET.md) | XP, level, streak, XV-1–XV-14 (D-28, D-29, D-37) |

Spesifikasi lain (bukan penilaian): backup ([`ENCRYPTED_BACKUP_RESTORE_SPEC.md`](ENCRYPTED_BACKUP_RESTORE_SPEC.md),
[`OD1_BACKUP_CRYPTO_DECISION_SHEET.md`](OD1_BACKUP_CRYPTO_DECISION_SHEET.md), [`OD2_BACKUP_INTEGRITY_DECISION_SHEET.md`](OD2_BACKUP_INTEGRITY_DECISION_SHEET.md)),
kalender ([`JAPAN_CALENDAR_HOLIDAY_SPEC.md`](JAPAN_CALENDAR_HOLIDAY_SPEC.md)), UI ([`UI_ACCESSIBILITY_VISUAL_SPEC.md`](UI_ACCESSIBILITY_VISUAL_SPEC.md),
[`ACCESSIBILITY_COLOR_DECISION_SHEET.md`](ACCESSIBILITY_COLOR_DECISION_SHEET.md)), toolchain ([`ANDROID_TOOLCHAIN_DECISION_SHEET.md`](ANDROID_TOOLCHAIN_DECISION_SHEET.md),
[`ENVIRONMENT.md`](ENVIRONMENT.md)), Python offline ([`PYTHON_OFFLINE_FEASIBILITY_PLAN.md`](PYTHON_OFFLINE_FEASIBILITY_PLAN.md)).
Riwayat: [`PLANNING_HISTORY.md`](PLANNING_HISTORY.md), [`FINAL_PLANNING_READINESS_REVIEW.md`](FINAL_PLANNING_READINESS_REVIEW.md),
[`UW43_PATH_CONSISTENCY_DECISION_SHEET.md`](UW43_PATH_CONSISTENCY_DECISION_SHEET.md).

## 6. Alur review dan merge

Batch → satu PR ke `main` → laporan → **STOP** → review ChatGPT → owner
mengirim "PR #X telah direview ChatGPT dan disetujui untuk merge." → Claude
memverifikasi nomor, status, SHA head, `mergeable_state`, checks → merge PR
itu saja ([`GITHUB_BRIDGE.md`](GITHUB_BRIDGE.md) §5). Templat PR:
[`.github/pull_request_template.md`](../.github/pull_request_template.md).

## 7. Rute navigasi per jenis tugas

Kolom: **Awal** = dibaca pertama · **Bersyarat** = hanya bila relevan ·
**Biasanya tidak perlu** · **Perluas bila** · **Keluaran** · **Berhenti bila**.
Semua rute dimulai dari `CLAUDE.md` + peta ini (TE-01).

| ID | Tugas | Awal | Bersyarat | Biasanya tidak perlu | Perluas bila | Keluaran | Berhenti bila |
|---|---|---|---|---|---|---|---|
| R-01 | Pemulihan sesi | `HANDOFF_STATE.md` §Checkpoint aktif; `git status`, `git log -3` | Dokumen di kolom "Berkas relevan" checkpoint | Decision sheet yang tidak disebut checkpoint | Checkpoint tidak cocok dengan `git log`/PR | Melanjutkan dari "Aksi berikutnya" | Aksi berikutnya = "tidak ada"/menunggu owner |
| R-02 | Produksi kurikulum modul (W2–W16; butuh otorisasi) | `CURRICULUM_TEMPLATES_CB0.md`; `CURRICULUM_PRODUCTION_PLAN.md` (baris modul); `curriculum/mod-w01/` (acuan) | `CURRICULUM_OFFLINE_LAB_SPEC.md` (topik minggu); decision sheet komponen | Backup, kalender, UI, toolchain | Modul kode (W9–W12, W16): + `CU6_LAB_SCORING_DECISION_SHEET.md`, `PYTHON_OFFLINE_FEASIBILITY_PLAN.md` | Berkas di `curriculum/mod-wNN/` + `review.md` | Tidak ada otorisasi produksi; konflik dengan keputusan terkunci |
| R-03 | Desain penilaian | Decision sheet komponen (§5); CB-0 §3a/§3b | `NUMERIC_PRECISION_DECISION_SHEET.md`; `ASSESSMENT_STATE_MACHINE_SPEC.md` | Kurikulum modul lain | Perubahan memengaruhi XP/restore | Spesifikasi/butir + bukti maksimum dapat dicapai | Perlu keputusan owner baru |
| R-04 | Spesifikasi lab | `CU6_LAB_SCORING_DECISION_SHEET.md`; CB-0 TPL lab + §1a | `curriculum/mod-w01/lab/` (pola) | Rubrik proyek | Lab kode (runtime NOT VERIFIED) | `spec.md` + `checks.yaml` | Butuh runtime/pengukuran (D-10) |
| R-05 | Rubrik proyek | `PROJECT_RUBRIC_DECISION_SHEETS.md`; CB-0 TPL proyek | `curriculum/mod-w01/project/` (pola) | Lab, teori | Capstone W16 | `spec.md` + `rubric.yaml` (+ bukti enumerasi bila ada) | Rubrik butuh kebijakan baru |
| R-06 | Revisi PR (temuan review) | Temuan review; `git diff main...HEAD --stat`; berkas yang disebut temuan | Dokumen yang terdampak silang | Berkas tak berubah dan tak disebut | Temuan menyentuh angka/maksimum/kontrak → regresi penuh komponen | Revisi di PR yang sama + bukti per temuan | Temuan bertentangan dengan keputusan owner → tanyakan |
| R-07 | Konflik spesifikasi | `CROSS_SPEC_CONSISTENCY_REVIEW.md`; dua dokumen yang bertentangan | `DECISIONS_LOG.md` | Kurikulum | Konflik menyentuh dokumen terkunci | Entri XS-C* + usulan pertanyaan owner | Penyelesaian butuh keputusan owner |
| R-08 | Keputusan owner | `OWNER_DECISION_CHECKLIST.md`; `DECISIONS_LOG.md` | Decision sheet terkait | Konten kurikulum | Keputusan mengubah status UW | Baris keputusan + sinkronisasi (sheet, roadmap, audit, handoff) | Teks owner ambigu → tanyakan; jangan memutuskan sendiri |
| R-09 | Pembaruan audit | `BATCH_01_10_UNFINISHED_AUDIT.md` bagian terakhir; `PLANNING_ROADMAP.md` §2 | AC butir di roadmap | Kurikulum | Jumlah tidak cocok → hitung ulang dari tabel §2 roadmap | Bagian audit baru + jumlah dihitung ulang | AC tidak terpenuhi → jangan tandai COMPLETE |
| R-10 | Handoff | `HANDOFF_STATE.md`; `git log`; PR terbuka | `DECISIONS_LOG.md` | Isi spesifikasi | — | Checkpoint aktif diperbarui (kontrak protokol §3) | Setelah PR dibuka → STOP |

Kondisi yang selalu memicu inspeksi lebih luas: kontradiksi antardokumen,
berkas berubah sejak dibaca, angka/maksimum/jumlah status tidak cocok, atau
instruksi owner yang menyentuh keputusan terkunci.
