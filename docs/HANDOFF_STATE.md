# IT ZERO → HERO — Handoff State

Checkpoint ringkas antarbatch (lihat [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md)).
Hanya berisi fakta yang dapat dicek di repositori atau GitHub. Diperbarui
di setiap PR batch.

## Status proyek

| Item | Nilai | Sumber |
|---|---|---|
| Tahap | PERSIAPAN; implementasi **belum diizinkan** | [`CLAUDE.md`](../CLAUDE.md), [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) |
| `main` saat checkpoint ditulis | `993a85c` (merge PR #9) | `git log` |
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
| PR Batch 05 | [ASSESSMENT_STATE_MACHINE_SPEC.md](ASSESSMENT_STATE_MACHINE_SPEC.md) + handoff | Terbuka, menunggu review owner |

## Tugas terakhir

Batch 05: [ASSESSMENT_STATE_MACHINE_SPEC.md](ASSESSMENT_STATE_MACHINE_SPEC.md)
— state machine attempt (ujian teori, lab, mini-project, penjelasan konsep),
status komponen/unit, aturan persistensi, tenggat ujian persisten dan risiko
jam perangkat, rumus 30/40/20/10 tanpa pembulatan untuk keputusan lulus,
tabel kasus batas, acceptance criteria ledger XP, dan 12 butir OPEN
(OP-1–OP-12). Status: PR terbuka, belum di-merge.

## Blocker

| # | Blocker | Butuh |
|---|---|---|
| B-1 | Implementasi belum diizinkan. | Izin eksplisit owner. |
| B-3 | `PLANNING_COMPLETION_BATCH.md` sudah di-merge tetapi header-nya masih *DRAFT FOR OWNER REVIEW* dan checklist §6 belum dicentang. Batch 02 merujuknya sebagai sumber guardrail UI. | Konfirmasi owner apakah isinya disetujui. |
| B-4 | `PLANNING_COMPLETION_BATCH.md` berada di root repo; Batch 02 merujuk `docs/`. File tidak dipindahkan. | Keputusan owner (opsional). |
| B-5 | O-01, O-02, O-04, O-06–O-11, O-16 masih OPEN. O-01 punya kombinasi PROPOSED tetapi belum terbukti di CI. O-04 sudah punya rencana uji, tetapi belum ada bukti; runtime Chaquopy berjalan di proses utama aplikasi, jadi isolasi bergantung pada uji `isolatedProcess` (F-07–F-10). | Izin prototipe + batas uji dari owner. |
| B-6 | Android SDK tidak tersedia di container cloud; `dl.google.com` 403. Tidak menghalangi karena build direncanakan di GitHub Actions. | — |
| B-7 | DataStore disebut "existing blueprint baseline" di Batch 02 (TD:26), tetapi tidak ada di blueprint (catatan K-1 di [DECISIONS_LOG.md](DECISIONS_LOG.md)). | Konfirmasi owner. |
| B-8 | Host dokumentasi resmi (`chaquo.com`, `docs.python.org`, `pyodide.org`, `docs.gradle.org`, `github.com`, `dl.google.com`) diblokir dari sesi cloud; riset memakai sumber dokumen di repositori resmi via `raw.githubusercontent.com`, `developer.android.com`, `kotlinlang.org`, dan Maven Central. | Opsional: buka host di pengaturan jaringan. |
| B-10 | Spesifikasi penilaian bergantung pada keputusan OPEN: cakupan agregasi skor, basis lulus (skor terbaik — OPEN-CONFIRM), representasi angka, rubrik penjelasan konsep, rumus durasi ujian, identitas XP, aturan unlock (OP-1–OP-12). | Keputusan owner. |
| B-9 | minSdk 24 hanya usulan; terkait M-19 (target perangkat) dan O-04 (Chaquopy butuh ≥ 24). | Keputusan owner. |

B-2 (sumber Batch 02 belum ada) selesai di PR #7.

## Langkah berikutnya (usulan, menunggu owner)

1. Owner meninjau spesifikasi penilaian dan menjawab OP-1, OP-2, OP-3
   (paling menentukan untuk desain data).
2. Owner meninjau kombinasi toolchain PROPOSED dan memutuskan minSdk (B-9).
3. Owner menetapkan batas uji O-04 dan memutuskan izin prototipe kelayakan.
4. Lanjut urutan Batch 02 §4: threat model backup dan kriteria penerimaan
   restore.
5. Spesifikasi dataset hari libur dan kriteria aksesibilitas/screenshot UI.
