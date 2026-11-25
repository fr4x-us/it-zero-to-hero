# IT ZERO → HERO — Matriks Cakupan Kompetensi W1–W8 (D-39)

Status: **dokumentasi** · audit statis butir · bukan verifikasi runtime atau
uji pelajar. Dibuat oleh generator `docs/validation/build_matrix.py` dari
`coverage_data.py` (pembacaan butir oleh penyusun) dan berkas butir nyata.
Kontrak: **D-39 HYBRID COMPETENCY COVERAGE** ({{DECISIONS_LOG_LINK}}).

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
  Konsep yang memakai bukti (b): **{{NB}}**. Aturan pemilihan tidak diubah.
- **Status**: PASS bila bukti jalur terpenuhi dengan lokasi berbukti
  semantik **kuat**; OPEN bila hanya terpenuhi dengan bukti semantik
  **lemah**; GAP bila tidak terpenuhi.
- **Remedial**: bukti berlaku untuk setiap indeks varian, jadi setiap
  attempt remedial (VA-2/VA-3, tanpa batas) tetap tercakup.
- Uji metode (dijalankan generator): hanya varian A → GAP; varian A di dua
  komponen → GAP; lab di kedua varian → PASS; varian A + B di dua slot satu
  komponen → PASS dengan bukti (b); hanya bukti semantik lemah → OPEN.

## 2. Ringkasan cakupan — HASIL PENULIS, belum diverifikasi independen

{{SUMMARY}}

Riwayat: baseline `a644d61` — 15 GAP (W1 1, W2 8, W3 2, W4 3, W6 1) →
dikoreksi putaran 3. Putaran 4 (review `4ddc993`): R3-04 = koreksi bukti
saja; R3-05, R3-06, R3-07 = bukti penolakan opsi tidak cukup, butir
direvisi minimum; R3-03 = isu keselamatan prosedur dikoreksi. Putaran 5
(review `796043c`, R4-03): proyek K4.q3 dihapus sebagai bukti salin; tiga
baris hanya berbukti semantik lemah kini **OPEN**. GAP: **{{GAPS}}**; OPEN:
**{{COV_OPEN}}** (usulan koreksi di §7, menunggu otorisasi owner).

Kesetaraan akademik varian (R3-02/R4-04–R4-09, §6; penilaian penulis): **{{EQ_PASS}} PASS**,
**{{EQ_OPEN}} OPEN** dari 48 slot. Cakupan modul dan kesetaraan varian adalah syarat terpisah.

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
| R3-04 | Bukti "salin mempertahankan asal" pada teori s17 vA tidak sah | CONFIRMED (bukti) — matriks dikoreksi; *putaran 4 menyebut proyek K4.q3; dikoreksi R4-03*: bukti (b) teori s15 vA + s17 vB | YA | BELUM |
| R3-05 | NAT: penolakan opsi tidak menuntut konsep berbagi | CONFIRMED — FIXED (W3 concept s02 vB opsi e) | YA | BELUM |
| R3-06 | Tanda vs bukti: vB opsi e tidak menuntut "bukan bukti" | CONFIRMED — FIXED (W4 concept s02 vB opsi e) | YA | BELUM |
| R3-07 | Pernyataan majemuk W4 concept s05 vA opsi b | CONFIRMED — FIXED (tidak ada lokasi wajib lain; opsi dijadikan satu klaim) | YA | BELUM |
| R3-08 | Status penerimaan hanya di komentar YAML | CONFIRMED — FIXED (TPL-01a `acceptance`, `check_acceptance.py`) | YA | BELUM |
| PR28-06 | Cakupan `required_concepts` | D-39 dicatat; audit penulis; **tetap OPEN**: 3 baris cakupan berbukti lemah dan 5 slot kesetaraan OPEN | SEBAGIAN | BELUM |
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

## 7. Usulan koreksi butir — MENUNGGU OTORISASI OWNER (tidak diterapkan)

| Slot | Masalah | Usulan minimum | Dampak |
|---|---|---|---|
| W4 concept s03 (diterima historis) | vA aritmetika PIN vs vB klasifikasi MFA | vB: jadikan baris salah sebuah pernyataan kombinasi PIN (mis. "PIN 4 digit … 400 kombinasi" → 10.000) dan ubah baris MFA menjadi benar ("Kata sandi + PIN bukan MFA…") | Cakupan "faktor berbeda jenis" tetap dijamin lab act-03.c02 kedua varian |
| W4 concept s01 (diterima historis) | Definisi vs klasifikasi skenario | vA: ubah menjadi pemetaan kejadian → istilah (kejadian berbeda dari vB) | Konsep sama; tuntutan setara |
| W3 concept s03 (diterima historis) | Hitung host vs keanggotaan | vB: baris salah menjadi jumlah host ("256 alamat dapat dipakai" → 254); baris keanggotaan menjadi benar | "tiga oktet" tetap dijamin lab act-02.c06–c08 |
| W3 concept s01 (diterima historis) | Peran router dan switch hanya berbukti lemah | vA kunci b: "…di LAN yang sama dan terhubung lewat switch/access point; router hanya diperlukan untuk ke jaringan lain" | Menutup 2 baris OPEN cakupan |
| W4 teori s10 vA (diterima historis) | "OTP tidak dibagikan" berbukti lemah | Ganti opsi salah e ("tanggal lahir") dengan "Membagikan OTP kepada orang yang mengaku petugas" (tetap salah; kunci a, c, d tetap) | Menutup 1 baris OPEN cakupan |
| W7 concept s02 (CB-2) | Jenis pola vs suku ke-n | vB: baris salah menjadi jenis pola (cermin vA); baris suku ke-n benar | Suku ke-n tetap dijamin teori s05 |
| W7 concept s03 (CB-2) | Menyaring vs generalisasi | vB: skenario menyaring informasi (cermin vA) | Generalisasi tetap dijamin teori s10 |

Setiap usulan akan mengubah varian butir (versi naik; W1–W4 tercatat PENDING
di TPL-01a) dan memerlukan otorisasi owner sebelum diterapkan.

