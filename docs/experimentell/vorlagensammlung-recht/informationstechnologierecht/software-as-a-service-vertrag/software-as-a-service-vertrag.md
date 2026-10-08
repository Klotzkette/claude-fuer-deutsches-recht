# Software-as-a-Service-Vertrag (B2B; SLA)

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Vertragseingang und Bearbeitungsstand

Anbieterin ist [vollständige Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Kundin ist [vollständige Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

SaaS-Dienst ist [Produktname, Modul, Mandant, Vertragsgebiet, Produktivstart].

Der Bearbeitungsstand ist [Entwurf / Verhandlung / Unterzeichnung / Vollzug], Datum: [Datum], Akte: [Az.].

### 1. Präambel / Gegenstand

1.1 Die Anbieterin stellt der Kundin den in Anlage 1 beschriebenen cloudbasierten SaaS-Dienst zur Nutzung über das Internet bereit. Der Dienst umfasst Anwendung, Mandantenverwaltung, Schnittstellen, Hosting, Datenspeicherung, Updates, Support und Exit-Leistungen nach diesem Vertrag.

1.2 Die Kundin nutzt den SaaS-Dienst ausschließlich für eigene geschäftliche Zwecke und für die in Anlage 1 bezeichneten Nutzergruppen, Mandanten, verbundenen Unternehmen und Schnittstellen. Eine lokale Installation des Dienstes, eine Quellcodeüberlassung und Individualentwicklung sind nicht geschuldet.

### 2. Nutzungsrechte, Nutzerkreis und verbotene Nutzung

2.1 Die Anbieterin räumt der Kundin für die Vertragslaufzeit ein einfaches, nicht übertragbares und nicht unterlizenzierbares Recht ein, den SaaS-Dienst im vereinbarten Nutzerkreis zu verwenden.

2.2 Berechtigte Nutzung besteht für [Named User mit Anzahl / Concurrent User mit Anzahl / verbundene Unternehmen nach konkreter Liste / externe Auftragnehmer nach Freigabe]. Nutzerkonten dürfen nicht geteilt werden; technische Servicekonten sind in Anlage 1 gesondert zu bezeichnen.

2.3 Die Kundin darf den Dienst nicht an Dritte vermieten, als eigenes Plattformangebot weiterverkaufen, Sicherheitsmechanismen umgehen, Lasttests ohne Freigabe durchführen, Schadcode einbringen oder Schnittstellen außerhalb der dokumentierten API verwenden.

### 3. Bereitstellung, Verfügbarkeit und Service Credits

3.1 Die Anbieterin stellt den Dienst ab [Produktivstart] am Übergabepunkt [Rechenzentrumsausgang / API-Endpunkt / Mandanten-URL] bereit. Die monatliche Mindestverfügbarkeit beträgt [Prozentwert] Prozent im Kalendermonat.

3.2 Nicht als Nichtverfügbarkeit zählen angekündigte Wartungsfenster, von der Kundin verursachte Fehlkonfigurationen, Ausfälle kundenseitiger Netze, höhere Gewalt, gesperrte Nutzerkonten wegen Missbrauchs und Ausfälle von Drittkomponenten, soweit die Anbieterin diese nicht beherrscht.

3.3 Die Anbieterin misst Verfügbarkeit, Antwortzeit, Fehlerquote und Ausfallzeit automatisiert und stellt der Kundin monatlich einen SLA-Bericht bereit. Messrohdaten werden [Anzahl] Monate aufbewahrt.

3.4 Service Credits werden wie folgt berechnet: Bei Unterschreitung der Mindestverfügbarkeit um bis zu [Prozentpunkte] erhält die Kundin [Prozentsatz] der Monatsgebühr als Gutschrift; bei Unterschreitung um mehr als [Prozentpunkte] erhält sie [Prozentsatz] der Monatsgebühr. Service Credits werden auf weitergehende gesetzliche Ansprüche angerechnet, schließen diese aber nicht aus, soweit ein Ausschluss AGB-rechtlich nicht wirksam vereinbart werden kann.

### 4. Support, Störungsklassen und Sicherheit

4.1 Die Kundin meldet Störungen über [Portal / E-Mail / Hotline] mit Nutzerkonto, Zeitpunkt, Mandant, betroffener Funktion, Fehlermeldung, Reproduktionsschritten und Geschäftsauswirkung.

4.2 Kritische Störungen liegen vor, wenn der Dienst insgesamt nicht nutzbar ist, Datenverlust droht, Sicherheitsfunktionen ausfallen oder produktionskritische Kernprozesse vollständig stehen. Die Anbieterin reagiert binnen [Stunden] und arbeitet bis zur Wiederherstellung mit angemessener Priorität fort.

4.3 Schwere Störungen liegen vor, wenn wesentliche Funktionen erheblich beeinträchtigt sind und kein zumutbarer Workaround besteht. Die Anbieterin reagiert binnen [Stunden] und stellt binnen [Werktage] einen Workaround oder eine Korrektur bereit.

4.4 Normale Störungen und Bedienfragen werden binnen [Werktage] qualifiziert beantwortet und nach Produktplanung, Sicherheitserfordernis und Schweregrad behoben.

4.5 Sicherheitsvorfälle werden unverzüglich an die in Anlage 2 benannten Kontakte gemeldet. Die Meldung enthält bekannte Tatsachen, betroffene Systeme, betroffene Datenkategorien, erste Eindämmungsmaßnahmen, weiteren Zeitplan und Ansprechpartner.

### 5. Änderungen, Updates und Schnittstellen

5.1 Die Anbieterin darf den Dienst fortentwickeln, Patches einspielen, Sicherheitsupdates ausrollen und technische Infrastruktur ändern, sofern Kernfunktionen, Datenzugriff, Schnittstellen und vereinbarte Service Level nicht wesentlich verschlechtert werden.

5.2 Wesentliche Funktionsänderungen, API-Änderungen, Datenmodelländerungen und Abschaltungen werden mit einer Vorlaufzeit von [Anzahl] Kalendertagen angekündigt. Die Anbieterin stellt Migrationshinweise, Testumgebung oder Übergangs-API bereit, soweit die Änderung produktive Prozesse der Kundin betrifft.

5.3 Dokumentierte Schnittstellen, Webhooks, Exportformate und Rate Limits sind in Anlage 3 festgelegt. Nicht dokumentierte Schnittstellen dürfen nicht für produktive Integrationen verwendet werden.

### 6. Datenschutz, Unterauftragnehmer und Datenlokation

6.1 Verarbeitet die Anbieterin personenbezogene Daten der Kundin oder ihrer Nutzerinnen und Nutzer, handeln die Parteien nach dem Auftragsverarbeitungsvertrag in Anlage 2. Der SaaS-Dienst darf erst produktiv genutzt werden, wenn Anlage 2 unterzeichnet oder in sonst zulässiger Form abgeschlossen ist.

6.2 Unterauftragnehmer für Hosting, Monitoring, Support, E-Mail-Versand, Ticketing, Logging, Backup oder Content Delivery sind in Anlage 2 mit Sitz, Leistungsgegenstand, Speicherort und Drittlandbezug zu benennen. Neue Unterauftragnehmer werden nach dem in Anlage 2 geregelten Widerspruchsverfahren eingebunden.

6.3 Kundendaten werden in [EWR / konkret bezeichnetes Land / konkret bezeichnete Rechenzentrumsregion] verarbeitet. Drittlandtransfers erfolgen nur nach Anlage 2 und nur mit geeigneten Garantien nach Art. 44 ff. DSGVO.

### 7. Vergütung, Abrechnung und Preisänderung

7.1 Die Kundin zahlt die in Anlage 4 vereinbarte Grundgebühr, Nutzergebühr, Mandantengebühr, Transaktionsgebühr, Speichergebühr und Supportgebühr zuzüglich gesetzlicher Umsatzsteuer.

7.2 Die Abrechnung erfolgt [monatlich nachträglich / jährlich im Voraus / gemischt nach Anlage 4]. Rechnungen sind binnen [Anzahl] Kalendertagen nach Zugang zahlbar.

7.3 Preisänderungen sind frühestens nach Ablauf von [Anzahl] Monaten zulässig und müssen der Kundin [Anzahl] Monate vor Wirksamwerden in Textform mitgeteilt werden. Übersteigt die Erhöhung [Prozentsatz] Prozent innerhalb von zwölf Monaten, darf die Kundin zum Wirksamwerden der Erhöhung außerordentlich kündigen.

### 8. Laufzeit, Kündigung und Exit

8.1 Der Vertrag beginnt am [Datum] und hat eine Mindestlaufzeit von [Anzahl] Monaten. Er verlängert sich jeweils um [Anzahl] Monate, wenn er nicht mit einer Frist von [Anzahl] Monaten zum Laufzeitende in Textform gekündigt wird.

8.2 Das Recht zur Kündigung aus wichtigem Grund bleibt unberührt. Ein wichtiger Grund liegt für die Kundin insbesondere vor, wenn kritische Störungen wiederholt auftreten, die Anbieterin Datenschutzpflichten schwer verletzt, die vereinbarte Mindestverfügbarkeit nachhaltig unterschreitet oder ein geschäftskritischer Export dauerhaft verweigert wird.

8.3 Die Anbieterin stellt der Kundin bei Vertragsende einen vollständigen Export der Kundendaten in den Formaten [CSV / JSON / XML / anderes Format] bereit. Der Export umfasst Stammdaten, Bewegungsdaten, Anhänge, Konfigurationen, Nutzerrollen, Audit-Logs und Metadaten, soweit diese Daten im Dienst verarbeitet werden.

8.4 Soweit der Dienst in den Anwendungsbereich der Verordnung (EU) 2023/2854 (Data Act) fällt, unterstützt die Anbieterin den Wechsel zu einem anderen Datenverarbeitungsdienst oder in eine eigene Infrastruktur nach den dort anwendbaren Wechsel- und Interoperabilitätsvorgaben.

8.5 Nach bestätigtem Export löscht die Anbieterin Kundendaten nach Anlage 2, soweit keine gesetzlichen Aufbewahrungspflichten bestehen. Backups werden nach dem regulären Backup-Zyklus überschrieben; die maximale Restlaufzeit beträgt [Anzahl] Tage.

### 9. Haftung und Vertraulichkeit

9.1 Die Anbieterin haftet unbeschränkt für Vorsatz, grobe Fahrlässigkeit, Verletzung von Leben, Körper oder Gesundheit, ausdrücklich übernommene Garantien und zwingende gesetzliche Haftung.

9.2 Bei einfacher Fahrlässigkeit haftet die Anbieterin nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den vertragstypischen, vorhersehbaren Schaden. Die Haftungsobergrenze beträgt [Jahresvergütung / Betrag in EUR] je Schadensfall und [Betrag in EUR] insgesamt je Vertragsjahr, soweit diese Begrenzung wirksam vereinbart werden kann.

9.3 Für Datenverlust haftet die Anbieterin nur in dem Umfang, der auch bei ordnungsgemäßer Export-, Backup- und Notfallorganisation der Kundin entstanden wäre; dies gilt nicht bei Verletzung vereinbarter Backup- oder Sicherheitsleistungen der Anbieterin.

9.4 Die Parteien halten Geschäftsgeheimnisse, Zugangsdaten, Sicherheitskonzepte, Preise, technische Dokumentation und nicht öffentliche Nutzungsdaten vertraulich. Die Pflicht gilt [Anzahl] Jahre über Vertragsende hinaus.

### 10. Schlussbestimmungen

10.1 Änderungen und Ergänzungen bedürfen der Textform, soweit nicht gesetzlich eine strengere Form gilt.

10.2 Es gilt das Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts.

10.3 Gerichtsstand ist [Ort], soweit gesetzlich zulässig.

### Schluss, Unterzeichnung und Freigabe

[Ort], den [Datum]

| Für die Anbieterin | Für die Kundin |
|---|---|
| _____________________________ | _____________________________ |
| [Name, Funktion, Vertretungsrolle] | [Name, Funktion, Vertretungsrolle] |

**Weitere Zustimmung / fachliche Freigabe:** [nicht erforderlich / Datenschutzfreigabe / IT-Sicherheitsfreigabe / Einkaufsfreigabe]

## Anlagen

### Anlage 1 — Leistungsbeschreibung, Nutzerkreis und Mandant

1. Leistungsumfang

1.1 Produktname, Version und Module: [Produktname; Versionsstand; gebuchte Module; optionale Add-ons; Mandantenfähigkeit; produktive URL].

1.2 Kernfunktionen und ausdrücklich ausgeschlossene Funktionen: [fachliche Kernprozesse; Rollen- und Rechtefunktionen; Reporting; ausdrücklich nicht geschuldete Individualentwicklung; nicht enthaltene Integrationen].

1.3 Nutzerkreis, Mandanten, verbundene Unternehmen und externe Nutzer: [Anzahl benannter Nutzer; Rollenprofile; verbundene Unternehmen; externe Dienstleister; Gastzugänge; Administrationsrechte].

2. Technische Voraussetzungen

2.1 Browser, Betriebssysteme, Schnittstellen und Authentifizierung: [freigegebene Browser; mobile Betriebssysteme; Single-Sign-on-Verfahren; Multi-Faktor-Authentifizierung; API-Protokolle].

2.2 Kundenseitige Systeme und Datenquellen: [ERP-System; CRM-System; Identity Provider; Datenquellen; Importformate; kundenseitige Firewall- oder Proxy-Anforderungen].

### Anlage 2 — Auftragsverarbeitung, TOM und Unterauftragnehmer

1. Verarbeitung

1.1 Gegenstand, Dauer, Art und Zweck der Verarbeitung: [Betrieb der SaaS-Anwendung; Support; Hosting; Laufzeit; Zweck der Verarbeitung; Weisungsumfang].

1.2 Kategorien personenbezogener Daten und betroffener Personen: [Stammdaten; Kommunikationsdaten; Nutzungsdaten; Inhaltsdaten; Beschäftigte; Kunden; Lieferanten; Administrationsnutzer].

1.3 Weisungen, TOM, Löschung, Rückgabe, Audit und Unterstützungspflichten: [Weisungskanal; technische und organisatorische Maßnahmen; Löschfrist; Rückgabeformat; Auditverfahren; Melde- und Unterstützungspflichten].

2. Unterauftragnehmer

2.1 Name, Sitz, Leistungsgegenstand, Speicherort und Drittlandbezug: [Unterauftragnehmer; Sitz; Hosting-Region; konkrete Teilleistung; Speicherort; Drittlandtransfer; Absicherungsinstrument].

2.2 Informations- und Widerspruchsverfahren: [Vorabinformation in Textform; Widerspruchsfrist; sachliche Widerspruchsgründe; Ersatzanbieter; Eskalationsweg].

### Anlage 3 — Schnittstellen, API und Exportformate

1. Schnittstellen

1.1 API-Endpunkte, Authentifizierung und Rate Limits: [Endpoint; Methode; Authentifizierungsverfahren; Token-Laufzeit; Rate Limit je Minute; Sperrmechanismus].

1.2 Webhooks, Datenformate und Versionierung: [Webhook-Ereignisse; JSON- oder XML-Schema; Versionsnummer; Deprecation-Frist; Testumgebung].

2. Exit

2.1 Exportumfang, Format, Testexport und Übergabeweg: [Datenkategorien; Dateiformat; Metadaten; Testexporttermin; verschlüsselter Übergabeweg; Prüfsumme].

2.2 Migrationsunterstützung und Stundensätze: [Ansprechpartner; enthaltene Stunden; zusätzliche Stundensätze in EUR; Reaktionszeit; Dokumentationsumfang].

### Anlage 4 — Vergütung und Service Credits

1. Gebühren

1.1 Grundgebühr, Nutzergebühr, Speichergebühr und Transaktionsgebühr: [monatliche Grundgebühr in EUR; Nutzerpreis in EUR; Speicherstaffel; Transaktionspreis; Mindestabnahme].

1.2 Abrechnungsperiode, Fälligkeit und Zahlungsweg: [monatliche oder jährliche Abrechnung; Fälligkeit nach Rechnung in Tagen; SEPA-Lastschrift; Überweisung; Rechnungsadresse].

2. Service Credits

2.1 Mindestverfügbarkeit: [Prozentwert].

2.2 Gutschriftenschwellen und Obergrenze: [Verfügbarkeitskorridor; Gutschrift in Prozent der Monatsgebühr; Ausschluss geplanter Wartung; Jahreshöchstbetrag].

---

Lizenz: Apache-2.0 OR MIT.
