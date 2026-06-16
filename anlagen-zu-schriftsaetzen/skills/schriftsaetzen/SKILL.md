---
name: schriftsaetzen
description: "Anwalt hat Schriftsatz fertig und muss Anlagen korrekt benennen nummerieren und als PDF-Konvolut aufbereiten. Anlagemanagement gerichtliche Schriftsaetze. Prüfraster: Schriftsatz lesen Beweisstuecke erkennen sortieren beA-konforme Benennung (Anlage K1 B1 A1) PDF-Konvertierung Stempel oben rechts..."
---

# Zuordnung von Anlagen zu gerichtlichen Schriftsätzen

## Triage — kläre vor dem Einsatz

1. **Nummernkreis:** Kläger/Antragsteller `K` oder `AST`, Beklagter/Antragsgegner `B` oder `AG`, Berufung `BK`/`BB`, Schiedsverfahren oder eigenes Schema?
2. **Arbeitsmodus:** Auto-Benennung, Schriftsatz folgt, Prüfmodus oder Rettung nach gerichtlichem Hinweis?
3. **Ziel-Schriftsatz:** Klage, Erwiderung, Replik, Duplik, Eilantrag, Berufung, Beschwerde, Schiedsgerichtsschriftsatz?
4. **Material:** Einzeldateien, ZIP/Datenraumexport, EML/MSG, PDF-Scans, DOCX, XLSX/CSV, Fotos/Screenshots, fremdsprachige Anlagen?
5. **K1-Leitanlage:** Gibt es einen Vertrag, Auftrag, Bescheid, Beschluss, Protokoll oder Datensatz, an dem die gesamte Anlagenlogik hängt?
6. **Versand:** Soll nur sortiert werden oder auch ein beA-/ERV-taugliches Paket mit Anlagenverzeichnis, Stempel, Konvolutdeckblättern und Prüfprotokoll entstehen?

## Zentrale Normen

§ 130 ZPO (Schriftsätze allgemein) — § 130a ZPO (elektronisches Dokument) — § 130d ZPO (Nutzungspflicht für vorbereitende Schriftsätze und Anträge durch professionelle Einreicher) — § 253 ZPO (Klageschrift) — §§ 286, 371 ff. ZPO (Beweiswürdigung, Urkundsbeweis, Augenschein) — § 142 ZPO (Urkundenvorlage) — § 294 ZPO (Glaubhaftmachung im Eilverfahren) — § 520 ZPO (Berufungsbegründung) — § 31a BRAO (besonderes elektronisches Anwaltspostfach) — ERVV und ERVB in der jeweils aktuellen Fassung.

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- **Schriftsatz-Entwurf** (PDF oder DOCX) — Pflicht.
- **Anlagen-Sammlung** als Ordner oder Liste von Dateien (PDF, DOCX, XLSX, JPG, PNG, EML, MSG).
- **Parteirolle:** K / B / A / AST / AG / NI — oder eigener Präfix.
- **Modus**: Auto-Benennung / Schriftsatz folgt / Prüfmodus.

## Vier Modi

### Modus 1 — Auto-Benennung

Schriftsatz ohne Anlage-Nummern → Skill liest Anker, ordnet Dateien zu, vergibt Nummern in Reihenfolge der ersten Erwähnung, erzeugt Vorschlag im Schriftsatz.

### Modus 2 — Schriftsatz folgt

Nummern bereits im Schriftsatz → Skill ordnet Dateien den vorhandenen Nummern zu, meldet Lücken und Überschüsse.

### Modus 3 — Prüfmodus

Alles schon zugeordnet → Skill validiert: Numerierungslücken, Doppelte, fehlende Dateien, Stempel-Fehlanpassungen, Format-Fehler.

### Modus 4 — Reparatur nach Hinweis

Gericht oder Gegenseite rügt Anlagenchaos → Skill baut Korrekturplan: Welche Anlage nachreichen, welche Nummer beibehalten, welche nur erläutern, welche Dateifassung ersetzen, welcher Schriftsatztext muss den Tatsachenkern nachholen?

## K1- und Konvolutlogik

Behandle `K1`/`B1` als Leitentscheidung:

- **Einzelanlage:** eine Urkunde, ein PDF, ein klarer Beweiszweck.
- **Konvolut:** mehrere Dokumente unter einer Nummer, nur wenn sie einen gemeinsamen Beweiszweck haben.
- **Untergliederung:** `K1.1`, `K1.2`, `K1.3` oder `K1/1`, `K1/2`, `K1/3` nur mit Deckblatt und kurzer Inhaltsliste.
- **Schriftsatzbezug:** Der Schriftsatz nennt die konkrete Unteranlage, wenn nur ein Teil des Konvoluts entscheidend ist.
- **Fassungsregel:** Entwurf, Scan, OCR-Fassung und E-Mail-Anhang werden nicht unkontrolliert alle zu K1; eine Fassung wird gerichtliche Fassung, der Rest wandert in Versionen-/Hashlog.

## Stempel-Spezifikation

- **Position:** rechter oberer Rand, ca. 1.5 cm vom oberen / rechten Rand.
- **Schrift:** Arial 12 pt regular.
- **Format:** `Anlage K 7` (Leerzeichen zwischen Präfix und Zahl).
- **Mehrseitige Anlagen:** Stempel nur Seite 1 (Standard); Option `--stempel jede-seite`.
- **Konvolute:** Deckblatt + Einzeldokumente mit Suffix `K 5/1`, `K 5/2` usw.

## Datei-Benennung (beA-/ERV-tauglich)

Beispiel: `anlage-k-003_2024-03-15_werkvertrag-lackieranlage.pdf`

Regeln: keine Umlaute in Dateinamen (`ae/oe/ue/ss`), keine Leerzeichen, stabile Nullfüllung (`001` bis `247`), Datum im Format `JJJJ-MM-TT`, Kurzbeschreibung ohne Sonderzeichen. Im normalen menschlichen Text bleiben Umlaute und `ß` erhalten.

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

Zusätzlich bei großen Akten:

```
kontrolle/
 belegmatrix.xlsx
 hash-und-duplikatlog.csv
 lueckenliste.md
 redaktionsprotokoll.md
 bea-versandplan.md
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

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
| Lesbarkeit/OCR | keine / K [...] unleserlich oder nicht durchsuchbar |
| Schwärzung/Geheimnisse | keine / K [...] vor Versand prüfen |
| beA-/ERV-Paket | keine / Paket [...] zu groß oder falsch benannt |

**Ergebnis:** [Kein Handlungsbedarf / Korrekturen erforderlich — Korrekturplan: ...]

---

Hinweis: Die Letztverantwortung für Vollständigkeit, Tatsachenvortrag, Verschwiegenheit (§ 43a BRAO, § 203 StGB), Datenschutz und Versand liegt beim Anwalt.
