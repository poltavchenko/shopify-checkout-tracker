import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
IMPORTER = ROOT / "scripts/import-heyapps.py"


def app(slug, **fields):
    return {
        "slug": slug,
        "name": slug.title(),
        "developer": "Example & Co",
        "delisted": "Oct 20, 2026",
        "launched": None,
        "source_url": "https://heyapps.dev/apps/" + slug,
        **fields,
    }


def capture(apps, count, view="delisted", sort="reviews", minute="24"):
    return {
        "source": "https://heyapps.dev/apps/delisted?" + (
            "view=recovered" if view == "recovered" else "sort=" + sort
        ),
        "captured_at": "2026-10-21T08:" + minute + ":00.000Z",
        "reported_count": count,
        "view": view,
        "apps": apps,
    }


class ImportHeyAppsTests(unittest.TestCase):
    def setUp(self):
        if not IMPORTER.is_file():
            self.fail("HeyApps importer is not implemented")
        spec = importlib.util.spec_from_file_location("import_heyapps", IMPORTER)
        self.importer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.importer)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.captures = [
            capture([app("privy"), app("duro_test")], 3),
            capture([app("duro_test"), app("third")], 3, sort="launched", minute="27"),
            capture([app("returned", recovered="Oct 21, 2026")], 1, "recovered", minute="25"),
        ]

    def write_captures(self):
        paths = []
        for index, data in enumerate(self.captures):
            path = self.directory / (str(index) + ".json")
            path.write_text(json.dumps(data), encoding="utf-8")
            paths.append(path)
        return paths

    def build(self):
        return self.importer.build_snapshot(self.write_captures())

    def test_overlapping_sorts_form_a_complete_unique_snapshot(self):
        paths = self.write_captures()
        data = self.importer.build_snapshot(paths)
        self.assertEqual(data["counts"], {"delisted": 3, "recovered": 1, "total": 4})
        self.assertEqual([a["slug"] for a in data["apps"]], ["duro_test", "privy", "third", "returned"])
        self.assertEqual(data["incident_ids"], {"privy": "privy"})
        self.assertEqual(data["checked"], "2026-10-21")
        self.assertEqual(data["captured_at"], "2026-10-21T08:27:00.000Z")
        self.assertEqual(data["capture_started_at"], "2026-10-21T08:24:00.000Z")
        self.assertIn("10:27:00", data["captured_local"])
        self.assertIn("Europe/Bratislava", data["captured_local"])
        self.assertEqual(data["sources"][0]["sha256"], hashlib.sha256(paths[0].read_bytes()).hexdigest())
        self.assertEqual(data["sources"][0]["captured_count"], 2)
        self.assertEqual(data, self.importer.build_snapshot(list(reversed(paths))))

    def test_partial_400_of_430_capture_is_rejected(self):
        self.captures[:2] = [capture([app("app-" + str(i)) for i in range(400)], 430)]
        with self.assertRaisesRegex(ValueError, "delisted.*400.*430"):
            self.build()

    def test_changed_record_across_sorts_is_rejected(self):
        self.captures[1]["apps"][0]["developer"] = "Another developer"
        with self.assertRaisesRegex(ValueError, "conflict.*duro_test"):
            self.build()

    def test_duplicate_within_one_capture_is_rejected(self):
        self.captures[0]["apps"].append(copy.deepcopy(self.captures[0]["apps"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate.*privy"):
            self.build()

    def test_reported_count_conflict_is_rejected(self):
        self.captures[1]["reported_count"] = 4
        with self.assertRaisesRegex(ValueError, "reported count"):
            self.build()

    def test_unsafe_app_and_capture_urls_are_rejected(self):
        for url in ["javascript:alert(1)", "https://heyapps.dev.evil.test/apps/privy", "https://heyapps.dev/apps/privy?x=1"]:
            with self.subTest(url=url):
                self.captures[0]["apps"][0]["source_url"] = url
                with self.assertRaisesRegex(ValueError, "source_url"):
                    self.build()
        self.captures[0]["apps"][0] = app("privy")
        self.captures[0]["source"] = "https://evil.test/apps/delisted"
        with self.assertRaisesRegex(ValueError, "capture source"):
            self.build()

    def test_invalid_dates_are_rejected(self):
        for field, value in [("delisted", "Feb 30, 2026"), ("delisted", None), ("launched", "2026-13-01")]:
            with self.subTest(field=field):
                original = self.captures[0]["apps"][0].copy()
                self.captures[0]["apps"][0][field] = value
                with self.assertRaisesRegex(ValueError, field):
                    self.build()
                self.captures[0]["apps"][0] = original

    def test_invalid_capture_shapes_and_timestamps_are_rejected(self):
        original = self.captures[0].copy()
        for field, value in [("apps", []), ("reported_count", True), ("view", "safe"), ("view", []), ("captured_at", "2026-10-21T08:00:00")]:
            with self.subTest(field=field):
                self.captures[0] = {**original, field: value}
                with self.assertRaises(ValueError):
                    self.build()

    def test_recovery_cannot_precede_delisting(self):
        self.captures[2]["apps"][0]["recovered"] = "Oct 19, 2026"
        with self.assertRaisesRegex(ValueError, "recovered.*before.*delisted"):
            self.build()

    def test_slug_must_be_safe_for_a_literal_html_id(self):
        self.captures[0]["apps"][0]["slug"] = 'privy" onclick="alert(1)'
        with self.assertRaisesRegex(ValueError, "slug"):
            self.build()

    def test_cross_state_duplicate_is_rejected(self):
        self.captures[2]["apps"][0] = app("privy", recovered="Oct 21, 2026")
        with self.assertRaisesRegex(ValueError, "both.*privy"):
            self.build()

    def test_missing_state_cannot_replace_the_complete_catalog(self):
        self.captures.pop()
        with self.assertRaisesRegex(ValueError, "recovered"):
            self.build()

    def test_injected_security_fields_are_dropped(self):
        self.captures[2]["apps"][0].update(status="ok", incident_id="rebuy", security="safe", links=[{"href": "javascript:alert(1)"}])
        data = self.build()
        returned = next(a for a in data["apps"] if a["slug"] == "returned")
        self.assertEqual(returned, {
            "slug": "returned", "name": "Returned", "developer": "Example & Co",
            "availability": "recovered", "delisted": "2026-10-20", "recovered": "2026-10-21",
            "launched": None, "source_url": "https://heyapps.dev/apps/returned",
        })
        self.assertNotIn("returned", data["incident_ids"])

    def test_failed_cli_does_not_overwrite_existing_output(self):
        self.captures[1]["reported_count"] = 430
        paths = self.write_captures()
        output = self.directory / "snapshot.json"
        output.write_text("preserve me", encoding="utf-8")
        run = subprocess.run([sys.executable, str(IMPORTER), "--output", str(output), *map(str, paths)], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("reported count", run.stderr)
        self.assertEqual(output.read_text(encoding="utf-8"), "preserve me")

    def test_cli_writes_the_validated_snapshot(self):
        paths = self.write_captures()
        output = self.directory / "snapshot.json"
        run = subprocess.run([sys.executable, str(IMPORTER), "--output", str(output), *map(str, paths)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.importer.build_snapshot(paths))


class PublishedSnapshotTests(unittest.TestCase):
    def test_full_snapshot_has_449_unique_apps_and_only_explicit_incident_matches(self):
        path = ROOT / "_data/heyapps.json"
        self.assertTrue(path.is_file(), "Full HeyApps snapshot is not generated")
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["counts"], {"delisted": 435, "recovered": 14, "total": 449})
        self.assertEqual(len(data["apps"]), 449)
        self.assertEqual(len({a["slug"] for a in data["apps"]}), 449)
        self.assertEqual(data["incident_ids"], {
            "product-options-by-hulkapps-1": "hulk-product-options", "upsell-cross-sell-kit-1": "selleasy",
            "swym-relay": "swym-wishlist-plus", "product-filter-search": "boost", "privy": "privy",
            "gdpr-backpack": "consentmo", "17track": "17track", "variant-swatch-king": "color-swatch-king",
            "rebuy": "rebuy", "product-network": "shopify-product-network",
        })
        curated = json.loads((ROOT / "_data/apps.json").read_text(encoding="utf-8"))["apps"]
        self.assertLessEqual(set(data["incident_ids"].values()), set(curated))
        self.assertEqual(len(data["sources"]), 4)
        self.assertTrue(all(set(a) == {"slug", "name", "developer", "availability", "delisted", "recovered", "launched", "source_url"} for a in data["apps"]))


if __name__ == "__main__":
    unittest.main()
