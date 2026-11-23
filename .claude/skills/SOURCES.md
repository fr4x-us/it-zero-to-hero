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
