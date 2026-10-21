import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser


ROOT = Path(__file__).resolve().parents[1]


class CatalogHTML(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.rows = {}
        self.row = None
        self.cell = None
        self.links = []
        self.scripts = []
        self.images = []
        self.text = ""
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "tr" and attrs.get("id", "").startswith("heyapps-"):
            self.row = {"cells": [], "buttons": [], "badges": []}
            self.rows[attrs["id"]] = self.row
        if self.row is not None:
            if tag == "td":
                self.row["cells"].append("")
                self.cell = len(self.row["cells"]) - 1
            if tag == "button":
                self.row["buttons"].append(attrs)
            if "badge" in attrs.get("class", "").split():
                self.row["badges"].append(attrs["class"])
        if tag == "link":
            self.links.append(attrs)
        if tag == "script":
            self.scripts.append(attrs)
        if tag == "img":
            self.images.append(attrs)

    def handle_endtag(self, tag):
        if tag == "tr":
            self.row = None
            self.cell = None
        if tag == "td":
            self.cell = None

    def handle_data(self, value):
        self.text += value
        if self.row is not None and self.cell is not None:
            self.row["cells"][self.cell] += value


class CatalogRenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = shlex.split(os.environ.get("JEKYLL_COMMAND", "jekyll"))
        if not shutil.which(command[0]):
            raise unittest.SkipTest("Set JEKYLL_COMMAND to run the real Jekyll rendering check")
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        source = Path(cls.temp.name).resolve() / "source"
        cls.destination = Path(cls.temp.name).resolve() / "site"
        shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns(".git", "_site", "__pycache__"))
        snapshot = source / "_data/heyapps.json"
        if not snapshot.is_file():
            raise AssertionError("HeyApps snapshot and catalog are not implemented")
        data = json.loads(snapshot.read_text(encoding="utf-8"))
        data["counts"]["delisted"] = 530
        cls.name = '<script id="injected">alert("name")</script> & App'
        cls.developer = '<img src=x onerror="alert(1)"> & Developer'
        for item in data["apps"]:
            if item["slug"] == "scarcity-ai-low-stock-counter":
                item.update(name=cls.name, developer=cls.developer, status="ok", incident_id="rebuy")
            if item["slug"] == "17track":
                item["status"] = "ok"
        snapshot.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        run = subprocess.run([*command, "build", "--source", str(source), "--destination", str(cls.destination), "--trace"], cwd=source, capture_output=True, text=True)
        if run.returncode:
            raise AssertionError(run.stdout + run.stderr)

    def test_catalog_escapes_source_text_and_keeps_incident_evidence_separate(self):
        for language in ["", "uk/"]:
            with self.subTest(language=language):
                path = self.destination / language / "apps/index.html"
                self.assertTrue(path.is_file(), "Localized catalog page is missing")
                page = CatalogHTML(path.read_text(encoding="utf-8"))
                self.assertEqual(len(page.rows), 450)
                row = page.rows["heyapps-scarcity-ai-low-stock-counter"]
                self.assertIn(self.name, row["cells"][0])
                self.assertIn(self.developer, row["cells"][0])
                self.assertEqual(len(row["cells"]), 5)
                self.assertEqual(row["buttons"], [])
                self.assertFalse(any("badge-ok" in badge or "badge-warn" in badge for badge in row["badges"]))
                self.assertIn("Інцидент не оцінювали" if language else "Incident not assessed", row["cells"][4])
                self.assertEqual(page.images, [])
                self.assertFalse(any(s.get("id") == "injected" for s in page.scripts))
                self.assertEqual([s["id"] for s in page.scripts if "id" in s], ["apps-data"])
                known = page.rows["heyapps-17track"]
                self.assertTrue(any("badge-warn" in badge for badge in known["badges"]))
                self.assertEqual([b.get("data-app") for b in known["buttons"]], ["17track"])
                buttons = [b["data-app"] for r in page.rows.values() for b in r["buttons"]]
                self.assertEqual(len(buttons), 10)

    def test_favicon_uses_baseurl_on_every_page_and_development_files_are_excluded(self):
        pages = ["index.html", "tracker/index.html", "apps/index.html", "faq/index.html", "checklist/index.html"]
        for language in ["", "uk/"]:
            for relative in pages:
                with self.subTest(page=language + relative):
                    page = CatalogHTML((self.destination / language / relative).read_text(encoding="utf-8"))
                    icons = [link for link in page.links if link.get("rel") == "icon"]
                    self.assertEqual(len(icons), 1)
                    self.assertEqual(icons[0]["href"], "/shopify-checkout-tracker/assets/favicon.svg")
                    self.assertEqual(icons[0]["type"], "image/svg+xml")
        self.assertTrue((self.destination / "assets/favicon.svg").is_file())
        self.assertFalse((self.destination / "scripts").exists())
        self.assertFalse((self.destination / "test").exists())

    def test_name_and_developer_remain_separate_search_words(self):
        for language in ["", "uk/"]:
            with self.subTest(language=language):
                page = CatalogHTML((self.destination / language / "apps/index.html").read_text(encoding="utf-8"))
                first_cell = page.rows["heyapps-script-test-app"]["cells"][0]
                self.assertIn("Boostatag Universali", " ".join(first_cell.split()))

    def test_faq_count_and_timestamp_come_from_the_catalog_snapshot(self):
        for language, sentence in [("", "HeyApps lists 530 delisted apps"), ("uk/", "HeyApps показує 530 знятих застосунків")]:
            with self.subTest(language=language):
                page = CatalogHTML((self.destination / language / "faq/index.html").read_text(encoding="utf-8"))
                self.assertIn(sentence, page.text)
                self.assertIn("2026-10-21 17:31:37", page.text)
                self.assertNotIn("429", page.text)


if __name__ == "__main__":
    unittest.main()
