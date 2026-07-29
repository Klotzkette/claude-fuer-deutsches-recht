# Regulatorisches Recht – Plugin für deutsches Aufsichtsrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/regulatorisches-recht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`regulatorisches-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/regulatorisches-recht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/regulatorisches-recht/regulatorisches-recht-werkstatt.md" download><code>regulatorisches-recht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/regulatorisches-recht/regulatorisches-recht-schnellstart.md" download><code>regulatorisches-recht-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [BaFin-Sonderprüfung Thalvenia Bank AG — Kryptoverwahrung, AML-Pflichtverletzungen, MiCAR-Lizenzkrise](../testakten/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart/README.md) | [Gesamt-PDF](../testakten/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart/gesamt-pdf/bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart_gesamt.pdf) | [`testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart.zip) | [`testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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
| **lücken-aufzeiger** *(Referenz)* | Gemeinsames Gap- und Kommentar-Tracker-Framework, das von `/luecken` und `/stellungnahmen` geladen wird |

## Interaktive Skills vs. geplante Agenten

Die obigen Skills werden bei Aufruf ausgeführt – für die aktive Arbeit an einem Mandat. Die folgenden Agenten laufen planmäßig – für das, was sich bewegt, wenn Sie nicht hinsehen:

| Agent | Was er beobachtet | Standardrhythmus |
|---|---|---|
| **regulierungs-änderungs-monitor** | Aufsichts-Feeds – filtert nach der bei der Ersteinrichtung erlernten Materialitätsschwelle und erstellt ein Digest aus Signal statt Rauschen | Wöchentlich (täglich bei aktivem regulatorischen Umfeld) |

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

**Finanzmarktrecht:** KWG, ZAG, WpHG, WpIG, GwG, KAGB, MaBV und BörsG; MaRisk in der aktuellen Fassung des BaFin-Rundschreibens 06/2024 (BA); DORA und die zugehörigen technischen Standards seit dem 17. Januar 2025 für den jeweils erfassten Anwendungsbereich

**Energie- und Telekommunikationsrecht:** EnWG, TKG, MessZV

**Heilmittel-/Gesundheitsrecht:** HeilMWerbG, AMG, MPG/MDR-EU, PatDSG

**Steuerrecht (Verfahren):** UStG, AO, FGO

## Hinweise

- Materialitätsfilterung ist der Mehrwert. Alles ist "technisch eine Regulierungsänderung" – das Plugin lernt, was hier tatsächlich wichtig ist.
- Policy-Diff vergleicht gegen indizierte Richtlinien. Wenn die Richtlinienbibliothek nicht verbunden ist, laufen Diffs gegen eingefügte Inhalte.
- Dies ist die automatisierte Version von `datenschutzrecht/regulierungs-luecken-analyse`. Kombination empfohlen: dieses beobachtet, jenes taucht tiefer ein.

## Konfiguration

Ihre Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` gespeichert und überlebt Plugin-Updates – die Einrichtung wird nur einmal durchgeführt.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-router`](skills/anschluss-router/SKILL.md), [`aufsichtsrecht-erstpruefung-und-mandatsziel`](skills/aufsichtsrecht-erstpruefung-und-mandatsziel/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`kaltstart-interview`](skills/kaltstart-interview/SKILL.md), [`mandat-arbeitsbereich`](skills/mandat-arbeitsbereich/SKILL.md), [`regulatorik-mandatssteckbrief-behoerden-fristen`](skills/regulatorik-mandatssteckbrief-behoerden-fristen/SKILL.md), [`workflow-anschluss-skills-router`](skills/workflow-anschluss-skills-router/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`aufsichtsverfahren-formular-portal-und-einreichung`](skills/aufsichtsverfahren-formular-portal-und-einreichung/SKILL.md), [`feeds-compliance-dokumentation-und-akte`](skills/feeds-compliance-dokumentation-und-akte/SKILL.md), [`inkasso-rdg-luecken-mar-mifid`](skills/inkasso-rdg-luecken-mar-mifid/SKILL.md), [`luecken`](skills/luecken/SKILL.md), [`luecken-aufzeiger`](skills/luecken-aufzeiger/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`rdg-quellenkarte`](skills/rdg-quellenkarte/SKILL.md), [`regulatorisches-stellungnahmen-beweislast`](skills/regulatorisches-stellungnahmen-beweislast/SKILL.md), [`spezial-feeds-compliance-dokumentation-und-akte`](skills/spezial-feeds-compliance-dokumentation-und-akte/SKILL.md), [`spezial-rdg-livequellen-und-rechtsprechungscheck`](skills/spezial-rdg-livequellen-und-rechtsprechungscheck/SKILL.md), [`stellungnahmen-beweislast-und-darlegungslast`](skills/stellungnahmen-beweislast-und-darlegungslast/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md), [`wphg-tatbestand-beweis-und-belege`](skills/wphg-tatbestand-beweis-und-belege/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`dora-ikt-vertragspruefung`](skills/dora-ikt-vertragspruefung/SKILL.md), [`fristen-risikoampel-mandantenkommunikation`](skills/fristen-risikoampel-mandantenkommunikation/SKILL.md), [`heilmwerbg-risikoampel-und-gegenargumente`](skills/heilmwerbg-risikoampel-und-gegenargumente/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`wpig-und-zag-pruefung`](skills/wpig-und-zag-pruefung/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`aufsichtsverfahren-anhoerung-gwg`](skills/aufsichtsverfahren-anhoerung-gwg/SKILL.md), [`gwg-fristen-form-und-zustaendigkeit`](skills/gwg-fristen-form-und-zustaendigkeit/SKILL.md), [`interview-fristennotiz-aufsichtssanktion`](skills/interview-fristennotiz-aufsichtssanktion/SKILL.md), [`umsatzsteuer-behoerden-gericht-und-registerweg`](skills/umsatzsteuer-behoerden-gericht-und-registerweg/SKILL.md), [`voranmeldung-schriftsatz-brief-und-memo-bausteine`](skills/voranmeldung-schriftsatz-brief-und-memo-bausteine/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`aufsichtskommunikation-grundregeln`](skills/aufsichtskommunikation-grundregeln/SKILL.md), [`massnahme-mandantenkommunikation-entscheidungsvorlage`](skills/massnahme-mandantenkommunikation-entscheidungsvorlage/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md), [`spezial-massnahme-mandantenkommunikation-entscheidungsvorlage`](skills/spezial-massnahme-mandantenkommunikation-entscheidungsvorlage/SKILL.md), [`stellungnahmen`](skills/stellungnahmen/SKILL.md), [`ustva-aufsichtskommunikation-grundregeln-dora`](skills/ustva-aufsichtskommunikation-grundregeln-dora/SKILL.md), [`wochendigest-interessen-wphg-stellungnahmen`](skills/wochendigest-interessen-wphg-stellungnahmen/SKILL.md), [`workflow-mandantenkommunikation`](skills/workflow-mandantenkommunikation/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`anhoerung-red-team-und-qualitaetskontrolle`](skills/anhoerung-red-team-und-qualitaetskontrolle/SKILL.md), [`spezial-anhoerung-red-team-und-qualitaetskontrolle`](skills/spezial-anhoerung-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`aufsichts-feed-monitor`](skills/aufsichts-feed-monitor/SKILL.md), [`aufsichtssanktion-revision-spezial`](skills/aufsichtssanktion-revision-spezial/SKILL.md), [`dora-stellvertreter-und-konzern`](skills/dora-stellvertreter-und-konzern/SKILL.md), [`enwg-feeds-heilmwerbg`](skills/enwg-feeds-heilmwerbg/SKILL.md), [`inkasso-massnahme-regulator`](skills/inkasso-massnahme-regulator/SKILL.md), [`mar-mifid-eltif-uebergreifend`](skills/mar-mifid-eltif-uebergreifend/SKILL.md), [`regr-dora-resilienz`](skills/regr-dora-resilienz/SKILL.md), [`regr-finanzdienstleistungsregulierung-bauleiter`](skills/regr-finanzdienstleistungsregulierung-bauleiter/SKILL.md), [`regr-mica-kryptoassets-spezial`](skills/regr-mica-kryptoassets-spezial/SKILL.md), [`regr-mifid2-regrecht-einfuehrung-internal`](skills/regr-mifid2-regrecht-einfuehrung-internal/SKILL.md), [`regrecht-einfuehrung-sektoren`](skills/regrecht-einfuehrung-sektoren/SKILL.md), [`regrecht-internal-policies-design`](skills/regrecht-internal-policies-design/SKILL.md), [`regulator-zahlen-schwellen-und-berechnung`](skills/regulator-zahlen-schwellen-und-berechnung/SKILL.md), [`regulatorisches-richtlinien-neufassung`](skills/regulatorisches-richtlinien-neufassung/SKILL.md), [`richtlinien-anhoerung-red-aufsichtsrecht`](skills/richtlinien-anhoerung-red-aufsichtsrecht/SKILL.md), [`richtlinien-neufassung`](skills/richtlinien-neufassung/SKILL.md), [`sonderfall-edge-case`](skills/sonderfall-edge-case/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 62 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`anhoerung-red-team-und-qualitaetskontrolle`](skills/anhoerung-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Anhörung: Red-Team und Qualitätskontrolle in Regulatorisches Recht – Plugin für deutsches geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anschluss-router`](skills/anschluss-router/SKILL.md) | Wenn es um Regulatorisches Recht — Allgemein in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufsichts-feed-monitor`](skills/aufsichts-feed-monitor/SKILL.md) | Wenn es um Regulatorischer Feed-Watcher in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufsichtskommunikation-grundregeln`](skills/aufsichtskommunikation-grundregeln/SKILL.md) | Wenn es um Aufsichtskommunikation Grundregeln in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufsichtsrecht-erstpruefung-und-mandatsziel`](skills/aufsichtsrecht-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel in Regulatorisches Recht – Plugin für deutsches geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel... |
| [`aufsichtssanktion-revision-spezial`](skills/aufsichtssanktion-revision-spezial/SKILL.md) | Wenn es um Aufsichtssanktion: Revision in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufsichtsverfahren-anhoerung-gwg`](skills/aufsichtsverfahren-anhoerung-gwg/SKILL.md) | Wenn es um Aufsichtsverfahren, Anhörung und Maßnahmebescheid in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits-... |
| [`aufsichtsverfahren-formular-portal-und-einreichung`](skills/aufsichtsverfahren-formular-portal-und-einreichung/SKILL.md) | Wenn es um Aufsichtsverfahren: Formular, Portal und Einreichungslogik in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dora-ikt-vertragspruefung`](skills/dora-ikt-vertragspruefung/SKILL.md) | Wenn es um DORA-IKT-Vertragsprüfung in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dora-stellvertreter-und-konzern`](skills/dora-stellvertreter-und-konzern/SKILL.md) | Wenn es um DORA: Konzern und Stellvertreter in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Regulatorisches Recht – Plugin für deutsches geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`enwg-feeds-heilmwerbg`](skills/enwg-feeds-heilmwerbg/SKILL.md) | Wenn es um Enwg: Dokumentenmatrix, Lückenliste und Nachforderung in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`feeds-compliance-dokumentation-und-akte`](skills/feeds-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Compliance-Dokumentation und Aktenvermerk (regulatorische Verfahren) in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| [`fristen-risikoampel-mandantenkommunikation`](skills/fristen-risikoampel-mandantenkommunikation/SKILL.md) | Wenn es um Fristen- und Risikoampel in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gwg-fristen-form-und-zustaendigkeit`](skills/gwg-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um GwG: Fristen, Form, Zuständigkeit und Rechtsweg in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`heilmwerbg-risikoampel-und-gegenargumente`](skills/heilmwerbg-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Heilmwerbg: Risikoampel, Gegenargumente und Verteidigungslinien in Regulatorisches Recht – Plugin für deutsches geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel... |
| [`inkasso-massnahme-regulator`](skills/inkasso-massnahme-regulator/SKILL.md) | Wenn es um Inkasso: Verhandlung, Vergleich und Eskalation in Regulatorisches Recht – Plugin für deutsches geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Opt... |
| [`inkasso-rdg-luecken-mar-mifid`](skills/inkasso-rdg-luecken-mar-mifid/SKILL.md) | Wenn es um Inkassodienstleistungen (RDG) in Regulatorisches Recht – Plugin für deutsches geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlag... |
| [`interview-fristennotiz-aufsichtssanktion`](skills/interview-fristennotiz-aufsichtssanktion/SKILL.md) | Wenn es um Interview: Fristennotiz und nächster Schritt in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Regulatorisches Recht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-interview`](skills/kaltstart-interview/SKILL.md) | Wenn es um Ersteinrichtung – Regulatorisches Recht in Regulatorisches Recht – Plugin für deutsches geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`luecken`](skills/luecken/SKILL.md) | Pflegt den aufsichtsrechtlichen Gap-Tracker ohne fachliche Befunde zu erfinden. Sortiert belegte Lücken nach Rechtsstatus, Risiko und Terminbasis und erzeugt Verantwortungs-, Eskalations- und Abschlussnachweise. |
| [`luecken-aufzeiger`](skills/luecken-aufzeiger/SKILL.md) | Vergleicht interne Richtlinien mit dem aktuell anwendbaren Aufsichtsrahmen. Trennt verbindliches Recht, Verwaltungspraxis und Orientierungshilfen und liefert eine belegte Gap-Matrix mit Priorität, Verantwortlichem und umsetzbarer Maßnahme. |
| [`mandat-arbeitsbereich`](skills/mandat-arbeitsbereich/SKILL.md) | Wenn es um Mandat-Workspace-Verwaltung in Regulatorisches Recht – Plugin für deutsches geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mar-mifid-eltif-uebergreifend`](skills/mar-mifid-eltif-uebergreifend/SKILL.md) | Wenn es um MAR und MiFID und ELTIF in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`massnahme-mandantenkommunikation-entscheidungsvorlage`](skills/massnahme-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Maßnahme: Mandantenkommunikation und Entscheidungsvorlage in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Soforts... |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Regulatorisches Recht – Plugin für deutsches geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Regulatorisches Recht – Plugin für deutsches geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`rdg-quellenkarte`](skills/rdg-quellenkarte/SKILL.md) | Wenn es um Rdg Quellenkarte in Regulatorisches Recht – Plugin für deutsches geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`regr-dora-resilienz`](skills/regr-dora-resilienz/SKILL.md) | Wenn es um RegR: DORA-Resilienz in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`regr-finanzdienstleistungsregulierung-bauleiter`](skills/regr-finanzdienstleistungsregulierung-bauleiter/SKILL.md) | Wenn es um RegR: FDL-Regulierung Bauleiter in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`regr-mica-kryptoassets-spezial`](skills/regr-mica-kryptoassets-spezial/SKILL.md) | Wenn es um RegR: MiCA Kryptoassets in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`regr-mifid2-regrecht-einfuehrung-internal`](skills/regr-mifid2-regrecht-einfuehrung-internal/SKILL.md) | Wenn es um RegR: MiFID II MAR in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`regrecht-einfuehrung-sektoren`](skills/regrecht-einfuehrung-sektoren/SKILL.md) | Wenn es um Regrecht: Sektoren-Einfuehrung in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`regrecht-internal-policies-design`](skills/regrecht-internal-policies-design/SKILL.md) | Wenn es um Regrecht: Internal Policies in Regulatorisches Recht – Plugin für deutsches geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken... |
| [`regulator-zahlen-schwellen-und-berechnung`](skills/regulator-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Regulator: Zahlen, Schwellenwerte und Berechnung in Regulatorisches Recht – Plugin für deutsches geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen u... |
| [`regulatorik-mandatssteckbrief-behoerden-fristen`](skills/regulatorik-mandatssteckbrief-behoerden-fristen/SKILL.md) | Wenn es um Regulatorisches Mandat: Behörden, Fristen und Rollen in Regulatorisches Recht – Plugin für deutsches geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofo... |
| [`regulatorisches-richtlinien-neufassung`](skills/regulatorisches-richtlinien-neufassung/SKILL.md) | Wenn es um Praxisprofil anpassen in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`regulatorisches-stellungnahmen-beweislast`](skills/regulatorisches-stellungnahmen-beweislast/SKILL.md) | Wenn es um Regulatorisches: Internationaler Bezug und Schnittstellen in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Soforts... |
| [`richtlinien-anhoerung-red-aufsichtsrecht`](skills/richtlinien-anhoerung-red-aufsichtsrecht/SKILL.md) | Erstellt einen prüfbaren Diff zwischen aktueller Aufsichtsquelle und interner Richtlinie. Ordnet jede Abweichung nach Geltungsstatus, Wortlaut, Umsetzung und Nachweis und übergibt konkrete Redline- und Eskalationsaufträge. |
| [`richtlinien-neufassung`](skills/richtlinien-neufassung/SKILL.md) | Überführt eine belegte aufsichtsrechtliche Lücke in eine vollständige interne Richtlinie oder Redline. Liefert normgenaue Regelungen, Rollen, Kontrollen, Nachweise, Freigabeschritte und eine umsetzbare Inkraftsetzungsfassung. |
| [`sonderfall-edge-case`](skills/sonderfall-edge-case/SKILL.md) | Wenn es um Kaltstart: Sonderfall und Edge-Case-Prüfung in Regulatorisches Recht – Plugin für deutsches geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschri... |
| [`spezial-anhoerung-red-team-und-qualitaetskontrolle`](skills/spezial-anhoerung-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Anhoerung: Red-Team und Qualitätskontrolle in Regulatorisches Recht – Plugin für deutsches geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-feeds-compliance-dokumentation-und-akte`](skills/spezial-feeds-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Feeds: Compliance-Dokumentation und Aktenvermerk in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-massnahme-mandantenkommunikation-entscheidungsvorlage`](skills/spezial-massnahme-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Massnahme: Mandantenkommunikation und Entscheidungsvorlage in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| [`spezial-rdg-livequellen-und-rechtsprechungscheck`](skills/spezial-rdg-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um RDG: Livequellen- und Rechtsprechungscheck in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stellungnahmen`](skills/stellungnahmen/SKILL.md) | Wenn es um Konsultationsbeiträge in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stellungnahmen-beweislast-und-darlegungslast`](skills/stellungnahmen-beweislast-und-darlegungslast/SKILL.md) | Wenn es um Stellungnahmen: Beweislast, Darlegungslast und Substantiierung in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit So... |
| [`umsatzsteuer-behoerden-gericht-und-registerweg`](skills/umsatzsteuer-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Umsatzsteuer: Behörden-, Gerichts- oder Registerweg in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ustva-aufsichtskommunikation-grundregeln-dora`](skills/ustva-aufsichtskommunikation-grundregeln-dora/SKILL.md) | Wenn es um Umsatzsteuer-Voranmeldung (Paragraf 18 UStG) in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`voranmeldung-schriftsatz-brief-und-memo-bausteine`](skills/voranmeldung-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Voranmeldung: Schriftsatz-, Brief- und Memo-Bausteine in Regulatorisches Recht – Plugin für deutsches geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträg... |
| [`wochendigest-interessen-wphg-stellungnahmen`](skills/wochendigest-interessen-wphg-stellungnahmen/SKILL.md) | Wenn es um Wochendigest: Mehrparteienkonflikt und Interessenmatrix in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortsch... |
| [`workflow-anschluss-skills-router`](skills/workflow-anschluss-skills-router/SKILL.md) | Wenn es um Anschluss-Skills Router in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Regulatorisches Recht – Plugin für deutsches geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-mandantenkommunikation`](skills/workflow-mandantenkommunikation/SKILL.md) | Wenn es um Mandantenkommunikation in Regulatorisches Recht – Plugin für deutsches geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Regulatorisches Recht – Plugin für deutsches geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`wphg-tatbestand-beweis-und-belege`](skills/wphg-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Wphg: Tatbestandsmerkmale, Beweisfragen und Beleglage in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`wpig-und-zag-pruefung`](skills/wpig-und-zag-pruefung/SKILL.md) | Wenn es um Wpig Und Zag Prüfung in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
