---
name: stb-jahresgespraech-mandant-ki-tools-lohn
description: "STB Jahresgespraech Mandant KI Tools Lohn: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STB Jahresgespraech Mandant KI Tools Lohn

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **STB Jahresgespraech Mandant KI Tools Lohn** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-jahresgespraech-mandant-bwa-basis` | Jahresgespraech Mandant auf BWA-Basis. Anwendungsfall jaehrliches Bilanzgespraech nach Jahresabschluss-Erstellung Gesamtjahresblick Mehrjahres-Trend Strategie Folgejahr. Methodik intensive Vorbereitung 2-3 Stunden Termin Dokumentation. Output Gespraechs-Protokoll Strategiepapier. |
| `stb-ki-tools-im-stb-betrieb-grenzen-berufsrecht` | KI-Tools im StB-Betrieb Berufsrechtliche Grenzen § 57 StBerG. Anwendungsfall ChatGPT Claude Microsoft Copilot Datev-KI Nutzung Mandantenkommunikation Berufsverschwiegenheit. Methodik Prüfung Compliance KI-VO Prüfraster. Output KI-Richtlinie Kanzlei. |
| `stb-lohn-arbeitgeber-arbeitnehmer-anteile` | Arbeitgeber- und Arbeitnehmer-Anteile in der SV. Anwendungsfall Verteilung der SV-Beitraege zwischen AG und AN PV-Zuschlag Kinderlose KV-Zusatzbeitrag Sonderbeitraege Lohnabrechnung. Methodik AG-AN-Aufteilung in DATEV LODAS. Output Lohnabrechnung mit korrekter Aufteilung. |
| `stb-lohn-aufzeichnungspflichten-milog` | Aufzeichnungspflichten nach MiLoG § 17 für Mindestlohn-relevante Branchen Geringfuegige Beschaeftigung. Anwendungsfall Prüfung Aufzeichnungspflicht 2 Jahre Aufbewahrung Schwarzarbeitsbekaempfung. Methodik Form der Aufzeichnung digitale Lösungen. Output Aufzeichnungssystem Mandanten-Notiz. |
| `stb-lohn-bav-doppelversorgung-foerderung` | bAV bei mehreren Durchführungswegen Doppelversorgung Foerderung. Anwendungsfall AN hat Direktversicherung und Pensionskasse Beitragsobergrenzen gemeinsame Prüfung Hoechstforderung. Methodik kumulierte 8-Prozent-Prüfung. Output bAV-Prüfnotiz. |
| `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende` | Berufsgenossenschaft Lohnnachweis Jahresende. Anwendungsfall jaehrlicher Lohnnachweis an die zuständige BG Vorauszahlung BG-Beitrag Schluesseldaten Gefahrtarif. Methodik elektronischer Lohnnachweis über sv.net oder DAKOTA. Output BG-Lohnnachweis Beitragsbescheid. |
| `stb-lohn-betriebsausfluege-aufmerksamkeiten-60-euro` | Aufmerksamkeiten 60 EUR-Freigrenze pro persoenlichem Anlass. Anwendungsfall Sachgeschenk zu Geburtstag Hochzeit Jubilaeum 60 EUR Hoechstwert LSt-frei. Methodik Abgrenzung zur 50 EUR-Sachbezugs-Freigrenze. Output korrekte Lohn-Behandlung Aufmerksamkeit. |
| `stb-lohn-betriebsveranstaltung-110-euro-freibetrag` | Betriebsveranstaltung 110 EUR-Freibetrag § 19 Abs 1 Nr 1a EStG. Anwendungsfall Firmenfeier Sommerfest Weihnachtsfeier Kostenkalkulation 110 EUR pro AN Pauschalierung. Methodik Berechnung Prüfung Belege. Output Lohn-Abrechnung mit Betriebsveranstaltung. |
| `stb-lohn-gesellschafter-geschaeftsfuehrer-sv` | Gesellschafter-Geschäftsführer GGF SV-Pflicht oder SV-Befreiung. Anwendungsfall Prüfung GGF einer GmbH ob abhaengig beschaeftigt oder selbständig tätig Statusfeststellung. Methodik Kriterienkatalog Beteiligung Weisungsgebundenheit Sperrminoritaet. Output Statusfeststellungs-Antrag Bescheid Mandanten-Notiz. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **STB Jahresgespraech Mandant KI Tools Lohn**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-jahresgespraech-mandant-bwa-basis`

**Fokus:** Jahresgespraech Mandant auf BWA-Basis. Anwendungsfall jaehrliches Bilanzgespraech nach Jahresabschluss-Erstellung Gesamtjahresblick Mehrjahres-Trend Strategie Folgejahr. Methodik intensive Vorbereitung 2-3 Stunden Termin Dokumentation. Output Gespraechs-Protokoll Strategiepapier.

# Jahresgespraech mit dem Mandanten

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Jahresgespraech mit dem Mandanten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Das Jahresgespraech ist die wichtigste Mandantenkommunikation des Jahres: Nach Abschluss des Jahresabschlusses (idR im Fruehjahr) trifft sich der Steuerberater mit dem Mandanten zu einem 2-3-stuendigen Bilanzgespraech. Themen: Jahresergebnis, Mehrjahres-Trend, steuerliche Themen, Strategie Folgejahr. Bei groesseren Mandanten oft mit Berufstraeger plus Sachbearbeiter, beim Mandanten GF plus Aufsichtsrat/Gesellschafter.

## Kaltstart-Rueckfragen

1. Ist Jahresabschluss endgueltig fertig?
2. Welche wesentlichen Ergebnisse / Auffaelligkeiten?
3. Welche Mehrjahres-Trends ablesbar?
4. Welche steuerlichen Optimierungen anstehend?
5. Welche Strategie-Themen vom Mandanten gewuenscht?
6. Wer nimmt teil (auf beiden Seiten)?
7. Welche Dokumente werden vorgelegt?
8. Welche Eskalations-Themen (Krisensignale)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 102 StaRUG** — Hinweispflicht.

**§ 5 RDG** — Abgrenzung Rechtsberatung.

## Workflow

### Phase 1 — Vorbereitung (2 Wochen)

- Jahres-BWA, Jahres-SuSa, Bilanz, GuV aufbereiten.
- Mehrjahres-Trend-Grafiken.
- Branchenvergleich (BBE).
- Steuerliche Themen sammeln.
- Strategie-Praesentation.
- Agenda an Mandant 1 Woche vorher.

### Phase 2 — Standard-Agenda Jahresgespraech

```
JAHRESGESPRAECH AGENDA
Mandant: [Firma] [Geschaeftsjahr]
Termin: [Datum]
Dauer: 2-3 Stunden

1. JAHR IN ZAHLEN (30 Min)
 - Umsatz, EBIT, Jahresueberschuss
 - Vorjahresvergleich
 - Mehrjahres-Trend
 - Branchenvergleich

2. BILANZ (20 Min)
 - Eigenkapital-Entwicklung
 - Liquiditaet
 - Anlagendeckung
 - Sondervorgaenge

3. STEUERN (30 Min)
 - Steuerbelastung im Jahr
 - Vorauszahlungen Folgejahr
 - Steuerliche Optimierungen
 - Investitionsabzugsbetrag § 7g EStG
 - Sonder-AfA-Optionen

4. PERSONAL (15 Min)
 - Personalentwicklung
 - Lohnkostenquote
 - Sondervergueteungs-Planung
 - SV-Themen

5. STRATEGIE FOLGEJAHR (30 Min)
 - Umsatz- und Ergebnis-Plan
 - Investitionsplan
 - Finanzierung
 - Eigenkapital-Verstaerkung

6. RISIKEN UND ESKALATIONEN (10 Min)
 - Krisensignale
 - § 102 StaRUG-Hinweise
 - Anhaengige Pruefungen
```

### Phase 3 — Gespraechsfuehrung

- Strukturiert, aber dialogisch.
- Bei wesentlichen Themen Mandanten aktiv einbeziehen.
- Bei Krisensignalen explizit warnen.
- Anwaltliche Themen NICHT selbst beraten (§ 5 RDG).

### Phase 4 — Bei groesseren Mandanten

- Berufstraeger + Sachbearbeiter.
- Bei Konzern: konsolidierte Daten.
- Bei Investor-Mandant: separate Investor-Update-Sitzung.

### Phase 5 — Dokumentation (1 Woche)

- Detailliertes Protokoll.
- Strategiepapier mit Folgejahr-Massnahmen.
- Wiedervorlage.

### Phase 6 — Nachfolge

- Verbindlichkeit der Vereinbarungen.
- Bei wesentlichen strategischen Entscheidungen: schriftliche Bestaetigung.

## Output

- Gespraechs-Protokoll.
- Strategiepapier Folgejahr.
- Massnahmen-Liste.
- Wiedervorlage in DATEV-Kanzleiplaner.

## Strategie und Praxis-Tipps

- Jahresgespraech ist Mandantenbindungs-Hoehepunkt — gut investierte Zeit.
- 2-3 Stunden mindestens — kuerzere Gespraeche bringen zu wenig Tiefe.
- Bei Krisensignalen: schriftliche Bestaetigung der ausgesprochenen Warnung.
- Bei mehreren Generationen Familien-GmbH: alle Generationen einladen.
- StBVV: Jahresgespraech in Pauschalvereinbarung oder separates Beratungshonorar.

## Querverweise

- `stb-bwa-jahres-bwa-erstellen` — Jahres-BWA.
- `stb-bwa-mandantengespraech-uebergabe` — BWA-Uebergabe.
- `stb-mandantenkommunikation-bwa-uebergabe-quartal` — Quartalsgespraech.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- StaRUG § 102.
- RDG § 5.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-ki-tools-im-stb-betrieb-grenzen-berufsrecht`

**Fokus:** KI-Tools im StB-Betrieb Berufsrechtliche Grenzen § 57 StBerG. Anwendungsfall ChatGPT Claude Microsoft Copilot Datev-KI Nutzung Mandantenkommunikation Berufsverschwiegenheit. Methodik Prüfung Compliance KI-VO Prüfraster. Output KI-Richtlinie Kanzlei.

# KI-Tools im StB-Betrieb — Berufsrechtliche Grenzen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KI-Tools im StB-Betrieb — Berufsrechtliche Grenzen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

KI-Tools wie ChatGPT, Claude, Microsoft 365 Copilot oder DATEV-KI veraendern auch die StB-Kanzlei: Textgenerierung, Recherche, Belegklassifizierung, Pruef-Assistenten. Berufsrechtliche Pflichten: Berufsverschwiegenheit nach § 57 Abs. 1 StBerG, strafrechtlich abgesichert durch § 203 Abs. 1 Nr. 3 StGB, ergaenzt durch die DSGVO. § 203 Abs. 3 S. 2 StGB erlaubt die Einbeziehung "mitwirkender Personen" (umfasst auch externe Dienstleister wie KI-Anbieter) nur unter strikten Voraussetzungen — insbesondere schriftliche Verpflichtung zur Verschwiegenheit. Zusaetzlich gilt seit 01.08.2024 die EU-KI-Verordnung (VO 2024/1689) mit gestaffelter Anwendung; allgemeine Pflichten und Verbote ab 02.02.2025, Vorschriften fuer General Purpose AI ab 02.08.2025, Vollanwendung fuer Hochrisiko-KI im Wesentlichen ab 02.08.2026.

## Kaltstart-Rueckfragen

1. Welche KI-Tools werden bereits genutzt?
2. Werden Mandantendaten verarbeitet?
3. Liegt AVV mit KI-Anbieter vor?
4. Wo liegt Server (EU, USA)?
5. Wird KI-Output zur Mandantenberatung verwendet?
6. Welche Schulung Sachbearbeiter?
7. Welche Risikoeinstufung KI-VO?
8. Welche Mandantenkommunikation zur KI-Nutzung?

## Rechtlicher Rahmen

### Primaernormen

**§ 57 Abs. 1 StBerG** — Berufsverschwiegenheit.

**§ 62 StBerG** — Mitwirkende Personen (Schweigepflicht-Erstreckung).

**§ 203 Abs. 1 Nr. 3 StGB** — Verletzung von Privatgeheimnissen (Tatbestand).

**§ 203 Abs. 3, 4 StGB** — Einbeziehung mitwirkender Personen / externer Dienstleister; Schriftform-Verpflichtung.

**DSGVO Art. 5, 28, 32, 44 ff.** — Grundsaetze, Auftragsverarbeitung, Sicherheit, Drittlandtransfer.

**EU-KI-VO (VO 2024/1689)** — Risikobasierter Regelungsrahmen, gestaffelte Anwendung 02.02.2025 / 02.08.2025 / 02.08.2026 / 02.08.2027.

**§ 5 RDG** — Abgrenzung Rechtsdienstleistung.

### Verwaltungsanweisungen

- BStBK-Hinweise zur KI.
- DStV-Praxisleitfaden.

## Workflow

### Phase 1 — KI-Tool-Inventar

| Tool | Verwendung | Mandantendaten? | AVV |
|---|---|---|---|
| ChatGPT (OpenAI) | Recherche, Text | Achtung | Pruefen |
| Claude (Anthropic) | Recherche, Text | Achtung | Pruefen |
| Microsoft 365 Copilot | Office | Ja | Ja |
| DATEV-KI | Lohn, Buchhaltung | Ja | Ja (DATEV-AVV) |
| Whisper / Speech-to-Text | Diktat | Achtung | Pruefen |

### Phase 2 — Berufsverschwiegenheits-Pruefung

- § 57 StBerG: Mandantendaten duerfen nicht weitergegeben werden.
- Bei KI-Tool ohne Berufsgeheimnistraeger-Klausel: Mandantendaten anonymisieren.
- Spezielle "Business-Versionen" mit kein Trainingsversprechen sicherer.

### Phase 3 — KI-VO Risikoeinstufung (VO 2024/1689)

| Risiko | Anwendung (Beispiele) |
|---|---|
| Unzulaessig (Art. 5) | Social Scoring durch Behoerden; biometrische Echtzeit-Fernidentifizierung im oeffentlichen Raum (mit Ausnahmen) |
| Hochrisiko (Anhang III) | KI in kritischer Infrastruktur, Bildung, Beschaeftigungs-Auswahl, kritische Rechtspflege-Anwendungen |
| Begrenztes Risiko | Chatbots, Deepfake-Generatoren — Transparenz-/Kennzeichnungspflichten Art. 50 |
| Minimales Risiko | Standard-Office-KI, KI in Buchhaltungs-Klassifikation, Recherche-Assistenten |

StB-typische KI-Nutzung (Recherche, Textgenerierung, Buchungsvorschlaege) ist regelmaessig "minimal" oder "begrenzt"; sie wird **nicht** allein durch die Mandantenbezogenheit zur Hochrisiko-KI. Hochrisiko liegt erst dann vor, wenn die KI zu einer "Kreditwuerdigkeit"-Bewertung oder zu Hochrisiko-Anwendungen iSv Anhang III VO 2024/1689 eingesetzt wird.

### Phase 4 — Sachbearbeiter-Schulung

- Welche Daten duerfen NICHT in KI?
- Mandantendaten, Personenbezogene Daten anonymisieren.
- Output kritisch pruefen (Halluzinationen).

### Phase 5 — Mandantenkommunikation

- KI-Nutzung im Datenschutzhinweis transparent.
- Bei Beratungsleistung: AN bleibt verantwortlich, nicht KI.

### Phase 6 — Output-Verantwortung

- KI-Output durch Sachbearbeiter pruefen.
- Bei Halluzinationen: Falschberatungs-Risiko.
- Bei rechtlichen Aspekten: § 5 RDG — KI darf nicht Rechtsberatung ersetzen.

## Output

- KI-Tool-Inventar mit Berufsrecht-Pruefung.
- KI-Richtlinie Kanzlei.
- Sachbearbeiter-Schulungs-Dokumentation.

## Strategie und Praxis-Tipps

- KI ist Produktivitaetshebel fuer Routine-Texte, Recherche, Beleg-Klassifikation; sie ersetzt aber keine berufsrechtlich verantwortete Pruefung durch den Berufstraeger.
- Mandantendaten gelangen nur in KI-Loesungen mit nachweisbarem AVV, dokumentiertem Hosting (EU-Praeferenz) und schriftlicher Verschwiegenheitsverpflichtung nach § 203 Abs. 4 StGB i.V.m. § 62 StBerG (z.B. DATEV-KI, Microsoft 365 Copilot Enterprise mit EU Data Boundary).
- Bei ChatGPT/Claude in Konsumfassung: Mandantendaten zwingend anonymisieren / pseudonymisieren; Trainings-Opt-Out aktivieren; bei Geschaeftskonten mit AVV (z.B. ChatGPT Enterprise, Claude for Work) sind die Anforderungen erfuellbar, jeweils Vertragsstand pruefen.
- Berufsverschwiegenheit ist strafrechtlich abgesichert (§ 203 StGB) — jeder Verstoss ist Offizialdelikt; zusaetzlich drohen DSGVO-Bussgelder bis 4 % Jahresumsatz.
- KI-VO-Compliance: Bis 02.02.2025 verbotene Praktiken vermeiden; Schulung der Sachbearbeiter zur Output-Kontrolle (Halluzinationsrisiko); ab 02.08.2026 Pruefung der eingesetzten KI auf Hochrisiko-Einstufung.
- Output-Verantwortung verbleibt beim Berufstraeger: jede inhaltliche Aussage ist vor Mandantenkommunikation durch den Berufstraeger zu pruefen (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang).

## Querverweise

- `stb-datentransfer-mandant-cloud-dsgvo` — DSGVO.
- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-mandantenanfrage-reaktion-frist-laufend` — Reaktionsfristen.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 57, 62.
- StGB § 203 Abs. 1 Nr. 3, Abs. 3, Abs. 4.
- DSGVO Art. 5, 28, 32, 44 ff.
- EU-KI-VO 2024/1689 (BGBl. EU L vom 12.07.2024).
- RDG § 5.
- BStBK-/DStV-Hinweise zur KI-Nutzung.
- Hinweis: KI-VO Anwendungsstufen — verbotene Praktiken ab 02.02.2025, General Purpose AI ab 02.08.2025, Hochrisiko-KI-Pflichten im Wesentlichen ab 02.08.2026; delegierte Rechtsakte laufend ueber eur-lex.europa.eu abrufen.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 2 ersetzt (Output-Verantwortungs-Satz ohne Marker neu formuliert; KI-VO-Anwendungsstufen mit konkreten Daten aus VO 2024/1689 belegt) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-lohn-arbeitgeber-arbeitnehmer-anteile`

**Fokus:** Arbeitgeber- und Arbeitnehmer-Anteile in der SV. Anwendungsfall Verteilung der SV-Beitraege zwischen AG und AN PV-Zuschlag Kinderlose KV-Zusatzbeitrag Sonderbeitraege Lohnabrechnung. Methodik AG-AN-Aufteilung in DATEV LODAS. Output Lohnabrechnung mit korrekter Aufteilung.

# AG-/AN-Anteile in der Sozialversicherung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AG-/AN-Anteile in der Sozialversicherung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die SV-Beitraege werden grundsaetzlich paritaetisch zwischen AG und AN aufgeteilt. Es gibt aber Sonderregelungen: PV-Kinderlosenzuschlag (AN allein), U1/U2-Umlagen (AG allein), Insolvenzgeld-Umlage (AG allein), Berufsgenossenschaft (AG allein), Sachsen-PV-Sonderregelung. Der Steuerberater konfiguriert die Aufteilung im DATEV LODAS / Lohn und Gehalt korrekt.

## Kaltstart-Rueckfragen

1. Welcher Mandant — Standardfall oder Sonderkonstellation?
2. Welche AN-Konstellation (Kinder, Bundesland)?
3. Welche Krankenkassen — Zusatzbeitragssatz individuell?
4. Welche Umlage-Pflichten — U1 (Kleinunternehmer), U2, Insolvenzgeld?
5. Berufsgenossenschaft mit welchem Beitrag?
6. Sondersituation Sachsen-PV?
7. Welche Sonderbeitraege (z.B. zusaetzliche BG)?
8. Welche tarifliche Sonderregelungen?

## Rechtlicher Rahmen

### Primaernormen

**§ 249 SGB V** — KV-Beitragsverteilung.

**§ 168 SGB VI** — RV-Beitragsverteilung.

**§ 346 SGB III** — AV-Beitragsverteilung.

**§ 58 SGB XI** — PV-Beitragsverteilung; § 55 Abs. 3 SGB XI PV-Zuschlag Kinderlose.

**AAG** — U1/U2-Umlage.

**§ 358 SGB III** — Insolvenzgeld-Umlage (Beitrag AG).

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.

## Workflow

### Phase 1 — Standard-Aufteilung

| Zweig | AG-Anteil (typisch derzeit ca.) | AN-Anteil (typisch derzeit ca.) |
|---|---|---|
| KV allgemein | 7,3 Prozent | 7,3 Prozent |
| KV-Zusatzbeitrag (KK-individuell) | halftig (paritaetisch seit 01.01.2019) | halftig |
| PV (allgemein, ausserhalb Sachsen) | halftig | halftig |
| PV-Zuschlag Kinderlose ab Vollendung des 23. Lj. | 0 | 0,6 Prozent allein zu Lasten AN (Stand 2025; § 55 Abs. 3 SGB XI i.d.F. PflegeunterstuetzungsG gueltig seit 01.07.2023; jaehrlich ueber GKV-Spitzenverband pruefen) |
| PV-Abschlag mit Kindern (PUEG ab 01.07.2023) | nicht beruehrt | gestaffelter Abschlag fuer AN je Kind ab 2. Kind (0,25 Prozent/Kind), bis maximal 5 Kinder (max. 1,0 Prozent Abschlag); § 55 Abs. 3 SGB XI (Stand 2025; bei kuenftigen Anpassungen GKV-Spitzenverband pruefen) |
| PV Sachsen (Buss- und Bettag) | typisch geringer AG-Anteil; AN traegt zusaetzliche 0,5 Prozent (§ 58 Abs. 3 SGB XI) | typisch hoeherer AN-Anteil |
| RV | 9,3 Prozent | 9,3 Prozent (gesamt 18,6 Prozent — Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen) |
| AV | 1,3 Prozent je Seite (gesamt 2,6 Prozent — Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen) | wie AG |
| U1 (Kleinunternehmer bis 30 AN) | voll AG | 0 |
| U2 (Mutterschaft, alle AG) | voll AG | 0 |
| Insolvenzgeld-Umlage | voll AG | 0 |
| Berufsgenossenschaft | voll AG | 0 |

(Saemtliche Beitragssaetze Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel ueber DRV, BMAS, GKV-Spitzenverband sowie KK-individuelle Zusatzbeitragssatzungen pruefen.)

### Phase 2 — PV-Kinderlosenzuschlag

- AN ohne Kinder ab 23 Jahre: zusaetzlicher Anteil 0,6 Prozent (Stand 2025, § 55 Abs. 3 SGB XI; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen).
- AN mit Kindern: Abschlag oder Wegfall des Zuschlags.
- Bei mehreren Kindern: gestaffelter Abschlag (Reform 2023 nachgelagert).

### Phase 3 — Sachsen-PV-Sonderregelung

- Sachsen-PV: AN-Anteil hoeher als AG-Anteil (anders als anderswo).
- DATEV LODAS-Stammdaten: Bundesland-Schluessel "Sachsen".

### Phase 4 — KV-Zusatzbeitragssatz

- Jede Krankenkasse erhebt individuellen Zusatzbeitrag.
- Standard-Zusatzbeitragssatz (BMAS-Statistik) durchschnittlich 2,5 Prozent (Stand 2025; Wert 2026 ueber GKV-Spitzenverband pruefen — KK-individuell).
- Bei KK-Wechsel: Umstellung im Lohn-Programm.

### Phase 5 — Umlagen U1/U2

- U1 (Krankheit): nur Kleinunternehmer (bis 30 AN) pflichtig.
- U2 (Mutterschaft): alle AG pflichtig.
- Insolvenzgeld-Umlage: alle AG pflichtig (Ausnahme: Privathaushalte).

### Phase 6 — DATEV LODAS-Konfiguration

- Mandantenstammdaten: Bundesland, BG-Schluessel, U1-Pflicht.
- AN-Stammdaten: Kinderlosen-Status, KK-Wahl.
- Automatische Berechnung der Anteile.

## Output

- Korrekt aufgeteilte SV-Beitraege.
- Lohnabrechnung mit AG- und AN-Anteilen.
- Buchung im Hauptbuch (AG-Anteile als Lohnnebenkosten).

## Strategie und Praxis-Tipps

- PV-Kinderlosenzuschlag und Sachsen-PV sind haeufige Fehlerquellen — sorgfaeltig konfigurieren.
- KV-Zusatzbeitrag KK-individuell — bei KK-Wechsel des AN sofort anpassen.
- BG-Mitgliedschaft regelmaessig aktualisieren (Gefahrtarif-Aenderungen).
- StBVV: Standardkonfiguration in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS automatische Beitragssatz-Aktualisierung zum Jahresbeginn.

## Querverweise

- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-umlage-u1-u2-insogeld-umlage` — Umlagen.
- `stb-lohn-mandantenaufnahme-onboarding` — Onboarding.
- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.

## Quellen und Updates

Stand: 05/2026.

- SGB V § 249.
- SGB VI § 168.
- SGB III §§ 346, 358.
- SGB XI §§ 55, 58.
- AAG.
- Beitragssaetze Stand 2025: RV 18,6 Prozent, AV 2,6 Prozent, KV allgemein 14,6 Prozent + KK-Zusatzbeitrag (durchschnittlich 2,5 Prozent), PV 3,6 Prozent (Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen).
- PV-Kinderlosenzuschlag 2025: 0,6 Prozent (§ 55 Abs. 3 SGB XI; Sozialversicherungs-Rechengroessenverordnung 2026 pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 9 Marker aufgeloest: 7 bestaetigt (Fundstelle/Datum), 2 ersetzt (neu formuliert ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-lohn-aufzeichnungspflichten-milog`

**Fokus:** Aufzeichnungspflichten nach MiLoG § 17 für Mindestlohn-relevante Branchen Geringfuegige Beschaeftigung. Anwendungsfall Prüfung Aufzeichnungspflicht 2 Jahre Aufbewahrung Schwarzarbeitsbekaempfung. Methodik Form der Aufzeichnung digitale Lösungen. Output Aufzeichnungssystem Mandanten-Notiz.

# Aufzeichnungspflichten nach MiLoG § 17

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aufzeichnungspflichten nach MiLoG § 17` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Aufzeichnungspflicht der taeglichen Arbeitszeit (Beginn, Ende, Dauer) trifft Arbeitgeber in bestimmten Branchen (§ 17 MiLoG i.V.m. SchwarzArbG) sowie alle Minijob-Verhaeltnisse. Form: schriftlich, papierfest oder digital, spaetestens am 7. Folgetag. Aufbewahrungsfrist: 2 Jahre. Verstoesse: Bussgeld bis 30.000 EUR. Sonderfall: BAG zur EuGH-Rechtsprechung verlangt allgemeine Arbeitszeit-Erfassung.

## Kaltstart-Rueckfragen

1. Welche Branche — § 2a SchwarzArbG-relevant (Bau, Gaststaette, Personenbefoerderung, Reinigung, Fleisch, Forst, Spedition, Sicherheit, Messebau, ...)?
2. Liegen Minijobs vor?
3. Welche Erfassungsform aktuell — Papier, Excel, digital?
4. Werden taegliche Anfang/Ende/Dauer aufgezeichnet?
5. Werden Pausen erfasst?
6. Wer hat Aufzeichnungs-Verantwortung (Mandant oder StB)?
7. Welche Pruefung durch Zoll-Hauptzollamt schon erfolgt?
8. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtlicher Rahmen

### Primaernormen

**§ 17 MiLoG** — Aufzeichnungspflicht.

**§ 2a SchwarzArbG** — Liste der besonders pruefungsrelevanten Branchen.

**§ 16 ArbZG** — Aufzeichnungspflicht Mehrarbeit allgemein.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

(Aktenzeichen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen.)

## Workflow

### Phase 1 — Geltungsbereich

| Geltung | Aufzeichnungspflicht |
|---|---|
| § 2a SchwarzArbG-Branchen | Strenge MiLoG-Pflicht |
| Minijobs (alle Branchen) | Strenge MiLoG-Pflicht |
| Sonstige AN | Allgemeine Arbeitszeit-Erfassung (EuGH/BAG) |

### Phase 2 — Aufzeichnungs-Inhalt

- Beginn der taeglichen Arbeitszeit.
- Ende der taeglichen Arbeitszeit.
- Dauer (netto, ohne Pausen).
- Datum.
- Identifizierbarer AN (Name/Personalnr).
- Ggf. Pausen.

### Phase 3 — Form

- Schriftlich: Papier, Stundenzettel.
- Digital: Excel, Stempeluhr, Zeiterfassungssoftware.
- Manipulationssicher: Excel umstritten (manipulierbar); zertifizierte Systeme bevorzugt.
- BAG verlangt grundsaetzlich objektive, verlaessliche, zugaengliche Aufzeichnung.

### Phase 4 — Aufbewahrung

- 2 Jahre nach Aufzeichnung.
- Bei Zoll-Pruefung Vorlagepflicht innerhalb gesetzter Frist.

### Phase 5 — Bussgelder

- § 21 Abs. 1 Nr. 7 i.V.m. Abs. 3 MiLoG: Bussgeld bis 30.000 EUR bei fehlender oder fehlerhafter Aufzeichnung.
- § 21 Abs. 1 Nr. 9 i.V.m. Abs. 3 MiLoG: bis 500.000 EUR bei Mindestlohn-Verstoss.
- Bei vorsaetzlicher Schwarzarbeit zusaetzlich § 266a StGB-Risiko.

### Phase 6 — Beratung Mandant

- Mandant ueber EuGH-/BAG-Rechtsprechung informieren — auch ausserhalb § 2a-Branchen relevant.
- Empfehlung Zeiterfassungssystem (Software z.B. ZEUS, AVERO, Pliam).
- Bei Vertrauensarbeitszeit: Aufzeichnungspflicht bleibt; alternative Erfassung moeglich.

## Output

- Mandanten-Notiz zu Aufzeichnungspflichten.
- Empfehlung Zeiterfassungssystem.
- Aufbewahrungs-Routine.

## Strategie und Praxis-Tipps

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Sondersituation Aussendienst, Home-Office: Aufzeichnung am Ort der Taetigkeit.
- Bei Pruefung durch Zoll: Vorlage in Deutsch in Originalform oder beglaubigter Uebersetzung.
- Bei Minijob: Aufzeichnung ist zentrale Pruefungsstelle der Pruefer.
- StBVV: Beratung Aufzeichnungspflichten Zusatzauftrag.
- DATEV-Tipp: DATEV-Zeitwirtschaft als Modul; Schnittstelle zu LODAS.

## Querverweise

- `stb-lohn-mehrarbeit-zuschlaege-39b-estg` — Zuschlaege.
- `stb-lohn-mindestlohn-aktuell-2026-anpassung` — Mindestlohn.
- `stb-lohn-minijob-538-euro-2024-anpassung` — Minijob.
- `stb-lohn-ueberstunden-abbau-arbeitszeitkonto` — Arbeitszeitkonto.

## Quellen und Updates

Stand: 05/2026.

- MiLoG §§ 17, 21.
- SchwarzArbG § 2a.
- ArbZG § 16.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (Pruefungshinweis neu formuliert ohne Marker) -->

## 5. `stb-lohn-bav-doppelversorgung-foerderung`

**Fokus:** bAV bei mehreren Durchführungswegen Doppelversorgung Foerderung. Anwendungsfall AN hat Direktversicherung und Pensionskasse Beitragsobergrenzen gemeinsame Prüfung Hoechstforderung. Methodik kumulierte 8-Prozent-Prüfung. Output bAV-Prüfnotiz.

# bAV bei mehreren Durchfuehrungswegen — Doppelversorgung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `bAV bei mehreren Durchfuehrungswegen — Doppelversorgung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Hat ein AN mehrere bAV-Vertraege (z.B. Direktversicherung und Pensionskasse), greift die 8-Prozent-BBG-Foerderung nach § 3 Nr. 63 EStG nur einmal kumuliert. Werden die Beitraege beider Wege zusammengezaehlt, ueberschreiten sie ggf. die Freibetragsgrenze — der ueberschiessende Teil ist voll versteuert. Der Steuerberater muss die Beitragssummen pruefen und ggf. anpassen.

## Kaltstart-Rueckfragen

1. Welche bAV-Vertraege hat der AN — Direktversicherung, Pensionskasse, Pensionsfonds?
2. Welche Beitragshoehe je Vertrag pro Monat?
3. Wann wurden die Vertraege abgeschlossen?
4. Sind alle Vertraege beim aktuellen AG?
5. Hat der AN aus frueheren AG-Verhaeltnis weiter laufende bAV?
6. Welche Direktzusagen (steuerlich anders)?
7. Welche steuerliche Praxis der Vorperioden (bisher LSt-frei abgerechnet)?
8. Was ist Wunsch des AN — voll foerdern oder Beitrag aufteilen?

## Rechtlicher Rahmen

### Primaernormen

**§ 3 Nr. 63 EStG** — Steuerfreiheit kumulative 8-Prozent-Grenze.

**§ 1a BetrAVG** — Entgeltumwandlung; 15-Prozent-AG-Zuschuss-Pflicht.

**§ 1 Abs. 1 Nr. 9 SvEV** — SV-Freiheit bAV-Beitraege bis 4 Prozent BBG-West RV (kumuliert ueber alle Durchfuehrungswege).

### Verwaltungsanweisungen

- BMF v. 06.12.2017 (BRSG-Umsetzung, IV C 5 - S 2333/17/10002).
- BMF v. 18.03.2022 (aktualisierte Auslegungshinweise bAV, IV C 5 - S 2333/19/10005); aktuelles BMF-Schreiben zur bAV-Foerderung ueber BMF-Internet abrufen.

## Workflow

### Phase 1 — Vertragsuebersicht

| Vertrag | Beitrag/Monat | Beitrag/Jahr | Beginn | Vertragspartner |
|---|---|---|---|---|
| Direktversicherung X | [Y EUR] | [Y*12] | [Datum] | [Versicherer] |
| Pensionskasse Y | [Y EUR] | [Y*12] | [Datum] | [Pensionskasse] |
| Summe | [Z EUR] | [Z*12] | | |

### Phase 2 — 8-Prozent-Pruefung

- Gesamtbeitrag in Direktversicherung + Pensionskasse + Pensionsfonds gemeinsam: bis 8 Prozent BBG (West) LSt-frei.
- Daruber hinaus voll lohnsteuerpflichtig.
- 4-Prozent-BBG-Grenze fuer SV-Freiheit auch kumulativ.
- **Zahlenbeispiel (Stand 2025):** AN hat Direktversicherung 250 EUR/Monat und Pensionskasse 200 EUR/Monat = 450 EUR/Monat = 5.400 EUR/Jahr. 8 Prozent BBG-West RV 2025 (96.600 EUR) = 7.728 EUR; voll LSt-frei. 4 Prozent BBG = 3.864 EUR; davon SV-frei. Differenz 5.400 - 3.864 = 1.536 EUR/Jahr SV-pflichtig (auch wenn LSt-frei). BBG-West RV 2026 ueber Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen.

### Phase 3 — Bei Ueberschreitung

- Ueberschiessender Beitrag: voll LSt-pflichtig.
- Optionen:
 - Beitrag reduzieren (in einem Vertrag).
 - Ueberschuss versteuern (Mandant akzeptiert).
 - Beitrag in Direktzusage umwandeln (kein § 3 Nr. 63 EStG-Limit, aber andere Behandlung).

### Phase 4 — Altvertraege § 40b EStG a.F.

- Direktversicherungen vor 2005 mit Pauschalbesteuerung 20 Prozent.
- Pauschalbeitraege werden NICHT in § 3 Nr. 63 EStG-Grenze eingerechnet.
- Solche Altvertraege getrennt fuehren.

### Phase 5 — Wechsel AG

- Bei Wechsel des AG: bisherige Beitraege sind beruecksichtigt fuer das Wechseljahr.
- Beim neuen AG: Jahresgrenze 8 Prozent BBG; bisherige Beitraege beim alten AG anrechnen.
- AN muss neue AG ueber laufende Vertraege informieren.

### Phase 6 — Dokumentation

- Beitragspruefliste pro AN mit allen Vertraegen.
- Jaehrliche Aktualisierung.
- Bei Aenderungen Anpassung Lohnabrechnung.

## Output

- bAV-Pruefnotiz mit Beitragssumme und Restbetragsgrenze.
- Empfehlung Beitragsanpassung.
- Lohnabrechnung mit Beruecksichtigung der Doppelfoerderung.

## Strategie und Praxis-Tipps

- Bei mehreren Vertraegen jahrelange Plausibilitaetspruefung — sonst rueckwirkende Versteuerung.
- AN-Information ueber alle bAV-Vertraege beim AG einholen (Antragsformular).
- Bei sehr engen Grenzen: Beitragsreduktion frueh angeben.
- StBVV: bei mehreren bAV-Vertraegen Mehraufwand — Zusatzauftrag.
- DATEV-Tipp: DATEV LODAS bAV-Kumulation pro AN, automatische 8-Prozent-Pruefung.

## Querverweise

- `stb-lohn-betriebliche-altersversorgung-grundlagen` — bAV.
- `stb-lohn-direktversicherung-3-nr-63-estg` — Direktversicherung.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 63, 19, 40b a.F.
- BetrAVG §§ 1, 1a.
- SvEV § 1 Abs. 1 Nr. 9.
- BMF v. 06.12.2017 (IV C 5 - S 2333/17/10002), BMF v. 18.03.2022 (IV C 5 - S 2333/19/10005).
- BBG-West RV 2025: 96.600 EUR/Jahr; 8 Prozent = 7.728 EUR LSt-frei, 4 Prozent = 3.864 EUR SV-frei (Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 2 bestaetigt (BMF-Daten recherchiert), 2 ersetzt (BBG-Werte 2025 eingesetzt, Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende`

**Fokus:** Berufsgenossenschaft Lohnnachweis Jahresende. Anwendungsfall jaehrlicher Lohnnachweis an die zuständige BG Vorauszahlung BG-Beitrag Schluesseldaten Gefahrtarif. Methodik elektronischer Lohnnachweis über sv.net oder DAKOTA. Output BG-Lohnnachweis Beitragsbescheid.

# Berufsgenossenschaft — Lohnnachweis Jahresende

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Berufsgenossenschaft — Lohnnachweis Jahresende` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Jeder AG ist Pflichtmitglied einer Berufsgenossenschaft (BG; gesetzliche Unfallversicherung). Der BG-Beitrag wird auf Basis der Lohnsumme und des Gefahrtarifs berechnet. Bis 15. Februar des Folgejahres muss der elektronische Lohnnachweis an die BG uebermittelt werden. Im laufenden Jahr werden Vorauszahlungen anhand der Vorjahres-Lohnsumme geleistet.

## Kaltstart-Rueckfragen

1. Welche BG ist zustaendig (Branche/Gewerbeart)?
2. Welcher Gefahrtarif (Beitragsklasse) liegt vor?
3. Welche Mitgliedsnummer?
4. Welche Lohnsumme aus Vorjahr (Bemessungsbasis)?
5. Welche Vorauszahlungs-Raten laufen?
6. Sind aussergewoehnliche Lohnentwicklungen zu melden?
7. Liegen BG-Korrespondenzen vor?
8. Welche AN sind in der Lohnsumme einbezogen (alle Vollzeit/Teilzeit/Minijob)?

## Rechtlicher Rahmen

### Primaernormen

**SGB VII** — Gesetzliche Unfallversicherung.

**§ 150 SGB VII** — Beitragspflicht AG.

**§ 165 SGB VII** — Lohnnachweis.

**§ 166 SGB VII** — Beitragsbemessung.

### Verwaltungsanweisungen

- BG-Satzungen.
- BG-Spitzenverband Rundschreiben.

## Workflow

### Phase 1 — BG-Mitgliedschaft pruefen

- Branche und Gewerbeart bestimmen zustaendige BG (z.B. BG Bau, BG Handel und Warenlogistik, BG ETEM, BG Holz und Metall).
- Mitgliedsnummer aus BG-Bescheid.
- Mitgliedschaftsbeginn dokumentiert.

### Phase 2 — Gefahrtarif

- Jede Beschaeftigung wird einer Gefahrenklasse zugeordnet (Branchenstaerke des Unfallrisikos).
- Gefahrtarif aus BG-Satzung.
- Beitragssatz auf 1.000 EUR Lohnsumme (z.B. 5,00 EUR pro 1.000 EUR Lohnsumme bei Gefahrenklasse 5).

### Phase 3 — Lohnsumme zusammenstellen

- Brutto-Lohnsumme aller AN ueber das Geschaeftsjahr.
- Einschluesse: alle SV-pflichtigen Loehne plus Minijob-Loehne.
- Aussschluesse: ggf. bestimmte Sonderzahlungen (BG-spezifisch).
- Aufteilung nach Gefahrenklasse (bei Mischbetrieb).

### Phase 4 — Elektronischer Lohnnachweis (UV-Jahresmeldung)

- Form: elektronisch ueber sv.net, DAKOTA oder das BG-Portal; in DATEV LODAS unter Auswertung → Jahresmeldungen → UV-Jahresmeldung.
- Frist: spaetestens 16. Februar des Folgejahres (§ 99 SGB IV i.V.m. § 165 SGB VII; bei Wochenend-Verschiebung folgender Werktag).
- Inhalt: Lohnsumme je Gefahrenklasse, geleistete Arbeitsstunden, Mitgliedsnummer.
- Nach BG-Bescheid: Beitragsbescheid mit Nachzahlung oder Erstattung; Faelligkeit der Nachzahlung je BG-Satzung (typisch 15. April oder 15. Mai des Folgejahres — genaue Faelligkeit in der Satzung der jeweils zustaendigen BG pruefen).

### Phase 5 — Vorauszahlungen

- Bemessung nach Vorjahres-Lohnsumme.
- Monatliche oder vierteljaehrliche Vorauszahlungen.
- Anpassung bei wesentlichen Lohnsummen-Aenderungen.

### Phase 6 — Buchung

- BG-Vorauszahlung als Lohnnebenkosten (Konto 4140 SKR 03 oder vergleichbar).
- Jahresabrechnung mit Soll-Ist-Vergleich.
- Bei Nachzahlung: zusaetzliche Buchung.

## Output

- Elektronischer Lohnnachweis.
- BG-Beitragsbescheid in Mandantenakte.
- Buchung im Hauptbuch.

## Strategie und Praxis-Tipps

- Frist 15. Februar zwingend einhalten — Verspaetungszuschlag der BG.
- Bei Branchenwechsel oder neuen Taetigkeiten BG-Konsultation (ggf. neue Gefahrenklasse).
- Bei wachsender Belegschaft: monatliche Vorauszahlungen anpassen, um Nachzahlung zu vermeiden.
- BG bietet oft Beratung zur Unfallpraevention an (Praemienrabatt moeglich).
- StBVV: BG-Lohnnachweis als Sonderauftrag (jaehrlich).
- DATEV-Tipp: DATEV LODAS BG-Modul mit automatischer Lohnsummen-Aufstellung.

## Querverweise

- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.
- `stb-lohn-jahresmeldungen-ahn-asn-besondere` — Jahresmeldungen.
- `stb-lohn-sv-meldungen-dakota-svnet` — sv.net.

## Quellen und Updates

Stand: 05/2026.

- SGB VII §§ 150, 165, 166.
- BG-Satzungen.
- BG-Spitzenverband Rundschreiben.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (BG-Satzungs-Faelligkeit ohne Marker neu formuliert) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-lohn-betriebsausfluege-aufmerksamkeiten-60-euro`

**Fokus:** Aufmerksamkeiten 60 EUR-Freigrenze pro persoenlichem Anlass. Anwendungsfall Sachgeschenk zu Geburtstag Hochzeit Jubilaeum 60 EUR Hoechstwert LSt-frei. Methodik Abgrenzung zur 50 EUR-Sachbezugs-Freigrenze. Output korrekte Lohn-Behandlung Aufmerksamkeit.

# Aufmerksamkeiten — 60-EUR-Freigrenze pro persoenlichem Anlass

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aufmerksamkeiten — 60-EUR-Freigrenze pro persoenlichem Anlass` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Aufmerksamkeiten zu persoenlichen Anlaessen (Geburtstag, Hochzeit, Geburt eines Kindes, runder Beschaeftigungs-Jubilaeum) sind LSt-frei bis 60 EUR pro Anlass (LStR R 19.6). Diese Regelung ist UNABHAENGIG von der 50-EUR-Sachbezugs-Freigrenze nach § 8 Abs. 2 Satz 11 EStG. Wichtig: keine Geldzuwendung, sondern Sachzuwendung. Anlassbezug muss erkennbar sein. Bei Ueberschreiten ist Aufmerksamkeit voll steuerpflichtig.

## Kaltstart-Rueckfragen

1. Liegt ein persoenlicher Anlass beim AN vor (Geburtstag, Hochzeit, Geburt, Jubilaeum)?
2. Welche Form der Zuwendung (Blumen, Sachgeschenk, Gutschein)?
3. Wert der Zuwendung?
4. Anlass dokumentiert (Karte, Vermerk)?
5. Hat der AG weitere Sachbezuege im Monat (50-EUR-Grenze ist getrennt)?
6. Bei Hochzeitsgeschenk: AN heiratet oder AG?
7. Bei Jubilaeum: AN-Beschaeftigungsdauer oder AG-Firmenjubilaeum?
8. Bei Tod nahestehender Person: Trauerbeihilfe (eigenes Regelwerk)?

## Rechtlicher Rahmen

### Primaernormen

**§ 8 Abs. 2 EStG** — Sachbezug.

**§ 19 EStG** — Arbeitslohn.

**LStR R 19.6** — Aufmerksamkeiten 60-EUR-Freigrenze.

### Verwaltungsanweisungen

- BMF zu Aufmerksamkeiten.
- LStR R 19.6 (laufende Aktualisierung).

## Workflow

### Phase 1 — Anlass-Pruefung

| Anlass | Aufmerksamkeit |
|---|---|
| Geburtstag (regelmaessig) | Ja (60 EUR-Grenze) |
| Runder Geburtstag (50, 60, 70) | Ja |
| Hochzeit | Ja |
| Geburt eines Kindes | Ja |
| Beschaeftigungs-Jubilaeum 10, 20, 25 Jahre | Ja |
| Krankheit, Genesung (Blumenstrauss) | Ja |
| Beerdigung (Trauerbeihilfe) | Eigenes Regelwerk (R 19.7 LStR) |
| Firmenjubilaeum (kein persoenlicher Anlass des AN) | Nein, ggf. § 19 Abs. 1 Nr. 1a EStG Betriebsveranstaltung |

### Phase 2 — Hoechstgrenze

- 60 EUR brutto inkl. USt pro persoenlichem Anlass.
- Ueberschreitung: GESAMTE Zuwendung steuerpflichtig (Freigrenze, nicht Freibetrag).
- Bei mehrfacher Aufmerksamkeit im Jahr: jede separat (z.B. Geburtstag + Hochzeit = beide bis 60 EUR moeglich).
- Beispiel: Geschenkkorb fuer 55 EUR brutto zum Geburtstag = LSt- und SV-frei. Geschenkkorb fuer 65 EUR brutto = vollstaendig (alle 65 EUR) lohnsteuer- und beitragspflichtig; Pauschalierung § 37b EStG (30 Prozent) als AG-Option moeglich.

### Phase 3 — Form der Zuwendung

- Sachzuwendung: Blumen, Sachgeschenk, Sachgutschein.
- Geldzuwendung: KEIN Aufmerksamkeit nach R 19.6 — voll steuerpflichtig.
- Gutschein: ZAG-konformer Sachgutschein wie Sachbezug (BMF v. 13.04.2021).

### Phase 4 — Dokumentation

- Belegabbau: Beleg der Sachzuwendung mit Anlass-Vermerk.
- Z.B. "Geburtstagsgeschenk Herr Mueller, 15.04.2026, Wert 55 EUR".
- Im Lohnordner archivieren.

### Phase 5 — Lohnabrechnung

- Bei Einhaltung 60-EUR-Grenze: LSt-frei, SV-frei.
- Keine Buchung in DATEV LODAS als Lohn.
- Belege im Lohnordner.

### Phase 6 — Bei Ueberschreitung

- Voller Wert lohnsteuerpflichtig (Freigrenze, daher gesamte Zuwendung).
- Pauschalierung § 37b EStG 30 Prozent (zzgl. SolZ und KiSt) durch AG moeglich; SV-Befreiung bei Pauschalierung im Anwendungsbereich des § 37b EStG (sofern "zusaetzlich zum Lohn") nach SvEV-Auslegung.
- Sonst regulaer SV-pflichtig.

## Output

- Aufmerksamkeits-Dokumentation pro Anlass.
- Lohn-Abrechnung nur bei Ueberschreitung.
- Beleg im Lohnordner.

## Strategie und Praxis-Tipps

- Aufmerksamkeiten sind nicht-versteuerter Bonus — generoes nutzen.
- 60-EUR-Grenze ist Freigrenze: bei 60,01 EUR alles steuerpflichtig.
- Geldzuwendung ist KEINE Aufmerksamkeit — immer steuerpflichtig (auch wenn der Anlass persoenlich ist).
- Bei mehreren Anlaessen im Monat: jeder einzeln 60-EUR-Grenze; nicht kumulativ.
- Wenn Aufmerksamkeit + Sachbezug zusammenkommen: Aufmerksamkeit gehoert NICHT in 50-EUR-Sachbezugs-Grenze, getrennt behandeln.
- StBVV: in Lohnpauschale; Gestaltungsberatung Zeithonorar.
- DATEV-Tipp: DATEV LODAS Aufmerksamkeits-Konto getrennt von Sachbezug.

## Querverweise

- `stb-lohn-sachbezuege-50-euro-freigrenze` — Sachbezug.
- `stb-lohn-betriebsveranstaltung-110-euro-freibetrag` — Betriebsveranstaltung.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 8, 19, 37b.
- LStR R 19.6, R 19.7.
- BMF v. 13.04.2021 (Gutscheine).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-lohn-betriebsveranstaltung-110-euro-freibetrag`

**Fokus:** Betriebsveranstaltung 110 EUR-Freibetrag § 19 Abs 1 Nr 1a EStG. Anwendungsfall Firmenfeier Sommerfest Weihnachtsfeier Kostenkalkulation 110 EUR pro AN Pauschalierung. Methodik Berechnung Prüfung Belege. Output Lohn-Abrechnung mit Betriebsveranstaltung.

# Betriebsveranstaltung — 110-EUR-Freibetrag § 19 Abs. 1 Nr. 1a EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebsveranstaltung — 110-EUR-Freibetrag § 19 Abs. 1 Nr. 1a EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Betriebsveranstaltungen (Sommerfest, Weihnachtsfeier, Betriebsausflug) sind Sachzuwendungen, fuer die ein Freibetrag von 110 EUR pro AN und pro Veranstaltung gilt (§ 19 Abs. 1 Nr. 1a EStG). Bei Ueberschreitung des Freibetrags ist nur der ueberschiessende Teil steuerpflichtig (Freibetrag, nicht Freigrenze!). Maximal 2 Veranstaltungen pro Jahr begunstigt. Begleitpersonen (Partner) werden dem AN zugerechnet.

## Kaltstart-Rueckfragen

1. Welche Art Betriebsveranstaltung — Sommerfest, Weihnachtsfeier, Jubilaeum?
2. Wie viele Veranstaltungen im laufenden Jahr (max. 2 begunstigt)?
3. Welche Gesamtkosten der Veranstaltung?
4. Wie viele AN nehmen teil? Mit Partnern/Familie?
5. Erfolgt die Teilnahme freiwillig?
6. Steht die Veranstaltung allen AN offen (sonst keine Begunstigung)?
7. Welche Belege liegen vor?
8. Pauschalierung § 40 Abs. 2 EStG fuer ueberschiessenden Teil gewuenscht?

## Rechtlicher Rahmen

### Primaernormen

**§ 19 Abs. 1 Nr. 1a EStG** — 110-EUR-Freibetrag Betriebsveranstaltung.

**§ 40 Abs. 2 Satz 1 Nr. 2 EStG** — Pauschalbesteuerung 25 Prozent.

**§ 8 Abs. 2 EStG** — Sachbezug.

### Verwaltungsanweisungen

- BMF v. 14.10.2015 — Betriebsveranstaltung (IV C 5 - S 2332/15/10006; aktuelle ergaenzende BMF-Schreiben ueber BMF-Internet pruefen).
- LStR R 19.5.

### Leitentscheidungen (Aktenzeichen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen)

- **BFH, Urteil vom 27.03.2024 — VI R 5/22**: Eine Betriebsveranstaltung i.S.d. § 19 Abs. 1 S. 1 Nr. 1a S. 1 EStG kann auch dann vorliegen, wenn sie nicht allen Angehoerigen eines Betriebs oder Betriebsteils offensteht (Begriff der Betriebsveranstaltung weit). Der Begriff in § 40 Abs. 2 S. 1 Nr. 2 EStG entspricht der Legaldefinition § 19 Abs. 1 S. 1 Nr. 1a S. 1 EStG. Volltext ueber BFH-Datenbank (STRE202410082).
- **Reaktion des Gesetzgebers — Steueraenderungsgesetz 2025** (verkuendet 23.12.2025, in Kraft 01.01.2026): Klarstellung, dass die **Offenheit fuer alle Beschaeftigten** des Betriebs / Betriebsteils Voraussetzung der **Pauschalbesteuerung nach § 40 Abs. 2 S. 1 Nr. 2 EStG** ist (Reaktion auf BFH VI R 5/22). Der 110-EUR-Freibetrag bleibt unveraendert; ebenso die Begrenzung auf zwei Veranstaltungen pro Jahr.
- BFH-Linie zur Aufteilung der Gesamtkosten auf alle teilnehmenden Personen (statt nur AN-Anzahl); aktuelle Entscheidungen vor Mandantengespraech in BFH-Datenbank / dejure.org pruefen.

## Workflow

### Phase 1 — Voraussetzungen

| Voraussetzung | Pruefung |
|---|---|
| Geselliger Charakter | Sommerfest, Weihnachtsfeier ja; Schulung nein |
| Offen fuer alle AN (oder Teilgruppe wie Abteilung) | Ja |
| Freiwillige Teilnahme | Ja |
| Max. 2 Veranstaltungen pro Jahr begunstigt | Pruefung |

### Phase 2 — Kostenermittlung

```
Gesamtkosten Veranstaltung (incl. USt):
+ Catering, Getraenke
+ Saalmiete, Veranstaltungsdienst
+ Unterhaltungsprogramm
+ Geschenke an AN (begrenzt)
+ Reisekosten zur Veranstaltung
+ Aufmerksamkeiten
= Gesamtkosten

Anteil je AN:
Gesamtkosten / Anzahl tatsaechlicher Teilnehmer = AN-Anteil
```

(Hinweis: Geltende BMF-Linie bezieht alle teilnahmenden Personen ein.)

### Phase 3 — Begleitpersonen

- Partner, Ehepartner, Kinder werden Anteil dem AN zugerechnet.
- Beispiel: AN mit Partner — Anteil ist doppelt so hoch.

### Phase 4 — Freibetrag-Verrechnung

- 110 EUR pro AN abziehen (Freibetrag, nicht Freigrenze: nur ueberschiessender Teil ist steuerpflichtig).
- Verbleibender Anteil: steuerpflichtig.
- Beispiel: AN-Anteil 150 EUR, Freibetrag 110 EUR, steuerpflichtig 40 EUR.
- Begleitperson zugerechnet: AN mit Partner und AN-Anteil 80 EUR + 80 EUR = 160 EUR; abzueglich 110 EUR Freibetrag = 50 EUR steuerpflichtig. (Der Freibetrag steht nur dem AN zu, nicht zusaetzlich der Begleitperson.)

### Phase 5 — Pauschalbesteuerung

- AG kann ueberschiessenden Teil pauschal 25 Prozent versteuern (§ 40 Abs. 2 EStG).
- AN-Vorteil: Netto bleibt.
- AG-Aufwand: 25 Prozent zzgl. KiSt und SolZ.
- Bei Pauschalbesteuerung: SV-frei.

### Phase 6 — Lohnabrechnung und Dokumentation

- Belege Veranstaltung aufbewahren.
- Teilnehmerliste mit AN-Namen und Begleitpersonen.
- DATEV LODAS: Sachbezug-Lohnart "Betriebsveranstaltung" mit Pauschalbesteuerung.

## Output

- Kostenkalkulation der Veranstaltung.
- Teilnehmerliste.
- Lohn-Abrechnung mit Pauschalbesteuerung.

## Strategie und Praxis-Tipps

- 110 EUR Freibetrag pro AN und pro Veranstaltung — bei 2 Veranstaltungen pro Jahr 220 EUR.
- Bei 3. Veranstaltung im Jahr: keine Freibetrags-Anwendung mehr, voll steuerpflichtig.
- "Geschlossene Teilnehmerkreise" (z.B. nur Vertrieb): keine Begunstigung.
- Bei Catering und Getranken sorgfaeltige Belegerstellung — Pruefer fragt nach.
- Geschenke an AN auf der Veranstaltung sind eingerechnet — Aufmerksamkeit 60 EUR pruefen.
- StBVV: Sonderlohn-Berechnung; bei groesseren Veranstaltungen Zeithonorar.
- DATEV-Tipp: DATEV LODAS Betriebsveranstaltungs-Modul mit automatischer Pauschalierung.

## Querverweise

- `stb-lohn-sachbezuege-50-euro-freigrenze` — Sachbezug.
- `stb-lohn-betriebsausfluege-aufmerksamkeiten-60-euro` — Aufmerksamkeit.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 19 Abs. 1 Nr. 1a, 40 Abs. 2.
- BMF v. 14.10.2015.
- LStR R 19.5.
- BFH v. 27.03.2024 — VI R 5/22.
- Steueraenderungsgesetz 2025 (BGBl. 2025 I, verkuendet 23.12.2025, in Kraft 01.01.2026) — Klarstellung zur Offenheit bei § 40 Abs. 2 S. 1 Nr. 2 EStG.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (BMF-Datum 14.10.2015 und GZ recherchiert), 1 ersetzt (Pruefhinweis ohne Marker) -->
<!-- UPDATE 29.05.2026 | BFH VI R 5/22 (27.03.2024) und Steueraenderungsgesetz 2025 ergaenzt -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-lohn-gesellschafter-geschaeftsfuehrer-sv`

**Fokus:** Gesellschafter-Geschäftsführer GGF SV-Pflicht oder SV-Befreiung. Anwendungsfall Prüfung GGF einer GmbH ob abhaengig beschaeftigt oder selbständig tätig Statusfeststellung. Methodik Kriterienkatalog Beteiligung Weisungsgebundenheit Sperrminoritaet. Output Statusfeststellungs-Antrag Bescheid Mandanten-Notiz.

# Gesellschafter-Geschaeftsfuehrer — SV-Pflicht oder Befreiung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafter-Geschaeftsfuehrer — SV-Pflicht oder Befreiung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Bei Gesellschafter-Geschaeftsfuehrern (GGF) einer GmbH ist die SV-Pflicht haeufig strittig: abhaengig beschaeftigt (= SV-pflichtig) oder selbstaendig (= nicht SV-pflichtig). Die DRV-Statusfeststellung (§ 7a SGB IV) gibt Rechtssicherheit. Wesentliche Kriterien: Beteiligungshoehe, Weisungsgebundenheit, unternehmerisches Risiko, Sperrminoritaet. BSG-Rechtsprechung sehr detailliert; Fehlklassifikation fuehrt zu Nachforderung ueber 4 Jahre + Saeumniszuschlag.

## Kaltstart-Rueckfragen

1. Welche Beteiligungshoehe hat der GGF (Prozentsatz Kapital)?
2. Liegt Stimmrechtsvertrag mit Sperrminoritaet vor?
3. Welche Anstellung — Geschaeftsfuehrer-Vertrag mit festem Gehalt? Erfolgsbezogen?
4. Welche Weisungsgebundenheit (Gesellschafterversammlung Weisungen)?
5. Andere Gesellschafter (Familie, externe)?
6. Wurde Statusfeststellung beantragt? Liegt Bescheid vor?
7. Liegt aktuelle BSG-Rechtsprechung dazu vor (z.B. Familien-GmbH)?
8. Bei abhaengiger Beschaeftigung: SV-Pflicht alle Zweige?

## Rechtlicher Rahmen

### Primaernormen

**§ 7 SGB IV** — Beschaeftigungs-Definition (abhaengig vs. selbstaendig).

**§ 7a SGB IV** — Statusfeststellungsverfahren bei DRV.

**§ 28a SGB IV** — Meldepflichten.

**§ 28p SGB IV** — Pruefung Sozialversicherungsbeitraege.

**GmbHG §§ 37, 47** — Geschaeftsfuehrer-Stellung und Stimmrechte.

### Leitentscheidungen BSG

| Gericht | Aktenzeichen | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

(Aktenzeichen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen.)

## Workflow

### Phase 1 — Kriterien-Pruefung

| Kriterium | Spricht fuer selbstaendig | Spricht fuer abhaengig |
|---|---|---|
| Kapitalbeteiligung | Mehrheit | Minderheit |
| Stimmrechte | Mehrheit oder Sperrminoritaet | Minderheit ohne Sperre |
| Weisungsbefugnis Gesellschafterversammlung | Nicht weisungsgebunden | Weisungsgebunden |
| Familienverhaeltnis | Familie mit Einigkeit | Externe Gesellschafter |
| Unternehmerisches Risiko | GGF traegt mit | Nur Lohn |
| Arbeitszeit | Frei einteilbar | Vorgegeben |
| Tantieme/Erfolgsbeteiligung | Hoch | Gering / fest |

### Phase 2 — Statusfeststellung

- Antrag bei DRV (§ 7a SGB IV).
- Formular V0027.
- Beilagen: Gesellschaftsvertrag, GF-Vertrag, Gesellschafterliste.
- Bearbeitungszeit ca. 3-6 Monate.
- Bescheid bindet auch fuer Krankenkasse und FA.

### Phase 3 — Wirkung bei selbstaendig

- Keine SV-Pflicht.
- AG zahlt keine SV-Beitraege.
- GGF privat versichert (KV/PV als Privatversicherung).
- RV freiwillig (DRV-freiwillige Versicherung).
- AV nicht moeglich.

### Phase 4 — Wirkung bei abhaengig

- SV-Pflicht alle Zweige (KV/PV/RV/AV).
- AG-Anteile zu zahlen.
- LSt nach Steuerklasse.
- BBG-Grenzen wie regulaer AN.

### Phase 5 — Sonderfaelle

- Fremd-Geschaeftsfuehrer (keine Kapitalbeteiligung): in der Regel abhaengig.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Geschaeftsfuehrer mit echter Sperrminoritaet ueber satzungsmaessige Beschluesse (typisch >25 Prozent bei Mehrheitsklauseln; einzelfallabhaengig): selbstaendig.
- 50/50-GGF mit zwei Gesellschaftern und Vetoposition: selbstaendig (kein Beschluss gegen ihn moeglich).
- Wichtig: Stimmrechtsvereinbarungen ausserhalb der Satzung (Pool-Vertrag) werden vom BSG seit ca. 2015 nicht mehr als Sperrminoritaet anerkannt.

### Phase 6 — Risiko bei Fehlklassifikation

- Bei DRV-Pruefung: rueckwirkende Nachforderung 4 Jahre.
- Saeumniszuschlag 1 Prozent pro Monat.
- AG haftet fuer AN- und AG-Anteil.
- Strafrechtlich § 266a StGB-Risiko bei Vorsatz.

## Output

- Statusfeststellungs-Antrag DRV.
- Bescheid mit Statusfeststellung.
- Mandanten-Notiz fuer Lohnabrechnung.
- Lohnabrechnung mit korrekter SV-Behandlung.

## Strategie und Praxis-Tipps

- Statusfeststellung bei jedem GGF zwingend empfehlen — Rechtssicherheit.
- Bei Familien-GmbH besonders sorgfaeltig — BSG hat hier mehrfach gewechselt.
- Satzungsmaessige Sperrminoritaet (Hoehe je nach Gesellschaftsvertrag, typisch >25 Prozent) ist nach BSG-Linie die sichere Trennlinie zu Selbstaendigkeit; Stimmrechtsvereinbarungen ausserhalb der Satzung reichen nicht.
- Bei spaeterer Aenderung (Verkauf Anteile, neue Gesellschaftervereinbarung): Statusfeststellung wiederholen.
- StBVV: Statusfeststellung als Zusatzauftrag mit Zeithonorar (komplex).
- DATEV-Tipp: DATEV LODAS bei GGF separate Personengruppen-Schluessel; bei "selbstaendig" Lohnabrechnung manuell konfigurieren.

## Querverweise

- `stb-drv-sozialversicherungspruefung` — DRV-Pruefung.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-pruefungen-drv-bp-haftung-stb` — DRV-Pruefung Haftung.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 7, 7a, 28a, 28p.
- GmbHG §§ 37, 47.
- StGB § 266a.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Gemeinsame Rundschreiben Spitzenverbaende KK.

<!-- AUDIT 27.05.2026 | welle 6 | 3 Marker aufgeloest: 2 bestaetigt (BSG-Az recherchiert), 1 ersetzt (Pruefhinweis ohne Marker) -->
