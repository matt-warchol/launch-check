# Publishing guide

## Prepared distribution

This release is prepared as a portable Agent Skill and a source repository suitable for GitHub. It has not been uploaded, installed globally, or submitted to a marketplace. Publishing destination and licensing were not specified in the original request; this guide keeps those decisions explicit.

Two archives accompany the source folder:

- `launch-check-1.1.0.zip`: one top-level skill folder containing the runtime files and licensing notice.
- `launch-check-source-1.1.0.zip`: complete source repository, including documentation and author validation tooling.

## Before public release

1. Choose the license and copyright-holder attribution. No open-source permission is assumed. If choosing MIT or another license, add its complete text to a root `LICENSE`, copy it into the distributed skill folder, and update frontmatter and the licensing notices. Use the rights holder's actual chosen name; do not guess it from a local username.
2. Review the validation report and perform a representative runtime trial on a disposable project. This is a recommendation to substantiate a stable-release claim, not a claim that the current package has passed an independent agent test.
3. Choose the repository owner/name and support route. The package has no invented maintainer identity, contact address, or repository link.
4. Recheck dated source guidance if the publication date differs materially from this review. Set the release version consistently in skill metadata and the changelog. Use `1.1.0` for this release.
5. Run validation, rebuild archives after any changes, and inspect their contents for unintended local data. Do not publish the input attachment unless the owner separately wants it included.

## Validate locally

Python and PyYAML are development-only dependencies. They are not required to invoke the skill.

From the source repository root, use an isolated environment:

```sh
python3 -m venv /tmp/launch-check-dev
/tmp/launch-check-dev/bin/python -m pip install -r requirements-dev.txt
/tmp/launch-check-dev/bin/python tools/validate_package.py
```

If the host provides the skill-creator validator, also run its `scripts/quick_validate.py` against `skills/launch-check`. The included validator adds local-link and presentation-metadata checks; neither evaluates agent behavior or SEO effectiveness.

## GitHub release

Create a repository under the intended account and upload the contents of this source folder, preserving the `skills/` layout. Review the diff before committing. Use the prepared [release notes](RELEASE-NOTES.md) as the release description, tag the candidate version, and attach the standalone skill ZIP. Attach the source ZIP if useful; GitHub also generates source archives for tags. This guide does not itself authorize public upload.

After publication, test installation from the published files in a clean project and add the real repository/install link to the README. Confirm license text travels with the standalone archive. A repository release and an in-product marketplace listing are separate distribution steps.

## Rebuild the ZIP files

From the repository root, this standard-library script writes archives to its parent directory. It uses explicit include paths so it does not package a repository's `.git`, environment files, or unrelated local files.

```sh
python3 - <<'PY'
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path.cwd()
skill = root / "skills/launch-check"
version = "1.1.0"  # update with the release metadata
assert (skill / "SKILL.md").is_file()
with ZipFile(root.parent / f"launch-check-{version}.zip", "w", ZIP_DEFLATED) as z:
    for p in sorted(skill.rglob("*")):
        if p.is_file() and not p.is_symlink():
            z.write(p, Path(skill.name) / p.relative_to(skill))
includes = ["README.md", "CHANGELOG.md", "LICENSE-NOTICE.md",
            "requirements-dev.txt", "tools", "docs", "skills"]
if (root / "LICENSE").is_file():
    includes.append("LICENSE")
with ZipFile(root.parent / f"launch-check-source-{version}.zip", "w", ZIP_DEFLATED) as z:
    for entry in includes:
        base = root / entry
        for p in sorted(base.rglob("*")) if base.is_dir() else [base]:
            if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts:
                z.write(p, Path("launch-check-source") / p.relative_to(root))
PY
```

## Optional plugin/marketplace distribution

This is a skill repository, not a submitted plugin. If you choose an OpenAI plugin listing, wrap the existing `skills/` folder using the current [plugin packaging instructions](https://developers.openai.com/plugins/build/plugins), then follow that platform's submission requirements. The portable manifest and any presentation assets belong to that additional distribution format. Do not assume a GitHub upload automatically creates a listing or that another marketplace accepts the same archive layout.

The [Agent Skills specification](https://agentskills.io/specification) defines the core folder format. Host-specific install and submission behavior should be checked at publication time. Packaging guidance checked 2026-09-29.
