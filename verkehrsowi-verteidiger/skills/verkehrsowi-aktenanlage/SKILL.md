---
name: verkehrsowi-aktenanlage
description: "Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverzeichnis (Messgerät, Eichschein). Output Aktenstruktur, Fristen-Übersicht-Tabelle, Beweismittelverzeichnis. Abgrenzung: Akteneinsicht Messakte siehe verkehrsowi-akteneinsicht-messakte; Einspruchsfrist siehe verkehrsowi-fristen-einspruch im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Aktenanlage OWi-Mandat

## Arbeitsbereich

Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverzeichnis (Messgerät, Eichschein). Output Aktenstruktur, Fristen-Übersicht-Tabelle, Beweismittelverzeichnis. Abgrenzung: Akteneinsicht Messakte siehe verkehrsowi-akteneinsicht-messakte; Einspruchsfrist siehe verkehrsowi-fristen-einspruch. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Vollmacht vorhanden?** — Ohne Vollmacht keine Akteneinsicht.
2. **Zustellungsdatum des Bescheids dokumentiert?** — Fristbeginn.
3. **Aktenzeichen und Delikt notiert?** — Grundlage für Schriftsaetze.
4. **Mandantenziel klar?** — Einspruch, Einstellung, Fahrverbot-Vermeidung.
5. **Sofortmassnahmen eingeleitet?** — Einspruch und Akteneinsicht.

## Aktenstruktur OWi-Mandat

```
01_MANDANT
 - Vollmacht Original
 - Personalien, Kontakt
 - Mandantenziel schriftlich

02_BUSSGELDBESCHEID
 - Bussgeldbescheid Original/Kopie
 - Zustellungsurkunde
 - § 66 OWiG-Pruefungsnotiz

03_FRISTEN
 - Einspruchsfrist: Zustellungsdatum + 14 Tage
 - Rechtsbeschwerde-Frist (wenn noetig): Urteil + 7 Tage
 - Verjährungs-Check

04_SCHRIFTSAETZE_AUSGEHEND
 - Einspruch (mit Eingangsbestaetigung)
 - Akteneinsichtsantrag (mit Messakte-Aufzaehlung)

05_MESSAKTE
 - Eichschein (Gueltigkeit geprueft: Datum markiert)
 - Messprotokoll
 - Schulungsnachweis
 - Rohmessdaten (falls vorhanden)
 - Messfoto hochaufloesend

06_BEWEISMITTELVERZEICHNIS
 (s. Vorlage unten)

07_KORRESPONDENZ
 - Bussgeldbehoerde, Amtsgericht, StA
 - Chronologisch

08_HAUPTVERHANDLUNG
 - Einlassung oder Schweigen-Notiz
 - Beweisantraege
 - Plaedoyer

09_URTEIL_RECHTSBEHELFE
 - Urteil Original
 - Rechtsbeschwerde
```

## Fristen-Uebersicht OWi

| Frist | Rechtsgrundlage | Datum | Erledigt |
|-------|----------------|-------|---------|
| Einspruch | § 67 Abs. 1 OWiG | [Zustellung + 14T] | □ |
| Akteneinsicht | § 49 OWiG | Sofort | □ |
| Wiedereinsetzung (falls noetig) | § 52 OWiG | [Kenntnis + 7T] | □ |
| Rechtsbeschwerde | § 79 Abs. 1 OWiG | [Urteil + 7T] | □ |
| Rechtsbeschwerde-Begruendung | § 79 Abs. 3 OWiG | [Zustellung Urteil + 1M] | □ |
| Vier-Monats-Frist Fahrverbot | § 25 Abs. 2a StVG | [Rechtskraft + 4M] | □ |

## Beweismittelverzeichnis Messakte

| Nr. | Dokument | Datum | Geprueft | Status |
|-----|---------|-------|---------|--------|
| 1 | Eichschein | [DATUM] | □ | Gueltig bis [DATUM] |
| 2 | Messprotokoll | [DATUM] | □ | Angriffspunkte? |
| 3 | Schulungsnachweis | [DATUM] | □ | Beamter [NAME] |
| 4 | Rohmessdaten | [DATUM] | □ | Vorhanden / Fehlt |
| 5 | Messfoto | [DATUM] | □ | Fahrer identifizierbar? |

## Harte Leitplanken

- Aktenanlage unmittelbar bei Mandatsuebernahme.
- Fristen immer als Erstes eintragen.
- Messakte-Vollstaendigkeitspruefung ist Pflicht.
- Bei Aktennachlieferungen: Verzeichnis aktualisieren.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
