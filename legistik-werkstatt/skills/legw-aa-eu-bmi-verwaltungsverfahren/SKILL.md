---
name: legw-aa-eu-bmi-verwaltungsverfahren
description: "Legw AA EU BMI Verwaltungsverfahren: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Legw AA EU BMI Verwaltungsverfahren

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Legw AA EU BMI Verwaltungsverfahren** im Plugin Legistik Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `legw-aa-eu-grundlagen-und-ratsverfahren` | Sachbereich EU-Grundlagen und Ratsverfahren im Geschaeftsbereich AA: Normbestand (EUV; AEUV; EUZBLG; EUZBBG; Lissabon-Begleitgesetzgebung.); Akteure (AA Europa-Abteilung; Bundeskanzleramt EU-Koordinator; Bundesministerien.); EU-Bezug (Rat der EU; Ratsformationen; AStV; Trilog mit Parlament und Kommission.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-aa (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-aa (Heranfuehrung). |
| `legw-bmi-verwaltungsverfahren-und-bundesverwaltung` | Sachbereich Verwaltungsverfahren und Bundesverwaltung im Geschaeftsbereich BMI: Normbestand (VwVfG; VwGO; IFG; UIG (mit BMUKN); BVerwGG; BBG; BeamtStG.); Akteure (Bundesbehoerden des allgemeinen Verwaltungsrechts; BVerwG.); EU-Bezug (EU-Verwaltungsverfahren; Single Digital Gateway.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmi (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmi (Heranfuehrung). |
| `legw-gesetzgebungsverfahren-bauleiter` | Bauleiter Gesetzgebungsverfahren Bund: Referentenentwurf, Kabinettsbeschluss, Bundesrat, Bundestag. Pruefraster fuer Verbandsstellungnahme. |
| `spezial-bundestag-fristen-form-und-zustaendigkeit` | Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Legw AA EU BMI Verwaltungsverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `legw-aa-eu-grundlagen-und-ratsverfahren`

**Fokus:** Sachbereich EU-Grundlagen und Ratsverfahren im Geschaeftsbereich AA: Normbestand (EUV; AEUV; EUZBLG; EUZBBG; Lissabon-Begleitgesetzgebung.); Akteure (AA Europa-Abteilung; Bundeskanzleramt EU-Koordinator; Bundesministerien.); EU-Bezug (Rat der EU; Ratsformationen; AStV; Trilog mit Parlament und Kommission.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-aa (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-aa (Heranfuehrung).


# EU-Grundlagen und Ratsverfahren (AA)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema EU-Grundlagen und Ratsverfahren im Geschaeftsbereich AA. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-aa`
- Aufgabenmatrix aus `legw-ressortaufgaben-aa`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: EUV; AEUV; EUZBLG; EUZBBG; Lissabon-Begleitgesetzgebung.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

AA Europa-Abteilung; Bundeskanzleramt EU-Koordinator; Bundesministerien.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

Rat der EU; Ratsformationen; AStV; Trilog mit Parlament und Kommission.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Ratsverfahren absichern; deutsche Position abstimmen; Subsidiaritaetsruege; Bundestag und Bundesrat nach Art. 23 GG informieren.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Versaeumte Konsultationen; Subsidiaritaetsruege-Frist; Trilog-Ergebnisse ohne nationale Mitwirkung.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld: EU-Grundlagen und Ratsverfahren
Ressort: AA
Kernnormen: EUV; AEUV; EUZBLG; EUZBBG; Lissabon-Begleitgesetzgebung.
Akteure/Aufsicht: AA Europa-Abteilung; Bundeskanzleramt EU-Koordinator; Bundesministerien.
EU/Voelkerrecht: Rat der EU; Ratsformationen; AStV; Trilog mit Parlament und Kommission.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-aa; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-aa` -> `legw-ressortaufgaben-aa` -> `legw-aa-eu-grundlagen-und-ratsverfahren` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 2. `legw-bmi-verwaltungsverfahren-und-bundesverwaltung`

**Fokus:** Sachbereich Verwaltungsverfahren und Bundesverwaltung im Geschaeftsbereich BMI: Normbestand (VwVfG; VwGO; IFG; UIG (mit BMUKN); BVerwGG; BBG; BeamtStG.); Akteure (Bundesbehoerden des allgemeinen Verwaltungsrechts; BVerwG.); EU-Bezug (EU-Verwaltungsverfahren; Single Digital Gateway.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmi (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmi (Heranfuehrung).


# Verwaltungsverfahren und Bundesverwaltung (BMI)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Verwaltungsverfahren und Bundesverwaltung im Geschaeftsbereich BMI. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmi`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmi`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: VwVfG; VwGO; IFG; UIG (mit BMUKN); BVerwGG; BBG; BeamtStG.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

Bundesbehoerden des allgemeinen Verwaltungsrechts; BVerwG.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

EU-Verwaltungsverfahren; Single Digital Gateway.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Verfahrensschritte; Anhoerungspflichten; Begruendungspflicht; Verwaltungsakt; Bekanntgabe; elektronischer Verwaltungsakt.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Anhoerungsmangel; fehlerhafte Ermessensausuebung; Drittwirkung; Vollstreckung von Verwaltungsakten.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld: Verwaltungsverfahren und Bundesverwaltung
Ressort: BMI
Kernnormen: VwVfG; VwGO; IFG; UIG (mit BMUKN); BVerwGG; BBG; BeamtStG.
Akteure/Aufsicht: Bundesbehoerden des allgemeinen Verwaltungsrechts; BVerwG.
EU/Voelkerrecht: EU-Verwaltungsverfahren; Single Digital Gateway.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-bmi; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmi` -> `legw-ressortaufgaben-bmi` -> `legw-bmi-verwaltungsverfahren-und-bundesverwaltung` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 3. `legw-gesetzgebungsverfahren-bauleiter`

**Fokus:** Bauleiter Gesetzgebungsverfahren Bund: Referentenentwurf, Kabinettsbeschluss, Bundesrat, Bundestag. Pruefraster fuer Verbandsstellungnahme.


# LegW: Gesetzgebungsverfahren

## Aufgabe
Bauleiter Gesetzgebungsverfahren Bund: Referentenentwurf, Kabinettsbeschluss, Bundesrat, Bundestag.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster Gesetzgebungsverfahren Bund

### 1. Initiativrecht (Art. 76 I GG)

- **Bundesregierung** (regelmäßig häufigster Initiator).
- **Bundestag** (aus seiner Mitte; Fraktion oder Anzahl Abgeordneter nach GO-BT).
- **Bundesrat**.

### 2. Vorbereitungsphase (Bundesregierung)

1. **Ressortabstimmung**: federführendes BMI / BMJ / Fachressort erarbeitet Referentenentwurf nach **GGO** (Gemeinsame Geschäftsordnung der Bundesministerien).
2. **Verbändeanhörung** § 47 III GGO: Anhörung der Verbände und Länder vor Kabinettsbefassung; Stellungnahmefrist regelmäßig 4-6 Wochen.
3. **NKR-Prüfung** § 4 NKRG: Nationaler Normenkontrollrat prüft Erfüllungsaufwand vor Kabinettsbefassung.
4. **Ressortbeteiligung**: Mitprüfung durch alle Ressorts, Konsultation BMJ (Rechtsförmlichkeitsprüfung).
5. **Kabinettsbeschluss**: Bundesregierung beschließt Entwurf.

### 3. Erster Durchgang Bundesrat (Art. 76 II GG)

- Sechs Wochen Stellungnahmefrist (bei besonderer Eilbedürftigkeit drei Wochen).
- Stellungnahme mit Empfehlungen oder Bedenken.
- Bundesregierung übermittelt Entwurf mit Stellungnahme und Gegenäußerung an Bundestag.

### 4. Bundestag (Art. 77 I, 78 GG)

- **Erste Lesung**: Aussprache, Überweisung an federführenden Ausschuss.
- **Ausschussberatungen**: Anhörungen Sachverständige (oft öffentlich), Beratung, Beschlussempfehlung.
- **Zweite Lesung**: Detailberatung; Änderungsanträge.
- **Dritte Lesung**: Schlussabstimmung; einfache Mehrheit der abgegebenen Stimmen (Art. 42 II GG).
- Bei Verfassungsänderung: 2/3-Mehrheit Art. 79 II GG.

### 5. Zweiter Durchgang Bundesrat

- **Einspruchsgesetz** Art. 77 III GG: BR kann Einspruch einlegen; BT kann mit Mehrheit zurückweisen (Art. 77 IV GG).
- **Zustimmungsgesetz** Art. 77 IIa, 84 I 6 GG: BR muss zustimmen; ohne Zustimmung gescheitert.
- **Vermittlungsausschuss** Art. 77 II GG: bei Streit BT / BR; berät Kompromiss.

### 6. Ausfertigung und Verkündung (Art. 82 GG)

- **Gegenzeichnung** Bundeskanzler und zuständiger Minister.
- **Ausfertigung** Bundespräsident.
- **Verkündung** im BGBl.
- **Inkrafttreten** wie im Gesetz bestimmt; mangels Bestimmung 14. Tag nach Verkündung Art. 82 II 2 GG.

## Verbandsstellungnahme — Strategische Hinweise

- **Frist** (regelmäßig 4-6 Wochen ab Übersendung Referentenentwurf): rechtzeitig planen.
- **Adressat**: federführendes Ministerium.
- **Form**: schriftlich (Brief, E-Mail) und durchnummeriert auf Paragraphen / Sätze.
- **Inhalt**:
 - Konkrete Formulierungsvorschläge (statt nur Kritik).
 - Folgenabschätzung: Erfüllungsaufwand, KMU-Belastung, Umsetzungspraxis.
 - Rechtsförmlichkeitsprüfung (Handbuch der Rechtsförmlichkeit HdR).
 - Vergleich zu EU-Vorgaben (Goldplating-Vermeidung).
- **Eskalationspunkte** identifizieren: Welche Punkte sind politisch verhandelbar, welche nicht?
- **Verbündete** suchen: Kontakt zu anderen Verbänden / Mitgliedsunternehmen / Bundesländern.

## Quellen für Materialien

- **Bundestag**: bundestag.de/Drucksachen; Tagesordnung; Ausschussprotokolle.
- **Bundesrat**: bundesrat.de; Bundesratsdrucksachen.
- **BMI / BMJ**: Referentenentwurf vor Kabinettsbeschluss auf Ministeriumshomepage.
- **NKR**: normenkontrollrat.bund.de mit Stellungnahmen zu Erfüllungsaufwand.
- **EU-Bezug**: EUR-Lex; Mitwirkung des Bundestages nach Art. 23 GG.

## Praxisfallen

- **Zustimmungserfordernis** unterschätzt: bei Eingriff in Verwaltungsverfahren der Länder (Art. 84 I 6 GG) Zustimmungspflicht.
- **Lobbyregister-Pflicht**: Verbandsstellungnahmen sind Interessenvertretung; § 3 LobbyRG-Pflicht prüfen.
- **EU-Notifizierungspflicht** RL 2015/1535 bei technischen Vorschriften: 3 Monate Stillhaltefrist; Versäumnis = Unanwendbarkeit der Norm.
- **Sachverständigenanhörung** Bundestag: Vorbereitung schriftlicher Stellungnahme (10-15 Seiten); rechtzeitig Einladung anfordern.
- **Kabinettsbeschluss ist Wendepunkt**: vorher relativ flexibel, nachher Änderung nur über Bundestag.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 4. `spezial-bundestag-fristen-form-und-zustaendigkeit`

**Fokus:** Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.


# Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg / bundestag fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** XML.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bundestag** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
