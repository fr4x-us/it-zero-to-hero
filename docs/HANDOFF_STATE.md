# IT ZERO → HERO — Handoff State

Checkpoint ringkas antarbatch (lihat [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md)).
Hanya berisi fakta yang dapat dicek di repositori atau GitHub. Diperbarui
di setiap PR batch.

## Status proyek

| Item | Nilai | Sumber |
|---|---|---|
| Tahap | PERSIAPAN; implementasi **belum diizinkan** | [`CLAUDE.md`](../CLAUDE.md), [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) |
| `main` saat checkpoint ditulis | `5931ece` (merge PR #16) | `git log` |
| Kode aplikasi / proyek Gradle / workflow CI / APK | Tidak ada | isi repositori |
| Build atau test Android pernah dijalankan | **Belum pernah** | [QUALITY_GATES.md](QUALITY_GATES.md) EV-1 |

## Riwayat PR

| PR | Isi | Status |
|---|---|---|
| #1 | Lima skill Android pihak ketiga | Merged |
| #2 | [ENVIRONMENT.md](ENVIRONMENT.md) — audit lingkungan + rencana CI | Merged |
| #3 | [QUALITY_GATES.md](QUALITY_GATES.md) | Merged |
| #4 | [PLANNING_HISTORY.md](PLANNING_HISTORY.md) | Merged |
| #5 | [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) (upload owner) | Merged |
| #6 | GitHub Bridge V1: [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md), template Issue/PR, handoff, [DECISIONS_LOG.md](DECISIONS_LOG.md) | Merged |
| #7 | [TECHNICAL_DECISIONS_BATCH_02.md](TECHNICAL_DECISIONS_BATCH_02.md) + pembaruan log keputusan dan handoff | Merged |
| #8 | [PYTHON_OFFLINE_FEASIBILITY_PLAN.md](PYTHON_OFFLINE_FEASIBILITY_PLAN.md) (Batch 03) | Merged |
| #9 | [ANDROID_TOOLCHAIN_DECISION_SHEET.md](ANDROID_TOOLCHAIN_DECISION_SHEET.md) (Batch 04) | Merged |
| #10 | [ASSESSMENT_STATE_MACHINE_SPEC.md](ASSESSMENT_STATE_MACHINE_SPEC.md) (Batch 05) | Merged |
| #11 | [ENCRYPTED_BACKUP_RESTORE_SPEC.md](ENCRYPTED_BACKUP_RESTORE_SPEC.md) (Batch 06) | Merged |
| #12 | [JAPAN_CALENDAR_HOLIDAY_SPEC.md](JAPAN_CALENDAR_HOLIDAY_SPEC.md) (Batch 07) | Merged 2026-11-23 sebagai `8fe5f5c` (di-merge Claude atas instruksi owner setelah review ChatGPT PASS) |
| #13 | [UI_ACCESSIBILITY_VISUAL_SPEC.md](UI_ACCESSIBILITY_VISUAL_SPEC.md) (Batch 08) | Merged 2026-11-23 sebagai `ec74570` (di-merge Claude atas instruksi owner setelah review ChatGPT PASS) |
| #14 | [CURRICULUM_OFFLINE_LAB_SPEC.md](CURRICULUM_OFFLINE_LAB_SPEC.md) (Batch 09) | Merged 2026-11-23 sebagai `caa9d8a` (di-merge Claude atas persetujuan eksplisit owner) |
| #15 | [FINAL_PLANNING_READINESS_REVIEW.md](FINAL_PLANNING_READINESS_REVIEW.md), aturan NO AUTO-MERGE (Batch 10) | Merged oleh owner 2026-11-23 sebagai `9804a05` |
| #16 | [BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) (audit Batch 01–10) | Merged 2026-11-23 sebagai `5931ece` (di-merge Claude atas persetujuan eksplisit owner) |
| PR Cleanup | Cleanup UW-44/46–51 + [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) | Terbuka, menunggu review; **tidak di-merge Claude** |

## Aturan merge (permanen)

Claude **tidak pernah auto-merge**. Merge hanya setelah pesan baru
pengguna menyebut "PR #X telah direview ChatGPT dan disetujui untuk
merge." untuk PR itu saja ([GITHUB_BRIDGE.md](GITHUB_BRIDGE.md) §5).

## Tugas terakhir

Audit cleanup + owner decision preparation: UW-46, UW-47, UW-48, UW-49,
UW-50, UW-51 COMPLETE; UW-44 PARTIAL (aturan rujukan, ID lama tidak
diganti); UW-43 dan UW-45 tetap BLOCKED (butuh owner).
[OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) memuat D-01–D-11
(UW-01–UW-11), semuanya AWAITING OWNER. **PLANNING CLEAR: NO.** Status: PR
terbuka, menunggu review.

## Blocker

Dikelompokkan menurut siapa yang dapat membukanya (UW-49). Nomor `B-n`
dipertahankan agar rujukan lama tetap valid. Daftar keputusan P0:
[OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md).

### Keputusan owner

| # | Blocker | Checklist / register |
|---|---|---|
| B-3 | `PLANNING_COMPLETION_BATCH.md` di-merge tetapi header masih *DRAFT FOR OWNER REVIEW*; §6 belum dicentang. | D-01 / UW-01 |
| B-7 | DataStore disebut baseline di TD:26 tetapi tidak ada di blueprint (DECISIONS_LOG K-1). | D-02 / UW-05 |
| B-9 | minSdk 24 hanya usulan; terkait M-19, O-04 (Chaquopy ≥ 24), O-06 (PBKDF2-SHA256 API 26+). | D-05 / UW-04 |
| B-10 | Penilaian: agregasi, basis lulus, representasi angka, rubrik, durasi, identitas XP, unlock (OP-1–OP-12). | D-04 / UW-11, UW-22, UW-26–UW-32 |
| B-11 | Backup: risiko pemalsuan oleh pemilik kata sandi (OD-2); konflik mode restore (OD-3); Auto Backup default aktif (OD-4). | D-03, D-07 / UW-09, UW-06, UW-16 |
| B-13 | UI: kontras palet; dark mode; tipografi/aset/breakpoint/alat screenshot (UO-1–UO-10). | UW-17–UW-19, UW-35 |
| B-14 | Kurikulum: garis besar hanya RECOVERED; konten belum ada; lab minggu 9–12 bergantung O-04; CU-1–CU-11. | UW-20, UW-21, UW-25, UW-36, UW-37 |
| B-4 | `PLANNING_COMPLETION_BATCH.md` di root; Batch 02 merujuk `docs/`. | UW-43 |
| B-5 | O-01, O-02, O-04, O-06–O-11, O-16 masih OPEN. | D-06, D-08, D-09, D-10 / UW-03, UW-07, UW-08, UW-10, UW-24, UW-38 |

### Izin

| # | Blocker | Checklist / register |
|---|---|---|
| B-1 | Implementasi belum diizinkan. | D-11 / UW-02 |
| (B-5) | Prototipe kelayakan O-04 butuh izin dan batas uji. | D-10 / UW-10 |

### Verifikasi sumber eksternal / lingkungan

| # | Blocker | Register |
|---|---|---|
| B-12 | Sumber resmi hari libur Jepang (Kantor Kabinet, e-Gov) diblokir; dataset belum terverifikasi. | UW-14, UW-23, UW-34 |
| B-8 | Host dokumentasi resmi diblokir (`chaquo.com`, `docs.python.org`, `pyodide.org`, `docs.gradle.org`, `github.com`, `dl.google.com`, `rfc-editor.org`, `csrc.nist.gov`, `www8.cao.go.jp`, `laws.e-gov.go.jp`); riset memakai `raw.githubusercontent.com`, `developer.android.com`, `kotlinlang.org`, Maven Central. | UW-53 |
| B-6 | Android SDK tidak tersedia di container cloud; `dl.google.com` 403. Tidak menghalangi (build di GitHub Actions). | UW-39 |

B-2 (sumber Batch 02 belum ada) selesai di PR #7.

## Langkah berikutnya (usulan, menunggu owner)

1. Review PR cleanup (ChatGPT). Jangan lanjut tahap berikutnya sebelum owner
   menyetujui.
2. Owner menjawab [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md),
   dimulai dari D-01 (status Batch 01).
3. Setelah D-01: Claude menyeragamkan label sumber Batch 01 (UW-45).
4. Implementasi dan prototipe tetap menunggu izin eksplisit (D-10, D-11).
