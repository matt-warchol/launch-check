#!/usr/bin/env python3
"""Check or update personal launch-check installs from the GitHub main branch."""

from __future__ import annotations

import argparse
import filecmp
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


REPO = "https://github.com/matt-warchol/launch-check.git"
SKILL_PATH = Path("skills/launch-check")
LOCATIONS = (".agents", ".codex", ".claude")
REQUIRED = ("SKILL.md", "references/indexnow.md", "agents/openai.yaml")


def version(skill: Path) -> tuple[int, int, int]:
    body = (skill / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = body.split("---", 2)
    if len(frontmatter) < 3 or frontmatter[0].strip():
        raise ValueError(f"Invalid SKILL.md frontmatter: {skill}")
    match = re.search(r'^\s*version:\s*["\']?(\d+)\.(\d+)\.(\d+)', frontmatter[1], re.M)
    if not match:
        raise ValueError(f"Missing semantic version: {skill}")
    return tuple(map(int, match.groups()))


def label(value: tuple[int, int, int]) -> str:
    return ".".join(map(str, value))


def same_tree(left: Path, right: Path) -> bool:
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    if any(not filecmp.cmp(left / name, right / name, shallow=False) for name in comparison.common_files):
        return False
    return all(same_tree(left / name, right / name) for name in comparison.common_dirs)


def replace_install(source: Path, destination: Path, backup_root: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    backup_root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = backup_root / f"{destination.parent.parent.name}-{stamp}"
    suffix = 1
    while backup.exists():
        backup = backup_root / f"{destination.parent.parent.name}-{stamp}-{suffix}"
        suffix += 1
    staged = Path(tempfile.mkdtemp(prefix=".launch-check-new-", dir=destination.parent))
    old = None
    try:
        shutil.rmtree(staged)
        shutil.copytree(source, staged)
        if destination.exists():
            shutil.copytree(destination, backup)
            old = Path(tempfile.mkdtemp(prefix=".launch-check-old-", dir=destination.parent))
            old.rmdir()
            destination.rename(old)
        try:
            staged.rename(destination)
        except Exception:
            if old is not None:
                old.rename(destination)
            raise
        if old is not None:
            shutil.rmtree(old)
        return backup
    finally:
        if staged.exists():
            shutil.rmtree(staged)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="install the newest version after checking")
    parser.add_argument("--home", type=Path, default=Path.home(), help=argparse.SUPPRESS)
    parser.add_argument("--source-dir", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    home = args.home.expanduser().resolve()

    with tempfile.TemporaryDirectory(prefix="launch-check-update-") as tmp:
        if args.source_dir:
            source = args.source_dir.resolve()
            commit = "local test source"
        else:
            checkout = Path(tmp) / "repo"
            subprocess.run(
                ["git", "clone", "--quiet", "--depth", "1", "--branch", "main", REPO, str(checkout)],
                check=True,
            )
            commit = subprocess.check_output(["git", "-C", str(checkout), "rev-parse", "--short", "HEAD"], text=True).strip()
            source = checkout / SKILL_PATH
        for relative in REQUIRED:
            if not (source / relative).is_file():
                raise ValueError(f"GitHub source is incomplete: missing {relative}")
        latest = version(source)
        print(f"GitHub launch-check: {label(latest)} ({commit})")

        destinations = [home / area / "skills" / "launch-check" for area in LOCATIONS]
        physical = set()
        for destination in destinations:
            if destination.is_symlink():
                print(f"{destination}: linked to {destination.resolve()}")
                continue
            if not destination.exists():
                print(f"{destination}: not installed")
                continue
            resolved = destination.resolve()
            if resolved in physical:
                continue
            physical.add(resolved)
            installed = version(destination)
            if installed > latest:
                print(f"{destination}: local version {label(installed)} is newer; kept")
            elif installed == latest:
                if same_tree(source, destination):
                    print(f"{destination}: current")
                else:
                    print(f"{destination}: same version, different files; kept for review")
            elif args.apply:
                backup = replace_install(source, destination, home / ".cache" / "launch-check" / "backups")
                print(f"{destination}: updated {label(installed)} → {label(latest)}; backup: {backup}")
            else:
                print(f"{destination}: update available {label(installed)} → {label(latest)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Update failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
