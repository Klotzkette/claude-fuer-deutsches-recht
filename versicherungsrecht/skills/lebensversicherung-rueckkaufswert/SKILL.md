---
name: lebensversicherung-rueckkaufswert
description: "Lebensversicherung Rueckkaufswert: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lebensversicherung Rueckkaufswert

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lebensversicherung Rueckkaufswert** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch` | Rückkaufswert, Abschlusskosten, Kündigung, Beitragsfreistellung und Altvertrags-Widerspruch in Lebens- und Rentenversicherung prüfen. |
| `lebensversicherung-ueberschussbeteiligung-bewertungsreserven` | Überschussbeteiligung, Schlussüberschuss, Bewertungsreserven und Informationsrechte in Lebensversicherung und Rentenversicherung verständlich prüfen. |
| `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt` | Nachhaltigkeits- und ESG-Angaben bei Versicherungsanlageprodukten: Taxonomie, SFDR, Greenwashing, Produktfreigabe und Vertrieb. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Lebensversicherung Rueckkaufswert**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch`

**Fokus:** Rückkaufswert, Abschlusskosten, Kündigung, Beitragsfreistellung und Altvertrags-Widerspruch in Lebens- und Rentenversicherung prüfen.

# Lebensversicherung: Rückkaufswert, Abschlusskosten, Widerspruch

## Einsatz

Der Skill ist für Mandate, in denen Kunden alte Lebensversicherungen kündigten oder widersprechen wollen.

## Norm- und Quellenanker

VVG §§ 150 ff., 169; VVG a.F. bei Altverträgen live prüfen; BGB; BGH-Rechtsprechung nur verifiziert verwenden.

## Arbeitsfragen

1. Welche Vertragsgeneration und Belehrung gilt?
2. Wie wurde der Rückkaufswert berechnet?
3. Sind Abschlusskosten/Zillmerung transparent?
4. Ist Widerspruch, Kündigung oder Vergleich wirtschaftlich besser?

## Output

Rückkaufswert-Check, Belehrungsprüfung, Anspruchsberechnung und Mandantenentscheidung.

## Red Flags

- Altvertrag ohne vollständige Unterlagen
- Widerspruch wirtschaftlich überschätzt
- Steuerfolgen vergessen
- Vergleich ohne Berechnung

## Anschluss-Skills

- lebensversicherung-bezugsrecht-widerruf-aenderung
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `lebensversicherung-ueberschussbeteiligung-bewertungsreserven`

**Fokus:** Überschussbeteiligung, Schlussüberschuss, Bewertungsreserven und Informationsrechte in Lebensversicherung und Rentenversicherung verständlich prüfen.

# Überschussbeteiligung und Bewertungsreserven

## Einsatz

Der Skill übersetzt versicherungsmathematische Schreiben in rechtlich prüfbare Fragen.

## Norm- und Quellenanker

VVG §§ 153 ff., 169; VAG; Informationspflichten; BaFin-Hinweise live prüfen.

## Arbeitsfragen

1. Welche Überschusskomponenten sind zugesagt, deklariert oder nur erwartet?
2. Wie wird Beteiligung an Bewertungsreserven erklärt?
3. Welche Änderung beruht auf Zinsumfeld, Kollektiv oder Kosten?
4. Welche Auskunft kann verlangt werden?

## Output

Transparenzmemo, Auskunftsschreiben und Plausibilitätscheck.

## Red Flags

- Schlussüberschuss als garantiert verstanden
- Bewertungsreserven nicht nachvollziehbar
- Tarifgeneration verwechselt
- BaFin-Aufsicht mit Individualanspruch verwechselt

## Anschluss-Skills

- vag-bafin-aufsicht-beschwerde-missstand
- solvency-ii-scr-orsa-aufsichtsrecht

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt`

**Fokus:** Nachhaltigkeits- und ESG-Angaben bei Versicherungsanlageprodukten: Taxonomie, SFDR, Greenwashing, Produktfreigabe und Vertrieb.

# Nachhaltigkeit bei Versicherungsprodukten

## Einsatz

Für Lebens-/Rentenversicherungsprodukte mit Fonds/ESG-Versprechen und Vertriebsunterlagen.

## Norm- und Quellenanker

SFDR; Taxonomie-VO; IDD; VAG/VVG Informationspflichten; UWG; BaFin-Verlautbarungen live prüfen.

## Arbeitsfragen

1. Welche Nachhaltigkeitsaussage wird gemacht?
2. Ist das Produkt Versicherungsanlageprodukt?
3. Welche Offenlegungspflichten treffen Hersteller und Vertrieb?
4. Besteht Greenwashing- oder Haftungsrisiko?

## Output

ESG-Disclosure-Check, Vertriebsfreigabe, Risikomemo und Korrekturvorschläge.

## Red Flags

- Marketingversprechen stärker als Anlagepolitik
- SFDR-Kategorie falsch verstanden
- Taxonomiequote nicht belegbar
- Beratung dokumentiert ESG-Wunsch nicht

## Anschluss-Skills

- idd-vertrieb-beratung-dokumentation
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
