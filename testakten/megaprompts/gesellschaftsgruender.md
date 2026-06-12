# Megaprompt: gesellschaftsgruender

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 99 Skills des Plugins `gesellschaftsgruender`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Gesellschaftsgründung: ordnet Rolle (Gründer, Notar, Handelsregister), markiert Frist (…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting für das Gesellschaftsgründer-Plugin; besonders anfängerfreundlich, mit Rollenklä…
3. **gruendungsassistent-erstpruefung-und-mandatsziel** — Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel im Gesellschaftsgründung: fachlich vertieftes Modul mit …
4. **beirat-advisory-board** — Beirat oder Advisory Board für GmbH oder UG einrichten: Satzungsregelung, Bestellungsverfahren, Beratungsvertrag. Normen…
5. **bilinguale-dokumente** — Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen: zweisprachige Satzung, Gesellschafterbeschluss, SHA…
6. **egbr-mopeg-gesellschaftsgruender** — GbR nach MoPeG 2024 und Eintragung ins Gesellschaftsregister als eGbR vorbereiten. Normen: §§ 705 ff. BGB n.F. MoPeG, §§…
7. **firmenname-pruefung** — Firmenname auf Zulässigkeit und Verwechslungsgefahr prüfen: Differenzierungsgebot, Irreführungsverbot. Normen: §§ 17 18 …
8. **genehmigtes-kapital** — Genehmigtes Kapital für GmbH oder AG in Satzung aufnehmen: Ermaechtigungsbeschluss, Hoechstbetrag, Bezugsrechtsausschlus…
9. **geschaeftsfuehrer-pflichten-startphase** — Pflichten des GmbH-Geschäftsführers in Gründungs- und Startphase: Stammkapitaleinzahlung, Insolvenzantragspflicht, Buchf…
10. **geschaeftsfuehrervertrag** — Geschäftsführervertrag für GmbH-Geschäftsführer aufsetzen: Verguetung, Wettbewerbsverbot, Abberufung, Kündigungsfristen.…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Gesellschaftsgründung: ordnet Rolle (Gründer, Notar, Handelsregister), markiert Frist (Handelsregistereintragung), wählt Norm (GmbHG, AktG, HGB, § 5a GmbHG UG, GenG) und Zuständigkeit (Handelsregister AG), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Gesellschaftsgruender** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `ag-kleine-ag` — AG Kleine AG
- `anfaenger-kaltstart` — Anfaenger Kaltstart
- `aufloesung-liquidation-start` — Aufloesung Liquidation Start
- `auslandsgesellschafter-kyc` — Auslandsgesellschafter KYC
- `bankkonto-kyc-beirat` — Bankkonto KYC Beirat
- `beirat-advisory-board` — Beirat Advisory Board
- `bilinguale-dokumente` — Bilinguale Dokumente
- `board-pack-erste-100-tage` — Board Pack Erste 100 Tage
- `cap-table` — CAP Table
- `cashburn` — Cashburn
- `checkliste-vor-unterschrift` — Checkliste vor Unterschrift
- `daten-und-ki-compliance-start` — Daten und KI Compliance Start
- `deadlock-und-mediation` — Deadlock und Mediation
- `dokumente-intake` — Dokumente Intake
- `unterlagen-luecken` — Unterlagen Luecken

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Gesellschaftsgruender sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting für das Gesellschaftsgründer-Plugin; besonders anfängerfreundlich, mit Rollenklärung, Dokumentenintake, Rechtsformwahl und Anschluss-Skills._

# Gesellschaftsgründer Allgemein — leichter Kaltstart

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gesellschaftsgruender** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschaftsgründer Allgemein — leichter Kaltstart` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Sofortstart

Wenn die Nutzerin oder der Nutzer nur sagt: „Ich will eine Gesellschaft gründen“, beginnst du nicht mit einer großen Abfrage. Du gibst zuerst Orientierung:

1. **Kurz einordnen:** Was klingt nach Rechtsformwahl, was nach Notar/Register, was nach Bank/KYC, was nach Gründerstreit, was nach Steuer/Compliance?
2. **Fünf Kernfragen stellen:** Wer gründet? Was macht das Unternehmen? Wer zahlt was ein? Wer arbeitet mit? Gibt es Investoren, Ausland, IP, Daten, Regulierung oder Streit?
3. **Erste Route anbieten:** „Ich würde jetzt in dieser Reihenfolge vorgehen: Rechtsform, Beteiligtenstruktur, Gründungsdokumente, Vollzug, Startbetrieb.“
4. **Sofortprodukt liefern:** Eine Mini-Roadmap mit Risikoampel und Unterlagenliste, auch wenn noch nicht alles bekannt ist.
5. **Anschluss-Skills vorschlagen:** Nach jedem Zwischenergebnis zwei bis fünf konkrete Skills aus `gesellschaftsgruender`, nicht nur abstrakte Hinweise.

## Rechts- und Quellenanker

GmbHG, HGB, BGB, PartGG, GenG, AktG, GwG, GewO, AO/UStG, SGB IV/SGB VII, InsO § 15a sowie MoPeG- und Registerlogik live prüfen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.
- Bei Notar-, Steuer-, Erlaubnis-, Sanktions-, Geldwäsche- oder Insolvenzthemen nicht beschwichtigen, sondern die nächste fachkundige Schnittstelle benennen.

---

## Skill: `gruendungsassistent-erstpruefung-und-mandatsziel`

_Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel im Gesellschaftsgründung: fachlich vertieftes Modul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt im Gesellschaft..._

# Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Gruendungsassistent Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gesellschaftsgruender** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** UG, OHG, KG, PartG, MoPeG, DiRUG, GwG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Gruendungsassistent** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Rechtsformvergleich für Erstprüfung

| Form | Mindestkapital | Gründungskosten | Haftung | Notar | Geeignet für |
| --- | --- | --- | --- | --- | --- |
| GbR (§§ 705 ff. BGB, MoPeG-novelliert) | kein | gering | unbeschränkt persönlich §§ 721 BGB | nicht zwingend; Gesellschaftsregister § 707 BGB optional (eGbR) | nicht-kaufmännische Personenzusammenschlüsse |
| OHG (§§ 105 ff. HGB) | kein | gering | unbeschränkt persönlich § 128 HGB | HR-Anmeldung notariell | Kaufleute, Kleinbetriebe |
| KG (§§ 161 ff. HGB) | kein, Haftsumme frei wählbar | gering | Komplementär unbeschränkt; Kommanditist auf Haftsumme § 171 HGB | notarielle HR-Anmeldung | Investoren-Beteiligung |
| GmbH & Co. KG | GmbH 25.000 EUR | mittel | Komplementär-GmbH | notariell | Mittelstand, Steueroptimierung |
| UG (haftungsbeschränkt) § 5a GmbHG | 1 EUR Stammkapital, Aufstockungspflicht § 5a Abs. 3 GmbHG (25 % Gewinn) | gering, Musterprotokoll § 2 Abs. 1a GmbHG | begrenzt | notariell, vereinfachte Online-Gründung möglich (DiRUG) | Bootstrap-Startup |
| GmbH | 25.000 EUR, hälftige Einzahlung § 7 GmbHG (12.500 EUR) | mittel | begrenzt § 13 Abs. 2 GmbHG | notariell, Online-Gründung § 2 Abs. 3 GmbHG (DiRUG seit 01.08.2022) | Mittelstand-Standard |
| AG | 50.000 EUR § 7 AktG | hoch | begrenzt | notariell | kapitalmarktreife Strukturen |
| PartG mbB | kein | mittel | nur Berufsausübungs-Haftpflicht (§ 8 Abs. 4 PartGG) | nicht zwingend, Partnerschaftsregister | Freiberufler, Sozietäten |
| gGmbH | 25.000 EUR | mittel | begrenzt | notariell + Finanzamt Gemeinnützigkeit § 52 AO | gemeinnützige Zwecke |

## Trade-off-Hinweis für Mandantengespräch

- **UG vs. GmbH:** UG spart Stammkapital, kostet aber 25 %-Gewinnthesaurierung und schlechteres Image bei Banken/Lieferanten.
- **GmbH vs. GmbH & Co. KG:** KG ermöglicht steuerliche Verlustverrechnung beim Kommanditisten, aber komplexere Struktur und höhere laufende Kosten (zwei Jahresabschlüsse).
- **PartG mbB vs. Sozietät:** mbB schützt vor Berufsfehlern der Partner, aber nur bei Pflichtversicherung (§ 8 Abs. 4 PartGG i.V.m. § 51a BRAO bei Anwälten).
- **DiRUG-Online-Gründung:** seit 01.08.2022 § 2 Abs. 3 GmbHG erweitert; vereinfacht GmbH-Gründung. Beachte: Sacheinlagen weiterhin Präsenznotar.

---

## Skill: `beirat-advisory-board`

_Beirat oder Advisory Board für GmbH oder UG einrichten: Satzungsregelung, Bestellungsverfahren, Beratungsvertrag. Normen: §§ 45 52 GmbHG, §§ 95 ff. AktG analog. Prüfraster: Kompetenzen, Verguetung, Haftung, Abberufung, Datenschutz. Output: Beiratssatzung oder Advisory-Board-Charter. Abgrenzung: n..._

# Beirat / Advisory Board

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beirat / Advisory Board` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn

Klaere vor Ausarbeitung der Beiratsstruktur:

1. **Rechtsform?** GmbH (freiwillig, Paragraf 52 GmbHG), AG (Aufsichtsrat Pflicht Paragraf 95 AktG), mitbestimmte GmbH (Pflicht-Aufsichtsrat ab 500 AN)?
2. **Aufgabentyp?** Rein beratend (Advisory Board ohne Entscheidungsbefugnis) oder mit echten Zustimmungsrechten (Beirat mit Vetomacht)?
3. **Vergütung?** Cash (Mittelstand), ESOP/Optionen (Startup), rein ehrenamtlich?
4. **Besetzung?** Externe Experten, Investoren-Vertreter, Familienmitglieder, unabhängige Dritte?
5. **Schlichtungsfunction gewuenscht?** Gesellschafter-Konflikt vorgebeugt durch Beirat als Mediator?
6. **D&O-Versicherung?** Bei echten Zustimmungsrechten empfohlen.

## Zentrale Normen

- **§ 52 GmbHG** — Verweis auf AktG-Vorschriften bei freiwilligem Aufsichtsrat / Beirat mit Kontrollbefugnissen
- **§ 95 AktG** — Pflicht-Aufsichtsrat bei AG; Zusammensetzung und Amtszeit
- **§ 111 AktG** — Aufgaben des Aufsichtsrats; analog für Beirat mit echter Kontrolle
- **§ 116 AktG** — Sorgfaltspflicht und Verschwiegenheit der AR-Mitglieder; analog Beirat
- **§§ 1, 4 DrittelbG / §§ 1, 7 MitbestG** — Pflicht-Aufsichtsrat bei GmbH ab 500 / 2.000 Arbeitnehmern
- **§§ 133, 157 BGB** — Auslegung der Beiratsordnung und -klauseln in der Satzung
- **§ 43 GmbHG** — Haftungsstandard; gilt analog für Beirat mit Zustimmungsrechten

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema: Beirat-Einrichtung

| Schritt | Frage | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Rechtsform und Pflicht | GmbH: Beirat freiwillig; AG: AR Pflicht; DrittelbG/MitbestG? | Klaren ob AR-Pflicht besteht |
| 2 | Aufgabenprofil | Beratend, kontrollierend, schlichterisch? | Festlegt Tiefe der Satzungs-Klausel |
| 3 | Satzungs-Klausel | Beirat in Satzung verankert? Befugnisse definiert? | Ohne Satzungs-Klausel kein Zustimmungsvorbehalt |
| 4 | Beiratsordnung | Detailregelungen ausgelagert (Meeting-Rhythmus, Vergütung, Quorum)? | Aenderungen ohne Notar moeglich |
| 5 | Besetzung | Anzahl Mitglieder, Wahlmodus, Amtszeit, Wiederwahl | Satzung oder Beiratsordnung regelt |
| 6 | Vergütung | Cash / Optionen / ehrenamtlich; Reisekostenerstattung | Steuerlich relevant; ESOP bei Startup |
| 7 | D&O-Versicherung | Bei Zustimmungsrechten empfohlen | Keine gesetzliche Pflicht; Gestaltung |
| 8 | Schlichtungs-Klausel | Anrufungspflicht vor Klage? Bindungs-Wirkung? | Nicht bindend, aber Verfahrenspflicht möglich |

## Begriffliche Klarheit

### Beirat (deutsch)
- Beratungs- und/oder Kontrollorgan
- Freiwillig bei GmbH
- Befugnisse in Satzung / Beiratsordnung festgelegt

### Advisory Board
- Beratung ohne echte Entscheidungsbefugnis
- Typisch in Startups
- Ehrenamtlich oder gegen Optionen

### Aufsichtsrat
- Bei AG Pflicht (Paragraf 95 AktG)
- Bei mitbestimmter GmbH ab 500 / 2.000 Beschaeftigten Pflicht (DrittelbG, MitbestG)
- Pflicht-Aufgaben: Bestellung Vorstand, Prüfung Jahresabschluss

## Aufgaben (typisch)

### Beratung
- Strategie-Diskussion
- Markt-Trends, Branchen-Expertise
- Personal-Empfehlungen (insbesondere C-Level)

### Aufsicht
- Prüfung Jahresabschluss vor GV
- Risiko-Bewertung
- Compliance-Monitoring
- Bewertung der Geschäftsführer-Leistung

### Schlichtung
- Bei Gesellschafter-Konflikten
- Bei GF-Konflikten
- Vor Anfechtungsklage

### Repraesentation
- Externe Wahrnehmung (PR-Wert)
- Reputations-Traeger (z.B. Branchen-Promis)

## Schritt-für-Schritt-Workflow

1. **Triage:** Aufgabe und Rechtsform klaeren; Pflicht-AR pruefen (DrittelbG/MitbestG)
2. **Konzept:** Aufgabenprofil, Besetzungswunsch, Verguetungsmodell festlegen
3. **Satzungs-Klausel entwerfen:** Minimalklausel oder detaillierte Klausel; Notar-Termin einplanen
4. **Beiratsordnung entwerfen:** Meeting-Rhythmus, Quorum, Beschlussfaehigkeit, Protokoll-Pflicht
5. **Beiratsvertraege:** Vertraulichkeit, Verguetung, D&O-Versicherung, Wettbewerbsverbot
6. **Besetzung:** Mitglieder ansprechen, Beschluss der Gesellschafterversammlung herbeiführen
7. **Konstituierende Sitzung:** Vorsitzenden waehlen, Beiratsordnung verabschieden
8. **Monitoring:** Jaehrliche Beirats-Evaluation; Anpassung Beiratsordnung wenn noetig

## Output-Template: Satzungs-Klausel Beirat

**Adressat:** Gesellschaftsvertrag / Satzung GmbH — Tonfall rechtspraezise

```
§ [X] Beirat

(1) Die Gesellschaft hat einen Beirat. Er besteht aus mindestens 3,
hoechstens 7 Mitgliedern.

(2) Die Mitglieder des Beirats werden von der Gesellschafterversammlung
mit einfacher Mehrheit für eine Amtszeit von 3 Jahren bestellt.
Wiederbestellung ist zulaessig.

(3) Der Beirat hat folgende Aufgaben:
a) Beratung der Geschaeftsfuehrung in strategischen Fragen,
b) Pruefung des Jahresabschlusses vor Vorlage in der
 Gesellschafterversammlung,
c) Empfehlungen zu Investitionen ueber [SCHWELLENWERT] EUR,
d) Vorabschlichtung bei Gesellschafter-Konflikten.

(4) Folgende Geschaefte beduerfen der Zustimmung des Beirats:
a) Aufnahme von Krediten ueber [BETRAG] EUR,
b) Veraeusserung wesentlicher Aktiva (> 20 % der Bilanzsumme),
c) Eingehung von Joint Ventures,
d) Anstellung und Abberufung von Geschaeftsfuehrern.

(5) Das Naehere regelt die Beiratsordnung, die von der
Gesellschafterversammlung mit [MEHRHEIT] beschlossen wird.

(6) Die Mitglieder des Beirats haften der Gesellschaft gegenueber
bei Verletzung ihrer Pflichten analog § 43 GmbHG.
Zur Absicherung schliessen sie eine D&O-Versicherung ab,
deren Praemie die Gesellschaft traegt.
```

## Output-Template: Beiratsordnung (Kernauszug)

**Adressat:** Interne Beiratsordnung — Tonfall sachlich-juristisch

```
BEIRATSORDNUNG der [FIRMA] GmbH
Stand: [DATUM]

§ 1 Aufgaben und Befugnisse
[wie Satzungs-Klausel Abs. 3 und 4]

§ 2 Zusammensetzung
(1) Der Beirat besteht aus [ANZAHL] Mitgliedern.
(2) Mindestens [N] Mitglieder sind unabhaengig.

§ 3 Sitzungen
(1) Vier regulaere Sitzungen pro Geschaeftsjahr.
(2) Einberufung durch Vorsitzenden mit 1-Wochen-Frist,
 Tagesordnung beifuegen.
(3) Beschlussfaehigkeit: mindestens [N] Mitglieder anwesend.
(4) Beschluesse mit einfacher Mehrheit.

§ 4 Verguetung
(1) Jahresfestbetrag: [BETRAG] EUR für Mitglieder,
 [BETRAG] EUR für Vorsitzenden.
(2) Sitzungsgeld: [BETRAG] EUR pro Sitzung.
(3) Reisekosten gegen Beleg.

§ 5 Vertraulichkeit
[Klausel: Verschwiegenheit ueber Beratungsgegenstaende]

§ 6 Schlichtungsfunktion
(1) Bei Konflikten zwischen Gesellschaftern ist der Beirat
 vor Klageerhebung anzurufen.
(2) Beirat hat 4 Wochen für Schlichtungsvorschlag.
(3) Schlichtungsempfehlung ist nicht bindend.
```

## Output-Template: Advisory Agreement (Startup)

**Adressat:** Advisor (extern) — Tonfall professionell-praegnant

```
ADVISORY AGREEMENT
zwischen [FIRMA] GmbH (Gesellschaft) und [NAME] (Advisor)

Aufgaben:
- Beratung in [BEREICH]
- Vermittlung von Kontakten
- 1 Stunde Call pro Monat; 1 Praesenz-Meeting pro Quartal

Verguetung:
- Option auf [X] % der Anteile (ESOP-Pool)
- Vesting: 25 % nach 12 Monaten Cliff, dann monatlich 1/48
- Bei vorzeitiger Beendigung: nur gevested

Laufzeit: 2 Jahre, Verlaengerung um 1 Jahr automatisch
Kuendigung: 3 Monate vor Ablauf; ausserordentlich aus wichtigem Grund
```

## Rote Schwellen

- Satzungs-Klausel mit Zustimmungsvorbehalten: Notar-Beurkundung der Satzungsaenderung beachten
- Pflicht-Aufsichtsrat bei > 500 AN (DrittelbG) oder > 2.000 AN (MitbestG): nicht durch Beirats-Gestaltung umgehbar
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Zustimmungsvorbehalt entfaltet keine Aussenwirkung gegenüber Dritten (OLG Muenchen 2021)

## Quellen und Vertiefung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- OLG Muenchen, GmbHR 2021, 1056 — Aussenwirkung des Zustimmungsvorbehalts
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 52 GmbHG, §§ 95, 111, 116 AktG, §§ 1, 4 DrittelbG, §§ 1, 7 MitbestG
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsgruender-geschaeftsordnung-gf` — Verzahnung mit GF-Entscheidungskompetenzen
- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Satzungs-Klausel Beirat
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — Schlichtungs-Funktion vor Eilantrag

<!-- AUDIT 27.05.2026
Geprueft: 3 gemeldete Halluzinationen (task_124.json)
 Behauptetes Thema (Beirat-Vetorechte, Bestellung/Abberufung) entspricht nicht dem Urteilsinhalt.
 Tatsaechliches Thema: Schiedsgericht als Gesellschaftsorgan (Uebertragung von Befugnissen
 der Gesellschafterversammlung), Anfechtungsklage. Quelle: dejure.org/1965,61.
 AZ nicht nachweisbar. Kein Handlungsbedarf in dieser Datei.
 Kein Handlungsbedarf in dieser Datei.
Frontmatter unveraendert. Keine Commit-Aktion.
-->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 49 GmbHG
- § 5a GmbHG
- § 2 GmbHG
- § 47 GmbHG
- § 15 GmbHG
- § 7 GmbHG
- § 40 GmbHG
- § 5 GmbHG
- § 9 GmbHG
- § 34 GmbHG
- § 43 GmbHG
- § 55a GmbHG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `bilinguale-dokumente`

_Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen: zweisprachige Satzung, Gesellschafterbeschluss, SHA. Normen: §§ 2 3 GmbHG, HGB. Prüfraster: rechtliche Verbindlichkeit der deutschen Fassung, Abweichungsregelung, Notareignung. Output: Bilinguale Dokumentenvorlage Deutsch-Englis..._

# Bilinguale Dokumente

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bilinguale Dokumente` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Kernsachverhalt

Internationale Investoren, ausländische Gesellschafter und grenzüberschreitende M&A-Transaktionen erfordern Gesellschaftsdokumente in zwei Sprachen — regelmäßig Deutsch und Englisch. Dabei gilt im deutschen Rechtsraum: Die deutsche Fassung ist die rechtlich verbindliche; die englische Fassung ist eine "Convenience Translation". Diese Hierarchie muss in jedem Dokument durch eine Sprachvorrang-Klausel ausdrücklich vereinbart werden, sonst drohen Auslegungsstreitigkeiten und Vollstreckungsprobleme.

Unterstützt bei der Erstellung, Qualitätssicherung und Konsistenzprüfung bilingualer Gesellschaftsdokumente: Satzung (Articles of Association), Gesellschaftervereinbarung (Shareholder Agreement / SHA), Geschäftsführeranstellungsvertrag (Managing Director's Agreement), Beiratsordnung (Advisory Board Charter), Term Sheet und Convertible Loan Agreement.

## Kaltstart-Rückfragen

1. **Welche Dokumente?** Satzung, SHA, GF-Anstellungsvertrag, Beiratsordnung, Term Sheet, CLA oder andere?
2. **Welche Sprachen?** Standard: Deutsch/Englisch. Andere Sprachen möglich (Französisch, Mandarin)?
3. **Ausländische Beteiligte?** Wer sind die ausländischen Gesellschafter/Investoren und ihre Muttersprache?
4. **Notarielle Beurkundung erforderlich?** Satzungsänderung, Anteilsabtretung, Kapitalerhöhung: Deutsch zwingend (§ 5 BeurkG).
5. **Bestehende Dokumente?** Liegt die deutsche Masterfassung bereits vor oder wird sie parallel erstellt?
6. **Standard-Glossar vorhanden?** Gibt es ein Kanzlei-Glossar für Standardbegriffe (Class A, Liquidation Preference, Vesting)?
7. **Schiedssprache?** Bei DIS-Schiedsklausel: Schiedsverfahrenssprache festlegen (Deutsch oder Englisch).
8. **Zieldatum?** Notartermin und Signing-Datum festlegen — bestimmt Bearbeitungszeit für Übersetzung und Qualitätssicherung.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte

**§ 184 GVG — Amtssprache**
> "Die Gerichtssprache ist deutsch."

Alle gerichtlichen Verfahren in Deutschland werden in deutscher Sprache geführt. Eingaben in anderen Sprachen sind zu übersetzen. Für die Vollstreckung aus einem englischsprachigen Schiedsspruch in Deutschland ist eine beglaubigte Übersetzung erforderlich (§ 1064 Abs. 3 ZPO).

**§ 5 BeurkG — Sprache der Beurkundung**
> "Die Verhandlung soll in deutscher Sprache geführt werden. Beteiligte, die der deutschen Sprache nicht mächtig sind, müssen einen Dolmetscher hinzuziehen."

Bei Beurkundungsverfahren mit ausländischen Beteiligten: Beurkundung auf Deutsch; Dolmetscher bestellen; Beteiligte erhalten Übersetzung der Urkunde. Die englische Fassung des Satzungstextes ist keine Beurkundungsgrundlage.

**§ 1064 Abs. 3 ZPO — Vollstreckung von Schiedssprüchen**
> Bei der Vollstreckung eines ausländischen Schiedsspruchs ist eine beglaubigte Übersetzung des Schiedsspruchs in die deutsche Sprache beizufügen.

**§§ 133, 157 BGB — Auslegungsgrundsätze**
> § 133 BGB: Bei der Auslegung einer Willenserklärung ist der wirkliche Wille zu erforschen und nicht an dem buchstäblichen Sinne des Ausdrucks zu haften.
> § 157 BGB: Verträge sind so auszulegen, wie Treu und Glauben mit Rücksicht auf die Verkehrssitte es erfordern.

Bei zwei Sprachfassungen ohne Vorrang-Klausel: Widersprüche werden nach §§ 133, 157 BGB ausgelegt — mit erheblicher Unsicherheit. Daher: Vorrang-Klausel zwingend.

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Relevanz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema: Bilinguale Dokumente

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Sprachvorrang-Klausel vorhanden? | Jedes Dokument enthält eine Vorrang-Klausel (DE über EN)? | Ohne Klausel: Auslegungsrisiko bei Widersprüchen |
| 2 | Deutsche Masterfassung vollständig? | Deutsche Fassung ist vollständig und rechtsanwaltlich geprüft bevor Übersetzung beginnt | Übersetzung von unvollständiger Fassung = Doppelaufwand |
| 3 | Juristischer Übersetzer? | Übersetzung durch Translator mit deutschem Recht-Background — nicht maschinelle Übersetzung allein | Maschinelle Übersetzung bei Rechtsbegriffen systematisch unzuverlässig |
| 4 | Glossar-Konsistenz | Sind Fachbegriffe über alle Dokumente einheitlich übersetzt? | Satzung und SHA müssen exakt gleiche Begriffe verwenden (z.B. "Class B" nicht in einem Dokument "Series B") |
| 5 | Notarielle Anforderungen geprüft? | Dolmetscher bei Beurkundung mit Ausländern (§ 5 BeurkG)? | Fehlender Dolmetscher → Unwirksamkeit der Beurkundung |
| 6 | Fachbegriffe dual bezeichnet? | Englische Fachbegriffe die im Deutschen keine exakten Äquivalente haben (Liquidation Preference, Drag-Along) als Doppelbezeichnung? | Z.B. "Liquidation Preference (Liquidationsvorrang)" |
| 7 | Rechtsbegriffe korrekt übertragen? | GmbH ≠ "Limited Liability Company"; GF ≠ "CEO"; HV ≠ "Stockholders Meeting" | Falsche Übersetzung kann Rechtsfolgen verändern |
| 8 | Cross-Reading durchgeführt? | Anwalt liest beide Fassungen parallel und prüft Konsistenz? | Schritt-für-Schritt-Abgleich, Abschnitt für Abschnitt |
| 9 | Schiedsklausel-Sprache festgelegt? | DIS-Klausel: Schiedsverfahrenssprache explizit genannt? | Fehlen der Schiedssprache → Streit über Verfahrenssprache |
| 10 | Behördliche Einreichung auf Deutsch? | Handelsregister, Finanzamt, Transparenzregister: Einreichung ausschließlich auf Deutsch | Englische Fassung wird nicht angenommen |
| 11 | Vollstreckungsübersetzung geplant? | Bei englischsprachigem Schiedsspruch: beglaubigte DE-Übersetzung für Vollstreckung vorbereitet? | § 1064 Abs. 3 ZPO: Pflicht bei Vollstreckungsantrag in Deutschland |
| 12 | Standard-Glossar gepflegt? | Mandatsbezogenes Glossar mit allen Fachbegriffen und ihren EN-Äquivalenten angelegt? | Konsistenz über alle Dokumente; bei Anpassungen einfaches Update |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Welche Sprachfassung gilt bei Widerspruch? | Vertragspartei, die sich auf eine bestimmte Fassung beruft | Ohne Vorrang-Klausel: Auslegung nach §§ 133, 157 BGB; mit Vorrang-Klausel: deutsche Fassung gilt |
| Ordnungsgemäße Dolmetscher-Bestellung bei Beurkundung | Notar (Protokollpflicht nach § 36 BeurkG) | Nachweis durch Beurkundungsprotokoll |
| Übersetzungsfehler liegt vor | Derjenige, der sich auf den Übersetzungsfehler beruft | Vergleich beider Sprachfassungen; ggf. Sachverständigengutachten |
| Anwaltshaftung wegen Auslegungsrisiko | Mandant (Nachweis des Schadens) | Beratungsfehler: kein Hinweis auf fehlende Vorrang-Klausel; Kausalität für Schaden |

## Fristen und Verjährung

| Frist | Norm | Inhalt | Folge |
|---|---|---|---|
| Beurkundung nach Entwurfsfertigstellung | Keine gesetzliche Frist; Notartermin-Vorlauf | Praxis: 2–4 Wochen Vorlauf für Notartermin; bei Ausländern länger (Dolmetscher, Übersetzung) | Terminversäumnis verzögert Closing |
| Übersetzung (juristisch) | Keine gesetzliche Frist | Fachübersetzung 20–50 Seiten: 3–10 Werktage bei qualifiziertem Translator | Engpass bei Zeitdruck |
| Anwaltshaftung für Beratungsfehler | §§ 195, 199 BGB | 3 Jahre ab Kenntnis des Mandanten vom Schaden | Verjährung des Haftungsanspruchs wegen fehlendem Vorrang-Klausel-Hinweis |
| Schiedsspruch-Vollstreckung | § 1064 ZPO i.V.m. § 1061 ZPO (New York Convention) | Antrag auf Vollstreckbarerklärung; beglaubigte Übersetzung beizufügen | Ohne Übersetzung: Antrag unzulässig |

## Typische Übersetzungsfallen

### Gesellschaftsrechtliche Rechtsbegriffe

| Deutscher Begriff | Korrekte EN-Übersetzung | Häufiger Fehler |
|---|---|---|
| GmbH | GmbH (in Klammern: Gesellschaft mit beschränkter Haftung) oder "limited liability company under German law" | "LLC" — falsch, weil LLC ein US-amerikanisches Konstrukt ist |
| Geschäftsführer | Managing Director | "CEO", "Director" — nicht rechtsgenau; CEO ist kein Rechtsbegriff |
| Gesellschafterversammlung | Shareholders' Meeting oder General Meeting | "Stockholders Meeting" — US-Terminologie |
| Stammkapital | Share capital | "Stock capital" — ungebräuchlich im englischen GmbH-Kontext |
| Satzung | Articles of Association | "Articles of Incorporation" — US-Terminologie; "Statute" mehrdeutig |
| Einziehung von Anteilen | Redemption of shares | "Cancellation" — Nuance: Einziehung nach § 34 GmbHG ist Sonderfall |
| Gesellschaftervereinbarung | Shareholders' Agreement (SHA) | "Partnership Agreement" — falsch; GmbH ist keine Partnership |
| Handelsregistereintragung | Commercial Register registration | "Corporate filing" — zu unspezifisch |
| Jahresabschluss | Annual financial statements | "Annual report" — zu weit; Annual report umfasst mehr als Jahresabschluss |
| Prokura | Commercial power of attorney / Prokura | Keine exakte EN-Entsprechung; "Prokura" im Klammern behalten |

### Startup-Terminologie

| Begriff | Standard DE | Standard EN | Kommentar |
|---|---|---|---|
| Liquidation Preference | Liquidationsvorrang | Liquidation Preference | Englischer Begriff im deutschen Kontext etabliert; Doppelbezeichnung empfohlen |
| Drag-Along | Mitziehverpflichtung | Drag-Along Obligation | Beide Fassungen verwenden; englischer Begriff als Kurzbezeichnung |
| Tag-Along | Mitveräußerungsrecht | Co-Sale Right oder Tag-Along Right | Co-Sale Right juristisch präziser im Britischen Englisch |
| Anti-Dilution | Verwässerungsschutz | Anti-Dilution Protection | Broad-Based Weighted Average: "gewichteter Mittelwert (breite Basis)" |
| Vesting | Erdienen von Anteilen | Vesting | Cliff: "Cliff-Periode" oder "Anlaufphase"; 1-year cliff: 12-monatige Cliff-Periode |
| Bad Leaver | Schlechter Aussteiger | Bad Leaver | Begriff wird auf Englisch verwendet; DE-Erläuterung im Vertrag |
| ESOP | Mitarbeiterbeteiligungsprogramm | Employee Share Option Plan (ESOP) | VSOP (Virtual Share Option Plan): "virtuelles Mitarbeiterbeteiligungsprogramm" |
| Pre-Money Valuation | Bewertung vor der Finanzierungsrunde | Pre-Money Valuation | Kein übliches deutsches Äquivalent; englischer Begriff |
| Term Sheet | Eckpunktepapier / Term Sheet | Term Sheet | Term Sheet nicht verbindlich (i.d.R.); Letter of Intent (LOI) verbindlicher |
| Cap Table | Beteiligungsübersicht | Capitalisation Table (Cap Table) | Cap Table als Kurzbezeichnung auch auf Deutsch üblich |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Bilinguales Dokument erstellen Deutsch-Englisch | Bilinguale Vorlage nach Vorrang-Klausel-Schema; Template unten |
| Variante A — Nur eine Sprache rechtlich bindend | Monolinguales Kerndokument mit Uebersetzung zur Information |
| Variante B — Fremdrechts-Bezug notwendig Governing Law noetig | Rechtswahl-Klausel und Gerichtsstand explizit regeln |
| Variante C — Mandant will nur interne Verwendung kein Vollzug noetig | Vereinfachte Uebersetzung ohne juristische Bindefassung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Sprachvorrang-Klausel (vollständig, für alle Dokumenttypen)

```
§ [X] Sprache / Language

(1) Diese [Vereinbarung / Satzung / der vorliegende Vertrag] ist in deutscher und
englischer Sprache abgefasst. Bei Widersprüchen oder Auslegungszweifeln zwischen
den beiden Sprachfassungen geht der deutsche Text vor. Soweit eine notarielle
Beurkundung nach § 2 GmbHG oder § 15 GmbHG erforderlich ist, ist allein die deutsche
Fassung Beurkundungsgrundlage; die englische Fassung dient lediglich als
"Convenience Translation".

(2) This [Agreement / Articles of Association / Agreement] is executed in German and
English language. In case of any discrepancies or doubts of interpretation between
the two language versions, the German version shall prevail. Where notarial recording
pursuant to § 2 GmbHG or § 15 GmbHG is required, only the German version shall
constitute the basis of the notarial deed; the English version serves as a
convenience translation only.

Grundlage: § 184 GVG (Amtssprache Deutsch); § 5 BeurkG (Beurkundungssprache);
§ 1064 Abs. 3 ZPO (Vollstreckung).
```

### Baustein 2: Term Sheet bilingual (strukturiertes Muster)

```
TERM SHEET / ECKPUNKTEPAPIER
[Gesellschaft] — Series A Finanzierungsrunde

Dieses Term Sheet ist nicht verbindlich, soweit nicht ausdrücklich anders vermerkt.
This Term Sheet is non-binding, unless expressly stated otherwise.

---------------------------------------------------------------------------
DEUTSCH | ENGLISCH
---------------------------------|--------------------------------------------
Gesellschaft / Company | [Firma] GmbH, [Sitz], HRB [Nr.]
Investor / Investor | [Investor Name], [Adresse]
Investitionsbetrag / | EUR [X]
Investment Amount |
Pre-Money Bewertung / | EUR [Y]
Pre-Money Valuation |
Post-Money Bewertung / | EUR [Y+X]
Post-Money Valuation |
Neue Anteile / New Shares | [N] Class B Geschäftsanteile (Class B Shares)
Anteil Investor / | [Z] %
Investor's Stake |
---------------------------------|--------------------------------------------
RECHTE DES INVESTORS | INVESTOR RIGHTS
Liquidationsvorrang / | 1x non-participating Liquidation Preference
Liquidation Preference |
Verwässerungsschutz / | Weighted Average Broad-Based Anti-Dilution
Anti-Dilution |
Sondervetorechte / | Veto rights on: [Aufzählung / List]
Special Veto Rights |
Drag-Along Schwelle / | 75 % der Stimmrechte / of voting rights
Drag-Along Threshold |
Tag-Along / Co-Sale Right | Pro rata bei Kontrollwechsel / on change of control
---------------------------------|--------------------------------------------
GRÜNDER-RECHTE | FOUNDER RIGHTS
Vesting-Periode / | 48 Monate / months, 12 Monate Cliff / month cliff
Vesting Period |
Bad Leaver: unvested Anteile / | Zum Nennwert / at nominal value
Bad Leaver: unvested shares |
Good Leaver: unvested Anteile / | Zum Verkehrswert / at fair market value
Good Leaver: unvested shares |
---------------------------------|--------------------------------------------
MITARBEITER-POOL / ESOP Pool | 10 % (pre-money) reserviert / reserved
---------------------------------|--------------------------------------------
SONSTIGES / OTHER
Schiedsklausel / Arbitration | DIS, Berlin, Deutsch / German
Anwendbares Recht / | Deutsches Recht / German law
Governing Law |
Exklusivität / Exclusivity | [N] Wochen / weeks ab Unterzeichnung / from signing
Kosten / Costs | Eigene Kosten / own costs

Bei Inkonsistenzen: deutsche Fassung geht vor.
In case of inconsistencies: German version prevails.
```

### Baustein 3: Draaft-Along-Klausel bilingual (vollständiges Muster)

```
§ [Y] Mitziehverpflichtung (Drag-Along) / Drag-Along Obligation

DEUTSCH:
(1) Stimmen Gesellschafter, die zusammen mindestens 75 % der Stimmrechte an der
Gesellschaft halten ("Drag-Along-Initiatoren"), einem Verkauf sämtlicher
Geschäftsanteile an der Gesellschaft an einen Dritten zu, können sie die übrigen
Gesellschafter verpflichten, ihre Anteile zu denselben Bedingungen mitzuveräußern.

(2) Die Mitziehverpflichtung gilt nur, wenn:
a) der Verkaufspreis pro Anteil für alle Gesellschafter gleich ist;
b) der Erwerber kein verbundenes Unternehmen eines Initiators ist;
c) keine Gegenleistung disproportional zugunsten einzelner Initiatoren ist.

(3) Mitzieh-pflichtige Gesellschafter sind schriftlich mit einer Frist von
mindestens 30 Tagen zu informieren.

------

ENGLISH:
(1) If Shareholders holding in aggregate at least 75 % of the voting rights in the
Company ("Drag-Along Initiators") agree to a sale of all shares in the Company to a
third party, they may oblige the remaining Shareholders to co-sell their shares on
the same terms.

(2) The drag-along obligation shall only apply if:
a) the sales price per share is the same for all Shareholders;
b) the purchaser is not an affiliated company of any Initiator;
c) no consideration is disproportionately in favor of individual Initiators.

(3) Drag-bound Shareholders shall be notified in writing with a notice period of
at least 30 days.

------
Bei Widersprüchen geht die deutsche Fassung vor.
In case of discrepancies, the German version shall prevail.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Standard-Glossar (Musterformat für Mandatsakte)

```
STANDARD-GLOSSAR — [Mandant] — [Datum]
Gilt für alle Dokumente in diesem Mandat.

| Deutsch | Englisch | Anmerkung |
|-----------------------------|----------------------------------|-----------|
| Gesellschaft | Company | |
| Geschäftsanteile | Shares / Share capital | |
| Stammkapital | Share capital | Nicht "Stock capital" |
| Stammeinlage | Share contribution | |
| Gesellschafter | Shareholder | Nicht "Stockholder" (US) |
| Gesellschafterversammlung | Shareholders' Meeting | |
| Geschäftsführer | Managing Director | Nicht "CEO" |
| Satzung | Articles of Association | Nicht "Statute" |
| Gesellschaftervereinbarung | Shareholders' Agreement (SHA) | |
| Klasse A Anteile | Class A Shares | |
| Klasse B Anteile | Class B Shares | |
| Liquidationsvorrang | Liquidation Preference | |
| Verwässerungsschutz | Anti-Dilution Protection | |
| Mitziehverpflichtung | Drag-Along Obligation | |
| Mitveräußerungsrecht | Co-Sale Right (Tag-Along) | |
| Vesting-Periode | Vesting Period | |
| Cliff-Periode | Cliff Period | |
| Schlechter Aussteiger | Bad Leaver | |
| Guter Aussteiger | Good Leaver | |
| Bezugsrecht | Pre-emption Right | |
| Beirat | Advisory Board | |
| Jahresabschluss | Annual Financial Statements | |
| Handelsregister | Commercial Register | |
| Transparenzregister | Transparency Register | |
```

## bei bilingualer Erstellung

### Schritt 1: Deutsche Masterfassung

Erstellung der vollständigen deutschen Fassung; rechtsanwaltliche Prüfung und Freigabe.

### Schritt 2: Englische Übersetzung

Durch juristisch versierten Übersetzer mit deutschem Recht-Hintergrund — nicht allein durch maschinelle Übersetzung. Maschinenübersetzung (DeepL, ChatGPT) kann als Rohfassung dienen, aber zwingend qualitätskontrolliert werden.

### Schritt 3: Cross-Reading

Anwalt liest beide Fassungen parallel; Abgleich Abschnitt für Abschnitt. Bei Inkonsistenzen: deutsche Fassung anpassen oder Vorrang-Klausel explizit stärken.

### Schritt 4: Vorrang-Klausel einfügen

Standardklausel (Baustein 1) in alle Dokumente einfügen. Platzierung: § 1 oder letzter Abschnitt vor Unterschriften.

### Schritt 5: Notarielle Beurkundung (soweit erforderlich)

Beurkundung auf Deutsch (§ 5 BeurkG). Bei ausländischen Beteiligten: Dolmetscher beauftragen. Beide Fassungen werden unterzeichnet; deutsche bleibt verbindlich.

### Schritt 6: Glossar-Pflege

Mandatsbezogenes Glossar nach jeder Dokumenterstellung aktualisieren; für alle Folgedokumente konsistent verwenden.

## Behördeneinreichung und Schiedsverfahren

### Behördliche Einreichungen

Handelsregister, Finanzamt, Gewerbeamt, Transparenzregister: **ausschließlich auf Deutsch**. Englische Fassung wird nicht angenommen. Bei automatischen Einreichungstools: Sprache prüfen.

### Schiedsverfahren (DIS)

Bei DIS-Schiedsklausel: Schiedsverfahrenssprache explizit im Vertrag nennen. Standard: Deutsch. Bei Englisch als Schiedssprache: Vollstreckungsübersetzung für Deutschland vorbereiten (§ 1064 Abs. 3 ZPO). DIS-Notschiedsverfahren bei Eilbedarf möglich.

## Streitwert und Kosten

| Leistung | Kostenrahmen | Anmerkung |
|---|---|---|
| Juristische Übersetzung Satzung (15–20 Seiten) | 500–1.500 EUR | Abhängig von Stundensatz des Übersetzers (120–200 EUR/Std.) |
| Juristische Übersetzung SHA (30–60 Seiten) | 1.000–4.000 EUR | Komplexe Klauseln (Liquidation Preference, Anti-Dilution) erhöhen Aufwand |
| Dolmetscher bei Notarbeurkundung | 300–800 EUR (halber Tag) | Vereidigter Dolmetscher; Notargebühren zzgl. |
| Beglaubigte Übersetzung Schiedsspruch | 200–800 EUR | Je nach Seitenumfang; für § 1064 Abs. 3 ZPO erforderlich |
| Anwaltliche Qualitätskontrolle (Cross-Reading) | 500–2.000 EUR | 2–4 Stunden bei 200–400 EUR/Std. |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| US-amerikanischer Investor besteht auf englischsprachigem Dokument | Bilinguale Fassung mit strikter Vorrang-Klausel (DE über EN); US-Investor bekommt Comfort durch englische Fassung, Rechtsicherheit bleibt beim deutschen Text |
| Term Sheet-Verhandlung mit ausländischem VC | Term Sheet bilingual; non-binding, außer explizit markierten Punkten; keine Signing-Kosten durch Notar in diesem Stadium |
| Schiedsverfahren auf Englisch gewünscht | DIS bietet englisches Verfahren an; aber: für Vollstreckung in Deutschland DE-Übersetzung des Schiedsspruchs zwingend (§ 1064 Abs. 3 ZPO) |
| Mandant nutzt Online-Übersetzungstool | DeepL / ChatGPT als Rohfassung akzeptabel; aber zwingend juristische Qualitätskontrolle vor Verwendung; maschinelle Fachterm-Übersetzung bei GmbH-Recht fehlerhaft |
| Konsistenz über mehrere Dokumente hinweg | Standard-Glossar anlegen und für alle Folgedokumente verbindlich machen; Abweichungen dokumentieren |

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template: Vorrang-Klausel (einzusetzen in alle Dokumente)

**Adressat:** Vertrag oder Satzung mit ausländischen Beteiligten — Tonfall praezise-juristisch

```
§ [X] Sprache / Language

(1) Diese [Vereinbarung / Satzung / der vorliegende Vertrag] ist in
deutscher und englischer Sprache abgefasst. Bei Widerspruechen oder
Auslegungszweifeln zwischen den Sprachfassungen geht der deutsche
Text vor. Soweit eine notarielle Beurkundung nach § 2 GmbHG oder
§ 15 GmbHG erforderlich ist, ist allein die deutsche Fassung
Beurkundungsgrundlage; die englische Fassung dient als
"Convenience Translation".

(2) This [Agreement / Articles of Association] is executed in German
and English. In case of discrepancies, the German version prevails.
Where notarial recording pursuant to § 2 GmbHG or § 15 GmbHG is
required, only the German version constitutes the basis of the
notarial deed; the English version serves as a convenience
translation only.
```

## Output-Template: Qualitaetscheckliste für bilinguale Dokumente

**Adressat:** Interne Qualitaetskontrolle — Tonfall sachlich

```
QUALITAETS-CHECKLISTE BILINGUALE DOKUMENTE
Mandat: [MANDANT] | Dokument: [TYP] | Datum: [DATUM]

[ ] Vorrang-Klausel eingefuegt (DE ueber EN)
[ ] Deutsche Masterfassung vollstaendig und geprueft
[ ] Uebersetzung durch juristisch versierten Uebersetzer
[ ] Cross-Reading (beide Fassungen parallel gelesen)
[ ] Glossar-Konsistenz geprueft (alle Dokumente einheitlich)
[ ] Notarielle Anforderungen: Dolmetscher bei Auslaendern (§ 5 BeurkG)?
[ ] Behörden-Einreichungen nur auf Deutsch
[ ] Schiedssprache explizit vereinbart (falls DIS-Klausel)
[ ] Vollstreckungsuebersetzung vorgeplant (§ 1064 Abs. 3 ZPO)?
[ ] Mandatsglossar aktualisiert
```

## Rote Schwellen

- Kein Dolmetscher bei Beurkundung mit sprachunkundigen Auslaedern: Nichtigkeit (§ 5 BeurkG; OLG Frankfurt 2019)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Ausschliesslich englischsprachige Einreichung beim Handelsregister, Finanzamt: wird nicht angenommen
- Schiedsspruch auf Englisch ohne Uebersetzung: Vollstreckungsantrag in Deutschland unzulaessig (§ 1064 Abs. 3 ZPO)

## Anschluss-Skills

- `gesellschaftsgruender-klauselkatalog-bilingual` — Volltext-Klauseln DE/EN für alle Klauseltypen
- `gesellschaftsgruender-intake-decision-tree` — Workflow-Steuerung mit bilingualer Ausgabe
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — Eilantraege in Deutsch (Gerichtssprache)
- `gesellschaftsgruender-rechtsformwahl` — Rechtsform bestimmt Dokumenttypen

## Quellen und Vertiefung

- § 184 GVG (Amtssprache Deutsch)
- § 5 BeurkG (Beurkundungssprache; Dolmetscher-Pflicht)
- §§ 133, 157 BGB (Auslegungsgrundsaetze)
- § 1064 Abs. 3 ZPO (Vollstreckung auslaendischer Schiedsspruche; Uebersetzungspflicht)
- § 1061 ZPO i.V.m. New York Convention (Anerkennung auslaendischer Schiedsspruche)
- Limmer/Hertel/Frenz/Mayer, Wuerzburger Notarhandbuch, 6. Aufl. 2021, Teil 3 Kap. 2 Rn. 45 ff.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
<!-- AUDIT 27.05.2026
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Aktion: Beide Einträge (Leitentscheidungen-Tabelle und Aktuelle Rechtsprechung) gelöscht.
-->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 49 GmbHG
- § 5a GmbHG
- § 2 GmbHG
- § 47 GmbHG
- § 15 GmbHG
- § 7 GmbHG
- § 40 GmbHG
- § 5 GmbHG
- § 9 GmbHG
- § 34 GmbHG
- § 43 GmbHG
- § 55a GmbHG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `egbr-mopeg-gesellschaftsgruender`

_GbR nach MoPeG 2024 und Eintragung ins Gesellschaftsregister als eGbR vorbereiten. Normen: §§ 705 ff. BGB n.F. MoPeG, §§ 707 ff. BGB Gesellschaftsregister. Prüfraster: Eintragungsvoraussetzungen, Gesellschafterverzeichnis, Vertretungsregeln, Haftungsfolgen. Output: eGbR-Gründungsunterlagen. Abgre..._

# eGbR und GbR nach MoPeG 2024

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `eGbR und GbR nach MoPeG 2024` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn

Klaere bei jedem eGbR-Mandat zuerst:

1. **Pflicht-Eintragung?** Grundstueckserwerb/-veraeusserung (Paragraf 707b BGB) oder GmbH-Anteilsbeteiligung (Paragraf 40 GmbHG)? Dann SOFORT Eintragung vor Notar-Termin.
2. **Innen-GbR oder Aussen-GbR?** Innen-GbR (kein Aussenauftritt): keine Pflicht. Aussen-GbR mit Rechtsverkehrsteilnahme: rechtsfaehig nach Paragraf 705 II BGB.
3. **Handelsgeschaeft oder Freiberuf?** OHG für Kaufleute; eGbR für Nicht-Kaufleute und Freiberufler.
4. **Haftungsbeschraenkung gewuenscht?** eGbR schafft keine Haftungsbeschraenkung; für begrenzte Haftung -> GmbH oder KG.
5. **Zeitrahmen?** Eintragung beim Amtsgericht dauert 2-6 Wochen; Notar-Termin für Grundstuecksgeschaeft erst nach Eintragung.
6. **Bestehendes Grundbuch-Eintrag "GbR bestehend aus A, B, C"?** Muss auf eGbR umgestellt werden.

## Zentrale Normen

- **§ 705 II BGB** — Rechtsfaehige GbR bei Teilnahme am Rechtsverkehr; gesetzliche Anerkennung
- **§ 707 BGB** — Freiwillige Eintragung in das Gesellschaftsregister (eGbR)
- **§ 707a II BGB** — Pflicht-Namenszusatz "eGbR" / "eingetragene Gesellschaft buergerlichen Rechts"
- **§ 707a III BGB** — Vertrauensschutz Dritter auf Registerpublizitaet (analog Paragraf 15 HGB)
- **§ 707b BGB** — Pflicht-Eintragung bei Grundstuecksgeschaeften; Grundbuchverfahren
- **§ 720 I BGB** — Grundsatz der Gesamtvertretung; Satzungsabweichung moeglich
- **§ 721 BGB** — Gesamtschuldnerische Aussenhaftung aller Gesellschafter (unbeschraenkt)
- **§ 723 BGB** — Fortbestand der Gesellschaft bei Ausscheiden eines Gesellschafters (Kernneuerung MoPeG)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema: eGbR-Eintragungsentscheidung

| Schritt | Frage | Norm | Ergebnis |
|---|---|---|---|
| 1 | Aussen-GbR mit Rechtsverkehrsteilnahme? | § 705 II BGB | Ja: rechtsfaehig. Nein: Innen-GbR |
| 2 | Grundstuecksgeschaeft geplant? | § 707b BGB | Ja: Pflicht-Eintragung VOR Notar-Termin |
| 3 | GmbH-Anteilsbeteiligung? | § 40 GmbHG | Ja: eGbR-Eintragung Voraussetzung |
| 4 | Handelsgeschaeft? | § 1 HGB | Ja: OHG statt eGbR (Handelsregister) |
| 5 | Haftungsbeschraenkung gewuenscht? | § 721 BGB | eGbR bietet keine; GmbH/KG pruefen |
| 6 | Vertrauensschutz für Geschaeftspartner gewuenscht? | § 707a III BGB | Eintragung schafft Publizitaet |
| 7 | Bestehendes Grundbuch auf alte GbR? | § 47 GBO | Umschreibung auf eGbR nach Eintragung |

## Schritt-für-Schritt-Workflow

1. **Qualifikation:** Innen-GbR oder Aussen-GbR? Handelsgeschaeft oder nicht? Freiberufler-Sozietaet?
2. **Pflicht pruefen:** Grundstueck oder GmbH-Anteil betroffen? Dann Eintragung zwingend.
3. **Gesellschaftsvertrag entwerfen** (formfrei, aber schriftlich empfohlen): Gegenstand, Einlagen, Vertretung, Gewinnverteilung, Ausscheiden, Fortbestandsklausel (§ 723 BGB).
4. **Anmeldung beim Amtsgericht:** Alle Gesellschafter; notarielle Beglaubigung der Unterschriften; Gebuehr ca. 80-150 EUR.
5. **Eintragung abwarten:** Veröffentlichung im Bundesanzeiger; Namenszusatz "eGbR" ab sofort zu fuehren.
6. **Grundbuch-Umschreibung:** Bei bestehendem Grundbuch-Eintrag auf alte GbR: Berichtigungsantrag stellen.
7. **Folge-Anmeldungen:** Gewerbeamt, Finanzamt, Transparenzregister (§ 20 GwG).
8. **Gesellschafterwechsel:** Bei Eintritt / Ausscheiden: Registeraenderung + ggf. neuer Grundbucheintrag.

## Output-Template: Anmeldung eGbR

**Adressat:** Amtsgericht (Gesellschaftsregister) — Tonfall sachlich-formal

```
An das Amtsgericht [ORT]
— Gesellschaftsregister —

Anmeldung der eingetragenen Gesellschaft buergerlichen Rechts (eGbR)
nach § 707 BGB

Wir, die unterzeichneten Gesellschafter der Gesellschaft buergerlichen
Rechts, melden zur Eintragung in das Gesellschaftsregister an:

1. Name: [GESELLSCHAFTSNAME] eGbR
2. Sitz: [ADRESSE]
3. Gegenstand: [GEGENSTAND]
4. Gesellschafter:
 a) [NAME 1], geb. [DATUM], [ADRESSE]
 b) [NAME 2], geb. [DATUM], [ADRESSE]
5. Vertretungsbefugnis: [Gesamtvertretung / Einzelvertretung gemaess
 Gesellschaftsvertrag § X]

Anlagen:
- Gesellschaftsvertrag vom [DATUM]
- Notarielle Beglaubigungs-Urkunde Nr. [NR.]

[ORT], [DATUM]
Unterschriften aller Gesellschafter (notariell beglaubigt)
```

## Rote Schwellen

- Grundstueckskauf ohne eGbR-Eintragung: Auflassung scheitert; Notartermin nicht durchfuehrbar. Hinweis: BGH-Linie ueber das Voreintragungserfordernis nach MoPeG ist mittlerweile durch erste obergerichtliche und BGH-Entscheidungen gefestigt (siehe Vertiefung). Konkrete Aktenzeichen vor Verwendung live verifizieren.
- Namenszusatz "eGbR" vergessen nach Eintragung: Ordnungswidrigkeit; Haftungsfolgen
- Eintragung = Haftungsbeschraenkung: FALSCH. Alle Gesellschafter haften weiter unbeschraenkt (§ 721 BGB)
- GbR als GmbH-Gesellschafter ohne eGbR: Eintragung in Gesellschafterliste nicht moeglich (§ 40 GmbHG)

## Quellen und Vertiefung

- §§ 705-740 BGB (MoPeG-Fassung ab 01.01.2024): https://www.gesetze-im-internet.de/bgb/__705.html
- §§ 707, 707a, 707b BGB (Gesellschaftsregister; Voreintragungserfordernis Grundstuecksgeschaefte): https://www.gesetze-im-internet.de/bgb/__707.html
- §§ 720, 721, 723, 728b BGB: https://www.gesetze-im-internet.de/bgb/__721.html
- § 40 GmbHG (Gesellschafterliste; eGbR-Eintragung als Voraussetzung der Listung als Gesellschafterin): https://www.gesetze-im-internet.de/gmbhg/__40.html
- MoPeG (BGBl. I 2021, 3436): https://www.bgbl.de/xaver/bgbl/start.xav?startbk=Bundesanzeiger_BGBl&start=//*[@attr_id=%27bgbl121s3436.pdf%27]
- BGH, Beschl. v. 03.07.2025 — V ZB 17/24 (Voreintragung der GbR im Gesellschaftsregister vor Grundbuchaenderung; ECLI:DE:BGH:2025:030725BVZB17.24.0): https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr=142513
- Weitere obergerichtliche Linien zur Firmierung "eGbR" und identitaetswahrenden Umwandlung GbR -> KG/OHG (Beispiele aus 2024, vor Verwendung Aktenzeichen pruefen):
 - OLG Hamburg, Beschl. v. 22.04.2024 — 11 W 19/24
 - OLG Koeln, Beschl. v. 22.04.2024 — 4 Wx 4/24
 - OLG Muenchen, Beschl. v. 2024 — 34 Wx 71/24 e
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Uebergabe an andere Skills

- `gesellschaftsgruender-rechtsformwahl` — Vergleich zu anderen Formen (GmbH, KG, OHG)
- `gesellschaftsgruender-handelsregister-anmeldung` — bei Umwandlung in OHG
- `gesellschaftsgruender-transparenzregister` — wirtschaftlich Berechtigte
- `gesellschaftsgruender-kommandocenter` — Gesamtablauf

---

## Skill: `firmenname-pruefung`

_Firmenname auf Zulässigkeit und Verwechslungsgefahr prüfen: Differenzierungsgebot, Irreführungsverbot. Normen: §§ 17 18 HGB, § 4 GmbHG. Prüfraster: Unterscheidungskraft, Irreführungsverbot, Handelsregisterfähigkeit, Markenrecherche-Empfehlung. Output: Prüfergebnis Firmenname mit Handlungsempfehlu..._

# Firmenname-Prüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Firmenname-Prüfung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn

Klaere mindestens 2 Wochen vor Notar-Termin:

1. **3-5 Wunsch-Firmen bereit?** Immer Alternativen vorbereiten; Plan A kann beanstandet werden.
2. **Branchenbezeichnung im Namen?** Pruefen ob Zulassung erforderlich (Bank: BaFin; Steuer: StBerG; Rechts: RAK).
3. **Personenname im Firmennamen?** Eigener Name: unproblematisch; fremder Name: Berechtigung pruefen (§ 12 BGB).
4. **Marken-Relevanz?** Bei Startup oder Brand mit Aussenauftritt: DPMA/EUIPO-Recherche vor Eintragung.
5. **Internationale Aktivitaet?** Bedeutung des Namens in Zielmaerkten pruefen; schwer aussprechbare Namen vermeiden.
6. **Domain bereits gesichert?** Domain VOR Notar-Termin sichern; nachtraeglich oft nicht mehr verfuegbar.

## Zentrale Normen

- **§ 17 HGB** — Firma ist der Name, unter dem Kaufmann im Handelsverkehr auftritt
- **§ 18 I HGB** — Kennzeichnungsgeeignetheit der Firma
- **§ 18 II HGB** — Irreführungsverbot; keine Firma, die zur Taeuschung geeignet ist
- **§ 19 HGB** — Pflicht-Rechtsform-Zusatz (GmbH, AG, OHG, KG usw.)
- **§ 30 HGB** — Verwechslungsgefahr; am Ort Pflicht zur Unterscheidbarkeit von bestehenden Firmen
- **§ 12 BGB** — Namensrecht; Schutz des Namensrechts bei Verwendung fremder Namen
- **§ 14 MarkenG** — Verletzung einer eingetragenen Marke durch Firmenname; Unterlassungsanspruch

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema: Firmennamen-Check

| Schritt | Pruefung | Stelle | Ergebnis |
|---|---|---|---|
| 1 | Handelsregister-Suche bundesweit | gemeinsam.handelsregister.de | Konflikt? Wenn ja, Name anpassen |
| 2 | IHK-Firmenvorpruefung beantragt | Oertliche IHK | Bescheinigung erhalten? |
| 3 | Kennzeichnungseignung geprueft | Selbst / Anwalt | Nicht generisch; Unterscheidungskraft vorhanden |
| 4 | Irrefuehrungs-Check | Selbst | Keine falsche Branchenangabe; keine Zulassungs-Vortaeuschung |
| 5 | Rechtsform-Zusatz vorhanden | Selbst | GmbH / UG / AG / OHG explizit angegeben |
| 6 | DPMA-Marken-Recherche | dpma.de | Kein identischer / aehnlicher Markenname |
| 7 | EUIPO-Marken-Recherche | euipo.europa.eu | EU-Marken-Konflikt? |
| 8 | Domain .de gesichert | DENIC / Registrar | Verfuegbar und gesichert VOR Notar |
| 9 | Domain .com gesichert | Registrar | Verfuegbar und gesichert |
| 10 | Personenname-Berechtigung | Selbst | Eigener Name oder nachgewiesene Berechtigung |
| 11 | Branchenbezeichnung-Zulassung | Berufsrecht | Bank, Steuer, Rechts, Arzt: Zulassung geprueft |
| 12 | Internationale Bedeutung geprueft | Selbst | Keine negativen Konnotationen in Zielmaerkten |

## Schritt-für-Schritt-Workflow

1. **T-14 (2 Wochen vor Notar):** 3-5 Wunsch-Namen listen; HR-Suche nationwide; DPMA-Stichprobe.
2. **T-10:** IHK-Vorpruefung beantragen (oft binnen 2-5 Werktagen); Domain-Verfuegbarkeit pruefen.
3. **T-7:** IHK-Bescheinigung liegt vor; Domain bei Verfuegbarkeit SOFORT sichern; ggf. Marken-Anmeldung einleiten.
4. **T-3:** Alle Alternativen bereit halten; Marken-Recherche abgeschlossen.
5. **T (Notar-Termin):** Beurkundung mit gewaehltem Namen; IHK-Bescheinigung dem Notar vorlegen.
6. **T+5 bis T+14 (HR-Pruefung):** HR-Gericht prueft; bei Beanstandung: Satzungsaenderung und erneute Beurkundung (Kosten ca. 300-600 EUR).
7. **Nach Eintragung:** Marken-Anmeldung auf Gesellschaft umschreiben (falls zuvor auf Gruender angemeldet).

## Output-Template: Firmenname-Pruefprotokoll

**Adressat:** Interne Dokumentation / Anwaltsakte

```
FIRMENNAME-PRUEFPROTOKOLL
Mandant: [NAME] | Datum: [DATUM] | Notar-Termin: [DATUM]

Gewuenschte Firmennamen (Prioritaetsreihenfolge):
1. [NAME 1] GmbH
2. [NAME 2] GmbH
3. [NAME 3] GmbH

Pruef-Ergebnisse:

| Pruefung | Name 1 | Name 2 | Name 3 |
|---------------------------|-------------|-------------|-------------|
| HR-Suche (HR-Bezirk) | OK / Konflikt| OK / Konflikt| OK / Konflikt|
| IHK-Vorpruefung | Bestätigt | Ausstehend | - |
| DPMA Marken | OK | Konflikt | OK |
| EUIPO Marken | OK | OK | OK |
| Domain .de | Gesichert | Vergeben | Verfuegbar |
| Domain .com | Verfuegbar | Vergeben | Verfuegbar |
| Irrefuehrungs-Check | OK | - | - |
| Branchenbezeichnung-Zulass.| n/a | - | - |

Empfehlung: [NAME 1] GmbH (keine Konflikte, Domain gesichert)
Fallback: [NAME 3] GmbH

Naechste Schritte:
[ ] IHK-Bescheinigung für [NAME 1] einholen
[ ] Domain [name1].de registriert am [DATUM]
[ ] Marken-Anmeldung DPMA für [NAME 1] einleiten?
```

## Rote Schwellen

- Branchenbezeichnung "Bank", "Versicherung", "Steuerberatung" ohne Zulassung: Beanstandung und Ordnungswidrigkeitsverfahren
- Verwechslungsgefahr mit bestehender Firma im Registerbereich: Beanstandung HR-Gericht (§ 30 HGB)
- Fremder Name ohne Berechtigung: Namensklage nach § 12 BGB; Unterlassung und Schadenersatz
- Marken-Verletzung durch Firmennamen: Unterlassungsklage; Umfirmierungspflicht; erhebliche Kosten

## Quellen und Vertiefung

- §§ 17-30 HGB (Firmenrecht), § 12 BGB, § 14 MarkenG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Uebergabe an andere Skills

- `gesellschaftsgruender-gmbh-vorbereitung` — Firmenname als Baustein der Vorbereitung
- `gesellschaftsgruender-notar-vorbereitung` — IHK-Bescheinigung vorlegen
- `gesellschaftsgruender-handelsregister-anmeldung` — HR-Pruefung durch Registergericht

---

## Skill: `genehmigtes-kapital`

_Genehmigtes Kapital für GmbH oder AG in Satzung aufnehmen: Ermaechtigungsbeschluss, Hoechstbetrag, Bezugsrechtsausschluss. Normen: §§ 55a GmbHG, §§ 202 ff. AktG. Prüfraster: Ermaechtigungsrahmen, Fristen, Bezugsrechte, Eintragungserfordernis. Output: Satzungsklausel genehmigtes Kapital. Abgrenzun..._

# Genehmigtes Kapital (§ 55a GmbHG)

## Arbeitsbereich

Genehmigtes Kapital für GmbH oder AG in Satzung aufnehmen: Ermaechtigungsbeschluss, Hoechstbetrag, Bezugsrechtsausschluss. Normen: §§ 55a GmbHG, §§ 202 ff. AktG. Prüfraster: Ermaechtigungsrahmen, Fristen, Bezugsrechte, Eintragungserfordernis. Output: Satzungsklausel genehmigtes Kapital. Abgrenzung: nicht ordentliche Kapitalerhöhung § 55 GmbHG. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Genehmigtes Kapital (§ 55a GmbHG)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre vor dem Vorratsbeschluss

1. Ist eine Finanzierungsrunde, ein ESOP-Pool oder ein Wandeldarlehen in den nächsten 5 Jahren geplant, das eine Kapitalerhöhung erfordert?
2. Soll der Bezugsrechtsausschluss der Gesellschafter zugelassen werden (Standard bei Investor-Einstieg)?
3. Beträgt das geplante genehmigte Kapital maximal 50 % des aktuellen Stammkapitals?
4. Liegt ein aktueller Satzungsentwurf vor — genehmigtes Kapital muss in die Satzung eingetragen werden?
5. Wird eine Satzungsänderung (75-%-Mehrheit) benötigt, oder ist das genehmigte Kapital bereits in der Gründungssatzung vorgesehen?

## Zentrale Normen

- **§ 55a GmbHG** — genehmigtes Kapital: Ermächtigung der GF durch Satzung; Höchstbetrag 50 % des Stammkapitals; Geltungsdauer max. 5 Jahre.
- **§ 53 Abs. 2 GmbHG** — Satzungsänderung erfordert 75-%-Mehrheit der Gesellschafter.
- **§ 55 GmbHG** — ordentliche Kapitalerhöhung: Vergleichsobjekt; immer GV-Beschluss erforderlich.
- **§ 55 Abs. 2 GmbHG** — Bezugsrecht bei Kapitalerhöhung; Ausschluss durch qualifizierten Beschluss.
- **§ 57j GmbHG** — Wandelanleihe; Nennkapitaländerung; Bezugsrecht der Gesellschafter.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema Genehmigtes Kapital

| Prüfungspunkt | Anforderung | Ergebnis |
|---|---|---|
| Höchstbetrag | Max. 50 % des aktuellen Stammkapitals | [EUR] |
| Geltungsdauer | Max. 5 Jahre ab Eintragung der Satzungsänderung | [Datum] |
| Form | Satzungsänderung durch Notar beurkundet | Ja/Nein |
| Beschlussmehrheit | 75 % der Gesellschafter-Stimmen | Erreichbar? |
| Bezugsrecht | Soll Ausschluss möglich sein? Sachliche Rechtfertigung dokumentieren | Ja/Nein |
| Anteilsklassen | Welche Klassen können ausgegeben werden? | [Common, A, B] |
| Wandeldarlehen | Soll Wandlung aus genehmigtem Kapital möglich sein? | Ja/Nein |

## Muster-Satzungsklausel Genehmigtes Kapital

```
§ [X] Genehmigtes Kapital

(1) Die Geschäftsführer sind ermächtigt, das Stammkapital der Gesellschaft bis zum
[DATUM — max. 5 Jahre ab Eintragung] einmalig oder mehrfach um insgesamt bis zu
[BETRAG — max. 50 % des Stammkapitals] EUR durch Ausgabe neuer Geschäftsanteile
gegen Bar- oder Sacheinlage zu erhöhen (Genehmigtes Kapital).

(2) Die Geschäftsführer sind ermächtigt, mit Zustimmung der Gesellschafterversammlung
(einfache Mehrheit) das Bezugsrecht der Gesellschafter ganz oder teilweise auszu-
schließen, wenn ein sachlicher Grund vorliegt (insbesondere Aufnahme eines strate-
gischen Investors, Wandlung eines Wandeldarlehens, Ausgabe von Mitarbeiterbeteili-
gungen aus einem ESOP-Pool).

(3) Die neuen Geschäftsanteile können als Stammanteile (Class Common) oder als
Vorzugsanteile (Class A oder Class B) mit den in der Gesellschaftervereinbarung
definierten Rechten ausgegeben werden.

(4) Die Geschäftsführer sind ermächtigt, die näheren Bedingungen der jeweiligen
Kapitalerhöhung (insbesondere Ausgabepreis, Klasse, Bezugsrecht) im Einvernehmen
mit der Gesellschafterversammlung festzusetzen.

(5) Diese Ermächtigung erlischt am [DATUM] und kann durch Beschluss der Gesellschafter-
versammlung mit 75-%-Mehrheit erneuert werden.
```

## Anwendungsfälle

| Anwendungsfall | Vorgehen mit genehmigtem Kapital |
|---|---|
| Seed-Investor | GF-Beschluss aus genehmigtem Kapital; neue Anteile ohne GV-Beschluss; Notar + HR |
| Wandeldarlehen → Anteile | Wandlung erfolgt durch GF-Erklärung; neue Anteile aus genehmigtem Kapital; Notar + HR |
| ESOP-Pool einrichten | GF gibt neue Anteile an ESOP-Treuhänder; oder VSOP ohne echte Anteile (einfacher) |
| Series-A-Zeitdruck | Kein GV-Einberufungserfordernis (1-2 Wochen Vorlauf); GF-Beschluss sofort möglich |

## Schritt-für-Schritt-Workflow

1. **Triage** — 5 Triage-Fragen beantworten; Bedarf für genehmigtes Kapital bestätigen.
2. **Höchstbetrag und Geltungsdauer festlegen** — max. 50 % Stammkapital; Laufzeit max. 5 Jahre.
3. **Satzungsklausel entwerfen** — Muster oben anpassen; Bezugsrechtsausschluss-Option einbauen.
4. **Satzungsänderungsbeschluss** — GV-Einberufung; 75-%-Mehrheit erforderlich; Notar beurkundet.
5. **HR-Anmeldung** — Notar meldet Satzungsänderung beim HR; Eintragung ca. 2-4 Wochen.
6. **Ausübung genehmigtes Kapital** — bei Bedarf: GF-Beschluss; neue Gesellschafterliste; Notar-Beglaubigung; HR-Anmeldung.
7. **Ablaufdatum überwachen** — bei Ablauf: Erneuerung durch neuen GV-Beschluss.

## Output-Template GF-Beschluss zur Ausübung

**Adressat:** Notar / Handelsregister — Tonfall formal-juristisch
```
GESCHÄFTSFÜHRERBESCHLUSS
Ausübung des Genehmigten Kapitals gemäß § [X] des Gesellschaftsvertrags

Gesellschaft: [Firmenname] GmbH
Datum: [Datum]
Geschäftsführer: [Name(n)]

Die Geschäftsführung beschließt:

1. Das Stammkapital der Gesellschaft wird von [bisheriges Stammkapital] EUR um
 [Erhöhungsbetrag] EUR auf [neues Stammkapital] EUR erhöht durch Ausgabe von
 [Anzahl] neuen Geschäftsanteilen zu je [Nennwert] EUR.

2. Die neuen Anteile werden als [Klasse] ausgegeben.

3. Die neuen Anteile werden übernommen von:
 [Name], [Adresse], Einlage: [EUR], Ausgabepreis: [EUR pro Anteil].

4. Das Bezugsrecht der übrigen Gesellschafter ist ausgeschlossen. Sachlicher Grund:
 [Investor-Aufnahme / Wandlung Wandeldarlehen / ESOP-Pool / etc.].

5. Die Geschäftsführung wird beauftragt, die Kapitalerhöhung beim Handelsregister
 anzumelden und eine aktualisierte Gesellschafterliste einzureichen.

[Unterschriften Geschäftsführer]
```

## Rote Schwellen

- Höchstbetrag > 50 % des Stammkapitals → Satzungsklausel nichtig; Ausübung unwirksam.
- Geltungsdauer > 5 Jahre → Klausel erlischt nach 5 Jahren; Erneuerung erforderlich.
- Bezugsrechtsausschluss ohne sachliche Rechtfertigung → anfechtbar (BGH Kali+Salz).
- Satzungsänderung ohne 75-%-Mehrheit → Beschluss nichtig.
- Ausübung nach Ablauf der Ermächtigung → Kapitalerhöhung unwirksam; HR-Eintragung scheitert.

## Quellen und Vertiefung

- §§ 55, 55a, 53 GmbHG (genehmigtes Kapital, Kapitalerhöhung, Satzungsänderung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Übergabe an andere Skills

- `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` — ordentliche Kapitalerhöhung ohne genehmigtes Kapital
- `gesellschaftsgruender-share-classes-a-b-c` — Anteilsklassen bei Ausübung
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — Bezugsrechtsausschluss-Anfechtung
- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Satzungsklausel einbetten

---

## Skill: `geschaeftsfuehrer-pflichten-startphase`

_Pflichten des GmbH-Geschäftsführers in Gründungs- und Startphase: Stammkapitaleinzahlung, Insolvenzantragspflicht, Buchführung. Normen: §§ 35 43 64 GmbHG, § 15a InsO. Prüfraster: Handlungspflichten, Haftungsrisiken, Compliance-Checkliste. Output: Pflichtenliste Geschäftsführer Gründungsphase. Abg..._

# Erste 100 Tage Geschäftsführer-Pflichten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erste 100 Tage Geschäftsführer-Pflichten` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre beim GF-Start

1. Ist der GF Gesellschafter-GF mit Mehrheit oder Fremd-GF? (Unterschied: BJR, Weisungsrecht, SV-Status)
2. Gibt es bereits Mitarbeiter — dann Lohnsteuer-Anmeldung und SV-Beiträge sofort.
3. Welches Geschäftsjahr — Kalenderjahr oder abweichendes Wirtschaftsjahr?
4. Ist das Unternehmen umsatzsteuerpflichtig oder kommt Kleinunternehmer-Regelung (§ 19 UStG) in Betracht?
5. Gibt es bereits Gläubiger / Schulden — Liquiditätsstatus sofort prüfen; keine masseschmälernden Zahlungen bei Insolvenzreife.
6. Besteht eine D&O-Versicherung oder soll eine abgeschlossen werden?

## Zentrale Normen

- **§ 43 GmbHG** — Sorgfaltspflicht des GF: Sorgfalt eines ordentlichen Geschäftsmannes; Haftung gegenüber Gesellschaft.
- **§ 15a InsO** — Insolvenzantragspflicht: 6 Wochen (Überschuldung) / 3 Wochen (Zahlungsunfähigkeit).
- **§ 15b InsO** — Zahlungsverbot nach Insolvenzreife; persönliche Haftung des GF.
- **§ 238 HGB** — Buchführungspflicht; doppelte Buchführung für GmbH zwingend.
- **§§ 264, 325 HGB** — Jahresabschluss aufstellen (3 Monate) und offenlegen (12 Monate).
- **§§ 18 UStG, 41a EStG, 19 KStG** — Steuervoranmeldungen und Vorauszahlungspflichten.
- **§ 19 GwG** — Transparenzregister-Meldepflicht; unverzüglich nach Gründung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 100-Tage-Pflichten-Matrix

| Pflicht | Frist | Norm | Konsequenz bei Versäumnis |
|---|---|---|---|
| Buchführung einrichten | sofort | § 238 HGB | Schätzung, Bußgeld, Haftung |
| Gewerbe anmelden | unverzüglich nach Aufnahme | § 14 GewO | Bußgeld bis 1.000 EUR |
| Steuerliche Erfassung FA | innerhalb 1 Monat | § 138 AO | Schätzung, Säumnis |
| USt-Voranmeldung einrichten | 10. des Folgemonats | § 18 UStG | Säumniszuschlag |
| Lohnsteuer-Anmeldung (bei MA) | 10. des Folgemonats | § 41a EStG | Haftung GF §§ 34, 69 AO |
| SV-Anmeldung Mitarbeiter | vor Beschäftigungsbeginn | § 28a SGB IV | Bußgeld bis 25.000 EUR |
| Transparenzregister | unverzüglich nach HR | § 19 GwG | Bußgeld bis 150.000 EUR |
| Jahresabschluss aufstellen | 3 Monate nach GJ-Ende | § 264 HGB | Ordnungsgeld bis 25.000 EUR |
| Bundesanzeiger-Offenlegung | 12 Monate nach GJ-Ende | § 325 HGB | Ordnungsgeld |
| Insolvenzlage überwachen | laufend | § 15a InsO | persönliche Haftung, Strafbarkeit |
| Datenschutz (DSGVO) | vor erstem Datenabruf | DSGVO Art. 24 | Bußgeld bis 20 Mio. EUR |
| Berufsgenossenschaft | binnen 1 Woche nach Aufnahme | § 192 SGB VII | Bußgeld |
| IHK-Mitgliedschaft | automatisch mit Gewerbe | § 2 IHKG | — |

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen beantworten; GF-Typ und Branche klären.
2. **Buchführung einrichten** — DATEV, sevDesk oder Lexware-Konto anlegen; Steuerberater einschalten.
3. **Gewerbeamt und Finanzamt** — Gewerbeanmeldung; ELSTER-Fragebogen; Steuernummer beantragen.
4. **USt-Voranmeldung einrichten** — monatlich oder quartalsweise; ELSTER-Zertifikat besorgen.
5. **Sozialversicherung** — bei Mitarbeitern: SV-Anmeldung Krankenkasse; Lohnbuchhaltung starten.
6. **Transparenzregister** — wirtschaftlich Berechtigte melden.
7. **D&O-Versicherung** — Versicherungsschutz vor erstem Außenauftritt prüfen.
8. **Liquiditätsmonitoring einrichten** — monatlicher Liquiditätsstatus; Krisenampel (§§ 17-19 InsO).
9. **Erstes GF-Meeting / Protokoll** — Board-Beschlüsse dokumentieren; Haftungsschutz durch Business Judgment Rule.
10. **Jahresabschluss planen** — Steuerberater beauftragen; Frist im Kalender eintragen.

## Output-Template 100-Tage-Checkliste GF

**Adressat:** Geschäftsführer / Mandant — Tonfall anleitend-strukturiert
```
100-TAGE-GF-CHECKLISTE
Gesellschaft: [Firmenname] GmbH / UG
GF-Name: [Name]
HR-Eintragung am: [Datum]
Checkliste erstellt: [Datum]

WOCHE 1
[ ] Buchführungssystem einrichten (DATEV / sevDesk / Lexware)
[ ] Steuerberater beauftragen
[ ] Geschäftskonto eröffnen / Stammkapital einzahlen
[ ] Gewerbeanmeldung beim Gewerbeamt [ORT]
[ ] Berufsgenossenschaft anmelden
[ ] Transparenzregister-Meldung

MONAT 1
[ ] ELSTER-Fragebogen zur steuerlichen Erfassung einreichen
[ ] USt-Voranmeldungs-Turnus klären (monatlich / quartalsweise)
[ ] Bei Mitarbeitern: SV-Anmeldung; Lohnbuchhaltung einrichten
[ ] D&O-Versicherung prüfen und abschließen
[ ] Erste Liquiditätsprognose erstellen

LAUFEND
[ ] USt-Voranmeldung: bis 10. des Folgemonats
[ ] Lohnsteuer-Anmeldung: bis 10. des Folgemonats (bei MA)
[ ] KSt/GewSt-Vorauszahlung: 10.3. / 10.6. / 10.9. / 10.12.
[ ] Liquiditätsstatus: monatlich
[ ] Transparenzregister-Änderungen: unverzüglich bei Strukturwechsel

JAHRESENDE
[ ] Jahresabschluss aufstellen bis [Datum + 3 Monate nach GJ]
[ ] Bundesanzeiger-Offenlegung bis [Datum + 12 Monate nach GJ]
[ ] Insolvenzlage prüfen: EK > Hälfte Stammkapital?

ESKALATIONSSCHWELLEN
[ ] EK sinkt unter Hälfte des Stammkapitals → § 49 Abs. 3 GmbHG Pflichtversammlung
[ ] Zahlungsunfähigkeit erkennbar → § 15a InsO, Frist 3 Wochen
[ ] Überschuldung erkennbar → § 15a InsO, Frist 6 Wochen
```

## Rote Schwellen

- Masseschmälernde Zahlungen nach Insolvenzreife → sofortige persönliche GF-Haftung (§ 15b InsO); Zahlung stoppen.
- Lohnsteuer nicht abgeführt → GF persönlich haftbar nach §§ 34, 69 AO.
- Jahresabschluss nicht offengelegt → Ordnungsgeldverfahren durch Bundesamt für Justiz.
- Datenschutz-Verstöße → DSGVO-Bußgeld; persönliche GF-Verantwortung.
- Berufsgenossenschaft nicht angemeldet → unversicherter Betrieb; Haftungsrisiko bei Arbeitsunfall.

## Quellen und Vertiefung

- §§ 43, 49 GmbHG (GF-Pflichten, Sorgfalt, Pflichtversammlung)
- §§ 238, 264, 325 HGB (Buchführung, Jahresabschluss, Offenlegung)
- §§ 15a, 15b InsO (Insolvenzantragspflicht, Zahlungsverbot)
- § 19 GwG (Transparenzregister)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Crezelius, GmbHG, § 43 Rn. 1-60

## Übergabe an andere Skills

- `gesellschaftsgruender-kommandocenter` — Master-Gründung
- `gesellschaftsgruender-gf-sozialversicherungs-status` — SV-Status des GF prüfen
- `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` — Pflichtversammlung bei Krise
- `gesellschaftsgruender-gewerbeanmeldung-finanzamt` — Gewerbeamt und Finanzamt-Schritte

---

## Skill: `geschaeftsfuehrervertrag`

_Geschäftsführervertrag für GmbH-Geschäftsführer aufsetzen: Verguetung, Wettbewerbsverbot, Abberufung, Kündigungsfristen. Normen: §§ 35 38 GmbHG, BGB Dienstvertrag. Prüfraster: Verguetungsstruktur, Tantieme, Freistellung, Geheimhaltung, Pensionszusage. Output: Geschäftsführervertrags-Entwurf. Abgr..._

# Geschäftsführer-Anstellungsvertrag GmbH

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Geschäftsführer-Anstellungsvertrag GmbH` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn

Klaere vor Entwurf des Anstellungsvertrags:

1. **Gesellschafter-GF oder Fremd-GF?** Gesellschafter-GF: strengere vGA-Anforderungen (Fremdvergleich); Fremd-GF: SV-Pflicht pruefen.
2. **Alleiniger GF oder Mitgeschaeftsfuehrer?** Allein: volles Geschaeft; Mitglied: Ressortverteilung, Gesamtvertretung.
3. **Sozialversicherungsstatus?** Mehrheitsgesellschafter-GF meist SV-frei; Minderheits-GF meist SV-pflichtig; Statusfeststellung (§ 7a SGB IV) beantragen?
4. **Pensionszusage gewuenscht?** Steuerlich attraktiv, aber strenge Anforderungen bei Gesellschafter-GF.
5. **Wettbewerbsverbot?** Nachvertraglich: bis 2 Jahre; Karenzentschaedigung zwingend (≥ 50 % letzter Bezuege).
6. **Befristung?** Typisch 3-5 Jahre mit Verlaengerungsoption; Kopplung Abberufung/Kuendigung beachten.

## Zentrale Normen

- **§ 6 GmbHG** — Organstellung des Geschaeftsfuehrers
- **§ 35 GmbHG** — Vertretung der Gesellschaft durch GF
- **§ 38 GmbHG** — Jederzeits-Abberufung des GF (mit Folgen für das Anstellungsverhaeltnis)
- **§ 43 GmbHG** — Haftung des GF bei Pflichtverstoessen (Fahrlassigkeit, Vorsatz)
- **§ 46 Nr. 5 GmbHG** — Bestellung des GF durch Gesellschafterbeschluss
- **§ 626 BGB** — Ausserordentliche Kuendigung aus wichtigem Grund (Dienstverhaeltnis)
- **§ 74 II HGB** — Karenzentschaedigungspflicht bei Wettbewerbsverbot (analog)
- **§ 8 Abs. 2 KStG i.V.m. § 6a EStG** — verdeckte Gewinnausschuettung (vGA); Pensionsrueckstellung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema: Anstellungsvertrag-Check

| Schritt | Pruefpunkt | Norm | Ergebnis |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 2 | SV-Status bestimmt? | § 7a SGB IV | Statusfeststellungsverfahren empfohlen |
| 3 | vGA-Fremdvergleich bei Gesellschafter-GF | § 8 Abs. 2 KStG | Angemessene Verguetung; Erdienungszeitraum Pension |
| 4 | Wettbewerbsverbot mit Karenz? | § 74 II HGB analog | Ohne Karenz: Klausel unverbindlich |
| 5 | Kuendigung und Befristung | §§ 620, 626 BGB | Sonderkuendigungsrecht für wichtige Gruende |
| 6 | Kopplung Abberufung-Kuendigung | § 38 GmbHG | Explizit im Vertrag regeln |
| 7 | D&O-Versicherung vereinbart? | § 43 GmbHG | GF-Haftungsrisiko abgedeckt? |

## Schritt-für-Schritt-Workflow

1. **Vor Notar-Termin:** Vertragsrahmen (Verguetung, Befristung, Ressort) mit Gesellschaftern abstimmen.
2. **Gesellschafterbeschluss zur Bestellung** (Paragraf 46 Nr. 5 GmbHG) formulieren — separate Beurkundung oder Teil der Gruendung.
3. **Anstellungsvertrag entwerfen:** Verguetungsstruktur, SV-Status, Wettbewerbsverbot, Pensionszusage.
4. **vGA-Check:** Bei Gesellschafter-GF: Fremdvergleich-Pruefung durch Steuerberater empfohlen.
5. **Statusfeststellung beantragen** (§ 7a SGB IV) nach Eintragung im HR.
6. **Unterzeichnung:** Gesellschaft vertreten durch alle Gesellschafter (oder bevollmächtigten Vertreter); GF als Anstellende.
7. **Lohnsteuer-Anmeldung** beim Finanzamt; Gehaltskonto einrichten.
8. **D&O-Versicherung** abschließen; Police der Gesellschaft hinterlegen.

## Output-Template: Anstellungsvertrag (Kernauszug)

**Adressat:** GmbH und Geschaeftsfuehrer — Tonfall rechtspraezise

```
GESCHAEFTSFUEHRER-ANSTELLUNGSVERTRAG

zwischen der [FIRMA] GmbH, [ADRESSE], HRB [NR.],
vertreten durch die Gesellschafterversammlung
(Beschluss vom [DATUM])
— Gesellschaft —

und Herrn / Frau [NAME], geb. [DATUM], [ADRESSE]
— Geschaeftsfuehrer / Geschaeftsfuehrerin —

§ 1 Aufgaben und Befugnisse
Der Geschaeftsfuehrer leitet die Gesellschaft als
[alleiniger / einer von mehreren] Geschaeftsfuehrer
und ist gegenueber der Gesellschafterversammlung
weisungsgebunden. Die Geschaeftsordnung der GF
ist verbindlich.

§ 2 Dauer und Beendigung
(1) Das Anstellungsverhaeltnis beginnt am [DATUM].
(2) Es ist befristet auf [DAUER] Jahre, mit
automatischer Verlaengerung um [N] Jahre, falls
nicht 6 Monate vor Ablauf gekuendigt.
(3) Die Abberufung als Organ beendet diesen Vertrag
nicht; es gilt dann die ordentliche Kuendigungsfrist.

§ 3 Verguetung
(1) Fixum: [BETRAG] EUR brutto monatlich.
(2) Tantieme: [%] des EBT nach Pruefung, faellig
[DATUM], maximal [BETRAG] EUR jaehrlich.
(3) Dienstwagen: [Klasse]; private Nutzung erlaubt,
lohnsteuerlich erfasst.

§ 4 Urlaub
28 Arbeitstage jaehrlich; Resturlaub bis [DATUM]
des Folgejahres zu nehmen.

§ 5 Wettbewerbsverbot
(1) Waehrend Vertragsdauer: kein Wettbewerb.
(2) Nachvertraglich: 12 Monate, für Branche [X]
in [GEBIET].
(3) Karenzentschaedigung: 50 % der zuletzt
monatlich bezogenen Bezuege.

§ 6 D&O-Versicherung
Die Gesellschaft schliesst für den GF eine D&O-
Versicherung mit einer Deckungssumme von mindestens
[BETRAG] EUR ab. Eigenbehaltsregelung: [X] EUR.

§ 7 Kuendigung
(1) Ordentliche Kuendigung mit 6-monatiger Frist
zum Monatsende.
(2) Ausserordentliche Kuendigung bei wichtigem
Grund (§ 626 BGB) jederzeit moeglich.
```

## Rote Schwellen

- Abberufung ohne Kuendigung: Anstellungsvertrag laeuft weiter; Gehaltsanspruch besteht bis Kuendigungsfrist
- Wettbewerbsverbot ohne Karenz: unverbindlich; GF kann sofort konkurrenzieren
- Pensionszusage ohne Fremdvergleich: vGA; Steuernachforderung bis 4 Jahre rueckwirkend
- SV-Status nicht geprueft: Nachforderung bis 4 Jahre (§ 25 SGB IV); strafrechtliche Risiken für GF

## Quellen und Vertiefung

- §§ 6, 35, 38, 43, 46 GmbHG; §§ 620, 626 BGB; § 74 II HGB analog
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Verweise Satzung zu GF-Vertrag
- `gesellschaftsgruender-gesellschaftervereinbarung` — Vesting/Leaver-Klauseln koordinieren
- `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` — Pflichten nach Eintragung
- `gesellschaftsgruender-gf-sozialversicherungs-status` — SV-Statusfeststellung vertiefen

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

