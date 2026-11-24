---
lesson_id: mod-w03.les-03
practice_id: mod-w03.prac-03
module_id: mod-w03
content_version: "1.0"
title: "Protokol Dasar dan Model Lapisan TCP/IP"
language: id
duration_minutes: 45        # materi 33 + latihan terbimbing 12
competencies: [comp-w03-proto-01, comp-w03-layer-01]
prerequisites: [mod-w03.les-02]
accessibility:
  diagrams:
    - id: dg-w03-03
      alt: "Empat lapisan TCP/IP bertumpuk dengan contoh protokol dan perangkat."
      long_description: >
        Empat kotak bertumpuk. Paling atas Aplikasi (HTTP, HTTPS, DNS,
        DHCP). Di bawahnya Transport (TCP, UDP, nomor port). Di bawahnya
        Internet (IP, alamat IP, router). Paling bawah Akses jaringan
        (Ethernet, Wi-Fi, kabel, switch, access point). Panah ke bawah di
        sisi pengirim berlabel "membungkus", panah ke atas di sisi penerima
        berlabel "membuka bungkus".
  tables_with_core_data: ["Tabel fungsi protokol", "Tabel lapisan TCP/IP", "Tabel TCP vs UDP"]
  english_terms: [protocol, DHCP, DNS, domain name, HTTP, HTTPS, port, TCP, UDP, layer, encapsulation, segment, packet, frame]
---

# Pelajaran 3 — Protokol Dasar dan Model Lapisan TCP/IP

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan fungsi **DHCP**, **DNS**, **HTTP**, dan **HTTPS**, serta
   nomor **port** bawaan HTTP dan HTTPS.
2. Membedakan **TCP** dan **UDP**.
3. Menjelaskan empat lapisan **model TCP/IP** dan memetakan protokol serta
   perangkat ke lapisannya.
4. Mengurutkan proses **pembungkusan** data saat dikirim.

## Mengapa ini penting?

Saat kamu mengetik nama situs, beberapa "aturan percakapan" bekerja dalam
sekejap. Memahami aturan itu dan lapisannya membantumu menebak di mana
masalah terjadi: kabel, alamat, nama situs, atau aplikasinya.

## 1. Protokol

**Protokol** adalah aturan yang disepakati tentang cara perangkat
berkomunikasi — seperti tata cara menulis alamat di amplop.

| Protokol | Fungsi | Contoh kejadian |
|---|---|---|
| **DHCP** | Memberi perangkat alamat IP, mask, gateway, dan alamat server DNS **secara otomatis** | Ponsel bergabung ke Wi-Fi kafe dan langsung mendapat alamat |
| **DNS** | Menerjemahkan **nama domain** (mis. `sekolah.example`) menjadi alamat IP | Browser mencari alamat IP untuk nama yang kamu ketik |
| **HTTP** | Aturan meminta dan mengirim halaman web, **tanpa** enkripsi | Alamat diawali `http://` |
| **HTTPS** | HTTP yang **dienkripsi** (dilindungi dari penyadapan) | Alamat diawali `https://` |

**Port** adalah nomor yang menunjukkan **layanan** mana di sebuah
perangkat yang dituju. Alamat IP seperti alamat gedung; port seperti nomor
loket. Port bawaan: **HTTP = 80**, **HTTPS = 443**.

*Catatan keamanan (dibahas lagi di W4):* HTTPS melindungi data **selama
perjalanan**, tetapi tidak menjamin situsnya jujur. Situs palsu pun dapat
memakai HTTPS.

Nama domain di pelajaran ini memakai akhiran `.example`, yang memang
dicadangkan untuk contoh dan tidak dipakai situs nyata.

## 2. TCP dan UDP

| | **TCP** | **UDP** |
|---|---|---|
| Cara kerja | Membuat sambungan; **selama sambungan berjalan**, data yang hilang dikirim ulang dan disusun **berurutan**. Bila sambungan putus total, TCP memberi tahu aplikasi bahwa pengiriman gagal — TCP tidak dapat memaksa data sampai | Mengirim tanpa memastikan sampai dan tanpa menyusun urutan |
| Kelebihan | Andal | Ringan dan cepat |
| Pemakaian **umum** (model W3) | Halaman web, email, unduhan berkas | Panggilan suara/video langsung, game daring (data yang terlambat tidak berguna lagi) |

*Catatan:* ini pemakaian yang umum, bukan aturan mutlak. Sebagian layanan
video langsung memakai TCP, dan protokol modern seperti QUIC (dipakai
sebagian browser) berjalan di atas UDP tetapi tetap mengirim ulang data.

## 3. Model lapisan TCP/IP

```
 PENGIRIM                                   PENERIMA
 [4 Aplikasi      : HTTP, HTTPS, DNS, DHCP ]    ▲
 [3 Transport     : TCP, UDP, port         ]    │ membuka
 [2 Internet      : IP, alamat IP, router  ]    │ bungkus
 [1 Akses jaringan: Ethernet, Wi-Fi, kabel,]    │
 [                  switch, access point   ]    │
   │ membungkus ▼
```

*Deskripsi diagram dg-w03-03:* empat lapisan dari atas ke bawah: Aplikasi,
Transport, Internet, Akses jaringan, dengan contoh protokol/perangkat di
setiap lapisan. Pengirim membungkus data dari atas ke bawah; penerima
membuka bungkus dari bawah ke atas.

| Lapisan | Tugas | Contoh |
|---|---|---|
| **Aplikasi** | Layanan yang dipakai program | HTTP, HTTPS, DNS, DHCP |
| **Transport** | Mengantar data ke **aplikasi** yang tepat (port); andal atau cepat | TCP, UDP |
| **Internet** | Mengalamatkan dan mengirim **antarjaringan** | IP; router bekerja di sini |
| **Akses jaringan** | Mengirim bit lewat media fisik **di dalam satu jaringan** | Ethernet, Wi-Fi, kabel; switch dan access point |

**Pembungkusan** (*encapsulation*) saat mengirim:

1. Aplikasi menyiapkan **data** (mis. permintaan halaman).
2. Transport menambahkan informasi port → **segmen** (TCP).
3. Internet menambahkan alamat IP pengirim dan tujuan → **paket**.
4. Akses jaringan membungkusnya untuk media (Ethernet/Wi-Fi) → **frame**,
   lalu dikirim sebagai sinyal.

Penerima melakukan kebalikannya, dari frame sampai data diserahkan ke
aplikasi.

*Model sederhana W3:* buku lain memakai **model OSI 7 lapisan**; empat
lapisan TCP/IP adalah ringkasan yang dipakai di W3. Nama satuan data
(segmen, paket, frame) juga dipakai sedikit berbeda di beberapa sumber.

## 4. Contoh terbimbing: membuka sebuah situs

**Soal:** Tablet baru menyala di rumah dan pemiliknya membuka
`https://perpustakaan.example`. Protokol apa saja yang bekerja, dan di
lapisan apa?

| Urutan | Kejadian | Protokol | Lapisan |
|---|---|---|---|
| 1 | Tablet bergabung ke Wi-Fi rumah | Wi-Fi | Akses jaringan |
| 2 | Tablet mendapat alamat IP, mask, gateway otomatis | DHCP | Aplikasi |
| 3 | Browser menanyakan alamat IP `perpustakaan.example` | DNS | Aplikasi |
| 4 | Browser membuat sambungan andal ke server port 443 | TCP | Transport |
| 5 | Halaman diminta dan dikirim terenkripsi | HTTPS | Aplikasi |

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "DNS memberi alamat IP untuk perangkatku." | Itu DHCP; DNS menerjemahkan nama domain menjadi alamat IP |
| "HTTPS berarti situsnya pasti aman dan jujur." | HTTPS hanya mengenkripsi perjalanan data |
| "UDP rusak karena tidak memastikan data sampai." | UDP sengaja ringan; cocok untuk data yang harus cepat |
| "Router bekerja di lapisan aplikasi." | Router meneruskan paket berdasarkan alamat IP: lapisan internet |

## 6. Latihan terbimbing (`mod-w03.prac-03`, tidak dinilai)

1. Protokol apa: (a) menerjemahkan `kantin.example` menjadi alamat IP,
   (b) memberi alamat IP otomatis kepada laptop tamu.
2. Menurut pemakaian **umum** di model W3, TCP atau UDP: (a) mengunduh
   dokumen PDF lewat browser biasa, (b) panggilan suara langsung di aplikasi
   telepon internet.
3. Lapisan apa: (a) switch, (b) TCP, (c) HTTP.

## 7. Cek pemahaman (tidak dinilai)

- Bila DNS bermasalah, mengapa membuka situs dengan alamat IP **kadang**
  masih berhasil? (Tidak selalu: banyak server menampung beberapa situs
  dan memerlukan nama domainnya, dan HTTPS memeriksa nama domain.)
- Mengapa data dibungkus lapis demi lapis?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) DNS, (b) DHCP.
2. (a) TCP, (b) UDP.
3. (a) akses jaringan, (b) transport, (c) aplikasi.

## Ringkasan

- **DHCP** memberi alamat otomatis; **DNS** nama → alamat IP; **HTTP**
  (port 80) dan **HTTPS** (port 443, terenkripsi) untuk halaman web.
- **TCP** mengirim ulang dan menyusun berurutan selama sambungan berjalan;
  **UDP** ringan dan cepat tanpa jaminan itu.
- TCP/IP: **Aplikasi → Transport → Internet → Akses jaringan**; kirim =
  membungkus (data → segmen → paket → frame), terima = membuka bungkus.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Protokol | protocol | Aturan komunikasi yang disepakati |
| DHCP | Dynamic Host Configuration Protocol | Pemberi alamat IP otomatis |
| DNS | Domain Name System | Penerjemah nama domain ke alamat IP |
| Nama domain | domain name | Nama situs yang mudah diingat |
| HTTP / HTTPS | HyperText Transfer Protocol (Secure) | Aturan halaman web; HTTPS terenkripsi |
| Port | port | Nomor layanan di perangkat |
| TCP / UDP | Transmission Control Protocol / User Datagram Protocol | Protokol transport yang mengirim ulang dan menyusun urutan / yang ringan tanpa jaminan |
| Lapisan | layer | Tingkat tugas dalam model jaringan |
| Pembungkusan | encapsulation | Menambahkan informasi setiap lapisan saat mengirim |
| Segmen, paket, frame | segment, packet, frame | Nama data di lapisan transport, internet, akses jaringan |
