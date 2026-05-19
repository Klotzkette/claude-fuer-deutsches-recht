# Plugin: Gewerblicher Rechtsschutz

Gewerblicher Rechtsschutz und Urheberrecht für die deutsche und europäische Rechtspraxis: Markenrecht (MarkenG, UMV), Designrecht (DesignG, GGV), Patentrecht (PatG, GebrMG, EPÜ), Urheberrecht (UrhG), Wettbewerbsrecht (UWG), Geschäftsgeheimnisschutz (GeschGehG) sowie Open-Source-Compliance. Das Plugin erstellt und triagiert Abmahnungen, führt Marken- und FTO-Recherchen durch, überprüft IP-Klauseln in Verträgen, verwaltet Schutzrechtsfristen und prüft Open-Source-Lizenzen auf Pflichten und Kompatibilität. Grundlage ist ein Kanzleiprofil, das beim Erststart durch ein Interview befüllt wird – das Plugin lernt Ihre Durchsetzungsstrategie, Ihr Portfolio und Ihre Genehmigungsmatrix, nicht eine generische Vorlage.

**Jedes Ergebnis ist ein Entwurf zur anwaltlichen Prüfung – zitiert, gekennzeichnet und gesperrt – keine Rechtsauskunft.** Das Plugin übernimmt die Arbeit: Dokumente lesen, Prüfschema anwenden, Probleme identifizieren, Memo entworten. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet. Privilegierungsvermerke werden konservativ gesetzt, damit keine Mandatsgeheimnisverletzung riskiert wird. Folgenreiche Handlungen – Abmahnungen versenden, Anmeldungen einreichen – sind durch explizite Freigabe gesperrt.

## Für wen dieses Plugin

| Rolle | Hauptanwendungen |
|---|---|
| **IP-Anwalt / Fachanwalt für gewerblichen Rechtsschutz** | Durchsetzungsentscheidungen, Klauselprüfung, Portfolioübersicht, FTO-Triage |
| **IP-Paralegal / Sachbearbeiter** | Portfolio- und Fristenverwaltung, erste Markenrecherche, Mandatsaufnahme |
| **Markenschutzbeauftragter** | Abmahnungen, Notice-and-Action-Meldungen, Überwachungsdienst-Nachverfolgung |
| **Patentanwalt** | FTO-Triage, Erfindungsmeldung, Klauselprüfung, Portfolioverwaltung – *keine Anspruchsformulierung* |
| **Kanzlei-IP-Assistent** | Mandatsarbeitsbereiche je Mandant, Markenrecherche, Klauselprüfung |
| **Legal Ops / IP-Portfoliomanagement** | Schutzrechtsregister, Verlängerungsfristen, OSS-Compliance-Prüfungen |

Dieses Plugin **formuliert keine Patentansprüche**. Patentprosekution mit Anspruchsstrategie erfordert einen zugelassenen Patentanwalt und sollte nicht an ein allgemeines Werkzeug delegiert werden. Patentarbeit beschränkt sich hier auf FTO-Triage (Ist dieses Produkt durch ein fremdes Patent gesperrt?), Klauselprüfung in Verträgen, Portfolioverlängerungsverwaltung und Verletzungstriage.

## Erststart: das Ersteinrichtungsinterview

Beim ersten Aufruf führt das Plugin ein Interview durch – zehn bis fünfzehn Minuten, gesprächsorientiert – um zu erfahren, wie Ihre Kanzlei tatsächlich arbeitet. Es fragt nach Ihrem Rechtsgebiets-Mix, Ihrer Jurisdiktion, Ihrer Durchsetzungsstrategie, Ihrer Genehmigungsmatrix und Ihren Eskalationsauslösern. Dann bittet es um Ihr Schutzrechtsverzeichnis, Markenrichtlinien, Abmahnvorlagen, Durchsetzungs-Vorgehensleitfaden und OSS-Richtlinie.

Das Ergebnis wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/gewerblicher-rechtsschutz/CLAUDE.md` gespeichert – ein Klartext-Dokument über Ihre Kanzlei, das jeder andere Skill vor dem Start liest.

```
/gewerblicher-rechtsschutz:cold-start-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/gewerblicher-rechtsschutz:cold-start-interview` | Ersteinrichtungsinterview ausführen (oder erneut ausführen) |
| `/gewerblicher-rechtsschutz:abmahnung [Kontext]` | Abmahnung entwerfen oder eingehende Abmahnung triagieren |
| `/gewerblicher-rechtsschutz:takedown [Kontext]` | Notice-and-Action (DSA / § 7 DDG) versenden oder auf eine erhaltene Meldung reagieren |
| `/gewerblicher-rechtsschutz:markenrecherche [Marke]` | Erste Markenrecherche – Identitäts-/Verwechslungsanalyse, Anwalt zeichnet ab |
| `/gewerblicher-rechtsschutz:fto-triage [Produkt / Anspruchsbereich]` | Freedom-to-Operate-Triage – Sperrpatente für Anwaltsprüfung aufzeigen |
| `/gewerblicher-rechtsschutz:erfindungsmeldung [Offenbarung]` | Erstprüfung Erfindungsmeldung (ArbnErfG) – Neuheit, erfinderische Tätigkeit, Schutzumfang |
| `/gewerblicher-rechtsschutz:verletzungs-triage [Kontext]` | Verletzungstriage – Ignorieren / informelles Schreiben / Abmahnung / Klage |
| `/gewerblicher-rechtsschutz:ip-klausel-review [Datei]` | IP-Klauseln in Verträgen prüfen – Abtretung, Lizenz, IP-Freistellung, OSS-Reps, ArbnErfG |
| `/gewerblicher-rechtsschutz:oss-review [Repository / Dateiliste]` | Open-Source-Lizenz-Compliance-Prüfung – Copyleft-Pflichten, Attribution, Kompatibilität |
| `/gewerblicher-rechtsschutz:portfolio` | Schutzrechtsregister und Fristenverwaltung – fällige Verlängerungen, eingereichte Anmeldungen |
| `/gewerblicher-rechtsschutz:markenanmeldung-dpma` | Markenanmeldung beim DPMA Schritt für Schritt |
| `/gewerblicher-rechtsschutz:abmahnung-urheberrecht` | Urheberrechtliche Abmahnung (insb. Filesharing, § 97a UrhG) |
| `/gewerblicher-rechtsschutz:mandats-arbeitsbereich` | Mandatsarbeitsbereiche verwalten (nur Mehrmandat-Kanzleien) |

## Skills

| Skill | Zweck |
|---|---|
| **cold-start-interview** | Ersteinrichtungsinterview – schreibt das Kanzleiprofil |
| **abmahnung** (cease-desist) | Abmahnung entwerfen oder triagieren; Genehmigungsmatrix durchlaufen |
| **takedown** | Notice-and-Action (DSA / § 7 ff. DDG) versenden oder darauf reagieren |
| **markenrecherche** (clearance) | Identitäts- und Verwechslungsanalyse für eine geplante Marke |
| **fto-triage** | FTO-Triage – Sperrpatente für Anwaltsprüfung markieren |
| **erfindungsmeldung** (invention-intake) | Erstprüfung einer Erfindungsmeldung nach ArbnErfG |
| **verletzungs-triage** (infringement-triage) | Verletzungssituation bewerten: Handlungsoptionen und Empfehlung |
| **ip-klausel-review** | IP-Klauseln in MSA, WV, Lizenzverträgen, Contractor-Vereinbarungen prüfen |
| **oss-review** | Open-Source-Lizenzen im Repository gegen die OSS-Richtlinie prüfen |
| **portfolio** | Schutzrechtsregister, Verlängerungsfristen, Status-Dashboard |
| **markenanmeldung-dpma** | Markenanmeldung beim DPMA – Schritt für Schritt |
| **abmahnung-urheberrecht** | Urheberrechtliche Abmahnung, insbesondere Filesharing, § 97a UrhG |
| **mandats-arbeitsbereich** (matter-workspace) | Mandatsarbeitsbereiche für Mehrmandat-Kanzleien anlegen, listen, wechseln und schließen |

## Interaktive Befehle und geplante Agenten

Die obigen Befehle werden bei Aufruf ausgeführt. Der nachstehende Agent läuft planmäßig:

| Agent | Was er überwacht | Standard-Takt |
|---|---|---|
| **ip-verlängerungs-watcher** | Schutzrechtsregister – berechnet fällige Verlängerungen, Aufrechterhaltungsgebühren in den nächsten 90 Tagen | Wöchentlich |

## Rechtsgrundlagen und anwendbares Recht

Dieses Plugin ist auf das **deutsche und europäische IP-Recht** ausgerichtet:

| Rechtsgebiet | Normen |
|---|---|
| Markenrecht | MarkenG; VO (EU) 2017/1001 (UMV/EUTMR); Madrider Abkommen/MMP |
| Designrecht | DesignG; VO (EG) Nr. 6/2002 (GGV); Haager Abkommen |
| Patentrecht | PatG; GebrMG; VO (EU) 2019/933 (SPC); EPÜ; PCT |
| Urheberrecht | UrhG; RL 2019/790/EU (DSM-RL); RL 2001/29/EG (InfoSoc) |
| Wettbewerbsrecht | UWG; RL 2005/29/EG (UGP-RL); RL 2006/114/EG |
| Geschäftsgeheimnisse | GeschGehG; RL 2016/943/EU |
| Plattformrecht / Takedown | DDG (§§ 7 ff.); VO (EU) 2022/2065 (DSA) |
| Arbeitnehmererfindungen | ArbnErfG; Vergütungsrichtlinien BMBF |

## Konnektoren und Zitatverifizierung

**Verknüpfen Sie zuerst ein Recherchetool – die Zitatprüfung hängt davon ab.** Ohne Verbindung wird jedes Zitat mit `[prüfen]` markiert und der Prüfvermerk über dem Dokument vermerkt dies. Das Plugin funktioniert in beiden Fällen; mit Recherchetool übernimmt es jedoch mehr der Verifizierung für Sie.

Empfohlene Datenbanken für deutsches IP-Recht:
- **DPMAregister** – Marken, Designs, Gebrauchsmuster (DE)
- **EUIPO eSearch+** – Unionsmarken, eingetragene Gemeinschaftsdesigns
- **WIPO Global Brand DB** – Internationale Marken (Madrid)
- **Espacenet / DPMApaplus** – Patente, Gebrauchsmuster
- **GRUR / WRP / MMR / NJW** – juristische Zeitschriften
- **Beck-Online / juris** – Rechtsprechungsdatenbanken

## Schnellstart

### 1. Interview durchführen

```
/gewerblicher-rechtsschutz:cold-start-interview
```

Zehn bis fünfzehn Minuten. Halten Sie Ihr Schutzrechtsverzeichnis, Markenrichtlinien (falls vorhanden), eine Abmahnvorlage (falls vorhanden) und Ihre OSS-Richtlinie (falls vorhanden) bereit.

### 2. Markenrecherche

```
/gewerblicher-rechtsschutz:markenrecherche "APEXBLATT"
```

Ergebnis: Identitätstreffer, Verwechslungsfaktorenanalyse, Kennzeichnungen zur Anwaltsprüfung. Kein Freigabe-/Sperrurteil.

### 3. Fällige Fristen anzeigen

```
/gewerblicher-rechtsschutz:portfolio
```

Ergebnis: Schutzrechte mit Verlängerungs- oder Aufrechterhaltungsfristen in den nächsten 90 Tagen, nach Dringlichkeit gruppiert.

## Dateistruktur

```
gewerblicher-rechtsschutz/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Kanzleiprofil – vom Interview geschrieben, von Ihnen bearbeitet
├── README.md
├── agenten/
│   └── ip-verlängerungs-watcher.md
├── skills/
│   ├── cold-start-interview/
│   ├── abmahnung/ (cease-desist)
│   ├── takedown/
│   ├── clearance/ (markenrecherche)
│   ├── fto-triage/
│   ├── erfindungsmeldung/ (invention-intake)
│   ├── infringement-triage/ (verletzungs-triage)
│   ├── ip-clause-review/
│   ├── oss-review/
│   ├── portfolio/
│   ├── markenanmeldung-dpma/
│   ├── abmahnung-urheberrecht/
│   └── mandats-arbeitsbereich/
└── ausloeser/ausloeser.json
```

## Konfiguration

Das Plugin liest kanzleispezifische Konfiguration aus:

```
~/.claude/plugins/config/claude-fuer-deutsches-recht/gewerblicher-rechtsschutz/CLAUDE.md
```

Dieser Pfad überlebt Plugin-Updates. Die mitgelieferte `CLAUDE.md` ist eine Vorlage – sie wird bei jedem Update ersetzt. Das Ersteinrichtungsinterview schreibt Ihre befüllte Version in den obigen Konfigurationspfad; ab dann bearbeiten Sie diese Datei direkt, wenn sich etwas ändert.

## Hinweise

- Jeder Skill liest zuerst das Kanzleiprofil. Findet er Platzhalter, stoppt er und fordert Sie auf, `/gewerblicher-rechtsschutz:cold-start-interview` auszuführen. Es gibt keinen generischen Fallback – eine generische IP-Strategie ist schlechter als gar keine.
- Das Versenden einer Abmahnung eröffnet einen Konflikt. Der `/gewerblicher-rechtsschutz:abmahnung`-Skill sendet nichts selbst; er entwirft, zeigt den Genehmigungsmatrixeintrag an und wartet auf den Genehmiger.
- `/gewerblicher-rechtsschutz:markenrecherche` und `/gewerblicher-rechtsschutz:fto-triage` sind **erste Triage-Schritte**. Das Ergebnis ist ein Recherchepaket für einen Anwalt, kein Freigabegutachten. Der Skill gibt dies bei jedem Durchlauf an.
- `/gewerblicher-rechtsschutz:oss-review` kennzeichnet Lizenzpflichten und -inkompatibilitäten. Er erteilt keine Genehmigung für eine kommerzielle Nutzungsentscheidung – das entscheiden Engineering und Recht gemeinsam.
- Patentanspruchsformulierung ist bewusst nicht im Umfang. Dieses Plugin arbeitet gut neben einem Patentanwalt; es ersetzt ihn nicht.
- **Berufsrechtlicher Hinweis:** Alle Entwürfe unterfallen dem Mandatsgeheimnis gem. § 43a Abs. 2 BRAO, § 203 StGB. Externe Weitergabe nur nach anwaltlicher Prüfung und Freigabe.
