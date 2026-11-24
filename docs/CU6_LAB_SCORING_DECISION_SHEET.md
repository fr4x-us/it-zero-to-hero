# IT ZERO → HERO — Decision Sheet CU-6: Penilaian Lab dan Bobot Test Case

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode
atau prototipe. Tanggal: **2026-11-24**. Basis: `main` = `bcecdae`.

Rekomendasi di §6 adalah saran, **bukan** keputusan. Terkait CU-6 (bagian
UW-36). Lembar ini mengatur **aturan skor**; eksekusi kode Python dan
isolasinya adalah urusan runtime (O-04, PY:F-01–F-15, NOT VERIFIED).

## 1. Aturan yang sudah disetujui

| ID | Aturan | Sumber |
|---|---|---|
| LB-R1 | Laboratory = 40% nilai modul; setiap modul memiliki komponen lab | BL:28, D-13 |
| LB-R2 | Komponen ≥ 75; nilai tertimbang ≥ 80; perbandingan eksak tanpa pembulatan dini | BL:31–32, D-12 |
| LB-R3 | Poin mentah bilangan bulat `earned/max`; maksimum 10.000 per komponen per attempt | D-12 |
| LB-R4 | Beberapa aktivitas dalam satu komponen digabung dengan menjumlah poin | D-13 |
| LB-R5 | Skor terbaik per komponen; tie → attempt paling awal; semua attempt disimpan; remedial tanpa batas | BL:33–34, D-12 |
| LB-R6 | XP sekali per aktivitas unik yang memenuhi syarat | TD:22, D-13 |
| LB-R7 | Test case objektif dan deterministik | BL:44, QG LB-5 |
| LB-R8 | Batas waktu eksekusi 3 detik per latihan; output maks. 64 KB (ambang uji D-10, rencana) | D-10 |

## 2. Opsi bobot test case

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| LW-A Bobot sama | Setiap test case bernilai sama | Sederhana | Test sepele dan test inti bernilai sama |
| LW-B Bobot terdefinisi | Setiap test case punya poin bilangan bulat yang ditulis penyusun konten | Mencerminkan tingkat kesulitan; tetap deterministik | Bobot harus direview (CC-06) |

## 3. Opsi test wajib dan opsional

| Opsi | Isi | Catatan |
|---|---|---|
| LR-A Penjumlahan murni | Skor aktivitas = jumlah poin test yang lulus; tidak ada test "gerbang" | Ambang komponen 75 sudah menuntut penguasaan |
| LR-B Test gerbang | Bila test wajib gagal, aktivitas bernilai 0 | Keras; satu kesalahan kecil menghapus semua kredit |
| LR-C Test bonus | Test opsional menambah poin di atas max | **Tidak direkomendasikan**: melanggar `earned ≤ max` (D-12) |

## 4. Kasus khusus (usulan)

| Kasus | Perlakuan |
|---|---|
| Output tidak valid (format salah) | Test tersebut gagal (0 poin) |
| Error runtime | Test yang terdampak gagal; test lain tetap dinilai bila dapat dijalankan terpisah (bergantung desain runtime, NOT VERIFIED) |
| Timeout (melewati batas waktu) | Test yang sedang berjalan dan test yang belum dijalankan dinilai 0 |
| Output melewati batas | Dipotong; test yang bergantung pada bagian terpotong gagal |
| Lab non-Python (biner, Boolean, flowchart, SQL, HTML/CSS) | Model skor sama (poin per pemeriksaan deterministik); pemeriksa spesifik per jenis lab |

## 5. Aktivitas, komponen, dan remedial

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| RA-1 Attempt per komponen | Satu attempt komponen mencakup **semua** aktivitas lab modul; disimpan bertahap (pause/resume, D-01 M-08) dan diserahkan bersama; skor = jumlah poin semua aktivitas | Sesuai "skor terbaik per komponen" (D-12) secara harfiah; riwayat jelas | Remedial mengulang semua aktivitas |
| RA-2 Skor terbaik per aktivitas | Setiap aktivitas dapat diulang sendiri; skor komponen = jumlah skor terbaik tiap aktivitas | Remedial lebih ringan | Menggabungkan bagian dari attempt berbeda ("memilih bagian terbaik"); menafsirkan ulang "skor terbaik per komponen" → **butuh persetujuan eksplisit owner** |

"Aktivitas selesai" = diserahkan dan dinilai. "Komponen selesai" = attempt
komponen diserahkan dan dinilai, apa pun hasilnya; "komponen memenuhi" =
skor ≥ 75.

XP: diberikan pada penyelesaian pertama yang memenuhi syarat untuk setiap
identitas aktivitas; test case tidak memberi XP; remedial dan varian tidak
memberi XP ulang (detail identitas: UW-30, OPEN).

## 6. Contoh dan kasus batas (ilustrasi, tidak dijalankan)

Komponen lab dengan 3 aktivitas (LW-B, LR-A, RA-1), max 110:

| Aktivitas | Test (poin) | Max | Attempt 1 lulus | Poin | Attempt 2 lulus | Poin |
|---|---|---|---|---|---|---|
| A1 | 10, 10, 20 | 40 | 10, 20 | 30 | semua | 40 |
| A2 | 25, 25 | 50 | 25 | 25 | 25 | 25 |
| A3 | 5, 5, 5, 5 | 20 | semua | 20 | semua | 20 |
| **Total** | | **110** | | **75** | | **85** |

- Attempt 1: 75/110 = 68,18…% → `4·75 = 300 < 3·110 = 330` → **belum memenuhi**.
- Attempt 2: 85/110 = 77,27…% → `340 ≥ 330` → **memenuhi**. Skor terbaik = attempt 2.
- Tepat 75%: 66/88 → `264 ≥ 264` → memenuhi; 65/88 (73,86…%) → `260 < 264` → belum.
- Batas poin: total max per komponen per attempt ≤ 10.000 (D-12).

Hitungan di atas hanya aritmetika bilangan bulat (diperiksa 2026-11-24).

## 7. Rekomendasi (saran, bukan keputusan)

**LW-B + LR-A + RA-1**: bobot test bilangan bulat yang direview, tanpa
test gerbang dan tanpa bonus, attempt per komponen yang mencakup semua
aktivitas, skor = jumlah poin. Paling sesuai dengan D-12/D-13 dan NP-4.

## 8. Pertanyaan untuk owner

1. **CU-6-Q1:** Setujui LW-B (bobot test bilangan bulat yang ditulis dan direview penyusun)?
2. **CU-6-Q2:** Setujui LR-A (tanpa test gerbang, tanpa bonus)?
3. **CU-6-Q3:** Setujui perlakuan kasus khusus §4 (output tidak valid, error, timeout, output terpotong)?
4. **CU-6-Q4:** Setujui RA-1 (attempt per komponen mencakup semua aktivitas), bukan RA-2?

Status: **AWAITING OWNER**. CU-6 tetap belum diputuskan.
