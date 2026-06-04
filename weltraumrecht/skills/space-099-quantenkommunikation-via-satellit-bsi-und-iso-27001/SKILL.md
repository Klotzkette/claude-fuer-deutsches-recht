---
name: space-099-quantenkommunikation-via-satellit-bsi-und-iso-27001
description: "Quantenkommunikation via Satellit: Quantum Key Distribution QKD-Missionen und Schluesselverteilung uebersatellitisches Backbone. Klaert die Pflichten nach BSI-Gesetz NIS2-RL Geheimschutz-Verordnung GHB sowie ITU-Frequenzkoordination und Exportkontrolle (Wassenaar Arrangement EU Dual-Use VO 2021/821). Behandelt Architektur Ground Segment Sicherheitsanforderungen Beweissicherung im Zwischenfall und Versicherbarkeit. Liefert Pruefraster und Schaltbild fuer Quantenkommunikations-Mandate."
---

# Quantenkommunikation via Satellit

## Aufgabe

Skill fuer Mandate aus Quantum-Communication-as-a-Service (QCaaS), QKD-Backbone-Aufbau, Sicherheitsbehoerden, Verteidigungsministerien, Banken, Energieversorger und Forschungsinstitutionen. Anlaesse: EuroQCI-Projekt der EU, IRIS2-Konstellation, deutsche QKD-Forschungsmissionen (Quartz, QuNet), kommerzielle Pilotanwendungen im Bankenbereich.

## Sofortfragen

1. Welche Rolle: Betreiber, Bodenstationsbetreiber, Forschungsinstitut, KRITIS-Sektor-Anwender oder Aufsichtsbehoerde?
2. Welche Schluessellaenge und welcher Protokollstandard (BB84, B92, E91)?
3. Welche Frequenzbaender (Free-Space-Optical-Communication ueblich; Funklink fuer Klassisch-Channel)?
4. Welcher Sicherheitsstufe (VS-NfD, VS-Vertraulich, GEHEIM)?
5. Welche internationale Reichweite (CN/US-Export, EU-Konsortium)?

## Rechtsrahmen

- **BSI-Gesetz (BSIG)** insbesondere §§ 8a-8b (KRITIS-Pflichten) und § 8c (KRITIS-Dachgesetz) iVm KRITIS-DachG-Entwurf 2023. Quantum-Backbone als IT-Infrastruktur kritischer Versorgungssektoren ist regelmaessig KRITIS-pflichtig.
- **NIS2-Richtlinie (EU) 2022/2555**: Umsetzung in DE durch NIS2-Umsetzungsgesetz (NIS2UmsuCG, in Kraft live verifizieren). Pflichten zur Risikomanagement, Vorfallmeldung 24/72 Stunden, Aufsicht durch BSI.
- **Sicherheitsueberpruefungsgesetz (SUeG)** und **Geheimschutzhandbuch (GHB)**: bei Beschaeftigten mit VS-Berechtigung.
- **VS-NfD-Bestimmungen** fuer raumfahrtbezogene Verschluesselungstechnologie.
- **Wassenaar Arrangement** und **EU Dual-Use-Verordnung (EU) 2021/821**: Quantum-Schluesselverteilungssysteme sind unter Position 5A002 (Information Security) und Position 5A004 (Quantum Computing) listenpflichtig.
- **Telekommunikationsgesetz (TKG)** § 165 zur Sicherheit von Telekommunikationsnetzen.
- **DSGVO** Art. 32 zur Sicherheit der Verarbeitung.
- **ITU Radio Regulations**: Frequenzkoordinierung fuer Klassisch-Channel (Tracking, Telemetry, Command, Daten-Downlink).

## Architektur und Pflichtenmatrix

- **Space Segment**: QKD-Payload (z. B. Polarisationskorrelation), Pointing-System, Klassisch-Funktion fuer Schluesselauthentifikation.
- **Ground Segment**: Optische Bodenstation, Wetterabhaengigkeit, Sichtbarkeitsfenster.
- **Key Management System**: Schluesselverwertung in symmetrischer Krypto (AES-256 oder kuenftige PQC-Algorithmen).
- **Trusted Node Architecture**: in EuroQCI mehrstufiges Vertrauensmodell.
- **Sicherheitsanforderungen**: Common Criteria EAL 4+ als Minimum; bei GEHEIM-Stufe EAL 6+.

## Beweissicherung im Zwischenfall

- **Side-Channel-Angriffe** (Photon-Number-Splitting, Bright-Light-Injection): protokollarisch dokumentieren.
- **Trojan-Horse-Attacks**: Hardware-Side-Channel-Analyse vorhalten.
- **Forensik**: Roh-Photonenstatistik archivieren (mind. 12 Monate, idealerweise gesamte Missionsdauer).
- **Meldepflichten**: BSI nach NIS2; Bundesnetzagentur nach TKG § 168; bei VS-Vorfall MAD/BND-Koordination.

## Versicherbarkeit

- TLI-/IOL-Versicherung mit Sondersummen fuer kryptografische Payloads.
- Cyber-Cover-Klauseln pruefen (oft Ausschluss bei staatlich gesponserten Angriffen).
- Lloyd's LMA5403 als haufige Cyber-Ausschlussklausel.

## Pruefraster

1. KRITIS-Pflicht ausgeloest? — § 8a BSIG.
2. NIS2-Pflichten (Vorfallmeldung 24/72h, Risikomanagement)?
3. Exportkontrolle (BAFA, Dual-Use-VO)?
4. Sicherheitsueberpruefung der Mitarbeiter?
5. Frequenzlizenz BNetzA?
6. Versicherung deckt Cyber + kryptografischer Schaden?
7. Schluesselmanagement nach BSI TR-02102?

## Output

- Compliance-Memo BSIG/NIS2/SUeG/DSGVO.
- Architekturpruefraster (Trusted Node vs. End-to-End).
- Vorfallreaktionsleitfaden (24/72-h-Meldungspfad).
- Vertragsentwuerfe fuer QKD-as-a-Service B2B.
- Risiko-Cockpit fuer Aufsichtsrat.
