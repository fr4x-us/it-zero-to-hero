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
- **Status bukti (b) (putaran 8): CONDITIONAL PASS — bukti kontrak desain
  lengkap, verifikasi implementasi dan OD-9 tertunda.** (1) *Kontrak desain*:
  VA-4a (otorisasi owner PR #28 O-2, [CCD](../CURRICULUM_CONTENT_DECISION_SHEETS.md)
  §B.2) mewajibkan semua varian satu attempt dipilih dari satu snapshot
  riwayat ter-commit, mencakup setiap slot wajib, dan di-commit atomik
  bersama identitas attempt; resume tidak memilih ulang. (2) *Bukti
  induksi*: basis — sebelum attempt pertama semua slot berstatus sama
  (pemakaian 0/0, tanpa varian sebelumnya); langkah — status riwayat sama →
  keputusan VA-2 deterministik sama (jumlah varian dan urutan vA, vB sama di
  setiap slot, diperiksa generator) → commit atomik menambahkan varian sama
  ke semua slot → status tetap sama. Maka setiap attempt teori memakai indeks
  varian sama di s15 dan s17, sehingga jalur sah hanya {s15 vA, s17 vA} atau
  {s15 vB, s17 vB}, dan keduanya menilai "salin mempertahankan asal". (3)
  *Simulasi generator*: normal, gagal sebelum commit, terputus setelah commit
  + resume berulang, remedial 51 attempt, restore snapshot utuh → sinkron;
  riwayat parsial/rusak ditolak sebagai masalah integritas. (4) *Tertunda*:
  verifikasi implementasi (belum ada aplikasi) dan OD-9/SB-12/UW-33 (restore
  saat `IN_PROGRESS`). Tidak ada verifikasi runtime Android.
- **Integritas kunci (R6-03, STRUKTUR)**: generator memeriksa bahwa setiap
  kunci merujuk elemen yang ada dan dinilai (opsi, baris + opsi koreksi,
  pasangan satu-ke-satu, permutasi urutan, kunci lab/K4, poin > 0) untuk
  semua varian teori/concept, lab, dan proyek W1–W8. Ini bukan bukti bahwa
  kunci benar secara makna.
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
**{{COV_OPEN}}** (usulan koreksi di §7, menunggu otorisasi owner). Putaran 6
(otorisasi owner): 4 varian concept direvisi untuk kesetaraan; cakupan tetap 153/3/0.
Putaran 7 (otorisasi bersyarat): 4 varian direvisi; cakupan 156/0/0 dan
kesetaraan 48/0 — **hasil penulis**, belum diverifikasi independen; PR28-06 tetap OPEN.

Kesetaraan akademik varian (R3-02/R4-04–R4-09, §6; penilaian penulis): **{{EQ_PASS}} PASS**,
**{{EQ_OPEN}} OPEN** dari 48 slot. Cakupan modul dan kesetaraan varian adalah syarat terpisah.

## 3. Koreksi butir untuk cakupan dan kesetaraan (D-39, putaran 3–4, 6, 7, dan 8)

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
| W3 | concept s01 vA (R7) | skenario kotak router Wi-Fi multifungsi; kunci: switch meneruskan di dalam LAN, router ke jaringan lain; pengecoh fungsi tertukar / access point | LAN vs internet, peran router, peran switch | b | 2.0 |
| W3 | concept s01 vB (R7) | skenario lab hanya switch; struktur kunci dan pengecoh cermin vA | idem | d | 2.0 |
| W4 | concept s01 vA (R7) | kejadian → istilah (foto KTP, nilai rapor, aplikasi bank, kode autentikator); R4 "Pencadangan data" | kerahasiaan, integritas, ketersediaan, autentikasi | L1→R3, L2→R5, L3→R1, L4→R2 | 2.0 |
| W4 | teori s10 vA (R7) | opsi d benar: tidak memberikan OTP kepada siapa pun (menggantikan "aktifkan MFA"); opsi e tanggal lahir tetap | OTP tidak dibagikan | a, c, d | 2.0 |
| W4 | teori s10 vA, vB (R8 O-1) | **hanya stem**: "Pilih semua kebiasaan yang baik untuk menjaga keamanan kata sandi dan autentikasi akun." (opsi, kunci, poin tetap) | OTP tidak dibagikan; sandi unik | vA a, c, d; vB b, c, e | vA 3.0, vB 2.0 |

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
| PR28-06 | Cakupan `required_concepts` | D-39 dicatat; audit penulis; **tetap OPEN**: putaran 7: cakupan 156 PASS dan kesetaraan 48 PASS (hasil penulis); tetap OPEN sampai review independen dan penerimaan owner | SEBAGIAN | BELUM |
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

## 4d. Register temuan review putaran 6 dan otorisasi putaran 7 (ID sementara R6-xx)

| ID | Temuan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R7-A | Otorisasi bersyarat: W3 concept s01 vA/vB, W4 concept s01 vA, W4 teori s10 vA | APPLIED — versi 2.0; kunci/posisi kunci tetap; 4 varian putaran 6 tidak diubah; 20 varian W1–W4 PENDING | YA | BELUM |
| R5-02 | Peran router/switch | APPLIED (R7) — kunci kedua varian menuntut fungsi keduanya; batas: alamat MAC tidak diajarkan di W3 sehingga tidak dinilai | YA | BELUM |
| R5-03 | OTP tanpa menghapus bukti sandi mudah ditebak | APPLIED (R7) — opsi d vA; opsi e tetap; anjuran praktis MFA tetap dinilai wajib di proyek K1.c07 (E→T2), K1.c11 (D→T2), K4.q2; faktor MFA di lab act-03.c02 vA+vB | YA | BELUM |
| R6-01 | Baseline penerimaan dipercaya dari metadata yang divalidasi | CONFIRMED — FIXED: jangkar terpisah `trust/acceptance_anchors.yaml` diperiksa silang dengan merge PR (#25, #27), leluhur HEAD, dan DECISIONS_LOG; baseline diambil dari jangkar; 8 uji. Batas: bukan bukti kriptografis otorisasi owner | YA | BELUM |
| R6-02 | Relokasi varian tidak terdeteksi | CONFIRMED — FIXED: modul, komponen, path, slot_id, item_id, variant_id dibandingkan dengan baseline; 5 uji | YA | BELUM |
| R6-03 | Kunci tidak divalidasi terhadap elemen | CONFIRMED — FIXED: integritas kunci 416 varian + lab + proyek; 28 uji (8 positif, 20 negatif) | YA | BELUM |
| R6-04 | `Rp5000 rupiah` diterima padahal kombinasi tidak tertulis | CONFIRMED (direproduksi) — FIXED: hanya kombinasi (awalan, akhiran) yang tertulis di accepted_answers; 12 fixture | YA | BELUM |
| R6-05 | Pemindai konsumen NB-5 mengakses `accepted_answers[0]` tanpa pemeriksaan | CONFIRMED — FIXED: validasi konten sebelum penurunan; diagnostik CONTENT_ERROR dengan path + ID; 9 uji ujung-ke-ujung termasuk CLI exit 1 tanpa traceback | YA | BELUM |
| R6-06 | Ketidakakuratan dokumentasi | CONFIRMED — FIXED: README, OFFICIAL_RUN, hitungan fixture | YA | BELUM |
| R3-04 / VA-2 | Bukti (b) bergantung pada riwayat sinkron | CONDITIONAL PASS — simulasi 6 skenario (§1); ketergantungan: pemilihan + pencatatan atomik semua slot (VA-4 tidak eksplisit), SB-12/OD-9 | SEBAGIAN | BELUM |

## 4e. Register temuan review putaran 7 dan otorisasi putaran 8 (ID sementara R7-xx)

| ID | Temuan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R7-01 / O-1 | Stem W4 teori s10 hanya menyebut kata sandi, padahal opsi menilai OTP | CONFIRMED — FIXED: stem vA dan vB diganti (hanya stem); vA 2.0 → 3.0, vB 1.0 → 2.0; 21 varian W1–W4 PENDING | YA | BELUM |
| O-2 / R3-04 | Pencatatan atomik varian VA-2 belum dinyatakan | FIXED (kontrak desain VA-4a + bukti induksi + simulasi); R3-04 **CONDITIONAL PASS** — implementasi dan OD-9 tertunda | SEBAGIAN | BELUM |
| R7-02 | Pemindai NB-5 melewatkan konsumen lab bila accepted_answers hilang/cacat | CONFIRMED — FIXED: konsumen lab diturunkan dari deklarasi `normalization` per pemeriksaan (52 konsumen sama seperti sebelumnya); 15 uji ujung-ke-ujung | YA | BELUM |

## 4f. Penerimaan owner final (2026-11-25)

Owner menerima CB-2 (W05-ACC–W08-ACC) dan 21 varian revisi W1–W4 (PR #28 ACC) pada HEAD review
`b54f930`, dengan verdict independen "PASS — targeted delta review with disclosed limitations".
Angka cakupan dan kesetaraan di dokumen ini tetap **hasil penulis**; review independen terarah tidak
memverifikasi ulang 156 konsep. PR28-06 diterima untuk perencanaan kurikulum di bawah penerimaan
owner dan batas review terarah (DECISIONS_LOG). R3-04 tetap CONDITIONAL PASS.

## 7. Usulan koreksi butir

Tidak ada usulan terbuka. Usulan putaran 5–6 (W3 concept s01 vA/vB, W4
concept s01 vA, W4 teori s10 vA) diterapkan atas otorisasi bersyarat
putaran 7 (§3, §4d). Otorisasi revisi **bukan** penerimaan: semua varian
revisi W1–W4 tetap PENDING (TPL-01a) sampai review independen dan
penerimaan owner.
