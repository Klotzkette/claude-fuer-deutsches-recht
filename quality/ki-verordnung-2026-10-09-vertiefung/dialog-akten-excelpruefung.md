# 1. Excel-Prüfung der Dialogakten

Stand: 9. Oktober 2026. Geprüft und eingefroren sind ausschließlich die beiden Arbeitsmappen in `ki-verbot-regnitz-sorglosabo` und `ki-transparenz-pegnesus-redaktion` sowie ihr MJS-Builder. Die zugehörigen DOCX-, PDF- und EML-Dateien waren nicht Gegenstand dieser Reparatur. Der zentrale Bearbeiter wurde über den notwendigen Neubau der Mailanhänge informiert.

## 1.1. Gelesene Grundlagen und reparierte Befunde

Die bestehenden XLSX-Dateien wurden vor Änderungen mit ihren tatsächlichen Formeln und gespeicherten Ergebnissen gelesen. Der Abgleich bezog die aktuellen Aktenangaben aus `scripts/data/ki-vertiefung-dialog-akten.json` ein, insbesondere Prüfauftrag, Kontrollnotizen und Buchhaltungsnachricht. Die Ausgangssummen waren richtig. Eine ungeklärte Zusatzlaufzeit blieb bereits im Ausgangsstand offen.

Bei Regnitz wurden zusätzliche Leerwertprüfungen erforderlich: Eine fehlende Grundrate, Zusatzrate, Journalgutschrift oder Buchungsangabe darf weder stillschweigend als Null gelten noch in einer Folgeformel einen Text-Rechenfehler erzeugen. Die fehlenden Angaben werden jetzt durchgehend als „offen“ weitergeführt. Die Quelle für die Zusatzrate nennt jetzt den Prüfauftrag, der die sieben Euro tatsächlich angibt. Konkrete Buchungstage waren in den vorliegenden Belegen nicht nachgewiesen; die Arbeitsmappe zeigt deshalb nur September und Oktober 2026. Die Zahlendarstellung bleibt von der benachbarten Einheit klar getrennt. Beschriftungen behaupten nach Änderungen der Laufzeit oder Rate keine unveränderten festen Eingabewerte.

Bei Pegnesus konnte der Vorspannanteil bei fehlender Beginn- oder Endzeit einen Rechenfehler erzeugen. Die Formel prüft jetzt beide Rechengrößen. Zwei leere Versionskennungen ergeben nicht mehr „gleich“, sondern „abweichend/offen“. Ein fehlender Status zu einer Medienprobe ergibt für die Gesamtzahl „offen“. Diese Reparaturen ergänzen keine tatsächliche Medienprüfung und keine Freigabe.

## 1.2. Rechenbefunde und tatsächlich ausgeführte Proben

Regnitz bleibt im gesicherten Ausgangsstand bei 791 Euro Grundentgelt, 174 Euro belegtem Banknetto und 617 Euro rechnerischer Differenz. Zusatzentgelt und daraus abgeleiteter Gesamtbetrag sind wegen der fehlenden Monatszahl offen. Eine ausdrücklich eingegebene Null ergibt 791 Euro Gesamtbetrag; 18 Zusatzmonate ergeben 917 Euro. Die Journalgutschrift von 39 Euro wird nicht als bereits erfolgte Bankerstattung abgezogen. Rente abzüglich Warmmiete ergibt 476 Euro; daraus folgt ein reiner Kostenanteil von rund 8,2 Prozent, kein frei verfügbares Einkommen.

Pegnesus enthält sechs geplante Ausspielungen, fünf abweichende beziehungsweise offene Fassungen und keine belegte Medienprobe. Der geplante Clip dauert 30 Sekunden. Er enthält nach dem Schnittplan keine Sekunde des ursprünglichen sechssekündigen Vorspanns. Eine Änderung des Clipbeginns auf null ergibt sechs Sekunden enthaltenen Vorspann. Eine Clipdauer von null ergibt beim Anteil „n.a.“. Fehlende Vorspannzeiten und fehlender Clipbeginn ergeben „offen“; die Ausgangswerte wurden anschließend wiederhergestellt.

Der Builder hat 36 konkrete Basis-, Null-, Leer- und Änderungsproben erfolgreich ausgeführt. Danach wurden die tatsächlich exportierten XLSX-Dateien erneut mit dem Tabellenwerkzeug importiert. Weitere 20 Proben bestätigten unter anderem die wiederhergestellten Basiswerte, die offenen Zusatzmonate, den Nullnenner, fehlende Geldangaben, fehlende Vorspannzeiten und zwei leere Versionskennungen. Dieser Importlauf schrieb keine Originaldatei.

In der exportierten Regnitz-Datei sind alle zehn Formeln mit Ergebnissen gespeichert, in Pegnesus alle 13. Keine Formel enthält einen fehlenden Ergebnis-Cache oder einen gespeicherten Excel-Fehler. Die konkreten Formeln, Ergebnisse, Einzelproben und SHA-256-Werte stehen in [dialog-akten-excelpruefung.json](dialog-akten-excelpruefung.json).

## 1.3. Sichtprüfung und Übergabe

Alle fünf Tabellenblätter wurden nach der Reparatur neu gerendert und einzeln visuell geprüft: Kosten, Eingaben, Buchungen, Ausspielung und Schnittplan. Überschriften, Zahlen, Eingaben, Quellenhinweise und erläuternde Grenzen sind vollständig lesbar. Es wurden keine abgeschnittenen Texte oder Überlagerungen festgestellt. Blaue Eingaben und schwarze Formelergebnisse bleiben unterscheidbar.

Beide XLSX-Dateien sind gegenüber dem übernommenen Stand geändert. Nach dem abschließenden Importtest wurden ihre Dateihashes erneut kontrolliert. Die Tabellen und der MJS-Builder sind eingefroren. Der notwendige Neubau der betroffenen EML-Anhänge sowie die Aktualisierung des Gesamtmanifests und der Sammelartefakte wurden dem zentralen Bearbeiter übergeben; deren erfolgreiche Ausführung wird durch diesen Tabellenbericht nicht vorweggenommen.
