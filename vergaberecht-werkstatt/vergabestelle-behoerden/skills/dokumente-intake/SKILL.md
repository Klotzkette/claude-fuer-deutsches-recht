---
name: dokumente-intake
description: "Dokumentenintake für Vergaberecht: sortiert Vergabeakte, Unterlagen, Angebote, Wertungsvermerk, Datum, Absender, Frist, Beweiswert, Lücken und Geschäftsgeheimnisse."
---

# Dokumentenintake

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Aktenstart statt Formularstart

Wenn zu Dokumente Intake bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwürfe vorliegen, lies diese zuerst aus. Bilde für Vergaberecht eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und nächstem sinnvollen Output. Frage nicht routinemäßig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rückmeldung:

```text
Ich habe aus der Akte vorläufig erkannt: [...]
Unsicher sind noch: [...]
Als nächsten Schritt schlage ich vor: [...]
```

Stelle danach höchstens drei Rückfragen und nur zu echten Lücken oder Widersprüchen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für Vergaberecht ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `vergabe-os-master-orchestrator` — Gesamtsteuerung für Vergabestellenfälle.
- `workflow-fristen-und-risikoampel` — rote Fristen aus Akte, Portal und Schreiben sichern.
- `workflow-chronologie-und-belegmatrix` — Vergabeakte, Portalprotokolle, Entscheidungen und Belege ordnen.
- `unterlagen-luecken` und `workflow-unterlagen-lueckenliste` — fehlende Unterlagen, Nachweise und Aktenstellen.
- `eforms-ted-bekanntmachung-check` — Bekanntmachung, CPV, Unterlagenlink, Fristen, eForms/TED/DVAL.
- `legacy-systeme-integration` und `wirklichkeitsdaten-beschaffung-steuern` — Datenquellen, Bauwerks-/Zustands-/Kosten-/BIM-Daten und Systemanschluss.
- `bestangebot-durchsetzen`, `10-zuschlagsmatrix-aufbauen` und `18-wertungsvermerk-erstellen` — Bestwertungsentscheidung und Dokumentation.
- `22-ruegeerwiderung`, `23-stellungnahme-vergabekammer`, `26-akteneinsicht-vergabekammer` und `24-vorlage-an-den-vergabesenat` — Streitführung.

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Vergaberecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach DSGVO und Geschäftsgeheimnisschutz behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Vergabekammer, Vergabesenat, Bietern, Beigeladenen, Aufsicht oder beauftragten Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
