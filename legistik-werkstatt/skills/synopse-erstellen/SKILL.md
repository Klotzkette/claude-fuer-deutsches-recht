---
name: synopse-erstellen
description: "Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Aenderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Aenderungen schnell zu erfassen. Pro geaendertem Paragrafen eine Zeile oder Block pro Stammgesetz eigene Synopsen-Tabelle. Spalten gleich breit druckbar A4 quer oder A3. Output Synopsen-Tabelle Markdown plus DOCX-Vorlage. Anschluss lesefassung-konsolidiert. Abgrenzung zu xml-paralleldarstellung maschinenlesbare Ausgabe."
---

# Synopse erstellen

> Drei Spalten: vorher, nachher, Änderungsbefehl. Hilft Allen.

## Aufbau einer Synopse

### Tabelle (Format Markdown / DOCX / PDF Landscape)

| Bisheriges Recht | Neues Recht | Änderungsbefehl |
|---|---|---|
| Paragraf 33 HGB (alte Fassung) Wortlaut ... | Paragraf 33 HGB (neue Fassung) Wortlaut ... | Paragraf 33 wird wie folgt gefasst ... |

### Pro Stammgesetz eine eigene Datei

- Synopse_HGB.md
- Synopse_ZPO.md
- Synopse_FamFG.md

### Spaltenbreite

DOCX: ca. 33 Prozent / 33 Prozent / 34 Prozent. Bei langen Sätzen A3 Landscape oder DIN A4 mit kleiner Schrift.

## Kennzeichnung von Änderungen

- Eingefügte Worte: **fett** oder Doppelunterstreichung
- Gestrichene Worte: ~~Durchstreichung~~ oder kursiv mit Hinweis "entfaellt"
- Bei voelliger Neufassung: Spalte "Bisheriges Recht" "Aufgehoben (alte Fassung in Anlage)"

## Lesefassung in separater Datei

Synopse ist gut für den Vergleich. Eine **Lesefassung** zeigt die geänderte Norm in einer einheitlich gelesenen Fassung.

Beispiel "Lesefassung_HGB_Paragraf_33.md" - das ist der Paragraf, wie er nach Inkrafttreten lautet.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 42-48 GGO (Synopse als Bestandteil der Begr.) — §§ 1-4 HdR (Rechtsfoermlichkeit, Vergleichs-Darstellungen) — Art. 76 Abs. 2 GG (Einbringungs-Unterlagen inkl. erlaeuternder Materialien)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anschluss

`lesefassung-konsolidiert`.
