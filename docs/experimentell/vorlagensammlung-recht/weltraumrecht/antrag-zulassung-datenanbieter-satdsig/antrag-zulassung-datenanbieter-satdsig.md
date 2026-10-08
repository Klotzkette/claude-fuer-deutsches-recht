# Antrag auf Zulassung als Anbieter hochwertiger Erdfernerkundungsdaten (§§ 11, 12 SatDSiG)

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Antragsbestandteil, nicht einreichen]

Diese Vorlage ersetzt nicht die anwaltliche und sicherheitstechnische Eigenleistung. Sie liefert das Gerüst, nicht die automatisierte Sensitivitätsprüfung. Der Anwender bringt Produkte, Kunden, Empfänger, Datenwege und BSI-Verfahren; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Kein hochwertiger Datensatz darf ohne dokumentiertes Prüf- und Freigabeergebnis verbreitet werden.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Adressat und Antragsteller

An das Bundesamt für Wirtschaft und Ausfuhrkontrolle

[zuständiger Bereich und Anschrift]

Antragsteller und Datenanbieter: [Firma, Sitz, Register und Vertretung]

Datenprodukte: [Systeme, Sensoren und Produktfamilien]

Betreff: Antrag auf Zulassung nach § 11 Abs. 1 Satellitendatensicherheitsgesetz (SatDSiG)

[Ort], den [Datum]

### 1. Antrag

1.1 Der Antragsteller beantragt die Zulassung als Datenanbieter für die in Anlage 1 bezeichneten Daten und Produkte der hochwertigen Erdfernerkundungssysteme [Systeme].

1.2 Die Zulassung soll Empfang, Verarbeitung, Speicherung und Verbreitung über die in Anlage 2 abschließend bezeichneten Bodenstandorte und Übermittlungswege erfassen.

### 2. Geschäfts- und Datenmodell

2.1 Der Antragsteller verbreitet [Rohdaten, Prozessierungsstufen, Analyseprodukte, Karten, Schnittstellendienste oder weitere Produkte] an [Behörden, Unternehmen, Forschung und weitere Kundengruppen].

2.2 Daten werden [auf konkrete Anfrage / aus einem Archiv / als Abonnement / über Schnittstelle / ohne Anfrage] bereitgestellt. Jeder Vertriebsweg löst vor Freigabe die in Abschnitt 6 beschriebene Sensitivitätsprüfung aus.

2.3 Betreiber und Genehmigungsstatus der Ursprungssysteme sind in Anlage 1 aufgeführt. Verträge verpflichten sie und sämtliche Bodensegmentdienstleister zur Bereitstellung der nach § 18 SatDSiG erforderlichen Protokolle.

### 3. Zuverlässigkeit und Organisation

3.1 Antragsteller, Vertretungsorgane und sicherheitsverantwortliche Personen besitzen die erforderliche Zuverlässigkeit. Nachweise und Erklärungen liegen in Anlage 3 vor.

3.2 Verantwortung für Kundenprüfung, Sensitivitätsprüfung, technische Auslieferung, Sicherheitsbetrieb und Behördenkommunikation ist personell zugeordnet. Kein Mitarbeiter kann allein Kunde anlegen, Prüfung verändern und Daten ausliefern.

### 4. Physischer und logischer Schutz

4.1 Empfangs-, Verarbeitungs- und Speichersysteme befinden sich in [Standorte]. Zutritt und Zugriff erfordern [Identitätsprüfung, Rollenrecht, Mehrfaktor-Authentisierung und Protokollierung].

4.2 Datenübertragungen zwischen Bodenstandorten und zu anderen Datenanbietern verwenden [Verfahren und BSI-Prüfstatus]. Schlüsselmanagement, Rotation, Sperre und Notfallwiederherstellung sind in Anlage 4 beschrieben.

4.3 Das sichere Verbreiten nach dem Stand der Technik wird durch [Verschlüsselung, Empfängerauthentisierung, Downloadgrenze, Wasserzeichen, Protokollierung und weitere Kontrollen] gewährleistet.

### 5. Personal und Sicherheitsüberprüfung

5.1 Personen mit Zugang zu Empfang, Verarbeitung oder Speicherung hochwertiger Daten sind in Anlage 5 nach Rolle und Berechtigung erfasst. Die einfache Sicherheitsüberprüfung nach § 12 Abs. 2 SatDSiG wird vor Zugriff veranlasst.

5.2 Ausscheiden, Rollenwechsel und Verdachtsfälle lösen unverzügliche Sperre, Schlüsselprüfung und dokumentierte Rechtebereinigung aus.

### 6. Sensitivitätsprüfung und Erlaubnis-Gate

6.1 Für jede Anfrage erfasst das System Anfragenden, Identitätsnachweis, sämtliche bestimmungsgemäßen Datenempfänger und deren gewöhnlichen Aufenthaltsort.

6.2 Die Prüfung kombiniert Informationsgehalt, Zielgebiet, Erzeugungszeit, Zeit bis zur Lieferung, Bodensegmente und Empfänger nach der aktuellen SatDSiV. Das System lässt keinen eigenen Einschätzungsspielraum außerhalb der vorgegebenen Entscheidungslogik zu.

6.3 [Variante A — keine sensitive Anfrage]

Ergibt die Prüfung keine sensitive Anfrage, wird die Auslieferung nach zweiter Freigabe protokolliert.

6.4 [Variante B — sensitive Anfrage ohne Erlaubnis]

Ergibt die Prüfung eine sensitive Anfrage, bleibt die Auslieferung technisch gesperrt, bis eine Erlaubnis nach § 19 SatDSiG vorliegt.

6.5 [Variante C — Sammelerlaubnis]

Die Anfrage fällt unter die Sammelerlaubnis [Bescheid, Umfang und Geltungsdauer]. Das System prüft zusätzlich jede dort festgelegte Bedingung.

### 7. Dokumentation und Aufbewahrung

7.1 Das System zeichnet Anfrage, Empfänger, Identitätsprüfung, Sensitivitätsprüfung, Erzeugungsauftrag, Empfang, Kryptografie, Verarbeitung, Metadaten, Transfer, Auslieferungsbestätigung und Rechnung vollständig auf.

7.2 Die Aufzeichnungen werden mindestens fünf Jahre nach Erzeugung der jeweiligen Daten aufbewahrt. Der Anfragende wird über Aufbewahrung und behördliche Einsichtsmöglichkeit informiert.

7.3 Protokolle fremder Bodensegmente werden technisch übernommen oder unveränderbar referenziert und für denselben Zeitraum bereitgehalten.

### 8. Anzeigen und Sicherheitsvorfälle

8.1 Änderungen registerrelevanter Tatsachen, Gesellschafter, Schutzmaßnahmen oder Anhaltspunkte für den Verlust der Datensicherung werden unverzüglich schriftlich oder elektronisch angezeigt.

8.2 Sicherheitsvorfälle lösen [Eindämmung, Auslieferungssperre, Beweissicherung, Bewertung, Behördenmeldung und Wiederanlauf] aus. Verantwortlich ist [Name und Kontakt].

### 9. Vorrangige Bundesanfragen

9.1 Das Betriebssystem kann Anfragen der Bundesrepublik Deutschland in den Fällen des § 21 SatDSiG gegenüber anderen Aufträgen priorisieren. Zuständigkeit, Authentisierung und Vergütungsabwicklung sind in Anlage 6 beschrieben.

### 10. BSI-Beteiligung und Inbetriebnahme

10.1 Das Bundesamt für Sicherheit in der Informationstechnik (BSI) wurde am [Datum] beteiligt. Die offenen Prüfgegenstände und Zieltermine ergeben sich aus Anlage 7.

10.2 Die produktive Verbreitung beginnt erst nach Zulassung, erforderlicher Eignungserklärung, Sicherheitsüberprüfungen und technischer Abnahme.

Mit freundlichen Grüßen

[Name, Funktion und Unterschrift]

## Anlagen

### Anlage 1 — Systeme und Produkte

1.1 [Ursprungssystem, Genehmigung, Sensor, Produktstufe und Informationsgehalt].

### Anlage 2 — Standorte und Datenflüsse

2.1 [Bodensegmente, Verarbeitung, Speicher, Empfänger und Übertragungswege].

### Anlage 3 — Zuverlässigkeit und Organisation

3.1 [Register, Organe, Verantwortliche, Rollen und Erklärungen].

### Anlage 4 — Sicherheitsarchitektur

4.1 [BSI-Verfahren, Kryptografie, Schlüssel, Zugriff und Auslieferung].

### Anlage 5 — Sicherheitsüberprüfungen

5.1 [Person, Rolle, Zugriff, Status und Freigabedatum].

### Anlage 6 — Prüf- und Priorisierungsprozess

6.1 [Identität, Sensitivität, Erlaubnis-Gate, Bundesanfragen und Protokolle].

### Anlage 7 — BSI-Prüfung und Abnahme

7.1 [Prüfplan, Ergebnisse, offene Punkte und Inbetriebnahmefreigabe].

---

Lizenz: Apache-2.0 OR MIT.
