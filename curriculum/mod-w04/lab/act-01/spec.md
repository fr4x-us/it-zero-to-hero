---
activity_id: mod-w04.lab.act-01
component: mod-w04.lab
content_version: "1.0"
variants: [mod-w04.lab.act-01.vA, mod-w04.lab.act-01.vB]
competencies: [comp-w04-threat-01]
max_points: 30
estimated_minutes: 30
checks_file: checks.yaml
---

# Lab W4 · Aktivitas 1 — Mengenali Ancaman dari Skenario

## Tujuan

Menentukan jenis ancaman — atau menyatakan **bukan ancaman** — dari
sepuluh skenario sehari-hari.

## Prasyarat

Pelajaran 1 §2, Pelajaran 3 §1.

## Keamanan aktivitas

Semua skenario fiktif. Kamu hanya **membaca dan mengklasifikasi**; tidak
ada tautan yang dibuka, tidak ada akun atau perangkat nyata yang dipakai.

## Instruksi

Pilih satu kode untuk setiap skenario, lalu tekan **Serahkan** (dengan
konfirmasi).

| Kode | Arti |
|---|---|
| `PHI` | Phishing (pesan/situs penyamar yang memancing data lewat tautan atau formulir) |
| `SOS` | Rekayasa sosial langsung (telepon/tatap muka), bukan lewat tautan atau situs palsu |
| `TRO` | Trojan |
| `RAN` | Ransomware |
| `SPY` | Spyware |
| `WIF` | Wi-Fi palsu/mencurigakan (skenario memberi bukti perilaku, bukan hanya nama mirip) |
| `AMN` | Bukan ancaman (tindakan aman) |

Bila ciri tumpang-tindih, pilih kategori **utama** (Pelajaran 1 §2):
menyamar sebagai program berguna → `TRO`; memata-matai tanpa disebut
menyamar → `SPY`; mengunci + tebusan → `RAN`; pesan/situs/formulir penyamar
yang memancing data → `PHI`; manipulasi langsung tanpa tautan → `SOS`.

**Contoh terlihat (tidak dinilai):** "Kamu mengunci layar ponsel dengan
PIN sebelum meninggalkannya di meja" → `AMN`.

## Data (fixture, urutan tampil tetap)

**Varian A**

| ID | Skenario |
|---|---|
| S1 | SMS: "Selamat! Kamu menang Rp5.000.000. Klaim di tautan dan isi nomor rekening serta PIN-mu." |
| S2 | Pemberitahuan pembaruan sistem muncul di menu Pengaturan ponsel, dan kamu memasangnya dari menu Pengaturan itu. |
| S3 | Orang tak dikenal di kantin meminjam ponselmu "untuk menelepon", lalu memintamu membacakan kode yang baru masuk. |
| S4 | Aplikasi yang tampak seperti "kalkulator gratis" dari situs unduhan tak resmi ternyata diam-diam memasang program jahat yang membuka akses dari jarak jauh. |
| S5 | Semua berkas di flashdisk klub berganti ekstensi menjadi `.kunci`, dan ada berkas berisi permintaan tebusan. |
| S6 | Di kafe muncul Wi-Fi terbuka "Kafe_Gratis_Free", padahal kasir menyebut Wi-Fi resmi bernama "KafeSenja" dengan sandi tertulis di struk. Setelah tersambung ke "Kafe_Gratis_Free", muncul halaman yang meminta kata sandi akun emailmu agar internet aktif. |
| S7 | Email "tim keamanan" berkata akunmu diblokir dalam 2 jam; tautannya menuju domain yang bukan milik penyedia akun. |
| S8 | Kamu membuka aplikasi bank resmi dari ikon aplikasi yang dipasang dari toko aplikasi resmi, lalu masuk dengan MFA. |
| S9 | Program tersembunyi di laptop bersama merekam setiap ketikan dan mengirimkannya ke server asing. |
| S10 | Guru mengumumkan sandi Wi-Fi sekolah diganti; sandi baru dibagikan lewat papan pengumuman resmi di ruang guru. |

**Varian B**

| ID | Skenario |
|---|---|
| S1 | Penelepon mengaku "petugas IT sekolah" dan meminta kata sandi akunmu untuk "migrasi data". |
| S2 | Aplikasi yang tampak seperti "game gratis" dari tautan chat ternyata juga memasang program jahat yang dapat mengendalikan ponsel. |
| S3 | Pesan WhatsApp "paket tertahan, bayar ongkir di tautan ini"; tautannya menuju domain yang bukan milik kurir. |
| S4 | Kamu memperbarui aplikasi lewat toko aplikasi resmi setelah ada pemberitahuan di toko itu. |
| S5 | Komputer laboratorium menampilkan "Berkas Anda dienkripsi. Kirim tebusan untuk mendapat kuncinya." |
| S6 | Ekstensi browser tersembunyi mencatat semua situs yang kamu buka dan mengirimkannya ke pihak asing. |
| S7 | Di stasiun muncul Wi-Fi "Stasiun-WiFi-Resmi" tanpa sandi yang meminta login akun email, padahal papan informasi menyebut nama Wi-Fi resmi yang lain. |
| S8 | Email meminta "verifikasi data rapor" lewat formulir di domain yang bukan milik sekolah. |
| S9 | Kamu masuk ke situs sekolah dengan mengetik sendiri alamat resminya dan memakai MFA. |
| S10 | Aplikasi bank resmi memberi tahu ada login dari perangkat baru, dan kamu memeriksanya di aplikasi resmi itu. |

## Yang diserahkan

Sepuluh kode.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c10 | 3 poin per kode benar | 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong atau kode di luar daftar → 0 untuk pemeriksaan itu; lainnya tetap
dinilai. Gangguan sistem → evaluasi diulang tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per skenario dan ciri yang menentukan jenisnya.

## Remedial

Varian lain menurut VA-2; materi remedial R-THREAT.
