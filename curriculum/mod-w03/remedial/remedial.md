---
module_id: mod-w03
content_version: "1.0"
template: TPL-14
purpose: "Penjelasan ulang dan latihan tambahan per kompetensi untuk persiapan remedial (tidak dinilai)"
---

# Materi Remedial W3

Gunakan bagian yang sesuai dengan kompetensi yang belum dikuasai (umpan
balik ujian menampilkan rincian per kompetensi, FB-A). Latihan di sini tidak
dinilai dan tidak memberi XP. Attempt remedial memakai **varian setara**
yang dipilih menurut VA-1–VA-6: varian dengan pemakaian paling sedikit,
bila seri bukan varian attempt sebelumnya, bila masih seri indeks terkecil
(VA-2; pemakaian ulang VA-3); remedial tidak dibatasi jumlahnya.

## R-NET — Jaringan dan perangkat (LO1)

**Ingat kembali:** switch = di dalam satu LAN; access point = Wi-Fi ke LAN;
router = antarjaringan; modem = ke saluran ISP. Klien meminta, server
menyediakan.

**Latihan tambahan:** (1) Kotak berport banyak yang menyambungkan 8
komputer di ruang guru? (2) Laptop yang membagikan folder ke laptop lain
berperan sebagai? *Jawaban:* (1) switch; (2) server (untuk layanan berbagi
folder itu).

## R-IP — Alamat IPv4 privat/publik (LO2)

**Ingat kembali:** valid = 4 oktet 0–255, tanpa nol di depan. Privat =
`10.x`, `172.16`–`172.31`, `192.168.x`. Periksa **oktet kedua** untuk
alamat `172.…`. "Publik" di soal W3 = valid dan bukan privat, karena alamat
soal dipilih di luar rentang khusus lain (model W3).

**Latihan tambahan:** klasifikasikan: (1) `172.24.0.3`, (2) `172.10.0.3`,
(3) `10.1.256.1`, (4) `192.168.44.4`. *Jawaban:* (1) privat; (2) publik;
(3) tidak valid; (4) privat.

## R-SUBNET — Jaringan /24 (LO3)

**Ingat kembali:** ambil tiga oktet pertama → tambah `.0` (jaringan),
`.255` (broadcast), `.1`–`.254` (host); satu jaringan ⇔ tiga oktet pertama
sama. Rentang `.a`–`.b` berisi `b − a + 1` alamat.

**Latihan tambahan:** untuk `172.27.8.66` /24: jaringan? broadcast?
Apakah `172.27.9.66` satu jaringan? Rentang DHCP `.30`–`.79` berisi berapa
alamat? *Jawaban:* `172.27.8.0`; `172.27.8.255`; tidak; 79 − 30 + 1 = 50.

## R-PROTO — Protokol (LO4)

**Ingat kembali:** DHCP = alamat otomatis; DNS = nama → IP; HTTP port 80;
HTTPS port 443 (terenkripsi, tetapi tidak menjamin situs jujur); TCP
mengirim ulang dan menyusun urutan selama sambungan berjalan, UDP ringan.

**Latihan tambahan:** ponsel mendapat alamat, situs dapat dibuka dengan
alamat IP, tetapi tidak dengan nama. Protokol yang diperiksa? *Jawaban:*
DNS.

## R-LAYER — Lapisan TCP/IP (LO5)

**Ingat kembali (dari atas):** Aplikasi (HTTP, DNS, DHCP) → Transport
(TCP, UDP, port) → Internet (IP, router) → Akses jaringan (Ethernet, Wi-Fi,
switch, access point). Kirim = membungkus ke bawah; terima = membuka ke
atas. Saat memeriksa gangguan, mulai dari bawah: sambungan fisik dulu.

**Latihan tambahan:** lapisan apa: (1) sinyal Wi-Fi hilang, (2) nomor port
443, (3) router memilih jalur. *Jawaban:* (1) akses jaringan,
(2) transport, (3) internet.

## R-RATE — Kecepatan dan waktu transfer (LO6)

**Ingat kembali:** Mbps ÷ 8 = MB/s; MB/s × 8 = Mbps; waktu = MB × 8 ÷
Mbps; GB → MB dulu (× 1.000). Hitungan ideal; nyata biasanya lebih lambat.

**Latihan tambahan:** (1) 64 Mbps = … MB/s; (2) berkas 90 MB pada 15 Mbps
= … detik. *Jawaban:* (1) 8 MB/s; (2) 90 × 8 = 720; 720 ÷ 15 = 48 detik.
