---
name: verspaetung-ticket-fluginformationen
description: "Verspaetung Ticket Fluginformationen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verspaetung Ticket Fluginformationen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verspaetung Ticket Fluginformationen** im Plugin Fluggastrechte (VO 261/2004). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-verspaetung-verhandlung-vergleich-und-eskalation` | Verspaetung: Verhandlung, Vergleich und Eskalation im Plugin fluggastrechte; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `ticket-und-fluginformationen-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpaesse PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankunftszeit Tarifklasse Passagiernamen ausführendes Luftfahrtunternehmen (Operating Carrier) vermarktendes (Code-Share). Ergaenzt manuell die Ist-Zeiten (taktsaechliche Abflug- und Ankunftszeit) und das Stoerungsereignis (Annullierung Verspaetung Nichtbefoerderung Umbuchung). Erzeugt Fallakte. |
| `vollmacht-familienmitglieder` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene Vollmacht mit Inhalt Bezug auf Buchung Mandatsumfang Empfangsvollmacht Untervollmacht. Bei minderjaehrigen Kindern Sondervorlage mit Erziehungsberechtigten. Datenschutzhinweis. Versandentwurf an die Mitreisenden zur Unterschrift. |

## Arbeitsweg

Im Plugin Fluggastrechte (VO 261/2004) gilt für **Verspaetung Ticket Fluginformationen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-verspaetung-verhandlung-vergleich-und-eskalation`

**Fokus:** Verspaetung: Verhandlung, Vergleich und Eskalation im Plugin fluggastrechte; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Verspaetung: Verhandlung, Vergleich und Eskalation

## Spezialwissen: Verspaetung: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** Verspaetung: Verhandlung, Vergleich und Eskalation / verspaetung verhandlung vergleich und eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VO, EG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verspaetung** prüfen.
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

## 2. `ticket-und-fluginformationen-erfassen`

**Fokus:** Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpaesse PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankunftszeit Tarifklasse Passagiernamen ausführendes Luftfahrtunternehmen (Operating Carrier) vermarktendes (Code-Share). Ergaenzt manuell die Ist-Zeiten (taktsaechliche Abflug- und Ankunftszeit) und das Stoerungsereignis (Annullierung Verspaetung Nichtbefoerderung Umbuchung). Erzeugt Fallakte.

# Ticket- und Fluginformationen erfassen

## Eingaben

Was hochgeladen werden kann:

- **Buchungsbestätigung** als PDF / E-Mail.
- **E-Ticket** mit IATA-Standard-Konfiguration.
- **Boardingpass** Foto oder PDF.
- **Störungsbenachrichtigung** von der Airline.
- **Korrespondenz** mit der Airline (E-Mail-Verlauf).
- **Pauschalreiseunterlagen** falls Buchung über Reiseveranstalter.

## Pflichtfelder

Zu jedem Flugabschnitt:

```yaml
fall-id: FG-2026-0042
reisedatum: 2026-05-12
passagiere:
 - name: Mueller, Hans
 geburtsdatum: 1972-08-15
 rolle: hauptbuchender
 - name: Mueller, Eva
 geburtsdatum: 1975-03-22
 rolle: ehepartner
 - name: Mueller, Lea
 geburtsdatum: 2010-06-18
 rolle: minderjährig

buchungscode: ABC123 # PNR
buchung-bei: Lufthansa # vermarktende Airline
buchungsdatum: 2026-04-12

flug:
 flugnummer: LH 1234 # Code des operating carrier
 operating-carrier: Lufthansa
 marketing-carrier: Lufthansa
 abflughafen: MUC (München)
 zielflughafen: LIS (Lissabon)
 geplante-abflugzeit: 2026-05-12T08:25:00+02:00
 geplante-ankunftszeit: 2026-05-12T11:00:00+01:00
 tatsaechliche-abflugzeit: null
 tatsaechliche-ankunftszeit: null
 flugklasse: economy
 distanz-km: 2280 # Skill `distanz-und-ausgleich-berechnen`

stoerung:
 art: annullierung # annullierung / verspätung / nichtbefoerderung / umbuchung / abweichender-flug
 bekanntgabe-am: 2026-05-12T06:30:00+02:00
 bekanntgabe-wie: SMS # SMS / E-Mail / Schalter-Mitteilung
 begruendung-airline: technischer Defekt
 ersatzangebot: Flug am 13.05.2026 LH 1234
 ersatz-tatsaechlich-genutzt: ja

belege:
 - typ: buchungsbestätigung
 pfad: belege/2026-05-12/buchung-LH1234.pdf
 - typ: boardingpass
 pfad: belege/2026-05-12/boardingpass-mueller.pdf
 - typ: stoerungsbenachrichtigung
 pfad: belege/2026-05-12/sms-annullierung.png
 - typ: ersatzboardingpass
 pfad: belege/2026-05-13/boardingpass-mueller-ersatz.pdf
```

## OCR / PDF-Extraktion

- Bei PDF-Tickets automatische Extraktion von PNR Flugnummer Datum und Flughaefen.
- Bei Foto-Belegen OCR; bei Konfidenz unter 90 Prozent Prüfer-Flag für manuelle Bestätigung.
- IATA-Codes (LH BA AF AZ) und Flughafen-Codes (FRA MUC CDG MAD) gegen Standardlisten validieren.

## Datenabgleich öffentliche Quellen

- **Flugplandaten** geplante Zeiten aus Buchungsbestätigung — autoritativ.
- **Ist-Zeiten** können Sie aus Boardingpass-Stempel SMS / E-Mail mit Verspätungs-Hinweis Flughafen-Anzeigetafel-Foto oder Airline-Verspätungs-API entnehmen.
- Verbraucher-relevante öffentliche Datenquellen sind regelmäßig **zahlungspflichtig oder nicht autoritativ** (FlightAware FlightRadar24 etc.); im Streit beweisbedeutsam ist die **Eingangsbestätigung der Airline** und die offizielle **Verspätungs-/Annullierungsmeldung** der Airline.
- Bei strittiger Ist-Zeit: Empfehlung **eigenhändige Dokumentation am Tag des Ereignisses** (Fotos Anzeigentafel SMS-Eingaenge) als späterer Beweis.

## Leitentscheidungen Informationserfassung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

- `fallakte.yaml` mit allen Stammdaten.
- `belegliste.md` mit Prüfer-Flags für fehlende Belege.
- `naechste-schritte.md` Empfehlung auf nächsten Skill (`annullierung-oder-verspaetung-einordnen`).

## Mehrere Passagiere

Pro Flug wird **ein** Anspruchsfall mit mehreren Passagieren erfasst. Jeder Passagier hat aber einen **eigenen Ausgleichsanspruch** (Art. 7 VO 261/2004 ist persönlich). Daher bei der Klage je Passagier eigener Antrag (Streitgenossenschaft möglich). Vollmacht der Mitreisenden falls einer für alle vorgeht — Skill `vollmacht-familienmitglieder`.
<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Tatsächliches Thema laut dejure.org: Pešková und Peška/Travel Service – Vogelschlag als außergewöhnlicher Umstand i.S.v. Art. 5 Abs. 3 VO 261/2004.
Aktion: Eintrag mit korrektem Thema und Fundstelle EU:C:2017:342 ersetzt.
-->

## 3. `vollmacht-familienmitglieder`

**Fokus:** Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene Vollmacht mit Inhalt Bezug auf Buchung Mandatsumfang Empfangsvollmacht Untervollmacht. Bei minderjaehrigen Kindern Sondervorlage mit Erziehungsberechtigten. Datenschutzhinweis. Versandentwurf an die Mitreisenden zur Unterschrift.

# Vollmacht für Familienmitglieder und Mitreisende

## Zweck

Wenn mehrere Personen unter einer gemeinsamen Buchung gestoert wurden hat **jeder** einen eigenen Anspruch aus Art. 7 VO 261/2004. Damit der Hauptansprechpartner alle Anspruechen gebearbeitet verfolgen kann braucht es Vollmachten der Mitreisenden.

## Vollmacht-Inhalt

```
Vollmacht

Ich, [Vor- und Nachname Vollmachtgeber],
geboren am [Geburtsdatum],
wohnhaft [Adresse],

bevollmaechtige hiermit

 [Vor- und Nachname Vollmachtnehmer],
 geboren am [Geburtsdatum],
 wohnhaft [Adresse],

mich in allen Angelegenheiten betreffend meine Anspruechen aus dem Flug

 Buchungscode (PNR): [PNR]
 Flugnummer: [Flugnummer]
 Datum: [Datum]
 Strecke: [Abflughafen] nach [Zielflughafen]
 Operating Carrier: [Airline]

zu vertreten. Die Vollmacht umfasst insbesondere:

 - Vorgerichtliche Geltendmachung der Ausgleichsanspruechen nach
 VO (EG) Nr. 261/2004 gegenüber der Airline
 - Korrespondenz mit der Airline und ihrer Kundenservice
 - Anrufung der Schlichtungsstelle Luftverkehr SOEP
 - Klageerhebung beim zuständigen Amtsgericht
 - Empfangnahme von Zahlungen und Schriftverkehr
 - Untervollmacht an einen Rechtsanwalt sowie Vertretung im Rechtsstreit

Diese Vollmacht gilt bis zum Widerruf in Textform.

Ort Datum
___________

___________________________________________
[Vor- und Nachname Vollmachtgeber]
```

## Vollmacht für Minderjährige

Bei minderjährigen Mitreisenden ist die Vollmacht durch die erziehungsberechtigten Personen zu erteilen (regelmäßig beide Elternteile gemeinsam, sofern beide sorgeberechtigt — § 1626 BGB):

```
Vollmacht für minderjähriges Kind

Wir, die Erziehungsberechtigten

 [Name Mutter / Vater 1], [Geburtsdatum], [Adresse]
 [Name Vater / Mutter 2], [Geburtsdatum], [Adresse]

vertreten unser minderjähriges Kind

 [Vor- und Nachname Kind], [Geburtsdatum]

und bevollmaechtigen hiermit

 [Vor- und Nachname Vollmachtnehmer]

in dessen Namen die Anspruechen aus dem Flug [PNR / Flugnummer / Datum]
nach VO (EG) Nr. 261/2004 geltend zu machen — einschließlich vorgerichtlich,
SOEP und gerichtlich.

Ort Datum
___________

___________________________________________ ___________________________________________
[Mutter / Vater 1] [Vater / Mutter 2]
```

## Datenschutzhinweis (Art. 13 DSGVO)

Bei der Verarbeitung der personenbezogenen Daten der Mitreisenden ist Hinweis auf den Verantwortlichen (Hauptansprechpartner), Zweck der Verarbeitung (Geltendmachung Anspruchsverlauf), Empfänger (Airline Schlichtungsstelle Gericht) und Speicherdauer (bis zur Anspruchsbefriedigung plus Aufbewahrungspflichten) zu geben.

## Versand der Vollmachten

```
Vorlage E-Mail an Mitreisende

Liebe(r) [Name],

beigefuegt findest Du den Entwurf einer Vollmacht in Sachen unseres
annullierten / verspäteten Flugs [Flugnummer] vom [Datum].

Bitte unterschreiben und mir zurückschicken (per Post Foto oder Scan).
Damit kann ich Deinen Ausgleichsanspruch von [X] EUR zusammen mit den
anderen geltend machen — ohne dass Du selbst etwas tun musst.

Ich melde mich sobald die Airline reagiert.

Liebe Grüße
[Name]
```

## Aktenablage

- Originale (oder Scans hoher Qualität) sind Pflichtanlagen jedes Schriftverkehrs.
- Aufbewahrung bis Anspruchsabwicklung plus drei Jahre (Verjährung).
- Datenschutz beachten — keine unnoetige Weiterleitung.

## Leitentscheidungen Vollmacht / Familienvertretung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

- `vollmacht-<name>-<datum>.docx` pro Mitreisendem.
- Vollmacht-Versandliste mit Status (versendet / unterschrieben / vorliegt).
- Hinweis: Eingang der unterschriebenen Vollmachten ist Voraussetzung für die Mitvertretung.
