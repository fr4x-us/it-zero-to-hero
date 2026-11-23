# IT ZERO → HERO — Planning Completion Batch 01

**Status:** OWNER-APPROVED WITH CONDITIONS (2026-11-23, D-01) · PREPARATION ONLY · NO APPLICATION IMPLEMENTATION  
**Approval:** M-01–M-19 approved by the owner on 2026-11-23 as recorded in §7. Details listed as OPEN/PARTIAL in §7 remain undecided. Originally merged as *DRAFT FOR OWNER REVIEW* (PR #5).  
**Date:** 2026-11-23  
**Authority:** Supplement to `docs/BLUEPRINT_LOCKED.md` and `CLAUDE.md`; neither is modified or superseded.  
**Purpose:** Transfer previously agreed planning details into a single, reviewable document, without fabricating missing technical decisions.

## 1. Evidence and decision convention

- **LOCKED / RECOVERED:** Explicitly agreed during the IT ZERO → HERO planning conversation and consistent with the locked blueprint. These additions need owner approval before being treated as repository-authoritative.
- **PARTIAL:** Intent and behavior agreed, but implementation details, content, or numerical parameters are still missing.
- **OPEN:** No approved choice yet. Recommendations are not decisions.
- The existing `PLANNING_HISTORY.md` is a **repository-only** historical inventory; its `MISSING SOURCE` labels were correct at the time. This supplement supplies some missing conversation-derived context but is not a verbatim transcript.
- The project remains **native Android**, **offline-first**, and **not authorized for implementation**.

## 2. Recovery matrix for M-01 to M-19

| ID | Status | Recovered specification / remaining gap |
|---|---|---|
| M-01 | PARTIAL | This document records decisions from prior planning. Full verbatim chat transcript is not included. |
| M-02 | PARTIAL | **16-week outline:** W1 hardware/software; W2 OS and files; W3 networking; W4 cybersecurity; W5 math foundations; W6 binary and Boolean logic; W7 computational thinking; W8 algorithms and flowcharts; W9 Python basics; W10 variables and data types; W11 conditions; W12 loops, functions and debugging; W13 databases and SQL; W14 HTML/CSS; W15 Git/GitHub; W16 capstone. Full lesson scripts, examples, diagrams, and item banks remain unwritten. |
| M-03 | PARTIAL | Total **128 hours over 16 weeks**, nominally **8 h/week**, with a **default Sat 4 h + Sun 4 h**. Work shifts can move sessions; no forced daily schedule. Exact per-lesson allocations remain OPEN. |
| M-04 | PARTIAL | Four phases of four modules; **linear unlock**. Academic passing is **weighted ≥80 AND every component ≥75**. Exact unlock behavior for partial, remedial, and preview content needs a detailed acceptance rule. |
| M-05 | PARTIAL | Theory **30%**, lab **40%**, mini-project **20%**, concept explanation **10%**; pass if weighted ≥80/100 **and** each component ≥75/100. Remedial unlimited; **best score per component** retained; **all attempts** preserved. Exact numeric precision, aggregation across modules, and tie handling remain OPEN. |
| M-06 | PARTIAL | Concept explanation (10%) must use **structured, objectively checkable offline tasks**, not AI scoring or ungraded free essays. Task bank and rubrics remain OPEN. |
| M-07 | PARTIAL | Theory exams are timed; **duration derived from question count, type, and complexity**, not a single arbitrary global timer. Persist deadline and autosaved answers; timer continues while app closed; reopening after deadline grades answers already saved. Detailed duration formula and question formats remain OPEN. |
| M-08 | PARTIAL | Labs and mini-projects **untimed**; learners may pause/resume. Autosave/crash recovery applies. Exact interruption and submission rules remain OPEN. |
| M-09 | OPEN | Mini-project/capstone topics, rubrics, test fixtures, and detailed acceptance tests have not been finalized. |
| M-10 | PARTIAL | Offline IT Lab: Python editor/runtime, logic/flowcharts, binary, SQL, HTML/CSS, test cases, and mini-projects. **Python runtime feasibility and sandbox/isolation must be validated** before selecting technology. Python libraries, SQL dialect, datasets, and execution limits remain OPEN. |
| M-11 | PARTIAL | XP, levels, achievements, mastery, and streaks are **separate from academic grades**. No XP farming or XP penalty for remedial attempts. Exact XP formula, caps, levels, and badge catalog remain OPEN. |
| M-12 | PARTIAL | Japanese-style calendar in **Asia/Tokyo**; **Sundays and Japanese national holidays red, Saturdays blue**; include substitute holidays and citizen's holidays. Era labels and precise localization details remain OPEN. |
| M-13 | PARTIAL | Distinguish **Japanese national holidays** from **company-specific working/off days**. Calendar must accommodate actual work schedule and reschedule learning. Company calendar source/import and default workday assumptions remain OPEN. |
| M-14 | PARTIAL | Study schedule starts **January 2027**, default weekends 4h/day, adjustable for shifts. Incomplete-session reminder **every 60 minutes**, subject to Android permissions; quiet hours **22:00–07:00 JST**. Exact notification rescheduling, permission-denial, and doze behavior remain OPEN. |
| M-15 | PARTIAL | Local automatic snapshots and manual export are agreed. Snapshot frequency, retention count, and storage quotas remain OPEN. |
| M-16 | PARTIAL | Portable manual **password-encrypted backup**; restore requires preview, explicit confirmation, integrity/version validation, rollback, preservation of prior attempts, and protection of existing data. **No automatic merging of grade histories**. AES-256-GCM and Argon2id were proposed, **not approved cryptographic parameters**. Password loss makes export unrecoverable. Exact format/KDF/parameterization remain OPEN. |
| M-17 | PARTIAL | **Colorful Academy**: bright, cheerful, professional, gamified. Proposed/approved visual palette from planning: purple `#7565F5`, blue `#3B82F6`, green `#22C55E`, yellow `#FFB020`, pink `#FF6B91`. Typography, icons, illustration assets and accessibility contrast validation remain OPEN. |
| M-18 | PARTIAL | Bottom navigation: **Home dashboard, Learning Journey, IT Lab, Schedule/Calendar, Progress**. Profile via avatar. Planned views include lesson, quiz, exam, result, XP/mastery/achievement, academic report, onboarding **four screens**, settings, backup/restore. Detailed screen fields and navigation states remain OPEN. |
| M-19 | PARTIAL | Readable, accessible, responsive Android UI. Exact `minSdk`, screen breakpoints, tablet/orientation support and measurable accessibility targets remain OPEN. |

## 3. Product and interaction invariants

### Curriculum and learning
- Audience: Indonesian-speaking beginner preparing for university IT study.
- Explanations and learning material primarily in **Bahasa Indonesia**.
- Theory + diagrams + interactive illustrations + simulations + exercises + quizzes + labs + exams + glossary + case studies.
- Optional curated YouTube content: Indonesian preferred; English acceptable with Indonesian subtitles. Core lessons must remain usable offline.
- Start January 2027; nominal 16 weeks / 128 hours. Rescheduling must not erase completed work.

### Assessment and persistence
- The four assessment components and two-part pass rule are **independent** of gamification.
- Preserve each attempt, keep best component score, prevent remedial XP farming.
- Use rule-based adaptive practice while keeping a fixed competency blueprint for formal exams.
- Concept explanation grading must be objective and offline, with auditable rubrics.
- Theory timer must use a persistent absolute deadline; autosave answers and recover gracefully after process death.

### Offline labs and safety
- Offline Python runtime is a **hard feasibility gate**, not a promise of a specific interpreter or security isolation method.
- HTML/CSS and SQL labs should work offline; avoid assuming WebView behavior or SQL sandbox until tested.
- Learner code must not have unrestricted access to app data, private files, or network by default.

### Visual design guardrails (anti-generic / anti-'AI slop')
- Design **Android-native Compose screens**, not web dashboards ported to Android.
- Use the locked Colorful Academy palette **semantically**, not as random gradients.
- Prioritize hierarchy, typography, whitespace, distinct screen composition, readable learning content, and accessible controls.
- Avoid repetitive card grids, excessive gradients, decorative emoji, generic stock art, ornamental glassmorphism, and motion without purpose.
- Design one reusable system of components and states, but allow intentional visual variety between Home, Journey, Lab, Calendar, and Progress.
- Validate with real device-size previews/screenshots, touch targets, contrast, dynamic text, loading/empty/error states, and accessibility before accepting a UI milestone.
- These are **quality guidelines**, not authorization to redesign the approved UI.

## 4. Decision register: O-01 to O-17

The following remain **OPEN** until approved or feasibility-tested. Do not silently promote recommendations to locked decisions.

| ID | Decision still required | Proposed resolution stage |
|---|---|---|
| O-01 | Compatible Kotlin/Compose/AGP/Gradle/JDK/SDK versions | Immediately before first Android scaffold; verify official compatibility |
| O-02 | INTERNET permission and optional YouTube opening method | Architecture preparation |
| O-03 | Numeric precision, rounding, grade aggregation | Assessment specification and unit-test design |
| O-04 | Offline Python runtime and execution isolation | **High-priority technical feasibility spike** |
| O-05 | Authoritative Japan holiday dataset and offline update policy | Calendar specification |
| O-06 | Encryption algorithm, KDF, parameters and file envelope | Security design and threat model |
| O-07 | Android system backup policy for sensitive data | Security design |
| O-08 | R8/minify and release APK size policy | Build/release design |
| O-09 | Emulator/device test runner | CI test planning |
| O-10 | Signing and distribution channel | Release planning |
| O-11 | Cloud Android SDK availability (currently unavailable) | Optional; GitHub Actions remains primary build path |
| O-12 | DI choice (manual/Hilt) | Architecture preparation |
| O-13 | Navigation library | Architecture preparation |
| O-14 | Gradle module structure | Architecture preparation |
| O-15 | Compose state/effect conventions | Architecture preparation |
| O-16 | Testing stack incl. screenshot/robolectric | Quality engineering preparation |
| O-17 | Exact anti-XP-farming semantics | Gamification acceptance criteria |

**Risk order:** (1) Python runtime feasibility/isolation; (2) build toolchain + CI viability; (3) assessment state and persistence; (4) backup cryptography and restore; (5) calendar correctness; (6) UI accessibility and screenshot verification. Priorities are planning recommendations, not product changes.

## 5. Documentation and review procedure

1. Review this document against `BLUEPRINT_LOCKED.md`, `CLAUDE.md`, and `PLANNING_HISTORY.md`.
2. Preserve `PLANNING_HISTORY.md` as a historical repository snapshot; do not rewrite its past evidence claims. Add a link to this supplement only if authorized.
3. Record unresolved questions as OPEN; do not invent missing lesson banks, design assets, numerical algorithms, or test outcomes.
4. Make **one documentation-only PR** after owner approval. No application code, Gradle project, CI workflow, external script execution, or tool installation.
5. In PR review, check that no locked decision was weakened and no recommendation was mislabeled as LOCKED.
6. Implementation remains prohibited until separately and explicitly authorized.

## 6. Batch completion criteria

- [x] Owner reviews and approves the supplement as an accurate record of prior decisions. — 2026-11-23, with conditions (§7).
- [x] Single documentation PR contains only the approved planning supplement (and optionally a link in a docs index). — PR #5 added only this file.
- [ ] PR review confirms consistency with locked blueprint. — Pending review of the D-01 recording PR (§7.3 lists the consistency check).
- [x] No implementation work started. — Repository contains documentation only.

## 7. Persetujuan owner — D-01 (2026-11-23)

Owner menyetujui M-01–M-19 pada 2026-11-23 (keputusan D-01 di
[`docs/OWNER_DECISION_CHECKLIST.md`](docs/OWNER_DECISION_CHECKLIST.md)),
dengan ketentuan bahwa seluruh detail teknis, konten, dan pengujian yang
belum selesai tetap OPEN/PARTIAL. Persetujuan ini **tidak** mengubah
`docs/BLUEPRINT_LOCKED.md`, **tidak** memberi izin implementasi atau
prototipe, dan **tidak** menyelesaikan keputusan D-02–D-11.

Matriks §2 di atas dipertahankan sebagai catatan historis. Bila ada
perbedaan, tabel §7.1 (keputusan owner) yang berlaku untuk M-01–M-19,
dan blueprint tetap berlaku di atas keduanya.

### 7.1 Keputusan owner per butir

| ID | Disetujui owner | Masih OPEN / PARTIAL |
|---|---|---|
| M-01 | Dokumen diterima sebagai ringkasan perencanaan, bukan transkrip verbatim. | — |
| M-02 | Kerangka kurikulum 16 minggu disetujui. | Materi lengkap belum selesai. |
| M-03 | Target 128 jam; jadwal fleksibel mengikuti shift; tanpa tenggat kalender wajib. | Alokasi per pelajaran. |
| M-04 | Empat fase; unlock linear per modul; remedial tanpa batas; pratinjau materi modul berikutnya boleh; latihan dan ujian terkunci sampai prasyarat lulus; modul yang sudah lulus tetap dapat diakses. | Agregasi skor (D-04). |
| M-05 | Bobot 30/40/20/10; lulus bila nilai tertimbang ≥ 80 dan setiap komponen ≥ 75; semua percobaan disimpan; nilai terbaik per komponen dipertahankan. | Presisi, agregasi, dan basis kelulusan formal (D-04). |
| M-06 | Penjelasan konsep dinilai dengan tugas objektif, terstruktur, offline, tanpa AI. Format: memilih alasan, mengurutkan proses, mencocokkan konsep, menemukan kesalahan. | Rubrik, nilai parsial, bank soal. |
| M-07 | Ujian teori berwaktu berdasarkan jumlah, jenis, dan kompleksitas soal; deadline persisten; timer berjalan saat aplikasi ditutup; jawaban tersimpan dapat dipulihkan; status autosave terlihat. | Rumus durasi, frekuensi autosave, mitigasi manipulasi waktu. |
| M-08 | Lab dan mini-project tanpa batas waktu; pause/resume; autosave dan pemulihan progres tersimpan. | Detail interupsi dan submission. |
| M-09 | Kebutuhan mini-project dan capstone beserta rubrik dan acceptance test disetujui. | Topik, fixture, rubrik, dan acceptance test konkret. **M-09 belum selesai.** |
| M-10 | Lab offline dipertahankan: Python, logika/flowchart, biner, SQL, HTML/CSS, test case. | Runtime Python dan keamanan isolasi menunggu feasibility gate (D-10); prototipe butuh izin terpisah. |
| M-11 | XP, level, achievement, mastery, dan streak terpisah dari nilai akademik; remedial tidak menyebabkan farming atau penalti XP. | Formula dan katalog. |
| M-12 | Kalender Asia/Tokyo; Minggu dan hari libur nasional Jepang merah, Sabtu biru; termasuk libur pengganti dan *citizens' holiday*. | Data resmi dan aturan lokalisasi sampai diverifikasi. |
| M-13 | Libur nasional Jepang dipisahkan dari hari kerja/libur perusahaan; mendukung perubahan shift dan reschedule. | Sumber kalender perusahaan. |
| M-14 | Mulai Januari 2027; jadwal awal akhir pekan 4 jam/hari, fleksibel; pengingat sesi belum selesai tiap 60 menit, tunduk pada izin dan pembatasan Android; jam tenang 22:00–07:00 JST. | Detail penjadwalan. |
| M-15 | Snapshot lokal otomatis dan ekspor manual. | Frekuensi, retensi, kuota. |
| M-16 | Backup portabel terenkripsi kata sandi; pratinjau; konfirmasi eksplisit; pemeriksaan integritas/versi; rollback; perlindungan data dan riwayat percobaan; tanpa auto-merge riwayat nilai. | Algoritma, KDF, parameter, dan kebijakan restore (keputusan terpisah: D-03, OD-1). |
| M-17 | Colorful Academy dan palet yang tercatat dipertahankan; aksesibilitas/kontras wajib diperhatikan. | Tipografi, aset, validasi visual (termasuk solusi kontras UO-1). |
| M-18 | Lima tab Home, Learn, Lab, Calendar, Progress; profil melalui avatar; onboarding empat layar; layar pendukung. | Detail navigasi. |
| M-19 | UI native Android yang responsif dan aksesibel. | minSdk (D-05), breakpoint, tablet/orientasi, target pengujian. |

### 7.2 Status setelah persetujuan

| Butir | Status |
|---|---|
| M-01 | APPROVED |
| M-02–M-19 | APPROVED (arah/kebutuhan) dengan detail OPEN/PARTIAL sesuai §7.1 |
| M-09 | Kebutuhan APPROVED; isi konkret **belum selesai** |
| D-02–D-11 | Tetap AWAITING OWNER |
| PLANNING CLEAR | NO |
| IMPLEMENTATION VERIFIED | NO |

### 7.3 Pemeriksaan konsistensi saat pencatatan

| # | Temuan | Penanganan |
|---|---|---|
| 1 | Semua butir §7.1 sejalan dengan `docs/BLUEPRINT_LOCKED.md` (BL:15–71); tidak ada keputusan blueprint yang diubah. | — |
| 2 | M-18 memakai nama tab blueprint (Home, Learn, Lab, Calendar, Progress); label lama di matriks §2 ("Learning Journey, IT Lab, Schedule/Calendar") tidak berlaku. | Dicatat; DECISIONS_LOG K-3 |
| 3 | M-03 "tanpa tenggat kalender wajib" mengatur jadwal belajar; tenggat persisten ujian teori (BL:36, M-07) tetap berlaku. | Dicatat, tidak ada konflik |
| 4 | M-04 menambah detail: pratinjau boleh, latihan/ujian terkunci sampai prasyarat lulus, modul lulus tetap dapat diakses. Sejalan dengan BL:21. | Dicatat |
| 5 | M-16 "tanpa auto-merge riwayat nilai" dan BL:63–64 "attempt-history preservation" tetap harus dipertemukan oleh mode restore. | **Tidak diselesaikan di sini**; tetap D-03 |
| 6 | DataStore (TD:26) tidak disebut dalam M-01–M-19. | **Tidak diselesaikan di sini**; tetap D-02 |
| 7 | M-17 mengonfirmasi palet; temuan kontras (UI spec §2.2) tetap berlaku. | Tetap UO-1 |

