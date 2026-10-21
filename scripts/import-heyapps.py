#!/usr/bin/env python3
"""Validate and merge offline HeyApps DOM captures into the public catalog."""

import argparse
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import parse_qs, urlsplit
from zoneinfo import ZoneInfo


INCIDENT_IDS = {
    "product-options-by-hulkapps-1": "hulk-product-options",
    "upsell-cross-sell-kit-1": "selleasy",
    "swym-relay": "swym-wishlist-plus",
    "product-filter-search": "boost",
    "privy": "privy",
    "gdpr-backpack": "consentmo",
    "17track": "17track",
    "variant-swatch-king": "color-swatch-king",
    "rebuy": "rebuy",
    "product-network": "shopify-product-network",
}


def parse_date(value, field, required=False):
    if value is None and not required:
        return None
    if not isinstance(value, str):
        raise ValueError("invalid " + field + " date")
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return date.fromisoformat(value).isoformat()
        match = re.fullmatch(r"([A-Z][a-z]{2}) (\d{1,2}), (\d{4})", value)
        months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
        if not match or match[1] not in months:
            raise ValueError()
        return date(int(match[3]), months.index(match[1]) + 1, int(match[2])).isoformat()
    except ValueError:
        raise ValueError("invalid " + field + " date: " + value) from None


def utc_timestamp(value):
    try:
        if not isinstance(value, str):
            raise ValueError()
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if stamp.tzinfo is None or stamp.utcoffset() is None:
            raise ValueError()
        return stamp.astimezone(timezone.utc)
    except ValueError:
        raise ValueError("captured_at must be an ISO timestamp with a time zone") from None


def format_timestamp(stamp):
    return stamp.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def normalize_app(raw, view):
    if not isinstance(raw, dict):
        raise ValueError("each app must be an object")
    slug = raw.get("slug")
    if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:[-_][a-z0-9]+)*", slug):
        raise ValueError("invalid app slug")
    if not isinstance(raw.get("name"), str) or not raw["name"].strip():
        raise ValueError("app name must be a nonempty string: " + slug)
    if "developer" not in raw or (raw["developer"] is not None and not isinstance(raw["developer"], str)):
        raise ValueError("developer must be a string or null: " + slug)
    if raw.get("source_url") != "https://heyapps.dev/apps/" + slug:
        raise ValueError("invalid app source_url: " + slug)
    if view == "delisted" and raw.get("recovered") is not None:
        raise ValueError("delisted app has a recovered date: " + slug)
    item = {
        "slug": slug,
        "name": raw["name"],
        "developer": raw["developer"],
        "availability": view,
        "delisted": parse_date(raw.get("delisted"), "delisted", required=True),
        "recovered": parse_date(raw.get("recovered"), "recovered", required=view == "recovered"),
        "launched": parse_date(raw.get("launched"), "launched"),
        "source_url": raw["source_url"],
    }
    if item["recovered"] is not None and item["recovered"] < item["delisted"]:
        raise ValueError("recovered date is before delisted date: " + slug)
    return item


def build_snapshot(paths):
    apps = {}
    counts = {}
    sources = []
    stamps = []
    for path in paths:
        content = Path(path).read_bytes()
        raw = json.loads(content)
        if not isinstance(raw, dict) or raw.get("view") not in ("delisted", "recovered"):
            raise ValueError("capture view must be delisted or recovered")
        view = raw["view"]
        source = raw.get("source")
        if not isinstance(source, str) or any(char.isspace() for char in source):
            raise ValueError("invalid capture source")
        url = urlsplit(source)
        if (url.scheme, url.netloc, url.path) != ("https", "heyapps.dev", "/apps/delisted") or url.fragment:
            raise ValueError("invalid capture source: " + source)
        if parse_qs(url.query, keep_blank_values=True).get("view", ["delisted"]) != [view]:
            raise ValueError("capture source does not match its view")
        count = raw.get("reported_count")
        if type(count) is not int or count < 1:
            raise ValueError("reported count must be a positive integer")
        if view in counts and counts[view] != count:
            raise ValueError("conflicting reported counts for " + view)
        counts[view] = count
        records = raw.get("apps")
        if not isinstance(records, list) or not records:
            raise ValueError("capture apps must be a nonempty array")
        stamp = utc_timestamp(raw.get("captured_at"))
        stamps.append(stamp)
        seen = set()
        for record in records:
            item = normalize_app(record, view)
            slug = item["slug"]
            if slug in seen:
                raise ValueError("duplicate app within capture: " + slug)
            seen.add(slug)
            if slug in apps:
                if apps[slug]["availability"] != view:
                    raise ValueError("app appears in both availability states: " + slug)
                if apps[slug] != item:
                    raise ValueError("conflicting app records: " + slug)
            apps[slug] = item
        sources.append({
            "url": source,
            "captured_at": format_timestamp(stamp),
            "view": view,
            "reported_count": count,
            "captured_count": len(records),
            "sha256": hashlib.sha256(content).hexdigest(),
        })
    for view in ("delisted", "recovered"):
        if view not in counts:
            raise ValueError("missing " + view + " capture")
        actual = sum(app["availability"] == view for app in apps.values())
        if actual != counts[view]:
            raise ValueError(view + " unique count " + str(actual) + " does not match reported count " + str(counts[view]))
    incident_ids = {slug: INCIDENT_IDS[slug] for slug in sorted(INCIDENT_IDS) if slug in apps}
    curated_path = Path(__file__).resolve().parents[1] / "_data/apps.json"
    curated = json.loads(curated_path.read_text(encoding="utf-8"))["apps"]
    if not set(incident_ids.values()) <= set(curated):
        raise ValueError("incident crosswalk target is missing from curated apps")
    latest = max(stamps)
    local = latest.astimezone(ZoneInfo("Europe/Bratislava"))
    offset = local.strftime("%z")
    return {
        "checked": latest.date().isoformat(),
        "captured_at": format_timestamp(latest),
        "capture_started_at": format_timestamp(min(stamps)),
        "captured_local": local.strftime("%Y-%m-%d %H:%M:%S") + " (Europe/Bratislava, UTC" + offset[:3] + ":" + offset[3:] + ")",
        "counts": {"delisted": counts["delisted"], "recovered": counts["recovered"], "total": len(apps)},
        "sources": sorted(sources, key=lambda source: (source["captured_at"], source["url"], source["sha256"])),
        "incident_ids": incident_ids,
        "apps": sorted(apps.values(), key=lambda app: (app["availability"], app["name"].casefold(), app["slug"])),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("captures", nargs="+", type=Path)
    args = parser.parse_args()
    temporary = None
    try:
        snapshot = build_snapshot(args.captures)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=args.output.parent, delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(snapshot, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        temporary.replace(args.output)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
