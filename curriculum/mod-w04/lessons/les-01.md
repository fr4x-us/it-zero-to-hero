---
lesson_id: mod-w04.les-01
practice_id: mod-w04.prac-01
module_id: mod-w04
content_version: "1.0"
title: "Tujuan Keamanan dan Ancaman Umum"
language: id
duration_minutes: 45        # materi 33 + latihan terbimbing 12
competencies: [comp-w04-cia-01, comp-w04-threat-01]
prerequisites: [mod-w03]
accessibility:
  diagrams:
    - id: dg-w04-01
      alt: "Segitiga dengan tiga sudut: kerahasiaan, integritas, ketersediaan."
      long_description: >
        Sebuah segitiga. Sudut atas berlabel Kerahasiaan (hanya yang berhak
        dapat membaca). Sudut kiri bawah berlabel Integritas (tidak diubah
        tanpa izin). Sudut kanan bawah berlabel Ketersediaan (dapat dipakai
        saat dibutuhkan).
  tables_with_core_data: ["Tabel tiga tujuan keamanan", "Tabel jenis ancaman dan tandanya"]
  english_terms: [cybersecurity, confidentiality, integrity, availability, CIA triad, threat, malware, virus, trojan, ransomware, spyware, phishing, social engineering, rogue Wi-Fi]
---

# Pelajaran 1 — Tujuan Keamanan dan Ancaman Umum

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Menjelaskan tiga tujuan keamanan: **kerahasiaan**, **integritas**, dan
   **ketersediaan**.
2. Menentukan tujuan yang terganggu pada sebuah kejadian.
3. Mengenali ancaman umum — **phishing**, **rekayasa sosial**,
   **malware** (virus, trojan, ransomware, spyware), dan **Wi-Fi palsu** —
   dari tanda-tandanya.

## Mengapa ini penting?

Semua yang kamu pelajari di W1–W3 — perangkat, berkas, jaringan — dapat
disalahgunakan. **Keamanan siber** adalah usaha melindungi perangkat, data,
dan akun dari penyalahgunaan. Modul ini bersifat **defensif**: kita belajar
mengenali dan mencegah, bukan menyerang. Semua contoh fiktif.

## 1. Tiga tujuan keamanan (CIA)

```
            KERAHASIAAN
         (hanya yang berhak membaca)
              /\
             /  \
            /____\
 INTEGRITAS        KETERSEDIAAN
 (tidak diubah     (dapat dipakai
  tanpa izin)       saat dibutuhkan)
```

*Deskripsi diagram dg-w04-01:* segitiga dengan tiga sudut: kerahasiaan di
atas, integritas di kiri bawah, ketersediaan di kanan bawah.

| Tujuan | Artinya | Contoh gangguan |
|---|---|---|
| **Kerahasiaan** (*confidentiality*) | Data hanya dapat dibaca pihak yang berhak | Orang lain membaca isi percakapan pribadimu |
| **Integritas** (*integrity*) | Data tidak diubah tanpa izin dan tetap benar | Jumlah pada catatan keuangan klub diubah diam-diam |
| **Ketersediaan** (*availability*) | Data dan layanan dapat dipakai saat dibutuhkan | Aplikasi pemesanan tiket tidak dapat dibuka seharian |

*Model sederhana W4:* satu kejadian nyata dapat mengganggu lebih dari satu
tujuan. Di soal W4 kita menentukan tujuan yang **terutama** terganggu,
dan stem menjelaskan kejadiannya dengan cukup jelas.

## 2. Ancaman umum

**Ancaman** adalah sesuatu yang dapat merugikan keamanan. **Malware**
(*malicious software*) adalah software jahat.

| Ancaman | Ciri utama | Tanda yang dapat kamu lihat |
|---|---|---|
| **Phishing** | Pesan/situs **menyamar** sebagai pihak tepercaya untuk memancing data (kata sandi, OTP, data kartu) | Mendesak ("akun diblokir 1 jam lagi"), tautan ke domain aneh, meminta kata sandi/OTP |
| **Rekayasa sosial** (*social engineering*) | Memanipulasi **orang** agar menyerahkan akses atau informasi; phishing adalah salah satu bentuknya | Penelepon mengaku petugas dan meminta kode; orang asing meminta "pinjam" kartu akses |
| **Virus** | Menempel pada berkas/program dan menyebar saat berkas itu dijalankan | Berkas program berubah atau rusak; perilaku aneh setelah menjalankan berkas kiriman |
| **Trojan** | Program yang **tampak berguna** tetapi menyembunyikan fungsi jahat | Aplikasi "gratis" dari sumber tak resmi meminta izin berlebihan |
| **Ransomware** | Mengunci/mengenkripsi berkas lalu **meminta tebusan** | Berkas tidak dapat dibuka, ekstensi berubah, muncul pesan tebusan |
| **Spyware** | Diam-diam **memata-matai** dan mengirim aktivitasmu | Kuota data cepat habis, aplikasi tak dikenal, izin aksesibilitas yang tidak kamu berikan |
| **Wi-Fi palsu** | Jaringan Wi-Fi tiruan untuk **menyadap** atau mengarahkan ke situs palsu | Nama mirip Wi-Fi resmi **saja belum membuktikan** apa pun (bisa jaringan lain yang sah). Tanda lebih kuat: meminta kata sandi akun yang tidak berkaitan (email, media sosial) atau mengarahkan ke halaman login tiruan |

Tanda-tanda di atas adalah **tanda peringatan**, bukan bukti pasti;
perangkat juga dapat lambat karena alasan biasa. Yang penting: kenali pola
yang patut dicurigai, lalu ambil tindakan aman (Pelajaran 4).

**Kategori utama.** Satu kejadian nyata dapat cocok dengan beberapa
kategori (mis. aplikasi palsu yang juga memata-matai). Di soal W4, setiap
skenario memuat bukti perilaku, dan kamu memilih kategori **utama**
dengan aturan berurutan — pakai aturan **pertama** yang cocok:

1. Mengunci/mengenkripsi berkas + meminta tebusan → ransomware.
2. Program yang menyamar sebagai program berguna → trojan.
3. Program yang memata-matai tanpa disebut menyamar → spyware.
4. Jaringan Wi-Fi tiruan/mencurigakan dengan bukti perilaku, termasuk
   halaman peminta data yang muncul dari jaringan itu → Wi-Fi palsu.
5. Pesan/situs/formulir penyamar lewat email, SMS, chat, atau tautan yang
   memancing data → phishing.
6. Manipulasi langsung (telepon, tatap muka) tanpa tautan → rekayasa sosial.

Di dunia nyata satu kejadian bisa termasuk beberapa kategori sekaligus;
aturan ini hanya cara W4 memilih satu jawaban yang dinilai.

## 3. Contoh terbimbing

**Soal:** Tentukan ancaman dan tujuan keamanan yang terutama terganggu.

| Kejadian | Pertanyaan bantu | Ancaman | Tujuan terganggu |
|---|---|---|---|
| Pesan berisi "Kamu menang undian! Isi data kartumu di tautan ini" | Menyamar + memancing data? | Phishing | Kerahasiaan (data kartu) |
| Aplikasi "pengedit foto gratis" dari situs tak resmi ternyata mengirim isi galeri ke server asing | Tampak berguna, tersembunyi jahat? | Trojan | Kerahasiaan |
| Semua dokumen di komputer perpustakaan tidak dapat dibuka dan muncul pesan minta tebusan | Mengunci + tebusan? | Ransomware | Ketersediaan |

## 4. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Penipu selalu memakai bahasa yang buruk." | Banyak pesan phishing ditulis rapi dan memakai logo asli |
| "Hanya orang penting yang diserang." | Banyak serangan dikirim massal ke siapa saja |
| "Malware hanya ada di komputer, bukan ponsel." | Ponsel juga dapat terkena malware, terutama dari aplikasi tak resmi |
| "Keamanan hanya soal kerahasiaan." | Integritas dan ketersediaan sama pentingnya |

## 5. Latihan terbimbing (`mod-w04.prac-01`, tidak dinilai)

1. Tujuan apa yang terutama terganggu: (a) nilai ujian di sistem diubah
   orang yang tidak berhak, (b) daftar kontakmu dibaca orang asing.
2. Ancaman apa: (a) "petugas bank" menelepon dan meminta kode yang baru
   masuk ke ponselmu, (b) muncul pesan "berkasmu dikunci, bayar untuk
   membukanya".

## 6. Cek pemahaman (tidak dinilai)

- Mengapa trojan sulit dikenali?
- Beri satu contoh kejadian yang mengganggu ketersediaan.

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. (a) integritas, (b) kerahasiaan.
2. (a) rekayasa sosial, (b) ransomware.

## Ringkasan

- Tujuan keamanan: **kerahasiaan, integritas, ketersediaan**.
- Ancaman umum: phishing, rekayasa sosial, malware (virus, trojan,
  ransomware, spyware), Wi-Fi palsu — kenali dari ciri dan tandanya.
- W4 bersifat defensif; semua contoh fiktif.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Keamanan siber | cybersecurity | Perlindungan perangkat, data, dan akun |
| Kerahasiaan | confidentiality | Hanya yang berhak dapat membaca |
| Integritas | integrity | Tidak diubah tanpa izin |
| Ketersediaan | availability | Dapat dipakai saat dibutuhkan |
| Ancaman | threat | Sesuatu yang dapat merugikan keamanan |
| Software jahat | malware | Software yang dibuat untuk merugikan |
| Pengelabuan | phishing | Pesan/situs palsu untuk memancing data |
| Rekayasa sosial | social engineering | Memanipulasi orang agar memberi akses/informasi |
| Ransomware | ransomware | Malware pengunci berkas yang meminta tebusan |
| Spyware | spyware | Malware pemata-mata |
| Trojan | trojan | Program tampak berguna yang menyembunyikan fungsi jahat |
