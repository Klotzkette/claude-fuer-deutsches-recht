#!/usr/bin/env python3
"""Erzeugt die vollständige Fachbibliothek neben der kompakten Skill-Auswahl."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from skill_sources import replacements

ROOT=Path(__file__).resolve().parents[1]
BEGIN='<!-- BEGIN FACHMODULE-NAVIGATION -->'
END='<!-- END FACHMODULE-NAVIGATION -->'

def title(path):
    text=path.read_text(encoding='utf-8')
    heading=re.search(r'^#\s+(.+)$',text,re.M)
    return (heading[1] if heading else path.parent.name).replace('[','').replace(']','')

def outputs(plugin):
    replacement = replacements().get(plugin['name'])
    if replacement is not None:
        return replacement_outputs(plugin, replacement)
    directory=ROOT/plugin['source'];count=len(plugin['keep'])+sum(len(r['members']) for r in plugin['routes'])
    active=len(plugin['keep'])+len(plugin['routes'])
    if plugin.get('consolidated_sources'):
        count=sum(len(route['members']) for route in plugin['routes'])
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
    if plugin.get('consolidated_sources'):
        retained = sorted((directory/'skills').glob('*/REFERENZ*.md'))
        if retained:
            section += 1
            lines += [f'## {section}. Ergänzende Arbeitsanweisungen', '', 'Die bisherigen vollständigen Anweisungen bleiben zusätzlich verlinkt; maßgeblich für die Auswahl sind die aktiven Arbeitswege.', '']
            for path in retained:
                lines.append(f'- [{title(path)}]({path.relative_to(directory).as_posix()})')
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


def replacement_outputs(plugin, replacement):
    directory = ROOT / replacement['source']
    active = sorted((directory/'skills').glob('*/SKILL.md'))
    if {path.parent.name for path in active} != set(replacement['active_skills']):
        raise ValueError('Fachbibliothek und aktive Skills weichen voneinander ab')
    chapters = replacement['chapters']
    if not chapters or len(chapters) != len(set(chapters)):
        raise ValueError('Eindeutige fachliche Kapitel erforderlich')
    lines = ['# Fachbibliothek für Konzernversorgung', '',
             f'{len(active)} auswählbare Skills führen durch die Bearbeitung. Die {len(chapters)} Fachkapitel vertiefen die jeweils benötigten Fragen; sie sind keine zusätzlichen Menü-Skills.', '',
             '[Plugin-Einstieg](README.md)', '',
             '## 1. Fachkapitel', '']
    for index, relative in enumerate(chapters, 1):
        path = directory / relative
        if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(directory.resolve()):
            raise ValueError(f'Fachkapitel fehlt oder verlässt das Plugin: {relative}')
        lines.append(f'{index}. [{title(path)}]({relative})')
    lines += ['', '## 2. Arbeitswege', '']
    for path in active:
        lines.append(f'- [{title(path)}]({path.relative_to(directory).as_posix()})')
    lines += ['', 'Die Kapitel enthalten Fachanweisungen und geprüfte Quellenanker. Historische Fassungen werden außerhalb des installierten Plugins als Prüfspur aufbewahrt. Maßgeblich sind die hier verlinkten Kapitel und der im jeweiligen Auftrag überprüfte Rechtsstand.', '']
    return {directory / 'FACHMODULE.md': '\n'.join(lines)}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    registry=json.loads((ROOT/'scripts/data/skill-cap-registry.json').read_text());different=[]
    for plugin in registry['plugins']:
        if plugin.get('retained_source_archive'):
            continue
        for path,text in outputs(plugin).items():
            if not path.exists() or path.read_text()!=text:
                different.append(str(path.relative_to(ROOT)))
                if not args.check:path.write_text(text,encoding='utf-8')
    print(f'Fachbibliotheken: {len(registry["plugins"])} Plugins, {len(different)} '+('abweichende Dateien' if args.check else 'aktualisierte Dateien'))
    if args.check and different:
        print('\n'.join(different[:15]));return 1
    return 0

if __name__=='__main__':raise SystemExit(main())
