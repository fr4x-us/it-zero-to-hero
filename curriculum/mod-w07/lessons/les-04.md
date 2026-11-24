---
lesson_id: mod-w07.les-04
practice_id: mod-w07.prac-04
module_id: mod-w07
content_version: "1.0"
title: "Langkah yang Tepat dan Kasus Uji"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w07-algo-01, comp-w07-test-01]
prerequisites: [mod-w07.les-01]
accessibility:
  diagrams:
    - id: dg-w07-04
      alt: "Garis bilangan dengan batas 120."
      long_description: >
        Garis bilangan dari 115 sampai 125 dengan titik tebal di 120. Di kiri
        berlabel tidak boleh, di 120 dan kanannya berlabel boleh. Panah
        menunjuk 119 dan 120 sebagai kasus uji batas.
  tables_with_core_data: ["Tabel ciri algoritma", "Tabel kasus uji", "Tabel tanda perbandingan"]
  english_terms: [algorithm, precise instruction, ambiguity, termination, trace, test case, expected output, boundary test]
---

# Pelajaran 4 — Langkah yang Tepat dan Kasus Uji

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menyebut ciri **algoritma**: jelas, berurutan, berakhir.
2. Menemukan langkah **ambigu** dan memperbaikinya.
3. **Menelusuri** langkah dan memakai **kasus uji**, termasuk **kasus
   batas**, untuk mengungkap kesalahan.

## Mengapa ini penting?

Komputer tidak dapat menebak maksud. "Masak sampai cukup" tidak dapat
dikerjakan mesin. Dan langkah yang tampak benar dapat gagal pada satu
masukan — kasus uji menemukannya sebelum pengguna menemukannya.

## 1. Ciri algoritma

| Ciri | Contoh buruk | Contoh baik |
|---|---|---|
| **Jelas/terukur** | "Tambahkan air secukupnya" | "Tambahkan 200 mL air" |
| **Berurutan benar** | "Tempel stiker, lalu kupas kertasnya" | "Kupas kertas stiker, lalu tempel" |
| **Berakhir** | "Ulangi terus" | "Ulangi 5 kali" atau "ulangi sampai ember penuh" |

## 2. Menelusuri langkah

Jalankan langkah **persis seperti tertulis**, satu per satu, catat nilainya.

Contoh: (1) mulai dengan 9; (2) kurangi 3; (3) kalikan 7; (4) bagi 2.
9 → 6 → 42 → **21**.

## 3. Kasus uji

**Kasus uji** = **masukan** + **hasil yang diharapkan**. Jalankan langkah
dengan masukan itu, lalu bandingkan.

Langkah "luas persegi panjang = p + l" (salah):

| Masukan | Diharapkan | Hasil langkah | Lolos? |
|---|---|---|---|
| p = 2, l = 2 | 4 | 4 | Lolos (kebetulan!) |
| p = 6, l = 3 | 18 | 9 | **Gagal** → kesalahan terungkap |

Lolos pada satu kasus **tidak** membuktikan langkah benar. Kasus yang
**gagal** membuktikan ada kesalahan.

## 4. Tanda perbandingan dan kasus batas

| Tanda | Arti | 120 memenuhi "≥ 120"? |
|---|---|---|
| `>` | lebih dari | — |
| `≥` | lebih dari atau sama dengan | Ya |
| `<` | kurang dari | — |
| `≤` | kurang dari atau sama dengan | — |

*Deskripsi diagram dg-w07-04:* aturan "boleh naik wahana bila tinggi ≥
120 cm"; kasus batas 119 dan 120.

Kesalahan sering terjadi **tepat di batas** (memakai `>` padahal aturannya
`≥`). Uji **tepat di batas** dan **tepat di sebelahnya**: 119 (tidak boleh)
dan 120 (boleh). Kasus jauh dari batas (90, 150) tidak akan mengungkap
kesalahan `>` vs `≥`.

## 5. Contoh terbimbing

**Soal:** Langkah tertulis: "Jika tinggi > 120, tulis boleh; selain itu tulis
tidak". Aturannya ≥ 120. Kasus uji mana yang mengungkap kesalahan: 150, 120,
100?

1. 150: diharapkan boleh, langkah "boleh" → lolos.
2. 120: diharapkan boleh, langkah "tidak" → **gagal**.
3. 100: diharapkan tidak, langkah "tidak" → lolos.

Kasus 120 mengungkap kesalahan.

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Langkah yang lolos satu tes pasti benar" | Satu kegagalan cukup membuktikan salah; satu kelulusan tidak membuktikan benar |
| "Kasus uji = masukan saja" | Harus ada hasil yang diharapkan |
| "Uji nilai jauh dari batas sudah cukup" | Uji tepat di batas dan di sebelahnya |
| "Saat menelusuri, perbaiki langkah yang salah di kepala" | Jalankan persis seperti tertulis |

## 7. Latihan terbimbing (`mod-w07.prac-04`, tidak dinilai)

1. Perbaiki: "Panaskan oven sebentar".
2. Telusuri: mulai 4; kalikan 5; kurangi 2; bagi 6.
3. Aturan "diskon pelajar bila usia ≤ 18". Pilih dua kasus uji batas.

## 8. Cek pemahaman (tidak dinilai)

- Mengapa kasus p = 2, l = 2 tidak mengungkap kesalahan "luas = p + l"?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Mis. "Panaskan oven pada 180 °C selama 10 menit".
2. 4 × 5 = 20; 20 − 2 = 18; 18 ÷ 6 = 3.
3. 18 (masih diskon) dan 19 (tidak).

Cek pemahaman: 2 + 2 dan 2 × 2 kebetulan sama-sama 4.

## Ringkasan

- Algoritma: jelas, berurutan benar, berakhir.
- Telusuri persis seperti tertulis.
- Kasus uji = masukan + hasil diharapkan; uji tepat di batas.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Algoritma | algorithm | Langkah tepat, berurutan, berakhir |
| Ambigu | ambiguous | Dapat ditafsirkan berbeda |
| Menelusuri | trace | Menjalankan langkah sambil mencatat nilai |
| Kasus uji | test case | Masukan dan hasil yang diharapkan |
| Kasus batas | boundary test | Masukan tepat di batas aturan dan di sebelahnya |
