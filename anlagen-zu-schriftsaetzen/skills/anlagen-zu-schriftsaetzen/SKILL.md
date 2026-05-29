---
name: anlagen-zu-schriftsaetzen
description: "Anwalt hat Schriftsatz fertig und muss Anlagen korrekt benennen nummerieren und als PDF-Konvolut aufbereiten. Anlagemanagement gerichtliche Schriftsaetze. Prüfraster: Schriftsatz lesen Beweisstuecke erkennen sortieren beA-konforme Benennung (Anlage K1 B1 A1) PDF-Konvertierung Stempel oben rechts Arial 12. Modi Auto-Benennung Schriftsatz folgt Prüfmodus. Output: nummeriertes Anlagenpaket in beA-Konvention. Abgrenzung zu anlagen-erstellen im Sozialrecht (K/W/A-Konvention) und normenkontrollantrag-schriftsatz."
---

# Zuordnung von Anlagen zu gerichtlichen Schriftsätzen

## Triage — kläre vor dem Einsatz

1. In welchem Modus soll der Skill arbeiten — Auto-Benennung (Schriftsatz noch ohne Anlage-Nummern), Schriftsatz folgt (Nummern schon im Schriftsatz) oder Prüfmodus (Zuordnung bereits fertig)?
2. Welche Parteirolle hat der Mandant im konkreten Schriftsatz (Kläger → K, Beklagter → B, Antragsteller → A/AST, Antragsgegner → AG, Nebenintervenient → NI)?
3. Sind alle Anlagen-Dateien in einem Ordner bereitgestellt und in verwertbarem Format (PDF, DOCX, XLSX, JPG, EML/MSG)?
4. Gibt es Konvolute (mehrere Dokumente unter einer Anlage-Nummer), und soll der Stempel auf jeder Seite oder nur auf Seite 1 erscheinen?
5. Soll ein einziges kombiniertes PDF (Schriftsatz + Anlagenkonvolut) erzeugt werden?

## Zentrale Normen

§ 253 ZPO (Klageschrift, Anlagen) — § 130 ZPO (Schriftsätze allgemein) — § 130a ZPO (elektronisches Dokument) — § 130d ZPO (beA-Pflicht ab 01.01.2022) — § 520 Abs. 2 ZPO (Anlage zur Berufungsbegründung) — §§ 286, 371 ZPO (Beweisaufnahme, Urkundenbeweis) — BRAO § 43e (beA-Nutzungspflicht) — BeAZulV (beA-Zulassungsverordnung)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill nimmt einen vorliegenden Schriftsatz-Entwurf und eine Sammlung kuratierter Anlagen und macht daraus ein beA-fertiges Anlagenkonvolut mit korrekter Reihenfolge, PDF-Konvertierung, beA-tauglicher Benennung und Arial-12-Stempel oben rechts.

## Eingaben

- **Schriftsatz-Entwurf** (PDF oder DOCX) — Pflicht.
- **Anlagen-Sammlung** als Ordner oder Liste von Dateien (PDF, DOCX, XLSX, JPG, PNG, EML, MSG).
- **Parteirolle:** K / B / A / AST / AG / NI — oder eigener Präfix.
- **Modus**: Auto-Benennung / Schriftsatz folgt / Prüfmodus.

## Drei Modi

### Modus 1 — Auto-Benennung

Schriftsatz ohne Anlage-Nummern → Skill liest Anker, ordnet Dateien zu, vergibt Nummern in Reihenfolge der ersten Erwähnung, erzeugt Vorschlag im Schriftsatz.

### Modus 2 — Schriftsatz folgt

Nummern bereits im Schriftsatz → Skill ordnet Dateien den vorhandenen Nummern zu, meldet Lücken und Überschüsse.

### Modus 3 — Prüfmodus

Alles schon zugeordnet → Skill validiert: Numerierungslücken, Doppelte, fehlende Dateien, Stempel-Fehlanpassungen, Format-Fehler.

## Stempel-Spezifikation

- **Position:** rechter oberer Rand, ca. 1.5 cm vom oberen / rechten Rand.
- **Schrift:** Arial 12 pt regular.
- **Format:** `Anlage K 7` (Leerzeichen zwischen Präfix und Zahl).
- **Mehrseitige Anlagen:** Stempel nur Seite 1 (Standard); Option `--stempel jede-seite`.
- **Konvolute:** Deckblatt + Einzeldokumente mit Suffix `K 5/1`, `K 5/2` usw.

## Datei-Benennung (beA-tauglich)

Beispiel: `Anlage_K-03_Vertrag-vom-2024-03-15.pdf`

Regeln: keine Umlaute (ae/oe/ue/ss), kein Leerzeichen, Zahlen zweistellig, max. ca. 90 Zeichen, Datum im Format JJJJ-MM-TT.

## Ausgabe

```
anlagen/
  Anlage_K-01_<Kurzbeschreibung>.pdf
  Anlage_K-02_<Kurzbeschreibung>.pdf
  …
  Anlagenkonvolut.pdf
  Anlagenverzeichnis.pdf
  Anlagenverzeichnis.md
```

Optional: `Schriftsatz_mit_Anlagen.pdf` — Schriftsatz vorab, dann Konvolut, mit durchlaufenden Lesezeichen.

## Was der Skill NICHT tut

- Keine inhaltliche Schwärzung (DSGVO).
- Keine Echtheits- oder Authentizitätsprüfung.
- Keine elektronische Signatur und kein direktes beA-Hochladen.

## Output-Template

**Prüfmodus-Report: Anlagenkonvolut**

Schriftsatz: [...]
Parteirolle: [...] (K / B / A)
Anzahl Anlagen im Schriftsatz zitiert: [...]
Anzahl Anlagen-Dateien vorhanden: [...]

| Fehlerklasse | Befund |
|---|---|
| Numerierungslücken | keine / K [...] fehlt |
| Doppelt vergebene Nummern | keine / K [...] doppelt |
| Zitiert aber Datei fehlt | keine / K [...] |
| Vorhanden aber nicht zitiert | keine / K [...] |
| Stempel-Fehlanpassungen | keine / K [...] |
| Format-Fehler (Umlaute, Leerzeichen) | keine / Datei: [...] |

**Ergebnis:** [Kein Handlungsbedarf / Korrekturen erforderlich — Korrekturplan: ...]

---

Hinweis: Die Letztverantwortung für Vollständigkeit und Berufspflichten (§ 43e BRAO, § 203 StGB, DSGVO) liegt beim Anwalt.

<!-- AUDIT 27.05.2026: BGH VI ZB 53/20 (NOT_FOUND auf dejure.org) entfernt und ersetzt durch BGH VII ZR 21/16, BauR 2018, 2056 (verifiziert auf dejure.org). -->
