---
name: verkehrsowi-aktenanlage
description: "Für Aktenanlage OWi-Mandat: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Aktenanlage OWi-Mandat

## Arbeitsbereich

Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverzeichnis (Messgerät, Eichschein). Output Aktenstruktur, Fristen-Übersicht-Tabelle, Beweismittelverzeichnis. Abgrenzung: Akteneinsicht Messakte siehe verkehrsowi-akteneinsicht-messakte; Einspruchsfrist siehe verkehrsowi-fristen-einspruch. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen; Verjährung nach Delikt und anwendbarer Fassung (aktuell § 26 Abs. 3 StVG grundsätzlich 6 Monate bei § 24 Abs. 1, §§ 31–33 OWiG); Fahrverbot § 25 Abs. 2, 3 und 6 StVG (grundsätzlich spätestens 1 Monat nach Rechtskraft wirksam, Viermonatsprivileg nur bei erfüllten Voraussetzungen; Verbotsfrist gesondert); § 79 OWiG Rechtsbeschwerde 1 Woche. Historische Fassung und Übergang prüfen; [amtlich belegte Einzelheiten](../../references/verkehrsowi-leitplanken.md).
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

## Fristen-Übersicht OWi

| Frist | Rechtsgrundlage | Datum | Erledigt |
|-------|----------------|-------|---------|
| Einspruch | § 67 Abs. 1 OWiG | [Zustellung + 14T] | □ |
| Akteneinsicht | § 49 OWiG | Sofort | □ |
| Wiedereinsetzung (falls noetig) | § 52 OWiG | [Kenntnis + 7T] | □ |
| Rechtsbeschwerde | § 79 Abs. 1 OWiG | [Urteil + 7T] | □ |
| Rechtsbeschwerde-Begruendung | § 79 Abs. 3 OWiG | [Zustellung Urteil + 1M] | □ |
| Fahrverbotswirksamkeit / Verbotsfrist | § 25 Abs. 2, 3 und 6 StVG; anwendbare Fassung prüfen | [Rechtskraft; grundsätzlich spätestens +1M, bei erfülltem Abs. 3 nach Bestimmung bis +4M; Verwahrung/Vermerk und Fristlauf gesondert] | □ |

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
