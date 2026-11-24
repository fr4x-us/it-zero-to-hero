# IT ZERO → HERO — Roadmap Perencanaan Tersisa (D-20–D-22)

Status: dokumentasi · **PLANNING CLEAR: NO** · **IMPLEMENTATION VERIFIED:
NO** · D-10: eksekusi prototipe **NOT AUTHORIZED** · D-11: implementasi
**DEFERRED** · PY:F-01–F-15: **NOT VERIFIED**. Tanggal: **2026-11-24**
(direvisi setelah review PR #23, F-01–F-06). Basis: `main` = `bcecdae`
(merge PR #22). Status berlaku saat PR pencatatan D-16–D-22 di-merge.

Klasifikasi jalur memakai D-20 (P/M/G/V), D-21 (kurikulum wajib di P), dan
D-22 (tiga penundaan). AC asli tiap butir ada di
[BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) §3 dan
tidak dihapus atau dilemahkan. Kode rujukan dokumen ini: `RM:`.

## 1. Ringkasan

Dua ukuran berbeda, dilaporkan terpisah. Keduanya **jumlah butir**, bukan
beban kerja, dan **bukan** kesiapan aplikasi (belum ada aplikasi).

| Ukuran | Pembilang | Penyebut | Nilai |
|---|---|---|---|
| Kemajuan register (semua butir) | 25 COMPLETE | 56 butir | 44,6% |
| Kemajuan jalur P (perencanaan wajib) | 25 butir P COMPLETE | 43 butir P | 58,1% |

Beban kerja tidak setara antarbutir: UW-37 saja mencakup 64 komponen
kurikulum (0/64 selesai, §5).

| Status register (56 butir) | Jumlah |
|---|---|
| COMPLETE | 25 |
| OPEN | 4 |
| BLOCKED | 19 |
| DEFERRED (M, D-22) | 3 |
| NOT VERIFIED | 5 |

| Jalur | COMPLETE | Belum | Total |
|---|---|---|---|
| P — Perencanaan wajib | 25 | 18 | 43 |
| M — Ditunda ke milestone (D-22) | 0 | 3 | 3 |
| G — Gerbang owner setelah PLANNING CLEAR | 0 | 2 | 2 |
| V — Verifikasi setelah izin | 0 | 8 | 8 |
| **Total** | **25** | **31** | **56** |

Pemindahan jalur yang perlu konfirmasi owner (RM-Q1): UW-15 dari P ke V
(§3). Bila owner menolak, UW-15 tetap di P dan kemajuan jalur P menjadi
**25/44 (56,8%)**; jalur V menjadi 7. Tidak ada pemindahan lain.

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
| UW-12 | OPEN | V | Eksekusi PY:F-01–F-15 setelah UW-10 (D-20) |
| UW-13 | NOT VERIFIED | V | Build CI pertama; butuh UW-02 |
| UW-14 | BLOCKED | P | Verifikasi **sumber** dataset untuk klaim perencanaan (CAL:AC-02), bukan verifikasi aplikasi; butuh akses host |
| UW-15 | NOT VERIFIED | V (usulan, RM-Q1) | Sisa AC "bukti" = pengukuran perangkat yang diizinkan terpisah (D-16 Q3). Sisa perencanaan dipindah eksplisit ke UW-33 (§3) |
| UW-16 | COMPLETE | P | Keputusan D-17 |
| UW-17 | COMPLETE | P | Keputusan D-14; AC dipenuhi dengan hitungan kontras terdokumentasi. Perilaku perangkat di UW-56 (V) |
| UW-18 | COMPLETE | P | Keputusan D-15; perilaku perangkat di UW-56 (V) |
| UW-19 | COMPLETE | P | Penyelarasan label dokumen |
| UW-20 | COMPLETE | P | Keputusan D-01 M-02 |
| UW-21 | DEFERRED | M | D-22; tidak memblokir penerimaan perencanaan W9–W12 (§5.2) |
| UW-22 | COMPLETE | P | Keputusan D-12; kasus batas dievaluasi dengan aritmetika terdokumentasi (NUM §10). Implementasi di UW-56 (V) |
| UW-23 | BLOCKED | P | Keputusan owner CO-1/CO-2 |
| UW-24 | BLOCKED | P | Keputusan owner O-09 (pilihan runner); menjalankan runner adalah V |
| UW-25 | BLOCKED | P | Keputusan owner CU-10 |
| UW-26 | OPEN | P | Keputusan OP-4 + bank tugas (D-21) |
| UW-27 | BLOCKED | P | Keputusan OP-5 |
| UW-28 | BLOCKED | P | Keputusan OP-6 |
| UW-29 | BLOCKED | P | Keputusan OP-7 |
| UW-30 | BLOCKED | P | Keputusan OP-8, CU-4 |
| UW-31 | BLOCKED | P | Keputusan OP-9 |
| UW-32 | BLOCKED | P | Keputusan OP-10, OP-11 |
| UW-33 | BLOCKED | P | Keputusan OD-5–OD-9 + sisa perencanaan OD-1 (OD-11–OD-14, §3) |
| UW-34 | BLOCKED | P | Keputusan CO-4–CO-6 |
| UW-35 | BLOCKED | P | Keputusan UO-3–UO-9 |
| UW-36 | BLOCKED | P | Keputusan CU-3, CU-5, CU-6, CU-7, CU-9, CU-11 (+ CU2-O3, CU2-O4 dilacak, §5.3) |
| UW-37 | OPEN | P | Konten lengkap 64 komponen (D-21) |
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
| Syarat rilis restore produksi | RR-1–RR-8 di [OD1_BACKUP_CRYPTO_DECISION_SHEET.md](OD1_BACKUP_CRYPTO_DECISION_SHEET.md) §11 | UW-15 + UW-33 + UW-02 | — |

OD-11–OD-14 adalah ID baru (keluarga OD sebelumnya berakhir di OD-10).
AC UW-33 diperluas, tidak diganti: "OD-5–OD-9 terisi" **dan** "OD-11–OD-14
terisi". AC UW-15 tetap "Parameter tertulis + bukti". Perluasan dan
pemindahan ini menunggu konfirmasi owner (RM-Q1); selama itu sisa
perencanaan tetap dilacak di UW-33 (P), tidak ditunda diam-diam.

## 4. Keputusan perencanaan yang masih dibutuhkan (jalur P, butuh owner)

| UW | Status | Keputusan terkait | Ketergantungan | Deliverable | AC (§3 audit) | Bukti selesai | Aksi berikutnya |
|---|---|---|---|---|---|---|---|
| UW-23 | BLOCKED | CO-1, CO-2 | UW-14 | Rentang tahun + mekanisme pembaruan dataset hari libur | Keputusan tertulis | Keputusan di checklist + DECISIONS_LOG | Claude siapkan lembar keputusan |
| UW-24 | BLOCKED | O-09 | — | Pilihan runner emulator/perangkat | Runner tersedia (keputusan + rencana; menjalankan = V) | Keputusan + rencana runner | Claude siapkan lembar opsi |
| UW-25 | BLOCKED | CU-10 | — | Penerimaan risiko kunci jawaban dapat diekstrak | Keputusan tertulis | Keputusan | Claude siapkan lembar (selaras D-17) |
| UW-26 | OPEN | OP-4 | — | Rubrik + bank tugas penjelasan konsep | CUR:CC-08 | Keputusan OP-4 + bank tugas 16 modul | Owner menjawab OP-4-Q1–Q5 |
| UW-27 | BLOCKED | OP-5 | — | Rumus durasi ujian, format soal | ASM:D-08 terisi | Keputusan | Claude siapkan lembar keputusan |
| UW-28 | BLOCKED | OP-6 | — | Kebijakan manipulasi jam, toleransi NTP | ASM:E-01–E-04 punya kebijakan | Keputusan | Claude siapkan lembar keputusan |
| UW-29 | BLOCKED | OP-7 | CU-6 (RA-1/RA-2) | Aturan pengumpulan/interupsi lab-proyek | ASM:L5 terisi | Keputusan | Bersama/sesudah CU-6 |
| UW-30 | BLOCKED | OP-8, CU-4 | — | Identitas XP, rumus, level, streak, revisi konten | ASM:X-07 terisi | Keputusan | Claude siapkan lembar keputusan |
| UW-31 | BLOCKED | OP-9 | D-01 M-04 | Aturan unlock rinci | ASM:C6 terisi | Keputusan | Claude siapkan lembar keputusan |
| UW-32 | BLOCKED | OP-10, OP-11 | — | Komponen yang boleh diulang; debounce autosave | OP-10, OP-11 terisi | Keputusan | Claude siapkan lembar keputusan |
| UW-33 | BLOCKED | OD-5–OD-9, OD-11–OD-14 | D-16, D-17 | §3 | OD-5–OD-9 dan OD-11–OD-14 terisi | Keputusan + dokumen review | Claude siapkan lembar keputusan |
| UW-34 | BLOCKED | CO-4–CO-6 | — | Kalender perusahaan, label era, notifikasi jam tenang | CO-4–CO-6 terisi | Keputusan | Claude siapkan lembar keputusan |
| UW-35 | BLOCKED | UO-3–UO-9 | D-14, D-15 | Tipografi, aset, breakpoint, tab bar, performa, field layar | UO-3–UO-9 terisi | Keputusan | Claude siapkan lembar keputusan |
| UW-36 | BLOCKED | CU-3, CU-5, CU-6, CU-7, CU-9, CU-11 (+ CU2-O3, CU2-O4) | OP-4 | Format konten, varian, penilaian lab, bentuk lab SQL/HTML/Git, rubrik capstone, pembagian W9/W10, alokasi jam, rubrik mini-project | CU terkait terisi | Keputusan | Owner menjawab CU-6-Q1–Q6; Claude siapkan lembar lain |
| UW-41 | BLOCKED | — | — | Daftar delapan skill tambahan (PENDING SOURCE) | FIN:SE-1–SE-6 | Daftar dari owner | Owner menyerahkan daftar |

Butir akses sumber (P): UW-14 (dataset `syukujitsu.csv`, host
`www8.cao.go.jp`) dan UW-53 (RFC, NIST, W3C, M3, CAO, e-Gov) — butuh owner
membuka host atau menyediakan salinan.

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

| Ketergantungan | Butir | Kolom/batch yang terdampak |
|---|---|---|
| Format soal dan durasi ujian (OP-5) | UW-27 | Theory, semua modul |
| Aturan kredit penjelasan konsep (OP-4) | UW-26 | Concept, semua modul |
| Penilaian lab (CU-6) | UW-36 | Laboratory, semua modul |
| Jumlah minimum varian remedial (CU-5) | UW-36 | Semua komponen (materi remedial) |
| Rubrik mini-project (CU2-O4) | UW-36 (dilacak, RM-Q1) | Mini-project W1–W15 |
| Rubrik capstone (CU-9) | UW-36 | W16 Mini-project |
| Format konten/markup/diagram (CU-3) | UW-36 | CB-0 |
| Bentuk lab SQL/HTML/Git (CU-7) | UW-36 | Laboratory W13–W15 |
| Pembagian W9/W10 (CU-11) | UW-36 | CB-3 |
| Alokasi jam per komponen (CU2-O3) | UW-36 (dilacak, RM-Q1) | Semua modul (CPP §5, PROPOSED) |
| Aturan pengumpulan/interupsi (OP-7) | UW-29 | Laboratory, Mini-project |
| Identitas XP (OP-8) | UW-30 | Penandaan aktivitas di semua komponen |
| Komponen yang boleh diulang (OP-10) | UW-32 | Materi remedial |
| Aturan unlock rinci (OP-9) | UW-31 | Prasyarat modul |
| Risiko kunci jawaban diekstrak (CU-10) | UW-25 | Desain bank soal |

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

Izin pengukuran kripto (D-16 Q3) juga izin terpisah; diusulkan dicatat
sebagai prasyarat UW-15, bukan butir baru (RM-Q1).

## 8. Verifikasi teknis setelah izin (jalur V)

| UW | Status | Verifikasi | Membutuhkan | AC |
|---|---|---|---|---|
| UW-12 | OPEN (NOT STARTED) | PY:F-01–F-15 | UW-10 | F-01–F-15 PASS dengan bukti EV |
| UW-13 | NOT VERIFIED | Build CI toolchain | UW-02 | Checklist TC §7 |
| UW-15 | NOT VERIFIED | Kompatibilitas BC, pengukuran KDF, nilai parameter final dan batas maksimum, CT-1–CT-12 | Izin pengukuran terpisah; OD-13 | Parameter tertulis + bukti |
| UW-39 | BLOCKED | Android SDK di cloud (opsional) | Pengaturan jaringan | Opsional |
| UW-52 | OPEN (NOT STARTED) | Cek ulang versi toolchain tepat sebelum scaffold | UW-02 | Sumber resmi bertanggal baru |
| UW-54 | NOT VERIFIED | Butir V toolchain | UW-13 | Log CI |
| UW-55 | NOT VERIFIED | Transfer antarperangkat dengan `allowBackup=false` | UW-02 | Bukti EV per jalur |
| UW-56 | NOT VERIFIED | Keputusan D-12–D-15 di aplikasi (NUM:NA-1–NA-6, ACC:AT-1–AT-6) | UW-02 | Bukti EV |

## 9. Jalur kritis menuju PLANNING CLEAR

```
Keputusan owner: OP-4 (UW-26), CU-6/CU-3/CU-5/CU-7/CU-9/CU-11/CU2-O3/CU2-O4 (UW-36),
                 OP-5 (UW-27), OP-7 (UW-29), OP-8 (UW-30), OP-9 (UW-31), OP-10 (UW-32), CU-10 (UW-25)
        │
        ▼
CB-0  Templat konten final (CPP §6)
        │
        ▼
CB-1 → CB-2 → CB-3 → CB-4   Produksi 64 komponen (UW-37); CB-3 = W9–W12, diterima
        │                    sebagai perencanaan (RM:RV-1–RV-3), runtime NOT VERIFIED
        ▼
CB-R  Review + penerimaan owner seluruh konten
        │
        ▼
PLANNING CLEAR (bersama butir P lain yang paralel)

Paralel (wajib untuk PLANNING CLEAR, tidak memblokir produksi konten):
UW-23, UW-24, UW-28, UW-33, UW-34, UW-35, UW-41, UW-14 + UW-53 (akses sumber)
```

Tidak ada butir M, G, atau V di jalur kritis PLANNING CLEAR.

## 10. Batch perencanaan berikutnya yang direkomendasikan

1. Owner menjawab OP-4-Q1–Q5, CU-6-Q1–Q6, dan RM-Q1.
2. Claude menyiapkan satu batch lembar keputusan untuk UW-27 (OP-5),
   CU-9, CU2-O4, CU2-O3, CU-3, CU-5, CU-7, CU-11, dan OP-7/OP-8/OP-10
   (UW-29, UW-30, UW-32).
3. Setelah itu: CB-0 (templat final), lalu CB-1.

## 11. Pertanyaan owner dari roadmap

**RM-Q1:** Setujui (a) pemindahan UW-15 dari P ke V dengan AC tetap; (b)
perluasan pelacakan UW-33 dengan OD-11–OD-14 (AC OD-5–OD-9 tetap); (c)
pelacakan CU2-O3 dan CU2-O4 di bawah UW-36; (d) izin pengukuran kripto
dicatat sebagai prasyarat UW-15, bukan butir baru? Bila (a) ditolak, UW-15
tetap di P (kemajuan P 25/44).

Status: **AWAITING OWNER**.
