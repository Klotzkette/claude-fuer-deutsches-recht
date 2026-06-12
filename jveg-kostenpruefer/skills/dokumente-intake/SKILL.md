---
name: dokumente-intake
description: "Dokumentenintake für JVEG-Kostenprüfer: sortiert SV-Rechnung, Reisekostenabrechnung, Stundennachweise, prüft Datum, Absender, Frist und Beweiswert (Aktennotizen, Reiseplanung); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Jveg Kostenpruefer** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Jveg Kostenpruefer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aktenstripper` — Aktenstripper
- `anspruchsberechtigung-antragsgenerator` — Anspruchsberechtigung Antragsgenerator
- `antragsgenerator` — Antragsgenerator
- `belegfeste-formular-portal-und-einreichung` — Belegfeste Formular Portal und Einreichung
- `beschwerde-dolmetscher-sonderfall` — Beschwerde Dolmetscher Sonderfall
- `dolmetscher-sonderfall-und-edge-case` — Dolmetscher Sonderfall und Edge Case
- `dolmetscher-uebersetzer` — Dolmetscher Übersetzer
- `dolmetscher-uebersetzer-fahrtkosten` — Dolmetscher Übersetzer Fahrtkosten
- `dolmetscherkosten-zahlen-schwellen-und-berechnung` — Dolmetscherkosten Zahlen Schwellen und Berechnung
- `fahrtkosten` — Fahrtkosten
- `fahrtkosten-festsetzung-interessen` — Fahrtkosten Festsetzung Interessen
- `festsetzung-beschwerde` — Festsetzung Beschwerde
- `festsetzung-mehrparteien-konflikt-und-interessen` — Festsetzung Mehrparteien Konflikt und Interessen
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Jveg Kostenpruefer-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: JVEG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
