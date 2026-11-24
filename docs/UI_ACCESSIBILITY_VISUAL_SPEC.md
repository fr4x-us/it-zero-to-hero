# IT ZERO → HERO — Spesifikasi UI, Aksesibilitas, dan Kualitas Visual

Status: PERSIAPAN · dokumentasi saja · belum ada UI, screenshot, atau uji
visual. Tanggal: **2026-11-23**.

Dokumen ini menjabarkan langkah 5 urutan persiapan Batch 02 (TD:64):
*UI accessibility/screenshot acceptance criteria*. Dokumen ini tidak
mendesain ulang UI yang disetujui dan tidak mengubah
[`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md).

## 0. Label

| Label | Arti |
|---|---|
| **APPROVED** | Blueprint (`BL:n`) atau Batch 02 (`TD:n`). |
| **VERIFIED** | Fakta dari sumber resmi yang terbaca di sesi ini, atau hasil hitungan yang dapat diulang. |
| **PROPOSED** | Usulan dokumen ini atau rincian B01 yang belum disetujui; perlu persetujuan owner. |
| **RECOVERED** | Hanya asal-usul historis: butir berasal dari [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) (B01). Bukan status persetujuan. |
| **OWNER APPROVED WITH CONDITIONS** | Disetujui owner melalui D-01 (PR #18) sebagaimana tertulis di kolom "Disetujui owner" B01 §7.1. Detail di kolom "Masih OPEN / PARTIAL" **tidak** ikut disetujui. Ditulis `OWNER APPROVED WITH CONDITIONS (D-01 M-xx)`. |
| **NOT VERIFIED** | Klaim yang masih menunggu bukti (uji, build, atau sumber resmi). |
| **OPEN** | Belum diputuskan. |

Sumber resmi:

| Kode | Sumber | Last updated |
|---|---|---|
| U1 | https://developer.android.com/guide/topics/ui/accessibility/apps | 2026-11-10 |
| U2 | https://developer.android.com/develop/ui/compose/accessibility | 2026-06-13 |

Tidak terbaca dari sesi ini (diblokir): `m3.material.io`, `www.w3.org`
(WCAG). Rasio kontras di §2.2 dihitung dengan rumus luminans relatif yang
umum dipakai WCAG; ambang yang dipakai adalah ambang U1.

## 1. Keputusan yang sudah ada

| ID | Isi | Status | Sumber |
|---|---|---|---|
| UI-01 | Colorful Academy, tema terang (*bright/light theme*). | APPROVED | BL:12, BL:67 |
| UI-02 | Lima tab utama: Home, Learn, Lab, Calendar, Progress. | APPROVED | BL:68–69, TD:25 |
| UI-03 | Pengaturan profil dan backup. | APPROVED | BL:70 |
| UI-04 | UI Android yang aksesibel, mudah dibaca, dan responsif. | APPROVED | BL:71 |
| UI-05 | Compose native; ikuti palet dan guardrail aksesibilitas/anti-generik Batch 01. Aset, tipografi, dan target terukur OPEN. | APPROVED (arah) | TD:25 |
| UI-06 | Navigation Compose untuk lima tab; satu modul `app`; UI state immutable + StateFlow. | APPROVED | TD:18–20 |
| UI-07 | Palet: ungu `#7565F5`, biru `#3B82F6`, hijau `#22C55E`, kuning `#FFB020`, merah muda `#FF6B91`. | OWNER APPROVED WITH CONDITIONS (D-01 M-17); semula PROPOSED | B01 M-17, TD:25 |
| UI-08 | Profil lewat avatar; onboarding 4 layar; tampilan pelajaran, kuis, ujian, hasil, XP/mastery/achievement, rapor akademik, pengaturan, backup/restore. | OWNER APPROVED WITH CONDITIONS (D-01 M-18): profil lewat avatar, onboarding empat layar, layar pendukung. Daftar rinci layar tetap PROPOSED | B01 M-18 |
| UI-09 | Guardrail anti-generik: Compose native (bukan dashboard web), palet dipakai secara semantik, hindari grid kartu berulang, gradien berlebih, emoji dekoratif, stock art generik, glassmorphism, animasi tanpa tujuan; validasi dengan screenshot ukuran perangkat nyata. | APPROVED arah (TD:25 merujuk guardrail Batch 01); RECOVERED (B01 §3); rincian penerapan PROPOSED | B01 §3, TD:25 |
| UI-10 | Target sentuh minimal 48dp × 48dp. | VERIFIED | U1 |
| UI-11 | Kontras teks: ≥ 4,5:1 untuk teks < 18sp (atau tebal < 14sp); ≥ 3:1 untuk teks lain. | VERIFIED | U1 |

Catatan nama tab: B01 M-18 memakai "Learning Journey, IT Lab,
Schedule/Calendar". Blueprint dan TD:25 memakai **Home, Learn, Lab,
Calendar, Progress**; nama blueprint yang berlaku (DECISIONS_LOG K-3).

## 2. Design system Colorful Academy

### 2.1 Peran semantik palet (PROPOSED)

| Warna | Peran usulan | Catatan |
|---|---|---|
| Ungu `#7565F5` | Merek / aksi utama | |
| Biru `#3B82F6` | Informasi, tautan, Sabtu di kalender (B01 M-12) | |
| Hijau `#22C55E` | Sukses, lulus, memenuhi ambang | Tidak boleh satu-satunya penanda status (lihat A-08) |
| Kuning `#FFB020` | Peringatan, XP/pencapaian | |
| Merah muda `#FF6B91` | Galat, belum lulus | Minggu/hari libur di kalender memakai "merah" (B01 M-12); apakah merah muda ini atau warna merah terpisah: **OPEN** |

Prinsip: warna akademik (lulus/belum lulus) dan warna gamifikasi (XP)
dipisahkan secara visual, sejalan dengan BL:49.

### 2.2 Temuan kontras (VERIFIED — hasil hitung)

| Warna | vs putih `#FFFFFF` | vs hitam `#000000` |
|---|---|---|
| Ungu `#7565F5` | 4,25 | 4,94 |
| Biru `#3B82F6` | 3,68 | 5,71 |
| Hijau `#22C55E` | 2,28 | 9,22 |
| Kuning `#FFB020` | 1,83 | 11,48 |
| Merah muda `#FF6B91` | 2,70 | 7,76 |

Implikasi:

- **Tidak satu pun** warna palet mencapai 4,5:1 dengan teks putih.
  Teks putih kecil di atas tombol ungu (4,25) **gagal** ambang U1.
- Hijau, kuning, dan merah muda dengan teks putih gagal bahkan ambang 3:1.
- Warna palet sebagai **teks** di atas latar putih hanya memenuhi 3:1
  untuk ungu dan biru (teks besar), dan gagal untuk hijau, kuning,
  merah muda.

Opsi (keputusan **OPEN**, palet tidak diubah di sini):

| Opsi | Isi |
|---|---|
| KC-1 | Teks gelap di atas isian palet (semua warna ≥ 4,5:1 dengan hitam). |
| KC-2 | Tambah token turunan (varian lebih gelap/terang) untuk teks dan isian, palet asli tetap sebagai identitas. Butuh persetujuan karena menambah warna. |
| KC-3 | Batasi warna palet pada elemen non-teks dan teks besar saja. |

### 2.3 Token lain (OPEN)

Tipografi, skala spasi, bentuk sudut, ikon, ilustrasi, dan warna netral
(latar, permukaan, teks) belum diputuskan (TD:25, B01 M-17).

## 3. Navigasi dan struktur layar

### 3.1 Lima tab (APPROVED: nama dan jumlah; PROPOSED: isi)

| Tab | Tujuan utama (PROPOSED) | Informasi prioritas |
|---|---|---|
| Home | Ringkasan hari ini | Sesi berikutnya, tugas yang sedang berjalan (lanjutkan), progres minggu, pengingat |
| Learn | Perjalanan belajar 16 minggu | Fase → modul → pelajaran; status terkunci/terbuka/selesai (unlock linear, BL:21) |
| Lab | IT Lab offline | Lab Python/SQL/logika (BL:41–43); pekerjaan tersimpan; status runtime (O-04 OPEN) |
| Calendar | Kalender JST | Hari libur nasional, kalender kerja, jadwal belajar ([JAPAN_CALENDAR_HOLIDAY_SPEC.md](JAPAN_CALENDAR_HOLIDAY_SPEC.md)) |
| Progress | Nilai dan gamifikasi | Rapor akademik (4 komponen, ambang) **terpisah** dari XP/level/achievement |

Profil dan pengaturan backup dibuka dari avatar (OWNER APPROVED WITH CONDITIONS (D-01 M-18)).

### 3.2 Aturan navigasi (PROPOSED)

| ID | Aturan |
|---|---|
| N-01 | Tab bar selalu terlihat di layar tingkat atas; disembunyikan pada layar fokus (ujian berjalan, editor lab) — perilaku persis **OPEN**. |
| N-02 | Tombol Kembali sistem dan predictive back berfungsi; tidak ada alur yang memerlukan gesture khusus (§4, A-07). |
| N-03 | Keluar dari ujian berjalan tidak menghentikan timer (ASM:A-12); dialog konfirmasi menjelaskan hal itu. |
| N-04 | State setiap tab dipertahankan saat berpindah tab dan setelah process death. |

### 3.3 Layar utama dan hierarki (PROPOSED)

| Layar | Elemen wajib | Hierarki |
|---|---|---|
| Pelajaran | Judul, materi, diagram, navigasi antarbagian | Isi bacaan dominan; aksi sekunder tidak mengganggu |
| Kuis / ujian teori | Soal, pilihan, sisa waktu (ujian), simpan otomatis | Soal > sisa waktu > navigasi |
| Hasil | Skor tiap komponen tanpa pembulatan untuk keputusan, status, opsi remedial | Status lulus/belum lulus jelas tanpa bergantung warna |
| Editor lab | Editor, jalankan, output, test case | Editor dominan; output dapat diperbesar |
| Rapor akademik | 4 komponen, skor terbaik, ambang, riwayat attempt | Tabel/daftar yang terbaca TalkBack |
| Backup/restore | Ekspor, impor, pratinjau, konfirmasi | Peringatan kata sandi dan risiko jelas ([ENCRYPTED_BACKUP_RESTORE_SPEC.md](ENCRYPTED_BACKUP_RESTORE_SPEC.md) §6) |

Detail field setiap layar: **OPEN** (B01 M-18).

### 3.4 Komponen konsisten (PROPOSED)

Satu set komponen yang dipakai ulang: kartu modul, chip status (terkunci /
berjalan / selesai / lulus / belum lulus), indikator progres, banner
offline/galat, dialog konfirmasi, tampilan skor, item kalender. Setiap
komponen punya state: normal, ditekan, fokus, nonaktif, loading, galat.
Variasi visual antar-tab diizinkan secara sengaja (UI-09).

## 4. Aksesibilitas

| ID | Kriteria | Status |
|---|---|---|
| A-01 | Semua elemen interaktif punya label yang dibacakan TalkBack; ikon dekoratif diabaikan pembaca layar. | APPROVED arah (BL:71, AB-8); cara PROPOSED |
| A-02 | Target sentuh ≥ 48dp × 48dp. | VERIFIED (U1) |
| A-03 | Kontras teks memenuhi U1 (4,5:1 / 3:1); lihat temuan §2.2. | VERIFIED ambang; desain OPEN (KC-1–KC-3) |
| A-04 | Teks tetap terbaca dan tidak terpotong saat ukuran font sistem diperbesar; teks memakai satuan `sp`. Skala maksimum yang diuji: **OPEN**. | APPROVED arah (AB-8) |
| A-05 | Urutan fokus mengikuti urutan baca logis; judul ditandai sebagai heading. | PROPOSED |
| A-06 | Sisa waktu ujian diumumkan dengan wajar (tidak setiap detik); mode live-region **OPEN**. | PROPOSED |
| A-07 | Tidak ada fungsi yang hanya bisa diakses lewat gesture (swipe, long-press); selalu ada alternatif tombol. | PROPOSED |
| A-08 | Status tidak disampaikan hanya lewat warna (lulus/belum lulus, hari libur, kesalahan): selalu ada teks atau ikon. | PROPOSED |
| A-09 | Navigasi keyboard/D-pad dasar berfungsi (fokus terlihat). | PROPOSED |
| A-10 | Diagram dan ilustrasi pelajaran punya deskripsi teks. | PROPOSED |

## 5. Konfigurasi dan perangkat

| ID | Kriteria | Status |
|---|---|---|
| C-01 | Tema terang sebagai tema utama. | APPROVED (BL:12) |
| C-02 | **Dark mode:** blueprint menetapkan *bright/light theme*. Dukungan dark mode akan menambah keputusan produk dan **tidak** diasumsikan. Perilaku saat sistem dalam mode gelap (tetap terang, atau tema gelap terpisah): **OPEN**. | OPEN |
| C-03 | Rotasi layar tidak menghilangkan input, posisi gulir, atau state ujian/lab. | APPROVED arah (OF-4, ASM:P-04) |
| C-04 | Orientasi lanskap dan tablet: dukungan **OPEN** (B01 M-19); minimal tidak rusak/terpotong. | OPEN |
| C-05 | Ukuran layar: breakpoint **OPEN**; usulan uji pada ponsel kecil, ponsel umum, dan satu ukuran besar. | PROPOSED |
| C-06 | Perubahan konfigurasi lain (bahasa sistem, ukuran font, zona waktu) tidak menyebabkan kehilangan data; tanggal tetap JST. | PROPOSED |

## 6. UI state

| State | Kriteria (PROPOSED) |
|---|---|
| Loading | Indikator muncul hanya bila operasi terasa; tidak memblokir navigasi; tidak menampilkan layar kosong tanpa penjelasan. |
| Empty | Pesan + aksi berikutnya (mis. "Belum ada attempt — mulai kuis"). |
| Error | Pesan jelas dalam Bahasa Indonesia, tanpa jargon teknis; aksi coba lagi bila relevan; tidak kehilangan input. |
| Offline | Aplikasi offline-first: offline **bukan** galat. Hanya fitur opsional (video YouTube, BL:24) yang menampilkan keterangan tidak tersedia. |
| Recovery | Setelah crash/process death: banner "pekerjaan dipulihkan" dan langsung ke attempt yang berjalan (OF-5). |
| Progress | Progres belajar, sisa waktu ujian, dan progres ekspor/restore dapat dibaca TalkBack. |

Model state per layar: satu UI state immutable (TD:20).

## 7. Animasi, transisi, responsivitas, performa

| ID | Kriteria | Status |
|---|---|---|
| P-01 | Animasi punya tujuan (transisi, umpan balik), bukan dekorasi (UI-09). | PROPOSED |
| P-02 | Menghormati pengaturan sistem yang mengurangi/mematikan animasi. | PROPOSED |
| P-03 | Tidak ada pekerjaan berat (database, eksekusi Python, kripto) di thread UI; UI tetap responsif saat lab berjalan (LB-4). | PROPOSED |
| P-04 | Daftar panjang (riwayat attempt, kalender) di-scroll tanpa patah. | PROPOSED |
| P-05 | Target terukur (waktu start, frame, jank) dan alat ukurnya: **OPEN**. | OPEN |

## 8. Screenshot dan visual regression

Belum ada screenshot. Tidak ada klaim visual yang teruji.

| ID | Rencana (PROPOSED) |
|---|---|
| S-01 | Screenshot hanya dari build nyata atau test screenshot otomatis, bukan mockup buatan (EV-1). |
| S-02 | Matriks: lima tab + layar §3.3 × state §6 × font normal dan besar × ponsel kecil dan umum × potret (lanskap/tablet sesuai C-04). |
| S-03 | Data uji tetap (tanpa waktu nyata/acak); jam dibekukan pada tanggal JST tetap. |
| S-04 | Alat screenshot test dan baseline: **OPEN** (O-16). |
| S-05 | Perubahan screenshot ditinjau manusia di PR; perbedaan tak disengaja = FAIL. |
| S-06 | Pemeriksaan aksesibilitas otomatis dan manual TalkBack per milestone UI. |

## 9. Matriks acceptance criteria

| ID | Kriteria | Cara verifikasi | Gate |
|---|---|---|---|
| AC-01 | Lima tab dengan nama blueprint | Compose test + screenshot | AB-7 |
| AC-02 | Tema terang Colorful Academy | Screenshot | AB-7 |
| AC-03 | Semua elemen interaktif berlabel | Compose test semantics + TalkBack manual | AB-8 |
| AC-04 | Target sentuh ≥ 48dp | Pemeriksaan otomatis/manual | AB-8 |
| AC-05 | Kontras teks memenuhi U1 | Pemeriksaan kontras per token | AB-8 |
| AC-06 | Font besar tidak memotong teks penting | Screenshot font besar | AB-8 |
| AC-07 | Status tidak hanya dengan warna | Review + screenshot grayscale | AB-8 |
| AC-08 | Rotasi tidak menghilangkan state | Compose/instrumented test | OF-4 |
| AC-09 | State loading/empty/error/recovery ada untuk setiap layar utama | Screenshot per state | AB-7 |
| AC-10 | Nilai akademik dan XP terpisah secara visual | Review | GR-8 |

## 10. Skenario Given–When–Then (bukan test executable)

| ID | Given | When | Then |
|---|---|---|---|
| G-01 | TalkBack aktif di Home | Geser fokus ke semua elemen | Setiap elemen interaktif dibacakan dengan label yang bermakna |
| G-02 | Ukuran font sistem maksimum yang diuji | Buka layar Hasil | Skor, status, dan tombol remedial terbaca tanpa terpotong |
| G-03 | Ujian berjalan | Rotasi layar | Jawaban dan sisa waktu tetap; fokus tidak hilang |
| G-04 | Lab berjalan dengan loop panjang | Ketuk tab lain | UI responsif; lab tetap berjalan/terhenti sesuai LB-4 |
| G-05 | Tidak ada koneksi | Buka modul dengan video opsional | Materi inti tampil; video ditandai tidak tersedia |
| G-06 | Process death saat lab | Buka aplikasi | Banner pemulihan; kode dikembalikan |
| G-07 | Layar Hasil "belum lulus" | Lihat dalam grayscale | Status tetap terbaca lewat teks/ikon |
| G-08 | Tombol dengan teks putih di atas ungu | Cek kontras | Gagal U1 (4,25 < 4,5) → harus memakai opsi KC yang disetujui |
| G-09 | Pengguna hanya memakai tombol (tanpa swipe) | Selesaikan satu pelajaran dan kuis | Semua langkah dapat diselesaikan |
| G-10 | Sistem dalam mode gelap | Buka aplikasi | Perilaku sesuai keputusan C-02 |

## 11. Daftar keputusan

### APPROVED
UI-01–UI-06; UI-07 (palet) dan UI-08 (avatar, onboarding empat layar, layar pendukung) — OWNER APPROVED WITH CONDITIONS (D-01); UI-09 arah (TD:25); C-01; ambang U1 (UI-10, UI-11 VERIFIED).

### PROPOSED (perlu persetujuan)
Peran semantik palet (§2.1), daftar rinci layar (UI-08), penerapan
guardrail (UI-09), isi tab (§3.1), aturan navigasi N-01–N-04, komponen (§3.4),
A-05–A-10, C-05–C-06, UI state (§6), P-01–P-04, S-01–S-06.

### OPEN
| ID | Keputusan |
|---|---|
| UO-1 | Solusi kontras palet: KC-1 / KC-2 / KC-3 |
| UO-2 | Dark mode vs *bright/light theme* (C-02) |
| UO-3 | Warna "merah" kalender: merah muda palet atau warna terpisah |
| UO-4 | Tipografi, spasi, bentuk, ikon, ilustrasi, warna netral |
| UO-5 | Lanskap, tablet, breakpoint, skala font maksimum yang diuji |
| UO-6 | Perilaku tab bar di layar fokus (N-01) |
| UO-7 | Target performa terukur dan alatnya (P-05) |
| UO-8 | Alat screenshot test dan baseline (S-04, O-16) |
| UO-9 | Detail field setiap layar (B01 M-18) |
| UO-10 | *(Selesai: palet oleh D-01 M-17; guardrail arah oleh TD:25.)* |

## 12. Keputusan owner D-14 dan D-15 (2026-11-24)

| Butir | Status |
|---|---|
| UO-1 | **Diputuskan (D-14)**: pasangan kontras sesuai [ACCESSIBILITY_COLOR_DECISION_SHEET.md](ACCESSIBILITY_COLOR_DECISION_SHEET.md) §4 dan §9; KC-1 + KC-2 terbatas |
| UO-2 / C-02 | **Diputuskan (D-15)**: tema terang saja (DM-1), Force Dark otomatis nonaktif, dynamic color nonaktif |
| UO-3–UO-9 | Tetap OPEN |
| Verifikasi | ACC:AT-1–AT-6 dan AC-01–AC-10 di dokumen ini tetap NOT VERIFIED (UW-56) |
