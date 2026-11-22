"""Regressionsfälle für lückenlose Hauptskill-Fortschreibung, ohne Hash-Ausnahmen."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import main_skill_revisions as rev
import quality_lab as lab
from release_routing import RELEASE_BASE, plugin_asset_url


def put(root, path, data):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data if isinstance(data, bytes) else json.dumps(data).encode())
    return target


class RevisionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.relative = 'beispiel/skills/start/SKILL.md'
        self.path = put(self.root, self.relative, b'Neue konkrete Arbeitsfolge\n')
        self.old = b'Historisch gepruefte Fassung\n'
        self.archive = rev.ARCHIVE + self.relative + '.txt'
        put(self.root, self.archive, self.old)
        put(self.root, '.claude-plugin/marketplace.json', {'plugins': [{'name':'beispiel', 'source':'./beispiel'}]})
        put(self.root, 'scripts/data/werkstatt-visualisierung-profile.json', {'plugins': {'beispiel': {'entry_skills':['start']}}})
        self.reference = 'beispiel/references/hauptworkflow-und-rechtsprechung.md'
        self.refpath = put(self.root, self.reference, b'Beleg, Anwendung und Grenze\n')
        self.review_path = 'quality/hauptskills-2026-11-18/beispiel-review.json'
        self.review = {'plugin':'beispiel', 'path':self.relative,
                       'before_sha256':rev.digest(self.old), 'after_sha256':rev.digest(self.path.read_bytes()),
                       'changes':['Neue Tatsachen im Ergebnis fortschreiben.'],
                       'scenario':{'input':'Kaufvertrag', 'expected_result':'Ruecktrittsschreiben', 'new_information':'Teilzahlung'},
                       'review_method':'desk_review', 'source_scope':'Keine pauschale aktuelle Volltextprüfung.',
                       'reference':self.reference, 'reference_sha256':rev.digest(self.refpath.read_bytes())}
        self.reviewfile = put(self.root, self.review_path, [self.review])
        self.row = {k:self.review[k] for k in ('plugin','path','before_sha256','after_sha256')}
        self.row.update(archive=self.archive, review_path=self.review_path,
                        review_sha256=rev.digest(self.reviewfile.read_bytes()),
                        references={self.reference:rev.digest(self.refpath.read_bytes())})
        self.save_registry()

    def save_registry(self):
        put(self.root, rev.REGISTRY, {'schema_version':1, 'method':'main_workflow_revision','files':[self.row]})

    def test_valid_chain_and_historical_hash(self):
        self.assertEqual(rev.previous_bytes(self.root,self.path,plugin='beispiel'),self.old)
        self.assertEqual(rev.historical_bytes(self.root,self.path,rev.digest(self.old)),self.old)
        self.assertEqual(rev.validate_all(self.root),1)
        lab.validate_file_hashes({'plugin':'beispiel','skill_hashes':{self.relative:rev.digest(self.old)}},self.root)

    def test_unrelated_expected_hash_not_accepted(self):
        with self.assertRaises(lab.LabError):
            lab.validate_file_hashes({'plugin':'beispiel','skill_hashes':{self.relative:'0'*64}},self.root)

    def test_archive_tampering_rejected(self):
        (self.root/self.archive).write_bytes(b'Historie ersetzt')
        with self.assertRaises(ValueError): rev.previous_bytes(self.root,self.path)

    def test_new_skill_tampering_rejected(self):
        self.path.write_bytes(b'Ungepruefte weitere Aenderung')
        with self.assertRaises(lab.LabError):
            lab.validate_file_hashes({'plugin':'beispiel','skill_hashes':{self.relative:rev.digest(self.old)}},self.root)

    def test_reference_tampering_rejected(self):
        self.refpath.write_bytes(b'Ungepruefte Rechtsaussage')
        with self.assertRaises(ValueError): rev.validate_all(self.root)

    def test_review_tampering_rejected(self):
        self.reviewfile.write_bytes(b'[]')
        with self.assertRaises(ValueError): rev.validate_all(self.root)

    def test_missing_specific_scenario_rejected_even_with_updated_hash(self):
        self.review['scenario'].pop('new_information')
        put(self.root,self.review_path,[self.review])
        self.row['review_sha256']=rev.digest(self.reviewfile.read_bytes()); self.save_registry()
        with self.assertRaises(ValueError): rev.validate_all(self.root)

    def test_other_skill_not_whitelisted(self):
        put(self.root,'scripts/data/werkstatt-visualisierung-profile.json',{'plugins':{'beispiel':{'entry_skills':['anderer-start']}}})
        with self.assertRaises(ValueError): rev.validate_all(self.root)

    def test_other_plugin_rejected(self):
        with self.assertRaises(ValueError): rev.previous_bytes(self.root,self.path,plugin='fremd')

    def test_archive_escape_rejected(self):
        self.row['archive']='../archiv.txt'; self.save_registry()
        with self.assertRaises(ValueError): rev.validate_all(self.root)

    def test_unregistered_non_main_file_stays_hash_bound(self):
        other=put(self.root,'beispiel/testakten/akte.pdf',b'Altakte')
        old=rev.digest(other.read_bytes()); other.write_bytes(b'Neue Akte')
        self.assertEqual(rev.historical_bytes(self.root,other,old),b'Neue Akte')
        with self.assertRaises(lab.LabError):
            lab.validate_file_hashes({'plugin':'beispiel','artifact_hashes':{'beispiel/testakten/akte.pdf':old}},self.root)

    def test_completed_older_review_is_bound_to_archive_and_current_revision(self):
        previous = {"status":"needs_review", "reason":"Historisch offen", "files":[self.relative]}
        report = put(self.root,'quality/older/report.md',b'Historischer Sachbericht')
        record = {"schema_version":1,"method":"full_file_review","plugin":"beispiel",
                  "date":"2026-01-01","limits":"Früherer Dateistand, kein heutiger Live-Test.",
                  "previous_status":previous,
                  "files":[{"path":self.relative,"full_file_read":True,"result":"revised",
                            "checked_points":["Auftrag","Rechtsfolge"],"finding":"Historisch geprüft",
                            "before_sha256":"1"*64,"reviewed_sha256":rev.digest(self.old)}],
                  "reports":{"quality/older/report.md":rev.digest(report.read_bytes())}}
        evidence=put(self.root,'quality/older/evidence.json',record)
        review={**previous,"status":"reviewed","evidence":{"path":"quality/older/evidence.json",
                "sha256":rev.digest(evidence.read_bytes())}}
        profile={"plugin":"beispiel","file_review_status":review}
        self.assertEqual(lab.pending_file_reviews(profile,self.root),[])
        original=evidence.read_bytes()
        self.path.write_bytes(b'Ungepruefte Nachaenderung')
        with self.assertRaises(lab.LabError): lab.pending_file_reviews(profile,self.root)
        self.assertEqual(evidence.read_bytes(),original)

    def metadata_record(self, relative, old, new):
        path=put(self.root,relative,new)
        archive=rev.ARCHIVE+relative+'.txt'; put(self.root,archive,old)
        data=rev.load(self.root/rev.REGISTRY)
        data['integration_files']=[{'plugin':'beispiel','path':relative,'method':'release_metadata_only',
             'archive':archive,'before_sha256':rev.digest(old),'after_sha256':rev.digest(new)}]
        put(self.root,rev.REGISTRY,data)
        return path

    def test_metadata_only_own_download_link_is_allowed(self):
        old=b'# Anleitung\nhttps://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/alt-v1.0.0/beispiel.zip\n'
        new=old.replace(b'alt-v1.0.0',b'neu-v2.0.0')
        put(self.root,'scripts/scoped-release-assets.json',{'schema_version':1,'assets':{'beispiel.zip':'neu-v2.0.0'}})
        path=self.metadata_record('beispiel/README.md',old,new)
        self.assertEqual(rev.previous_bytes(self.root,path),old)
        path=self.metadata_record('beispiel/README.md',old,new.replace(b'Anleitung',b'Andere Rechtsaussage'))
        with self.assertRaisesRegex(ValueError,'mehr als eigene Paketlinks'):rev.previous_bytes(self.root,path)

    def test_readme_skill_cell_and_package_links_preserve_earlier_editions(self):
        package = "beispiel.zip"
        previous_tag = "komponente-v1.0.0"
        tag = "paketpflege-v1.0.0"
        old = (f"# Handbuch\n{RELEASE_BASE}/latest/download/{package}\n"
               "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->\n"
               "| [`start`](start.md) | Alter Ablauf | [MD herunterladen / Download MD](start.md) |\n"
               "| [`ende`](ende.md) | Abschluss | [MD herunterladen / Download MD](ende.md) |\n"
               "<!-- END SKILLS-OVERVIEW (auto-generated) -->\n").encode()
        previous = old.replace(b"latest/download", b"download/" + previous_tag.encode())
        revised = previous.replace(b"Alter Ablauf", b"Neuer Ablauf")
        published = revised.replace(previous_tag.encode(), tag.encode())
        path = self.metadata_record("beispiel/README.md", old, previous)
        registry = rev.load(self.root / rev.REGISTRY)
        row = registry["integration_files"][0]
        row["skill_overview_revision"] = {"skill": "start", "before_sha256": rev.digest(previous),
                                         "after_sha256": rev.digest(revised)}
        publication = {"previous_tag": previous_tag, "published_tag": tag, "after_sha256": rev.digest(published)}
        row["package_route_revision"] = publication
        put(self.root, rev.REGISTRY, registry)
        for active_tag, active_readme in ((previous_tag, revised), (tag, published)):
            put(self.root, "scripts/scoped-release-assets.json",
                {"schema_version": 1, "assets": {package: active_tag}})
            path.write_bytes(active_readme)
            for edition in (old, previous, revised, active_readme):
                self.assertEqual(rev.historical_bytes(self.root, path, rev.digest(edition), plugin="beispiel"), edition)
            path.write_bytes(published if active_readme == revised else revised)
            with self.assertRaisesRegex(ValueError, "aktiven Release"):
                rev.previous_bytes(self.root, path, plugin="beispiel")

        for word, replacement in ((b"Handbuch", b"Neue Rechtsfolge"), (b"Abschluss", b"Neuer Fachtext"),
                                  (b"(start.md)", b"(fremd.md)"), (tag.encode(), b"fremder-tag")):
            with self.subTest(word=word):
                wrong = published.replace(word, replacement)
                path.write_bytes(wrong)
                publication["after_sha256"] = rev.digest(wrong)
                row["skill_overview_revision"]["after_sha256"] = rev.digest(
                    wrong.replace(tag.encode(), previous_tag.encode()))
                put(self.root, rev.REGISTRY, registry)
                with self.assertRaises(ValueError):
                    rev.previous_bytes(self.root, path, plugin="beispiel")

    def test_reviewed_case_row_cannot_hide_unrelated_edits(self):
        slug = "erste-akte"
        base = "../testakten/" + slug
        relative = "beispiel/README.md"
        title = "Unsere Akte"
        put(self.root, f"testakten/{slug}/README.md", ("# " + title + "\n").encode())
        old = b"# Handbuch\n[2 zugeordnete Akten](#zugeordnete-testakten)\n"
        path = self.metadata_record(relative, old, old)
        version = "akten-v1.0.0"
        names = [f"testakte-{slug}{suffix}.zip" for suffix in ("", "-einzelpdfs")]
        put(self.root, "scripts/scoped-release-assets.json", {"schema_version": 1,
            "assets": {name: version for name in names}})
        cells = [f"[{title}]({base}/README.md)", f"[Gesamt-PDF]({base}/gesamt-pdf/{slug}_gesamt.pdf)"]
        url = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/" + version
        cells.extend(f"[`{name}`]({url}/{name})" for name in names)
        current = old.replace(b"[2 ", b"[3 ") + ("| " + " | ".join(cells) + " |\n").encode()
        record = rev.load(self.root / rev.REGISTRY)
        addition = {"slug": slug, "title": title, "previous_count": 2, "after_sha256": rev.digest(current)}
        record["integration_files"][0]["case_index_addition"] = addition
        put(self.root, rev.REGISTRY, record)
        path.write_bytes(current)
        self.assertEqual(rev.previous_bytes(self.root, path), old)
        unrelated = current.replace(b"Handbuch", b"Neue Rechtsaussage")
        path.write_bytes(unrelated)
        addition["after_sha256"] = rev.digest(unrelated)
        put(self.root, rev.REGISTRY, record)
        with self.assertRaises(ValueError):
            rev.previous_bytes(self.root, path)

        addition["after_sha256"] = rev.digest(current)
        updated_tag = "akten-v1.1.0"
        rerouted = current.replace(version.encode(), updated_tag.encode())
        addition["download_revision"] = {"previous_tag": version, "after_sha256": rev.digest(rerouted)}
        put(self.root, rev.REGISTRY, record)
        put(self.root, "scripts/scoped-release-assets.json", {"schema_version": 1,
            "assets": {name: updated_tag for name in names}})
        for content in (current, rerouted):
            path.write_bytes(content)
            self.assertEqual(rev.previous_bytes(self.root, path), old)
        path.write_bytes(rerouted.replace(b"Handbuch", b"Geaendert"))
        with self.assertRaises(ValueError):
            rev.previous_bytes(self.root, path)

    def test_followup_preserves_both_previous_editions_and_rejects_changed_text(self):
        relative = 'beispiel/README.md'
        url = b'https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/'
        old = b'# Anleitung\n' + url + b'alt-v1.0.0/beispiel.zip\n'
        prior = old.replace(b'alt-v1.0.0', b'mitte-v2.0.0')
        current = old.replace(b'alt-v1.0.0', b'neu-v3.0.0')
        path = self.metadata_record(relative, old, prior)
        archive = 'quality/paketnavigation-2026-11-19/bestand/' + relative + '.txt'
        saved = put(self.root, archive, prior)
        record = rev.load(self.root / rev.REGISTRY)
        followup = {'previous_archive': archive, 'after_sha256': rev.digest(current)}
        record['integration_files'][0]['publication_followup'] = followup
        put(self.root, rev.REGISTRY, record)
        put(self.root, 'scripts/scoped-release-assets.json', {'schema_version': 1, 'assets': {'beispiel.zip': 'neu-v3.0.0'}})
        path.write_bytes(current)
        for edition in (old, prior, current):
            self.assertEqual(rev.historical_bytes(self.root, path, rev.digest(edition)), edition)
        saved.write_bytes(old)
        with self.assertRaises(ValueError):
            rev.previous_bytes(self.root, path)
        saved.write_bytes(prior)
        wrong = current.replace(b'Anleitung', b'Geaenderte Rechtsaussage')
        path.write_bytes(wrong)
        followup['after_sha256'] = rev.digest(wrong)
        put(self.root, rev.REGISTRY, record)
        with self.assertRaisesRegex(ValueError, 'mehr als eigene Paketlinks'):
            rev.previous_bytes(self.root, path)

    def test_case_download_sections_preserve_all_original_bytes(self):
        from case_navigation_revision import CASES, EVIDENCE, previous_case_readme
        repository = Path(__file__).resolve().parents[1]
        evidence = rev.load(repository / EVIDENCE)
        put(self.root, EVIDENCE, evidence)
        for relative in CASES:
            with self.subTest(path=relative):
                content = (repository / relative).read_bytes()
                original = previous_case_readme(self.root, relative, content)
                self.assertEqual(rev.digest(original), evidence[relative]['before_sha256'])
                with self.assertRaises(ValueError):
                    previous_case_readme(self.root, relative, content + b'Anderer Sachverhalt')
        relative = sorted(CASES)[0]
        changed = (repository / relative).read_bytes().replace(b'Vollakte mit Originalbelegen', b'Andere rechtliche Folgerung', 1)
        evidence[relative]['after_sha256'] = rev.digest(changed)
        put(self.root, EVIDENCE, evidence)
        with self.assertRaises(ValueError):
            previous_case_readme(self.root, relative, changed)

    def test_fachaufnahme_requires_reviewed_old_and_new_text_and_correct_plugin(self):
        relative = "geldwaeschebeauftragter/skills/geldwaescheproblem-loesen/SKILL.md"
        old, new = b"Vorpruefung", b"Aktueller Quellenstand"
        path = put(self.root, relative, new)
        base = "quality/fachaufnahme-2026-11-21/"
        snapshot = put(self.root, base + "bestand/" + relative + ".txt", old)
        put(self.root, base + "fachtexte.json", {relative: {"vorher": rev.digest(old), "nachher": rev.digest(new)}})
        self.assertEqual(rev.before_fachaufnahme(self.root, path, new, plugin="geldwaeschebeauftragter"), old)
        for content, plugin in ((new + b"Zusatz", "geldwaeschebeauftragter"), (new, "aktenanleger")):
            with self.subTest(plugin=plugin, content=content), self.assertRaises(ValueError):
                rev.before_fachaufnahme(self.root, path, content, plugin=plugin)
        snapshot.write_bytes(b"Abweichende Vorfassung")
        with self.assertRaises(ValueError):
            rev.before_fachaufnahme(self.root, path, new)

    def test_pruefer_release_reconstructs_only_the_bound_file_and_publication(self):
        repository = Path(__file__).resolve().parents[1]
        base = Path("quality/pruefer-fortschreibung-2026-11-21")
        proof = put(self.root, base / "nachweis.json", (repository / base / "nachweis.json").read_bytes())
        snapshot = put(self.root, base / "vorfassungen.zip", (repository / base / "vorfassungen.zip").read_bytes())
        record = rev.load(proof)
        for name in ("arbeitszeugnispruefer/skills/azubi-zeugnis-analyse/FACHINHALT.md",
                     "bautraegervertrag-pruefer/skills/vertragssoll-bearbeiten/SKILL.md"):
            with self.subTest(name=name):
                body = (repository / name).read_bytes()
                path = put(self.root, name, body)
                expected = record["files"][name]["previous_sha256"]
                plugin = name.split("/")[0]
                self.assertEqual(rev.digest(rev.historical_bytes(self.root, path, expected, plugin=plugin)), expected)
                self.assertEqual(rev.historical_bytes(self.root, path, "0" * 64, plugin=plugin), body)
                with self.assertRaisesRegex(ValueError, "anderem Plugin"):
                    rev.historical_bytes(self.root, path, expected, plugin="fremde-pruefung")
                path.write_bytes(body + b"Abweichende fachliche Bewertung")
                with self.assertRaisesRegex(ValueError, "weicht vom veröffentlichten Prüferpaket ab"):
                    rev.historical_bytes(self.root, path, expected, plugin=plugin)
        path.write_bytes(body)
        snapshot.write_bytes(snapshot.read_bytes() + b"Nachtraegliche Veraenderung")
        with self.assertRaisesRegex(ValueError, "Archiv der Prüferfortschreibung verändert"):
            rev.historical_bytes(self.root, path, expected)
        record["archive_sha256"] = rev.digest(snapshot.read_bytes())
        put(self.root, proof, record)
        with self.assertRaisesRegex(ValueError, "Nachweis der Prüferfortschreibung verändert"):
            rev.historical_bytes(self.root, path, expected)

    def test_full_release_audit_rejects_rollback_or_lost_proof(self):
        repository = Path(__file__).resolve().parents[1]
        base = rev.PRUEFER_PROOF
        for name in ("nachweis.json", "vorfassungen.zip"):
            put(self.root, base / name, (repository / base / name).read_bytes())
        put(self.root, "scripts/data/rechtsprechung-pruefer-release.json",
            (repository / "scripts/data/rechtsprechung-pruefer-release.json").read_bytes())
        record = rev.pruefer_release_manifest(self.root)
        for name in record["files"]:
            put(self.root, name, (repository / name).read_bytes())
        self.assertEqual(rev.validate_all(self.root), 1)
        name = "bautraegervertrag-pruefer/skills/mabv-ratenplan-pruefen/FACHINHALT.md"
        path = self.root / name
        current = path.read_bytes()
        with rev.pruefer_release_archive(self.root, record) as archive:
            path.write_bytes(archive.read(name))
        with self.assertRaisesRegex(ValueError, "weicht vom veröffentlichten Prüferpaket ab"):
            rev.validate_all(self.root)
        path.write_bytes(current)
        (self.root / base).rename(self.root / "entfernter-nachweis")
        with self.assertRaises(FileNotFoundError):
            rev.validate_all(self.root)

    def test_catalog_growth_only_reverses_the_two_generated_counts(self):
        market = ".claude-plugin/marketplace.json"
        entries = [{"name": "beispiel", "source": "./beispiel"}]
        put(self.root, market, {"plugins": entries + [
            {"name": "allgemeines-notariat", "source": "./allgemeines-notariat"}]})
        put(self.root, "scripts/scoped-release-assets.json", {"schema_version": 1, "assets": {}})
        sentence = "Dieses Plugin gehört zum Marketplace mit 312 Plugins."
        old = ("# Beispiel\n<!-- BEGIN direkt-loslegen (autogen) -->\n## Was ist das hier?\n\n"
               + sentence + " Für die Installation nimm das Einzel-ZIP.\n"
               + "> Marketplace-Hinweis: " + sentence + " Das Sammelpaket steht bereit.\n"
               + "<!-- END direkt-loslegen (autogen) -->\n" + sentence + " Fachtext.\n").encode()
        new = old.replace(b"312 Plugins", b"313 Plugins", 2)
        path = self.metadata_record("beispiel/README.md", old, old)
        path.write_bytes(new)
        self.assertEqual(rev.previous_bytes(self.root, path, plugin="beispiel"), old)
        self.assertEqual(rev.historical_bytes(self.root, path, rev.digest(old), plugin="beispiel"), old)
        for changed in (new.replace(b"312 Plugins", b"313 Plugins"),
                        new.replace(b"Fachtext", b"Fachauftrag"),
                        new.replace(b"313 Plugins", b"314 Plugins"),
                        new.replace(b"313 Plugins", b"312 Plugins", 1)):
            with self.subTest(changed=changed):
                path.write_bytes(changed)
                with self.assertRaises(ValueError):
                    rev.historical_bytes(self.root, path, rev.digest(old), plugin="beispiel")
        catalog = rev.load(self.root / market)
        for name in ("aktenanleger", "umwandlungssteuerrecht"):
            catalog["plugins"].append({"name": name, "source": "./" + name})
        put(self.root, market, catalog)
        grown = old.replace(b"312 Plugins", b"315 Plugins", 2)
        path.write_bytes(grown)
        self.assertEqual(rev.previous_bytes(self.root, path, plugin="beispiel"), old)
        path.write_bytes(grown.replace(b"315 Plugins", b"316 Plugins", 1))
        with self.assertRaises(ValueError):
            rev.previous_bytes(self.root, path, plugin="beispiel")
        nested = put(self.root, "beispiel/references/README.md", new)
        self.assertEqual(rev.historical_bytes(self.root, nested, rev.digest(old)), new)
        put(self.root, market, {"plugins": entries})
        path.write_bytes(new)
        with self.assertRaises(ValueError):
            rev.previous_bytes(self.root, path, plugin="beispiel")

    def test_metadata_manifest_cannot_change_description(self):
        put(self.root,'.claude-plugin/marketplace.json',{'plugins':[{'name':'beispiel','source':'./beispiel','version':'2.0.0'}]})
        old=json.dumps({'name':'beispiel','version':'1.0.0','description':'Fachauftrag'}).encode()
        new=json.dumps({'name':'beispiel','version':'2.0.0','description':'Fachauftrag'}).encode()
        path=self.metadata_record('beispiel/.claude-plugin/plugin.json',old,new)
        self.assertEqual(rev.previous_bytes(self.root,path),old)
        path=self.metadata_record('beispiel/.claude-plugin/plugin.json',old,new.replace(b'Fachauftrag',b'Erweiterter Auftrag'))
        with self.assertRaisesRegex(ValueError,'mehr als die Paketversion'):rev.previous_bytes(self.root,path)

    def test_source_map_preserves_original_byte_reconstruction(self):
        spec=importlib.util.spec_from_file_location('consolidation',Path(__file__).with_name('consolidate-skill-cap.py'))
        module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        report={'files':[{'path':self.relative,'plugin':'beispiel','sha256':rev.digest(self.old),'original_sha256':rev.digest(self.old),'edits':[]}], 'plugins':[]}
        self.assertEqual(module.verify_source_map(self.root,report),[])
        report['files'][0]['original_sha256']='0'*64
        self.assertTrue(module.verify_source_map(self.root,report))

    def test_preview_links_reconstruct_the_original_source_map_files(self):
        repository = Path(__file__).resolve().parents[1]
        report = rev.load(repository / "quality/skill-consolidation/2026-11-14/source-map.json")
        for row in report["files"]:
            if not row["path"].endswith("/assets/vorschau/index.html"):
                continue
            with self.subTest(path=row["path"]):
                path = repository / row["path"]
                original = rev.historical_bytes(repository, path, row["sha256"])
                self.assertEqual(rev.digest(original), row["sha256"])
                self.assertEqual(rev.digest(original), row["original_sha256"])

    def test_diesel_directory_indexes_restore_only_their_bound_download_link(self):
        repository = Path(__file__).resolve().parents[1]
        name = "diesel-schadensersatz"
        tag = "paketpflege-v1.0.0"
        route = f"{RELEASE_BASE}/download/{tag}/{name}.zip".encode()
        put(self.root, "scripts/scoped-release-assets.json", {"schema_version": 1, "assets": {name + ".zip": tag}})
        for directory, expected in rev.DIESEL_INDEX_SHA256.items():
            relative = Path(name, directory, "README.md")
            source = (repository / relative).read_bytes()
            path = put(self.root, relative, source.replace(plugin_asset_url(name, root=repository).encode(), route))
            with self.subTest(directory=directory):
                original = rev.historical_bytes(self.root, path, expected, plugin=name)
                self.assertEqual(rev.digest(original), expected)
                path.write_bytes(path.read_bytes().replace(b"[Plugin-README]", b"[Fremdes Plugin]"))
                with self.assertRaisesRegex(ValueError, "weicht über den Paketlink hinaus"):
                    rev.historical_bytes(self.root, path, expected, plugin=name)
                path.write_bytes(original)
                self.assertEqual(rev.historical_bytes(self.root, path, expected, plugin=name), original)

    def test_preview_proof_rejects_other_edits_paths_plugins_and_hashes(self):
        repository = Path(__file__).resolve().parents[1]
        relative = "energierecht/assets/vorschau/index.html"
        package = "energierecht.zip"
        expected = rev.PREVIEW_ORIGINAL_SHA256["energierecht"]
        source = (repository / relative).read_bytes()
        source_url = plugin_asset_url("energierecht", root=repository).encode()
        latest = f"{RELEASE_BASE}/latest/download/{package}".encode()
        original = source.replace(source_url, latest)
        self.assertEqual(rev.digest(original), expected)

        tag = "energierecht-v2.0.0"
        routes = put(self.root, "scripts/scoped-release-assets.json",
                     {"schema_version": 1, "assets": {package: tag}})
        pinned = f"{RELEASE_BASE}/download/{tag}/{package}".encode()
        current = original.replace(latest, pinned)
        path = put(self.root, relative, current)
        self.assertEqual(rev.historical_bytes(self.root, path, expected), original)
        wrong_tag = current.replace(pinned, pinned.replace(tag.encode(), b"anderer-tag"))
        wrong_zip = current.replace(pinned, pinned.replace(package.encode(), b"umweltrecht.zip"))
        for altered in (current + b"Zusatz", current + current, wrong_tag, wrong_zip):
            with self.subTest(altered=rev.digest(altered)), self.assertRaises(ValueError):
                path.write_bytes(altered)
                rev.historical_bytes(self.root, path, expected)
        path.write_bytes(current)
        with self.assertRaisesRegex(ValueError, "anderen Plugin"):
            rev.historical_bytes(self.root, path, expected, plugin="umweltrecht")
        self.assertEqual(rev.historical_bytes(self.root, path, "0" * 64), current)
        for other in ("energierecht/references/index.html", "ungeprueft/assets/vorschau/index.html"):
            with self.subTest(path=other):
                self.assertEqual(rev.historical_bytes(self.root, put(self.root, other, current), expected), current)

        # Nach Aufhebung der komponentenspezifischen Zuordnung gilt der Sammelrelease.
        routes.write_text(json.dumps({"schema_version": 1, "assets": {}}), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "genau ein belegter Paketlink"):
            rev.historical_bytes(self.root, path, expected)
        path.write_bytes(original)
        self.assertEqual(rev.historical_bytes(self.root, path, expected), original)
        path.write_bytes(original + b"Zusatz")
        with self.assertRaisesRegex(ValueError, "weicht über den Paketlink hinaus"):
            rev.historical_bytes(self.root, path, expected)


if __name__=='__main__': unittest.main()
