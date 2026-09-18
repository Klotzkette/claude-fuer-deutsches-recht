# 1. Digitale Barrierefreiheit prüfen und Nachbesserung begleiten

Prüfe den beauftragten Nutzerweg und erstelle den gewünschten Prüfbericht, Maßnahmenplan, Erklärungstext oder die Antwort auf eine Beschwerde. Lies vorhandenen Auftrag, Code, Angebotsbeschreibung, Screenshots und Prüfprotokolle zuerst.

Ein technischer Prüfauftrag verlangt weder automatisch eine rechtliche Gesamtbewertung noch einen gerichtlichen Antrag.

## 1.1. Angebot und Prüfmaßstab bestimmen

Unterscheide Website, App, PDF, Formular, Checkout und Intranet sowie öffentliche Stelle, privaten Anbieter, Produkt und Dienstleistung. Prüfe Verbraucherbezug, Anbieterrolle, Bereitstellungsdatum und mögliche Ausnahmen. BFSG, BGG, BITV und die Web Accessibility Directive (WAD) dürfen nicht als einheitlicher Pflichtenkatalog behandelt werden. Berücksichtige daneben konkret vereinbarte Vergabe-, Fördermittel- oder Vertragsanforderungen.

Ordne gesetzliche Anforderung, BFSGV, EN 301 549, WCAG-Kriterium, Version und Konformitätsstufe getrennt zu. Ein technischer Fehler ist nicht schon deshalb ein nachgewiesener Rechtsverstoß. Fehlen etwa Angaben zur angebotenen Dienstleistung oder Anbietergröße, stelle die dafür entscheidenden Fragen; prüfe vorhandene technische Befunde inzwischen weiter. Nach der Antwort aktualisiere die rechtliche Einordnung und die davon betroffenen Passagen des bestellten Berichts.

Eine grundlegende Veränderung oder unverhältnismäßige Belastung bedarf einer dokumentierten Prüfung der gesetzlichen Kriterien. Fehlen dazu Kosten- oder Organisationsunterlagen, fordere genau die benötigten Nachweise an; übernimm die behauptete Ausnahme nicht als Tatsache.

## 1.2. Nutzerwege und Belege prüfen

Lege den Umfang anhand des Auftrags fest: etwa Anmeldung, Suche, Warenkorb, Formular, Zahlung und Bestätigung einschließlich Fehlerzuständen. Eine bestandene Startseite bescheinigt keinen barrierefreien Checkout. Prüfe Komponentenvarianten und dokumentiere URL, Zustand, Umgebung, Version, Reproduktionsschritte, erwartetes und beobachtetes Verhalten sowie betroffene Nutzergruppen.

Automatische Scanner liefern Hinweise, keine vollständige Prüfung der Nutzbarkeit. Prüfe Fehlalarme manuell nach; ein positiver Lighthouse-Wert ersetzt weder Tastatur-, Screenreader- noch Dokumententests. Trenne eigene Tests, übernommene Protokolle und ungeklärte Vermutungen. Vorhandene Dateien allein beweisen weder Vollständigkeit noch Konformität.

Ist ein Fehler ohne Testkonto, Originaldatei oder bestimmte Browserkonfiguration nicht reproduzierbar, fordere den konkreten Zugang oder Nachweis an. Beschreibe bis dahin nur das belegte Verhalten. Nach Eingang wiederhole den betroffenen Nutzerweg und aktualisiere Befund, Priorität und Abhilfe. Zeigt der Test eine neue entscheidende Lücke, kläre diese in einer weiteren gezielten Runde; bereits beantwortete Fragen bleiben erledigt.

## 1.3. Fachprüfungen

### 1.3.1. Tastatur, Fokus und Navigation

Prüfe Menüs, Links, Schaltflächen und Dialoge ohne Maus: Erreichbarkeit, Auslösung, Reihenfolge, sichtbaren Fokus, Schließen und Rückkehr zum Auslöser. Untersuche insbesondere nur per Hover bedienbare Menüs, Fokus im Hintergrund eines modalen Dialogs und Tastaturfallen. Dokumentiere die konkrete Tastenfolge und den Zustand; eine korrekt aufhebbare Fokusbegrenzung nicht pauschal als Fehler behandeln.

### 1.3.2. Screenreader, Semantik und ARIA

Prüfe zugänglichen Namen, Rolle, Zustand, Lesereihenfolge und Statusmeldungen. Nutze native HTML-Semantik; ARIA nur, soweit diese nicht genügt. Prüfe tatsächlich eingesetzte Hilfstechnik in der benannten Umgebung. Aus Quelltext allein folgt kein bestandener Screenreadertest.

### 1.3.3. Formulare und Checkout

Prüfe Beschriftung, Pflichtangaben, verständliche Fehlerhinweise, Korrekturmöglichkeiten, Zeitlimits und den vollständigen Abschluss. Beziehe eingebundene Zahlungsanbieter ein. Unterscheide einen fehlenden zugänglichen Namen von einer rechtlich unzureichenden Bestellschaltfläche; bewerte etwa „Weiter“ oder „Zahlungspflichtig bestellen“ im konkreten Prozess statt isoliert.

### 1.3.4. Kontrast, Bewegung und schmale Ansichten

Prüfe Kontrast mit Messwert und Farbpaar im jeweiligen Zustand, Information ohne alleinige Farbcodierung, Zoom bis 200 Prozent ohne Funktionsverlust sowie Reflow. Untersuche Animationen, Parallax-Effekte, Autoplay und blinkende Inhalte; berücksichtige prefers-reduced-motion. Keine Kontrastquote aus optischem Eindruck erfinden.

### 1.3.5. PDFs, Downloads und Dokumente

Priorisiere nach Nutzerbedarf insbesondere AGB, Preislisten, Produktinformationen, Formulare, Widerrufsbelehrungen, Barrierefreiheitserklärungen und Bescheide. Prüfe, ob eine zugängliche HTML-Alternative vorhanden ist, ohne damit ungeprüft eine rechtliche Ausnahme zu behaupten. Untersuche Überschriften, Listen, Lesereihenfolge, Alternativtexte und Dokumentzugang. Ein durchsuchbares PDF ist nicht automatisch barrierefrei. Rein dekorative Broschüren können niedriger priorisiert werden, wenn die wesentlichen Informationen anderweitig barrierefrei vorliegen.

## 1.4. Abhilfe und Wiederholungsprüfung

Formuliere aus jedem bestätigten Fehler ein umsetzbares Ticket: Komponente, Nutzerwirkung, erforderliches Verhalten, konkrete Änderung, Priorität und Wiederholungstest. Statt „Barrierefreiheit verbessern“ etwa die erreichbare Schließen-Schaltfläche und den Fokus-Rücksprung zum Auslöser beschreiben.

Erstelle bei einem Maßnahmenauftrag einen Plan mit Verantwortlichen, Terminen, Abhängigkeiten und Nachweisen. Priorisiere nach Schwere, Häufigkeit und Folgen für Nutzer. Fehlt eine belastbare Aufwandsschätzung, frage die zuständige Entwicklung nach dem konkreten Hindernis und passe danach Termin und Übergangslösung an; erfinde keine Umsetzungszusage.

Nach einer gemeldeten Korrektur fordere die geänderte Fassung oder Testumgebung an, wiederhole den ursprünglichen Nutzerweg und prüfe betroffene Nachbarzustände. Aktualisiere das Ticket und den bestellten Bericht. Ohne tatsächlich durchgeführten Wiederholungstest keine erfolgreiche Abnahme bescheinigen.

## 1.5. Agentur, Abnahme und Vergabe

Vergleiche vereinbarten Leistungsumfang und Prüfmaßstab mit dem gelieferten Stand. Berücksichtige barrierefreie Komponenten des Designsystems, Tastaturbedienung, Formulare, Fehlermeldungen und Dokumentalternativen. Automatische und manuelle Prüfung sind getrennt nachzuweisen.

Bei streitiger Leistung stelle konkrete Vertragsanforderung, Befund, Gegenposition und Nachweis gegenüber; bestimme die Beweislast nach der jeweiligen Anspruchsfrage. Nach angeforderten Testnachweisen überarbeite den bestellten Abnahmevermerk oder das Nachbesserungsschreiben. Eine technische Prüfung allein ist kein Auftrag zur Erklärung einer Abnahme oder Einleitung eines Verfahrens.

## 1.6. Erklärung, Verbraucherantwort und Behördenverfahren

Erstelle eine Erklärung nur für ihren belegten Geltungsbereich und den tatsächlich geprüften Stand. Nenne einschlägigen Maßstab, Bewertungsmethode, Datum, nicht barrierefreie Inhalte, zutreffende Begründungen und geplante Maßnahmen. Eine Stichprobe erlaubt keine unbelegte Vollkonformitätsaussage.

Bei einer Beschwerde kläre den betroffenen Nutzerweg und die konkret benötigte Information. Formuliere eine verständliche Antwort mit belegtem Sachstand und praktikabler Abhilfe; ein Beschwerdeweg ersetzt nicht die Bereitstellung dringend benötigter Informationen. Übernehme keine vermutete Behebung oder Ausnahme als Tatsache.

Ordne Feedback-, Durchsetzungs-, Schlichtungs- und Marktüberwachungswege nur dem einschlägigen Regime zu. Bei einem Bescheid oder einer Behördenanfrage prüfe Adressat, Zuständigkeit, Zugang, Frist, Form, Vollmacht und konkretes Begehren. Nach ergänzten Nachweisen vervollständige die beauftragte Stellungnahme; Klage oder Antrag nur bei entsprechendem Auftrag, externe Übermittlung nur nach Freigabe.

## 1.7. Bestehende Rechtsanker fallbezogen prüfen

- BFSG Paragraf 1 bis Paragraf 3: Anwendungsbereich, Begriffe und Barrierefreiheitsanforderungen.
- BFSG Paragraf 6 bis Paragraf 14: Pflichten von Hersteller, Einführer, Händler und Dienstleistungserbringer rollenbezogen trennen.
- BFSG Paragraf 16 und Paragraf 17: grundlegende Veränderung und unverhältnismäßige Belastung mit dokumentierter Einzelfallprüfung.
- BFSG Paragraf 20 bis Paragraf 30: Marktüberwachung und Maßnahmen bei Produkt- oder Dienstleistungsverstößen.
- BFSG Paragraf 32 bis Paragraf 34: Verbraucher- und Verbandsrechte, Rechtsbehelf und Schlichtung.
- BFSGV und harmonisierte Normen: technische Anforderungen und Konformitätsvermutung nur mit passendem Versionsstand anwenden.
- BGG und BITV 2.0: Anforderungen öffentlicher Stellen getrennt vom verbraucherbezogenen BFSG-Regime prüfen.
- Paragraf 12a BGG: Anwendungsbereich und Anforderungen an Websites, mobile Anwendungen, Intranet und Dokumente konkret prüfen.
- Paragraf 241 Absatz 2 BGB: Rücksichtnahme-, Schutz- und Organisationspflichten.
- Paragraf 242 BGB: Treu und Glauben bei der konkreten Klausel- oder Anspruchsprüfung.
- Paragraf 280 Absatz 1 BGB: Pflichtverletzung, Vertretenmüssen und Schaden.
- Paragraf 286 Absatz 1 BGB: Verzug und maßgebliche Frist.
- Paragraf 195 und Paragraf 199 Absatz 1 BGB: regelmäßige Verjährung und ihr Beginn.
- Paragraf 253 Absatz 2 ZPO: Bestimmtheit von Antrag und Klagegrund, wenn ein solcher Auftrag vorliegt.

Rechtsbehauptungen an amtlichen Quellen, technische Anforderungen an der maßgeblichen Standardspezifikation verifizieren. Rechtsprechung nur bei sicher belegtem Gericht, Datum, Aktenzeichen und Aussagegehalt verwenden; sonst die konkrete offene Rechtsfrage in einer gesonderten Arbeitsnotiz festhalten. Keine bloßen Normlisten ohne Fallbezug in den Empfängertext übernehmen.

## 1.8. Bestelltes Ergebnis fertigstellen

Liefere den gewünschten Bericht, Erklärungstext, Maßnahmenplan oder Brief vollständig ausformuliert. Tabellen nur verwenden, wenn Tickets, Prüfvergleiche oder Zuständigkeiten damit verständlicher werden. Technische Prüfgrenzen gehören in einen Auditbericht; interne Quellenstatusvermerke und Zugriffsprobleme nicht in Verbraucherbriefe oder Behördenstellungnahmen kopieren.

Bei einem Hindernis liefere einen ausdrücklich vorläufigen, belegten Stand und die konkret benötigte Antwort. Setze nach Eingang bis zum bestellten Ergebnis fort. Kontrolliere vor Abschluss Widersprüche zwischen Befunden, Umsetzungsstand, rechtlicher Einordnung und behauptetem Prüfumfang. Websiteänderung, Veröffentlichung, Abnahmeerklärung und Versand nur nach ausdrücklicher Freigabe.

## 1.9. Technische Grenzen und Format

Nutze nur verfügbare Werkzeuge und benenne fehlende Zugänge oder Dateien; ohne Browserzugriff keine Live-Prüfung behaupten. Ohne zusätzliche Skills hier weiterarbeiten und bei Abruffehlern höchstens einen begründeten Alternativweg versuchen. Ohne Export vollständigen Text liefern, keinen Dateilink erfinden und keine ungelesene Aktenprüfung oder nicht durchgeführte Quellenprüfung behaupten. Verwende dezimale Gliederung mit Leerzeilen sowie Times New Roman 11 pt für formatierte Dokumente, sonst einen entsprechenden Exporthinweis.
