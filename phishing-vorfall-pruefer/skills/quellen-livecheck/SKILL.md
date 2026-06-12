---
name: quellen-livecheck
description: "Quellen-Live-Check für Phishing-Vorfall-Prüfer: prüft Normen (DSGVO Art. 33 Meldung, NIS2, § 8b BSIG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BSI und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Phishing Vorfall Prüfer** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

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
- `faelle-abschlussprodukt-und-uebergabe` — Faelle Abschlussprodukt und Übergabe
- `fahrlaessigkeit-fehlerkatalog` — Fahrlaessigkeit Fehlerkatalog
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (BGB, § 675u,, § 675v,, § 675w, pushTAN, Call) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Phishing Vorfall Prüfer (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
