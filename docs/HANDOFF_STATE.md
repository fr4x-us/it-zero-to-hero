# IT ZERO → HERO — Handoff State

Checkpoint ringkas antarbatch (lihat [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md)).
Hanya berisi fakta yang dapat dicek di repositori atau GitHub. Diperbarui
di setiap PR batch.

## Status proyek

| Item | Nilai | Sumber |
|---|---|---|
| Tahap | PERSIAPAN; implementasi **belum diizinkan** | [`CLAUDE.md`](../CLAUDE.md), [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) |
| `main` saat checkpoint ditulis | `40ca205` (merge PR #24) | `git log` |
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
| #19 | Pencatatan keputusan owner D-02–D-11 | Merged 2026-11-23 sebagai `2114ca8` (di-merge Claude atas persetujuan eksplisit owner) |
| #20 | Cleanup UW-45/22/44 (label B01, lembar presisi angka, rujukan ID) | Merged 2026-11-23 sebagai `6a805a1` (di-merge Claude atas persetujuan eksplisit owner) |
| #21 | Persiapan keputusan UW-22, CU-2, UO-1/UO-2 | Merged 2026-11-24 sebagai `b789e9a` (di-merge Claude atas persetujuan eksplisit owner) |
| #22 | Pencatatan D-12–D-15; lembar OD-1, OD-2, UW-43 | Merged 2026-11-24 sebagai `bcecdae` (di-merge Claude atas persetujuan eksplisit owner) |
| #23 | Pencatatan D-16–D-22; roadmap; lembar OP-4, CU-6; rencana produksi kurikulum; revisi F-01–F-06 | Merged 2026-11-24 sebagai `928e278` (di-merge Claude atas persetujuan eksplisit owner) |
| #24 | Pencatatan D-23–D-25; lembar keputusan kurikulum; templat CB-0; tinjauan konsistensi | Merged 2026-11-24 sebagai `40ca205` (di-merge Claude atas persetujuan eksplisit owner) |
| #25 | Pencatatan D-26–D-35; CB-0; konten W1; revisi kualitas W1 (F-01–F-18) | Terbuka, menunggu review ulang; **tidak di-merge Claude** |

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
| D-12–D-15 | OWNER APPROVED (2026-11-24); verifikasi implementasi NOT VERIFIED (UW-56) |
| D-16 | OWNER APPROVED, bersyarat verifikasi teknis; restore produksi nonaktif sampai batas KDF terverifikasi (UW-15 NOT VERIFIED) |
| D-17–D-22 | OWNER APPROVED (2026-11-24) |
| D-23–D-25 | OWNER APPROVED (2026-11-24); UW-26, UW-36 tetap belum selesai; runtime dan kripto NOT VERIFIED |
| D-26–D-35 | OWNER APPROVED (2026-11-24); UW-36 menunggu CU-6-Q13; UW-26/UW-37 menunggu konten W2–W16 |
| D-11 | **DEFERRED; IMPLEMENTATION NOT AUTHORIZED** |
| PLANNING CLEAR | **NO** |
| IMPLEMENTATION VERIFIED | **NO** |
| Python PY:F-01–F-15 | **NOT VERIFIED** |

Rincian: [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md),
[DECISIONS_LOG.md](DECISIONS_LOG.md) §Keputusan owner.

## Tugas terakhir

Merge PR #24 (`40ca205`). Pencatatan D-26–D-35. CB-0
([CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md)) dapat dipakai
untuk W1–W8; finalisasi global menunggu CU-6-Q13. Revisi review PR #25:
rubrik proyek (F8, jumlah keping, contoh E01–E16), posisi kunci seimbang,
varian setara (matriks), contoh proyek tidak membocorkan jawaban, review per
butir; putaran 2: maksimum lab dapat dicapai, arah konversi, presisi soal,
field kanonik, aturan angka, QC-01–QC-10. Konten W1 lengkap diproduksi di
[curriculum/mod-w01/](../curriculum/mod-w01/module.yaml): 4 pelajaran, 40
soal teori, 6 spesifikasi lab, 1 mini-project, 12 soal concept, remedial,
review mandiri. Audit §18: 31 COMPLETE, 4 OPEN, 13 BLOCKED, 3 DEFERRED, 5
NOT VERIFIED. Jalur P 31/43. Kurikulum diproduksi 4/64, diterima 0/64.
Status: PR terbuka, menunggu review.

## Blocker

Dikelompokkan menurut siapa yang dapat membukanya. Nomor `B-n`
dipertahankan agar rujukan lama tetap valid.

### Keputusan owner (sisa)

| # | Blocker | Register |
|---|---|---|
| B-10 | Penilaian: basis skor terbaik dan kelulusan per modul **diputuskan (D-04)**; sisa: agregasi numerik program, representasi angka, rubrik penjelasan konsep, durasi ujian, identitas XP, aturan unlock rinci, implikasi empat komponen per modul (CU-2). | UW-11, UW-22, UW-26–UW-32, UW-36 |
| B-11 | Backup: D-03, D-07, D-16, D-17 **diputuskan**; sisa OD-5–OD-9 dan retensi log restore (UW-33); verifikasi kripto (UW-15, jalur V). | UW-33 |
| B-13 | UI: palet (D-01 M-17), kontras (D-14), tema (D-15) **diputuskan**; sisa: tipografi/aset/breakpoint/alat screenshot (UO-3–UO-9). | UW-35 |
| B-14 | Kurikulum: kerangka disetujui (D-01 M-02); konten belum ada; lab minggu 9–12 bergantung O-04; CU-2–CU-11. | UW-21, UW-25, UW-36, UW-37 |
| B-5 | O-04, O-06, O-08, O-09, O-10, O-11 masih OPEN (O-01, O-02, O-07, O-16 diputuskan D-06, D-08, D-07, D-09). | UW-15, UW-24, UW-38, UW-39 |

### Izin

| # | Blocker | Register |
|---|---|---|
| B-1 | Implementasi **ditunda** (D-11): selesaikan perencanaan Batch 01–10, PLANNING CLEAR: YES, lalu izin owner baru. | UW-02 |
| (B-5) | Eksekusi prototipe O-04 tidak diizinkan (D-10); ambang sudah disetujui. | UW-10, UW-12 |

### Verifikasi teknis / sumber eksternal / lingkungan

| # | Blocker | Register |
|---|---|---|
| B-15 | Keputusan yang harus diverifikasi saat diizinkan: toolchain D-06 di CI, versi DataStore, transfer antarperangkat dengan `allowBackup=false` (D-07), isolasi jaringan lab Python (D-08, PY:F-09). | UW-13, UW-52, UW-54, UW-55, UW-12 |
| B-12 | Sumber resmi hari libur Jepang diblokir; dataset belum terverifikasi. | UW-14, UW-23, UW-34 |
| B-8 | Host dokumentasi resmi diblokir (`chaquo.com`, `docs.python.org`, `pyodide.org`, `docs.gradle.org`, `github.com`, `dl.google.com`, `rfc-editor.org`, `csrc.nist.gov`, `www8.cao.go.jp`, `laws.e-gov.go.jp`); riset memakai `raw.githubusercontent.com`, `developer.android.com`, `kotlinlang.org`, Maven Central. | UW-53 |
| B-6 | Android SDK tidak tersedia di container cloud. Tidak menghalangi (build di GitHub Actions). | UW-39 |

Selesai: B-2 (PR #7); B-3 (D-01, PR #18); B-7 (D-02, PR #19); B-9 (D-05, PR #19); B-4 (D-18, berlaku saat PR #23 di-merge).

## Langkah berikutnya (usulan, menunggu owner)

1. Review PR batch ini (ChatGPT) → instruksi merge eksplisit bila PASS.
2. Owner menerima W1 sebagai modul acuan (W01-ACC) dan menjawab CU-6-Q13
   serta OD-15-Q2 ([OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md)).
3. Produksi W2 (satu PR per modul), lalu W3, W4
   ([CURRICULUM_PRODUCTION_PLAN.md](CURRICULUM_PRODUCTION_PLAN.md) §6.1).
4. Implementasi, prototipe, pengukuran, dan benchmark tetap tidak diizinkan.
