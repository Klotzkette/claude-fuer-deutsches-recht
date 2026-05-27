---
name: datenschutzrecht-kaltstart-interview
description: "Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen. Art. 5 6 DSGVO Grundsaetze § 26 BDSG Beschaeftigtendaten. Pruefraster: Verarbeitungszweck Datenarten betroffene Personen Empfaenger Aufbewahrungsdauer Risiken. Output: Mandatssteckbrief Verarbeitungsregister-Entwurf fehlende Informationen. Abgrenzung: nicht fuer laufendes Mandat."
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
DSB: [Name], intern, bestellt nach Art. 37 DSGVO / § 38 BDSG
Drittlandtransfer: nein (Hosting Frankfurt, alle Sub-AVs EU)
Deal-Breaker: Sub-AV-Wechsel ohne 4-Wochen-Vorankündigung
```

## Risiken / typische Fehler

- **Falsche Aufsichtsbehörde:** Niederlassungsprinzip Art. 56 DSGVO und § 19 BDSG – Hauptniederlassung der Organisation, nicht Serverstandort, ist maßgeblich. Bei grenzüberschreitender Verarbeitung ist federführende Behörde zu bestimmen.
- **DSB-Benennungspflicht übersehen:** Pflicht nach Art. 37 DSGVO besteht ab Kerngeschäft mit Verarbeitungen, die regelmäßige systematische Überwachung erfordern, oder bei Verarbeitung besonderer Kategorien im großen Umfang; §§ 37–39 BDSG ergänzen.
- **CLAUDE.md ohne Verarbeitungsverzeichnis:** Ohne Systemliste können spätere DSAR-Abfragen keine vollständige Antwort liefern; Nutzer vor Abschluss darauf hinweisen.
- **AVV-Extraktion zu oberflächlich:** Das Playbook muss konkrete Fallback-Positionen enthalten, sonst gibt `avv-pruefung` immer den generischen Standard aus.
- **Integrations-Check:** Nur ✓ bei erfolgreichem Test-Aufruf; konfiguriert ≠ funktioniert.

## Quellen / Updates

Stand: 05/2026. Bei Änderungen der Aufsichtsbehördenstruktur (Art. 56 DSGVO), BRAO-Novellen oder Änderungen des BDSG Skill aktualisieren.

**Querverweise:**
- `datenschutzrecht/skills/datenschutzrecht-anpassen/SKILL.md` — Gezielte Anpassung einzelner Profil-Abschnitte ohne Vollinterview
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Drittlandtransfer-Konfiguration im Praxisprofil

## Aktuelle Rechtsprechung (v14.2)

- EuGH, Urt. v. 09.03.2023 — C-453/21 (X-FAB Dresden), NJW 2023, 1549 Rn. 30–48: DSB-Unabhängigkeit nach Art. 38 Abs. 3 DSGVO; keine leitende Position, die eigene Datenschutzüberwachung erfordert — Kaltstart muss DSB-Interessenkonflikte abfragen.
- EuGH, Urt. v. 15.06.2021 — C-645/19 (Facebook Ireland), NJW 2021, 2463 Rn. 55–78: Federführende Aufsichtsbehörde nach Art. 56 DSGVO richtet sich nach tatsächlicher Hauptniederlassung — Kaltstart muss Unternehmensstruktur und Hauptniederlassung klären.
- BGH, Urt. v. 23.01.2024 — VI ZR 7/23, NJW 2024, 1200 Rn. 28: § 26 BDSG gilt als lex specialis für Beschäftigtendaten — Kaltstart muss Verarbeitungskategorien und anwendbare Spezialgesetze klären.
- BVerwG, Urt. v. 27.04.2022 — 6 C 8.20, BVerwGE 175, 234 Rn. 38: Zur Behördenzuständigkeit nach Art. 56 DSGVO bei grenzüberschreitenden Verarbeitungen — relevant für die Konfiguration der zuständigen Aufsichtsbehörde.

## Triage zu Beginn

1. Erstmalige Einrichtung oder Update des Praxisprofils?
2. Liegt bereits eine CLAUDE.md vor? Falls ja: Welche Abschnitte sollen aktualisiert werden?
3. Welche Dokumente stehen bereit? (Datenschutzerklärung, VVT, bestehende AVV)
4. Welche Rechtsgebiete sind relevant? (rein DSGVO / zusätzlich BDSG / TKG-TDDDG / KRITIS)

## Output-Template — Praxisprofil-Zusammenfassung

**Adressat:** DSB / Kanzlei intern — Tonfall: sachlich-strukturiert

```
Praxisprofil-Zusammenfassung [DATUM]
Organisation: [NAME, RECHTSFORM]
Sitz: [ORT, LAND]
Federführende Aufsichtsbehoerde: [BEHOERDE]
DSB: [NAME, intern/extern]
Hauptrolle: Verantwortlicher / Auftragsverarbeiter / beide
Hauptverarbeitungstaetigkeiten: [KURZBESCHREIBUNG]
Drittlandtransfers: [ja/nein; Laender]
AVV-Playbook: konfiguriert / nicht konfiguriert
Systemliste: konfiguriert / nicht konfiguriert
Naechste Schritte: [LISTE]
```
