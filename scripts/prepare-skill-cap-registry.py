#!/usr/bin/env python3
"""Erzeugt einen überprüfbaren Zuordnungsentwurf; verändert keine Plugins.

Die fachlichen Arbeitsstationen stammen aus den kuratierten Themenprofilen.
Die endgültige explizite Registry ist die Eingabe der Migration. Eine
Schlüsselwortzuordnung ist kein fachlicher Quellencheck.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata
from themen_profile import profile_for
from skill_cap_taxonomy import TOPICS
from skill_limits import MAX_ACTIVE_SKILLS_PER_PLUGIN

ROOT = Path(__file__).resolve().parents[1]
STOP = set('und oder mit fuer von der die das den dem des ein eine einen einer einem im in zu zur zum als auf aus an am durch nach bei vor ist sind wird werden pruefen pruefung bearbeiten erstellen klaeren sowie getrennt konkret konkrete konkreten bestimmen fall fachlich'.split())
NAME_ACTIONS = set('pruefen bearbeiten erstellen gestalten ausarbeiten kontrollieren auswerten ordnen einordnen berechnen vorbereiten planen organisieren steuern koordinieren entscheiden durchsetzen begleiten bewerten abstimmen analysieren formulieren beantworten verhandeln klaeren umsetzen vollziehen abrechnen dokumentieren vergleichen bestimmen sichern abschliessen fuehren'.split())
GENERIC_NAME_WORDS = STOP | NAME_ACTIONS | set('skill skills workflow fachworkflow modul module kompendium kompendien allgemein spezial hauptsache hauptskill hauptworkflow hauptauftrag aufgabe aufgaben test thema themen bereich fachbereich fachthema faelle'.split())
NAME_CONNECTORS = set('und oder mit fuer von der die das den dem des ein eine einen einer einem im in zu zur zum als auf aus an am durch nach bei vor'.split())

# Die allgemeine Familie reicht für diese spezialisierten Produkte nicht aus.
# Jede Station beschreibt Anlass und bearbeitbares Ergebnis, nicht nur ein Menü.
OVERRIDES = {
 'arbeits': [
  'Vertrag und Beschäftigungsstatus: Arbeitsvertrag, Befristung, Nachweis, Arbeitnehmerstellung und Weisungsrecht prüfen und eine belastbare Vertragsfassung ausarbeiten.',
  'Vergütung und laufendes Arbeitsverhältnis: Arbeitszeit, Annahmeverzug, Urlaub, Krankheit, Entgelt und Ausschlussfristen mit Belegen abrechnen oder geltend machen.',
  'Kündigung und Trennung: Kündigungsgrund, Abmahnung, Beteiligung, Form, Zugang, Fristen und Weiterbeschäftigung bis zum konkreten Schreiben bearbeiten.',
  'Betriebsrat und kollektive Regelungen: Tarifvertrag, Betriebsvereinbarung, Mitbestimmung, Betriebsänderung und Sozialplan auf den Vorgang anwenden.',
  'Schutzpflichten und Beschäftigtendaten: Gleichbehandlung, AGG, Arbeitsschutz, Datenschutz und interne Untersuchungen mit verhältnismäßiger Beweissicherung verbinden.',
  'Arbeitsgericht und Verständigung: Klage, Erwiderung, Beweisfragen, Rechtsmittel und Vergleich bis zum vollständigen Arbeitsprodukt führen.',
 ],
 'datenschutz': [
  'Verarbeitung und Rechtsgrundlage: Rollen, Zwecke, Datenkategorien, Erforderlichkeit und Rechtsgrundlage zu einer belegten Zulässigkeitsprüfung verbinden.',
  'Betroffenenrechte und Auskunft: Auskunft, Kopie, Berichtigung, Löschung, Widerspruch, Identität, Fristen und Rechte Dritter bis zur Antwort bearbeiten.',
  'Verträge und Datenübermittlung: Auftragsverarbeitung, gemeinsame Verantwortlichkeit, Empfänger und Drittlandtransfer mit den tatsächlichen Datenflüssen abgleichen.',
  'Technik und Folgenabschätzung: Technische und organisatorische Maßnahmen, Datenschutzfolgenabschätzung, Verzeichnis und Systemänderungen dokumentieren.',
  'Beschäftigte und digitale Dienste: Personaldaten, Überwachung, Marketing, Cookies, Plattformen und KI am konkreten Einsatz prüfen.',
  'Datenpanne und Aufsicht: Vorfall, Meldung, Benachrichtigung, behördliche Untersuchung und Sanktionen anhand der gesicherten Tatsachen bearbeiten.',
  'Schadensersatz und Rechtsschutz: Anspruch, Darlegung, Beweis, Verjährung und gerichtlichen Rechtsschutz zu einem ausformulierten Schreiben oder Schriftsatz führen.',
 ],
 'steuer': [
  'Erklärung und Gewinnermittlung: Belege, Buchführung, Betriebsausgaben, Einkommen, Gewinn und Erklärung zu einer nachvollziehbaren Berechnung verbinden.',
  'Umsatzsteuer und Leistungsbeziehungen: Rechnung, Leistungsort, Vorsteuer, Befreiung, Reverse Charge und Meldung auf tatsächliche Leistungen zurückführen.',
  'Unternehmen und Umstrukturierung: Körperschaftsteuer, Gewerbesteuer, Beteiligung, Sonderbetriebsvermögen, Umwandlung und Unternehmensnachfolge prüfen.',
  'Vermögen und persönliche Steuern: Erbschaft, Schenkung, Grundstück, Grundsteuer und private Einkünfte mit Bewertung und persönlichen Merkmalen abgleichen.',
  'Prüfung und Steuerstrafrecht: Betriebsprüfung, Kasse, Schätzung, Mitwirkung, Berichtigung und strafrechtliche Risiken voneinander trennen.',
  'Bescheid und Rechtsschutz: Bekanntgabe, Änderung, Einspruch, Aussetzung der Vollziehung, Finanzgericht und Rechtsmittel bis zum beauftragten Schriftsatz bearbeiten.',
 ],
 'insolvenz': [
  'Insolvenzreife und Antrag: Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Eröffnungsverfahren anhand der Finanzunterlagen getrennt prüfen.',
  'Forderung und Tabelle: Anmeldung, Rang, Titel, Prüfung, Bestreiten, Feststellung und Verteilung mit dem belegten Forderungsstand abgleichen.',
  'Masse und Vertragsabwicklung: Vermögensbestand, Sicherheiten, Aussonderung, Absonderung, Aufrechnung und Erfüllungswahl bis zum konkreten Verwaltungsschritt bearbeiten.',
  'Anfechtung und Haftung: Zahlung, Rechtshandlung, Zeitraum, Benachteiligung, Kenntnis und Haftungstatbestand anhand der Belege subsumieren.',
  'Sanierung und Verfahrensabschluss: Betriebsfortführung, Plan, Restschuldbefreiung, Gläubigerentscheidung und Abschlussbericht auf den Verfahrensstand abstimmen.',
  'Verfahrensakte und Schreiben: Unterlagen, Chronologie, Fristen und Beweise für Antrag, Bericht, Klage, Erwiderung oder Verständigung ausarbeiten.',
 ],
 'gesellschaft': [
  'Gründung und Gesellschaftsvertrag: Rechtsform, Kapital, Satzung, Beteiligung und Vollzug bis zum abgestimmten Gründungstext führen.',
  'Organe und Vertretung: Geschäftsführung, Aufsichtsrat, Bestellung, Abberufung, Vollmacht und Vertretungsmacht anhand der Beschlüsse prüfen.',
  'Gesellschafter und Beschlussfassung: Einladung, Stimmrecht, Mehrheiten, Informationsrecht, Treuepflicht und Minderheitenschutz im konkreten Konflikt bearbeiten.',
  'Kapital und Strukturmaßnahmen: Finanzierung, Kapitalerhaltung, Umwandlung, Übertragung und Ausscheiden mit den Vertrags- und Registerunterlagen abgleichen.',
  'Register und Vollzug: Anmeldung, Gesellschafterliste, Publizität, Nachweise und Zwischenverfügung bis zum einreichbaren Dokument bearbeiten.',
  'Haftung und Gesellschaftsstreit: Pflichtverletzung, Anspruchsinhaber, Darlegung, Eilrechtsschutz und Einigung zu einem begründeten Arbeitsprodukt führen.',
 ],
 'bauwirtschaft': [
  'Planung und Genehmigung: HOAI Phasen 1 bis 5, Grundlagen, Varianten, Planstände und Fachplanung bis zur Ausführungsreife koordinieren.',
  'Vergabe und Leistungsverzeichnis: Losbildung, Mengen, LV, HOAI Phasen 6 und 7, Bieterfragen und Angebotswertung auf unveränderter Grundlage bearbeiten.',
  'Bauvertrag und Nachunternehmer: Leistungsumfang, Schnittstellen, Sicherheiten und Vertragseinbeziehung ausformulieren.',
  'Kosten und Zahlungsplan: Budget, Liquidität, Rechnungen, Aufmaß, Buchhaltung und Zahlungsfreigabe ohne Doppelzählung fortschreiben.',
  'Bauablauf und Nachträge: Termine, Bautagebuch, Behinderung, Bauzeitfolgen und Mehrleistung bis zum belegten Nachtragsprodukt führen.',
  'Abnahme und Objektbetreuung: HOAI Phasen 8 und 9, Mängel, Übergabe, Gewährleistung und Sicherheitsfreigabe dokumentieren.',
  'Projektbericht und Entscheidung: Kosten, Termine, Risiken und tatsächlich delegierte Befugnisse in einer entscheidungsreifen Vorlage zusammenführen.',
 ],
}
PLUGIN_OVERRIDES = {
 'aussenwirtschaft-zoll-sanktionen': [
  'Geschäft und Güterklassifizierung: Beteiligte, Ware, Technologie, Zolltarif, Ursprung, Empfänger und Endverwendung aus den Unterlagen bestimmen.',
  'Exportkontrolle und Sanktionen: Dual Use, Embargo, Listenprüfung, Umgehungsrisiko und Genehmigungspflicht bis zur konkreten Freigabeentscheidung prüfen.',
  'Zoll und Einfuhrabgaben: Anmeldung, Zollwert, Präferenz, CBAM, Einfuhrumsatzsteuer und Erstattung mit den Lieferbelegen abgleichen.',
  'Verträge und Lieferketten: Transport, Incoterms, Zahlungsweg, Lieferantenpflichten und Nachweise in den konkreten Auftrag einarbeiten.',
  'Behörde und Rechtsschutz: Auskunft, Genehmigung, Prüfung, Sanktion und Rechtsbehelf mit Frist und Beleglage bearbeiten.',
 ],
 'seerecht-schifffahrtsrecht': [
  'Schiff und Betrieb: Eigentum, Register, Flagge, Besatzung, Sicherheit und technische Zulassung nach Fahrtgebiet bestimmen.',
  'Fracht und Charter: Frachtvertrag, Charterparty, Konnossement, Reise, Liegezeit und Ladungsschaden bis zum Vertrags- oder Anspruchstext bearbeiten.',
  'Schiffsunfall und Haftung: Kollision, Bergung, Havarie, Umweltschaden, Haftungsbeschränkung und Versicherung anhand der Belege prüfen.',
  'Hafen und Regulierung: Hafenbetrieb, Lotsen, Gebühren, Sanktionen, Emissionen und öffentlich-rechtliche Pflichten abgleichen.',
  'Streit und Durchsetzung: Arrest, Zuständigkeit, Schiedsverfahren, Beweis, Frist und Vollstreckung zur konkreten Rechtsverfolgung verbinden.',
 ],
 'ki-native-kanzlei': [
  'Mandat und Datenaufnahme: Konflikt, Identität, Beauftragung, Dokumenteingang und Mandantenziel im bestehenden Vorgang zusammenführen.',
  'Bearbeitung und Quellenkontrolle: Recherche, Aktenanalyse, Wissensbestand, Belege und Qualitätsprüfung bis zum belastbaren Entwurf verbinden.',
  'Kanzleiorganisation und Automatisierung: Aufgaben, Rollen, Systeme, Datenschutz, Sicherheit und wirtschaftliche Steuerung anhand des tatsächlichen Betriebs gestalten.',
  'Produkt und Mandantenkommunikation: Schreiben, Präsentation, Bericht, Beratung und Freigabe aus derselben Fassung entwickeln.',
  'Abschluss und Nachweise: Versand, Rechnung, Fristen, Archivierung und Erfolgskontrolle nachvollziehbar abschließen.',
 ],
}

def norm(s):
    for a,b in [('ä','ae'),('ö','oe'),('ü','ue'),('ß','ss')]: s=s.lower().replace(a,b)
    return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()

def words(s):
    return [w for w in re.findall('[a-z][a-z0-9]+',norm(s)) if len(w)>3 and w not in STOP]

def score(text, station):
    a,b=set(words(text)),set(words(station))
    return sum(3 if x==y else 1 for x in a for y in b if x==y or (len(x)>5 and len(y)>5 and x[:5]==y[:5]))

def clean(s):
    return re.sub(r'\s*->\s*skills/[^:]+:', ':', s).strip()

def title(s):
    return ' '.join(s.split(':',1)[0].strip().rstrip('.').split())

def slug(s):
    """Begriffswahrender Namensvorschlag; keine Prüfung fachlicher Qualität."""
    tokens=re.findall('[a-z0-9]+',norm(s))
    def meaningful(parts):
        return any(re.search('[a-z]',word) and word.rstrip('0123456789') not in GENERIC_NAME_WORDS for word in parts)
    if not meaningful(tokens):
        raise ValueError(f'Verständlichen fachlichen Skill-Namen redaktionell festlegen: {s!r}')
    action=tokens[-1] if tokens[-1] in NAME_ACTIONS else 'bearbeiten'
    subject=tokens[:-1] if tokens[-1] in NAME_ACTIONS else tokens[:]
    budget=64-len(action)-1
    shortened=False
    while subject and len('-'.join(subject))>budget:
        subject.pop()
        shortened=True
    if shortened:
        while subject and subject[-1] in NAME_CONNECTORS:
            subject.pop()
    if not meaningful(subject):
        raise ValueError(f'Skill-Namen ohne Wortabbruch auf höchstens 64 Zeichen kürzen: {s!r}')
    return '-'.join([*subject,action])

def protect_entry_skills(name, keep, docs, profiles):
    """Erhält deklarierte Einstiege; bewertet keinen vollständigen Hauptworkflow."""
    profile=profiles.get(name)
    entries=profile.get('entry_skills') if isinstance(profile,dict) else None
    if (not isinstance(entries,list) or not 1<=len(entries)<=3
            or any(not isinstance(entry,str) or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',entry) for entry in entries)
            or len(set(entries))!=len(entries)):
        raise ValueError(f'{name}: eindeutige Einstiegsskills im Visualisierungsprofil erforderlich')
    if (not isinstance(keep,list) or any(not isinstance(item,str) for item in keep)
            or len(set(keep))!=len(keep)):
        raise ValueError(f'{name}: keep muss eindeutige vorhandene Skill-Namen enthalten')
    missing=set(entries)-set(docs)
    if missing:
        raise ValueError(f'{name}: deklarierte Einstiegsskills fehlen als SKILL.md: {sorted(missing)}')
    unprotected=set(entries)-set(keep)
    if unprotected:
        raise ValueError(f'{name}: bestehende Einstiegsskills in keep erhalten: {sorted(unprotected)}')
    if set(keep)-set(docs):
        raise ValueError(f'{name}: in keep genannte Skills fehlen: {sorted(set(keep)-set(docs))}')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--keep',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    profile_data=json.loads((ROOT/'scripts/data/werkstatt-visualisierung-profile.json').read_text())
    if profile_data.get('schema_version')!=1 or not isinstance(profile_data.get('plugins'),dict):
        raise ValueError('Gültige bestehende Visualisierungsprofile für die Einstiegsskills erforderlich')
    entry_profiles=profile_data['plugins']
    registry={'schema_version':1,'plugins':[]}; review=[]
    for item in json.loads(args.keep.read_text())['plugins']:
        name=item['name']; root=ROOT/item['source']
        docs={p.parent.name:p.read_text() for p in (root/'skills').glob('*/SKILL.md')}
        protect_entry_skills(name,item['keep'],docs,entry_profiles)
        profile=profile_for(name)
        topics=TOPICS.get(name,TOPICS.get(profile.key,[]))
        stations=[clean(s) for s in PLUGIN_OVERRIDES.get(name,OVERRIDES.get(profile.key,profile.stationen))]
        if topics: stations=[s for s,rx in topics]
        # Zwei durchgängige Arbeitsprodukte bündeln die früher vielfach
        # duplizierten Mikro-Skills. Fachliche Spezialfragen bleiben separat.
        shared=[
            'Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen.',
            'Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären.',
        ]
        stations+=shared
        groups=[[] for s in stations]
        # Nur der Entwurf nutzt diese Hilfe. Alle Zuordnungen stehen explizit in
        # der Registry und können dort ohne versteckte Laufzeitheuristik geändert werden.
        frequencies=Counter(w for s in docs for w in set(words(s)))
        for old,text in sorted(docs.items()):
            if old in item['keep']: continue
            head=re.search(r'^#\s+(.+)',text,re.M)
            terms=' '.join(w for w in words(old) if frequencies[w]<len(docs)*0.65)
            scores=[score(terms,s)*4+score(head[1] if head else '',s) for s in stations]
            # Querschnittsmodule gehören zum passenden Arbeitsschritt, nicht
            # zufällig zur häufigsten materiellen Station.
            hints=''
            if re.search('redteam|red-team|qualitygate|qualitaet|fehlerkatalog|kontrolle',old): hints='Arbeitsprodukt Ergebnis Prüfung Ausgabe'
            elif re.search('chronologie|dokumentenmatrix|unterlagen|luecken|quellen|recherche|nachforderung',old): hints='Textzeuge Unterlagen Datenraum Belege Information'
            elif re.search('frist|zustaendigkeit|eingang|kaltstart|triage|intake|routing',old): hints='Vorgang Frage Auftrag Frist Verfahren'
            elif re.search('kommunikation|schreiben|export|output|memo|praesentation',old): hints='Arbeitsprodukt Schreiben Ergebnis Antwort'
            if hints:
                for i,s in enumerate(stations): scores[i]+=score(hints,s)*2
            chosen=max(range(len(stations)),key=lambda i:(scores[i],-len(groups[i])))
            if max(scores)==0:
                # Fachprofil enthält eine Prüfstation; dort bleibt die
                # unklare Spezialfrage sichtbar, bis die Zuordnung geprüft ist.
                chosen=max(range(len(stations)),key=lambda i:score('Prüfung Anspruch Fallanalyse Rechtsgrundlage Pflichtenprüfung',stations[i]))
            if topics:
                matched=[]
                for i,(station,pattern) in enumerate(topics):
                    found=re.search(pattern,old)
                    if found: matched.append((found.start(),-len(found[0]),i))
                if matched: chosen=min(matched)[2]
            # Unterscheidung anhand des Arbeitsprodukts bei den duplizierten
            # Querschnitts-Anweisungen; kein Zufallstreffer in der Fachstation.
            if re.search(r'(?:red-?team|qualitygate|qualitaetskontrolle|qualitaetsgate|fehlerkatalog|output-waehlen|outputpaket|schriftsatz-brief|mandantenkommunikation|mandantenbericht|export|output|versandmappe|entwurf-redaktion|verhandlung-vergleich-und-eskalation)',old):
                chosen=len(stations)-1
            elif re.search(r'(?:chronologie|belegmatrix|dokumentenmatrix|unterlagen-luecken|unterlagen-und-luecken|quellenkarte|quellen-livecheck|rechtsquellen-livecheck|livequellen-und-rechtsprechungscheck|dokumente-intake|workflow-kaltstart|einstieg-routing|anwendungsfall-triage|anschluss-routing)',old):
                chosen=len(stations)-2
            groups[chosen].append(old)
            review.append({'plugin':name,'skill':old,'station':title(stations[chosen]),'score':scores[chosen]})
        routes=[]
        for i,(station,members) in enumerate(zip(stations,groups)):
            if not members:continue
            heading=title(station); route_slug=slug(heading)
            if route_slug in docs or any(r['slug']==route_slug for r in routes):
                raise ValueError(f'{name}: Skill-Name {route_slug!r} für {heading!r} kollidiert; einen fachlich unterscheidbaren Namen redaktionell festlegen')
            topic_examples=[]
            for member in members[:2]:
                h=re.search(r'^#\s+(.+)',docs[member],re.M)
                topic_examples.append(f'Ein Auftrag zu „{h[1] if h else member}“: die zugehörige Fachvertiefung lesen, vorhandene Belege auswerten und das verlangte Ergebnis ausarbeiten.')
            routes.append({
                'slug':route_slug,'title':heading,
                'description':f'Für {profile.label}: {station} Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkreten Auftrag eingesetzt.',
                'purpose':station,
                'inputs':['Den konkreten Auftrag und das gewünschte Dokument aus dem Gespräch übernehmen.', 'Bereits vorliegende Fachunterlagen, Fassungen, Belege und zeitliche Angaben zuerst lesen; nur entscheidende Lücken erfragen.'],
                'steps':[station, 'Den passenden Fachinhalt unten anhand des konkreten Gegenstands auswählen und vollständig lesen. Mehrere betroffene Themen gemeinsam behandeln; nicht bei einer bloßen Menüauswahl stehen bleiben.', profile.pruefraster[min(i,len(profile.pruefraster)-1)] if profile.pruefraster else 'Beleglage und fachliche Voraussetzungen getrennt auswerten.', 'Belegte Tatsachen, maßgebliche Quellen, Gegenposition und Unsicherheit am jeweiligen Ergebnis ausweisen. Änderungen in derselben Fassung fortführen und das bestellte Arbeitsprodukt ausarbeiten.'],
                'outputs':[f'Das im Auftrag verlangte, ausgearbeitete Ergebnis zu „{heading}“, mit konkreten Belegstellen und erkennbaren offenen Punkten.', 'Nur soweit hilfreich: eine Vergleichstabelle, Zeitleiste oder grafische Übersicht zusätzlich zum vollständigen Text.'],
                'examples':topic_examples,'members':members,
            })
        active_count=len(item['keep'])+len(routes)
        if active_count>MAX_ACTIVE_SKILLS_PER_PLUGIN:
            raise ValueError(f'{name}: {active_count} aktive Skills überschreiten {MAX_ACTIVE_SKILLS_PER_PLUGIN}; Taxonomie manuell verdichten')
        registry['plugins'].append({'name':name,'source':item['source'],'keep':item['keep'],'routes':routes})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    args.output.with_suffix('.review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(registry["plugins"])} Plugins, {sum(len(p["keep"])+len(p["routes"]) for p in registry["plugins"])} aktive Wege; explizite Zuordnung zur Prüfung geschrieben.')

if __name__=='__main__':main()
