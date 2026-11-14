---
name: output-waehlen
description: "Auf Bieterseite: Output-Wahl im Vergaberecht steuern: Adressat, Frist, Zweck und Format für Rüge, Nachprüfungsantrag, OLG-Beschwerde, Vermerk, Tabelle oder Uploadpaket."
---

# Output wählen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Einsatzlage

Diese Output-Weiche für Vergaberecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Teambrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `vergabe-os-master-orchestrator` — Gesamtsteuerung für Bieterfälle.
- `unterlagen-und-lv-datenformate-auslesen` und `angebot-in-vorgegebenem-format-erstellen` — Angebotspaket, GAEB/XML/Excel/PDF, Portalabgabe und Uploadnachweis.
- `qualitaetsvorsprung-nachweisen`, `13-konzeptionelle-anlagen` und `10-leistungsverzeichnis-bepreisen` — Bestangebot trotz höherem Preis.
- `bieterfragen-antworten-management`, `21-ruegeschreiben-erstellen` und `ruege-vor-zuschlag` — Frage, Rüge, Frist und Präklusion.
- `nachpruefungsantrag-powerdraft`, `nachpruefungsantrag-vk`, `nachpruefungsverfahren-vk` und `vergabekammer-verhandlung-vergleich-und-eskalation` — VK-Rechtsschutz.
- `eignungspruefung`, `ausschluss-bieter-paragraf-124-gwb`, `28-selbstreinigung-nach-ausschluss-paragraf-125` und `wettbewerbsregister-abfrage-selbstreinigung` — Ausschluss, Nachforderung und Selbstreinigung.
- `08-bietergemeinschaft-bildung` und `17-bietergemeinschaftserklaerung` — Bietergemeinschaft, Steuer-/Sozialabgaben und Mitgliederaustausch.
- `olg-vergabesenat-beschwerdebriefing`, `schadensersatz-181-gwb` und `vergleichsverhandlung-strategie` — OLG, Kosten und Vergleich.

## Arbeitsweg

- Ergebnistyp bestimmen: internes Bieter-/Kanzleimemo, Rüge, Nachprüfungsantrag, Eilantrag, OLG-Beschwerde, Risikoampel, Vertragsentwurf, Tabellen-Dashboard oder Vergleichsvorschlag — was braucht das Team wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Vergaberecht (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei fachlichem Empfänger ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Output-Applets

Wähle bei komplexen Fällen ein kleines, verwertbares Applet statt langer Erstberatung:

| Lage | Bestes Applet |
|---|---|
| Unklare Unterlagen | Dokumentenmatrix mit LV-/GAEB-/XML-/Excel-/PDF-Status |
| Unklare Belege | Belegmatrix mit Behauptung, Fundstelle, Gegnerargument und Replik |
| Mehrere Rügepunkte | Rügepunkt-Tabelle mit Norm, Tatsache, Beleg, Kausalität und Abhilfe |
| Unklare Wertung | Wertungsmatrix mit Kriterium, Gewicht, Bewertung, Fehler und Zuschlagschance |
| Laufendes VK-Verfahren | VK-OLG-Streitdashboard mit Zulässigkeit, Begründetheit, Eilbedarf und Kosten |
| Angebotsabgabe | Uploadliste mit Dateinamen, Hash, Signatur, Portalnachweis und Freigabe |
| Entscheidungsvorbereitung | Go-/No-Go-Ampel mit Frist, Chance, Kosten, Geschäftsrisiko und nächstem Schritt |

Wenn kein Applet passt, begründe kurz, warum ein Schriftsatz oder Memo besser ist.

## Output-Menü

Nach dem ersten Dashboard genau eine bevorzugte Ausgabe und maximal zwei Alternativen anbieten:

| Ausgabe | Nutzen | Mindestinhalt |
|---|---|---|
| Schriftsatz | VK/OLG oder Gegner adressieren | Anträge, Sachverhalt, Zulässigkeit, Begründetheit, Anlagen |
| Rüge | Frist wahren und Abhilfe verlangen | Fehler, Norm, Tatsache, Beleg, Kausalität, Abhilfe |
| Tabelle | Teamentscheidung vorbereiten | Frist, Risiko, Beleg, nächste Aktion, Owner |
| Checkliste | Angebots- oder Fristenarbeit führen | Pflichtpunkt, Status, Beleg, Lücke, Freigabe |
| Angebotspaket | formgerecht abgeben | Zielformat, Dateien, Hash, Signatur, Portalnachweis |
| Uploadpaket | Portalabgabe vorbereiten | Dateinamen, Reihenfolge, Größencheck, Freigabe, Bestätigung |

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
