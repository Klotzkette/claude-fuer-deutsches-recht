---
name: dokumente-intake
description: "Dokumentenintake für Fachanwalt Migrationsrecht: sortiert Bescheid BAMF/ABH, Pass, Aufenthaltstitel, prüft Datum, Absender, Frist und Beweiswert (Identitätsnachweise, Sprachzeugnisse); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Migrationsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Migrationsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abschiebehaft-paragraf-62-aufenthg` — Abschiebehaft Paragraf 62 Aufenthg
- `einstieg-schnelltriage-fallrouting` — Abschiebungsabwehr Sofort Arbeitgeber
- `arbeitgeberwechsel` — Arbeitgeberwechsel Asyl Anhoerung Asylg
- `asylantrag-folgeverfahren-paragraf-71-asylg` — Asylantrag Folgeverfahren Paragraf 71 Asylg
- `aufenthalt-paragraf-25a-aufenthg` — Aufenthalt Paragraf 25A Aufenthg
- `aufenthaltstitel-antrag` — Aufenthaltstitel
- `workflow-aufenthaltstitel-router` — Aufenthaltstitel Ausweisung Start
- `aufenthaltstitel-pruefung` — Aufenthaltstitel Erstgespraech Mandatsannahme
- `ausweisung-paragrafe-53-55-aufenthg` — Ausweisung Paragrafe 53 55 Aufenthg
- `ba-zustimmung-beschaeftigung` — BA Zustimmung Beschäftigungsduldung
- `blaue-karte-eu-mobilitaet` — Blaue Karte Bleiberecht 25A Chancenaufenthalt
- `workflow-botschaft-visumtermin` — Botschaft Visumtermin Dokumentenstapel
- `datenschutz-sicherheit-migration` — Datenschutz Sicherheit Daueraufenthalt EU
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Migrationsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
