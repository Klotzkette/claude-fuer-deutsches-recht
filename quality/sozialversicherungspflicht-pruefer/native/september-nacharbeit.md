# Begrenzte Septemberkorrektur – erneut freigegeben

Vor dem Eingriff wurden alle 27 nummerierten Originale aus dem aktuellen Akten-ZIP unverändert nach `qa-local/probe-werkstatt/eingabe-original-stand-1` gesichert. `snapshot-manifest.json` dokumentiert ZIP-Hash und Einzeldateihashes. Der Stand der laufenden Werkstattprobe bleibt damit rekonstruierbar.

Geändert wurden ausschließlich `03_Unterrichtsbetrieb_September_2025.docx` und der entsprechende Textabschnitt in `scripts/build-sv-lehre-programmierung-akten.py`. Der Generator wurde nicht ausgeführt. Die übrigen 26 nummerierten Originale sind gegenüber dem Stand unmittelbar vor dem Eingriff bytegleich. Andere Fallakten, Tabellen, Gesamt-PDFs und ZIPs wurden nicht geändert.

Der Betriebsplan enthält nun die zusätzlichen Septemberreservierungen: Mittwoch 10./17./24. September jeweils 10–15.15 Uhr in Raum 4 mit sieben Einheiten; Freitag 12./26. September jeweils 10–14.30 Uhr in Raum 3 mit sechs Einheiten. Die Wochentage wurden rechnerisch geprüft. Vier reguläre Dienstage mit je sechs ganzen Einheiten und drei reguläre Donnerstage mit je acht Einheiten ergeben 48 Zeitfenster; hinzu kommen 33, insgesamt 81. Zwei bleiben zunächst frei. Damit sind die 76 erteilten und drei vergüteten Ausfälle räumlich und zeitlich möglich. Die Rechnungsbeträge wurden nicht verändert; montags wird der bestehende Auftrag in Pankow berücksichtigt.

Das DOCX wurde mit dem gebündelten Python und dem kanonischen `render_docx.py` unter explizitem gebündelten `SOFFICE`-Pfad gerendert. Die einzige Seite wurde vollständig visuell geprüft: keine Überläufe, keine abgeschnittenen Inhalte, kein unerwünschter Seitenumbruch. Render und Hashes liegen im Unterordner `render` sowie in `aenderungsmanifest.json`.

Freeze: Original 03 und Builder sind wieder final. Root kann die davon abhängigen Auslieferungen neu bauen. Keine weiteren Mutationen durch diesen Subagenten geplant.
