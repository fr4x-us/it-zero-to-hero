---
lesson_id: mod-w04.les-02
practice_id: mod-w04.prac-02
module_id: mod-w04
content_version: "1.0"
title: "Autentikasi, Kata Sandi, dan MFA"
language: id
duration_minutes: 45        # materi 33 + latihan terbimbing 12
competencies: [comp-w04-auth-01]
prerequisites: [mod-w04.les-01]
accessibility:
  diagrams:
    - id: dg-w04-02
      alt: "Tiga faktor autentikasi: sesuatu yang diketahui, dimiliki, melekat."
      long_description: >
        Tiga kotak berdampingan. Kotak pertama "yang kamu ketahui" berisi
        kata sandi dan PIN. Kotak kedua "yang kamu miliki" berisi ponsel
        dengan aplikasi autentikator dan kunci keamanan. Kotak ketiga "yang
        melekat padamu" berisi sidik jari dan wajah. Di bawahnya tertulis:
        MFA = dua faktor atau lebih dari kotak yang berbeda.
  tables_with_core_data: ["Tabel faktor autentikasi", "Tabel jumlah kombinasi PIN", "Tabel kebiasaan kata sandi"]
  english_terms: [authentication, factor, password, passphrase, PIN, multi-factor authentication (MFA), one-time password (OTP), authenticator app, password manager, credential stuffing]
---

# Pelajaran 2 — Autentikasi, Kata Sandi, dan MFA

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan **autentikasi** dan tiga jenis **faktor**.
2. Menjelaskan **MFA** dan mengapa OTP tidak boleh dibagikan.
3. Menghitung jumlah **kombinasi PIN** dan menjelaskan mengapa kata sandi
   **panjang** dan **unik** lebih aman.

## Mengapa ini penting?

Akun email, media sosial, dan dompet digital dijaga oleh "kunci" yang
kamu pilih sendiri. Kunci yang lemah atau dipakai ulang membuat satu
kebocoran membuka banyak akun sekaligus.

## 1. Autentikasi dan faktornya

**Autentikasi** adalah menunjukkan bukti yang sudah terdaftar untuk sebuah
akun (mis. kata sandi atau ponsel tertentu) sehingga sistem mengizinkan
masuk. Sistem hanya memeriksa **bukti**, bukan siapa orangnya: siapa pun
yang mencuri bukti itu dapat masuk. Karena itu bukti harus dijaga.

| Faktor | Contoh |
|---|---|
| **Sesuatu yang kamu ketahui** | Kata sandi, PIN |
| **Sesuatu yang kamu miliki** | Ponsel dengan aplikasi autentikator, kode OTP yang dikirim ke ponselmu, kunci keamanan fisik |
| **Sesuatu yang melekat padamu** | Sidik jari, wajah |

*Deskripsi diagram dg-w04-02:* tiga kotak faktor seperti tabel di atas;
MFA memakai dua faktor atau lebih dari kotak yang **berbeda**.

**MFA** (*multi-factor authentication*, autentikasi multifaktor) memakai
**dua faktor atau lebih dari jenis berbeda**, mis. kata sandi + kode dari
aplikasi autentikator. Bila kata sandi bocor, penyerang masih butuh faktor
kedua.

**OTP** (*one-time password*) adalah kode sekali pakai. Faktornya adalah
**perangkat atau nomor** yang kamu miliki; kodenya hanya bukti sementara
bahwa seseorang punya akses ke perangkat, nomor, atau autentikator itu —
bukan bukti pasti siapa yang memegangnya. Kode dapat dicuri, diteruskan,
atau didapat lewat perangkat yang diretas. Siapa pun yang mendapat kode itu dapat memakainya, jadi
**jangan pernah membagikannya** kepada siapa pun, termasuk yang mengaku
petugas. Petugas resmi tidak pernah meminta OTP.

*Batas MFA:* MFA membuat pengambilalihan akun **jauh lebih sulit**, tetapi tidak
mustahil — misalnya bila korban tertipu menyerahkan OTP atau mengisi kode
di situs palsu.

*Catatan:* dua kata sandi berbeda bukan MFA — keduanya faktor jenis yang
sama ("yang diketahui").

## 2. Menghitung kombinasi PIN

PIN dari angka 0–9: setiap digit punya **10** kemungkinan, dan pilihan
setiap digit dikalikan.

| PIN | Hitungan | Kombinasi |
|---|---|---|
| 2 digit | 10 × 10 | 100 |
| 3 digit | 10 × 10 × 10 | 1.000 |
| 6 digit | 10 × 10 × 10 × 10 × 10 × 10 | 1.000.000 |

Setiap **tambahan satu digit** membuat kombinasi **10 kali lipat**.

Contoh perbandingan: PIN 3 digit dibanding 2 digit → 1.000 ÷ 100 =
**10 kali lipat** (satu digit tambahan).

*Asumsi hitungan (model W4):* digit boleh **diawali 0** dan boleh
**berulang** (mis. `0070`), jadi setiap posisi punya 10 pilihan. Hitungan
ini menghasilkan **jumlah PIN berbeda yang mungkin**, bukan peluang
sebuah PIN dipilih orang: kenyataannya orang sering memilih PIN mudah
(tanggal lahir, `123456`) yang ditebak lebih dulu. Banyak sistem juga
**membatasi** percobaan (mengunci akun atau memberi jeda setelah beberapa
kali salah); ini membuat menebak semua kombinasi jauh lebih lama dan sulit,
tetapi tidak menjamin mustahil (mis. bila pembatasannya lemah atau data
PIN bocor dari tempat lain).

## 3. Kata sandi yang kuat

| Kebiasaan baik | Mengapa |
|---|---|
| **Panjang** — mis. frasa sandi dari beberapa kata acak (≥ 12 karakter) | Makin panjang, makin banyak kemungkinan; lebih mudah diingat daripada simbol acak pendek. Panjang saja **tidak cukup**: kalimat terkenal, lirik lagu, atau sandi yang pernah bocor tetap mudah ditebak |
| **Unik** untuk setiap akun penting | Bila satu situs bocor, penyerang sering mencoba sandi yang sama di situs lain (*credential stuffing*) |
| Pakai **pengelola kata sandi** (*password manager*) | Menyimpan dan membuat sandi unik; kamu cukup mengingat satu sandi utama yang kuat |
| Aktifkan **MFA** | Sandi bocor saja tidak cukup untuk masuk |

| Kebiasaan buruk | Mengapa |
|---|---|
| Tanggal lahir, nama hewan peliharaan | Mudah ditebak dari media sosial |
| Sandi yang sama untuk banyak akun | Satu kebocoran membuka semuanya |
| Menulis sandi di catatan foto ponsel tanpa kunci | Siapa pun yang memegang ponsel dapat membacanya |
| Membagikan OTP | Menyerahkan faktor kedua kepada penyerang |

## 4. Contoh terbimbing

**Soal:** Raka memakai sandi `raka2010` untuk email, game, dan media
sosial, tanpa MFA. Situs game bocor. Apa risikonya dan apa perbaikannya?

| Langkah berpikir | Jawaban |
|---|---|
| Apa yang diketahui penyerang? | Sandi `raka2010` dari kebocoran situs game |
| Akun lain mana yang terancam? | Email dan media sosial (sandi sama) |
| Mengapa sandi itu lemah? | Pendek dan memuat nama + tahun yang mudah ditebak |
| Perbaikan | Sandi panjang dan **unik** per akun (pengelola kata sandi), aktifkan MFA terutama di email |

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Kata sandi pendek dengan banyak simbol selalu lebih kuat daripada frasa panjang." | Panjang sangat berpengaruh; frasa panjang dari kata acak kuat dan mudah diingat |
| "Petugas resmi boleh menerima OTP." | OTP tidak pernah dibagikan |
| "Dua kata sandi = MFA." | MFA butuh faktor dari jenis berbeda |
| "Menambah satu digit PIN hanya menambah sedikit kombinasi." | Setiap tambahan digit membuat kombinasi 10 kali lipat |

## 6. Latihan terbimbing (`mod-w04.prac-02`, tidak dinilai)

1. Faktor apa: (a) PIN ATM, (b) pemindai wajah, (c) kunci keamanan USB.
2. Berapa kombinasi PIN 2 digit? Berapa kali lipat PIN 2 digit dibanding
   1 digit?
3. Mana yang lebih baik untuk akun email: `Melati!1` atau
   `kopi-sepeda-awan-jendela`? Mengapa?

## 7. Cek pemahaman (tidak dinilai)

- Mengapa memakai satu sandi untuk semua akun berbahaya?
- Mengapa OTP disebut "yang kamu miliki"?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) yang diketahui, (b) yang melekat, (c) yang dimiliki.
2. 100; 100 ÷ 10 = 10 kali lipat.
3. Frasa panjang `kopi-sepeda-awan-jendela`: jauh lebih panjang dan
   tidak memuat nama yang mudah ditebak (tetap harus unik dan tidak
   dipakai di akun lain).

## Ringkasan

- Autentikasi = memeriksa bukti yang terdaftar untuk akun; faktor: diketahui, dimiliki,
  melekat. **MFA** = dua faktor atau lebih dari jenis berbeda.
- Kombinasi PIN = 10 pangkat jumlah digit; +1 digit → ×10.
- Sandi **panjang, unik**, pengelola kata sandi, MFA; **OTP tidak pernah
  dibagikan**.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Autentikasi | authentication | Pemeriksaan bukti yang terdaftar untuk akun sebelum mengizinkan masuk |
| Faktor | factor | Jenis bukti autentikasi |
| Frasa sandi | passphrase | Kata sandi panjang dari beberapa kata |
| Autentikasi multifaktor | MFA | Dua faktor atau lebih dari jenis berbeda |
| Kode sekali pakai | OTP (one-time password) | Kode yang hanya berlaku sekali |
| Aplikasi autentikator | authenticator app | Aplikasi pembuat kode MFA |
| Pengelola kata sandi | password manager | Aplikasi penyimpan dan pembuat sandi |
| Pengisian kredensial | credential stuffing | Mencoba sandi bocor di situs lain |
