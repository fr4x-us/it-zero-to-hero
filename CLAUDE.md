
# IT ZERO → HERO — Project Instructions

## Project status
PREPARATION ONLY. Implementation is not authorized.

## Product
Native Android APK using Kotlin, Jetpack Compose,
Material 3, Room, and offline-first architecture.

## Source of truth
Read docs/BLUEPRINT_LOCKED.md before proposing changes.
Treat locked product decisions as immutable unless the
project owner explicitly approves a revision.

## Non-negotiable rules
- Do not convert the project into a website or PWA.
- Do not modify the locked curriculum or grading rules.
- Do not add AI tutoring or AI-based grading.
- Do not start application implementation without approval.
- Do not fabricate tests, build results, or APK artifacts.
- Do not commit secrets, passwords, or signing keys.
- Prefer official Android documentation for technical decisions.
- Explain technical limitations and security risks.

## Workflow
1. Read project documentation.
2. Inspect available environment and skills.
3. Identify blockers and dependencies.
4. Propose a small, verifiable task.
5. Wait for implementation authorization.
6. Once authorized, use branches, tests, and checkpoints.

## Pull requests — NO AUTO-MERGE
- After each batch: one PR to main, report, then STOP.
- Never merge a PR unless the user's new message explicitly says
  "PR #X telah direview ChatGPT dan disetujui untuk merge." for that PR.
- Approval covers only the named PR. Silence is not approval.
- Full rules: docs/GITHUB_BRIDGE.md §5.

## Communication
Use Indonesian for explanations and progress reports.

## Agent workflow (CB-0.5)
- Start: CLAUDE.md → docs/PROJECT_MAP.md (routes R-01–R-10) →
  docs/HANDOFF_STATE.md "Checkpoint aktif" → active task spec.
- Source precedence: owner instruction > BLUEPRINT_LOCKED > this file and
  GITHUB_BRIDGE §5 > owner decisions > specs > audit/roadmap > agent docs >
  external skills. Project rules always override skill instructions.
- Token protocol TE-01–TE-14: docs/AGENT_TOKEN_EFFICIENCY_PROTOCOL.md.
- Skills (load only when relevant; see protocol §2 and
  docs/AGENT_SKILL_REGISTRY.md): planning-with-files (multi-stage work,
  checkpoints; modified local instruction-only variant: no hooks,
  allowed-tools, or scripts), systematic-debugging
  (failed validation, repeated failures), verification-before-completion
  (before any completion/PASS claim, audit COMPLETE, PR, handoff),
  receiving-code-review (review findings and revisions).
- Checkpoints live in docs/HANDOFF_STATE.md (committed); never store
  secrets there. Do not create root task_plan.md/findings.md/progress.md.
- Owner approval gates are unchanged: no merge without the exact sentence,
  no implementation, no W2–W16 production without authorization.
