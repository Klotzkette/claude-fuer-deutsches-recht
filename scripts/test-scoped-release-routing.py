"""Component releases must not silently redirect unrelated downloads."""
import json,tempfile,unittest
from pathlib import Path
import release_routing as R

class ScopedRouting(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/'scripts').mkdir();(self.root/'.claude-plugin').mkdir()
        (self.root/'.claude-plugin/marketplace.json').write_text(json.dumps({'version':'777.1.0'}))
        self.config=self.root/'scripts/release-routes.json'
        self.config.write_text(json.dumps({'schema_version':1,'companion_case_slugs':['case-one','case-two']}))
        self.pins=self.root/'scripts/scoped-release-assets.json'
        self.pins.write_text(json.dumps({'schema_version':1,'assets':{'new-plugin.zip':'new-plugin-v777.1.0','testakte-case-one.zip':'new-plugin-v777.1.0','testakte-case-one-einzelpdfs.zip':'new-plugin-v777.1.0'}}))
    def test_precise_asset_pin_and_default(self):
        self.assertIn('/download/new-plugin-v777.1.0/',R.plugin_asset_url('new-plugin',root=self.root))
        self.assertIn('/latest/download/',R.plugin_asset_url('old-plugin',root=self.root))
        self.assertIn('/download/new-plugin-v777.1.0/',R.case_asset_url('case-one',root=self.root,config=self.config))
        self.assertIn('/download/akten-v777.1.0/',R.case_asset_url('case-two',root=self.root,config=self.config))
    def test_rewrite_both_variants_is_idempotent(self):
        text='\n'.join(f'{R.RELEASE_BASE}/latest/download/testakte-case-one{s}.zip' for s in ('','-einzelpdfs'))
        actual=R.rewrite_case_asset_urls(text,root=self.root,config=self.config)
        self.assertEqual(actual.count('/download/new-plugin-v777.1.0/'),2)
        self.assertEqual(actual,R.rewrite_case_asset_urls(actual,root=self.root,config=self.config))
    def test_invalid_pin_fails(self):
        self.pins.write_text(json.dumps({'schema_version':1,'assets':{'new-plugin.zip':'../../bad'}}))
        with self.assertRaises(ValueError):R.plugin_asset_url('new-plugin',root=self.root)
    def test_absent_config_preserves_default(self):
        self.pins.unlink()
        self.assertIn('/latest/download/',R.plugin_asset_url('new-plugin',root=self.root))
        self.assertIn('/download/akten-v777.1.0/',R.case_asset_url('case-one',root=self.root,config=self.config))
    def test_component_version_requires_exact_pin(self):
        entry = {'name': 'new-plugin', 'version': '777.1.0'}
        self.assertIsNone(R.validate_plugin_version(entry, '777.0.0', root=self.root))
        with self.assertRaises(ValueError):
            R.validate_plugin_version({**entry, 'version': '777.1.1'}, '777.0.0', root=self.root)
        with self.assertRaises(ValueError):
            R.validate_plugin_version({**entry, 'name': 'other-plugin'}, '777.0.0', root=self.root)
    def test_global_version_and_invalid_version(self):
        self.assertIsNone(R.validate_plugin_version({'name': 'old-plugin', 'version': '777.1.0'}, '777.1.0', root=self.root))
        with self.assertRaises(ValueError):
            R.validate_plugin_version({'name': 'old-plugin', 'version': '777.1'}, '777.1.0', root=self.root)

    def bundle_proof(self):
        tag = 'bundle-v777.2.0'
        asset = 'new-plugin.zip'
        self.pins.write_text(json.dumps({'schema_version': 1, 'assets': {asset: tag}}))
        self.registry = self.root / 'scripts/scoped-release-package-versions.json'
        self.evidence = self.root / 'quality/bundle/pakete.json'
        self.evidence.parent.mkdir(parents=True)
        self.record = {'tag': tag, 'version': '777.1.0', 'sha256': 'a' * 64,
                       'evidence': 'quality/bundle/pakete.json'}
        self.proof = {'release': tag, 'version': '777.1.0', 'plugins': [{'name': 'new-plugin'}],
                      'assets': {asset: 'a' * 64}}
        self.registry.write_text(json.dumps({'schema_version': 1, 'assets': {asset: self.record}}))
        self.evidence.write_text(json.dumps(self.proof))
        return {'name': 'new-plugin', 'version': '777.1.0'}

    def test_differing_bundle_tag_requires_exact_package_evidence(self):
        plugin = self.bundle_proof()
        self.assertIsNone(R.validate_plugin_version(plugin, '777.3.0', root=self.root))
        for changed in ({**plugin, 'name': 'other-plugin'}, {**plugin, 'version': '777.1.1'}):
            with self.subTest(plugin=changed), self.assertRaises(ValueError):
                R.validate_plugin_version(changed, '777.3.0', root=self.root)
        self.pins.write_text(json.dumps({'schema_version': 1, 'assets': {'new-plugin.zip': 'other-v777.2.0'}}))
        with self.assertRaises(ValueError):
            R.validate_plugin_version(plugin, '777.3.0', root=self.root)

    def test_mismatched_evidence_never_authorizes_package_version(self):
        plugin = self.bundle_proof()
        for field, value in (('release', 'other-v777.2.0'), ('version', '777.1.1'),
                             ('assets', {'new-plugin.zip': 'b' * 64}),
                             ('assets', {'other-plugin.zip': 'a' * 64}),
                             ('plugins', [{'name': 'other-plugin'}]), ('plugins', None)):
            self.evidence.write_text(json.dumps({**self.proof, field: value}))
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                R.validate_plugin_version(plugin, '777.3.0', root=self.root)

    def test_missing_or_invalid_proof_registry_fails_closed(self):
        plugin = self.bundle_proof()
        for data in ({'schema_version': 2, 'assets': {}}, {'schema_version': 1, 'assets': []},
                     {'schema_version': 1, 'assets': {'new-plugin.zip': {}}},
                     {'schema_version': 1, 'assets': {'other-plugin.zip': self.record}}):
            self.registry.write_text(json.dumps(data))
            with self.subTest(data=data), self.assertRaises(ValueError):
                R.validate_plugin_version(plugin, '777.3.0', root=self.root)
        self.registry.unlink()
        with self.assertRaises(ValueError):
            R.validate_plugin_version(plugin, '777.3.0', root=self.root)

    def test_missing_malformed_escaping_or_symlinked_evidence_fails_closed(self):
        plugin = self.bundle_proof()
        for evidence in ('quality/missing.json', '../outside.json', '/tmp/outside.json',
                         'quality/../scripts/pakete.json', 'scripts/pakete.json', 'quality//bundle/pakete.json'):
            self.registry.write_text(json.dumps({'schema_version': 1, 'assets': {
                'new-plugin.zip': {**self.record, 'evidence': evidence}}}))
            with self.subTest(evidence=evidence), self.assertRaises(ValueError):
                R.validate_plugin_version(plugin, '777.3.0', root=self.root)
        self.registry.write_text(json.dumps({'schema_version': 1, 'assets': {'new-plugin.zip': self.record}}))
        self.evidence.write_text('{')
        with self.assertRaises(ValueError):
            R.validate_plugin_version(plugin, '777.3.0', root=self.root)
        self.evidence.unlink()
        target = self.root / 'target.json'
        target.write_text(json.dumps(self.proof))
        self.evidence.symlink_to(target)
        with self.assertRaises(ValueError):
            R.validate_plugin_version(plugin, '777.3.0', root=self.root)

    def test_invalid_digest_or_different_registered_version_stays_invalid(self):
        plugin = self.bundle_proof()
        for field, value in (('sha256', 'a' * 63), ('sha256', 'b' * 64), ('version', '777.1.1'),
                             ('tag', 'other-v777.2.0'), ('evidence', None)):
            self.registry.write_text(json.dumps({'schema_version': 1, 'assets': {
                'new-plugin.zip': {**self.record, field: value}}}))
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                R.validate_plugin_version(plugin, '777.3.0', root=self.root)

if __name__=='__main__':unittest.main()
