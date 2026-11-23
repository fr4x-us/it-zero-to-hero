# IT ZERO → HERO — Handoff State

Checkpoint ringkas antarbatch (lihat [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md)).
Hanya berisi fakta yang dapat dicek di repositori atau GitHub. Diperbarui
di setiap PR batch.

## Status proyek

| Item | Nilai | Sumber |
|---|---|---|
| Tahap | PERSIAPAN; implementasi **belum diizinkan** | [`CLAUDE.md`](../CLAUDE.md), [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) |
| `main` saat checkpoint ditulis | `86ee7cb` (merge PR #11) | `git log` |
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
| PR Batch 07 | [JAPAN_CALENDAR_HOLIDAY_SPEC.md](JAPAN_CALENDAR_HOLIDAY_SPEC.md) + handoff | Terbuka, menunggu review owner |

## Tugas terakhir

Batch 07: [JAPAN_CALENDAR_HOLIDAY_SPEC.md](JAPAN_CALENDAR_HOLIDAY_SPEC.md)
— sumber resmi hari libur Jepang, aturan libur pengganti dan *citizens'
holiday*, lapisan hari libur nasional vs kalender kerja, format dan
validasi dataset offline, aturan JST/jam tenang, acceptance criteria
AC-01–AC-08, skenario K-01–K-12, dan keputusan CO-1–CO-7. Sumber resmi
Jepang diblokir, jadi tidak ada tanggal yang ditandai VERIFIED. Status: PR
terbuka, belum di-merge.

## Blocker

| # | Blocker | Butuh |
|---|---|---|
| B-1 | Implementasi belum diizinkan. | Izin eksplisit owner. |
| B-3 | `PLANNING_COMPLETION_BATCH.md` sudah di-merge tetapi header-nya masih *DRAFT FOR OWNER REVIEW* dan checklist §6 belum dicentang. Batch 02 merujuknya sebagai sumber guardrail UI. | Konfirmasi owner apakah isinya disetujui. |
| B-4 | `PLANNING_COMPLETION_BATCH.md` berada di root repo; Batch 02 merujuk `docs/`. File tidak dipindahkan. | Keputusan owner (opsional). |
| B-5 | O-01, O-02, O-04, O-06–O-11, O-16 masih OPEN. O-01 punya kombinasi PROPOSED tetapi belum terbukti di CI. O-04 sudah punya rencana uji, tetapi belum ada bukti; runtime Chaquopy berjalan di proses utama aplikasi, jadi isolasi bergantung pada uji `isolatedProcess` (F-07–F-10). | Izin prototipe + batas uji dari owner. |
| B-6 | Android SDK tidak tersedia di container cloud; `dl.google.com` 403. Tidak menghalangi karena build direncanakan di GitHub Actions. | — |
| B-7 | DataStore disebut "existing blueprint baseline" di Batch 02 (TD:26), tetapi tidak ada di blueprint (catatan K-1 di [DECISIONS_LOG.md](DECISIONS_LOG.md)). | Konfirmasi owner. |
| B-8 | Host dokumentasi resmi (`chaquo.com`, `docs.python.org`, `pyodide.org`, `docs.gradle.org`, `github.com`, `dl.google.com`, `rfc-editor.org`, `csrc.nist.gov`, `www8.cao.go.jp`, `laws.e-gov.go.jp`) diblokir dari sesi cloud; riset memakai sumber dokumen di repositori resmi via `raw.githubusercontent.com`, `developer.android.com`, `kotlinlang.org`, dan Maven Central. | Opsional: buka host di pengaturan jaringan. |
| B-10 | Spesifikasi penilaian bergantung pada keputusan OPEN: cakupan agregasi skor, basis lulus (skor terbaik — OPEN-CONFIRM), representasi angka, rubrik penjelasan konsep, rumus durasi ujian, identitas XP, aturan unlock (OP-1–OP-12). | Keputusan owner. |
| B-11 | Backup: pemalsuan nilai oleh pemilik kata sandi tidak dapat dicegah kripto offline (OD-2); mode restore bertentangan antara pelestarian riwayat (BL:63–64) dan larangan merge otomatis (B01 M-16) (OD-3); Auto Backup aktif secara default (OD-4). | Keputusan owner. |
| B-12 | Kalender: situs resmi Kantor Kabinet Jepang dan e-Gov diblokir; dataset hari libur dan contoh tanggal belum terverifikasi; rentang tahun, mekanisme pembaruan, kalender perusahaan, label era, dan perilaku jam tenang OPEN (CO-1–CO-7). | Akses ke `www8.cao.go.jp` + keputusan owner. |
| B-9 | minSdk 24 hanya usulan; terkait M-19 (target perangkat), O-04 (Chaquopy butuh ≥ 24), dan O-06 (`PBKDF2withHmacSHA256` platform baru tersedia di API 26+). | Keputusan owner. |

B-2 (sumber Batch 02 belum ada) selesai di PR #7.

## Langkah berikutnya (usulan, menunggu owner)

Urutan persiapan Batch 02 §4 sudah dicakup Batch 03–07, kecuali kriteria
aksesibilitas/screenshot UI.

1. Owner memutuskan butir prioritas: OD-2/OD-3/OD-4 (backup), OP-1–OP-3
   (penilaian), CO-1/CO-2 (kalender), minSdk (B-9), batas uji O-04.
2. Verifikasi dataset hari libur dari `syukujitsu.csv` resmi (CO-3).
3. Spesifikasi kriteria aksesibilitas dan screenshot UI.
4. Konfirmasi status Batch 01 (B-3) dan DataStore (B-7).
