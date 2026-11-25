---
lesson_id: mod-w06.les-04
practice_id: mod-w06.prac-04
module_id: mod-w06
content_version: "1.0"
title: "Dari Aturan ke Ekspresi Boolean"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w06-model-01, comp-w06-table-01]
prerequisites: [mod-w06.les-03]
accessibility:
  diagrams:
    - id: dg-w06-04
      alt: "Tiga langkah dari kalimat aturan ke ekspresi yang diperiksa."
      long_description: >
        Tiga kotak berpanah dari kiri ke kanan. Kotak 1: tentukan variabel
        dan arti nilai 1. Kotak 2: terjemahkan kata dan, atau, tidak menjadi
        AND, OR, NOT, lalu tambahkan kurung sesuai pengelompokan kalimat.
        Kotak 3: periksa dengan tabel kebenaran lengkap.
  tables_with_core_data: ["Tabel kata → operator", "Tabel kebenaran pemeriksaan ekuivalensi"]
  english_terms: [modeling, condition, inclusive or, equivalent expressions, grouping, verification]
---

# Pelajaran 4 — Dari Aturan ke Ekspresi Boolean

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menentukan **variabel** dan arti nilai 1 dari sebuah aturan.
2. Menerjemahkan kata **dan**, **atau**, **tidak** menjadi `AND`, `OR`,
   `NOT`, dengan **kurung** yang sesuai.
3. Memeriksa apakah dua ekspresi **ekuivalen** dengan tabel kebenaran.

## Mengapa ini penting?

Programmer sering menerima aturan dalam bahasa sehari-hari ("diskon untuk
anggota atau pembelian di atas Rp100.000"). Menerjemahkannya dengan tepat —
termasuk pengelompokan — mencegah sistem bekerja di keadaan yang salah.

## 1. Tiga langkah memodelkan

*Deskripsi diagram dg-w06-04:* variabel → terjemahan dan kurung → periksa
dengan tabel.

1. **Variabel:** beri nama setiap kondisi dan tulis arti nilai 1.
   Contoh: `K` = tanah kering (1), `H` = sedang hujan (1).
2. **Terjemahan:**

| Kata dalam aturan | Operator | Catatan |
|---|---|---|
| dan, sekaligus, keduanya | `AND` | Semua kondisi harus 1 |
| atau, salah satu, sedikitnya satu | `OR` | Termasuk bila keduanya 1 (OR inklusif) |
| tidak, bukan, tanpa | `NOT` | Membalik kondisi |

3. **Periksa** dengan tabel kebenaran: apakah hasilnya sesuai aturan di
   setiap baris?

**Contoh.** "Penyiram menyala bila tanah kering **dan tidak** sedang
hujan": `K AND NOT H`.

| K | H | NOT H | K AND NOT H | Sesuai aturan? |
|---|---|---|---|---|
| 0 | 0 | 1 | 0 | Tanah basah → mati ✓ |
| 0 | 1 | 0 | 0 | ✓ |
| 1 | 0 | 1 | 1 | Kering, tidak hujan → menyala ✓ |
| 1 | 1 | 0 | 0 | Hujan → mati ✓ |

## 2. Pengelompokan dan kurung

Kalimat sering mengelompokkan kondisi. Kurung menuliskan kelompok itu.

"Komputer lab boleh dipakai bila (siswa **terdaftar** dan **ada guru**)
**atau** pemakainya **asisten lab**": `(T AND G) OR A`.

Karena AND dikerjakan sebelum OR, `T AND G OR A` dibaca sama. Tetapi
`T AND (G OR A)` berarti lain: asisten lab yang **tidak** terdaftar sebagai
siswa ditolak. Periksa baris T = 0, G = 0, A = 1:

| Ekspresi | Hasil pada T = 0, G = 0, A = 1 |
|---|---|
| `(T AND G) OR A` | 1 (boleh) |
| `T AND (G OR A)` | 0 (ditolak) |

Satu baris yang berbeda sudah cukup untuk menunjukkan dua ekspresi **tidak**
ekuivalen. Untuk menunjukkan **ekuivalen**, semua baris harus sama.

## 3. Ekspresi ekuivalen

Dua ekspresi **ekuivalen** bila bernilai sama pada **semua** kombinasi
input. Contoh: `X OR (NOT X AND Y)` dan `X OR Y`.

| X | Y | NOT X AND Y | X OR (NOT X AND Y) | X OR Y |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 |

Kolom keempat dan kelima sama di keempat baris → ekuivalen. Jadi sebuah
aturan dapat ditulis dengan beberapa ekspresi yang sama-sama benar; urutan
operand juga tidak berpengaruh (`X AND Y` ekuivalen dengan `Y AND X`).

*Catatan:* NOT di depan kurung tidak boleh "dibagikan" begitu saja ke
setiap variabel. Ada aturan umum untuknya (hukum De Morgan, dipelajari
lebih lanjut kelak); di W6 selalu periksa dengan tabel kebenaran.

## 4. Contoh terbimbing

**Soal:** "Pintu garasi terbuka bila tombol remote ditekan (R) **dan tidak**
ada halangan (S), **atau** bila tombol darurat ditekan (D)."

1. Variabel: R, S, D (1 = ditekan/ada).
2. "R dan tidak S" adalah satu kelompok; "atau D" berdiri sendiri:
   `(R AND NOT S) OR D`.
3. Periksa baris R = 1, S = 1, D = 0: (1 AND 0) OR 0 = 0 → tertutup ✓.
   Baris R = 0, S = 1, D = 1: 0 OR 1 = 1 → terbuka (tombol darurat) ✓.

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Atau berarti hanya salah satu" | Dalam W6, atau = OR inklusif |
| "Hanya ada satu ekspresi yang benar" | Semua ekspresi ekuivalen sama-sama benar |
| "Kurung hanya hiasan" | Kurung dapat mengubah arti |
| "`NOT (X OR Y)` sama dengan `NOT X OR NOT Y`" | Tidak ekuivalen: berbeda pada X = 1, Y = 0 (0 vs 1) dan X = 0, Y = 1; selalu periksa semua baris tabel |

## 6. Latihan terbimbing (`mod-w06.prac-04`, tidak dinilai)

1. "Lampu baca menyala bila saklar (S) hidup **dan** bohlam (B) baik."
2. "Ujian dapat dimulai bila peserta hadir (H) **atau** mendapat izin
   susulan (I)."
3. Apakah `X AND (Y OR X)` ekuivalen dengan `X`? Periksa empat baris.
4. Tunjukkan satu baris yang membedakan `X OR Y AND Z` dan
   `(X OR Y) AND Z`.

## 7. Cek pemahaman (tidak dinilai)

- Mengapa satu baris berbeda cukup untuk menunjukkan **tidak** ekuivalen,
  tetapi satu baris sama **tidak** cukup untuk menunjukkan ekuivalen?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. `S AND B`.
2. `H OR I`.
3. Ya: X = 0 → 0; X = 1 → Y OR 1 = 1, jadi hasil = X di keempat baris.
4. X = 1, Y = 0, Z = 0: `X OR (Y AND Z)` = 1, `(X OR Y) AND Z` = 0.

Cek pemahaman: ekuivalen menuntut sama di semua baris; satu pengecualian
sudah membatalkannya.

## Ringkasan

- Variabel + arti nilai 1 → terjemahan dan/atau/tidak → kurung → tabel.
- Ekspresi ekuivalen sama di semua baris; semuanya benar.
- Kurung mengubah arti; periksa, jangan menebak.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Memodelkan | modeling | Mengubah aturan menjadi ekspresi |
| OR inklusif | inclusive or | Bernilai 1 juga bila semua input 1 |
| Ekuivalen | equivalent | Sama di semua kombinasi input |
| Pengelompokan | grouping | Kondisi yang dihitung bersama, ditulis dengan kurung |
