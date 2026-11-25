# IT ZERO → HERO — Handoff State

Checkpoint ringkas antarbatch (lihat [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md)).
Hanya berisi fakta yang dapat dicek di repositori atau GitHub. Diperbarui
di setiap PR batch.

## Status proyek

| Item | Nilai | Sumber |
|---|---|---|
| Tahap | PERSIAPAN; implementasi **belum diizinkan** | [`CLAUDE.md`](../CLAUDE.md), [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) |
| `main` saat checkpoint ditulis | `ab0103e` (merge PR #26) | `git log` |
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
| #25 | Pencatatan D-26–D-37; CB-0; konten W1; revisi kualitas W1 (F-01–F-23) | Merged 2026-11-24 sebagai `df76c5f` (head `f4cb173`; di-merge Claude atas otorisasi eksplisit owner) |
| #26 | CB-0.5: D-38, W01-ACC, empat skill agen, PROJECT_MAP, protokol efisiensi token; revisi F-24–F-27 (hardening keamanan) | Merged 2026-11-24 sebagai `ab0103e` (head `691ae87`; di-merge Claude atas otorisasi eksplisit owner, master prompt CB-1) |
| #27 | CB-1: V03 PASS; kurikulum W2–W4 (12 komponen); dua putaran koreksi F-28–F-72 | Merged 2026-11-24 sebagai `846051f` (head `1a58338`; di-merge Claude atas otorisasi eksplisit owner, master prompt CB-2) |
| #28 | CB-2: penerimaan W02-ACC–W04-ACC; kurikulum W5–W8 (16 komponen) | OPEN — review independen REQUEST CHANGES (SHA `ca73981`) → dikoreksi (PR28-01–PR28-12) → menunggu review delta independen; **tidak di-merge Claude** (base `main` = `846051f`, branch `planning/cb2-w05-w08`) |

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
| D-26–D-35 | OWNER APPROVED (2026-11-24); UW-26/UW-37 OPEN: W1–W4 diterima, W5–W8 menunggu review/penerimaan, W9–W16 belum diproduksi |
| D-36–D-37 | OWNER APPROVED (2026-11-24): HF-A; XV-7–XV-14 + RX-A. UW-33 menunggu OD-5–OD-9, OD-11–OD-14 |
| D-38, W01-ACC | OWNER APPROVED / ACCEPTED (2026-11-24): angka LX-2 = keluaran UW-12 (V); UW-36 COMPLETE. W1 = modul acuan (batas review independen diungkapkan) |
| CB-0.5 | AUTHORIZED (2026-11-24): tepat empat skill; skill lain ON HOLD. **Diterima owner** (master prompt CB-1) dengan V03 saat itu NOT VERIFIED; V03 kemudian **PASS** di sesi baru |
| CB-1 | **AUTHORIZED** (2026-11-24): produksi W2–W4 setelah V03 PASS; satu PR baru; tanpa merge otomatis; W5–W16 dan implementasi tidak diizinkan |
| D-11 | **DEFERRED; IMPLEMENTATION NOT AUTHORIZED** |
| PLANNING CLEAR | **NO** |
| IMPLEMENTATION VERIFIED | **NO** |
| Python PY:F-01–F-15 | **NOT VERIFIED** |

Rincian: [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md),
[DECISIONS_LOG.md](DECISIONS_LOG.md) §Keputusan owner.

## Tugas terakhir

CB-2 (2026-11-24): PR #27 di-merge (`846051f`); W02-ACC–W04-ACC dicatat;
W5–W8 diproduksi (PR #28); review independen REQUEST CHANGES dua kali →
koreksi putaran 1 (PR28-01–PR28-12) dan putaran 2 (PR28-07, PR28-08,
PR28-11, PR28-12). Kurikulum diproduksi 8/16 modul (32/64 komponen),
diterima 4/16 (16/64). Audit 32/4/12/3/5 = 56; jalur P 32/43; UW-26 dan
UW-37 OPEN. PR #28 menunggu review delta; tidak di-merge.

*Historis (CB-1):*

CB-1 (2026-11-24): Fase A — PR #26 di-merge (`ab0103e`, head `691ae87`),
diverifikasi ulang di sesi baru. Fase B — V03 **PASS**: keempat skill
ditemukan dan dimuat di sesi baru `session_011Df1V7VYFZ1Fdwc9jRg7nK`
([CB05_VALIDATION_REPORT.md](CB05_VALIDATION_REPORT.md) §4). Fase D — W2
(OS & berkas), W3 (jaringan), W4 (keamanan siber) diproduksi di
`curriculum/mod-w02/`–`mod-w04/` dengan `review.md` masing-masing.
Audit §20: 32 COMPLETE, 4 OPEN, 12 BLOCKED, 3 DEFERRED, 5 NOT VERIFIED;
jalur P 32/43. Kurikulum diproduksi 16/64, diterima 4/64. Satu PR CB-1
dibuka untuk review independen; tidak di-merge.

## Checkpoint aktif (persisten; dibaca pertama saat memulai ulang sesi)

Kontrak field: [AGENT_TOKEN_EFFICIENCY_PROTOCOL.md](AGENT_TOKEN_EFFICIENCY_PROTOCOL.md) §3.

| Field | Nilai |
|---|---|
| Tugas aktif dan lingkup | Koreksi PR #28 (CB-2) atas REQUEST CHANGES: kunci F4 W8, kontrak NB-5/BN-6/BX/B01, kebocoran K4, akurasi akademik, sinkronisasi status; tanpa merge, tanpa W9, tanpa implementasi |
| Fase | CB-2 diproduksi (PR #28); review independen REQUEST CHANGES; koreksi diterapkan dan divalidasi → PR #28 diperbarui → STOP |
| Selesai | PR #27 merged (`846051f66ee4d1e36e9b34e0c9d1787fb713617b`); W02-ACC, W03-ACC, W04-ACC dicatat (DECISIONS_LOG, OWNER_DECISION_CHECKLIST, module.yaml, review.md); **W5** `curriculum/mod-w05/` (42 berkas; validator NO ERRORS; 13/13 contoh proyek; NB-5 58 butir angka; kunci a6 b6 c7 d6); **W6** `curriculum/mod-w06/` (42 berkas; validator NO ERRORS; 16/16 contoh proyek; 24 butir biner + 22 butir Boolean dihitung ulang dari teks soal; kunci a6 b7 c8 d6); **W7** `curriculum/mod-w07/` (42 berkas; validator NO ERRORS; 16/16 contoh proyek; urutan valid dienumerasi; kunci a7 b7 c9 d8); **W8** `curriculum/mod-w08/` (42 berkas; validator NO ERRORS; 17/17 contoh proyek; 256 kombinasi blok dienumerasi → 2 benar; kunci a8 b7 c7 d7); review W6 dikoreksi (hitungan asersi 64/18) |
| Sisa | Review delta independen PR #28; keputusan owner: cakupan `required_concepts` (PR28-06), M-10/entri Boolean; ledger F-73–F-94 asli tidak tersedia (ID sementara PR28-nn) |
| Berkas relevan | `docs/CURRICULUM_TEMPLATES_CB0.md`, `docs/CURRICULUM_CONTENT_DECISION_SHEETS.md` §D (HA-A fase 2: M 150 · U 45 · L 120 · P 90 · C 30 · R 45), `docs/PROJECT_RUBRIC_DECISION_SHEETS.md` A.3, `docs/ASSESSMENT_FLOW_DECISION_SHEETS.md` A.4, `curriculum/mod-w01`–`mod-w04` (acuan) |
| Versi kerja | Branch `planning/cb2-w05-w08` dari `main` = `846051f66ee4d1e36e9b34e0c9d1787fb713617b`; versi terkini = head branch di GitHub |
| Keputusan | Owner: merge PR #27, W02-ACC–W04-ACC (batas review terarah diungkapkan), CB-2 diotorisasi. LO rinci W5–W8 disusun penyusun dari CUR §2 (CU-1 PROPOSED) |
| Blocker | Format editor flowchart (M-10) dan bentuk entri ekspresi Boolean belum diputuskan → W6/W8 memakai bentuk jawaban terstruktur yang sudah ada (pilihan, isian eksak, tabel), tanpa editor graf; dicatat untuk owner |
| Pendekatan gagal | W5: asersi generator salah tulis (bukan kunci); regex pemeriksa NB-5 awalnya mengurai `18.8` sebagai 18 + satuan — diperbaiki sebelum dipakai sebagai bukti. W6: salah sambung templat module.yaml (YAML rusak, tertangkap validator); restart worker 1 (dilanjutkan dari berkas) |
| Bukti verifikasi | PR #27 `merged: true`, merge commit `846051f`; main lokal = remote, working tree bersih sebelum branch dibuat |
| Aksi berikutnya yang diizinkan | Tidak ada tanpa instruksi owner; menunggu review delta |
| Kondisi berhenti | PR #28 diperbarui dengan laporan koreksi → STOP. Jangan merge, jangan tandai CB-2 diterima, jangan mulai W9, jangan implementasi |

## Blocker

Dikelompokkan menurut siapa yang dapat membukanya. Nomor `B-n`
dipertahankan agar rujukan lama tetap valid.

### Keputusan owner (sisa)

| # | Blocker | Register |
|---|---|---|
| B-10 | Penilaian: kebijakan diputuskan (D-04, D-12, D-13, D-23–D-38); sisa: rubrik concept — W1–W4 diproduksi dan diterima owner; W5–W8 diproduksi, menunggu review independen dan penerimaan owner (PR #28); W9–W16 NOT STARTED / NOT AUTHORIZED (UW-26 OPEN); OP-6 jam (UW-28). | UW-26, UW-28 |
| B-11 | Backup: D-03, D-07, D-16, D-17 **diputuskan**; sisa OD-5–OD-9 dan retensi log restore (UW-33); verifikasi kripto (UW-15, jalur V). | UW-33 |
| B-13 | UI: palet (D-01 M-17), kontras (D-14), tema (D-15) **diputuskan**; sisa: tipografi/aset/breakpoint/alat screenshot (UO-3–UO-9). | UW-35 |
| B-14 | Kurikulum: kebijakan CU lengkap (UW-36 COMPLETE, D-38); W1–W4 diterima (W01-ACC–W04-ACC); W5–W8 diproduksi (CB-2), menunggu review independen/penerimaan; W9–W16 NOT STARTED / NOT AUTHORIZED; format editor flowchart (M-10) dan entri ekspresi Boolean OPEN; lab minggu 9–12 bergantung O-04. | UW-21, UW-37 |
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

1. Review delta independen PR #28 (CB-2, koreksi REQUEST CHANGES) →
   revisi bila ada temuan → otorisasi merge eksplisit bila PASS.
2. Penerimaan owner W5–W8 (terpisah dari merge); W1–W4 sudah diterima.
3. Produksi W9–W16 belum diizinkan; butuh otorisasi terpisah.
4. Implementasi, prototipe, pengukuran, dan benchmark tetap tidak diizinkan.
