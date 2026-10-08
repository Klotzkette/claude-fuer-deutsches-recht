# 100-Punkte-Fehlerkatalog der beA-Schriftsatzwerkstatt

Diese Kontrollspur gilt für die technische Endfertigung eines bereits fachlich freigegebenen Schriftsatzes. Jeder einschlägige Punkt erhält `grün`, `gelb`, `rot` oder `nicht einschlägig` mit kurzem Nachweis. Ein roter Punkt sperrt die Paketfreigabe; ein gelber Punkt braucht eine dokumentierte Entscheidung einer real benannten verantwortlichen Person.

## 1. Eingang und unveränderte Quellen

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 001 | Der übergebene Projektordner ist nicht eindeutig benannt oder nicht erreichbar. |
| 002 | Eine Quelldatei wird umbenannt, verschoben oder überschrieben statt nur gelesen. |
| 003 | Eine leere Datei wird als Schriftsatz oder Anlage eingeplant. |
| 004 | Temporäre Office-Dateien, Sperrdateien oder automatische Sicherungen werden versehentlich übernommen. |
| 005 | Ein Archiv wird ungeprüft als Gerichtsdatei eingeplant statt im Arbeitsbereich inventarisiert. |
| 006 | Eine ausführbare Datei, ein Makro oder ein unbekannter aktiver Inhalt bleibt unmarkiert. |
| 007 | Passwortgeschützte oder nicht lesbare Quellen werden still ausgelassen. |
| 008 | Ein unbekanntes Format wird nur durch Änderung seiner Dateiendung als PDF ausgegeben. |
| 009 | Relativer Pfad, Größe, Änderungszeit und SHA-256 jeder Quelle fehlen im Eingangsinventar. |
| 010 | Eine Quelle ändert sich nach der Inventarisierung, ohne dass der Lauf neu bewertet wird. |

## 2. Nachricht und Verfahrenszuordnung

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 011 | Dateien aus zwei Gerichtsverfahren werden in dasselbe Upload-Paket gemischt. |
| 012 | Gericht und vorgesehener SAFE-Empfänger sind nicht durch eine reale Person bestätigt. |
| 013 | Ein vorhandenes Aktenzeichen fehlt, ist veraltet oder gehört zu einem anderen Verfahren. |
| 014 | Bei einem Neueingang wird irrtümlich ein fremdes Aktenzeichen verwendet. |
| 015 | Der Nachrichtenbetreff ist leer, kryptisch oder widerspricht dem Schriftsatz. |
| 016 | Die maßgebliche Frist und der interne Versandpuffer sind nicht dokumentiert. |
| 017 | Kläger-/Beklagtenrolle oder die sonst vereinbarte Anlagenlogik ist ungeklärt. |
| 018 | Die fachlich verantwortliche Person ist nur vermutet statt namentlich benannt. |
| 019 | Die tatsächlich versendende Person ist nur vermutet statt namentlich benannt. |
| 020 | Aktiver beA-/Kanzleisoftwarestand, verwendetes XJustiz-Profil oder clientseitige Dateinamens- und Anhangswarnungen fehlen im Preflight. |

## 3. Hauptschriftsatz und Versionssperre

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 021 | Es gibt keinen oder mehr als einen als Hauptschriftsatz festgelegten Stand. |
| 022 | Der Hash der fachlich freigegebenen Hauptquelle ist nicht festgehalten. |
| 023 | Das jüngste Dateidatum wird ohne reale Bestätigung als Freigabenachweis behandelt. |
| 024 | Änderungsverfolgung oder Kommentare bleiben in der Versandfassung sichtbar. |
| 025 | Ausgeblendeter Text, verborgene Absätze oder unsichtbare Tabelleninhalte bleiben ungeklärt. |
| 026 | Dynamische Felder zeigen beim Rendern einen anderen Stand als in der geprüften Quelle. |
| 027 | Kopfzeile, Fußzeile, Seitenzahl oder Briefkopf fehlen nach der Konvertierung. |
| 028 | Ein Platzhalter, interner Hinweis oder Entwurfswasserzeichen bleibt im Schriftsatz. |
| 029 | Der Namenszug am Dokumentende fehlt oder ist nicht eindeutig zugeordnet. |
| 030 | Eine Änderung nach der Versionssperre lässt Prüf-, Signatur- oder Freigabestatus bestehen. |

## 4. Anlagenfolge und Kennzeichnung

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 031 | Ein Anlagenzitat im Schriftsatz hat keine eindeutig zugeordnete Quelldatei. |
| 032 | Eine vorgesehene Anlage wird im Schriftsatz nirgends zitiert, ohne dass dies entschieden ist. |
| 033 | Bereits eingereichte K-/B-Nummern werden erneut vergeben. |
| 034 | Eine Folgeeinreichung beginnt bei Anlage 1 statt nach der höchsten vergebenen Nummer. |
| 035 | Dieselbe Anlagenbezeichnung wird zwei verschiedenen Dateien zugeordnet. |
| 036 | Inhaltsgleiche Dateien werden unbemerkt als verschiedene Anlagen eingeplant. |
| 037 | Verschiedene Dokumente werden ohne sachlichen Plan zu einem Konvolut verbunden. |
| 038 | Seitenfolge oder Inhaltsblatt eines echten Konvoluts ist nicht eindeutig. |
| 039 | Die sichtbare Anlagenbezeichnung verdeckt Briefkopf, Datum, Barcode, Text oder Seitenzahl. |
| 040 | Eine bereits elektronisch signierte PDF wird für Stempel oder Deckblatt verändert, ohne die Signaturfolge zu klären. |

## 5. Formatspezifische Konvertierung

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 041 | DOC, DOCX, ODT oder RTF wird ohne stabilen Renderer und Schriftenabgleich ausgegeben. |
| 042 | Word-Tabellen, Fußnoten oder Seitenumbrüche verschieben sich unbemerkt. |
| 043 | Verknüpfte Bilder, externe Felder oder nicht eingebettete Schriften fehlen im PDF. |
| 044 | XLS, XLSX, ODS oder CSV enthält ungeprüfte ausgeblendete Blätter, Zeilen oder Spalten. |
| 045 | Druckbereich, Orientierung, Skalierung oder wiederholte Tabellenköpfe sind unbrauchbar. |
| 046 | Formeln, externe Datenverbindungen oder nur zwischengespeicherte Werte bleiben ungeklärt. |
| 047 | EML oder MSG verliert Absender, Empfänger, CC, Datum, Zeitzone, Betreff oder Nachrichtentext. |
| 048 | E-Mail-Anhänge oder eingebettete Nachrichten verschwinden unbemerkt in der Konvertierung. |
| 049 | JPEG, PNG, TIFF oder HEIC wird mit falscher Ausrichtung, falschem Zuschnitt oder unlesbarer Auflösung gerendert. |
| 050 | PPT/PPTX oder ein sonstiges Format wird trotz fehlender verlässlicher Renderkontrolle freigegeben. |

## 6. Sicht- und PDF-Strukturprüfung

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 051 | Eine Datei trägt nur die Endung `.pdf`, besitzt aber keinen echten PDF-Header. |
| 052 | Eine PDF kann nicht vollständig geöffnet und strukturell gelesen werden. |
| 053 | Eine PDF hat keine Seite oder eine Seite ohne positive, endliche Abmessungen. |
| 054 | Seitenzahl von Quelle, Arbeitskopie und Manifest widerspricht sich. |
| 055 | Erste oder letzte Seite bleibt ohne gerenderte Sichtprüfung. |
| 056 | Schriftsatz, Tabelle, Scan, Bild, Konvolut oder Warnfall bleibt teilweise ungesehen. |
| 057 | Ränder, Spalten, Fußnoten, Unterschriften oder Anlagenstempel sind abgeschnitten. |
| 058 | Schriftzeichen werden ersetzt, überlagert oder als schwarze Flächen ausgegeben. |
| 059 | OCR-Text widerspricht dem Seitenbild oder ein erforderlicher OCR-Lauf ist fehlgeschlagen. |
| 060 | Druckbarkeit, Leserichtung, Drehung oder sinnvolle Seitenskalierung ist nicht geprüft. |

## 7. Sicherheit, Signaturen und Datenschutz der Dateien

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 061 | Eine PDF ist verschlüsselt oder passwortgeschützt. |
| 062 | Eine PDF enthält JavaScript oder eine automatische Startaktion. |
| 063 | Eine PDF enthält eingebettete Dateien oder Office-Objekte. |
| 064 | Eine PDF enthält Rich-Media-, 3D-, Audio- oder Videoinhalte. |
| 065 | Interaktive Formulare oder Kommentare bleiben ohne dokumentierte Entscheidung aktiv. |
| 066 | Eine vorhandene elektronische Signatur wird nachträglich entwertet oder falsch zugeordnet. |
| 067 | Vertrauliche Metadaten, interne Kommentare oder persönliche Autorendaten bleiben unbemerkt. |
| 068 | Nicht verfahrensbezogene personenbezogene Daten werden unnötig mitgesendet. |
| 069 | Der Datenschutzstatus lautet offen, Stopp oder ist nicht dokumentiert. |
| 070 | Ein Zugangstoken, Kennwort, interner Pfad oder sonstiges Betriebsgeheimnis gelangt in den Upload. |

## 8. Dateinamen und Manifest

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 071 | Ein Zielname überschreitet den internen Standard von 80 Zeichen einschließlich `.pdf`. |
| 072 | Ein Zielname enthält Nicht-ASCII-Zeichen, Leerzeichen oder mehr als einen Punkt. |
| 073 | Wörter sind nicht eindeutig mit Unterstrich oder Minus getrennt. |
| 074 | Nummernpräfixe sind nicht lückenlos, einheitlich breit oder logisch sortierbar. |
| 075 | Datei 01 ist nicht der einzige Hauptschriftsatz. |
| 076 | Zielnamen sind doppelt oder kollidieren ohne Beachtung der Großschreibung. |
| 077 | Ein Manifest-Quellpfad ist absolut, enthält `..`, Rückwärtsschrägstriche oder beginnt wie eine Tabellenformel. |
| 078 | CSV-Kopf, Spaltenreihenfolge oder Zahl der Werte weicht von der Vorlage ab. |
| 079 | Anlagenbezeichnung, sichtbarer Stempel und kompakte K-/B-Kennung im Zielnamen widersprechen sich. |
| 080 | Seiten, Bytes oder SHA-256 im Manifest stimmen nicht exakt mit der finalen PDF überein. |

## 9. Signaturweg und reale Freigabe

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 081 | Der Schriftsatz besitzt weder eine wirksame qeS noch eine einfache Signatur mit passendem sicheren Übermittlungsweg. |
| 082 | Die einfache Signatur besteht nicht aus einer lesbaren Namenswiedergabe der verantwortlichen Person. |
| 083 | Bei einfacher Signatur versendet eine andere Person als die verantwortliche Person. |
| 084 | Eine qeS gehört nicht zur verantwortlichen Person oder nicht exakt zur finalen Hauptschrift. |
| 085 | Mehrere elektronische Dokumente werden mit einer gemeinsamen qeS verbunden. |
| 086 | Anlagen werden unnötig als eigenständig signaturpflichtige Schriftsätze behandelt. |
| 087 | Eine PDF wird nach Anbringung der qeS noch verändert. |
| 088 | Postfachzugang oder organisatorische Versandberechtigung wird vom System nur unterstellt. |
| 089 | Das System setzt selbst eine Freigabeperson ein oder erteilt die reale Freigabe. |
| 090 | Ein Paket mit offenem Punkt verliert vorzeitig den Status `ENTWURF - NICHT VERSENDEN/EINREICHEN`. |

## 10. Paket, Eingang und schneller Wiederholungslauf

| Nr. | Fehler, der aktiv ausgeschlossen wird |
|---:|---|
| 091 | Im Upload-Ordner liegen ZIP, Office-Dateien, Protokolle, Symlinks oder Unterordner statt Versand-PDFs und gegebenenfalls eindeutig zugeordneter CAdES-Dateien. |
| 092 | Interne Manifeste, Prüfprotokolle oder Freigabekarten werden versehentlich als Anlagen mitgesendet. |
| 093 | Dateizahl oder Gesamtgröße einschließlich eines real erzeugten separaten Signaturartefakts wird nicht gegen 1.000 Dateien und 200.000.000 Bytes geprüft. |
| 094 | Die interne Warnschwelle von 900 Dateien oder 180.000.000 Bytes bleibt unbeachtet. |
| 095 | Eine Überschreitung wird eigenmächtig aufgeteilt statt nach § 3 ERVV eskaliert. |
| 096 | Der finale Paketvalidator wird nicht gegen genau den freigegebenen Upload-Ordner ausgeführt. |
| 097 | Der Status `gesendet` wird ohne automatisierte gerichtliche Eingangsbestätigung als Eingang behandelt. |
| 098 | Bestätigte Dateinamen, Dateizahl, Empfänger oder Zeitstempel weichen ab, ohne dass sofort gestoppt wird. |
| 099 | Ein Delta-Lauf verwendet eine alte PDF trotz geändertem Quellhash, Konvertierungsprofil, Werkzeugstand oder Ausgabehash. |
| 100 | Unbegrenzte Datei-/Seitenläufe oder fehlende Fortsetzungsmarken überlasten den Lauf; Parallelisierung verändert die Reihenfolge oder ersetzt die abschließende vollständige Paketprüfung. |

## Anwendung

Der Katalog wird nicht als zusätzliche Gerichtsdatei versendet. Skill 01 verwendet ihn für Annahme und Delta-Plan, Skills 02 bis 07 für ihre jeweiligen Prüffelder, Skill 08 für den vollständigen Preflight und Skill 09 für Eingang und Archivierung. Datei- und Seitenstapel sowie Fortsetzungsmarken begrenzen Speicher- und Kontextlast. Der maschinelle Paketvalidator prüft die objektiv automatisierbaren Punkte; Sichtprüfung, Signaturgültigkeit, Empfängerwahl und reale Freigabe bleiben personengebundene Kontrollen.
