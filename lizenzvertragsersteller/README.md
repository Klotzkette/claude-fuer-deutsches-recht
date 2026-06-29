# Lizenzvertragsersteller

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Baukastensystem für IP-Lizenzverträge deutsches und internationales Recht. 32 Skills: Urheber Patent Marken Design Gebrauchsmuster Geschäftsgeheimnis Know-how; Klausel-Bausteine, Quellcode-Escrow, Insolvenz-Klausel, Sicherungslizenz, TT-GVO, DSGVO, Quellensteuer, Output DE EN bilingual.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`lizenzvertragsersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lizenzvertragsersteller.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lizenzvertragsersteller-werkstatt.md" download><code>lizenzvertragsersteller-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lizenzvertragsersteller-schnellstart.md" download><code>lizenzvertragsersteller-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Baukastensystem für IP-Lizenzvertraege nach deutschem und internationalem Recht. Pro Rolle, IP-Typ und Klauselbaustein ein Skill — die Skills greifen ineinander, vom Mandats-Intake bis zum unterschriftsreifen Vertrag in DE, EN oder bilingual.

## Was deckt das Plugin ab?

### IP-Typen
- **Urheberrecht und Software** (UrhG; $$ 31, 32, 32a, 69a-g)
- **Patente** (PatG; TT-GVO-Konformitaet)
- **Marken** (MarkenG $ 30; DPMA/EUIPO; Qualitaetskontrolle)
- **Geschmacksmuster / Design** (DesignG; EU-VO 6/2002)
- **Gebrauchsmuster** (GebrMG; Schnellschuss-Strategie neben Patent)
- **Geschäftsgeheimnisse / Know-how** (GeschGehG; Reverse-Engineering-Verbot)

### Parteienrollen
- Lizenzgeber / Lizenznehmer
- Sicherheitengeber / Sicherheitennehmer (Bank, Investor)
- Verwahrer / Escrow-Agent (Source-Code-Hinterlegung)
- Cross-Lizenz-Partner (Patent-Pool, Forschungspartnerschaft)
- Konzernlizenznehmer

### Vertragsbausteine
- Lizenzgegenstand mit Anlage A (IP-Liste, Reg.-Nr., Belastungen)
- Lizenzumfang (Territorium, Zeit, Anwendungsfeld)
- Exklusivitaet (sole, exclusive, non-exclusive, Most-Favoured-Customer)
- Vergütung (Pauschale, Running Royalty, Tiered, Mindestlizenz, Milestones)
- Reporting, Audit, Strafzinsen
- Sub-Lizenzen
- Verbesserungen / Grant-Back
- Haftung / Gewährleistung / Indemnification
- Rechtswahl + Gerichtsstand + Schiedsklausel (DE/EN/Schiedsinstitute)
- Vertragsdauer + Kuendigung + Folgen
- Vertraulichkeit + NDA-Interimsphase
- Source-Code-Escrow
- Insolvenzfestigkeit ($ 103 InsO)
- Sicherungslizenz / Pfandrecht an Immaterialguetern

### Compliance-Schichten
- Kartellrecht (TT-GVO EU 316/2014)
- Exportkontrolle (Dual-Use VO EU 2021/821; AWG/AWV; Sanktionen)
- Datenschutz (DSGVO Art. 28, 44 ff., 26)
- Steuern + Quellensteuer + DBA

### Output-Module
- Vertrag DE (Fertigentwurf, 20 Paragraphen, Anlagen A-E)
- Vertrag EN (Licence Agreement, English Law oder German Law)
- Bilingual DE/EN (side-by-side + Massgeb-Klausel)

## Workflow

```
1. einstieg-routing                          (Dashboard, Sofort-Triage)
2. mandat-intake-und-konfliktpruefung        (Konflikt-Check, Eilfristen)
3. ip-identifikation-und-bestandsaufnahme    (Anlage A: IP-Inventar)
4. parteienrolle-klaeren-...                  (Rollenmatrix)
5. transaktionsstruktur-visualisieren-ascii  (Diagramm)
6. pro IP-Typ: lizenz-XXX-spezialskill        (UrhG, PatG, MarkenG, ...)
7. Klauselbausteine waehlen + adaptieren     (klausel-XXX)
8. Compliance-Pruefung                        (TT-GVO, Dual-Use, DSGVO, Steuern)
9. Output                                     (DE / EN / bilingual)
```

## Quellenhygiene

- Rechtsprechung nur live verifizieren auf `bundesgerichtshof.de`, `dejure.org`, `curia.europa.eu`, `bundespatentgericht.de`.
- Keine BeckRS-/juris-/Kommentar-/Aufsatz-Blindzitate.
- Norm-Stellen aus `gesetze-im-internet.de` und `eur-lex.europa.eu`.

Konvention: siehe `references/quellenhygiene.md`, `references/zitierweise.md`, `references/leitentscheidungen-anker.md`.

## 32 Skills auf einen Blick

| Gruppe | Skills |
|---|---|
| Einstieg + Intake | `einstieg-routing`, `mandat-intake-und-konfliktpruefung`, `ip-identifikation-und-bestandsaufnahme`, `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer`, `transaktionsstruktur-visualisieren-ascii` |
| IP-Typ | `lizenz-urheberrecht-und-software-urhg`, `lizenz-patent-patg`, `lizenz-marke-markeng`, `lizenz-geschmacksmuster-design-designg`, `lizenz-gebrauchsmuster-gebrmg`, `lizenz-geschaeftsgeheimnis-knowhow-geschgehg` |
| Klauseln | `klausel-lizenzgegenstand-und-anlage-ip-liste`, `klausel-lizenzumfang-territorium-zeit-feld`, `klausel-exklusivitaet-sole-non-exclusive`, `klausel-verguetung-pauschale-royalty-tiered`, `klausel-mindestlizenzen-meldungen-audit`, `klausel-unterlizenzen-sublicensing`, `klausel-verbesserungen-grant-back`, `klausel-haftung-gewaehrleistung-indemnification`, `klausel-rechtswahl-gerichtsstand-schiedsklausel`, `klausel-vertragsdauer-kuendigung-rueckwirkung`, `klausel-vertraulichkeit-und-nda-interimsphase` |
| Insolvenz + Sicherheiten | `escrow-quellcode-verwahrer-vereinbarung`, `insolvenz-fortbestand-paragraf-103-inso-lizenz`, `sicherungslizenz-pfandrecht-an-immaterialguetern` |
| Compliance | `kartellrecht-tt-gvo-eu-316-2014`, `exportkontrolle-dual-use-eu-2021-821`, `datenschutz-dsgvo-im-lizenzvertrag`, `steuern-quellensteuer-und-dba-lizenz` |
| Output | `output-vertrag-deutsch-fertigentwurf`, `output-vertrag-englisch-fertigentwurf`, `output-zweisprachig-bilingual-deutsch-englisch` |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 32 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `datenschutz-dsgvo-im-lizenzvertrag` | DSGVO im Lizenzvertrag: Auftragsverarbeitung Art. 28 DSGVO; Kundendaten als Lizenz-Inhalt; Drittlands-Uebermittlungen Art. 44 ff. DSGVO; SCCs Schrems II Folgen; Joint Controllership Art. 26 DSGVO bei Cross-License. |
| `einstieg-routing` | Anwalts-Dashboard fuer den Lizenzvertragsersteller: Sofort-Triage (IP-Typ, Parteien, Sprache, Rechtswahl), Risiko-Ampel, Anschluss-Skill-Router, Norm-Radar, Leitentscheidungs-Anker; maximal eine Rueckfrage. |
| `escrow-quellcode-verwahrer-vereinbarung` | Source-Code-Escrow-Vereinbarung: drei-Parteien-Vertrag Lizenzgeber - Lizenznehmer - Escrow-Agent; Hinterlegungsumfang; Release-Trigger (Insolvenz, Wartungsausfall); Aktualisierungspflicht; bekannte Escrow-Anbieter; insolvenzfeste Gestalt... |
| `exportkontrolle-dual-use-eu-2021-821` | Exportkontrolle bei Lizenzvertraegen: VO (EU) 2021/821 (Dual-Use); AWG / AWV; Embargo-/Sanktions-Listen; Technologie-Transfer als genehmigungspflichtige Ausfuhr; Cloud-Lizenzen mit Cross-Border-Datenzugriff. |
| `insolvenz-fortbestand-paragraf-103-inso-lizenz` | Insolvenzfestigkeit von Lizenzen $ 103 InsO: Wahlrecht des Verwalters, BGH-Linie zur Lizenz-Behandlung bei Lizenzgeber-Insolvenz; Sicherungslizenz; Escrow als praktische Loesung; Vertragsklauseln zur Vermeidung der Wahl. |
| `ip-identifikation-und-bestandsaufnahme` | IP-Identifikation und Bestandsaufnahme fuer Lizenzvertraege: Schutzrechtsregister-Auszug, Klassifikation nach Typ (Urheber Patent Marke Design Gebrauchsmuster Geschäftsgeheimnis), Belastungen, Erfindervergutung, Lizenzhistorie, IP-Invent... |
| `kartellrecht-tt-gvo-eu-316-2014` | Kartellrecht im Lizenzvertrag: TT-GVO VO (EU) 316/2014 Technologietransfer-Gruppenfreistellung; Marktanteilsschwellen 20 / 30 Prozent; Kernbeschraenkungen Art. 4; nicht-freigestellte Beschraenkungen Art. 5; Schranken bei vertikalen Vertr... |
| `klausel-exklusivitaet-sole-non-exclusive` | Exklusivitaetsklauseln: ausschliessliche Lizenz (mit / ohne Selbstnutzung Lizenzgeber), Sole License, einfache Lizenz, Most-Favoured-Customer-Klauseln; kartellrechtliche Schranken TT-GVO. |
| `klausel-haftung-gewaehrleistung-indemnification` | Haftungs- und Gewaehrleistungsklauseln im Lizenzvertrag: Inhaberschaftsgarantie, Patent-Marketability, IP-Infringement-Indemnification, Haftungshoechstgrenzen, Ausschluesse fuer Vorsatz und grobe Fahrlaessigkeit, Drittansprueche. |
| `klausel-lizenzgegenstand-und-anlage-ip-liste` | Klausel Lizenzgegenstand mit Anlage A (IP-Liste): pro IP-Typ Identifikation, Schutzrechtsregister-Nummern, Schutzgebiete, Lebensdauer, Belastungen; mit Praezisierungstechniken (Patente per Anspruch, Marken per Nizza-Klasse, Software per... |
| `klausel-lizenzumfang-territorium-zeit-feld` | Lizenzumfang-Klausel: territorial (Schutzgebiete), zeitlich (Laufzeit, Beendigung), Anwendungsfeld (Field of Use). Mit Beispielklauseln fuer enge und weite Fassungen, Zweckuebertragungstheorie $ 31 V UrhG. |
| `klausel-mindestlizenzen-meldungen-audit` | Mindestlizenzen, Reporting, Audit-Recht: Berichtspflichten quartalsweise, jaehrliche Prüfer-Audit, Strafzinsen bei Verzug, Beschraenkung Audit-Frequenz. Mit Mustertext und Eskalationsstufen. |
| `klausel-rechtswahl-gerichtsstand-schiedsklausel` | Rechtswahl-, Gerichtsstands- und Schiedsklauseln im Lizenzvertrag: Rom-I-VO Art. 4, deutsches Recht, Schweizer Recht, English Law, NY Law; ICC, DIS, LCIA, Stockholm Schiedsklauseln; Mediation-Vorschaltung. |
| `klausel-unterlizenzen-sublicensing` | Sublizenz-Klauseln $ 35 UrhG: Zustimmung des Lizenzgebers, Konzern-Sublizenzen ohne Zustimmung, Sub-Royalty-Beteiligung, Kettendurchgriff, Haftungskette bei Sub-Lizenznehmer-Versagen. |
| `klausel-verbesserungen-grant-back` | Grant-Back-Klauseln fuer Verbesserungen und Weiterentwicklungen: Pflichtmeldung; nicht-ausschliessliches vs. ausschliessliches Grant-Back; Field-of-Use-Trennung; kartellrechtliche Grenzen TT-GVO Art. 5. |
| `klausel-verguetung-pauschale-royalty-tiered` | Verguetungsmodelle: Pauschale (Lump Sum), Running Royalty (Stueck / Umsatz / Gewinn), Tiered Royalties (sinkende Raten mit steigendem Umsatz), Mindestlizenzgebuehren, Front Loaded Payments. Mit Rechen-Beispielen. |
| `klausel-vertragsdauer-kuendigung-rueckwirkung` | Vertragsdauer-Klauseln: feste Laufzeit, unbefristet mit Kuendigung, Verlaengerungsautomatik (Roll-over), ordentliche und ausserordentliche Kuendigung, Folgen Beendigung (Rueckgabe, Vertraulichkeit überhang, Lizenz-Nachwirkung). |
| `klausel-vertraulichkeit-und-nda-interimsphase` | Vertraulichkeitsklausel im Lizenzvertrag sowie NDA fuer Interimsphase vor Vertragsschluss: Definition vertraulicher Informationen, Ausnahmen (oeffentlich, schon bekannt), Dauer (5 Jahre nach Vertragsende), Beweislast, Rueckgabepflicht, v... |
| `lizenz-gebrauchsmuster-gebrmg` | Gebrauchsmusterlizenzen nach GebrMG: kleine Schwester des Patents, ohne Prüfverfahren; Schutzdauer 10 Jahre; eintragungsbeduerftiges Recht; Erfindungshoehe geringer als Patent; Zweigutachten-Strategie (parallel zu Patent). |
| `lizenz-geschaeftsgeheimnis-knowhow-geschgehg` | Lizenz von Geschäftsgeheimnissen und Know-how nach GeschGehG: $$ 1-12 GeschGehG; Schutzmassnahmen $ 2 Nr. 1b; Reverse Engineering $ 3; Sphaeren-Trennung; Know-how-Lizenz mit Vertraulichkeitsklauseln und Sanktionsregelungen. |
| `lizenz-geschmacksmuster-design-designg` | Designlizenzen nach DesignG (frueher GeschmacksmusterG): $ 31 DesignG Uebertragung und Lizenz; Eintragung DPMA/EUIPO; Schutzdauer max 25 Jahre; EU-Gemeinschaftsgeschmacksmuster GGV 6/2002; nicht eingetragenes Gemeinschaftsgeschmacksmuste... |
| `lizenz-marke-markeng` | Markenrechtslizenzen nach MarkenG $ 30: Qualitaetskontrolle, Bezeichnungspflicht, Eintragungspflicht im DPMA-Register $ 30 III, Erloeschen nicht-genutzter Marken $ 26, EU-Marken EUIPO. Mit Klauselbausteinen Qualitaetskontrolle. |
| `lizenz-patent-patg` | Patentlizenzen nach PatG und EPUe: $$ 9 und 15 PatG Lizenz; Erfinderbenennung $ 63 PatG; ArbnErfG Arbeitnehmererfindergesetz; Zwangslizenz $ 24 PatG; Patent-Pool und FRAND-Lizenz; TT-GVO als Kartellfreistellung. |
| `lizenz-urheberrecht-und-software-urhg` | Urheberrechts- und Software-Lizenzen nach UrhG: $ 31 ff. UrhG einfache und ausschliessliche Nutzungsrechte, $ 32 angemessene Verguetung, $ 32a Bestseller-Klausel, $ 69a-g UrhG Computerprogramme, $ 137l UrhG unbekannte Nutzungsarten. Mit... |
| `mandat-intake-und-konfliktpruefung` | Mandatsannahme fuer Lizenzvertragsersteller: Konfliktcheck (mehrseitige Vertretung im IP-Verkehr ist Standardrisiko), Mandantenbasisdaten, Ziel- und Eilfristanalyse, Vorvertragspruefung (NDA, LOI, MOU), Dokumenten-Intake-Liste. |
| `output-vertrag-deutsch-fertigentwurf` | Output: vollstaendiger Lizenzvertragsentwurf in deutscher Sprache. Praeambel; 19 Paragraphen; Anlagen A-E; Unterschriftenseite. Aus den Klausel-Bausteinen zusammengestellt; modular je nach IP-Typ und Konstellation. |
| `output-vertrag-englisch-fertigentwurf` | Output: vollstaendiger Lizenzvertrag in englischer Sprache (Licence Agreement). Standard-Klauseln in English Law / German-Law-Variante; Royalty / Sublicensing / Indemnification / Governing Law / Arbitration. Bilingual-faehig. |
| `output-zweisprachig-bilingual-deutsch-englisch` | Output: zweisprachiger Lizenzvertrag mit Massgeb-Sprache. Side-by-side DE/EN; Massgeb-Klausel bei Divergenz; sprachliche Sorgfalt; Glossar; Vorteile und Risiken bilingualer Gestaltung. |
| `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer` | Rollenmatrix fuer Lizenzvertraege: Lizenzgeber, Lizenznehmer, Sicherheitengeber, Sicherheitennehmer, Verwahrer (Source-Code-Escrow), Konzernlizenzen, Cross-License. Mit Klärungs-Checkliste pro Rolle. |
| `sicherungslizenz-pfandrecht-an-immaterialguetern` | Sicherungslizenz und Pfandrecht an Immaterialguetern: Verpfaendung von Patenten/Marken nach $$ 1273 ff. BGB analog; Sicherungsabtretung; aufschiebend bedingte Lizenz; Verwertung im Sicherungsfall; Eintragungsfaehigkeit DPMA. |
| `steuern-quellensteuer-und-dba-lizenz` | Steuern und Quellensteuer im Lizenzvertrag: $ 49 EStG Quellensteuer auf Royalties 15 Prozent; DBA-Reduktion (z. B. 0 Prozent DE-USA mit Antrag); EU-Zinsen-Lizenzgebuehren-Richtlinie; Umsatzsteuer auf Lizenzen; Gross-up-Klauseln. |
| `transaktionsstruktur-visualisieren-ascii` | ASCII-Visualisierung der Lizenztransaktion: Parteien als Boxen, Lizenzflows als Pfeile, Sicherheiten und Escrow-Wege. Pro Konstellation (Einfach, Cross-License, Konzern, Pool, mit Sicherheiten) ein Schema. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
