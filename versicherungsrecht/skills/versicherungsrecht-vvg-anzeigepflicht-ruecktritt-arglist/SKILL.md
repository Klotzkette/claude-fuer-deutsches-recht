---
name: versicherungsrecht-vvg-anzeigepflicht-ruecktritt-arglist
description: "VVG Anzeigepflicht Ruecktritt Arglist: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# VVG Anzeigepflicht Ruecktritt Arglist

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **VVG Anzeigepflicht Ruecktritt Arglist** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vvg-anzeigepflicht-19-ruecktritt-kuendigung-anpassung` | § 19 VVG in Leben, BU, PKV und Unfallversicherung: Gesundheitsfragen, Kenntnis, Kausalität, Rücktritt, Kündigung, Vertragsanpassung, Arglist und Belehrungsfehler prüfen. |
| `vvg-arglist-taeuschung-anfechtung` | Arglistanfechtung nach § 22 VVG/BGB § 123: Gesundheitsangaben, Schadenhergang, Vorschäden, subjektives Element, Indizien und Gegenbeweis. |
| `vvg-falligkeit-14-abschlagszahlung` | Fälligkeit des Versicherungsanspruchs, Ermittlungsdauer, Abschlagszahlung, Verzug und taktische Beschleunigung bei großen Schäden. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **VVG Anzeigepflicht Ruecktritt Arglist**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vvg-anzeigepflicht-19-ruecktritt-kuendigung-anpassung`

**Fokus:** § 19 VVG in Leben, BU, PKV und Unfallversicherung: Gesundheitsfragen, Kenntnis, Kausalität, Rücktritt, Kündigung, Vertragsanpassung, Arglist und Belehrungsfehler prüfen.

# Vorvertragliche Anzeigepflicht § 19 VVG

## Einsatz

Dieser Skill ist für Fälle, in denen der Versicherer nachträglich Gesundheitsfragen, Vorversicherungen oder Gefahrumstände aufgreift.

## Norm- und Quellenanker

VVG §§ 19–22, 194; BGB § 123; AVB; DSGVO/Gesundheitsdaten; ZPO Beweislast.

## Arbeitsfragen

1. Welche Frage wurde gestellt, war sie in Textform und verständlich?
2. Welche Tatsache wurde objektiv falsch oder unvollständig beantwortet?
3. Welche Kenntnis hatte der Antragsteller bei Antragstellung?
4. Welche Belehrung lag vor und war sie drucktechnisch/inhaltlich ausreichend?
5. Welche Rechtsfolge passt: Rücktritt, Kündigung, Anpassung oder Anfechtung?

## Output

§-19-Prüfvermerk, Angriffspunkte zur Belehrung, Kausalitätsmatrix und Entwurf einer Erwiderung.

## Red Flags

- Versicherer springt sofort zu Arglist
- Gesundheitsfrage zu weit oder mehrdeutig
- Maklernotiz widerspricht Antrag
- Kausalität zwischen Anzeigeverstoß und Schaden unklar

## Anschluss-Skills

- vvg-arglist-taeuschung-anfechtung
- bu-berufsbild-50-prozent-substantiierung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `vvg-arglist-taeuschung-anfechtung`

**Fokus:** Arglistanfechtung nach § 22 VVG/BGB § 123: Gesundheitsangaben, Schadenhergang, Vorschäden, subjektives Element, Indizien und Gegenbeweis.

# Arglistanfechtung des Versicherers

## Einsatz

Der Skill ist für die härteste Ablehnungslinie des Versicherers: Arglist. Er trennt Irrtum, Erinnerungslücke, Maklerfehler und bewusste Täuschung.

## Norm- und Quellenanker

VVG § 22; BGB § 123; ZPO; DSGVO Gesundheitsdaten; AVB.

## Arbeitsfragen

1. Welche konkrete Täuschungshandlung wird behauptet?
2. Welche Indizien sprechen für Vorsatz, welche dagegen?
3. Welche Rolle spielten Makler, Arztunterlagen, Antragsfragen und Sprache?
4. Ist die Anfechtung fristgerecht und richtig erklärt?

## Output

Arglist-Indizientabelle, Gegenbeweisstrategie, Mandantenbefragung und Schriftsatzkern.

## Red Flags

- Arglist nur aus objektiver Falschangabe abgeleitet
- Antragsfrage unklar
- Makler hat Angaben zusammengefasst
- Versicherer ignoriert entlastende Arztunterlagen

## Anschluss-Skills

- vvg-anzeigepflicht-19-ruecktritt-kuendigung-anpassung
- datenschutz-schweigepflicht-gesundheitsdaten

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `vvg-falligkeit-14-abschlagszahlung`

**Fokus:** Fälligkeit des Versicherungsanspruchs, Ermittlungsdauer, Abschlagszahlung, Verzug und taktische Beschleunigung bei großen Schäden.

# Fälligkeit und Abschlagszahlung § 14 VVG

## Einsatz

Der Skill hilft, wenn der Versicherer immer weiter prüft und der Mandant Liquidität braucht.

## Norm- und Quellenanker

VVG § 14; BGB §§ 286, 288; ZPO; AVB; Sachverständigenverfahren.

## Arbeitsfragen

1. Welche Erhebungen sind objektiv noch notwendig?
2. Welche unstreitigen Mindestbeträge sind abschlagsfähig?
3. Welche Nachweise kann der Versicherungsnehmer sofort liefern?
4. Ab wann entsteht Verzug oder Klagedruck?

## Output

Zahlungsfahrplan, Abschlagsforderung, Verzugsschreiben und Klage-/Eilvermerk.

## Red Flags

- endlose Prüfung ohne konkreten Fragenkatalog
- Gutachten liegt vor, Zahlung bleibt aus
- Versicherer koppelt Zahlung an überzogene Generalvollmacht
- Liquiditätsnot im Betrieb

## Anschluss-Skills

- sachverstaendigenverfahren-versicherung
- betriebsunterbrechung-sachschaden-trigger

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
