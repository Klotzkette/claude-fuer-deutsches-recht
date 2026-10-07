#!/usr/bin/env python3
"""Spezifische Integrationsprüfung der vertieften KI-nativen Kanzlei."""
import hashlib,json,re,sys
from pathlib import Path
from urllib.parse import unquote,urlsplit
import yaml
from quality_lab import validate_profile
from prompt_profiles import validate_files
ROOT=Path(__file__).resolve().parents[1];PLUGIN=ROOT/'ki-native-kanzlei'

def main():
    skills=sorted((PLUGIN/'skills').glob('*/SKILL.md'));assert len(skills)==18
    records=[]
    for p in skills:
        s=p.read_text();fm=re.match(r'^---\n(.*?)\n---\n',s,re.S);assert fm,p
        data=yaml.safe_load(fm.group(1));assert set(data)=={'name','description'};assert data['name']==p.parent.name;assert len(data['name'])<=64;assert len(data['description'])<=1024
        assert re.findall(r'^## ([1-6])\.',s,re.M)==list('123456'),p
        assert not re.search(r'^#{2,6} (?:[A-Za-z]|[IVX]+)[.)] ',s,re.M),p
        assert 'Times New Roman' in s and '11' in s and ('ausformuliert' in s.lower() or 'vollständig formuliert' in s.lower()),p
        assert 'sechzehn Skills' not in s and 'SI-native Kanzlei' not in s,p
        for dest in re.findall(r'\[[^\]]+\]\(([^)]+)\)',s):
            if dest.startswith(('https://','http://','#','mailto:')):continue
            file=unquote(dest.split('#',1)[0]);assert (p.parent/file).exists(),(p,dest)
        records.append({'skill':p.parent.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'words_without_frontmatter':len(s[fm.end():].split())})
    limits={}
    for kind in ['schnellstart','hauptproblem','werkstatt']:
        p=PLUGIN/f'ki-native-kanzlei-{kind}.md';assert p.read_bytes()==p.with_suffix('.txt').read_bytes()
        if kind!='werkstatt':assert len(p.read_bytes())<=7500,(kind,len(p.read_bytes()))
        limits[kind]={'utf8_bytes':len(p.read_bytes()),'words':len(p.read_text().split())}
    assert not validate_files(PLUGIN,'ki-native-kanzlei',ROOT)
    profile=json.loads((ROOT/'quality/evals/ki-native-kanzlei.json').read_text());validate_profile(profile,'ki-native-kanzlei',PLUGIN,ROOT)
    market=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())['plugins'];entries=[p for p in market if p['name']=='ki-native-kanzlei'];assert len(entries)==1 and entries[0]['source']=='./ki-native-kanzlei';assert not any(p['name']=='si-native-kanzlei' for p in market)
    for p in [PLUGIN/'plugin.json',PLUGIN/'.claude-plugin/plugin.json',PLUGIN/'.codex-plugin/plugin.json']:
        d=json.loads(p.read_text());assert d['name']=='ki-native-kanzlei' and d['version']=='445.33.7'
    for name in ['README.md','SKILLS.md','ASSET_INDEX.md','SCHWERPUNKTE.md','QUALITY.md','skills-index/README.md','references/rechtsgebiete-uebersicht.md','docs/werkstatt-und-schnellstart-coverage.md']:
        s=(ROOT/name).read_text();assert 'ki-native-kanzlei' in s,name;assert 'si-native-kanzlei/README.md' not in s,name
    report=json.loads((ROOT/'quality/ki-native-kanzlei/umfang.json').read_text());assert report['skill_count']==18
    assert {r['skill']:r['source_sha256'] for r in report['skills']}=={r['skill']:r['sha256'] for r in records};assert min(r['pages'] for r in report['skills'])>=10
    result={'skills':records,'prompts':limits,'cases_in_profile':len(profile['cases']),'criteria_in_profile':sum(len(c['criteria']) for c in profile['cases']),'all_checks':'passed'}
    (ROOT/'quality/ki-native-kanzlei/struktur-pruefung.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'skills':18,'prompt_limits':limits,'pages_total':report['handbook_pages'],'all_checks':'passed'},ensure_ascii=False))
if __name__=='__main__':main()
