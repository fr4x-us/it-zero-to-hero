---
component: mod-w04.project
content_version: "1.0"
competencies: [comp-w04-cia-01, comp-w04-threat-01, comp-w04-auth-01, comp-w04-phish-01, comp-w04-protect-01, comp-w04-incident-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W4 — Rencana Keamanan Akun Pribadi

## Skenario

Lina, siswi kelas 10, baru saja mengalami beberapa kejadian mencurigakan
dan ingin menyusun **rencana keamanan** untuk akun-akunnya serta cadangan
foto kegiatannya. Semua tokoh, akun, dan kejadian fiktif. Kamu **tidak**
membuka akun, tautan, atau perangkat nyata; kamu hanya mengisi formulir
rencana.

## Tujuan belajar

Menerapkan seluruh tujuan W4: tujuan keamanan (LO1), ancaman (LO2),
autentikasi (LO3), phishing (LO4), perlindungan dan cadangan (LO5), serta
respons insiden (LO6).

## Bagian A — Kejadian yang dialami Lina

Klasifikasikan setiap kejadian dengan kode: `PHI` phishing · `SOS`
rekayasa sosial langsung (telepon/tatap muka) · `TRO` trojan · `RAN`
ransomware · `SPY` spyware · `WIF` Wi-Fi palsu.

| ID | Kejadian |
|---|---|
| S1 | Email bernama tampilan "Admin Sekolah" meminta Lina memasukkan kata sandi lewat tautan yang domain terdaftarnya bukan milik sekolah |
| S2 | Penelepon mengaku petugas dompet digital dan meminta kode OTP yang baru masuk |
| S3 | Aplikasi "pengubah suara gratis" dari tautan chat diam-diam memasang program jahat |
| S4 | Wi-Fi "Perpus_Kota_Free" tanpa sandi muncul di samping Wi-Fi resmi "PerpusKota" yang sandinya tertera di meja layanan |
| S5 | Berkas di laptop adik Lina terkunci dan muncul permintaan tebusan |
| S6 | SMS "hadiah pulsa" meminta data kartu di situs tiruan |

## Bagian B — Akun Lina dan aturan rencana

| Akun | Dipakai untuk memulihkan akun lain? | Menyimpan uang? | Profil dapat dilihat publik? |
|---|---|---|---|
| E — Email sekolah | Ya | Tidak | Tidak |
| M — Media sosial | Tidak | Tidak | Ya |
| D — Dompet digital | Tidak | Ya | Tidak |
| G — Game daring (tanpa saldo uang) | Tidak | Tidak | Tidak |

Daftar tindakan:

| Kode | Tindakan |
|---|---|
| T1 | Kata sandi unik dan panjang (≥ 12 karakter atau frasa sandi) |
| T2 | Aktifkan MFA |
| T3 | Simpan sandi di pengelola kata sandi |
| T4 | Pakai sandi yang sama dengan akun lain agar mudah diingat |
| T5 | Bagikan OTP bila "petugas" memintanya |
| T6 | Pasang email/nomor pemulihan yang masih aktif |
| T7 | Periksa daftar perangkat/sesi yang masuk setiap bulan |
| T8 | Matikan notifikasi login agar tidak mengganggu |
| T9 | Batasi siapa yang dapat melihat profil |
| T10 | Simpan sandi di foto catatan di ponsel tanpa kunci layar |

Aturan rencana:

| ID | Aturan |
|---|---|
| AR-1 | **Setiap** akun wajib memilih T1 dan T6 |
| AR-2 | Akun yang **dipakai memulihkan akun lain** atau **menyimpan uang** juga wajib T2 |
| AR-3 | Akun dengan **profil publik** juga wajib T9 |
| AR-4 | **Tidak boleh** memilih tindakan berbahaya |
| AR-5 | Tindakan lain yang aman boleh ditambahkan |

## Bagian C — Cadangan foto kegiatan

Foto asli ada di **laptop Lina di rumah**. Pilih lokasi cadangan
tambahan (boleh lebih dari satu):

| Kode | Lokasi | Jenis media (model W4) | Tempat |
|---|---|---|---|
| L2 | Folder lain di laptop yang sama | Penyimpanan internal (perangkat yang sama) | Rumah |
| L3 | Harddisk eksternal | Harddisk/SSD eksternal | Rumah |
| L4 | Flashdisk | Flashdisk | Rumah |
| L5 | Layanan penyimpanan awan | Layanan awan | Di luar lokasi |
| L6 | Harddisk eksternal di rumah nenek | Harddisk/SSD eksternal | Di luar lokasi |

Gunakan aturan CB-1–CB-4 (Pelajaran 4 §2).

## Deliverable (formulir di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1 | Kode untuk S1–S6 | Pilihan dari daftar kode |
| F2 | Tindakan untuk akun E, M, D, G | Centang dari T1–T10 per akun |
| F3 | Lokasi cadangan tambahan | Centang dari L2–L6 |
| F4 | Jumlah salinan foto yang **dihitung** (CB-1–CB-4), termasuk asli, menurut pilihan F3 | Bilangan bulat |
| F5 | Jumlah **jenis media** berbeda yang dipakai (termasuk laptop) menurut pilihan F3 | Bilangan bulat |
| F6 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Instruksi

1. Klasifikasikan S1–S6 (Bagian A).
2. Untuk setiap akun, tentukan tindakan wajib dari AR-1–AR-3, hindari
   tindakan berbahaya (AR-4), dan boleh tambahkan tindakan aman lain.
3. Pilih lokasi cadangan sehingga memenuhi 3-2-1, lalu isi F4 dan F5
   sesuai pilihanmu.
4. Jawab lima soal penjelasan, lalu tekan **Serahkan** (dengan
   konfirmasi).

## Contoh bentuk isian (bukan jawaban proyek)

Contoh untuk akun **lain** (akun perpustakaan Budi dengan aturan sendiri),
sehingga tidak memberi jawaban.

| Isian | Contoh bentuk yang benar |
|---|---|
| Kode kejadian | `WIF` |
| Centang tindakan | `T1`, `T3`, `T6` |
| Centang lokasi | `L4` |
| Bilangan bulat | `2` atau `2 salinan` / `2 jenis` (bentuk saja) |

**Aturan menulis angka.** Bentuk terbaik angka saja (`3`). Bentuk dengan
kata satuan (`3 salinan`, `3 jenis`) tetap dibaca untuk pemeriksaan
kebenaran, tetapi kehilangan poin format. Kata (`tiga`), desimal, atau
tanda tidak dapat dibaca.

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Lupa tindakan wajib (mis. MFA untuk akun yang menyimpan uang) | Pemeriksaan "wajib" akun itu gagal |
| Memilih satu saja tindakan berbahaya | Pemeriksaan "larangan" akun itu gagal |
| Menghitung folder lain di laptop sebagai salinan | F4 salah; 3-2-1 mungkin tidak terpenuhi |
| Tidak ada salinan di luar lokasi | Pemeriksaan 3-2-1 gagal |
| Akun tanpa satu pun tindakan | Pemeriksaan akun itu dan kelengkapannya bernilai 0 |
| Centang "sudah selesai" tanpa isian | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | Klasifikasi S1–S6; tindakan wajib dan larangan per akun; cadangan 3-2-1; kebenaran F4 dan F5 terhadap pilihanmu |
| K2 Kelengkapan deliverable | 20 | Semua bagian terisi dengan **bentuk yang sah** |
| K3 Struktur dan format | 10 | Bagian A, B, C semuanya ada; F4 dan F5 hanya digit |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Kredit parsial per pemeriksaan; isian yang tidak sah membuat pemeriksaan
yang membutuhkannya bernilai 0, yang lain tetap dinilai (MR-2). Ada banyak
rencana yang benar; semua dinilai dengan aturan yang sama (MR-3).

## Bukti yang dinilai

Hanya isian F1–F6. Pernyataan "sudah aman" tidak dinilai (MR-6).

## Remedial

Attempt baru boleh dimulai dari salinan isian sebelumnya (MPV-A). Attempt
lama tetap tersimpan; skor terbaik dipakai (D-12).

## Durasi

90 menit (Bagian A 15, Bagian B 35, Bagian C 20, memeriksa 5, soal
penjelasan 15).
