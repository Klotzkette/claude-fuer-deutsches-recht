# 1. Rechenkern: Ausführung und Belegstand

Stand: 28.09.2026. Dieser Vermerk fasst den Ausführungsbericht des technischen Teilauftrags zusammen und trennt ihn von der anschließend vorgenommenen Leseprüfung der erhaltenen Artefakte. Die Hauptbearbeitung hat die elf Node-Fälle und die abschließend acht nativen Builder-Fälle vor Fertigstellung erneut erfolgreich ausgeführt. Ihre Konsolenprotokolle sind archiviert. Die übrigen Prüfungen wurden bei der Zusammenstellung dieses Ordners nicht erneut ausgeführt.

## 1.1. Gegenstand der Korrekturen

Das Padlet berücksichtigt alle drei Zuflussperioden. Anfangsverpflichtungen und neu fällige Verpflichtungen werden getrennt eingegeben; operative Zahlungen auf bereits erfasste Schulden erhöhen die Passiva nicht erneut. Zum tatsächlichen Stichtag werden die folgenden 21 Kalendertage angezeigt. Fehlende oder ungültige Eingaben sowie der ausstehende Belegabgleich bleiben offen. Eine Quote und die Anzahl von Indizien lösen keine rechtliche Diagnose aus.

Die Excel-Vorlage führt vier gesonderte Statusbeträge, einen ausdrücklichen Belegabgleich und das genaue Zeitfenster. Die ursprüngliche Wochenrechnung bleibt erhalten; laut dokumentiertem Abgleich wurden im bisherigen Raster nur die Überschriften A1 und A3 geändert. Der Status wird nicht automatisch aus Wochenzahlungen abgeleitet.

Der Python-Builder erzeugt einen operativen Hinweis aus drei vollständigen Planwochen. Ein früher negativer Wochenendbestand bleibt erkennbar, auch wenn später ein Zufluss folgt. Fehlende Wochen, fehlende Ein- oder Auszahlungsobjekte, fehlende Datenbestätigung und unvollständige Endfenster gelten nicht als nachgewiesene Deckung. Dies gilt nach einer abschließenden Korrektur auch dann, wenn eine unvollständige Vorwoche den Anfangsbestand späterer Perioden beeinflusst. Dieser Hinweis ersetzt keinen insolvenzrechtlichen Status.

## 1.2. Ausgeführte Prüfungen und abschließende Wiederholung

| Prüfart | Berichteter Umfang und Ergebnis | Abgrenzung |
| --- | --- | --- |
| Automatisierte Padlet-Rechnung | Elf Fälle bestanden: fehlende Werte gegenüber Null, Erstperiodenzufluss, Altschuldzahlung, fällige ungezahlte Schuld, neue Fälligkeiten, Fünfprozentlücke, Einzelindiz, ungültiges Datum, negativer Betrag, früher Engpass und Altstandimport. | Das Repo-Skript führt das extrahierte JavaScript in einer Node-VM aus. Dies ist kein Browsertest. |
| Browserinteraktion | Der technische Teilauftrag berichtet einen erfolgreichen Chrome-Lauf mit leerem Ausgangszustand, Formulareingaben, Erstperiodenzufluss, Jahreswechsel, Einzelindiz, Desktop-/Mobilansicht und Prüfung auf Laufzeitfehler. | Der Browserlauf ist von den elf Node-Fällen zu unterscheiden. Seine vollständige Interaktions- und Konsolenspur wurde nicht dauerhaft in diesen Ordner übernommen. |
| Excel-Vorlage | Sieben Varianten wurden laut Teilauftrag zunächst mit Artifact Tool und zusätzlich nativ mit LibreOffice neu berechnet: leer, gedeckt, Fünfprozentlücke, echte Nullbeträge, fehlender Posten, negativer Betrag und Altschuldzahlung. | Hierzu liegen getrennte Soll-/Ist-/native Ergebnisdaten vor. |
| Python-Builder | Der abschließende Lauf umfasst acht bestandene Fälle: leer, gedeckt, früher Engpass vor späterem Zufluss, nur zwei Wochen, fehlender Belegabgleich, echte Nullbeträge, fehlende Vorwoche und gedeckter Vierwochen-Gegenfall. Die beiden unvollständigen Endfenster bleiben offen. | Das Python-Testskript erzeugt Builder-Dateien und lässt sie tatsächlich mit LibreOffice konvertieren. Diese acht Fälle sind nicht die sieben Varianten der gesonderten Excel-Vorlage. |
| Leere Auslieferungsvorlage | Die endgültige Vorlage wurde nach dem Export nochmals nativ neu berechnet. Das Ergebnis lautet `UNVOLLSTÄNDIG`, die Lücke bleibt offen und es wurden keine Formelfehler berichtet. | Hash und Ergebnis sind gesondert archiviert. |
| Erhaltung der Vorlage | Der Teilauftrag berichtet erhaltene Wochenformeln und Eingabewerte sowie erhaltene Druckeigenschaften und Fensterfixierung. | Die archivierte JSON-Datei enthält die Vergleichsergebnisse, nicht das vollständige Vergleichsprotokoll. |

## 1.3. Nachträglich anhand vorhandener Artefakte geprüft

Die Leseprüfung der technischen Belege bestätigt, dass [template-native-proof.json](belege/template-native-proof.json) sieben Fälle mit übereinstimmenden erwarteten, berechneten und nativen Ergebnissen enthält. Die zusätzlich im Arbeitsbereich vorhandenen sieben nativen Ausgabe-XLSX enthielten entsprechende gespeicherte Ergebniszellen und LibreOffice-Metadaten; gespeicherte Excel-Fehlerzellen wurden nicht gefunden. Diese Ausgabe-XLSX werden in diesem Qualitätsordner nicht vervielfältigt.

[final-native-proof.json](belege/final-native-proof.json) dokumentiert die leere Endvorlage und ihren SHA-256. Der Hash der im Repository liegenden Auslieferungsvorlage wurde bei der Archivierung erneut berechnet und stimmt mit `984dcc0c26e9bf97fc035dd855624ce00e1dd4af33cf9b16c58c57a884457e38` überein. Die native leere Ausgabe enthält die Ergebnisse `offen`, `offen` und `UNVOLLSTÄNDIG`.

[xlsx-preservation.json](belege/xlsx-preservation.json) hält für beide Arbeitsblätter die Erhaltung der Druckmetadaten und Fensterfixierung fest. Für das ursprüngliche Wochenraster nennt sie nur A1 und A3 als geänderte Zellen sowie die erhaltenen Formeln und Eingabewerte. Dies ist ein gespeicherter Ergebnisvermerk, kein vollständiger Nachweis jedes einzelnen Vergleichsschritts.

Die vorhandenen Browserbilder zeigen Desktop- und Mobilansichten mit Erstzufluss 100, Verpflichtungen 100, einem Indiz und dem Jahreswechselfenster vom 29.12.2026 bis 18.01.2027. Ein Screenshot allein belegt weder die vorgelagerte Eingabefolge noch einen leeren Ausgangszustand oder das Ausbleiben aller Laufzeitfehler. Diese Aussagen bleiben dem Ausführungsvermerk des damaligen Browserlaufs zugeordnet.

Die elf Padlet-Fälle wurden durch die Hauptbearbeitung erneut ausgeführt; [padlet-regression.log](belege/padlet-regression.log) enthält elf erfolgreiche Einzelmeldungen und die Abschlussmeldung. Nach einer zusätzlich reproduzierten und behobenen Vorwochenlücke wurde der Builder um zwei gezielte Fälle ergänzt. [builder-native-regression.log](belege/builder-native-regression.log) enthält den erfolgreichen abschließenden Lauf aller acht nativen Szenarien. Beide Läufe endeten laut Ausführungsmeldung der Hauptbearbeitung mit Exitcode 0. Die drei Vorlagen-JSONs sind davon getrennte Belege und werden nicht als Ersatzprotokoll für diese Tests ausgegeben.

## 1.4. Wiederholbare Repo-Prüfungen

Die folgenden Befehle werden im Repository-Wurzelverzeichnis ausgeführt:

```sh
node scripts/test-liquiditaetsplanung-rechenlogik.mjs
python3 scripts/test-liquiditaetsplanung-excel.py
```

Das [Node-Skript](../../../scripts/test-liquiditaetsplanung-rechenlogik.mjs) benötigt die Node-Standardbibliothek. Das [Python-Skript](../../../scripts/test-liquiditaetsplanung-excel.py) benötigt Python sowie `libreoffice` oder `soffice` im Suchpfad. Alternativ kann die ausführbare Datei über `SOFFICE` angegeben werden. Fehlt LibreOffice, wird die native Prüfung ausdrücklich als nicht ausgeführt gemeldet und der Test endet erfolglos.

Diese Befehle wiederholen die elf Padlet-Rechenfälle und die acht nativen Builder-Fälle. Sie wiederholen weder automatisch die Browserinteraktion noch die sieben Varianten der gesonderten Auslieferungsvorlage. Die gespeicherten Vorlagenbelege sind daher zusätzlich zu betrachten.

## 1.5. Reproduzierter Builder-Fehler, Korrektur und Grenzen

Die abschließende Nachprüfung reproduzierte einen zusätzlichen Fehler: Waren die Daten einer Vorwoche unvollständig, konnte ein späteres, für sich vollständig eingegebenes Dreiwochenfenster dennoch als gedeckt erscheinen, obwohl sein Anfangsbestand nicht belastbar war. Die Korrektur hält die dadurch betroffenen Folgezustände offen. Der neue native Fall `vorwoche-fehlt` prüft genau diese Konstellation. Der positive Gegenfall `vier-wochen-gedeckt` stellt sicher, dass vollständig belegte spätere Fenster weiterhin als rechnerisch gedeckt ausgewiesen werden können. Der finale native Lauf belegt beide Fälle zusammen mit den bisherigen sechs Szenarien.

## 1.6. Exportkorrektur und verbleibende Grenzen

Der technische Teilauftrag berichtet, dass der Artifact-Tool-Export die ursprünglichen Druckmetadaten nicht erhielt und nach dem Leeren zweier Eingabezellen leere Formel-XML-Knoten zurückließ. Daraufhin wurden ausschließlich die ursprünglichen Druck-XML-Blöcke zurückkopiert und die beiden leeren Formelknoten entfernt. Finanzformeln und Werte wurden dadurch nicht neu erzeugt. Die endgültige Vorlage wurde anschließend nativ geprüft. Die Autorenschaft und jeder einzelne Exportreparaturschritt werden durch die hier archivierten Ergebnis-JSONs nicht vollständig protokolliert.

Die technische Prüfung betrifft konkrete Eingaben, Formeln, Zustände und Ansichten. Sie belegt keine juristische Richtigkeit jeder denkbaren Planung und keine allgemeine Kompatibilität mit sämtlichen Excel-Versionen. Eine rechnerische Deckung ist keine Bescheinigung der Zahlungsfähigkeit.
