# IT ZERO → HERO — Registry Skill Agen (CB-0.5)

Otorisasi: owner, 2026-11-24 — pasang dan integrasikan **tepat empat** skill.
Skill lain (termasuk sisa Superpowers) **ON HOLD**. Skill Android yang sudah
ada sejak PR #1 tercatat di [`.claude/skills/SOURCES.md`](../.claude/skills/SOURCES.md)
dan tidak diubah. Bukti validasi: [CB05_VALIDATION_REPORT.md](CB05_VALIDATION_REPORT.md).

Status yang diizinkan: VERIFIED_ACTIVE · INSTALLED_UNVERIFIED ·
PARTIALLY_COMPATIBLE · DOCUMENTATION_ONLY · BLOCKED · REJECTED.
Keberadaan berkas saja **bukan** bukti aktivasi.

## 1. Ringkasan

| Skill | Path | Status | Isi |
|---|---|---|---|
| planning-with-files | `.claude/skills/planning-with-files/` | **VERIFIED_ACTIVE** (sesi ini; varian lokal **dimodifikasi**) | Varian instruksi saja; tanpa hook, `allowed-tools`, skrip, templat |
| verification-before-completion | `.claude/skills/verification-before-completion/` | **VERIFIED_ACTIVE** (sesi ini) | Identik upstream |
| systematic-debugging | `.claude/skills/systematic-debugging/` | **VERIFIED_ACTIVE** (sesi ini) | Identik upstream (subset berkas) |
| receiving-code-review | `.claude/skills/receiving-code-review/` | **VERIFIED_ACTIVE** (sesi ini) | Identik upstream |

"VERIFIED_ACTIVE (sesi ini)" = terdeteksi di daftar skill sesi Claude Code
Cloud ini **dan** berhasil dimuat dengan alat `Skill`. Aktivasi di **sesi baru**
(`session_011Df1V7VYFZ1Fdwc9jRg7nK`, setelah merge PR #26): **VERIFIED** untuk
keempatnya (V03 PASS, [CB05_VALIDATION_REPORT.md](CB05_VALIDATION_REPORT.md) §4).

## 2. Asal dan versi (diamati 2026-11-24)

| | Planning with Files | Superpowers (3 skill) |
|---|---|---|
| Repositori resmi | https://github.com/OthmanAdi/planning-with-files | https://github.com/obra/superpowers |
| Bintang GitHub (GitHub search API, 2026-11-24) | 28.213 | 325.518 |
| Push terakhir / diarsipkan | 2026-11-23 / tidak | 2026-11-03 / tidak |
| Rilis | Tag `v3.29.1`; commit pin = 1 commit setelah tag | Tag `v7.0.2` = commit pin |
| Commit pin | `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228` | `22f0b463e7a5e579904dd6211a520321035526f7` |
| Lisensi / atribusi | MIT, © 2026 Ahmad Adi — `LICENSE` disalin; atribusi di `SKILL.md` lokal | MIT, © 2025 Jesse Vincent — `LICENSE` di tiap folder |
| Pemeliharaan | Aktif (655 commit; SECURITY.md) | Aktif (687 commit) |

## 3. Berkas terpasang

### 3.1 planning-with-files — varian lokal (dimodifikasi, F-24–F-26)

| | Upstream (`skills/planning-with-files/SKILL.md` @ `aaa38bc`) | Lokal |
|---|---|---|
| SHA-256 `SKILL.md` | `b99281fc78316b7bcc0a9bbbcf1ca245bf514813380f9edbbccb40ec12e19d58` | `9ae86193abd4528557dd0e7dfe734f57aa0c89272ec7925bc7955047975674b7` |
| Ukuran `SKILL.md` | 41.938 B (534 baris) | 3.241 B |
| Berkas di folder | (PR #26 awal) `SKILL.md`, `reference.md` 8.455 B, `examples.md` 4.518 B, `templates/` 4.965 B, `LICENSE` — total `.md` 59.876 B | `SKILL.md`, `LICENSE` |
| Frontmatter | `name`, `description`, `user-invocable`, `allowed-tools`, `hooks` (5 event), `metadata` | `name`, `description` saja |

Ringkasan modifikasi:

- **Dihapus**: deklarasi `hooks` (UserPromptSubmit, PreToolUse, PostToolUse,
  Stop, PreCompact) dan `allowed-tools` (F-24, F-25); instruksi skrip
  (`init-session`, `check-complete`, `resolve-plan-dir`, `attest-plan`,
  `plan-doctor`, `set-active-plan`, ledger), `session-catchup.py`,
  `/plan-goal`, `/plan-loop`, `loop.md`, mode autonomous/gated, instalasi
  global; tautan `templates/`, `plan-inventory.md`, `reference.md`,
  `examples.md`.
- **Diadaptasi**: berkas perencanaan → HANDOFF_STATE §Checkpoint aktif dan
  dokumen bukti; "3-strike" → TE-05 protokol (tidak diduplikasi).
- **Dipertahankan**: prinsip memori di disk, pulihkan sebelum mulai, baca
  sebelum memutuskan, perbarui setelah bertindak, catat kegagalan, jangan
  ulangi kegagalan, simpan bukti, reboot test, aturan keamanan data.
- Sumber upstream yang tidak tersedia disebut eksplisit di `SKILL.md` lokal
  dengan larangan menjalankan/memasangnya.

### 3.2 Tiga skill Superpowers (byte-identik; `cmp` terhadap commit pin)

| Skill | Berkas | SHA-256 `SKILL.md` | Ukuran |
|---|---|---|---|
| verification-before-completion | `SKILL.md`, `LICENSE` | `2befe7fc…20b3` | 3.646 B |
| systematic-debugging | `SKILL.md`, `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`, `LICENSE` | `51c6435d…f202` | 9.530 B |
| receiving-code-review | `SKILL.md`, `LICENSE` | `091df162…2438` | 6.203 B |

Frontmatter ketiganya hanya `name` dan `description` (tanpa `hooks`,
`allowed-tools`, atau deklarasi perluasan izin lain) — diperiksa F-25.

### 3.3 Sengaja tidak dipasang

| Berkas upstream | Alasan |
|---|---|
| PwF `scripts/`, `hooks/`, `commands/`, `.claude-plugin/`, folder IDE lain, `templates/`, `reference.md`, `examples.md`, `plan-inventory.md`, `evals/`, i18n | Varian instruksi saja; templat akan memicu berkas perencanaan tandingan |
| systematic-debugging `find-polluter.sh`, `condition-based-waiting-example.ts` | Untuk suite test aplikasi; implementasi dilarang |
| Superpowers lain, hook `session-start`, `package.json`, `index.js` | Tidak diotorisasi (ON HOLD) |

## 4. Temuan keamanan dan kompatibilitas

| ID | Skill | Temuan | Status | Mitigasi dan bukti |
|---|---|---|---|---|
| SK-01 | PwF | Upstream mendeklarasikan 5 hook lifecycle yang menjalankan `skill-hook.sh`, dengan fallback ke `$HOME/.claude/skills/…` dan `$HOME/.claude/plugins/…` | **Ditutup (F-24)** | Deklarasi `hooks` dihapus dari frontmatter lokal. Bukti: pencarian `^hooks:` dan `type: command` di keempat folder skill = 0 hasil; frontmatter lokal hanya `name`, `description`. Tidak bergantung pada skrip yang hilang |
| SK-02 | PwF | `allowed-tools: "Read Write Edit Bash Glob Grep"` memperluas izin saat skill aktif | **Ditutup (F-25)** | Dihapus; izin memakai mekanisme izin Claude Code biasa. Pencarian `allowed-tools` di frontmatter keempat skill = 0 hasil. Pengaturan izin global tidak diubah |
| SK-03 | PwF | `session-catchup.py` dapat membaca transkrip sesi lokal | Ditutup | Skrip tidak dipasang; instruksi dihapus; `SKILL.md` lokal melarang membaca transkrip |
| SK-04 | PwF | Instruksi merujuk skrip yang tidak ada | Ditutup (F-26) | Instruksi dihapus; sumber yang tidak tersedia disebut tanpa perintah menjalankan |
| SK-05 | PwF | Overhead konteks 41.938 B | Ditutup | Varian lokal 3.241 B |
| SK-06 | systematic-debugging | Merujuk `superpowers:test-driven-development` dan `find-polluter.sh` (tidak dipasang) | Diterima | Protokol §4: reproduksi dengan skrip validasi di scratchpad; berkas tidak diubah (bukan masalah keamanan) |
| SK-07 | receiving-code-review | Menyarankan balasan thread via `gh api` | Diterima | Aturan proyek menang (komentar GitHub hanya atas permintaan owner) |
| SK-08 | Semua | Tanpa symlink, tanpa Unicode tersembunyi (Cf/Co/Cs), tanpa perintah jaringan atau eksekusi jarak jauh | — | Diperiksa ulang setelah modifikasi |
| SK-09 | PwF | Tautan menggantung ke `plan-inventory.md` | **Ditutup (F-26)** | Tautan dihapus di varian lokal; 0 tautan rusak di repositori |
| SK-10 | PwF | Hook dari pemuatan varian **upstream** sebelumnya mungkin masih terdaftar dalam sesi yang sama sampai sesi berakhir (perilaku host tidak dapat diamati) | **Ditutup** (sesi baru) | Sesi baru memuat varian lokal tanpa hook; tidak ada salinan upstream di `~/.claude` (laporan §4) |

## 5. Aktivasi

| Tingkat bukti | planning-with-files (lokal) | 3 skill Superpowers |
|---|---|---|
| Berkas terpasang | Ya | Ya |
| Ditemukan (daftar skill sesi) | Ya — deskripsi baru varian lokal muncul setelah modifikasi | Ya |
| Dimuat (`Skill`) | Ya — isi varian lokal dimuat setelah modifikasi | Ya (sebelum modifikasi PwF; berkas tidak berubah sejak itu) |
| Kompatibilitas mode instruksi | Ya (inspeksi: tidak ada instruksi yang membutuhkan alat yang tidak tersedia) | Ya, dengan SK-06/SK-07 |
| Perilaku alur kerja nyata | Sebagian: checkpoint HANDOFF dipakai dan diperbarui di revisi ini | verification-before-completion dipakai sebelum klaim; lainnya disimulasikan (V07, V09) |
| Aktivasi di sesi baru | **VERIFIED** (2026-11-24; laporan §4) | **VERIFIED** (2026-11-24; laporan §4) |

Verifikasi sesi baru selesai (V03 PASS): keempat skill ada di daftar skill
dan `planning-with-files` memuat varian lokal. Sisa kompatibilitas: SK-06,
SK-07 (diterima); hook milik host tidak dapat diaudit dari sesi.

Pemasangan tingkat repositori; tidak ada perubahan pengaturan akun global,
`settings.json`, plugin, atau hook.

## 6. Pembaruan dan rollback

**Pembaruan Superpowers** (butuh otorisasi owner): klon upstream, pin commit
baru, audit ulang (§4), salin berkas yang sama, `cmp`, perbarui §2–§3, uji
pemuatan, PR terpisah.

**Pembaruan planning-with-files**: baca diff upstream antara `aaa38bc` dan
commit baru; nilai apakah prinsip yang dipertahankan (§3.1) berubah; terapkan
perubahan secara manual ke varian lokal **tanpa** memasukkan kembali `hooks`,
`allowed-tools`, skrip, atau akses transkrip; perbarui commit pin, kedua
hash, dan ukuran di §3.1; uji pemuatan; PR terpisah.

**Rollback** satu skill: `git rm -r .claude/skills/<nama>/`, lalu hapus baris
di registry ini, routing di protokol §2, rujukan di `CLAUDE.md` dan
`SOURCES.md`; PR. Rollback penuh CB-0.5: `git revert` (setelah merge: revert
merge commit dengan `-m 1`). Proyek tetap dapat dinavigasi tanpa skill.
