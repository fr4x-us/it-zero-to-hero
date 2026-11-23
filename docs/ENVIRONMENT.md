# IT ZERO → HERO — Lingkungan Pengembangan dan Build

Status: PERSIAPAN. Implementasi aplikasi belum diizinkan.
Dokumen ini tidak mengubah `docs/BLUEPRINT_LOCKED.md` maupun `CLAUDE.md`;
keduanya tetap menjadi sumber kebenaran.

## 1. Hasil audit lingkungan Claude Code Cloud

Audit dilakukan pada 2026-11-23 di container sesi Claude Code Cloud,
hanya dengan perintah baca/periksa (tanpa instalasi).

| Pemeriksaan | Hasil aktual | Status |
|---|---|---|
| Sistem operasi | Ubuntu 24.04.5 LTS, kernel 6.18.44 | PASS |
| Arsitektur CPU | x86_64, 4 core | PASS |
| Java | OpenJDK 21.0.13 (`java` dan `javac`) | PASS |
| `JAVA_HOME` | `/usr/lib/jvm/java-21-openjdk-amd64` | PASS |
| `ANDROID_HOME` / `ANDROID_SDK_ROOT` | tidak di-set | FAIL |
| Android SDK di disk | tidak ditemukan (`sdkmanager`, `adb`, `android.jar` tidak ada) | FAIL |
| `sdkmanager`, `avdmanager`, `adb` | tidak ditemukan | FAIL |
| Build Tools (`aapt2`, `d8`, `apksigner`, `zipalign`) | tidak ditemukan | FAIL |
| Emulator / `/dev/kvm` | tidak tersedia | WARNING |
| Git | 2.43.0 | PASS |
| Gradle (sistem) | 8.14.3 di `/opt/gradle` | WARNING (proyek harus memakai Gradle Wrapper) |
| `kotlinc` | tidak ditemukan (tidak diperlukan; Kotlin dibawa oleh Gradle) | WARNING |
| Disk | ±61 GB tersedia | PASS |
| Memori | 15 GiB RAM, tanpa swap | PASS |
| `maven.google.com` | HTTP 200 | PASS |
| `dl.google.com` | `CONNECT tunnel failed, response 403` (ditolak kebijakan jaringan sesi) | FAIL |
| Maven Central | HTTP 429 sementara, lalu 200 saat diulang | PASS |
| `plugins.gradle.org`, `services.gradle.org` | HTTP 200 | PASS |

### Dampak

- Tanpa Android SDK, Android Gradle Plugin (AGP) tidak dapat mengompilasi
  atau mengemas APK di container ini.
- `dl.google.com` menyajikan paket SDK dan artefak Google Maven (AGP,
  AndroidX, Compose, Room). Selama host ini diblokir, sinkronisasi Gradle
  proyek Android di container ini diperkirakan gagal (belum diuji dengan
  build nyata karena proyek belum ada).
- Tanpa KVM, emulator dan instrumented test tidak dapat dijalankan di sini.

Keputusan: container cloud **tidak** dipakai untuk build APK. Pengaturan
jaringan dan instalasi SDK sengaja tidak diubah.

## 2. Arsitektur kerja

```
 ┌─────────────────────────────┐      push branch / PR      ┌──────────────────────────────┐
 │ Claude Code Cloud           │ ─────────────────────────▶ │ GitHub Actions               │
 │ - baca dokumen & skill      │                            │ - setup JDK + Android SDK    │
 │ - tulis kode & test         │ ◀───────────────────────── │ - build, lint, unit test     │
 │ - review, dokumentasi       │   status check, log, APK   │ - artefak APK (debug)        │
 └─────────────────────────────┘                            └──────────────────────────────┘
```

| Peran | Lingkungan | Tanggung jawab |
|---|---|---|
| Pengembangan | Claude Code Cloud | Menulis kode/test/dokumen di branch kerja, membuka PR. Tidak mengklaim build/test lulus tanpa bukti dari CI. |
| Build, test, APK | GitHub Actions (runner Ubuntu yang di-host GitHub) | Sumber kebenaran untuk hasil build, lint, unit test, dan artefak APK. |
| Uji perangkat/emulator | Mesin lokal owner atau runner dengan KVM (diputuskan kemudian) | Instrumented test dan uji manual APK. |
| Rilis | Diputuskan kemudian, dengan persetujuan owner | Penandatanganan APK rilis memakai secret, bukan file di repo. |

Aturan:

- Hasil build/test hanya dilaporkan berdasarkan log GitHub Actions yang nyata.
- Tidak ada keystore, password, atau token di repositori.
- Perubahan masuk melalui branch dan pull request.

## 3. Rencana workflow Android CI (belum dibuat)

Belum ada file di `.github/workflows/`. Workflow build **tidak boleh** dibuat
sebelum proyek Android (Gradle Wrapper, `settings.gradle.kts`, modul `app`)
ada dan implementasi diizinkan. Rencana berikut adalah rancangan, bukan
konfigurasi aktif.

### Pemicu

- `pull_request` ke `main`.
- `push` ke `main`.
- `workflow_dispatch` untuk build manual.

### Langkah yang direncanakan

1. `actions/checkout` — ambil kode.
2. `actions/setup-java` — JDK distribusi Temurin, versi sesuai matriks
   kompatibilitas (lihat bagian 4).
3. Android SDK — runner `ubuntu-latest` milik GitHub menyediakan Android SDK
   bawaan; ketersediaan dan versi paketnya diverifikasi terhadap dokumentasi
   `actions/runner-images` saat implementasi. Bila perlu, paket platform dan
   build-tools dipasang eksplisit dengan `sdkmanager`.
4. `gradle/actions/setup-gradle` — cache Gradle dan validasi Gradle Wrapper.
5. `./gradlew lint` — Android Lint.
6. `./gradlew testDebugUnitTest` — unit test JVM (termasuk aturan penilaian
   terkunci dan logika kalender).
7. `./gradlew assembleDebug` — APK debug.
8. `actions/upload-artifact` — unggah APK debug dan laporan test/lint.

### Prinsip keamanan dan keandalan

- `permissions: contents: read` sebagai default.
- Action pihak ketiga dipin ke commit SHA.
- `concurrency` untuk membatalkan run lama pada branch yang sama.
- Build rilis bertanda tangan dipisah ke workflow sendiri, hanya berjalan
  dengan persetujuan owner; keystore dari GitHub Secrets, tidak pernah dari
  repo dan tidak pernah dicetak ke log.
- Instrumented test (emulator) direncanakan terpisah karena butuh KVM dan
  waktu lebih lama.

## 4. Pemilihan versi toolchain

Versi berikut **belum dipilih** dan harus ditetapkan sebagai satu kombinasi
yang kompatibel ketika implementasi diizinkan:

| Komponen | Batasan yang harus dicek |
|---|---|
| AGP | Menentukan versi Gradle minimum dan JDK minimum. |
| Gradle (Wrapper) | Harus memenuhi syarat AGP; Gradle sistem 8.14.3 tidak dijadikan acuan. |
| JDK | Harus memenuhi syarat AGP; JDK 21 tersedia di cloud, versi CI mengikuti matriks. |
| Kotlin | Sejak Kotlin 2.0, Compose Compiler disertakan sebagai plugin Gradle Kotlin dengan versi sama dengan Kotlin. |
| Compose | Dikelola melalui Compose BOM; harus cocok dengan Kotlin dan `compileSdk`. |
| `compileSdk` / `targetSdk` / `minSdk` | Mengikuti persyaratan Google Play terbaru dan dukungan perangkat target. |
| KSP, Room | Versi KSP harus cocok dengan versi Kotlin. |

Sumber acuan (dokumentasi resmi):

- Catatan rilis dan tabel kompatibilitas AGP: <https://developer.android.com/build/releases/gradle-plugin>
- Compose BOM: <https://developer.android.com/develop/ui/compose/bom>
- Compose Compiler Gradle plugin: <https://developer.android.com/develop/ui/compose/compiler>
- Persyaratan target API Google Play: <https://developer.android.com/google/play/requirements/target-sdk>

Kombinasi terpilih dicatat dalam dokumen keputusan tersendiri dan disetujui
owner sebelum proyek Gradle dibuat.

## 5. Opsi lanjutan (belum dijalankan)

- Membuka `dl.google.com` di pengaturan jaringan environment cloud agar sync
  Gradle dan kompilasi lokal di container dimungkinkan. Ini perubahan
  pengaturan dan memerlukan persetujuan owner.
- Memasang Android SDK command-line tools melalui setup script environment.

Keduanya opsional; GitHub Actions tetap menjadi lingkungan build utama.
