# IT ZERO → HERO — Protokol Efisiensi Token Agen (CB-0.5)

Berlaku untuk sesi agen di repositori ini. Mutu didahulukan (TE-10):
tidak ada verifikasi atau konten wajib yang dilewati demi menghemat token.
Pemakaian token/kuota akun **tidak dapat diamati** dari dalam sesi; protokol
ini tidak mengklaim angka penghematan.

## 1. Aturan TE-01–TE-14

| ID | Aturan | Penerapan di proyek ini |
|---|---|---|
| TE-01 | Muat konteks selektif | Mulai dari `CLAUDE.md` → [PROJECT_MAP.md](PROJECT_MAP.md) → [HANDOFF_STATE.md](HANDOFF_STATE.md) §Checkpoint aktif → spesifikasi tugas aktif. Ikuti rute R-01–R-10 di peta |
| TE-02 | Kerja berbasis delta | Pakai checkpoint, `git diff`, `git log`, daftar berkas berubah; jangan membaca ulang seluruh repositori |
| TE-03 | Hindari baca ulang | Baca ulang hanya bila konteks hilang, berkas berubah, ada kontradiksi, atau verifikasi tepat membutuhkannya |
| TE-04 | Satu tugas aktif utama | Checkpoint hanya punya satu "Tugas aktif" |
| TE-05 | Anti-loop | Setelah dua kegagalan setara: hentikan dan nilai ulang (skill systematic-debugging). Setelah tiga pendekatan yang berbeda secara material gagal: catat blocker di checkpoint dan laporkan. Jangan mengulang kegagalan identik tanpa bukti baru |
| TE-06 | Pemuatan skill progresif | Muat hanya skill yang relevan (routing §2); jangan memuat keempat skill untuk setiap tugas |
| TE-07 | Checkpoint | Perbarui checkpoint pada transisi fase, verifikasi penting, blocker, tanda pemadatan konteks, dan sebelum sesi berakhir |
| TE-08 | Laporan ringkas | Laporan: perubahan, bukti, blocker, aksi berikutnya. Bukti rinci disimpan di dokumen repositori |
| TE-09 | Batch operasi independen | Gabungkan panggilan alat yang independen; hindari panggilan dan agen redundan |
| TE-10 | Mutu didahulukan | Verifikasi dan konten wajib tidak pernah dilewati |
| TE-11 | Keputusan proyek menang | Keputusan owner dan aturan proyek mengalahkan rekomendasi skill eksternal (lihat §4) |
| TE-12 | Lanjut dari checkpoint terverifikasi | Jangan mengulang pekerjaan yang sudah selesai dan terverifikasi |
| TE-13 | Pakai ulang bukti verifikasi | Boleh bila versi sumber, lingkup, dan asumsi tidak berubah; sebutkan commit sumber bukti |
| TE-14 | Berhenti setelah deliverable | Setelah deliverable yang diotorisasi selesai (PR dibuka): STOP; jangan menambah pekerjaan |

## 2. Routing skill

| Skill | Muat saat | Jangan muat saat |
|---|---|---|
| planning-with-files | Tugas multi-tahap, perencanaan persisten, checkpoint, pemulihan sesi | Pertanyaan sederhana, edit satu berkas |
| systematic-debugging | Validasi gagal, inkonsistensi skor/maksimum, kegagalan berulang, analisis akar masalah | Tidak ada kegagalan |
| verification-before-completion | Klaim selesai/PASS, penandaan COMPLETE di audit, pembuatan PR, handoff | Eksplorasi awal |
| receiving-code-review | Temuan review independen, revisi, temuan yang disanggah, cek regresi | Tidak ada umpan balik review |

Proyek tetap dapat dinavigasi tanpa skill eksternal: aturan inti TE-01–TE-14,
peta, dan checkpoint ada di dokumen ini, [PROJECT_MAP.md](PROJECT_MAP.md), dan
[HANDOFF_STATE.md](HANDOFF_STATE.md).

## 3. Kontrak checkpoint persisten

Checkpoint disimpan di [HANDOFF_STATE.md](HANDOFF_STATE.md) §Checkpoint aktif
(berkas yang di-commit; bertahan setelah sesi berakhir dan pemadatan konteks).
Tanggung jawab `task_plan.md` / `findings.md` / `progress.md` dari Planning
with Files dipetakan ke dokumen yang ada; berkas itu **tidak** dibuat di root
repositori:

| Berkas Planning with Files | Dipetakan ke |
|---|---|
| `task_plan.md` (fase, keputusan) | HANDOFF_STATE §Checkpoint aktif + prompt owner + PR |
| `findings.md` (temuan) | Dokumen bukti tugas (`review.md` modul, laporan validasi, audit) |
| `progress.md` (log sesi) | Riwayat PR + "Tugas terakhir" di HANDOFF_STATE; bagian audit bertanggal |

Field wajib: tugas aktif dan lingkup otorisasi · fase · selesai · sisa ·
berkas relevan · branch dan commit · keputusan · blocker · pendekatan gagal ·
bukti verifikasi · aksi berikutnya yang diizinkan · kondisi berhenti.

Dilarang di checkpoint: kredensial, rahasia, email pribadi, jejak penalaran
privat. Jangan mengandalkan berkas sementara atau yang di-gitignore sebagai
satu-satunya checkpoint. Catatan kerja lokal (mis. `.planning/`) boleh
dipakai sementara, tetapi bukan sumber otoritatif dan tidak di-commit.

## 4. Konflik skill vs aturan proyek (dimenangkan aturan proyek)

| Instruksi skill | Aturan yang berlaku |
|---|---|
| Planning with Files: jalankan `scripts/init-session.sh`, hook otomatis | Skrip dan hook tidak dipasang (registry §3.1); pakai checkpoint §3 secara manual |
| Planning with Files: buat `task_plan.md` dulu, "2-Action Rule" | Checkpoint di HANDOFF_STATE diperbarui per TE-07; tidak menulis setiap dua aksi |
| Planning with Files: `session-catchup.py --replay` | Tidak dipasang; jangan membaca transkrip sesi lokal |
| systematic-debugging: tulis test gagal (`superpowers:test-driven-development`) | Skill TDD ON HOLD; untuk dokumentasi, reproduksi = skrip validasi di scratchpad. Test aplikasi dilarang (tidak ada implementasi) |
| receiving-code-review: balas thread via `gh api` | Komentar GitHub hanya bila owner meminta; `gh` hanya untuk pencarian |
| receiving-code-review: "human partner" | = owner; ChatGPT = reviewer eksternal; persetujuan merge hanya kalimat owner (GITHUB_BRIDGE §5) |
| Skill apa pun: merge/commit otomatis, melewati gerbang | Dilarang; NO AUTO-MERGE |

## 5. Baseline efisiensi

Baseline pertama (sesi CB-0.5) dicatat di
[CB05_VALIDATION_REPORT.md](CB05_VALIDATION_REPORT.md) §3. Pembanding:
sesi produksi W2 (setelah diizinkan) mencatat metrik yang sama.
