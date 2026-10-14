# Launch-check repository

This repository is the source for the `launch-check` Agent Skill, also called “launch-skill” in chat. The published skill is `skills/launch-check/`; its GitHub source is `https://github.com/matt-warchol/launch-check` on `main`.

For a request to update an installed copy, follow the update section in `skills/launch-check/SKILL.md` and use `skills/launch-check/scripts/update_from_github.py`. Do not substitute a similarly named repository or assume that editing this checkout refreshes personal installations.

For source changes, edit the skill in this repository, bump its version, update the README/changelog where behavior changed, run `tools/validate_package.py` and the skill validator, then sync personal installations only within the user's authorization. Do not overwrite local differences without a backup.
