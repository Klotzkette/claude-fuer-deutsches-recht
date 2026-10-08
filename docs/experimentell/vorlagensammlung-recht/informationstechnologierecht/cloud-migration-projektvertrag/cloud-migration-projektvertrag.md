# Cloud-Migration-Projektvertrag

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Cloud-Migration ist Ausfall-, Datenschutz- und Vendor-Lock-in-riskant. Cutover, Rollback, Backups, Zugriffe und Exit müssen testbar geregelt werden.

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Vertragseingang und Bearbeitungsstand

Kundin ist [vollständiger Name oder Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Dienstleisterin ist [vollständiger Name oder Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Weitere Beteiligte / Zustimmungsberechtigte sind [Name, Rolle, Vertretung / keine].

Der Bearbeitungsstand ist [Entwurf / Verhandlung / Unterzeichnung / Vollzug], Datum: [Datum], Akte: [Az.].

## 1. Präambel / Gegenstand

1.1 Die Kundin beauftragt die Dienstleisterin mit der Migration der in Anlage 1 beschriebenen Anwendungen, Datenbestände, Schnittstellen und Betriebsprozesse aus der bestehenden IT-Umgebung in die vereinbarte Cloud-Zielarchitektur.

1.2 Die Parteien vereinbaren Migrationsumfang, Verantwortungsmatrix, Testmigration, Cutover, Rollback, Datensicherung, Zugriffsrechte, Datenschutz, Informationssicherheit, Abnahme und Betriebshandover.

## 2. Vertragsgegenstand und Abgrenzung

2.1 Vertragsgegenstand ist die planmäßige Überführung von [Systeme / Workloads / Datenbanken / Nutzergruppen] in die Cloud-Umgebung [Provider / Region / Tenant] einschließlich Migrationskonzept, Testlauf, Cutover und Übergabe in den Regelbetrieb.

2.2 Nicht geschuldet sind fachliche Neuentwicklung, Prozessberatung außerhalb der Migrationsschnittstellen, Dauerbetrieb nach Betriebshandover, Provider-Verfügbarkeit außerhalb des vereinbarten Service Levels oder Freigaben von Drittanbietern, die die Kundin selbst beibringen muss.

2.3 Migrationskonzept, Systeminventar, Datenmapping, Cutover- und Rollback-Plan, TOM-Matrix, Testprotokolle und Go/No-Go-Freigaben gelten nur in der freigegebenen Fassung. Bei Widersprüchen geht der individuell unterzeichnete Projektvertrag vor.

2.4 Migration und Abnahme erfolgen nach folgenden Regeln:

2.4.1 Scope, Quellsysteme, Zielarchitektur, Datenvolumen, Schnittstellen, Verantwortliche und Mitwirkungspflichten sind in Anlage 1 verbindlich beschrieben.

2.4.2 Testmigration, Fehlerklassen, Cutover-Fenster, Go/No-Go-Entscheidung und Rollback-Szenario werden vor Produktivschaltung in Anlage 2 freigegeben.

2.4.3 Datenschutz, Verschlüsselung, Zugriffskontrolle, Protokollierung, Unterauftragnehmer und Drittlandtransfers richten sich nach Anlage 3.

2.4.4 Abnahme erfolgt nach bestandenem Funktionstest und Datenabgleich; Betriebshandover, Restmängel und Exit-Dokumentation werden in Anlage 4 festgehalten.

## 3. Pflichten: Kundin

3.1 Kundin stellt die in Anlage 1 bezeichneten Unterlagen vollständig, richtig und aktuell bereit.

3.2 Die Kundin informiert die Dienstleisterin unverzüglich in Textform über Änderungen an Quellsystemen, Datenklassen, Schnittstellen, Berechtigungen, Provider-Vorgaben, Wartungsfenstern, Datenschutzfreigaben und jede Störung, die Testmigration, Cutover oder Rückfallplan berührt.

3.3 Die Kundin steht für die Richtigkeit der bereitgestellten System-, Daten- und Berechtigungsinformationen ein. Die Dienstleisterin übernimmt keine Verantwortung für Altlasten, Dateninkonsistenzen oder Provider-Sperren, die vor Projektbeginn bestanden und nicht offengelegt wurden.

3.4 Die Kundin führt eine Migrationsakte, in der Quellsysteme, Zielsysteme, Datenklassen, Schnittstellen, Ausfallfenster, Rollen, Testfälle, Rückfallplan, Freigaben, Datenschutzprüfungen und Restmängel dem jeweiligen Cutover-Schritt zugeordnet werden. Die Migrationsakte ist Anlage 2 zuzuordnen und vor Unterzeichnung freizugeben.

## 4. Pflichten: Dienstleisterin

4.1 Dienstleisterin erstellt den Migrationsplan, führt Testmigration und Cutover nach Anlage 2 durch, dokumentiert Datenabgleich und Fehlerklassen und übergibt den Betrieb erst nach freigegebenem Funktionstest.

4.2 Die Dienstleisterin prüft Datenlandkarte, Schnittstellenbeschreibung, Berechtigungsmatrix, Verschlüsselungsvorgaben, Testdatensatz, Provider-Vorgaben und Cutover-Kalender unverzüglich auf erkennbare Migrationssperren. Beanstandungen, die Datenintegrität, Verfügbarkeit, Datenschutz oder Rückfallfähigkeit berühren, meldet sie binnen [fünf Bankarbeitstagen] in Textform.

4.3 Dienstleisterin darf Unterlagen, Daten und Rechte nur für den Vertragszweck verwenden und nur an Personen weitergeben, die für Prüfung, Vollzug, Finanzierung, Beratung oder Rechtsdurchsetzung erforderlich sind.

4.4 Abnahme, Betriebshandover, Restmängel und Exit-Dokumentation richten sich zusätzlich nach 2.4.4 und Anlage 4.

## 5. Projektvergütung, Change Requests und Abrechnung

5.1 Projektpauschale, Meilensteinvergütung, Stundensätze, Change-Request-Sätze, Provider-Weiterbelastungen, Reise- und Nebenkosten sowie Exit-Dokumentationskosten werden im Vergütungsplan nach Anlage 5 betragsmäßig oder als Berechnungsformel festgelegt und verstehen sich zuzüglich Umsatzsteuer, soweit diese anfällt.

5.2 Meilensteinzahlungen werden nach freigegebenem Testprotokoll, Cutover-Freigabe oder Betriebshandover und Zugang einer prüffähigen Rechnung fällig; Change Requests und Provider-Weiterbelastungen werden nur abgerechnet, wenn sie nach Anlage 5 freigegeben, belegt und dem betroffenen Arbeitspaket zugeordnet sind.

5.3 Gerät eine Partei mit einer fälligen Zahlung in Verzug, gelten §§ 286, 288 BGB, soweit deutsches Recht anwendbar ist; weitergehender konkret nachgewiesener Schaden bleibt vorbehalten.

5.4 Aufrechnung und Zurückbehaltung sind nur mit unbestrittenen, rechtskräftig festgestellten oder aus demselben Vertragsverhältnis entscheidungsreifen Ansprüchen zulässig, soweit AGB-rechtlich wirksam.

## 6. Risiko, Haftung und Leistungsstörungen

6.1 Die Dienstleisterin haftet für von ihr zu vertretende Fehler bei Migrationsplanung, Datenextraktion, Mapping, Verschlüsselung, Cutover, Rollback, Protokollierung, Berechtigungsmigration und Handover-Dokumentation. Die Auftraggeberin haftet für unvollständige Systeminformationen, verspätete Fachfreigaben, fehlerhafte Datenbereinigung, nicht bereitgestellte Testnutzer und produktive Änderungen während eines freigegebenen Cutover-Fensters.

6.2 Haftungsbeschränkungen gelten nicht für Vorsatz, grobe Fahrlässigkeit, Verletzung von Leben, Körper oder Gesundheit, arglistiges Verschweigen, ausdrücklich übernommene Garantien oder zwingende gesetzliche Haftung.

6.3 Migrationsstörungen werden als [kritischer Datenverlust / Cutover-Blocker / fachlicher Mappingfehler / Performanceabweichung / Dokumentationsmangel] klassifiziert. Die Meldung enthält betroffene Datenobjekte, Quell- und Zielsystem, Reproduktionsschritte, Geschäftsauswirkung, Verantwortlichkeit sowie Restore-, Rollback- und Nachtestplan.

6.4 Ein Datenverlust gilt erst als behoben, wenn Datenbestand, Berechtigungen, Metadaten, Stichprobenabgleich und Fachbereichsfreigabe nach Anlage 4 übereinstimmen. Ein bloß technischer Import ohne fachlichen Datenabgleich genügt für den Handover nicht.

## 7. Compliance und Datenschutz

7.1 Vor Datenextraktion und Cutover dokumentieren die Parteien Mandantentrennung, Berechtigungskonzept, Verschlüsselung, Protokollierung, Subdienstleister, Exportkontrolle und Geheimnisschutz. Produktivdaten dürfen nur in freigegebenen Migrationswerkzeugen und Zielregionen verarbeitet werden.

7.2 Soweit die Dienstleisterin personenbezogene Daten im Auftrag verarbeitet, gilt die Vereinbarung nach Art. 28 DSGVO einschließlich Unterauftragnehmer- und Drittlandmodul. Testdaten werden anonymisiert oder minimiert; temporäre Extrakte, Transfer-Buckets und Sicherungskopien werden nach erfolgreichem Handover nachweisbar gelöscht.

## 8. Laufzeit, Beendigung und Rückabwicklung

8.1 Der Projektvertrag beginnt am [Datum] und endet nach erfolgreichem Cutover, fachlicher Abnahme, Ablauf der Hypercare-Phase von [Anzahl] Tagen und Übergabe sämtlicher Betriebs-, Berechtigungs- und Löschungsnachweise.

8.2 Ein wichtiger Kündigungsgrund liegt insbesondere vor, wenn ein kritischer Meilenstein trotz Recovery-Plan endgültig verfehlt wird, Datenintegrität nicht wiederherstellbar ist oder ein schwerwiegender Sicherheitsverstoß fortbesteht. Vor Kündigung eines heilbaren Projektfehlers durchläuft die Abweichung Eskalationsstufen, Fristen und Entscheidungsgremien nach Anlage [Nummer].

8.3 Bei vorzeitigem Projektende erstellt die Dienstleisterin einen exportfähigen Datenstand, übergibt Mapping-, Skript- und Protokolldokumentation, unterstützt Rollback oder Providerwechsel und löscht nicht mehr benötigte Projektkopien. Vergütung und Rechte werden je abgenommenem Arbeitspaket abgerechnet.

## 9. Schlussbestimmungen

9.1 Änderungen und Ergänzungen bedürfen der Textform, soweit nicht gesetzlich strengere Form vorgeschrieben ist. Individualabreden haben Vorrang.

9.2 Es gilt das Recht der Bundesrepublik Deutschland, soweit nicht zwingendes ausländisches Recht, Unionsrecht oder Aufsichtsrecht eingreift.

9.3 Gerichtsstand ist [Ort], soweit gesetzlich zulässig. Zwingende Gerichtsstände, Aufsichtsverfahren und insolvenzrechtliche Zuständigkeiten bleiben unberührt.

9.4 Sollte eine Bestimmung unwirksam sein oder werden, bleibt der Vertrag im Übrigen wirksam. Die Parteien ersetzen die unwirksame Bestimmung durch eine wirksame Regelung, die dem wirtschaftlichen Zweck am nächsten kommt.

### Schluss, Unterzeichnung und Freigabe

[Ort], den [Datum]

| Für Kundin | Für Dienstleisterin |
|---|---|
| _____________________________ | _____________________________ |
| [Name, Funktion, Vertretungsrolle] | [Name, Funktion, Vertretungsrolle] |

## Anlagen

| Anlage | Bezeichnung |
| --- | --- |
| Anlage 1 | Sachverhalts-, Rechte- und Unterlagenverzeichnis |
| Anlage 2 | Vollzugsvoraussetzungen und Prüfmatrix |
| Anlage 3 | Datenschutz-, Sicherheits- und Betriebsübergabematrix |
| Anlage 4 | Abnahme, Betriebshandover und Exit-Dokumentation |
| Anlage 5 | Vergütungsplan, Change Requests und Provider-Weiterbelastungen |

### Anlage 1 — Sachverhalts-, Rechte- und Unterlagenverzeichnis

1. Identifikation

1.1 Akte: [Az.]

1.2 Datum: [JJJJ-MM-TT]

1.3 Beteiligte: [Beteiligte]

1.4 Dokumentenstand: [Entwurf / freigegeben]

2. Unterlagen

2.1 Hauptvertrag oder Term Sheet: [Bezeichnung]

2.2 Systeminventar, Datenobjekte, Mapping, Berechtigungen, Schnittstellen, Providerlizenzen und Cutover-Abhängigkeiten: [Nachweise je Quell- und Zielsystem]

2.3 Auftragsverarbeitung, Drittlandtransfer, Informationssicherheit, Exportkontrolle, Lizenz- und Auslagerungsprüfung: [Prüfstatus je Migrationsstrom]

2.4 Offene Punkte: [Liste]

3. Freigabe

3.1 Fachliche Prüfung: [Name], [Datum]

3.2 Versand- oder Unterzeichnungsfreigabe: [Name], [Datum]

### Anlage 3 — Datenschutz-, Sicherheits- und Betriebsübergabematrix

1. Datenschutzrollen

1.1 Verantwortliche Stelle ist [Name]; Auftragsverarbeiterin ist [Name]; Unterauftragnehmer sind [Liste].

1.2 Verarbeitungszwecke, Datenkategorien, betroffene Personen, Löschfristen und Speicherorte werden je Anwendungssystem dokumentiert.

2. Technische und organisatorische Maßnahmen

2.1 Verschlüsselung, Zugriffskontrolle, Protokollierung, Backup, Wiederherstellung, Schwachstellenmanagement und Administrationsrechte werden systembezogen beschrieben.

2.2 Drittlandtransfers werden nur auf Grundlage einer geprüften Rechtsgrundlage, Transfer Impact Assessment und dokumentierter Zusatzmaßnahmen freigegeben.

2.3 Änderungen an Unterauftragnehmern werden mit Frist, Widerspruchsrecht und Migrationsrisiko dokumentiert.

3. Freigabe

3.1 Datenschutz, Informationssicherheit, Fachbereich und Projektleitung geben die Migration vor Cutover frei: [Namen], [Datum].

3.2 Offene Risiken werden mit Risikoeigner, Abhilfemaßnahme und Frist aufgenommen.

### Anlage 4 — Abnahme, Betriebshandover und Exit-Dokumentation

1. Abnahmetests

1.1 Funktionstests, Datenabgleich, Schnittstellentests, Lasttests, Berechtigungsprüfung und Wiederherstellungstest werden mit Ergebnis, Prüferin und Datum protokolliert.

1.2 Abnahmehindernisse werden nur angenommen, wenn sie produktive Nutzung, Datenintegrität, Sicherheit oder vertraglich vereinbarte Kernprozesse wesentlich beeinträchtigen.

2. Betriebshandover

2.1 Zu übergeben sind Architekturdiagramm, Betriebshandbuch, Monitoring-Konzept, Incident-Prozess, Rollenmodell, Notfallkontakte und Lizenzübersicht.

2.2 Restmängel werden mit Schweregrad, Workaround, Verantwortlichkeit und Erledigungsfrist dokumentiert.

3. Exit

3.1 Exit-Dokumentation umfasst Exportformat, Rückgabefrist, Löschbestätigung, Wechselunterstützung, Kosten und technische Abhängigkeiten.

3.2 Der Exit-Test wird spätestens [Frist] nach Produktivsetzung einmal durchgeführt und dokumentiert.

### Anlage 5 — Vergütungsplan, Change Requests und Provider-Weiterbelastungen

1. Projektvergütung

1.1 Projektpauschale: [Betrag in EUR]. Die Pauschale umfasst [Arbeitspakete] und endet bei [Abgrenzung / ausgeschlossene Leistungen].

1.2 Meilensteinvergütung: [Meilenstein], [Betrag], [Fälligkeitsvoraussetzung], [Abnahmedokument].

1.3 Stundensätze für zusätzlich freigegebene Leistungen: [Rolle], [Satz], [Abrechnungseinheit], [Höchstbudget].

2. Change Requests

2.1 Ein Change Request bezeichnet Änderungswunsch, Ursache, betroffene Systeme, Aufwand, Terminfolge, Datenschutzfolge und Preisfolge.

2.2 Die Dienstleisterin darf Zusatzaufwand erst nach Freigabe in Textform abrechnen; Notfallmaßnahmen zur Abwehr eines produktionskritischen Ausfalls werden nachträglich binnen [Frist] dokumentiert.

3. Provider- und Exit-Kosten

3.1 Provider-Weiterbelastungen werden nur ersetzt, wenn Provider, Leistungszeitraum, Tarif, Verbrauchseinheit und Beleg offengelegt sind.

3.2 Exit-Dokumentationskosten werden getrennt nach Datenexport, Löschbestätigung, Wechselunterstützung, technischem Workshop und Abschlussbericht ausgewiesen.

---

Lizenz: Apache-2.0 OR MIT.
