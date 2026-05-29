---
name: wuerfel-aufbauen
description: "3D-Wuerfelstruktur für den Tabellenreview aufbauen: Zeilen, Spalten, Perspektiven verknuepfen. Normen: §§ 174 ff. InsO. Prüfraster: Dimensionen-Vollständigkeit, Verknuepfungslogik, Konfiguration. Output: Wuerfelkonfigurationsdokument. Abgrenzung: nicht Prüfungsdurchführung."
---

# /tabellenreview-3d:würfel-aufbauen


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Bevor ein Reviewlauf startet, muss die Würfel-Struktur stehen. Dieser Skill fragt die drei Achsen ab und schreibt sie in eine versionierte `wuerfel-schema.yaml`. Die Reviewlauf-Skills lesen ausschließlich diese Datei. Wer den Würfel ändern will ändert das Schema; nichts verschwindet still.

## Eingaben

- Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/CLAUDE.md`
- Projektname (kebab-case)
- Anwendungsfall (M&A-DD / Immobilien / Vendor / Arbeitsvertrag / Mietvertrag / Anlage / Eigenwürfel)
- Optional: Vorlage aus dem Plugin (siehe Skills `vorlage-*`)
- Optional: bestehende Spaltenprompt-Bibliothek

## Methodik

1. **Achse 1 — Spalten (Datenpunkte) definieren**
   - Jede Spalte ist ein Spaltenprompt: eine einzige präzise Frage, die für ALLE Dokumente gleich beantwortet wird.
   - Pflichtfelder pro Spalte: `id`, `titel`, `prompt`, `antworttyp` (Freitext / Zitat-mit-Fundstelle / ja-nein / Datum / Geldbetrag / Aufzählung), `pflichtfeld` (ja / nein), `ampel-regel` (wann rot / gelb / grün).
2. **Achse 2 — Zeilen (Dokumente) definieren**
   - Jede Zeile ist ein Dokument mit Quellpfad Hash und optionalem Zeilenprompt.
   - Pflichtfelder pro Zeile: `id`, `pfad`, `hash`, `dokumenttyp`, optional `zeilenprompt` für dokumentspezifische Sonderanweisungen.
3. **Achse 3 — Arbeitsblätter (Perspektiven) definieren**
   - Jedes Arbeitsblatt ist eine eigene Pruefperspektive die über denselben Dokumentenstapel läuft.
   - Beispiele: Recht (Anwaltsperspektive) / Steuer (Steuerberater) / Wirtschaft (Buyside) / Datenschutz (DSGVO) / IT (Architektur) / Betrieb (Operations)
   - Pflichtfelder pro Arbeitsblatt: `id`, `titel`, `perspektive`, `eigene-spalten-zusätze` (Arbeitsblatt-spezifische Zusatzspalten) und `auslassungen` (Spalten die für dieses Blatt nicht gelten).
4. **Risikoampel-Konsolidierung** je Achse festlegen: Wann ist eine Zelle rot? Wann eine ganze Zeile rot? Wann ein ganzes Arbeitsblatt rot?
5. **Belegkette-Konvention:** jedes Zitat in einer Zelle muss zurückverfolgbar sein auf Datei-Hash und Stelle (Seite Absatz Ziffer).
6. **Audit-Trail:** Prompt-Versionen Reviewlauf-Zeitstempel Prüfer-Abnahmen werden separat protokolliert.

## Ausgabe

- `wuerfel-schema.yaml` mit allen drei Achsen, vollständig definiert
- `wuerfel-vorschau.md` — menschenlesbare Übersicht zur Prüfer-Abnahme
- Optional: `spaltenprompt-bibliothek.yaml` als Referenz auf Standard-Spaltenprompts

## Quellenpflicht

Verbindlich gegen `references/zitierweise.md` im Repository. Jede juristische Anspielung im Spaltenprompt benötigt einen Verweis auf Norm Rechtsprechung oder Kommentarstelle.

## Beispiel

Würfel für M&A-DD bei Erwerb einer SaaS-GmbH:
- **Spalten:** 12 Datenpunkte (Vertragsart Laufzeit Kündigungsfrist Change-of-Control Abtretungsverbot Haftungsbegrenzung Service-Level Datenschutz-Auftragsverarbeitung Geheimhaltung Vergütung-Anpassungsklausel anwendbares Recht Gerichtsstand)
- **Zeilen:** 87 Verträge aus dem Datenraum (Kunden Lieferanten Banken Lizenzen Personal)
- **Arbeitsblätter:** 4 Perspektiven (Recht / Steuer / Wirtschaft / Datenschutz)
- Ergebnis: 12 mal 87 mal 4 = 4176 Zellen, jede mit wörtlichem Zitat und Fundstelle.

## Grenzen

Das Schema ist nur die Architektur. Der eigentliche Reviewlauf erfolgt im Skill `review-durchfuehren`. Wer das Schema nachträglich ändert nachdem schon ein Lauf erfolgt ist muss `prompt-versionierung` und `caching-und-teil-rerun` beachten.
