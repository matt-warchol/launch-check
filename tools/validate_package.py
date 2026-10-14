#!/usr/bin/env python3
"""Validate this release's metadata, local references, and portable file layout.

Author tooling only. Does not execute the skill or prove SEO effectiveness.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


def validate(root):
    errors = []
    skill = root / "skills/launch-check"
    required = ["SKILL.md", "agents/openai.yaml", "references/research.md",
                "references/audit.md", "references/footer.md",
                "references/technical-seo.md", "references/launch.md",
                "references/landing-page.md", "references/is-agentic.md", "references/indexnow.md",
                "references/google-analytics.md", "references/legal-pages.md",
                "assets/privacy-policy-template.md", "assets/terms-of-use-template.md",
                "assets/gdpr-notice-template.md",
                "assets/report-template.md", "scripts/update_from_github.py", "LICENSE-NOTICE.md"]
    for name in required:
        if not (skill / name).is_file():
            errors.append(f"Missing skill file: {name}")
    if errors:
        return errors

    # Reusable legal drafts must not carry the source company's identity.
    for name in ["privacy-policy-template.md", "terms-of-use-template.md", "gdpr-notice-template.md"]:
        draft = (skill / "assets" / name).read_text(encoding="utf-8").lower()
        if any(value in draft for value in ["brainhub", "6312663239", "364666949", "0000622336", "gliwice"]):
            errors.append(f"Source-company identity remains in legal template: {name}")

    content = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not match:
        return ["Missing or malformed frontmatter fences"]
    try:
        meta = yaml.safe_load(match.group(1))
        ui = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"Invalid YAML: {exc}"]
    if not isinstance(meta, dict) or not isinstance(ui, dict):
        return ["Metadata must be YAML mappings"]
    name = meta.get("name")
    if name != skill.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(name)) or len(str(name)) > 64:
        errors.append("Skill name must match the folder and naming specification")
    description = meta.get("description")
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        errors.append("Description must be a nonempty string of at most 1024 characters")
    metadata = meta.get("metadata", {})
    if not isinstance(metadata, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()):
        errors.append("Metadata keys and values must be strings")
    interface = ui.get("interface", {})
    if not isinstance(interface, dict):
        return errors + ["UI interface must be a mapping"]
    short = interface.get("short_description", "")
    if not isinstance(short, str) or not 25 <= len(short) <= 64:
        errors.append("UI short description must have 25–64 characters")
    prompt = interface.get("default_prompt", "")
    if not isinstance(prompt, str) or f"${name}" not in prompt:
        errors.append("Default prompt must mention the skill")
    if not isinstance(interface.get("display_name"), str) or not interface["display_name"].strip():
        errors.append("Missing UI display name")

    root = root.resolve()
    for path in root.rglob("*"):
        if path.is_symlink():
            errors.append(f"Symlink not allowed in release: {path.relative_to(root)}")
            continue
        if not path.is_file() or path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", text):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f"Broken or escaping local link in {path.relative_to(root)}: {target}")
            elif path.is_relative_to(skill) and not resolved.is_relative_to(skill):
                errors.append(f"Runtime skill link escapes standalone bundle: {target}")
    return errors


if __name__ == "__main__":
    problems = validate(Path(__file__).resolve().parents[1])
    for problem in problems:
        print(f"FAIL: {problem}")
    if not problems:
        print("PASS: metadata, required resources, relative links, and portable layout")
    sys.exit(bool(problems))
