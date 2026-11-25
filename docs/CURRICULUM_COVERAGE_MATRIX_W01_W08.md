# IT ZERO → HERO — Matriks Cakupan Kompetensi W1–W8 (D-39)

Status: **dokumentasi** · audit statis butir · bukan verifikasi runtime atau
uji pelajar. Tanggal: **2026-11-25**. Kontrak: **D-39 HYBRID COMPETENCY
COVERAGE** ([DECISIONS_LOG.md](DECISIONS_LOG.md)).

## 1. Metode

- **Konsep wajib** = `required_concepts` setiap slot concept (6 slot × 8 modul).
  Tidak ada konsep yang dihapus atau diubah namanya (aturan D-39 no. 10).
- **Kelas**: *inti* = konsep yang dinyatakan langsung dalam teks LO slot itu
  (`module.yaml`); *pendukung* = konsep lain yang dibutuhkan untuk LO.
- **Dinilai** hanya bila pelajar harus menunjukkan konsep itu untuk memperoleh
  poin pada kriteria bernilai: kunci/pengecoh yang dinilai pada pilihan
  majemuk (CE-S2/TF-2, setiap opsi dinilai), pasangan kiri (CE-S4), item urutan
  (CE-S3), baris salah + perbaikannya (CE-S5), kunci pilihan tunggal
  (CE-S1/TF-1), isian (TF-3, lab), atau pemeriksaan proyek. Baris CE-S5 yang
  benar, pengecoh pilihan tunggal, stem, umpan balik, pelajaran, dan remedial
  **tidak** dihitung.
- **Jalur penilaian**: setiap komponen dipilih per attempt (VA-2: per slot,
  dengan riwayat pemakaian yang sama untuk semua slot komponen → varian A pada
  attempt 1, B pada attempt 2, bergiliran; lab RA-1 untuk seluruh komponen).
  Komponen saling bebas (skor terbaik per komponen, D-12), sehingga jalur =
  {A, B} untuk teori × concept × lab, proyek tanpa varian (MPV-A).
- **Bukti jaminan** (deterministik): konsep PASS bila ada **satu lokasi wajib**
  yang menilainya di **setiap** varian yang dapat dipilih (atau proyek). Bukti
  yang bergantung pada korelasi varian antarslot tidak dipakai (0 konsep).
  Karena bukti berlaku untuk setiap indeks varian, jaminan juga berlaku untuk
  setiap attempt remedial (VA-2/VA-3, tanpa batas).
- Uji metode: konsep hanya di varian A dan tidak ada lokasi lain → **GAP**;
  konsep pendukung tidak ada di satu varian concept tetapi dinilai lab di
  kedua varian → **PASS** (`cov_check.py`, skrip dokumentasi sementara).

## 2. Ringkasan

| Modul | Konsep wajib | PASS | GAP | OPEN |
|---|---|---|---|---|
| W1 | 19 | 19 | 0 | 0 |
| W2 | 24 | 24 | 0 | 0 |
| W3 | 20 | 20 | 0 | 0 |
| W4 | 20 | 20 | 0 | 0 |
| W5 | 21 | 21 | 0 | 0 |
| W6 | 19 | 19 | 0 | 0 |
| W7 | 14 | 14 | 0 | 0 |
| W8 | 19 | 19 | 0 | 0 |
| **Total** | **156** | **156** | **0** | **0** |

Sebelum koreksi D-39 (baseline `a644d61`): **15 GAP** (W1 1, W2 8, W3 2,
W4 3, W6 1). Kandidat prioritas PR28-06 (W5 concept s01 pangkat, s04
60 menit; W6 s03 nilai terbesar, s04 NOT) **PASS tanpa perubahan**: dijamin
lokasi wajib lain di kedua varian.

Kesetaraan inti: setiap varian dari 48 slot concept menilai kompetensi slot
yang sama dan sedikitnya satu konsep inti slot itu (PASS 96/96 varian).

## 3. Koreksi D-39 (celah terbukti)

| Modul | Butir diubah | Konsep yang ditutup | Kunci |
|---|---|---|---|
| W1 | teori s10 vB: `16 bit = … byte` | 1 byte = 8 bit | 2 (dihitung ulang) |
| W2 | concept s01 vA: L1 `Kernel` | kernel | pemetaan tetap L1→R3 |
| W2 | teori s02 vB: opsi c (giliran CPU), e (driver) | manajemen proses, manajemen perangkat | a, c, e (tetap) |
| W2 | teori s05 vA: stem + kunci a (belum disimpan hilang) | yang belum disimpan hilang | a (tetap) |
| W2 | teori s09 vB: opsi b (aplikasi pembuka) | ekstensi memilih aplikasi pembuka | b, c, d (tetap) |
| W2 | teori s17 vB: langkah 4 pulihkan; opsi b/d ditukar | pulihkan | b (posisi tetap; isi dihitung ulang) |
| W2 | concept s05 vA: pulihkan → periksa → kosongkan | periksa sebelum menghapus permanen | satu urutan A B C D |
| W2 | concept s06 vB: opsi c (akun administrator) | akun biasa vs admin | b, d (tetap) |
| W3 | concept s02 vB: opsi e (NAT) | NAT berbagi alamat publik | a, c, d (tetap) |
| W3 | teori s08 vB: host tersisa setelah router | 254 host | 253 (dihitung ulang) |
| W4 | concept s02 vB: opsi a (phishing = rekayasa sosial) | phishing sebagai rekayasa sosial | b, c, e (tetap) |
| W4 | concept s04 vA: kunci b memuat arti HTTPS | HTTPS bukan bukti identitas | b (tetap) |
| W4 | concept s05 vA: opsi b (perlindungan tidak menjamin) | perlindungan tidak menjamin | a, c (tetap) |
| W6 | concept s05 vB: opsi e (urutan baris standar) | urutan baris standar | b, c, e (tetap) |

Format, poin, kesulitan, kompetensi, dan posisi kunci setiap modul tidak
berubah (validator: distribusi posisi kunci identik dengan baseline). Varian
yang diubah memakai `item_version: '2.0'`. Butir W1–W4 yang diubah **tidak**
tercakup penerimaan W01-ACC–W04-ACC dan memerlukan review delta independen.

## 4. Matriks per konsep

| Modul | LO | Slot | Konsep wajib | Kelas | Concept | Lokasi wajib lain | Jaminan jalur | Remedial | Bukti/catatan | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| W1 | LO3 | s01 | RAM volatil | inti | vA | theory s09 (vA+vB) | lokasi tunggal: theory s09 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO3 | s01 | penyimpanan non-volatil | inti | vB | theory s09 (vA+vB) | lokasi tunggal: theory s09 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO3 | s01 | akibat listrik mati | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO2 | s02 | core | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO2 | s02 | pekerjaan yang dapat dibagi vs berurutan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO5 | s03 | firmware bekerja sebelum sistem operasi | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO5 | s03 | POST | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO5 | s03 | perangkat boot | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO5 | s03 | bootloader memuat ke RAM | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO1 | s04 | dua tahap IPOS | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO1 | s04 | dua istilah dasar (hardware/software atau data/informasi) | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO4 | s05 | 1 byte = 8 bit | pendukung | — | theory s10 (vA+vB) | lokasi tunggal: theory s10 | sama (VA-2 bergiliran) | D-39: teori s10 vB diubah (16 bit = 2 byte) | PASS |
| W1 | LO4 | s05 | aturan desimal ×1.000 | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO4 | s05 | konversi GB–MB | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO6 | s06 | soket | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO6 | s06 | jenis RAM | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO6 | s06 | jumlah slot | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO6 | s06 | daya PSU | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W1 | LO6 | s06 | semua syarat dan anggaran | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO1 | s01 | manajemen proses | inti | — | theory s02 (vA+vB) | lokasi tunggal: theory s02 | sama (VA-2 bergiliran) | D-39: concept s01 vA L1 → Kernel; teori s02 vB opsi c | PASS |
| W2 | LO1 | s01 | manajemen memori | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO1 | s01 | manajemen perangkat | inti | vA | theory s02 (vA+vB); theory s03 (vA) | lokasi tunggal: theory s02 | sama (VA-2 bergiliran) | D-39: teori s02 vB opsi e | PASS |
| W2 | LO1 | s01 | manajemen file | inti | vB | project K4.q4 (tanpa varian); theory s02 (vB); theory s03 (vB) | lokasi tunggal: project K4.q4 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO1 | s01 | antarmuka pengguna | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO1 | s01 | kernel | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s01 vA L1 → Kernel | PASS |
| W2 | LO2 | s02 | proses memakai RAM sendiri | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO2 | s02 | mengakhiri proses mengembalikan RAM | inti | vA | theory s05 (vA+vB) | lokasi tunggal: theory s05 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO2 | s02 | yang belum disimpan hilang | inti | vA | theory s05 (vA+vB) | lokasi tunggal: theory s05 | sama (VA-2 bergiliran) | D-39: teori s05 vA (stem + kunci) | PASS |
| W2 | LO2 | s02 | proses lain tetap berjalan | inti | vB | theory s05 (vA+vB) | lokasi tunggal: theory s05 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO3 | s03 | ekstensi dari titik terakhir | inti | vB | theory s08 (vA+vB) | lokasi tunggal: theory s08 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO3 | s03 | ekstensi memilih aplikasi pembuka | pendukung | vA | theory s09 (vA+vB) | lokasi tunggal: theory s09 | sama (VA-2 bergiliran) | D-39: teori s09 vB opsi b | PASS |
| W2 | LO3 | s03 | isi tidak berubah saat ekstensi diganti | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO4 | s04 | path absolut diawali / | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO4 | s04 | .. naik satu tingkat | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO4 | s04 | path relatif dari folder kerja | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO4 | s04 | huruf besar/kecil dibedakan | pendukung | — | project K3.c01–c02 (tanpa varian) | lokasi tunggal: project K3.c01–c02 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO5 | s05 | Tempat Sampah | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO5 | s05 | pulihkan | inti | vA | theory s17 (vA+vB) | lokasi tunggal: theory s17 | sama (VA-2 bergiliran) | D-39: teori s17 vB langkah 4 → pulihkan | PASS |
| W2 | LO5 | s05 | salin mempertahankan asal | inti | vB | theory s17 (vA+vB) | lokasi tunggal: theory s17 | sama (VA-2 bergiliran) | concept s05 vA tidak lagi memuat salin (D-39) | PASS |
| W2 | LO5 | s05 | periksa sebelum menghapus permanen | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s05 vA | PASS |
| W2 | LO6 | s06 | hak minimum | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO6 | s06 | izin sesuai fungsi | inti | vB | theory s18 (vA+vB) | lokasi tunggal: theory s18 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W2 | LO6 | s06 | akun biasa vs admin | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s06 vB opsi c | PASS |
| W3 | LO1 | s01 | LAN vs internet | inti | vA | project K4.q1 (tanpa varian) | lokasi tunggal: project K4.q1 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO1 | s01 | peran router | inti | vB | lab act-03.c01 (vA); theory s01 (vB); project K4.q2 (tanpa varian) | lokasi tunggal: project K4.q2 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO1 | s01 | peran switch | inti | vB | project K4.q1 (tanpa varian) | lokasi tunggal: project K4.q1 | sama (VA-2 bergiliran) | kunci K4.q1 memuat peran switch/access point di LAN | PASS |
| W3 | LO2 | s02 | rentang privat | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO2 | s02 | alamat publik dari ISP | inti | vB | project K4.q2 (tanpa varian) | lokasi tunggal: project K4.q2 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO2 | s02 | NAT berbagi alamat publik | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s02 vB opsi e | PASS |
| W3 | LO3 | s03 | alamat jaringan | inti | — | lab act-02.c01 (vA+vB) | lokasi tunggal: lab act-02.c01 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO3 | s03 | broadcast | inti | — | lab act-02.c02 (vA+vB) | lokasi tunggal: lab act-02.c02 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO3 | s03 | 254 host | inti | vA | theory s08 (vA+vB) | lokasi tunggal: theory s08 | sama (VA-2 bergiliran) | D-39: teori s08 vB (253 tersisa) | PASS |
| W3 | LO3 | s03 | satu jaringan = tiga oktet pertama sama | inti | vB | lab act-02.c06–c08 (vA+vB) | lokasi tunggal: lab act-02.c06–c08 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO4 | s04 | DHCP | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO4 | s04 | DNS | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO4 | s04 | HTTP/HTTPS | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO4 | s04 | TCP vs UDP | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO5 | s05 | urutan lapisan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO5 | s05 | pembungkusan/membuka bungkus | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO5 | s05 | port di transport | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO5 | s05 | alamat IP di internet | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO6 | s06 | bit vs byte (× 8) | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W3 | LO6 | s06 | model ideal vs nyata | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO1 | s01 | kerahasiaan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO1 | s01 | integritas | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO1 | s01 | ketersediaan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO1 | s01 | autentikasi bukan tujuan CIA | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO2 | s02 | phishing sebagai rekayasa sosial | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s02 vB opsi a | PASS |
| W4 | LO2 | s02 | trojan menyamar | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO2 | s02 | tanda bukan bukti pasti | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO3 | s03 | faktor berbeda jenis | inti | vB | lab act-03.c02 (vA+vB) | lokasi tunggal: lab act-03.c02 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO3 | s03 | OTP tidak dibagikan | pendukung | — | project K1.c02 (S2 = SOS), K4.q5 (tanpa varian); theory s10 (vB) | lokasi tunggal: project K1.c02 (S2 = SOS), K4.q5 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO3 | s03 | kombinasi ×10 per digit | inti | vA | theory s09 (vA+vB); lab act-03.c03 (vA+vB) | lokasi tunggal: theory s09, lab act-03.c03 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO3 | s03 | sandi unik | inti | — | theory s10 (vA+vB) | lokasi tunggal: theory s10 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO4 | s04 | domain terdaftar menunjukkan pengendali nama | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO4 | s04 | subdomain/path dapat menipu | inti | vA | theory s13 (vA+vB) | lokasi tunggal: theory s13 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO4 | s04 | HTTPS = sambungan terenkripsi ke nama domain, bukan bukti identitas organisasi atau kejujuran | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s04 vA kunci b | PASS |
| W4 | LO5 | s05 | 3 salinan, 2 media, 1 di luar lokasi | inti | vA | theory s16 (vA+vB); project K1.c15 (tanpa varian) | lokasi tunggal: theory s16, project K1.c15 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO5 | s05 | perangkat sama tidak dihitung | pendukung | vA | project K1.c16 (tanpa varian); theory s16 (vB) | lokasi tunggal: project K1.c16 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO5 | s05 | perlindungan tidak menjamin | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s05 vA opsi b | PASS |
| W4 | LO6 | s06 | hentikan → amankan (pelaporan dapat dilakukan lebih awal atau bersamaan) | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO6 | s06 | kanal resmi | pendukung | — | project K4.q5 (tanpa varian) | lokasi tunggal: project K4.q5 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W4 | LO6 | s06 | prasyarat antarlangkah | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO1 | s01 | urutan operasi | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO1 | s01 | kurung | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO1 | s01 | kiri ke kanan untuk operasi setara | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO1 | s01 | pangkat | pendukung | vB | theory s06 (vA+vB); lab act-01.c03 (vA+vB) | lokasi tunggal: theory s06, lab act-01.c03 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W5 | LO2 | s02 | variabel | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO2 | s02 | substitusi | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO2 | s02 | pangkat | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO2 | s02 | rata-rata | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO3 | s03 | hasil bagi | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO3 | s03 | sisa | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO3 | s03 | sisa < pembagi | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO3 | s03 | hasil bagi × pembagi + sisa | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO4 | s04 | 1 jam = 60 menit (bukan 100) | pendukung | vA | theory s11 (vA+vB); lab act-03.c01 (vA+vB) | lokasi tunggal: theory s11, lab act-03.c01 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W5 | LO4 | s04 | konversi sebelum menulis desimal | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO4 | s04 | satuan berbeda tidak dijumlahkan langsung | pendukung | vA+vB | lab act-03.c01 (vA+vB) | lokasi tunggal: concept concept-slot, lab act-03.c01 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO5 | s05 | nilai dasar | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO5 | s05 | persen → pecahan desimal | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO5 | s05 | urutan perhitungan diskon/kenaikan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO6 | s06 | aturan pembulatan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO6 | s06 | pembulatan ke atas untuk kebutuhan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W5 | LO6 | s06 | bulatkan di akhir | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO1 | s01 | bilangan biner | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO1 | s01 | bilangan desimal | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO1 | s01 | nilai Boolean benar/salah | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO2 | s02 | nomor posisi dari kanan mulai 0 | pendukung | vA | theory s02 (vA+vB) | lokasi tunggal: theory s02 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO2 | s02 | bobot 2^posisi | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO2 | s02 | jumlahkan bobot bit 1 | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO3 | s03 | bobot bit | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO3 | s03 | n bit dengan nol di depan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO3 | s03 | nilai terbesar 2ⁿ − 1 | inti | — | lab act-01.c08 (vA+vB); theory s10 (vA); theory s11 (vB) | lokasi tunggal: lab act-01.c08 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W6 | LO4 | s04 | AND = semua 1 | inti | vA | lab act-02.c05–c06 (vA+vB); project K1.c09 (tanpa varian) | lokasi tunggal: lab act-02.c05–c06, project K1.c09 | sama (VA-2 bergiliran) | kandidat prioritas | PASS |
| W6 | LO4 | s04 | OR = sedikitnya satu 1 | inti | vB | lab act-02.c05–c06 (vA+vB); project K1.c09 (tanpa varian) | lokasi tunggal: lab act-02.c05–c06, project K1.c09 | sama (VA-2 bergiliran) | kandidat prioritas | PASS |
| W6 | LO4 | s04 | NOT membalik | inti | — | lab act-02.c01–c04 (vA+vB); theory s13 (vA+vB); project K1.c11 (tanpa varian) | lokasi tunggal: lab act-02.c01–c04, theory s13, project K1.c11 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W6 | LO5 | s05 | 2ⁿ baris | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO5 | s05 | urutan baris standar | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | D-39: concept s05 vB opsi e | PASS |
| W6 | LO5 | s05 | prioritas NOT > AND > OR | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO5 | s05 | ekuivalen = sama di semua baris | inti | vA | lab act-03.c05 (vA+vB); theory s20 (vA+vB) | lokasi tunggal: lab act-03.c05, theory s20 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO6 | s06 | kalimat "dan" → AND | inti | vA | lab act-03.c03 (vA+vB); project K1.c09 (tanpa varian) | lokasi tunggal: lab act-03.c03, project K1.c09 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO6 | s06 | kalimat "atau" → OR | inti | vB | lab act-03.c04 (vA+vB); project K1.c09 (tanpa varian) | lokasi tunggal: lab act-03.c04, project K1.c09 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W6 | LO6 | s06 | ekspresi ekuivalen diterima | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO1 | s01 | bagian mencakup semua kebutuhan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO1 | s01 | tanpa bagian yang tidak relevan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO2 | s02 | bertambah tetap | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO2 | s02 | berlipat | inti | vA | lab act-02.c04 (vA+vB) | lokasi tunggal: lab act-02.c04 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO2 | s02 | rumus suku ke-n | inti | vB | theory s05 (vA+vB) | lokasi tunggal: theory s05 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO3 | s03 | menyaring informasi menurut tujuan | inti | vA | project K1.c11 (F4) (tanpa varian) | lokasi tunggal: project K1.c11 (F4) | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO3 | s03 | generalisasi dengan variabel | inti | vB | theory s10 (vA+vB) | lokasi tunggal: theory s10 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO4 | s04 | jelas/terukur | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO4 | s04 | berakhir | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO4 | s04 | urutan benar | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO5 | s05 | prasyarat menentukan urutan | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO5 | s05 | tugas tanpa ketergantungan boleh ditukar | pendukung | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO6 | s06 | kasus uji di batas | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W7 | LO6 | s06 | kesalahan > vs ≥ | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO1 | s01 | input | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO1 | s01 | output | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO1 | s01 | asumsi domain | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO1 | s01 | berhenti | inti | vA | theory s11 (vA+vB) | lokasi tunggal: theory s11 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO2 | s02 | oval | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO2 | s02 | jajar genjang | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO2 | s02 | persegi panjang | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO2 | s02 | belah ketupat | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO3 | s03 | dua cabang | pendukung | vA+vB | theory s07 (vA+vB) | lokasi tunggal: concept concept-slot, theory s07 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO3 | s03 | nilai tepat di batas | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO3 | s03 | > vs ≥ | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO4 | s04 | variabel pengendali berubah | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO4 | s04 | syarat berhenti | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO5 | s05 | baris penelusuran mengikuti langkah | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO5 | s05 | nilai lama dipakai sampai diganti | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO6 | s06 | nilai awal | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO6 | s06 | nilai negatif | inti | vA+vB | — | lokasi tunggal: concept concept-slot | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO6 | s06 | nilai sama | inti | vA | theory s19 (vA+vB) | lokasi tunggal: theory s19 | sama (VA-2 bergiliran) | tinjauan butir | PASS |
| W8 | LO6 | s06 | satu tes lolos bukan bukti | pendukung | vA | project K4.q1 (tanpa varian) | lokasi tunggal: project K4.q1 | sama (VA-2 bergiliran) | tinjauan butir | PASS |

Lokasi: `theory sNN` = slot teori modul itu; `lab act-0N.cNN` = pemeriksaan
lab; `project` = kriteria `project/rubric.yaml`. Bacaan per butir dicatat di
register PR28-06 pada `review.md` W1–W8.

