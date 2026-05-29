---
name: strafbefehl-quality-gate
description: "Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO Einspruchsfrist § 409 StPO Strafbefehlsinhalt § 46 StGB Strafzumessung. Output Fehlerliste mit Ampel-Bewertung und Checkliste offener Punkte. Abgrenzung: strafbefehl-kommandocenter für laufende Mandats-Steuerung."
---

# Quality Gate — Strafbefehl-Mandat

## Zweck

Dieser Skill ist die abschliessende Qualitaetssicherung fuer das Strafbefehlsmandat. Er ist an drei kritischen Punkten einzusetzen:
1. **Vor Einspruch-Versand** — alle formalen Voraussetzungen erfuellt?
2. **Vor der Hauptverhandlung** — vollstaendige Vorbereitung?
3. **Nach dem Urteil** — Rechtsmitteloptionen geprueft?

## Gate 1: Vor Einspruch-Versand

```
□ Einspruchsfrist § 410 Abs. 1 StPO berechnet und noch offen?
   Zustellungsdatum: [DATUM] + 14 Tage = Fristende: [DATUM]
□ Vollmacht des Mandanten liegt vor?
□ Strafbefehl-Inhalt auf § 409 StPO geprueft (Pflicht-Inhalte)?
□ Delikt ist Vergehen (kein Verbrechen § 12 StGB)?
□ Sanktion liegt im Katalog § 407 Abs. 2 StPO?
□ Beschraenkt oder unbeschraenkt? Mandant aufgeklaert?
□ Einspruchsschreiben: Name, Az., Zustellungsdatum, Datum, Unterschrift?
□ Einspruch per EB-Fax oder anwaltlichem Fax versendet?
□ Eingang beim Gericht bestaetigt?
□ Akteneinsicht gleichzeitig beantragt?
AMPEL: GRUEN wenn alle Punkte erfuellt / ROT wenn Frist nicht mehr offen
```

## Gate 2: Vor Hauptverhandlung

```
□ Akteneinsicht vollstaendig erhalten und ausgewertet?
□ Einlassung mit Mandant abgestimmt (Schweigen oder Aussage)?
□ Beweisantraege vorbereitet (Beweisthema + Beweismittel)?
□ Sachverstaendiger beauftragt wenn noetig?
□ Einkommensnachweise fuer Tagessatz-Pruefung vollstaendig?
□ § 153a-Antrag bei Staatsanwaltschaft gestellt oder abgelehnt?
□ Verstaendigung § 257c StPO geprueft und entschieden?
□ Mandant ueber HV-Ablauf informiert (Aufruf, Vernehmung, Plaedoyer, Letztes Wort)?
□ Fahrerlaubnis-Problematik (§ 69 StGB / § 44 StGB) vollstaendig bearbeitet?
□ Pflichtverteidiger-Beiordnung geprueft (§ 140 StPO)?
□ Erscheinungspflicht oder Entbindungsantrag § 411 Abs. 2 StPO?
AMPEL: GRUEN wenn vollstaendig / GELB wenn offene Punkte / ROT wenn kritische Luecken
```

## Gate 3: Nach Urteil

```
□ Urteil vollstaendig angehoert / protokolliert?
□ Rechtsmittelfrist notiert: 1 Woche ab Urteilsverkuendung (§§ 314, 341 StPO)?
□ Fristende: [DATUM DES URTEILS] + 7 Tage = [FRISTENDE]
□ Berufung oder Revision geprüft? (Tatsachen vs. Rechtsfehler)
□ Annahme-Berufung § 313 StPO: Erfolgaussichten vorhanden?
□ Absolute Revisionsgründe § 338 StPO geprueft?
□ Tagessatz-Hoehe korrekt berechnet?
□ Fahrerlaubnis-Massnahme korrekt?
□ Beschraenktes Rechtsmittel auf Rechtsfolgen moeglich?
□ Mandant ueber Entscheidung und Optionen informiert?
□ Ratenzahlungsantrag § 42 StGB noetig?
AMPEL: GRUEN wenn zufriedenstellend / GELB wenn Rechtsmittel moeglich / ROT wenn Fehler vorhanden
```

## Harte Leitplanken

- Quality Gate niemals ueberspringen — auch bei einfachen Faellen.
- ROT-Punkte immer dokumentieren und ansprechen.
- Mandant ueber jeden Schritt informieren und Entscheidungen schriftlich bestaetigen.
- Anwaltliche Endkontrolle bei jedem Gate zwingend.
