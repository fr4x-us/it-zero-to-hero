# IT ZERO → HERO — Roadmap Perencanaan Tersisa (D-20–D-22)

Status: dokumentasi · **PLANNING CLEAR: NO** · **IMPLEMENTATION VERIFIED:
NO** · D-10: eksekusi prototipe **NOT AUTHORIZED** · D-11: implementasi
**DEFERRED** · PY:F-01–F-15: **NOT VERIFIED**. Tanggal: **2026-11-24**.
Basis: `main` = `bcecdae` (merge PR #22). Status berlaku saat PR pencatatan
D-16–D-22 di-merge.

Klasifikasi jalur memakai D-20 (P/M/G/V), D-21 (kurikulum wajib di P), dan
D-22 (tiga penundaan). AC asli tiap butir ada di
[BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) §3 dan
tidak diubah.

## 1. Ringkasan

| Status register (56 butir) | Jumlah |
|---|---|
| COMPLETE | 25 |
| OPEN | 4 |
| BLOCKED | 19 |
| DEFERRED (M, D-22) | 3 |
| NOT VERIFIED | 5 |

| Jalur | Selesai | Belum | Total | Catatan |
|---|---|---|---|---|
| **P — Perencanaan wajib** | 25 | 18 | 43 | Kemajuan jalur P = **25/43 butir (58%) dihitung per butir**, bukan per beban kerja: UW-37 sendiri mencakup 64 komponen penilaian (0/64 selesai) |
| M — Ditunda ke milestone | 0 | 3 | 3 | Bukan penyelesaian |
| G — Gerbang owner | 0 | 2 | 2 | Setelah PLANNING CLEAR |
| V — Verifikasi setelah izin | 0 | 8 | 8 | Untuk IMPLEMENTATION VERIFIED |

Persentase register gabungan **bukan** ukuran kesiapan aplikasi; belum ada
aplikasi.

Perubahan jalur yang perlu dicatat: UW-15 sebelumnya di jalur P; setelah
D-16, keputusan kripto selesai dan yang tersisa hanya **pengukuran perangkat
yang diizinkan terpisah** (eksplisit di D-16 Q3), sehingga UW-15 kini
NOT VERIFIED di jalur V. Tidak ada butir P lain yang dipindah.

## 2. Keputusan perencanaan yang masih dibutuhkan (jalur P, butuh owner)

| UW | Status | Keputusan terkait | Ketergantungan | Deliverable | AC (§3 audit) | Bukti selesai | Aksi berikutnya | Butuh owner |
|---|---|---|---|---|---|---|---|---|
| UW-23 | BLOCKED | CO-1, CO-2 | UW-14 | Rentang tahun + mekanisme pembaruan dataset hari libur | Keputusan tertulis | Keputusan di checklist + DECISIONS_LOG | Claude siapkan lembar keputusan | Ya |
| UW-24 | BLOCKED | O-09 | — | Pilihan runner emulator/perangkat | Runner tersedia | Keputusan + rencana runner | Claude siapkan lembar opsi | Ya |
| UW-25 | BLOCKED | CU-10 | — | Penerimaan risiko kunci jawaban dapat diekstrak | Keputusan tertulis | Keputusan | Claude siapkan lembar keputusan (selaras D-17) | Ya |
| UW-26 | OPEN | OP-4 | — | Rubrik + bank tugas penjelasan konsep | CUR:CC-08 | Keputusan OP-4 + bank tugas 16 modul | Owner menjawab OP-4-Q1–Q4 | Ya (OP-4) |
| UW-27 | BLOCKED | OP-5 | — | Rumus durasi ujian, format soal | ASM:D-08 terisi | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-28 | BLOCKED | OP-6 | — | Kebijakan manipulasi jam, toleransi NTP | ASM:E-01–E-04 punya kebijakan | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-29 | BLOCKED | OP-7 | CU-6 (RA-1/RA-2) | Aturan pengumpulan/interupsi lab-proyek | ASM:L5 terisi | Keputusan | Setelah CU-6 | Ya |
| UW-30 | BLOCKED | OP-8, CU-4 | — | Identitas XP, rumus, level, streak, revisi konten | ASM:X-07 terisi | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-31 | BLOCKED | OP-9 | D-01 M-04 | Aturan unlock rinci | ASM:C6 terisi | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-32 | BLOCKED | OP-10, OP-11 | — | Komponen yang boleh diulang; debounce autosave | OP-10, OP-11 terisi | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-33 | BLOCKED | OD-5–OD-9 | D-16, D-17 | Format payload, aturan kata sandi, batas ukuran, retensi snapshot dan log restore, attempt berjalan | OD-5–OD-9 terisi | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-34 | BLOCKED | CO-4–CO-6 | — | Kalender perusahaan, label era, notifikasi jam tenang | CO-4–CO-6 terisi | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-35 | BLOCKED | UO-3–UO-9 | D-14, D-15 | Tipografi, aset, breakpoint, tab bar, performa, field layar | UO-3–UO-9 terisi | Keputusan | Claude siapkan lembar keputusan | Ya |
| UW-36 | BLOCKED | CU-3, CU-5, CU-6, CU-7, CU-9, CU-11 | OP-4 | Format konten, varian, bobot lab, bentuk lab SQL/HTML/Git, rubrik capstone, pembagian W9/W10 | Semua CU terkait terisi | Keputusan | Owner menjawab CU-6-Q1–Q4; Claude siapkan lembar CU-3/5/7/9/11 | Ya |
| UW-41 | BLOCKED | — | — | Daftar delapan skill tambahan (PENDING SOURCE) | Prosedur FIN:SE-1–SE-6 | Daftar dari owner | Owner menyerahkan daftar | Ya |

## 3. Pekerjaan dokumentasi yang dapat dikerjakan Claude (jalur P)

| UW | Status | Pekerjaan | Ketergantungan | AC | Bukti selesai | Aksi berikutnya | Butuh owner |
|---|---|---|---|---|---|---|---|
| UW-37 | OPEN (NOT STARTED) | Konten lengkap 16 modul / 64 komponen ([CURRICULUM_PRODUCTION_PLAN.md](CURRICULUM_PRODUCTION_PLAN.md)) | Bagian yang tidak bergantung keputusan (tujuan, prasyarat, penjelasan pelajaran, glosarium, materi remedial) dapat didraf sekarang; soal, rubrik, test, dan poin menunggu OP-4, CU-6, UW-27, CU-9, CU2-O4, CU-3, CU-5 | CUR:CC-01–CC-11, CPP:CA-01–CA-11 | 64 sel matriks CPP §4 diterima owner | Draf CB-1 bagian penjelasan | Ya, untuk acceptance |
| (persiapan) | — | Lembar keputusan untuk UW-23–UW-25, UW-27, UW-28, UW-30–UW-35, CU-3/5/7/9/11 | — | — | Lembar dibuat | Satu batch lembar keputusan | Ya, untuk keputusan |

## 4. Butuh akses sumber eksternal (jalur P)

| UW | Status | Pekerjaan | AC | Bukti selesai | Aksi berikutnya | Butuh owner |
|---|---|---|---|---|---|---|
| UW-14 | BLOCKED | Verifikasi dataset hari libur dari `syukujitsu.csv` | CAL:AC-02 PASS | Perbandingan tanggal dengan sumber resmi | Owner membuka host `www8.cao.go.jp` atau menyerahkan file | Ya (akses) |
| UW-53 | BLOCKED | Baca sumber resmi yang diblokir (RFC, NIST, W3C, M3, CAO, e-Gov) | Klaim terkait diverifikasi | Kutipan dari sumber | Owner membuka host atau menyediakan salinan | Ya (akses) |

## 5. Penundaan milestone yang disetujui (jalur M, D-22)

| UW | Status | Milestone | Prasyarat | Verifikasi | Penanganan kegagalan | AC (tetap) |
|---|---|---|---|---|---|---|
| UW-21 | DEFERRED | Hasil uji kelayakan Python (setelah UW-10, UW-12) | PY:F-01–F-15 dijalankan | Hasil F-01–F-15 dengan bukti EV | Bila gagal: owner memilih alternatif minggu 9–12 (CU-8) sebelum konten W9–W12 diterima final | Keputusan tertulis |
| UW-38 | DEFERRED | Milestone rilis | Implementasi diizinkan; build CI ada | AP-3–AP-5 | Rilis tidak dilakukan sampai keputusan signing/R8/distribusi ada | AP-3–AP-5 |
| UW-40 | DEFERRED | Milestone UI pertama | Implementasi diizinkan | Keputusan mekanisme effect + uji UI | Memakai pola StateFlow yang sudah disetujui (TD:20) sampai diputuskan | Keputusan tertulis |

## 6. Gerbang otorisasi owner (jalur G — setelah PLANNING CLEAR)

| UW | Status | Gerbang | Prasyarat | Catatan |
|---|---|---|---|---|
| UW-10 | BLOCKED | Izin eksekusi prototipe Python | PLANNING CLEAR: YES | Rencana dan ambang sudah disetujui (D-10); eksekusi butuh izin baru |
| UW-02 | BLOCKED | Izin implementasi | PLANNING CLEAR: YES | D-11; PLANNING CLEAR tidak mengizinkan implementasi (D-20) |

## 7. Verifikasi teknis setelah izin (jalur V)

| UW | Status | Verifikasi | Membutuhkan | AC |
|---|---|---|---|---|
| UW-12 | OPEN (NOT STARTED) | PY:F-01–F-15 | UW-10 | F-01–F-15 PASS dengan bukti EV |
| UW-13 | NOT VERIFIED | Build CI toolchain | UW-02 | Checklist TC §7 |
| UW-15 | NOT VERIFIED | Review dependensi BC, kompatibilitas Android, pengukuran KDF, batas maksimum, CT-1–CT-12 | Izin pengukuran terpisah | Parameter tertulis + bukti; restore produksi nonaktif sampai lolos |
| UW-39 | BLOCKED | Android SDK di cloud (opsional) | Pengaturan jaringan | Opsional |
| UW-52 | OPEN (NOT STARTED) | Cek ulang versi toolchain tepat sebelum scaffold | UW-02 | Sumber resmi bertanggal baru |
| UW-54 | NOT VERIFIED | Butir V toolchain | UW-13 | Log CI |
| UW-55 | NOT VERIFIED | Transfer antarperangkat dengan `allowBackup=false` | UW-02 | Bukti EV per jalur |
| UW-56 | NOT VERIFIED | Keputusan D-12–D-15 di aplikasi (NUM:NA-1–NA-6, ACC:AT-1–AT-6) | UW-02 | Bukti EV |

## 8. Jalur kritis menuju PLANNING CLEAR

```
Keputusan owner: OP-4 (UW-26), CU-6 + CU-3/5/7/9/11 (UW-36), UW-27, CU2-O4 rubrik mini-project
        │
        ▼
CB-0  Templat konten final (CPP §6)
        │
        ▼
CB-1 → CB-2 → CB-3 → CB-4   Produksi 64 komponen (UW-37)
        │
        ▼
CB-R  Review + penerimaan owner seluruh konten
        │
        ▼
PLANNING CLEAR (bersama butir P lain yang paralel)

Paralel (tidak memblokir produksi konten, tetapi wajib untuk PLANNING CLEAR):
UW-23, UW-24, UW-25, UW-28–UW-35, UW-41, UW-14 + UW-53 (akses sumber)
```

Butir dengan dampak terbesar: **UW-37** (beban kerja terbesar, bergantung
pada hampir semua keputusan penilaian).

## 9. Batch perencanaan berikutnya yang direkomendasikan

1. Owner menjawab OP-4-Q1–Q4 dan CU-6-Q1–Q4.
2. Claude menyiapkan satu batch lembar keputusan untuk UW-27 (format dan
   durasi ujian), CU-9 (rubrik capstone), CU2-O4 (rubrik mini-project),
   CU-3, CU-5, CU-7, CU-11.
3. Setelah itu: CB-0 (templat final), lalu CB-1.
