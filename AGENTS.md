# AGENTS.md – Repository-Regeln für alle Agenten

Dieses Repository enthält Plugins für deutsche Kanzleien. Diese Datei gilt für **jedes** Werkzeug, das hier arbeitet. Der vollständige Leitfaden steht im zentralen Repository-Leitfaden im Wurzelverzeichnis; halte dich an beide.

## Umfang und Qualität der Plugins

Beitragsanfragen zuerst auf fachlichen Nutzen und Richtigkeit prüfen. Sinnvolle Ergänzungen eigenständig ausarbeiten; ein neues Plugin nur anlegen, wenn es einen klaren eigenen Arbeitsauftrag erfüllt. Ein bereits passendes Paket gezielt verbessern. Eine erledigte Anfrage begründet kein zweites gleichartiges Plugin.

- Jedes Plugin hat höchstens **21 aktive Skills einschließlich Hauptskill**. Ein kompakter Bestand von etwa zehn Skills bleibt sinnvoll, wenn er den Fachauftrag vollständig abdeckt; 21 ist eine Obergrenze, kein Ausbauziel. Fachvertiefungen dürfen ausführlich sein und über klar benannte Abschnitte oder lokale Referenzdateien erreichbar bleiben; keine zusätzlichen Skills allein zur Zerteilung eines zusammenhängenden Arbeitswegs.
- Jedes Plugin hat einen klar erkennbaren **Hauptsache-Skill (Hauptskill)** für den vollständigen Arbeitsablauf: vorhandenen Auftrag und Unterlagen verstehen, entscheidende Lücken klären, erforderliche Fachprüfungen verbinden, das bestellte Ergebnis ausarbeiten, prüfen und mit neuen Angaben fortführen. Er bindet die Spezialskills nach Bedarf ein; eine klare Einzelfrage beantwortet er direkt. Ein bloßes Themenmenü, ein Argumentationsbaustein oder eine Weiterleitung ohne Fortführung genügt nicht. Bei App-Plugins umfasst der Hauptskill den tatsächlich verfügbaren Bedien- und Ergebnisweg.
- Dazu gehören ein eigenständig nutzbarer großer Werkstatt-Prompt, ein eigenständig nutzbarer Mini-Prompt und zugeordnete Testakten. Die README macht diese Einstiege und ihre unterschiedlichen Zwecke unmittelbar auffindbar.
- Prompts und Skills beginnen verständlich beim konkreten Fachproblem. Sie verbinden Unterlagen, entscheidende Rückfragen, belegte Rechtsprüfung, Gegenargumente und das vollständig ausformulierte Ergebnis. Länge dient der fachlichen Tiefe, nicht der Wiederholung. Rechtsprechung und Gesetzgebung nach den Quellenregeln prüfen; Recherchegrenzen offen benennen.
- Testakten sind seriös, anschaulich und lebensnah. Sie erklären Beteiligte, Ablauf, Unterlagen und den noch offenen Arbeitsauftrag durch konkrete Aktenstücke. Der [Testakten-Qualitätsstandard](testakten/QUALITAETSSTANDARD.md) regelt Darstellung, Originalformate und die getrennte Grundakte. Beim Bündeln von Skills bleiben bestehende Testakten erhalten.

## Verständliche Skill-Namen und Generierung

Skill-Name, sichtbare Überschrift und Beschreibung benennen denselben konkreten Auftrag. Namen verbinden möglichst Fachgegenstand und Tätigkeit oder Arbeitsprodukt, etwa `einspruch-begruenden`, `liquiditaet-pruefen` oder `nachtragsangebote-vergleichen`. Keine bedeutungsleeren Sammelnamen, bloßen Sortiernummern oder abgeschnittenen Wörter. Fachlich notwendige Abkürzungen sind zulässig; interne Generatorbegriffe sind kein verständlicher Skill-Name. Der technische Slug bleibt höchstens 64 Zeichen lang und verwendet Kleinbuchstaben, Ziffern und Bindestriche.

Vor dem Schreiben neuer oder überarbeiteter Skills den Hauptworkflow, die Abgrenzung der Spezialaufgaben, die verständlichen Namen und die Gesamtzahl einschließlich Hauptskill prüfen. Generatoren dürfen bei Namenskollisionen keine nummerierten Ersatznamen erfinden und keine vorhandenen Einstiegsskills still entfernen oder reaktivieren. Bestehende Namen nur gezielt ändern und dann sämtliche Verweise nachführen. Eine bestandene Namenssyntax- oder Existenzprüfung belegt weder sprachliche Verständlichkeit noch einen fachlich vollständigen Hauptworkflow; diese Punkte zusätzlich am Inhalt prüfen.

## README-Einstiege

READMEs beginnen mit Zweck, Zielgruppe und Benutzung des jeweiligen Angebots. Keine vorangestellte Änderungschronik, keine Meldungen wie „Neu“, „Erweitert“ oder Vergleiche mit Vorgängerversionen. Versionsstände und Änderungen gehören ins Changelog oder in Release-Notes; im README genügt ein Verweis nach der Einführung. Fachlich erforderliche Rechtsstandsangaben und konkrete Nutzungshinweise bleiben erhalten.

## Einstiege eigenständiger Prompts

Werkstatt- und Schnellstart-Prompts beginnen mit dem konkreten Fachproblem und den daraus entstehenden Arbeitsprodukten. Technische Einrichtungslisten, Autorvermerke und umfangreiche Routingtabellen gehören nicht vor diese Erklärung. Ein fachlich passender, belegter Entscheidungsanker soll früh erscheinen, zusammen mit seiner Bedeutung und seiner Aussagegrenze; einschlägige Normen konkret nennen. Historischen, rein technischen oder sprachlichen Werkzeugen keine sachfremde Rechtsprechung aufzwingen. Fehlende verifizierte Rechtsprechung offen benennen, statt einen Anker zu erfinden.

Vorhandene Unterlagen zuerst auftragsbezogen lesen. Nur entscheidende Lücken erfragen, Antworten in denselben Entwurf einarbeiten und bis zum bestellten Dokument weiterarbeiten. Durch redaktionelles Straffen dürfen weder Verzweigungen noch Quellenstatus, Gegenargumente oder Freigabegrenzen verloren gehen. Die Einstiegsprüfung ist keine erneute Prüfung sämtlicher Quellen und kein Nachweis einer erfolgreichen Ausführung in einer bestimmten Oberfläche.

Werkstatt-Prompts haben kein redaktionelles Seitenlimit. Gliedere lange Fassungen nach echten Entscheidungsschritten und trenne den kurzen Einstieg von ausführlichen Beweis-, Quellen- und Variantenprüfungen. Längere Entwürfe in einer vorhandenen Dokumentansicht fortführen. Interaktive Fallansichten nur nutzen, wenn sie fachlich helfen und tatsächlich ausführbar sind. Ohne solche Funktionen denselben Arbeitsablauf im Text anbieten und die gewählte Variante in das beauftragte Dokument übernehmen.

## Gliederung und Nummerierung (verbindlich für alle Vorlagen und Verträge)

Diese Regel gilt **dauerhaft und für jedes Werkzeug**. Sie ist nicht verhandelbar.

- **Ausschließlich dezimale Gliederung:** `1`, dann `1.1`, dann `1.1.1`, dann `1.1.1.1` und so weiter, beliebig tief.
- **Niemals** römische Ziffern (`I`, `II`), Großbuchstaben (`A`, `B`, `C`), Kleinbuchstaben (`a`, `b`) oder gemischte Verlags-Gliederungen (`A. I. 1. a) aa)`). Genau diese Schemata sind verboten, weil man sich darin nicht zurechtfindet.
- **Leerzeile zwischen Gliederungspunkt und seinem Inhalt sowie zwischen Gliederungsebenen.** Überschrift bzw. Nummer und der folgende Text/Unterpunkt werden durch eine Leerzeile getrennt, sonst ist es nicht lesbar.
- **Einrückung sparsam.** Nur leicht einrücken, gerade so viel, dass die Hierarchie sichtbar bleibt und es gut aussieht – nie so tief, dass das Dokument zerfleddert wirkt.

Gilt für alle Vorlagen, Verträge, Memos, Schriftsätze und sonstigen Dokumente in diesem Repository.

## Pflicht-Hinweis für Testakten

Für jede bestehende und jede künftig angelegte Testakte gilt der folgende unveränderte Hinweis auf Deutsch und Englisch:

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

- Gesamt-PDF und Einzel-PDFs enthalten weder eine Hinweisseite noch diesen Warntext. Der Hinweis für PDF-Downloads steht ausschließlich auf der zugehörigen README-/Downloadseite unmittelbar vor dem Downloadlink oder der Downloadtabelle.
- Beide ZIP-Varianten, also Originalformat-ZIP und Einzel-PDF-ZIP, enthalten unmittelbar auf der ZIP-Wurzelebene eine UTF-8-kodierte `README.txt`, die mit dem zweisprachigen Hinweis beginnt. Dasselbe gilt für Sammelpakete mit Testakten.
- Auf der Repository-Startseite, im Download-Index sowie in den zentralen, aktenbezogenen und Plugin-READMEs steht der vollständige Hinweis unmittelbar vor jeder PDF-/ZIP-Downloadgruppe für Testakten. Ein allgemeiner Hinweis an anderer Stelle genügt nicht.
- Die zentralen Testakten-Builder und README-Generatoren erzeugen die Hinweise reproduzierbar. Änderungen an einer Testakte dürfen die zugehörigen Prüfungen von Wortlaut und Position nicht umgehen oder abschwächen.
