---
name: dokumente-intake
description: "Dokumentenintake für Mietrecht (Wohnraum/Gewerbe): sortiert Mietvertrag, Nebenkostenabrechnung, Mängelanzeige, prüft Datum, Absender, Frist und Beweiswert (Mängelfotos, Mietspiegel); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Mietrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `amtlichen-amtsgericht-sonderfall` — Amtlichen Amtsgericht Sonderfall
- `amtsgericht-sonderfall-und-edge-case` — Amtsgericht Sonderfall und Edge Case
- `ausschliesslich-dokumentenmatrix-und-lueckenliste` — Ausschliesslich Dokumentenmatrix und Lueckenliste
- `betriebskostenabrechnung-belege-und-formelpruefer` — Betriebskostenabrechnung Belege und Formelpruefer
- `bundesland-datenerhebung-grossstadt` — Bundesland Datenerhebung Grossstadt
- `datenerhebung-zahlen-schwellen-und-berechnung` — Datenerhebung Zahlen Schwellen und Berechnung
- `eigenbedarfskuendigung-erstellen` — Eigenbedarfskuendigung Erstellen
- `erstellung-fehlerkatalog` — Erstellung Fehlerkatalog
- `grossstadt-mietspiegel-und-kappung` — Grossstadt Mietspiegel und Kappung
- `klageentwurf-amtsgericht-miet-gewerbemiete` — Klageentwurf Amtsgericht Miet Gewerbemiete
- `klageentwurf-beweislast-und-darlegungslast` — Klageentwurf Beweislast und Darlegungslast
- `lage-ausstattung-mahnung-zahlungsverzug` — Lage Ausstattung Mahnung Zahlungsverzug
- `mahnung-zahlungsverzug-mieter` — Mahnung Zahlungsverzug Mieter
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Mietvertrag, Mieterhöhungsverlangen, Mietspiegel, Nebenkostenabrechnung, Kündigungsschreiben, Modernisierungsankündigung, WEG-Protokoll, Beschlusssammlung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Mietrecht und WEG-Recht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB §§ 535, 536, 543, 558, 558a, 558b, 573, 573c, 574, 556, 556a, 556b, BetrKV, WEG §§ 24, 25, 27 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Vermieter, Mieter, Hausverwaltung, WEG-Verwaltung, Amtsgericht der Belegenheit, Mieterverein, Eigentümergemeinschaft prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Mieter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
