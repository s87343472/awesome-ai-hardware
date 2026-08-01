#!/usr/bin/env python3
"""Validate structured X showcase data and its monthly pages."""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "showcases.json"
PROJECTS_FILE = ROOT / "data" / "projects.json"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
X_POST = re.compile(r"^https://x\.com/[^/]+/status/[0-9]+$")
CATEGORIES = {
    "smart-home-iot",
    "wearables",
    "voice-companions",
    "robotics",
    "edge-ai",
    "protocols-infrastructure",
    "creative-hardware",
}
RELATIONSHIPS = {"author", "project-team", "community"}
MEDIA_TYPES = {"image", "video", "thread"}
CATALOG_STATUSES = {"listed", "deferred", "showcase-only"}
REQUIRED = {
    "id",
    "title_en",
    "title_zh",
    "post_url",
    "post_author",
    "relationship",
    "published_at",
    "media_type",
    "media_url",
    "category",
    "catalog_status",
    "summary_en",
    "summary_zh",
    "linked_repos",
}
OPTIONAL = {"related_urls"}


def is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate() -> list[str]:
    errors: list[str] = []
    try:
        showcases = json.loads(DATA_FILE.read_text(encoding="utf-8")).get("showcases")
        projects = json.loads(PROJECTS_FILE.read_text(encoding="utf-8")).get("projects")
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot read showcase or project data: {exc}"]

    if not isinstance(showcases, list):
        return ["Top-level 'showcases' must be an array."]
    if not isinstance(projects, list):
        return ["Top-level project data is invalid."]

    listed_repos = {project.get("repo_url", "").rstrip("/").casefold() for project in projects}
    seen_ids: set[str] = set()
    seen_posts: set[str] = set()
    sort_keys: list[tuple[int, str]] = []

    for index, showcase in enumerate(showcases):
        label = f"showcases[{index}]"
        if not isinstance(showcase, dict):
            errors.append(f"{label} must be an object.")
            continue

        missing = REQUIRED - showcase.keys()
        unknown = showcase.keys() - REQUIRED - OPTIONAL
        if missing:
            errors.append(f"{label} missing: {', '.join(sorted(missing))}.")
        if unknown:
            errors.append(f"{label} has unknown fields: {', '.join(sorted(unknown))}.")

        showcase_id = showcase.get("id")
        if not isinstance(showcase_id, str) or not SLUG.fullmatch(showcase_id):
            errors.append(f"{label}.id must be a lowercase kebab-case slug.")
        elif showcase_id in seen_ids:
            errors.append(f"Duplicate showcase id: {showcase_id}.")
        else:
            seen_ids.add(showcase_id)

        for field in ("title_en", "title_zh", "post_author", "summary_en", "summary_zh"):
            value = showcase.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{field} must be a non-empty string.")

        post_url = showcase.get("post_url")
        if not isinstance(post_url, str) or not X_POST.fullmatch(post_url):
            errors.append(f"{label}.post_url must be a canonical X status URL.")
        elif post_url in seen_posts:
            errors.append(f"Duplicate X post: {post_url}.")
        else:
            seen_posts.add(post_url)

        if showcase.get("relationship") not in RELATIONSHIPS:
            errors.append(f"{label}.relationship is not recognized.")
        if showcase.get("media_type") not in MEDIA_TYPES:
            errors.append(f"{label}.media_type is not recognized.")
        if showcase.get("category") not in CATEGORIES:
            errors.append(f"{label}.category is not recognized.")
        if showcase.get("catalog_status") not in CATALOG_STATUSES:
            errors.append(f"{label}.catalog_status is not recognized.")
        if not is_http_url(showcase.get("media_url")):
            errors.append(f"{label}.media_url must be an HTTP(S) URL.")

        try:
            published = dt.date.fromisoformat(showcase.get("published_at", ""))
            if published > dt.date.today():
                errors.append(f"{label}.published_at cannot be in the future.")
            sort_keys.append((-published.toordinal(), str(showcase.get("title_en", "")).casefold()))
            monthly_file = ROOT / "showcase" / str(published.year) / f"{published.month:02d}.md"
            if not monthly_file.is_file():
                errors.append(f"{label} has no monthly showcase file: {monthly_file.relative_to(ROOT)}.")
            elif isinstance(post_url, str) and post_url not in monthly_file.read_text(encoding="utf-8"):
                errors.append(f"{label}.post_url is missing from {monthly_file.relative_to(ROOT)}.")
        except (TypeError, ValueError):
            errors.append(f"{label}.published_at must use YYYY-MM-DD.")

        linked_repos = showcase.get("linked_repos")
        if not isinstance(linked_repos, list):
            errors.append(f"{label}.linked_repos must be an array.")
            linked_repos = []
        elif len(linked_repos) != len(set(linked_repos)):
            errors.append(f"{label}.linked_repos contains duplicates.")
        for repo_url in linked_repos:
            parsed = urlparse(repo_url) if isinstance(repo_url, str) else None
            if not parsed or parsed.scheme != "https" or parsed.netloc.casefold() != "github.com":
                errors.append(f"{label}.linked_repos contains an invalid GitHub URL.")

        linked_normalized = {url.rstrip("/").casefold() for url in linked_repos if isinstance(url, str)}
        if showcase.get("catalog_status") == "listed" and not (linked_normalized & listed_repos):
            errors.append(f"{label} is marked listed but has no repository in projects.json.")

        related_urls = showcase.get("related_urls", [])
        if not isinstance(related_urls, list) or any(not is_http_url(url) for url in related_urls):
            errors.append(f"{label}.related_urls must be an array of HTTP(S) URLs.")
        elif len(related_urls) != len(set(related_urls)):
            errors.append(f"{label}.related_urls contains duplicates.")

    if sort_keys != sorted(sort_keys):
        errors.append("Showcases must be sorted by publication date descending, then English title.")

    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("Showcase data validation failed:")
        for problem in problems:
            print(f"- {problem}")
        sys.exit(1)
    print("Showcase data is valid and indexed.")
