# IT ZERO → HERO — Decision Sheet OP-8 dan CU-4: XP, Level, Streak, Identitas Aktivitas

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode
atau skema. Tanggal: **2026-11-24**. Basis: `main` = `928e278`. Kode
rujukan: `XP:`. Terkait UW-30 (AC: **ASM:X-07 terisi**).

Rekomendasi adalah saran, **bukan** keputusan.

## 1. Batasan yang sudah disetujui

| ID | Batasan | Sumber |
|---|---|---|
| XR-1 | XP, level, achievement, mastery, dan streak **terpisah** dari nilai akademik | BL:47–49, D-01 M-11 |
| XR-2 | Tanpa penalti XP dan tanpa XP farming | BL:35 |
| XR-3 | XP sekali per identitas aktivitas; remedial/pengulangan tidak memberi XP itu lagi; ledger award persisten | TD:22, TD:38, ASM:A-10, X-01–X-03 |
| XR-4 | XP tidak memengaruhi skor, kelulusan, atau unlock | ASM:X-05, CUR:RM-08 |
| XR-5 | Varian soal tidak menjadi identitas XP baru | CUR:RM-09 (PROPOSED) |
| XR-6 | Tanpa tenggat kalender wajib; jadwal fleksibel mengikuti shift | D-01 M-03 |
| XR-7 | Tanggal lokal dan pergantian hari memakai Asia/Tokyo, 00:00 JST | CAL:Z-01–Z-03 |
| XR-8 | Restore tanpa penggabungan riwayat otomatis; M-2 default, M-1 eksplisit | D-03 |
| XR-9 | LA-4: XP tidak diberikan untuk attempt yang belum selesai; test case tidak memberi XP | D-24 |

## 2. Identitas aktivitas yang stabil (CU-4)

| ID | Aturan (usulan) |
|---|---|
| XI-1 | Identitas XP = `activity_id` dari konten (mis. `mod-w03.lab`), **bukan** ID attempt, ID varian, atau versi konten |
| XI-2 | Slot award per identitas: `completion` dan `mastery` (§3). Kunci ledger = (`activity_id`, slot); unik |
| XI-3 | Varian setara (CU-5) berbagi `activity_id` yang sama → tidak ada XP tambahan lewat varian (XR-5) |
| XI-4 | Revisi konten minor (perbaikan typo, klarifikasi) dan mayor (soal diganti dengan tujuan belajar yang sama) **mempertahankan** `activity_id`; XP yang sudah diberikan tidak diberikan lagi dan tidak dicabut |
| XI-5 | Aktivitas yang benar-benar baru (tujuan belajar baru) mendapat `activity_id` baru dan dapat memberi XP saat diselesaikan |
| XI-6 | Aktivitas yang dihapus dari konten: XP yang sudah diberikan tetap (tanpa penalti, XR-2) |
| XI-7 | `activity_id` tidak pernah dipakai ulang untuk konten berbeda (CUR §4.1) |

## 3. Kelayakan XP

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| XE-A Penyelesaian saja | XP pada attempt pertama yang selesai, berapa pun skornya | Menghargai usaha | Tidak menghargai penguasaan |
| XE-B Penguasaan saja | XP pada attempt pertama yang mencapai ≥ 75 | Mendorong penguasaan | Pelajar yang berjuang tidak mendapat apa pun dalam waktu lama |
| **XE-C Dua slot** | `completion`: attempt pertama yang selesai (LA-2 / `GRADED`); `mastery`: attempt pertama dengan skor komponen ≥ 75 (`4·e ≥ 3·m`). Masing-masing sekali | Menghargai usaha dan penguasaan; remedial yang akhirnya mencapai 75 tetap mendapat mastery **sekali** (bukan farming, karena slot itu belum pernah diberikan) | Perlu dua entri ledger |

Catatan konsistensi: XE-C tidak melanggar XR-3 karena `mastery` adalah slot
yang berbeda dan hanya diberikan sekali; attempt berikutnya tidak memberi
XP apa pun untuk slot yang sudah terisi. Butuh persetujuan eksplisit.

## 4. Rumus XP (usulan, bilangan bulat)

| Jenis aktivitas | `completion` | `mastery` |
|---|---|---|
| Pelajaran (dibaca sampai akhir) | 10 | — |
| Latihan/kuis tidak dinilai | 10 | — |
| Ujian teori (komponen) | 30 | 20 |
| Lab (komponen, RA-1) | 40 | 30 |
| Mini-project (komponen) | 30 | 20 |
| Concept explanation (komponen) | 15 | 10 |
| Modul lulus (`PASSED`) | 50 | — |
| Capstone memenuhi rubrik (CU-9) | 100 | — |

Contoh total (ilustrasi; jumlah pelajaran per modul belum diputuskan): modul
dengan 4 pelajaran dan 2 latihan: `4·10 + 2·10 + 50 + 70 + 50 + 25 + 50 =
305`; 16 modul + capstone: `16·305 + 100 = 4.980` XP. XP tidak pernah
dikurangi; tidak ada XP dari "Jalankan" (SB-2) atau test case.

Opsi lain: XF-B XP sebanding skor (melanggar pemisahan XR-1 secara
semangat dan mendorong pengulangan untuk XP); XF-C XP per menit belajar
(mudah dimanipulasi). Tidak direkomendasikan.

## 5. Level

Ambang kumulatif `L(n) = 50 · n · (n − 1)` XP untuk level `n ≥ 1`:

| Level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| XP minimum | 0 | 100 | 300 | 600 | 1.000 | 1.500 | 2.100 | 2.800 | 3.600 | 4.500 | 5.500 |

Dengan contoh 4.980 XP, pelajar yang menyelesaikan program mencapai level
10. Level **diturunkan** dari total XP ledger (tidak disimpan sebagai sumber
kebenaran terpisah); tanpa batas atas; level tidak pernah turun karena XP
tidak pernah dikurangi.

## 6. Streak (Asia/Tokyo)

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| ST-A Harian | Hari JST berturut-turut dengan aktivitas belajar | Umum di aplikasi belajar | **Konflik** dengan XR-6: jadwal default akhir pekan 2 hari/minggu dan shift kerja membuat streak harian putus secara normal → terasa seperti hukuman |
| ST-B Sesi terjadwal | Sesi terjadwal berturut-turut yang diselesaikan | Menghormati jadwal pribadi | Bergantung modul jadwal dan kalender perusahaan (UW-34); lebih kompleks |
| **ST-C Mingguan** | Minggu JST (Senin 00:00 – Minggu 23:59:59) berturut-turut dengan ≥ 1 aktivitas belajar yang selesai | Selaras 8 jam/minggu dan jadwal fleksibel; tidak menuntut belajar harian | Umpan balik lebih jarang |

Aturan bersama (usulan): aktivitas belajar yang dihitung = pelajaran selesai
atau attempt yang selesai (`GRADED`), dengan tanggal JST dari instant
penyelesaian; streak putus → hitungan kembali ke 0 tanpa pengurangan XP;
"rekor streak terbaik" tetap ditampilkan; streak **tidak** memberi XP (hanya
achievement) agar tidak mendorong aktivitas minimal demi XP; streak
diturunkan dari riwayat aktivitas, sehingga konsisten setelah restore.
Manipulasi jam hanya memengaruhi tampilan gamifikasi, bukan nilai.

## 7. Achievement dan mastery (struktur, katalog final saat produksi konten)

| ID | Usulan |
|---|---|
| XA-1 | Achievement = pencapaian sekali, tanpa XP tambahan selain yang tercantum di §4: modul pertama lulus, tiap fase selesai (4), capstone, streak mingguan 4/8/16 minggu |
| XA-2 | Mastery per kompetensi = tampilan turunan dari skor terbaik soal-soal kompetensi itu; label non-akademik; tidak menggantikan rapor |
| XA-3 | Rapor akademik (4 komponen, ambang) dan gamifikasi tampil terpisah (UI Progress) |

## 8. Restore dan konsistensi progres

| ID | Aturan (usulan) |
|---|---|
| XB-1 | Ledger XP ikut backup/restore (ASM:X-06); restore M-1 mengganti ledger bersama data akademik; M-2 menolak restore yang menghilangkan attempt aktif → ledger tetap konsisten dengan attempt |
| XB-2 | Tidak ada penggabungan ledger dua sumber (D-03); karena itu tidak ada duplikasi award dari restore |
| XB-3 | Setelah restore: total XP, level, streak, mastery, achievement, dan unlock **dihitung ulang** dari data yang dipulihkan |
| XB-4 | Pemeriksaan konsistensi setelah restore: setiap entri ledger menunjuk attempt/aktivitas yang ada; entri yatim dicatat di log restore (D-17) dan tidak dihapus diam-diam |
| XB-5 | Award idempoten: ditulis dalam transaksi yang sama dengan `GRADED` (ASM:X-04) |

## 9. Rekomendasi dan alasan

**XI-1–XI-7 + XE-C + rumus §4 + level §5 + ST-C + XA-1–XA-3 + XB-1–XB-5.**
Alasan pendidikan: menghargai usaha dan penguasaan tanpa tekanan belajar
harian yang bertentangan dengan jadwal shift; gamifikasi tetap terpisah dari
kelulusan (D-19 tidak terpengaruh). Implikasi teknis: ledger dengan kunci unik
(`activity_id`, slot); nilai turunan dihitung ulang; tidak ada skema yang
ditetapkan di sini. Ketergantungan: CU-3 (format ID di konten), CU-5
(varian), OP-7 (definisi selesai), CU-9 (capstone), UW-33/OD-8 (log restore).

## 10. Acceptance criteria

| ID | Kriteria |
|---|---|
| XP-AC-01 | ASM:X-07 terisi: identitas, jumlah, batas, level, streak, achievement, mastery, revisi konten |
| XP-AC-02 | Tidak ada jalur yang memberi XP dua kali untuk (`activity_id`, slot) yang sama, termasuk lewat varian, remedial, revisi, atau restore |
| XP-AC-03 | Tidak ada entri XP negatif; streak putus tidak mengurangi XP |
| XP-AC-04 | Nilai akademik, kelulusan, dan unlock tidak membaca XP |
| XP-AC-05 | Contoh total dan ambang level dapat dihitung ulang manual |

## 11. Pertanyaan untuk owner

| ID | Pertanyaan | Rekomendasi |
|---|---|---|
| OP-8-Q1 | Identitas XP = `activity_id` stabil, termasuk aturan revisi XI-4–XI-6 (CU-4)? | Ya |
| OP-8-Q2 | Kelayakan XE-C (slot completion + mastery, masing-masing sekali)? | XE-C |
| OP-8-Q3 | Jumlah XP §4 dan rumus level §5? | Ya |
| OP-8-Q4 | Streak mingguan ST-C tanpa XP? | ST-C |
| OP-8-Q5 | Struktur achievement/mastery XA-1–XA-3 dan aturan restore XB-1–XB-5? | Ya |

Status: **AWAITING OWNER**. UW-30 tetap BLOCKED.
