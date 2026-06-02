---
name: legw-ressort-router
description: "Ressort-Router der Legistik-Werkstatt: leitet nach Auftragsaufnahme in das richtige Bundes-Ressort. Klaert Ressort-Kuerzel BMF; BMI; AA; BMVg; BMWE; BMFTR; BMJV; BMBFSFJ; BMAS; BMDS; BMV; BMUKN; BMG; BMLEH; BMZ und BMWSB. Pro Ressort: Heranfuehrung; Ressortaufgaben; fuenf Spezialfelder. Output: gewaehltes Ressort plus Skill-Empfehlungskette. Abgrenzung: legistik-auftragsaufnahme (vorher); normhierarchie-routing (Normwahl); normenkartierung (Bestandskartierung)."
---

# Legistik-Werkstatt - Ressort-Router

> Zweiter Skill nach legistik-auftragsaufnahme. Leitet auf den fachlich richtigen Ressort-Kompass.

## Wozu

Legistinnen und Legisten kommen oft aus den Politikwissenschaften, dem oeffentlichen Recht oder aus
Verwaltungslaufbahnen - das Ressort und seine Materie sind dabei zunaechst nicht ihr Heimspielfeld.
Dieser Skill macht den Sprung vom abstrakten Vorhaben zur ressortspezifischen Arbeitsumgebung:
**welches Ministerium - welche Materie - welche Skills.**

## Ressort-Matrix Bundesregierung Kabinett Merz Stand 2026

| Kuerzel | Ressort | Schwerpunkt |
|---|---|---|
| BMF | Finanzen | Steuern; Haushalt; Finanzmarkt; Zoll; Geldwaesche |
| BMI | Innern | Sicherheit; Migration; Verwaltung; Bevoelkerungsschutz; oeffentlicher Dienst |
| AA | Auswaertiges Amt | Voelkerrecht; Konsular; Aussenwirtschaft; EU-Verfahren; Sanktionen |
| BMVg | Verteidigung | Wehrrecht; Beschaffung; NATO; Wehrtechnik; Reserve |
| BMWE | Wirtschaft und Energie | Energie und Netze; Erneuerbare; Industrie; Kartellrecht |
| BMFTR | Forschung; Technologie; Raumfahrt | Hochschule; Raumfahrt; Forschungsfoerderung; KI; Biotech |
| BMJV | Justiz und Verbraucherschutz | BGB; StGB; Prozessrecht; Verbraucherschutz; Rechtsstaat |
| BMBFSFJ | Bildung; Familie; Senioren; Frauen; Jugend | Schule; Jugendhilfe; Familie; Gleichstellung; Senioren |
| BMAS | Arbeit und Soziales | Arbeitsrecht; SGB; Rente; Arbeitsschutz; Teilhabe |
| BMDS | Digitales und Staatsmodernisierung | OZG; IT-Sicherheit; Datenrecht; Register; KI-VO |
| BMV | Verkehr | Strasse; Schiene; Luft; Wasser; Fuehrerschein |
| BMUKN | Umwelt; Klimaschutz; Naturschutz; nukleare Sicherheit | BImSchG; Wasser; Abfall; Naturschutz; Nukleares |
| BMG | Gesundheit | Arzneimittel; SGB V; IfSG; Heilberufe; Krankenhaus |
| BMLEH | Landwirtschaft; Ernaehrung; Heimat | Agrar; Tierschutz; Lebensmittel; Forst; Oekolandbau |
| BMZ | Wirtschaftliche Zusammenarbeit und Entwicklung | Bilaterale Abkommen; humanitaere Hilfe; Klimafinanzierung |
| BMWSB | Wohnen; Stadtentwicklung; Bauwesen | BauGB; Mietrecht; Stadtentwicklung; Bauprodukte; GEG |

## Vorgehen

### Schritt 1 - Ressort waehlen

Der Auftrag wurde in `legistik-auftragsaufnahme` aufgenommen. Frage:

> Welches Bundesressort fuehrt federfuehrend (BMF; BMI; AA; BMVg; BMWE; BMFTR; BMJV; BMBFSFJ;
> BMAS; BMDS; BMV; BMUKN; BMG; BMLEH; BMZ; BMWSB)?

Bei Mitzeichnung oder ressortuebergreifenden Vorhaben: federfuehrendes Ressort + alle Mitzeichner
festhalten. Federfuehrung steuert HdR-Vorlage; Mitzeichner steuern Inhalte.

### Schritt 2 - Heranfuehrungs-Skill rufen

Jedes Ressort hat einen Heranfuehrungs-Skill `legw-ressort-<kuerzel>`. Beispiel:
- Federfuehrer BMUKN -> `legw-ressort-bmukn` (Atomrecht; Immissionsschutz; Wasser; Abfall; Naturschutz)
- Federfuehrer BMLEH -> `legw-ressort-bmleh` (Agrar; Tierschutz; Lebensmittel; Forst; Oekolandbau)

Diese Skills erklaeren in kurzer Form **Materie; Akteure; Normbestand; typische Stolpersteine**.

### Schritt 3 - Ressortaufgaben-Skill rufen

Pro Ressort gibt es `legw-ressortaufgaben-<kuerzel>`. Er bricht die typische Legistik-Aufgabe
auf das Ressort herunter: welche Begruendungsteile; welche Verbaende; welche Befassung im
Bundestag; welche Ausschuesse; welche Aufsicht; welche Fristen.

### Schritt 4 - Spezialfeld-Skill rufen

Jedes Ressort hat fuenf Spezialfeld-Skills `legw-<kuerzel>-<thema>`. Beispiel BMLEH:
- `legw-bmleh-agrar-und-foerderungsrecht-gak-gap`
- `legw-bmleh-tierschutz-und-tiergesundheitsrecht`
- `legw-bmleh-lebensmittelrecht-und-futtermittelrecht`
- `legw-bmleh-forst-und-jagdrecht`
- `legw-bmleh-oekolandbau-und-pflanzenschutzrecht`

Diese decken sachliche Detailfragen ab und sind das Brett, auf dem der Politikwissenschaftler steht,
wenn er an eine fremde Materie heran muss.

### Schritt 5 - Optional RuleMapping-Anschluss

Wenn das Vorhaben digital-tauglich werden soll (BMJ-Initiative; SPRIND-Foerderung; Rulemap-Builder):
weiter zu `legw-rmap-einstieg-und-eignung`. Von dort 9 RuleMapping-Skills.

## Output

Ein Routing-Block fuer das Auftragsblatt:

```
Ressort federfuehrend: <kuerzel> - <Volltitel>
Mitzeichnende Ressorts: <Liste>
Empfohlene Skill-Kette:
  1. legw-ressort-<kuerzel>            (Heranfuehrung)
  2. legw-ressortaufgaben-<kuerzel>    (Ressortaufgaben)
  3. legw-<kuerzel>-<thema>            (Spezialfeld)
  4. normhierarchie-routing            (Normwahl)
  5. <weitere Spezial- und Werkstattskills>
Optional RuleMapping-Anschluss: legw-rmap-einstieg-und-eignung
```

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
