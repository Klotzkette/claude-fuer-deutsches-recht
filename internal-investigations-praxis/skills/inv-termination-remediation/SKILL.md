---
name: inv-termination-remediation
description: "Inv 044 Termination Strategy, Inv 045 Remediation Plan: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 044 Termination Strategy, Inv 045 Remediation Plan

## Arbeitsbereich

Dieser Skill bündelt **Inv 044 Termination Strategy, Inv 045 Remediation Plan** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-044-termination-strategy` | Entwickelt Kündigungsstrategie für Beschuldigte und Beteiligte – Tatkündigung, Verdachtskündigung, Trennungsvereinbarung, Outplacement. |
| `inv-045-remediation-plan` | Erstellt einen strukturierten Remediation-Plan nach Untersuchungsabschluss – Kontrolllücken, Compliance-Verbesserungen, Behörden-Reporting und Nachverfolgung. |

## Arbeitsweg

Für **Inv 044 Termination Strategy, Inv 045 Remediation Plan** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-044-termination-strategy`

**Fokus:** Entwickelt Kündigungsstrategie für Beschuldigte und Beteiligte – Tatkündigung, Verdachtskündigung, Trennungsvereinbarung, Outplacement.

# Kündigungsstrategie nach Internal Investigations

## Rechtlicher Rahmen

Die Kündigung nach einer Internal Investigation ist der arbeitsrechtliche Endpunkt eines Disziplinarverfahrens. Die rechtlichen Instrumente sind: ordentliche verhaltensbedingte Kündigung (§ 1 KSchG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kschg/__1.html)), außerordentliche Kündigung (§ 626 BGB, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__626.html)) und Verdachtskündigung (BAG-Rechtsprechung). Alternativ: Aufhebungsvertrag oder Trennungsvereinbarung. Besonderheit: Zeitdruck (§ 626 Abs. 2 BGB: 2-Wochen-Frist für außerordentliche Kündigung ab Kenntnis der maßgeblichen Tatsachen).

## Ziel dieses Skills

Dieser Skill entwickelt für jeden Beschuldigten die optimale Kündigungsstrategie – unter Berücksichtigung des Beweismaterials, der Rechtslage und des Verhältnisses zu Behörden.

## Arbeitsprogramm

### 1. Entscheidungsbaum: Kündigung vs. Aufhebungsvertrag
- Kündigung: Konfrontation; Arbeitnehmer kann Kündigungsschutzklage erheben.
- Aufhebungsvertrag: einvernehmliche Trennung; schneller, aber Zugeständnisse nötig.
- Strategische Überlegungen: Soll der Täter als Zeuge im Strafverfahren auftreten? Dann kein vollständiger Rechtsfrieden.
- Kooperationsverpflichtung im Aufhebungsvertrag: Mitarbeit bei behördlichen Anfragen, Rückgabe von Unterlagen.

### 2. Außerordentliche Kündigung (§ 626 BGB)
- Wichtiger Grund: Pflichtverletzung, die das Arbeitsverhältnis unzumutbar macht.
- 2-Wochen-Frist: beginnt mit vollständiger Sachkenntnis (nicht mit erstem Verdacht).
- Untersuchungsdauer verlängert Frist nicht unbegrenzt; BAG-Rechtsprechung: Untersuchungszeitraum innerhalb des Verhältnismäßigen (BAG, Urt. v. 21.2.2013 – 2 AZR 433/12, [openjur.de](https://openjur.de/o/627892.html)).
- Betriebsratsanhörung: auch bei außerordentlicher Kündigung zwingend (§ 102 BetrVG, 3-Tage-Frist).

### 3. Verdachtskündigung
- Dringender Verdacht einer schwerwiegenden Pflichtverletzung als eigenständiger Kündigungsgrund.
- Vorherige Anhörung des Arbeitnehmers zum Verdacht ist Wirksamkeitsvoraussetzung.
- Beweisniveau: Verdacht muss auf objektiven Tatsachen beruhen, die stark genug sind, um Verbleib unzumutbar zu machen.
- Entlastung im Nachgang: Kündigung bleibt wirksam, wenn sie im Zeitpunkt des Verdachts berechtigt war.

### 4. Aufhebungsvertrag und Trennungsvereinbarung
- **Inhalte**: Auflösungstermin, Abfindung, Zeugnis, Abgeltung von Urlaubsansprüchen, Geheimhaltung, Kooperationspflicht.
- **Abfindung**: kein gesetzlicher Anspruch; strategisch zur Risikovermeidung.
- **Freistellungsvereinbarung**: Freistellung für Restlaufzeit; keine Gefahr weiterer Handlungen des Beschuldigten.
- **Kooperationsklausel**: Mitarbeiter verpflichtet sich, bei Behördenanfragen und Gerichtsverfahren zu kooperieren.
- **Schadensersatzvorbehalt**: Geltendmachung von Schadensersatzansprüchen bleibt unberührt.

### 5. Organmitglieder
- § 84 AktG: Abberufung des Vorstandsmitglieds durch Aufsichtsrat; wichtiger Grund erforderlich.
- Dienstvertrag läuft nach Abberufung weiter (Trennungsprinzip); Vergütungsanspruch bleibt bis Dienstvertragsende.
- Verhandlungslösung: Aufhebung des Dienstvertrags mit Ausgleich; D&O-Versicherungsdeckung berücksichtigen.
- Schadensersatzklage gegen Organmitglied: § 93 Abs. 2 AktG; parallel zur Abberufung möglich.

### 6. Besondere Personengruppen
- **Betriebsratsmitglied**: § 103 BetrVG – besonderer Kündigungsschutz; Zustimmung des Betriebsrats oder Arbeitsgericht erforderlich.
- **Schwerbehinderte**: § 168 SGB IX – Zustimmung des Integrationsamts vor Kündigung.
- **Schwangere**: § 17 MuSchG – Kündigung nur mit behördlicher Genehmigung.
- **Datenschutzbeauftragter (DSB)**: besonderer Kündigungsschutz nach § 38 Abs. 2 BDSG i. V. m. § 626 BGB.

### 7. Post-Trennungs-Maßnahmen
- Rückgabe von Unternehmenseigentum (Laptop, Mobiltelefon, Zugangskarten).
- Löschung/Sperrung von Systemzugängen.
- Dokumentation für mögliche Zeugenbefragung in künftigen Verfahren.
- Zeugnis: fair und wahrheitsgemäß; keine Gefälligkeitszeugnisse trotz Aufhebungsvertrag.

## Red-Team-Fragen

- Ist die 2-Wochen-Frist für außerordentliche Kündigung tatsächlich gewahrt?
- Wurde der Mitarbeiter vor der Verdachtskündigung angehört und hatte die Möglichkeit zur Stellungnahme?
- Sind Betriebsratsanhörung und ggf. Sonderkündigungsschutz (Betriebsrat, Schwerbehinderte, DSB) korrekt beachtet?
- Enthält der Aufhebungsvertrag eine Schadensersatzklausel, die spätere Regressansprüche offenhält?
- Wurde sichergestellt, dass der Beschuldigte keinen Zugriff mehr auf Systeme hat?
- Ist die Kündigung konsistent mit den Maßnahmen gegen vergleichbare Fälle im Unternehmen?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 626 BGB | Außerordentliche Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__626.html) |
| § 1 KSchG | Ordentliche Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kschg/__1.html) |
| § 84 AktG | Abberufung Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__84.html) |
| § 103 BetrVG | Kündigung Betriebsratsmitglied | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__103.html) |
| § 168 SGB IX | Kündigung Schwerbehinderter | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/sgb_9_2018/__168.html) |

## Ausgabeformate

- **Kündigungsstrategie-Entscheidungsbaum** (Kündigung vs. Aufhebung vs. Verdacht)
- **Außerordentliche Kündigung** (Musterschreiben)
- **Aufhebungsvertrag** mit Schadensersatzvorbehalt und Kooperationsklausel
- **Betriebsratsanhörung nach § 102 BetrVG**
- **Post-Trennungs-Checkliste** (Systemzugang, Unterlagen, Zeugnis)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-045-remediation-plan`

**Fokus:** Erstellt einen strukturierten Remediation-Plan nach Untersuchungsabschluss – Kontrolllücken, Compliance-Verbesserungen, Behörden-Reporting und Nachverfolgung.

# Remediation-Plan nach Internal Investigation

## Rechtlicher Rahmen

Ein Remediation-Plan ist nach einer Internal Investigation aus mehreren Gründen rechtlich geboten: (1) § 130 OWiG setzt voraus, dass das Unternehmen Aufsichtspflichten erfüllt; eine fehlende Reaktion auf festgestellte Mängel ist erneut ein Verstoß ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html)). (2) DOJ und SEC bewerten Remediation als wesentlichen Kooperationsfaktor. (3) BGH II ZR 234/09 (Siemens/Neubürger, [openjur.de](https://openjur.de/o/577696.html)) verlangt ein effektives Compliance-Management-System. (4) Behörden (BaFin, Bundeskartellamt) erwarten konkrete, fristgebundene Maßnahmen.

## Ziel dieses Skills

Dieser Skill erstellt einen strukturierten, priorisierten und nachverfolgbaren Remediation-Plan, der sowohl interne als auch behördliche Anforderungen erfüllt.

## Arbeitsprogramm

### 1. Root-Cause-Analyse
- Warum konnte der Verstoß entstehen?
- Kontrolllücken: fehlende Four-Eyes-Prinzipien, fehlende Genehmigungsprozesse, unzureichende Segregation of Duties.
- Kulturelle Faktoren: „Tone from the Top", Druck auf Mitarbeiter, Wegschauen durch Führungskräfte.
- Systemische Schwächen: Compliance-Funktionen ohne ausreichende Ressourcen oder Unabhängigkeit.
- Externe Faktoren: Marktpraktiken, Regulierungslücken.

### 2. Maßnahmenentwicklung (SMART-Kriterien)
- **Spezifisch**: Was genau wird verändert?
- **Messbar**: Wie wird die Wirksamkeit gemessen?
- **Assigniert**: Wer ist verantwortlich?
- **Realistisch**: Ist die Maßnahme mit vorhandenen Ressourcen umsetzbar?
- **Terminiert**: Bis wann muss die Maßnahme abgeschlossen sein?

### 3. Maßnahmenkategorien
- **Prozessverbesserungen**: neue SOPs, Genehmigungsprozesse, Segregation of Duties.
- **Technische Kontrollen**: DLP-Systeme, automatisches Sanktionsscreening, ERP-Kontrolleinstellungen.
- **Personalmaßnahmen**: Schulung, neue Compliance-Ressourcen, Rotation kritischer Funktionen.
- **Governance**: Compliance-Berichtslinie zum Aufsichtsrat, Audit-Committee-Reporting.
- **Third-Party-Management**: Due-Diligence-Prozesse für Agenten, Lieferanten.
- **Kultur**: Tone-from-the-Top-Messaging, Whistleblower-Programm.

### 4. Priorisierung der Maßnahmen
| Priorität | Kriterium | Frist |
|---|---|---|
| Kritisch | Unmittelbare Haftungsrisiken, aktive Verstöße | Sofort (7 Tage) |
| Hoch | Wesentliche Kontrolllücken | 30–60 Tage |
| Mittel | Prozessverbesserungen ohne unmittelbares Risiko | 60–180 Tage |
| Niedrig | Langfristige Kulturprogramme | 6–12 Monate |

### 5. Behördliche Einbindung
- DOJ: Remediation-Bericht als Teil der Kooperationsdokumentation; Corporate Enforcement Policy honoriert nachgewiesene Fortschritte.
- BaFin: Maßnahmenplan mit Fristen und Verantwortlichen; regelmäßige Umsetzungsberichte.
- Datenschutzbehörde: Remediation-Maßnahmen bei DSGVO-Verstößen als bußgeldmindernder Faktor (Art. 83 Abs. 2 lit. f DSGVO).
- Bundeskartellamt: Compliance-Programm als Bußgeld-mildernder Faktor.

### 6. Monitoring und Nachverfolgung
- Compliance-Monitoring-Funktion: unabhängige Überprüfung der Umsetzung.
- Interne Revision: Follow-up-Audit nach 6–12 Monaten.
- Maßnahmen-Tracking-System: offene Maßnahmen, Verantwortliche, Fristen, Eskalation bei Verzug.
- Vorstandsberichterstattung: regelmäßige Updates zum Remediation-Status.
- Aufsichtsrat/Prüfungsausschuss: halbjährlicher Bericht.

### 7. Nachhaltigkeit und Kulturwandel
- Compliance-Programm muss gelebt werden, nicht nur dokumentiert sein.
- Incentives: Compliance-Verhalten in Zielvereinbarungen und Bonusstrukturen verankern.
- Leadership: Vorstand und Senior Management als sichtbare Treiber des Wandels.
- Regelmäßige Compliance-Risikobeurteilung (Compliance Risk Assessment).
- Externe Überprüfung: unabhängiger Compliance-Monitor oder Externer Prüfer.

## Red-Team-Fragen

- Adressiert der Remediation-Plan die Root Causes, oder werden nur Symptome bekämpft?
- Sind alle Maßnahmen mit klaren Verantwortlichen und Fristen versehen?
- Hat der Vorstand den Remediation-Plan persönlich gebilligt und unterstützt er ihn aktiv?
- Werden die Maßnahmen unabhängig überwacht, oder prüft der Verantwortliche sich selbst?
- Würde das DOJ oder die BaFin den Remediation-Plan als ernsthaft und ausreichend bewerten?
- Gibt es Maßnahmen, die nur auf dem Papier existieren, aber in der Praxis nicht umgesetzt werden?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |
| § 93 AktG | Sorgfaltspflicht Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| Art. 83 DSGVO | DSGVO-Bußgelder (Kooperation) | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| BGH II ZR 234/09 | Siemens/Neubürger | [openjur.de](https://openjur.de/o/577696.html) |

## Ausgabeformate

- **Remediation-Plan-Template** (Maßnahme × Verantwortlicher × Frist × Messkriterium)
- **Root-Cause-Analyse-Vorlage**
- **Priorisierungsmatrix** (Kritisch/Hoch/Mittel/Niedrig)
- **Monitoring-Dashboard-Vorlage**
- **Behörden-Remediation-Bericht** (für DOJ/BaFin)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
