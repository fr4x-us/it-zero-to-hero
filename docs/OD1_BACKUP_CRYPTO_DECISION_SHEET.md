# IT ZERO → HERO — Decision Sheet OD-1: Kriptografi Backup Terenkripsi

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode,
prototipe, atau benchmark. Tanggal: **2026-11-24**. Basis: `main` =
`b789e9a` (merge PR #21).

Rekomendasi di §7 adalah saran teknis, **bukan** keputusan. Tidak ada
algoritma atau parameter yang disetujui di sini. Keamanan **belum**
terbukti.

## 1. Keputusan yang sudah ada

| ID | Isi | Sumber |
|---|---|---|
| K-01 | Ekspor backup portabel terenkripsi kata sandi; pratinjau, konfirmasi, validasi integritas/versi, rollback, perlindungan riwayat | BL:62–64, D-01 M-16 |
| K-02 | Restore: BKP:M-2 default; BKP:M-1 hanya eksplisit dengan snapshot pra-restore yang dapat dipulihkan; tanpa merge riwayat nilai otomatis | D-03 |
| K-03 | Android Auto Backup dinonaktifkan; backup memakai mekanisme aplikasi sendiri | D-07 |
| K-04 | minSdk 29 | D-05 |
| K-05 | `INTERNET` diizinkan untuk fitur opsional; ekspor/impor backup tetap offline | D-08, BKP §5.3 |
| K-06 | Kandidat AES-GCM/Argon2id adalah kandidat, bukan parameter yang disetujui | TD:46 |

## 2. Sumber (diakses 2026-11-24 kecuali disebut lain)

| Kode | Sumber | Isi yang dipakai |
|---|---|---|
| C1 | developer.android.com — `javax.crypto.Cipher` (Last updated 2026-08-03; dibaca 2026-11-23) | `AES/GCM/NoPadding` API 10+; `AES_256/GCM/NoPadding` API 26+; `ChaCha20/NONE/Poly1305` API 28+; GCM-SIV API 30+; "Use a different IV value for every encryption" |
| C2 | developer.android.com — `SecretKeyFactory` (dibaca 2026-11-23) | `PBKDF2withHmacSHA256` API 26+; Argon2id tidak tercantum |
| C3 | developer.android.com — `GCMParameterSpec` (Last updated 2026-08-03) | Panjang tag GCM yang valid menurut spesifikasi: 128, 120, 112, 104, 96 (64/32 untuk aplikasi tertentu); merujuk NIST SP 800-38D |
| C4 | developer.android.com — `SecureRandom` (Last updated 2026-08-03) | "cryptographically strong random number generator" |
| C5 | developer.android.com — Android Keystore (Last updated 2026-11-23) | Kunci di Keystore *non-exportable*; dapat berada di secure hardware (TEE/StrongBox) |
| C6 | OWASP Password Storage Cheat Sheet (repo resmi `OWASP/CheatSheetSeries`) | Argon2id minimum 19 MiB, t=2, p=1; scrypt N=2¹⁷, r=8, p=1; PBKDF2-HMAC-SHA256 ≥ 600.000 iterasi |
| C7 | OWASP Cryptographic Storage Cheat Sheet (repo resmi) | "authenticated modes should always be used" (GCM/CCM); CSPRNG untuk kunci dan IV |
| C8 | Bouncy Castle `bc-java` (repo resmi): `Argon2BytesGenerator.java`, `LICENSE.html` | Implementasi Argon2 (termasuk `ARGON2_id`) ada; lisensi MIT |

Tidak dapat diakses dari sesi ini: NIST SP 800-38D, NIST SP 800-132,
RFC 9106 (Argon2), RFC 5116 (AEAD) — host `csrc.nist.gov` dan
`rfc-editor.org` diblokir. Pernyataan yang bergantung pada dokumen itu
tidak ditandai terverifikasi.

## 3. Kemampuan platform vs hal yang belum terverifikasi

| Butir | Status |
|---|---|
| AES-GCM tersedia di API 29 | **TERKONFIRMASI** (C1: API 10+) |
| AES-256-GCM eksplisit tersedia di API 29 | **TERKONFIRMASI** (C1: API 26+) |
| ChaCha20-Poly1305 tersedia di API 29 | **TERKONFIRMASI** (C1: API 28+) |
| PBKDF2-HMAC-SHA256 tersedia di API 29 | **TERKONFIRMASI** (C2: API 26+) |
| Argon2id di platform Android | **TIDAK ADA** (C2) |
| Argon2id lewat Bouncy Castle berjalan benar di Android API 29, ukuran APK, konflik dengan BC bawaan platform | **NOT VERIFIED** |
| Waktu dan memori KDF di perangkat target | **NOT VERIFIED** (benchmark tidak dijalankan; D-10/D-11) |
| Perilaku dekripsi GCM untuk payload besar (buffering sampai tag terverifikasi) | **NOT VERIFIED** |

## 4. Kandidat

### 4.1 Authenticated encryption (AEAD)

| Kandidat | Kelebihan | Kekurangan |
|---|---|---|
| E-1 AES-256-GCM | Platform API 29 (C1); mode terautentikasi yang direkomendasikan OWASP (C7); tag 128-bit didukung (C3) | Nonce **wajib** unik per kunci; penggunaan ulang nonce merusak kerahasiaan dan integritas |
| E-2 ChaCha20-Poly1305 | Platform API 28+ (C1); tidak bergantung akselerasi AES | Tidak ada keunggulan nyata bila AES dipercepat hardware (NOT VERIFIED per perangkat) |
| E-3 AES-GCM-SIV | Tahan penggunaan ulang nonce | API 30+ (C1) — **tidak** tersedia di minSdk 29 |

### 4.2 Password-based KDF

| Kandidat | Kelebihan | Kekurangan |
|---|---|---|
| P-1 Argon2id (Bouncy Castle, MIT) | Memory-hard; pilihan utama OWASP (C6) | Dependensi pihak ketiga; kompatibilitas/ukuran/kinerja NOT VERIFIED |
| P-2 PBKDF2-HMAC-SHA256 (platform) | Tanpa dependensi; tersedia API 29 (C2) | Tidak memory-hard; ≥ 600.000 iterasi (C6) — waktu di perangkat lemah NOT VERIFIED |
| P-3 scrypt (pustaka) | Memory-hard (C6) | Dependensi pihak ketiga; tidak lebih baik dari Argon2id menurut C6 |

## 5. Rancangan envelope berversi (PROPOSED)

| Bagian | Isi | Catatan |
|---|---|---|
| `magic` | Penanda format aplikasi | Menolak file bukan backup |
| `format_version` | Bilangan bulat | Untuk migrasi |
| `kdf_id` + `kdf_params` | mis. Argon2id (m, t, p) atau PBKDF2 (iterasi) | Disimpan agar bisa didekripsi di masa depan |
| `salt` | 16 byte acak dari `SecureRandom` (C4), baru setiap ekspor | Panjang final OPEN |
| `aead_id` | mis. AES-256-GCM | |
| `nonce` | 12 byte acak dari `SecureRandom`, baru setiap enkripsi | Salt baru per ekspor → kunci baru per ekspor; risiko tabrakan nonce di bawah kunci yang sama praktis dihilangkan |
| `header_len` | Panjang header | Batas maksimum untuk parsing aman |
| `ciphertext ‖ tag` | Payload terenkripsi + tag 128-bit (C3) | |

**Metadata terautentikasi:** seluruh header (magic sampai `header_len`)
menjadi *associated data* AEAD. Perubahan versi, parameter KDF, salt, atau
nonce menggagalkan dekripsi.

**Payload:** ekspor logis berisi manifest (versi skema, versi aplikasi,
waktu ekspor UTC, jumlah entitas, hash per bagian) — sesuai BKP §5.2
(format final OD-5 OPEN).

## 6. Penanganan kasus

| ID | Kasus | Perilaku yang diusulkan |
|---|---|---|
| H-1 | Kata sandi salah | Tag gagal → pesan umum "kata sandi salah atau file rusak"; tidak membedakan keduanya; data aktif tidak berubah |
| H-2 | File rusak / terpotong | Ditolak saat parsing header (panjang) atau saat verifikasi tag |
| H-3 | Input berbahaya | Parsing header dengan batas ketat **sebelum** KDF; tolak `kdf_params` di luar rentang yang diizinkan (mencegah DoS memori/waktu dan downgrade); batas ukuran file; plaintext tidak diproses sebelum tag terverifikasi; batas dekompresi; validasi skema di staging |
| H-4 | Migrasi format | Pembaca mendukung versi yang tercantum; ekspor selalu memakai versi terbaru; migrasi data dilakukan di staging setelah dekripsi |
| H-5 | Kebocoran data sensitif | Kata sandi diterima sebagai `CharArray` dan dibersihkan setelah KDF (upaya terbaik; JVM tidak menjamin); tidak ada kata sandi, kunci, salt+kunci, atau plaintext di log; file sementara hanya di penyimpanan privat aplikasi dan dihapus setelah selesai atau saat start berikutnya; tidak ada plaintext di lokasi SAF |
| H-6 | Offline | Seluruh enkripsi/dekripsi lokal; tanpa jaringan (K-05) |
| H-7 | Batas sumber daya | Biaya KDF minimum = rekomendasi OWASP (C6); batas atas memori/waktu ditetapkan setelah pengukuran di perangkat target (NOT VERIFIED) |

## 7. Rekomendasi (saran, bukan keputusan)

1. **AEAD: E-1 AES-256-GCM**, nonce acak 96-bit, tag 128-bit, header
   sebagai AAD. Alasan: tersedia di platform API 29, mode terautentikasi
   yang direkomendasikan, tidak menambah dependensi.
2. **KDF: P-1 Argon2id** dengan parameter minimum OWASP (19 MiB, t=2, p=1)
   sebagai lantai, **bersyarat** pada review dependensi Bouncy Castle dan
   uji kompatibilitas/kinerja setelah izin implementasi. **P-2
   PBKDF2-HMAC-SHA256 (≥ 600.000 iterasi)** sebagai cadangan bila
   dependensi ditolak atau tidak lolos uji.
3. Parameter final ditetapkan dari pengukuran nyata, bukan dari dokumen
   ini.

Risiko residual: kekuatan backup tetap bergantung pada kekuatan kata sandi
(aturan kata sandi = OD-6, OPEN); KDF hanya memperlambat tebakan.

## 8. Acceptance test di masa depan (NOT VERIFIED)

| ID | Uji |
|---|---|
| CT-1 | Vektor uji resmi untuk AES-GCM dan KDF terpilih lolos |
| CT-2 | Dua ekspor dengan kata sandi sama menghasilkan salt dan nonce berbeda |
| CT-3 | Satu bit diubah di header, ciphertext, atau tag → ditolak; data aktif utuh |
| CT-4 | File terpotong di berbagai titik → ditolak |
| CT-5 | `kdf_params` di luar rentang → ditolak sebelum KDF dijalankan |
| CT-6 | Kata sandi salah → pesan umum; tidak ada perubahan data |
| CT-7 | Ekspor di perangkat A, restore di perangkat B (API 29 dan versi terbaru) berhasil |
| CT-8 | Tidak ada kata sandi/kunci/plaintext di logcat |
| CT-9 | File sementara terhapus setelah sukses, gagal, dan process death |
| CT-10 | Waktu dan memori KDF di perangkat target dalam batas yang disetujui owner |

## 9. Pertanyaan untuk owner

1. **OD-1-Q1:** Setujui AES-256-GCM (nonce acak 96-bit, tag 128-bit, header sebagai AAD) sebagai AEAD?
2. **OD-1-Q2:** Setujui Argon2id via Bouncy Castle sebagai KDF utama (bersyarat review dependensi dan uji), dengan PBKDF2-HMAC-SHA256 ≥ 600.000 iterasi sebagai cadangan?
3. **OD-1-Q3:** Setujui parameter minimum OWASP sebagai lantai, dengan nilai final ditetapkan setelah pengukuran perangkat (butuh izin terpisah)?
4. **OD-1-Q4:** Setujui struktur envelope §5 (field dan AAD) sebagai dasar format?
5. **OD-1-Q5:** Setujui penanganan H-1–H-7?

Status: **AWAITING OWNER**. OD-1 (UW-15) tetap **BLOCKED**.
