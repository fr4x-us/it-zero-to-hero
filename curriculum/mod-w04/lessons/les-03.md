---
lesson_id: mod-w04.les-03
practice_id: mod-w04.prac-03
module_id: mod-w04
content_version: "1.0"
title: "Mengenali Phishing dan Membaca Alamat Situs"
language: id
duration_minutes: 45        # materi 33 + latihan terbimbing 12
competencies: [comp-w04-phish-01]
prerequisites: [mod-w04.les-01, mod-w03.les-03]
accessibility:
  diagrams:
    - id: dg-w04-03
      alt: "Bagian-bagian alamat situs: skema, nama host, path."
      long_description: >
        Alamat https://portal.kampus.example/nilai dibagi tiga: "https://"
        berlabel skema; "portal.kampus.example" berlabel nama host, dengan
        "kampus.example" diberi label domain terdaftar dan "portal" diberi
        label subdomain; "/nilai" berlabel path.
  tables_with_core_data: ["Tabel tanda phishing", "Tabel contoh domain resmi dan tiruan", "Tabel respons aman"]
  english_terms: [phishing, URL, scheme, host name, domain, subdomain, path, lookalike domain, attachment, report]
---

# Pelajaran 3 — Mengenali Phishing dan Membaca Alamat Situs

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Mengenali **tanda phishing** pada pesan.
2. Membaca **alamat situs** (URL) dan menemukan **domain terdaftar** yang
   sebenarnya.
3. Memilih **respons aman** terhadap pesan mencurigakan.

## Mengapa ini penting?

Phishing adalah cara paling umum penipu mendapatkan kata sandi dan OTP.
Pesannya meniru bank, sekolah, atau kurir. Kemampuan membaca alamat situs
adalah salah satu perlindungan terbaik — dan kamu sudah punya dasarnya dari
DNS (W3).

## 1. Tanda phishing

| Tanda | Contoh |
|---|---|
| **Mendesak atau menakut-nakuti** | "Akun diblokir dalam 1 jam!" |
| **Hadiah yang terlalu bagus** | "Kamu menang ponsel, isi data di tautan ini" |
| **Meminta data rahasia** | Kata sandi, OTP, nomor kartu, PIN |
| **Tautan ke domain yang tidak cocok** | Mengaku dari bank, tetapi domain tautannya lain (§2) |
| **Lampiran atau berkas tak terduga** | Berkas `.apk` atau `.exe` dikirim lewat chat (W2: ekstensi dapat disembunyikan) |
| **Pengirim tidak cocok** | Nama tampilan "Admin Sekolah", tetapi alamat pengirimnya acak |

Pesan phishing dapat ditulis rapi, memakai logo asli, bahkan menyebut
namamu. Satu tanda saja sudah cukup untuk berhati-hati.

## 2. Membaca alamat situs (model W4)

```
https://portal.kampus.example/nilai
└skema┘└──── nama host ────┘└path┘
        └sub┘└domain terdaftar┘
```

*Deskripsi diagram dg-w04-03:* `https://` skema; `portal.kampus.example`
nama host; di dalamnya `kampus.example` domain terdaftar dan `portal`
subdomain; `/nilai` path.

Aturan **model W4**:

| ID | Aturan |
|---|---|
| UR-1 | **Nama host** = bagian setelah `://` sampai garis miring `/` pertama berikutnya (atau sampai akhir) |
| UR-2 | **Domain terdaftar** = **dua bagian terakhir** nama host (dipisah titik). Inilah yang menunjukkan **pemilik** situs |
| UR-3 | Bagian di **kiri** domain terdaftar adalah subdomain — pemilik domain bebas menamainya, termasuk meniru nama lain |
| UR-4 | Teks di **path** (setelah `/`) tidak menunjukkan pemilik |
| UR-5 | Huruf besar/kecil pada nama host tidak dibedakan |

Contoh (situs resmi: `kampus.example`):

| Alamat | Domain terdaftar | Resmi? | Alasan |
|---|---|---|---|
| `https://portal.kampus.example/nilai` | `kampus.example` | Ya | Subdomain milik pemilik resmi |
| `https://kampus.example.login-cepat.test/nilai` | `login-cepat.test` | **Tidak** | "kampus.example" hanya subdomain milik domain lain |
| `https://kampus-example.test/nilai` | `kampus-example.test` | **Tidak** | Tanda hubung membuat domain berbeda |
| `https://kampuss.example/nilai` | `kampuss.example` | **Tidak** | Huruf tambahan (domain tiruan) |
| `https://kampus.test/kampus.example` | `kampus.test` | **Tidak** | "kampus.example" hanya di path |

*Model sederhana W4:* nama domain di W4 memakai akhiran fiktif `.example`
dan `.test` (dicadangkan untuk contoh), sehingga domain terdaftar selalu
dua bagian terakhir. Di dunia nyata ada akhiran dua tingkat seperti
`.co.id` (domain terdaftar `nama.co.id` terdiri dari tiga bagian), dan ada
trik lain (mis. huruf yang mirip). Alamat W4 juga tidak memuat `@` atau
nomor port.

**HTTPS tidak cukup:** gembok HTTPS (W3) hanya berarti sambungan
terenkripsi ke domain itu. Situs phishing pun dapat memakai HTTPS. Yang
menentukan pemilik adalah **domain terdaftar**.

## 3. Respons aman

| Lakukan | Jangan |
|---|---|
| Buka situs/aplikasi resmi **sendiri** (ketik alamat atau pakai penanda/aplikasi resmi) | Mengeklik tautan di pesan mencurigakan |
| Verifikasi lewat **kanal resmi** (nomor di kartu, situs resmi) | Menelepon nomor yang tercantum di pesan mencurigakan |
| Laporkan ke pengelola (guru/IT sekolah, fitur "laporkan" di aplikasi) | Membalas, mengisi formulir, atau mengirim OTP |
| Hapus pesan setelah dilaporkan | Meneruskannya ke teman "untuk berjaga-jaga" |

## 4. Contoh terbimbing

**Soal:** Pesan WhatsApp: "Paket Anda tertahan. Bayar biaya Rp9.000 di
`https://kurir-cepat.example.bayar-ongkir.test/lacak` dalam 30 menit."
Kamu memang menunggu paket dari kurir resmi `kurir-cepat.example`.

| Langkah | Hasil |
|---|---|
| Nama host (UR-1) | `kurir-cepat.example.bayar-ongkir.test` |
| Domain terdaftar (UR-2) | `bayar-ongkir.test` — bukan `kurir-cepat.example` |
| Tanda lain | Mendesak (30 menit), meminta pembayaran |
| Respons aman | Jangan klik; buka aplikasi/situs resmi kurir sendiri untuk mengecek paket; laporkan pesan |

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Ada nama bank di alamatnya, jadi pasti resmi." | Nama itu bisa hanya subdomain atau path; lihat domain terdaftar |
| "Ada gembok HTTPS, jadi aman." | HTTPS hanya mengenkripsi sambungan |
| "Pesan dari teman pasti aman." | Akun teman dapat diambil alih dan dipakai mengirim tautan phishing |
| "Menelepon nomor di pesan untuk memastikan itu aman." | Nomor itu bisa milik penipu; pakai nomor dari kanal resmi |

## 6. Latihan terbimbing (`mod-w04.prac-03`, tidak dinilai)

Situs resmi koperasi: `koperasi-siswa.example`.

1. Tulis domain terdaftar: (a) `https://anggota.koperasi-siswa.example/saldo`,
   (b) `https://koperasi-siswa.example.saldo-cek.test/`.
2. Mana yang resmi di antara (a) dan (b)?
3. Sebutkan dua tanda phishing pada pesan: "SEGERA! Kirim OTP yang baru
   masuk agar saldo koperasimu tidak hangus hari ini."

## 7. Cek pemahaman (tidak dinilai)

- Mengapa bagian kiri nama host tidak dapat dipercaya untuk menentukan
  pemilik?
- Apa respons aman bila menerima tautan mencurigakan dari teman?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) `koperasi-siswa.example`, (b) `saldo-cek.test`.
2. (a).
3. Mendesak ("SEGERA", "hari ini") dan meminta OTP.

## Ringkasan

- Tanda phishing: mendesak, hadiah, meminta data rahasia, domain tidak
  cocok, lampiran tak terduga.
- Pemilik situs = **domain terdaftar** (dua bagian terakhir nama host,
  model W4); subdomain dan path dapat menipu; HTTPS tidak menjamin jujur.
- Respons aman: jangan klik; buka kanal resmi sendiri; laporkan.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Alamat situs | URL | Alamat lengkap sebuah halaman |
| Skema | scheme | Bagian awal seperti `https://` |
| Nama host | host name | Nama komputer/situs di dalam URL |
| Domain terdaftar | registered domain | Domain yang dimiliki pendaftar; penentu pemilik |
| Subdomain | subdomain | Bagian di kiri domain terdaftar |
| Path | path | Bagian setelah nama host |
| Domain tiruan | lookalike domain | Domain yang dibuat mirip domain resmi |
| Lampiran | attachment | Berkas yang dikirim bersama pesan |
