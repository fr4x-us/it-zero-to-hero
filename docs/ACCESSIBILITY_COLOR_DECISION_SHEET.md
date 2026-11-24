# IT ZERO → HERO — Decision Sheet: Kontras Palet dan Strategi Dark Mode (UO-1 / UO-2)

Status: **OPEN — menunggu keputusan owner** · dokumentasi saja · tanpa kode.
Tanggal: **2026-11-23**. Basis: `main` = `6a805a1` (merge PR #20).

Lima warna merek **tidak diganti**. Rekomendasi di §6 adalah saran teknis,
**bukan** keputusan. Tidak ada strategi dark mode yang disetujui di sini.

## 1. Dasar

| ID | Isi | Status | Sumber |
|---|---|---|---|
| AC-B1 | Colorful Academy, tema terang (*bright/light theme*) | APPROVED | BL:12, BL:67 |
| AC-B2 | Palet: ungu `#7565F5`, biru `#3B82F6`, hijau `#22C55E`, kuning `#FFB020`, merah muda `#FF6B91`; aksesibilitas/kontras wajib diperhatikan | OWNER APPROVED WITH CONDITIONS (D-01 M-17) | B01 M-17 |
| AC-B3 | Kontras teks ≥ 4,5:1 untuk teks < 18sp, atau teks tebal < 14sp; ≥ 3:1 untuk teks lain, yaitu **teks besar** = teks ≥ 18sp, atau teks tebal ≥ 14sp. Teks tebal < 14sp tetap wajib 4,5:1 | VERIFIED (dokumentasi resmi) | developer.android.com/guide/topics/ui/accessibility/apps (Last updated 2026-11-10) |
| AC-B4 | Force Dark (Android 10): aplikasi ikut bila tema mengatur `android:forceDarkAllowed="true"`; atribut ini **sudah diset** pada semua tema terang bawaan sistem dan AndroidX (mis. `Theme.Material.Light`) | VERIFIED (dokumentasi resmi) | developer.android.com/develop/ui/views/theming/darktheme (Last updated 2026-10-28) |
| AC-B5 | Dynamic color tersedia di Android 12+; bila dipakai, skema warna diturunkan dari wallpaper | VERIFIED (dokumentasi resmi) | developer.android.com/develop/ui/compose/designsystems/material3 (Last updated 2026-11-10) |
| AC-B6 | Accessibility Scanner dan UI Check Mode Android Studio mendeteksi kontras rendah | VERIFIED (dokumentasi resmi) | developer.android.com/guide/topics/ui/accessibility/testing (Last updated 2026-10-23) |

## 2. Hitungan kontras (dapat diulang)

Metode: rumus luminans relatif sRGB yang dipakai WCAG,
`(L_terang + 0,05) / (L_gelap + 0,05)`. Dihitung dengan Python
2026-11-23. Ini hasil hitung, bukan uji di perangkat.

| Warna merek | vs putih `#FFFFFF` | vs hitam `#000000` | vs netral gelap `#1C1B1F` |
|---|---|---|---|
| Ungu `#7565F5` | 4,25 | 4,94 | 4,03 |
| Biru `#3B82F6` | 3,68 | 5,71 | 4,66 |
| Hijau `#22C55E` | 2,28 | 9,22 | 7,52 |
| Kuning `#FFB020` | 1,83 | 11,48 | 9,37 |
| Merah muda `#FF6B91` | 2,70 | 7,76 | 6,33 |

`#1C1B1F` vs putih: 17,13.

Temuan:

1. Teks putih kecil tidak memenuhi 4,5:1 di atas **satu pun** warna merek.
2. Teks hitam memenuhi 4,5:1 di atas **semua** warna merek.
3. `#1C1B1F` di atas ungu hanya 4,03 (gagal untuk teks kecil).
4. Warna merek sebagai teks di atas putih: tidak ada yang mencapai 4,5:1;
   hanya ungu (4,25) dan biru (3,68) yang mencapai 3:1 untuk teks besar.

## 3. Varian turunan untuk teks (PROPOSED — tidak menggantikan warna merek)

Varian dibuat dengan menskalakan kanal sRGB warna merek ke arah hitam
sampai ambang tercapai. Warna merek asli tetap dipakai untuk isian,
ikon besar, ilustrasi, dan aksen.

| Warna merek | Varian teks ≥ 4,5:1 di atas putih | Kontras | Varian ≥ 3:1 (teks besar / elemen non-teks) | Kontras |
|---|---|---|---|---|
| Ungu `#7565F5` | `#7161EC` | 4,54 | `#7565F5` (asli) | 4,25 |
| Biru `#3B82F6` | `#3473DA` | 4,55 | `#3B82F6` (asli) | 3,68 |
| Hijau `#22C55E` | `#178841` | 4,53 | `#1DAA51` | 3,03 |
| Kuning `#FFB020` | `#9E6D14` | 4,51 | `#C68819` | 3,03 |
| Merah muda `#FF6B91` | `#C1516D` | 4,50 | `#F16589` | 3,02 |

Catatan: varian kuning dan hijau untuk teks berubah cukup jauh dari warna
asli; kecocokan visual dengan identitas merek perlu penilaian owner.

## 4. Pasangan teks–latar yang diusulkan (PROPOSED)

| Pemakaian | Latar | Teks/ikon | Kontras | Memenuhi |
|---|---|---|---|---|
| Tombol utama | Ungu `#7565F5` | Hitam `#000000` | 4,94 | 4,5:1 |
| Tombol utama — alternatif **hanya untuk teks besar** (≥ 18sp, atau tebal ≥ 14sp) | Ungu `#7565F5` | Putih | 4,25 | 3:1 saja; **gagal** untuk teks < 18sp dan teks tebal < 14sp |
| Chip/label status lulus | Hijau `#22C55E` | Hitam | 9,22 | 4,5:1 |
| Peringatan / XP | Kuning `#FFB020` | Hitam | 11,48 | 4,5:1 |
| Galat / belum lulus | Merah muda `#FF6B91` | Hitam | 7,76 | 4,5:1 |
| Informasi | Biru `#3B82F6` | Hitam | 5,71 | 4,5:1 |
| Teks isi pada permukaan | Putih | `#1C1B1F` | 17,13 | 4,5:1 |
| Tautan/teks berwarna kecil pada putih | Putih | Varian ≥ 4,5:1 (§3) | ≥ 4,50 | 4,5:1 |

Teks gelap yang diusulkan per warna merek (dari tabel §2):

| Isian warna merek | `#000000` | `#1C1B1F` | Teks gelap yang diusulkan untuk teks kecil |
|---|---|---|---|
| Ungu `#7565F5` | 4,94 ✓ | **4,03 ✗** | **`#000000` saja** |
| Biru `#3B82F6` | 5,71 ✓ | 4,66 ✓ | `#000000` atau `#1C1B1F` |
| Hijau `#22C55E` | 9,22 ✓ | 7,52 ✓ | `#000000` atau `#1C1B1F` |
| Kuning `#FFB020` | 11,48 ✓ | 9,37 ✓ | `#000000` atau `#1C1B1F` |
| Merah muda `#FF6B91` | 7,76 ✓ | 6,33 ✓ | `#000000` atau `#1C1B1F` |

✓ = memenuhi 4,5:1; ✗ = gagal untuk teks kecil. `#1C1B1F` hanya boleh
dipakai pada pasangan yang memenuhi ambang.

Status tidak boleh disampaikan hanya lewat warna (UI:A-08).

## 5. Strategi dark mode

| Opsi | Isi | Kesesuaian blueprint | Risiko / implikasi |
|---|---|---|---|
| DM-1 Tema terang saja | Aplikasi selalu tampil terang; Force Dark dinonaktifkan eksplisit (`forceDarkAllowed=false`) karena tema terang bawaan mengizinkannya (AC-B4) | Sesuai BL:12 | Pengguna yang memakai mode gelap sistem tetap mendapat tampilan terang; perilaku Force Dark pada UI Compose **NOT VERIFIED** |
| DM-2 Tema gelap terpisah | Skema gelap dengan warna merek sebagai aksen | Menambah keputusan di luar BL:12 ("bright/light theme") → butuh persetujuan/revisi owner | Butuh pasangan kontras baru untuk latar gelap; dua set screenshot dan uji |
| DM-3 Force Dark otomatis | Membiarkan sistem menggelapkan UI | Tidak sesuai identitas warna; hasil tidak terkontrol | Kontras dan warna merek tidak dapat dijamin |

Implikasi Material 3 (PROPOSED):

- Skema warna dibangun manual dari token merek (`lightColorScheme`),
  **tanpa** dynamic color, agar palet merek tidak diganti warna wallpaper
  (AC-B5).
- Peran `onPrimary`, `onSecondary`, `onTertiary`, `onError`, dst. memakai
  pasangan §4 yang memenuhi 4,5:1.
- Token turunan §3 ditambahkan sebagai peran terpisah (mis. untuk teks
  berwarna), bukan mengganti `primary`.

## 6. Rekomendasi (saran, bukan keputusan)

1. **UO-1:** UI:KC-1 + UI:KC-2 terbatas:
   - Teks kecil di atas isian **ungu** memakai **`#000000`** (4,94). `#1C1B1F`
     di atas ungu (4,03) gagal untuk teks kecil dan tidak diusulkan.
   - Teks kecil di atas biru, hijau, kuning, dan merah muda memakai
     `#000000` atau `#1C1B1F` (keduanya ≥ 4,5:1, tabel §4).
   - Teks putih di atas ungu (4,25) hanya untuk **teks besar** (≥ 18sp, atau
     tebal ≥ 14sp), bukan untuk semua teks tebal.
   - Varian turunan §3 hanya untuk teks berwarna kecil di atas putih.
   - Lima warna merek tetap tidak berubah.
2. **UO-2:** DM-1 untuk V1, karena paling sesuai BL:12. DM-2 dapat
   dipertimbangkan kemudian sebagai keputusan owner terpisah.

## 7. Kriteria uji aksesibilitas (untuk implementasi nanti; NOT VERIFIED)

| ID | Kriteria |
|---|---|
| AT-1 | Setiap pasangan token teks–latar yang dipakai memenuhi AC-B3 (cek otomatis atas daftar token) |
| AT-2 | Accessibility Scanner dan UI Check Mode tidak melaporkan kontras rendah pada layar utama (AC-B6) |
| AT-3 | Dengan mode gelap sistem aktif, tampilan sesuai opsi yang dipilih (DM-1: tetap terang, tanpa Force Dark) |
| AT-4 | Dynamic color tidak mengubah warna merek pada Android 12+ |
| AT-5 | Status lulus/belum lulus/hari libur terbaca dalam grayscale (UI:A-08) |
| AT-6 | Teks pada skala font maksimum yang diuji tetap kontras dan tidak terpotong (UI:A-04) |

## 8. Pertanyaan untuk owner

1. **UO-1-Q1:** Setujui teks kecil `#000000` di atas isian ungu, dan `#000000` atau `#1C1B1F` di atas isian biru, hijau, kuning, dan merah muda (hanya pasangan yang ≥ 4,5:1)?
2. **UO-1-Q2:** Setujui penambahan varian turunan §3 khusus untuk teks berwarna kecil di atas putih (warna merek tetap)?
3. **UO-1-Q3:** Bila tombol utama ungu harus berteks putih (4,25:1), batasi hanya pada **teks besar** — ≥ 18sp, atau tebal ≥ 14sp — sehingga teks < 18sp dan teks tebal < 14sp tetap memakai `#000000`?
4. **UO-2-Q1:** Setujui DM-1 (tema terang saja, Force Dark dinonaktifkan) untuk V1?
5. **UO-2-Q2:** Setujui Material 3 tanpa dynamic color?

Status: **AWAITING OWNER**. UO-1 (UW-17) dan UO-2 (UW-18) tetap **BLOCKED**.
