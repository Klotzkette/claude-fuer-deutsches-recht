---
name: befristung-tzbfg-bem-verfahren-fazugang
description: "Befristung Tzbfg BEM Verfahren Fazugang im Plugin Fachanwalt Arbeitsrecht: prüft konkret Befristungskontrolle und Befristungsgestaltung nach TzBfG, Prüfungslinie für fachanwalt arbeitsrecht bem verfahren, Kündigungsfrist berechnen bei unsicherem Zugangsdatum. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Befristung Tzbfg BEM Verfahren Fazugang

## Arbeitsbereich

**Befristung Tzbfg BEM Verfahren Fazugang** ordnet den Fall über die tragenden Prüfungslinien: Befristungskontrolle und Befristungsgestaltung nach TzBfG, Prüfungslinie für fachanwalt arbeitsrecht bem verfahren, Kündigungsfrist berechnen bei unsicherem Zugangsdatum. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-arbeitsrecht-befristung-tzbfg` | Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer. Anwendungsfall befristeter Arbeitsvertrag soll geprüft oder neuer Befristungsvertrag gestaltet werden. Normen § 14 TzBfG Sachgrundbefristung sachgrundlose Befristung § 14 Abs. 4 TzBfG Schriftform vor Beschaeftigungsbeginn § 17 TzBfG Klagefrist drei Wochen. Prüfraster Schriftform-Zeitpunkt Sachgrund Vorbeschaeftigungsverbot § 14 Abs. 2 S. 2 BAG-Linie. Output Befristungsprüf-Protokoll oder Befristungsvertrags-Entwurf mit Klagefrist-Hinweis. Abgrenzung zu fachanwalt-arbeitsrecht-kündigungsschutzklage und fachanwalt-arbeitsrecht-betriebsratsanhoerung. |
| `fachanwalt-arbeitsrecht-bem-verfahren` | Prüfungslinie für fachanwalt arbeitsrecht bem verfahren: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `fazugang-neu-005-kuendigungsfrist-berechnen-bei-unsicherem-zugan` | Kündigungsfrist berechnen bei unsicherem Zugangsdatum: frühest- und spätestmöglicher Zugang, Fristberechnung §§ 187 ff. BGB, Drei-Wochen-Klagefrist § 4 KSchG, Kündigungsfristen § 622 BGB, worst-case-Strategie für Mandant. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-arbeitsrecht-befristung-tzbfg`

**Fokus:** Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer. Anwendungsfall befristeter Arbeitsvertrag soll geprüft oder neuer Befristungsvertrag gestaltet werden. Normen § 14 TzBfG Sachgrundbefristung sachgrundlose Befristung § 14 Abs. 4 TzBfG Schriftform vor Beschaeftigungsbeginn § 17 TzBfG Klagefrist drei Wochen. Prüfraster Schriftform-Zeitpunkt Sachgrund Vorbeschaeftigungsverbot § 14 Abs. 2 S. 2 BAG-Linie. Output Befristungsprüf-Protokoll oder Befristungsvertrags-Entwurf mit Klagefrist-Hinweis. Abgrenzung zu fachanwalt-arbeitsrecht-kündigungsschutzklage und fachanwalt-arbeitsrecht-betriebsratsanhoerung.

# Befristung nach TzBfG (Teilzeit- und Befristungsgesetz)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Befristung nach TzBfG (Teilzeit- und Befristungsgesetz)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Kaltstart-Rückfragen

1. Liegt schriftlicher Arbeitsvertrag mit Befristung **vor** Beschäftigungsbeginn vor?
2. Sachgrundbefristung (§ 14 Abs. 1 TzBfG) oder sachgrundlos (§ 14 Abs. 2 TzBfG)?
3. Bei sachgrundloser Befristung: Vorbeschäftigung bei diesem Arbeitgeber?
4. Verlängerungen oder echte Neubefristung?
5. Wann endet die Befristung?

## Rechtsgrundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Sachgrundbefristung:** § 14 Abs. 1 TzBfG, sachliche Gründe in S. 2 Nr. 1 bis 8.
- **Sachgrundlos:** § 14 Abs. 2 TzBfG — bis zu zwei Jahre, höchstens dreimalige Verlängerung in dieser Zeit.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Befristungskontrollklage:** § 17 TzBfG — drei Wochen nach vereinbartem Ende; Versäumung führt zur Fiktion der Wirksamkeit (§ 17 S. 2 iVm § 7 KSchG).
- **Neueinstellung Älterer:** § 14 Abs. 3 TzBfG — sachgrundlose Befristung bis fünf Jahre, wenn der Arbeitnehmer bei Beginn des befristeten Arbeitsverhältnisses das 52. Lebensjahr vollendet hat **und** unmittelbar vor Beginn des Arbeitsverhältnisses **mindestens vier Monate** beschäftigungslos war (§ 138 SGB III), Transferkurzarbeitergeld bezog oder an einer Maßnahme nach SGB II/III teilgenommen hat. Mehrfachverlaengerung innerhalb der Gesamtdauer von fünf Jahren zulaessig.
- **Wissenschaftszeitvertragsgesetz (WissZeitVG):** Sondergesetz für Wissenschaft.

## Sachgründe (§ 14 Abs. 1 S. 2 TzBfG)

| Nr. | Sachgrund |
|---|---|
| 1 | Vorübergehender betrieblicher Bedarf |
| 2 | Befristung im Anschluss an Ausbildung/Studium zur Erleichterung des Übergangs |
| 3 | Vertretung anderer Arbeitnehmer (Krankheit, Elternzeit, Mutterschutz) |
| 4 | Eigenart der Arbeitsleistung (z. B. Künstler, Profisport) |
| 5 | Erprobung |
| 6 | In der Person des Arbeitnehmers liegende Gründe |
| 7 | Vergütung aus Haushaltsmitteln, die für eine befristete Beschäftigung bestimmt sind |
| 8 | Gerichtlicher Vergleich |

## Prüfschema

```
1. Schriftform § 14 Abs. 4 TzBfG
 - Originale beider Parteien vor Beschäftigungsbeginn?
2. Verlängerungen oder Neubefristung?
 - Verlängerung iSd § 14 Abs. 2 S. 1 Hs. 2 TzBfG ist nur die nahtlose Anschluss-Befristung ohne inhaltliche Änderung.
3. Sachgrund oder sachgrundlos?
 - Bei sachgrundlos: Vorbeschäftigung prüfen (BAG-Linie post-BVerfG).
 - Bei Sachgrund: Stichhaltigkeit der konkreten Gründe.
4. Höchstdauer
 - § 14 Abs. 2 TzBfG zwei Jahre / drei Verlängerungen.
 - Tarifvertragliche Abweichungen § 14 Abs. 2 S. 3, 4 TzBfG.
5. Klagefrist § 17 TzBfG
 - Drei Wochen ab vereinbartem Ende.
6. Folge bei Unwirksamkeit
 - Arbeitsverhältnis als unbefristet abgeschlossen.
 - Kündigung nur nach KSchG.
```

## Schreibvorlage (Befristungskontrollklage)

```
An das Arbeitsgericht [Ort]
[Anschrift] [Ort, Datum]

In dem Rechtsstreit
[Klagepartei] ./. [Beklagte]
 - wegen Befristungskontrolle -

erheben wir namens und in Vollmacht der Klagepartei

 Befristungskontrollklage

und beantragen,

1. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien nicht aufgrund der Befristung im Arbeitsvertrag vom [Datum] mit Ablauf des [Datum] geendet hat, sondern auf unbestimmte Zeit fortbesteht.
2. Hilfsweise: Es wird festgestellt, dass das Arbeitsverhältnis nicht aufgrund einer auflösenden Bedingung beendet ist.
3. Die Beklagte trägt die Kosten des Rechtsstreits.

Sachverhalt: [Einstellung, Vertragsverlauf, Befristungen, Verlängerungen, ggf. Vorbeschäftigung]

Rechtliche Bewertung:
1. Klagefrist § 17 TzBfG ist gewahrt (vereinbartes Ende: [Datum]).
2. Befristung ist unwirksam, weil [Schriftformverstoß / Vorbeschäftigung / fehlender Sachgrund].
3. Folge: Arbeitsverhältnis besteht unbefristet fort.

[Anwalt, Fachanwalt für Arbeitsrecht]
```

## Übergabe

- Klagefrist § 17 TzBfG **ab vereinbartem Ende** — anders als § 4 KSchG (ab Zugang).
- Bei einvernehmlicher Verlängerung Schriftform peinlich genau wahren (Originale, Unterschriften vor Beginn).
- Zitierweise nach `zitierweise-deutsches-recht` v3.0.

## Aktuelle Rechtsprechung (Stand Mai 2026)

- **BAG, Urteil vom 18.06.2025 - 7 AZR 50/24**: § 14 Abs. 2 TzBfG ist uneingeschraenkt auf Betriebsratsmitglieder anwendbar; eine teleologische Reduktion zur Begruenstigung von Betriebsratsmitgliedern findet nicht statt. Verweigert der Arbeitgeber dem befristet beschaeftigten Betriebsratsmitglied jedoch wegen des Mandats einen Folgevertrag, hat das Mitglied einen Schadensersatzanspruch gerichtet auf Abschluss des verweigerten Folgevertrags (§ 78 BetrVG i.V.m. § 280 BGB). Quelle: dejure.org / luther-lawfirm.com Newsroom; vor Schriftsatzverwendung Volltextpruefung empfohlen.
- Hinweis: Aeltere Leitentscheidungen zur sachgrundlosen Befristung (z.B. BVerfG, Beschl. vom 06.06.2018 - 1 BvL 7/14 u.a., zur Verfassungsmaessigkeit des Vorbeschaeftigungsverbots; BAG-Folgerechtsprechung) bleiben massgeblich; Aktenzeichen vor Zitat ueber dejure.org / openjur.de verifizieren.

## Paragrafenkette

- § 14 Abs. 1 TzBfG — Sachgrundbefristung (Nr. 1-8)
- § 14 Abs. 2 TzBfG — Sachgrundlose Befristung (max. zwei Jahre, drei Verlängerungen)
- § 14 Abs. 2 S. 2 TzBfG — Vorbeschäftigungsverbot
- § 14 Abs. 4 TzBfG i.V.m. § 126 BGB — Schriftformerfordernis
- § 17 TzBfG — Befristungskontrollklage (Frist drei Wochen ab vereinbartem Ende)
- § 16 TzBfG — Rechtsfolge Unwirksamkeit: Arbeitsverhältnis gilt als unbefristet geschlossen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `fachanwalt-arbeitsrecht-bem-verfahren`

**Fokus:** Prüfungslinie für fachanwalt arbeitsrecht bem verfahren: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# BEM-Verfahren § 167 II SGB IX

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `BEM-Verfahren § 167 II SGB IX` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Das Betriebliche Eingliederungs-Management (BEM) ist Pflicht bei mehr als 6 Wochen AU innerhalb eines Jahres. Versäumnis führt fast immer zu **Unwirksamkeit einer personenbedingten Kündigung** (BAG-Linie).

## 1) Eingangs-Abfrage

1. **AU-Dauer im letzten Jahr**: Summenanalyse > 6 Wochen?
2. AU-Grund: einmalig (Unfall) oder chronisch (Rueckenleiden, psychisch)?
3. Schwerbehinderten-Status?
4. Hat AG **BEM-Einladung** ausgesprochen?
5. AN reagiert/teilnahme?
6. Aktueller Zustand: Wiedereingliederung möglich?

## 2) Pflicht des Arbeitgebers § 167 II SGB IX

> "Sind Beschaeftigte innerhalb eines Jahres laenger als sechs Wochen ununterbrochen oder wiederholt arbeitsunfähig, klärt der Arbeitgeber mit der zuständigen Interessenvertretung im Sinne des § 176, bei schwerbehinderten Menschen außerdem mit der Schwerbehindertenvertretung, mit Zustimmung und Beteiligung der betroffenen Person die Möglichkeiten, wie die Arbeitsunfähigkeit möglichst überwunden werden und mit welchen Leistungen oder Hilfen erneuter Arbeitsunfähigkeit vorgebeugt und der Arbeitsplatz erhalten werden kann (betriebliches Eingliederungsmanagement)."

## 3) Wirksamkeit der personenbedingten Kündigung

### BAG-Linie

- **BAG, Urteil vom 20.11.2014 - 2 AZR 755/13**: Der Arbeitgeber traegt die Initiativlast zur Durchfuehrung des BEM (§ 167 Abs. 2 SGB IX); er muss den Arbeitnehmer ueber Ziele, Art und Umfang der zu erhebenden Daten unterrichten. Quelle: dejure.org-Vernetzung BAG 20.11.2014 - 2 AZR 755/13.
- **BAG, Urteil vom 10.12.2009 - 2 AZR 400/08**: BEM ist zwar keine formelle Wirksamkeitsvoraussetzung der Kuendigung, aber faktisch entscheidend; Arbeitgeber ohne BEM hat erhebliche Darlegungslast, dass auch ein BEM die Kuendigung nicht haette verhindern koennen. Quelle: dejure.org-Vernetzung BAG 10.12.2009 - 2 AZR 400/08.
- **BAG, Urteil vom 18.11.2021 - 2 AZR 138/21**: Auch nach abgeschlossenem BEM ist grundsaetzlich ein erneutes BEM durchzufuehren, wenn der Arbeitnehmer innerhalb eines Jahres wieder mehr als 6 Wochen arbeitsunfaehig war. Quelle: dejure.org-Vernetzung.
- **BAG, Urteil vom 15.12.2022 - 2 AZR 162/22**: Die Zustimmung des Integrationsamts zur krankheitsbedingten Kuendigung schwerbehinderter Menschen entbindet den Arbeitgeber nicht von der BEM-Pflicht; sie begruendet auch keine Vermutung, dass ein BEM die Kuendigung nicht haette verhindern koennen. Quelle: dejure.org-Vernetzung BAG 15.12.2022 - 2 AZR 162/22.

### Konsequenz

Ohne BEM = Kündigungsschutzklage **gewinnbar** in 80-90 % der Fälle.

## 4) Ablauf des BEM

### Schritt 1 — Einladung

- AG schreibt AN **schriftlich** an, dass BEM angeboten wird
- Hinweis auf **Freiwilligkeit** der Teilnahme
- Hinweis auf Beteiligung BR/SBV (mit Zustimmung AN)

### Schritt 2 — Erst-Gespräch

- Mit AG, BR/SBV, AN
- Vertraulichkeit
- AN bestimmt, welche AU-Gründe offenbart werden

### Schritt 3 — Maßnahmen-Plan

- Anpassung Arbeitsplatz (Stuhl, Hilfsmittel, Telearbeit)
- Änderung Arbeitszeit (Teilzeit, Schicht)
- Versetzung intern
- Wiedereingliederung **Hamburger Modell** § 74 SGB V iVm § 28 SGB IX

### Schritt 4 — Umsetzung und Evaluation

- Dokumentation
- Nach 6-12 Monaten Review

## 5) Zustimmung Integrationsamt bei Schwerbehinderten § 168 SGB IX

- Bei Schwerbehinderten zwingend **vor Kündigung** Zustimmung Integrationsamt
- Frist Integrationsamt: 1 Monat (Verlängerung möglich)
- Bei Verstoß: Kündigung **nichtig**

## 6) AN-Strategie bei Kündigung trotz fehlendem BEM

### Schritt 1 — Klage binnen 3 Wochen nach Zugang (§ 4 KSchG)

- Verfahrensvermerk: AG hat BEM nicht durchgeführt

### Schritt 2 — Beweisaufnahme

- AG muss darlegen **konkret**, warum BEM aussichtslos war
- BAG-Linie: nicht ausreichend "BEM hätte nichts gebracht"

### Schritt 3 — Verhandlungs-Position

- Bei fehlendem BEM: Vergleichs-Bereitschaft AG hoch
- Abfindung typisch 0,75-1,5 Brutto-Monatsgehaelter pro Beschaeftigungsjahr

## 7) AG-Strategie

### Saubere Dokumentation

- Einladung schriftlich, Zugangs-Nachweis
- AN-Ablehnung schriftlich (Verzicht-Erklärung)
- Bei Teilnahme: Protokoll des Erst-Gesprächs
- Maßnahmen-Plan schriftlich
- Evaluation nach 3-6-12 Monaten

### Bei AN-Ablehnung

- AN muss **schriftlich** verzichten
- AG ist von Pflicht entlastet
- Aber: Pflicht endet nicht bei jedem AU-Fall

## 8) Hamburger Modell — Stufenweise Wiedereingliederung

- Ärztliches Attest mit Stufen-Plan (z.B. 3h, 4h, 6h, 8h)
- AG entscheidet über Teilnahme — kann auch ablehnen
- Lohnzahlung während Wiedereingliederung: typisch keine (Krankengeld bleibt)
- Bei Erfolg: Zurueck zur vollen Arbeitsfähigkeit
- Bei Misserfolg: BEM-Folge-Termin

## 9) Typische Fehler

1. **AG führt BEM gar nicht durch** — Kündigung waekt unwirksam
2. **Einladung ohne Hinweis auf Freiwilligkeit** — formale Pflicht
3. **Bei AN-Ablehnung kein Verzicht-Schriftstück** — Beweisproblem
4. **Schwerbehinderten-Zustimmung Integrationsamt vergessen** — Kündigung nichtig
5. **BEM nur einmalig**, nicht bei wiederholten AU-Fällen — Pflicht-Verletzung

## 10) Honorar

- BEM-Begleitung: pauschal oder Stundensatz
- Kündigungsschutzklage: § 42 II GKG (3 Brutto-Monatsgehaelter Streitwert)
- Vergleich oft mit Abfindungs-Quote

## Anschluss

- `fachanwalt-arbeitsrecht-kuendigungsschutzklage` — bei Klage
- `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit` — bei einvernehmlicher Lösung
- `fachanwalt-sozialrecht-krankengeld-aussteuerung` — bei laufender Krankheit

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BAG, 20.11.2014 - 2 AZR 755/13: Initiativlast und Datenschutz-Unterrichtung. Quelle: dejure.org-Vernetzung.
- BAG, 10.12.2009 - 2 AZR 400/08: Konkretisierung der Darlegungslast bei fehlendem BEM. Quelle: dejure.org-Vernetzung.
- BAG, 18.11.2021 - 2 AZR 138/21: Erneutes BEM bei > 6 Wochen AU im Folgejahr. Quelle: dejure.org-Vernetzung.
- BAG, 15.12.2022 - 2 AZR 162/22: Integrationsamtszustimmung entbindet nicht von BEM-Pflicht; keine Vermutung gegen Verhinderbarkeit. Quelle: dejure.org-Vernetzung.
- Aktuellere Rechtsprechung (Q4/2025 - Q2/2026) zur BEM-Substantiierung in offenen Quellen vor Schriftsatzverwendung pruefen.

## Paragrafenkette

- § 167 Abs. 2 SGB IX — BEM-Pflicht ab sechs Wochen AU
- § 168 SGB IX — Zustimmung Integrationsamt bei Schwerbehinderten
- § 1 Abs. 2 KSchG — personenbedingte Kündigung (Ultima Ratio nach BEM)
- § 84 SGB IX a.F. / § 167 SGB IX n.F. — Wiedereingliederung
- § 69 SGB IX — Feststellung Schwerbehinderung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `fazugang-neu-005-kuendigungsfrist-berechnen-bei-unsicherem-zugan`

**Fokus:** Kündigungsfrist berechnen bei unsicherem Zugangsdatum: frühest- und spätestmöglicher Zugang, Fristberechnung §§ 187 ff. BGB, Drei-Wochen-Klagefrist § 4 KSchG, Kündigungsfristen § 622 BGB, worst-case-Strategie für Mandant.

# Kündigungsfrist berechnen bei unsicherem Zugang

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kündigungsfrist berechnen bei unsicherem Zugang` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Präzise Fristberechnung, wenn das genaue Zugangsdatum der Kündigung unsicher ist — für die Klagefrist (§ 4 KSchG: 3 Wochen) und für die Berechnung der Kündigungsfrist (§ 622 BGB). Worst-Case-Strategie und Sicherheitspolster für die anwaltliche Praxis.

## Einstieg
Wenn ein Sachverhalt vorliegt, zuerst die Zeitachse klären:

1. **Was ist gesichert?** Datum der Kündigung (auf dem Schreiben), Datum der Zustellung (behauptet), Datum der tatsächlichen Kenntnisnahme?
2. **Was ist streitig?** Nur der Zeitpunkt, nur der Inhalt, oder beides?
3. **Wie ist die Fristen-Lage heute?** Wie viele Tage seit dem frühestmöglichen Zugangsdatum?
4. **Hat der Mandant bereits reagiert?** Klageschrift eingereicht? Gegenseite kontaktiert?

## Grundregeln Fristberechnung

### §§ 187–188 BGB — Fristenregeln

**§ 187 BGB:** Ist für den Anfang einer Frist ein Ereignis oder Zeitpunkt maßgebend, so wird bei der Berechnung der Frist der Tag, auf den das Ereignis fällt, nicht mitgerechnet (Fristbeginn am Folgetag).

**§ 188 BGB:** Eine nach Wochen bestimmte Frist endet mit dem Ablauf desjenigen Tages der letzten Woche, welcher durch seine Benennung dem Tag entspricht, in den das Ereignis fällt.

**Beispiel:** Zugang Freitag, 10.01.2025 → 3-Wochen-Frist beginnt am 11.01.2025 → endet am Freitag, 31.01.2025 (Ablauf dieses Tages, also 24:00 Uhr).

**§ 193 BGB:** Fällt das Ende einer Frist auf einen Sonntag, staatlich anerkannten Feiertag oder Sonnabend → Verlängerung auf nächsten Werktag.

## Drei-Wochen-Klagefrist § 4 KSchG

### Berechnung
| Zugang | Fristbeginn (§ 187 BGB) | Fristende (§ 188 BGB) |
|---|---|---|
| Montag | Dienstag | Montag 3 Wochen später (24:00 Uhr) |
| Freitag | Samstag | Freitag 3 Wochen später (24:00 Uhr) |
| Samstag | Sonntag | Samstag 3 Wochen später; wenn Feiertag → § 193 BGB |

### Bei unsicherem Zugangsdatum
**Worst-Case-Strategie für den Arbeitnehmer:**
- Frühestmöglichen Zugangstag als Ausgangspunkt wählen
- Klagefrist ab diesem Datum berechnen
- Klage einreichen, bevor diese Worst-Case-Frist abläuft

**Begründung:** Ist das tatsächliche Zugangsdatum streitig, muss der Anwalt von dem für den Mandanten ungünstigsten Datum ausgehen, um Fristversäumnis zu vermeiden.

## Kündigungsfristen § 622 BGB

### Gesetzliche Mindestkündigungsfristen

| Betriebszugehörigkeit | Kündigungsfrist (AG-Kündigung) |
|---|---|
| 0–2 Jahre | 4 Wochen zum 15. oder Monatsende |
| 2 Jahre | 1 Monat zum Monatsende |
| 5 Jahre | 2 Monate zum Monatsende |
| 8 Jahre | 3 Monate zum Monatsende |
| 10 Jahre | 4 Monate zum Monatsende |
| 12 Jahre | 5 Monate zum Monatsende |
| 15 Jahre | 6 Monate zum Monatsende |
| 20 Jahre | 7 Monate zum Monatsende |

**Berechnung Betriebszugehörigkeit:** Beginn des Arbeitsverhältnisses bis zum Kündigungszugang. Zeiten vor dem 25. Lebensjahr bleiben unberücksichtigt (§ 622 Abs. 2 Satz 2 BGB — verfassungsrechtlich umstritten, EuGH-Vorlage erfolgt). Aktuelle BAG-Linie vor Ausgabe live prüfen.

### Berechnung des Beendigungstermins bei unsicherem Zugang
**Beispiel:**
- Kündigung datiert auf 10.01.2025
- Zugangsdatum streitig: entweder 13.01.2025 (Arbeitgeber) oder 15.01.2025 (Arbeitnehmer)
- Betriebszugehörigkeit: 10 Jahre → 4 Monate Kündigungsfrist zum Monatsende
- Bei Zugang 13.01.2025: 4 Monate zum Monatsende = 31.05.2025
- Bei Zugang 15.01.2025: 4 Monate zum Monatsende = 31.05.2025 (gleich, da beide im Januar)
- Wenn Grenzfall: z.B. Zugang entweder 31.01.2025 oder 01.02.2025 → unterschiedliche Ergebnisse möglich

## Worst-Case-Tabelle: Fristen für den Mandanten sichern

| Situation | Empfehlung |
|---|---|
| Zugangsdatum unklar ± 1-3 Tage | Frühestmögliches Datum annehmen; Klage zügig einreichen |
| Zugangsdatum unklar, Einschreiben nicht abgeholt | Zugang bei persönlicher Abholung annehmen; Botenzustellung parallel beachten |
| Mandant hat 2 Wochen gezögert | Sofortiger Handlungsbedarf; Rest der Frist berechnen |
| Zugang streitig, Arbeitgeber behauptet früheren Zugang | Klage sofort einreichen; im Prozess Zugang bestreiten |

## Fristenkontrollliste

- [ ] Zugangsdatum aus Unterlagen/Mandantenangabe fixiert
- [ ] Worst-Case-Datum für Klagefrist berechnet
- [ ] Klagefrist-Ablauf im Kalender notiert (§ 4 KSchG)
- [ ] Hemmungen/Verlängerungen (§ 193 BGB, Feiertage) geprüft
- [ ] Entfristungsklagefrist (§ 17 TzBfG) geprüft, falls Befristung
- [ ] AGG-Frist (§ 15 Abs. 4 AGG: 2 Monate) geprüft, falls Diskriminierung

## Anschluss-Skills
- `fazugang-neu-001-kuendigung-durch-boten-beweisvermerk-und-prozessstrategie` für Zugangsdokumentation
- `fazugang-neu-003-zugang-bei-urlaub-krankheit-klinik-und-auslandsaufenthalt` für Sonderfälle
- `ar-kuendigungspruefung-workflow` für vollständige Prüfung

## Quellenregel
- Normtext live prüfen auf [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link: [dejure.org](https://dejure.org), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de).
- Keine modellwissensbasierten Fristen ohne Verifikation.
- Annahmen explizit kennzeichnen.

## Was dieser Arbeitsgang nicht macht
- Keine automatisierte Fristenberechnung; Einzelfallprüfung bleibt notwendig.
- Keine Berücksichtigung abweichender tariflicher oder vertraglicher Fristen ohne konkrete Vorlage.
