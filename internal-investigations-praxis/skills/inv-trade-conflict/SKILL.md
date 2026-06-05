---
name: inv-trade-conflict
description: "Inv 034 Trade Secret Leak, Inv 035 Conflict Of Interest: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 034 Trade Secret Leak, Inv 035 Conflict Of Interest

## Arbeitsbereich

Dieser Skill bündelt **Inv 034 Trade Secret Leak, Inv 035 Conflict Of Interest** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-034-trade-secret-leak` | Untersucht Geheimnisverrat und Trade-Secret-Leaks – GeschGehG, § 17 UWG a.F., Täteridentifizierung, einstweilige Verfügung, Strafanzeige. |
| `inv-035-conflict-of-interest` | Untersucht Interessenkonflikte von Mitarbeitern und Organmitgliedern – Offenlegungspflichten, § 93 AktG, § 34 HGB, Insider-Geschäfte. |

## Arbeitsweg

Für **Inv 034 Trade Secret Leak, Inv 035 Conflict Of Interest** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-034-trade-secret-leak`

**Fokus:** Untersucht Geheimnisverrat und Trade-Secret-Leaks – GeschGehG, § 17 UWG a.F., Täteridentifizierung, einstweilige Verfügung, Strafanzeige.

# Trade-Secret-Leak und Geheimnisverrat

## Rechtlicher Rahmen

Der Schutz von Geschäftsgeheimnissen richtet sich nach dem GeschGehG (Gesetz zum Schutz von Geschäftsgeheimnissen, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/)), das die EU-Richtlinie 2016/943 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943)) umsetzt. Strafrechtlich ist § 23 GeschGehG (Strafbarkeit Geheimnisverrat) und § 17 UWG a. F. (heute weitgehend durch GeschGehG ersetzt) relevant. Täter können Mitarbeiter, ehemalige Mitarbeiter, Wettbewerber oder staatliche Akteure (Industriespionage) sein. Sofortmaßnahmen und einstweilige Verfügungen sind zeitkritisch.

## Ziel dieses Skills

Dieser Skill identifiziert den Täter, sichert Beweise und leitet zivil- und strafrechtliche Maßnahmen sowie einstweiligen Rechtsschutz ein.

## Arbeitsprogramm

### 1. Schadensfeststellung und Scope-Analyse
- Was wurde abgeflossen? Welche Geschäftsgeheimnisse (Definition § 2 Nr. 1 GeschGehG)?
- Wie wurde es abgeflossen? E-Mail-Versand, USB, Cloud-Upload, mündliche Weitergabe?
- An wen wurde es weitergegeben? Wettbewerber, ausländische Regierung, Presse?
- Welche wirtschaftlichen Schäden sind entstanden oder drohen?

### 2. Täteridentifizierung – Digitale Forensik
- **Access Logs**: Wer hat auf die betreffenden Dateien/Systeme zugegriffen (wann, wie oft)?
- **DLP-Systeme**: Data Loss Prevention – Alerts auf ungewöhnliche Downloads oder E-Mail-Ausgang?
- **USB-Protokolle**: Wurden USB-Sticks an Unternehmensgeräten verwendet?
- **Cloud-Upload-Logs**: Uploads zu Dropbox, Google Drive, persönlichen Konten?
- **E-Mail-Header**: externe Weitergabe via privater E-Mail-Adressen?
- **Printing-Logs**: ungewöhnliche Druckaufträge vor dem Ausscheiden?

### 3. Datenschutzrechtliche Grenzen der Tätersuche
- § 26 BDSG: Forensik zur Aufdeckung einer Straftat (§ 23 GeschGehG) zulässig bei konkreten Verdachtsmomenten.
- Verhältnismäßigkeit: gezielte Suche, keine Massenüberwachung.
- Betriebsrat: Mitbestimmung bei Einrichtung von DLP-Systemen (§ 87 Abs. 1 Nr. 6 BetrVG); ad-hoc-Forensik im Verdachtsfall regelmäßig ohne Mitbestimmung.
- § 202a StGB: kein unberechtigter Zugriff auf Systeme, auch nicht zur Tätersuche.

### 4. Einstweilige Verfügung
- § 935 ZPO: einstweilige Verfügung gegen Täter und Empfänger zur Unterlassung weiterer Nutzung des Geheimnisses.
- §§ 6, 7 GeschGehG: Ansprüche auf Unterlassung, Beseitigung, Schadensersatz, Herausgabe.
- Dringlichkeit: einstweilige Verfügung muss unverzüglich beantragt werden; Kammergericht Berlin akzeptiert oft 4-6 Wochen als Frist.
- Ex-parte-Verfügung (ohne Anhörung des Antragsgegners): bei Gefahr der Vernichtung von Beweisen möglich.

### 5. Strafanzeige
- § 23 GeschGehG: Strafbarkeit des Täters; Freiheitsstrafe bis zu 3 Jahren.
- Strafantrag erforderlich (§ 23 Abs. 4 GeschGehG); Frist 3 Monate ab Kenntnis.
- § 17 UWG a. F. noch relevant für Altfälle (vor GeschGehG 2019).
- ZAC (Zentrale Ansprechstelle Cybercrime): bei IT-gestütztem Geheimnisverrat.
- Wirtschaftsspionage durch ausländische Staatsstellen: Kontakt mit Verfassungsschutz.

### 6. Arbeitsrechtliche Maßnahmen
- Außerordentliche Kündigung des Täters (§ 626 BGB): schwerwiegende Verletzung der Verschwiegenheitspflicht.
- Schadensersatzklage: § 10 GeschGehG (Schadensersatz inkl. Lizenzanalogie).
- Unterlassungserklärung durch den (ehemaligen) Mitarbeiter verlangen.
- Nachvertragliche Wettbewerbsverbote (§§ 74 ff. HGB): durchsetzen oder auf Karenzzahlung verzichten.

### 7. Präventive Maßnahmen
- GeschGehG-Anforderungen (§ 2 Nr. 1): aktive Geheimhaltungsmaßnahmen sind Schutzvoraussetzung.
- NDA für alle Mitarbeiter und Auftragnehmer mit Zugang zu Geheimnissen.
- Need-to-know-Prinzip bei Datenzugriff.
- DLP-Systeme und USB-Beschränkungen einrichten (mit Betriebsratseinbindung).
- Regelmäßige Überprüfung der Zugriffsberechtigungen.

## Red-Team-Fragen

- Sind die GeschGehG-Schutzvoraussetzungen (§ 2 Nr. 1: geheim, Wert, Schutzmaßnahmen) erfüllt?
- Gibt es konkrete forensische Beweise für den Datenabriss, oder nur indirekten Verdacht?
- Wurde die einstweilige Verfügung unverzüglich beantragt?
- Ist der Strafantrag innerhalb der 3-Monats-Frist gestellt worden?
- Wurden DLP-Systeme mit Betriebsratszustimmung eingerichtet, oder droht Verwertungsverbot?
- Hat der Täter einen eigenen Anspruch als Whistleblower (§ 5 Nr. 2 GeschGehG), der den Schutzanspruch einschränkt?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| GeschGehG §§ 2, 6, 7, 10 | Schutz, Ansprüche | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/) |
| § 23 GeschGehG | Strafbarkeit Geheimnisverrat | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/__23.html) |
| § 935 ZPO | Einstweilige Verfügung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__935.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| EU-RL 2016/943 | Geheimnisschutzrichtlinie | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943) |

## Ausgabeformate

- **Digitale-Forensik-Checkliste** für Trade-Secret-Leak
- **Einstweilige-Verfügungs-Antrag** (Musterstruktur)
- **Strafanzeige** nach § 23 GeschGehG
- **Kündigung und Unterlassungserklärung** für Täter
- **GeschGehG-Schutzmaßnahmen-Audit**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-035-conflict-of-interest`

**Fokus:** Untersucht Interessenkonflikte von Mitarbeitern und Organmitgliedern – Offenlegungspflichten, § 93 AktG, § 34 HGB, Insider-Geschäfte.

# Interessenkonflikte – Untersuchung und Prävention

## Rechtlicher Rahmen

Interessenkonflikte von Mitarbeitern und Organmitgliedern sind einer der häufigsten Compliance-Verstöße und können zur Haftung nach § 93 AktG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html)), § 43 GmbHG, § 266 StGB (Untreue) und § 34 HGB (Wettbewerbsverbot für kaufmännische Angestellte, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__34.html)) führen. Im Kapitalmarktrecht lösen Interessenkonflikte Offenlegungspflichten nach MAR Art. 14, 17 aus. Aufsichtsratsmitglieder unterliegen Sonderregeln (§ 100 AktG: persönliche Anforderungen; § 114 AktG: Beraterverträge).

## Ziel dieses Skills

Dieser Skill identifiziert und untersucht Interessenkonflikte, leitet Remediation-Maßnahmen ab und klärt die haftungsrechtlichen Konsequenzen.

## Arbeitsprogramm

### 1. Kategorisierung von Interessenkonflikten
- **Wirtschaftliche Interessen**: Mitarbeiter oder dessen Angehörige profitieren von Unternehmensentscheidungen (z. B. Lieferantenwahl, Auftragsvergabe).
- **Doppelmandate**: Aufsichtsratsmitglied oder Vorstandsmitglied ist zugleich Berater oder Gesellschafter eines Lieferanten.
- **Nebentätigkeiten**: Mitarbeiter ist bei Wettbewerber oder Kunden tätig (§ 60 HGB: Wettbewerbsverbot, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__60.html)).
- **Family-and-Friend-Deals**: Vergabe von Aufträgen an Familienangehörige oder Freunde.
- **Post-Employment**: ehemaliger Mitarbeiter wechselt zu Auftragnehmer, bei dem er zuvor Entscheidungen getroffen hat.

### 2. Offenlegungsregime
- **Corporate Policy**: Pflicht zur Offenlegung von Interessenkonflikten gegenüber Compliance/HR; Code of Conduct.
- **§ 93 AktG**: Vorstandsmitglied darf keine Geschäftschancen der Gesellschaft für sich nutzen (Corporate Opportunity Doctrine).
- **§ 100 Abs. 2 Nr. 3 AktG**: Aufsichtsratsmitglied darf nicht gleichzeitig gesetzlicher Vertreter eines wesentlichen Wettbewerbers sein.
- **MAR**: Interessenkonflikte bei Kapitalmarkttransaktionen müssen offengelegt werden.

### 3. Untersuchungsschritte
- **Finanzdaten**: Zahlen an Lieferanten, die Verbindungen zu Mitarbeitern haben, identifizieren.
- **Handelsregisterrecherche**: Beteiligungen von Mitarbeitern an Unternehmen, die Geschäftsbeziehungen zur Gesellschaft haben.
- **E-Mail-Analyse**: Kommunikation zwischen Mitarbeiter und bevorteiltem Dritten.
- **Entscheidungsdokumentation**: Wer hat welche Beschaffungsentscheidungen getroffen, und hat er dabei einen Interessenkonflikt verschwiegen?
- **Spesenabrechnungen**: gemeinsame Reisen, Bewirtung mit Begünstigtem.

### 4. Interessenkonflikte von Organmitgliedern
- Aufsichtsratsmitglied: § 101 AktG; kein persönliches Abstimmungsrecht bei eigenen Angelegenheiten.
- Vorstandsmitglied: § 93 AktG; Enthaltungs- und Offenlegungspflicht.
- § 114 AktG: Beraterverträge mit Aufsichtsratsmitglied bedürfen der Zustimmung des Aufsichtsrats ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__114.html)).
- Verletzung: Beschlüsse anfechtbar; Haftung nach § 116 AktG.

### 5. Strafrecht
- § 266 StGB (Untreue): Bevorzugung eines Interessenkonflikt-Begünstigten zum Nachteil der Gesellschaft.
- § 299 StGB: Vorteilsannahme im geschäftlichen Verkehr.
- § 263 StGB: Betrug, wenn Entscheidungen aktiv falsch dargestellt wurden.

### 6. Remediation
- Betroffene Entscheidungen rückwirkend überprüfen: waren sie zum Nachteil der Gesellschaft?
- Schadensersatz gegen Mitarbeiter oder Organmitglied, wenn Schaden nachweisbar.
- Kündigung / Abberufung bei schwerwiegendem, vorsätzlichem Verstoß.
- Code-of-Conduct-Update: klarere Offenlegungspflichten und jährliche Erklärungen.
- Interessenkonflikt-Register einführen.

### 7. Prävention
- Jährliche Interessenkonflikt-Erklärung aller Mitarbeiter in entscheidungsrelevanten Positionen.
- Four-Eyes-Prinzip bei Beschaffungsentscheidungen über bestimmten Schwellenwert.
- Due Diligence für Lieferanten: Verbindungen zu Mitarbeitern prüfen.
- Rotation: Entscheidungsträger in kritischen Beschaffungspositionen regelmäßig rotieren.

## Red-Team-Fragen

- Wurden alle Entscheidungen, die der verdächtige Mitarbeiter in seinem Interessenbereich getroffen hat, systematisch auf Nachteiligkeit überprüft?
- Gibt es familiäre oder freundschaftliche Verbindungen zwischen Entscheidungsträgern und Lieferanten, die im Handelsregister oder in sozialen Netzwerken recherchierbar sind?
- Hat das Organmitglied im Aufsichtsrat abgestimmt, obwohl ein Interessenkonflikt vorlag?
- Deckt die D&O-Versicherung diesen Fall, oder gibt es Ausschlüsse für Interessenkonflikt-Szenarien?
- Ist das Code-of-Conduct-Offenlegungsregime so klar formuliert, dass Mitarbeiter wissen, was offenzulegen ist?
- Sind Schadensersatzansprüche gegen den Täter verjährungsmäßig gesichert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 93 AktG | Treuepflicht Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| § 114 AktG | Beraterverträge Aufsichtsrat | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__114.html) |
| § 60 HGB | Wettbewerbsverbot | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__60.html) |
| § 266 StGB | Untreue | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__266.html) |
| § 299 StGB | Vorteilsannahme | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299.html) |

## Ausgabeformate

- **Interessenkonflikt-Analyse-Matrix** (Person × Entscheidung × Begünstigter × Schaden)
- **Interessenkonflikt-Erklärungsformular** (jährlich)
- **Handelsregister-Recherche-Protokoll**
- **Remediation-Plan** (Code-of-Conduct-Update, Entscheidungsüberprüfung)
- **Schadensersatz-Berechnungsvorlage**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
