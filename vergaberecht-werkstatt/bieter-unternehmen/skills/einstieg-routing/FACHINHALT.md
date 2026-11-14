---
name: einstieg-routing
description: 'Orientiert Bewerber und Bieter ohne Unterlagen: klärt Rolle, Ziel, Phase, Auftraggeber- und Auftragsart, Regime, Rechtsweg, mögliche rote Frist und nächsten Output. Bei einem Dokument übernimmt die Schnelltriage, bei Ordner oder ZIP der Master-Orchestrator.'
---

# Einstieg und Routing

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Einsatzlage

Dieser Einstieg dient ausschließlich der Orientierung ohne Unterlagen. Er ordnet einen kurzen mündlichen Sachverhalt nach Bieterrolle, Ziel, Phase, Regime, Rechtsweg und nächstem Arbeitsprodukt ein.

## Abgrenzung

- Ohne Unterlagen und noch ohne klaren Angebots- oder Rechtsschutzpfad: dieser Skill.
- Ein einzelnes Dokument oder eine konkrete Rechtsfrage: `workflow-kaltstart-und-routing`.
- Ordner, ZIP, Portal-/Unternehmensexport oder mehrere Arbeitsstränge: `vergabe-os-master-orchestrator`.

## Fachlandkarte dieses Plugins

- `vergabe-os-master-orchestrator` — Gesamtsteuerung für Bieterfälle, Fristen, Formate, Angebot, Rüge und VK/OLG.
- `workflow-kaltstart-und-routing` — erster Satz oder Dokumentenpaket in den passenden Arbeitsweg.
- `dokumente-intake` und `unterlagen-und-lv-datenformate-auslesen` — Bekanntmachung, Unterlagen, LV, GAEB/XML/Excel/PDF und Portalexporte ordnen.
- `legacy-systeme-integration` — SAP/ERP/CRM/AVA/DMS/API/MCP als Angebots- oder Beweisquelle anbinden.
- `angebot-in-vorgegebenem-format-erstellen` — Angebot, Nachweise und Anlagen im geforderten Format liefern.
- `qualitaetsvorsprung-nachweisen` — teureres, aber wirtschaftlich besseres Angebot punktwirksam darstellen.
- `bieterfragen-antworten-management` und `21-ruegeschreiben-erstellen` — Klärung, Rüge, Präklusion und Abhilfe.
- `nachpruefungsantrag-powerdraft`, `nachpruefungsantrag-vk` und `nachpruefungsverfahren-vk` — VK-Rechtsschutz.
- `eignungspruefung`, `ausschluss-bieter-paragraf-124-gwb`, `08-bietergemeinschaft-bildung`, `17-bietergemeinschaftserklaerung` und `wettbewerbsregister-abfrage-selbstreinigung` — Ausschluss, Nachforderung, Steuer-/Sozialabgaben und Selbstreinigung.
- `vergabekammer-verhandlung-vergleich-und-eskalation` und `olg-vergabesenat-beschwerdebriefing` — Termin, Vergleich und Beschwerde.

## Arbeitsweg

- Rolle und Ziel klären: Welche Seite handelt, welcher Ergebnistyp wird gebraucht (Schriftsatz, Angebotscheck, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: tragende Normen über `gesetze-im-internet.de`, Unionsrecht über `eur-lex.europa.eu` und Rechtsprechung über amtliche Gerichtsquellen oder `rechtsprechung-im-internet.de` prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Bieterteam, Vergabestelle, Beigeladene, Vergabekammer, Vergabesenat, Portalbetreiber oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Startbildschirm statt Textwüste

Wenn der Sachverhalt länger als ein Einzelfall ist, zuerst fünf Felder ausgeben: Was liegt vor, welche Rolle, welcher Verfahrensstand, welches Ziel, welcher Output. Danach direkt das passende Applet wählen: Fristenampel, Dokumentenmatrix, Belegmatrix, Angriff-/Verteidigungslinie, Wertungsmatrix, Upload-/Formatexport-Check oder VK-/OLG-Streitdashboard.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
