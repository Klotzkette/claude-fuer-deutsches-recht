---
name: mieteranfragen-bearbeitung
description: Bearbeitet eingehende mietrechtliche Anfragen — Mietmaengelanzeigen Kuendigungen Mieterhoehungsverlangen Widersprueche nach § 574 BGB Betriebskosten-Einwendungen Untervermietungsanfragen — und erstellt fundierte Antwortschreiben mit BGH-Verankerung. Jede Anfrage wird klassifiziert dem passenden Antwortmuster zugeordnet und mit Pinpoint-Zitierung versehen (juengere Rechtsprechung zuerst Randnummer angefuegt). Output ist .docx auf Kanzlei- oder Abteilungsbriefkopf mit zweiter Datei Aktenvermerk. Geeignet fuer Wohnraum und Gewerberaum. Bei nicht-standardisierbaren Konstellationen weist der Skill auf manuelle Pruefung hin.
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
