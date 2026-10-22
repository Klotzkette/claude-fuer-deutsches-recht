---
name: berichtserstellung-steuern
description: Steuert als Hauptproblemskill den vollständigen Zwischen- und Schlussberichtslauf. Hält Produkte, Stichtage, Fassungen, Belege, Gates, Freigaben, Fristen und Übergaben zusammen und führt zum nächsten prüfbaren Dokument.
---

# Berichtserstellung steuern

## 1. Zweck und Anwendungsfall

Dieser Hauptskill übernimmt komplexe oder gemischte Aufträge und steuert sie bis zum bestellten Bericht oder Abschlusspaket. Er entscheidet nicht materiell anstelle der Fachskills, sondern hält Verfahrensstand, führende Fassungen, Stichtage, Gates, Fragen und Übergaben konsistent.

Verwenden Sie ihn bei unübersichtlichen Akten, mehreren Berichtstypen, fortlaufenden Aktualisierungen, Abschlussprüfungen oder wenn unklar ist, welcher Fachskill als Nächstes arbeiten muss. Er zeigt auf Wunsch zuerst das Berichtscockpit oder erzeugt unmittelbar die bearbeitbare Fassung, wenn der Auftrag klar ist.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-CTRL`. Die Fachroute übergibt an alle zehn Fachskills. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Auftrag | gewünschtes Ergebnis, Empfänger und Außenhandlung | Nutzerauftrag oder gerichtliche Verfügung |
| Verfahrenskarte | BER-INT mit Rolle, Zeitraum, Stichtag und Frist | Fachskill Akte und Anlass |
| Produkte | alle vorhandenen BER-Fassungen mit Pfad und Hash | Arbeitsordner |
| Gates | Status, Freigebende, Nachweis und Sperre | Freigabejournal |
| Fristen | gerichtliche, gesetzliche und interne Termine | Fristenregister |
| Fragen | offene Tatsachen, Rechtsfragen und Rechenabweichungen | Lücken- und Widerspruchsliste |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Steuerungsstand und Änderungsvektor

Das Cockpit führt je Produkt die Vorfassung, die neue Fassung, den gemeinsamen Stichtag, den letzten Nachlaufbeleg und einen Änderungsvektor. Dieser nennt jede Änderung an Betrag, Forderungsbasis, Rechtsstatus, Abschlussaussage, Anlage oder Freigabe sowie alle davon abhängigen Produkte. Ein Kostenbeschluss verändert beispielsweise nicht nur `BER-SKV`, sondern regelmäßig auch `BER-SR`, den verfügbaren Betrag in `BER-FQ`, die Abschlussdarstellung in `BER-SB` und gegebenenfalls `BER-SVA`.

Ordnen Sie jede Information entweder der Periode bis zum Stichtag, dem Nachlauf als Beleg für eine stichtagsbezogene Tatsache oder einem echten Ereignis nach dem Stichtag zu. Nur die ersten beiden Kategorien können den stichtagsbezogenen Zahlenstand ändern. Jede Änderung erhält einen Deltaeintrag mit alter und neuer Zahl, Ursache, Beleg, betroffenen Produkten und verbrauchten Freigaben.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Bestimmen Sie das bestellte Endprodukt und zerlegen Sie es in die erforderlichen BER-Produkte. Beginnen Sie mit der Aktenroute, wenn BER-INT fehlt oder veraltet ist.
2. Erstellen Sie ein Cockpit mit Produkt, führender Fassung, Stichtag, Datenstand, Verantwortlichem, Gate und nächstem Schritt.
3. Prüfen Sie die Synchronität. Ein Schlussbericht, eine Schlussrechnung und ein Schlussverzeichnis mit unterschiedlichen Stichtagen dürfen nicht als abgestimmtes Paket ausgegeben werden.
4. Routen Sie Tatsachen- und Rechenfragen an BER-MV, BER-FQ, BER-SKV oder BER-PAH. Geben Sie der Route konkrete Eingaben, Frage und gewünschte Rückgabe.
5. Führen Sie Rückgaben nur nach Versions- und Plausibilitätskontrolle zusammen. Dokumentieren Sie jede daraus folgende Änderung anderer Produkte.
6. Berechnen Sie Fristen ausschließlich aus belegten Auslösern. Kennzeichnen Sie vorläufige Termine, wenn Zugang oder Bekanntmachung nicht belegt ist.
7. Öffnen und schließen Sie Gates nur mit den in der Matrix verlangten Nachweisen. Eine Maschine dokumentiert den Stand, gibt aber kein menschliches Gate frei.
8. Geben Sie das bestellte Dokument zuerst aus und danach das interne Cockpit mit offenen Punkten, Freigabe und nächster Route.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

### 3.3 Qualitätsgates

Der Hauptskill verwaltet `G1 Auftrag`, `G2 Belegbestand`, `G3 Rechenwerk`, `G4 Fachfassung`, `G5 Einreichung`, `G6 Verteilung`, `G7 Zahlung` und `G8 Nachtrag`. Ein Gate ist `offen`, `prüfbereit`, `menschlich freigegeben` oder `ausgeführt und belegt`. „Automatisch freigegeben“ ist unzulässig. Bei einer Änderung tragender Daten setzt der Skill betroffene Gates auf `offen` zurück.

Ein Gate darf nur auf `prüfbereit` wechseln, wenn sein Mindestnachweis vollständig bezeichnet ist und alle vorgelagerten Sperren aufgelöst sind. `G3` verlangt insbesondere eine reproduzierbare Überleitung des Bestands und der Forderungsbasis; `G4` die namentliche Prüfung der exakten Hash-Fassung; `G5` einen konkreten Empfänger, Übermittlungsweg und vollständige Anlagenliste; `G6` die belegten organschaftlichen und gerichtlichen Voraussetzungen; `G7` eine unveränderte Zahldatei oder Zahlungsliste mit verifizierten Empfängerdaten; `G8` die Massezugehörigkeit und tatsächliche gerichtliche Anordnung. Der Cockpitstatus nennt nicht nur „rot“, sondern die fehlende Bedingung und das Produkt, das sie nachweisen muss.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

Die Übergabe ist produktgenau. Sie enthält eine Zeile je Ausgangs- und Zielprodukt mit Quellkennung, Zielkennung, übernommenen Feldern, ausgeschlossenen Feldern, Stichtag, Hash und Annahmestatus. `BER-SR` übergibt an `BER-FQ` den belegten verfügbaren Bestand, nicht die rechtliche Forderungsbasis. `BER-FQ` übergibt an `BER-SVA` die freigegebene Basis, Quote und Einzelbeträge, nicht eine Zahlungsfreigabe. `BER-SB` übernimmt aus Fachmodulen nur freigegebene Tatsachen und kennzeichnet jede verkürzte rechtliche Bewertung als solche.

## 4. Quellenpflicht

Der Hauptskill übernimmt nur die in den Fachprodukten dokumentierten Rechtsquellen. Für Abschlussreife ist BGH, Beschluss vom 11.11.2021 – IX ZB 19/20, Rn. 12 und 14 bis 21, ein zentraler Anker mit den in der Quellenkarte beschriebenen Grenzen. Für Verteilung und Nachtrag werden nur die jeweils einschlägigen, dort verifizierten Anker übernommen. Der Hauptskill erfindet keinen zusätzlichen Rechtsprechungsnachweis.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** BGH, Beschluss vom 11.11.2021 – IX ZB 19/20, Rn. 12 und 14 bis 21, trägt im Abschlusscockpit die Sperre, wenn die Verwertungstätigkeit tatsächlich fortdauert. Die weiteren Anker der Quellenkarte tragen nur die dort bezeichneten Verteilungs-, Forderungs- oder Nachtragsfragen.

**Trägt nicht:** Der Beschluss trägt weder einen automatischen Abschlussstatus aus einer vorgelegten Schlussrechnung noch eine zeitabschnittsweise Teilfestsetzung. Das Cockpit darf aus einem grünen Fachmodul keine gerichtliche Zustimmung, Zahlung oder Aufhebung ableiten.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-CTRL`

1. Auftrag und gewünschtes Endprodukt
2. Verfahrensstand und Berichtscockpit
3. führende Fassungen und Stichtagssynchronität
4. Gates, Freigaben und Sperrwirkungen
5. offene Fragen, Fristen und Verantwortliche
6. Fachrouting und Übergaben
7. nächstes Dokument und konkrete Handlung

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Vollständiges Abschlusspaket

Der Auftrag lautet, Schlussbericht und Verteilung vorzubereiten. BER-SR zeigt eine ungeklärte Kontendifferenz. Der Hauptskill lässt BER-SB in den belegten Teilen ausarbeiten, hält aber `G3`, Quote und BER-SVA offen. Er routet die Differenz mit Betrag, Konten und Frist zurück und nennt als nächstes Produkt die korrigierte BER-SR-Fassung.

### 6.2 Neue Information nach Fachfreigabe

Nach Freigabe des Schlussberichts geht ein Kostenbeschluss ein. Der Hauptskill identifiziert BER-SKV, BER-SR, BER-FQ und BER-SB als betroffen, erstellt neue Versionen und setzt die betroffenen Gates zurück. Eine frühere Einreichungs- oder Zahlungsfreigabe wird nicht übertragen.

### 6.3 Stichtagsgleicher Text bei abweichender Tabelle

`BER-SB` und `BER-SR` tragen den 30. Juni, `BER-FQ` beruht jedoch noch auf dem gerichtlichen Tabellenstand vom 15. Mai und enthält eine später festgestellte Forderung nicht. Der Hauptskill bezeichnet nicht das ganze Paket als stichtagsgleich. Er weist die fachlich zulässige Datenasymmetrie sichtbar aus, verlangt eine Deltaüberleitung der Forderungsbasis und sperrt Quote und `BER-SVA`, bis die Folgeprodukte auf dem freigegebenen Stand neu erzeugt wurden.
