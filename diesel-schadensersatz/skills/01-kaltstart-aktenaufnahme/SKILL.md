---
name: 01-kaltstart-aktenaufnahme
description: "Default für neue oder ungeordnete Dieselakten und gemischte Uploads. Sichert Dateien und Fundstellen, bildet Fallkern, Lücken und Arbeitsstand und nennt genau einen nächsten Skill. Nicht für Anspruchs- oder Klageentwürfe."
---

# Kaltstart und Aktenaufnahme

## Zweck und Anwendungsfall

Dieser Skill ist der Einstieg in jeden Dieselgate-Fall. Er startet, wenn der Nutzer nur sagt "hier ist mein Fall" oder einen gemischten Upload liefert: Kaufvertrag, Rechnung, Fahrzeugschein oder Zulassungsbescheinigung, KBA-Rückrufschreiben, Werkstattbestätigung zum Software-Update, Finanzierungs- oder Leasingvertrag, Kontoauszüge, Fotos von Typenschild oder Kilometerstand, Korrespondenz mit Autohaus oder Hersteller. Er inventarisiert alles, legt die strukturierte Kaufakte an und übergibt mit Startkarte an genau einen nächsten Skill. Er ersetzt keine fachliche Prüfung; die Weiche stellt Skill `06-anspruchstriage-fallstrategie`.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Liefere zuerst den fallbezogenen Befund mit Ampel, präziser Lückenliste und genau einem nächsten Schritt; höchstens drei ergebnisrelevante Fragen. Tabelle nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern, sonst vollständige Absätze oder kurze Liste. Schwierige Rechtsfragen an eine Rechtsanwältin oder einen Rechtsanwalt eskalieren; Anwaltszwang und RDG-Grenzen wahren.

## Erste Antwort

Die erste Antwort dieses Skills ist immer ein fertiges Arbeitsprodukt, nie eine Vorrede. Sie enthält in dieser Reihenfolge: Startkarte (Fallart, Ampel, Grund, Frist, genau ein nächster Skill), dokumentenscharfes Inventar, ausformulierten Stammdaten-Kern mit Fundstellen sowie eine präzise Lückenliste mit Beschaffungsweg und Auswirkung jeder Lücke. Eine Tabelle wird nur bei mindestens drei Dokumenten oder wiederkehrenden Inventarfeldern verwendet; bei einem einzelnen Dokument oder einer bloßen Fallschilderung genügen vollständige Absätze oder eine kurze Liste. Fehlende Daten werden als konkrete Lücke bezeichnet, nicht durch leere Zellen dargestellt.

In der ersten Antwort verboten: Erklärungen zum Plugin oder zur Skill-Auswahl, Theorie zu Anspruchsgrundlagen, Werkzeug- oder Pfad-Fehlermeldungen als Hauptinhalt, mehr als drei Rückfragen sowie jede Rückfrage, deren Antwort die Startkarte nicht ändern würde. Wer "neuer Fall", "mach die Akte fertig", "Profi-Schnelllauf" oder Vergleichbares sagt und Unterlagen anhängt, bekommt sofort das Inventar — keine Gegenfrage nach Fallart, Skillnummer oder gewünschter Klageform.

Das Aktenstart-Werkzeug ist ein Beschleuniger, keine Startbedingung: Läuft es nicht (kein Ordnerzugriff, fehlende Abhängigkeit, Pfadproblem), wird ohne weiteren Kommentar manuell inventarisiert. Ein Werkzeugfehler wird höchstens in einer Zeile der Kontrollansicht vermerkt und blockiert weder Aufnahme noch Startkarte.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Beliebiges Upload-Bundle oder einzelne Dokumente rund um Kauf, Fahrzeug, Finanzierung und Rückruf.
- Falls vorhanden: FIN, Motorcode, Modell, Kaufdatum, Kilometerstand.
- Rolle der anfragenden Person (Geschädigte:r, Kanzlei, Verbraucherschutz, Legal-Tech).

## Ablauf / Checkliste

1. Autostart auslösen, sobald mindestens ein fallbezogenes Dokument oder eine Fallschilderung vorliegt; keine Rückfrage nach dem Fachpfad vor dem Inventar. Die erste Antwort folgt dem Kontrakt aus `## Erste Antwort`.
2. Optionaler Beschleuniger bei lokalem Ordnerzugriff: einmalig `python3 tools/diesel-aktenstart.py <AKTENORDNER> --output-dir <ARBEITSORDNER>/aktenstart` ausführen (im Plugin-Kontext Toolpfad über `$CLAUDE_PLUGIN_ROOT/tools/diesel-aktenstart.py`). `STARTBEREIT` erlaubt die Inhaltsaufnahme, `PRUEFUNG_NOETIG` verlangt die benannten Kontrollen, `BLOCKIERT` stoppt nur das Lesen der konkret benannten Dateien — nie die Aktenaufnahme insgesamt. Läuft das Werkzeug nicht oder gibt es keinen Ordnerzugriff (typisch bei Chat-Uploads), sofort manuell inventarisieren; kein zweiter Reparaturversuch in derselben Antwort.
3. Falls ein `aktenstart-manifest.json` vorliegt, gegen `assets/schemas/aktenstart-manifest.schema.json` lesen. Hash, Größe, relativer Pfad und Dateikopf sind Maschinenbefunde; Kategorie und Beweisrolle bleiben Dateinamenheuristiken. Bereits stabil gehashte identische Dateien nicht erneut analysieren, bevor Dublette und maßgebliche Fassung geklärt sind.
4. Profi-Modus erkennen, wenn der Nutzer "Profi-Modus", "Schnelllauf", "Bulk", "nur Ergebnis", "Klagepaket" oder "E-Akte fertig" verlangt. Dann Startkarte, Inventar, rote Stopps und nächstes Arbeitsprodukt kompakt in einem Durchgang liefern, ohne Quellenstatus, Konflikte oder Fristen wegzulassen.
5. Dateien fachlich inventarisieren: Datum, Absender, tatsächlicher Inhalt, Lesbarkeit und Beweiswert (Original, Kopie, Screenshot, E-Mail, Parteivortrag). Die Maschinenkategorie nie ungeprüft als Dokumentinhalt ausgeben.
6. OCR-Bedarf, fehlende Seiten, unlesbare Beträge, Dubletten, Namenskollisionen und Fassungsstand markieren. Bei exakten Dubletten eine Datei nur als Arbeitskopie bestimmen; keine Datei löschen. Nichts ins Blaue ergänzen.
7. Stammdaten in die Kaufakte ziehen: Käufer:in/Halter:in, Fahrzeug (FIN, Modell, Motorcode, Erstzulassung), Kaufdatum, Kaufpreis, Verkäufer (Händler oder privat), Finanzierung, Kilometerstand — jede Angabe mit Dokument-ID, Seite/Fundstelle, Sicherheit und Konfliktvermerk.
8. Betroffenheitshinweise sofort markieren: KBA-Rückrufcode, Motorfamilie (EA189, EA288, OM651 oder vergleichbar), Software-Update-Vermerk. Keine Betroffenheitsfeststellung behaupten; das prüfen Skills `04` und `05`.
9. Fristen und Zugangsdaten herausziehen: Kaufdatum vor oder nach Herbst 2015, Rückruf- und Update-Daten, laufende Fristen aus Korrespondenz. Kein automatisch erzeugtes Dateidatum als Zugangsnachweis behandeln.
10. Lückenliste erstellen: fehlende Pflichtdokumente mit Priorität, Beschaffungsweg (Autohaus, Werkstatt, Bank, KBA) und Folge des Fehlens. Höchstens drei Fragen gleichzeitig; zuerst nur die Fragen, die Strategie, Frist oder Gegnerwahl tatsächlich ändern.
11. Datenschutz beachten: personenbezogene und sensible Daten nur zweckgebunden aufnehmen; Weitergabe an Dritte nur mit Abtretung oder Vollmacht (Details in Skill `20-eakte-export-kanzleisoftware`).
12. Startkarte ausgeben: Fallart, Ampel, kurzer Grund, fehlende Kernstücke, Frist und genau ein nächster Skill.
13. Übergabe: vollständiges Inventar an Skill `06-anspruchstriage-fallstrategie`; Vertrags- und Zahlungstiefe an Skill `02-kaufvertrag-zahlungen-belege`; Rückruf- und Motorklärung an Skill `04-betroffenheit-motor-kba-rueckruf`; E-Akte-Import oder -Export an Skill `20-eakte-export-kanzleisoftware`.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Aus ungeordnetem Eingangsmaterial eine zitierfähige Tatsachenbasis herstellen, ohne Dateinamenheuristik, OCR-Text oder Eigenauskunft zum Beweis aufzuwerten.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Jede übernommene Kerntatsache führt Dokument-ID, Fundstelle, Quellenrolle, Sicherheit und Konfliktstatus.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Kaufdatum, Kaufpreis und FIN tragen den großen Schadensersatz; ohne saubere Kaufakte ist die Rückabwicklung nicht bezifferbar. | Bestätigt |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Der Differenzschaden wird als Prozentsatz des Kaufpreises geschätzt; der belegte Kaufpreis ist Pflichtfeld der Akte. | Bestätigt |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19; Urt. v. 09.04.2024 - VI ZR 660/20 | Auch Gebrauchtwagenkäufe können erfasst sein; Erst- oder Zweiterwerb gehört deshalb in die Stammdaten. | Bestätigt |
| EuGH, Urt. v. 01.08.2025 - C-666/23 | Update-Bestätigungen gesondert erfassen; ein Update kann eine streitige Einrichtung dokumentieren, begründet die Haftung aber nicht ohne weitere Prüfung. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

Startkarten-Vorlage (in der ersten Antwort mit Fallwerten füllen; alle Sätze bleiben vollständig):

> **Startkarte [Nachname Geschädigte:r] ./. [Hersteller]** — Fallart: [z. B. EA189-Prüfstandserkennung, Gebrauchtwagenkauf 2015]. Ampel: [grün/gelb/rot], weil [ein Satz mit dem tragenden Grund, z. B. "der Kaufvertrag mit FIN und Kaufpreis vorliegt, aber jeder Kilometerstandsnachweis fehlt"]. Nächste Frist: [Datum TT.MM.JJJJ oder "keine akute Frist erkennbar; Verjährungsprüfung folgt in Skill 07"]. Nächster Skill: [genau einer, mit einem Halbsatz Begründung].

Der Stammdaten-Kern nennt Käufer:in und Halter:in, Modell, FIN, Motorcode, Erstzulassung, Kaufdatum und Kaufpreis, Verkäuferrolle, Finanzierung oder Leasing, jeden datierten Kilometerstand sowie KBA-Rückruf und Software-Update. Hinter jeder bekannten Angabe stehen Dokument-ID, Seite oder Fundstelle, Sicherheit und ein etwaiger Konflikt. Für jedes unbekannte Pflichtfeld folgt stattdessen ein vollständiger Lückensatz mit Beschaffungsweg und Auswirkung, etwa: „Der Kilometerstand bei Übergabe ist nicht belegt; anzufordern sind Übergabeprotokoll oder erste Werkstattrechnung, andernfalls bleibt die Nutzungsrechnung gesperrt.“

Ergebnissatz-Bausteine für das Inventar:

- "Die Akte enthält [Anzahl] Dokumente; tragfähig belegt sind damit [Kaufvertrag/FIN/Kaufpreis], offen bleiben [Kilometerstand/Rückrufcode/Update-Nachweis]."
- "Der Kilometerstand ist nur als [Foto/Parteiangabe] belegt; für die Nutzungsentschädigung wird ein datierter Werkstatt- oder TÜV-Nachweis benötigt, zu beschaffen über [Werkstatt/TÜV-Bericht], sonst rechnet Skill 08 mit einer offen ausgewiesenen Schätzspanne."
- "Ein KBA-Rückrufschreiben liegt [vor/nicht vor]; ohne amtlichen Rückrufcode bleibt die Betroffenheit Arbeitshypothese und wird in Skill 04 geklärt."

Weichen-Tabelle für die Übergabe:

| Befund im Intake | Nächster Skill | Grund |
| --- | --- | --- |
| Inventar vollständig, Fallart klar | 06-anspruchstriage-fallstrategie | Triage stellt die Anspruchs- und Fristenweiche. |
| Kaufvertrag, Finanzierung oder Zahlungen unklar oder widersprüchlich | 02-kaufvertrag-zahlungen-belege | Vertrags- und Zahlungstiefe vor jeder Bezifferung. |
| Motorcode, Rückruf oder Update ungeklärt | 04-betroffenheit-motor-kba-rueckruf | Amtliche Betroffenheit trägt jeden weiteren Schritt. |
| Kaufdatum nahe 2013 oder früher, Kenntnisthema sichtbar | 06, mit Vermerk für 07-verjaehrung-restschadensersatz | Fristenlage kann den ganzen Fall entscheiden. |
| Nutzer verlangt E-Akte, Export oder DMS-Register | 20-eakte-export-kanzleisoftware | Exportpaket direkt aus dem Inventar. |

## Quellenpflicht

Es gilt `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst). Betroffenheits- und Anspruchsaussagen nur aus `references/gepruefte-anker-dieselgate.md`; OCR- und Mappingunsicherheiten offen markieren. Keine erfundenen Aktenzeichen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Startkarte, dokumentenscharfes Inventar und strukturierte Kaufakte mit Stammdaten und Lückenliste. Ab drei Dokumenten oder wiederkehrenden Feldern enthält das Inventar die Spalten Dokument-ID, Datei, Datum, Absender, Inhalt, Fundstelle, Beweiswert, Konflikt und Lücke; sonst werden dieselben Angaben vollständig in Absätzen oder einer kurzen Liste ausgegeben. Bei Werkzeugnutzung bleiben `aktenstart-manifest.json` und `aktenstart-startkarte.md` Teil der Kontrollspur. Alle Texte sind vollständig ausformuliert; bloße Stichwortsammlungen sind als Endprodukt unzulässig. Auf Wunsch zusätzlich als `fallakte.json` oder `dms-register.csv` über Skill 20.

## Beispiele

- Nutzer schreibt "Neuer Fall, mach die Akte fertig" und hängt Kaufvertrag, Rückrufbrief und Kontoauszug an: Die erste Antwort ist Startkarte (gelb, Kilometerstand fehlt), Inventar mit drei Dokument-IDs, Stammdaten-Kern mit Fundstellen und Lückenliste; nächster Skill 06. Keine einzige Rückfrage, weil die Startkarte ohne Antworten steht.
- Nur eine Fallschilderung ohne Dokumente ("2015 einen Passat gekauft, jetzt von Manipulation gelesen"): Startkarte mit Fallart-Hypothese und roter Lücke "kein Kaufnachweis", Lückenliste mit Beschaffungsweg (Autohaus, Bank, Zulassungsstelle) und genau einer Rückfrage nach dem Kaufjahr, weil es die Verjährungsweiche ändert.
- Upload eines ganzen Aktenordners im Dateisystem: Aktenstart-Werkzeug läuft einmal, Manifest wird übernommen; scheitert es, entsteht dasselbe Inventar manuell — die erste Antwort sieht in beiden Fällen gleich aus, nur die Kontrollansicht vermerkt den Werkzeugstatus in einer Zeile.
- Foto vom Typenschild plus Leasingvertrag: Motorcode-Hinweis markiert, Finanzierungsspur vorgemerkt, Übergabe an Skill 04 zur Rückrufklärung; die Leasingkonstellation wird als eigene Zeile im Stammdaten-Kern geführt.
