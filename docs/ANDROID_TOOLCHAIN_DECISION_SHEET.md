# IT ZERO → HERO — Android Toolchain Decision Sheet (O-01)

Status: PERSIAPAN · semua versi **PROPOSED**, bukan LOCKED · O-01 tetap
**OPEN** sampai owner menyetujui dan kombinasi terbukti di GitHub Actions.
Tanggal pemeriksaan sumber: **2026-11-23**.

Dokumen ini tidak membuat proyek Android, file Gradle, kode, workflow, atau
APK. Dasar: [`ENVIRONMENT.md`](ENVIRONMENT.md) §2–4,
[`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md)
(O-01 TD:47, O-04 TD:45, CI TD:24, arsitektur TD:17–20, TD:26),
[`PYTHON_OFFLINE_FEASIBILITY_PLAN.md`](PYTHON_OFFLINE_FEASIBILITY_PLAN.md),
[`QUALITY_GATES.md`](QUALITY_GATES.md) AB-3 dan EV-1–EV-6.

## 0. Label bukti

| Label | Arti |
|---|---|
| **D** | Terverifikasi dari dokumentasi resmi atau metadata repositori resmi (§1). |
| **V** | Versi ada, tetapi kompatibilitasnya **belum** dinyatakan sumber resmi; wajib diverifikasi di CI. |
| **A** | Asumsi/usulan perencanaan. |

## 1. Sumber resmi (diakses 2026-11-23)

| Kode | Sumber | "Last updated" halaman |
|---|---|---|
| T1 | https://developer.android.com/build/releases/agp-9-3-0-release-notes | 2026-11-05 |
| T2 | https://developer.android.com/build/releases/agp-9-4-0-release-notes | — |
| T3 | https://developer.android.com/build/releases/gradle-plugin (→ AGP 9.5.0, Oktober 2026) | 2026-11-05 |
| T4 | https://developer.android.com/build/migrate-to-built-in-kotlin | 2026-09-15 |
| T5 | https://kotlinlang.org/docs/gradle-configure-project.html (tabel KGP–Gradle–AGP) | — |
| T6 | https://kotlinlang.org/docs/releases.html | — |
| T7 | https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler | 2026-11-11 |
| T8 | https://developer.android.com/develop/ui/compose/bom/bom-mapping | 2026-11-18 |
| T9 | https://developer.android.com/jetpack/androidx/releases/compose | 2026-11-20 |
| T10 | https://developer.android.com/jetpack/androidx/releases/room | 2026-11-20 |
| T11 | https://developer.android.com/jetpack/androidx/releases/navigation | 2026-11-20 |
| T12 | https://kotlinlang.org/docs/ksp-overview.html (§Requirements) | 23 Nov 2026 |
| T13 | https://developer.android.com/build/migrate-to-ksp | 2026-11-12 |
| T14 | https://developer.android.com/build/jdks | 2026-11-12 |
| T15 | https://developer.android.com/google/play/requirements/target-sdk | 2026-10-28 |
| T16 | https://developer.android.com/tools/releases/platforms | 2026-10-28 |
| T17 | https://services.gradle.org/versions/all (daftar rilis Gradle resmi) | — |
| T18 | `gradle/gradle` — `platforms/documentation/docs/src/docs/userguide/releases/compatibility.adoc` (cabang `master`) | — |
| T19 | Maven Central `com/google/devtools/ksp/symbol-processing-gradle-plugin/maven-metadata.xml` | lastUpdated 2026-11-13 |
| T20 | Maven Central `com/chaquo/python/gradle/maven-metadata.xml` | lastUpdated 2026-10-26 |
| T21 | `chaquo/chaquopy` — `product/runtime/docs/sphinx/versions.rst`, `android.rst` (lihat Batch 03) | — |

Tidak dapat diakses dari sesi ini: `docs.gradle.org` (dipakai T18 sebagai
sumber dokumen yang sama), `dl.google.com`/Google Maven metadata (versi
AndroidX diambil dari halaman rilis T9–T11), `github.com` (rilis KSP diambil
dari T12 dan T19).

## 2. Kombinasi yang direkomendasikan (PROPOSED)

| Komponen | Versi PROPOSED | Label | Dasar |
|---|---|---|---|
| Android Gradle Plugin | **9.3.1** | D | AGP 9.3.0 rilis Juli 2026, patch 9.3.1 tercantum (T1); batas atas AGP yang *fully supported* KGP 2.4.20–2.4.21 adalah **9.3.1** (T5). |
| Gradle Wrapper | **9.7.0** | D | AGP 9.3 minimum Gradle 9.5.0 (T1); KGP 2.4.21 *fully supported* Gradle 7.6.3–**9.7.0** (T5); 9.7.0 dirilis 2026-08-06 (T17). |
| JDK (CI dan daemon Gradle) | **17** | D | AGP 9.3 minimum dan default JDK 17 (T1, T14); Gradle butuh JVM 17–27 (T18). |
| Kotlin (KGP, built-in Kotlin AGP 9) | **2.4.21** | D | Rilis 2026-10-08, lini 2.4 didukung sampai 2027-12-03 (T6); AGP 9.0+ memakai built-in Kotlin, plugin `kotlin-android` tidak lagi diterapkan (T4). |
| Compose Compiler | **plugin `org.jetbrains.kotlin.plugin.compose` 2.4.21** | D | Versi plugin "matches your Kotlin version"; tersedia sejak Kotlin 2.0 (T7). |
| Compose BOM | **2026.11.01** | D / V | BOM terbaru di tabel pemetaan (T8); rilis stabil Compose 1.13.0 dan Material3 1.5.0 pada 2026-11-18 (T9). Pemetaan BOM→versi artefak dibaca dari urutan tabel T8 → konfirmasi di CI (V). |
| KSP | **2.3.12** | D | "The latest KSP version, 2.3.12" mendukung KGP 2.3.20–2.4.x, AGP ≥ 8.13.0, Gradle ≥ 8.13, JDK ≥ 17 (T12). |
| Room | **2.8.5** | D | Stabil terbaru, 2026-09-09; memakai KSP (T10). |
| Navigation Compose | **2.10.2** | D | Stabil terbaru, 2026-09-23 (T11). Seri 2.10 menaikkan *compileSdk* Compose ke API 37 dan mensyaratkan **AGP ≥ 9.2.0** (T11). |
| `compileSdk` | **37** | D / V | Diwajibkan Navigation 2.10 (T11); API maksimum AGP 9.3 = 37 (T1). Ketersediaan paket platform 37 di runner: V. |
| SDK Build Tools | **36.0.0** | D | Minimum dan default AGP 9.3 (T1). |
| `targetSdk` | **36** | D / A | Google Play: app baru dan update wajib target ≥ API 36 (Android 16) (T15). Memilih 36 (bukan 37) adalah usulan (A) untuk menghindari perubahan perilaku API 37 sebelum diuji. |
| `minSdk` | **24** | A | AndroidX default minSdk 23 (T11); Chaquopy membutuhkan ≥ 24 (T21). 24 menjaga opsi Chaquopy terbuka **tanpa** memilihnya. Keputusan akhir mengikuti M-19 dan O-04. |

Ringkasnya: **AGP 9.3.1 · Gradle 9.7.0 · JDK 17 · Kotlin 2.4.21 · Compose
Compiler 2.4.21 · Compose BOM 2026.11.01 · KSP 2.3.12 · Room 2.8.5 ·
Navigation 2.10.2 · compileSdk 37 · targetSdk 36 · minSdk 24 · Build Tools
36.0.0.**

## 3. Matriks kompatibilitas

| Pasangan | Syarat resmi | Kombinasi | Status |
|---|---|---|---|
| AGP 9.3 ↔ Gradle | Gradle ≥ 9.5.0 (T1) | 9.7.0 | D ✓ |
| KGP 2.4.21 ↔ Gradle | 7.6.3–9.7.0 *fully supported* (T5) | 9.7.0 | D ✓ (tepat di batas atas) |
| KGP 2.4.21 ↔ AGP | 8.5.2–9.3.1 *fully supported* (T5) | 9.3.1 | D ✓ (tepat di batas atas) |
| AGP 9.3 ↔ JDK | JDK 17 min/default (T1) | 17 | D ✓ |
| Gradle ↔ JDK | Menjalankan Gradle: JVM 17–27 (T18) | 17 | D ✓ |
| KSP 2.3.12 ↔ KGP/AGP/Gradle/JDK | KGP 2.3.20–2.4.x, AGP ≥ 8.13.0, Gradle ≥ 8.13, JDK ≥ 17 (T12) | 2.4.21 / 9.3.1 / 9.7.0 / 17 | D ✓ |
| Compose Compiler ↔ Kotlin | Versi plugin sama dengan Kotlin (T7) | 2.4.21 | D ✓ |
| Navigation 2.10 ↔ AGP / compileSdk | AGP ≥ 9.2.0, compileSdk 37 (T11) | 9.3.1 / 37 | D ✓ |
| AGP 9.3 ↔ compileSdk | Maksimum API 37 (T1) | 37 | D ✓ |
| Room 2.8.5 ↔ KSP | Room memakai KSP (T10); versi KSP minimum untuk Room tidak dinyatakan | 2.3.12 | V |
| Compose 1.13 / BOM 2026.11.01 ↔ compileSdk, Kotlin | Tidak ditemukan pernyataan eksplisit | 37 / 2.4.21 | V |
| Built-in Kotlin AGP 9 ↔ KSP dan plugin Compose | Halaman migrasi tidak memuat matriks versi (T4) | — | V |
| Chaquopy 17.2 ↔ AGP | AGP 7.3–9.5 (T21) | 9.3.1 | D ✓ (bila kelak dipilih) |
| Chaquopy ↔ minSdk | ≥ 24 (T21) | 24 | D ✓ (bila kelak dipilih) |

## 4. Alasan pemilihan

1. **Batas Kotlin menentukan AGP.** Rilis AGP terbaru adalah 9.5.x (T3),
   tetapi KGP 2.4.21 (Kotlin stabil terbaru, T6) hanya *fully supported*
   sampai AGP 9.3.1 dan Gradle 9.7.0 (T5). AGP 9.4/9.5 juga mensyaratkan
   Gradle ≥ 9.6.0 (T2, T3). Memilih AGP 9.3.1 menjaga semua pasangan di
   dalam rentang yang terdokumentasi.
2. **Navigation 2.10 memaksa AGP ≥ 9.2.0 dan compileSdk 37** (T11); AGP
   9.3.1 memenuhi keduanya.
3. **JDK 17** adalah minimum dan default AGP (T1, T14); paling sedikit
   risiko di CI.
4. **KSP 2.3.12** adalah versi yang persyaratannya tertulis (T12). Versi
   2.3.14 sudah ada di Maven Central (T19) tetapi persyaratannya belum
   tercantum → alternatif V.
5. **Selaras Batch 02:** satu modul `app` (O-14), Navigation Compose
   (O-13), DI manual tanpa Hilt (O-12) — tidak ada kebutuhan versi Hilt.

## 5. Alternatif kompatibel

| Alternatif | Isi | Kapan dipakai | Risiko |
|---|---|---|---|
| ALT-1 (patch terbaru) | AGP 9.3.3, Gradle 9.7.1, KSP 2.3.14 | Bila 9.3.1/9.7.0/2.3.12 memiliki bug yang diperbaiki patch | Di luar rentang *fully supported* yang tertulis (T5, T12) → V |
| ALT-2 (Gradle default AGP) | Gradle 9.5.0 (min & default AGP 9.3, T1) | Bila Gradle 9.7.0 bermasalah | Masih dalam rentang KGP (T5) → D |
| ALT-3 (JDK 21) | JDK 21 untuk menjalankan Gradle | Bila ada kebutuhan JDK lebih baru | Gradle mendukung (T18); AGP hanya menyatakan minimum 17 → V |
| ALT-4 (AGP terbaru) | AGP 9.5.x + Gradle ≥ 9.6.0 + Kotlin 2.4.21 | Hanya bila fitur AGP 9.4/9.5 dibutuhkan | AGP di atas rentang KGP (T5): "might encounter deprecation warnings or some new features might not work" → butuh persetujuan owner |
| ALT-5 (targetSdk 37) | targetSdk = compileSdk = 37 | Setelah perubahan perilaku API 37 ditinjau | Perilaku baru API 37 belum diuji → V |

## 6. Risiko

| # | Risiko | Mitigasi |
|---|---|---|
| R1 | AGP 9.3.1 dan Gradle 9.7.0 tepat di batas atas dukungan KGP 2.4.21; kenaikan salah satu tanpa menaikkan Kotlin keluar dari rentang. | Naikkan versi sebagai satu paket; cek ulang T5 setiap kali. |
| R2 | Paket platform `android-37` mungkin belum terpasang di runner GitHub. | Langkah CI memasang eksplisit via `sdkmanager` dan mencatat lognya. |
| R3 | Pemetaan BOM 2026.11.01 dibaca dari urutan tabel. | Cek `dependencies`/`dependencyInsight` di CI. |
| R4 | Interaksi built-in Kotlin AGP 9 dengan KSP dan plugin Compose belum ada matriks resmi. | Build CI pertama adalah bukti; bila gagal, kembali ke owner. |
| R5 | `minSdk 24` adalah usulan; bila owner memilih lebih rendah, Chaquopy tidak dapat dipakai (T21). | Putuskan bersama M-19 dan O-04. |
| R6 | `dl.google.com` diblokir di sesi cloud; verifikasi hanya mungkin di GitHub Actions. | Sesuai L-100 (CI sebagai lingkungan build). |
| R7 | DataStore (TD:26) belum punya versi di sini karena status B-7 belum dikonfirmasi. | Tambahkan setelah B-7 selesai. |

## 7. Daftar periksa GitHub Actions (saat implementasi diizinkan)

Tidak ada workflow yang dibuat sekarang. Saat proyek Android diizinkan:

- [ ] `actions/setup-java` dengan JDK 17; log `java -version`.
- [ ] Gradle Wrapper 9.7.0 ter-commit dan tervalidasi; log `./gradlew --version` (Gradle, Kotlin DSL, JVM).
- [ ] Pasang eksplisit `platforms;android-37` dan `build-tools;36.0.0`; log `sdkmanager --list_installed`.
- [ ] `./gradlew buildEnvironment` mencatat AGP 9.3.1, KGP 2.4.21, KSP 2.3.12, plugin Compose 2.4.21.
- [ ] `./gradlew :app:dependencies --configuration releaseRuntimeClasspath` mencatat Compose 1.13.0 / Material3 1.5.0 dari BOM 2026.11.01, Room 2.8.5, Navigation 2.10.2.
- [ ] Tidak ada peringatan kompatibilitas AGP/KGP/KSP di log build; bila ada, catat dan bawa ke owner.
- [ ] `lint`, `testDebugUnitTest`, `assembleDebug` lulus dengan bukti EV-1–EV-6.
- [ ] APK debug: catat `minSdk`, `targetSdk`, `compileSdk` dari `aapt2 dump badging` + SHA-256 (EV-4).

O-01 dapat diusulkan untuk ditutup hanya bila semua butir di atas PASS
dan owner menyetujui kombinasi.

## 8. Ringkasan status

| Item | Status |
|---|---|
| Kombinasi §2 | PROPOSED |
| O-01 | **OPEN** |
| minSdk final | OPEN (M-19, O-04) |
| Runtime Python | OPEN (O-04); Chaquopy **tidak** dipilih — batasnya dicatat agar kombinasi tidak menutup opsi tersebut |
