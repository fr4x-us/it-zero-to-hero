# IT ZERO → HERO — Matriks Cakupan Kompetensi W1–W8 (D-39)

Status: **dokumentasi** · audit statis butir · bukan verifikasi runtime atau
uji pelajar. Dibuat oleh generator `docs/validation/build_matrix.py` dari
`coverage_data.py` (pembacaan butir oleh penyusun) dan berkas butir nyata.
Kontrak: **D-39 HYBRID COMPETENCY COVERAGE** ([DECISIONS_LOG.md](DECISIONS_LOG.md)).

## 1. Metode

- **Konsep wajib** = `required_concepts` setiap slot concept (6 slot × 8
  modul); generator memastikan daftar sama persis dengan berkas (tidak ada
  konsep yang dihapus atau diubah, D-39 no. 10).
- **Kelas**: *inti* = dinyatakan langsung dalam teks LO slot (`module.yaml`);
  *pendukung* = dibutuhkan LO tetapi tidak disebut langsung. Klasifikasi
  disusun penyusun, belum dikonfirmasi owner.
- **Dinilai** hanya bila pelajar harus menunjukkan konsep itu untuk
  memperoleh poin: setiap opsi pilihan majemuk (CE-S2/TF-2), pasangan kiri
  (CE-S4), item urutan (CE-S3), baris salah + perbaikan (CE-S5), kunci
  pilihan tunggal (CE-S1/TF-1), isian (TF-3, lab), atau pemeriksaan proyek.
  Tidak dihitung: stem, pengecoh pilihan tunggal, baris CE-S5 yang benar,
  umpan balik, pelajaran, remedial, latihan opsional, refleksi tanpa skor.
- **Jalur penilaian**: VA-2 memilih varian per slot dari riwayat pemakaian
  komponen yang sama untuk semua slot → setiap attempt satu komponen memakai
  indeks varian yang sama (A, lalu B, bergiliran); lab RA-1 per komponen.
  Komponen saling bebas (skor terbaik per komponen, D-12); proyek tanpa
  varian (MPV-A). Jalur sah = {A, B} teori × {A, B} concept × {A, B} lab.
- **Dua lapis bukti (R4-03).** (1) **Bukti semantik** bahwa sebuah lokasi
  benar-benar menilai konsep adalah **penilaian penulis** yang dicatat di
  `coverage_data.py` (kolom "semantik kuat/lemah"); generator **tidak**
  membuktikannya, hanya memastikan setiap lokasi yang dirujuk ada (berkas,
  varian, ID pemeriksaan/kriteria) dan mencatat jenis kriterianya (kunci
  pilihan tunggal, setiap opsi dinilai, isian, urutan, pemeriksaan lab/proyek,
  kunci K4). (2) **Bukti jalur** (matematis) bahwa anotasi itu menjangkau
  setiap jalur pelajar sah dihitung generator.
- **Bukti jalur QC-13** (R3-01): (a) cukup bila satu lokasi wajib menilai
  konsep di semua varian yang dapat dipilih, atau proyek; (b) juga sah bila
  gabungan lokasi dalam **satu** komponen menutup semua indeks varian
  komponen itu. Bukti (b) hanya dipakai karena VA-2 (D-30) menjamin indeks
  varian yang sama untuk semua slot pada setiap attempt komponen: riwayat
  pemakaian semua slot identik karena setiap attempt memuat semua slot
  (blueprint teori 20 slot; concept 6 slot; lab RA-1). Generator
  mensimulasikan VA-2 (8 attempt × 20 slot → A, B, A, B, … untuk semua slot).
  Konsep yang memakai bukti (b): **1**. Aturan pemilihan tidak diubah.
- **Status**: PASS bila bukti jalur terpenuhi dengan lokasi berbukti
  semantik **kuat**; OPEN bila hanya terpenuhi dengan bukti semantik
  **lemah**; GAP bila tidak terpenuhi.
- **Remedial**: bukti berlaku untuk setiap indeks varian, jadi setiap
  attempt remedial (VA-2/VA-3, tanpa batas) tetap tercakup.
- Uji metode (dijalankan generator): hanya varian A → GAP; varian A di dua
  komponen → GAP; lab di kedua varian → PASS; varian A + B di dua slot satu
  komponen → PASS dengan bukti (b); hanya bukti semantik lemah → OPEN.

## 2. Ringkasan cakupan — HASIL PENULIS, belum diverifikasi independen

| Modul | Konsep wajib | PASS | GAP | OPEN |
|---|---|---|---|---|
| W1 | 19 | 19 | 0 | 0 |
| W2 | 24 | 24 | 0 | 0 |
| W3 | 20 | 18 | 0 | 2 |
| W4 | 20 | 19 | 0 | 1 |
| W5 | 21 | 21 | 0 | 0 |
| W6 | 19 | 19 | 0 | 0 |
| W7 | 14 | 14 | 0 | 0 |
| W8 | 19 | 19 | 0 | 0 |
| **Total** | **156** | **153** | **0** | **3** |

Riwayat: baseline `a644d61` — 15 GAP (W1 1, W2 8, W3 2, W4 3, W6 1) →
dikoreksi putaran 3. Putaran 4 (review `4ddc993`): R3-04 = koreksi bukti
saja; R3-05, R3-06, R3-07 = bukti penolakan opsi tidak cukup, butir
direvisi minimum; R3-03 = isu keselamatan prosedur dikoreksi. Putaran 5
(review `796043c`, R4-03): proyek K4.q3 dihapus sebagai bukti salin; tiga
baris hanya berbukti semantik lemah kini **OPEN**. GAP: **0**; OPEN:
**3** (usulan koreksi di §7, menunggu otorisasi owner). Putaran 6
(otorisasi owner): 4 varian concept direvisi untuk kesetaraan; cakupan tetap 153/3/0.

Kesetaraan akademik varian (R3-02/R4-04–R4-09, §6; penilaian penulis): **47 PASS**,
**1 OPEN** dari 48 slot. Cakupan modul dan kesetaraan varian adalah syarat terpisah.

## 3. Koreksi butir untuk cakupan dan kesetaraan (D-39, putaran 3–4 dan 6)

| Modul | Varian | Perubahan | Konsep | Kunci | Versi |
|---|---|---|---|---|---|
| W1 | teori s10 vB | `16 bit = … byte` | 1 byte = 8 bit | 2 | 2.0 |
| W2 | concept s01 vA | L1 `Kernel` | kernel | L1→R3 | 2.0 |
| W2 | teori s02 vB | opsi c (giliran CPU), e (driver) | manajemen proses, perangkat | a, c, e | 2.0 |
| W2 | teori s05 vA | stem + kunci a (belum disimpan hilang) | yang belum disimpan hilang | a | 2.0 |
| W2 | teori s09 vB | opsi b (aplikasi pembuka) | ekstensi memilih aplikasi | b, c, d | 2.0 |
| W2 | teori s17 vB | langkah 4 pulihkan; opsi b/d ditukar | pulihkan | b | 2.0 |
| W2 | concept s05 vA | simulasi; periksa **seluruh** isi Tempat Sampah sebelum mengosongkan (R3-03) | periksa sebelum menghapus permanen | A B C D | 3.0 |
| W2 | concept s05 vB | idem langkah D (R3-03) | idem | A B C D | 2.0 |
| W2 | concept s06 vB | opsi c (akun administrator) | akun biasa vs admin | b, d | 2.0 |
| W3 | concept s02 vB | opsi e: "tidak dapat berbagi satu alamat publik" (R3-05) | NAT berbagi alamat publik | a, c, d | 3.0 |
| W3 | teori s08 vB | host tersisa setelah router | 254 host | 253 | 2.0 |
| W4 | concept s02 vB | opsi a (phishing = RS); opsi e "belum membuktikan" (R3-06) | phishing RS; tanda bukan bukti | b, c, e | 3.0 |
| W4 | concept s04 vA | kunci b memuat arti HTTPS | HTTPS bukan bukti identitas | b | 2.0 |
| W4 | concept s05 vA | stem "pernyataan yang benar"; opsi b satu klaim (R3-07) | perlindungan tidak menjamin | a, c | 3.0 |
| W6 | concept s05 vB | opsi e (urutan baris standar) | urutan baris standar | b, c, e | 2.0 |
| W3 | concept s03 vB (R6) | baris salah 4: "2⁸ − 1 = 255" host → 254; baris keanggotaan kini benar | 254 host | 4 + b | 2.0 |
| W4 | concept s03 vB (R6) | baris salah 2: PIN 4 digit "40" → 10.000; baris MFA kini benar (sandi + PIN = dua faktor "yang diketahui") | kombinasi ×10 per digit | 2 + b | 2.0 |
| W7 | concept s02 vB (CB-2, R6) | baris salah 3: 3, 9, 27, 81 "bertambah tetap 6" → berlipat tiga | berlipat | 3 + c | 2.0 |
| W7 | concept s03 vB (CB-2, R6) | skenario formulir lomba lari: menyaring informasi menurut tujuan | menyaring informasi menurut tujuan | d | 2.0 |

Format, poin, kompetensi, dan distribusi posisi kunci setiap modul tidak
berubah (`check_keys.py`, snapshot = baseline `4ddc993`). Varian W1–W4 di
atas **belum diterima** (TPL-01a `acceptance.revised_variants`, PENDING).

## 4. Register temuan reviewer putaran 3 (ID sementara; F-73–F-94 asli tidak tersedia)

| ID | Temuan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R3-01 | Metode bukti QC-13 terlalu sempit | DOCUMENTATION CLARIFIED (QC-13 a/b, TPL-13, §1) | YA | BELUM |
| R3-02 | Kesetaraan 96/96 tanpa register | DOCUMENTATION CLARIFIED (§6, 48 slot; OPEN dilaporkan) | YA | BELUM |
| R3-03 | W2 concept s05: mengosongkan seluruh Tempat Sampah setelah memeriksa satu berkas | CONFIRMED — FIXED (vA, vB; simulasi) | YA | BELUM |
| R3-04 | Bukti "salin mempertahankan asal" pada teori s17 vA tidak sah | CONFIRMED (bukti) — matriks dikoreksi; *putaran 4 menyebut proyek K4.q3; dikoreksi R4-03*: bukti (b) teori s15 vA + s17 vB | YA | BELUM |
| R3-05 | NAT: penolakan opsi tidak menuntut konsep berbagi | CONFIRMED — FIXED (W3 concept s02 vB opsi e) | YA | BELUM |
| R3-06 | Tanda vs bukti: vB opsi e tidak menuntut "bukan bukti" | CONFIRMED — FIXED (W4 concept s02 vB opsi e) | YA | BELUM |
| R3-07 | Pernyataan majemuk W4 concept s05 vA opsi b | CONFIRMED — FIXED (tidak ada lokasi wajib lain; opsi dijadikan satu klaim) | YA | BELUM |
| R3-08 | Status penerimaan hanya di komentar YAML | CONFIRMED — FIXED (TPL-01a `acceptance`, `check_acceptance.py`) | YA | BELUM |
| PR28-06 | Cakupan `required_concepts` | D-39 dicatat; audit penulis; **tetap OPEN**: 3 baris cakupan berbukti lemah; kesetaraan OPEN 5 → 1 slot (W4 concept s01) setelah putaran 6 | SEBAGIAN | BELUM |
| PR28-02 | NB-5 | Paket reproduksi `docs/validation/` | YA | BELUM (PARTIAL PASS independen) |

## 4b. Register temuan reviewer putaran 4 (ID sementara R4-xx)

| ID | Temuan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R4-01 | `docs/PROJECT_MAP.md` kosong (putaran 4) | CONFIRMED — FIXED: dipulihkan dari `4ddc993` + pembaruan status; `check_docs.py` | YA | BELUM |
| R4-02 | Validator penerimaan berasumsi versi 1.0 | CONFIRMED — FIXED: perbandingan isi terhadap `baseline_commit` git; 12 uji (9 mutasi terdeteksi) | YA | BELUM |
| R4-03 | Bukti semantik vs bukti jalur; K4.q3 untuk salin | CONFIRMED — FIXED: dua lapis bukti, validasi referensi, simulasi VA-2; 3 baris OPEN | YA | BELUM |
| R4-04–R4-06, R4-09 | Kesetaraan varian | CONFIRMED — register manual 48 slot; 5 OPEN; usulan koreksi §7 (tidak diterapkan) | SEBAGIAN | BELUM |
| R4-07 | Provenance SHA tidak konsisten | CONFIRMED — FIXED: lihat `docs/validation/README.md` | YA | BELUM |
| R4-08 | Validasi snapshot bersih | CONFIRMED — FIXED: `run_all.py --official` + `test_provenance.py` | YA | BELUM |
| R4-10 | Kategori klaim validasi | CONFIRMED — FIXED: label HITUNG/REGRESI/STRUKTUR/SEMANTIK | YA | BELUM |

## 4c. Register temuan reviewer putaran 5 dan otorisasi putaran 6 (ID sementara R5-xx)

| ID | Temuan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R6-A | Otorisasi owner: W3 concept s03 vB, W4 concept s03 vB, W7 concept s02 vB, W7 concept s03 vB | APPLIED — versi 1.0 → 2.0; posisi kunci per modul tidak berubah; konsep yang dipindah dijamin lokasi wajib lain (lihat §6 dan kolom elemen) | YA | BELUM |
| R5-01 | Granularitas rujukan bukti cakupan | CONFIRMED — FIXED: kolom elemen bernilai tepat (ID opsi/pasangan/item urutan, baris salah + koreksi, kunci, isian, ID pemeriksaan lab, kriteria proyek); `coverage_elements.py`; validasi keberadaan + kelayakan dinilai; 11 uji positif/negatif | YA | BELUM |
| R5-02 | Peran router/switch hanya berbukti lemah | NOT APPLIED (tidak diotorisasi) — lokasi wajib alternatif diperiksa: tidak ada; usulan diperbaiki §7; baris tetap OPEN | SEBAGIAN | BELUM |
| R5-03 | Usulan W4 teori s10 vA opsi e menghilangkan konsep sandi mudah ditebak | CONFIRMED — usulan lama ditarik; usulan baru §7 mempertahankan keduanya (tidak diterapkan); OTP tetap OPEN | SEBAGIAN | BELUM |
| R5-04 | NB-5 untuk konten cacat | CONFIRMED — FIXED: `nb5_content_errors()`; konten cacat → CONTENT_ERROR, isian bukan teks → EVALUATION_ERROR; 16 fixture + 112 kombinasi tanpa exception | YA | BELUM |
| R5-05 | Validator penerimaan mengabaikan field slot bersama | CONFIRMED — FIXED: field tingkat berkas dibandingkan dengan baseline; perubahan bersama menandai semua varian berkas; 22 uji (18 mutasi terdeteksi); 16 varian W1–W4 PENDING | YA | BELUM |

## 7. Usulan koreksi butir — MENUNGGU OTORISASI OWNER (tidak diterapkan)

Usulan yang sudah diterapkan atas otorisasi putaran 6 (W3 concept s03 vB,
W4 concept s03 vB, W7 concept s02 vB, W7 concept s03 vB) dipindah ke §3.

| Slot | Masalah dan bukti | Usulan | Dampak dan batas |
|---|---|---|---|
| W3 concept s01 vA (diterima historis) — R5-02 | Peran router dan switch hanya berbukti lemah. Lokasi wajib alternatif diperiksa: teori s01 TF-1 kunci vA *Access point*, vB *Router* (Switch hanya pengecoh); lab act-03.c01 vA *Router*, vB *Access point*; teori s03 Switch hanya pengecoh; proyek K4.q1 menyebut "bagian switch/access point" hanya di kunci tanpa pembeda fungsi (lemah). Router vB (teori) + vA (lab) berada di komponen berbeda → bukan bukti (b) VA-2. | vA kunci b: "Laptop dan printer berada di LAN yang sama; fungsi switch/access point meneruskan data di dalam LAN, sedangkan fungsi router hanya diperlukan untuk menuju jaringan lain seperti internet". Ganti pengecoh d dengan peran tertukar: "Fungsi router meneruskan data di dalam LAN, sedangkan fungsi switch menghubungkan LAN ke internet". | CE-S1 hanya kunci dihitung; pengecoh peran tertukar membuat pemilihan kunci menuntut pembedaan fungsi. vB kunci d menyebut router saja; agar *peran switch* berbukti kuat di vB juga diperlukan revisi vB (kunci menyebut "switch hanya meneruskan di dalam LAN") — butuh otorisasi terpisah. Posisi kunci tetap. Penilaian semantik = review independen. |
| W4 teori s10 vA (diterima historis) — R5-03 | Usulan lama (ganti opsi e "tanggal lahir") ditarik: opsi e adalah **satu-satunya** elemen bernilai W4 untuk sandi yang mudah ditebak dari data pribadi (lab act-03 vB c02 opsi c hanya pengecoh pilihan tunggal). | **Opsi 1 (tanpa ubah konten, kandidat bukti)**: jalur (b) VA-2 teori s12 vA kunci a ("Pesan memintamu mengirim kode OTP" = tanda phishing terkuat) + teori s10 vB opsi d (salah, dinilai). Perlu putusan semantik independen: s12 vA menilai pengenalan permintaan OTP sebagai phishing, belum tentu larangan membagikan. **Opsi 2 (ubah konten)**: vA ganti opsi d benar "Mengaktifkan MFA bila tersedia" dengan opsi benar "Tidak memberikan OTP kepada siapa pun, termasuk penelepon yang mengaku petugas"; kunci {a, c, d} dan opsi e tetap. | Opsi 2 kehilangan kebiasaan "aktifkan MFA" di vA (bukan required concept; faktor MFA dijamin lab act-03.c02 vA+vB). Kedua opsi tidak diterapkan; baris "OTP tidak dibagikan" tetap **OPEN**. |
| W4 concept s01 vA (diterima historis) — usulan final | vA pemetaan istilah → definisi; vB kejadian → istilah. | vA menjadi kejadian → istilah dengan kejadian berbeda dari vB: L1 "Foto KTP pelanggan terlihat oleh orang yang tidak berhak" → R3 Kerahasiaan; L2 "Nilai rapor di server sekolah diganti tanpa izin" → R5 Integritas; L3 "Aplikasi bank tidak dapat dipakai selama server gangguan" → R1 Ketersediaan; L4 "Kode dari aplikasi autentikator diperiksa sebelum akun dibuka" → R2 Autentikasi; R4 pengecoh "Pencadangan data". | Pemetaan kunci {L1→R3, L2→R5, L3→R1, L4→R2} tidak berubah; 4 konsep wajib tetap dinilai per pasangan; kesetaraan tetap OPEN sampai diotorisasi dan direview. |

Setiap usulan akan mengubah varian butir (versi naik; W1–W4 tercatat PENDING
di TPL-01a) dan memerlukan otorisasi owner sebelum diterapkan.

## 5. Matriks per konsep

| Modul | LO | Slot | Konsep wajib | Kelas | Concept (elemen bernilai) | Lokasi wajib lain [elemen bernilai] | Jaminan jalur (QC-13) | Remedial | Bukti/catatan | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| W1 | LO3 | s01 | RAM volatil | inti | vA kunci b | theory s09 [vA kunci a; vB kunci b] (kunci pilihan tunggal; semantik kuat) | (a) theory s09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO3 | s01 | penyimpanan non-volatil | inti | vB kunci d | theory s09 [vA kunci a; vB kunci b] (kunci pilihan tunggal; semantik kuat) | (a) theory s09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO3 | s01 | akibat listrik mati | pendukung | vA kunci b; vB kunci d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO2 | s02 | core | inti | vA opsi dinilai b; vB opsi dinilai a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO2 | s02 | pekerjaan yang dapat dibagi vs berurutan | inti | vA opsi dinilai d; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | firmware bekerja sebelum sistem operasi | inti | vA item urutan B; vB item urutan B | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | POST | pendukung | vA item urutan B; vB item urutan B | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | perangkat boot | pendukung | vA item urutan C; vB item urutan C | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | bootloader memuat ke RAM | pendukung | vA item urutan D; vB item urutan D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO1 | s04 | dua tahap IPOS | inti | vA pasangan L1,L2; vB pasangan L1,L2 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO1 | s04 | dua istilah dasar (hardware/software atau data/informasi) | inti | vA pasangan L3,L4; vB pasangan L3,L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO4 | s05 | 1 byte = 8 bit | pendukung | — | theory s10 [vA isian 8; vB isian 2] (isian; semantik kuat) | (a) theory s10 | sama (VA-2 bergiliran) | D-39: teori s10 vB diubah (16 bit = 2 byte) | PASS |
| W1 | LO4 | s05 | aturan desimal ×1.000 | inti | vA baris salah 3 + koreksi c; vB baris salah 4 + koreksi b | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO4 | s05 | konversi GB–MB | inti | vA baris salah 3 + koreksi c; vB baris salah 4 + koreksi b | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | soket | pendukung | vA opsi dinilai a; vB opsi dinilai b | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | jenis RAM | pendukung | vA opsi dinilai c; vB opsi dinilai a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | jumlah slot | pendukung | vA opsi dinilai b; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | daya PSU | pendukung | vA opsi dinilai e; vB opsi dinilai e | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | semua syarat dan anggaran | inti | vA opsi dinilai d; vB opsi dinilai d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | manajemen proses | inti | — | theory s02 [vA opsi dinilai a; vB opsi dinilai c] (setiap opsi dinilai; semantik kuat) | (a) theory s02 | sama (VA-2 bergiliran) | D-39: concept s01 vA L1 → Kernel; teori s02 vB opsi c | PASS |
| W2 | LO1 | s01 | manajemen memori | inti | vA pasangan L2; vB pasangan L2 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | manajemen perangkat | inti | vA pasangan L3 | theory s02 [vA opsi dinilai c; vB opsi dinilai e] (setiap opsi dinilai; semantik kuat); theory s03 [vA kunci d] (kunci pilihan tunggal; semantik kuat) | (a) theory s02 | sama (VA-2 bergiliran) | D-39: teori s02 vB opsi e | PASS |
| W2 | LO1 | s01 | manajemen file | inti | vB pasangan L1 | project K4.q4 [kunci K4.q4] (kunci K4; semantik kuat); theory s02 [vB opsi dinilai a] (setiap opsi dinilai; semantik kuat); theory s03 [vB kunci c] (kunci pilihan tunggal; semantik kuat) | (a) project K4.q4 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | antarmuka pengguna | inti | vA pasangan L4; vB pasangan L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | kernel | pendukung | vA pasangan L1; vB pasangan L3 | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s01 vA L1 → Kernel | PASS |
| W2 | LO2 | s02 | proses memakai RAM sendiri | pendukung | vA kunci b; vB kunci d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO2 | s02 | mengakhiri proses mengembalikan RAM | inti | vA kunci b | theory s05 [vA kunci a; vB kunci d] (kunci pilihan; semantik kuat) | (a) theory s05 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO2 | s02 | yang belum disimpan hilang | inti | vA kunci b | theory s05 [vA kunci a; vB kunci d] (kunci pilihan; semantik kuat) | (a) theory s05 | sama (VA-2 bergiliran) | D-39: teori s05 vA (stem + kunci) | PASS |
| W2 | LO2 | s02 | proses lain tetap berjalan | inti | vB kunci d | theory s05 [vA kunci a; vB kunci d] (kunci pilihan; semantik kuat) | (a) theory s05 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO3 | s03 | ekstensi dari titik terakhir | inti | vB opsi dinilai b,c | theory s08 [vA isian csv; vB isian docx] (isian; semantik kuat) | (a) theory s08 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO3 | s03 | ekstensi memilih aplikasi pembuka | pendukung | vA opsi dinilai b,d | theory s09 [vA opsi dinilai a; vB opsi dinilai b] (setiap opsi dinilai; semantik kuat) | (a) theory s09 | sama (VA-2 bergiliran) | D-39: teori s09 vB opsi b | PASS |
| W2 | LO3 | s03 | isi tidak berubah saat ekstensi diganti | inti | vA opsi dinilai a,c; vB opsi dinilai d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | path absolut diawali / | inti | vA baris salah 4 + koreksi a; vB baris salah 3 + koreksi c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | .. naik satu tingkat | inti | vA baris salah 4 + koreksi a; vB baris salah 3 + koreksi c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | path relatif dari folder kerja | inti | vA baris salah 4 + koreksi a; vB baris salah 3 + koreksi c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | huruf besar/kecil dibedakan | pendukung | — | project K3.c01–c02 [kriteria K3.c01,K3.c02] (pemeriksaan proyek; semantik kuat) | (a) project K3.c01–c02 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO5 | s05 | Tempat Sampah | inti | vA item urutan A,D; vB item urutan D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO5 | s05 | pulihkan | inti | vA item urutan B | theory s17 [vA kunci a; vB kunci b] (kunci pilihan; semantik kuat) | (a) theory s17 | sama (VA-2 bergiliran) | D-39: teori s17 vB langkah 4 → pulihkan | PASS |
| W2 | LO5 | s05 | salin mempertahankan asal | inti | — | theory s15 [vA kunci c] (kunci pilihan tunggal; semantik kuat); theory s17 [vB kunci b] (kunci pilihan; semantik kuat) | (b) berkorelasi VA-2 dalam komponen: theory | sama (VA-2 bergiliran) | R4-03: teori s15 vA (kunci Salin: tetap ada di asal) + s17 vB (salin berhasil, asal tetap) — bukti (b) berkorelasi VA-2; proyek K4.q3 dihapus (salin hanya pengecoh) | PASS |
| W2 | LO5 | s05 | periksa sebelum menghapus permanen | pendukung | vA item urutan C; vB item urutan B,D | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39 + R3-03: kedua varian memeriksa seluruh isi Tempat Sampah sebelum dikosongkan | PASS |
| W2 | LO6 | s06 | hak minimum | inti | vA opsi dinilai c; vB opsi dinilai d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO6 | s06 | izin sesuai fungsi | inti | vB opsi dinilai b,d | theory s18 [vA kunci b; vB kunci c] (kunci pilihan tunggal; semantik kuat) | (a) theory s18 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO6 | s06 | akun biasa vs admin | pendukung | vA opsi dinilai a; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s06 vB opsi c | PASS |
| W3 | LO1 | s01 | LAN vs internet | inti | vA kunci b | project K4.q1 [kunci K4.q1] (kunci K4; semantik kuat) | (a) project K4.q1 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO1 | s01 | peran router | inti | vB kunci d | lab act-03.c01 [vA act-03.c01] (pemeriksaan lab; semantik kuat); theory s01 [vB kunci c] (kunci pilihan tunggal; semantik kuat); project K4.q2 [kunci K4.q2] (kunci K4; semantik lemah) | (a) project K4.q2 — hanya dengan bukti semantik lemah | sama (VA-2 bergiliran) | R4-03: lab vA dan teori vB berada di komponen berbeda; jaminan hanya lewat kunci K4.q2 ("router memakai alamat publik dari ISP") — bukti semantik lemah | OPEN |
| W3 | LO1 | s01 | peran switch | inti | vB kunci d | project K4.q1 [kunci K4.q1] (kunci K4; semantik lemah) | (a) project K4.q1 — hanya dengan bukti semantik lemah | sama (VA-2 bergiliran) | R4-03: peran switch hanya disebut dalam kurung pada kunci K4.q1 — bukti semantik lemah | OPEN |
| W3 | LO2 | s02 | rentang privat | inti | vA opsi dinilai a,d; vB opsi dinilai a,d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO2 | s02 | alamat publik dari ISP | inti | vB opsi dinilai c | project K4.q2 [kunci K4.q2] (kunci K4; semantik kuat) | (a) project K4.q2 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO2 | s02 | NAT berbagi alamat publik | pendukung | vA opsi dinilai e; vB opsi dinilai e | — | (a) concept slot concept | sama (VA-2 bergiliran) | R3-05: vB opsi e kini menyatakan "tidak dapat berbagi satu alamat publik" (salah); vA opsi e benar | PASS |
| W3 | LO3 | s03 | alamat jaringan | inti | — | lab act-02.c01 [vA act-02.c01; vB act-02.c01] (pemeriksaan lab; semantik kuat) | (a) lab act-02.c01 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO3 | s03 | broadcast | inti | — | lab act-02.c02 [vA act-02.c02; vB act-02.c02] (pemeriksaan lab; semantik kuat) | (a) lab act-02.c02 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO3 | s03 | 254 host | inti | vA baris salah 3 + koreksi a; vB baris salah 4 + koreksi b | theory s08 [vA isian 254; vB isian 253] (isian; semantik kuat) | (a) concept slot concept; theory s08 | sama (VA-2 bergiliran) | D-39: teori s08 vB; putaran 6: concept s03 vB baris salah jumlah host | PASS |
| W3 | LO3 | s03 | satu jaringan = tiga oktet pertama sama | inti | — | lab act-02.c06–c08 [vA act-02.c06–c08; vB act-02.c06–c08] (pemeriksaan lab; semantik kuat) | (a) lab act-02.c06–c08 | sama (VA-2 bergiliran) | putaran 6: concept s03 vB tidak lagi menilai keanggotaan; dijamin lab act-02.c06–c08 | PASS |
| W3 | LO4 | s04 | DHCP | inti | vA pasangan L1; vB pasangan L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO4 | s04 | DNS | inti | vA pasangan L2; vB pasangan L3 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO4 | s04 | HTTP/HTTPS | inti | vA pasangan L3; vB pasangan L2 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO4 | s04 | TCP vs UDP | inti | vA pasangan L4; vB pasangan L1 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | urutan lapisan | inti | vA item urutan B,C,D; vB item urutan B,C,D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | pembungkusan/membuka bungkus | inti | vA item urutan B,C,D; vB item urutan B,C,D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | port di transport | pendukung | vA item urutan B; vB item urutan D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | alamat IP di internet | pendukung | vA item urutan C; vB item urutan C | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO6 | s06 | bit vs byte (× 8) | inti | vA opsi dinilai a,d; vB opsi dinilai a,b,d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO6 | s06 | model ideal vs nyata | pendukung | vA opsi dinilai b,c; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | kerahasiaan | inti | vA pasangan L1; vB pasangan L2 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | integritas | inti | vA pasangan L2; vB pasangan L1 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | ketersediaan | inti | vA pasangan L3; vB pasangan L3 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | autentikasi bukan tujuan CIA | pendukung | vA pasangan L4; vB pasangan L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO2 | s02 | phishing sebagai rekayasa sosial | inti | vA opsi dinilai a; vB opsi dinilai a | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s02 vB opsi a | PASS |
| W4 | LO2 | s02 | trojan menyamar | inti | vA opsi dinilai c; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO2 | s02 | tanda bukan bukti pasti | pendukung | vA opsi dinilai e; vB opsi dinilai e | — | (a) concept slot concept | sama (VA-2 bergiliran) | R3-06: vB opsi e kini "…belum membuktikan pesannya pasti phishing" (benar); vA opsi e | PASS |
| W4 | LO3 | s03 | faktor berbeda jenis | inti | — | lab act-03.c02 [vA act-03.c02; vB act-03.c02] (pemeriksaan lab; semantik kuat) | (a) lab act-03.c02 | sama (VA-2 bergiliran) | putaran 6: concept s03 vB kini baris salah PIN; MFA dijamin lab act-03.c02 | PASS |
| W4 | LO3 | s03 | OTP tidak dibagikan | pendukung | — | project K1.c02 [kriteria K1.c02] (pemeriksaan proyek; semantik lemah); theory s10 [vB opsi dinilai d] (setiap opsi dinilai; semantik kuat) | (a) project K1.c02 — hanya dengan bukti semantik lemah | sama (VA-2 bergiliran) | R4-03: K1.c02 menilai klasifikasi S2 (penelepon meminta OTP) sebagai rekayasa sosial, bukan larangan membagikan OTP secara langsung; K4.q5 (kanal resmi) dihapus sebagai bukti — bukti semantik lemah | OPEN |
| W4 | LO3 | s03 | kombinasi ×10 per digit | inti | vA baris salah 3 + koreksi a; vB baris salah 2 + koreksi b | theory s09 [vA isian 10000; vB isian 100000] (isian; semantik kuat); lab act-03.c03 [vA act-03.c03; vB act-03.c03] (pemeriksaan lab; semantik kuat) | (a) concept slot concept; theory s09; lab act-03.c03 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO3 | s03 | sandi unik | inti | — | theory s10 [vA opsi dinilai b; vB opsi dinilai b] (setiap opsi dinilai; semantik kuat) | (a) theory s10 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO4 | s04 | domain terdaftar menunjukkan pengendali nama | inti | vA kunci b; vB kunci a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO4 | s04 | subdomain/path dapat menipu | inti | vA kunci b | theory s13 [vA isian verifikasi-akun.test; vB isian login-bankcontoh.test] (isian; semantik kuat) | (a) theory s13 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO4 | s04 | HTTPS = sambungan terenkripsi ke nama domain, bukan bukti identitas organisasi atau kejujuran | pendukung | vA kunci b; vB kunci a | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s04 vA kunci b | PASS |
| W4 | LO5 | s05 | 3 salinan, 2 media, 1 di luar lokasi | inti | vA opsi dinilai c | theory s16 [vA kunci d; vB kunci c] (kunci pilihan tunggal; semantik kuat); project K1.c15 [kriteria K1.c15] (pemeriksaan proyek; semantik kuat) | (a) theory s16; project K1.c15 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO5 | s05 | perangkat sama tidak dihitung | pendukung | vA opsi dinilai a | project K1.c16 [kriteria K1.c16] (pemeriksaan proyek; semantik kuat); theory s16 [vB kunci c] (kunci pilihan tunggal; semantik kuat) | (a) project K1.c16 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO5 | s05 | perlindungan tidak menjamin | inti | vA opsi dinilai b; vB opsi dinilai a,b | — | (a) concept slot concept | sama (VA-2 bergiliran) | R3-07: vA opsi b kini satu klaim ("menjamin data tidak akan pernah hilang", salah) dalam stem "pernyataan yang benar"; vB opsi b benar | PASS |
| W4 | LO6 | s06 | hentikan → amankan (pelaporan dapat dilakukan lebih awal atau bersamaan) | inti | vA item urutan A,B,C; vB item urutan A,B | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO6 | s06 | kanal resmi | pendukung | — | project K4.q5 [kunci K4.q5] (kunci K4; semantik kuat) | (a) project K4.q5 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO6 | s06 | prasyarat antarlangkah | inti | vA item urutan A,B; vB item urutan A,B | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | urutan operasi | inti | vA pasangan L1; vB pasangan L3 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | kurung | inti | vA pasangan L2,L4; vB pasangan L2,L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | kiri ke kanan untuk operasi setara | inti | vA pasangan L3; vB pasangan L1 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | pangkat | pendukung | vB pasangan L3,L4 | theory s06 [vA isian 31; vB isian 11] (isian; semantik kuat); lab act-01.c03 [vA act-01.c03; vB act-01.c03] (pemeriksaan lab; semantik kuat) | (a) theory s06; lab act-01.c03 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W5 | LO2 | s02 | variabel | inti | vA opsi dinilai a,e; vB opsi dinilai a,e | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO2 | s02 | substitusi | inti | vA opsi dinilai b; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO2 | s02 | pangkat | inti | vA opsi dinilai c; vB opsi dinilai b | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO2 | s02 | rata-rata | inti | vA opsi dinilai d; vB opsi dinilai d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | hasil bagi | inti | vA baris salah 4 + koreksi a; vB baris salah 2 + koreksi d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | sisa | inti | vA baris salah 4 + koreksi a; vB baris salah 2 + koreksi d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | sisa < pembagi | pendukung | vA baris salah 4 + koreksi a; vB baris salah 2 + koreksi d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | hasil bagi × pembagi + sisa | pendukung | vA baris salah 4 + koreksi a; vB baris salah 2 + koreksi d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO4 | s04 | 1 jam = 60 menit (bukan 100) | pendukung | vA kunci d | theory s11 [vA isian 205; vB isian 160] (isian; semantik kuat); lab act-03.c01 [vA act-03.c01; vB act-03.c01] (pemeriksaan lab; semantik kuat) | (a) theory s11; lab act-03.c01 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W5 | LO4 | s04 | konversi sebelum menulis desimal | inti | vA kunci d; vB kunci c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO4 | s04 | satuan berbeda tidak dijumlahkan langsung | pendukung | vA kunci d; vB kunci c | lab act-03.c01 [vA act-03.c01; vB act-03.c01] (pemeriksaan lab; semantik kuat) | (a) concept slot concept; lab act-03.c01 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO5 | s05 | nilai dasar | inti | vA item urutan A; vB item urutan B | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO5 | s05 | persen → pecahan desimal | inti | vA item urutan B; vB item urutan D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO5 | s05 | urutan perhitungan diskon/kenaikan | inti | vA item urutan C,D; vB item urutan A,C | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO6 | s06 | aturan pembulatan | inti | vA opsi dinilai a,d; vB opsi dinilai b,d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO6 | s06 | pembulatan ke atas untuk kebutuhan | inti | vA opsi dinilai b; vB opsi dinilai a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO6 | s06 | bulatkan di akhir | pendukung | vA opsi dinilai c; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO1 | s01 | bilangan biner | inti | vA pasangan L1; vB pasangan L1 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO1 | s01 | bilangan desimal | inti | vA pasangan L2; vB pasangan L2 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO1 | s01 | nilai Boolean benar/salah | inti | vA pasangan L3,L4; vB pasangan L3,L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO2 | s02 | nomor posisi dari kanan mulai 0 | pendukung | vA item urutan A | theory s02 [vA kunci d; vB kunci b] (kunci pilihan tunggal; semantik kuat) | (a) theory s02 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO2 | s02 | bobot 2^posisi | inti | vA item urutan B; vB item urutan A | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO2 | s02 | jumlahkan bobot bit 1 | inti | vA item urutan C,D; vB item urutan B,C | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO3 | s03 | bobot bit | pendukung | vA baris salah 4 + koreksi d; vB baris salah 3 + koreksi c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO3 | s03 | n bit dengan nol di depan | inti | vA baris salah 4 + koreksi d; vB baris salah 3 + koreksi c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO3 | s03 | nilai terbesar 2ⁿ − 1 | inti | — | lab act-01.c08 [vA act-01.c08; vB act-01.c08] (pemeriksaan lab; semantik kuat); theory s10 [vA kunci c] (kunci pilihan tunggal; semantik kuat); theory s11 [vB isian 127] (isian; semantik kuat) | (a) lab act-01.c08 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W6 | LO4 | s04 | AND = semua 1 | inti | vA kunci b | lab act-02.c05–c06 [vA act-02.c05–c06; vB act-02.c05–c06] (pemeriksaan lab; semantik kuat); project K1.c09 [kriteria K1.c09] (pemeriksaan proyek; semantik kuat) | (a) lab act-02.c05–c06; project K1.c09 | sama (VA-2 bergiliran) | kandidat prioritas | PASS |
| W6 | LO4 | s04 | OR = sedikitnya satu 1 | inti | vB kunci d | lab act-02.c05–c06 [vA act-02.c05–c06; vB act-02.c05–c06] (pemeriksaan lab; semantik kuat); project K1.c09 [kriteria K1.c09] (pemeriksaan proyek; semantik kuat) | (a) lab act-02.c05–c06; project K1.c09 | sama (VA-2 bergiliran) | kandidat prioritas | PASS |
| W6 | LO4 | s04 | NOT membalik | inti | — | lab act-02.c01–c04 [vA act-02.c01–c04; vB act-02.c01–c04] (pemeriksaan lab; semantik kuat); theory s13 [vA isian 0; vB isian 1] (isian; semantik kuat); project K1.c11 [kriteria K1.c11] (pemeriksaan proyek; semantik kuat) | (a) lab act-02.c01–c04; theory s13; project K1.c11 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W6 | LO5 | s05 | 2ⁿ baris | inti | vA opsi dinilai a; vB opsi dinilai a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO5 | s05 | urutan baris standar | inti | vA opsi dinilai b; vB opsi dinilai e | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s05 vB opsi e | PASS |
| W6 | LO5 | s05 | prioritas NOT > AND > OR | inti | vA opsi dinilai c; vB opsi dinilai b | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO5 | s05 | ekuivalen = sama di semua baris | inti | vA opsi dinilai d,e | lab act-03.c05 [vA act-03.c05; vB act-03.c05] (pemeriksaan lab; semantik kuat); theory s20 [vA kunci a; vB kunci d] (kunci pilihan tunggal; semantik kuat) | (a) lab act-03.c05; theory s20 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO6 | s06 | kalimat "dan" → AND | inti | vA opsi dinilai a,b | lab act-03.c03 [vA act-03.c03; vB act-03.c03] (pemeriksaan lab; semantik kuat); project K1.c09 [kriteria K1.c09] (pemeriksaan proyek; semantik kuat) | (a) lab act-03.c03; project K1.c09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO6 | s06 | kalimat "atau" → OR | inti | vB opsi dinilai b,c | lab act-03.c04 [vA act-03.c04; vB act-03.c04] (pemeriksaan lab; semantik kuat); project K1.c09 [kriteria K1.c09] (pemeriksaan proyek; semantik kuat) | (a) lab act-03.c04; project K1.c09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO6 | s06 | ekspresi ekuivalen diterima | pendukung | vA opsi dinilai a,b; vB opsi dinilai b,c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO1 | s01 | bagian mencakup semua kebutuhan | inti | vA opsi dinilai a,b,c; vB opsi dinilai b,c,e | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO1 | s01 | tanpa bagian yang tidak relevan | inti | vA opsi dinilai d,e; vB opsi dinilai a,d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO2 | s02 | bertambah tetap | inti | vA baris salah 3 + koreksi b; vB baris salah 3 + koreksi c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO2 | s02 | berlipat | inti | vA baris salah 3 + koreksi b; vB baris salah 3 + koreksi c | lab act-02.c04 [vA act-02.c04; vB act-02.c04] (pemeriksaan lab; semantik kuat) | (a) concept slot concept; lab act-02.c04 | sama (VA-2 bergiliran) | putaran 6: concept s02 vB baris salah berlipat tiga | PASS |
| W7 | LO2 | s02 | rumus suku ke-n | inti | — | theory s05 [vA isian 41; vB isian 52] (isian; semantik kuat) | (a) theory s05 | sama (VA-2 bergiliran) | putaran 6: dijamin teori s05 (isian) kedua varian | PASS |
| W7 | LO3 | s03 | menyaring informasi menurut tujuan | inti | vA kunci b; vB kunci d | project K1.c11 [kriteria K1.c11] (pemeriksaan proyek; semantik kuat) | (a) concept slot concept; project K1.c11 | sama (VA-2 bergiliran) | putaran 6: concept s03 vB skenario formulir lomba lari | PASS |
| W7 | LO3 | s03 | generalisasi dengan variabel | inti | — | theory s10 [vA kunci c; vB kunci a] (kunci pilihan tunggal; semantik kuat) | (a) theory s10 | sama (VA-2 bergiliran) | putaran 6: dijamin teori s10 (kunci) kedua varian | PASS |
| W7 | LO4 | s04 | jelas/terukur | inti | vA pasangan L1,L4; vB pasangan L1,L3 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO4 | s04 | berakhir | inti | vA pasangan L2; vB pasangan L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO4 | s04 | urutan benar | inti | vA pasangan L3; vB pasangan L2 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO5 | s05 | prasyarat menentukan urutan | inti | vA item urutan A,D; vB item urutan A,D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO5 | s05 | tugas tanpa ketergantungan boleh ditukar | pendukung | vA item urutan B,C; vB item urutan B,C | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO6 | s06 | kasus uji di batas | inti | vA opsi dinilai a,b; vB opsi dinilai a,b,c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO6 | s06 | kesalahan > vs ≥ | inti | vA opsi dinilai c,d; vB opsi dinilai d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | input | inti | vA opsi dinilai a; vB opsi dinilai a,b | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | output | inti | vA opsi dinilai c; vB opsi dinilai d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | asumsi domain | inti | vA opsi dinilai b,e; vB opsi dinilai a,e | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | berhenti | inti | vA opsi dinilai d | theory s11 [vA kunci c; vB kunci a] (kunci pilihan tunggal; semantik kuat) | (a) theory s11 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | oval | inti | vA pasangan L1; vB pasangan L4 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | jajar genjang | inti | vA pasangan L2; vB pasangan L1 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | persegi panjang | inti | vA pasangan L3; vB pasangan L3 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | belah ketupat | inti | vA pasangan L4; vB pasangan L2 | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO3 | s03 | dua cabang | pendukung | vA baris salah 3 + koreksi d; vB baris salah 1 + koreksi a | theory s07 [vA isian 57; vB isian 10] (isian; semantik kuat) | (a) concept slot concept; theory s07 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO3 | s03 | nilai tepat di batas | inti | vA baris salah 3 + koreksi d; vB baris salah 1 + koreksi a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO3 | s03 | > vs ≥ | inti | vA baris salah 3 + koreksi d; vB baris salah 1 + koreksi a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO4 | s04 | variabel pengendali berubah | inti | vA kunci b; vB kunci d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO4 | s04 | syarat berhenti | inti | vA kunci b; vB kunci d | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO5 | s05 | baris penelusuran mengikuti langkah | inti | vA item urutan A,B,C,D; vB item urutan A,B,C,D | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO5 | s05 | nilai lama dipakai sampai diganti | inti | vA item urutan C; vB item urutan C | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | nilai awal | inti | vA opsi dinilai a,b; vB opsi dinilai a | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | nilai negatif | inti | vA opsi dinilai a; vB opsi dinilai c | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | nilai sama | inti | vA opsi dinilai c | theory s19 [vA kunci b; vB kunci c] (kunci pilihan tunggal; semantik kuat) | (a) theory s19 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | satu tes lolos bukan bukti | pendukung | vA opsi dinilai d | project K4.q1 [kunci K4.q1] (kunci K4; semantik kuat) | (a) project K4.q1 | sama (VA-2 bergiliran) | pembacaan butir | PASS |

## 6. Register kesetaraan kompetensi inti (48 slot concept, R3-02)

Register ini adalah **penilaian semantik penulis** (`equivalence_notes.py`), bukan bukti otomatis. Format dan poin maksimum ditetapkan per slot (sama untuk kedua varian); struktur dihitung dari butir. Kesamaan ID kompetensi, format, atau rasio kata **tidak** dipakai sebagai bukti kesetaraan; rasio kata hanya penyaring. Bank concept tidak memiliki field kesulitan atau waktu per varian; durasi tidak diuji pelajar.

| Slot | LO — kompetensi bernilai bersama | Format, poin | Perilaku bernilai vA | Perilaku bernilai vB | Perbandingan tuntutan kognitif | Penyaring kompleksitas/waktu | Versi revisi | Status |
|---|---|---|---|---|---|---|---|---|
| W1 s01 | LO3 — Menjelaskan persistensi data dari sifat volatil/non-volatil | CE-S1, 4 poin (slot) | vA: memilih alasan RAM volatil (isi hilang saat listrik mati) (4 pilihan, 1 kunci) | vB: memilih alasan SSD menyimpan data tanpa listrik (4 pilihan, 1 kunci) | Instans cermin dari aturan yang sama (volatil vs non-volatil); satu penjelasan sebab-akibat | 26 vs 36 kata, rasio 1.38 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s02 | LO2 — Menilai manfaat core tambahan dari sifat pekerjaan | CE-S2, 2 poin (slot) | vA: menilai 4 pernyataan untuk banyak aplikasi bersamaan (4 pernyataan, 2 benar) | vB: menilai 4 pernyataan untuk program berurutan (4 pernyataan, 2 benar) | Aturan "dapat dibagi" diterapkan pada kasus cermin | 60 vs 60 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s03 | LO5 — Mengurutkan proses boot | CE-S3, 4 poin (slot) | vA: mengurutkan 5 langkah boot sampai OS siap (5 langkah, 1 urutan diterima) | vB: mengurutkan 5 langkah boot dari flashdisk instalasi (5 langkah, 1 urutan diterima) | Urutan 5 langkah yang sama; konteks bacaan vB lebih panjang tetapi relevan (review independen: PASS) | 35 vs 67 kata, rasio 1.91 → perlu ditinjau; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s04 | LO1 — Memetakan istilah IPOS dan istilah dasar | CE-S4, 4 poin (slot) | vA: memetakan input, proses, hardware, informasi (4 pasangan, 5 pilihan kanan) | vB: memetakan output, penyimpanan, software, data (4 pasangan, 5 pilihan kanan) | Tugas pemetaan identik pada empat istilah dasar berbeda dengan tingkat yang sama | 34 vs 37 kata, rasio 1.09 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s05 | LO4 — Mendeteksi dan memperbaiki konversi satuan data desimal | CE-S5, 4 poin (slot) | vA: baris salah 1 GB = 100 MB → 1.000 MB (5 baris, 4 perbaikan) | vB: baris salah 500 GB = 50.000 MB → 500.000 MB (5 baris, 4 perbaikan) | Kesalahan faktor ×1.000 yang sama; vB satu langkah perkalian lebih | 70 vs 65 kata, rasio 1.08 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s06 | LO6 — Menilai syarat kompatibilitas rakitan | CE-S2, 3 poin (slot) | vA: menilai 5 pernyataan soket/RAM/slot/PSU/anggaran (5 pernyataan, 3 benar) | vB: menilai 5 pernyataan soket/RAM/slot/PSU/anggaran (5 pernyataan, 3 benar) | Konsep dan struktur sama | 54 vs 54 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s01 | LO1 — Memetakan fungsi dan istilah sistem operasi | CE-S4, 4 poin (slot) | vA: memetakan kernel, memori, perangkat, antarmuka (4 pasangan, 5 pilihan kanan) | vB: memetakan file, memori, kernel, antarmuka (4 pasangan, 5 pilihan kanan) | Tugas pemetaan sama; tiga dari empat istilah sama | 47 vs 47 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 2.0 | PASS |
| W2 s02 | LO2 — Menjelaskan akibat mengakhiri proses dari model "proses punya RAM sendiri" | CE-S1, 4 poin (slot) | vA: memilih alasan tulisan belum disimpan hilang (4 pilihan, 1 kunci) | vB: memilih alasan proses lain tetap berjalan (4 pilihan, 1 kunci) | Dua akibat cermin dari model yang sama; satu penjelasan | 57 vs 50 kata, rasio 1.14 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s03 | LO3 — Menafsirkan makna ekstensi berkas | CE-S2, 3 poin (slot) | vA: menilai pernyataan ganti ekstensi (isi tetap, aplikasi pembuka) (5 pernyataan, 3 benar) | vB: menilai pernyataan ekstensi tersembunyi (titik terakhir, isi tetap, exe) (5 pernyataan, 3 benar) | Berbagi konsep yang dinilai langsung "isi tidak berubah" di kedua varian; satu konsep berbeda masing-masing dengan bobot setara | 52 vs 55 kata, rasio 1.06 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s04 | LO4 — Menafsirkan path relatif terpendek | CE-S5, 4 poin (slot) | vA: baris salah `/Musik` → `../Musik` (5 baris, 4 perbaikan) | vB: baris salah `../../sampul.png` → `../sampul.png` (5 baris, 4 perbaikan) | Keterampilan sama (menghitung naik tingkat dan membedakan absolut/relatif) | 62 vs 57 kata, rasio 1.09 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s05 | LO5 — Mengurutkan operasi berkas yang aman | CE-S3, 3 poin (slot) | vA: pulihkan → periksa seluruh Tempat Sampah → kosongkan (simulasi) (4 langkah, 1 urutan diterima) | vB: salin → verifikasi → hapus → periksa lalu kosongkan (simulasi) (4 langkah, 1 urutan diterima) | Prinsip sama: verifikasi sebelum langkah permanen; 4 langkah, satu urutan | 53 vs 74 kata, rasio 1.40 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 3.0, vB 2.0 | PASS |
| W2 s06 | LO6 — Menerapkan prinsip hak minimum | CE-S2, 2 poin (slot) | vA: menilai alasan memakai akun biasa (4 pernyataan, 2 benar) | vB: menilai izin aplikasi senter dan akun administrator (4 pernyataan, 2 benar) | Aturan hak minimum diterapkan pada akun vs izin; keduanya memuat penilaian akun administrator setelah D-39 | 63 vs 54 kata, rasio 1.17 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W3 s01 | LO1 — Menjelaskan batas LAN–internet dan peran perangkat | CE-S1, 4 poin (slot) | vA: memilih alasan pencetakan LAN tetap jalan tanpa internet (4 pilihan, 1 kunci) | vB: memilih alasan router diperlukan untuk ke internet (4 pilihan, 1 kunci) | Penalaran batas jaringan yang sama dari dua sisi (lalu lintas lokal vs antarjaringan) | 47 vs 41 kata, rasio 1.15 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W3 s02 | LO2 — Menilai pernyataan alamat privat/publik | CE-S2, 3 poin (slot) | vA: menilai 5 pernyataan (rentang privat, unik, NAT) (5 pernyataan, 3 benar) | vB: menilai 5 pernyataan (rentang privat, ISP, NAT) (5 pernyataan, 3 benar) | Konsep dan struktur sama | 45 vs 56 kata, rasio 1.24 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 3.0 | PASS |
| W3 s03 | LO3 — Menerapkan aturan subnet /24 | CE-S5, 4 poin (slot) | vA: baris salah: jumlah host 256 → 254 (hitung) (5 baris, 4 perbaikan) | vB: baris salah v2.0: jumlah host 2⁸ − 1 = 255 → 254 (hitung) (5 baris, 4 perbaikan) | Ronde 6: vB 2.0 kini menilai perhitungan jumlah host yang sama (kurangi alamat jaringan dan broadcast); keanggotaan jaringan pindah ke lab act-02.c06–c08 (vA+vB). Kesetaraan = penilaian penulis; menunggu review independen | 47 vs 52 kata, rasio 1.11 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W3 s04 | LO4 — Memetakan protokol ke fungsi | CE-S4, 4 poin (slot) | vA: memetakan DHCP, DNS, HTTPS, UDP (4 pasangan, 5 pilihan kanan) | vB: memetakan TCP, HTTP, DNS, DHCP (4 pasangan, 5 pilihan kanan) | Tugas pemetaan sama; dua protokol sama | 43 vs 43 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W3 s05 | LO5 — Mengurutkan pembungkusan TCP/IP | CE-S3, 4 poin (slot) | vA: mengurutkan 5 langkah mengirim (5 langkah, 1 urutan diterima) | vB: mengurutkan 5 langkah menerima (5 langkah, 1 urutan diterima) | Instans cermin (bungkus vs buka bungkus) dari model lapisan yang sama | 42 vs 43 kata, rasio 1.02 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W3 s06 | LO6 — Menilai kecepatan bit vs byte dan model ideal | CE-S2, 2 poin (slot) | vA: menilai 4 pernyataan dari 50 Mbps (4 pernyataan, 2 benar) | vB: menilai 4 pernyataan dari 3 MB/s (4 pernyataan, 2 benar) | Konversi ×8 dan ideal vs nyata di kedua varian | 43 vs 40 kata, rasio 1.07 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W4 s01 | LO1 — Mengenali tujuan CIA dan autentikasi | CE-S4, 4 poin (slot) | vA: memetakan istilah → definisi (4 pasangan, 5 pilihan kanan) | vB: memetakan kejadian → istilah (4 pasangan, 5 pilihan kanan) | Konsep sama, tetapi vA pengenalan definisi sedangkan vB klasifikasi skenario; tuntutan kognitif mungkin berbeda (review independen: OPEN) | 42 vs 60 kata, rasio 1.43 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | OPEN |
| W4 s02 | LO2 — Mengenali ancaman dan tanda | CE-S2, 3 poin (slot) | vA: menilai 5 pernyataan (phishing RS, trojan, tanda bukan bukti) (5 pernyataan, 3 benar) | vB: menilai 5 pernyataan (phishing RS, trojan, tanda bukan bukti) (5 pernyataan, 3 benar) | Konsep yang dinilai sama setelah D-39/R3-06 | 42 vs 59 kata, rasio 1.40 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 3.0 | PASS |
| W4 s03 | LO3 — Mendeteksi kesalahan autentikasi | CE-S5, 4 poin (slot) | vA: baris salah: hitung kombinasi PIN 3 digit (10³ = 1.000) (5 baris, 4 perbaikan) | vB: baris salah v2.0: hitung kombinasi PIN 4 digit (10⁴ = 10.000) (5 baris, 4 perbaikan) | Ronde 6: vB 2.0 kini menilai aturan ×10 per digit yang sama; MFA (faktor berbeda jenis) pindah ke lab act-03.c02 (vA+vB). Batas: theory s09 vA juga meminta 10.000 (keterpaparan angka). Penilaian penulis; menunggu review independen | 65 vs 88 kata, rasio 1.35 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W4 s04 | LO4 — Menilai bukti identitas situs | CE-S1, 4 poin (slot) | vA: memilih alasan: domain terdaftar + arti HTTPS (4 pilihan, 1 kunci) | vB: memilih alasan: arti HTTPS untuk nama domain tertentu (4 pilihan, 1 kunci) | Keduanya menuntut membedakan nama domain dari klaim identitas dan arti HTTPS (setelah D-39) | 59 vs 60 kata, rasio 1.02 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 2.0 | PASS |
| W4 s05 | LO5 — Menilai rencana cadangan dan batas perlindungan | CE-S2, 2 poin (slot) | vA: menilai pernyataan salinan di laptop yang sama (3-2-1, perlindungan bukan jaminan) (4 pernyataan, 2 benar) | vB: menilai alasan cadangan tetap perlu (perlindungan bukan jaminan, pemulihan) (4 pernyataan, 2 benar) | Berbagi konsep yang dinilai langsung "perlindungan tidak menjamin" (R3-07); satu konsep berbeda masing-masing | 59 vs 44 kata, rasio 1.34 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 3.0 | PASS |
| W4 s06 | LO6 — Mengurutkan respons insiden hentikan → amankan | CE-S3, 3 poin (slot) | vA: mengurutkan 4 langkah ponsel hilang (4 langkah, 2 urutan diterima) | vB: mengurutkan 4 langkah setelah phishing (4 langkah, 2 urutan diterima) | Struktur urutan dan dua urutan diterima sama (review independen: PASS) | 84 vs 51 kata, rasio 1.65 → perlu ditinjau; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s01 | LO1 — Menghitung dengan urutan operasi | CE-S4, 4 poin (slot) | vA: memetakan 4 ekspresi (kurung, kiri ke kanan) (4 pasangan, 5 pilihan kanan) | vB: memetakan 4 ekspresi (kurung, pangkat) (4 pasangan, 5 pilihan kanan) | Keterampilan sama; satu aturan berbeda per varian, pangkat dijamin di teori s06/lab | 30 vs 26 kata, rasio 1.15 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s02 | LO2 — Menilai pernyataan variabel/ekspresi | CE-S2, 3 poin (slot) | vA: menilai 5 pernyataan (5 pernyataan, 3 benar) | vB: menilai 5 pernyataan (5 pernyataan, 3 benar) | Konsep sama (variabel, substitusi, pangkat, rata-rata) | 47 vs 44 kata, rasio 1.07 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s03 | LO3 — Memeriksa hasil bagi dan sisa | CE-S5, 4 poin (slot) | vA: baris salah 29 ÷ 4 (5 baris, 4 perbaikan) | vB: baris salah 38 ÷ 6 (5 baris, 4 perbaikan) | Keterampilan dan pengecoh (sisa ≥ pembagi) sama | 80 vs 80 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s04 | LO4 — Mengonversi besaran bersatuan campuran | CE-S1, 4 poin (slot) | vA: jam-menit ke desimal jam (4 pilihan, 1 kunci) | vB: kg-g ke gram (4 pilihan, 1 kunci) | Keterampilan konversi sama pada satuan berbeda (LO4: waktu dan massa) | 50 vs 46 kata, rasio 1.09 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s05 | LO5 — Mengurutkan perhitungan persentase dari nilai dasar | CE-S3, 3 poin (slot) | vA: urutan diskon 25% (4 langkah, 2 urutan diterima) | vB: urutan kenaikan 60 → 75 (4 langkah, 2 urutan diterima) | Prosedur nilai dasar sama; dua urutan diterima di kedua varian | 42 vs 38 kata, rasio 1.11 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s06 | LO6 — Menilai aturan pembulatan | CE-S2, 2 poin (slot) | vA: menilai 4 pernyataan (4 pernyataan, 2 benar) | vB: menilai 4 pernyataan (4 pernyataan, 2 benar) | Konsep sama | 47 vs 50 kata, rasio 1.06 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s01 | LO1 — Membedakan biner, desimal, Boolean | CE-S4, 4 poin (slot) | vA: memetakan 4 tulisan (4 pasangan, 5 pilihan kanan) | vB: memetakan 4 tulisan (4 pasangan, 5 pilihan kanan) | Tugas sama | 21 vs 21 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s02 | LO2 — Mengurutkan konversi biner → desimal | CE-S3, 3 poin (slot) | vA: prosedur umum 4 langkah (4 langkah, 1 urutan diterima) | vB: memeriksa `1100₂` 4 langkah (4 langkah, 1 urutan diterima) | Prosedur bobot yang sama; vB konkret | 35 vs 43 kata, rasio 1.23 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s03 | LO3 — Memeriksa biner tepat 8 bit | CE-S5, 4 poin (slot) | vA: baris salah 37 → 00100101 (5 baris, 4 perbaikan) | vB: baris salah 52 → 00110100 (5 baris, 4 perbaikan) | Keterampilan sama | 60 vs 57 kata, rasio 1.05 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s04 | LO4 — Menjelaskan operator Boolean dari definisinya | CE-S1, 4 poin (slot) | vA: alasan AND = 0 (4 pilihan, 1 kunci) | vB: alasan OR = 1 (4 pilihan, 1 kunci) | Instans cermin dari definisi operator (bandingkan review independen W6 s06: PASS) | 45 vs 46 kata, rasio 1.02 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s05 | LO5 — Menilai aturan tabel kebenaran | CE-S2, 3 poin (slot) | vA: menilai 5 pernyataan (5 pernyataan, 3 benar) | vB: menilai 5 pernyataan (5 pernyataan, 3 benar) | Konsep sama setelah D-39 | 51 vs 49 kata, rasio 1.04 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W6 s06 | LO6 — Menerjemahkan aturan ke BX dan mengenali ekspresi ekuivalen | CE-S2, 2 poin (slot) | vA: memilih ekspresi "dan" (4 pernyataan, 2 benar) | vB: memilih ekspresi "atau" (4 pernyataan, 2 benar) | Variasi AND/OR yang wajar (review independen: PASS) | 33 vs 33 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s01 | LO1 — Memilih dekomposisi lengkap tanpa bagian tidak relevan | CE-S2, 3 poin (slot) | vA: memilih sub-masalah lomba (5 pernyataan, 3 benar) | vB: memilih sub-masalah video (5 pernyataan, 3 benar) | Tugas sama | 30 vs 28 kata, rasio 1.07 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s02 | LO2 — Mendeteksi kesalahan pola | CE-S5, 4 poin (slot) | vA: baris salah: jenis pola 1, 2, 4, 8 (berlipat dikira bertambah tetap) (5 baris, 4 perbaikan) | vB: baris salah v2.0: jenis pola 3, 9, 27, 81 (berlipat dikira bertambah tetap) (5 baris, 4 perbaikan) | Ronde 6: vB 2.0 kini menilai klasifikasi jenis pola yang sama; rumus suku ke-n pindah ke theory s05 (TF-3, vA+vB). Penilaian penulis; menunggu review independen | 66 vs 79 kata, rasio 1.20 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W7 s03 | LO3 — Menjelaskan tujuan abstraksi | CE-S1, 4 poin (slot) | vA: alasan menyaring informasi (peta kereta) (4 pilihan, 1 kunci) | vB: alasan v2.0 menyaring informasi menurut tujuan (formulir lomba lari) (4 pilihan, 1 kunci) | Ronde 6: vB 2.0 kini menilai penyaringan informasi menurut tujuan, sama dengan vA (CE-S1); generalisasi dengan variabel pindah ke theory s10 (TF-1, vA+vB). Penilaian penulis; menunggu review independen | 50 vs 75 kata, rasio 1.50 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W7 s04 | LO4 — Menilai kualitas instruksi | CE-S4, 4 poin (slot) | vA: memetakan 4 instruksi (4 pasangan, 5 pilihan kanan) | vB: memetakan 4 instruksi (4 pasangan, 5 pilihan kanan) | Kategori sama | 38 vs 40 kata, rasio 1.05 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s05 | LO5 — Mengurutkan tugas berprasyarat | CE-S3, 3 poin (slot) | vA: 4 tugas, 2 urutan (4 langkah, 2 urutan diterima) | vB: 4 tugas, 2 urutan (4 langkah, 2 urutan diterima) | Struktur sama | 30 vs 29 kata, rasio 1.03 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s06 | LO6 — Memilih kasus uji batas | CE-S2, 2 poin (slot) | vA: aturan ≥ 12 (4 pernyataan, 2 benar) | vB: aturan ≥ 50.000 (4 pernyataan, 2 benar) | Struktur sama | 59 vs 49 kata, rasio 1.20 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s01 | LO1 — Menilai input, output, domain algoritma | CE-S2, 3 poin (slot) | vA: menilai 5 pernyataan pembagian rata (5 pernyataan, 3 benar) | vB: menilai 5 pernyataan konversi detik (5 pernyataan, 3 benar) | Konsep sama | 34 vs 41 kata, rasio 1.21 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s02 | LO2 — Memetakan bentuk flowchart | CE-S4, 4 poin (slot) | vA: bentuk → kegunaan (4 pasangan, 5 pilihan kanan) | vB: isi blok → bentuk (4 pasangan, 5 pilihan kanan) | Arah pemetaan cermin pada tingkat yang sama | 23 vs 25 kata, rasio 1.09 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s03 | LO3 — Menelusuri percabangan di batas | CE-S5, 4 poin (slot) | vA: baris salah x = 10 dengan > (5 baris, 4 perbaikan) | vB: baris salah x = 5 dengan ≤ (5 baris, 4 perbaikan) | Keterampilan sama | 85 vs 85 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s04 | LO4 — Menjelaskan berhentinya perulangan | CE-S1, 4 poin (slot) | vA: alasan tidak berhenti tanpa perubahan (4 pilihan, 1 kunci) | vB: alasan perubahan di dalam perulangan (4 pilihan, 1 kunci) | Instans cermin dari aturan yang sama | 46 vs 39 kata, rasio 1.18 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s05 | LO5 — Menyusun tabel penelusuran | CE-S3, 3 poin (slot) | vA: 4 baris (4 langkah, 1 urutan diterima) | vB: 4 baris (4 langkah, 1 urutan diterima) | Struktur sama | 52 vs 52 kata, rasio 1.00 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s06 | LO6 — Menilai kebenaran algoritma daftar | CE-S2, 2 poin (slot) | vA: nilai awal, negatif, nilai sama, satu tes (4 pernyataan, 2 benar) | vB: nilai awal, daftar kosong, negatif (4 pernyataan, 2 benar) | Berbagi konsep yang dinilai langsung (nilai awal, negatif) | 59 vs 44 kata, rasio 1.34 → tidak ditandai; tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
