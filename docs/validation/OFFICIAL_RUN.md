# Catatan Eksekusi Resmi Paket Validasi (PR #28 penerimaan owner final)

Dicatat dari keluaran nyata (stdout dan stderr digabung, `2>&1`). Eksekusi
dilakukan pada commit `9dfa5cdac3481ebcfc1ded78c99e6a318bfad314` dengan working tree bersih (`git status
--porcelain` = 0 baris). Berkas ini ditambahkan pada commit **sesudahnya**
yang hanya mengubah berkas ini; mode resmi dijalankan ulang pada HEAD akhir
dan hasilnya dilaporkan di deskripsi PR. Hasil penulis, **bukan** review
independen. Hasil SEMANTIK (bukti "lokasi menilai konsep", register
kesetaraan) tidak diverifikasi otomatis. Catatan putaran 5–8 digantikan; commit yang diuji adalah commit penerimaan (hanya metadata penerimaan, register, status, dan validator penerimaan berubah dari HEAD review `b54f930`). Eksekusi independen oleh reviewer sebelumnya terhambat clone GitHub (exit 128); eksekusi penulis ini tidak menyelesaikan batas itu.

| Item | Nilai |
|---|---|
| Commit diuji | `9dfa5cdac3481ebcfc1ded78c99e6a318bfad314` |
| Tree `curriculum/` | `3a071f2b419aced48aefaf2fed0475e5991df13b` |
| Tree `docs/` | `3d1502c9efa0045754ba0dc79d3fbf23ce49bb83` |
| Tree `docs/validation/` | `acbcd045fb58aac060919c83cace8a5777632f1b` |
| Dependensi | Python 3.13.18, PyYAML 6.0.3, git version 2.43.0 |

## 1. `python3 docs/validation/run_all.py --official`

Exit code: 0 · harapan: 0 dan `KELUARAN = expected/run_all.txt`

```text
Mode: RESMI
Python 3.13.18; PyYAML 6.0.3
commit: 9dfa5cdac3481ebcfc1ded78c99e6a318bfad314
tree_curriculum: 3a071f2b419aced48aefaf2fed0475e5991df13b
tree_docs_validation: acbcd045fb58aac060919c83cace8a5777632f1b
tree_docs: 3d1502c9efa0045754ba0dc79d3fbf23ce49bb83
Provenance: snapshot bersih
  dokumen wajib: 43; uji negatif 3, positif 1
[dokumen] pemeriksaan 5 (STRUKTUR 5): ALL OK
  fixture NB-5: 67
  kombinasi konten cacat: 112
  konsumen NB-5 W5–W6: 82 (teori 30, lab 52)
  uji mutasi tertangkap: 5/5
  uji pemindai ujung-ke-ujung R6-05/R7-02: 15 (11 konten cacat, 2 pengecualian non-NB-5, 2 CLI)
[NB-5] pemeriksaan 243 (REGRESI 198, STRUKTUR 45): ALL OK
  fixture BN-6 10, B01 9, BX 14
[BN-6/B01/BX] pemeriksaan 60 (HITUNG 5, REGRESI 47, STRUKTUR 8): ALL OK
  W7 tukar bersebelahan diuji: 16476
[kunci] pemeriksaan 33 (HITUNG 11, REGRESI 17, STRUKTUR 5): ALL OK
  W01: baseline tepercaya df76c5f (merge PR #25, W01-ACC); varian berubah 1; revisi PENDING 0, ACCEPTED 1
  W02: baseline tepercaya 846051f (merge PR #27, W02-ACC); varian berubah 8; revisi PENDING 0, ACCEPTED 8
  W03: baseline tepercaya 846051f (merge PR #27, W03-ACC); varian berubah 5; revisi PENDING 0, ACCEPTED 5
  W04: baseline tepercaya 846051f (merge PR #27, W04-ACC); varian berubah 7; revisi PENDING 0, ACCEPTED 7
  W05: baseline tepercaya b54f930 (HEAD review PR #28, W05-ACC); varian berubah 0; revisi PENDING 0, ACCEPTED 0
  W06: baseline tepercaya b54f930 (HEAD review PR #28, W06-ACC); varian berubah 0; revisi PENDING 0, ACCEPTED 0
  W07: baseline tepercaya b54f930 (HEAD review PR #28, W07-ACC); varian berubah 0; revisi PENDING 0, ACCEPTED 0
  W08: baseline tepercaya b54f930 (HEAD review PR #28, W08-ACC); varian berubah 0; revisi PENDING 0, ACCEPTED 0
  total varian revisi W1–W4: PENDING 0, ACCEPTED 21
  uji validator: 33 kasus — 27 mutasi terdeteksi, 6 kasus sah diterima (data PENDING; versi historis 2.0; revisi 2.0 → 3.0; field bersama berubah + semua varian tercatat; lokasi asli; penerimaan revisi PR #28 ACC)
  uji jangkar R6-01: 8 kasus — 7 penolakan, 1 penerimaan (baseline sah)
[penerimaan] pemeriksaan 73 (STRUKTUR 73): ALL OK
  R6-03 integritas kunci: 416 varian butir + lab + proyek W1–W8; uji kunci 28 (positif 8, negatif 20)
  VA-2 skenario: 8 attempt normal — diizinkan VA-4a; sinkron+induksi True; jalur salin aman True
  VA-2 skenario: gagal sebelum commit (tanpa sisa parsial) — diizinkan VA-4a; sinkron+induksi True; jalur salin aman True
  VA-2 skenario: terputus setelah commit utuh + resume berulang tanpa pemilihan ulang — diizinkan VA-4a; sinkron+induksi True; jalur salin aman True
  VA-2 skenario: remedial tanpa batas (VA-3, 51 attempt) — diizinkan VA-4a; sinkron+induksi True; jalur salin aman True
  VA-2 skenario: restore snapshot utuh yang diizinkan — diizinkan VA-4a; sinkron+induksi True; jalur salin aman True
  VA-2 skenario: riwayat parsial (slot tidak tercatat) — ditolak (integritas terkendali) True
  VA-2 skenario: riwayat rusak (catatan slot hilang) — ditolak (integritas terkendali) True
  VA-2 asumsi jumlah/urutan varian: OK
  konsep 156; PASS 156; OPEN (semantik lemah) 0 []; GAP 0; kesetaraan PASS 48, OPEN 0 []
  SEMANTIK: bukti "lokasi menilai konsep" dan register kesetaraan = penilaian penulis (tidak diverifikasi otomatis)
[cakupan] pemeriksaan 378 (STRUKTUR 378): ALL OK
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
