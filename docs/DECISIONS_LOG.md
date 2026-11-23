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
| Batch 01 | [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) | AVAILABLE (di root repo, bukan `docs/`) | Di-merge (PR #5); header dokumen masih **DRAFT FOR OWNER REVIEW** dan kriteria selesai §6 belum dicentang | Perlu konfirmasi owner apakah merge PR #5 = persetujuan isi. |
| Batch 02 | [`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md) | AVAILABLE | OWNER-APPROVED (header dokumen, TD:3) | Disalin tanpa perubahan dari lampiran owner (SHA-256 `0a27420e…a980b`). |

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
| K-1 | TD:26 menyebut **DataStore** sebagai bagian "existing blueprint baseline", padahal `BLUEPRINT_LOCKED.md` hanya menyebut Room/SQLite (BL:11). Dicatat apa adanya; perlu konfirmasi owner bahwa DataStore adalah tambahan yang disetujui, bukan bagian blueprint. | Butuh konfirmasi |
| K-2 | TD:5 dan TD:68 merujuk `docs/PLANNING_COMPLETION_BATCH.md`, sedangkan file tersebut berada di root repo. | Informasi |
| K-3 | Batch 01 M-18 memakai label tab "Learning Journey, IT Lab, Schedule/Calendar"; blueprint (BL:69) dan TD:25 memakai "Learn, Lab, Calendar". Blueprint yang berlaku. | Informasi |
| K-4 | ID lokal dipakai ulang antardokumen (mis. `A-xx`, `B-0x`, `F-xx`, `M-1…M-3` vs `M-01…M-19`). Rujukan lintas dokumen harus menyebut nama dokumen. Detail: FINAL_PLANNING_READINESS_REVIEW KS-07. | Informasi |
| K-5 | `QUALITY_GATES.md` GR-10 lebih lama dari TD:21; arah "bulatkan hanya untuk tampilan" sudah APPROVED (TD:21), agregasi/representasi tetap OPEN. | Informasi |
