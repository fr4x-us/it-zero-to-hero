# IT ZERO → HERO — Log Sumber Keputusan

Status: PERSIAPAN. Implementasi aplikasi belum diizinkan.

Dokumen ini hanya **menunjuk** ke sumber keputusan per batch. Isi keputusan
tetap berada di dokumen sumbernya. Dokumen ini tidak menambah, mengubah,
atau menggantikan [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) dan
[`CLAUDE.md`](../CLAUDE.md).

| Status sumber | Arti |
|---|---|
| AVAILABLE | Dokumen ada di `main`. |
| PENDING SOURCE | Dokumen disebut owner tetapi belum ada di repositori; isinya tidak boleh dibuat ulang dari ingatan atau dugaan. |

## Daftar batch

| Batch | Dokumen sumber | Status sumber | Status persetujuan | Catatan |
|---|---|---|---|---|
| Baseline | [`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md), [`CLAUDE.md`](../CLAUDE.md) | AVAILABLE | LOCKED | Sumber tertinggi. |
| Inventaris | [`PLANNING_HISTORY.md`](PLANNING_HISTORY.md) | AVAILABLE | Di-merge (PR #4) | Snapshot berbasis repo per `260800d`. |
| Batch 01 | [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) | AVAILABLE (di root repo, bukan `docs/`) | **OWNER-APPROVED WITH CONDITIONS** (D-01, 2026-11-23): M-01–M-19 disetujui; detail OPEN/PARTIAL tercatat di §7 dokumen | Matriks §2 historis; §7.1 berlaku. Merge PR #5 sendiri bukan persetujuan. |
| Batch 02 | [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md) | AVAILABLE | OWNER-APPROVED (header dokumen, TD:3) | Disalin tanpa perubahan dari lampiran owner (SHA-256 `0a27420e…a980b`). |

## Keputusan owner D-01–D-11 (2026-11-23)

Sumber: [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) (kolom
"Keputusan final"). Status Batch 02 di bawah tetap dicatat apa adanya;
tabel ini menunjukkan keputusan owner yang lebih baru.

| ID | Status | Ringkasan | Menyelesaikan / memperbarui | Masih OPEN / NOT VERIFIED |
|---|---|---|---|---|
| D-01 | APPROVED (PR #18) | M-01–M-19 disetujui dengan ketentuan | B-3, K-3 | Detail per M (`PLANNING_COMPLETION_BATCH.md` §7.1) |
| D-02 | OWNER APPROVED | DataStore untuk preferensi aplikasi; Room sumber kebenaran data akademik | K-1 / B-7 (DataStore kini keputusan owner, bukan klaim blueprint) | Versi DataStore |
| D-03 | OWNER APPROVED | Restore BKP:M-2 default; BKP:M-1 eksplisit + peringatan + konfirmasi + snapshot pra-restore; tanpa auto-merge | OD-3; konflik BL:63–64 vs B01 M-16 | Retensi snapshot, batas penyimpanan, detail rollback, parameter kripto (OD-1, OD-8) |
| D-04 | OWNER APPROVED | Skor terbaik per komponen; kelulusan per modul (≥ 80 dan tiap komponen ≥ 75, tanpa pembulatan); unlock linear; program = 16 modul lulus + capstone | OP-2; OP-1 sebagian (tingkat modul) | Agregasi numerik tingkat program, representasi angka (OP-3), rubrik capstone (CU-9), implikasi komponen per modul (CU-2) |
| D-05 | OWNER APPROVED | minSdk 29 | B-9, OD-10; usulan 24 dan rekomendasi 26 SUPERSEDED | — |
| D-06 | OWNER APPROVED (provisional) | Baseline toolchain sementara | O-01 (arah) | Cek ulang sebelum scaffold; verifikasi CI setelah izin implementasi; versi DataStore |
| D-07 | OWNER APPROVED | BKP:AB-1: Auto Backup dinonaktifkan | O-07, OD-4 | Perilaku transfer antarperangkat (NOT VERIFIED) |
| D-08 | OWNER APPROVED | `INTERNET` diizinkan untuk fitur opsional; lab Python tanpa jaringan | O-02 | Isolasi jaringan lab (PY:F-09 NOT VERIFIED) |
| D-09 | OWNER APPROVED | JUnit, kotlinx-coroutines-test, Compose UI Test, Robolectric | O-16 (baseline) | Alat screenshot (milestone UI); verifikasi terhadap D-06 |
| D-10 | PLANNING APPROVED; EXECUTION NOT AUTHORIZED | Ambang PY:F-01–F-15 disetujui sebagai rencana | Batas uji O-04 | Izin eksekusi; runtime; PY:F-01–F-15 NOT VERIFIED |
| D-11 | DEFERRED; NOT AUTHORIZED | Implementasi ditunda sampai perencanaan selesai dan izin baru | — | Izin implementasi |

Status Batch 02 "Tetap OPEN" yang terdampak: O-01 → provisional (D-06);
O-02 → diputuskan (D-08); O-07 → diputuskan (D-07); O-16 → baseline
diputuskan (D-09). O-04, O-06, O-08, O-09, O-10, O-11 tetap OPEN.

## Dokumen batch (spesifikasi, bukan sumber keputusan)

Dokumen berikut menjabarkan kriteria dan usulan. Isinya **bukan**
keputusan kecuali butir yang berlabel APPROVED dengan rujukan ke
blueprint atau Batch 02.

| Batch | Dokumen | PR | Topik OPEN utama |
|---|---|---|---|
| 03 | [PYTHON_OFFLINE_FEASIBILITY_PLAN.md](PYTHON_OFFLINE_FEASIBILITY_PLAN.md) | #8 | O-04 |
| 04 | [ANDROID_TOOLCHAIN_DECISION_SHEET.md](ANDROID_TOOLCHAIN_DECISION_SHEET.md) | #9 | O-01, minSdk |
| 05 | [ASSESSMENT_STATE_MACHINE_SPEC.md](ASSESSMENT_STATE_MACHINE_SPEC.md) | #10 | OP-1–OP-12 |
| 06 | [ENCRYPTED_BACKUP_RESTORE_SPEC.md](ENCRYPTED_BACKUP_RESTORE_SPEC.md) | #11 | OD-1–OD-10 (O-06, O-07) |
| 07 | [JAPAN_CALENDAR_HOLIDAY_SPEC.md](JAPAN_CALENDAR_HOLIDAY_SPEC.md) | #12 | CO-1–CO-7 (O-05) |
| 08 | [UI_ACCESSIBILITY_VISUAL_SPEC.md](UI_ACCESSIBILITY_VISUAL_SPEC.md) | #13 | UO-1–UO-10 |
| 09 | [CURRICULUM_OFFLINE_LAB_SPEC.md](CURRICULUM_OFFLINE_LAB_SPEC.md) | #14 | CU-1–CU-11, M-01–M-19 |
| 10 | [FINAL_PLANNING_READINESS_REVIEW.md](FINAL_PLANNING_READINESS_REVIEW.md) | #15 | Ringkasan kesiapan |
| Audit | [BATCH_01_10_UNFINISHED_AUDIT.md](BATCH_01_10_UNFINISHED_AUDIT.md) | #16 | UW-01–UW-54 |
| Checklist | [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) | #17, #18, #19 | D-01–D-11 (lihat §Keputusan owner) |
| UW-22 | [NUMERIC_PRECISION_DECISION_SHEET.md](NUMERIC_PRECISION_DECISION_SHEET.md) | PR cleanup UW-22/44/45 | OP-3 / UW-22 — menunggu owner |

## Aturan rujukan lintas dokumen (editorial, UW-44)

Beberapa dokumen memakai ID lokal yang sama (mis. `B-01` kasus batas vs
blocker `B-1`; `M-1` mode restore vs gap `M-01`). ID yang ada **tidak**
diganti. Saat merujuk ID lokal dari dokumen lain, tulis kode dokumennya:

| Kode | Dokumen |
|---|---|
| `BL:n` / `TD:n` | Blueprint / Batch 02 (nomor baris) |
| `B01 M-xx` | Batch 01 |
| `PY:` | Python plan |
| `TC:` | Toolchain sheet |
| `ASM:` | Assessment spec |
| `BKP:` | Backup spec |
| `CAL:` | Calendar spec |
| `UI:` | UI spec |
| `CUR:` | Curriculum spec |
| `HS:B-n` | Blocker di HANDOFF_STATE |
| `FIN:` | FINAL_PLANNING_READINESS_REVIEW (mis. `FIN:C-4`) |
| `AUD:D-xx` | Pemeriksaan konsistensi audit §4 |
| `NUM:` | NUMERIC_PRECISION_DECISION_SHEET |
| `UW-nn` | Register audit (ID global, unik) |
| `D-01`–`D-11` (tanpa kode) | Keputusan owner (global) — [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md) |
| `O-`, `OP-`, `OD-`, `CO-`, `UO-`, `CU-`, `KS-`, gate QG (`AB-`, `OF-`, `GR-`, `LB-`, `CL-`, `SC-`, `AP-`, `EV-`) | ID global unik, tanpa kode. Pengecualian: opsi Auto Backup `AB-1`–`AB-3` di BKP §7 bentrok dengan gate `AB-1`–`AB-8`, sehingga ditulis `BKP:AB-x` |

Contoh: `ASM:B-03` (kasus batas skor), `BKP:M-1` (mode restore),
`HS:B-3` (blocker status Batch 01).

## Batch 02 — Keputusan teknis

Sumber: [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md)
(rujukan `TD:n` = nomor baris). Tabel ini hanya meringkas; bila berbeda,
dokumen sumber yang berlaku. Status **APPROVED** berarti *arah* desain
disetujui, belum tentu setiap detail implementasi (TD:69).

### APPROVED (arah disetujui)

| ID | Area | Keputusan | Masih OPEN di dalamnya | Sumber |
|---|---|---|---|---|
| O-12 | Dependency injection | DI manual untuk V1; Hilt hanya bila kompleksitas menuntut dan didokumentasikan. | — | TD:17 |
| O-13 | Navigasi | Navigation Compose untuk lima tab. | Kompatibilitas library diverifikasi sebelum implementasi. | TD:18 |
| O-14 | Struktur Gradle | Satu modul `app` di V1; dipecah hanya bila ada kebutuhan terbukti. | — | TD:19 |
| O-15 | State UI | UI state immutable + StateFlow; effect sekali jalan eksplisit; koleksi lifecycle-aware. | Detail mekanisme effect. | TD:20 |
| O-03 | Presisi skor | Hitung dengan presisi penuh; pembulatan hanya untuk tampilan, bukan untuk ambang lulus. | Representasi numerik, agregasi, aturan seri. | TD:21, TD:30 |
| O-17 | XP farming | XP diberikan sekali per identitas aktivitas yang sama; pengulangan/remedial tidak memberi XP lagi; tanpa penalti. | Definisi identitas, batas, kasus tepi. | TD:22, TD:38 |
| O-05 | Hari libur Jepang | Dataset hari libur offline + proses pembaruan terkontrol; libur pengganti dan *citizens' holidays*. | Sumber data, rentang tahun, mekanisme pembaruan. | TD:23 |
| CI | Verifikasi build | GitHub Actions sebagai lingkungan build/lint/unit test/APK utama. | Tidak ada workflow sebelum izin implementasi. | TD:24 |
| UI | Desain visual | Colorful Academy, Compose native; lima tab Home, Learn, Lab, Calendar, Progress; palet dan guardrail Batch 01. | Aset, tipografi, target terukur. | TD:25 |
| Arsitektur | Baseline | Kotlin + Compose + M3, Room/SQLite, DataStore, MVVM/Repository, offline-first. | — | TD:26 |

### Tetap OPEN

| ID | Topik | Bukti yang dibutuhkan sebelum dipilih | Sumber |
|---|---|---|---|
| O-04 | Eksekusi Python offline | Kelayakan runtime, packaging offline, isolasi kode, batas memori/waktu, uji perangkat. | TD:45 |
| O-06 | Backup terenkripsi | Threat model, envelope berversi, AEAD, KDF + parameter, uji restore. AES-GCM/Argon2id hanya kandidat. | TD:46 |
| O-01 | Versi toolchain, min/target SDK | Kombinasi kompatibel dari dokumentasi resmi tepat sebelum scaffold pertama. | TD:47 |
| O-07 | Kebijakan backup OS Android | Aturan `allowBackup`/ekstraksi data. | TD:48 |
| O-02 | Video opsional / izin `INTERNET` | Strategi buka eksternal yang aman offline, izin minimal. | TD:49 |
| O-08 | R8/minify, ukuran APK | Profil rilis dan dampak test. | TD:50 |
| O-09 | Infrastruktur emulator/perangkat | Runner yang layak dan tersedia. | TD:51 |
| O-10 | Penandatanganan/distribusi | Manajemen kunci dan kanal rilis. | TD:52 |
| O-11 | Akses SDK di cloud | Opsional; tidak memblokir rencana GitHub Actions. | TD:53 |
| O-16 | Library testing | Stack unit/integrasi/UI/screenshot yang kompatibel. | TD:54 |

Celah rincian M-01–M-19 yang belum terselesaikan tetap mengacu ke matriks
Batch 01 (TD:56).

### Catatan konsistensi

| # | Temuan | Status |
|---|---|---|
| K-1 | Catatan historis: TD:26 menyebut **DataStore** sebagai bagian "existing blueprint baseline", padahal `BLUEPRINT_LOCKED.md` hanya menyebut Room/SQLite (BL:11). DataStore bukan bagian blueprint awal. Owner kemudian menyetujuinya melalui D-02 (2026-11-23) sebagai keputusan baru, khusus untuk preferensi aplikasi; Room/SQLite tetap sumber kebenaran data akademik dan versi DataStore masih OPEN. TD:26 tidak diubah. Blocker terkait: B-7 (HANDOFF_STATE). | Selesai oleh D-02 |
| K-2 | TD:5 dan TD:68 merujuk `docs/PLANNING_COMPLETION_BATCH.md`, sedangkan file tersebut berada di root repo. | Informasi |
| K-3 | (Diselesaikan oleh D-01 M-18: nama tab blueprint berlaku.) Batch 01 M-18 memakai label tab "Learning Journey, IT Lab, Schedule/Calendar"; blueprint (BL:69) dan TD:25 memakai "Learn, Lab, Calendar". Blueprint yang berlaku. | Informasi |
| K-4 | ID lokal dipakai ulang antardokumen (mis. `A-xx`, `B-0x`, `F-xx`, `M-1…M-3` vs `M-01…M-19`). Rujukan lintas dokumen harus menyebut nama dokumen. Detail: FINAL_PLANNING_READINESS_REVIEW KS-07. | Informasi |
| K-5 | `QUALITY_GATES.md` GR-10 lebih lama dari TD:21; arah "bulatkan hanya untuk tampilan" sudah APPROVED (TD:21), agregasi/representasi tetap OPEN. | Informasi |
