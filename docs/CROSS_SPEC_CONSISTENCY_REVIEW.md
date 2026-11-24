# IT ZERO → HERO — Tinjauan Konsistensi Lintas Spesifikasi (Batch D-23–D-25)

Status: dokumentasi · tinjauan atas **usulan** batch ini terhadap keputusan
yang berlaku. Tanggal: **2026-11-24**. Basis: `main` = `928e278`. Kode
rujukan: `XS:`. Konflik dicatat eksplisit, **tidak** diselesaikan dengan
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
| XS-15 | XP sekali per identitas, tanpa penalti (BL:35, TD:22) | PI-A tanpa XP baru | XE-C dua slot (lihat XS-C6) | VA-5 | — | — | — | Konsisten dengan catatan |
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
| XS-C6 | XE-C memberi XP `mastery` pada remedial pertama yang mencapai 75 | Dapat dibaca sebagai "remedial memberi XP"; sebenarnya slot berbeda yang diberikan sekali | Butuh persetujuan eksplisit; XE-A/XE-B tersedia | OP-8-Q2 |
| XS-C7 | CPP §5 versi lama (2,5/1,5/2,5/1,0/0,5) vs CU2-O3 §D | Dua usulan jam berbeda | CPP §5 diganti rujukan ke CU2-O3 (keduanya PROPOSED) | CU2-O3-Q1 |
| XS-C8 | HTML pratinjau butuh WebView (BL:45 "runtime compatibility requires validation") | Pratinjau mungkin tidak tersedia | Pratinjau tidak dinilai (HT-5) | CU-7-Q2 |
| XS-C9 | TB-A sebagai cadangan dapat memberi hasil berbeda dari TB-B pada timeout kode pelajar | Kesetaraan skor tidak sempurna | LX-5: satu mode per versi konten, dicatat pada attempt, butuh keputusan owner | CU-6-Q10, Q11 |
| XS-C10 | Rubrik capstone memiliki CR-6 (penjelasan) dan modul W16 juga memiliki komponen Concept 10% | Risiko dianggap penghitungan ganda | Dipisah eksplisit: CR-6 bagian skor Mini-project W16; komponen Concept W16 dinilai sendiri | CU-9-Q2 |
| XS-C11 | CUR §5 "Skor: persentase bobot test case" vs D-12 poin mentah | Bahasa lama | D-12/D-24 berlaku; CUR §5 historis | Tidak |
| XS-C12 | ASM §2.3 OPEN: apakah `PASSED` dapat berubah karena revisi konten | — | UL-9/RV-A: tidak dicabut | OP-9-Q1 |
| XS-C13 | TA-B (perpanjangan waktu aksesibilitas) adalah fitur baru di luar D-01 M-07 | Menambah aturan ujian | Diajukan sebagai opsi; tidak diasumsikan | OP-5-Q6 |

## 3. Kesimpulan

Tidak ditemukan usulan yang mengubah blueprint, bobot, ambang, D-01–D-25,
atau semantik skor yang disetujui. Tiga belas ketegangan (XS-C1–XS-C13)
dicatat dan dipetakan ke pertanyaan owner. Semua klaim runtime tetap
**NOT VERIFIED**.
