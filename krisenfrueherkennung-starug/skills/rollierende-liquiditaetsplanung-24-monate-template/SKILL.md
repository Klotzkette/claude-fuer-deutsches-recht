---
name: rollierende-liquiditaetsplanung-24-monate-template
description: "Erstellt eine rollierende Liquiditätsplanung für Status, Drei-Wochen-Sicht, 13-Wochen-Steuerung und die regelmäßige 24-Monats-Prognose nach Paragraf 18 Absatz 2 InsO."
---

# 1. Rollierende Liquiditätsplanung für 24 Monate

## 1.1. Arbeitsauftrag

Baue aus Kontoauszügen, OPOS, Verträgen, Titeln, Steuer- und Sozialversicherungsdaten sowie Finanzierungsunterlagen eine stichtagsbezogene Liquiditätsplanung. Verwende vorhandene Dateien zuerst. Fehlende Angaben werden als konkrete Nachforderung mit Auswirkung auf Status oder Prognose bezeichnet.

## 1.2. Rechtsrahmen

1. Paragraf 17 InsO: aktuelle Zahlungsunfähigkeit anhand fälliger Zahlungspflichten und verfügbarer Zahlungsmittel.
2. Paragraf 18 Absatz 2 InsO: drohende Zahlungsunfähigkeit; in aller Regel 24 Monate Prognosezeitraum.
3. Paragraf 19 Absatz 2 InsO: Überschuldung und in aller Regel zwölfmonatige Fortführungsprognose.
4. Paragraf 1 StaRUG: fortlaufende Überwachung bestandsgefährdender Entwicklungen, Gegenmaßnahmen und Organbericht; kein eigener fester 24-Monats-Zeitraum.
5. Paragraf 29 Absatz 1 StaRUG: gerichtliche Instrumente zur nachhaltigen Beseitigung drohender Zahlungsunfähigkeit.
6. Paragraf 50 Absatz 2 Nummer 2 StaRUG: gesonderter sechsmonatiger Finanzplan für den Antrag auf Stabilisierungsanordnung.

## 2. Vier Planungsebenen

| Ebene | Zweck | Granularität | Rechts- oder Praxisanker |
| --- | --- | --- | --- |
| Stichtagsstatus | heutige Deckung fälliger Pflichten | Einzelposten | Paragraf 17 InsO |
| Drei-Wochen-Sicht | Zahlungsstockung oder Zahlungsunfähigkeit abgrenzen | tag- oder wochenweise | BGH-Linie zu Paragraf 17 InsO |
| 13-Wochen-Steuerung | operative Zahlungssteuerung und Maßnahmen | wöchentlich | bewährtes Steuerungsmodell, keine gesetzliche Fixfrist |
| 24-Monats-Prognose | drohende Zahlungsunfähigkeit beurteilen | zunächst wöchentlich, danach monatlich | Paragraf 18 Absatz 2 InsO |

Die Ebenen dürfen nicht durch einen einzigen Monatssaldo ersetzt werden. Jede braucht eigenen Stichtag, eigenen Zweck und nachvollziehbare Quellen.

## 3. Datenmodell

### 3.1. Verfügbare Zahlungsmittel

Erfasse Kasse, Bankguthaben und tatsächlich frei verfügbare Kreditlinien. Eine Linie ist nur verfügbar, wenn Ziehungsvoraussetzungen erfüllt sind und keine Kündigung, Sperre oder Covenant-Folge entgegensteht. Noch zu verhandelnde Finanzierung ist keine sichere Liquidität, sondern eine Maßnahme mit Eintrittswahrscheinlichkeit und Long-Stop-Datum.

### 3.2. Zahlungspflichten

Jeder Abfluss erhält mindestens:

1. Gläubiger und Rechtsgrund.
2. Brutto- oder Nettobetrag.
3. Fälligkeit und etwaige Stundung.
4. Bestandsstatus: unstreitig, streitig nicht tituliert, tituliert, aufschiebend bedingt.
5. Vollstreckungsstatus.
6. Beleg und Fundstelle.
7. Verantwortlicher für rechtliche Klärung.

Nach BGH, Urteil vom 23.01.2025 - IX ZR 229/22, richtet sich die Berücksichtigung einer streitigen nicht titulierten Verbindlichkeit nach der objektiven Rechtslage. Besteht sie objektiv, darf sie nicht mit einer Prozessrisikoquote gekürzt werden; besteht sie objektiv nicht, begründet sie keine Zahlungsunfähigkeit. Bei einem vorläufig vollstreckbaren Titel und eingeleiteter Vollstreckung ist der Nennbetrag in der Liquiditätsprüfung anzusetzen. Unsicherheit wird nicht als beliebiger Prozentabschlag versteckt, sondern durch Rechtsvermerk, Belegstatus und Szenario transparent gemacht.

### 3.3. Zuflüsse

Ordne Forderungen nach Fälligkeit, Einbringlichkeit und tatsächlichem Zahlungstermin. Umsatzplanung ist erst dann Liquidität, wenn Debitorenlaufzeit, Ausfall, Aufrechnung, Skonto und Steuerwirkung berücksichtigt sind.

## 4. Modellstruktur

| Zeile | KW 1 | KW 2 | KW 3 | KW 4 | Monat 2 bis 3 | Monat 4 bis 24 | Quelle |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Anfangsliquidität | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Bank/Kasse |
| Sichere Kundenzahlungen | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | OPOS und Vertrag |
| Bedingte Zuflüsse | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Maßnahmenregister |
| Personal und Sozialversicherung | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Lohnlauf |
| Steuern | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Bescheid/Anmeldung |
| Lieferanten | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Kreditoren-OPOS |
| Finanzierung | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Kreditvertrag |
| Streitige Verbindlichkeiten | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Rechtsvermerk |
| Endliquidität | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | [EUR] | Formel |

## 5. Prämissen- und Maßnahmenbuch

| Kennung | Annahme oder Maßnahme | Base Case | Stressfall | Beleg | Verantwortlicher | Fällig | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P-01 | Debitorenlaufzeit | [Tage] | [Tage] | OPOS-Historie | [Name] | [Datum] | [Status] |
| M-01 | Kreditverlängerung | [Betrag] | [Betrag] | Term Sheet | [Name] | [Datum] | [Status] |

Jede Maßnahme wird nur angesetzt, wenn sie rechtlich und tatsächlich umsetzbar, finanziert und zeitlich passend ist. Der Plan enthält eine Rückfalllogik, falls sie ausbleibt.

## 6. Prüfworkflow

1. Datenstichtag und Bankbestände abstimmen.
2. OPOS mit Verträgen, Mahnungen, Titeln und Zahlungsverläufen abgleichen.
3. Fälligkeiten und Stundungen rechtlich prüfen.
4. Status nach Paragraf 17 InsO ohne Maßnahmenkosmetik feststellen.
5. Drei-Wochen-Entwicklung und Deckungslücke berechnen.
6. 13-Wochen-Steuerung mit sicheren und bedingten Maßnahmen trennen.
7. Regelmäßige 24-Monats-Prognose nach Paragraf 18 Absatz 2 InsO mit Base Case und Stressfall aufstellen.
8. Zwölfmonats-Fortführungsprognose nach Paragraf 19 Absatz 2 InsO gesondert beurteilen.
9. Plan-Ist-Abweichung, neue Erkenntnisse und Versionshistorie dokumentieren.
10. Geschäftsleitungsbeschluss mit Status, Maßnahmen, Organbericht und Wiedervorlage erstellen.

## 7. Ergebnisvermerk

```text
Stichtag: [Datum]
Datenstand: [Datum/Uhrzeit]

1. Paragraf 17 InsO
Fällige Zahlungspflichten: EUR [Betrag]
Verfügbare Zahlungsmittel: EUR [Betrag]
Deckungslücke: EUR [Betrag] beziehungsweise [Prozent]
Ergebnis und Begründung: [Text]

2. Paragraf 18 InsO
Regelmäßiger Prognosezeitraum: [von/bis]
Erster voraussichtlicher Unterdeckungszeitpunkt: [Datum]
Tragende Annahmen: [Text]
Ergebnis und Begründung: [Text]

3. Paragraf 19 InsO
Fortführungsprognose für den maßgeblichen Zeitraum: [Ergebnis]

4. Maßnahmen und Entscheidung
[Maßnahme, Betrag, Eintrittsvoraussetzung, Verantwortlicher, Termin]

5. Offene Rechts- und Belegfragen
[Frage, Auswirkung, Nachforderung]
```

## 8. Fehlerbremse

1. Paragraf 1 StaRUG nicht als Quelle eines festen 24-Monats-Zeitraums bezeichnen.
2. OPOS-Summen nie ohne Einzelposten, Fälligkeit und Beleg übernehmen.
3. Streitige Verbindlichkeiten nicht mit frei gewählten Prozessrisikoquoten kürzen.
4. Noch nicht vereinbarte Finanzierung nicht als freie Linie ausweisen.
5. Planwert, Buchwert und Liquiditätswirkung nicht vermischen.
6. Einen negativen Saldo nicht durch Maßnahmen beseitigen, deren Vollzug nach Eintritt der Unterdeckung liegt.
7. Bei möglicher Insolvenzreife unverzüglich Paragraf 15a InsO prüfen; die Maximalfristen betragen drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung.

## 9. Quellenregel

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden. Berufsständische Standards nur in der tatsächlich vorliegenden Fassung und als Methodenstandard kennzeichnen.
