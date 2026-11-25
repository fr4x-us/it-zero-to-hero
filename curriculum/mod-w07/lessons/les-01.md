---
lesson_id: mod-w07.les-01
practice_id: mod-w07.prac-01
module_id: mod-w07
content_version: "1.0"
title: "Berpikir Komputasional, Dekomposisi, dan Urutan Tugas"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w07-decomp-01, comp-w07-order-01]
prerequisites: [mod-w06]
accessibility:
  diagrams:
    - id: dg-w07-01
      alt: "Pohon dekomposisi acara pentas seni kelas."
      long_description: >
        Kotak teratas "pentas seni kelas" bercabang ke tiga kotak: acara,
        tempat, publikasi. Kotak acara bercabang lagi ke dua kotak: daftar
        penampil dan susunan acara.
    - id: dg-w07-01b
      alt: "Diagram prasyarat lima tugas."
      long_description: >
        Lima lingkaran A sampai E dengan panah. Panah dari A ke B, dari A ke
        C, dari B ke D, dari C ke D, dan dari D ke E. Panah berarti tugas di
        ujung panah membutuhkan hasil tugas di pangkal panah.
  tables_with_core_data: ["Tabel empat pilar", "Tabel ciri dekomposisi yang baik", "Tabel urutan valid"]
  english_terms: [computational thinking, decomposition, sub-problem, dependency, prerequisite, valid order, parallel task]
---

# Pelajaran 1 — Berpikir Komputasional, Dekomposisi, dan Urutan Tugas

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menyebut empat pilar **berpikir komputasional**.
2. Memecah masalah dengan **dekomposisi** yang lengkap dan tidak
   tumpang-tindih.
3. Menyusun **urutan tugas yang valid** dari prasyarat, menghitung banyak
   urutan valid kecil, dan menemukan tugas yang dapat dikerjakan
   **bersamaan**.

## Mengapa ini penting?

Berpikir komputasional adalah cara memecahkan masalah sehingga solusinya
dapat dikerjakan oleh orang lain — atau oleh komputer. Programmer, manajer
proyek, dan analis memakai cara ini setiap hari, bahkan sebelum menulis satu
baris kode.

## 1. Empat pilar

| Pilar | Pertanyaan | Pelajaran |
|---|---|---|
| **Dekomposisi** | Bagian apa saja yang membentuk masalah ini? | 1 |
| **Pengenalan pola** | Apa yang berulang atau teratur? | 2 |
| **Abstraksi** | Informasi apa yang penting untuk tujuan ini? | 3 |
| **Algoritma** | Langkah tepat apa, dalam urutan apa? | 4 (dilanjutkan W8) |

## 2. Dekomposisi

*Deskripsi diagram dg-w07-01:* "pentas seni kelas" → acara (daftar
penampil, susunan acara), tempat, publikasi.

Dekomposisi yang baik:

| Ciri | Artinya |
|---|---|
| **Lengkap** | Gabungan semua bagian mencakup seluruh kebutuhan |
| **Tidak tumpang-tindih** | Satu kebutuhan tidak dikerjakan dua bagian |
| **Cukup kecil** | Setiap bagian dapat dikerjakan atau dijelaskan sendiri; bila belum, pecah lagi |

Sering ada **beberapa** dekomposisi yang sama baiknya. Yang dinilai di W7:
apakah bagian-bagiannya memenuhi ciri di atas untuk kebutuhan yang
disebutkan.

**Mengelompokkan menurut hasil.** Cara yang jelas untuk menentukan bagian
mana sebuah tugas: lihat **hasilnya**. "Menulis daftar penampil" menghasilkan
daftar acara → bagian acara, walaupun dikerjakan di ruang kelas.

## 3. Prasyarat dan urutan valid

Kadang satu bagian membutuhkan hasil bagian lain. Kita tulis **"X sebelum
Y"**: Y membutuhkan hasil X.

*Deskripsi diagram dg-w07-01b:* A → B, A → C, B → D, C → D, D → E.

Urutan **valid** = setiap prasyarat terpenuhi. Untuk diagram di atas:

| Urutan | Valid? | Alasan |
|---|---|---|
| A, B, C, D, E | Ya | Semua panah dari kiri ke kanan |
| A, C, B, D, E | Ya | B dan C tidak saling membutuhkan |
| A, B, D, C, E | Tidak | D dikerjakan sebelum C, padahal D butuh C |

Jadi ada **2** urutan valid. Cara memeriksa: ambil setiap prasyarat satu per
satu dan pastikan tugas yang dibutuhkan muncul lebih dulu.

**Menghitung urutan kecil.** Contoh lain: tiga tugas P, Q, R dengan prasyarat
hanya "P sebelum Q". R bebas, jadi R dapat diletakkan di depan, di tengah,
atau di belakang P-Q: R P Q, P R Q, P Q R → **3** urutan. Untuk masalah
kecil, daftarkan secara teratur agar tidak ada yang terlewat.

**Bersamaan.** Dua tugas dapat dikerjakan **bersamaan** oleh dua orang bila
tidak ada yang membutuhkan hasil yang lain, langsung maupun lewat tugas lain.
Pada diagram di atas: B dan C.

## 4. Contoh terbimbing

**Soal:** Tugas menyiapkan kemah: S = menyusun daftar barang, B = membeli
barang (butuh S), T = memesan tempat, K = mengemas tas (butuh B). Prasyarat:
S sebelum B, B sebelum K. Tulis satu urutan valid dan sebutkan tugas yang
dapat dikerjakan bersamaan dengan S.

1. Rantai: S → B → K; T bebas.
2. Satu urutan valid: T, S, B, K (masih ada yang lain).
3. T tidak membutuhkan dan tidak dibutuhkan siapa pun → T dapat dikerjakan
   bersamaan dengan S.

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Hanya ada satu dekomposisi yang benar" | Sering ada beberapa; periksa ciri-cirinya |
| "Bagian makin banyak makin baik" | Bagian yang tumpang-tindih atau tidak dibutuhkan justru menambah masalah |
| "Hanya ada satu urutan benar" | Tugas yang tidak saling bergantung boleh ditukar |
| "Tugas bersamaan cukup tidak bersebelahan" | Harus tidak saling membutuhkan, termasuk lewat tugas lain |

## 6. Latihan terbimbing (`mod-w07.prac-01`, tidak dinilai)

1. Pecah "merayakan ulang tahun guru" bila kebutuhannya: kue, kartu ucapan,
   dan waktu yang tepat.
2. Prasyarat: J sebelum K, J sebelum L. Tulis semua urutan valid J, K, L.
3. Pada soal 2, tugas mana yang dapat dikerjakan bersamaan?

## 7. Cek pemahaman (tidak dinilai)

- Mengapa "mengelompokkan menurut hasil" membuat pengelompokan tidak
  bergantung pada selera?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Satu dekomposisi yang memenuhi ciri: kue · kartu ucapan · waktu
   (bagian lain yang setara juga benar bila lengkap dan tidak tumpang-tindih).
2. J K L dan J L K (2 urutan).
3. K dan L.

Cek pemahaman: hasil tugas tertulis jelas, sehingga dua orang akan
memilih kelompok yang sama.

## Ringkasan

- Empat pilar: dekomposisi, pola, abstraksi, algoritma.
- Dekomposisi: lengkap, tidak tumpang-tindih, cukup kecil.
- Urutan valid memenuhi setiap prasyarat; tugas yang tidak saling
  bergantung boleh ditukar atau dikerjakan bersamaan.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Berpikir komputasional | computational thinking | Cara memecahkan masalah agar solusinya dapat dikerjakan orang lain atau komputer |
| Dekomposisi | decomposition | Memecah masalah menjadi bagian |
| Prasyarat | prerequisite | Tugas yang hasilnya dibutuhkan tugas lain |
| Urutan valid | valid order | Urutan yang memenuhi semua prasyarat |
| Bersamaan | in parallel | Dikerjakan pada waktu yang sama oleh orang berbeda |
