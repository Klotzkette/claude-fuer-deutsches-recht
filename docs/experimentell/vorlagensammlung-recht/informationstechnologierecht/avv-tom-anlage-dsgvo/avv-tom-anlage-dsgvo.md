# Anlage Technisch-Organisatorische Maßnahmen (TOM) zum Auftragsverarbeitungsvertrag

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Rubrum, Beteiligte und Bearbeitungsstand

**Auftragsverarbeiter (Anbieter):**

[vollständiger Firmenname, Rechtsform, Registergericht und Registernummer, Sitz, Geschäftsadresse, Datenschutzverantwortliche oder Datenschutzbeauftragter: Name, E-Mail]

**Verantwortlicher (Auftraggeber):**

[vollständiger Firmenname oder Vor- und Nachname, Rechtsform, Registergericht und Registernummer oder Geburtsdatum, Sitz oder Anschrift, Datenschutzverantwortliche oder Datenschutzbeauftragter: Name, E-Mail]

**Bezug:** Diese TOM-Anlage ist Bestandteil des Auftragsverarbeitungsvertrags (AVV) vom [Datum] zwischen den Parteien (Art. 28 Abs. 3 lit. c DSGVO).

**Verarbeitungsgegenstand:** [Beschreibung der Verarbeitung, z. B. Hosting und Betrieb der CRM-Software Name für den Verantwortlichen; alternativ: E-Mail-Marketing-Dienstleistungen]

**Kategorien betroffener Personen:** [z. B. Kunden, Interessenten, Mitarbeitende des Verantwortlichen]

**Kategorien personenbezogener Daten:** [z. B. Name, E-Mail-Adresse, Telefonnummer, Vertragshistorie, IP-Adressen]

**Bearbeitungsstand:** [Entwurf / geprüft / unterzeichnet am Datum, Akte: Az.]

## Technisch-Organisatorische Maßnahmen nach Art. 32 DSGVO

### 1. Zutrittskontrolle

Maßnahmen, die verhindern, dass Unbefugte Zugang zu Datenverarbeitungsanlagen erhalten, mit denen personenbezogene Daten verarbeitet werden:

| Maßnahme | Umsetzung beim Auftragsverarbeiter | Nachweis / Prüfintervall |
| --- | --- | --- |
| Zutrittssicherung Rechenzentrum | Zutrittskontrollsystem mit Chipkarte oder biometrischer Authentifizierung; kein physischer Zutritt ohne dokumentierte Genehmigung | [Zertifikat ISO 27001 / Audit-Bericht, jährlich] |
| Sicherheitszonen | Serverräume in eigenständiger Sicherheitszone mit eigener Zugangskontrolle und Videoüberwachung | [Besichtigungsprotokoll / Audit] |
| Besucherinnen- und Besucher-Management | Besucherinnen und Besucher werden registriert, begleitet und erhalten keinen unbeaufsichtigten Zutritt | [Besucherregister] |
| Alarmanlage und Einbruchschutz | Einbruchmeldeanlage (EMA) mit direkter Meldung an Sicherheitsdienst | [Wartungsprotokoll, halbjährlich] |

### 2. Zugangskontrolle

Maßnahmen, die verhindern, dass Datenverarbeitungssysteme von Unbefugten genutzt werden:

| Maßnahme | Umsetzung | Nachweis / Prüfintervall |
| --- | --- | --- |
| Passwortpolitik | Mindestlänge [12] Zeichen, Kombination aus Groß- und Kleinbuchstaben, Ziffern und Sonderzeichen; Passwortänderung alle [90] Tage oder bei Verdacht auf Kompromittierung | [IT-Richtlinie, Versionsstand Datum] |
| Mehr-Faktor-Authentifizierung (MFA) | MFA für alle Konten mit Zugriff auf personenbezogene Daten zwingend aktiviert | [technische Konfigurationsdokumentation] |
| Automatische Sperrung | Konten werden nach [fünf] Fehlversuchen für [15] Minuten gesperrt; Bildschirm sperrt sich nach [10] Minuten Inaktivität | [technische Konfigurationsdokumentation] |
| Privilegierter Zugang (PAM) | Administratorzugänge gesondert verwaltet, protokolliert und nach dem Vier-Augen-Prinzip vergeben | [PAM-System-Dokumentation] |

### 3. Zugriffskontrolle

Maßnahmen, die gewährleisten, dass die zur Benutzung von Datenverarbeitungssystemen Befugten ausschließlich auf die ihrer Zugangsberechtigung unterliegenden Daten zugreifen können:

| Maßnahme | Umsetzung | Nachweis / Prüfintervall |
| --- | --- | --- |
| Rollen- und Rechtekonzept (RBAC) | Berechtigungen nach dem Least-Privilege-Prinzip; Rollen definiert und dokumentiert | [RBAC-Dokumentation, Versionsstand Datum] |
| Need-to-know-Prinzip | Zugriff auf personenbezogene Daten nur für Mitarbeiter, die diese für ihre Aufgabe benötigen | [Berechtigungsmatrix] |
| Regelmäßige Zugriffsprüfung | Berechtigungen werden mindestens [jährlich] sowie bei Rollenwechsel oder Ausscheiden überprüft und angepasst | [Prüfprotokoll] |
| Protokollierung | Zugriffe auf personenbezogene Daten werden im Umfang des technisch Möglichen und rechtlich Zulässigen protokolliert | [Logging-Konzept] |

### 4. Trennungskontrolle

Maßnahmen, die gewährleisten, dass zu unterschiedlichen Zwecken erhobene Daten getrennt verarbeitet werden können:

| Maßnahme | Umsetzung | Nachweis / Prüfintervall |
| --- | --- | --- |
| Mandantentrennung | Daten verschiedener Auftraggeber in getrennten Datenbankinstanzen oder durch logische Mandantentrennung mit nachgewiesener technischer Isolation | [Architektur-Dokumentation] |
| Testdaten | Produktivdaten werden in Test- und Entwicklungsumgebungen nicht verwendet; Testdaten werden anonymisiert oder synthetisch erzeugt | [Testdatenrichtlinie] |

### 5. Pseudonymisierung und Verschlüsselung

| Maßnahme | Umsetzung | Standard / Algorithmus |
| --- | --- | --- |
| Verschlüsselung in der Übertragung | TLS 1.2 oder höher für alle Datenübertragungen; veraltete Protokolle (SSLv3, TLS 1.0, TLS 1.1) deaktiviert | TLS ≥ 1.2, HSTS |
| Verschlüsselung at rest | Festplatten und Backup-Medien mit AES-256 verschlüsselt | AES-256 |
| Pseudonymisierung | Wo technisch möglich und zweckmäßig werden Direktidentifikatoren durch Pseudonyme ersetzt; Zuordnungstabelle getrennt aufbewahrt | [Pseudonymisierungskonzept] |

### 6. Verfügbarkeits- und Belastbarkeitskontrolle

| Maßnahme | Umsetzung | Nachweis / Prüfintervall |
| --- | --- | --- |
| Backup | Tägliches vollständiges Backup; inkrementelle Backups [stündlich]; Aufbewahrungsdauer [30 Tage]; geografische Redundanz in mindestens zwei Rechenzentren | [Backup-Konzept, Testprotokoll] |
| Disaster Recovery | Recovery-Time-Objective (RTO) [vier] Stunden; Recovery-Point-Objective (RPO) [24] Stunden; DR-Test mindestens [einmal jährlich] | [DR-Testprotokoll] |
| Redundanz und Hochverfügbarkeit | Redundante Stromversorgung (USV, Notstromaggregat), redundante Netzwerkanbindung, RAID-Systeme | [Infrastrukturdokumentation] |
| Kapazitätsplanung | Regelmäßige Überprüfung der Ressourcenauslastung; Skalierbarkeit dokumentiert | [Kapazitätsbericht, quartalsweise] |
| DDoS-Schutz | Eingerichteter DDoS-Schutz über [Anbieter / CDN / Firewall] | [Konfigurationsdokumentation] |

### 7. Verfahren zur regelmäßigen Überprüfung (Art. 32 Abs. 1 lit. d DSGVO)

| Maßnahme | Umsetzung | Nachweis / Prüfintervall |
| --- | --- | --- |
| Penetrationstest | Mindestens [jährliche] externe Penetrationstests durch akkreditiertes Unternehmen | [Pentest-Bericht, zuletzt Datum] |
| Schwachstellenscan | Automatisierter Schwachstellenscan mindestens [monatlich] | [Scan-Report] |
| Patch-Management | Sicherheitskritische Patches werden innerhalb von [72] Stunden nach Veröffentlichung eingespielt | [Patch-Protokoll] |
| ISMS | Informationssicherheits-Managementsystem nach ISO 27001 oder vergleichbarem Standard | [Zertifikat, gültig bis Datum] |
| Datenschutz-Folgenabschätzung | Für Verarbeitungen mit hohem Risiko wird eine DSFA nach Art. 35 DSGVO durchgeführt | [DSFA-Register] |

### 8. Unterauftragsverarbeiter (Art. 28 Abs. 2 und 4 DSGVO)

Der Auftragsverarbeiter setzt folgende Unterauftragsverarbeiter ein:

| Unterauftragsverarbeiter | Sitz | Verarbeitungsgegenstand | Übermittlungsgrundlage | Prüfintervall |
| --- | --- | --- | --- | --- |
| [Name des Cloud-Anbieters oder sonstigen Unterauftragsverarbeiters] | [EU / Drittland: Land] | [Serverinfrastruktur / Speicherung / sonstige Leistung] | [Art. 45 DSGVO Angemessenheitsbeschluss / Art. 46 DSGVO Standardvertragsklauseln] | jährlich |
| [Name] | [EU / Drittland] | [z. B. E-Mail-Dienst, Monitoring] | […] | [jährlich] |

Eine Änderung des Unteraufträgerskreises wird dem Verantwortlichen mindestens [vier] Wochen vorab in Textform mitgeteilt; der Verantwortliche kann innerhalb von [zwei] Wochen widersprechen.

### 9. Löschkonzept

9.1 Personenbezogene Daten werden nach Zweckfortfall oder auf Weisung des Verantwortlichen unverzüglich gelöscht. Löschfristen richten sich nach dem Verarbeitungsverzeichnis des Verantwortlichen.

9.2 Nach Beendigung des AVV werden alle Daten innerhalb von [30] Tagen sicher gelöscht oder dem Verantwortlichen in einem gängigen Format zur Verfügung gestellt und danach gelöscht.

9.3 Die Löschung wird protokolliert und dem Verantwortlichen schriftlich bestätigt.

### Freigabe und Unterzeichnung

[Ort], den [Datum]

| Für den Auftragsverarbeiter | Für den Verantwortlichen |
|---|---|
| _____________________________ | _____________________________ |
| [Name, Funktion, Datenschutzbeauftragte oder Datenschutzbeauftragter] | [Name, Funktion] |

### Anlage 1 — Prüf- und Bewertungsschema

1. Zweck und Prüfstand

1.1 Dieses Schema bewertet vor Unterzeichnung, ob die in den Ziffern 1 bis 9 beschriebenen Maßnahmen dem Schutzbedarf der konkreten Verarbeitung nach Art. 32 Abs. 1 DSGVO genügen.

1.2 Geprüfte TOM-Fassung: [Versionsstand / Datum]; Prüfdatum: [JJJJ-MM-TT]; prüfende Person: [Name, Funktion].

2. Schutzbedarfsfeststellung

2.1 Schutzbedarf der verarbeiteten Datenkategorien unter Berücksichtigung von Art, Umfang, Umständen und Zwecken der Verarbeitung: [normal / hoch / sehr hoch] mit Begründung [Freitext].

2.2 Maßgebliche Risikoszenarien für die betroffenen Personen: [unbefugte Offenlegung / Verlust / Verfälschung / Nichtverfügbarkeit], jeweils mit Eintrittswahrscheinlichkeit [gering / mittel / hoch] und Schwere [gering / mittel / hoch].

3. Bewertung je Kontrollbereich

3.1 Zutrittskontrolle nach Ziffer 1: Umsetzungsgrad [vollständig / teilweise / offen], vorgelegter Nachweis [Dokument, Datum], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

3.2 Zugangskontrolle nach Ziffer 2: Umsetzungsgrad [vollständig / teilweise / offen], vorgelegter Nachweis [Dokument, Datum], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

3.3 Zugriffskontrolle nach Ziffer 3: Umsetzungsgrad [vollständig / teilweise / offen], vorgelegter Nachweis [Dokument, Datum], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

3.4 Trennungskontrolle nach Ziffer 4: Umsetzungsgrad [vollständig / teilweise / offen], vorgelegter Nachweis [Dokument, Datum], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

3.5 Pseudonymisierung und Verschlüsselung nach Ziffer 5: Umsetzungsgrad [vollständig / teilweise / offen], eingesetzte Standards [Protokoll / Algorithmus], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

3.6 Verfügbarkeit und Belastbarkeit nach Ziffer 6: Umsetzungsgrad [vollständig / teilweise / offen], letzter Wiederherstellungstest [Datum, Ergebnis], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

3.7 Überprüfungsverfahren nach Ziffer 7: Umsetzungsgrad [vollständig / teilweise / offen], letzter Penetrationstest [Datum, Prüfer], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

3.8 Unterauftragsverarbeiter nach Ziffer 8: Vollständigkeit und Aktualität der Liste [bestätigt / zu ergänzen], Drittlandbezug [ja / nein, Land], Transferinstrument [Angemessenheitsbeschluss / Standardvertragsklauseln / offen].

3.9 Löschkonzept nach Ziffer 9: Umsetzungsgrad [vollständig / teilweise / offen], Nachweisform [Löschprotokoll / Bestätigung], festgestellte Lücke [Freitext], Abhilfemaßnahme mit Frist [Maßnahme, Datum].

4. Gesamtbewertung und Freigabe

4.1 Gesamtergebnis der Angemessenheitsprüfung nach Art. 32 DSGVO: [angemessen / angemessen mit Auflagen / nicht angemessen] mit Begründung [Freitext].

4.2 Auflagen mit verantwortlicher Person und Wiedervorlagetermin: [Auflage, Name, Datum].

4.3 Freigabevermerk: [Ort], [Datum], [Name, Funktion, Unterschrift].

---

Lizenz: Apache-2.0 OR MIT.
