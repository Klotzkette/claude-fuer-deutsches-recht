# Rentenrecht: Frühere Altersrente und Kontenlücken einer Werftmitarbeiterin

Mandatsakte einer langjährig beschäftigten Werftmitarbeiterin aus Kiel. Der Versicherungsverlauf enthält ungeklärte Monate, Pflegezeiten, Minijobphasen und eine teilablehnende Antwort der Deutschen Rentenversicherung. Die Fristen sind offen; Ziel ist eine belastbare 35- und 45-Jahre-Prüfung sowie ein Fahrplan für einen früheren Rentenbeginn.

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 56 KB) | PDF | [`gesamt-pdf/rentenrecht-fruehrente-kontenluecken-werft-kiel_gesamt.pdf`](gesamt-pdf/rentenrecht-fruehrente-kontenluecken-werft-kiel_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-fruehrente-kontenluecken-werft-kiel.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-fruehrente-kontenluecken-werft-kiel.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-fruehrente-kontenluecken-werft-kiel-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-fruehrente-kontenluecken-werft-kiel-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `rentenpruefer`.

## Kurzbild

Maren Thies, 63, seit 1982 im Kieler Werftumfeld, will im Frühjahr 2027 vorzeitig in Rente. Die Rentenauskunft weist für den Wunschbeginn 01.03.2027 einen Abschlag von 10,2 Prozent aus; für die abschlagsfreie Rente für besonders langjährig Versicherte fehlen nach Kontostand sechseinhalb Jahre — die aber, wenn alle strittigen Zeiten zählen und weitergearbeitet wird, bis Ende 2027 knapp aufgeholt sein könnten. Drei Lückenkomplexe stehen im Raum: zwei Jahre bei einer 1994 liquidierten Werftzulieferin (belegt durch Arbeitgeberbescheinigung, Lohnabrechnungen und AOK-Bescheinigung, aber ohne Kontomeldung), ein schwach belegter Bäckerei-Minijob 2001 und eine Pflegezeit, für die die Pflegekasse Beitragszahlung bescheinigt, die im Konto trotzdem fehlt. Dazu ein Arbeitslosigkeitszeitraum, den die Agentur als beitragspflichtigen Leistungsbezug bewilligt hat, der im Konto aber nur als Anrechnungszeit steht.

## Aktenstruktur

```
rentenrecht-fruehrente-kontenluecken-werft-kiel/
├── README.md                                  ← diese Datei
├── 01_mandatsaufnahme.docx                      ← Kanzleivermerk: Lückenkomplexe, Wunschtermin, Arbeitsauftrag
├── 02_drv_versicherungsverlauf.docx             ← Kontostand mit drei ungeklärten Zeiträumen
├── 03_drv_rentenauskunft.docx                   ← Abschlagsbild, 45-Jahre-Stand, Ausgleichszahlungs-Vorbehalt
├── 04_arbeitgeberbescheinigung_nordstahl_1992.docx ← Originalbescheinigung der liquidierten Arbeitgeberin
├── 05_lohnabrechnungen_1990_91_auszug.docx      ← drei Abrechnungen mit ausgewiesenem RV-Einbehalt
├── 06_aok_mitgliedsbescheinigung_1990_1992.docx ← Einzugsstellen-Nachweis über die gesamte Lückenzeit
├── 07_pflegekassenbescheinigung_2011.docx       ← Pflegezeit, Beitragszahlung ab 03/2010, Zuordnungsrätsel
├── 08_minijob_nachweise_2001.docx               ← Kontoauszüge, Weihnachtskarte, Zeugin Clausen
├── 09_arbeitsagentur_bescheid_2014.docx         ← Alg-Bewilligung 2014/2015 und Widerspruch zum Kontostand
├── 10_schreiben_mandantin_drv.docx              ← eigenes Schreiben der Mandantin vom 02.06.2026
├── 11_drv_zwischennachricht.docx                ← Einleitung der Kontenklärung, Vordrucke, Einzelanfragen
├── 12_beratervermerk_monatsraster.csv           ← Monatsraster: Kontostand, Beleglage, Streitpunkt je Zeitraum
├── 13_kontenspiegel_wartezeit_datenkern.csv     ← Datenkern: Zeitart, Monate, Wartezeit-35/45-Zählung, Entgeltpunkte, Beleglage; Wartezeit und Abschlag nachrechenbar
├── 14_zeugenerklaerung_clausen_2026-06-30.md    ← schriftliche Zeugenerklärung der Filialleiterin zum Minijob 2001
├── 15_drv_zwischenmitteilung_kontenklaerung_2026-07-04.md ← Zwischenstand der DRV Nord: Pflegezeit gutgeschrieben, Nordstahl/Alg/Minijob offen
├── eml/
    ├── 01_kanzlei_an_drv_kontenklaerung.eml     ← Kanzlei übersendet Nachweise, stellt drei Anträge
    ├── 02_aok_einzugsstelle_auskunft.eml        ← AOK Nordwest: Pflege-Zuordnungsfehler bestätigt, Nordstahl/Minijob ohne RV-Meldung
    ├── 03_sohn_thies_baeckerei_hinweis.eml      ← Sohn zur Beleglage des Minijobs (Mai/Juni bar, ohne Beleg)
    └── chatverlauf_thies_familie.txt            ← WhatsApp-Export Mutter/Sohn zur Unterlagensuche
├── 91_fristsachen_belege_offene_punkte_2026-07-06.csv    # Fristsachen, Belege und offene Punkte (Ergaenzung v426)
└── eml/2026-07-06_sachstand_nachforderung.eml            # Sachstand zur Nachforderung (Ergaenzung v426)
```

Der Datenkern in `13_kontenspiegel_wartezeit_datenkern.csv` macht den Streit rechnerisch nachvollziehbar: Die DRV setzt für die Wartezeit von 45 Jahren nur die gemeldeten Pflichtzeiten mit 462 Monaten (38 Jahre 6 Monate) an, während aus den Belegen 62 zusätzliche, teils streitige Monate rekonstruierbar sind. Ob der abschlagsfreie 45-Jahre-Beginn zum 01.01.2028 erreichbar ist, hängt daran, welche dieser Monate zählen.

## Bearbeitungsziel

Die Akte soll eine strukturierte Kontenklärung erzwingen: je Lückenkomplex Beweislage und Ermittlungsansätze ordnen, die Wartezeiten von 35 und 45 Jahren in Klärungsvarianten rechnen, den Widerspruch zwischen Pflegekassen- und Agenturbescheinigungen einerseits und dem Kontostand andererseits auflösen und der Mandantin einen belastbaren Fahrplan für einen Rentenbeginn im Frühjahr 2027 samt Ausgleichszahlungsoption geben — ohne die rechtliche Einordnung der einzelnen Zeitarten vorwegzunehmen.
