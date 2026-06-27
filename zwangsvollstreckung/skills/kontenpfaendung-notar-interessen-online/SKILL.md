---
name: kontenpfaendung-notar-interessen-online
description: "Kontopfändung per Pfändungs- und Überweisungsbeschluss: Antrag, Forderungsaufstellung, Bank als Drittschuldner, Paragraf-840-Erklärung, P-Konto, elektronische Einreichung und digitale Zustellung an Kreditinstitute ab 2027."
---

# Kontopfändung: Pfändungs- und Überweisungsbeschluss gegen Banken

## Einsatzlage

Nutze diesen Skill, wenn der Gläubiger ein Bankkonto des Schuldners pfänden will. Der Skill erzeugt eine prüffähige Antragsroute für den Pfändungs- und Überweisungsbeschluss, trennt Antrag an das Vollstreckungsgericht von Zustellung durch den Gerichtsvollzieher und berücksichtigt die Digitalstufen der Zwangsvollstreckung ab 2026 und 2027.

## Kaltstart-Rückfragen

1. Welcher Titel liegt vor, und sind Klausel, Zustellung, Sicherheitsleistung und Wartefrist erledigt?
2. Welche Bank ist Drittschuldner: vollständige Firma, Anschrift, bekannte IBAN, Filiale, zentrale Pfändungsadresse?
3. Welche Forderung wird gepfändet: Hauptforderung, Zinsen, Kosten, Vollstreckungskosten, laufende Ansprüche?
4. Ist mit P-Konto, Sozialleistungen, Arbeitseinkommen, Insolvenzverfahren oder Vollstreckungsschutz zu rechnen?
5. Soll die Zustellung besonders beschleunigt werden: Gerichtsvollzieher, elektronische Übermittlung, ab 1.6.2027 Bank mit sicherem Übermittlungsweg?

## Normenanker

| Thema | Anker | Arbeitsregel |
| --- | --- | --- |
| Titelvoraussetzungen | Paragraf 704, 724, 750 ZPO | Vor Antrag vollständig prüfen |
| Forderungspfändung | Paragraf 829 ZPO | Pfändung entsteht mit Zustellung an den Drittschuldner |
| Elektronischer Antrag | Paragraf 829a ZPO n.F. | Ab 1.10.2026 erleichterte elektronische Antragstellung mit elektronischen Kopien |
| Strukturierter Antrag | Paragraf 829 Absatz 5 ZPO n.F. | Ab 1.1.2027 können PDF und strukturierter XML-Datensatz eingereicht werden; bei Widerspruch zählt XML |
| Drittschuldnererklärung | Paragraf 840 ZPO | Bank zur Erklärung über Bestand, Rechte Dritter und Vorpfändungen auffordern |
| Schuldnerschutz | Paragraf 850k ZPO | P-Konto und Freibeträge mitdenken, aber nicht im Pfändungsantrag lösen |
| Elektronische Zustellung an Banken | Paragraf 173 Absatz 2 Nummer 1 ZPO n.F. | Kreditinstitute müssen ab 1.6.2027 einen sicheren Übermittlungsweg eröffnen |
| Insolvenz | Paragraf 89 InsO | Nach Verfahrenseröffnung Einzelvollstreckung grundsätzlich sperren |

## Workflow

1. Vollstreckungsreife feststellen: Titel, Klausel, Zustellung, Sicherheitsleistung, Zustellungsurkunden und Forderungsaufstellung.
2. Zuständiges Vollstreckungsgericht bestimmen: regelmäßig Amtsgericht am allgemeinen Gerichtsstand des Schuldners.
3. Drittschuldner sauber bezeichnen: Kreditinstitut mit zutreffender juristischer Person; bei Unsicherheit zentrale Pfändungsadresse recherchieren.
4. Forderungsaufstellung erstellen: Hauptforderung, Zinsen mit Zeitraum und Zinssatz, titulierte Kosten, bisherige Vollstreckungskosten, Gesamtbetrag.
5. Antrag formulieren: Pfändung des Anspruchs auf Auszahlung und Gutschrift aus Kontoverbindung, Überweisung zur Einziehung, Zustellung an die Bank.
6. Paragraf-840-Erklärung mit beantragen: Anerkennung, Zahlungsbereitschaft, entgegenstehende Rechte, Vorpfändungen, andere Gläubiger, P-Konto-Hinweise.
7. Zustellung steuern: Gerichtsvollzieherzustellung an die Bank als Drittschuldner; Schuldnerzustellung nachgelagert dokumentieren.
8. Digitalroute wählen:
   - Bis 30.9.2026: bisherige elektronische Einreichung nach allgemeinen Regeln oder Papierweg.
   - Ab 1.10.2026: Paragraf 829a ZPO n.F. für elektronische Kopien von Titel, Klausel und Zustellungsnachweis nutzen.
   - Ab 1.1.2027: PDF-Antrag und, wenn verfügbar, strukturierten XML-Datensatz nach Paragraf 829 Absatz 5 ZPO n.F. konsistent halten.
   - Ab 1.6.2027: Zustellung an Kreditinstitute regelmäßig über deren sicheren Übermittlungsweg vorbereiten.
9. Nachlauf überwachen: Eingang der Drittschuldnererklärung, Zahlung der Bank, P-Konto-Freigaben, Rang, Vorpfändungen und Folgepfändung.

## Digitalmatrix

| Datum | Änderung | Auswirkung auf den Antrag |
| --- | --- | --- |
| 1.10.2026 | Elektronischer PfÜB-Antrag nach Paragraf 829a ZPO n.F. | Elektronische Kopien können genügen, wenn Identität und Forderungsfortbestand versichert werden |
| 1.1.2027 | Strukturierter Datensatz nach Paragraf 829 Absatz 5 ZPO n.F. | PDF und XML müssen inhaltlich gleich laufen; XML entscheidet bei Abweichung |
| 1.6.2027 | Kreditinstitute mit sicherem Übermittlungsweg nach Paragraf 173 Absatz 2 Nummer 1 ZPO n.F. | Gerichtsvollzieher kann die Bankzustellung digital abwickeln; Zustellnachweis eng kontrollieren |

## Antragsskelett

```text
An das Amtsgericht [Ort] als Vollstreckungsgericht

In der Zwangsvollstreckung
[Gläubiger] gegen [Schuldner]
aus [Titel, Gericht/Notar, Datum, Aktenzeichen]

beantragen wir den Erlass eines Pfändungs- und Überweisungsbeschlusses.

Drittschuldner:
[Kreditinstitut, vollständige Firma, Anschrift, bekannte IBAN/Kontonummer]

Gepfändet werden die Ansprüche des Schuldners gegen den Drittschuldner aus der Kontoverbindung, insbesondere auf Auszahlung, Überweisung, Gutschrift, Rechnungsabschluss und Herausgabe pfändbarer Guthaben.

Die gepfändeten Ansprüche werden dem Gläubiger zur Einziehung überwiesen.

Der Drittschuldner wird aufgefordert, die Erklärung nach Paragraf 840 ZPO abzugeben.

Anlagen:
- Vollstreckbarer Titel
- Klausel
- Zustellungsnachweis
- Forderungsaufstellung
- Nachweise zu Kosten und Zinsen
```

## Fehlerquellen

| Fehler | Folge | Reparatur |
| --- | --- | --- |
| Falsche Bankgesellschaft | Zustellung läuft ins Leere | Juristische Person und zentrale Pfändungsadresse prüfen |
| Zinsen unklar | Kürzung oder Rückfrage | Zeitraum, Zinssatz und Berechnungsgrundlage tabellarisch ausweisen |
| P-Konto ignoriert | Zahlung geringer als erwartet | Freibeträge einplanen, aber Antrag nicht unnötig beschränken |
| XML weicht ab 2027 vom PDF ab | Strukturdaten können maßgeblich sein | Daten vor Einreichung abgleichen |
| Insolvenz eröffnet | Einzelvollstreckung unzulässig | Insolvenzbekanntmachungen prüfen und Forderungsanmeldung erwägen |

## Qualitätsgates

- Pfändung entsteht erst mit wirksamer Zustellung an die Bank als Drittschuldner; Eingangsbestätigung des Gerichts genügt nicht.
- Paragraf-840-Erklärung immer mitziehen und Nachfrist setzen, wenn die Bank nicht reagiert.
- Ab 1.1.2027 PDF und XML nicht getrennt pflegen; jede Betragsänderung muss in beiden Fassungen identisch sein.
- Ab 1.6.2027 elektronische Bankzustellung nicht nur behaupten, sondern Zustellnachweis und Übermittlungsweg dokumentieren.
