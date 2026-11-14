---
name: einstieg-routing
description: 'Orientiert die Vergabestelle ohne Unterlagen: klärt Rolle, Bedarf, Phase, Auftraggeber- und Auftragsart, Regime, Rechtsweg, Zuständigkeit, mögliche rote Frist und nächsten Output. Bei einem Dokument übernimmt die Schnelltriage, bei Ordner oder ZIP der Master-Orchestrator.'
---

# Einstieg und Routing

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Einsatzlage

Dieser Einstieg dient ausschließlich der Orientierung ohne Unterlagen. Er ordnet einen kurzen mündlichen Sachverhalt nach Rolle, Bedarf, Phase, Regime, Rechtsweg und nächstem Arbeitsprodukt ein.

## Abgrenzung

- Ohne Unterlagen und noch ohne klaren Verfahrenspfad: dieser Skill.
- Ein einzelnes Dokument oder eine konkrete Rechtsfrage: `workflow-kaltstart-und-routing`.
- Ordner, ZIP, Portal-/DMS-Export oder mehrere Arbeitsstränge: `vergabe-os-master-orchestrator`.

## Fachlandkarte dieses Plugins

- `vergabe-os-master-orchestrator` — Gesamtsteuerung für Bedarf, Verfahren, Wertung, Rechtsschutz und Upload.
- `workflow-kaltstart-und-routing` und `workflow-fristen-und-risikoampel` — erster Satz, rote Fristen, Verfahrensstand und Output-Weiche.
- `dokumente-intake`, `unterlagen-luecken` und `workflow-unterlagen-lueckenliste` — Vergabeakte, Unterlagen, LV, Angebote, Protokolle und Lücken.
- `quellen-livecheck`, `schwellenwerte-2026-2027-livecheck` und `schnittstelle-zahlen-schwellen-und-berechnung` — Normen, Schwellen, Wertgrenzen und Rechenweg.
- `eforms-ted-bekanntmachung-check`, `05-bekanntmachung-erstellen` und `bekanntmachung-berichtigung-und-upload-routing` — Bekanntmachung, TED/DVAL, Berichtigung und Portal.
- `wirklichkeitsdaten-beschaffung-steuern`, `legacy-systeme-integration` und `vergabeunterlagen-lv-datenformate-bereitstellen` — Datenquellen, GAEB/XML/Excel/PDF und Systemanschluss.
- `bestangebot-durchsetzen`, `10-zuschlagsmatrix-aufbauen`, `wertungspreisqualitaet-matrix` und `18-wertungsvermerk-erstellen` — Bestwertung statt Preisautomatismus.
- `12-ausschlussgruende-pruefen`, `wettbewerbsregister-abfrage-selbstreinigung` und `27-selbstreinigung-paragraf-125` — Ausschluss, Register und Selbstreinigung.
- `22-ruegeerwiderung`, `23-stellungnahme-vergabekammer`, `26-akteneinsicht-vergabekammer` und `24-vorlage-an-den-vergabesenat` — Rüge, VK, Akteneinsicht und OLG.

## Arbeitsweg

- Rolle und Ziel klären: Welche Stelle handelt, welcher Ergebnistyp wird gebraucht (Schriftsatz, Vergabevermerk, Entscheidungsvorlage, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: tragende Normen über `gesetze-im-internet.de`, Unionsrecht über `eur-lex.europa.eu` und Rechtsprechung über amtliche Gerichtsquellen oder `rechtsprechung-im-internet.de` prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Vergabestelle, Bieter, Beigeladene, Vergabekammer, Vergabesenat, Aufsicht, Portalbetreiber oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Startbildschirm statt Textwüste

Wenn der Sachverhalt länger als ein Einzelfall ist, zuerst fünf Felder ausgeben: Was liegt vor, welche Rolle, welcher Verfahrensstand, welches Ziel, welcher Output. Danach direkt das passende Applet wählen: Fristenampel, Dokumentenmatrix, Belegmatrix, Angriff-/Verteidigungslinie, Wertungsmatrix, Upload-/Formatexport-Check oder VK-/OLG-Streitdashboard.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
