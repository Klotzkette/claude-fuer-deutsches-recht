# Vertragsrecht-Plugin

Workflows für innerbetriebliche Rechtsabteilungen und Kanzleien im deutschen Vertragsrecht: Lieferanten- und Dienstleisterverträge, NDA-/Geheimhaltungsvereinbarungen, SaaS-/MSA-Prüfungen, Vertragsfristen-Tracking, Eskalationssteuerung und mandantengerechte Zusammenfassungen. Das Plugin erlernt das **eigene Playbook** der Rechtsabteilung durch ein einmaliges Ersteinrichtungs-Interview – keine Standardlösung von der Stange.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, gekennzeichnet und abgestuft – keine abschließende Rechtsberatung.** Das Plugin liest die Dokumente, wendet das Playbook an, identifiziert Abweichungen und erstellt das Prüfvermerk. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Quellen werden nach Herkunft gekennzeichnet, damit der Prüfer weiß, welche Zitate aus einem Recherche-Tool stammen und welche zu prüfen sind. Vertraulichkeitshinweise werden konservativ gesetzt, damit keine unbeabsichtigte Preisgabe erfolgt. Folgenreiche Handlungen – Einreichung, Versand, Unterzeichnung – stehen unter ausdrücklichem Bestätigungsvorbehalt.

## Für wen ist dieses Plugin

| Rolle | Primäre Workflows |
|---|---|
| **Unternehmensjurist / Legal Counsel** | Lieferantenverträge, Eskalationssteuerung, Stakeholder-Zusammenfassungen |
| **Vertragsmanager / Paralegals** | NDA-Triage, Fristen-Tracking, Erstprüfung |
| **Einkauf / Beschaffung** | Vertragsfristen, Stakeholder-Zusammenfassungen als Empfänger |
| **Vertrieb / BD** | NDA-Triage eigenverantwortlich vor Einbindung der Rechtsabteilung |

## Erste Nutzung: das Ersteinrichtungs-Interview

Bei der ersten Nutzung führt das Plugin ein ca. zehnminütiges Gespräch, um zu erfahren, wie die Rechtsabteilung tatsächlich arbeitet. Es fragt nach Playbook-Positionen, Eskalationsregeln und den typischen Problemen im Tagesgeschäft. Anschließend werden 5–10 bereits unterzeichnete Verträge erbeten (mehr ist besser; 20 Verträge ergeben ein klareres Muster), um die eigenen Positionen in der Praxis zu erkennen.

Das Erlernte wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` gespeichert – ein Klartextdokument über die Rechtsabteilung, das jede Funktion liest, bevor sie tätig wird. Das Dokument wird direkt bearbeitet, keine Konfigurationsdatei.

```
/vertragsrecht:ersteinrichtung
```

**Seite des Mandanten.** Früh in der Einrichtung wird gefragt, ob ein **Verkäufer-Playbook** (das Unternehmen verkauft Produkte/Dienstleistungen; eigenes Muster), ein **Käufer-Playbook** (das Unternehmen kauft bei Lieferanten; deren Muster) oder beides aufgebaut werden soll. Die Antwort kehrt nahezu jede Playbook-Position um – Haftungsgrenzen, Freistellungsrichtung, Kündigungsrechte, IP-Zuordnung – daher ist sie von grundlegender Bedeutung.

## Befehle

| Befehl | Funktion |
|---|---|
| `/vertragsrecht:ersteinrichtung` | Ersteinrichtungs-Interview durchführen oder wiederholen |
| `/vertragsrecht:pruefen [Datei]` | Vertrag gegen das Playbook prüfen |
| `/vertragsrecht:verlängerungstracker` | Welche Verträge laufen in 90 Tagen aus und bis wann muss die Kündigung eingehen? |
| `/vertragsrecht:eskalation` | Eskalationspfad ermitteln und Vorlage formulieren |
| `/vertragsrecht:nachtragsverwaltung [Datei(en)]` | Vertragsänderungen über Basisvertrag und alle Nachträge nachverfolgen |
| `/vertragsrecht:klausel-vorschlaege` | Ausstehende Playbook-Aktualisierungen aus dem Monitor-Agenten durcharbeiten |
| `/vertragsrecht:akte` | Akten verwalten (nur Kanzleinutzung mit mehreren Mandanten) |

## Skills

| Skill | Zweck |
|---|---|
| **ersteinrichtung** | Interview, das `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` schreibt |
| **lieferantenvertrag-pruefung** | Vollständige Playbook-Abweichungsanalyse mit Klausel-Redlines (§§ 631, 611 BGB; LkSG) |
| **nda-pruefung** | Schnelle GRÜN/GELB/ROT-Triage (§§ 17 ff. GeschGehG, § 241 II BGB) |
| **saas-msa-pruefung** | SaaS-/MSA-spezifische Prüfung: AGB, Datenschutz Art. 28 DSGVO, Haftung, Preiseskalation |
| **verlängerungstracker** | Register der Kündigungsfristen; zeigt Fristen gemäß § 309 Nr. 9 BGB |
| **eskalation** | Eskalationsmatrix aus dem Playbook, Vorlage für Genehmigungsanfrage |
| **stakeholder-zusammenfassung** | Zweisprachige Nicht-Juristen-Fassung eines Rechtsgutachtens |
| **nachtragsverwaltung** | Änderungen über Basisvertrag und Nachträge zusammenfassen oder Klausel zurückverfolgen |
| **akte** | Akten anlegen, auflisten, wechseln und schließen für Mehrfachmandatsverhältnisse |

## Befehle vs. terminierte Agenten

Die obigen Befehle werden auf Abruf ausgeführt – für die aktive Bearbeitung eines Vorgangs. Die Agenten laufen planmäßig im Hintergrund.

| Agent | Beobachtet | Standard-Takt |
|---|---|---|
| **verlängerungs-wächter** | Fristen-Register: meldet, was in 90 Tagen fällig wird; Rot-Flag bei 0–13 Tagen | Wöchentlich (montags) |
| **abschluss-debrief** | Kürzlich unterzeichnete Verträge auf Playbook-Abweichungen; Erinnerung zur Erfassung von Kontext | Wöchentlich (montags) |
| **playbook-monitor** | Abweichungsprotokoll: schlägt Playbook-Aktualisierungen vor, wenn eine Klausel in 12 Monaten ≥ 5-mal abgewichen wurde | Datengesteuert (nach jedem Abschluss-Debrief) |

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
/vertragsrecht:ersteinrichtung
```

Dauer: ca. 10 Minuten. 5–10 unterzeichnete Verträge bereithalten (mehr ist besser, 20 ergibt ein klareres Muster).

Die Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` gespeichert und bleibt bei Plugin-Updates erhalten.

### 2. Vertrag prüfen

```
/vertragsrecht:pruefen lieferanten-msa.pdf
```

Ausgabe: Abweichungsprotokoll gegen das Playbook mit konkreten Redline-Formulierungen und namentlich genanntem Genehmiger.

### 3. Ablaufende Verträge abrufen

```
/vertragsrecht:verlängerungstracker
```

Ausgabe: alles mit Kündigungsfrist in den nächsten 90 Tagen, nach Dringlichkeit geordnet.

## Wie das Plugin lernt

Das Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich mit der Nutzung. Skills melden, wenn eine Ausgabe auf einem Standard basiert, der angepasst werden sollte. Der `playbook-monitor`-Agent schlägt Aktualisierungen vor, wenn die Praxis vom Playbook abweicht. Das Interview kann wiederholt werden, die Datei kann direkt bearbeitet werden, oder ein Skill kann eine neue Position erfassen.

## Verzeichnisstruktur

```
vertragsrecht/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Praxisprofil der Rechtsabteilung
├── README.md
├── agents/
│   ├── verlängerungs-wächter.md
│   ├── abschluss-debrief.md
│   └── playbook-monitor.md
├── skills/
│   ├── cold-start-interview/    # → ersteinrichtung
│   ├── review/                  # → prüfen
│   ├── review-proposals/        # → klausel-vorschläge
│   ├── vendor-agreement-review/ # → lieferantenvertrag-prüfung
│   ├── nda-review/              # → nda-prüfung
│   ├── saas-msa-review/         # → saas-msa-prüfung
│   ├── renewal-tracker/         # → verlängerungstracker
│   │   └── references/renewal-register.yaml
│   ├── escalation-flagger/      # → eskalation
│   ├── amendment-history/       # → nachtragsverwaltung
│   ├── matter-workspace/        # → akte
│   ├── stakeholder-summary/     # → stakeholder-zusammenfassung
│   ├── abmahnung-uwg/           # NEU
│   ├── agb-pruefung/            # NEU
│   └── widerruf-fernabsatz/     # NEU
└── hooks/hooks.json
```

## Hinweise

- Das Plugin geht standardmäßig davon aus, dass das Unternehmen **Kunde/Käufer** bei den meisten Prüfungen ist. Beim Auftreten als Verkäufer/Auftragnehmer ist dies zu markieren, damit das Playbook umgekehrt angewendet wird.
- Die NDA-Triage ist für die eigenverantwortliche Nutzung durch Nicht-Juristen konzipiert. GRÜN bedeutet „zur Unterschrift weiterleiten". Sie verhandelt nicht.
- Das Fristen-Tracking erfasst nur Verträge, die über dieses Plugin geprüft oder aus dem CLM einmalig importiert wurden. Vor der Installation unterzeichnete Verträge erfordern einen einmaligen Erstimport.
- **Berufsrechtlicher Hinweis:** Jede Ausgabe ist ein Arbeitsentwurf. Die anwaltliche Verschwiegenheitspflicht (§ 43a Abs. 2 BRAO, § 203 StGB) ist bei jeder Weitergabe zu beachten.
