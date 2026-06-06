---
name: ziel-und-rechtsweg-bestimmung
description: "Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG. Warnt bei Zweifelsfaellen im Subsumtions Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Ziel- und Rechtsweg-Bestimmung

## Arbeitsbereich

Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG. Warnt bei Zweifelsfaellen. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — kläre vor der Rechtsweg-Bestimmung

1. Was möchte der Nutzer erreichen?
2. Wer ist Gegner? (Privatperson / Unternehmen / Behörde / Staat)
3. Ist Behördenbeteiligung erkennbar? → Öffentliches Recht prüfen
4. Besteht Dringlichkeit? → Eilverfahren parallel skizzieren
5. Wurde ein Vorverfahren (Widerspruch, Einspruch) bereits durchgeführt?

## Zweck

Das Ziel bestimmt den Rechtsweg, die Verfahrensart, die Klageart und letztlich die einschlägigen Normen. Dieser Skill erfasst das Ziel strukturiert und gibt einen ersten Rechtsweg-Hinweis.

## Zentrale Normen zur Rechtswegsbestimmung

- § 13 GVG — ordentliche Gerichtsbarkeit (bürgerliche Rechtsstreitigkeiten)
- § 40 VwGO — Verwaltungsrechtsweg (öffentlich-rechtliche Streitigkeiten)
- § 51 SGG — Sozialgerichtsbarkeit (Sozialversicherung)
- § 33 FGO — Finanzgerichtsbarkeit (Steuern und Abgaben)
- § 2 ArbGG — Arbeitsgerichtsbarkeit (Arbeitsverhältnisse)
- § 17 GVG — Rechtsweg-Verweisung; § 17a GVG — Rüge der Unzuständigkeit

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
| 11 | Arbeitssache (Kündigung, Lohn) | ArbGG |
| 12 | EU-Recht durchsetzen / anwenden | Nationales Gericht + ggf. Vorabentscheidungsersuchen Art. 267 AEUV |

## Rechtsweg-Entscheidungsbaum

```
Ist eine Behörde beteiligt?
├─ Ja → Handlung hoheitlich?
│ ├─ Ja → VwGO / SGG / FGO (je nach Sachgebiet)
│ │ ├─ Sozialversicherung → SGG
│ │ ├─ Steuer → FGO
│ │ └─ sonst öffentl. Recht → VwGO
│ └─ Nein → ordentliche Gerichtsbarkeit (Fiskusprivileg ausnahmsweise)
└─ Nein → ZPO (ordentliche Gerichtsbarkeit)
 ├─ Schiedsklausel vorhanden? → §§ 1025 ff. ZPO
 ├─ Arbeitssache? → ArbGG
 └─ Familiensache? → FamFG
```

## Vorverfahren und Fristen

| Rechtsweg | Vorverfahren | Frist |
|---|---|---|
| VwGO | Widerspruch (§ 70 VwGO) | 1 Monat ab VA-Bekanntgabe |
| VwGO | Klage nach Widerspruchsbescheid | 1 Monat ab Zustellung WB (§ 74 VwGO) |
| SGG | Widerspruch (§ 83 SGG) | 1 Monat |
| FGO | Einspruch (§ 347 AO) | 1 Monat |
| ArbGG | Kündigungsschutzklage | 3 Wochen ab Zugang Kündigung (§ 4 KSchG) |
| ZPO | keine zwingenden Vorverfahren | Verjährungsfristen (§§ 195 ff. BGB) |

## Zweifelsfälle und Warnungen

- **Doppelte Rechtswegmöglichkeit:** Bei gemischten Sachverhalten (z. B. Amtshaftung § 839 BGB: ordentliche Gerichtsbarkeit; Hoheitsakt: VwGO) ist Trennungsprinzip zu beachten.
- **Rüge der Unzuständigkeit (§ 17a GVG):** Rechtzeitig erheben; Verweisung an zuständiges Gericht möglich.
- **Unionsrecht:** Nationales Gericht wendet EU-Recht an; bei Auslegungsfragen: Vorabentscheidungsersuchen (Art. 267 AEUV; → eu-vorabentscheidung-pruefen).

## Ausgabe

Rechtsweg-Bestimmung mit Entscheidungsbaum, Klageart, Zuständigkeit, Frist und Warnungen bei Zweifelsfällen. Empfehlung zur Folgeskill-Nutzung (z. B. verfahrensart-bestimmen, workflow-fristen-und-risikoampel).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern (dejure.org, bgh.de, bverfg.de).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (GVG §§ 13, 17, 17a; VwGO §§ 40, 70, 74; SGG § 51; FGO § 33; ArbGG § 2; KSchG § 4; BVerfGG § 90; ZPO §§ 935, 940, 1025 ff.).
