#!/usr/bin/env python3
"""Minimal websearch -> content generation test.

Flow:
1) perform websearch (DuckDuckGo Instant Answer API)
2) persist normalized search results
3) generate markdown content derived from those results

This is intentionally small and easy to verify.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any, Dict, List

SEARCH_OUTPUT = "websearch-results.json"
GENERATED_OUTPUT = "generated-content.md"
FALLBACK_FIXTURE = "websearch-fixture.json"


def _flatten_related(related: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    items: List[Dict[str, str]] = []

    for entry in related:
        # Some entries have nested "Topics"
        if isinstance(entry, dict) and "Topics" in entry and isinstance(entry["Topics"], list):
            items.extend(_flatten_related(entry["Topics"]))
            continue

        text = (entry or {}).get("Text", "")
        url = (entry or {}).get("FirstURL", "")
        if text:
            items.append({"title": text, "url": url})

    return items


def perform_websearch(query: str, max_results: int = 5) -> Dict[str, Any]:
    # Primary source: DuckDuckGo Instant Answer API
    params = urllib.parse.urlencode(
        {
            "q": query,
            "format": "json",
            "no_redirect": "1",
            "no_html": "1",
            "skip_disambig": "1",
        }
    )
    ddg_url = f"https://api.duckduckgo.com/?{params}"

    request = urllib.request.Request(ddg_url, headers={"User-Agent": "Mozilla/5.0 (OpenClaw test)"})
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))

    candidates = _flatten_related(payload.get("RelatedTopics", []))

    # Fallback to abstract if related topics are empty
    if not candidates and payload.get("AbstractText"):
        candidates = [
            {
                "title": payload.get("AbstractText", "").strip(),
                "url": payload.get("AbstractURL", ""),
            }
        ]

    source = "DuckDuckGo Instant Answer API"

    # Secondary fallback: Wikipedia OpenSearch to keep test verifiable
    if not candidates:
        wiki_params = urllib.parse.urlencode(
            {
                "action": "opensearch",
                "search": query,
                "limit": str(max_results),
                "namespace": "0",
                "format": "json",
            }
        )
        wiki_url = f"https://en.wikipedia.org/w/api.php?{wiki_params}"
        wiki_request = urllib.request.Request(wiki_url, headers={"User-Agent": "Mozilla/5.0 (OpenClaw test)"})
        with urllib.request.urlopen(wiki_request, timeout=20) as response:
            wiki_payload = json.loads(response.read().decode("utf-8"))

        titles = wiki_payload[1] if len(wiki_payload) > 1 else []
        links = wiki_payload[3] if len(wiki_payload) > 3 else []
        for i, title in enumerate(titles[:max_results]):
            candidates.append({"title": title, "url": links[i] if i < len(links) else ""})

        source = "Wikipedia OpenSearch API (fallback)"

    results = candidates[:max_results]

    return {
        "query": query,
        "source": source,
        "fetchedAt": datetime.now(timezone.utc).isoformat(),
        "count": len(results),
        "results": results,
    }


def generate_content(search_data: Dict[str, Any]) -> str:
    query = search_data.get("query", "")
    source = search_data.get("source", "")
    fetched_at = search_data.get("fetchedAt", "")
    results = search_data.get("results", [])

    lines = [
        "# Generated Content from Websearch",
        "",
        f"- Query: `{query}`",
        f"- Source: {source}",
        f"- Fetched: {fetched_at}",
        "",
        "## Top Results",
        "",
    ]

    for idx, item in enumerate(results, start=1):
        title = item.get("title", "(no title)")
        url = item.get("url", "")
        lines.append(f"{idx}. {title}")
        if url:
            lines.append(f"   - {url}")

    lines.extend(
        [
            "",
            "## Derived Update",
            "",
            "This content was generated from live websearch results. "
            "If the results change, this file should change too.",
            "",
        ]
    )

    return "\n".join(lines)


def load_fixture_if_available() -> Dict[str, Any] | None:
    if not os.path.exists(FALLBACK_FIXTURE):
        return None
    with open(FALLBACK_FIXTURE, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a minimal websearch->generation test")
    parser.add_argument(
        "--query",
        default="CSS card layout best practices",
        help="Search query to run before generation",
    )
    args = parser.parse_args()

    try:
        search_data = perform_websearch(args.query)
    except Exception as exc:  # noqa: BLE001
        print(f"WARN: live websearch failed: {exc}", file=sys.stderr)
        search_data = {"query": args.query, "count": 0, "results": []}

    if search_data.get("count", 0) <= 0:
        fixture = load_fixture_if_available()
        if fixture and fixture.get("count", 0) > 0:
            search_data = fixture
            print(f"INFO: using fallback fixture: {FALLBACK_FIXTURE}")
        else:
            print("ERROR: websearch returned zero usable results and no fixture fallback available", file=sys.stderr)
            return 2

    with open(SEARCH_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(search_data, f, ensure_ascii=False, indent=2)

    generated = generate_content(search_data)
    with open(GENERATED_OUTPUT, "w", encoding="utf-8") as f:
        f.write(generated)

    print(f"OK: wrote {SEARCH_OUTPUT} and {GENERATED_OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
