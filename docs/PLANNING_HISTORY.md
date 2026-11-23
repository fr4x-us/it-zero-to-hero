# IT ZERO → HERO — Riwayat Perencanaan

Status: PERSIAPAN. Implementasi aplikasi belum diizinkan.

Dokumen ini **mencatat**, bukan membuat, keputusan perencanaan. Isinya
hanya berasal dari dokumen yang ada di repositori per commit `260800d`
(branch `main`, 2026-11-23). Riwayat percakapan perencanaan asli **tidak**
tersedia di repositori dan tidak direkonstruksi di sini.

Dokumen ini tidak mengubah `docs/BLUEPRINT_LOCKED.md` atau `CLAUDE.md`.
Bila ada perbedaan, kedua dokumen itu yang berlaku.

## 0. Klasifikasi dan kode sumber

| Status | Arti |
|---|---|
| **LOCKED** | Didukung langsung oleh dokumen sumber di repositori. |
| **OPEN** | Belum ditentukan; memerlukan keputusan owner. Contoh atau rekomendasi teknis yang pernah ditulis **tidak** dianggap keputusan. |
| **MISSING SOURCE** | Rinciannya disebut pernah direncanakan atau dirujuk oleh dokumen sumber, tetapi isinya tidak ada di repositori. |

| Kode | Sumber | Masuk ke `main` melalui |
|---|---|---|
| BL | `docs/BLUEPRINT_LOCKED.md` (status LOCKED, perubahan perlu persetujuan eksplisit owner) | commit `a277ba7` |
| CM | `CLAUDE.md` (instruksi proyek) | commit `15d61c0` |
| EN | `docs/ENVIRONMENT.md` | PR #2 (merge `80cb33d`) |
| QG | `docs/QUALITY_GATES.md` | PR #3 (merge `260800d`) |
| SK | `.claude/skills/SOURCES.md` | PR #1 (merge `c5f62e6`) |

Rujukan baris memakai format `BL:15` = `docs/BLUEPRINT_LOCKED.md` baris 15.

Catatan hierarki: keputusan **produk** hanya bersumber dari BL dan CM.
EN dan QG adalah dokumen proses/verifikasi yang telah di-merge owner;
keduanya tidak menambah keputusan produk.

## 1. Riwayat dokumen di repositori

Semua commit bertanggal 2026-11-23.

| Commit | Peristiwa |
|---|---|
| `36b4ba0` | Initial commit (README). |
| `15d61c0` | Instruksi proyek dan aturan tidak dapat ditawar (CM). |
| `a277ba7` | Blueprint terkunci V1 (BL). |
| `093afd3` → `c5f62e6` | Lima skill Android pihak ketiga dipasang (PR #1). |
| `599f5e5` → `80cb33d` | Audit lingkungan dan rencana CI (PR #2). |
| `bd99674` → `260800d` | Quality gates (PR #3). |

## 2. Keputusan LOCKED

### 2.1 Status dan aturan proyek

| ID | Keputusan | Sumber |
|---|---|---|
| L-01 | Proyek di tahap persiapan; implementasi belum diizinkan. | CM:5, BL:74 |
| L-02 | Keputusan produk terkunci tidak berubah tanpa persetujuan eksplisit owner. | BL:4–5, CM:13–14 |
| L-03 | Bukan website atau PWA. | CM:17 |
| L-04 | Kurikulum dan aturan penilaian terkunci tidak boleh diubah. | CM:18 |
| L-05 | Tanpa AI tutoring dan tanpa penilaian berbasis AI. | CM:19, BL:38 |
| L-06 | Tidak memalsukan test, hasil build, atau artefak APK. | CM:21 |
| L-07 | Tidak meng-commit secret, kata sandi, atau kunci penandatanganan. | CM:22 |
| L-08 | Dokumentasi resmi Android diutamakan untuk keputusan teknis. | CM:23 |
| L-09 | Keterbatasan teknis dan risiko keamanan wajib dijelaskan. | CM:24 |
| L-10 | Alur kerja: baca dokumen → periksa lingkungan → identifikasi blocker → usulkan tugas kecil terverifikasi → tunggu izin → branch, test, checkpoint. | CM:27–32 |
| L-11 | Penjelasan dan laporan memakai Bahasa Indonesia. | CM:35 |

### 2.2 Platform dan arsitektur

| ID | Keputusan | Sumber |
|---|---|---|
| L-20 | APK Android native. | BL:8, CM:8 |
| L-21 | Kotlin + Jetpack Compose + Material 3. | BL:9, CM:8–9 |
| L-22 | Offline-first. | BL:10, CM:9 |
| L-23 | Room/SQLite, MVVM, Repository. | BL:11 |
| L-24 | Tema Colorful Academy, terang. | BL:12, BL:67 |

### 2.3 Kurikulum

| ID | Keputusan | Sumber |
|---|---|---|
| L-30 | 16 minggu, nominal 128 jam. | BL:15 |
| L-31 | Empat fase: (1) IT foundations; (2) Mathematics and computational thinking; (3) Python programming; (4) Database, web basics, Git, capstone. | BL:16–20 |
| L-32 | Modul dibuka secara linear. | BL:21 |
| L-33 | Isi meliputi teori akademik, diagram, lab, latihan, kuis, proyek, ujian, dan ringkasan. | BL:22–23 |
| L-34 | Video YouTube online bersifat opsional. | BL:24 |

### 2.4 Penilaian

| ID | Keputusan | Sumber |
|---|---|---|
| L-40 | Bobot: Theory 30%, Laboratory 40%, Mini-project 20%, Concept explanation 10%. | BL:27–30 |
| L-41 | Skor akhir berbobot minimal 80. | BL:31 |
| L-42 | Setiap komponen minimal 75. | BL:32 |
| L-43 | Remedial tanpa batas. | BL:33 |
| L-44 | Skor komponen terbaik dan seluruh riwayat percobaan disimpan. | BL:34 |
| L-45 | Tidak ada penalti XP dan tidak ada XP farming. | BL:35 |
| L-46 | Ujian teori berwaktu dengan tenggat persisten. | BL:36 |
| L-47 | Sesi lab dan proyek fleksibel. | BL:37 |
| L-48 | Penilaian objektif dan offline. | BL:38 |

### 2.5 Laboratorium

| ID | Keputusan | Sumber |
|---|---|---|
| L-50 | Editor dan eksekusi Python offline. | BL:41 |
| L-51 | Aktivitas logika dan flowchart. | BL:42 |
| L-52 | Latihan SQL. | BL:43 |
| L-53 | Test case objektif. | BL:44 |
| L-54 | Kompatibilitas dan isolasi runtime wajib divalidasi. | BL:45 |

### 2.6 Gamifikasi

| ID | Keputusan | Sumber |
|---|---|---|
| L-60 | XP, level, achievement, mastery. | BL:48 |
| L-61 | Nilai akademik terpisah dari XP. | BL:49 |

### 2.7 Kalender studi

| ID | Keputusan | Sumber |
|---|---|---|
| L-70 | Zona waktu Asia/Tokyo. | BL:52 |
| L-71 | Hari libur nasional Jepang dan hari libur pengganti. | BL:53 |
| L-72 | Presentasi kalender Jepang. | BL:54 |
| L-73 | Hari kerja perusahaan dibedakan dari hari libur nasional. | BL:55 |
| L-74 | Penjadwalan belajar fleksibel. | BL:56 |
| L-75 | Jam tenang 22:00–07:00 JST. | BL:57 |

### 2.8 Keandalan dan keamanan

| ID | Keputusan | Sumber |
|---|---|---|
| L-80 | Autosave dan crash recovery. | BL:60 |
| L-81 | Local snapshots. | BL:61 |
| L-82 | Ekspor backup portabel terenkripsi kata sandi. | BL:62 |
| L-83 | Restore aman: pratinjau, konfirmasi, validasi, rollback, dan pelestarian riwayat percobaan. | BL:63–64 |

### 2.9 UI

| ID | Keputusan | Sumber |
|---|---|---|
| L-90 | Lima tab utama: Home, Learn, Lab, Calendar, Progress. | BL:68–69 |
| L-91 | Pengaturan profil dan backup. | BL:70 |
| L-92 | UI Android yang aksesibel, mudah dibaca, dan responsif. | BL:71 |

### 2.10 Proses dan lingkungan (bukan keputusan produk)

Keputusan berikut tercatat dalam dokumen yang di-merge owner. Keputusan
ini mengatur cara kerja, bukan isi produk.

| ID | Keputusan | Sumber |
|---|---|---|
| L-100 | Claude Code Cloud untuk pengembangan; GitHub Actions sebagai lingkungan build, lint, unit test, dan APK utama. | EN §2 |
| L-101 | Workflow CI build tidak dibuat sebelum proyek Android ada dan implementasi diizinkan. | EN §3 |
| L-102 | Versi toolchain dipilih sebagai satu kombinasi kompatibel dan disetujui owner sebelum proyek Gradle dibuat. | EN §4 |
| L-103 | Setiap klaim build/test/APK wajib disertai bukti log aktual; tanpa bukti statusnya NOT RUN. | QG §1 (EV-1–EV-6), sejalan dengan CM:21 |
| L-104 | Lima skill Android pihak ketiga dipasang sebagai panduan; `BLUEPRINT_LOCKED.md` dan `CLAUDE.md` lebih tinggi. | SK |

## 3. Keputusan OPEN

Butir yang tidak ditentukan dokumen sumber. Contoh di QG/EN (mis. AES-GCM,
Hilt, Temurin) adalah **rekomendasi atau contoh**, bukan keputusan.

| ID | Topik | Keterangan | Sumber yang mencatat |
|---|---|---|---|
| O-01 | Kombinasi toolchain (AGP, Gradle Wrapper, JDK, Kotlin, Compose BOM, KSP, `compileSdk`/`targetSdk`/`minSdk`) | Belum dipilih. | EN §4, QG AB-3 |
| O-02 | Izin `INTERNET` dan cara membuka video YouTube opsional | Belum diputuskan. | QG OF-3 |
| O-03 | Pembulatan skor dan dasar perhitungan skor akhir | Perlu dikonfirmasi terhadap riwayat perencanaan (lihat M-05). | QG GR-10 |
| O-04 | Runtime Python offline | Pilihan runtime belum ada; BL mewajibkan validasi. | QG LB-2, BL:45 |
| O-05 | Sumber dan pembaruan data hari libur Jepang | Belum diputuskan. | QG CL-3 |
| O-06 | Algoritma, KDF, dan parameter enkripsi backup | AES-GCM di QG hanya contoh. | QG SC-1 |
| O-07 | Kebijakan backup otomatis Android (`allowBackup`, aturan ekstraksi data) | Belum diputuskan. | QG SC-6 |
| O-08 | Kebijakan R8/minify dan ukuran APK | Belum diputuskan. | QG AP-5 |
| O-09 | Runner untuk uji emulator/perangkat | "Diputuskan kemudian". | EN §2 |
| O-10 | Proses rilis, penandatanganan, dan kanal distribusi | "Diputuskan kemudian". | EN §2 |
| O-11 | Akses `dl.google.com` dan SDK di container cloud | Opsional, belum dijalankan. | EN §5 |
| O-12 | Dependency injection (mis. Hilt atau manual) | Hilt hanya default skill. | Audit akhir; `android-dev` |
| O-13 | Library navigasi (Navigation Compose atau Navigation 3) | Hanya disebut di skill. | Audit akhir; `compose` |
| O-14 | Struktur modul Gradle | Belum diputuskan. | Audit akhir |
| O-15 | Pola state/effect UI | Default skill, belum disetujui. | Audit akhir; `android-dev` |
| O-16 | Stack test (Robolectric, alat screenshot test) | Belum diputuskan. | Audit akhir; `android-testing` |
| O-17 | Interpretasi "no XP farming" di QG GR-8 | Rumusan QG adalah interpretasi, perlu konfirmasi owner. | QG GR-8, BL:35 |

Catatan: O-12 sampai O-16 berasal dari audit akhir kesiapan (laporan
sesi, bukan dokumen di repositori) dan belum tercatat di QG.

## 4. MISSING SOURCE

BL:75–78 menyatakan blueprint adalah *"condensed baseline of the approved
planning decisions, not the complete lesson content"* dan meminta
*"Preserve detailed decisions from the approved planning history"*.
Riwayat perencanaan yang disetujui itu **tidak ada** di repositori.
Rincian berikut dirujuk oleh dokumen sumber tetapi isinya tidak tersedia:

| ID | Rincian yang hilang | Dirujuk oleh |
|---|---|---|
| M-01 | Riwayat perencanaan lengkap yang telah disetujui (dokumen atau percakapan asli). | BL:75–78 |
| M-02 | Isi pelajaran lengkap: daftar modul per minggu dan per fase, tujuan belajar, materi, diagram. | BL:15–23, BL:75–76 |
| M-03 | Pembagian 128 jam nominal ke fase, minggu, dan modul. | BL:15 |
| M-04 | Kriteria pembukaan modul linear (syarat lulus modul sebelumnya, peran kuis/latihan). | BL:21 |
| M-05 | Rincian rumus penilaian: cakupan tiap komponen per modul/fase, pembulatan, apakah skor akhir memakai skor komponen terbaik. | BL:27–34 |
| M-06 | Metode penilaian objektif offline untuk *Concept explanation* (10%) tanpa AI. | BL:30, BL:38 |
| M-07 | Aturan ujian teori: durasi, format soal, perilaku saat tenggat persisten terlewat. | BL:36 |
| M-08 | Batas "fleksibel" untuk sesi lab dan proyek. | BL:37 |
| M-09 | Spesifikasi mini-project dan capstone (topik, rubrik objektif, test case). | BL:20, BL:29 |
| M-10 | Spesifikasi lab: versi dan cakupan library Python, format aktivitas logika/flowchart, dialek dan dataset SQL, isi test case. | BL:41–44 |
| M-11 | Rumus XP, level, achievement, dan mastery; definisi tepat "XP farming". | BL:35, BL:48 |
| M-12 | Rincian presentasi kalender Jepang (mis. era Jepang, format tanggal). | BL:54 |
| M-13 | Sumber dan definisi hari kerja perusahaan. | BL:55 |
| M-14 | Aturan penjadwalan belajar fleksibel dan perilaku jam tenang (apa yang ditahan atau ditunda). | BL:56–57 |
| M-15 | Frekuensi, retensi, dan cakupan local snapshot. | BL:61 |
| M-16 | Format file backup portabel dan alur restore terperinci. | BL:62–64 |
| M-17 | Spesifikasi visual Colorful Academy (palet, tipografi, ikon, ilustrasi). | BL:12, BL:67 |
| M-18 | Isi tiap tab utama serta field profil dan pengaturan backup. | BL:68–70 |
| M-19 | Target aksesibilitas dan perangkat (ukuran layar, orientasi, versi Android minimum). | BL:71 |

## 5. Aturan pemeliharaan dokumen ini

- Butir MISSING SOURCE hanya dipindah ke LOCKED bila owner menyerahkan
  sumbernya ke repositori atau menyetujuinya secara eksplisit; sumber baru
  dicantumkan sebagai rujukan.
- Butir OPEN hanya dipindah ke LOCKED melalui keputusan owner yang
  tercatat (mis. dokumen keputusan yang di-merge).
- Perubahan pada keputusan LOCKED yang bersumber dari BL memerlukan revisi
  blueprint yang disetujui owner; dokumen ini tidak dapat menggantikannya.
