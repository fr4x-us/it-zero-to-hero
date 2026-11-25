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
- **Bukti QC-13** (R3-01): (a) **cukup** bila satu lokasi wajib menilai
  konsep di semua varian yang dapat dipilih, atau proyek; (b) **juga sah**
  bila bukti deterministik setara mencakup setiap jalur sah — di sini:
  gabungan lokasi dalam **satu** komponen menutup semua indeks varian
  komponen itu (varian berkorelasi menurut VA-2). Konsep yang memakai bukti
  (b): **0**. Aturan pemilihan tidak diubah.
- **Remedial**: bukti berlaku untuk setiap indeks varian, jadi setiap
  attempt remedial (VA-2/VA-3, tanpa batas) tetap tercakup.
- Uji metode (dijalankan generator): hanya varian A → GAP; varian A di dua
  komponen → GAP; lab di kedua varian → PASS; varian A + B di dua slot satu
  komponen → PASS dengan bukti (b).

## 2. Ringkasan cakupan (penulis; belum diverifikasi independen)

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

Riwayat: baseline `a644d61` — 15 GAP (W1 1, W2 8, W3 2, W4 3, W6 1) →
dikoreksi putaran 3. Putaran 4 (review `4ddc993`): R3-04 = koreksi bukti
saja; R3-05, R3-06, R3-07 = bukti penolakan opsi tidak cukup, butir
direvisi minimum; R3-03 = isu keselamatan prosedur dikoreksi. GAP saat ini:
**0**.

Kesetaraan kompetensi inti (R3-02, §6): **44 PASS**, **4 OPEN**
dari 48 slot.

## 3. Koreksi butir untuk cakupan (D-39, putaran 3–4)

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

Format, poin, kompetensi, dan distribusi posisi kunci setiap modul tidak
berubah (`check_keys.py`, snapshot = baseline `4ddc993`). Varian W1–W4 di
atas **belum diterima** (TPL-01a `acceptance.revised_variants`, PENDING).

## 4. Register temuan reviewer putaran 3 (ID sementara; F-73–F-94 asli tidak tersedia)

| ID | Temuan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R3-01 | Metode bukti QC-13 terlalu sempit | DOCUMENTATION CLARIFIED (QC-13 a/b, TPL-13, §1) | YA | BELUM |
| R3-02 | Kesetaraan 96/96 tanpa register | DOCUMENTATION CLARIFIED (§6, 48 slot; OPEN dilaporkan) | YA | BELUM |
| R3-03 | W2 concept s05: mengosongkan seluruh Tempat Sampah setelah memeriksa satu berkas | CONFIRMED — FIXED (vA, vB; simulasi) | YA | BELUM |
| R3-04 | Bukti "salin mempertahankan asal" pada teori s17 vA tidak sah | CONFIRMED (bukti) — matriks dikoreksi; cakupan dijamin proyek K4.q3 | YA | BELUM |
| R3-05 | NAT: penolakan opsi tidak menuntut konsep berbagi | CONFIRMED — FIXED (W3 concept s02 vB opsi e) | YA | BELUM |
| R3-06 | Tanda vs bukti: vB opsi e tidak menuntut "bukan bukti" | CONFIRMED — FIXED (W4 concept s02 vB opsi e) | YA | BELUM |
| R3-07 | Pernyataan majemuk W4 concept s05 vA opsi b | CONFIRMED — FIXED (tidak ada lokasi wajib lain; opsi dijadikan satu klaim) | YA | BELUM |
| R3-08 | Status penerimaan hanya di komentar YAML | CONFIRMED — FIXED (TPL-01a `acceptance`, `check_acceptance.py`) | YA | BELUM |
| PR28-06 | Cakupan `required_concepts` | D-39 dicatat; audit dan koreksi penulis | YA | BELUM |
| PR28-02 | NB-5 | Paket reproduksi `docs/validation/` | YA | BELUM (PARTIAL PASS independen) |

## 5. Matriks per konsep

| Modul | LO | Slot | Konsep wajib | Kelas | Concept | Lokasi wajib lain | Jaminan jalur (QC-13) | Remedial | Bukti/catatan | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| W1 | LO3 | s01 | RAM volatil | inti | vA | theory s09 (vA+vB) | (a) theory s09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO3 | s01 | penyimpanan non-volatil | inti | vB | theory s09 (vA+vB) | (a) theory s09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO3 | s01 | akibat listrik mati | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO2 | s02 | core | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO2 | s02 | pekerjaan yang dapat dibagi vs berurutan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | firmware bekerja sebelum sistem operasi | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | POST | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | perangkat boot | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO5 | s03 | bootloader memuat ke RAM | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO1 | s04 | dua tahap IPOS | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO1 | s04 | dua istilah dasar (hardware/software atau data/informasi) | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO4 | s05 | 1 byte = 8 bit | pendukung | — | theory s10 (vA+vB) | (a) theory s10 | sama (VA-2 bergiliran) | D-39: teori s10 vB diubah (16 bit = 2 byte) | PASS |
| W1 | LO4 | s05 | aturan desimal ×1.000 | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO4 | s05 | konversi GB–MB | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | soket | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | jenis RAM | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | jumlah slot | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | daya PSU | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W1 | LO6 | s06 | semua syarat dan anggaran | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | manajemen proses | inti | — | theory s02 (vA+vB) | (a) theory s02 | sama (VA-2 bergiliran) | D-39: concept s01 vA L1 → Kernel; teori s02 vB opsi c | PASS |
| W2 | LO1 | s01 | manajemen memori | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | manajemen perangkat | inti | vA | theory s02 (vA+vB); theory s03 (vA) | (a) theory s02 | sama (VA-2 bergiliran) | D-39: teori s02 vB opsi e | PASS |
| W2 | LO1 | s01 | manajemen file | inti | vB | project K4.q4 (tanpa varian); theory s02 (vB); theory s03 (vB) | (a) project K4.q4 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | antarmuka pengguna | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO1 | s01 | kernel | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s01 vA L1 → Kernel | PASS |
| W2 | LO2 | s02 | proses memakai RAM sendiri | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO2 | s02 | mengakhiri proses mengembalikan RAM | inti | vA | theory s05 (vA+vB) | (a) theory s05 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO2 | s02 | yang belum disimpan hilang | inti | vA | theory s05 (vA+vB) | (a) theory s05 | sama (VA-2 bergiliran) | D-39: teori s05 vA (stem + kunci) | PASS |
| W2 | LO2 | s02 | proses lain tetap berjalan | inti | vB | theory s05 (vA+vB) | (a) theory s05 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO3 | s03 | ekstensi dari titik terakhir | inti | vB | theory s08 (vA+vB) | (a) theory s08 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO3 | s03 | ekstensi memilih aplikasi pembuka | pendukung | vA | theory s09 (vA+vB) | (a) theory s09 | sama (VA-2 bergiliran) | D-39: teori s09 vB opsi b | PASS |
| W2 | LO3 | s03 | isi tidak berubah saat ekstensi diganti | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | path absolut diawali / | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | .. naik satu tingkat | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | path relatif dari folder kerja | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO4 | s04 | huruf besar/kecil dibedakan | pendukung | — | project K3.c01–c02 (tanpa varian) | (a) project K3.c01–c02 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO5 | s05 | Tempat Sampah | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO5 | s05 | pulihkan | inti | vA | theory s17 (vA+vB) | (a) theory s17 | sama (VA-2 bergiliran) | D-39: teori s17 vB langkah 4 → pulihkan | PASS |
| W2 | LO5 | s05 | salin mempertahankan asal | inti | — | project K4.q3 (tanpa varian); theory s15 (vA); theory s17 (vB) | (a) project K4.q3 | sama (VA-2 bergiliran) | R3-04: bukti dikoreksi — proyek K4.q3 (pindah vs salin; pengecoh b = perilaku salin) dan teori s15 vA (kunci Salin) + s17 vB (salin berhasil, asal tetap); concept s05 kini tidak memuat salin | PASS |
| W2 | LO5 | s05 | periksa sebelum menghapus permanen | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39 + R3-03: kedua varian memeriksa seluruh isi Tempat Sampah sebelum dikosongkan | PASS |
| W2 | LO6 | s06 | hak minimum | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO6 | s06 | izin sesuai fungsi | inti | vB | theory s18 (vA+vB) | (a) theory s18 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W2 | LO6 | s06 | akun biasa vs admin | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s06 vB opsi c | PASS |
| W3 | LO1 | s01 | LAN vs internet | inti | vA | project K4.q1 (tanpa varian) | (a) project K4.q1 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO1 | s01 | peran router | inti | vB | lab act-03.c01 (vA); theory s01 (vB); project K4.q2 (tanpa varian) | (a) project K4.q2 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO1 | s01 | peran switch | inti | vB | project K4.q1 (tanpa varian) | (a) project K4.q1 | sama (VA-2 bergiliran) | kunci K4.q1 memuat peran switch/access point di LAN | PASS |
| W3 | LO2 | s02 | rentang privat | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO2 | s02 | alamat publik dari ISP | inti | vB | project K4.q2 (tanpa varian) | (a) project K4.q2 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO2 | s02 | NAT berbagi alamat publik | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | R3-05: vB opsi e kini menyatakan "tidak dapat berbagi satu alamat publik" (salah); vA opsi e benar | PASS |
| W3 | LO3 | s03 | alamat jaringan | inti | — | lab act-02.c01 (vA+vB) | (a) lab act-02.c01 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO3 | s03 | broadcast | inti | — | lab act-02.c02 (vA+vB) | (a) lab act-02.c02 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO3 | s03 | 254 host | inti | vA | theory s08 (vA+vB) | (a) theory s08 | sama (VA-2 bergiliran) | D-39: teori s08 vB (253 tersisa) | PASS |
| W3 | LO3 | s03 | satu jaringan = tiga oktet pertama sama | inti | vB | lab act-02.c06–c08 (vA+vB) | (a) lab act-02.c06–c08 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO4 | s04 | DHCP | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO4 | s04 | DNS | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO4 | s04 | HTTP/HTTPS | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO4 | s04 | TCP vs UDP | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | urutan lapisan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | pembungkusan/membuka bungkus | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | port di transport | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO5 | s05 | alamat IP di internet | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO6 | s06 | bit vs byte (× 8) | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W3 | LO6 | s06 | model ideal vs nyata | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | kerahasiaan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | integritas | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | ketersediaan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO1 | s01 | autentikasi bukan tujuan CIA | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO2 | s02 | phishing sebagai rekayasa sosial | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s02 vB opsi a | PASS |
| W4 | LO2 | s02 | trojan menyamar | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO2 | s02 | tanda bukan bukti pasti | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | R3-06: vB opsi e kini "…belum membuktikan pesannya pasti phishing" (benar); vA opsi e | PASS |
| W4 | LO3 | s03 | faktor berbeda jenis | inti | vB | lab act-03.c02 (vA+vB) | (a) lab act-03.c02 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO3 | s03 | OTP tidak dibagikan | pendukung | — | project K1.c02 (S2 = SOS), K4.q5 (tanpa varian); theory s10 (vB) | (a) project K1.c02 (S2 = SOS), K4.q5 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO3 | s03 | kombinasi ×10 per digit | inti | vA | theory s09 (vA+vB); lab act-03.c03 (vA+vB) | (a) theory s09; lab act-03.c03 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO3 | s03 | sandi unik | inti | — | theory s10 (vA+vB) | (a) theory s10 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO4 | s04 | domain terdaftar menunjukkan pengendali nama | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO4 | s04 | subdomain/path dapat menipu | inti | vA | theory s13 (vA+vB) | (a) theory s13 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO4 | s04 | HTTPS = sambungan terenkripsi ke nama domain, bukan bukti identitas organisasi atau kejujuran | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s04 vA kunci b | PASS |
| W4 | LO5 | s05 | 3 salinan, 2 media, 1 di luar lokasi | inti | vA | theory s16 (vA+vB); project K1.c15 (tanpa varian) | (a) theory s16; project K1.c15 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO5 | s05 | perangkat sama tidak dihitung | pendukung | vA | project K1.c16 (tanpa varian); theory s16 (vB) | (a) project K1.c16 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO5 | s05 | perlindungan tidak menjamin | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | R3-07: vA opsi b kini satu klaim ("menjamin data tidak akan pernah hilang", salah) dalam stem "pernyataan yang benar"; vB opsi b benar | PASS |
| W4 | LO6 | s06 | hentikan → amankan (pelaporan dapat dilakukan lebih awal atau bersamaan) | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO6 | s06 | kanal resmi | pendukung | — | project K4.q5 (tanpa varian) | (a) project K4.q5 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W4 | LO6 | s06 | prasyarat antarlangkah | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | urutan operasi | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | kurung | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | kiri ke kanan untuk operasi setara | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO1 | s01 | pangkat | pendukung | vB | theory s06 (vA+vB); lab act-01.c03 (vA+vB) | (a) theory s06; lab act-01.c03 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W5 | LO2 | s02 | variabel | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO2 | s02 | substitusi | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO2 | s02 | pangkat | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO2 | s02 | rata-rata | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | hasil bagi | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | sisa | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | sisa < pembagi | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO3 | s03 | hasil bagi × pembagi + sisa | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO4 | s04 | 1 jam = 60 menit (bukan 100) | pendukung | vA | theory s11 (vA+vB); lab act-03.c01 (vA+vB) | (a) theory s11; lab act-03.c01 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W5 | LO4 | s04 | konversi sebelum menulis desimal | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO4 | s04 | satuan berbeda tidak dijumlahkan langsung | pendukung | vA+vB | lab act-03.c01 (vA+vB) | (a) concept slot concept; lab act-03.c01 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO5 | s05 | nilai dasar | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO5 | s05 | persen → pecahan desimal | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO5 | s05 | urutan perhitungan diskon/kenaikan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO6 | s06 | aturan pembulatan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO6 | s06 | pembulatan ke atas untuk kebutuhan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W5 | LO6 | s06 | bulatkan di akhir | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO1 | s01 | bilangan biner | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO1 | s01 | bilangan desimal | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO1 | s01 | nilai Boolean benar/salah | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO2 | s02 | nomor posisi dari kanan mulai 0 | pendukung | vA | theory s02 (vA+vB) | (a) theory s02 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO2 | s02 | bobot 2^posisi | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO2 | s02 | jumlahkan bobot bit 1 | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO3 | s03 | bobot bit | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO3 | s03 | n bit dengan nol di depan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO3 | s03 | nilai terbesar 2ⁿ − 1 | inti | — | lab act-01.c08 (vA+vB); theory s10 (vA); theory s11 (vB) | (a) lab act-01.c08 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W6 | LO4 | s04 | AND = semua 1 | inti | vA | lab act-02.c05–c06 (vA+vB); project K1.c09 (tanpa varian) | (a) lab act-02.c05–c06; project K1.c09 | sama (VA-2 bergiliran) | kandidat prioritas | PASS |
| W6 | LO4 | s04 | OR = sedikitnya satu 1 | inti | vB | lab act-02.c05–c06 (vA+vB); project K1.c09 (tanpa varian) | (a) lab act-02.c05–c06; project K1.c09 | sama (VA-2 bergiliran) | kandidat prioritas | PASS |
| W6 | LO4 | s04 | NOT membalik | inti | — | lab act-02.c01–c04 (vA+vB); theory s13 (vA+vB); project K1.c11 (tanpa varian) | (a) lab act-02.c01–c04; theory s13; project K1.c11 | sama (VA-2 bergiliran) | kandidat prioritas: PASS tanpa perubahan | PASS |
| W6 | LO5 | s05 | 2ⁿ baris | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO5 | s05 | urutan baris standar | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | D-39: concept s05 vB opsi e | PASS |
| W6 | LO5 | s05 | prioritas NOT > AND > OR | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO5 | s05 | ekuivalen = sama di semua baris | inti | vA | lab act-03.c05 (vA+vB); theory s20 (vA+vB) | (a) lab act-03.c05; theory s20 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO6 | s06 | kalimat "dan" → AND | inti | vA | lab act-03.c03 (vA+vB); project K1.c09 (tanpa varian) | (a) lab act-03.c03; project K1.c09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO6 | s06 | kalimat "atau" → OR | inti | vB | lab act-03.c04 (vA+vB); project K1.c09 (tanpa varian) | (a) lab act-03.c04; project K1.c09 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W6 | LO6 | s06 | ekspresi ekuivalen diterima | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO1 | s01 | bagian mencakup semua kebutuhan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO1 | s01 | tanpa bagian yang tidak relevan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO2 | s02 | bertambah tetap | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO2 | s02 | berlipat | inti | vA | lab act-02.c04 (vA+vB) | (a) lab act-02.c04 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO2 | s02 | rumus suku ke-n | inti | vB | theory s05 (vA+vB) | (a) theory s05 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO3 | s03 | menyaring informasi menurut tujuan | inti | vA | project K1.c11 (F4) (tanpa varian) | (a) project K1.c11 (F4) | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO3 | s03 | generalisasi dengan variabel | inti | vB | theory s10 (vA+vB) | (a) theory s10 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO4 | s04 | jelas/terukur | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO4 | s04 | berakhir | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO4 | s04 | urutan benar | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO5 | s05 | prasyarat menentukan urutan | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO5 | s05 | tugas tanpa ketergantungan boleh ditukar | pendukung | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO6 | s06 | kasus uji di batas | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W7 | LO6 | s06 | kesalahan > vs ≥ | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | input | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | output | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | asumsi domain | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO1 | s01 | berhenti | inti | vA | theory s11 (vA+vB) | (a) theory s11 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | oval | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | jajar genjang | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | persegi panjang | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO2 | s02 | belah ketupat | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO3 | s03 | dua cabang | pendukung | vA+vB | theory s07 (vA+vB) | (a) concept slot concept; theory s07 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO3 | s03 | nilai tepat di batas | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO3 | s03 | > vs ≥ | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO4 | s04 | variabel pengendali berubah | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO4 | s04 | syarat berhenti | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO5 | s05 | baris penelusuran mengikuti langkah | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO5 | s05 | nilai lama dipakai sampai diganti | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | nilai awal | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | nilai negatif | inti | vA+vB | — | (a) concept slot concept | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | nilai sama | inti | vA | theory s19 (vA+vB) | (a) theory s19 | sama (VA-2 bergiliran) | pembacaan butir | PASS |
| W8 | LO6 | s06 | satu tes lolos bukan bukti | pendukung | vA | project K4.q1 (tanpa varian) | (a) project K4.q1 | sama (VA-2 bergiliran) | pembacaan butir | PASS |

## 6. Register kesetaraan kompetensi inti (48 slot concept, R3-02)

Perilaku bernilai dikutip dari stem dan struktur butir; tuntutan kognitif dinilai penyusun. Format dan poin maksimum ditetapkan per slot (sama untuk kedua varian). Bank concept tidak memiliki field kesulitan atau waktu per varian; beban baca (jumlah kata stem + teks pilihan) dipakai sebagai proksi, bukan bukti waktu pelajar.

| Slot | LO / kompetensi | Format, poin | Perilaku bernilai vA | Perilaku bernilai vB | Tuntutan kognitif | Kesulitan/waktu | Versi revisi | Status |
|---|---|---|---|---|---|---|---|---|
| W1 s01 | LO3 / `comp-w01-mem-01` | CE-S1, 4 poin (slot) | vA: Mengapa RAM disebut **volatil**?… — 4 pilihan, 1 kunci | vB: Mengapa berkas di **SSD** masih ada setelah komputer dimatikan?… — 4 pilihan, 1 kunci | Menjelaskan sifat memori dari akibat listrik mati (vA RAM volatil, vB SSD non-volatil); keduanya memilih penjelasan sebab-akibat | 26 vs 36 kata (rasio 1.38); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s02 | LO2 / `comp-w01-cpu-01` | CE-S2, 2 poin (slot) | vA: CPU 8 core dan CPU 4 core berasal dari generasi dan GHz yang sama. Pilih **semua** alasan… — 4 pernyataan, 2 benar | vB: CPU 8 core dan CPU 4 core berasal dari generasi dan GHz yang sama. Sebuah program mengerja… — 4 pernyataan, 2 benar | Menilai pengaruh jumlah core terhadap beban kerja (vA banyak aplikasi, vB program berurutan); keduanya menerapkan aturan "dapat dibagi" | 60 vs 60 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s03 | LO5 / `comp-w01-sw-01` | CE-S3, 4 poin (slot) | vA: Model boot sederhana W1. Urutkan langkah saat komputer dinyalakan sampai sistem operasi si… — 5 langkah, 1 urutan diterima | vB: Model boot sederhana W1. Flashdisk instalasi sistem operasi sudah dicolokkan **dan sudah d… — 5 langkah, 1 urutan diterima | Mengurutkan 5 langkah boot (vA OS, vB flashdisk instalasi); urutan tunggal yang sama strukturnya | 35 vs 67 kata (rasio 1.91); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | OPEN: beban baca berbeda (35 vs 67 kata) |
| W1 s04 | LO1 / `comp-w01-ipos-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap istilah dengan penjelasannya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap istilah dengan penjelasannya.… — 4 pasangan, 5 pilihan kanan | Memetakan 4 istilah dasar ke definisi (vA input/proses/hardware/informasi, vB output/penyimpanan/software/data) | 34 vs 37 kata (rasio 1.09); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s05 | LO4 / `comp-w01-unit-01` | CE-S5, 4 poin (slot) | vA: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | vB: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | Menemukan baris konversi satuan data yang salah dan memilih perbaikan (vA 1 GB, vB 500 GB) | 70 vs 65 kata (rasio 1.08); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W1 s06 | LO6 / `comp-w01-spec-01` | CE-S2, 3 poin (slot) | vA: Menurut model kompatibilitas W1, pilih **semua** pernyataan yang benar.… — 5 pernyataan, 3 benar | vB: Menurut model kompatibilitas W1, pilih **semua** pernyataan yang benar.… — 5 pernyataan, 3 benar | Menilai 5 pernyataan kompatibilitas rakitan (soket, RAM, slot, PSU, syarat+anggaran) | 54 vs 54 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s01 | LO1 / `comp-w02-os-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap istilah dengan penjelasannya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap istilah dengan penjelasannya.… — 4 pasangan, 5 pilihan kanan | Memetakan 4 fungsi/istilah sistem operasi ke penjelasannya | 47 vs 47 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 2.0 | PASS |
| W2 s02 | LO2 / `comp-w02-proc-01` | CE-S1, 4 poin (slot) | vA: Pengolah kata ini **tidak** punya simpan otomatis atau fitur pemulihan. Mengapa tulisan ya… — 4 pilihan, 1 kunci | vB: Mengapa aplikasi musik **tetap berjalan** setelah kamu mengakhiri proses game yang macet?… — 4 pilihan, 1 kunci | Menjelaskan akibat mengakhiri proses (vA tulisan belum disimpan hilang, vB proses lain tetap berjalan) | 57 vs 50 kata (rasio 1.14); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s03 | LO3 / `comp-w02-fs-01` | CE-S2, 3 poin (slot) | vA: Rudi mengganti nama `foto-kelas.jpg` menjadi `foto-kelas.txt`. Pilih **semua** pernyataan… — 5 pernyataan, 3 benar | vB: Rina melihat berkas tampil sebagai `jadwal.pdf` karena sistem operasinya menyembunyikan ek… — 5 pernyataan, 3 benar | Menilai 5 pernyataan tentang ekstensi pada satu kasus nama berkas | 52 vs 55 kata (rasio 1.06); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s04 | LO4 / `comp-w02-path-01` | CE-S5, 4 poin (slot) | vA: Seorang siswa menulis catatan berikut (model path W2). Satu baris salah. Temukan barisnya… — 5 baris, 4 perbaikan | vB: Seorang siswa menulis catatan berikut (model path W2). Satu baris salah. Temukan barisnya… — 5 baris, 4 perbaikan | Menemukan path relatif yang salah dan memilih perbaikan (`..`) | 62 vs 57 kata (rasio 1.09); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W2 s05 | LO5 / `comp-w02-ops-01` | CE-S3, 3 poin (slot) | vA: Simulasi pengelola berkas (bukan berkas pribadimu): `kontrak.pdf` tidak sengaja dihapus da… — 4 langkah, 1 urutan diterima | vB: Simulasi pengelola berkas (bukan berkas pribadimu): kamu ingin memindahkan folder `Resep`… — 4 langkah, 1 urutan diterima | Mengurutkan 4 langkah operasi berkas yang aman, termasuk memeriksa seluruh isi Tempat Sampah sebelum mengosongkan (simulasi) | 53 vs 74 kata (rasio 1.40); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 3.0, vB 2.0 | PASS |
| W2 s06 | LO6 / `comp-w02-perm-01` | CE-S2, 2 poin (slot) | vA: Pilih **semua** alasan yang benar untuk memakai akun **pengguna biasa** (bukan administrat… — 4 pernyataan, 2 benar | vB: Aplikasi senter meminta izin **kontak** dan **lokasi**. Pilih **semua** pernyataan yang be… — 4 pernyataan, 2 benar | Menilai pernyataan hak minimum (vA akun biasa, vB izin aplikasi) | 63 vs 54 kata (rasio 1.17); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W3 s01 | LO1 / `comp-w03-net-01` | CE-S1, 4 poin (slot) | vA: Mengapa laptop masih dapat mencetak ke printer di LAN rumah saat sambungan internet dari I… — 4 pilihan, 1 kunci | vB: Mengapa rumah memerlukan **router**, bukan hanya switch, agar perangkat dapat membuka situ… — 4 pilihan, 1 kunci | Menjelaskan peran komponen jaringan dari situasi (vA LAN tanpa internet, vB router vs switch) | 47 vs 41 kata (rasio 1.15); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W3 s02 | LO2 / `comp-w03-ip-01` | CE-S2, 3 poin (slot) | vA: Pilih **semua** pernyataan yang benar tentang alamat IP.… — 5 pernyataan, 3 benar | vB: Pilih **semua** pernyataan yang benar tentang alamat IP.… — 5 pernyataan, 3 benar | Menilai 5 pernyataan alamat IP privat/publik/NAT | 45 vs 56 kata (rasio 1.24); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 3.0 | PASS |
| W3 s03 | LO3 / `comp-w03-subnet-01` | CE-S5, 4 poin (slot) | vA: Seorang siswa menulis catatan tentang jaringan `192.168.12.0/24`. Satu baris salah. Temuka… — 5 baris, 4 perbaikan | vB: Seorang siswa menulis catatan tentang jaringan `10.77.5.0/24`. Satu baris salah. Temukan b… — 5 baris, 4 perbaikan | Menemukan baris subnet /24 yang salah dan memilih perbaikan (vA jumlah host, vB keanggotaan jaringan) | 47 vs 67 kata (rasio 1.43); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W3 s04 | LO4 / `comp-w03-proto-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap protokol dengan fungsinya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap protokol dengan fungsinya.… — 4 pasangan, 5 pilihan kanan | Memetakan 4 protokol ke fungsinya | 43 vs 43 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W3 s05 | LO5 / `comp-w03-layer-01` | CE-S3, 4 poin (slot) | vA: Model TCP/IP W3. Urutkan langkah saat laptop **mengirim** permintaan halaman lewat Wi-Fi.… — 5 langkah, 1 urutan diterima | vB: Model TCP/IP W3. Urutkan langkah saat laptop **menerima** halaman lewat kabel LAN.… — 5 langkah, 1 urutan diterima | Mengurutkan 5 langkah lapisan TCP/IP (vA mengirim, vB menerima) | 42 vs 43 kata (rasio 1.02); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W3 s06 | LO6 / `comp-w03-rate-01` | CE-S2, 2 poin (slot) | vA: Paket internet rumah tertulis **50 Mbps**. Pilih **semua** pernyataan yang benar (aturan d… — 4 pernyataan, 2 benar | vB: Aplikasi unduhan menampilkan **3 MB/s**. Pilih **semua** pernyataan yang benar (aturan des… — 4 pernyataan, 2 benar | Menilai 4 pernyataan kecepatan Mbps vs MB/s dan model ideal | 43 vs 40 kata (rasio 1.07); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W4 s01 | LO1 / `comp-w04-cia-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap istilah dengan penjelasannya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap kejadian dengan istilah yang paling tepat (tiga gangguan → tujuan keamanan… — 4 pasangan, 5 pilihan kanan | OPEN: vA memetakan istilah → definisi (ingatan/pemahaman), vB memetakan kejadian → istilah (penerapan/klasifikasi); struktur sama tetapi tuntutan kognitif vB tampak lebih tinggi | 42 vs 60 kata (rasio 1.43); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | OPEN: tuntutan kognitif |
| W4 s02 | LO2 / `comp-w04-threat-01` | CE-S2, 3 poin (slot) | vA: Pilih **semua** pernyataan yang benar tentang ancaman.… — 5 pernyataan, 3 benar | vB: Pilih **semua** pernyataan yang benar tentang ancaman.… — 5 pernyataan, 3 benar | Menilai 5 pernyataan tentang ancaman (rekayasa sosial, trojan, tanda vs bukti) | 42 vs 59 kata (rasio 1.40); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 3.0 | PASS |
| W4 s03 | LO3 / `comp-w04-auth-01` | CE-S5, 4 poin (slot) | vA: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | vB: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | Menemukan baris autentikasi yang salah dan memilih perbaikan (vA hitung kombinasi PIN, vB jenis faktor MFA) | 65 vs 107 kata (rasio 1.65); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | OPEN: beban baca berbeda (65 vs 107 kata) |
| W4 s04 | LO4 / `comp-w04-phish-01` | CE-S1, 4 poin (slot) | vA: Mengapa alamat `https://tokobuku.example.promo-hemat.test/` **tidak** menuju situs resmi `… — 4 pilihan, 1 kunci | vB: Mengapa gembok HTTPS pada `https://akun-dompet.test/masuk` **tidak** membuktikan situs itu… — 4 pilihan, 1 kunci | Menjelaskan mengapa alamat/gembok tidak membuktikan situs resmi (domain terdaftar, HTTPS) | 59 vs 60 kata (rasio 1.02); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 2.0 | PASS |
| W4 s05 | LO5 / `comp-w04-protect-01` | CE-S2, 2 poin (slot) | vA: Model W4: Rina menyimpan salinan foto di folder lain pada laptop yang sama. Pilih **semua*… — 4 pernyataan, 2 benar | vB: Pilih **semua** alasan yang benar mengapa cadangan tetap diperlukan walaupun perangkat sud… — 4 pernyataan, 2 benar | Menilai pernyataan cadangan (vA salinan di laptop yang sama, vB cadangan tetap perlu) | 59 vs 44 kata (rasio 1.34); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vA 3.0 | PASS |
| W4 s06 | LO6 / `comp-w04-incident-01` | CE-S3, 3 poin (slot) | vA: Ponselmu hilang di angkutan umum. Kamu sudah menelepon operator lewat kanal resmi untuk me… — 4 langkah, 2 urutan diterima | vB: Kamu mengeklik tautan phishing di laptop dan sempat mengisi kata sandi akun kursus daring.… — 4 langkah, 2 urutan diterima | Mengurutkan 4 langkah respons insiden (hentikan → amankan), dua urutan diterima | 84 vs 51 kata (rasio 1.65); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | OPEN: beban baca berbeda (84 vs 51 kata) |
| W5 s01 | LO1 / `comp-w05-arith-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap ekspresi dengan nilainya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap ekspresi dengan nilainya.… — 4 pasangan, 5 pilihan kanan | Memetakan 4 ekspresi ke nilainya dengan urutan operasi | 30 vs 26 kata (rasio 1.15); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s02 | LO2 / `comp-w05-expr-01` | CE-S2, 3 poin (slot) | vA: Pilih **semua** pernyataan yang benar.… — 5 pernyataan, 3 benar | vB: Pilih **semua** pernyataan yang benar.… — 5 pernyataan, 3 benar | Menilai 5 pernyataan variabel, substitusi, pangkat, rata-rata | 47 vs 44 kata (rasio 1.07); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s03 | LO3 / `comp-w05-divmod-01` | CE-S5, 4 poin (slot) | vA: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | vB: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | Menemukan baris pembagian bersisa yang salah dan memilih perbaikan | 80 vs 80 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s04 | LO4 / `comp-w05-unit-01` | CE-S1, 4 poin (slot) | vA: Mengapa **2 jam 30 menit** tidak sama dengan **2,3 jam**?… — 4 pilihan, 1 kunci | vB: Mengapa **1,5 kg** tidak sama dengan **1 kg 5 g**?… — 4 pilihan, 1 kunci | Menjelaskan mengapa besaran bersatuan campuran ≠ bentuk desimal yang salah (vA jam-menit, vB kg-g) | 50 vs 46 kata (rasio 1.09); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s05 | LO5 / `comp-w05-pct-01` | CE-S3, 3 poin (slot) | vA: Urutkan langkah menghitung harga setelah diskon 25% dari Rp160.000.… — 4 langkah, 2 urutan diterima | vB: Urutkan langkah menghitung persentase kenaikan dari 60 menjadi 75.… — 4 langkah, 2 urutan diterima | Mengurutkan 4 langkah persentase dari nilai dasar (vA diskon, vB kenaikan), dua urutan diterima | 42 vs 38 kata (rasio 1.11); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W5 s06 | LO6 / `comp-w05-round-01` | CE-S2, 2 poin (slot) | vA: Pilih **semua** pernyataan yang benar menurut aturan pembulatan W5.… — 4 pernyataan, 2 benar | vB: Pilih **semua** pernyataan yang benar menurut aturan pembulatan W5.… — 4 pernyataan, 2 benar | Menilai 4 pernyataan aturan pembulatan | 47 vs 50 kata (rasio 1.06); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s01 | LO1 / `comp-w06-repr-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap tulisan dengan artinya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap tulisan dengan artinya.… — 4 pasangan, 5 pilihan kanan | Memetakan 4 tulisan (biner, desimal, Boolean) ke artinya | 21 vs 21 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s02 | LO2 / `comp-w06-bin2dec-01` | CE-S3, 3 poin (slot) | vA: Urutkan langkah mengubah bilangan biner ke desimal.… — 4 langkah, 1 urutan diterima | vB: Urutkan langkah memeriksa bahwa `1100₂` bernilai 12.… — 4 langkah, 1 urutan diterima | Mengurutkan 4 langkah biner → desimal (vA prosedur umum, vB memeriksa satu bilangan) | 35 vs 43 kata (rasio 1.23); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s03 | LO3 / `comp-w06-dec2bin-01` | CE-S5, 4 poin (slot) | vA: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | vB: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | Menemukan baris biner yang salah dan memilih perbaikan 8 bit | 60 vs 57 kata (rasio 1.05); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s04 | LO4 / `comp-w06-ops-01` | CE-S1, 4 poin (slot) | vA: Mengapa `A AND B` bernilai **0** bila A = 1 dan B = 0?… — 4 pilihan, 1 kunci | vB: Mengapa `A OR B` bernilai **1** bila A = 0 dan B = 1?… — 4 pilihan, 1 kunci | Menjelaskan hasil satu operator dari definisinya (vA AND, vB OR) | 45 vs 46 kata (rasio 1.02); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W6 s05 | LO5 / `comp-w06-table-01` | CE-S2, 3 poin (slot) | vA: Pilih **semua** pernyataan yang benar tentang tabel kebenaran.… — 5 pernyataan, 3 benar | vB: Pilih **semua** pernyataan yang benar tentang tabel kebenaran.… — 5 pernyataan, 3 benar | Menilai 5 pernyataan tabel kebenaran | 51 vs 49 kata (rasio 1.04); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | vB 2.0 | PASS |
| W6 s06 | LO6 / `comp-w06-model-01` | CE-S2, 2 poin (slot) | vA: Alarm berbunyi bila **pintu terbuka (P = 1) dan mode malam aktif (M = 1)**. Pilih **semua*… — 4 pernyataan, 2 benar | vB: Kipas menyala bila **suhu panas (S = 1) atau tombol manual ditekan (T = 1)**. Pilih **semu… — 4 pernyataan, 2 benar | Memilih semua ekspresi BX yang tepat untuk satu aturan (vA "dan", vB "atau"), dua ekspresi ekuivalen | 33 vs 33 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s01 | LO1 / `comp-w07-decomp-01` | CE-S2, 3 poin (slot) | vA: Masalah: menyelenggarakan lomba kebersihan kelas. Kebutuhannya: aturan lomba, juri, dan ha… — 5 pernyataan, 3 benar | vB: Masalah: membuat video profil sekolah. Kebutuhannya: naskah, pengambilan gambar, dan penyu… — 5 pernyataan, 3 benar | Memilih sub-masalah yang mencakup kebutuhan tanpa yang tidak relevan | 30 vs 28 kata (rasio 1.07); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s02 | LO2 / `comp-w07-pattern-01` | CE-S5, 4 poin (slot) | vA: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | vB: Seorang siswa menulis catatan berikut. Satu baris salah. Temukan barisnya dan pilih perbai… — 5 baris, 4 perbaikan | Menemukan baris pola yang salah dan memilih perbaikan (vA jenis pola, vB suku ke-n) | 66 vs 74 kata (rasio 1.12); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s03 | LO3 / `comp-w07-abstract-01` | CE-S1, 4 poin (slot) | vA: Mengapa peta jalur kereta hanya menampilkan urutan stasiun dan tempat berganti jalur, buka… — 4 pilihan, 1 kunci | vB: Mengapa rumus `total = n × h` lebih berguna daripada `total = 3 × 15.000`?… — 4 pilihan, 1 kunci | Menjelaskan alasan abstraksi (vA menyaring informasi, vB generalisasi variabel) | 50 vs 42 kata (rasio 1.19); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s04 | LO4 / `comp-w07-algo-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap instruksi dengan penilaiannya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap instruksi dengan penilaiannya.… — 4 pasangan, 5 pilihan kanan | Memetakan 4 instruksi ke penilaiannya (ambigu, tidak berakhir, urutan salah, jelas) | 38 vs 40 kata (rasio 1.05); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s05 | LO5 / `comp-w07-order-01` | CE-S3, 3 poin (slot) | vA: Urutkan tugas menyiapkan presentasi kecil. Prasyarat tertulis di setiap tugas.… — 4 langkah, 2 urutan diterima | vB: Urutkan tugas membuat kue. Prasyarat tertulis di setiap tugas.… — 4 langkah, 2 urutan diterima | Mengurutkan 4 tugas berprasyarat, dua urutan diterima | 30 vs 29 kata (rasio 1.03); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W7 s06 | LO6 / `comp-w07-test-01` | CE-S2, 2 poin (slot) | vA: Aturan: boleh meminjam buku bila usia **≥ 12**. Langkah yang ditulis: "Jika usia > 12, tul… — 4 pernyataan, 2 benar | vB: Aturan: diskon bila belanja **≥ Rp50.000**. Langkah yang ditulis: "Jika belanja > 50.000,… — 4 pernyataan, 2 benar | Menilai pernyataan kasus uji batas dan kesalahan > vs ≥ | 59 vs 49 kata (rasio 1.20); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s01 | LO1 / `comp-w08-algo-01` | CE-S2, 3 poin (slot) | vA: Algoritma membagi tagihan rata: `bagian ← tagihan ÷ n`. Pilih **semua** pernyataan yang be… — 5 pernyataan, 3 benar | vB: Algoritma mengubah detik menjadi menit dan sisa detik. Pilih **semua** pernyataan yang ben… — 5 pernyataan, 3 benar | Menilai 5 pernyataan input/output/domain algoritma | 34 vs 41 kata (rasio 1.21); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s02 | LO2 / `comp-w08-symbol-01` | CE-S4, 4 poin (slot) | vA: Cocokkan setiap bentuk dengan kegunaannya.… — 4 pasangan, 5 pilihan kanan | vB: Cocokkan setiap isi blok dengan bentuknya.… — 4 pasangan, 5 pilihan kanan | Memetakan 4 bentuk/isi blok flowchart (vA bentuk → kegunaan, vB isi → bentuk) | 23 vs 25 kata (rasio 1.09); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s03 | LO3 / `comp-w08-branch-01` | CE-S5, 4 poin (slot) | vA: Aturan: jika x > 10 maka y ← 1, selain itu y ← 2. Seorang siswa menulis catatan berikut. S… — 5 baris, 4 perbaikan | vB: Aturan: jika x ≤ 5 maka y ← "kecil", selain itu y ← "besar". Seorang siswa menulis catatan… — 5 baris, 4 perbaikan | Menemukan baris percabangan yang salah di batas dan memilih perbaikan | 85 vs 85 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s04 | LO4 / `comp-w08-loop-01` | CE-S1, 4 poin (slot) | vA: Mengapa perulangan `i ← 1`; selama `i ≤ 5`: tulis i (tanpa `i ← i + 1`) **tidak pernah ber… — 4 pilihan, 1 kunci | vB: Mengapa `i ← i + 1` diletakkan **di dalam** perulangan "selama i ≤ 10"?… — 4 pilihan, 1 kunci | Menjelaskan peran perubahan variabel pengendali bagi berhentinya perulangan | 46 vs 39 kata (rasio 1.18); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s05 | LO5 / `comp-w08-trace-01` | CE-S3, 3 poin (slot) | vA: Langkah: `a ← 3`; `b ← a × 2`; `a ← a + b`; `b ← a − 1`. Urutkan baris tabel penelusuran (… — 4 langkah, 1 urutan diterima | vB: Langkah: `x ← 10`; `y ← x ÷ 2`; `x ← x − y`; `y ← y + x`. Urutkan baris tabel penelusuran… — 4 langkah, 1 urutan diterima | Mengurutkan 4 baris tabel penelusuran | 52 vs 52 kata (rasio 1.00); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
| W8 s06 | LO6 / `comp-w08-correct-01` | CE-S2, 2 poin (slot) | vA: Algoritma "nilai **terkecil**": `kecil ← A[1]`, lalu bandingkan A[2] … A[n] dengan `<`. Pi… — 4 pernyataan, 2 benar | vB: Algoritma **menjumlahkan** daftar nilai. Pilih **semua** pernyataan yang benar.… — 4 pernyataan, 2 benar | Menilai 4 pernyataan kebenaran algoritma daftar (nilai awal, negatif, nilai sama, kasus uji) | 59 vs 44 kata (rasio 1.34); tanpa field kesulitan/waktu per varian; durasi tidak diuji pelajar | — | PASS |
