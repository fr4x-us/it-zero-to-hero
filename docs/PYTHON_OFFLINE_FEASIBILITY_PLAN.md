# IT ZERO → HERO — Rencana Kelayakan Python Offline (O-04)

Status: PERSIAPAN · RISET DAN RENCANA UJI SAJA · O-04 tetap **OPEN**.
Tanggal pemeriksaan sumber: **2026-11-23**.

Dokumen ini tidak memilih runtime, tidak membuat prototipe, dan tidak
mengubah [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md). Dasar tugas:

- BL §Laboratory: *Offline Python editor and execution* dan *Runtime
  compatibility and isolation require validation*.
- [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md)
  O-04 (TD:45) dan §4 langkah 1: rencana uji kelayakan, tanpa prototipe
  sampai diizinkan terpisah; tidak boleh mengklaim sandbox aman tanpa bukti.
- [`QUALITY_GATES.md`](QUALITY_GATES.md) LB-1 sampai LB-5.

## 0. Label bukti

| Label | Arti |
|---|---|
| **D** | Terdokumentasi di sumber resmi yang dikutip di §1. |
| **A** | Asumsi atau inferensi; belum didukung sumber resmi. |
| **U** | Wajib diuji pada perangkat/emulator nyata sebelum keputusan. |

## 1. Sumber dan keterbatasan riset

Host dokumentasi `chaquo.com`, `docs.python.org`, `pyodide.org`, dan
`docs.micropython.org` **tidak dapat diakses** dari lingkungan sesi ini
(ditolak kebijakan jaringan). Karena itu dokumentasi resmi dibaca dari
**sumber dokumen di repositori resmi proyek** (cabang utama, diambil
2026-11-23), yang merupakan sumber halaman dokumentasi tersebut:

| Kode | Sumber resmi | Isi yang dipakai |
|---|---|---|
| S1 | `github.com/chaquo/chaquopy` — `LICENSE.txt`, `README.md` | Lisensi MIT, deskripsi produk |
| S2 | `chaquo/chaquopy` — `product/runtime/docs/sphinx/versions.rst` | Versi Chaquopy, versi Python, versi AGP, minSdk |
| S3 | `chaquo/chaquopy` — `product/runtime/docs/sphinx/android.rst` | minSdk, ABI, pip saat build |
| S4 | `chaquo/chaquopy` — `product/runtime/docs/sphinx/faq.rst` | Ukuran, proses, interupsi kode |
| S5 | `chaquo/chaquopy` — `product/runtime/docs/sphinx/changelog.rst` | Rilis 17.2.0 (2026-10-26), 17.1.0 (2026-10-12) |
| S6 | `github.com/python/cpython` — `Doc/using/android.rst` | Mode embedded, alat yang direkomendasikan, rilis Android di python.org |
| S7 | `python/peps` — `peps/pep-0011.rst` | Android (`aarch64-linux-android`, `x86_64-linux-android`) di Tier 3 |
| S8 | `python/cpython` — `Doc/library/intro.rst` §Mobile platforms | File I/O, socket, threading berperilaku POSIX; subprocess tidak didukung resmi; `multiprocessing` tidak tersedia |
| S9 | `python/cpython` — `Doc/library/sys.rst` (`addaudithook`) | Audit hook "not suitable for implementing a sandbox" |
| S10 | `python/cpython` — `LICENSE` | Lisensi PSF |
| S11 | `pyodide/pyodide` — `LICENSE` | MPL-2.0 |
| S12 | `micropython/micropython` — `LICENSE`, `README.md` | MIT; daftar port resmi tidak memuat Android |
| S13 | `beeware/briefcase` — `LICENSE` | Lisensi BSD (Briefcase) |
| S14 | developer.android.com — *`<service>` element*, atribut `android:isolatedProcess` (hasil pencarian resmi, 2026-11-23) | Proses terisolasi tanpa izin sendiri; komunikasi hanya lewat Service API |
| S15 | PEP 738 (peps.python.org, via hasil pencarian) | Android sebagai platform CPython sejak 3.13 |

Fakta di bawah yang tidak bersumber S1–S15 diberi label **A** atau **U**.

## 2. Kandidat runtime

| # | Kandidat | Ringkasan | Relevansi untuk Kotlin + Compose native |
|---|---|---|---|
| K1 | **Chaquopy** | SDK Python untuk Android, terintegrasi dengan plugin Gradle Android, API panggilan Kotlin/Java ↔ Python (S1). | Tinggi: dirancang untuk aplikasi Android Studio/Gradle biasa (S1). |
| K2 | **CPython embedded (resmi)** | Interpreter CPython di-embed via `libpython` + JNI/C; rilis Android tersedia di python.org; contoh *testbed app* (S6). Tier 3 (S7). | Sedang: semua integrasi manual (salin `.so` dan stdlib, ekstrak aset, start interpreter dari C lewat JNI) (S6). |
| K3 | **Pyodide di WebView** | CPython yang dikompilasi ke WebAssembly, MPL-2.0 (S11). | Rendah–sedang: bergantung pada WebView; Batch 01 meminta tidak mengasumsikan perilaku WebView (A). |
| K4 | **MicroPython** | Implementasi Python ringkas, MIT (S12). | Rendah: tidak ada port Android resmi (S12) → port NDK sendiri; bukan CPython penuh, berisiko untuk kurikulum Python (A). |
| — | Briefcase, Buildozer/Kivy, Flet | Direkomendasikan S6 untuk "adding Python to an Android app". | Tidak cocok: alat ini membangun aplikasi berpusat Python, bertentangan dengan UI Kotlin/Compose yang terkunci (A). Tidak diuji. |

## 3. Matriks perbandingan

| Kriteria | K1 Chaquopy | K2 CPython embedded | K3 Pyodide/WebView | K4 MicroPython |
|---|---|---|---|---|
| Versi terkini | 17.2.0, 2026-10-26 (D, S5) | Tier 3 sejak 3.13 (D, S7, S15) | U | U |
| Versi Python | 3.10–3.15 pada 17.1–17.2 (D, S2) | Mengikuti rilis CPython (D, S6) | U | Bukan CPython (D, S12) |
| Kompatibilitas AGP | 7.3–9.5 pada 17.2 (D, S2) | Tidak ada plugin; Gradle manual (D, S6) | — | — |
| minSdk | ≥ 24 (D, S3) | U (lihat `Platforms/Android/README.md`) | U (versi WebView) | U |
| ABI | `arm64-v8a`, `x86_64`; `armeabi-v7a`/`x86` hanya Python ≤ 3.11 (D, S3) | `aarch64`, `x86_64` di Tier 3 (D, S7) | Tidak bergantung ABI (A) | Harus dibangun per ABI (A) |
| Lisensi | MIT (D, S1) | PSF (D, S10) | MPL-2.0 (D, S11) | MIT (D, S12) |
| Offline | Paket pip dipasang saat build; runtime ikut dalam APK (D, S3) | Stdlib dan kode dikemas ke aplikasi (D, S6) | Harus membundel semua aset WASM secara lokal (U) | Ya, bila dibundel (A) |
| Ukuran paket | "Each ABI will add several MB" + paket native (D, S3); angka pasti U | U | U (aset WASM besar — A) | Kecil (A) |
| Kompleksitas integrasi | Rendah: plugin Gradle (D, S1) | Tinggi: JNI/C, ekstraksi aset (D, S6) | Sedang: jembatan JS ↔ Kotlin (A) | Tinggi: port NDK sendiri (A) |
| Pemeliharaan | Rilis aktif Oktober 2026 (D, S5) | Didukung CPython, Tier 3 (D, S7) | U | U |
| Model proses | Python berjalan di **proses utama aplikasi**; tidak ada proses Python terpisah (D, S4) | Sama dengan proses yang meng-embed (A) | Proses renderer WebView (A) | Tergantung port (A) |
| Penghentian paksa | Tidak ada; kode harus berhenti sendiri atau dipaksa lewat `PyThreadState_SetAsyncExc` (D, S4) | U | U | U |

## 4. Risiko menjalankan kode Python buatan pengguna

Prinsip: **runtime Python bukan sandbox.** CPython menyatakan audit hook
tidak cocok untuk sandbox dan mudah dilewati (D, S9). File I/O, socket,
dan threading di Android berperilaku seperti POSIX biasa (D, S8). Artinya
kode pengguna memiliki hak yang sama dengan proses tempat ia berjalan.

| Risiko | Bila Python berjalan di proses utama aplikasi | Mitigasi kandidat | Label |
|---|---|---|---|
| R1 Akses file aplikasi | Kode pengguna dapat membaca/menulis file yang dapat diakses proses aplikasi, termasuk database Room dan file backup. | Jalankan interpreter di proses berbeda UID (`android:isolatedProcess`) (S14). | D (S8), mitigasi U |
| R2 Jaringan | Socket berfungsi bila aplikasi memiliki izin `INTERNET`. | Tidak meminta `INTERNET` (terkait O-02) dan/atau proses terisolasi tanpa izin (S14). | D (S8, S14), efek U |
| R3 Modul sistem (`os`, `ctypes`, `subprocess`) | `ctypes` dan modul native dapat melewati pembatasan tingkat Python; subprocess mungkin tetapi tidak didukung resmi (S8). | Pembatasan Python (hapus builtins, audit hook) **bukan** pertahanan (S9); isolasi harus di tingkat OS. | D, U |
| R4 Loop tak berujung | Tidak dapat dihentikan paksa secara andal di proses utama (S4); loop di kode C tidak terinterupsi `PyThreadState_SetAsyncExc` (A). Bila di thread UI → ANR. | Eksekusi di proses terpisah yang dapat dimatikan saat timeout. | D (S4), U |
| R5 Kehabisan memori / crash native | Crash di proses utama mematikan seluruh aplikasi (A); autosave/crash recovery ikut teruji. | Proses terpisah; batas output. | A, U |
| R6 Database aplikasi | Sama dengan R1; latihan SQL juga harus memakai database latihan terpisah (QG LB-6). | Proses terisolasi + database latihan sementara. | U |
| R7 Keluaran besar | Output tak terbatas dapat menghabiskan memori UI. | Batasi ukuran output di sisi Kotlin. | A, U |
| R8 Kompatibilitas proses terisolasi | Proses `isolatedProcess` memakai UID berbeda dan tidak punya izin sendiri (S14); belum diketahui apakah K1/K2 dapat memuat stdlib dan aset dari proses itu. | Uji F-07–F-09. | **U (kritis)** |

Catatan: opsi *"process"* di manifest yang disebut FAQ Chaquopy (S4)
memisahkan crash dan memungkinkan proses dimatikan, tetapi **tidak**
memisahkan UID — akses file aplikasi tetap ada (A, berdasarkan perilaku
proses Android dengan UID sama). Hanya `isolatedProcess` yang
terdokumentasi tanpa izin sendiri (S14).

## 5. Terdokumentasi vs asumsi vs wajib diuji

| Topik | D | A | U |
|---|---|---|---|
| Chaquopy MIT, syarat minSdk ≥ 24, ABI 64-bit, AGP 7.3–9.5, Python 3.10–3.15 | ✓ | | |
| Chaquopy di proses utama, tanpa penghentian paksa | ✓ | | |
| CPython Android Tier 3, embedded via JNI, rilis python.org | ✓ | | |
| Audit hook bukan sandbox | ✓ | | |
| `isolatedProcess` tanpa izin, komunikasi lewat Service API | ✓ | | |
| Ukuran APK nyata per ABI | | | ✓ |
| Runtime dapat berjalan di `isolatedProcess` | | | ✓ |
| Proses terisolasi tidak dapat membuka DB/backup aplikasi | | ✓ (inferensi dari UID berbeda) | ✓ |
| Tanpa `INTERNET`, socket Python gagal | | ✓ | ✓ |
| Timeout via mematikan proses cukup cepat dan aplikasi pulih | | | ✓ |
| Waktu start interpreter dapat diterima | | | ✓ |
| Perilaku Pyodide/WebView offline | | | ✓ |

## 6. Matriks uji kelayakan (dijalankan hanya setelah prototipe diizinkan)

Target perangkat minimal: satu perangkat fisik `arm64-v8a` dan satu
emulator `x86_64`; minSdk **29** (D-05; semula "mengikuti O-01, ≥ 24 bila K1" — SUPERSEDED).
Semua hasil wajib memakai bukti EV-1–EV-6 ([`QUALITY_GATES.md`](QUALITY_GATES.md)).

| ID | Uji | PASS | FAIL | Gate |
|---|---|---|---|---|
| F-01 | Build APK debug dengan runtime di GitHub Actions | Build sukses, log tersedia | Build gagal tanpa jalan keluar terdokumentasi | AB-5, LB-2 |
| F-02 | `print("halo")` dan stdlib dasar dalam mode pesawat | Output benar, tanpa jaringan | Butuh jaringan / crash | LB-1 |
| F-03 | Ukuran APK per ABI (`arm64-v8a`, `x86_64`) | Tercatat dan diterima owner | Melebihi batas yang owner tetapkan | LB-2 |
| F-04 | Waktu start interpreter (dingin dan hangat) | Tercatat; dalam batas yang ditetapkan owner | Melebihi batas | LB-1 |
| F-05 | Cakupan kurikulum: skrip contoh minggu 9–12 (variabel, kondisi, loop, fungsi, debugging) | Semua berjalan sesuai harapan | Fitur bahasa yang dibutuhkan tidak tersedia | LB-1 |
| F-06 | Penilai test case objektif deterministik | Hasil sama pada 10 kali ulang | Hasil berbeda | LB-5 |
| F-07 | Runtime berjalan di `isolatedProcess` | Interpreter start dan mengembalikan hasil lewat Binder | Tidak dapat start / tidak dapat memuat stdlib | LB-3 |
| F-08 | Skrip uji membaca DB Room, file backup, `filesDir` aplikasi | Semua ditolak | Salah satu terbaca/tertulis | LB-3 |
| F-09 | Skrip uji membuka socket / HTTP | Gagal | Koneksi berhasil | LB-3 |
| F-10 | Skrip uji `ctypes`, `os.system`, `subprocess` | Tidak dapat menyentuh data aplikasi atau jaringan | Ada akses data/jaringan | LB-3 |
| F-11 | `while True: pass` dan loop di kode C | Dihentikan ≤ batas waktu; UI responsif; tanpa ANR | Aplikasi beku/ANR/crash | LB-4 |
| F-12 | Alokasi memori besar | Proses eksekusi berakhir; aplikasi utama tetap hidup | Aplikasi utama crash | LB-4 |
| F-13 | Output sangat besar | Dipotong sesuai batas | UI beku / OOM | LB-4 |
| F-14 | Process death di tengah eksekusi | Kode lab tersimpan (autosave) dan dipulihkan | Kode hilang | OF-4, OF-5 |
| F-15 | Lisensi pihak ketiga dalam APK | Daftar lisensi lengkap dan kompatibel | Lisensi tak jelas/tidak kompatibel | LB-2 |

O-04 hanya dapat diusulkan untuk ditutup bila F-01–F-15 PASS pada kedua
target dan owner menyetujui.

## 7. Kondisi yang wajib dibawa kembali ke owner

Hentikan dan minta keputusan owner bila salah satu terjadi:

1. **F-07 atau F-08 FAIL** — isolasi OS tidak tercapai. Pilihan arsitektur
   (mis. membatasi lab Python ke subset yang dieksekusi interpreter
   terbatas, menerima risiko terdokumentasi, atau mengubah cakupan lab)
   memengaruhi kontrak produk dan butuh persetujuan.
2. **F-11 atau F-12 FAIL** — kode pengguna dapat membekukan/mematikan
   aplikasi.
3. **F-03 atau F-04** melebihi batas, atau batas belum ditetapkan owner.
4. *(Tidak berlaku lagi: minSdk 29 ditetapkan D-05, memenuhi syarat K1 ≥ 24.)*
5. Kandidat satu-satunya yang lolos adalah **K3 (WebView)** atau **K4
   (bukan CPython)** — keduanya menyentuh guardrail Batch 01 atau
   kecocokan kurikulum.
6. Lisensi (F-15) atau pemeliharaan kandidat bermasalah.
7. Ditemukan kebutuhan izin `INTERNET` untuk runtime (bertentangan dengan
   O-02 yang masih OPEN).

## 8. Yang belum diputuskan

- Runtime final: **OPEN** (O-04).
- Batas waktu eksekusi, memori, output, ukuran APK, dan waktu start:
  **OPEN**, ditetapkan owner sebelum uji.
- Mekanisme komunikasi proses (Binder/AIDL/Messenger): **OPEN**, ditentukan
  saat prototipe diizinkan.
- Urutan uji yang disarankan (bukan keputusan): K1 lebih dulu karena
  integrasi Gradle-nya terdokumentasi (S1–S3), K2 sebagai pembanding bila
  F-07 gagal pada K1, K3/K4 hanya bila K1 dan K2 gagal.

## 9. Keputusan owner D-10 dan D-08 (2026-11-23)

**D-10: PLANNING APPROVED; EXECUTION NOT AUTHORIZED.** Cakupan F-01–F-15 dan
ambang penerimaan berikut disetujui sebagai **keputusan perencanaan**. Ini
ambang yang diusulkan, **bukan** hasil pengukuran. F-01–F-15 tetap
**NOT VERIFIED**; runtime final **tidak** dipilih.

| Uji | Ambang PASS yang disetujui |
|---|---|
| F-03 Ukuran APK | ≤ 100 MB per ABI |
| F-04 Start interpreter dingin | ≤ 5 detik |
| F-11 Batas waktu eksekusi | 3 detik per latihan; aplikasi tetap responsif, tanpa ANR |
| F-12 Memori | Target batas memori proses Python 128 MB; aplikasi utama tetap hidup bila batas terlampaui. Apakah Android dapat menegakkan batas memori per proses **belum diverifikasi** |
| F-13 Output | ≤ 64 KB per eksekusi; sisanya dipotong |
| Target uji | 1 perangkat fisik ARM64 + 1 emulator x86_64 |
| API minimum | 29 |

Syarat eksekusi prototipe (belum terpenuhi):
1. Kebutuhan perencanaan yang tersisa selesai.
2. Izin owner terpisah yang eksplisit.
3. Cakupan eksperimental terisolasi, bukan kode produksi.

**D-08 (`INTERNET` diizinkan untuk fitur opsional):** aplikasi akan
memiliki izin jaringan, sehingga F-09 (kode pengguna tidak dapat membuka
socket/HTTP) menjadi **syarat wajib** yang harus dibuktikan oleh isolasi
proses, bukan oleh ketiadaan izin aplikasi. Threat model, isolasi proses,
dan uji penolakan jaringan wajib. F-09 tetap **NOT VERIFIED**; tidak ada
klaim sandbox aman.
