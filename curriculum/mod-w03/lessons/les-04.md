---
lesson_id: mod-w03.les-04
practice_id: mod-w03.prac-04
module_id: mod-w03
content_version: "1.0"
title: "Kecepatan Jaringan dan Merencanakan Alamat"
language: id
duration_minutes: 40        # materi 28 + latihan terbimbing 12
competencies: [comp-w03-rate-01, comp-w03-subnet-01]
prerequisites: [mod-w03.les-02, mod-w03.les-03]
accessibility:
  diagrams:
    - id: dg-w03-04
      alt: "Pembagian alamat jaringan 172.20.9.0/24 menjadi beberapa wilayah."
      long_description: >
        Garis bilangan oktet terakhir 0 sampai 255. Di ujung kiri 0 berlabel
        alamat jaringan; 1 berlabel router (gateway); 2 sampai 49 berlabel
        alamat statis; 50 sampai 149 berlabel rentang DHCP; 150 sampai 254
        berlabel cadangan statis; 255 berlabel broadcast.
  tables_with_core_data: ["Tabel bit vs byte per detik", "Tabel rencana alamat contoh"]
  english_terms: [bandwidth, bit per second, Mbps, MB/s, transfer time, static IP, DHCP pool, address conflict]
---

# Pelajaran 4 — Kecepatan Jaringan dan Merencanakan Alamat

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Mengonversi **Mbps** dan **MB/s** dengan aturan desimal (1 byte = 8 bit).
2. Menghitung **waktu transfer** ideal sebuah berkas.
3. Menyusun **rencana alamat** jaringan /24: gateway, rentang DHCP, dan
   alamat **statis** yang tidak bentrok.

## Mengapa ini penting?

Iklan internet menulis "100 Mbps", sedangkan aplikasi unduhan menulis
"12,5 MB/s" — keduanya bisa berarti kecepatan yang sama. Dan saat printer
tiba-tiba "hilang", sering penyebabnya alamatnya berubah atau bentrok.

## 1. Bit dan byte per detik

Ingat W1: **1 byte = 8 bit**, dan awalan desimal **M = 1.000.000**.

| Satuan | Arti | Dipakai di |
|---|---|---|
| **Mbps** (megabit per detik) | 1.000.000 **bit** per detik | Paket internet, kecepatan Wi-Fi |
| **MB/s** (megabyte per detik) | 1.000.000 **byte** per detik | Aplikasi unduhan, salin berkas |

Konversi (dua arah):

- **Mbps → MB/s:** bagi 8. Contoh 16 Mbps ÷ 8 = **2 MB/s**.
- **MB/s → Mbps:** kali 8. Contoh 2 MB/s × 8 = **16 Mbps**.

Perhatikan huruf: **b** kecil = bit, **B** besar = byte.

## 2. Waktu transfer (model ideal)

```
waktu (detik) = ukuran (MB) × 8 ÷ kecepatan (Mbps)
```

*Deskripsi:* ukuran dalam megabyte dikali 8 menjadi megabit, lalu dibagi
kecepatan dalam megabit per detik.

**Contoh 1:** berkas 600 MB pada 40 Mbps → 600 × 8 = 4.800 Mb →
4.800 ÷ 40 = **120 detik** (2 menit).

**Contoh 2 (dua langkah):** berkas 1 GB pada 100 Mbps → 1 GB = 1.000 MB
(desimal, W1) → 1.000 × 8 = 8.000 Mb → 8.000 ÷ 100 = **80 detik**.

*Model sederhana W3:* hitungan ini **ideal** — kecepatan dianggap tetap
dan seluruhnya untuk data berkas. Kenyataannya lebih lambat karena tambahan
informasi protokol (lapisan), gangguan sinyal Wi-Fi, dan berbagi kecepatan
dengan perangkat lain. Semua soal W3 memakai satuan **desimal**; satuan
biner (MiB) tidak dipakai.

## 3. Merencanakan alamat jaringan /24

Di LAN, sebagian perangkat mendapat alamat otomatis dari **DHCP**, sebagian
diberi alamat **statis** (ditulis manual) agar tidak berubah — misalnya
printer atau kamera keamanan, supaya perangkat lain selalu dapat
menemukannya.

*Model W3:* alamat statis ditulis manual dan berada di luar rentang DHCP.
Ini salah satu cara yang sederhana dan aman, bukan satu-satunya: banyak
router juga menyediakan **reservasi DHCP** (DHCP selalu memberi alamat yang
sama kepada perangkat tertentu).

Contoh rencana untuk jaringan `172.20.9.0/24`:

```
.0 jaringan │ .1 router │ .2–.49 statis │ .50–.149 DHCP │ .150–.254 statis cadangan │ .255 broadcast
```

*Deskripsi diagram dg-w03-04:* oktet terakhir 0 = alamat jaringan; 1 =
router/gateway; 2–49 = alamat statis; 50–149 = rentang DHCP; 150–254 =
cadangan statis; 255 = broadcast.

| Perangkat | IP | Mask | Gateway |
|---|---|---|---|
| Router | `172.20.9.1` | `255.255.255.0` | — |
| Printer kantor | `172.20.9.10` | `255.255.255.0` | `172.20.9.1` |
| Komputer kasir | `172.20.9.11` | `255.255.255.0` | `172.20.9.1` |

*Deskripsi tabel:* tiga baris contoh dengan alamat statis di luar rentang
DHCP; semua perangkat memakai mask dan gateway yang sama.

Aturan rencana yang baik:

| ID | Aturan |
|---|---|
| RA-1 | Semua alamat valid dan berada di jaringan yang sama (tiga oktet pertama sama) |
| RA-2 | Bukan alamat jaringan (`.0`) atau broadcast (`.255`) |
| RA-3 | Setiap alamat **unik** (tidak ada dua perangkat memakai alamat yang sama) |
| RA-4 | Alamat statis **di luar** rentang DHCP, agar DHCP tidak memberikannya ke perangkat lain (konflik) |
| RA-5 | Setiap **perangkat klien di LAN** memakai mask yang sama dan gateway = alamat LAN router. Router sendiri tidak memakai alamat LAN-nya sebagai gateway; gateway router mengarah ke ISP dan diatur terpisah (di luar model W3) |

**Menghitung alamat tersisa:** jaringan /24 punya 254 alamat host. Pada
contoh di atas, rentang DHCP `.50`–`.149` berisi 149 − 50 + 1 = **100**
alamat. Alamat host di luar DHCP = 254 − 100 = 154. Router dan dua
perangkat statis memakai 3 → sisa **151** alamat statis.

Hati-hati menghitung rentang: dari `.50` sampai `.149` **termasuk kedua
ujungnya**, jadi 149 − 50 + 1, bukan 149 − 50.

## 4. Contoh terbimbing

**Soal:** Unduhan aplikasi menampilkan 5 MB/s. Berapa Mbps? Berapa lama
mengunduh berkas 450 MB pada kecepatan itu?

| Langkah | Hitung | Hasil |
|---|---|---|
| MB/s → Mbps | 5 × 8 | 40 Mbps |
| Ukuran dalam Mb | 450 × 8 | 3.600 Mb |
| Waktu | 3.600 ÷ 40 | 90 detik |

Periksa dengan cara lain: 450 MB ÷ 5 MB/s = 90 detik. Sama.

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "100 Mbps berarti berkas 100 MB selesai dalam 1 detik." | 100 Mbps = 12,5 MB/s; 100 MB butuh 8 detik (ideal) |
| "Mb dan MB sama." | b kecil = bit, B besar = byte; 1 MB = 8 Mb |
| "Alamat statis boleh di tengah rentang DHCP asal belum dipakai." | DHCP dapat memberikannya ke perangkat lain → konflik |
| "Rentang .50–.149 berisi 99 alamat." | Termasuk kedua ujung: 100 alamat |

## 6. Latihan terbimbing (`mod-w03.prac-04`, tidak dinilai)

1. 48 Mbps = … MB/s.
2. Berkas 200 MB pada 16 Mbps: berapa detik?
3. Jaringan `192.168.88.0/24` dengan rentang DHCP `.100`–`.149`. Berapa
   alamat di rentang DHCP? Bolehkah printer diberi `192.168.88.120`?

## 7. Cek pemahaman (tidak dinilai)

- Mengapa printer sebaiknya memakai alamat statis di luar rentang DHCP?
- Mengapa waktu unduhan nyata biasanya lebih lama dari hitungan ideal?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. 48 ÷ 8 = 6 MB/s.
2. 200 × 8 = 1.600 Mb; 1.600 ÷ 16 = 100 detik.
3. 149 − 100 + 1 = 50 alamat; tidak boleh, `.120` ada di dalam rentang
   DHCP (RA-4).

## Ringkasan

- Mbps ÷ 8 = MB/s; MB/s × 8 = Mbps (desimal; b = bit, B = byte).
- Waktu ideal = MB × 8 ÷ Mbps; ubah GB ke MB dulu (× 1.000).
- Rencana alamat /24: valid, satu jaringan, bukan `.0`/`.255`, unik,
  statis di luar DHCP, mask dan gateway sama.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Kecepatan transfer | bandwidth / data rate | Jumlah data per detik |
| Megabit per detik | Mbps | 1.000.000 bit per detik |
| Megabyte per detik | MB/s | 1.000.000 byte per detik |
| Alamat statis | static IP | Alamat yang diatur manual dan tetap |
| Rentang DHCP | DHCP pool | Alamat yang dibagikan DHCP |
| Konflik alamat | address conflict | Dua perangkat memakai alamat yang sama |
