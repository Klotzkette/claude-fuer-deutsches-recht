---
name: inv-expense-export
description: "Inv 028 Expense Fraud, Inv 029 Export Control Breach: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 028 Expense Fraud, Inv 029 Export Control Breach

## Arbeitsbereich

Dieser Skill bündelt **Inv 028 Expense Fraud, Inv 029 Export Control Breach** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-028-expense-fraud` | Untersucht Spesenabrechungs- und Reisekostenbetrug – forensische Buchprüfung, Beweissicherung, arbeitsrechtliche und strafrechtliche Konsequenzen. |
| `inv-029-export-control-breach` | Untersucht Verstöße gegen Exportkontrollrecht – AWG, AWV, EG-Dual-Use-VO, BAFA-Meldepflichten, US-Re-Export-Kontrolle. |

## Arbeitsweg

Für **Inv 028 Expense Fraud, Inv 029 Export Control Breach** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-028-expense-fraud`

**Fokus:** Untersucht Spesenabrechungs- und Reisekostenbetrug – forensische Buchprüfung, Beweissicherung, arbeitsrechtliche und strafrechtliche Konsequenzen.

# Spesenbetrug und Reisekostenmissbrauch

## Rechtlicher Rahmen

Spesenabrechungsbetrug ist eine der häufigsten Formen des Mitarbeiterbetrugs und erfüllt regelmäßig den Tatbestand des § 263 StGB (Betrug, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__263.html)) oder § 266 StGB (Untreue, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__266.html)), wenn der Täter besondere Vertrauensstellung hat. Hinzu kommt § 370 AO (Steuerhinterziehung), wenn Falschabrechnungen steuerlich geltend gemacht werden. Für Unternehmen begründet § 130 OWiG eine Haftung, wenn fehlende Kontrollmechanismen den Missbrauch ermöglicht haben.

## Ziel dieses Skills

Dieser Skill strukturiert die forensische Untersuchung von Spesenbetrug: von der Datenbankanalyse über Dokumentenprüfung bis zu den arbeitsrechtlichen und strafrechtlichen Maßnahmen.

## Arbeitsprogramm

### 1. Datenanalyse – Erste Auffälligkeiten
- **Statistische Ausreißer**: Mitarbeiter mit überdurchschnittlich hohen Spesenabrechnungen im Vergleich zu Peers.
- **Timing-Analyse**: Abrechnungen direkt nach Jahresendabrechnung oder kurz vor Ausscheiden.
- **Doppelabrechnung**: dieselbe Leistung zweimal abgerechnet (z. B. Taxi und Mietwagen für dieselbe Strecke).
- **Phantomrechnungen**: Lieferanten, die nicht existieren oder keine Leistung erbracht haben.
- **Round-Numbers-Test**: Rechnungen in runden Beträgen (z. B. genau 999 EUR kurz unter Genehmigungsgrenze).
- **Benford's Law**: führende Ziffern der Abrechnungsbeträge auf Manipulation prüfen.

### 2. Dokumentenprüfung
- Originalbelege verlangen: Kreditkartenabrechnung, Quittung, Hotelbuchungsbestätigung.
- Abgleich mit externen Quellen: Flugbuchungen, Hotelraten, Taxiquittungen.
- Modifizierte Belege (PDF-Manipulation): Metadaten, Schriftarten, Formatierungsfehler prüfen.
- Lieferantenregister: Existenz und Aktivität der in Rechnungen genannten Unternehmen prüfen (Handelsregister).

### 3. Digitale Forensik
- E-Mails: Kommunikation mit Lieferanten; Selbstbuchungen; Genehmigungsanfragen.
- Systeme: ERP-Buchungen (SAP, Oracle), Kreditkartensystemdaten, Reisebuchungstools.
- Zugriffsrechte: Hatte der Täter Zugriff auf Genehmigungsprozesse, die er manipulieren konnte?
- Temporäre Dateien: gelöschte Dokumente, Entwürfe (in forensischen Images oder Backup).

### 4. Interviews
- Täter-Interview: erst nach vollständiger Dokumenten- und Datenanalyse; Konfrontation mit konkreten Belegen.
- Zeugen: Kollegen, Vorgesetzte, Genehmiger; haben sie Auffälligkeiten wahrgenommen?
- Kontrollperson: Wer hat die Abrechnungen genehmigt? Mitverantwortung?
- Belehrung: wenn strafrechtliche Relevanz, nemo tenetur.

### 5. Schadensberechnung
- Vollständige Berechnung des Schadens: zu Unrecht erstattete Beträge + steuerliche Nachteile des Unternehmens.
- Gegenrechnung: Steuererstattungen, die auf betrügerischen Abrechnungen basieren → auch Schadensposition.
- Zeitraum: Wie lange dauerte der Betrug? Verjährung (§ 78 StGB, § 195 BGB)?

### 6. Arbeitsrechtliche und strafrechtliche Konsequenzen
- Außerordentliche Kündigung: Betrug am Arbeitgeber ist regelmäßig ein wichtiger Grund (§ 626 BGB); kein Abmahnungserfordernis bei erheblichem Betrug.
- Strafanzeige: § 263 oder § 266 StGB; Ermessen des Unternehmens; Interessenabwägung (Öffentlichkeit vs. Reputationsschaden).
- Schadensersatz: § 249 BGB; Einbehalt des letzten Gehalts auf Basis einer Aufrechnung (Aufrechnung nach § 387 BGB mit zu Unrecht erstatteten Beträgen).

### 7. Systemic Findings
- Wie war der Betrug möglich? Fehlende Vier-Augen-Prinzipien, fehlende Belegnachweise, überhöhte Genehmigungsgrenzen.
- Remediation: Kontrollen verschärfen, Spending-Limits anpassen, Prüfung externer Lieferanten automatisieren.
- § 130 OWiG: Fehlende Kontrollen können selbst bußgeldbewehrt sein.

## Red-Team-Fragen

- Wurden alle verfügbaren Datenquellen (ERP, Kreditkarte, Reisebuchung) systematisch ausgewertet?
- Gibt es Indizien, dass Genehmiger kompromittiert oder mitbeteiligt waren?
- Sind die modifizierten Belege so dokumentiert (Metadaten, Schriftarten), dass ein Sachverständiger im Strafverfahren den Betrug bestätigen kann?
- Wurde der Schaden vollständig berechnet, einschließlich steuerlicher Effekte?
- Ist die 2-Wochen-Frist für die außerordentliche Kündigung eingehalten?
- Wurden Systemschwachstellen identifiziert und Remediation-Maßnahmen festgelegt?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 263 StGB | Betrug | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__263.html) |
| § 266 StGB | Untreue | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__266.html) |
| § 370 AO | Steuerhinterziehung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/__370.html) |
| § 626 BGB | Außerordentliche Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__626.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |

## Ausgabeformate

- **Spesenbetrugs-Analyse-Template** (Statistische Ausreißer, Doppelbuchungen, Phantomrechnungen)
- **Dokumenten-Prüfmatrix** (Beleg × Originalcheck × Ergebnis)
- **Schadensberechnungs-Tabelle**
- **Kündigungsschreiben** bei Spesenbetrug
- **Remediation-Maßnahmenplan** (Kontrolllücken schließen)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-029-export-control-breach`

**Fokus:** Untersucht Verstöße gegen Exportkontrollrecht – AWG, AWV, EG-Dual-Use-VO, BAFA-Meldepflichten, US-Re-Export-Kontrolle.

# Exportkontrollverstöße – Untersuchung und Meldepflichten

## Rechtlicher Rahmen

Exportkontrollverstöße sind strafbewehrt nach § 18 AWG (Außenwirtschaftsgesetz, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/__18.html)) und § 70 AWV. EU-Dual-Use-Güter unterliegen der EG-Dual-Use-Verordnung VO (EU) 2021/821 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32021R0821)). US-Güter und -Technologien fallen unter EAR (Export Administration Regulations) und können Re-Export-Genehmigungspflichten auslösen. Behörden: BAFA (Bundesamt für Wirtschaft und Ausfuhrkontrolle) und US-BIS (Bureau of Industry and Security), OFAC (Office of Foreign Assets Control) bei Sanktionsbezug. Verstöße können zu Entzug von Exportlizenzen und erheblichen Strafzahlungen führen.

## Ziel dieses Skills

Dieser Skill identifiziert Exportkontrollverstöße, leitet Selbstanzeige-Entscheidungen ab und strukturiert die behördliche Kooperation mit BAFA, Zoll und US-BIS/OFAC.

## Arbeitsprogramm

### 1. Tatbestandsanalyse
- Welche Güter wurden exportiert? Klassifizierung nach Exportkontrollliste (EKL) oder EU-Dual-Use-Liste prüfen.
- In welche Länder? Embargoländer (§ 74 AWV; EU-Embargos nach EU-Verordnungen), Sanktionslisten (EU, US-OFAC).
- Lagen Genehmigungen vor? Wurden sie überschritten?
- Wer hat intern entschieden und genehmigt?

### 2. Dokumentenprüfung
- Exportdeklarationen: EX1/Zollanmeldungen; BAFA-Genehmigungen und deren Umfang.
- End-User-Zertifikate: korrekte Empfänger angegeben? Tatsächliche Endverwendung geprüft?
- Lieferverträge: Wiederverkaufsbeschränkungen vereinbart? Re-Export-Klauseln?
- Klassifizierungsdokumentation: wer hat die Exportkontrollklassifizierung vorgenommen?

### 3. Interne Compliance-Struktur
- Exportkontroll-Beauftragter vorhanden und ausgebildet?
- Screening-Prozesse: Kunden, End-User, Sanktionslisten (EU, OFAC, Wassenaar).
- ICP (Internal Compliance Programme): dokumentiert und gelebt?
- § 130 OWiG: fehlende Compliance-Strukturen begründen Unternehmensbußgeld.

### 4. Schwere der Verletzung
- Leichte Verstöße: fehlerhafte Klassifizierung ohne strategischen Gütercharakter; administrative Sanktion.
- Mittelschwere: genehmigungspflichtige Dual-Use-Güter ohne Genehmigung.
- Schwere: Güter mit militärischem Endverwendungspotenzial in Embargoländer; Strafbarkeit nach § 18 AWG.
- US-Re-Export: Verstoß gegen EAR auch für Nicht-US-Unternehmen bei US-Güterkomponenten ≥ de minimis.

### 5. BAFA-Selbstanzeige
- § 22 AWG: Möglichkeit der Selbstanzeige; strafmildernde Wirkung dokumentiert.
- Inhalt: vollständige Sachverhaltsdarstellung, betroffene Güter, Zeitraum, beteiligte Personen, Schadensumfang.
- Timing: vor BAFA-Entdeckung; danach kein Selbstanzeigeeffekt mehr.
- Gleichzeitige Abstimmung mit Strafverfolgungsbehörden, falls Straftatverdacht besteht.

### 6. US-Voluntary Disclosure (BIS/OFAC)
- BIS Voluntary Self-Disclosure: erhebliche Strafminderung (bis zu 50 % Reduktion).
- OFAC Voluntary Self-Disclosure: Grundlage für Penalty-Reduktion.
- DOJ/OFAC-Koordination: sicherstellen, dass BIS-Disclosure nicht dem DOJ-Verfahren schadet.
- Sperrlisten-Screening: alle relevanten Geschäftspartner nochmals prüfen.

### 7. Remediation
- Exportkontrolle-Audit: vollständige Überprüfung aller Exporttransaktionen der letzten Jahre.
- Klassifizierungsübersicht: alle Güter neu klassifizieren und dokumentieren.
- Sanktionsscreening-Software implementieren (z. B. Accuity, Dow Jones Risk & Compliance).
- Training: alle Mitarbeiter in Exportkontrolle schulen.
- BAFA-Monitorauftrag: ggf. externe Compliance-Überwachung als Teil der Selbstanzeige-Vereinbarung.

## Red-Team-Fragen

- Wurden alle exportierten Güter korrekt nach Exportkontrollliste klassifiziert?
- Gibt es US-Komponenten in den exportierten Gütern, die Re-Export-Genehmigungen auslösen?
- Wurden End-User-Zertifikate auf Plausibilität geprüft, oder wurden sie nur formal abgehakt?
- Sind alle relevanten Sanktionslisten (EU, US-OFAC, UN) für alle beteiligten Parteien gescreent worden?
- Wurde die Entscheidung zur Selbstanzeige dokumentiert – mit Pro-Contra-Abwägung?
- Sind die internen Compliance-Strukturen nach dem Verstoß gestärkt worden?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 18 AWG | Straftatbestände Exportkontrolle | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/__18.html) |
| § 22 AWG | Selbstanzeige | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/__22.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |
| VO (EU) 2021/821 | Dual-Use-Güter | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32021R0821) |
| BAFA | Behördeninfos | [bafa.de](https://www.bafa.de/) |

## Ausgabeformate

- **Exportkontroll-Prüfmatrix** (Güter × Klassifizierung × Genehmigung × Land)
- **BAFA-Selbstanzeige-Vorlage**
- **End-User-Zertifikat-Prüfcheckliste**
- **ICP-Gap-Analysis** (Vergleich Ist-Soll Compliance-Struktur)
- **Remediation-Plan** (Klassifizierung, Screening, Training)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
