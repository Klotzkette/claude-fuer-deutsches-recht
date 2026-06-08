---
name: dokumente-intake
description: "Dokumentenintake für Phishing-Vorfall-Prüfer: sortiert Vorfallsbericht, Logs, Bank-Korrespondenz, prüft Datum, Absender, Frist und Beweiswert (Mail-Forensik, Server-Logs); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Phishing Vorfall Prüfer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `675u-675w-banking` — 675u 675w Banking
- `675v-quellenkarte` — 675v Quellenkarte
- `675w-zahlen-schwellen-und-berechnung` — 675w Zahlen Schwellen und Berechnung
- `arbeitnehmer-haftung-bgb-675u-phish-ceo` — Arbeitnehmer Haftung BGB 675u Phish CEO
- `aufsicht-bafin-bank-strategie-banking-app` — Aufsicht Bafin Bank Strategie Banking APP
- `banking-behoerden-gericht-und-registerweg` — Banking Behoerden Gericht und Registerweg
- `bankpflichten-beweislast-bgb` — Bankpflichten Beweislast BGB
- `bea-notfall-bgb-675v-erstkontakt-mandant` — BEA Notfall BGB 675v Erstkontakt Mandant
- `beweislast-mandantenkommunikation-entscheidungsvorlage` — Beweislast Mandantenkommunikation Entscheidungsvorlage
- `bgb-schriftsatz-brief-und-memo-bausteine` — BGB Schriftsatz Brief und Memo Bausteine
- `call-interessen-faelle-freistehender` — Call Interessen Faelle Freistehender
- `faelle-abschlussprodukt-und-uebergabe` — Faelle Abschlussprodukt und Uebergabe
- `fahrlaessigkeit-fehlerkatalog` — Fahrlaessigkeit Fehlerkatalog
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Phishing Vorfall Pruefer-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB, § 675u,, § 675v,, § 675w, pushTAN, Call — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Geschädigtes Unternehmen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
