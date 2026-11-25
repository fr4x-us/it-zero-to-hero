# Catatan Eksekusi Resmi Paket Validasi (PR #28 putaran 5)

Dicatat dari keluaran nyata. Eksekusi dilakukan pada commit `81158d896217601390f94b970c5452dbc97f67f1`
(snapshot bersih); berkas ini ditambahkan pada commit **sesudahnya** yang
hanya menambah berkas ini (isi yang diuji tidak berubah). Hasil penulis,
bukan verifikasi independen. Hasil SEMANTIK (bukti "lokasi menilai konsep",
register kesetaraan) tidak diverifikasi otomatis.

| Item | Nilai |
|---|---|
| Commit diuji | `81158d896217601390f94b970c5452dbc97f67f1` |
| Tree `curriculum/` | `bf41b53f511261954bb961498f2432bfa0c1f595` |
| Tree `docs/` | `6355ed13fa830b737508e96090cc1a8237653b88` |
| Tree `docs/validation/` | `443a43bdb153eb40bf4297e09ac947a90ddcb06d` |
| Dependensi | Python 3.13.18, PyYAML 6.0.3, git version 2.43.0 |

## 1. `python3 docs/validation/run_all.py --official`

Exit code: 0

```text
Mode: RESMI
Python 3.13.18; PyYAML 6.0.3
commit: 81158d896217601390f94b970c5452dbc97f67f1
tree_curriculum: bf41b53f511261954bb961498f2432bfa0c1f595
tree_docs_validation: 443a43bdb153eb40bf4297e09ac947a90ddcb06d
tree_docs: 6355ed13fa830b737508e96090cc1a8237653b88
Provenance: snapshot bersih
  dokumen wajib: 43; uji negatif 3, positif 1
[dokumen] pemeriksaan 5 (STRUKTUR 5): ALL OK
  fixture NB-5: 39
  konsumen NB-5 W5–W6: 82 (teori 30, lab 52)
  uji mutasi tertangkap: 5/5
[NB-5] pemeriksaan 84 (REGRESI 43, STRUKTUR 41): ALL OK
  fixture BN-6 10, B01 9, BX 14
[BN-6/B01/BX] pemeriksaan 60 (HITUNG 5, REGRESI 47, STRUKTUR 8): ALL OK
  W7 tukar bersebelahan diuji: 16476
[kunci] pemeriksaan 33 (HITUNG 11, REGRESI 17, STRUKTUR 5): ALL OK
  W01: baseline df76c5f; varian berubah 1; tercatat PENDING 1
  W02: baseline 846051f; varian berubah 8; tercatat PENDING 8
  W03: baseline 846051f; varian berubah 2; tercatat PENDING 2
  W04: baseline 846051f; varian berubah 3; tercatat PENDING 3
  W05: belum diterima owner
  W06: belum diterima owner
  W07: belum diterima owner
  W08: belum diterima owner
  uji validator: 12 kasus — 9 mutasi terdeteksi, 3 kasus sah diterima (data asli; versi historis 2.0; revisi 2.0 → 3.0)
[penerimaan] pemeriksaan 28 (STRUKTUR 28): ALL OK
  konsep 156; PASS 153; OPEN (semantik lemah) 3 [('03', 's01', 'peran router'), ('03', 's01', 'peran switch'), ('04', 's03', 'OTP tidak dibagikan')]; GAP 0; kesetaraan PASS 43, OPEN 5 [('03', 's03'), ('04', 's01'), ('04', 's03'), ('07', 's02'), ('07', 's03')]
  SEMANTIK: bukti "lokasi menilai konsep" dan register kesetaraan = penilaian penulis (tidak diverifikasi otomatis)
[cakupan] pemeriksaan 174 (STRUKTUR 174): ALL OK
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
