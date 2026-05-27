---
name: verkehrsowi-aktenanlage
description: "Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bussgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bussgeldbescheid), § 67 OWiG (Einspruch). Pruefraster: Bussgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverzeichnis (Messgeraet, Eichschein). Output Aktenstruktur, Fristen-Uebersicht-Tabelle, Beweismittelverzeichnis. Abgrenzung: Akteneinsicht Messakte siehe verkehrsowi-akteneinsicht-messakte; Einspruchsfrist siehe verkehrsowi-fristen-einspruch."
---

# Aktenanlage OWi-Mandat

## Triage zu Beginn

1. **Vollmacht vorhanden?** — Ohne Vollmacht keine Akteneinsicht.
2. **Zustellungsdatum des Bescheids dokumentiert?** — Fristbeginn.
3. **Aktenzeichen und Delikt notiert?** — Grundlage fuer Schriftsaetze.
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
   - Verjaehrungs-Check

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
