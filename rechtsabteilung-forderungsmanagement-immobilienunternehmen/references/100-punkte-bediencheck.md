# 100-Punkte-Bediencheck für das Immobilien-Forderungsmanagement

Dieser Check hält die konkrete Bedien- und Robustheitsspur des Repositories fest. Jeder einschlägige Punkt erhält bei Pilot, Review oder Release `erfüllt`, `offen` oder `nicht einschlägig` mit kurzem Nachweis. Ein offener Punkt zu Frist, Rollenbefugnis, Freigabe, Dateiintegrität oder Quellenstatus sperrt den betroffenen Außenprozess.

## 1. Einstieg und Routing

| Nr. | Prüfkriterium |
|---:|---|
| 001 | Der Ein-Satz-Auftrag `Neuer Fall. Prüfe den gesamten Ordner, sichere zuerst alle Fristen und arbeite ohne Skillauswahl bis zur nächsten freigabefähigen Entscheidung weiter.` startet den Dokumentenmix-Intake. |
| 002 | Ein sauberer SAP-Status- oder Mietkontoauszug startet die SAP-Normalisierung statt einer Klageerstellung. |
| 003 | Eine bereits belastbare Fallkarte führt direkt zur Fallziel-Triage, ohne den Vollintake zu wiederholen. |
| 004 | Gerichtliche Klageerwiderung, gerichtlicher Hinweis und gegnerischer Prozessschriftsatz führen zu Skill 37. |
| 005 | Ein außergerichtliches Mieterverein- oder Anwaltsschreiben führt zu Skill 43, nicht zu Skill 37. |
| 006 | Mieterklage und Widerklage führen zu Skill 42; eine bloße Einwendung in der eigenen Klage tut dies nicht. |
| 007 | KFA, KFB und positiver Titel werden getrennt zu Skills 46, 47 und 48 geroutet. |
| 008 | Interne Skillnummern werden nicht als Bedienentscheidung an die Fachangestellten ausgegeben. |
| 009 | Die Nutzeransicht zeigt im Feld `Jetzt` genau eine nächste Arbeitsaktion; weitere Aufgaben stehen geordnet in der Warteschlange. |
| 010 | Nur sofort entscheidende Rückfragen zu Frist, Rolle oder Maßnahme werden gestellt, höchstens drei zugleich und jeweils mit Grund und Folge; nicht blockierende Lücken bleiben gelb. |

## 2. Sofortkarte und Aktenzustand

| Nr. | Prüfkriterium |
|---:|---|
| 011 | Vor der Tiefenauswertung erscheint dieselbe kurze Sofortkarte mit Modus, Akten-ID/Stichtag, Fallart, Frist/Quelle, Ampel/Grund, gelesen/gesamt, Kernlücken und Feld `Jetzt`. |
| 012 | Die Sofortkarte nennt die früheste mögliche Frist und behandelt Unsicherheit ausdrücklich. |
| 013 | Jede Frist nennt Auslöser, Quelldatei, Seite oder Dokumentstelle und Rechenstatus. |
| 014 | Grün, gelb oder rot wird mit einem konkreten Grund statt nur als Farbe ausgegeben. |
| 015 | Der Dateistand trennt sichtbar, lesbar, defekt und OCR-offen. |
| 016 | Die Sofortkarte enthält höchstens drei Kernlücken und priorisiert sie nach Rechtsfolge. |
| 017 | Vollintake und Delta-Fortschreibung werden vor der Bearbeitung eindeutig unterschieden. |
| 018 | Eine Änderungskarte trennt Altstand, Neuzugang, geänderte Werte und unveränderten Kernstand. |
| 019 | Überholte Annahmen, Salden und Entwürfe bleiben erkennbar und werden nicht still überschrieben. |
| 020 | Bei mehreren Ereignissen führt die nächste harte Frist; alle weiteren Aufgaben bleiben auffindbar. |

## 3. Große Akten und Wiederaufnahme

| Nr. | Prüfkriterium |
|---:|---|
| 021 | Ein günstiger Sofortscan erfasst den gesamten sichtbaren Bestand, bevor einzelne Dateien vertieft werden. |
| 022 | Ein fachlicher Tiefenstapel umfasst höchstens 20 Dateien. |
| 023 | Ein Lang-PDF wird in Stapeln von höchstens 30 Seiten vertieft. |
| 024 | Nach jedem Stapel sichert eine Fortsetzungsmarke Akten-ID, Stichtag, verarbeitet/offen, letzte Quelle und nächste Einheit. |
| 025 | Nach Unterbrechung wird an der bestätigten Fortsetzungsmarke statt bei Datei 1 weitergearbeitet. |
| 026 | Ein OCR-, Lese- oder Konvertierungsfehler stoppt nur die betroffene Quelle und nicht alle übrigen Dateien. |
| 027 | Unveränderte Roh-OCR, Langtabellen und Dokumentvolltexte werden beim Fortsetzen nicht erneut ausgegeben. |
| 028 | Große Dateien werden blockweise gehasht und nicht vollständig in den Arbeitsspeicher geladen. |
| 029 | Die beA-Werkstatt führt höchstens vier unabhängige Konvertierungen parallel aus. |
| 030 | Die PDF-Sichtprüfung rendert höchstens zwei Aufträge parallel und verwirft protokollierte Seitenbilder wieder. |

## 4. Lesbarkeit und Arbeitssprache

| Nr. | Prüfkriterium |
|---:|---|
| 031 | Eine sichtbare Nutzertabelle hat höchstens sieben Spalten. |
| 032 | Hashes, DMS-IDs und weitere Technikfelder stehen bei Bedarf in einem getrennten Register. |
| 033 | Ein ausformulierter Entwurf besteht aus vollständigen Sätzen und nicht aus einem Stichwortskelett. |
| 034 | Arbeitsnamen und Klartext ersetzen interne IDs, soweit die ID nicht für Nachweis oder Support nötig ist. |
| 035 | Wiederkehrende Ausgaben verwenden dieselbe Reihenfolge: Karte, Register, Prüfung, Lücken, Aktion, Entwurf. |
| 036 | Beträge, Salden, Zinsen und Zahlungen stehen in einer nachvollziehbaren Rechenzeile mit Quelle. |
| 037 | Daten werden kalendarisch eindeutig und nicht nur als relative Angaben wie `morgen` ausgegeben. |
| 038 | Fehlende Angaben erscheinen nur in einer internen Arbeitsskizze als sprechende eckige Platzhalter; kein solcher Platzhalter erreicht Freigabe oder beA-Übergabe. |
| 039 | Ein roter Stopp nennt betroffene Datei, Grund, Auswirkung, zuständige Person und Korrekturweg. |
| 040 | Die erste Bildschirmansicht bleibt handlungsorientiert und wird nicht von Methodik- oder Quellenprosa verdrängt. |

## 5. Juristische Nachvollziehbarkeit

| Nr. | Prüfkriterium |
|---:|---|
| 041 | Jede juristische Freigabeentscheidung nennt die einschlägige Norm. |
| 042 | Tatbestandsvoraussetzungen werden einzeln mit erfüllt, offen oder nicht erfüllt bewertet. |
| 043 | Darlegungs- und Beweislast sowie vorhandenes Beweismittel werden getrennt ausgewiesen. |
| 044 | Rechtsprechungsanker werden vor Verwendung in einer amtlichen oder frei zugänglichen Primärquelle verifiziert. |
| 045 | Amtlicher Volltext, Pressemitteilung, Sekundärfund und bloßer Nutzerhinweis erhalten einen sichtbaren Quellenstatus. |
| 046 | Entscheidungsdatum, Gericht, Aktenzeichen, tragender Satz und Übertragbarkeit werden gemeinsam geprüft. |
| 047 | Nicht verifizierte oder widersprüchliche Aktenzeichen werden nicht als sichere Autorität ausgegeben. |
| 048 | Akteninhalt, rechtliche Wertung und bloße Arbeitshypothese bleiben sprachlich getrennt. |
| 049 | Die interne Grenze von 10.000 EUR wird nicht als gesetzliche Zuständigkeitsgrenze des Amtsgerichts dargestellt. |
| 050 | Landgericht, Rechtsmittel, Insolvenz, Strafrecht und großer Sachverständigenstreit lösen die anwaltliche Eskalationsspur aus. |

## 6. Außendokumente und Gerichtspaket

| Nr. | Prüfkriterium |
|---:|---|
| 051 | Vor der Produktion wird das gewünschte Ergebnisformat ausdrücklich aus dem Auftrag oder einer gebündelten Rückfrage bestimmt. |
| 052 | Die interne Freigabekarte bleibt vom Mieter-, Gegner- oder Gerichtsdokument getrennt. |
| 053 | Bis zur realen Freigabe lautet der Status `ENTWURF - NICHT VERSENDEN/EINREICHEN`. |
| 054 | Änderung an Betrag, Antrag, Partei, Frist, Beweis, Anlage, Weg oder Stichtag hebt die alte Freigabe auf. |
| 055 | Bereits eingereichte K-/B-Nummern bleiben gesperrt und neue Anlagen setzen die höchste Nummer fort. |
| 056 | Originaldateien bleiben unverändert; Render-, OCR-, Stempel- und Versandfassungen sind Arbeitskopien. |
| 057 | Hauptschriftsatz und jede Anlage werden als getrennte PDF geplant, nicht als Versand-ZIP. |
| 058 | Versanddateien bleiben ASCII, sprechend, logisch sortiert und höchstens 80 Zeichen lang. |
| 059 | Jede relevante PDF-Seite wird visuell auf Beschnitt, Lesbarkeit, Reihenfolge, Signatur und Kennzeichnung geprüft. |
| 060 | `gesendet` wird erst mit plausibler automatisierter Eingangsbestätigung zum technisch bestätigten Gerichtseingang. |

## 7. SAP, DMS, DATEV, RA-MICRO und MCP

| Nr. | Prüfkriterium |
|---:|---|
| 061 | Quellsystem, Exportweg, Stichtag und verantwortliche Organisationseinheit sind je Datenlauf benannt. |
| 062 | SAP-, DocuWeb-/DocuWare-, DATEV-, RA-MICRO- oder Fremd-IDs bleiben für Rückexport und Audit erhalten. |
| 063 | Fachwert, Quelldatei, Seite oder Tabellenzeile und technischer Identifikator werden miteinander verknüpft. |
| 064 | Unbekannte Zielfelder erzeugen eine Mappingfrage statt einer erfundenen Importfähigkeit. |
| 065 | Lesende und schreibende Schnittstellenrechte werden getrennt geprüft. |
| 066 | Schreibende Integrationen beginnen im Testsystem und benötigen eine reale Freigabe. |
| 067 | Import und Rückexport definieren Dubletten-, Idempotenz- und Konfliktregeln. |
| 068 | Ohne proprietäre Schnittstelle stehen dokumentiertes CSV, JSON oder XML als kontrollierter Austauschweg bereit. |
| 069 | Ein erzeugter Export wird gegen Schema, Pflichtfelder, Zeichensatz, Anzahl und Prüfsumme validiert. |
| 070 | MCP-Resources und Tools legen Aktenraum, Zweck, Rechte, Schreibwirkung und Protokollierung offen. |

## 8. Plugin- und Prompt-Nutzung

| Nr. | Prüfkriterium |
|---:|---|
| 071 | Das Fachplugin funktioniert mit seinen gepackten Referenzen ohne Zugriff auf Repo-Root-Dateien. |
| 072 | Werkstatt- und Schnellstartprompt führen den Workflow autark aus und verweisen nicht auf zu ladende Skills. |
| 073 | Der gebaute Schnellstart-Skill bleibt einschließlich Frontmatter unter 7.500 Zeichen. |
| 074 | Der vertiefte Werkstattprompt bleibt einschließlich Standalone-Frontmatter unter 30.000 Zeichen. |
| 075 | Skillbeschreibungen enthalten konkrete positive Trigger und trennscharfe Negativtrigger. |
| 076 | Der Output jedes Fachskills nennt einen konkreten Arbeitsgegenstand statt allgemeiner Beratungsprosa. |
| 077 | Plugin und beide Prompts verwenden dieselbe Reihenfolge für Intake, Triage, Entwurf, Freigabe und Fortschreibung. |
| 078 | Beide Prompts enthalten Stapelgrenzen und Fortsetzungsmarke für große Akten. |
| 079 | Eigenvertretung, Kanzlei/beA und eBO werden im Einreichungspfad getrennt geprüft. |
| 080 | Quellenpflicht und Blindzitat-Verbot gelten in Plugin und beiden autarken Prompts gleich. |

## 9. Testakten und Schulungsmaterial

| Nr. | Prüfkriterium |
|---:|---|
| 081 | Aktenstücke selbst enthalten keine didaktischen Lösungshinweise oder erwarteten Skillnamen. |
| 082 | Die jeweilige Testakten-README erklärt Lernziel, Bestand, Inkonsistenzen und zulässige Nutzung. |
| 083 | Jede Fach-Testakte bietet Arbeits-ZIP, Gesamt-PDF und Einzel-PDF-ZIP als getrennte Downloads. |
| 084 | Dateien und PDF-Anlagen sind sprechend benannt und in der README vollständig aufgelistet. |
| 085 | Mietkonto, Vertrag, Zahlungen und Forderungsaufstellung bestehen die finanzielle Konsistenzprüfung. |
| 086 | Namen, Adressen, Vertragsnummern und Objektdaten sind innerhalb einer Testakte konsistent. |
| 087 | Gesamt-PDFs sind A4, ohne Beschnitt, große Leerflächen oder unlesbare Tabellen und werden visuell stichprobenartig geprüft. |
| 088 | Einzel-PDFs bewahren Dokumentgrenzen und ein lebensnahes Erscheinungsbild. |
| 089 | Realistischer Beifang bleibt als Trainingssignal erhalten, ohne Kernfrist oder Kernbeleg zu verfälschen. |
| 090 | Testdaten sind synthetisch und enthalten keine versehentlich übernommenen realen Mieterdaten. |

## 10. Navigation, Download und Release

| Nr. | Prüfkriterium |
|---:|---|
| 091 | Die Root-README führt innerhalb der ersten Abschnitte zu Plugin, Schnellstart, Testakten und Downloads. |
| 092 | Jeder Skill ist im Plugin-README mit Arbeitsname, Kurzbeschreibung und direktem Link erreichbar. |
| 093 | Release-Assets sind über stabile `releases/latest/download`-Links direkt herunterladbar. |
| 094 | Downloadmatrix und Release-Katalog unterscheiden Plugin-ZIP, Prompt-Skill, Dokumentation und Testakten eindeutig. |
| 095 | Relative Markdown-Links werden geprüft; verwaiste interne Ziele stoppen die Abnahme. |
| 096 | Plugin- und Marketplace-Beschreibungen erfüllen Längen-, Zeichen- und Slug-Regeln. |
| 097 | Das Plugin-ZIP enthält alle von Skills referenzierten Bedien-, Quellen- und Schnittstellendateien. |
| 098 | Frontmatter-, Struktur-, Rechtsanker-, Umlaut-, Link-, PDF- und Testaktenvalidatoren laufen vor Release grün. |
| 099 | Release-Katalog, Assets und Prüfsummen werden gemeinsam erzeugt und gegeneinander validiert. |
| 100 | Temporäre Render-, Cache- und Prüfdateien bleiben aus Git und Release-Assets ausgeschlossen; Changelog und Versionsstand bleiben synchron. |

## Anwendung

Der Check ist eine Abnahmespur, kein zusätzlicher Nutzerfragebogen. Der Autostart wendet die einschlägigen Regeln still an und zeigt nur Sofortkarte, konkrete Lücken, Stopps und nächste Arbeitsaktion. Technische Detailnachweise bleiben in getrennten Protokollen; für die beA-Endfertigung ergänzt der eigenständige `100-Punkte-Fehlerkatalog` der Schriftsatzwerkstatt diesen Bediencheck.
