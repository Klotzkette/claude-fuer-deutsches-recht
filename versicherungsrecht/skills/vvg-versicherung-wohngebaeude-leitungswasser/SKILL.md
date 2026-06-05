---
name: vvg-versicherung-wohngebaeude-leitungswasser
description: "VVG Versicherung Wohngebaeude Leitungswasser: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# VVG Versicherung Wohngebaeude Leitungswasser

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **VVG Versicherung Wohngebaeude Leitungswasser** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vvg-versicherung-fuer-fremde-43-48` | Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sicherungsnehmer, Leasinggeber, Mieter, Subunternehmer und Konzernunternehmen? |
| `wohngebaeude-leitungswasser-sturm-hagel-brand` | Wohngebäudeversicherung: Leitungswasser, Sturm/Hagel, Brand, Elementarschaden, grobe Fahrlässigkeit, Obliegenheiten und Sanierungskosten. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **VVG Versicherung Wohngebaeude Leitungswasser**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vvg-versicherung-fuer-fremde-43-48`

**Fokus:** Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sicherungsnehmer, Leasinggeber, Mieter, Subunternehmer und Konzernunternehmen?

# Versicherung für fremde Rechnung §§ 43–48 VVG

## Einsatz

Dieser Skill klärt Dreiecksverhältnisse, in denen Versicherungsnehmer und wirtschaftlich Betroffener auseinanderfallen.

## Norm- und Quellenanker

VVG §§ 43–48, 44, 45; BGB Abtretung/Einziehung; ZPO Prozessführungsbefugnis.

## Arbeitsfragen

1. Wer ist Versicherungsnehmer, versicherte Person, Bezugsberechtigter, Sicherungsnehmer?
2. Wer besitzt Police und kann Zahlung verlangen?
3. Welche Einwendungen gegen wen sind möglich?
4. Ist gewillkürte Prozessstandschaft oder Abtretung nötig?

## Output

Beteiligtenmatrix, Anspruchsinhaber-Prüfung, Prozessführungsnotiz und Zahlungsempfänger-Check.

## Red Flags

- Leasingobjekt beschädigt
- Bank als Sicherungsnehmer
- Konzernpolice mit Tochtergesellschaft
- versicherte Person will direkt klagen

## Anschluss-Skills

- transportversicherung-ware-lagerung
- direktanspruch-pflichtversicherung-115-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `wohngebaeude-leitungswasser-sturm-hagel-brand`

**Fokus:** Wohngebäudeversicherung: Leitungswasser, Sturm/Hagel, Brand, Elementarschaden, grobe Fahrlässigkeit, Obliegenheiten und Sanierungskosten.

# Wohngebäudeversicherung: Leitungswasser, Sturm, Brand

## Einsatz

Der Skill führt durch typische Gebäudeschäden mit Gutachten, Handwerkerangeboten und Streit um Ursache oder Höhe.

## Norm- und Quellenanker

VVG §§ 1, 28, 81, 82; BGB; VGB/AVB; Sachverständigenverfahren.

## Arbeitsfragen

1. Welche Gefahr ist versichert und welche ausgeschlossen?
2. Was ist Ursache, Folgeschaden, Sanierung und Sowieso-Kosten?
3. Wurde Schadenminderung erfüllt?
4. Ist grobe Fahrlässigkeit quotenrelevant?

## Output

Deckungsmemo, Schadenpositionsliste, Gutachterfragen und Zahlungsaufforderung.

## Red Flags

- Leitungswasser vs. Grundwasser verwechselt
- Sanierung vor Besichtigung ohne Fotobeweise
- Schimmel als Folgeschaden unklar
- Neuwertspitze nicht beachtet

## Anschluss-Skills

- sachverstaendigenverfahren-versicherung
- elementarschaden-starkregen-ueberschwemmung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
