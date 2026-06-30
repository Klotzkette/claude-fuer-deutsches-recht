# Regulatorisches Recht – Plugin für deutsches Aufsichtsrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`regulatorisches-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/regulatorisches-recht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/regulatorisches-recht/regulatorisches-recht-werkstatt.md" download><code>regulatorisches-recht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/regulatorisches-recht/regulatorisches-recht-schnellstart.md" download><code>regulatorisches-recht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | BaFin-Sonderprüfung Thalvenia Bank AG — Kryptoverwahrung, AML-Pflichtverletzungen, MiCAR-Lizenzkrise: [Gesamt-PDF](../testakten/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart/gesamt-pdf/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart_gesamt.pdf), [`testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip), [`testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Überwacht Aufsichts-Feeds, vergleicht neue Regulierungsakte gegen Ihre Richtlinienbibliothek und identifiziert Lücken. Lernt Ihre Materialitätsschwelle, damit keine Meldung bei jeder Pressemitteilung erfolgt. Ausgelegt für BaFin-Newsroom, Bundesgesetzblatt, EUR-Lex und direkte Behörden-Feeds.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, markiert und freigabepflichtig – keine Rechtsauskunft.** Das Plugin übernimmt die Arbeit: liest Dokumente, wendet Ihr Regelwerk an, findet Lücken, erstellt Vermerke. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Zitate werden nach Quelle gekennzeichnet. Privilegierungsvermerke werden konservativ gesetzt, damit kein unbeabsichtigter Verzicht entsteht. Folgenreiche Handlungen – Einreichungen, Versendungen, Ausführungen – erfordern ausdrückliche Bestätigung.

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

Automatisch generierte Komplett-Liste aller 61 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anhoerung-red-team-und-qualitaetskontrolle` | Anhörung: Red-Team und Qualitätskontrolle. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Regulatorisches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `aufsichts-feed-monitor` | Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Änderungen für Mandanten identifizieren. KWG WpHG DORA VAG BaFin-Rundschreiben. Prüfraster: Relevanz für Mandant Umsetzungsfrist Handlungsbedarf Meldepflich... |
| `aufsichtskommunikation-grundregeln` | Grundregeln Aufsichtskommunikation: Mitteilungspflichten, Auskunftsrechte, Sonderpruefung, Anhörung, Bussgeldverfahren. Tonfall, Tempo, Vollstaendigkeit, Konsistenz Schriftverkehr. Prüfraster für Antworten an BaFin, BNetzA, Bundeskartell... |
| `aufsichtsrecht-erstpruefung-und-mandatsziel` | Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `aufsichtssanktion-revision-spezial` | Revisionsverfahren gegen Aufsichtssanktion: BaFin-Verfuegung, BNetzA-Verfuegung. Widerspruch, Anfechtungsklage Verwaltungsgericht, Kostenrisiko. Prüfraster zur Erfolgsprognose und strategische Optionen (Vergleich, Verfahrensmaengel). Mus... |
| `aufsichtsverfahren-anhoerung-gwg` | Aufsichtsverfahren, Anhörung und Maßnahmebescheid: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Regulatorisches Recht. |
| `aufsichtsverfahren-formular-portal-und-einreichung` | Aufsichtsverfahren: Formular, Portal und Einreichungslogik. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `dokumente-intake` | Dokumentenintake für Regulatorisches Recht (Sektoren): sortiert Genehmigungsbescheid, Aufsichtsbescheid, Compliance-Manual, prüft Datum, Absender, Frist und Beweiswert (Compliance-Logs, Audit-Reports); markiert Lücken; berücksichtigt Man... |
| `dora-ikt-vertragspruefung` | IKT-Drittanbietervertraege auf DORA-Konformität prüfen wenn Finanzunternehmen digitale Dienstleistungen einkaufen. Art. 28 30 DORA VO (EU) 2022/2554. Prüfraster: Pflichtklauseln Art. 30 DORA Ausstiegsstrategien Aufsichtsrechte Subdienstl... |
| `dora-stellvertreter-und-konzern` | DORA-Spezial: Stellvertreter, Konzernregelungen, Outsourcing zum gruppeneigenen IT-Dienstleister, kritische TPP-Registrierung bei ESAs. Prüfraster und Klauseln in Konzern-IT-Vertraegen. Schnittstelle zu Aufsichtsrecht der Toechter im Aus... |
| `einstieg-routing` | Einstieg, Triage und Routing für Regulatorisches Recht (Sektoren): ordnet Rolle (Unternehmen reguliert, Aufsichtsbehörde, Verbraucher/Kunden), markiert Frist (Beschwerdefrist Aufsichtsbescheid), wählt Norm (TKG, EnWG, KWG, VersAufsG, AMG... |
| `enwg-feeds-heilmwerbg` | Enwg: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `feeds-compliance-dokumentation-und-akte` | Compliance-Dokumentation und Aktenvermerk fuer regulatorische Verfahren. Eingangsdaten ordnen, Schwellenwerte und Meldepflichten erfassen, Beweismittel listen und Aktenvermerk anlegen. |
| `fristen-risikoampel-mandantenkommunikation` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Regulatorisches Recht. |
| `gwg-fristen-form-und-zustaendigkeit` | GwG: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `heilmwerbg-risikoampel-und-gegenargumente` | Heilmwerbg: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `inkasso-massnahme-regulator` | Inkasso: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `inkasso-rdg-luecken-mar-mifid` | Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg Inkassoerlaubnis Zulassung... |
| `interview-fristennotiz-aufsichtssanktion` | Interview: Fristennotiz und nächster Schritt. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `kaltstart-interview` | Neues regulatorisches Mandat durch strukturiertes Erstgespraech aufnehmen. KWG WpHG DORA VAG GwG. Prüfraster: Branche Regulierungsrahmen Sachverhalt Fristen Pflichten Risiko. Output: Mandatssteckbrief Normenkarte fehlende Informationen.... |
| `luecken` | Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: n... |
| `luecken-aufzeiger` | Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen. GG Art. 12 80 AEUV Art. 107. Prüfraster: Normtext Regelungsziele Luecken unbeabsichtigte Folgen Verbesserungsvorschlaeg... |
| `mandat-arbeitsbereich` | Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behörden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. Ab... |
| `mar-mifid-eltif-uebergreifend` | MAR-MiFID-ELTIF uebergreifend: Insiderhandel, Marktmanipulation, Geeignetheit, ELTIF 2.0 Retail-Vertrieb. Prüfraster ueber alle drei Regelwerke für einen typischen Produktentwicklungsfall. Schnittstellen und Konfliktpunkte im Regulatoris... |
| `massnahme-mandantenkommunikation-entscheidungsvorlage` | Maßnahme: Mandantenkommunikation und Entscheidungsvorlage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Regulatorisches Recht (Sektoren): stimmt Adressat (Unternehmen reguliert, Aufsichtsbehörde, Verbraucher/Kunden), Frist (Beschwerdefrist Aufsichtsbescheid) und Form auf den Zweck ab — typische Outputs: Stellungnahme Aufsic... |
| `quellen-livecheck` | Quellen-Live-Check für Regulatorisches Recht (Sektoren): prüft Normen (TKG, EnWG, KWG, VersAufsG, AMG, Branchen-Spezialgesetze) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BNetzA und Quellenhygiene nach refere... |
| `rdg-quellenkarte` | Rdg Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `regr-dora-resilienz` | Spezialfall DORA Digital Operational Resilience Act: IKT-Risikomanagement, Drittparteienrisiko, TLPT-Tests. Prüfraster für Finanzunternehmen und IKT-Dienstleister im Regulatorisches Recht. |
| `regr-finanzdienstleistungsregulierung-bauleiter` | Bauleiter Finanzdienstleistungsregulierung: KWG, ZAG, KAGB, WpHG, BaFin-Mitteilungen. Prüfraster für Lizenz- und Erlaubnistatbestaende im Regulatorisches Recht. |
| `regr-mica-kryptoassets-spezial` | Spezialfall MiCA-Verordnung Kryptoassets: Asset-Referenced-Tokens, E-Money-Tokens, andere Kryptowerte. Prüfraster für Emittent, CASP, Vertrieb im Regulatorisches Recht. |
| `regr-mifid2-regrecht-einfuehrung-internal` | Leitfaden MiFID II und MAR: Wohlverhaltenspflichten, Suitability, Ad-hoc-Publizitaet, Insiderrecht. Prüfraster für Emittent und Wertpapierdienstleister im Regulatorisches Recht. |
| `regrecht-einfuehrung-sektoren` | Einfuehrung regulatorisches Recht in den wichtigsten Sektoren: Bank, Versicherung, Energie, Telekommunikation, Verkehr, Pharma, Lebensmittel. Pro Sektor: Aufsicht, Kernnormen, Lizenzpflicht, typische Compliance-Aufgaben. Entscheidungstab... |
| `regrecht-internal-policies-design` | Internal Policies regulatorisch design: Hierarchie (Konzernrichtlinie, Tochterrichtlinie, Arbeitsanweisung, Verfahrensbeschreibung), Pflichtbestandteile, Versionierung, Verteilung, Schulung, Wirksamkeitsmessung. Mustertemplate für Bank-... |
| `regulator-zahlen-schwellen-und-berechnung` | Regulator: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `regulatorik-mandatssteckbrief-behoerden-fristen` | Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. A... |
| `regulatorisches-richtlinien-neufassung` | Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf. Output: ueberarbeit... |
| `regulatorisches-stellungnahmen-beweislast` | Regulatorisches: Internationaler Bezug und Schnittstellen. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `richtlinien-anhoerung-red-aufsichtsrecht` | Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Änderungshistorie Bedeutung der Änderungen. Output: Vergleichst... |
| `richtlinien-neufassung` | Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg. Output: neue Richtli... |
| `sonderfall-edge-case` | Kaltstart: Sonderfall und Edge-Case-Prüfung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verf... |
| `spezial-anhoerung-red-team-und-qualitaetskontrolle` | Anhoerung: Red-Team und Qualitätskontrolle. |
| `spezial-feeds-compliance-dokumentation-und-akte` | Feeds: Compliance-Dokumentation und Aktenvermerk. |
| `spezial-massnahme-mandantenkommunikation-entscheidungsvorlage` | Massnahme: Mandantenkommunikation und Entscheidungsvorlage. |
| `spezial-rdg-livequellen-und-rechtsprechungscheck` | RDG: Livequellen- und Rechtsprechungscheck. |
| `stellungnahmen` | Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prüfraster: Konsultationsumfang regulatorische Ziele Kritikpunkte Alternativvorschlaege Verhältnismäßigkeit. Output: str... |
| `stellungnahmen-beweislast-und-darlegungslast` | Stellungnahmen: Beweislast, Darlegungslast und Substantiierung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `umsatzsteuer-behoerden-gericht-und-registerweg` | Umsatzsteuer: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Regulatorisches Recht (Sektoren): trennt fehlende Tatsachen von fehlenden Belegen (Genehmigungsbescheid, Aufsichtsbescheid, Compliance-Manual), nennt pro Lücke Beweisthema, Beschaffungsweg (BNetzA), Fris... |
| `ustva-aufsichtskommunikation-grundregeln-dora` | Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse Vorsteuer Fristen Sonder... |
| `voranmeldung-schriftsatz-brief-und-memo-bausteine` | Voranmeldung: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `wochendigest-interessen-wphg-stellungnahmen` | Wochendigest: Mehrparteienkonflikt und Interessenmatrix. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Regulatorisches Recht. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Regulatorisches Recht. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Regulatorisches Recht. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Regulatorisches Recht. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `wphg-tatbestand-beweis-und-belege` | Wphg: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `wpig-und-zag-pruefung` | WpIG und ZAG Prüfung: Wertpapierinstitutsgesetz und Zahlungsdiensteaufsichtsgesetz Voraussetzungen für Lizenz, Anwendungsbereich, Schnittstellen zu PSD3-Entwurf, Crypto-Asset-Service-Provider unter MiCAR: WpIG und ZAG Prüfung: Wertpapier... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
