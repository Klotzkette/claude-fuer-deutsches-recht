# Erbrecht: Patchwork-Erbfolge und Stiefgroßvater in Karlsruhe


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 29 KB) | PDF | [`gesamt-pdf/erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe_gesamt.pdf`](gesamt-pdf/erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `fachanwalt-erbrecht`.

## Kurzbild

Vier Jugendfreunde aus Karlsruhe heirateten, trennten sich und verbanden ihre Familien neu: Armin heiratete Beate, Clemens heiratete Dana. Nach Scheidungen heiratete Armin Dana. Clemens und Dana hatten die Tochter Fiona. Nach der Scheidung von Armin und Dana heiratete Armin viele Jahre später die inzwischen erwachsene Fiona. Nun sterben Armin und Clemens kurz nacheinander. Die Akte fragt, wer nach gesetzlicher Erbfolge, früheren Testamenten, Scheidung und Stiefverwandtschaft welche Position hat.

## Aktenstücke

| Datei | Inhalt |
| --- | --- |
| `01_familienstammbaum_und_zeitstrahl.docx` | Beziehungen, Ehen, Scheidungen, Todesfälle |
| `02_testamente_und_scheidungen.docx` | Frühere Verfügungen und Scheidungsklauseln |
| `03_nachlass_armin.docx` | Vermögen Armin, Ehe mit Fiona, Streit um Ehegattenerbrecht |
| `04_nachlass_clemens.docx` | Vermögen Clemens, Tochter Fiona, frühere Ehe mit Dana |
| `05_erbscheinantrag_fiona.docx` | Antrag und Gegenargumente |
| `06_stammbaum_matrix.csv` | Personen, Verwandtschaft, erbrechtliche Rolle |
| `07_pruefvermerk_erbreihenfolge.docx` | Chronologische Lösung der beiden Erbfälle |
| `08_standesamt_registerauszuege.docx` | Standesamtliche Registerauskunft zu Ehen, Scheidungen, Abstammung und Namensführung |
| `09_email_nachlassgericht_rueckfrage.eml` | Nachlassgerichtliche Rückfrage zu Personenstand und Antragsfassung (4 VI 312/26) |
| `10_familienchat_auszug.txt` | Familiennachrichten mit tatsächlichen Hinweisen zu Beziehungen und Nachlassbesitz |
| `11_testament_armin_beate_1994_abschrift.docx` | Gemeinschaftliches Testament 1994 mit Schlusserbenklausel und Eröffnungsvermerk |
| `12_testament_armin_2014_abschrift.docx` | Testament Armins von 2014 mit Zuwendungen an Dana und Fiona |
| `13_testament_clemens_2018_abschrift.docx` | Testament Clemens' von 2018: Fiona Alleinerbin, Ausschluss Danas |
| `14_sterbeurkunden_abschriften.docx` | Sterbeurkunden beider Erblasser mit urkundlicher Reihenfolge der Erbfälle |

## Aktenstruktur

```text
erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe/
├── 01_familienstammbaum_und_zeitstrahl.docx      Personen, Ehen, Scheidungen, Todesfälle im Zeitstrahl
├── 02_testamente_und_scheidungen.docx            Überblick über alle Verfügungen und Scheidungsfolgen
├── 03_nachlass_armin.docx                        Vermögen Armins, Erbscheinlage, Ehe mit Fiona
├── 04_nachlass_clemens.docx                      Vermögen Clemens', Tochter Fiona, frühere Ehe mit Dana
├── 05_erbscheinantrag_fiona.docx                 Antrag Fionas, Gegenargumente von Beate und Dana
├── 06_stammbaum_matrix.csv                     Statusmatrix: Person, Verwandtschaft, mögliche Rolle
├── 07_pruefvermerk_erbreihenfolge.docx           Kanzleivermerk zur chronologischen Lösung beider Erbfälle
├── 08_standesamt_registerauszuege.docx           Registerauskunft des Standesamts Karlsruhe an das Nachlassgericht
├── 09_email_nachlassgericht_rueckfrage.eml     Rückfrage des AG Karlsruhe zum Erbscheinantrag
├── 10_familienchat_auszug.txt                  Messenger-Export: Unterlagenbesitz und Positionen der Beteiligten
├── 11_testament_armin_beate_1994_abschrift.docx  Gemeinschaftliches Testament 1994 (Abschrift, eröffnet)
├── 12_testament_armin_2014_abschrift.docx        Testament 2014 (Abschrift, eröffnet, Auslegungsfragen)
├── 13_testament_clemens_2018_abschrift.docx      Testament 2018 aus amtlicher Verwahrung (Abschrift)
├── 14_sterbeurkunden_abschriften.docx            Sterbeurkunden Armin (14.05.2026) und Clemens (02.06.2026)
├── README.md                                   Diese Übersicht
├── rubric.yaml                                 Prüfkriterien für die Bearbeitung
└── gesamt-pdf/
    └── erbrecht-patchwork-stiefgrossvater-erbfolge-karlsruhe_gesamt.pdf  Lesefassung der Gesamtakte
```

## Bearbeitungsziel

Die Akte ist eine Verwandtschafts- und Erbfolgefalle: Es geht nicht um Sensation, sondern um präzise Statusprüfung. Ehe, Scheidung, frühere letztwillige Verfügung, Stiefverhältnis, Abkömmling, Ehegattenerbrecht und gleichzeitige beziehungsweise kurz nacheinander eintretende Erbfälle müssen sauber getrennt werden.
