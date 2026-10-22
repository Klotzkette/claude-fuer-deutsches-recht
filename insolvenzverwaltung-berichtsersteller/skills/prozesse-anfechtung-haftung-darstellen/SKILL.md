---
name: prozesse-anfechtung-haftung-darstellen
description: Erstellt das Fachmodul zu Aktiv- und Passivprozessen, Insolvenzanfechtung, Organhaftung und sonstigen Ansprüchen. Trennt Nominalwert, Prozessstand, Kosten, Risiko, Vergleich und tatsächlich realisierten Massezufluss.
---

# Prozesse, Anfechtung und Haftung darstellen

## 1. Zweck und Anwendungsfall

Dieser Skill führt gerichtliche und außergerichtliche Streitigkeiten sowie mögliche Anfechtungs- und Haftungsansprüche in einer wirtschaftlich und rechtlich nachvollziehbaren Übersicht. Er wird für Zwischenberichte, Schlussberichte und Abschlussreife eingesetzt.

Der Skill entscheidet nicht allein aufgrund einer Forderungshöhe, dass ein Anspruch werthaltig ist. Er trennt Rechtsgrund, Tatsachen, Beweise, Verjährung, Verfahrensstand, Kosten, Vollstreckbarkeit, Vergleich und tatsächlichen Zufluss.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-PAH`. Die Fachroute übergibt an die Berichtsskills, `masse-verwertung-betrieb-darstellen` und `schlussrechnung-konten-abgleichen`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Ansprüche | Gegner, Rechtsgrund, Betrag, Tatsachen und Beweise | Anspruchsakte |
| Verfahren | Gericht, Aktenzeichen, Anträge, Termine, Entscheidungen und Rechtsmittel | Prozessakte |
| Anfechtung | Rechtshandlung, Zeitpunkt, Insolvenzbezug, Kenntnis und Rückgewähr | Anfechtungsakte |
| Haftung | Pflicht, Person, Schaden, Kausalität, Einwendungen und Versicherung | Haftungsakte |
| Wirtschaftlichkeit | Kosten, Finanzierung, Solvenz, Vollstreckbarkeit und Vergleich | Berechnung und Recherche |
| Geldfluss | Zahlung, Kostenfestsetzung und Bankbeleg | BER-SR |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Vorgangsstichtag und Delta

Jede Vorgangskarte weist den Stand der letzten Berichtsfassung, die Bewegungen im neuen Berichtszeitraum, den Stand am Stichtag und Ereignisse nach dem Stichtag aus. Als Bewegungen gelten insbesondere neue Tatsachen oder Belege, Geltendmachung, Klage, Entscheidung, Rechtsmittel, Vergleich, Vollstreckungsmaßnahme, Kostenfestsetzung und Zahlung. Ein Urteil nach dem Stichtag ist ein Nachlaufereignis; ein nach dem Stichtag eingegangener Schriftsatz kann dagegen eine bereits vor dem Stichtag erfolgte Prozesshandlung belegen.

Die wirtschaftliche Deltaübersicht trennt Nominalbetrag, titulierten Betrag, Vergleichsbetrag, festgesetzte Kosten, Zahlungseingang, Zahlungsausgang und offenen Vollstreckungsbetrag. Änderungen an Erfolgsaussicht oder Durchsetzbarkeit werden mit neuem Beleg und Begründung dokumentiert, nicht als rückwirkend sichere Zahl behandelt.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Vergeben Sie je Vorgang eine eindeutige Kennung und trennen Sie Anspruch, Gegner und Rechtsgrund. Vermischen Sie nicht mehrere Zahlungen oder Haftungspersonen.
2. Erstellen Sie eine Chronologie aus Primärbelegen. Kennzeichnen Sie streitige Tatsachen und die jeweilige Beweisquelle.
3. Prüfen Sie Anspruchsgrund, Einwendungen, Verjährung und prozessuale Lage nur mit zugänglichen verifizierten Quellen. Der Bericht fasst die tragenden Punkte prägnant zusammen.
4. Erfassen Sie Stadium als Prüfung, außergerichtliche Geltendmachung, Klage, Rechtsmittel, Titel, Vollstreckung, Vergleich oder erledigt. Ein Urteil ist kein Zahlungseingang.
5. Ermitteln Sie Nominalwert, plausibles Risikoband, erwartete Kosten, Vollstreckbarkeit und tatsächlichen Massewert. Schätzungen werden als solche bezeichnet.
6. Dokumentieren Sie bei Vergleich oder Nichtverfolgung Erkenntnisgrundlage, wirtschaftliche Abwägung, Zustimmungen und konkrete Rechtswirkung.
7. Ordnen Sie Zahlung, Kosten und Erstattung über Bankbelege BER-SR zu. Kostenfestsetzung und Zahlung bleiben getrennt.
8. Prüfen Sie, ob ein offener Vorgang die Abschlussreife sperrt oder mit einer konkreten Behandlung als gelbe Position fortgeführt werden kann.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Rechnen Sie je Vorgang eine transparente wirtschaftliche Brücke. Auf der Aktivseite stehen realisierte Zahlungen abzüglich tatsächlich gezahlter externer Kosten; offene Ansprüche und Kostenerstattungen werden daneben geführt. Auf der Passivseite stehen tatsächlich gezahlte Beträge und konkret behandelte offene Verpflichtungen. Ein Risikoband darf die Szenarien `kein Zufluss`, `Vergleich` und `volle Durchsetzung` zeigen, wird aber nicht mit Scheingenauigkeit zu freier Masse verdichtet. Die Gesamtsummen der realisierten Zahlungsströme müssen mit `BER-SR` übereinstimmen.

### 3.3 Qualitätsgates

`G2` verlangt je wesentlichem Vorgang Chronologie, Tatsachenbehauptung, Gegenposition, Beleglage, Fristenstand, Stadium und wirtschaftliche Wirkung. Fehlt ein entscheidender Beleg, wird die betroffene Anspruchsvoraussetzung als offen markiert. `G4` verlangt namentliche Freigabe der rechtlichen Bewertung und jeder Empfehlung zu Klage, Vergleich, Verzicht oder Nichtverfolgung. Bei einer besonders bedeutsamen Prozess- oder Vergleichshandlung wird außerdem die dokumentierte Prüfung von § 160 InsO übergeben. `G5` ist für jedes Anspruchsschreiben oder jede gerichtliche Einreichung separat. Offene wirtschaftlich wesentliche Vorgänge sperren Abschlussreife, wenn ihre Fortführung, Übertragung, Rückstellung oder sonstige Behandlung nicht konkret belegt ist.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

An die Berichtsskills geht je Vorgang eine ausformulierte Kurzlage mit Rechtsgrund, Streitstand, Stadium, nächstem Termin, wirtschaftlicher Bedeutung und Abschlusswirkung. An `schlussrechnung-konten-abgleichen` geht ausschließlich die belegte Zahlungsliste mit Vorgangskennung, Bruttozahlung, Kosten, Erstattung, Valuta und Bankbeleg. An `masse-verwertung-betrieb-darstellen` gehen nur Ansprüche oder Erlöse, die einem Vermögenskomplex zugeordnet werden müssen. Ein Nominalbetrag oder Urteil wird niemals als realisierter Massezufluss übergeben.

## 4. Quellenpflicht

Für Insolvenzanfechtung sind §§ 129 bis 147 InsO in der aktuellen Fassung zu prüfen; eine bloße Normnennung ersetzt keine tatbestandsbezogene Prüfung. § 15b InsO ist bei den dort erfassten Zahlungen und Ersatzansprüchen statusgenau zu prüfen. §§ 85 und 86 InsO sind für die Aufnahme anhängiger Rechtsstreitigkeiten relevant. § 160 InsO ist bei wirtschaftlich besonders bedeutsamen Prozessen und Vergleichen als Zustimmungskontrolle zu beachten. Dieser Skill verwendet keine zusätzliche Gerichtsentscheidung aus Modellwissen; tragende Entscheidungen werden nur nach amtlichem Volltextcheck ergänzt.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** §§ 129 bis 147 InsO tragen die tatbestandsbezogene Prüfung von Insolvenzanfechtung; § 15b InsO die dort bezeichnete Anspruchsprüfung zu Zahlungen; §§ 85 und 86 InsO die Prüfung der Aufnahme anhängiger Rechtsstreitigkeiten; § 160 InsO die Zustimmungskontrolle bei besonders bedeutsamen Prozessen oder Vergleichen.

**Trägt nicht:** Die Normen beweisen weder eine konkrete Rechtshandlung, Kenntnis, Pflichtverletzung, Schadenshöhe, Solvenz des Gegners noch den Zahlungseingang. Ein hoher Nominalbetrag ersetzt keine Beweis-, Kosten- und Durchsetzbarkeitsprüfung; eine fachliche Empfehlung ersetzt keine erforderliche Zustimmung oder Außenfreigabe.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-PAH`

1. Vorgangsregister und wirtschaftliche Übersicht
2. Tatsachen, Beweise und Streitstand
3. rechtliche Kernfragen und Einwendungen
4. Verfahrensstadium, Termine und Rechtsmittel
5. Kosten, Vollstreckbarkeit, Risiko und Massewert
6. Vergleich, Nichtverfolgung oder weitere Maßnahme
7. Zahlungen, Abschlusswirkung und Übergaben

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Obsiegendes Urteil ohne Zahlung

Ein Urteil über 120.000 Euro ist ergangen; der Gegner hat Berufung eingelegt und es gibt Hinweise auf Vollstreckungsrisiken. Der Skill berichtet Titel, Rechtsmittel, Kosten und Vollstreckbarkeit getrennt. BER-SR enthält keinen Erlös, solange keine Zahlung belegt ist.

### 6.2 Kleiner Anspruch mit hohen Kosten

Ein möglicher Anspruch beträgt 8.000 Euro. Beweisaufnahme und Auslandszustellung wären kostspielig. Der Skill dokumentiert Tatsachen, Beweislage, Kostenband und fachliche Entscheidung. Eine Nichtverfolgung wird nicht mit einer Leerformel, sondern mit der konkreten wirtschaftlichen Abwägung beschrieben.

### 6.3 Vergleich mit später Zahlung

Ein Anspruch über 200.000 Euro wird am 20. Juni durch einen freigegebenen Vergleich über 90.000 Euro erledigt; der Stichtag ist der 30. Juni, die Zahlung geht am 5. Juli ein. Der Skill weist zum Stichtag Vergleich und offene Vergleichsforderung aus, aber keinen Zahlungseingang. Der Zahlungseingang erscheint als Nachlaufereignis und wird erst in der folgenden Rechenfassung über Bankbeleg in `BER-SR` übernommen. Vergleichsabschluss, Kosten und tatsächlicher Nettozufluss bleiben getrennte Status.
