# IT ZERO → HERO — Threat Model Backup Terenkripsi dan Acceptance Criteria Restore

Status: PERSIAPAN · dokumentasi saja · O-06 dan O-07 tetap **OPEN**.
Tanggal pemeriksaan sumber: **2026-11-23**.

Dokumen ini menjabarkan langkah 4 urutan persiapan Batch 02 (TD:63):
*backup threat model and restore acceptance criteria; do not choose
cryptographic parameters by guesswork*. Tidak ada algoritma atau parameter
yang dipilih final di sini. Keamanan **belum** terbukti; semua klaim
keamanan bergantung pada pengujian dan review di masa implementasi.

## 0. Label

| Label | Arti |
|---|---|
| **APPROVED** | Blueprint (`BL:n`) atau Batch 02 (`TD:n`). |
| **VERIFIED** | Fakta platform/standar yang terkonfirmasi dari sumber resmi di §1. Bukan bukti keamanan aplikasi. |
| **PROPOSED** | Usulan desain dokumen ini; perlu persetujuan owner. |
| **OPEN** | Belum diputuskan. |

Butir dari [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md)
(`B01 M-xx`) ditandai PROPOSED karena status persetujuannya masih
menunggu konfirmasi owner (blocker B-3).

## 1. Sumber

| Kode | Sumber resmi | Diakses / Last updated |
|---|---|---|
| K1 | https://developer.android.com/identity/data/autobackup | 2026-11-18 |
| K2 | https://developer.android.com/reference/javax/crypto/Cipher (tabel transformasi) | 2026-08-03 |
| K3 | https://developer.android.com/reference/javax/crypto/SecretKeyFactory (tabel algoritma) | 2026-08-03 |
| K4 | https://developer.android.com/training/data-storage/shared/documents-files (Storage Access Framework) | 2026-11-13 |
| K5 | https://developer.android.com/training/data-storage/app-specific | 2026-11-13 |
| K6 | OWASP Password Storage Cheat Sheet — sumber di `OWASP/CheatSheetSeries` (`cheatsheets/Password_Storage_Cheat_Sheet.md`, cabang `master`) | 2026-11-23 |

Tidak dapat diakses dari sesi ini (ditolak kebijakan jaringan):
`rfc-editor.org` (RFC 9106 Argon2, RFC 5116 AEAD), `datatracker.ietf.org`,
`csrc.nist.gov` (SP 800-38D GCM, SP 800-132 PBKDF). Pernyataan yang
seharusnya bersumber dari dokumen tersebut tidak ditulis sebagai VERIFIED.

## 2. Keputusan yang sudah ada

| ID | Isi | Status | Sumber |
|---|---|---|---|
| A-1 | Autosave dan crash recovery; local snapshots. | APPROVED | BL:60–61 |
| A-2 | Ekspor backup portabel terenkripsi kata sandi. | APPROVED | BL:62 |
| A-3 | Restore aman: pratinjau, konfirmasi, validasi, rollback, pelestarian riwayat percobaan. | APPROVED | BL:63–64 |
| A-4 | Bukti yang dibutuhkan sebelum memilih: threat model, envelope berversi, AEAD, KDF + parameter, integritas, rollback restore, uji pemulihan. AES-GCM/Argon2id hanya kandidat. | APPROVED (arah) | TD:46 |
| A-5 | Kebijakan backup OS Android (eksposur data sensitif, aturan ekstraksi/`allowBackup`) harus ditentukan. | APPROVED (arah), pilihan OPEN | TD:48 |
| A-6 | Tidak ada penggabungan otomatis riwayat nilai; kehilangan kata sandi membuat ekspor tidak dapat dipulihkan. | PROPOSED (B01 M-16, B-3) | B01 M-16 |
| A-7 | Kata sandi backup tidak disimpan, tidak di-log, tidak dikirim. | APPROVED (gate) | QG SC-2 |
| A-8 | Attempt *append-only*; restore mempertahankan riwayat; ledger XP ikut backup tanpa duplikasi. | PROPOSED | ASSESSMENT spec P-07, P-10, X-06 |

## 3. Threat model

### 3.1 Aset

| Aset | Mengapa penting |
|---|---|
| AS-1 Riwayat percobaan dan skor (semua komponen) | BL:34 mewajibkan seluruh riwayat disimpan. |
| AS-2 Skor terbaik dan status lulus | Menentukan unlock dan rapor. |
| AS-3 Ledger XP | Harus bebas duplikasi (TD:38). |
| AS-4 Progres belajar, pekerjaan lab tersimpan, jadwal | Pekerjaan pengguna. |
| AS-5 Profil pengguna | Data pribadi. |
| AS-6 Kata sandi backup dan kunci turunannya | Kebocoran = semua ekspor terbuka. |
| AS-7 Integritas database aplikasi saat restore | Restore gagal tidak boleh merusak data aktif. |

### 3.2 Batas kepercayaan

| Zona | Kepercayaan |
|---|---|
| Z1 Sandbox aplikasi (penyimpanan internal app) | Dipercaya (asumsi perangkat tidak di-root). |
| Z2 Lokasi pilihan pengguna via SAF (folder lokal, kartu SD, penyedia dokumen pihak ketiga) | **Tidak dipercaya**: file bisa disalin, dibaca, diubah. |
| Z3 Google Drive melalui Android Auto Backup | Di luar kendali aplikasi; enkripsi end-to-end hanya pada Android 9+ dengan PIN/pola/kata sandi layar (K1). |
| Z4 File impor dari mana pun | **Tidak dipercaya** sampai lolos validasi. |
| Z5 Pengguna pemilik kata sandi | Dipercaya untuk kerahasiaan, **bukan** untuk integritas nilai (lihat T-03). |

### 3.3 Asumsi keamanan

- AS-01 Perangkat tidak di-root dan tidak terinfeksi malware dengan akses ke sandbox aplikasi (di luar cakupan).
- AS-02 Penyerang dapat memperoleh salinan file ekspor dan mencoba menebak kata sandi secara offline tanpa batas.
- AS-03 Kekuatan kata sandi menentukan kekuatan backup; KDF hanya memperlambat tebakan.
- AS-04 Tidak ada server: tidak ada pemulihan kata sandi, tidak ada escrow kunci.

### 3.4 Ancaman

| ID | Ancaman | Dampak | Mitigasi (PROPOSED kecuali disebut) |
|---|---|---|---|
| T-01 | File ekspor dicuri; tebakan kata sandi offline | Kerahasiaan AS-1–AS-5 | KDF berbiaya tinggi + salt acak per ekspor; aturan kekuatan kata sandi (OPEN). |
| T-02 | Pihak ketiga mengubah isi file | Restore data palsu | AEAD: tag autentikasi gagal → tolak. Header ikut sebagai AAD. |
| T-03 | **Pengguna sendiri** mendekripsi, mengubah nilai, mengenkripsi ulang | Nilai tidak sah | **Tidak dapat dicegah** oleh enkripsi berbasis kata sandi pengguna: pemilik kata sandi dapat membuat file valid. Kunci tersembunyi di APK juga dapat diekstrak. Keputusan penerimaan risiko: **OPEN (owner)**. |
| T-04 | File berbahaya (parser exploit, bom dekompresi, path traversal) | Crash / kerusakan data | Batas ukuran, verifikasi tag **sebelum** parsing, staging di direktori privat, nama file internal tidak diambil dari arsip. |
| T-05 | Versi format lama/baru atau downgrade | Salah tafsir data | Versi format dan versi skema di header (AAD); tolak versi tak dikenal. |
| T-06 | Nonce dipakai ulang dengan kunci sama | Kebocoran kerahasiaan/integritas GCM | Salt baru per ekspor → kunci baru; nonce acak baru per enkripsi. Javadoc Android: "Use a different IV value for every encryption" (VERIFIED, K2). |
| T-07 | Kata sandi lupa | Ekspor tidak dapat dibuka | Diterima sebagai konsekuensi (A-6); peringatan eksplisit di UI. |
| T-08 | Kata sandi bocor ke log/crash report/clipboard | AS-6 | Tidak di-log (A-7); bersihkan buffer setelah derivasi; tidak disimpan. |
| T-09 | Penyimpanan penuh / tulis terputus saat ekspor | File rusak yang tampak valid | Tulis ke file sementara, verifikasi baca-ulang, baru dianggap selesai. |
| T-10 | Proses terputus saat restore | Database setengah ter-restore | Staging + snapshot pra-restore + jurnal restore (§6). |
| T-11 | Auto Backup mengunggah database tidak terenkripsi ke cloud / D2D | Eksposur AS-1–AS-5 di luar kendali | Keputusan O-07 (§7). |
| T-12 | Auto Backup memulihkan database lama setelah instal ulang | Riwayat tampak "hilang" atau tidak konsisten | Keputusan O-07 (§7). |
| T-13 | File ekspor disimpan di penyimpanan app-specific | Terhapus saat aplikasi di-uninstall (VERIFIED, K5) | Ekspor ke lokasi pilihan pengguna via SAF (K4). |

**Kesimpulan threat model:** enkripsi melindungi **kerahasiaan dan
integritas terhadap pihak ketiga**. Enkripsi ini **bukan** mekanisme
anti-kecurangan terhadap pemilik kata sandi (T-03).

## 4. Evaluasi kandidat kriptografi

### 4.1 Ketersediaan di platform Android (VERIFIED, K2–K3)

| Primitif | Transformasi Android | API level |
|---|---|---|
| AES-GCM | `AES/GCM/NoPadding` | 10+ |
| AES-256-GCM eksplisit | `AES_256/GCM/NoPadding` | 26+ |
| AES-GCM-SIV | `AES/GCM-SIV/NoPadding` | 30+ |
| ChaCha20-Poly1305 | `ChaCha20/NONE/Poly1305` | 28+ |
| PBKDF2-HMAC-SHA256 | `PBKDF2withHmacSHA256` | 26+ |
| PBKDF2-HMAC-SHA1 | `PBKDF2withHmacSHA1` | 10+ |
| Argon2id | **Tidak ada** di tabel `SecretKeyFactory` Android | — |

Implikasi: dengan `minSdk 24` (usulan Batch 04), `PBKDF2withHmacSHA256`
**tidak** tersedia di API 24–25 melalui platform. Argon2id selalu butuh
pustaka pihak ketiga. Keduanya memengaruhi O-06 dan minSdk (B-9).

### 4.2 Rekomendasi parameter dari OWASP (VERIFIED sebagai isi K6)

K6 ditulis untuk *password storage*; penerapannya ke derivasi kunci
backup adalah inferensi (PROPOSED).

| KDF | Parameter minimum menurut K6 |
|---|---|
| Argon2id | 19 MiB memori, 2 iterasi, paralelisme 1 |
| scrypt (bila Argon2id tidak tersedia) | N = 2^17, r = 8, p = 1 |
| PBKDF2 (bila butuh FIPS-140) | HMAC-SHA-256, ≥ 600.000 iterasi |

### 4.3 Matriks kandidat (keputusan **OPEN**)

| Kandidat | Kelebihan | Kekurangan / yang wajib diuji |
|---|---|---|
| C-1 Argon2id + AES-256-GCM (disebut B01) | KDF memory-hard; AES-GCM tersedia API 10+ | Butuh pustaka pihak ketiga (lisensi, ukuran, pemeliharaan); waktu derivasi di perangkat lemah; memori. |
| C-2 PBKDF2-HMAC-SHA256 + AES-256-GCM | Semua dari platform pada API 26+ | Tidak memory-hard; ≥ 600.000 iterasi (K6) perlu diukur waktunya; minSdk 24 bermasalah (§4.1). |
| C-3 scrypt + AES-256-GCM | Memory-hard | Pustaka pihak ketiga; parameter K6 perlu diukur di perangkat. |
| C-4 KDF terpilih + ChaCha20-Poly1305 | Cepat tanpa akselerasi AES | API 28+; perlu alasan memilih selain AES-GCM. |

Bukti yang dibutuhkan sebelum memilih (dari TD:46): pengukuran waktu dan
memori KDF di perangkat target, review pustaka, uji vektor, uji restore.

## 5. Format backup portabel (PROPOSED, semua nilai konkret OPEN)

### 5.1 Envelope

| Bagian | Isi | Dilindungi |
|---|---|---|
| Magic | Penanda format aplikasi | AAD |
| `format_version` | Versi envelope | AAD |
| `kdf_id` + parameter | Algoritma KDF dan biaya | AAD |
| `salt` | Acak, baru setiap ekspor (panjang OPEN) | AAD |
| `aead_id` + `nonce` | Algoritma AEAD dan nonce acak baru | AAD |
| `ciphertext` + `tag` | Payload terenkripsi | AEAD |

Seluruh header menjadi *associated data* sehingga perubahan header
menggagalkan dekripsi (T-02, T-05).

### 5.2 Payload

| Opsi | Kelebihan | Kekurangan |
|---|---|---|
| P-A Salinan file database SQLite | Sederhana | Terikat versi skema; perlu checkpoint WAL; sulit divalidasi per entitas. |
| P-B Ekspor logis (manifest + data per entitas, mis. JSON/CBOR) | Portabel antarversi skema; dapat divalidasi dan dihitung | Perlu pemetaan migrasi format. |

PROPOSED: P-B. Pilihan final **OPEN**.

Manifest payload (PROPOSED): versi skema data, versi aplikasi pembuat,
waktu ekspor (UTC), jumlah entitas per jenis (attempt, skor, ledger XP,
progres), dan hash per bagian untuk validasi pasca-dekripsi.

### 5.3 Alur ekspor (offline)

1. Pengguna memilih "Ekspor" dan memasukkan kata sandi dua kali (aturan
   kekuatan: OPEN).
2. Snapshot konsisten database dibaca dalam satu transaksi baca.
3. Payload dibuat → KDF dengan salt baru → AEAD dengan nonce baru.
4. File ditulis ke lokasi pilihan pengguna via `ACTION_CREATE_DOCUMENT`
   (VERIFIED, K4), sebagai file sementara lalu difinalkan bila
   memungkinkan.
5. **Verifikasi setelah tulis:** file dibaca ulang dan didekripsi di
   memori; manifest dicocokkan. Gagal → ekspor dinyatakan gagal.
6. Tidak ada jaringan di seluruh alur.

## 6. Restore aman

### 6.1 Alur (PROPOSED)

| Tahap | Aksi | Perubahan pada data aktif |
|---|---|---|
| R1 Pilih file | `ACTION_OPEN_DOCUMENT` (K4); cek ukuran maksimum (OPEN) | Tidak ada |
| R2 Baca header | Validasi magic, versi format, ID algoritma, parameter dalam batas | Tidak ada |
| R3 Dekripsi | KDF + AEAD; **plaintext tidak dipakai sebelum tag terverifikasi** | Tidak ada |
| R4 Validasi payload | Versi skema didukung; hash bagian cocok; jumlah entitas cocok manifest; referensi antarentitas konsisten | Tidak ada |
| R5 Staging | Muat ke database staging di direktori privat | Tidak ada |
| R6 Pratinjau | Tampilkan ringkasan: tanggal ekspor, jumlah attempt, skor terbaik, total XP, progres; bandingkan dengan data aktif | Tidak ada |
| R7 Konfirmasi | Konfirmasi eksplisit pengguna | Tidak ada |
| R8 Snapshot pra-restore | Simpan snapshot data aktif sebagai titik rollback | Tidak ada |
| R9 Terapkan | Satu transaksi atomik (atau pertukaran file database yang atomik); jurnal restore ditandai "berjalan" | Ya |
| R10 Verifikasi pasca-restore | Jumlah entitas dan hash cocok dengan staging; invarian §6.3 lolos | — |
| R11 Selesai / rollback | Lolos → jurnal "selesai", staging dihapus. Gagal → pulihkan snapshot R8 | — |

Saat aplikasi start dan jurnal restore berstatus "berjalan" (T-10):
lakukan rollback ke snapshot R8, laporkan ke pengguna.

### 6.2 Mode restore dan pelestarian riwayat — **OPEN (owner)**

Ada ketegangan antara dua aturan:

- BL:63–64: restore harus mempertahankan riwayat percobaan.
- B01 M-16: tidak ada penggabungan otomatis riwayat nilai.

Bila data aktif berisi attempt yang **tidak ada** di file backup, mode
"ganti total" akan menghilangkan attempt tersebut dari database aktif.
Opsi (tidak dipilih di sini):

| Opsi | Perilaku | Catatan |
|---|---|---|
| M-1 Ganti total + snapshot pra-restore disimpan | Riwayat lama tetap ada di snapshot, tetapi tidak di database aktif | Perlu kebijakan retensi snapshot. |
| M-2 Tolak restore bila data aktif punya attempt yang tidak ada di backup | Tidak ada riwayat hilang | Pengguna dapat terhalang. |
| M-3 Gabung berbasis ID stabil (append attempt yang belum ada) | Riwayat lengkap | Bertentangan dengan "no automatic merging" kecuali owner mengizinkan penggabungan eksplisit. |

### 6.3 Invarian data (acceptance criteria)

| ID | Invarian |
|---|---|
| I-01 | Setiap attempt punya ID stabil (PROPOSED); tidak ada dua attempt dengan ID sama setelah restore. |
| I-02 | Jumlah attempt setelah restore sesuai mode yang dipilih (§6.2) dan manifest; tidak ada attempt hilang tanpa jejak (tersimpan di database aktif atau snapshot). |
| I-03 | Skor terbaik setelah restore sama dengan maksimum dari attempt yang ter-restore (ASSESSMENT P-08). |
| I-04 | Ledger XP: paling banyak satu award per identitas aktivitas; total XP = jumlah entri ledger. |
| I-05 | Status lulus dan unlock konsisten dengan skor terbaik dan aturan A-02 (ASSESSMENT §6). |
| I-06 | Attempt yang sedang `IN_PROGRESS` di data aktif: perilaku saat restore **OPEN**. |

## 7. Interaksi dengan Android Auto Backup (O-07)

Fakta (VERIFIED, K1):

- Aplikasi yang menargetkan API 23+ otomatis ikut Auto Backup; default
  `android:allowBackup` = `true`.
- Data dicadangkan ke Google Drive pengguna, maks. 25 MB per aplikasi;
  hanya backup terbaru yang disimpan.
- Enkripsi end-to-end hanya pada Android 9+ dengan PIN/pola/kata sandi
  layar.
- Target Android 12+: aturan lewat `android:dataExtractionRules`; untuk
  Android 11 ke bawah diperlukan aturan terpisah.
- Pada sebagian produsen perangkat, `allowBackup="false"` menonaktifkan
  backup cloud tetapi **tidak** menonaktifkan transfer antarperangkat (D2D).

Opsi (keputusan **OPEN**):

| Opsi | Efek | Risiko |
|---|---|---|
| AB-1 `allowBackup=false` | Tidak ada salinan cloud | D2D mungkin tetap terjadi pada sebagian perangkat; pengguna hanya mengandalkan ekspor manual. |
| AB-2 Izinkan, kecualikan database dan snapshot lewat aturan ekstraksi | Preferensi ringan tetap ikut | Aturan harus diuji untuk cloud dan D2D, API ≤ 30 dan ≥ 31. |
| AB-3 Izinkan semua | Pemulihan otomatis saat ganti perangkat | Database tidak terenkripsi aplikasi ada di cloud; pada perangkat tanpa kunci layar tidak E2E; restore otomatis melewati alur §6. |

Catatan penyimpanan: file di penyimpanan app-specific terhapus saat
uninstall (VERIFIED, K5). Local snapshot (BL:61) di lokasi itu ikut
terhapus; ekspor manual harus disimpan di lokasi pilihan pengguna (K4).

## 8. Acceptance criteria kegagalan

| ID | Kondisi | Hasil yang diharapkan |
|---|---|---|
| F-01 | Kata sandi salah | Ditolak di R3; pesan umum ("kata sandi salah atau file rusak"); data aktif tidak berubah. |
| F-02 | File terpotong / rusak | Ditolak di R2 atau R3; data aktif tidak berubah. |
| F-03 | Satu byte ciphertext atau header diubah | Tag gagal; ditolak; data aktif tidak berubah. |
| F-04 | Versi format/skema lebih baru dari aplikasi | Ditolak dengan pesan versi; tidak ada parsing parsial. |
| F-05 | Versi lama yang didukung | Dimigrasikan di staging; divalidasi; lalu alur normal. |
| F-06 | Ruang penyimpanan habis saat ekspor | Ekspor gagal secara eksplisit; tidak ada file yang tampak valid tetapi rusak. |
| F-07 | Ruang penyimpanan habis saat staging/restore | Restore dibatalkan sebelum R9 atau di-rollback; data aktif utuh. |
| F-08 | Process death saat R1–R8 | Tidak ada perubahan data aktif; staging dibersihkan saat start. |
| F-09 | Process death saat R9–R10 | Saat start: rollback ke snapshot R8; pengguna diberi tahu. |
| F-10 | File sangat besar / bom dekompresi | Ditolak sebelum memori habis (batas OPEN). |
| F-11 | Parameter KDF di header di luar batas aman yang didukung | Ditolak (mencegah DoS dan downgrade). |
| F-12 | Ekspor dibatalkan pengguna | Tidak ada file parsial yang tertinggal sebagai backup valid. |

## 9. Matriks risiko

| Risiko | Kemungkinan | Dampak | Status mitigasi |
|---|---|---|---|
| T-03 pengguna memalsukan nilai lewat backup | Sedang | Tinggi (integritas akademik) | **Tidak dapat dimitigasi dengan kripto offline** → keputusan owner |
| T-01 tebakan kata sandi offline | Sedang | Tinggi | Bergantung KDF + kekuatan kata sandi (OPEN) |
| T-10 restore terputus | Rendah | Tinggi | Desain §6.1, perlu uji |
| §6.2 riwayat hilang saat restore | Sedang | Tinggi | Perlu keputusan mode |
| T-11/T-12 Auto Backup | Tinggi (default aktif) | Sedang–Tinggi | Perlu keputusan O-07 |
| T-06 nonce reuse | Rendah bila desain diikuti | Tinggi | Salt + nonce baru per ekspor; perlu uji |
| T-04 file berbahaya | Rendah | Sedang | Validasi bertahap; perlu uji fuzz |
| minSdk 24 vs PBKDF2-SHA256 (API 26+) | Pasti bila C-2 + minSdk 24 | Sedang | Keputusan O-06 + B-9 |
| Pustaka Argon2id/scrypt pihak ketiga | — | Sedang (rantai pasok) | Review lisensi/pemeliharaan |

## 10. Skenario pengujian (Given–When–Then, bukan test executable)

| ID | Given | When | Then | Gate |
|---|---|---|---|---|
| G-01 | Data berisi 120 attempt, 40 award XP | Ekspor lalu restore pada instal bersih | 120 attempt, 40 award, skor terbaik dan status lulus identik | SC-3, SC-4 |
| G-02 | File ekspor valid | Restore dengan kata sandi salah | Ditolak; data aktif tidak berubah | SC-3 |
| G-03 | File ekspor valid | Ubah 1 byte di header | Ditolak (tag gagal) | SC-1, SC-3 |
| G-04 | File ekspor valid | Ubah 1 byte di ciphertext | Ditolak | SC-1 |
| G-05 | File terpotong 50% | Restore | Ditolak; data aktif utuh | SC-3 |
| G-06 | Restore di tahap R9 | Force stop | Start berikutnya: rollback; data sama dengan sebelum restore | SC-3, OF-5 |
| G-07 | Penyimpanan hampir penuh | Ekspor | Gagal eksplisit; tidak ada file valid palsu | SC-1 |
| G-08 | Dua ekspor berturut-turut dengan kata sandi sama | Bandingkan header | Salt dan nonce berbeda | SC-1 |
| G-09 | File dari versi format lebih baru | Restore | Ditolak dengan pesan versi | SC-3 |
| G-10 | Ekspor dan restore | Periksa log aplikasi | Kata sandi tidak muncul | SC-2 |
| G-11 | Data aktif berisi attempt yang tidak ada di backup | Restore | Perilaku sesuai mode §6.2 yang disetujui; tidak ada attempt hilang tanpa jejak | SC-4 |
| G-12 | Aturan Auto Backup sesuai keputusan O-07 | Jalankan uji backup/restore cloud dan D2D | Data yang dikecualikan tidak ikut | SC-6 |

## 11. Keputusan yang memerlukan owner

| ID | Keputusan | Rujukan |
|---|---|---|
| OD-1 | Kandidat KDF + AEAD (C-1–C-4) dan parameternya setelah pengukuran | O-06, §4 |
| OD-2 | Penerimaan risiko T-03 (pemalsuan nilai oleh pemilik kata sandi) | §3.4 |
| OD-3 | Mode restore: M-1 / M-2 / M-3 | §6.2, BL:63–64, B01 M-16 |
| OD-4 | Kebijakan Auto Backup: AB-1 / AB-2 / AB-3 | O-07, §7 |
| OD-5 | Format payload P-A / P-B | §5.2 |
| OD-6 | Aturan kekuatan kata sandi | T-01 |
| OD-7 | Batas ukuran file impor dan biaya KDF maksimum yang diterima | F-10, F-11 |
| OD-8 | Retensi snapshot pra-restore dan local snapshot (frekuensi, jumlah) | B01 M-15 |
| OD-9 | Perlakuan attempt `IN_PROGRESS` saat restore | I-06 |
| OD-10 | minSdk final terhadap ketersediaan primitif (API 26+ untuk PBKDF2-SHA256) | B-9, §4.1 |
