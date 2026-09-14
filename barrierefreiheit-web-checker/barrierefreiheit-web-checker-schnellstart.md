# 1. Digitales Angebot nachvollziehbar prüfen

Lies Nutzerauftrag, vorhandenen Code, Prüfprotokolle, Screenshots und Angebotsbeschreibung zuerst. Prüfe den beauftragten Nutzerweg, nicht ungefragt die gesamte Organisation. Liefere reproduzierbare Befunde mit Nutzerwirkung, Abhilfe und Wiederholungstest. Frage nur nach blockierenden Angaben. Ohne Browserzugriff vorhandene Belege analysieren, aber keine eigene Live-Prüfung behaupten.

## 2. Umfang und Maßstab festlegen

Trenne öffentliche Stelle und privates Angebot, Website und App, Produkt und Dienstleistung sowie Verbraucher- und reinen Unternehmensbezug. [Paragraf 1 BFSG](https://www.gesetze-im-internet.de/bfsg/__1.html) erfasst bestimmte Produkte und Dienstleistungen, darunter elektronischen Geschäftsverkehr für Verbraucher; nicht jede private Informationsseite pauschal dem BFSG unterwerfen. Ausnahmen und zeitliche Anwendbarkeit konkret prüfen.

Bei Kleinstunternehmen die dienstleistungsbezogene Ausnahme nach [Paragraf 3 Absatz 3 BFSG](https://www.gesetze-im-internet.de/bfsg/__3.html) prüfen, nicht ungeprüft auf Produkte übertragen. Für öffentliche Stellen einschlägiges Bundes- oder Landesrecht bestimmen. BFSG, BGG und BITV nicht zu einem einheitlichen Pflichtenkatalog vermischen.

Dokumentiere technische Referenz, Version, Konformitätsstufe und rechtlichen Bezug getrennt. Eine gewählte WCAG-Version ist nicht automatisch vollständig gesetzlich verbindlich oder harmonisiert. Technischer Befund bleibt auch dann beschreibbar, wenn seine genaue rechtliche Zuordnung noch offen ist.

## 3. Nutzerwege statt Scannerquote

3.1. Auswahl: Start, Suche, Auswahl, Warenkorb, Anmeldung, Formular, Bezahlung und Bestätigung nach Auftrag durchgehen. Komponentenvarianten und Fehlerzustände einbeziehen. Eine bestandene Startseite bescheinigt keinen barrierefreien Checkout.

3.2. Tastatur: Ohne Maus Erreichbarkeit, Auslösung, Reihenfolge und sichtbaren Fokus prüfen. Dialog öffnen, innerhalb navigieren, schließen und Rückkehr zum Auslöser kontrollieren. Festhalten, ob die Tastatur den Bereich wieder verlassen kann. [WCAG 2.2, Erfolgskriterium 2.1.2](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html) behandelt Tastaturfallen. Nicht jede absichtliche Fokusbegrenzung in einem korrekt schließbaren modalen Dialog als Fehler bewerten.

3.3. Screenreader und Formulare: Zugänglichen Namen, Rolle, Zustand, Beschriftung, Pflichtfeldhinweis, Fehlermeldung und Statusänderung untersuchen. Sichtbarer Text ist nicht zwangsläufig programmatisch zugeordnet. Testumgebung und tatsächlich eingesetzte Hilfstechnik nennen; aus Quelltext allein keinen bestandenen Screenreadertest ableiten.

3.4. Darstellung: Zoom, schmale Ansichten, Reflow, Textvergrößerung, Kontrast und Überlagerungen prüfen. Messwert, Vorder- und Hintergrund sowie Zustand festhalten. Keine Kontrastquote aus optischem Eindruck erfinden. Bilder nach Informationsfunktion beurteilen; dekorative und informative Inhalte unterscheiden.

3.5. Dokumente und Medien: Zugang, Lesereihenfolge, Struktur, Alternativtexte und gegebenenfalls Untertitel prüfen. Ein durchsuchbares PDF ist nicht allein deshalb barrierefrei. Bei fehlender Datei lediglich den Verlinkungsbefund liefern.

## 4. Befund als umsetzbares Ticket

Je Fehler URL oder Komponente, Zustand, Umgebung, Reproduktionsschritte, erwartetes und beobachtetes Verhalten, betroffene Nutzergruppe, Priorität und Beleg erfassen. Quellenkritisch trennen: eigener Test, übernommenes Nutzerprotokoll, Scannerhinweis und noch offene Vermutung.

Abhilfe konkret auf Verhalten ausrichten: etwa erreichbare Schließen-Schaltfläche und sinnvoller Fokus-Rücksprung statt „Barrierefreiheit verbessern“. Wiederholungstest mit demselben Nutzerweg festlegen. Automatische Prüfung und manuelle Abnahme getrennt dokumentieren. Keine Abnahme ohne tatsächlich wiederholten Test erteilen.

## 5. Auslieferung und optionale Vertiefung

Optional vertieft [Tastatur, Fokus, Navigation](skills/tastatur-fokus-ueberwachungsstelle/SKILL.md) die manuelle Prüfung. Ohne diese Datei mit Abschnitt 3 arbeiten. Ein fertiger Bericht enthält Prüfgrenzen, priorisierte Tickets, offene Tests und gegebenenfalls getrennte rechtliche Einordnung. Konformitätsunterlagen oder Erklärungen nur mit belegtem Umfang erstellen, nicht aus einer Stichprobe als Vollkonformität ableiten.

Rechtliche Behauptungen an amtlichen Quellen, technische Kriterien an der maßgeblichen Standardspezifikation verifizieren. Tatsächlich geprüfte Fassung, Abschnitt und URL nennen; keine erfundenen Testergebnisse. Optional: [Zitierweise](../references/zitierweise.md). Vollständige Sätze, dezimale Gliederung mit Leerzeilen und Times New Roman 11 pt beziehungsweise Exporthinweis verwenden. Ohne Export Text liefern. Keine Website ändern, Veröffentlichung vornehmen oder Verbraucherantwort versenden, sofern nicht beauftragt.
