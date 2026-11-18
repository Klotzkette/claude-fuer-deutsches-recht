---
name: schlussbericht-erstellen
description: Erstellt den ausformulierten Schlussbericht eines Insolvenzverfahrens. Prüft Abschlussreife, erklärt Verlauf, Masse, Verwertung, Forderungen, Kosten, Prozesse und Restpositionen und stimmt den Text mit Rechnung und Verteilung ab.
---

# Schlussbericht erstellen

## 1. Zweck und Anwendungsfall

Dieser Skill erstellt den erzählenden und rechtlich eingeordneten Schlussbericht. Er wird erst nach einer dokumentierten Abschlussreifeprüfung verwendet oder liefert ausdrücklich einen Entwurf mit den noch fehlenden Abschlussvoraussetzungen. Er erklärt, was im Verfahren geschehen ist, welche wirtschaftlichen Ergebnisse erzielt wurden und welche Restpunkte rechtlich behandelt werden.

Der Schlussbericht bleibt von Schlussrechnung, Schlussverzeichnis, Vergütungsantrag und Verteilungsrechnung getrennt. Er verweist auf diese Produkte und übernimmt nur Werte aus derselben freigegebenen Stichtagsfassung.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-SB`. Die Fachroute übergibt an `schlussrechnung-konten-abgleichen`, sämtliche Fachmodule und `berichtserstellung-steuern`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Abschlussreife | vollständige Matrix zu Masse, Betrieb, Steuern, Prozessen und Verteilung | BER-CTRL |
| Verfahrensverlauf | Beschlüsse, Berichte und Maßnahmenchronologie | Gerichts- und Kanzleiakte |
| Fachmodule | BER-MV, BER-FQ, BER-SKV und BER-PAH | freigegebene Stichtagsfassungen |
| Rechnung | BER-SR mit erklärtem Null- oder Restbestand | Kontenabgleich |
| Verteilung | Entwurf des Schlussverzeichnisses und Quotenrechnung | BER-FQ und BER-SVA |
| Vorgaben | gerichtliche Verfügung, Hausformat und Anlagenanforderung | konkrete Verfahrensakte |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Abschlussstichtag und Veränderungsprotokoll

Legen Sie einen Abschlussstichtag fest, den `BER-SB`, `BER-SR`, `BER-FQ` und die Abschlussreifematrix gemeinsam verwenden. Für jeden Fachbereich werden Vorfassung, Änderung bis zum Stichtag, neuer Stand und Nachlaufereignisse getrennt. Eine nach dem Stichtag eingegangene Rechnung über eine bereits am Stichtag bestehende Verpflichtung kann den Abschlussstand korrigieren; eine erst danach neu begründete Verpflichtung wird als Nachlauf behandelt. Die Zuordnung wird mit Leistungs- oder Entstehungsgrund und Beleg begründet, nicht allein mit Rechnungs- oder Zahlungsdatum.

Das Veränderungsprotokoll führt jede Änderung nach fachlicher Freigabe mit alter Aussage, neuer Aussage, Betragseffekt, Beleg, betroffenen Berichtspassagen, betroffenen Anlagen und verbrauchten Gates. Ohne diese Rückverfolgung darf eine neue Schlussberichtsversion nicht als bloße redaktionelle Korrektur bezeichnet werden.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Prüfen Sie zuerst, ob wesentliche Verwertungen, Prozesse, Steuerfragen oder Kontendifferenzen offen sind. Benennen Sie rote Positionen statt Abschlussreife zu behaupten.
2. Rekonstruieren Sie den Verfahrensverlauf aus Beschlüssen und belegten Maßnahmen. Vermeiden Sie nicht belegte Ursache- oder Verschuldenszuschreibungen.
3. Stellen Sie Masseermittlung, Fremdrechte und Verwertung nach wirtschaftlichen Komplexen dar. Erläutern Sie erhebliche Abweichungen zwischen Schätzung und Ergebnis.
4. Beschreiben Sie Betrieb, Verträge und Personal nur für das Verständnis des Masseergebnisses und der Verfahrensentscheidungen.
5. Führen Sie Tabelle, Rang, Sicherheiten und Verteilungsbasis konsistent mit BER-FQ. Eine Anmeldung wird nicht als Feststellung bezeichnet.
6. Erklären Sie Prozesse und Ansprüche einschließlich der Entscheidung, sie weiterzuverfolgen, zu vergleichen oder nicht weiterzuverfolgen. Nennen Sie Erkenntnisgrundlage und wirtschaftliche Erwägung.
7. Behandeln Sie Steuern, Kosten, Masseverbindlichkeiten und Vergütung statusrichtig. Ein Antrag wird nicht als Festsetzung dargestellt.
8. Formulieren Sie Schlussvorschlag und beantragte oder angeregte gerichtliche Schritte, ohne künftige Zustimmung oder Aufhebung vorwegzunehmen.

9. Entscheiden Sie die Abschlussreife für jeden Bereich als `grün`, `gelb` oder `rot`. `Grün` verlangt belegte Erledigung und abgeglichene Zahlen. `Gelb` verlangt eine rechtlich und rechnerisch konkrete Behandlung eines Restpunkts mit Betrag, Verantwortlichem und Folgeweg. `Rot` liegt vor, wenn eine wesentliche Verwertung, ein wirtschaftlich erheblicher Vorgang, eine Steuer- oder Kostenposition oder eine Kontendifferenz weder erledigt noch belastbar behandelt ist. Nur wenn kein roter Bereich verbleibt, darf der Skill eine positive Gesamtbewertung vorbereiten.
10. Erstellen Sie vor der Endfassung einen Satz-für-Satz-Nachweisindex für jede wesentliche Zahl und Abschlussaussage. Die interne Prüfung verbindet Berichtssatz, Fachprodukt, Belegkennung und Rechenzelle oder Rechenweg. Der Nachweisindex bleibt intern, während die Empfängerfassung nur die erforderlichen Anlagen- und Aktenverweise enthält.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Führen Sie eine Abschlusszahlenmatrix mit mindestens Massezuflüssen, Verwertungskosten, Betriebswirkung, Prozesszuflüssen und -kosten, Steuerzahlungen oder -erstattungen, Verfahrenskosten, sonstigen Masseverbindlichkeiten, Kontenendbestand, verfügbarem Verteilungsbetrag und Forderungsbasis. Jede Zahl nennt Quellprodukt und Status. Die Matrix verlangt Zahlenidentität zwischen Bericht, Schlussrechnung, Forderungsmodul und Anlagen. Abweichende Begriffe wie Bruttoerlös, Nettoerlös, Bestand und verfügbarer Betrag werden nicht synonym verwendet.

### 3.3 Qualitätsgates

`G3 Rechenwerk` setzt einen erklärten Konten- und Rechnungsstand, eine Null-Differenz im Dreifachabgleich und stichtagsgleiche Abschlusszahlen voraus. `G4 Fachfassung` verlangt die namentliche rechtliche, tatsächliche und rechnerische Prüfung der konkreten Hash-Fassung einschließlich Anlagenliste und Nachweisindex. `G5 Einreichung` ist eine eigene namentliche Freigabe für Empfänger, Übermittlungsweg und genau bezeichnetes Paket. Eine rote Abschlussreifeposition verhindert eine vorbehaltlos positive Schlussfassung; eine gelbe Position muss im Bericht mit ihrer konkreten Behandlung erscheinen.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

`BER-SB` wird zusammen mit Abschlussreifematrix, Abschlusszahlenmatrix, Nachweisindex, Anlagenverzeichnis und Änderungsprotokoll an `berichtserstellung-steuern` übergeben. An `schlussverteilung-aufhebung-vorbereiten` gehen nur die freigegebene Schlussaussage, der gemeinsame Stichtag und die Kennungen von `BER-SR` und `BER-FQ`; der Schlussbericht selbst erteilt keine Verteilungs- oder Zahlungsfreigabe. Muss ein Fachmodul korrigiert werden, nennt die Rückgabe die betroffene Berichtspassage und die zu ersetzende Zielversion.

## 4. Quellenpflicht

BGH, Beschluss vom 11.11.2021 – IX ZB 19/20, Rn. 12 und 14 bis 21, trägt, dass Schlussrechnung oder Schlusstermin bei fortdauernder Verwertung nicht genügen und die Verwaltertätigkeit grundsätzlich erledigt sein muss. Die Entscheidung trägt keine pauschale Aussage, dass jeder spätere Zufluss den früheren Abschluss widerlegt. § 66 InsO regelt die Schlussrechnung; die konkrete Form eines zusätzlichen Schlussberichts folgt aus gerichtlicher Anforderung und belegtem Kanzleistandard.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** § 66 InsO trägt die Schlussrechnung als eigenes Rechnungslegungsprodukt. BGH, Beschluss vom 11.11.2021 – IX ZB 19/20, Rn. 12 und 14 bis 21, trägt die Sperre der Abschlussreife und Vergütungsfälligkeit bei grundsätzlich noch nicht beendeter Verwaltertätigkeit trotz vorgelegter Schlussrechnung oder abgehaltenem Schlusstermin.

**Trägt nicht:** Die Entscheidung verlangt keine rückwirkende Fehlerannahme bei jedem späteren Massezufluss und erlaubt keine zeitabschnittsweise Teilfestsetzung. Weder § 66 InsO noch der Beschluss belegt die tatsächliche Erledigung einzelner Verwertungen, Kontenabstimmung, Einreichung oder gerichtliche Zustimmung im konkreten Verfahren.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-SB`

1. Rubrum, Verfahrensdaten und Gegenstand
2. Ausgangslage, Eröffnung und wesentliche Verfahrensschritte
3. Masseermittlung und Fremdrechte
4. Verwertung, Betrieb, Verträge und Personal
5. Forderungen, Sicherheiten und Verteilungsbasis
6. Steuern, Kosten, Vergütung und Masseverbindlichkeiten
7. Prozesse, Anfechtung und Haftung
8. nicht verwertete Positionen und Abschlussreife
9. Schlussvorschlag, Anlagen und Unterschrift

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Abschluss mit offener Kostenfestsetzung

Ein Haftungsprozess ist bezahlt erledigt, aber die Kostenfestsetzung steht aus. Der Skill prüft Betrag und Bedeutung. Ist die Position wesentlich und nicht belastbar zurückgestellt, bleibt Abschlussreife offen. Liegt eine konkret begründete Behandlung vor, wird sie als gelbe Position erläutert; der Bericht behauptet keine endgültige Erledigung.

### 6.2 Muster mit Altdaten

Eine historische Vorlage enthält Namen, Konten und Ursachenfeststellungen. Der Skill übernimmt nur die für den Auftrag geeignete Gliederungslogik. Sämtliche Tatsachen werden aus der aktuellen Akte neu belegt; Altdaten werden weder pseudonymisiert weiterverwendet noch als Platzhalter stehen gelassen.

### 6.3 Späte Rechnung für eine alte Leistung

Nach fachlicher Freigabe trifft eine Rechnung über 4.800 Euro für eine vor dem Abschlussstichtag erbrachte Leistung ein. Der Skill prüft Leistungsgrund, Betrag und Massebezug, setzt die betroffenen Fassungen von `BER-SKV`, `BER-SR`, `BER-FQ` und `BER-SB` zurück und dokumentiert das Delta. Die Rechnung wird nicht allein wegen ihres späten Eingangs ignoriert. Eine neue positive Abschlussaussage entsteht erst, wenn die Kostenposition behandelt, das Rechenwerk erneut abgeglichen und die genaue neue Fassung freigegeben ist.
