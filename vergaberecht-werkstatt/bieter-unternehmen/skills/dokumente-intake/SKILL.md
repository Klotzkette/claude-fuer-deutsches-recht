---
name: dokumente-intake
description: "Dokumentenintake für Vergaberecht: sortiert Vergabeunterlagen, Angebot, Wertungsvermerk, Datum, Absender, Frist, Beweiswert, Lücken, Geschäftsgeheimnisse und nächste Arbeitsschritte."
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

- `vergabe-os-master-orchestrator` — Gesamtsteuerung für Bieterfälle.
- `workflow-fristen-und-risikoampel` — rote Fristen aus Unterlagen, Portalnachrichten und Schreiben sichern.
- `unterlagen-und-lv-datenformate-auslesen` — Bekanntmachung, Unterlagen, LV, GAEB/XML/Excel/PDF und Portalexporte ordnen.
- `legacy-systeme-integration` — SAP/ERP/CRM/AVA/DMS/API/MCP als Angebots- oder Beweisquelle anbinden.
- `angebot-in-vorgegebenem-format-erstellen` — Angebots- und Nachweisdateien abgabefähig machen.
- `qualitaetsvorsprung-nachweisen` — Bestangebot trotz höherem Preis belegen.
- `21-ruegeschreiben-erstellen`, `nachpruefungsantrag-powerdraft` und `nachpruefungsverfahren-vk` — Rüge, VK und laufender Rechtsschutz.
- `eignungspruefung`, `08-bietergemeinschaft-bildung`, `17-bietergemeinschaftserklaerung` und `wettbewerbsregister-abfrage-selbstreinigung` — Eignung, Ausschluss, Nachforderung und Selbstreinigung.
- `vergabekammer-verhandlung-vergleich-und-eskalation` und `olg-vergabesenat-beschwerdebriefing` — Termin, Vergleich und OLG.

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Vergaberecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Geschäftsgeheimnisschutz behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Bieterteam, Vergabestelle, zuständigem Gericht oder Behörde, etwaigen Sachverständigen oder beauftragten Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
