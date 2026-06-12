# Megaprompt: strafzumessung

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `strafzumessung`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Strafzumessung: ordnet Rolle (Angeklagter, Verteidiger, Staatsanwaltschaft), markiert F…
2. **orientierung-triage-paragraph-stgb-besonders** — Einstieg und Triage. Ordnet das Mandat (Strafverteidiger, Staatsanwaltschaft, Beistand) nach Verfahrensstadium (Strafbef…
3. **strafzumessung-erstpruefung-und-mandatsziel** — Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel im Strafzumessung.
4. **153a-stpo-iii-bewaehrung-stgb** — Einstellung gegen Auflage nach § 153a StPO. Zustimmungserfordernis Staatsanwaltschaft, Gericht und Beschuldigter. Voraus…
5. **bewaehrung-56-stgb-positive-sozialprognose** — Aussetzung der Vollstreckung zur Bewaehrung nach § 56 StGB. Voraussetzungen positive Sozialprognose Abs. 1 bis 1 Jahr; b…
6. **bewaehrung-auflagen-bewaehrungswiderruf-56f** — Auflagen § 56b StGB und Weisungen § 56c StGB im Bewaehrungsbeschluss. Auflagen dienen der Genugtuung Wiedergutmachung Ge…
7. **bewaehrungswiderruf-56f-stgb** — Widerruf der Strafaussetzung zur Bewaehrung nach § 56f StGB. Widerrufsgruende neue Straftat in der Bewaehrungszeit, Verl…
8. **freiheitsstrafe-ohne-bewaehrung-vollstreckung** — Freiheitsstrafe ohne Bewaehrung. Anrechnung Untersuchungshaft und Auslieferungshaft § 51 StGB. Vollstreckungsplanung Res…
9. **freiheitsstrafe-strafmass-geldstrafe** — Konkrete Zumessung der Freiheitsstrafe nach §§ 38 39 46 StGB. Strafrahmen pruefen, Strafhoehe innerhalb des Schuldrahmen…
10. **geldstrafe-tagessatzanzahl-bestimmen** — Bestimmung der Tagessatzanzahl der Geldstrafe nach § 40 Abs. 1 StGB. 5 bis 360 Tagessaetze als Grundgrenze; bei Gesamtge…
11. **geldstrafe-vs-freiheitsstrafe-47-stgb** — Vorrang der Geldstrafe vor kurzer Freiheitsstrafe nach § 47 StGB. Kurze Freiheitsstrafe unter 6 Monaten nur bei besonder…
12. **haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung** — Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung wenn Einbeziehung nach § 55 StGB nicht moeglich ist (Strafe ber…
13. **iii-stpo-begruendungsanforderungen-strafurteil** — Begruendungsanforderungen an die Strafzumessung im Strafurteil § 267 Abs. 3 StPO. Pflicht zur Mitteilung der bestimmende…
14. **minder-schwerer-fall-und-besonders-schwerer-fall** — Strafrahmen-Modifikation durch minder schweren Fall (Strafrahmen-Senkung) und besonders schweren Fall (Strafrahmen-Anheb…
15. **nachtraegliche-gesamtstrafenbildung-55-stgb** — Nachtraegliche Gesamtstrafenbildung nach § 55 StGB. Voraussetzung: spaetere Tat wurde **vor** einer frueheren Verurteilu…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Strafzumessung: ordnet Rolle (Angeklagter, Verteidiger, Staatsanwaltschaft), markiert Frist (Revision 1 Woche/1 Monat § 341 StPO), wählt Norm (§ 46 StGB, §§ 47-50 StGB Strafmilderung/-schärfung, BGH-Strafzumessungsleitlinien) und Zuständigkeit (Strafgericht (Amts-..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Strafzumessung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `153a-stpo-iii-bewaehrung-stgb` — 153a STPO III Bewaehrung STGB
- `besonders-formular-portal-und-einreichung` — Besonders Formular Portal und Einreichung
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung 56 STGB Positive Sozialprognose
- `bewaehrung-auflagen-bewaehrungswiderruf-56f` — Bewaehrung Auflagen Bewaehrungswiderruf 56F
- `bewaehrung-interessen-deutschem` — Bewaehrung Interessen Deutschem
- `bewaehrungswiderruf-56f-stgb` — Bewaehrungswiderruf 56F STGB
- `deutschem-tatbestand-beweis-und-belege` — Deutschem Tatbestand Beweis und Belege
- `freiheitsstrafe-compliance-dokumentation-und-akte` — Freiheitsstrafe Compliance Dokumentation und Akte
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Freiheitsstrafe Ohne Bewaehrung Vollstreckung
- `freiheitsstrafe-strafmass-geldstrafe` — Freiheitsstrafe Strafmass Geldstrafe
- `geldstrafe-grossen-rechtsmittel` — Geldstrafe Grossen Rechtsmittel
- `geldstrafe-tagessatzanzahl-bestimmen` — Geldstrafe Tagessatzanzahl Bestimmen
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Geldstrafe VS Freiheitsstrafe 47 STGB
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: § 56 StGB Bewährungszeit 2–5 Jahre, § 57 StGB 2/3-Reststrafenaussetzung, § 57a StGB lebenslange Freiheitsstrafe nach 15 Jahren.
- Fachpfad wählen: zentrale Anker im Strafzumessung sind StGB §§ 46, 46a, 46b, 47, 49, 56, 57, 57a, 64, JGG §§ 17, 18, 21, BtMG § 31. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Tatrichter, Verteidiger, Staatsanwaltschaft, Bewährungshelfer, Vollstreckungsbehörde.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `orientierung-triage-paragraph-stgb-besonders`

_Einstieg und Triage. Ordnet das Mandat (Strafverteidiger, Staatsanwaltschaft, Beistand) nach Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe), erkennt Eilfristen, schlaegt passende Fachmodule aus diesem Plugin vor u..._

# Strafzumessung — Orientierung und Triage

## Aktenstart statt Formularstart

Wenn zu **Orientierung Triage Paragraph Stgb Besonders** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Strafzumessung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Strafzumessung ist die richterliche Bestimmung von Strafart und Strafhoehe innerhalb des gesetzlichen Strafrahmens. Grundlage ist die Schuld des Taeters (§ 46 Abs. 1 Satz 1 StGB). Dieser Allgemein-Skill ist der Eingang in das Plugin: er ordnet den Stand des Verfahrens, identifiziert Fristen und schlaegt den passenden Fachmodul vor.

## Wann brauchen Sie diese Skill?

- Mandant hat Strafbefehl erhalten, Strafzumessung soll angegriffen oder beschraenkter Einspruch erwogen werden.
- Anklageschrift liegt vor, Strafzumessungs-Verteidigung in der Hauptverhandlung wird vorbereitet.
- Verstaendigungs-Gespraech (§ 257c StPO) mit Gericht und Staatsanwaltschaft steht an, Strafrahmen wird sondiert.
- Urteil ist ergangen, Strafzumessungsruege wird vorbereitet (§ 267 Abs. 3 StPO).
- Mehrere Verurteilungen liegen vor, nachtraegliche Gesamtstrafenbildung (§ 55 StGB) oder Haerteausgleich pruefen.

## Rolle abklaeren (Pflicht)

| Rolle | Typischer Fokus |
|---|---|
| Strafverteidiger | Strafmilderung, Bewaehrung, TOA, Verstaendigung, Strafzumessungsruege |
| Staatsanwaltschaft | Antragsstrafe, Strafzumessungsrichtlinien, Schwere-Argumente |
| Mandant / Betroffener (mit Anwalt) | Verstaendnis der Strafzumessungslogik; Tagessatzpruefung |
| Nebenklaegervertreter | Strafzumessungs-Aspekte zugunsten des Opfers |

Wenn die Rolle unklar ist, **frage zuerst** — die Argumentationsrichtung haengt davon ab.

## Verfahrensstadium-Triage

| Stadium | Primaerer Skill |
|---|---|
| Strafbefehl liegt vor | `strafbefehl-strafzumessung-407-stpo`, ggf. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` |
| Einstellungsangebot § 153a StPO | `153a-stpo-einstellung-gegen-auflage` |
| Anklage liegt vor, Hauptverhandlung vorbereiten | `strafrahmen-und-strafzumessungsstufen`, dann `paragraph-46-stgb-grundsatz-strafzumessung` |
| Verstaendigung steht an | `verstaendigung-257c-stpo-strafzumessung` |
| TOA mit dem Opfer moeglich | `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` |
| Mehrere Taten in einem Verfahren | `gesamtstrafenbildung-53-54-stgb-erste-instanz` |
| Mehrere Verurteilungen, eine Anlasstat | `nachtraegliche-gesamtstrafenbildung-55-stgb`, ggf. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` |
| Urteil liegt vor, Strafzumessungsruege | `267-iii-stpo-begruendungsanforderungen-strafurteil` |
| Mandant unter 21 Jahren | `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` |

## Schritt-für-Schritt-Anleitung

1. Rolle und Verfahrensstadium erfragen oder aus Material erkennen.
2. Eilfristen pruefen (Einspruchsfrist § 410 StPO, Revisionsbegruendung § 345 StPO, Bewaehrungsstellungnahme).
3. Strafrahmen-Frage stellen: Welche Norm, welcher Strafrahmen, gibt es Regelbeispiele oder minder schweren Fall?
4. Strafzumessungs-Tatsachen sammeln (§ 46 Abs. 2 StGB): Vorleben, Tat, Nachtatverhalten.
5. Passenden Fachmodul auswaehlen; bei klarer Faktenlage sofort ersten Entwurf mit Platzhaltern liefern.
6. Quellenpflicht beachten: § 46 StGB, einschlaegige Spezialnormen, BGH-Linie nur mit verifiziertem Aktenzeichen.

## Typische Fehler

- Strafzumessung wird ohne Sortierung des Strafrahmens diskutiert: erst Strafrahmen pruefen, dann konkretisieren.
- Verstaendigung wird abgeschlossen, bevor die Belehrungspflicht (§ 257c Abs. 4 und 5 StPO) sauber gepruefte ist.
- TOA wird als reine Schadenswiedergutmachung verstanden; nach BGH ist ein friedensstiftender kommunikativer Prozess noetig.
- Tagessatzhoehe wird ohne Einkommensnachweis akzeptiert; Gericht schaetzt sonst zu Lasten des Mandanten.
- Nachtraegliche Gesamtstrafe wird vergessen; Haerteausgleich nicht thematisiert.

## Quellen und Stand 05/2026

- StGB §§ 38 ff. (Strafarten, Strafrahmen), § 46 (Grundsatz), §§ 47, 49, 56, 56b–f, 53–55 StGB.
- StPO §§ 153, 153a, 257c, 267 Abs. 3, 407 ff., 460 StPO.
- JGG §§ 5 ff., 17, 18, 105.
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; vgl. `references/zitierweise.md`.

---

## Skill: `strafzumessung-erstpruefung-und-mandatsziel`

_Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel im Strafzumessung._

# Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Strafzumessung Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Strafzumessung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** StPO, TOA, JGG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Strafzumessung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Strafzumessungs-Erstpruefung Bausteine
- **Mandantenrolle und Ziel:**
 - **Beschuldigter / Angeklagter:** Strafmilderung; Bewaehrung; Einstellung; Verstaendigung-Korridor.
 - **Verletzter / Nebenklage § 395 StPO:** Schaden-Wiedergutmachung; angemessene Sanktion.
 - **StA-Mitarbeit (selten Mandat):** Strafmasspruefung Antrag.
 - **Gericht/Schoeffe:** strafrahmen-konforme Entscheidung.
- **Sofort-Checkliste:**
 - Welcher Tatbestand? Strafrahmen abstrakt (Min-Max).
 - Vorstrafen (BZRG-Auszug); Verwertungsverbot § 51 BZRG.
 - Schuldfaehigkeit § 20 StGB / verminderte Schuldfaehigkeit § 21 StGB - Anhaltspunkte für Gutachten?
 - Tatschuld (objektive Schwere, subjektive Vorwerfbarkeit) - § 46 I 1 StGB Grundlage.
 - Pruefung Regelbeispiel / besonders schwerer Fall / minderschwerer Fall.
 - Strafrahmenverschiebung § 49 StGB pruefen.
- **Erwartungsspanne kommunizieren:**
 - **Geldstrafe** ueblicher Bereich nach Vergehen, Vorstrafen, Schuld: Zahl der TS; **Tagessatzhoehe** = 1/30 Nettoeinkommen.
 - **Freiheitsstrafe**: idR ab 6 Monaten (§ 47 StGB), Bewaehrungspraxis § 56 StGB.
 - **Nebenfolgen**: Fahrverbot § 44 StGB, Entziehung Fahrerlaubnis § 69 StGB, BZRG-Eintrag, FZR.
- **Mandatsziel-Matrix:** Sachverhalt vs. Beweislage; Beste-Case / Wahrscheinlichster / Worst-Case Strafmass.
- **Strategie:** Gestaendnis vs. Verteidigung; Verstaendigung § 257c StPO; TOA § 46a StGB; Einstellung §§ 153, 153a StPO.
- **Anschluss:** Tatbestand-Belege / Strafmilderung / Bewaehrung / Rechtsmittel.

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.

---

## Skill: `153a-stpo-iii-bewaehrung-stgb`

_Einstellung gegen Auflage nach § 153a StPO. Zustimmungserfordernis Staatsanwaltschaft, Gericht und Beschuldigter. Voraussetzung kein öffentliches Interesse an der Strafverfolgung Vergehen. Auflagen Geldzahlung gemeinnuetzige Arbeit Schadenswiedergutmachung Unterhaltspflicht TOA. Verhaeltnis zur S..._

# Einstellung gegen Auflage — § 153a StPO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

§ 153a StPO erlaubt die Einstellung des Verfahrens **gegen Auflagen oder Weisungen**, wenn das öffentliche Interesse an der Strafverfolgung beseitigt werden kann und die Schwere der Schuld nicht entgegensteht. Es bedarf der Zustimmung des Beschuldigten, des Gerichts (im gerichtlichen Stadium) und der Staatsanwaltschaft. Mit Erfuellung der Auflage ist die Tat **nicht mehr** verfolgbar (Verbrauch der Strafklage in dem Umfang).

## Wann brauchen Sie diese Skill?

- Sie sondieren eine Einstellung mit Staatsanwaltschaft oder Gericht.
- Sie pruefen, ob die Schwere der Schuld den Weg ueber § 153a StPO oeffnet oder versperrt.
- Sie verhandeln die Hoehe der Geldauflage und vergleichen sie mit der drohenden Geldstrafe.

## Rechtliche Grundlagen

- **§ 153a Abs. 1 StPO** — Vorlaeufige Einstellung mit Auflagen durch die Staatsanwaltschaft (mit Zustimmung des Gerichts, ab dem Zwischenverfahren bereits Gerichts-Zustimmung).
- **§ 153a Abs. 2 StPO** — Einstellung durch das Gericht in jedem Stadium.
- **§ 153a Abs. 3 StPO** — Auflagenkatalog:
 - Nr. 1: Wiedergutmachung des Schadens.
 - Nr. 2: Geldbetrag an gemeinnuetzige Einrichtung oder Staatskasse.
 - Nr. 3: Sonstige gemeinnuetzige Leistung.
 - Nr. 4: Unterhaltsleistung.
 - Nr. 5: Taeter-Opfer-Ausgleich, § 46a StGB.
 - Nr. 6: Verkehrserziehungsmassnahme.
 - Nr. 7: Beratungs-/Therapiemassnahme.
- **§ 153 StPO** — Einstellung **ohne** Auflage bei Geringfuegigkeit (Bagatelle).

## Strafzumessungs-Grundsatz

§ 153a StPO ist **keine** Strafe; daher kein BZRG-Eintrag, kein Vorstrafenstatus. Aber:

- Die Auflagenhoehe orientiert sich faktisch an der **drohenden Strafe**.
- Daumenregel: Geldauflage entspricht ungefaehr der Geldstrafe, die bei Verurteilung gedroht haette.
- Anrechnung von Geldauflage auf eine spaeter doch verhaengte Strafe nach § 153a Abs. 1 Satz 6 StPO (bei Wiederaufnahme).

## Voraussetzungen

1. **Vergehen** (keine Verbrechen).
2. **Schwere der Schuld** steht nicht entgegen.
3. **Auflage** ist geeignet, das öffentliche Interesse zu beseitigen.
4. **Zustimmung** Beschuldigter + Gericht + Staatsanwaltschaft.

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Eignung pruefen**:
 - Vergehen? Strafdrohung max. 5 Jahre Freiheitsstrafe oder Geldstrafe (allgemein).
 - Schwere der Schuld vertretbar? Bei einschlaegigen Vorbelastungen oft schwierig.
2. **Auflagenpaket** mit Mandant abstimmen:
 - Schadenswiedergutmachung: vorrangig.
 - Geldauflage: Hoehe realistisch (i.d.R. 500-15 000 EUR; bei Wirtschaftsstrafsachen hoeher).
 - Gemeinnuetzige Arbeit als Alternative.
 - TOA wenn moeglich.
3. **Verhandlung** mit Staatsanwaltschaft / Gericht:
 - Schriftlicher Vorschlag mit konkretem Auflagenpaket.
 - Begruendung: warum öffentliches Interesse beseitigt ist.
 - Kompensation gegenueber drohender Strafe darstellen.
4. **Belehrung** des Mandanten: Zustimmung wird mit Verbrauch der Strafklage ueber den **abgegrenzten Tatvorwurf** wirksam; keine spaetere Strafverfolgung dieses Vorwurfs.
5. **Erfuellungsnachweis** sichern: Zahlungsbeleg, Stundenkarte gemeinnuetzige Arbeit, TOA-Bestaetigung. Erfuellung innerhalb der gesetzten Frist (verlaengerbar nach § 153a Abs. 1 Satz 4 StPO).

## Schritt-für-Schritt-Anleitung (Anklage)

- **§ 153 StPO** bei Bagatellen; ohne Auflage.
- **§ 153a StPO** bei mittlerer Schwere mit Auflage.
- Bei Anklage **trotz** Einigungsspielraum: Begruendung der "öffentlichen Interesse"-Erforderlichkeit.

## Wirkung der Einstellung

- **Strafklageverbrauch** in Bezug auf den abgegrenzten Vorwurf.
- **Kein BZRG-Eintrag**.
- Berufsrechtliche Folgen oft minimal (im Vergleich zur Verurteilung).
- Bei **Nichterfuellung**: Wiederaufnahme des Verfahrens; gezahlte Geldauflage wird angerechnet (§ 153a Abs. 1 Satz 6 StPO).

## Vergleich Strafbefehl vs. § 153a StPO

| Merkmal | Strafbefehl | § 153a StPO |
|---|---|---|
| Schuldspruch | ja | nein |
| BZRG-Eintrag | ja | nein |
| Sanktion | Geldstrafe / Bewaehrung | Auflage |
| Vorstrafe | ja | nein |
| Beschleunigung | ja | ja |
| Hoehe Geld | Tagessatze x Zahl | i.d.R. aehnlich, oft etwas hoeher |

## Typische Fehler

- **Schwere der Schuld** uebersehen: Bei Wiederholungstaetern oder hoher Schadenshoehe ist § 153a STO oft nicht moeglich.
- **Auflagenerfuellung** versaeumt: Verfahren wird wiederaufgenommen.
- **Zustimmung** vor Mandantenbelehrung: Unterschrift ohne Konsequenz-Verstaendnis.
- **Auflagenhoehe** zu niedrig angesetzt: Staatsanwaltschaft / Gericht lehnen ab.
- **TOA-Anbau** ungenutzt: Kombination § 153a + TOA-Auflage bringt oft das Gericht zur Zustimmung.

## Quellen und Stand 05/2026

- §§ 153, 153a StPO in der geltenden Fassung.
- § 46a StGB.
- Quellenregel: vgl. `references/zitierweise.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46 StGB
- § 49 StGB
- § 55 JGG
- § 55 StGB
- § 56 StGB
- § 46a StGB
- § 40 StGB
- § 47 StGB
- § 56f StGB
- § 54 StGB
- § 57 StGB
- § 105 JGG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `bewaehrung-56-stgb-positive-sozialprognose`

_Aussetzung der Vollstreckung zur Bewaehrung nach § 56 StGB. Voraussetzungen positive Sozialprognose Abs. 1 bis 1 Jahr; besondere Umstaende Abs. 2 bis 2 Jahre; Verteidigung der Rechtsordnung Abs. 3. Prognose-Faktoren Vorleben, soziale Bindungen, Reue, Wiedergutmachung, Therapiebereitschaft. Bewaeh..._

# Strafaussetzung zur Bewaehrung — § 56 StGB

## Arbeitsbereich

Aussetzung der Vollstreckung zur Bewaehrung nach § 56 StGB. Voraussetzungen positive Sozialprognose Abs. 1 bis 1 Jahr; besondere Umstaende Abs. 2 bis 2 Jahre; Verteidigung der Rechtsordnung Abs. 3. Prognose-Faktoren Vorleben, soziale Bindungen, Reue, Wiedergutmachung, Therapiebereitschaft. Bewaehrungszeit § 56a. Auflagen Weisungen. Schnittstelle 267 Abs. 3 StPO. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

§ 56 StGB ermoeglicht, Freiheitsstrafen unter zwei Jahren zur Bewaehrung auszusetzen. Es ist die zentrale Weiche für das spaetere Verhalten des Verurteilten und das wichtigste Verteidigungs-Ziel bei Freiheitsstrafen nahe der Bewaehrungsschwelle.

## Wann brauchen Sie diese Skill?

- Sie verteidigen gegen eine drohende Freiheitsstrafe und wollen Bewaehrung sichern.
- Sie strukturieren das Plaedoyer um die Sozialprognose.
- Sie pruefen ein Urteil ohne Bewaehrung auf Revisionsangriff.
- Sie planen die Bewaehrungsverhandlung mit dem Mandanten (Auflagen, Weisungen, Bewaehrungshelfer).

## Rechtliche Grundlagen

- **§ 56 Abs. 1 StGB** — Aussetzung von Strafe bis 1 Jahr bei positiver Sozialprognose: Es muss zu erwarten sein, dass der Verurteilte sich schon die Verurteilung zur Warnung dienen lassen wird und kuenftig auch ohne die Einwirkung des Strafvollzugs keine Straftaten mehr begehen wird.
- **§ 56 Abs. 2 StGB** — Aussetzung von Strafe bis 2 Jahre nur bei **besonderen Umstaenden** in der Tat und in der Persoenlichkeit des Verurteilten.
- **§ 56 Abs. 3 StGB** — Aussetzung kann versagt werden, wenn die **Verteidigung der Rechtsordnung** die Vollstreckung gebietet (Strafe von mindestens 6 Monaten).
- **§ 56a StGB** — Bewaehrungszeit 2 bis 5 Jahre, mindestens 2 Jahre.
- **§ 56b, 56c StGB** — Auflagen und Weisungen; vgl. `bewaehrung-auflagen-und-weisungen-56b-c-stgb`.
- **§ 56f StGB** — Widerruf; vgl. `bewaehrungswiderruf-56f-stgb`.
- **§ 56g StGB** — Erlass der Strafe nach Bewaehrungsablauf.

## Strafzumessungs-Grundsatz

Bewaehrung ist **Regelfall** bei Strafe bis 1 Jahr, sofern Sozialprognose positiv ist. Bei Strafe bis 2 Jahre ist Bewaehrung Ausnahme; es muessen **besondere Umstaende** vorliegen.

## Prognose-Faktoren (positiv)

- **Persoenlichkeit**: stabile Lebensfuehrung, keine Vorstrafen, sozial integriert.
- **Vorleben**: keine einschlaegigen Vorstrafen; lange straffreie Zeit.
- **Tatumstaende**: erstmaliger Verstoss, niedrige kriminelle Energie, Notlage.
- **Verhalten nach der Tat**: Reue, Gestaendnis, Schadenswiedergutmachung, TOA (§ 46a StGB), Therapie- oder Suchtberatung in Anspruch genommen.
- **Soziale Bindungen**: Familie, Beruf, fester Wohnsitz, Bindung an Kinder.
- **Lebensplanung**: Ausbildung, Arbeitsstelle, Aussicht auf Stabilitaet.

## Prognose-Faktoren (negativ)

- Einschlaegige Vorbelastung, Wiederholungstaeter.
- Bewaehrungs-Versager in der Vorgeschichte.
- Aktuelle Sucht ohne Therapie.
- Tat in laufender Bewaehrung.
- Fehlende Einsicht oder Vermeidung von Auseinandersetzung.

## "Besondere Umstaende" iSv § 56 Abs. 2 StGB

Bei Strafe ueber 1 bis 2 Jahre. Erforderlich sind Umstaende, die das Gewicht der drohenden Vollstreckung **deutlich** mindern. Typisch:

- Massive Tatfolgen schon beim Taeter (Behinderung, Verstuemmelung in Tatzusammenhang).
- Hohe Strafempfindlichkeit (Sucht-Therapieaufenthalt droht abzubrechen, schwere familiaere Belastung).
- Sehr lange Verfahrensdauer (Vollstreckungsmodell).
- Aussergewoehnliches Nachtatverhalten (komplette Wiedergutmachung, dauerhafte Therapie).

## "Verteidigung der Rechtsordnung" iSv § 56 Abs. 3 StGB

Restriktive Auslegung der st. Rspr.: Nicht jede mediale Empoerung; erforderlich sind besondere Tatumstaende, die das Vertrauen der Allgemeinheit in die Geltung der Rechtsordnung beruehren. **Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.**

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Strafmass-Schwelle** im Blick: Ziel 11 Monate oder 1 Jahr 11 Monate, je nach Konstellation.
2. **Prognose-Vortrag** vorbereiten: Beweise und Beleg sammeln (Arbeitsvertrag, Mietvertrag, Therapiebescheinigung, Schulbestaetigung).
3. **Sozialbericht** der Bewaehrungshilfe anregen, wenn das hilft (§ 56d StGB Bewaehrungshelfer; auch vorab anhoerend).
4. **Konkret beantragen**: "Wir beantragen, die Strafe nach § 56 Abs. [1/2] StGB zur Bewaehrung auszusetzen. Sozialprognose ist positiv, weil [...]."
5. **Auflagenangebote** vorbereiten (Zahlung an gemeinnuetzige Einrichtung, Therapie, Wiedergutmachung); vgl. `bewaehrung-auflagen-und-weisungen-56b-c-stgb`.
6. **Hilfsweise Reststrafenaussetzung** nach § 57 StGB ansprechen, falls Bewaehrung in erster Instanz nicht zugesprochen wird.

## Schritt-für-Schritt-Anleitung (Anklage)

- Bei Strafantrag ohne Bewaehrung: konkrete Begruendung, warum Sozialprognose negativ ist.
- Bei Strafe ueber 1 Jahr und bis 2 Jahre Bewaehrung: konkrete Begruendung, warum keine besonderen Umstaende vorliegen.
- "Verteidigung der Rechtsordnung" sparsam und nur bei konkreten Anhaltspunkten.

## Begruendungspflicht des Gerichts

Wird Bewaehrung **versagt**, muss das Urteil im Strafzumessungsteil konkret darlegen, warum die Sozialprognose negativ ist (§ 267 Abs. 3 Satz 4 StPO). Pauschale Wendungen reichen nicht.

## Typische Fehler

- **Pauschale Prognose** ohne Tatsachenbasis (Verteidigung wie Gericht).
- **Bewaehrung bei Strafe ueber 2 Jahren** beantragt: rechtlich ausgeschlossen.
- **Auflagen/Weisungen** im Bewaehrungsbeschluss nicht ausdifferenziert: Mandant uebersieht Risiko des Widerrufs.
- **Sucht ohne Therapie**: Bewaehrung ohne stoffspezifische Therapieweisung ist riskant.
- **Verfahrensdauer-Kompensation** vergessen.

## Quellen und Stand 05/2026

- §§ 56, 56a-g, 57, 57a StGB in der geltenden Fassung.
- § 267 Abs. 3 Satz 4 StPO.
- BGH-Linie zu "Verteidigung der Rechtsordnung" — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46 StGB
- § 49 StGB
- § 55 JGG
- § 55 StGB
- § 56 StGB
- § 46a StGB
- § 40 StGB
- § 47 StGB
- § 56f StGB
- § 54 StGB
- § 57 StGB
- § 105 JGG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `bewaehrung-auflagen-bewaehrungswiderruf-56f`

_Auflagen § 56b StGB und Weisungen § 56c StGB im Bewaehrungsbeschluss. Auflagen dienen der Genugtuung Wiedergutmachung Geldzahlung gemeinnuetzige Arbeit. Weisungen lenken kuenftiges Verhalten Aufenthalt Beruf Therapie Kontaktverbot. Bewaehrungshelfer § 56d StGB. Aktive Verteidigungsstrategie: Aufl..._

# Auflagen und Weisungen — §§ 56b, 56c StGB

## Arbeitsbereich

Auflagen § 56b StGB und Weisungen § 56c StGB im Bewaehrungsbeschluss. Auflagen dienen der Genugtuung Wiedergutmachung Geldzahlung gemeinnuetzige Arbeit. Weisungen lenken kuenftiges Verhalten Aufenthalt Beruf Therapie Kontaktverbot. Bewaehrungshelfer § 56d StGB. Aktive Verteidigungsstrategie: Auflagenangebote vorbereiten, ueberzogene Weisungen abwehren. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Bei Aussetzung zur Bewaehrung kann das Gericht **Auflagen** (§ 56b StGB) und **Weisungen** (§ 56c StGB) erteilen. **Auflagen** dienen der Genugtuung für das begangene Unrecht. **Weisungen** dienen der Lebensfuehrung und Resozialisierung. Sinnvoll vorbereitete Auflagenangebote des Verteidigers helfen oft, die Bewaehrungsschwelle zu nehmen.

## Wann brauchen Sie diese Skill?

- Sie verteidigen vor einer Hauptverhandlung mit Aussicht auf Bewaehrung und wollen das Gericht durch konkrete Auflagenangebote unterstuetzen.
- Sie pruefen einen Bewaehrungsbeschluss, dessen Weisungen unzumutbar oder unverhaeltnismaessig sind.
- Sie begleiten den Mandanten in der Bewaehrungszeit (Pflichten, Risiken).

## Rechtliche Grundlagen

### § 56b StGB — Auflagen (Genugtuungs-Charakter)

Das Gericht kann dem Verurteilten auferlegen,

- den Schaden nach Kraeften wiedergutzumachen (Nr. 1);
- einen Geldbetrag an eine gemeinnuetzige Einrichtung zu zahlen (Nr. 2);
- sonst gemeinnuetzige Leistungen zu erbringen (Nr. 3);
- einen Geldbetrag an die Staatskasse zu zahlen (Nr. 4).

Auflagen mit Schadenswiedergutmachungscharakter haben **Vorrang**.

### § 56c StGB — Weisungen (Resozialisierungs-Charakter)

Beispiele:

- Anordnungen zu Aufenthalt, Ausbildung, Arbeit, Freizeit, wirtschaftlichen Verhaeltnissen (Abs. 2 Nr. 1).
- Sich zu bestimmten Zeiten oder Anlaessen bei Gericht oder anderer Stelle zu melden (Nr. 2).
- Mit bestimmten Personen oder Personengruppen keinen Verkehr zu pflegen, bei ihnen nicht zu wohnen und nicht zu uebernachten (Nr. 3).
- Bestimmte Gegenstaende nicht zu besitzen oder verwahren zu lassen, die ihm Gelegenheit oder Anreiz zu weiteren Straftaten bieten koennten (Nr. 4).
- Unterhaltspflichten nachzukommen (Nr. 5).

### § 56d StGB — Bewaehrungshelfer

Das Gericht **kann** einen Bewaehrungshelfer bestellen. Bei Strafe ueber 9 Monaten und bei Verurteilten unter 27 Jahren ist die Bestellung Regelfall.

## Grenzen

- Auflagen und Weisungen muessen **zumutbar** sein (§ 56b Abs. 1 Satz 1, § 56c Abs. 1 Satz 1 StGB).
- Sie duerfen den Verurteilten nicht in der **Lebensfuehrung** unverhaeltnismaessig einschraenken.
- Therapieweisungen nur mit **Einwilligung** des Verurteilten (§ 56c Abs. 3 Nr. 1, 2 StGB) — Therapie ist nicht erzwingbar.
- Geldauflagen muessen wirtschaftlich tragbar sein.

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Vor der Hauptverhandlung**: Auflagenpaket mit dem Mandanten abstimmen — was kann er tragen?
 - Schadenswiedergutmachung an den Geschaedigten (auch Ratenangebot).
 - Geldbetrag an eine konkrete gemeinnuetzige Einrichtung in einer wirtschaftlich tragbaren Hoehe.
 - Stundenangebot für gemeinnuetzige Arbeit (z.B. 60 oder 100 Stunden).
2. **Im Plaedoyer** ausdruecklich anbieten:
 - "Mein Mandant ist bereit, zur Genugtuung [...] zu zahlen."
 - "Mein Mandant ist bereit, [X] Stunden gemeinnuetzige Arbeit zu leisten."
3. **Weisungen** nur akzeptieren oder anregen, wenn sie zumutbar sind und das Mandanteninteresse nicht verletzen:
 - Therapie nur mit Einwilligung.
 - Aufenthaltsweisungen, die Arbeitsstelle gefaehrden, ablehnen.
 - Kontaktverbote nur, wenn der Mandant einverstanden ist.
4. **Nach Verkuendung**: Auflagen-/Weisungs-Beschluss pruefen, ggf. **sofortige Beschwerde** nach § 305a StPO oder § 311 StPO innerhalb einer Woche.

## Standardauflagen (Praxis)

- Geldzahlung an gemeinnuetzige Einrichtung (oft 500 bis 5 000 EUR).
- Gemeinnuetzige Arbeit (40 bis 200 Stunden).
- Schadenswiedergutmachung mit Ratenplan.
- Teilnahme an Verkehrserziehungs- oder Anti-Aggressions-Kurs.
- Suchtberatung oder Therapie (mit Einwilligung).

## Bewaehrungsbeschluss-Struktur

```
Beschluss (§ 268a StPO)

I. Die Vollstreckung der Freiheitsstrafe von [X] Monaten wird
 zur Bewaehrung ausgesetzt.
II. Die Bewaehrungszeit wird auf [X] Jahre festgesetzt.
III. Auflagen (§ 56b StGB):
 - [Wiedergutmachung]
 - [Geldzahlung]
 - [gemeinnuetzige Arbeit]
IV. Weisungen (§ 56c StGB):
 - [Aufenthalt / Beruf / Therapie / Meldepflicht / Kontaktverbot]
V. [Bestellung Bewaehrungshelfer nach § 56d StGB]
VI. Belehrung nach § 268a Abs. 3 StPO.
```

## Typische Fehler

- **Therapieweisung ohne Einwilligung**: unwirksam; § 56c Abs. 3 StGB.
- **Geldauflage** unwirtschaftlich angesetzt: Verurteilter kann nicht zahlen, Widerrufsgefahr.
- **Aufenthaltsweisung** kollidiert mit Arbeitsstelle: laesst sich oft korrigieren mit sofortiger Beschwerde.
- **Auflagenangebote** zu spaet (erst nach Verkuendung): wirkt nicht mehr strafzumessend.
- **Standardauflage** ohne Bezug zur Tat: schwaecht Wirkung.

## Quellen und Stand 05/2026

- §§ 56b, 56c, 56d, 56g StGB in der geltenden Fassung.
- §§ 268a, 305a, 311 StPO.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `bewaehrungswiderruf-56f-stgb`

_Widerruf der Strafaussetzung zur Bewaehrung nach § 56f StGB. Widerrufsgruende neue Straftat in der Bewaehrungszeit, Verletzung von Auflagen Weisungen, Entziehung von der Bewaehrungshilfe. Verhaeltnismaessigkeitspruefung. Beschluss-Verfahren § 453 StPO. Sofortige Beschwerde. Verteidigungsstrategie..._

# Bewaehrungswiderruf — § 56f StGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

§ 56f StGB regelt den Widerruf der Strafaussetzung zur Bewaehrung. Tritt eine Bewaehrungsverletzung ein, drohen Widerruf und Vollstreckung der ausgesetzten Strafe. Bevor das Gericht widerruft, muss es **andere, weniger einschneidende Massnahmen** pruefen (§ 56f Abs. 2 StGB).

## Wann brauchen Sie diese Skill?

- Der Mandant ist in der Bewaehrungszeit erneut auffaellig geworden (neue Tat, neue Anklage).
- Eine Auflage oder Weisung wurde nicht erfuellt (Geldauflage nicht gezahlt, gemeinnuetzige Arbeit nicht geleistet).
- Der Bewaehrungshelfer hat einen Bericht mit negativem Inhalt vorgelegt.
- Eine Widerrufsverfuegung wird angekuendigt oder ist bereits ergangen.

## Rechtliche Grundlagen

### § 56f Abs. 1 StGB — Widerrufsgruende

Das Gericht widerruft die Aussetzung, wenn der Verurteilte:

- in der Bewaehrungszeit eine **Straftat** begeht und dadurch zeigt, dass die Erwartung, die der Strafaussetzung zugrunde lag, sich nicht erfuellt hat (Nr. 1);
- gegen **Weisungen** groeblich oder beharrlich verstoesst oder sich der Aufsicht und Leitung des Bewaehrungshelfers beharrlich entzieht und dadurch Anlass zur Besorgnis gibt, dass er erneut Straftaten begehen wird (Nr. 2);
- gegen **Auflagen** groeblich oder beharrlich verstoesst (Nr. 3).

### § 56f Abs. 2 StGB — Mildere Massnahmen

Das Gericht sieht von dem Widerruf ab, wenn es ausreicht,

- **weitere Auflagen oder Weisungen** zu erteilen, insbesondere den Verurteilten einem Bewaehrungshelfer zu unterstellen (Nr. 1);
- die **Bewaehrungszeit** oder Unterstellungszeit zu **verlaengern** (Nr. 2).

### § 56f Abs. 3 StGB — Anrechnung

Bei Widerruf werden Leistungen, die der Verurteilte zur Erfuellung von Auflagen oder Anweisungen erbracht hat, **nicht erstattet**. Das Gericht kann jedoch Leistungen nach § 56b Abs. 2 Satz 1 Nr. 2-4 StGB (Geld/Stunden) auf die Strafe anrechnen.

### Verfahren

- **§ 453 StPO** — Beschlussverfahren ueber Strafaussetzung und Widerruf.
- **§ 453 Abs. 1 Satz 4 StPO** — Verurteilter ist **anzuhoeren**.
- **§ 453 Abs. 2 StPO** — Sofortige Beschwerde innerhalb einer Woche (§ 311 Abs. 2 StPO).

## Strafzumessungs-Grundsatz Widerruf

- **Verhaeltnismaessigkeitspruefung** ist Pflicht (§ 56f Abs. 2 StGB).
- Eine Verurteilung wegen einer neuen Straftat allein begruendet nicht zwingend den Widerruf; das Gericht muss pruefen, ob die Sozialprognose unverwertbar enttaeuscht ist.
- Bei **Verfehlung unter der Erheblichkeitsschwelle** ist mildere Massnahme (Auflagen-Erhoehung, Verlaengerung) Pflicht.

## Widerrufsgruende im Detail

### Neue Straftat (Nr. 1)

- Rechtskraeftige Verurteilung **erforderlich** (str.; st. Rspr. erforderlich, vgl. die juengere Linie; Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren).
- Auch eine **Bewaehrungszeit ueberschreitende** Tat kann Widerrufsgrund sein, wenn sie waehrend der Bewaehrungszeit begangen wurde (BGH st. Rspr.; Aktenzeichen verifizieren).
- Tat im Zustand verminderter Schuldfaehigkeit (§ 21 StGB) oder Bagatelle kann mildernde Massnahme nahelegen.

### Weisungs-Verstoss (Nr. 2)

- "Groeblich oder beharrlich" — einmaliger geringfuegiger Verstoss reicht nicht.
- "Anlass zur Besorgnis" — Prognose-Anforderung, kein automatischer Schluss.

### Auflagen-Verstoss (Nr. 3)

- Geldauflage nicht gezahlt: bei Zahlungsunfaehigkeit ist Widerruf unverhaeltnismaessig.
- Gemeinnuetzige Arbeit nicht geleistet: Pruefung von Hinderungsgruenden.

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Akteneinsicht** § 147 StPO in die Bewaehrungsakte (Bewaehrungshelfer-Berichte, vorhaltliche Schreiben).
2. **Tatsachenstand klaeren**: Welche konkreten Verstoesse werden vorgeworfen? Gibt es Belege?
3. **Mildere Massnahmen** offensiv anbieten:
 - Auflagenerfuellung nachholen.
 - Bewaehrungszeit-Verlaengerung.
 - Therapieteilnahme aufnehmen.
 - Schadenswiedergutmachung nachholen.
4. **Anhörungstermin** (§ 453 StPO) gut vorbereiten:
 - Mandant praesentieren: stabilisiert, lernfaehig.
 - Schriftliche Stellungnahme einreichen.
 - Beleg für aktuelle Lebenssituation.
5. **Sofortige Beschwerde** nach § 453 Abs. 2 StPO i.V.m. § 311 StPO innerhalb einer **Woche** ab Zustellung.
6. **Bei zweiter Verurteilung** in der Bewaehrungszeit: Pruefung, ob Gesamtstrafenbildung (§ 55 StGB) anstelle eines Widerrufs sinnvoll ist; vgl. `nachtraegliche-gesamtstrafenbildung-55-stgb`.

## Anhörungstermin — typische Strategie

- Schriftliche Eingabe vor dem Termin (Aktuelle Sozialdaten, Therapienachweis, Quittungen).
- Mandant erscheint persoenlich und aeussert sich klar zur eigenen Situation.
- Konkrete mildere Massnahme vorschlagen — das Gericht muss sie ausdruecklich erwaegen (§ 56f Abs. 2 StGB).

## Typische Fehler

- **Anhörung versaeumt** oder rein formal abgewickelt: Verfahrensruege moeglich.
- **Mildere Massnahmen** wurden nicht gepruegt — Pflicht des Gerichts; Beschluss-Begruendung pruefen.
- **Frist** der sofortigen Beschwerde versaeumt (1 Woche).
- **Geldauflage**-Verstoss bei nachgewiesener Zahlungsunfaehigkeit: Widerruf unverhaeltnismaessig.
- **Neue Tat** in der Bewaehrungszeit noch nicht rechtskraeftig: Widerruf zumeist verfrueht.

## Quellen und Stand 05/2026

- § 56f StGB in der geltenden Fassung.
- §§ 453, 311 StPO.
- BGH-Linie zur "Beharrlichkeit" und zum Verhaeltnis "Widerruf vs. Gesamtstrafe" — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `freiheitsstrafe-ohne-bewaehrung-vollstreckung`

_Freiheitsstrafe ohne Bewaehrung. Anrechnung Untersuchungshaft und Auslieferungshaft § 51 StGB. Vollstreckungsplanung Reststrafenaussetzung § 57 StGB Halbstrafe Drittel. Lebenslang § 57a StGB. Strafaufschub § 456 StPO. Strafunterbrechung § 455 StPO. § 35 BtMG Therapie statt Strafe. Beleidigte Voll..._

# Freiheitsstrafe ohne Bewaehrung — Vollstreckung

## Arbeitsbereich

Freiheitsstrafe ohne Bewaehrung. Anrechnung Untersuchungshaft und Auslieferungshaft § 51 StGB. Vollstreckungsplanung Reststrafenaussetzung § 57 StGB Halbstrafe Drittel. Lebenslang § 57a StGB. Strafaufschub § 456 StPO. Strafunterbrechung § 455 StPO. § 35 BtMG Therapie statt Strafe. Beleidigte Vollstreckungsplanung; Verteidigung im Vollstreckungsstadium. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Wird die Freiheitsstrafe nicht zur Bewaehrung ausgesetzt, beginnt das Vollstreckungsverfahren. Wichtige Stellschrauben sind die Anrechnung der U-Haft (§ 51 StGB), die Reststrafenaussetzung (§§ 57, 57a StGB), Strafaufschub (§ 456 StPO), Strafunterbrechung (§ 455 StPO) und § 35 BtMG.

## Wann brauchen Sie diese Skill?

- Der Mandant ist zu einer Freiheitsstrafe ohne Bewaehrung verurteilt; Sie planen das weitere Verteidigungsvorgehen.
- U-Haft wurde verbuesst und muss korrekt angerechnet werden.
- Reststrafenaussetzung nach 2/3, 1/2 oder bei Lebenslang nach 15 Jahren steht an.
- Strafaufschubs- oder Strafunterbrechungsantrag wegen besonderer Lage (Schwangerschaft, schwere Krankheit, betreuungspflichtige Kinder).
- § 35 BtMG Therapie statt Strafvollzug.

## Rechtliche Grundlagen

- **§ 51 StGB** — Anrechnung von Untersuchungshaft, einstweiliger Unterbringung, Auslieferungshaft und vergleichbarer Freiheitsentziehung. Pflicht zur vollstaendigen Anrechnung, sofern keine ausdrueckliche Versagung wegen vorwerfbaren Verhaltens.
- **§ 57 StGB** — Aussetzung des Strafrests bei zeitiger Freiheitsstrafe; Regelfall nach 2/3, in besonderen Faellen nach 1/2.
- **§ 57a StGB** — Aussetzung des Strafrests bei lebenslanger Freiheitsstrafe; frueheste Pruefung nach 15 Jahren; **besondere Schwere der Schuld** kann verlaengern (§ 57a Abs. 1 Satz 1 Nr. 2 StGB).
- **§ 57b StGB** — Aussetzung bei Gesamtstrafe aus lebenslanger und zeitiger Freiheitsstrafe.
- **§ 35 BtMG** — Zurueckstellung der Strafvollstreckung bei Betaeubungsmittelabhaengigkeit zugunsten Therapie.
- **§ 36 BtMG** — Anrechnung der Therapiezeit.
- **§ 455 StPO** — Aufschub der Vollstreckung; Strafunterbrechung wegen Gesundheit.
- **§ 456 StPO** — Aufschub aus persönlichen Gruenden.
- **§ 456a StPO** — Absehen von Vollstreckung bei Auslaendern (Auslieferung/Ausweisung).
- **§ 462a StPO** — Strafvollstreckungskammer ist zuständig für Reststrafenaussetzung bei zeitiger Strafe ab 9 Monaten.

## Anrechnung U-Haft (§ 51 StGB)

- **Vollstaendig anzurechnen**: jeder Tag U-Haft, einstweilige Unterbringung, Auslieferungshaft.
- **Ausnahme**: vorwerfbares Verhalten des Verurteilten (selbstverschuldete Verlaengerung); Anrechnung ganz oder teilweise versagt — Urteilsformel pruefen.
- **Anrechnungssatz**: 1 Tag U-Haft = 1 Tag Freiheitsstrafe (Standard).
- **Massregel-Anrechnung**: Bei Sicherungsverwahrung oder § 64 StGB im Vorgriff kann § 67 Abs. 4 StGB greifen.

## Reststrafenaussetzung (§ 57 StGB)

### 2/3 (§ 57 Abs. 1 StGB)

- Pruefung **von Amts wegen** nach Verbuessung von 2/3.
- Erforderlich: positive Sozialprognose und Zustimmung des Verurteilten.
- Bewaehrungszeit 2 bis 5 Jahre.
- Anhörung durch Strafvollstreckungskammer (§ 454 StPO).

### 1/2 (§ 57 Abs. 2 StGB)

- Pruefung nur bei besonderen Umstaenden.
- Voraussetzungen:
 - Erstvollverbuesser ohne einschlaegige Vorbelastung, **oder**
 - besondere Umstaende der Tat, der Persoenlichkeit oder der Entwicklung im Vollzug.
- Frueheste Pruefung nach Verbuessung von 1/2 der Strafe, jedoch mindestens 6 Monate.

### Lebenslang (§ 57a StGB)

- Frueheste Pruefung nach **15 Jahren**.
- Besondere Schwere der Schuld (§ 57a Abs. 1 Satz 1 Nr. 2 StGB) kann zusaetzliche Mindestverbuessungsdauer begruenden — wird durch das **Tatgericht** im Urteilstenor festgestellt.
- Bei Gesamtstrafe mit lebenslang siehe § 57b StGB.

## § 35 BtMG — Therapie statt Strafvollzug

- Voraussetzung: Tat begangen wegen Betaeubungsmittelabhaengigkeit; Strafe wegen Verstoss gegen BtMG oder andere Straftat in BtM-Zusammenhang; Strafe nicht mehr als 2 Jahre (vollstreckbarer Rest).
- Antrag der Staatsanwaltschaft mit Zustimmung des Verurteilten.
- Therapieaufenthalt wird auf die Strafe angerechnet (§ 36 BtMG).

## Strafaufschub / Strafunterbrechung (§§ 455, 456 StPO)

- **§ 455 Abs. 1 StPO** — Strafaufschub bei Geisteskrankheit.
- **§ 455 Abs. 2-4 StPO** — bei schwerer Krankheit, lebensgefahr; Vollstreckungsbehoerde entscheidet.
- **§ 455a StPO** — Strafunterbrechung in besonderen Faellen.
- **§ 456 StPO** — Aufschub aus persönlichen Gruenden (z.B. Pruefung, Schwangerschaft, betreuungspflichtige Kinder) auf laengstens 4 Monate.

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Urteilsformel pruefen**: U-Haft-Anrechnung korrekt? Wenn nein, Beschluss der Vollstreckungsbehoerde nach § 458 StPO anregen.
2. **§ 35 BtMG** pruefen, wenn Tat im BtM-Zusammenhang.
3. **Strafaufschub / -unterbrechung** pruefen, wenn persönliche Lage es erfordert.
4. **Reststrafenaussetzung** rechtzeitig vorbereiten:
 - Sozialprognose mit Schulungs-/Therapie-/Arbeitsangebot für die Bewaehrungszeit.
 - Anhörungsschriftsatz bei der Strafvollstreckungskammer.
5. **Vollstreckungsplan** mit dem Mandanten besprechen: realistische Erwartung, JVA-Standort, Familienkontakt, Bildungs- und Therapieangebote im Vollzug.

## Typische Fehler

- **U-Haft-Anrechnung** uebersehen oder unvollstaendig (Tag fehlt).
- **§ 35 BtMG** zu spaet beantragt: nach Vollzugsbeginn wird oft abgelehnt.
- **Reststrafenaussetzung** ohne ausreichende Vorbereitung: Sozialdaten fehlen.
- **Anhörung** nicht persoenlich wahrgenommen: Strafvollstreckungskammer trifft auf einen "unsichtbaren" Verurteilten.
- **Sofortige Beschwerde** gegen ablehnenden Reststrafenaussetzungs-Beschluss versaeumt (Frist 1 Woche, § 311 StPO).

## Quellen und Stand 05/2026

- §§ 38, 51, 57, 57a, 57b StGB in der geltenden Fassung.
- §§ 35, 36 BtMG.
- §§ 454, 455, 455a, 456, 456a, 458, 462a StPO.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `freiheitsstrafe-strafmass-geldstrafe`

_Konkrete Zumessung der Freiheitsstrafe nach §§ 38 39 46 StGB. Strafrahmen pruefen, Strafhoehe innerhalb des Schuldrahmens bestimmen, Wechselwirkung mit Bewaehrung (§ 56 StGB) und Aussetzung des Strafrests (§ 57 StGB). Faustwerte für typische Tatbestaende. Schnittstelle Verteidigungsplaedoyer, Ant..._

# Freiheitsstrafe — Strafmass pruefen

## Arbeitsbereich

Konkrete Zumessung der Freiheitsstrafe nach §§ 38 39 46 StGB. Strafrahmen pruefen, Strafhoehe innerhalb des Schuldrahmens bestimmen, Wechselwirkung mit Bewaehrung (§ 56 StGB) und Aussetzung des Strafrests (§ 57 StGB). Faustwerte für typische Tatbestaende. Schnittstelle Verteidigungsplaedoyer, Antragsstrafe Staatsanwaltschaft, Urteilsbegruendung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Sobald feststeht, dass Freiheitsstrafe verhaengt wird, ist innerhalb des konkreten Strafrahmens die **Hoehe** zu bestimmen. Grundlage ist § 46 StGB. § 38 StGB regelt die zeitige Freiheitsstrafe (1 Monat bis 15 Jahre), § 39 StGB die Bemessung (Monate, Jahre und Monate). Die Hoehe entscheidet ueber Bewaehrungsfaehigkeit (§§ 56, 57 StGB).

## Wann brauchen Sie diese Skill?

- Sie verteidigen in der Hauptverhandlung und plaedieren auf konkrete Strafhoehe.
- Sie pruefen den Strafantrag der Staatsanwaltschaft auf Angemessenheit.
- Sie sondieren eine Verstaendigung; Strafrahmen-Untergrenze und -Obergrenze bilden den Handlungsspielraum.
- Sie schreiben die Strafzumessung im Urteil oder pruefen sie revisionsmaessig.

## Rechtliche Grundlagen

- **§ 38 StGB** — Zeitige Freiheitsstrafe 1 Monat bis 15 Jahre; lebenslang.
- **§ 39 StGB** — Bemessung: bis 1 Jahr in vollen Wochen und Monaten; ueber 1 Jahr in Jahren und Monaten.
- **§ 46 StGB** — Grundsatz; vgl. `paragraph-46-stgb-grundsatz-strafzumessung`.
- **§ 47 StGB** — Vorrang Geldstrafe bei kurzer Freiheitsstrafe; vgl. `geldstrafe-vs-freiheitsstrafe-47-stgb`.
- **§ 56 StGB** — Aussetzung zur Bewaehrung; vgl. `bewaehrung-56-stgb-positive-sozialprognose`.
- **§ 57 StGB** — Aussetzung des Strafrests bei zeitiger Freiheitsstrafe.
- **§ 57a StGB** — Aussetzung des Strafrests bei lebenslanger Freiheitsstrafe (besondere Schwere der Schuld § 57a Abs. 1 Satz 1 Nr. 2 StGB).

## Strafzumessungs-Grundsatz

- **Spielraum schuldangemessener Strafe**: Ober- und Untergrenze; innerhalb davon nach Praevention bemessen.
- **Wechselwirkung Strafhoehe und Bewaehrung**:
 - Bis 1 Jahr: Bewaehrung Regelfall bei positiver Sozialprognose (§ 56 Abs. 1 StGB).
 - 1 bis 2 Jahre: Bewaehrung moeglich, aber nur bei besonderen Umstaenden (§ 56 Abs. 2 StGB).
 - Ueber 2 Jahre: keine Bewaehrung mehr.
- Verteidigung achtet darauf, ob ein Strafmass moeglichst unter 2 Jahre (und idealerweise unter 1 Jahr) liegt.

## Schritt-für-Schritt-Anleitung

1. **Konkreten Strafrahmen** feststellen (vgl. `strafrahmen-und-strafzumessungsstufen`).
2. **Schuldrahmen-Spielraum** bilden: untere und obere Grenze schuldangemessener Strafe.
3. **Strafzumessungstatsachen** aus § 46 Abs. 2 StGB sammeln und gewichten (vgl. `strafzumessungs-tatsachen-46-ii-stgb`).
4. **Strafmilderungsgruende** pruefen: §§ 46a, 17, 21, 23 Abs. 2, 27 Abs. 2, 28 Abs. 1, 49 StGB.
5. **Bewaehrungsperspektive** im Blick: Wenn 1-Jahres- oder 2-Jahres-Schwelle in Reichweite, Argumente entsprechend ausrichten.
6. **Lange Verfahrensdauer** als Kompensationsfaktor pruefen (Art. 6 EMRK; Vollstreckungsmodell der st. Rspr.).
7. **Anrechnung** U-Haft / Auslieferungshaft nach § 51 StGB; vgl. `freiheitsstrafe-ohne-bewaehrung-vollstreckung`.

## Faustwerte (orientierend, kein Praejudiz)

| Tatbestandsbereich | Typischer Bereich |
|---|---|
| Einfacher Diebstahl § 242 Erstverstoss | 30-90 Tagessaetze; selten Freiheitsstrafe |
| Wohnungseinbruchsdiebstahl § 244 Abs. 4 (Mindeststrafe 1 Jahr) | 1 bis 3 Jahre |
| Betrug § 263 mittlere Schaeden | Geldstrafe bis 1 Jahr |
| Betrug § 263 schwere Schaeden / gewerbsmaessig | 1 bis 3 Jahre |
| Koerperverletzung § 223 ohne Vorbelastung | Geldstrafe bis 6 Monate |
| Gefaehrliche Koerperverletzung § 224 | 6 Monate bis 3 Jahre |
| Schwere Koerperverletzung § 226 | 1 Jahr bis 10 Jahre |
| Raub § 249 Abs. 1 | Mindeststrafe 1 Jahr, oft 2-4 Jahre |
| Schwerer Raub § 250 Abs. 1 | 3 bis 6 Jahre |
| Totschlag § 212 | 5 bis 15 Jahre |
| Mord § 211 | lebenslang |

Diese Werte ersetzen **keinen** Einzelfall; sie zeigen, wo regional, gerichtsbezogen und individuell zumeist Verhandlungsraum liegt.

## Verteidigungs-Hebel

- Strafmilderungsgruende konsequent aufzeigen: §§ 46a, 17, 21 StGB.
- Lange Verfahrensdauer ruegen und Kompensation einfordern.
- Bewaehrungsperspektive sichern: Argumente zur Sozialprognose vorbereiten.
- Wirtschaftliche und persönliche Verhaeltnisse substantiiert vortragen.

## Antrags-Strategie Staatsanwaltschaft

- Antragstrafe darf nicht hinter der Schuld zurueckbleiben.
- Bei Bewaehrungsantrag konkret Vortrag zur Sozialprognose.
- Bei keinem Bewaehrungsantrag konkret zu den negativen Prognosefaktoren.
- Strafzumessungsrichtlinien der Landes-Justizverwaltungen koennen orientieren (siehe je nach Bundesland; nicht bindend).

## Typische Fehler

- **Schuldrahmen-Begruendung fehlt**: Urteil nennt nur den konkret verhaengten Wert ohne Bandbreite; revisionsanfaellig.
- **Bewaehrungsschwelle** uebersehen: Strafhoehe knapp ueber 2 Jahren ohne Begruendung der Schwere; Verteidigung sollte vor Urteilsverkuendung punktgenau argumentieren.
- **Lange Verfahrensdauer** nicht kompensiert.
- **U-Haft-Anrechnung** in der Urteilsformel uebersehen (§ 51 StGB).
- **Doppelverwertung** Tatbestandsmerkmale.

## Quellen und Stand 05/2026

- §§ 38, 39, 46, 47, 49, 51, 56-57a StGB in der geltenden Fassung.
- Art. 6 Abs. 1 EMRK Verfahrensdauer.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `geldstrafe-tagessatzanzahl-bestimmen`

_Bestimmung der Tagessatzanzahl der Geldstrafe nach § 40 Abs. 1 StGB. 5 bis 360 Tagessaetze als Grundgrenze; bei Gesamtgeldstrafe bis 720 Tagessaetze. Die Anzahl bildet die Schuldkomponente und folgt § 46 StGB. Abgrenzung zur Tagessatzhoehe, die das Nettoeinkommen abbildet. Schnittstelle Strafbefe..._

# Tagessatzanzahl der Geldstrafe — § 40 Abs. 1 StGB

## Arbeitsbereich

Bestimmung der Tagessatzanzahl der Geldstrafe nach § 40 Abs. 1 StGB. 5 bis 360 Tagessaetze als Grundgrenze; bei Gesamtgeldstrafe bis 720 Tagessaetze. Die Anzahl bildet die Schuldkomponente und folgt § 46 StGB. Abgrenzung zur Tagessatzhoehe, die das Nettoeinkommen abbildet. Schnittstelle Strafbefehl, Hauptverhandlung, Gesamtstrafe. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Bei der Geldstrafe wird die **Schuld** ueber die **Anzahl der Tagessaetze** ausgedrueckt; die **Hoehe** des einzelnen Tagessatzes spiegelt die wirtschaftlichen Verhaeltnisse wider (§ 40 Abs. 2 StGB; vgl. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst`). Dieser Skill konzentriert sich auf die Zahl.

## Wann brauchen Sie diese Skill?

- Sie pruefen einen Strafbefehl mit Tagessatzfestsetzung und wollen die Schuldkomponente ueberpruefen.
- Sie bereiten den Strafantrag der Staatsanwaltschaft für ein Vergehen vor.
- Sie schreiben die Strafzumessung im Urteil oder pruefen sie im Revisionsverfahren.
- Sie bilden eine Gesamtgeldstrafe nach §§ 53, 54 StGB.

## Rechtliche Grundlagen

- **§ 40 Abs. 1 Satz 2 StGB** — "Die Geldstrafe betraegt mindestens fuenf und, soweit das Gesetz nichts anderes bestimmt, hoechstens dreihundertsechzig volle Tagessaetze."
- **§ 54 Abs. 2 Satz 2 StGB** — Gesamtgeldstrafe bis 720 Tagessaetze.
- **§ 47 StGB** — Vorrang Geldstrafe vor kurzer Freiheitsstrafe unter 6 Monaten; vgl. `geldstrafe-vs-freiheitsstrafe-47-stgb`.
- **§ 41 StGB** — Geldstrafe neben Freiheitsstrafe moeglich, wenn der Taeter durch die Tat sich bereichert hat oder zu bereichern versucht hat.
- **§ 53 Abs. 2 StGB** — Bei Realkonkurrenz mehrerer Geldstrafen Gesamtgeldstrafe.

## Strafzumessungs-Grundsatz

- Die Tagessatzanzahl folgt allein **§ 46 StGB**; Strafzumessungstatsachen wie Vorleben, Tatfolgen, Nachtatverhalten sind hier abzubilden.
- Die Hoehe darf **nicht** in die Anzahl einfliessen — das waere eine unzulaessige Vermengung.
- Schuldrahmen-Theorie auch hier: Innerhalb des "Spielraums schuldangemessener Strafe" wird konkret bestimmt.

## Schritt-für-Schritt-Anleitung

1. **Strafrahmen pruefen**: Ist Geldstrafe ueberhaupt vorgesehen? Wird die Strafrahmen-Obergrenze des Tatbestands beruehrt (z.B. § 242 StGB: bis 5 Jahre oder Geldstrafe; § 263 Abs. 1 StGB: bis 5 Jahre oder Geldstrafe).
2. **Umrechnungsschluessel** beachten: 30 Tagessaetze = 1 Monat Freiheitsstrafe (faustregelhafte Aequivalenz; nicht starr, aber Orientierung).
3. **Strafzumessungstatsachen** nach § 46 StGB sammeln und gewichten (vgl. `strafzumessungs-tatsachen-46-ii-stgb`).
4. **Anzahl bestimmen** im Schuldrahmen.
5. **Kein Lappenanteil** — § 40 Abs. 1 StGB verlangt "volle" Tagessaetze.
6. **Bei Gesamtgeldstrafe** (§§ 53, 54 StGB): hoechste Einzelstrafe als Einsatzstrafe, dann Erhoehung um angemessenen Bruchteil bis maximal 720 Tagessaetze; vgl. `gesamtstrafenbildung-53-54-stgb-erste-instanz`.

## Faustwerte (orientierend, nicht starr)

| Bereich | Tagessatzanzahl |
|---|---|
| Bagatelle, ggf. § 153a StPO statt Strafbefehl | 5-30 |
| Mittlere Vergehen ohne Vorbelastung | 30-90 |
| Mittlere Vergehen mit Vorbelastung | 90-180 |
| Schwere Vergehen, Mehrtaeterstrukturen | 180-360 |
| Gesamtgeldstrafe Schwer-Komplex | 360-720 |

Die Tabelle ersetzt **keine** Einzelfallbetrachtung; sie zeigt nur das Spielfeld.

## Sonderfaelle

- **Mehrere Einzelstrafen** (Realkonkurrenz, § 53 StGB): Gesamtgeldstrafe nach § 54 Abs. 2 StGB; Erhoehung der hoechsten Einzelstrafe; max. 720 Tagessaetze.
- **Geldstrafe neben Freiheitsstrafe** (§ 41 StGB): nur wenn Bereicherungsabsicht und Bereicherung erkennbar; sonst Aufhebungsgrund.
- **Strafbefehl** (§ 407 Abs. 2 StPO): bis 360 Tagessaetze ohne Hauptverhandlung; vgl. `strafbefehl-strafzumessung-407-stpo`.
- **Verstaendigung** (§ 257c StPO): Strafrahmen-Ober- und Untergrenze für Tagessatzanzahl koennen Verhandlungsgegenstand sein; vgl. `verstaendigung-257c-stpo-strafzumessung`.

## Typische Fehler

- **Tagessatzanzahl und -hoehe vermengt**: Schwierige wirtschaftliche Verhaeltnisse mindern die Hoehe, nicht die Anzahl.
- **Doppelverwertung**: Tatbestandsmerkmal wird in die Anzahl eingerechnet.
- **Strafrahmen ignoriert**: Bei Tatbestand mit Mindeststrafe Freiheitsstrafe ist Geldstrafe ausgeschlossen.
- **§ 47 StGB uebersehen**: Wenn das Gericht statt Geldstrafe eine kurze Freiheitsstrafe verhaengt, muss es besondere Umstaende benennen.
- **Gesamtgeldstrafe** falsch gebildet: Es duerfen nicht einfach die Einzelstrafen addiert werden; § 54 Abs. 1 Satz 2 StGB verlangt Erhoehung um eine "angemessene" Quote.

## Quellen und Stand 05/2026

- §§ 40, 41, 47, 53, 54 StGB in der geltenden Fassung.
- § 407 Abs. 2 StPO Strafbefehl.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `geldstrafe-vs-freiheitsstrafe-47-stgb`

_Vorrang der Geldstrafe vor kurzer Freiheitsstrafe nach § 47 StGB. Kurze Freiheitsstrafe unter 6 Monaten nur bei besonderen Umstaenden in der Tat oder in der Persoenlichkeit. Begruendungspflicht des Gerichts. Verhaeltnis Geldstrafe + Freiheitsstrafe (§ 41 StGB). Strategiewahl Verteidigung gegen ku..._

# Geldstrafe vs. Freiheitsstrafe — § 47 StGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

§ 47 Abs. 1 StGB enthaelt eine gesetzgeberische Wertentscheidung **gegen** kurze Freiheitsstrafen. Eine Freiheitsstrafe unter sechs Monaten darf das Gericht nur verhaengen, wenn besondere Umstaende, die in der Tat oder der Persoenlichkeit des Taeters liegen, die Verhaengung der Freiheitsstrafe zur Einwirkung auf den Taeter oder zur Verteidigung der Rechtsordnung unerlaesslich machen. § 47 Abs. 2 StGB regelt das Verhaeltnis bei Tatbestaenden, die nur Freiheitsstrafe vorsehen.

## Wann brauchen Sie diese Skill?

- Sie verteidigen gegen einen Strafantrag oder ein Urteil mit kurzer Freiheitsstrafe und wollen auf Geldstrafe umstellen lassen.
- Sie pruefen die Strafzumessungsruege bei kurzer Freiheitsstrafe ohne ausreichende Begruendung.
- Sie verhandeln in einer Verstaendigung den Strafrahmen und wollen die Geldstrafe-Schiene sichern.
- Sie sondieren bei einem Tatbestand ohne Geldstrafe-Option, ob § 47 Abs. 2 StGB den Strafrahmen oeffnet.

## Rechtliche Grundlagen

- **§ 47 Abs. 1 StGB** — Eine Freiheitsstrafe unter sechs Monaten verhaengt das Gericht nur, wenn besondere Umstaende, die in der Tat oder in der Persoenlichkeit des Taeters liegen, die Verhaengung einer Freiheitsstrafe zur Einwirkung auf den Taeter oder zur Verteidigung der Rechtsordnung unerlaesslich machen.
- **§ 47 Abs. 2 StGB** — Wenn das Gesetz keine Geldstrafe androht und eine Freiheitsstrafe unter sechs Monaten nicht in Betracht kommt, ist auf Geldstrafe zu erkennen. Der Strafrahmen der Geldstrafe ergibt sich aus § 40 Abs. 1 StGB (5 bis 360 Tagessaetze).
- **§ 41 StGB** — Geldstrafe **neben** Freiheitsstrafe bei Bereicherungsabsicht.

## Strafzumessungs-Grundsatz

§ 47 StGB ist Ausdruck der **Subsidiaritaet** der kurzen Freiheitsstrafe. Praevention und Schuld stehen in einer Stufung:

1. Erste Wahl: Geldstrafe.
2. Nur in Ausnahmefaellen: kurze Freiheitsstrafe; das Gericht muss "besondere Umstaende" konkret benennen.
3. Auch dann moeglichst mit Bewaehrung (§ 56 StGB).

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Strafrahmen pruefen**: Sieht der Tatbestand Geldstrafe vor? Wenn nein, Klappentest für § 47 Abs. 2 StGB.
2. **Argumente gegen besondere Umstaende sammeln**:
 - Erstmaliger Verstoss.
 - Niedrige kriminelle Energie.
 - Soziale Integration: Beruf, Familie, intakte Bindungen.
 - Akute persönliche Belastung (Sucht, Krise) bereits in Behandlung.
 - Kein einschlaegiges Vorleben.
3. **Tagessatz-Berechnung beilegen**, damit das Gericht Geldstrafe konkret verhaengen kann; vgl. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst`.
4. **In der Hauptverhandlung** ausdruecklich beantragen: "Wir beantragen Verhaengung einer Geldstrafe; eine Freiheitsstrafe ist nach § 47 Abs. 1 StGB nicht unerlaesslich, da [...]."
5. **Wenn doch kurze Freiheitsstrafe**: hilfsweise Bewaehrung (§ 56 StGB) sichern; vgl. `bewaehrung-56-stgb-positive-sozialprognose`.
6. **In der Revision**: § 47 Abs. 1 StGB ist eine Vorschrift, deren Verletzung mit der Sachruege geltend gemacht werden kann; Begruendungsmangel im Urteil ist regelmäßiger Aufhebungsgrund.

## Schritt-für-Schritt-Anleitung (Anklage)

- Wenn kurze Freiheitsstrafe angestrebt wird, **konkret** vortragen, welche besonderen Umstaende vorliegen:
 - Einschlaegige Vorbelastung, mehrfache Bewaehrungsversager.
 - Tat-Spezifika (z.B. Gewerbsmaessigkeit, Bandenstruktur, Wiederholungstat in Bewaehrung).
 - Schwergewichtige Tatfolgen ueber Tatbestandsmerkmal hinaus.
- Verteidigung der Rechtsordnung nur bei massiven oder oeffentlichkeitswirksamen Faellen tragfaehig.

## Strafmildernde Wirkung gegenueber Geldstrafe

- Geldstrafe statt Freiheitsstrafe ist **kein** automatischer Strafzumessungsabschlag. Anzahl der Tagessaetze kann hoch sein, ohne dass das Strafmass unverhaeltnismaessig wird.
- Faustregel der Praxis: 30 Tagessaetze entsprechen ungefaehr 1 Monat Freiheitsstrafe (orientierend).

## Verhaeltnis zu § 56 StGB (Bewaehrung)

Wird trotzdem eine kurze Freiheitsstrafe (3 bis 6 Monate) verhaengt, ist Bewaehrung nach § 56 Abs. 1 StGB (Strafe bis 1 Jahr) Standard, sofern Sozialprognose positiv ist; vgl. `bewaehrung-56-stgb-positive-sozialprognose`.

## Typische Fehler

- **Pauschale Begruendung** im Urteil: "Die Schwere der Tat erfordert eine Freiheitsstrafe." Das ist keine besondere Umstaende-Begruendung iSv § 47 Abs. 1 StGB; Revisionsruege.
- **Verteidigung der Rechtsordnung** ohne Tatsachen: Floskel, die in der Revision regelmaessig faellt.
- **Vorstrafen** allein begruenden in der Regel nicht ohne weiteres die Unerlaesslichkeit; nur einschlaegige und intensive Vorbelastung.
- **§ 41 StGB falsch** angewendet: Geldstrafe neben Freiheitsstrafe **nur** bei Bereicherungsabsicht.

## Quellen und Stand 05/2026

- §§ 40, 41, 47, 56 StGB in der geltenden Fassung.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`

_Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung wenn Einbeziehung nach § 55 StGB nicht moeglich ist (Strafe bereits vollstreckt, verjaehrt oder erlassen, Bewaehrung abgelaufen, Auslandsstrafen). BGH-staendige Linie: Schutzzweck des § 55 StGB rechtfertigt Strafabschlag als rechtspolitisch..._

# Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung

## Arbeitsbereich

Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung wenn Einbeziehung nach § 55 StGB nicht moeglich ist (Strafe bereits vollstreckt, verjaehrt oder erlassen, Bewaehrung abgelaufen, Auslandsstrafen). BGH-staendige Linie: Schutzzweck des § 55 StGB rechtfertigt Strafabschlag als rechtspolitisches Ausgleichs-Element. Anwendung in Hauptverhandlung und Beschluss-Verfahren. Verteidigerantrag und Begruendungspflicht. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Wenn eine nachtraegliche Gesamtstrafenbildung nach § 55 StGB **nicht** moeglich ist — typischerweise weil die fruehere Strafe bereits vollstreckt, verjaehrt oder erlassen ist (auch nach abgelaufener Bewaehrung) —, kann der **Haerteausgleich** als nicht-kodifiziertes, von der staendigen Rechtsprechung entwickeltes Instrument zum Tragen kommen. Er gleicht die zufaelligen Nachteile aus, die durch die getrennte Aburteilung entstehen.

**BGH-staendige Linie**: Der Schutzzweck des § 55 StGB darf nicht durch verfahrenstechnische Zufaelle (Reihenfolge der Verurteilungen, Tempo der Vollstreckung, Ausland) entwertet werden. Wenn eine Einbeziehung an einem ausserhalb der Schuld liegenden Umstand scheitert, ist ein Strafabschlag zu gewaehren. **Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.**

## Wann brauchen Sie diese Skill?

- Mandant ist bereits einmal verurteilt; die fruehere Strafe wurde mittlerweile vollstreckt oder die Bewaehrung ist erlassen worden.
- Eine weitere Tat des Mandanten, die er **vor** der frueheren Verurteilung begangen hat, wird nun abgeurteilt.
- Sie pruefen ein Urteil, das die Sondersituation uebersehen hat.
- Auslandsstrafen liegen vor und koennen nicht einbezogen werden.

## Rechtliche Grundlagen

- **§ 55 StGB** — Nachtraegliche Gesamtstrafenbildung; vgl. `nachtraegliche-gesamtstrafenbildung-55-stgb`.
- **§ 46 StGB** — Strafzumessungsgrundsatz; Haerteausgleich wird als Strafzumessungsfaktor in die konkrete Strafe eingearbeitet.
- **§ 267 Abs. 3 StPO** — Begruendung; Haerteausgleich muss als bestimmender Strafzumessungsgrund mitgeteilt werden.
- **BGH-staendige Linie**: Schutzzweck des § 55 StGB rechtfertigt rechnerischen Strafabschlag bei zufaelliger Nichteinbeziehung. Aktenzeichen verifizieren.

## Konstellationen, die typisch Haerteausgleich ausloesen

### 1. Fruehere Strafe vollstreckt

Wird die fruehere Strafe vor der jetzigen Verurteilung vollstaendig vollstreckt, kann sie nicht mehr in eine Gesamtstrafe einbezogen werden. Der Verurteilte ist gegenueber einer gemeinsamen Aburteilung schlechter gestellt.

### 2. Bewaehrungszeit abgelaufen / Strafe erlassen (§ 56g StGB)

Wird die Bewaehrung gluecklich beendet und die Strafe erlassen, kann sie nicht mehr einbezogen werden. Auch hier waere eine gemeinsame Aburteilung guenstiger gewesen.

### 3. Verjährung der frueheren Strafe

Die Strafe ist verjaehrt; keine Einbeziehung mehr.

### 4. Auslandsstrafen

Auslandsstrafen werden grundsaetzlich **nicht** in eine nachtraegliche Gesamtstrafe nach § 55 StGB einbezogen (st. Rspr.; Az verifizieren). Ein Haerteausgleich kann bei rein "schicksalhaft" zustandegekommener Auslandsstrafe geboten sein.

### 5. Strafe aus Strafbefehl bereits gezahlt

Eine vollstaendig gezahlte Geldstrafe aus Strafbefehl wird nicht einbezogen.

## Hoehe und Form des Haerteausgleichs

- **Kein** starres Berechnungsschema.
- **Orientierung**: Was waere die Gesamtstrafe gewesen, wenn beide Taten in einem Verfahren abgeurteilt worden waeren?
- **Differenz** zwischen hypothetischer Gesamtstrafe und kumulierten Einzelstrafen kann als Massstab dienen.
- **Strafabschlag** wird auf die nunmehr zu verhaengende Strafe angerechnet — entweder durch Senkung der Einzelstrafe oder durch ausdruecklichen Abschlag in der Strafzumessungsbegruendung.

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Vorverurteilungen** und Status pruefen: BZRG-Auszug, Vollstreckungsakte, Bewaehrungsentscheidungen.
2. **Zaesur-Pruefung**: Wurde die abzuurteilende Tat **vor** der frueheren Verurteilung begangen?
3. **Einbeziehung pruefen** (§ 55 StGB):
 - Ist die fruehere Strafe noch offen? Dann § 55 StGB; vgl. `nachtraegliche-gesamtstrafenbildung-55-stgb`.
 - Ist sie schon vollstreckt / erlassen / verjaehrt? Dann **Haerteausgleich**.
4. **Antrag** in der Hauptverhandlung oder im Schriftsatz:

 ```
 Wir beantragen, bei der Strafzumessung einen Haerteausgleich
 zu gewaehren, da die Tat vom [Datum] vor der Verurteilung
 vom [Datum] begangen wurde und eine Einbeziehung in eine
 Gesamtstrafe nach § 55 StGB allein deshalb ausscheidet,
 weil die damals verhaengte Strafe inzwischen [vollstreckt /
 erlassen / verjaehrt] ist. Eine gemeinsame Aburteilung haette
 zu einer wesentlich niedrigeren Gesamtstrafe gefuehrt.
 ```

5. **Hoehe** des Haerteausgleichs vortragen:
 - Hypothetische Gesamtstrafe bei gemeinsamer Aburteilung berechnen.
 - Differenz zwischen dieser hypothetischen Gesamtstrafe und der jetzt zu erwartenden kumulierten Strafenlast.
 - Strafabschlag konkret beantragen (z.B. "Strafabschlag von [X] Monaten" oder "Reduktion der zu verhaengenden Strafe um etwa [X] %").
6. **Begruendungspflicht** im Urteil: Das Gericht muss den Haerteausgleich als bestimmenden Strafzumessungsgrund angeben (§ 267 Abs. 3 StPO).

## Verhaeltnis zu § 55 StGB

| Situation | Rechtsfolge |
|---|---|
| Fruehere Strafe noch offen | § 55 StGB Einbeziehung; nachtraegliche Gesamtstrafe |
| Fruehere Strafe vollstreckt / verjaehrt / erlassen | **Haerteausgleich** im Rahmen § 46 StGB |
| Tat **nach** Vorverurteilung begangen (Zaesur uebersprungen) | Weder § 55 StGB noch Haerteausgleich; reguläre Einzelstrafe |
| Auslandsstrafen | § 55 StGB scheidet aus; Haerteausgleich in Ausnahmefaellen |

## Sonderkonstellationen

### Bewaehrungswiderruf-Drohung

Wenn die fruehere Strafe noch in Bewaehrung laeuft, ist die Einbeziehung nach § 55 StGB zumeist guenstiger als ein Bewaehrungswiderruf (§ 56f StGB) + getrennte neue Strafe. Verteidiger pruefen, welcher Weg wirtschaftlich besser ist; vgl. `bewaehrungswiderruf-56f-stgb`.

### Mehrere Zaesuren

Bei mehreren Vorverurteilungen ist sorgfaeltig zu pruefen, welche Strafen einbeziehbar sind und welche nicht — und ob für die nicht einbeziehbaren ein Haerteausgleich vorzunehmen ist.

### Geldstrafe schon gezahlt

Auch eine bereits gezahlte Geldstrafe kann Haerteausgleich begruenden, wenn sie haette einbezogen werden koennen (st. Rspr.; Az verifizieren).

## Begruendung im Urteil (Muster-Element)

```
[...] Bei der Strafzumessung war zu beruecksichtigen, dass die hier
abzuurteilende Tat vor der Verurteilung des Angeklagten durch
[Gericht] vom [Datum] (Az.: [...]) begangen wurde. Eine Einbeziehung
der damals verhaengten Strafe von [Einzelstrafe] in eine Gesamtstrafe
nach § 55 StGB ist nicht moeglich, da diese Strafe bereits vollstaendig
[vollstreckt / erlassen / verjaehrt] ist.

Es waere eine Gesamtstrafe von voraussichtlich [hypothetische Strafe]
gebildet worden. Daraus errechnet sich eine zu beruecksichtigende
Haerte, die das Gericht durch einen Abschlag von [X] Monaten
ausgleicht. Die Strafe von [konkrete Strafe] beruecksichtigt diesen
Haerteausgleich.
```

## Typische Fehler

- **Haerteausgleich uebersehen**: revisionsrechtlich relevanter Strafzumessungsmangel.
- **Hoehe pauschal**: Das Gericht muss die hypothetische Gesamtstrafe und die Differenz nachvollziehbar machen.
- **Verwechslung mit § 55 StGB**: Haerteausgleich ist subsidiaer; vorrangig ist die Einbeziehung nach § 55 StGB.
- **§ 55 StGB-Voraussetzungen** nicht systematisch geprueft: zuerst Zaesur, dann Status der frueheren Strafe.
- **Bewaehrungsstrafe** als "erlassen" angesehen, obwohl die Bewaehrung noch laeuft.
- **Auslandsstrafen** automatisch als haerteausgleichsbeduerftig gewertet — die st. Rspr. ist hier restriktiver; Einzelfallpruefung.

## Quellen-Recherche-Hinweis

Die BGH-Rspr. zum Haerteausgleich bei nicht moeglicher Einbeziehung nach § 55 StGB ist umfangreich und gefestigt; Leitentscheidungen finden sich beispielsweise in BGHSt-Bestaenden zur Gesamtstrafenbildung. **Vor Zitat im Schriftsatz immer Aktenzeichen in dejure.org oder openjur.de verifizieren**, da konkrete Az nicht aus Modellwissen uebernommen werden duerfen (vgl. Quellenregel `references/zitierweise.md`).

## Quellen und Stand 05/2026

- § 55 StGB in der geltenden Fassung.
- §§ 53, 54, 56g StGB.
- § 267 Abs. 3 StPO.
- BGH-staendige Linie zum Haerteausgleich bei nicht moeglicher Einbeziehung — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `iii-stpo-begruendungsanforderungen-strafurteil`

_Begruendungsanforderungen an die Strafzumessung im Strafurteil § 267 Abs. 3 StPO. Pflicht zur Mitteilung der bestimmenden Strafzumessungsgruende. Strafrahmen, Schuldrahmen, Strafzumessungstatsachen § 46 Abs. 2 StGB. Bewaehrungs- und Strafaussetzungsbegruendung. Strafzumessungsruege im Revisionsve..._

# Begruendung der Strafzumessung im Urteil — § 267 Abs. 3 StPO

## Arbeitsbereich

Begruendungsanforderungen an die Strafzumessung im Strafurteil § 267 Abs. 3 StPO. Pflicht zur Mitteilung der bestimmenden Strafzumessungsgruende. Strafrahmen, Schuldrahmen, Strafzumessungstatsachen § 46 Abs. 2 StGB. Bewaehrungs- und Strafaussetzungsbegruendung. Strafzumessungsruege im Revisionsverfahren. Typische Aufhebungsgruende: Pauschalbegruendung Doppelverwertung Schweigen Praevention vor Schuld. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Das Strafurteil muss die **bestimmenden** Strafzumessungsgruende in seinen Gruenden mitteilen (§ 267 Abs. 3 Satz 1 StPO). Diese Begruendung ist Voraussetzung für die revisionsrechtliche Pruefung der Strafzumessung. Bei Versagung der Bewaehrung sind die Gruende ausdruecklich darzulegen (§ 267 Abs. 3 Satz 4 StPO).

## Wann brauchen Sie diese Skill?

- Sie schreiben einen Urteilsentwurf als Richter oder Berichterstatter.
- Sie pruefen ein Urteil revisionsmaessig auf Strafzumessungsfehler.
- Sie reviewen die Strafzumessungsbegruendung im Ausbildungs- oder Qualitaetskontext.

## Rechtliche Grundlagen

- **§ 267 Abs. 3 Satz 1 StPO** — Mitteilung der bestimmenden Strafzumessungsgruende.
- **§ 267 Abs. 3 Satz 2 StPO** — Bei Geldstrafe Tagessatzhoehe und -anzahl.
- **§ 267 Abs. 3 Satz 4 StPO** — Bei Versagung der Bewaehrung Mitteilung der Gruende.
- **§ 267 Abs. 3 Satz 5 StPO** — Bei Verstaendigung Mitteilung von Inhalt und Belehrung.
- **§ 46 Abs. 1, 2, 3 StGB** — Materielle Pflicht-Inhalte.
- **§ 337 StPO** — Revision wegen Rechtsverletzung; Strafzumessung kann mit Sach- oder Verfahrensruege angegriffen werden.

## Strafzumessungs-Grundsatz

Die Begruendung muss:

- den **Strafrahmen** angeben (Grundtatbestand, Modifikation durch Regelbeispiel oder minder schweren Fall, § 49-Milderung);
- die **bestimmenden** Strafzumessungstatsachen (§ 46 Abs. 2 StGB) nennen;
- die **Abwaegung** zwischen strafmildernden und strafschaerfenden Faktoren erkennbar machen;
- bei **Geldstrafe** die Tagessatzanzahl und -hoehe getrennt begruenden (§ 267 Abs. 3 Satz 2 StPO);
- bei **Versagung der Bewaehrung** die negative Sozialprognose oder andere Gruende darlegen (§ 267 Abs. 3 Satz 4 StPO);
- bei **Verstaendigung** Inhalt und Belehrung mitteilen (§ 267 Abs. 3 Satz 5 StPO).

## Struktur einer Strafzumessungsbegruendung (Muster)

```
III. Strafzumessung

1. Strafrahmen
 Der Strafrahmen ergibt sich aus § ... StGB
 ([Strafrahmen]). [Ggf. Regelbeispiel / minder schwerer Fall
 / § 49 StGB-Milderung]. Daraus ergibt sich der konkrete
 Strafrahmen von [...] bis [...].

2. Strafzumessungstatsachen (§ 46 Abs. 2 StGB)

 a) Zugunsten des Angeklagten

 [Konkrete Tatsachen, z.B. Gestaendnis, Reue, TOA,
 Schadenswiedergutmachung, Erstverstoss, lange Verfahrens-
 dauer (Art. 6 EMRK), persönliche Verhaeltnisse].

 b) Zulasten des Angeklagten

 [Konkrete Tatsachen, z.B. Vorstrafen einschlaegig,
 Tatfolgen ueberdurchschnittlich, Tatbeteiligung mehrerer].

3. Gesamtabwaegung
 Unter Wuerdigung der genannten Umstaende hat das Gericht
 eine [Strafart] von [Strafmass] verhaengt.

4. Strafaussetzung zur Bewaehrung [oder: keine Aussetzung]
 [Sozialprognose und Begruendung].

5. Anrechnung U-Haft (§ 51 StGB)
 [Tage].

6. [Bei Verstaendigung]
 Hinweis nach § 257c Abs. 5 StPO erfolgte am [Datum].
 Inhalt der Verstaendigung: [...].
```

## Typische revisionsrechtliche Pruefpunkte

### Pauschalbegruendung

- "Unter Beruecksichtigung aller Umstaende" ohne Einzelabwaegung — revisionsanfaellig.
- BGH st. Rspr.; Aktenzeichen verifizieren.

### Doppelverwertung (§ 46 Abs. 3 StGB)

- Tatbestandsmerkmale duerfen nicht erneut strafschaerfend angefuehrt werden.
- Z.B. bei § 224 Abs. 1 Nr. 2 StGB darf das Tatmittel "Messer" nicht erneut schaerfen.

### Schweigen strafschaerfend

- Schweigen des Angeklagten darf nicht zum Nachteil verwertet werden (st. Rspr.).

### Praevention vor Schuld

- Die Strafe darf nicht aus generalpraeventiven Gruenden ueber den Schuldrahmen hinaus erhoeht werden.

### Bewaehrungsversagung ohne Begruendung

- § 267 Abs. 3 Satz 4 StPO: bei Versagung Bewaehrung muessen die Gruende mitgeteilt werden.

### Strafrahmen nicht angegeben

- Konkreter Strafrahmen muss benannt werden, sonst kann das Revisionsgericht die Schuldangemessenheit nicht pruefen.

### Verstaendigung ohne Mitteilung

- § 267 Abs. 3 Satz 5 StPO und § 273 Abs. 1a StPO: Inhalt und Belehrung muessen mitgeteilt werden.

### Tagessatzhoehe ohne Begruendung

- § 267 Abs. 3 Satz 2 StPO: Tagessatzanzahl und -hoehe getrennt darstellen.

### Lange Verfahrensdauer

- Art. 6 EMRK; Kompensation muss konkret bezeichnet werden (Vollstreckungsmodell).

## Schritt-für-Schritt-Anleitung (Verteidigung / Revisionsruege)

1. **Urteilsgruende** durchlesen, Strafzumessungsteil markieren.
2. **Strafrahmen-Pruefung**: Hat das Gericht den richtigen Strafrahmen angegeben?
3. **§ 46 Abs. 2 StGB Pruefung**: Sind die bestimmenden Strafzumessungstatsachen genannt?
4. **§ 46 Abs. 3 StGB**: Doppelverwertung?
5. **Schweigen**: Wird es strafschaerfend gewertet?
6. **Bewaehrung**: Ist die Versagung begruendet?
7. **Verstaendigung**: Mitteilung erfolgt?
8. **Tagessatzhoehe**: Begruendet?
9. **Strafzumessungsruege** formulieren als Sachruege im Revisionsverfahren; bei Verfahrensfehler als Verfahrensruege.

## Schritt-für-Schritt-Anleitung (Urteilsverfasser)

1. **Strafrahmen** explizit nennen.
2. **§ 46 Abs. 2 StGB Katalog** abarbeiten: jede einschlaegige Tatsache mit Belegstelle der Beweisaufnahme.
3. **Abwaegung** transparent: nicht nur Auflistung, sondern Gewichtung.
4. **Konkrete Strafe** im Schuldrahmen begruenden.
5. **Bewaehrungsentscheidung** ausdruecklich begruenden.
6. **U-Haft-Anrechnung** ausweisen.
7. **Verstaendigung** mitteilen, falls einschlaegig.
8. **§ 46 Abs. 3 StGB** im Hinterkopf: Tatbestandsmerkmale nicht erneut verwerten.

## Typische Fehler

- Strafzumessungs-Begruendung **vor** dem Strafmass — Reihenfolge muss sein: Strafrahmen, Abwaegung, Mass.
- **Pauschalbegruendung** mit Floskeln.
- **Doppelverwertung**.
- **Schweigen** strafschaerfend.
- **Tagessatzhoehe** ohne Einkommens-Begruendung.
- **Verstaendigung** ohne Mitteilung im Urteil (§ 267 Abs. 3 Satz 5 StPO).
- **U-Haft-Anrechnung** vergessen.

## Quellen und Stand 05/2026

- § 267 Abs. 3 StPO in der geltenden Fassung.
- §§ 46, 51 StGB.
- §§ 257c, 273 Abs. 1a, 337 StPO.
- Art. 6 EMRK.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `minder-schwerer-fall-und-besonders-schwerer-fall`

_Strafrahmen-Modifikation durch minder schweren Fall (Strafrahmen-Senkung) und besonders schweren Fall (Strafrahmen-Anhebung). Gesamtwuerdigung aller Tat- und Taeter-Umstaende. Beziehung zu Regelbeispielen. Konkurrenz minder schwerer Fall vs. § 49 StGB. Pruefungsreihenfolge. Anwendungsfaelle § 213..._

# Minder schwerer Fall und besonders schwerer Fall

## Arbeitsbereich

Strafrahmen-Modifikation durch minder schweren Fall (Strafrahmen-Senkung) und besonders schweren Fall (Strafrahmen-Anhebung). Gesamtwuerdigung aller Tat- und Taeter-Umstaende. Beziehung zu Regelbeispielen. Konkurrenz minder schwerer Fall vs. § 49 StGB. Pruefungsreihenfolge. Anwendungsfaelle § 213 StGB Totschlag, § 249 Abs. 2 StGB Raub, § 243 StGB Diebstahl, § 263 Abs. 3 StGB Betrug. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Viele Tatbestaende sehen einen **modifizierten Strafrahmen** vor:

- **Minder schwerer Fall**: gesenkter Strafrahmen, z.B. § 213 StGB beim Totschlag, § 249 Abs. 2 StGB beim Raub.
- **Besonders schwerer Fall**: erhoehter Strafrahmen, oft mit **Regelbeispielen**, z.B. § 243 StGB Diebstahl, § 263 Abs. 3 StGB Betrug.

Die Modifikation erfolgt durch **Gesamtwuerdigung** aller Umstaende.

## Wann brauchen Sie diese Skill?

- Sie wollen die Strafrahmen-Senkung "minder schwerer Fall" zugunsten des Mandanten erreichen.
- Sie pruefen, ob ein Regelbeispiel erfuellt ist und ob die Indizwirkung entkraeftet werden kann.
- Sie ordnen die Pruefungsreihenfolge bei mehreren Strafrahmen-Modifikationen.

## Rechtliche Grundlagen

### Minder schwerer Fall — Beispiele

- **§ 213 StGB** — Minder schwerer Fall des Totschlags: Provokation des Opfers oder sonstige mildernde Umstaende; Strafrahmen 1 bis 10 Jahre statt 5 bis 15 Jahre.
- **§ 249 Abs. 2 StGB** — Minder schwerer Fall des Raubs: 6 Monate bis 5 Jahre statt 1 bis 15 Jahre.
- **§ 250 Abs. 3 StGB** — Minder schwerer Fall des schweren Raubs.
- **§ 226 Abs. 3 StGB** — Minder schwerer Fall der schweren Koerperverletzung.
- **§ 224 Abs. 1 letzter Halbsatz StGB** — Minder schwerer Fall der gefaehrlichen Koerperverletzung: Freiheitsstrafe 3 Monate bis 5 Jahre statt 6 Monate bis 10 Jahre.

### Besonders schwerer Fall — Beispiele

- **§ 243 StGB** — Besonders schwerer Fall des Diebstahls mit Regelbeispielkatalog: 3 Monate bis 10 Jahre.
- **§ 263 Abs. 3 StGB** — Besonders schwerer Fall des Betrugs mit Regelbeispielkatalog: 6 Monate bis 10 Jahre.
- **§ 267 Abs. 3 StGB** — Besonders schwerer Fall der Urkundenfaelschung.
- **§ 240 Abs. 4 StGB** — Besonders schwerer Fall der Noetigung.

## Strafzumessungs-Grundsatz

### Minder schwerer Fall

- Erfordert **Gesamtwuerdigung**: alle straftatbezogenen und persönlichen Umstaende werden zusammengenommen.
- Schwellenfrage: weicht das Gesamtgewicht der Tat so deutlich nach unten von der Durchschnittstat ab, dass der gesetzliche Regelstrafrahmen unangemessen waere?
- Strafmilderungsgruende nach § 49 StGB koennen den Tatbestand des minder schweren Falls **mitausloesen** ("vertypte Milderungsgruende" bei Gesamtwuerdigung beruecksichtigen). Wenn der Tatbestand des minder schweren Falls bejaht wird, **entfaellt** die zusaetzliche Milderung nach § 49 StGB regelmaessig nicht automatisch; vielmehr kann der gemilderten Strafrahmen weiter nach § 49 StGB modifiziert werden. **St. Rspr.; Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.**

### Besonders schwerer Fall

- Bei **Regelbeispielen** Indizwirkung: ist ein Regelbeispiel erfuellt, ist die Indizwirkung für besonders schweren Fall regelmaessig gegeben.
- Gegenindizien koennen die Indizwirkung **entkraeften** — Gesamtwuerdigung.
- Bei "unbenannten besonders schweren Faellen" muss die Tat in Gewicht und Charakter den Regelbeispielen ungefaehr entsprechen.

## Pruefungsreihenfolge

1. **Grundtatbestand** und **Qualifikationen** pruefen.
2. **Regelbeispiele** (besonders schwerer Fall): Ist Tatbestand erfuellt? Indizwirkung. Gegenindizien?
3. **Minder schwerer Fall**: Gesamtwuerdigung; Tatbild deutlich unterhalb des Durchschnitts?
4. **Vertypte Milderungsgruende** nach § 49 StGB (Versuch, Beihilfe, § 21, § 17, § 28 Abs. 1, § 46a StGB).
5. Konkreten Strafrahmen festlegen.
6. Strafe im Schuldrahmen nach § 46 StGB konkretisieren.

## Konkurrenz minder schwerer Fall vs. § 49 StGB

Wenn ein vertypter Milderungsgrund vorliegt **und** zusaetzlich ein minder schwerer Fall in Betracht kommt: **Wahlrecht** des Gerichts in der Logik der st. Rspr.:

- Pruefung des minder schweren Falls **unter Einbeziehung** des vertypten Milderungsgrundes.
- Wenn minder schwerer Fall bejaht: weitere Milderung nach § 49 StGB ist nicht zwingend.
- Wenn minder schwerer Fall verneint: Milderung nach § 49 StGB greift für den Regelstrafrahmen.

In der Verteidigungspraxis stets **hilfsweise** beide Wege beantragen. **Aktenzeichen der einschlaegigen BGH-Linie vor Zitat verifizieren.**

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **Strafrahmen-Modifikation** identifizieren: Liegt eine minder schwere Fall-Norm vor? Liegt ein Regelbeispiel-Katalog vor?
2. **Argumente für minder schweren Fall** sammeln:
 - Provokation, Notlage, akuter Affekt.
 - Erstmaliger Verstoss.
 - Tatfolgen geringfuegig.
 - Tatumstaende untypisch.
3. **Argumente gegen Regelbeispiel-Indiz** sammeln:
 - Konkreter Vorgang weicht von der Modellvorstellung des Regelbeispiels ab.
 - Sonstige starke Strafmilderungs-Gesichtspunkte ueberwiegen.
4. **Antrag**: "Wir beantragen Verurteilung nach minder schwerem Fall (§ ..., Abs. ...). Hilfsweise Strafmilderung nach § 49 Abs. 1 StGB."

## Schritt-für-Schritt-Anleitung (Anklage)

1. **Regelbeispiel-Vortrag** mit Tatsachen substantiieren.
2. **Unbenannte besonders schwere Faelle** nur bei klarem Vergleichsgewicht zu den Regelbeispielen.
3. **Gegenargumente** zum minder schweren Fall antizipieren.

## Typische Fehler

- **Minder schwerer Fall pauschal** abgelehnt: ohne Gesamtwuerdigung; Revisionsangriff.
- **Regelbeispiel automatisch** zu besonders schwerem Fall: Indizwirkung nicht widerlegt geprueft.
- **Doppelte Anwendung**: Tatumstand begruendet minder schweren Fall **und** wird zusaetzlich strafmildernd in § 46 StGB beruecksichtigt — moegliche Verstoss gegen § 46 Abs. 3 StGB.
- **§ 49 StGB** nicht im Verhaeltnis zum minder schweren Fall geprueft.

## Quellen und Stand 05/2026

- §§ 213, 224, 226, 240, 243, 249, 250, 263, 267 StGB in der geltenden Fassung.
- BGH-Linie zur Konkurrenz minder schwerer Fall / § 49 StGB — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Skill: `nachtraegliche-gesamtstrafenbildung-55-stgb`

_Nachtraegliche Gesamtstrafenbildung nach § 55 StGB. Voraussetzung: spaetere Tat wurde **vor** einer frueheren Verurteilung begangen (Zaesurwirkung). Beschluss-Verfahren § 460 StPO. Einbeziehung rechtskraeftiger Strafen. Haerteausgleich, wenn die Einbeziehung nicht moeglich ist (Bewaehrung bereits..._

# Nachtraegliche Gesamtstrafenbildung — § 55 StGB

## Arbeitsbereich

Nachtraegliche Gesamtstrafenbildung nach § 55 StGB. Voraussetzung: spaetere Tat wurde **vor** einer frueheren Verurteilung begangen (Zaesurwirkung). Beschluss-Verfahren § 460 StPO. Einbeziehung rechtskraeftiger Strafen. Haerteausgleich, wenn die Einbeziehung nicht moeglich ist (Bewaehrung bereits erledigt, Strafvollstreckung beendet). BGH-staendige Linie. Verteidigung im Vollstreckungsstadium. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

§ 55 StGB ermoeglicht eine **nachtraegliche** Bildung einer Gesamtstrafe, wenn ein bereits rechtskraeftig Verurteilter wegen einer **anderen** Tat verurteilt wird, die er **vor** der frueheren Verurteilung begangen hat. Es findet eine **rueckwirkende** Gesamtbetrachtung statt — so, als waeren beide Taten in einem Verfahren entschieden worden. Die fruehere Verurteilung wirkt als **Zaesur**.

## Wann brauchen Sie diese Skill?

- Mandant ist bereits einmal rechtskraeftig verurteilt; jetzt wird eine weitere Tat abgeurteilt, die **vor** der frueheren Verurteilung begangen wurde.
- Sie pruefen die Akte, ob nachtraegliche Gesamtstrafenbildung moeglich ist (oder schon haette erfolgen muessen).
- Sie schreiben einen Antrag im Beschluss-Verfahren nach § 460 StPO.
- Sie pruefen, ob die Einbeziehung nicht (mehr) moeglich ist und ob ein **Haerteausgleich** erforderlich wird (vgl. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`).

## Rechtliche Grundlagen

- **§ 55 Abs. 1 StGB** — Wird ein bereits rechtskraeftig Verurteilter spaeter wegen einer anderen Tat verurteilt, die vor der frueheren Verurteilung begangen wurde, so ist eine nachtraegliche Gesamtstrafe nach §§ 53, 54 StGB zu bilden. Vorverurteilung muss in den Aburteilung einbezogen werden, soweit die Strafe noch nicht **vollstreckt, verjaehrt oder erlassen** ist.
- **§ 55 Abs. 2 StGB** — Bei Nebenstrafen, Nebenfolgen und Massregeln gilt § 53 Abs. 4 StGB sinngemaess.
- **§ 460 StPO** — Beschluss-Verfahren zur nachtraeglichen Gesamtstrafenbildung; zuständig ist das Gericht des letzten Verfahrens.
- **§ 462 StPO** — Anhörung, sofortige Beschwerde.
- **§ 462a StPO** — Strafvollstreckungskammer für bestimmte Konstellationen.

## Zentrale Voraussetzung — Zaesurwirkung

Die fruehere Verurteilung wirkt als **Zaesur**: Sie bildet die Trennlinie zwischen Taten, die nachtraeglich noch in eine Gesamtstrafe einbezogen werden koennen, und Taten, die in der Folgezeit begangen wurden. Massgeblich ist das **Datum der ersten tatrichterlichen Verurteilung** im jeweiligen Verfahren (st. Rspr.; Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren).

**Beispiel**:

- 01.03.2024: Tat A.
- 15.05.2024: Tat B.
- 10.07.2024: Verurteilung Tat A (AG, Geldstrafe 90 Tagessaetze; rechtskraeftig).
- 20.11.2024: Tat C.
- 15.04.2025: Tat B wird abgeurteilt (LG, Freiheitsstrafe 8 Monate).

Tat B wurde **vor** der Verurteilung vom 10.07.2024 begangen. Bei der Verurteilung am 15.04.2025 ist nach § 55 StGB eine nachtraegliche Gesamtstrafe aus der Geldstrafe vom 10.07.2024 und der Freiheitsstrafe vom 15.04.2025 zu bilden.

Tat C wurde **nach** der Verurteilung vom 10.07.2024 begangen — sie kann **nicht** mit Tat A in eine Gesamtstrafe einbezogen werden; die Verurteilung vom 10.07.2024 wirkt als Zaesur.

## Wann ist eine Einbeziehung nicht (mehr) moeglich?

§ 55 Abs. 1 Satz 1 StGB schliesst die Einbeziehung aus, wenn die fruehere Strafe:

- **vollstreckt** ist;
- **verjaehrt** ist;
- **erlassen** ist (z.B. nach abgelaufener Bewaehrung, § 56g StGB).

In solchen Faellen kommt der **Haerteausgleich** in Betracht; vgl. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`.

## Schritt-für-Schritt-Anleitung (Verteidigung)

1. **BZRG-Auszug** und Verfahrensakte pruefen: Welche Vorverurteilungen liegen vor? Welche Tatzeiten?
2. **Zaesur-Pruefung**: Wurde die abzuurteilende Tat **vor** der ersten tatrichterlichen Verurteilung begangen?
3. **Status der Vorverurteilung**:
 - Vollstreckung schon abgeschlossen? — Haerteausgleich.
 - Verjaehrt? — Haerteausgleich.
 - Erlassen (Bewaehrung gluecklich abgelaufen)? — Haerteausgleich.
 - Noch offen / in Vollstreckung / Bewaehrung laufend? — Einbeziehung nach § 55 StGB.
4. **Antrag**:
 - **In der Hauptverhandlung**: "Wir beantragen, gemaess § 55 StGB eine Gesamtstrafe aus der Strafe aus dem Urteil [Az.] vom [Datum] und der hier zu verhaengenden Strafe zu bilden."
 - **Nach Rechtskraft (Beschluss-Verfahren)**: § 460 StPO; zuständig ist das Gericht des **letzten** Verfahrens.
5. **Begruendung im Urteil**: Einzelstrafen, Einsatzstrafe, Gesamtstrafe; vgl. `gesamtstrafenbildung-53-54-stgb-erste-instanz`.
6. **Bewaehrungsperspektive**: Gesamtstrafe darf nicht ueber 2 Jahre liegen, wenn Bewaehrung erhalten bleiben soll.

## Beschluss-Verfahren nach § 460 StPO

- Antrag der Staatsanwaltschaft oder des Verurteilten.
- Zustaendig: Gericht des **letzten** Verfahrens.
- Anhörung des Verurteilten und der Staatsanwaltschaft (§ 462 Abs. 2 StPO).
- Entscheidung durch **Beschluss**; sofortige Beschwerde nach § 462 Abs. 3 StPO innerhalb einer Woche.
- Die einbezogenen Strafen verlieren ihre Selbststaendigkeit; die alte Strafvollstreckungsgrundlage wird ersetzt durch den neuen Gesamtstrafen-Beschluss.

## Strafzumessungs-Grundsatz bei nachtraeglicher Gesamtstrafenbildung

- **Hypothetische Gesamtbetrachtung**: Wie waere entschieden worden, wenn beide Taten in einem Verfahren abgeurteilt worden waeren?
- **Schutzzweck** des § 55 StGB: Der Verurteilte soll durch die Aufspaltung in mehrere Verfahren **nicht schlechter gestellt** werden, als wenn beide Taten gemeinsam abgeurteilt worden waeren.
- **Bildung**: hoechste Einzelstrafe als Einsatzstrafe, dann angemessene Erhoehung; max. 15 Jahre Freiheitsstrafe / 720 Tagessaetze Geldstrafe (§ 54 Abs. 2 StGB).

## Sonderfaelle

### Mehrere fruehere Verurteilungen

- Es koennen **mehrere** fruehere Verurteilungen einbezogen werden, soweit die jeweilige Tat vor der jeweiligen frueheren Verurteilung begangen wurde.
- Komplexe Konstellationen: oft mehrere Zaesuren mit unterschiedlichen Einbeziehungsmoeglichkeiten.

### Verstrickung mit Bewaehrungsstrafe

- Wird die fruehere Bewaehrungsstrafe in die Gesamtstrafe einbezogen, faellt sie als selbststaendige Bewaehrungsstrafe weg.
- Die neue Gesamtstrafe kann ihrerseits zur Bewaehrung ausgesetzt werden (§ 56 StGB); Bewaehrungs-Voraussetzungen pruefen.
- Falls die Bewaehrungsstrafe schon **erlassen** ist (§ 56g StGB), Einbeziehung nicht moeglich — Haerteausgleich.

### Mehrere offene Verfahren

- Wenn mehrere Verfahren gleichzeitig laufen, sind die Verfahren oft prozessoekonomisch zu **verbinden** (§ 4 StPO), damit nachtraegliche Gesamtstrafenbildung entfaellt.

### Auslandsstrafen

- Auslandsstrafen werden **nicht** einbezogen (BGH st. Rspr.; Aktenzeichen verifizieren).
- Kompensation kann ggf. durch Strafmilderung erfolgen.

## Typische Fehler

- **Zaesur falsch bestimmt**: Massgeblich ist das erste tatrichterliche Urteil im jeweiligen Verfahren, **nicht** die Rechtskraft.
- **Einbeziehung uebersehen**: Wenn das Gericht die fruehere Strafe nicht einbezieht, obwohl sie noch offen ist, liegt Strafzumessungsmangel vor (Revisionsruege).
- **Haerteausgleich nicht angesprochen**: Wenn Einbeziehung nicht moeglich ist, muss der Schutzzweck des § 55 StGB durch Haerteausgleich gewahrt werden.
- **Bewaehrung** der frueheren Strafe nicht beachtet: Bei Einbeziehung faellt die alte Bewaehrungsanordnung weg.
- **Gesamtstrafen-Obergrenze** ueberschritten (§ 54 Abs. 2 StGB).
- **Mehrere Zaesuren** in komplexer Konstellation falsch geordnet.

## Quellen und Stand 05/2026

- § 55 StGB in der geltenden Fassung.
- §§ 53, 54 StGB.
- §§ 460, 462, 462a StPO.
- BGH-staendige Linie zu Zaesurwirkung, Einbeziehung und Schutzzweck — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

