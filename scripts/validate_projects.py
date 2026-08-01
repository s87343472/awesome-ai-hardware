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
    "added_at",
    "last_verified",
    "tags",
}
OPTIONAL = {
    "description_en",
    "discovered_at",
    "source_url",
    "demo_url",
    "resources",
}
RESOURCE_TYPES = {"image", "video", "demo", "article", "docs"}


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
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

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

        parsed_dates: dict[str, dt.date] = {}
        for field in ("added_at", "discovered_at", "last_verified"):
            if field not in project:
                continue
            try:
                parsed_dates[field] = dt.date.fromisoformat(project[field])
                if parsed_dates[field] > dt.date.today():
                    errors.append(f"{label}.{field} cannot be in the future.")
            except (TypeError, ValueError):
                errors.append(f"{label}.{field} must use YYYY-MM-DD.")

        if parsed_dates.get("last_verified", dt.date.min) < parsed_dates.get("added_at", dt.date.min):
            errors.append(f"{label}.last_verified cannot be earlier than added_at.")

        if isinstance(repo_url, str):
            if repo_url not in readme_en:
                errors.append(f"{label}.repo_url is missing from README.md.")
            if repo_url not in readme_zh:
                errors.append(f"{label}.repo_url is missing from README.zh-CN.md.")
            added_at = parsed_dates.get("added_at")
            if added_at:
                timeline_file = ROOT / "timeline" / str(added_at.year) / f"{added_at.month:02d}.md"
                if not timeline_file.is_file():
                    errors.append(f"{label} has no monthly timeline file: {timeline_file.relative_to(ROOT)}.")
                elif repo_url not in timeline_file.read_text(encoding="utf-8"):
                    errors.append(f"{label}.repo_url is missing from {timeline_file.relative_to(ROOT)}.")

        resources = project.get("resources", [])
        if not isinstance(resources, list):
            errors.append(f"{label}.resources must be an array.")
        else:
            resource_urls: set[str] = set()
            for resource_index, resource in enumerate(resources):
                resource_label = f"{label}.resources[{resource_index}]"
                if not isinstance(resource, dict):
                    errors.append(f"{resource_label} must be an object.")
                    continue
                if set(resource) != {"type", "title", "url"}:
                    errors.append(f"{resource_label} must contain only type, title, and url.")
                if resource.get("type") not in RESOURCE_TYPES:
                    errors.append(f"{resource_label}.type is not recognized.")
                if not isinstance(resource.get("title"), str) or not resource["title"].strip():
                    errors.append(f"{resource_label}.title must be a non-empty string.")
                if not is_http_url(resource.get("url")):
                    errors.append(f"{resource_label}.url must be an HTTP(S) URL.")
                elif resource["url"] in resource_urls:
                    errors.append(f"{resource_label}.url is duplicated in this project.")
                else:
                    resource_urls.add(resource["url"])

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
