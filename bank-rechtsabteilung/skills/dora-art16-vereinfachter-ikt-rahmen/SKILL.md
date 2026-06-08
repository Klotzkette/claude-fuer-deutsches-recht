---
name: dora-art16-vereinfachter-ikt-rahmen
description: "DORA Artikel 16 für kleinere oder privilegierte Finanzunternehmen: vereinfachten IKT-Risikomanagementrahmen, Governance, Asset-Inventar, Need-to-use, Business Continuity, Drittparteienrisiko, Vertragslücken und Nachweisordner prüfbar machen im Bank-Rechtsabteilung."
---

# DORA Artikel 16: Vereinfachter IKT-Rahmen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Erste Weiche

| Frage | Wenn ja | Wenn nein |
| --- | --- | --- |
| Fällt das Unternehmen überhaupt unter DORA? | Finanzsektor-Scope und Institutstyp bestimmen | NIS2/BSIG, DSGVO Art. 32, Vertrags- und Organpflichten prüfen |
| Ist Artikel 16 einschlägig? | vereinfachten Rahmen prüfen | regulären Rahmen nach Art. 5 bis 15 DORA prüfen |
| Gibt es kritische oder wichtige Funktionen? | Drittparteien, BCP, Exit und Tests vertiefen | Grundrahmen trotzdem dokumentieren |
| Ist ein IKT-Drittanbieter beteiligt? | Art. 28 bis 30 DORA plus Vertrag prüfen | interne IKT-Governance reicht nicht automatisch |

## Prüfprogramm

| Baustein | Was der Skill abfragt | Output |
| --- | --- | --- |
| Governance | Leitungsorgan, Verantwortlichkeiten, Kontrollfunktionen, Ressourcen | Governance-Map und Beschlussbedarf |
| IKT-Risiko | Risikoidentifikation, Bewertung, Maßnahmen, Rest-Risiko | Risiko- und Maßnahmenregister |
| Assets | Systeme, Daten, Schnittstellen, Kritikalität, Eigentümer | Asset-Inventar-Lückenliste |
| Zugriff | Need-to-use, Adminrechte, Rezertifizierung, Segregation of Duties | IAM-Kontrollplan |
| Betrieb | Change, Patch, Schwachstellen, Logging, Backup | Betriebs-Checkliste |
| Kontinuität | Szenarien, Wiederanlauf, Tests, Krisenkommunikation | BCP/DR-Testplan |
| Drittparteien | Due Diligence, Vertrag, Subdienstleister, Monitoring, Exit | DORA-Klausel- und Registercheck |
| Nachweis | Protokolle, Reports, Schulungen, Vorfälle, Findings | Aufsichtsordner |

## Vertragscheck IKT-Drittparteien

Prüfe mindestens:

- Leistungsbeschreibung, Standorte, Datenarten, Kritikalität.
- Sicherheitsanforderungen, Schwachstellenmanagement, Incident-Meldung, Unterstützungsfristen.
- Audit-, Informations- und Zugangsrechte für Institut, Prüfer und Aufsicht.
- Unterauslagerung/Subcontracting, Informationspflichten und Widerspruchs-/Kündigungsmechanik.
- Exit, Datenrückgabe, Datenlöschung, Portabilität, Übergangsleistungen.
- Register-of-Information-Fähigkeit: Vertrag muss die DORA-Registerdaten praktisch hergeben.

## Typische Fehler

- Das Unternehmen hat ein allgemeines ISMS, aber kein DORA-taugliches IKT-Risikobild.
- Asset-Liste und Vertragsregister sprechen nicht dieselbe Sprache.
- Cloud-Vertrag enthält schöne Security-Anhänge, aber keinen realistischen Exit.
- Subdienstleister werden nur pauschal erlaubt.
- Geschäftsleitung wird informiert, aber nicht entscheidungsfähig eingebunden.
- Tests finden statt, aber Lessons Learned und Maßnahmenabschluss fehlen.

## Anschluss

Bei Bankauslagerungen `marisk-auslagerungen-at9-dora` zuschalten. Bei Cyber-Gesamtcompliance `nis2-cybersecurity-compliance:dora-finanzsektor-abgrenzung` oder `nis2-cybersecurity-compliance:dora-art16-finanzunternehmen-simplified-framework` verwenden.

