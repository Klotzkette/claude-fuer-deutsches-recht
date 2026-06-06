---
name: strafbefehl-aktenanlage
description: "Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeichnis. Normen § 410 StPO Einspruchsfrist § 147 StPO Akteneinsicht § 43 StPO Fristberechnung. Output Mandatsakte-Template Fristenuebersicht Excel-Export Akten-Checkliste. Abgrenzung: strafbefehl-kommandocenter für uebergreifende Mandats-Steuerung im Strafbefehl Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Aktenanlage im Strafbefehlsverfahren

## Arbeitsbereich

Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeichnis. Normen § 410 StPO Einspruchsfrist § 147 StPO Akteneinsicht § 43 StPO Fristberechnung. Output Mandatsakte-Template Fristenuebersicht Excel-Export Akten-Checkliste. Abgrenzung: strafbefehl-kommandocenter für uebergreifende Mandats-Steuerung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Liegt die Vollmacht des Mandanten vor?** — Ohne Vollmacht keine Verfahrenshandlungen.
2. **Zugangsdatum des Strafbefehls dokumentiert?** — Ausgangspunkt fuer alle Fristen.
3. **Delikt und Aktenzeichen notiert?** — Grundlage fuer alle Schriftsaetze.
4. **Mandantenziel festgehalten?** — Freispruch, Einstellung, Strafmassreduzierung, Fahrverbots-Vermeidung.
5. **Sofortmassnahmen ausgeloest?** — Einspruch fristgerecht eingelegt? Akteneinsicht beantragt?

## Aktenstruktur Strafbefehlsmandat

```
01_MANDANT
 - Vollmacht Original
 - Personalien, Kontakt
 - Mandantenziel (schriftlich)

02_STRAFBEFEHL
 - Strafbefehl Original / Kopie
 - Zustellungsurkunde
 - § 409-Pruefungs-Notiz

03_FRISTEN
 - Fristen-Uebersicht (Excel oder Tabelle)
 - Einspruchsfrist: [DATUM]
 - Revisionsbegründungsfrist (falls noetig): [DATUM]

04_SCHRIFTSAETZE_AUSGEHEND
 - Einspruch (mit Eingangsbestaetigung)
 - Akteneinsichtsantrag
 - Weitere Antraege

05_AKTENEINSICHT
 - Ermittlungsakte vollstaendig
 - Messakte (bei Verkehrsdelikten)
 - Beweismittelverzeichnis

06_KORRESPONDENZ
 - Behörden, Gericht, StA
 - E-Mails chronologisch

07_HAUPTVERHANDLUNG
 - Einlassung (Endfassung)
 - Beweisantraege
 - Plaedoyer

08_URTEIL_RECHTSMITTEL
 - Urteil Original
 - Rechtsmittelschrift
 - Revisionsbegründung
```

## Fristen-Uebersicht — Template

| Frist | Rechtsgrundlage | Datum | Erledigt |
|-------|----------------|-------|---------|
| Einspruch | § 410 Abs. 1 StPO | [Zustellung + 14 Tage] | □ |
| Akteneinsicht | § 147 StPO | [Sofort] | □ |
| Wiedereinsetzung (falls noetig) | § 45 Abs. 1 StPO | [Kenntnis + 7 Tage] | □ |
| Berufung | § 314 StPO | [Urteil + 7 Tage] | □ |
| Revision | § 341 StPO | [Urteil + 7 Tage] | □ |
| Revisionsbegründung | § 345 StPO | [Urteilszustellung + 1 Monat] | □ |

## Beweismittelverzeichnis — Template

| Nr. | Beweismittel | Art | Akten-Bl. | Beweisthema | Status |
|-----|-------------|-----|----------|-------------|--------|
| 1 | Zeuge [Name] | Zeuge | Bl. [X] | [Thema] | auswerten |
| 2 | Polizeibericht | Urkunde | Bl. [X] | Tathergang | auswerten |
| 3 | Messprotokoll | Urkunde | Bl. [X] | Geschwindigkeit | kritisch pruefen |

## Zentrale Normen

- **§ 147 StPO** — Akteneinsicht
- **§ 410 StPO** — Einspruchsfrist
- **§ 44, 45 StPO** — Wiedereinsetzung
- **§ 314, 341, 345 StPO** — Rechtsmittelfristen

## Harte Leitplanken

- Aktenanlage unmittelbar bei Mandatsuebernahme — nicht nach Einspruch.
- Fristenkalender zwingend fuehren, nie im Kopf.
- Vollmacht immer im Original verwahren.
- Bei Aktennachlieferungen: Verzeichnis aktualisieren, neue Teile markieren.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
