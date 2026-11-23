# IT ZERO → HERO — Quality Gates

Status: PERSIAPAN. Implementasi aplikasi belum diizinkan.

Dokumen ini menetapkan **cara memverifikasi** implementasi nanti. Ia tidak
menambah, mengurangi, atau mengubah keputusan produk. Jika ada perbedaan,
`docs/BLUEPRINT_LOCKED.md` dan `CLAUDE.md` yang berlaku. Hal yang belum
diputuskan blueprint ditandai **OPEN** dan memerlukan keputusan owner
sebelum diimplementasikan.

Rujukan: `CLAUDE.md`, `docs/BLUEPRINT_LOCKED.md`, `docs/ENVIRONMENT.md`.

## 0. Cara memakai dokumen ini

- Setiap PR implementasi menyebut gate mana yang disentuh dan menyertakan
  bukti untuk gate tersebut.
- Status gate hanya **PASS**, **FAIL**, atau **NOT RUN** (dengan alasan).
  "Seharusnya lulus" bukan status.
- Gate yang belum bisa diuji otomatis diverifikasi manual dengan langkah
  dan hasil yang tertulis.

## 1. Gate bukti (berlaku untuk semua gate lain)

Aturan ini mengikuti larangan `CLAUDE.md`: tidak memalsukan test, hasil
build, atau artefak APK.

| ID | Aturan |
|---|---|
| EV-1 | Setiap klaim build atau test lulus wajib punya bukti log aktual. Tanpa log, statusnya NOT RUN. |
| EV-2 | Bukti dari GitHub Actions mencantumkan: tautan run, commit SHA, nama job, kesimpulan (`success`/`failure`), dan kutipan log yang relevan (mis. ringkasan `BUILD SUCCESSFUL` atau jumlah test lulus/gagal). |
| EV-3 | Bukti dari container Claude Code Cloud mencantumkan perintah yang dijalankan dan output aktualnya. Sesuai `docs/ENVIRONMENT.md`, container ini tidak dipakai untuk build APK. |
| EV-4 | Klaim APK mencantumkan: run asal, nama artefak, varian (`debug`/`release`), ukuran, dan SHA-256 file. |
| EV-5 | Test yang dilewati, dinonaktifkan, atau gagal dilaporkan apa adanya. Test tidak boleh di-skip atau dihapus agar CI hijau. |
| EV-6 | Hasil yang belum diverifikasi ditulis sebagai rencana, bukan sebagai hasil. |

## 2. Gate Android dan build

| ID | Kriteria | Cara verifikasi |
|---|---|---|
| AB-1 | Aplikasi adalah APK Android native: Kotlin, Jetpack Compose, Material 3. Bukan website, PWA, atau WebView sebagai UI utama. | Review kode dan manifest. |
| AB-2 | Arsitektur MVVM + Repository, penyimpanan Room/SQLite. | Review struktur modul dan dependensi. |
| AB-3 | Toolchain (AGP, Gradle Wrapper, JDK, Kotlin, Compose BOM, KSP, SDK level) dipilih sebagai satu kombinasi kompatibel dan disetujui owner (lihat `docs/ENVIRONMENT.md` bagian 4). **OPEN** | Dokumen keputusan versi + build CI sukses. |
| AB-4 | Gradle Wrapper ter-commit dan tervalidasi; versi dependensi terpusat (mis. version catalog). | Log CI langkah validasi wrapper. |
| AB-5 | `lint`, unit test, dan `assembleDebug` lulus di GitHub Actions. | Bukti sesuai EV-2. |
| AB-6 | Tidak ada peringatan lint tingkat error yang diabaikan tanpa alasan tertulis. | Laporan lint sebagai artefak CI. |
| AB-7 | UI: lima tab utama Home, Learn, Lab, Calendar, Progress; tema Colorful Academy terang. | Uji UI/Compose test + tangkapan layar dari build nyata. |
| AB-8 | Aksesibilitas: label untuk pembaca layar, kontras terbaca, target sentuh memadai, teks tetap terbaca saat ukuran font sistem diperbesar. | Compose test berbasis semantics + pemeriksaan manual. |

## 3. Gate offline-first

| ID | Kriteria | Cara verifikasi |
|---|---|---|
| OF-1 | Semua fitur inti (materi, kuis, ujian, lab, penilaian, kalender, progres, backup) berfungsi tanpa koneksi internet. | Uji manual dalam mode pesawat pada build nyata. |
| OF-2 | Video YouTube hanya opsional; ketiadaan internet tidak memblokir modul, penilaian, atau unlocking. | Uji manual offline pada modul yang punya video. |
| OF-3 | Kebutuhan izin `INTERNET` diputuskan secara eksplisit (mis. video dibuka melalui aplikasi/browser eksternal). **OPEN** | Review manifest. |
| OF-4 | Autosave: progres yang sedang dikerjakan tersimpan tanpa tombol simpan manual. | Test repository/ViewModel + uji manual. |
| OF-5 | Crash recovery: setelah aplikasi dimatikan paksa atau process death, pekerjaan terakhir yang tersimpan dipulihkan. | Uji manual (force stop, "Don't keep activities") + test state restoration. |
| OF-6 | Migrasi skema Room teruji; skema diekspor ke repo; tidak memakai migrasi destruktif pada data pengguna. | Room migration test di CI. |
| OF-7 | Local snapshots dapat dibuat dan dipulihkan tanpa kehilangan riwayat percobaan. | Test integrasi data layer. |

## 4. Gate penilaian akademik

Angka berikut disalin dari blueprint terkunci dan **tidak boleh diubah**.

| ID | Kriteria | Cara verifikasi |
|---|---|---|
| GR-1 | Bobot: Theory 30%, Laboratory 40%, Mini-project 20%, Concept explanation 10%. | Unit test kalkulasi skor akhir. |
| GR-2 | Lulus hanya jika skor akhir berbobot ≥ 80 **dan** setiap komponen ≥ 75. | Unit test kasus batas: tepat 80/75, tepat di bawahnya, skor akhir ≥ 80 dengan satu komponen < 75 (harus tidak lulus). |
| GR-3 | Remedial tanpa batas jumlah percobaan. | Unit test: percobaan ke-N tetap diterima. |
| GR-4 | Skor komponen terbaik dipertahankan; semua riwayat percobaan disimpan dan tidak pernah ditimpa. | Unit test repository + test integrasi Room. |
| GR-5 | Ujian teori berwaktu dengan tenggat persisten: tenggat tidak ter-reset oleh restart aplikasi, rotasi layar, atau process death. | Test dengan jam yang dapat dikendalikan (test clock), bukan jam dinding. |
| GR-6 | Sesi lab dan proyek fleksibel (tidak dibatasi waktu seperti ujian teori). | Unit test aturan sesi. |
| GR-7 | Penilaian objektif dan offline; tidak ada AI untuk penilaian maupun tutoring. | Review dependensi dan kode; tidak ada panggilan jaringan pada jalur penilaian. |
| GR-8 | XP terpisah dari nilai akademik: tidak ada penalti XP dan tidak ada XP farming (pengulangan tidak menghasilkan XP tak terbatas). | Unit test aturan XP. |
| GR-9 | Unlocking modul linear: modul berikutnya terbuka sesuai aturan kelulusan. | Unit test + Compose test alur unlock. |
| GR-10 | Aturan pembulatan skor dan dasar skor akhir (mis. dihitung dari skor komponen terbaik) dikonfirmasi terhadap riwayat perencanaan yang disetujui. **OPEN** | Dokumen keputusan + unit test. |

## 5. Gate IT Lab

| ID | Kriteria | Cara verifikasi |
|---|---|---|
| LB-1 | Editor dan eksekusi Python berjalan offline. | Uji manual offline pada build nyata. |
| LB-2 | Runtime Python yang dipakai dipilih dan divalidasi kompatibilitasnya (lisensi, ukuran APK, ABI perangkat, versi Python). Blueprint menyatakan ini wajib divalidasi. **OPEN** | Dokumen keputusan + bukti prototipe sebelum dipakai. |
| LB-3 | Isolasi: kode pengguna tidak dapat membaca/menulis database aplikasi, file backup, atau data di luar area sandbox lab, dan tidak dapat mengakses jaringan. | Test berbasis skrip berbahaya yang diketahui (akses file, jaringan, impor modul sistem) harus ditolak. |
| LB-4 | Batas sumber daya: waktu eksekusi dan output dibatasi; loop tak berujung tidak membekukan atau mematikan aplikasi. | Test timeout + uji manual. |
| LB-5 | Penilaian lab memakai test case objektif yang deterministik. | Unit test penilai dengan jawaban benar, salah, dan kasus tepi. |
| LB-6 | Latihan SQL berjalan pada database latihan terpisah, bukan database aplikasi. | Test yang memastikan database aplikasi tidak berubah. |
| LB-7 | Aktivitas logika dan flowchart dinilai secara objektif. | Unit test penilai. |

## 6. Gate kalender studi

| ID | Kriteria | Cara verifikasi |
|---|---|---|
| CL-1 | Zona waktu `Asia/Tokyo` dipakai secara eksplisit, tidak bergantung pada zona waktu perangkat. | Unit test dengan zona perangkat berbeda. |
| CL-2 | Hari libur nasional Jepang dan hari libur pengganti benar. | Unit test terhadap daftar resmi untuk tahun yang didukung. |
| CL-3 | Sumber data hari libur offline dan mekanisme pembaruannya diputuskan. **OPEN** | Dokumen keputusan. |
| CL-4 | Hari kerja perusahaan dibedakan dari hari libur nasional. | Unit test. |
| CL-5 | Presentasi kalender Jepang ditampilkan sesuai keputusan perencanaan. | Compose test + tangkapan layar. |
| CL-6 | Tidak ada notifikasi pada jam tenang 22:00–07:00 JST, termasuk batas tepat 22:00 dan 07:00. | Unit test dengan test clock. |

## 7. Gate keamanan dan backup

| ID | Kriteria | Cara verifikasi |
|---|---|---|
| SC-1 | Ekspor backup portabel terenkripsi dengan kata sandi, memakai primitif standar yang diautentikasi (mis. AES-GCM) dan KDF kata sandi yang kuat; tidak ada kriptografi buatan sendiri. Algoritma dan parameter final **OPEN**. | Review kode + unit test enkripsi/dekripsi. |
| SC-2 | Kata sandi backup tidak disimpan, tidak di-log, dan tidak dikirim ke mana pun. | Review kode + pemeriksaan log. |
| SC-3 | Restore aman: pratinjau isi, konfirmasi pengguna, validasi file (versi, integritas, kata sandi), dan rollback otomatis bila gagal. | Test integrasi: file rusak, kata sandi salah, versi tidak cocok → data lama utuh. |
| SC-4 | Restore mempertahankan riwayat percobaan; tidak ada riwayat yang hilang diam-diam. | Test integrasi sebelum/sesudah restore. |
| SC-5 | Tidak ada secret, kata sandi, keystore, atau token di repositori. | Pemindaian secret + review PR. |
| SC-6 | Cadangan otomatis sistem Android (`allowBackup`/aturan ekstraksi data) diputuskan secara sadar agar tidak bertentangan dengan backup terenkripsi. **OPEN** | Review manifest. |
| SC-7 | Tidak ada izin Android yang tidak diperlukan. | Review manifest terhadap daftar izin yang disetujui. |

## 8. Gate APK

| ID | Kriteria | Cara verifikasi |
|---|---|---|
| AP-1 | APK debug dihasilkan oleh GitHub Actions, bukan dibuat atau diunggah manual. | Bukti EV-2 dan EV-4. |
| AP-2 | APK terpasang dan berjalan pada perangkat atau emulator nyata. | Catatan uji manual: model/API level perangkat, langkah, hasil. |
| AP-3 | APK rilis ditandatangani melalui workflow terpisah dengan keystore dari GitHub Secrets; hanya dengan persetujuan owner. | Log workflow rilis (tanpa mencetak secret). |
| AP-4 | `versionCode` naik setiap rilis; `versionName` konsisten dengan catatan rilis. | Review PR rilis. |
| AP-5 | Kebijakan minify/R8 dan ukuran APK diputuskan; APK rilis diuji setelah minify. **OPEN** | Bukti build rilis + uji manual. |

## 9. Audit konsistensi dengan blueprint terkunci (2026-11-23)

| Dokumen | Temuan | Status |
|---|---|---|
| `CLAUDE.md` | Sejalan dengan blueprint: APK native, Kotlin/Compose/M3, Room, offline-first, tanpa AI grading, implementasi belum diizinkan. | Konsisten |
| `docs/ENVIRONMENT.md` | Hanya mengatur lingkungan dan rencana CI; tidak mengubah keputusan produk. | Konsisten |
| `docs/QUALITY_GATES.md` | Angka penilaian, aturan kalender, dan keamanan disalin dari blueprint; hal yang belum diputuskan ditandai OPEN. | Konsisten |
| `.claude/skills/*` | Default skill (mis. Hilt, Coil, Navigation 3) bukan keputusan blueprint; harus disetujui sebelum dipakai. | Catatan |

Hal yang perlu keputusan owner sebelum implementasi (OPEN): AB-3, OF-3,
GR-10, LB-2, CL-3, SC-1, SC-6, AP-5.

## 10. Rujukan gate OPEN ke dokumen batch (editorial, 2026-11-23)

Tabel ini hanya menunjuk dokumen terkait. Isi gate di atas tidak diubah,
dan tidak ada gate yang ditutup.

| Gate | Status | Dokumen terkait |
|---|---|---|
| AB-3 | OPEN | [ANDROID_TOOLCHAIN_DECISION_SHEET.md](ANDROID_TOOLCHAIN_DECISION_SHEET.md) (O-01, PROPOSED) |
| OF-3 | OPEN | O-02; [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) |
| GR-10 | OPEN sebagian | Arah "bulatkan hanya untuk tampilan" APPROVED (TD:21); agregasi/representasi di [ASSESSMENT_STATE_MACHINE_SPEC.md](ASSESSMENT_STATE_MACHINE_SPEC.md) OP-1–OP-3 |
| LB-2 | OPEN | [PYTHON_OFFLINE_FEASIBILITY_PLAN.md](PYTHON_OFFLINE_FEASIBILITY_PLAN.md) (O-04) |
| CL-3 | OPEN | Arah APPROVED (TD:23); detail di [JAPAN_CALENDAR_HOLIDAY_SPEC.md](JAPAN_CALENDAR_HOLIDAY_SPEC.md) CO-1–CO-3 |
| SC-1 | OPEN | [ENCRYPTED_BACKUP_RESTORE_SPEC.md](ENCRYPTED_BACKUP_RESTORE_SPEC.md) OD-1 (O-06) |
| SC-6 | OPEN | [ENCRYPTED_BACKUP_RESTORE_SPEC.md](ENCRYPTED_BACKUP_RESTORE_SPEC.md) OD-4 (O-07) |
| AP-5 | OPEN | O-08 |
