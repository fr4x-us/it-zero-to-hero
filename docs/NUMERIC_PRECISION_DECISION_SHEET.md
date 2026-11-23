# IT ZERO → HERO — Decision Sheet: Representasi Angka dan Presisi Penilaian (UW-22)

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode.
Tanggal: **2026-11-23**. Basis: `main` = `2114ca8` (merge PR #19).

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
| Risiko overflow | Rendah (`Long`) | Tidak ada | Tidak ada | Rendah bila poin maksimum dibatasi; perlu batas tertulis (mis. `Long` dengan poin ≤ 10⁶) |
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
