# Datenschutzrecht-Plugin

Datenschutzrechtliche Arbeitsabläufe für Kanzleien und Datenschutzbeauftragte: AVV-Prüfung, Betroffenenauskunft, Datenschutz-Folgenabschätzung, Drittlandstransfer-Prüfung, US-Transfer mit DPF/SCC/TIA, Behördenpaket, regulatorische Lückenanalyse und Richtlinien-Monitoring. Vollständig ausgerichtet auf DSGVO, BDSG, TDDDG und KUG. Entwickelt für deutsche und EU-ansässige Verantwortliche und Auftragsverarbeiter.

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

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **Solis Vision X (Smartglasses, DSGVO/CISG)** | [testakte-solis-vision-x-smartglasses.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-solis-vision-x-smartglasses.zip) |
| **CloudSuite Assist (US-Transfer, DPF/SCC/TIA)** | [testakte-datenschutz-us-transfer-cloudsuite-rheinmain.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-datenschutz-us-transfer-cloudsuite-rheinmain.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Datenschutz: US-Transfer CloudSuite Assist** ([`testakten/datenschutz-us-transfer-cloudsuite-rheinmain/`](../testakten/datenschutz-us-transfer-cloudsuite-rheinmain/)).

Direkt-Download als ZIP: [testakte-datenschutz-us-transfer-cloudsuite-rheinmain.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-datenschutz-us-transfer-cloudsuite-rheinmain.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

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
| `/datenschutzrecht:us-transfer-tia-dokumentation [US-Dienst]` | US-Transfer mit DPF-Listing, Schrems-Historie, SCC/BCR-Ausweichpfad, TIA und ergänzenden Maßnahmen dokumentieren |
| `/datenschutzrecht:standardvertragsklauseln-scc-paket [DPA/SaaS-Vertrag]` | SCC-Modul 1–4 wählen, Annex I–III und Subprozessoren prüfbar vorbereiten |
| `/datenschutzrecht:drittlandtransfer-behoerdenpaket-output [Akte]` | Druckreifes Paket für deutsche Datenschutzaufsicht: Deckvermerk, Nachweise, Antwortschreiben, Maßnahmenplan |
| `/datenschutzrecht:regulierungs-luecken-analyse [Leitlinie/Gesetz]` | Lückenanalyse neue Anforderung vs. aktueller Praxis |
| `/datenschutzrecht:richtlinien-monitor` | Wöchentlicher Drift-Scan der Datenschutzerklärung und Richtlinien |
| `/datenschutzrecht:datenschutzrecht-mandat-arbeitsbereich` | Mandate verwalten (für Mehrmandat-Kanzleien): neu, liste, wechsle, schließe |

## Skills (21)

| Skill | Funktion |
|---|---|
| **kaltstart-interview** | Schreibt CLAUDE.md aus Interview und Ausgangsdokumenten |
| **anwendungsfall-triage** | DSFA-Pflicht? Verzeichnisaufnahme, Rechtsgrundlage Art. 6/9 DSGVO |
| **avv-pruefung** | AVV-Prüfung bi-direktional (Verantwortlicher/Auftragsverarbeiter), Art. 28 DSGVO, Sub-AV, TIA, EU-SCC, DPF |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| **dsgvo-auskunft-antwort** | Identitätsprüfung → Systemabfrage → Ausnahmen → Antwortentwurf (Art. 15–22, Art. 12 Abs. 3 DSGVO) |
| **dsfa-erstellung** | DSFA nach Art. 35 DSGVO, BfDI-Blacklist/-Whitelist, Schwellwertanalyse |
| **drittlandstransfer-pruefung** | Drittlandstransfer Art. 44 ff. DSGVO: Angemessenheitsbeschlüsse, SCC 2021 Module 1–4, TIA nach Schrems II, BCR — **neu in v3.3.0** |
| **us-transfer-tia-dokumentation** | US-Transfer nach Art. 44 ff. DSGVO: EU-US Data Privacy Framework, DPF-Scope, Schrems I/II, SCC/BCR-Ausweichpfad, TIA und supplementary measures |
| **standardvertragsklauseln-scc-paket** | SCC-Modulwahl 1–4, Annex I–III, Subprozessoren, TOMs, AVV-Schnittstelle und Unterzeichnungspaket ohne Veränderung der offiziellen Klauseln |
| **drittlandtransfer-behoerdenpaket-output** | Behördenfähiges Dokumentationspaket mit Deckvermerk, Transferregister, DPF-/SCC-/TIA-Nachweisen, Antwortentwurf und Review-Kalender |
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

### 4a. US-Transfer behördenfest dokumentieren

```
/datenschutzrecht:us-transfer-tia-dokumentation "US-SaaS mit Supportzugriff, DPF behauptet"
/datenschutzrecht:standardvertragsklauseln-scc-paket anbieter-dpa.pdf
/datenschutzrecht:drittlandtransfer-behoerdenpaket-output akte-cloudsuite.zip
```

Ergebnis: DPF-Listing- und Scope-Vermerk, Schrems-I/II-Historie ohne falsche Privacy-Shield-Berufung, SCC-Modul- und Annex-Paket, TIA, TOM-Matrix, Subprozessorenliste, Antwortentwurf für die Aufsichtsbehörde und Wiedervorlage.

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
│   ├── drittlandstransfer-pruefung/
│   ├── us-transfer-tia-dokumentation/
│   ├── standardvertragsklauseln-scc-paket/
│   ├── drittlandtransfer-behoerdenpaket-output/
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
- **Drittlandstransfer:** `drittlandstransfer-pruefung` deckt den allgemeinen Prüfpfad nach Kapitel V DSGVO ab. Für US-Fälle vertieft `us-transfer-tia-dokumentation` DPF, Schrems I/II, SCC/BCR und TIA; `standardvertragsklauseln-scc-paket` baut die SCC-Anlagen; `drittlandtransfer-behoerdenpaket-output` macht daraus ein Behördenpaket.
- **Aufsichtsbehörden:** Das Plugin kennt BfDI (Bundesebene) und alle 16 LfDI (Länderebene). Die zuständige Behörde wird aus der Organisationshauptschaft und dem Verarbeitungskontext bestimmt.
- **Zitierweise:** Verbindlich nach `../references/zitierweise.md` (BGH-Stil). Alle normativen Verweise folgen dem dortigen Schema.

## Changelog

### v21.0.0 Nachlauf (05/2026)
- **Neue Skills:** `us-transfer-tia-dokumentation`, `standardvertragsklauseln-scc-paket`, `drittlandtransfer-behoerdenpaket-output`
- US-Transfer-Workflow trennt aktuelle DPF-Basis, SCC/TIA-Ausweichpfad und historische Safe-Harbor-/Privacy-Shield-Prüfung.
- Neue Testakte `datenschutz-us-transfer-cloudsuite-rheinmain` mit Behördenanfrage, DPF-Vermerk, SCC-Anlagen, TIA, TOMs, Subprozessoren und Antwortentwurf.

### v3.3.0 (05/2026)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **avv-pruefung:** EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher/Auftragsverarbeiter ergänzt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **mandantendaten-ki:** Querverweis auf geplantes Plugin `ki-richtlinie-kanzleien` (ab v3.3.0)
- Alle damals 18 Skills: Abschnitt "Quellen / Updates" ergänzt; Cross-References zwischen verwandten Skills ausgebaut
- `plugin.json` Version auf 3.3.0, description aktualisiert (TDDDG → TDDDG, Drittlandstransfer ergänzt)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 21 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. B... |
| `anwendungsfall-triage` | Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG. Prüfraster: Anwendungsbereich personenbezogene Daten Verantwortlicher Auftragsverarbeiter Drittland. Output: Triage-... |
| `avv-pruefung` | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28 DSGVO AVV-Pflicht § 62 BDSG. Prüfraster: Pflichtinhalte Art. 28 Abs. 3 Weisungsgebundenheit Subauftragsverarbeiter R... |
| `datenpanne-meldung` | Datenpanne nach Art. 33 34 DSGVO melden wenn Sicherheitsverletzung personenbezogener Daten vorliegt. Art. 33 34 DSGVO Meldepflichten § 65 BDSG. Prüfraster: Meldepflicht 72-Stunden-Frist Schwere Risikobewertung Behordenmeldung Betroffenen... |
| `datenschutzrecht-anpassen` | Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. 5 24 DSGVO Rechenschaftspflicht. Prüfraster: Bestandsaufnahme Lueckenanalyse DSGVO-Anforderungen BDSG-Besonderheiten... |
| `datenschutzrecht-kaltstart-interview` | Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen. Art. 5 6 DSGVO Grundsaetze § 26 BDSG Beschaeftigtendaten. Prüfraster: Verarbeitungszweck Datenarten betroffene Personen Empfaenger Aufbewahrungsdauer Risiken. Output:... |
| `datenschutzrecht-mandat-arbeitsbereich` | Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen. Art. 5 24 DSGVO §§ 1 ff. BDSG. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe externe Datenschutzberatung. Output: Mandatssteckbrief Arbeitsplan Rol... |
| `drittlandstransfer-pruefung` | Datentransfer in Drittlaender außerhalb EU und EWR auf Zulässigkeit prüfen. Art. 44 ff. DSGVO Kapitel V Drittlandstransfer. Prüfraster: Angemessenheitsbeschluss SCC BCR Schrems-II-Folgen Transfer Impact Assessment zusaetzliche Massnahmen... |
| `drittlandtransfer-behoerdenpaket-output` | Behördenfähiges Dokumentations- und Antwortpaket für Drittlandtransfers erstellen: Deckvermerk, Transferregister, DPF/SCC/TIA-Nachweise, TOMs, Subprozessoren, Maßnahmenplan und Antwort an deutsche Datenschutzaufsicht. |
| `dsb-bestellungspflicht-pruefung` | Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung. Output: Bestellungsprüfm... |
| `dsfa-erstellung` | Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchführen wenn hohes Risiko für Betroffene vorliegt. Art. 35 36 DSGVO DSFA § 67 BDSG. Prüfraster: Risikobewertung Verarbeitungsbeschreibung Notwendigkeit Verhältnismäßigkeit Massnahmen... |
| `dsgvo-auskunft` | Auskunftsersuchen nach Art. 15 DSGVO prüfen und beantworten wenn Betroffener Auskunft verlangt. Art. 15 12 DSGVO Betroffenenrechte. Prüfraster: Identitätsnachweis Vollständigkeitsprüfung Auskunftsinhalt Fristen Einschraenkungsgründe. Out... |
| `dsgvo-auskunft-antwort` | DSGVO-Auskunftsantwort an Betroffenen vollständig und rechtskonform gestalten. Art. 15 12 Abs. 3 DSGVO Antwortpflicht. Prüfraster: Antwortinhalt Format Fristen Klarheit Weglassungsgründe Begleitschreiben. Output: vollständiges Auskunftss... |
| `joint-controller-vereinbarung` | Joint-Controller-Vereinbarung nach Art. 26 DSGVO erstellen wenn zwei oder mehr Verantwortliche gemeinsam entscheiden. Art. 26 DSGVO Gemeinsame Verantwortlichkeit. Prüfraster: gemeinsame Zwecke und Mittel Aufgabenverteilung Anlaufstelle B... |
| `ki-verordnung-compliance` | KI-Systeme auf Anforderungen der KI-VO und Datenschutz prüfen. KI-VO Risikoklassen Art. 5 9 DSGVO Einwilligung. Prüfraster: Risikoklasse Verbote Hochrisiko-KI Dokumentationspflichten DSGVO-Schnittmengen Transparenzpflichten. Output: KI-C... |
| `mandantendaten-ki` | Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei prüfen. Art. 5 6 DSGVO BRAO § 43a Verschwiegenheit. Prüfraster: Rechtsgrundlage Zweckbindung Vertraulichkeit Anwaltsprivileg AVV KI-Anbieter. Outp... |
| `regulierungs-luecken-analyse` | Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen. Art. 5 6 24 DSGVO BDSG. Prüfraster: Bestandsaufnahme bestehender Massnahmen Soll-Ist-Abgleich Lueckenbewertung Prioritaeten. Output: Lueckenanalys... |
| `richtlinien-monitor` | Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Aenderungsbedarf neue Verarbeitungstätigkeiten gesetzliche Neuerungen Umset... |
| `standardvertragsklauseln-scc-paket` | Standardvertragsklauseln fuer Drittlandtransfers nach Art. 46 DSGVO vorbereiten: SCC-Modulwahl 1-4, Annex I-III, Subprozessoren, TOMs, AVV-Schnittstelle, TIA-Andockung, Signatur- und Behördenpaket ohne Veränderung der offiziellen Klauseln. |
| `us-transfer-tia-dokumentation` | US-Drittlandtransfer nach Art. 44 ff. DSGVO dokumentieren: EU-US Data Privacy Framework, DPF-Listing, Schrems I/II-Historie, SCC/BCR-Ausweichpfad, Transfer Impact Assessment, supplementary measures, Behördennachweis und Review-Kalender. |
| `verarbeitungsverzeichnis-vvt-generator` | Verzeichnis der Verarbeitungstätigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren. Art. 30 DSGVO VVT-Pflicht. Prüfraster: Pflichtangaben Art. 30 Abs. 1 Verantwortlicher Zweck Kategorien Empfaenger Fristen Massnahmen. Output: volls... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
