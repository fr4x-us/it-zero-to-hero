# IT ZERO → HERO — Spesifikasi Kalender Jepang dan Dataset Hari Libur

Status: PERSIAPAN · dokumentasi saja · O-05 punya arah APPROVED, detail
tetap **OPEN**. Tanggal pemeriksaan sumber: **2026-11-23**.

Dokumen ini menjabarkan langkah 5 urutan persiapan Batch 02 (TD:64):
*holiday dataset/update specification*. Tidak ada keputusan LOCKED yang
diubah.

## 0. Label

| Label | Arti |
|---|---|
| **APPROVED** | Blueprint (`BL:n`) atau Batch 02 (`TD:n`). |
| **VERIFIED** | Dikonfirmasi dari sumber resmi yang benar-benar terbaca di sesi ini. |
| **PROPOSED** | Usulan dokumen ini; perlu persetujuan owner. |
| **OPEN** | Belum diputuskan atau belum terverifikasi. |

Butir dari [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md)
(`B01 M-xx`) ditandai PROPOSED karena status persetujuannya menunggu
konfirmasi owner (blocker B-3).

## 1. Keputusan yang sudah ada

| ID | Isi | Status | Sumber |
|---|---|---|---|
| J-01 | Zona waktu Asia/Tokyo. | APPROVED | BL:52 |
| J-02 | Hari libur nasional Jepang dan hari libur pengganti. | APPROVED | BL:53 |
| J-03 | Presentasi kalender Jepang. | APPROVED (detail OPEN) | BL:54 |
| J-04 | Hari kerja perusahaan dibedakan dari hari libur nasional. | APPROVED | BL:55 |
| J-05 | Penjadwalan belajar fleksibel. | APPROVED | BL:56 |
| J-06 | Jam tenang 22:00–07:00 JST. | APPROVED | BL:57 |
| J-07 | Dataset hari libur Jepang tersedia offline + proses pembaruan terkontrol; menangani libur pengganti dan *citizens' holidays*. Sumber, rentang tahun, mekanisme pembaruan OPEN. | APPROVED (arah) | TD:23 |
| J-08 | Minggu dan hari libur nasional merah, Sabtu biru; termasuk libur pengganti dan *citizens' holiday*. | PROPOSED (B01 M-12, B-3) | B01 M-12 |
| J-09 | Jadwal belajar mulai Januari 2027; default akhir pekan 4 jam/hari; dapat disesuaikan dengan shift; pengingat sesi belum selesai tiap 60 menit, tunduk izin Android. | PROPOSED (B01 M-14, B-3) | B01 M-14 |
| J-10 | Sumber/impor kalender perusahaan dan asumsi hari kerja default. | OPEN | B01 M-13 |

Gate terkait: [`QUALITY_GATES.md`](QUALITY_GATES.md) CL-1–CL-6.

## 2. Sumber resmi

| Kode | Sumber | Status akses di sesi ini |
|---|---|---|
| H1 | Kantor Kabinet Jepang (内閣府), "国民の祝日について": https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html | **Diblokir** (jaringan); hanya cuplikan via hasil pencarian |
| H2 | Data CSV resmi Kantor Kabinet: https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv | **Diblokir**; tidak terbaca |
| H3 | 国民の祝日に関する法律 (UU No. 178 Tahun 1948) di e-Gov: https://laws.e-gov.go.jp/law/323AC1000000178 | **Diblokir** |
| H4 | Terjemahan resmi UU di Japanese Law Translation (versi s.d. revisi UU No. 57/2018) | **Diblokir**; hanya cuplikan via hasil pencarian |
| H5 | Android `android.icu.util.JapaneseCalendar`: https://developer.android.com/reference/android/icu/util/JapaneseCalendar | Terbaca (Last updated 2026-08-03) |
| H6 | Android `java.time.ZoneId`: https://developer.android.com/reference/java/time/ZoneId | Terbaca (Last updated 2026-08-03) |

Karena H1–H4 tidak terbaca langsung, **tidak ada tanggal libur yang
ditandai VERIFIED** di dokumen ini. Tanggal contoh di §7 berasal dari
cuplikan pencarian (cuplikan H1 dan sumber sekunder) dan **wajib**
dicocokkan dengan H2 sebelum dipakai sebagai fixture uji.

## 3. Aturan hari libur

| ID | Aturan | Status |
|---|---|---|
| R-01 | Hari libur nasional (国民の祝日) ditetapkan UU H3. | Sumber diketahui; teks belum terbaca (OPEN-VERIFY) |
| R-02 | **Hari libur pengganti (振替休日, UU Pasal 3 ayat 2):** bila hari libur nasional jatuh pada hari Minggu, hari berikutnya yang bukan hari libur nasional menjadi hari libur. Contoh dari cuplikan: 3 Mei 2026 (Minggu) → libur pengganti 6 Mei 2026 (karena 4 dan 5 Mei sudah libur). | Isi dari cuplikan H1/H4; OPEN-VERIFY terhadap teks H3 |
| R-03 | **Citizens' holiday (国民の休日, UU Pasal 3 ayat 3):** hari biasa yang diapit dua hari libur nasional menjadi hari libur. Contoh dari cuplikan: 22 September 2026 (antara 21 dan 23 September). | Isi dari cuplikan H1; OPEN-VERIFY |
| R-04 | Ada hari libur yang ditetapkan atau dipindahkan oleh UU khusus untuk tahun tertentu (asumsi berdasarkan pengetahuan umum; contoh tidak diverifikasi di sesi ini). | OPEN-VERIFY |
| R-05 | Tanggal Hari Ekuinoks Musim Semi/Gugur ditetapkan per tahun, bukan tanggal tetap (asumsi; belum diverifikasi di sesi ini). | OPEN-VERIFY |

**Implikasi desain (PROPOSED):** karena R-04 dan R-05, aplikasi tidak
menghitung hari libur dari rumus. Aplikasi memakai **daftar tanggal** dari
dataset resmi (H2). Aturan R-02/R-03 hanya dipakai sebagai **validasi
silang** saat dataset dibangun, bukan sebagai sumber kebenaran.

## 4. Hari libur nasional vs hari kerja perusahaan

Dua lapisan data terpisah (PROPOSED, dasar J-04):

| Lapisan | Isi | Sumber | Dapat diubah pengguna |
|---|---|---|---|
| L1 Hari libur nasional | Tanggal + nama + jenis (祝日 / 振替休日 / 国民の休日) | Dataset resmi (§5) | Tidak |
| L2 Kalender kerja pengguna | Hari kerja / libur perusahaan / shift | Input pengguna atau impor (J-10 OPEN) | Ya |

| Kasus | Tampilan L1 | Ketersediaan belajar (L2) |
|---|---|---|
| Hari libur nasional, pengguna libur | Merah (J-08) | Libur |
| Hari libur nasional, pengguna **masuk kerja** | Tetap merah sebagai hari libur nasional | Hari kerja (L2 menang untuk penjadwalan) |
| Hari biasa, libur perusahaan | Warna hari biasa | Libur |
| Sabtu, pengguna masuk shift | Biru (J-08) | Hari kerja |

Aturan (PROPOSED): L2 **tidak pernah** mengubah status L1; L2 hanya
memengaruhi penjadwalan belajar. Penjadwalan ulang tidak menghapus
pekerjaan yang sudah selesai (B01 §3).

## 5. Dataset: rentang, pembaruan, validasi offline

### 5.1 Rentang tahun (OPEN, dengan usulan)

| Kebutuhan | Dasar |
|---|---|
| Wajib mencakup seluruh periode belajar | Mulai Januari 2027, nominal 16 minggu (J-09, BL:15) |
| Usulan minimum: 2026–2028 | Mencakup periode belajar, penjadwalan ulang, dan riwayat terakhir (PROPOSED) |
| Rentang final | **OPEN** |

### 5.2 Format dataset (PROPOSED)

| Field | Keterangan |
|---|---|
| `dataset_version` | Versi dataset aplikasi |
| `source` | URL H2 dan tanggal unduh |
| `source_published` | Tanggal publikasi sumber (bila tersedia) |
| `year_from`, `year_to` | Rentang tahun yang **dijamin lengkap** |
| `entries[]` | `date` (ISO-8601, tanggal lokal Jepang), `name_ja`, `name_id` (OPEN), `type` (`national` / `substitute` / `citizens`) |
| `checksum` | SHA-256 atas `entries` |

Catatan: kolom H2 (format, encoding) belum dapat diperiksa di sesi ini
(**OPEN-VERIFY**).

### 5.3 Pembaruan terkontrol (OPEN, opsi)

| Opsi | Cara | Catatan |
|---|---|---|
| U-1 Bersama rilis aplikasi | Dataset dibundel sebagai aset; diperbarui saat rilis baru | Paling sederhana; tidak perlu jaringan atau izin. |
| U-2 Impor file dataset oleh pengguna | Pengguna memilih file lewat SAF | Butuh validasi tanda tangan/checksum; risiko file palsu. |
| U-3 Unduh otomatis | Aplikasi mengambil H2 | Butuh `INTERNET` (diizinkan untuk fitur opsional oleh D-08); kalender inti tetap harus berfungsi offline. Pilihan mekanisme tetap CO-2 (OPEN). |

PROPOSED: U-1 sebagai default. Pilihan final **OPEN**.

### 5.4 Validasi offline (PROPOSED)

| ID | Validasi saat build dataset dan saat aplikasi memuat |
|---|---|
| V-01 | Checksum cocok. |
| V-02 | Tidak ada tanggal ganda; semua tanggal dalam `year_from`–`year_to`. |
| V-03 | Setiap `substitute` jatuh setelah libur nasional hari Minggu sesuai R-02. |
| V-04 | Setiap `citizens` diapit dua libur nasional sesuai R-03. |
| V-05 | Untuk tanggal di luar rentang: aplikasi menampilkan "data hari libur belum tersedia", **tidak** menganggapnya hari kerja biasa. |
| V-06 | Dataset rusak saat dimuat → pakai dataset bawaan terakhir yang valid; laporkan ke pengguna. |

## 6. JST, pergantian tanggal, dan zona waktu

| ID | Aturan | Status |
|---|---|---|
| Z-01 | Semua perhitungan "hari ini", hari libur, jadwal, dan jam tenang memakai `ZoneId.of("Asia/Tokyo")` secara eksplisit, bukan zona perangkat. | APPROVED arah (BL:52, CL-1); cara PROPOSED |
| Z-02 | Waktu kejadian (attempt, autosave, tenggat) disimpan sebagai *instant* UTC; tanggal lokal diturunkan di Asia/Tokyo. | PROPOSED (selaras ASSESSMENT D-07) |
| Z-03 | Pergantian tanggal pada 00:00 JST. | PROPOSED |
| Z-04 | Jam tenang 22:00–07:00 JST melintasi tengah malam: aktif bila waktu JST ≥ 22:00 **atau** < 07:00. Batas tepat: 22:00 aktif, 07:00 tidak aktif. | APPROVED (rentang), interpretasi batas PROPOSED (CL-6) |
| Z-05 | Notifikasi yang jatuh di jam tenang ditahan/ditunda; perilaku rinci (tunda ke 07:00 atau batalkan) **OPEN** (M-14). | OPEN |
| Z-06 | Asia/Tokyo saat ini tanpa DST (asumsi, belum diverifikasi di sesi ini); desain tetap memakai aturan zona dari platform, bukan offset tetap +09:00. | PROPOSED |
| Z-07 | Era Jepang: `android.icu.util.JapaneseCalendar` menomori tahun berdasarkan era dan menangani pergantian era di tengah tahun (VERIFIED, H5). Label era yang ditampilkan dan format tanggal **OPEN** (M-12). | VERIFIED (platform), tampilan OPEN |
| Z-08 | Era baru di masa depan butuh pembaruan data ICU/platform; aplikasi tidak menebak nama era (A). | PROPOSED |

## 7. Acceptance criteria dan skenario pengujian

### 7.1 Acceptance criteria

| ID | Kriteria | Gate |
|---|---|---|
| AC-01 | Tanggal yang ditampilkan sebagai "hari ini" adalah tanggal JST, apa pun zona perangkat. | CL-1 |
| AC-02 | Seluruh tanggal dataset untuk rentang yang didukung identik dengan H2. | CL-2 |
| AC-03 | Libur pengganti dan *citizens' holiday* diberi jenis yang benar. | CL-2 |
| AC-04 | Kalender kerja pengguna tidak mengubah status hari libur nasional. | CL-4 |
| AC-05 | Warna dan label sesuai keputusan presentasi yang disetujui. | CL-5 |
| AC-06 | Tidak ada notifikasi 22:00–06:59:59 JST; notifikasi pada 07:00:00 diperbolehkan. | CL-6 |
| AC-07 | Tanggal di luar rentang dataset ditandai "belum tersedia". | V-05 |
| AC-08 | Dataset rusak tidak membuat aplikasi crash dan tidak menghapus jadwal. | V-06 |

### 7.2 Skenario (Given–When–Then, bukan test executable)

Tanggal contoh **wajib diverifikasi terhadap H2** sebelum dipakai.

| ID | Given | When | Then |
|---|---|---|---|
| K-01 | Zona perangkat Asia/Jakarta (UTC+7), pukul 23:30 WIB tanggal 1 | Buka kalender | "Hari ini" = tanggal 2 (01:30 JST) |
| K-02 | Dataset 2026 | Lihat 6 Mei 2026 | Ditandai libur pengganti (contoh R-02) |
| K-03 | Dataset 2026 | Lihat 22 September 2026 | Ditandai *citizens' holiday* (contoh R-03) |
| K-04 | Dataset 2027 | Lihat 22 Maret 2027 | Ditandai libur pengganti (cuplikan sekunder: ekuinoks 21 Maret 2027 jatuh hari Minggu) |
| K-05 | Libur nasional dan pengguna menandai hari itu sebagai hari kerja | Buka kalender dan jadwal | Tanggal tetap merah; jadwal belajar memperlakukannya sebagai hari kerja |
| K-06 | Waktu 21:59:59 JST | Ada pengingat | Notifikasi boleh tampil |
| K-07 | Waktu 22:00:00 JST | Ada pengingat | Tidak tampil (ditahan sesuai Z-05) |
| K-08 | Waktu 06:59:59 JST | Ada pengingat | Tidak tampil |
| K-09 | Waktu 07:00:00 JST | Ada pengingat yang ditahan | Boleh tampil |
| K-10 | Tanggal di luar `year_to` | Buka bulan itu | Banner "data hari libur belum tersedia" |
| K-11 | File dataset rusak (checksum salah) | Aplikasi start | Memakai dataset valid terakhir; tidak crash |
| K-12 | Pengguna mengubah zona perangkat saat aplikasi berjalan | Kembali ke kalender | Tanggal dan jam tenang tetap berbasis JST |

## 8. Risiko

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Sumber resmi H1–H3 diblokir dari sesi ini | Tanggal belum terverifikasi | Verifikasi dari H2 di lingkungan lain sebelum dataset dibuat (B-8) |
| Pemerintah menambah/memindahkan hari libur setelah rilis | Kalender salah | Pembaruan terkontrol (§5.3); tampilkan versi dataset |
| Dataset dihitung dari rumus | Salah untuk tahun dengan UU khusus | Pakai daftar resmi (§3) |
| Memakai zona perangkat | Tanggal dan jam tenang salah saat pengguna bepergian | Z-01 |
| Offset tetap +09:00 | Salah bila aturan zona berubah | Z-06 |
| Pengingat 60 menit vs batas Android (izin notifikasi, alarm presisi, Doze) | Pengingat tidak muncul tepat waktu | Diputuskan bersama Z-05 (OPEN, B01 M-14) |
| Status Batch 01 belum dikonfirmasi | J-08, J-09 bisa berubah | Konfirmasi B-3 |

## 9. Keputusan OPEN

| ID | Keputusan | Rujukan |
|---|---|---|
| CO-1 | Rentang tahun dataset final | O-05, §5.1 |
| CO-2 | Mekanisme pembaruan U-1 / U-2 / U-3 | O-05, O-02, §5.3 |
| CO-3 | Verifikasi format dan isi H2 (memerlukan akses ke `www8.cao.go.jp`) | B-8 |
| CO-4 | Sumber/impor kalender perusahaan dan default hari kerja | J-10, B01 M-13 |
| CO-5 | Label era dan format tanggal Jepang; bahasa nama hari libur (Jepang/Indonesia) | M-12, Z-07 |
| CO-6 | Perilaku notifikasi saat jam tenang (tunda/batalkan) dan pengingat 60 menit vs batas Android | M-14, Z-05 |
| CO-7 | Konfirmasi status B01 untuk J-08 (warna) dan J-09 (jadwal) | B-3 |
