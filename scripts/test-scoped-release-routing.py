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

if __name__=='__main__':unittest.main()
