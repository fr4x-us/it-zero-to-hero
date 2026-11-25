# Catatan Eksekusi Resmi Paket Validasi (PR #28 putaran 6)

Dicatat dari keluaran nyata. Eksekusi dilakukan pada commit `f29ac81e2f5eceb7a1dbe202602e6ce55b92b337`
(snapshot bersih); berkas ini ditambahkan pada commit **sesudahnya** yang
hanya menambah berkas ini (isi yang diuji tidak berubah). Hasil penulis,
bukan verifikasi independen. Hasil SEMANTIK (bukti "lokasi menilai konsep",
register kesetaraan) tidak diverifikasi otomatis.

| Item | Nilai |
|---|---|
| Commit diuji | `f29ac81e2f5eceb7a1dbe202602e6ce55b92b337` |
| Tree `curriculum/` | `acc1103218f871f2b455e66284bbcfcb54c01122` |
| Tree `docs/` | `253ea26110889b8a9593baefcead576ebfefa89d` |
| Tree `docs/validation/` | `131c458cf524f838b750f4d6a7116c600de9ea6c` |
| Dependensi | Python 3.13.18, PyYAML 6.0.3, git version 2.43.0 |

## 1. `python3 docs/validation/run_all.py --official`

Exit code: 0

```text
Mode: RESMI
Python 3.13.18; PyYAML 6.0.3
commit: f29ac81e2f5eceb7a1dbe202602e6ce55b92b337
tree_curriculum: acc1103218f871f2b455e66284bbcfcb54c01122
tree_docs_validation: 131c458cf524f838b750f4d6a7116c600de9ea6c
tree_docs: 253ea26110889b8a9593baefcead576ebfefa89d
Provenance: snapshot bersih
  dokumen wajib: 43; uji negatif 3, positif 1
[dokumen] pemeriksaan 5 (STRUKTUR 5): ALL OK
  fixture NB-5: 55
  kombinasi konten cacat: 112
  konsumen NB-5 W5–W6: 82 (teori 30, lab 52)
  uji mutasi tertangkap: 5/5
[NB-5] pemeriksaan 213 (REGRESI 171, STRUKTUR 42): ALL OK
  fixture BN-6 10, B01 9, BX 14
[BN-6/B01/BX] pemeriksaan 60 (HITUNG 5, REGRESI 47, STRUKTUR 8): ALL OK
  W7 tukar bersebelahan diuji: 16476
[kunci] pemeriksaan 33 (HITUNG 11, REGRESI 17, STRUKTUR 5): ALL OK
  W01: baseline df76c5f; varian berubah 1; tercatat PENDING 1
  W02: baseline 846051f; varian berubah 8; tercatat PENDING 8
  W03: baseline 846051f; varian berubah 3; tercatat PENDING 3
  W04: baseline 846051f; varian berubah 4; tercatat PENDING 4
  W05: belum diterima owner
  W06: belum diterima owner
  W07: belum diterima owner
  W08: belum diterima owner
  total varian W1–W4 tercatat PENDING: 16
  uji validator: 22 kasus — 18 mutasi terdeteksi, 4 kasus sah diterima (data asli; versi historis 2.0; revisi 2.0 → 3.0; field bersama berubah + semua varian tercatat)
[penerimaan] pemeriksaan 38 (STRUKTUR 38): ALL OK
  konsep 156; PASS 153; OPEN (semantik lemah) 3 [('03', 's01', 'peran router'), ('03', 's01', 'peran switch'), ('04', 's03', 'OTP tidak dibagikan')]; GAP 0; kesetaraan PASS 47, OPEN 1 [('04', 's01')]
  SEMANTIK: bukti "lokasi menilai konsep" dan register kesetaraan = penilaian penulis (tidak diverifikasi otomatis)
[cakupan] pemeriksaan 341 (STRUKTUR 341): ALL OK
KELUARAN = expected/run_all.txt
Catatan: penilaian SEMANTIK penulis (coverage_data.py, equivalence_notes.py) tidak diverifikasi otomatis.
```

## 2. `python3 docs/validation/test_provenance.py`

Exit code: 0

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
