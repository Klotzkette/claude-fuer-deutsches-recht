# Akte: Revision nach abgelehntem Beweisantrag Duisburg

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/strafrecht-revision-beweisantrag-lg-duisburg_gesamt.pdf`](gesamt-pdf/strafrecht-revision-beweisantrag-lg-duisburg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-strafrecht-revision-beweisantrag-lg-duisburg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-revision-beweisantrag-lg-duisburg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-strafrecht-revision-beweisantrag-lg-duisburg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-revision-beweisantrag-lg-duisburg-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

## Sachverhalt

Das Landgericht Duisburg verurteilte Murat Candan wegen eines Überfalls auf einen Getränkemarkt. Die Kammer stützte sich wesentlich auf die Aussage eines Mitangeklagten und eine unscharfe Videoaufnahme. Die Verteidigung hatte beantragt, den Taxifahrer Karol Nowak zu vernehmen, der Candan zur Tatzeit am Bahnhof gesehen haben will. Der Antrag wurde als bedeutungslos abgelehnt.

Das Hauptverhandlungsprotokoll enthält den Wortlaut des Beweisantrags nur verkürzt. Die Verteidigung besitzt eine eigene Mitschrift und den eingereichten Antrag als PDF. Die Urteilsgründe würdigen das Alibi nur knapp und verweisen darauf, der Taxifahrer könne sich wegen vieler Fahrten nicht zuverlässig erinnern. Eine tatsächliche Vernehmung fand nicht statt.

Die Akte zwingt zur revisionsrechtlichen Präzision: Rügebegründung, Protokolllage, Darlegung der Konnexität, Aufklärungsrüge und Sachrüge müssen sauber getrennt werden. Gleichzeitig ist eine mögliche Protokollberichtigung taktisch zu bewerten.

Der Beweiskern liegt im Abgleich der Hauptverhandlungs-Chronologie mit den beiden Protokollfassungen. Die Datei `10_hauptverhandlung_protokoll_chronologie.csv` erfasst je Sitzungstag die relevanten Vorgänge mit Quelle und Protokolldeckung; erst die Verbindung mit der Gegenüberstellung von amtlichem Protokoll und Verteidiger-Mitschrift sowie der Berichtigungskorrespondenz macht den Verfahrensfehler und die für § 274 StPO maßgeblichen Divergenzen sichtbar.

## Verfahrensstand

Gericht: Bundesgerichtshof über Landgericht Duisburg, 7 KLs 220 Js 1180/25

Staatsanwaltschaft: Staatsanwaltschaft Duisburg, 220 Js 1180/25

Verteidigung oder Vertretung: RA Dr. Enno Falkenberg, Essen

Mandatsbezug: Murat Candan, verurteilt wegen schweren Raubes

## Beteiligte

| Name | Rolle |
| --- | --- |
| Murat Candan | Angeklagter und Revisionsführer, verurteilt wegen schweren Raubes |
| Dennis Krawczyk | Mitangeklagter und Belastungszeuge |
| Karol Nowak | Taxifahrer, benannter Alibizeuge |
| VRiLG Dr. Hartmut Söllner | Vorsitzender der 7. Großen Strafkammer |
| Getränkemarkt Rheinperle | Tatort des abgeurteilten Überfalls |
| Taxi-Ruf Duisburg | Arbeitgeber des Zeugen Nowak, Fahrtenprotokoll |
| RA Dr. Enno Falkenberg | Verteidiger und Revisionsführer |

## Zeitachse

| Datum | Vorgang |
| --- | --- |
| 12.02.2026 | Urteil Landgericht Duisburg: fünf Jahre und sechs Monate |
| 12.02.2026 | Revision zu Protokoll eingelegt |
| 20.04.2026 | schriftliche Urteilsgründe zugestellt |
| 20.05.2026 | Fristende Revisionsbegründung |
| 07.06.2026 | Protokollberichtigung durch Vorsitzenden angeregt |
| 18.06.2026 | Erwiderung auf Berichtigungsvermerk vorbereitet |

## Aktenstruktur

```
strafrecht-revision-beweisantrag-lg-duisburg/
├── 02_sachverhalt_chronologie.docx                     Ausformulierter Sachverhalt, Zeitachse und offene Widersprüche
├── 03_ermittlungsakte_auszuege.docx                    Auszüge aus Verfahrens- und Urteilsunterlagen
├── 04_beweismittel_und_arbeitsauftraege.xlsx           Beweismittelmatrix mit Belastungs- und Entlastungsrichtungen
├── 05_fristen_und_verfahrensstand.csv                  Fristen, Termine, Zustellungen und Wiedervorlagen
├── 06_email_akteneinsicht_und_rueckfragen.eml          E-Mail zu Akteneinsicht und Nachforderungen
├── 07_rechtliche_arbeitsnotiz.docx                     Normanker, Beweislastfragen, taktische Linien
├── 08_entwurf_verfahrensschritt.docx                   Entwurf für Rechtsmittelbegründung oder Antrag
├── 09_originalanlage_behoerdenvermerk.pdf              PDF-Anlage mit behördlichem oder fachlichem Vermerk
├── 10_hauptverhandlung_protokoll_chronologie.csv      Sitzungschronologie mit Quelle und Protokolldeckung (Datenauswertungs-Kern)
├── 11_revisionsbegruendung_bgh_2026-05-19.docx         Ausformulierte Revisionsbegründung mit Verfahrens-, Aufklärungs- und Sachrüge
├── 12_protokollauszug_und_mitschrift_2026-02-12.docx   Gegenüberstellung amtliches Protokoll und Verteidiger-Mitschrift
├── 13_telefonvermerk_zeuge_nowak_2026-06-20.docx         Telefonvermerk zum Erinnerungsstand des Zeugen, GPS-Verlauf und Urlaubszeiten
├── eml/
│   ├── 01_falkenberg_protokollberichtigung_2026-06-07.eml Anregung der Protokollberichtigung an den Vorsitzenden
│   ├── 02_vorsitzender_berichtigungsvermerk_2026-06-15.eml Ablehnung der Berichtigung durch den Vorsitzenden
│   ├── 03_taxiruf_nowak_verfuegbarkeit_2026-05-12.eml     Verfügbarkeit des Zeugen Nowak und Fahrtenprotokoll
│   └── 04_lg_duisburg_aktenvorlage_bgh_2026-06-26.eml     Mitteilung der Geschäftsstelle zur Aktenvorlage an den Generalbundesanwalt
├── whatsapp/
│   └── chatverlauf.txt                                  Chat Nowak/Disposition der Tatnacht: Aufnahme Bahnhof 21:18 Uhr
├── README.md                                            Diese Übersicht
└── rubric.yaml                                          Prüfpunkte für die Bearbeitung der Akte
```

## Prüffokus

- Verurteilung wegen schweren Raubes
- Revision mit Verfahrens- und Sachrüge
- Beweisantragsablehnung nach Paragraf 244 StPO
- Beweiswert und Beweisverwertungsfragen getrennt prüfen.
- Nebenfolgen, Fristen und Verfahrensziel früh sichtbar machen.

## Passende Arbeitsrichtungen

`fachanwalt-strafrecht`, `richter-landgericht-strafkammer`, `subsumtions-pruefer`
