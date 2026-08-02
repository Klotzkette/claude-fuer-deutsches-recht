# Rentenrecht: Betriebsrente, Direktversicherung und Zusatzversorgung in Hannover

Akte einer Arbeitnehmerin kurz vor Rentenbeginn mit gesetzlicher Rente, kommunaler Zusatzversorgung, Direktversicherung und privater Rentenversicherung. Schwerpunkt ist die Nettoentscheidung zwischen Kapitalwahl, Betriebsrente, KVdR und privater Vorsorge.

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/rentenrecht-betriebsrente-direktversicherung-vbl-hannover_gesamt.pdf`](gesamt-pdf/rentenrecht-betriebsrente-direktversicherung-vbl-hannover_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-betriebsrente-direktversicherung-vbl-hannover.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-betriebsrente-direktversicherung-vbl-hannover.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-betriebsrente-direktversicherung-vbl-hannover-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-betriebsrente-direktversicherung-vbl-hannover-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `rentenpruefer`.

## Kurzbild

Dagmar Ellersen, 61, Hauswirtschaftsleitung einer Klinik-Servicegesellschaft, will zwischen Ende 2027 und 2031 in Rente und muss vier Säulen zusammenbringen: gesetzliche Rente (1.742,60 EUR bei Regelbeginn, 14,4 Prozent Abschlag bei Beginn Dezember 2027), Zusatzversorgungskasse (318,40 EUR, aber fünf Jahre vor dem Konzernwechsel fehlen — ein alter VBL-Nachweis taucht erst spät auf), Direktversicherung mit Kapitalwahlrecht (61.900 EUR oder 213,40 EUR Rente, Wahlfrist sechs Monate vor Abruf) und eine private Police von 1998 ohne ausgewiesenen Rentenfaktor. Dazu ein marodes Dach für 28.400 EUR, ein Ehemann mit anderer Risikoneigung und eine ältere Renteninformation, die 70 EUR mehr versprach als die aktuelle Auskunft.

Kein Bescheid ist angegriffen; die Akte ist ein reines Gestaltungs- und Rechenmandat unter Fristdruck (Kapitalwahl bis Ende Mai 2027 bei Beginn Dezember 2027).

## Aktenstruktur

```
rentenrecht-betriebsrente-direktversicherung-vbl-hannover/
├── README.md                                   ← diese Datei
├── 02_drv_rentenauskunft.docx                    ← Rentenauskunft mit Abschlagstabelle für drei Beginntermine
├── 03_zusatzversorgungskasse_auskunft.docx       ← Betriebsrente 318,40 EUR, fehlende Zeiten vor 07/2004, Überleitungshinweis
├── 04_arbeitgeberbescheinigung_entgeltumwandlung.docx ← Beschäftigungszeiten, ZVK-Meldung, Entgeltumwandlung seit 2004
├── 05_direktversicherung_standmitteilung.docx    ← Rente oder Kapital, Wahlfrist, fehlende Kostenaufschlüsselung
├── 06_private_rente_standmitteilung.docx         ← Police von 1998 ohne Rentenfaktor, unklares Bezugsrecht
├── 07_anfrage_direktversicherung.docx            ← Auskunftsersuchen der Beraterin mit Fristsetzung
├── 08_anfrage_private_rente.docx                 ← Auskunftsersuchen zu Rentenfaktor, Abruffenster, Bezugsrecht
├── 09_krankenkasse_auskunft_versorgungsbezuege.docx ← Verbeitragung von Betriebsrente, Kapital und privater Rente
├── 10_renteninformation_2022_vergleich.docx      ← ältere Hochrechnung 1.812,45 EUR und Klärungsnotiz
├── 11_mehrsaeulenplan.csv                      ← Arbeitsraster der Beraterin über alle vier Säulen
├── 12_email_mandantin_kapitalwahl.eml          ← Dachsanierung, VBL-Zettel von 1999, Grundsatzfragen
├── 13_antwort_direktversicherung.md            ← Antwort der Hannoversche Vorsorge: Werte für drei Abruftermine, Rentenfaktor, Kostenausweis 2004–2011 noch offen
├── 14_email_vbl_zwischennachricht.eml          ← VBL bestätigt Pflichtversicherung 1999–2004, Meldelücke zweites Halbjahr 2001, Überleitung nur auf Antrag
└── 15_haushaltsrechnung_ellersen.csv           ← Monatliche Ausgabenübersicht der Mandantin mit Dachrücklage und offenen Posten
```

## Bearbeitungsziel

Die Akte soll eine Beratung erzwingen, die die drei Beginn-Szenarien netto durchrechnet, die Kapitalwahl gegen die lebenslange Rente unter Beitrags- und Steuergesichtspunkten abwägt, die fehlenden Zusatzversorgungsjahre 1999 bis 2004 über den aufgetauchten VBL-Nachweis verfolgt und die Differenz zwischen Renteninformation 2022 und Rentenauskunft 2026 sauber erklärt — ohne den Fristenkalender (Kapitalwahl, Formular ZV-A 12, Antwortfristen) aus dem Blick zu verlieren.
