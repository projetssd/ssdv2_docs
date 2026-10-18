#!/usr/bin/env python3
"""Audit internal links in the *rendered* MkDocs site before deploying GitHub Pages.

Checks all HTML pages and their <a href> links against actual generated paths.
External services/URLs are deliberately excluded from the local audit.
No documentation text is changed by this check.

Usage: python tools/check_internal_links.py site
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urljoin, urlsplit


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.values: list[tuple[int, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.values.append((self.getpos()[0], href))


def audit(site: Path, public_url: str) -> tuple[int, int, list[tuple[str, int, str, str]]]:
    base = public_url.rstrip("/") + "/"
    origin = urlsplit(base)
    prefix = origin.path
    html_files = sorted(site.rglob("*.html"))
    failures: list[tuple[str, int, str, str]] = []
    checked = 0

    for file in html_files:
        relative = file.relative_to(site).as_posix()
        current_url = urljoin(base, relative)
        parser = Links()
        parser.feed(file.read_text(encoding="utf-8"))
        for line, href in parser.values:
            if href.startswith(("javascript:", "mailto:", "tel:", "data:", "//")):
                continue
            absolute = urlsplit(urljoin(current_url, href))
            if absolute.hostname != origin.hostname:
                continue  # External URLs cannot be checked with generated files.
            if not unquote(absolute.path).startswith(prefix):
                failures.append((relative, line, href, "outside documentation base path"))
                continue

            checked += 1
            url_path = unquote(absolute.path)[len(prefix):]
            if not url_path:
                target = "index.html"
            elif url_path.endswith("/"):
                target = url_path + "index.html"
            else:
                target = url_path

            # MkDocs 'use_directory_urls' generates /slug/index.html; accepting
            # /slug (without slash) as well is consistent with Pages redirects.
            if not (site / target).is_file() and not Path(target).suffix:
                target = target.rstrip("/") + "/index.html"
            if not (site / target).is_file():
                failures.append((relative, line, href, f"missing output: {target}"))

    return len(html_files), checked, failures


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("site", type=Path, help="MkDocs output directory")
    cli.add_argument("--site-url", default="https://projetssd.github.io/ssdv2_docs/")
    args = cli.parse_args()
    if not args.site.is_dir():
        cli.error(f"Site output not found: {args.site}")
    pages, checked, failures = audit(args.site, args.site_url)
    print(f"Audited {pages} generated HTML pages and {checked} internal links.")
    if failures:
        print(f"FAIL: {len(failures)} broken internal link(s):")
        for page, line, href, reason in failures[:100]:
            print(f"  {page}:{line}: {href!r} -> {reason}")
        if len(failures) > 100:
            print(f"  ... and {len(failures) - 100} more.")
        return 1
    print("PASS: every internal link resolves to a generated file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
