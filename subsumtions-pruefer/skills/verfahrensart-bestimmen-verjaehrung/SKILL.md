---
name: verfahrensart-bestimmen-verjaehrung
description: "Bestimmt die passende Verfahrensart: ordentlich (ZPO), einstweilig (§§ 935/940 ZPO), Mahnverfahren, FG-Verfahren, Schiedsverfahren, Insolvenzverfahren, OWi-Verfahren, Verwaltungs-, Straf- und Verfassungsgerichtsverfahren. Gibt formale Mindestvoraussetzungen im Subsumtions Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Verfahrensart bestimmen

## Arbeitsbereich

Bestimmt die passende Verfahrensart: ordentlich (ZPO), einstweilig (§§ 935/940 ZPO), Mahnverfahren, FG-Verfahren, Schiedsverfahren, Insolvenzverfahren, OWi-Verfahren, Verwaltungs-, Straf- und Verfassungsgerichtsverfahren. Gibt formale Mindestvoraussetzungen. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — kläre vor der Verfahrensauswahl

1. Was ist das Rechtsschutzziel? (Zahlung, Unterlassung, Feststellung, Anfechtung VA, Strafverfolgung)
2. Besteht Eilbedürftigkeit? → einstweiliger Rechtsschutz prüfen
3. Ist eine Schiedsklausel im Vertrag vereinbart? (§ 1029 ZPO)
4. Wie hoch ist der Streitwert? (AG bis EUR 5.000 / LG ab EUR 5.000)
5. Ist das ordentliche Gericht durch Sondergerichtsstände ausgeschlossen? (Arbeitsgericht, Familiengericht)

## Zentrale Verfahrensnormen

- §§ 23, 71 GVG — sachliche Zuständigkeit AG/LG nach Streitwert
- §§ 12 ff. ZPO — örtliche Zuständigkeit; allgemeiner Gerichtsstand Wohnsitz
- §§ 935, 940 ZPO — einstweilige Verfügung (Sicherungs- / Regelungsverfügung)
- §§ 688 ff. ZPO — Mahnverfahren; §§ 1025 ff. ZPO — Schiedsverfahren
- §§ 23 ff. FamFG — örtliche Zuständigkeit im FG-Verfahren
- § 1029 ZPO — Schiedsvereinbarung (formell: schriftlich)

## Übersicht der Verfahrensarten

### Ordentliches Klageverfahren (ZPO)

**Wann:** Zivilrechtliche Ansprüche auf Zahlung, Herausgabe, Unterlassung; ohne Eilbedürfnis.

**Zuständigkeit:** Amtsgericht bis EUR 5.000 (§ 23 GVG); Landgericht ab EUR 5.000 (§ 71 GVG); Anwaltszwang vor LG, OLG, BGH.

**Mindestvoraussetzungen Klage:** Rubrum, bestimmter Antrag (§ 253 Abs. 2 Nr. 2 ZPO), Klagebegründung, Beweisangebote.

### Einstweiliger Rechtsschutz (ZPO)

**Wann:** Eilbedürftigkeit (Verfügungsgrund) und Glaubhaftmachung des Anspruchs (Verfügungsanspruch). §§ 935/940 ZPO.

**Sicherungsverfügung § 935 ZPO:** Zur Sicherung eines bestehenden Rechts.
**Regelungsverfügung § 940 ZPO:** Zur vorläufigen Regelung eines streitigen Rechtsverhältnisses.

**Entscheidungsbaum einstweiliger Rechtsschutz:**
```
Eilbedürftigkeit?
├─ Ja und Sicherung eines bestehenden Rechts → einstw. Verfügung § 935 ZPO
├─ Ja und vorläufige Regelung → einstw. Verfügung § 940 ZPO
└─ Nein → ordentliche Klage
```

**Selbsterfüllungsverbot:** Antragsteller darf nicht durch eigenes Handeln Eilbedürftigkeit beseitigen.

### Mahnverfahren (§§ 688 ff. ZPO)

**Wann:** Unbestrittene Geldforderungen; einfacher als Klage; kostengünstiger.

**Ablauf:** Mahnantrag (online oder Formular) → Mahnbescheid → Widerspruch? → Vollstreckungsbescheid → Vollstreckung.

**Ausschluss:** Wenn Forderung von Gegenleistung abhängt (§ 688 Abs. 2 ZPO) oder Zustellung im Ausland nötig.

### Verwaltungsgerichtsverfahren (VwGO)

**Wann:** Öffentlich-rechtliche Streitigkeiten; Anfechtung von Verwaltungsakten; § 40 VwGO.

**Vorverfahren:** Widerspruch (§§ 68 ff. VwGO) als Zulässigkeitsvoraussetzung (Ausnahme: § 68 Abs. 1 S. 2 VwGO).

**Fristen:** Widerspruchsfrist: 1 Monat (§ 70 VwGO); Klagefrist: 1 Monat nach Widerspruchsbescheid (§ 74 VwGO).

### Arbeitsgerichtsverfahren (ArbGG)

**Wann:** Streitigkeiten zwischen Arbeitgeber und Arbeitnehmer aus dem Arbeitsverhältnis (§ 2 ArbGG).

**Besonderheiten:** Kein Anwaltszwang in der 1. Instanz; Güteverhandlung (§ 54 ArbGG) obligatorisch.

### Schiedsverfahren (§§ 1025 ff. ZPO)

**Wann:** Schiedsvereinbarung (§ 1029 ZPO) in Vertragsform; schriftlich.

**Vollstreckbarkeit:** Schiedsspruch muss durch staatliches Gericht für vollstreckbar erklärt werden (§ 1060 ZPO) oder unterliegt Anerkennung nach New Yorker Übereinkommen (international).

### Strafverfahren (StPO)

**Wann:** Strafbare Handlung; Strafanzeige bei Polizei oder Staatsanwaltschaft.

**Privatklage (§§ 374 ff. StPO):** Bei bestimmten Delikten (z. B. Beleidigung, Hausfriedensbruch) direkt beim AG.

## Verfahrensauswahl-Entscheidungsbaum

```
Rechtsschutzziel?
├─ Geldforderung, unbestritten → Mahnverfahren (§§ 688 ff. ZPO)
├─ Geldforderung, streitig → Klage (ZPO)
├─ Unterlassung, dringend → einstweilige Verfügung (§§ 935/940 ZPO)
├─ VA-Anfechtung → VwGO (Widerspruch + Klage)
├─ Strafe / OWi → StPO / OWiG
├─ Schiedsklausel → §§ 1025 ff. ZPO
└─ Arbeitssache → ArbGG
```

## Formale Mindestvoraussetzungen

| Verfahrensart | Formvoraussetzungen |
|---|---|
| Klage ZPO | Rubrum, bestimmter Antrag (§ 253 Abs. 2 Nr. 2 ZPO), Begründung, Beweisangebote |
| einstw. Verfügung | Glaubhaftmachung (§ 294 ZPO); Verfügungsanspruch und -grund; eidesstattl. Versicherung |
| Mahnantrag | Online-Formular oder amtl. Vordruck; bestimmte Geldforderung; keine Abhängigkeit von Gegenleistung |
| Schiedsklage | Schiedsvereinbarung vorlegen; Klageschrift nach Schiedsordnung |

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de (ZPO, GVG, VwGO, ArbGG, ArbGG, StPO, OWiG).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, bgh.de).
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (ZPO §§ 23, 71 GVG; §§ 253, 688 ff., 935, 940, 1025 ff., 1029 ZPO; §§ 40, 68 ff., 74 VwGO).
