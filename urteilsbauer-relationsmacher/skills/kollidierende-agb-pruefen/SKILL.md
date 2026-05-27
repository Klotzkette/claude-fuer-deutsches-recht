---
name: kollidierende-agb-pruefen
description: "Kollidierende AGB im B2B-Verkehr (Battle of the Forms) loesen: Kaufvertrag mit beiderseitigen AGB und widerspruechen. Normen: §§ 305-310 BGB (AGB-Recht B2B), CISG Art. 19 (Annahme mit Abweichungen). Pruefraster: Last-Shot-Doctrine, Knock-out-Regel (Restgueltigkeit), Rechtswahlklauseln, Gerichtsstandsklauseln, Schiedsklauseln, Haftungsbeschraenkungen, Eigentumsvorbehalt. Output Loesungs-Memo mit Vertragsinhalt nach Battle of the Forms. Abgrenzung: AGB-Kontrolle allgemein siehe Vertragsrecht-Plugin; CISG spezifisch siehe cisg-pruefen."
---

# Kollidierende AGB

Klassisches Problem im B2B-Geschäft: Beide Parteien verweisen auf ihre eigenen AGB, die widersprechen sich.


## Triage zu Beginn

1. Haben beide Parteien bei Vertragsschluss auf ihre eigenen AGB verwiesen?
2. Handelt es sich um B2B oder B2C — nur B2B kommt AGB-Kollision in Betracht?
3. Welche konkreten Klauseln kollidieren (Rechtswahlklausel, Gerichtsstand, Haftungsbeschränkung)?
4. Wie haben die Parteien den Vertrag danach vollzogen — ist ein Vertrag zustande gekommen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Aktuelle Rechtsprechung

- BGH, Urt. v. 20.01.1983 - VII ZR 105/81, NJW 1985, 1838 — Grundsatzentscheidung zur Knock-out-Doktrin: kollidierende AGB-Klauseln heben sich gegenseitig auf; an ihre Stelle tritt dispositives Gesetzesrecht.
- BGH, Urt. v. 09.01.2002 - VIII ZR 304/00, NJW 2002, 1651 — Bestätigungsschreiben: enthalten AGB erst im Bestätigungsschreiben, ohne ausdrücklichen Widerspruch des Empfängers, gelten diese AGB wenn branchenüblich.
- BGH, Urt. v. 01.03.2017 - VIII ZR 134/15, NJW 2017, 2202 — Eigentumsvorbehalt: einfacher Eigentumsvorbehalt des Verkäufers geht verlängertem Eigentumsvorbehalt des Käufers vor, wenn Käufer AGB zuletzt übergeben hat — Knock-out gilt nicht bei Eigentumsvorbehalts-Kollision.
- BGH, Urt. v. 07.06.1978 - VIII ZR 84/77, NJW 1978, 1858 — Wer zuletzt AGB übermittelt und der andere schweigend leistet, dessen AGB gelten nur im Schweige-Einverständnis-Fall; ohne dieses gilt Knock-out.

## Zentrale Normen

- § 305 BGB — Einbeziehungsvoraussetzungen AGB
- § 305c BGB — überraschende oder unklare Klauseln (keine Einbeziehung)
- § 310 Abs. 1 BGB — B2B: erleichterte Einbeziehung, eingeschränkte Inhaltskontrolle
- Art. 19 CISG — modifizierte Annahme (wesentliche Abweichung = Ablehnung + neues Angebot)

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, § 305 Rn. 50-70 (kollidierende AGB, Knock-out)
- MüKo-BGB/Basedow, 9. Aufl. 2022, § 305 Rn. 80-100 (Einbeziehung und Kollision)
- Schlechtriem/Schwenzer, CISG, 7. Aufl. 2019, Art. 19 Rn. 1-20 (battle of forms CISG)

## Schritt-für-Schritt-Workflow


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

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

Nach der Knock-out-Doktrin (BGH NJW 1985, 1838) heben sich kollidierende Klauseln auf:

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
