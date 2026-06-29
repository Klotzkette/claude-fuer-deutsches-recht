---
name: kaltstart-interview
description: "Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter / beratender Anwalt / Geschäftsleiter / Sanierungsberater / Wirtschaftsprüfer), ty..."
---

# /insolvenzrecht:insolvenzrecht-kaltstart-interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/insolvenzrecht:insolvenzrecht-kaltstart-interview` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung anzeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft die Konnektoren-Verfügbarkeit (Dokumentenspeicher, Forderungsanmeldung-Portal, Insolvenzbekanntmachungen-RSS, Buchhaltungs-MCP). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen: nur `✓` melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `⚪` markieren.

---

## Kaltstart-Interview: Insolvenzrecht

### 1. Wer nutzt dieses Plugin?

- **Rolle:** Insolvenzverwalter (§ 56 InsO) / Sachwalter (§ 274 InsO) / Sanierungsmoderator (§ 94 StaRUG) / beratender Anwalt (Schuldner- oder Gläubigerseite) / Geschäftsleiter mit Antragspflicht (§ 15a InsO) / Sanierungsberater (außerhalb gerichtlicher Verfahren) / Wirtschaftsprüfer mit Insolvenzmandaten?
- **Anwaltlicher Ansprechpartner** (bei Nicht-Anwälten): Name, Kanzlei, Erreichbarkeit
- **Berufsverband:** VID (Verband Insolvenzverwalter), Gravenbrucher Kreis, DRSC, IDW, sonstige

### 2. Typische Mandate / Verfahren

- **Verfahrensarten:** Regelinsolvenz / Eigenverwaltung (§§ 270 ff. InsO) / Schutzschirmverfahren (§ 270d InsO) / StaRUG / Restrukturierungsbeauftragter / Konzerninsolvenzen / Verbraucherinsolvenz
- **Branchen-Schwerpunkte** (falls vorhanden): Baugewerbe / Handel / Dienstleistung / Industrie / Immobilien / Healthcare
- **Volumen** (für Sanierungsberater): typische Bilanzsumme der Mandanten

### 3. Gutachten- und Berichtsstandards

- **IDW S 6** (Sanierungskonzept): wird verwendet ja / nein
- **IDW S 9** (Anforderungen an Insolvenzpläne): ja / nein
- **IDW S 11** (Beurteilung Insolvenzeröffnungsgründe): ja / nein
- **Eigene Hausstandards:** zusätzliche Templates, Checklisten, Berichtsstrukturen

### 4. Zuständige Insolvenzgerichte

- **Hauptzuständigkeiten:** AG/LG nach Bezirk; bei Konzerninsolvenzen: § 3a InsO (Gruppen-Gerichtsstand)
- **Bekanntmachungen:** insolvenzbekanntmachungen.de — wird regelmäßig überwacht?

### 5. Antragspflicht-Prüfung

- **Wann konsultiert das Mandat / der Geschäftsleiter typischerweise:** schon bei drohender Zahlungsunfähigkeit (§ 18 InsO) / erst bei Zahlungsunfähigkeit (§ 17 InsO) / erst bei Überschuldung (§ 19 InsO)
- **Standard für Fortbestehensprognose:** 12 Monate (§ 19 Abs. 2 InsO) / Branchenstandard / einzelfallabhängig
- **3-Wochen-Frist (§ 15a InsO):** Eskalationspfad bei Annäherung

### 6. Vergütung

- **InsVV-Anwendung:** Regelvergütung nach §§ 1 ff. InsVV / Vergütungsvereinbarung mit Gericht
- **Honorarberatung:** Stundensatz / RVG / Pauschalen

### 7. Standort

- **Bundesland / Hauptgerichtsbezirk:** [Bayern / NRW / etc.]
- **Kanzleitypus:** Einzelkanzlei / Sozietät / Großkanzlei / Inhouse

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde
- Welche Skills jetzt sinnvoll als nächstes laufen können:
 - `/insolvenzrecht:zahlungsunfähigkeit-prüfung-17-inso` — bei Liquiditätsengpässen
 - `/insolvenzrecht:überschuldung-prüfung-19-inso` — bei bilanzieller Überschuldung mit Fortbestehensprognose
 - `/insolvenzrecht:antragspflicht-15a-inso` — bei drohender 3-Wochen-Frist
 - `/insolvenzrecht:gläubigerantrag-prüfung` — bei eingegangenem Gläubigerantrag
 - `/insolvenzrecht:liquiditätsvorschau-insolvenzrechtlich` — für 21-Tage-Liquiditätsstatus
- Hinweis auf Mandatsgeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB)

## Rechtlicher Rahmen

- **InsO** — Insolvenzordnung: §§ 15a, 17, 18, 19, 56, 270 ff. (Eigenverwaltung), 286 ff. (Restschuldbefreiung)
- **StaRUG** — Unternehmensstabilisierungs- und -restrukturierungsgesetz (seit 01.01.2021)
- **InsVV** — Insolvenzrechtliche Vergütungsverordnung
- **IDW-Standards:** S 6 (Sanierungskonzept), S 9 (Insolvenzplan), S 11 (Insolvenzeröffnungsgründe)
- **Maßgebliche Rspr.:** BGH IX. Zivilsenat (Insolvenz) und II. Zivilsenat (Gesellschaftsrecht/Geschäftsleiterhaftung)

## Hinweise

Dieses Plugin ersetzt keine anwaltliche Beratung. Zitate aus Trainingsdaten sind vor Verwendung gegen Primärquellen (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang) zu prüfen. Insolvenzantragspflicht und Eröffnungsgründe sind hochkomplex; im Zweifel **immer** anwaltliche Begleitung.

## Rechtlicher Rahmen — Kaltstart-Orientierung (Stand Mai 2026)

- § 15a InsO (Antragspflicht 3 Wo. ZU / 6 Wo. Überschuldung), §§ 17–19 InsO (Eröffnungsgründe), §§ 129 ff. InsO (Anfechtung), §§ 174 ff. InsO (Forderungsanmeldung), §§ 270 ff. InsO (Eigenverwaltung / Schutzschirm), §§ 4 ff. StaRUG.
- Aktuelle BGH-Linie (vor Ausgabe über dejure.org / openjur.de verifizieren):
 - **BGH IX ZR 122/23 vom 05.12.2024** (Unlauterkeit Bargeschäft § 142 InsO).
 - **BGH IX ZR 129/22 vom 18.04.2024** (Vorsatzanfechtung § 133 InsO; konkrete Bedrohungslage).
 - **BGH II ZR 206/22 vom 23.07.2024** (Fortwirkende Haftung ausgeschiedener GF).
 - **BGH IV ZR 66/25 vom 19.11.2025** (D&O-Wissentlichkeitsausschluss).
 - **BGH 5 StR 287/24 vom 27.02.2025** (Faktischer GF).
 - **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard — Aktionärsforderungen nachrangig).
 - **BVerfG 1 BvR 418/25 vom 28.02.2025** (StaRUG / VARTA).
