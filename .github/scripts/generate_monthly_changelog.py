#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

RE_FIX = re.compile(r"^(fix|fixes|fixed|fixing)\b", re.IGNORECASE)

DOCS_DIR = Path("docs")
UPDATES_DIR = DOCS_DIR / "updates"
MKDOCS_YML = Path("mkdocs.yml")

SUBSCRIBE_LINE = (
    "[Subscribe :material-open-in-new:](https://buttondown.com/buildacubesat#subscribe-form)"
    "{ target=_blank } to get a summary of changes once a month.\n"
)


@dataclass(frozen=True)
class CommitEntry:
    sha: str
    subject: str
    primary_url: str | None


def sh(args: list[str]) -> str:
    return subprocess.check_output(args, text=True).strip()


def month_range_utc(now_utc: datetime) -> tuple[datetime, datetime, str, str]:
    """Return [start, end) of previous month in UTC, plus YYYY-MM and 'Month YYYY'."""
    first_this_month = now_utc.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_prev_month = first_this_month - timedelta(days=1)
    first_prev_month = last_prev_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    yyyymm = f"{first_prev_month.year:04d}-{first_prev_month.month:02d}"
    title = first_prev_month.strftime("%B %Y")
    return first_prev_month, first_this_month, yyyymm, title


def read_site_url() -> str:
    # Tiny YAML parse (we only need site_url: ...)
    text = MKDOCS_YML.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("site_url:"):
            return line.split(":", 1)[1].strip()
    raise RuntimeError("site_url not found in mkdocs.yml")


def list_commits(start: datetime, end: datetime) -> list[tuple[str, str]]:
    # Old to new
    out = sh(
        [
            "git",
            "log",
            "--reverse",
            "--pretty=format:%H%x09%s",
            f"--since={start.isoformat()}",
            f"--until={end.isoformat()}",
        ]
    )
    if not out:
        return []
    rows: list[tuple[str, str]] = []
    for line in out.splitlines():
        sha, subject = line.split("\t", 1)
        rows.append((sha, subject.strip()))
    return rows


def changed_files(sha: str) -> list[str]:
    out = sh(["git", "show", "--name-only", "--pretty=format:", sha])
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def docs_url_for_path(site_url: str, path: str) -> str | None:
    # Only map docs/*.md (excluding updates)
    if not path.startswith("docs/") or not path.endswith(".md"):
        return None
    if path.startswith("docs/updates/"):
        return None

    rel = path[len("docs/") :]

    # Root index.md -> /
    if rel == "index.md":
        return site_url.rstrip("/") + "/"

    # .../index.md -> /.../
    if rel.endswith("/index.md"):
        rel_dir = rel[: -len("/index.md")]
        return site_url.rstrip("/") + "/" + rel_dir.strip("/") + "/"

    # foo/bar.md -> /foo/bar/
    rel_no_ext = rel[: -len(".md")]
    return site_url.rstrip("/") + "/" + rel_no_ext.strip("/") + "/"


def pick_primary_page_url(site_url: str, files: Iterable[str]) -> str | None:
    candidates: list[str] = []
    for f in files:
        if f.endswith(".md") and f.startswith("docs/") and not f.startswith("docs/updates/"):
            url = docs_url_for_path(site_url, f)
            if url:
                candidates.append(url)

    if not candidates:
        return None
    # If multiple, take the first (git show order). Good enough.
    return candidates[0]


def commit_url(repo_url: str, sha: str) -> str:
    return repo_url.rstrip("/") + "/commit/" + sha


def is_self_changelog_commit(files: list[str], target_relpath: str) -> bool:
    # Ignore commits that touch the file we’re about to generate
    return target_relpath in files


def render_entry(subject: str, url: str | None) -> str:
    if url:
        return f"- {subject} [↗]({url}){{ target=_blank }}\n"
    return f"- {subject}\n"


def main() -> None:
    now_utc = datetime.now(timezone.utc)
    start, end, yyyymm, title = month_range_utc(now_utc)

    site_url = read_site_url()

    # repo_url is present in mkdocs.yml; grab it similarly
    mk = MKDOCS_YML.read_text(encoding="utf-8")
    repo_url = None
    for line in mk.splitlines():
        if line.startswith("repo_url:"):
            repo_url = line.split(":", 1)[1].strip()
            break
    if not repo_url:
        raise RuntimeError("repo_url not found in mkdocs.yml")

    target_file = UPDATES_DIR / f"{yyyymm}.md"
    target_relpath = str(target_file.as_posix())

    commits = list_commits(start, end)

    entries: list[CommitEntry] = []
    for sha, subject in commits:
        files = changed_files(sha)

        # skip any commit that edits the target changelog file (avoid recursion)
        if is_self_changelog_commit(files, target_relpath):
            continue

        primary = pick_primary_page_url(site_url, files)
        if not primary:
            primary = commit_url(repo_url, sha)

        entries.append(CommitEntry(sha=sha, subject=subject, primary_url=primary))

    fixes: list[CommitEntry] = [e for e in entries if RE_FIX.match(e.subject)]
    changes: list[CommitEntry] = [e for e in entries if not RE_FIX.match(e.subject)]

    UPDATES_DIR.mkdir(parents=True, exist_ok=True)

    if not entries:
        # Exact template you requested
        content = (
            f"# {title}\n\n"
            "- No changes\n\n"
            "---\n\n"
            f"{SUBSCRIBE_LINE}"
        )
        target_file.write_text(content, encoding="utf-8")
        return

    parts: list[str] = [f"# {title}\n\n"]

    if changes:
        parts.append("## Changes\n\n")
        for e in changes:
            parts.append(render_entry(e.subject, e.primary_url))
        parts.append("\n")

    if fixes:
        parts.append("## Fixes\n\n")
        for e in fixes:
            parts.append(render_entry(e.subject, e.primary_url))
        parts.append("\n")

    parts.append("---\n\n")
    parts.append(SUBSCRIBE_LINE)

    target_file.write_text("".join(parts), encoding="utf-8")


if __name__ == "__main__":
    main()
