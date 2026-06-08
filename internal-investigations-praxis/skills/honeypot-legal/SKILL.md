---
name: honeypot-legal
description: "Bewertet das Risiko, dass die Untersuchung selbst zum Honeypot für Behörden, Gegner, US-Discovery oder Presselecks wird im Internal Investigations Praxis."
---

# Honeypot-Risiko in Internal Investigations

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

