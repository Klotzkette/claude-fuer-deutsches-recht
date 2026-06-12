---
name: tia-zusaetzliche-schutzmassnahmen-encryption
description: "Zusaetzliche Schutzmassnahmen (Supplementary Measures) nach EDPB-Empfehlung 01/2020 Annex 2. Technische Maßnahmen Verschluesselung Pseudonymisierung Split Processing Key Management; vertragliche Maßnahmen Transparenzpflichten Warrant Canary; organisatorische Maßnahmen Schulung Policy. Mit Use-..."
---

# Zusaetzliche Schutzmassnahmen für das TIA (Schritt 4 EDPB-Roadmap)

## Wann dieses Modul hilft

- Schritt 3 des TIA hat ergeben, dass Drittlandsrecht/Praxis das SCC-Schutzniveau nicht abdeckt.
- Vertragsverhandlung mit US-Anbieter; ergaenzende Schutzklauseln zu formulieren.
- Architekturentscheidung Cloud-Anbieter: technisch realisierbares Schutzmodell?
- Prüfung, ob Use Case 6 oder 7 vorliegt (keine wirksamen Maßnahmen möglich).
- Diskussion mit Anbieter, der nur vertragliche Maßnahmen anbieten will.

## Rechtlicher Rahmen

- EuGH **C-311/18** Schrems II vom 16.07.2020.
- **EDPB Empfehlung 01/2020** Final 18.06.2021, **Annex 2**: Use Cases 1-7.
- Art. **32 DSGVO** (TOMs als Basisanforderung; bei Drittlandtransfer hoeher).
- Art. **25 DSGVO** (Datenschutz durch Technikgestaltung).

## Ablauf / Checkliste

### Use-Case-Bewertung Annex 2

| Use Case | Konstellation | Wirksamkeit möglich? |
|---|---|---|
| 1 | Datenspeicherung mit Verschluesselung; Schlüssel ausschließlich beim Exporteur in der EU | Ja (effektiv) |
| 2 | Uebermittlung pseudonymisierter Daten ohne Moeglichkeit der Re-Identifizierung durch Importeur | Ja (effektiv) |
| 3 | Verschluesselter Transit für Empfaenger im Drittland mit gesetzlich geschuetztem Berufsgeheimnis | Bedingt |
| 4 | Geteilte Verarbeitung (Split Processing) mehrerer unabhaengiger Importeure | Bedingt |
| 5 | Importeur und Exporteur teilen Zugriff im EU-Gebiet; Drittlandimporteur erhaelt nur statistische Aggregate | Ja |
| 6 | Daten zur Klartextverarbeitung an Importeur im Drittland mit Zugriffsbefugnissen ohne adaequaten Schutz | Nein – keine wirksamen Maßnahmen |
| 7 | Remote Access im Klartext durch Importeur im Drittland mit Zugriffsbefugnissen ohne adaequaten Schutz | Nein – keine wirksamen Maßnahmen |

### Technische Maßnahmen

- **Starke Verschluesselung at-rest und in-transit** (mindestens AES-256, TLS 1.3, geprueft anhand ENISA-/BSI-TR-02102).
- **Key Management ausserhalb des Drittlands**: Schlüssel im EU/EWR-HSM; Importeur kann nicht entschluesseln.
- **Hold-Your-Own-Key (HYOK), Bring-Your-Own-Key (BYOK)** mit Vorbehalten – HYOK ist staerker.
- **Pseudonymisierung mit unkorrelierten Schlüsseln** (Art. 4 Nr. 5 DSGVO; § 22 Abs. 2 Nr. 5 BDSG).
- **Anonymisierung**, soweit Re-Identifizierung im Drittland praktisch ausgeschlossen.
- **Split Processing / Confidential Computing** (Enclaves, TEEs) – Wirksamkeit von Implementation abhaengig.
- **Tokenisierung**, **Format-Preserving Encryption**.
- **Confidentiality Computing** (Intel SGX, AMD SEV) – noch nicht universell als alleiniger Schutz akzeptiert.

### Vertragliche Maßnahmen

- Berichtspflicht zu Behördenanfragen (Art und Anzahl, soweit zulässig); **Warrant Canary**.
- Anfechtungspflicht des Importeurs ("challenge any legally available avenue").
- Erweiterte Audit-Rechte für Exporteur und Aufsichtsbehoerde.
- Sofortige Aussetzungspflicht bei Anweisung, die nicht abgewehrt werden kann.
- Klausel zur Mitteilung bei Änderung der Rechtslage.
- Haftungs- und Schadensersatzregelungen verstaerken.

### Organisatorische Maßnahmen

- Mitarbeiterschulung mit Schwerpunkt Behördenanfragen-Reaktion.
- Standardisierte interne Prüfprozesse für eingehende Government Requests.
- Veroeffentlichte Privacy Policy / Transparenzberichte des Importeurs.
- Datenminimierung an der Quelle.
- Klare Rollendefinition: wer entscheidet Aussetzung?

### Wirksamkeitspruefung

- Schutz greift sowohl rechtlich als auch praktisch?
- Maßnahmen kumulativ ausreichend, um die Garantien A bis D zu kompensieren?
- Restrisiko dokumentiert und akzeptiert?

## Mustertext / Template

Vertragsbaustein – Behördenanfragen:

> Der Datenimporteur verpflichtet sich, jede Anfrage einer staatlichen Stelle oder einer Sicherheitsbehoerde, die auf Herausgabe der uebermittelten personenbezogenen Daten oder auf direkten Zugriff hierauf gerichtet ist, unverzueglich dem Datenexporteur mitzuteilen, soweit dies rechtlich zulässig ist. Ist die Mitteilung gesetzlich untersagt, verpflichtet sich der Datenimporteur, sich auf rechtmäßigem Wege für eine Aufhebung oder Lockerung des Verbots einzusetzen und mindestens halbjaehrlich aggregierte Statistiken zu solchen Anfragen zu veröffentlichen. Der Datenimporteur stellt sicher, dass jede Anfrage auf ihre Rechtmaessigkeit, Notwendigkeit und Verhältnismäßigkeit geprueft wird und dass alle rechtlichen Mittel zur Begrenzung der Datenherausgabe ausgeschoepft werden.

Technischer Baustein:

> Vor jeder Uebermittlung wird der personenbezogene Datensatz anhand des Schlüssels K1 verschluesselt; K1 wird im Hardware Security Module des Exporteurs in der EU verwaltet und nicht an den Importeur uebermittelt. Der Importeur erhaelt ausschließlich verschluesselte Datenstroeme. Eine Entschluesselung ist ohne K1 nicht möglich. Der Importeur fuehrt keine Klartextverarbeitung durch und besitzt keine Funktion zur Entschluesselung.

## Typische Fehler

- Nur vertragliche Maßnahmen ohne technische Untermauerung – EDPB-konform unzureichend bei Use Case 6/7.
- "Cloud-Anbieter-Verschluesselung" akzeptiert, obwohl Schlüssel beim Anbieter im Drittland liegen.
- Pseudonymisierung "vor Ort", aber Importeur erhaelt Zuordnungsschluessel.
- TEEs / Enclaves als alleiniger Schutz angesetzt, ohne dass die Konfiguration validiert ist.
- Use Case 6/7 vorliegend, aber dennoch "Schutzmassnahmen wirken" formuliert – sachwidrig.
- Restrisiko nicht dokumentiert; Entscheider-Sign-off fehlt.
- Warrant Canary versprochen, aber kein operatives Verfahren.

## Quellen Stand 06/2026

- EDPB Empfehlung 01/2020 Final 18.06.2021, insb. Annex 2 Use Cases.
- EDPB Empfehlung 02/2020 vom 10.11.2020 (EEG).
- EuGH C-311/18 (Schrems II) vom 16.07.2020.
- DSGVO, Art. 25, 32.
- BSI Technische Richtlinie TR-02102 (kryptografische Verfahren), aktueller Stand auf bsi.bund.de prüfen.
- ENISA Guidelines for SMEs on the security of personal data processing (Dezember 2016) und Folgepapiere.
