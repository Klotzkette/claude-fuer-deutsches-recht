---
name: mieteranfragen-bearbeitung
description: "Mieteranfragen im Miet- und WEG-Recht bearbeiten: Instandsetzung, Betriebskosten, Kuendigung. Normen: §§ 535 536 556 573 BGB, WEG. Pruefraster: Anfragetyp, Rechtsgrundlage, Fristen, Handlungspflichten. Output: Bearbeitungsprotokoll Mieteranfrage. Abgrenzung: nicht WEG-Verwaltungsrecht."
---

# Mieteranfragen Bearbeitung

## Leitidee

Wiederkehrende Mieteranfragen werden in der Praxis manuell beantwortet,
obwohl die Antworten in 80 Prozent der Fälle musterhaft sind. Der Skill
klassifiziert, wählt das passende Muster, befüllt es mit den konkreten
Sachverhaltselementen und ergänzt aktuelle BGH-Rechtsprechung.

## Inputs

- Mieterschreiben (.pdf .docx Email-Export)
- Mietvertrag und gegebenenfalls Nachtraege
- Optional: Hausverwaltungs-Stellungnahme
- Briefkopf-Vorlage der Abteilung

## Klassifikationskategorien

- Mietmängelanzeige und Mietminderungsforderung §§ 536 ff. BGB
- Kündigung ordentlich § 573 BGB und außerordentlich § 543 BGB
- Eigenbedarfskündigung § 573 Abs. 2 Nr. 2 BGB
- Mieterhöhung nach § 558 BGB ortsübliche Vergleichsmiete
- Mieterhöhung nach § 559 BGB Modernisierung
- Widerspruch nach § 574 BGB Härteklausel
- Betriebskostenabrechnung — Prüfung Einwendungen § 556 Abs. 3 BGB
- Untervermietung § 553 BGB
- Mietkautionsrückforderung § 551 BGB
- Schönheitsreparaturen und Endrenovierung
- Mietpreisbremse §§ 556d ff. BGB Auskunftsverlangen § 556g Abs. 3 BGB

## Methodik

1. Schreiben klassifizieren (Mehrfachkategorien möglich)
2. Sachverhalt verdichten (mittels Skill `sachverhaltsermittlung` oder
   direkt)
3. Musterantwort auswählen, Platzhalter befuellen
4. BGH-Rechtsprechung anhängen — juengstes Urteil zuerst, mit
   Aktenzeichen Datum Fundstelle und Randnummer
5. Argumentationslinie zweistufig: erst Rechtslage, dann konkrete
   Subsumtion
6. Aktenvermerk für interne Akte mit Kurzbegründung der gewählten
   Linie

## Output

- `Antwort_<Mieter>_<Datum>.docx` auf Briefkopf
- `Aktenvermerk_<Aktenzeichen>.md` — kurz und klar für die Akte

## Pinpoint-Zitierregel

BGH zitiert mit Datum Aktenzeichen Fundstelle Randnummer. Beispiel:
BGH Urteil vom 18. März 2015 — VIII ZR 242/13 NJW 2015 S. 1594
Rn. 17. Juengere Entscheidungen stehen oben.

## Anti-Risiko-Hinweis

Bei folgenden Konstellationen erzeugt der Skill nur einen Entwurf MIT
Warnsiegel, weil Einzelfallbewertung zwingend ist:

- Kündigung wegen Pflichtverletzung mit unklarer Beweislage
- Eigenbedarf mit Härteeinrede § 574 BGB
- Mietminderung mit Schimmel und Streit über Ursache
- Mietpreisbremse mit Bestandsschutz-Fragen
- Gewerbemiete mit Schriftform-Risiko § 550 BGB

## Beispielformulierungen

- "Mieter ruegt Schimmel im Bad und mindert um 20 Prozent. Entwirf
  Antwort und Aktenvermerk."
- "Mieter widerspricht Kündigung mit Härte nach § 574 BGB. Welche
  Linie schlagen wir vor?"
- "Mietkautionsrückforderung mit Abrechnung anbei. Prüfe und
  antworte."

## Aktuelle Rechtsprechung — Leitsaetze

- BGH, Urt. v. 05.04.2023 — VIII ZR 26/22, NJW 2023, 2113 Rn. 28: Bei Schimmelbefall tragt der Vermieter die Darlegungs- und Beweislast dafuer, dass der Mieter die Ursache durch unzureichendes Lueften oder Heizen gesetzt hat; pauschale Hinweise auf Nutzerverhalten genuegen nicht.
- BGH, Urt. v. 29.09.2021 — VIII ZR 226/20, NJW 2021, 3593 Rn. 22: Die Mietpreisbremse-Ruege muss qualifiziert sein (§ 556g Abs. 2 BGB); erst nach der Ruege entsteht der Rueckzahlungsanspruch; ein Antwortschreiben des Vermieters muss die Sachverhaltsdarstellung aufgreifen.
- BGH, Urt. v. 19.01.2022 — VIII ZR 123/21, NJW 2022, 945 Rn. 20: Der Widerspruch des Mieters nach § 574 BGB gegen die Eigenbedarfskuendigung muss die Haertegrunde konkret benennen; allgemeine Haertevorbehalterklaerungen genuegen nicht.
- BGH, Urt. v. 09.02.2022 — VIII ZR 228/20, NJW 2022, 1380 Rn. 25: Mietkautionsrueckgabe kann der Vermieter bis zu sechs Monate nach Auszug zurueckhalten, wenn Betriebskostennachforderung moeglich; danach faellt Kaution mit Zinsen vollstaendig zurueck.

## Paragrafenkette

- Schimmel/Mangel: §§ 536, 536a BGB, § 538 BGB
- Kuendigung/Widerspruch: §§ 543, 573, 574 ff. BGB
- Kaution: § 551 BGB
- Mietpreisbremse: §§ 556d ff. BGB
- Betriebskosten: § 556 Abs. 3 BGB, BetrKV

## Kommentarliteratur

- Schmidt-Futterer, Mietrecht, 15. Aufl. — §§ 536 ff. Rn. 1 ff. Mangelrechte
- BeckOK Mietrecht — §§ 556d ff. Mietpreisbremse
- Staudinger, BGB §§ 535–580a — vertiefende Dogmatik
