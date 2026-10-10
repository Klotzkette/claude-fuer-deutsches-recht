---
name: aenderungen-nachhalten
description: Pflegt Änderungen an Tätigkeiten, Quellen und Prüfständen mit Revisionen und Konfliktabgleich. Erkennt erneuten DSFA-Prüfbedarf, veraltete Angaben und offene Maßnahmen, ohne bestehende Daten stillschweigend zu überschreiben.
---

# Verzeichnisänderungen nachvollziehbar nachhalten

## 1. Zweck und Anwendungsfall

Pflegen Sie das Verzeichnis nach konkreten Ereignissen und bei vereinbarten Überprüfungen. Der Skill übernimmt neue Tatsachen, macht Unterschiede nachvollziehbar und leitet erforderliche Folgeprüfungen ein. Ziel ist eine aktuelle führende Fassung statt vieler widersprüchlicher Excel-Anhänge. Er behauptet keinen ständig laufenden Hintergrunddienst, wenn ein solcher nicht tatsächlich eingerichtet wurde.

Die Pflege kann durch eine Nachricht „Unser Anbieter hat jetzt einen neuen Supportstandort“ oder durch eine überarbeitete Tabelle ausgelöst werden. Der bestehende Auftrag erlaubt die notwendigen internen Vergleiche. Eine neue gesamte Unternehmensaufnahme ist nicht erforderlich, wenn nur ein bestimmter Prozess geändert wurde.

## 2. Eingaben

Lesen Sie führende JSON-Datei, Registerkennung, aktuelle Revision, neue Unterlagen und gegebenenfalls die exportierte Ausgangsmappe. Erfassen Sie den Änderungsanlass, die berichtende Person, betroffene Tätigkeiten und das tatsächliche Änderungsdatum. Prüfen Sie, ob eine Nachricht einen Vorschlag, einen bereits erfolgten Wechsel oder eine verbindlich beschlossene Änderung beschreibt.

Fehlen Zeitpunkt oder Umfang, übernehmen Sie nur den belegten Teil. Bewahren Sie Quellunterlagen und vorherige Stände. Fragen Sie nicht nach Zugangsdaten oder unnötigen personenbezogenen Einzelbelegen. Ein Screenshot kann eine geänderte Funktion belegen; er beweist nicht automatisch deren Einsatz in allen Abteilungen.

## 3. Ablauf und Checkliste

### 3.1. Den Umfang der Änderung bestimmen

Vergleichen Sie Zwecke, Rollen, Daten- und Personenkategorien, Empfänger, Länder, Systeme, Löschfristen, technische Maßnahmen und Verantwortlichkeiten. Stellen Sie fest, ob eine bestehende Tätigkeit fortgeschrieben, aufgeteilt oder eine neue Tätigkeit angelegt werden muss. Ein bloßer Produktname kann sich ändern, ohne den Prozess zu ändern; eine gleich benannte Software kann dagegen neue Profilingfunktionen erhalten.

Ordnen Sie die Änderung den stabilen Tätigkeitskennungen zu. Bei mehreren betroffenen Vorgängen erfassen Sie einen gemeinsamen Anlass und getrennte Auswirkungen. Eine neue Unterauftragnehmerliste kann beispielsweise Kundenhosting und interne Personalverwaltung unterschiedlich betreffen. Eine angeblich globale Änderung wird nicht ungeprüft auf alle Einträge übertragen.

### 3.2. Ausgangsrevision und Konflikte prüfen

Nutzen Sie für Dateimutationen den Helfer [vvt.py](../../scripts/vvt.py) entsprechend seiner tatsächlichen Hilfe und dem [Datenmodell](../../references/datenmodell.md). Prüfen Sie Registerkennung und Ausgangsrevision vor dem Import. Ein Export aus einer älteren Registerfassung ist kein Auftrag, inzwischen eingegangene Informationen zurückzusetzen. Bei Konflikten entsteht eine Vergleichsliste mit bisherigem, eingehendem und vorzuschlagendem Stand.

Fehlende Excel-Zeilen bedeuten keine Löschanweisung. Eine leere Zelle ist von einer ausdrücklich bestätigten Korrektur zu unterscheiden. Eine beendete Tätigkeit wird mit ihrem Status und nachvollziehbarer Historie erhalten, soweit der Arbeitsauftrag und die berechtigte Dokumentation dies erfordern. Beendigung des Betriebs bedeutet nicht, dass alle Daten bereits gelöscht sind. Prüfen Sie verbleibende Aufbewahrung und Abwicklungszugriffe.

### 3.3. Rechtsfolgen und erneute Prüfungen auslösen

Artikel 24 DSGVO verlangt erforderlichenfalls Überprüfung und Aktualisierung geeigneter Maßnahmen. Artikel 35 Absatz 11 verlangt eine Überprüfung der Folgenabschätzung jedenfalls bei Änderungen des verarbeitungsbezogenen Risikos. Neue Zwecke, Personengruppen, Überwachungsfunktionen, sensible Daten oder Drittlandszugriffe können deshalb einen materiellen Nachlauf erfordern. Ein alter Prüfvermerk bleibt historisch, trägt aber nicht automatisch den neuen Sachstand.

Lassen Sie [Rechtsgrundlagen und Löschung](../rechtsgrundlagen-loeschung-pruefen/SKILL.md) veränderte Zwecke oder Fristen prüfen. Neue Empfänger, Zugriffe und Schutzmaßnahmen gehen an [Dienstleister, Transfers und TOM](../dienstleister-transfers-tom-pruefen/SKILL.md). Eine neue oder überholte DSFA-Vorprüfung bearbeiten Sie mit [Risiken und DSFA](../risiken-dsfa-pruefen/SKILL.md). Die Gegenprüfung soll konkret benennen, welche bisherige Annahme jetzt nicht mehr trägt.

### 3.4. Menschliche Bewertung und technische Speicherung trennen

Der Helfer kann eine dokumentierte Entscheidung mit dem aktuellen Sachstand verbinden. Er kann nicht beurteilen, ob die angegebene Person tatsächlich geprüft hat oder eine eingegebene Begründung juristisch genügt. Erfassen Sie deshalb nur wirklich abgegebene Entscheidungen mit Name, Zeitpunkt, Begründung und Quellen. Erfinden Sie keine Freigabe durch den Datenschutzbeauftragten und kein Einverständnis der Geschäftsführung.

Technische Prüfsummen und Revisionsangaben erleichtern Nachvollziehbarkeit, sind aber keine qualifizierten elektronischen Signaturen und kein manipulationssicheres Langzeitarchiv. Eine veraltete Bewertung wird als überholt angezeigt. Ihre fachliche Erneuerung braucht tatsächliche Prüfung; das unveränderte Kopieren des alten Textes und Datums erledigt sie nicht.

### 3.5. Wiedervorlagen und offene Maßnahmen pflegen

Vereinbaren Sie sinnvolle interne Prüfintervalle abhängig von Risiko und Veränderung. Kennzeichnen Sie das Datum als Organisationsentscheidung, soweit es nicht auf einer gesondert nachgewiesenen rechtlichen Frist beruht. Die DSGVO enthält keine allgemeine Pflicht, jedes Verzeichnis genau jährlich oder monatlich neu zu unterschreiben. Ereignisbezogene Aktualisierungen können früher erforderlich sein.

Jede Maßnahme nennt eine zuständige Person, das benötigte Ergebnis und den Termin. Ein abgelaufener Termin wird als offen und überfällig gemeldet, nicht als automatisch erledigt. Trennen Sie Nachfragen, materielle Entscheidungen und technische Umsetzung. Ein unbeantwortetes Schreiben an den Cloudanbieter beendet die Prüfung nicht. Ohne eingerichteten Scheduler ist eine Wiedervorlage nur gespeicherte Information; eine tatsächliche Erinnerung darf erst nach entsprechender Einrichtung zugesagt werden.

### 3.6. Einen überprüfbaren Abschluss erzeugen

Nach dem Speichern lesen Sie den neuen Stand erneut und prüfen die betroffenen Kennungen, Revisionen und offenen Entscheidungen. Stellen Sie sicher, dass unveränderte Tätigkeiten nicht unbeabsichtigt verloren gingen. Eine neu erzeugte Excel-Datei erhält den aktuellen Ausgangsstand für spätere Importe. Eine externe Weitergabe ist von diesem internen Export getrennt zu behandeln.

Übergeben Sie `aenderungsprotokoll` und `register` an [Verzeichnis ausgeben](../verzeichnis-ausgeben/SKILL.md). Bei fehlerhaftem Import kehren Sie zum letzten gesicherten Stand zurück, halten die Fehlermeldung fest und erzeugen einen korrigierten Vorschlag. Führen Sie einen fehlgeschlagenen Import nicht mehrfach blind aus. Der Nutzer soll erkennen, ob lediglich vorbereitet, gespeichert oder fachlich entschieden wurde.

## 4. Quellenpflicht

Beachten Sie [Rechtsquellen](../../references/rechtsquellen.md), insbesondere Artikel 5 Absatz 2, 24, 30 und 35 Absatz 11 DSGVO, sowie [Zitierweise](../../references/zitierweise.md). Unterschiedliche historische Normstände werden nicht vermischt. Geplante Änderungen der Verzeichnis-Ausnahme werden als Gesetzgebungsverfahren beobachtet, aber erst nach Prüfung von geltendem Text und Inkrafttreten in die rechtliche Bewertung übernommen.

## 5. Ausgabeformat

Liefern Sie einen kurzen Änderungsbericht, die neue Registerdatei und erforderliche Folgeaufträge. Bericht und Anschreiben sind vollständig ausformuliert; keine unerklärten Statuskürzel als einziges Ergebnis. Verwenden Sie Times New Roman, 11 pt und dezimale Gliederung für Dokumente. Ein Änderungsvergleich kann strukturierte Werte enthalten, muss aber den sachlichen Grund in verständlicher Sprache nennen.

Nennen Sie alte und neue Revision, betroffene Kennungen, übernommene Angaben, Konflikte und offene Entscheidungen. Behaupten Sie keine dauernde Überwachung oder rechtliche Freigabe allein aufgrund eines erfolgreichen Skriptlaufs.

## 6. Beispiele

Zwei Abteilungen bearbeiten dieselbe exportierte Excel-Datei unabhängig voneinander. Nach dem ersten Import wird der zweite nicht still darübergeschrieben. Sie vergleichen die Änderungen mit dem aktuellen Register und übernehmen nur den abgestimmten Stand in einer neuen Revision.

Eine bisher auf Terminorganisation beschränkte Praxissoftware erhält eine KI-Funktion zur Gesundheitsbewertung. Sie erfassen Funktion und geplanten Einsatz, markieren die alte DSFA-Vorprüfung als nicht ausreichend für den neuen Sachstand und verlangen eine erneute begründete Bewertung vor Einführung.
