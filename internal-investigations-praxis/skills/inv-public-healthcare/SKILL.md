---
name: inv-public-healthcare
description: "Inv 038 Public Procurement, Inv 039 Healthcare Compliance: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 038 Public Procurement, Inv 039 Healthcare Compliance

## Arbeitsbereich

Dieser Skill bündelt **Inv 038 Public Procurement, Inv 039 Healthcare Compliance** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-038-public-procurement` | Untersucht Unregelmäßigkeiten bei öffentlichen Vergabeverfahren – GWB, VgV, Kartellrecht, Manipulationsrisiken und Konsequenzen. |
| `inv-039-healthcare-compliance` | Untersucht Healthcare-Compliance-Verstöße – § 299a/b StGB, Transparenzgesetz, AMG/HWG, Kick-Back-Verbote, FSA-Kodex und US-AKS. |

## Arbeitsweg

Für **Inv 038 Public Procurement, Inv 039 Healthcare Compliance** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-038-public-procurement`

**Fokus:** Untersucht Unregelmäßigkeiten bei öffentlichen Vergabeverfahren – GWB, VgV, Kartellrecht, Manipulationsrisiken und Konsequenzen.

# Öffentliche Vergabe und Beschaffungsmanipulation

## Rechtlicher Rahmen

Unregelmäßigkeiten bei öffentlichen Vergabeverfahren können sowohl das Unternehmen als Bieter als auch als öffentlichen Auftraggeber betreffen. Für Bieter: § 298 StGB (Wettbewerbsbeschränkende Absprachen bei Ausschreibungen, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__298.html)); § 333 StGB (Vorteilsgewährung an Amtsträger). Für den Auftraggeber: §§ 331–335 StGB (Korruption von Amtsträgern). Das vergaberechtliche Rahmenwerk folgt aus §§ 97 ff. GWB ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__97.html)), der VgV und dem UVgO. Europarechtliche Grundlage: Vergaberichtlinien RL 2014/24/EU ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014L0024)).

## Ziel dieses Skills

Dieser Skill untersucht Manipulationen in öffentlichen Vergabeverfahren und leitet die richtigen rechtlichen und compliance-seitigen Maßnahmen ab.

## Arbeitsprogramm

### 1. Tätergruppen
- **Bieter-seitig**: Absprachen zwischen Bietern (§ 298 StGB, kartellrechtlich); Bestechung von Vergabebeamten (§ 333 StGB).
- **Auftraggeber-seitig**: Vergabebeamter nimmt Vorteile an (§ 331 StGB); Spezifikationen werden zugunsten bestimmter Bieter formuliert; Ausschreibung wird unterdrückt oder verkürzt.
- **Intern**: Unternehmensmitarbeiter gibt Insider-Informationen an bevorzugten Bieter weiter.

### 2. Vergaberechtliche Red Flags (Auftraggeber)
- Ausschreibungsfrist kürzer als vergaberechtlich vorgeschrieben.
- Technische Spezifikationen, die nur ein Unternehmen erfüllen kann.
- Ausschluss offensichtlich qualifizierter Bieter ohne nachvollziehbaren Grund.
- Direktvergabe ohne Ausschreibung trotz Überschreitung der Schwellenwerte.
- Nachträgliche Vertragsänderungen, die wesentlichen Vertragsinhalt ändern (Umgehung der Ausschreibungspflicht).

### 3. Vergaberechtliche Red Flags (Bieter)
- Preis liegt weit unter Marktpreis (Unterkostenangebot; Dumping als Verdrängungsstrategie).
- Alle relevanten Bieter haben ähnliche Preise (Preisabsprache, § 1 GWB, Art. 101 AEUV).
- Deckungsangebote (cover pricing): Bieter reichen absichtlich überhöhte Angebote ein.
- Rotationsabsprachen: Bieter wechseln sich ab, wer gewinnt.

### 4. Untersuchungsschritte
- Vergabeakte anfordern: vollständige Dokumentation des Vergabeverfahrens (§ 8 VgV: Dokumentationspflicht).
- Angebotsdaten analysieren: Preise, Einreichungszeitpunkte, Dokument-Metadaten (identische Word-Vorlagen?).
- E-Mail-Kommunikation zwischen Bietern und Vergabebeamten.
- Interessenkonflikte: hat Vergabebeamter persönliche Verbindungen zu bevorzugtem Bieter?
- Externe Bewerbungen: haben andere Bieter Einspruch erhoben?

### 5. Vergaberecht-Überprüfungsverfahren
- Nachprüfungsverfahren bei Vergabekammer (§ 160 GWB, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__160.html)): für unterlegene Bieter.
- Schadensersatzklage bei schuldhafter Verletzung des Vergaberechts (§ 181 GWB).
- EU-Kommission: bei grenzüberschreitenden Verstößen gegen RL 2014/24/EU.

### 6. Strafverfolgung
- § 298 StGB: Absprachen bei Ausschreibungen; Freiheitsstrafe bis 5 Jahre.
- §§ 331–335 StGB: Korruption von Amtsträgern.
- Strafanzeige bei Staatsanwaltschaft; Bundeskartellamt bei wettbewerbsrechtlichen Komponenten.
- Kronzeugenregelung des Bundeskartellamts: wenn Preisabsprachen mit anderen Bietern.

### 7. Konsequenzen für das Unternehmen als Bieter
- Ausschluss von Vergabeverfahren (§ 123 GWB: Ausschlussgründe, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__123.html)).
- Abschöpfung von Gewinnen aus manipulierten Aufträgen.
- Schadensersatz gegenüber dem öffentlichen Auftraggeber.
- Rehabilitation durch Selbstreinigung (§ 125 GWB): Nachweis angemessener Compliance-Maßnahmen.

## Red-Team-Fragen

- Gibt es Dokument-Metadaten, die auf identische Erstellungsumgebung mehrerer Bieter hindeuten?
- Wurden Spezifikationen im Vergabeverfahren nachträglich zum Vorteil eines Bieters geändert?
- Hat das Unternehmen bei einem Misserfolg in einem Vergabeverfahren die Vergabeakte gemäß § 165 GWB eingesehen?
- Wurden alle Beteiligten an der Vergabeentscheidung auf Interessenkonflikte geprüft?
- Wenn Absprachen mit anderen Bietern vorlagen: wurde der Kronzeugenantrag beim Bundeskartellamt erwogen?
- Ist eine Selbstreinigung nach § 125 GWB möglich und sinnvoll, um Vergabeausschlüsse zu vermeiden?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 298 StGB | Wettbewerbsbeschränkende Absprachen | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__298.html) |
| §§ 97 ff. GWB | Vergaberecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__97.html) |
| § 123 GWB | Ausschlussgründe | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__123.html) |
| § 125 GWB | Selbstreinigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__125.html) |
| RL 2014/24/EU | EU-Vergaberichtlinie | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014L0024) |

## Ausgabeformate

- **Vergabeverfahren-Red-Flag-Checkliste**
- **Angebotsdaten-Analyse-Template** (Metadaten, Preiskorrelation)
- **Nachprüfungsantrag** Vergabekammer (Struktur)
- **Selbstreinigung-Dokumentation** nach § 125 GWB
- **Strafanzeige** §§ 298, 333 StGB

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-039-healthcare-compliance`

**Fokus:** Untersucht Healthcare-Compliance-Verstöße – § 299a/b StGB, Transparenzgesetz, AMG/HWG, Kick-Back-Verbote, FSA-Kodex und US-AKS.

# Healthcare-Compliance-Verstöße und Untersuchung

## Rechtlicher Rahmen

Die Pharmaindustrie und Medizinproduktehersteller unterliegen strengen Anti-Korruptions-Regelungen: §§ 299a, 299b StGB (Bestechung und Bestechlichkeit im Gesundheitswesen, eingeführt 2016; [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299a.html)) richten sich speziell gegen finanzielle Vorteile für Angehörige der Heilberufe. Hinzu kommen das AMG (Arzneimittelgesetz), das HWG (Heilmittelwerbegesetz), der FSA-Kodex (Freiwillige Selbstkontrolle für die Arzneimittelindustrie) und bei US-Bezug der Anti-Kickback Statute (42 U.S.C. § 1320a-7b) und der False Claims Act.

## Ziel dieses Skills

Dieser Skill untersucht Healthcare-spezifische Korruptionsszenarien, klärt die einschlägigen Normen und leitet Untersuchungsmaßnahmen ab.

## Arbeitsprogramm

### 1. Tatbestandsanalyse §§ 299a, 299b StGB
- § 299a StGB (Bestechlichkeit): Angehöriger eines Heilberufs fordert/annimmt Vorteil für Bezug oder Verordnung von Arznei-/Hilfsmitteln.
- § 299b StGB (Bestechung): wer einem Angehörigen eines Heilberufs einen Vorteil anbietet/verspricht/gewährt.
- Vorteil: jeder Vermögensvorteil, auch immaterielle Vorteile (Einladungen, Reisen, Vorträge ohne Gegenleistung).
- Heilberufsangehörige: Ärzte, Zahnärzte, Apotheker, Tierärzte, Hebammen.

### 2. Typische Fallkonstellationen
- **Anwendungsbeobachtungsstudien (AWB)**: Zahlungen für Patientenberichte als verdeckte Marketing-Maßnahmen.
- **Referentenhonorare**: Ärzte erhalten Honorare für Vorträge, die weit über marktüblichem Niveau liegen.
- **Kongress-Sponsoring**: Kostenübernahme für Kongressteilnahme ohne ausreichenden Zusammenhang zur beruflichen Fortbildung.
- **Rabatte und Freimuster**: über HWG § 7 erlaubte Grenzen hinaus.
- **CME-Sponsoring**: finanzielle Unterstützung für Fortbildungen mit unangemessener Gegenleistung.

### 3. Transparenz- und Meldepflichten
- FSA-Kodex 2023: Offenlegung von Zuwendungen an Angehörige der Heilberufe und Gesundheitsorganisationen (EFPIA-Transparenzregelungen).
- Transparenz-Datenbank: Erfassung aller Zahlungen und geldwerten Vorteile an HCPs (Healthcare Professionals).
- § 20 Abs. 3 BÄO, Ärztekammer-Berufsordnungen: Ärzte haben eigene Meldepflichten.
- US-Sunshine Act (42 U.S.C. § 1320a-7h): Zahlung an HCPs muss der US-Regierung gemeldet werden.

### 4. Forensische Untersuchungsmethoden
- **Zahlungsanalyse**: alle Zahlungen an HCPs (Referentenhonorare, AWBs, Advisory Boards) über definierten Zeitraum.
- **Benchmarking**: ist das Honorar für den HCP marktüblich (Fair Market Value)?
- **CRM-Daten**: Korrelation zwischen Honorarzahlungen und Verordnungsverhalten des Arztes.
- **Vergabedaten**: welche Ärzte haben nach Erhalt von Zuwendungen mehr des eigenen Produkts verschrieben?
- **Dokumentenprüfung**: Verträge für Advisory Boards, AWBs, CME-Sponsoring.

### 5. US-Anti-Kickback Statute (AKS)
- 42 U.S.C. § 1320a-7b: verbietet jede Zuwendung, die dazu dient, Überweisungen oder Verordnungen zu Medicare/Medicaid zu induzieren.
- Safe Harbors: bestimmte Konstellationen sind erlaubt (z. B. fair market value Honorare, Personal Services Arrangements).
- False Claims Act (31 U.S.C. § 3729): fehlerhafter Abrechnungsanspruch an Bundesbehörden; Qui-Tam-Klagen von Whistleblowern.
- DOJ-Healthcare-Fraud-Settlements: hohe Geldstrafen; Corporate Integrity Agreements (CIA).

### 6. Behördenstrategie und Selbstanzeige
- Staatsanwaltschaft: §§ 299a/b StGB; Ermittlungen gegen Pharmaunternehmen und Ärzte.
- BaFin: wenn Kapitalmärkte betroffen (Falschinformationen über Studienergebnisse).
- FSA-Schiedsgericht: brancheninterne Beschwerden.
- US-DOJ: bei FCPA/AKS-Bezug; Voluntary Disclosure.

### 7. Compliance-Programm
- SOPs für alle HCP-Interaktionen (Honorare, AWBs, CME).
- Fair-Market-Value-Datenbank für Honorar-Benchmarking.
- Pre-Approval-Prozess für alle Zahlungen über Schwellenwert.
- Training für Sales-Force und Medical-Affairs.
- Monitoring: stichprobenartiger Review aller HCP-Zahlungen.

## Red-Team-Fragen

- Ist die Korrelation zwischen Honorarzahlungen und Verordnungsverhalten dokumentiert und analysiert worden?
- Sind alle HCP-Zahlungen im FSA-Transparenzbericht korrekt ausgewiesen?
- Werden Fair-Market-Value-Benchmarks für Referentenhonorare tatsächlich angewandt?
- Gibt es AWBs, bei denen die wissenschaftliche Substanz so gering ist, dass sie als verdecktes Marketing qualifizieren?
- Wurden Hochrisikoärzte (hohe Zahlungen + hohe Verordnungsvolumina) im Rahmen der internen Untersuchung identifiziert?
- Ist ein US-AKS-Exposure vorhanden, und wurde das DOJ-Voluntary-Disclosure erwogen?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 299a StGB | Bestechlichkeit Heilberufe | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299a.html) |
| § 299b StGB | Bestechung Heilberufe | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299b.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |
| 42 U.S.C. § 1320a-7b | Anti-Kickback Statute | US Government |
| 31 U.S.C. § 3729 | False Claims Act | US Government |

## Ausgabeformate

- **HCP-Zahlungsanalyse-Template** (Benchmarking, Korrelation Verordnungsverhalten)
- **AWB-Review-Checkliste** (wissenschaftliche Substanz vs. Marketing)
- **FSA-Transparenzbericht-Prüfung**
- **Fair-Market-Value-Analyse** für Honorare
- **Compliance-SOP-Template** für HCP-Interaktionen

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
