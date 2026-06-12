# Kanzlei-Mandant Lifecycle

<!-- BEGIN plugin-sofort-download-section (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kanzlei-mandant-lifecycle`) | [`kanzlei-mandant-lifecycle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-mandant-lifecycle.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Falkenried & Partner mbB — Managementakte Q2/2026** (`kanzlei-management-falkenried-partnerkreis-q2-2026`) | [Gesamt-PDF lesen](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) |
| **Mandatsbeziehung Nordstern BioTherapeutics — Kanzlei Falkenried** (`mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech`) | [Gesamt-PDF lesen](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/gesamt-pdf/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech_gesamt.pdf) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Plugin für die ganze Lebensbeziehung zwischen Kanzlei, Einzelanwalt, Mandant und Rechtsabteilung: Mandatsannahme, Scope, Outside Counsel Guidelines, Budget, Forecast, Statusbericht, Gerichtsakte, Rechnung, Erwartungsmanagement, Enttäuschung, Eskalation, Quickwins und Abschluss.

Es denkt nicht nur juristisch, sondern auch organisatorisch und kaufmännisch: Wer braucht welche Entscheidung, was kostet es, was ist schon erledigt, was blockiert, was darf aus Geheimhaltungs-, Datenschutz- oder Berufsrechtsgründen überhaupt in ein gemeinsames System?

## Kaltstart

1. Rolle klären: Kanzlei, Rechtsabteilung, GC, CFO, Fachabteilung, Einzelanwalt oder externer Dienstleister.
2. Matter klären: Beratung, Prozess, Behörde, Transaktion, Krise, Untersuchung oder Dauerberatung.
3. Dashboard wählen: Status, Budget, Rechnung, Litigation, Board, Risiko, Legal Hold oder Beziehungspuls.
4. Geheimhaltung prüfen: Mandatsgeheimnis, Datenschutz, Dienstleister, KI-System, Zugriff und Export.
5. Nächsten Arbeitsschritt erzeugen: Mail, Memo, Board Paper, Rechnungskommentar, Fristenliste, Entscheidungslog oder Eskalationsnotiz.

## Leitidee

Das Plugin soll beide Seiten stärker machen. Die Kanzlei liefert verständlicher, schneller und berechenbarer. Der Mandant versteht Kosten, Risiko und Fortschritt. Die Rechtsabteilung bekommt ein Cockpit, ohne das Mandatsgeheimnis zu zerlegen. Niemand soll mit schönen Dashboards betäubt werden; jedes Dashboard muss eine echte Entscheidung erleichtern.

## Typische Outputs

- Matter Dashboard mit Ampeln für Frist, Budget, Chancen, Blocker und nächste Entscheidung.
- Invoice Review mit Narrative-Check, OCG-Abgleich und Kürzungsvorschlag.
- Weekly Status Report und Board One-Pager.
- Litigation Roadmap mit Kosten- und Vergleichsfenster.
- Relationship Pulse nach schwierigen Phasen.
- Closeout mit Lessons Learned und Template-Update.

## Quellenhygiene

Vor rechtlich tragenden Aussagen immer live prüfen: BRAO, BORA, RVG, DSGVO, § 203 StGB, Verfahrensrecht und die konkrete Vergütungsvereinbarung. Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 115 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `access-control-roles` | Access Control Roles: steuert Rollen, Berechtigungen, Need-to-know, externe Dienstleister und Austritt aus dem Matter zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege un... |
| `action-item-owner-matrix` | Action-Item Owner Matrix: steuert Wer schuldet was bis wann: Kanzlei, Inhouse, Fachabteilung, Gericht, Gegner, Gutachter zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `appeal-decision-gate` | Rechtsmittel Decision Gate: steuert Berufung/Revision/Beschwerde: Frist, Kosten, Chancen, Business-Ziel und Gremienfreigabe zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfl... |
| `associate-workbench` | Associate Workbench: steuert Associate bekommt klare Aufgaben, Kontext, Deadline, Qualitätsmaßstab und Feedback zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quel... |
| `audit-response-trail-logs-authority-matrix` | Audit Response Legal: steuert Wirtschaftsprüferanfragen, Rechtsstreitbestätigungen und Privilege-sichere Antworten steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfle... |
| `audit-trail-and-logs` | Audit Trail und Logs: steuert wer hat wann was gesehen, geändert, freigegeben oder exportiert zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene im Kanz... |
| `authority-matrix` | Authority Matrix: steuert wer darf Mandat, Budget, Vergleich, Rechtsmittel, Presse und Strategie freigeben zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhy... |
| `bad-news-memo` | Bad News Memo: steuert Kanzlei muss schlechte Nachricht liefern, ohne Vertrauen zu zerstören oder Haftung zu verschleiern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfleg... |
| `beauty-contest-scoring` | Beauty Contest Scoring: steuert Kanzleien nach Erfahrung, Team, Budget, Chemistry, Konflikten und Umsetzungskraft bewerten zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfle... |
| `billing-to-blockbilling-detector-board` | Billing to XRechnung: steuert Kanzleirechnung in E-Rechnung/XRechnung, Kostenstellen und Prüfüberführen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygie... |
| `blockbilling-detector` | Blockbilling Detector: steuert zu grobe Stundenblöcke, doppelte Arbeit, Reisezeit und interne Abstimmungen prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Qu... |
| `board-reporting` | Board Reporting: steuert Vorstand/Aufsichtsrat-Gremium bekommt knappe, belastbare Lage: Risiko, Kosten, Entscheidung, nächste Frist zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezie... |
| `budget-baseline-und-phasen` | Budget Baseline und Phasenplan: steuert Budget nach Phasen, Annahmen, Exclusions, Triggern und Reforecast-Regeln aufsetzen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfle... |
| `budget-overrun-escalation` | Budget Overrun Escalation: steuert Budgetüberschreitung erklären, genehmigen, nachsteuern oder stoppen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygien... |
| `client-business-owner-data-retention-facing` | Business Owner Education: steuert Fachbereich lernt, wann Legal einzubinden ist und welche Unterlagen nötig sind zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Que... |
| `client-data-retention` | Client Data Retention: steuert Aufbewahrung, Löschung, Archiv, Legal Hold und Datenrückgabe nach Mandatsende zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellen... |
| `client-facing-language` | Client Facing Language: steuert Juristische Arbeit in klare Business-Sprache übersetzen, ohne Genauigkeit zu verlieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege u... |
| `client-satisfaction-pulse` | Client Satisfaction Pulse: steuert kurzer Beziehungspuls: Vertrauen, Tempo, Verständlichkeit, Kosten, Strategieklarheit zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `commercial-litigation-budget` | Commercial Litigation Budget: steuert Klage, Beweisaufnahme, Vergleich, Berufung und Vollstreckung budgetieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quell... |
| `communication-charter-conflict-after-court` | Communication Charter: steuert Ton, Kanäle, Frequenz, Kürze, Eskalation und Dokumentationspflichten festlegen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quelle... |
| `conflict-after-mandate` | Konflikt nach Mandat: steuert spätere Gegnermandate, Wissensschutz, Sozietätswechsel und Ethical Walls zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygien... |
| `court-deadline-dashboard` | Court Deadline Dashboard: steuert gerichtliche Fristen, Vorfristen, Zustellungen und Mandantenfreigaben gemeinsam sehen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `court-file-progress` | Gerichtsakten-Fortschritt: steuert Gerichtsakte, beA-Eingänge, Fristen, Schriftsätze, Anlagen und Mandantenfreigaben synchronisieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezi... |
| `crisis-mode` | Crisis Mode: steuert Durchsuchung, Presse, Vorstand, Kunden, Behörden und Kanzlei in Stundenlogik koordinieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quell... |
| `crossborder-counsel-dashboard-matter-data` | Cross-Border Counsel Sync: steuert ausländische Kanzleien, Privilege, Budget, Zeitzonen und konsolidierte Strategie verbinden zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungsp... |
| `dashboard-design-qualitygate` | Dashboard Design Qualitygate: steuert Dashboard so prüfen, dass es führt statt blendet: keine falsche Präzision, klare Owner, echte Risiken zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeite... |
| `dashboard-matter-status` | Matter Status Dashboard: steuert Ampel zu Fortschritt, Budget, Frist, Erfolgsaussicht, Blockern und Entscheiderfragen erzeugen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungs... |
| `data-room-for-board` | Datenraum für Board/Gremien: steuert Gremienunterlagen, Rechte, Versionen, Beschlüsse und Kanzleiinput sicher teilen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und... |
| `datenschutz-avv-legalops` | Datenschutz bei Legal-Ops-Tools: steuert Matter-Management, eBilling, KI-Tool, DMS und gemeinsame Dashboards datenschutz- und berufsrechtsfest machen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwor... |
| `decision-log` | Decision Log: steuert Mandantenentscheidungen, Optionen, Warnungen, Freigaben und Nichtentscheidungen beweisbar dokumentieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungsp... |
| `delegation-supervision-deliverable-acceptance` | Delegation und Supervision: steuert Wer darf was tun, wie wird reviewed, wann muss Partnerin selbst ran zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygie... |
| `deliverable-acceptance` | Deliverable Acceptance: steuert Gutachten, Schriftsatz, Redline, Vermerk oder Board Paper abnehmen, versionieren und freigeben zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungs... |
| `document-room-governance` | Datenraum Governance: steuert Zugriffsrechte, Index, Redactions, Watermark, Versionen und Downloadlogik für Mandat und Verfahren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehun... |
| `enforcement-monitor` | Enforcement Monitor: steuert Vollstreckung, Sicherheiten, Vergleichsbruch und Kosten im Dashboard führen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygi... |
| `engagement-letter-scope` | Engagement Letter und Scope: steuert Mandatsvereinbarung, Scope, Out-of-Scope, Teams, Kommunikationskanäle und Abnahme zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege u... |
| `erfolgsmessung-kpi-escalation-ladder-evidence` | Erfolgsmessung KPI: steuert KPIs jenseits Sieg/Niederlage: Tempo, Budgettreue, Prävention, Business Impact zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhy... |
| `escalation-ladder` | Escalation Ladder: steuert wer wann wen anruft: Associate, Partner, GC, CFO, Vorstand, Fachabteilung zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene... |
| `evidence-gap-dashboard` | Evidence Gap Dashboard: steuert fehlende Beweise, Owner, Quelle, Frist und Risiko in einer Lückenmatrix steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quel... |
| `evidence-request-pack` | Evidence Request Pack: steuert Belege vom Mandanten so anfordern, dass sie wirklich kommen und verwendbar sind zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quell... |
| `executive-summary-generator` | Executive Summary Generator: steuert eine Seite für GC/Vorstand: Lage, Risiko, Entscheidung, Kosten, Timing zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenh... |
| `expectation-management-expert-fachabteilung` | Erwartungsmanagement: steuert Enttäuschungen, schlechte Nachrichten, unsichere Rechtslage und Entscheidungsdruck konstruktiv steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezi... |
| `expert-management` | Expert Management: steuert Sachverständige, Privatgutachten, Gutachterbudget, Briefing und Unabhängigkeit steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Qu... |
| `fachabteilung-briefing` | Fachabteilung Briefing: steuert Business-Leute so briefen, dass Kanzlei keine unbrauchbaren oder gefährlichen Fakten bekommt zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspf... |
| `fee-model-selector` | Fee Model Selector: steuert Stundensatz, Festpreis, Cap, Blended Rate, Success-Komponente und Retainer vergleichen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Q... |
| `festpreis-change-request` | Festpreis und Change Request: steuert Festpreisprojekt steuern, Scope Creep erkennen und Change Request sauber auslösen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `gc-dashboard-handover-kanzleiwechsel-inhouse` | General Counsel Dashboard: steuert GC sieht Matter-Portfolio, Budget, Risiko, Fristen, Board-Entscheidungen und Kanzleileistung zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehung... |
| `handover-kanzleiwechsel` | Handover Kanzleiwechsel: steuert Kanzleiwechsel, Aktenherausgabe, offene Fristen, Datenraum und Rechnungsabschluss zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Q... |
| `inhouse-counsel-ethics` | Inhouse Counsel Ethics: steuert Rechtsabteilung zwischen Vorstandsdruck, Fachbereich, Compliance und externer Kanzlei zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege un... |
| `inhouse-legal-triage` | Inhouse Legal Triage: steuert Rechtsabteilung priorisiert Anfragen, externe Kanzleien, Risiko und Budget zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygi... |
| `injunction-sprint` | Einstweiliger-Rechtsschutz Sprint: steuert 48-Stunden-Mandat mit Fakten, Eidesstattlichen Versicherungen, Anlagen und Budget steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezi... |
| `insurance-notice-investigation-governance` | Insurance Notice: steuert D&O, Rechtsschutz, Cyber, Produkthaftpflicht und Deckungsmeldung im Mandat koordinieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Qu... |
| `investigation-governance` | Investigation Governance: steuert interne Untersuchung, Upjohn-Warnung, Interviewplan, Dokumentensicherung und Reporting zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `invoice-review-narratives` | Invoice Review Narratives: steuert Stundenbeschreibungen auf Verständlichkeit, Doppelerfassung, Blockbilling und OCG-Konformität prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, B... |
| `joint-ai-workspace` | Gemeinsamer KI-Workspace: steuert Kanzlei und Mandant arbeiten in einem KI-System mit getrennten Rollen, Logs und Freigaben zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfl... |
| `kaltstart-beide-seiten-dashboard` | Kaltstart für beide Seiten: steuert gemeinsamer Einstieg für Kanzlei, Einzelanwalt, Rechtsabteilung und Fachabteilung mit Rollen, Zielbild, Budget und Vertraulichkeitsgrenzen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, B... |
| `kanzlei-ki-tool-mandanteneinwilligung` | KI-Tool und Mandanteneinwilligung: steuert KI-Einsatz im Mandat offenlegen, absichern, begrenzen und dokumentieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Q... |
| `law-firm-feedback-loop` | Law Firm Feedback Loop: steuert Mandant gibt Feedback ohne Gesichtsverlust; Kanzlei verbessert sich messbar zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenh... |
| `law-firm-internal-language` | Kanzlei-interne Sprache: steuert interne Tasknotizen, Reviewkommentare und Risikoformulierungen mandatsfest halten zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Q... |
| `legal-engineer-dashboard` | Legal Engineer Dashboard: steuert Automatisierung, Datenextraktion, KI-Nutzung, Datenschutz und Outputprüfung im Mandat zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `legal-hold-dashboard` | Legal Hold Dashboard: steuert Legal Holds mit Custodians, Datenquellen, Bestätigung und Review-Fenstern führen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quell... |
| `legal-knowledge-capture-law-firm-engineer` | Knowledge Capture: steuert Mandatswissen in Playbooks, Muster, Risikoentscheidungen und Lessons Learned überführen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Q... |
| `legal-ops-roadmap` | Legal Ops Roadmap: steuert von E-Mail-Chaos zu Matter-Management, eBilling, Dashboards und Wissensspeicher zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhy... |
| `legal-spend-lessons-to-litigation-hold` | Legal Spend und Accruals: steuert Rückstellungen, Forecasts, Monatsabschluss, Abgrenzung und Überraschungsrechnungen vermeiden zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungs... |
| `lessons-to-playbook` | Lessons to Playbook: steuert aus Mandatsschmerz ein besseres Playbook für nächste Fälle bauen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene im Kanz... |
| `litigation-hold-client` | Litigation Hold beim Mandanten: steuert E-Mails, Chats, Dateien, Teams/Slack, Backups und Löschroutinen sichern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quel... |
| `litigation-roadmap-client` | Litigation Roadmap für Mandanten: steuert Gerichtsverfahren in Phasen, Schriftsatzkalender, Beweis, Vergleich und Kosten erklären zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehu... |
| `mandant-self-service` | Mandant Self Service: steuert Mandant lädt Dokumente, prüft Status, beantwortet Fragen und sieht nächste Entscheidungen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `mandatsannahme-conflict-gwg` | Mandatsannahme, Conflict und GwG: steuert Konfliktprüfung, wirtschaftlich Berechtigte, Sanktions-/PEP-Hinweise, Scope und Ablehnungsszenarien zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkei... |
| `mandatsbeziehung-qualitygate` | Mandatsbeziehung Qualitygate: steuert letzter Check vor Versand an Mandant oder Kanzlei: Ton, Recht, Budget, Aktion zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und... |
| `matter-closeout` | Matter Closeout: steuert Abschlussbericht, Lessons Learned, offene Rechnungen, Aktenrückgabe und Know-how sichern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Qu... |
| `matter-intake-form-builder` | Matter Intake Form Builder: steuert ein Intake-Formular bauen, das genug fragt und nicht nervt zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene im Kan... |
| `matter-mandantenschulung-mandatsannahme` | Mandantenschulung: steuert Kanzlei schult Fachabteilung oder Legal Team; Inhalte, Grenzen, Dokumentation und Follow-up zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege u... |
| `matter-taxonomy` | Matter Taxonomy: steuert Mandate so klassifizieren, dass Reports, Budgets und Wissensmanagement funktionieren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quelle... |
| `meeting-cadence-monthly-business-multi-client` | Meeting Cadence: steuert Jour fixe, Steering Committee, Ad-hoc Calls, Minuten und Action Items sinnvoll takten zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quell... |
| `monthly-business-review` | Monthly Business Review: steuert Monatsreview Kanzlei/Rechtsabteilung: Kosten, Matters, Learnings, Forecast und Beziehung zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfleg... |
| `multi-client-matter` | Mehrere Mandanten in einer Sache: steuert Joint Defense, gleichlaufende Interessen, Kostenteilung, Konfliktumschlag und Information zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezie... |
| `narrative-value-writing` | Narrative Value Writing: steuert Tätigkeitsbeschreibungen so schreiben, dass der Mandant Wert und Zweck erkennt zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quel... |
| `outside-counsel-guidelines` | Outside Counsel Guidelines: steuert OCG des Unternehmens in alltagstaugliche Kanzlei-Pflichten, Eskalationen und Abrechnungsregeln übersetzen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkei... |
| `panel-management-partner-dashboard-post` | Panel Management: steuert Kanzleipanel steuern, Leistungsprofile, Konflikte, Preise, Diversity, Kapazität und Qualität zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege u... |
| `partner-dashboard` | Partner Dashboard: steuert Mandatsverantwortliche Partnerin sieht Budget, Team, Qualität, Mandantenzufriedenheit und Haftungsrisiken zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezi... |
| `post-mortem-retrospective` | Post-Mortem Retrospective: steuert Nach großem Mandat: Was lief gut, was teuer, was nervte, was wird nächstes Mal anders zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege... |
| `press-and-litigation-comms` | Press and Litigation Comms: steuert Litigation-PR, Ad-hoc-Fragen, Social Media und Mandatsstrategie abstimmen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quelle... |
| `privilege-und-vertraulichkeit` | Privilege und Vertraulichkeit: steuert Mandatsgeheimnis, Legal Privilege, interne Weiterleitung, Dienstleister und gemeinsame Plattform zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, B... |
| `pro-bono-procurement-legal-quickwin` | Pro Bono und Low Bono: steuert reduzierte Vergütung, Mindestgebühren, Mandatsumfang, Erwartungsmanagement und Haftung zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege un... |
| `procurement-legal-interface` | Procurement Legal Interface: steuert Einkauf will Kanzleikosten drücken; Legal will Qualität, Privilege und Geschwindigkeit sichern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezie... |
| `quickwin-identifikation` | Quickwin-Identifikation: steuert kleine schnelle Erfolge finden: Frist retten, Gegner beruhigen, Datenraum ordnen, Rechnung klären zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezieh... |
| `rate-card-review` | Rate Card Review: steuert Stundensätze, Seniorität, Staffing, Blended Rate und jährliche Anpassung prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhyg... |
| `rechnung-streit-deeskalation` | Rechnungsstreit deeskalieren: steuert Kürzung, Missverständnis, Value Story, Kulanz, Nachlass und künftiger Prozess zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und... |
| `red-team-mandatsbeziehung` | Red Team Mandatsbeziehung: steuert Ergebnis, Dashboard, Rechnung und Beziehung auf Missverständnisse, Halluzinationen und Risiken prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten,... |
| `redaction-confidentiality-regulatory-matter` | Redaction und Confidentiality: steuert Schwärzungen, Anlagen, Betriebsgeheimnisse und Gerichts-/Gegnerfassung sauber steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspf... |
| `regulatory-matter-command` | Regulatory Matter Command: steuert Behördenverfahren mit Kanzlei und Inhouse steuern: Auskunft, Akteneinsicht, Frist, Ton zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfleg... |
| `regulatory-remediation-plan` | Regulatory Remediation Plan: steuert nach Auflage/Bußgeld/Prüfung Maßnahmenplan, Owner, Nachweis und Kanzleirolle steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfleg... |
| `relationship-redflags` | Relationship Red Flags: steuert Warnzeichen: Funkstille, Überraschungsrechnung, Scope-Unklarheit, Strategiedrift, Fristdruck zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspf... |
| `relationship-renewal` | Relationship Renewal: steuert nach Krise oder Erfolg: neue OCG, bessere Reports, neue Teams, neue Preise zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygi... |
| `reserve-litigation-rfp-kanzleiauswahl-risk` | Reserve Litigation Risk: steuert Rückstellung und Prozessrisiko so formulieren, dass Legal und Finance beide damit arbeiten können zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Bezieh... |
| `rfp-kanzleiauswahl` | RFP Kanzleiauswahl: steuert Pitch/RFP für Kanzlei erstellen, Antworten vergleichen und nicht nur Stundensatz bewerten zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege un... |
| `risk-register` | Risk Register: steuert rechtliche, wirtschaftliche, prozessuale und Beziehungssrisiken in einem Register führen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quel... |
| `scope-creep-fruehwarnung` | Scope Creep Frühwarnung: steuert Mandat wächst stillschweigend; Zusatzarbeit, Budget und Verantwortung rechtzeitig klären zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfleg... |
| `second-opinion-management` | Second Opinion Management: steuert zweite Kanzlei einbinden, ohne Vertrauen, Privilege und Strategie zu beschädigen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und... |
| `service-level-settlement-authority` | Service Level Agreement: steuert Antwortzeiten, Eskalationswege, Freigaben, Wochenberichte und Notfallkontakte vereinbaren zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfle... |
| `settlement-authority` | Settlement Authority: steuert Vergleichsvollmacht, wirtschaftliche Untergrenzen, Eskalationsleiter und Gremienfreigabe zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege u... |
| `settlement-implementation` | Settlement Implementation: steuert Vergleich umgesetzt bekommen: Zahlung, Verpflichtungen, Kommunikation, Monitoring und Closeout zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehu... |
| `staffing-pyramide` | Staffing Pyramide: steuert Partner, Counsel, Associate, Legal Engineer und Paralegal sinnvoll einsetzen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygie... |
| `stakeholder-map` | Stakeholder Map: steuert GC, Legal Ops, CFO, Fachbereich, Vorstand, Kanzleipartner und Gericht/Behörde abbilden zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quel... |
| `subsidiary-parent-success-fee-probability` | Konzernmandat Mutter/Tochter: steuert wer ist Mandant: Mutter, Tochter, Vorstand, Projektgesellschaft oder Gruppe zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Qu... |
| `success-fee-compliance` | Success Fee Compliance: steuert Erfolgsvergütung, Bonus, Premium, Discount und gesetzliche Grenzen prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhyg... |
| `success-probability-alignment` | Erfolgsaussichten Alignment: steuert Kanzlei- und Mandantensicht auf Chancen, Risiken, Bauchgefühl und Business-Ziel abgleichen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehung... |
| `template-library-governance` | Template Library Governance: steuert Mustertexte, Klauseln, Schriftsatzbausteine, Freigaben und Aktualitätscheck verwalten zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspfle... |
| `termination-of-mandate` | Mandatsbeendigung: steuert Kündigung des Mandats, Fristen, Herausgabe, offene Rechnungen und Anschlussvertretung zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Que... |
| `third-party-time-entry-translation-management` | Third Party Funding: steuert Prozessfinanzierer einbinden, Interessenkonflikt, Vergleichshoheit und Reporting zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quelle... |
| `time-entry-hygiene` | Time Entry Hygiene: steuert Zeiterfassung präzise, verständlich, abrechenbar und nicht peinlich machen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygien... |
| `translation-management` | Translation Management: steuert Übersetzungen, beglaubigte Fassungen, bilinguale Schriftsätze und Kosten steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Que... |
| `vat-reverse-charge-legalfees` | Umsatzsteuer bei Legal Fees: steuert grenzüberschreitende Kanzleirechnungen, Reverse Charge, Auslagen und Kostenstellen prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungs... |
| `vergleichswert-story` | Vergleichswert Story: steuert Warum ein Vergleich wirtschaftlich sinnvoll oder falsch ist; Kosten, Zeit, Risiko und Beziehung zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungsp... |
| `weekly-status-report` | Weekly Status Report: steuert Wochenbericht mit Done/Doing/Blocked, Fristen, Budget, Risiken und Entscheidungen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quel... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`kanzlei-mandant-lifecycle.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/kanzlei-mandant-lifecycle.md) (35 KB)
- Im Repo: [`testakten/megaprompts/kanzlei-mandant-lifecycle.md`](../testakten/megaprompts/kanzlei-mandant-lifecycle.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->
