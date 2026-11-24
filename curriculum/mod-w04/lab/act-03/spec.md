---
activity_id: mod-w04.lab.act-03
component: mod-w04.lab
content_version: "1.0"
variants: [mod-w04.lab.act-03.vA, mod-w04.lab.act-03.vB]
competencies: [comp-w04-cia-01, comp-w04-auth-01, comp-w04-protect-01, comp-w04-incident-01]
max_points: 30
estimated_minutes: 30
checks_file: checks.yaml
---

# Lab W4 · Aktivitas 3 — Tujuan Keamanan, Autentikasi, Perlindungan, dan Respons

## Tujuan

Menerapkan tujuan keamanan, MFA, hitungan kombinasi PIN, aturan cadangan
3-2-1, izin aplikasi, dan langkah respons yang tepat.

## Prasyarat

Pelajaran 1 §1, Pelajaran 2, Pelajaran 4.

## Asumsi (model W4)

Setiap PIN sama mungkin (angka 0–9). Cadangan memakai aturan CB-1–CB-4
(Pelajaran 4 §2). Semua skenario fiktif.

**Contoh terlihat (tidak dinilai):** kombinasi PIN 1 digit = 10.

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 1 | Jadwal piket di grup kelas diubah oleh orang yang tidak berhak. Tujuan yang terutama terganggu: (a) kerahasiaan, (b) integritas, (c) ketersediaan, (d) autentikasi | Aplikasi absensi sekolah tidak dapat dibuka seharian karena servernya mati. Tujuan yang terutama terganggu: (a) kerahasiaan, (b) integritas, (c) ketersediaan, (d) autentikasi |
| 2 | Pasangan mana yang merupakan MFA? (a) kata sandi + PIN, (b) kata sandi + kode aplikasi autentikator, (c) dua kata sandi berbeda, (d) PIN + jawaban pertanyaan rahasia | Pasangan mana yang merupakan MFA? (a) kata sandi + sidik jari, (b) kata sandi + PIN, (c) PIN + tanggal lahir, (d) dua kata sandi berbeda |
| 3 | Berapa kombinasi PIN 7 digit? | Berapa kombinasi PIN 8 digit? |
| 4 | Rencana: laptop (asli) + flashdisk di rumah + kartu memori di rumah + folder lain di laptop yang sama. Berapa salinan yang dihitung (CB-1–CB-4), termasuk asli? | Rencana: PC (asli) + dua folder lain di PC yang sama + layanan awan. Berapa salinan yang dihitung (CB-1–CB-4), termasuk asli? |
| 5 | Aplikasi kamus luring meminta izin kontak, lokasi, dan mikrofon; fungsinya hanya mencari arti kata yang diketik. Pilihan sesuai hak minimum: (a) izinkan semua, (b) izinkan kontak saja, (c) izinkan lokasi sepanjang waktu, (d) tolak ketiganya | Aplikasi pemindai dokumen meminta izin kamera dan kontak; fungsinya memotret dokumen. Pilihan sesuai hak minimum: (a) izinkan kamera saat aplikasi digunakan, tolak kontak, (b) izinkan keduanya sepanjang waktu, (c) izinkan kontak saja, (d) tolak kamera walaupun aplikasi harus memotret |
| 6 | Laptop menampilkan pesan tebusan ransomware. Langkah pertama yang paling tepat: (a) membayar tebusan, (b) menyambungkan harddisk cadangan, (c) mengunggah tangkapan layar ke media sosial, (d) memutuskan laptop dari jaringan | Temanmu menemukan sandi Wi-Fi sekolah tertulis di meja guru dan mengajakmu memakainya diam-diam untuk mengunduh game. Tindakan yang tepat: (a) memakainya sebentar saja, (b) memotret sandinya untuk nanti, (c) menolak dan memberi tahu guru agar sandinya diamankan, (d) membagikannya ke grup kelas |

## Yang diserahkan

Huruf opsi (1, 2, 5, 6); bilangan bulat (3, 4) — boleh dengan titik ribuan
berpola `1.234` dan diikuti satuan yang diminta (`kombinasi`, `salinan`).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, huruf di luar a–d, angka dengan pangkat (`10^7`), desimal, atau
titik ribuan yang salah → 0 untuk pemeriksaan itu; lainnya tetap dinilai.
Gangguan sistem → evaluasi diulang tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasannya.

## Remedial

Varian lain menurut VA-2; materi remedial R-CIA, R-AUTH, R-PROTECT,
R-INCIDENT.
