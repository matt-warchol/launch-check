#!/usr/bin/env python3
"""Submit newly published or meaningfully updated sitemap URLs to IndexNow.

Run this after a successful production deployment. Persist --state between
deployments. The first run records a baseline unless --submit-initial is set.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import gzip
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
from urllib.robotparser import RobotFileParser

MAX_URLS_PER_POST = 10_000
TIMEOUT = 20


class PageHead(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonical: str | None = None
        self.noindex = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        if tag.lower() == "link" and "canonical" in values.get("rel", "").lower().split():
            self.canonical = values.get("href")
        if tag.lower() == "meta" and values.get("name", "").lower() in {"robots", "bingbot"}:
            directives = [item.strip() for item in values.get("content", "").lower().split(",")]
            if "noindex" in directives:
                self.noindex = True


def get(url: str) -> tuple[bytes, object]:
    req = Request(url, headers={"User-Agent": "launch-check-indexnow/1.0"})
    with urlopen(req, timeout=TIMEOUT) as response:
        return response.read(), response


def host_of(url: str) -> str:
    return (urlsplit(url).hostname or "").lower().rstrip(".")


def read_sitemap(url: str, expected_host: str, seen: set[str] | None = None, depth: int = 0) -> dict[str, str]:
    if depth > 5:
        raise ValueError("Sitemap index nesting exceeds five levels")
    seen = seen or set()
    if url in seen:
        return {}
    seen.add(url)
    body, response = get(url)
    if host_of(response.geturl()) != expected_host:
        raise ValueError("Sitemap URL redirected outside the submitted host")
    if urlsplit(url).path.lower().endswith(".gz") or response.headers.get("Content-Encoding", "").lower() == "gzip":
        body = gzip.decompress(body)
    try:
        root = ET.fromstring(body)
    except ET.ParseError as exc:
        raise ValueError(f"Invalid XML sitemap at {url}: {exc}") from exc
    kind = root.tag.rsplit("}", 1)[-1].lower()
    found: dict[str, str] = {}
    if kind not in {"urlset", "sitemapindex"}:
        raise ValueError(f"Expected urlset or sitemapindex at {url}")
    for node in root:
        loc = next((child.text.strip() for child in node if child.tag.rsplit("}", 1)[-1].lower() == "loc" and child.text), "")
        lastmod = next((child.text.strip() for child in node if child.tag.rsplit("}", 1)[-1].lower() == "lastmod" and child.text), "")
        if not loc:
            continue
        if kind == "sitemapindex":
            if host_of(loc) != expected_host:
                print(f"Skipped external sitemap URL: {loc}", file=sys.stderr)
                continue
            found.update(read_sitemap(loc, expected_host, seen, depth + 1))
        elif host_of(loc) == expected_host and urlsplit(loc).scheme in {"http", "https"}:
            found[loc] = lastmod
    return found


def load_state(path: Path, host: str) -> dict[str, str] | None:
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("host") != host or not isinstance(data.get("urls"), dict):
        raise ValueError("State file host/schema mismatch; inspect it before replacing it")
    return {str(url): str(meta.get("lastmod", "")) if isinstance(meta, dict) else "" for url, meta in data["urls"].items()}


def save_state(path: Path, host: str, urls: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps({"host": host, "urls": {u: {"lastmod": d} for u, d in sorted(urls.items())}}, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def robots_parser(origin: str) -> RobotFileParser:
    robots_url = urljoin(origin, "/robots.txt")
    parser = RobotFileParser(robots_url)
    try:
        body, _ = get(robots_url)
        parser.parse(body.decode("utf-8", errors="replace").splitlines())
    except HTTPError as exc:
        if exc.code == 404:
            parser.parse([])  # A missing robots.txt has no crawl restrictions.
        else:
            raise ValueError(f"Could not verify robots.txt (HTTP {exc.code})") from exc
    except (URLError, TimeoutError) as exc:
        raise ValueError(f"Could not verify robots.txt: {exc}") from exc
    return parser


def eligible(url: str, host: str, robots: RobotFileParser) -> tuple[bool, str]:
    if host_of(url) != host:
        return False, "different host"
    if urlsplit(url).scheme != "https":
        return False, "not HTTPS production URL"
    if not robots.can_fetch("bingbot", url):
        return False, "blocked for Bingbot by robots.txt"
    try:
        body, response = get(url)
    except (HTTPError, URLError, TimeoutError) as exc:
        return False, f"page fetch failed ({getattr(exc, 'code', 'network error')})"
    if response.status != 200 or response.geturl() != url:
        return False, "not a direct HTTP 200 canonical URL"
    headers = response.headers
    if "noindex" in headers.get("X-Robots-Tag", "").lower():
        return False, "X-Robots-Tag noindex"
    content_type = headers.get("Content-Type", "").lower()
    if "html" in content_type:
        page = PageHead()
        page.feed(body.decode("utf-8", errors="replace"))
        if page.noindex:
            return False, "meta robots noindex"
        if page.canonical and urljoin(url, page.canonical) != url:
            return False, "canonical points to another URL"
    return True, "eligible"


def verify_key(host: str, key: str, key_location: str) -> None:
    if not re.fullmatch(r"[A-Fa-f0-9-]{8,128}", key):
        raise ValueError("INDEXNOW_KEY must be 8–128 hexadecimal characters or hyphens")
    if host_of(key_location) != host or urlsplit(key_location).scheme != "https":
        raise ValueError("Key file must use HTTPS on the submitted host")
    body, response = get(key_location)
    if response.status != 200 or response.geturl() != key_location or body.decode("utf-8", errors="replace").strip() != key:
        raise ValueError("Public IndexNow key file is missing or its body does not match INDEXNOW_KEY")


def submit(host: str, key: str, key_location: str, urls: list[str]) -> dict[str, tuple[int, int]]:
    endpoint = "https://api.indexnow.org/indexnow"
    results: dict[str, tuple[int, int]] = {}
    for start in range(0, len(urls), MAX_URLS_PER_POST):
        batch = urls[start:start + MAX_URLS_PER_POST]
        payload = {"host": host, "key": key, "keyLocation": key_location, "urlList": batch}
        request = Request(endpoint, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
        for attempt in range(3):
            try:
                with urlopen(request, timeout=TIMEOUT) as response:
                    status = response.status
                break
            except HTTPError as exc:
                status = exc.code
                if status == 202:
                    break
                if status != 429 and status < 500:
                    raise RuntimeError(f"IndexNow rejected the batch with HTTP {status}") from exc
                if attempt == 2:
                    raise RuntimeError(f"IndexNow remained unavailable after retries (HTTP {status})") from exc
                time.sleep(2 ** attempt)
            except (URLError, TimeoutError) as exc:
                if attempt == 2:
                    raise RuntimeError(f"IndexNow request failed after retries: {exc}") from exc
                time.sleep(2 ** attempt)
        if status not in {200, 202}:
            raise RuntimeError(f"Unexpected IndexNow response: HTTP {status}")
        for url in batch:
            results[url] = (status, attempt + 1)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sitemap", required=True, help="Public production sitemap URL")
    parser.add_argument("--state", type=Path, default=Path(".launch-check/indexnow-state.json"), help="Persistent state file; preserve it between deployments")
    parser.add_argument("--submit-initial", action="store_true", help="Explicitly submit all current sitemap URLs on first run")
    parser.add_argument("--dry-run", action="store_true", help="Print new/lastmod-changed sitemap URLs without fetching pages or sending")
    args = parser.parse_args()
    sitemap = args.sitemap
    host = host_of(sitemap)
    if not host or (urlsplit(sitemap).scheme != "https" and not args.dry_run):
        raise ValueError("--sitemap must be an HTTPS production sitemap URL")
    current = read_sitemap(sitemap, host)
    if not current:
        raise ValueError("Sitemap contains no canonical URLs for its host")
    previous = load_state(args.state, host)
    if previous is None:
        if args.submit_initial:
            candidates = current
        else:
            save_state(args.state, host, current)
            print(f"Saved baseline for {len(current)} sitemap URLs; no URLs submitted. Persist the state file between deployments.")
            return 0
    else:
        candidates = {url: mod for url, mod in current.items() if url not in previous or (mod and mod != previous.get(url, ""))}
    if not candidates:
        save_state(args.state, host, current)
        print("No new or lastmod-updated sitemap URLs.")
        return 0
    if args.dry_run:
        print(f"Dry run: {len(candidates)} changed sitemap URLs found")
        for url in candidates:
            print(url)
        return 0

    robots = robots_parser(urlsplit(sitemap)._replace(path="/", query="", fragment="").geturl())
    valid: dict[str, str] = {}
    for url, lastmod in candidates.items():
        ok, reason = eligible(url, host, robots)
        if ok:
            valid[url] = lastmod
        else:
            print(f"Skipped {url}: {reason}", file=sys.stderr)
    if valid:
        key = os.environ.get("INDEXNOW_KEY", "")
        key_location = os.environ.get("INDEXNOW_KEY_LOCATION", f"https://{host}/{key}.txt" if key else "")
        if not key or not key_location:
            raise ValueError("Set INDEXNOW_KEY and optionally INDEXNOW_KEY_LOCATION in the deployment environment")
        verify_key(host, key, key_location)
        results = submit(host, key, key_location, list(valid))
        timestamp = datetime.now(timezone.utc).isoformat()
        for url, (status, attempts) in results.items():
            event = "initial" if previous is None else ("new" if url not in previous else "updated")
            print(f"{timestamp} event={event} http={status} attempts={attempts} url={url}")
        print(f"IndexNow accepted {len(valid)} eligible URL(s). This confirms receipt, not indexing.")
    merged = dict(current)
    # Keep failed candidates at their previous state so they are rechecked next deploy.
    for url in candidates.keys() - valid.keys():
        if previous is not None and url in previous:
            merged[url] = previous[url]
        else:
            merged.pop(url, None)
    save_state(args.state, host, merged)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"IndexNow submission failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
