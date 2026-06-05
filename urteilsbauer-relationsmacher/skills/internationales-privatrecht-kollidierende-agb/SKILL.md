---
name: internationales-privatrecht-kollidierende-agb
description: "Internationales Privatrecht Kollidierende AGB: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Internationales Privatrecht Kollidierende AGB

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Internationales Privatrecht Kollidierende AGB** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `internationales-privatrecht` | Anwendbares Recht bei grenzüberschreitenden Vertraegen und Delikten bestimmen: Auslandsbezug im Prozess erfordert IPR-Prüfung. Normen: Rom-I-VO (vertragliche Schuldverhältnisse), Rom-II-VO (außervertragliche), Art. 4 ff. EGBGB (autonomes IPR), Art. 9 Rom-I (Eingriffsnormen, z.B. DSGVO). Prüfraster: Rechtswahlklausel, Anknuepfung ohne Rechtswahl, Eingriffsnormen, ordre public Art. 21 Rom-I, Verhältnis zu CISG. Output IPR-Prüfschema, anwendbares Recht. Abgrenzung: CISG siehe cisg-prüfen; Incoterms siehe incoterms-und-gefahruebergang; EU-Zuständigkeit siehe zulässigkeit-prüfen. |
| `kollidierende-agb-pruefen` | Kollidierende AGB im B2B-Verkehr (Battle of the Forms) lösen: Kaufvertrag mit beiderseitigen AGB und widerspruechen. Normen: §§ 305-310 BGB (AGB-Recht B2B), CISG Art. 19 (Annahme mit Abweichungen). Prüfraster: Last-Shot-Doctrine, Knock-out-Regel (Restgueltigkeit), Rechtswahlklauseln, Gerichtsstandsklauseln, Schiedsklauseln, Haftungsbeschraenkungen, Eigentumsvorbehalt. Output Lösungs-Memo mit Vertragsinhalt nach Battle of the Forms. Abgrenzung: AGB-Kontrolle allgemein siehe Vertragsrecht-Plugin; CISG spezifisch siehe cisg-prüfen. |
| `kostenentscheidung-bauen` | Kostenentscheidung nach §§ 91 ff. ZPO erstellen: Richter muss Kostenquote und -grundentscheidung formulieren. Normen: § 91 ZPO (vollständiges Obsiegen), § 92 ZPO (teilweises Obsiegen), § 100 ZPO (mehrere Beklagte), § 101 ZPO (Streitgenossenschaft/Nebenintervenient), § 93 ZPO (sofortiges Anerkenntnis). Prüfraster: Obsiegens-Quote, Streitwert-Aufteilung, Nebenintervenient, sofortiges Anerkenntnis. Output Kostenentscheidung-Entwurf mit Quote. Abgrenzung: Vollstreckbarkeit siehe vorlaeufige-vollstreckbarkeit; Rechtsmittelbelehrung siehe rechtsmittelbelehrung-zivil. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Internationales Privatrecht Kollidierende AGB**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `internationales-privatrecht`

**Fokus:** Anwendbares Recht bei grenzüberschreitenden Vertraegen und Delikten bestimmen: Auslandsbezug im Prozess erfordert IPR-Prüfung. Normen: Rom-I-VO (vertragliche Schuldverhältnisse), Rom-II-VO (außervertragliche), Art. 4 ff. EGBGB (autonomes IPR), Art. 9 Rom-I (Eingriffsnormen, z.B. DSGVO). Prüfraster: Rechtswahlklausel, Anknuepfung ohne Rechtswahl, Eingriffsnormen, ordre public Art. 21 Rom-I, Verhältnis zu CISG. Output IPR-Prüfschema, anwendbares Recht. Abgrenzung: CISG siehe cisg-prüfen; Incoterms siehe incoterms-und-gefahruebergang; EU-Zuständigkeit siehe zulässigkeit-prüfen.

# Internationales Privatrecht

Bei Auslandsbezug immer prüfen, welches Recht zur Anwendung kommt.


## Triage zu Beginn

1. Liegt überhaupt Auslandsbezug vor (Sitz der Parteien, Erfüllungsort, Schadensort)?
2. Welches EU-Kollisionsrecht ist einschlägig — Rom-I (Vertrag) oder Rom-II (Delikt/Bereicherung)?
3. Haben die Parteien eine wirksame Rechtswahl getroffen (Art. 3 Rom-I)?
4. Ist CISG vorrangig anwendbar (vor dem IPR-Kollisionsrecht)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- Verordnung (EG) Nr. 593/2008 (Rom-I) — vertragliche Schuldverhältnisse
 - Art. 3: Rechtswahl
 - Art. 4: Anknüpfung ohne Wahl (charakteristische Leistung)
 - Art. 6: Verbraucherverträge (Schutz des Verbrauchers)
 - Art. 9: Eingriffsnormen (DSGVO, AGB-Recht, Datenschutz)
- Verordnung (EG) Nr. 864/2007 (Rom-II) — außervertragliche Schuldverhältnisse
 - Art. 4: Erfolgsortprinzip
- Art. 3 ff. EGBGB — autonomes deutsches IPR
- CISG — internationales Einheitskaufrecht, vorrangig

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Auslandsbezug feststellen:** Welche Anknüpfungspunkte liegen im Ausland?
2. **Vorrang prüfen:** CISG anwendbar? Wenn ja: CISG gilt, kein IPR nötig.
3. **Rom-I oder Rom-II:** Vertragliches Schuldverhältnis → Rom-I; außervertraglich → Rom-II.
4. **Rechtswahl prüfen (Art. 3 Rom-I):** Wirksame Vereinbarung? Ausdrücklich oder konkludent?
5. **Anknüpfung ohne Wahl (Art. 4 Rom-I):** Charakteristische Leistung bestimmen.
6. **Eingriffsnormen (Art. 9 Rom-I):** DSGVO, AGB-Recht, Mietrecht (§ 565 BGB) etc.
7. **Ordre public (Art. 21 Rom-I):** Greifen Kernwerte des deutschen Rechts ein?

## Output-Template

**Adressat:** Entscheidungsgründe — Tonfall: sachlich-juristisch

```
## Anwendbares Recht (IPR)

**Auslandsbezug:** [Beklagte hat Sitz in USA / Erfüllungsort in Schweiz / Schaden in Deutschland].

**CISG:** [Das CISG ist anwendbar / nicht anwendbar, weil ...]

**Kollisionsrecht (Rom-I):** Das Schuldverhältnis ist vertraglich. Die Parteien haben [keine]
Rechtswahl getroffen. Nach Art. 4 Abs. 1 lit. a Rom-I gilt das Recht des Staates, in dem der
Verkäufer seinen gewöhnlichen Aufenthalt hat: [STAAT].

**Eingriffsnormen:** Die DSGVO ist als Eingriffsnorm (Art. 9 Rom-I) anwendbar.
```

## Reihenfolge

1. **Völker- und EU-rechtliche Vorrang-Regeln**: CISG, FAA, COTIF, Montrealer Übereinkommen, MARPOL usw.
2. **EU-Verordnungen**: Rom-I (Verordnung Nr. 593 2008), Rom-II (Verordnung Nr. 864 2007), Rom-III (Familiensachen)
3. **Bilaterale Abkommen** (z. B. mit Iran)
4. **Autonomes deutsches IPR**: Artikel 3 ff EGBGB

## Rom-I

- Artikel 3: Rechtswahl
- Artikel 4: ohne Rechtswahl - Anknuepfung an die charakteristische Leistung
- Artikel 6: Verbraucherverträge - günstigeres Recht des gewoehnlichen Aufenthalts des Verbrauchers
- Artikel 9: Eingriffsnormen des Forums (DSGVO ist Eingriffsnorm im Sinne dieser Vorschrift, Erwaegungsgrund 81 Rom-I, st. Rspr. der nationalen Gerichte und EuGH)
- Artikel 21: ordre public

## Rom-II

- Artikel 4: Erfolgsortprinzip
- Artikel 17: Sicherheits- und Verhaltensregeln am Handlungsort

## Eingriffsnormen

DSGVO Artikel 3 (raeumlicher Anwendungsbereich) ist Eingriffsnorm. Das deutsche Datenschutzrecht ist auf Verarbeitungen anwendbar, die sich an Personen in der EU richten, unabhängig vom Sitz des Verantwortlichen.

## 2. `kollidierende-agb-pruefen`

**Fokus:** Kollidierende AGB im B2B-Verkehr (Battle of the Forms) lösen: Kaufvertrag mit beiderseitigen AGB und widerspruechen. Normen: §§ 305-310 BGB (AGB-Recht B2B), CISG Art. 19 (Annahme mit Abweichungen). Prüfraster: Last-Shot-Doctrine, Knock-out-Regel (Restgueltigkeit), Rechtswahlklauseln, Gerichtsstandsklauseln, Schiedsklauseln, Haftungsbeschraenkungen, Eigentumsvorbehalt. Output Lösungs-Memo mit Vertragsinhalt nach Battle of the Forms. Abgrenzung: AGB-Kontrolle allgemein siehe Vertragsrecht-Plugin; CISG spezifisch siehe cisg-prüfen.

# Kollidierende AGB

Klassisches Problem im B2B-Geschäft: Beide Parteien verweisen auf ihre eigenen AGB, die widersprechen sich.


## Triage zu Beginn

1. Haben beide Parteien bei Vertragsschluss auf ihre eigenen AGB verwiesen?
2. Handelt es sich um B2B oder B2C — nur B2B kommt AGB-Kollision in Betracht?
3. Welche konkreten Klauseln kollidieren (Rechtswahlklausel, Gerichtsstand, Haftungsbeschränkung)?
4. Wie haben die Parteien den Vertrag danach vollzogen — ist ein Vertrag zustande gekommen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 305 BGB — Einbeziehungsvoraussetzungen AGB
- § 305c BGB — überraschende oder unklare Klauseln (keine Einbeziehung)
- § 310 Abs. 1 BGB — B2B: erleichterte Einbeziehung, eingeschränkte Inhaltskontrolle
- Art. 19 CISG — modifizierte Annahme (wesentliche Abweichung = Ablehnung + neues Angebot)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **B2B oder B2C feststellen:** B2C → keine AGB-Kollision; B2B → weiter.
2. **Kollidierende Klauseln identifizieren:** Welche Klauseln widersprechen sich?
3. **Knock-out anwenden (hM Deutschland):** Kollidierende Klauseln streichen, dispositives Recht einfügen.
4. **CISG-Besonderheit:** Art. 19 CISG prüfen — hat eine Partei wesentlich abweichend angenommen?
5. **Ergebnis je Klausel:** Gilt die Klausel, gilt die andere, oder greift dispositives Recht?

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Kollidierende AGB pruefen nach battle-of-forms | Pruefungsergebnis nach Schema; Template unten |
| Variante A — Letzter Schuss der Gegenseite Guillotine-Klausel | Letzte Erklaerung gegnerische AGB massgeblich; Widerspruch sofort |
| Variante B — Keine AGB beider Seiten Individualvertrag | Kein AGB-Kollisions-Problem; Individualvertrag direkt pruefend |
| Variante C — Internationale AGB verschiedene Rechtsordnungen | IPR pruefen; CISG als Aufangrecht beachten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template

**Adressat:** Entscheidungsgründe — Tonfall: sachlich-juristisch

```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Kollidierende AGB

Beide Parteien haben auf ihre jeweiligen AGB verwiesen. Die Parteien haben den Vertrag
gleichwohl vollzogen (Lieferung / Zahlung). Ein Vertrag ist zustande gekommen.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

| Klausel | AGB Kläger | AGB Beklagte | Ergebnis |
|---|---|---|---|
| Rechtswahl | deutsches Recht | Schweizer Recht | Knock-out → IPR (Rom-I) |
| Gerichtsstand | Hamburg | Zürich | Knock-out → § 12 ff. ZPO |
| Haftungsgrenze | 50.000 EUR | unbegrenzt | Knock-out → § 280 BGB |
```

## Geltungsumfang

- B2C: keine AGB-Kollision möglich, da Paragraf 305 II BGB die Einbeziehung in B2C strikt regelt.
- B2B: Paragraf 310 I BGB - Inhaltskontrolle eingeschraenkt, Einbeziehung schon dann möglich, wenn der Verwender klar zu erkennen gibt, dass er nur unter seinen Bedingungen abschließen will. Bei Kollision gilt:

## Lösungstheorien

1. **Last shot doctrine** (Theorie der letzten Stellungnahme): Wer zuletzt seine AGB einbringt und der andere schweigend leistet, dessen AGB gelten. **In Deutschland nicht mehr herrschende Meinung.**
2. **Knock-out / Restgültigkeit** (herrschende Meinung in Deutschland): Soweit die AGB der beiden Seiten kollidieren, fallen die kollidierenden Klauseln raus, der Rest gilt; statt der weggefallenen Klauseln greift dispositives Recht. So entschied der BGH in NJW Jahrgang 1985 auf Seite 1838.
3. **CISG**: Artikel 19 CISG ist umstritten. Herrschende Meinung wendet auch hier Knock-out an, weil ein modifiziertes Angebot mit AGB nicht zwingend Ablehnung darstellt, wenn die Parteien dennoch durchführen.

## Typische Kollisionsfelder

- Rechtswahlklausel (deutsches Recht vs. Schweizer Recht): Kollision => Knock-out, dispositives IPR (Rom-I)
- Gerichtsstand
- Schiedsklausel
- Eigentumsvorbehalt (einfach, verlaengert, erweitert)
- Haftungsbeschraenkungen
- Skonto / Zahlungsfristen

## Bezugnahme im Urteil

Im Tatbestand: Inhalt der streitigen AGB-Klauseln knapp zitieren, Verweis auf die Anlagen mit Bezugnahme nach Paragraf 313 II 2 ZPO.

## 3. `kostenentscheidung-bauen`

**Fokus:** Kostenentscheidung nach §§ 91 ff. ZPO erstellen: Richter muss Kostenquote und -grundentscheidung formulieren. Normen: § 91 ZPO (vollständiges Obsiegen), § 92 ZPO (teilweises Obsiegen), § 100 ZPO (mehrere Beklagte), § 101 ZPO (Streitgenossenschaft/Nebenintervenient), § 93 ZPO (sofortiges Anerkenntnis). Prüfraster: Obsiegens-Quote, Streitwert-Aufteilung, Nebenintervenient, sofortiges Anerkenntnis. Output Kostenentscheidung-Entwurf mit Quote. Abgrenzung: Vollstreckbarkeit siehe vorlaeufige-vollstreckbarkeit; Rechtsmittelbelehrung siehe rechtsmittelbelehrung-zivil.

# Kostenentscheidung

## Triage zu Beginn

1. Wer hat in der Hauptsache gewonnen — vollständig oder teilweise?
2. Bei teilweisem Obsiegen: wie hoch sind die Streitwertanteile beider Parteien?
3. Sind mehrere Beklagte vorhanden — Gesamtschuldner (§ 100 Abs. 4 ZPO) oder anteilig (§ 100 Abs. 1 ZPO)?
4. Liegt sofortiges Anerkenntnis ohne Veranlassung vor (§ 93 ZPO — Kostenfolge für Kläger)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 91 ZPO — vollständige Kostentragung durch Unterliegenden
- § 92 ZPO — Quotelung bei teilweisem Obsiegen
- § 93 ZPO — sofortiges Anerkenntnis (Kosten für Kläger)
- § 100 ZPO — mehrere Beklagte (anteilig oder gesamtschuldnerisch)
- § 101 ZPO — Kosten bei Nebenintervention
- § 3 ZPO — Streitwertschätzung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Obsiegen/Unterliegen feststellen:** Welche Klageanträge wurden zugesprochen, welche abgewiesen?
2. **Streitwertanteile berechnen:** Zugesprochener Betrag / Gesamtstreitwert = Obsiegensquote Kläger.
3. **Regelfall § 91 ZPO:** Voller Sieg → Beklagter trägt alle Kosten.
4. **Teilsieg § 92 ZPO:** Quote berechnen und Kostenverteilung quotalisch.
5. **Sonderfälle prüfen:** § 93 ZPO (sofortiges Anerkenntnis), § 96 ZPO (Vergleich), § 101 ZPO (Nebenintervention).
6. **Formulierung wählen** (s. Beispiele oben).

## Output-Template

**Adressat:** Urteil → Tenor (Ziff. 2) und Entscheidungsgründe — Tonfall: sachlich-juristisch

```
## Kostenentscheidung

**Tenor Ziff. 2:**
"Die Kosten des Rechtsstreits trägt die Beklagte." [Volles Obsiegen]
"Von den Kosten des Rechtsstreits trägt der Kläger [X] von hundert, die Beklagte [Y] von hundert." [Quotelung]

**Begründung in Entscheidungsgründen:**
Die Kostenentscheidung beruht auf § [91 / 92 Abs. 1] ZPO. Der Kläger hat in Höhe von
[BETRAG] EUR obsiegt (zugesprochene Forderung) und ist in Höhe von [BETRAG] EUR unterlegen.
Dies ergibt eine Obsiegensquote von [X] Prozent.
```

## Grundregeln

- Paragraf 91 ZPO - die unterlegene Partei traegt alle Kosten
- Paragraf 92 ZPO - bei teilweisem Obsiegen Quote nach Streitwertverhältnis und Erfolg
- Paragraf 93 ZPO - sofortiges Anerkenntnis ohne Veranlassung - Kläger traegt Kosten
- Paragraf 96 ZPO - Vergleichsspezial
- Paragraf 100 ZPO - mehrere unterlegene Streitgenossen
- Paragraf 101 ZPO - Nebenintervention

## Quotenberechnung

1. Ausgangsstreitwert ermitteln
2. Tatsächliches Obsiegen / Unterliegen jeder Partei beziffern
3. Quoten bilden: Obsiegen Kläger / Streitwert = Verurteilungsquote Beklagter
4. Gegenrechnung: gegenseitige Anteile bei Widerklage / Drittwiderklage

## Formulierung

- "Die Kosten des Rechtsstreits traegt die Beklagte."
- "Von den Kosten des Rechtsstreits tragen der Kläger einhundertacht von hundert und die Beklagte zweiundneunzig von hundert."
- Bei mehreren Beklagten: "Die Kosten des Rechtsstreits tragen die Beklagten als Gesamtschuldner."
- Bei Widerklage: getrennte Quoten für Klage und Widerklage möglich

## Streitwert

Streitwertbeschluss separat oder im Tenor. Pflicht zur Begründung bei Abweichung vom Klagantrag.

<!-- AUDIT 27.05.2026
-->
