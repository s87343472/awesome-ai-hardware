#!/usr/bin/env python3
"""Validate project data using only the Python standard library."""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "projects.json"
CATEGORIES = {
    "smart-home-iot",
    "wearables",
    "voice-companions",
    "robotics",
    "edge-ai",
    "protocols-infrastructure",
    "creative-hardware",
}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED = {
    "id",
    "name",
    "repo_url",
    "category",
    "description_zh",
    "ai_role",
    "hardware_role",
    "license",
    "last_verified",
    "tags",
}
OPTIONAL = {"description_en", "source_url", "demo_url"}


def is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate() -> list[str]:
    errors: list[str] = []
    try:
        document = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot read {DATA_FILE}: {exc}"]

    projects = document.get("projects")
    if not isinstance(projects, list):
        return ["Top-level 'projects' must be an array."]

    seen_ids: set[str] = set()
    seen_repos: set[str] = set()
    names: list[str] = []

    for index, project in enumerate(projects):
        label = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{label} must be an object.")
            continue

        missing = REQUIRED - project.keys()
        unknown = project.keys() - REQUIRED - OPTIONAL
        if missing:
            errors.append(f"{label} missing: {', '.join(sorted(missing))}.")
        if unknown:
            errors.append(f"{label} has unknown fields: {', '.join(sorted(unknown))}.")

        project_id = project.get("id")
        if not isinstance(project_id, str) or not SLUG.fullmatch(project_id):
            errors.append(f"{label}.id must be a lowercase kebab-case slug.")
        elif project_id in seen_ids:
            errors.append(f"Duplicate id: {project_id}.")
        else:
            seen_ids.add(project_id)

        name = project.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label}.name must be a non-empty string.")
        else:
            names.append(name.casefold())

        repo_url = project.get("repo_url")
        if not is_http_url(repo_url) or urlparse(repo_url).netloc.casefold() != "github.com":
            errors.append(f"{label}.repo_url must be a GitHub HTTPS URL.")
        elif repo_url.rstrip("/").casefold() in seen_repos:
            errors.append(f"Duplicate repository: {repo_url}.")
        else:
            seen_repos.add(repo_url.rstrip("/").casefold())

        if project.get("category") not in CATEGORIES:
            errors.append(f"{label}.category is not recognized.")

        for field in ("description_zh", "ai_role", "hardware_role", "license"):
            value = project.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{field} must be a non-empty string.")

        for field in ("source_url", "demo_url"):
            if field in project and not is_http_url(project[field]):
                errors.append(f"{label}.{field} must be an HTTP(S) URL.")

        try:
            verified = dt.date.fromisoformat(project.get("last_verified", ""))
            if verified > dt.date.today():
                errors.append(f"{label}.last_verified cannot be in the future.")
        except (TypeError, ValueError):
            errors.append(f"{label}.last_verified must use YYYY-MM-DD.")

        tags = project.get("tags")
        if not isinstance(tags, list) or any(not isinstance(tag, str) or not SLUG.fullmatch(tag) for tag in tags):
            errors.append(f"{label}.tags must be an array of lowercase kebab-case strings.")
        elif len(tags) != len(set(tags)):
            errors.append(f"{label}.tags contains duplicates.")

    if names != sorted(names):
        errors.append("Projects must be sorted alphabetically by name.")

    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("Project data validation failed:")
        for problem in problems:
            print(f"- {problem}")
        sys.exit(1)
    print("Project data is valid.")
