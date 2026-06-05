---
name: inv-whistleblower-forensic
description: "Inv 013 Whistleblower, Inv 015 Forensic Imaging: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 013 Whistleblower, Inv 015 Forensic Imaging

## Arbeitsbereich

Dieser Skill bündelt **Inv 013 Whistleblower, Inv 015 Forensic Imaging** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-013-whistleblower` | Bewertet Whistleblower-Meldungen rechtssicher – HinSchG 2023, EU-Richtlinie 2019/1937, Schutzumfang, Meldestellen und Reaktionspflichten. |
| `inv-015-forensic-imaging` | Leitet forensische Sicherung von IT-Systemen an – Imaging-Standards, Chain of Custody, Hash-Werte, Zulässigkeit und DSGVO-Konformität. |

## Arbeitsweg

Für **Inv 013 Whistleblower, Inv 015 Forensic Imaging** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-013-whistleblower`

**Fokus:** Bewertet Whistleblower-Meldungen rechtssicher – HinSchG 2023, EU-Richtlinie 2019/1937, Schutzumfang, Meldestellen und Reaktionspflichten.

# Whistleblower-Schutz und -Management

## Rechtlicher Rahmen

Das Hinweisgeberschutzgesetz (HinSchG 2023, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/)) und die zugrundeliegende EU-Richtlinie 2019/1937 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1937)) schaffen erstmals einen umfassenden gesetzlichen Schutz für Hinweisgeber in Deutschland. Unternehmen ab 50 Mitarbeitern sind verpflichtet, interne Meldekanäle einzurichten (§ 12 HinSchG). Repressalien gegen Hinweisgeber sind verboten und lösen Schadensersatzansprüche aus (§ 36 HinSchG). Der BGH hat bereits vor HinSchG einen arbeitsrechtlichen Schutz für Whistleblower entwickelt, der Kündigungen aufgrund von Strafanzeigen einschränkt.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass Whistleblower-Meldungen rechtskonform entgegengenommen, bewertet und bearbeitet werden, ohne dass das Unternehmen Repressalienschutz-Pflichten verletzt, und analysiert, ob eine Meldung eine Internal Investigation auslöst.

## Arbeitsprogramm

### 1. HinSchG – Pflichten des Unternehmens
- § 12 HinSchG: Pflicht zur Einrichtung interner Meldekanäle (ab 50 Mitarbeiter); Frist bereits abgelaufen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/__12.html)).
- § 13 HinSchG: Anforderungen an die Meldestelle (Vertraulichkeit, Unabhängigkeit, Reaktionspflicht).
- § 17 HinSchG: Meldestellenperson muss Meldungen bestätigen (7 Tage) und Rückmeldung geben (3 Monate).
- § 16 HinSchG: Vertraulichkeit der Identität des Hinweisgebers; keine Offenbarung ohne Einwilligung.

### 2. Schutzumfang für Hinweisgeber
- § 33 HinSchG: Verbot von Repressalien (Kündigung, Abmahnung, Degradierung, Mobbing).
- § 36 HinSchG: Schadensersatzanspruch des Hinweisgebers bei Repressalien; Beweislastumkehr zugunsten des Hinweisgebers.
- § 35 HinSchG: Strafbarkeit von Repressalien (bis 50.000 EUR Bußgeld).
- Schutz gilt auch bei anonymer Meldung (§ 27 HinSchG: Bearbeitung anonymer Meldungen empfohlen).

### 3. Sachlicher Anwendungsbereich
- § 2 HinSchG: Schutz bei Verstößen gegen EU-Recht (FCPA, MAR, DSGVO, Kartellrecht) und deutsches Strafrecht.
- Kein Schutz bei reinen Arbeitszeitbeschwerden oder persönlichen Konflikten ohne Gesetzesbezug.
- Beweislast für den Gesetzesbezug liegt zunächst beim Unternehmen, wenn es die Schutzwürdigkeit bestreitet.

### 4. Externe Meldekanäle
- § 19 HinSchG: Hinweisgeber kann auch an externe Meldestellen gehen (Bundesamt für Justiz, BaFin, Bundeskartellamt).
- Kein Vorzug interner vor externer Meldung zwingend – Hinweisgeber hat freie Wahl.
- SEC Whistleblower Program: US-amerikanische Hinweisgeber können FCPA-Verstöße direkt bei SEC melden (21 U.S.C. § 78u-6); Prämie bis 30 % der Sanktion.

### 5. Reaktion auf Whistleblower-Meldung
- Eingangsbestätigung innerhalb von 7 Tagen (§ 17 Abs. 1 HinSchG).
- Prüfung der Meldung auf Plausibilität; Entscheidung über Internal Investigation auslösen.
- Keine Offenbarung der Identität ohne zwingenden Grund.
- Dokumentation aller Maßnahmen (Audit Trail).
- Rückmeldung an Hinweisgeber spätestens nach 3 Monaten (§ 17 Abs. 2 HinSchG).

### 6. Rechtsprechung vor HinSchG
- BGH, Urt. v. 3.7.2003 – I ZR 4/01: Anzeige einer Straftat durch Arbeitnehmer ist grundsätzlich zulässig, kein Treuepflichtverstoß.
- BVerfG, Beschl. v. 2.7.2001 – 1 BvR 2049/00: Schutz der Meinungsfreiheit auch für innerbetriebliche Kritik.
- EGMR, Urt. v. 21.7.2011 – 28274/08 (Heinisch/Deutschland): Whistleblowing als EMRK Art. 10-Schutz.

### 7. Konflikte mit GeschGehG
- Offenbarung von Geschäftsgeheimnissen durch Whistleblower: § 5 Nr. 2 GeschGehG schützt, wenn zur Aufdeckung rechtswidrigen Verhaltens nötig.
- HinSchG ergänzt GeschGehG: Whistleblower-Schutz hat Vorrang vor Geheimnisschutz, wenn Meldung in gutem Glauben erfolgt.

## Red-Team-Fragen

- Hat das Unternehmen einen funktionsfähigen internen Meldekanal eingerichtet, der den HinSchG-Anforderungen entspricht?
- Wurde die Identität des Hinweisgebers geschützt – insbesondere bei der Weitergabe der Meldung an die Untersuchungskommission?
- Gibt es Anzeichen für Repressalien gegen den Hinweisgeber? Beweislastumkehr im Blick behalten!
- Hat der Hinweisgeber bereits extern (BaFin, SEC) gemeldet – und wenn ja, was bedeutet das für das Timing der internen Untersuchung?
- Ist die Meldung inhaltlich plausibel und von § 2 HinSchG erfasst?
- Wurde die 3-Monats-Rückmeldepflicht eingehalten?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| HinSchG §§ 12–17 | Interne Meldestellen, Verfahren | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |
| HinSchG § 33 | Repressalienverbot | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |
| HinSchG § 36 | Schadensersatz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |
| § 5 GeschGehG | Whistleblower-Ausnahme | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/) |
| EU-RL 2019/1937 | Whistleblower-Richtlinie | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1937) |

## Ausgabeformate

- **Meldestellen-Setup-Checkliste** (HinSchG-Anforderungen)
- **Eingangsbestätigung** (Mustertext, § 17 HinSchG)
- **Bewertungsmatrix** für Whistleblower-Meldungen (Plausibilität, Anwendungsbereich, Handlungsbedarf)
- **Repressalien-Risikoanalyse**
- **Rückmeldung an Hinweisgeber** nach 3 Monaten (Mustertext)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-015-forensic-imaging`

**Fokus:** Leitet forensische Sicherung von IT-Systemen an – Imaging-Standards, Chain of Custody, Hash-Werte, Zulässigkeit und DSGVO-Konformität.

# Forensic Imaging und IT-Datensicherung

## Rechtlicher Rahmen

Forensic Imaging ist die Erstellung einer bit-genauen Kopie eines digitalen Datenträgers, um Beweise integer zu sichern. Es unterliegt keiner spezifischen deutschen Gesetzesnorm, muss aber DSGVO-konform sein (§ 26 BDSG, Art. 5 Abs. 1 lit. c DSGVO – Datenminimierung) und den technischen Standard ISO/IEC 27037 (Guidelines for identification, collection, acquisition and preservation of digital evidence) einhalten. Bei fehlerhafter Durchführung drohen Beweisverwertungsverbote, und die Integrität des gesamten Ermittlungsergebnisses kann in Frage gestellt werden.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass forensische Sicherungsmaßnahmen technisch korrekt, rechtlich zulässig und beweissicher durchgeführt werden.

## Arbeitsprogramm

### 1. Vorbereitung und Rechtsgrundlage
- DSGVO-Rechtsgrundlage für die Verarbeitung der gesicherten Daten (§ 26 BDSG bei Beschäftigtendaten; Art. 6 Abs. 1 lit. f DSGVO).
- Verhältnismäßigkeit: Ist ein vollständiges Disk-Image erforderlich, oder reicht Selective Collection?
- Betriebsratszustimmung (§ 87 Abs. 1 Nr. 6 BetrVG) bei systematischer Überwachung prüfen.
- Auftragserteilung an externen IT-Forensiker: NDA und Auftragsverarbeitungsvertrag (Art. 28 DSGVO) abschließen.

### 2. Forensic-Imaging-Standard
- **Write-Blocker**: Hardware-Write-Blocker verwenden, um keine Spuren auf dem Original zu hinterlassen.
- **Hash-Werte**: SHA-256-Hash von Originalmedium und Image berechnen; Übereinstimmung dokumentiert Integrität.
- **Image-Format**: EnCase (E01), FTK-Image, DD-Format – dokumentieren, welches Format und welche Software verwendet wurde.
- **Dokumentation**: Gerätebeschreibung (Seriennummer, Hersteller, Modell), Zeitstempel, Name des Forensikers, Zeuge.
- ISO/IEC 27037: Identifikation → Sicherung → Dokumentation → Übergabe.

### 3. Chain of Custody
- Jeder Zugriff auf das Originalmedium und das Image wird protokolliert (wer, wann, warum).
- Physische Sicherung: Image auf verschlüsseltem Datenträger in versiegeltem Behälter.
- Keine Auswertung des Originals – nur des Images.
- Für gerichtliche Verwertung: Chain-of-Custody-Protokoll als Anlage zum Ermittlungsbericht.

### 4. Scope: Vollbild vs. gezielte Sicherung
- Vollständiges Disk-Image: höchste Beweissicherung, aber datenschutzrechtlich eingriffsintensiver.
- Selective Collection (z. B. nur bestimmte Ordner, Dateitypen, Zeiträume): datenschutzfreundlicher, aber Beweislücken möglich.
- Keyword-Suche auf Image: erstes Selektionsmittel; Liste der Keywords dokumentieren und begründen.
- Responsive vs. non-responsive Dokumente trennen (für US-Discovery relevant).

### 5. Besondere Datenträger
- **Mobile Devices**: Chip-off, JTAG oder forensische Software (Cellebrite, Oxygen Forensics) – Passwortschutz und Verschlüsselung beachten (vgl. inv-018-mobile-devices).
- **Cloud-Dienste**: Exportfunktionen nutzen (Google Workspace, M365 eDiscovery); Drittstaatentransfer prüfen.
- **Encrypted Devices**: BitLocker/FileVault – Schlüssel bei IT sichern oder Entschlüsselungshilfe vom Gerätehersteller anfordern.
- **Collaboration Tools**: Teams-Compliance-Center, Slack eDiscovery API.

### 6. DSGVO-Anforderungen bei der Auswertung
- Keine Auswertung privater Kommunikation, wenn private Nutzung erlaubt oder unklar ist.
- Filter für private E-Mails/Dokumente vor Übergabe an Rechtsanwalt einsetzen.
- Drittbetroffene (Kunden, Geschäftspartner): personenbezogene Daten minimieren.
- Löschkonzept: wann werden forensische Images vernichtet?

### 7. Dokumentation für den Bericht
- Forensik-Summary: welche Systeme, welche Zeiträume, welche Keywords, Treffer-Übersicht.
- Nicht verwertbare Dateien dokumentieren (defekte Sektoren, verschlüsselte Bereiche).
- Expert Witness Report für US-Discovery oder Strafverfahren.

## Red-Team-Fragen

- Wurden Write-Blocker verwendet und dokumentiert?
- Stimmen Hash-Werte von Original und Image überein?
- Ist die Chain of Custody lückenlos – insbesondere bei Übergabe an externe Berater?
- Wurden private Kommunikationsdaten gefiltert, bevor der Forensiker die Auswertung begann?
- Ist der IT-Forensiker nach ISO/IEC 27037 oder einem vergleichbaren Standard zertifiziert?
- Gibt es Datenschutzbedenken beim Transfer forensischer Images an US-Counsel oder US-Behörden?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| Art. 5 DSGVO | Datenminimierung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 28 DSGVO | Auftragsverarbeitung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |

## Ausgabeformate

- **Forensik-Auftragsvorlage** (Scope, Standards, NDA, Art. 28 DSGVO)
- **Chain-of-Custody-Protokoll**
- **Forensik-Summary-Vorlage**
- **DSGVO-Konformitätsprüfung** für Forensic Imaging
- **Expert Witness Report** (Vorlage für US-Discovery)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
