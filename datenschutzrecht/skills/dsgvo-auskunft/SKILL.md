---
name: dsgvo-auskunft
description: "Unterstützt bei der Bearbeitung von Auskunftsersuchen nach Art. 15 DSGVO – von der Identifizierung der betroffenen Person über Fristeinhaltung bis zur Formulierung der Auskunft und Prüfung von Ausnahmegründen. Lädt, wenn ein Mandant ein Auskunftsverlangen erhält oder stellen möchte."
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
