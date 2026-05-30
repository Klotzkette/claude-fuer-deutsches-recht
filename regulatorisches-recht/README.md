# Regulatorisches Recht – Plugin für deutsches Aufsichtsrecht



<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`regulatorisches-recht`) | [`regulatorisches-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/regulatorisches-recht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte: BaFin-Sonderprüfung Thalvenia Bank AG — Kryptoverwahrung, AML-Pflichtverletzungen, MiCAR-Lizenzkrise** (`bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart`) | [Gesamt-PDF lesen](../testakten/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart/gesamt-pdf/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart_gesamt.pdf) | [`testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **BaFin-Sonderprüfung Thalvenia Bank AG — Kryptoverwahrung, AML-Pflichtverletzungen, MiCAR-Lizenzkrise** (`bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart`) | [Gesamt-PDF lesen](../testakten/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart/gesamt-pdf/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Überwacht Aufsichts-Feeds, vergleicht neue Regulierungsakte gegen Ihre Richtlinienbibliothek und identifiziert Lücken. Lernt Ihre Materialitätsschwelle, damit keine Meldung bei jeder Pressemitteilung erfolgt. Ausgelegt für BaFin-Newsroom, Bundesgesetzblatt, EUR-Lex und direkte Behörden-Feeds.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, markiert und freigabepflichtig – keine Rechtsauskunft.** Das Plugin übernimmt die Arbeit: liest Dokumente, wendet Ihr Regelwerk an, findet Lücken, erstellt Vermerke. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Zitate werden nach Quelle gekennzeichnet. Privilegierungsvermerke werden konservativ gesetzt, damit kein unbeabsichtigter Verzicht entsteht. Folgenreiche Handlungen – Einreichungen, Versendungen, Ausführungen – erfordern ausdrückliche Bestätigung.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Regulatorisches Recht (`regulatorisches-recht`, dieses Plugin) | [regulatorisches-recht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/regulatorisches-recht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Für wen dieses Plugin gedacht ist

| Rolle | Primäre Abläufe |
|---|---|
| **Compliance-/Aufsichtsrechtler** | Beobachtungsliste, Gap-Triage, Richtlinienaktualisierung |
| **Datenschutz-/Produktjurist** | Gefilterte Alerts für das eigene Gebiet |
| **GC / Chefjustitiar** | Eskalationsempfänger bei wesentlichen Lücken mit Fristen |

## Erster Start: Kaltstart

Fragt ab, welche Behörden Sie beobachten, verbindet Ihren Richtlinienordner und erlernt, was "wesentlich" bedeutet. Erstellt eine Beobachtungsliste und indiziert Ihre Richtlinienbibliothek.

```
/regulatorisches-recht:regulatorisches-recht-kaltstart-interview
```

## Skills

| Skill | Funktion |
|---|---|
| `/regulatorisches-recht:regulatorisches-recht-kaltstart-interview` | Ersteinrichtung: Beobachtungsliste + Richtlinienindex + Materialitätsschwelle |
| `/regulatorisches-recht:aufsichts-feed-monitor` | Feeds jetzt prüfen, Neues melden |
| `/regulatorisches-recht:richtlinien-vergleich [Norm]` | Diff einer konkreten Rechtsänderung gegen die Richtlinienbibliothek |
| `/regulatorisches-recht:luecken` | Offener Gap-Tracker – was wurde gemeldet und noch nicht geschlossen? |
| `/regulatorisches-recht:stellungnahmen` | Offene Konsultationszeiträume prüfen, Entscheidungen protokollieren, Fristen verfolgen |
| `/regulatorisches-recht:richtlinien-neufassung` | Vorgeschlagene Richtlinienneufassung, die eine Lücke schließt – Erstentwurf zur internen Prüfung, kein direktes Bearbeiten von Quelldokumenten |
| `/regulatorisches-recht:regulatorisches-recht-mandat-arbeitsbereich` | Mandats-Workspaces verwalten (nur Multi-Mandantenpraxis) – neu, auflisten, wechseln, schließen, keiner |
| **luecken-aufzeiger** *(Referenz)* | Gemeinsames Gap- und Kommentar-Tracker-Framework, das von `/luecken` und `/stellungnahmen` geladen wird |

## Interaktive Skills vs. geplante Agenten

Die obigen Skills werden bei Aufruf ausgeführt – für die aktive Arbeit an einem Mandat. Die folgenden Agenten laufen planmäßig – für das, was sich bewegt, wenn Sie nicht hinsehen:

| Agent | Was er beobachtet | Standardrhythmus |
|---|---|---|
| **regulierungs-aenderungs-monitor** | Aufsichts-Feeds – filtert nach der bei der Ersteinrichtung erlernten Materialitätsschwelle und erstellt ein Digest aus Signal statt Rauschen | Wöchentlich (täglich bei aktivem regulatorischen Umfeld) |

## Konnektoren und Zitatverifizierung

**Zuerst ein Recherchewerkzeug verbinden – die Zitier-Schutzregeln bauen darauf auf.** Ohne eines wird jedes Zitat mit `[prüfen]` versehen und die Prüfernotiz über jedem Ergebnis hält fest, dass Quellen nicht verifiziert wurden. Das Plugin arbeitet in beiden Fällen; es übernimmt nur mehr der Verifizierung, wenn ein Recherchewerkzeug verbunden ist.

Die Rechtsrecherche-Konnektoren in diesem Plugin sind nicht nur Datenquellen – sie sind der Unterschied zwischen einem verifizierten Zitat und einem, das Sie prüfen müssen. Ein über einen verbundenen Recherche-Konnektor abgerufenes Zitat ist mit seiner Quelle markiert und rückverfolgbar. Zitate aus Modellwissen oder bloßer Web-Suche werden nicht als zitierfähige Fundstelle ausgegeben, bis Norm, Entscheidung, Randnummer oder Seite gegen eine Primärquelle geprüft sind.

## Integrationsmöglichkeiten

Enthält die allgemeinen Konnektoren in `.mcp.json`:

- **Slack** – Nachrichten suchen, Kanäle lesen, Diskussionen finden
- **Google Drive** – Dokumente suchen, lesen und abrufen

BaFin-Newsroom-RSS, Bundesgesetzblatt-Feed und EUR-Lex-Alerts können als direkte Behörden-Feeds eingebunden werden.

## Voraussetzungen

Eigentümer-Benachrichtigungen (Gap-Zuweisungen, Fristenerinnerungen, Konsultationsalerts) erfordern einen Slack-MCP-Server in Ihrer Umgebung. Ohne einen solchen funktionieren Gap-Tracker und Kommentar-Tracker weiterhin – Benachrichtigungen werden jedoch nicht gepostet, und die Skills markieren ungegatedete Einträge stattdessen im Statusbericht.

## Wie das Plugin lernt

Ihr Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` ist nicht statisch – es verbessert sich mit der Nutzung. Skills informieren Sie, wenn eine Ausgabe eine Standardeinstellung verwendet, die Sie anpassen sollten. Der `regulierungs-aenderungs-monitor`-Agent beobachtet die Aufsichts-Feeds und markiert Änderungen gegen Ihre Richtlinienbibliothek. Sie können die Einrichtung erneut ausführen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine neue Position aufzuzeichnen.

## Abgedeckte Normen und Behörden

**Aufsichtsbehörden:** BaFin, Deutsche Bundesbank, BMF, Bundesnetzagentur (BNetzA), BMG, BAFA, BMJ, BMWi/BMWK, EBA, ESMA, EZB/SSM

**Finanzmarktrecht:** KWG, ZAG, WpHG, WpIG, GwG, KAG/KAGB, MaRisk (BaFin-RS 09/2017 i.d.F. 2023), MaBV, BörsG

**Energie- und Telekommunikationsrecht:** EnWG, TKG, MessZV

**Heilmittel-/Gesundheitsrecht:** HeilMWerbG, AMG, MPG/MDR-EU, PatDSG

**Steuerrecht (Verfahren):** UStG, AO, FGO

## Hinweise

- Materialitätsfilterung ist der Mehrwert. Alles ist "technisch eine Regulierungsänderung" – das Plugin lernt, was hier tatsächlich wichtig ist.
- Policy-Diff vergleicht gegen indizierte Richtlinien. Wenn die Richtlinienbibliothek nicht verbunden ist, laufen Diffs gegen eingefügte Inhalte.
- Dies ist die automatisierte Version von `datenschutzrecht/regulierungs-luecken-analyse`. Kombination empfohlen: dieses beobachtet, jenes taucht tiefer ein.

## Konfiguration

Ihre Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` gespeichert und überlebt Plugin-Updates – die Einrichtung wird nur einmal durchgeführt.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Regulatorisches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `aufsichts-feed-monitor` | Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifizieren. KWG WpHG DORA VAG BaFin-Rundschreiben. Prüfraster: Relevanz für Mandant Umsetzungsfrist Handlungsbedarf Meldepflic... |
| `dora-ikt-vertragspruefung` | IKT-Drittanbietervertraege auf DORA-Konformität prüfen wenn Finanzunternehmen digitale Dienstleistungen einkaufen. Art. 28 30 DORA VO (EU) 2022/2554. Prüfraster: Pflichtklauseln Art. 30 DORA Ausstiegsstrategien Aufsichtsrechte Subdienstl... |
| `inkasso-rdg` | Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg Inkassoerlaubnis Zulassung... |
| `luecken` | Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: n... |
| `luecken-aufzeiger` | Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen. GG Art. 12 80 AEUV Art. 107. Prüfraster: Normtext Regelungsziele Luecken unbeabsichtigte Folgen Verbesserungsvorschlaeg... |
| `regulatorisches-recht-anpassen` | Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf. Output: ueberarbeit... |
| `regulatorisches-recht-kaltstart-interview` | Neues regulatorisches Mandat durch strukturiertes Erstgespraech aufnehmen. KWG WpHG DORA VAG GwG. Prüfraster: Branche Regulierungsrahmen Sachverhalt Fristen Pflichten Risiko. Output: Mandatssteckbrief Normenkarte fehlende Informationen.... |
| `regulatorisches-recht-mandat-arbeitsbereich` | Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. A... |
| `richtlinien-neufassung` | Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg. Output: neue Richtli... |
| `richtlinien-vergleich` | Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Aenderungshistorie Bedeutung der Aenderungen. Output: Vergleich... |
| `stellungnahmen` | Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prüfraster: Konsultationsumfang regulatorische Ziele Kritikpunkte Alternativvorschlaege Verhältnismäßigkeit. Output: str... |
| `ustva` | Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse Vorsteuer Fristen Sonder... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
