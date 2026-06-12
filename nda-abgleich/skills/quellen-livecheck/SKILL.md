---
name: quellen-livecheck
description: "Quellen-Live-Check für NDA-Abgleich: prüft Normen (BGB §§ 145 ff., 280/339, GeschGehG, DSGVO Art. 28) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Nda Abgleich** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `aenderungsmodus-compliance-dokumentation` — Änderungsmodus Compliance Dokumentation
- `aenderungsmodus-compliance-dokumentation-und-akte` — Änderungsmodus Compliance Dokumentation und Akte
- `ampelmatrix-internationaler-bezug-schnittstellen` — Ampelmatrix Internationaler Bezug Schnittstellen
- `ampelmatrix-internationaler-bezug-und-schnittstellen` — Ampelmatrix Internationaler Bezug und Schnittstellen
- `arbeitnehmer-kuendigung` — Arbeitnehmer Kuendigung
- `ausgabe-changes-docx-beweislast` — Ausgabe Changes Docx Beweislast
- `ausgabe-mandantenkommunikation-entscheidungsvorlage` — Ausgabe Mandantenkommunikation Entscheidungsvorlage
- `changes-abschlussprodukt-uebergabe` — Changes Abschlussprodukt Übergabe
- `changes-abschlussprodukt-und-uebergabe` — Changes Abschlussprodukt und Übergabe
- `chirurgisch-quellenkarte` — Chirurgisch Quellenkarte
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `docx-beweislast-darlegungslast` — Docx Beweislast Darlegungslast
- `docx-beweislast-und-darlegungslast` — Docx Beweislast und Darlegungslast
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (GehG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Nda Abgleich (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 305 BGB (AGB-Begriff)
- § 305c BGB (überraschende Klauseln)
- § 307 BGB (Inhaltskontrolle)
- § 90 HGB (Geschäftsgeheimnisse)
- GeschGehG (Geschäftsgeheimnisgesetz)

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
