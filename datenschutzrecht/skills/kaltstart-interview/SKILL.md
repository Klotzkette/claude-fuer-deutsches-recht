---
name: kaltstart-interview
description: "Ersteinrichtung des Datenschutzrecht-Plugins – erlernt Ihre Datenschutzpraxis und schreibt CLAUDE.md aus Interview und Ausgangsdokumenten. Auslöser: erster Start, CLAUDE.md fehlt oder enthält Platzhalter, Nutzer sagt „Plugin einrichten\", „konfigurieren\", „neu starten\" oder „Interview wiederholen\"."
---

# Kaltstart-Interview – Datenschutzrecht

## Zweck

Dieses Interview richtet das Plugin auf Ihre konkrete Datenschutzpraxis aus: Wer sind Sie als Verantwortlicher oder Auftragsverarbeiter? Welche Rechtsgrundlagen nutzen Sie? Welche Aufsichtsbehörde ist zuständig? Was darf in einem AVV nicht stehen? Die Antworten landen in `CLAUDE.md` – der Wissensbasis, die jeder andere Skill als Grundlage nutzt.

## Eingaben

- Öffentliche URL der Datenschutzerklärung oder Datei
- AVV-Mustervorlage (Datei oder Paste)
- Eine abgeschlossene, inhaltlich akzeptable DSFA als Referenz
- Optional: Verarbeitungsverzeichnis nach Art. 30 DSGVO (gibt dem Plugin eine Systemübersicht)

## Ablauf

1. **Voraussetzungs-Check.**
   - `~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/CLAUDE.md` prüfen.
   - Wenn befüllt (keine `[PLATZHALTER]`) und kein `--redo`: Bestätigung einholen, bevor überschrieben wird.
   - Wenn altes Cache-Profil unter `~/.claude/plugins/cache/…` vorhanden: automatisch übertragen, dem Nutzer mitteilen.

2. **Organisations-Interview.** Folgende Fragen stellen (gebündelt, nicht einzeln):
   - Organisations- oder Kanzleiname, Rechtsform, Hauptniederlassung (Bundesland)
   - Primär Verantwortlicher, Auftragsverarbeiter oder beides? Für welche Daten?
   - Welche Rechtsgrundlagen Art. 6 DSGVO kommen hauptsächlich zur Anwendung?
   - Werden besondere Kategorien (Art. 9 DSGVO) oder Beschäftigtendaten (§ 26 BDSG) verarbeitet?
   - Gibt es einen bestellten DSB? Intern oder extern? Name und Kontakt?
   - Zuständige Aufsichtsbehörde (BfDI oder LfDI – welches Bundesland)?
   - Drittlandtransfers vorhanden? In welche Länder? Welcher Mechanismus (SCC, DPF, Binding Corporate Rules)?
   - Praxisumgebung: Kanzlei / internes Team / öffentliche Stelle?
   - Wer nutzt das Plugin? (Rechtsanwalt, externer DSB, Compliance-Manager, Sachbearbeitung)

3. **Ausgangsdokumente lesen.**
   - Datenschutzerklärung: Datenkategorien, Zwecke, Fristen, Drittempfänger, Rechte, Cookie-Infrastruktur extrahieren.
   - AVV-Vorlage: Klauseln zu Sub-AV, Audit, Datenpanne, Datenhaltung, Laufzeit, Haftung herausarbeiten; Abweichungen von DSGVO-Mindestanforderungen kennzeichnen.
   - Referenz-DSFA: Struktur, Gliederung, Tiefe, Format für zukünftige DSFAs übernehmen.
   - Verarbeitungsverzeichnis (falls bereitgestellt): Systemliste für DSAR-Abfragen übernehmen.

4. **AVV-Playbook-Fragen.**
   - Wo sind Sie Deal-Breaker-sensibel? (z.B. Sub-AV-Transparenz, Datenhaltung EU)
   - Was akzeptieren Sie unter keinen Umständen?
   - Welche Klauseln sind Standard-Fallback?

5. **Integrations-Check.**
   - Dokumentenspeicher (Drive / SharePoint / lokaler Pfad) testen.
   - Benachrichtigungskanal (Slack / Teams / E-Mail) testen.
   - Aufgabenplanung testen.
   - Nur ✓ melden, wenn ein Tool-Aufruf tatsächlich funktioniert hat; konfiguriert-aber-ungetestet als ⚪ ausweisen.

6. **`CLAUDE.md` schreiben.**
   - Alle Platzhalter mit den ermittelten Werten befüllen.
   - Übergeordnetes `organisation-profil.md` anlegen oder aktualisieren.
   - Zusammenfassung der geschriebenen Konfiguration zeigen.
   - Ersten nützlichen Befehl anbieten.

## `--check-integrations`

Führt nur Schritt 5 erneut aus. Aktualisiert den Abschnitt `## Verfügbare Integrationen` in `CLAUDE.md`. Kein erneutes Interview. Nutzen, wenn ein MCP-Connector neu hinzugefügt oder entfernt wurde.

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 13, 14 DSGVO (Informationspflichten – Grundlage für Datenschutzerklärungsanalyse)
- Art. 28, 29 DSGVO (Auftragsverarbeitung – Grundlage für AVV-Analyse)
- Art. 30 DSGVO (Verarbeitungsverzeichnis)
- Art. 35 DSGVO (DSFA-Pflicht – Referenz für DSFA-Strukturanalyse)
- § 38 BDSG (Benennungspflicht DSB)
- Kühling, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 28 Rn. 1 ff.
- Hartung, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 30 Rn. 1 ff.

## Ausgabeformat

Abschlusszusammenfassung als strukturierte Auflistung der geschriebenen Konfiguration:
- Welche Werte aus Interview übernommen
- Welche aus Ausgangsdokumenten extrahiert
- Welche als Fallback-Standard gesetzt (Kennzeichnung: „Standard – bitte anpassen")
- Offene Punkte, die noch ausgefüllt werden müssen
- Erste empfohlene Folgeaktion (z.B. `anwendungsfall-triage` für aktuelle Verarbeitungstätigkeit)

## Beispiel

**Situation:** Mittelständische Softwarefirma, Hauptniederlassung NRW, Auftragsverarbeiter für CRM-Kunden, interner DSB, kein DPF, Hosting in Frankfurt.

**Erwartete Konfiguration (Auszug):**
```
Praxisumgebung: Unternehmen intern
Primär: Auftragsverarbeiter (Art. 28 DSGVO) für Kundendaten
Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO (Vertragserfüllung) für Kunden; Art. 6 Abs. 1 lit. c DSGVO (gesetzliche Pflicht)
Zuständige Aufsichtsbehörde: LfDI NRW (Hauptniederlassung NRW)
DSB: [Name], intern, bestellt nach § 37 DSGVO / § 38 BDSG
Drittlandtransfer: nein (Hosting Frankfurt, alle Sub-AVs EU)
Deal-Breaker: Sub-AV-Wechsel ohne 4-Wochen-Vorankündigung
```

## Risiken / typische Fehler

- **Falsche Aufsichtsbehörde:** Niederlassungsprinzip Art. 56 DSGVO und § 19 BDSG – Hauptniederlassung der Organisation, nicht Serverstandort, ist maßgeblich. Bei grenzüberschreitender Verarbeitung ist federführende Behörde zu bestimmen.
- **DSB-Benennungspflicht übersehen:** Pflicht nach Art. 37 DSGVO besteht ab Kerngeschäft mit Verarbeitungen, die regelmäßige systematische Überwachung erfordern, oder bei Verarbeitung besonderer Kategorien im großen Umfang; §§ 37–39 BDSG ergänzen.
- **CLAUDE.md ohne Verarbeitungsverzeichnis:** Ohne Systemliste können spätere DSAR-Abfragen keine vollständige Antwort liefern; Nutzer vor Abschluss darauf hinweisen.
- **AVV-Extraktion zu oberflächlich:** Das Playbook muss konkrete Fallback-Positionen enthalten, sonst gibt `avv-pruefung` immer den generischen Standard aus.
- **Integrations-Check:** Nur ✓ bei erfolgreichem Test-Aufruf; konfiguriert ≠ funktioniert.
