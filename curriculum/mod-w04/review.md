---
module_id: mod-w04
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-1 + koreksi F-28–F-72 (dua putaran). Review independen PR #27: REQUEST CHANGES (dua kali) → dikoreksi → delta review PASS (terarah, dengan batas yang diungkapkan); diterima owner W04-ACC (2026-11-24)"
---

# W4 — Review Kualitas, Kesetaraan Varian, Keamanan Konten, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-1) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review independen (ChatGPT) | PR #27: **REQUEST CHANGES** (F-28–F-70, lalu delta F-28–F-72) → dikoreksi → **delta review PASS** — targeted delta review with disclosed limitations (lihat bagian penerimaan) |
| Diterima owner (W04-ACC) | **YA** (2026-11-24, PR #27 merge `846051f`) — lihat bagian penerimaan di akhir dokumen |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim |
| Durasi diuji dengan pelajar | **TIDAK** |

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah |
|---|---|
| Pelajaran / set latihan | 4 / 4 (4 × 45 = 180 menit) |
| Soal teori | **40** (20 slot × 2) |
| Soal concept | **12** (6 slot × 2) |
| Spesifikasi lab | **6** (3 aktivitas × 2) |
| Mini-project | **1** (rubrik MR-A, 13 contoh reviewer) |
| Materi remedial | 6 bagian (R-CIA, R-THREAT, R-AUTH, R-PHISH, R-PROTECT, R-INCIDENT) |

Pemeriksa dokumen: **191 ID unik**, 0 duplikat; kunci di opsi;
`distractor_rationale` lengkap; urutan diterima ≠ urutan tampil; CE-S4
satu-ke-satu; CE-S5 P genap; poin = maksimum; field kanonik; 0 galat.

## 3. Tujuan belajar

| LO | Kompetensi | Pelajaran | Teori | Lab | Proyek | Concept |
|---|---|---|---|---|---|---|
| LO1 CIA | `comp-w04-cia-01` | les-01 | s01–s03 | act-03.c01 | K4.q1 | s01 |
| LO2 ancaman | `comp-w04-threat-01` | les-01 | s04–s07 | act-01 | K1.c01–c06 | s02 |
| LO3 autentikasi | `comp-w04-auth-01` | les-02 | s08–s11 | act-03.c02–c03 | K1.c07–c14 (T1, T2), K4.q2 | s03 |
| LO4 phishing/URL | `comp-w04-phish-01` | les-03 | s12–s14 | act-02 | K4.q3 | s04 |
| LO5 perlindungan/cadangan | `comp-w04-protect-01` | les-04 | s15–s17 | act-03.c04–c05 | K1.c08–c17, K4.q4 | s05 |
| LO6 respons/etika | `comp-w04-incident-01` | les-04 | s18–s20 | act-03.c06 | K4.q5 | s06 |

Prasyarat: W2 (ekstensi tersembunyi, izin, akun biasa), W3 (DNS, HTTPS
port 443). Tidak ada materi modul berikutnya.

## 4. Keamanan konten (wajib W4)

| Pemeriksaan | Hasil | Bukti |
|---|---|---|
| Defensif dan edukatif | PASS | Tidak ada instruksi menyerang, membuat malware, menebak sandi orang, atau melewati pengaman; pemindaian kata kunci berisiko = 0 |
| Skenario dan data fiktif | PASS | Semua domain berakhiran `.example`/`.test` (dicadangkan untuk contoh); 0 domain nyata selain penjelasan umum `.co.id` (`nama.co.id`, placeholder) di Pelajaran 3 |
| Tanpa akses nyata | PASS | Lab dan proyek hanya membaca/mengklasifikasi/mengisi formulir; `safety` tertulis di setiap `checks.yaml` dan rubrik; refleksi melarang menulis sandi/data pribadi |
| Tanpa jaminan keamanan berlebihan | PASS | Pelajaran 1 §2 (tanda bukan bukti pasti), Pelajaran 4 §1 (perlindungan mengurangi, tidak menjamin), HTTPS bukan bukti kejujuran |
| Etika | PASS | Pelajaran 4 §4; lab act-03 vB c06; concept dan teori tidak meminta pelajar mengakses milik orang lain |
| Pihak nyata | PASS | Nama lembaga fiktif (Bank Contoh, Sekolah Pelita, DompetKu, dll.); tidak meniru merek nyata |

## 5. Skor yang dapat dicapai dan aritmetika

### 5.1 Maksimum (QC-01)

| Komponen | Dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori | 56 | **56** | 8 × 2 + 8 × 3 + 4 × 4 |
| Lab act-01 / act-02 / act-03 | 30 / 40 / 30 | **30 / 40 / 30** | 10 × 3; 8 × 5; 6 × 5 — setiap jawaban benar terverifikasi (§5.3) |
| Lab komponen | 100 | **100** | 30 + 40 + 30 |
| Proyek | 100 | **100** | E01, E02, E08 = 100 (18/18 cocok dengan evaluator setelah koreksi) |
| Concept | 20 | **20** | CE-S4 4 + CE-S2 (k 3) 3 + CE-S5 4 + CE-S1 4 + CE-S2 (k 2) 2 + CE-S3 (n 4) 3 |

### 5.2 Durasi teori, XP, jadwal

| Hal | Hasil |
|---|---|
| Komposisi | TF-1 × 11, TF-2 × 3, TF-3 × 3, TF-4 × 2, TF-5 × 1; D1 8 · D2 8 · D3 4 |
| Rumus A.4 | dasar 11·45 + 3·75 + 3·60 + 2·90 + 75 = **1.155**; S = **1.635** → ⌈1.798,5⌉ = 1.799 → ⌈29,98…⌉ + 2 = **32 menit** |
| Timer / review / TA-B | **32** / **13** / **48** menit |
| XP | 305 |
| Jadwal | 180 + 45 + 90 (30 + 30 + 30) + 90 + 30 + 45 = **480**; sesi 240 + 240 |

### 5.3 Verifikasi deterministik

| Cakupan | Hasil |
|---|---|
| Domain terdaftar (UR-1–UR-5) untuk lab act-02 (8 URL), teori s13, s14 (8 URL), concept s04, Pelajaran 3, latihan, remedial | Dihitung ulang; nama host dibandingkan dengan `urllib.parse.urlsplit` — 0 selisih |
| Aturan penilaian pesan act-02 | vA A, C, C, A; vB C, A, A, C — sesuai `verdict_rule` |
| PIN | 10⁴ = 10.000; 10⁵ = 100.000; 10⁶/10⁴ = 100; 10⁸/10⁵ = 1.000; lab 10⁷, 10⁸ (bentuk bertitik diterima) |
| Cadangan CB-1–CB-4 | Teori s16 (8 rencana), lab act-03 c04 (3; 2), Pelajaran 4 (Fajar: 2 salinan, gagal), latihan, remedial |
| Proyek | F2: 8.192 kombinasi tindakan bernilai penuh; F3: 20 dari 31 himpunan memenuhi 3-2-1; total 163.840 rencana bernilai penuh; batas 2 jenis media (E08) dan "semua di rumah" (E07) diuji |

### 5.4 Skenario kelulusan

Maksimum W4 (56 / 100 / 100 / 20) **sama** dengan W2, sehingga rumus
`280·W = 150·T + 112·L + 56·P + 140·C` dan skenario SC-1–SC-6 W2
([`../mod-w02/review.md`](../mod-w02/review.md) §4.5) berlaku tanpa
perubahan (TE-13: sumber dan asumsi sama). Contoh batas: T 42, L 75, P 90,
C 19 → 22.400 → W tepat 80, **PASSED**; T 47, L 75, P 86, C 15 → 22.366
→ 79,87…, NOT_PASSED.

## 6. Posisi kunci jawaban

**a 9 · b 8 · c 10 · d 8** (setelah penyeimbangan dari a 9 · b 11 · c 10 ·
d 5: opsi s06 vA, s14 vB, s20 vB ditata ulang). Pilihan ganda: s05
{a,b,d}/{b,c,e}; s10 {a,c,d}/{b,c,e}; s17 {a,c,d}/{a,c,e}; concept s02
{a,c,e}/{b,c,e}; s05 {a,c}/{b,c}.

## 7. Matriks kesetaraan varian (QC-04)

| Slot | Kompetensi | Konsep wajib | Format | Kesulitan | Maks. | Alasan kesetaraan |
|---|---|---|---|---|---|---|
| s01 | cia | definisi tujuan | TF-1 | D1 | 2 | Opsi sama; A kerahasiaan, B integritas |
| s02 | cia | kejadian → tujuan | TF-4 | D2 | 3 | 4 kejadian (2 kerahasiaan + 1 integritas + 1 ketersediaan); A cari ketersediaan, B cari integritas |
| s03 | cia | tujuan dari skenario | TF-1 | D1 | 2 | Kedua stem berlabel model W4 "terutama"; A ketersediaan, B kerahasiaan |
| s04 | threat | jenis malware | TF-1 | D1 | 2 | Opsi sama; A ransomware, B spyware |
| s05 | threat | tanda malware | TF-2 | D2 | 3 | 3 tanda + 2 perilaku normal; laptop / ponsel |
| s06 | threat | Wi-Fi palsu / rekayasa sosial | TF-1 | D2 | 3 | Keduanya mengenali penyamaran dari skenario dan memilih respons/ jenis |
| s07 | threat | klasifikasi 3 kejadian | TF-4 | D3 | 4 | 3 kejadian berbeda jenis; pengecoh = pertukaran dua label |
| s08 | auth | jenis faktor | TF-1 | D1 | 2 | Opsi sama; melekat / dimiliki |
| s09 | auth | kombinasi PIN | TF-3 | D1 | 2 | 10ⁿ (n = 4 / 5) |
| s10 | auth | kebiasaan sandi | TF-2 | D2 | 3 | 3 baik + 2 buruk |
| s11 | auth | perbandingan kombinasi | TF-3 | D3 | 4 | Dua pangkat lalu bagi (selisih 2 / 3 digit) |
| s12 | phish | tanda phishing | TF-1 | D1 | 2 | Satu tanda kuat di antara 3 ciri netral |
| s13 | phish | domain terdaftar | TF-3 | D2 | 3 | Nama resmi muncul sebagai subdomain (A) / path (B) |
| s14 | phish | tautan resmi | TF-1 | D3 | 4 | 4 tautan: 1 resmi (subdomain), 3 tiruan (subdomain milik lain, tanda hubung, salah eja) |
| s15 | protect | fungsi perlindungan | TF-1 | D1 | 2 | Pembaruan / kunci layar; pengecoh "menjamin" |
| s16 | protect | 3-2-1 | TF-1 | D2 | 3 | A cari yang memenuhi, B cari yang tidak; CB-4 diuji di keduanya |
| s17 | protect | mengurangi risiko malware | TF-2 | D2 | 3 | 3 tindakan baik + 2 buruk; ponsel / laptop |
| s18 | incident | langkah pertama | TF-1 | D1 | 2 | Amankan akun dulu (sandi / kanal resmi) |
| s19 | incident | urutan respons | TF-5 | D2 | 3 | 4 langkah dengan prasyarat eksplisit ("setelah …") → urutan unik |
| s20 | incident | tindakan terbaik | TF-1 | D3 | 4 | Skenario bertingkat (ransomware + cadangan / sandi dipakai ulang) |

| Slot | Konsep wajib | Format | Maks. | Alasan kesetaraan |
|---|---|---|---|---|
| concept.s01 | tiga tujuan + autentikasi | CE-S4 | 4 | A definisi; B contoh kejadian → istilah; masing-masing 1 pengecoh |
| concept.s02 | phishing ⊂ rekayasa sosial; trojan; tanda ≠ bukti | CE-S2 (k 3) | 3 | 3 benar + 2 miskonsepsi |
| concept.s03 | MFA, OTP, 10ⁿ | CE-S5 | 4 | Satu baris salah (hitungan PIN / definisi MFA) |
| concept.s04 | domain terdaftar; HTTPS bukan bukti | CE-S1 | 4 | Mengapa tautan tidak resmi meski memuat nama/HTTPS |
| concept.s05 | CB-4; perlindungan tidak menjamin | CE-S2 (k 2) | 2 | Satu risiko/batas + satu fungsi/aturan |
| concept.s06 | hentikan → amankan; kanal resmi | CE-S3 (n 4) | 3 | Dua skenario, masing-masing 2 urutan diterima (langkah terakhir dapat ditukar) |

| Aktivitas | Maks. | Menit | Bukti kesetaraan |
|---|---|---|---|
| act-01 | 30 | 30 | Distribusi kode sama: PHI 2, SOS 1, TRO 1, RAN 1, SPY 1, WIF 1, AMN 3 |
| act-02 | 40 | 30 | 4 pesan: 2 resmi (subdomain/www, tanpa permintaan data), 2 tiruan (subdomain milik lain / tanda hubung atau path); pola A/C berbeda urutan |
| act-03 | 30 | 30 | Pasangan per nomor setara; c06: A teknis (ransomware), B etika — keduanya keputusan respons pertama LO6 (dicatat sebagai perbedaan konteks) |

## 8. Model sederhana vs kenyataan (QC-05)

| Model W4 | Kenyataan (ditulis di pelajaran) |
|---|---|
| "Terutama" satu tujuan CIA | Kejadian nyata dapat mengganggu beberapa tujuan |
| Domain terdaftar = dua bagian terakhir | `.co.id` dan akhiran lain; trik huruf mirip |
| Setiap PIN sama mungkin | Orang memilih PIN mudah; sistem mengunci setelah beberapa kali salah |
| Tanda malware | Bukan bukti pasti |
| Jenis media cadangan (5 kategori) | Penyederhanaan untuk belajar |
| Perlindungan | Mengurangi risiko, tidak menjamin |

## 9. Tumpang-tindih dan visibilitas (QC-06, QC-11)

| Temuan | Tindakan |
|---|---|
| Pelajaran 2 contoh "6 digit vs 2 digit = 10.000 kali" sama dengan jawaban s09 vA (10.000) | **Diperbaiki**: contoh 3 vs 2 digit (10 kali); latihan diganti 2 digit/1 digit |
| Pelajaran 2 miskonsepsi "6 digit = 100 kali 4 digit" = jawaban s11 vA | **Diperbaiki** sebelum validasi: dirumuskan umum "+1 digit ×10" |
| Lab act-03 vA c04 sama struktur dan hasil dengan contoh Fajar (Pelajaran 4) | **Diperbaiki**: rencana dan jawaban diganti (3; vB 2) |
| Concept s01 vB satu kejadian dapat ditafsirkan ganda | **Diperbaiki**: diganti kejadian autentikasi yang tidak ambigu |
| Domain act-02 terlihat di `spec.md` | Diterima: tugasnya mengekstrak domain dari URL yang harus ditampilkan |
| `1.000`, `100` di Pelajaran 2/remedial (hitungan kombinasi) vs jawaban s11 (perbandingan) | Diterima: jenis hitungan berbeda; dicatat |

## 10. QC-01–QC-12 dan CQ-01–CQ-20

| QC | Hasil | Bukti |
|---|---|---|
| QC-01 | PASS | §5.1 |
| QC-02 | PASS | §5.3 (18/18) |
| QC-03 | NOT APPLICABLE | Tidak ada konversi satuan |
| QC-04 | PASS | §7 |
| QC-05 | PASS | §8 |
| QC-06 | PASS setelah perbaikan | §9 |
| QC-07 | PASS | `spec.md` ↔ `checks.yaml` (skenario, URL, domain resmi, opsi); proyek AR-1–AR-5, CB-1–CB-4 ↔ rubrik |
| QC-08 | PASS | Normalisasi domain (huruf bebas, tanpa skema/path), angka bertitik, kode; `depends_on` mencegah poin tanpa pekerjaan (E12) |
| QC-09 | PASS | Field kanonik |
| QC-10 | PASS | Batas 2 jenis media, semua di rumah, CB-4, AMN vs ancaman |
| QC-11 | PASS | §9 |
| QC-12 | NOT APPLICABLE | Tidak ada satuan data |

CQ-01–CQ-20: PASS (kebenaran teknis dan keamanan konten §4; ramah pemula;
LO terukur; prasyarat; cakupan; tidak menilai materi yang belum diajarkan;
kelengkapan; kesetaraan; kunci; aritmetika; fixture deterministik; rubrik
objektif; concept D-23; XP unik; aksesibilitas; versi; 480 menit; offline;
konsistensi D-01–D-38; kunci tidak tampil sebelum umpan balik).

## 11. Regresi F-01–F-23

| Temuan W1 | Pemeriksaan di W4 | Status |
|---|---|---|
| F-01/F-02/F-19 | F4/F5 punya pemeriksaan kebenaran; K2 bentuk; MR-2; tanpa gerbang nol | PASS |
| F-03 | §6 | PASS |
| F-04/F-12/F-13 | §7 | PASS |
| F-05/F-21 | §5.3 enumerasi | PASS |
| F-07/F-14/F-23 | §9 | PASS setelah perbaikan |
| F-09 | §5.1 | PASS |
| F-10/F-22 | Tidak ada konversi satuan | NOT APPLICABLE |
| F-11/F-15 | §8; "model W4" di stem s03, s11, s13, s14, s16 | PASS |
| F-16/F-20 | Field kanonik | PASS |
| F-17 | Kode `SOS` didefinisikan "langsung, bukan lewat tautan" untuk membedakan dari PHI | PASS |
| F-24–F-27 | `.claude/` tidak disentuh | Dipertahankan |

## 12. Batas penilaian objektif dan bukti reviewer

Pemeriksaan membuktikan jawaban sesuai aturan W4 pada skenario fiktif;
tidak membuktikan akun nyata pelajar aman (D-17, D-34).

| Field | Isi |
|---|---|
| Reviewer / tanggal / basis | Claude (penyusun), 2026-11-24, `main` = `ab0103e` |
| Temuan terbuka | Tidak ada BLOCKED (deskripsi F-55–F-57, F-59 dipulihkan owner, putaran 2); *historis (sebelum penerimaan):* butuh re-review independen dan penerimaan owner; **status aktif:** delta review PASS dan diterima owner W04-ACC (lihat bagian penerimaan). Register: bagian koreksi konsolidasi di akhir dokumen |

Metrik W4 (dari transkrip; ±2): panggilan alat ≈ 22; berkas baru dibaca 0;
baca ulang 0; aksi gagal 0; temuan pemeriksa yang benar 5 (2 tumpang-tindih
angka, 1 tumpang-tindih lab, 1 butir ambigu, bias kunci); positif palsu
skrip 2 (pemetaan nama media, `.co.id` penjelasan); kegagalan identik
berulang 0; aktivasi skill 0 tambahan; checkpoint 1; operasi validasi 6;
pemulihan sesi 0. TOKEN USAGE: **NOT MEASURABLE**.

## 13. Koreksi konsolidasi CB-1 (PR #27, F-28–F-70; 2026-11-24)

Review PR #27 = **REQUEST CHANGES**. Sebelum mengedit diverifikasi: head
`a9241d33c2cf32e177ca92618df458b78dd6cb98`, base
`ab0103e4954ead4ded6343d105d73a2729916cd6` (cocok). Koreksi diterapkan pada
PR #27 yang sama. *Historis (saat koreksi):* status modul **diproduksi dan dikoreksi; menunggu re-review
independen dan penerimaan owner** — belum diterima.

### 13.1 Register F-28–F-72 (45 ID; diperbarui pada koreksi terarah putaran 2)

| ID | Lingkup | Disposisi | Bukti |
|---|---|---|---|
| F-28 | W3 | CONFIRMED — FIXED | `project/rubric.yaml` K1.c02–c06 membandingkan dengan konstanta `192.168.50.1` (bukan isian F1) + `f1_dependency`; F1 salah tidak lagi menjatuhkan pemeriksaan lain; fixture E18–E21 |
| F-29 | W4 ◀ | CONFIRMED — FIXED | `lab/act-02` `verdict_rule`: A = tidak ada indikator dalam model W4, **bukan** jaminan aman; spesifikasi diselaraskan |
| F-30 | W4 ◀ | CONFIRMED — FIXED | act-01 vA S6 + halaman yang meminta sandi email (bukti perilaku fiktif); label `WIF` = bukti perilaku; les-01: nama mirip saja bukan bukti; proyek S4 diperkuat |
| F-31 | W3 | NOT REPRODUCED | Blueprint dan review W3 pada commit produksi awal `9a562ce` dan pada head koreksi: TF-3 = 7 slot (s05, s08, s09, s10, s18, s19, s20) di keduanya; review mencantumkan "TF-3 × 7" di keduanya (dihitung ulang dari `git show`) |
| F-32 | W2 | CONFIRMED — FIXED | theory s05 vB dan concept s02 vA menyatakan "tidak punya simpan otomatis/pemulihan"; les-02 menjelaskan pengecualian simpan otomatis |
| F-33 | W2 | CONFIRMED — FIXED | theory s09 vA opsi a; concept s03 vA opsi d + umpan balik isi/ekstensi/pengaitan; les-03 membedakan isi, ekstensi, pengaitan aplikasi |
| F-34 | W3 | CONFIRMED — FIXED | theory s01 vA/vB dan act-03 c01: "Model peran W3 … **fungsi**" + rasional kotak router Wi-Fi; les-01 fungsi vs kotak |
| F-35 | W3 | CONFIRMED — FIXED | concept s04 (R5/R2): TCP mengirim ulang data hilang dan menyusun berurutan **selama sambungan berjalan**; les-03 diselaraskan |
| F-36 | W4 ◀ | CONFIRMED — FIXED | concept s04 opsi/umpan balik: HTTPS = sambungan terenkripsi ke nama domain, bukan bukti organisasi/kejujuran; les-03 tabel empat pertanyaan; remedial R-PHISH |
| F-37 | W4 ◀ | CONFIRMED — DOCUMENTATION CLARIFIED | Klarifikasi asumsi skenario (putaran 2): stem menyatakan model hentikan → amankan dan A prasyarat B; dua urutan diterima per varian **bukan** cacat. Isi putaran 1: concept s06 vA ditulis ulang: model "hentikan → amankan" dinyatakan di stem; A prasyarat B; 2 urutan diterima (ABCD, ABDC) — setara dengan vB (2 urutan); petunjuk "Setelah …" yang membocorkan urutan dihapus |
| F-38 | W4 ◀ | CONFIRMED — FIXED | s09/s11, act-03 c03, concept s03, les-02, remedial: digit 0–9, boleh diawali 0 dan berulang, yang dihitung jumlah PIN berbeda; jawaban diverifikasi `10**n` |
| F-39 | W4 ◀ | CONFIRMED — FIXED | `collection_validity` (kode tak dikenal/ganda → koleksi INVALID, pemeriksaan yang bergantung 0, lainnya tetap); fixture E14–E17 |
| F-40 | W2 | CONFIRMED — FIXED | `tree_valid` (6 syarat); pohon rusak → pemeriksaan bergantung F1 = 0, K2.c02–c05 tetap; gangguan aplikasi → EVALUATION_ERROR; fixture E17–E20 |
| F-41 | W2 | CONFIRMED — FIXED | act-01: "jenis isi yang **diharapkan** dari ekstensi"; umpan balik "→ diharapkan …"; les-03: ekstensi bukan bukti isi |
| F-42 | W2–W4 ◀ | CONFIRMED — FIXED | Aturan normalisasi eksplisit di setiap TF-3 dan lab (nol di depan ditolak; pemisah ribuan hanya bila diizinkan, pola `1.234`); `normalization_examples` di checks lab; diperiksa konsisten otomatis |
| F-43 | W3 | CONFIRMED — FIXED | act-01 `network_assumptions` menyebut rentang khusus (loopback, link-local, dll.) di luar model; les-02: publik "umumnya unik"; status publik hanya dari fixture |
| F-44 | W4 ◀ | CONFIRMED — FIXED | les-02: pembatasan percobaan PIN menurunkan risiko, **tidak** membuat tebakan mustahil; MFA "jauh lebih sulit", bukan mustahil |
| F-45 | W2 | CONFIRMED — DOCUMENTATION CLARIFIED | `final_state_only`: hanya keadaan akhir pohon dinilai; spesifikasi N4; fixture E21 (dihapus lalu dipulihkan → 100) |
| F-46 | W3 | CONFIRMED — DOCUMENTATION CLARIFIED | `suffix_24_rule` dan catatan IPN (lab vs proyek); fixture E20 (F1 `/24`) |
| F-47 | W4 ◀ | CONFIRMED — DOCUMENTATION CLARIFIED | T1 diberi catatan "aturan simulasi"; les-02: panjang saja tidak cukup (sandi umum/bocor tetap lemah) |
| F-48 | W2 | CONFIRMED — DOCUMENTATION CLARIFIED | s19 vB rasional = model W2; les-04 membedakan model tulis/hapus W2 dari izin folder nyata |
| F-49 | W3 | CONFIRMED — FIXED | Putaran 2 (deskripsi asli): s07 vA opsi a dan pembahasan tidak lagi menganggap router pasti beralamat publik; alamat privat tidak dirutekan langsung di internet publik; CGNAT disebut; vB menyatakan skenario tanpa CGNAT; les-02 diselaraskan. Kunci tetap a/c. Koreksi putaran 1 dipertahankan: les-02: alamat IP milik **antarmuka**, bukan perangkat |
| F-50 | W3 | CONFIRMED — FIXED | Putaran 2: s13 vA memberi asumsi (halaman sama tanpa peringatan sertifikat; pesan "alamat server untuk nama itu tidak ditemukan"); rasional HTTPS dan pembahasan menyebut DNS sebagai dugaan terkuat, bukan bukti pasti. Kunci tetap b. Putaran 1 dipertahankan: les-03 cek pemahaman: DNS/IP "kadang" (cache, alamat langsung) — tidak dinyatakan selalu |
| F-51 | W3 | CONFIRMED — FIXED | Putaran 2 (koreksi penilaian): satuan kecepatan peka huruf — s18 (`NUMR`, normalization_examples), lab act-03 c05 (head lama menerima `12 mb/s` dan `12 Mb/s`), spesifikasi lab, les-04; 8 fixture owner + 107 contoh lolos `norm_check.py`. Putaran 1 dipertahankan: les-04: reservasi DHCP sebagai alternatif alamat statis di luar rentang; aturan RA tidak berubah |
| F-52 | W4 ◀ | CONFIRMED — FIXED | Putaran 2: aturan kategori utama dijadikan **berurutan** (aturan pertama yang cocok) karena WIF dan PHI tumpang-tindih pada Wi-Fi tiruan yang menampilkan halaman peminta sandi (act-01 vA S6, vB S7; proyek S4); kunci tidak berubah, setiap skenario tepat satu kunci. Putaran 1: Aturan **kategori utama** (s07 stem, act-01 `primary_classification_rule`, proyek Bagian A, les-01); s07 vB E2 diperjelas |
| F-53 | W4 ◀ | CONFIRMED — FIXED | Putaran 2: s08 vB pembahasan, concept s01 (R2, L4) dan s03 vB baris 3, les-02, remedial: OTP = bukti sementara akses ke autentikator/rahasianya, dapat dicuri/diteruskan; tanpa klaim "membuktikan pemilik/memegang ponsel". Putaran 1 (rumusan "bukti memegang ponsel" kini diganti): s08 vB; concept s03 baris autentikator; les-02: autentikasi = pembuktian, OTP = faktor "yang dimiliki" |
| F-54 | W4 ◀ | CONFIRMED — FIXED | Putaran 2: s16 vA/vB pembahasan mendefinisikan lima jenis media model W4 (CB-2) dan menghitung media tiap rencana; folder lain di perangkat sama bukan media baru. Kunci dan aturan 3-2-1 tetap. Putaran 1: les-04 CB-1 "salinan terpisah"; model W4 menganggap salinan utuh, dunia nyata perlu uji pemulihan; aturan 3-2-1 dan penilaian tidak berubah |
| F-55 | W4 ◀ | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): s19 vA kini menyatakan Nia masih dapat masuk dengan sandi lama dari perangkat aman; pembahasan menyebut urutan berlaku untuk skenario ini (bila akses hilang: pemulihan lewat kanal resmi; melapor sedini mungkin). Urutan tetap tunggal BDAC |
| F-56 | W2 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner: concept s04 vB opsi d `../../foto/sampul.png` mencapai tujuan tetapi bukan terpendek. Diperbaiki di putaran 1 (baris salah menuntut "path relatif **terpendek**"; rasional d). Inspeksi independen terarah: PASS; dipertahankan |
| F-57 | W2 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): concept s05 vB langkah B kini memeriksa jumlah/nama berkas **dan** membuka setiap berkas untuk memastikan isinya lengkap dan terbaca sebelum menghapus asal (tanpa hash); umpan balik dan les-04 diselaraskan. Format CE-S3 dan urutan ABCD tetap |
| F-58 | W4 ◀ | CONFIRMED — FIXED | Putaran 2 (deskripsi asli): concept s01 vB L2 "dibaca orang lain **tanpa izin pemiliknya**"; skenario CIA terkait diperketat (s01 vB L1, theory s02 vB K2/K3/K4, s03 vB). Koreksi putaran 1 tentang tanda vs bukti malware dipertahankan sebagai koreksi tambahan, bukan pengganti: s05 stem: gejala = **tanda peringatan**, bukan bukti pasti; klasifikasi unik hanya dengan bukti perilaku fiktif (act-01, les-01) |
| F-59 | W4 ◀ | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): label AMN = tindakan pengguna tepat / bukti ancaman tidak cukup, **bukan** jaminan tidak ada ancaman — spec, checks (`codes`, `primary_classification_rule`), skenario vB S10 (yang diklasifikasikan = tindakan memeriksa lewat aplikasi resmi), umpan balik. ID AMN dan poin tetap |
| F-60 | W2 | CONFIRMED — FIXED | les-01: "aplikasi biasa" berjalan di atas OS + catatan perangkat tanpa OS (bare-metal) |
| F-61 | W2 | CONFIRMED — FIXED | les-02 latihan 1c: satu aplikasi dapat punya dua proses (dua PID) + pembahasan; jendela ≠ proses |
| F-62 | W3 | CONFIRMED — FIXED | les-01: modem vs ONT/ONU (fiber) |
| F-63 | W3 | CONFIRMED — FIXED | les-03: contoh TCP/UDP sebagai "pemakaian umum" + catatan QUIC (HTTP/3 di atas UDP) |
| F-64 | W3 | CONFIRMED — FIXED | les-04: RA-5 (gateway) berlaku untuk klien LAN |
| F-65 | W4 ◀ | CONFIRMED — FIXED | Inspeksi independen terarah PASS; dipertahankan (pengecualian `@`, port, `?`, `#`). les-03: UR-1 hanya untuk bentuk alamat W4 (tanpa port, userinfo, alamat IP) |
| F-66 | W4 ◀ | CONFIRMED — FIXED | les-04 dan concept s06: laporkan sedini mungkin (boleh bersamaan); tidak harus menunggu langkah terakhir |
| F-67 | W2–W4 ◀ | CONFIRMED — FIXED | Remedial W2–W4: VA-1–VA-6 (pemakaian paling sedikit → bukan varian sebelumnya → indeks terkecil; VA-3) |
| F-68 | W4 ◀ | CONFIRMED — FIXED | Remedial R-AUTH: MFA = **dua faktor atau lebih** dari jenis berbeda |
| F-69 | docs | CONFIRMED — FIXED | `CURRICULUM_PRODUCTION_PLAN.md` header/legenda/§4/§6.1 (historis)/§8; `CURRICULUM_OFFLINE_LAB_SPEC.md` K-13 historis + status aktif |
| F-70 | docs | CONFIRMED — FIXED | Baris CB-0: semua kebijakan terputuskan, tanpa penerimaan terpisah, review independen terbatas, **bukan** final global; CB-1a ACCEPTED (W01-ACC) |
| F-71 | W2 | CONFIRMED — FIXED | Baru (putaran 2): setiap depends_on yang memakai F1 kini `F1 (tree_valid)`, termasuk K1.c11–c14 (head lama tanpa F1); dependency_rule diperjelas. `sim_w02.py`: 19 pemeriksaan bergantung tree_valid, independen tepat K2.c02–c05; E17–E20 = 0/16/0 · 26; E21 = 100 |
| F-72 | W4 ◀ | CONFIRMED — FIXED | Baru (putaran 2): depends_on K1.c01–c17, K2.c01–c06, K3.c01–c03 mensyaratkan isian sah (collection_validity); K2.c07–c08 tetap independen; akun tak dikenal dan struktur luar rusak diperjelas dengan kontrak yang ada; fixture E19, E20; `sim_w04.py` 34 asersi dependensi + uji mutasi |

Ringkasan (45 ID, satu disposisi per ID; bukan 45 cacat aktif): FIXED 39 · NOT REPRODUCED 1 · DOCUMENTATION CLARIFIED 5. ◀ = berlaku untuk modul ini.

### 13.2 Matriks bukti per butir

Kolom 1–10 = kriteria re-audit: 1 kompetensi/LO · 2 akurasi akademik ·
3 asumsi model eksplisit · 4 kunci benar dan tunggal · 5 pengecoh sah ·
6 skor deterministik · 7 maksimum tercapai · 8 kesetaraan varian ·
9 umpan balik · 10 visibilitas. **A** = diperiksa otomatis (pemeriksa
struktur: ID unik, kunci di opsi, rasional per pengecoh, poin, kompetensi;
pemindai V-L); **S** = jawaban dihitung ulang independen (simulasi, mis.
`ipaddress`, `urlsplit`, `10**n`); **M** = dibaca manual oleh penyusun;
— = tidak berlaku. Semua sel lolos pada putaran ini; kolom "Koreksi" =
temuan yang menyentuh butir itu. Ini review mandiri, bukan review independen.

| Butir | Komp. | Format · D | Kunci vA / vB | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Koreksi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-s01 | cia-01 | TF-1 · D1 · 2 | `a` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s02 | cia-01 | TF-4 · D2 · 3 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s03 | cia-01 | TF-1 · D1 · 2 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s04 | threat-01 | TF-1 · D1 · 2 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s05 | threat-01 | TF-2 · D2 · 3 | `a,b,d` / `b,c,e` | A | M | M | A | A+M | A | A | M | A | A | F-58 |
| T-s06 | threat-01 | TF-1 · D2 · 3 | `d` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s07 | threat-01 | TF-4 · D3 · 4 | `c` / `a` | A | M | M | A | A+M | A | A | M | A | A | F-52 |
| T-s08 | auth-01 | TF-1 · D1 · 2 | `c` / `b` | A | M | M | A | A+M | A | A | M | A | A | F-53 |
| T-s09 | auth-01 | TF-3 · D1 · 2 | `10000,10.000,10000 kombi` / `100000,100.000,100000 ko` | A | M | M | A+S | — | A | A | M | A | A | F-38, F-42 |
| T-s10 | auth-01 | TF-2 · D2 · 3 | `a,c,d` / `b,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s11 | auth-01 | TF-3 · D3 · 4 | `100,100 kali,100kali` / `1000,1.000,1000 kali,1.0` | A | M | M | A+S | — | A | A | M | A | A | F-38, F-42 |
| T-s12 | phish-01 | TF-1 · D1 · 2 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s13 | phish-01 | TF-3 · D2 · 3 | `verifikasi-akun.test` / `login-bankcontoh.test` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s14 | phish-01 | TF-1 · D3 · 4 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s15 | protect-01 | TF-1 · D1 · 2 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s16 | protect-01 | TF-1 · D2 · 3 | `d` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s17 | protect-01 | TF-2 · D2 · 3 | `a,c,d` / `a,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s18 | incident-01 | TF-1 · D1 · 2 | `a` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s19 | incident-01 | TF-5 · D2 · 3 | `B,D,A,C` / `C,D,A,B` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s20 | incident-01 | TF-1 · D3 · 4 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| C-s01 | cia-01 | CE-S4 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s02 | threat-01 | CE-S2 · 3 | `a,c,e` / `b,c,e` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s03 | auth-01 | CE-S5 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A | F-38, F-53 |
| C-s04 | phish-01 | CE-S1 · 4 | `b` / `a` | A | M | M | A+M | M | A | A | M | A | A | F-36 |
| C-s05 | protect-01 | CE-S2 · 2 | `a,c` / `b,c` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s06 | incident-01 | CE-S3 · 3 | `A,B,C,D` / `A,B,C,D` | A | M | M | A+M | M | A | A | M | A | A | F-37, F-66 |
| L-act-01.vA | threat-01 | 10 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-30, F-52 |
| L-act-01.vB | threat-01 | 10 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-30, F-52 |
| L-act-02.vA | phish-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A | F-29 |
| L-act-02.vB | phish-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A | F-29 |
| L-act-03.vA | cia-01, auth-01, protect-01, incident-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-38, F-42 |
| L-act-03.vB | cia-01, auth-01, protect-01, incident-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-38, F-42 |
| P (spec+rubrik) | semua LO | MR-A | contoh 18 | A | M | M | S | — | A+S | A+S | — | A | A | F-39, F-47, F-52 |
| les-01 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-30, F-52, F-58 |
| les-02 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-53, F-38, F-44, F-47 |
| les-03 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-65, F-36 |
| les-04 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-66, F-54 |
| remedial | semua LO | TPL-14 | — | M | M | M | M | — | — | — | — | M | A | F-67, F-68 |

CE-S3 (s06): kedua varian kini 2 urutan diterima (ABCD, ABDC) — sebelumnya vA hanya 1 dengan petunjuk "Setelah …" yang membuka urutan (temuan putaran ini, diperbaiki bersama F-37); urutan tampilan vA C,A,D,B, vB D,B,A,C. CE-S5 (s03) diperiksa: satu baris salah per varian (vA baris 3 → 1.000; vB baris 2 → "bukan MFA, keduanya yang diketahui"), koreksi tunggal; baris benar lainnya tetap benar di bawah asumsi PIN yang dinyatakan.

### 13.3 Fixture evaluator baru (dokumentasi, bukan evaluator produksi)

| Fixture | Input | Diharapkan | K1/K2/K3 · total | Alasan |
|---|---|---|---|---|
| E14 | F2.G memuat `T11` (ID tidak dikenal) | Daftar G INVALID | 52/18/10 · 90 | `collection_validity` (F-39); akun lain tetap dinilai |
| E15 | F2.E memuat `T1` dua kali | Daftar E INVALID | 52/18/10 · 90 | ID ganda |
| E16 | F3 = {L3, L5, L5} | F3 INVALID | 50/18/0 · 78 | ID ganda; bentuk F4/F5 tetap mendapat K2.c07–c08 |
| E17 | F3 = {L1, L5} | F3 INVALID | 50/18/0 · 78 | L1 bukan pilihan (asli tidak dicentang) |
| E18 | F1.S4 = `WIFI` | Kode tidak dikenal | 57/14/10 · 91 | Hanya K1.c04 dan K2.c01 yang 0 |

Contoh rubrik: **18/18** cocok dengan evaluator dokumentasi. Jumlah rencana bernilai penuh tetap **163.840** (20 himpunan cadangan × 8.192 kombinasi tindakan; diverifikasi enumerasi).

### 13.4 Regresi skor dan durasi

W4: teori 56 (D1 16, D2 24, D3 16; TP-B 40/40/20); S = 1.635 → S_buffer 1.799 → timer **32**, review 13, TA-B 48; lab 30 + 40 + 30 = 100; concept 20; proyek 100. Tidak ada perubahan maksimum, durasi, atau XP (305 XP/modul; 915 untuk
W2–W4). Aturan lulus tetap: 4·e ≥ 3·m per komponen (skor terbaik) dan
Σ bobot·e/m ≥ 80% eksak; pembulatan hanya untuk tampilan.

### 13.5 Visibilitas dan keamanan (QC-06, QC-11, VC-1–VC-5)

Pemindai V-L dijalankan ulang: semua temuan termasuk kategori yang sudah
diterima di bagian visibilitas di atas (fakta yang diajarkan dan diuji
sebagai ingatan; data input fixture yang tampil di spesifikasi; positif palsu
substring). Tidak ada judul pembuka jawaban, urutan tampilan CE-S3 = urutan
jawaban, rasional pengecoh sebelum dinilai, atau contoh rubrik yang membuka
jawaban proyek. D-34 dipertahankan (tanpa enkripsi/proteksi kunci palsu).
Semua skenario fiktif dan defensif; tidak ada kredensial nyata, kode
berbahaya, sistem tanpa izin, atau latihan ofensif.

### 13.6 Pedagogi

Penjelasan mendahului penilaian; koreksi putaran ini menambah koreksi
miskonsepsi pada pelajaran yang tersentuh (kolom "Koreksi" di §13.2) tanpa
menambah menit (anggaran 480 menit tetap). Latihan terbimbing berbeda dari
butir bernilai (dicek silang). Tidak ada ketergantungan pada W5–W16. Tidak
diklaim setara universitas atau efektivitas belajar tervalidasi.

### 13.7 Regresi F-01–F-27

F-01–F-23 (kebenaran rubrik dan kredit independen, distribusi kunci,
kesetaraan varian, enumerasi solusi sah, asumsi akademik, field kanonik,
maksimum tercapai, normalisasi, visibilitas, satuan desimal/biner, kualitas
bukti): diperiksa ulang lewat pemeriksa struktur, simulasi, dan pemindai yang
sama — lolos. F-24–F-27 (pengerasan alur kerja) dipertahankan: tidak ada
perubahan pada `.claude/`, izin, hooks, allowed-tools, asal skill, atau
kontrak alur kerja. V03 tetap verifikasi sesi baru yang dilaporkan
sebelumnya; **tidak** dijalankan ulang di putaran ini.

### 13.8 Batas dan metrik putaran koreksi

*Historis (putaran 1):* temuan F-55, F-56, F-57, F-59 saat itu **BLOCKED** — penutupan penuh register tidak
diklaim. Metrik (perkiraan dari transkrip, ±10%): satu putaran koreksi untuk
W2–W4 bersama; aksi gagal yang tercatat: patch multi-pasangan yang gagal
total (dijalankan ulang per pasangan) dan beberapa total fixture hitungan
tangan yang salah (dikoreksi dari evaluator dokumentasi); pemulihan sesi 1
(konteks diringkas). TOKEN USAGE: **NOT MEASURABLE**.

## 14. Koreksi terarah putaran 2 (delta review PR #27; 2026-11-24)

Delta review independen = **REQUEST CHANGES**. Sebelum mengedit
diverifikasi: PR #27 terbuka, belum di-merge; head
`145bb5693320c322eda4d7ea0d08b0a284018c9e`, base
`ab0103e4954ead4ded6343d105d73a2729916cd6`, branch `planning/cb1-w02-w04`.
Register di §13.1 kini memuat **45 ID** (F-28–F-72) dengan satu disposisi
per ID; deskripsi F-55, F-56, F-57, F-59 dipulihkan owner, sehingga tidak
ada lagi yang BLOCKED karena rincian hilang. F-49–F-51 mengikuti deskripsi
asli; koreksi putaran 1 yang tercatat di bawah ID itu dipertahankan.

### 14.1 Perubahan dan bukti modul ini

| ID | Perubahan putaran 2 | Bukti terjalankan |
|---|---|---|
| F-52 | Aturan kategori utama berurutan (aturan pertama yang cocok): `lessons/les-01.md`, `lab/act-01/spec.md`, `checks.yaml` `primary_classification_rule`, `theory/items/s07.yaml`, `project/spec.md` | Penelusuran manual 20 skenario lab + 6 kejadian proyek + 6 kejadian s07: tepat satu aturan pertama yang cocok = kunci yang ada; kunci tidak berubah |
| F-53 | `theory/items/s08.yaml` vB, `concept/items/s01.yaml` (R2, L4), `concept/items/s03.yaml` vB baris 3, `lessons/les-02.md`, `remedial/remedial.md`, `theory/items/s01.yaml` rasional d | Kunci tetap; baris 3 s03 vB tetap benar (baris salah tetap 2) |
| F-54 | `theory/items/s16.yaml` pembahasan vA/vB: lima jenis media CB-2 dan hitungan per rencana | Kunci tetap d / c; `sim_w04.py` model 3-2-1 lolos |
| F-55 | `theory/items/s19.yaml` vA: prasyarat akses Nia + batas urutan dunia nyata | Urutan diterima tetap satu: B, D, A, C |
| F-58 | `concept/items/s01.yaml` vB L1/L2, `theory/items/s02.yaml` vB, `theory/items/s03.yaml` vB: "tanpa izin" / "tidak berhak" | Kunci tetap |
| F-59 | AMN: label di `lab/act-01/checks.yaml` dan spec, skenario vB S10, aturan berurutan (7), umpan balik | Kunci AMN dan poin 3 per pemeriksaan tetap |
| F-72 | `project/rubric.yaml`: depends_on K1.c01–c17, K2.c01–c06, K3.c01–c03 mensyaratkan isian sah; akun tak dikenal dan struktur luar rusak; fixture E19, E20 | Head lama: 28 pemeriksaan tanpa syarat "sah" di depends_on. `sim_w04.py`: 34 asersi "depends_on menyebut isian tak sah ⇒ skor 0" lolos, K2.c07/c08 tetap 2 di semua kasus; uji mutasi (memberi poin larangan untuk daftar tak sah) ditangkap. E14 52/18/10 · 90; E15 52/18/10 · 90; E16 50/18/0 · 78; E17 50/18/0 · 78; E18 57/14/10 · 91; E19 60/20/10 · 100; E20 28/12/6 · 56; 20/20 contoh cocok; ruang solusi tetap 163.840 |

### 14.2 Prosedur validasi (skrip dokumentasi sementara di scratchpad sesi, tidak di-commit)

| Prosedur | Hasil teramati |
|---|---|
| `validate.py mod-w01` … `mod-w04` (struktur, ID unik, kunci di opsi, poin, durasi A.4, field kanonik) | NO ERRORS × 4 |
| `sim_w02.py`, `sim_w03.py`, `sim_w04.py` (evaluator dokumentasi; dihitung ulang tanpa memakai total yang dinyatakan) | W2 22/22 + F-71 OK; W3 21/21; W4 20/20 + 34 asersi dependensi |
| `norm_check.py` (F-51 dan seluruh `normalization_examples`) | 8/8 fixture owner; 107 contoh; ALL OK |
| `scan_vl.py` (V-L) | Hit W2 3 · W3 23 · W4 12 — sama dengan putaran 1, semua kategori yang sudah diterima |
| Inspeksi dokumen | Pembacaan manual penyusun untuk butir yang diubah (bukan review independen) |

Baseline tetap (diverifikasi dari isi): teori 56/56/56; lab 100/100/100;
proyek 100/100/100; concept 20/21/20; timer 33/32/32 menit; TP-B 8/8/4
slot; XP 305 per modul (915); 480 menit per modul; bobot 30/40/20/10, lulus
≥ 75 per komponen dan ≥ 80 berbobot (eksak). Tidak ada runtime yang
diverifikasi; tidak ada evaluator produksi.

### 14.3 Regresi F-01–F-27

Pemeriksa yang sama dengan putaran 1 lolos (kunci, kesetaraan varian,
maksimum, normalisasi, visibilitas, satuan desimal/biner, enumerasi solusi:
W2 1, W3 78.485.511.600, W4 163.840 — tidak berubah). F-24–F-27
dipertahankan: tidak ada perubahan `.claude/`, izin, hooks, allowed-tools,
asal skill, atau kontrak alur kerja; W1 tidak diubah. V03 tidak dijalankan
ulang. TOKEN USAGE: **NOT MEASURABLE**.


## Penerimaan W4 (W04-ACC) dan batas review independen

PR #27 di-merge (head `1a58338bcc863320ff4eafbb0f407cee4b2a9f59`, merge commit `846051f66ee4d1e36e9b34e0c9d1787fb713617b`). Owner menerima W4 (W04-ACC, 2026-11-24).

Verdict independen: **PASS — targeted delta review with disclosed limitations.** Batas review independen (dinyatakan owner): delta review terarah PASS — F-49–F-59 dan F-71–F-72 lolos review terarah; integritas register F-28–F-72 diverifikasi; 16 simulasi normalisasi independen lolos. Regresi historis penuh, semua skrip validasi sementara, uji dengan pelajar, dan verifikasi runtime Android **tidak** diulang secara independen.

Register F-01–F-72 dan disposisinya di atas tetap sebagai catatan historis (39 FIXED, 5 DOCUMENTATION CLARIFIED, F-31 NOT REPRODUCED pada F-28–F-72). Penerimaan ini **bukan** verifikasi menyeluruh, verifikasi runtime, atau uji durasi dengan pelajar; temuan baru tetap boleh diangkat. Bukti aktivasi V03 tetap dari sesi segar sebelumnya.

## Penyelarasan kebijakan D-39 (2026-11-25) — bukan perubahan disposisi historis

Owner menyetujui **D-39 HYBRID COMPETENCY COVERAGE**. Audit cakupan
([CURRICULUM_COVERAGE_MATRIX_W01_W08.md](../../docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md))
menemukan celah **di bawah kontrak baru** (bukan kegagalan terhadap kontrak
saat W4 diterima). Koreksi minimum (format, poin, kesulitan,
kompetensi, dan distribusi posisi kunci tetap; `item_version: '2.0'`):

| Butir | Perubahan | Konsep yang dijamin |
|---|---|---|
| concept s02 vB | opsi a → phishing bukan rekayasa sosial (salah); kunci tetap | phishing sebagai rekayasa sosial |
| concept s04 vA | kunci b juga menyatakan arti HTTPS | HTTPS bukan bukti identitas |
| concept s05 vA | opsi b → perlindungan "menjamin" (salah); kunci tetap | perlindungan tidak menjamin |

Penerimaan W04-ACC tetap tercatat untuk isi yang diterima. Varian yang
diubah di atas **tidak** tercakup penerimaan itu dan memerlukan **review
delta independen** terarah. Register F-01–F-72 tidak berubah.

### Putaran 4 (review `4ddc993`, REQUEST CHANGES) — tindak lanjut D-39

| ID | Tindakan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R3-06 | concept s02 vB (3.0) opsi e: tanda = alasan waspada, belum bukti pasti (benar); kunci b, c, e tetap | CONFIRMED — FIXED | YA | BELUM |
| R3-07 | concept s05 vA (3.0): stem "pernyataan yang benar"; opsi b satu klaim "menjamin data tidak akan pernah hilang" (salah); kunci a, c tetap | CONFIRMED — FIXED | YA | BELUM |
| R3-08 | Status penerimaan terstruktur TPL-01a di `module.yaml` → `acceptance` (historis tetap; varian revisi PENDING) | CONFIRMED — FIXED | YA | BELUM |

Register kesetaraan dan cakupan: [CURRICULUM_COVERAGE_MATRIX_W01_W08.md](../../docs/CURRICULUM_COVERAGE_MATRIX_W01_W08.md).
Penerimaan W04-ACC tetap historis; varian revisi belum diterima.

