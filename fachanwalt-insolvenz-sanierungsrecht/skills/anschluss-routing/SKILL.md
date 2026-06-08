---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Insolvenz Sanierungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `eroeffnung-fachanwalt-fao-glaeubigerantrag-inso` — Eroeffnung Fachanwalt Fao Glaeubigerantrag Inso
- `fa-schuldschein` — Fa Schuldschein
- `glaeubigerantrag-insolvenzanfechtung-orientierung` — Glaeubigerantrag Insolvenzanfechtung Orientierung
- `glaeubigerverhandlung-sanierung-idw-s6-krypto-verwertung` — Glaeubigerverhandlung Sanierung Idw S6 Krypto Verwertung
- `inso-insanw-eigenverwaltung-konzerninsolvenz-koordination` — Inso Insanw Eigenverwaltung Konzerninsolvenz Koordination
- `inso-kommunikation-glaeubiger-p002-amtsgericht-p003-ortliche` — Inso Kommunikation Glaeubiger P002 Amtsgericht P003 Ortliche
- `inso-livecheck-fristennotiz-sanierungsrecht-p104-fixgeschafte` — Inso Livecheck Fristennotiz Sanierungsrecht P104 Fixgeschafte
- `inso-p001-ziele-p003c-zustandigkeit-p004a-stundung-p005-p011` — Inso P001 Ziele P003c Zustandigkeit P004a Stundung P005 P011
- `inso-p003d` — Inso P003d
- `inso-p003e-unternehmensgruppe-p004b-ruckzahlung-p004c-aufhebung` — Inso P003e Unternehmensgruppe P004b Ruckzahlung P004c Aufhebung
- `inso-p020-auskunfts-p021-anordnung-p022-rechtsstellung-p022a` — Inso P020 Auskunfts P021 Anordnung P022 Rechtsstellung P022a
- `inso-p040-unterhaltsanspruche-p041-nicht-p042-auflosend-p044` — Inso P040 Unterhaltsanspruche P041 Nicht P042 Auflosend P044
- `inso-p054-kosten-p088-vollstreckung-p095-eintritt-p121-p124` — Inso P054 Kosten P088 Vollstreckung P095 Eintritt P121 P124
- `inso-p061-nichterfullung-p062-verjahrung-p063-vergutung-p064` — Inso P061 Nichterfullung P062 Verjahrung P063 Vergutung P064

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Insolvenz Sanierungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Insolvenz- und Sanierungsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 26 StaRUG
- § 49 StaRUG
- § 25 StaRUG
- § 31 StaRUG
- § 29 StaRUG
- § 9 StaRUG
- § 23 EStG
- § 4-65 StaRUG
- § 73 StaRUG
- § 64 StaRUG
- § 7 StaRUG
- § 8 StaRUG

### Leitentscheidungen

- BGH IX ZR 122/23
- BGH IX ZR 129/22
- BGH IX ZR 239/22
- BGH IX ZR 127/24
- BGH II ZR 206/22

