---
name: dsgvo-auskunft
description: "Auskunftsersuchen nach Art. 15 DSGVO pruefen und beantworten wenn Betroffener Auskunft verlangt. Art. 15 12 DSGVO Betroffenenrechte. Pruefraster: Identitaetsnachweis Vollstaendigkeitspruefung Auskunftsinhalt Fristen Einschraenkungsgruende. Output: Auskunftserteilung oder Ablehnungsbegrundung. Abgrenzung: nicht fuer Auskunftsantwort-Gestaltung (dsgvo-auskunft-antwort)."
---

# DSGVO-Auskunftsrecht (Art. 15 DSGVO)

## Zweck

Dieser Skill begleitet Verantwortliche (und deren Berater) bei der vollständigen und fristgerechten Bearbeitung von Auskunftsersuchen nach Art. 15 DSGVO. Er deckt ebenso die Beratung betroffener Personen ab, die ein Auskunftsverlangen stellen wollen. Anwendungsfälle: Unternehmen erhält Auskunftsanfrage eines Kunden, ehemaligen Mitarbeiters oder Behörde; Arbeitnehmer fragt nach gespeicherten HR-Daten; Betroffener begehrt Auskunft von Auskunftei.

## Eingaben

Das Modell benötigt folgende Informationen:

- **Rolle des Mandanten**: Verantwortlicher (Art. 4 Nr. 7 DSGVO) oder betroffene Person?
- **Inhalt des Ersuchens**: Liegt ein schriftliches/mündliches Verlangen vor? Vollständiger Text?
- **Eingangsdatum** des Ersuchens (für Fristberechnung entscheidend)
- **Identitätsstatus**: Ist die betroffene Person zweifelsfrei identifiziert oder bestehen Zweifel?
- **Datenkategorien und -systeme**: Welche Daten werden verarbeitet (CRM, HR, Protokolldateien)?
- **Ausnahmetatbestände**: Gibt es Anhaltspunkte für § 34 BDSG, § 29 Abs. 1 BDSG, Berufsgeheimnis?
- **Bereits erteilte Auskünfte**: Frühere Anfragen derselben Person in den letzten 12 Monaten?

## Rechtlicher Rahmen

### Primärnormen

- **Art. 15 Abs. 1 DSGVO**: Anspruch auf Bestätigung der Verarbeitung und Auskunft über Kategorien, Zwecke, Empfänger, Speicherdauer, Herkunft, automatisierte Entscheidungsfindung.
- **Art. 15 Abs. 3 DSGVO**: Anspruch auf Kopie der verarbeiteten personenbezogenen Daten; bei elektronischer Antragstellung in gängigem elektronischem Format.
- **Art. 12 Abs. 3 DSGVO**: Frist von einem Monat ab Eingang des Ersuchens; Verlängerung um bis zu zwei weitere Monate bei Komplexität oder Vielzahl von Anfragen – Mitteilung über Verlängerung und Gründe innerhalb eines Monats.
- **Art. 12 Abs. 5 DSGVO**: Unentgeltlichkeit; bei offenkundig unbegründeten oder exzessiven Anträgen: Gebühr oder Ablehnung möglich.
- **§ 34 BDSG**: Ausnahmen vom Auskunftsrecht, insbesondere bei Vertraulichkeitspflichten, Gefährdung öffentlicher Ordnung, Unmöglichkeit oder unverhältnismäßigem Aufwand.
- **§ 29 Abs. 1 BDSG**: Einschränkungen bei Datenverarbeitung zu journalistischen oder wissenschaftlichen Zwecken sowie bei Berufsgeheimnisträgern.

### Leitentscheidungen

1. EuGH, Urt. v. 04.05.2023 – C-487/21 (Österreichische Datenschutzbehörde), NJW 2023, 2253 Rn. 32–45: Der Begriff „Kopie" in Art. 15 Abs. 3 DSGVO meint keine bloße Zusammenfassung, sondern eine originalgetreue Reproduktion der personenbezogenen Daten. Der Kontext der Daten muss erkennbar sein; eine strukturierte Zusammenstellung genügt nur, wenn alle Daten enthalten sind.

2. BGH, Urt. v. 15.06.2021 – VI ZR 576/19, NJW 2021, 2726 Rn. 18–24: Der Auskunftsanspruch aus Art. 15 DSGVO ist grundsätzlich nicht auf besondere Kategorien von Daten beschränkt. Der Verantwortliche muss alle verarbeiteten personenbezogenen Daten benennen; eine pauschale Verweisung auf Datenspeichersysteme genügt nicht. Das Gericht stellt klar, dass der Anspruch auch gegenüber Versicherern bezüglich Vorgangsdaten aus Schadensregulierung besteht.

### Kommentarliteratur

1. Franck, in: Gola/Heckmann, DSGVO/BDSG, 3. Aufl. 2022, Art. 15 DSGVO Rn. 12–28: Zur Reichweite der Datenkopie und der Pflicht, Metadaten sowie Verarbeitungszwecke vollständig mitzuteilen; Abgrenzung zur bloßen Beschreibung des Datenbestands.

2. Schmidt-Wudy, in: BeckOK Datenschutzrecht, 47. Ed. (Stand 01.02.2025), Art. 15 DSGVO Rn. 35–60: Ausführlich zu Identifizierungspflicht, Verhältnis des Auskunftsrechts zu Betriebs- und Geschäftsgeheimnissen, Prüfung exzessiver Anfragen sowie Abgrenzung zu nationalen Ausnahmen nach § 34 BDSG.

## Ablauf

**Schritt 1 – Eingangserfassung und Fristsetzen**
- Eingangsdatum dokumentieren; 1-Monatsfrist nach Art. 12 Abs. 3 DSGVO berechnen.
- Prüfen, ob Verlängerung um 2 Monate wegen Komplexität in Betracht kommt – wenn ja, Mitteilung an Betroffenen innerhalb der ersten Monatsfrist (Art. 12 Abs. 3 Satz 3 DSGVO).

**Schritt 2 – Identifizierung der betroffenen Person**
- Ausreichende Identifizierung verlangen, wenn Zweifel bestehen (Art. 12 Abs. 6 DSGVO); kein unverhältnismäßiges Nachforschungsrecht des Verantwortlichen.
- Bei Online-Diensten: E-Mail-Abgleich, ggf. Sicherheitsfrage; keine Forderung nach Ausweis-Scan ohne konkreten Anlass.

**Schritt 3 – Dateninventur**
- Systematische Abfrage aller betroffenen Systeme: CRM, ERP, E-Mail-Archive, Protokolldateien, Backups (soweit zugänglich), Cloud-Dienste, Auftragsverarbeiter (Art. 28 Abs. 3 lit. f DSGVO).
- Beauftragung von Auftragsverarbeitern, relevante Daten zu melden (Art. 28 Abs. 3 lit. f DSGVO).

**Schritt 4 – Prüfung von Ausnahmetatbeständen**
- § 34 Abs. 1 BDSG: Vertraulichkeit steuerlicher Daten; § 34 Abs. 2 BDSG: Daten zu präventiven und repressiven Zwecken.
- § 29 Abs. 1 BDSG: Berufsgeheimnisträger (Rechtsanwälte, Ärzte, Steuerberater); Drittinteressen nach Art. 15 Abs. 4 DSGVO (Geschäftsgeheimnisse).
- Konkurrierende Interessen nach ErwGr. 63 DSGVO abwägen.

**Schritt 5 – Auskunftserteilung**
- Umfang gem. Art. 15 Abs. 1 lit. a–h DSGVO vollständig abarbeiten; Datenkopie (Art. 15 Abs. 3 DSGVO) beilegen.
- Gebührenfreie erste Kopie; Folgeantrag kann kostenpflichtig sein.
- Bei Ablehnung: schriftliche Begründung + Hinweis auf Beschwerderecht bei Aufsichtsbehörde (Art. 12 Abs. 4 DSGVO).

**Schritt 6 – Dokumentation**
- Interne Dokumentation der Anfrage, Prüfschritte, Ergebnis und Versanddatum (Nachweispflicht Art. 5 Abs. 2 DSGVO).

## Ausgabeformat

- **Auskunftsschreiben** (Brief oder E-Mail) an Betroffenen: strukturierte Tabelle der Datenkategorien, Zwecke, Empfänger, Fristen; Anlage: Datenkopie.
- **Internes Prüfmemo** (bei komplexen Fällen): Tatbestand, Rechtslage, Ausnahmeprüfung, Ergebnis, Fristprotokoll.
- **Ablehnungsschreiben** mit Begründung und Belehrung über Beschwerderecht.
- Stil: klar, präzise, ohne Fachjargon gegenüber dem Betroffenen; juristisch präzise im Mandanten-Memo.

## Beispiel

**Sachverhalt**: Ehemalige Mitarbeiterin M verlangt am 03.02.2025 per E-Mail Auskunft über alle sie betreffenden Daten sowie eine Datenkopie gemäß Art. 15 DSGVO vom Unternehmen U.

**Gutachtenstil**:

*Frist*: Die einmonatige Frist des Art. 12 Abs. 3 Satz 1 DSGVO läuft bis zum 03.03.2025. Eine Verlängerung setzt voraus, dass U spätestens bis 03.03.2025 unter Angabe der Gründe Mitteilung macht (Art. 12 Abs. 3 Satz 3 DSGVO).

*Umfang*: U hat M Auskunft über sämtliche Datenkategorien (Art. 15 Abs. 1 lit. a–h DSGVO) zu erteilen, einschließlich HR-Stammdaten, Entgeltabrechnungen, E-Mail-Kommunikation, Zugangsdaten und Protokolldateien. Gemäß EuGH, Urt. v. 04.05.2023 – C-487/21 Rn. 40, muss die Datenkopie die Daten in ihrer ursprünglichen Form reproduzieren; eine zusammenfassende Übersicht genügt nicht.

*Ausnahmen*: Soweit E-Mails Geschäftsgeheimnisse Dritter enthalten, sind diese nach Art. 15 Abs. 4 DSGVO i.V.m. ErwGr. 63 DSGVO zu schwärzen. § 34 BDSG greift hier nicht, da keine der dort genannten Konstellationen vorliegt.

*Ergebnis*: U erteilt bis 03.03.2025 vollständige Auskunft mit geschwärzter Datenkopie und dokumentiert den Vorgang intern (Art. 5 Abs. 2 DSGVO).

## Risiken und typische Fehler

- **Fristversäumnis**: 1 Monat ab Eingang (nicht ab Bearbeitung); Verlängerung muss innerhalb der ersten Monatsfrist mitgeteilt werden – BGH, Urt. v. 15.06.2021 – VI ZR 576/19, NJW 2021, 2726 Rn. 20.
- **Unvollständige Datenermittlung**: Fehlende Protokolldateien, Backup-Daten oder Cloud-Systeme begründen Pflichtverletzung; Beweislast beim Verantwortlichen (Art. 5 Abs. 2 DSGVO).
- **Datenkopie unterschätzt**: Bloße Kategorienauflistung ohne tatsächliche Datenkopie verletzt Art. 15 Abs. 3 DSGVO (EuGH C-487/21).
- **Identifizierung übertrieben**: Unverhältnismäßige Ausweispflicht abwehren; Art. 12 Abs. 6 DSGVO erlaubt zusätzliche Informationen nur bei begründetem Zweifel.
- **§ 34 BDSG-Ausnahme zu weit**: Ausnahmen sind restriktiv auszulegen; pauschale Berufung auf „unverhältnismäßigen Aufwand" ohne konkrete Begründung genügt nicht.
- **Berufsrecht**: Bei anwaltlicher Beratung des Verantwortlichen: Keine unzulässige Auskunftsverzögerung; § 43a Abs. 2 BRAO (Gewissenhaftigkeit) gebietet korrekte Beratung zur Frist.
- **Mehrfachanträge**: Erst bei offenkundig exzessivem Verhalten darf Gebühr erhoben werden (Art. 12 Abs. 5 DSGVO); Dokumentationspflicht der Exzessivität.

## Quellenpflicht

Jede juristische Aussage in Auskunftsschreiben, Memos und Ablehnungsschreiben ist nach dem Standard in `references/zitierweise.md` zu belegen. Mindestens zwei Rechtsprechungsbelege im BGH-Stil und zwei Kommentarbelege im Bearbeiter-Stil. Nicht belegte Rechtsbehauptungen gelten als Qualitätsfehler. Bei fehlendem Rspr.-Nachweis zu einzelnen Rechtsfragen ist dies ausdrücklich zu kennzeichnen und durch Kommentarliteratur zu kompensieren.

## Rechtsmissbrauch (Art. 12 Abs. 5 DSGVO) — EuGH C-526/24

### Leitentscheidung

EuGH, Urt. v. 19.03.2026 – C-526/24 (Brillen Rottler), Vorabentscheidung auf Vorlage AG Arnsberg; Schlussanträge GA Maciej Szpunar v. 12.09.2025 in C-526/24.

### Grundsatz

Auch ein erstmaliger Auskunftsantrag kann „exzessiv" i.S.d. Art. 12 Abs. 5 DSGVO und damit rechtsmissbräuchlich sein — nicht nur bei einer Vielzahl von Anfragen (quantitativ), sondern auch qualitativ. Da das Auskunftsrecht ein fundamentales Recht ist, sind die Ausnahmen nach Art. 12 Abs. 5 DSGVO eng auszulegen; Rechtsmissbrauch setzt außergewöhnliche Umstände voraus. Die Beweislast für das Vorliegen von Rechtsmissbrauch liegt beim Verantwortlichen.

### Zweistufiges Prüfschema (objektives + subjektives Element)

Der Verantwortliche muss kumulativ nachweisen:

**Stufe 1 — Objektives Element:**
Umstände, die auf ein künstliches Herbeiführen der Anfragesituation hindeuten, z.B.:
- Ungewöhnlich kurzer Zeitabstand zwischen Datenerhebung und Auskunftsantrag
- Gezielte Anmeldung zu einem Newsletter o.Ä. kurz vor Antragstellung ohne erkennbares Informationsinteresse
- Dokumentiertes Muster massenhaften Vorgehens (öffentlich bekannte Serienanfragen)

**Stufe 2 — Subjektives Element:**
Missbräuchliche Absicht der betroffenen Person, das Verfahren zu instrumentalisieren — insbesondere um einen Schadensersatzanspruch nach Art. 82 DSGVO künstlich herbeizuführen.

### Indizien-Checkliste (Gesamtschau Einzelfall)

| Indiz | Gewicht | Erläuterung |
|---|---|---|
| Zeitpunkt und Abstand Datenerhebung → Anfrage | mittel–hoch | Sehr kurzer Abstand ohne erkennbaren Anlass erhöht Missbrauchsverdacht |
| Art der Datenerhebung (aktive Anmeldung kurz vor Anfrage) | hoch | Spricht für künstliches Herbeiführen der Situation |
| Verhalten vor und nach Antragstellung | mittel | Kommunikationsmuster, öffentliche Äußerungen |
| Art der Kommunikation | mittel | Formulierungsgleichheit mit Serienmustern, sofortiger Schadensersatzhinweis |
| Öffentlich dokumentiertes massenhaftes Vorgehen | allein nicht ausreichend | EuGH C-526/24: Für sich genommen kein Missbrauchsnachweis |
| Frühere ähnliche Anfragen derselben Person | allein nicht ausreichend | Geltendmachung von Rechten ist nicht per se missbräuchlich |

### Konsequenzen für den Verantwortlichen

- **Ablehnung nur bei vollständigem Nachweis beider Stufen:** Weder das objektive noch das subjektive Element allein genügt; beide müssen durch konkrete, dokumentierte Umstände belegt werden.
- **Dokumentationspflicht:** Alle zur Ablehnung herangezogenen Umstände sind intern zu dokumentieren (Zeitachse, Newsletter-Anmeldedaten, Korrespondenzverlauf) — Rechenschaftspflicht Art. 5 Abs. 2 DSGVO.
- **Risiko unberechtigter Ablehnung:** Lehnt der Verantwortliche eine Auskunft ab, ohne den zweistufigen Nachweis führen zu können, stellt dies einen eigenständigen DSGVO-Verstoß dar, der einen eigenständigen Schadensersatzanspruch nach Art. 82 DSGVO auslöst — auch wenn die zugrundeliegende Datenverarbeitung selbst vollständig DSGVO-konform war.
- **Kein Automatismus beim Schadensersatz:** Der bloße Verstoß löst nicht automatisch Schadensersatz aus; die betroffene Person muss den konkreten materiellen oder immateriellen Schaden darlegen (Kontrollverlust, Ungewissheit über Verarbeitung). Kein verschuldensunabhängiges Haftungsregime.
- **Eigenverschulden der betroffenen Person:** Ist das Verhalten der betroffenen Person selbst die entscheidende Schadensursache, entfällt der Anspruch.

### Empfehlung

Vorzugsweise vollständige, fristgerechte Auskunft erteilen. Ablehnung nur als ultima ratio bei lückenlos dokumentiertem zweistufigen Nachweis. Im Zweifel Auskunft erteilen und ggf. Gebühr nach Art. 12 Abs. 5 DSGVO erheben.

### Querverweise

- `datenschutzrecht/skills/dsgvo-auskunft-antwort/SKILL.md` — Abschnitt „Ablehnung wegen Rechtsmissbrauch" mit Formulierungsbausteinen

## Ergänzende Rechtsprechung (Aktualitäten)

### EuGH C-579/21 — Protokolldaten als Gegenstand des Auskunftsrechts

EuGH, Urt. v. 22.06.2023 – C-579/21 (Pankki S), NJW 2023, 2545: Das Auskunftsrecht nach Art. 15 DSGVO umfasst auch Protokolldaten (Zugriffsprotokolle, Log-Dateien), in denen die betroffene Person als Benutzer oder als betroffene Person erfasst ist, sofern diese Daten personenbezogene Daten i.S.d. Art. 4 Nr. 1 DSGVO darstellen. Der Verantwortliche kann die Auskunft über solche Protokolldaten nicht allein mit dem Hinweis verweigern, dass die Protokollierung primär IT-Sicherheitszwecken dient. Maßgeblich ist, ob die Daten die betroffene Person identifizieren oder identifizierbar machen. Konsequenz für die Praxis: Protokolldaten (Server-Logs, Zugangsprotokolle, Datenbankzugriffe) sind systematisch in die Dateninventur nach Schritt 3 einzubeziehen.

### Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei weiteren EuGH-Vorabentscheidungen zu Art. 15 DSGVO sowie bei EDSA-Leitlinien zu Auskunftsersuchen. Nächste Überprüfung: 05/2027 oder bei wesentlichen Änderungen.

## Aktuelle Rechtsprechung (v14.2 — Ergaenzung)

- EuGH, Urt. v. 26.10.2023 — C-307/22 (FT/Bundesrepublik Deutschland/Zahnarzt), NJW 2024, 88 Rn. 42–55: Art. 15 DSGVO begründet ein Recht auf unentgeltliche erste Auskunftskopie; der Verantwortliche kann für weitere Kopien ein angemessenes Entgelt verlangen (Art. 15 Abs. 3 Satz 2 DSGVO). Der Auskunftsanspruch wird nicht durch berufsrechtliche Verschwiegenheitspflichten des Verantwortlichen eingeschränkt.
- BGH, Urt. v. 15.11.2022 — VI ZR 617/20, NJW 2023, 512 Rn. 28: Zur Durchsetzbarkeit des Art. 15 DSGVO-Auskunftsanspruchs im Klagewege; fehlende oder unvollständige Auskunft begründet Anspruch auf Schadensersatz nach Art. 82 DSGVO und Ordnungsgeld nach § 888 ZPO bei Weigerung.

## Triage zu Beginn

1. Wer stellt das Auskunftsersuchen (Mitarbeiter, Kunde, Wettbewerber im Rechtsstreit)?
2. Liegt eine Identitätsverifizierung vor (Art. 12 Abs. 6 DSGVO — Nachweise anfordern bei Zweifeln)?
3. Wann ist das Ersuchen eingegangen? (1-Monatsfrist nach Art. 12 Abs. 3 DSGVO berechnen)
4. Besteht ein Ausnahmetatbestand (§§ 34, 35 BDSG; Art. 14 Abs. 5 DSGVO)?

## Output-Template — Auskunftsantwort (Kurzform)

**Adressat:** Betroffene Person — Tonfall: verständlich-erklärend, sachlich

```
Sehr geehrte/r Frau/Herr [NAME BETROFFENE PERSON],

wir bestätigen den Eingang Ihres Auskunftsersuchens vom [DATUM] und erteilen
Ihnen hiermit Auskunft gemäß Art. 15 DSGVO:

1. Verarbeitete Datenkategorien:
   [LISTE NACH Art. 15 Abs. 1 lit. a DSGVO]

2. Verarbeitungszwecke: [ZWECKE]

3. Empfänger / Kategorien von Empfängern: [LISTE]

4. Speicherdauer / -kriterien: [FRIST ODER KRITERIEN]

5. Rechte: Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung (Art. 18),
   Widerspruch (Art. 21), Beschwerde Aufsichtsbehörde (Art. 77 DSGVO): [BEHOERDE].

6. Datenkopie: [ANLAGE / GESONDERT ÜBERMITTELT]

[Unterschrift, Datenschutzbeauftragter]
[DATUM]
```
