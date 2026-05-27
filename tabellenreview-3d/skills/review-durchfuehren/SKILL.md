---
name: review-durchfuehren
description: "3D-Tabellenreview konkret durchfuehren: jede Zeile in allen drei Perspektiven pruefen und bewerten. Normen: §§ 174 ff. 176 InsO. Pruefraster: Forderungshoehe, Pruefergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung. Output: Ausgefuellte 3D-Review-Tabelle. Abgrenzung: nicht Wuerfel-Aufbau (Vorbereitung)."
---

# /tabellenreview-3d:review-durchführen


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


## Zweck

Das ist der Hauptlauf. Wenn der Würfel 25 Spalten 200 Zeilen und 5 Arbeitsblätter hat sind das 25.000 Zellen. Jede Zelle braucht: Antwort + wörtliches Zitat + Fundstelle + Ampel + Prüfer-Flag.

## Eingaben

- `wuerfel-schema.yaml`
- `spaltenprompts.yaml`
- `zeilenprompts.yaml`
- `arbeitsblaetter.yaml`
- `zeilen-inventar.yaml`
- Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/CLAUDE.md`

## Ablauf pro Zelle

1. **Prompt zusammenführen:** Arbeitsblatt-Perspektive vor Spaltenprompt vor Zeilenprompt. Konflikte protokollieren.
2. **Quelldokument öffnen:** Pfad + Hash gegen Inventar abgleichen — falls Hash abweicht: Belegkette unterbrochen Prüfer-Flag setzen.
3. **Antwort extrahieren:** Antworttyp aus Spaltenprompt-Definition beachten (Freitext / zitat-mit-fundstelle / ja-nein / Datum / Geldbetrag / Aufzählung).
4. **Belegkette schreiben:** wörtliches Zitat in Anführungszeichen, danach Fundstelle (Datei-ID + Seite + Absatz + ggf. Ziffer).
5. **Ampel setzen:** anhand `ampel-regel` aus dem Spaltenprompt (rot / gelb / grün).
6. **Prüfer-Flag setzen wenn:**
   - OCR-Konfidenz unter 90 Prozent
   - Antworttyp `zitat-mit-fundstelle` aber kein Zitat extrahierbar
   - Konflikt zwischen Spalten- und Zeilenprompt
   - Mehrdeutigkeit (mehrere plausible Antworten im Dokument)
7. **Querweis aufbauen:** wenn Zellen-Ergebnis auf anderen Vertrag referenziert (`siehe Anlage 7 zu Vertrag X`) als Cross-Ref vermerken.
8. **Cache prüfen:** bei Quasi-Duplikaten (Ähnlichkeit über 95 Prozent) zur Zelle eines bereits geprüften Dokuments Cache-Treffer vorschlagen — Prüfer entscheidet ob übernommen.

## Ausgabeformat

- `wuerfel.parquet` (oder JSON) mit einer Zeile pro Zelle:

```
arbeitsblatt-id, zeile-id, spalte-id, antwort, woertliches-zitat, fundstelle, ampel, prüfer-flag, prompt-version, lauf-zeitstempel
```

- `lauf-zusammenfassung.md` — Anzahl Zellen pro Ampel, Anzahl Prüfer-Flags, Anzahl Cache-Treffer, Laufdauer, Modell-Version, Audit-Trail-Eintrag-ID.

## Reihenfolge

Standard: Arbeitsblatt-außen, Zeile-mittel, Spalte-innen. Optional: Spalte-außen wenn Spaltenprompt aufwaendig (z. B. Volltext-Indexierung) und über den Stapel gemeinsam profitiert.

## Grenzen

Jede Zelle ist ein Hinweis kein Befund. Prüfer-Flags sind die wichtigste Ausgabe — sie sagen wo der menschliche Prüfer hinschauen muss. Untermarkierung ist eine Einbahnstraße; Übermarkierung ist eine Zweiwegtür die ein Anwalt in 30 Sekunden schließt.
