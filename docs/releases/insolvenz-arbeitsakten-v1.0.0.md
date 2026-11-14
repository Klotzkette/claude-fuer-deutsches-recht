# 1 Insolvenz-Arbeitsakten 1.0.0

Die Akten enthalten getrennte Eingangsunterlagen für die eigene Prüfung und weiterführende Verfahrensunterlagen. Dieses Aktenrelease umfasst neun Fälle. Die Versionen der installierbaren Plugins bleiben unverändert.

## 1.1 Vertragsgrundlagen und Schriftsatzform

Die drei Insolvenzreifeakten enthalten 40 zusätzliche Vertrags- und Abrechnungsurkunden mit 78 Seiten, drei CSV-Verzeichnisse und drei E-Mails mit identischen Vertragsanlagen. Darlehen, Kreditlinien, Sicherungszweck, Grundstückssicherheiten, Gesellschafterforderungen, Nachrang, Patronat, Leasing und Kartenreserve lassen sich anhand vollständiger Erklärungen prüfen. Bankbuchungen und bestehende insolvenzrechtliche Kontrollbefunde bleiben unverändert.

Weserfunken erhält vollständig gesetzte Kanzleibriefköpfe, Gerichtsempfänger, Rubrum, konkrete Anträge und dezimale Gliederungen. Die Klage umfasst 18 Seiten, die gesonderte Erwiderung 14 Seiten. Inhaltliche Streitpunkte und bewusst fehlerhafte Parteizuordnungen bleiben Teil der Übung. Die historischen Originale sind mit einer begrenzten, belegten Satzmigration abgeglichen. Auch fünf Rückforderungsschreiben und Schriftsätze in den vier weiteren Anfechtungsakten erhalten einen vollständigen Kanzleisatz.

## 1.2 Hamburg: Backbord Backstube

Ein privater gewerblicher Entsorger verlangt 21.532,47 EUR aus neun Monatsrechnungen. Die Backstube hält die Leistungsmengen für unplausibel. Der getrennte spätere Eingang enthält Fahrzeugereignisse, QR-Zuordnungshistorie, Klinikunterlagen und eine berichtigte Mandantenauskunft. Die Zuordnung der Behälter muss neu geprüft werden.

Die 55 Originaldateien sind in `Grundakte`, `01_Gerichtseingang_2026-11-06` und `02_Nachlieferung_2026-11-12_und_13` aufgeteilt. Eine fertige Klageerwiderung oder rechtliche Musterlösung ist nicht enthalten. Die Klage und gerichtliche Verfügung gehören ausschließlich in den getrennten Gerichtseingang.

## 1.3 Umfang

| Akte | Originaldateien | Davon Grundakte | Gesamt-PDF-Seiten |
| --- | ---: | ---: | ---: |
| Spreeglasur Cottbus | 107 | 100 | 294 |
| Schlachtensee Stahl & Form Zehlendorf | 104 | 97 | 284 |
| Uckerbogen Rotorcharter Prenzlau | 108 | 101 | 298 |
| Weserfunken Bremen | 62 | 41 | 229 |
| Blechliebe Bamberg | 24 | 18 | 24 |
| Faltenwurf Fürth | 24 | 18 | 24 |
| Veedelwende Direktzahlung | 24 | 15 | 27 |
| Veedelwende Zession | 24 | 16 | 29 |
| Backbord Backstube Hamburg | 55 | 34 | 108 |

Insgesamt 532 Originaldateien, davon 440 Grundakten-Dateien, und 1.317 Seiten in den neun Gesamt-PDFs. Die drei Insolvenzreife-Grundakten umfassen zusammen 298 Dateien. README.txt-Dateien sind in diesen Dokumentenzahlen nicht enthalten.

## 1.4 Download und Benutzung

Öffnen Sie für einen unvorbereiteten Erstauftrag ausschließlich den jeweiligen Ordner `Grundakte`. Verfahrensunterlagen und ausdrücklich bezeichnete Vorlagen außerhalb dieses Ordners werden erst für den weiteren Arbeitsauftrag verwendet. Gesamt-PDFs stehen separat bereit; sie sind nicht in den Originalformat-ZIPs enthalten.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Paket | Download |
| --- | --- |
| Nur die drei Insolvenzreife-Grundakten | [Insolvenzreife_Drei_Grundakten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenz-arbeitsakten-v1.0.0/Insolvenzreife_Drei_Grundakten.zip) |
| Vollständige drei Insolvenzreifeakten | [Insolvenzreife_Drei_Originalakten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenz-arbeitsakten-v1.0.0/Insolvenzreife_Drei_Originalakten.zip) |
| Alle neun Originalakten | [Neun_Arbeitsakten_Originalformate.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenz-arbeitsakten-v1.0.0/Neun_Arbeitsakten_Originalformate.zip) |

## 1.5 Technischer Nachweis

Das Release enthält genau 32 Dateien: neun Original-ZIPs, neun Einzel-PDF-ZIPs, neun Gesamt-PDFs, drei Sammel-ZIPs, `release-bestand.json` und `checksums-sha256.txt`. Das Inventar nennt jede enthaltene Originaldatei mit SHA-256 sowie jedes Einzel-PDF mit SHA-256 und Seitenzahl. Die Verifikation vergleicht zusätzlich Grundakten, E-Mail-Anlagen, Sammelpakete und die Seiteninhalte der Gesamt-PDFs.

Erzeugung: `python3 scripts/build-insolvenz-arbeitsakten-release.py --dist <leeres Verzeichnis>`.

Prüfung eines Downloads: `python3 scripts/build-insolvenz-arbeitsakten-release.py --dist <Downloadverzeichnis> --verify --offline`.

Für einen vollständigen Neubau der Originale werden die dokumentierten Artefaktwerkzeuge und rechtmäßig vorhandene Times-New-Roman-Schriften benötigt. Die Prüfberichte stehen unter `quality/insolvenz-arbeitsakten`, `quality/insolvenzreife` und `quality/legal`. Bestehende Releases und Tags werden nicht überschrieben.
