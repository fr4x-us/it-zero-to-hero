# IT ZERO → HERO — Owner Decision Checklist (P0)

Status: D-01 **APPROVED** · D-02–D-09 **OWNER APPROVED** (tunduk pada
verifikasi yang tersisa) · D-10 **PLANNING APPROVED; EXECUTION NOT
AUTHORIZED** · D-11 **DEFERRED; IMPLEMENTATION NOT AUTHORIZED** · D-12–D-15
**OWNER APPROVED** (2026-11-24; verifikasi implementasi NOT VERIFIED) · D-16–D-22 **OWNER APPROVED** (2026-11-24; D-16 bersyarat verifikasi teknis) · D-23–D-25 **OWNER APPROVED** (2026-11-24) · D-26–D-38 **OWNER APPROVED** (2026-11-24) · W01-ACC **OWNER ACCEPTED** (2026-11-24) · tidak
ada keputusan yang diisi atas nama owner · **PLANNING CLEAR: NO** ·
**IMPLEMENTATION VERIFIED: NO**.
Tanggal: **2026-11-23**. Basis awal: `main` = `5931ece` (merge PR #16);
D-01 dicatat pada basis `4eacaa0` (merge PR #17); D-02–D-11 dicatat pada basis `777f5dc` (merge PR #18).

Sumber register: [`BATCH_01_10_UNFINISHED_AUDIT.md`](BATCH_01_10_UNFINISHED_AUDIT.md)
§3 (UW-01–UW-11). Blueprint terkunci: [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md).

Kolom **Rekomendasi teknis** adalah saran Claude, **bukan** keputusan.
Kolom **Keputusan final** hanya diisi berdasarkan jawaban tertulis owner
(melalui PR yang disetujui). D-01–D-11 kini terisi sesuai keputusan owner 2026-11-23; kolom Rekomendasi teknis tetap dipertahankan sebagai catatan historis.

## 0. Urutan berdasarkan ketergantungan

```
D-01 Batch 01 (UW-01)
 ├─► D-02 DataStore (UW-05)
 ├─► D-03 Mode restore (UW-09) ──► D-07 Auto Backup (UW-06)
 ├─► D-04 Agregasi skor & basis lulus (UW-11)
 └─► D-05 minSdk (UW-04) ──► D-06 Toolchain (UW-03) ──► D-09 Stack test (UW-08)
D-08 INTERNET (UW-07)                (independen; memengaruhi D-07, D-10)
D-10 Izin prototipe O-04 (UW-10)     (butuh D-05; terkait D-08)
D-11 Izin implementasi (UW-02)       (butuh D-01–D-09; terpisah dari D-10)
```

| Kelompok | Butir |
|---|---|
| A. Keputusan produk dan data | D-01, D-02, D-03, D-04, D-07, D-08 |
| B. Keputusan teknis | D-05, D-06, D-09 |
| C. Izin prototipe | D-10 |
| D. Izin implementasi | D-11 |

## A. Keputusan produk dan data

### D-01 — Status persetujuan Batch 01 (UW-01)

| Butir | Isi |
|---|---|
| Sumber | [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) (semula DRAFT, kini §7); HANDOFF B-3; OP-12, CO-7, UO-10 |
| Masalah | Dokumen sudah di-merge (PR #5) tetapi header masih *DRAFT FOR OWNER REVIEW*; Batch 05–09 memakai isinya sebagai RECOVERED/PROPOSED; TD:25 menyebut palet/guardrail-nya "approved" |
| Pilihan | (a) Setujui seluruhnya; (b) setujui dengan revisi tertulis per butir M; (c) tolak sebagian (sebutkan butir) |
| Rekomendasi teknis | (b) bila ada butir yang ingin diubah, selain itu (a). Keputusan ini membuka paling banyak butir lain |
| Risiko (a) | Detail yang belum ditinjau ikut terkunci |
| Risiko (b) | Butuh waktu meninjau 19 butir M |
| Risiko (c) | Butir yang ditolak harus ditulis ulang; dokumen Batch 05–09 perlu diselaraskan |
| Ketergantungan | Tidak ada; menjadi prasyarat D-02, D-03, D-04, UW-19, UW-20 |
| Status | **APPROVED BY OWNER** (2026-11-23) — dicatat lewat PR dokumentasi D-01; berlaku efektif setelah PR itu di-merge |
| Keputusan final | Opsi (a) dengan ketentuan: owner menyetujui M-01–M-19 sebagaimana dirinci di [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) §7.1; seluruh detail teknis, konten, dan pengujian yang belum selesai tetap OPEN/PARTIAL; M-09 belum selesai; blueprint tidak berubah; tidak ada izin implementasi/prototipe |
| Dampak | Membuka tindak lanjut UW-19 (status palet: dikonfirmasi M-17), UW-20 (kerangka 16 minggu: disetujui M-02), dan UW-45 (penyeragaman label). Status butir-butir itu **belum** diubah di PR ini. Konflik restore (D-03) dan DataStore (D-02) tetap terbuka |

### D-02 — DataStore dalam baseline (UW-05)

| Butir | Isi |
|---|---|
| Sumber | TD:26 vs BL:11; DECISIONS_LOG K-1; HANDOFF B-7 |
| Masalah | Batch 02 menyebut DataStore sebagai "existing blueprint baseline", padahal blueprint hanya menyebut Room/SQLite |
| Pilihan | (a) DataStore disetujui sebagai tambahan baseline; (b) tidak dipakai di V1 (preferensi disimpan di Room); (c) ditunda sampai ada kebutuhan konkret |
| Rekomendasi teknis | (a) atau (c). DataStore cocok untuk preferensi ringan, tetapi harus dicatat sebagai keputusan baru, bukan bagian blueprint |
| Risiko (a) | Satu dependensi tambahan; masuk Auto Backup bila tidak dikecualikan (D-07) |
| Risiko (b) | Preferensi bercampur dengan data akademik di Room |
| Risiko (c) | Ketidakjelasan saat scaffold |
| Ketergantungan | D-01 (konsistensi sumber); memengaruhi D-06 |
| Status | **OWNER APPROVED** (2026-11-23) — tunduk pada verifikasi yang tersisa; berlaku efektif setelah PR pencatatan D-02–D-11 di-merge |
| Keputusan final | Opsi (a): Jetpack DataStore ditambahkan ke arsitektur rencana **hanya untuk preferensi aplikasi**; Room/SQLite tetap sumber kebenaran data akademik. Versi DataStore **OPEN** sampai verifikasi kompatibilitas. Tidak ada perubahan arsitektur lain. Ini keputusan baru owner, bukan bagian blueprint (TD:26 dikoreksi oleh keputusan ini) |

### D-03 — Mode restore backup (UW-09)

| Butir | Isi |
|---|---|
| Sumber | BL:63–64; B01 M-16; [`ENCRYPTED_BACKUP_RESTORE_SPEC.md`](ENCRYPTED_BACKUP_RESTORE_SPEC.md) §6.2, OD-3 |
| Masalah | Blueprint meminta riwayat percobaan dipertahankan saat restore; B01 melarang penggabungan riwayat nilai otomatis. Restore "ganti total" bisa menghilangkan attempt yang tidak ada di file backup |
| Pilihan | BKP:M-1 ganti total + snapshot pra-restore disimpan; BKP:M-2 tolak restore bila data aktif punya attempt yang tidak ada di backup; BKP:M-3 gabung berbasis ID stabil (append saja) |
| Rekomendasi teknis | BKP:M-2 sebagai default aman, BKP:M-1 sebagai opsi eksplisit dengan peringatan |
| Risiko BKP:M-1 | Riwayat hanya ada di snapshot; butuh kebijakan retensi |
| Risiko BKP:M-2 | Pengguna bisa terhalang memulihkan data |
| Risiko BKP:M-3 | Bertentangan dengan "no automatic merging" kecuali owner mengizinkan |
| Ketergantungan | D-01 (status B01 M-16); memengaruhi D-07 dan model data attempt |
| Status | **OWNER APPROVED** (2026-11-23) — tunduk pada verifikasi yang tersisa; berlaku efektif setelah PR pencatatan D-02–D-11 di-merge |
| Keputusan final | **BKP:M-2 default aman**: restore ditolak bila akan menghilangkan attempt akademik yang ada di data aktif tetapi tidak ada di backup. **BKP:M-1 hanya sebagai pilihan eksplisit pengguna** (penggantian penuh) dengan peringatan jelas, konfirmasi eksplisit, dan snapshot pra-restore yang berhasil dibuat serta dapat dipulihkan. **Tanpa penggabungan riwayat nilai otomatis** (BKP:M-3 ditolak). OPEN: retensi snapshot, batas penyimpanan, detail rollback, parameter kriptografi |

### D-04 — Agregasi skor dan basis kelulusan (UW-11)

| Butir | Isi |
|---|---|
| Sumber | BL:27–34; TD:21, TD:32; [`ASSESSMENT_STATE_MACHINE_SPEC.md`](ASSESSMENT_STATE_MACHINE_SPEC.md) OP-1, OP-2; CU-2 |
| Masalah | (1) Cakupan "unit penilaian": per modul, per fase, atau program. (2) Apakah keputusan lulus memakai skor terbaik per komponen |
| Pilihan cakupan | (a) per modul; (b) per fase; (c) per program; (d) kombinasi (mis. modul untuk unlock, program untuk kelulusan akhir) |
| Pilihan basis | (i) skor terbaik per komponen; (ii) skor attempt terakhir; (iii) aturan lain yang owner tetapkan |
| Rekomendasi teknis | (d) dengan (i): unlock linear per modul, kelulusan akhir dari agregasi yang owner tetapkan; (i) adalah tafsiran paling langsung atas BL:34 |
| Risiko (a) | Banyak ujian kecil; beban siswa |
| Risiko (b)/(c) | Unlock modul butuh aturan terpisah |
| Risiko (ii) | Remedial yang lebih buruk menurunkan status — bertentangan dengan semangat BL:34 |
| Ketergantungan | D-01; memengaruhi model data, CU-2, UW-22 |
| Status | **OWNER APPROVED** (2026-11-23) — tunduk pada verifikasi yang tersisa; berlaku efektif setelah PR pencatatan D-02–D-11 di-merge |
| Keputusan final | Skor terbaik per komponen; setiap attempt disimpan. **Kelulusan modul**: nilai tertimbang ≥ 80 dan setiap komponen ≥ 75, tanpa pembulatan. Modul berikutnya terbuka linear setelah modul sebelumnya lulus. **Penyelesaian program**: seluruh 16 modul lulus **dan** capstone selesai menurut rubrik yang akan disetujui kemudian. Tidak ada rata-rata program atau ambang tambahan baru. OPEN: agregasi numerik tingkat program, representasi angka, rubrik capstone |

### D-07 — Kebijakan Android Auto Backup (UW-06)

| Butir | Isi |
|---|---|
| Sumber | TD:48 (O-07); [`ENCRYPTED_BACKUP_RESTORE_SPEC.md`](ENCRYPTED_BACKUP_RESTORE_SPEC.md) §7, OD-4 |
| Masalah | Auto Backup aktif secara default; database bisa terunggah ke Google Drive; E2E hanya di Android 9+ dengan kunci layar; sebagian perangkat tetap melakukan transfer antarperangkat walau `allowBackup=false` |
| Pilihan | BKP:AB-1 `allowBackup=false`; BKP:AB-2 izinkan tetapi kecualikan database dan snapshot; BKP:AB-3 izinkan semua |
| Rekomendasi teknis | BKP:AB-1 atau BKP:AB-2, diputuskan bersama D-03 |
| Risiko BKP:AB-1 | Pengguna hanya mengandalkan ekspor manual; D2D mungkin tetap terjadi |
| Risiko BKP:AB-2 | Aturan ekstraksi harus diuji untuk cloud dan D2D di API ≤ 30 dan ≥ 31 |
| Risiko BKP:AB-3 | Data akademik di cloud tanpa enkripsi aplikasi; restore otomatis melewati alur restore aman |
| Ketergantungan | D-03; D-02 (bila DataStore dipakai) |
| Status | **OWNER APPROVED** (2026-11-23) — tunduk pada verifikasi yang tersisa; berlaku efektif setelah PR pencatatan D-02–D-11 di-merge |
| Keputusan final | **BKP:AB-1**: Android Auto Backup dinonaktifkan; aplikasi memakai mekanisme backup terenkripsinya sendiri (selaras D-03). `allowBackup=false` **tidak** dianggap menjamin semua jalur transfer tercegah; perilaku transfer antarperangkat (termasuk pengecualian per produsen) **wajib diverifikasi** (NOT VERIFIED) |

### D-08 — Izin `INTERNET` (UW-07)

| Butir | Isi |
|---|---|
| Sumber | BL:10, BL:24; O-02; QG OF-3; PY:F-09; CAL:U-3 |
| Masalah | Video YouTube opsional butuh jaringan; izin `INTERNET` juga membuka akses jaringan bagi kode lab bila isolasi gagal |
| Pilihan | (a) Tanpa `INTERNET`; video dibuka di aplikasi/browser eksternal; (b) dengan `INTERNET` untuk fitur opsional |
| Rekomendasi teknis | (a) untuk V1 |
| Risiko (a) | Tidak ada pembaruan data/konten lewat jaringan (sesuai offline-first) |
| Risiko (b) | Permukaan serangan lebih besar; lab Python bisa mengakses jaringan bila isolasi gagal |
| Ketergantungan | Independen; memengaruhi D-07, D-10, CO-2 |
| Status | **OWNER APPROVED** (2026-11-23) — tunduk pada verifikasi yang tersisa; berlaku efektif setelah PR pencatatan D-02–D-11 di-merge |
| Keputusan final | **Opsi (b)**: izin `INTERNET` diperbolehkan untuk fitur opsional. Fitur belajar inti tetap berfungsi offline. Eksekusi lab Python **tidak boleh** mendapat akses jaringan; threat model, isolasi proses, dan uji penolakan jaringan **wajib**. PY:F-09 tetap feasibility gate yang **NOT VERIFIED**. Tidak ada klaim sandbox aman |

## B. Keputusan teknis

### D-05 — minSdk (UW-04)

| Butir | Isi |
|---|---|
| Sumber | [`ANDROID_TOOLCHAIN_DECISION_SHEET.md`](ANDROID_TOOLCHAIN_DECISION_SHEET.md) §2 (usulan 24); BKP §4.1; PY §3; M-19; HANDOFF B-9; OD-10 |
| Masalah | Batas bawah versi Android |
| Pilihan | (a) 24; (b) 26; (c) lebih tinggi |
| Rekomendasi teknis | (b) 26 dipertimbangkan |
| Alasan | Chaquopy butuh ≥ 24; `PBKDF2withHmacSHA256` platform baru tersedia di API 26+; AndroidX default 23 |
| Risiko (a) | Kandidat KDF platform terbatas di API 24–25 |
| Risiko (b) | Jangkauan perangkat sedikit berkurang (data jangkauan perangkat belum diperiksa) |
| Risiko (c) | Jangkauan berkurang lebih jauh |
| Ketergantungan | D-01 (M-19); memengaruhi D-06, D-10, OD-1 |
| Status | **OWNER APPROVED** (2026-11-23) — tunduk pada verifikasi yang tersisa; berlaku efektif setelah PR pencatatan D-02–D-11 di-merge |
| Keputusan final | **minSdk = 29 (Android 10)**. Menggantikan usulan minSdk 24 (Batch 04) dan rekomendasi teknis 26 (keduanya kini SUPERSEDED) |

### D-06 — Kombinasi toolchain (UW-03)

| Butir | Isi |
|---|---|
| Sumber | [`ANDROID_TOOLCHAIN_DECISION_SHEET.md`](ANDROID_TOOLCHAIN_DECISION_SHEET.md); O-01; TD:47; QG AB-3 |
| Masalah | Menyetujui satu kombinasi versi |
| Pilihan | (a) Kombinasi PROPOSED (AGP 9.3.1, Gradle 9.7.0, JDK 17, Kotlin 2.4.21, BOM 2026.11.01, KSP 2.3.12, Room 2.8.5, Navigation 2.10.2, compileSdk 37, targetSdk 36); (b) alternatif ALT-1–ALT-5; (c) minta pengecekan ulang tepat sebelum scaffold |
| Rekomendasi teknis | (a) disetujui **arahnya**, dengan (c) wajib dijalankan sebelum scaffold (TD:47) |
| Risiko (a) | AGP dan Gradle tepat di batas atas dukungan Kotlin 2.4.21; beberapa pasangan berlabel V |
| Risiko (b) | ALT-4 keluar dari rentang dukungan Kotlin |
| Risiko (c) | Tanpa persetujuan arah, scaffold tetap tertahan |
| Ketergantungan | D-05; D-02 (versi DataStore) |
| Status | **OWNER APPROVED AS PROVISIONAL BASELINE** (2026-11-23) — belum terverifikasi build |
| Keputusan final | Baseline sementara: AGP 9.3.1 · Gradle 9.7.0 · JDK 17 · Kotlin 2.4.21 · Compose Compiler 2.4.21 · Compose BOM 2026.11.01 · KSP 2.3.12 · Room 2.8.5 · Navigation Compose 2.10.2 · compileSdk 37 · targetSdk 36 · minSdk 29 · Build Tools 36.0.0 · DataStore (versi belum dipilih). Ketersediaan dan kompatibilitas semua dependensi **wajib dicek ulang sebelum scaffold** dan **diverifikasi di CI hanya setelah izin implementasi terpisah**. **Tidak** build-verified |

### D-09 — Stack test minimal (UW-08)

| Butir | Isi |
|---|---|
| Sumber | O-16; UI UO-8; skill `android-testing` |
| Masalah | Alat unit test, test UI Compose, dan screenshot test belum dipilih |
| Pilihan | (a) JUnit + kotlinx-coroutines-test + Compose UI test (instrumented); (b) (a) + Robolectric untuk test UI di JVM; (c) (b) + alat screenshot test (kandidat disebut skill: Roborazzi, Paparazzi, Compose Preview Screenshot Testing) |
| Rekomendasi teknis | (b) untuk milestone pertama; alat screenshot dipilih saat milestone UI |
| Risiko (a) | Test UI hanya jalan di emulator/perangkat (butuh O-09) |
| Risiko (b) | Robolectric perlu diverifikasi dengan toolchain D-06 |
| Risiko (c) | Lebih banyak dependensi sebelum ada UI |
| Ketergantungan | D-06; O-09 (runner) |
| Status | **OWNER APPROVED** (2026-11-23) — tunduk pada verifikasi yang tersisa; berlaku efektif setelah PR pencatatan D-02–D-11 di-merge |
| Keputusan final | **Opsi (b)**: baseline awal JUnit, kotlinx-coroutines-test, Compose UI Test, Robolectric. Alat screenshot test dipilih pada milestone UI. Robolectric dan semua dependensi test wajib diverifikasi terhadap toolchain D-06. Tidak membuat test, infrastruktur test, atau workflow CI sekarang |

## C. Izin prototipe

### D-10 — Batas uji dan izin prototipe kelayakan O-04 (UW-10)

| Butir | Isi |
|---|---|
| Sumber | [`PYTHON_OFFLINE_FEASIBILITY_PLAN.md`](PYTHON_OFFLINE_FEASIBILITY_PLAN.md) §6–8; TD:45, TD:60 |
| Masalah | Uji PY:F-01–PY:F-15 butuh (1) batas angka dan (2) izin prototipe terbatas |
| Angka yang dibutuhkan | Ukuran APK maksimum per ABI (PY:F-03); waktu start interpreter maksimum (PY:F-04); batas waktu eksekusi (PY:F-11); batas memori (PY:F-12); batas output (PY:F-13); perangkat uji |
| Pilihan | (a) Izinkan prototipe terbatas setelah batas ditetapkan; (b) tunda; (c) tolak dan putuskan alternatif lab minggu 9–12 (CU-8) |
| Rekomendasi teknis | (a). Prototipe hanya untuk PY:F-01–PY:F-15, terpisah dari aplikasi, tidak menjadi dasar kode produksi tanpa izin implementasi |
| Risiko (a) | Waktu pengerjaan; hasil bisa gagal dan memicu eskalasi |
| Risiko (b) | Lab Python tetap tidak dapat direncanakan |
| Risiko (c) | Mengubah cakupan kurikulum terkunci (BL:19, BL:41) — butuh revisi blueprint |
| Ketergantungan | D-05 (minSdk); D-08 (jaringan); izin ini **tidak** sama dengan D-11 |
| Status | **PLANNING APPROVED; EXECUTION NOT AUTHORIZED** (2026-11-23) |
| Batas yang ditetapkan owner | APK maks. 100 MB per ABI (PY:F-03) · start interpreter dingin maks. 5 detik (PY:F-04) · batas waktu eksekusi 3 detik per latihan (PY:F-11) · target batas memori proses Python 128 MB (PY:F-12) · output maks. 64 KB per eksekusi (PY:F-13) · target uji: 1 perangkat fisik ARM64 + 1 emulator x86_64 · API minimum 29. **Ambang penerimaan yang diusulkan, bukan hasil pengukuran** |
| Keputusan final | Cakupan dan ambang penerimaan PY:F-01–PY:F-15 disetujui **sebagai keputusan perencanaan**. Prototipe **tidak** diizinkan untuk diimplementasikan atau dijalankan sekarang. Eksekusi butuh: (1) penyelesaian kebutuhan perencanaan yang tersisa; (2) izin owner terpisah yang eksplisit; (3) cakupan eksperimental yang terisolasi. Runtime final **tidak** dipilih; PY:F-01–PY:F-15 **NOT VERIFIED** |

## D. Izin implementasi

### D-11 — Izin implementasi tahap pertama (UW-02)

| Butir | Isi |
|---|---|
| Sumber | `CLAUDE.md` (implementation not authorized); BL:74; HANDOFF B-1 |
| Masalah | Kapan kerangka proyek Android + workflow CI boleh dibuat |
| Pilihan | (a) Izinkan tahap pertama terbatas (scaffold + CI build/lint/unit test, tanpa fitur) setelah D-01–D-09; (b) tunda |
| Rekomendasi teknis | (a) hanya setelah D-01–D-09 terjawab; ruang lingkup tahap pertama ditulis eksplisit |
| Risiko (a) | Keputusan yang masih terbuka di P1/P2 dapat memaksa refaktor kemudian |
| Risiko (b) | Toolchain tidak pernah terbukti; versi menua |
| Ketergantungan | D-01–D-09 |
| Status | **DEFERRED — IMPLEMENTATION NOT AUTHORIZED** (2026-11-23) |
| Keputusan final | Owner menulis "D-11 opsi A", tetapi instruksi substantifnya adalah **menunda** implementasi; opsi (a) di checklist ini berarti mengizinkan scaffold terbatas, sehingga **tidak** dicatat sebagai opsi (a). Keputusan yang dicatat: selesaikan dulu seluruh butir perencanaan Batch 01–10 yang belum selesai; PLANNING CLEAR: YES hanya setelah penyelesaian terdokumentasi dan direview; minta izin owner baru yang eksplisit sebelum implementasi apa pun. Tetap dilarang: coding aplikasi, scaffold Android, proyek Gradle, workflow CI, implementasi/eksekusi prototipe Python, build APK, instalasi skill tambahan, auto-merge PR |

## Ringkasan

| ID | Keputusan | Kelompok | Status | Keputusan final |
|---|---|---|---|---|
| D-01 | Status Batch 01 | Produk | **APPROVED BY OWNER** (2026-11-23) | Setujui M-01–M-19 dengan ketentuan (lihat D-01) |
| D-02 | DataStore | Produk/data | OWNER APPROVED | (a) preferensi saja; Room sumber kebenaran; versi OPEN |
| D-03 | Mode restore | Produk/data | OWNER APPROVED | BKP:M-2 default; BKP:M-1 eksplisit + snapshot; tanpa auto-merge |
| D-04 | Agregasi skor + basis lulus | Produk | OWNER APPROVED | Skor terbaik; lulus per modul; program = 16 modul + capstone; agregasi program OPEN |
| D-05 | minSdk | Teknis | OWNER APPROVED | 29 |
| D-06 | Toolchain | Teknis | OWNER APPROVED (provisional) | Baseline sementara; belum build-verified |
| D-07 | Auto Backup | Produk/data | OWNER APPROVED | BKP:AB-1; D2D NOT VERIFIED |
| D-08 | `INTERNET` | Produk | OWNER APPROVED | (b) untuk fitur opsional; lab Python tanpa jaringan (PY:F-09 NOT VERIFIED) |
| D-09 | Stack test | Teknis | OWNER APPROVED | (b) JUnit, coroutines-test, Compose UI Test, Robolectric |
| D-10 | Prototipe O-04 | Izin prototipe | PLANNING APPROVED; EXECUTION NOT AUTHORIZED | Ambang disetujui; prototipe tidak diizinkan |
| D-11 | Implementasi tahap pertama | Izin implementasi | DEFERRED; NOT AUTHORIZED | Selesaikan perencanaan dulu; izin baru diperlukan |

Cara menjawab: owner mengirim jawaban per ID (mis. "D-03: BKP:M-2"). Claude
mencatatnya di PR terpisah, memperbarui DECISIONS_LOG, dan mengubah
status menjadi APPROVED hanya setelah PR itu disetujui.

## Catatan konsistensi saat pencatatan D-02–D-11

| # | Temuan | Penanganan |
|---|---|---|
| 1 | D-05 (minSdk 29) menggantikan usulan 24 (Batch 04) dan rekomendasi 26. | Dokumen terkait diberi label SUPERSEDED; nilai lama dipertahankan sebagai riwayat |
| 2 | D-08 opsi (b) berbeda dari rekomendasi teknis (a). Akibatnya isolasi jaringan lab Python menjadi syarat wajib, bukan sekadar efek samping tanpa izin. | Dicatat di Python plan §9 |
| 3 | D-11: label "opsi A" vs instruksi menunda. | Dicatat sebagai DEFERRED sesuai instruksi substantif owner |
| 4 | D-04 menetapkan kelulusan per modul dengan empat komponen. Implikasinya: setiap modul memerlukan keempat komponen penilaian (termasuk mini-project dan penjelasan konsep). | **Tidak** diselesaikan diam-diam; dicatat sebagai implikasi yang perlu dikonfirmasi pada CU-2 |
| 5 | D-04: "16 modul lulus dan capstone selesai" — capstone juga merupakan minggu 16 di kerangka kurikulum. | Hubungan modul 16 dengan capstone dan rubriknya tetap OPEN (CU-9) |
| 6 | D-10: batas memori 128 MB adalah target; kemampuan Android menegakkan batas memori per proses belum diverifikasi. | Tetap bagian PY:F-12 (NOT VERIFIED) |

## Antrean keputusan berikutnya (bukan P0) — disiapkan 2026-11-23

Semua butir di bawah telah dijawab owner pada 2026-11-24 (D-12–D-15). Kolom
rekomendasi dipertahankan sebagai catatan historis.

| ID | Pertanyaan | Rekomendasi teknis | Lembar keputusan | Keputusan final |
|---|---|---|---|---|
| UW-22-Q1 | Representasi skor | NP-4 (integer rasional dari poin mentah) | [NUMERIC_PRECISION_DECISION_SHEET.md](NUMERIC_PRECISION_DECISION_SHEET.md) §8 | D-12: NP-4 disetujui |
| UW-22-Q2 | Batas poin maksimum per komponen per attempt | `max ≤ 10.000` | idem | D-12: `max ≤ 10.000` disetujui |
| UW-22-Q3 | Tie skor sama | Attempt paling awal | idem | D-12: attempt paling awal; semua attempt disimpan |
| UW-22-Q4 | Presisi tampilan | 2 desimal dibulatkan ke bawah + status teks | idem | D-12: 2 desimal dibulatkan ke bawah + status lulus/belum lulus eksplisit |
| CU-2-Q1 | Keempat komponen di setiap modul | Opsi A | [CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md](CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md) §7 | D-13: keempat komponen di semua 16 modul (30/40/20/10) |
| CU-2-Q2 | Capstone vs modul 16 | Tidak ada rekomendasi; keputusan produk | idem | D-13: capstone = mini-project modul 16 dengan rubrik capstone khusus |
| CU-2-Q3 | Beberapa aktivitas dalam satu komponen | Poin dijumlah (sejalan NP-4) | idem | D-13: jumlahkan poin diperoleh dan poin maksimum |
| UO-1-Q1 | Teks kecil `#000000` di atas ungu; `#000000` atau `#1C1B1F` di atas biru, hijau, kuning, merah muda (hanya pasangan ≥ 4,5:1; `#1C1B1F` di atas ungu 4,03 gagal) | Ya | [ACCESSIBILITY_COLOR_DECISION_SHEET.md](ACCESSIBILITY_COLOR_DECISION_SHEET.md) §8 | D-14 disetujui |
| UO-1-Q2 | Varian turunan untuk teks berwarna kecil | Ya (warna merek tetap) | idem | D-14 disetujui (lima warna merek tetap) |
| UO-1-Q3 | Teks putih pada ungu (4,25) hanya untuk teks besar (≥ 18sp, atau tebal ≥ 14sp); teks tebal < 14sp tetap `#000000` | Ya | idem | D-14 disetujui |
| UO-2-Q1 | Dark mode | DM-1 (terang saja, Force Dark nonaktif) untuk V1 | idem | D-15: DM-1; Force Dark otomatis dinonaktifkan |
| UO-2-Q2 | Material 3 tanpa dynamic color | Ya | idem | D-15: dynamic color dinonaktifkan |

## Keputusan owner D-12–D-15 (2026-11-24)

Pernyataan owner: "Saya menyetujui seluruh rekomendasi D-12–D-15. ...
Implementasi tetap dilarang." Status: **OWNER APPROVED**, berlaku efektif
setelah PR pencatatan di-merge. Verifikasi pada implementasi tetap
**NOT VERIFIED** (UW-56).

### D-12 — Presisi angka (UW-22)

| Butir | Keputusan |
|---|---|
| Q1 | NP-4: aritmetika integer rasional eksak dari poin mentah `earned` dan `max` |
| Q2 | Maksimum 10.000 poin per komponen per attempt |
| Q3 | Skor terbaik sama → pilih attempt paling awal; semua attempt disimpan |
| Q4 | Tampilan 2 desimal dibulatkan ke bawah, selalu disertai status lulus/belum lulus eksplisit |
| Wajib dipertahankan | Setiap komponen ≥ 75 dan nilai modul tertimbang ≥ 80 dengan perbandingan eksak; tanpa pembulatan sebelum keputusan akademik; aritmetika *checked* untuk mencegah overflow; pembulatan tampilan tidak pernah memengaruhi hasil akademik |
| Masih OPEN | Cara nilai parsial penjelasan konsep (OP-4); bobot test case lab (CU-6); alokasi poin per aktivitas; pilihan teknis aritmetika *checked* (mis. `multiplyExact` atau `BigInteger`) saat implementasi |

### D-13 — Struktur komponen per modul (CU-2)

| Butir | Keputusan |
|---|---|
| Q1 | Semua 16 modul memiliki keempat komponen: Theory 30%, Laboratory 40%, Mini-project 20%, Concept explanation 10% |
| Q2 | Capstone adalah mini-project modul 16, dengan rubrik capstone khusus; capstone **tidak** menjadi proyek wajib tambahan di luar 128 jam |
| Q3 | Komponen dengan beberapa aktivitas bernilai: jumlahkan poin diperoleh dan poin maksimum |
| Wajib dipertahankan | 16 modul, 128 jam; unlock linear; remedial tanpa batas; skor terbaik per komponen; riwayat attempt lengkap; XP sekali per aktivitas unik yang memenuhi syarat |
| Masih OPEN | Rubrik rinci (termasuk rubrik capstone), alokasi poin per aktivitas, alokasi jam per komponen |

### D-14 — Aksesibilitas dan kontras (UO-1)

| Butir | Keputusan |
|---|---|
| Q1 | Pasangan teks–latar harus memenuhi ambang kontras; teks kecil di atas ungu `#7565F5` memakai `#000000`; di atas empat warna merek lain boleh `#000000` atau `#1C1B1F` hanya bila ambang terpenuhi |
| Q2 | Warna turunan yang aksesibel diizinkan tanpa mengganti lima warna merek terkunci |
| Q3 | Teks putih di atas ungu hanya untuk teks besar yang memenuhi syarat (≥ 18sp, atau tebal ≥ 14sp), sesuai persyaratan kontras |
| Wajib dipertahankan | Status akademik tidak pernah disampaikan hanya lewat warna; pemeriksaan ambang memakai rasio kontras tanpa pembulatan; palet Colorful Academy asli tetap |

### D-15 — Strategi tema (UO-2)

| Butir | Keputusan |
|---|---|
| Q1 | DM-1: tema terang saja untuk V1; Force Dark otomatis dinonaktifkan |
| Q2 | Material 3 dynamic color dinonaktifkan untuk menjaga identitas merek |
| Catatan | Dark mode dapat dipertimbangkan kelak lewat keputusan terpisah. Perilaku nyata di perangkat **NOT VERIFIED** |

## Antrean keputusan berikutnya — disiapkan 2026-11-24

*Historis:* semula AWAITING OWNER; seluruh butir dijawab owner pada
2026-11-24 (D-16–D-22). Kolom rekomendasi dipertahankan sebagai catatan.

| ID | Pertanyaan | Rekomendasi teknis | Lembar keputusan | Keputusan final |
|---|---|---|---|---|
| OD-1-Q1 | AEAD | AES-256-GCM, nonce acak 96-bit, tag 128-bit, header sebagai AAD | [OD1_BACKUP_CRYPTO_DECISION_SHEET.md](OD1_BACKUP_CRYPTO_DECISION_SHEET.md) §9 | D-16 |
| OD-1-Q2 | KDF | Argon2id (Bouncy Castle, bersyarat review/uji); cadangan PBKDF2-HMAC-SHA256 ≥ 600.000 iterasi | idem | D-16 (Argon2id bersyarat; PBKDF2 ≥ 600.000 cadangan) |
| OD-1-Q3 | Parameter KDF | Minimum OWASP sebagai batas minimum; batas maksimum difinalkan dari pengukuran sebelum restore produksi diaktifkan (KV-2, KV-3) | idem | D-16 |
| OD-1-Q4 | Envelope | Struktur §5 dengan header sebagai AAD | idem | D-16 (detail serialisasi OPEN) |
| OD-1-Q5 | Penanganan kasus dan validasi | H-1–H-7, KV-1–KV-8 (validasi header sebelum KDF; tanpa downgrade diam-diam; tanpa retry KDF lain; tanpa plaintext sebelum autentikasi) | idem | D-16 |
| OD-1-Q6 | KDF cadangan | Hanya untuk ekspor baru di bawah kebijakan yang disetujui owner (KV-6); backup lama memakai KDF yang dinyatakan di header (KV-5) | idem | D-16 |
| OD-2-Q1 | Model ancaman | Terima §5 dengan risiko residual eksplisit | [OD2_BACKUP_INTEGRITY_DECISION_SHEET.md](OD2_BACKUP_INTEGRITY_DECISION_SHEET.md) §7 | D-17: I-1, risiko residual diterima |
| OD-2-Q2 | Penanda asal-usul + log restore (informatif, tidak tahan manipulasi) | Ya | idem | D-17 (informatif, tidak tahan manipulasi) |
| OD-2-Q3 | Tanda tangan terikat perangkat | Tidak untuk V1 | idem | D-17: I-2 tidak dipakai di V1 |
| OD-2-Q4 | Rantai hash riwayat | Opsional, hanya pencegah kasual | idem | D-17: I-3 tidak dipakai di V1 |
| OD-2-Q5 | Pernyataan "catatan belajar mandiri" | Ya | idem | D-17 |
| UW-43-Q1 | Lokasi file Batch 01 | Opsi B (tetap di root + erratum TD:5) | [UW43_PATH_CONSISTENCY_DECISION_SHEET.md](UW43_PATH_CONSISTENCY_DECISION_SHEET.md) §4 | D-18: Opsi B |
| UW-11-Q1 | Perlukah skor numerik tingkat program? (D-04 melarang rata-rata baru; bila tidak perlu, agregasi program ditutup sebagai "tidak ada") | Tidak perlu; penyelesaian program = 16 modul lulus + capstone | [BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) §15 | D-19: tidak ada skor numerik tingkat program |
| PL-Q1 | Konfirmasi klasifikasi register (audit §15.3): butir verifikasi teknis tidak menjadi syarat PLANNING CLEAR, tetapi tetap syarat IMPLEMENTATION VERIFIED; izin eksekusi prototipe (UW-10) dan izin implementasi (UW-02) adalah gerbang owner **setelah** PLANNING CLEAR | Ya | idem §15.3 | D-20 |
| PL-Q2 | Apakah penulisan konten lengkap 16 modul (UW-37) wajib selesai sebelum PLANNING CLEAR, atau cukup format, rubrik, dan contoh per jenis komponen? | Owner memutuskan; Claude tidak merekomendasikan pengurangan syarat | [BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) §15.3 | D-21: kurikulum lengkap wajib sebelum PLANNING CLEAR |
| PL-Q3 | Apakah UW-21 (alternatif bila O-04 gagal), UW-38 (R8/signing/distribusi), dan UW-40 (mekanisme effect UI) boleh ditunda ke milestone terkait dan tidak menjadi syarat PLANNING CLEAR? | Ya, karena bergantung hasil uji atau implementasi | idem | D-22 |

## Keputusan owner D-16–D-22 (2026-11-24)

Pernyataan owner: "Saya menyetujui seluruh rekomendasi D-16–D-22. ...
Implementasi tetap dilarang." Status: **OWNER APPROVED**, berlaku efektif
setelah PR pencatatan di-merge.

| ID | Topik | Keputusan | Tetap OPEN / NOT VERIFIED |
|---|---|---|---|
| D-16 | OD-1 kriptografi backup (UW-15) | Q1: AES-256-GCM, nonce acak 96-bit, tag 128-bit, seluruh header envelope sebagai AAD, salt acak baru (CSPRNG) per ekspor. Q2: KDF utama Argon2id via Bouncy Castle, **bersyarat** review dependensi, kompatibilitas Android, dan verifikasi kinerja; cadangan PBKDF2-HMAC-SHA256 ≥ 600.000 iterasi. Q3: minimum Argon2id 19 MiB, t=2, p=1; parameter final dan batas maksimum ditetapkan lewat pengukuran perangkat yang diizinkan terpisah; **restore produksi tetap nonaktif** sampai batas disetujui dan terverifikasi. Q4: struktur envelope OD1 §5 sebagai baseline format. Q5: H-1–H-7 dan KV-1–KV-8; validasi ketat header tak tepercaya sebelum alokasi sumber daya dan KDF; tanpa downgrade diam-diam; tanpa retry KDF lain setelah autentikasi gagal; tanpa parsing/tampilan/staging/penerapan plaintext sebelum autentikasi berhasil; data aktif dipertahankan bila validasi atau autentikasi gagal. Q6: KDF cadangan hanya untuk ekspor baru di bawah kebijakan yang disetujui; backup lama didekripsi dengan format dan KDF yang dinyatakan dan terautentikasi | Detail serialisasi; parameter final; batas maksimum; implementasi kripto **NOT VERIFIED**; CT-1–CT-12 **NOT VERIFIED** |
| D-17 | OD-2 pemalsuan dan integritas akademik (UW-16) | Q1: I-1 dengan risiko residual terdokumentasi diterima secara eksplisit. Q2: penanda asal-usul restore dan log peristiwa restore yang persisten. Q3: tanpa tanda tangan terikat perangkat (I-2) di V1. Q4: tanpa rantai hash riwayat attempt (I-3) di V1. Q5: rapor akademik adalah catatan belajar mandiri, bukan bukti akademik tersertifikasi. Penanda dan log bersifat informatif, tidak tahan manipulasi; enkripsi berbasis kata sandi tidak mencegah pemalsuan oleh pemilik kata sandi; portabilitas lintas perangkat dipertahankan; D-03 tetap | Retensi dan penyimpanan log restore |
| D-18 | UW-43 konsistensi path | Opsi B: `PLANNING_COMPLETION_BATCH.md` tetap di root; erratum TD:5 dicatat di DECISIONS_LOG; dokumen Batch 02 verbatim tidak diubah; file Batch 01 tidak dipindahkan; tautan relatif dan riwayat dipertahankan | — |
| D-19 | UW-11 agregasi tingkat program | Tidak ada skor numerik tingkat program; tidak ada rata-rata atau ambang kelulusan program baru; program selesai bila 16 modul lulus dan capstone memenuhi rubrik khususnya; capstone tetap mini-project modul 16; aturan tingkat modul tidak berubah | Rubrik capstone (CU-9) |
| D-20 | PL-Q1 klasifikasi | Klasifikasi P/M/G/V audit §15.3 diadopsi, tunduk pada D-21 dan D-22. P = persyaratan perencanaan wajib; M = pekerjaan bergantung milestone yang disetujui; G = gerbang otorisasi owner; V = verifikasi teknis setelah otorisasi. PLANNING CLEAR mensyaratkan semua persyaratan P wajib dan AC perencanaan yang berlaku terpenuhi. UW-02 dan UW-10 adalah gerbang **setelah** PLANNING CLEAR. Verifikasi teknis tetap wajib untuk gerbang implementasi dan rilis. PLANNING CLEAR **tidak** mengizinkan implementasi; izin owner baru wajib sebelum eksekusi prototipe atau implementasi | Tidak ada butir P tambahan yang boleh dipindah ke M atau V tanpa persetujuan |
| D-21 | PL-Q2 kurikulum | Kurikulum lengkap wajib sebelum PLANNING CLEAR; UW-37 tetap wajib di jalur P; seluruh 64 komponen penilaian dicakup; contoh edukatif dan spesifikasi test berbentuk dokumentasi diizinkan; tanpa prototipe, implementasi runtime, source aplikasi, atau otomasi test; tidak ada klaim latihan sudah dijalankan/terverifikasi | Seluruh konten (UW-37) |
| D-22 | PL-Q3 penundaan milestone | UW-21 (alternatif final bila runtime Python gagal), UW-38 (R8, signing, distribusi), UW-40 (mekanisme effect UI) ditunda ke milestone terkait; AC asli dipertahankan; penundaan **bukan** penyelesaian; tidak ada penundaan lain tanpa persetujuan eksplisit | Ketiga butir tetap belum selesai |

## Antrean keputusan — disiapkan 2026-11-24 (setelah D-16–D-22)

*Historis:* semula AWAITING OWNER; seluruh butir dijawab owner pada
2026-11-24 (D-23, D-24, D-25).

| ID | Pertanyaan | Rekomendasi teknis | Lembar keputusan | Keputusan final |
|---|---|---|---|---|
| OP-4-Q1 | Struktur rubrik penjelasan konsep | CE-B (kredit parsial terdefinisi per format) | [OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md](OP4_CONCEPT_EXPLANATION_DECISION_SHEET.md) §7 | D-23: CE-B |
| OP-4-Q2 | Aturan skor per format CE-S1–CE-S5 (adjacency maksimum, `max_soal` eksak) | §3 lembar OP-4 | idem | D-23: CE-S1–CE-S5, CE-S3a–S3c |
| OP-4-Q3 | Penalti dan self-assessment | Tolak CE-C; CE-D hanya latihan tanpa skor | idem | D-23: CE-C ditolak; CE-D refleksi tanpa skor |
| OP-4-Q4 | Konsep wajib, jawaban alternatif, review manusia | CE-K1–CE-K4 | idem | D-23: CE-K1–CE-K4 |
| OP-4-Q5 | Validasi jawaban (kosong, ID asing/ganda, bentuk salah, sebagian) | CE-V1–CE-V6 | idem | D-23: CE-V1–CE-V6 (+ CE-V7) |
| CU-6-Q1 | Bobot test lab | LW-B (bobot bilangan bulat yang direview) | [CU6_LAB_SCORING_DECISION_SHEET.md](CU6_LAB_SCORING_DECISION_SHEET.md) §12 | D-24: LW-B |
| CU-6-Q2 | Test wajib/bonus | LR-A (tanpa gerbang, tanpa bonus) | idem | D-24: LR-A |
| CU-6-Q3 | Kode hasil test; penyebab pelajar vs infrastruktur; output > 64 KB selalu gagal | §5–§6 lembar CU-6 | idem | D-24: §5–§6 |
| CU-6-Q4 | Lingkup remedial lab, penyelesaian attempt, XP | RA-1 + LA-1–LA-4 | idem | D-24: RA-1, LA-1–LA-4 |
| CU-6-Q5 | Anggaran eksekusi (D-10 tetap) | TB-B, cadangan TB-A; EB-1–EB-5 | idem | D-24: TB-B, TB-A cadangan bersyarat, EB-1–EB-5 |
| CU-6-Q6 | Eksekusi tidak lengkap dan pelestarian poin | IE-1–IE-5 | idem | D-24: IE-1–IE-5 |
| RM-Q1 | UW-15 ke jalur V; OD-11–OD-14 di UW-33; CU2-O3/CU2-O4 dilacak di UW-36; izin pengukuran kripto sebagai prasyarat UW-15 | Setujui | [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §11 | D-25: (a)–(d) disetujui |

## Keputusan owner D-23–D-25 (2026-11-24)

Pernyataan owner: "Saya menyetujui rekomendasi D-23, D-24, D-25. Buat satu
prompt merge PR #23, pencatatan keputusan yang disetujui, dan lanjutkan batch
planning kurikulum. Implementasi tetap dilarang." Status: **OWNER APPROVED**,
berlaku efektif setelah PR pencatatan di-merge.

| ID | Topik | Keputusan | Tetap OPEN / NOT VERIFIED |
|---|---|---|---|
| D-23 | OP-4 penilaian penjelasan konsep (UW-26) | CE-B; CE-S1–CE-S5 (pilihan tunggal penuh/nol; pilihan ganda `max(0, c − w)`; pengurutan = adjacency maksimum terhadap satu urutan diterima lengkap, pasangan dari urutan berbeda tidak digabung; pencocokan 1 poin per pasangan; menemukan kesalahan penuh/setengah/nol); CE-S3a–S3c; poin integer eksak; CE-C ditolak; CE-D hanya refleksi tanpa skor; CE-K1–CE-K4; CE-V1–CE-V6; jawaban salah bentuk dibedakan dari kegagalan infrastruktur/konten rusak, tanpa penalti diam-diam (CE-V7); tanpa AI grading, tutor AI, atau penilaian server wajib | UW-26 tetap OPEN sampai bank soal 16 modul ada |
| D-24 | CU-6 penilaian lab (bagian UW-36) | LW-B; LR-A; RA-1; TB-B dengan TB-A cadangan bersyarat; EB-1–EB-5, LA-1–LA-4, IE-1–IE-5 yang berlaku. Dipertahankan: 3.000 ms kode pelajar per latihan Python; start interpreter diukur terpisah; ambang D-10; output > 64 KB tidak dapat `PASS` lewat awalan terpotong; poin test lulus dipertahankan saat test lain gagal karena kode pelajar; kegagalan infrastruktur membatalkan evaluasi aktivitas tanpa penalti; evaluasi ulang tanpa attempt baru; tanpa pewarisan poin antar attempt; skor terbaik attempt selesai per komponen; riwayat lengkap; tanpa XP ganda | Klarifikasi LX-1–LX-9 (CU-6-Q7–Q12); batas sumber daya final; runtime **NOT VERIFIED**; UW-36 tetap BLOCKED |
| D-25 | RM-Q1 klasifikasi roadmap | (a) UW-15 di jalur V, AC asli tetap; (b) OD-11–OD-14 dilacak di UW-33 bersama OD-5–OD-9; (c) CU2-O3 dan CU2-O4 dilacak di UW-36; (d) pengukuran kripto butuh izin owner terpisah, dicatat sebagai prasyarat UW-15. Tidak ada persyaratan keamanan yang dihapus | Tidak ada pengukuran, benchmark, prototipe, atau implementasi yang diizinkan |

## Matriks keputusan owner — disiapkan 2026-11-24 (setelah D-23–D-25; direvisi review PR #24)

*Historis:* semula AWAITING OWNER; seluruh 45 pertanyaan dijawab owner pada
2026-11-24 (D-26–D-35, kolom "Keputusan final"). ID unik (diperiksa otomatis). Ketegangan terkait:
[CROSS_SPEC_CONSISTENCY_REVIEW.md](CROSS_SPEC_CONSISTENCY_REVIEW.md) §2.
Gelombang 1 (prasyarat CB-0): grup 1, 2 (OP-7, OP-10), 3 (OP-8-Q1–Q3), 4
(CU-3, CU-5, CU2-O5, CU2-O3), 6 (CU2-O4). Gelombang 2: sisanya.

### Grup 1 Ujian teori (UW-27)

| ID | Topik | Rekomendasi | Trade-off utama | Lembar | Keputusan final |
|---|---|---|---|---|---|
| OP-5-Q1 | Jumlah soal | TQ-B: 20 (W1–W15), 10 (W16), ≥ 2 per kompetensi | Cakupan terjamin vs beban blueprint per modul | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.1 | D-26: disetujui (TQ-B: 20 (W1–W15), 10 (W16), ≥ 2 per kompetensi) |
| OP-5-Q2 | Format soal | TF-1–TF-5, tanpa esai | Objektif offline vs tidak menilai tulisan bebas | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.2 | D-26: disetujui (TF-1–TF-5, tanpa esai) |
| OP-5-Q3 | Poin dan kesulitan | TP-B 2/3/4 semua-atau-tidak; 40/40/20 | Sederhana vs berbeda dari kredit parsial D-23 (TP-C) | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.3 | D-26: disetujui (TP-B 2/3/4 semua-atau-tidak; 40/40/20) |
| OP-5-Q4 | Rumus durasi | A.4; standar 33 menit; min. 10; > 45 ditolak | Memenuhi M-07 vs perlu hitung per blueprint | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.4 | D-26: disetujui (A.4; standar 33 menit; min. 10; > 45 ditolak) |
| OP-5-Q5 | Tenggat, kosong, otomatis, interupsi, varian, tenggat remedial | EX-1–EX-13 termasuk ASM:T7/D-04/D-05 | Mengikuti M-07 vs tanpa perpanjangan otomatis | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.5–A.6 | D-26: disetujui (EX-1–EX-13 termasuk ASM:T7/D-04/D-05) |
| OP-5-Q6 | Aksesibilitas waktu | TA-B ×1,5 (maks. 68 menit), TA-1–TA-4 | Inklusif vs pengecualian dari batas standar | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.5a | D-26: disetujui (TA-B ×1,5 (maks. 68 menit), TA-1–TA-4) |
| OP-5-Q7 | Umpan balik | FB-A pembahasan setelah dinilai | Nilai belajar vs varian dapat dihafal | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.6 | D-26: disetujui (FB-A pembahasan setelah dinilai) |
| OP-5-Q8 | Persistensi di sekitar tenggat | DL-1–DL-9 + SF-A | Riwayat utuh vs attempt bermasalah tetap dihitung (SF-B alternatif) | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §A.5b | D-26: disetujui (DL-1–DL-9 + SF-A) |

### Grup 2 Alur attempt (UW-29, UW-31, UW-32)

| ID | Topik | Rekomendasi | Trade-off utama | Lembar | Keputusan final |
|---|---|---|---|---|---|
| OP-7-Q1 | Pengumpulan dan interupsi | SB-A + SB-1–SB-12 | Umpan balik bertahap vs dua tingkat penyelesaian | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §B | D-27: disetujui (SB-A + SB-1–SB-12) |
| OP-9-Q1 | Unlock rinci | UL-1–UL-10, PV-A, RV-A | Prasyarat terjaga vs tanpa pratinjau jauh | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §C | D-27: disetujui (UL-1–UL-10, PV-A, RV-A) |
| OP-10-Q1 | Komponen yang boleh diulang saat `NOT_PASSED` | RE-A semua komponen | Satu-satunya opsi tanpa kebuntuan (ASM:B-02) | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §D.1 | D-27: disetujui (RE-A semua komponen) |
| OP-10-Q2 | Perbaikan setelah lulus | PI-A | Penguasaan vs rapor dapat naik | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §D.1 | D-27: disetujui (PI-A) |
| OP-11-Q1 | Autosave | AS-B (lab/proyek/concept) + DL untuk ujian | Beban tulis wajar vs jendela kecil saat crash | [AF](ASSESSMENT_FLOW_DECISION_SHEETS.md) §D.2 | D-27: disetujui (AS-B (lab/proyek/concept) + DL untuk ujian) |

### Grup 3 XP dan restore (UW-30, UW-33)

| ID | Topik | Rekomendasi | Trade-off utama | Lembar | Keputusan final |
|---|---|---|---|---|---|
| OP-8-Q1 | Identitas XP | XI-1–XI-9 (komponen sebagai identitas dinilai) | Sederhana vs aktivitas lab tanpa XP sendiri | [XP](XP_PROGRESS_DECISION_SHEET.md) §3 | D-28: disetujui (XI-1–XI-9 (komponen sebagai identitas dinilai)) |
| OP-8-Q2 | Kelayakan | XE-B sekali saat pertama ≥ 75 (+ tafsiran XE-2) | Sesuai X-01 vs usaha tanpa penguasaan tidak ber-XP | [XP](XP_PROGRESS_DECISION_SHEET.md) §4 | D-28: disetujui (XE-B sekali saat pertama ≥ 75 (+ tafsiran XE-2)) |
| OP-8-Q3 | Aktivitas tidak dinilai | UG-A (XP sekali) | Motivasi membaca vs XP non-akademik dari aktivitas ringan | [XP](XP_PROGRESS_DECISION_SHEET.md) §4 | D-28: disetujui (UG-A (XP sekali)) |
| OP-8-Q4 | Jumlah XP dan level | §5, `L(n) = 50·n·(n−1)` | Level 10 di akhir program vs angka dapat diubah kelak | [XP](XP_PROGRESS_DECISION_SHEET.md) §5–§6 | D-28: disetujui (§5, `L(n) = 50·n·(n−1)`) |
| OP-8-Q5 | Streak | ST-C mingguan, SK-1–SK-6 | Selaras jadwal shift vs umpan balik lebih jarang | [XP](XP_PROGRESS_DECISION_SHEET.md) §9 | D-28: disetujui (ST-C mingguan, SK-1–SK-6) |
| OP-8-Q6 | Achievement, mastery, tampilan restore M-1 | XA-1–XA-3, §8.1 | Transparan vs XP dapat turun karena restore pilihan pengguna | [XP](XP_PROGRESS_DECISION_SHEET.md) §8, §10 | D-28: disetujui (XA-1–XA-3, §8.1) |
| OP-8-Q7 | Milestone modul dan capstone | Identitas terpisah 50 / 100 | Merayakan kelulusan vs tambahan identitas | [XP](XP_PROGRESS_DECISION_SHEET.md) §3 | D-28: disetujui (Identitas terpisah 50 / 100) |
| OD-15-Q1 | Validasi ledger saat restore | XV-1–XV-6 + RX-A (tolak bila ada temuan) | Data aman vs backup lama yang rusak tidak dapat dipakai (RX-B) | [XP](XP_PROGRESS_DECISION_SHEET.md) §8.2 | D-29: disetujui (XV-1–XV-6 + RX-A (tolak bila ada temuan)) |

### Grup 4 Konten dan struktur (UW-36)

| ID | Topik | Rekomendasi | Trade-off utama | Lembar | Keputusan final |
|---|---|---|---|---|---|
| CU-3-Q1 | Format konten | CF-A Markdown terbatas + YAML | Mudah direview vs perlu konversi kelak | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §A | D-30: disetujui (CF-A Markdown terbatas + YAML) |
| CU-3-Q2 | Folder dan pembaruan | A.3 + UP-A (lewat APK) | Sederhana dan aman vs pembaruan lambat | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §A | D-30: disetujui (A.3 + UP-A (lewat APK)) |
| CU-5-Q1 | Jumlah varian | VR-B (2/2/2) + MPV-A | Beban realistis vs bank lebih kecil dari VR-C | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §B | D-30: disetujui (VR-B (2/2/2) + MPV-A) |
| CU-5-Q2 | Kesetaraan dan pemilihan | VA-1–VA-6 | Deterministik vs pemakaian ulang bergiliran | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §B | D-30: disetujui (VA-1–VA-6) |
| CU2-O5-Q1 | Asumsi struktur | 6 soal concept + 3 aktivitas lab per modul | Dasar beban dan durasi vs fleksibilitas konten | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §B | D-30: disetujui (6 soal concept + 3 aktivitas lab per modul) |
| CU2-O3-Q1 | Alokasi 128 jam | Tabel §D (M/U/L/P/C/R) | Fase-sensitif vs angka per modul tetap | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §D | D-32: disetujui (Tabel §D (M/U/L/P/C/R)) |
| CU-11-Q1 | Pembagian W9/W10 | PB-A revisi | Proyek W9 bermakna vs konversi diajarkan dua tahap | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §E | D-32: disetujui (PB-A revisi) |

### Grup 5 Lab SQL/HTML/Git (UW-36)

| ID | Topik | Rekomendasi | Trade-off utama | Lembar | Keputusan final |
|---|---|---|---|---|---|
| CU-7-Q1 | SQL | SQ-1–SQ-9 (urutan penuh bila wajib; real lewat `ROUND`) | Deterministik vs SQL dasar saja | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §C.1 | D-31: disetujui (SQ-1–SQ-9 (urutan penuh bila wajib; real lewat `ROUND`)) |
| CU-7-Q2 | HTML/CSS | HV-A struktur; pratinjau tidak dinilai | Deterministik vs tidak menilai tampilan | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §C.2 | D-31: disetujui (HV-A struktur; pratinjau tidak dinilai) |
| CU-7-Q3 | Git | GS-A simulasi keadaan; GitHub opsional | Offline vs bukan Git asli | [CCD](CURRICULUM_CONTENT_DECISION_SHEETS.md) §C.3 | D-31: disetujui (GS-A simulasi keadaan; GitHub opsional) |

### Grup 6 Rubrik (UW-36)

| ID | Topik | Rekomendasi | Trade-off utama | Lembar | Keputusan final |
|---|---|---|---|---|---|
| CU2-O4-Q1 | Rubrik mini-project | MR-A 60/20/10/10 + MR-1–MR-8 + A.2a | Konsisten vs bobot sama untuk proyek berbeda | [RB](PROJECT_RUBRIC_DECISION_SHEETS.md) §A | D-33: disetujui (MR-A 60/20/10/10 + MR-1–MR-8 + A.2a) |
| CU2-O4-Q2 | Brief W1–W15 | A.3 sebagai arah | Arah produksi jelas vs dapat berubah di CB | [RB](PROJECT_RUBRIC_DECISION_SHEETS.md) §A.3 | D-33: disetujui (A.3 sebagai arah) |
| CU-9-Q1 | Tema, deliverable, skema SQL | B.1 + B.1a | Integratif vs satu tema untuk semua pelajar | [RB](PROJECT_RUBRIC_DECISION_SHEETS.md) §B.1 | D-33: disetujui (B.1 + B.1a) |
| CU-9-Q2 | Rubrik dan kriteria wajib | B.2 + MC-1–MC-4 | Inti program terjamin vs gerbang tambahan | [RB](PROJECT_RUBRIC_DECISION_SHEETS.md) §B.2–B.3 | D-33: disetujui (B.2 + MC-1–MC-4) |
| CU-9-Q3 | Gerbang capstone | CG-B | Adil terhadap riwayat attempt vs dua aturan berbeda | [RB](PROJECT_RUBRIC_DECISION_SHEETS.md) §B.4 | D-33: disetujui (CG-B) |
| CU-9-Q4 | Capstone setelah W16 lulus | CP-6 (selalu tersedia sampai gerbang terpenuhi) | Tidak buntu vs attempt setelah lulus | [RB](PROJECT_RUBRIC_DECISION_SHEETS.md) §B.5 | D-33: disetujui (CP-6 (selalu tersedia sampai gerbang terpenuhi)) |

### Grup 7 Risiko dan klarifikasi lab (UW-25, D-24 LX)

| ID | Topik | Rekomendasi | Trade-off utama | Lembar | Keputusan final |
|---|---|---|---|---|---|
| CU-10-Q1 | Risiko ekstraksi kunci | Terima (selaras D-17) | Jujur vs tidak ada perlindungan teknis | [CU10](CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) | D-34: disetujui (Terima (selaras D-17)) |
| CU-10-Q2 | Mitigasi V1 | AK-A kebersihan UI | Tanpa rasa aman palsu vs kunci tetap dapat diekstrak | [CU10](CU10_ANSWER_KEY_RISK_DECISION_SHEET.md) | D-34: disetujui (AK-A kebersihan UI) |
| CU-6-Q7 | Output per eksekusi (LX-1) | Ya | Sesuai D-10 vs TB-A berbagi 64 KB | [CU6](CU6_LAB_SCORING_DECISION_SHEET.md) §14 | D-35: disetujui (Ya) |
| CU-6-Q8 | Kebijakan batas agregat (LX-2) | Ya; nilai OPEN | Aman vs nilai menunggu pengukuran | [CU6](CU6_LAB_SCORING_DECISION_SHEET.md) §14 | D-35: disetujui (Ya; nilai OPEN) |
| CU-6-Q9 | Waktu dan proses (LX-3, LX-4) | Ya | Adil bagi pelajar vs evaluasi lebih lama | [CU6](CU6_LAB_SCORING_DECISION_SHEET.md) §14 | D-35: disetujui (Ya) |
| CU-6-Q10 | Urutan dan isolasi test (LX-5, LX-6) | Ya | Deterministik vs konten wajib bebas state | [CU6](CU6_LAB_SCORING_DECISION_SHEET.md) §14 | D-35: disetujui (Ya) |
| CU-6-Q11 | Aktivasi TB-A (LX-7) | Ya | Terkontrol vs butuh review konten | [CU6](CU6_LAB_SCORING_DECISION_SHEET.md) §14 | D-35: disetujui (Ya) |
| CU-6-Q12 | Tanpa klaim kesetaraan; pencatatan (LX-8, LX-9) | Ya | Jujur vs hasil lintas mode tidak sebanding sempurna | [CU6](CU6_LAB_SCORING_DECISION_SHEET.md) §14 | D-35: disetujui (Ya) |

Jumlah pertanyaan: **45**.

## Keputusan owner D-26–D-35 (2026-11-24)

Pernyataan owner: "Saya menyetujui rekomendasi D-26, D-27, D-28, D-29, D-30,
D-31, D-32, D-33, D-34, D-35. Buat satu prompt merge PR #24, pencatatan
keputusan yang disetujui, finalisasi CB-0 dan lanjutkan planning kurikulum
modul W1. Implementasi tetap dilarang." Status: **OWNER APPROVED**, berlaku
efektif setelah PR pencatatan di-merge. Rincian opsi dan AC terdampak:
[DECISIONS_LOG.md](DECISIONS_LOG.md) dan bagian keputusan tiap lembar.

| ID | Pertanyaan | Ringkasan | Tetap OPEN / NOT VERIFIED |
|---|---|---|---|
| D-26 | OP-5-Q1–Q8 | Ujian teori: TQ-B, TF-1–TF-5, TP-B, 40/40/20, rumus A.4, EX-1–EX-13, TA-B + TA-1–TA-4, FB-A, DL-1–DL-9 + SF-A | OP-6 (UW-28) |
| D-27 | OP-7-Q1, OP-9-Q1, OP-10-Q1–Q2, OP-11-Q1 | SB-A, UL-1–UL-10 + PV-A + RV-A, RE-A, PI-A, AS-B | — |
| D-28 | OP-8-Q1–Q7 | XI, XE-B, UG-A, jumlah XP, level, ST-C, XA, XL, milestone | — |
| D-29 | OD-15-Q1 | XV-1–XV-6 + RX-A | OD-15-Q2; sisa UW-33 |
| D-30 | CU-3-Q1–Q2, CU-5-Q1–Q2, CU2-O5-Q1 | CF-A + UP-A, VR-B + MPV-A + VA-1–VA-6, 6 concept + 3 lab per modul | — |
| D-31 | CU-7-Q1–Q3 | SQL/HTML/Git | Mekanisme NOT VERIFIED |
| D-32 | CU2-O3-Q1, CU-11-Q1 | HA-A, PB-A revisi | — |
| D-33 | CU2-O4-Q1–Q2, CU-9-Q1–Q4 | MR-A, capstone, CG-B | — |
| D-34 | CU-10-Q1–Q2 | AK-A | — |
| D-35 | CU-6-Q7–Q12 | LX-1–LX-9 | Nilai batas agregat; CU-6-Q13 |

## Antrean keputusan — disiapkan 2026-11-24 (setelah D-26–D-35)

CU-6-Q13 dan OD-15-Q2 dijawab owner (D-36, D-37). RM-Q2 dijawab (D-38); W01-ACC diterima owner. Antrean ini kosong.

| ID | Pertanyaan | Rekomendasi | Trade-off | Lembar | Keputusan final |
|---|---|---|---|---|---|
| CU-6-Q13 | Umpan balik test tersembunyi lab kode setelah evaluasi | HF-A (kode hasil + deskripsi kasus) | Umpan balik bermakna vs penyusun menulis deskripsi | [CU6_LAB_SCORING_DECISION_SHEET.md](CU6_LAB_SCORING_DECISION_SHEET.md) §16 | D-36: HF-A disetujui |
| OD-15-Q2 | Perluasan validasi kelayakan award XV-7–XV-14 dengan RX-A | Ya | Ledger terbukti sah vs butuh catatan peristiwa pelajaran/latihan | [XP_PROGRESS_DECISION_SHEET.md](XP_PROGRESS_DECISION_SHEET.md) §14.1 | D-37: XV-7–XV-14 + RX-A disetujui |
| W01-ACC | Penerimaan konten modul W1 sebagai modul acuan | Review PR lalu terima bila tidak ada temuan | Standar untuk W2–W16 vs revisi lebih awal | [curriculum/mod-w01/review.md](../curriculum/mod-w01/review.md) | W01-ACC: diterima sebagai modul acuan, dengan batas review independen |
| RM-Q2 | Nilai angka batas agregat lab (LX-2) adalah hasil pengukuran yang diizinkan: catat sebagai keluaran verifikasi di UW-12 (jalur V), sehingga UW-36 (kebijakan CU) dapat dinilai lengkap? | Ya — kebijakan LX-2 sudah disetujui (D-35); hanya angkanya butuh pengukuran | Butir P tidak bergantung pada pengukuran vs pemindahan butir butuh persetujuan (D-20) | [PLANNING_ROADMAP.md](PLANNING_ROADMAP.md) §11 | D-38: Ya |

## Keputusan owner D-36–D-37 (2026-11-24)

| ID | Pertanyaan | Keputusan | Tetap OPEN / NOT VERIFIED |
|---|---|---|---|
| D-36 | CU-6-Q13 | HF-A: kode hasil + deskripsi kasus; tanpa input mentah, output diharapkan, atau output pelajar untuk test tersembunyi; `case_description` wajib di templat | Nilai batas agregat LX-2; implementasi |
| D-37 | OD-15-Q2 | XV-7–XV-14 dengan RX-A, persis seperti lembar XP §14.1 | OD-5–OD-9, OD-11–OD-14 (UW-33); implementasi |

## Keputusan owner D-38 dan W01-ACC (2026-11-24)

| ID | Pertanyaan | Keputusan | Tetap OPEN / NOT VERIFIED |
|---|---|---|---|
| D-38 | RM-Q2 | Nilai angka batas agregat eksekusi lab (LX-2) = keluaran verifikasi UW-12 (jalur V) | Pengukuran (UW-12; D-10 NOT AUTHORIZED) |
| W01-ACC | Penerimaan W1 | Diterima sebagai modul kurikulum acuan | Batas review independen (dinyatakan owner): F-22 dan F-23 menerima review akhir terarah; pencatatan D-36/D-37 diperiksa; enumerasi independen mengonfirmasi 3.840 kombinasi dan 46 build valid. Tidak setiap baris CSV terbaru, setiap butir penilaian yang berubah, atau setiap penerapan kontrak visibilitas diaudit ulang secara independen. |

## Penerimaan owner W02-ACC, W03-ACC, W04-ACC (2026-11-24)

| ID | Pertanyaan | Keputusan | Batas |
|---|---|---|---|
| W02-ACC | Penerimaan W2 | Diterima (PR #27 di-merge, `846051f`) | Batas review independen (dinyatakan owner): delta review terarah PASS — F-49–F-59 dan F-71–F-72 lolos review terarah; integritas register F-28–F-72 diverifikasi; 16 simulasi normalisasi independen lolos. Regresi historis penuh, semua skrip validasi sementara, uji dengan pelajar, dan verifikasi runtime Android **tidak** diulang secara independen. |
| W03-ACC | Penerimaan W3 | Diterima (PR #27 di-merge, `846051f`) | Batas review independen (dinyatakan owner): delta review terarah PASS — F-49–F-59 dan F-71–F-72 lolos review terarah; integritas register F-28–F-72 diverifikasi; 16 simulasi normalisasi independen lolos. Regresi historis penuh, semua skrip validasi sementara, uji dengan pelajar, dan verifikasi runtime Android **tidak** diulang secara independen. |
| W04-ACC | Penerimaan W4 | Diterima (PR #27 di-merge, `846051f`) | Batas review independen (dinyatakan owner): delta review terarah PASS — F-49–F-59 dan F-71–F-72 lolos review terarah; integritas register F-28–F-72 diverifikasi; 16 simulasi normalisasi independen lolos. Regresi historis penuh, semua skrip validasi sementara, uji dengan pelajar, dan verifikasi runtime Android **tidak** diulang secara independen. |
