# IT ZERO → HERO — Decision Sheet CU-10: Risiko Ekstraksi Kunci Jawaban Offline

Status: **DIPUTUSKAN OWNER — D-34 (2026-11-24)**, lihat §7 · dokumentasi saja. Tanggal:
**2026-11-24**. Basis: `main` = `928e278`. Kode rujukan: `CU10:`. Terkait
UW-25 (AC: keputusan tertulis).

Rekomendasi adalah saran, **bukan** keputusan.

## 1. Fakta

| ID | Fakta |
|---|---|
| AK-F1 | Penilaian objektif offline tanpa server (BL:38, BL:10) mengharuskan kunci jawaban, test tersembunyi, dan fixture tersedia di perangkat saat menilai |
| AK-F2 | APK adalah arsip yang dapat dibuka; aset dan resource dapat diekstrak oleh pemilik perangkat yang mahir |
| AK-F3 | Obfuscation kode (R8, UW-38) mempersulit membaca logika, tetapi **tidak** menyembunyikan data aset secara andal |
| AK-F4 | Enkripsi konten di perangkat membutuhkan kunci yang juga ada di perangkat; pemilik perangkat yang bertekad dapat memulihkannya. Ini hanya menaikkan usaha, bukan perlindungan |
| AK-F5 | Hash jawaban tidak melindungi soal dengan ruang jawaban kecil (pilihan ganda, biner pendek): semua kemungkinan dapat dicoba |
| AK-F6 | Pengguna adalah pemilik perangkat dan satu-satunya pelajar; rapor = catatan belajar mandiri, bukan sertifikat (D-17) |

**Kunci jawaban offline tidak dapat dibuat sepenuhnya tidak dapat diakses
oleh pemilik perangkat yang bertekad.**

## 2. Model ancaman (belajar mandiri pribadi)

| Pelaku | Motif | Dampak |
|---|---|---|
| Pelajar sendiri | Melewati remedial atau membuka modul lebih cepat | Merugikan belajarnya sendiri; tidak merugikan pihak lain karena tidak ada sertifikasi resmi (D-17) |
| Pihak lain yang memegang perangkat | Membaca kunci | Dampak kecil; data akademik pribadi sudah dilindungi kunci layar perangkat (di luar aplikasi) |

Batas integritas akademik: sama dengan D-17 — aplikasi tidak dapat
membuktikan bahwa nilai dicapai tanpa kecurangan; laporan bukan bukti untuk
pihak ketiga.

## 3. Opsi mitigasi V1

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| **AK-A Terima risiko + kebersihan UI** | Kunci tidak pernah ditampilkan sebelum attempt dinilai; kunci di file terpisah dari materi (CU-3); umpan balik setelah dinilai sesuai keputusan OP-5/D-24; tanpa klaim perlindungan | Jujur; tanpa kompleksitas | Ekstraksi tetap mungkin |
| AK-B Hash kunci untuk jawaban eksak | Simpan hash jawaban singkat | Mencegah membaca santai untuk ruang jawaban besar | Tidak berguna untuk pilihan ganda (AK-F5); tidak cocok untuk perbandingan multiset SQL atau kredit parsial |
| AK-C Enkripsi paket konten | Kunci di aplikasi | Mencegah penjelajahan santai | Rasa aman palsu (AK-F4); kompleksitas dan risiko kerusakan konten |
| AK-D Penilaian server | Kunci di server | Kunci tidak di perangkat | **Ditolak**: melanggar offline-first dan tanpa server wajib (BL:10, BL:38) |

## 4. Rekomendasi dan alasan

**AK-A**: terima risiko secara eksplisit, terapkan kebersihan UI, dan
nyatakan di dokumentasi pengguna bahwa nilai adalah catatan belajar mandiri
(selaras D-17). Alasan pendidikan: varian (CU-5) dan pembahasan (FB-A)
lebih bermanfaat daripada perlindungan semu. Implikasi teknis: tidak ada
mekanisme kripto tambahan; kunci dibundel apa adanya. Ketergantungan: D-17,
CU-3, CU-5, OP-5 (FB), UW-38 (R8 tidak dihitung sebagai perlindungan).

## 5. Acceptance criteria

| ID | Kriteria |
|---|---|
| CU10-AC-01 | Keputusan owner tertulis (AC UW-25) |
| CU10-AC-02 | Tidak ada dokumen yang mengklaim kunci tidak dapat diekstrak |
| CU10-AC-03 | Aturan UI "kunci tidak tampil sebelum dinilai" tercatat sebagai persyaratan |

## 6. Pertanyaan untuk owner

| ID | Pertanyaan | Rekomendasi |
|---|---|---|
| CU-10-Q1 | Terima risiko ekstraksi kunci jawaban dengan model ancaman §2 (selaras D-17)? | Ya |
| CU-10-Q2 | Mitigasi V1 AK-A (kebersihan UI, tanpa enkripsi/hash konten, tanpa klaim perlindungan)? | AK-A |

~~Status: **AWAITING OWNER**. UW-25 tetap BLOCKED.~~ *(Historis — dijawab owner 2026-11-24; lihat bagian keputusan di bawah.)*

## 7. Keputusan owner — D-34 (2026-11-24)

Pernyataan owner: "Saya menyetujui rekomendasi D-26, D-27, D-28, D-29, D-30, D-31, D-32, D-33, D-34, D-35."

CU-10-Q1 dan CU-10-Q2 disetujui: risiko ekstraksi kunci diterima dengan
model ancaman belajar mandiri (§2); mitigasi V1 = AK-A. Tidak ada klaim bahwa
kunci tidak dapat diekstrak; tanpa validasi server wajib, penilaian AI, atau
tutor AI; hasil belajar lokal bukan kompetensi tersertifikasi independen.
