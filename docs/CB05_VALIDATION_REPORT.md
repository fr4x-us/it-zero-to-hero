# IT ZERO → HERO — Laporan Validasi CB-0.5

Tanggal 2026-11-24 · branch `planning/cb-0-5-agent-workflow` · basis `main`
= `df76c5f` (merge PR #25). Jenis bukti: **E** = eksekusi nyata di sesi ini ·
**I** = inspeksi manual · **S** = simulasi (bukan bukti aktivasi runtime).

## 1. Merge PR #25 (prasyarat)

| Pemeriksaan | Hasil | Bukti |
|---|---|---|
| Kalimat otorisasi | Ada di pesan owner ("PR #25 telah direview ChatGPT dan disetujui untuk merge.") | E. Pesan sebelumnya tanpa kalimat itu → merge ditahan |
| Repositori, status | `fr4x-us/it-zero-to-hero`; open, bukan draft | E (`pull_request_read`) |
| SHA head | `f4cb17335c65489b165d2214e309ff2f00a765ee` = SHA diotorisasi | E; merge memakai `expectedHeadSha` |
| `mergeable_state` / checks | `clean`; 0 check run (repositori tanpa CI) | E |
| PR #25 diubah sebelum merge | Tidak | E |
| Hasil | `merged: true`; merge commit `df76c5fbf946e6e8d2ca9e8e87505454041623a3` (metode merge, sama seperti PR #24) | E |

## 2. V01–V18

| ID | Validasi | Hasil | Jenis | Bukti / alasan |
|---|---|---|---|---|
| V01 | Berkas instalasi wajib | **PASS** | E | Keempat folder berisi `SKILL.md` + `LICENSE`; berkas pendukung sesuai registry §3 |
| V02 | Provenans dan lisensi | **PASS** | E | `cmp` byte-identik dengan klon upstream pada commit pin; LICENSE MIT disalin; `SOURCES.md` + registry §2 |
| V03 | Penemuan dan aktivasi nyata | **PASS (sesi ini)** / NOT VERIFIED (sesi baru) | E | Panggilan pertama "Unknown skill"; setelah daftar skill sesi diperbarui, keempatnya terdaftar dan dimuat via `Skill`. Sesi baru belum diamati. PwF: hook tidak dapat diamati langsung (registry §5) |
| V04 | Akurasi path PROJECT_MAP | **PASS** | E | 48 tautan, 0 rusak (seluruh repositori: 1 tautan menggantung, di `SKILL.md` upstream PwF → `plan-inventory.md`, sengaja tidak dipasang; registry SK-09); 5 path kode, 0 hilang; rentang `s01..s20` (20 berkas), `s01..s06` (6), `les-01..04`, `act-01..03` ada |
| V05 | Simulasi rute tugas W2 (tanpa konten W2) | **PASS** | S | Rute R-02: awal = CB-0, baris W2 di rencana produksi, `curriculum/mod-w01/` (acuan); bersyarat = `CURRICULUM_OFFLINE_LAB_SPEC.md` + decision sheet; berhenti = tidak ada otorisasi produksi → simulasi berhenti di langkah pertama. Tidak ada `curriculum/mod-w02/` dibuat (E: `ls curriculum` = `mod-w01`) |
| V06 | Pemulihan dari checkpoint | **PASS** | E + S | 12/12 field kontrak ada di HANDOFF §Checkpoint aktif; basis commit di checkpoint = `origin/main` (`df76c5f`); semua berkas yang dirujuk ada. Simulasi: sesi baru membaca checkpoint → "Aksi berikutnya" = tidak ada sampai owner → tidak mengulang pekerjaan selesai |
| V07 | Perilaku anti-loop | **PASS** | E + S | Kegagalan nyata: `Skill` → "Unknown skill" (1×). Tidak diulang identik; akar masalah diselidiki (daftar skill sesi belum diperbarui) lalu pemanggilan diulang hanya setelah bukti baru (skill muncul di daftar). Aturan TE-05 (2 setara → nilai ulang; 3 berbeda → blocker) tertulis di protokol |
| V08 | Bukti sebelum klaim selesai | **PASS** | I | Skill verification-before-completion dimuat sebelum klaim; setiap PASS di tabel ini merujuk keluaran perintah. Klaim yang tidak terbukti ditandai NOT VERIFIED (V03 sesi baru, hook PwF) |
| V09 | Penanganan review contoh + kesadaran regresi | **PASS** | S | Temuan contoh: "maksimum lab act-02 c01 hanya 9, bukan 12". Diperiksa terhadap `lab/act-02/checks.yaml`: `points` 12, `reachable_values` [0, 4, 8, 12] → temuan ditolak dengan bukti teknis (pola receiving-code-review), tanpa perubahan berkas |
| V10 | Perlindungan persetujuan owner | **PASS** | E | Merge PR #25 ditahan saat kalimat otorisasi tidak ada; dilakukan hanya setelah kalimat tepat + SHA cocok. PR CB-0.5 tidak di-merge |
| V11 | Kepatuhan lingkup perencanaan | **PASS** | E | `git diff --name-only main...HEAD`: hanya `.claude/skills/` (4 skill), `CLAUDE.md`, `README.md`, `docs/*.md`, `curriculum/mod-w01/review.md`. Tidak ada kode Kotlin/Gradle/CI/Python/APK |
| V12 | Konsistensi spesifikasi | **PASS** | E | Roadmap §2: 56 butir = 32 COMPLETE / 4 OPEN / 12 BLOCKED / 3 DEFERRED / 5 NOT VERIFIED; P 32/43 — sama dengan audit §19.2 dan HANDOFF. Rujukan "UW-36 BLOCKED/RM-Q2 AWAITING" yang tersisa hanya di bagian audit bertanggal lama (historis) |
| V13 | Tidak ada berkas perencanaan tandingan | **PASS** | E | Tidak ada `task_plan.md`/`findings.md`/`progress.md`/`.planning` di root; templat hanya di folder skill. PROJECT_MAP menyatakan diri bukan sumber kebijakan |
| V14 | Pelaporan kompatibilitas jujur | **PASS** | I | PwF = PARTIALLY_COMPATIBLE (skrip/hook tidak dipasang); konflik skill dicatat (registry §4, protokol §4) |
| V15 | Kesiapan rollback | **PASS** | I | Registry §6: per skill `git rm -r`, penuh `git revert`; tidak ada keadaan di luar repositori (tanpa settings global) |
| V16 | Efisiensi navigasi selektif | **PASS** | I | Rute R-01–R-10 memuat 1–4 dokumen awal (median 2–3) dari 40 dokumen di `docs/` |
| V17 | Keputusan dan batas review dipertahankan | **PASS** | E | D-01–D-37 tidak diubah (diff hanya menambah baris D-38); batas review independen tertulis di DECISIONS_LOG, checklist, audit §19.3, CB-0, `review.md` §11. `BLUEPRINT_LOCKED.md`, `TECHNICAL_DECISIONS_BATCH_02.md`, `PLANNING_COMPLETION_BATCH.md` tidak berubah |
| V18 | Berhenti setelah membuka PR CB-0.5 | **PASS (diterapkan saat penyerahan)** | I | Kondisi berhenti ada di checkpoint; tidak ada aksi setelah PR dibuka |

Ringkasan: 18 PASS (V03 PASS untuk sesi ini; aktivasi di sesi baru NOT
VERIFIED). 0 FAIL.

## 3. Baseline efisiensi (dapat diamati)

| Metrik | Nilai | Cara |
|---|---|---|
| TOKEN USAGE | **NOT MEASURABLE** | Tidak ada penghitung token/kuota di sesi |
| Panggilan alat (dari otorisasi merge sampai validasi) | 41 (Bash 30, Skill 5, Write 3, GitHub 2, ToolSearch 1) | Hitung dari transkrip sesi |
| Kegagalan alat | 1 (`Skill` "Unknown skill"); kegagalan berulang identik 0 | Idem |
| Berkas repositori yang disentuh perintah baca/edit | 19 unik; terbanyak: roadmap 8×, handoff 7×, audit 6× | Hitung path di perintah shell (mencakup edit, bukan hanya baca) |
| Baca ulang | Roadmap, handoff, audit dibaca per bagian berbeda (bukan seluruh berkas) | I |
| Overhead pemuatan skill | `SKILL.md`: 41.938 + 3.646 + 9.530 + 6.203 = 61.317 B (keempatnya dimuat sekali untuk bukti aktivasi; pemakaian normal memuat sesuai routing) | Ukuran berkas |
| Panjang rute navigasi | R-01–R-10: 1–4 dokumen awal | PROJECT_MAP §7 |
| Kelengkapan checkpoint | 12/12 field | V06 |
| Panjang laporan akhir | ≤ 13 butir ringkas; bukti rinci di dokumen ini | TE-08 |

Tidak ada persentase penghematan yang diklaim. Pembanding: sesi produksi W2
(setelah diizinkan) mencatat metrik yang sama.
