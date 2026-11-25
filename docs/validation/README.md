# Paket Validasi Dokumentasi Kurikulum (PR #28)

Paket ini adalah **alat review dokumentasi**: membaca berkas YAML/Markdown di
`curriculum/` dan `docs/`, lalu memeriksa kontrak yang tertulis. Paket ini
**bukan** evaluator produksi, **bukan** kode aplikasi Android, dan **tidak**
dijalankan oleh CI. Disusun oleh penulis PR (Claude); hasilnya adalah hasil
penulis, **bukan** verifikasi independen.

## Cara menjalankan

Prasyarat: Python ≥ 3.10 dan PyYAML (diuji dengan Python 3.13.18, PyYAML 6.0.3).
Tidak ada dependensi lain.

```bash
# dari akar repositori
python3 docs/validation/run_all.py          # semua pemeriksaan; keluar 0 bila lolos dan keluaran = expected/run_all.txt
python3 docs/validation/check_nb5.py        # NB-5 saja (PR28-02)
python3 docs/validation/check_formats.py    # BN-6, B01, BX (PR28-03/04/05)
python3 docs/validation/check_keys.py       # kunci yang diubah PR #28 + posisi kunci
python3 docs/validation/check_acceptance.py # status penerimaan terstruktur TPL-01a (R3-08)
python3 docs/validation/build_matrix.py     # cakupan D-39 + register kesetaraan; --write membuat ulang dokumen matriks
```

`run_all.py` mencetak commit dan tree `curriculum/` yang diuji, serta tanda
bila working tree kotor.

## Konten yang diuji

| Item | Nilai |
|---|---|
| Commit konten (putaran 4) | `{{CONTENT_COMMIT}}` |
| Tree `curriculum/` pada commit itu | `{{CURRICULUM_TREE}}` |
| Keluaran yang diharapkan | [`expected/run_all.txt`](expected/run_all.txt) |
| Snapshot posisi kunci | [`expected/key_positions.yaml`](expected/key_positions.yaml) (= baseline `4ddc993`) |

## Isi paket

| Berkas | Fungsi |
|---|---|
| `lib.py` | Pemuatan berkas; kontrak NB-5 N1–N6 (`nb5`), BN-6 (`bn6`), B01 (`b01`), tata bahasa BX (`bx_parse`) |
| `check_nb5.py` + `fixtures/nb5_fixtures.yaml`, `fixtures/f51_fixtures.yaml` | 39 fixture terikat butir nyata; pemindaian 82 konsumen NB-5 W5–W6 (afiks per butir, presisi, kanonik, tanda, ribuan, `Rp` persis, pembeda EVALUATION_ERROR lab); uji mutasi 5; F-51 W3 tetap peka huruf |
| `check_formats.py` + `fixtures/format_fixtures.yaml` | BN-6 (nol kanonik, lebar tetap), B01 (trim + satu digit), BX (8 baris tabel kebenaran; terbaca vs ekuivalen vs tidak terbaca; mode strict K3) |
| `check_keys.py` | W8 F4 (interpreter tingkat-blok, 256 kombinasi, skor b/a/c/d/e = 100/94/94/94/92), W8 latihan 3, W7 K4.q2 (tukar bersebelahan), kunci butir D-39 dan putaran 4, distribusi posisi kunci |
| `check_acceptance.py` | TPL-01a: setiap varian yang berubah setelah penerimaan historis tercatat tepat dengan versi dan status PENDING |
| `coverage_data.py`, `equivalence_notes.py`, `matrix_header.md`, `build_matrix.py` | Data pembacaan butir (penulis), bukti QC-13 (a)/(b), uji metode, matriks 156 konsep dan register kesetaraan 48 slot |

## Arti hasil

- `ACCEPT` = bentuk sah dan nilai benar; `WRONG` = bentuk sah, nilai salah;
  `INVALID` = INVALID_ANSWER (bentuk tidak sah). EVALUATION_ERROR (kegagalan
  konten/aplikasi) dibedakan di teks kontrak dan diperiksa keberadaannya,
  bukan disimulasikan.
- Butir BN-6/B01 dikecualikan dari NB-5 secara eksplisit (`W6_NOT_NB5`).

## Batasan

- Pembacaan "konsep dinilai" dan klasifikasi inti/pendukung adalah penilaian
  penulis di `coverage_data.py`; skrip hanya menghitung bukti dari data itu
  dan memastikan daftar konsep sama dengan berkas.
- Tidak ada uji pelajar, runtime Android, atau evaluator produksi.
