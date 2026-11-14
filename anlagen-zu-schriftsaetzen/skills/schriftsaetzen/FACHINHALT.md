---
name: schriftsaetzen
description: "Für Zuordnung von Anlagen zu gerichtlichen Schriftsätzen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
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
- Mehrseitige Anlagen: Bezeichnung auf jeder Seite oben rechts; das Werkzeug verwendet dies als Standard. Nur bei einer ausdrücklich dokumentierten abweichenden Vorgabe darf `--stempel-seiten erste` gewählt werden.
- **Konvolute:** Deckblatt + Einzeldokumente mit Suffix `K 5/1`, `K 5/2` usw.

## Datei-Benennung (beA-/ERV-tauglich)

Beispiel im strengen Gerichtsprofil: `003_20240315_AnlageK3_Werkvertrag.pdf`

Regeln: Gerichtshinweis zuerst prüfen. Im strengen Sicherheitsprofil keine Umlaute, keine Leerzeichen, stabile Nullfüllung, Datum als `JJJJMMTT`, Kurzbeschreibung mit Unterstrichen und insgesamt höchstens 60 Zeichen. Die ERVB 2025 erlaubt bundesweit bis zu 90 Zeichen und auch Umlaute; der strengere ASCII-Standard ist eine Kanzleientscheidung. Im normalen Text bleiben Umlaute und `ß` erhalten.

## Ausgabe

```
anlagen/
 Anlage_K-01_<Kurzbeschreibung>.pdf
 Anlage_K-02_<Kurzbeschreibung>.pdf
 …
 versandfertig/00_..._Schriftsatz.pdf
 versandfertig/01_..._AnlageK1_....pdf
 intern/Anlagenkonvolut_Prueffassung.pdf
 intern/Anlagenverzeichnis.pdf
 intern/Anlagenverzeichnis.md
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
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
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
| Abweichung vom gewählten Dateinamensprofil | keine / Datei: [...] |
| Lesbarkeit/OCR | keine / K [...] unleserlich oder nicht durchsuchbar |
| Schwärzung/Geheimnisse | keine / K [...] vor Versand prüfen |
| beA-/ERV-Paket | keine / Paket [...] zu groß oder falsch benannt |

**Ergebnis:** [Kein Handlungsbedarf / Korrekturen erforderlich — Korrekturplan: ...]

---

Hinweis: Die Letztverantwortung für Vollständigkeit, Tatsachenvortrag, Verschwiegenheit (§ 43a BRAO, § 203 StGB), Datenschutz und Versand liegt beim Anwalt.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
