---
name: dokumente-intake
description: "Dokumentenintake für Zwangsvollstreckung: sortiert Vollstreckungstitel, Pfändungs- und Überweisungsbeschluss (PfÜB), Gerichtsvollzieher-Protokoll, prüft Datum, Absender, Frist und Beweiswert (Titel mit Klausel, Zustellungsnachweis); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Zwangsvollstreckung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `765a-fehlerkatalog` — 765a Fehlerkatalog
- `802l-verhandlung-vergleich-und-eskalation` — 802l Verhandlung Vergleich und Eskalation
- `abwehr-schuldner` — Abwehr Schuldner
- `arbeit-schriftsatz-brief-und-memo-bausteine` — Arbeit Schriftsatz Brief und Memo Bausteine
- `bank-haertefall-inso` — Bank Haertefall Inso
- `elektronische-zustellung-eu` — Elektronische Zustellung EU
- `eu-kontenpfaendung-655-2014` — EU Kontenpfaendung 655 2014
- `haertefall-mandantenkommunikation-entscheidungsvorlage` — Haertefall Mandantenkommunikation Entscheidungsvorlage
- `inso-internationaler-bezug-und-schnittstellen` — Inso Internationaler Bezug und Schnittstellen
- `kommandocenter` — Kommandocenter
- `kontenpfaendung-notar-interessen-online` — Kontenpfaendung Notar Interessen Online
- `kontensuche-drittschuldner` — Kontensuche Drittschuldner
- `kontensuche-quellenkarte` — Kontensuche Quellenkarte
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Zwangsvollstreckung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: ZPO, § 201 InsO, ZVG, EU, § 765a H, § 800 ZPO Notar,, § 802l Kontensuche, Verm, §§ 704 ff — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Gläubiger.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
