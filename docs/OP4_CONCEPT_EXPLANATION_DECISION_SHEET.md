# IT ZERO → HERO — Decision Sheet OP-4: Penilaian Penjelasan Konsep

Status: **DIPUTUSKAN OWNER — D-23 (2026-11-24)**, lihat §9 · dokumentasi saja · tanpa kode.
Tanggal: **2026-11-24** (direvisi setelah review PR #23, F-03). Basis:
`main` = `bcecdae` (merge PR #22).

Rekomendasi di §7 adalah saran, **bukan** keputusan. Terkait UW-26 (rubrik
dan bank tugas penjelasan konsep).

## 1. Aturan yang sudah disetujui

| ID | Aturan | Sumber |
|---|---|---|
| CE-R1 | Concept explanation = 10% nilai modul | BL:30 |
| CE-R2 | Penilaian objektif, offline, tanpa AI; tanpa tutor AI; tanpa penilaian server wajib | BL:38, CLAUDE.md, D-01 M-06 |
| CE-R3 | Format tugas: memilih alasan, mengurutkan proses, mencocokkan konsep, menemukan kesalahan | D-01 M-06 |
| CE-R4 | Skor dari poin mentah `earned/max`, maksimum 10.000 per komponen per attempt; perbandingan eksak; komponen ≥ 75 | D-12, BL:32 |
| CE-R5 | Beberapa aktivitas/soal dalam satu komponen digabung dengan menjumlah poin | D-13 |
| CE-R6 | Skor terbaik per komponen; tie → attempt paling awal; semua attempt disimpan; remedial tanpa batas | BL:33–34, D-12 |
| CE-R7 | XP sekali per aktivitas unik yang memenuhi syarat; remedial tidak memberi XP lagi | TD:22, D-13 |
| CE-R8 | Setiap modul memiliki komponen concept explanation (16 komponen) | D-13 |

## 2. Struktur rubrik (opsi)

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| CE-A Semua-atau-tidak per soal | Soal benar penuh = poin penuh; selain itu 0 | Paling sederhana dan deterministik | Tidak menghargai pemahaman sebagian (mis. urutan hampir benar) |
| CE-B Kredit parsial terdefinisi per format | Setiap format punya aturan kredit parsial tertulis (§3) | Tetap objektif dan deterministik; lebih adil untuk soal multi-langkah | Rubrik lebih panjang; perlu kasus uji per aturan |
| CE-C Penalti jawaban salah | Jawaban salah mengurangi poin **komponen** (lintas soal) | Menekan tebakan | Menambah kompleksitas; tidak sejalan dengan semangat tanpa penalti (BL:35 untuk XP) — **tidak direkomendasikan** |
| CE-D Esai bebas dinilai sendiri (self-assessment) | Siswa menilai penjelasannya sendiri dengan daftar periksa | Melatih refleksi | **Tidak objektif**: tidak boleh menyumbang skor (§6) |

Catatan: pengurangan di format pilihan ganda (§3, CE-S2) **bukan** CE-C.
Pengurangan itu lokal di dalam satu soal, dibatasi bawah 0, dan tidak
pernah memengaruhi soal lain.

## 3. Aturan skor deterministik per format (usulan untuk CE-B)

Setiap soal menyimpan jawaban sebagai **ID opsi** (bukan teks). Semua poin
bilangan bulat; tidak ada pecahan (NP-4). `earned` setiap soal selalu
`0 ≤ earned ≤ max_soal`.

| ID | Format | Bentuk jawaban | `max_soal` (eksak) | `earned` |
|---|---|---|---|---|
| CE-S1 | Memilih alasan, pilihan tunggal | Tepat satu ID opsi | `P`, bilangan bulat ≥ 1 yang ditulis penyusun | `P` bila ID = kunci; selain itu 0 |
| CE-S2 | Memilih alasan, pilihan ganda (k opsi benar, k ≥ 1) | Himpunan ID opsi | `k` | `max(0, c − w)`, `c` = opsi benar yang dipilih, `w` = opsi salah yang dipilih. Penuh (`k`) hanya bila himpunan tepat sama dengan kunci |
| CE-S3 | Mengurutkan proses (n langkah, n ≥ 2) | Barisan ID langkah | `n − 1` | Skor adjacency maksimum terhadap **setiap** urutan diterima (CE-S3a–S3c) |
| CE-S4 | Mencocokkan konsep (k item kiri, r ≥ k opsi kanan, satu-ke-satu; r > k berarti ada pengecoh) | Pemetaan ID kiri → ID kanan | `k` | 1 per item kiri yang dipetakan ke pasangan benarnya |
| CE-S5 | Menemukan kesalahan (tepat satu baris/bagian salah per soal) | (ID baris, ID perbaikan) | `P`, bilangan bulat **genap** ≥ 2 | `P` bila baris dan perbaikan benar; `P/2` bila baris benar dan perbaikan salah atau kosong; 0 bila baris salah atau kosong |

### 3.1 Pengurutan dengan beberapa urutan diterima

- **CE-S3a — pasangan adjacency:** untuk barisan jawaban `x₁ … x_m` dan
  satu urutan diterima `S`, hitung jumlah indeks `i` (1 ≤ i < m) dengan
  `x_{i+1}` tepat **sesudah** `x_i` di `S`. Hanya urutan maju yang
  dihitung.
- **CE-S3b — maksimum:** `earned = max` hasil CE-S3a terhadap setiap urutan
  diterima yang **lengkap** di kunci (CE-K3). Satu urutan dipilih utuh;
  pasangan dari urutan diterima yang berbeda **tidak** digabung.
- **CE-S3c — kredit penuh:** `earned = n − 1` hanya bila jawaban sama
  persis dengan salah satu urutan diterima. (Diperiksa: untuk n = 5 dan dua
  urutan diterima, seluruh 120 permutasi memenuhi "skor n − 1 ⇔ sama dengan
  urutan diterima".)

### 3.2 Validasi jawaban

| ID | Kondisi | Perlakuan |
|---|---|---|
| CE-V1 | Kosong (tidak ada ID sama sekali) | `earned = 0`; bukan error; attempt tetap dapat diserahkan |
| CE-V2 | ID tidak dikenal (bukan ID opsi soal tersebut) | Soal **tidak valid** → `earned = 0`, ditandai `INVALID_ANSWER` di hasil per soal |
| CE-V3 | ID ganda (langkah muncul dua kali, opsi dipilih dua kali, item kiri dipetakan dua kali, atau opsi kanan dipakai dua kali) | Tidak valid → `earned = 0`, `INVALID_ANSWER` |
| CE-V4 | Bentuk salah (mis. lebih dari satu ID untuk CE-S1, data tidak dapat diurai) | Tidak valid → `earned = 0`, `INVALID_ANSWER` |
| CE-V5 | Sebagian (CE-S3: barisan tanpa ID asing/ganda tetapi tidak memuat semua langkah; CE-S4: sebagian item kiri tidak dipetakan; CE-S5: baris diisi, perbaikan kosong) | Dinilai dengan aturan formatnya atas bagian yang diisi: CE-S3a atas barisan yang ada; CE-S4 item kosong = 0; CE-S5 = `P/2` bila baris benar |
| CE-V6 | Hasil per soal | Disimpan pada attempt: ID jawaban mentah, `earned`, `max_soal`, penanda validasi, versi soal |

UI dirancang untuk mencegah CE-V2–CE-V4; aturan ini tetap berlaku untuk data
yang tersimpan atau dipulihkan, sehingga hasil selalu deterministik.
`INVALID_ANSWER` tidak memengaruhi soal lain dan tidak membatalkan attempt.

## 4. Konsep wajib dan jawaban alternatif

| ID | Aturan (PROPOSED) |
|---|---|
| CE-K1 | Setiap tugas mencantumkan konsep wajib yang diuji (mis. "byte = 8 bit") dan kompetensi modulnya |
| CE-K2 | Jawaban alternatif yang benar ditulis eksplisit di kunci (himpunan jawaban diterima), bukan diputuskan saat menilai |
| CE-K3 | Untuk pengurutan, langkah yang dapat ditukar ditulis sebagai beberapa urutan diterima, masing-masing lengkap (n langkah) |
| CE-K4 | Kunci jawaban dan rubrik direview manusia sebelum diterima (CC-06) |

Contoh soal (ilustrasi dokumentasi, bukan konten final):

| Format | Soal | Jawaban benar | Jawaban salah dan alasannya |
|---|---|---|---|
| Memilih alasan | "Mengapa RAM disebut *volatile*?" | "Isinya hilang saat daya mati" | "Karena kapasitasnya kecil" — tidak berkaitan dengan volatilitas |
| Mengurutkan | Urutkan: ambil instruksi (F), dekode (D), eksekusi (E), simpan hasil (S) | F → D → E → S | D → F → … — dekode tidak mungkin sebelum instruksi diambil |
| Mencocokkan | Cocokkan DNS, DHCP, HTTP, FTP dengan fungsinya (5 opsi kanan, 1 pengecoh "enkripsi disk") | DNS–nama ke alamat; DHCP–pemberian alamat IP; HTTP–transfer halaman web; FTP–transfer file | DNS–pemberian alamat IP — tertukar dengan DHCP |
| Menemukan kesalahan | Flowchart menghitung rata-rata membagi sebelum menjumlahkan | Langkah pembagian ditempatkan setelah penjumlahan selesai | Menandai langkah input sebagai salah — input sudah benar |

## 5. Contoh hitungan (diperiksa ulang 2026-11-24, tidak dijalankan di aplikasi)

### 5.1 Pengurutan, satu urutan diterima `F D E S` (max 3)

| Jawaban | Pasangan yang dihitung | `earned` |
|---|---|---|
| F D E S | F→D, D→E, E→S | 3 (penuh) |
| S F D E | F→D, D→E | 2 |
| F D S E | F→D | 1 |
| E F D S | F→D | 1 |
| S E D F | — | 0 |

### 5.2 Pengurutan, dua urutan diterima (B dan C dapat ditukar; max 4)

S₁ = `A B C D E`, S₂ = `A C B D E`.

| Jawaban | Terhadap S₁ | Terhadap S₂ | `earned` (CE-S3b) |
|---|---|---|---|
| A B C D E | 4 | 1 | 4 (penuh, = S₁) |
| A C B D E | 1 | 4 | 4 (penuh, = S₂) |
| A C B E D | 0 | 2 | 2 |
| B C A D E | 2 | 1 | 2 |
| A B D C E | 1 | 1 | 1 |
| E D C B A | 0 | 1 | 1 |
| A C B (sebagian, CE-V5) | 0 | 2 | 2 |
| A B B C D E | — | — | 0 (`INVALID_ANSWER`, CE-V3) |

### 5.3 Pilihan ganda (CE-S2), k = 2

| Dipilih | c | w | `earned` |
|---|---|---|---|
| Kedua opsi benar | 2 | 0 | 2 (penuh) |
| Kedua opsi benar + 1 salah | 2 | 1 | 1 |
| 1 benar + 2 salah | 1 | 2 | 0 (bukan −1) |

### 5.4 Satu komponen dengan 4 soal (max 15)

| Soal | Format | `max_soal` | Jawaban | `earned` |
|---|---|---|---|---|
| 1 | CE-S1, P = 4 | 4 | Benar | 4 |
| 2 | CE-S3, n = 4 (`F D E S`) | 3 | `S F D E` | 2 |
| 3 | CE-S4, k = 4, r = 5 | 4 | 3 benar; FTP dipetakan ke pengecoh | 3 |
| 4 | CE-S5, P = 4 | 4 | Baris benar, perbaikan salah | 2 |
| **Total** | | **15** | | **11** |

*Koreksi terhadap versi sebelumnya:* contoh lama menulis "mencocokkan 4
pasangan, 3 benar" tanpa pengecoh. Pada pencocokan satu-ke-satu lengkap
dengan 4 opsi, tiga pasangan benar memaksa pasangan keempat juga benar,
sehingga "tepat 3" tidak mungkin; kini memakai r = 5 (satu pengecoh).

11/15 → `4·11 = 44 < 3·15 = 45` → **belum memenuhi 75**. Attempt remedial
12/15 → `48 ≥ 45` → memenuhi. Bila dua attempt sama-sama 12/15, yang dipakai
attempt paling awal (D-12). Semua attempt tersimpan.

## 6. Batas self-assessment

- Self-assessment (CE-D) boleh dipakai sebagai latihan refleksi **tanpa
  skor**; tidak menyumbang nilai komponen, karena tidak objektif.
- Tidak ada evaluasi teks bebas oleh AI (BL:38).

## 7. Rekomendasi (saran, bukan keputusan)

**CE-B** dengan CE-S1–CE-S5 dan validasi CE-V1–CE-V6: kredit parsial
terdefinisi per format, poin bilangan bulat, digabung dengan menjumlah poin
per komponen (D-13), skor terbaik per komponen, tie ke attempt paling awal
(D-12).

Alur offline: soal dan kunci dibundel di aplikasi; penilaian deterministik
saat attempt diserahkan; hasil per soal disimpan pada attempt (CE-V6);
remedial memakai varian soal setara (CUR:RM-04, RM-05; jumlah minimum
CU-5); XP mengikuti keputusan identitas XP (OP-8, UW-30).

Risiko: kunci jawaban yang dibundel dapat diekstrak (CU-10, UW-25).

## 8. Pertanyaan untuk owner

1. **OP-4-Q1:** Setujui CE-B (kredit parsial terdefinisi per format)?
2. **OP-4-Q2:** Setujui CE-S1–CE-S5, termasuk `max_soal` eksak, adjacency maksimum terhadap satu urutan diterima yang lengkap (CE-S3a–S3c), dan setengah poin (P genap) untuk menemukan kesalahan?
3. **OP-4-Q3:** Tolak CE-C (penalti lintas soal) dan batasi CE-D (self-assessment) sebagai latihan tanpa skor?
4. **OP-4-Q4:** Setujui CE-K1–CE-K4 (konsep wajib, jawaban alternatif eksplisit, review manusia)?
5. **OP-4-Q5:** Setujui validasi CE-V1–CE-V6 (kosong = 0; ID asing/ganda/bentuk salah = 0 dengan `INVALID_ANSWER`; jawaban sebagian dinilai atas bagian yang diisi)?

~~Status: AWAITING OWNER. OP-4 (UW-26) tetap belum diputuskan.~~ *(Historis — dijawab D-23 pada 2026-11-24; lihat §9.)*

## 9. Keputusan owner — D-23 (2026-11-24)

Pernyataan owner: "Saya menyetujui rekomendasi D-23, D-24, D-25."

| Butir | Keputusan |
|---|---|
| OP-4-Q1 | **CE-B** — kredit parsial deterministik per format |
| OP-4-Q2 | **CE-S1–CE-S5** dan **CE-S3a–CE-S3c**: pilihan tunggal penuh/nol; pilihan ganda `max(0, c − w)`; pengurutan = adjacency maksimum terhadap **satu** urutan diterima yang lengkap (pasangan dari urutan berbeda tidak digabung); pencocokan 1 poin per pasangan benar; menemukan kesalahan penuh / setengah (lokasi benar saja) / nol. Poin bilangan bulat eksak |
| OP-4-Q3 | **CE-C ditolak** (tanpa penalti lintas soal); **CE-D** hanya refleksi tanpa skor |
| OP-4-Q4 | **CE-K1–CE-K4**: konsep wajib eksplisit, jawaban alternatif eksplisit, urutan diterima lengkap, review manusia atas kunci dan rubrik |
| OP-4-Q5 | **CE-V1–CE-V6**: kosong = 0; ID asing/ganda/bentuk salah = 0 dengan `INVALID_ANSWER`; jawaban sebagian yang valid dinilai sesuai format; simpan jawaban mentah, poin, maks., status validasi, versi soal |

Ketentuan tambahan dari owner:

| ID | Ketentuan |
|---|---|
| CE-V7 | Jawaban pelajar yang salah bentuk (`INVALID_ANSWER`) **dibedakan** dari kegagalan infrastruktur atau konten rusak (mis. kunci hilang, versi soal tidak cocok, data tersimpan rusak di luar jawaban). Kegagalan infrastruktur/konten **tidak** dinilai 0: soal/attempt ditandai `EVALUATION_ERROR`, tidak dihitung untuk skor terbaik, dan dinilai ulang setelah konten valid tanpa attempt baru (selaras D-24 IE-2) |
| CE-V8 | Tanpa penilaian AI, tutor AI, atau penilaian server wajib |

UW-26 **tetap OPEN**: AC CUR:CC-08 mencakup bank soal penjelasan konsep
untuk ke-16 modul, yang belum ditulis (UW-37, CB-1–CB-4).
