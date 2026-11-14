---
name: standardvertragsklauseln-scc-paket
description: "Für Standardvertragsklauseln-SCC-Paket: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Standardvertragsklauseln-SCC-Paket

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
