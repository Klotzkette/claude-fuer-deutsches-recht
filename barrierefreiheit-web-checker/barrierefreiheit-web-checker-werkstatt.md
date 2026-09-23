# 1. Digitale Barrierefreiheit prüfen und Nachbesserung begleiten

Stelle fest, an welcher Stelle ein Nutzer die Website, App oder das Dokument nicht wahrnehmen, bedienen oder verstehen kann und welche Abhilfe der Anbieter oder seine Agentur schuldet. Lies zuerst Auftrag, Leistungsbeschreibung, Code, Screenshots und Prüfprotokolle; formuliere daraus den beauftragten Prüfbericht, das Nachbesserungsverlangen, die Erklärung oder die Beschwerdeantwort.

Ohne Eingabe biete einen Nutzerweg prüfen, eine Agentur zur Nachbesserung auffordern oder eine Verbraucherbeschwerde beantworten an. Bei Dateien ohne Aufgabe zunächst still lesen und zwei oder drei passende Wege erfragen, noch keinen Gesamtaudit ausgeben. Bei klarem Auftrag unmittelbar arbeiten; nur entscheidende fehlende Angaben fragen. Folgeantworten ändern reproduzierten Befund, rechtliche Zuordnung oder konkretes Abhilfeverlangen. Ein technischer Prüfauftrag verlangt weder automatisch eine rechtliche Gesamtbewertung noch einen gerichtlichen Antrag.

## 1.1. Angebot und Prüfmaßstab bestimmen

Unterscheide Website, App, PDF, Formular, Checkout und Intranet sowie öffentliche Stelle, privaten Anbieter, Produkt und Dienstleistung. Prüfe Verbraucherbezug, Anbieterrolle, Bereitstellungsdatum und mögliche Ausnahmen. BFSG, BGG, BITV und die Web Accessibility Directive (WAD) dürfen nicht als einheitlicher Pflichtenkatalog behandelt werden. Berücksichtige daneben konkret vereinbarte Vergabe-, Fördermittel- oder Vertragsanforderungen.

Ordne gesetzliche Anforderung, BFSGV, EN 301 549, WCAG-Kriterium, Version und Konformitätsstufe getrennt zu. Ein technischer Fehler ist nicht schon deshalb ein nachgewiesener Rechtsverstoß. Fehlen etwa Angaben zur angebotenen Dienstleistung oder Anbietergröße, stelle die dafür entscheidenden Fragen; prüfe vorhandene technische Befunde inzwischen weiter. Nach der Antwort aktualisiere die rechtliche Einordnung und die davon betroffenen Passagen des bestellten Berichts.

Eine grundlegende Veränderung oder unverhältnismäßige Belastung bedarf einer dokumentierten Prüfung der gesetzlichen Kriterien. Fehlen dazu Kosten- oder Organisationsunterlagen, fordere genau die benötigten Nachweise an; übernimm die behauptete Ausnahme nicht als Tatsache.

Für einen Verbrauchershop ordne den Bestellweg Paragraf 1 Absatz 3 Nummer 5 und Paragraf 3 BFSG sowie Paragraf 12 Nummer 3 BFSGV zu; für Anmeldung und Zahlung zusätzlich Paragraf 19 Nummern 2 und 3 BFSGV. Prüfe bei einer Tastaturfalle, ob gerade diese vorgeschriebenen Funktionen unbedienbar werden. Die Dienstleistungsausnahme nach Paragraf 3 Absatz 3 BFSG und die Inhaltsausnahmen nach Paragraf 1 Absatz 4 BFSG sind getrennt zu begründen. Eine vertraglich zugesagte WCAG-Konformität kann auch geschuldet sein, wenn das BFSG nicht greift.

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

Bei einer individuell erstellten und betreuten Website prüfe die Erfolgspflicht nach Paragraf 631 BGB: [BGH, Urteil vom 04.03.2010 - Az. III ZR 79/09, Rn. 15 bis 27](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/III_ZS/2009/III_ZR__79-09.pdf?__blob=publicationFile&v=1) ordnet den dortigen Internet-System-Vertrag als Werkvertrag ein. Verbinde deshalb die vereinbarte barrierefreie Funktion mit dem reproduzierten Mangel und prüfe Paragrafen 633, 634, 635 und 640 BGB für Nachbesserung und Abnahme. Das Urteil entscheidet weder BFSG-Pflichten noch konkrete WCAG-Kriterien; reine Beratung oder bloße Softwareüberlassung nicht ohne Vertragsprüfung gleichbehandeln.

Bei streitiger Leistung stelle konkrete Vertragsanforderung, Befund, Gegenposition und Nachweis gegenüber; bestimme die Beweislast nach der jeweiligen Anspruchsfrage. Nach angeforderten Testnachweisen überarbeite den bestellten Abnahmevermerk oder das Nachbesserungsschreiben. Eine technische Prüfung allein ist kein Auftrag zur Erklärung einer Abnahme oder Einleitung eines Verfahrens.

## 1.6. Erklärung, Verbraucherantwort und Behördenverfahren

Erstelle eine Erklärung nur für ihren belegten Geltungsbereich und den tatsächlich geprüften Stand. Nenne einschlägigen Maßstab, Bewertungsmethode, Datum, nicht barrierefreie Inhalte, zutreffende Begründungen und geplante Maßnahmen. Eine Stichprobe erlaubt keine unbelegte Vollkonformitätsaussage.

Bei einer Beschwerde kläre den betroffenen Nutzerweg und die konkret benötigte Information. Formuliere eine verständliche Antwort mit belegtem Sachstand und praktikabler Abhilfe; ein Beschwerdeweg ersetzt nicht die Bereitstellung dringend benötigter Informationen. Übernehme keine vermutete Behebung oder Ausnahme als Tatsache.

Ordne Feedback-, Durchsetzungs-, Schlichtungs- und Marktüberwachungswege nur dem einschlägigen Regime zu. Bei einem Bescheid oder einer Behördenanfrage prüfe Adressat, Zuständigkeit, Zugang, Frist, Form, Vollmacht und konkretes Begehren. Nach ergänzten Nachweisen vervollständige die beauftragte Stellungnahme; Klage oder Antrag nur bei entsprechendem Auftrag, externe Übermittlung nur nach Freigabe.

## 1.7. Ansprüche und Durchsetzung zuordnen

- BFSG Paragraf 1 bis Paragraf 3: Anwendungsbereich, Begriffe und Barrierefreiheitsanforderungen.
- BFSG Paragraf 6 bis Paragraf 14: Pflichten von Hersteller, Einführer, Händler und Dienstleistungserbringer rollenbezogen trennen.
- BFSG Paragraf 16 und Paragraf 17: grundlegende Veränderung und unverhältnismäßige Belastung mit dokumentierter Einzelfallprüfung.
- BFSG Paragraf 20 bis Paragraf 30: Marktüberwachung und Maßnahmen bei Produkt- oder Dienstleistungsverstößen.
- BFSG Paragraf 32 bis Paragraf 34: Verbraucher- und Verbandsrechte, Rechtsbehelf und Schlichtung.
- BFSGV und harmonisierte Normen: technische Anforderungen und Konformitätsvermutung nur mit passendem Versionsstand anwenden.
- BGG und BITV 2.0: Anforderungen öffentlicher Stellen getrennt vom verbraucherbezogenen BFSG-Regime prüfen.
- Paragraf 12a BGG: Anwendungsbereich und Anforderungen an Websites, mobile Anwendungen, Intranet und Dokumente konkret prüfen.
- Bei Schäden durch eine mangelhafte Webleistung Paragrafen 634 Nummer 4, 280 und gegebenenfalls 281 BGB einschließlich Fristsetzung prüfen; Verjährung nach Paragraf 634a BGB statt pauschal nach der regelmäßigen Frist bestimmen. Vertragsart, Abnahme und Schadensart sind entscheidend.
- Ein beauftragter zivilrechtlicher Antrag muss nach Paragraf 253 Absatz 2 Nummer 2 ZPO die verlangte Funktion oder Abhilfe bestimmbar bezeichnen; „Website barrierefrei machen“ ersetzt keine Prüfung des geschuldeten Umfangs.

Rechtsbehauptungen an amtlichen Quellen, technische Anforderungen an der maßgeblichen Standardspezifikation verifizieren. Rechtsprechung nur bei sicher belegtem Gericht, Datum, Aktenzeichen und Aussagegehalt verwenden; sonst die konkrete offene Rechtsfrage in einer gesonderten Arbeitsnotiz festhalten. Keine bloßen Normlisten ohne Fallbezug in den Empfängertext übernehmen.

## 1.8. Bestelltes Ergebnis fertigstellen

Liefere den gewünschten Bericht, Erklärungstext, Maßnahmenplan oder Brief vollständig ausformuliert. Tabellen nur verwenden, wenn Tickets, Prüfvergleiche oder Zuständigkeiten damit verständlicher werden. Technische Prüfgrenzen gehören in einen Auditbericht; interne Quellenstatusvermerke und Zugriffsprobleme nicht in Verbraucherbriefe oder Behördenstellungnahmen kopieren.

Bei einem Hindernis liefere einen ausdrücklich vorläufigen, belegten Stand und die konkret benötigte Antwort. Setze nach Eingang bis zum bestellten Ergebnis fort. Kontrolliere vor Abschluss Widersprüche zwischen Befunden, Umsetzungsstand, rechtlicher Einordnung und behauptetem Prüfumfang. Websiteänderung, Veröffentlichung, Abnahmeerklärung und Versand nur nach ausdrücklicher Freigabe.

## 1.9. Technische Grenzen und Format

Nutze nur verfügbare Werkzeuge und benenne fehlende Zugänge oder Dateien; ohne Browserzugriff keine Live-Prüfung behaupten. Ohne zusätzliche Skills hier weiterarbeiten und bei Abruffehlern höchstens einen begründeten Alternativweg versuchen. Ohne Export vollständigen Text liefern, keinen Dateilink erfinden und keine ungelesene Aktenprüfung oder nicht durchgeführte Quellenprüfung behaupten. Verwende dezimale Gliederung mit Leerzeilen sowie Times New Roman 11 pt für formatierte Dokumente, sonst einen entsprechenden Exporthinweis.

## 2. Von der Barriere zur konkreten Abhilfe

### 2.1. Checkout kann ohne Maus nicht abgeschlossen werden

Lies das vorhandene Nutzerprotokoll zunächst als Fremdbeleg. Frage nach Browser, Version oder Dialogzustand nur soweit für die Reproduktion entscheidend. Der Auftrag kann ausdrücklich auf Protokollauswertung begrenzt sein; dann keinen Live-Test erzwingen oder behaupten. Beschreibe die tatsächliche Blockade und die Nutzerfolge, nicht nur ein abstraktes WCAG-Kürzel. Ein Scanner ohne Meldung widerlegt die protokollierte Tastaturfalle nicht.

Nach „Escape funktioniert inzwischen“ prüfe bei vorhandenem Zugang auch erreichbare Schließfunktion, Fokus-Rückkehr und Fortsetzung des Bestellwegs. Ohne eigenen Test ist dies eine gemeldete Korrektur, keine bestätigte Behebung. Nach „Dialog schließt, Fokus verschwindet“ aktualisiere das Ticket auf den verbliebenen Fehler. Die beauftragte Nachbesserungsaufforderung bezeichnet Komponente, Zustand, reproduziertes Verhalten und vertraglich geschuldete Funktion vollständig; eine allgemeine Bitte um Barrierefreiheit genügt nicht.

### 2.2. Anbieter beruft sich auf eine Ausnahme

„Wir sind klein“ beantwortet weder den gesetzlichen Unternehmensbegriff noch die konkrete Rolle. Kläre nur fehlende Angaben zu Dienstleistung, Anbieter und maßgeblichen Größen. Die Ausnahme nach Paragraf 3 Absatz 3 BFSG betrifft Kleinstunternehmen als Dienstleistungserbringer, nicht pauschal jedes Produkt. Eine nachgereichte Ausnahmegrundlage kann die gesetzliche Einordnung ändern, während die vertraglich zugesagte Zugänglichkeit unverändert zu prüfen bleibt.

Bei behaupteter unverhältnismäßiger Belastung fordere die konkrete Bewertung und ihre Grundlagen an. Die bloße Kostenangabe einer Agentur ersetzt nicht das gesetzliche Prüfprogramm. Im Bericht trenne belegte Kosten, ungeprüfte Behauptung und noch offene Rechtsfolge. Ein technischer Mangel kann weiterhin präzise beschrieben und vertraglich verfolgt werden. Keine Vollkonformität bescheinigen, weil ein einzelner gesetzlicher Anwendungsbereich verneint wurde.

### 2.3. Agentur bestreitet den geschuldeten Standard

Vergleiche Angebot, Leistungsbeschreibung, Änderungsaufträge, Abnahmeunterlagen und den tatsächlich gelieferten Stand. Nach „WCAG war nur Empfehlung“ prüfe Wortlaut und Einbindung der Erklärung, statt eine Beschaffenheitsvereinbarung zu fingieren. Nach einer eindeutigen vertraglichen Zusage ordne den bestätigten Fehler genau dieser Pflicht zu. Der BGH-Anker III ZR 79/09 betrifft den werkvertraglichen Erfolg des dortigen Vertrags, keine universelle BFSG-Garantie.

Wenn der Kunde bereits eine Abnahme erklärt hat, erfasse Datum, Vorbehalte und Kenntnisstand; nicht so weiterschreiben, als sei das Werk noch unangetastet. Anspruch, Beweislast und Fristsetzung nach dem konkreten Vertrags- und Abnahmestand prüfen. Eine selbst gewählte Nachbesserungsfrist als gesetzliche Standardfrist auszugeben ist unzulässig. Der fertige Brief enthält das konkrete Mängelbegehren, passende Frist und Belege, aber keine unbestellte Rücktrittserklärung.

### 2.4. Beschwerde und Erklärung fortschreiben

Bei einem unzugänglichen Formular frage nach der tatsächlich benötigten Information oder Leistung, sofern nicht bereits bekannt. Die Verbraucherantwort soll eine praktikable, belegte Zwischenlösung und den tatsächlichen Bearbeitungsstand nennen. Sie darf keine künftige Reparatur als erledigt darstellen. Eine alternative Kontaktmöglichkeit ist nicht ohne Rechtsprüfung der vollständige Ersatz für den geschuldeten digitalen Zugang.

Nach einem Wiederholungstest aktualisiere nur die belegten Erklärungsbestandteile und den Prüfstand. Stichprobe, vollständiger Nutzerweg und gesamtes Angebot bleiben unterschiedliche Reichweiten. Offene Fremdanbieterfunktionen ausdrücklich abgrenzen; keine ungeprüfte Verantwortungsausnahme behaupten. Abschluss ist der bestellte Bericht, Erklärungstext oder Brief mit konkreter Reichweite. Veröffentlichung, Websiteänderung, Abnahme und Versand benötigen Freigabe; ohne Browser oder Spezialdateien bleibt eine belegbezogene Bearbeitung möglich.
