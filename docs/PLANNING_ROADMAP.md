# IT ZERO → HERO — Roadmap Perencanaan Tersisa (D-20–D-22)

Status: dokumentasi · **PLANNING CLEAR: NO** · **IMPLEMENTATION VERIFIED:
NO** · D-10: eksekusi prototipe **NOT AUTHORIZED** · D-11: implementasi
**DEFERRED** · PY:F-01–F-15: **NOT VERIFIED**. Tanggal: **2026-11-24**
(direvisi setelah review PR #23, F-01–F-06; diperbarui batch D-23–D-25).
Basis: `main` = `40ca205` (merge PR #24); diperbarui batch D-26–D-35. Klasifikasi jalur disetujui
owner (D-20, D-25).

Klasifikasi jalur memakai D-20 (P/M/G/V), D-21 (kurikulum wajib di P), dan
D-22 (tiga penundaan). AC asli tiap butir ada di
[BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) §3 dan
tidak dihapus atau dilemahkan. Kode rujukan dokumen ini: `RM:`.

## 1. Ringkasan

Dua ukuran berbeda, dilaporkan terpisah. Keduanya **jumlah butir**, bukan
beban kerja, dan **bukan** kesiapan aplikasi (belum ada aplikasi).

| Ukuran | Pembilang | Penyebut | Nilai |
|---|---|---|---|
| Kemajuan register (semua butir) | 32 COMPLETE | 56 butir | 57,1% |
| Kemajuan jalur P (perencanaan wajib) | 32 butir P COMPLETE | 43 butir P | 74,4% |

Beban kerja tidak setara antarbutir: UW-37 saja mencakup 64 komponen
kurikulum (4/64 diproduksi, 4/64 diterima owner melalui W01-ACC, §5).

| Status register (56 butir) | Jumlah |
|---|---|
| COMPLETE | 32 |
| OPEN | 4 |
| BLOCKED | 12 |
| DEFERRED (M, D-22) | 3 |
| NOT VERIFIED | 5 |

| Jalur | COMPLETE | Belum | Total |
|---|---|---|---|
| P — Perencanaan wajib | 32 | 11 | 43 |
| M — Ditunda ke milestone (D-22) | 0 | 3 | 3 |
| G — Gerbang owner setelah PLANNING CLEAR | 0 | 2 | 2 |
| V — Verifikasi setelah izin | 0 | 8 | 8 |
| **Total** | **32** | **24** | **56** |

Pemindahan UW-15 dari P ke V **disetujui D-25** (RM-Q1(a)); AC UW-15
tetap. Penyebut jalur P = 43 sudah final menurut klasifikasi yang disetujui.
Batch D-26–D-35 menyelesaikan UW-25, UW-27, UW-29, UW-30, UW-31, UW-32
(AC = keputusan tertulis terpenuhi). UW-36 kini COMPLETE (D-38, §12); UW-26
dan UW-37 tetap OPEN (konten 15 modul belum ada); UW-33 tetap BLOCKED.

## 2. Register lengkap dengan klasifikasi (56 butir)

Diperiksa otomatis 2026-11-24: 56 ID unik UW-01–UW-56, tanpa duplikat dan
tanpa ID hilang; jumlah per status dan per jalur sama dengan §1.

| ID | Status | Jalur | Alasan klasifikasi |
|---|---|---|---|
| UW-01 | COMPLETE | P | Keputusan owner D-01 |
| UW-02 | BLOCKED | G | Izin implementasi; gerbang setelah PLANNING CLEAR (D-11, D-20) |
| UW-03 | COMPLETE | P | Keputusan D-06 (AC: kombinasi tercatat). Verifikasi build ada di UW-13/UW-54 (V), tidak dihitung di sini |
| UW-04 | COMPLETE | P | Keputusan D-05 |
| UW-05 | COMPLETE | P | Keputusan D-02 |
| UW-06 | COMPLETE | P | Keputusan D-07; verifikasi perangkat di UW-55 (V) |
| UW-07 | COMPLETE | P | Keputusan D-08; isolasi jaringan diverifikasi di UW-12 (V) |
| UW-08 | COMPLETE | P | Keputusan D-09; verifikasi di UW-13 (V) |
| UW-09 | COMPLETE | P | Keputusan D-03 |
| UW-10 | BLOCKED | G | Izin eksekusi prototipe; gerbang setelah PLANNING CLEAR (D-10, D-20) |
| UW-11 | COMPLETE | P | Keputusan D-19 |
| UW-12 | OPEN | V | Eksekusi PY:F-01–F-15 setelah UW-10 (D-20); juga menghasilkan angka batas agregat lab LX-2 (D-38) |
| UW-13 | NOT VERIFIED | V | Build CI pertama; butuh UW-02 |
| UW-14 | BLOCKED | P | Verifikasi **sumber** dataset untuk klaim perencanaan (CAL:AC-02), bukan verifikasi aplikasi; butuh akses host |
| UW-15 | NOT VERIFIED | V (D-25) | Sisa AC "bukti" = pengukuran perangkat yang diizinkan terpisah (D-16 Q3; prasyarat UW-15, D-25). Sisa perencanaan di UW-33 (§3) |
| UW-16 | COMPLETE | P | Keputusan D-17 |
| UW-17 | COMPLETE | P | Keputusan D-14; AC dipenuhi dengan hitungan kontras terdokumentasi. Perilaku perangkat di UW-56 (V) |
| UW-18 | COMPLETE | P | Keputusan D-15; perilaku perangkat di UW-56 (V) |
| UW-19 | COMPLETE | P | Penyelarasan label dokumen |
| UW-20 | COMPLETE | P | Keputusan D-01 M-02 |
| UW-21 | DEFERRED | M | D-22; tidak memblokir penerimaan perencanaan W9–W12 (§5.2) |
| UW-22 | COMPLETE | P | Keputusan D-12; kasus batas dievaluasi dengan aritmetika terdokumentasi (NUM §10). Implementasi di UW-56 (V) |
| UW-23 | BLOCKED | P | Keputusan owner CO-1/CO-2 |
| UW-24 | BLOCKED | P | Keputusan owner O-09 (pilihan runner); menjalankan runner adalah V |
| UW-25 | COMPLETE | P | Keputusan D-34 (AC: keputusan tertulis) |
| UW-26 | OPEN | P | OP-4 diputuskan (D-23); bank concept W1–W4 diproduksi (48/192 soal; W1 diterima owner, W2–W4 belum direview/diterima), 12 modul belum |
| UW-27 | COMPLETE | P | D-26 (ASM:D-08 terisi) |
| UW-28 | BLOCKED | P | Keputusan OP-6 |
| UW-29 | COMPLETE | P | D-27 (ASM:L5 terisi) |
| UW-30 | COMPLETE | P | D-28 (ASM:X-07 terisi) |
| UW-31 | COMPLETE | P | D-27 (ASM:C6 terisi) |
| UW-32 | COMPLETE | P | D-27 (OP-10, OP-11 terisi) |
| UW-33 | BLOCKED | P | OD-15 diputuskan (D-29, D-37); OD-5–OD-9, OD-11–OD-14 belum |
| UW-34 | BLOCKED | P | Keputusan CO-4–CO-6 |
| UW-35 | BLOCKED | P | Keputusan UO-3–UO-9 |
| UW-36 | COMPLETE | P | Semua kebijakan CU diputuskan (D-13, D-24, D-30–D-36); angka batas agregat LX-2 = keluaran verifikasi UW-12 (D-38) |
| UW-37 | OPEN | P | Konten lengkap 64 komponen (D-21); diproduksi 16/64 (W1–W4); diterima owner 4/64 (W01-ACC); W2–W4 dikoreksi (F-28–F-72, dua putaran, PR #27), menunggu re-review independen dan penerimaan owner |
| UW-38 | DEFERRED | M | D-22 |
| UW-39 | BLOCKED | V | Lingkungan SDK opsional untuk verifikasi build; tidak punya AC perencanaan |
| UW-40 | DEFERRED | M | D-22 |
| UW-41 | BLOCKED | P | Daftar skill dari owner (PENDING SOURCE) |
| UW-42 | COMPLETE | P | Perapian dokumentasi |
| UW-43 | COMPLETE | P | Keputusan D-18 + pemeriksaan tautan dokumentasi |
| UW-44 | COMPLETE | P | Perapian ID dokumentasi |
| UW-45 | COMPLETE | P | Penyeragaman label dokumentasi |
| UW-46 | COMPLETE | P | Dokumentasi GitHub Bridge |
| UW-47 | COMPLETE | P | Rujukan DECISIONS_LOG |
| UW-48 | COMPLETE | P | Rujukan QUALITY_GATES |
| UW-49 | COMPLETE | P | Perapian blocker HANDOFF |
| UW-50 | COMPLETE | P | README |
| UW-51 | COMPLETE | P | Pemeriksaan label template Issue di repo (metadata repo, bukan verifikasi aplikasi) |
| UW-52 | OPEN | V | Cek ulang versi toolchain **tepat sebelum** scaffold; terikat UW-02 |
| UW-53 | BLOCKED | P | Membaca sumber resmi untuk klaim perencanaan; butuh akses host |
| UW-54 | NOT VERIFIED | V | Butir V toolchain lewat CI (UW-13) |
| UW-55 | NOT VERIFIED | V | Perilaku transfer perangkat; butuh UW-02 |
| UW-56 | NOT VERIFIED | V | Keputusan D-12–D-15 di aplikasi; butuh UW-02 |

Tidak ada butir COMPLETE yang selesai karena verifikasi teknis aplikasi:
setiap COMPLETE dipenuhi keputusan owner atau pekerjaan dokumentasi, dan
verifikasi aplikasinya dicatat terpisah di jalur V.

## 3. Pemisahan OD-1: perencanaan vs verifikasi (F-02)

| Kelompok | Isi | Butir | Jalur |
|---|---|---|---|
| Disetujui (D-16) | AES-256-GCM, nonce acak 96-bit, tag 128-bit, header = AAD, salt CSPRNG per ekspor; Argon2id via Bouncy Castle (bersyarat) + cadangan PBKDF2-HMAC-SHA256 ≥ 600.000; minimum Argon2id 19 MiB/t=2/p=1; envelope OD1 §5 sebagai baseline; H-1–H-7, KV-1–KV-8; restore produksi nonaktif sampai terverifikasi | — (keputusan) | — |
| Sisa perencanaan | OD-5 format payload; OD-6 aturan kata sandi; OD-7 **kebijakan** batas sumber daya (jenis batas, titik pemeriksaan sebelum alokasi/KDF, perilaku penolakan); OD-8 retensi snapshot + log restore (D-17); OD-9 attempt berjalan; **OD-11** serialisasi envelope (tata letak byte, encoding field, versi; OD-1-Q4 OPEN); **OD-12** kebijakan kapan KDF cadangan dipakai untuk ekspor baru (OD-1-Q6); **OD-13** rencana dan protokol pengukuran (perangkat, prosedur, kriteria terima) untuk diizinkan owner; **OD-14** review dokumen dependensi Bouncy Castle (lisensi, versi, ukuran, dependensi transitif) | UW-33 | P |
| Verifikasi teknis | Kompatibilitas Bouncy Castle di Android API 29+; pengukuran KDF di perangkat yang diizinkan; **nilai** parameter final dan batas maksimum (disetujui owner setelah pengukuran); CT-1–CT-12 dengan bukti EV | UW-15 | V |
| Usulan baru (butuh persetujuan, OD-15-Q1) | **OD-15** validasi ledger XP saat pratinjau restore dan perlakuan temuan ([XP_PROGRESS_DECISION_SHEET.md](XP_PROGRESS_DECISION_SHEET.md) §8.2); diusulkan dilacak di UW-33 | UW-33 | P |
| Syarat rilis restore produksi | RR-1–RR-8 di [OD1_BACKUP_CRYPTO_DECISION_SHEET.md](OD1_BACKUP_CRYPTO_DECISION_SHEET.md) §11 | UW-15 + UW-33 + UW-02 | — |

OD-11–OD-14 adalah ID baru (keluarga OD sebelumnya berakhir di OD-10).
AC UW-33 diperluas, tidak diganti: "OD-5–OD-9 terisi" **dan** "OD-11–OD-14
terisi". AC UW-15 tetap "Parameter tertulis + bukti". **Disetujui D-25**
(RM-Q1(a), (b), (d)); tidak ada persyaratan keamanan yang dihapus.

## 4. Keputusan perencanaan yang masih dibutuhkan (jalur P, butuh owner)

| UW | Status | Keputusan terkait | Deliverable | AC (§3 audit) | Aksi berikutnya |
|---|---|---|---|---|---|
| UW-23 | BLOCKED | CO-1, CO-2 | Rentang tahun + mekanisme pembaruan dataset hari libur | Keputusan tertulis | Claude siapkan lembar |
| UW-24 | BLOCKED | O-09 | Pilihan runner emulator/perangkat | Runner tersedia (keputusan + rencana) | Claude siapkan lembar |
| UW-28 | BLOCKED | OP-6 | Kebijakan manipulasi jam, toleransi NTP | ASM:E-01–E-04 punya kebijakan | Claude siapkan lembar |
| UW-33 | BLOCKED | OD-5–OD-9, OD-11–OD-14, OD-15-Q2 | §3 | Semua OD terkait terisi | Owner menjawab OD-15-Q2; Claude siapkan lembar OD-5–OD-9, OD-11–OD-14 |
| UW-34 | BLOCKED | CO-4–CO-6 | Kalender perusahaan, label era, notifikasi jam tenang | CO-4–CO-6 terisi | Claude siapkan lembar |
| UW-35 | BLOCKED | UO-3–UO-9 | Tipografi, aset, breakpoint, tab bar, performa, field layar | UO-3–UO-9 terisi | Claude siapkan lembar |
| UW-41 | BLOCKED | — | Daftar delapan skill tambahan (PENDING SOURCE) | FIN:SE-1–SE-6 | Owner menyerahkan daftar |

Konten (bukan keputusan): UW-26 dan UW-37 — produksi W2–W16 dan penerimaan
owner (§5). Akses sumber: UW-14 (`www8.cao.go.jp`) dan UW-53 (RFC, NIST, W3C,
M3, CAO, e-Gov).

## 5. Kurikulum (UW-37, jalur P) — tanpa ketergantungan melingkar (F-01)

### 5.1 Masalah yang diperbaiki

Versi sebelumnya menyatakan konten W9–W12 baru "diterima final" setelah
hasil uji runtime (UW-21). Itu melingkar: D-21 mewajibkan kurikulum lengkap
**sebelum** PLANNING CLEAR, sedangkan D-10, D-11, dan D-20 melarang
eksekusi prototipe **sebelum** PLANNING CLEAR dan izin terpisah. Versi itu
dicabut.

### 5.2 Aturan yang berlaku (diturunkan dari D-10, D-11, D-20, D-21, D-22)

| ID | Aturan |
|---|---|
| RM:RV-1 | Konten Python W9–W12 (dan bagian Python capstone W16) **dapat diterima sebagai perencanaan** sebelum runtime dieksekusi. Penerimaan perencanaan = konten lengkap terdokumentasi dan lolos CPP:CA-01–CA-11 |
| RM:RV-2 | Wajib terdokumentasi lengkap: materi pelajaran, latihan, rubrik, fixture, dan rencana test case (input, keluaran yang diharapkan, poin, timeout). D-21 tidak dikurangi |
| RM:RV-3 | Eksekusi runtime tetap **NOT VERIFIED**; penerimaan perencanaan tidak menyatakan test pernah dijalankan |
| RM:RV-4 | UW-21 (DEFERRED, D-22) **tidak** memblokir penerimaan perencanaan W9–W12 dan tidak memblokir PLANNING CLEAR |
| RM:RV-5 | Bila kelayakan runtime gagal setelah izin (UW-10 → UW-12): implementasi yang terdampak dihentikan; kurikulum **tidak** diubah tanpa keputusan eksplisit owner (UW-21/CU-8) |
| RM:RV-6 | Setelah perubahan yang disetujui: konten kurikulum terdampak dan persyaratan implementasi terdampak divalidasi ulang (CPP:CA-01–CA-11, AC butir terkait) dan status penerimaannya dicatat ulang |

### 5.3 Ketergantungan produksi konten (F-06)

| Ketergantungan | Butir | Status | Lembar | Kolom/batch terdampak |
|---|---|---|---|---|
| Format soal, poin, durasi ujian (OP-5) | UW-27 | **D-26** | [ASSESSMENT_FLOW_DECISION_SHEETS.md](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A | Theory |
| Aturan kredit penjelasan konsep (OP-4) | UW-26 | **D-23** | [OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md](OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md) | Concept |
| Penilaian lab (CU-6) | UW-36 | **D-24, D-35, D-36** | [CU6_LAB_SCORING_DECISION_SHEET.md](CU6_LAB_SCORING_DECISION_SHEET.md) | Laboratory |
| Varian remedial (CU-5) | UW-36 | **D-30** | [CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md) §B | Semua komponen |
| Rubrik mini-project (CU2-O4) | UW-36 (D-25) | **D-33** | [PROJECT_RUBRIC_DECISION_SHEETS.md](PROJECT_RUBRIC_DECISION_SHEETS.md) §A | Mini-project W1–W15 |
| Rubrik capstone (CU-9) | UW-36 | **D-33** | idem §B | W16 Mini-project |
| Format konten (CU-3) | UW-36 | **D-30** | CCD §A | CB-0 |
| Lab SQL/HTML/Git (CU-7) | UW-36 | **D-31** | CCD §C | W13–W15 |
| Pembagian W9/W10 (CU-11) | UW-36 | **D-32** | CCD §E | CB-3 |
| Alokasi jam (CU2-O3) | UW-36 (D-25) | **D-32** | CCD §D | Semua modul |
| Pengumpulan/interupsi (OP-7) | UW-29 | **D-27** | AF §B | Laboratory, Mini-project |
| Identitas XP (OP-8, CU-4) | UW-30 | **D-28** | [XP_PROGRESS_DECISION_SHEET.md](XP_PROGRESS_DECISION_SHEET.md) | `activity_id` semua komponen |
| Unlock rinci (OP-9) | UW-31 | **D-27** | AF §C | Prasyarat |
| Remedial dan autosave (OP-10, OP-11) | UW-32 | **D-27** | AF §D | Materi remedial |
| Risiko kunci jawaban (CU-10) | UW-25 | **D-34** | [CU10_ANSWER_KEY_RISK_DECISION_SHEET.md](CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) | Desain bank soal |
| Asumsi struktur: 6 soal concept, 3 aktivitas lab per modul (CU2-O5) | UW-36 (usulan) | **D-30** | CCD §B | Beban konten, durasi C dan L |
| Persistensi ujian di sekitar tenggat (OP-5-Q8) | UW-27 | **D-26** | AF §A.5b | Theory |

Konsistensi terhadap D-01–D-35: [CROSS_SPEC_CONSISTENCY_REVIEW.md](CROSS_SPEC_CONSISTENCY_REVIEW.md).
Standar produksi CB-0 (kebijakan lengkap setelah D-36; menunggu review independen dan penerimaan owner): [CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md).

Templat dan rencana produksi ([CURRICULUM_PRODUCTION_PLAN.md](CURRICULUM_PRODUCTION_PLAN.md))
**bukan** konten; matriks 64 komponen tetap 0/64.

## 6. Penundaan milestone yang disetujui (jalur M, D-22)

| UW | Status | Milestone | Prasyarat | Verifikasi | Penanganan kegagalan | AC (tetap) |
|---|---|---|---|---|---|---|
| UW-21 | DEFERRED | Hasil uji kelayakan Python (setelah UW-10, UW-12) | PY:F-01–F-15 dijalankan | Hasil F-01–F-15 dengan bukti EV | RM:RV-5 dan RM:RV-6. **Tidak** memblokir penerimaan perencanaan W9–W12 (RM:RV-4) | Keputusan tertulis |
| UW-38 | DEFERRED | Milestone rilis | Implementasi diizinkan; build CI ada | AP-3–AP-5 | Rilis tidak dilakukan sampai keputusan signing/R8/distribusi ada | AP-3–AP-5 |
| UW-40 | DEFERRED | Milestone UI pertama | Implementasi diizinkan | Keputusan mekanisme effect + uji UI | Pola StateFlow yang sudah disetujui (TD:20) sampai diputuskan | Keputusan tertulis |

## 7. Gerbang otorisasi owner (jalur G — setelah PLANNING CLEAR)

| UW | Status | Gerbang | Prasyarat | Catatan |
|---|---|---|---|---|
| UW-10 | BLOCKED | Izin eksekusi prototipe Python | PLANNING CLEAR: YES | Rencana dan ambang disetujui (D-10); eksekusi butuh izin baru |
| UW-02 | BLOCKED | Izin implementasi | PLANNING CLEAR: YES | D-11; PLANNING CLEAR tidak mengizinkan implementasi (D-20) |

Izin pengukuran kripto (D-16 Q3) adalah izin terpisah, dicatat sebagai
prasyarat UW-15, bukan butir baru (D-25). Belum diberikan.

## 8. Verifikasi teknis setelah izin (jalur V)

| UW | Status | Verifikasi | Membutuhkan | AC |
|---|---|---|---|---|
| UW-12 | OPEN (NOT STARTED) | PY:F-01–F-15; angka LX-2 (D-38) | UW-10 | F-01–F-15 PASS dengan bukti EV; angka batas agregat LX-2 tercatat dari pengukuran |
| UW-13 | NOT VERIFIED | Build CI toolchain | UW-02 | Checklist TC §7 |
| UW-15 | NOT VERIFIED | Kompatibilitas BC, pengukuran KDF, nilai parameter final dan batas maksimum, CT-1–CT-12 (NOT VERIFIED) | Izin pengukuran terpisah (prasyarat, D-25); OD-13 | Parameter tertulis + bukti |
| UW-39 | BLOCKED | Android SDK di cloud (opsional) | Pengaturan jaringan | Opsional |
| UW-52 | OPEN (NOT STARTED) | Cek ulang versi toolchain tepat sebelum scaffold | UW-02 | Sumber resmi bertanggal baru |
| UW-54 | NOT VERIFIED | Butir V toolchain | UW-13 | Log CI |
| UW-55 | NOT VERIFIED | Transfer antarperangkat dengan `allowBackup=false` | UW-02 | Bukti EV per jalur |
| UW-56 | NOT VERIFIED | Keputusan D-12–D-15 di aplikasi (NUM:NA-1–NA-6, ACC:AT-1–AT-6) | UW-02 | Bukti EV |

## 9. Jalur kritis menuju PLANNING CLEAR

```
CB-0: kebijakan terputuskan (D-36); review independen dan penerimaan owner belum
        │
        ▼
W1 PRODUCED (direvisi PR #25) ──► review ulang ChatGPT ──► penerimaan owner (modul acuan)
        │
        ▼
W2 → W3 → W4 (CB-1b, satu PR per modul) → W5–W8 (CB-2)
        │
        ▼
W9–W12 (CB-3, runtime NOT VERIFIED) → W13–W16 (CB-4, capstone)
        │
        ▼
CB-R  Penerimaan owner 64 komponen (UW-37) + bank concept 16 modul (UW-26)
        │
        ▼
PLANNING CLEAR (bersama butir P lain)

Paralel (wajib untuk PLANNING CLEAR, tidak memblokir produksi konten):
UW-23, UW-24, UW-28, UW-33, UW-34, UW-35, UW-41, UW-14 + UW-53 (akses sumber)
```

Tidak ada butir M, G, atau V di jalur kritis PLANNING CLEAR.

## 10. Batch berikutnya yang direkomendasikan

1. Review PR batch ini; owner menerima (atau meminta revisi) W1 sebagai
   modul acuan dan CB-0.
2. Produksi W2 (OS & file) sebagai satu PR, mengikuti rencana CB-1b di
   [CURRICULUM_PRODUCTION_PLAN.md](CURRICULUM_PRODUCTION_PLAN.md) §6.1; lalu
   W3, W4.
3. Paralel (kecil): owner menjawab CU-6-Q13 dan OD-15-Q2; Claude
   menyiapkan lembar UW-28 (OP-6) dan UW-33 (OD-5–OD-9, OD-11–OD-14).

## 11. Pertanyaan owner dari roadmap

~~RM-Q1~~ — *dijawab D-25 (2026-11-24)*: (a) UW-15 di jalur V dengan AC
tetap; (b) OD-11–OD-14 di UW-33 bersama OD-5–OD-9; (c) CU2-O3 dan CU2-O4
di UW-36; (d) izin pengukuran kripto = prasyarat UW-15.

**RM-Q2 (dijawab D-38: Ya):** nilai angka batas agregat lab (LX-2, D-35)
hanya dapat ditetapkan dari pengukuran yang diizinkan. Setujui pencatatannya
sebagai keluaran verifikasi UW-12 (jalur V), sehingga UW-36 (kebijakan CU)
dapat dinilai lengkap? Rekomendasi: Ya.

## 12. Pembaruan D-38, W01-ACC, CB-0.5 (2026-11-24)

- UW-36 → **COMPLETE** (AC "CU-2, CU-3, CU-5–CU-7, CU-9, CU-11 terisi" terpenuhi;
  angka LX-2 dipindah ke UW-12 oleh D-38). Tidak ada pengukuran yang dilakukan.
- Register: COMPLETE 32 · OPEN 4 · BLOCKED 12 · DEFERRED 3 · NOT VERIFIED 5 = 56;
  jalur P 32/43.
- W01-ACC diterima; UW-26/UW-37 tetap OPEN (W2–W16 belum diproduksi).
- CB-0.5 (alur kerja agen) **tidak** dihitung di register UW; lihat
  [AGENT_SKILL_REGISTRY.md](AGENT_SKILL_REGISTRY.md).

## 13. Pembaruan CB-1 — produksi W2–W4 (2026-11-24)

- PR #26 di-merge (`ab0103e`); owner menerima CB-0.5; V03 PASS di sesi baru
  ([CB05_VALIDATION_REPORT.md](CB05_VALIDATION_REPORT.md) §4).
- W2, W3, W4 **diproduksi** (12 komponen; `curriculum/mod-w02/`–`mod-w04/`),
  review mandiri penyusun; **belum** direview ChatGPT dan **belum** diterima
  owner. Produksi kurikulum 16/64 komponen; diterima owner tetap 4/64.
- UW-26 dan UW-37 tetap **OPEN** (AC menuntut konten lengkap 16 modul dan
  penerimaan); jumlah register tidak berubah: COMPLETE 32 · OPEN 4 ·
  BLOCKED 12 · DEFERRED 3 · NOT VERIFIED 5 = 56; jalur P 32/43.

## 14. Koreksi konsolidasi CB-1 (PR #27, 2026-11-24)

- Review PR #27 = REQUEST CHANGES (F-28–F-70); koreksi diterapkan pada PR
  yang sama. Disposisi per temuan di `curriculum/mod-w0N/review.md`.
- F-55, F-56, F-57, F-59: **BLOCKED** — rincian temuan asli tidak tersedia.
- W2–W4: diproduksi dan dikoreksi; menunggu re-review independen dan
  penerimaan owner. W5–W16: NOT STARTED / NOT AUTHORIZED.
- Register tidak berubah (32/4/12/3/5 = 56; P 32/43); UW-26, UW-37 OPEN.
  PLANNING CLEAR: NO · IMPLEMENTATION VERIFIED: NO · D-10 NOT AUTHORIZED ·
  D-11 DEFERRED.

## 15. Koreksi terarah putaran 2 (PR #27, 2026-11-24)

- Delta review PR #27 = REQUEST CHANGES; register diperluas menjadi F-28–F-72
  (45 ID). Deskripsi F-55, F-56, F-57, F-59 dipulihkan owner dan ditangani;
  catatan BLOCKED di §14 kini historis.
- F-51 (satuan bit/byte peka huruf, W3), F-71 (W2) dan F-72 (W4)
  (dependensi rubrik eksplisit) diperbaiki; fixture W4 E19–E20 ditambahkan.
- Status tidak berubah: W2–W4 menunggu re-review independen dan penerimaan
  owner; W5–W16 NOT STARTED / NOT AUTHORIZED; register 32/4/12/3/5 = 56;
  P 32/43; PLANNING CLEAR NO; IMPLEMENTATION VERIFIED NO.
