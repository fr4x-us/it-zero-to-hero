---
component: mod-w06.project
content_version: "1.0"
competencies: [comp-w06-repr-01, comp-w06-bin2dec-01, comp-w06-dec2bin-01, comp-w06-ops-01, comp-w06-table-01, comp-w06-model-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W6 — Logika Alarm Rumah

## Skenario

Keluarga Pak Arif memasang alarm sederhana (fiktif) dengan tiga input:

| Input | Arti nilai 1 | Arti nilai 0 |
|---|---|---|
| `P` | Pintu terbuka | Pintu tertutup |
| `J` | Jendela terbuka | Jendela tertutup |
| `M` | Mode malam aktif | Mode malam tidak aktif |

Aturan perangkat:

- **Alarm** berbunyi bila mode malam aktif **dan** pintu terbuka **atau**
  jendela terbuka (sedikitnya satu dari keduanya).
- **Lampu kuning** menyala bila mode malam **tidak** aktif **dan** pintu
  terbuka **atau** jendela terbuka (sedikitnya satu dari keduanya).

Kamu menyusun logika perangkat ini di atas kertas, bukan merakit perangkat
nyata.

## Tujuan belajar

Menerapkan seluruh tujuan W6: representasi biner vs Boolean (LO1),
konversi biner–desimal (LO2, LO3), operator (LO4), tabel kebenaran (LO5),
dan memodelkan aturan menjadi ekspresi (LO6).

## Deliverable (formulir di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1 | Kolom **alarm** pada tabel kebenaran: baris R1–R8 untuk kombinasi P J M dari `000` sampai `111` (P paling kiri) | Satu digit 0/1 per baris |
| F2 | Ekspresi Boolean untuk **alarm** | Tata bahasa BX |
| F3 | Banyak baris (dari 8) yang membuat alarm berbunyi | Bilangan bulat |
| F4 | Ekspresi Boolean untuk **lampu kuning** | Tata bahasa BX |
| F5 | Kombinasi P = 1, J = 1, M = 0 ditulis sebagai bilangan biner P J M. Berapa nilainya dalam **desimal**? | Bilangan bulat |
| F6 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Tata bahasa ekspresi BX (Pelajaran 3 §3, Pelajaran 4 §2)

- Variabel yang boleh dipakai: `P`, `J`, `M`.
- Kata kunci: `AND`, `OR`, `NOT`; kurung `( )` berpasangan.
- Prioritas: `NOT` lebih dulu, lalu `AND`, lalu `OR`; kurung dihitung
  lebih dulu.
- `NOT` berlaku untuk satu operand dan boleh berulang (`NOT NOT M` = `M`);
  `AND` dan `OR` selalu membutuhkan operand di kiri dan kanan.
- Simbol lain (`&&`, `||`, `!`, `+`, `*`), variabel lain, atau kurung yang
  tidak berpasangan membuat ekspresi **tidak dapat dibaca**.
- Bentuk terbaik: kata kunci dan variabel **huruf besar**. Huruf kecil
  tetap dibaca, tetapi kehilangan poin format.
- **Ekspresi apa pun yang bernilai sama di kedelapan baris diterima** —
  tidak ada satu tulisan "resmi".

## Contoh bentuk isian (bukan jawaban proyek)

Contoh memakai aturan **lain**: "kipas menyala bila tombol `T` ditekan
dan suhu `S` tidak panas".

| Isian | Contoh bentuk terbaik |
|---|---|
| Ekspresi | `T AND NOT S` |
| Sel tabel | `1` |
| Bilangan bulat | `4` |

## Instruksi

1. Tulis kedelapan kombinasi P J M berurutan, lalu tentukan nilai alarm di
   setiap baris dari aturan.
2. Susun ekspresi alarm dan lampu kuning; periksa dengan tabel kebenaran.
3. Hitung banyak baris alarm berbunyi.
4. Ubah kode biner P J M di F5 ke desimal.
5. Jawab lima soal penjelasan, lalu tekan **Serahkan** (dengan
   konfirmasi).

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Lupa kurung sehingga prioritas AND/OR mengubah arti aturan | Ekspresi tidak ekuivalen dengan aturan |
| Memakai `&&` atau `||` | Ekspresi tidak dapat dibaca |
| Menulis kode biner pada F5 | Nilai salah (F5 meminta desimal) |
| Menulis `benar` pada sel tabel | Sel tidak dapat dibaca |
| Menyalin ekspresi alarm ke lampu kuning | F4 salah |
| Centang "sudah selesai" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | Setiap sel F1; F2 dan F4 ekuivalen dengan aturan di 8 baris; F3; F5 |
| K2 Kelengkapan deliverable | 20 | Semua isian terisi dan dapat dibaca |
| K3 Struktur dan format | 10 | Huruf besar pada ekspresi; F3 dan F5 digit saja |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Setiap isian dinilai terhadap aturan perangkat (bukan terhadap isian kamu
yang lain). Isian yang tidak dapat dibaca membuat pemeriksaan yang
membutuhkannya bernilai 0; isian lain tetap dinilai (MR-2).

## Bukti yang dinilai

Hanya isian F1–F6 (MR-6).

## Remedial

Attempt baru boleh dimulai dari salinan isian sebelumnya (MPV-A). Attempt
lama tetap tersimpan; skor terbaik dipakai (D-12).

## Durasi

90 menit (memahami aturan 10, tabel kebenaran 25, ekspresi dan pemeriksaan
25, F3 dan F5 10, memeriksa 5, soal penjelasan 15).
