# IT ZERO → HERO — Log Sumber Keputusan

Status: PERSIAPAN. Implementasi aplikasi belum diizinkan.

Dokumen ini hanya **menunjuk** ke sumber keputusan per batch. Isi keputusan
tetap berada di dokumen sumbernya. Dokumen ini tidak menambah, mengubah,
atau menggantikan [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) dan
[`CLAUDE.md`](../CLAUDE.md).

| Status sumber | Arti |
|---|---|
| AVAILABLE | Dokumen ada di `main`. |
| PENDING SOURCE | Dokumen disebut owner tetapi belum ada di repositori; isinya tidak boleh dibuat ulang dari ingatan atau dugaan. |

## Daftar batch

| Batch | Dokumen sumber | Status sumber | Status persetujuan | Catatan |
|---|---|---|---|---|
| Baseline | [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md), [`CLAUDE.md`](../CLAUDE.md) | AVAILABLE | LOCKED | Sumber tertinggi. |
| Inventaris | [`PLANNING_HISTORY.md`](PLANNING_HISTORY.md) | AVAILABLE | Di-merge (PR #4) | Snapshot berbasis repo per `260800d`. |
| Batch 01 | [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) | AVAILABLE (di root repo, bukan `docs/`) | Di-merge (PR #5); header dokumen masih **DRAFT FOR OWNER REVIEW** dan kriteria selesai §6 belum dicentang | Perlu konfirmasi owner apakah merge PR #5 = persetujuan isi. |
| Batch 02 | `docs/TECHNICAL_DECISIONS_BATCH_02.md` (lokasi yang diharapkan) | **PENDING SOURCE** | Tidak diketahui | Tidak ada di repositori per `c0b73ad`. Isinya tidak dibuat ulang. |

## Batch 02 — Keputusan teknis (PENDING SOURCE)

Tempat ini disiapkan untuk mencatat keputusan teknis Batch 02 yang telah
disetujui owner. Sampai dokumen sumber diserahkan ke repositori:

- Semua butir O-01–O-17 tetap **OPEN** sesuai
  [`PLANNING_HISTORY.md` §3](PLANNING_HISTORY.md) dan
  [`PLANNING_COMPLETION_BATCH.md` §4](../PLANNING_COMPLETION_BATCH.md).
- Tabel di bawah sengaja kosong.

Cara mengisi setelah sumber tersedia: owner menambahkan
`docs/TECHNICAL_DECISIONS_BATCH_02.md` (melalui PR atau upload), lalu satu
PR dokumentasi mengisi tabel ini dengan rujukan bagian/baris ke dokumen
tersebut.

| ID OPEN | Keputusan disetujui | Rujukan sumber | PR |
|---|---|---|---|
| — | PENDING SOURCE | — | — |
