# IT ZERO → HERO — Owner Decision Checklist (P0)

Status: D-01 **APPROVED** · D-02–D-09 **OWNER APPROVED** (tunduk pada
verifikasi yang tersisa) · D-10 **PLANNING APPROVED; EXECUTION NOT
AUTHORIZED** · D-11 **DEFERRED; IMPLEMENTATION NOT AUTHORIZED** · tidak
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

Semua butir di bawah **AWAITING OWNER**. Rekomendasi hanya saran.

| ID | Pertanyaan | Rekomendasi teknis | Lembar keputusan | Keputusan final |
|---|---|---|---|---|
| UW-22-Q1 | Representasi skor | NP-4 (integer rasional dari poin mentah) | [NUMERIC_PRECISION_DECISION_SHEET.md](NUMERIC_PRECISION_DECISION_SHEET.md) §8 | |
| UW-22-Q2 | Batas poin maksimum per komponen per attempt | `max ≤ 10.000` | idem | |
| UW-22-Q3 | Tie skor sama | Attempt paling awal | idem | |
| UW-22-Q4 | Presisi tampilan | 2 desimal dibulatkan ke bawah + status teks | idem | |
| CU-2-Q1 | Keempat komponen di setiap modul | Opsi A | [CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md](CU2_ASSESSMENT_STRUCTURE_DECISION_SHEET.md) §7 | |
| CU-2-Q2 | Capstone vs modul 16 | Tidak ada rekomendasi; keputusan produk | idem | |
| CU-2-Q3 | Beberapa aktivitas dalam satu komponen | Poin dijumlah (sejalan NP-4) | idem | |
| UO-1-Q1 | Teks gelap di atas isian warna merek | Ya | [ACCESSIBILITY_COLOR_DECISION_SHEET.md](ACCESSIBILITY_COLOR_DECISION_SHEET.md) §8 | |
| UO-1-Q2 | Varian turunan untuk teks berwarna kecil | Ya (warna merek tetap) | idem | |
| UO-1-Q3 | Teks putih pada ungu hanya untuk teks besar/tebal | Ya | idem | |
| UO-2-Q1 | Dark mode | DM-1 (terang saja, Force Dark nonaktif) untuk V1 | idem | |
| UO-2-Q2 | Material 3 tanpa dynamic color | Ya | idem | |

