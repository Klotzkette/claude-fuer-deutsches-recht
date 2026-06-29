---
name: dokumente-intake
description: "Dokumentenintake fuer Forderungsakten: liest eine vorhandene Ordner- oder ZIP-Struktur zuerst aus, sortiert Vertrag, Leistung, Rechnung, Mahnung, Zahlung, Mahnbescheid, Widerspruch, Titel und Vollstreckungsunterlagen und erzeugt daraus Akteninventar, Belegmatrix und Lueckenliste."
---

# Dokumente Intake

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

Eingang einer Forderungssache ohne saubere Aktenstruktur fuehrt zwei Wochen später zum Belegchaos. Dieser Skill normiert die Aufnahme, aber ohne den Nutzer mit Fragen zu erschlagen: erst Dokumente auswerten, dann Luecken fragen.

## Ordner zuerst auslesen

Wenn ein Ordner, ZIP oder Dokumentenstapel vorhanden ist:

1. Dateiliste mit Namen, Format, erkennbarem Datum und vermuteter Funktion erstellen.
2. Briefkoepfe, Signaturen, Vollmacht, Rechnungssteller, Rechnungsempfaenger und Aktenzeichen abgleichen.
3. Rechnungs- und Zahlungsdaten aus Kontoauszuegen, Avisen und Gutschriften gegenueberstellen.
4. Mahnungen, Fristsetzungen und Zugangsbelege in eine Chronologie bringen.
5. Gerichtliche Dokumente gesondert markieren: Mahnbescheid, Widerspruch, Vollstreckungsbescheid, Klage, Verfuegung.
6. Nur danach gezielt Luecken abfragen.

## Intake-Checkliste

| Kategorie | Typische Dokumente | Pflicht |
|---|---|---|
| Vertragsunterlagen | Angebot Annahme Bestellung AGB Auftragsbestaetigung | ja |
| Leistungsnachweis | Lieferschein Abnahmeprotokoll Stundenzettel Zeitnachweis | ja |
| Rechnung | Rechnung Schlussrechnung Gutschrift Korrektur | ja |
| Mahnungen | Erstmahnung Zweitmahnung Anwaltsschreiben | ja |
| Schuldnerkommunikation | E-Mails Briefe Telefonvermerke | ja sofern vorhanden |
| Zahlungsbelege | Kontoauszug Verrechnungen Teilzahlungen | ja sofern vorhanden |
| Drittunterlagen | Handelsregister Auskunft Schufa SCHUFA-Auskunft | wenn vorhanden |
| Verfahrensunterlagen | bisheriger Schriftverkehr Gegenseitige Anwaltsbriefe | ja sofern vorhanden |

## Erste Ausgabe

```text
Akteninventar:
- sichere Dokumente:
- unsichere Dokumente:
- doppelte oder widerspruechliche Dokumente:
- fehlende Dokumente:

Parteienhypothese:
- mutmasslicher Glaeubiger:
- mutmasslicher Schuldner:
- Vertreter:
- Zustellanschrift:

Naechste Rueckfragen:
1. [...]
2. [...]
3. [...]
```

## Aktenstruktur

```
[Aktenzeichen]/
  01_Mandat/
    Vollmacht.pdf
    Auftragsbestaetigung.pdf
  02_Vertrag/
    Vertrag.pdf
    AGB.pdf
  03_Leistung/
    Lieferschein.pdf
  04_Rechnung/
    Rechnung_2024-117.pdf
  05_Mahnung/
    Mahnung_01.pdf
    Mahnung_02_Anwalt.pdf
  06_Kommunikation/
    E-Mails.pdf
  07_Schriftsatz/
    Klage.docx
  08_Belege_Anlagen_K/
    K_01.pdf
```

## Einsichtsanspruch BGB 810

Mandantin kann von Dritten Einsicht in Urkunden verlangen die in ihrem Interesse errichtet wurden oder ein Rechtsverhaeltnis dokumentieren. Bei Werkvertraegen wichtig für Massenermittlung.

## Vorlagepflicht im Prozess

- ZPO 142 das Gericht kann Vorlage anordnen
- ZPO 422 423 Vorlagepflicht der Gegenpartei

## Norm-Pinpoints

- ZPO 142 422 423
- BGB 810

## Quellen

- [ZPO 142](https://www.gesetze-im-internet.de/zpo/__142.html)
- [BGB 810](https://www.gesetze-im-internet.de/bgb/__810.html)
