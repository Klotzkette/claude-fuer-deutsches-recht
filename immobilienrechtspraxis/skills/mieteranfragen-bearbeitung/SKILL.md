---
name: mieteranfragen-bearbeitung
description: "Mieteranfragen im Miet- und WEG-Recht bearbeiten: Instandsetzung, Betriebskosten, Kündigung. Normen: §§ 535 536 556 573 BGB, WEG. Prüfraster: Anfragetyp, Rechtsgrundlage, Fristen, Handlungspflichten. Output: Bearbeitungsprotokoll Mieteranfrage. Abgrenzung: nicht WEG-Verwaltungsrecht."
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
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Schimmel/Mangel: §§ 536, 536a BGB, § 538 BGB
- Kuendigung/Widerspruch: §§ 543, 573, 574 ff. BGB
- Kaution: § 551 BGB
- Mietpreisbremse: §§ 556d ff. BGB
- Betriebskosten: § 556 Abs. 3 BGB, BetrKV

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.