# Vergleichsmaterial: Abgleich nach der Satzüberarbeitung

Prüfstand: 14. November 2026. Gegenstand sind ausschließlich die geänderten Originalfassungen der fünf Akten Weserfunken Bremen, Blechliebe Bamberg, Faltenwurf Fürth sowie VeedelWende Direktzahlung und Forderungskauf Köln.

## 1. Durchgeführter Abgleich

Die fünf Quellen unter `quality/insolvenz-testakten/gutachten/` wurden mit den geänderten Schriftsätzen und Schreiben abgeglichen. Zusätzlich wurden die bestehenden Gutachten-PDFs und Word-Klagevorlagen unter `pruefmaterial-insolvenz/` ausgelesen. Die Dateien und ihre Quellen sind gegenüber dem bisherigen Materialbestand bytegleich. Die Wordvorlage bleibt eine fallübergreifende Blankovorlage; sie enthält keine festen Seitenverweise auf die neu gesetzten Schriftsätze.

Die Gutachten beziehen sich auf Aktenstück- und Anlagenkennungen, Zahlungsdaten und Beträge. Diese Bezugsgrößen haben sich durch Briefköpfe, vorangestellte Anträge, neue Dezimalgliederung und fließenden Satz nicht geändert. In den Gutachtenquellen und den bestehenden Vergleichsdateien findet sich insbesondere kein zu korrigierender Verweis auf eine 25-seitige Klage oder 20-seitige Erwiderung der Weserfunken-Akte. Die beiden konkreten Binnenverweise des Weserfunken-Gutachtens wurden im Original nachgesehen: B1 Ziffer 7.2 betrifft unverändert den Ausschluss einer Rückkauf- und Verlustausgleichspflicht; K7 Blatt 6 enthält unverändert die Rückabwicklungsmitteilung und Fälligkeitsangaben vom 2. Mai 2024.

Bei Blechliebe bleibt die Bezifferung von 34.140 EUR und die Unterscheidung zwischen Altzahlungen, Neulieferung und Sicherung erhalten. Bei Faltenwurf bleiben die drei Komplexe 80.000 EUR Darlehensrückzahlung, 35.000 EUR Bankentlastung und Maschinensicherheit getrennt. Die Kölner Vergleichsgutachten stimmen weiterhin mit den Fallzweigen 150.000 EUR Direktzahlung beziehungsweise 96.000 EUR Zahlung an Quast überein. Die neue Antragsdarstellung verändert diese Prüfaufträge und die streitigen Parteipositionen nicht.

## 2. Freigabe und Grenze

Das vorhandene Vergleichsmaterial kann für die neu gesetzten Akten weiterverwendet werden. Die Prüfung gibt den Abgleich von Sachverhalt, Anlagenzuordnung und Verweisen nach einer Formänderung frei. Sie ist keine erneute vollständige Aktualitätsprüfung sämtlicher Rechtsquellen, keine Neubewertung der didaktisch streitigen Parteithesen und keine Bestätigung tatsächlich eingereichter Schriftsätze.

## 3. Bestandsfortschreibung

`inspect_material(expected_material())` wurde auf dem tatsächlichen Dateibestand ausgeführt. Es ergaben sich genau die fünf erwarteten Abweichungen, jeweils ausschließlich im Wert `aktenstand.sha256`. Die Dateizahl beträgt weiterhin 62 für Weserfunken und jeweils 24 für die vier anderen Akten.

In `quality/insolvenz-testakten/bestand.json` wurden nur diese fünf berechneten Aktenstandwerte übernommen. Vor dem Schreiben wurde programmatisch sichergestellt, dass sämtliche `material`-Einträge einschließlich Datei-, Quellen- und Vorlagenbasishashes sowie sämtliche anderen Akten vollständig unverändert sind. Es wurden weder Vergleichsmaterialien noch andere Akten neu erzeugt.
