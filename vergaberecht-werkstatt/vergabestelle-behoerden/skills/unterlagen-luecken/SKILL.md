---
name: unterlagen-luecken
description: "Auf Auftraggeberseite: Lücken- und Beschaffungsliste für Vergaberecht: trennt fehlende Tatsachen von fehlenden Belegen (Vergabeunterlagen, Angebot, Wertungsvermerk), nennt pro Lücke Beweisthema, Beschaffungsweg (Vergabekammer Bund/Länder), Frist und Ersatznachweis."
---

# Vergabeakte: Unterlagen- und Beleglücken schließen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Einsatzlage

Diese Prüfung baut aus dem vorhandenen Projektordner eine belastbare Vergabeakte. Sie unterscheidet fehlendes Dokument, fehlende Tatsachengrundlage, fehlende Freigabe, unlesbares Format und widersprüchliche Version. Das Ergebnis ist ein ausführbarer Arbeitsauftrag an die konkret zuständige Stelle.

## Fachlandkarte dieses Plugins

- `dokumente-intake` — Aktenstart und Unterlageninventar.
- `workflow-unterlagen-lueckenliste` — fehlende Vergabeunterlagen, Wertungsbelege, Portalprotokolle und Freigaben als Arbeitsauftrag.
- `vergabeunterlagen-lv-datenformate-bereitstellen` — LV, GAEB, XML, Excel, PDF und Lesefassung bereitstellen.
- `eforms-ted-bekanntmachung-check` und `bekanntmachung-berichtigung-und-upload-routing` — Bekanntmachungs- und Uploadlücken.
- `legacy-systeme-integration` und `wirklichkeitsdaten-beschaffung-steuern` — Quellsysteme, Datenqualität und Fachfreigabe.
- `bestangebot-durchsetzen`, `10-zuschlagsmatrix-aufbauen` und `18-wertungsvermerk-erstellen` — Wertungs- und Dokumentationslücken.
- `22-ruegeerwiderung`, `23-stellungnahme-vergabekammer` und `26-akteneinsicht-vergabekammer` — Lücken im Streitfall schließen.
- `12-ausschlussgruende-pruefen` und `wettbewerbsregister-abfrage-selbstreinigung` — Ausschluss-, Register- und Selbstreinigungsbelege.

## Arbeitsweg

1. Sollkatalog aus Phase und Regime bilden: Bedarfs- und Budgetfreigabe, Auftragswert, Markterkundung, Verfahrenswahl, Bekanntmachung, Unterlagen, Kommunikation, Öffnung, Eignung, Aufklärung, Wertung, §-134-Information, Zuschlag und Vertragsänderung.
2. Istbestand nach Originaldatei, Version, Ersteller, Datum, Freigabe, Quellsystem, Format und Beweisthema erfassen.
3. Jede Lücke klassifizieren: `Dokument fehlt`, `Inhalt fehlt`, `Quelle unklar`, `Version widersprüchlich`, `Format nicht prüfbar`, `Entscheidung nicht begründet` oder `Versandbeleg fehlt`.
4. Priorität festlegen: rote Frist- oder Zuschlagssperre, gelbe Wertungs-/Beweisrelevanz, grüne Komfortergänzung.
5. Arbeitsauftrag an Bedarfsträger, Zentrale Vergabestelle, Haushalt, IT, Datenschutz, Fachplaner, Plattformbetreiber oder externe Beratung formulieren: Dokument, Beweisthema, Originalquelle, zulässiger Beschaffungsweg, Termin und Ersatzbeleg.
6. Keine fehlende Aktenbegründung nachträglich als damalige Erwägung ausgeben. Eine zulässige Ergänzung muss als spätere Erläuterung gekennzeichnet und auf zeitgenössische Unterlagen gestützt werden.

## Pflichtmatrix

| ID | Phase | fehlender Gegenstand | Beweisthema | Quelle/Eigentümer | Format | Fristfolge | Ersatzbeleg | Status |
|---|---|---|---|---|---|---|---|---|
| L-01 | [Phase] | [Dokument oder Inhalt] | [Tatbestandsmerkmal] | [Stelle/System] | [Originalformat] | [Norm und Termin] | [falls zulässig] | rot/gelb/grün |

Bei Rüge oder Nachprüfung zusätzlich Aktenvorlage, Geheimniskennzeichnung und Schwärzungsvorschlag nach § 165 GWB vorbereiten. Die Vergabekammer erhält die entscheidungserhebliche Vergabeakte; allgemeine Akteneinsichtsnormen anderer Verfahrensordnungen nicht als Ersatz verwenden.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Bei Zeitdruck zuerst Zuschlagssperre, Rechtsbehelfsfrist, Portalzugang, Wertungsmaßstab und Originalbeleg sichern.
- Die Ausgabe endet mit einem versandfertigen Arbeitsauftrag und einer Entscheidung, ob das Verfahren bis zur Schließung der roten Lücke fortgesetzt werden darf.
