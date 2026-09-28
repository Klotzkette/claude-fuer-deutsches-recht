---
name: praesentation-pruefen-und-proben
description: "Prüft einen juristischen Foliensatz vor Vortrag oder Weitergabe auf Aussagegenauigkeit, Nachweise, Verständlichkeit, Lesbarkeit und technische Vollständigkeit. Korrigiert konkrete Mängel, plant oder begleitet die Zeitprobe und trennt tatsächlich getestete Funktionen von noch offenen Prüfungen."
---

# Präsentation prüfen und proben

## 1. Zweck und Anwendungsfall

Führe eine inhaltliche und technische Schlusskontrolle am tatsächlichen Foliensatz durch und behebe festgestellte Mängel. Der Skill liefert eine korrigierte Fassung, nicht nur eine allgemeine Liste guter Vorsätze. Eine Zeitprobe oder Funktionsprüfung nur als durchgeführt melden, wenn sie tatsächlich stattgefunden hat.

## 2. Eingaben

Lies die finale PPTX oder vollständige Textfassung einschließlich Notizen, Quellen und relevanter Originale. Übernimm Anlass, Publikum, Redezeit und Weitergabeumfang aus dem Auftrag. Kläre nur noch offene Zielumgebung, besondere Zugänglichkeitsanforderungen oder die Frage, ob interne Notizen mitverteilt werden sollen. Fehlende Quellen betreffen zunächst die konkrete Aussage, nicht automatisch die gesamte Präsentation.

## 3. Ablauf und Checkliste

1. Den roten Faden prüfen: Wird die angekündigte Frage beantwortet und der gewünschte Abschluss erreicht? Eine Entscheidungsvorlage braucht eine Entscheidung oder einen klaren Klärungsbedarf, ein Vortrag eine verständliche fachliche Schlussfolgerung. Wiederholte Vorreden entfernen, notwendige Einschränkungen erhalten.
2. Jede tragende Rechtsaussage mit Normfassung und tatsächlich gelesener Fundstelle abgleichen. Stimmen Tenor, Entscheidungsart, Datum, Aktenzeichen und Reichweite? Eigene Folgerungen nicht als Gerichtsposition ausgeben. Widersprüche zwischen Titel, Notiz und Quellenblatt gezielt korrigieren.
3. Zahlen und Belege prüfen: Einheit, Zeitraum, Rundung, Summen, Seitenbezug und Kennzeichnung von Ausschnitten. Unleserliche Screenshots durch eine besser lesbare Originalansicht oder getrennte Erläuterung ersetzen; fehlende Belegteile nicht rekonstruieren.
4. Sämtliche Folien in der tatsächlichen Ausgabe sichten. Überlauf, Überdeckung, kleine Quellenzeilen, abweichende Schrift, verzerrte Bilder und schwer lesbare Farben beheben. Lesereihenfolge, Alternativtexte und aussagekräftige Titel prüfen. Ein automatischer Bericht ergänzt die Sichtprüfung, ersetzt sie nicht.
5. Für die Weitergabe Kommentare, Notizen, ausgeblendete Folien, eingebettete Tabellen und Eigenschaften kontrollieren. Eine öffentliche Fassung bei Bedarf getrennt speichern. Nicht sämtliche Notizen löschen, wenn sie das bestellte Vortragsmanuskript enthalten; sensible und zugehörige fachliche Inhalte unterscheiden.
6. Echte Vortragsprobe nur mit Wiedergabe und Zeitmessung durchführen oder durch den Vortragenden durchführen lassen. Eine aus Notizen abgeleitete Dauer als Schätzung kennzeichnen. Bei Überschreitung konkrete Folien kürzen, verschieben oder streichen und die Übergänge nachziehen. Fragen und Pausen nicht heimlich aus dem Zeitbudget entfernen.
7. Bei Animationen Klickfolge, jeden Zwischenstand, Rücksprung und statische Ausweichfassung prüfen. Nach einer aufgezeichneten Zeitprobe den gewünschten manuellen Folienwechsel kontrollieren. Ohne Wiedergabewerkzeug eine genaue Prüfanleitung liefern, nicht „Animation funktioniert“ behaupten.
8. Korrekturen erneut an den betroffenen Folien und abhängigen Verweisen prüfen. Keine unveränderte Gesamtproduktion wiederholen. Abschließend korrigierte Dateien und eine kurze, priorisierte Übergabe mit tatsächlich verbliebenen Hindernissen liefern.

Für die technische Paketkontrolle bei verfügbarem Python den [lokalen Prüfer](../../scripts/pptx_pruefen.py) mit `python3 scripts/pptx_pruefen.py DATEI.pptx` aus dem Plugin-Verzeichnis ausführen. Auf der Endfassung nicht `--template` setzen. Fehler blockieren die technische Freigabe; Warnungen einzeln klären. Eine Suche mit wiederholtem `--forbid-term` ergänzt die Prüfung konkret unerwünschter Angaben, erfasst aber keine Bildschrift. Ein erfolgreicher Rückgabewert bescheinigt keine Lesbarkeit, Barrierefreiheit, Rechtsrichtigkeit oder abgespielte Animation.

## 4. Quellenpflicht

Juristische Nachweise nach [Zitierweise](../../references/zitierweise.md), Gerichtsbelege nach [Gericht und Belegtreue](../../references/gericht-und-belegtreue.md) und technische Kontrollen nach [PowerPoint und Barrierearmut](../../references/powerpoint-und-barrierearmut.md) prüfen. Nicht aus einem erfolgreichen Export auf Rechtsrichtigkeit oder aus einem Vorschaubild auf die erfolgreiche Bildschirmpräsentation schließen.

## 5. Ausgabeformat

Liefere die tatsächlich korrigierte Präsentation oder, falls nur Text bearbeitbar ist, die vollständig überarbeiteten betroffenen Folien mit Notizen. Der kurze Prüfvermerk nennt Befund, Änderung, konkrete geprüfte Fassung und verbleibende Grenze. Für eine noch offene Prüfung angeben, wer was im Zielprogramm prüfen muss. Keine pauschale Fehlerfreiheit oder garantierte Kompatibilität bescheinigen.

Die Ausformulierungspflicht gilt für Sprechtexte und Übergabeerläuterungen; unverständliche Stichworte nicht als Endfassung zurückgeben. Präsentationsfolien folgen aus Lesbarkeitsgründen der Vorlage. Ein gesonderter juristischer Prüfvermerk verwendet, soweit technisch möglich, Times New Roman 11 pt und dezimale Gliederung. Eine Tabelle mit Prüfstatus darf den Vermerk ergänzen, aber eine notwendige Erklärung nicht ersetzen.

## 6. Beispiele

„Kann das morgen so an die Mandanten raus?“ Prüfe die konkrete Empfängerfassung einschließlich verborgener Inhalte, vollständiger Nachweise und Lesbarkeit; keinen Versand auslösen.

„Wir brauchen statt 60 nur 30 Minuten.“ Priorisiere Kernaussagen und nötige Vorbehalte, passe Notizen und Übergänge an und trenne eine geschätzte von einer tatsächlich gemessenen Dauer.
