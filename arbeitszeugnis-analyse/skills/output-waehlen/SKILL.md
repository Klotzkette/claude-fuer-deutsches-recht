---
name: output-waehlen
description: "Output-Wahl für Arbeitszeugnis-Analyse: stimmt Adressat (Mandant/Arbeitnehmer, Arbeitgeber/HR, Vorgesetzte), Frist (BAG 5.7.2018 – 9 AZR 244/17 Anspruch entstehung) und Form auf den Zweck ab — typische Outputs: Notenmatrix, Geheimcode-Befund, Berichtigungsklage."
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Arbeitszeugnis Analyse** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `ampelsystem-tabellenausgabe` — Ampelsystem Tabellenausgabe
- `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste` — Arbeitszeugnis Ampelsystem Dokumentenmatrix Lueckenliste
- `arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk` — Arbeitszeugnis Codeworte Compliance Dokumentation Aktenvermerk
- `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen` — Arbeitszeugnis Deutscher Tatbestandsmerkmale Beweisfragen
- `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine` — Arbeitszeugnis Geheimcodes Schriftsatz Brief Memo Bausteine
- `arbeitszeugnis-gruen-behoerden-gerichts-registerweg` — Arbeitszeugnis Gruen Behoerden Gerichts Registerweg
- `arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung` — Arbeitszeugnis Negative Zahlen Schwellenwerte Berechnung
- `arbeitszeugnis-orange-risikoampel-gegenargumente` — Arbeitszeugnis Orange Risikoampel Gegenargumente
- `arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation` — Arbeitszeugnis Schaufenster Verhandlung Vergleich Eskalation
- `arbeitszeugnis-zeugnisanalyse-wortlaut-codes` — Arbeitszeugnis Zeugnisanalyse Wortlaut Codes
- `aufforderungsschreiben-arbeitgeber` — Aufforderungsschreiben Arbeitgeber
- `azubi-zeugnis-analyse` — Azubi Zeugnis Analyse
- `bereichs-drift-detektor` — Bereichs Drift Detektor
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Arbeitszeugnis Analyse (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.


## Leitentscheidungs-Anker (vollstaendige BAG-Linie)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast für bessere Note beim Arbeitnehmer, für schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast für bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 20.02.2001 - 9 AZR 44/00** | Beginn der staendigen Linie: kein Anspruch auf Schlussformel mit Dank und guten Wuenschen; Fehlen kein unzulaessiges Geheimzeichen. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 11.12.2012 - 9 AZR 227/11** | Kein Anspruch auf Dank/Wuensche; bei unzufriedener Mandantschaft mit erteilter Schlussformel ist nur ein Zeugnis OHNE Schlussformel einklagbar - keine Umformulierung. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 25.01.2022 - 9 AZR 146/21** | Bestaetigung der Linie; Abwaegung mit Meinungsfreiheit des Arbeitgebers (Art. 5 I GG). | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 06.06.2023 - 9 AZR 272/22** | Massregelungsverbot $ 612a BGB: eine einmal erteilte Dankes-/Wunschformel darf nicht in spaeterer Fassung gestrichen werden, nur weil der Arbeitnehmer berechtigte Änderungswuensche geltend gemacht hat. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 21.06.2005 - 9 AZR 352/04** | Gebot der Zeugnisklarheit ($ 109 II GewO): massgeblich ist der objektive Empfaengerhorizont, nicht die Absicht des Arbeitgebers. "Kennen gelernt" allein ist kein Geheimcode. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 15.11.2011 - 9 AZR 386/10** | Bestaetigung: "kennen gelernt" ist allein und losgeloest vom uebrigen Zeugnisinhalt kein unzulaessiger Geheimcode; Werturteile-Spielraum mit Grenze Zeugniswahrheit/-klarheit. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 21.09.1999 - 9 AZR 893/98** | Aeussere Form: zweimaliges Falten zulässig, wenn Original kopierfaehig bleibt und Knicke nicht durchschlagen. Wer mit Maschinenname unterzeichnet, muss eigenhaendig unterschreiben. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 27.04.2021 - 9 AZR 262/20** | Tabellarische Ankreuz-/Schulnotenformulare erfuellen $ 109 GewO regelmaessig nicht - individuelle Hervorhebung verlangt Fliesstext. | bundesarbeitsgericht.de / dejure.org |
| **LAG Hamm, Beschl. v. 14.11.2016 - 12 Ta 475/16** | Ironisch ueberzogenes Lob ist unzulaessig; Arbeitnehmer hat Anspruch auf geschaeftsuebliche Unterschrift des Ausstellers; quer-laufende Unterschrift weckt Zweifel an Ernsthaftigkeit. | nrwe.de / justiz.nrw.de |
| **ArbG Kiel, Urt. v. 18.04.2013 - 5 Ca 80 b/13** | In die Unterschrift eingearbeiteter Smiley mit herabgezogenen Mundwinkeln ist ein unzulaessiges Geheimzeichen ($ 109 II 2 GewO). | frei publiziert / dejure-Suche |
| **BAG, Beschl. v. 07.05.2026 - 8 AZB 25/25** | Im gerichtlichen Vergleich uebernommene Pflicht, Zeugnis nach dem ENTWURF des Arbeitnehmers zu erteilen mit Abweichungs-Vorbehalt aus wichtigem Grund, hat vollstreckungsfaehigen Inhalt. | bundesarbeitsgericht.de / dejure.org (vor Schriftsatzverwendung live verifizieren - Entscheidung aus 2026) |
| **BAG, Urt. v. 08.03.1995 - 5 AZR 848/93** | Zeugniserteilung ist Holschuld ($ 269 BGB): Arbeitnehmer holt im Betrieb ab; nur ausnahmsweise (Unzumutbarkeit, $ 242 BGB) Schickschuld. | bundesarbeitsgericht.de / dejure.org |


## HR-Gegenpruefung (Arbeitgeberseite)

Wenn ein **Entwurf** vor Erteilung geprueft werden soll (HR, Geschäftsführung, Kanzlei auf Arbeitgeberseite):

```
1. Einschaetzungsmatrix wie ueblich - aber mit Blickrichtung: Welche
   Formulierung liest ein kundiger Empfaenger schlechter als gemeint?
2. Unbeabsichtigte Codes markieren und neutral umformulieren.
3. Klarheits-Check nach $ 109 II GewO und BAG 9 AZR 352/04 / 386/10:
   keine mehrdeutigen, ironischen oder ueberzogenen Formulierungen
   (LAG Hamm 12 Ta 475/16).
4. Formalia-Check: Fliesstext (BAG 9 AZR 262/20 verbietet Ankreuzschemata),
   Unterschrift durch genannte Person (BAG 9 AZR 893/98), keine
   elektronische Form ($ 109 III GewO).
5. Konsistenz: Hauptformel, Einzelsaetze, Schlussformel auf derselben
   Notenstufe? Drift vermeiden, bevor sie entsteht.
```

Ziel: ein Zeugnis, das wohlwollend, wahr und unangreifbar ist - was heute sauber formuliert ist, muss morgen nicht berichtigt werden.
