---
name: standardvertragsklauseln-scc-paket
description: "Standardvertragsklauseln für Drittlandtransfers nach Art. 46 DSGVO vorbereiten: SCC-Modulwahl 1-4, Annex I-III, Subprozessoren, TOMs, AVV-Schnittstelle, TIA-Andockung, Signatur- und Behördenpaket ohne Veränderung der offiziellen Klauseln."
---

# Standardvertragsklauseln-SCC-Paket

## Zweck

Dieser Skill erstellt ein praxistaugliches SCC-Arbeitspaket für Drittlandtransfers. Er wählt das richtige Modul, bereitet die Anlagen vor, verbindet die SCC mit AVV/DPA, TIA und Subprozessoren und erzeugt eine unterschriftsreife Dokumentationsstruktur.

**Wichtig:** Die offiziellen Standardvertragsklauseln der EU-Kommission werden nicht umformuliert. Das Tool erstellt Auswahl, Anlagen, Begleitvermerk, Verhandlungs- und Lückenliste. Der endgültige Vertrag muss die offiziellen Klauseln unverändert enthalten, soweit keine zulässige Ergänzung außerhalb des Klauselkerns erfolgt.

## Einsatzfälle

- US- oder sonstiger Drittlandanbieter ist nicht oder nicht passend über einen Angemessenheitsbeschluss abgedeckt.
- DPF-Listing ist unklar, unvollständig oder nur für andere Datenkategorien einschlägig.
- AVV/DPA enthält SCC, aber Modul, Anlagen oder Subprozessoren passen nicht.
- Ein Auftragsverarbeiter nutzt Drittland-Subprozessoren.
- Ein Konzern braucht SCC für interne Transfers.
- Eine Behörde verlangt SCC-Nachweise und TIA-Dokumentation.

## Intake

| Punkt | Frage |
|---|---|
| Rollen | Wer ist Datenexporteur und wer Datenimporteur? Verantwortlicher oder Auftragsverarbeiter? |
| Transferbeziehung | Direktvertrag, Subprozessor, Konzerntransfer, Weiterübermittlung, Supportzugriff? |
| Daten | Kategorien, Art. 9 DSGVO, Beschäftigtendaten, Kinder, Mandats-/Berufsgeheimnisse |
| Zweck | Hauptverarbeitung, Support, Hosting, Analyse, KI, Sicherheit, Abrechnung |
| Länder | Importland, Subprozessorländer, Zugriffsländer |
| Dokumente | AVV/DPA, Master Service Agreement, TOMs, Subprozessorliste, Datenschutzanhang |
| Stand | Bereits unterschrieben, Entwurf, Anbieterformular, Konzernmuster, Renewal |

## Modulwahl

| Modul | Konstellation | Typisches Beispiel |
|---|---|---|
| Modul 1 | Verantwortlicher an Verantwortlichen | EU-Unternehmen übermittelt Lead-Daten an eigenständig entscheidenden US-Partner |
| Modul 2 | Verantwortlicher an Auftragsverarbeiter | EU-Unternehmen nutzt US-SaaS als Processor |
| Modul 3 | Auftragsverarbeiter an Unterauftragsverarbeiter | EU-Processor beauftragt US-Subprocessor |
| Modul 4 | Auftragsverarbeiter an Verantwortlichen | EU-Processor sendet Daten zurück/an Drittland-Controller |

Wenn mehrere Rollen nebeneinander bestehen, erstelle eine Modulmatrix. Bei Dienstleistungsketten niemals nur den ersten Transfer prüfen; Onward Transfers gesondert abbilden.

## SCC-Paketstruktur

### 1. Modul- und Parteienvermerk

Erzeuge:

- Modulentscheidung mit Begründung.
- Parteienübersicht mit Rechtsträger, Adresse, Rolle, Kontakt, Datenschutzkontakt.
- Zeichnungsbefugnis und Unterzeichner.
- Datum des Inkrafttretens und Laufzeit.

### 2. Annex I: Parteien, Beschreibung, zuständige Behörde

Annex I muss praktisch ausgefüllt sein:

- Datenexporteur und Datenimporteur.
- Kategorien betroffener Personen.
- Kategorien personenbezogener Daten.
- Sensible Daten und zusätzliche Schutzmaßnahmen.
- Häufigkeit der Übermittlung.
- Art und Zweck der Verarbeitung.
- Speicherdauer oder Kriterien.
- Unterauftragsverarbeiter und Weiterübermittlungen.
- Zuständige Aufsichtsbehörde.

### 3. Annex II: TOMs und ergänzende Maßnahmen

Strukturiere Annex II so, dass er auditierbar ist:

- Verschlüsselung in Transit und at Rest.
- Key Management, idealerweise EU/EWR-kontrolliert, wenn Risikolage das verlangt.
- Zugriffskontrolle, MFA, Least Privilege, Rollen.
- Logging, Monitoring, Alerting, Audit Trails.
- Pseudonymisierung/Maskierung.
- Mandantentrennung.
- Backup, Löschung, Rückgabe.
- Incident Response und Behörden-/Betroffenenkommunikation.
- Government-Access-Policy, Challenge-Verfahren, Transparenzberichte.

### 4. Annex III: Subprozessoren

Erstelle eine Subprozessorentabelle:

| Subprozessor | Rolle | Land | Datenarten | Zweck | Transferinstrument | TOMs | Genehmigungsstatus | Änderungsvorbehalt |
|---|---|---|---|---|---|---|---|---|

Markiere fehlende Angaben als `Blocker`, wenn dadurch die Transferkette nicht prüfbar ist.

### 5. AVV/DPA-Schnittstelle

Prüfe Konsistenz:

- Art. 28 DSGVO-Pflichten im AVV/DPA.
- Weisungsrecht, Unterstützungspflichten, Löschung/Rückgabe.
- Audit- und Informationsrechte.
- Subprozessor-Genehmigung.
- Vorrangregel bei Konflikt zwischen AVV, MSA und SCC.
- Haftung, Indemnity und technische Leistungsversprechen.

## Output

Lieferbare Dokumente:

1. **SCC-Modulmatrix** mit Entscheidung.
2. **Annex-I-Arbeitsfassung**.
3. **Annex-II-TOM-Matrix**.
4. **Annex-III-Subprozessorenliste**.
5. **Lücken- und Verhandlungsprotokoll**.
6. **Unterzeichnungscheckliste**.
7. **Behördenfähiger SCC-Deckvermerk**.
8. **TIA-Andockliste** für `us-transfer-tia-dokumentation`.

## Lückenbewertung

| Ampel | Bedeutung |
|---|---|
| Grün | Modul richtig, Anlagen vollständig, TIA vorhanden, Subprozessoren transparent |
| Gelb | Vertrag nutzbar mit Auflagen oder Nachweisen |
| Rot | Falsches Modul, fehlende Anlagen, unklare Parteien, nicht prüfbare Subprozessoren, keine ergänzenden Maßnahmen |

## Typische Fehler

- Anbieter legt SCC bei, aber Annex II enthält nur Marketing-Floskeln.
- Konzernmutter unterschreibt, tatsächlich verarbeitet eine andere US-Gesellschaft.
- Modul 2 wird verwendet, obwohl der Empfänger eigenständig über Zwecke entscheidet.
- DPF wird behauptet, aber SCC werden trotzdem als Backup benötigt, weil Transferumfang nicht abgedeckt ist.
- Subprozessorliste verweist nur auf eine URL ohne Archivierung des Stands.
- SCC werden unterschrieben, aber keine TIA-Entscheidung dokumentiert.

## Quellen und Aktualität

- Stand: 05/2026.
- DSGVO Art. 28, 44-46.
- Durchführungsbeschluss (EU) 2021/914 der Kommission zu Standardvertragsklauseln.
- EDSA Recommendations 01/2020 zu ergänzenden Maßnahmen.
- Bei US-Transfers immer mit `us-transfer-tia-dokumentation` kombinieren.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
