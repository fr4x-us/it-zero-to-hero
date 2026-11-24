---
lesson_id: mod-w04.les-04
practice_id: mod-w04.prac-04
module_id: mod-w04
content_version: "1.0"
title: "Melindungi Perangkat dan Menanggapi Insiden"
language: id
duration_minutes: 45        # materi 33 + latihan terbimbing 12
competencies: [comp-w04-protect-01, comp-w04-incident-01]
prerequisites: [mod-w04.les-02, mod-w04.les-03]
accessibility:
  diagrams:
    - id: dg-w04-04
      alt: "Aturan cadangan 3-2-1."
      long_description: >
        Tiga ikon dokumen berlabel "3 salinan". Di bawahnya dua ikon
        berbeda (laptop dan harddisk eksternal) berlabel "2 jenis media".
        Di samping, ikon awan berlabel "1 di luar lokasi".
  tables_with_core_data: ["Tabel praktik perlindungan", "Tabel aturan 3-2-1 model W4", "Tabel langkah respons insiden"]
  english_terms: [update, patch, vulnerability, antimalware, backup, 3-2-1 rule, offsite, screen lock, incident response, report, ethics]
---

# Pelajaran 4 — Melindungi Perangkat dan Menanggapi Insiden

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Memilih praktik perlindungan: **pembaruan**, sumber aplikasi resmi,
   **izin aplikasi**, **kunci layar**, dan **cadangan 3-2-1**.
2. Memeriksa apakah sebuah rencana cadangan memenuhi aturan **3-2-1**.
3. Mengurutkan langkah **respons insiden** pribadi dan bertindak etis.

## Mengapa ini penting?

Tidak ada perlindungan yang sempurna. Kebiasaan yang baik mengurangi
peluang terkena masalah, dan rencana respons membuat kerugian sekecil
mungkin bila masalah tetap terjadi.

## 1. Praktik perlindungan

| Praktik | Mengapa |
|---|---|
| **Pembaruan** (*update/patch*) OS dan aplikasi | Menutup **celah keamanan** (*vulnerability*) yang sudah diketahui |
| Pasang aplikasi dari **sumber resmi** (toko aplikasi resmi, situs pembuat) | Mengurangi risiko trojan |
| Periksa **izin aplikasi** sesuai fungsinya (W2, hak minimum) | Aplikasi yang tidak perlu kontak/lokasi tidak diberi akses itu |
| **Kunci layar** (PIN, sidik jari, wajah) | Melindungi perangkat yang tertinggal atau dipinjam tanpa izin |
| Perlindungan **antimalware** bawaan aktif dan diperbarui | Mendeteksi banyak malware yang sudah dikenal |
| Akun **pengguna biasa** untuk sehari-hari (W2) | Membatasi kerusakan bila ada program jahat |
| Hati-hati di **Wi-Fi publik** | Pastikan nama jaringan resmi; hindari membuka akun penting di jaringan yang tidak jelas |

*Batas perlindungan:* pembaruan dan antimalware **mengurangi** risiko,
tetapi tidak menjamin perangkat bebas malware. Karena itu cadangan dan
rencana respons tetap dibutuhkan.

## 2. Cadangan 3-2-1 (model W4)

```
[doc][doc][doc]  3 salinan
[laptop][HDD]    2 jenis media
        (awan)   1 di luar lokasi
```

*Deskripsi diagram dg-w04-04:* tiga salinan data, pada dua jenis media
berbeda, dan satu salinan di luar lokasi.

| ID | Aturan model W4 |
|---|---|
| CB-1 | Minimal **3 salinan terpisah** data, **termasuk** data asli (salinan yang rusak/hilang sendiri-sendiri, bukan nama lain untuk berkas yang sama) |
| CB-2 | Salinan berada di minimal **2 jenis media** berbeda. Jenis media W4: penyimpanan internal perangkat · harddisk/SSD eksternal · flashdisk · kartu memori · layanan penyimpanan awan |
| CB-3 | Minimal **1 salinan di luar lokasi** (rumah/sekolah tempat data asli), mis. layanan awan atau rumah kerabat |
| CB-4 | Salinan di folder lain pada **perangkat yang sama** dengan data asli **tidak dihitung** sebagai salinan cadangan (rusak atau hilang bersama) |

*Model W4:* setiap salinan dianggap utuh dan dapat dipulihkan. Di dunia
nyata cadangan perlu **diuji** sesekali (coba pulihkan satu berkas), karena
cadangan yang rusak atau tidak lengkap baru ketahuan saat dibutuhkan.

**Contoh memenuhi:** tugas di PC rumah (asli) + SSD eksternal di rumah +
layanan awan → 3 salinan, 3 jenis media (internal, eksternal, awan), 1 di
luar lokasi (awan).

**Contoh tidak memenuhi:** tugas di PC (asli) + folder "cadangan" di PC
yang sama + flashdisk di rumah → hanya 2 salinan yang dihitung (CB-4) dan
tidak ada yang di luar lokasi.

Ransomware dapat mengunci cadangan yang **sedang tersambung**. Cadangan
yang biasanya dilepas (harddisk eksternal yang dicabut) atau versi lama di
layanan awan membantu pemulihan.

## 3. Respons insiden pribadi

**Insiden** adalah kejadian keamanan yang sedang atau sudah terjadi. Pola
umum: **hentikan → amankan → pulihkan**, dan **laporkan** — melapor tidak
harus menunggu akhir: sering lebih baik melapor sejak awal atau
bersamaan (mis. ke orang dewasa, pengelola IT, atau penyedia layanan), agar
mereka dapat membantu menghentikan kerusakan.

| Insiden | Langkah yang dianjurkan (urutan umum; pelaporan dapat dilakukan lebih awal) |
|---|---|
| Kata sandi dimasukkan ke situs palsu | (1) Ganti sandi akun itu dari perangkat aman · (2) Aktifkan MFA · (3) Periksa aktivitas login dan keluarkan sesi asing · (4) Ganti sandi akun lain yang memakai sandi sama · Laporkan ke penyedia/pengelola (kapan saja, sedini mungkin) |
| Perangkat terkena ransomware | (1) Putuskan dari jaringan · (2) Minta bantuan orang dewasa/pengelola IT; jangan membayar tebusan (tidak menjamin berkas kembali) · (3) Bersihkan/pasang ulang sistem · (4) Pulihkan dari cadangan · Laporkan (dapat bersamaan dengan langkah 2) |
| OTP terlanjur diberikan | Segera hubungi penyedia layanan lewat **kanal resmi** untuk mengamankan akun, lalu ganti sandi |

Untuk pemula: libatkan **orang dewasa tepercaya**, guru, atau pengelola IT;
jangan mencoba "membalas" penyerang.

## 4. Etika

- **Jangan** mengakses akun, perangkat, atau jaringan orang lain tanpa izin
  — walaupun kata sandinya terlihat atau "hanya ingin melihat". Itu
  melanggar privasi dan dapat melanggar hukum.
- Bila menemukan celah atau kata sandi orang lain, **beri tahu pemiliknya
  atau pengelola**, jangan mencobanya.
- Latihan keamanan hanya dilakukan pada sistem latihan milikmu sendiri atau
  yang diizinkan.

## 5. Contoh terbimbing

**Soal:** Fajar menyimpan foto lomba di laptop (asli), salinan di folder
lain laptop yang sama, dan salinan di kartu memori di laci rumah. Apakah
memenuhi 3-2-1? Apa perbaikan paling sederhana?

| Langkah | Hasil |
|---|---|
| Salinan yang dihitung (CB-4) | Laptop (asli) + kartu memori = 2 (folder lain di laptop tidak dihitung) |
| Jenis media | Internal laptop, kartu memori = 2 |
| Di luar lokasi | Tidak ada |
| Kesimpulan | Belum memenuhi (CB-1, CB-3 gagal) |
| Perbaikan | Tambahkan satu salinan di layanan awan atau di rumah kerabat → 3 salinan, ≥ 2 jenis, 1 di luar lokasi |

## 6. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Antimalware membuat perangkat kebal." | Mengurangi risiko, tidak menjamin |
| "Membayar tebusan pasti mengembalikan berkas." | Tidak ada jaminan; cadangan adalah perlindungan yang lebih andal |
| "Salinan di folder lain sudah cadangan." | Satu perangkat rusak → keduanya hilang (CB-4) |
| "Menunda pembaruan lebih aman." | Pembaruan menutup celah yang sudah diketahui |

## 7. Latihan terbimbing (`mod-w04.prac-04`, tidak dinilai)

1. Apakah memenuhi 3-2-1: dokumen di PC (asli) + flashdisk di rumah +
   layanan awan?
2. Urutkan untuk insiden ransomware: pulihkan dari cadangan · putuskan dari
   jaringan · bersihkan sistem.
3. Temanmu melihat kata sandi Wi-Fi tetangga tertempel di jendela dan ingin
   memakainya diam-diam. Tindakan yang etis?

## 8. Cek pemahaman (tidak dinilai)

- Mengapa cadangan yang selalu tersambung masih berisiko terhadap
  ransomware?
- Mengapa respons insiden dimulai dengan menghentikan penyebaran?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Ya: 3 salinan, 3 jenis media, awan di luar lokasi.
2. Putuskan dari jaringan → bersihkan sistem → pulihkan dari cadangan.
3. Tidak memakainya tanpa izin; bila perlu, beri tahu pemiliknya.

## Ringkasan

- Perlindungan: pembaruan, sumber resmi, izin aplikasi, kunci layar,
  antimalware, akun biasa, hati-hati di Wi-Fi publik — mengurangi risiko,
  tidak menjamin.
- Cadangan **3-2-1** (model W4): 3 salinan, 2 jenis media, 1 di luar
  lokasi; folder lain di perangkat yang sama tidak dihitung.
- Respons insiden: hentikan → amankan → pulihkan; laporkan sedini mungkin;
  bertindak etis.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Pembaruan | update / patch | Perbaikan software, termasuk celah keamanan |
| Celah keamanan | vulnerability | Kelemahan yang dapat disalahgunakan |
| Antimalware | antimalware | Software pendeteksi malware |
| Cadangan | backup | Salinan data untuk pemulihan |
| Di luar lokasi | offsite | Disimpan di tempat lain |
| Kunci layar | screen lock | Pengaman saat perangkat dibuka |
| Respons insiden | incident response | Langkah menanggapi kejadian keamanan |
| Etika | ethics | Prinsip bertindak benar |
