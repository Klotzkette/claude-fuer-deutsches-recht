---
name: dokumente-intake
description: "Dokumentenintake für Forderungsmanagement Klagewerkstatt: sortiert Mahnung, Mahnbescheid, Vollstreckungsbescheid, prüft Datum, Absender, Frist und Beweiswert (Vertrag, Rechnung); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumente Intake

Eingang einer Forderungssache ohne saubere Aktenstruktur fuehrt zwei Wochen spaeter zum Belegchaos. Dieser Skill normiert die Aufnahme.

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
