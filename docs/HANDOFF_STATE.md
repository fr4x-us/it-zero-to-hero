# IT ZERO → HERO — Handoff State

Checkpoint ringkas antarbatch (lihat [GITHUB_BRIDGE.md](GITHUB_BRIDGE.md)).
Hanya berisi fakta yang dapat dicek di repositori atau GitHub. Diperbarui
di setiap PR batch.

## Status proyek

| Item | Nilai | Sumber |
|---|---|---|
| Tahap | PERSIAPAN; implementasi **belum diizinkan** | [`CLAUDE.md`](../CLAUDE.md), [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) |
| `main` saat checkpoint ditulis | `9267e10` (merge PR #6) | `git log` |
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
| PR Batch 02 | [TECHNICAL_DECISIONS_BATCH_02.md](TECHNICAL_DECISIONS_BATCH_02.md) + pembaruan log keputusan dan handoff | Terbuka, menunggu review owner |

## Tugas terakhir

Batch 02: lampiran owner `TECHNICAL_DECISIONS_BATCH_02.md` ditambahkan
tanpa perubahan (SHA-256 sama dengan lampiran);
[DECISIONS_LOG.md](DECISIONS_LOG.md) mencatat 10 arah APPROVED dan 10
butir yang tetap OPEN. Status: PR terbuka, belum di-merge.

## Blocker

| # | Blocker | Butuh |
|---|---|---|
| B-1 | Implementasi belum diizinkan. | Izin eksplisit owner. |
| B-3 | `PLANNING_COMPLETION_BATCH.md` sudah di-merge tetapi header-nya masih *DRAFT FOR OWNER REVIEW* dan checklist §6 belum dicentang. Batch 02 merujuknya sebagai sumber guardrail UI. | Konfirmasi owner apakah isinya disetujui. |
| B-4 | `PLANNING_COMPLETION_BATCH.md` berada di root repo; Batch 02 merujuk `docs/`. File tidak dipindahkan. | Keputusan owner (opsional). |
| B-5 | O-01, O-02, O-04, O-06–O-11, O-16 masih OPEN; paling berisiko O-04 (runtime Python offline). | Rencana kelayakan / keputusan owner. |
| B-6 | Android SDK tidak tersedia di container cloud; `dl.google.com` 403. Tidak menghalangi karena build direncanakan di GitHub Actions. | — |
| B-7 | DataStore disebut "existing blueprint baseline" di Batch 02 (TD:26), tetapi tidak ada di blueprint (catatan K-1 di [DECISIONS_LOG.md](DECISIONS_LOG.md)). | Konfirmasi owner. |

B-2 (sumber Batch 02 belum ada) selesai di PR Batch 02.

## Langkah berikutnya (usulan, menunggu owner)

Urutan persiapan dari Batch 02 §4 (bukan izin implementasi):

1. Rencana uji kelayakan Python offline (tanpa prototipe).
2. Lembar keputusan kompatibilitas toolchain (tanpa file Gradle).
3. Kriteria penerimaan state machine penilaian dan persistensi.
4. Threat model backup dan kriteria penerimaan restore.
5. Spesifikasi dataset hari libur dan kriteria aksesibilitas/screenshot UI.
