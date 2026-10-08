# Transfer Impact Assessment für SCC-Drittlandtransfer

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Aktenbestandteil für externe Herausgabe]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Datenflüsse, die Dienstleisterauskünfte und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne Drittlandrecht, Technik und tatsächliche Zugriffslage zu prüfen, hat noch kein verwendbares Dokument, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Rubrum, Assessment-Stelle und Prüffassung

### TRANSFER IMPACT ASSESSMENT FÜR SCC-DRITTLANDTRANSFER

Assessment-ID: [TIA-Nummer].

Exporteur: [Name, Rechtsform, Anschrift, Rolle als Verantwortlicher oder Auftragsverarbeiter].

Importeur: [Name, Rechtsform, Anschrift, Drittland, Rolle].

SCC-Modul: [Modul 1 Verantwortlicher an Verantwortlichen / Modul 2 Verantwortlicher an Auftragsverarbeiter / Modul 3 Auftragsverarbeiter an Auftragsverarbeiter / Modul 4 Auftragsverarbeiter an Verantwortlichen].

#### 1. Transferbeschreibung

1.1 Der Transfer betrifft [System, Dienst, Schnittstelle] und dient [konkreter Zweck]. Ohne diesen Transfer wäre [fachlicher oder technischer Nachteil] zu erwarten; gleichwertige Verarbeitung ohne Drittlandbezug wurde geprüft und [verworfen aus Gründen / als zumutbare Alternative gewählt].

1.2 Übertragen oder zugänglich gemacht werden [Datenkategorien]. Besonders schutzbedürftig sind [Art. 9 DSGVO-Daten / Beschäftigtendaten / Kommunikationsinhalte / Kinder- oder Patientendaten / Zugangsdaten / keine besonders kritischen Kategorien].

1.3 Der Importeur erhält [dauerhafte Speicherung / temporäre Verarbeitung / reinen Fernzugriff / Supportzugriff nach Ticketfreigabe / Backup-Verarbeitung / Protokolldatenzugriff].

1.4 Weiterübermittlungen sind beschränkt auf [freigegebene Unterauftragsverarbeiter, Länder und Funktionen]. Jede weitere Übermittlung setzt [vorherige Textformfreigabe / aktualisierte Unterauftragsliste mit Widerspruchsfrist / neues TIA] voraus.

#### 2. Transferinstrument und Vertragslage

2.1 Die Parteien verwenden die EU-Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/914 in der Fassung vom [Datum der Unterzeichnung] mit dem in diesem Assessment bezeichneten Modul.

2.2 Die SCC-Anlagen enthalten [Parteienliste, Beschreibung des Transfers, technische und organisatorische Maßnahmen, Unterauftragsverarbeiterliste, zuständige Aufsichtsbehörde]. Fehlende oder pauschale Anlagen werden vor Produktivstart ersetzt.

2.3 Der Importeur hat bestätigt, dass er [keine rechtlichen Gründe sieht, die SCC einzuhalten / folgende rechtliche Einschränkungen sieht: Beschreibung / folgende Behördenzugriffe in den letzten Jahren erhalten hat: Anzahl, Art, Zeitraum].

#### 3. Drittlandrecht und Zugriffswahrscheinlichkeit

3.1 Maßgeblich ist das Recht von [Zielland] einschließlich [Überwachungsrecht, Strafprozessrecht, Nachrichtendienstrecht, Telekommunikationsrecht, Cloud- oder Plattformregulierung].

3.2 Für den konkreten Transfer ist relevant, ob Behörden Zugriff verlangen können auf [Inhaltsdaten / Metadaten / gespeicherte Dateien / Administrationsprotokolle / Verschlüsselungsschlüssel / Support-Tickets].

3.3 Die Zugriffswahrscheinlichkeit wird wie folgt bewertet: [niedrig, weil Daten stark pseudonymisiert und für Behördenzwecke wenig aussagekräftig sind / mittel, weil der Importeur regulierter Kommunikations- oder Cloud-Anbieter ist / hoch, weil sensible Inhaltsdaten in Klartext im Drittland gespeichert werden].

3.4 Für US-Transfers außerhalb einer vollständig einschlägigen DPF-Listung wird dokumentiert, ob und in welchem Umfang die im Angemessenheitsbeschluss zum EU-US Data Privacy Framework beschriebenen Schutzmechanismen für den konkreten Importeur und das gewählte Transferinstrument berücksichtigt werden können.

#### 4. Ergänzende technische Maßnahmen

4.1 Verschlüsselung: [Daten werden vor Transfer mit Schlüsselverwaltung ausschließlich im EWR verschlüsselt / Daten werden während Transport und Speicherung verschlüsselt, Schlüssel liegen jedoch beim Importeur / keine wirksame Verschlüsselung, Begründung].

4.2 Pseudonymisierung: [Daten werden vor Transfer so pseudonymisiert, dass der Importeur ohne separat im EWR gehaltene Zusatzinformationen keine Re-Identifizierung vornehmen kann / nur organisatorische Maskierung / keine Pseudonymisierung möglich, Begründung].

4.3 Zugriffskontrolle: [rollenbasierte Freigabe / Just-in-Time-Zugriff / Ticketbindung / Mehr-Faktor-Authentifizierung / Vier-Augen-Freigabe / Protokollierung mit monatlicher Prüfung].

4.4 Datenminimierung: [nur folgende Felder werden übertragen: Liste; Freitextfelder ausgeschlossen; Anhänge ausgeschlossen; Löschfrist; Exportfilter].

#### 5. Ergänzende vertragliche und organisatorische Maßnahmen

5.1 Der Importeur verpflichtet sich, rechtswidrige oder unverhältnismäßige Behördenanfragen rechtlich zu prüfen, soweit zulässig anzufechten und den Exporteur unverzüglich zu informieren, soweit ein gesetzliches Verbot nicht entgegensteht.

5.2 Der Importeur legt mindestens jährlich [Transparenzbericht / Behördenanfragenstatistik / Auditbericht / ISO- oder SOC-Nachweis / Lösch- und Zugriffsnachweis] vor.

5.3 Der Exporteur führt [jährliche Nachprüfung / anlassbezogene Nachprüfung bei Gesetzesänderung / Nachprüfung bei neuem Unterauftragsverarbeiter / Nachprüfung bei Sicherheitsvorfall] durch.

#### 6. Restrisiko und Entscheidung

6.1 Nach Umsetzung der Maßnahmen verbleibt folgendes Restrisiko: [niedrig / mittel / hoch] wegen [konkrete Gründe].

6.2 Der Transfer wird [freigegeben / unter Auflagen freigegeben / abgelehnt / bis zur technischen Nachrüstung ausgesetzt].

6.3 Auflagen: [SCC-Anlagen vervollständigen; Schlüsselverwaltung verlagern; Unterauftragnehmer streichen; DPF-Status zusätzlich prüfen; Betroffeneninformation aktualisieren; Löschtest durchführen; Exportumfang reduzieren].

6.4 Wird eine Auflage nicht bis [Datum] erfüllt, endet die Freigabe automatisch und der Transfer ist technisch zu sperren.

#### 7. Nachprüfung

7.1 Nächste reguläre Nachprüfung: [Datum].

7.2 Anlassbezogene Nachprüfung bei [Änderung des Ziellandrechts; Änderung des Dienstes; neuer Unterauftragsverarbeiter; Verlust von DPF-Zertifizierung; Behördenzugriff; Sicherheitsvorfall; neue EDSA- oder Behördenleitlinie].

#### 8. Freigabe

[Ort], den [Datum]

| Datenschutz | IT-Sicherheit | Fachbereich |
|---|---|---|
| _____________________________ | _____________________________ | _____________________________ |
| [Name, Funktion] | [Name, Funktion] | [Name, Funktion] |

### Anlage 1 — Prüf- und Bewertungsschema

1. Zweck und Prüfstand

1.1 Dieses Schema führt das Assessment als fünfstufige Prüfung von der Rechtsgrundlage bis zur Dokumentation; jede Stufe wird nur bei tragfähigem Ergebnis der vorherigen erreicht, und jeder Befund nennt seine Quelle.

1.2 Assessment-ID: [TIA-Nummer]; Prüfdatum: [JJJJ-MM-TT]; prüfende Person: [Name, Funktion].

2. Stufe 1 — Rechtsgrundlage und Erforderlichkeit

2.1 Die Ausgangsverarbeitung ist gerechtfertigt nach [Art. 6 Abs. 1 DSGVO, Buchstabe], bei besonderen Kategorien zusätzlich nach [Art. 9 Abs. 2 DSGVO, Buchstabe]; die Alternativenprüfung nach Ziffer 1.1 des Assessments (Verarbeitung ohne Drittlandbezug) ist dokumentiert.

2.2 Befund Stufe 1: [tragfähig / nicht tragfähig — Prüfung endet].

3. Stufe 2 — Transferinstrument

3.1 Das SCC-Modul passt zur tatsächlichen Rollenverteilung von Exporteur und Importeur; die Anlagen I bis III sind konkret ausgefüllt und nicht pauschal; Unterzeichnungsdatum: [Datum].

3.2 Die Importeur-Bestätigungen nach Ziffer 2.3 des Assessments liegen schriftlich vor; Auffälligkeiten [bisherige Behördenzugriffe, rechtliche Einschränkungen]: [keine / Beschreibung].

3.3 Befund Stufe 2: [Instrument trägt / Instrument trägt mit Nachbesserung der Anlagen / Instrument trägt nicht].

4. Stufe 3 — Recht und Praxis des Ziellands

4.1 Die einschlägigen Zugriffsregime des Ziellands sind je Datenart bewertet (Inhaltsdaten, Metadaten, Schlüssel, Protokolle) anhand von [Gesetzesquellen, Transparenzberichten, Importeur-Auskünften, veröffentlichter Behördenpraxis] (Suchanker für die Live-Recherche: EuGH Schrems II ergänzende Maßnahmen; EDSA Empfehlungen 01/2020 wesentliche Garantien).

4.2 Die Zugriffswahrscheinlichkeit nach Ziffer 3.3 des Assessments ist mit Tatsachen begründet und nicht nur behauptet; Quellenliste: [Aufzählung mit Abrufdatum].

4.3 Befund Stufe 3: [keine relevante Beeinträchtigung / Beeinträchtigung möglich — Stufe 4 zwingend / Beeinträchtigung gravierend — Freigabe nur bei technisch ausgeschlossenem Zugriff].

5. Stufe 4 — Ergänzende Maßnahmen

5.1 Technische Maßnahmen nach Abschnitt 4 des Assessments: Wirksamkeit gegen die in Stufe 3 festgestellten Szenarien je Maßnahme [Verschlüsselung mit Schlüsselhoheit im EWR: wirksam / unwirksam; Pseudonymisierung: wirksam / unwirksam; Zugriffskontrolle: unterstützend; Datenminimierung: unterstützend].

5.2 Vertragliche und organisatorische Maßnahmen nach Abschnitt 5: [Anfechtungspflicht, Informationspflicht, Transparenzbericht, Nachprüfung] — als alleinige Absicherung [ausreichend / nicht ausreichend, nur ergänzend].

5.3 Befund Stufe 4: [Schutzniveau hergestellt / hergestellt nur für reduzierten Datenumfang / nicht herstellbar — keine Freigabe].

6. Stufe 5 — Dokumentation und Folgeprozesse

6.1 SCC samt Anlagen, Importeur-Bestätigungen, Quellenliste, Betroffeneninformation, Verzeichnis der Verarbeitungstätigkeiten und Transferregister sind abgelegt unter [Fundstellen].

6.2 Auflagen aus Ziffer 6.3 des Assessments sind mit Verantwortlichem, Frist und automatischer Sperrfolge nach Ziffer 6.4 erfasst: [Auflage, Name, Datum].

6.3 Gesamtergebnis der Stufenprüfung: [Freigabe / Freigabe unter Auflagen / Aussetzung / Ablehnung]; nächste Nachprüfung: [Datum]; Vermerk: [Ort, Datum, Name, Funktion].

---

Lizenz: Apache-2.0 OR MIT.
