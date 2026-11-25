# Catatan Eksekusi Resmi Paket Validasi (PR #28 putaran 7)

Dicatat dari keluaran nyata (stdout dan stderr digabung, `2>&1`). Eksekusi
dilakukan pada commit `3617fc61f30fcb72a95bb346438b9cc38ee0c3cd` dengan working tree bersih (`git status
--porcelain` = 0 baris). Berkas ini ditambahkan pada commit **sesudahnya**
yang hanya mengubah berkas ini; mode resmi dijalankan ulang pada HEAD akhir
dan hasilnya dilaporkan di deskripsi PR. Hasil penulis, **bukan** review
independen. Hasil SEMANTIK (bukti "lokasi menilai konsep", register
kesetaraan) tidak diverifikasi otomatis. Catatan putaran 5–6 digantikan.

| Item | Nilai |
|---|---|
| Commit diuji | `3617fc61f30fcb72a95bb346438b9cc38ee0c3cd` |
| Tree `curriculum/` | `595ac8f836024d8a1dc2db042eac4527fe943216` |
| Tree `docs/` | `96237dacfcc5ed7a2d403ec86f159e06cbec1f2b` |
| Tree `docs/validation/` | `81067fa79c21b04e09c359538290f2597ef6f7c1` |
| Dependensi | Python 3.13.18, PyYAML 6.0.3, git version 2.43.0 |

## 1. `python3 docs/validation/run_all.py --official`

Exit code: 0 · harapan: 0 dan `KELUARAN = expected/run_all.txt`

```text
Mode: RESMI
Python 3.13.18; PyYAML 6.0.3
commit: 3617fc61f30fcb72a95bb346438b9cc38ee0c3cd
tree_curriculum: 595ac8f836024d8a1dc2db042eac4527fe943216
tree_docs_validation: 81067fa79c21b04e09c359538290f2597ef6f7c1
tree_docs: 96237dacfcc5ed7a2d403ec86f159e06cbec1f2b
Provenance: snapshot bersih
  dokumen wajib: 43; uji negatif 3, positif 1
[dokumen] pemeriksaan 5 (STRUKTUR 5): ALL OK
  fixture NB-5: 67
  kombinasi konten cacat: 112
  konsumen NB-5 W5–W6: 82 (teori 30, lab 52)
  uji mutasi tertangkap: 5/5
  uji pemindai ujung-ke-ujung R6-05: 9 (7 konten cacat, 2 CLI)
[NB-5] pemeriksaan 237 (REGRESI 192, STRUKTUR 45): ALL OK
  fixture BN-6 10, B01 9, BX 14
[BN-6/B01/BX] pemeriksaan 60 (HITUNG 5, REGRESI 47, STRUKTUR 8): ALL OK
  W7 tukar bersebelahan diuji: 16476
[kunci] pemeriksaan 33 (HITUNG 11, REGRESI 17, STRUKTUR 5): ALL OK
  W01: baseline tepercaya df76c5f (merge PR #25, W01-ACC); varian berubah 1; tercatat PENDING 1
  W02: baseline tepercaya 846051f (merge PR #27, W02-ACC); varian berubah 8; tercatat PENDING 8
  W03: baseline tepercaya 846051f (merge PR #27, W03-ACC); varian berubah 5; tercatat PENDING 5
  W04: baseline tepercaya 846051f (merge PR #27, W04-ACC); varian berubah 6; tercatat PENDING 6
  W05: belum diterima owner
  W06: belum diterima owner
  W07: belum diterima owner
  W08: belum diterima owner
  total varian W1–W4 tercatat PENDING: 20
  uji validator: 27 kasus — 22 mutasi terdeteksi, 5 kasus sah diterima (data asli; versi historis 2.0; revisi 2.0 → 3.0; field bersama berubah + semua varian tercatat; lokasi asli)
  uji jangkar R6-01: 8 kasus — 7 penolakan, 1 penerimaan (baseline sah)
[penerimaan] pemeriksaan 59 (STRUKTUR 59): ALL OK
  R6-03 integritas kunci: 416 varian butir + lab + proyek W1–W8; uji kunci 28 (positif 8, negatif 20)
  VA-2 skenario: 8 attempt normal — diizinkan; sinkron True; jalur salin aman True
  VA-2 skenario: attempt terputus (IN_PROGRESS, SB-8/SB-9 dicatat apa adanya) — diizinkan; sinkron True; jalur salin aman True
  VA-2 skenario: remedial tanpa batas (VA-3) — diizinkan; sinkron True; jalur salin aman True
  VA-2 skenario: restore cadangan lama (attempt utuh) — diizinkan; sinkron True; jalur salin aman True
  VA-2 skenario: pencatatan slot tidak atomik (tidak dijamin kontrak) — di luar jaminan kontrak; sinkron False; jalur salin aman False
  VA-2 skenario: riwayat rusak: catatan satu slot hilang — di luar jaminan kontrak; sinkron False; jalur salin aman True
  konsep 156; PASS 156; OPEN (semantik lemah) 0 []; GAP 0; kesetaraan PASS 48, OPEN 0 []
  SEMANTIK: bukti "lokasi menilai konsep" dan register kesetaraan = penilaian penulis (tidak diverifikasi otomatis)
[cakupan] pemeriksaan 376 (STRUKTUR 376): ALL OK
KELUARAN = expected/run_all.txt
Catatan: penilaian SEMANTIK penulis (coverage_data.py, equivalence_notes.py) tidak diverifikasi otomatis.
```

## 2. `python3 docs/validation/test_provenance.py`

Exit code: 0 · harapan: 0 (8 kasus)

```text
  OK    positif: snapshot bersih (exit 0)
  OK    negatif: berkas kurikulum berubah (exit 2)
  OK    negatif: fixture berubah (exit 2)
  OK    negatif: skrip validasi berubah (exit 2)
  OK    negatif: dokumen relevan berubah (exit 2)
  OK    negatif: berkas baru tak terlacak (exit 2)
  OK    diagnostik: tree kotor tetap dijalankan tetapi ditandai TIDAK TERVERIFIKASI (bukan bukti) (exit 0)
  OK    negatif: git/HEAD tidak tersedia (exit 2)
[provenance] kasus 8: ALL OK
```
