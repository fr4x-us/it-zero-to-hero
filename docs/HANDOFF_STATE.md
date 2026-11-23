# IT ZERO → HERO — Handoff State

Checkpoint ringkas antarbatch (lihat [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md)).
Hanya berisi fakta yang dapat dicek di repositori atau GitHub. Diperbarui
di setiap PR batch.

## Status proyek

| Item | Nilai | Sumber |
|---|---|---|
| Tahap | PERSIAPAN; implementasi **belum diizinkan** | [`CLAUDE.md`](../CLAUDE.md), [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) |
| `main` saat checkpoint ditulis | `777f5dc` (merge PR #18) | `git log` |
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
| #17 | Cleanup UW-44/46–51 + [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) | Merged 2026-11-23 sebagai `4eacaa0` (di-merge Claude atas persetujuan eksplisit owner) |
| #18 | Pencatatan persetujuan owner Batch 01 (D-01, M-01–M-19) | Merged 2026-11-23 sebagai `777f5dc` (di-merge Claude atas otorisasi eksplisit owner) |
| PR D-02–D-11 | Pencatatan keputusan owner D-02–D-11 | Terbuka, menunggu review; **tidak di-merge Claude** |

## Aturan merge (permanen)

Claude **tidak pernah auto-merge**. Merge hanya setelah pesan baru
pengguna menyebut "PR #X telah direview ChatGPT dan disetujui untuk
merge." untuk PR itu saja ([GITHUB_BRIDGE.md](GITHUB_BRIDGE.md) §5).

## Status keputusan owner

| ID | Status |
|---|---|
| D-01 | APPROVED (PR #18) |
| D-02–D-09 | OWNER APPROVED (2026-11-23), tunduk pada verifikasi yang tersisa |
| D-10 | PLANNING APPROVED; **EXECUTION NOT AUTHORIZED** |
| D-11 | **DEFERRED; IMPLEMENTATION NOT AUTHORIZED** |
| PLANNING CLEAR | **NO** |
| IMPLEMENTATION VERIFIED | **NO** |
| Python F-01–F-15 | **NOT VERIFIED** |

Rincian: [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md),
[DECISIONS_LOG.md](DECISIONS_LOG.md) §Keputusan owner.

## Tugas terakhir

Pencatatan keputusan owner D-02–D-11 (2026-11-23) di checklist,
DECISIONS_LOG, audit §12, `PLANNING_COMPLETION_BATCH.md` §7.4, dan
spesifikasi terkait (toolchain, backup, Python, penilaian, kurikulum, UI,
kalender, quality gates). minSdk 24 ditandai SUPERSEDED oleh D-05 (29).
D-11 dicatat sebagai DEFERRED. Status: PR terbuka, menunggu review.

## Blocker

Dikelompokkan menurut siapa yang dapat membukanya. Nomor `B-n`
dipertahankan agar rujukan lama tetap valid.

### Keputusan owner (sisa)

| # | Blocker | Register |
|---|---|---|
| B-10 | Penilaian: basis skor terbaik dan kelulusan per modul **diputuskan (D-04)**; sisa: agregasi numerik program, representasi angka, rubrik penjelasan konsep, durasi ujian, identitas XP, aturan unlock rinci, implikasi empat komponen per modul (CU-2). | UW-11, UW-22, UW-26–UW-32, UW-36 |
| B-11 | Backup: mode restore **diputuskan (D-03)**, Auto Backup **diputuskan (D-07)**; sisa: risiko pemalsuan oleh pemilik kata sandi (OD-2), KDF/AEAD (OD-1), OD-5–OD-9. | UW-15, UW-16, UW-33 |
| B-13 | UI: palet **disetujui (D-01 M-17)**; sisa: solusi kontras, dark mode, tipografi/aset/breakpoint/alat screenshot. | UW-17, UW-18, UW-35 |
| B-14 | Kurikulum: kerangka disetujui (D-01 M-02); konten belum ada; lab minggu 9–12 bergantung O-04; CU-2–CU-11. | UW-21, UW-25, UW-36, UW-37 |
| B-4 | `PLANNING_COMPLETION_BATCH.md` di root; Batch 02 merujuk `docs/`. | UW-43 |
| B-5 | O-04, O-06, O-08, O-09, O-10, O-11 masih OPEN (O-01, O-02, O-07, O-16 diputuskan D-06, D-08, D-07, D-09). | UW-15, UW-24, UW-38, UW-39 |

### Izin

| # | Blocker | Register |
|---|---|---|
| B-1 | Implementasi **ditunda** (D-11): selesaikan perencanaan Batch 01–10, PLANNING CLEAR: YES, lalu izin owner baru. | UW-02 |
| (B-5) | Eksekusi prototipe O-04 tidak diizinkan (D-10); ambang sudah disetujui. | UW-10, UW-12 |

### Verifikasi teknis / sumber eksternal / lingkungan

| # | Blocker | Register |
|---|---|---|
| B-15 | Keputusan yang harus diverifikasi saat diizinkan: toolchain D-06 di CI, versi DataStore, transfer antarperangkat dengan `allowBackup=false` (D-07), isolasi jaringan lab Python (D-08, F-09). | UW-13, UW-52, UW-54, UW-55, UW-12 |
| B-12 | Sumber resmi hari libur Jepang diblokir; dataset belum terverifikasi. | UW-14, UW-23, UW-34 |
| B-8 | Host dokumentasi resmi diblokir (`chaquo.com`, `docs.python.org`, `pyodide.org`, `docs.gradle.org`, `github.com`, `dl.google.com`, `rfc-editor.org`, `csrc.nist.gov`, `www8.cao.go.jp`, `laws.e-gov.go.jp`); riset memakai `raw.githubusercontent.com`, `developer.android.com`, `kotlinlang.org`, Maven Central. | UW-53 |
| B-6 | Android SDK tidak tersedia di container cloud. Tidak menghalangi (build di GitHub Actions). | UW-39 |

Selesai: B-2 (PR #7); B-3 (D-01, PR #18); B-7 (D-02); B-9 (D-05). B-7 dan
B-9 berlaku saat PR D-02–D-11 di-merge.

## Langkah berikutnya (usulan, menunggu owner)

1. Review PR D-02–D-11 (ChatGPT) → instruksi merge eksplisit bila PASS.
2. Tugas dokumentasi berikutnya yang direkomendasikan (tanpa coding):
   menyelesaikan butir perencanaan yang dapat dikerjakan Claude —
   UW-45 (penyeragaman label sumber Batch 01) dan lembar opsi untuk UW-22
   (representasi angka) — lalu menyiapkan keputusan owner berikutnya
   (CU-2 implikasi empat komponen per modul, UO-1 kontras, UO-2 dark mode,
   OD-1/OD-2).
3. Implementasi dan prototipe tetap tidak diizinkan (D-10, D-11).
