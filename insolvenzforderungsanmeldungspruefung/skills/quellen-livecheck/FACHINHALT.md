---
name: quellen-livecheck
description: "Für Rechtsquellen-Livecheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Insolvenzforderungsanmeldungsprüfung."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Insolvenzforderungsanmeldungspruefung** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `aktenanlage-batchregister` — Aktenanlage Batchregister
- `beleg-und-urkundencheck` — Beleg und Urkundencheck
- `bestreiten-interessen-betrag` — Bestreiten Interessen Betrag
- `bestreiten-mehrparteien-konflikt-und-interessen` — Bestreiten Mehrparteien Konflikt und Interessen
- `betrag-behoerden-gericht-und-registerweg` — Betrag Behoerden Gericht und Registerweg
- `dubletten-serienforderungen` — Dubletten Serienforderungen
- `feststellung-forderungsgrund-rang-grund` — Feststellung Forderungsgrund Rang Grund
- `forderungsanmeldung-mandantenkommunikation-redteam-qualitygate` — Forderungsanmeldung Mandantenkommunikation Redteam Qualitygate
- `vbuh-verhandlung-vergleich-und-eskalation` — Forderungsanmeldung Vbuh Verhandlung Vergleich Eskalation
- `forderungsgrund-rang-und-belegpruefung` — Forderungsgrund Rang und Belegpruefung
- `formalpruefung-174` — Formalpruefung 174
- `grund-betrag-zinsen` — Grund Betrag Zinsen
- `grund-risikoampel-und-gegenargumente` — Grund Risikoampel und Gegenargumente
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (§ 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Pr) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Insolvenzforderungsanmeldungspruefung (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
