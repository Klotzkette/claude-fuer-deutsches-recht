---
name: dsgvo-auskunft-antwort
description: "Für Betroffenenanfragen – Art. 15–22 DSGVO: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# 1. Betroffenenanfragen – Art. 15–22 DSGVO

## 1.1. Eingaben

- Art der Anfrage (Auskunft, Berichtigung, Löschung, Einschränkung, Datenportabilität, Widerspruch, Einwilligungswiderruf)
- Eingangsdatum der Anfrage
- Name, E-Mail-Adresse oder sonstige Angaben des Antragstellers
- Praxisprofil aus `CLAUDE.md` (Systemliste, Identifikationsstandard, DSB)
- Optional: Dokument oder E-Mail der Anfrage

## 1.2. Ablauf

1. **Eingangsklassifikation.**
 - Anfrage-Art bestimmen: Auskunft (Art. 15), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung (Art. 18), Datenportabilität (Art. 20), Widerspruch (Art. 21), Einwilligungswiderruf (Art. 7 Abs. 3)?
 - Mehrfachanfragen erkennen (häufig: kombinierter Auskunfts- und Löschantrag).
 - Handelt es sich um ein Auskunftsersuchen nach IFG/UIG statt DSGVO? (Abgrenzung bei öffentlichen Stellen)

2. **Fristberechnung.**
 - Grundfrist: 1 Monat ab Eingang, Art. 12 Abs. 3 Satz 1 DSGVO.
 - Verlängerung um bis zu 2 Monate möglich bei Komplexität oder Vielzahl von Anfragen, Art. 12 Abs. 3 Satz 2 DSGVO.
 - **Verlängerung erfordert Mitteilung an Betroffenen innerhalb der 1-Monatsfrist** mit Begründung.
 - Fristende berechnen: [Eingangsdatum + 1 Monat] = [Datum]. Verlängerung bis [Datum + 2 Monate].
 - Fristberechnung nach der Verordnung (EWG, Euratom) Nr. 1182/71; entsprechender Kalendertag des Folgemonats, bei fehlendem Tag dessen letzter Tag. Fällt das Ende auf ein Wochenende oder einen Feiertag, gilt der nächste Arbeitstag. EDSA-Leitlinien 01/2022, Version 2.1, Rn. 157–161; keine Verwechslung mit der Verfahrensordnung des EuGH.

3. **Identitätsverifikation.**
 - Ist die Identität des Antragstellers ausreichend nachgewiesen?
 - Standard aus `CLAUDE.md` anwenden.
 - Art. 12 Abs. 6 DSGVO: Bei begründeten Zweifeln kann zusätzliche Information angefordert werden – aber **keine unverhältnismäßige Identifikationshürde** (vgl. EDSA-Leitlinien 01/2022 zu DSAR, Abschn. 3.2).
 - Identitätsprüfung bei Online-Diensten: Konto-Login-Bestätigung oder sichere Alternative; keine Ausweis-Kopien ohne konkreten Zweck (Daten dürfen nicht für andere Zwecke genutzt werden).

4. **Systemabfrage.**
 - Alle relevanten Systeme aus der Systemliste in `CLAUDE.md` durchgehen.
 - Kategorien: CRM, ERP, E-Mail-Archiv, Protokolldateien, Backups, Cloud-Dienste, Sub-AV-Systeme.
 - Für jeden Treffer: Datenkategorie, Verarbeitungszweck, Rechtsgrundlage, Empfänger, Speicherfrist notieren.
 - Keine eigenmächtige Löschung vor Abschluss der Prüfung (Dokumentationspflicht Art. 5 Abs. 2 DSGVO).

5. **Ausnahmenprüfung.**
 - § 34 BDSG (Auskunftsverweigerung, z.B. zur Abwehr von Straftaten, Geschäftsgeheimnisse)
 - § 35 BDSG (eingeschränkte Löschung, z.B. gesetzliche Aufbewahrungsfristen)
 - Art. 17 Abs. 3 DSGVO (kein Löschrecht bei gesetzlicher Aufbewahrungspflicht, Geltendmachung/Verteidigung von Rechtsansprüchen)
 - Art. 15 Abs. 4 DSGVO (Datenkopie darf Rechte Dritter nicht beeinträchtigen)
 - Berufsgeheimnisschutz bei Kanzleien / medizinischen Einrichtungen (§ 203 StGB)
 - Für jede angewandte Ausnahme: konkrete Norm und Begründung dokumentieren.

6. **Antwortentwurf erstellen.**
 - Adressierung korrekt (Name, Adresse aus Anfrage).
 - Positiv-Auskunft oder begründete Ablehnung/Einschränkung.
 - Bei Auskunft: Bestätigung und Zugang zu den eigenen Daten, sämtliche einschlägigen Informationen nach Artikel 15 Absatz 1 Buchstaben a bis h DSGVO, bei Drittlandübermittlung Absatz 2 und die Datenkopie nach Absatz 3. Keine frei erfundene Zahl von Pflichtziffern verwenden.
 - Hinweis auf Beschwerderecht bei Aufsichtsbehörde (Art. 77 DSGVO) in jedem Ablehnungsschreiben.
 - Hinweis auf Klagerecht Art. 79 DSGVO.
 - Auskunft grundsätzlich unentgeltlich; nachgewiesene Ausnahme nach Artikel 12 Absatz 5 DSGVO auch beim Erstantrag prüfen, nicht allein auf Folgeanfragen beschränken.

7. **Dokumentation.**
 - Eingang, Frist, Bearbeitungsschritte, Ausnahmen, Ergebnis im Datenschutzregister erfassen.
 - Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht).

## 1.3. Auskunft über Daten im Verfahren der Aufsicht

Die Datenschutzaufsicht ist für ihre eigene Verarbeitung im Beschwerdeverfahren selbst Verantwortlicher. Nach [EuGH, Urteil vom 05.11.2026, Az. C-205/25, Lindenberg, Rn. 29–47 und 54–67](https://juris.curia.europa.eu/juris/document/document.jsf?docid=316753&doclang=DE) besteht grundsätzlich Auskunft über die eigenen Daten, aber kein allgemeiner Anspruch auf die gesamte Verwaltungsakte. Ermittle Adressat, eigene Daten und konkrete Einschränkungsnorm. Rechte anderer, Behördenunabhängigkeit und Verwaltungsaufwand tragen keine pauschale Verweigerung. Prüfe stattdessen Auszug, Schwärzung oder Anonymisierung unter Erhalt des nötigen Kontexts (Rn. 58–60). Die Behörde nicht mit dem Unternehmen verwechseln, gegen dessen Verarbeitung sich die Beschwerde richtet. Genannte amtliche Passagen am 14.11.2026 gelesen.

## 1.4. Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`. Für Frist und Ausgabeformat [EDSA-Leitlinien 01/2022, Version 2.1, Rn. 153–161](https://www.edpb.europa.eu/system/files/documents/2023-04/edpb_guidelines_202201_data_subject_rights_access_v2_en.pdf) verwenden; diese Behördenauslegung ist kein Gerichtsurteil. Die genannten Passagen wurden am 14.11.2026 geprüft.

- Art. 12 Abs. 3, 4, 5, 6 DSGVO (Fristen, Kosten, Identitätsprüfung)
- Art. 15 DSGVO (Auskunftsrecht, Inhalt)
- Art. 16 DSGVO (Berichtigung)
- Art. 17 DSGVO (Löschung, Ausnahmen)
- Art. 18 DSGVO (Einschränkung)
- Art. 20 DSGVO (Datenportabilität)
- Art. 21 DSGVO (Widerspruch)
- Art. 77 DSGVO (Beschwerderecht Aufsichtsbehörde)
- §§ 34, 35 BDSG (Auskunfts- und Löscheinschränkungen)
- Literatur nur anhand einer vorliegenden Nutzerquelle oder eines verifizierten lizenzierten Zugriffs heranziehen; ungeprüfte Kommentarauflagen und Randnummern nicht verwenden.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 1.5. Beispiel (Auskunftsanfrage)

**Sachverhalt:** Frau M. stellt am 03.06.2024 per E-Mail eine Auskunftsanfrage gemäß Art. 15 DSGVO und bittet zusätzlich um Herausgabe einer Datenkopie (Art. 15 Abs. 3 DSGVO). Kein Kundenkonto, Identität nur per E-Mail bekannt.

**Frist:** Grundfrist endet am 03.07.2024. Verlängerung (Art. 12 Abs. 3 Satz 2 DSGVO) bis 03.09.2024 möglich; Mitteilung an Frau M. spätestens 03.07.2024 erforderlich.

**Identität:** E-Mail-Adresse allein reicht bei reinen Newsletter-Abonnenten aus, wenn keine weiteren personenbezogenen Daten verarbeitet werden. Vgl. EDSA-Leitlinien 01/2022, Abschn. 3.2: Verhältnismäßigkeit der Verifikation.


**Ausnahmen:** § 34 BDSG: keine einschlägigen Tatbestände. Art. 17 Abs. 3 DSGVO: nicht relevant (kein Löschantrag). Keine weiteren Ausnahmen erkennbar.

**Antwortentwurf-Auszug:**
> Sehr geehrte Frau M., vielen Dank für Ihre Anfrage vom 03.06.2024. Gemäß Art. 15 Abs. 1 DSGVO teilen wir Ihnen mit, dass wir folgende personenbezogene Daten über Sie verarbeiten: [Auflistung]. Die Verarbeitung erfolgt zu folgenden Zwecken: [Zwecke], auf Grundlage von [Rechtsgrundlagen]. Im Übrigen stehen Ihnen die in Art. 16–21 DSGVO genannten Rechte zu. Sollten Sie mit unserer Antwort nicht zufrieden sein, steht Ihnen das Beschwerderecht bei der zuständigen Aufsichtsbehörde ([LfDI/BfDI]) gemäß Art. 77 DSGVO sowie das Klagerecht nach Art. 79 DSGVO zu.

## 1.6. Risiken / typische Fehler

- **Fristversäumnis:** Artikel 12 Absatz 4 DSGVO verpflichtet bei Nichttätigwerden zur fristgerechten Begründung und Information über Beschwerde und gerichtlichen Rechtsbehelf. Keine gesetzliche Ablehnungsfiktion behaupten. Verlängerungsmitteilung und ihre Begründung sind eigenständige Pflichten.
- **Unvollständige Systemabfrage:** Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht) verpflichtet zu nachweisbarer vollständiger Prüfung. Backup-Systeme und Archive werden häufig vergessen.
- **Übermäßige Identitätshürde:** Passverlangen ohne Anlass verletzt Art. 12 Abs. 6 DSGVO; EDSA warnt vor übermäßiger Identifizierung als faktischem Abwehrmittel.
- **§ 34 BDSG-Ausnahmen ohne Dokumentation:** Ausnahme muss einzelfallbezogen begründet sein; pauschale Verweigerung "wegen Geschäftsgeheimnisse" ist nicht ausreichend.
- **Datenkopie-Format:** Bei elektronischem Antrag grundsätzlich ein gängiges elektronisches Format verwenden, sofern nichts anderes angegeben wird. Die Information muss verständlich und dauerhaft zugänglich sein. Die zusätzlichen Formatanforderungen der Datenportabilität nach Artikel 20 DSGVO nicht ungeprüft auf Artikel 15 übertragen.


### 1.6.1. Rechtliche Grundlage

Schon der erste Auskunftsantrag kann exzessiv sein, wenn der Verantwortliche nachweist, dass er darauf abzielt, künstlich einen Ersatzanspruch zu schaffen. Zahl früherer Anträge und kurze Zeitabstände sind Indizien, die für sich nicht genügen. Ein Auskunftsverstoß kann Art. 82 DSGVO auslösen. Tatsächlicher Schaden und Kausalität bleiben gesondert zu belegen, auch bei Kontrollverlust oder Unsicherheit. Eine eigene Handlung kann als entscheidende Schadensursache den Zurechnungszusammenhang unterbrechen. [EuGH, Urteil vom 19.03.2026 – C-526/24, Brillen Rottler, Rn. 37–45, 48–55 und 59–67](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62024CJ0526).

Art. 12 Abs. 5 DSGVO erlaubt die Ablehnung eines Auskunftsantrags als "exzessiv" — auch bei Erstantrag, wenn außergewöhnliche Umstände einen Rechtsmissbrauch belegen. Die Hürde ist hoch; das Auskunftsrecht ist ein fundamentales Recht, Ausnahmen sind eng auszulegen.

### 1.6.2. Zweistufiges Prüfschema vor Ablehnung

Beide Stufen müssen kumulativ dokumentiert sein, bevor eine Ablehnung erfolgt:

| Stufe | Inhalt | Dokumentationsanforderung |
|---|---|---|
| **Objektives Element** | Umstände, die auf künstliches Herbeiführen der Situation hindeuten | Zeitachse (Datenerhebung → Anfrage), Art der Datenerhebung, Kommunikationsmuster |
| **Subjektives Element** | Missbräuchliche Absicht, Verfahren zu instrumentalisieren (Ziel: Schadensersatz Art. 82 DSGVO) | Indizien aus Gesamtschau: Formulierungsmuster, sofortige Schadensersatzdrohung, öffentliche Serienaktivität |

**Nicht ausreichend allein:**
- Frühere Anfragen derselben Person
- Öffentlich dokumentiertes massenhaftes Vorgehen dieser Person ohne Einzelfallbezug
- Geltendmachung von Art. 82 DSGVO-Schadensersatz als solche

### 1.6.3. Formulierungsbausteine

**Ablehnungsschreiben (Missbrauch dokumentiert):**

> Sehr geehrte·r [Name], Ihren Antrag auf Auskunft gemäß Art. 15 DSGVO vom [DATUM] lehnen wir gemäß Art. 12 Abs. 5 Satz 2 Alt. 2 DSGVO als offenkundig exzessiv ab. Im Einzelnen stützen wir die Ablehnung auf folgende dokumentierte Umstände:
>
> 1. [Konkrete belegte Gesamtumstände erläutern; ein kurzer Zeitraum zwischen Anmeldung und Antrag genügt allein nicht.]
> 2. [Belegen, weshalb die Gesamtumstände eine Absicht zur künstlichen Schaffung eines Schadensersatzanspruchs nachweisen; eine Schadensersatzankündigung allein genügt nicht.]
>
>
> Sie haben das Recht, gegen diese Entscheidung Beschwerde bei [zuständige Aufsichtsbehörde] gemäß Art. 77 DSGVO oder Klage gemäß Art. 79 DSGVO zu erheben.

**Internes Dokumentationsprotokoll (Pflicht vor Ablehnung):**

```
Datum der Ablehnung: [DATUM]
Antragsdatum: [DATUM]
Datum der Datenerhebung: [DATUM]
Abstand Datenerhebung → Antrag: [N] Tage

Objektives Element (Belege):
- [Nachweis 1: z.B. Newsletter-Anmeldedaten]
- [Nachweis 2: z.B. Screenshot/E-Mail]

Subjektives Element (Belege):
- [Nachweis: z.B. Wortlaut des Antragsschreibens, sofortige Schadensersatzankündigung]

Gesamtwürdigung: [Begründung in eigenen Worten]
Verantwortlich (DSB-Freigabe): [Name, Datum]
```

### 1.6.4. Schadensersatzrisiko bei unberechtigter Ablehnung

- Eine Ablehnung ohne vollständigen zweistufigen Nachweis ist ein eigenständiger DSGVO-Verstoß.
- Dieser Verstoß kann bei nachgewiesenem Schaden und Kausalität einen Schadensersatzanspruch nach Art. 82 DSGVO begründen — auch wenn die zugrundeliegende Datenverarbeitung vollständig DSGVO-konform war.
- Der bloße Verstoß genügt nicht automatisch; die betroffene Person muss einen konkreten materiellen oder immateriellen Schaden darlegen (z.B. Kontrollverlust, Ungewissheit über Datenverarbeitung). Kein verschuldensunabhängiges Haftungsregime.
- Eigenverschulden der betroffenen Person (wenn ihr eigenes Verhalten die entscheidende Schadensursache ist) schließt den Anspruch aus.

### 1.6.5. Konsequenz für die Antwortformulierung

**Empfehlung:** Im Zweifel Auskunft vollständig und fristgerecht erteilen. Ablehnung nur bei lückenlos dokumentiertem zweistufigen Nachweis und nach DSB-Freigabe. Alternativ: Auskunft erteilen und Gebühr nach Art. 12 Abs. 5 Satz 2 Alt. 1 DSGVO erheben (ebenfalls nur bei dokumentiertem Exzess).

**Perspektive betroffene Person:** Anfragen sollen erkennbar dem Zweck der Transparenz dienen. Schadensersatz nach Art. 82 DSGVO ist auch bei reiner Auskunftsverletzung möglich — konkreten Schaden (Kontrollverlust, Ungewissheit) in Klage- oder Beschwerdeschrift substantiiert darlegen.

### 1.6.6. Querverweise

- `datenschutzrecht/skills/dsgvo-auskunft/FACHINHALT.md` — Abschnitt "Rechtsmissbrauch" mit vollständigem Prüfschema und Indizien-Checkliste

## 1.7. Triage zu Beginn

1. Wer fragt aus? Mitarbeiter (§§ 34/35 BDSG prüfen) / Kunde / Vertragspartner / unbekannte Person
2. Identitätsverifizierung erforderlich (Zweifel? Art. 12 Abs. 6 DSGVO → Nachweise anfordern)?
3. Fristberechnung: Eingang [DATUM] → Ablauf 1 Monat: [DATUM]; Verlängerung möglich bis [DATUM]?
4. Ausnahmetatbestände (§§ 34, 35 BDSG; Rechte Dritter Art. 15 Abs. 4; Geschäftsgeheimnisse)?

## 1.8. Output-Template — Auskunftsantwort formal

**Adressat:** Betroffene Person — Tonfall: verständlich-erklärend

```
[ORGANISATION, ADRESSE]
[DATUM]

Betreff: Auskunft nach Art. 15 DSGVO — Ihr Ersuchen vom [DATUM]
Unser Zeichen: [AZ]

Sehr geehrte/r Frau/Herr [NAME BETROFFENE PERSON],

wir erteilen Ihnen hiermit Auskunft über die Verarbeitung Ihrer
personenbezogenen Daten gemäß Art. 15 DSGVO:

1. Verarbeitungszwecke (Art. 15 Abs. 1 lit. a): [ZWECKE]
2. Datenkategorien (Art. 15 Abs. 1 lit. b): [KATEGORIEN]
3. Empfänger (Art. 15 Abs. 1 lit. c): [EMPFAENGER]
4. Speicherdauer (Art. 15 Abs. 1 lit. d): [FRIST/KRITERIEN]
5. Rechte (Art. 15 Abs. 1 lit. e und f): Berichtigung, Löschung, Einschränkung
 und Widerspruch nach den jeweiligen Voraussetzungen sowie Beschwerde
 bei [AUFSICHTSBEHOERDE].
6. Herkunft der Daten (Art. 15 Abs. 1 lit. g): [HERKUNFT]
7. Automatisierte Entscheidungen (Art. 15 Abs. 1 lit. h): [Bestehen und,
 soweit einschlägig, verständliche Information über Logik, Tragweite und Folgen].
8. Drittlandübermittlung (Art. 15 Abs. 2): [Übermittlung und gegebenenfalls
 geeignete Garantien nach Art. 46 verständlich erläutern].

Datenkopie gemäß Art. 15 Abs. 3 DSGVO: [ANLAGE / Ablehnung mit Begruendung]

[Ggf. Ausnahmen: § 34 BDSG / § 35 BDSG / Art. 15 Abs. 4 DSGVO: [BEGRUENDUNG]]

Mit freundlichen Grüßen
[NAME, FUNKTION, DSB-KONTAKT]
```



<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
