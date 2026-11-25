# IT ZERO → HERO — Standar Produksi Kurikulum (CB-0)

Status (dibedakan; diperbarui setelah merge PR #25, D-38, W01-ACC):

| Aspek | Status |
|---|---|
| Keputusan kebijakan owner yang dibutuhkan templat | **Semua terputuskan** (D-12, D-13, D-21, D-23–D-36). Kebijakan umpan balik test tersembunyi = D-36 (HF-A) |
| Kelengkapan templat (TPL-01–TPL-20, §1a, §3a, §3b) | **Lengkap** sebagai dokumentasi; tidak ada field yang bergantung keputusan terbuka. Nilai angka batas agregat LX-2 bukan field templat (hasil pengukuran, UW-12) |
| Dapat dipakai | W1–W16 (lab kode W9–W12, W16 kini memiliki aturan umpan balik test tersembunyi) |
| Review independen (ChatGPT) | **Lolos review akhir PR #25** dengan batas: F-22 dan F-23 menerima review akhir terarah; pencatatan D-36/D-37 diperiksa; enumerasi independen mengonfirmasi 3.840 kombinasi dan 46 build valid. **Tidak** setiap baris CSV terbaru, setiap butir penilaian yang berubah, atau setiap penerapan kontrak visibilitas diaudit ulang secara independen. |
| Penerimaan owner | CB-0 sendiri: tidak ada keputusan penerimaan terpisah. Modul W1 yang disusun dengan CB-0 **diterima** (W01-ACC) |
| Verifikasi implementasi teknis | Tidak berlaku (tidak ada implementasi; D-10, D-11) |

CB-0 **tidak** dinyatakan final secara global: belum ada penerimaan owner
terpisah untuk CB-0, dan review independen bersifat terbatas. Templat **bukan** konten dan
tidak dihitung sebagai komponen selesai. Tanggal: **2026-11-24**. Basis:
`main` = `40ca205` (merge PR #24). Kode rujukan: `TPL:`.

Dasar keputusan: D-12, D-13, D-21, D-23 (concept), D-24 + D-35 (lab), D-26
(teori), D-27 (pengumpulan, unlock, remedial, autosave), D-28 (XP), D-30
(format CF-A, varian VR-B, struktur CU2-O5), D-31 (SQL/HTML/Git), D-32 (jam
HA-A, PB-A), D-33 (rubrik MR-A, capstone), D-34 (kunci jawaban).
Contoh penerapan lengkap: [`curriculum/mod-w01/`](../curriculum/mod-w01/module.yaml).

## 1. Struktur berkas (CU-3 A.3, D-30)

```
curriculum/mod-wNN/
  module.yaml              TPL-01, -02, -03, -15, -17, -18
  lessons/les-NN.md        TPL-04, -05, -06, -16   (front matter YAML + Markdown terbatas)
  theory/blueprint.yaml    TPL-07
  theory/items/sNN.yaml    TPL-07, -08, -14        (kunci; bukan untuk pelajar sebelum dinilai)
  lab/act-NN/spec.md       TPL-09                  (instruksi untuk pelajar)
  lab/act-NN/checks.yaml   TPL-09, -10, -14        (kunci, poin, fixture)
  project/spec.md          TPL-11
  project/rubric.yaml      TPL-12                  (pemeriksaan dan kunci K4)
  concept/items/sNN.yaml   TPL-13, -14
  remedial/remedial.md     TPL-14
  review.md                TPL-19, -20
```

**Pemisahan sumber, kunci, dan tampilan:** materi untuk pelajar ada di
`.md`; kunci, pembahasan, dan pemeriksaan ada di `.yaml` dengan komentar
"tidak ditampilkan sebelum dinilai". Kunci tampil hanya pada tahap umpan
balik yang disetujui: teori setelah `GRADED` (FB-A, D-26); concept dan lab
setelah evaluasi; proyek setelah dinilai. Pembahasan **latihan tidak
dinilai** boleh ada di pelajaran, ditampilkan setelah pelajar mencoba.

## 1a. Kontrak visibilitas pelajar / penilai (revisi review PR #25, F-23)

Kontrak ini mengatur **isi dokumen** dalam format konten yang disetujui
(CF-A); tidak menetapkan mekanisme aplikasi. Penerimaan risiko ekstraksi
kunci offline (D-34) tetap berlaku: kontrak ini mencegah pengungkapan
**sengaja** di materi pelajar, bukan perlindungan teknis.

| Kelas | Kapan terlihat | Tempat (CF-A) | Isi yang boleh |
|---|---|---|---|
| **V-L** Pelajar, sebelum dinilai | Selama mengerjakan | `lessons/*.md`; `lab/*/spec.md`; `project/spec.md`; field soal `stem`, `options`, `items`, `left`/`right`, `lines`, `stimulus_table`, `display_order` | Tujuan, prasyarat, instruksi, fixture **dalam urutan tampil acak**, deliverable, aturan skor umum tanpa jawaban, contoh yang **tidak berkaitan** dengan butir bernilai, contoh terlihat bernilai 0 |
| **V-E** Penilai saja, sebelum dinilai | Tidak pernah ditampilkan sebelum dinilai | `theory/items`, `concept/items`, `lab/*/checks.yaml`, `project/rubric.yaml`, `review.md`, `project/evidence/`: `key`, `accepted_answers`, `accepted_sequences`, `key_mapping`, `error_line`, `correction_key`, `expected`, `rule`, `depends_on`, `evaluator_examples`, `reviewer_examples`, `catalog_analysis`, `distractor_rationale` | Kunci, urutan diterima, label benar, contoh jawaban bernilai yang tepat, metadata evaluasi |
| **V-P** Pelajar, setelah dinilai | Sesuai kebijakan umpan balik | Field `explanation` / `feedback`, hasil per pemeriksaan | Jawaban benar bila diizinkan (teori FB-A, D-26; lab non-kode dan concept setelah evaluasi; lab kode: test tersembunyi hanya kode hasil + `case_description`, D-36), penjelasan, arahan remedial |

Aturan:

| ID | Aturan |
|---|---|
| VC-1 | Berkas V-L tidak memuat isi V-E: tidak ada urutan diterima, label benar, pilihan benar, atau contoh jawaban butir bernilai |
| VC-2 | Fixture yang diacak ditulis **dalam urutan tampil**, bukan urutan benar |
| VC-3 | Contoh aturan skor untuk pelajar memakai skenario yang tidak berkaitan dengan butir bernilai |
| VC-4 | Deskripsi bagian "Umpan balik" di berkas V-L hanya menyebut **jenis** umpan balik, tanpa isi jawaban |
| VC-5 | Pembahasan latihan **tidak dinilai** boleh berada di pelajaran (V-P untuk latihan), asalkan tidak sama dengan butir bernilai (QC-06) |

## 2. Konvensi penamaan

| Entitas | Pola | Contoh W1 |
|---|---|---|
| Modul | `mod-wNN` | `mod-w01` |
| Kompetensi | `comp-wNN-<topik>-NN` | `comp-w01-spec-01` |
| Tujuan belajar | `LOn` (lokal modul) ↔ satu kompetensi | `LO6` ↔ `comp-w01-spec-01` |
| Pelajaran | `mod-wNN.les-NN` | `mod-w01.les-03` |
| Set latihan | `mod-wNN.prac-NN` | `mod-w01.prac-03` |
| Komponen | `mod-wNN.theory` / `.lab` / `.project` / `.concept` | `mod-w01.lab` |
| Slot soal | `mod-wNN.<theory\|concept>.sNN` | `mod-w01.theory.s12` |
| Varian | `<slot>.vA` / `.vB` | `mod-w01.theory.s12.vB` |
| ID soal | `item-wNN-<t\|c>-sNN-<a\|b>` + `item_version` | `item-w01-t-s12-b` |
| Aktivitas lab | `mod-wNN.lab.act-NN` | `mod-w01.lab.act-02` |
| Varian lab | `<aktivitas>.vA` / `.vB` | `mod-w01.lab.act-02.vB` |
| Pemeriksaan/test | `<varian lab>.cNN` | `mod-w01.lab.act-02.vB.c06` |
| Kriteria proyek | `mod-wNN.project.K<n>.cNN` / `.qN` | `mod-w01.project.K1.c07` |
| Identitas XP | sama dengan ID pelajaran/latihan/komponen; milestone `mod-wNN.passed`, `program.capstone` | `mod-w01.passed` |
| Versi konten | `content_version` per berkas; `item_version` per soal; `mayor.minor` | `"1.0"` |

## 3. Templat (TPL-01–TPL-20)

Kolom "Dasar" menunjukkan keputusan yang menetapkan field. Semua field wajib
kecuali ditandai opsional.

### TPL-01 Ikhtisar modul (`module.yaml`)

| Field | Isi | Dasar |
|---|---|---|
| `module_id`, `phase`, `week`, `title`, `locked_scope` | Sesuai urutan terkunci | BL:15–24, D-01 M-02 |
| `status` | `documentation`, `reviewed`, `owner_accepted`, `runtime_verified`, `learner_tested` (dipisah) | Instruksi owner batch ini |
| `audience`, `prerequisites`, `nominal_minutes` = 480 | — | D-32 |
| `components` | 4 komponen, bobot 30/40/20/10, maks. poin, berkas | D-13, BL:27–30 |
| `pass_rule` | `4·e ≥ 3·m` per komponen dan W ≥ 80 eksak | D-04, D-12 |
| `unscored_reflection` (opsional) | Refleksi CE-D, `scored: false` | D-23 |
| `acceptance` (TPL-01a, ekstensi D-39 putaran 4) | Wajib bila `status.owner_accepted: YES` dan ada varian yang berubah setelah penerimaan. `historical` {`id`, `date`, `baseline_commit` (commit git isi yang diterima), `basis`, `scope`}; `current_content` ∈ {`ACCEPTED_AS_IS`, `REVISED_PENDING`, `REVISED_ACCEPTED`}; `revised_variants[]` {`variant_id`, `accepted_version`, `current_version`, `reason`, `independent_review` ∈ {`PENDING`, `TARGETED_LIMITED`}, `owner_acceptance` ∈ {`PENDING`, `ACCEPTED`}}; `revision_acceptance` {`id`, `date`, `reviewed_head`, `independent_scope`} bila owner menerima versi revisi (PR #28 ACC). `TARGETED_LIMITED` = tercakup review delta terarah dengan batas diungkapkan, **bukan** verifikasi independen per varian | D-39; `status.owner_accepted` tetap mencatat penerimaan **historis** dan tidak ditimpa. R6-01: `baseline_commit` harus sama dengan jangkar terpisah `docs/validation/trust/acceptance_anchors.yaml` (merge PR penerimaan, tercatat di DECISIONS_LOG); validasi lokal, bukan bukti kriptografis |

**Aturan TPL-01a.** Validator membandingkan setiap varian dengan isinya pada
`baseline_commit` (bukan dengan asumsi versi 1.0): isi sama → versi sama dan
tidak tercatat sebagai revisi; isi berubah → versi naik dan tercatat di
`revised_variants` dengan `accepted_version` = versi baseline (boleh > 1.0)
dan `current_version` = versi berkas; status `PENDING` sampai review
independen dan penerimaan owner. Variant ID ganda, entri ganda, entri
hilang, atau versi salah membuat validasi gagal (`docs/validation/check_acceptance.py`).
Ekstensi ini hanya menambah field; tidak ada field lama yang diubah artinya.

### TPL-02 Prasyarat dan tujuan belajar

`learning_objectives[]`: `id`, `competency`, `text` (kata kerja terukur);
prasyarat modul/kompetensi sebelumnya (linear, D-27 UL). Tidak boleh
mensyaratkan topik modul berikutnya (PB-A untuk W9/W10, D-32).

### TPL-03 Pemetaan kompetensi

`objective_mapping`: setiap LO → pelajaran, latihan, slot teori, pemeriksaan
lab (atau kosong dengan alasan), kriteria proyek, slot concept. Setiap
kompetensi ujian ≥ 2 slot teori (TQ-B, D-26).

### TPL-04 Penjelasan pelajaran (`lessons/les-NN.md`)

Front matter: `lesson_id`, `practice_id`, `content_version`, `duration_minutes`,
`competencies`, `prerequisites`, `accessibility`. Badan: tujuan, mengapa
penting, penjelasan, analogi, contoh nyata, miskonsepsi, ringkasan,
glosarium (istilah Indonesia + Inggris). Markdown terbatas: judul ≤ 3
tingkat, tabel, blok kode berlabel, tanpa HTML mentah (CF-A, D-30).

### TPL-05 Contoh terbimbing

Di dalam pelajaran: soal, langkah berpikir (tabel atau berurutan), jawaban.

### TPL-06 Latihan tidak dinilai

Bagian "Latihan terbimbing (`prac-NN`)" + "Cek pemahaman" + "Pembahasan
latihan (ditampilkan setelah pelajar mencoba)". XP sekali saat set pertama
kali diselesaikan (UG-A, D-28).

### TPL-07 Ujian teori

`blueprint.yaml`: `slot_count` (20; W16: 10), distribusi D1/D2/D3 =
40/40/20, `format_counts`, `competency_counts`, `max_points` (TP-B:
2/3/4), `duration` (rumus A.4; standar 10–45 menit; review terjadwal = U −
standar; TA-B = ⌈standar × 3/2⌉, maks. 68). Per slot: `slot_id`,
`competency`, `format` (TF-1–TF-5), `difficulty`, `max_points`,
`estimated_seconds` (= dasar format + tambahan kesulitan).

### TPL-08 Kunci dan pembahasan teori

Per varian: `item_id`, `variant_id`, `item_version`, `stem`,
`stimulus_table` (opsional, TF-4), `options`, `key` / `accepted_answers` +
`normalization` (TF-3) / `accepted_sequences` (TF-5), `distractor_rationale`
untuk setiap opsi salah, `explanation`. Semua teori semua-atau-tidak (TP-B).

### TPL-09 Spesifikasi aktivitas lab

`spec.md`: tujuan, skenario, prasyarat, instruksi, fixture, contoh
terlihat (0 poin), yang diserahkan, tabel penilaian, kasus gagal, umpan
balik, remedial, durasi. Satu attempt komponen mencakup semua aktivitas
(RA-1); penyerahan per aktivitas dengan konfirmasi (SB-A, D-27). Lab
SQL/HTML/Git mengikuti SQ-1–SQ-9, HV-A/HT-1–HT-5, GS-A/GT-1–GT-4 (D-31).

### TPL-10 Fixture, test, dan hasil yang diharapkan (`checks.yaml`)

| Field | Isi | Dasar |
|---|---|---|
| `variants[].fixture` | Data uji deterministik | LB-5 |
| `checks[]` | `check_id`, `expected`/`accepted_answers`/`rule`, `points` (integer ≥ 1) | LW-B, D-24 |
| Jumlah poin varian | = `max_points` aktivitas; komponen ≤ 10.000 | D-12 |
| `t_ms` per test (lab kode) | `Σ tᵢ ≤ 3.000` per latihan Python; urutan `test_index` deterministik | TB-B, LX-5, D-35 |
| Kode hasil | §5 lembar CU-6 | D-24 |
| `answer_validation` | Kosong/ID asing/ganda → 0 untuk pemeriksaan itu; infrastruktur → `EVALUATION_ERROR` | D-24 IE-2 |
| `visible_example` | Contoh terlihat bernilai 0; pemeriksaan bernilai disembunyikan sampai evaluasi (penerapan CUR:CC-07 untuk lab non-kode) | CC-07 |
| `hidden_test_feedback` | Setelah evaluasi, test tersembunyi menampilkan **kode hasil** (§5 CU-6) dan **`case_description`** saja; tanpa input mentah, output diharapkan, atau output pelajar. Test terlihat menampilkan semuanya | D-36 (HF-A) |
| `case_description` | Wajib untuk setiap test tersembunyi lab kode: deskripsi kasus yang bermakna dan tidak membocorkan nilai (mis. "input kosong", "angka negatif", "daftar satu elemen") | D-36 |

### TPL-11 Spesifikasi mini-project (`project/spec.md`)

Skenario, tujuan, kebutuhan sebagai syarat yang dapat diperiksa, informasi
awal (katalog/fixture), deliverable (formulir), instruksi, contoh dapat
diterima dan tidak dapat diterima, ringkasan penilaian, bukti yang dinilai,
remedial (MPV-A, salinan submission sebelumnya), durasi. W16 = capstone
(tema "Pencatat Sesi Belajar", D-33).

### TPL-12 Rubrik objektif (`project/rubric.yaml`)

MR-A: K1 60 · K2 20 · K3 10 · K4 10 (D-33). Pembagian peran: **K1** kebenaran nilai; **K2** isian ada dan valid secara bentuk (pilihan tertutup = salah satu pilihan tersedia; angka = dapat dibaca menurut aturan angka); **K3** bentuk ketat dan aturan struktur (mis. slot). Satu isian kosong atau salah bentuk dapat kehilangan poin di K1, K2, dan K3 sekaligus; ini konsekuensi definisi MR-A, bukan gerbang nol. Setiap pemeriksaan: `id`,
`rule` yang dapat diperiksa, `depends_on`, `points` integer; jumlah tepat
sama dengan anggaran (MR-8) **dan dapat dicapai bersamaan** (QC-01). K4 dengan komposisi A.2a (jumlah `max_soal`
tepat 10, tanpa penskalaan). Capstone: CR-1–CR-6, MC-1–MC-4, CG-B, CP-1–CP-6.
Pernyataan pelajar = 0 poin (MR-6).

### TPL-13 Bank soal penjelasan konsep (`concept/items/sNN.yaml`)

6 slot per modul × 2 varian (CU2-O5, VR-B, D-30). Per slot:
`required_concepts`, `format` (CE-S1–CE-S5), `max_points` (struktural),
`validation` (CE-V1–CE-V7). Per varian: kunci, `accepted_sequences`
lengkap (CE-S3), `key_mapping` satu-ke-satu (CE-S4), `error_line` +
`correction_key` + P genap (CE-S5), `credit_rule`, `feedback` (D-23).
Cakupan `required_concepts` mengikuti **D-39 (hybrid)**: setiap varian
menilai kompetensi inti slot; setiap konsep wajib dinilai di setiap jalur
penilaian yang sah — di slot ini atau di lokasi wajib lain (teori, lab,
proyek) yang menilainya pada **semua** varian yang dapat dipilih — atau
dengan bukti deterministik setara atas semua jalur sah (QC-13 b). Konsep
yang hanya disebut di stem, pengecoh pilihan tunggal, baris CE-S5 yang
benar, umpan balik, pelajaran, atau remedial tidak dihitung (QC-13).

### TPL-14 Varian remedial

Teori dan concept: 2 varian per slot; lab: 2 varian per aktivitas;
mini-project: MPV-A (tanpa varian). Kesetaraan VA-1 (kompetensi, format,
kesulitan, poin, tujuan sama; direview; dilengkapi D-39: kompetensi inti
sama di setiap varian dan cakupan konsep wajib terjamin di setiap jalur);
pemilihan VA-2 (pemakaian paling
sedikit → bukan varian attempt sebelumnya → indeks terkecil); pemakaian
ulang bergiliran (VA-3); `remedial.md` per LO (D-30).

### TPL-15 Identitas dan kelayakan XP (`module.yaml` → `xp`)

`identities[]`: `xp_id`, `amount`, `eligibility`. Pelajaran 5, latihan 10,
teori 50, lab 70, proyek 50, concept 25, modul lulus 50, capstone 100
(D-28). Komponen: award sekali saat pertama mencapai ambang komponen
(XE-B). `not_identities` wajib dicantumkan (aktivitas lab, varian, latihan
lab, refleksi).

### TPL-16 Metadata aksesibilitas

Di front matter: `diagrams[]` (`id`, `alt`, `long_description`),
`tables_with_core_data`, `english_terms`. Diagram teks di badan pelajaran
diikuti deskripsi tertulis (CC-10).

### TPL-17 Versi konten

`content_version` per berkas; `item_version` per soal; aturan: perbaikan
typo/klarifikasi → minor; perubahan kunci/poin/isi soal → mayor; `xp_id` dan
`item_id` tetap bila tujuan belajar sama (XI-6, D-28).

### TPL-18 Alokasi waktu (`module.yaml` → `schedule`)

`allocation_minutes` M/U/L/P/C/R sesuai HA-A (D-32; jumlah 480);
`theory_exam` (standar, review terjadwal, TA-B); `suggested_sessions`
(saran, bukan tenggat; D-01 M-03); `outside_nominal` (aksesibilitas,
remedial, review opsional).

### TPL-19 Checklist penerimaan konten (`review.md`)

CQ-01–CQ-20 dan QC-01–QC-12 (§3b): kebenaran teknis, ramah pemula, LO terukur, prasyarat, cakupan,
tidak menilai yang belum diajarkan, kelengkapan, kesetaraan varian, kunci,
aritmetika, fixture deterministik, rubrik objektif, concept, XP unik,
aksesibilitas, versi, 480 menit, offline, konsistensi D-01–D-35, kunci tidak
tampil sebelum tahap umpan balik.

### TPL-20 Bukti reviewer

Tabel status terpisah (diproduksi / direview / diterima owner / runtime /
diuji pelajar), inventaris yang dihitung dari berkas, aritmetika, temuan
yang diperbaiki, batas penilaian objektif, reviewer dan tanggal.

## 3a. Field metadata kanonik (revisi review PR #25, F-16)

| Field | Dipakai untuk | Catatan |
|---|---|---|
| `key` | Kunci soal pilihan (teori, concept, K4) | Satu ID atau daftar ID (pilihan ganda) |
| `accepted_answers` | Jawaban singkat teori dan pemeriksaan lab berbentuk teks/angka | Daftar lengkap bentuk yang diterima, huruf kecil |
| `normalization` | Aturan pencocokan `accepted_answers` | Satu nama di teori dan lab (dulu lab memakai `answer_normalization`) |
| `accepted_sequences` | Urutan yang diterima (TF-5, CE-S3, lab urutan) | Dulu lab memakai `expected_sequence` |
| `display_order` | Urutan tampil item urutan | Tidak boleh sama dengan urutan diterima |
| `expected` | Hasil yang diharapkan satu pemeriksaan lab | — |
| `rule` | Aturan pemeriksaan rubrik/lab | Harus deterministik |
| `depends_on` | Isian yang dibutuhkan pemeriksaan rubrik | **Satu-satunya** nama; dulu W1 memakai `needs` |
| `points` / `max_points` | Poin pemeriksaan / maksimum butir atau komponen | Bilangan bulat |
| `reachable_values` | Nilai poin yang dapat dicapai pemeriksaan berkredit parsial | Wajib untuk aturan per pasangan/per butir |
| `acceptance` | Status penerimaan terstruktur modul (TPL-01a) | Hanya di `module.yaml`; lihat TPL-01 |

Aturan angka (dokumentasi, bukan parser): spasi tepi dibuang; spasi di
dalam angka ditolak; bilangan bulat tanpa nol di depan atau berkelompok
titik tepat tiap 3 digit; tanpa tanda dan desimal; awalan/satuan hanya
yang diizinkan per isian. Contoh diterima/ditolak:
[`curriculum/mod-w01/project/rubric.yaml`](../curriculum/mod-w01/project/rubric.yaml)
`field_rules.number_fields`.

## 3b. Kriteria kualitas dokumentasi (wajib setiap modul; dari review W1)

| ID | Kriteria | Bukti yang diminta di `review.md` |
|---|---|---|
| QC-01 | Setiap maksimum yang dinyatakan **dapat dicapai**, bukan hanya jumlah field poin | Contoh jawaban yang mencapai maksimum untuk setiap pemeriksaan berkredit parsial dan setiap komponen |
| QC-02 | Setiap contoh skor cocok dengan aturan skor yang berlaku | Contoh dihitung ulang dari aturan |
| QC-03 | Setiap rumus konversi satuan benar ke dua arah | Contoh besar → kecil, kecil → besar, dan dua tingkat |
| QC-04 | Varian setara menilai konsep wajib yang setara | Matriks kesetaraan dengan bukti isi kedua varian |
| QC-05 | Model teknis yang disederhanakan diberi label | Daftar model sederhana vs kenyataan |
| QC-06 | Contoh pengajaran tidak memuat jawaban lengkap tugas bernilai | Tabel tumpang-tindih pelajaran/latihan/remedial vs butir bernilai |
| QC-07 | Instruksi pelajar dan metadata penilai sesuai | Perbandingan spec.md vs YAML |
| QC-08 | Aturan normalisasi dan ketergantungan deterministik | Contoh diterima/ditolak |
| QC-09 | Semua nama field mengikuti §3a | Pemeriksaan nama field |
| QC-10 | Fixture batas mencakup batas yang dapat dicapai (atau dinyatakan tidak dapat dicapai) | Contoh batas dari fixture nyata |
| QC-11 | Berkas V-L mematuhi kontrak visibilitas §1a (VC-1–VC-5) | Pemeriksaan setiap `spec.md` dan pelajaran terhadap kunci |
| QC-12 | Satuan desimal vs biner dinyatakan; desimal bawaan; konversi GB–GiB lewat byte | Pemeriksaan pelajaran, soal, lab |
| QC-13 | Cakupan D-39: setiap konsep wajib dijamin di setiap jalur penilaian yang sah; setiap varian menilai kompetensi inti slot secara setara. Bukti yang **cukup**: (a) satu lokasi wajib yang menilai konsep di semua varian yang dapat dipilih, atau proyek; **atau** (b) bukti deterministik setara yang mencakup setiap jalur pelajar sah menurut aturan pemilihan yang berlaku (mis. varian berkorelasi antarslot dalam satu komponen menurut VA-2). Jaminan D-39 dan aturan pemilihan tidak dilemahkan. Bukti **semantik** (lokasi benar-benar menilai konsep) adalah penilaian reviewer/penulis yang dicatat terpisah dari bukti **jalur** (matematis); kesetaraan varian (VA-1) dinilai terpisah dari cakupan modul | Baris matriks cakupan per konsep dan register kesetaraan per slot ([CURRICULUM_COVERAGE_MATRIX_W01_W08.md](CURRICULUM_COVERAGE_MATRIX_W01_W08.md)); uji negatif/positif metode; paket `docs/validation/` |

Kriteria ini adalah persyaratan kualitas dokumentasi, **bukan** izin
implementasi. TPL-19 (checklist penerimaan) mencakup CQ-01–CQ-20 **dan**
QC-01–QC-13.

## 4. Batas penilaian objektif (berlaku untuk semua modul)

| Bukti | Arti | Bukan bukti untuk |
|---|---|---|
| Jawaban/isian cocok dengan kunci atau aturan | Hasil yang diserahkan benar | Pemahaman penuh (dapat menebak) |
| Test kode lulus (W9+) | Perilaku program benar pada input yang diuji | Pemakaian konstruksi atau algoritma tertentu; kebenaran pada semua input |
| Skor ≥ 75 / modul `PASSED` | Memenuhi aturan penilaian aplikasi | Sertifikasi kompetensi independen (D-17, D-34) |

## 5. Bukti penerimaan CB-0

| ID | Kriteria | Bukti | Status |
|---|---|---|---|
| CB0-AC-01 | 20 templat wajib ada | §3 TPL-01–TPL-20 | Lulus |
| CB0-AC-02 | Setiap field dapat dilacak ke keputusan | Kolom/teks "Dasar" | Lulus |
| CB0-AC-03 | Konvensi penamaan dan field kanonik konsisten | §2, §3a; diterapkan di W1 (213 ID unik; `depends_on`, `normalization`, `accepted_sequences` seragam) | Lulus |
| CB0-AC-04 | Sumber, kunci, dan tampilan dipisahkan | §1 | Lulus |
| CB0-AC-05 | Semua field wajib terdefinisi oleh keputusan yang disetujui | TPL-10 `hidden_test_feedback` dan `case_description` ditetapkan D-36 | Lulus (dokumentasi) |
| CB0-AC-06 | Diterapkan pada satu modul lengkap | `curriculum/mod-w01/` | Diproduksi; W1 belum lolos review dan belum diterima |
| CB0-AC-07 | Tidak ada parser, skema database, atau kode aplikasi | Hanya Markdown/YAML konten | Lulus |
| CB0-AC-08 | Diterima owner | — | **Belum** |

Kesimpulan: kebijakan dan kelengkapan templat terpenuhi; CB-0 **belum** final secara global karena review independen (CB0-AC-06) dan penerimaan owner (CB0-AC-08) belum ada. Tambahan dari review PR #25:
TPL-07/TPL-08/TPL-13 kini mensyaratkan **posisi kunci seimbang** dengan
urutan opsi tetap (tanpa pengacakan); TPL-14 mensyaratkan **matriks
kesetaraan varian** (kompetensi, konsep wajib, tuntutan kognitif, format,
poin, waktu); TPL-11 mensyaratkan contoh untuk pelajar **tidak** memuat
jawaban tugas bernilai (contoh nyata hanya di berkas penilai).
