# IT-Service-Level-Agreement

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Rubrum, Beteiligte und Bearbeitungsstand

**IT-Dienstleisterin oder IT-Dienstleister (Auftragnehmer):**

[vollständiger Firmenname, Rechtsform, Registergericht und Registernummer, Sitz, Geschäftsadresse, vertreten durch Geschäftsführer oder Vorstand, Name und Funktion]

**Kunde (Auftraggeber):**

[vollständiger Firmenname oder Vor- und Nachname, Rechtsform, Registergericht und Registernummer oder Geburtsdatum, Sitz oder Anschrift, vertreten durch Name, Funktion]

**Bearbeitungsstand:** [Entwurf / Verhandlung / Unterzeichnung / Vollzug], Datum: [Datum], Akte: [Az.]

## 1. Präambel / Gegenstand

1.1 Dieser IT-Service-Level-Agreement (SLA) regelt die Qualitäts- und Leistungsstandards für folgende IT-Dienste und IT-Systeme: [konkrete Bezeichnung des Dienstes oder Systems, z. B. Hosting der Webanwendung „Produktname" auf der Cloud-Infrastruktur Anbieter in der Region; alternativ: Betrieb des ERP-Systems Systemname in Rechenzentrum Ort.]

1.2 Dieser SLA ist Bestandteil des Hauptvertrags zwischen den Parteien vom [Datum] (Hauptvertrag) und ergänzt dessen Leistungsbeschreibung. Bei Widersprüchen geht der individuell ausgehandelte Teil des Hauptvertrags vor.

1.3 Anlagen werden nur Vertragsbestandteil, wenn sie in diesem SLA ausdrücklich bezeichnet sind. Bei Widersprüchen gelten zuerst die individuell ausgehandelten Bestimmungen, danach Anlagen und zuletzt sonstige Unterlagen.

## 2. Servicebeschreibung und Leistungsumfang

2.1 Der IT-Dienstleister erbringt folgende Dienste:

| Dienst | Beschreibung | Messpunkt | Einbeziehung in SLA |
| --- | --- | --- | --- |
| [z. B. Webserver-Hosting] | [Betrieb des Webservers inkl. Load Balancer, TLS-Zertifikat, CDN] | [HTTP-Statuscode am definierten Endpunkt] | ja |
| [z. B. Datenbankbetrieb] | [Betrieb des relationalen Datenbanksystems Name inkl. Backup] | [Antwortzeit auf Standard-Query] | ja |
| [z. B. E-Mail-Weiterleitung] | [SMTP-Relay für ausgehende Transaktionsmails] | [Zustellbestätigung an MX-Record] | nein (Best-Effort) |

2.2 Nicht vom SLA umfasst sind: Force-Majeure-Ereignisse, geplante Wartungsfenster nach Abschnitt 5, Ausfälle aufgrund fehlerhafter Kundenkonfiguration, Ausfälle in der Infrastruktur Dritter außerhalb des Einflussbereichs des IT-Dienstleisters sowie Leistungsminderungen aufgrund unzureichender Mitwirkung der Kundin oder des Kunden.

## 3. Verfügbarkeit

3.1 Der IT-Dienstleister schuldet für die in Abschnitt 2 SLA-pflichtigen Dienste eine monatliche Verfügbarkeit von mindestens [99,5]% (Basis: Kalendermonat, gemessen am in Abschnitt 2 definierten Messpunkt).

3.2 Die Verfügbarkeit berechnet sich nach folgender Formel:

Verfügbarkeit (%) = [(Gesamtminuten im Monat − Ausfallminuten) ÷ Gesamtminuten im Monat] × 100

3.3 Als Ausfall gilt jede ununterbrochene Nichtverfügbarkeit des Dienstes von mehr als [fünf] Minuten, die nicht auf geplante Wartungsfenster nach Abschnitt 5 entfällt.

3.4 Verfügbarkeitsstufen und ihre Rechtsfolgen:

| Monatliche Verfügbarkeit | Service Credit |
| --- | --- |
| ≥ 99,5% | kein Credit |
| mindestens 99,0 %, aber weniger als 99,5 % | 5 % der monatlichen Servicepauschale |
| mindestens 98,0 %, aber weniger als 99,0 % | 10 % der monatlichen Servicepauschale |
| mindestens 95,0 %, aber weniger als 98,0 % | 20 % der monatlichen Servicepauschale |
| weniger als 95,0 % | 30 % der monatlichen Servicepauschale; Sonderkündigungsrecht nach Abschnitt 10.2 |

## 4. Incident-Klassen und Reaktionszeiten

4.1 Incidents werden nach folgenden Klassen klassifiziert:

| Klasse | Kriterium | Reaktionszeit (Bestätigung) | Lösungszeit (angestrebt) | Eskalation bei Überschreitung |
| --- | --- | --- | --- | --- |
| P1 — Kritisch | Vollständiger Ausfall oder Datenverlustrisiko; unmittelbare Auswirkung auf das Geschäft | 30 Minuten (24/7) | 4 Stunden | Eskalation an [Ansprechpartner IT-Dienstleister] und [Ansprechpartner Kunde] |
| P2 — Hoch | Wesentliche Funktionseinschränkung; Workaround möglich | 2 Stunden (Geschäftszeit) | 1 Werktag | Eskalation an Projektleitung |
| P3 — Mittel | Einzelne Funktion eingeschränkt; kein kritischer Geschäftsprozess betroffen | 4 Stunden (Geschäftszeit) | 5 Werktage | Bericht im monatlichen Review |
| P4 — Niedrig | Kosmetische Fehler, Wünsche, Informationsanfragen | 1 Werktag (Geschäftszeit) | nach Vereinbarung | — |

4.2 Geschäftszeit ist Montag bis Freitag, [8:00 bis 18:00 Uhr CET/CEST], ausgenommen gesetzliche Feiertage am Sitz des IT-Dienstleisters.

4.3 Die Reaktionszeit beginnt mit dem Zeitpunkt des Eingangs der Incident-Meldung über den in Anlage 1 beschriebenen Meldekanal.

## 5. Wartungsfenster

5.1 Geplante Wartungsarbeiten finden in folgenden Fenstern statt und gelten nicht als Ausfallzeit:

| Wartungstyp | Zeitfenster | Ankündigungsfrist |
| --- | --- | --- |
| Routinewartung (wöchentlich) | [Sonntag, 2:00 bis 4:00 Uhr CET/CEST] | keine Ankündigung erforderlich |
| Größere Updates | [nach Vereinbarung, außerhalb Geschäftszeit] | mindestens [72] Stunden vorher |
| Notfall-Patches | sofort, wenn Sicherheitsrisiko P1 | so schnell wie möglich, Ankündigung gleichzeitig mit Durchführung |

5.2 Überschreitet eine geplante Wartung das angekündigte Zeitfenster um mehr als [30] Minuten, gilt die Überschreitung als Ausfall nach Abschnitt 3.

## 6. Monitoring und Reporting

6.1 Der IT-Dienstleister betreibt ein kontinuierliches Monitoring der in Abschnitt 2 bezeichneten Dienste und dokumentiert Verfügbarkeit, Reaktionszeiten und Incidents in einem monatlichen SLA-Bericht.

6.2 Der SLA-Bericht wird spätestens am fünften Werktag des Folgemonats in Textform übermittelt und enthält: monatliche Verfügbarkeit je Dienst, Anzahl und Klassifikation aller Incidents, Reaktions- und Lösungszeiten, Wartungsfensterprotokolle und Höhe etwaiger Service Credits.

6.3 Die Kundin oder der Kunde hat das Recht, die Monitoring-Daten über das in Anlage 1 bezeichnete Dashboard in Echtzeit einzusehen.

## 7. Service Credits

7.1 Service Credits nach Abschnitt 3.4 werden automatisch mit der nächsten Monatsrechnung verrechnet oder, auf Antrag der Kundin oder des Kunden, als Gutschrift ausgestellt. Eine Barauszahlung von Service Credits ist ausgeschlossen.

7.2 Service Credits stellen keine Anerkennung einer Pflichtverletzung dar und schließen weitergehende gesetzliche Ansprüche nicht aus, soweit der tatsächlich eingetretene Schaden die Service Credits übersteigt.

7.3 Die Geltendmachung von Service Credits muss innerhalb von [30] Tagen nach Ende des betreffenden Kalendermonats beantragt werden; spätere Anträge sind ausgeschlossen.

## 8. Datensicherung (Backup) und Wiederherstellung

8.1 Der IT-Dienstleister erstellt täglich ein vollständiges Backup aller kundenbezogenen Daten. Die Backups werden für mindestens [30] Tage aufbewahrt und geografisch redundant gespeichert ([Standort 1 und Standort 2]).

8.2 Die Recovery Time Objective (RTO) beträgt [vier] Stunden; die Recovery Point Objective (RPO) beträgt [24] Stunden.

8.3 Die Kundin oder der Kunde kann einen vollständigen Wiederherstellungstest einmal pro Jahr anfordern. Der IT-Dienstleister führt diesen Test innerhalb von [zehn] Werktagen durch und dokumentiert das Ergebnis.

## 9. Eskalationspfad

9.1 Eskalationsstufen und Ansprechpersonen:

| Stufe | Auslöser | IT-Dienstleister | Kunde |
| --- | --- | --- | --- |
| 1 — operativ | Incident P1 länger als 2 Stunden offen | [Name, Funktion, Telefon] | [Name, Funktion, Telefon] |
| 2 — Management | SLA-Bericht zeigt Verfügbarkeit unter 99,0 Prozent | [Name, Funktion, E-Mail] | [Name, Funktion, E-Mail] |
| 3 — Geschäftsführung | Wiederholte SLA-Verletzung (3× innerhalb 6 Monate) | [Name, Funktion] | [Name, Funktion] |

## 10. Laufzeit und Kündigung

10.1 Dieser SLA gilt ab dem [Datum] für die Laufzeit des Hauptvertrags. Eine vorzeitige ordentliche Kündigung des SLA ist nicht möglich; er endet automatisch mit Beendigung des Hauptvertrags.

10.2 Die Kundin oder der Kunde hat ein außerordentliches Sonderkündigungsrecht des Hauptvertrags, wenn die monatliche Verfügbarkeit in zwei aufeinanderfolgenden Kalendermonaten unter 95,0% liegt. Die Kündigung muss innerhalb von [30] Tagen nach dem zweiten Unterschreiten erklärt werden.

10.3 Nach Vertragsende wird der IT-Dienstleister alle Kundendaten in einem gängigen, exportierbaren Format innerhalb von [15] Werktagen zur Verfügung stellen und danach unwiederbringlich löschen, soweit keine gesetzliche Aufbewahrungspflicht entgegensteht.

## 11. Mitwirkungspflichten der Kundin oder des Kunden

11.1 Die Kundin oder der Kunde benennt mindestens eine technische Ansprechperson und eine betriebswirtschaftliche Ansprechperson sowie deren Vertretungen und teilt Änderungen unverzüglich mit.

11.2 Die Kundin oder der Kunde meldet Incidents unverzüglich über den in Anlage 1 definierten Meldekanal unter Angabe des Schweregrads, der betroffenen Systeme und einer Fehlerbeschreibung.

11.3 Versäumte Mitwirkung, die zu einer Verlängerung der Lösezeit oder einem Ausfall führt, wird bei der SLA-Berechnung nicht als Ausfallzeit gewertet.

## 12. Schlussbestimmungen

12.1 Änderungen und Ergänzungen dieses SLA bedürfen der Textform.

12.2 Sollte eine Bestimmung unwirksam sein, bleibt der SLA im Übrigen wirksam.

12.3 Es gilt deutsches Recht. Gerichtsstand ist [Ort].

12.4 Abschnitt 1 „Präambel / Gegenstand" ist Bestandteil dieses SLA und hat Regelungsgehalt.

### Unterzeichnung

[Ort], den [Datum]

| Für den IT-Dienstleister | Für die Kundin oder den Kunden |
|---|---|
| _____________________________ | _____________________________ |
| [Name, Funktion] | [Name, Funktion] |

## Anlagen

**Anlage 1** — Meldewege und Kontakte: Incident-Ticket-System, E-Mail-Adressen, Telefonnummern, Dashboard-URL

**Anlage 2** — Dienste außerhalb des SLA-Anwendungsbereichs (Best-Effort-Dienste)

---

Lizenz: Apache-2.0 OR MIT.
