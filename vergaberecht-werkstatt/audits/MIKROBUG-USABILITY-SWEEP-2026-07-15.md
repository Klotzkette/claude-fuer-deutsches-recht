# Mikrobug- und Usability-Sweep vom 15.07.2026

## Prüfmaßstab

Geprüft wurden 249 Skills, drei Pluginrollen, 15 zentrale Bedienflächen, 423 Markdown-Dateien, sieben Testakten, 478 juristische Textdateien, 74 juristische Binärartefakte und der vollständige Release-Bau. Jede Tabellenzeile bündelt fünf konkrete Einzelproben. Damit sind 100 Fehlerproben und 100 Bedienproben nachvollziehbar erfasst; ein Prüfschritt ohne Befund wird nicht als gefundener Fehler ausgegeben.

## 100 Fehlerproben

| Proben | Konkreter Prüfgegenstand | Ergebnis |
|---:|---|---|
| 1-5 | Marketplace-Version, drei Plugin-Versionen, Plugin-Slugs, Manifestquellen, Beschreibungsgrenzen | ohne Befund |
| 6-10 | YAML-Abschluss, Name-Verzeichnis-Gleichlauf, Description-Länge, verbotene Zeichen, UTF-8 | ohne Befund |
| 11-15 | Behörden-Triage: Verfahrensart, Leistungsbeschreibung, Legacy-System, Wertung, Zielskill | vier Phantom-Routen behoben |
| 16-20 | Bieter-Kaltstart: Unterlagenprüfung, Angebot, Legacy-System, Qualitätsvorsprung, Zielskill | vier Phantom-Routen behoben |
| 21-25 | Bieter-Mandatstriage: Unterlagenprüfung, Angebot, Legacy-System, Qualitätsvorsprung, Zielskill | vier Phantom-Routen behoben |
| 26-30 | Routingtabellen erkennen, Zielslug prüfen, Zeilennummer melden, Pluginrolle begrenzen, Regression abbrechen | Validator ergänzt |
| 31-35 | lokale Pfade, Root-Grenze, Same-File-Anker, fremde Markdown-Anker, doppelte Heading-Slugs | Ankerprüfung ergänzt; Bestand sauber |
| 36-40 | absolute ZIP-Pfade, Windows-Laufwerke, Elternpfade, NUL-Zeichen, Ausgabe als Quelle | Abweisung ergänzt |
| 41-45 | Groß-/Kleinschreibung, Unicode-NFC, doppelte Archivnamen, Symlinks, leere Archive | Kollisionsschutz ergänzt |
| 46-50 | Vollspeicher-Read, 1-MB-Streaming, ZIP64, Quelländerung während Bau, atomarer Austausch | Streaming und Änderungswache ergänzt |
| 51-55 | PDF-, ZIP-, DOCX-, XLSX-, PPTX-Rekompression | bereits komprimierte Formate werden gespeichert statt erneut komprimiert |
| 56-60 | Ausgabe im Quellbaum, alte Ausgabe bei Fehler, Dateirechte, feste ZIP-Zeit, Sortierung | abgesichert und getestet |
| 61-65 | `gh api`-Hänger, Release-View-Hänger, ungültiges JSON, SHA-256-Vollspeicher-Read, Polling-Ende | Timeouts und Streaming-Hash ergänzt |
| 66-70 | Megaprompt-H1, Modul-Hierarchie, Code-Fence-Überschriften, Zeilenlänge, Coverage-Text | Mehrfach-H1 beseitigt; Validator ergänzt |
| 71-75 | Behörden-, Bieter-, Konkurrenten-Rechtskern, BTTG-Langzeile, technische Anker | in lesbare, rollenfeste Blöcke geteilt |
| 76-80 | statischer BTTG-Tagesstand, BMAS-Livequelle, Abrufdatum, fiktive Tarifwerte, Regressionssperre | schnell alternden Tagesstand ersetzt |
| 81-85 | § 132 GWB, Advania, Strominator, Amtsblattpfad, Eignungs-Recheck | amtlich gegengeprüft; Schreibweisen bereinigt |
| 86-90 | § 160 Abs. 2 und 3 GWB, zehn Kalendertage, 15 Kalendertage, Missbrauch, Verordnungsangriff | Rechtsvalidator grün |
| 91-95 | PDF-Seiten, Bildseiten, Briefkopf, Überlauf, leere Seiten | 21 Stichprobenseiten visuell geprüft; ohne Befund |
| 96-100 | JSON, NFC-Dateinamen, Case-Kollisionen, Symlinks, leere Nutzdateien | 912 Dateien geprüft; nur `.nojekyll` absichtlich leer |

## 100 Bedien- und Darstellungsproben

| Proben | Konkreter Prüfgegenstand | Verbesserung |
|---:|---|---|
| 1-5 | Repo-Start, Dateikatalog, Downloads, drei Rollen, Testakten | Links und Anker maschinell geprüft |
| 6-10 | Plugin-Start, Werkstattprompt, Skill-Katalog, Vorlagen, Rohdateien | Werkstattprompt in allen drei Menüs vor die lange Skill-Liste gesetzt |
| 11-15 | Intake, Arbeitsstatus, Antwortstandard, Schnellwahl, Nutzungscheck | auf allen drei Startbildschirmen vereinheitlicht |
| 16-20 | Friststatus, Aktenstand, Freigabe, Erstoutput, offene Werte | sichtbare Statusleiste und Nicht-Erfindungsregel ergänzt |
| 21-25 | Unterlagenangriff, Preiswertung, Konkurrenteneignung, Nichtabhilfe, Zuschlagsgefahr | Konkurrenten-Schnellwahl ergänzt |
| 26-30 | Kurzbild, Zulässigkeit, Begründetheit, Schutzstatus, OLG-Reserve | Konkurrenten-Streitdashboard vollständig ausgebaut |
| 31-35 | Rüge, VK-Antrag, §-169-Schutz, Akteneinsicht, VK-Termin | konkrete Streitfall-Applets ergänzt |
| 36-40 | OLG, Vergleich, Kosten, Belegmatrix, Abschlussstatus | einreichungsnahe Outputs statt Leerformular ergänzt |
| 41-45 | Fallkarte, Quelleninventar, Verarbeitungsstatus, Fristenampel, Output-Weiche | Ordnerfall-Protokolle gleich gegliedert |
| 46-50 | Dateigrenze, Volumengrenze, Paketgröße, Einzeldateimodus, Checkpoint | Großaktenmodus in drei Rollen sichtbar gemacht |
| 51-55 | beschädigte Datei, Verschlüsselung, nicht unterstütztes Format, Ersatzanforderung, Weiterlauf | fehlertolerante Fortsetzung statt Gesamtabbruch |
| 56-60 | Quelle, Hash, Status, Ergebnis, nächster Lauf | Wiederaufnahme ohne Doppelarbeit ermöglicht |
| 61-65 | SAP/ERP, AVA/GAEB, DMS, API/MCP, Portal | Last- und Fortsetzungsregeln in allen Legacy-Skills ergänzt |
| 66-70 | Originalschutz, Mapping, Freeze, Freigabe, Quittung | produktive Wiederholung nach Abbruch ausdrücklich gesperrt |
| 71-75 | Behördenentscheidung, Angebot, Rüge, VK-Schriftsatz, Uploadpaket | genau ein Erstoutput und höchstens zwei Alternativen erzwungen |
| 76-80 | Preis, Qualität, Tempo, Lebenszyklus, Zuschlagschance | Bestangebotslogik in Rollenoberflächen erhalten und prüfbar |
| 81-85 | Norm, Tatbestand, Beweislast, Quellenstatus, Rechtsfolge | Fallkarten bleiben vor Langtext und verweisen auf belastbare Outputs |
| 86-90 | Hauptüberschrift, Modulüberschrift, Leselänge, Inhaltsverzeichnis, Skill-Slug | Megaprompts scanbar und autark gehalten |
| 91-95 | Umlaute, §-Zeichen, Fachbegriffe, Handlungssprache, veraltete Bedienphrasen | sichtbare Stolperformulierungen beseitigt |
| 96-100 | Laufzeit, Speicher, Determinismus, Timeout, Resume | 59-MB-Archiv in 0,07 s bei 24,5 MB Max-RSS; identischer SHA-256 in zwei Läufen |

## Ergebnis

- Zwölf tatsächlich tote Skill-Routen sind repariert und künftig releaseblockierend.
- Vier nachgelagerte Triage-Skills sind klar vom Rohaktenstart abgegrenzt; Ordner, ZIP und Systemexporte haben damit genau einen Master-Einstieg.
- Archivbau, Remote-Prüfungen und Großaktenworkflows haben begrenzte Ressourcen und Fortsetzungspunkte.
- Die drei Rollenoberflächen sind strukturell gleich und besitzen jeweils eine rollenfeste Abschlusskontrolle, ohne unterschiedliche Entscheidungen und Rechtsbehelfe zu verwischen.
- Der Konkurrentenworkflow reagiert auf eine Nichtabhilfe und weist diese Entscheidung nicht mehr versehentlich der angreifenden Marktseite zu.
- Der tagesbezogene BTTG-Status wurde durch eine amtliche Live-Weiche mit Abrufdatum ersetzt.
- Der vollständige schnelle Smoke-Lauf und der temporäre Release-Bau sind grün.
