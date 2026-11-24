# IT ZERO → HERO — Decision Sheet OP-8 dan CU-4: XP, Level, Streak, Identitas Aktivitas

Status: **DIPUTUSKAN OWNER — D-28, D-29 (2026-11-24)**, lihat §14; perluasan validasi §8.2a **AWAITING OWNER** · dokumentasi saja · tanpa kode
atau skema. Tanggal: **2026-11-24** (direvisi setelah review PR #24, F-01,
F-02). Basis: `main` = `928e278`. Kode rujukan: `XP:`. Terkait UW-30 (AC:
**ASM:X-07 terisi**) dan UW-33 (validasi restore, OD-15).

Rekomendasi adalah saran, **bukan** keputusan. Semua keputusan XP baru tetap
**AWAITING OWNER**.

## 1. Batasan yang sudah disetujui

| ID | Batasan | Sumber |
|---|---|---|
| XR-1 | XP, level, achievement, mastery, dan streak **terpisah** dari nilai akademik | BL:47–49, D-01 M-11 |
| XR-2 | Tanpa penalti XP dan tanpa XP farming | BL:35 |
| XR-3 | XP diberikan **sekali** per identitas aktivitas yang sama; pengulangan/remedial tidak memberi XP itu lagi; ledger award persisten; satu entri award per identitas | TD:22, TD:38, ASM:A-10, ASM:X-01–X-03 |
| XR-4 | XP tidak memengaruhi skor, kelulusan, atau unlock | ASM:X-05, CUR:RM-08 |
| XR-5 | Varian soal tidak menjadi identitas XP baru | CUR:RM-09 (PROPOSED) |
| XR-6 | Tanpa tenggat kalender wajib; jadwal fleksibel mengikuti shift | D-01 M-03 |
| XR-7 | Tanggal lokal memakai Asia/Tokyo; pergantian hari 00:00 JST | CAL:Z-01–Z-03 |
| XR-8 | Restore tanpa penggabungan riwayat otomatis; M-2 default, M-1 eksplisit dengan snapshot pra-restore | D-03 |
| XR-9 | Penanda asal-usul dan log restore informatif; rapor = catatan belajar mandiri | D-17 |
| XR-10 | LA-4: XP paling banyak sekali per identitas aktivitas pada penyelesaian pertama yang memenuhi syarat; attempt belum selesai tidak memberi XP; test case tidak memberi XP | D-24 |

## 2. Koreksi terhadap versi sebelumnya (F-01)

Versi sebelumnya merekomendasikan XE-C (dua slot award `completion` dan
`mastery` untuk aktivitas yang sama) dan menyebutnya konsisten dengan XR-3.
Klaim itu **dicabut**: ASM:X-01 menetapkan **satu** entri award per identitas
aktivitas, sehingga dua award untuk aktivitas yang sama tidak otomatis
sesuai. XE-C tetap dicantumkan sebagai opsi yang membutuhkan persetujuan
eksplisit untuk menafsirkan ulang X-01, tetapi **tidak direkomendasikan**.

## 3. Identitas XP (CU-4)

| ID | Aturan (usulan) |
|---|---|
| XI-1 | Satu identitas XP = satu `xp_id` stabil dari katalog konten; **bukan** ID attempt, ID varian, atau versi konten |
| XI-2 | **Aktivitas dinilai**: identitas pada tingkat **komponen** — `mod-wNN.theory`, `mod-wNN.lab`, `mod-wNN.project`, `mod-wNN.concept` (64 identitas). Aktivitas lab individual di dalam komponen (RA-1) **tidak** memiliki identitas XP sendiri, karena kriteria penguasaan (≥ 75) berlaku pada komponen |
| XI-3 | **Aktivitas tidak dinilai**: setiap pelajaran (`mod-wNN.les-nn`) dan setiap set latihan (`mod-wNN.prac-nn`) memiliki identitas sendiri |
| XI-4 | **Milestone** (butuh persetujuan terpisah, OP-8-Q7): `mod-wNN.passed` (modul `PASSED`) dan `program.capstone` (gerbang capstone terpenuhi, CU-9) adalah identitas terpisah dari komponen |
| XI-5 | Varian setara (CU-5) berbagi identitas komponen → tidak ada XP lewat varian |
| XI-6 | Revisi konten minor dan mayor dengan tujuan belajar sama **mempertahankan** `xp_id`; award yang sudah ada tidak diulang dan tidak dicabut |
| XI-7 | Aktivitas baru (tujuan belajar baru) mendapat `xp_id` baru |
| XI-8 | Identitas yang dihentikan dicatat di daftar **identitas pensiun** katalog (ID + versi terakhir); award lama tetap sah (XR-2) |
| XI-9 | `xp_id` tidak pernah dipakai ulang untuk konten berbeda (CUR §4.1) |

Opsi lain: XI-B identitas per aktivitas lab (butuh kriteria penguasaan per
aktivitas yang belum ada; menambah banyak award kecil). Tidak
direkomendasikan.

## 4. Kelayakan XP

| Opsi | Isi | Kesesuaian dengan X-01 | Rekomendasi |
|---|---|---|---|
| XE-A Penyelesaian | Award saat attempt komponen pertama selesai (LA-2 / `GRADED`), berapa pun skornya | Satu award | Tidak — tidak menghargai penguasaan |
| **XE-B Penguasaan** | Award **sekali** saat komponen **pertama kali** mencapai kriteria penguasaan yang disetujui: skor attempt selesai ≥ 75 (`4·e ≥ 3·m`) | Satu award per identitas | **Ya** |
| XE-C Dua slot | `completion` + `mastery` untuk identitas yang sama | **Butuh tafsiran ulang X-01** | Tidak |

Aturan XE-B:

| ID | Aturan |
|---|---|
| XE-1 | Award ditulis dalam transaksi yang sama dengan `GRADED` dari attempt yang **pertama** memenuhi kriteria (ASM:X-04) |
| XE-2 | Bila kriteria pertama kali tercapai pada attempt remedial, award diberikan pada attempt itu. Ini **bukan** XP ganda: belum ada award untuk identitas itu sebelumnya. Attempt sesudahnya (remedial, perbaikan PI-A, varian) tidak pernah memberi XP untuk identitas itu (XR-3, "again") — tafsiran ini butuh konfirmasi owner (OP-8-Q2) |
| XE-3 | Penyelesaian dan penguasaan **ditampilkan** terpisah (mis. "Selesai", "Dikuasai") tanpa XP tambahan |
| XE-4 | Aktivitas tidak dinilai: award sekali saat pelajaran dibuka sampai bagian akhir (`les`) atau set latihan diselesaikan pertama kali (`prac`), berapa pun skornya (opsi UG-A). Opsi UG-B: tanpa XP untuk aktivitas tidak dinilai |
| XE-5 | Milestone (bila disetujui): `mod-wNN.passed` saat modul pertama kali `PASSED`; `program.capstone` saat gerbang capstone pertama kali terpenuhi |
| XE-6 | Attempt yang belum selesai, test case, dan "Jalankan" (SB-2) tidak memberi XP (XR-10) |

## 5. Jumlah XP (usulan, bilangan bulat)

| Identitas | XP |
|---|---|
| Pelajaran (`les`, UG-A) | 5 |
| Set latihan (`prac`, UG-A) | 10 |
| Theory (komponen) | 50 |
| Laboratory (komponen) | 70 |
| Mini-project (komponen) | 50 |
| Concept explanation (komponen) | 25 |
| Milestone modul lulus | 50 |
| Milestone capstone | 100 |

Contoh total (ilustrasi; jumlah pelajaran dan set latihan per modul belum
diputuskan — asumsi 4 pelajaran dan 2 set latihan):
`4·5 + 2·10 + 50 + 70 + 50 + 25 + 50 = 285` per modul; 16 modul + capstone:
`16·285 + 100 = 4.660` XP (diperiksa 2026-11-24). Tanpa milestone (bila
OP-8-Q7 ditolak): `16·235 = 3.760` XP.

## 6. Level

Ambang kumulatif `L(n) = 50 · n · (n − 1)` XP untuk level `n ≥ 1`:

| Level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| XP minimum | 0 | 100 | 300 | 600 | 1.000 | 1.500 | 2.100 | 2.800 | 3.600 | 4.500 | 5.500 |

Contoh 4.660 XP → level 10 (4.500 ≤ 4.660 < 5.500). Contoh 3.760 XP → level
9 (3.600 ≤ 3.760 < 4.500). Level diturunkan dari total ledger; tanpa batas
atas.

## 7. Ledger

| ID | Aturan |
|---|---|
| XL-1 | Kunci unik ledger = `xp_id` (satu entri per identitas, ASM:X-01) |
| XL-2 | Entri memuat: `xp_id`, jumlah XP, versi katalog, ID attempt pemicu (untuk identitas dinilai) atau ID peristiwa (pelajaran/latihan/milestone), instant UTC |
| XL-3 | Tidak ada entri negatif; tidak ada pengurangan XP dalam progres biasa |

## 8. Restore dan konsistensi (revisi F-02)

### 8.1 Progres biasa vs penggantian snapshot

- **Progres biasa** tidak pernah mengurangi XP, level, atau streak karena
  penalti (XR-2).
- **Restore M-1** (pilihan eksplisit pengguna, D-03) **mengganti** data aktif
  dengan isi backup, termasuk ledger XP. Bila backup lebih lama, total XP,
  level, streak, achievement, dan mastery **dapat turun**. Ini bukan penalti
  XP, melainkan akibat penggantian snapshot yang dipilih pengguna. Pratinjau
  restore wajib menampilkan perubahan itu (XP sekarang → XP sesudah restore)
  sebelum konfirmasi.
- **Restore M-2** menolak restore yang menghilangkan attempt akademik yang
  ada di data aktif. Pelestarian attempt **tidak** membuktikan bahwa ledger
  XP di backup lengkap atau benar; ledger divalidasi terpisah (§8.2).

### 8.2 Validasi ledger saat pratinjau restore (usulan; perlakuan → OD-15, UW-33)

| ID | Pemeriksaan | Contoh |
|---|---|---|
| XV-1 | Award ganda | Dua entri dengan `xp_id` sama |
| XV-2 | Award hilang | Komponen dengan attempt selesai ≥ 75 tetapi tanpa entri |
| XV-3 | Identitas tidak dikenal | `xp_id` tidak ada di katalog aktif **maupun** daftar identitas pensiun (XI-8) |
| XV-4 | Jumlah tidak valid | Negatif, nol, atau berbeda dari jumlah katalog untuk versi yang tercatat |
| XV-5 | Entri yatim | Entri menunjuk ID attempt/peristiwa yang tidak ada di backup |
| XV-6 | Identitas pensiun | `xp_id` ada di daftar pensiun → **sah**, bukan temuan kerusakan |

Prinsip: tidak ada perbaikan, penghapusan, penggabungan, atau pembuatan
entri XP maupun riwayat akademik secara diam-diam. Temuan ditampilkan di
pratinjau dan dicatat di log restore (D-17).

| Opsi perlakuan temuan XV-1–XV-5 | Isi | Catatan |
|---|---|---|
| **RX-A** | Restore ditolak bila ada temuan; data aktif dipertahankan | Paling aman; backup rusak tidak masuk |
| RX-B | Restore boleh dengan konfirmasi eksplisit; data dipulihkan **apa adanya**; temuan dicatat; nilai turunan dihitung dari ledger apa adanya | Pengguna tetap dapat memakai backup lama; ledger bisa tidak konsisten |

Keputusan perlakuan dan rincian validasi dilacak sebagai **OD-15** di UW-33
(sejalan D-25: sisa perencanaan restore di UW-33). D-03 dan D-17 tidak
berubah.

### 8.3 Setelah restore

Total XP, level, streak, mastery, achievement, dan unlock dihitung ulang dari
data yang dipulihkan. Tidak ada award yang dibuat otomatis untuk XV-2.

## 9. Streak (Asia/Tokyo)

| Opsi | Isi | Catatan |
|---|---|---|
| ST-A Harian | Hari JST berturut-turut dengan aktivitas | **Konflik** dengan XR-6 (jadwal akhir pekan/shift) |
| ST-B Sesi terjadwal | Sesi terjadwal berturut-turut | Bergantung kalender perusahaan (UW-34) |
| **ST-C Mingguan** | Minggu JST berturut-turut dengan ≥ 1 aktivitas belajar selesai | Selaras 8 jam/minggu |

Definisi ST-C:

| ID | Aturan |
|---|---|
| SK-1 | Minggu `k` = interval setengah terbuka `[Senin 00:00 JST, Senin berikutnya 00:00 JST)` |
| SK-2 | Aktivitas pada instant `t` termasuk minggu `k` bila `awal_k ≤ t < akhir_k` (dikonversi ke Asia/Tokyo) |
| SK-3 | Aktivitas belajar = pelajaran selesai (XE-4) atau attempt selesai (`GRADED`) |
| SK-4 | Minggu berjalan yang belum ada aktivitasnya **tidak** memutus streak; streak putus hanya setelah satu minggu penuh berakhir tanpa aktivitas |
| SK-5 | Nilai streak = jumlah minggu berturut-turut dengan aktivitas, berakhir di minggu berjalan bila sudah ada aktivitas, atau di minggu sebelumnya bila belum |
| SK-6 | Streak tidak memberi XP; streak putus tidak mengurangi XP; rekor terbaik ditampilkan |

## 10. Achievement dan mastery

| ID | Usulan |
|---|---|
| XA-1 | Achievement tanpa XP tambahan: modul pertama lulus, tiap fase selesai, capstone, streak 4/8/16 minggu |
| XA-2 | Mastery per kompetensi = tampilan turunan dari skor terbaik; label non-akademik |
| XA-3 | Rapor akademik dan gamifikasi tampil terpisah |

## 11. Rekomendasi dan alasan

**XI-1–XI-9 (komponen sebagai identitas dinilai) + XE-B (XE-1–XE-6, UG-A) +
§5 + level §6 + XL-1–XL-3 + validasi XV-1–XV-6 dengan RX-A + ST-C
(SK-1–SK-6) + XA-1–XA-3.** Milestone (XI-4) direkomendasikan, tetapi
diputuskan terpisah. Alasan pendidikan: XP mengikuti penguasaan, bukan jumlah
attempt; tidak ada tekanan harian. Implikasi teknis: satu entri per
identitas; nilai turunan dihitung ulang; validasi restore deterministik.

## 12. Acceptance criteria

| ID | Kriteria |
|---|---|
| XP-AC-01 | ASM:X-07 terisi: identitas, kelayakan, jumlah, level, streak, achievement, mastery, revisi konten |
| XP-AC-02 | Tidak ada jalur yang menghasilkan dua entri untuk `xp_id` yang sama (remedial, varian, revisi, restore) |
| XP-AC-03 | Progres biasa tidak pernah mengurangi XP; penurunan karena M-1 ditampilkan di pratinjau |
| XP-AC-04 | Nilai akademik, kelulusan, dan unlock tidak membaca XP |
| XP-AC-05 | Contoh total, level, dan batas minggu dapat dihitung ulang manual |
| XP-AC-06 | Validasi XV-1–XV-6 tertulis; tidak ada perbaikan diam-diam |

## 13. Pertanyaan untuk owner

| ID | Pertanyaan | Rekomendasi |
|---|---|---|
| OP-8-Q1 | Identitas XP XI-1–XI-9: komponen sebagai identitas aktivitas dinilai (aktivitas lab individual tanpa identitas XP), pelajaran/latihan beridentitas sendiri, revisi dan identitas pensiun (CU-4)? | Ya |
| OP-8-Q2 | Kelayakan XE-B (sekali saat pertama mencapai ≥ 75), termasuk tafsiran XE-2 bahwa award pertama pada attempt remedial bukan XP ganda? | XE-B |
| OP-8-Q3 | Aktivitas tidak dinilai: UG-A (XP sekali) atau UG-B (tanpa XP)? | UG-A |
| OP-8-Q4 | Jumlah XP §5 dan rumus level §6? | Ya |
| OP-8-Q5 | Streak ST-C dengan SK-1–SK-6? | ST-C |
| OP-8-Q6 | Achievement/mastery XA-1–XA-3 dan tampilan penurunan XP pada restore M-1 (§8.1)? | Ya |
| OP-8-Q7 | Milestone `mod-wNN.passed` (50) dan `program.capstone` (100) sebagai identitas terpisah? | Ya |
| OD-15-Q1 | Validasi ledger XV-1–XV-6 saat restore dan perlakuan temuan RX-A (tolak) atau RX-B (pulihkan apa adanya dengan konfirmasi)? (UW-33) | RX-A |

~~Status: **AWAITING OWNER**. UW-30 dan UW-33 tetap BLOCKED.~~ *(Historis — dijawab owner 2026-11-24; lihat bagian keputusan di bawah.)*

## 14. Keputusan owner — D-28, D-29 (2026-11-24)

Pernyataan owner: "Saya menyetujui rekomendasi D-26, D-27, D-28, D-29, D-30, D-31, D-32, D-33, D-34, D-35."

| Keputusan | Pertanyaan | Disetujui | AC terdampak |
|---|---|---|---|
| D-28 | OP-8-Q1 | XI-1–XI-9 (komponen sebagai identitas dinilai; pelajaran/latihan beridentitas sendiri; revisi dan identitas pensiun) | ASM:X-07 (identitas, revisi) |
| D-28 | OP-8-Q2 | XE-B, XE-1–XE-6 (award pertama pada attempt remedial diperbolehkan; award ganda tidak) | X-07 (kelayakan) |
| D-28 | OP-8-Q3 | UG-A | X-07 |
| D-28 | OP-8-Q4 | Jumlah XP §5; level `L(n) = 50·n·(n−1)`; XL-1–XL-3 | X-07 (jumlah, level) |
| D-28 | OP-8-Q5 | ST-C, SK-1–SK-6 (minggu JST setengah terbuka; minggu berjalan tidak memutus streak; tanpa penalti XP) | X-07 (streak) |
| D-28 | OP-8-Q6 | XA-1–XA-3; tampilan penurunan pada restore M-1 | X-07 (achievement, mastery) |
| D-28 | OP-8-Q7 | Milestone `mod-wNN.passed` (50) dan `program.capstone` (100) sebagai identitas terpisah | X-07 |
| D-29 | OD-15-Q1 | XV-1–XV-6 dan RX-A (restore ditolak bila validasi menemukan kerusakan/inkonsistensi) | OD-15 (UW-33) |

Kelulusan akademik dan program tetap tidak membaca XP. D-03 dan D-17 tidak
berubah. Sisa perencanaan restore tetap di UW-33.

### 14.1 Perluasan validasi kelayakan award (OD-15-Q2) — diputuskan D-37, lihat §14.2

Satu referensi attempt yang ada **tidak** membuktikan bahwa award sah.
Usulan pemeriksaan tambahan saat pratinjau restore (perlakuan temuan tetap
RX-A):

| ID | Pemeriksaan |
|---|---|
| XV-7 | `xp_id` cocok dengan jenis identitas di katalog (pelajaran, latihan, komponen, milestone) |
| XV-8 | Versi katalog yang tercatat ada dan jumlah XP sama dengan jumlah untuk versi itu |
| XV-9 | Peristiwa pemicu ada dan berjenis benar: attempt komponen yang sama (identitas dinilai), peristiwa selesai pelajaran/latihan (identitas tidak dinilai), atau keadaan modul/gerbang (milestone) |
| XV-10 | Attempt pemicu selesai (`GRADED`/LA-2) dan skornya memenuhi kriteria (`4·e ≥ 3·m`) menurut skor yang tercatat |
| XV-11 | Attempt pemicu adalah attempt **pertama** yang memenuhi kriteria untuk identitas itu |
| XV-12 | Prasyarat milestone terpenuhi: modul `PASSED` dihitung ulang dari attempt; gerbang capstone CG-B terpenuhi dalam satu attempt |
| XV-13 | Identitas pensiun hanya sah bila ada di daftar pensiun dengan versi yang sesuai; selain itu XV-3 |
| XV-14 | Award hilang diperiksa untuk identitas dinilai **dan** tidak dinilai (butuh catatan peristiwa selesai pelajaran/latihan di data) |

~~Pertanyaan: OD-15-Q2 — setujui XV-7–XV-14 sebagai bagian validasi OD-15 dengan perlakuan RX-A? Rekomendasi: Ya.~~ *(Historis — dijawab D-37.)*

### 14.2 Keputusan owner — D-37 (2026-11-24)

Pernyataan owner (2026-11-24, prompt revisi akhir PR #25): owner secara eksplisit menyetujui D-36 (CU-6-Q13: HF-A) dan D-37 (OD-15-Q2: XV-7–XV-14 dengan RX-A).

**OD-15-Q2 → disetujui persis seperti §14.1:** XV-7 (identitas XP vs jenis
identitas katalog), XV-8 (versi katalog dan jumlah award), XV-9 (peristiwa
pemicu ada dan berjenis benar), XV-10 (attempt selesai dan skor memenuhi),
XV-11 (attempt pertama yang memenuhi), XV-12 (prasyarat milestone), XV-13
(identitas pensiun dan versinya), XV-14 (award hilang untuk identitas dinilai
dan tidak dinilai), dengan **RX-A**: restore ditolak bila validasi menemukan
kerusakan atau inkonsistensi. Tidak ada perbaikan ledger diam-diam dan tidak
ada kebijakan XP baru. D-03, D-28, D-29, XV-1–XV-6, semantik M-1/M-2, dan
persyaratan rollback tidak berubah. Sisa perencanaan restore (OD-5–OD-9,
OD-11–OD-14) tetap di UW-33. Persetujuan ini bukan verifikasi implementasi.
