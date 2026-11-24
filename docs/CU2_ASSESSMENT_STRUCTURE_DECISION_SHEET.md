# IT ZERO → HERO — Decision Sheet: Struktur Komponen Penilaian per Modul (CU-2)

Status: **DIPUTUSKAN OWNER — D-13 (2026-11-24)**, lihat §8 · dokumentasi saja · tanpa kode.
Tanggal: **2026-11-23**. Basis: `main` = `6a805a1` (merge PR #20).

Rekomendasi di §5 adalah saran teknis, **bukan** keputusan. Aturan
penilaian terkunci tidak diubah.

## 1. Masalah

D-04 menetapkan bahwa **kelulusan modul** dinilai dengan nilai tertimbang
≥ 80 dan setiap komponen ≥ 75, tanpa pembulatan. Rumus tertimbang memakai
empat komponen dengan bobot tetap:

| Komponen | Bobot | Sumber |
|---|---|---|
| Theory | 30% | BL:27 |
| Laboratory | 40% | BL:28 |
| Mini-project | 20% | BL:29 |
| Concept explanation | 10% | BL:30 |

Pertanyaan CU-2: apakah **setiap** dari 16 modul wajib memiliki keempat
komponen? Dokumen kurikulum sebelumnya menyebut penempatan ujian teori dan
mini-project "per modul atau per fase" sebagai OPEN
([CURRICULUM_OFFLINE_LAB_SPEC.md](CURRICULUM_OFFLINE_LAB_SPEC.md) §2, §11).

## 2. Fakta yang membatasi pilihan

| # | Fakta | Sumber |
|---|---|---|
| F1 | Bobot 30/40/20/10 dan dua syarat lulus adalah aturan terkunci; `CLAUDE.md` melarang mengubah aturan penilaian terkunci | BL:27–32, CLAUDE.md |
| F2 | Kelulusan dinilai **per modul** dan modul berikutnya terbuka setelah modul sebelumnya lulus | D-04 |
| F3 | Bila satu komponen tidak ada, bobot tersisa tidak berjumlah 100% dan syarat "setiap komponen ≥ 75" tidak dapat dievaluasi untuk komponen itu | Aritmetika |
| F4 | Program selesai bila 16 modul lulus **dan** capstone selesai menurut rubrik yang disetujui kemudian | D-04 |
| F5 | Lab dan mini-project tanpa batas waktu; remedial tanpa batas; skor terbaik per komponen | D-01 M-05, M-08; BL:33–34 |
| F6 | Target 128 jam / 16 minggu, jadwal fleksibel | D-01 M-03 |

## 3. Opsi

### Opsi A — Setiap modul memiliki keempat komponen

Setiap modul `mod-w01`…`mod-w16` memiliki tepat satu komponen Theory,
Laboratory, Mini-project, dan Concept explanation, masing-masing dengan
attempt dan skor terbaik sendiri.

### Opsi B — Komponen boleh berbeda per modul dengan aturan kesetaraan yang disetujui

Contoh aturan kesetaraan (semuanya memerlukan persetujuan eksplisit owner):

- **B1 — Normalisasi bobot:** modul tanpa mini-project menormalkan bobot
  sisa (30/40/10 → 37,5/50/12,5).
- **B2 — Komponen bersama per fase:** satu mini-project per fase; skornya
  dipakai oleh keempat modul dalam fase itu.
- **B3 — Substitusi:** komponen yang tidak ada diganti komponen lain
  (mis. lab kedua sebagai pengganti mini-project).

## 4. Perbandingan konsekuensi

| Aspek | Opsi A | Opsi B |
|---|---|---|
| Kesesuaian dengan blueprint (F1) | Langsung: rumus dan bobot dipakai apa adanya di setiap modul | B1/B3 mengubah bobot efektif atau arti komponen → menyentuh aturan penilaian terkunci; butuh revisi blueprint yang disetujui owner. B2 mempertahankan bobot tetapi mengubah arti "per modul" |
| Kesesuaian dengan D-04 (F2) | Langsung | B2: kelulusan modul 1–3 dalam fase bisa bergantung pada mini-project yang baru dikerjakan di akhir fase → bertentangan dengan unlock linear per modul, atau butuh aturan tambahan |
| Kelulusan modul | Selalu terdefinisi | Bergantung aturan kesetaraan per modul |
| Beban kurikulum | 16 ujian teori + 16 lab + 16 mini-project + 16 tugas penjelasan konsep dalam ±8 jam/minggu → mini-project harus kecil (lingkup satu minggu) | Lebih ringan bila mini-project per fase |
| Model data | Sederhana: 4 komponen tetap per modul; attempt per (modul, komponen) | Butuh tabel aturan kesetaraan, bobot per modul, atau relasi komponen bersama |
| Remedial | Per komponen per modul; skor terbaik per komponen; tidak mengganggu modul lain | B2: remedial mini-project fase memengaruhi beberapa modul sekaligus; riwayat lebih rumit |
| Konsistensi uji | Kasus batas ASM:B-01–B-10 berlaku sama untuk semua modul | Butuh kasus batas per aturan kesetaraan |
| Capstone (F4) | Perlu ditentukan apakah capstone = mini-project modul 16, atau artefak terpisah di samping modul 16 | Sama, ditambah aturan kesetaraan modul 16 |

## 5. Rekomendasi (saran, bukan keputusan)

**Opsi A — setiap modul memiliki keempat komponen**, karena:

1. Paling konsisten dengan bobot terkunci BL:27–30 dan dengan D-04
   (kelulusan per modul + unlock linear), tanpa merevisi aturan penilaian.
2. Model data dan aturan remedial paling sederhana dan dapat diuji dengan
   kasus batas yang sama untuk semua modul.
3. Opsi B hampir selalu memerlukan revisi aturan penilaian terkunci (B1,
   B3) atau aturan tambahan untuk unlock linear (B2).

Konsekuensi yang harus diterima bila Opsi A dipilih:

- Mini-project setiap modul harus berlingkup kecil agar total beban
  tetap ±8 jam/minggu (alokasi waktu per komponen: OPEN, D-01 M-03).
- Konten untuk 64 komponen penilaian (16 × 4) harus ditulis (UW-37).

## 6. Hal yang tetap OPEN apa pun opsinya

| ID | Butir |
|---|---|
| CU2-O1 | Hubungan capstone dengan modul 16: (i) capstone = mini-project modul 16; (ii) capstone artefak terpisah dengan rubrik sendiri (D-04 menyebut "16 modul lulus **dan** capstone") |
| CU2-O2 | Bila satu komponen per modul terdiri dari beberapa aktivitas (mis. dua lab), cara menggabungkannya menjadi satu skor komponen (poin dijumlah atau rata-rata) — berkaitan dengan UW-22 (NP-4) |
| CU2-O3 | Alokasi jam per komponen per minggu (D-01 M-03) |
| CU2-O4 | Rubrik mini-project dan penjelasan konsep (OP-4, CU-9) |

## 7. Pertanyaan untuk owner

1. **CU-2-Q1:** Setujui Opsi A — setiap modul (1–16) memiliki keempat komponen dengan bobot 30/40/20/10?
2. **CU-2-Q2:** Capstone: (i) sama dengan mini-project modul 16, atau (ii) artefak terpisah?
3. **CU-2-Q3:** Bila satu komponen berisi beberapa aktivitas: poin dijumlah (sejalan dengan NP-4) atau cara lain?

Status: **AWAITING OWNER**. CU-2 (UW-36) tetap **BLOCKED**.

## 8. Keputusan owner — D-13 (2026-11-24)

| Butir | Keputusan |
|---|---|
| CU-2-Q1 | **Opsi A**: semua 16 modul memiliki Theory 30%, Laboratory 40%, Mini-project 20%, Concept explanation 10% |
| CU-2-Q2 | **Capstone = mini-project modul 16**, dengan rubrik capstone khusus; tidak menjadi proyek wajib tambahan di luar 128 jam |
| CU-2-Q3 | Beberapa aktivitas bernilai dalam satu komponen: **jumlahkan** poin diperoleh dan poin maksimum |

Dipertahankan: 16 modul dan 128 jam; unlock linear; remedial tanpa batas;
skor terbaik per komponen; riwayat attempt lengkap; XP sekali per aktivitas
unik yang memenuhi syarat.

CU2-O1 dan CU2-O2 (§6) **terjawab** oleh Q2 dan Q3. Tetap OPEN: CU2-O3
(alokasi jam per komponen), CU2-O4 (rubrik mini-project, penjelasan konsep,
dan rubrik capstone), alokasi poin per aktivitas.
