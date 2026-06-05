# Insolvenzrecht-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`insolvenzrecht`) | [`insolvenzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |
| **Sanierungsgewinn im Insolvenzplan — Grossbach Druckguss & Präzision GmbH & Co. KG Erfurt (2026)** (`sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026/gesamt-pdf/sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026.zip) |
| **Sanierungsgewinn bei solventer GmbH-Liquidation — Strassburger Handelshof GmbH (Berlin-Charlottenburg)** (`sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026/gesamt-pdf/sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026.zip) |
| **Sanierungsgewinn im StaRUG-Plan — Pellbach Windenergie GmbH Brandenburg (2026)** (`sanierungsgewinn-starug-plan-windenergie-pellbach-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-starug-plan-windenergie-pellbach-2026/gesamt-pdf/sanierungsgewinn-starug-plan-windenergie-pellbach-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-starug-plan-windenergie-pellbach-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-starug-plan-windenergie-pellbach-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Insolvenz- und sanierungsrechtliche Skills nach deutschem Recht (InsO, StaRUG, COVInsAG-Nachwirkungen). Zielgruppe: Insolvenzverwalter, beratende Rechtsanwälte (Insolvenz-/Sanierungsrecht), Geschäftsführer, Vorstände, Sanierungsberater, Wirtschaftsprüfer (IDW-S-11-/S-6-/S-9-Praxis).


## Enthaltene Skills

| Skill | Zweck |
|---|---|
| `zahlungsunfaehigkeit-pruefung-17-inso` | Prüfung der Zahlungsunfähigkeit gem. § 17 InsO anhand BGH-Liquiditätsstatus (10%-/3-Wochen-Schwelle) |
| `ueberschuldung-pruefung-19-inso` | Zweistufige Überschuldungsprüfung gem. § 19 InsO: Fortbestehensprognose + insolvenzrechtlicher Überschuldungsstatus |
| `liquiditaetsvorschau-insolvenzrechtlich` | Rollierende 13-/26-/52-Wochen-Liquiditätsvorschau mit Ampel als Beweismittel für § 17 InsO und Fortbestehensprognose § 19 InsO; Excel-Export |
| `antragspflicht-15a-inso` | Höchstfrist nach § 15a InsO, Haftung bei Insolvenzverschleppung, Schutz Geschäftsführer/Vorstand |
| `glaeubigerantrag-pruefung` | Prüfung Zulässigkeit/Begründetheit eines Gläubigerantrags (§ 14 InsO), Glaubhaftmachung Forderung + Eröffnungsgrund |

## Abgrenzung zu den Schwester-Plugins

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Dieses Plugin `insolvenzrecht` ist **gerichtsfähig-formal** ausgerichtet: Es liefert die rechtlichen Subsumtionsbausteine und Beweismittel, wenn die Krise bereits eingetreten ist — Zeitpunkt der Zahlungsunfähigkeit, Überschuldungsstatus zum Stichtag, Antragspflichtfrist, Haftung Geschäftsleiter.

## Rechtlicher Rahmen (übergreifend)

- **InsO**: §§ 14, 15, 15a, 16, 17, 18, 19, 130, 131, 133, 142
- **StaRUG**: §§ 29 ff. (Restrukturierungsverfahren), § 102 (Hinweispflicht)
- **GmbHG**: § 64 a.F. (ersetzt durch § 15b InsO), § 30 (Auszahlungsverbot)
- **AktG**: § 92 Abs. 2 (Anzeigepflichten), § 93 (Sorgfaltspflicht)
- **HGB**: § 252 Abs. 1 Nr. 2 (going concern)
- **StGB**: §§ 283–283d (Bankrott, Verletzung der Buchführungspflicht), § 266a (Vorenthalten Arbeitsentgelt)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Lizenz

Doppellizenziert unter Apache License, Version 2.0 ODER MIT License, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`). Siehe `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT` und `NOTICE` im Repository-Wurzelverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfechtungsrechte-antragspflicht-15a` | Anfechtungsrechte Prüfen, Antragspflicht 15a Inso, Auslaendischer Insolvenzverwalter Register Und Grundbuch, Forderungsanmeldung Glaeubiger 174 177 Inso: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundla... |
| `feststellung-sonderfall-glaeubigerantrag-inso` | Feststellung Sonderfall Und Edge Case, Glaeubigerantrag Risikoampel Und Gegenargumente, Inso Schriftsatz Brief Und Memo Bausteine, Insolvenzrecht Behörden Gericht Und Registerweg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit... |
| `glaeubigerantrag-glaeubigerausschuss` | Glaeubigerantrag Prüfung, Glaeubigerausschuss Mitwirkung, Inso Dsgvo Art17 Nach Restschuldbefreiung, Inso Eroeffnungsantrag Checkliste: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `glaeubigerausschuss-fristennotiz` | Glaeubigerausschuss Fristennotiz Und Naechster Schritt, Ueberschuldung Fristen Form Und Zustaendigkeit, Do Versicherung Manager Haftung, Insol Sanierungsgewinn Iv Haftung Für Versaumte 3a Iv Antraege: wählt den konkreten Prüfpfad, trennt... |
| `inso-gerichtliche-aufsichtswege` | Inso Gerichtliche Und Aufsichtswege Schufa, Inso Glaeubigerausschuss Praxis, Inso Glaeubigerausschuss Zustimmung Spezial, Inso Insolvenzbekanntmachungen Auskunfteien: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `inso-lma-facility-massearmut` | Inso Lma Facility Agent Und Syndikat, Inso Massearmut Massekostenmangel Spezial, Inso Negativeintrag Bestreiten Belegpaket, Inso Neustart Bonitaet Konto Kredit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |
| `inso-npl-kreditkauf-restschuldbefreiung` | Inso Npl Kreditkauf Krzwmg, Inso Restschuldbefreiung Und Versagungsgruende, Inso Schufa Restschuldbefreiung Löschung, Inso Schuldschein Darlehen In Der Insolvenz: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rech... |
| `inso-pl` | Mandantenkommunikation, Redteam Qualitygate, Inso Pl Einfuehrung Verfahrenstypen, Insol Sanierungsgewinn Finanzamt Im Insolvenzverfahren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert d... |
| `inso-tabelle-verbraucherinsolvenz-leitfaden` | Inso Tabelle Und Feststellung Spezial, Inso Verbraucherinsolvenz Leitfaden, Insol Sanierungsgewinn Rangruecktritt Und 5 Abs 2a Estg Im Plan, Insolvenzgeld 165 Sgb Iii: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `insol-sanierungsgewinn-7b-debt-equity` | Insol Sanierungsgewinn 7b Gewstg Im Insolvenzplan Paralleltrack, Insol Sanierungsgewinn Debt Equity Swap Im Plan, Insol Sanierungsgewinn Eigenverwaltung Und Cra, Insol Sanierungsgewinn Fruehe Vorbereitung Vor Plan: wählt den konkreten Pr... |
| `insol-sanierungsgewinn-insolvenzreife` | Insol Sanierungsgewinn Massehaftungsbefreiung Und Bilanz, Insolvenzreife Antragspflicht Und Haftung, Insol Sanierungsgewinn 3a Estg Im Insolvenzplan, Insol Sanierungsgewinn 3a Estg Im Starug Plan: wählt den konkreten Prüfpfad, trennt Fri... |
| `insol-sanierungsgewinn-liquidation` | Insol Sanierungsgewinn Liquidation Statt Plan Folgen, Insol Sanierungsgewinn Mandantenwarnung Iv Und Cro, Insol Sanierungsgewinn Massenpriorisierung 261 Vs 3a Estg, Insol Sanierungsgewinn Restschuldbefreiung Und 3a Estg: wählt den konkre... |
| `insol-sanierungsgewinn-uebertragende` | Insol Sanierungsgewinn Uebertragende Sanierung Asset Deal, Insol Sanierungsgewinn Vergleich Mit Finanzamt Und Stundung, Insol Sanierungsgewinn Verlustvortrag Und 3a Iii Vorab, Insol Sanierungsgewinn Verzicht Bilanz Im Plan: wählt den kon... |
| `insolvenzrecht-anschluss` | Allgemein, Anschluss Skills Router, Chronologie Und Belegmatrix, Fristen Und Risikoampel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `insolvenzrecht-antragspflicht-15a-17-19` | Antragspflicht Dokumentenmatrix Und Lueckenliste, Belegmatrix Formular Portal Und Einreichung, Chronologie Internationaler Bezug Und Schnittstellen, Einfuehrung Verhandlung Vergleich Und Eskalation: wählt den konkreten Prüfpfad, trennt F... |
| `insolvenzrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `insolvenzrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `insolvenzrecht-kaltstart-interview` | Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter / beratender Anwalt /... |
| `insolvenzrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `insolvenzrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `insolvenzrecht-rechtsquellen` | Rechtsquellen: Zahlen, Schwellenwerte und Berechnung im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nut... |
| `insolvenzrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `insolvenzrechtliche-livecheck-red-team` | Insolvenzrechtliche Erstpruefung Und Mandatsziel, Livecheck Compliance Dokumentation Und Akte, Mandat Red Team Und Qualitaetskontrolle, Tabelle Beweislast Und Darlegungslast: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bel... |
| `internationales-drittstaaten-konzerninsolvenz` | Internationales Insolvenzrecht Drittstaaten Inzidentpruefung, Konzerninsolvenz Koordination, Mandat Triage Insolvenzrecht, Rechtsabteilung Auslaendischer Insolvenzverwalter In Deutschland: wählt den konkreten Prüfpfad, trennt Frist, Zust... |
| `liquiditaetsvorschau-insolvenzrechtlich` | Erstellt und bewertet die rollierende Liquiditätsvorschau als strukturierte Arbeitsgrundlage für insolvenzrechtliche Tatbestände nach § 17 InsO (Zahlungsunfähigkeit) und § 19 Abs. 2 InsO (Fortbestehensprognose). Lädt, wenn geprüft werden... |
| `rechtsabteilung-lieferantenpool-npl` | Rechtsabteilung Lieferantenpool Und Eigentumsvorbehalt, Rechtsabteilung Npl Kaeufer Im Schuldnerinsolvenzfall, Rechtsabteilung Schufa Löschung Nach Restschuldbefreiung, Rechtsabteilung Starug Fruehwarnsystem Für Rechtsabteilung: wählt de... |
| `triage-verbraucherinsolvenz` | Triage Mandantenkommunikation Entscheidungsvorlage, Verbraucherinsolvenz Mehrparteienkonflikt, Zahlungsunfaehigkeit Tatbestand Beweis Und Belege, Ueberschuldung Prüfung 19 Inso: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `uebertragende-sanierung-auslaendischer-office` | Uebertragende Sanierung Und Asset Deals, Auslaendischer Office Holder Register Und Grundbuch, Vorsatzanfechtung 133 Inso, Zahlungsunfaehigkeit Prüfung 17 Inso: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsg... |
| `verfahrenstypen-quellenkarte` | Verfahrenstypen Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
