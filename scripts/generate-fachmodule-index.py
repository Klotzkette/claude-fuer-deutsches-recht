#!/usr/bin/env python3
"""Erzeugt die vollständige Fachbibliothek neben der kompakten Skill-Auswahl."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
BEGIN='<!-- BEGIN FACHMODULE-NAVIGATION -->'
END='<!-- END FACHMODULE-NAVIGATION -->'

def title(path):
    text=path.read_text(encoding='utf-8')
    heading=re.search(r'^#\s+(.+)$',text,re.M)
    return (heading[1] if heading else path.parent.name).replace('[','').replace(']','')

def outputs(plugin):
    directory=ROOT/plugin['source'];count=len(plugin['keep'])+sum(len(r['members']) for r in plugin['routes'])
    active=len(plugin['keep'])+len(plugin['routes'])
    lines=['# Fachmodule und Arbeitswege','',f'{count} vollständige Fachmodule sind über {active} auswählbare Skills erreichbar. Die Arbeitswege verbinden verwandte Aufgaben; die Fachtexte, Werkzeuge und Vorlagen werden nach Bedarf geladen.','',
           '[Plugin-Einstieg](README.md) · [Aktive Skill-Auswahl](../skills-index/'+plugin['name']+'.md)','',
           'Ein Fachmodul ist eine Vertiefung innerhalb eines Skills. Einzeln heruntergeladene Markdown-Dateien enthalten verknüpfte Hilfsdateien nicht; das Plugin-ZIP enthält den vollständigen Zusammenhang.','']
    section=0
    if plugin['keep']:
        section+=1;lines += [f'## {section}. Direkte Einstiege und Fachwerkzeuge','']
        for slug in plugin['keep']:
            path=directory/'skills'/slug/'SKILL.md'
            lines.append(f'- [{title(path)}](skills/{slug}/SKILL.md)')
        lines.append('')
    for route in plugin['routes']:
        section+=1;lines += [f'## {section}. {route["title"]}','',route['purpose'],'',f'[Arbeitsweg öffnen](skills/{route["slug"]}/SKILL.md)','']
        for member in route['members']:
            path=directory/'skills'/member/'FACHINHALT.md'
            if not path.is_file():raise ValueError(f'Fachmodul fehlt: {path}')
            lines.append(f'- [{title(path)}](skills/{member}/FACHINHALT.md)')
        lines.append('')
    # Repo-übergreifende Navigation gehört nicht zum Inhalt des Pluginarchivs.
    lines[4]='[Plugin-Einstieg](README.md)'
    index='\n'.join(lines)
    block=f'{BEGIN}\n\nDas Plugin bietet **{active} auswählbare Skills**. Die **{count} vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.\n\n{END}'
    path=directory/'README.md';readme=path.read_text()
    if BEGIN in readme:
        start,end=readme.index(BEGIN),readme.index(END)+len(END);readme=readme[:start]+block+readme[end:]
    else:
        # Bei der fachlichen Auswahl platzieren, nicht vor der Zweckerklärung.
        markers=[readme.find(m) for m in ('<!-- BEGIN SKILLS-LOGIC', '<!-- BEGIN SKILLS-OVERVIEW') if m in readme]
        pos=min(markers) if markers else len(readme)
        readme=readme[:pos].rstrip()+'\n\n'+block+'\n\n'+readme[pos:]
    return {directory/'FACHMODULE.md':index,path:readme}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    registry=json.loads((ROOT/'scripts/data/skill-cap-registry.json').read_text());different=[]
    for plugin in registry['plugins']:
        for path,text in outputs(plugin).items():
            if not path.exists() or path.read_text()!=text:
                different.append(str(path.relative_to(ROOT)))
                if not args.check:path.write_text(text,encoding='utf-8')
    print(f'Fachbibliotheken: {len(registry["plugins"])} Plugins, {len(different)} '+('abweichende Dateien' if args.check else 'aktualisierte Dateien'))
    if args.check and different:
        print('\n'.join(different[:15]));return 1
    return 0

if __name__=='__main__':raise SystemExit(main())
