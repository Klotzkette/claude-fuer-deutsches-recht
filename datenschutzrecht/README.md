# Datenschutzrecht-Plugin

Datenschutzrechtliche Arbeitsabläufe für Kanzleien und Datenschutzbeauftragte: AVV-Prüfung, Betroffenenauskunft, Datenschutz-Folgenabschätzung, Drittlandstransfer-Prüfung, regulatorische Lückenanalyse und Richtlinien-Monitoring. Vollständig ausgerichtet auf DSGVO, BDSG, TDDDG und KUG. Entwickelt für deutsche und EU-ansässige Verantwortliche und Auftragsverarbeiter.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, gekennzeichnet und freigabepflichtig, keine abschließende Rechtsauskunft.** Das Plugin übernimmt die Arbeit: es liest Dokumente, wendet Ihr Praxisprofil an, findet Schwachstellen und verfasst Memos. Der Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Herkunft gekennzeichnet (Modellwissen vs. abgerufen). Mandatsgeheimnisschutz (§ 43a Abs. 2 BRAO, § 203 StGB) wird konservativ gehandhabt. Folgenreiche Maßnahmen – Übermittlung an Aufsichtsbehörden, Versand von Betroffenenschreiben, Vertragsunterzeichnung – werden erst nach ausdrücklicher Bestätigung durchgeführt.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Version | Direkt-Download |
| --- | --- | --- |
| Datenschutzrecht (`datenschutzrecht`, dieses Plugin) | v3.3.0 | [datenschutzrecht-v3.3.0.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutzrecht.zip) |
| Datenschutzrecht (neueste Version) | latest | [datenschutzrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutzrecht.zip) |

Die URL zum latest-Release ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP" verwenden.


## Zielgruppe

| Rolle | Hauptarbeitsabläufe |
|---|---|
| **Datenschutzbeauftragte·r (intern/extern)** | AVV-Prüfung, DSFA, DS-Gap-Analyse, Verarbeitungsverzeichnis |
| **Datenschutz-Counsel / Datenschutzanwalt** | Betroffenenanfragen, Datenpannen-Meldung, Mandantendaten-Drittlandtransfer |
| **Compliance-/Datenschutzmanager** | Richtlinien-Monitoring, Schwellwertanalyse, Triage neuer Verarbeitungstätigkeiten |
| **Produktverantwortliche / Entwickler** | DSFA-Einstieg, Rechtsgrundlagen-Triage, Einwilligungsgestaltung |
| **Sachbearbeitung / Support** | Betroffenenanfragen-Erstbearbeitung (mit Eskalation) |

## Ersteinrichtung: Kaltstart-Interview

Das Plugin befragt Sie zur Identifikation Ihrer Organisation: Verantwortlicher oder Auftragsverarbeiter? Welche Verarbeitungstätigkeiten? Zuständige Aufsichtsbehörde (BfDI oder zuständiger LfDI)? Interner oder externer DSB? Anschließend liest es drei Ausgangsdokumente – Datenschutzerklärung, AVV-Vorlage, eine abgeschlossene DSFA – und erlernt Ihre Positionen und Ihren Kanzleistil.

Die Konfiguration wird gespeichert unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/CLAUDE.md` und bleibt bei Plugin-Updates erhalten.

```
/datenschutzrecht:datenschutzrecht-kaltstart-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/datenschutzrecht:datenschutzrecht-kaltstart-interview` | Ersteinrichtung |
| `/datenschutzrecht:anwendungsfall-triage [Verarbeitungstätigkeit]` | Benötigt diese Verarbeitung eine DSFA? Triage + Rechtsgrundlage |
| `/datenschutzrecht:avv-pruefung [Datei]` | AVV-Prüfung nach Art. 28 DSGVO (Richtung automatisch erkannt) |
| `/datenschutzrecht:dsgvo-auskunft-antwort` | Betroffenenanfrage (Art. 15–22 DSGVO) vollständig bearbeiten |
| `/datenschutzrecht:dsfa-erstellung [Vorhaben]` | DSFA nach Art. 35 DSGVO erstellen |
| `/datenschutzrecht:drittlandstransfer-pruefung [Empfaenger/Land]` | Drittlandstransfer nach Art. 44 ff. DSGVO prüfen (neu in v3.3.0) |
| `/datenschutzrecht:regulierungs-luecken-analyse [Leitlinie/Gesetz]` | Lückenanalyse neue Anforderung vs. aktueller Praxis |
| `/datenschutzrecht:richtlinien-monitor` | Wöchentlicher Drift-Scan der Datenschutzerklärung und Richtlinien |
| `/datenschutzrecht:datenschutzrecht-mandat-arbeitsbereich` | Mandate verwalten (für Mehrmandat-Kanzleien): neu, liste, wechsle, schließe |

## Skills (13)

| Skill | Funktion |
|---|---|
| **kaltstart-interview** | Schreibt CLAUDE.md aus Interview und Ausgangsdokumenten |
| **anwendungsfall-triage** | DSFA-Pflicht? Verzeichnisaufnahme, Rechtsgrundlage Art. 6/9 DSGVO |
| **avv-prüfung** | AVV-Prüfung bi-direktional (Verantwortlicher/Auftragsverarbeiter), Art. 28 DSGVO, Sub-AV, TIA, EU-SCC, DPF |
| **dsgvo-auskunft** | Vollständiger Arbeitsablauf Auskunft Art. 15 DSGVO, Fristen, Ausnahmen § 34 BDSG, Rechtsmissbrauchsprüfung (EuGH C-526/24) |
| **dsgvo-auskunft-antwort** | Identitätsprüfung → Systemabfrage → Ausnahmen → Antwortentwurf (Art. 15–22, Art. 12 Abs. 3 DSGVO) |
| **dsfa-erstellung** | DSFA nach Art. 35 DSGVO, BfDI-Blacklist/-Whitelist, Schwellwertanalyse |
| **drittlandstransfer-prüfung** | Drittlandstransfer Art. 44 ff. DSGVO: Angemessenheitsbeschlüsse, SCC 2021 Module 1–4, TIA nach Schrems II, BCR — **neu in v3.3.0** |
| **regulierungs-luecken-analyse** | Neue Leitlinie/VO vs. Ist-Zustand; EDSA- und DSK-Leitlinien |
| **richtlinien-monitor** | Drift-Monitoring Datenschutzerklärung; Entwurf von Aktualisierungen |
| **mandats-arbeitsbereich** | Mandate anlegen, auflisten, wechseln und schließen für Mehrmandat-Kanzleien |
| **datenpanne-meldung** | Datenpanne Art. 33/34 DSGVO: 72h-Meldung, Betroffenenbenachrichtigung, Dokumentation |
| **mandantendaten-ki** | Verarbeitung von Mandantendaten in externen IT-/KI-Diensten: § 203 StGB, BRAO, Art. 28 DSGVO AVV |
| **datenschutzrecht-anpassen** | Praxisprofil gezielt anpassen ohne vollständiges Neu-Interview |

## Schnellstart

### 1. Einrichtung

```
/datenschutzrecht:datenschutzrecht-kaltstart-interview
```

Bereithalten: URL Ihrer Datenschutzerklärung, AVV-Mustervorlage, eine abgeschlossene DSFA.

### 2. Neue Verarbeitungstätigkeit prüfen

```
/datenschutzrecht:anwendungsfall-triage "Marketing möchte Verhaltensdaten für personalisierte Werbung nutzen"
```

Ergebnis: ZULÄSSIG / DSFA EMPFOHLEN / DSFA ERFORDERLICH / STOP – mit Bedingungstabelle, Rechtsgrundlagen-Analyse und Angebot zum direkten DSFA-Start.

### 3. AVV eines Anbieters prüfen

```
/datenschutzrecht:avv-pruefung anbieter-avv.pdf
```

Ergebnis: Richtung automatisch erkannt, Klausel-für-Klausel-Vergleich mit Ihrem Vorgehensleitfaden, Änderungsvorschläge, Konsistenzprüfung gegen Datenschutzerklärung.

### 4. Drittlandstransfer prüfen (neu in v3.3.0)

```
/datenschutzrecht:drittlandstransfer-pruefung "US-Cloud-Dienst, Hosting Virginia"
```

Ergebnis: Angemessenheitsbeschluss-Check, SCC-Modul-Empfehlung, TIA-Checkliste, Risikoampel.

### 5. Betroffenenanfrage bearbeiten

```
/datenschutzrecht:dsgvo-auskunft-antwort
```

Geführter Ablauf: klassifizieren → Identität prüfen → Daten lokalisieren → Ausnahmen prüfen → Antwortentwurf. Fristen nach Art. 12 Abs. 3 DSGVO werden automatisch berechnet.

### 6. DSFA für ein neues Vorhaben

```
/datenschutzrecht:dsfa-erstellung "Einsatz eines KI-gestützten Bewerbermanagementsystems"
```

Eingangsabfragen → DSFA in Ihrem Kanzleiformat → Konsistenzprüfung → Auflagenliste.

### 7. Datenpanne melden

```
/datenschutzrecht:datenpanne-meldung
```

72h-Frist nach Art. 33 DSGVO: Sachverhalt → Risikobewertung → Meldung an BfDI/LfDI → ggf. Betroffenenbenachrichtigung Art. 34 DSGVO → interne Dokumentation.

## Lernfähigkeit

Das Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/CLAUDE.md` ist nicht statisch – es verbessert sich bei Nutzung. Skills melden, wenn eine Ausgabe auf einem Standard basiert, den Sie anpassen sollten. Der `richtlinien-monitor`-Skill überwacht den Drift zwischen Datenschutzerklärung und gelebter Praxis und schlägt Aktualisierungen vor. Das Interview kann jederzeit wiederholt werden.

## Verzeichnisstruktur

```
datenschutzrecht/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md
├── README.md
├── skills/
│   ├── anwendungsfall-triage/
│   ├── avv-pruefung/
│   ├── datenpanne-meldung/
│   ├── datenschutzrecht-anpassen/
│   ├── datenschutzrecht-kaltstart-interview/
│   ├── datenschutzrecht-mandat-arbeitsbereich/
│   ├── drittlandstransfer-pruefung/       ← neu in v3.3.0
│   ├── dsfa-erstellung/
│   ├── dsgvo-auskunft/
│   ├── dsgvo-auskunft-antwort/
│   ├── mandantendaten-ki/
│   ├── regulierungs-luecken-analyse/
│   └── richtlinien-monitor/
└── ausloeser/ausloeser.json
```

## Hinweise

- **Bidirektionale AVV-Prüfung:** Derselbe Skill behandelt eingehende Anbieter-AVVs (operative Flexibilität verteidigen) und ausgehende Auftraggeber-AVVs (Datenschutz der Betroffenen sichern). Richtung wird automatisch erkannt oder kann angegeben werden.
- **DSFA-Format:** Das Format richtet sich nach Ihrer Referenz-DSFA. Wurde keine angegeben, wird die DSFA-Methodik der Artikel-29-Gruppe / des EDSA genutzt – erneutes Setup mit einer Referenz-DSFA verbessert die Passgenauigkeit.
- **Lückenanalyse vs. Policy-Monitor:** `regulierungs-luecken-analyse` analysiert eingehende neue Anforderungen (neue EDSA-Leitlinie, Gesetzesänderung). `richtlinien-monitor` überwacht internen Praxis-Drift. Zwei unterschiedliche Werkzeuge für zwei Richtungen der Veränderung.
- **Drittlandstransfer (neu v3.3.0):** `drittlandstransfer-pruefung` deckt den gesamten Prüfpfad nach Kapitel V DSGVO ab — von der Angemessenheitsbeschluss-Prüfung über SCC-Modul-Auswahl bis zum Transfer Impact Assessment nach EuGH C-311/18 Schrems II. Quervernetzt mit `avv-pruefung` und `dsfa-erstellung`.
- **Aufsichtsbehörden:** Das Plugin kennt BfDI (Bundesebene) und alle 16 LfDI (Länderebene). Die zuständige Behörde wird aus der Organisationshauptschaft und dem Verarbeitungskontext bestimmt.
- **Zitierweise:** Verbindlich nach `../references/zitierweise.md` (BGH-Stil). Alle normativen Verweise folgen dem dortigen Schema.

## Changelog

### v3.3.0 (05/2026)
- **Neuer Skill:** `drittlandstransfer-pruefung` — vollständige Prüfung nach Art. 44 ff. DSGVO inkl. EU-US Data Privacy Framework 2023, SCC 2021 Module 1–4, TIA nach EuGH C-311/18 Schrems II
- **dsgvo-auskunft:** Neuer Abschnitt Rechtsmissbrauch nach EuGH C-526/24 (Brillen Rottler, 19.03.2026) mit zweistufigem Prüfschema; EuGH C-579/21 (Protokolldaten) ergänzt
- **dsgvo-auskunft-antwort:** Neuer Abschnitt Ablehnung wegen Rechtsmissbrauch mit Formulierungsbausteinen; EuGH C-579/21 und C-487/21 ergänzt
- **avv-prüfung:** EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher/Auftragsverarbeiter ergänzt
- **datenpanne-meldung:** Quellen/Updates und Cross-Refs ergänzt (EuGH C-340/21 war bereits enthalten)
- **mandantendaten-ki:** Querverweis auf geplantes Plugin `ki-richtlinie-kanzleien` (ab v3.3.0)
- Alle 13 Skills: Abschnitt „Quellen / Updates" ergänzt; Cross-References zwischen verwandten Skills ausgebaut
- `plugin.json` Version auf 3.3.0, description aktualisiert (TDDDG → TDDDG, Drittlandstransfer ergänzt)
