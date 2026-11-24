---
lesson_id: mod-w08.les-01
practice_id: mod-w08.prac-01
module_id: mod-w08
content_version: "1.0"
title: "Algoritma: Input, Proses, Output, dan Domain"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w08-algo-01]
prerequisites: [mod-w07]
accessibility:
  diagrams:
    - id: dg-w08-01
      alt: "Tiga kotak input, proses, output."
      long_description: >
        Kotak kiri berlabel input berisi jarak dan kecepatan. Panah ke kotak
        tengah berlabel proses berisi waktu ← jarak ÷ kecepatan. Panah ke
        kotak kanan berlabel output berisi waktu.
  tables_with_core_data: ["Tabel input-proses-output", "Tabel notasi langkah", "Tabel domain input"]
  english_terms: [algorithm, input, process, output, assignment, domain, assumption, termination, pseudocode]
---

# Pelajaran 1 — Algoritma: Input, Proses, Output, dan Domain

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan algoritma sebagai **input → proses → output** yang
   **berhenti**.
2. Membaca notasi langkah `←` (pemberian nilai) dan perbandingan.
3. Menyatakan **domain input** (asumsi) agar setiap langkah dapat
   dikerjakan.

## Mengapa ini penting?

W7 mengajarkan langkah yang jelas. W8 menuliskannya dengan cara yang
dipakai programmer sebelum menulis kode: langkah bernotasi dan flowchart.
Mulai W9 langkah-langkah ini akan ditulis sebagai program Python.

## 1. Input, proses, output

*Deskripsi diagram dg-w08-01:* input jarak dan kecepatan → proses `waktu ←
jarak ÷ kecepatan` → output waktu.

| Bagian | Arti | Contoh "hitung keliling persegi" |
|---|---|---|
| **Input** | Data yang diberikan | sisi `s` |
| **Proses** | Langkah pengolahan | `keliling ← 4 × s` |
| **Output** | Hasil yang diberikan | keliling |

Algoritma harus **berhenti** setelah sejumlah langkah berhingga dan setiap
langkahnya **jelas** (W7).

## 2. Notasi langkah

| Notasi | Arti | Contoh |
|---|---|---|
| `x ← 5` | Beri x nilai 5 (nilai lama diganti) | |
| `x ← x + 1` | Nilai x yang baru = nilai x lama + 1 | x = 3 → x = 4 |
| `=`, `<`, `>`, `≤`, `≥` | Perbandingan (hasilnya benar/salah, W6) | `x ≤ 10?` |
| `A[i]` | Nilai ke-i dari daftar A (mulai 1) | A = [6, 1, 8]: A[2] = 1 |

`x ← x + 1` bukan persamaan matematika yang "salah"; ia perintah: ambil
nilai x sekarang, tambah 1, simpan lagi di x.

## 3. Domain input dan asumsi

**Domain** = himpunan input yang boleh diberikan agar algoritma bekerja
benar. Domain harus ditulis bersama algoritma.

| Algoritma | Masalah bila domain tidak dinyatakan | Domain yang tepat |
|---|---|---|
| `waktu ← jarak ÷ kecepatan` | kecepatan = 0 → pembagian tidak terdefinisi | kecepatan > 0 |
| Hari ke-n dalam minggu (W5) | n negatif membingungkan | n bilangan bulat ≥ 0 |
| Nilai pertama daftar `A[1]` | Daftar kosong tidak punya A[1] | daftar berisi n ≥ 1 nilai |

Input di luar domain tidak dijamin menghasilkan output yang bermakna. Di
aplikasi nyata input seperti itu ditolak atau ditangani tersendiri.

## 4. Contoh terbimbing

**Soal:** Tulis algoritma "rata-rata tiga nilai" dengan input, proses,
output, dan domain.

1. Input: a, b, c (bilangan).
2. Proses: `jumlah ← a + b + c`; `r ← jumlah ÷ 3`.
3. Output: r.
4. Domain: a, b, c bilangan apa pun (pembaginya 3, tidak pernah 0).

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "`x ← x + 1` mustahil" | Itu perintah pemberian nilai, bukan persamaan |
| "Domain tidak perlu ditulis" | Tanpa domain, sebagian input membuat langkah gagal |
| "Output sama dengan proses" | Output adalah hasil yang diberikan ke pengguna |
| "A[1] adalah nilai kedua" | Di W8 penomoran daftar mulai 1 |

## 6. Latihan terbimbing (`mod-w08.prac-01`, tidak dinilai)

1. Tentukan input, proses, output untuk "ubah suhu Celsius ke Fahrenheit
   dengan `F ← C × 9 ÷ 5 + 32`".
2. x = 7. Setelah `x ← x × 2` lalu `x ← x − 3`, berapa x?
3. Algoritma `bagian ← kue ÷ orang`. Tulis domain untuk `orang`.

## 7. Cek pemahaman (tidak dinilai)

- Mengapa algoritma yang tidak pernah berhenti tidak dapat memberi output?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Input C; proses `F ← C × 9 ÷ 5 + 32`; output F.
2. 14, lalu 11.
3. `orang` bilangan bulat ≥ 1.

Cek pemahaman: output diberikan setelah langkah selesai; bila tidak pernah
selesai, output tidak pernah muncul.

## Ringkasan

- Algoritma: input → proses → output, berhenti, langkah jelas.
- `←` memberi nilai; perbandingan menghasilkan benar/salah.
- Tulis domain input bersama algoritma.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Input | input | Data yang diberikan ke algoritma |
| Output | output | Hasil algoritma |
| Pemberian nilai | assignment | Menyimpan nilai ke variabel (`←`) |
| Domain | domain | Himpunan input yang boleh diberikan |
| Berhenti | terminate | Selesai setelah langkah berhingga |
