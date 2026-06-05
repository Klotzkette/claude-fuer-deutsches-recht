---
name: mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation, Redteam Qualitygate, Jveg Fristen Erloeschen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Mandantenkommunikation, Redteam Qualitygate, Jveg Fristen Erloeschen

## Arbeitsbereich

Dieser Skill bündelt **Mandantenkommunikation, Redteam Qualitygate, Jveg Fristen Erloeschen** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin jveg-kostenpruefer: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin jveg-kostenpruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `jveg-fristen-erloeschen` | Antragsfristen nach JVEG prüfen: drei Monate Ausschlussfrist für Verguetungsantrag. Normen: § 2 Abs. 1 JVEG. Prüfraster: Fristbeginn, Fristende, Wiedereinsetzungsmöglichkeit. Output: Fristenprüfung JVEG mit Empfehlung. Abgrenzung: nicht materiell-rechtliche Verguetungsberechnung. |

## Arbeitsweg

Für **Mandantenkommunikation, Redteam Qualitygate, Jveg Fristen Erloeschen** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `jveg-kostenpruefer` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin jveg-kostenpruefer: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin jveg-kostenpruefer: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## JVEG-Kommunikation an Mandanten und Sachverständige
- **Kostenrisiko erklären:** Sachverständigenkosten sind Gerichtskosten (§ 1 GKG iVm § 6 JVEG); bei vorgängigem Vorschuss § 17 GKG für Vorschusspflicht des Antragstellers.
- **Erfolgsfall:** Erstattungsfähigkeit JVEG-Kosten nach § 91 ZPO (notwendige Kosten der zweckentsprechenden Rechtsverteidigung); bei Streitwerttreiber Sachverständiger frühzeitig hinweisen.
- **Sachverständige als Auftragnehmer:** Auf Honorargruppen-Einordnung achten (M1/M2/M3); bei Streit Beweisbeschluss zitieren.
- **Frist klar kommunizieren:** § 2 Abs. 1 JVEG drei Monate ab Auftragsbeendigung — Mandant/Sachverständiger informieren, sonst Anspruchsverlust.
- **Vorschuss-Antrag:** § 12 JVEG erleichtert bei wirtschaftlich schwacher Lage des Sachverständigen; Antrag mit Zeitschätzung und Aufgabenbeschreibung.
- Falle: Stundensatz aus Privatauftrag wird gegenüber Mandant als JVEG-Honorar dargestellt — Differenz zwischen Privat- und Gerichts-Sachverständigem ist erstattungsrechtlich nicht erstattbar.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin jveg-kostenpruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieser Arbeitsmodul prüft die fertige JVEG-Kostenfestsetzung gegen typische Fehlerquellen: Honorargruppen-Fehlzuordnung, Stundenzahl-Inplausibilität, Wegegeld-Doppelung, fehlende Belege, Umsatzsteuer-Klippe (§ 12 JVEG).

## JVEG-spezifische Prüfpunkte
- **Honorargruppe nachvollziehbar?** Anlage 1 JVEG: Gruppen 1 bis 12. Begründung im Beschluss vorhanden? (BVerwG, Beschl. v. 31.05.2022 - 9 KSt 1.22 zur Bindung an Heranziehung.)
- **Stundensatz korrekt?** § 9 Abs. 1 JVEG: aktuelle Sätze laut KostRÄG-Stand prüfen unter `gesetze-im-internet.de/jveg`.
- **Zeitaufwand erforderlich?** § 8 Abs. 2 JVEG: nur notwendiger Zeitaufwand vergütungsfähig. Reine Wartezeit nur unter § 19 JVEG.
- **Auslagen belegt?** § 5 JVEG (Fahrt: 0,42 EUR/km Pkw oder BC100), § 6 JVEG (Tage-/Übernachtungsgeld), § 7 JVEG (Schreibauslagen).
- **Umsatzsteuer:** § 12 JVEG (Ust nur bei Steuerpflicht des SV; nicht bei Kleinunternehmer § 19 UStG).
- **Pauschalvereinbarung:** § 13 JVEG nur mit Zustimmung des Sachverständigen und schriftlich.
- **Frist Erinnerung:** § 4 Abs. 1 JVEG -- sechs Monate ab Bekanntgabe der Festsetzung; ohne Aufschub.
- Falle: Vergleich von Stundensätzen aus alten Beschlüssen (vor KostRÄG 2021/2022) ohne Hinweis auf aktuelle Fassung.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `jveg-fristen-erloeschen`

**Fokus:** Antragsfristen nach JVEG prüfen: drei Monate Ausschlussfrist für Verguetungsantrag. Normen: § 2 Abs. 1 JVEG. Prüfraster: Fristbeginn, Fristende, Wiedereinsetzungsmöglichkeit. Output: Fristenprüfung JVEG mit Empfehlung. Abgrenzung: nicht materiell-rechtliche Verguetungsberechnung.

# JVEG-Fristen-Erloeschen

## Fachkern: JVEG-Fristen-Erloeschen
- **Spezialgegenstand:** JVEG-Fristen-Erloeschen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe, ob JVEG-Vergütungsansprüche fristgerecht geltend gemacht wurden, und bewerte Risiken des Anspruchserlöschens nach § 23 JVEG.

## Triage — kläre vor der Prüfung

1. **Leistungsdatum:** Wann wurde die anspruchsbegründende Leistung erbracht (Beginn der Dreimonatsfrist)?
2. **Geltendmachungsdatum:** Wann wurde der Antrag beim Gericht eingereicht?
3. **Belehrung:** Wurde der Anspruchsberechtigte über die Dreimonatsfrist belehrt (§ 23 Abs. 1 S. 3 JVEG)?
4. **Wiedereinsetzung:** Liegen Hindernisse vor, die eine Wiedereinsetzung in den vorigen Stand rechtfertigen?
5. **Verjährung:** Wurde die dreijährige Regelverjährung (§ 195 BGB) berücksichtigt, soweit § 23 JVEG nicht greift?

## Zentrale Normen
- § 23 JVEG (Dreimonatsfrist / Erlöschen)
- § 23 Abs. 1 S. 3 JVEG (Belehrungspflicht des Gerichts)
- § 2 JVEG (Anspruchsberechtigte)
- § 195 BGB (Regelverjährung — subsidiär)
- § 233 ff. ZPO (Wiedereinsetzung in den vorigen Stand — analog)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Jeder JVEG-Vorgang, bei dem Zeitpunkt der Leistungserbringung und Antragstellung bekannt sind.

## Arbeitsweise
1. Leistungsdatum und Antragsdatum gegenüberstellen.
2. Dreimonatsfrist nach § 23 JVEG berechnen.
3. Belehrungsdokumentation prüfen.
4. Wiedereinsetzungspotenzial bewerten.
5. Fristennotiz für Akte erstellen.

## Output-Template

| Kriterium | Befund |
|---|---|
| Leistungserbringung | TT.MM.JJJJ |
| Fristende § 23 JVEG | TT.MM.JJJJ |
| Antrag eingereicht | TT.MM.JJJJ |
| Frist gewahrt | Ja / Nein |
| Belehrung erteilt | Ja / Nein / Unklar |
| Wiedereinsetzungsrisiko | [Gering / Mittel / Hoch] |
| Empfehlung | [Antrag stellen / Wiedereinsetzung prüfen / Anspruch erloschen] |

## Ausgabe
Fristennotiz mit Risikoeinschätzung und Handlungsempfehlung.

## Leitplanken
- Dreimonatsfrist ist absolut; keine Kulanzregelung ohne Wiedereinsetzung.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
