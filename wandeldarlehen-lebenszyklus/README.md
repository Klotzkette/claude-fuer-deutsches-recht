# Wandeldarlehen-Lebenszyklus

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/wandeldarlehen-lebenszyklus.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`wandeldarlehen-lebenszyklus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wandeldarlehen-lebenszyklus.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/wandeldarlehen-lebenszyklus/wandeldarlehen-lebenszyklus-werkstatt.md" download><code>wandeldarlehen-lebenszyklus-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/wandeldarlehen-lebenszyklus/wandeldarlehen-lebenszyklus-schnellstart.md" download><code>wandeldarlehen-lebenszyklus-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Nebelstern Ventures - Berliner VC-Pipeline, Wandeldarlehen und Follow-on-Chaos](../testakten/venture-capital-geber-nebelstern-portfolio-berlin/README.md) | [Gesamt-PDF](../testakten/venture-capital-geber-nebelstern-portfolio-berlin/gesamt-pdf/venture-capital-geber-nebelstern-portfolio-berlin_gesamt.pdf) | [`testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip) | [`testakte-venture-capital-geber-nebelstern-portfolio-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-venture-capital-geber-nebelstern-portfolio-berlin-einzelpdfs.zip) |
| [Wandeldarlehen-Lebenszyklus (Sonnenglas Solartechnologie UG)](../testakten/wandeldarlehen-beispielcase/README.md) | [Gesamt-PDF](../testakten/wandeldarlehen-beispielcase/gesamt-pdf/wandeldarlehen-beispielcase_gesamt.pdf) | [`testakte-wandeldarlehen-beispielcase.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wandeldarlehen-beispielcase.zip) | [`testakte-wandeldarlehen-beispielcase-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wandeldarlehen-beispielcase-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Vollständiger Workflow-Assistent für den Lebenszyklus eines Wandeldarlehens bei GmbH und UG (haftungsbeschränkt) — von der ersten Mandatsbesprechung über Vertragsgestaltung (bilingual DE/EN oder einsprachig DE), Beurkundungsprüfung, Wandelereignisse und Wandlungsberechnung bis zum Cap-Table-Update, Gesellschafterbeschluss und Handelsregisteranmeldung durch den Notar.

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

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`begleitet-erstpruefung-und-mandatsziel`](skills/begleitet-erstpruefung-und-mandatsziel/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md), [`mandat-triage-mehrere-parallel`](skills/mandat-triage-mehrere-parallel/SKILL.md), [`wandelereignis-eingang`](skills/wandelereignis-eingang/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`beurkundungspruefung-quellenkarte-check`](skills/beurkundungspruefung-quellenkarte-check/SKILL.md), [`dokumenten-upload-formfehler-heilungs`](skills/dokumenten-upload-formfehler-heilungs/SKILL.md), [`spezial-beurkundungspruefung-livequellen-check`](skills/spezial-beurkundungspruefung-livequellen-check/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`vollstaendigen-tatbestand-beweis-und-belege`](skills/vollstaendigen-tatbestand-beweis-und-belege/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`beurkundungserfordernis-pruefung`](skills/beurkundungserfordernis-pruefung/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`wandlungspreis-wandlungspruefung-trigger`](skills/wandlungspreis-wandlungspruefung-trigger/SKILL.md), [`wandlungspruefung-trigger`](skills/wandlungspruefung-trigger/SKILL.md), [`wandlungspruefung-trigger-liquidation`](skills/wandlungspruefung-trigger-liquidation/SKILL.md), [`wandlungspruefung-trigger-qualified-financing`](skills/wandlungspruefung-trigger-qualified-financing/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`bilinguale-vertragserstellung`](skills/bilinguale-vertragserstellung/SKILL.md), [`einsprachig-verhandlung-vergleich-und-eskalation`](skills/einsprachig-verhandlung-vergleich-und-eskalation/SKILL.md), [`einsprachige-vertragsfassung`](skills/einsprachige-vertragsfassung/SKILL.md), [`lebenszyklus-bilinguale-vertragserstellung`](skills/lebenszyklus-bilinguale-vertragserstellung/SKILL.md), [`vertragserstellung-behoerden-gericht-und-registerweg`](skills/vertragserstellung-behoerden-gericht-und-registerweg/SKILL.md), [`vertraulichkeit-sprachklausel`](skills/vertraulichkeit-sprachklausel/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`chronologie-fristen`](skills/chronologie-fristen/SKILL.md), [`gesellschafterbeschluss-kapitalerhoehung`](skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md), [`gesellschafterbeschluss-vorbereiten`](skills/gesellschafterbeschluss-vorbereiten/SKILL.md), [`handelsregisteranmeldung-kapitalerhoehung-kyc`](skills/handelsregisteranmeldung-kapitalerhoehung-kyc/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-waehlen`](skills/output-waehlen/SKILL.md), [`sacheinlagebericht-werthaltigkeit-begleitet`](skills/sacheinlagebericht-werthaltigkeit-begleitet/SKILL.md), [`wandelereignis-trigger-wandlung-kommunikation`](skills/wandelereignis-trigger-wandlung-kommunikation/SKILL.md), [`wandlung-kommunikation-paketverteilung`](skills/wandlung-kommunikation-paketverteilung/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`formfehler-heilungs-timeline`](skills/formfehler-heilungs-timeline/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`bilingual-einsprachig`](skills/bilingual-einsprachig/SKILL.md), [`cap-table-darlehenshoehe-konditionen`](skills/cap-table-darlehenshoehe-konditionen/SKILL.md), [`darlehenshoehe-konditionen`](skills/darlehenshoehe-konditionen/SKILL.md), [`gesellschafterliste-aktualisieren`](skills/gesellschafterliste-aktualisieren/SKILL.md), [`gesellschafterversammlung-einberufen`](skills/gesellschafterversammlung-einberufen/SKILL.md), [`gmbh-vollstaendigen`](skills/gmbh-vollstaendigen/SKILL.md), [`kyc-aml-geldwaesche`](skills/kyc-aml-geldwaesche/SKILL.md), [`mehrere-wandeldarlehen-parallel`](skills/mehrere-wandeldarlehen-parallel/SKILL.md), [`notar-paket-parteien-erfassen`](skills/notar-paket-parteien-erfassen/SKILL.md), [`parteien-erfassen`](skills/parteien-erfassen/SKILL.md), [`post-eintragung-rangruecktritt-formulieren`](skills/post-eintragung-rangruecktritt-formulieren/SKILL.md), [`rangruecktritt-formulieren`](skills/rangruecktritt-formulieren/SKILL.md), [`textform-vs-schriftform-vs-notariell`](skills/textform-vs-schriftform-vs-notariell/SKILL.md), [`unterzeichnung-elektronisch-wandelereignis`](skills/unterzeichnung-elektronisch-wandelereignis/SKILL.md), [`wandeldarlehens-wandelereignisse`](skills/wandeldarlehens-wandelereignisse/SKILL.md), [`wandelereignisse-zahlen-schwellen-und-berechnung`](skills/wandelereignisse-zahlen-schwellen-und-berechnung/SKILL.md), [`wandlungsausloeser-cap-discount-textform`](skills/wandlungsausloeser-cap-discount-textform/SKILL.md), [`wandlungsausschluss-wandlungsmechanik`](skills/wandlungsausschluss-wandlungsmechanik/SKILL.md), ... plus 1 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`begleitet-erstpruefung-und-mandatsziel`](skills/begleitet-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Begleitet: Erstprüfung, Rollenklärung und Mandatsziel in Wandeldarlehen-Lebenszyklus geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beurkundungserfordernis-pruefung`](skills/beurkundungserfordernis-pruefung/SKILL.md) | Wenn es um Beurkundungserfordernis-Prüfung in Wandeldarlehen-Lebenszyklus geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`beurkundungspruefung-quellenkarte-check`](skills/beurkundungspruefung-quellenkarte-check/SKILL.md) | Wenn es um Beurkundungspruefung Quellenkarte Check in Wandeldarlehen-Lebenszyklus geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nach... |
| [`bilingual-einsprachig`](skills/bilingual-einsprachig/SKILL.md) | Wenn es um Bilingual: Schriftsatz-, Brief- und Memo-Bausteine in Wandeldarlehen-Lebenszyklus geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und A... |
| [`bilinguale-vertragserstellung`](skills/bilinguale-vertragserstellung/SKILL.md) | Wenn es um Bilinguale Vertragserstellung DE/EN in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`cap-table-darlehenshoehe-konditionen`](skills/cap-table-darlehenshoehe-konditionen/SKILL.md) | Wenn es um Cap-Table Update – Pre-Money und Post-Money in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`chronologie-fristen`](skills/chronologie-fristen/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`darlehenshoehe-konditionen`](skills/darlehenshoehe-konditionen/SKILL.md) | Wenn es um Darlehensbetrag und Konditionen in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dokumenten-upload-formfehler-heilungs`](skills/dokumenten-upload-formfehler-heilungs/SKILL.md) | Wenn es um Dokumenten-Upload und Datenextraktion in Wandeldarlehen-Lebenszyklus geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`einsprachig-verhandlung-vergleich-und-eskalation`](skills/einsprachig-verhandlung-vergleich-und-eskalation/SKILL.md) | Wenn es um Einsprachig: Verhandlung, Vergleich und Eskalation in Wandeldarlehen-Lebenszyklus geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`einsprachige-vertragsfassung`](skills/einsprachige-vertragsfassung/SKILL.md) | Wenn es um Einsprachige Vertragsfassung (nur DE) in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Wandeldarlehen-Lebenszyklus geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`formfehler-heilungs-timeline`](skills/formfehler-heilungs-timeline/SKILL.md) | Wenn es um Formfehler und Heilungs-Timeline in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`gesellschafterbeschluss-kapitalerhoehung`](skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md) | Wenn es um Gesellschafterbeschluss – Kapitalerhöhung gegen Sacheinlage in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`gesellschafterbeschluss-vorbereiten`](skills/gesellschafterbeschluss-vorbereiten/SKILL.md) | Wenn es um Gesellschafterbeschluss vorbereiten (vor Unterzeichnung) in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gesellschafterliste-aktualisieren`](skills/gesellschafterliste-aktualisieren/SKILL.md) | Wenn es um Gesellschafterliste aktualisieren (Paragraf 40 GmbHG) in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gesellschafterversammlung-einberufen`](skills/gesellschafterversammlung-einberufen/SKILL.md) | Wenn es um Gesellschafterversammlung einberufen (Kapitalerhöhung) in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gmbh-vollstaendigen`](skills/gmbh-vollstaendigen/SKILL.md) | Wenn es um GmbH: Risikoampel, Gegenargumente und Verteidigungslinien in Wandeldarlehen-Lebenszyklus geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`handelsregisteranmeldung-kapitalerhoehung-kyc`](skills/handelsregisteranmeldung-kapitalerhoehung-kyc/SKILL.md) | Wenn es um Handelsregisteranmeldung Kapitalerhöhung in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Wandeldarlehen Lebenszyklus ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) | Wenn es um Kaltstart Triage in Wandeldarlehen-Lebenszyklus geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kyc-aml-geldwaesche`](skills/kyc-aml-geldwaesche/SKILL.md) | Wenn es um KYC / AML / Geldwäscheprävention in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`lebenszyklus-bilinguale-vertragserstellung`](skills/lebenszyklus-bilinguale-vertragserstellung/SKILL.md) | Wenn es um Lebenszyklus: Fristen, Form, Zuständigkeit und Rechtsweg in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandat-triage-mehrere-parallel`](skills/mandat-triage-mehrere-parallel/SKILL.md) | Wenn es um Mandat-Triage Wandeldarlehen – Erstgespräch in Wandeldarlehen-Lebenszyklus geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mehrere-wandeldarlehen-parallel`](skills/mehrere-wandeldarlehen-parallel/SKILL.md) | Wenn es um Mehrere parallele Wandeldarlehen in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`notar-paket-parteien-erfassen`](skills/notar-paket-parteien-erfassen/SKILL.md) | Wenn es um Notar-Paket zur Handelsregister-Anmeldung in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Wandeldarlehen-Lebenszyklus geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`parteien-erfassen`](skills/parteien-erfassen/SKILL.md) | Wenn es um Parteien erfassen – KYC und Vertretungsmacht in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`post-eintragung-rangruecktritt-formulieren`](skills/post-eintragung-rangruecktritt-formulieren/SKILL.md) | Wenn es um Post-Eintragung-Checkliste in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rangruecktritt-formulieren`](skills/rangruecktritt-formulieren/SKILL.md) | Wenn es um Qualifizierten Rangrücktritt formulieren in Wandeldarlehen-Lebenszyklus geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nac... |
| [`sacheinlagebericht-werthaltigkeit-begleitet`](skills/sacheinlagebericht-werthaltigkeit-begleitet/SKILL.md) | Wenn es um Sacheinlagebericht und Werthaltigkeit der Forderung in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-beurkundungspruefung-livequellen-check`](skills/spezial-beurkundungspruefung-livequellen-check/SKILL.md) | Wenn es um Beurkundungspruefung: Livequellen- und Rechtsprechungscheck in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`textform-vs-schriftform-vs-notariell`](skills/textform-vs-schriftform-vs-notariell/SKILL.md) | Wenn es um Textform vs. Schriftform vs. Notarielle Beurkundung in Wandeldarlehen-Lebenszyklus geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterzeichnung-elektronisch-wandelereignis`](skills/unterzeichnung-elektronisch-wandelereignis/SKILL.md) | Wenn es um Elektronische Unterzeichnung (DocuSign / Adobe Sign) in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| [`vertragserstellung-behoerden-gericht-und-registerweg`](skills/vertragserstellung-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Vertragserstellung: Behörden-, Gerichts- oder Registerweg in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vertraulichkeit-sprachklausel`](skills/vertraulichkeit-sprachklausel/SKILL.md) | Wenn es um Vertraulichkeit und Sprachklausel in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vollstaendigen-tatbestand-beweis-und-belege`](skills/vollstaendigen-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Vollstaendigen: Tatbestandsmerkmale, Beweisfragen und Beleglage in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`wandeldarlehens-wandelereignisse`](skills/wandeldarlehens-wandelereignisse/SKILL.md) | Wenn es um Wandeldarlehens: Dokumentenmatrix, Lückenliste und Nachforderung in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`wandelereignis-eingang`](skills/wandelereignis-eingang/SKILL.md) | Wenn es um Wandelereignis – Eingang Wandlungserklärung in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wandelereignis-trigger-wandlung-kommunikation`](skills/wandelereignis-trigger-wandlung-kommunikation/SKILL.md) | Wenn es um Master-Dispatcher Wandelereignis in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wandelereignisse-zahlen-schwellen-und-berechnung`](skills/wandelereignisse-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Wandelereignisse: Zahlen, Schwellenwerte und Berechnung in Wandeldarlehen-Lebenszyklus geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrol... |
| [`wandlung-kommunikation-paketverteilung`](skills/wandlung-kommunikation-paketverteilung/SKILL.md) | Wenn es um Wandlung – Kommunikation und Paketverteilung in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wandlungsausloeser-cap-discount-textform`](skills/wandlungsausloeser-cap-discount-textform/SKILL.md) | Wenn es um Wandlungsauslöser, Cap und Discount sauber berechnen in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfr... |
| [`wandlungsausschluss-wandlungsmechanik`](skills/wandlungsausschluss-wandlungsmechanik/SKILL.md) | Wenn es um Wandlungsausschluss-Prüfung in Wandeldarlehen-Lebenszyklus geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`wandlungsmechanik-konzipieren`](skills/wandlungsmechanik-konzipieren/SKILL.md) | Wenn es um Wandlungsmechanik konzipieren in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wandlungspreis-wandlungspruefung-trigger`](skills/wandlungspreis-wandlungspruefung-trigger/SKILL.md) | Wenn es um Wandlungspreis-Berechnung in Wandeldarlehen-Lebenszyklus geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`wandlungspruefung-trigger`](skills/wandlungspruefung-trigger/SKILL.md) | Wenn es um Wandlungsprüfung – Trigger Maturity (Laufzeitablauf) in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wandlungspruefung-trigger-liquidation`](skills/wandlungspruefung-trigger-liquidation/SKILL.md) | Wenn es um Wandlungsprüfung – Trigger Liquidation Event in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wandlungspruefung-trigger-qualified-financing`](skills/wandlungspruefung-trigger-qualified-financing/SKILL.md) | Wenn es um Wandlungsprüfung – Trigger Qualified Financing in Wandeldarlehen-Lebenszyklus geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in Wandeldarlehen-Lebenszyklus geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Wandeldarlehen-Lebenszyklus geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Wandeldarlehen-Lebenszyklus geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
