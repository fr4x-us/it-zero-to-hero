---
lesson_id: mod-w08.les-04
practice_id: mod-w08.prac-04
module_id: mod-w08
content_version: "1.0"
title: "Kebenaran Algoritma dan Kasus Batas"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w08-correct-01, comp-w08-trace-01]
prerequisites: [mod-w08.les-03]
accessibility:
  diagrams:
    - id: dg-w08-04
      alt: "Tabel daftar kasus uji untuk algoritma daftar."
      long_description: >
        Lima baris kasus uji: satu nilai, semua positif, semua negatif,
        ada nilai sama, nilai penting di posisi terakhir. Setiap baris
        punya kolom alasan.
  tables_with_core_data: ["Tabel nilai awal", "Tabel kasus uji daftar", "Tabel penelusuran algoritma terkecil"]
  english_terms: [correctness, initial value, neutral element, edge case, duplicate values, negative values, first occurrence, last occurrence]
---

# Pelajaran 4 — Kebenaran Algoritma dan Kasus Batas

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Memilih **nilai awal** yang benar untuk akumulator dan pembanding.
2. Menjelaskan pengaruh **nilai sama** (`<` vs `≤`) dan **nilai negatif**.
3. Memilih **kasus uji** yang mengungkap kesalahan algoritma daftar.

## Mengapa ini penting?

Algoritma yang benar untuk contoh yang dicoba belum tentu benar untuk semua
input dalam domainnya. Kesalahan paling sering terjadi pada nilai awal,
nilai sama, nilai negatif, dan ujung daftar.

## 1. Nilai awal

| Tujuan | Nilai awal | Alasan |
|---|---|---|
| Menjumlahkan | `0` | 0 + x = x (tidak menambah apa-apa) |
| Menghitung banyak (penghitung) | `0` | Belum ada yang dihitung |
| Mengalikan | `1` | 1 × x = x |
| Mencari nilai terkecil | **nilai pertama daftar** `A[1]` | Selalu anggota daftar; **syarat**: daftar tidak kosong (n ≥ 1) |

Mengapa bukan angka "besar" atau 0 untuk nilai terkecil? Untuk daftar
`[12, 30, 18]`, nilai awal 0 membuat tidak ada nilai yang lebih kecil, dan
output 0 — padahal 0 bukan anggota daftar. Nilai awal dari daftar sendiri
selalu aman, asalkan daftar tidak kosong.

## 2. Algoritma nilai terkecil (domain: daftar berisi n ≥ 1 nilai)

| Blok | Isi |
|---|---|
| 1 | `kecil ← A[1]`; `i ← 2` |
| 2 | selama `i ≤ n`: |
| 3 | jika `A[i] < kecil`: `kecil ← A[i]` |
| 4 | `i ← i + 1` |
| 5 | Output kecil |

Telusuri A = `[−1, 6, −4, 2]`:

| i | A[i] | `A[i] < kecil?` | kecil |
|---|---|---|---|
| (awal) | | | −1 |
| 2 | 6 | Tidak | −1 |
| 3 | −4 | Ya | −4 |
| 4 | 2 | Tidak | −4 |

Output −4. Bilangan negatif dibandingkan seperti biasa (−4 < −1).

## 3. Nilai sama: `<` atau `≤`

Bila nilai terkecil muncul dua kali, `<` dan `≤` memberi **nilai** output
yang sama, tetapi berbeda dalam **berapa kali** nilai diganti dan
**posisi** mana yang tercatat bila algoritma menyimpan posisi:

- `<`: posisi **pertama** dari nilai yang sama tetap dipakai.
- `≤`: posisi **terakhir** yang dipakai.

Bila yang diminta hanya nilainya, keduanya benar. Bila yang diminta posisi
pertama, hanya `<` yang benar. Soal harus menyatakan mana yang diminta.

## 4. Kasus uji untuk algoritma daftar

*Deskripsi diagram dg-w08-04:* lima jenis kasus uji.

| Kasus | Contoh | Mengungkap |
|---|---|---|
| Satu nilai | `[4]` | Perulangan yang tidak boleh berjalan |
| Semua positif | `[12, 30, 18]` | Nilai awal 0 untuk nilai terkecil |
| Semua negatif | `[−6, −2, −9]` | Nilai awal 0 untuk nilai **terbesar** |
| Ada nilai sama | `[3, 1, 1]` | Pilihan `<` vs `≤` |
| Nilai penting di akhir | `[8, 6, 2]` | Syarat perulangan yang melewatkan A[n] |

Satu kasus uji yang lolos tidak membuktikan algoritma benar; kumpulan kasus
yang dipilih dengan alasan membuat kesalahan umum terungkap.

## 5. Contoh terbimbing

**Soal:** Seseorang menulis syarat perulangan `i < n` pada algoritma
nilai terkecil. Pilih kasus uji yang mengungkapnya.

1. Dengan `i < n`, A[n] tidak pernah dibandingkan.
2. Kasus `[8, 6, 2]`: algoritma salah memberi 6; seharusnya 2.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Nilai awal 0 selalu aman" | Aman untuk menjumlahkan dan menghitung banyak; tidak untuk perkalian atau pembanding (terkecil/terbesar) |
| "Bilangan negatif perlu aturan khusus" | Dibandingkan seperti biasa |
| "`<` dan `≤` selalu sama saja" | Sama untuk nilai, bisa beda untuk posisi/jumlah penggantian |
| "Daftar contoh di soal cukup untuk menguji" | Pilih kasus uji yang mengincar kesalahan umum |

## 7. Latihan terbimbing (`mod-w08.prac-04`, tidak dinilai)

1. Nilai awal untuk menghitung **banyak** nilai genap?
2. Telusuri algoritma nilai terkecil untuk `[5, 5, 3]` dengan `<`: berapa
   kali `kecil` diganti?
3. Algoritma **mengalikan** daftar memakai `hasil ← 0`. Kasus uji mana yang
   mengungkap kesalahannya: `[0, 4]` atau `[2, 3]`?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa "nilai pertama daftar" selalu aman sebagai nilai awal pembanding?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 0 (penghitung dimulai dari nol).
2. Sekali (di i = 3: 3 < 5); di i = 2, 5 < 5 salah.
3. `[2, 3]`: output 0 padahal hasil kali 6. `[0, 4]` lolos (hasil kali
   memang 0) — kasus uji yang lolos tidak membuktikan algoritma benar.

Cek pemahaman: nilai itu anggota daftar, jadi tidak pernah memberi output
yang tidak ada di daftar.

## Ringkasan

- Nilai awal: 0 untuk jumlah dan penghitung, 1 untuk perkalian, nilai
  pertama untuk pembanding (daftar tidak kosong).
- Nilai sama: `<` posisi pertama, `≤` posisi terakhir; nilai sama.
- Uji: satu nilai, semua positif, semua negatif, nilai sama, nilai di akhir.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Nilai awal | initial value | Nilai variabel sebelum perulangan |
| Kasus tepi | edge case | Input di ujung domain yang mudah membuat salah |
| Kemunculan pertama | first occurrence | Posisi paling awal nilai yang sama |
| Kebenaran | correctness | Algoritma benar untuk semua input dalam domain |
