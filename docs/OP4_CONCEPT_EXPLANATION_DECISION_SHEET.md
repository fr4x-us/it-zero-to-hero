# IT ZERO → HERO — Decision Sheet OP-4: Penilaian Penjelasan Konsep

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode.
Tanggal: **2026-11-24**. Basis: `main` = `bcecdae` (merge PR #22).

Rekomendasi di §6 adalah saran, **bukan** keputusan. Terkait UW-26 (rubrik
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
| CE-C Penalti jawaban salah | Jawaban salah mengurangi poin | Menekan tebakan | Menambah kompleksitas; tidak sejalan dengan semangat tanpa penalti (BL:35 untuk XP) — **tidak direkomendasikan** |
| CE-D Esai bebas dinilai sendiri (self-assessment) | Siswa menilai penjelasannya sendiri dengan daftar periksa | Melatih refleksi | **Tidak objektif**: tidak boleh menyumbang skor (§5) |

## 3. Aturan kredit penuh, parsial, nol (usulan untuk CE-B)

| Format | Kredit penuh | Kredit parsial | Kredit nol |
|---|---|---|---|
| Memilih alasan (pilihan tunggal) | Pilihan benar | — (semua-atau-tidak) | Pilihan lain / kosong |
| Memilih alasan (pilihan ganda, beberapa benar) | Tepat himpunan benar | `max(0, benar_dipilih − salah_dipilih)` poin, maksimal jumlah opsi benar | Hasil ≤ 0 |
| Mengurutkan proses (n langkah) | Urutan sesuai salah satu urutan yang diterima | 1 poin per pasangan berurutan (adjacent) yang benar, maksimal n − 1 | Tidak ada pasangan benar |
| Mencocokkan konsep (k pasangan) | Semua pasangan benar | 1 poin per pasangan benar | Tidak ada pasangan benar |
| Menemukan kesalahan | Baris/bagian salah ditemukan **dan** perbaikan benar dipilih | Baris/bagian benar ditemukan, perbaikan salah: setengah poin soal (poin soal genap) | Baris/bagian salah |

Catatan: semua poin bilangan bulat; tidak ada pecahan poin (sesuai NP-4).

## 4. Konsep wajib dan jawaban alternatif

| ID | Aturan (PROPOSED) |
|---|---|
| CE-K1 | Setiap tugas mencantumkan konsep wajib yang diuji (mis. "byte = 8 bit") dan kompetensi modulnya |
| CE-K2 | Jawaban alternatif yang benar ditulis eksplisit di kunci (himpunan jawaban diterima), bukan diputuskan saat menilai |
| CE-K3 | Untuk pengurutan, langkah yang dapat ditukar ditulis sebagai beberapa urutan diterima |
| CE-K4 | Kunci jawaban dan rubrik direview manusia sebelum diterima (CC-06) |

Contoh (ilustrasi dokumentasi, bukan konten final):

| Format | Soal | Jawaban benar | Jawaban salah dan alasannya |
|---|---|---|---|
| Memilih alasan | "Mengapa RAM disebut *volatile*?" | "Isinya hilang saat daya mati" | "Karena kapasitasnya kecil" — tidak berkaitan dengan volatilitas |
| Mengurutkan | Urutkan: ambil instruksi, dekode, eksekusi, simpan hasil | Ambil → dekode → eksekusi → simpan | Dekode → ambil → … — dekode tidak mungkin sebelum instruksi diambil |
| Mencocokkan | Cocokkan: DNS, DHCP, HTTP dengan fungsinya | DNS–nama ke alamat; DHCP–pemberian alamat IP; HTTP–transfer halaman web | DNS–pemberian alamat IP — tertukar dengan DHCP |
| Menemukan kesalahan | Flowchart menghitung rata-rata membagi sebelum menjumlahkan | Langkah pembagian ditempatkan setelah penjumlahan selesai | Menandai langkah input sebagai salah — input sudah benar |

Contoh hitungan (CE-B), satu komponen dengan 4 soal (max 15 poin):

| Soal | Format | Max | Jawaban | Poin |
|---|---|---|---|---|
| 1 | Memilih alasan (tunggal) | 4 | Benar | 4 |
| 2 | Mengurutkan 4 langkah | 3 (= n − 1 pasangan) | 2 dari 3 pasangan berurutan benar | 2 |
| 3 | Mencocokkan 4 pasangan | 4 | 3 pasangan benar | 3 |
| 4 | Menemukan kesalahan | 4 (genap) | Baris benar, perbaikan salah | 2 |
| **Total** | | **15** | | **11** |

11/15 = 73,33…% → `4·11 = 44 < 3·15 = 45` → **belum memenuhi 75**. Attempt
remedial dengan 12/15 → `48 ≥ 45` → memenuhi. Bila dua attempt sama-sama
12/15, yang dipakai adalah attempt paling awal (D-12). Semua attempt
tersimpan. Ini contoh dokumentasi; tidak ada yang dijalankan.

## 5. Batas self-assessment

- Self-assessment (CE-D) boleh dipakai sebagai latihan refleksi **tanpa
  skor**; tidak menyumbang nilai komponen, karena tidak objektif.
- Tidak ada evaluasi teks bebas oleh AI (BL:38).

## 6. Rekomendasi (saran, bukan keputusan)

**CE-B** — kredit parsial terdefinisi per format, poin bilangan bulat,
digabung dengan menjumlah poin per komponen (D-13), skor terbaik per
komponen, tie ke attempt paling awal (D-12).

Alur offline: soal dan kunci dibundel di aplikasi; penilaian deterministik
saat attempt diserahkan; hasil per soal disimpan pada attempt; remedial
memakai varian soal setara (CUR:RM-04, RM-05); XP hanya pada penyelesaian
pertama yang memenuhi syarat.

Risiko: kunci jawaban yang dibundel dapat diekstrak (CU-10, UW-25).

## 7. Pertanyaan untuk owner

1. **OP-4-Q1:** Setujui CE-B (kredit parsial terdefinisi per format)?
2. **OP-4-Q2:** Setujui aturan kredit §3, termasuk "pasangan berurutan" untuk pengurutan dan setengah poin (poin soal genap) untuk menemukan kesalahan?
3. **OP-4-Q3:** Tolak CE-C (penalti) dan batasi CE-D (self-assessment) sebagai latihan tanpa skor?
4. **OP-4-Q4:** Setujui CE-K1–CE-K4 (konsep wajib, jawaban alternatif eksplisit, review manusia)?

Status: **AWAITING OWNER**. OP-4 (UW-26) tetap belum diputuskan.
