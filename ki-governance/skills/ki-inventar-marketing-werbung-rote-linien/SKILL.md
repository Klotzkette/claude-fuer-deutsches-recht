---
name: ki-inventar-marketing-werbung-rote-linien
description: "Für /ki-inventar: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# /ki-inventar

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Verordnung (EU) 2024/1689 in der Fassung 2026/1744: Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5 für Anhang III ab 02.12.2027, für Anhang I ab 02.08.2028. Artikel 4 neuer Fassung, Artikel 4a, Verbote und Transparenz gesondert prüfen; Vorfallfrist nach Tatbestand und Ereignis, Datenschutz-Folgenabschätzung vor riskanter Verarbeitung.
- Tragende Rechtsgrundlagen am amtlichen EUR-Lex-Text der KI-Verordnung und der gegebenenfalls einschlägigen DSGVO prüfen. ISO/IEC 42001, NIST AI RMF und OECD-Prinzipien sind keine Verordnungsartikel. Bei harmonisierten Normen konkrete Fassung, Amtsblattfundstelle und abgedeckte Anforderungen nach Artikel 40 feststellen; freiwilliges Managementzertifikat und Konformitätsverfahren nach Artikel 43 trennen. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Dieses Inventar dient der strukturierten Erfassung aller KI-Systeme einer Organisation nach
Art. 6 ff. KI-VO (VO 2024/1689). Der zentrale Grundsatz: **Rolle und Risikoklasse werden
je KI-System bewertet, nicht je Unternehmen.** Eine Organisation kann Anbieter von System A,
Betreiber von System B und Einführer von System C sein. Jede Kombination löst nach der KI-VO
unterschiedliche Pflichten aus (z. B. Art. 16 ff. für Anbieter, Art. 26 für Betreiber).
Sanktionen nach Artikel 99 hängen vom konkreten Pflichtverstoß, Adressaten und Zeitpunkt ab; die Höchstwerte für Artikel 5 sind kein allgemeiner Bußgeldrahmen für jeden Inventarfehler. Das Inventar dient als Basis für alle nachgelagerten Pflichten;
die eigentliche Obligationenanalyse erfolgt im Gespräch, nicht aus einer fest codierten Tabelle.

## Eingaben

- Konfiguration aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
- Bestehendes Inventar unter `ki-systeme.yaml` (gleicher Konfigurationspfad)
- Systembeschreibung des Nutzers oder vorhandene Unterlagen (technische Dokumentation, Verträge)

## Ablauf

1. **Konfiguration lesen.** Prüfen, ob das Praxisprofil vorhanden und befüllt ist. Fehlen
 `[PLATZHALTER]`-Marker, Nutzer an `/ki-governance:kaltstart-interview` verweisen.

2. **Inventar lesen.** Liegt unter `ki-systeme.yaml`. Existiert die Datei nicht, bei erstem
 `add`-Befehl mit leerem `systeme:`-Block anlegen.

3. **Befehl ausführen:**
 - Kein Argument oder `list` → Inventartabelle anzeigen (siehe **Listenformat**)
 - `add` → **Aufnahmefluss** starten
 - `edit <id>` → aktuellen Datensatz zeigen, Änderungsfrage stellen, ein Feld ändern,
 bestätigen, schreiben
 - `classify <id>` → **Klassifizierungsdurchlauf** für bestehenden Datensatz starten,
 `rolle`, `klasse`, `rollenbasis` und `klassenbasis` aktualisieren
 - `show <id>` → vollständigen Datensatz anzeigen

4. **Nach `list` Dashboard anbieten:**
 "Dashboard gewünscht? Filterbar nach Status / Klasse / EU-Nexus / Eigentümer. Auf Wunsch."

5. **Jede Aktion mit Anschlusshinweis abschließen:**
 > Erfasst. Wenn Sie die Pflichten für dieses System durcharbeiten möchten, fragen Sie
 > einfach – ich führe die Analyse im Gespräch durch und markiere, wo die Artikel-Zuordnung
 > Ihre Verifizierung erfordert. Pflichten werden nicht aus einer Tabelle abgeleitet, weil
 > die Zuordnung funktions- und rollenbezogen erfolgt und Artikel 111/113 unterschiedliche Anwendungs- und Übergangszeitpunkte enthalten; eine pauschale Einführungsphase „bis 2027“ gibt es nicht.

## Listenformat

Kompakte Tabelle:

| ID | Name | Eigentümer | Status | EU-Nexus | Rolle | Klasse | Nächste Prüfung |
|----|------|-----------|--------|----------|-------|--------|-----------------|
| sys-001 | Lebenslauf-Screening | HR / Schmidt | in_produktion | ja | Betreiber | hochrisiko | 2026-08-01 |
| sys-002 | E-Mail-Drafting-Assistent | IT / Meier | in_produktion | nein | Betreiber | begrenzt | 2026-12-01 |

Unter der Tabelle: Zählung nach Klasse und: "N Systeme zur Prüfung innerhalb von 30 Tagen."
Nur bei einem konkreten möglichen Verstoß den zutreffenden Absatz des Artikels 99 und die Sonderregeln der Absätze 6/6a prüfen; keine pauschale Sanktionsdrohung im Inventar.

## Aufnahmefluss (Interview)

Felder einzeln abfragen (oder Einfügen akzeptieren). Pflichtfelder: `name`, `eigentümer`,
`beschreibung`, `status`, `eu_nexus`. Rest kann zurückgestellt werden – explizit darauf
hinweisen: "Sie können die Klassifizierung mit `/ki-governance:ki-inventar classify <id>`
nachholen."

1. **Name.** Kurzbezeichnung des Systems.
2. **Eigentümer.** Person oder Team, das täglich für das System verantwortlich ist.
3. **Beschreibung.** Ein bis zwei Sätze: Was tut es, und mit welchen Daten?
4. **Status.** `geplant | in_entwicklung | in_produktion | ausgemustert`
5. **EU-Nexus.** Wird das System in der EU/EWR betrieben, EU/EWR-Nutzern angeboten oder
 erzeugt es Ausgaben, die in der Union verwendet werden? Den räumlichen und persönlichen Anwendungsbereich nach Artikel 2 sowie Ausnahmen und den EWR-Rechtsstand gesondert belegen; eine Betroffenheit allein ist keine vollständige Subsumtion.
 Transparenzpflichten nach Art. 50 KI-VO beachten (z. B. Offenlegung bei Chatbots,
 Deepfake-Kennzeichnung).
6. **Klassifizierung jetzt?** Anbieten, den Durchlauf sofort zu starten oder zurückzustellen.

ID vergeben: `sys-NNN` (nächste aufsteigende Nummer in der Datei).

## Klassifizierungsdurchlauf

Der Durchlauf ergibt `rolle`, `rollenbasis`, `klasse`, `klassenbasis`. Beide Begründungen
brauchen eine sichtbare Quellenbasis mit Artikel, Anhangspunkt und Datum der Prüfung, weil
die Artikel-Zuordnung komplex ist und die KI-VO noch in der Einführungsphase ist. Der Anwalt
trägt die Verantwortung für die finale Verifizierung.

### Schritt 1: Rolle

> **Wer macht was mit diesem System?**

Optionen mit unterscheidendem Merkmal:

- **Anbieter (Art. 3 Nr. 3 KI-VO)** – Sie entwickeln das KI-System (oder lassen es entwickeln)
 und bringen es unter eigenem Namen oder Warenzeichen auf den EU-Markt oder in Betrieb.
- **Betreiber (Art. 3 Nr. 4 KI-VO)** – Sie nutzen das KI-System in eigener Verantwortung,
 nicht zu rein persönlichen nicht-beruflichen Zwecken. (Häufigster Fall innerhalb von
 Unternehmen.) Betreiberpflichten: Art. 26 KI-VO.
- **Einführer (Art. 3 Nr. 6 KI-VO)** – Sie bringen ein KI-System aus einem Nicht-EU-Anbieter
 unter dem Namen oder der Marke eines Drittstaatenanbieters auf dem Unionsmarkt in Verkehr; Ansässigkeit in der Union prüfen.
- **Händler (Art. 3 Nr. 7 KI-VO)** – Sie machen ein KI-System auf dem EU-Markt verfügbar,
 ohne Anbieter oder Einführer zu sein.
- **Bevollmächtigter (Art. 3 Nr. 5 KI-VO)** – Sie handeln im Auftrag eines Nicht-EU-Anbieters
 und sind in der EU/EWR ansässig.
- **Produkthersteller (Artikel 25 Absatz 3 KI-Verordnung)** – Prüfen Sie die dort bezeichnete Verbindung von Produkt, Hochrisiko-KI und eigenem Namen. Keine automatische Anbieterrolle jedes Integrators; Artikel 3 Nummer 15 definiert den Sicherheitsbauteil, nicht den Produkthersteller.

**Doppelrollen-Flag.** Wenn der Nutzer ein Anbieter-System wesentlich ändert (Fine-Tuning auf
eigenen Daten, Änderung des vorgesehenen Verwendungszwecks, Rebranding), kann er zum
**Anbieter** des geänderten Systems werden – auch wenn er als Betreiber begann. Hinweis
geben, wann immer eine Änderung über die Konfiguration hinausgeht. `[gegen aktuellen
KI-VO-Text prüfen – Art. 25 KI-VO, Anbieterpflichten und wesentliche Änderung]`

Rolle schreiben. `rollenbasis` in einem Satz schreiben.

### Schritt 2: Pflichtspuren

#### 2.1. Gegenstand und Rollen

Fixieren Sie Systemversion, beabsichtigte Funktion, tatsächlichen Einsatz, Betroffene, Datenfluss, Anbieter und Betreiber. Modell und darauf aufbauendes System sind verschiedene Prüfgegenstände. Ein Produktname wie „Agent“ oder ein interner Governance-Reifegrad belegt keinen Tatbestand. Erfragen Sie nur das für die nächste Weiche fehlende Detail; nutzen Sie zuerst vorhandene Verträge, Screenshots und Prozessbeschreibungen.

Ordnen Sie Rollen nach Artikel 3 und gegebenenfalls Artikel 25 zu. Entwicklung im Auftrag und Inbetriebnahme unter eigenem Namen können Anbieterrelevanz haben. Eine bloße Beschaffung oder ein nicht näher beschriebenes Fine-Tuning macht den Betreiber nicht automatisch zum Anbieter. Die Drittel-FLOP-Orientierung in GPAI-Leitlinien betrifft die Bewertung eines geänderten Modells und begründet keine allgemeine Freistellung von Systempflichten.

#### 2.2. Parallele Pflichtspuren

Prüfen Sie Artikel 5 vor einer Nutzungsfreigabe nach dem jeweiligen vollständigen Tatbestand. Manipulation benötigt die beschriebenen Verhaltens- und Schadensvoraussetzungen; nicht jede Überzeugung ist verboten. Social Scoring ist nicht auf öffentliche Anbieter beschränkt. Medizinische oder sicherheitsbezogene Zwecke bei Emotionserkennung müssen tatsächlich belegt sein. Eine Risikoanalyse kann ein verbotenes System nicht legalisieren.

Prüfen Sie den Produktpfad nach Artikel 6 Absatz 1 mit Anhang I getrennt vom Verwendungspfad nach Absatz 2 mit Anhang III. Im Produktpfad müssen Sicherheitsbauteil-/Produktbezug und erforderliche Drittbewertung nach einschlägigem Produktrecht zusammentreffen. Absätze 1a bis 1c und die deutsche Berichtigung beachten: Eine unterstützende Funktion schließt eine sicherheitsrelevante Funktion nicht pauschal aus. Anhang I Abschnitt B, insbesondere Maschinen nach Nummer 21, unterliegt der Sonderregel des Artikels 2 Absatz 2.

Im Anhang-III-Pfad prüfen Sie die konkrete Unterkategorie: Biometrie, kritische Infrastruktur, Bildung, Beschäftigung und Selbstständigkeit, wesentliche Dienste, Strafverfolgung, Migration/Asyl/Grenzkontrolle sowie Justiz/demokratische Prozesse. Diese Überschriften allein sind keine positiven Tatbestandsfeststellungen. Erforderliche Akteure, Zwecke und Ausnahmen jeweils benennen.

Die Ausnahme des Artikels 6 Absatz 3 ist nur für den Anhang-III-Pfad vorgesehen. Belegen Sie das fehlende erhebliche Risiko für Gesundheit, Sicherheit und Grundrechte einschließlich fehlender wesentlicher Beeinflussung des Entscheidungsergebnisses sowie mindestens eine der vier Fallgruppen: eng gefasste Verfahrensaufgabe, Verbesserung eines bereits abgeschlossenen menschlichen Ergebnisses, Erkennen von Mustern oder Abweichungen unter den zusätzlichen Kontrollbedingungen oder vorbereitende Aufgabe. Profiling natürlicher Personen schließt die Ausnahme aus. Der Anbieter dokumentiert nach Absatz 4 und registriert nach Artikel 49 Absatz 2. Ein menschlicher Letztentscheider genügt allein nicht.

Prüfen Sie Artikel 50 zusätzlich nach Funktion und Rolle; ein Hochrisiko-System kann zugleich Transparenzpflichten auslösen. Unterscheiden Sie Anbieterinformation bei Interaktion, technische Kennzeichnung synthetischer Ausgaben und Betreiberinformation bei Emotions-/Biometriekategorisierung, Deepfakes und Texten zu Angelegenheiten öffentlichen Interesses. Die redaktionelle Ausnahme betrifft den dortigen Textfall. Die Bezeichnungen „begrenzt“ oder „minimal“ sind keine selbstständigen Klassen des Artikels 6 und keine allgemeine Rechtsfreigabe.

Prüfen Sie GPAI auf Modellebene. Die Vermutung nach Artikel 51 Absatz 2 knüpft an mehr als 10 hoch 25 FLOP an; Artikel 51/52 enthalten weitere Einstufungs- und Verfahrensregeln. Eine lokale Installation eines fremden Modells belegt keine eigene Modellanbieterrolle. Modellpflichten, Systempflichten und Datenschutz können nebeneinander bestehen.

#### 2.3. Folgenabschätzungen und Nachweise

Eine FRIA nach Artikel 27 betrifft die genannten öffentlichen Einrichtungen, privaten Erbringer öffentlicher Dienstleistungen und Betreiber der Systeme nach Anhang III Nummer 5 Buchstaben b/c; Nummer 2 ist ausgenommen. Öffentliche Finanzierung allein und eine beliebige private Personalabteilung erfüllen den Adressatenkreis nicht. Die DSFA nach Artikel 35 DSGVO separat begründen; einschlägige vorhandene Teile können nach Artikel 27 Absatz 4 einbezogen werden.

Artikel 9 verlangt ein konkretes lebenszyklusbezogenes Risikomanagement des Anbieters. Artikel 17 betrifft dessen Qualitätsmanagement. Ein internes Risikoregister kann Arbeitsmittel sein, ist aber nicht mit einem gesetzlich vorgeschriebenen Datenbankeintrag identisch. ISO 31000, ISO/IEC 42001 oder ISO/IEC 23894 allein belegen keine Konformität. Für Artikel 40 sind Ausgabe, Amtsblattfundstelle und Deckungsbereich nachzuweisen; Artikel 43 bestimmt den Verfahrenspfad.

#### 2.4. Zeit und Fortsetzung

Artikel 113 Buchstabe c verschiebt Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5 für Anhang III auf den 02.12.2027 und für Anhang I auf den 02.08.2028. Artikel 111 und Normen außerhalb dieser Verschiebungsformel gesondert prüfen. Weder alles bis 2028 verschieben noch jede Register-/Konformitätspflicht ohne Prüfung bereits für jeden Altbestand behaupten.

Bestehende Artikel-5-Verbote gelten seit 02.02.2025; neue Buchstaben ba/bb und Absätze 1a/1b ab 02.12.2026. Artikel 111 Absatz 4 enthält nur für Artikel 50 Absatz 2 bei erfassten generativen Alt-Systemen einen Übergang bis 02.12.2026. Artikel 4 neuer Fassung verlangt angemessene Kompetenzmaßnahmen und keine Garantie eines individuellen Niveaus oder ein bestimmtes Zertifikat.

Speichern Sie Feststellung, Beleg, offene Frage, verantwortliche Person und nächsten Schritt. Bei Versions- oder Zweckänderung öffnen Sie genau die betroffenen Weichen erneut. Ohne Beleg bleibt der Punkt offen; ein freiwilliger vorsichtiger Projektstopp ist als organisatorische Entscheidung zu kennzeichnen, nicht als erfundene gesetzliche Einstufung.

### Schritt 3: Empfehlungen

Drei nächste Schritte anbieten:
1. "Möchten Sie, dass ich die Pflichten für dieses System durcharbeite? Ich mache das im
 Gespräch – keine Tabelle."
2. "Möchten Sie `/ki-governance:ki-folgenabschaetzung` starten, um eine vollständige
 KI-Folgenabschätzung zu erstellen?"
3. "Möchten Sie ein nächstes Prüfdatum setzen? Ich füge es dem Inventar hinzu."

## Datensatzformat

```yaml
systeme:
 - id: sys-001
 name: "Lebenslauf-Screening-Tool"
 eigentuemer: "HR / Schmidt"
 beschreibung: "Filtert eingehende Lebensläufe nach Stellenkriterien"
 status: in_produktion # geplant | in_entwicklung | in_produktion | ausgemustert
 eu_nexus: true # betrieben, angeboten oder betrifft Personen in der EU/EWR
 rolle: betreiber # anbieter | betreiber | einführer | händler | bevollmächtigter | produkthersteller
 rollenbasis: "Wir lizenzieren von AnbieterX und betreiben intern; Rollenbasis im Quellenlog auf Art. 3 Nr. 4 KI-VO vermerkt"
 klasse: anhang_iii_pruefung # Anzeigefeld, keine abschließende oder exklusive Rechtsklasse
 pflichtspuren: [artikel_5, artikel_6_absatz_2_und_3, artikel_26, artikel_50]
 modellpruefung: separat
 freigabestatus: offen
 klassenbasis: "Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO – Beschäftigung, Einstellungsauswahl"
 pflichten_bewertet: false
 pflichten_hinweis: "Artikel 26 nach Rolle und Datum prüfen. Anbieterinformationen für die wirksame menschliche Aufsicht, Eingabedatenqualität, Überwachung und Protokollierung anfordern. Eine gegebenenfalls erforderliche FRIA ist Aufgabe des erfassten Betreibers, keine pauschale Lieferpflicht des Anbieters."
 art50_transparenz: "Offenlegungspflicht nach Art. 50 KI-VO gesondert prüfen und dokumentieren"
 naechste_pruefung: "2026-08-01"
 pruef_ausloeser: "bei wesentlicher Änderung oder jährlich"
 erstellt: "2026-05-18"
 aktualisiert: "2026-05-18"
```

## Quellen und Zitierweise

Prüfstand dieser KI-VO-Einordnung: 09.10.2026. [Amtlicher konsolidierter Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727).

Verbindliche Zitierweise gemäß `../references/zitierweise.md`.

**Leitende Normen:**
- Art. 3 Nr. 3, 4, 5, 6, 7 KI-VO (VO 2024/1689) – Definitionen `[Primärquelle – EUR-Lex]`
- Art. 5 KI-VO – Verbotene Praktiken `[Primärquelle – EUR-Lex]`
- Art. 6 KI-VO i.V.m. Anhang III – Hochrisiko-KI-Systeme `[Primärquelle – EUR-Lex]`
- Art. 14, 16, 26 KI-VO – Betreiber- und Anbieterpflichten `[Primärquelle – EUR-Lex]`
- Art. 27 KI-VO – Folgenabschätzung für Grundrechte (FRIA) `[Primärquelle – EUR-Lex]`
- Art. 50 KI-VO – Transparenzpflichten `[Primärquelle – EUR-Lex]`
- Art. 99 KI-VO – Bußgeldrahmen `[Primärquelle – EUR-Lex]`

## Beispiel

```
/ki-governance:ki-inventar classify sys-001
```

> **Klassifizierungsdurchlauf – sys-001: Lebenslauf-Screening-Tool**
>
> **Schritt 1: Rolle**
> Sie lizenzieren das System von VendorX und setzen es intern für HR ein. Sie bestimmen den
> Verwendungszweck und tragen die operative Verantwortung → **Betreiber** nach Art. 3 Nr. 4
> KI-VO.
> Rollenbasis: "Lizenziertes System von VendorX, interner Betrieb durch HR-Team."
>
> **Schritt 2: Risikoklasse**
> Kein Treffer in Art. 5 (kein Verbot erkennbar).
> Anhang III Nr. 4 lit. a: KI-Systeme für Einstellung, Auswahl, Beförderung → **hochrisiko**
> Klassenbasis: "Anhang III Nr. 4 lit. a KI-VO – Einstellungsauswahl."
>
> **Empfehlungen:**
> 1. Pflichten als Betreiber eines hochriskanten Systems durcharbeiten? (Art. 26, 14 KI-VO)
> 2. KI-Folgenabschätzung erstellen? `/ki-governance:ki-folgenabschaetzung`
> 3. Nächstes Prüfdatum: 2027-05-18 (Jahresprüfung)?

## Risiken / typische Fehler

- **Stille Klassifizierung.** Klassifizierungsdurchlauf muss sichtbar sein; kein Auto-Klassifizieren
 aus einer Systembeschreibung.
- **Quellenbasis unterschlagen.** Artikel, Anhangspunkt und Prüfdatum gehören in die Ausgabe;
 keine bloßen Bauchklassifikationen ohne Normanker.
- **Wesentliche Änderung ignorieren.** Wenn ein System über die Konfiguration hinaus geändert
 wird, `/ki-inventar classify` erneut ausführen – Änderungen können die Rolle verschieben.
- **Pflichten aus Tabelle ableiten.** Bei Anfragen die Analyse im Gespräch durchführen und
 an `/ki-folgenabschaetzung` für alles weiterleiten, das einen formellen Nachweis benötigt.
- **Sanktionen konkret prüfen:** Artikel 99 nach tatsächlich verletzter Pflicht und Unternehmensgröße anwenden. Eine allgemeine Inventarlücke begründet nicht automatisch den Höchstrahmen für verbotene Praktiken.

## Zentrale Normen (Paragrafenkette)
- Artikel 6 Absatz 1 mit Anhang I, Absätze 1a bis 1c sowie Absatz 2 mit Anhang III und Ausnahme Absatz 3 getrennt prüfen. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber Definitionen
- Art. 16 ff. KI-VO — Anbieterpflichten (technische Dokumentation, Konformitaetsbewertung)
- Art. 26 KI-VO — Betreiberpflichten (menschliche Aufsicht, Protokollierung)
- Artikel 99 KI-Verordnung — tatbestandsbezogene Sanktionsrahmen und Sonderregeln der Absätze 6/6a

## Triage zu Beginn
1. Ist das Inventar bereits vorhanden oder wird es neu angelegt?
2. Welche Systeme sind bereits produktiv — und wurden diese nach KI-VO klassifiziert?
3. Hat das Unternehmen EU-Nexus für jedes System (Betreiber/Anbieter in der EU)?
4. Sind Hochrisiko-Systeme (Anhang III Nr. 1-8) im Inventar — welche Betreiberpflichten (Art. 26 KI-VO) greifen?
5. Ist für jedes System ein Systemeigentuemer benannt?

## Output-Template — KI-System-Inventar
**Adressat:** KI-Governance-Verantwortlicher — Tonfall: strukturiert-tabellarisch
```
KI-SYSTEM-INVENTAR
[UNTERNEHMEN / NAME MANDANT] — Stand: [DATUM]

| ID | System | Eigentuemer | Status | EU-Nexus | Rolle | Risikoklasse | Naechste Pruefung |
|---|---|---|---|---|---|---|---|
| sys-001 | [SYSTEM] | [NAME] | in_produktion | ja | Betreiber | [KLASSE] | [DATUM] |
| sys-002 | [SYSTEM] | [NAME] | pilotbetrieb | nein | Anbieter | [KLASSE] | [DATUM] |

ZUSAMMENFASSUNG:
- Hochrisiko (Art. 6 i.V.m. Anhang III): [ANZAHL] Systeme
- Transparenzpflichten zusätzlich geprüft: [ANZAHL] Funktionen
- Weitere Einstufung noch offen: [ANZAHL] Funktionen
- Systeme zur Pruefung in 30 Tagen: [ANZAHL]

AUSSTEHENDE PFLICHTEN:
- [SYSTEM-ID]: [PFLICHT — Art. X KI-VO — Frist: DATUM]

Stand: [DATUM] — Naechste Vollpruefung: [DATUM]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
