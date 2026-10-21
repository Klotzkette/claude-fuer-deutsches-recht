# Gegenlese und enge Anwendungsprobe vom 21. Oktober 2026

## 1. Umfang und Methode

Die Gegenlese verglich die Plugintexte und den zuvor erstellten [Quellenbericht](quellenpruefung-2026-10-21.md) mit den tatsächlichen Verträgen und Zahlungsdaten der drei Übungsakten. Besondere Schwerpunkte waren Gläubigerwechsel, Drittzahlung, subjektive Voraussetzungen, Bargeschäft sowie die finanziellen und zeitlichen Zusammenhänge der beiden neuen Akten. Die Gegenlese wurde durch einen anderen Bearbeitungsagenten als den Verfasser der neuen Plugintexte vorgenommen. Sie ist keine erneute unabhängige Live-Verifikation sämtlicher amtlicher Rechtsquellen.

Die Lesebasis umfasste insbesondere die ursprünglichen Bremer Fixtures `case.json` und `contracts.json`, die neue Bremer Ergänzung, die neuen Fallfixtures und erzeugten Bamberger DOCX-, PDF- und EML-Dateien sowie Mini-, Hauptproblem- und Werkstatt-Prompt und die betroffenen Fachskills. Die XLSX-Berechnungen wurden gegen die Belegbeträge gerechnet. Die Weserfunken-Erweiterung wurde zusätzlich gebaut, visuell geprüft und mit Originalhashes abgeglichen; ihre Einzelheiten stehen im [separaten QA-Bericht](../legal/fintech-bremen-anfechtung-vertiefung.md).

## 2. Befunde und umgesetzte Korrekturen

| Befund | Korrektur und Gegenprüfung | Status |
|---|---|---|
| Die Bremer Akte war in einem Beispiel als Übernahme einer Schuld durch Weserfunken beschrieben. Tatsächlich bleibt Weserfunken stets Darlehensnehmerin. | Gläubiger-/Vertragsgeberwechsel Nexora zu Vellio, Kaufpreiszahlung Vellios und spätere Zahlungen Weserfunkens getrennt. Hauptproblem Abschnitte 4/5 und Beispiel 6 des Dreiecksskills erneut gelesen; § 134 nicht als automatische Folge eines unwirksamen Gläubigerwechsels verwendet. | Erledigt |
| Im Bargeschäftsskill stand bei der Unlauterkeit „Erkennbarkeit“ statt tatsächlich erforderlichem Erkennen. | Der Text verlangt jetzt ausdrücklich die gesonderte Prüfung, ob der andere Teil das unlautere Handeln tatsächlich erkannt hat. Der reine Kenntnisstand zu wirtschaftlichen Schwierigkeiten genügt nicht. | Erledigt |
| „Benachteiligungsabsicht“ konnte im Vorsatzskill und Werkstatttext einen zu engen Vorsatzmaßstab nahelegen. | Begriff durch „Benachteiligungsvorsatz“ ersetzt. Die dabei entstandene grammatische Folge wurde ebenfalls korrigiert; in Skill und Werkstatt steht nach erneuter Gegenprüfung „über den Benachteiligungsvorsatz“. | Erledigt |
| Die Abtretungsurkunde vom 8. Mai enthielt bereits einen Versand vom 12. Mai, ohne diesen als spätere Ergänzung zu kennzeichnen. | „Nachträglicher Versandvermerk vom 12.05.2026“ eingefügt. Nicht nur Fixture, sondern neu erzeugte native DOCX gelesen. | Erledigt |

Die Bamberger Urkunden enthalten bewusst keine abschließende Musterlösung: Die vorzeitige Mehrzahlung, die spätere Sicherung und widersprüchliche Erinnerungen bleiben auswertbare Tatsachen. Falsche Rechtsprechungszitate oder ein rechtliches Endergebnis wurden nicht als zusätzliche Fallbelege erfunden.

## 3. Betrags- und Chronologieabgleich

### 3.1 Blechliebe, Bamberg

Die alten Rechnungen ergeben 14.280,00 EUR plus 9.520,00 EUR plus 11.900,00 EUR, mithin 35.700,00 EUR. Vier Zahlungen auf diesen Bestand ergeben 6.000,00 EUR plus 6.000,00 EUR plus 6.000,00 EUR plus 9.000,00 EUR, mithin 27.000,00 EUR. Offen bleiben 8.700,00 EUR. Die Neulieferung kostet zusätzlich 6.000,00 EUR netto plus 1.140,00 EUR Umsatzsteuer, also 7.140,00 EUR brutto. Die angegriffenen Zahlungen ergeben insgesamt 34.140,00 EUR. Der Nennbetrag der Sicherheit von 16.660,00 EUR ist kein weiterer Geldeingang.

Der Antrag ging nach dem Beschluss am 15. Juni 2026 ein; die Eröffnung am 1. September darf nicht als Ausgangstag der Rückschau verwendet werden. Der 12. März liegt vor dem 15. März als kalenderbezogenem Beginn des Dreimonatszeitraums. Die rechtliche Wirksamkeit der ersten Zahlung ist dennoch am Empfängerkonto zu prüfen. Die 9.000,00 EUR vom 9. Juni liegen einen Tag vor dem vereinbarten 10. Juni und übersteigen die geplante Rate um 3.000,00 EUR. Diese Abweichung wurde als eigenständiges Anfechtungsrisiko in die Anwendungsprobe aufgenommen.

Python-Kalenderprüfung: 8. Mai ist Freitag, 11. Mai Montag, 12. Mai Dienstag, 26. Mai Dienstag, 29. Mai Freitag, 1. Juni Montag und 2. Juni Dienstag. Damit passen Ratennachfrage, spätere Versandnotiz, angekündigte Montagsinventur und Dienstagsausgabe zusammen. Der 12. Oktober ist Montag, der 21. Oktober Mittwoch und die Antwortfrist 27. Oktober Dienstag. Ein in der Akte genanntes ursprüngliches Rechnungsziel am Sonntag ist als Rechnungsangabe erhalten; seine rechtliche Fälligkeit darf nicht allein aus dem gedruckten Datum abgeleitet werden. Für die betrachteten alten Raten ist die spätere Ratenvereinbarung gesondert maßgeblich.

### 3.2 Faltenwurf, Fürth

Das ursprüngliche Darlehen von 280.000,00 EUR abzüglich 80.000,00 EUR Rückzahlung ergibt einen rechnerischen Rest von 200.000,00 EUR. Die bezeichnete Bankverbindlichkeit von 52.000,00 EUR abzüglich 35.000,00 EUR Zahlung ergibt 17.000,00 EUR. Die Positionen Haderlein über 4.800,00 EUR und 286,40 EUR bleiben verschiedene Vorgänge; aus einer Summenbildung allein folgt keine einheitliche Darlehensqualifikation. Sicherungsbestellung und Rückzahlung wurden nicht zu einer Handlung zusammengezogen.

Die relativen Wochentagsangaben wurden abgeglichen: 19. Juni 2026 ist Freitag und der davorliegende Mittwoch der 17. Juni. 20. Juni ist Samstag, der folgende Montag der 22. Juni. 29. Juni ist Montag; „morgen“ bezeichnet dort den Dienstag, 30. Juni. In den geprüften Rechnungs- und Chronologiebezügen wurde kein weiterer Widerspruch gefunden. Dies ersetzt keine abschließende rechtliche Falllösung.

### 3.3 Weserfunken, Bremen

Der neue Teil wahrt den ursprünglichen Darlehensbetrag von 500.000,00 EUR, 18 Zinszahlungen von zusammen 90.000,00 EUR und insgesamt 590.000,00 EUR Schuldnerzahlungen an Vellio. Die eigene Kaufpreiszahlung Vellios an Nexora wird nicht als weitere Schuldnerzahlung mitgezählt. Die erwogene Drittzahlung Nordhafen an Nordkai von 42.840,00 EUR wurde nicht ausgeführt; ein Entwurf ist kein Bankumsatz. Nachträgliche Rückabwicklungsdaten wurden nicht in frühere Liquiditätsstichtage zurückgeschrieben. Alle 42 bisherigen Originaldateien blieben nach Hashabgleich unverändert.

## 4. Tatsächlich ausgeführte Modell-Anwendungsprobe

Das [ausformulierte erste Antwortschreiben mit interner Notiz](anwendungsprobe/blechliebe-erste-antwort.md) entstand nach Lektüre des Mini-Prompts und der erzeugten Bamberger Originalunterlagen. Der Auftrag lautete, Raban gegen die pauschale Rückforderung von 34.140,00 EUR zunächst außergerichtlich zu vertreten. Es wurde kein Antworttext aus einer vorhandenen Musterlösung kopiert.

Die Probe trennt 27.000,00 EUR Altschuld und 7.140,00 EUR Neulieferung, behandelt die Märzrate nur bedingt als außerhalb des Dreimonatszeitraums, lässt § 133 offen und nimmt weder eine generelle Ratenimmunität noch eine Dreißigtagesregel nach § 142 an. Sie erkennt die belastende Juni-Abweichung und die Nachbesicherung. Fehlende Gutschriftbelege, Vertragsänderungen, Kenntnistatsachen und Gegenwertnachweise werden gezielt benannt. Fristen, eine noch nicht belegte Vertretungsanzeige und die bereits vergangene Forderungsanmeldefrist werden getrennt geführt.

Die abschließende Bewertung stammt vom selben Modell wie das Antwortschreiben. Es gab keinen unabhängigen Richterlauf, keine tatsächliche Anwendung in einer Produktoberfläche und keine Außenwirkung. Der Quellenbericht wurde als zuvor dokumentierte Primärquellenprüfung verwendet; ein neuer Live-Abruf wurde in dieser Probe nicht behauptet.

## 5. Reproduzierbarkeit und Grenzen

Am Zeitpunkt der Eingangslektüre bestanden folgende SHA-256-Werte:

| Eingabe | SHA-256 |
|---|---|
| Mini-Prompt `insolvenzanfechtung-schnellstart.md` | `98492625d5c230d84e5054c473bbbed9105bc219df3afa49b16c9364ea2c277a` |
| Quellenbericht vom 21.10.2026 | `020287c81d1645821e3958691021712983d6d82ca7ee7ef2e1b695c0ff5d534b` |
| Blechliebe `20_Rueckforderung.docx` | `8aba03b9deea2698520bb4f57b6a8836228ad6df6cd42c4cb8365a878e6f0d22` |

Spätere redaktionelle Änderungen können Dateihashes verändern. Diese Werte dokumentieren die konkrete Lektüre und behaupten keine Unveränderlichkeit der übrigen Dateien. Die Gegenlese bescheinigt weder einen vollständigen unabhängigen Rechtsprechungsaudit noch das Ergebnis eines realen Rechtsstreits. Die offene Prüfung des aktuellen konsolidierten unionsrechtlichen und österreichischen Rechts für die internationale Bremer Variante bleibt nach dem Quellenbericht erhalten.
