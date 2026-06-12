# Megaprompt: umweltrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `umweltrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Umweltrecht: ordnet Rolle (Vorhabenträger, Behörde, Umweltverband), markiert Frist (Kla…
2. **umweltrecht-erstpruefung-und-mandatsziel** — Umweltrecht: Erstprüfung, Rollenklärung und Mandatsziel im Umweltrecht.
3. **abfall-circular-economy** — Unternehmen oder Anlagenbetreiber hat Abfall-Frage: Abfalleigenschaft Entsorgungspflichten Nebenprodukt-Einstufung Ende …
4. **bussgeld-emissionshandel-tehg-uwr** — Unternehmen erhaelt Anhörung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWi…
5. **compliance-schulung** — Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfa…
6. **emissionshandel-tehg** — Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 2…
7. **immissionsschutz-bimschg** — Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG…
8. **kommandocenter** — Umweltmandat-Einstieg: Intake Anlagenkarte Behördenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG Kr…
9. **lksg-csddd-lieferkettensorgfalt** — Unternehmen ab 1000 Mitarbeitern muss Lieferketten-Sorgfaltspflichten nach LkSG und kuenftig CSDDD erfuellen. LkSG seit …
10. **naturschutz-artenschutz** — Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artens…
11. **start-chronologie-fristen** — Einstieg, Schnelltriage und Fallrouting im Umweltrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsc…
12. **stoerfall-anlagen-transaktionen-dd** — Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 1…
13. **transaktionen-dd** — M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturs…
14. **umweltinformation-uig-ifg** — Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 …
15. **verfahren** — Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhörung Widerspruch Eil- und Klageverfahren. Normen VwG…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Umweltrecht: ordnet Rolle (Vorhabenträger, Behörde, Umweltverband), markiert Frist (Klagefrist UVPG), wählt Norm (BImSchG, BNatSchG, WHG, BBodSchG, UVPG) und Zuständigkeit (Umweltbehörden Länder), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Umweltrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abfall-anlagen-bimschg` — Abfall Anlagen Bimschg
- `abfall-circular-economy` — Abfall Circular Economy
- `anlagen-abschlussprodukt-und-uebergabe` — Anlagen Abschlussprodukt und Uebergabe
- `bimschg-tatbestand-beweis-und-belege` — Bimschg Tatbestand Beweis und Belege
- `boden-csddd-csrd-sonderfall` — Boden Csddd CSRD Sonderfall
- `bussgeld-emissionshandel-tehg-uwr` — Bussgeld Emissionshandel Tehg UWR
- `bussgeld-quellenkarte` — Bussgeld Quellenkarte
- `compliance-schulung` — Compliance Schulung
- `csddd-mandantenkommunikation-entscheidungsvorlage` — Csddd Mandantenkommunikation Entscheidungsvorlage
- `csrd-sonderfall-und-edge-case` — CSRD Sonderfall und Edge Case
- `diligence-greenwashing-beweislast-klimaklagen` — Diligence Greenwashing Beweislast Klimaklagen
- `emissionshandel-tehg` — Emissionshandel Tehg
- `esg-greenwashing-klimaklagen-verbandsklage` — ESG Greenwashing Klimaklagen Verbandsklage
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Umweltrecht sind BImSchG, ESG, LkSG, TEHG, UIG, UmwRG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `umweltrecht-erstpruefung-und-mandatsziel`

_Umweltrecht: Erstprüfung, Rollenklärung und Mandatsziel im Umweltrecht._

# Umweltrecht: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Umweltrecht Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Umweltrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 12 Abs. 1 GG` — Berufswahl- und Ausbildungsbezug.
- `Art. 3 Abs. 1 GG` — Gleichbehandlung und Bewertungsfairness.
- `§ 2 HRG` — Aufgaben der Hochschulen.
- `§ 4 HRG` — Freiheit von Forschung, Lehre und Studium.
- `§ 7 HRG` — Ziel des Studiums.
- `§ 15 HRG` — Pruefungen und Leistungspunktsystem.
- `§ 16 HRG` — Pruefungsordnungen.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 123 Abs. 1 VwGO` — Eilrechtsschutz bei Studien-/Pruefungsentscheidungen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Umweltrecht: Erstprüfung, Rollenklärung und Mandatsziel
- **Konkreter Gegenstand:** Umweltrecht: Erstprüfung, Rollenklärung und Mandatsziel.
- **Normen-/Verfahrensanker:** BImSchG/UVPG/WHG/KrWG/BNatSchG/TEHG/UmwRG/UIG sowie Landesrecht und Behördenvollzug.
- **Entscheidende Weiche:** Genehmigung, Nebenbestimmung, Drittschutz, Verbandsklage, Mess-/Gutachtengrundlage, Sanierungsanordnung, Bußgeld und Sofortvollzug getrennt prüfen.
- **Arbeitsprodukt:** Erstelle eine fallbezogene Matrix `Behauptung / Norm / Beleg / Risiko / Gegenargument / nächster Schritt`; keine bloße Wiederholung des allgemeinen Plugin-Workflows.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Umweltrecht** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `abfall-circular-economy`

_Unternehmen oder Anlagenbetreiber hat Abfall-Frage: Abfalleigenschaft Entsorgungspflichten Nebenprodukt-Einstufung Ende der Abfalleigenschaft. Normen KrWG §§ 3 4 5 7 14 17 EU-Abfallrahmenrichtlinie 2008/98/EG LAGA. Prüfraster Abfalleigenschaftsprüfung Entsorgungsnachweis Kreislaufwirtschafts-Anfo..._

# Abfallrecht und Circular Economy

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere zuerst

1. Ist der Stoff Abfall (§ 3 Abs. 1 KrWG) oder liegt ein Nebenprodukt (§ 4 KrWG) oder Ende der Abfalleigenschaft (§ 5 KrWG) vor?
2. Wer ist Abfallerzeuger / -besitzer? Liegt gewerbliche Sammlung (§ 17 Abs. 2 Nr. 4 KrWG) vor?
3. Welche Entsorgungsanlage soll genutzt werden — genehmigt oder nicht?
4. Besteht Ueberlassungspflicht an oeffentlich-rechtliche Entsorgungstraeger (§ 17 Abs. 1 KrWG)?
5. Welche Nachweispflichten (§§ 49 ff. KrWG, NachwV) sind einzuhalten?
6. Gibt es Transporte — nationale Grenze? (EG-AbfVerbrV, Basler Uebereinkommen)

## Zentrale Normen und Paragrafenkette

- **§ 3 KrWG** — Abfallbegriff (Entledigung, Entledigungswille, Entledigungspflicht)
- **§ 4 KrWG** — Nebenprodukt (sichere weitere Verwendung, Nachfrage, unmittelbare Nutzung)
- **§ 5 KrWG** — Ende der Abfalleigenschaft (Aufbereitungsverfahren, Guetestandard, kein schutzloser Stoff)
- **§ 7 KrWG** — Grundpflichten der Kreislaufwirtschaft (Vermeidung > Verwertung > Beseitigung)
- **§ 14 KrWG** — Verpflichtung zur Getrenntsammlung
- **§ 17 KrWG** — Ueberlassungspflichten Haushaltsabfaelle / gewerbliche Abfaelle
- **§ 49 KrWG i.V.m. NachwV** — Nachweispflichten gefaehrliche Abfaelle
- **§ 62 KrWG** — Anordnungsrecht der Behörde
- **Art. 6 Richtlinie 2008/98/EG** — Ende der Abfalleigenschaft EU-Recht

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Stoff-Klassifikation**: Ist Stoff Abfall, Nebenprodukt oder nicht-Abfall nach §§ 3-5 KrWG + Europaeischem Abfallverzeichnis (AVV)?
2. **Entsorgungsweg bestimmen**: Verwertung (§ 8 KrWG — energetisch, werkstofflich, biologisch) oder Beseitigung (§ 15 KrWG)?
3. **Genehmigung pruefen**: Entsorgungsanlage §§ 4 ff. BImSchG, Planfeststellung (Deponie §§ 35 ff. KrWG)?
4. **Nachweise**: Gefaehrliche Abfaelle — Begleitschein/Entsorgernachweis (NachwV); elektronisches Nachweisverfahren.
5. **Ueberlassungspflicht**: § 17 KrWG — Ausnahmen für Eigenkompostierung, gemeinnuetzige Sammlung, gewerbliche Drittbeauftragung.
6. **Grenzueberschreitend**: EG-AbfVerbrV Nr. 1013/2006 — Notifizierungspflicht bei gruenen / orangenen / roten Listen; Basel-Genehmigung bei gefaehrlichen Abfaellen in Drittstaaten.
7. **Circular-Economy**: EU-Kreislaufwirtschaftspaket — Oekodesign-VO 2024/1781, EU End-of-Waste-Kriterien-VO (Stahl, Kupfer, Papier); CSRD-Berichtspflicht.

### Entscheidungsbaum Abfalleigenschaft

```
Entledigt sich der Erzeuger des Stoffes?
 JA → Ist Entsorgung sicher und Verwendung nachgefragt?
 JA → Nebenprodukt § 4 KrWG pruefen
 NEIN → Abfall → Entsorgungspflicht § 7 KrWG
 NEIN → Verwendung weiterhin beabsichtigt → kein Abfall
```

## Output-Template: Begleitschreiben Behördenanfrage Nebenprodukt

**Adressat:** Zustaendige Abfallbehoerde — Tonfall: sachlich-juristisch

```
An die [BEHOERDE] — Abteilung Abfallrecht

Antrag auf Bestaetigung Nebenprodukt-Status gemaess § 4 KrWG

Absender: [NAME MANDANT], [ADRESSE]
Betr.: Stoff [BEZEICHNUNG], Anfall [MENGE] t/a, Anlage [ORT]

I. Sachverhalt
Bei der Produktion von [PRODUKT] faellt als Koppelprodukt [STOFF] an.
Dieser wird unmittelbar an [ABNEHMER] veraeussert und dort als
[ZWECK] verwendet.

II. Voraussetzungen § 4 KrWG
1. Sichere weitere Verwendung: Langfristiger Liefervertrag mit [ABNEHMER] liegt bei (Anlage).
2. Kein Aufbereitungserfordernis: [STOFF] entspricht ohne weitere Behandlung der Norm [ISO/DIN].
3. Nachfrage: Jaehrlicher Bezug seit [JAHR], Marktpreis [BETRAG] EUR/t.
4. Keine schutzlosen Stoffe: TDS/SDS-Datenblatt liegt bei (Anlage).

III. Antrag
Wir bitten um Bestaetigung, dass [STOFF] ein Nebenprodukt i.S.d. § 4 KrWG darstellt
und keiner Entsorgungsnachweis-Pflicht unterliegt.

Anlagen: Liefervertrag, SDS-Datenblatt, Laboranalyse
```

## Vertiefung: Circular Economy Anforderungen

- **EU-Oekodesign-Verordnung 2024/1781**: Produktanforderungen Haltbarkeit, Reparierbarkeit, Rezyklierbarkeit; ab 2026 schrittweise Sektoren.
- **CSRD/ESRS E5**: Berichtspflicht zu Ressourcennutzung, Kreislaufwirtschaft, Abfallmengen.
- **End-of-Waste-Kriterien** (EU-Verordnungen zu Stahl, Aluminium, Kupfer, Papier, Glas, Reifen): automatisches Ende der Abfalleigenschaft bei Erreichung der Qualitaetsschwellen.
- **EU-Verpackungsverordnung 2025** (PPWR): Mindest-Recyclatanteile, Sammelquoten, Einwegverbot.

## Anschluss-Skills

- `umweltrecht-verfahren` — Klageverfahren gegen Abfallbescheid
- `umweltrecht-transaktionen-dd` — Abfallrisiken in M&A
- `esg-greenwashing-csrd` — CSRD-Berichtspflicht Kreislaufwirtschaft
- `umweltrecht-wasser-bodenschutz` — Altlasten bei Deponien

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 BImSchG
- § 70 VwG
- § 10 BImSchG
- § 2 UmwRG
- § 24 BBodSchG
- § 74 VwG
- § 4 BBodSchG
- § 34 BNatSchG
- § 17 BImSchG
- § 47 VwG
- § 44 BNatSchG
- § 4 KrWG

### Leitentscheidungen

- EuGH C-243/15
- BGH I ZR 98/23
- BGH I ZR 142/23

---

## Skill: `bussgeld-emissionshandel-tehg-uwr`

_Unternehmen erhaelt Anhörung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR. Prüfraster Tatbestandsprüfung Verjährung Verwertungsverbote Verteidigungsargume..._

# Bussgeld, Sanktionen und Anhörung im Umweltrecht

## Arbeitsbereich

Unternehmen erhaelt Anhörung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR. Prüfraster Tatbestandsprüfung Verjährung Verwertungsverbote Verteidigungsargumente. Output Verteidigungsschrift Widerspruch Akteneinsicht-Antrag. Abgrenzung zu umweltrecht-verfahren (Verwaltungsklage) und umweltrecht-immissionsschutz-bimschg (Genehmigung). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere vor Reaktion auf Anhörung

1. Welches Umweltgesetz ist Grundlage (BImSchG § 62, KrWG § 69, WHG § 103, BNatSchG § 69)?
2. Welcher Vorwurf genau — vorsaetzlich oder fahrlassig (OWiG § 10)?
3. Welche Behörde fuehrt das Verfahren (Gewerbeaufsicht, Umweltbehoerde, Staatsanwaltschaft)?
4. Wurde bereits Akteneinsicht beantragt (§ 49 OWiG)?
5. Ist der Mandant die juristische oder die natuerliche Person (GF-Haftung §§ 9, 30 OWiG)?
6. Bestehen Verjaehjrungsfristen (§ 31 OWiG: 3 Jahre bei Bussgeld bis 100.000 EUR)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 62 BImSchG** — Bussgeldbewehrte Pflichtverletzungen Betreiber (Betrieb ohne Genehmigung, Verstoss Nebenbestimmungen)
- **§ 64 BImSchG** — Strafbewehrte Verstoesze (Schadstoffe in der Luft wissentlich)
- **§ 69 KrWG** — Ordnungswidrigkeiten (illegale Entsorgung, Nachweispflichtverletzung)
- **§ 70 KrWG** — Straftatbestaende Abfallrecht (§ 326 StGB Verweis)
- **§ 103 WHG** — Ordnungswidrigkeiten Wasserrecht
- **§ 69 BNatSchG** — Ordnungswidrigkeiten Naturschutz
- **§ 55 OWiG** — Anhörungsrecht Betroffener
- **§ 67 OWiG** — Einspruch gegen Bussgeld-Bescheid (2 Wochen)
- **§ 68 OWiG** — Hauptverhandlung beim Amtsgericht
- **§ 30 OWiG** — Verbandsgeldbuse gegen jur. Person
- **§ 31 OWiG** — Verjaeahrung (3 Jahre bei max. Bussgeld > 1.000 EUR)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Anhörungsschreiben analysieren**: Vorwurf, Norm, Tatzeit, Beweismittel, gesetzte Frist.
2. **Akteneinsicht beantragen** (§ 49 OWiG): Vollstaendige Akte — Messberichte, Kontrolle-Protokolle, Zeugenaussagen.
3. **Schuld pruefen**: Vorsatz / Fahrlassigkeit, Zurechnung auf Mandant, Delegationskette.
4. **Verjaeahrung pruefen**: § 31 OWiG; Unterbrechung durch Anhörung (§ 33 OWiG).
5. **Verteidigungsschrift einreichen**: Tatsachen und Recht; Antrag auf Einstellung oder Bussgeld-Reduzierung.
6. **Einspruch bei Bescheid**: § 67 OWiG — 2 Wochen-Frist ab Bekanntgabe; Einspruch hemmt Rechtskraft.
7. **Amtsgericht**: Hauptverhandlung § 68 OWiG — Zeugenbefragung, Sachverstaendige; Strafverfahren § 70 KrWG / § 326 StGB separat.

### Entscheidungsbaum nach Anhörungsschreiben

```
Anhörungsschreiben erhalten
 → Frist noch offen?
 JA → Akteneinsicht sofort beantragen
 → Schuld-Pruefung: War Pflichtverletzung schuldhaft?
 JA → Minderungsgruende? → Verteidigungsschrift mit Minderungsargumentation
 NEIN → Einstellungsantrag wegen fehlendem Vorsatz/Fahrlassigkeit
 NEIN → Einspruch (§ 67 OWiG, 2 Wochen ab Bescheid)
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Einlassung im Umwelt-Bussgeldbescheid-Anhörungsverfahren | Einlassung nach Schema; Template unten |
| Variante A — Behörde will Besprechung vor Bescheid | Vorgespräch annehmen; Einlassung dann muendlich |
| Variante B — Mandant will Bussgeldbescheid akzeptieren | Keine Einlassung noetig; Bussgeldbescheid abwarten |
| Variante C — Strafrecht parallel ermittelt | Strafverteidigung-Skill parallel; vorsichtige Einlassung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template: Einlassung im Anhörungsverfahren

**Adressat:** Zustaendige Behörde — Tonfall: sachlich-juristisch

```
An die [BEHOERDE]

Stellungnahme im Anhörungsverfahren gemaess § 55 OWiG

Betroffene/r: [NAME MANDANT], [ADRESSE]
Ihr Zeichen: [AZ BEHOERDE]
Vorwurf: [KURZBESCHREIBUNG]

I. Wir zeigen die anwaltliche Vertretung von [MANDANT] an.
 Akteneinsicht beantragen wir hiermit ausdruecklich gemaess § 49 OWiG.
 Wir bitten um Verlaengerung der Stellungnahme-Frist bis [DATUM].

II. Sachverhalt
[MANDANT] ist Betreiber der Anlage [NAME] in [ORT].
[Objektiver Sachverhalt aus Mandantensicht].

III. Rechtliche Einlassung
a) Tatbestand: § [X] [Gesetz] ist nicht erfuellt, weil [Argumentation].
b) Schuld: Ein schuldhaftes Handeln liegt nicht vor. [MANDANT] hat alle
 zumutbaren Vorkehrungen getroffen (Nachweise Anlage [X]).
c) Verjaeahrung: Die Tat soll sich am [DATUM] ereignet haben. Gemaess
 § 31 OWiG verjaeahrte die Ordnungswidrigkeit am [DATUM].

IV. Antrag
Wir beantragen, das Verfahren einzustellen.

Anlagen: Betriebsprotokoll, Wartungsnachweise, Vollmacht
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Vertiefung: Verbandsbussgeld § 30 OWiG

- Behörde kann gegen jur. Person Bussgeld festsetzen, wenn GF/Organ Pflicht verletzt.
- Bussgeld bis 10 Mio. EUR (§ 30 Abs. 2 OWiG) bei Vorsatz; bei Fahrlassigkeit Haelfte.
- Selbststaendiges Verfahren gegen jur. Person neben Verfahren gegen natuerliche Person moeglich.
- Verteidigung: Mangelnde Zurechnung der Handlung, fehlende Aufsichtspflichtverletzung § 130 OWiG.

## Fristen im Ueberblick

| Verfahrensschritt | Frist | Grundlage |
|---|---|---|
| Einspruch gegen Bussgeld-Bescheid | 2 Wochen ab Bekanntgabe | § 67 Abs. 1 OWiG |
| Akteneinsicht-Antrag | Unverzueglich nach Anhörung | § 49 OWiG |
| Verjaeahrung OWi (Bussgeld > 1000 EUR) | 3 Jahre | § 31 Abs. 2 Nr. 1 OWiG |
| Strafverfolgungsverjaehrung (§ 326 StGB) | 5 Jahre | § 78 Abs. 3 Nr. 4 StGB |

## Anschluss-Skills

- `umweltrecht-verfahren` — Gerichtsverfahren nach Einspruch
- `umweltrecht-immissionsschutz-bimschg` — Nachtraegliche Auflagen als Busjgeld-Alternative
- `umweltrecht-kommandocenter` — Intake und Mandats-Triage

---

## Skill: `compliance-schulung`

_Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfallverantwortliche. Normen BImSchG §§ 53-58 KrWG §§ 59 60 WHG §§ 64 65. Prüfraster Schulungspflichten Dokumentationspflichten Audit-Planung. Output Schulungsplan-Template Jahresa..._

# Compliance, Beauftragte und Schulung im Umweltrecht

## Arbeitsbereich

Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfallverantwortliche. Normen BImSchG §§ 53-58 KrWG §§ 59 60 WHG §§ 64 65. Prüfraster Schulungspflichten Dokumentationspflichten Audit-Planung. Output Schulungsplan-Template Jahresaudit-Checkliste. Abgrenzung zu umweltrecht-immissionsschutz-bimschg (Genehmigung) und umweltrecht-abfall-circular-economy (Abfall-Compliance). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere Schulungs-/Audit-Kontext

1. Welche Beauftragte sind nach Gesetz zu bestellen (ImmSchBeauftragter, Abfallbeauftragter, Gewaesserschutzbeauftragter)?
2. Besteht bereits ein Compliance-Management-System oder steht erstmalige Einrichtung an?
3. Wurde ein behordliches Audit oder eine Ueberwachung angekuendigt?
4. Wie gross ist das Unternehmen — Anzahl Anlagen, Produktionsstaetten, Mitarbeiter?
5. Welche Schulungsthemen sind akut (TEHG, KrWG-Novelle, BImSchG-Aenderung, CSRD)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 53 BImSchG** — Bestellung Immissionsschutzbeauftragter (Pflicht bei Anlagen der 4. BImSchV, § 1 5. BImSchV)
- **§ 54 BImSchG** — Aufgaben des ISB (Unterrichtung Betreiber, Ueberpruefung Betrieb, Stellungnahme Genehmigungsaenderung)
- **§ 55 BImSchG** — Pflichten des Betreibers gegenueber ISB (Unterrichtungs-, Ausstattungspflicht)
- **§ 58 BImSchG** — Haftungsfreistellung ISB
- **§ 59 KrWG** — Bestellung Abfallbeauftragter (Pflicht § 1 AbfBeauftrV)
- **§ 64 WHG** — Bestellung Gewaesserschutzbeauftragter (Pflicht bei Einleitungen)
- **§ 130 OWiG** — Ordnungswidrigkeitshaftung bei mangelnder Aufsicht (Leitungsperson)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Beauftragten-Bestellung pruefen

1. **ISB-Pflicht**: § 53 BImSchG i.V.m. § 1 5. BImSchV — Anlage nach Anlage 1 Nr. 1-10 der 5. BImSchV; Genehmigung nach § 4 BImSchG.
2. **ABfallbeauftragter**: § 59 KrWG i.V.m. § 1 AbfBeauftrV — Anlagen mit bestimmten Abfallmengen oder Betreiber von Entsorgungsanlagen.
3. **Gewaesserschutzbeauftragter**: § 64 WHG — Direkteinleiter in Gewaesser.
4. **Bestellung formal**: Schriftlich, Mitteilung an Behörde, Fachkunde-Nachweise; interne Richtlinie.
5. **Freistellung OWiG**: § 130 OWiG — ohne funktionierende Compliance droht Verbandsbussgeld.

### B) Schulungsplan erstellen

1. **Bedarfsanalyse**: Welche Rechtsgebiete betreffen Anlagen (BImSchG, KrWG, WHG, TEHG, BNatSchG)?
2. **Jede Zielgruppe definieren**: Geschaeftsfuehrung (Haftung), ISB/Abfallbeauftragter (Fachkunde), Mitarbeiter (Praxis).
3. **Schulungsplan**: Jährliche Pflichtschulung je Beauftragtenrolle; Ad-hoc-Schulung bei Gesetzesaenderung.
4. **Dokumentation**: Teilnahmelisten, Schulungsunterlagen, Teilnehmerzertifikate (Pflicht für Fachkunde-Erhalt).
5. **Audit-Vorbereitung**: Interne Revision vor behordlichem Audit; Mangelbeseitigung.

### C) Jahres-Audit-Checkliste (Kurzform)

| Pruefpunkt | Erfuellt? | Quelle | Bemerkung |
|---|---|---|---|
| ISB bestellt und fachkundig | JA/NEIN | § 53 BImSchG | Letzte Schulung: [DATUM] |
| Abfallbeauftragter bestellt | JA/NEIN | § 59 KrWG | Letzte Schulung: [DATUM] |
| Genehmigungen aktuell | JA/NEIN | § 4 BImSchG | Naechste Pruefung: [DATUM] |
| TEHG-Abgabe geleistet | JA/NEIN | § 8 TEHG | Letzte Abgabe: [DATUM] |
| Abfallnachweise vollstaendig | JA/NEIN | NachwV | Letzter Bericht: [DATUM] |
| Emissionsberichte aktuell | JA/NEIN | § 5 TEHG | Letzter Bericht: [DATUM] |
| Gewaesserschutz-Audit | JA/NEIN | § 64 WHG | Letzter Audit: [DATUM] |
| Unterweisung Mitarbeiter | JA/NEIN | § 130 OWiG | Protokoll: [DATUM] |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Umwelt-Compliance-Schulungsplan erstellen | Schulungsplan nach Schema; Template unten |
| Variante A — Schulung nur für Fuehrungskraefte nicht alle Mitarbeiter | Fuehrungsebenen-Schulung; vereinfachter Plan |
| Variante B — Schulung als Reaktion auf Behörden-Auflage | Auflagerungs-konforme Schulung; Nachweis-Dokumentation betonen |
| Variante C — Online-Schulung statt Praesenzseminar | Online-Variante des Plans; E-Learning-Formate einbinden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template: Schulungsplan Umwelt-Compliance

**Adressat:** Internes Compliance-Management / Fuehrung — Tonfall: strukturiert, praxisorientiert

```
JAHRESSCHULUNGSPLAN UMWELT-COMPLIANCE [JAHR]
[UNTERNEHMEN], [ORT]

1. PFLICHTSCHULUNGEN FUeR BEAUFTRAGTe

Modul A: Immissionsschutzbeauftragter (ISB)
Zielgruppe: [NAME ISB], Stellvertreter [NAME]
Datum: [DATUM], [ORT/VIDEO]
Themen: BImSchG §§ 53-58, aktuelle BVerwG-Entscheidungen,
 TA-Luft/TA-Laerm-Novellen [JAHR], Meldepflichten.
Dauer: 4 h (inkl. Uebungsfall)
Dokumentation: Teilnahme-Bestaetigung, Update Fachkundenachweise

Modul B: Abfallbeauftragter
Zielgruppe: [NAME], [NAME]
Datum: [DATUM]
Themen: KrWG-Aenderungen, Nachweisverfahren elektronisch, AVV-Aktualisierung.
Dauer: 3 h

Modul C: Gewaesserschutzbeauftragter
Zielgruppe: [NAME]
Datum: [DATUM]
Themen: WHG-Erlaubnisse, WRRL-Verpflichtungen, Emissionsgrenzen AbwV.
Dauer: 2 h

2. ALLGEMEINE MITARBEITER-UNTERWEISUNG

Zielgruppe: Alle Mitarbeiter mit Umweltbezug (Produktion, Logistik, Lager)
Datum: [DATUM]
Themen: Abfalltrennung, Gefahrstoff-Lagerung, Stoerfall-Meldung, Ansprechpersonen.
Dauer: 1 h + Quiz
Protokoll-Pflicht: § 130 OWiG-Dokumentation

3. AD-HOC SCHULUNGEN

Trigger: Neue Gesetzgebung (z.B. KrWG-Novelle, TEHG-Aenderung), Bussgeld-Bescheid,
 Behörden-Audit-Ankuendigung.
Verantwortlich: [NAME COMPLIANCE-OFFICER]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Vertiefung: CSRD-Berichtspflicht Umwelt-Compliance

- CSRD-Unternehmen (ab 250 MA oder Boersennotierung) muessen Compliance-Systeme im Nachhaltigkeitsbericht (ESRS) offenlegen.
- ESRS E1 (Klimawandel), E2 (Umweltverschmutzung): Angaben zu Compliance-Massnahmen, Zielen, Messzahlen.
- Audit durch Wirtschaftspruefer (Reasonable Assurance ab 2028, Limited Assurance ab 2024).

## Anschluss-Skills

- `esg-greenwashing-csrd` — CSRD-Berichtspflicht Umwelt
- `umweltrecht-bussgeld-sanktionen` — Reaktion auf Audit-Beanstandung
- `umweltrecht-immissionsschutz-bimschg` — ISB-Pflichten im BImSchG-Kontext

---

## Skill: `emissionshandel-tehg`

_Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster Zuteilungs-Berechnung Monitoring-Pflichten Abgabe-Frist DEHSt-Anordnung. Output Zuteilun..._

# Emissionshandel und TEHG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere zuerst

1. Welcher EU-ETS-Handelszeitraum (Phase 4: 2021-2030)?
2. Ist die Anlage TEHG-pflichtig (§ 2 TEHG i.V.m. Anlage 1 TEHG)?
3. Kostenlose Zuteilung oder Auktion — Grundlage ZuV 2020?
4. Monitoring-Plan DEHSt genehmigt?
5. Abgabe-Frist 30. April eingehalten?
6. Welche Art von Streit — Zuteilungsbescheid, Monitoring-Anordnung, Bussgeld?

## Zentrale Normen und Paragrafenkette

- **§ 2 TEHG i.V.m. Anlage 1** — Anwendungsbereich; Taetigkeitsliste (Energieumwandlung, Industrie, Luftverkehr)
- **§ 4 TEHG** — Genehmigungspflicht Anlagenbetreiber
- **§ 5 TEHG** — Monitoring-Pflicht (akkreditierter Pruefstelle)
- **§ 7 TEHG** — Jaehrliche Berichtspflicht (verifizierter Emissionsbericht)
- **§ 8 TEHG** — Abgabepflicht 30. April (Anzahl Berechtigungen entspricht verifizierten Emissionen)
- **§ 9 TEHG** — Kostenlose Zuteilung (ZuV 2020, Produktbenchmarks)
- **§ 26 TEHG** — Sanktion 100 EUR/t CO2 bei Abgaberueckstand; keine Befreiung durch Zahlung
- **ZuV 2020** — Zuteilungsverordnung 2020 — Benchmarks, Benchmark-Kurven, Cross-Sektoral-Correction-Faktor (CSCF)
- **BEHG** — Brennstoffemissionshandelsgesetz (nationaler ETS); § 10 BEHG Berichts- und Abgabepflicht

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **TEHG-Pflicht pruefen**: Anlage 1 TEHG — Taetigkeitskategorie, Schwellenwert (z.B. Feuerungsanlage > 20 MW thermisch).
2. **Genehmigungs-/Monitoring-Antrag**: § 4 TEHG-Genehmigung + Monitoring-Plan gemaess MVO/DEHSt.
3. **Zuteilungsantrag** (Phase 4: bis 31.05.2019 gestellt; laufende Anpassung bei Kapazitaetsaenderung): ZuV 2020-Benchmarks bestimmen; Baseline-Daten (2014-2018) einreichen.
4. **Jaehrliches Monitoring**: Emissionen messen/berechnen, von akkreditiertem Pruefstelle verifizieren lassen.
5. **Emissionsbericht 31. Maerz**: DEHSt-Einreichung.
6. **Abgabe 30. April**: Berechtigungen (EUAs) im EUTL-Konto abbuchen; fehlende Berechtigungen zukaufen (Spot oder Forward).
7. **Bei Zuteilungsbescheid-Angriff**: Widerspruch DEHSt, Klageverwaltungsgericht Berlin (§ 88 VwGO, auschliessliche Zuständigkeit VG Berlin).

### Entscheidungsbaum Abgabe-Ruckstand

```
Abgabe-Frist 30.04. versaeumt?
 JA → § 26 TEHG: Sanktion 100 EUR/t CO2 Rueckstand
 → Sofort fehlende EUAs kaufen (Markt oder Broker)
 → Abgabe nachholen
 → Sanktions-Bescheid DEHSt anfechten? → Nur Verjaeahrung oder Fehler Feststellungsbescheid pruefbar
 NEIN → Alles korrekt → Dokumentation sichern
```

## Output-Template: Widerspruch Zuteilungsbescheid

**Adressat:** DEHSt — Tonfall: sachlich-juristisch

```
An die Deutsche Emissionshandelsstelle (DEHSt)
Bismarckplatz 1, 14193 Berlin

Widerspruch gegen Zuteilungsbescheid

Anlagenbetreiber: [NAME MANDANT]
Anlage: [NAME], [ORT], TEHG-Genehmigung Nr. [NR.]
DEHSt-Az.: [AZ.]

I. Hiermit legen wir namens und in Vollmacht des Anlagenbetreibers
 Widerspruch gegen den Zuteilungsbescheid vom [DATUM] ein.

II. Sachverhalt
Die DEHSt hat für die Handelsperiode 2021-2030 eine kostenlose
Zuteilung von [X] EUAs/Jahr festgesetzt. Unsere Berechnung
auf Basis der ZuV 2020 und der Benchmark-Daten ergibt jedoch
[Y] EUAs/Jahr.

III. Begruendung
a) Falsche Benchmark-Anwendung: DEHSt hat Benchmark [BM-CODE]
 angewendet, richtig waere [ANDERER CODE] (vgl. ZuV 2020 Anhang 1).
b) Baseline-Daten fehlerhaft: Produktionsmenge [JAHR] betraegt
 [ZAHL] t (Nachweise Anlage), nicht [ZAHL t DEHSt].
c) CSCF-Korrektur unzulaessig hoch: Berechnung gem. Beschl. EU 2021/355.

IV. Antrag
Wir beantragen, den Zuteilungsbescheid aufzuheben und
[Y] EUAs/Jahr zuzuteilen.

Anlagen: Produktionsdaten, Pruefstellen-Bericht, Benchmark-Berechnung
```

## Vertiefung: BEHG Nationaler Emissionshandel

- Gilt für Brennstofflieferanten (Waerme, Verkehr, Gebaeude, Kleingewerbe nicht unter EU-ETS).
- Festpreis-Phase bis 2025: 25 EUR/t CO2 (2021), schrittweise auf 55 EUR/t (2025).
- Ab 2026: Mengenhandel im Preiskorridor 55-65 EUR/t.
- Abgabe-Pflicht: Berechtigungszertifikate (nEHS-Zertifikate) bis 31. Juli des Folgejahres.
- DEHSt für nEHS-Registerueberwachung zuständig.

## Fristen-Ueberblick

| Schritt | Frist | Grundlage |
|---|---|---|
| Zuteilungsantrag Phase 4 (laufend) | Bei Neuanlage: 12 Monate vor Betrieb | ZuV 2020 § 4 |
| Emissionsbericht einreichen | 31. Maerz Folgejahr | § 7 TEHG |
| Abgabe Emissionsberechtigungen | 30. April Folgejahr | § 8 TEHG |
| Widerspruch Zuteilungsbescheid | 1 Monat | § 70 VwGO |
| Klage VG Berlin | 1 Monat nach Widerspruchsbescheid | § 74 VwGO |

## Anschluss-Skills

- `umweltrecht-verfahren` — Klageverfahren VG Berlin
- `esg-greenwashing-csrd` — CSRD-Berichtspflicht ETS-Kosten
- `energierecht-industriekunden` — Befreiung BES-Regelung CO2-Kompensation
- `umweltrecht-kommandocenter` — Mandat-Intake

---

## Skill: `immissionsschutz-bimschg`

_Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot. Prüfraster Genehmigungspflicht UVP-Pflicht Drittschutz Nachbarklage Verbandskl..._

# Immissionsschutz und BImSchG

## Arbeitsbereich

Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot. Prüfraster Genehmigungspflicht UVP-Pflicht Drittschutz Nachbarklage Verbandsklage UmwRG. Output Genehmigungsantrag-Struktur Schriftsatz OVG. Abgrenzung zu umweltrecht-naturschutz-artenschutz (Naturschutz) und umweltrecht-stoerfall-anlagen (Stoerfall). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere vor Verfahrens-Einstieg

1. Welche Anlage (Typ, installierte Leistung, Emissionspotenzial) — Spalte 1 oder 2 der 4. BImSchV?
2. Formelles (§ 10 BImSchG, mit Oeffentlichkeitsbeteiligung) oder vereinfachtes Verfahren (§ 19 BImSchG)?
3. Ist eine UVP-Pflicht gemaess UVPG-Anlage 1 ausgeloest?
4. Wer ist Mandant — Betreiber/Investor oder klagender Dritter (Nachbar, Umweltverband)?
5. Liegt ein Ausgangsbescheid vor oder steht Antrag am Anfang?
6. Welche Fristen laufen (Widerspruch § 70 VwGO, Klage § 74 VwGO je 1 Monat)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 4 BImSchG** — Genehmigungspflicht für Anlagen der 4. BImSchV
- **§ 5 Abs. 1 Nr. 1 BImSchG** — Betreiberpflicht Schutz vor schaedlichen Umwelteinwirkungen (Drittschutz-Norm)
- **§ 5 Abs. 1 Nr. 2 BImSchG** — Vorsorge-Pflicht Emissionsminimierung
- **§ 6 BImSchG** — Genehmigungsvoraussetzungen; gebundene Entscheidung
- **§ 10 BImSchG i.V.m. 9. BImSchV** — Foermliches Verfahren mit Oeffentlichkeitsbeteiligung
- **§ 16 BImSchG** — Wesentliche Aenderung genehmigungsbeduerftiger Anlagen
- **§ 17 BImSchG** — Nachtraegliche Auflagen
- **§ 19 BImSchG** — Vereinfachtes Verfahren ohne Oeffentlichkeitsbeteiligung
- **§ 48 BImSchG i.V.m. TA Luft, TA Laerm** — Verwaltungsvorschriften als antizipierte Sachverstaendigen-Gutachten
- **§ 1 UmwRG** — Klagebefugnis anerkannter Umweltvereinigungen
- **§ 113 Abs. 1 VwGO** — Aufhebungsklage gegen Genehmigung

## Leitentscheidungen (Stand 05/2026, verifiziert bverwg.de / curia.europa.eu)

- **BVerwG 17.12.2020, 4 C 5.19**: BImSchG-Genehmigung Windkraftanlage; Anforderungen an artenschutzrechtliche Pruefung (saP). Quelle: bverwg.de.
- **BVerwG 18.07.2019, 7 C 26.17**: UVP-Vorpruefung; Aufhebung nur bei kausalen Verfahrensmaengeln. Quelle: bverwg.de.
- **BVerwG 28.11.2017, 7 A 17.12**: TA Laerm als antizipiertes Sachverstaendigengutachten — bindet Behörde nicht bei abweichenden Erkenntnissen im Einzelfall. Quelle: bverwg.de.
- **EuGH 15.10.2009, C-263/08 (Djurgården)**: Beteiligungsrechte und Aarhus-Konvention; Begriff „betroffene Oeffentlichkeit". Quelle: curia.europa.eu.
- **EuGH 16.04.2015, C-570/13 (Gruber)**: Klagebefugnis Drittbetroffener auch ohne foermliche Beteiligung am Verfahren. Quelle: curia.europa.eu.

Konkrete Aktenzeichen weiterer Entscheidungen (insb. OVG / VGH) vor Ausgabe ueber bverwg.de bzw. landesrecht-[bundesland].de verifizieren.

## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Betreiber-Perspektive: Genehmigungsantrag

1. **Anlage einordnen**: 4. BImSchV Spalte 1 oder 2, UVP-Screening nach UVPG Anlage 1.
2. **Verfahrensart bestimmen**: § 10 (foermlich) oder § 19 BImSchG (vereinfacht).
3. **Antragsunterlagen zusammenstellen**: § 4 9. BImSchV — Erlauterungsbericht, Immissionsprognosen (Schall, Staub, Luft), Lageplaeane, Betriebsbeschreibung, Sicherheitsbericht bei Stoerfallanlage.
4. **Behörde benennen**: Genehmigungsbehoerde (Landes-Immissionsschutzbeh.), beteiligte Fachbehoerden (Wasserbeh., Naturschutz, Arbeitsschutz).
5. **Oeffentlichkeitsbeteiligung**: Auslegung 1 Monat; Einwendungsfrist; Eroerterungstermin.
6. **Bescheid pruefen**: Nebenbestimmungen angreifen wenn unverhaltsnismassig (§ 12 BImSchG).
7. **Vollzug sichern**: Nebenbestimmungen erfuellen, Betrieb anzeigen, Emissionsberichte.

### B) Nachbar-/Dritter-Perspektive: Drittanfechtung

1. **Drittschutz pruefen**: § 5 Abs. 1 Nr. 1 BImSchG (Schutz vor schaedlichen Umwelteinwirkungen), TA-Laerm, TA-Luft-Richtwerte; Eigentumsverletzung benennen.
2. **Klagebefugnis**: Analogie § 42 Abs. 2 VwGO; Betroffenheit in eigenen Rechten.
3. **Frist**: 1 Monat nach Bekanntgabe Genehmigung (Widerspruch, soweit Widerspruchsverfahren erhalten, ansonsten direkt Klage VG).
4. **Eilantrag**: § 80a Abs. 3, § 80 Abs. 5 VwGO bei bereits vollziehbarer Genehmigung.
5. **Gruende**: Schallgutachten falsch (Methodik, Pegelbewertung), UVP-Fehler, fehlende Behörden-Beteiligung, Drittschutz-Verstoss.
6. **Verband**: UmwRG-Vereinigung — Verbandsklage § 2 UmwRG bei UVP-pflichtigen Vorhaben.

### Entscheidungsbaum Klage

```
Liegt ein BImSchG-Bescheid vor?
 JA → Bin ich Adressat (Betreiber)?
 JA → Nebenbestimmungsanfechtung oder Aufhebungsklage
 NEIN → Dritter (Nachbar/Verband)?
 JA → Drittschutz § 5 Abs. 1 Nr. 1? TA-Laerm-Grenzwert ueberschritten?
 JA → Anfechtungsklage VG + ggf. § 80a Eilantrag
 NEIN → Zulassungsklage aussichtsarm
 NEIN → Antragsverfahren laueft → Beteiligungsrechte wahren, Einwendungen erheben
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Widerspruch oder Klage gegen Drittanfechtung BImSchG | Klage-Schriftsatz nach Schema; Template unten |
| Variante A — Genehmigung noch nicht bestandskraeftig Einwendung moeglich | Einwendung im Verfahren zuerst; Klage erst nach Abschluss |
| Variante B — Mandant will nur bestimmte Auflagen anfechten | Teilanfechtung nur der belastenden Nebenbestimmungen |
| Variante C — Drittanfechtung Nachbar klagt gegen Genehmigung | Beiladungsantrag stellen; Verteidigung der Genehmigung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template Widerspruch/Klage Drittanfechtung

**Adressat:** Widerspruchsbehoerde / Verwaltungsgericht — Tonfall: sachlich-juristisch

```
An die [Behörde / das Verwaltungsgericht [ORT]]

Widerspruch / Klage

des/der [NAME MANDANT], [ADRESSE]
— Widersprechende/r / Klaeger/in —

gegen

Genehmigungsbescheid der [BEHOERDE] vom [DATUM], Az. [AZ.]
— zugunsten [BETREIBER] —

I. Wir erheben Widerspruch / Klage und beantragen:
1. Der Bescheid vom [DATUM] wird aufgehoben.
2. [BEHOERDE] traegt die Kosten.

II. Begruendung
Der/die Klaeger/in ist Eigentuemerinn des Grundstuecks [FLUR].
Die Genehmigung verletzt drittschuetzende Normen (§ 5 Abs. 1 Nr. 1 BImSchG):
- Schallpegel: Prognostizierter Nachtwert [X] dB(A) ueberschreitet TA-Laerm-Richtwert
 von 40 dB(A) im Reinen Wohngebiet / 45 dB(A) im Allgemeinen Wohngebiet.
- Gutachten-Maengel: [Konkrete Maengel benennen — Messpunkt, Methodik, Kumulation]
- UVP-Verfahrensfehler: [Falls UVP-pflichtig — Oeffentlichkeitsbeteiligung unterblieben]

Anlagen: Eigentumsnachweis, Schallgutachten-Gegengutachten, Lageplan
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Fristen und Verfahrenseckpunkte

| Schritt | Frist | Grundlage |
|---|---|---|
| Einwendungen im Genehmigungsverfahren | Auslegungsfrist + 2 Wochen | § 10 Abs. 3 BImSchG |
| Widerspruch | 1 Monat ab Bekanntgabe | § 70 VwGO |
| Anfechtungsklage (ohne Widerspruchsverfahren) | 1 Monat | § 74 VwGO |
| Eilantrag § 80a | Unverzueglich | § 80a VwGO |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Vertiefung: Typische Fehler und Verteidigung

- **TA-Laerm-Anwendung**: Zu optimistische Ausbreitung, fehlende Impulshaltigkeit, Tageszeit-Staffelung fehlt → Gegengutachten beauftragen.
- **Kumulation**: Andere vorhandene Anlagen als Vorbelastung nicht beruecksichtigt.
- **Praeventions-Gebot**: Nebenbestimmungen statt Ablehnung — Verhaeltnismaessigkeit pruefen.
- BVerwG 17.12.2020, 4 C 5.19 — saP-Pruefung Wind (bverwg.de); BVerwG 18.07.2019, 7 C 26.17 — UVP-Vorpruefung (bverwg.de); EuGH C-243/15 / C-664/15 — Aarhus-Klagebefugnis Umweltverband (curia.europa.eu).

## Anschluss-Skills

- `fachanwalt-verwaltungsrecht-drittanfechtung-umwelt` — Drittanfechtungs-Strategie
- `umweltrecht-verfahren` — Klageverfahren Geruestvorbereitung
- `energieanlagen-bimschg-genehmigung-verfahren` — Spezial-Energieanlagen
- `eilantrag-80-abs-5-vwgo` — Eilrechtsschutz nach Genehmigung

---

## Skill: `kommandocenter`

_Umweltmandat-Einstieg: Intake Anlagenkarte Behördenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster Mandanten-Typ-Identifikation Sachgebiets-Routing Triage-Matrix. Output Mandat-Karte Routing-Empfehlung N..._

# Umweltrecht-Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage-Matrix — welcher Fachmodul?

| Sachverhalt | Fachmodul |
|---|---|
| BImSchG-Genehmigung beantragen oder anfechten | `umweltrecht-immissionsschutz-bimschg` |
| Emissionshandel TEHG, BEHG, DEHSt | `umweltrecht-emissionshandel-tehg` |
| Abfallstatus, KrWG, Nebenprodukt, Circular Economy | `umweltrecht-abfall-circular-economy` |
| Naturschutz, FFH, Artenschutz § 44 BNatSchG | `umweltrecht-naturschutz-artenschutz` |
| Stoerfall-Anlage, 12. BImSchV, Seveso | `umweltrecht-stoerfall-anlagen` |
| Wasser-Erlaubnis, Altlasten, BBodSchG | `umweltrecht-wasser-bodenschutz` |
| M&A-Transaktion, Umwelt-DD, Red Flags | `umweltrecht-transaktionen-dd` |
| UIG/IFG-Informationsantrag, Ablehnung | `umweltrecht-umweltinformation-uig-ifg` |
| VG-Klage, Eilantrag, Beschwerde OVG | `umweltrecht-verfahren` |
| Bussgeld-Bescheid, Anhörung, Sanktionen | `umweltrecht-bussgeld-sanktionen` |
| Compliance, Beauftragte, Schulungsplan | `umweltrecht-compliance-schulung` |
| ESG, CSRD, Greenwashing | `esg-greenwashing-csrd` |
| Klimaklage, Verbandsklage UmwRG | `klimaklagen-verbandsklage-umwrg` |
| Lieferkette, LkSG, CSDDD | `lksg-csddd-lieferkettensorgfalt` |

## Intake-Fragen (für jeden Mandat)

1. **Mandantenrolle**: Betreiber, Investor, Betroffener Dritter, Umweltverband, Behörde?
2. **Rechtsgebiet**: BImSchG, KrWG, WHG, BBodSchG, TEHG, BNatSchG — oder mehrere?
3. **Verfahrensstand**: Noch kein Verfahren / Antragsverfahren laufend / Bescheid ergangen / Klage anhangig?
4. **Fristen akut**: Widerspruch 1 Monat, Klage 1 Monat, Eilantrag unverzueglich — Eingang Bescheid?
5. **Beweismaterial**: Welche Dokumente — Genehmigung, Gutachten, Behördenkorrespondenz, Fotos?
6. **Wirtschaftliches Ziel**: Betrieb sichern, Anlage verhindern, Entschaedigung, Informationszugang, Reputationsschutz?

## Zentrale Querschnitts-Normen Umweltrecht

- **§§ 3-10 BImSchG** — Grundpflichten Emissionsschutz
- **§§ 4 9 10 BBodSchG** — Altlasten-Verantwortung und Sanierung
- **§§ 8 9 10 WHG** — Wasserrechtliche Erlaubnisse
- **§§ 14 15 34 44 BNatSchG** — Eingriff, FFH, Artenschutz
- **§ 2 UmwRG** — Verbandsklage-Befugnis
- **§ 4 UmwRG** — Verfahrensfehler als Aufhebungsgrund
- **§ 80 Abs. 5 VwGO** — Eilrechtsschutz gegen vollziehbare Genehmigung

## Leitentscheidungen (Ueberblick)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ampelmatrix Risikobewertung (Standard-Output)

| Risiko | Ampel | Fristen | Verantwortlich | Naechste Handlung |
|---|---|---|---|---|
| [THEMA 1] | ROT | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 2] | ORANGE | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 3] | GRUEN | — | [PERSON] | Monitoring |

## Output-Template: Mandatskarte Umweltrecht

**Adressat:** Akte / Interne Notiz — Tonfall: strukturiert, stichwortartig

```
MANDATSKARTE UMWELTRECHT
Stand: [DATUM]
Akte: [AKTENZEICHEN]

MANDANT: [NAME], [ROLLE: Betreiber/Nachbar/Verband]
GEGNER/BEHOERDE: [NAME/STELLE]
ANLAGE: [BEZEICHNUNG], [ORT], [TYP]

RECHTSRAHMEN:
- Hauptnorm: § [X] [GESETZ]
- Nebenrecht: [weitere Normen]

VERFAHRENSSTAND:
- [DATUM]: Genehmigung erteilt / Antrag gestellt / Bescheid erhalten
- [DATUM]: Widerspruch eingelegt / Klage erhoben
- [DATUM]: Naechster Termin [Erörterungstermin / VG / OVG]

FRISTEN:
- [DATUM]: Klagefrist / Einwendungsfrist / TEHG-Abgabe

RISIKEN:
- ROT: [Konkrete Gefahr, z.B. Praeklusion mangels Einwendung]
- ORANGE: [Risiko mit Einschaetzung Wahrscheinlichkeit]

NAECHSTE HANDLUNG:
1. [Konkrete Massnahme, Verantwortlich, Deadline]
2. [Weitere Massnahme]

OFFENE FRAGEN / BENOETIGT:
- [Dokument / Information]
```

## Schnittstellen-Skills

- `fachanwalt-verwaltungsrecht-orientierung` — allgemeine Verwaltungsrechtspruefung
- `energieanlagen-bimschg-genehmigung-verfahren` — Energie-Spezial-BImSchG
- `energietrassen-planfeststellung-rechtsschutz` — Energie-Planfeststellung
- `esg-greenwashing-csrd` — Nachhaltigkeitsberichte
- `klimaklagen-verbandsklage-umwrg` — Klimaklagen

---

## Skill: `lksg-csddd-lieferkettensorgfalt`

_Unternehmen ab 1000 Mitarbeitern muss Lieferketten-Sorgfaltspflichten nach LkSG und kuenftig CSDDD erfuellen. LkSG seit 1.1.2023 CSDDD Richtlinie 2024/1760 Phasing ab 2027. Normen LkSG §§ 3 4 8 11 24 CSDDD Art. 1 ff. Prüfraster Anwendungsbereich Sorgfaltspflichten Risikoanalyse Beschwerdemechanis..._

# LkSG und CSDDD — Lieferkettensorgfalt

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Unternehmens-Größe (Beschäftigten-Zahl Umsatz)
- Sitz Deutschland / andere EU-Staaten
- Branche (Risiko-Profil)
- Lieferanten-Liste
- Bisherige Compliance-Strukturen
- Bekannte Vorwürfe / Audits

## Schritt 1 — Anwendungs-Bereich

### LkSG seit 1.1.2023

| Phase | Beschäftigten-Schwelle |
|---|---|
| 1.1.2023 | Ab 3000 Beschäftigte in Deutschland |
| 1.1.2024 | Ab 1000 Beschäftigte in Deutschland |

- **Konzern-Betrachtung** Mutter-Tochter aggregiert
- **Auch ausländische Mütter** mit deutscher Niederlassung über Schwelle

### EU-CSDDD Richtlinie (EU) 2024/1760

- **Rechtsnatur:** Richtlinie (nicht Verordnung) — nationale Umsetzung erforderlich
- **Umsetzungsfrist** der Mitgliedstaaten: **26.7.2026**
- Deutschland muss LkSG entsprechend anpassen / ablösen

| Phase Anwendung | Schwellen-Anforderung |
|---|---|
| 2027 | Über 5000 Beschäftigte und Umsatz > EUR 1,5 Mrd. weltweit |
| 2028 | Über 3000 Beschäftigte und Umsatz > EUR 900 Mio |
| 2029 | Über 1000 Beschäftigte und Umsatz > EUR 450 Mio |

- **Hochrisiko-Sektoren** mit reduzierten Schwellen (Textil Mineralien Forstwirtschaft Bau)
- **EU-Niederlassungs-Bezug** auch Drittstaaten-Unternehmen mit EU-Umsatz

### Verhältnis LkSG zu CSDDD

- Bei Inkrafttreten CSDDD ggf. Anpassung LkSG (CSDDD-Implementations-Gesetz)
- CSDDD-Pflichten sind weitgehend strenger
- Tieferes Erstrecken auf gesamte Lieferkette (CSDDD) statt nur mittelbarer Zulieferer bei substantiierter Kenntnis (LkSG)

## Schritt 2 — Sorgfaltspflichten LkSG § 3

### Grundsatzerklärung § 6 Abs. 2 LkSG

- Verabschiedung durch oberste Geschäftsführung
- Bestimmung der Risiken
- Verpflichtung des Unternehmens
- Erwartungen an Mitarbeiter und Zulieferer

### Risikomanagement § 4 LkSG

- Festlegung Zuständigkeiten
- Schulung Mitarbeiter
- Wirksamkeitskontrolle

### Risikoanalyse § 5 LkSG

- **Jährlich** und **anlassbezogen**
- Eigener Geschäftsbereich, unmittelbare Zulieferer
- Bei substantiierten Hinweisen auch mittelbare Zulieferer § 9 LkSG
- Priorisierung nach Risiko (schwere Folgen unmittelbar beeinflussbar)

### Präventionsmaßnahmen § 6 LkSG

- Im eigenen Geschäftsbereich Lieferanten-Auswahl
- Lieferanten-Verträge mit Sorgfalts-Klauseln
- Schulung Lieferanten
- Kontrollen

### Abhilfemaßnahmen § 7 LkSG

- Bei festgestellten Verletzungen sofort
- Eigener Bereich Beendigung
- Unmittelbare Zulieferer Vermeidung Verminderung
- Mittelbare Zulieferer angemessene Maßnahmen

### Beschwerdemechanismus § 8 LkSG

- Zugänglich für eigene Mitarbeiter und Zulieferer-Mitarbeiter
- Vertraulich
- Schutz vor Repressalien
- Verfahrens-Ordnung schriftlich

### Dokumentation und Berichterstattung § 10 LkSG

- Jährlich Bericht spätestens vier Monate nach Geschäftsjahres-Ende
- BAFA-Hochladung
- Öffentlich

## Schritt 3 — Geschützte Rechte und Verbote

### Menschenrechte (LkSG Anlage)

- Kinderarbeit (ILO-Konvention 138, 182)
- Zwangsarbeit
- Diskriminierung
- Vereinigungs-Freiheit
- Arbeitssicherheit und Gesundheit
- Angemessene Vergütung
- Vertrags-Sicherheit

### Umwelt-Verbote (Auswahl)

- Quecksilber (Minamata-Übereinkommen)
- POPs (Stockholmer Übereinkommen)
- Basel-Übereinkommen (Abfall-Export)

### CSDDD-Erweiterung

- Klimaschutz (Klimaplan mit Reduktions-Pfaden)
- Mehr Umwelt-Konventionen
- Internationale Menschenrechte erweitert

## Schritt 4 — Eskalations-Hierarchie

### Eigener Geschäftsbereich

- **Direkte Verletzungs-Vermeidung** sofort
- **Compliance-Programm** umfassend
- **Audit-System**

### Unmittelbare Zulieferer

- **Auswahl** mit Sorgfalts-Klauseln
- **Verträge** mit Eskalations-Stufen
- **Audits** vor Ort
- **Bei Verletzung** Verbesserungs-Plan und ggf. Beendigung

### Mittelbare Zulieferer

- **Standard:** keine aktive Pflicht
- **Bei substantiierter Kenntnis** § 9 Abs. 3 LkSG (Whistleblower-Beschwerde NGO-Hinweis Medien-Bericht)
- **Risiko-Analyse** anlassbezogen erforderlich
- **Maßnahmen** angemessen

### Eskalations-Schritte vor Beendigung

- Verbesserungs-Plan mit Frist
- Aussetzungs-Mechanismus
- Beratung
- Letzte Möglichkeit: Beendigung

## Schritt 5 — Sanktionen

### Bußgelder § 24 LkSG

| Verstoß | Höchst-Betrag |
|---|---|
| Verstoß gegen Risikomanagement | EUR 800.000 |
| Verstoß gegen Berichterstattung | EUR 100.000 |
| Verstoß gegen Beschwerdemechanismus | EUR 100.000 |
| Bei Konzernen > 400 Mio EUR Umsatz | bis 2 Prozent Konzernumsatz |

### Zwangsgelder

- Bei Pflicht-Verletzung als Beugemittel
- Bis EUR 50.000 pro Verfügung

### Ausschluss öffentliche Vergabe § 22 LkSG

- Bei rechtskräftigem Bußgeld ab EUR 175.000
- Bis zu drei Jahre

### Schadensersatz nach allgemeinen Regeln

- **§ 11 LkSG begründet KEINE eigene zivilrechtliche Anspruchs-Grundlage** (§ 3 Abs. 3 LkSG)
- **§ 11 LkSG regelt Prozessstandschaft**: Gewerkschaften und NGOs können mit Ermächtigung des Betroffenen dessen Ansprüche im eigenen Namen einklagen (kein eigenes Verbandsklage-Recht)
- Allgemeine Schadensersatz-Normen (§ 823 BGB, deliktische Konzern-Haftung, ggf. ausländisches Recht) bleiben unberührt
- CSDDD Art. 29 wird hier später eine **eigene zivilrechtliche Haftung** einführen

## Schritt 6 — Verteidigung bei Vorwurf

### BAFA-Verfahren

- Anhörung
- Akteneinsicht
- Stellungnahme

### Argumentation

- **Angemessenheit** der Maßnahmen § 3 Abs. 2 LkSG
- **Bemühens-Pflicht** keine Erfolgs-Pflicht
- **Risiko-Priorisierung** plausibel
- **Konkrete Maßnahmen** dokumentiert

### Sachverhalts-Aufklärung

- Audit-Berichte
- Lieferanten-Korrespondenz
- Verbesserungs-Pläne
- Beschwerdemechanismus-Protokoll

## Schritt 7 — Audit-System

### Internes Audit

- Jährlich
- Risiko-basiert
- Dokumentation

### Externes Audit

- Bei größeren Lieferanten
- Branchen-Standards (amfori BSCI, SA8000, RBA)
- Multi-Stakeholder-Initiativen

### KI-Tools

- Beschaffungs-Software mit Sorgfalts-Modul
- Sanktions- und Risiko-Screening

## Schritt 8 — Compliance-Bausteine

### Lieferanten-Vertrags-Klauseln

```
Der Lieferant verpflichtet sich, die Sorgfaltspflichten
des deutschen Lieferkettensorgfaltspflichtengesetzes und
(ab Geltung) der EU-Lieferketten-Richtlinie in seinem
Geschaeftsbereich und gegenueber seinen eigenen Zulieferern
einzuhalten.

Der Lieferant gewaehrt dem Auftraggeber und seinen
beauftragten Pruefern auf Anforderung Zugang zu
Betriebsstaetten und Unterlagen zur Verifizierung
der Sorgfaltspflichten-Einhaltung.

Bei substantiierten Hinweisen auf Verletzungen verpflichtet
sich der Lieferant zu Mitwirkung an Aufklaerung und Abhilfe.

Bei wiederholten oder schweren Verletzungen kann der
Auftraggeber den Vertrag mit angemessener Frist beenden.
```

### Grundsatz-Erklärung Mustertext

```
Wir als [Unternehmen] verpflichten uns zur Achtung der
Menschenrechte und Umweltstandards in unserem
Geschaeftsbereich und in unserer Lieferkette.

Folgende Risiken haben wir identifiziert und priorisieren
wir: [Liste].

Folgende Praeventions- und Abhilfemassnahmen haben wir
eingerichtet: [Liste].

Diese Erklaerung ist von der Geschaeftsfuehrung am [Datum]
verabschiedet und wird jaehrlich aktualisiert.
```

## Schritt 9 — Beschwerdemechanismus-Aufbau

### Zugang

- Online-Portal (mehrsprachig)
- Hotline mit Übersetzungs-Optionen
- Schriftlich
- Anonym möglich

### Verfahren

- Eingangs-Bestätigung
- Bearbeitungs-Frist
- Rückmeldung Beschwerdeführer
- Repressalien-Schutz

### Verfahrens-Ordnung

- Schriftlich öffentlich
- Aktualisierung jährlich
- Schnittstelle HinSchG-Meldekanal (Synergien)

## Schritt 10 — Bericht-Inhalt § 10 LkSG

### Pflicht-Inhalte

- Risiken identifiziert
- Wirksamkeit Maßnahmen
- Folgerung künftige Maßnahmen
- Berücksichtigung Erwartungen Anspruchsberechtigter

### Form

- Über BAFA-Portal (XML-Schema)
- Veröffentlichung Webseite

### Frist

- Vier Monate nach Geschäftsjahres-Ende
- Bei Versäumnis Zwangsgeld

## Schritt 11 — CSDDD-Vorbereitung

### Klima-Plan-Pflicht

- Reduktions-Pfade gemäß 1,5-Grad-Ziel
- Konkrete Zwischen-Ziele
- Investitions-Pläne

### Erweiterung Lieferketten-Tiefe

- "Activity Chain" — gesamte vor- und nachgelagerte Wertschöpfungs-Kette
- Mehr Sektoren-Erfassung

### Zivilrechtliche Haftung CSDDD Art. 22

- **Eigene zivilrechtliche Haftung** in EU
- Schadensersatz bei Pflichtverletzung
- Bewusst weiter als LkSG

### Sanktionen CSDDD

- Bis 5 Prozent Konzernumsatz Bußgeld
- Veröffentlichung Sanktion

## Schritt 12 — Verzahnung mit anderen Plugins

- **fachanwalt-internationales-wirtschaftsrecht** Sanktions-Prüfung
- **datenschutzrecht** ki-verordnung-compliance bei automatisierter Lieferanten-Risiko-Bewertung
- **fachanwalt-arbeitsrecht** HinSchG-Synergien bei Beschwerdemechanismus
- **umweltrecht-compliance-schulung** Bei Umwelt-Pflichten

## Ausgabe

- `lksg-csddd-pruefung-{unternehmen}.md` mit Anwendungsbereich Pflichten Lücken
- Compliance-Roadmap mit Fristen
- Risiko-Analyse-Vorlage
- Beschwerdemechanismus-Verfahrens-Ordnung
- Lieferanten-Vertragsklausel-Bibliothek
- Bei Vorwurf: Verteidigungs-Strategie
- Frist im Fristenbuch (Bericht vier Monate Geschäftsjahres-Ende)

## Quellen

- LkSG §§ 3 4 5 6 7 8 9 10 11 22 24
- Richtlinie (EU) 2024/1760 CSDDD (Umsetzungsfrist 26.7.2026)
- ILO-Konventionen 138 182
- Minamata-Übereinkommen
- Stockholmer Übereinkommen POPs
- Basel-Übereinkommen
- BAFA-Verlautbarungen
- UN Guiding Principles on Business and Human Rights
- OECD Due Diligence Guidance

---

## Skill: `naturschutz-artenschutz`

_Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL 92/43/EWG Vogelschutz-RL. Prüfraster Eingriffs-Ausgleichs-Regelung saP-Gutachten FFH-..._

# Naturschutz und Artenschutz

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere vor Eingriffs-Beurteilung

1. Liegt ein Eingriff in Natur und Landschaft vor (§ 14 BNatSchG)?
2. Befindet sich das Vorhaben im oder in der Naehe eines FFH-/Vogelschutz-Gebiets?
3. Koennen besonders/streng geschuetzte Arten betroffen sein (§ 44 BNatSchG)?
4. Ist ein naturschutzrechtlicher Fachbeitrag (saP, FFH-VS) erforderlich?
5. Wer ist Mandant — Vorhabentraeger oder klagender Umweltverband?
6. Liegt bestandskraeftige Genehmigung vor oder laeuft Verfahren?

## Zentrale Normen und Paragrafenkette

- **§ 14 BNatSchG** — Eingriffsbegriff (Veraenderung Gestalt/Nutzung Grundflaeche)
- **§ 15 BNatSchG** — Eingriffs-Ausgleichs-Regelung (Vermeidung, Ausgleich, Ersatz, Ausnahme)
- **§ 34 BNatSchG** — FFH-Vertraeglichkeitspruefung (erhebliche Beeintraechtigung Schutzzweck)
- **§ 36 BNatSchG** — Ausnahme FFH (zwingende Gruende öffentliches Interesse, Ausgleichsmasnnahmen)
- **§ 44 Abs. 1 BNatSchG** — Verbotstatbestaende Artenschutz (Toeten, Stoeren, Entnahme, Zerstoerung Fortpflanzungsstaetten)
- **§ 45 BNatSchG** — Befreiung und Ausnahme Artenschutz
- **§ 69 BNatSchG** — Ordnungswidrigkeiten (Bussgeld bis 50.000 EUR)
- **§ 1 UmwRG** — Klagebefugnis anerkannter Umweltvereinigungen
- **§ 2 UmwRG** — Verbandsklage ohne Selbstbetroffenheit
- **Art. 12 FFH-Richtlinie 92/43/EWG** — Europaeischer Artenschutz strenge Verbote

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

### A) Vorhabentraeger: Artenschutzpruefung und FFH-VS

1. **Screening**: Lage in FFH-/VS-Gebiet oder signifikante Naehe? LANA-Hinweise zur Erheblichkeit.
2. **saP in Auftrag geben**: Spezieller artenschutzrechtlicher Fachbeitrag; Begehungen Fruehling und Herbst; Zielarten (Feldvogel, Fledermaus, Reptilien) kartieren.
3. **FFH-Vertraeglichkeitspruefung**: Screening-Stufe (erhebliche Beeintraechtigung moeglich?) → Hauptpruefung (alle Wirkpfade; Mafsnahmen zur Schadensbegrenzung).
4. **Ausnahme § 45 BNatSchG beantragen** (wenn Verbotstatbestand nicht vermeidbar): Oeffentliches Interesse, keine Alternativen, Ausgleich durch vorgezogene Ausgleichsmafsnahmen (CEF-Mafsnahmen).
5. **Eingriffsregelung § 15 BNatSchG**: Gruenplan mit Ausgleichsflaechen; Verhaeltnis Eingriff/Ausgleich 1:1 bis 1:3.
6. **Dokumentation**: Bestandteil des Genehmigungsantrags; Aktualisierung bei laenger als 2 Jahre zurueckliegenden Kartierungen.

### B) Umweltverband: Verbandsklage

1. **Klagebefugnis pruefen**: UmwRG-Anerkennung BUND, NABU, DUH; § 2 UmwRG kein Selbstbetroffenheitserfordernis.
2. **Ruege im Verwaltungsverfahren**: Pflicht zur Beteiligung; Unterlassen fuehrt zu Praeklusion im Klageverfahren (§ 5 UmwRG).
3. **Angriffspunkte**: Fehlerhafte saP, unzureichende FFH-VS, Artenschutz-Ausnahme nicht gerechtfertigt.
4. **Eilantrag § 80a VwGO**: Bei vollziehbarer Genehmigung sofort stellen.

### Entscheidungsbaum

```
Ist streng geschuetzte Art betroffen (§ 44 Abs. 1 BNatSchG)?
 JA → Vermeidung technisch moeglich?
 JA → Vermeidungsmafsnahme festlegen und dokumentieren
 NEIN → Ausnahme § 45 BNatSchG:
 Oeffentliches Interesse? JA → CEF-Mafsnahmen + Behördenentscheidung
 NEIN → Vorhaben in dieser Form nicht genehmigungsfaehig
 NEIN → Eingriffs-Ausgleichs-Regelung § 15 BNatSchG genuegt
```

## Output-Template: Einwendung im Genehmigungsverfahren (Verband)

**Adressat:** Genehmigungsbehoerde — Tonfall: sachlich-juristisch

```
An die [GENEHMIGUNGSBEHOERDE]

Einwendung des [VERBAND] gemaess § 10 Abs. 3 BImSchG / § 73 Abs. 4 VwVfG

Vorhabentraeger: [NAME]
Vorhaben: [BESCHREIBUNG]
Auslegung vom [DATUM] bis [DATUM]

I. Grundlage
[VERBAND] ist anerkannte Vereinigung i.S.d. § 3 UmwRG (Anerkennungsbescheid Anlage).

II. Artenschutz § 44 BNatSchG
Die saP vom [DATUM] genuegt nicht den Anforderungen:
1. Kartierung Fledermaeuse: Nur [X] Begehungen, keine Auswertung Horchboxen.
2. Brutvoegel: Brutvogel-Kartierung fehlt für Bereich [X] vollstaendig.
3. Stoerungsverbot § 44 Abs. 1 Nr. 2 BNatSchG: Laermimmission waehrend Brutzeit
 nicht bewertet.

III. FFH-Vertraeglichkeit § 34 BNatSchG
Das FFH-Gebiet [NAME] liegt [X] m entfernt. Eine FFH-VS liegt nicht vor,
obwohl erhebliche Beeintraechtigung des Schutzzwecks [ZIELART] nicht
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

IV. Antrag
Die Genehmigung darf erst erteilt werden, wenn aktuelle saP und FFH-VS
vorgelegt und ausgelegt werden.
```

## Vertiefung: CEF-Mafsnahmen

- CEF = Continuous Ecological Functionality; muessen vor Eingriff wirksam sein.
- Typische CEF: Nisthilfen, alternative Bruthabitate, Amphibien-Leitwaende.
- Monitoring-Pflicht: Regelmäßige Kontrolle Wirksamkeit; bei Versagen: Anordnung Nachbesserung.

## Anschluss-Skills

- `umweltrecht-verfahren` — Klageverfahren Naturschutz
- `klimaklagen-verbandsklage-umwrg` — Verbandsklage Klimaschutz
- `energieanlagen-bimschg-genehmigung-verfahren` — Artenschutz bei Energieanlagen
- `fachanwalt-verwaltungsrecht-drittanfechtung-umwelt` — Drittanfechtung Naturschutz

---

## Skill: `start-chronologie-fristen`

_Einstieg, Schnelltriage und Fallrouting im Umweltrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordne..._

# Umweltrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Umweltrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `lksg-csddd-lieferkettensorgfalt` | Unternehmen ab 1000 Mitarbeitern muss Lieferketten-Sorgfaltspflichten nach LkSG und kuenftig CSDDD erfuellen. LkSG seit 1.1.2023 CSDDD Richtlinie 2024/1760 Phasing ab 2027. Normen LkSG §§ 3 4 8 11 24 CSDDD Art. 1 ff.… |
| `umweltrecht-abfall-circular-economy` | Unternehmen oder Anlagenbetreiber hat Abfall-Frage: Abfalleigenschaft Entsorgungspflichten Nebenprodukt-Einstufung Ende der Abfalleigenschaft. Normen KrWG §§ 3 4 5 7 14 17 EU-Abfallrahmenrichtlinie 2008/98/EG LAGA.… |
| `umweltrecht-bussgeld-sanktionen` | Unternehmen erhaelt Anhörung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR.… |
| `umweltrecht-compliance-schulung` | Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfallverantwortliche. Normen BImSchG §§ 53-58 KrWG §§ 59 60 WHG §§ 64 65. Prüfraster… |
| `umweltrecht-emissionshandel-tehg` | Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster… |
| `umweltrecht-immissionsschutz-bimschg` | Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot.… |
| `umweltrecht-kommandocenter` | Umweltmandat-Einstieg: Intake Anlagenkarte Behördenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster… |
| `umweltrecht-naturschutz-artenschutz` | Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL… |
| `umweltrecht-stoerfall-anlagen` | Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung… |
| `umweltrecht-transaktionen-dd` | M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags… |
| `umweltrecht-umweltinformation-uig-ifg` | Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz… |
| `umweltrecht-verfahren` | Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhörung Widerspruch Eil- und Klageverfahren. Normen VwGO §§ 42 43 47 80 80a 80b 113 123 VwVfG §§ 28 39 UmwRG §§ 1 2 4. Prüfraster Klagebefugnis… |
| `umweltrecht-wasser-bodenschutz` | Unternehmen beantragt WHG-Erlaubnis oder hat Altlastenverantwortung oder Bodenverunreinigung. Normen WHG §§ 8 9 10 12 57 BBodSchG §§ 4 9 10 12 24 BodSchV. Prüfraster Erlaubnis-Voraussetzungen Altlasten-Haftungskette… |

## Worum geht es?

Das Plugin deckt das gesamte Umweltrecht von der Anlagengenehmigung nach BImSchG ueber den Emissionshandel (TEHG), Abfallrecht und Gewaesserschutz bis hin zu Naturschutz, Artenschutz und Stoerfallanlagen ab. Es begleitet sowohl Zulassungsverfahren als auch behordliche Ueberwachung, Bussgeldverfahren und verwaltungsgerichtliche Streitigkeiten.

Hinzu kommen neuere Rechtsgebiete: ESG-Berichtspflichten nach CSRD, Greenwashing-Abwehr, Lieferkettensorgfaltspflichten nach LkSG und CSDDD sowie Klimaklagen und Verbandsklagen nach UmwRG. Zielgruppe sind Anlagenbetreiber, Unternehmensjuristen, Umweltberater und Verwaltungsrechtler.

## Wann brauchen Sie diese Skill?

- Anlagenbetreiber will BImSchG-Genehmigung beantragen, aendern oder verteidigen, oder Nachbar klagt gegen Anlage.
- Unternehmen erhalt Bussgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will Gegenvorstellung oder Einspruch einlegen.
- M&A-Transaktion: Anwalt prueft im Datenraum umweltrechtliche Risiken (Altlasten, Genehmigungsstatus, Abfall).
- ESG-Bericht muss erstellt oder ein Greenwashing-Vorwurf abgewehrt werden.
- Unternehmen ab 1.000 Mitarbeitern muss LkSG-Sorgfaltspflichten implementieren und dokumentieren.

## Fachbegriffe (kurz erklaert)

- **BImSchG** — Bundes-Immissionsschutzgesetz; regelt Genehmigung und Betrieb emittierender Anlagen.
- **TEHG** — Treibhausgas-Emissionshandelsgesetz; nationaler Rahmen für EU-Emissionshandel.
- **Stoerfall-Anlage (Seveso III)** — Anlage mit besonderem Gefahrenpotenzial; gesonderte Pflichten nach 12. BImSchV.
- **FFH-Vertraeglichkeit** — Pruefung nach der Fauna-Flora-Habitat-Richtlinie (RL 92/43/EWG), ob ein Vorhaben ein Natura-2000-Gebiet erheblich beeintraechtigt.
- **CSRD** — Corporate Sustainability Reporting Directive (EU); erweiterte Nachhaltigkeitsberichtspflichten gestaffelt ab 2024.
- **LkSG** — Lieferkettensorgfaltspflichtengesetz; gilt seit 01.01.2024 für Unternehmen ab 1.000 Mitarbeiter in Deutschland.
- **UmwRG** — Umwelt-Rechtsbehelfsgesetz; ermoeglicht anerkannten Umweltverbaenden Klagen gegen Zulassungsentscheidungen.
- **UIG** — Umweltinformationsgesetz; Recht auf Zugang zu Umweltinformationen bei Behörden.

## Rechtsgrundlagen

- BImSchG §§ 4 5 6 10 — Genehmigungspflicht und -voraussetzungen
- TEHG §§ 4 5 7 8 9 — Emissionshandel, Zuteilung, Abgabe
- KrWG — Kreislaufwirtschaftsgesetz (Abfall)
- WHG §§ 8 9 10 12 — Wasserrecht, Erlaubnis, Bewilligung
- BBodSchG — Bundesbodenschutzgesetz, Altlasten
- BNatSchG §§ 44 45 — Artenschutzverbote und Ausnahmen
- UmwRG — Umwelt-Rechtsbehelfsgesetz
- LkSG — Lieferkettensorgfaltspflichtengesetz
- CSRD (EU) VO 2022/2464 — Nachhaltigkeitsberichtspflichten

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Anlagenbetreiber, Unternehmen mit Lieferkettenpflichten, Verband oder Nachbar?
2. Phase bestimmen: Genehmigungsantrag, laufender Betrieb, Behördenpruefung, Bussgeld oder Klage?
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Widerspruchs- und Klagefrist gegen Genehmigung oder Bescheid (§§ 68 ff. VwGO).
5. Anschluss-Skill bestimmen: z.B. nach Bussgeld ggf. Compliance-Schulung; nach DD ggf. Transaktionsabsicherung.

## Skill-Tour (was gibt es hier?)

- `umweltrecht-kommandocenter` — Intake-Routing: neues Umweltmandat einsortieren, Anlagenkarte erstellen, naechste Schritte bestimmen.
- `umweltrecht-immissionsschutz-bimschg` — BImSchG-Genehmigung beantragen, anfechten oder Nachbar-Drittschutz geltend machen.
- `umweltrecht-emissionshandel-tehg` — Zuteilungsantrag, Monitoring, Abgabepflicht nach TEHG; DEHSt-Sanktion abwehren.
- `umweltrecht-abfall-circular-economy` — Abfalleigenschaft, Entsorgungspflichten, Nebenprodukt, Ende-der-Abfalleigenschaft nach KrWG.
- `umweltrecht-wasser-bodenschutz` — WHG-Erlaubnis, Altlastenverantwortung, Bodensanierung nach BBodSchG.
- `umweltrecht-naturschutz-artenschutz` — FFH-Vertraeglichkeit, Artenschutzverbote nach § 44 BNatSchG, Ausnahmen.
- `umweltrecht-stoerfall-anlagen` — Seveso-III-Compliance: Stoerfall-Meldepflicht, Sicherheitsbericht, DEHSt-Verfahren.
- `umweltrecht-transaktionen-dd` — Umwelt-Due-Diligence in M&A-Transaktionen: Genehmigungen, Altlasten, Abfall, Emissionen.
- `umweltrecht-bussgeld-sanktionen` — Umwelt-Ordnungswidrigkeiten: Bussgeld-Bescheid, Einspruch, Sanktionsvermeidung.
- `umweltrecht-verfahren` — Verwaltungsgerichtliche Verfahren: Widerspruch, Klage, Eilrechtsschutz im Umweltrecht.
- `umweltrecht-umweltinformation-uig-ifg` — UIG/IFG-Antrag stellen oder Ablehnung anfechten; Informationszugang durchsetzen.
- `umweltrecht-compliance-schulung` — Compliance-Schulungsplaene und Jahresaudit für Immissionsschutz- und Abfallbeauftragte.
- `lksg-csddd-lieferkettensorgfalt` — LkSG-Sorgfaltspflichten implementieren; CSDDD-Vorbereitung für europaische Erweiterung.
- `esg-greenwashing-csrd` — CSRD-Bericht erstellen oder Greenwashing-Vorwuerfe nach UWG und Green Claims-RL abwehren.
- `klimaklagen-verbandsklage-umwrg` — Klimaklage oder Verbandsklage nach UmwRG; BVerfG-Klimabeschluss, UmwRG-Klagebefugnis.

## Worauf besonders achten

- BImSchG-Genehmigungen sind anlagenbezogen, nicht personenbezogen; Betreiberwechsel erfordert Anzeige, kann Genehmigungspflicht ausloesen.
- LkSG-Sorgfaltspflichten gelten ab 01.01.2024 auch für Unternehmen ab 1.000 Mitarbeitern; Verstoss loest BAFA-Bussgelder aus.
- FFH-Vertraeglichkeitspruefung ist eigenstaendiger Schritt vor Planfeststellung; Fehler fuehren regelmaessig zur Aufhebung in der Revision.
- Emissionshandel hat harte Abgabefristen (30. April des Folgejahres); Versaeumnis loest automatische Strafzahlungen aus.
- CSRD-Berichte muessen von einem Wirtschaftspruefer oder Umweltgutachter beglaubigt werden; Fehler bei Wesentlichkeitsanalyse sind Haftungsrisiko.

## Typische Fehler

- BImSchG-Genehmigung nicht rechtzeitig geaendert: Wesentliche Aenderungen an genehmigten Anlagen beduerften gesonderter Genehmigung (§ 16 BImSchG); ungenehmigte Aenderung ist illegal.
- Altlasten in M&A-Transaktionen unterschaetzt: Bodensanierungspflicht geht auf Kaeufer ueber; kein Haftungsausschluss ohne vollstaendige DD.
- UmwRG-Klagebefugnis uebersehen: Nur anerkannte Umweltverbaende koennen nach § 3 UmwRG klagen; Private beduerften eigener Rechtsverletzung.
- Greenwashing-Aussagen ohne Substanz: EU Green Claims-Richtlinie (Entwurf) und § 5 UWG erfordern pruefbare Belege für Umweltaussagen.
- Verfristete LkSG-Risikoberichte: Jaehrliche Dokumentationspflicht mit gesetzlicher Frist; fehlendes Reporting loest BAFA-Massnahmen aus.

## Quellen und Aktualitaet

- Stand: 05/2026
- BImSchG, TEHG, KrWG, WHG, BBodSchG, BNatSchG, UmwRG, UIG, LkSG in aktuell geltender Fassung
- CSRD (EU VO 2022/2464) gestaffelt ab 2024/2025/2026 in Kraft

---

## Skill: `stoerfall-anlagen-transaktionen-dd`

_Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung Sicherheitsbericht Betreiberpflichten Sicherheitsabstaende Bauleitplanung. Output Sicherheitsb..._

# Stoerfall, Anlagenbetrieb und Betreiberpflichten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere zuerst

1. Faellt die Anlage unter die 12. BImSchV (Stoerfall-Verordnung) — Grundpflichten (Anhang I Spalte 1) oder erweiterte Pflichten (Anhang I Spalte 2)?
2. Sind gefaehrliche Stoffe (Anhang I 12. BImSchV) in welchen Mengen vorhanden?
3. Liegt ein Stoerfall bereits vor oder geht es um praeventive Compliance?
4. Wurden die zuständige Behörde und die Oeffentlichkeit informiert (§§ 19, 20 BImSchV)?
5. Besteht eine Anordnung der Behörde (§ 17 BImSchG) auf Grundlage Sicherheitsmangel?
6. Ist Bauleitplanung in der Naehe geplant — Sicherheitsabstandsproblem?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 3 Abs. 5a BImSchG** — Stoerfall-Definition (unkontrolliertes Ereignis, erhebliche Gefahr)
- **§ 7 Abs. 1 Nr. 5 BImSchG** — Anforderungen an Anlagen Sicherheitsbericht
- **§ 16 BImSchV (12. BImSchV)** — Sicherheitsbericht Pflichtinhalt (Gefahrenquellen, Schutz-/Notfallkonzept)
- **§ 17 BImSchV** — Bericht nach Stoerfall (Untersuchungspflicht, Massnahmen)
- **§ 19 BImSchV** — Stoerfallanzeige bei Behörde (unverzueglich)
- **§ 20 BImSchV** — Unterrichtung Oeffentlichkeit (Angaben Anlagen-Website)
- **Art. 13 Seveso-III-Richtlinie (2012/18/EU)** — Sicherheitsabstaende Raumordnung
- **§ 50 BImSchG** — Trennungsgebot Gebiete mit schweren Unfaellen und Wohnnutzung
- **§ 17 BImSchG** — Nachtraegliche Auflagen und Anordnungen
- **§ 62 BImSchG** — Ordnungswidrigkeiten (Bussgeld bis 50.000 EUR)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Praeventive Compliance-Pruefung

1. **Stoerfall-Relevanz pruefen**: Mengen gefaehrlicher Stoffe nach Anhang I 12. BImSchV — Spalte 1 oder 2.
2. **Sicherheitskonzept Grundpflichten**: § 8 12. BImSchV — schriftliches Konzept Verhuetung Stoerfaelle.
3. **Sicherheitsbericht Erweiterte Pflichten**: § 16 12. BImSchV — Inhalt: Stoffe, Anlage, Risiken, Notfallplanung; Prueflauf alle 5 Jahre.
4. **Anzeige/Genehmigung**: § 4 BImSchG, § 9 12. BImSchV — Behörde informieren vor Betriebsbeginn.
5. **Sicherheitsabstand pruefen**: KAS-18-Leitfaden BG Chemie; Abstand zu schutzbeduerftigen Gebieten ermitteln.
6. **Notfallplan**: § 10 12. BImSchV — interner Alarm- und Notfallplan; externe Information an Behörde.
7. **Unterrichtung Oeffentlichkeit**: § 20 12. BImSchV — Anlage-Website Sicherheitsinformationen.

### B) Reaktion auf Stoerfall

1. **Sofortanzeige**: § 19 12. BImSchV — unverzueglich an Behörde, Feuerwehr, Umweltamt.
2. **Ursachenuntersuchung**: § 17 12. BImSchV — Bericht innerhalb angemessener Frist.
3. **Massnahmenumsetzung**: Wiederholungsvermeidung; Dokumentation.
4. **Bussgeld-Abwehr**: § 62 BImSchG — schuldlose Pflichtverletzung, technisches Versagen ohne Vorwerfbarkeit?
5. **Kommunikation Behörde**: Kooperationsbereitschaft zeigen; Massnahmenplan vorlegen.

### Entscheidungsbaum Stoerfallrelevanz

```
Stoff in Anhang I 12. BImSchV?
 JA → Menge erreicht Spalte-1-Schwelle?
 JA → Grundpflichten (§§ 3-9 12. BImSchV)
 Menge erreicht Spalte-2-Schwelle?
 JA → Erweiterte Pflichten incl. Sicherheitsbericht § 16
 NEIN → Nur Grundpflichten
 NEIN → Keine Stoerfall-VO-Pflicht; normale BImSchG-Anforderungen
 NEIN → Keine Stoerfall-Relevanz
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Stellungnahme nach Storfallmeldung erstellen | Stellungnahme nach Schema; Template unten |
| Variante A — Stoeranfall noch laufend keine Stellungnahme moeglich | Krisenkommunikation zuerst; Stellungnahme nach Abschluss |
| Variante B — Stoeranfall ohne Schaden nur formale Meldepflicht | Minimale Meldung; Stellungnahme kurzgefasst |
| Variante C — Behörde droht Betriebsuntersagung | Dringlichkeit erhoehen; Stellungnahme mit Massnahmenplan |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template: Stellungnahme nach Stoerfallanzeige

**Adressat:** Zustaendige Behörde — Tonfall: sachlich-kooperativ

```
An die [BEHOERDE]

Stoerfall-Bericht gemaess § 17 der 12. BImSchV

Betreiber: [NAME MANDANT]
Anlage: [NAME], [ORT], BImSchG-Genehmigung Az. [NR.]
Ereignis: [DATUM], [UHRZEIT]

I. Beschreibung des Ereignisses
Am [DATUM] um [UHRZEIT] ereignete sich [kurze Beschreibung].
Freigesetzte Stoffe: [Stoff, Menge, Ausbreitung].
Betroffener Bereich: [Gelaende/Oeffentlichkeit].

II. Sofortmassnahmen
1. Alarmierung Feuerwehr und Werkschutz um [UHRZEIT].
2. Evakuierung Gefahrenbereich ab [UHRZEIT].
3. Auftrag Dekontamination an [FIRMA] erteilt.

III. Ursache (vorläufige Einschaetzung)
[Beschreibung technischer Ursache, menschliches Versagen / hoeherer Gewalt].

IV. Massnahmen zur Wiederholung-Vermeidung
1. [Technische Massnahme, Zeitplan].
2. [Schulung Personal, Datum].
3. [Aenderung Betriebsanweisung].

V. Naechste Schritte
Wir legen bis zum [DATUM] einen vollstaendigen Untersuchungsbericht vor.

Anlagen: Lageplan, Stofffliessschema, Messprotokoll
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Anlagenpflichtenmatrix (Kurzform)

| Pflicht | Spalte 1 | Spalte 2 | Grundlage |
|---|---|---|---|
| Schriftliches Sicherheitskonzept | JA | JA | § 8 12. BImSchV |
| Sicherheitsbericht | NEIN | JA | § 16 12. BImSchV |
| Notfallplan intern | JA | JA | § 10 Abs. 1 |
| Extern. Notfallplan Behörde | NEIN | JA | § 10 Abs. 2 |
| Dominoeffekt-Pruefung | NEIN | JA | § 14 12. BImSchV |
| Oeffentlichkeits-Information | NEIN | JA | § 20 12. BImSchV |
| Sicherheitsabstand | JA | JA | § 50 BImSchG |

## Anschluss-Skills

- `umweltrecht-immissionsschutz-bimschg` — BImSchG-Genehmigungsrahmen
- `umweltrecht-bussgeld-sanktionen` — Bussgeld nach Stoerfall
- `umweltrecht-verfahren` — Klageverfahren gegen Behördenanordnung
- `umweltrecht-transaktionen-dd` — Stoerfall-Risiken in M&A

---

## Skill: `transaktionen-dd`

_M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags Closing-Conditions Capex-Risiken Wert-Adjustierung. Output Umwelt-DD-Report Kaufvertrags-K..._

# Umweltrechtliche Transaktions-Due-Diligence

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere vor DD-Beginn

1. Share Deal oder Asset Deal? (Share Deal: Haftung folgt Gesellschaft; Asset Deal: Einzelvermoegensuebertragung, Haftungsrueckstand bleibt bei Verkaeufer in Grenzen).
2. Welche Anlagen/Standorte — BImSchG-Genehmigungen vorhanden?
3. Altlasten bekannt (§§ 4, 9 BBodSchG) — Bodenuntersuchungen vorgelegt?
4. TEHG-Pflicht? Emissionshandel-Status?
5. Produktions-Genehmigungen aktuell oder laeuft Aenderungsverfahren?
6. Bestehen Behördenanordnungen oder laufende Verwaltungs-/Gerichtsverfahren?

## Zentrale Normen und Paragrafenkette

- **§§ 4 6 BImSchG** — Betriebsgenehmigung; Rechtsnachfolge bei Share Deal
- **§ 17 BImSchG** — Nachtraegliche Auflagen; uebernimmt Erwerber bei Share Deal
- **§§ 4 9 BBodSchG** — Altlastenverantwortlichkeit (Verursacher, Eigentueemer, Gesamtrechtsnachfolger)
- **§ 5 KrWG** — Ende Abfalleigenschaft; DD-relevante Bewertung Abfallstatus
- **§ 13 WHG** — Wasserrechtliche Gestattungen; Erlaubnisse nicht automatisch uebertragbar
- **§ 9 TEHG** — Kostenlose ETS-Zuteilung; Kapazitaetsaenderung nach Transaktion melden
- **§ 1 UmwHaftG** — Haftung für Schaden durch Anlage
- **§ 24 BBodSchG** — Erstattungsanspruch bei Sanierung durch Dritte

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-DD

### Phase 1: Kick-off und Scope-Setting

1. Transaktionsstruktur festlegen: Share/Asset Deal, betroffene Gesellschaften, Standorte.
2. DD-Scope: Welche Umweltbereiche — Genehmigungen, Altlasten, Emissionen, Abfall, Wasser, Naturschutz?
3. Datenraum-Liste anfordern: Genehmigungen, Bescheide, Behördenkorrespondenz, Gutachten, Monitoring-Berichte.
4. Wesentlichkeitsschwelle definieren: welche Findings ab welchem EUR-Wert als Red Flag?

### Phase 2: Dokument-Analyse

1. **BImSchG-Genehmigungen**: Inhalt, Nebenbestimmungen, Aenderungs-Historie; laufen aktuelle Verfahren?
2. **Altlasten**: Bodenuntersuchungen Phase I (historische Nutzung) und Phase II (Analytik); Sanierungsplan?
3. **TEHG**: Zuteilungsbescheid, Monitoring-Plan; Abgabe-Geschichte letzter 5 Jahre.
4. **Wasserrecht**: Einleitgenehmigungen, Entnahmegenehmigungen; ablaufende Genehmigungen?
5. **Abfallrecht**: Entsorgungsvertraege, Nachweise; unerlaubte Ablagerungen?
6. **Verfahren/Anordnungen**: Klagen, Widerspruchsverfahren, Behördenanordnungen § 17 BImSchG.

### Phase 3: Red-Flag-Bewertung

| Kategorie | Red Flag | Orange | Gruen |
|---|---|---|---|
| BImSchG-Genehmigung | Fehlt oder wesentlich veraltet | Aenderung laufend | Aktuell und vollstaendig |
| Altlasten | Aktiver Kontaminationsherd | Historische Untersuchung fehlt | Phase II ohne Befund |
| TEHG-Abgabe | Rueckstand > 3 Jahre | Einmalige Verspaetung | Vollstaendig |
| Behördenanordnung | Rechtshaft unanfechtbar | Widerspruch laufend | Keine |
| Naturschutz | Stoerfall-Anlage in Schutzgebiet | FFH-VS fehlt | Vollstaendig |

### Phase 4: Kaufvertrags-Klauseln

1. **Garantien (W&I)**: Genauigkeit Genehmigungen, Altlasten-Freiheit, keine unbekannten Anordnungen.
2. **Indemnities**: Verkaeufer-Freistellung für bekannte Altlasten (Schedule mit Standorten).
3. **Closing-Conditions**: Vorlage aktueller Umwelt-Gutachten, Behörden-Auskunft Altlasten, Freigabe DEHSt TEHG-Konto.
4. **Purchase-Price-Anpassung**: Discount für quantifizierbare Capex-Risiken (Sanierung, Nachruestung).
5. **W&I-Versicherung**: Typical für Mid-Market M&A; Umwelt-Endorsements (Altlasten-Ausschluss / Einschluss gegen Praemie).

## Output-Template: DD-Kurz-Finding (Red Flag)

**Adressat:** Mandant (Kaeufer) / Deal Team — Tonfall: sachlich-analysierend

```
Umwelt-DD-Finding Nr. [X]
Kategorie: Altlasten / BImSchG / TEHG / Wasser
Bewertung: ROT / ORANGE / GRUEN
Standort: [ORT], Grundstueck [FLUR/STRASSE]

Befund:
[Beschreibung des konkreten Problems: fehlende Genehmigung, Altlast-Nachweis, Behördenanordnung]

Rechtsgrundlage: § [X] [Gesetz]

Risikobewertung:
- Haftungsrisiko Erwerber: Bis [BETRAG] EUR gemaess § 4 Abs. 3 BBodSchG
- Sanierungskosten: geschaetzt [BETRAG] EUR (Gutachten [DATUM])
- Zeitraum: [ZEITHORIZONT] Monate bis Behebung

Empfehlung:
1. Closing-Condition: Vollstaendige Phase-II-Untersuchung oder Sanierungsplan.
2. Preisabzug: [BETRAG] EUR.
3. Verkaeufer-Indemnity für bekannten Altlast-Herd.
4. W&I-Versicherungs-Endorsement pruefen.

Quellen: [Dokument im Datenraum, Seite/Tab]
```

## Vertiefung: BBodSchG Haftungskette

- Verursacher > Rechtsnachfolger > Grundstueckseigentuemer > Inhaber tatsaechlicher Gewalt.
- Bei Share Deal: Erwerber tritt als Gesamtrechtsnachfolger in Haftungsposition des Verkaeufers ein.
- Gesamtschuldner-Ausgleich § 24 BBodSchG: Sanierungskosten koennen intern aufgeteilt werden.
- Haftungs-Cap im Kaufvertrag gilt nur zwischen Vertragsparteien, nicht gegenueber Behörde.

## Anschluss-Skills

- `umweltrecht-wasser-bodenschutz` — Altlasten-Vertiefung
- `umweltrecht-emissionshandel-tehg` — TEHG bei Transaktion
- `umweltrecht-immissionsschutz-bimschg` — Genehmigungsrechtsnachfolge
- `energierecht-transaktionen-dd` — Energie-Asset-DD

---

## Skill: `umweltinformation-uig-ifg`

_Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz Drittbeteiligung Widerspruchs-Klage. Output Antrags-Muster Widerspruch Klage VG..._

# Umweltinformation nach UIG und IFG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere vor Antragstellung

1. Liegt Umweltinformation (§ 2 Abs. 3 UIG) vor oder allgemeine Behördeninformation (IFG)?
2. Welche Behörde/Stelle — Behörde des Bundes (IFG/UIG Bund), Behörde des Landes (LIFG/LUIG)?
3. Besteht Drittbeteiligung (Unternehmen, das Geheimnisschutz beansprucht — § 9 UIG)?
4. Ist Antragsgruende angabe notwendig (IFG: nicht erforderlich; UIG: ebenso nicht)?
5. Besteht Eilbedarf (Oeffentlichkeitsbeteiligung in Genehmigungsverfahren laufend)?
6. Soll Widerspruch oder direkt Klage (VG) erhoben werden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 3 Abs. 1 UIG** — Anspruch auf Umweltinformationen (jedermann, keine Begruendung)
- **§ 4 UIG** — Antragstellung; Frist Behörde 1 Monat (verlaeaerbar auf 2 Monate bei Umfang)
- **§ 8 UIG** — Ausschlussgrundsaetze öffentliches Interesse (laufende Verfahren, Landesverteidigung)
- **§ 9 UIG** — Schutz Betriebs- und Geschäftsgeheimnisse; Drittbeteiligung Verfahren
- **§ 10 UIG** — Aktive Verbreitung durch Behörde
- **§ 1 IFG** — Anspruch auf Zugang zu amtlichen Informationen (Bundesbehoerden)
- **§ 3 IFG** — Schutz besonderer öffentlicher Belange (Sicherheit, Beratungsgeheimnis)
- **§ 5 IFG** — Schutz personenbezogener Daten
- **§ 6 IFG** — Schutz des geistigen Eigentums und Betriebs-/Geschäftsgeheimnisse
- **§ 9 IFG** — Antrag und Frist (1 Monat)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Antragsteller (Buerger, NGO, Unternehmen)

1. **Antrag formulieren**: Konkrete Umweltinformation benennen; Bezug zu § 2 Abs. 3 UIG herstellen; keine Begruendung erforderlich.
2. **Adressat**: Informationspflichtige Stelle (Behörde, privatrechtliche Stelle mit öffentlichen Aufgaben — § 2 Abs. 1 UIG).
3. **Frist kontrollieren**: Behörde muss binnen 1 Monat antworten (§ 4 UIG); bei Umfang 2 Monate unter Mitteilung.
4. **Drittbeteiligung abwarten**: Wenn Dritter (Unternehmen) beteiligt — Stellungnahme-Frist + Entscheidung.
5. **Ablehnung anfechten**: Widerspruch (falls Widerspruchsverfahren vorgesehen) oder Klage VG; Klagerecht § 6 UIG auch ohne Vorverfahren in einigen Ländern.
6. **Eilbedarf**: § 123 VwGO Antrag auf vorläufige Herausgabe wenn Informationsbedarf dringend.

### B) Dritter (Unternehmen) — Geheimnisschutz verteidigen

1. **Drittbeteiligung beobachten**: Behörde muss vor Herausgabe Anhoerun durchfuehren (§ 9 Abs. 1 UIG).
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Behördenentscheidung anfechten**: Klage VG gegen Herausgabe-Anordnung; Eilantrag § 80 Abs. 5 VwGO (aufschiebende Wirkung bis VG-Entscheidung).

### Entscheidungsbaum Antrag

```
Informationsbegehren
 → UIG oder IFG? (Umweltbezug → UIG; allgemeine Behörde → IFG)
 → Behörde bundesrechtlich? (Bund: UIG-Bund/IFG; Land: UIG-Land/LIFG)
 → Antrag stellen, 1-Monats-Frist abwarten
 → Keine Antwort? → Untaetigkeit-Klage VG
 → Ablehnung? → Widerspruch (falls vorgesehen) → Klage VG
 → Drittbeteiligung? → Stellungnahme Geheimhaltung → Behörde entscheidet → Klage des Dritten moeglich
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Informationsantrag nach UIG stellen | Antrag nach Schema; Template unten |
| Variante A — Antrag wurde bereits abgelehnt Widerspruch noetig | Widerspruchstemplate verwenden statt Erstantrag |
| Variante B — IFG statt UIG anzuwenden Verwaltungsinformation | IFG-Variante; Abgrenzung UIG-IFG klaeren |
| Variante C — Information eilig Behörde soll priorisieren | Dringlichkeitsvermerk in Antrag aufnehmen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template: Informationsantrag UIG

**Adressat:** Zustaendige Behörde — Tonfall: sachlich, klar

```
An die [BEHOERDE]

Antrag auf Zugang zu Umweltinformationen gemaess § 3 Abs. 1 UIG

Antragsteller: [NAME], [ADRESSE]

Ich beantrage Zugang zu folgenden Umweltinformationen:

1. [Konkrete Beschreibung der gesuchten Information]
 Bezug: [Anlage, Ort, Verfahren, Datum]

2. [Zweite Information, falls mehrere]

Diese Informationen betreffen Umweltfaktoren i.S.d. § 2 Abs. 3 UIG:
[Luft, Wasser, Boden, Emissionen, Massnahmen, Zustand der Umwelt].

Ich bitte um Zugang in folgender Form:
[ ] digitale Kopie (PDF per E-Mail)
[ ] Akteneinsicht vor Ort
[ ] schriftliche Auskunft

Gemaess § 4 Abs. 1 UIG bitte ich um Bescheidung binnen eines Monats.

[NAME], [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Output-Template: Widerspruch nach Ablehnung

**Adressat:** Widerspruchsbehoerde — Tonfall: sachlich-juristisch

```
An die [BEHOERDE]

Widerspruch gegen Ablehnungsbescheid

Antragsteller: [NAME]
Ihr Bescheid vom [DATUM], Az. [AZ.]

I. Hiermit legen wir Widerspruch ein.

II. Begruendung
Die Ablehnung ist rechtswidrig:
a) § 9 UIG Geheimnisschutz: Die Behörde hat keine eigene Abwaegung vorgenommen.
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
b) § 8 UIG laufende Verfahren: Das Verfahren ist abgeschlossen; Ausschlussgrund
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
c) Emissionsdaten sind nach § 9 Abs. 1 Satz 2 UIG grundsaetzlich offenzulegen
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

III. Antrag
Wir beantragen, den Ablehnungsbescheid aufzuheben und die Informationen herauszugeben.
```

## Vertiefung: Aktive Informationspflicht § 10 UIG

- Behörden sollen Umweltinformationen von allgemeinem Interesse aktiv ins Netz stellen.
- Emissionsdaten, Genehmigungen, UVP-Berichte grundsaetzlich oeffentlich.
- Verstoss gegen aktive Veroeffentlichungspflicht: Ruege durch UIG-Antrag + Klage.

## Fristen-Ueberblick

| Schritt | Frist | Grundlage |
|---|---|---|
| Behördenentscheidung | 1 Monat (max. 2 Monate) | § 4 Abs. 1 UIG |
| Widerspruch | 1 Monat ab Ablehnung | § 70 VwGO |
| Klage VG | 1 Monat nach Widerspruchsbescheid | § 74 VwGO |
| Untaetigkeit-Klage | 3 Monate | § 75 VwGO |

## Anschluss-Skills

- `umweltrecht-verfahren` — VG-Klage auf Informationszugang
- `klimaklagen-verbandsklage-umwrg` — NGO-Strategie Umweltinformation
- `fachanwalt-verwaltungsrecht-anfechtungsklage` — Klage gegen Ablehnung

---

## Skill: `verfahren`

_Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhörung Widerspruch Eil- und Klageverfahren. Normen VwGO §§ 42 43 47 80 80a 80b 113 123 VwVfG §§ 28 39 UmwRG §§ 1 2 4. Prüfraster Klagebefugnis Praeklusion Eilantrag-Grounds Planfeststellungs-Zuständigkeit. Output Klage-Entwurf Eila..._

# Umweltrechtliche Verwaltungs- und Gerichtsverfahren

## Arbeitsbereich

Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhörung Widerspruch Eil- und Klageverfahren. Normen VwGO §§ 42 43 47 80 80a 80b 113 123 VwVfG §§ 28 39 UmwRG §§ 1 2 4. Prüfraster Klagebefugnis Praeklusion Eilantrag-Grounds Planfeststellungs-Zuständigkeit. Output Klage-Entwurf Eilantrag Schriftsatz. Abgrenzung zu klimaklagen-verbandsklage-umwrg (spezielle Klage) und umweltrecht-bußgeld-sanktionen (Ordnungsrecht). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — klaere Verfahrenskontext

1. Wer ist Klaeger/Antragsteller — Betreiber, Nachbar oder Umweltverband?
2. Liegt Bescheid/Genehmigung vor oder geht es um Normenkontrolle (§ 47 VwGO)?
3. Ist Verfahren BImSchG-Genehmigung (VG), Planfeststellung (OVG/BVerwG) oder Rechtsetzung?
4. Besteht Eilbedarf (vollziehbare Genehmigung, bevorstehende Baumafsnahme)?
5. Wurden Einwendungen im Genehmigungsverfahren rechtzeitig erhoben (Praeklusions-Risiko)?
6. UmwRG-Vereinigung — Anerkennungsstatus geprueft?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 42 Abs. 1 VwGO** — Anfechtungsklage (Aufhebung Verwaltungsakt)
- **§ 42 Abs. 2 VwGO** — Klagebefugnis (moegliche Verletzung eigener Rechte)
- **§ 43 VwGO** — Feststellungsklage (Rechtsverhaeltnis, Unwirksamkeit Norm)
- **§ 47 VwGO** — Normenkontrolle (Satzungen, Verordnungen, Bebauungsplaene)
- **§ 80 Abs. 5 VwGO** — Eilantrag Wiederherstellung/Anordnung aufschiebende Wirkung
- **§ 80a VwGO** — Drittanfechtung Baugenehmigung/Zulassung
- **§ 113 Abs. 1 VwGO** — Aufhebungsklage; Abs. 5 — Verpflichtungsklage
- **§ 123 VwGO** — Einstweilige Anordnung (Unterlassung, Vorabrherausgabe)
- **§ 1 UmwRG** — Anwendungsbereich (UVP-pflichtige, IPPC-Anlagen, Plaene)
- **§ 2 UmwRG** — Verbandsklage ohne Selbstbetroffenheit
- **§ 4 UmwRG** — Verfahrensfehler für sich allein als Aufhebungsgrund bei UVP-Pflicht
- **§ 5 UmwRG** — Praeklusion bei Nichtbeteiligung im Verwaltungsverfahren

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Anfechtungsklage (Dritter gegen Genehmigung)

1. **Klagebefugnis pruefen**: § 42 Abs. 2 VwGO — drittschuetzende Norm (§ 5 Abs. 1 Nr. 1 BImSchG, TA-Laerm)?
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Klagefrist**: § 74 Abs. 1 VwGO — 1 Monat ab Bekanntgabe; bei Auslegung § 10 BImSchG: 2 Wochen nach Auslegungsende (§ 10 Abs. 8 BImSchG beachten).
4. **Eilantrag § 80a**: Sofort wenn Genehmigung vollziehbar und Bauarbeitten drohen.
5. **Klageschrift**: Klageantrag, Sachverhalt, rechtliche Begruendung mit Leitsaetzen.
6. **Verbandsklage**: UmwRG-Anerkennung pruefen; § 4 UmwRG Verfahrensfehler als eigenstaendiger Aufhebungsgrund.

### B) Verpflichtungsklage (Betreiber auf Genehmigung)

1. **Vorverfahren**: Antrag bei Behörde; Ablehnung oder Untaetigkeit 3 Monate (§ 75 VwGO).
2. **Klage**: Verpflichtungsklage auf Genehmigungserteilung; ggf. hilfsweise Verbescheidungsklage.
3. **Eilantrag § 123 VwGO**: Einstweilige Anordnung auf Duldung Vorbau-/Vorbereitung.
4. **Normenkontrolle § 47 VwGO**: Bei Angriff auf Bauleitplan, der Projekt verhindert.

### Entscheidungsbaum Klageform

```
Liegt ein belastender VA vor?
 JA → Anfechtungsklage § 42 Abs. 1 VwGO
 Dritter (nicht Adressat)?
 JA → Drittschutz pruefen; § 80a Eilantrag
 NEIN → Standard-Anfechtungsklage
 NEIN → Ist eine Handlung (Genehmigung) abgelehnt?
 JA → Verpflichtungsklage § 42 Abs. 1 Alt. 2 VwGO
 NEIN → Feststellungsklage § 43 VwGO (Rechtsverhaeltnis)
 Norm angreifbar? → Normenkontrolle § 47 VwGO (OVG)
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Klage gegen BImSchG-Genehmigung | Klageschrift nach Schema; Template unten |
| Variante A — Genehmigung auf Antrag von Mandant Verteidigung noetig | Verteidigungsposition als Beigeladener; Klageschrift ist Klaeger-Template |
| Variante B — Nur bestimmte Auflagen anfechtbar nicht Gesamtgenehmigung | Teilklage; nur Auflagen angreifen |
| Variante C — Normenkontrolle als staerkerer Angriffspunkt | Normenkontrolle § 47 VwGO pruefen; oft wirkungsvoller als Einzelklage |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template: Klageschrift Anfechtung BImSchG-Genehmigung

**Adressat:** Verwaltungsgericht [ORT] — Tonfall: sachlich-juristisch

```
An das Verwaltungsgericht [ORT]

K l a g e

des/der [NAME KLAEGER], [ADRESSE]
— Klaeger/in —
Verfahrensbevollmaechtigte: [KANZLEI]

gegen

[BUNDESLAND/BEHOERDE]
— Beklagte —
beigeladen: [BETREIBER]

wegen Aufhebung einer Genehmigung nach BImSchG

A n t r a g

Der Bescheid vom [DATUM], Az. [AZ.], wird aufgehoben.

B e g r u e n d u n g

I. Sachverhalt
[BETREIBER] erhielt am [DATUM] eine Genehmigung gemaess § 4 BImSchG
für [Anlage, Ort, Kapazitaet]. Klaeger/in ist Eigentuemerinn des Grundstuecks
[Flur], ca. [X] m von der Anlage entfernt.

II. Klagebefugnis
Klaeger/in ist in drittschuetzenden Normen verletzt:
§ 5 Abs. 1 Nr. 1 BImSchG — Schutz vor schaedlichen Umwelteinwirkungen.
TA-Laerm-Richtwert Nacht 40 dB(A) wird prognostiziert ueberschritten.

III. Begruendung
1. Schallgutachten fehlerhaft: [Konkrete Maengel]
2. UVP-Pflicht (UVPG Anlage 1 Nr. [X]) verletzt; Verfahren nicht durchgefuehrt.
 § 4 UmwRG: Verfahrensfehler fuehrt ohne Kausalitaetspruefung zur Aufhebung.
3. Materieller Fehler: Nebenbestimmung Betriebszeit unzureichend.

Anlagen: Eigentumsnachweise, Schall-Gegengutachten, Lageplan
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Fristen-Ueberblick

| Schritt | Frist | Grundlage |
|---|---|---|
| Einwendungen im Verfahren | Auslegungsfrist + 2 Wochen | § 10 Abs. 3 BImSchG |
| Widerspruch | 1 Monat | § 70 VwGO |
| Klage | 1 Monat | § 74 VwGO |
| Eilantrag § 80a | Unverzueglich | — |
| Beschwerde OVG § 146 | 2 Wochen / Begruendung 1 Monat | § 146 VwGO |
| Normenkontrolle OVG | 1 Jahr ab Bekanntmachung | § 47 Abs. 2 VwGO |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- EuGH hat deutsche Praeklusion § 5 UmwRG für unionsrechtswidrig erklaert soweit sie den gerichtlichen Zugang Einzelner beschraenkt.
- Praxis: Gericht prueft Einwendungen auch wenn im Verwaltungsverfahren nicht erhoben — Chance für Klaeger.
- Aber: VG prueft Opportunitaet im Einzelfall; konservativere OVG-Linie partiell erhalten.

## Anschluss-Skills

- `eilantrag-80-abs-5-vwgo` — Eilrechtsschutz bei Genehmigung
- `fachanwalt-verwaltungsrecht-drittanfechtung-umwelt` — Drittanfechtungs-Strategie
- `klimaklagen-verbandsklage-umwrg` — Verbandsklage UmwRG
- `fachanwalt-verwaltungsrecht-normenkontrolle-47-vwgo` — Normenkontrolle

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

