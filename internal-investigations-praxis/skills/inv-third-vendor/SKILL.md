---
name: inv-third-vendor
description: "Inv 036 Third Party Agent, Inv 037 Vendor Kickback: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 036 Third Party Agent, Inv 037 Vendor Kickback

## Arbeitsbereich

Dieser Skill bündelt **Inv 036 Third Party Agent, Inv 037 Vendor Kickback** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-036-third-party-agent` | Überprüft Third-Party-Agenten und Intermediäre auf FCPA/UK-Bribery-Risiken – Due Diligence, Verträge, Red Flags und Vertragsbeendigung. |
| `inv-037-vendor-kickback` | Untersucht Lieferanten-Kickbacks – forensische Zahlungsanalyse, Vergabeverfahren-Review, Täteridentifizierung, strafrechtliche und arbeitsrechtliche Konsequenzen. |

## Arbeitsweg

Für **Inv 036 Third Party Agent, Inv 037 Vendor Kickback** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-036-third-party-agent`

**Fokus:** Überprüft Third-Party-Agenten und Intermediäre auf FCPA/UK-Bribery-Risiken – Due Diligence, Verträge, Red Flags und Vertragsbeendigung.

# Third-Party-Due-Diligence und Agenten-Untersuchung

## Rechtlicher Rahmen

Drittparteien (Agenten, Berater, Distributoren, Joint-Venture-Partner) sind die häufigste Quelle von FCPA- und UK-Bribery-Act-Verstößen. Das Unternehmen haftet für Handlungen seiner Agenten, wenn es die korrupten Handlungen „authorized, directed or controlled" (FCPA) oder keine angemessenen Präventivmaßnahmen getroffen hat (UK Bribery Act Section 7: Failure to Prevent Bribery). Im deutschen Recht droht § 30 OWiG, wenn leitende Personen Korruption durch Agenten nicht verhindert haben (§ 130 OWiG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html)).

## Ziel dieses Skills

Dieser Skill strukturiert die Überprüfung von Drittparteien auf Korruptionsrisiken und die Untersuchung konkreter Verdachtsmomente bei bestehenden Agenten.

## Arbeitsprogramm

### 1. Due-Diligence-Prozess (präventiv)
- **Onboarding-DD**: vor Vertragsschluss; umfasst Hintergrundprüfung, Sanktionslisten-Screening, Reputationsrecherche, Offenlegung politischer Verbindungen (PEP-Check).
- **Risikostufung**: geografisches Risiko (TI Korruptionswahrnehmungsindex), Art der Tätigkeit, Umgang mit öffentlichen Funktionsträgern.
- **Ongoing-DD**: jährliche Überprüfung bei Hochrisiko-Agenten.
- **Red Flags**: Agent fordert Cash, übermäßige Provisionen, Zahlung in Drittland, keine Erklärung für Vertragsnecessity.

### 2. Vertragsgestaltung und Compliance-Klauseln
- Repräsentations- und Warranty-Klauseln: Agent bestätigt Einhaltung von FCPA, UK Bribery Act, GeschGehG.
- Audit Right: Unternehmen hat das Recht, Bücher und Aufzeichnungen des Agenten zu prüfen.
- Termination for Cause: sofortige Kündigung bei Compliance-Verstoß ohne Entschädigungspflicht.
- No-Cash-Zahlungs-Klausel, Dokumentationspflicht für alle Ausgaben.
- FCPA-Training-Pflicht für Agenten.

### 3. Untersuchung bei konkretem Verdacht
- **Zahlungsanalyse**: Provisionen im Vergleich zu erbrachten Leistungen; Split-Payments; Zahlungen in Offshore-Konten.
- **Leistungsnachweis**: Welche konkreten Tätigkeiten hat der Agent nachweislich erbracht?
- **Kommunikation**: E-Mail zwischen Agent und Mitarbeitern; Hinweise auf beabsichtigte oder vollzogene Zahlungen an Funktionsträger?
- **Transaktionshistorie**: Wann wurde der Vertrag abgeschlossen? Folgte darauf eine Auftragszusage der Gegenseite?
- **Geografische Analyse**: Transaktionen zeitlich mit Behördenentscheidungen oder Vertragsvergaben korreliert?

### 4. Interview des Agenten
- Beauftragter Anwalt des Unternehmens führt das Interview; Agent sollte eigenen Anwalt haben.
- Keine strafrechtlichen Geständnisse einholen wollen; Ziel: Sachverhaltsklärung.
- Vertragliche Kooperationspflicht: Agent ist vertraglich zur Auskunft verpflichtet.
- Wenn Agent die Kooperation verweigert: sofortige Vertragskündigung.

### 5. Vertragsbeendigung und Folgen
- Kündigung bei Red Flags auch ohne vollständigen Beweis möglich, wenn das Weiterbeschäftigen das Unternehmen gefährdet.
- Keine Entschädigungspflicht bei Kündigung wegen Compliance-Verstoß (sofern Vertrag entsprechend gestaltet).
- Nachvertragliche Pflichten: Agent darf keine Informationen des Unternehmens weiternutzen; NDA-Erinnerung.
- Regulatorische Konsequenz: wenn Agent bereits Behördenmitarbeiter bestochen hat, Self-Reporting prüfen.

### 6. Dokumentation für behördliche Kooperation
- Vollständige Due-Diligence-Unterlagen für DOJ/SEC: Zeigen Sie, dass angemessene Präventivmaßnahmen vorhanden waren.
- Audit-Right-Ergebnisse: wenn Prüfung des Agenten Red Flags ergab, wann wurde reagiert?
- Nachweis lückenloser Compliance-Struktur: DOJ Corporate Enforcement Policy honoriert proaktive Maßnahmen.

### 7. Systemische Überprüfung
- Alle Agenten und Intermediäre auflisten; Hochrisikosegment identifizieren.
- Verträge ohne aktuelle DD oder Compliance-Klauseln sofort aktualisieren.
- Agenten-Register mit DD-Status und nächstem Review-Datum.

## Red-Team-Fragen

- Gibt es Agenten, die keine aktuelle Due-Diligence-Prüfung haben?
- Sind Provisionen im Verhältnis zur nachweisbaren Leistung des Agenten angemessen?
- Wurden Vertragskündigungen bei Red Flags rechtzeitig ausgesprochen, oder hat das Unternehmen zu lange zugeschaut?
- Hat das Unternehmen das Audit-Right gegenüber Hochrisiko-Agenten tatsächlich ausgeübt?
- Kann das Unternehmen gegenüber dem DOJ demonstrieren, dass Adequate Procedures vorhanden waren?
- Gibt es Hinweise auf Zahlungen nach der Vertragskündigung oder auf laufende Verbindungen zu dem Agenten?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |
| § 30 OWiG | Verbandsgeldbuße | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__30.html) |
| § 299 StGB | Bestechung im Geschäftsverkehr | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299.html) |
| 15 U.S.C. § 78dd-1 | FCPA Anti-Bribery | US Government |
| UK Bribery Act Section 7 | Failure to Prevent Bribery | UK Government |

## Ausgabeformate

- **Third-Party-Due-Diligence-Checkliste** (Onboarding + Ongoing)
- **Risikostufungs-Matrix** (geografisch, Tätigkeitsbereich, PEP-Verbindungen)
- **Compliance-Klausel-Vorlage** für Agentenverträge
- **Audit-Right-Ausübungsprotokoll**
- **Kündigungsschreiben** bei Compliance-Verstoß (Muster)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-037-vendor-kickback`

**Fokus:** Untersucht Lieferanten-Kickbacks – forensische Zahlungsanalyse, Vergabeverfahren-Review, Täteridentifizierung, strafrechtliche und arbeitsrechtliche Konsequenzen.

# Lieferanten-Kickback-Untersuchung

## Rechtlicher Rahmen

Kickbacks von Lieferanten an Einkäufer oder Entscheidungsträger erfüllen die Tatbestände der §§ 299, 300 StGB (Bestechung und Bestechlichkeit im geschäftlichen Verkehr, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299.html)), § 263 StGB (Betrug) und § 266 StGB (Untreue), je nach Konstruktion. Für das Unternehmen als Geldwäscheadressat kommt § 261 StGB in Betracht, wenn Kickback-Erlöse in das Unternehmen zurückfließen. Das Unternehmen selbst haftet nach § 30 OWiG, wenn § 130 OWiG-Verstöße vorliegen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__30.html)).

## Ziel dieses Skills

Dieser Skill strukturiert die forensische Untersuchung von Kickback-Verdachtsmomenten in Beschaffungsprozessen.

## Arbeitsprogramm

### 1. Red-Flag-Identifizierung in Vergabeverfahren
- **Preisanomalien**: Lieferant liegt erheblich über Marktpreis; Qualitätsmängel werden toleriert.
- **Auftragsvergabe ohne Ausschreibung**: Direktvergabe an bestimmten Lieferanten.
- **Häufige Auftragsänderungen**: Nachträge, die den ursprünglichen Auftragswert erhöhen.
- **Rahmenverträge ohne Leistungsnachweis**: pauschale Zahlungen ohne dokumentierte Gegenleistung.
- **Interessenkonflikt des Entscheiders**: vgl. inv-035-conflict-of-interest.

### 2. Forensische Zahlungsanalyse
- Alle Lieferantenzahlungen über definierten Zeitraum und Betragsgrenzen extrahieren.
- Vergleich Lieferantenpreise mit Marktpreisen (Benchmarking).
- Identifikation von Lieferanten, die kurz nach Gründung große Aufträge erhalten haben.
- Analyse von Rechnungen ohne ordnungsgemäße Beschreibung der Leistung.
- Verbindungen zwischen Lieferanten und Entscheidungsträgern (Handelsregister, soziale Netzwerke).

### 3. Vergabeverfahren-Review
- Dokumentation der Auswahlentscheidungen: Wer hat entschieden? Welche Kriterien?
- Ausschreibungsunterlagen: Wurden Spezifikationen so formuliert, dass nur ein Bieter gewinnen konnte?
- Bewertungsmatrizen: Wurden die Kriterien eingehalten, oder wurde das Ergebnis manipuliert?
- Genehmigungsweg: Wurden alle erforderlichen Genehmigungen eingeholt?

### 4. Lieferanten-seitige Untersuchung
- Lieferant kooperiert: eigene Aufzeichnungen über gezahlte Provisionen oder Geschenke vorlegen.
- Lieferant verweigert: vertragliche Audit-Right ausüben (falls vereinbart); andernfalls beweismittelseitig auf interne Daten beschränkt.
- Handelsregister-Prüfung: Identität der Eigentümer und Verbindung zu Mitarbeitern.
- Offshore-Zahlungen: wurden Kick-backs über Briefkastengesellschaften verschleiert?

### 5. Täter-Interview
- Vorherige Dokumentenanalyse abschließen; Konfrontation nur mit belegbaren Fakten.
- Belehrung: wenn strafrechtliche Relevanz offensichtlich, Schweigerecht nach § 136 StPO.
- Umfang des Schadens: erbrachte Leistung des Lieferanten vs. gezahlter Preis.
- Kooperation des Täters mit der Untersuchung: kann strafmildernd wirken.

### 6. Arbeitsrechtliche und strafrechtliche Maßnahmen
- Außerordentliche Kündigung (§ 626 BGB): schwere Pflichtverletzung.
- Strafanzeige: §§ 299, 266, 263 StGB; auch gegen Lieferanten.
- Schadensersatz: gegen Täter und Lieferanten (als Mittäter oder Teilnehmer).
- Geldwäsche: wenn Kickback-Erlöse in das Unternehmen zurückgeflossen sind: § 261 StGB prüfen.

### 7. Prävention und Remediation
- Beschaffungsrichtlinie mit klaren Ausschreibungspflichten.
- Vier-Augen-Prinzip bei Lieferantenauswahl über Schwellenwert.
- Supplier Code of Conduct mit Kickback-Verbot.
- Anonyme Meldestelle für Lieferantenbeschwerden.
- Rotationsprinzip für Einkäufer in sensiblen Kategorien.

## Red-Team-Fragen

- Gibt es systematische Muster in der Lieferantenauswahl, die auf Manipulation hindeuten?
- Wurden Preisvergleiche für die verdächtigen Lieferantentransaktionen durchgeführt?
- Haben Kickback-Zahlungen den Weg zurück in das Unternehmen gefunden (Geldwäsche-Risiko)?
- Gibt es Verbindungen zwischen dem verdächtigen Lieferanten und Einkäufern oder Führungskräften im Unternehmen?
- Wurden alle erforderlichen Genehmigungen ordnungsgemäß eingeholt und dokumentiert?
- Ist der Schaden vollständig berechnet – nicht nur der Kickback-Betrag, sondern der gesamte Überzahlungsbetrag?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 299 StGB | Bestechung im Geschäftsverkehr | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299.html) |
| § 266 StGB | Untreue | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__266.html) |
| § 261 StGB | Geldwäsche | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__261.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |
| § 626 BGB | Außerordentliche Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__626.html) |

## Ausgabeformate

- **Lieferanten-Zahlungsanalyse-Template** (Anomalien, Benchmarking)
- **Vergabeverfahren-Review-Checkliste**
- **Kickback-Schadensberechnungs-Vorlage**
- **Strafanzeige** §§ 299, 266 StGB
- **Präventionsmaßnahmen-Katalog** (Beschaffungsrichtlinie, Supplier Code of Conduct)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
