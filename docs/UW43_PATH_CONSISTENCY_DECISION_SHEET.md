# IT ZERO → HERO — Decision Sheet UW-43: Konsistensi Path `PLANNING_COMPLETION_BATCH.md`

Status: **DIPUTUSKAN OWNER — D-18 (2026-11-24): Opsi B**, lihat §5 · dokumentasi saja ·
file **tidak** dipindahkan. Tanggal: **2026-11-24**. Basis: `main` = `b789e9a`.

## 1. Temuan (diperiksa ulang 2026-11-24)

| Butir | Hasil |
|---|---|
| Lokasi file sebenarnya | `PLANNING_COMPLETION_BATCH.md` (root repo) |
| Rujukan ke `docs/PLANNING_COMPLETION_BATCH.md` di dokumen owner verbatim | **Hanya TD:5** (`TECHNICAL_DECISIONS_BATCH_02.md` baris 5) |
| **Koreksi:** catatan lama menyebut "TD:5 **dan TD:68**" | Salah. TD:68 merujuk `docs/TECHNICAL_DECISIONS_BATCH_02.md`, bukan Batch 01. Dikoreksi di DECISIONS_LOG K-2 dan dicatat di audit §15.1; baris historis audit (§1, §4) dibiarkan sebagai catatan masa lalu |
| Rujukan path lain yang menyebut `docs/PLANNING_COMPLETION_BATCH.md` | Hanya di dokumen audit/log yang **mendeskripsikan** masalah ini (DECISIONS_LOG K-2, audit, FINAL REVIEW) |
| Tautan Markdown ke file di root | 13 tautan di 12 file (`README.md` dan 11 dokumen di `docs/`), semuanya valid |
| Tautan keluar dari dalam file Batch 01 | Satu tautan Markdown ke `docs/OWNER_DECISION_CHECKLIST.md` di §7, ditulis relatif dari root (akan rusak bila file dipindah tanpa penyesuaian) |
| `CLAUDE.md` | Tidak merujuk file ini |
| Riwayat Git | 4 commit (`2fb4778` upload owner, `4f4d7fb`, `303657a`, `a17e04b`) |

## 2. Opsi

| Kriteria | Opsi A — pindahkan ke `docs/` dan perbarui rujukan | Opsi B — tetap di root + erratum eksplisit |
|---|---|---|
| Dokumen verbatim/historis | TD:5 menjadi benar **tanpa** mengubah TD; isi Batch 01 tidak berubah, hanya lokasinya | TD tidak diubah; erratum dicatat di DECISIONS_LOG |
| Tautan relatif | 13 tautan di 12 file harus diubah, ditambah tautan di dalam Batch 01 §7 | Tidak ada tautan yang berubah |
| Riwayat Git | Terlacak lewat `git log --follow`, tetapi tautan lama di PR/riwayat menunjuk path lama | Tidak berubah |
| `CLAUDE.md` dan navigasi | `CLAUDE.md` tidak terdampak; README harus diubah | Tidak terdampak |
| Risiko merusak rujukan sumber kebenaran | Sedang: banyak tautan diubah sekaligus; rujukan eksternal (prompt, catatan ChatGPT) ke path root menjadi basi | Rendah: satu rujukan teks di TD:5 tetap salah, tetapi didokumentasikan |
| Perubahan file | ±14 file | 1–2 file (erratum) |

## 3. Rekomendasi (saran, bukan keputusan)

**Opsi B** — paling sedikit gangguan: tidak ada file yang dipindahkan,
tidak ada tautan yang berubah, dan dokumen verbatim tetap utuh. Erratum
yang diusulkan untuk dicatat di DECISIONS_LOG:

> Erratum TD:5: `docs/PLANNING_COMPLETION_BATCH.md` harus dibaca sebagai
> `PLANNING_COMPLETION_BATCH.md` (root repositori). Teks TD tidak diubah
> karena merupakan salinan verbatim keputusan owner.

Opsi A tetap layak bila owner ingin semua dokumen perencanaan berada di
`docs/`; pemindahan harus dilakukan dalam satu PR khusus dengan pemeriksaan
tautan.

## 4. Pertanyaan untuk owner — *historis, dijawab D-18*

1. **UW-43-Q1:** Pilih Opsi B (tetap di root + erratum TD:5) atau Opsi A (pindah ke `docs/`)?

~~Status: AWAITING OWNER. UW-43 tetap BLOCKED.~~ *(Historis — dijawab D-18.)* File tidak dipindahkan
dan dokumen verbatim tidak diubah di PR ini.

## 5. Keputusan owner — D-18 (2026-11-24)

**Opsi B.** `PLANNING_COMPLETION_BATCH.md` tetap di root; erratum TD:5
dicatat di [DECISIONS_LOG.md](DECISIONS_LOG.md) (§Erratum, ER-1);
`TECHNICAL_DECISIONS_BATCH_02.md` tidak diubah; file Batch 01 tidak
dipindahkan; tautan relatif dan riwayat dipertahankan.

Verifikasi AC UW-43 ("Rujukan valid") pada 2026-11-24:

| Pemeriksaan | Hasil |
|---|---|
| Erratum ER-1 tercatat | Ya (DECISIONS_LOG) |
| File Batch 01 masih di root | Ya |
| TD:5 tidak diubah | Ya (`git diff` kosong untuk dokumen Batch 02) |
| Seluruh tautan Markdown relatif ke `PLANNING_COMPLETION_BATCH.md` valid | Ya (cek otomatis, 0 rusak) |
