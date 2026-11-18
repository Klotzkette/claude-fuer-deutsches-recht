---
name: zwischenbericht-erstellen
description: Erstellt und aktualisiert einen belegten Zwischenbericht. Vergleicht den neuen Berichtszeitraum mit der letzten eingereichten Fassung und führt Masse, Verwertung, Betrieb, Forderungen, Kosten, Prozesse und Maßnahmen zusammen.
---

# Zwischenbericht erstellen

## 1. Zweck und Anwendungsfall

Dieser Skill erstellt einen gerichtstauglichen Zwischenbericht für einen klar abgegrenzten Zeitraum. Er zeigt Entwicklungen seit der letzten eingereichten Fassung, erläutert erhebliche Soll-Ist-Abweichungen und nennt entscheidungsbedürftige Punkte. Er eignet sich für turnusmäßige, anlassbezogene und vom Gericht konkret angeforderte Berichte.

Der Skill schreibt keinen alten Bericht mit neuen Zahlen kosmetisch fort. Er rekonstruiert die Veränderungen aus Belegen, hält unveränderte Dauersachverhalte knapp und unterscheidet tatsächlichen Stand, fachliche Bewertung sowie nächste Maßnahme.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-ZW`. Die Fachroute übergibt an `akte-und-berichtsanlass-steuern`, die vier Fachmodule und `berichtserstellung-steuern`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Verfahrenskarte | BER-INT mit Auftrag, Zeitraum, Stichtag und Frist | freigegebene Arbeitsfassung |
| Vergleich | letzter eingereichter Bericht und Zugangsbeleg | Gerichtsverkehr |
| Fachmodule | BER-MV, BER-FQ, BER-SKV und BER-PAH | jeweils stichtagsbezogene Fassung |
| Rechnung | Buchhaltung, Bank, Kasse und Liquiditätsübersicht | Konten- und Belegauszüge |
| Entscheidungen | neue Beschlüsse, Ausschussentscheidungen und wesentliche Verträge | Originaldokumente |
| Maßnahmen | offene Aufgaben, Verantwortliche und Termine | Wiedervorlage und Fachakten |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Berichtsgrenze und Delta

Definieren Sie den Vorstichtag `T0` aus der letzten tatsächlich eingereichten Fassung, den neuen Stichtag `T1` und das Ende des technischen Nachlaufs `N`. Die Kernfrage jeder Berichtspassage lautet: Was galt zu `T0`, welche belegte Bewegung trat bis `T1` ein und welcher Stand gilt zu `T1`? Ein nach `T1` eingegangener Beleg kann eine vorher eingetretene Tatsache nachweisen; ein erst nach `T1` eingetretenes Ereignis wird in einem eigenen Nachlaufabsatz dargestellt und nicht in Stichtagssummen eingerechnet.

Die Veränderungsmatrix enthält je Sachverhalt Vorwert oder Vorstatus, Zugänge, Abgänge, Korrekturen, Neuwert oder Neustatus, Beleg und Berichtspassage. Korrekturen einer früheren Fehlangabe werden ausdrücklich von neuen Periodenbewegungen getrennt. Gibt es keine Veränderung, wird der unveränderte Stand nur übernommen, wenn die für den neuen Stichtag erforderliche Fortgeltung belegt oder fachlich nachvollziehbar ist.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Vergleichen Sie jede wesentliche Aussage der Vorfassung mit dem neuen Belegstand. Ordnen Sie sie als unverändert, erledigt, geändert, neu oder widerlegt ein.
2. Erstellen Sie eine Veränderungsmatrix mit früherem Stand, neuem Stand, Beleg, Betragseffekt und Berichtsauswirkung.
3. Führen Sie Masse und Verwertung nach Vermögenskomplexen. Trennen Sie Schätzwert, Vertragswert, Rechnung, Zahlung und Nettoerlös.
4. Beschreiben Sie Betriebsfortführung oder Stilllegung anhand von Zeitraum, Umsatz, Kosten, Liquidität, Personal, Verträgen und konkretem Masseeffekt.
5. Aktualisieren Sie Tabelle, Sicherheiten, Steuern, Kosten, Vergütung und Prozesse aus den führenden Fachmodulen. Übernehmen Sie keine überholte Kanzleiliste.
6. Benennen Sie Risiken nur mit Ursache, möglicher Folge und Maßnahme. Vermeiden Sie pauschale Floskeln wie „unter Kontrolle“.
7. Ordnen Sie jede nächste Maßnahme einer Person, einem Ziel, einer Frist und einem erwarteten Folgeprodukt zu.
8. Prüfen Sie vor Ausgabe Zahlenidentität zwischen Text, Tabellen und Anlagenverzeichnis.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Rechnen Sie für jede zahlenführende Berichtstabelle die Beziehung `Stand T0 + Zugänge - Abgänge ± Korrekturen = Stand T1`. Stimmen Sie Zahlungsbewegungen mit `BER-SR`, Forderungsstatus mit `BER-FQ`, Verwertung mit `BER-MV`, Steuern und Kosten mit `BER-SKV` sowie Prozesse mit `BER-PAH` ab. Eine Differenz wird nicht durch Übernahme des vermeintlich plausibelsten Werts beseitigt, sondern mit Betrag, Ursache oder Prüfweg und Auswirkung auf die Berichtsaussage ausgewiesen.

Führen Sie vor Ausgabe eine Quersummenprüfung durch: Summen im Fließtext, Tabellen und Anlagen müssen identisch sein; Prozentwerte müssen aus den bezeichneten Zählern und Nennern reproduzierbar sein; offene Restbeträge müssen aus Vertrags- oder Festsetzungsbetrag abzüglich belegter Zahlungen folgen. Schätzungen stehen außerhalb der tatsächlich realisierten Summen.

### 3.3 Qualitätsgates

`G1` verlangt belegte Verfahrensidentität, Berichtsauftrag, `T0`, `T1`, Empfänger und Frist. `G2` verlangt eine vollständige Veränderungsmatrix für alle wesentlichen Sachverhalte und sichtbare Lücken mit Sperrwirkung. `G3 Rechenwerk` ist nur prüfbereit, wenn die Deltaformeln und Quersummen auf null Differenz schließen oder jede verbleibende Differenz die betroffene Aussage sichtbar sperrt. `G4 Fachfassung` wird durch eine namentlich bezeichnete Person für genau diese Version und Anlagenliste erteilt. `G5 Einreichung` bleibt bis zur konkreten menschlichen Versandfreigabe mit Empfänger, Weg und Dateiliste offen.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

Das Übergabepaket an `berichtserstellung-steuern` besteht aus `BER-ZW`, Veränderungsmatrix, Zahlenkontrollblatt, Nachlaufverzeichnis, Anlagenliste und Freigabevermerk. Rückfragen an Fachmodule nennen die konkrete Berichtspassage, den widersprüchlichen Wert oder Status, beide Quellen und das erwartete Zielprodukt. An die nächste Zwischenberichtsperiode werden die eingereichte Fassung samt Zugangsnachweis und nicht nur die letzte interne Datei als neue Vergleichsbasis übergeben.

## 4. Quellenpflicht

§ 58 Absatz 1 InsO erlaubt dem Insolvenzgericht, jederzeit einzelne Auskünfte oder einen Bericht über den Sachstand und die Geschäftsführung zu verlangen. Davon ist § 66 Absatz 3 InsO zu trennen: Danach kann die Gläubigerversammlung zu bestimmten Zeitpunkten während des Verfahrens eine Zwischenrechnung verlangen. Keine der Vorschriften schreibt für jeden Zwischenbericht dieselbe Gliederung vor. § 69 InsO ist bei einem Gläubigerausschuss für dessen Prüf- und Überwachungsrolle relevant.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** § 58 Absatz 1 InsO trägt die gerichtliche Anforderung einzelner Auskünfte oder eines Sachstands- und Geschäftsführungsberichts. § 66 Absatz 3 InsO trägt das Recht der Gläubigerversammlung, zu bestimmten Zeitpunkten eine Zwischenrechnung zu verlangen. §§ 69 und 79 InsO tragen die dort beschriebenen Unterstützungs-, Berichts- und Prüfbezüge. Die fachlichen Normen und Entscheidungen aus der Quellenkarte tragen nur die jeweils ausdrücklich abgegrenzte Einzelpassage des Zwischenberichts.

**Trägt nicht:** Diese Vorschriften geben nicht ohne konkrete gerichtliche Verfügung für jeden Zwischenbericht dieselbe Gliederung, Berichtsperiode oder Anlagenliste vor. Sie belegen weder einen tatsächlichen Zahlungseingang noch eine Feststellung, Zustimmung oder Einreichung; dafür bleiben Akten- und Rechennachweise erforderlich.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-ZW`

1. Verfahrensdaten, Auftrag, Zeitraum und Stichtag
2. wesentliche Veränderungen seit der Vorfassung
3. Masse, Verwertung und Betrieb
4. Forderungen, Sicherheiten und Tabelle
5. Steuern, Kosten, Vergütung und Liquidität
6. Prozesse, Anfechtung und Haftung
7. Risiken, Entscheidungen und nächste Maßnahmen
8. Anlagen und interne Vollständigkeitskontrolle

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Neuer Verwertungserlös

Im Vorbericht war ein Maschinenverkauf mit 180.000 Euro erwartet. Der notarielle oder schriftliche Vertrag weist 170.000 Euro aus; auf dem Massekonto gingen bis zum Stichtag 150.000 Euro ein. Der Skill berichtet Erwartung, Vertrag und Zahlung getrennt, erläutert die offene Restforderung und übernimmt nur 150.000 Euro in den verfügbaren Bestand.

### 6.2 Offener Steuerbescheid

Die Steuerberatung erwartet eine Erstattung. Ein Bescheid fehlt. Der Zwischenbericht nennt die Erwartung als Angabe der Steuerberatung, nicht als Massezufluss. Die Beschaffung des Bescheids erhält Verantwortlichen und Frist; die Liquiditätsrechnung bleibt unverändert.

### 6.3 Korrektur der Vorfassung und echtes Periodendelta

Der Vorbericht nannte irrtümlich 40.000 Euro offenen Kaufpreis; der damalige Vertrag belegte tatsächlich 35.000 Euro. Im neuen Zeitraum gehen 20.000 Euro ein. Der Skill weist zuerst die Korrektur von minus 5.000 Euro und danach den Zahlungseingang von minus 20.000 Euro aus. Der offene Stand zu `T1` beträgt 15.000 Euro. Dadurch bleibt erkennbar, dass nur 20.000 Euro als neuer Massezufluss in `BER-SR` gehören und die übrige Abweichung eine Korrektur der Vorberichtsangabe ist.
