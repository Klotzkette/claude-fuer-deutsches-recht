---
name: verzeichnis-ausgeben
description: Erzeugt konsistente Ausgaben des Verarbeitungsverzeichnisses mit Rollenansichten, Quellenstand und offenen Aufgaben. Prüft lesbare Dateien, Excel-Rückimport und Formatgrenzen und bereitet eine konkrete interne oder behördliche Vorlage vor.
---

# Verzeichnis als Excel, Word, JSON und XML ausgeben

## 1. Zweck und Anwendungsfall

Geben Sie den geführten Registerbestand in einem für den Zweck geeigneten Format aus. Excel dient der übersichtlichen Bearbeitung, Word dem verständlichen Bericht, JSON dem führenden strukturierten Bestand und XML dem dokumentierten Datenaustausch. Der Auftrag kann eine interne Leitungsübersicht, eine Arbeitsmappe für Fachbereiche oder die Vorbereitung einer behördlichen Anfrage betreffen.

Die verschiedenen Fassungen müssen denselben Datenstand erkennen lassen. Ein Export ist eine Momentaufnahme und wird nicht durch bloßes Öffnen automatisch mit späteren Änderungen synchronisiert. Die Nutzung des Formats beweist weder fachliche Vollständigkeit noch Datenschutzkonformität. Behaupten Sie keine Kompatibilität mit fremden Systemen, wenn deren Schnittstelle nicht geprüft ist.

## 2. Eingaben

Lesen Sie die aktuelle Registerdatei mit Kennung, Revision, Änderungsstand und offenen Prüfungen. Klären Sie Adressat, Umfang, gewünschte Formate und zulässigen Speicher- beziehungsweise Übermittlungsort, soweit dies nicht bereits feststeht. Eine externe Anfrage ist im Original zu lesen: Welche Gesellschaft, welcher Zeitraum und welche Tätigkeiten werden verlangt?

Prüfen Sie, ob vertrauliche Sicherheitsdetails, personenbezogene Namen oder fremde Mandanteninformationen enthalten sind. Fordern Sie keine zusätzlichen Einzeldatensätze an, wenn es nur um Kategorien und Prozessbeschreibungen geht. Nutzen Sie [Datenmodell](../../references/datenmodell.md) und tatsächliche Helferfunktionen statt erfundener Exportbefehle.

## 3. Ablauf und Checkliste

### 3.1. Ausgabezweck und Umfang festlegen

Wählen Sie die Formate nach Aufgabe. Für die laufende Pflege ist die Excel-Arbeitsmappe mit Revisionsbezug sinnvoll; eine Word-Fassung erleichtert das Lesen ausführlicher Erläuterungen. JSON und der eigene XML-Container erhalten die Struktur, müssen aber von einem Zielsystem ausdrücklich unterstützt werden. Eine PDF-Fassung kann aus Word erzeugt werden, wenn ein entsprechender Renderer verfügbar ist; sie wird nicht ohne tatsächliche Erstellung als Download behauptet.

Verwenden Sie die vollständige führende Fassung als Ausgangspunkt. Eine Teilansicht bleibt als solche erkennbar und nennt Auswahlkriterien. Werden aus Gründen der Vertraulichkeit Angaben beschränkt, dokumentieren Sie dies intern. Ein gefilterter Managementbericht darf nicht unbemerkt zum angeblich vollständigen Verzeichnis der Aufsichtsbehörde werden.

### 3.2. Verantwortlichen- und Auftragsverarbeiteransichten trennen

Ordnen Sie die Mindestangaben nach Artikel 30 Absatz 1 und Absatz 2 DSGVO in getrennte, gut lesbare Abschnitte. Der Organisationsstamm kann gemeinsam sein, sofern die unterschiedlichen Rollen klar bezeichnet sind. Bei Auftragsverarbeitung muss die Zuordnung der Verarbeitungskategorien zu jedem Verantwortlichen einschließlich Kontakt erhalten bleiben. Eine nur verdichtete Kundengruppe genügt dafür nicht.

Kennzeichnen Sie ergänzende Angaben zu Rechtsgrundlagen, internen Prioritäten, DSFA-Vorprüfung, Maßnahmen und Quellen als Zusatzinformationen. Die fachliche Nachvollziehbarkeit wird dadurch verbessert; die Pflichtfelder dürfen aber nicht in einem nur internen Maßnahmenblatt verschwinden. Eine Leerseite oder ein leeres Exportfeld gilt nicht als begründetes „nicht einschlägig“.

### 3.3. Excel als tatsächlich pflegbare Arbeitsmappe liefern

Prüfen Sie Blattnamen, lesbare Spaltenbreiten, Zeilenumbrüche und Filter. Tätigkeitskennungen müssen in allen Ansichten erhalten bleiben. Der Nutzer soll erkennen, welche Felder bearbeitet werden dürfen und welche Revision als Ausgangspunkt dient. Hinweise zu Rollen, DSFA-Entscheidungen und internen Prioritäten gehören in die Arbeitsmappe oder die mitgelieferte Anleitung.

Schützen Sie die Datenbedeutung beim Transport. Führende Nullen, ISO-Datumswerte, lange Quellverweise und Texte, die mit Formelzeichen beginnen, dürfen nicht unbemerkt umgedeutet werden. Ein Export darf fremde Texte nicht als aktive Formel ausführen. Nach der Ausgabe prüfen Sie Anzahl und Kennungen der Tätigkeiten sowie repräsentative lange Textfelder und Sonderzeichen. Die Prüfung soll tatsächliche Inhalte vergleichen, nicht nur die Existenz einer Datei.

### 3.4. Word und technische Exporte ehrlich beschreiben

Ein Word-Bericht enthält ausformulierte Zweckbeschreibungen, Rollenangaben, Datenkategorien, Empfänger, Löschlogik, Maßnahmen und offene Fragen. Verwenden Sie dezimale Überschriften und gut lesbare Absätze, statt alle Informationen in eine extrem breite Tabelle zu pressen. Mehrere Seiten je Tätigkeit sind zulässig, wenn die Angaben tatsächlich umfangreich sind. Technische Anhänge werden nur aufgenommen, soweit sie für den Empfänger bestimmt sind.

Der XML-Export des Helfers ist ein ausdrücklich dokumentierter eigener Container und kein amtlich standardisiertes Austauschformat. Nennen Sie dessen tatsächliche Struktur. Ein erfolgreiches Wiedereinlesen beweist den technischen Erhalt der Daten, nicht die Interoperabilität mit einer bestimmten Datenschutzsoftware. JSON bleibt die führende Datei; gegebenenfalls unterstützte Importe folgen der beschriebenen Revisions- und Konfliktprüfung.

### 3.5. Inhalt und Darstellungsqualität kontrollieren

Öffnen oder prüfen Sie die erzeugten Dateien mit verfügbaren Werkzeugen. Vergleichen Sie Registerkennung, Revision, Tätigkeitszahl, Rollen, lange Freitexte, Quellen und offene DSFA-Entscheidungen. Bei Word oder PDF prüfen Sie Seitenumbrüche, abgeschnittene Tabellen und lesbare Schrift. Fehlende Werkzeuge werden als Prüfgrenze benannt; ein nicht ausgeführter visueller Check wird nicht behauptet.

Nutzen Sie aussagekräftige Dateinamen mit Stand, ohne geheime Kundendaten unnötig im Pfad offenzulegen. Ein Hash dient dem Vergleich von Fassungen und ist keine elektronische Unterschrift. Behalten Sie das Ausgangsregister und eine nachvollziehbare Zuordnung der erzeugten Ausgaben. Nach einem späteren Registerupdate muss eine neue Ausgabe bewusst erzeugt werden.

### 3.6. Behördliche Vorlage und interne Pflege auseinanderhalten

Artikel 30 Absatz 4 DSGVO verlangt die Bereitstellung auf Anfrage der Aufsichtsbehörde. Daraus folgt keine allgemeine Pflicht, das interne Verzeichnis im Internet zu veröffentlichen. Lesen Sie Umfang und Frist der konkreten Anfrage und bereiten Sie ein vollständiges, sachliches Begleitschreiben vor. Offene Angaben sind transparent zu erläutern; sie werden nicht zur besseren Optik entfernt.

Eine Übermittlung erfolgt nur auf Grundlage des konkreten Auftrags beziehungsweise der dokumentierten Freigabe mit Empfänger und Anlagenstand. Prüfen Sie vor Versand, dass die freigegebene Fassung tatsächlich die zu versendende ist. Ohne Versandwerkzeug liefern Sie das Paket und den Entwurf, nicht eine erfundene Versandbestätigung. Für spätere Änderungen geht das Paket zurück an [Änderungen nachhalten](../aenderungen-nachhalten/SKILL.md).

## 4. Quellenpflicht

Folgen Sie [Rechtsquellen](../../references/rechtsquellen.md) und [Zitierweise](../../references/zitierweise.md). Artikel 30 Absatz 3 erlaubt schriftliche Führung einschließlich elektronischen Formats; die Norm schreibt das hier gewählte Dateischema nicht vor. Rechtsgrundlagen, Transferprüfung und DSFA-Entscheidungen behalten ihre Quellen und Aussagegrenzen auch in einer verkürzten Ansicht. Datierte Arbeitshilfen werden nicht als neue Rechtsnormen dargestellt.

## 5. Ausgabeformat

Liefern Sie die tatsächlich erzeugten Dateien mit klaren Links oder Pfaden sowie einen knappen Inhalts- und Prüfhinweis. Erläuterungen und Begleitschreiben sind vollständig ausformuliert; reine Schlagworte oder Skeletttexte genügen nicht. Formatierte Dokumente verwenden Times New Roman, 11 pt und dezimale Gliederung. Fehlt die Schrift technisch, wird die tatsächliche Ersatzschrift in einer getrennten Exportnotiz genannt.

Nennen Sie Stand, Revision, Auswahlumfang, noch offene Entscheidungen und gegebenenfalls nicht ausgeführte Prüfungen. Ein Downloadlink bezeichnet eine vorhandene Datei. Die erfolgreiche Ausgabe ist von einer externen Vorlage oder Freigabe getrennt zu bestätigen.

## 6. Beispiele

Die Geschäftsführung möchte einen kurzen Überblick, die Datenschutzkoordination die vollständige Arbeitsdatei. Sie erzeugen beide Ansichten aus derselben Revision, kennzeichnen die Verdichtung und halten offene Transfer- und DSFA-Fragen in beiden sichtbar.

Eine Behörde fordert das Verzeichnis für ein bestimmtes Unternehmen an. Sie prüfen die Gesellschaftszuordnung, bereiten die vollständige angefragte Fassung und ein erläutertes Begleitschreiben vor. Eine Freigabe zur internen Excel-Pflege wird nicht als Auftrag zum Behördenversand missverstanden.
