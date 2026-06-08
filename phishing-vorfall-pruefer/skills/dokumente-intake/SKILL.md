---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Phishing Vorfall Prüfer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `675u-675w-banking` — 675u 675w Banking
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `arbeitnehmer-haftung-bgb-675u-phish-ceo` — Arbeitnehmer Haftung Bgb 675u Phish Ceo
- `aufsicht-bafin-bank-strategie-banking-app` — Aufsicht Bafin Bank Strategie Banking App
- `bankpflichten-beweislast-beweislast-bgb` — Bankpflichten Beweislast Beweislast Bgb
- `bea-notfall-bgb-675v-erstkontakt-mandant` — Bea Notfall Bgb 675v Erstkontakt Mandant
- `call-interessen-faelle-freistehender` — Call Interessen Faelle Freistehender
- `grobe-online-phishing` — Grobe Online Phishing
- `klage-fristennotiz-vorfall-phish-banking` — Klage Fristennotiz Vorfall Phish Banking
- `phish-incident-phish-meldepflichten-arten-erkennen` — Phish Incident Phish Meldepflichten Arten Erkennen
- `phishing-faelle-rentner-kryptowaehrung-recovery-geschaeftskonto` — Phishing Faelle Rentner Kryptowaehrung Recovery Geschaeftskonto
- `phishing-praeventionscheckliste-strafanzeige-vorbereiten-supply` — Phishing Praeventionscheckliste Strafanzeige Vorbereiten Supply
- `spoofing` — Spoofing
- `versicherer-cyber-phishing-vorfall-zivilklage-bank` — Versicherer Cyber Phishing Vorfall Zivilklage Bank

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
