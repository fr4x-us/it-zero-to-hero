# IT ZERO → HERO — Templat Dokumentasi Kurikulum (CB-0, PROVISIONAL)

Status: **PROVISIONAL** · dokumentasi saja · templat **bukan** konten
kurikulum dan tidak dihitung sebagai komponen selesai. Tanggal:
**2026-11-24**. Basis: `main` = `928e278`. Kode rujukan: `TPL:`.

CB-0 baru final setelah keputusan owner yang ditandai di kolom
"Bergantung" (lihat [CURRICULUM_PRODUCTION_PLAN.md](CURRICULUM_PRODUCTION_PLAN.md)
§6). Field yang sudah ditetapkan keputusan owner ditandai dengan nomor
keputusannya.

Legenda "Bergantung": **—** = tidak bergantung keputusan terbuka;
`OP-5`, `OP-7`, `OP-8`, `OP-9`, `OP-10`, `CU-3`, `CU-5`, `CU-7`, `CU-9`,
`CU-11`, `CU2-O3`, `CU2-O4`, `CU2-O5`, `CU-10`, `OD-15` = keputusan yang masih OPEN.

## TPL-01 Ikhtisar modul

| Field | Isi | Bergantung |
|---|---|---|
| `module_id` | `mod-wNN` (stabil) | — (CUR §4.1) |
| Fase, minggu, judul | Sesuai urutan terkunci | — (BL:15–24, D-01 M-02) |
| `content_version` | Versi mayor.minor | CU-3 |
| Ringkasan modul | 3–5 kalimat Bahasa Indonesia | — |
| Prasyarat | Modul/kompetensi sebelumnya | OP-9 |
| Alokasi jam M/U/L/P/C/R | Jumlah 8,0 jam | CU2-O3 |
| Daftar komponen | Theory 30%, Lab 40%, Mini-project 20%, Concept 10% | — (D-13) |
| Catatan runtime | W9–W12, W16: eksekusi NOT VERIFIED; penerimaan perencanaan sesuai RM:RV-1–RV-6 | — |

## TPL-02 Tujuan belajar

| Field | Isi | Bergantung |
|---|---|---|
| `competency_id` | `comp-wNN-xxx-nn` | — |
| Tujuan terukur | Kata kerja terukur (menjelaskan, menghitung, menulis, menelusuri) | — |
| Tingkat kesulitan sasaran | D1/D2/D3 | OP-5 |
| Komponen yang mengukur | Theory/Lab/Mini-project/Concept | — |

## TPL-03 Isi pelajaran

| Field | Isi | Bergantung |
|---|---|---|
| `lesson_id` | `mod-wNN.les-nn` | — |
| Teks | Markdown terbatas | CU-3 |
| Diagram | Sumber + `alt` + deskripsi panjang | CU-3 (format), — (deskripsi wajib, CC-10) |
| Contoh kode | Blok berlabel + output contoh | CU-3 |
| Glosarium | Istilah, padanan Inggris, definisi | — |
| Ringkasan | Poin utama | — |
| Video opsional | Tautan, ditandai tidak tersedia offline | — (BL:24) |
| Durasi | Menit | CU2-O3 |

## TPL-04 Bank soal teori

| Field | Isi | Bergantung |
|---|---|---|
| `item_id`, `item_version` | Stabil + versi | — |
| Slot blueprint | Kompetensi × format × kesulitan | OP-5 |
| Format | TF-1–TF-5 | OP-5 |
| Teks soal, opsi | — | — |
| Kunci + jawaban alternatif | Eksplisit | — (CE-K2 sebagai praktik) |
| Normalisasi jawaban singkat | Aturan eksplisit | OP-5 |
| Poin | Bilangan bulat | OP-5 (TP) |
| Pembahasan | Untuk umpan balik | OP-5 (FB) |
| Varian | ID varian setara | CU-5 |

## TPL-05 Latihan laboratorium

| Field | Isi | Bergantung |
|---|---|---|
| `activity_id` | `mod-wNN.lab.act-nn` | OP-8 (identitas XP) |
| Jenis lab | Python, SQL, HTML/CSS, Git, biner/Boolean, flowchart, klasifikasi | CU-7 (SQL/HTML/Git) |
| Instruksi + kode/skema awal | — | — |
| Test (ID, input, output diharapkan, poin integer, `tᵢ` ms, terlihat/tersembunyi) | LW-B, LR-A, TB-B (`Σ tᵢ ≤ 3.000` ms) | — (D-24); LX-1–LX-9 OPEN |
| Kode hasil dan kasus khusus | §5–§6 CU-6 | — (D-24) |
| Varian | Data/fixture berbeda | CU-5 |
| Penyerahan | Per aktivitas dalam attempt RA-1 | OP-7 |

## TPL-06 Fixture uji

| Field | Isi | Bergantung |
|---|---|---|
| `fixture_id` | Stabil | — |
| Isi | Data uji (teks, tabel SQL, dokumen) | CU-7 |
| Terlihat/tersembunyi | — | — |
| Kasus tepi yang dicakup | Kosong, batas, rusak, `NULL`, duplikat | CU-7 |
| Deterministik | Tanpa waktu nyata/acak tanpa seed | — (LB-5) |

## TPL-07 Spesifikasi mini-project

| Field | Isi | Bergantung |
|---|---|---|
| Tujuan dan lingkup | Sesuai jam P | CU2-O3 |
| Deliverable | Daftar | CU2-O4 (W1–W15), CU-9 (W16) |
| Rubrik | TPL-09 | CU2-O4, CU-9 |
| Acceptance test terencana | Tidak dijalankan | — |
| Remedial | Salinan submission sebelumnya | CU-5 (MPV) |

## TPL-08 Bank soal penjelasan konsep

| Field | Isi | Bergantung |
|---|---|---|
| `item_id`, `item_version` | — | — |
| Format | CE-S1–CE-S5 | — (D-23) |
| Konsep wajib | CE-K1 | — (D-23) |
| Jawaban diterima + alternatif; urutan diterima lengkap | CE-K2, CE-K3 | — (D-23) |
| `max_soal`, aturan kredit | CE-S | — (D-23) |
| Validasi | CE-V1–CE-V7 | — (D-23) |
| Varian | — | CU-5 |
| Review manusia | Nama/tanggal | — (CE-K4) |

## TPL-09 Rubrik penilaian

| Field | Isi | Bergantung |
|---|---|---|
| Kriteria | ID, deskripsi objektif | CU2-O4 / CU-9 |
| Poin | Bilangan bulat; total ≤ 10.000 | — (D-12) |
| Metode evaluasi offline | Pemeriksa otomatis | CU-7 |
| Wajib/tidak | Kriteria wajib capstone | CU-9 |
| Kredit parsial | Per pemeriksaan | CU2-O4 / CU-9 |

## TPL-10 Varian remedial

| Field | Isi | Bergantung |
|---|---|---|
| Slot/aktivitas | — | — |
| Daftar varian + bukti kesetaraan (kompetensi, format, kesulitan, poin) | — | CU-5 (jumlah N) |
| Aturan pemilihan | VA-2 | CU-5 |
| Materi remedial | Penjelasan ulang per kompetensi | — |

## TPL-11 Metadata aksesibilitas

| Field | Isi | Bergantung |
|---|---|---|
| `alt` gambar/diagram | Wajib | — (CC-10) |
| Deskripsi panjang | Wajib untuk diagram | — |
| Penanda bahasa istilah Inggris | `lang: en` | CU-3 |
| Deskripsi tabel | Bila tabel memuat data inti | — |
| Urutan baca | Eksplisit bila tata letak tidak linear | CU-3 |

## TPL-12 Checklist review konten

| ID | Pemeriksaan |
|---|---|
| TR-01 | Semua field TPL-01–TPL-11 terisi; field bergantung keputusan OPEN tidak diisi dengan tebakan |
| TR-02 | CPP:CA-01–CA-11 lolos |
| TR-03 | Poin integer; total per komponen per attempt ≤ 10.000 |
| TR-04 | Kunci, jawaban alternatif, dan aturan kredit eksplisit; review manusia tercatat |
| TR-05 | Test dan fixture deterministik; tidak ada klaim sudah dijalankan |
| TR-06 | Materi inti offline; video opsional |
| TR-07 | Bahasa Indonesia; istilah Inggris dijelaskan |
| TR-08 | Aksesibilitas TPL-11 |
| TR-09 | Durasi sesuai alokasi; total modul 8,0 jam |
| TR-10 | Tanpa AI grading/tutor; tanpa server wajib |
| TR-11 | Penerimaan owner tercatat |

Templat ini tidak mengubah status 64 komponen (tetap **NOT STARTED**).
