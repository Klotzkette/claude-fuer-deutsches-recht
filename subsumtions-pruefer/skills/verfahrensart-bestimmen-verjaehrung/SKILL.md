---
name: verfahrensart-bestimmen-verjaehrung
description: "Verfahrensart Bestimmen Verjaehrung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verfahrensart Bestimmen Verjaehrung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verfahrensart Bestimmen Verjaehrung** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verfahrensart-bestimmen` | Bestimmt die passende Verfahrensart: ordentlich (ZPO), einstweilig (§§ 935/940 ZPO), Mahnverfahren, FG-Verfahren, Schiedsverfahren, Insolvenzverfahren, OWi-Verfahren, Verwaltungs-, Straf- und Verfassungsgerichtsverfahren. Gibt formale Mindestvoraussetzungen. |
| `verjaehrung-fristen-pruefen` | Prüft Verjährungsfristen: Regelfrist 3 Jahre (§§ 195/199 BGB), kenntnisabhaengige Fristen, absolute 10- und 30-Jahresfristen, Hemmung (§§ 203 ff. BGB), Neubeginn (§ 212 BGB), prozessuale Notfristen und EU-Verjährungsregeln. Ergebnis: verjährt ja/nein/fraglich. |
| `generalklauseln-pruefen` | Prüft Generalklauseln wie Treu und Glauben (§ 242 BGB), gute Sitten (§ 138 BGB), billiges Ermessen, öffentliches Interesse und Verhältnismäßigkeit. Gibt Indizien und Fallgruppen statt mechanischer Subsumtion. Warnt vor der Grenzen automatisierter Prüfung. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Verfahrensart Bestimmen Verjaehrung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verfahrensart-bestimmen`

**Fokus:** Bestimmt die passende Verfahrensart: ordentlich (ZPO), einstweilig (§§ 935/940 ZPO), Mahnverfahren, FG-Verfahren, Schiedsverfahren, Insolvenzverfahren, OWi-Verfahren, Verwaltungs-, Straf- und Verfassungsgerichtsverfahren. Gibt formale Mindestvoraussetzungen.

# Verfahrensart bestimmen

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

## 2. `verjaehrung-fristen-pruefen`

**Fokus:** Prüft Verjährungsfristen: Regelfrist 3 Jahre (§§ 195/199 BGB), kenntnisabhaengige Fristen, absolute 10- und 30-Jahresfristen, Hemmung (§§ 203 ff. BGB), Neubeginn (§ 212 BGB), prozessuale Notfristen und EU-Verjährungsregeln. Ergebnis: verjährt ja/nein/fraglich.

# Verjährung und Fristen prüfen

## Triage zu Beginn — kläre vor der Verjährungsprüfung

1. Wann ist der Anspruch entstanden? (Vertragsabschluss, Schadenseintritt, Fälligkeit)
2. Wann hatte der Gläubiger Kenntnis von Anspruch und Schuldner?
3. Ist Verjährungseinrede bereits erhoben oder wird sie vom Gegner erhoben werden?
4. Gibt es Hemmungstatbestände? (Verhandlungen, Klageerhebung, Mahnbescheid)
5. Gilt eine Sonderverjährung (Kaufmängel 2 Jahre, Ausschlussfristen Tarif/Vertrag)?

## Zentrale Paragrafenkette

- § 195 BGB — Regelverjährung 3 Jahre
- § 199 Abs. 1 BGB — Beginn: Ende des Entstehungsjahres + Kenntnis
- § 199 Abs. 4 BGB — absolute Verjährung ohne Kenntnis: 10 Jahre
- § 197 BGB — 30 Jahre für titulierte Ansprüche und Herausgabeansprüche aus Eigentum
- §§ 203-213 BGB — Hemmung der Verjährung (Verhandlung, Klage, Mahnbescheid)
- § 212 BGB — Neubeginn der Verjährung (Anerkenntnis, Vollstreckungshandlung)
- § 214 BGB — Verjährungseinrede: muss erhoben werden, kein Amtsbeweise
- § 438 BGB — Sonderverjährung Kaufmängel (2 Jahre / 5 Jahre Bau)
- § 634a BGB — Sonderverjährung Werkvertragsansprüche (2 Jahre / 5 Jahre)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Verjährungsfristen im deutschen Recht

### Regelfrist § 195 BGB

3 Jahre; Beginn: 31. Dezember des Jahres, in dem der Anspruch entstanden ist und der Gläubiger Kenntnis erlangt hat oder hätte erlangen müssen (§ 199 Abs. 1 BGB).

**Wichtig:** Beginn zum 31.12. des Entstehungsjahres — nicht zum Tag des schädigenden Ereignisses!

### Absolute Verjährungsfristen

- 10 Jahre: bei Ansprüchen ohne Kenntnis (§ 199 Abs. 4 BGB)
- 30 Jahre: Herausgabeansprüche aus Eigentum; titulierte Ansprüche (§§ 197/201 BGB)

### Besondere Fristen

| Anspruch | Frist | Norm |
|---------|-------|------|
| Kaufmängel bewegliche Sachen | 2 Jahre ab Übergabe | § 438 Abs. 1 Nr. 3 BGB |
| Kaufmängel Bauwerke | 5 Jahre ab Übergabe | § 438 Abs. 1 Nr. 2 BGB |
| Werkvertrag Mängel | 2 Jahre (Regelfall) | § 634a BGB |
| UWG-Abmahnung | 6 Monate ab Kenntnis; absolut 3 Jahre | § 11 UWG |
| Reisevertragsansprüche | 2 Jahre | § 651j BGB |

### Verjährung im Arbeitsrecht

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Hemmung der Verjährung §§ 203–213 BGB

Hemmung: Die Verjährungsfrist läuft nicht; die Restfrist läuft nach Ende des Hemmungszeitraums weiter.

**Wichtige Hemmungstatbestände:**
- Klageerhebung (§ 204 Abs. 1 Nr. 1 BGB): Hemmung mit Einreichung, wenn demnächst zugestellt
- Mahnbescheid (§ 204 Abs. 1 Nr. 3 BGB): Hemmung bei Zustellung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Stillhaltevereinbarung (§ 205 BGB): vertragliche Stundung

## Neubeginn der Verjährung § 212 BGB

Der Neubeginn löscht die bisher abgelaufene Verjährungszeit:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Zwangsvollstreckungshandlung

## Prozessuale Notfristen

- Einspruch gegen Versäumnisurteil: 2 Wochen (§ 339 ZPO)
- Berufungsfrist: 1 Monat ab Zustellung (§ 517 ZPO)
- Revisionsfrist: 1 Monat ab Zustellung (§ 548 ZPO)
- Verfassungsbeschwerde: 1 Monat (§ 93 Abs. 1 BVerfGG); bei VA: 1 Jahr (§ 93 Abs. 3 BVerfGG)

## Entscheidungsbaum Verjährungsprüfung

```
Anspruch entstanden wann?
└─ Beginn: 31.12. des Entstehungsjahres
 ├─ Regelfrist: 3 Jahre (§ 195 BGB)
 ├─ Sonderverjährung einschlägig? → Tabelle oben
 ├─ Hemmungstatbestand vorhanden?
 │ ├─ Ja → Hemmungszeitraum herausrechnen
 │ └─ Nein → weiter
 └─ Neubeginn ausgelöst?
 ├─ Ja → neue Frist ab Neubeginnzeitpunkt
 └─ Nein → Ergebnis: verjährt / nicht verjährt
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `generalklauseln-pruefen`

**Fokus:** Prüft Generalklauseln wie Treu und Glauben (§ 242 BGB), gute Sitten (§ 138 BGB), billiges Ermessen, öffentliches Interesse und Verhältnismäßigkeit. Gibt Indizien und Fallgruppen statt mechanischer Subsumtion. Warnt vor der Grenzen automatisierter Prüfung.

# Generalklauseln prüfen

## Triage zu Beginn — kläre vor der Generalklausel-Prüfung

1. Ist eine speziellere Norm vorhanden, die die Generalklausel verdrängt? (lex specialis-Vorrang)
2. Soll Treu und Glauben (§ 242 BGB) als Einrede oder als Anspruchsmodifikation wirken?
3. Handelt es sich um Privatrecht (§§ 138, 242 BGB) oder öffentliches Recht (Verhältnismäßigkeit)?
4. Besteht ein Zeit- und Umstandsmoment für Verwirkung? — beide kumulativ erforderlich
5. Welche Fallgruppe der Generalklausel ist primär einschlägig? → System listet Fallgruppen

## Zweck

Generalklauseln entziehen sich per definitionem der rein mechanischen Subsumtion. Dieser Skill liefert anerkannte Fallgruppen, Indizien und Auslegungsmaßstäbe, die als Orientierung dienen. Das System gibt ausdrücklich keine abschließende Bewertung bei Generalklauseln — es benennt Indizien, keine Ergebnisse.

## Zentrale Normen

- § 242 BGB — Treu und Glauben (Fallgruppen: Verwirkung, venire contra factum proprium, exceptio doli generalis)
- § 138 BGB — Sittenwidrigkeit und Wucher (Nichtigkeit ex lege)
- § 315 BGB — Billiges Ermessen bei einseitiger Leistungsbestimmung
- Art. 20 Abs. 3 GG — Verhältnismäßigkeitsgrundsatz im öffentlichen Recht
- Art. 5 Abs. 4 EUV — Verhältnismäßigkeit auf EU-Ebene

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wichtige Generalklauseln

### § 242 BGB — Treu und Glauben

**Definition:** Schuldner muss so leisten, wie Treu und Glauben mit Rücksicht auf die Verkehrssitte es erfordern.

**Fallgruppen (Auswahl):**
- **Verwirkung:** Recht darf nach langer Nichtausübung und Vertrauenstatbestand beim Verpflichteten nicht mehr geltend gemacht werden (BGH st. Rspr.; Zeit- und Umstandsmoment kumulativ erforderlich)
- **Venire contra factum proprium:** eigenes widersprüchliches Verhalten
- **Leistungsverweigerungsrecht** wegen unverhältnismäßiger Aufwendungen (§ 275 Abs. 2 BGB als Spezialregelung)
- **Exceptio doli generalis:** arglistiges Geltendmachen formal bestehender Rechte

**Entscheidungsbaum Verwirkung:**
```
Zeitmoment: Ungewöhnlich lange Nichtausübung?
├─ Nein → keine Verwirkung
└─ Ja → Umstandsmoment: Hat Schuldner auf Nichtgeltendmachung vertraut und disponiert?
 ├─ Nein → keine Verwirkung
 └─ Ja → Verwirkung prüfbar; aber: Wertungsfrage des Gerichts
```

### § 138 BGB — Sittenwidrigkeit

**Definition:** Rechtsgeschäft, das gegen die guten Sitten verstößt, ist nichtig.

**Fallgruppen:**
- Wucherische Rechtsgeschäfte (§ 138 Abs. 2 BGB): Ausbeutung einer Zwangslage, Leichtsinn oder Unerfahrenheit
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bürgschaftsverträge von einkommensschwachen Angehörigen (BGH ständige Rechtsprechung)
- Knebelungsverträge, Schmiergeldabreden

### Verhältnismäßigkeitsgrundsatz

Im öffentlichen Recht: Geeignetheit, Erforderlichkeit, Angemessenheit (Übermaßverbot).

**Prüfungsschema:**
1. **Geeignetheit:** Kann die Maßnahme den Zweck fördern?
2. **Erforderlichkeit:** Gibt es ein milderes, gleich geeignetes Mittel?
3. **Angemessenheit (Verhältnismäßigkeit i.e.S.):** Überwiegen die Vorteile die Nachteile? — Abwägung; das System listet Argumente, trifft keine Entscheidung

### § 315 BGB — Billiges Ermessen

Bei einseitiger Leistungsbestimmung: Das System prüft, ob die Bestimmung sich im Rahmen des Üblichen und Sachgerechten hält. Indizien: Marktvergleich, frühere Vertragspraxis, Begründung der Bestimmung.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Das System gibt:
- Name der Generalklausel
- Einschlägige Fallgruppe (soweit erkennbar)
- Indizien pro und contra
- Ausdrücklichen Hinweis: "Das Ergebnis dieser Prüfung ist eine Indiziensammlung, keine rechtliche Bewertung."

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

<!-- AUDIT 27.05.2026 bundle_044
 → Vollzitat-Zeile und Fundstellen-Verweis NJW 2021, 1952 gelöscht
 → kein Ersatz eingetragen (keine verifizierte Alternative gefunden)
-->
