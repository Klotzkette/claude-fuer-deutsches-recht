# Plugin: Gewerblicher Rechtsschutz

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`gewerblicher-rechtsschutz`) | [`gewerblicher-rechtsschutz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gewerblicher-rechtsschutz.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Patentstreit Vellbruck Medizintechnik ./. TitanOrtho / Bochstaedt — Hüftimplantat Titan EP 3 218 922 B1** (`patent-verletzung-implantat-titan-vellbruck-stuttgart`) | [Gesamt-PDF lesen](../testakten/patent-verletzung-implantat-titan-vellbruck-stuttgart/gesamt-pdf/patent-verletzung-implantat-titan-vellbruck-stuttgart_gesamt.pdf) | [`testakte-patent-verletzung-implantat-titan-vellbruck-stuttgart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patent-verletzung-implantat-titan-vellbruck-stuttgart.zip) |
| **Patentrecht — Erfindungsakten Ravenstein & Moll** (`patentrecht-erfindungsakten-ravenstein-moll`) | [Gesamt-PDF lesen](../testakten/patentrecht-erfindungsakten-ravenstein-moll/gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf) | [`testakte-patentrecht-erfindungsakten-ravenstein-moll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Gewerblicher Rechtsschutz und Urheberrecht für die deutsche und europäische Rechtspraxis: Markenrecht (MarkenG, UMV), Designrecht (DesignG, GGV), Patentrecht (PatG, GebrMG, EPÜ), Urheberrecht (UrhG), Wettbewerbsrecht (UWG), Geschäftsgeheimnisschutz (GeschGehG) sowie Open-Source-Compliance. Das Plugin erstellt und triagiert Abmahnungen, führt Marken- und FTO-Recherchen durch, überprüft IP-Klauseln in Verträgen, verwaltet Schutzrechtsfristen und prüft Open-Source-Lizenzen auf Pflichten und Kompatibilität. Grundlage ist ein Kanzleiprofil, das beim Erststart durch ein Interview befüllt wird – das Plugin lernt Ihre Durchsetzungsstrategie, Ihr Portfolio und Ihre Genehmigungsmatrix, nicht eine generische Vorlage.

**Jedes Ergebnis ist ein Entwurf zur anwaltlichen Prüfung – zitiert, gekennzeichnet und gesperrt – keine Rechtsauskunft.** Das Plugin übernimmt die Arbeit: Dokumente lesen, Prüfschema anwenden, Probleme identifizieren, Memo entworten. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet. Privilegierungsvermerke werden konservativ gesetzt, damit keine Mandatsgeheimnisverletzung riskiert wird. Folgenreiche Handlungen – Abmahnungen versenden, Anmeldungen einreichen – sind durch explizite Freigabe gesperrt.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Gewerblicher Rechtsschutz (`gewerblicher-rechtsschutz`, dieses Plugin) | [gewerblicher-rechtsschutz.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gewerblicher-rechtsschutz.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


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
/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-kaltstart-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-kaltstart-interview` | Ersteinrichtungsinterview ausführen (oder erneut ausführen) |
| `/gewerblicher-rechtsschutz:abmahnung-urheberrecht [Kontext]` | Abmahnung entwerfen oder eingehende Abmahnung triagieren |
| `/gewerblicher-rechtsschutz:takedown-anweisung [Kontext]` | Notice-and-Action (DSA / § 7 DDG) versenden oder auf eine erhaltene Meldung reagieren |
| `/gewerblicher-rechtsschutz:markenrecherche [Marke]` | Erste Markenrecherche – Identitäts-/Verwechslungsanalyse, Anwalt zeichnet ab |
| `/gewerblicher-rechtsschutz:fto-triage [Produkt / Anspruchsbereich]` | Freedom-to-Operate-Triage – Sperrpatente für Anwaltsprüfung aufzeigen |
| `/gewerblicher-rechtsschutz:erfindungsmeldung-aufnahme [Offenbarung]` | Erstprüfung Erfindungsmeldung (ArbnErfG) – Neuheit, erfinderische Tätigkeit, Schutzumfang |
| `/gewerblicher-rechtsschutz:verletzungs-triage [Kontext]` | Verletzungstriage – Ignorieren / informelles Schreiben / Abmahnung / Klage |
| `/gewerblicher-rechtsschutz:ip-klausel-pruefung [Datei]` | IP-Klauseln in Verträgen prüfen – Abtretung, Lizenz, IP-Freistellung, OSS-Reps, ArbnErfG |
| `/gewerblicher-rechtsschutz:open-source-pruefung [Repository / Dateiliste]` | Open-Source-Lizenz-Compliance-Prüfung – Copyleft-Pflichten, Attribution, Kompatibilität |
| `/gewerblicher-rechtsschutz:schutzrechts-portfolio` | Schutzrechtsregister und Fristenverwaltung – fällige Verlängerungen, eingereichte Anmeldungen |
| `/gewerblicher-rechtsschutz:markenanmeldung-dpma` | Markenanmeldung beim DPMA Schritt für Schritt |
| `/gewerblicher-rechtsschutz:abmahnung-urheberrecht` | Urheberrechtliche Abmahnung (insb. Filesharing, § 97a UrhG) |
| `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich` | Mandatsarbeitsbereiche verwalten (nur Mehrmandat-Kanzleien) |

## Skills

| Skill | Zweck |
|---|---|
| **kaltstart-interview** | Ersteinrichtungsinterview – schreibt das Kanzleiprofil |
| **abmahnung** (unterlassungsverlangen) | Abmahnung entwerfen oder triagieren; Genehmigungsmatrix durchlaufen |
| **takedown** | Notice-and-Action (DSA / § 7 ff. DDG) versenden oder darauf reagieren |
| **markenrecherche** (clearance) | Identitäts- und Verwechslungsanalyse für eine geplante Marke |
| **fto-triage** | FTO-Triage – Sperrpatente für Anwaltsprüfung markieren |
| **erfindungsmeldung** (erfindungsmeldung-aufnahme) | Erstprüfung einer Erfindungsmeldung nach ArbnErfG |
| **verletzungs-triage** (verletzungs-triage) | Verletzungssituation bewerten: Handlungsoptionen und Empfehlung |
| **ip-klausel-review** | IP-Klauseln in MSA, WV, Lizenzverträgen, Contractor-Vereinbarungen prüfen |
| **open-source-pruefung** | Open-Source-Lizenzen im Repository gegen die OSS-Richtlinie prüfen |
| **portfolio** | Schutzrechtsregister, Verlängerungsfristen, Status-Dashboard |
| **markenanmeldung-dpma** | Markenanmeldung beim DPMA – Schritt für Schritt |
| **abmahnung-urheberrecht** | Urheberrechtliche Abmahnung, insbesondere Filesharing, § 97a UrhG |
| **mandats-arbeitsbereich** (mandat-arbeitsbereich) | Mandatsarbeitsbereiche für Mehrmandat-Kanzleien anlegen, listen, wechseln und schließen |

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
- **amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang** – Rechtsprechungsdatenbanken

## Schnellstart

### 1. Interview durchführen

```
/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-kaltstart-interview
```

Zehn bis fünfzehn Minuten. Halten Sie Ihr Schutzrechtsverzeichnis, Markenrichtlinien (falls vorhanden), eine Abmahnvorlage (falls vorhanden) und Ihre OSS-Richtlinie (falls vorhanden) bereit.

### 2. Markenrecherche

```
/gewerblicher-rechtsschutz:markenrecherche "APEXBLATT"
```

Ergebnis: Identitätstreffer, Verwechslungsfaktorenanalyse, Kennzeichnungen zur Anwaltsprüfung. Kein Freigabe-/Sperrurteil.

### 3. Fällige Fristen anzeigen

```
/gewerblicher-rechtsschutz:schutzrechts-portfolio
```

Ergebnis: Schutzrechte mit Verlängerungs- oder Aufrechterhaltungsfristen in den nächsten 90 Tagen, nach Dringlichkeit gruppiert.

## Dateistruktur

```
gewerblicher-rechtsschutz/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Kanzleiprofil – vom Interview geschrieben, von Ihnen bearbeitet
├── README.md
├── agents/
│   └── schutzrechts-verlaengerungs-monitor.md
├── skills/
│   ├── kaltstart-interview/
│   ├── abmahnung/ (unterlassungsverlangen)
│   ├── takedown-anweisung/
│   ├── markenrecherche/ (markenrecherche)
│   ├── fto-triage/
│   ├── erfindungsmeldung/ (erfindungsmeldung-aufnahme)
│   ├── verletzungs-triage/ (verletzungs-triage)
│   ├── ip-klausel-pruefung/
│   ├── open-source-pruefung/
│   ├── schutzrechts-portfolio/
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

- Jeder Skill liest zuerst das Kanzleiprofil. Findet er Platzhalter, stoppt er und fordert Sie auf, `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-kaltstart-interview` auszuführen. Es gibt keinen generischen Fallback – eine generische IP-Strategie ist schlechter als gar keine.
- Das Versenden einer Abmahnung eröffnet einen Konflikt. Der `/gewerblicher-rechtsschutz:abmahnung-urheberrecht`-Skill sendet nichts selbst; er entwirft, zeigt den Genehmigungsmatrixeintrag an und wartet auf den Genehmiger.
- `/gewerblicher-rechtsschutz:markenrecherche` und `/gewerblicher-rechtsschutz:fto-triage` sind **erste Triage-Schritte**. Das Ergebnis ist ein Recherchepaket für einen Anwalt, kein Freigabegutachten. Der Skill gibt dies bei jedem Durchlauf an.
- `/gewerblicher-rechtsschutz:open-source-pruefung` kennzeichnet Lizenzpflichten und -inkompatibilitäten. Er erteilt keine Genehmigung für eine kommerzielle Nutzungsentscheidung – das entscheiden Engineering und Recht gemeinsam.
- Patentanspruchsformulierung ist bewusst nicht im Umfang. Dieses Plugin arbeitet gut neben einem Patentanwalt; es ersetzt ihn nicht.
- **Berufsrechtlicher Hinweis:** Alle Entwürfe unterfallen dem Mandatsgeheimnis gem. § 43a Abs. 2 BRAO, § 203 StGB. Externe Weitergabe nur nach anwaltlicher Prüfung und Freigabe.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-urheberrecht` | Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrechtsverletzung. § 97a UrhG Abmahnung und Unterlassung. Prüfraster: modifizierte Unterlassungserklärung Deckelung Abmahnk... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbei... |
| `erfindungsmeldung-aufnahme` | Mitarbeiter meldet eine Erfindung oder Unternehmen prüft eingegangene Erfindungsmeldung. ArbnErfG Arbeitnehmererfindungsgesetz. Prüfraster: Neuheit erfinderische Tätigkeit technischer Charakter EPUe Schutzfähigkeit Arbeitnehmererfindung... |
| `fto-triage` | Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und EP-Patente. Ergebnis Recherc... |
| `gewerblicher-rechtsschutz-anpassen` | Kanzlei moechte ihr gewerbliches-Rechtsschutz-Profil nachjustieren ohne das gesamte Ersteinrichtungsinterview zu wiederholen. Profil-Update Gewerblicher Rechtsschutz. Prüfraster: Durchsetzungsstrategie Genehmigungsmatrix Portfolio-Regist... |
| `gewerblicher-rechtsschutz-kaltstart-interview` | Kanzlei oder Unternehmen richtet das gewerbliche-Rechtsschutz-Plugin zum ersten Mal ein und muss Profil und Strategie hinterlegen. Ersteinrichtung Gewerblicher Rechtsschutz. Prüfraster: Kanzleiprofil Schutzrechtsportfolio Durchsetzungsst... |
| `gewerblicher-rechtsschutz-mandat-arbeitsbereich` | Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwaltung IP-Kanzlei. Prüfraster: Anlegen Auflisten Wechseln Schließen oder Trennen des aktiven Mandats Mandantenkontext f... |
| `gewr-einstweilige-verfuegung-eilverfahren-spezial` | Spezialfall einstweilige Verfuegung im UWG / Markenrecht: Dringlichkeitsvermutung § 12 Abs. 2 UWG, Selbstwiderlegung, Schutzschrift. Pruefraster fuer Verfuegungs- und Antragsgegnerseite. |
| `gewr-geschaeftsgeheimnisgesetz-spezial` | Spezialfall Geschaeftsgeheimnisgesetz GeschGehG: angemessene Geheimhaltungsmassnahmen, erlaubter Reverse Engineering, Whistleblower-Ausnahme. Pruefraster Schutzmassnahmen und Klage. |
| `gewr-markenanmeldung-bauleiter` | Bauleiter Markenanmeldung DPMA / EUIPO: Markenformen, Nizza-Klassen, absolute und relative Schutzhindernisse, Recherchekosten. Pruefraster fuer Mandant. |
| `gewr-uwg-abmahnung-checkliste` | Checkliste UWG-Abmahnung §§ 3 ff. UWG: spuerbarkeit, Mitbewerbereigenschaft, Unterlassungserklaerung, Streitwert, Wiederholungsgefahr. Mustertext Abmahnung und Antwort. |
| `gw-einfuehrung-rechtsschutzwege` | Gewerblicher Rechtsschutz einfuehrend: Markenrecht, UWG, Designrecht, Patentrecht, Geschaeftsgeheimnisschutz. Rechtsschutzwege einstweilige Verfuegung, Klage, Verbandsklage, Schiedsklage. Entscheidungstabelle. |
| `gw-einstweilige-verfuegung-spezial` | Spezialfall einstweilige Verfuegung im gewerblichen Rechtsschutz: Dringlichkeitsvermutung in UWG- und Marken-Sachen, Schutzschrift, Widerspruch, Vollziehung binnen 1 Monat § 929 ZPO. Pruefraster und Mustertexte. |
| `ip-klausel-pruefung` | Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP-Klauseln Vertragsrecht. Prüfraster: Übertragung Inhaberschaft Lizenzgewaehrung exklusiv/nicht-exklusiv Gewährleistun... |
| `mandat-triage-gewerblicher-rechtsschutz` | Neues Mandat im gewerblichen Rechtsschutz: Anwalt klaert welches Sachgebiet und welche Skills benoetigt werden. Eingangs-Triage IP-Recht. Prüfraster: Mandantenrolle (Schutzrechtsinhaber Verletzer Lizenznehmer) Sachgebiet (Marke Patent De... |
| `markenanmeldung-dpma` | Mandant moechte eine Marke beim DPMA anmelden oder Widerspruch gegen eine eingetragene Marke einlegen. §§ 32 ff. MarkenG Markenanmeldung. Prüfraster: Nizza-Klassifikation Anmeldegebühren absolute Eintragungshindernisse § 8 MarkenG Widers... |
| `markenrecherche` | Unternehmen oder Mandant plant neue Marke oder Produktname und fragt: Bestehen Kollisionsrisiken mit aelteren Marken? Markenrecherche vor Anmeldung. Prüfraster: Identitäts- und Aehnlichkeitsprüfung DPMAregister EUIPO eSearch+ WIPO Global... |
| `open-source-pruefung` | Unternehmen will Software ausliefern oder als Open Source veroffentlichen und fragt nach Lizenz-Compliance. Open-Source-Lizenz-Compliance. Prüfraster: Manifest SBOM Repository Copyleft-Pflichten Lizenzkompatibilitaet GPL LGPL MIT Apache... |
| `schutzrechts-portfolio` | Unternehmen oder Kanzlei muss IP-Portfolio verwalten und anstehende Fristen im Blick behalten. Schutzrechtsportfolio-Verwaltung. Prüfraster: Eintragungen Verlaengerungen Jahresgebühren Benutzungsnachweise Fristkalender. Output: Fristenka... |
| `schutzschrift-eilverfuegung` | Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befuerchtet einstweilige Verfuegung ohne Anhoerung. § 945a ZPO Schutzschrift ZSER. Prüfraster: Hinterlegung zentrales elektronisches Schutzschriftenregister § 945a ZPO Sachverh... |
| `spezial-abmahnung-compliance-dokumentation-und-akte` | Abmahnung: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-anmeldung-behoerden-gericht-und-registerweg` | Anmeldung: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-compliance-mandantenkommunikation-entscheidungsvorlage` | Compliance: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-dpma-fristen-form-und-zustaendigkeit` | Dpma: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-euipo-dokumentenmatrix-und-lueckenliste` | Euipo: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-freedom-schriftsatz-brief-und-memo-bausteine` | Freedom: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fristen-abschlussprodukt-und-uebergabe` | Fristen: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gewerblicher-erstpruefung-und-mandatsziel` | Gewerblicher: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klausel-beweislast-und-darlegungslast` | Klausel: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-markenrecherche-risikoampel-und-gegenargumente` | Markenrecherche: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-open-formular-portal-und-einreichung` | Open: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-operate-verhandlung-vergleich-und-eskalation` | Operate: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-patentscreening-livequellen-und-rechtsprechungscheck` | Patentscreening: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-reaktion-internationaler-bezug-und-schnittstellen` | Reaktion: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsschutz-tatbestand-beweis-und-belege` | Rechtsschutz: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-review-sonderfall-und-edge-case` | Review: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-schutzrechts-fristennotiz-und-naechster-schritt` | Schutzrechts: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-source-red-team-und-qualitaetskontrolle` | Source: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-urheberrechts-zahlen-schwellen-und-berechnung` | Urheberrechts: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-versand-mehrparteien-konflikt-und-interessen` | Versand: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `streitwert-igr-berechnen` | Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG Muenchen I LG Duesseldorf... |
| `takedown-anweisung` | Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-and-Take-Down §§ 7 ff. TMG/DDG DSA Art. 16. Prüfraster: Meldung an Hostprovider Stoererhaftung DSA Meldeformular Gegen... |
| `unterlassungsverlangen` | Schutzrechtsinhaber will Verletzung abmahnen oder hat selbst Abmahnung erhalten. Abmahnung Unterlassung MarkenG PatG UrhG UWG. Prüfraster: Abmahnungsentwurf modifizierte Unterlassungserklärung Streitwert Kostenansatz RVG oder Reaktions-O... |
| `verletzungs-triage` | Mandant sieht IP-Verletzung oder hat Verletzungsschreiben erhalten und fragt: Was ist zu tun? Verletzungs-Triage gewerblicher Rechtsschutz. Prüfraster: Marke § 14 MarkenG Patent § 9 PatG Urheber § 97 UrhG Wettbewerb § 8 UWG Entscheidungs... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin gewerblicher-rechtsschutz: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin gewerblicher-rechtsschutz: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin gewerblicher-rechtsschutz: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin gewerblicher-rechtsschutz: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin gewerblicher-rechtsschutz: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin gewerblicher-rechtsschutz: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin gewerblicher-rechtsschutz: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin gewerblicher-rechtsschutz: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin gewerblicher-rechtsschutz: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin gewerblicher-rechtsschutz: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
