# Rentenrecht: Hinterbliebenenrente, KVdR und Pflegezeiten in Bremen

Akte einer Witwe mit Witwenrentenbescheid, eigener kleiner Rente, Unterstützungskasse, Einkommensanrechnung, Krankenversicherung der Rentner und ungeklärten Pflegezeiten des verstorbenen Ehemanns.

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 54 KB) | PDF | [`gesamt-pdf/rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen_gesamt.pdf`](gesamt-pdf/rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `rentenpruefer`.

## Kurzbild

Helga Bruns, 68, ist seit dem 21.04.2026 verwitwet. Die DRV Oldenburg-Bremen bewilligt eine große Witwenrente, rechnet ab August 2026 aber ein Nettoeinkommen von 1.236,20 EUR an, das sich aus den vorliegenden Unterlagen nicht ergibt. Parallel verbeitragt die Weser Krankenkasse die Unterstützungskassenleistung als Versorgungsbezug und kündigt eine Nachberechnung ab Mai 2023 an. Die Pflegekasse hat für die zweijährige häusliche Pflege des Ehemanns nur lückenhaft Rentenbeiträge gezahlt — und zwar in das Konto der Mandantin, die fest davon ausgeht, die Pflege müsse die Rente ihres Mannes erhöht haben.

Die Akte verlangt die saubere Trennung von Sterbevierteljahr und Einkommensanrechnung, die beitragsrechtliche Einordnung dreier Zahlungsströme in der KVdR und die Aufklärung der Pflegebeitragslücken samt Zuordnungsfrage.

Neu hinzugekommen ist ein vierter Streitpunkt: Die Weser Krankenkasse stellt nach dem Tod des Ehemannes die KVdR-Pflichtmitgliedschaft der Mandantin selbst in Frage und droht mit dem Wechsel in die deutlich teurere freiwillige Versicherung. Sie zählt für die Vorversicherungszeit nur die gesetzlich belegten Monate und übergeht die Kindererziehung der drei Kinder Anke, Torben und Wiebke. Ob die Neun-Zehntel-Belegung erfüllt ist, entscheidet sich rechnerisch an dieser Anrechnung.

## Aktenstruktur

```
rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen/
├── README.md                                  ← diese Datei
├── 01_mandatsaufnahme.docx                      ← Kanzleivermerk: Beteiligte, Fristen, Arbeitsauftrag
├── 02_drv_bescheid_witwenrente.docx             ← Bewilligungsbescheid mit Sterbevierteljahr, Anrechnung, Rechtsbehelfsbelehrung
├── 03_unterstuetzungskasse_leistungsmitteilung.docx ← Zahlstelle erklärt Beitragsabzug ab Juni 2026
├── 04_krankenkasse_beitragsmitteilung.docx      ← KVdR-Einordnung, Beitragssätze, angekündigte Nachberechnung
├── 05_pflegekasse_bescheinigung.docx            ← Pflegegrad, gemeldete Pflegeperson, lückenhafte Beitragszeiträume
├── 06_pflegedienst_leistungsnachweis.docx       ← Dokumentationsauszug zum Pflegeumfang der Ehefrau
├── 07_versicherungsverlauf_auszug_mandantin.docx ← Kontoauszug DRV mit Pflegebeiträgen und Speicherlücke
├── 08_widerspruch_kanzlei.docx                  ← fristwahrender Widerspruch mit Auskunftsanträgen
├── 09_drv_eingangsbestaetigung.docx             ← Eingangsbestätigung, Begründungsfrist, Fachreferats-Abgabe
├── 10_kontoauszug_zahlungseingaenge.txt         ← Zahlungseingänge Juni 2026 mit Notiz der Mandantin
├── 11_email_nachfragen_tochter.eml              ← Fragen der Tochter, Zeugin für den Erhebungsbogen 2023
├── 12_kvdr_vorversicherung_datenkern.csv        ← Datenkern: Rahmenfrist, Belegungszeiten, Kindererziehung; Neun-Zehntel-Belegung nachrechenbar
├── 13_anwaltliche_stellungnahme_kvdr_2026-07-03.md ← Stellungnahme an die Krankenkasse: Kindererziehung führt über die Schwelle
├── 14_drv_bescheinigung_kindererziehungszeiten_2026-06-29.md ← DRV-Bescheinigung der drei Kindererziehungszeiten
├── rubric.yaml                                  ← Prüfkriterien für die Bearbeitung
├── eml/
    ├── 01_weser_kk_kvdr_ueberpruefung.eml       ← Krankenkasse: Vorversicherungszeit angeblich nicht erfüllt (172 von 252)
    ├── 02_kanzlei_an_weser_kk_kindererziehung.eml ← Kanzlei: drei Kinder mal drei Jahre erfüllen die Schwelle
    ├── 03_pflegekasse_erhebungsbogen.eml        ← Pflegekasse zur Beitragslücke 07/2023 bis 11/2023 und zur Zeugin
    └── chatverlauf_geschwister_bruns.txt        ← WhatsApp-Export der drei Kinder zur Suche der Geburtsurkunden
├── 91_fristsachen_belege_offene_punkte_2026-07-06.csv    # Fristsachen, Belege und offene Punkte (Ergaenzung v426)
└── eml/2026-07-06_sachstand_nachforderung.eml            # Sachstand zur Nachforderung (Ergaenzung v426)
```

Der Datenkern in `12_kvdr_vorversicherung_datenkern.csv` macht den KVdR-Streit rechnerisch nachvollziehbar: Zweite Rahmenfristhälfte 280 Monate, Schwelle 252 Monate, belegt 172 Monate, Kindererziehung 108 Monate, zusammen 280 Monate. Die Krankenkasse kommt nur deshalb auf ein Fehlen der Vorversicherungszeit, weil sie die 108 Monate Kindererziehung nicht mitzählt.

## Bearbeitungsziel

Die Akte soll eine Rentenberatung zwingen, den Anrechnungsbetrag nicht hinzunehmen, sondern die Herkunft des angesetzten Nettoeinkommens aufzuklären, die Verbeitragung der drei Zahlungsströme einzeln zu prüfen (einschließlich Freibetragsfragen beim Versorgungsbezug) und die Pflegebeitragslücken Juli bis November 2023 sowie das Beitragsende März 2024 rechtlich einzuordnen, ohne die Erwartung der Mandantin ungeprüft zu übernehmen.
