---
name: tia-zusaetzliche-schutzmassnahmen-encryption
description: "Zusaetzliche Schutzmassnahmen (Supplementary Measures) nach EDPB-Empfehlung 01/2020 Annex 2. Technische Massnahmen Verschluesselung Pseudonymisierung Split Processing Key Management; vertragliche Massnahmen Transparenzpflichten Warrant Canary; organisatorische Massnahmen Schulung Policy. Mit Use-Case-Matrix und Anforderungen an starke Verschluesselung."
---

# Zusaetzliche Schutzmassnahmen für das TIA (Schritt 4 EDPB-Roadmap)

## Zweck

Dieser Skill behandelt Schritt 4 der EDPB-Sechs-Schritte-Roadmap: die Auswahl und Bewertung zusaetzlicher Schutzmassnahmen (supplementary measures), wenn das Schutzniveau im Drittland nicht von vornherein der Union "im Wesentlichen gleichwertig" ist. Grundlage ist insbesondere Annex 2 der EDPB-Empfehlung 01/2020 mit den Use Cases 1 bis 7.

## Wann dieses Modul hilft

- Schritt 3 des TIA hat ergeben, dass Drittlandsrecht/Praxis das SCC-Schutzniveau nicht abdeckt.
- Vertragsverhandlung mit US-Anbieter; ergaenzende Schutzklauseln zu formulieren.
- Architekturentscheidung Cloud-Anbieter: technisch realisierbares Schutzmodell?
- Pruefung, ob Use Case 6 oder 7 vorliegt (keine wirksamen Massnahmen moeglich).
- Diskussion mit Anbieter, der nur vertragliche Massnahmen anbieten will.

## Rechtlicher Rahmen

- EuGH **C-311/18** Schrems II vom 16.07.2020.
- **EDPB Empfehlung 01/2020** Final 18.06.2021, **Annex 2**: Use Cases 1-7.
- Art. **32 DSGVO** (TOMs als Basisanforderung; bei Drittlandtransfer hoeher).
- Art. **25 DSGVO** (Datenschutz durch Technikgestaltung).

## Ablauf / Checkliste

### Use-Case-Bewertung Annex 2

| Use Case | Konstellation | Wirksamkeit moeglich? |
|---|---|---|
| 1 | Datenspeicherung mit Verschluesselung; Schluessel ausschliesslich beim Exporteur in der EU | Ja (effektiv) |
| 2 | Uebermittlung pseudonymisierter Daten ohne Moeglichkeit der Re-Identifizierung durch Importeur | Ja (effektiv) |
| 3 | Verschluesselter Transit für Empfaenger im Drittland mit gesetzlich geschuetztem Berufsgeheimnis | Bedingt |
| 4 | Geteilte Verarbeitung (Split Processing) mehrerer unabhaengiger Importeure | Bedingt |
| 5 | Importeur und Exporteur teilen Zugriff im EU-Gebiet; Drittlandimporteur erhaelt nur statistische Aggregate | Ja |
| 6 | Daten zur Klartextverarbeitung an Importeur im Drittland mit Zugriffsbefugnissen ohne adaequaten Schutz | Nein – keine wirksamen Massnahmen |
| 7 | Remote Access im Klartext durch Importeur im Drittland mit Zugriffsbefugnissen ohne adaequaten Schutz | Nein – keine wirksamen Massnahmen |

### Technische Massnahmen

- **Starke Verschluesselung at-rest und in-transit** (mindestens AES-256, TLS 1.3, geprueft anhand ENISA-/BSI-TR-02102).
- **Key Management ausserhalb des Drittlands**: Schluessel im EU/EWR-HSM; Importeur kann nicht entschluesseln.
- **Hold-Your-Own-Key (HYOK), Bring-Your-Own-Key (BYOK)** mit Vorbehalten – HYOK ist staerker.
- **Pseudonymisierung mit unkorrelierten Schluesseln** (Art. 4 Nr. 5 DSGVO; § 22 Abs. 2 Nr. 5 BDSG).
- **Anonymisierung**, soweit Re-Identifizierung im Drittland praktisch ausgeschlossen.
- **Split Processing / Confidential Computing** (Enclaves, TEEs) – Wirksamkeit von Implementation abhaengig.
- **Tokenisierung**, **Format-Preserving Encryption**.
- **Confidentiality Computing** (Intel SGX, AMD SEV) – noch nicht universell als alleiniger Schutz akzeptiert.

### Vertragliche Massnahmen

- Berichtspflicht zu Behördenanfragen (Art und Anzahl, soweit zulaessig); **Warrant Canary**.
- Anfechtungspflicht des Importeurs ("challenge any legally available avenue").
- Erweiterte Audit-Rechte für Exporteur und Aufsichtsbehoerde.
- Sofortige Aussetzungspflicht bei Anweisung, die nicht abgewehrt werden kann.
- Klausel zur Mitteilung bei Aenderung der Rechtslage.
- Haftungs- und Schadensersatzregelungen verstaerken.

### Organisatorische Massnahmen

- Mitarbeiterschulung mit Schwerpunkt Behördenanfragen-Reaktion.
- Standardisierte interne Pruefprozesse für eingehende Government Requests.
- Veroeffentlichte Privacy Policy / Transparenzberichte des Importeurs.
- Datenminimierung an der Quelle.
- Klare Rollendefinition: wer entscheidet Aussetzung?

### Wirksamkeitspruefung

- Schutz greift sowohl rechtlich als auch praktisch?
- Massnahmen kumulativ ausreichend, um die Garantien A bis D zu kompensieren?
- Restrisiko dokumentiert und akzeptiert?

## Mustertext / Template

Vertragsbaustein – Behördenanfragen:

> Der Datenimporteur verpflichtet sich, jede Anfrage einer staatlichen Stelle oder einer Sicherheitsbehoerde, die auf Herausgabe der uebermittelten personenbezogenen Daten oder auf direkten Zugriff hierauf gerichtet ist, unverzueglich dem Datenexporteur mitzuteilen, soweit dies rechtlich zulaessig ist. Ist die Mitteilung gesetzlich untersagt, verpflichtet sich der Datenimporteur, sich auf rechtmäßigem Wege für eine Aufhebung oder Lockerung des Verbots einzusetzen und mindestens halbjaehrlich aggregierte Statistiken zu solchen Anfragen zu veröffentlichen. Der Datenimporteur stellt sicher, dass jede Anfrage auf ihre Rechtmaessigkeit, Notwendigkeit und Verhaeltnismaessigkeit geprueft wird und dass alle rechtlichen Mittel zur Begrenzung der Datenherausgabe ausgeschoepft werden.

Technischer Baustein:

> Vor jeder Uebermittlung wird der personenbezogene Datensatz anhand des Schluessels K1 verschluesselt; K1 wird im Hardware Security Module des Exporteurs in der EU verwaltet und nicht an den Importeur uebermittelt. Der Importeur erhaelt ausschliesslich verschluesselte Datenstroeme. Eine Entschluesselung ist ohne K1 nicht moeglich. Der Importeur fuehrt keine Klartextverarbeitung durch und besitzt keine Funktion zur Entschluesselung.

## Typische Fehler

- Nur vertragliche Massnahmen ohne technische Untermauerung – EDPB-konform unzureichend bei Use Case 6/7.
- "Cloud-Anbieter-Verschluesselung" akzeptiert, obwohl Schluessel beim Anbieter im Drittland liegen.
- Pseudonymisierung "vor Ort", aber Importeur erhaelt Zuordnungsschluessel.
- TEEs / Enclaves als alleiniger Schutz angesetzt, ohne dass die Konfiguration validiert ist.
- Use Case 6/7 vorliegend, aber dennoch "Schutzmassnahmen wirken" formuliert – sachwidrig.
- Restrisiko nicht dokumentiert; Entscheider-Sign-off fehlt.
- Warrant Canary versprochen, aber kein operatives Verfahren.

## Querverweise

- `tia-edpb-roadmap-6-schritte-deutsch` für Roadmap.
- `tia-us-fisa-702-und-eo-12333-bewertung` für US-Use Case.
- `avv-tom-art-32-dsgvo-anlage` für TOMs.
- `tia-template-deutsch-vollvorlage` für Vollvorlage.

## Quellen Stand 06/2026

- EDPB Empfehlung 01/2020 Final 18.06.2021, insb. Annex 2 Use Cases.
- EDPB Empfehlung 02/2020 vom 10.11.2020 (EEG).
- EuGH C-311/18 (Schrems II) vom 16.07.2020.
- DSGVO, Art. 25, 32.
- BSI Technische Richtlinie TR-02102 (kryptografische Verfahren), aktueller Stand auf bsi.bund.de pruefen.
- ENISA Guidelines for SMEs on the security of personal data processing (Dezember 2016) und Folgepapiere.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
