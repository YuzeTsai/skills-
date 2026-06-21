#!/usr/bin/env python3
"""
fetch_school_info.py
Fetch grad school admissions data via Firecrawl API.

Usage:
    python scripts/fetch_school_info.py \
        --school "Columbia University" \
        --program "MS in Data Science" \
        --season "2027 Fall" \
        --field "data science"

Output: JSON to stdout.
Requires: FIRECRAWL_API_KEY environment variable.
"""

import argparse
import json
import os
import sys

import requests

API_KEY = os.environ.get("FIRECRAWL_API_KEY", "")
BASE = "https://api.firecrawl.dev/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
TIMEOUT = 30


def search(query: str) -> list[dict]:
    resp = requests.post(
        f"{BASE}/search",
        headers=HEADERS,
        json={"query": query, "limit": 3},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json().get("data", [])


def scrape(url: str) -> str:
    resp = requests.post(
        f"{BASE}/scrape",
        headers=HEADERS,
        json={"url": url, "formats": ["markdown"]},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json().get("data", {}).get("markdown", "")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--school", required=True)
    parser.add_argument("--program", required=True)
    parser.add_argument("--season", default="2027 Fall")
    parser.add_argument("--field", default="data science")
    args = parser.parse_args()

    out = {
        "school": args.school,
        "program": args.program,
        "source_url": None,
        "raw_content": None,
        "error": None,
    }

    if not API_KEY:
        out["error"] = "FIRECRAWL_API_KEY not set"
        print(json.dumps(out, ensure_ascii=False))
        sys.exit(1)

    try:
        query = f"{args.school} {args.program} {args.season} application admissions official"
        results = search(query)
        if not results:
            out["error"] = "No search results"
            print(json.dumps(out, ensure_ascii=False))
            return

        url = results[0].get("url", "")
        out["source_url"] = url

        if url:
            markdown = scrape(url)
            out["raw_content"] = markdown[:6000]  # cap to avoid token bloat

    except requests.RequestException as e:
        out["error"] = str(e)

    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
