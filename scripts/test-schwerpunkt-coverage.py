#!/usr/bin/env python3
"""Prüft die neuen Schwerpunktpakete, nicht ihre juristische Freigabe."""

from pathlib import Path
from copy import deepcopy
from hashlib import sha256
from html.parser import HTMLParser
import importlib.util
import re
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile
from urllib.parse import parse_qs, unquote, urlsplit

from markdown_it import MarkdownIt
from quality_lab import ROOT, LabError, load, marketplace, validate_focus_review, validate_profile


# Fachlich eigenständige Quellenregeln im Bestand vom 09.10.2026. Diese
# expliziten Dateistände sind keine neue juristische Vollprüfung. Änderungen
# benötigen einen gezielten Abgleich; unbekannte Abweichungen bleiben Fehler.
CURATED_CITATIONS = {
    "agb-werkstatt": ("references/arbeitsweise.md", "3187afd88f3b31e8774e70d4e5f941ec6420aa31e2666ddc8613f2aae97e1250"),
    "geldwaeschebeauftragter": ("references/zitierweise.md", "214a2330a21287e1dc54063c1ff3e12ec3382ea2fa40d3c65af29d86755ec288"),
    "ki-native-kanzlei": ("references/zitierweise.md", "de79fc80cb2e10433de15d0acd8d76ec1f0a6a66d4df7cbf6fdcadd550ffee58"),
    "ki-verordnung-hochrisiko-pruefer": ("references/zitierweise.md", "59fe8a74044008ea57ffc195581bed7ef3c9d7135efa491d7fd78de3b9f43b4f"),
    "ki-verordnung-konformitaet": ("references/zitierweise.md", "d436a5da95d1f36ac328bf84c0bd1129d72f605ad36b4bf0b68af2bbe345cb39"),
    "ki-verordnung-register-meldungen": ("references/zitierweise.md", "d436a5da95d1f36ac328bf84c0bd1129d72f605ad36b4bf0b68af2bbe345cb39"),
    "ki-verordnung-transparenzpruefer": ("references/zitierweise.md", "a395c1cc178c5b94f4d69da65eebc03ed5b4ed225e9a1c45bd12e50f26bcbadd"),
    "ki-verordnung-verbotene-praktiken": ("references/zitierweise.md", "eabc625a8ef872f2801bb0879a453105057435ab73897936368b29dcc1a268b0"),
}


def focus_skill(profile, name, directory, root=ROOT):
    target = profile.get("selection", {}).get("target_skill")
    validate_focus_review(profile.get("focus_review"), name, target, directory, root)
    return directory / "skills" / target / "SKILL.md"


def citation_reference(name, directory, skill, root=ROOT):
    relative, expected_hash = CURATED_CITATIONS.get(name, ("references/zitierweise.md", None))
    reference = directory / relative
    if not reference.is_file() or not reference.resolve().is_relative_to(directory.resolve()):
        raise AssertionError(f"{name}: lokale Zitierregel fehlt oder verlässt das Plugin: {relative}")
    if relative not in skill.read_text(encoding="utf-8"):
        raise AssertionError(f"{name}: Schwerpunkt verweist nicht auf {relative}")
    content = reference.read_bytes()
    if expected_hash is not None:
        if sha256(content).hexdigest() != expected_hash:
            raise AssertionError(f"{name}: kuratierte Zitierregel wurde verändert: {relative}")
    elif content != (root / "references/zitierweise.md").read_bytes():
        raise AssertionError(f"{name}: nicht registrierte Abweichung der Zitierregel")
    return reference


class DownloadLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.current = None
        self.elements = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        hidden = (any(value for _, value in self.elements) or tag in {"script", "style", "template"}
                  or "hidden" in attrs or attrs.get("aria-hidden") == "true"
                  or bool(re.search(r"(?:display\s*:\s*none|visibility\s*:\s*hidden)", attrs.get("style", ""), re.I)))
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.elements.append((tag, hidden))
        if tag == "a":
            self.current = None if hidden else [attrs.get("href", ""), ""]

    def handle_data(self, data):
        if self.current is not None:
            self.current[1] += data

    def handle_endtag(self, tag):
        if tag == "a" and self.current is not None:
            if self.current[1].strip():
                self.links.append(self.current[0])
            self.current = None
        for index in range(len(self.elements) - 1, -1, -1):
            if self.elements[index][0] == tag:
                del self.elements[index:]
                break


def require_focus_download(text, prompt, root=ROOT):
    if not prompt.is_file():
        raise AssertionError(f"Hauptproblemdatei fehlt: {prompt}")
    expected = prompt.relative_to(root).as_posix()
    parser = DownloadLinks()
    parser.feed(MarkdownIt().render(text))
    for target in parser.links:
        url = urlsplit(target)
        if (url.scheme == "https" and url.netloc == "klotzkette.github.io"
                and url.path == "/claude-fuer-deutsches-recht/download.html"
                and parse_qs(url.query) == {"path": [expected]} and not url.fragment):
            return
    raise AssertionError(f"Sichtbarer Direktdownload fehlt: {expected}")


def require_complete_markdown_bundle(bundle, name, directory):
    expected = {f"{name}/README.md": directory / "README.md"}
    for folder in (directory / "skills", directory / "references"):
        for source in folder.rglob("*.md"):
            if source.is_file():
                expected[f"{name}/{source.relative_to(directory).as_posix()}"] = source
    names = bundle.namelist()
    if len(names) != len(set(names)) or set(names) != set(expected):
        raise AssertionError(f"{name}: Markdown-Bundle hat fehlende, doppelte oder zusätzliche Dateien")
    for member, source in expected.items():
        if bundle.read(member) != source.read_bytes():
            raise AssertionError(f"{name}: Markdown-Bundle verändert {member}")


class SchwerpunktCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packages = {name: path for name, path in marketplace().items()
                        if name.startswith("fachanwalt-")
                        or name in {"insolvenzrecht", "steuerrecht-anwalt-und-berater", "zugewinnausgleich"}
                        or (path / f"{name}-hauptproblem.md").is_file()}

    def test_every_specialist_has_concrete_skill_and_prompt(self):
        self.assertTrue(self.packages)
        for name, directory in self.packages.items():
            with self.subTest(plugin=name):
                profile = load(ROOT / "quality/evals" / f"{name}.json")
                validate_profile(profile, name, directory)
                skill = focus_skill(profile, name, directory)
                self.assertGreater(len(skill.read_bytes()), 2500)
                prompt = directory / f"{name}-hauptproblem.md"
                raw = prompt.read_bytes()
                self.assertGreater(len(raw), 2500)
                self.assertLessEqual(len(raw), 7500)
                self.assertTrue(raw.decode("utf-8").startswith("# "))
                self.assertGreaterEqual(len(profile["sources"]), 1)

    def test_new_skill_relative_dependencies_stay_in_plugin(self):
        parser = MarkdownIt()
        for name, directory in self.packages.items():
            profile = load(ROOT / "quality/evals" / f"{name}.json")
            skill = focus_skill(profile, name, directory)
            for token in parser.parse(skill.read_text(encoding="utf-8")):
                for child in token.children or []:
                    if child.type != "link_open":
                        continue
                    destination = urlsplit(child.attrGet("href"))
                    if destination.scheme or not destination.path:
                        continue
                    with self.subTest(plugin=name, link=destination.path):
                        path = (skill.parent / unquote(destination.path)).resolve()
                        self.assertTrue(path.is_relative_to(directory.resolve()))
                        self.assertTrue(path.exists())

    def test_local_citation_reference_matches_declared_source(self):
        for name, directory in self.packages.items():
            with self.subTest(plugin=name):
                profile = load(ROOT / "quality/evals" / f"{name}.json")
                citation_reference(name, directory, focus_skill(profile, name, directory))

    def test_download_is_visible_in_each_readme(self):
        for name, directory in self.packages.items():
            with self.subTest(plugin=name):
                text = (directory / "README.md").read_text(encoding="utf-8")
                require_focus_download(text, directory / f"{name}-hauptproblem.md")

    def test_markdown_bundle_contains_all_skills_and_references_but_no_prompts(self):
        spec = importlib.util.spec_from_file_location("bundles", ROOT / "scripts/build-skills-markdown-bundles.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temporary:
            for name, directory in self.packages.items():
                with self.subTest(plugin=name):
                    archive, _ = module.build_plugin_bundle(
                        {"name": name, "source": str(directory.relative_to(ROOT))}, ROOT, Path(temporary))
                    with ZipFile(archive) as bundle:
                        require_complete_markdown_bundle(bundle, name, directory)
                        self.assertFalse(any(p.endswith(("-werkstatt.md", "-schnellstart.md", "-hauptproblem.md"))
                                             for p in bundle.namelist()))

    def test_release_requires_exact_installable_focus_skill(self):
        spec = importlib.util.spec_from_file_location("release_zips", ROOT / "scripts/validate-release-zips.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temporary:
            for name, directory in self.packages.items():
                profile_path = ROOT / "quality/evals" / f"{name}.json"
                target = load(profile_path)["selection"]["target_skill"]
                relative = f"skills/{target}/SKILL.md"
                archive_path = Path(temporary) / f"{name}.zip"
                for state in ("correct", "missing", "changed"):
                    with self.subTest(plugin=name, state=state):
                        with ZipFile(archive_path, "w") as archive:
                            if state != "missing":
                                archive.writestr(relative, (directory / relative).read_bytes()
                                                 if state == "correct" else b"Abweichender Text")
                        if state == "correct":
                            module.validate_focus_skill(archive_path, directory, profile_path)
                        else:
                            with patch.object(module, "fail", side_effect=ValueError), self.assertRaises(ValueError):
                                module.validate_focus_skill(archive_path, directory, profile_path)


class SchwerpunktContractRegressions(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.name = "schwerpunkt-probe"
        self.directory = self.root / self.name
        self.skill = self.directory / "skills/fall-steuern/SKILL.md"
        self.prompt = self.directory / f"{self.name}-hauptproblem.md"
        self.reference = self.directory / "references/zitierweise.md"
        for path, text in (
            (self.skill, "# Fall steuern\n\nVerwende references/zitierweise.md.\n"),
            (self.prompt, "# Hauptproblem\n\nBearbeite den konkreten Fall.\n"),
            (self.reference, "# Zitierweise\n\nGericht, Datum und gelesene Randnummer belegen.\n"),
            (self.root / "references/zitierweise.md", "# Zitierweise\n\nGericht, Datum und gelesene Randnummer belegen.\n"),
            (self.directory / "README.md", "# Schwerpunkt\n"),
        ):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        self.profile = {"selection": {"target_skill": "fall-steuern"},
                        "cases": [{"target_skill": "anderer-fachfall"}],
                        "focus_review": {"method": "desk_review", "reviewed_on": "2026-10-09",
                                         "verdict": "retained", "reason": "Gezielter Dateivertrag; kein Modelltest.",
                                         "changes": []}}
        for kind, source in (("skill", self.skill), ("prompt", self.prompt)):
            self.profile["focus_review"][f"{kind}_path"] = source.relative_to(self.root).as_posix()
            self.profile["focus_review"][f"{kind}_sha256"] = sha256(source.read_bytes()).hexdigest()

    def test_focus_comes_from_hash_bound_selection_not_first_case(self):
        self.assertEqual(focus_skill(self.profile, self.name, self.directory, self.root), self.skill)
        for state in ("wrong-target", "missing-review", "wrong-hash", "wrong-path"):
            profile = deepcopy(self.profile)
            if state == "wrong-target":
                profile["selection"]["target_skill"] = "anderer-fachfall"
            elif state == "missing-review":
                del profile["focus_review"]
            elif state == "wrong-hash":
                profile["focus_review"]["skill_sha256"] = "0" * 64
            else:
                profile["focus_review"]["skill_path"] = "anderes-plugin/skills/fall-steuern/SKILL.md"
            with self.subTest(state=state), self.assertRaises(LabError):
                focus_skill(profile, self.name, self.directory, self.root)

    def test_citation_contract_rejects_missing_unregistered_or_unused_reference(self):
        citation_reference(self.name, self.directory, self.skill, self.root)
        original = self.reference.read_bytes()
        self.reference.write_text("Ungeprüfte Ersatzregel\n")
        with self.assertRaises(AssertionError):
            citation_reference(self.name, self.directory, self.skill, self.root)
        self.reference.write_bytes(original)
        self.skill.write_text("# Kein Quellenverweis\n")
        with self.assertRaises(AssertionError):
            citation_reference(self.name, self.directory, self.skill, self.root)
        self.reference.unlink()
        with self.assertRaises(AssertionError):
            citation_reference(self.name, self.directory, self.skill, self.root)

    def test_curated_alternative_has_an_exact_path_and_content_contract(self):
        name = "agb-werkstatt"
        relative, _ = CURATED_CITATIONS[name]
        reference = self.directory / relative
        reference.write_bytes((ROOT / name / relative).read_bytes())
        self.skill.write_text(f"# Schwerpunkt\n\nZitierweise: {relative}.\n")
        self.assertEqual(citation_reference(name, self.directory, self.skill, self.root), reference)
        reference.write_bytes(reference.read_bytes() + b"\nUngepruefte Aenderung\n")
        with self.assertRaises(AssertionError):
            citation_reference(name, self.directory, self.skill, self.root)

    def test_download_requires_visible_link_to_exact_existing_prompt(self):
        url = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=" + self.prompt.relative_to(self.root).as_posix()
        for text in (f"[MD herunterladen]({url})", f'<a href="{url}" download>Hauptproblem als Markdown</a>'):
            require_focus_download(text, self.prompt, self.root)
        for text in (url, f"[MD]({url.replace('hauptproblem.md', 'werkstatt.md')})",
                     f"[MD]({url.replace('klotzkette.github.io', 'example.org')})",
                     f"[MD]({url}&path=anderes-plugin/falsch.md)", f'<!-- <a href="{url}">MD</a> -->',
                     f'```html\n<a href="{url}">MD</a>\n```', f'<a href="{url}"></a>',
                     f'<a hidden href="{url}">MD</a>', f'<div hidden><a href="{url}">MD</a></div>'):
            with self.subTest(text=text), self.assertRaises(AssertionError):
                require_focus_download(text, self.prompt, self.root)
        self.prompt.unlink()
        with self.assertRaises(AssertionError):
            require_focus_download(f"[MD]({url})", self.prompt, self.root)

    def test_bundle_rejects_missing_changed_or_extra_markdown(self):
        files = {f"{self.name}/{source.relative_to(self.directory).as_posix()}": source.read_bytes()
                 for source in (self.skill, self.reference, self.directory / "README.md")}
        archive = self.root / "probe.zip"
        for state in ("correct", "missing", "changed", "prompt-added"):
            payloads = dict(files)
            reference = f"{self.name}/references/zitierweise.md"
            if state == "missing":
                del payloads[reference]
            elif state == "changed":
                payloads[reference] = b"Abweichender Referenztext"
            elif state == "prompt-added":
                payloads[f"{self.name}/{self.prompt.name}"] = self.prompt.read_bytes()
            with ZipFile(archive, "w") as bundle:
                for name, content in payloads.items():
                    bundle.writestr(name, content)
            with self.subTest(state=state), ZipFile(archive) as bundle:
                if state == "correct":
                    require_complete_markdown_bundle(bundle, self.name, self.directory)
                else:
                    with self.assertRaises(AssertionError):
                        require_complete_markdown_bundle(bundle, self.name, self.directory)


if __name__ == "__main__":
    unittest.main()
