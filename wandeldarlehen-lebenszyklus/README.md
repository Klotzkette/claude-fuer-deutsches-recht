# Wandeldarlehen-Lebenszyklus

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`wandeldarlehen-lebenszyklus`) | [`wandeldarlehen-lebenszyklus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wandeldarlehen-lebenszyklus.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Wandeldarlehen-Lebenszyklus (Sonnenglas Solartechnologie UG)** (`wandeldarlehen-beispielcase`) | [Gesamt-PDF lesen](../testakten/wandeldarlehen-beispielcase/gesamt-pdf/wandeldarlehen-beispielcase_gesamt.pdf) | [`testakte-wandeldarlehen-beispielcase.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wandeldarlehen-beispielcase.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Vollständiger Workflow-Assistent für den Lebenszyklus eines Wandeldarlehens bei GmbH und UG (haftungsbeschränkt) — von der ersten Mandatsbesprechung über Vertragsgestaltung (bilingual DE/EN oder einsprachig DE), Beurkundungsprüfung, Wandelereignisse und Wandlungsberechnung bis zum Cap-Table-Update, Gesellschafterbeschluss und Handelsregisteranmeldung durch den Notar.

## Direkt-Download

[wandeldarlehen-lebenszyklus.zip herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wandeldarlehen-lebenszyklus.zip)

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Wandeldarlehen-Lebenszyklus (Sonnenglas Solartechnologie UG)** ([`testakten/wandeldarlehen-beispielcase/`](../testakten/wandeldarlehen-beispielcase/)).

Direkt-Download als ZIP: [testakte-wandeldarlehen-beispielcase.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wandeldarlehen-beispielcase.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Lebenszyklus-Visualisierung

```
Phase A — Erstellung
  └─ Mandat-Triage → Parteien erfassen → Konditionen → Wandlungsmechanik
     → Rangrücktritt → Vertragserstellung (bilingual / einsprachig)
     → Vertraulichkeit und Sprachklausel

Phase B — Beurkundung und Unterzeichnung
  └─ Beurkundungserfordernis → Form (Textform/Schriftform/Notariell)
     → Formfehler-Heilungs-Timeline → DocuSign-Unterzeichnung
     → Gesellschafterbeschluss (Absicht) → KYC/AML

Phase C — Wandelereignisse und Wandlungsberechnung
  └─ Eingang Wandlungserklärung → Trigger-Dispatcher → Trigger-Prüfung
     (Qualified Financing / Maturity / Liquidation) → Wandlungspreis-Berechnung
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
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `bilinguale-vertragserstellung` | Vollständiger Vertrag DE/EN zweispaltig, Sprachklausel |
| `einsprachige-vertragsfassung-de` | Einsprachige DE-Fassung, identischer materieller Inhalt |
| `vertraulichkeit-und-sprachklausel` | § 8 Vertraulichkeit, Sprachklausel, DIS-Schiedsklausel, salvatorische Klausel |

### Phase B — Beurkundung und Unterzeichnung (6 Skills)

| Slug | Beschreibung |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `textform-vs-schriftform-vs-notariell` | § 126b/§ 126/§ 128 BGB, Formstufen, DocuSign-Praxis |
| `formfehler-heilungs-timeline` | Form-Stufen § 126b/§ 126/§ 128 BGB, Heilung durch nachfolgende Beurkundung § 15 Abs. 4 S. 2 GmbHG, Insolvenz-Risiko-Fenster |
| `unterzeichnung-elektronisch-docusign` | Authentifizierung, Audit Trail, zehn Jahre Archivierung § 147 AO |
| `gesellschafterbeschluss-vorbereiten` | Grundsatzbeschluss Kapitalerhöhungsbereitschaft, § 51 GmbHG |
| `kyc-aml-geldwaesche` | GwG KYC, wirtschaftlich Berechtigte, PEP, Sanktionslisten EU/OFAC/UN |

### Phase C — Wandelereignisse und Wandlungsberechnung (11 Skills)

| Slug | Beschreibung |
|---|---|
| `wandelereignis-eingang` | Eingang Wandlungserklärung, Vier-Augen-Prüfung, Eingangsbestätigung |
| `wandelereignis-trigger-dispatcher` | Master-Logik bei parallelen Triggern, Prioritäts-Regelung, Cap-Table-Simulation, MFN-Kaskade |
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
| Handelsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| Steuerrecht | UmwStG §§ 20, 22; EStG § 17; AO § 147 |
| Elektronische Signatur | eIDAS-VO 910/2014; Art. 26 ff. |
| Schiedsgerichtsbarkeit | DIS-Schiedsordnung 2018 |

## Verwendungsbeispiel

**Einstiegs-Prompt:**

> "Ich möchte ein Wandeldarlehen aufsetzen — was brauchst du von mir?"

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

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Wandeldarlehen Lebenszyklus-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arb... |
| `beurkundungserfordernis-pruefung` | Beurkundungserfordernis für Wandeldarlehen und Kapitalerhohung prüfen wenn Frage besteht ob Notartermin erforderlich ist. §§ 15 55 GmbHG § 311b BGB Formvorschriften. Prüfraster: Sacheinlage Kapitalerhohung GmbH-Anteil Vorratskapital Abtr... |
| `bilinguale-vertragserstellung` | Wandeldarlehensvertrag zweisprachig deutsch und englisch erstellen für internationale Transaktionen oder ausl. Investoren. BGB Darlehen §§ 488 ff. BGB GmbHG Kapitalerhohung. Prüfraster: Terminologie-Konsistenz Rechtswahl governing-law ju... |
| `cap-table-update-pre-post` | Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 GmbHG Kapitalerhohung §§ 17 ff. GmbHG Gesellschafterliste. Prüfraster: Pre-Money Post-Money Wandlungspreis neue Anteil... |
| `darlehenshoehe-konditionen` | Darlehenshoehe Zinsen Laufzeit und Konditionen für Wandeldarlehen verhandeln und dokumentieren. §§ 488 491 BGB Darlehensvertrag §§ 246 247 BGB Zinsen. Prüfraster: Darlehenshoehe Zinssatz Disagio Laufzeit Fälligkeit Sicherheiten Rangrückt... |
| `dokumenten-upload-extraktion` | Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardterminologie. Prüfraster: Vertragsparteien Darlehenshoehe Zinsen Wandlungspreisbeschreibung Trigger Laufzeit Sonderrec... |
| `einsprachige-vertragsfassung-de` | Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Prüfraster: SAFE-Konditionen BGB-Konformität Schriftformerfordernisse Investoren-So... |
| `formfehler-heilungs-timeline` | Formfehler in Wandeldarlehen oder Kapitalerhohungsdokumenten identifizieren und Heilungsmassnahmen planen. §§ 125 311b BGB Nichtigkeit §§ 15 55 GmbHG Formerfordernisse. Prüfraster: Formmangel Nichtigkeit Heilung Nachbeurkundung Fristen.... |
| `gesellschafterbeschluss-kapitalerhoehung` | Gesellschafterbeschluss für Kapitalerhohung nach Wandlung vorbereiten. §§ 53 55 56 GmbHG Kapitalerhohung. Prüfraster: Beschlussinhalt Mehrheitserfordernisse notarielle Form neues Stammkapital Einlagepflicht Handelsregistereintrag. Output... |
| `gesellschafterbeschluss-vorbereiten` | Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten. §§ 46 53 GmbHG Gesellschafterbeschluesse. Prüfraster: Beschlussgegenstand Mehrheiten Ladungspflicht Form Anlagen. Output: Beschlussentwurf Sitzungspr... |
| `gesellschafterliste-aktualisieren` | Gesellschafterliste nach Kapitalerhohung durch Wandlung aktualisieren und beim Handelsregister einreichen. § 40 GmbHG Gesellschafterliste § 16 GmbHG Legitimationswirkung. Prüfraster: neue Gesellschafter Anteile Stammnummern Notar Einreic... |
| `gesellschafterversammlung-einberufen` | Gesellschafterversammlung für Wandeldarlehensmandat einberufen und Tagesordnung aufstellen. §§ 49 51 GmbHG Ladungspflichten. Prüfraster: Ladungsfrist Form Tagesordnung Quorum Vollmachten Protokollpflicht. Output: Einberufungsschreiben Ta... |
| `handelsregisteranmeldung-kapitalerhoehung` | Handelsregisteranmeldung nach Kapitalerhohung durch Wandlung vorbereiten. § 57 GmbHG Anmeldepflicht §§ 54 55 GmbHG Kapitalerhohung. Prüfraster: Anmeldungsinhalt Unterlagen Notar Einreichungspflicht Eintragungsvoraussetzungen. Output: Anm... |
| `kyc-aml-geldwaesche` | KYC- und AML-Anforderungen bei Wandeldarlehensmandat prüfen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG Sorgfaltspflichten. Prüfraster: wirtschaftlich Berechtigter Risikoklasse PEP-Status Herkunft Kapital Dokumentation. Ou... |
| `mandat-triage-wandeldarlehen` | Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Vertragstyp SAFE Convertible Note Laufzeit Wandlungsereignisse offene Punkte. Output: Mandatssteckbrief R... |
| `mehrere-wandeldarlehen-parallel` | Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren und Konflikte erkennen. §§ 488 ff. BGB § 39 InsO Rangrücktritt. Prüfraster: Pari-passu-Stellung Rangregelungen Wandlungsrechte Verwasserungsschutz Vesting. Output... |
| `notar-paket-uebermittlung` | Notarpaket für Beurkundungstermin bei Kapitalerhohung durch Wandlung zusammenstellen und uebermitteln. §§ 15 55 GmbHG BeurkG. Prüfraster: Vollständigkeit Beschluss Zeichnungsschein Gesellschafterliste Vollmachten Identitätsnachweise. Out... |
| `parteien-erfassen` | Vertragsparteien eines Wandeldarlehens vollständig identifizieren und dokumentieren. §§ 13 17 GmbHG Gesellschafter §§ 305 ff. BGB AGB bei mehreren Darlehensgebern. Prüfraster: Darlehensgeberin Darlehensnehmerin vertretungsberechtigte Org... |
| `post-eintragung-checkliste` | Nacharbeiten nach Handelsregistereintragung der Kapitalerhohung abschließen. §§ 57 40 GmbHG §§ 39 16 GmbHG Legitimationswirkung. Prüfraster: Eintragsbekanntmachung Gesellschafterliste Anteilsurkunden Investor-Cap-Table-Update Mitteilungs... |
| `rangruecktritt-formulieren` | Rangrücktrittserklärung für Wandeldarlehen formulieren um insolvenzrechtliche Nachrang­wirkung herzustellen. § 39 InsO qualifizierter Rangrücktritt. Prüfraster: Formulierungsanforderungen BGH-Anforderungen qualifizierter Nachrang Masseve... |
| `sacheinlagebericht-werthaltigkeit` | Sacheinlagebericht für Sachkapitalerhohung durch Wandeldarlehen erstellen und Werthaltigkeit prufen. § 56 GmbHG Sacheinlage §§ 19 8 GmbHG Einlageverpflichtung. Prüfraster: Sacheinlagegegenstand Bewertung Werthaltigkeit Bericht Unterschri... |
| `spezial-begleitet-erstpruefung-und-mandatsziel` | Begleitet: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-beurkundungspruefung-livequellen-check` | Beurkundungspruefung: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bilingual-schriftsatz-brief-und-memo-bausteine` | Bilingual: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-einsprachig-verhandlung-vergleich-und-eskalation` | Einsprachig: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gmbh-risikoampel-und-gegenargumente` | GmbH: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-lebenszyklus-fristen-form-und-zustaendigkeit` | Lebenszyklus: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertragserstellung-behoerden-gericht-und-registerweg` | Vertragserstellung: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vollstaendigen-tatbestand-beweis-und-belege` | Vollstaendigen: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wandeldarlehens-dokumentenmatrix-und-lueckenliste` | Wandeldarlehens: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wandelereignisse-zahlen-schwellen-und-berechnung` | Wandelereignisse: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wandlungsausloeser-cap-und-discount` | Wandlungsauslöser, Cap und Discount sauber berechnen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `textform-vs-schriftform-vs-notariell` | Formerfordernis für einzelne Wandeldarlehens-Dokumente bestimmen und zuordnen. §§ 126 126a 126b BGB Schriftform Textform elektronische Form. Prüfraster: Vertragstyp Erklärung Beschluss gesetzliches Formerfordernis vereinbartes Formerford... |
| `unterzeichnung-elektronisch-docusign` | Elektronische Unterzeichnung von Wandeldarlehensvertraegen und Begleitdokumenten organisieren. §§ 126a 126b BGB eIDAS-VO qualifizierte elektronische Signatur. Prüfraster: Formerfordernis je Dokument einfache QES oder qualifizierte Signat... |
| `vertraulichkeit-und-sprachklausel` | Vertraulichkeits- und Sprachklauseln in Wandeldarlehensvertrag prüfen oder formulieren. §§ 307 ff. BGB AGB-Recht § 5 BDSG Datengeheimnis. Prüfraster: Geheimhaltungsumfang Ausnahmen Vertragssprache Kollisionsregel Sprachklausel. Output: K... |
| `wandelereignis-eingang` | Eingehende Wandelereignis-Notification prüfen und naechste Schritte bestimmen wenn Investor Wandlung ankündigt. §§ 488 ff. BGB Darlehensvertrag §§ 53 55 GmbHG. Prüfraster: Trigger-Typ Frist Preisbestimmung Erklärung Kapitalerhohungsbedar... |
| `wandelereignis-trigger-dispatcher` | Wandlungstrigger kategorisieren und an den richtigen Folge-Skill weiterleiten wenn Wandelereignis vorliegt. §§ 488 ff. BGB GmbHG SAFE-Terminologie. Prüfraster: Trigger-Typ Qualified Financing Maturity Liquidation Exit Klassifizierung. Ou... |
| `wandlung-kommunikation-paketverteilung` | Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung organisieren. §§ 130 132 BGB Zugang §§ 15 55 GmbHG. Prüfraster: Empfaengerliste Dokumente Zugang Fristen Bestätigung. Output: Kommunikationsplan Versandpr... |
| `wandlungsausschluss-pruefung` | Prüfen ob Wandlung gesperrt oder ausgeschlossen ist bei vertraglichen oder gesetzlichen Hindernissen. §§ 134 138 BGB Nichtigkeit § 30 GmbHG Kapitalerhaltung. Prüfraster: Ausschlusstatbestaende Insolvenzreife Kapitalerhaltungsverbot Vorzu... |
| `wandlungsmechanik-konzipieren` | Wandlungsmechanik eines SAFE oder Convertible Note konzipieren: Preis Verwasserungsschutz Sonderrechte. SAFE Y-Combinator-Terminologie §§ 53 55 GmbHG §§ 488 ff. BGB. Prüfraster: Wandlungspreis Bewertungsdeckel Rabatt Verwasserungsschutz... |
| `wandlungspreis-berechnung` | Wandlungspreis auf Basis vertraglich vereinbarter Parameter berechnen wenn Wandlung ausgelöst wird. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Bewertungsdeckel Rabatt Qualified-Financing-Preis MFN Verwasserungsschutz Rundungsregel.... |
| `wandlungspruefung-trigger-liquidation` | Wandlung bei Liquidationsereignis Auflösung oder Exit prüfen. §§ 60 ff. GmbHG Auflösungsgründe § 179a AktG. Prüfraster: Liquidationstatbestand Liquidationspraeference Verwasserungsschutz Rangordnung Zahlungsreihenfolge. Output: Prüfproto... |
| `wandlungspruefung-trigger-maturity` | Wandlung bei Laufzeitablauf des Wandeldarlehens prüfen wenn kein qualifiziertes Finanzierungsereignis eingetreten ist. §§ 488 ff. BGB Fälligkeit. Prüfraster: Laufzeitenddatum Wandlungsrecht Wandlungspflicht Rückzahlungsalternative Preisb... |
| `wandlungspruefung-trigger-qualified-financing` | Wandlung bei qualifizierter Finanzierungsrunde prüfen wenn neue Investitionsrunde als Trigger definiert ist. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Qualified-Financing-Definition Mindestbetrag Lead-Investor Wandlungspflicht oder... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin wandeldarlehen-lebenszyklus: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin wandeldarlehen-lebenszyklus: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin wandeldarlehen-lebenszyklus: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin wandeldarlehen-lebenszyklus: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin wandeldarlehen-lebenszyklus: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin wandeldarlehen-lebenszyklus: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
