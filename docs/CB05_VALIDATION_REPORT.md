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

## 2. V01–V18 (revisi F-27, setelah F-24–F-26)

Bukti tidak berubah dipakai ulang (TE-13) bila berkas dan lingkupnya tidak
berubah sejak `102b7a4`; baris yang diuji ulang ditandai **ulang**.

| ID | Validasi | Hasil | Jenis | Bukti / alasan |
|---|---|---|---|---|
| V01 | Berkas instalasi wajib | **PASS** (ulang) | E | Empat folder; masing-masing `SKILL.md` + `LICENSE`; PwF lokal hanya dua berkas itu |
| V02 | Provenans dan lisensi | **PASS** (ulang) | E | Tiga skill Superpowers: `cmp` identik dengan commit pin. PwF: dicatat sebagai **dimodifikasi** dengan hash upstream/lokal, commit pin, atribusi MIT (registry §3.1); `LICENSE` asli disalin |
| V03 | Penemuan dan aktivasi nyata | **NOT VERIFIED** (sebagian PASS) | E | Rinci di §2.1. Sesi ini: ditemukan + dimuat (keempatnya; PwF lokal diuji ulang setelah modifikasi). Sesi baru: belum diamati |
| V04 | Akurasi path PROJECT_MAP | **PASS** (ulang) | E | 48 tautan peta, 0 rusak; seluruh repositori 0 tautan rusak (SK-09 ditutup); berkas yang disebut di tabel rute §7 semuanya ada |
| V05 | Simulasi rute W2 (tanpa konten W2) | **PASS** | S | Bukti dipakai ulang; peta tidak berubah. `curriculum/` hanya `mod-w01` |
| V06 | Pemulihan dari checkpoint | **PASS** (ulang) | E + S | 12/12 field; "Versi kerja" = branch + SHA basis penuh (= `origin/main`) + rujukan head PR #26 (tanpa SHA dirinya sendiri); semua berkas yang dirujuk ada |
| V07 | Anti-loop | **PASS** | E + S | Bukti dipakai ulang + kejadian baru: pendekatan "skrip hilang sebagai batas keamanan" ditolak review → diganti pendekatan berbeda (hapus deklarasi), dicatat di "Pendekatan gagal" |
| V08 | Bukti sebelum klaim | **PASS** (ulang) | I | Klaim di laporan ini merujuk keluaran perintah; klaim lama yang terlalu luas (V03, status PwF) dikoreksi |
| V09 | Penanganan review + regresi | **PASS** | E + S | Simulasi lama dipakai ulang; review nyata F-24–F-27 ditangani per butir dengan bukti (§2.2) |
| V10 | Perlindungan persetujuan owner | **PASS** | E | Bukti dipakai ulang; PR #26 tidak di-merge |
| V11 | Lingkup perencanaan | **PASS** (ulang) | E | Diff revisi: hanya `.claude/skills/planning-with-files/`, `.claude/skills/SOURCES.md`, `CLAUDE.md`, dokumen `docs/` |
| V12 | Konsistensi spesifikasi | **PASS** | E | Jumlah audit tidak berubah (32/4/12/3/5 = 56; P 32/43); tidak ada dokumen status yang disentuh selain HANDOFF |
| V13 | Tidak ada berkas perencanaan tandingan | **PASS** (ulang) | E | Tidak ada `task_plan.md`/`findings.md`/`progress.md`/`.planning` di repositori, termasuk templat di folder skill (dihapus) |
| V14 | Kompatibilitas jujur | **PASS** | I | Varian PwF dicatat dimodifikasi; SK-06/SK-07/SK-10 sebagai sisa; sesi baru NOT VERIFIED |
| V15 | Kesiapan rollback | **PASS** (ulang) | I | Registry §6 ditambah prosedur pembaruan varian lokal |
| V16 | Efisiensi navigasi | **PASS** | I | Bukti dipakai ulang; peta tidak berubah |
| V17 | Keputusan dan batas review dipertahankan | **PASS** (ulang) | E | D-38, W01-ACC, bukti UW-36, dan jumlah audit tidak disentuh revisi ini; dokumen terkunci tidak berubah |
| V18 | Berhenti setelah PR | **PASS** | E | Setelah PR #26 dibuka, tidak ada aksi sampai instruksi revisi ini |

Ringkasan: **17 PASS, 1 NOT VERIFIED (V03), 0 FAIL.** CB-0.5 tidak
dinyatakan berhasil penuh selama V03 belum terverifikasi di sesi baru.

### 2.1 Tingkat bukti aktivasi (F-27)

| Tingkat | PwF (lokal, dimodifikasi) | verification-before-completion | systematic-debugging | receiving-code-review |
|---|---|---|---|---|
| Berkas terpasang | E: ya | E: ya | E: ya | E: ya |
| Penemuan (daftar skill sesi) | E: ya, deskripsi varian lokal muncul setelah modifikasi | E: ya | E: ya | E: ya |
| Pemuatan (`Skill`) | E: ya, isi varian lokal dimuat ulang setelah modifikasi | E: ya (berkas tidak berubah sejak) | E: ya | E: ya |
| Kompatibilitas mode instruksi | I: ya | I: ya | I: ya (SK-06) | I: ya (SK-07) |
| Perilaku alur kerja nyata | E sebagian: checkpoint HANDOFF dipakai dan diperbarui | E: dipakai sebelum klaim | S: V07 | S + E: V09, review F-24–F-27 |
| Aktivasi sesi baru | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |

### 2.2 Bukti F-24–F-26

| Temuan | Bukti |
|---|---|
| F-24 hook | Frontmatter PwF lokal hanya `name`, `description`. Pencarian `^hooks:` dan `type: command` di keempat folder skill: 0 hasil |
| F-25 izin | Pencarian `allowed-tools` di frontmatter keempat skill: 0 hasil (satu kemunculan hanya di teks catatan modifikasi PwF). Tiga skill Superpowers: frontmatter hanya `name`, `description`. Pengaturan izin global tidak diubah |
| F-26 varian lokal | SHA-256 upstream `b99281fc…19d58` (41.938 B) → lokal `9ae86193…74b7` (3.241 B). Berkas PwF: 6 `.md` + LICENSE (59.876 B `.md`) → `SKILL.md` + LICENSE. 0 tautan menggantung. Pemindaian ulang: 0 symlink, 0 Unicode tersembunyi, 0 `curl`/`wget` |

## 3. Baseline efisiensi (dapat diamati)

| Metrik | PR #26 awal | Revisi F-24–F-27 | Cara |
|---|---|---|---|
| TOKEN USAGE | **NOT MEASURABLE** | **NOT MEASURABLE** | Tidak ada penghitung token/kuota di sesi |
| Panggilan alat | 41 | 8 sampai laporan ini ditulis (hitungan parsial; commit/push/PR menyusul) | Hitung dari transkrip sesi |
| Kegagalan alat / kegagalan berulang identik | 1 / 0 | 0 / 0 | Idem |
| Berkas repositori yang disentuh | 19 unik | 12 berkas berubah (`git diff --name-only`) | Path di perintah shell / git |
| Ukuran `SKILL.md` keempat skill | 61.317 B | 22.620 B (PwF 41.938 → 3.241) | Ukuran berkas |
| Total berkas `.md` folder PwF | 59.876 B | 3.241 B | Ukuran berkas |
| Panjang rute navigasi | 1–4 dokumen awal | Sama | PROJECT_MAP §7 |
| Kelengkapan checkpoint | 12/12 | 12/12 ("Versi kerja" diperbaiki) | V06 |

Pengurangan ukuran berkas skill bukan pengukuran pemakaian token. Tidak ada
persentase penghematan yang diklaim.
