---
lesson_id: mod-w06.les-03
practice_id: mod-w06.prac-03
module_id: mod-w06
content_version: "1.0"
title: "Operator Boolean dan Tabel Kebenaran"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w06-ops-01, comp-w06-table-01]
prerequisites: [mod-w06.les-01]
accessibility:
  diagrams:
    - id: dg-w06-03
      alt: "Tiga tabel kebenaran dasar: AND, OR, NOT."
      long_description: >
        Tabel AND dengan kolom X, Y, hasil: 0 0 0; 0 1 0; 1 0 0; 1 1 1.
        Tabel OR: 0 0 0; 0 1 1; 1 0 1; 1 1 1. Tabel NOT dengan kolom X,
        hasil: 0 1; 1 0.
    - id: dg-w06-03b
      alt: "Tabel kebenaran tiga variabel dengan kolom bantu."
      long_description: >
        Kolom X, Y, Z berisi delapan baris dari 000 sampai 111. Kolom bantu
        X AND Y, lalu kolom hasil (X AND Y) OR NOT Z. Setiap baris dihitung
        dari kiri ke kanan memakai kolom bantu.
  tables_with_core_data: ["Tabel AND/OR/NOT", "Tabel prioritas", "Tabel kebenaran contoh"]
  english_terms: [Boolean logic, AND, OR, NOT, truth table, operator precedence, parentheses, helper column]
---

# Pelajaran 3 — Operator Boolean dan Tabel Kebenaran

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menerapkan operator **AND**, **OR**, dan **NOT**.
2. Menyusun **tabel kebenaran lengkap** dengan urutan baris standar.
3. Mengevaluasi ekspresi dengan **kurung** dan **prioritas**
   NOT → AND → OR.

## Mengapa ini penting?

Setiap keputusan program ("jika sandi benar **dan** akun tidak terkunci")
adalah logika Boolean. Tabel kebenaran adalah cara paling jujur untuk
memeriksa apakah sebuah aturan bekerja di **semua** keadaan, bukan hanya di
keadaan yang kebetulan dicoba.

## 1. Nilai Boolean

Logika Boolean hanya mengenal dua nilai: **1 = benar**, **0 = salah**
(Pelajaran 1 §4). Variabel Boolean, mis. `X`, bernilai 1 atau 0.

## 2. Tiga operator dasar

*Deskripsi diagram dg-w06-03:* tabel AND, OR, NOT.

| X | Y | X AND Y | X OR Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

| X | NOT X |
|---|---|
| 0 | 1 |
| 1 | 0 |

- **AND**: 1 hanya bila **semua** input 1.
- **OR**: 1 bila **sedikitnya satu** input 1 (termasuk bila keduanya 1).
- **NOT**: membalik nilai (satu input).

*Catatan cakupan:* W6 hanya memakai AND, OR, NOT. Operator lain (mis. XOR)
tidak dinilai.

## 3. Prioritas dan kurung

Seperti urutan operasi di W5, ekspresi Boolean punya urutan:

| Tingkat | Operator |
|---|---|
| 1 | Kurung `( )` |
| 2 | `NOT` |
| 3 | `AND` |
| 4 | `OR` |

Operator setara dikerjakan dari kiri ke kanan. Contoh: `X OR Y AND Z`
dibaca `X OR (Y AND Z)`. Bila yang dimaksud `(X OR Y) AND Z`, **tulis
kurungnya**. Menulis kurung walaupun tidak wajib membuat maksud jelas.

**Tata bahasa BX** (dipakai di soal isian W6): variabel yang disebut soal,
kata `AND`, `OR`, `NOT`, dan kurung berpasangan. Simbol seperti `&&`, `||`,
atau `!` tidak dipakai di W6.

## 4. Tabel kebenaran lengkap

- Banyak baris = **2ⁿ** untuk n variabel (2 variabel: 4; 3 variabel: 8).
- Urutan standar: tulis kombinasi seperti menghitung biner dari 0 —
  `000`, `001`, `010`, … `111`. Dengan urutan ini tidak ada kombinasi yang
  terlewat atau terulang.
- Untuk ekspresi panjang, buat **kolom bantu**.

*Deskripsi diagram dg-w06-03b:* tabel `(X AND Y) OR NOT Z`.

| X | Y | Z | X AND Y | NOT Z | (X AND Y) OR NOT Z |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 1 |

Hasil bernilai 1 di 5 baris.

## 5. Contoh terbimbing

**Soal:** X = 0, Y = 1, Z = 1. Nilai `NOT X OR Y AND NOT Z`?

1. Prioritas: NOT dulu → NOT X = 1; NOT Z = 0.
2. AND berikutnya → Y AND NOT Z = 1 AND 0 = 0.
3. OR terakhir → 1 OR 0 = 1.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "OR berarti salah satu saja, tidak boleh keduanya" | OR juga 1 bila keduanya 1 |
| "Dikerjakan kiri ke kanan tanpa prioritas" | NOT → AND → OR, kecuali ada kurung |
| "Mencoba dua baris sudah cukup" | Periksa semua 2ⁿ baris |
| "1 AND 1 = 2" | Nilai Boolean: 1 AND 1 = 1 |

## 7. Latihan terbimbing (`mod-w06.prac-03`, tidak dinilai)

1. X = 1, Y = 1: `X AND NOT Y`?
2. X = 0, Y = 0, Z = 1: `X OR Y OR Z`?
3. Berapa baris tabel lengkap 5 variabel?
4. Susun tabel `X OR NOT Y`. Di baris mana bernilai 0?
5. Bagaimana `X OR Y AND Z` dibaca menurut prioritas?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa urutan baris seperti menghitung biner menjamin tidak ada
  kombinasi terlewat?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. NOT Y = 0; 1 AND 0 = 0.
2. 0 OR 0 OR 1 = 1.
3. 2⁵ = 32.
4. Hanya X = 0, Y = 1 (baris lain bernilai 1).
5. `X OR (Y AND Z)`.

Cek pemahaman: kombinasi 000 sampai 111 adalah bilangan 0 sampai 7, masing-
masing tepat sekali.

## Ringkasan

- AND: semua 1; OR: sedikitnya satu 1; NOT: membalik.
- Prioritas: kurung → NOT → AND → OR.
- Tabel lengkap: 2ⁿ baris, urutan seperti menghitung biner, kolom bantu.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Operator Boolean | Boolean operator | AND, OR, NOT |
| Tabel kebenaran | truth table | Daftar hasil ekspresi untuk setiap kombinasi input |
| Prioritas | precedence | Urutan operator dikerjakan |
| Kolom bantu | helper column | Kolom hasil antara dalam tabel kebenaran |
