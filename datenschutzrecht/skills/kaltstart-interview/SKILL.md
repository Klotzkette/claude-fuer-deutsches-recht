---
name: kaltstart-interview
description: "Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen. Art. 5 6 DSGVO Grundsaetze § 26 BDSG Beschäftigtendaten. Prüfraster: Verarbeitungszweck Datenarten betroffene Personen Empfaenger Aufbewahrungsdauer Risiken. Output: Mandatssteckbrief Verarbeitungsregister-Entwurf fehlende Inf..."
---

# Kaltstart-Interview – Datenschutzrecht

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

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

2. **Organisations-Interview.** Folgende Fragen stellen (gebearbeitet, nicht einzeln):
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
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
Drittlandtransfers: [ja/nein; Länder]
AVV-Playbook: konfiguriert / nicht konfiguriert
Systemliste: konfiguriert / nicht konfiguriert
Naechste Schritte: [LISTE]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

