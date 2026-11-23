# IT ZERO → HERO — Owner Decision Checklist (P0)

Status: D-01 **APPROVED BY OWNER** (2026-11-23) · D-02–D-11 **AWAITING
OWNER** · tidak ada keputusan yang diisi atas nama owner · tidak ada izin
implementasi atau prototipe.
Tanggal: **2026-11-23**. Basis awal: `main` = `5931ece` (merge PR #16);
D-01 dicatat pada basis `4eacaa0` (merge PR #17).

Sumber register: [`BATCH_01_10_UNFINISHED_AUDIT.md`](BATCH_01_10_UNFINISHED_AUDIT.md)
§3 (UW-01–UW-11). Blueprint terkunci: [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md).

Kolom **Rekomendasi teknis** adalah saran Claude, **bukan** keputusan.
Kolom **Keputusan final** hanya diisi berdasarkan jawaban tertulis owner
(melalui PR yang disetujui). Saat ini hanya D-01 yang terisi.

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
| Status | **AWAITING OWNER** |
| Keputusan final | |

### D-03 — Mode restore backup (UW-09)

| Butir | Isi |
|---|---|
| Sumber | BL:63–64; B01 M-16; [`ENCRYPTED_BACKUP_RESTORE_SPEC.md`](ENCRYPTED_BACKUP_RESTORE_SPEC.md) §6.2, OD-3 |
| Masalah | Blueprint meminta riwayat percobaan dipertahankan saat restore; B01 melarang penggabungan riwayat nilai otomatis. Restore "ganti total" bisa menghilangkan attempt yang tidak ada di file backup |
| Pilihan | M-1 ganti total + snapshot pra-restore disimpan; M-2 tolak restore bila data aktif punya attempt yang tidak ada di backup; M-3 gabung berbasis ID stabil (append saja) |
| Rekomendasi teknis | M-2 sebagai default aman, M-1 sebagai opsi eksplisit dengan peringatan |
| Risiko M-1 | Riwayat hanya ada di snapshot; butuh kebijakan retensi |
| Risiko M-2 | Pengguna bisa terhalang memulihkan data |
| Risiko M-3 | Bertentangan dengan "no automatic merging" kecuali owner mengizinkan |
| Ketergantungan | D-01 (status B01 M-16); memengaruhi D-07 dan model data attempt |
| Status | **AWAITING OWNER** |
| Keputusan final | |

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
| Status | **AWAITING OWNER** |
| Keputusan final | |

### D-07 — Kebijakan Android Auto Backup (UW-06)

| Butir | Isi |
|---|---|
| Sumber | TD:48 (O-07); [`ENCRYPTED_BACKUP_RESTORE_SPEC.md`](ENCRYPTED_BACKUP_RESTORE_SPEC.md) §7, OD-4 |
| Masalah | Auto Backup aktif secara default; database bisa terunggah ke Google Drive; E2E hanya di Android 9+ dengan kunci layar; sebagian perangkat tetap melakukan transfer antarperangkat walau `allowBackup=false` |
| Pilihan | AB-1 `allowBackup=false`; AB-2 izinkan tetapi kecualikan database dan snapshot; AB-3 izinkan semua |
| Rekomendasi teknis | AB-1 atau AB-2, diputuskan bersama D-03 |
| Risiko AB-1 | Pengguna hanya mengandalkan ekspor manual; D2D mungkin tetap terjadi |
| Risiko AB-2 | Aturan ekstraksi harus diuji untuk cloud dan D2D di API ≤ 30 dan ≥ 31 |
| Risiko AB-3 | Data akademik di cloud tanpa enkripsi aplikasi; restore otomatis melewati alur restore aman |
| Ketergantungan | D-03; D-02 (bila DataStore dipakai) |
| Status | **AWAITING OWNER** |
| Keputusan final | |

### D-08 — Izin `INTERNET` (UW-07)

| Butir | Isi |
|---|---|
| Sumber | BL:10, BL:24; O-02; QG OF-3; PY F-09; CAL U-3 |
| Masalah | Video YouTube opsional butuh jaringan; izin `INTERNET` juga membuka akses jaringan bagi kode lab bila isolasi gagal |
| Pilihan | (a) Tanpa `INTERNET`; video dibuka di aplikasi/browser eksternal; (b) dengan `INTERNET` untuk fitur opsional |
| Rekomendasi teknis | (a) untuk V1 |
| Risiko (a) | Tidak ada pembaruan data/konten lewat jaringan (sesuai offline-first) |
| Risiko (b) | Permukaan serangan lebih besar; lab Python bisa mengakses jaringan bila isolasi gagal |
| Ketergantungan | Independen; memengaruhi D-07, D-10, CO-2 |
| Status | **AWAITING OWNER** |
| Keputusan final | |

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
| Status | **AWAITING OWNER** |
| Keputusan final | |

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
| Status | **AWAITING OWNER** |
| Keputusan final | |

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
| Status | **AWAITING OWNER** |
| Keputusan final | |

## C. Izin prototipe

### D-10 — Batas uji dan izin prototipe kelayakan O-04 (UW-10)

| Butir | Isi |
|---|---|
| Sumber | [`PYTHON_OFFLINE_FEASIBILITY_PLAN.md`](PYTHON_OFFLINE_FEASIBILITY_PLAN.md) §6–8; TD:45, TD:60 |
| Masalah | Uji F-01–F-15 butuh (1) batas angka dan (2) izin prototipe terbatas |
| Angka yang dibutuhkan | Ukuran APK maksimum per ABI (F-03); waktu start interpreter maksimum (F-04); batas waktu eksekusi (F-11); batas memori (F-12); batas output (F-13); perangkat uji |
| Pilihan | (a) Izinkan prototipe terbatas setelah batas ditetapkan; (b) tunda; (c) tolak dan putuskan alternatif lab minggu 9–12 (CU-8) |
| Rekomendasi teknis | (a). Prototipe hanya untuk F-01–F-15, terpisah dari aplikasi, tidak menjadi dasar kode produksi tanpa izin implementasi |
| Risiko (a) | Waktu pengerjaan; hasil bisa gagal dan memicu eskalasi |
| Risiko (b) | Lab Python tetap tidak dapat direncanakan |
| Risiko (c) | Mengubah cakupan kurikulum terkunci (BL:19, BL:41) — butuh revisi blueprint |
| Ketergantungan | D-05 (minSdk); D-08 (jaringan); izin ini **tidak** sama dengan D-11 |
| Status | **AWAITING OWNER** |
| Batas yang ditetapkan owner | |
| Keputusan final | |

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
| Status | **AWAITING OWNER** |
| Keputusan final | |

## Ringkasan

| ID | Keputusan | Kelompok | Status | Keputusan final |
|---|---|---|---|---|
| D-01 | Status Batch 01 | Produk | **APPROVED BY OWNER** (2026-11-23) | Setujui M-01–M-19 dengan ketentuan (lihat D-01) |
| D-02 | DataStore | Produk/data | AWAITING OWNER | |
| D-03 | Mode restore | Produk/data | AWAITING OWNER | |
| D-04 | Agregasi skor + basis lulus | Produk | AWAITING OWNER | |
| D-05 | minSdk | Teknis | AWAITING OWNER | |
| D-06 | Toolchain | Teknis | AWAITING OWNER | |
| D-07 | Auto Backup | Produk/data | AWAITING OWNER | |
| D-08 | `INTERNET` | Produk | AWAITING OWNER | |
| D-09 | Stack test | Teknis | AWAITING OWNER | |
| D-10 | Prototipe O-04 | Izin prototipe | AWAITING OWNER | |
| D-11 | Implementasi tahap pertama | Izin implementasi | AWAITING OWNER | |

Cara menjawab: owner mengirim jawaban per ID (mis. "D-03: M-2"). Claude
mencatatnya di PR terpisah, memperbarui DECISIONS_LOG, dan mengubah
status menjadi APPROVED hanya setelah PR itu disetujui.
