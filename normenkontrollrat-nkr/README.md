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

Automatisch generierte Komplett-Liste aller 37 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `nkr-alternativen-pruefung-keine-regelung-soft-law` | Systematische Pruefung von Alternativen zur geplanten Regelung: Verzicht Selbstregulierung Brancheninitiative Empfehlung freiwillige Vereinbarung verbesserte Vollzugspraxis Verlaengerung bestehender Befristung. Liefert eine 5-Stufen-Hier... |
| `nkr-aufgabe-und-kompetenz-nkrg` | Zeigt Aufgabe Zustaendigkeit Unabhaengigkeit und Befassungspflichten des Nationalen Normenkontrollrats nach NKRG. Erklaert insbesondere § 1 Einsetzung beim BMJ § 2 Erfuellungsaufwand § 3 Zusammensetzung § 4 Pruefung § 6 Stellungnahme und... |
| `nkr-buerokratieabbau-katalog-konkrete-vorschlaege` | Katalog konkreter Buerokratieabbau-Vorschlaege als Standardrepertoire des NKR. Sammelt typische Entlastungsmuster (Schwellenwerte Once-Only Bagatell-Ausnahmen Stichproben statt Vollkontrolle digitale Verfahren Aufhebung redundanter Vorsc... |
| `nkr-buerokratiekosten-vs-erfuellungsaufwand` | Trennt den engen Begriff Buerokratiekosten von dem umfassenderen Begriff Erfuellungsaufwand. Beschreibt historische Entwicklung (SKM 2006 nur Informationspflichten; Ausweitung 2011) und zeigt Folgen fuer Pruefung Berichtswesen Vorblatt O... |
| `nkr-digital-anschlussfaehigkeit-tauglich` | Pruefskill Digitaltauglichkeit. Adressiert die seit 2022 geltende Pflicht zum Digitalcheck (Bundesregelungsvorhaben muessen digital praktikabel sein) und die OZG-Anschlussfaehigkeit. Mit Standardpruefraster Anschluss an bestehende Standa... |
| `nkr-digitalcheck-und-onlinezugangsgesetz-ozg` | Spezialskill OZG und Digitalcheck. Beschreibt das Onlinezugangsgesetz die OZG-Leistungen den Portalverbund das Once-Only-Prinzip und die ab dem 1. Januar 2023 anwendbare Digitalcheck-Methodik nach § 4 Abs. 3 i.V.m. § 9 NKRG fuer Bundesre... |
| `nkr-einmalig-vs-jaehrlich-laufend` | Trennscharfe Unterscheidung zwischen einmaligem Umstellungsaufwand und jaehrlich laufendem Erfuellungsaufwand. Erklaert Abgrenzung Grenzfaelle (mehrjaehriger Investitionszyklus IT-Refresh) Implikationen fuer Stellungnahme und One-in-one-... |
| `nkr-erforderlichkeitspruefung-warum-ueberhaupt-regeln` | Erforderlichkeitspruefung als erster Pruefschritt jeder NKR-Stellungnahme. Zwingt das Ressort zur Beantwortung der Grundfrage Warum ueberhaupt regeln. Liefert Pruefraster Marktversagen-Test Notwendigkeits-Test und Begruendungstiefe. Mit... |
| `nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung` | Trennt den Erfuellungsaufwand methodisch nach den drei Adressatengruppen Buerger Wirtschaft Verwaltung. Erklaert Spezifika je Gruppe Standard-Zeitwerte Lohnsaetze Bandbreiten und die typischen Falltypen. Mit Mustertabelle fuer die Stellu... |
| `nkr-erfuellungsaufwand-grundbegriff` | Definiert den Grundbegriff Erfuellungsaufwand nach NKRG GGO § 44 und HdR. Trennt den Begriff von benachbarten Konzepten (Buerokratiekosten Vollzugskosten Haushaltskosten Folgekosten Sachkosten). Liefert die Standarddefinition wie sie in... |
| `nkr-eu-ebene-und-better-regulation` | Verortet den NKR im europaeischen Better-Regulation-Kontext. Stellt Beruehrungspunkte zu EU-Richtlinien EU-Verordnungen Impact Assessments REFIT-Programm und dem Regulatory Scrutiny Board RSB der EU-Kommission dar. Zeigt wo der NKR bei d... |
| `nkr-eu-richtlinien-umsetzung-und-goldplating` | Detailskill EU-Richtlinienumsetzung und Goldplating-Vermeidung. Beschreibt 1:1-Umsetzungsprinzip Pruefraster fuer Goldplating Delta-Berechnung und Bezug zur Better-Regulation-Methodik der EU-Kommission. Mit Pruef-Checkliste Mustertexten... |
| `nkr-evaluation-und-jahresbericht` | Beschreibt Evaluierungspraxis ex-post-Pruefung und Jahresbericht des NKR nach § 7 NKRG. Erklaert wie der NKR vergangene Stellungnahmen bilanziert wie er Trends im Buerokratiekostenstand identifiziert und wie der Jahresbericht politisch w... |
| `nkr-evaluierung-befristung-sunset-klausel` | Praxis-Skill zur Empfehlung von Evaluierungsklauseln Befristungen und Sunset-Klauseln. Beschreibt wann der NKR welches Instrument empfiehlt welche Indikatoren noetig sind und wie die Klauseltechnik im Gesetzestext aussieht. Mit Klausel-V... |
| `nkr-fallzahlen-schaetzung-bandbreiten` | Methodischer Spezial-Skill fuer Schaetzungen mit Bandbreiten wenn keine harten Statistik-Daten vorliegen. Beschreibt Plausibilitaetsraster Sensitivitaetsanalyse Min-Max-Punkt-Schaetzung Dunkelzifferproblematik und Begruendungstiefe. Mit... |
| `nkr-gleichstellungs-und-gendercheck` | Spezialskill Gleichstellungs- und Gendercheck nach § 1 BGleiG und § 2 GGO. Beschreibt die Pflicht zur geschlechterdifferenzierten Folgenabschaetzung wann ein Gendercheck zwingend ist und wie die NKR-Pruefung sich darauf bezieht. Mit Prue... |
| `nkr-handelsregister-und-elektronische-zustellung` | Spezialskill fuer Vorhaben mit Handelsregister-Bezug und elektronischer Zustellung. Beschreibt die Schnittstellen HRG ZPO beA beBPO De-Mail eIDAS-Wallet und die typischen NKR-Pruefpunkte bei Handelsregister-Vorhaben (Fallzahlen rund 1.8... |
| `nkr-leitfaden-ermittlung-und-darstellung` | Strukturierter Ueberblick ueber den Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR) als methodische Hauptgrundlage. Beschreibt Aufbau Kapitelstruktur die zwingenden Darstellungsformen im Vorblatt und in der B... |
| `nkr-mittelstandsfreundlichkeit-kmu-test` | KMU-Test (Small and Medium Enterprises Test) als Standardelement des NKR-Pruefrasters. Erklaert KMU-Definition Schwellenwerte differenzierte Aufwandsschaetzung und typische Entlastungsinstrumente (Ausnahmen Schwellen Uebergangsregelungen... |
| `nkr-nachhaltigkeit-klimacheck-und-vereinbarkeit` | Spezialskill Nachhaltigkeitspruefung und Klimacheck. Beschreibt die Nachhaltigkeitspruefung der Bundesregierung im Sinne der Deutschen Nachhaltigkeitsstrategie und der SDG sowie den Klimacheck (CO2-Wirkung neuer Regelungen). Erlaeutert w... |
| `nkr-one-in-one-out-bilanz-und-buchung` | One-in-one-out-Regel der Bundesregierung 2015 als Standardpruefelement. Erklaert die Bilanzierung jaehrlich laufender Buerokratie-Belastungen fuer die Wirtschaft die Entlastungs-Nachweispflicht den Saldo-Zaehler pro Ressort die Behandlun... |
| `nkr-orientierung-und-mandatsaufnahme` | Einstiegs-Skill fuer NKR-Pruefauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welche... |
| `nkr-praktikabilitaet-vollzug-test` | Praktikabilitaetstest fuer den Vollzug. Prueft ob die Regelung von Behoerden und Adressaten ueberhaupt leistbar ist. Faktoren Personalbedarf IT-Voraussetzungen Datenverfuegbarkeit Schulungserfordernisse Vollzugskaskaden Konnexitaet Konfl... |
| `nkr-pruefumfang-was-prueft-der-nkr-nicht` | Negativabgrenzung des NKR-Pruefumfangs. Erklaert was der NKR ausdruecklich nicht prueft (politische Zielwahl Verfassungsmaessigkeit Haushaltsfolgen) und was er sehr wohl prueft (Methodik Erfuellungsaufwand Praktikabilitaet Digitaltauglic... |
| `nkr-standardkostenmodell-skm` | Beschreibt das Standardkostenmodell SKM als methodischen Kern der Erfuellungsaufwandsberechnung. Erklaert die Standardformel Aufwand pro Fall × Fallzahl Bandbreiten Komplexitaetsfaktoren Bezug auf DESTATIS-Lohnsaetze und Dokumentationsan... |
| `nkr-stellungnahme-aufbau-und-format` | Standardaufbau und Format einer NKR-Stellungnahme nach § 6 NKRG. Beschreibt die typische Gliederung Briefkopf Vorhabens-Identifikation Grundsatzfeststellung methodische Bewertung Empfehlungen Ergebnis-Bewertung Hinweise sowie typische La... |
| `nkr-stellungnahme-ergebnis-und-empfehlung` | Schreibt den Schlussteil einer NKR-Stellungnahme. Drei Bausteine: (1) konkrete Empfehlungen nummeriert (2) Ergebnisformel im NKR-Standardvokabular (keine Einwaende / Einwaende / Bemerkungen) (3) Hinweise und Vorbehalte. Mit Vorlagen Eska... |
| `nkr-stellungnahme-evaluationsklausel-vorschlag` | Spezialskill fuer den NKR-Empfehlungs-Baustein Evaluierungsklausel. Liefert Vorlage Klausel-Text Indikatorliste Frist-Vorschlag Berichtsadressat Konkretisierung der Pflichten und Standard-Argumentation warum die Klausel noetig ist. Mit k... |
| `nkr-stellungnahme-formulierungshilfe-vs-referentenentwurf` | Behandlung von Formulierungshilfen der Bundesregierung an Koalitionsfraktionen im Vergleich zu Referentenentwuerfen. Beschreibt die Umgehungsproblematik die faktische NKR-Befassung die methodischen Besonderheiten der Formulierungshilfe (... |
| `nkr-stellungnahme-grundsatzfeststellung` | Schreibt den Eingangsabschnitt Grundsatzfeststellung einer NKR-Stellungnahme. Drei Saetze: (1) Was will das Vorhaben (2) Position zur Erforderlichkeit (3) Position zur Ausgestaltung. Mit Standardformeln Tonalitaet Verbindlichkeit und typ... |
| `nkr-stellungnahme-mahnender-charakter-grenzen` | Beschaeftigt sich mit dem mahnenden Charakter der NKR-Stellungnahme und ihren Grenzen. Wann darf der NKR mahnen wann sollte er konstruktiv bleiben wann hat die Mahnung politische Wirkung wo verlaeuft die rote Linie zur politischen Bewert... |
| `nkr-stellungnahme-pressepolitik-und-jahresbericht` | Verzahnt einzelne NKR-Stellungnahmen mit der oeffentlichen Wirksamkeit ueber Jahresbericht Pressemitteilung Hintergrundgespraech und Bilanz-Konferenz. Beschreibt wie der NKR seine Mahnungen oeffentlich verstaerken kann ohne politisch zu... |
| `nkr-stellungnahme-zum-bundestag-anhoerung` | Vorbereitung einer Anhoerung im federfuehrenden Ausschuss des Bundestages. Beschreibt typische Anhoerungssituation NKR-Vertretung muendliche Eingangsaussage Vorbereitung Folienpaket Antworten auf Abgeordnetenfragen und Folge-Stellungnahm... |
| `nkr-verfahrensgang-referentenentwurf-bis-bundestag` | Skizziert den Verfahrensgang eines Vorhabens von der Ressortidee ueber Referentenentwurf Ressortabstimmung NKR-Befassung Laender- und Verbaendeanhoerung Kabinett Bundesrat Bundestag und Verkuendung mit den jeweiligen NKR-Andockpunkten un... |
| `nkr-verhaeltnismaessigkeit-aus-nkr-sicht` | Verhaeltnismaessigkeit aus NKR-Sicht: keine grundrechtliche Pruefung sondern Kosten-Nutzen- und Eingriffstiefe-Pruefung. Erklaert wie der NKR die drei klassischen Stufen Geeignetheit Erforderlichkeit Angemessenheit auf Erfuellungsaufwand... |
| `nkr-zeitwerttabelle-und-fallzahlen` | Praxisleitfaden zu Zeitwerttabellen und Fallzahlenermittlung. Zeigt die Struktur der Leitfaden-Zeitwerttabelle die Komplexitaetsstufen die Standard-Lohnsaetze DESTATIS-Quellen die Datenwege zur Fallzahlenermittlung und die typischen Quel... |
| `nkr-zusammenarbeit-mit-bundesregierung-und-ressorts` | Verhaltens-Skill fuer die taegliche Zusammenarbeit zwischen NKR-Sekretariat und Ressorts. Beschreibt informelle Vorklaerungen Datenanforderungen § 5 NKRG Eskalationsstufen Konfliktbewaeltigung Dialog mit dem federfuehrenden Referat und S... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
