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

# Aktenaufträge für die Vergabestelle. Namen und Zuständigkeiten kommen aus den Skills und der Registry.
VERGABESTELLE_AUFTRAEGE = {
    'vergabe-os-master-orchestrator': ('1-direkte-einstiege-und-fachwerkzeuge', 'Morgen ist Freigaberunde. Was können wir nach Aktenlage entscheiden?', 'Entscheidungsvorlage mit Empfehlung, offenen Freigaben und nächstem Termin.'),
    'vergabeart-und-schwelle-bearbeiten': ('2-vergabeart-und-schwelle', 'Am Betriebshof werden Beton, Beschichtung und Malerarbeiten vergeben. Können Betriebe nur für ein Gewerk oder einen Gebäudeteil anbieten?', 'Auftragswertschätzung, Vergleich der Loszuschnitte und begründete Verfahrenswahl.'),
    'vergabeunterlagen-bearbeiten': ('3-vergabeunterlagen', 'Im Leistungsverzeichnis steht ein Fabrikat. Was muss vor der Bekanntmachung geändert werden?', 'Freigabefassung der betroffenen Position mit Leistungsanforderungen und Nachweisen für die Gleichwertigkeit.'),
    'ruege-bearbeiten': ('4-rüge', 'Ein Betrieb beanstandet die Pflicht zu zwei Kolonnen für ein Los. Wie reagieren wir vor Ablauf der Angebotsfrist?', 'Antwortentwurf und Entscheidung über Abhilfe, Berichtigung der Unterlagen und Angebotsfrist.'),
    'nachpruefung-bearbeiten': ('5-nachpruefung', 'Die Vergabekammer fordert die Akte und eine Stellungnahme zum geplanten Zuschlag an. Was legen wir vor?', 'Stellungnahme zu den Angriffspunkten mit Aktenfundstellen, Vorlageverzeichnis und Fristen.'),
    'arbeitsprodukt-bearbeiten': ('6-arbeitsprodukt', 'Ein Angebot ist beim Preis besser, das andere bei der Bauzeit. Welche Wertung tragen die Formblätter?', 'Nachgerechnete Wertungsmatrix und begründeter Zuschlagsvorschlag.'),
    'unterlagen-und-quellen-auswerten-bearbeiten': ('7-unterlagen-und-quellen-auswerten', 'Im Wertungsbogen fehlt ein Bildverweis. Welche Vorgaben und Testprotokolle belegen den Befund?', 'Belegübersicht mit Fundstellen, widersprüchlichen Angaben und gezielter Anforderung fehlender Unterlagen.'),
    'arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten': ('8-arbeitsprodukt-ausarbeiten-und-kontrollieren', 'Der Ausschlussvermerk liegt zur Unterschrift vor. Passen Begründung, Preisblatt und Bieterantwort zusammen?', 'Gegengelesene Entscheidungsvorlage mit konkreten Korrekturen und offenen Freigabepunkten.'),
}

# Lesetitel einzelner Fachvertiefungen mit historischen Datei- und Überschriftennamen.
VERGABESTELLE_FACHFRAGEN = {
    '21-aufhebung-rechtssicher': 'Aufhebung der Ausschreibung begründen',
    '30-datenschutz-bieterdaten': 'Personenbezogene Bieterdaten schützen',
    'ausschluss-bieter-paragraf-124-gwb': 'Fakultativen Ausschluss nach § 124 GWB prüfen',
    'inhouse-interkommunal': 'Auftrag an eine eigene Gesellschaft oder eine andere Kommune prüfen',
    'mandat-triage-vergaberecht': 'Bei Akteneingang Fristen und anstehende Entscheidungen erkennen',
    'oeffentlich-privat-partnerschaft': 'Öffentlich-private Partnerschaft prüfen',
    'uvgo-fristen-form-und-zustaendigkeit': 'Unterschwellenvergabe nach UVgO auf Fristen, Form und Zuständigkeit prüfen',
    'verg-mehrparteien-konflikt-und-interessen': 'Interessen und Zuständigkeiten mehrerer Beteiligter klären',
    'wirklichkeitsdaten-beschaffung-steuern': 'Betriebs- und Planungsdaten für die Beschaffung prüfen',
    'freiberufliche-leistungen-hoai': 'Planungsaufträge und andere freiberufliche Leistungen vergeben',
    'vergaberecht-anti-korruption-paragraf-123-gwb': 'Korruptionsvorwürfe und zwingende Ausschlussgründe nach § 123 GWB prüfen',
    'vergaberueg-paragraf-160-gwb': 'Rüge und Rügefrist nach § 160 GWB prüfen',
    'bekanntmachung-berichtigung-und-upload-routing': 'Bekanntmachung berichtigen und den Versand im Portal nachweisen',
    'dokumente-intake': 'Eingegangene Vergabeunterlagen erfassen und zuordnen',
    'einstieg-routing': 'Bearbeitungsstand und nächsten Auftrag klären',
    'quellen-livecheck': 'Geltung und Fundstelle der Rechtsgrundlagen prüfen',
    'sektvo-dokumentenmatrix-und-lueckenliste': 'Fehlende Unterlagen in der Sektorenvergabe bestimmen',
    'vergabesenat-quellenkarte': 'Entscheidungen des Vergabesenats mit Fundstellen zusammenstellen',
    'workflow-kaltstart-und-routing': 'Einzelunterlage sichten und die konkrete Vergabefrage bestimmen',
    'konzvgv-risikoampel-und-gegenargumente': 'Risiken und Gegenargumente einer Konzessionsvergabe prüfen',
    'orientierung-fehlerkatalog': 'Typische Fehler im Verfahrensentwurf erkennen',
    'output-waehlen': 'Benötigten Vermerk, Antwortbrief oder Schriftsatz bestimmen',
    'spezial-orientierung-red-team-und-qualitaetskontrolle': 'Entwurf aus Sicht eines Einwenders gegenprüfen',
}

def title(path):
    text=path.read_text(encoding='utf-8')
    heading=re.search(r'^#\s+(.+)$',text,re.M)
    return (heading[1] if heading else path.parent.name).replace('[','').replace(']','')

def vergabestellen_navigation(plugin, directory, count):
    main, = plugin['keep']
    routes = [(main, title(directory/'skills'/main/'SKILL.md'), plugin['keep'])]
    routes.extend((route['slug'], route['title'], route['members']) for route in plugin['routes'])
    if {slug for slug, _, _ in routes} != set(VERGABESTELLE_AUFTRAEGE):
        raise ValueError('Die Auftragsauswahl muss jeden aktiven Behörden-Skill enthalten.')
    menu = [BEGIN, '', '<a id="skills"></a>', '', '## Welcher Auftrag liegt auf Ihrem Tisch?', '',
            'Hängen Sie die Unterlagen an und nennen Sie die anstehende Entscheidung oder das gewünschte Schreiben. '
            'Für einen ganzen Vorgang beginnen Sie mit dem ersten Arbeitsweg.', '',
            '| Arbeitsweg | Auftrag aus der Praxis | Was Sie erhalten |', '| --- | --- | --- |']
    catalog = ['<a id="fachmodule-und-arbeitswege"></a>', '', '# Fachmodule für die Vergabestelle', '',
               f'Die {len(routes)} Arbeitswege erschließen den Hauptskill und {count - 1} Fachvertiefungen. Wählen Sie einen Arbeitsweg, wenn Sie eine Entscheidung '
               'oder einen Entwurf brauchen. Für eine einzelne Fachfrage können Sie direkt zum passenden Prüfschritt oder Rechtsgebiet springen.', '',
               '[Aufträge und Beispiele im Plugin-Einstieg](README.md#skills)', '']
    source = directory.relative_to(ROOT).as_posix()
    for number, (slug, name, _) in enumerate(routes, 1):
        anchor, example, result = VERGABESTELLE_AUFTRAEGE[slug]
        download = f"https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path={source}/skills/{slug}/SKILL.md"
        menu.append(f'| [{name}]({download}) | {example} | {result} |')
        catalog.append(f'{number}. [{name}](#{anchor})')
    for number, (slug, name, members) in enumerate(routes, 1):
        anchor, _, result = VERGABESTELLE_AUFTRAEGE[slug]
        catalog.extend(['', f'<a id="{anchor}"></a>', '', f'## {number}. {name}', '', result, '',
                        f'[Arbeitsweg öffnen](skills/{slug}/SKILL.md)', ''])
        for member in members:
            if member != main:
                path = directory/'skills'/member/'FACHINHALT.md'
                label = VERGABESTELLE_FACHFRAGEN.get(member) or title(path)
                catalog.append(f'- [{label}](skills/{member}/FACHINHALT.md)')
    menu.extend(['', f'[Hauptskill und {count - 1} Fachvertiefungen nach Arbeitsweg](FACHMODULE.md)', '', END])
    return '\n'.join(catalog).rstrip()+'\n', '\n'.join(menu)

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
    block=f'{BEGIN}\n\nDas Plugin bietet **{active} auswählbare Skills**. Die **{count} vollständigen Fachmodule** und ihre Hilfsdateien stehen in der [Fachbibliothek](FACHMODULE.md). Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.\n\n{END}'
    if plugin['name'] == 'vergabestelle-behoerden':
        index, block = vergabestellen_navigation(plugin, directory, count)
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
