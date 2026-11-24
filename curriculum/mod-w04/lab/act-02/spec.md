---
activity_id: mod-w04.lab.act-02
component: mod-w04.lab
content_version: "1.0"
variants: [mod-w04.lab.act-02.vA, mod-w04.lab.act-02.vB]
competencies: [comp-w04-phish-01]
max_points: 40
estimated_minutes: 30
checks_file: checks.yaml
---

# Lab W4 · Aktivitas 2 — Menganalisis Pesan dan Alamat Situs

## Tujuan

1. Menemukan **domain terdaftar** tautan dengan aturan UR-1–UR-5.
2. Menilai setiap pesan sebagai **aman** atau **mencurigakan**.

## Prasyarat

Pelajaran 3.

## Keamanan aktivitas

Semua pesan dan domain fiktif (`.example`, `.test`). **Jangan** membuka
tautan; cukup membaca teksnya.

## Aturan penilaian pesan

Tulis `C` (mencurigakan) bila **domain terdaftar** tautan **bukan** domain
resmi pengirim yang tercantum di daftar, **atau** pesan meminta kata sandi,
PIN, OTP, atau data kartu. Selain itu tulis `A` (aman).

**Contoh terlihat (tidak dinilai):** contoh terbimbing Pelajaran 3 §4
(`kurir-cepat.example`).

## Data (fixture)

**Varian A** — domain resmi: `pelita.example` (Sekolah Pelita),
`bankcontoh.example` (Bank Contoh), `kirimcepat.example` (Kirim Cepat),
`arenagame.example` (Arena Game).

| ID | Pengirim (nama tampilan) | Isi pesan |
|---|---|---|
| M1 | Admin Sekolah Pelita | Nilai rapor sudah terbit. Lihat di `https://rapor.pelita.example/semester` |
| M2 | Bank Contoh | Akun Anda DIBEKUKAN! Verifikasi dalam 30 menit: `https://bankcontoh.example.amankan-akun.test/login` |
| M3 | Kirim Cepat | Paket tertahan. Bayar Rp7.500 di `https://kirimcepat-example.test/bayar` |
| M4 | Arena Game | Turnamen akhir pekan dibuka. Jadwal di `https://www.arenagame.example/turnamen` |

**Varian B** — domain resmi: `dompetku.example` (DompetKu),
`bacabuku.example` (Perpustakaan BacaBuku), `klubrobot.example` (Klub
Robot), `jalanyuk.example` (JalanYuk).

| ID | Pengirim (nama tampilan) | Isi pesan |
|---|---|---|
| M1 | DompetKu | Saldo Anda HANGUS hari ini! Masukkan PIN di `https://dompetku.example.hadiah-saldo.test/klaim` |
| M2 | Perpustakaan BacaBuku | Buku pesananmu sudah tersedia: `https://layanan.bacabuku.example/pinjaman` |
| M3 | Klub Robot | Pendaftaran lomba robot dibuka: `https://klubrobot.example/daftar` |
| M4 | JalanYuk | Akun Anda diblokir. Login ulang di `https://jalanyuk.test/akun/jalanyuk.example` |

## Yang diserahkan

Untuk setiap pesan: (1) domain terdaftar tautannya; (2) `A` atau `C`.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01, c03, c05, c07 | Domain terdaftar benar (huruf besar/kecil bebas; tanpa `https://` atau path) | 4 × 5 = 20 |
| c02, c04, c06, c08 | Penilaian `A`/`C` benar | 4 × 5 = 20 |
| **Maksimum aktivitas** | | **40** |

## Kasus gagal

Kosong, domain dengan skema/path, atau huruf selain A/C → 0 untuk
pemeriksaan itu; lainnya tetap dinilai. Gangguan sistem → evaluasi diulang
tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per pemeriksaan dan pembahasan nama host untuk varian yang
kamu kerjakan.

## Remedial

Varian lain menurut VA-2; ulangi Pelajaran 3 §2–§3; materi remedial
R-PHISH.
