# Quellcode-Herausgabe- und Datenexport-Notfallplan

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Dokumentbestandteil, nicht mitverwenden]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch kein verwendbares Dokument, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Rubrum, Projekt, Beteiligte und System

Dieser Notfallplan betrifft das System [Name], betrieben für [Auftraggeberin oder Kunde] durch [Dienstleisterin oder Anbieterin]. Fachlich verantwortlich ist [Name, Rolle]. Technisch verantwortlich ist [Name, Rolle].

Der Plan wird aktiviert, wenn [Kündigung / Insolvenz / schwerer Ausfall / Sicherheitsvorfall / verweigerter Datenexport / Escrow-Fall] eintritt und die Fortführung, Migration oder rechtssichere Stilllegung des Systems ohne geordnete Herausgabe gefährdet ist.

### 1. Gegenstand und Aktivierungsfall

1.1 Gegenstand dieses Plans sind Quellcode, Build- und Deploymentskripte, Datenbankschemata, Datenexporte, Schnittstellendokumentation, Konfigurationsdateien, Schlüsselverzeichnisse, Betriebsdokumentation und Übergabewissen.

1.2 Der Aktivierungsfall liegt vor, wenn eines der folgenden Ereignisse eintritt: [konkretes Ereignis]. Das Ereignis wird durch [Person oder Stelle] festgestellt und in Anlage 1 dokumentiert.

1.3 Die Aktivierung berechtigt nur zu den Herausgabe-, Nutzungs- und Migrationshandlungen, die nach Vertrag, Lizenz, Escrow-Regelung, Datenschutzrecht und Geschäftsgeheimnisschutz zulässig sind.

### 2. Herausgabepaket

2.1 Das Herausgabepaket enthält den aktuellen produktiven Quellcode einschließlich Branch, Commit-Stand, Build-Anweisung und Abhängigkeiten.

2.2 Es enthält alle Skripte, Containerdefinitionen, Infrastrukturdefinitionen, Datenbankschemata, Konfigurationsmuster und Migrationsskripte, die für eine lauffähige Neuinstallation in [Zielumgebung] erforderlich sind.

2.3 Es enthält eine Liste sämtlicher Drittkomponenten, Open-Source-Bibliotheken, Lizenztexte, Copyleft-Hinweise, proprietärer Module und nicht übertragbarer Bestandteile.

2.4 Es enthält die Betriebsdokumentation mit Systemarchitektur, Schnittstellen, Wartungsroutinen, Backup- und Restore-Verfahren, Monitoring, Störungsbehandlung und bekannten technischen Schulden.

### 3. Datenexport

3.1 Personenbezogene Daten, Stamm- und Bewegungsdaten, Protokolle, Dokumente, Metadaten und Mandanten- oder Kundendaten werden in den Formaten [Format] exportiert.

3.2 Der Export enthält Datenmodell, Feldbeschreibung, Primär- und Fremdschlüssel, Zeichensatz, Zeitzonenlogik, Löschkennzeichen und Versionsstand.

3.3 Der Export wird verschlüsselt übergeben. Schlüssel und Passwörter werden über einen getrennten Kommunikationskanal an [berechtigte Person] übermittelt.

3.4 Vor Herausgabe wird geprüft, ob Daten Dritter, Geheimnisse, nicht migrierbare Inhalte oder gesetzliche Löschpflichten einer Übergabe entgegenstehen.

### 4. Zugänge, Schlüssel und Geheimnisse

4.1 Produktionszugänge werden nicht pauschal herausgegeben. Es werden nur diejenigen Zugänge, Schlüssel und Tokens übergeben, die für Migration, Stabilisierung oder geordneten Weiterbetrieb erforderlich sind.

4.2 API-Schlüssel, Zertifikate, Service-Accounts, Admin-Zugänge und Datenbankzugänge werden in Anlage 2 mit Zweck, Berechtigung, Ablaufdatum und Rotationsplan dokumentiert.

4.3 Nach Übergabe werden kompromittierungsgefährdete Schlüssel ersetzt. Alte Schlüssel werden gesperrt, sobald der Übergang technisch abgeschlossen ist.

### 5. Prüfung und Abnahme der Herausgabe

5.1 Die empfangende Stelle prüft binnen [Anzahl] Bankarbeitstagen, ob Quellcode, Datenexport, Dokumentation und Zugänge vollständig, lesbar, entschlüsselbar und technisch nutzbar sind.

5.2 Die Prüfung umfasst einen Test-Build, einen Test-Import, eine Integritätsprüfung der Exportdateien und eine Plausibilitätsprüfung der Datenbestände.

5.3 Mängel werden in Anlage 3 dokumentiert. Die herausgabepflichtige Partei behebt behebbare Mängel binnen [Anzahl] Bankarbeitstagen, soweit ihr dies rechtlich und technisch möglich ist.

### 6. Datenschutz und Geheimnisschutz

6.1 Personenbezogene Daten werden nur auf Grundlage des bestehenden Vertrags, einer Weisung, einer rechtlichen Pflicht oder einer gesonderten Vereinbarung verarbeitet.

6.2 Geschäftsgeheimnisse bleiben geschützt. Die empfangende Stelle nutzt Quellcode, Dokumentation und Betriebswissen nur für Stabilisierung, Migration, Wartung, Fehlerbehebung, Prüfung und rechtlich zulässige Anschlussnutzung.

6.3 Unbefugte Kopien werden vermieden. Nicht mehr benötigte Zwischenstände werden nach Abschluss der Migration gelöscht oder archiviert, soweit gesetzliche Aufbewahrungspflichten entgegenstehen.

### 7. Freigabe und Abschluss

7.1 Der Notfallplan ist abgeschlossen, wenn Herausgabepaket, Datenexport, Schlüsselübergabe, Testimport, Rechtsprüfung und Lösch- oder Archivierungsentscheidung dokumentiert sind.

7.2 Offene Punkte werden mit Verantwortlichkeit und Frist in Anlage 3 geführt.

7.3 Ort, Datum: [Ort], [Datum].

Unterschriften:

7.4 Auftraggeberin oder Kunde: [Name, Funktion, Unterschrift].

7.5 Dienstleisterin oder Anbieterin: [Name, Funktion, Unterschrift].

### Anlage 1 — Aktivierungsvermerk

1. Ereignis

1.1 Aktivierungsgrund: [Ereignis].

1.2 Eintrittsdatum: [Datum].

1.3 Feststellende Stelle: [Name, Rolle].

2. Vertragsgrundlage

2.1 Vertrag oder Escrow-Regelung: [Dokument, Abschnitt].

2.2 Zulässiger Nutzungsumfang: [Beschreibung].

2.3 Rechtsprüfung abgeschlossen durch: [Name, Datum].

### Anlage 2 — Übergabeinventar

| Gegenstand | Format / Ort | Version | Verantwortlich | Bemerkung |
| --- | --- | --- | --- | --- |
| Quellcode | [Repository / Archiv] | [Commit] | [Name] | [Hinweis] |
| Datenexport | [Format] | [Datum] | [Name] | [Hinweis] |
| Dokumentation | [Ort] | [Version] | [Name] | [Hinweis] |
| Schlüssel | [separater Kanal] | [Datum] | [Name] | [Rotation] |

### Anlage 3 — Prüf- und Mängelprotokoll

1. Prüfung

1.1 Test-Build durchgeführt am: [Datum].

1.2 Test-Import durchgeführt am: [Datum].

1.3 Integritätsprüfung durchgeführt am: [Datum].

2. Offene Punkte

2.1 Mangel: [Beschreibung].

2.2 Verantwortlich: [Name].

2.3 Frist: [Datum].

2.4 Erledigt am: [Datum].

---

Lizenz: Apache-2.0 OR MIT.
