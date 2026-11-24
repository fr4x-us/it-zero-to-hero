---
component: mod-w02.project
content_version: "1.0"
competencies: [comp-w02-os-01, comp-w02-proc-01, comp-w02-fs-01, comp-w02-path-01, comp-w02-ops-01, comp-w02-perm-01]
max_points: 100
estimated_minutes: 90
rubric_file: rubric.yaml       # pemeriksaan, kunci K4, dan contoh evaluasi; tidak ditampilkan kepada pelajar sebelum dinilai
rubric_model: MR-A (60/20/10/10, D-33)
remedial: MPV-A — attempt baru dapat dimulai dari salinan submission sebelumnya (D-30)
---

# Mini-project W2 — Menata Folder Proyek Sains

## Skenario

Bima mengunduh semua bahan tugas kelompok **Proyek Sains** ke folder
`/home/bima/Unduhan`, bercampur dengan berkas lain. Ia memintamu menata
berkas proyek ke struktur folder yang rapi memakai **simulator pohon
folder** di aplikasi, lalu menuliskan beberapa path untuk laporan
kelompok.

## Tujuan belajar

Menerapkan tujuan W2: fungsi OS (LO1), proses (LO2), jenis berkas dan
pohon folder (LO3), path absolut dan relatif (LO4), operasi berkas (LO5),
dan izin akses (LO6).

## Keadaan awal (informasi awal)

Folder `/home/bima/Unduhan` berisi 12 berkas:

| No. | Nama berkas |
|---|---|
| 1 | `sains-laporan.docx` |
| 2 | `lagu-favorit.mp3` |
| 3 | `sains-grafik.png` |
| 4 | `sains-pengukuran.csv` |
| 5 | `undangan-ulang-tahun.pdf` |
| 6 | `sains-catatan.txt` |
| 7 | `sains-foto-akar.jpg` |
| 8 | `sains-suhu.xlsx` |
| 9 | `pemasang-game.exe` |
| 10 | `sains-daftar-pustaka.pdf` |
| 11 | `sains-sketsa.png` |
| 12 | `sains-kelembapan.csv` |

*Deskripsi tabel:* 12 nama berkas di folder Unduhan. Selain folder
`Unduhan`, folder `/home/bima` belum berisi folder lain.

## Kebutuhan Bima

| ID | Syarat |
|---|---|
| N1 | Buat folder `/home/bima/ProyekSains` dengan tiga subfolder bernama persis `dokumen`, `gambar`, dan `data` (huruf kecil) |
| N2 | **Berkas proyek** adalah berkas yang namanya diawali `sains-`. Setiap berkas proyek **dipindah** (bukan disalin) ke subfolder sesuai ekstensinya: `.docx`, `.pdf`, `.txt` → `dokumen`; `.jpg`, `.png` → `gambar`; `.csv`, `.xlsx` → `data` |
| N3 | Berkas yang **bukan** berkas proyek tetap di `/home/bima/Unduhan` |
| N4 | Jangan membuat folder lain, jangan menghapus, dan jangan mengganti nama berkas. *Yang dinilai hanya **keadaan akhir** pohon (folder tambahan, berkas hilang/berganti nama, salinan ganda). Langkah sementara yang sudah dibatalkan sebelum diserahkan (mis. dihapus lalu dipulihkan) tidak terlihat dan tidak dinilai* |

## Deliverable (di aplikasi)

| ID | Isian | Bentuk |
|---|---|---|
| F1 | Pohon folder akhir | Keadaan simulator setelah kamu membuat folder dan memindahkan berkas |
| F2 | Path absolut `sains-laporan.docx` di pohon akhirmu | Teks path |
| F3 | Path relatif terpendek dari folder kerja `/home/bima/ProyekSains/gambar` ke `sains-laporan.docx` | Teks path |
| F4 | Path relatif terpendek dari folder kerja `/home/bima/Unduhan` ke `sains-pengukuran.csv` | Teks path |
| F5 | Jumlah berkas di folder `/home/bima/ProyekSains/data` pada pohon akhirmu | Bilangan bulat |
| F6 | Lima soal penjelasan proyek | Pilihan tunggal (K4) |

## Instruksi

1. Di simulator, buat folder sesuai N1.
2. Tentukan berkas mana yang berkas proyek (N2) dan mana yang bukan (N3).
3. **Pindahkan** setiap berkas proyek ke subfolder yang sesuai.
4. Periksa pohon akhirmu: semua berkas proyek tertata, berkas lain tetap
   di Unduhan, tidak ada folder tambahan.
5. Isi F2–F5 berdasarkan pohon akhirmu, memakai aturan path W2
   (Pelajaran 3).
6. Jawab lima soal penjelasan (F6).
7. Tekan **Serahkan** (dengan konfirmasi).

## Contoh bentuk isian (bukan jawaban proyek)

Contoh ini memakai pohon **lain** (`/home/contoh`), sehingga tidak memberi
jawaban.

| Isian | Contoh bentuk yang benar | Dari pohon contoh |
|---|---|---|
| Path absolut | `/home/contoh/Resep/kue/bolu.txt` | Berkas `bolu.txt` di folder `kue` |
| Path relatif | `../kue/bolu.txt` atau `./../kue/bolu.txt` | Dari folder kerja `/home/contoh/Resep/sup` |
| Jumlah berkas | `4` atau `4 berkas` | Folder berisi empat berkas |

**Aturan menulis path.** Pakai `/`, huruf besar/kecil persis, tanpa spasi,
tanpa `/` di akhir. Path relatif tidak diawali `/` dan harus terpendek.

## Kesalahan umum yang membuat poin hilang

| Kesalahan | Akibat |
|---|---|
| Nama folder berbeda huruf (`Dokumen`, `Data`) atau salah tempat | Berkas di dalamnya dianggap di folder yang salah; pemeriksaan struktur gagal |
| Menyalin, bukan memindahkan | Berkas ganda: pemeriksaan penempatan berkas itu gagal |
| Memindahkan berkas bukan-proyek (mis. PDF yang tidak diawali `sains-`) | Pemeriksaan "berkas lain tetap di Unduhan" gagal |
| Menghapus atau mengganti nama berkas | Pemeriksaan N4 gagal |
| Membuat folder tambahan | Pemeriksaan N4 gagal |
| Path memakai `\`, diakhiri `/`, atau beda huruf | Isian path tidak sah |
| Path relatif ditulis absolut, atau memutar | Pemeriksaan path itu gagal |
| F5 ditulis dengan kata (`tiga`) | Isian angka tidak sah |
| Hanya mengisi path tanpa menata pohon | Pemeriksaan path bergantung pada berkas yang sudah dipindah ke `ProyekSains`; nilainya 0 |
| Centang "sudah selesai" tanpa menata pohon | 0 poin (MR-6) |

## Penilaian (MR-A, rincian di `rubric.yaml`)

| Kriteria | Poin | Isi |
|---|---|---|
| K1 Kebenaran fungsional | 60 | Penempatan setiap berkas proyek; berkas lain tetap di Unduhan; kebenaran F2, F3, F4, dan F5 terhadap pohon akhirmu |
| K2 Kelengkapan deliverable | 20 | Pohon memuat folder baru; F2–F5 terisi dengan **bentuk yang sah**. Kebenaran nilai dinilai di K1 |
| K3 Struktur dan format | 10 | Nama dan letak keempat folder persis; tanpa folder tambahan; tanpa berkas dihapus, disalin, atau diganti nama |
| K4 Penjelasan proyek | 10 | 5 soal × 2 poin (komposisi K-A) |
| **Total** | **100** | |

Kredit parsial per pemeriksaan. Isian yang tidak sah atau kosong membuat
pemeriksaan yang membutuhkannya bernilai 0; pemeriksaan lain tetap dinilai
(MR-2).

## Bukti yang dinilai

Hanya keadaan simulator (F1) dan isian F2–F6. Pernyataan "sudah selesai"
atau catatan bebas tidak dinilai (MR-6).

## Remedial

Attempt baru boleh dimulai dari salinan pohon dan isian sebelumnya
(MPV-A). Perbaiki pemeriksaan yang gagal sesuai umpan balik. Attempt lama
tetap tersimpan; skor terbaik dipakai (D-12).

## Durasi

90 menit (memahami kebutuhan 15, menata pohon 35, menulis path dan jumlah
20, memeriksa 5, soal penjelasan 15).
