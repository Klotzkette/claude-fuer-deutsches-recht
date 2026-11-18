import json
from pathlib import Path
import tempfile
import unittest
import package_link_revisions as R


class LinkRevisionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.put('.claude-plugin/marketplace.json',json.dumps({'plugins':[{'name':'demo','source':'./demo'}]}))
        self.target=self.put('references/zitierweise.md','Geprüfte Zitierweise')
        self.copy=self.put('demo/references/zitierweise.md','Geprüfte Zitierweise')
        self.relative='demo/skills/start/SKILL.md';self.old=b'# Auftrag\n\n[Quellen](../../../references/zitierweise.md)\n'
        self.path=self.put(self.relative,b'# Auftrag\n\n[Quellen](../../references/zitierweise.md)\n')
        self.row={'plugin':'demo','path':self.relative,'before_sha256':R.sha(self.old),'after_sha256':R.sha(self.path.read_bytes()),
                  'archive':R.ARCHIVE+self.relative+'.txt',
                  'replacements':[{'old':'../../../references/zitierweise.md','new':'../../references/zitierweise.md',
                    'target':'references/zitierweise.md','kind':'local_reference','copied_to':'demo/references/zitierweise.md',
                    'copied_sha256':R.sha(self.copy.read_bytes())}]}
        self.put(self.row['archive'],self.old);self.save()

    def put(self,path,data):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data.encode() if isinstance(data,str) else data);return p
    def save(self):self.put(R.MANIFEST,json.dumps({'files':[self.row]}))
    def test_verified_local_copy_and_link_only(self):self.assertEqual(R.previous_bytes(self.root,self.path),self.old)
    def test_unreviewed_body_change_even_with_current_hash_fails(self):
        self.path.write_bytes(self.path.read_bytes()+b'Neue Rechtsbehauptung')
        self.row['after_sha256']=R.sha(self.path.read_bytes());self.save()
        with self.assertRaises(ValueError):R.validate_all(self.root)
    def test_changed_copy_fails(self):
        self.copy.write_bytes(b'Abweichung')
        with self.assertRaises(ValueError):R.validate_all(self.root)
    def test_changed_copy_and_original_still_need_review(self):
        self.copy.write_bytes(b'Abweichung');self.target.write_bytes(b'Abweichung')
        with self.assertRaises(ValueError):R.validate_all(self.root)
    def test_alternate_destination_fails(self):
        self.row['replacements'][0]['new']='https://example.org/unrelated';self.save()
        with self.assertRaises(ValueError):R.validate_all(self.root)
    def test_archive_tampering_fails(self):
        self.put(self.row['archive'],'Andere frühere Quelle')
        with self.assertRaises(ValueError):R.validate_all(self.root)
    def test_outside_plugin_source_fails(self):
        self.row['plugin']='other';self.save()
        with self.assertRaises(ValueError):R.validate_all(self.root)
    def test_public_case_link_preserves_exact_target(self):
        self.put('testakten/demo/README.md','Fallakte')
        old=b'# Auftrag\n[Fall](../../../testakten/demo/README.md)\n'
        new=b'# Auftrag\n[Fall](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/demo/README.md)\n'
        self.row.update(before_sha256=R.sha(old),after_sha256=R.sha(new),replacements=[{'old':'../../../testakten/demo/README.md','new':R.WEB+'testakten/demo/README.md','target':'testakten/demo/README.md','kind':'public_repository'}])
        self.put(self.row['archive'],old);self.path.write_bytes(new);self.save()
        self.assertEqual(R.previous_bytes(self.root,self.path),old)

    def add_main_followup(self):
        import main_skill_revisions as M
        archive='quality/hauptskills-2026-11-18/paketlink-zwischenfassungen/'+self.relative+'.txt'
        self.put(archive,self.path.read_bytes())
        self.path.write_bytes(self.path.read_bytes().replace(b'# Auftrag',b'# Auftrag bearbeiten'))
        self.put('scripts/data/werkstatt-visualisierung-profile.json',json.dumps({'plugins':{'demo':{'entry_skills':['start']}}}))
        self.put(M.ARCHIVE+self.relative+'.txt',self.old)
        review={'plugin':'demo','path':self.relative,'before_sha256':R.sha(self.old),'after_sha256':R.sha(self.path.read_bytes()),
                'changes':['Arbeitsauftrag sprachlich präzisiert.'],'scenario':{'input':'Akte','expected_result':'Entwurf','new_information':'Nachtrag'},
                'source_scope':'Sprachprüfung, keine neue Rechtsrecherche.','review_method':'desk_review','inline_source_cards':True}
        review_path='quality/hauptskills-2026-11-18/demo-review.json';review_file=self.put(review_path,json.dumps([review]))
        record={k:review[k] for k in ('plugin','path','before_sha256','after_sha256')}
        record.update(archive=M.ARCHIVE+self.relative+'.txt',review_path=review_path,review_sha256=R.sha(review_file.read_bytes()),references={})
        self.put(M.REGISTRY,json.dumps({'schema_version':1,'method':'main_workflow_revision','files':[record]}))
        self.row['main_revision_followup']={'registry':M.REGISTRY,'archive':archive};self.save()
        return archive

    def test_reviewed_main_followup_keeps_link_replay_bound_to_intermediate_bytes(self):
        self.add_main_followup()
        self.assertEqual(R.previous_bytes(self.root,self.path),self.old)

    def test_main_followup_does_not_allow_unreviewed_current_body(self):
        self.add_main_followup();self.path.write_bytes(self.path.read_bytes()+b'Ungepruefte Aussage')
        with self.assertRaises(ValueError):R.validate_all(self.root)

    def test_main_followup_still_rejects_intermediate_archive_tampering(self):
        archive=self.add_main_followup();self.put(archive,b'Anderer Zwischentext')
        with self.assertRaises(ValueError):R.validate_all(self.root)

    def test_main_followup_cannot_whitelist_an_unregistered_skill(self):
        self.add_main_followup()
        self.put('scripts/data/werkstatt-visualisierung-profile.json',json.dumps({'plugins':{'demo':{'entry_skills':['anderer']}}}))
        with self.assertRaises(ValueError):R.validate_all(self.root)

if __name__=='__main__':unittest.main()
