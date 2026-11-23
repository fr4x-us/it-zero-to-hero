# IT ZERO → HERO — Technical Decisions Batch 02

**Status:** OWNER-APPROVED PLANNING DECISIONS · PREPARATION ONLY · NO APPLICATION IMPLEMENTATION  
**Date:** 2026-11-23  
**Authority:** Supplements `docs/BLUEPRINT_LOCKED.md`, `CLAUDE.md`, `docs/PLANNING_HISTORY.md`, and `docs/PLANNING_COMPLETION_BATCH.md`. Does not supersede locked blueprint or authorize coding.

## 1. Scope and provenance

The owner explicitly approved the recommendations presented in Batch 02. This document records **only those recommendations** as approved planning choices, with feasibility-sensitive items remaining provisional. Prior planning details are in `PLANNING_COMPLETION_BATCH.md`; do not duplicate its 19-item recovery matrix. This is not evidence of a successful build, test, security assessment, or device validation.

**Decision states:** APPROVED = owner-approved design direction; CONDITIONAL = approved direction contingent on verification; OPEN = no final selection or parameter. Where technical evidence conflicts with a direction, report it and seek approval before changing the product contract.

## 2. Approved technical directions

| ID | Area | Decision | State / constraint |
|---|---|---|---|
| O-12 | Dependency injection | Prefer **manual dependency injection** for V1; introduce Hilt only if complexity warrants it and change is documented. | APPROVED |
| O-13 | Navigation | Prefer **Navigation Compose** for the five-tab Android-native application. | APPROVED; verify current library compatibility before implementation |
| O-14 | Gradle structure | Start with a **single `app` module** in V1; split modules only when a demonstrated need exists. | APPROVED |
| O-15 | UI state | **Immutable UI state + StateFlow**; use explicit one-time effect handling and lifecycle-aware collection. | APPROVED; effect mechanism detail OPEN |
| O-03 | Scoring precision | Keep calculations at full defined precision; **round only for display**, not for pass/fail thresholds. | APPROVED; numeric representation, aggregation and tie rules OPEN |
| O-17 | XP farming | A qualifying activity awards XP **only once for the same activity identity**; repeat/remedial attempts do not award that XP again. No XP penalties for remedials. | APPROVED; identity definition, caps and edge cases OPEN |
| O-05 | Japan holidays | Ship an **offline-available Japanese holiday dataset** and provide a controlled update process; handle substitute/citizens' holidays. | APPROVED; source, year range and update mechanism OPEN |
| CI | Build verification | **GitHub Actions** is the primary build/lint/unit-test/APK environment because cloud environment lacks usable Android SDK access. | APPROVED planning direction; no workflow before implementation authorization |
| UI | Visual design | **Colorful Academy**, bright Android-native Compose UI; five tabs Home, Learn, Lab, Calendar, Progress; follow approved palette and accessibility/anti-generic guardrails in Batch 01. | APPROVED; assets, typography and measurable targets OPEN |
| Architecture | Baseline | **Kotlin + Jetpack Compose + Material 3, Room/SQLite, DataStore, MVVM/Repository, offline-first**. | Existing blueprint baseline, reaffirmed; not a new architecture override |

### Assessment acceptance implications

- Passing requires **weighted score >= 80** and **every component >= 75**, using unrounded scores.
- Weighting remains theory 30%, lab 40%, mini-project 20%, concept explanation 10%.
- Retain the best score for each component and every attempt record. Do not infer how to aggregate across modules without a separate approved rule.
- No AI-based evaluation. Concept explanation requires objectively checkable offline assessment; detailed rubric remains OPEN.

### Gamification acceptance implications

- Academic scores and XP remain independent.
- Define a stable activity identity and persistent award ledger before XP implementation. Repeating an activity or taking a remedial must not mint XP for that same identity.
- Streaks, achievements, mastery, XP amounts, level thresholds, and handling revised content remain OPEN.

## 3. High-risk decisions deliberately left OPEN

| ID | Topic | Required evidence before final selection |
|---|---|---|
| O-04 | Offline Python execution | Android runtime feasibility, offline packaging, API compatibility, user-code isolation, memory/time limits, app-data protection, tests on supported devices. No claims of secure sandbox without evidence. |
| O-06 | Portable encrypted backup | Threat model, versioned file envelope, authenticated encryption, password KDF and parameters, integrity checks, restore rollback and recovery tests. AES-GCM/Argon2id remain candidates, not approved parameters. |
| O-01 | Toolchain versions and min/target SDK | Choose a mutually compatible set using official Android/Kotlin/Gradle documentation immediately before first scaffold; record pinned versions and verification evidence. |
| O-07 | Android OS backup policy | Determine sensitive-data exposure and extraction/allowBackup rules. |
| O-02 | Optional video/INTERNET permission | Choose an offline-safe external-opening strategy and least-privilege permissions. |
| O-08 | R8/minification and APK size | Determine release profile and test impact. |
| O-09 | Emulator/device test infrastructure | Select viable runner and verify availability. |
| O-10 | Signing/distribution | Decide safe key management and release channel. |
| O-11 | Cloud SDK access | Optional; do not block GitHub Actions plan on it. |
| O-16 | Testing libraries | Select compatible unit, integration, UI and screenshot testing stack with evidence. |

**Still unresolved within partially recovered M-01–M-19:** detailed lessons/question banks, per-lesson time allocations, unlock rules, score aggregation, objective explanation rubrics, exam duration formula, project fixtures, Python/SQL lab specifications, XP catalog, company-calendar import, reminder behavior, backup retention/file format, UI assets and accessibility/device targets. The Batch 01 recovery matrix remains the source of these gaps.

## 4. Risk-first preparation sequence (not implementation authorization)

1. Prepare a **Python offline feasibility test plan**: candidate runtimes, success/failure criteria, security limitations, supported Android targets. No prototype until separately authorized.
2. Prepare a **toolchain compatibility decision sheet** based on official documentation, without generating Gradle project files.
3. Prepare **assessment state-machine and persistence acceptance criteria**, including timer/process death and unrounded pass rules.
4. Prepare **backup threat model and restore acceptance criteria**; do not choose cryptographic parameters by guesswork.
5. Prepare **holiday dataset/update specification** and **UI accessibility/screenshot acceptance criteria**.

## 5. Repository integration and review rules

- Add this file as `docs/TECHNICAL_DECISIONS_BATCH_02.md` in **one documentation-only PR**. Optionally add a link to it in an existing documentation index, but avoid unrelated edits.
- Do **not** rewrite historical `PLANNING_HISTORY.md` or silently reclassify every OPEN item as resolved. O-03, O-05, O-12–O-15, and O-17 have an approved **direction**, not necessarily every implementation detail.
- Do **not** modify `docs/BLUEPRINT_LOCKED.md`, `CLAUDE.md`, skills, workflows, Gradle, source code, tests, assets, or build configurations.
- Report only: files changed, consistency findings, unresolved blockers, PR link. Do not rerun previously passed audits without a concrete conflict.
- **Application implementation remains forbidden** until explicit separate owner authorization.
