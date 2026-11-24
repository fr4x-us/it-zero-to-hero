---
lesson_id: mod-w08.les-03
practice_id: mod-w08.prac-03
module_id: mod-w08
content_version: "1.0"
title: "Perulangan dan Tabel Penelusuran"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w08-loop-01, comp-w08-trace-01]
prerequisites: [mod-w08.les-02]
accessibility:
  diagrams:
    - id: dg-w08-03
      alt: "Flowchart perulangan dengan panah kembali."
      long_description: >
        Blok inisialisasi, lalu keputusan i ≤ n. Cabang Ya ke blok proses
        dan blok i ← i + 1, lalu panah kembali ke keputusan. Cabang Tidak ke
        output. Panah kembali menunjuk ke keputusan, bukan ke inisialisasi.
  tables_with_core_data: ["Tabel bagian perulangan", "Tabel penelusuran contoh"]
  english_terms: [loop, loop counter, loop condition, iteration, infinite loop, trace table, accumulator]
---

# Pelajaran 3 — Perulangan dan Tabel Penelusuran

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Mengenali bagian **perulangan**: nilai awal, syarat, isi, perubahan.
2. Menghitung banyak **putaran** dan banyak **pemeriksaan syarat**.
3. Mengenali perulangan yang **tidak pernah berhenti**.
4. Menyusun **tabel penelusuran** (*trace table*).

## Mengapa ini penting?

Pola berulang (W7) ditulis sekali lalu diulang dengan perulangan. Tabel
penelusuran adalah cara paling teliti untuk memastikan perulangan bekerja
seperti yang dimaksud.

## 1. Bagian perulangan

*Deskripsi diagram dg-w08-03:* inisialisasi → keputusan → isi → perubahan
→ kembali ke keputusan.

| Bagian | Contoh | Catatan |
|---|---|---|
| Nilai awal (sekali) | `jumlah ← 0; i ← 1` | **Sebelum** perulangan |
| Syarat | `i ≤ 3?` | Diperiksa setiap putaran |
| Isi | `jumlah ← jumlah + 5` | Dikerjakan bila syarat benar |
| Perubahan | `i ← i + 1` | Mendekatkan ke berhenti |
| Panah kembali | ke **syarat** | Bukan ke nilai awal |

Bila panah kembali ke nilai awal, nilai di-reset terus dan perulangan tidak
pernah berhenti.

## 2. Menghitung putaran dan pemeriksaan

`i ← 1`; selama `i ≤ 3`: isi; `i ← i + 1`.

| Pemeriksaan ke- | i | `i ≤ 3?` | Isi dikerjakan? |
|---|---|---|---|
| 1 | 1 | Ya | Ya |
| 2 | 2 | Ya | Ya |
| 3 | 3 | Ya | Ya |
| 4 | 4 | Tidak | Tidak (berhenti) |

Isi dikerjakan **3** kali; syarat diperiksa **4** kali (yang terakhir
bernilai Tidak). Saat berhenti, i = 4.

Bila syarat sudah salah pada pemeriksaan pertama (mis. `i ← 1` dan syarat
`i ≤ 0`), isi dikerjakan **0** kali.

## 3. Perulangan yang tidak berhenti

Perulangan berhenti hanya bila syaratnya suatu saat **salah**. Bila
perubahan menjauhkan dari berhenti (atau tidak ada perubahan), perulangan
tidak berhenti. Contoh: `j ← 10`; selama `j ≥ 1`: `j ← j + 2` — j makin
besar, `j ≥ 1` selalu benar.

## 4. Tabel penelusuran

Tulis setiap variabel sebagai kolom; satu baris per langkah atau putaran.

Algoritma: `hasil ← 0`; `k ← 1`; selama `k ≤ 3`: `hasil ← hasil + 2 × k`;
`k ← k + 1`. Output hasil.

| Putaran | k (sebelum) | hasil (sesudah) | k (sesudah) |
|---|---|---|---|
| 1 | 1 | 2 | 2 |
| 2 | 2 | 6 | 3 |
| 3 | 3 | 12 | 4 |
| — | 4 | `4 ≤ 3?` Tidak → output 12 | |

Variabel bernama `hasil` atau `jumlah` yang terus ditambah disebut
**akumulator**; nilai awalnya untuk penjumlahan adalah 0.

## 5. Contoh terbimbing

**Soal:** `a ← 5`; `b ← a + 1`; `a ← a × b`; `b ← a − b`. Isi tabel.

| Langkah | a | b |
|---|---|---|
| 1 | 5 | — |
| 2 | 5 | 6 |
| 3 | 30 | 6 |
| 4 | 30 | 24 |

Nilai lama tetap berlaku sampai diganti.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Banyak putaran = banyak pemeriksaan" | Pemeriksaan = putaran + 1 (yang terakhir Tidak) |
| "Panah kembali boleh ke nilai awal" | Ke syarat; nilai awal hanya sekali |
| "Semua variabel berubah setiap langkah" | Hanya yang diberi nilai |
| "Perulangan selalu jalan minimal sekali" | Bisa 0 kali bila syarat langsung salah |

## 7. Latihan terbimbing (`mod-w08.prac-03`, tidak dinilai)

1. `i ← 2`; selama `i ≤ 5`: tulis i; `i ← i + 1`. Berapa kali tulis i?
   Berapa kali syarat diperiksa?
2. Apakah perulangan `m ← 1`; selama `m ≠ 10`: `m ← m + 2` berhenti?
3. Telusuri: `t ← 1`; `k ← 1`; selama `k ≤ 3`: `t ← t × 2`; `k ← k + 1`.

## 8. Cek pemahaman (tidak dinilai)

- Mengapa nilai awal ditulis di luar perulangan?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 4 kali (i = 2, 3, 4, 5); syarat diperiksa 5 kali.
2. Tidak: m = 1, 3, 5, 7, 9, 11, … tidak pernah tepat 10.
3. t: 2, 4, 8; output 8 (k berakhir 4).

Cek pemahaman: bila di dalam, nilainya di-reset setiap putaran.

## Ringkasan

- Nilai awal → syarat → isi → perubahan → kembali ke syarat.
- Pemeriksaan = putaran + 1; perulangan bisa 0 kali.
- Tabel penelusuran: kolom per variabel, baris per langkah.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Perulangan | loop | Langkah yang diulang selama syarat benar |
| Putaran | iteration | Satu kali isi perulangan dikerjakan |
| Variabel pengendali | loop counter | Variabel yang menentukan kapan berhenti |
| Akumulator | accumulator | Variabel yang mengumpulkan hasil |
| Tabel penelusuran | trace table | Tabel nilai variabel langkah demi langkah |
