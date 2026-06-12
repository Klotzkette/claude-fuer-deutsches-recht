---
name: quellen-livecheck
description: "Quellen-Live-Check für Vertragsrecht (BGB-Vertragsrecht): prüft Normen (BGB §§ 145 ff., 305 ff., HGB §§ 343 ff.) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Zivilgerichte und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Vertragsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `abmahnung-uwg` — Abmahnung UWG
- `aenderungs-historie-agb-eskalations-marker` — Änderungs Historie AGB Eskalations Marker
- `agb-pruefung` — AGB Prüfung
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `bgb-business-einzelabrufe-sonderfall` — BGB Business Einzelabrufe Sonderfall
- `business-compliance-dokumentation-und-akte` — Business Compliance Dokumentation und Akte
- `einzelabrufe-sonderfall-und-edge-case` — Einzelabrufe Sonderfall und Edge Case
- `eskalations-marker` — Eskalations Marker
- `eskalations-quellenkarte` — Eskalations Quellenkarte
- `fernabsatz-lieferanten-red-team` — Fernabsatz Lieferanten RED Team
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `fristennotiz-naechster-vertriebsvertraege` — Fristennotiz Naechster Vertriebsvertraege
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Tragende Normen (BGB §§ 116–144, 145–157, 158–163, 195, 199, 241, 242, 249, 254, 273, 275, 276, 280, 281, 282, 284, 286, 288, 305–310, 311, 311a, 311b, 313, 314, 320, 323, 324, 339–345, 433 ff., 535 ff., 631 ff., 651a ff., 765 ff., 812 ff., 823 ff.) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Vertragsrecht (BGB Allgemeiner Teil und Schuldrecht) (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
