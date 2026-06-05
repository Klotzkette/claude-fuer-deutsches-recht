---
name: inv-honeypot-legal
description: "Inv 002 Honeypot Risiko, Inv 003 Legal Hold: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 002 Honeypot Risiko, Inv 003 Legal Hold

## Arbeitsbereich

Dieser Skill bündelt **Inv 002 Honeypot Risiko, Inv 003 Legal Hold** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-002-honeypot-risiko` | Bewertet das Risiko, dass die Untersuchung selbst zum Honeypot für Behörden, Gegner, US-Discovery oder Presselecks wird. |
| `inv-003-legal-hold` | Implementiert Legal Hold – Sicherung, Sperrung und Dokumentation aller potenziell relevanten Beweismittel ab Verdachtsmoment. |

## Arbeitsweg

Für **Inv 002 Honeypot Risiko, Inv 003 Legal Hold** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-002-honeypot-risiko`

**Fokus:** Bewertet das Risiko, dass die Untersuchung selbst zum Honeypot für Behörden, Gegner, US-Discovery oder Presselecks wird.

# Honeypot-Risiko in Internal Investigations

## Rechtlicher Rahmen

Jede Internal Investigation erzeugt Dokumente, die in fremden Händen gefährlich werden können. Das sog. „Honeypot-Risiko" beschreibt die Gefahr, dass der Untersuchungsbericht, Interviewprotokolle, Forensik-Ergebnisse oder interne E-Mails von Strafverfolgungsbehörden beschlagnahmt (§§ 94, 97 StPO, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__94.html)), im US-Discovery-Verfahren herausverlangt (FRCP Rule 26/34) oder durch Dritte gezielt als Beweismittel genutzt werden. Das Anwaltsgeheimnis schützt nur, soweit es in Anspruch genommen werden kann – nach EuGH C-550/07 P (Akzo Nobel, [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE)) gilt der EU-Schutz nicht für Inhouse Counsel. Im deutschen Recht schützen §§ 97, 148 StPO die Mandatsunterlagen des externen Anwalts, aber nur unter bestimmten Voraussetzungen.

## Ziel dieses Skills

Dieser Skill analysiert vor jeder Untersuchungshandlung, ob und welche Dokumente ein Risikopotenzial für die Gesellschaft, ihre Organe oder betroffene Mitarbeiter begründen. Das Ziel ist keine Beweisunterdrückung, sondern strukturierte Risikominimierung im Rahmen des rechtlich Zulässigen.

## Arbeitsprogramm

### 1. Dokumenten-Topographie
- Welche Dokumente entstehen (Interviewprotokolle, Forensik-Images, Berichte, Memos)?
- Wer hat Zugriff (Anwalt, Mandant, IT-Dienstleister, Wirtschaftsprüfer)?
- Werden Dokumente auf Unternehmensservern oder in externen Systemen (US-Cloud, MS365, AWS) gespeichert?

### 2. Privilege-Analyse
- Work-Product-Doctrine und Attorney-Client Privilege für US-Verfahren prüfen (Upjohn Co. v. United States, 449 U.S. 383 (1981)).
- § 97 StPO: Beschlagnahmeschutz für Verteidigungsunterlagen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html)).
- Gemischte Teams (Anwalt + Wirtschaftsprüfer): Privilege kann verloren gehen, wenn Dritte einbezogen werden, die keine gesetzliche Verschwiegenheitspflicht tragen (§ 203 StGB gilt nicht für alle Dienstleister; [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html)).
- EuGH Akzo Nobel C-550/07 P: Inhouse-Anwalt genießt kein EU-Privilege bei Kommissionsverfahren.

### 3. US-Discovery-Risiko
- Sind US-Gesellschaften, US-Gerichte oder US-Behörden involviert? Dann droht FRCP-Discovery auf alle „reasonably accessible" Dokumente.
- Litigation Hold (§ 91 ZPO analog, FRCP 37(e)) muss ausgelöst werden, sobald Verfahren absehbar ist.
- „Crime-fraud exception": Privilege fällt weg, wenn Dokumente zur Vorbereitung künftiger Straftaten dienen.

### 4. Beschlagnahmerisiko Deutschland
- §§ 94–110 StPO: Beschlagnahme von Geschäftsunterlagen, E-Mails, Forensik-Images.
- § 97 StPO schützt Unterlagen zwischen Beschuldigtem und Verteidiger – nicht aber Unterlagen des Unternehmens beim Anwalt, der das Unternehmen berät (und der Beschuldigte ist Mitarbeiter).
- Separation of Work-Product: Anwalt sollte eigene Aufzeichnungen von reinen Fakten-Summaries trennen.

### 5. Leakage-Risiko
- Insider (HR, IT-Admin, betroffene Manager) könnten Dokumente abziehen.
- Need-to-know-Prinzip: Verteiler auf ein Minimum beschränken.
- Watermarking und Versionskontrolle für vertrauliche Berichte.
- DSGVO: Unbefugte Weitergabe = Datenpanne (Art. 33 DSGVO), ggf. Meldepflicht gegenüber Datenschutzbehörde.

### 6. Presserisiko und § 353b StGB
- § 353b StGB schützt behördliche Geheimnisse; für Private gilt strafrechtlich kein vergleichbarer Schutz, aber zivilrechtlicher Geheimnisschutz nach GeschGehG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/)).
- Medienanfragen: Keine Stellungnahme ohne Pressestrategie (vgl. inv-051-press-strategy).

## Red-Team-Fragen

- Wer außer dem eigenen Anwalt hat jemals physischen oder digitalen Zugriff auf den Bericht erhalten?
- Ist der Bericht so formuliert, dass er gegen die Gesellschaft verwendet werden kann, wenn er beschlagnahmt wird?
- Wurden US-Cloud-Dienste genutzt, die dem US-CLOUD-Act (18 U.S.C. § 2713) unterliegen?
- Hat der Wirtschaftsprüfer eigene Arbeitspapiere erstellt, die nicht vom Anwaltsgeheimnis erfasst sind?
- Wurde der Betriebsrat informiert – und wenn ja: durch wen, wann, in welchem Umfang?
- Gibt es Co-Counsel in den USA, die dem eigenen Privilege-Regime nicht unterliegen?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| §§ 94, 97 StPO | Beschlagnahme / Beschlagnahmeschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html) |
| § 203 StGB | Verletzung von Privatgeheimnissen | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html) |
| GeschGehG | Geschäftsgeheimnisschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/) |
| Art. 33 DSGVO | Meldepflicht Datenpannen | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| EuGH C-550/07 P | Akzo Nobel / Inhouse Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |

## Ausgabeformate

- **Privilege-Matrix**: Dokumenttyp × Schutznorm × Risikostufe
- **Verteilerliste** (Need-to-know-Analyse)
- **Beschlagnahme-Szenarien** mit Handlungsempfehlungen
- **US-Discovery-Risikoampel**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## Weiterführende Hinweise

- Jede Version des Berichts erhält eine eindeutige Versionsnummer und einen Verteiler-Vermerk; veraltete Versionen werden aus dem Umlauf genommen.
- Kommunikation über die Untersuchung in unverschlüsselten E-Mails oder Messaging-Diensten ist zu vermeiden; alle internen Kommunikationen sollten über sichere Kanäle erfolgen.
- Wenn ein Journalist gezielt nach der Untersuchung fragt, deutet das oft darauf hin, dass ein Insider Informationen geleakt hat; interne Forensik (Zugriffsprotokoll des VDR) sollte sofort prüfen, wer wann Zugriff hatte.
- Der Honeypot-Risikocheck wird mindestens einmal in der Woche durch den verantwortlichen Anwalt aktualisiert, sobald neue Dokumente produziert oder neue Personen informiert wurden.

## 2. `inv-003-legal-hold`

**Fokus:** Implementiert Legal Hold – Sicherung, Sperrung und Dokumentation aller potenziell relevanten Beweismittel ab Verdachtsmoment.

# Legal Hold

## Rechtlicher Rahmen

Der Legal Hold (Beweismittelsicherungsanordnung) ist die erste operative Maßnahme nach Entstehung eines Verdachts. Die Pflicht zur Beweismittelsicherung folgt im deutschen Recht aus der allgemeinen Treuepflicht des Vorstands (§ 93 AktG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html)) sowie aus der Beweislastumkehr in zivilrechtlichen Schadensersatzverfahren. Werden Beweismittel schuldhaft vernichtet, können Gerichte nach § 286 ZPO nachteilige Schlüsse ziehen; im US-Recht droht „Spoliation" mit Sanktionen nach FRCP 37(e). Strafrechtlich ist Beweismittelvernichtung nach § 274 StGB strafbar ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__274.html)). Datenschutzrechtlich kollidiert der Legal Hold mit dem Löschungsgebot nach Art. 17 DSGVO und § 35 BDSG – dieser Konflikt muss explizit gelöst werden.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass relevante Daten und Dokumente ab dem Moment des Verdachts gesichert, unveränderlich aufbewahrt und so dokumentiert werden, dass die Integrität der Beweismittelkette (Chain of Custody) in jedem Verfahren belegbar ist.

## Arbeitsprogramm

### 1. Trigger-Ereignisse identifizieren
- Wann entstand der Verdacht? Erste interne Meldung, externe Anfrage, Whistleblower-Hinweis (HinSchG § 3, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/))?
- Ab wann besteht Verfahrenswahrscheinlichkeit (US: „reasonable anticipation of litigation")?
- Dokumentation des Trigger-Zeitpunkts für spätere Fristberechnung.

### 2. Custodians und Datenquellen identifizieren
- Wer sind die relevanten Personen (Custodians)? Betroffene, Vorgesetzte, Buchhalter, IT-Admins?
- Welche Datenquellen existieren: E-Mail-Server, Sharepoint, Teams/Slack, Mobilgeräte, physische Dokumente, Buchhaltungssysteme, Cloud-Dienste?
- Drittparteien: Steuerberater, Wirtschaftsprüfer, externe Berater mit relevanten Unterlagen.

### 3. Sicherungsmaßnahmen
- IT-Snapshot und E-Mail-Archivierung: Archivierungsregel in Exchange/M365 oder Veritas aktivieren.
- Gelöschte E-Mails: Backup-Tapes, Exchange Recoverable Items (14-Tage-Fenster beachten).
- Automatische Löschroutinen deaktivieren (z. B. 30-Tage-Chat-Löschung in Teams).
- Physische Dokumente: Versiegelung von Büros, Aktenschränken bei Bedarf.
- Mobile Devices: MDM-Fernsperre, Cloud-Backup stoppen (vgl. inv-018-mobile-devices).

### 4. Legal-Hold-Benachrichtigung
- Schriftliche Hold-Notice an alle Custodians: was gesichert wird, warum, welche Handlungen verboten sind (Löschen, Verschieben, Verändern).
- Empfangsbestätigung dokumentieren.
- Keine Selbstjustiz: Mitarbeiter dürfen keine eigenen Selektionen vornehmen.
- Betriebsrat: Mitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG bei technischer Überwachungseinrichtung prüfen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html)).

### 5. Datenschutzkonflikt auflösen
- DSGVO Art. 17 Abs. 3 lit. e: Löschpflicht entfällt, soweit Verarbeitung zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist.
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten zulässig, wenn tatsächliche Anhaltspunkte vorliegen und Verhältnismäßigkeit gewahrt ist ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)).
- Verzeichnis der Verarbeitungstätigkeiten (Art. 30 DSGVO) aktualisieren.
- Datenschutzbeauftragter (DSB) einbinden.

### 6. Chain of Custody dokumentieren
- Hash-Werte (SHA-256) aller gesicherten Datensätze zum Sicherungszeitpunkt.
- Wer hat wann Zugriff gehabt – lückenlose Zugriffsprotokollierung.
- Forensik-Images nach ISO/IEC 27037 (Leitfaden für digitale Beweise).

### 7. Abgrenzung Legal Hold vs. Vollsicherung
- Legal Hold ≠ vollständige Forensik: Nur Sicherung, keine Auswertung durch Unternehmen selbst.
- Auswertung erst nach Rechtsgrundlagenklärung (Datenschutz, BetrVG, Strafrecht).

## Red-Team-Fragen

- Wurden automatische Löschroutinen auf allen Systemen (inkl. Mobile, Cloud, Backup) deaktiviert?
- Hat jeder Custodian eine Hold-Notice erhalten und bestätigt?
- Ist der Datenschutzkonflikt (DSGVO Art. 17 vs. Beweismittelsicherung) dokumentiert gelöst?
- Gibt es Drittparteien (Steuerberater, Wirtschaftsprüfer), die eigene Unterlagen halten und noch keinen Hold erhalten haben?
- Wurde der Betriebsrat über die Überwachungsmaßnahmen informiert?
- Können Hash-Werte und Zugangsprotokolle im Verfahren vorgelegt werden?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 93 AktG | Sorgfaltspflicht Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| § 274 StGB | Urkundenunterdrückung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__274.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| Art. 17 DSGVO | Recht auf Löschung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| HinSchG | Hinweisgeberschutz 2023 | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |

## Ausgabeformate

- **Legal-Hold-Notice** (Mustertext für Custodians)
- **Custodian-Liste** mit Bestätigungsmatrix
- **Chain-of-Custody-Protokoll**
- **Datenschutz-Abwägungsmemo** (Art. 17 Abs. 3 lit. e DSGVO vs. Löschpflicht)
- **IT-Anweisungsliste** für Systemadministratoren

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
