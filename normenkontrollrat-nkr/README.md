# Normenkontrollrat (NKR) — Pruefung von Gesetzentwuerfen

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`normenkontrollrat-nkr`) | [`normenkontrollrat-nkr.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrollrat-nkr.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Testakte NKR: Elektronische Erreichbarkeit von Handelsregister-Gesellschaften (ElErrHandRegG 2026)** (`nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026`) | [Gesamt-PDF lesen](../testakten/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026/gesamt-pdf/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026_gesamt.pdf) | [`testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin fuer die Arbeit eines **Mitglieds oder Referenten / einer Referentin des Nationalen Normenkontrollrats (NKR)** nach dem Gesetz ueber die Einsetzung eines Nationalen Normenkontrollrats (**NKRG vom 14.08.2006, BGBl. I S. 1866**) in der jeweils geltenden Fassung.

Es bildet den vollstaendigen Pruefzyklus eines Vorhabens ab: von der **Eingangstriage** eines Referentenentwurfs ueber die **Erfuellungsaufwand-Berechnung** nach Standardkostenmodell (SKM) und die **Pruefraster** des NKR bis zur **Stellungnahme** nach § 6 NKRG.

## Mandatsperspektive

Das Plugin schreibt aus der Sicht des **NKR-Pruefers**, nicht aus Ressortsicht. Es geht **nicht** darum, einen Entwurf zu verteidigen, sondern darum, ihn nach den NKR-Kriterien zu pruefen und ggf. **kritisch zu kommentieren**.

Leitsatz: *"Wenn nicht noetig, dann nicht regeln; wenn noetig, dann so einfach, so digital, so mittelstandsfreundlich und so evaluationsfest wie moeglich."*

## Aufbau

Das Plugin enthaelt 37 Skills in fuenf Clustern:

```
A — Grundlagen, Verfahren, Mandat (7 Skills)
   nkr-orientierung-und-mandatsaufnahme
   nkr-aufgabe-und-kompetenz-nkrg
   nkr-pruefumfang-was-prueft-der-nkr-nicht
   nkr-verfahrensgang-referentenentwurf-bis-bundestag
   nkr-zusammenarbeit-mit-bundesregierung-und-ressorts
   nkr-eu-ebene-und-better-regulation
   nkr-evaluation-und-jahresbericht

B — Erfuellungsaufwand-Methodik (8 Skills)
   nkr-erfuellungsaufwand-grundbegriff
   nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung
   nkr-standardkostenmodell-skm
   nkr-zeitwerttabelle-und-fallzahlen
   nkr-einmalig-vs-jaehrlich-laufend
   nkr-buerokratiekosten-vs-erfuellungsaufwand
   nkr-fallzahlen-schaetzung-bandbreiten
   nkr-leitfaden-ermittlung-und-darstellung

C — Pruefraster (8 Skills)
   nkr-erforderlichkeitspruefung-warum-ueberhaupt-regeln
   nkr-alternativen-pruefung-keine-regelung-soft-law
   nkr-verhaeltnismaessigkeit-aus-nkr-sicht
   nkr-mittelstandsfreundlichkeit-kmu-test
   nkr-praktikabilitaet-vollzug-test
   nkr-evaluierung-befristung-sunset-klausel
   nkr-digital-anschlussfaehigkeit-tauglich
   nkr-one-in-one-out-bilanz-und-buchung

D — Stellungnahme-Drafting (8 Skills)
   nkr-stellungnahme-aufbau-und-format
   nkr-stellungnahme-grundsatzfeststellung
   nkr-stellungnahme-ergebnis-und-empfehlung
   nkr-stellungnahme-formulierungshilfe-vs-referentenentwurf
   nkr-stellungnahme-zum-bundestag-anhoerung
   nkr-stellungnahme-evaluationsklausel-vorschlag
   nkr-stellungnahme-mahnender-charakter-grenzen
   nkr-stellungnahme-pressepolitik-und-jahresbericht

E — Spezialfaelle / komplexe Themen (6 Skills)
   nkr-digitalcheck-und-onlinezugangsgesetz-ozg
   nkr-eu-richtlinien-umsetzung-und-goldplating
   nkr-handelsregister-und-elektronische-zustellung
   nkr-nachhaltigkeit-klimacheck-und-vereinbarkeit
   nkr-gleichstellungs-und-gendercheck
   nkr-buerokratieabbau-katalog-konkrete-vorschlaege
```

## Methodische Grundlagen (Pflicht-Bezugnahmen)

- **NKRG** vom 14.08.2006 (BGBl. I S. 1866) in der jeweils geltenden Fassung
- **GGO** insbesondere § 44 (Pruefung der Gesetzesfolgen) und § 45 (Erfuellungsaufwand-Darstellung)
- **Handbuch der Rechtsfoermlichkeit (HdR)** als Drafting-Grundlage
- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR)
- **Standardkostenmodell (SKM)** als NKR-Methodik
- **One-in-one-out-Regel** (Beschluss der Bundesregierung 2015)
- **Digitalcheck** (seit 2022)
- **OZG** und OZG-Folgeregulierung (Stand vom Anwender zu verifizieren)
- **EU Better Regulation** der EU-Kommission

## Testakte

Zu diesem Plugin existiert eine vollstaendige Beispielakte unter [`testakten/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026/`](../testakten/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026/).

**Sachverhalt**: Referentenentwurf des BMJ vom 14.04.2026 zur Verbesserung der elektronischen Erreichbarkeit im Handelsregister eingetragener Gesellschaften (**ElErrHandRegG**). NKR-Pruefung ergibt: Regelung ist erforderlich, Ausgestaltung jedoch zu komplex; geschaetzter Erfuellungsaufwand 320 Mio EUR jaehrlich fuer die Wirtschaft. Stellungnahme weist die Notwendigkeit positiv aus, kritisiert die konkrete Ausgestaltung und schlaegt eine zentrale Loesung vor.

Die Akte zeigt sowohl die **mahnende** als auch die **konstruktive** Funktion des NKR.

## Quellenhygiene

- Keine erfundenen NKR-Stellungnahme-Aktenzeichen oder Berichte aus Modellwissen.
- NKRG und methodische Grundlagen werden mit Norm und Stand zitiert; NKR-Jahresberichte allgemein als "NKR-Jahresbericht <Jahr>".
- Vor Ausgabe stets Live-Quellen pruefen: [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de), BMI-Leitfaden, Bundesanzeiger.

## Installation

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install normenkontrollrat-nkr@claude-fuer-deutsches-recht
```

## Konversationsstil

Erste Antwort knapp. Maximal eine gezielte Rueckfrage zur Mandatsaufnahme. Sofort in den Pruefraster-Modus uebergehen und einen ersten Stellungnahme-Entwurf liefern, sobald Eckdaten vorliegen. Subsumtion und ausfuehrliche Begruendung nur dort, wo der Skill dies ausdruecklich vorsieht (Erforderlichkeit, Verhaeltnismaessigkeit, Alternativenpruefung).

## Verwandte Plugins

- [`legistik-werkstatt`](../legistik-werkstatt/) — Drafting-Werkstatt fuer Referenten- und Kabinettsentwuerfe (Ressortsicht; NKR ist der Pruefer dieser Entwuerfe).
- [`normenkontrolle-bauleitplanung`](../normenkontrolle-bauleitplanung/) — Anfechtung von Bauleitplaenen nach § 47 VwGO (begriffliche Verwandtschaft, nicht inhaltlich).
- [`buerokratieversteher-entbuerokratisierer`](../buerokratieversteher-entbuerokratisierer/) — operative Entbuerokratisierung in einzelnen Verfahren.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg in das Normenkontrollrat-NKR-Plugin: Triage von Gesetzesvorhaben nach Erfüllungsaufwand, One-in-one-out, Digitalcheck, Befristung, Alternativenprüfung und Vollzugsfolgenabschätzung. Routet zum passenden Spezial-Skill und liefert... |
| `alternativen-keine-aufgabe-kompetenz` | Systematische Pruefung von Alternativen zur geplanten Regelung: Verzicht Selbstregulierung Brancheninitiative Empfehlung freiwillige Vereinbarung verbesserte Vollzugspraxis Verlaengerung bestehender Befristung. Liefert eine 5-Stufen-Hier... |
| `alternativen-keine-regelung-soft-law` | Systematische Pruefung von Alternativen zur geplanten Regelung: Verzicht Selbstregulierung Brancheninitiative Empfehlung freiwillige Vereinbarung verbesserte Vollzugspraxis Verlaengerung bestehender Befristung. Liefert eine 5-Stufen-Hier... |
| `aufgabe-und-kompetenz-nkrg` | Zeigt Aufgabe Zuständigkeit Unabhaengigkeit und Befassungspflichten des Nationalen Normenkontrollrats nach NKRG. Erklaert insbesondere § 1 Einsetzung beim BMJ § 2 Erfuellungsaufwand § 3 Zusammensetzung § 4 Pruefung § 6 Stellungnahme und... |
| `buerokratieabbau-katalog-buerokratiekosten-vs` | Katalog konkreter Buerokratieabbau-Vorschlaege als Standardrepertoire des NKR. Sammelt typische Entlastungsmuster (Schwellenwerte Once-Only Bagatell-Ausnahmen Stichproben statt Vollkontrolle digitale Verfahren Aufhebung redundanter Vorsc... |
| `buerokratieabbau-katalog-konkrete` | Katalog konkreter Buerokratieabbau-Vorschlaege als Standardrepertoire des NKR. Sammelt typische Entlastungsmuster (Schwellenwerte Once-Only Bagatell-Ausnahmen Stichproben statt Vollkontrolle digitale Verfahren Aufhebung redundanter Vorsc... |
| `buerokratiekosten-vs-erfuellungsaufwand` | Trennt den engen Begriff Buerokratiekosten von dem umfassenderen Begriff Erfuellungsaufwand. Beschreibt historische Entwicklung (SKM 2006 nur Informationspflichten; Ausweitung 2011) und zeigt Folgen für Pruefung Berichtswesen Vorblatt On... |
| `digital-anschlussfaehigkeit-digitalcheck` | Pruefskill Digitaltauglichkeit. Adressiert die seit 2022 geltende Pflicht zum Digitalcheck (Bundesregelungsvorhaben muessen digital praktikabel sein) und die OZG-Anschlussfaehigkeit. Mit Standardpruefraster Anschluss an bestehende Standa... |
| `digital-anschlussfaehigkeit-tauglich` | Pruefskill Digitaltauglichkeit. Adressiert die seit 2022 geltende Pflicht zum Digitalcheck (Bundesregelungsvorhaben muessen digital praktikabel sein) und die OZG-Anschlussfaehigkeit. Mit Standardpruefraster Anschluss an bestehende Standa... |
| `digitalcheck-und-onlinezugangsgesetz-ozg` | Fachmodul OZG und Digitalcheck. Beschreibt das Onlinezugangsgesetz die OZG-Leistungen den Portalverbund das Once-Only-Prinzip und die ab dem 1. Januar 2023 anwendbare Digitalcheck-Methodik nach § 4 Abs. 3 i.V.m. § 9 NKRG für Bundesregelu... |
| `einmalig-vs-erforderlichkeitspruefung-warum` | Trennscharfe Unterscheidung zwischen einmaligem Umstellungsaufwand und jaehrlich laufendem Erfuellungsaufwand. Erklaert Abgrenzung Grenzfaelle (mehrjaehriger Investitionszyklus IT-Refresh) Implikationen für Stellungnahme und One-in-one-o... |
| `einmalig-vs-jaehrlich-laufend` | Trennscharfe Unterscheidung zwischen einmaligem Umstellungsaufwand und jaehrlich laufendem Erfuellungsaufwand. Erklaert Abgrenzung Grenzfaelle (mehrjaehriger Investitionszyklus IT-Refresh) Implikationen für Stellungnahme und One-in-one-o... |
| `erforderlichkeitspruefung-warum` | Erforderlichkeitspruefung als erster Pruefschritt jeder NKR-Stellungnahme. Zwingt das Ressort zur Beantwortung der Grundfrage Warum ueberhaupt regeln. Liefert Pruefraster Marktversagen-Test Notwendigkeits-Test und Begruendungstiefe. Mit... |
| `erforderlichkeitspruefung-warum-ueberhaupt-regeln` | Erforderlichkeitspruefung als erster Pruefschritt jeder NKR-Stellungnahme. Zwingt das Ressort zur Beantwortung der Grundfrage Warum ueberhaupt regeln. Liefert Pruefraster Marktversagen-Test Notwendigkeits-Test und Begruendungstiefe. Mit... |
| `erfuellungsaufwand-buerger-grundbegriff` | Trennt den Erfuellungsaufwand methodisch nach den drei Adressatengruppen Buerger Wirtschaft Verwaltung. Erklaert Spezifika je Gruppe Standard-Zeitwerte Lohnsaetze Bandbreiten und die typischen Falltypen. Mit Mustertabelle für die Stellun... |
| `erfuellungsaufwand-buerger-wirtschaft` | Trennt den Erfuellungsaufwand methodisch nach den drei Adressatengruppen Buerger Wirtschaft Verwaltung. Erklaert Spezifika je Gruppe Standard-Zeitwerte Lohnsaetze Bandbreiten und die typischen Falltypen. Mit Mustertabelle für die Stellun... |
| `erfuellungsaufwand-grundbegriff` | Definiert den Grundbegriff Erfuellungsaufwand nach NKRG GGO § 44 und HdR. Trennt den Begriff von benachbarten Konzepten (Buerokratiekosten Vollzugskosten Haushaltskosten Folgekosten Sachkosten). Liefert die Standarddefinition wie sie in... |
| `eu-ebene-eu-richtlinien` | Verortet den NKR im europaeischen Better-Regulation-Kontext. Stellt Beruehrungspunkte zu EU-Richtlinien EU-Verordnungen Impact Assessments REFIT-Programm und dem Regulatory Scrutiny Board RSB der EU-Kommission dar. Zeigt wo der NKR bei d... |
| `eu-ebene-und-better-regulation` | Verortet den NKR im europaeischen Better-Regulation-Kontext. Stellt Beruehrungspunkte zu EU-Richtlinien EU-Verordnungen Impact Assessments REFIT-Programm und dem Regulatory Scrutiny Board RSB der EU-Kommission dar. Zeigt wo der NKR bei d... |
| `eu-richtlinien-umsetzung-und-goldplating` | Detailskill EU-Richtlinienumsetzung und Goldplating-Vermeidung. Beschreibt 1:1-Umsetzungsprinzip Pruefraster für Goldplating Delta-Berechnung und Bezug zur Better-Regulation-Methodik der EU-Kommission. Mit Pruef-Checkliste Mustertexten u... |
| `evaluation-jahresbericht-fallzahlen` | Beschreibt Evaluierungspraxis ex-post-Pruefung und Jahresbericht des NKR nach § 7 NKRG. Erklaert wie der NKR vergangene Stellungnahmen bilanziert wie er Trends im Buerokratiekostenstand identifiziert und wie der Jahresbericht politisch w... |
| `evaluation-und-jahresbericht` | Beschreibt Evaluierungspraxis ex-post-Pruefung und Jahresbericht des NKR nach § 7 NKRG. Erklaert wie der NKR vergangene Stellungnahmen bilanziert wie er Trends im Buerokratiekostenstand identifiziert und wie der Jahresbericht politisch w... |
| `evaluierung-befristung-sunset-klausel` | Praxis-Skill zur Empfehlung von Evaluierungsklauseln Befristungen und Sunset-Klauseln. Beschreibt wann der NKR welches Instrument empfiehlt welche Indikatoren noetig sind und wie die Klauseltechnik im Gesetzestext aussieht. Mit Klausel-V... |
| `evaluierung-befristung-verfahrensgang` | Praxis-Skill zur Empfehlung von Evaluierungsklauseln Befristungen und Sunset-Klauseln. Beschreibt wann der NKR welches Instrument empfiehlt welche Indikatoren noetig sind und wie die Klauseltechnik im Gesetzestext aussieht. Mit Klausel-V... |
| `fallzahlen-schaetzung-bandbreiten` | Methodischer Fachmodul für Schaetzungen mit Bandbreiten wenn keine harten Statistik-Daten vorliegen. Beschreibt Plausibilitaetsraster Sensitivitaetsanalyse Min-Max-Punkt-Schaetzung Dunkelzifferproblematik und Begruendungstiefe. Mit Muste... |
| `gleichstellungs-gendercheck-handelsregister` | Fachmodul Gleichstellungs- und Gendercheck nach § 1 BGleiG und § 2 GGO. Beschreibt die Pflicht zur geschlechterdifferenzierten Folgenabschaetzung wann ein Gendercheck zwingend ist und wie die NKR-Pruefung sich darauf bezieht. Mit Pruefra... |
| `gleichstellungs-und-gendercheck` | Fachmodul Gleichstellungs- und Gendercheck nach § 1 BGleiG und § 2 GGO. Beschreibt die Pflicht zur geschlechterdifferenzierten Folgenabschaetzung wann ein Gendercheck zwingend ist und wie die NKR-Pruefung sich darauf bezieht. Mit Pruefra... |
| `handelsregister-elektronische-zustellung` | Fachmodul für Vorhaben mit Handelsregister-Bezug und elektronischer Zustellung. Beschreibt die Schnittstellen HRG ZPO beA beBPO De-Mail eIDAS-Wallet und die typischen NKR-Pruefpunkte bei Handelsregister-Vorhaben (Fallzahlen rund 1.8 Mio... |
| `handelsregister-und-elektronische-zustellung` | Fachmodul für Vorhaben mit Handelsregister-Bezug und elektronischer Zustellung. Beschreibt die Schnittstellen HRG ZPO beA beBPO De-Mail eIDAS-Wallet und die typischen NKR-Pruefpunkte bei Handelsregister-Vorhaben (Fallzahlen rund 1.8 Mio... |
| `leitfaden-ermittlung` | Strukturierter Ueberblick ueber den Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR) als methodische Hauptgrundlage. Beschreibt Aufbau Kapitelstruktur die zwingenden Darstellungsformen im Vorblatt und in der B... |
| `leitfaden-ermittlung-und-darstellung` | Strukturierter Ueberblick ueber den Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR) als methodische Hauptgrundlage. Beschreibt Aufbau Kapitelstruktur die zwingenden Darstellungsformen im Vorblatt und in der B... |
| `mittelstandsfreundlichkeit-kmu-test` | KMU-Test (Small and Medium Enterprises Test) als Standardelement des NKR-Pruefrasters. Erklaert KMU-Definition Schwellenwerte differenzierte Aufwandsschaetzung und typische Entlastungsinstrumente (Ausnahmen Schwellen Uebergangsregelungen... |
| `nachhaltigkeit-klimacheck-one` | Fachmodul Nachhaltigkeitspruefung und Klimacheck. Beschreibt die Nachhaltigkeitspruefung der Bundesregierung im Sinne der Deutschen Nachhaltigkeitsstrategie und der SDG sowie den Klimacheck (CO2-Wirkung neuer Regelungen). Erlaeutert wo d... |
| `nachhaltigkeit-klimacheck-vereinbarkeit` | Fachmodul Nachhaltigkeitspruefung und Klimacheck. Beschreibt die Nachhaltigkeitspruefung der Bundesregierung im Sinne der Deutschen Nachhaltigkeitsstrategie und der SDG sowie den Klimacheck (CO2-Wirkung neuer Regelungen). Erlaeutert wo d... |
| `one-in-one-out-bilanz-und-buchung` | One-in-one-out-Regel der Bundesregierung 2015 als Standardpruefelement. Erklaert die Bilanzierung jaehrlich laufender Buerokratie-Belastungen für die Wirtschaft die Entlastungs-Nachweispflicht den Saldo-Zaehler pro Ressort die Behandlung... |
| `one-in-out-bilanz-und-buchung` | One-in-one-out-Regel der Bundesregierung 2015 als Standardpruefelement. Erklaert die Bilanzierung jaehrlich laufender Buerokratie-Belastungen für die Wirtschaft die Entlastungs-Nachweispflicht den Saldo-Zaehler pro Ressort die Behandlung... |
| `orientierung-mandatsaufnahme-praktikabilitaet` | Einstiegs-Skill für NKR-Pruefauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welchem... |
| `orientierung-und-mandatsaufnahme` | Einstiegs-Skill für NKR-Pruefauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welchem... |
| `praktikabilitaet-vollzug-test` | Praktikabilitaetstest für den Vollzug. Prueft ob die Regelung von Behörden und Adressaten ueberhaupt leistbar ist. Faktoren Personalbedarf IT-Voraussetzungen Datenverfuegbarkeit Schulungserfordernisse Vollzugskaskaden Konnexitaet Konflik... |
| `pruefumfang-was-prueft-der-nicht` | Negativabgrenzung des NKR-Pruefumfangs. Erklaert was der NKR ausdruecklich nicht prueft (politische Zielwahl Verfassungsmaessigkeit Haushaltsfolgen) und was er sehr wohl prueft (Methodik Erfuellungsaufwand Praktikabilitaet Digitaltauglic... |
| `pruefumfang-was-standardkostenmodell-skm` | Negativabgrenzung des NKR-Pruefumfangs. Erklaert was der NKR ausdruecklich nicht prueft (politische Zielwahl Verfassungsmaessigkeit Haushaltsfolgen) und was er sehr wohl prueft (Methodik Erfuellungsaufwand Praktikabilitaet Digitaltauglic... |
| `standardkostenmodell-skm` | Beschreibt das Standardkostenmodell SKM als methodischen Kern der Erfuellungsaufwandsberechnung. Erklaert die Standardformel Aufwand pro Fall × Fallzahl Bandbreiten Komplexitaetsfaktoren Bezug auf DESTATIS-Lohnsaetze und Dokumentationsan... |
| `stellungnahme-aufbau-ergebnis` | Standardaufbau und Format einer NKR-Stellungnahme nach § 6 NKRG. Beschreibt die typische Gliederung Briefkopf Vorhabens-Identifikation Grundsatzfeststellung methodische Bewertung Empfehlungen Ergebnis-Bewertung Hinweise sowie typische La... |
| `stellungnahme-aufbau-und-format` | Standardaufbau und Format einer NKR-Stellungnahme nach § 6 NKRG. Beschreibt die typische Gliederung Briefkopf Vorhabens-Identifikation Grundsatzfeststellung methodische Bewertung Empfehlungen Ergebnis-Bewertung Hinweise sowie typische La... |
| `stellungnahme-ergebnis-und-empfehlung` | Schreibt den Schlussteil einer NKR-Stellungnahme. Drei Bausteine: (1) konkrete Empfehlungen nummeriert (2) Ergebnisformel im NKR-Standardvokabular (keine Einwaende / Einwaende / Bemerkungen) (3) Hinweise und Vorbehalte. Mit Vorlagen Eska... |
| `stellungnahme-evaluationsklausel` | Fachmodul für den NKR-Empfehlungs-Baustein Evaluierungsklausel. Liefert Vorlage Klausel-Text Indikatorliste Frist-Vorschlag Berichtsadressat Konkretisierung der Pflichten und Standard-Argumentation warum die Klausel noetig ist. Mit konkr... |
| `stellungnahme-formulierungshilfe-vs` | Behandlung von Formulierungshilfen der Bundesregierung an Koalitionsfraktionen im Vergleich zu Referentenentwuerfen. Beschreibt die Umgehungsproblematik die faktische NKR-Befassung die methodischen Besonderheiten der Formulierungshilfe (... |
| `stellungnahme-formulierungshilfe-vs-referentenentwurf` | Behandlung von Formulierungshilfen der Bundesregierung an Koalitionsfraktionen im Vergleich zu Referentenentwuerfen. Beschreibt die Umgehungsproblematik die faktische NKR-Befassung die methodischen Besonderheiten der Formulierungshilfe (... |
| `stellungnahme-grundsatzfeststellung` | Schreibt den Eingangsabschnitt Grundsatzfeststellung einer NKR-Stellungnahme. Drei Saetze: (1) Was will das Vorhaben (2) Position zur Erforderlichkeit (3) Position zur Ausgestaltung. Mit Standardformeln Tonalitaet Verbindlichkeit und typ... |
| `stellungnahme-mahnender-charakter-grenzen` | Beschaeftigt sich mit dem mahnenden Charakter der NKR-Stellungnahme und ihren Grenzen. Wann darf der NKR mahnen wann sollte er konstruktiv bleiben wann hat die Mahnung politische Wirkung wo verlaeuft die rote Linie zur politischen Bewert... |
| `stellungnahme-pressepolitik-bundestag` | Verzahnt einzelne NKR-Stellungnahmen mit der öffentlichen Wirksamkeit ueber Jahresbericht Pressemitteilung Hintergrundgespraech und Bilanz-Konferenz. Beschreibt wie der NKR seine Mahnungen oeffentlich verstaerken kann ohne politisch zu w... |
| `stellungnahme-pressepolitik-jahresbericht` | Verzahnt einzelne NKR-Stellungnahmen mit der öffentlichen Wirksamkeit ueber Jahresbericht Pressemitteilung Hintergrundgespraech und Bilanz-Konferenz. Beschreibt wie der NKR seine Mahnungen oeffentlich verstaerken kann ohne politisch zu w... |
| `stellungnahme-zum-bundestag-anhoerung` | Vorbereitung einer Anhörung im federfuehrenden Ausschuss des Bundestages. Beschreibt typische Anhörungssituation NKR-Vertretung muendliche Eingangsaussage Vorbereitung Folienpaket Antworten auf Abgeordnetenfragen und Folge-Stellungnahme.... |
| `verfahrensgang-referentenentwurf` | Skizziert den Verfahrensgang eines Vorhabens von der Ressortidee ueber Referentenentwurf Ressortabstimmung NKR-Befassung Länder- und Verbaendeanhoerung Kabinett Bundesrat Bundestag und Verkuendung mit den jeweiligen NKR-Andockpunkten und... |
| `verfahrensgang-referentenentwurf-bis-bundestag` | Skizziert den Verfahrensgang eines Vorhabens von der Ressortidee ueber Referentenentwurf Ressortabstimmung NKR-Befassung Länder- und Verbaendeanhoerung Kabinett Bundesrat Bundestag und Verkuendung mit den jeweiligen NKR-Andockpunkten und... |
| `verhaeltnismaessigkeit-aus-sicht` | Verhaeltnismaessigkeit aus NKR-Sicht: keine grundrechtliche Pruefung sondern Kosten-Nutzen- und Eingriffstiefe-Pruefung. Erklaert wie der NKR die drei klassischen Stufen Geeignetheit Erforderlichkeit Angemessenheit auf Erfuellungsaufwand... |
| `verhaeltnismaessigkeit-sicht-zeitwerttabelle` | Verhaeltnismaessigkeit aus NKR-Sicht: keine grundrechtliche Pruefung sondern Kosten-Nutzen- und Eingriffstiefe-Pruefung. Erklaert wie der NKR die drei klassischen Stufen Geeignetheit Erforderlichkeit Angemessenheit auf Erfuellungsaufwand... |
| `zeitwerttabelle-und-fallzahlen` | Praxisleitfaden zu Zeitwerttabellen und Fallzahlenermittlung. Zeigt die Struktur der Leitfaden-Zeitwerttabelle die Komplexitaetsstufen die Standard-Lohnsaetze DESTATIS-Quellen die Datenwege zur Fallzahlenermittlung und die typischen Quel... |
| `zusammenarbeit-bundesregierung` | Zusammenarbeit Bundesregierung im Plugin Normenkontrollrat Nkr im Normenkontrollrat Nkr. |
| `zusammenarbeit-bundesregierung-ressorts` | Verhaltens-Skill für die taegliche Zusammenarbeit zwischen NKR-Sekretariat und Ressorts. Beschreibt informelle Vorklaerungen Datenanforderungen § 5 NKRG Eskalationsstufen Konfliktbewaeltigung Dialog mit dem federfuehrenden Referat und Sc... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
