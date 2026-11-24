# IT ZERO → HERO — Registry Skill Agen (CB-0.5)

Otorisasi: owner, 2026-11-24 — pasang dan integrasikan **tepat empat** skill.
Skill lain (termasuk sisa Superpowers) **ON HOLD**. Skill Android yang sudah
ada sejak PR #1 tercatat di [`.claude/skills/SOURCES.md`](../.claude/skills/SOURCES.md)
dan tidak diubah. Bukti validasi: [CB05_VALIDATION_REPORT.md](CB05_VALIDATION_REPORT.md).

Status yang diizinkan: VERIFIED_ACTIVE · INSTALLED_UNVERIFIED ·
PARTIALLY_COMPATIBLE · DOCUMENTATION_ONLY · BLOCKED · REJECTED.
Keberadaan berkas saja **bukan** bukti aktivasi.

## 1. Ringkasan

| Skill | Path | Status | Ringkasnya |
|---|---|---|---|
| planning-with-files | `.claude/skills/planning-with-files/` | **PARTIALLY_COMPATIBLE** | Terdeteksi dan dimuat; mode instruksi saja. Skrip, hook, perintah, dan `session-catchup.py` sengaja tidak dipasang |
| verification-before-completion | `.claude/skills/verification-before-completion/` | **VERIFIED_ACTIVE** | Terdeteksi dan dimuat |
| systematic-debugging | `.claude/skills/systematic-debugging/` | **VERIFIED_ACTIVE** | Terdeteksi dan dimuat; contoh `.ts` dan skrip `find-polluter.sh` tidak dipasang |
| receiving-code-review | `.claude/skills/receiving-code-review/` | **VERIFIED_ACTIVE** | Terdeteksi dan dimuat; aturan balasan GitHub dikalahkan aturan proyek |

"VERIFIED_ACTIVE" berarti: di sesi Claude Code Cloud ini, skill muncul di
daftar skill sesi dan berhasil dimuat dengan alat `Skill`. Belum diamati di
sesi baru yang dimulai setelah merge (lihat §5).

## 2. Asal dan versi (diamati 2026-11-24)

| | Planning with Files | Superpowers (3 skill) |
|---|---|---|
| Repositori resmi | https://github.com/OthmanAdi/planning-with-files | https://github.com/obra/superpowers |
| Bintang GitHub (diamati 2026-11-24 via GitHub search API) | 28.213 | 325.518 |
| Push terakhir | 2026-11-23 | 2026-11-03 |
| Diarsipkan | Tidak | Tidak |
| Rilis | Tag terbaru `v3.29.1`; commit pin = 1 commit setelah tag (`v3.29.1-1-gaaa38bc`); `metadata.version` 3.29.1 | Tag `v7.0.2` = commit pin; plugin version 7.0.2 |
| Commit pin | `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228` (2026-11-23) | `22f0b463e7a5e579904dd6211a520321035526f7` (2026-11-03) |
| Lisensi | MIT, © 2026 Ahmad Adi — disalin sebagai `LICENSE` di folder skill | MIT, © 2025 Jesse Vincent — disalin sebagai `LICENSE` di tiap folder skill |
| Kewajiban atribusi | Sertakan pemberitahuan hak cipta + izin MIT (terpenuhi) | Idem (terpenuhi) |
| Pemeliharaan | Aktif (655 commit; SECURITY.md dengan pelaporan privat) | Aktif (687 commit) |

## 3. Berkas yang dipasang (byte-identik dengan upstream; diperiksa `cmp`)

| Skill | Berkas dipasang | SHA-256 `SKILL.md` | Ukuran `SKILL.md` |
|---|---|---|---|
| planning-with-files | `SKILL.md`, `reference.md`, `examples.md`, `templates/{task_plan,findings,progress}.md`, `LICENSE` (dari `skills/planning-with-files/` + root `LICENSE`) | `b99281fc…19d58` | 41.938 B |
| verification-before-completion | `SKILL.md`, `LICENSE` | `2befe7fc…20b3` | 3.646 B |
| systematic-debugging | `SKILL.md`, `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`, `LICENSE` | `51c6435d…f202` | 9.530 B |
| receiving-code-review | `SKILL.md`, `LICENSE` | `091df162…2438` | 6.203 B |

Tidak ada berkas upstream yang diubah. Integrasi proyek ditulis terpisah di
[AGENT_TOKEN_EFFICIENCY_PROTOCOL.md](AGENT_TOKEN_EFFICIENCY_PROTOCOL.md) dan `CLAUDE.md`.

### 3.1 Sengaja tidak dipasang

| Berkas upstream | Alasan |
|---|---|
| PwF `scripts/` (skill-hook, init-session, check-complete, gate-stop, session-catchup.py, attest, ledger, dll.) | Hook otomatis menyuntikkan isi rencana pada setiap panggilan alat (overhead konteks), mode gated dapat memblokir Stop, `session-catchup.py` dapat membaca transkrip sesi lokal. Tidak dibutuhkan untuk mode instruksi |
| PwF `hooks/`, `commands/`, `.claude-plugin/`, folder IDE lain, `templates/loop.md`, template analytics/autonomous, `evals/`, `plan-inventory.md`, i18n | Di luar lingkup; plugin/perintah tidak diotorisasi |
| systematic-debugging `find-polluter.sh`, `condition-based-waiting-example.ts` | Menjalankan suite test aplikasi / kode TypeScript; tidak ada aplikasi (implementasi dilarang) |
| Superpowers lain (`using-superpowers`, `test-driven-development`, dll.), hook `session-start`, `package.json`, `index.js` | Tidak diotorisasi (ON HOLD) |

## 4. Temuan keamanan dan kompatibilitas

| ID | Skill | Temuan | Tingkat | Mitigasi |
|---|---|---|---|---|
| SK-01 | PwF | Frontmatter mendaftarkan hook UserPromptSubmit, PreToolUse, PostToolUse, Stop, PreCompact yang menjalankan `scripts/skill-hook.sh` setelah skill dimuat | Sedang | Skrip tidak dipasang. Perintah hook mencari skrip di folder skill lalu di `$HOME/.claude/skills/planning-with-files/` dan `$HOME/.claude/plugins/marketplaces/planning-with-files/`; ketiganya tidak ada → hook keluar 0 tanpa keluaran. **Jangan** memasang PwF tingkat pengguna (akan mengaktifkan hook) |
| SK-02 | PwF | `allowed-tools: "Read Write Edit Bash Glob Grep"` memberi izin alat tanpa prompt saat skill aktif | Sedang | Aturan proyek tetap berlaku (tidak ada implementasi, tidak ada merge otomatis). Tidak diubah agar berkas tetap identik upstream; dicatat sebagai risiko yang diterima dalam lingkup otorisasi |
| SK-03 | PwF | `session-catchup.py --replay` dapat membaca transkrip sesi lokal | Sedang | Skrip tidak dipasang; protokol §4 melarang |
| SK-04 | PwF | Instruksi merujuk skrip yang tidak ada (init-session, check-complete) | Rendah | Mode manual; checkpoint di HANDOFF_STATE (protokol §3) |
| SK-05 | PwF | Overhead konteks: `SKILL.md` 41.938 B dimuat penuh saat skill dipanggil | Rendah | Muat hanya untuk tugas multi-tahap (TE-06) |
| SK-06 | systematic-debugging | Merujuk `superpowers:test-driven-development` (tidak dipasang) dan `find-polluter.sh` (tidak dipasang) | Rendah | Protokol §4: reproduksi dengan skrip validasi di scratchpad |
| SK-07 | receiving-code-review | Menyarankan balasan thread via `gh api` | Rendah | Komentar GitHub hanya atas permintaan owner; `gh` hanya untuk pencarian |
| SK-09 | PwF | `SKILL.md` menautkan `plan-inventory.md` yang tidak dipasang (hanya mendokumentasikan `set-active-plan.sh`, yang juga tidak dipasang) → satu tautan relatif menggantung di berkas upstream | Rendah | Dibiarkan agar `SKILL.md` tetap identik upstream; fitur yang dirujuk memang tidak tersedia |
| SK-08 | Semua | Pemindaian: tanpa symlink, tanpa karakter Unicode tersembunyi (kategori Cf/Co/Cs), tanpa perintah jaringan (`curl`/`wget`) atau eksekusi jarak jauh di berkas yang dipasang; hanya tiga tautan dokumentasi (code.claude.com, github.com, manus.im) di teks Markdown | — | Diperiksa 2026-11-24 |

Tidak ada temuan eksfiltrasi data, kredensial, skrip jarak jauh, loop tak
terkendali, dependensi baru, atau penghindaran gerbang persetujuan pada
berkas yang dipasang. Tidak ada perintah curl-to-shell yang dijalankan.

## 5. Aktivasi

| Bukti | Hasil |
|---|---|
| Panggilan `Skill` segera setelah berkas disalin | "Unknown skill" (daftar skill sesi belum diperbarui) |
| Daftar skill sesi setelah pembaruan lingkungan | Keempat skill muncul dengan deskripsi upstream |
| Panggilan `Skill` (verification-before-completion, receiving-code-review, systematic-debugging, planning-with-files) | Keempatnya dimuat ("Launching skill") dengan isi `SKILL.md` |
| Hook PwF setelah dimuat | Tidak ada keluaran hook yang teramati pada panggilan alat berikutnya. Apakah hook terdaftar tidak dapat diamati langsung (NOT VERIFIED); efeknya nol karena skrip tidak ada |
| Sesi baru setelah merge | **NOT VERIFIED** — langkah verifikasi tersisa: di sesi baru, pastikan keempat skill ada di daftar skill |

Pemasangan tingkat repositori; tidak ada perubahan pengaturan akun global
atau `settings.json`.

## 6. Pembaruan dan rollback

**Pembaruan** (butuh otorisasi owner): klon upstream, pin commit baru,
audit ulang (§4), salin berkas yang sama, `cmp` terhadap upstream, perbarui
§2–§3, uji pemuatan, PR terpisah.

**Rollback** satu skill: `git rm -r .claude/skills/<nama>/` lalu hapus baris
di registry ini, routing di protokol §2, dan rujukan di `CLAUDE.md`; PR.
Rollback penuh CB-0.5: `git revert` commit CB-0.5 (setelah merge: revert
merge commit dengan `-m 1`). Proyek tetap dapat dinavigasi tanpa skill
(protokol §2). Tidak ada keadaan di luar repositori yang perlu dibersihkan.
