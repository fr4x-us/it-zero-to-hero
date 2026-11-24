# IT ZERO → HERO — Decision Sheets Konten Kurikulum (CU-3, CU-5, CU-7, CU2-O3, CU-11)

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa
parser, mesin konten, mesin SQL, WebView, simulator Git, skema database, atau
prototipe. Tanggal: **2026-11-24**. Basis: `main` = `928e278`. Kode
rujukan: `CCD:`. Direvisi setelah review PR #24 (F-07–F-09).

Rekomendasi adalah saran, **bukan** keputusan. Semua bagian terkait UW-36
(CU-3, CU-5, CU-7, CU-11, CU2-O3 — D-25) dan menjadi prasyarat CB-0
([CURRICULUM_PRODUCTION_PLAN.md](CURRICULUM_PRODUCTION_PLAN.md)).

Batasan bersama: 16 modul, urutan terkunci (BL:15–24, D-01 M-02); 64
komponen (D-13); 128 jam (BL:15); materi inti offline, video opsional
(BL:24); Bahasa Indonesia dengan istilah Inggris dijelaskan (CUR:CC-03);
diagram berdeskripsi teks (CC-10); penilaian objektif tanpa AI (BL:38);
minSdk 29 (D-05); konten Python dapat diterima sebagai perencanaan sebelum
runtime (RM:RV-1–RV-6).

---

## A. CU-3 — Format konten

### A.1 Opsi format sumber

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **CF-A Markdown terbatas + YAML** | Teks pelajaran dalam subset CommonMark (judul, paragraf, daftar, tabel, blok kode, kutipan, tautan internal); soal, kunci, rubrik, test, fixture dalam file YAML terstruktur | Mudah ditulis dan direview di GitHub; diff jelas; pemisahan materi vs kunci | Perlu langkah konversi ke format aplikasi kelak |
| CF-B JSON blok saja | Semua konten sebagai blok JSON | Langsung dapat dibaca mesin | Sulit ditulis/direview manusia |
| CF-C HTML | Pelajaran sebagai HTML | Kaya format | Render butuh WebView (belum diverifikasi); risiko markup tak terkontrol |
| CF-D XML khusus | Skema sendiri | Validasi ketat | Beban alat dan penulisan tinggi |

### A.2 Elemen konten (usulan untuk CF-A)

| Elemen | Representasi sumber | Catatan |
|---|---|---|
| Penjelasan, judul, teks terstruktur | Markdown terbatas; maks. 3 tingkat judul | Tanpa HTML mentah |
| Tabel | Tabel Markdown dengan baris judul | Wajib keterangan bila tabel memuat data penting |
| Diagram | SVG sumber + **deskripsi teks wajib** (`alt` singkat + deskripsi panjang) | Cara menampilkan di Android (VectorDrawable, raster, atau lainnya) diputuskan saat implementasi; NOT VERIFIED |
| Contoh kode | Blok kode berlabel bahasa (`python`, `sql`, `html`, `css`, `text`) | Contoh output ditulis terpisah sebagai teks |
| Gambar | PNG/WebP + teks alternatif wajib | Tanpa gambar yang memuat teks penting tanpa padanan teks |
| Soal, kunci, aturan kredit | YAML per soal: `item_id`, `item_version`, `competency`, `format`, `difficulty`, `points`, opsi, kunci, jawaban alternatif, pembahasan | Kunci tidak pernah berada di file pelajaran |
| Rubrik | YAML: kriteria, poin integer, metode evaluasi, wajib/tidak | CU2-O4, CU-9 |
| Test lab dan fixture | YAML test (input, output diharapkan, poin, timeout, terlihat/tersembunyi) + file fixture | D-24 |
| Metadata aksesibilitas | `alt`, deskripsi panjang, penanda istilah bahasa Inggris (`lang: en`), urutan baca, deskripsi tabel | CC-10, UI spec |
| Versi konten | `content_version` per modul + `item_version` per soal; mayor/minor | XP:XI-4, CUR §4.1 |

### A.3 Struktur folder usulan (belum dibuat; dibuat mulai CB-1)

```
curriculum/
  mod-w01/
    module.yaml            # identitas, tujuan, prasyarat, durasi, kompetensi
    lessons/les-01.md      # materi
    theory/blueprint.yaml  # slot soal ujian
    theory/items/*.yaml    # soal + varian + kunci
    lab/act-01/spec.md     # instruksi
    lab/act-01/tests.yaml  # test case
    lab/act-01/fixtures/   # data uji
    project/spec.md        # mini-project
    project/rubric.yaml
    concept/items/*.yaml
    remedial/*.md
    review.md              # checklist CPP §7
```

Mekanisme pembaruan konten V1: **UP-A** hanya bersama pembaruan APK
(direkomendasikan; selaras D-08 bahwa `INTERNET` hanya untuk fitur
opsional); UP-B unduhan paket konten (butuh keputusan jaringan, tanda tangan
paket, dan validasi — tidak direkomendasikan untuk V1).

Rekomendasi: **CF-A + A.2 + A.3 + UP-A.** Alasan pendidikan: penulis dan
reviewer fokus pada isi; kunci terpisah dari materi. Implikasi teknis: format
aplikasi (mis. JSON hasil konversi) dan parser diputuskan saat implementasi;
YAML hanya format penulisan. Ketergantungan: OP-5 (field soal), D-23/D-24
(field kredit dan test), OP-8 (ID).

AC: CCD-AC-01 — setiap elemen A.2 punya representasi tertulis; CCD-AC-02 —
contoh satu soal, satu test lab, dan satu rubrik ditulis dalam templat CB-0.

---

## B. CU-5 — Varian remedial

### B.1 Opsi jumlah minimum

Asumsi beban — **asumsi struktur yang butuh persetujuan eksplisit (CU2-O5, §F)**: 6 soal concept explanation per modul dan 3 aktivitas lab per modul; jumlah pelajaran dan set latihan per modul belum diasumsikan. Usulan dari OP-5 dan §D: slot ujian teori 15 × 20 + 10 =
**310**; concept explanation 6 soal × 16 = **96** slot; lab 3 aktivitas × 16
= **48** aktivitas; mini-project 15 + capstone 1.

| Opsi | Teori (per slot) | Concept (per slot) | Lab (per aktivitas) | Total soal teori | Total soal concept | Total spesifikasi lab |
|---|---|---|---|---|---|---|
| VR-A | 2 | 2 | 1 (tanpa varian lab) | 620 | 192 | 48 |
| **VR-B** | 2 | 2 | 2 (soal sama tujuan, data/fixture berbeda) | 620 | 192 | 96 |
| VR-C | 3 | 3 | 2 | 930 | 288 | 96 |

Mini-project (W1–W15) dan capstone: **MPV-A** attempt remedial memperbaiki
submission sebelumnya (salinan, SB-11), dengan fixture uji tersembunyi tetap;
MPV-B brief varian baru per attempt (beban konten dua kali lipat). MPV-A
lebih bernilai pendidikan (belajar memperbaiki kesalahan sendiri).

### B.2 Aturan kesetaraan dan pemilihan (usulan)

| ID | Aturan |
|---|---|
| VA-1 | Varian setara = kompetensi sama, format sama, kesulitan sama, poin maks. sama, tujuan belajar sama; direview manusia (CC-06) |
| VA-2 | Pemilihan deterministik per slot: pilih varian dengan jumlah pemakaian paling sedikit dalam riwayat attempt pelajar untuk komponen itu; seri → varian yang **tidak** dipakai attempt sebelumnya; masih seri → indeks varian terkecil |
| VA-3 | Setelah semua varian terpakai, pemakaian ulang mengikuti VA-2 (bergiliran); remedial tetap tanpa batas tanpa bank tak terbatas |
| VA-4 | Pemilihan dicatat pada attempt (ID varian + versi) sehingga hasil dapat ditafsirkan dan dihitung ulang setelah restore |
| VA-5 | Varian berbagi identitas XP (XP:XI-3) |
| VA-6 | Latihan adaptif (CUR:RM-06) memakai soal latihan non-ujian; tidak mengurangi pool ujian |

Contoh VA-2 dengan 2 varian (A, B): attempt 1 → A; attempt 2 → B; attempt 3
→ pemakaian A = 1, B = 1, sebelumnya B → A; attempt 4 → B.

Rekomendasi: **VR-B + MPV-A + VA-1–VA-6.** Alasan: dua varian mencegah
pengulangan soal identik pada remedial berikutnya; beban konten tetap
realistis untuk D-21. Bila owner memilih VR-C, beban teori naik 50%.

AC: CCD-AC-03 — CUR:CC-05 terisi (N); CCD-AC-04 — aturan VA-2 menghasilkan
urutan yang sama bila dihitung ulang dari riwayat.

---

## C. CU-7 — Bentuk lab SQL, HTML/CSS, dan Git

Spesifikasi pendidikan saja. Mekanisme eksekusi (mesin SQL, WebView,
simulator Git) diputuskan saat implementasi dan **NOT VERIFIED**.

### C.1 SQL (W13)

| ID | Usulan |
|---|---|
| SQ-1 | Dialek: SQLite. Versi SQLite bawaan Android berbeda antarversi OS/perangkat (NOT VERIFIED untuk API 29+); kurikulum membatasi diri pada SQL dasar: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, agregat + `GROUP BY`/`HAVING`, `INNER JOIN`/`LEFT JOIN`, `INSERT`/`UPDATE`/`DELETE`, `CREATE TABLE` sederhana. Fitur lanjutan (window function, `RIGHT JOIN`) tidak dipakai |
| SQ-2 | Dataset fixture: satu skema latihan bertema toko (pelanggan, produk, pesanan, item_pesanan), ≤ 50 baris per tabel, sengaja memuat `NULL`, baris duplikat, dan relasi tanpa pasangan untuk latihan `LEFT JOIN` |
| SQ-3 | Setiap lab punya fixture **terlihat** dan fixture **tersembunyi** berisi data berbeda dengan skema sama, agar query yang hanya mencetak nilai tetap gagal |
| SQ-4 | Validasi hasil `SELECT`: jumlah kolom dan urutan kolom dibandingkan; nama kolom hanya dibandingkan bila soal meminta alias tertentu |
| SQ-5 | Urutan baris: bila soal mewajibkan urutan, soal **wajib** menulis `ORDER BY` yang menentukan urutan penuh (kunci pengurut + tie-break sampai unik) dan perbandingan dilakukan **berurutan**; bila soal tidak mewajibkan urutan, perbandingan sebagai **multiset** (duplikat dihitung). Soal dengan urutan wajib tetapi tie tanpa tie-break ditolak saat review konten |
| SQ-6 | `NULL` dianggap sama dengan `NULL` dalam perbandingan hasil (bukan semantik SQL); kelas nilai dibandingkan (bilangan bulat ≠ teks "1"). Bilangan real: fixture dan soal diutamakan bilangan bulat; bila hasil real tidak terhindarkan (mis. `AVG`), soal menetapkan `ROUND(ekspresi, n)` dan nilai dibandingkan sebagai teks hasil pembulatan dengan tepat `n` desimal; perbandingan real mentah tidak dipakai |
| SQ-7 | Query setara diterima karena penilaian berdasarkan hasil, bukan teks query |
| SQ-8 | Soal DML dinilai dari keadaan tabel setelah eksekusi; database latihan terpisah dan di-reset per evaluasi (CUR:S-04, QG LB-6) |
| SQ-9 | Pernyataan di luar cakupan (mis. `ATTACH`, `PRAGMA`, ekstensi) ditolak sebagai kesalahan pelajar; mekanisme isolasi NOT VERIFIED |

### C.2 HTML/CSS (W14)

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **HV-A Validasi struktur** | Dokumen diurai; diperiksa properti objektif: elemen ada, nesting, atribut, teks, deklarasi CSS pada selector tertentu | Deterministik, tidak bergantung versi WebView | Tidak menilai tampilan akhir |
| HV-B Render/screenshot | Bandingkan hasil render | Menilai tampilan | Tidak deterministik antarversi WebView/perangkat; ditolak untuk skor |

| ID | Usulan (HV-A) |
|---|---|
| HT-1 | Latihan terstruktur: membuat kerangka dokumen (`<!DOCTYPE html>`, `lang`, `head`, `title`, `body`), judul berurutan, daftar, tautan, gambar dengan `alt`, tabel, formulir sederhana |
| HT-2 | Properti yang diperiksa contohnya: "ada tepat satu `h1`", "`img` memiliki `alt` tidak kosong", "`nav` berisi ≥ 3 `a`", "selector `.kartu` memiliki `padding`" |
| HT-3 | Persyaratan tata letak diperiksa lewat deklarasi (mis. `.wadah { display: flex; }`), bukan hasil layout terhitung |
| HT-4 | Solusi alternatif yang valid lolos selama properti terpenuhi |
| HT-5 | Pratinjau offline: dianjurkan secara pendidikan; **tidak dinilai**; bergantung kemampuan WebView tanpa jaringan (NOT VERIFIED). Lab tetap dapat dinilai bila pratinjau tidak tersedia |

### C.3 Git/GitHub (W15)

Tidak ada Git CLI di Android (CUR §2).

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **GS-A Simulasi keadaan** | Model repositori: working tree, staging, commit, branch, HEAD; pelajar memakai subset perintah; penilaian berdasarkan **keadaan akhir** | Deterministik; offline; fokus konsep | Bukan Git asli |
| GS-B Pustaka Git nyata di perangkat | Menjalankan Git sungguhan | Autentik | Berat; risiko implementasi; belum diverifikasi |
| GS-C Kuis saja | Pilihan dan urutan | Paling ringan | Tidak ada praktik |

| ID | Usulan (GS-A) |
|---|---|
| GT-1 | Konsep: repositori, working tree, staging, commit, pesan commit, log, branch, switch/checkout, merge fast-forward, merge tiga arah, konflik |
| GT-2 | Subset perintah: `init`, `status`, `add`, `commit -m`, `log`, `branch`, `switch`, `merge`; resolusi konflik dengan memilih/menyunting isi file lalu `add` + `commit` |
| GT-3 | Penilaian: graf commit (jumlah, induk), posisi branch, isi file per commit, tidak ada penanda konflik tersisa; teks perintah tidak dinilai |
| GT-4 | GitHub (remote, push, pull, pull request) diajarkan sebagai konsep dan simulasi tanpa jaringan; interaksi GitHub nyata hanya opsional di luar aplikasi dan tidak dinilai |

Rekomendasi: **SQ-1–SQ-9 + HV-A (HT-1–HT-5) + GS-A (GT-1–GT-4).** Alasan
pendidikan: menilai hasil, bukan hafalan sintaks; latihan tetap realistis.
Implikasi teknis: tiga pemeriksa deterministik terpisah (implementasi
kelak). AC: CCD-AC-05 — setiap jenis lab punya aturan validasi tertulis;
CCD-AC-06 — fixture SQL mencakup `NULL`, duplikat, dan baris tanpa pasangan.

---

## D. CU2-O3 — Alokasi 128 jam (menggantikan usulan lama CPP §5)

Kategori: **M** materi pelajaran dan latihan; **U** penilaian teori (ujian +
membaca hasil); **L** lab; **P** mini-project/capstone; **C** concept
explanation; **R** review terjadwal dan persiapan remedial.

| Modul | M | U | L | P | C | R | Total |
|---|---|---|---|---|---|---|---|
| W1–W4 (fase 1, masing-masing) | 3,0 | 0,75 | 1,5 | 1,5 | 0,5 | 0,75 | 8,0 |
| W5–W8 (fase 2, masing-masing) | 2,5 | 0,75 | 2,0 | 1,5 | 0,5 | 0,75 | 8,0 |
| W9–W12 (fase 3, masing-masing) | 2,5 | 0,75 | 2,5 | 1,5 | 0,5 | 0,25 | 8,0 |
| W13–W15 (fase 4, masing-masing) | 2,5 | 0,75 | 2,5 | 1,5 | 0,5 | 0,25 | 8,0 |
| W16 (capstone) | 0,75 | 0,5 | 1,0 | 5,0 | 0,5 | 0,25 | 8,0 |
| **Total program** | **40,25** | **11,75** | **32,5** | **27,5** | **8,0** | **8,0** | **128,0** |

Pemeriksaan (aritmetika 2026-11-24): M = 4·3 + 8·2,5 + 3·2,5 + 0,75 = 40,25;
U = 15·0,75 + 0,5 = 11,75; L = 4·1,5 + 4·2 + 7·2,5 + 1 = 32,5; P = 15·1,5 +
5 = 27,5; C = 16·0,5 = 8; R = 8·0,75 + 7·0,25 + 0,25 = 8; jumlah = 128.

Catatan: ujian standar 33 menit (OP-5) muat dalam U = 0,75 jam; ujian W16
18 menit muat dalam 0,5 jam. Alokasi ini adalah **waktu belajar**, bukan
bobot penilaian (30/40/20/10 tetap). Waktu remedial tambahan yang
bergantung pada pelajar (attempt ulang) **di luar** 128 jam nominal; R hanya
review terjadwal. Fase 1 memberi lebih banyak waktu materi (pemula); fase 3–4
memberi lebih banyak waktu lab (praktik kode).

Opsi lain: HA-B alokasi seragam semua modul (abaikan perbedaan fase); HA-C
tanpa R (tidak ada waktu review terencana). Rekomendasi: **tabel di atas
(HA-A).** AC: CCD-AC-07 — setiap modul berjumlah 8,0 jam; total 128,0;
CCD-AC-08 — urutan modul tidak berubah.

---

## E. CU-11 — Pembagian Python W9/W10

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **PB-A** (direvisi F-08) | W9: program pertama, `print`, komentar, aritmetika, variabel (penugasan dasar), `input()` **dengan konversi angka dasar** `int()`/`float()` agar perhitungan dari input dapat dilakukan, membaca pesan error; W10: tipe data formal, `type()`, konversi lengkap dan kesalahan konversi (`ValueError` dibaca, tidak ditangani), operasi string, f-string, operasi list dan dict | W9 sudah menghasilkan program bermakna dari input; W10 memperdalam tanpa mengulang | Konversi muncul dua kali (dasar vs lengkap) — tujuan berbeda |
| PB-B | W9 tanpa variabel sama sekali | Batas tegas | Program W9 sangat terbatas; lab sulit bermakna |
| PB-C | List/dict dipindah ke W12 | W10 lebih ringan | W12 terlalu padat (loop, fungsi, debugging, struktur data) |

### E.1 Rincian PB-A

| Aspek | W9 Dasar Python | W10 Variabel dan tipe data |
|---|---|---|
| Tujuan | Menulis dan menjalankan program berurutan; membaca pesan error | Memilih tipe yang tepat; mengonversi input; mengolah teks dan koleksi sederhana |
| Urutan topik | 1) apa itu program/interpreter; 2) `print` dan string literal; 3) komentar; 4) aritmetika `+ − * / // % **` dan prioritas; 5) variabel dan penugasan; 6) `input()` (hasil selalu teks) dan konversi dasar `int(input())`, `float(input())`; 7) `SyntaxError`/`NameError`/`ValueError` dan cara membacanya | 1) tipe `int`, `float`, `str`, `bool`; 2) `type()`; 3) konversi lengkap `int()`, `float()`, `str()`, `bool()` dan kapan konversi gagal (`ValueError` dibaca, **tanpa** `try`/`except`); 4) string: gabung, `len`, indeks, slicing, metode umum (`upper`, `strip`, `split`, `isdigit`); 5) f-string; 6) list: buat, indeks, slicing, `append`, `len`, `in`; 7) dict: buat, ambil/ubah nilai lewat kunci, `keys`/`values` |
| Prasyarat | W5 (operasi, modulo), W8 (algoritma berurutan) | W9; W6 (nilai Boolean) |
| Progresi latihan | Cetak → hitung → simpan dalam variabel → baca input dan konversi → hitung dari input → perbaiki error | Pilih tipe → konversi dan jelaskan kegagalan → format output → olah string → kumpulkan data di list/dict (jumlah elemen tetap) |
| Kompetensi akhir | Program 5–15 baris berurutan yang membaca angka, menghitung, dan mencetak hasil | Program berurutan yang mengonversi input dan mengolah teks/list/dict **tanpa** percabangan, perulangan, atau penanganan exception |
| Dipakai di W11 | Ekspresi, variabel | `bool`, perbandingan nilai bertipe, konversi input |
| Dipakai di W12 | Membaca error | List/dict untuk iterasi; string untuk fungsi |
| Dipakai di W16 | Struktur program dasar | Pengolahan data teks, list, dict |

Pemeriksaan prasyarat proyek (F-08): W9 "kalkulator konversi satuan" =
input + `float()` + aritmetika + `print` (semua W9). W10 "pengolah profil
teks" = jumlah field tetap, metode string, list/dict, f-string (W9–W10,
tanpa percabangan). W11 "penentu kategori" = kondisi (W11) + konversi (W10).
W12 "rekap nilai" = perulangan dan fungsi (W12) atas list/dict (W10).
Capstone = W9–W12 + SQL W13 + Git W15; validasi baris memakai `isdigit`/
`split`/`len` (W10) dan kondisi (W11), **tanpa** `try`/`except`. Tidak ada
proyek yang memakai konsep sebelum diajarkan.

Operator perbandingan dan logika diajarkan di W11 (kondisi) dengan tipe
`bool` dari W10. Penerimaan perencanaan W9/W10 tidak bergantung pada hasil
runtime (RM:RV-1).

Rekomendasi: **PB-A.** AC: CCD-AC-09 — setiap topik W9–W12 dan kebutuhan
capstone muncul tepat satu kali sebagai topik utama; CCD-AC-10 — tidak ada
topik yang dipakai sebelum diajarkan.

---

## F. Pertanyaan untuk owner

| ID | Pertanyaan | Rekomendasi |
|---|---|---|
| CU-3-Q1 | Format sumber CF-A (Markdown terbatas + YAML) dengan elemen A.2? | CF-A |
| CU-3-Q2 | Struktur folder A.3 dan pembaruan konten hanya lewat APK (UP-A) untuk V1? | Ya |
| CU-5-Q1 | Jumlah varian VR-B (teori 2, concept 2, lab 2) dan MPV-A untuk mini-project/capstone? | VR-B + MPV-A |
| CU-5-Q2 | Aturan kesetaraan dan pemilihan deterministik VA-1–VA-6? | Ya |
| CU2-O5-Q1 | Asumsi struktur: 6 soal concept explanation per modul dan 3 aktivitas lab per modul (dasar perhitungan beban §B dan durasi C = 0,5 jam), disetujui sebelum produksi konten final? | Ya |
| CU-7-Q1 | SQL: SQ-1–SQ-9 (SQLite, SQL dasar, perbandingan multiset/berurutan, NULL)? | Ya |
| CU-7-Q2 | HTML/CSS: HV-A, pratinjau tidak dinilai (HT-1–HT-5)? | HV-A |
| CU-7-Q3 | Git: GS-A simulasi keadaan; GitHub nyata opsional dan tidak dinilai (GT-1–GT-4)? | GS-A |
| CU2-O3-Q1 | Alokasi jam tabel §D (M/U/L/P/C/R) dan remedial tambahan di luar 128 jam nominal? | Ya |
| CU-11-Q1 | Pembagian PB-A (revisi F-08) W9/W10? | PB-A |

Status: **AWAITING OWNER**. UW-36 tetap BLOCKED (CU-3, CU-5, CU-7, CU-9,
CU-11, CU2-O3, CU2-O4 belum diputuskan).
