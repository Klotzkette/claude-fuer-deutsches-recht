---
name: ziel-und-rechtsweg-bestimmung
description: "Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG. Warnt bei Zweifelsfaellen."
---

# Ziel- und Rechtsweg-Bestimmung

## Triage zu Beginn — kläre vor der Rechtsweg-Bestimmung

1. Was möchte der Nutzer erreichen? (Zahlung / Unterlassung / Anfechtung VA / Strafanzeige / ...)
2. Wer ist Gegner? (Privatperson / Unternehmen / Behörde / Staat)
3. Ist Behördenbeteiligung erkennbar? → Öffentliches Recht prüfen
4. Besteht Dringlichkeit? → Eilverfahren parallel skizzieren
5. Wurde ein Vorverfahren (Widerspruch, Einspruch) bereits durchgeführt?

## Zweck

Das Ziel bestimmt den Rechtsweg, die Verfahrensart, die Klageart und letztlich die einschlägigen Normen. Dieser Skill erfasst das Ziel strukturiert und gibt einen ersten Rechtsweg-Hinweis.

## Zentrale Normen zur Rechtswegsbestimmung

- § 13 GVG — ordentliche Gerichtsbarkeit (bürgerliche Rechtsstreitigkeiten, Streit über Privatrecht)
- § 40 VwGO — Verwaltungsrechtsweg (öffentlich-rechtliche Streitigkeiten, nicht verfassungsrechtlicher Art)
- § 51 SGG — Sozialgerichtsbarkeit (Angelegenheiten der Sozialversicherung)
- § 33 FGO — Finanzgerichtsbarkeit (Steuern und Abgaben)
- § 17 GVG — Rechtsweg-Verweisung; § 17a GVG — Rüge der Unzuständigkeit

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 10.12.2020 - III ZB 57/20, NJW 2021, 392 — Die Abgrenzung ordentliche Gerichtsbarkeit / Verwaltungsgerichtsbarkeit richtet sich nach der Natur des Anspruchs; privatrechtliche Forderung gegen Behörde ist vor ordentlichem Gericht zu klagen, nicht vor VG.
- BVerwG, Beschl. v. 18.09.2019 - 6 B 46.18, NVwZ 2020, 246 — Für die Eröffnung des Verwaltungsrechtswegs (§ 40 VwGO) genügt, dass eine öffentlich-rechtliche Streitigkeit vorliegt; die Abgrenzung zu bürgerlich-rechtlichen Streitigkeiten richtet sich nach dem Charakter der streitbegründenden Norm.
- BSG, Urt. v. 23.07.2020 - B 3 KR 4/20 R, NJW 2021, 183 — Streitigkeiten über gesetzliche Krankenversicherungsleistungen sind ausschließlich vor den Sozialgerichten (SGG) zu entscheiden; eine Klage vor dem ordentlichen Gericht ist unzulässig.
- BGH, Beschl. v. 17.06.2021 - I ZB 55/20, NJW 2021, 2437 — Bei Zweifeln über den zuständigen Rechtsweg ist der Rechtsstreit nach § 17a GVG an das zuständige Gericht zu verweisen; eine Rüge der Unzuständigkeit muss vor dem Mündlichkeitstermin erhoben werden.

## Zielfragen

**Was möchten Sie erreichen?**

| Nr. | Ziel | Typischer Rechtsweg |
|-----|------|---------------------|
| 1 | Anspruch durchsetzen (Zahlung, Unterlassung, Herausgabe) | ZPO / ordentliche Gerichtsbarkeit |
| 2 | Anspruch abwehren (Klageabweisung, Widerklage) | ZPO |
| 3 | Verwaltungsentscheidung anfechten (Bescheid) | VwGO Anfechtungsklage § 42 Abs. 1 Alt. 1 |
| 4 | Verwaltungsentscheidung erzwingen | VwGO Verpflichtungsklage § 42 Abs. 1 Alt. 2 |
| 5 | Sozialleistung durchsetzen oder anfechten | SGG |
| 6 | Steuerbescheid anfechten | FGO (Einspruch → Klage) |
| 7 | Strafanzeige erstatten | StPO / Staatsanwaltschaft |
| 8 | Verfassungsbeschwerde erheben | BVerfGG § 90 (Erschöpfung Rechtsweg) |
| 9 | Einstweiligen Rechtsschutz | §§ 935/940 ZPO / § 80 Abs. 5 VwGO |
| 10 | Familiensache (Sorge, Unterhalt, Scheidung) | FamFG |

## Rechtsweg-Entscheidungsbaum

```
Ist eine Behörde beteiligt?
├─ Ja → Handlung hoheitlich?
│       ├─ Ja → VwGO / SGG / FGO (je nach Sachgebiet)
│       └─ Nein → ordentliche Gerichtsbarkeit (Fiskusprivileg ausnahmsweise)
└─ Nein → ZPO (ordentliche Gerichtsbarkeit)
          ├─ Schiedsklausel vorhanden? → §§ 1025 ff. ZPO
          └─ Arbeitssache? → ArbGG; Familiensache? → FamFG
```

## Warnmechanik

Das System warnt bei folgenden Konstellationen:
- Nutzer nennt Ziel im Zivilrecht, Sachverhalt klingt nach öffentlichem Recht: Hinweis auf VwGO
- Nutzer möchte Strafanzeige, aber Sachverhalt betrifft nur Zivilrecht: kein Straftatbestand erkennbar
- Vorverfahren (Widerspruch) noch nicht durchgeführt: Klage unzulässig (§ 68 VwGO)

**Das System trifft keine verbindliche Rechtswegentscheidung.** Die endgültige Bestimmung obliegt dem Gericht (§ 17a GVG).

## Kommentarliteratur

- Kopp/Schenke VwGO § 40 (Rechtsweg öffentliches Recht)
- Zöller ZPO § 13 GVG (ordentlicher Rechtsweg)
- Baumbach/Lauterbach ZPO §§ 17/17a GVG (Rechtswegverweisung)

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
