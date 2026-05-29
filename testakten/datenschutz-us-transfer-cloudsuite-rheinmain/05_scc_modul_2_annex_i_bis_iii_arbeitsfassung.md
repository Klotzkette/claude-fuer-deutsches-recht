# SCC Modul 2: Annex I-III Arbeitsfassung

Dokumenttyp: Interne Arbeitsfassung, nicht unterschriftsersetzend
Stand: 18.05.2026

## 1. Modulwahl

Für die Kernverarbeitung CloudSuite Assist wird **Modul 2** der EU-Standardvertragsklauseln 2021/914 gewählt: Verantwortlicher in der EU übermittelt Daten an einen Auftragsverarbeiter in einem Drittland.

Begründung:

- RheinMain Präzisionstechnik entscheidet über Zwecke und Mittel der CRM- und Supportverarbeitung.
- CloudSuite Assist Inc. verarbeitet die Daten nach Weisung zur Bereitstellung der SaaS-Plattform.
- CloudSuite Ireland Ltd. ist Vertragspartnerin, aber die US-Gesellschaft erhält Zugriff und verarbeitet Telemetrie.

Für NorthPeak Analytics LLC ist zu prüfen, ob CloudSuite Assist Inc. diese als Unterauftragsverarbeiter einbindet (dann Modul 3 in der Anbieter-Kette) oder ob RheinMain eine direkte funktionale Beauftragung vornimmt (dann Modul 2).

## 2. Annex I.A Parteien

**Datenexporteur:**
RheinMain Präzisionstechnik GmbH, Hanauer Landstraße 188, 60314 Frankfurt am Main.
Kontakt Datenschutz: datenschutz@rheinmain-pt.example.

**Datenimporteur:**
CloudSuite Assist Inc., 221 Harbor Street, San José, CA 95113, USA.
Kontakt Datenschutz: privacy@cloudsuite-assist.example.

## 3. Annex I.B Beschreibung der Übermittlung

| Kategorie | Beschreibung |
|---|---|
| Betroffene Personen | B2B-Kundenkontakte, Lieferantenkontakte, Interessenten, Serviceansprechpartner |
| Datenkategorien | Name, geschäftliche Kontaktdaten, Unternehmen, Funktion, Kommunikationsinhalte, Ticketverlauf, Maschinenseriennummer, Logdaten |
| Sensible Daten | Nicht vorgesehen; Freitext kann zufällige Gesundheits- oder HR-Angaben enthalten |
| Zweck | CRM, Support, Ersatzteilkoordination, KI-gestützte Antwortvorschläge |
| Häufigkeit | Kontinuierlicher SaaS-Betrieb; US-Supportzugriff anlassbezogen |
| Speicherdauer | Nach Löschkonzept RheinMain; Telemetrie 180 Tage; Backups 35 Tage |
| Subprozessoren | MainRack GmbH, NorthPeak Analytics LLC, TicketForge LLC |

## 4. Annex I.C Zuständige Aufsichtsbehörde

Hessischer Beauftragter für Datenschutz und Informationsfreiheit, soweit RheinMain Präzisionstechnik GmbH Hauptniederlassung und Entscheidungszentrum in Hessen hat.

## 5. Annex II Technische und organisatorische Maßnahmen

| Maßnahme | Anbieterangabe | Bewertung RheinMain |
|---|---|---|
| Transportverschlüsselung | TLS 1.3 | Plausibel, Zertifikatspinning nicht erforderlich |
| Verschlüsselung ruhender Daten | AES-256 | Nachweis aus Security Addendum vorhanden |
| Key Management | Kundenschlüssel optional, Standard: Anbieter-KMS | Für ReplyPilot EU-kontrollierte Schlüssel prüfen |
| Zugriffskontrolle | MFA, rollenbasiert, JIT-Supportzugriff | Supportfreigabe protokollieren und monatlich prüfen |
| Logging | Admin- und Supportzugriffe 365 Tage | Exportrecht für Audit klären |
| Pseudonymisierung | Ticket-ID statt Klarnamen in Telemetrie teilweise | Freitextmaskierung vor ReplyPilot fehlt |
| Government Access | Policy: notification and challenge where legally permitted | Transparenzbericht 2025 anfordern |
| Löschung | API und Admin-Konsole | Testlöschung halbjährlich |

## 6. Annex III Unterauftragsverarbeiter

Siehe `08_subprocessor_map.csv`. Offen ist, ob TicketForge LLC nur Notfall-Wartung oder regulären Zugriff erhält. Bis zur Klärung darf TicketForge nicht als vollständig bewertet gelten.

## 7. Lückenliste SCC

| Lücke | Gewicht | Maßnahme |
|---|---|---|
| ReplyPilot im Produkt-Scope unklar | Hoch | Anbieterbestätigung und TIA-Nachtrag |
| Annex II Key Management zu allgemein | Mittel | EU-Key-Option oder zusätzliche Verschlüsselung prüfen |
| Subprozessor TicketForge unklar | Hoch | Rollen- und Zugriffsbeschreibung anfordern |
| Kein archivierter DPF-Abruf bei Vertragsschluss | Mittel | Aktuellen Abruf archivieren und Review-Kalender setzen |
