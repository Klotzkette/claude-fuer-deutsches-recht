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
