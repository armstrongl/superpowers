#!/usr/bin/env python3
"""Fetch latest reference content from official sources.

This script pulls current documentation from authoritative URLs and saves
them to the references/ directory. Run it before major skill revisions
or when reference content feels outdated.

Usage:
    python scripts/fetch_resources.py

Customization:
    Edit the SOURCES list below to point at the authoritative sources
    for your skill's domain. Each entry needs:
      - url: The source URL to fetch.
      - filename: Where to save in references/ (relative to skill root).
      - description (optional): What this source provides.

The script uses only Python stdlib (no dependencies to install).
"""

import os
import sys
import hashlib
import re
from html.parser import HTMLParser
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from pathlib import Path


# ===========================================================================
# CONFIGURE THESE SOURCES FOR YOUR SKILL
# ===========================================================================
SOURCES = [
    {
        "url": "https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows",
        "filename": "git-branching-workflows.md",
        "description": "Official Git documentation on branching workflows (long-running vs topic branches).",
    },
    {
        "url": "https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging",
        "filename": "git-basic-branching-and-merging.md",
        "description": "Official Git documentation on basic branching and merging mechanics.",
    },
    {
        "url": "https://docs.github.com/en/get-started/using-github/github-flow",
        "filename": "github-flow.md",
        "description": "GitHub Flow: the lightweight branch-based workflow used for PRs.",
    },
    {
        "url": "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github",
        "filename": "github-merge-methods.md",
        "description": "GitHub documentation on merge commit, squash, and rebase merge methods.",
    },
]
# ===========================================================================


class HTMLTextExtractor(HTMLParser):
    """Extract readable text from HTML, stripping tags and scripts."""

    def __init__(self):
        super().__init__()
        self._pieces = []
        self._skip_depth = 0
        self._skip_tags = {"script", "style", "nav", "footer", "header"}

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip_depth += 1
        if tag in ("p", "br", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr"):
            self._pieces.append("\n")
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self._pieces.append("#" * level + " ")

    def handle_endtag(self, tag):
        if tag in self._skip_tags and self._skip_depth > 0:
            self._skip_depth -= 1
        if tag in ("p", "div", "h1", "h2", "h3", "h4", "h5", "h6"):
            self._pieces.append("\n")

    def handle_data(self, data):
        if self._skip_depth == 0:
            self._pieces.append(data)

    def get_text(self):
        text = "".join(self._pieces)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def extract_text(html_content):
    """Extract readable text from HTML content."""
    parser = HTMLTextExtractor()
    parser.feed(html_content)
    return parser.get_text()


def file_hash(content):
    """Compute a hash of content for change detection."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]


def fetch_url(url):
    """Fetch a URL and return the response body as text."""
    req = Request(url, headers={"User-Agent": "fetch_resources/1.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main():
    script_dir = Path(__file__).resolve().parent
    skill_root = script_dir.parent
    references_dir = skill_root / "references"

    if not SOURCES:
        print("No sources configured. Edit the SOURCES list in this script.")
        print("See the comments at the top of the file for instructions.")
        sys.exit(0)

    results = {"fetched": [], "failed": [], "unchanged": [], "updated": []}

    for source in SOURCES:
        url = source["url"]
        filename = source["filename"]
        description = source.get("description", "")
        target_path = references_dir / filename

        print(f"Fetching: {url}")
        print(f"  -> {target_path}")

        try:
            raw_html = fetch_url(url)
            content = extract_text(raw_html)

            if not content.strip():
                print(f"  WARNING: Extracted content is empty. Skipping.")
                results["failed"].append({"url": url, "reason": "Empty content after extraction."})
                continue

            header = f"<!-- Source: {url} -->\n<!-- Fetched by fetch_resources.py -->\n\n"
            final_content = header + content

            target_path.parent.mkdir(parents=True, exist_ok=True)

            if target_path.exists():
                existing = target_path.read_text(encoding="utf-8")
                if file_hash(existing) == file_hash(final_content):
                    print(f"  No changes.")
                    results["unchanged"].append(url)
                    continue
                else:
                    print(f"  Updated (content changed).")
                    results["updated"].append(url)
            else:
                print(f"  New file.")
                results["fetched"].append(url)

            target_path.write_text(final_content, encoding="utf-8")

        except (URLError, HTTPError) as e:
            print(f"  FAILED: {e}")
            results["failed"].append({"url": url, "reason": str(e)})
        except Exception as e:
            print(f"  FAILED: {e}")
            results["failed"].append({"url": url, "reason": str(e)})

    print("\n--- Summary ---")
    print(f"New:       {len(results['fetched'])}")
    print(f"Updated:   {len(results['updated'])}")
    print(f"Unchanged: {len(results['unchanged'])}")
    print(f"Failed:    {len(results['failed'])}")

    if results["failed"]:
        print("\nFailed sources:")
        for f in results["failed"]:
            print(f"  {f['url']}: {f['reason']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
