# Vertragsrecht-Plugin

Arbeitsabläufe für innerbetriebliche Rechtsabteilungen und Kanzleien im deutschen Vertragsrecht: Lieferanten- und Dienstleisterverträge, NDA-/Geheimhaltungsvereinbarungen, SaaS-/MSA-Prüfungen, Vertragsfristen-Tracking, Eskalationssteuerung und mandantengerechte Zusammenfassungen. Das Plugin erlernt den **eigenen Vorgehensleitfaden** der Rechtsabteilung durch ein einmaliges Ersteinrichtungs-Interview – keine Standardlösung von der Stange.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, gekennzeichnet und abgestuft – keine abschließende Rechtsberatung.** Das Plugin liest die Dokumente, wendet den Vorgehensleitfaden an, identifiziert Abweichungen und erstellt das Prüfvermerk. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Quellen werden nach Herkunft gekennzeichnet, damit der Prüfer weiß, welche Zitate aus einem Recherche-Tool stammen und welche zu prüfen sind. Vertraulichkeitshinweise werden konservativ gesetzt, damit keine unbeabsichtigte Preisgabe erfolgt. Folgenreiche Handlungen – Einreichung, Versand, Unterzeichnung – stehen unter ausdrücklichem Bestätigungsvorbehalt.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Vertragsrecht (`vertragsrecht`, dieses Plugin) | [vertragsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **LG Regensburg Sieglinger (SV-Gutachten KI-Vorwurf)** | [testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH** ([`testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/`](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/)).

Direkt-Download als ZIP: [testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Für wen ist dieses Plugin

| Rolle | Primäre Arbeitsabläufe |
|---|---|
| **Unternehmensjurist / Legal Counsel** | Lieferantenverträge, Eskalationssteuerung, Stakeholder-Zusammenfassungen |
| **Vertragsmanager / Paralegals** | NDA-Triage, Fristen-Tracking, Erstprüfung |
| **Einkauf / Beschaffung** | Vertragsfristen, Stakeholder-Zusammenfassungen als Empfänger |
| **Vertrieb / BD** | NDA-Triage eigenverantwortlich vor Einbindung der Rechtsabteilung |

## Erste Nutzung: das Ersteinrichtungs-Interview

Bei der ersten Nutzung führt das Plugin ein ca. zehnminütiges Gespräch, um zu erfahren, wie die Rechtsabteilung tatsächlich arbeitet. Es fragt nach den Positionen im Vorgehensleitfaden, Eskalationsregeln und den typischen Problemen im Tagesgeschäft. Anschließend werden 5–10 bereits unterzeichnete Verträge erbeten (mehr ist besser; 20 Verträge ergeben ein klareres Muster), um die eigenen Positionen in der Praxis zu erkennen.

Das Erlernte wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` gespeichert – ein Klartextdokument über die Rechtsabteilung, das jede Funktion liest, bevor sie tätig wird. Das Dokument wird direkt bearbeitet, keine Konfigurationsdatei.

```
/vertragsrecht:vertragsrecht-kaltstart-interview
```

**Seite des Mandanten.** Früh in der Einrichtung wird gefragt, ob ein **Verkäufer-Vorgehensleitfaden** (das Unternehmen verkauft Produkte/Dienstleistungen; eigenes Muster), ein **Käufer-Vorgehensleitfaden** (das Unternehmen kauft bei Lieferanten; deren Muster) oder beides aufgebaut werden soll. Die Antwort kehrt nahezu jede Position im Vorgehensleitfaden um – Haftungsgrenzen, Freistellungsrichtung, Kündigungsrechte, IP-Zuordnung – daher ist sie von grundlegender Bedeutung.

## Befehle

| Befehl | Funktion |
|---|---|
| `/vertragsrecht:vertragsrecht-kaltstart-interview` | Ersteinrichtungs-Interview durchführen oder wiederholen |
| `/vertragsrecht:vertragspruefung [Datei]` | Vertrag gegen den Vorgehensleitfaden prüfen |
| `/vertragsrecht:vertragsverlaengerungs-monitor` | Welche Verträge laufen in 90 Tagen aus und bis wann muss die Kündigung eingehen? |
| `/vertragsrecht:eskalations-marker` | Eskalationspfad ermitteln und Vorlage formulieren |
| `/vertragsrecht:aenderungs-historie [Datei(en)]` | Vertragsänderungen über Basisvertrag und alle Nachträge nachverfolgen |
| `/vertragsrecht:pruefungsvorschlaege` | Ausstehende Aktualisierungen des Vorgehensleitfadens aus dem Monitor-Agenten durcharbeiten |
| `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich` | Akten verwalten (nur Kanzleinutzung mit mehreren Mandanten) |

## Skills

| Skill | Zweck |
|---|---|
| **ersteinrichtung** | Interview, das `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` schreibt |
| **lieferantenvertrag-pruefung** | Vollständige Abweichungsanalyse gegen den Vorgehensleitfaden mit Klausel-Redlines (§§ 631, 611 BGB; LkSG) |
| **nda-pruefung** | Schnelle GRÜN/GELB/ROT-Triage (§§ 17 ff. GeschGehG, § 241 II BGB) |
| **saas-msa-pruefung** | SaaS-/MSA-spezifische Prüfung: AGB, Datenschutz Art. 28 DSGVO, Haftung, Preiseskalation |
| **vertragsverlaengerungs-monitor** | Register der Kündigungsfristen; zeigt Fristen gemäß § 309 Nr. 9 BGB |
| **eskalation** | Eskalationsmatrix aus dem Vorgehensleitfaden, Vorlage für Genehmigungsanfrage |
| **stakeholder-zusammenfassung** | Zweisprachige Nicht-Juristen-Fassung eines Rechtsgutachtens |
| **aenderungs-historie** | Änderungen über Basisvertrag und Nachträge zusammenfassen oder Klausel zurückverfolgen |
| **akte** | Akten anlegen, auflisten, wechseln und schließen für Mehrfachmandatsverhältnisse |

## Befehle vs. terminierte Agenten

Die obigen Befehle werden auf Abruf ausgeführt – für die aktive Bearbeitung eines Vorgangs. Die Agenten laufen planmäßig im Hintergrund.

| Agent | Beobachtet | Standard-Takt |
|---|---|---|
| **verlängerungs-wächter** | Fristen-Register: meldet, was in 90 Tagen fällig wird; Rot-Flag bei 0–13 Tagen | Wöchentlich (montags) |
| **abschluss-debrief** | Kürzlich unterzeichnete Verträge auf Abweichungen vom Vorgehensleitfaden; Erinnerung zur Erfassung von Kontext | Wöchentlich (montags) |
| **vorgehensleitfaden-monitor** | Abweichungsprotokoll: schlägt Aktualisierungen des Vorgehensleitfadens vor, wenn eine Klausel in 12 Monaten ≥ 5-mal abgewichen wurde | Datengesteuert (nach jedem Abschluss-Debrief) |

## Integrationen

**Zuerst ein Recherche-Tool verbinden – die Zitier-Prüfmechanismen hängen davon ab.** Ohne Verbindung wird jede Quellenangabe mit `[prüfen]` gekennzeichnet und der Prüferhinweis über dem Dokument vermerkt, dass Quellen nicht verifiziert wurden.

Integrierte Konnektoren (`.mcp.json`):

- **Ironclad / Agiloft** – Vertragslebenszyklusverwaltung (CLM)
- **DocuSign** – Unterschriftsstatus und Umschlag-Tracking
- **Slack** – Nachrichten durchsuchen, Kanäle lesen, Diskussionen finden
- **Google Drive / SharePoint** – Dokumente suchen, lesen und abrufen

## Schnellstart

### 1. Interview durchführen

```
/vertragsrecht:vertragsrecht-kaltstart-interview
```

Dauer: ca. 10 Minuten. 5–10 unterzeichnete Verträge bereithalten (mehr ist besser, 20 ergibt ein klareres Muster).

Die Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` gespeichert und bleibt bei Plugin-Updates erhalten.

### 2. Vertrag prüfen

```
/vertragsrecht:vertragspruefung lieferanten-msa.pdf
```

Ausgabe: Abweichungsprotokoll gegen den Vorgehensleitfaden mit konkreten Redline-Formulierungen und namentlich genanntem Genehmiger.

### 3. Ablaufende Verträge abrufen

```
/vertragsrecht:vertragsverlaengerungs-monitor
```

Ausgabe: alles mit Kündigungsfrist in den nächsten 90 Tagen, nach Dringlichkeit geordnet.

## Wie das Plugin lernt

Das Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich mit der Nutzung. Skills melden, wenn eine Ausgabe auf einem Standard basiert, der angepasst werden sollte. Der `vorgehensleitfaden-monitor`-Agent schlägt Aktualisierungen vor, wenn die Praxis vom Vorgehensleitfaden abweicht. Das Interview kann wiederholt werden, die Datei kann direkt bearbeitet werden, oder ein Skill kann eine neue Position erfassen.

## Verzeichnisstruktur

```
vertragsrecht/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Praxisprofil der Rechtsabteilung
├── README.md
├── agents/
│   ├── verlaengerungs-monitor.md
│   ├── deal-nachbesprechung.md
│   └── spielbuch-monitor.md
├── skills/
│   ├── kaltstart-interview/    # → ersteinrichtung
│   ├── vertragspruefung/                  # → prüfen
│   ├── pruefungsvorschlaege/        # → klausel-vorschläge
│   ├── lieferantenvertrag-pruefung/
│   ├── nda-pruefung/
│   ├── saas-msa-pruefung/
│   ├── vertragsverlaengerungs-monitor/         # → vertragsverlaengerungs-monitor
│   │   └── references/renewal-register.yaml
│   ├── eskalations-marker/      # → eskalation
│   ├── aenderungs-historie/       # → aenderungs-historie
│   ├── mandats-arbeitsbereich/  # → akte
│   ├── stakeholder-zusammenfassung/     # → stakeholder-zusammenfassung
│   ├── abmahnung-uwg/           # NEU
│   ├── agb-pruefung/            # NEU
│   └── widerruf-fernabsatz/     # NEU
└── ausloeser/ausloeser.json
```

## Hinweise

- Das Plugin geht standardmäßig davon aus, dass das Unternehmen **Kunde/Käufer** bei den meisten Prüfungen ist. Beim Auftreten als Verkäufer/Auftragnehmer ist dies zu markieren, damit der Vorgehensleitfaden umgekehrt angewendet wird.
- Die NDA-Triage ist für die eigenverantwortliche Nutzung durch Nicht-Juristen konzipiert. GRÜN bedeutet "zur Unterschrift weiterleiten". Sie verhandelt nicht.
- Das Fristen-Tracking erfasst nur Verträge, die über dieses Plugin geprüft oder aus dem CLM einmalig importiert wurden. Vor der Installation unterzeichnete Verträge erfordern einen einmaligen Erstimport.
- **Berufsrechtlicher Hinweis:** Jede Ausgabe ist ein Arbeitsentwurf. Die anwaltliche Verschwiegenheitspflicht (§ 43a Abs. 2 BRAO, § 203 StGB) ist bei jeder Weitergabe zu beachten.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 17 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-uwg` | Unterstützt beim Verfassen und Prüfen von UWG-Abmahnungen nach § 13 UWG sowie der dazugehörigen modifizierten Unterlassungserklärung mit Vertragsstrafe und der Schutzschrift. Lädt, wenn ein Mandat eine wettbewerbsrechtliche Abmahnung, ei... |
| `aenderungs-historie` | 'Verfolgt, wie sich ein Vertrag über Basisvertrag und alle Nachträge hinweg verändert hat – entweder als Gesamtüberblick aller Änderungen oder als Klausel-Rückverfolgung für eine bestimmte Bestimmung. Laden, wenn der Nutzer fragt "was ha... |
| `agb-pruefung` | Unterstützt bei der rechtlichen Prüfung von Allgemeinen Geschäftsbedingungen (AGB) auf Einbeziehung, Inhaltskontrolle und Transparenzgebot nach §§ 305–310 BGB. Lädt, wenn ein Mandat die Prüfung, Erstellung oder Verteidigung von AGB im B2... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Vertragsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `eskalations-marker` | 'Ordnet ein Vertragsproblem dem richtigen Genehmiger per Eskalationsmatrix aus dem Praxisprofil zu und erstellt die Genehmigungsanfrage. Laden, wenn der Nutzer fragt "wer muss das genehmigen", "eskalieren", "braucht das GC-Freigabe", "Ge... |
| `lieferantenvertrag-pruefung` | Prüfung eines eingehenden Lieferanten- oder Dienstleistervertrags gegen das Playbook der Rechtsabteilung. Werk-/Dienstvertrag (§§ 631 und 611 BGB), Gewährleistung, Haftungsbegrenzung, LkSG-Anforderungen, CISG-Abwahl. Abweichungen werden... |
| `nda-durchsetzer` | 'Überarbeitet ein NDA der Gegenseite **konservativ im Änderungsmodus**, ohne Struktur, Nummerierung, Reihenfolge oder Look-&-Feel zu verändern, und erstellt parallel eine strukturierte Analyse (Executive Summary, struktureller Vergleich,... |
| `nda-pruefung` | Schnelle Triage von eingehenden NDA-/Geheimhaltungsvereinbarungen in GRÜN / GELB / ROT, damit nur die Vereinbarungen anwaltliche Zeit beanspruchen, die sie wirklich brauchen. Geeignet für Vertrieb und BD zur eigenständigen Erstprüfung. W... |
| `pruefungsvorschlaege` | 'Prüft und genehmigt (oder lehnt ab) ausstehende Playbook-Aktualisierungsvorschläge des Playbook-Monitor-Agenten und überträgt genehmigte Änderungen in das Kanzleiprofil. Lädt, wenn der Monitor Vorschläge gemeldet hat, wenn der Nutzer "P... |
| `saas-msa-pruefung` | Prüfung von SaaS-Abonnement- und Rahmenverträgen (MSA) mit Schwerpunkt auf AGB-Kontrolle (§§ 305–310 BGB), automatischer Verlängerung, Preiseskalation, Datenschutz (Art. 28 DSGVO), Haftungsbegrenzung und Vertragsstrafe (§ 339 BGB). Wird... |
| `stakeholder-zusammenfassung` | 'Übersetzt ein Vertragsprüfungsmemo in eine Zusammenfassung für Geschäftsführung, Vorstand oder Einkauf — kein Rechtsgutachten, sondern eine klare Entscheidungsgrundlage. Lädt, wenn der Nutzer "Zusammenfassung für Geschäftsführung", "für... |
| `vertragspruefung` | 'Prüft einen Vertrag gegen das Kanzlei-Playbook nach deutschem Recht. Identifiziert Vertragsstruktur anhand der Titelseite, ordnet das Dokument dem richtigen Prüfpfad zu (Lieferantenvertrag, NDA, AGB-Klauselkontrolle, Dienstleistungsvert... |
| `vertragsrecht-anpassen` | 'Geführte Anpassung des Kanzleiprofils im Vertragsrecht — ändert einzelne Einstellungen ohne erneutes Erstgespräch. Lädt, wenn der Nutzer "Profil anpassen", "Playbook ändern", "Eskalation aktualisieren", "Klauselposition ändern" oder "ko... |
| `vertragsrecht-kaltstart-interview` | 'Führt das Erstgespräch zur Mandatsaufnahme im Vertragsrecht durch und schreibt das Kanzlei- bzw. Mandatsprofil. Lädt beim ersten Einsatz des Plugins, wenn die Konfigurationsdatei noch Platzhalter enthält oder wenn der Nutzer "Plugin ein... |
| `vertragsrecht-mandat-arbeitsbereich` | Verwaltet Mandatsarbeitsbereiche — neu anlegen, auflisten, wechseln, abschließen oder von Mandatsebene auf Kanzleiebene wechseln. Lädt, wenn ein Anwalt mit mehreren Mandanten ein neues Mandat anlegen, zum aktiven Mandat wechseln, Mandate... |
| `vertragsverlaengerungs-monitor` | 'Zeigt Verträge mit ablaufenden Kündigungsfristen an und warnt rechtzeitig, bevor Verlängerungs-/Kündigungsfenster schließen. Relevant insbesondere bei § 309 Nr. 9 BGB (automatische Verlängerung). Laden, wenn der Nutzer fragt "welche Ver... |
| `widerruf-fernabsatz` | Unterstützt bei Fragen zum Widerrufsrecht im Fernabsatzrecht nach §§ 312g und 355 BGB: Belehrungspflichten, Fristberechnung, Rechtsfolgen des Widerrufs und Ausnahmen. Lädt, wenn ein Mandat Widerrufsbelehrung, Widerrufsdurchsetzung oder R... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
