# IT ZERO → HERO — Decision Sheets Rubrik Mini-project (CU2-O4) dan Capstone (CU-9)

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode
atau prototipe. Tanggal: **2026-11-24** (direvisi setelah review PR #24, F-07, F-08). Basis: `main` = `928e278`. Kode
rujukan: `RB:`. Terkait UW-36 (CU-9, CU2-O4 — D-25).

Rekomendasi adalah saran, **bukan** keputusan.

## 1. Batasan yang sudah disetujui

| ID | Batasan | Sumber |
|---|---|---|
| RB-R1 | Mini-project = 20% nilai modul; ada di semua 16 modul | BL:29, D-13 |
| RB-R2 | Komponen ≥ 75 (`4·e ≥ 3·m`); nilai tertimbang ≥ 80; eksak | BL:31–32, D-12 |
| RB-R3 | Poin bilangan bulat, maks. 10.000 per komponen per attempt; skor terbaik; tie → attempt paling awal | D-12 |
| RB-R4 | Mini-project tidak berwaktu; jeda/lanjut; remedial tanpa batas | BL:33, BL:37, D-01 M-08 |
| RB-R5 | Penilaian objektif offline tanpa AI | BL:38 |
| RB-R6 | Capstone = mini-project modul 16, di dalam 128 jam, dengan rubrik khusus | D-13 |
| RB-R7 | Program selesai = 16 modul lulus **dan** capstone memenuhi rubrik capstone; tanpa skor program | D-04, D-19 |
| RB-R8 | Kebutuhan mini-project dan capstone beserta rubrik dan acceptance test disetujui; isinya belum | D-01 M-09 |
| RB-R9 | Klaim penyelesaian oleh pelajar sendiri bukan bukti kinerja objektif | Instruksi owner batch ini; BL:38 |

---

## A. CU2-O4 — Rubrik mini-project W1–W15 (templat yang dapat dipakai ulang)

### A.1 Opsi struktur

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **MR-A Empat kriteria tetap** | K1 kebenaran fungsional 60, K2 kelengkapan deliverable 20, K3 struktur/format 10, K4 penjelasan terstruktur 10 (total 100) | Konsisten antarmodul; mudah dibandingkan | Bobot kriteria sama walau sifat proyek berbeda |
| MR-B Kriteria bebas per modul | Penyusun memilih kriteria dan bobot | Fleksibel | Sulit direview; risiko kriteria subjektif |
| MR-C Lulus/tidak per kriteria | Tanpa kredit parsial | Sederhana | Tidak menghargai progres; skor 0/100 ekstrem |

### A.2 Templat MR-A

| Kriteria | Poin | Metode evaluasi offline | Kredit parsial |
|---|---|---|---|
| K1 Kebenaran fungsional | 60 | Pemeriksaan otomatis deterministik sesuai jenis lab: test kode (D-24), perbandingan hasil SQL (CU-7 SQ), properti HTML (HV-A), keadaan Git (GS-A), aturan pada formulir terstruktur, tabel kebenaran, nilai trace table | Jumlah poin pemeriksaan yang lulus (LW-B, LR-A) |
| K2 Kelengkapan deliverable | 20 | Setiap deliverable wajib ada **dan** valid secara bentuk (mis. file ada, field terisi sesuai format) | Poin per deliverable |
| K3 Struktur dan format | 10 | Aturan bentuk yang dapat diperiksa: penamaan yang diminta, bagian wajib, batas panjang, tipe data | Poin per aturan |
| K4 Penjelasan proyek | 10 | Soal terstruktur tentang **tugas proyek ini** (desain, urutan langkah, alasan pilihan) dengan format D-23; tetap = soal tertulis di konten, bukan dibuat dari kode pelajar | Sesuai D-23; anggaran tetap 10 (A.2a) |

| ID | Aturan (usulan) |
|---|---|
| MR-1 | Poin kriteria bilangan bulat; total 100 per attempt (≤ 10.000) |
| MR-2 | Deliverable tidak ada: kriteria yang bergantung padanya bernilai 0; kriteria lain tetap dinilai |
| MR-3 | Solusi alternatif valid diterima: pemeriksaan K1 berbasis properti/hasil, bukan jawaban tunggal |
| MR-4 | Umpan balik per kriteria dan per pemeriksaan (lulus/gagal + petunjuk); pemeriksaan tersembunyi tidak dibocorkan isinya (kebijakan umpan balik lab D-24) |
| MR-5 | Remedial: attempt baru dari salinan submission sebelumnya (MPV-A, CU-5); attempt lama tidak berubah |
| MR-6 | Centang "sudah selesai", catatan refleksi, atau estimasi waktu oleh pelajar bernilai **0 poin** (RB-R9) |
| MR-8 | Poin setiap pemeriksaan K1–K3 ditulis eksplisit sebagai bilangan bulat dan jumlahnya **tepat** sama dengan anggaran kriteria; review menolak alokasi yang tidak dapat dicapai (mis. 5 pemeriksaan untuk 12 poin tanpa pembagian integer yang ditulis) |

### A.2a Pemetaan CE-S1–CE-S5 ke anggaran tetap (K4 = 10, CR-6 = 10)

Tidak ada penskalaan atau pembulatan: anggaran dipenuhi lewat **komposisi**
soal sehingga jumlah `max_soal` tepat 10 (D-23: maks. struktural CE-S2 = k,
CE-S3 = n − 1, CE-S4 = k; CE-S1 = P; CE-S5 = P genap).

| Komposisi contoh | Rincian `max_soal` | Jumlah |
|---|---|---|
| K-A | 5 × CE-S1 (P = 2) | 10 |
| K-B | 2 × CE-S1 (P = 2) + CE-S3 (n = 4 → 3) + CE-S4 (k = 3 → 3) | 4 + 3 + 3 = 10 |
| K-C | CE-S5 (P = 4) + CE-S2 (k = 3 → 3) + CE-S3 (n = 4 → 3) | 4 + 3 + 3 = 10 |
| Tidak sah | CE-S5 (P = 3) + … | P ganjil melanggar CE-S5 |
| Tidak sah | 3 × CE-S1 (P = 3) | 9 ≠ 10 |

Soal penjelasan **proyek** (K4, CR-6) adalah bagian skor komponen
Mini-project. Komponen **Concept explanation** (10% modul) terpisah: bank
soalnya sendiri tentang konsep modul (D-23, UW-26); soal tidak boleh dipakai
bersama di kedua komponen.
| MR-7 | Kegagalan infrastruktur saat evaluasi mengikuti IE-2 (D-24): evaluasi diulang, tanpa penalti |

### A.3 Brief mini-project W1–W15 (usulan; isi final di CB-1–CB-4)

| Modul | Mini-project | Deliverable | Evaluasi K1 |
|---|---|---|---|
| W1 | Spesifikasi PC untuk kebutuhan tertentu dari katalog komponen | Formulir pilihan komponen + anggaran | Aturan: kompatibilitas soket/RAM, kebutuhan minimum, total ≤ anggaran |
| W2 | Struktur folder proyek | Pohon folder di simulator + jawaban path absolut/relatif | Keadaan pohon; path cocok |
| W3 | Rencana alamat jaringan rumah | Tabel perangkat: IP, subnet, gateway | Semua IP valid, unik, satu subnet, gateway dalam rentang |
| W4 | Rencana keamanan akun pribadi | Klasifikasi skenario ancaman + daftar tindakan | Klasifikasi cocok kunci; tindakan wajib ada |
| W5 | Tabel anggaran belajar | Tabel total, persentase, pembulatan yang ditentukan | Nilai eksak |
| W6 | Rangkaian logika alarm | Tabel kebenaran + ekspresi Boolean | Ekuivalen di semua kombinasi input |
| W7 | Dekomposisi tugas jadwal belajar | Langkah, pola, abstraksi terstruktur | Struktur dan urutan valid (CE-S3) |
| W8 | Algoritma nilai maksimum | Flowchart + trace table | Trace table eksak; jalur flowchart benar pada fixture |
| W9 | Kalkulator konversi satuan | Program Python | Test I/O (runtime NOT VERIFIED) |
| W10 | Pengolah profil teks (jumlah field tetap, tanpa perulangan atau percabangan) | Program Python (konversi, string, list, dict) | Test I/O |
| W11 | Penentu kategori nilai | Program Python dengan kondisi | Test termasuk batas (mis. 74/75) |
| W12 | Rekap nilai + perbaikan bug | Program dengan fungsi dan loop; program rusak yang diperbaiki | Test fungsi dan test regresi bug |
| W13 | Laporan toko | 5 query SQL | Perbandingan hasil SQ-4–SQ-6 |
| W14 | Halaman profil statis | HTML + CSS | Properti HT-2–HT-3 |
| W15 | Riwayat proyek dengan branch | Keadaan repositori simulasi | K1 = 60: ≥ 4 commit di `main` (10); branch `fitur` dibuat dari `main` (10); `fitur` memiliki ≥ 1 commit sendiri (10); `fitur` di-merge ke `main` (10); konflik pada `README.txt` diselesaikan tanpa penanda `<<<<<<<`/`=======`/`>>>>>>>` (10); isi berkas di commit `main` terakhir sama dengan isi yang diminta (10) |

Rekomendasi CU2-O4: **MR-A + MR-1–MR-7 + brief A.3 sebagai arah.** Alasan
pendidikan: satu struktur rubrik memudahkan pelajar memahami harapan;
kebenaran fungsional dominan sesuai sifat praktik. Implikasi teknis: setiap
kriteria memakai pemeriksa yang sama dengan lab; tidak ada penilaian manual.

AC: RB-AC-01 — setiap kriteria punya metode evaluasi offline tertulis;
RB-AC-02 — tidak ada kriteria yang bergantung pada pernyataan pelajar;
RB-AC-03 — total poin integer dan ≤ 10.000.

---

## B. CU-9 — Rubrik capstone (mini-project modul 16)

### B.1 Tujuan dan deliverable (usulan)

Tema: **"Pencatat Sesi Belajar"** — program Python yang membaca data sesi
belajar berformat teks (`tanggal;modul;menit`), memvalidasi baris, dan
menghasilkan rekap per modul; dilengkapi query SQL atas data yang sama,
README terstruktur, riwayat Git, dan penjelasan terstruktur.

| ID | Deliverable |
|---|---|
| CD-1 | Program Python dengan fungsi wajib bertanda tangan tetap: `parse_line(baris)`, `validasi(record)`, `total_per_modul(records)`, `buat_laporan(records)`. Validasi memakai metode string (mis. `isdigit`, `split`, `len`) dan kondisi; **tidak** memerlukan `try`/`except` (tidak diajarkan W9–W12) |
| CD-2 | Tiga query SQL atas skema fixture B.1a: Q1 total menit per modul; Q2 modul tanpa sesi (`LEFT JOIN`); Q3 tiga tanggal dengan total menit terbanyak |
| CD-3 | README terstruktur (formulir): tujuan, cara pakai, contoh input, contoh output, keterbatasan |
| CD-4 | Repositori simulasi Git (GS-A): ≥ 3 commit, satu branch fitur yang di-merge ke `main`, tanpa penanda konflik |
| CD-5 | 5 soal penjelasan terstruktur tentang **tugas capstone** (desain dan alur `buat_laporan`), format D-23; bukan soal komponen Concept W16 |

### B.1a Skema fixture SQL capstone (usulan)

```
modul(kode TEXT PRIMARY KEY,          -- 'W01' … 'W16' (16 baris)
      nama TEXT NOT NULL)
sesi (id INTEGER PRIMARY KEY,
      tanggal TEXT NOT NULL,           -- 'YYYY-MM-DD'
      kode_modul TEXT NOT NULL REFERENCES modul(kode),
      menit INTEGER NOT NULL CHECK (menit > 0))
```

| Query | Hasil yang diharapkan | Urutan |
|---|---|---|
| Q1 | `kode_modul`, `total_menit` (= `SUM(menit)`) untuk modul yang punya sesi | `ORDER BY kode_modul ASC` (unik → urutan penuh) |
| Q2 | `kode`, `nama` dari `modul` tanpa baris `sesi` (`LEFT JOIN … WHERE sesi.id IS NULL`) | `ORDER BY kode ASC` |
| Q3 | `tanggal`, `total_menit` per tanggal; 3 teratas | `ORDER BY total_menit DESC, tanggal ASC LIMIT 3` — tie-break tanggal paling awal; fixture memuat seri tepat di peringkat 3 agar tie-break teruji |

Semua nilai bilangan bulat; tidak ada bilangan real. Fixture tersembunyi
memakai skema sama dengan data berbeda (CP-3).

### B.2 Rubrik (100 poin)

| Kriteria | Poin | Metode evaluasi offline |
|---|---|---|
| CR-1 Kebenaran fungsional | 35 | Test tersembunyi terhadap `buat_laporan` dengan fixture standar dan fixture variasi (7 test × 5 poin) |
| CR-2 Dasar pemrograman | 15 | Test unit perilaku fungsi wajib CD-1: `parse_line` 4, `validasi` 4, `total_per_modul` 4, `buat_laporan` 3. Test membuktikan **perilaku** fungsi, **bukan** bahwa kode memakai perulangan atau kondisi; pemeriksaan struktur kode butuh analisis kode (mekanisme NOT VERIFIED) dan tidak diusulkan |
| CR-3 Pengolahan data | 20 | Python, 5 kasus × 2 poin: baris kosong, kolom kurang, menit bukan angka, tanggal salah format, data kosong (10); SQL CD-2: query 1 = 3, query 2 = 4, query 3 = 3 (10) |
| CR-4 Dokumentasi | 10 | Field README wajib terisi sesuai format (2 poin per field); kualitas tulisan tidak dinilai |
| CR-5 Alur kerja Git | 10 | Keadaan repositori simulasi: ≥ 3 commit di `main` (3); branch fitur dengan ≥ 1 commit di-merge ke `main` (3); tidak ada penanda konflik di berkas mana pun pada commit `main` terakhir (2); berkas `program.py` pada commit `main` terakhir **identik byte demi byte** (setelah normalisasi akhir baris ke `\n`) dengan program CD-1 yang diserahkan (2) |
| CR-6 Penjelasan proyek | 10 | CD-5 dengan aturan D-23; komposisi K-A (5 × CE-S1, P = 2) atau komposisi lain yang berjumlah tepat 10 (A.2a) |

Catatan: CR-6 adalah bagian rubrik capstone (komponen Mini-project W16).
Hubungan berkas final dan commit (CR-5 butir 4, MC-3) diperiksa objektif
dengan perbandingan isi berkas, bukan pernyataan pelajar.
Komponen Concept explanation W16 (10%) tetap terpisah dan dinilai sendiri.

### B.3 Kriteria wajib capstone

| ID | Kriteria wajib |
|---|---|
| MC-1 | Semua test inti CR-1 (3 test yang ditandai inti) lulus |
| MC-2 | Program berjalan tanpa error pada fixture standar |
| MC-3 | `program.py` pada commit `main` terakhir identik dengan program yang diserahkan (CR-5 butir 4) |
| MC-4 | README memuat semua field wajib |

### B.4 Gerbang capstone vs kelulusan modul

| Opsi | Kelulusan modul 16 (aturan biasa) | Capstone "memenuhi rubrik" (D-19) |
|---|---|---|
| CG-A | Skor terbaik setiap komponen W16 ≥ 75 dan W ≥ 80 | Sama dengan komponen Mini-project W16 ≥ 75; tanpa kriteria wajib |
| **CG-B** | Sama (tidak berubah) | Ada **setidaknya satu attempt capstone selesai** dengan skor ≥ 75 **dan** MC-1–MC-4 terpenuhi pada attempt yang sama |
| CG-C | Sama | Hanya attempt dengan skor terbaik yang diperiksa terhadap MC |

CG-B memisahkan dua aturan secara eksplisit: kelulusan **modul** 16 tetap
memakai skor terbaik per komponen (D-12); gerbang **capstone** memeriksa
kriteria wajib pada attempt yang memenuhinya. CG-C dapat menghukum pelajar
bila attempt dengan skor tertinggi kebetulan gagal satu kriteria wajib
padahal attempt lain memenuhi semuanya.

Contoh (diperiksa `4·e` vs `3·m`, m = 100):

| Attempt | Skor | MC | Komponen ≥ 75 | Gerbang capstone (CG-B) |
|---|---|---|---|---|
| A — dapat diterima | 80 | Semua terpenuhi | `320 ≥ 300` ya | **Terpenuhi** |
| B — tidak dapat diterima | 85 | MC-1 gagal (1 test inti gagal) | `340 ≥ 300` ya → dihitung untuk kelulusan modul | Tidak terpenuhi → program belum selesai; remedial capstone |
| C — tidak dapat diterima | 70 | Semua terpenuhi | `280 < 300` tidak | Tidak terpenuhi |
| D — batas | 75 | Semua terpenuhi | `300 ≥ 300` ya | Terpenuhi |

Riwayat B lalu A: skor terbaik komponen = 85 (attempt B) untuk kelulusan
modul; gerbang capstone terpenuhi oleh attempt A. Program selesai bila ke-16
modul `PASSED` dan gerbang terpenuhi (D-19).

### B.5 Aturan lain

| ID | Aturan (usulan) |
|---|---|
| CP-1 | Kredit parsial per test/field/query sesuai tabel B.2; poin bilangan bulat |
| CP-2 | Remedial: attempt baru dari salinan submission sebelumnya (MPV-A); semua attempt disimpan |
| CP-3 | Fixture tersembunyi berbeda dari contoh agar keluaran yang dikodekan langsung gagal |
| CP-4 | Bagian Python dapat diterima sebagai perencanaan sebelum runtime (RM:RV-1); eksekusi NOT VERIFIED |
| CP-5 | Capstone tidak menambah modul atau jam (5 jam di W16, CU2-O3) |
| CP-6 | Selama gerbang capstone (CG-B) belum terpenuhi, attempt capstone **selalu** dapat dimulai, termasuk bila W16 sudah `PASSED` — terlepas dari keputusan OP-10-Q2 (PI-A/PI-B) |

Rekomendasi CU-9: **tema B.1, skema B.1a, rubrik B.2, MC-1–MC-4, CG-B, CP-1–CP-6.**
Alasan pendidikan: capstone menggabungkan Python (W9–W12), SQL (W13), dan
Git (W15) dengan dokumentasi; kriteria wajib memastikan inti program benar,
bukan hanya mengumpulkan poin dari bagian pinggir. Implikasi teknis: hanya
pemeriksa yang sama dengan lab; tanda tangan fungsi tetap memungkinkan test
unit objektif.

AC: RB-AC-04 — perbedaan gerbang capstone dan kelulusan modul tertulis;
RB-AC-05 — contoh B.4 dapat dihitung ulang; RB-AC-06 — tidak ada kriteria
subjektif.

## C. Pertanyaan untuk owner

| ID | Pertanyaan | Rekomendasi |
|---|---|---|
| CU2-O4-Q1 | Rubrik mini-project MR-A (60/20/10/10) dengan MR-1–MR-8 dan pemetaan anggaran tetap A.2a? | MR-A |
| CU2-O4-Q2 | Brief A.3 sebagai arah produksi W1–W15? | Ya |
| CU-9-Q1 | Tema, deliverable B.1, dan skema fixture SQL B.1a? | Ya |
| CU-9-Q2 | Rubrik B.2 dan kriteria wajib MC-1–MC-4? | Ya |
| CU-9-Q3 | Gerbang capstone CG-B (attempt ≥ 75 dengan semua MC terpenuhi), terpisah dari kelulusan modul 16? | CG-B |
| CU-9-Q4 | CP-6: attempt capstone tetap tersedia setelah W16 `PASSED` selama gerbang belum terpenuhi? | Ya |

Status: **AWAITING OWNER**.
