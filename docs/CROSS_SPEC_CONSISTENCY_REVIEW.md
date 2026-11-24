# IT ZERO → HERO — Tinjauan Konsistensi Lintas Spesifikasi (Batch D-23–D-25)

Status: dokumentasi · tinjauan atas **usulan** batch ini terhadap keputusan
yang berlaku. Tanggal: **2026-11-24**. Basis: `main` = `928e278`. Kode
rujukan: `XS:`. Direvisi setelah review PR #24 (F-09). Konflik dicatat eksplisit, **tidak** diselesaikan dengan
keputusan baru atas nama owner.

Dokumen yang ditinjau:
[ASSESSMENT_FLOW_DECISION_SHEETS.md](ASSESSMENT_FLOW_DECISION_SHEETS.md) (AF),
[XP_PROGRESS_DECISION_SHEET.md](XP_PROGRESS_DECISION_SHEET.md) (XP),
[CURRICULUM_CONTENT_DECISION_SHEETS.md](CURRICULUM_CONTENT_DECISION_SHEETS.md) (CCD),
[PROJECT_RUBRIC_DECISION_SHEETS.md](PROJECT_RUBRIC_DECISION_SHEETS.md) (RB),
[CU10_ANSWER_KEY_RISK_DECISION_SHEET.md](CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) (CU10),
[CURRICULUM_TEMPLATES_CB0.md](CURRICULUM_TEMPLATES_CB0.md) (TPL),
[CU6_LAB_SCORING_DECISION_SHEET.md](CU6_LAB_SCORING_DECISION_SHEET.md) §14 (LX).

## 1. Pemeriksaan terhadap aturan tetap

| ID | Aturan acuan | AF | XP | CCD | RB | CU10 | LX | Hasil |
|---|---|---|---|---|---|---|---|---|
| XS-01 | Bobot 30/40/20/10 (BL:27–30) | Tidak diubah | Tidak dibaca | Jam ≠ bobot (§D) | Tidak diubah | — | — | Konsisten |
| XS-02 | W ≥ 80 dan komponen ≥ 75, eksak (BL:31–32, D-12) | RE-A mencegah buntu | — | — | `4·e ≥ 3·m` di contoh | — | — | Konsisten |
| XS-03 | Skor terbaik, tie → attempt paling awal, riwayat lengkap (D-12) | Dipertahankan | — | VA-4 mencatat varian | CG-B memisahkan gerbang | — | IE-4 | Konsisten |
| XS-04 | Remedial tanpa batas (BL:33) | Tanpa batas; RE-A, PI-A | — | VA-3 (pemakaian ulang) | MPV-A | — | — | Konsisten |
| XS-05 | NP-4 / poin integer ≤ 10.000 (D-12) | Teori maks. 56/28 | XP integer (bukan nilai akademik) | — | 100 per attempt | — | — | Konsisten |
| XS-06 | Tanpa skor tingkat program (D-19) | — | XP terpisah | — | Gerbang capstone bukan skor | — | — | Konsisten |
| XS-07 | Capstone = mini-project W16 di dalam 128 jam (D-13) | UL-7 | — | P W16 = 5 jam | CP-5 | — | — | Konsisten |
| XS-08 | Penjelasan konsep D-23 | TP-B berbeda **disengaja** untuk teori (lihat XS-C3) | — | — | K4/CR-6 memakai D-23 | — | — | Konsisten dengan catatan |
| XS-09 | Lab D-24 | SB-6 = IE-2 | LA-4 | Varian lab data berbeda | K1 memakai pemeriksa lab | — | D-10 tetap | Konsisten |
| XS-10 | Backup/restore D-03, D-16, D-17 | UL-8, SB-12 → OD-9 | XB-1–XB-5 tanpa merge | — | — | Selaras D-17 | — | Konsisten |
| XS-11 | Offline-first, tanpa server wajib (BL:10, BL:38) | Ya | Ya | UP-A | Ya | AK-D ditolak | — | Konsisten |
| XS-12 | minSdk 29 (D-05) | — | — | SQ-1 membatasi fitur SQL karena versi SQLite bervariasi (NOT VERIFIED) | — | — | — | Konsisten; verifikasi saat implementasi |
| XS-13 | Asia/Tokyo, 00:00 JST (CAL:Z-01–Z-03) | EX-1 instant UTC | ST-C minggu JST | — | — | — | — | Konsisten |
| XS-14 | Aksesibilitas (BL:71, CC-10) | TA-B (usulan baru) | — | A.2, TPL-11 | — | — | — | Konsisten; TA-B butuh keputusan |
| XS-15 | XP sekali per identitas, satu entri per identitas (BL:35, TD:22, TD:38, ASM:X-01–X-03, LA-4) | PI-A tanpa XP baru | XE-B: satu award per `xp_id`; XE-C tidak direkomendasikan | VA-5 | — | — | — | Konsisten (setelah revisi F-01) |
| XS-16 | Lab/proyek tanpa batas waktu (BL:37) | SB-8 | — | — | — | — | Timeout per test hanya batas eksekusi kode, bukan batas sesi | Konsisten |
| XS-17 | Unlock linear, pratinjau modul berikutnya (D-01 M-04) | UL-1–UL-10, PV-A | XP tidak membuka modul | — | — | — | — | Konsisten |
| XS-18 | Konten Python diterima sebagai perencanaan sebelum runtime (RM:RV-1–RV-6) | — | — | CU-11 | CP-4 | — | — | Konsisten |

## 2. Konflik dan ketegangan yang dicatat (tidak diselesaikan sendiri)

| ID | Temuan | Dampak | Penanganan yang diusulkan | Butuh owner |
|---|---|---|---|---|
| XS-C1 | ASM:P-03 (PROPOSED) "tidak kehilangan pekerjaan yang terlihat setelah process death" vs debounce AS-B | Crash tanpa callback dapat menghilangkan ≤ 5 detik ketikan yang belum ditandai tersimpan | Tafsirkan P-03 untuk pekerjaan yang ditandai "Tersimpan"; atau pilih AS-A | OP-11-Q1 |
| XS-C2 | RE-B (hanya komponen < 75 boleh diulang) membuat ASM:B-02/B-06 buntu | Melanggar BL:33 secara efektif | RE-B tidak direkomendasikan | OP-10-Q1 |
| XS-C3 | Teori TP-B semua-atau-tidak vs kredit parsial D-23 untuk concept explanation | Dua aturan berbeda untuk format serupa | Disengaja (komponen berbeda); TP-C tersedia bila owner ingin satu aturan | OP-5-Q3 |
| XS-C4 | ASM:T7, ASM:D-04, ASM:D-05 masih PROPOSED (RECOVERED), tidak tercakup D-01 M-07 | Perilaku dibuka-setelah-tenggat belum disetujui | Diajukan eksplisit | OP-5-Q5 |
| XS-C5 | ST-A (streak harian) bertentangan dengan D-01 M-03 (tanpa tenggat kalender wajib, jadwal akhir pekan/shift) | Streak putus secara normal → terasa sebagai hukuman | ST-C mingguan | OP-8-Q4 |
| XS-C6 | Versi awal batch ini menyebut XE-C (dua slot per aktivitas) otomatis sesuai aturan satu-award — **klaim dicabut** | XE-C bertentangan dengan ASM:X-01 tanpa tafsiran ulang | Rekomendasi diganti XE-B; award pertama pada attempt remedial dijelaskan sebagai award pertama (XE-2), butuh konfirmasi | OP-8-Q2 |
| XS-C7 | CPP §5 versi lama (2,5/1,5/2,5/1,0/0,5) vs CU2-O3 §D | Dua usulan jam berbeda | CPP §5 diganti rujukan ke CU2-O3 (keduanya PROPOSED) | CU2-O3-Q1 |
| XS-C8 | HTML pratinjau butuh WebView (BL:45 "runtime compatibility requires validation") | Pratinjau mungkin tidak tersedia | Pratinjau tidak dinilai (HT-5) | CU-7-Q2 |
| XS-C9 | TB-A dan TB-B dapat memberi hasil berbeda (timeout bersama, crash, output 64 KB bersama, state terbawa) | **Tidak ada klaim kesetaraan** | LX-5–LX-9: urutan deterministik, isolasi, review sebelum aktivasi, pencatatan mode/versi, attempt historis tidak dinilai ulang | CU-6-Q10–Q12 |
| XS-C10 | Rubrik capstone memiliki CR-6 (penjelasan) dan modul W16 juga memiliki komponen Concept 10% | Risiko dianggap penghitungan ganda | Dipisah eksplisit: CR-6 bagian skor Mini-project W16; komponen Concept W16 dinilai sendiri | CU-9-Q2 |
| XS-C11 | CUR §5 "Skor: persentase bobot test case" vs D-12 poin mentah | Bahasa lama | D-12/D-24 berlaku; CUR §5 historis | Tidak |
| XS-C12 | ASM §2.3 OPEN: apakah `PASSED` dapat berubah karena revisi konten | — | UL-9/RV-A: tidak dicabut | OP-9-Q1 |
| XS-C13 | TA-B (perpanjangan waktu aksesibilitas) adalah fitur baru di luar D-01 M-07 | Menambah aturan ujian | Pengecualian eksplisit; maks. 68 menit; dicatat sebelum mulai; di luar 128 jam (TA-1–TA-4) | OP-5-Q6 |
| XS-C14 | Restore M-1 dari snapshot lama dapat menurunkan XP/level/streak vs "tanpa penalti XP" (BL:35) | Bukan penalti progres, tetapi penggantian data yang dipilih pengguna | Dibedakan eksplisit; pratinjau menampilkan perubahan (XP §8.1) | OP-8-Q6 |
| XS-C15 | Pelestarian attempt M-2 tidak membuktikan ledger XP lengkap | Ledger rusak dapat masuk | Validasi XV-1–XV-6; perlakuan RX-A/RX-B dilacak sebagai OD-15 di UW-33 (perluasan pelacakan, butuh persetujuan) | OD-15-Q1 |
| XS-C16 | AS-B (debounce) vs EX-5 (tenggat) | Jawaban di jendela debounce dapat hilang di tenggat | Ujian memakai tulis segera DL-1–DL-9; tidak ada jaminan durabilitas tanpa syarat | OP-5-Q8, OP-11-Q1 |
| XS-C17 | Klaim awal "tanda tangan fungsi tetap memaksa kondisi dan loop" | Klaim tidak benar | Dicabut; CR-2 hanya menguji perilaku | CU-9-Q2 |
| XS-C18 | Versi awal W9 tanpa konversi angka padahal proyek W9 menghitung dari input | Prasyarat hilang | PB-A direvisi: konversi dasar di W9; W10 tanpa percabangan/exception | CU-11-Q1 |
| XS-C19 | Asumsi 6 soal concept dan 3 aktivitas lab per modul dipakai dalam perhitungan beban | Belum disetujui | Diajukan eksplisit | CU2-O5-Q1 |

## 3. Kesimpulan

Tidak ditemukan usulan yang mengubah blueprint, bobot, ambang, D-01–D-25,
atau semantik skor yang disetujui. Sembilan belas ketegangan (XS-C1–XS-C19)
dicatat dan dipetakan ke pertanyaan owner; tidak ada keputusan baru yang
dicatat sebagai disetujui. Semua klaim runtime tetap
**NOT VERIFIED**.
