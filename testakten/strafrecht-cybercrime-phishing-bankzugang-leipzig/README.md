# Akte: Phishing und Bankzugang Leipzig


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 32 KB) | PDF | [`gesamt-pdf/strafrecht-cybercrime-phishing-bankzugang-leipzig_gesamt.pdf`](gesamt-pdf/strafrecht-cybercrime-phishing-bankzugang-leipzig_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## Sachverhalt

Die 72-jährige Bankkundin Irmgard Seidel erhielt eine SMS mit Link auf eine nachgebaute Bankseite und gab dort Zugangsdaten sowie zwei TAN-Freigaben ein. Am nächsten Morgen gingen 8.400 Euro und 6.900 Euro auf dem Konto von Jonas Peukert ein. Innerhalb von 41 Minuten wurden 12.000 Euro an drei Automaten abgehoben, der Rest per Echtzeitüberweisung weitergeleitet.

Peukert behauptet, er habe sein Konto nur für einen angeblichen Kryptohandel zur Verfügung gestellt und selbst keine Phishingseite betrieben. Sein Handy enthält Chatnachrichten mit einer Person namens Riko, die eine Provision von 700 Euro versprach. Die IP-Adresse der Phishingseite führt zu einem ausländischen Server; bei Peukert wurden keine Administrationsdaten gefunden.

Die Akte zwingt zur Trennung zwischen Haupttat, Kontoleihe, Vorsatz und Vermögensabschöpfung. Der Verteidigungsansatz liegt bei fehlender Kenntnis der Phishingstruktur, begrenzter Tatherrschaft und der Frage, ob die Bank- und Providerdaten lückenlos gesichert wurden.

Der Datenauswertungs-Kern liegt im zusammengeführten Transaktions- und Login-Log. Aus ihm sind die Schadenssumme, die Bargeldabhebungen und die Weiterleitungskette über die Finanzagenten rekonstruierbar, sobald die in unterschiedlichen Zeitzonen geführten Bank- und Serverprotokolle aufeinander abgeglichen werden. Gegen die Einlassung, das Konto sei nur für einen Kryptohandel verliehen worden, steht dabei der Befund, dass der Löwenanteil des Geldes mit der körperlichen Girocard und der PIN des Kontoinhabers an drei Automaten im eigenen Wohnviertel Leipzig-Grünau abgehoben wurde. Diese Diskrepanz und die Höhe der abgeschöpften Summe müssen rechnerisch belegt werden.

## Verfahrensstand

Gericht: Amtsgericht Leipzig, Schöffengericht Abteilung 212

Staatsanwaltschaft: Staatsanwaltschaft Leipzig, 212 Js 6180/26

Verteidigung oder Vertretung: RAin Dr. Hanna Weigand, Leipzig

Mandatsbezug: Jonas Peukert, 24 Jahre, Lagerist, Kontoinhaber

## Beteiligte

| Person | Rolle |
| --- | --- |
| Jonas Peukert | Beschuldigter, Kontoinhaber, 24 Jahre |
| Irmgard Seidel | Geschädigte, 72 Jahre, Bankkundin |
| Riko | unbekannter Anwerber und Chatkontakt |
| Kevin Arlt | Finanzagent, Empfänger einer Weiterleitung |
| Mandy Röhl | Finanzagentin, Empfängerin einer Weiterleitung |
| Steffen Kolbe | Saxonia Bank AG, Fraud Desk |
| Dr. Ing. Ulf Sander | Landeskriminalamt Sachsen, Cybercrime |
| RAin Dr. Hanna Weigand | Verteidigung, Leipzig |

## Zeitachse

| Datum | Vorgang |
| --- | --- |
| 17.04.2026 | Phishing-SMS an Bankkundin Irmgard Seidel |
| 18.04.2026 | zwei Echtzeitüberweisungen auf Konto Peukert |
| 19.04.2026 | Bargeldabhebungen an Automaten Leipzig-Grünau |
| 28.04.2026 | Kontosperre und Strafanzeige der Bank |
| 19.06.2026 | Durchsuchung Wohnung Peukert |
| 05.08.2026 | Frist zur Stellungnahme zum IT-Auswertebericht |

## Aktenstruktur

```
strafrecht-cybercrime-phishing-bankzugang-leipzig/
├── 01_mandatsnotiz_erstgespraech.docx                                    — Erstkontakt, Rolle, Sofortfragen und Mandatsziel
├── 02_sachverhalt_chronologie.docx                                       — ausformulierter Sachverhalt, Zeitachse und offene Widersprüche
├── 03_ermittlungsakte_auszuege.docx                                      — Auszüge aus polizeilichen und staatsanwaltlichen Vermerken mit Beweismittelübersicht
├── 04_beweismittel_und_arbeitsauftraege.xlsx                             — Beweismittelmatrix mit Belastungs- und Entlastungsrichtungen
├── 05_fristen_und_verfahrensstand.csv                                    — Fristen, Termine, Zustellungen und Wiedervorlagen
├── 06_email_akteneinsicht_und_rueckfragen.eml                            — E-Mail der Verteidigung zu Akteneinsicht und Nachforderungen
├── 07_rechtliche_arbeitsnotiz.docx                                       — Normanker, Beweislastfragen, taktische Linien
├── 08_entwurf_verfahrensschritt.docx                                     — Entwurf für Stellungnahme und Einziehungsprüfung
├── 09_originalanlage_behoerdenvermerk.pdf                                — PDF-Anlage mit behördlichem Vermerk
├── 10_it_auswertebericht_2026-06-30.docx                                 — IT-forensischer Auswertebericht mit Geldfluss, IP-Zuordnung und Zeitzonenabgleich
├── 11_beschuldigtenvernehmung_peukert_2026-06-19.docx                    — Vernehmung des Beschuldigten mit Einlassung zur Kontoleihe
├── 12_transaktions_und_loginlog_2026-04-18_bis_2026-04-19.csv            — Transaktions- und Login-Log; Kern der Schadens- und Weiterleitungsberechnung
├── eml/
│   ├── 2026-04-10_finanzagenten_anwerbung.eml                            — Anwerbung des Beschuldigten als Zahlungsabwickler über Riko
│   ├── 2026-04-17_phishing_mail_original.eml                             — Original der Phishing-Nachricht an die Geschädigte
│   └── 2026-04-28_bank_betrugsabteilung_anzeige.eml                      — Strafanzeige und Transaktionsübersicht der Bank
├── signal/
│   └── chatverlauf.txt                                                   — Signal-Verlauf mit Riko: Provision, Abhebung und Weiterleitung
├── rubric.yaml                                                           — Sechs Prüfpunkte für die fachliche Auswertung
└── README.md                                                             — Diese Übersicht
```

## Prüffokus

- Computerbetrug nach Paragraf 263a StGB
- Geldwäscheprüfung nach Paragraf 261 StGB
- Beihilfe durch Kontobereitstellung
- Beweiswert und Beweisverwertungsfragen getrennt prüfen.
- Nebenfolgen, Fristen und Verfahrensziel früh sichtbar machen.

## Passende Arbeitsrichtungen

`fachanwalt-strafrecht`, `aktenaufbereiter-strafrecht`, `staatsanwaltschaft-praxis-einstieg`
