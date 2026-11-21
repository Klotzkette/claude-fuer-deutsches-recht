"""Regressionsfälle für lückenlose Hauptskill-Fortschreibung, ohne Hash-Ausnahmen."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import main_skill_revisions as rev
import quality_lab as lab


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


if __name__=='__main__': unittest.main()
