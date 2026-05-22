# Wandeldarlehen-Lebenszyklus

Vollständiger Workflow-Assistent für den Lebenszyklus eines Wandeldarlehens bei GmbH und UG (haftungsbeschränkt) — von der ersten Mandatsbesprechung über Vertragsgestaltung (bilingual DE/EN oder einsprachig DE), Beurkundungsprüfung, Wandelereignisse und Wandlungsberechnung bis zum Cap-Table-Update, Gesellschafterbeschluss und Handelsregisteranmeldung durch den Notar.

## Direkt-Download

[wandeldarlehen-lebenszyklus.zip herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wandeldarlehen-lebenszyklus.zip)

## Testakte

Die vollständige Beispielakte liegt unter [`testakten/wandeldarlehen-beispielcase/`](../testakten/wandeldarlehen-beispielcase/) und kann direkt auf GitHub durchgesehen werden. Als ZIP zum Download: [testakte-wandeldarlehen-beispielcase.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wandeldarlehen-beispielcase.zip).

### Einzelne Dateien direkt öffnen

Tipp: Bei DOCX/XLSX rendert GitHub keine lesbare Vorschau. Daher liegt zu jeder Vertrags- oder Tabellendatei eine `.md`-Vorschau daneben, die auf GitHub direkt lesbar ist. Maßgeblich bleibt jeweils das Original.

| Datei | Inhalt |
|---|---|
| [README.md](../testakten/wandeldarlehen-beispielcase/README.md) | Überblick Sonnenglas UG / Northstar Pre-Seed Partners, Parteien, Konditionen |
| [Wandeldarlehen-Sonnenglas-Northstar-bilingual.md](../testakten/wandeldarlehen-beispielcase/Wandeldarlehen-Sonnenglas-Northstar-bilingual.md) | Markdown-Vorschau des bilingualen Vertrags (DE/EN) |
| [Wandeldarlehen-Sonnenglas-Northstar-bilingual.docx](../testakten/wandeldarlehen-beispielcase/Wandeldarlehen-Sonnenglas-Northstar-bilingual.docx) | Bilingualer Vertrag DE/EN, zweispaltig (Original) |
| [Wandeldarlehen-Sonnenglas-Northstar-nur-deutsch.md](../testakten/wandeldarlehen-beispielcase/Wandeldarlehen-Sonnenglas-Northstar-nur-deutsch.md) | Markdown-Vorschau des einsprachigen Vertrags |
| [Wandeldarlehen-Sonnenglas-Northstar-nur-deutsch.docx](../testakten/wandeldarlehen-beispielcase/Wandeldarlehen-Sonnenglas-Northstar-nur-deutsch.docx) | Einsprachige Vertragsfassung DE (Original) |
| [Cap-Table-Pre-Money.md](../testakten/wandeldarlehen-beispielcase/Cap-Table-Pre-Money.md) | Markdown-Vorschau Cap-Table vor Wandlung |
| [Cap-Table-Pre-Money.xlsx](../testakten/wandeldarlehen-beispielcase/Cap-Table-Pre-Money.xlsx) | Cap-Table vor Wandlung (Original) |
| [Cap-Table-Post-Money.md](../testakten/wandeldarlehen-beispielcase/Cap-Table-Post-Money.md) | Markdown-Vorschau Cap-Table nach Wandlung |
| [Cap-Table-Post-Money.xlsx](../testakten/wandeldarlehen-beispielcase/Cap-Table-Post-Money.xlsx) | Cap-Table nach Seed-Runde und Wandlung (Original) |
| [Wandlungserklaerung-Muster.md](../testakten/wandeldarlehen-beispielcase/Wandlungserklaerung-Muster.md) | Markdown-Vorschau der Wandlungserklärung |
| [Wandlungserklaerung-Muster.docx](../testakten/wandeldarlehen-beispielcase/Wandlungserklaerung-Muster.docx) | Muster-Wandlungserklärung Northstar an Sonnenglas (Original) |
| [Gesellschafterbeschluss-Kapitalerhoehung-Muster.md](../testakten/wandeldarlehen-beispielcase/Gesellschafterbeschluss-Kapitalerhoehung-Muster.md) | Markdown-Vorschau des Beschlusses |
| [Gesellschafterbeschluss-Kapitalerhoehung-Muster.docx](../testakten/wandeldarlehen-beispielcase/Gesellschafterbeschluss-Kapitalerhoehung-Muster.docx) | Beschluss über Kapitalerhöhung gegen Sacheinlage (Original) |
| [Notar-Paket-Inhaltsverzeichnis.md](../testakten/wandeldarlehen-beispielcase/Notar-Paket-Inhaltsverzeichnis.md) | Markdown-Vorschau Notar-Paket |
| [Notar-Paket-Inhaltsverzeichnis.docx](../testakten/wandeldarlehen-beispielcase/Notar-Paket-Inhaltsverzeichnis.docx) | Inhaltsverzeichnis aller Notar-Unterlagen (Original) |

## Lebenszyklus-Visualisierung

```
Phase A — Erstellung
  └─ Mandat-Triage → Parteien erfassen → Konditionen → Wandlungsmechanik
     → Rangrücktritt → Vertragserstellung (bilingual / einsprachig)
     → Vertraulichkeit und Sprachklausel

Phase B — Beurkundung und Unterzeichnung
  └─ Beurkundungserfordernis → Form (Textform/Schriftform/Notariell)
     → DocuSign-Unterzeichnung → Gesellschafterbeschluss (Absicht)
     → KYC/AML

Phase C — Wandelereignisse und Wandlungsberechnung
  └─ Eingang Wandlungserklärung → Trigger-Prüfung (Qualified Financing /
     Maturity / Liquidation) → Wandlungspreis-Berechnung
     → Cap-Table Pre/Post → Dokumente-Extraktion
     → Ausschluss-Prüfung → Mehrere WD → Kommunikation

Phase D — Gesellschafterbeschluss und Notar
  └─ Gesellschafterversammlung einberufen → Beschluss Kapitalerhöhung
     → Sacheinlagebericht → Notar-Paket → Gesellschafterliste
     → HR-Anmeldung → Post-Eintragung-Checkliste
```

## Skills nach Phasen

### Phase A — Erstellung (8 Skills)

| Slug | Beschreibung |
|---|---|
| `mandat-triage-wandeldarlehen` | Erstgespräch: Rechtsform, Beteiligte, Wandelereignisse, Sprachen-Stack |
| `parteien-erfassen` | Gesellschaft, Gesellschafterinnen, Darlehensgeber, KYC, Vertretungsmacht |
| `darlehenshoehe-konditionen` | Darlehensbetrag, Laufzeit, Zinssatz, Auszahlung, Bankverbindung |
| `wandlungsmechanik-konzipieren` | Cap, Discount, Trigger-Logik, Wandlungsformel, MFN, Pro-rata |
| `rangruecktritt-formulieren` | Qualifizierter Rangrücktritt BGH IX ZR 133/14, Durchsetzungssperre, IDW S 11 |
| `bilinguale-vertragserstellung` | Vollständiger Vertrag DE/EN zweispaltig, Sprachklausel |
| `einsprachige-vertragsfassung-de` | Einsprachige DE-Fassung, identischer materieller Inhalt |
| `vertraulichkeit-und-sprachklausel` | § 8 Vertraulichkeit, Sprachklausel, DIS-Schiedsklausel, salvatorische Klausel |

### Phase B — Beurkundung und Unterzeichnung (5 Skills)

| Slug | Beschreibung |
|---|---|
| `beurkundungserfordernis-pruefung` | § 15 GmbHG, zweistufige Konstruktion, OLG München 31 Wx 79/16, Heilungsklausel |
| `textform-vs-schriftform-vs-notariell` | § 126b/§ 126/§ 128 BGB, Formstufen, DocuSign-Praxis |
| `unterzeichnung-elektronisch-docusign` | Authentifizierung, Audit Trail, zehn Jahre Archivierung § 147 AO |
| `gesellschafterbeschluss-vorbereiten` | Grundsatzbeschluss Kapitalerhöhungsbereitschaft, § 51 GmbHG |
| `kyc-aml-geldwaesche` | GwG KYC, wirtschaftlich Berechtigte, PEP, Sanktionslisten EU/OFAC/UN |

### Phase C — Wandelereignisse und Wandlungsberechnung (10 Skills)

| Slug | Beschreibung |
|---|---|
| `wandelereignis-eingang` | Eingang Wandlungserklärung, Vier-Augen-Prüfung, Eingangsbestätigung |
| `wandlungspruefung-trigger-qualified-financing` | Schwellentest, MIN-Methode Cap/Discount/Rundenpreis |
| `wandlungspruefung-trigger-maturity` | Laufzeitablauf, Fall-back-Bewertung, Wahlrecht Lender |
| `wandlungspruefung-trigger-liquidation` | Exit/Trade Sale/IPO, Liquidationspräferenz, Wahlrecht |
| `wandlungspreis-berechnung` | Vollständige Formel, Aufrundung § 5 GmbHG, Kapitalrücklage § 272 HGB |
| `cap-table-update-pre-post` | Pre-Money und Post-Money Cap-Table, Verwässerungsdarstellung |
| `dokumenten-upload-extraktion` | Term Sheet, SPA, IRA: relevante Zahlen extrahieren |
| `wandlungsausschluss-pruefung` | Verfristung, Verjährung, Verwirkung, Verzicht |
| `mehrere-wandeldarlehen-parallel` | Stack-Order, MFN, gleichzeitige Wandlung, kombinierter Cap-Table |
| `wandlung-kommunikation-paketverteilung` | Lender, Gesellschaft, Steuerberater, Buchhaltung informieren |

### Phase D — Gesellschafterbeschluss und Notar (7 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschafterversammlung-einberufen` | Einberufung, § 51 GmbHG, Ladungsfristen, Vollmacht, Notartermin |
| `gesellschafterbeschluss-kapitalerhoehung` | Beschluss Kapitalerhöhung gegen Sacheinlage, § 53 Abs. 2 GmbHG |
| `sacheinlagebericht-werthaltigkeit` | Werthaltigkeit Forderung, Differenzhaftung § 9 GmbHG, IDW RS HFA 42 |
| `notar-paket-uebermittlung` | Vollständigkeitscheckliste, Notar-Briefing, § 57 GmbHG-Anmeldung |
| `gesellschafterliste-aktualisieren` | § 40 GmbHG, Gutglaubenswirkung § 16 GmbHG, Transparenzregister |
| `handelsregisteranmeldung-kapitalerhoehung` | § 57 GmbHG, Bearbeitungsdauer, Beanstandungsgründe, § 19 GwG |
| `post-eintragung-checkliste` | Bestätigung, Steuer (§ 20 UmwStG), Sperrfrist § 22 UmwStG, Abschluss-Memo |

## Rechtsgrundlagen

| Bereich | Normen |
|---|---|
| GmbH-Gesellschaftsrecht | GmbHG §§ 1, 5, 5a, 15, 40, 46, 49–51, 53–57, 78 |
| Insolvenzrecht | InsO §§ 17, 19, 38, 39, 44, 15a, 15b |
| Zivilrecht / Form | BGB §§ 126, 126b, 128, 130, 194 ff., 311, 314, 397, 398, 488 ff. |
| Geldwäscherecht | GwG §§ 1–3, 10–13, 19, 43, 47, 56 |
| Handelsrecht | HGB § 272 Abs. 2 Nr. 4 (Kapitalrücklage) |
| Steuerrecht | UmwStG §§ 20, 22; EStG § 17; AO § 147 |
| Elektronische Signatur | eIDAS-VO 910/2014; Art. 26 ff. |
| Schiedsgerichtsbarkeit | DIS-Schiedsordnung 2018 |

## Verwendungsbeispiel

**Einstiegs-Prompt:**

> „Ich möchte ein Wandeldarlehen aufsetzen — was brauchst du von mir?"

Das Plugin startet mit `mandat-triage-wandeldarlehen` und führt durch:
1. Rechtsform und Parteien klären
2. Konditionen und Wandlungsmechanik festlegen
3. Vertrag erstellen (bilingual DE/EN oder nur DE)
4. Beurkundungserfordernis prüfen
5. DocuSign-Unterzeichnung koordinieren
6. Bei Wandlungsereignis: Trigger prüfen, Preis berechnen, Cap-Table aktualisieren
7. Gesellschafterbeschluss und Notarpaket erstellen
8. Handelsregisteranmeldung begleiten

## Wichtiger Hinweis

Alle Texte dienen als Arbeitshilfe für die anwaltliche Praxis. Sie ersetzen keine rechtliche Beratung im Einzelfall. Jeder Skill verweist auf die maßgebliche Rechtsprechung (BGH/OLG mit Aktenzeichen und Datum). Änderungen in GmbHG, InsO, UmwStG oder GwG sind einzuarbeiten (Stand: 05/2026).
