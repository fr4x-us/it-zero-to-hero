---
lesson_id: mod-w03.les-02
practice_id: mod-w03.prac-02
module_id: mod-w03
content_version: "1.0"
title: "Alamat IPv4 dan Jaringan /24"
language: id
duration_minutes: 55        # materi 40 + latihan terbimbing 15
competencies: [comp-w03-ip-01, comp-w03-subnet-01]
prerequisites: [mod-w03.les-01]
accessibility:
  diagrams:
    - id: dg-w03-02
      alt: "Alamat 192.168.5.42 dibagi menjadi bagian jaringan dan bagian host."
      long_description: >
        Alamat 192.168.5.42 ditulis dalam empat kotak oktet. Tiga kotak
        pertama (192, 168, 5) diberi label "bagian jaringan" dan berada di
        bawah tulisan 255.255.255 dari mask. Kotak keempat (42) diberi label
        "bagian host" dan berada di bawah angka 0 dari mask.
  tables_with_core_data: ["Tabel aturan alamat IPv4 valid", "Tabel rentang alamat privat", "Tabel alamat khusus jaringan /24"]
  english_terms: [IP address, IPv4, octet, private address, public address, loopback, subnet mask, network address, broadcast address, host, gateway, prefix /24]
---

# Pelajaran 2 — Alamat IPv4 dan Jaringan /24

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Membaca **alamat IPv4** dan menentukan apakah alamat itu **valid**.
2. Membedakan **alamat privat** dan **alamat publik**.
3. Dengan **mask 255.255.255.0** (/24), menentukan **alamat jaringan**,
   **alamat broadcast**, **rentang host**, dan apakah dua alamat berada di
   **jaringan yang sama**.
4. Menjelaskan peran **gateway**.

## Mengapa ini penting?

Setiap perangkat di jaringan butuh alamat agar data sampai ke tempat yang
benar — seperti alamat rumah untuk paket kiriman. Saat printer "tidak
ditemukan" atau dua perangkat "bentrok", penyebabnya sering alamat yang
salah.

## 1. Alamat IPv4

**Alamat IP** (*Internet Protocol*) adalah nomor yang menandai sebuah
perangkat di jaringan. Versi yang dipelajari di sini adalah **IPv4**:
empat bilangan desimal dipisahkan titik, mis. `192.168.5.42`. Setiap
bilangan disebut **oktet**.

| Aturan model W3 (alamat valid) | Contoh valid | Contoh tidak valid |
|---|---|---|
| Tepat **4** oktet dipisah titik | `10.1.2.3` | `10.1.2` (3 oktet) |
| Setiap oktet bilangan bulat **0–255** | `172.20.0.255` | `172.20.0.300` (300 > 255) |
| Hanya digit, tanpa spasi atau tanda | `192.168.0.7` | `192.168.0.-7` |
| Tanpa nol di depan (kecuali oktet `0`) | `10.0.0.8` | `10.0.0.08` |

Mengapa tanpa nol di depan? Sebagian program membaca `010` sebagai
bilangan oktal (= 8), bukan sepuluh — sumber kesalahan yang berbahaya.

*Catatan:* setiap oktet sebenarnya tersusun dari 8 bit (sehingga
nilainya 0–255). Cara menghitung dengan bit dipelajari di W6; di W3 kita
cukup memakai bilangan desimal. Ada juga **IPv6** (alamat yang jauh lebih
panjang, mis. `2001:db8::1`); W3 hanya membahas IPv4.

## 2. Alamat privat dan publik

**Alamat privat** dipakai di dalam LAN (rumah, sekolah, kantor) dan
**tidak** diteruskan langsung di internet. Rentangnya ditetapkan standar
(RFC 1918):

| Rentang privat | Dari | Sampai |
|---|---|---|
| 10.x.x.x | `10.0.0.0` | `10.255.255.255` |
| 172.16.x.x – 172.31.x.x | `172.16.0.0` | `172.31.255.255` |
| 192.168.x.x | `192.168.0.0` | `192.168.255.255` |

*Deskripsi tabel:* tiga rentang. Perhatikan rentang kedua: oktet kedua
harus 16 sampai 31; `172.15.…` dan `172.32.…` **bukan** privat.

**Alamat publik** dipakai di internet dan unik di seluruh dunia; biasanya
diberikan ISP ke router rumahmu. Router memakai teknik bernama **NAT** agar
banyak perangkat beralamat privat dapat berbagi satu alamat publik.

Alamat khusus: `127.0.0.1` (*loopback*) berarti "perangkat ini sendiri";
tidak dipakai sebagai alamat perangkat di jaringan.

*Model sederhana W3:* alamat valid yang **tidak** termasuk tiga rentang
privat dan bukan `127.x.x.x` kita sebut **publik**. Kenyataannya ada
rentang khusus lain (mis. `169.254.x.x` saat DHCP gagal, `100.64.x.x`
untuk ISP, rentang dokumentasi) yang tidak dipakai di soal W3.

## 3. Mask 255.255.255.0 (/24): jaringan dan host

Alamat IP terdiri dari **bagian jaringan** dan **bagian host**. Batasnya
ditunjukkan **subnet mask**. Di W3 kita hanya memakai mask
**`255.255.255.0`**, yang juga ditulis **/24**.

```
Alamat :  192 . 168 .  5  . 42
Mask   :  255 . 255 . 255 .  0
          └── bagian jaringan ──┘ └ host ┘
```

*Deskripsi diagram dg-w03-02:* oktet yang berhadapan dengan 255 adalah
bagian jaringan (192.168.5); oktet yang berhadapan dengan 0 adalah bagian
host (42).

Dengan mask /24:

| Istilah | Aturan | Contoh untuk `192.168.5.42` |
|---|---|---|
| **Alamat jaringan** | Tiga oktet pertama + `.0` | `192.168.5.0` |
| **Alamat broadcast** (ke semua perangkat di jaringan itu) | Tiga oktet pertama + `.255` | `192.168.5.255` |
| **Host pertama** | Tiga oktet pertama + `.1` | `192.168.5.1` |
| **Host terakhir** | Tiga oktet pertama + `.254` | `192.168.5.254` |
| **Jumlah alamat host yang dapat dipakai** | 256 − 2 (jaringan dan broadcast) | **254** |
| **Jaringan yang sama?** | Tiga oktet pertama **sama persis** | `192.168.5.200` ya; `192.168.6.42` tidak |

Alamat jaringan dan broadcast **tidak boleh** dipakai sebagai alamat
perangkat. Dua perangkat dalam satu jaringan juga **tidak boleh** memakai
alamat yang sama (konflik alamat).

*Model sederhana W3:* mask lain (mis. `255.255.255.128`, /25) membagi
oktet terakhir menjadi beberapa jaringan dan butuh hitungan bit (W6). Di
W3 semua soal memakai /24.

## 4. Gateway

Perangkat dapat langsung berbicara dengan perangkat lain di **jaringan
yang sama**. Untuk mengirim ke jaringan **lain** (mis. internet), perangkat
menyerahkan data ke **gateway** — biasanya alamat router di LAN itu.

Aturan: alamat gateway harus berada **di jaringan yang sama** dengan
perangkat. Router rumah sering memakai `.1` atau `.254`; itu kebiasaan,
bukan aturan wajib.

## 5. Contoh terbimbing

**Soal:** Laptop memakai `10.20.30.40`, mask `255.255.255.0`, gateway
`10.20.30.1`. Tentukan alamat jaringan, broadcast, apakah `10.20.31.5`
satu jaringan, dan apakah gatewaynya sah.

| Langkah | Berpikir | Hasil |
|---|---|---|
| Bagian jaringan | Mask /24 → tiga oktet pertama | `10.20.30` |
| Alamat jaringan | + `.0` | `10.20.30.0` |
| Broadcast | + `.255` | `10.20.30.255` |
| `10.20.31.5` | Tiga oktet pertama `10.20.31` ≠ `10.20.30` | Jaringan berbeda |
| Gateway `10.20.30.1` | Tiga oktet pertama sama, oktet terakhir 1–254 | Sah |

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Alamat 192.168.x.x dapat dihubungi dari mana saja di internet." | Itu alamat privat; hanya bermakna di dalam LAN |
| "`172.x.x.x` selalu privat." | Hanya `172.16`–`172.31` |
| "Jaringan /24 punya 256 alamat perangkat." | 256 alamat, tetapi 2 dipakai untuk jaringan dan broadcast → 254 |
| "Gateway boleh berada di jaringan lain." | Gateway harus berada di jaringan yang sama dengan perangkat |
| "`.0` dan `.255` dapat dipakai printer." | Pada /24 keduanya alamat khusus |

## 7. Latihan terbimbing (`mod-w03.prac-02`, tidak dinilai)

1. Valid atau tidak: (a) `192.168.1.254`, (b) `10.300.0.1`,
   (c) `172.16.5`.
2. Privat atau publik: (a) `172.31.0.9`, (b) `172.33.0.9`,
   (c) `192.168.77.1`.
3. Untuk `172.18.4.99` /24: alamat jaringan? broadcast? host terakhir?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa jumlah alamat host /24 adalah 254, bukan 256?
- Mengapa perangkat butuh gateway untuk membuka situs di internet?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) valid, (b) tidak valid (300 > 255), (c) tidak valid (3 oktet).
2. (a) privat, (b) publik (33 di luar 16–31), (c) privat.
3. `172.18.4.0`, `172.18.4.255`, `172.18.4.254`.

## Ringkasan

- IPv4 = 4 oktet desimal 0–255, tanpa nol di depan (model W3).
- Privat: `10.x`, `172.16`–`172.31`, `192.168.x`; selain itu (dan bukan
  `127.x`) disebut publik di model W3.
- /24: jaringan `.0`, broadcast `.255`, host `.1`–`.254` (254 alamat);
  satu jaringan ⇔ tiga oktet pertama sama; gateway di jaringan yang sama.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Alamat IP | IP address | Nomor penanda perangkat di jaringan |
| Oktet | octet | Satu dari empat bilangan pada alamat IPv4 |
| Alamat privat | private address | Alamat untuk dipakai di dalam LAN |
| Alamat publik | public address | Alamat yang dipakai di internet |
| Loopback | loopback | Alamat 127.0.0.1, "perangkat ini sendiri" |
| Subnet mask | subnet mask | Penanda batas bagian jaringan dan host |
| Alamat jaringan | network address | Alamat yang menandai jaringan itu sendiri |
| Alamat broadcast | broadcast address | Alamat untuk semua perangkat di jaringan |
| Host | host | Perangkat yang diberi alamat |
| Gateway | gateway | Alamat tujuan untuk data ke jaringan lain |
