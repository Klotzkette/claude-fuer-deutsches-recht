---
name: review-durchfuehren
description: "Fuehrt den eigentlichen Reviewlauf ueber den Wuerfel durch — Anzahl Zellen = Spalten x Zeilen x Arbeitsblaetter. Pro Zelle: Spaltenprompt + Zeilenprompt + Arbeitsblatt-Perspektive zusammenfuehren, Antwort aus dem Dokument extrahieren mit woertlichem Zitat und Fundstelle, Ampel anhand der Spalten-Ampelregel setzen. Bei Quasi-Duplikaten Cache aus `caching-und-teil-rerun` nutzen. Bei OCR-Konfidenz unter 90 Prozent automatisch Pruefer-Flag. Pro Reviewlauf Audit-Eintrag in `audit-trail-protokoll`. Schreibt `wuerfel.parquet` mit allen Zellen sowie `lauf-zusammenfassung.md`."
---

# /tabellenreview-3d:review-durchführen

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
