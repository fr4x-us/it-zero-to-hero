# IT ZERO → HERO — Decision Sheet: Representasi Angka dan Presisi Penilaian (UW-22)

Status: **DIPUTUSKAN OWNER — D-12 (2026-11-24)**, lihat §9 · dokumentasi saja · tanpa kode.
Verifikasi pada implementasi: **NOT VERIFIED**.
Tanggal: **2026-11-23**. Basis awal: `main` = `2114ca8` (merge PR #19);
§8 ditambahkan pada basis `6a805a1` (merge PR #20).

Lembar ini menyiapkan keputusan OP-3 / UW-22. Rekomendasi di §5 adalah
saran teknis, **bukan** keputusan. Aturan penilaian terkunci tidak
diubah.

## 1. Aturan yang harus dipenuhi (sudah disetujui)

| ID | Aturan | Sumber |
|---|---|---|
| N-R1 | Bobot: Theory 30%, Laboratory 40%, Mini-project 20%, Concept explanation 10% | BL:27–30 |
| N-R2 | Lulus modul bila nilai tertimbang ≥ 80 **dan** setiap komponen ≥ 75 | BL:31–32, D-04 |
| N-R3 | Tidak ada pembulatan sebelum keputusan lulus; pembulatan hanya untuk tampilan | TD:21, TD:30, D-04 |
| N-R4 | Skor terbaik per komponen; semua attempt disimpan | BL:34, D-04 |
| N-R5 | Hasil harus sama setiap kali dihitung ulang (setelah restart, migrasi, restore, di perangkat lain) | ASM:P-08, BKP:I-03 |
| N-R6 | Kasus batas ASM:B-01–ASM:B-10 harus menghasilkan keputusan yang benar | [`ASSESSMENT_STATE_MACHINE_SPEC.md`](ASSESSMENT_STATE_MACHINE_SPEC.md) §6.3 |

## 2. Fakta penting: skor komponen belum tentu desimal berhingga

Cara skor komponen dihasilkan (poin soal, bobot test case lab, nilai
parsial penjelasan konsep) masih **OPEN** (OP-4, CU-6). Bila skor adalah
rasio poin, misalnya 7 dari 9 poin, nilainya 700/9 = 77,777… — tidak
berhingga dalam desimal. Representasi yang memotong angka ini sudah
melakukan **pembulatan sebelum keputusan lulus**, yang dilarang N-R3.

## 3. Bukti hitungan (bukan uji aplikasi)

Dihitung 2026-11-23 dengan Python (`float` IEEE 754 double dan
`fractions.Fraction` eksak). Ini hanya ilustrasi aritmetika, bukan hasil
uji aplikasi.

| Kasus | Rumus float naif `0.3T+0.4L+0.2P+0.1C` | Nilai eksak | Keputusan float | Keputusan eksak |
|---|---|---|---|---|
| ASM:B-01 (80/80/80/80) | 80.0 | 80 | Lulus | Lulus |
| ASM:B-03 (75/85/80/75) | 80.0 | 80 | Lulus | Lulus |
| ASM:B-07 (79,97/80/80/80) | 79.991 | 79,991 | Belum lulus | Belum lulus |
| ASM:B-08 (100/100/100/74,999) | 97.4999 | 97,4999 | Belum lulus (komponen) | Belum lulus (komponen) |
| **77/75/88/93** (bukan bagian ASM:B) | **79.99999999999999** | **80** | **Belum lulus — SALAH** | Lulus |

Pencarian menyeluruh atas semua kombinasi skor bilangan bulat 75–100 per
komponen menemukan **19 kombinasi** yang diputuskan salah oleh rumus float
naif (semuanya bernilai tepat 80 secara eksak tetapi terhitung
79,99999999999999). Contoh: 77/75/88/93, 77/75/89/91, 77/75/93/83,
77/75/94/81, 77/80/78/93.

## 4. Perbandingan opsi

| Kriteria | NP-1 Integer berskala (fixed-point) | NP-2 Decimal (`BigDecimal`) | NP-3 Floating-point + pengaman batas | NP-4 Integer rasional (poin mentah) |
|---|---|---|---|---|
| Cara kerja | Skor disimpan sebagai bilangan bulat berskala tetap, mis. 1/100 poin persen (77,77 → 7777) | Desimal berbasis-10 dengan skala/`MathContext` | `Double` + toleransi (epsilon) atau penyesuaian di batas | Simpan poin diperoleh dan poin maksimum (bilangan bulat) per attempt; bandingkan dengan perkalian silang bilangan bulat |
| Ambang 75 dan 80 eksak | Ya, **bila** skor memang berada di grid skala | Ya untuk desimal berhingga; pembagian seperti 7/9 butuh mode pembulatan | Tidak dijamin; bergantung epsilon | Ya, selalu |
| Bobot 30/40/20/10 | `30t + 40l + 20p + 10c ≥ 800000` (skala 1/100), tanpa pembagian | Eksak untuk desimal berhingga | Bisa salah (19 kasus di §3) | `Σ wᵢ·eᵢ/mᵢ ≥ 0,8` diubah menjadi pertidaksamaan bilangan bulat |
| Skor terbaik per komponen | Perbandingan bilangan bulat | `compareTo` | Rawan tie palsu | Perkalian silang `e₁·m₂ ? e₂·m₁` |
| Tanpa pembulatan sebelum lulus (N-R3) | **Melanggar** bila skor asli tidak di grid (7/9) — harus dibulatkan saat disimpan | **Melanggar** untuk pembagian tak berhingga kecuali disimpan sebagai pecahan | **Melanggar** secara inheren (representasi biner) | **Memenuhi** |
| Persistensi Room | `INTEGER` | `TEXT` (string desimal) atau skala ke `INTEGER` | `REAL` | Dua kolom `INTEGER` per komponen per attempt |
| Repeatability lintas perangkat | Ya | Ya, bila `MathContext` tetap | Umumnya ya, tetapi keputusan batas rapuh | Ya |
| Risiko overflow | Rendah (`Long`) | Tidak ada | Tidak ada | Rendah bila poin maksimum dibatasi. **Koreksi (verifikasi 2026-11-23):** contoh semula "poin ≤ 10⁶" salah — perbandingan silang empat komponen butuh hingga 100·M⁴, sehingga dengan `Long` batas aman M ≤ 17.426 poin per komponen; lihat §8 |
| Kompleksitas | Rendah | Sedang | Rendah, tetapi pengaman batas sulit dibuktikan | Sedang (fungsi pembanding rasional + test) |
| Tampilan | Bagi skala, bulatkan untuk UI | Format desimal | Format | Hitung desimal hanya untuk tampilan |

## 5. Rekomendasi (saran, bukan keputusan)

**NP-4 — integer rasional dengan poin mentah**, dengan alasan:

1. Satu-satunya opsi yang memenuhi N-R3 apa pun cara skor komponen
   dihasilkan (termasuk rasio seperti 7/9).
2. Ambang 75 dan 80 dibandingkan secara eksak tanpa epsilon.
3. Data asli (poin) tetap tersimpan, sehingga perubahan rumus tampilan
   tidak mengubah keputusan lama (N-R5).
4. Kasus 77/75/88/93 dan seluruh ASM:B-01–ASM:B-10 diputuskan benar.

Alternatif bila owner menetapkan bahwa **setiap skor komponen didefinisikan
pada grid tetap** (mis. persen bulat atau kelipatan 0,01): NP-1 setara
eksak dan lebih sederhana. Keputusan ini bergantung pada OP-4 dan CU-6.

NP-3 **tidak** direkomendasikan karena §3 menunjukkan kesalahan nyata pada
nilai tepat 80.

## 6. Kriteria penerimaan bila opsi dipilih (untuk implementasi nanti)

| ID | Kriteria |
|---|---|
| NA-1 | ASM:B-01–ASM:B-10 menghasilkan keputusan sesuai tabel ASM §6.3 |
| NA-2 | Seluruh 19 kombinasi di §3 dinyatakan lulus (nilai eksak 80) |
| NA-3 | Komponen bernilai tepat 75 memenuhi ambang; 74,999… tidak |
| NA-4 | Skor terbaik dipilih dengan perbandingan eksak; tie diputuskan konsisten (aturan tie: OPEN, OP-3) |
| NA-5 | Keputusan identik setelah restart, migrasi, backup/restore |
| NA-6 | Nilai yang ditampilkan dibulatkan hanya di lapisan UI; pembulatan tidak pernah dipakai untuk keputusan |

Kriteria ini **NOT VERIFIED** — belum ada implementasi.

## 7. Yang masih OPEN

| ID | Butir |
|---|---|
| NP-O1 | Pilihan opsi (NP-1–NP-4) — keputusan owner (UW-22) |
| NP-O2 | Cara skor komponen dihasilkan: poin per soal, bobot test case, nilai parsial (OP-4, CU-6) |
| NP-O3 | Aturan tie antar-attempt dengan skor sama (mis. attempt paling awal) |
| NP-O4 | Presisi tampilan (berapa digit desimal) |
| NP-O5 | Agregasi numerik tingkat program (D-04 menyatakan OPEN; tidak ada rata-rata baru) |

## 8. Permintaan keputusan owner — UW-22 (2026-11-23)

### 8.1 Verifikasi ulang (hitungan, bukan uji aplikasi)

| Pemeriksaan | Hasil |
|---|---|
| Aturan NP-1: `W ≥ 80 ⇔ 30t + 40l + 20p + 10c ≥ 800000` untuk skor berskala 1/100 (`t = T × 100`) | Benar: `W = (30t + 40l + 20p + 10c) / 10000` |
| Aturan NP-4 vs aritmetika pecahan eksak | 200.000 kombinasi acak (poin maksimum 1–50 per komponen): **0** perbedaan keputusan |
| 19 kombinasi float naif di §3 | Semuanya bernilai eksak `30T+40L+20P+10C = 8000` (tepat 80) |
| Batas overflow NP-4 dengan `Long` (2⁶³ − 1) | Ruas kiri terburuk = 100·M⁴; aman untuk M ≤ **17.426** poin maksimum per komponen. Contoh "≤ 10⁶" di §4 dikoreksi |

### 8.2 Rincian NP-4 yang diusulkan (PROPOSED)

| Aspek | Usulan |
|---|---|
| Representasi skor mentah | Setiap attempt per komponen menyimpan dua bilangan bulat: `earned` (0 ≤ earned ≤ max) dan `max` (> 0). Tidak menyimpan persen sebagai sumber kebenaran |
| Ambang komponen | `komponen ≥ 75 ⇔ 4·earned ≥ 3·max` |
| Ambang tertimbang | Dengan `D = m_T·m_L·m_P·m_C`: `30·e_T·(D/m_T) + 40·e_L·(D/m_L) + 20·e_P·(D/m_P) + 10·e_C·(D/m_C) ≥ 80·D` |
| Pengaman overflow | (1) Batas tertulis `max ≤ 10.000` per komponen per attempt (di bawah 17.426, dengan margin); (2) perkalian memakai operasi yang gagal eksplisit bila overflow (mis. `Math.multiplyExact`), atau `BigInteger` sebagai cadangan. Pilihan teknis final saat implementasi |
| Skor terbaik per komponen | Bandingkan `e₁·m₂` dengan `e₂·m₁` |
| Tie (skor sama) | Usulan: pilih attempt **paling awal** yang mencapai skor terbaik, agar hasil stabil dan tidak berubah oleh remedial berskor sama. Keputusan owner (NP-O3) |
| Presisi tampilan | Usulan: tampilkan 2 desimal **dibulatkan ke bawah** (mis. 79,991 → "79,99"; 74,999 → "74,99"; 80 → "80,00"), selalu disertai status teks lulus/belum lulus. Pembulatan ke bawah mencegah angka tampil memenuhi ambang padahal belum. Keputusan owner (NP-O4) |
| Ketergantungan | OP-4 (cara nilai parsial penjelasan konsep) dan CU-6 / CUR §5 (bobot test case lab) menentukan nilai `earned`/`max`; agregasi beberapa aktivitas dalam satu komponen per modul belum diputuskan (lihat [CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md](CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md)) |

### 8.3 Pertanyaan untuk owner

1. **UW-22-Q1:** Setujui NP-4 (integer rasional dari poin mentah) sebagai representasi skor? (Alternatif: NP-1 bila semua skor didefinisikan pada grid 0,01.)
2. **UW-22-Q2:** Setujui batas `max ≤ 10.000` poin per komponen per attempt?
3. **UW-22-Q3:** Tie skor sama: pilih attempt paling awal?
4. **UW-22-Q4:** Tampilan: 2 desimal dibulatkan ke bawah + status teks?

Status: **AWAITING OWNER**. UW-22 tetap **OPEN/BLOCKED** sampai dijawab.

## 9. Keputusan owner — D-12 (2026-11-24)

| Butir | Keputusan |
|---|---|
| UW-22-Q1 | **NP-4** disetujui: integer rasional eksak dari poin mentah `earned`/`max` |
| UW-22-Q2 | Maksimum **10.000** poin per komponen per attempt |
| UW-22-Q3 | Skor terbaik sama → **attempt paling awal**; semua attempt disimpan |
| UW-22-Q4 | Tampilan **2 desimal dibulatkan ke bawah** + status lulus/belum lulus eksplisit |

Tetap berlaku: komponen ≥ 75 dan nilai tertimbang ≥ 80 dibandingkan
secara eksak; tanpa pembulatan sebelum keputusan akademik; aritmetika
*checked* mencegah overflow; pembulatan tampilan tidak memengaruhi hasil.

Ketergantungan yang tersisa (tidak diputuskan di sini): OP-4 (nilai parsial
penjelasan konsep), CU-6 (bobot test case lab), alokasi poin per aktivitas
(D-13 menjumlahkan poin aktivitas dalam satu komponen), dan pilihan teknis
aritmetika *checked* saat implementasi. NA-1–NA-6 (§6) tetap
**NOT VERIFIED** sampai implementasi diizinkan dan diuji (UW-56).
