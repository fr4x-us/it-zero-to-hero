---
activity_id: mod-w03.lab.act-03
component: mod-w03.lab
content_version: "1.0"
variants: [mod-w03.lab.act-03.vA, mod-w03.lab.act-03.vB]
competencies: [comp-w03-net-01, comp-w03-proto-01, comp-w03-layer-01, comp-w03-rate-01]
max_points: 30
estimated_minutes: 30
checks_file: checks.yaml
---

# Lab W3 · Aktivitas 3 — Perangkat, Protokol, Lapisan, dan Kecepatan

## Tujuan

1. Menentukan peran perangkat jaringan.
2. Menentukan protokol dan port dari sebuah kejadian.
3. Menentukan lapisan TCP/IP yang bermasalah.
4. Menghitung konversi kecepatan dan waktu unduh ideal.

## Prasyarat

Pelajaran 1, Pelajaran 3, Pelajaran 4 §1–§2.

## Asumsi (model W3)

Kecepatan ideal: tetap, tanpa tambahan informasi protokol; aturan desimal
(1 byte = 8 bit). Nama domain berakhiran `.example` adalah contoh.

**Contoh terlihat (tidak dinilai):** 32 Mbps = 4 MB/s.

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 1 | **Fungsi** (model peran W3, fungsi dinilai terpisah) yang menghubungkan LAN rumah dengan internet dan meneruskan paket antarjaringan: (a) switch, (b) router, (c) access point, (d) modem | **Fungsi** (model peran W3, fungsi dinilai terpisah walaupun router Wi-Fi rumah menggabungkannya) yang memancarkan Wi-Fi agar ponsel dapat bergabung ke LAN: (a) switch, (b) router, (c) access point, (d) modem |
| 2 | Laptop baru bergabung ke Wi-Fi dan otomatis mendapat alamat IP, mask, dan gateway. Tulis nama protokolnya | Browser perlu mengetahui alamat IP dari nama `perpustakaan.example`. Tulis nama protokolnya |
| 3 | Situs dibuka dengan `https://`. Tulis nomor port bawaan di server | Situs dibuka dengan `http://` (tanpa s). Tulis nomor port bawaan di server |
| 4 | Kabel LAN laptop tercabut sehingga lampu port mati. Lapisan TCP/IP yang bermasalah: (a) aplikasi, (b) transport, (c) internet, (d) akses jaringan | Kabel dan alamat IP benar dan situs lain terbuka, tetapi aplikasi email gagal karena alamat server di pengaturan aplikasinya salah ketik. Lapisan yang bermasalah: (a) aplikasi, (b) transport, (c) internet, (d) akses jaringan |
| 5 | 96 Mbps = … MB/s | 9 MB/s = … Mbps |
| 6 | Berkas 750 MB diunduh pada 30 Mbps = … detik | Berkas 900 MB diunduh pada 40 Mbps = … detik |

## Yang diserahkan

Huruf opsi (1, 4), nama protokol (2), bilangan bulat (3, 5, 6; boleh
diikuti satuan yang diminta). Satuan kecepatan di nomor 5 peka huruf
besar/kecil: tulis persis `MB/s` (varian A) atau `Mbps` (varian B), atau
angka saja; `b` kecil = bit, `B` besar = byte.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, opsi di luar a–d, angka desimal, atau satuan lain → 0 untuk
pemeriksaan itu; lainnya tetap dinilai. Gangguan sistem → evaluasi diulang
tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan singkat untuk varian yang kamu
kerjakan.

## Remedial

Varian lain menurut VA-2; materi remedial R-NET, R-PROTO, R-LAYER, R-RATE.
