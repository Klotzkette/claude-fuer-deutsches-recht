---
name: avv-tom-art-32-dsgvo-anlage
description: "TOM-Anlage zum AVV nach Art. 32 DSGVO. Strukturierte Aufstellung der technischen und organisatorischen Massnahmen mit Pseudonymisierung Verschluesselung Vertraulichkeit Integritaet Verfuegbarkeit Belastbarkeit sowie regelmäßige Pruefung. Output: Strukturierte TOM-Anlage auf Deutsch."
---

# TOM-Anlage Art. 32 DSGVO

## Zweck / Purpose

Strukturierte Anlage zum AVV mit den technischen und organisatorischen Massnahmen des Auftragsverarbeiters gemaess Art. 32 DSGVO und Art. 28 Abs. 3 lit. c DSGVO. Purpose (EN): German-language TOM annex to a DPA under Article 32 GDPR.

## Wann dieses Modul hilft

- TOM-Anlage zum AVV ist zu erstellen, zu pruefen oder zu aktualisieren.
- Aufsichtsbehoerde fordert Nachweis der TOM.
- Nach Datenpanne ist die TOM-Anlage auf Aktualitaet zu pruefen.
- Bei Aenderung der Verarbeitung ist die TOM-Anlage anzupassen.

## Rechtlicher Rahmen

- Art. 32 Abs. 1 DSGVO: Geeignete TOM unter Beruecksichtigung des Stands der Technik, der Implementierungskosten und der Art, des Umfangs, der Umstaende und der Zwecke der Verarbeitung sowie der unterschiedlichen Eintrittswahrscheinlichkeit und Schwere des Risikos.
- Art. 32 Abs. 1 lit. a bis d DSGVO: Pseudonymisierung und Verschluesselung, Vertraulichkeit, Integritaet, Verfuegbarkeit, Belastbarkeit, Wiederherstellbarkeit, regelmäßige Pruefung.
- Art. 25 DSGVO: Datenschutz durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen.
- Art. 28 Abs. 3 lit. c DSGVO: TOM als Pflichtklausel im AVV.

## Ablauf / Checkliste

1. **Risikobewertung.**
 - Art der Daten (Stamm-, Verkehrs-, Inhaltsdaten, Art. 9 DSGVO).
 - Umfang und Zweck.
 - Eintrittswahrscheinlichkeit und Schwere des Risikos für Betroffene.

2. **Mindestkategorien (Art. 32 Abs. 1 DSGVO).**

 | Kategorie | Massnahmenbeispiele |
 |---|---|
 | Pseudonymisierung | Pseudonymisierung in Test- und Entwicklungsumgebungen, technische Trennung der Zuordnungstabelle |
 | Verschluesselung | TLS 1.3 in Transit; AES-256 at rest; Schluesselverwaltung HSM |
 | Vertraulichkeit | Zutrittskontrolle, Zugangskontrolle, Zugriffskontrolle, Trennungskontrolle |
 | Integritaet | Weitergabekontrolle, Eingabekontrolle, Logging, Hashfunktionen |
 | Verfuegbarkeit | Backup, RPO/RTO, Notfallplan, geo-redundante Speicherung |
 | Belastbarkeit | DDoS-Schutz, Lastverteilung, Failover-Verfahren |
 | Wiederherstellbarkeit | Backup-Tests, dokumentierte Wiederherstellungsverfahren |
 | Regelmäßige Pruefung | jaehrliche TOM-Audits, Penetrationstests, Vulnerability Scans |

3. **Organisatorische Massnahmen.**
 - Datenschutzbeauftragter, Datenschutzschulungen (jaehrlich), Vertraulichkeitsverpflichtungen, IT-Sicherheits-Richtlinie, Incident-Response-Plan, Need-to-Know-Prinzip, Berechtigungsverwaltung, Joiner-Mover-Leaver-Prozess.

4. **Zertifikate und Standards.**
 - ISO/IEC 27001:2022.
 - BSI IT-Grundschutz / BSI C5:2020 (Cloud-Spezifikum).
 - SOC 2 Type II Trust Services Criteria.
 - TISAX (Automotive).
 - PCI-DSS (Zahlungsverkehr).

5. **Sub-AV-Konsistenz.**
 - Sub-AV muessen mindestens dasselbe TOM-Niveau einhalten.
 - Vertragliche Durchleitung (Art. 28 Abs. 4 DSGVO).

## Mustertext / Template

TOM-Anlage (Strukturvorlage):

```
Anlage 2 zum Auftragsverarbeitungsvertrag
Technische und organisatorische Massnahmen (Art. 32 DSGVO)

Stand: [DATUM]
Auftragsverarbeiter: [NAME]
Pruefturnus: jaehrlich, unverzueglich bei wesentlicher Aenderung

1. Pseudonymisierung (Art. 32 Abs. 1 lit. a DSGVO)
 1.1 In Entwicklungs- und Testumgebungen werden personenbezogene Daten ausschliesslich in pseudonymisierter Form verarbeitet.
 1.2 Die Zuordnungstabelle wird getrennt gespeichert; Zugriff nur für den Datenschutzbeauftragten.

2. Verschluesselung (Art. 32 Abs. 1 lit. a DSGVO)
 2.1 In Transit: TLS 1.3 mit Forward Secrecy; SSL/TLS-Konfiguration gemaess BSI TR-02102.
 2.2 At Rest: AES-256 (CBC oder GCM) für alle Datenbanken und Backups.
 2.3 Schluesselverwaltung: HSM oder gleichwertige Loesung; jaehrliche Rotation.

3. Vertraulichkeit (Art. 32 Abs. 1 lit. b DSGVO)
 3.1 Zutrittskontrolle: physische Sicherung der Rechenzentren (24/7-Bewachung, Mehrfaktor-Zutritt).
 3.2 Zugangskontrolle: Multi-Faktor-Authentifizierung für alle priviligierten Konten.
 3.3 Zugriffskontrolle: rollenbasiertes Berechtigungsmodell, Least Privilege, periodische Rezertifizierung.
 3.4 Trennungskontrolle: mandantenfaehige Trennung; logische Trennung mit eigener Zugriffskontrolle.

4. Integritaet (Art. 32 Abs. 1 lit. b DSGVO)
 4.1 Weitergabekontrolle: dokumentierte Schnittstellen, Audit-Log für alle Datenexporte.
 4.2 Eingabekontrolle: nachvollziehbare Protokollierung aller Schreibvorgaenge auf personenbezogene Daten.
 4.3 Hash-Funktionen: SHA-256 oder besser für Integritaetspruefungen.

5. Verfuegbarkeit und Belastbarkeit (Art. 32 Abs. 1 lit. b DSGVO)
 5.1 Backup: taegliche inkrementelle Backups, woechentliche Vollbackups, Aufbewahrung 30 Tage.
 5.2 RPO (Recovery Point Objective): hoechstens 24 Stunden.
 5.3 RTO (Recovery Time Objective): hoechstens 8 Stunden für kritische Verarbeitungen.
 5.4 Geo-Redundanz: synchrone Replikation in mindestens zwei EU-Rechenzentren.
 5.5 DDoS-Schutz: vorgeschalteter Filter; SLA mit Provider.

6. Wiederherstellbarkeit (Art. 32 Abs. 1 lit. c DSGVO)
 6.1 Notfallhandbuch; Notfalluebungen mindestens jaehrlich.
 6.2 Dokumentierte Wiederherstellungsverfahren.
 6.3 Verifikation der Wiederherstellbarkeit durch tatsaechlichen Wiederherstellungstest mindestens halbjaehrlich.

7. Regelmäßige Pruefung (Art. 32 Abs. 1 lit. d DSGVO)
 7.1 Penetrationstest durch unabhaengige Dritte mindestens jaehrlich.
 7.2 Vulnerability Scan monatlich.
 7.3 ISMS-internes Audit jaehrlich; externes Audit nach ISO 27001 jaehrlich.
 7.4 TOM-Anlage wird mindestens jaehrlich auf Aktualitaet geprueft.

8. Organisatorische Massnahmen
 8.1 Datenschutzbeauftragter benannt; Kontaktangabe in Anlage 4.
 8.2 Verschwiegenheitsverpflichtung aller Mitarbeitenden (Art. 28 Abs. 3 lit. b DSGVO).
 8.3 Jaehrliche Datenschutzschulung; Schulungsnachweise vorhanden.
 8.4 Joiner-Mover-Leaver-Prozess; sofortiger Entzug der Zugriffsrechte bei Austritt.
 8.5 Incident-Response-Plan mit Meldewegen an den Verantwortlichen binnen 48 Stunden nach Kenntnis einer Datenpanne (Art. 33 DSGVO).

9. Zertifikate und Standards
 9.1 ISO/IEC 27001:2022 – Zertifizierungsdatum [DATUM], Zertifizierer [STELLE].
 9.2 BSI C5:2020 Typ 2 – Stand [DATUM].
 9.3 SOC 2 Type II – Berichtszeitraum [ZEITRAUM].

10. Sub-Auftragsverarbeiter
 10.1 Sub-AV unterliegen denselben oder gleichwertigen TOM gemaess Art. 28 Abs. 4 DSGVO.
 10.2 Sub-AV-Audits werden auf Verlangen vorgelegt.
```

## Typische Drafting-Fehler

- TOM-Anlage als Marketingbroschuere statt konkreter Massnahmen.
- Pauschalformulierungen ("nach Stand der Technik") ohne konkrete Beschreibung.
- Keine Aktualisierung seit Vertragsschluss.
- Pseudonymisierung als Pflicht uebergangen, obwohl Art. 32 Abs. 1 lit. a DSGVO sie explizit benennt.
- Keine RPO/RTO.
- Keine Pruefturnusangaben.
- Sub-AV-Konsistenz nicht adressiert.

## Querverweise

- `datenschutzrecht/skills/avv-art-28-mindestinhalte-checkliste/SKILL.md`
- `datenschutzrecht/skills/avv-audit-und-kontrollrechte/SKILL.md`
- `datenschutzrecht/skills/avv-cloud-und-subverarbeitung-art-28-iv/SKILL.md`
- `datenschutzrecht/skills/dpa-en-tom-annex-template/SKILL.md`

## Quellen Stand 06/2026

- Art. 25, Art. 28 Abs. 3 lit. c, Art. 32 DSGVO.
- BSI TR-02102 (Kryptografische Verfahren).
- ISO/IEC 27001:2022.
- BSI C5:2020.
- SOC 2 Trust Services Criteria.
- Zitierweise: `../../../references/zitierweise.md`.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
