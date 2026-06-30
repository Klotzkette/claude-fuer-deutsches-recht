# DFG-Förderantrag

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

DFG-Förderantragssteller für Sachbeihilfe, adaptive Anfänger-/Profi-Führung, kleine schnelle Anträge, große Koselleck-Strategien, elan-Formalia, Finanzplan, Reviewer-Red-Team, Forschungsdaten, KI-/Ethik-Check und Wiedereinreichung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`dfg-foerderantrag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dfg-foerderantrag.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/dfg-foerderantrag/dfg-foerderantrag-werkstatt.md" download><code>dfg-foerderantrag-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/dfg-foerderantrag/dfg-foerderantrag-schnellstart.md" download><code>dfg-foerderantrag-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Plugin für die praktische Antragstellung bei der Deutschen Forschungsgemeinschaft: Sachbeihilfe, elan-Formalia, Projektbeschreibung, Finanzplan, Forschungsdaten, Ethik-/KI-Check, Reviewer-Perspektive, Wiedereinreichung und strategische Entscheidung zwischen kleinem schnellen Antrag und großem Prestigeprojekt.

Der Stil ist bewusst nicht bürokratisch. Das Plugin fragt zuerst: Was ist wissenschaftlich stark, was ist realistisch förderbar, was kann schneller entschieden werden und wo ist der große Antrag zwar verführerisch, aber prozessual zäher? Es arbeitet adaptiv: Anfänger bekommen eine geführte Mini-Roadmap; erfahrene Antragsteller bekommen direkt Red-Team, Kürzungsrisiko und Programmstrategie.

## Quellen-Gate

Vor jeder belastbaren Ausgabe aktuelle DFG-Seiten prüfen:

- DFG Sachbeihilfe: themenoffene Einzelförderung, Neuanträge jederzeit, Fortsetzungsanträge spätestens 6 Monate vor Mittelverbrauch.
- DFG Begutachtung: grundsätzlich zwei Gutachten; bei Anträgen bis 200.000 Euro kann ausnahmsweise ein aussagekräftiges externes Gutachten reichen.
- Reinhart-Koselleck-Projekte: 500.000 bis 1,25 Mio. Euro für fünf Jahre in Stufen von 250.000 Euro; nur für herausragende, besonders innovative oder risikobehaftete Projekte, die nicht in normale Verfahren passen.
- DFG-Merkblätter, elan-Vorlagen, fachzuständige Ansprechpersonen und aktuelle Vordruckstände immer live gegen `dfg.de` prüfen.

## Schnellstart

```text
/dfg-foerderantrag:allgemein
```

Der Allgemein-Skill führt in 60 Sekunden durch: Forschungsfrage, Förderprogramm, Summe, Tempo, Zielgruppe der Begutachtung, Vorarbeiten, Risiken, Daten-/Ethikthemen und gewünschtes Ergebnis.

Typische Startpunkte:

| Situation | Start |
| --- | --- |
| "Ich habe nur eine Forschungsidee" | `dfg-foerderantrag-allgemein` → Mini-Roadmap und Minimalprojekt |
| "Sachbeihilfe oder größer?" | `dfg-foerderstrategie-schnell-oder-gross` |
| "Entwurf liegt vor" | `dfg-reviewer-red-team` → danach Text- und Finanzskills |
| "Ablehnung liegt vor" | `dfg-wiedereinreichung-nach-ablehnung` |

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `dfg-foerderantrag-allgemein` | Einstieg, Triage, Programmroute und erster Arbeitsplan |
| `dfg-foerderstrategie-schnell-oder-gross` | Entscheidung: kleiner schneller Antrag, normale Sachbeihilfe, Koselleck oder anderes Programm |
| `dfg-sachbeihilfe-elan-formalia` | Sachbeihilfe, elan, Anlagen, Vordrucklogik, formales Gate |
| `dfg-bis-200k-begutachtung-light` | Kleine/mittlere Anträge so bauen, dass sie schnell, klar und begutachtbar sind |
| `dfg-koselleck-500k-125m` | Koselleck-Check: 500.000 bis 1,25 Mio. Euro, Risiko, Profil, Vertrauensvorschuss |
| `dfg-projektbeschreibung-arbeitsprogramm` | Forschungsfrage, Stand der Forschung, Ziele, Arbeitspakete, Meilensteine |
| `dfg-finanzplan-module-personal-geraete` | Personal, Geräte, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Budgetbegründung |
| `dfg-reviewer-red-team` | Gutachterperspektive, Angriffsflächen, Kürzungsrisiken, Ablehnungsgründe |
| `dfg-wiedereinreichung-nach-ablehnung` | Ablehnung auswerten, Gutachten ernst nehmen, Neuaufstellung |
| `dfg-ki-ethik-forschungsdaten` | KI-Nutzung, Vertraulichkeit, Forschungsdatenmanagement, Ethik und Datenschutz |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 84 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `adaptive-dokumentenmatrix-lueckenliste` | Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustell... |
| `adaptive-dokumentenmatrix-und-lueckenliste` | Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `anfaenger-antraege-dfg` | Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `anfaenger-risikoampel-gegenargumente` | Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `anschluss-routing` | Anschluss-Routing für DFG-Förderantrag: wählt den nächsten Spezial-Skill nach Engpass (Antragsfrist Ausschreibungstermin, Projektbeschreibung, Finanzierungsplan, Lebenslauf), dokumentiert Router-Entscheidung mit Begründung. |
| `antraege-zahlen-schwellen-und-berechnung` | Antraege: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `antraege-zahlen-schwellenwerte-berechnung` | Antraege: Zahlen, Schwellenwerte und Berechnung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwe... |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Bereich dfg-foerderantrag: aktenbasierter Arbeitsgang mit Tatsachen-/Belegmatrix, Fristen- und Formcheck, passenden Fachankern, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `dfg-bis-200k-begutachtung-light` | Kleine und mittlere DFG-Anträge bis 200.000 Euro begutachtungsfreundlich bauen: klare Kernfrage, schlanker Finanzplan, ein Gutachten möglich, schnelle Lesbarkeit, Fortsetzungsfähigkeit. |
| `dfg-eigenanteil-und-grundausstattung` | Eigenanteil und Grundausstattung der Hochschule sauber von DFG-Förderung abgrenzen: Was muss die Hochschule stellen (Buero, Standardrechner, Sekretariat, Bibliothek), was darf die DFG finanzieren (projektspezifische Geraete, Personal ueb... |
| `dfg-eigene-vorarbeiten-darstellen` | Eigene Vorarbeiten in DFG-Antrag richtig darstellen: bisher publizierte Ergebnisse, eigene Methodik-Beitraege, Pilotdaten. Reviewer-Perspektive: Anknuepfungsfaehigkeit prüfen, keine Selbstplagiat-Prüfung. Mustertext für 2-Seiten-Kapitel. |
| `dfg-erstantragsteller-besondere-checks` | Erstantragsteller-Spezialcheck: Promotion abgeschlossen, gute eigene Vorarbeit (Publikationen Erst- und Letztautor), Anbindung an erfahrene Person ohne Co-Antragstellung wenn moeglich, Lebenslauf mit Eltern- und Pflegezeiten transparent,... |
| `dfg-erstpruefung-und-mandatsziel` | DFG: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `dfg-finanzplan-module-personal-geraete` | DFG-Finanzplan und Modulbegründung erstellen: Personal, Geräte, Verbrauchsmittel, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Öffentlichkeitsarbeit, Kostenlogik und Kürzungsabwehr. |
| `dfg-foerderstrategie-schnell-oder-gross` | Strategischer DFG-Router: entscheidet zwischen kleiner schneller Sachbeihilfe, normalem Antrag über 200.000 Euro, Koselleck ab 500.000 Euro oder anderem DFG-Programm. Enthält Spatz-in-der-Hand-Logik, Kürzungsrisiko, Begutachtungsdichte u... |
| `dfg-grossgeraete-und-cluster-antrag` | Grossgeraete und Cluster-Geraete in DFG-Antrag: Geraete ab 50.000 Euro mit zusaetzlicher Wirtschaftlichkeit, Auslastungsplan, technische Anschlussbedingungen, Wartungsvertrag, Folgekosten. Eigene Geraetekommission der DFG. Prüfraster für... |
| `dfg-grundsystem-foerderlinien` | Grundsystem der DFG-Foerderlinien einfuehrend erklaeren: Sachbeihilfe (Einzelantrag), Emmy Noether, Heisenberg, Reinhart Koselleck, SFB, GRK, Forschergruppen, Schwerpunktprogramme. Pro Linie: Zielgruppe, Hoehe, Dauer, Antragsweg, Begutac... |
| `dfg-internationale-kooperation-aufbau` | Internationale Kooperation in DFG-Antrag aufbauen: D-A-CH-Lead-Agency-Verfahren (DACH, SNF, FWF), Bilateral mit DFG-Partnerorganisationen (NSF, JSPS, ISF, NSFC). Kooperationszusagen, Mittelverteilung, Hauptantragsteller, Co-Antragsteller... |
| `dfg-ki-ethik-forschungsdaten` | DFG-Antrag auf KI-Nutzung, Ethik, Datenschutz, Forschungsdatenmanagement und gute wissenschaftliche Praxis prüfen. Behandelt Vertraulichkeit in Begutachtung, Datenmanagementplan, sensible Daten, Open Access und Nachnutzung. |
| `dfg-kollegen-review-organisieren` | Kollegen-Review eines DFG-Antrags strukturiert organisieren: 2 erfahrene Profs aus dem Fach plus 1 Methodik-Kollege, Briefing-Mail, Review-Raster (Originalitaet, Arbeitsprogramm, Finanzplan, Vorarbeiten), 1-Wochen-Frist. Output Vorlage B... |
| `dfg-koselleck-500k-125m` | Reinhart-Koselleck-Projekt prüfen und entwerfen: 500.000 Euro bis 1.250.000 Euro, 5 Jahre, Stufen von 250.000 Euro, außergewöhnliches Profil, positives Risiko, Vertrauensvorschuss, Abgrenzung zur Sachbeihilfe. |
| `dfg-koselleck-500k-praeregistrierung` | Reinhart-Koselleck-Projekt prüfen und entwerfen: 500.000 Euro bis 1.250.000 Euro, 5 Jahre, Stufen von 250.000 Euro, außergewöhnliches Profil, positives Risiko, Vertrauensvorschuss, Abgrenzung zur Sachbeihilfe im DFG-Förderantrag. |
| `dfg-praeregistrierung-replication-studies` | Praeregistrierung und Replikationsstudien im DFG-Antrag: Hypothesen ex ante festlegen, registered reports, OSF-Praeregistrierung, Replikationsplaene als eigenstaendiges Vorhaben. DFG-Statement to scientific integrity. Vorteile für Review... |
| `dfg-projektbeschreibung-arbeitsprogramm` | DFG-Projektbeschreibung und Arbeitsprogramm ausarbeiten: Forschungslücke, Stand der Forschung, Ziele, Hypothesen, Methoden, Arbeitspakete, Meilensteine, Risiken, Forschungsdaten und verwertbare Antragssprache. |
| `dfg-publikationsstrategie-projekt` | Publikationsstrategie für das beantragte Projekt: realistische Zahl Publikationen, geplante Zeitschriften mit Impact und Open-Access-Status, DFG-Open-Access-Politik, Praeprints, Datenpublikation. Im Antrag muss Publikationsplan zu Arbeit... |
| `dfg-replikationskrise-statistik-spezial` | Spezialfall Statistikabschnitt nach Replikationskrise: a-priori-Power-Analyse, Effektgroessenschaetzung, Vorab-Festlegung Hypothesen, Korrektur für multiple Testung, Sensitivitaetsanalysen. Prüfraster für Reviewer-Akzeptanz. |
| `dfg-reviewer-red-team` | DFG-Antrag aus Gutachterperspektive red-teamen: Originalität, Machbarkeit, Arbeitsprogramm, Qualifikation, Umfeld, Bias-Risiken, Kürzungsargumente, Ablehnungsrisiken und Verbesserungsplan. |
| `dfg-sachbeihilfe-elan-formalia` | DFG-Sachbeihilfe und elan-Formalia prüfen: Antragsberechtigung, Module, Vordrucke, Anlagen, Seitenlogik, Fachzuordnung, Fortsetzungsantrag, internationale Kooperation, formale Einreichungsreife. |
| `dfg-software-veroeffentlichung-spezial` | Spezialfall Software als Forschungsergebnis: DFG-Hinweise zur Open-Source-Veroeffentlichung, Lizenzwahl (MIT, BSD, Apache-2.0, GPL), Zenodo-DOI, Reproducibility. Prüfraster und Mustertext für Software-Sektion im Arbeitsprogramm. |
| `dfg-software-veroeffentlichung-tieforschung` | Spezialfall Software als Forschungsergebnis: DFG-Hinweise zur Open-Source-Veroeffentlichung, Lizenzwahl (MIT, BSD, Apache-2.0, GPL), Zenodo-DOI, Reproducibility. Prüfraster und Mustertext für Software-Sektion im Arbeitsprogramm im DFG-Fö... |
| `dfg-tieforschung-ethik-pflichten` | Tierversuchsethik-Pflichten in DFG-Antraegen: 3R-Prinzip (Replace, Reduce, Refine), TierSchG, TierSchVersV, Tierversuchsantrag bei der Behörde parallel zur DFG. DFG-Senatskommission für tierexperimentelle Forschung. Ethik-Sektion im Antr... |
| `dfg-wiedereinreichung-nach-ablehnung` | DFG-Ablehnung, Gutachten und Entscheidung auswerten: tragende Kritik extrahieren, Verteidigungsreflex vermeiden, Wiedereinreichung planen, Antrag umbauen, Anschreiben und Änderungsmatrix erstellen. |
| `dfg-zeitplan-und-meilensteine` | Antragszeitplan vom ersten Skizzen-Entwurf bis zur Einreichung in elan strukturieren: 6 Monate vorher Themenfindung, 4 Monate vorher Literaturrecherche und Arbeitsprogramm, 3 Monate vorher Finanzplan, 6 Wochen vorher Kollegenreview, 2 Wo... |
| `dfg-zwischen-und-abschlussbericht` | Zwischen- und Abschlussbericht systematisch vorbereiten: Berichtsraster der DFG, Soll-Ist-Abgleich Arbeitsprogramm, Publikationen, Personal, Geraete, Mittelabfluss. Abschlussbericht ist gleichzeitig Bewertungsbasis für Folgeantrag. Typis... |
| `dokumente-intake` | Dokumentenintake für DFG-Förderantrag: sortiert Projektbeschreibung, Finanzierungsplan, Lebenslauf, prüft Datum, Absender, Frist und Beweiswert (Publikationsverzeichnis, Vorarbeiten); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43... |
| `eigene-vorarbeiten-erstantragsteller` | Eigene Vorarbeiten in DFG-Antrag richtig darstellen: bisher publizierte Ergebnisse, eigene Methodik-Beitraege, Pilotdaten. Reviewer-Perspektive: Anknuepfungsfaehigkeit prüfen, keine Selbstplagiat-Prüfung. Mustertext für 2-Seiten-Kapitel... |
| `einstieg-routing` | Einstieg, Triage und Routing für DFG-Förderantrag: ordnet Rolle (Antragsteller, DFG-Gutachter, Universitätsleitung), markiert Frist (Antragsfrist Ausschreibungstermin), wählt Norm (DFG-Verwendungsrichtlinien, Wissenschaftsfreiheit Art. 5... |
| `elan-ethik-finanzplan` | Elan: Formular, Portal und Einreichungslogik. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `elan-formular-portal-einreichungslogik` | Elan: Formular, Portal und Einreichungslogik im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `erstantrag-projektlogik` | Foerderantragssteller: Tatbestandsmerkmale, Beweisfragen und Beleglage im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche F... |
| `erstpruefung-rollenklaerung-mandatsziel` | DFG: Erstprüfung, Rollenklärung und Mandatsziel im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwe... |
| `ethik-abschlussprodukt-uebergabe` | Ethik: Abschlussprodukt und Übergabe im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlun... |
| `ethik-abschlussprodukt-und-uebergabe` | Ethik: Abschlussprodukt und Übergabe. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `finanzplan-mandantenkommunikation` | Finanzplan: Mandantenkommunikation und Entscheidungsvorlage im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zuste... |
| `finanzplan-mandantenkommunikation-entscheidungsvorlage` | Finanzplan: Mandantenkommunikation und Entscheidungsvorlage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `foerderantragssteller-formalia-red-fuehrung` | Foerderantragssteller: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `foerderstrategie-schnell-grossgeraete-cluster` | Strategischer DFG-Router: entscheidet zwischen kleiner schneller Sachbeihilfe, normalem Antrag über 200.000 Euro, Koselleck ab 500.000 Euro oder anderem DFG-Programm. Enthält Spatz-in-der-Hand-Logik, Kürzungsrisiko, Begutachtungsdichte u... |
| `formalia-fehlerkatalog` | Formalia Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `formalia-red-team-und-qualitaetskontrolle` | Formalia: Red-Team und Qualitätskontrolle. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `forschungsdaten-fristennotiz-naechster` | Forschungsdaten: Fristennotiz und nächster Schritt im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sc... |
| `forschungsdaten-fristennotiz-und-naechster-schritt` | Forschungsdaten: Fristennotiz und nächster Schritt. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im Bereich dfg-foerderantrag: aktenbasierter Arbeitsgang mit Tatsachen-/Belegmatrix, Fristen- und Formcheck, passenden Fachankern, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `fuehrung-schriftsatz-brief-memo-bausteine` | Fuehrung: Schriftsatz-, Brief- und Memo-Bausteine im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sch... |
| `fuehrung-schriftsatz-brief-und-memo-bausteine` | Fuehrung: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `grosse-compliance-dokumentation-aktenvermerk` | Grosse: Compliance-Dokumentation und Aktenvermerk im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sch... |
| `grosse-kleine-koselleck-interessen` | Grosse: Compliance-Dokumentation und Aktenvermerk. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `internationale-kooperation-ki-ethik-kollegen` | Internationale Kooperation in DFG-Antrag aufbauen: D-A-CH-Lead-Agency-Verfahren (DACH, SNF, FWF), Bilateral mit DFG-Partnerorganisationen (NSF, JSPS, ISF, NSFC). Kooperationszusagen, Mittelverteilung, Hauptantragsteller, Co-Antragsteller... |
| `kaltstart-triage` | Adaptiver Einstieg, Schnelltriage und Fallrouting im DFG-Förderantrag-Plugin. Führt Anfänger mit maximal sechs Fragen, fordert Profis mit Go/No-Go und Reviewer-Risiken, klärt Forschungsfrage, Programmroute, Antragssumme, Tempo, Vorarbeit... |
| `kleine-verhandlung-vergleich-eskalation` | Kleine: Verhandlung, Vergleich und Eskalation im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwell... |
| `kleine-verhandlung-vergleich-und-eskalation` | Kleine: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `koselleck-interessen` | Koselleck: Mehrparteienkonflikt und Interessenmatrix im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `koselleck-mehrparteien-konflikt-und-interessen` | Koselleck: Mehrparteienkonflikt und Interessenmatrix. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `mandantenkommunikation` | Mandantenkommunikation im Bereich dfg-foerderantrag: aktenbasierter Arbeitsgang mit Tatsachen-/Belegmatrix, Fristen- und Formcheck, passenden Fachankern, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `output-waehlen` | Output-Wahl für DFG-Förderantrag: stimmt Adressat (Antragsteller, DFG-Gutachter, Universitätsleitung), Frist (Antragsfrist Ausschreibungstermin) und Form auf den Zweck ab — typische Outputs: Projektbeschreibung, Finanzierungsplan, Begrün... |
| `profi-behoerden-gerichts-registerweg` | Profi: Behörden-, Gerichts- oder Registerweg im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `profi-reviewer-beweislast-strategien` | Profi: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `publikationsstrategie-projekt` | Publikationsstrategie für das beantragte Projekt: realistische Zahl Publikationen, geplante Zeitschriften mit Impact und Open-Access-Status, DFG-Open-Access-Politik, Praeprints, Datenpublikation. Im Antrag muss Publikationsplan zu Arbeit... |
| `quellen-livecheck` | Quellen-Live-Check für DFG-Förderantrag: prüft Normen (DFG-Verwendungsrichtlinien, Wissenschaftsfreiheit Art. 5 III GG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Deutsche Forschungsgemeinschaft und Quellenhy... |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand |
| `reviewer-beweislast-darlegungslast` | Reviewer: Beweislast, Darlegungslast und Substantiierung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellu... |
| `reviewer-beweislast-und-darlegungslast` | Reviewer: Beweislast, Darlegungslast und Substantiierung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `sachbeihilfe-bis-200k-eigenanteil` | Sachbeihilfe: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `sachbeihilfe-fristen-form-zustaendigkeit` | Sachbeihilfe: Fristen, Form, Zuständigkeit und Rechtsweg im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellu... |
| `schnelle-quellenkarte` | Schnelle Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `spezial-grosse-compliance-dokumentation-und-akte` | Grosse: Compliance-Dokumentation und Aktenvermerk. |
| `spezial-schnelle-livequellen-und-rechtsprechungscheck` | Schnelle: Livequellen- und Rechtsprechungscheck. |
| `start-chronologie-fristen` | Adaptiver Einstieg, Schnelltriage und Fallrouting im DFG-Förderantrag-Plugin. Führt Anfänger mit maximal sechs Fragen, fordert Profis mit Go/No-Go und Reviewer-Risiken, klärt Forschungsfrage, Programmroute, Antragssumme, Tempo, Vorarbeit... |
| `strategien-internationaler-bezug` | Strategien: Internationaler Bezug und Schnittstellen im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `strategien-internationaler-bezug-und-schnittstellen` | Strategien: Internationaler Bezug und Schnittstellen. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `team-sonderfall-edge-case` | Team: Sonderfall und Edge-Case-Prüfung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahl... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für DFG-Förderantrag: trennt fehlende Tatsachen von fehlenden Belegen (Projektbeschreibung, Finanzierungsplan, Lebenslauf), nennt pro Lücke Beweisthema, Beschaffungsweg (Deutsche Forschungsgemeinschaft), Fri... |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zeitplan-meilensteine-zwischen` | Antragszeitplan vom ersten Skizzen-Entwurf bis zur Einreichung in elan strukturieren: 6 Monate vorher Themenfindung, 4 Monate vorher Literaturrecherche und Arbeitsprogramm, 3 Monate vorher Finanzplan, 6 Wochen vorher Kollegenreview, 2 Wo... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
