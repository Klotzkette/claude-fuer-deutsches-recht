# Patentrecht — Erfindungsakten Ravenstein & Moll


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Diese Arbeitsakte gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 1096 KB) | PDF | [`gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf`](gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-patentrecht-erfindungsakten-ravenstein-moll.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-patentrecht-erfindungsakten-ravenstein-moll-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Diese Akte bündelt sechs patentrechtliche Mandatslagen aus einer Patentanwalts- und Rechtsanwaltskanzlei. Sie ist bewusst unordentlich: Erfinder erzählen technisch zu knapp, Anspruchsentwürfe sind noch roh, Abmahnfristen laufen, Lizenzverträge widersprechen sich, Recherchen enthalten Treffer mit unterschiedlicher Relevanz und Bestandsverfahren müssen strategisch gegen Verletzungsrisiken gespiegelt werden.

**Passende Plugins:** `patentrecht`, `patentrecherche`, `gewerblicher-rechtsschutz`, `fachanwalt-gewerblicher-rechtsschutz`; für saubere Mandantenbriefe zusätzlich das Word-Schreibplugin.

## Arbeitsszenarien

| Akte | Kernproblem | Erwarteter Skillpfad |
| --- | --- | --- |
| A Hühnerstall-Dämmerungstorheber | Erfindung ist anschaulich, aber Anspruchsentwurf und Offenbarungsrisiko sind ungeklärt. | `erfindungsmeldung-aufnahme-und-rueckfragen` → `patentanmeldung-anspruchsentwurf` → `stand-der-technik-recherche-workflow` |
| B Laserdüse Flow-Edge | Abmahnung mit enger Frist, unvollständiger Claim Chart und möglichem Vorbenutzungsrecht. | `abmahnung-patentverletzung-verteidigung` → `patentverletzung-claim-chart` → `vorbenutzungsrecht-paragraph-12-patg` |
| C selbstnivellierender Getränkehalter | Crowdfunding-Launch vor Recherche; mehrere nahe Treffer in unterschiedlichen Datenbanken. | `stand-der-technik-recherche-workflow` → `neuheit-und-erfinderische-taetigkeit` → `patentrecherche/agentische-datenbank-recherche` |
| D Patentlizenz VitaPhotonics | Vertragsentwurf enthält widersprüchliche Lizenz-, Territory-, Inhaberschafts- und Improvement-Regeln. | `patentlizenzvertrag-review` → `patentlizenzvertrag-de-en-drafting` → `erfinderbenennung-und-arbeitnehmererfindung` |
| E DE/EN-Term-Sheet Aerotech | Deutsches und englisches Lizenzmuster muss aus Term Sheet-Informationen konsistent gefüllt werden. | `patentlizenzvertrag-de-en-drafting` → `patentlizenzvertrag-review` |
| F Frosthaus-Fassadenelement | EPA-Einspruchsfrist und alternative deutsche Nichtigkeitsroute; technische Prior-Art-Auswertung erforderlich. | `einspruch-epa-und-nichtigkeit-bpatg` → `neuheit-und-erfinderische-taetigkeit` → `rechtsstand-register-und-fristen` |

## Dateien

| Pfad | Inhalt |
| --- | --- |
| `pdfs/originale/` | Eingereichte Original-PDFs zu den sechs Akten und interne Auswertungsmaterialien |
| `01-aktenuebersicht-und-soforttriage.md` | Kanzleiinterner Überblick, Fristen, Risiken, Skillrouting |
| `02-akte-a-erfindungsaufnahme-huehnerstall.md` | Erfindungsaufnahme, Merkmale, Offenbarungsrisiken, Rückfragen |
| `03-akte-a-anspruchsentwurf-v0-3.md` | Arbeitsentwurf Anspruch 1 und Unteransprüche |
| `04-akte-b-abmahnung-laserduese-claim-chart.md` | Claim Chart Verteidigung und Abmahnreaktion |
| `05-akte-c-rechercheplan-getraenkehalter.md` | Recherchestrategie, Suchstrings, Prior-Art-Bewertung |
| `06-akte-d-lizenzvertrag-reviewmatrix.md` | Reviewmatrix Patentlizenz VitaPhotonics/Luminos |
| `07-akte-e-termsheet-variablenmapping-de-en.md` | Variablenmapping und Klauselcheck DE/EN |
| `08-akte-f-einspruch-nichtigkeit-fristen.md` | Einspruchs-/Nichtigkeitsstrategie Frosthaus |
| `emails/` | echte EML-Dateien mit Mandantenkommunikation und Fristdruck |
| `tabellen/` | CSV-Arbeitstabellen für Fristen, Prior Art, Lizenzfehler und Term-Sheet-Variablen |
| `docx/` | Arbeitsentwürfe für Anspruch und Mandantenkommunikation |
| `xlsx/` | Claim-Chart- und Variablenmapping-Arbeitsmappen |

## Nutzung

1. Zuerst mit `patentrecht/allgemein` oder `patentrecht-kaltstart-interview` die Akte einordnen.
2. Für Akte A bis F jeweils den passenden Spezialskill starten.
3. Bei Recherchefragen an `patentrecherche` übergeben und Treffer dokumentieren.
4. Am Ende immer `patentrecht-redteam-qualitygate` verwenden: Fristen, Registerstand, Anspruchsfassung, Quellen und offene technische Tatsachen prüfen.
