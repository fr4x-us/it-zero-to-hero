# IT ZERO → HERO — Decision Sheet CU-6: Penilaian Lab dan Bobot Test Case

Status: **DIPUTUSKAN OWNER — D-24 (2026-11-24)**, lihat §13; klarifikasi lanjutan §14 **OPEN** · dokumentasi saja · tanpa kode
atau prototipe. Tanggal: **2026-11-24** (direvisi setelah review PR #23,
F-04). Basis: `main` = `bcecdae`.

Rekomendasi di §11 adalah saran, **bukan** keputusan. Terkait CU-6 (bagian
UW-36). Lembar ini mengatur **aturan skor**; eksekusi kode Python dan
isolasinya adalah urusan runtime (O-04, PY:F-01–F-15, **NOT VERIFIED**).
Ambang D-10 **tidak diubah** oleh lembar ini.

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
| LB-R8 | Ambang uji kelayakan D-10: batas waktu eksekusi **3 detik per latihan** (PY:F-11); output **≤ 64 KB per eksekusi, sisanya dipotong** (PY:F-13); target memori proses Python 128 MB (PY:F-12, penegakan belum diverifikasi) | D-10 |

## 2. Opsi bobot test case

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| LW-A Bobot sama | Setiap test case bernilai sama | Sederhana | Test sepele dan test inti bernilai sama |
| LW-B Bobot terdefinisi | Setiap test case punya poin bilangan bulat ≥ 1 yang ditulis penyusun konten | Mencerminkan tingkat kesulitan; tetap deterministik | Bobot harus direview (CC-06) |

## 3. Opsi test wajib dan opsional

| Opsi | Isi | Catatan |
|---|---|---|
| LR-A Penjumlahan murni | Skor aktivitas = jumlah poin test yang lulus; tidak ada test "gerbang" | Ambang komponen 75 sudah menuntut penguasaan |
| LR-B Test gerbang | Bila test wajib gagal, aktivitas bernilai 0 | Keras; satu kesalahan kecil menghapus semua kredit |
| LR-C Test bonus | Test opsional menambah poin di atas max | **Tidak direkomendasikan**: melanggar `earned ≤ max` (D-12) |

## 4. Anggaran eksekusi (usulan; D-10 tetap)

Pembedaan:

- **Ambang D-10 (PY:F-11)** = kriteria penerimaan uji kelayakan runtime:
  kode pelajar harus dapat dihentikan dalam 3 detik per latihan tanpa
  membekukan aplikasi. Ini **bukan** aturan skor dan tidak diubah.
- **Timeout per test** (usulan di bawah) = aturan skor: kapan satu test case
  dinyatakan gagal karena waktu habis.

| Opsi | Isi | Total per latihan |
|---|---|---|
| TB-A Anggaran bersama | Semua test satu aktivitas dijalankan dalam satu eksekusi dengan anggaran total 3 detik; test yang belum tercapai saat anggaran habis = `NOT_RUN` | ≤ 3 detik |
| TB-B Timeout per test | Setiap test dijalankan terpisah dengan timeout `tᵢ` (milidetik bilangan bulat, ditulis penyusun) dan `Σ tᵢ ≤ 3.000 ms` per aktivitas; timeout satu test tidak menghentikan test lain | ≤ 3 detik |

Ketentuan bersama (usulan):

| ID | Ketentuan |
|---|---|
| EB-1 | Yang diukur hanya waktu eksekusi kode pelajar; start interpreter diukur terpisah oleh PY:F-04 dan tidak memotong anggaran pelajar |
| EB-2 | Output: batas 64 KB berlaku **per eksekusi** (PY:F-13). Pada TB-A satu eksekusi mencakup semua test; pada TB-B setiap test satu eksekusi |
| EB-3 | Memori: target 128 MB (PY:F-12). Selama penegakan batas memori belum diverifikasi dan belum disetujui, kegagalan memori **tidak** dibebankan ke pelajar (lihat §6, IF-4) |
| EB-4 | Lab non-Python (biner, Boolean, flowchart, SQL, HTML/CSS, Git): pemeriksa deterministik per jenis; batas sumber daya SQL/HTML/Git menunggu CU-7 |
| EB-5 | Kelayakan TB-B (menjalankan test terpisah dalam anggaran) bergantung pada desain runtime dan **NOT VERIFIED** |

## 5. Hasil per test case

| Kode | Arti | Poin |
|---|---|---|
| `PASS` | Output cocok dengan keluaran yang diharapkan, tanpa melewati batas | Poin test |
| `FAIL_OUTPUT` | Output tidak cocok atau format salah | 0 |
| `FAIL_ERROR` | Error runtime/sintaks dari kode pelajar | 0 |
| `FAIL_TIMEOUT` | Melewati timeout karena kode pelajar | 0 |
| `FAIL_OUTPUT_LIMIT` | Output melewati 64 KB | 0 — **tidak** dibandingkan, walaupun awalan yang terpotong cocok dengan keluaran yang diharapkan |
| `NOT_RUN_LEARNER` | Tidak dijalankan karena anggaran habis oleh kode pelajar (TB-A) atau eksekusi dihentikan karena penyebab pelajar | 0 |
| `EVALUATION_ERROR` | Kegagalan infrastruktur (§6) | Tidak ada skor; lihat §7 |

Output yang dipotong (PY:F-13) tetap boleh ditampilkan ke pelajar sebagai
umpan balik; pemotongan hanya untuk melindungi UI dan memori.

## 6. Penyebab pelajar vs kegagalan infrastruktur

| ID | Penyebab pelajar (test gagal, 0 poin) | ID | Kegagalan infrastruktur (tanpa penalti) |
|---|---|---|---|
| LC-1 | Exception atau error sintaks dari kode pelajar | IF-1 | Runtime/interpreter gagal start atau crash di luar kode pelajar |
| LC-2 | Timeout karena kode pelajar (loop tak berhenti, kerja berlebih) | IF-2 | Proses evaluasi dihentikan sistem (aplikasi ditutup, proses dibunuh OS, perangkat mati) |
| LC-3 | Output melewati 64 KB | IF-3 | Error pemeriksa/fixture/konten (mis. fixture rusak, kunci keluaran hilang) |
| LC-4 | Operasi yang dilarang oleh isolasi (mis. akses jaringan, D-08) ditolak dan menghasilkan error | IF-4 | Kehabisan memori selama batas memori belum diverifikasi dan disetujui (EB-3) |
| — | — | IF-5 | Penyimpanan gagal saat menulis hasil |

Aturan: tanpa kebijakan owner yang disetujui, kegagalan infrastruktur
**tidak pernah** mengurangi skor pelajar, tidak menghabiskan attempt, dan
tidak dicatat sebagai `FAIL`. Kasus yang tidak dapat dipastikan
penyebabnya diperlakukan sebagai infrastruktur.

## 7. Eksekusi tidak lengkap dan pelestarian poin

| ID | Aturan (usulan) |
|---|---|
| IE-1 | Hasil dihitung per test. Dalam satu evaluasi, test yang sudah `PASS` sebelum timeout/error pelajar pada test lain **tetap** mendapat poinnya |
| IE-2 | Bila terjadi `EVALUATION_ERROR` pada aktivitas, **seluruh** evaluasi aktivitas itu dibatalkan (tidak ada skor parsial dari evaluasi yang terganggu infrastruktur). Submission yang sama dievaluasi ulang dari awal; tidak membuat attempt baru |
| IE-3 | Evaluasi ulang submission dan versi konten yang sama harus memberi hasil yang sama; hasil berbeda ditandai sebagai kegagalan infrastruktur, bukan memilih hasil terbaik |
| IE-4 | Antar attempt tidak ada pewarisan poin test (RA-1); skor terbaik dipilih per komponen (D-12). Pada RA-2 skor terbaik dipilih per aktivitas |
| IE-5 | Hasil per test disimpan: kode hasil (§5), poin, versi test, ringkasan output yang dipotong |

## 8. Aktivitas, komponen, remedial, dan XP

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| RA-1 Attempt per komponen | Satu attempt komponen mencakup **semua** aktivitas lab modul; disimpan bertahap (pause/resume, D-01 M-08) dan diserahkan bersama; skor = jumlah poin semua aktivitas | Sesuai "skor terbaik per komponen" (D-12) secara harfiah; riwayat jelas | Remedial mengulang semua aktivitas |
| RA-2 Skor terbaik per aktivitas | Setiap aktivitas dapat diulang sendiri; skor komponen = jumlah skor terbaik tiap aktivitas | Remedial lebih ringan | Menggabungkan bagian dari attempt berbeda; menafsirkan ulang "skor terbaik per komponen" → **butuh persetujuan eksplisit owner** |

| ID | Definisi (usulan) |
|---|---|
| LA-1 | "Aktivitas selesai" = diserahkan dan dievaluasi tanpa `EVALUATION_ERROR` yang tersisa |
| LA-2 | "Attempt komponen selesai" = semua aktivitas attempt itu selesai (LA-1), apa pun skornya. Selama ada `EVALUATION_ERROR` yang belum dievaluasi ulang, attempt berstatus menunggu evaluasi dan tidak dihitung untuk skor terbaik |
| LA-3 | "Komponen memenuhi" = skor attempt selesai ≥ 75 (`4·earned ≥ 3·max`) |
| LA-4 | XP: paling banyak sekali per identitas aktivitas pada penyelesaian pertama yang memenuhi syarat; test case tidak memberi XP; remedial dan varian tidak memberi XP ulang; attempt yang belum selesai (LA-2) tidak memberi XP. "Memenuhi syarat" dan identitas aktivitas menunggu OP-8 (UW-30) |

## 9. Ketergantungan yang belum diputuskan

| ID | Keputusan | Dampak pada lembar ini |
|---|---|---|
| OP-7 (UW-29) | Aturan pengumpulan dan interupsi lab/proyek | Penyimpanan bertahap RA-1, perlakuan aplikasi ditutup di tengah evaluasi (IF-2), batas waktu pengumpulan |
| OP-8 (UW-30) | Identitas aktivitas XP | LA-4: kapan XP diberikan dan untuk identitas apa |
| OP-10 (UW-32) | Komponen yang boleh diulang | Apakah remedial lab (RA-1/RA-2) tersedia setelah `NOT_PASSED` |
| CU-7 (UW-36) | Bentuk lab SQL/HTML/Git | EB-4 |
| O-04, PY:F-01–F-15 (UW-12) | Kelayakan runtime | EB-5, IF-4; **NOT VERIFIED** |

## 10. Contoh dan kasus batas (ilustrasi, tidak dijalankan)

Komponen lab dengan 3 aktivitas (LW-B, LR-A, RA-1), max 110:

| Aktivitas | Test (poin) | Max | Attempt 1 lulus | Poin | Attempt 2 lulus | Poin |
|---|---|---|---|---|---|---|
| A1 | 10, 10, 20 | 40 | 10, 20 | 30 | semua | 40 |
| A2 | 25, 25 | 50 | 25 | 25 | 25 | 25 |
| A3 | 5, 5, 5, 5 | 20 | semua | 20 | semua | 20 |
| **Total** | | **110** | | **75** | | **85** |

- Attempt 1: 75/110 → `4·75 = 300 < 3·110 = 330` → **belum memenuhi**.
- Attempt 2: 85/110 → `340 ≥ 330` → **memenuhi**. Skor terbaik = attempt 2.
- Tepat 75%: 66/88 → `264 ≥ 264` → memenuhi; 65/88 → `260 < 264` → belum.
- IE-1 (TB-B): A1 test 1 dan 2 `PASS` (20), test 3 `FAIL_TIMEOUT` → A1 = 20; poin 20 tetap.
- §5: test berharap 10 baris, kode mencetak 10 baris itu lalu 70 KB tambahan → `FAIL_OUTPUT_LIMIT`, 0 poin.
- IE-2: A2 berhenti karena aplikasi dibunuh OS (IF-2) → evaluasi A2 dibatalkan, dievaluasi ulang; attempt tidak bertambah; tidak ada penalti.

Hitungan di atas hanya aritmetika bilangan bulat (diperiksa 2026-11-24).

## 11. Rekomendasi (saran, bukan keputusan)

**LW-B + LR-A + RA-1 + TB-B**, dengan §5–§7 dan LA-1–LA-4: bobot test
bilangan bulat yang direview, tanpa test gerbang dan tanpa bonus, timeout
per test dengan total ≤ 3 detik per latihan (bila runtime memungkinkan,
EB-5; bila tidak, TB-A), kegagalan infrastruktur tanpa penalti, attempt per
komponen yang mencakup semua aktivitas.

## 12. Pertanyaan untuk owner

1. **CU-6-Q1:** Setujui LW-B (bobot test bilangan bulat yang ditulis dan direview penyusun)?
2. **CU-6-Q2:** Setujui LR-A (tanpa test gerbang, tanpa bonus)?
3. **CU-6-Q3:** Setujui kode hasil §5 dan pembagian penyebab pelajar/infrastruktur §6, termasuk: output > 64 KB selalu gagal, dan kegagalan infrastruktur tanpa penalti?
4. **CU-6-Q4:** Setujui RA-1 (attempt per komponen mencakup semua aktivitas), bukan RA-2, beserta LA-1–LA-4?
5. **CU-6-Q5:** Setujui anggaran eksekusi TB-B (cadangan TB-A) dan EB-1–EB-5, tanpa mengubah ambang D-10?
6. **CU-6-Q6:** Setujui IE-1–IE-5 (pelestarian poin dalam satu evaluasi; evaluasi terganggu infrastruktur diulang utuh)?

~~Status: AWAITING OWNER. CU-6 tetap belum diputuskan; LA-4 tetap bergantung OP-8.~~ *(Historis — dijawab D-24 pada 2026-11-24; lihat §13. LA-4 tetap bergantung OP-8.)*

## 13. Keputusan owner — D-24 (2026-11-24)

| Butir | Keputusan |
|---|---|
| CU-6-Q1 | **LW-B** — test case berbobot eksplisit |
| CU-6-Q2 | **LR-A** — jumlah poin test lulus; tanpa bonus dan tanpa gerbang nol |
| CU-6-Q3 | Kode hasil §5 dan pembagian penyebab §6 disetujui |
| CU-6-Q4 | **RA-1** — attempt mencakup seluruh komponen lab; **LA-1–LA-4** |
| CU-6-Q5 | **TB-B** — timeout per test; **TB-A** cadangan bersyarat bila TB-B tidak layak; **EB-1–EB-5** yang berlaku |
| CU-6-Q6 | **IE-1–IE-5** |

Dipertahankan secara eksplisit: anggaran eksekusi kode pelajar total
3.000 ms per latihan Python; start interpreter diukur terpisah; ambang D-10
tidak berubah; output > 64 KB per eksekusi tidak dapat `PASS` karena awalan
terpotong yang cocok; test yang sudah lulus mempertahankan poin saat test lain
gagal karena kode pelajar; kegagalan infrastruktur membatalkan evaluasi
aktivitas terdampak tanpa penalti; evaluasi ulang submission yang sama tidak
membuat attempt baru; tanpa pewarisan poin test antar attempt; skor terbaik
attempt selesai per komponen; riwayat attempt lengkap; tanpa XP ganda.

Kelayakan runtime tetap **NOT VERIFIED**. UW-36 **tidak** COMPLETE (CU-3,
CU-5, CU-7, CU-9, CU-11, CU2-O3, CU2-O4 belum diputuskan).

## 14. Klarifikasi lanjutan yang diminta D-24 (direvisi setelah review PR #24, F-05; **diputuskan D-35**, lihat §15)

Ambang D-10 tidak berubah: 3 detik per latihan (PY:F-11), output ≤ 64 KB
per eksekusi (PY:F-13), target memori 128 MB (PY:F-12, penegakan NOT
VERIFIED), start interpreter dingin ≤ 5 detik (PY:F-04). Tidak ada nilai
batas agregat final yang ditetapkan di sini; nilai yang belum diukur tetap
**OPEN** sampai pengukuran yang diizinkan (UW-12). Tidak ada runtime atau
benchmark yang dijalankan.

### 14.1 Batas per eksekusi vs batas agregat evaluasi

| ID | Usulan |
|---|---|
| LX-1 | **Per eksekusi** (disetujui D-10/D-24): output ≤ 64 KB per eksekusi; melewati → `FAIL_OUTPUT_LIMIT` untuk test yang dijalankan oleh eksekusi itu. Pada TB-B satu eksekusi = satu test; pada TB-A satu eksekusi = semua test aktivitas, sehingga 64 KB dibagi bersama oleh semua test (perbedaan mode, lihat LX-8) |
| LX-2 | **Agregat evaluasi** (kebijakan wajib, nilai OPEN): setiap aktivitas memiliki batas agregat untuk (a) jumlah test maksimum, (b) total byte output yang **disimpan** untuk tampilan/riwayat, (c) total waktu wall-clock evaluasi termasuk start dan perbandingan, (d) jumlah proses interpreter. Aturan kebijakan: batas sama untuk semua pelajar; ditetapkan owner dari bukti pengukuran yang diizinkan; batas (b) hanya memotong salinan yang disimpan dan tidak memengaruhi skor; melewati (c) atau (d) karena bukan kode pelajar → `EVALUATION_ERROR` tanpa penalti |

### 14.2 Waktu dan proses

| ID | Usulan |
|---|---|
| LX-3 | Anggaran kode pelajar `Σ tᵢ ≤ 3.000 ms` per latihan Python (D-24) hanya menghitung eksekusi kode pelajar. Start interpreter (PY:F-04), komunikasi proses, dan perbandingan output dihitung pada batas agregat LX-2(c), bukan anggaran pelajar |
| LX-4 | Bila memakai beberapa proses: test dijalankan **berurutan**, tidak paralel; waktu kode pelajar dijumlahkan lintas proses dan tetap ≤ 3.000 ms; target memori berlaku per proses; jumlah proses dibatasi LX-2(d) |

### 14.3 Urutan dan isolasi test

| ID | Usulan |
|---|---|
| LX-5 | Urutan test deterministik = urutan indeks di konten (`test_index` 1…n), sama di TB-A dan TB-B; konten menempatkan test inti lebih dulu |
| LX-6 | Isolasi state: setiap test menjalankan kode pelajar dari awal dengan input sendiri dan tidak boleh bergantung pada state test lain. **TB-B**: proses/interpreter baru per test (isolasi penuh menurut desain; NOT VERIFIED). **TB-A**: satu proses untuk semua test; harness memuat ulang kode pelajar per test, tetapi state global interpreter (modul yang sudah diimpor, objek bawaan yang diubah, berkas sementara) **dapat** terbawa antar test — isolasi lebih lemah. Konten wajib ditulis agar benar di kedua mode |

### 14.4 Cadangan TB-A: tanpa klaim kesetaraan

| ID | Usulan |
|---|---|
| LX-7 | Aktivasi TB-A hanya dengan **keputusan owner tertulis** setelah bukti uji kelayakan yang diizinkan menunjukkan TB-B tidak layak. Sebelum aktivasi: (1) daftar semua aktivitas Python terdampak; (2) review setiap test terhadap ketergantungan urutan/state (LX-5, LX-6) dan batas output bersama (LX-1); (3) dokumen perbedaan hasil yang mungkin per aktivitas; (4) owner menyetujui daftar dan perbedaan itu. Berlaku untuk seluruh konten (satu mode per versi konten), tidak per pelajar atau per attempt |
| LX-8 | **Tidak ada klaim kesetaraan skor** antara TB-A dan TB-B. Hasil dapat berbeda karena: timeout kode pelajar menghabiskan anggaran bersama (`NOT_RUN_LEARNER` di TB-A vs test berikutnya tetap dinilai di TB-B); crash proses menghentikan test sisa; output bersama 64 KB; state yang terbawa (LX-6) |
| LX-9 | Setiap attempt mencatat mode eksekusi (TB-A/TB-B), versi konten, dan versi runtime. Attempt historis **tidak** dinilai ulang setelah peralihan; skor terbaik per komponen dan tie ke attempt paling awal (D-12) tetap berlaku lintas mode, dengan catatan mode terlihat di riwayat |

Pertanyaan owner (menggantikan CU-6-Q7–Q11 versi sebelumnya):

| ID | Pertanyaan | Rekomendasi |
|---|---|---|
| CU-6-Q7 | LX-1: batas 64 KB per eksekusi dan perbedaannya di TB-A/TB-B? | Ya |
| CU-6-Q8 | LX-2: kebijakan batas agregat (a)–(d), nilai ditetapkan setelah pengukuran yang diizinkan? | Ya (nilai OPEN) |
| CU-6-Q9 | LX-3, LX-4: pemisahan waktu kode pelajar vs waktu evaluasi; proses berurutan? | Ya |
| CU-6-Q10 | LX-5, LX-6: urutan test deterministik dan aturan isolasi state? | Ya |
| CU-6-Q11 | LX-7: syarat dan prosedur review sebelum aktivasi TB-A? | Ya |
| CU-6-Q12 | LX-8, LX-9: tanpa klaim kesetaraan; pencatatan mode/versi; attempt historis tidak dinilai ulang? | Ya |

## 15. Keputusan owner — D-35 (2026-11-24)

Pernyataan owner: "Saya menyetujui rekomendasi D-26, D-27, D-28, D-29, D-30, D-31, D-32, D-33, D-34, D-35."

CU-6-Q7–Q12 dan LX-1–LX-9 disetujui. Dipertahankan: TB-B mode utama; TB-A
cadangan bersyarat dengan otorisasi owner eksplisit sebelum aktivasi;
anggaran kode pelajar 3.000 ms per latihan Python; output 64 KB per
eksekusi; start interpreter diukur terpisah; urutan test deterministik;
mode eksekusi dan versi konten dicatat; tanpa klaim kesetaraan TB-A/TB-B;
attempt historis dipertahankan; semantik skor terbaik tetap. Kebijakan
sumber daya agregat disetujui hanya sebatas LX-2; **nilai batas final tetap
OPEN** (butuh pengukuran yang diizinkan, UW-12). Tidak ada eksekusi runtime,
benchmark, atau pengukuran yang diizinkan.

## 16. Pertanyaan terbuka: umpan balik test tersembunyi (CU-6-Q13, AWAITING OWNER)

CUR §10 mendefinisikan CU-6 sebagai "batas eksekusi lab **dan kebijakan
umpan balik test tersembunyi**". Bagian kedua belum pernah diputuskan
(D-24/D-35 tidak memuatnya).

| Opsi | Setelah evaluasi, untuk test tersembunyi ditampilkan | Kelebihan | Kekurangan |
|---|---|---|---|
| **HF-A** | Kode hasil (§5) dan **deskripsi kasus** yang ditulis penyusun (mis. "input kosong"), tanpa input/output mentah | Pelajar tahu jenis kasus yang gagal | Penyusun wajib menulis deskripsi |
| HF-B | Hanya jumlah test lulus/gagal | Bank test terlindungi | Umpan balik lemah |
| HF-C | Input, output diharapkan, dan output pelajar | Umpan balik terlengkap | Test tersembunyi menjadi terlihat untuk remedial berikutnya; varian lab (VR-B) membatasi dampaknya |

Test **terlihat** selalu menampilkan input, output diharapkan, dan output
pelajar. **CU-6-Q13:** pilih HF-A, HF-B, atau HF-C. Rekomendasi: **HF-A**
(selaras FB-A untuk teori dan D-34: tidak mengklaim perlindungan, tetapi
tidak membuang nilai remedial).

