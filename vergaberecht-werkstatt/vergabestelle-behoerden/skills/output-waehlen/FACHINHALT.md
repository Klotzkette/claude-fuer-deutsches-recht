---
name: output-waehlen
description: "Auf Auftraggeberseite: Output-Wahl im Vergaberecht steuern: Adressat, Frist, Zweck und Format für Rüge, Nachprüfungsantrag, OLG-Beschwerde, Vermerk, Tabelle oder Uploadpaket."
---

# Output wählen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Einsatzlage

Diese Output-Weiche für Vergaberecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste, Behördenbrief oder Entscheidungsvorlage der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `vergabe-os-master-orchestrator` — Gesamtsteuerung und Output-Weiche.
- `workflow-fristen-und-risikoampel` — Fristenampel und Sofortmaßnahmen.
- `output-waehlen` — Vermerk, Rügeerwiderung, VK-Stellungnahme, Tabelle, Checkliste oder Uploadpaket.
- `bestangebot-durchsetzen`, `10-zuschlagsmatrix-aufbauen`, `wertungspreisqualitaet-matrix` und `18-wertungsvermerk-erstellen` — Bestwertung und Wertungsdokumentation.
- `eforms-ted-bekanntmachung-check`, `05-bekanntmachung-erstellen` und `bekanntmachung-berichtigung-und-upload-routing` — Veröffentlichungs- und Uploadoutputs.
- `vergabeunterlagen-lv-datenformate-bereitstellen` und `legacy-systeme-integration` — Unterlagen-, LV- und Systemoutputs.
- `22-ruegeerwiderung`, `23-stellungnahme-vergabekammer`, `26-akteneinsicht-vergabekammer` und `24-vorlage-an-den-vergabesenat` — Rechtsschutzoutputs.
- `wettbewerbsregister-abfrage-selbstreinigung`, `12-ausschlussgruende-pruefen` und `27-selbstreinigung-paragraf-125` — Register- und Ausschlussoutputs.

## Arbeitsweg

- Ergebnistyp bestimmen: Vergabevermerk, Entscheidungsvorlage, Bieterantwort, Rügeerwiderung, VK-Stellungnahme, OLG-Erwiderung, Risikoampel, Tabellen-Dashboard, Uploadauftrag oder Vergleichsvorschlag — was braucht die Vergabestelle wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Vergaberecht (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei fachlichem Empfänger ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Output-Applets

Wähle bei komplexen Fällen ein kleines, verwertbares Applet statt langer Erstberatung:

| Lage | Bestes Applet |
|---|---|
| Unklare Vergabeakte | Aktenmatrix mit Bekanntmachung, Unterlagen, LV-/GAEB-/XML-/Excel-/PDF-Status und Portalprotokollen |
| Unklare Belege | Belegmatrix mit Entscheidung, Aktenstelle, Begründung und Nachweiswert |
| Rüge oder Bieterfrage | Rüge-/Antwort-Tabelle mit Vorwurf, Norm, Aktenstelle, Abhilfeoption und Frist |
| Unklare Wertung | Wertungsmatrix mit Kriterium, Gewicht, Bewertung, Dokumentation und Reparaturpfad |
| Laufendes VK-Verfahren | VK-OLG-Streitdashboard mit Zulässigkeit, Verteidigung, Eilbedarf, Akteneinsicht und Kosten |
| Berichtigung/Upload | Veröffentlichungs- und Uploadauftrag mit Freigabecheck, eForms/TED/DVAL/Portal und Nachweis |
| Gremienentscheidung | Beschlussvorlage mit Entscheidungsoptionen, Risiken, Haushalts-/Projektfolgen und nächstem Schritt |

Wenn kein Applet passt, begründe kurz, warum ein Vermerk, Schriftsatz oder Memo besser ist.

## Output-Menü

Nach dem ersten Dashboard genau eine bevorzugte Ausgabe und maximal zwei Alternativen anbieten:

| Ausgabe | Nutzen | Mindestinhalt |
|---|---|---|
| Vermerk | Entscheidung aktenfest machen | Sachstand, Rechtsgrundlage, Abwägung, Ergebnis, Aktenstelle |
| Rügeerwiderung | Bieterangriff beantworten | Vorwurf, Zulässigkeit, Begründetheit, Abhilfe, Frist |
| VK-Stellungnahme | Nachprüfung verteidigen | Anträge, Sachverhalt, Zulässigkeit, Begründetheit, Aktenverzeichnis |
| Tabelle | Behördenentscheidung vorbereiten | Frist, Risiko, Aktenbeleg, nächste Aktion, Owner |
| Checkliste | Fristen- oder Unterlagenarbeit führen | Pflichtpunkt, Status, Beleg, Lücke, Freigabe |
| Uploadpaket | Veröffentlichung vorbereiten | Portal, Feldliste, Dateien, Hash, Freigabe, Uploadnachweis |

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
