---
name: kommandocenter
description: "Für Umweltrecht-Kommandocenter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Umweltrecht-Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage-Matrix — welcher Fachmodul?

| Sachverhalt | Fachmodul |
|---|---|
| BImSchG-Genehmigung beantragen oder anfechten | `umweltrecht-immissionsschutz-bimschg` |
| Emissionshandel TEHG, BEHG, DEHSt | `umweltrecht-emissionshandel-tehg` |
| Abfallstatus, KrWG, Nebenprodukt, Circular Economy | `umweltrecht-abfall-circular-economy` |
| Naturschutz, FFH, Artenschutz § 44 BNatSchG | `umweltrecht-naturschutz-artenschutz` |
| Stoerfall-Anlage, 12. BImSchV, Seveso | `umweltrecht-stoerfall-anlagen` |
| Wasser-Erlaubnis, Altlasten, BBodSchG | `umweltrecht-wasser-bodenschutz` |
| M&A-Transaktion, Umwelt-DD, Red Flags | `umweltrecht-transaktionen-dd` |
| UIG/IFG-Informationsantrag, Ablehnung | `umweltrecht-umweltinformation-uig-ifg` |
| VG-Klage, Eilantrag, Beschwerde OVG | `umweltrecht-verfahren` |
| Bussgeld-Bescheid, Anhörung, Sanktionen | `umweltrecht-bussgeld-sanktionen` |
| Compliance, Beauftragte, Schulungsplan | `umweltrecht-compliance-schulung` |
| ESG, CSRD, Greenwashing | `esg-greenwashing-csrd` |
| Klimaklage, Verbandsklage UmwRG | `klimaklagen-verbandsklage-umwrg` |
| Lieferkette, LkSG, CSDDD | `lksg-csddd-lieferkettensorgfalt` |

## Intake-Fragen (für jeden Mandat)

1. **Mandantenrolle**: Betreiber, Investor, Betroffener Dritter, Umweltverband, Behörde?
2. **Rechtsgebiet**: BImSchG, KrWG, WHG, BBodSchG, TEHG, BNatSchG — oder mehrere?
3. **Verfahrensstand**: Noch kein Verfahren / Antragsverfahren laufend / Bescheid ergangen / Klage anhangig?
4. **Fristen akut**: Widerspruch 1 Monat, Klage 1 Monat, Eilantrag unverzueglich — Eingang Bescheid?
5. **Beweismaterial**: Welche Dokumente — Genehmigung, Gutachten, Behördenkorrespondenz, Fotos?
6. **Wirtschaftliches Ziel**: Betrieb sichern, Anlage verhindern, Entschaedigung, Informationszugang, Reputationsschutz?

## Zentrale Querschnitts-Normen Umweltrecht

- **§§ 3-10 BImSchG** — Grundpflichten Emissionsschutz
- **§§ 4 9 10 BBodSchG** — Altlasten-Verantwortung und Sanierung
- **§§ 8 9 10 WHG** — Wasserrechtliche Erlaubnisse
- **§§ 14 15 34 44 BNatSchG** — Eingriff, FFH, Artenschutz
- **§ 2 UmwRG** — Verbandsklage-Befugnis
- **§ 4 UmwRG** — Verfahrensfehler als Aufhebungsgrund
- **§ 80 Abs. 5 VwGO** — Eilrechtsschutz gegen vollziehbare Genehmigung

## Ampelmatrix Risikobewertung (Standard-Output)

| Risiko | Ampel | Fristen | Verantwortlich | Naechste Handlung |
|---|---|---|---|---|
| [THEMA 1] | ROT | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 2] | ORANGE | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 3] | GRUEN | — | [PERSON] | Monitoring |

## Output-Template: Mandatskarte Umweltrecht

**Adressat:** Akte / Interne Notiz — Tonfall: strukturiert, stichwortartig

```
MANDATSKARTE UMWELTRECHT
Stand: [DATUM]
Akte: [AKTENZEICHEN]

MANDANT: [NAME], [ROLLE: Betreiber/Nachbar/Verband]
GEGNER/BEHOERDE: [NAME/STELLE]
ANLAGE: [BEZEICHNUNG], [ORT], [TYP]

RECHTSRAHMEN:
- Hauptnorm: § [X] [GESETZ]
- Nebenrecht: [weitere Normen]

VERFAHRENSSTAND:
- [DATUM]: Genehmigung erteilt / Antrag gestellt / Bescheid erhalten
- [DATUM]: Widerspruch eingelegt / Klage erhoben
- [DATUM]: Naechster Termin [Erörterungstermin / VG / OVG]

FRISTEN:
- [DATUM]: Klagefrist / Einwendungsfrist / TEHG-Abgabe

RISIKEN:
- ROT: [Konkrete Gefahr, z.B. Praeklusion mangels Einwendung]
- ORANGE: [Risiko mit Einschaetzung Wahrscheinlichkeit]

NAECHSTE HANDLUNG:
1. [Konkrete Massnahme, Verantwortlich, Deadline]
2. [Weitere Massnahme]

OFFENE FRAGEN / BENOETIGT:
- [Dokument / Information]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Schnittstellen-Skills

- `fachanwalt-verwaltungsrecht-orientierung` — allgemeine Verwaltungsrechtspruefung
- `energieanlagen-bimschg-genehmigung-verfahren` — Energie-Spezial-BImSchG
- `energietrassen-planfeststellung-rechtsschutz` — Energie-Planfeststellung
- `esg-greenwashing-csrd` — Nachhaltigkeitsberichte
- `klimaklagen-verbandsklage-umwrg` — Klimaklagen

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
