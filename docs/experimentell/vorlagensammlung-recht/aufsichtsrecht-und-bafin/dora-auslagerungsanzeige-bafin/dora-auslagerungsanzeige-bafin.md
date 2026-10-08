# Anzeige und Dokumentation kritischer IKT-Drittdienstleistung nach DORA

[WARNHINWEIS — nicht Schriftsatzbestandteil, nicht miteinreichen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Schriftsatz, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

Aufsichtliche Anzeige, Registerauszug und Steuerungsdokumentation für eine IKT-Drittdienstleistung, die eine kritische oder wichtige Funktion unterstützt.

---

### Rubrum, Adressat und Institut

An die
Bundesanstalt für Finanzdienstleistungsaufsicht
[zuständiges Referat]
[Anschrift]

über die
Deutsche Bundesbank
Hauptverwaltung [zuständige Hauptverwaltung]
[Anschrift]

Anzeigendes Unternehmen ist [Firma], [Rechtsform], [Registernummer], [Sitz], vertreten durch [Geschäftsleitung].

Kontakt für Rückfragen: [Name, Funktion, Telefon, E-Mail].

Betroffene IKT-Drittdienstleistung: [Bezeichnung der Dienstleistung], erbracht durch [Name des IKT-Drittdienstleisters, Sitz, Konzernzugehörigkeit].

## 1. Anzeige und Einordnung

1.1 Namens und im Auftrag des anzeigenden Unternehmens zeigen wir die beabsichtigte oder bestehende vertragliche Vereinbarung über die IKT-Drittdienstleistung [Bezeichnung] an und reichen den zugehörigen Registerauszug, die Risikoanalyse und die Steuerungsunterlagen ein.

1.2 Die Dienstleistung unterstützt die Funktion [kritische oder wichtige Funktion], weil [konkrete Begründung: Kundenzahl, Transaktionsvolumen, Ausfallfolge, regulatorische Pflicht, Datenkritikalität, fehlende kurzfristige Substituierbarkeit].

1.3 Die vertragliche Vereinbarung beginnt am [Datum] und hat eine Laufzeit bis [Datum / unbefristet mit Kündigungsfrist]. Die Leistung wird an den Standorten [Standorte] erbracht; Daten werden verarbeitet in [Land / Rechenzentrum / Cloud-Region].

## 2. Dienstleistungsumfang und Abhängigkeit

2.1 Der Dienstleister erbringt [Hosting / Cloud-Infrastruktur / Kernbankensystem / Zahlungsverkehrsmodul / Identifizierungsdienst / Datenanalyse / Sicherheitsüberwachung]. Die Leistung umfasst [konkrete Module] und ist technisch angebunden über [Schnittstellen, API, Netzwerk, Administrationszugang].

2.2 Die betroffenen Geschäftsprozesse sind [Prozess 1], [Prozess 2] und [Prozess 3]. Ein Ausfall länger als [Stunden] hätte folgende Auswirkungen: [Kundenausfall, Transaktionsstopp, Meldefehler, Abwicklungsrisiko, Datenschutzrisiko].

2.3 Unterauslagerungen bestehen an [Unterauftragnehmer, Sitz, Leistung, Datenzugriff]. Neue Unterauslagerungen dürfen nur nach [Informationsfrist, Widerspruchsrecht, Genehmigungserfordernis] eingesetzt werden.

## 3. DORA-Steuerung und Vertragsmindestinhalt

3.1 Die vertragliche Vereinbarung enthält Leistungsbeschreibung, Service-Level, Verfügbarkeit, Integrität, Vertraulichkeit, Datenzugang, Datenrückgabe, Prüfungsrechte, Informationspflichten, Unterauslagerung, Exit, Unterstützung bei Vorfällen und Kündigungsrechte.

3.2 Prüfungs- und Zugangsrechte werden nicht auf Zertifikate beschränkt. Das anzeigende Unternehmen erhält [direktes Prüfungsrecht / gepooltes Audit / Drittprüfermodell] einschließlich Einsicht in [Systeme, Standorte, Sicherheitsnachweise, Vorfallsberichte].

3.3 Für schwerwiegende IKT-bezogene Vorfälle gelten Meldewege, interne Eskalationsfristen und Zuständigkeiten nach Anlage 3. Der Dienstleister muss sicherheitsrelevante Vorfälle innerhalb von [Frist] melden und die für aufsichtsrechtliche Meldungen erforderlichen Informationen liefern.

3.4 Die Vertragsprüfung bestätigt, dass die Mindestinhalte für IKT-Drittdienstleistungen nicht nur in Rahmenbedingungen, sondern in durchsetzbaren Klauseln stehen: präzise Leistungsbeschreibung, Orte der Datenverarbeitung, Zugriff und Wiederherstellung von Daten, Unterstützung bei Vorfällen, Prüfungsrechte, Unterauslagerungskontrolle, Kündigungsrechte und geordneter Exit.

## 4. Risikoanalyse, Konzentrationsrisiko und Exit

4.1 Die Risikoanalyse bewertet Schutzbedarf, Datenkategorien, Kritikalität, Ausfallfolgen, Konzentrationsrisiken, Substituierbarkeit, Unterauslagerungen, Drittlandbezug und Wirksamkeit der Kontrollen.

4.2 Das Konzentrationsrisiko wird anhand folgender Kriterien bewertet: [Anzahl weiterer kritischer Leistungen desselben Dienstleisters], [Marktverfügbarkeit alternativer Anbieter], [technische Wechselkosten], [Datenportabilität], [Abhängigkeit von proprietären Schnittstellen].

4.3 Der Exit-Plan sieht vor: Auslöser, Entscheidungszuständigkeit, Datenexportformat, Migrationsfenster, Parallelbetrieb, Kundenauswirkung, Rückgabe und Löschung von Daten, Vertragskündigung und Notbetrieb bis zur Übernahme durch [Ersatzdienstleister / Eigenbetrieb].

4.4 Die Exit-Fähigkeit wird nicht nur abstrakt beschrieben, sondern durch [Testmigration / Datenexportprobe / Wiederanlauftest / Vertragsklauseltest / Ersatzanbieteranalyse] nachgewiesen. Offene Abhängigkeiten werden mit Zieltermin, verantwortlicher Funktion und Übergangsmaßnahme in Anlage 5 geführt.

## 5. Registerauszug und Anlagen

5.1 Dem Schreiben sind beigefügt:

| Anlage | Inhalt | Zweck |
| --- | --- | --- |
| Anlage 1 | Registerauszug IKT-Drittdienstleistung | eindeutige Erfassung der Dienstleistung |
| Anlage 2 | Risikoanalyse und Klassifizierung | Kritikalität, Schutzbedarf, Konzentration |
| Anlage 3 | Vorfalls-, Melde- und Eskalationsmatrix | DORA- und Aufsichtsanschluss |
| Anlage 4 | Vertragskontrollblatt | Mindestinhalte, Prüfungsrechte, Exit |
| Anlage 5 | Ausstiegs- und Migrationsplan | Substituierbarkeit und Abwicklungsfähigkeit |
| Anlage 6 | Datenschutz- und Geheimhaltungsvermerk | Datenstandorte, Rollen, Schwärzungen |

5.2 Wir bitten um Bestätigung des Eingangs und um Bündelung etwaiger Rückfragen über [Ansprechperson].

[Ort], den [Datum]

_____________________________
[Unterschrift, Name, Funktion]

## Anlagen

### Anlage 1 — Registerauszug IKT-Drittdienstleistung

1. Identifikation

1.1 Dienstleistung: [Bezeichnung].

1.2 Dienstleister: [Name, Sitz, Registernummer, Konzern].

1.3 Vertragsnummer und Vertragsdatum: [Nummer], [Datum].

1.4 Betroffene Funktion: [kritische oder wichtige Funktion].

2. Leistungsdaten

2.1 Leistungsort und Datenstandort: [Ort, Land, Cloud-Region].

2.2 Unterauftragnehmer: [Name, Leistung, Sitz].

2.3 Laufzeit und Kündigung: [Laufzeit, Kündigungsfrist, Sonderkündigungsrechte].

### Anlage 2 — Risikoanalyse und Klassifizierung

1. Kritikalität

1.1 Ausfallfolge: [konkrete Auswirkung].

1.2 Datenkritikalität: [personenbezogene Daten, Transaktionsdaten, Risikodaten].

1.3 Substituierbarkeit: [Ersatzanbieter, Wechselaufwand, Migrationsdauer].

2. Kontrollen

2.1 Vertragliche Kontrollen: [Prüfungsrecht, Informationspflicht, Service-Level].

2.2 Technische Kontrollen: [Verschlüsselung, Zugriff, Protokollierung, Backup].

2.3 Organisatorische Kontrollen: [Owner, Review-Frequenz, Eskalation].

### Anlage 3 — Vorfalls-, Melde- und Eskalationsmatrix

1. Vorfallklassen

1.1 Schwerwiegender IKT-Vorfall: [Kriterien].

1.2 Sicherheitsereignis ohne Meldepflicht: [Kriterien].

2. Eskalation

2.1 Dienstleistermeldung an das Institut: [Frist, Kanal, Pflichtangaben].

2.2 Interne Entscheidung über Aufsichtsmeldung: [Funktion, Frist].

2.3 Kunden- und Behördenkommunikation: [Verantwortlichkeit].

### Anlage 4 — Vertragskontrollblatt

1. Mindestinhalte

1.1 Leistungsbeschreibung und Service-Level: [Fundstelle].

1.2 Datenzugang, Datenrückgabe und Löschung: [Fundstelle].

1.3 Prüfungs- und Zugangsrechte: [Fundstelle].

1.4 Unterauslagerung: [Fundstelle].

1.5 Kündigung und Exit: [Fundstelle].

1.6 Unterstützung bei IKT-Vorfällen, aufsichtsrechtlichen Prüfungen und Kundenkommunikation: [Fundstelle].

### Anlage 5 — Ausstiegs- und Migrationsplan

1. Exit-Auslöser

1.1 Regulatorischer Exit: [Auslöser].

1.2 Operativer Exit: [Auslöser].

1.3 Wirtschaftlicher Exit: [Auslöser].

2. Migration

2.1 Ersatzlösung: [Anbieter / Eigenbetrieb].

2.2 Datenexport: [Format, Frist, Test].

2.3 Parallelbetrieb: [Dauer, Verantwortliche].

2.4 Testnachweis: [Datum, Umfang, Ergebnis, offene Befunde].

### Anlage 6 — Datenschutz- und Geheimhaltungsvermerk

1. Daten

1.1 Datenkategorien: [Kategorien].

1.2 Rollen nach DSGVO: [Verantwortlicher / Auftragsverarbeiter / gemeinsame Verantwortlichkeit].

1.3 Drittlandtransfer: [nein / ja, Rechtsgrundlage und Schutzmaßnahmen].

2. Geheimhaltung

2.1 Geschäftsgeheimnisse: [Kennzeichnung].

2.2 Schwärzungen: [Dokumente, Grund, Freigabe].

---

Lizenz: Apache-2.0 OR MIT.
