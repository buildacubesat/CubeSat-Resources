#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

BUTTONDOWN_ENDPOINT = "https://api.buttondown.email/v1/emails"

# Matches the footer block:
# ---
#
# [Subscribe ...](...)...
SUBSCRIBE_BLOCK_RE = re.compile(r"\n---\n\n\[Subscribe .*?\n?$", re.DOTALL)

NO_CHANGES_RE = re.compile(r"^\s*-\s*No changes\s*$", re.IGNORECASE | re.MULTILINE)


def sh(args: list[str]) -> str:
    return subprocess.check_output(args, text=True).strip()


def latest_update_file_in_repo() -> Path:
    candidates = sorted(UPDATES_DIR.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].md"))
    if not candidates:
        raise RuntimeError("No docs/updates/YYYY-MM.md files found in docs/updates.")
    return candidates[-1]

def strip_subscribe_footer(md: str) -> str:
    return re.sub(SUBSCRIBE_BLOCK_RE, "\n", md).rstrip() + "\n"


def title_from_markdown(md: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "CubeSat Resources"


def is_no_changes_month(md: str) -> bool:
    # If the file contains "- No changes" anywhere, treat it as no-changes month.
    # (That matches your template.)
    return bool(NO_CHANGES_RE.search(md))


def build_email_body(month_title: str, changelog_md: str) -> str:
    opener = (
        "Hi,\n\n"
        f"Here’s the CubeSat Resources changelog for **{month_title}**:\n\n"
    )

    closing = (
        "\n"
        "---\n\n"
        "Thanks for reading – and as always, if you spot something that should be added or fixed, "
        "just hit reply.\n"
        "\n"
        "Manuel\n"
    )

    return opener + changelog_md.strip() + closing


def post_buttondown_draft(subject: str, body_markdown: str) -> None:
    api_key = os.environ.get("BUTTONDOWN_API_KEY")
    if not api_key:
        raise RuntimeError("BUTTONDOWN_API_KEY env var not set.")

    payload = {
        "subject": subject,
        "body": body_markdown,
        "status": "draft",
    }

    req = urllib.request.Request(
        BUTTONDOWN_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Token {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as resp:
        print(resp.read().decode("utf-8"))


def main() -> None:
    update_file = latest_update_file_in_repo()
    raw = update_file.read_text(encoding="utf-8")

    if is_no_changes_month(raw):
        print(f"[buttondown] {update_file}: 'No changes' month → skipping draft.")
        return

    month_title = title_from_markdown(raw)
    subject = f"CubeSat Resources Changelog – {month_title}"

    cleaned = strip_subscribe_footer(raw)

    # Keep the changelog content as-is *except*:
    # - remove footer
    # - drop the H1, since subject already carries it, and we add our own intro line
    cleaned_lines = cleaned.splitlines()
    if cleaned_lines and cleaned_lines[0].startswith("# "):
        cleaned = "\n".join(cleaned_lines[1:]).lstrip()

    body = build_email_body(month_title, cleaned)

    print(f"[buttondown] Using changelog: {update_file}")
    print(f"[buttondown] Subject: {subject}")

    post_buttondown_draft(subject, body)
    print("[buttondown] Draft created.")


if __name__ == "__main__":
    main()
