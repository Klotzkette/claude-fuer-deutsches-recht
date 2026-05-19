# Datenschutzrecht-Plugin

Datenschutzrechtliche Arbeitsabläufe für Kanzleien und Datenschutzbeauftragte: AVV-Prüfung, Betroffenenauskunft, Datenschutz-Folgenabschätzung, regulatorische Lückenanalyse und Richtlinien-Monitoring. Vollständig ausgerichtet auf DSGVO, BDSG, TTDSG und KUG. Entwickelt für deutsche und EU-ansässige Verantwortliche und Auftragsverarbeiter.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, gekennzeichnet und freigabepflichtig, keine abschließende Rechtsauskunft.** Das Plugin übernimmt die Arbeit: es liest Dokumente, wendet Ihr Praxisprofil an, findet Schwachstellen und verfasst Memos. Der Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Herkunft gekennzeichnet (Modellwissen vs. abgerufen). Mandatsgeheimnisschutz (§ 43a Abs. 2 BRAO, § 203 StGB) wird konservativ gehandhabt. Folgenreiche Maßnahmen – Übermittlung an Aufsichtsbehörden, Versand von Betroffenenschreiben, Vertragsunterzeichnung – werden erst nach ausdrücklicher Bestätigung durchgeführt.

## Zielgruppe

| Rolle | Hauptarbeitsabläufe |
|---|---|
| **Datenschutzbeauftragte·r (intern/extern)** | AVV-Prüfung, DSFA, DS-Gap-Analyse, Verarbeitungsverzeichnis |
| **Datenschutz-Counsel / Datenschutzanwalt** | Betroffenenanfragen, Datenpannen-Meldung, Mandantendaten-KI |
| **Compliance-/Datenschutzmanager** | Richtlinien-Monitoring, Schwellwertanalyse, Triage neuer Verarbeitungstätigkeiten |
| **Produktverantwortliche / Entwickler** | DSFA-Einstieg, Rechtsgrundlagen-Triage, Einwilligungsgestaltung |
| **Sachbearbeitung / Support** | Betroffenenanfragen-Erstbearbeitung (mit Eskalation) |

## Ersteinrichtung: Cold-Start-Interview

Das Plugin befragt Sie zur Identifikation Ihrer Organisation: Verantwortlicher oder Auftragsverarbeiter? Welche Verarbeitungstätigkeiten? Zuständige Aufsichtsbehörde (BfDI oder zuständiger LfDI)? Interner oder externer DSB? Anschließend liest es drei Ausgangsdokumente – Datenschutzerklärung, AVV-Vorlage, eine abgeschlossene DSFA – und erlernt Ihre Positionen und Ihren Kanzleistil.

Die Konfiguration wird gespeichert unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/CLAUDE.md` und bleibt bei Plugin-Updates erhalten.

```
/datenschutzrecht:kaltstart-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/datenschutzrecht:kaltstart-interview` | Ersteinrichtung |
| `/datenschutzrecht:anwendungsfall-triage [Verarbeitungstätigkeit]` | Benötigt diese Verarbeitung eine DSFA? Triage + Rechtsgrundlage |
| `/datenschutzrecht:avv-pruefung [Datei]` | AVV-Prüfung nach Art. 28 DSGVO (Richtung automatisch erkannt) |
| `/datenschutzrecht:dsgvo-auskunft-antwort` | Betroffenenanfrage (Art. 15–22 DSGVO) vollständig bearbeiten |
| `/datenschutzrecht:dsfa-erstellung [Vorhaben]` | DSFA nach Art. 35 DSGVO erstellen |
| `/datenschutzrecht:regulierungs-luecken-analyse [Leitlinie/Gesetz]` | Lückenanalyse neue Anforderung vs. aktueller Praxis |
| `/datenschutzrecht:richtlinien-monitor` | Wöchentlicher Drift-Scan der Datenschutzerklärung und Richtlinien |
| `/datenschutzrecht:mandats-arbeitsbereich` | Mandate verwalten (für Mehrmandat-Kanzleien): neu, liste, wechsle, schließe |

## Skills

| Skill | Funktion |
|---|---|
| **kaltstart-interview** | Schreibt CLAUDE.md aus Interview und Ausgangsdokumenten |
| **anwendungsfall-triage** | DSFA-Pflicht? Verzeichnisaufnahme, Rechtsgrundlage Art. 6/9 DSGVO |
| **avv-pruefung** | AVV-Prüfung bi-direktional (Verantwortlicher/Auftragsverarbeiter), Art. 28 DSGVO, Sub-AV, TIA, EU-SCC, DPF |
| **dsgvo-auskunft-antwort** | Identitätsprüfung → Systemabfrage → Ausnahmen → Antwortentwurf (Art. 15–22, 12 Abs. 3 DSGVO) |
| **dsfa-erstellung** | DSFA nach Art. 35 DSGVO, BfDI-Blacklist/-Whitelist, Schwellwertanalyse |
| **regulierungs-luecken-analyse** | Neue Leitlinie/VO vs. Ist-Zustand; EDSA- und DSK-Leitlinien |
| **richtlinien-monitor** | Drift-Monitoring Datenschutzerklärung; Entwurf von Aktualisierungen |
| **mandats-arbeitsbereich** | Mandate anlegen, auflisten, wechseln und schließen für Mehrmandat-Kanzleien |
| **dsgvo-auskunft** | Vollständiger Arbeitsablauf Auskunft Art. 15 DSGVO, Fristen, Ausnahmen § 34 BDSG |
| **datenpanne-meldung** | Datenpanne Art. 33/34 DSGVO: 72h-Meldung, Betroffenenbenachrichtigung, Dokumentation |
| **mandantendaten-ki** | Verarbeitung von Mandantendaten in KI-Tools: § 203 StGB, BRAO, Art. 28 DSGVO AVV |

## Schnellstart

### 1. Einrichtung

```
/datenschutzrecht:kaltstart-interview
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

### 4. Betroffenenanfrage bearbeiten

```
/datenschutzrecht:dsgvo-auskunft-antwort
```

Geführter Ablauf: klassifizieren → Identität prüfen → Daten lokalisieren → Ausnahmen prüfen → Antwortentwurf. Fristen nach Art. 12 Abs. 3 DSGVO werden automatisch berechnet.

### 5. DSFA für ein neues Vorhaben

```
/datenschutzrecht:dsfa-erstellung "Einsatz eines KI-gestützten Bewerbermanagementsystems"
```

Eingangsabfragen → DSFA in Ihrem Kanzleiformat → Konsistenzprüfung → Auflagenliste.

### 6. Datenpanne melden

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
│   ├── kaltstart-interview/
│   ├── anwendungsfall-triage/
│   ├── avv-pruefung/
│   ├── dsgvo-auskunft-antwort/
│   ├── dsfa-erstellung/
│   ├── regulierungs-luecken-analyse/
│   ├── richtlinien-monitor/
│   ├── mandats-arbeitsbereich/
│   ├── dsgvo-auskunft/
│   ├── datenpanne-meldung/
│   └── mandantendaten-ki/
└── ausloeser/ausloeser.json
```

## Hinweise

- **Bidirektionale AVV-Prüfung:** Derselbe Skill behandelt eingehende Anbieter-AVVs (operative Flexibilität verteidigen) und ausgehende Auftraggeber-AVVs (Datenschutz der Betroffenen sichern). Richtung wird automatisch erkannt oder kann angegeben werden.
- **DSFA-Format:** Das Format richtet sich nach Ihrer Referenz-DSFA. Wurde keine angegeben, wird die DSFA-Methodik der Artikel-29-Gruppe / des EDSA genutzt – erneutes Setup mit einer Referenz-DSFA verbessert die Passgenauigkeit.
- **Lückenanalyse vs. Policy-Monitor:** `regulierungs-luecken-analyse` analysiert eingehende neue Anforderungen (neue EDSA-Leitlinie, Gesetzesänderung). `richtlinien-monitor` überwacht internen Praxis-Drift. Zwei unterschiedliche Werkzeuge für zwei Richtungen der Veränderung.
- **Aufsichtsbehörden:** Das Plugin kennt BfDI (Bundesebene) und alle 16 LfDI (Länderebene). Die zuständige Behörde wird aus der Organisationshauptschaft und dem Verarbeitungskontext bestimmt.
- **Zitierweise:** Verbindlich nach `../references/zitierweise.md` (BGH-Stil). Alle normativen Verweise folgen dem dortigen Schema.
