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
| **BaFin-Sonderprüfung Thalvenia Bank AG — Kryptoverwahrung, AML-Pflichtverletzungen, MiCAR-Lizenzkrise** (`bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart`) | [Gesamt-PDF lesen](../testakten/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart/gesamt-pdf/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart_gesamt.pdf) | [`testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Regulatorisches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `aufsichts-feed-monitor` | Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifizieren. KWG WpHG DORA VAG BaFin-Rundschreiben. Prüfraster: Relevanz für Mandant Umsetzungsfrist Handlungsbedarf Meldepflic... |
| `aufsichtskommunikation-grundregeln` | Grundregeln Aufsichtskommunikation: Mitteilungspflichten, Auskunftsrechte, Sonderpruefung, Anhoerung, Bussgeldverfahren. Tonfall, Tempo, Vollstaendigkeit, Konsistenz Schriftverkehr. Pruefraster fuer Antworten an BaFin, BNetzA, Bundeskart... |
| `aufsichtssanktion-revision-spezial` | Revisionsverfahren gegen Aufsichtssanktion: BaFin-Verfuegung, BNetzA-Verfuegung. Widerspruch, Anfechtungsklage Verwaltungsgericht, Kostenrisiko. Pruefraster zur Erfolgsprognose und strategische Optionen (Vergleich, Verfahrensmaengel). Mu... |
| `dora-ikt-vertragspruefung` | IKT-Drittanbietervertraege auf DORA-Konformität prüfen wenn Finanzunternehmen digitale Dienstleistungen einkaufen. Art. 28 30 DORA VO (EU) 2022/2554. Prüfraster: Pflichtklauseln Art. 30 DORA Ausstiegsstrategien Aufsichtsrechte Subdienstl... |
| `dora-stellvertreter-und-konzern` | DORA-Spezial: Stellvertreter, Konzernregelungen, Outsourcing zum gruppeneigenen IT-Dienstleister, kritische TPP-Registrierung bei ESAs. Pruefraster und Klauseln in Konzern-IT-Vertraegen. Schnittstelle zu Aufsichtsrecht der Toechter im Au... |
| `inkasso-rdg` | Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg Inkassoerlaubnis Zulassung... |
| `luecken` | Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: n... |
| `luecken-aufzeiger` | Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen. GG Art. 12 80 AEUV Art. 107. Prüfraster: Normtext Regelungsziele Luecken unbeabsichtigte Folgen Verbesserungsvorschlaeg... |
| `mar-mifid-eltif-uebergreifend` | MAR-MiFID-ELTIF uebergreifend: Insiderhandel, Marktmanipulation, Geeignetheit, ELTIF 2.0 Retail-Vertrieb. Pruefraster ueber alle drei Regelwerke fuer einen typischen Produktentwicklungsfall. Schnittstellen und Konfliktpunkte. |
| `regr-dora-resilienz-spezial` | Spezialfall DORA Digital Operational Resilience Act: IKT-Risikomanagement, Drittparteienrisiko, TLPT-Tests. Pruefraster fuer Finanzunternehmen und IKT-Dienstleister. |
| `regr-finanzdienstleistungsregulierung-bauleiter` | Bauleiter Finanzdienstleistungsregulierung: KWG, ZAG, KAGB, WpHG, BaFin-Mitteilungen. Pruefraster fuer Lizenz- und Erlaubnistatbestaende. |
| `regr-mica-kryptoassets-spezial` | Spezialfall MiCA-Verordnung Kryptoassets: Asset-Referenced-Tokens, E-Money-Tokens, andere Kryptowerte. Pruefraster fuer Emittent, CASP, Vertrieb. |
| `regr-mifid2-mar-leitfaden` | Leitfaden MiFID II und MAR: Wohlverhaltenspflichten, Suitability, Ad-hoc-Publizitaet, Insiderrecht. Pruefraster fuer Emittent und Wertpapierdienstleister. |
| `regrecht-einfuehrung-sektoren` | Einfuehrung regulatorisches Recht in den wichtigsten Sektoren: Bank, Versicherung, Energie, Telekommunikation, Verkehr, Pharma, Lebensmittel. Pro Sektor: Aufsicht, Kernnormen, Lizenzpflicht, typische Compliance-Aufgaben. Entscheidungstab... |
| `regrecht-internal-policies-design` | Internal Policies regulatorisch design: Hierarchie (Konzernrichtlinie, Tochterrichtlinie, Arbeitsanweisung, Verfahrensbeschreibung), Pflichtbestandteile, Versionierung, Verteilung, Schulung, Wirksamkeitsmessung. Mustertemplate fuer Bank-... |
| `regulatorisches-recht-anpassen` | Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf. Output: ueberarbeit... |
| `regulatorisches-recht-kaltstart-interview` | Neues regulatorisches Mandat durch strukturiertes Erstgespraech aufnehmen. KWG WpHG DORA VAG GwG. Prüfraster: Branche Regulierungsrahmen Sachverhalt Fristen Pflichten Risiko. Output: Mandatssteckbrief Normenkarte fehlende Informationen.... |
| `regulatorisches-recht-mandat-arbeitsbereich` | Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. A... |
| `richtlinien-neufassung` | Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg. Output: neue Richtli... |
| `richtlinien-vergleich` | Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Aenderungshistorie Bedeutung der Aenderungen. Output: Vergleich... |
| `spezial-anhoerung-red-team-und-qualitaetskontrolle` | Anhoerung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-aufsichtsrecht-erstpruefung-und-mandatsziel` | Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-aufsichtsverfahren-anhoerung-massnahme` | Aufsichtsverfahren, Anhörung und Maßnahmebescheid: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-aufsichtsverfahren-formular-portal-und-einreichung` | Aufsichtsverfahren: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-enwg-dokumentenmatrix-und-lueckenliste` | Enwg: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-feeds-compliance-dokumentation-und-akte` | Feeds: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gwg-fristen-form-und-zustaendigkeit` | GwG: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-heilmwerbg-risikoampel-und-gegenargumente` | Heilmwerbg: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-inkasso-verhandlung-vergleich-und-eskalation` | Inkasso: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-interview-fristennotiz-und-naechster-schritt` | Interview: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kaltstart-sonderfall-und-edge-case` | Kaltstart: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-massnahme-mandantenkommunikation-entscheidungsvorlage` | Massnahme: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rdg-livequellen-und-rechtsprechungscheck` | RDG: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-regulator-zahlen-schwellen-und-berechnung` | Regulator: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-regulatorisches-internationaler-bezug-und-schnittstellen` | Regulatorisches: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stellungnahmen-beweislast-und-darlegungslast` | Stellungnahmen: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-umsatzsteuer-behoerden-gericht-und-registerweg` | Umsatzsteuer: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-voranmeldung-schriftsatz-brief-und-memo-bausteine` | Voranmeldung: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wochendigest-mehrparteien-konflikt-und-interessen` | Wochendigest: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wphg-tatbestand-beweis-und-belege` | Wphg: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `stellungnahmen` | Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prüfraster: Konsultationsumfang regulatorische Ziele Kritikpunkte Alternativvorschlaege Verhältnismäßigkeit. Output: str... |
| `ustva` | Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse Vorsteuer Fristen Sonder... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin regulatorisches-recht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin regulatorisches-recht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin regulatorisches-recht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin regulatorisches-recht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin regulatorisches-recht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin regulatorisches-recht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin regulatorisches-recht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin regulatorisches-recht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin regulatorisches-recht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin regulatorisches-recht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `wpig-und-zag-pruefung` | WpIG und ZAG Pruefung: Wertpapierinstitutsgesetz und Zahlungsdiensteaufsichtsgesetz Voraussetzungen fuer Lizenz, Anwendungsbereich, Schnittstellen zu PSD3-Entwurf, Crypto-Asset-Service-Provider unter MiCAR. Pruefraster fuer Geschaeftsmod... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
