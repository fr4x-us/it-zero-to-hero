---
module_id: mod-w04
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-1. Belum direview ChatGPT; belum diterima owner"
---

# W4 — Review Kualitas, Kesetaraan Varian, Keamanan Konten, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-1) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review ChatGPT | **BELUM** |
| Diterima owner | **BELUM** |
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
| Proyek | 100 | **100** | E01, E02, E08 = 100 (13/13 cocok dengan evaluator) |
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
| QC-02 | PASS | §5.3 (13/13) |
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
| Temuan terbuka | Tidak ada yang diketahui; butuh review ChatGPT dan penerimaan owner |

Metrik W4 (dari transkrip; ±2): panggilan alat ≈ 22; berkas baru dibaca 0;
baca ulang 0; aksi gagal 0; temuan pemeriksa yang benar 5 (2 tumpang-tindih
angka, 1 tumpang-tindih lab, 1 butir ambigu, bias kunci); positif palsu
skrip 2 (pemetaan nama media, `.co.id` penjelasan); kegagalan identik
berulang 0; aktivasi skill 0 tambahan; checkpoint 1; operasi validasi 6;
pemulihan sesi 0. TOKEN USAGE: **NOT MEASURABLE**.
