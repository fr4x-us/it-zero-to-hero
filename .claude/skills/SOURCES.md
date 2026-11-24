# Third-party skills — provenance

| Skill | Source path |
|---|---|
| android-dev | plugins/android-skills/skills/android-dev |
| compose | plugins/android-skills/skills/compose |
| android-data-layer | plugins/android-skills/skills/android-data-layer |
| android-testing | plugins/android-skills/skills/android-testing |
| kotlin-coroutines | plugins/android-skills/skills/kotlin-coroutines |

- Repository: https://github.com/rcosteira79/android-skills
- Commit: fa39ae26f224fac45b32280f66ac839ae57b4c64 (2026-11-10)
- License: MIT — see `LICENSE-android-skills.txt`
- Copied verbatim (SHA-256 verified); no files modified.
- Audit: Markdown only — no scripts, binaries, symlinks, or hidden Unicode characters.

Notes:
- Skills cross-reference each other as `android-skills:<name>` (plugin namespace).
  Installed here as project skills, they are invoked by their bare name (e.g. `compose`).
  Referenced skills not installed here (e.g. `kotlin-flows`, `android-ux`, `android-retrofit`) are unavailable.
- Some passages mention the `android` CLI (`android docs ...`, `android skills add ...`),
  which is not installed in this environment.
- Guidance is generic Android/KMP; `docs/BLUEPRINT_LOCKED.md` and `CLAUDE.md` take precedence.

## CB-0.5 agent workflow skills (2026-11-24)

| Skill | Source | Commit | License |
|---|---|---|---|
| planning-with-files | https://github.com/OthmanAdi/planning-with-files `skills/planning-with-files` | aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228 | MIT (`planning-with-files/LICENSE`) |
| verification-before-completion | https://github.com/obra/superpowers `skills/verification-before-completion` | 22f0b463e7a5e579904dd6211a520321035526f7 (v7.0.2) | MIT (`<skill>/LICENSE`) |
| systematic-debugging | idem `skills/systematic-debugging` | idem | idem |
| receiving-code-review | idem `skills/receiving-code-review` | idem | idem |

Copied verbatim (byte-compared with `cmp`); subset of files only. Scripts and
hooks of planning-with-files are intentionally not installed. Full audit,
status and rollback: `docs/AGENT_SKILL_REGISTRY.md`.

