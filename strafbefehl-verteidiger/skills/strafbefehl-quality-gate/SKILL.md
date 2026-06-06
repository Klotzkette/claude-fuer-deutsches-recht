---
name: strafbefehl-quality-gate
description: "Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO Einspruchsfrist § 409 StPO Strafbefehlsinhalt § 46 StGB Strafzumessung. Output Fehlerliste mit Ampel-Bewertung und Checkliste offener Punkte. Abgrenzung: strafbefehl-kommandocenter für laufende Mandats-Steuerung im Strafbefehl Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Quality Gate — Strafbefehl-Mandat

## Arbeitsbereich

Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO Einspruchsfrist § 409 StPO Strafbefehlsinhalt § 46 StGB Strafzumessung. Output Fehlerliste mit Ampel-Bewertung und Checkliste offener Punkte. Abgrenzung: strafbefehl-kommandocenter für laufende Mandats-Steuerung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
