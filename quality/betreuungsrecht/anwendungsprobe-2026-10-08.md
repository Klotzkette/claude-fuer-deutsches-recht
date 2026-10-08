# 1. Unabhängige Anwendungsprobe vom 08.10.2026

Die begrenzte Agentenprobe führte mit dem neuen Skill zu einer korrekten September-Saldenbrücke, vollständiger Eliminierung des eigenen Kontentransfers und zwei unterschiedlich begründeten, vollständig ausformulierten Nachfragebriefen. Bargeld, mögliche Geschenke und Vertragsschluss bleiben dort offen, wo die Akte keine sichere Aussage trägt. Die Probe ist ein tatsächlicher Dokumentendurchlauf durch einen unabhängig beauftragten Agenten, **kein Cowork- oder ChatGPT-Clienttest** und kein vollständiger Test des gesamten Skills.

## 1.1 Rahmen und Unabhängigkeit

Der Agent erhielt ausschließlich den Prüfauftrag, den Repository-Pfad, den neuen Skill und die Themen September 2026, Fenster/Ruprecht, Egon Knusper sowie Streaming/Abofalle. Ergebniszahlen waren nicht vorgegeben. Gelesen wurden AGENTS.md, der dort verbindlich einbezogene CODEX.md, allein dieser fachliche SKILL.md sowie ausgewählte Originalunterlagen der Testakte. Keine Quality-Kontrollwerte, Builder, JSON-Daten, Sollwerte oder Excel-Bankexporte wurden gelesen. Eine anfänglich zu breite Dateinamensuche wurde auf die benannte Testakte beschränkt; dabei wurden keine fremden Fachinhalte oder Kontrollwerte geöffnet.

Skill: `betreuungsrecht/skills/unterlagen-auswerten-abrechnung-anschreiben/SKILL.md`; SHA-256 beim Abschluss der Probe: `b4eba03e578fceab891e1851c681379d83d1c3812be49ac09e8fe4699dc0265f`.

Die Aufgabe begrenzte das Ergebnis ausdrücklich auf einen knappen Vermerk und zwei Briefe, TXT ausreichend. Das Aktendokument mit dem Dreijahresauftrag wurde als Akteninhalt gelesen; daraus wurde keine Erweiterung dieser Probe auf alle 36 Monate abgeleitet. Es wurden keine Nachrichten versandt, keine Konten bedient und keine Plugin- oder Testaktendateien durch diesen Agenten verändert.

## 1.2 Gelesene Unterlagen und technische Durchführung

Original-PDFs: September und August 2026 jeweils Giro/Spar; Giro Mai/Juni 2024, August/September/November 2025 und April 2026; Bestellungsmitteilung; W-24051 und EK-2026-09. Die Konto-PDFs wurden mit `pdftotext -layout` tatsächlich ausgelesen. Die 20 Septemberbuchungen wurden aus dem PDF-Text einzeln mit Konto, Datum, Betrag in Cent, Referenz, Seite und Transferkennung erfasst. Beträge wurden in ganzen Cent addiert; kein Bankexport diente als Rechenquelle.

DOCX: Gespräch 02.10., Übergabe 06.10., Gerätenotiz 07.10., Arbeitsauftrag 08.10., Nachbarschaftshilfe 02.09.2024, Fensternotiz 11.06.2024 und Ruprechts Stellungnahme 04.10.2026. Inhalte wurden aus dem DOCX-XML gelesen. EML: Nachrichten 04–07, 10–11, 15–19, 23, 25–26 und 30–31 mit Absendern, Datum, Message-ID, Text und Anhangsnamen. Bildschirmfotos 01, 03 und 04 wurden visuell geöffnet.

Die Anhänge W-24051 in EML 05 und EK-2026-09 in EML 31 wurden als Bytes mit den Einzel-PDFs verglichen: jeweils identisch. Sie werden nicht als zusätzliche Rechnung oder Zahlung gezählt.

## 1.3 Rechenergebnis

| Bereich | Anfang | Eingänge | Ausgänge | Ende | Differenz zum Auszug |
|---|---:|---:|---:|---:|---:|
| Giro September | 17.892,10 | 2.565,00 | 2.878,68 | 17.578,42 | 0,00 |
| Spar September | 23.557,50 | 250,00 | 0,00 | 23.807,50 | 0,00 |
| Beide Konten, sämtliche Bewegungen | 41.449,60 | 2.815,00 | 2.878,68 | 41.385,92 | 0,00 |

B0546/B0547 bilden den belegten eigenen Transfer von 250,00 EUR am 21.09.2026. Ohne ihn verbleiben 2.565,00 EUR externe Eingänge und 2.628,68 EUR Bankabgänge außerhalb eigener Kontentransfers. Davon sind 850,00 EUR Bargeldabhebungen mit offenem Verbleib und 1.778,68 EUR Zahlungen an Dritte. Kontoguthaben und nachgewiesenes Gesamtvermögen werden nicht gleichgesetzt. Die August-Schlussbestände stimmen mit den September-Anfängen überein.

Zusätzliche Kontrollen der erzeugten Buchungsliste bestanden: 20 eindeutige Buchungsreferenzen, beide Kontobrücken in Cent, Transfernetto null, Bargeldsumme 850,00 EUR, Gesamtveränderung −63,68 EUR. Diese Kontrollen entstanden aus den tatsächlich gelesenen Kontoauszügen und nicht aus vorgegebenen Sollwerten.

## 1.4 Fachliche Ergebnisse und Abdeckung

| Prüfpunkt | Tatsächlich beobachtetes Ergebnis |
|---|---|
| Zeitachsen | September als historische Aufklärung vor Bestellung getrennt; keine selbst verantwortete Dreijahresrechnung behauptet. |
| Fenster/Ruprecht | 4.200,00 Abfluss, 600,00 bankbelegte Erstattung, 3.600,00 verbleibender Abfluss; fremdes Haus erkannt, Geschenk-/Darlehensfrage offen. Kein Rückforderungsbetrag erfunden. |
| Egon | 145,00 Septemberpauschale mit Rechnung/Abrede abgeglichen. 275,00 Drucker, 350,00 Handy, 980,00 Jahrespaket und 2.200,00 mögliches Geschenk getrennt; 3.805,00 zusätzliche Zahlungen nicht als Schaden bezeichnet. |
| Bargeld | 650,00 und 200,00 als offene Mittelverwendung, weder Konsum noch Egons Entnahme unterstellt. Zähltermin 09.10. nicht als bereits erfolgt behandelt. |
| Wille | SofaKino ausdrücklich behalten; Egons Hilfe nach Wunsch vorerst fortführen; sachliche Nachfragen, keine pauschale Anzeige oder Kündigung. Erinnerung, Angehörigenangabe und Kontobeleg getrennt. |
| LebensKompass | 69,90 Septemberzahlung, Abschlussweg/Bestätigung/Mandat offen. Doppelbelastung November 2025 vollständig erstattet und nicht nochmals gefordert. Screenshot nicht als vollständiger Bestellablauf oder Beweis eines Kündigungsbutton-Verstoßes behandelt. |
| Schriftverkehr | Zwei vollständige, konkret adressierte Briefe mit Tatsachen, Beträgen, sachbezogenen Anfragen, Antwortdatum, Anlagen und Betreuerinnenrolle. Keine ungeprüften zwingenden Anspruchsbehauptungen. |

## 1.5 Konkrete Hindernisse und Rückmeldung

Ein tatsächlicher Aktenfehler wurde während der Probe gefunden: EML 26 vom 12.08.2026 berichtete rückblickend über „im September“ geleistete Hilfe. Der Agent meldete den Widerspruch ohne Builder- oder Kontrollwertzugriff. Der Aktenautor berichtigte vor Veröffentlichung den Monat zu **Juli**. Anschließend wurde die Original-EML erneut geöffnet und die Korrektur tatsächlich bestätigt. Die veröffentlichten Probeprodukte berücksichtigen Juli; die Erstbeobachtung bleibt hier und im Vermerk sichtbar. Offen bleibt die sachliche Abgrenzung früherer Juli-Hilfe von einer Vorauszahlung für das kommende Jahr.

Weitere konkrete Grenzen: Nur Bestellungsmitteilung, keine vollständige Beschlussausfertigung oder Betreuerausweiskopie im gelesenen Bestand; kein ausgewiesenes gerichtliches Rechnungsjahr; keine separate Wertstellung in den Kontoauszügen; Bargeld nicht gezählt; Gerätequittungen fehlen; Helferabrede nur als Büroabschrift; Erinnerungen zu Schenkungen widersprüchlich; Vertragsabschluss von LebensKompass unvollständig. Die Screenshots 03/04 zeigen verkürzte Jahresangaben, deshalb keine eigenständigen exakten Aufnahmedaten daraus konstruiert. Keine dieser Lücken verhinderte Saldenrechnung oder sachliche Entwürfe.

Die Anweisungen des Skills waren für die gewählte Probe ausreichend. Es war keine ergänzende Autorenanweisung für die finanzielle Einordnung oder den Briefinhalt nötig. Der Prüfauftrag benannte allerdings die Themen und Prüfkriterien; eine völlig ungesteuerte Themenfindung wurde damit nicht getestet.

## 1.6 Produkte und verbleibende Testgrenzen

- [Auswertungsvermerk](probe/auswertungsvermerk.txt)
- [Vollständiger Nachfragebrief an Egon Knusper](probe/brief-01-egon-knusper.txt)
- [Vollständiger Nachfragebrief an LebensKompass Direkt GmbH](probe/brief-02-lebenskompass.txt)
- [Septemberbuchungen mit PDF-Fundstellen](probe/september-buchungen.csv)

Die Original-Arbeitsprodukte liegen zusätzlich unter `/tmp/betreuung-probe/`. Die hier verlinkten Kopien sind Qualitätsnachweise außerhalb der Testakte und ihrer ZIP-Dateien. Antwortdatum 22.10.2026 ist ein organisatorisch gewählter Termin, keine behauptete gesetzliche Ausschlussfrist. Entwürfe und Anlagenliste bedeuten keinen Versand oder bereits zusammengestellte Versandmappe.

Nicht getestet: vollständige 36-Monats-Auswertung, XLSX-Erzeugung und Formeldynamik, Druckgestaltung, Live-Connectoren, gerichtliche Einreichung, laufender Postfachzugriff, Kündigung oder Rücklastschrift, Rechtsbehelfs-/Verjährungsberechnung und aktuelle amtliche Rechtsprechungsprüfung. Für die hier gewählten reinen Sachverhaltsnachfragen wurden keine konkreten zusätzlichen Norm- oder Urteilsbehauptungen benötigt und daher keine ungeprüften Rechtsquellen ergänzt. Die Probe bestätigt die fachliche Anwendbarkeit in diesem Ausschnitt, keine allgemeine Vollständigkeit oder Plattformkompatibilität.
