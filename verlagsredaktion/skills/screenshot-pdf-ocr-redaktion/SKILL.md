---
name: screenshot-pdf-ocr-redaktion
description: "Fuehrt einen sauberen OCR-für gescannte PDFs und Screenshots zu redaktionellem Manuskript, mit Fehlerquoten-Stichprobe und Pinpoint-Erhalt im Verlagsredaktion."
---

# Screenshot / PDF-OCR-Workflow

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: VerlG § 17 Ablieferungsfrist, UrhG § 41 Rückrufsrecht wegen Nichtausübung nach 2 Jahren, VG-Wort-Meldungen jährlich, JuSchG-Indizierung sofort wirksam.
- Tragende Normen verifizieren: UrhG §§ 1, 7, 11, 31, 32, 34, 38, 41, 43, 50, 51, 51a, 53, 87a-h, VerlG, BGB §§ 433, 631, JuSchG, PresseG der Länder, ImpressumsR, DSGVO Art. 85 (Medienprivileg) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verlag, Autor, Lektor, Übersetzer, VG Wort, Lizenzpartner, Vertrieb, Datenschutzbeauftragter, ggf. Bundeszentrale für Kinder- und Jugendmedienschutz.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verlagsvertrag, Übersetzervertrag, Lizenzvertrag, Honorarrechnung, Pflichtexemplarmeldung, VG-Wort-Meldung, Impressum, AGB — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es konkret

Autorinnen, Mandantinnen oder Fremdmaterial liegen oft als gescannte PDFs oder als Screenshots vor: alte Festschriftsbeitraege, Bescheidkopien, ausgedruckte und wieder eingescannte Aufsaetze. OCR ist Pflicht, aber OCR-Ergebnisse sind nie sauber. Dieser Skill fuehrt durch den vollstaendigen OCR-inklusive Fehlerquoten-Stichprobe.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn, sobald eine Bildquelle (Scan, Screenshot, fotografierte Seite) zum durchsuchbaren Text werden muss. Klaeren Sie:

1. Auflage hoch oder niedrig (300 dpi+? unter 200 dpi liefert OCR-Mist)?
2. Schriftart: Antiqua moderner Druck, Fraktur, Schreibmaschine?
3. Sprache (Deutsch, Englisch, Latein in Fussnoten)?
4. Sind sensible Daten enthalten (Mandantenname, Aktenzeichen)?

## Material- bzw. Sachrahmen

- PDF / Bilddatei.
- Idealerweise mehrere Seiten als Vergleich (eine Seite ist keine OCR-Statistik).
- Hinweise auf besondere Schriftbestandteile (Tabellen, Marginalien, Fussnoten in kleinerer Schrift).

## Praxisleitfaden / Schritt für Schritt

1. **Datenschutz pruefen.** Wenn Mandantendaten enthalten sind: nur in Tools mit AVV und entsprechend BRAO § 43a Abs. 2.
2. **Qualitaet pruefen.** Eine Stichprobe von zwei bis drei Seiten ansehen. Unter 200 dpi: zurueck zur Quelle (neu scannen).
3. **OCR ausfuehren.** Tesseract, Adobe Acrobat oder vergleichbare Werkzeuge mit Sprachpaket "deu" (und ggf. "lat", "eng").
4. **Fehlerquoten-Stichprobe.** Zwei zufaellige Seiten Wort-für-Wort vergleichen, Fehlerrate dokumentieren (typisch 0,3 bis 3 % bei modernem Druck, deutlich mehr bei Fraktur).
5. **Manuelle Nachkorrektur** vor allem bei: Eigennamen (Personen, Orte, Kommentar-Bearbeitern), Zahlen (Aktenzeichen, Randnummern, Seitenangaben), Sonderzeichen (§, II 2, vgl.), Fussnoten.
6. **Strukturmarkierung.** OCR liefert Fliesstext ohne Stilauszeichnung; Ueberschriften, Fussnoten, Tabellen mit Verlagsvorlage neu auszeichnen.
7. **Audit-Log.** Quelle, Stichproben-Fehlerrate, manuelle Korrekturen dokumentieren - der Verlag muss spaeter beweisen koennen, dass nicht halluziniert wurde.

## Trade-off-Matrix

| Pfad | A: Adobe / kommerzielles OCR | B: Tesseract / Open Source | Empfehlung |
|------|------------------------------|----------------------------|------------|
| Qualitaet moderner Druck | sehr gut | gut | B reicht meist |
| Fraktur / historisch | mittel | besser mit speziellen Modellen | B mit Fraktur-Modell |
| Datenschutz | Cloud vs. Desktop, AVV pruefen | lokal moeglich | B bei Mandantendaten |
| Zeit | schnell | langsamer | A bei Volumen |

## Praxistipps der alten Redaktion

- "Aktenzeichen sind die haeufigste OCR-Falle. Eine 6 wird zur 8, eine 1 zum l. Vor Abgabe jedes Aktenzeichen pruefen."
- Marginalien-Druck (oft am Rand) wird oft als Hauptfliesstext fehlgedeutet - manuell sortieren.
- Bei Frakturschrift fast immer manuelle Nachbearbeitung; ohne Spezialmodell waeren 5-10 % Fehler normal.
- Screenshots aus Word/PDF-Reader haben den Vorteil, dass der Originaltext per Copy-Paste oft verfuegbar waere - lieber den nachfragen statt OCR.

## Mustertexte / Vorlagen

**OCR-Auditlogfile:**

```
Quelle: Festschrift Mueller, S. 211-238 (Scan vom 03.06.2026)
Aufloesung: 300 dpi, Graustufe
Schriftart: Antiqua, Auflage 1998
OCR-Tool: Tesseract 5.4, Sprachpaket deu
Stichprobenseiten: S. 215, S. 228
Fehler in Stichprobe: 7 von 1.218 Woertern = 0,57 %
Manuelle Korrektur: 23 Aktenzeichen, 11 Randnummern, 4 Bearbeiternamen
Status: redaktionsreif nach Lektoratspruefung
```

**Anschreiben bei schlechter Scanqualitaet:**

> Sehr geehrte Frau Doktor, das uebersandte PDF (Anlage Festschrift S. 211 ff.) ist mit rund 150 dpi gescannt. Eine zuverlaessige Texterkennung ist auf dieser Basis nicht moeglich. Wir bitten um einen neuen Scan mit mindestens 300 dpi (Graustufe ausreichend) bis 19.06.2026.

## Typische Fehler / Pitfalls

- OCR-Ergebnis ungeprueft uebernommen - Aktenzeichen verfaelscht.
- Fraktur ohne Spezialmodell - 10 % Fehler im Fliesstext.
- Tabellen werden zu Fliesstext - Werte verschoben.
- Mandantendaten in Cloud-OCR ohne AVV.
- Kein Audit-Log - im Streitfall nicht nachvollziehbar.

## Quellen Stand 06/2026

- BRAO § 43a Abs. 2 (Verschwiegenheit).
- StGB § 203 (Verletzung von Privatgeheimnissen).
- DSGVO Art. 6, Art. 28 (Auftragsverarbeitung), [https://eur-lex.europa.eu/eli/reg/2016/679/oj](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- Tesseract OCR, [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).
- Duden, Die deutsche Rechtschreibung, 29. Aufl. 2024.
- Byrd / Lehmann, Zitierfibel für Juristen, 2. Aufl. 2016, zur Pinpoint-Disziplin.

