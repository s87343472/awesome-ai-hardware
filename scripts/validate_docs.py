#!/usr/bin/env python3
"""Validate bilingual Markdown coverage and documentation indexes."""

from __future__ import annotations

import sys
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git"}
CORE_DOCS = {
    "README.md": "README.zh-CN.md",
    "CONTRIBUTING.md": "CONTRIBUTING.zh-CN.md",
    "CODE_OF_CONDUCT.md": "CODE_OF_CONDUCT.zh-CN.md",
    "SECURITY.md": "SECURITY.zh-CN.md",
    "docs/REVIEW_GUIDE.md": "docs/REVIEW_GUIDE.zh-CN.md",
}
INDEXED_CORE_DOCS = {
    "../README.md",
    "../README.zh-CN.md",
    "../CONTRIBUTING.md",
    "../CONTRIBUTING.zh-CN.md",
    "REVIEW_GUIDE.md",
    "REVIEW_GUIDE.zh-CN.md",
    "../CODE_OF_CONDUCT.md",
    "../CODE_OF_CONDUCT.zh-CN.md",
    "../SECURITY.md",
    "../SECURITY.zh-CN.md",
    "../timeline/README.md",
    "../showcase/README.md",
    "../reviews/README.md",
}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []

    for english, chinese in CORE_DOCS.items():
        english_path = ROOT / english
        chinese_path = ROOT / chinese
        if not english_path.is_file():
            errors.append(f"Missing English document: {english}.")
            continue
        if not chinese_path.is_file():
            errors.append(f"Missing Simplified Chinese document: {chinese}.")
            continue
        chinese_name = Path(chinese).name
        if chinese_name not in read(english):
            errors.append(f"{english} does not link to {chinese_name}.")
        english_name = Path(english).name
        if english_name not in read(chinese):
            errors.append(f"{chinese} does not link to {english_name}.")

    for markdown in ROOT.rglob("*.md"):
        if any(part in IGNORED_PARTS for part in markdown.parts):
            continue
        relative = markdown.relative_to(ROOT).as_posix()
        if relative in CORE_DOCS or relative in CORE_DOCS.values():
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            local_target = (markdown.parent / unquote(target)).resolve()
            if not local_target.exists():
                errors.append(f"{relative} contains a broken local link: {raw_target}.")
        if "English" not in text or "简体中文" not in text:
            errors.append(
                f"{relative} must be bilingual in one file or have an explicit language switch."
            )

    docs_index = read("docs/README.md") if (ROOT / "docs/README.md").is_file() else ""
    for target in sorted(INDEXED_CORE_DOCS):
        if f"({target})" not in docs_index:
            errors.append(f"docs/README.md does not index {target}.")

    timeline_index = read("timeline/README.md") if (ROOT / "timeline/README.md").is_file() else ""
    if "(2026/README.md)" not in timeline_index:
        errors.append("timeline/README.md does not link the 2026 index.")
    year_index = read("timeline/2026/README.md") if (ROOT / "timeline/2026/README.md").is_file() else ""
    if "(08.md)" not in year_index:
        errors.append("timeline/2026/README.md does not link the August page.")
    review_index = read("reviews/README.md") if (ROOT / "reviews/README.md").is_file() else ""
    if "(2026-08-01-initial-batch.md)" not in review_index:
        errors.append("reviews/README.md does not link the initial batch review.")
    if "(2026-08-01-showcase-batch.md)" not in review_index:
        errors.append("reviews/README.md does not link the showcase batch review.")

    showcase_index = read("showcase/README.md") if (ROOT / "showcase/README.md").is_file() else ""
    for year in (2026, 2025):
        if f"({year}/README.md)" not in showcase_index:
            errors.append(f"showcase/README.md does not link the {year} index.")
    showcase_2026 = read("showcase/2026/README.md") if (ROOT / "showcase/2026/README.md").is_file() else ""
    for month in ("07", "06", "04"):
        if f"({month}.md)" not in showcase_2026:
            errors.append(f"showcase/2026/README.md does not link {month}.md.")
    showcase_2025 = read("showcase/2025/README.md") if (ROOT / "showcase/2025/README.md").is_file() else ""
    if "(07.md)" not in showcase_2025:
        errors.append("showcase/2025/README.md does not link 07.md.")

    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("Documentation validation failed:")
        for problem in problems:
            print(f"- {problem}")
        sys.exit(1)
    print("Documentation is bilingual and indexed.")
