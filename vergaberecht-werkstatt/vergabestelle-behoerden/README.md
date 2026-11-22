# vergabestelle-behoerden

Für öffentliche Auftraggeber: Vergabeunterlagen und Angebote prüfen, Rügen bearbeiten und den beauftragten Vergabevermerk, die Bieterantwort oder Zuschlagsentscheidung ausarbeiten. Vorhandene Unterlagen bestimmen Rechtsregime und nächsten Fachschritt; nur entscheidende Lücken werden nachgefragt.

<!-- BEGIN plugin-sofort-download-section (autogen) -->
[Öffentliche Startseite](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/README.md) | [Gesamtkatalog](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/SKILLS.md) | [Öffentlicher Skill-Index](../../skills-index/vergabestelle-behoerden.md) | [Download-Index](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/ASSET_INDEX.md) | [Alle Testakten](../../testakten/README.md) | [Plugin-Dateien](.)

[Repo-Start](../README.md) | [Dateikatalog](../README.md#dateikatalog) | [Downloads](../README.md#sofort-downloads) | [Vergabestelle](../vergabestelle-behoerden/README.md) | [Bieter](../bieter-unternehmen/README.md) | [Konkurrent](../konkurrenten-rechtsschutz/README.md) | [Alle Skills](../SKILLS.md) | [Testakten](../testakten/README.md) | [Rechtsprechung](../references/leitentscheidungen-anker.md)

## Direkt starten

**1. Einmal installieren**

- **Claude Desktop oder Cowork:** [`vergabestelle-behoerden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/vergabestelle-behoerden.zip) herunterladen. In `Customize`, `Plugins`, `+` die Funktion zum Hochladen eines eigenen Plugins wählen.
- **Claude Code:**

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install vergabestelle-behoerden@klotzkette-german-legal-skills
/reload-plugins
```

Die Marketplace-Zeile ist nur beim ersten Plugin nötig. [Offizielle Installationshinweise](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

**2. Fallunterlagen anhängen**

**3. Genau diesen Satz senden**

> Neuer Vergabestellenfall. Prüfe die beigefügten Unterlagen vollständig, sichere Fristen und Rechtsregime und erstelle den nächsten entscheidungsreifen Behördenoutput.

Kein zusätzlicher Prompt und keine manuelle Skillwahl sind nötig. Das Plugin bearbeitet den Auftrag eigenständig. Bei einem offenen Ordnerauftrag kann es mit `Lage | Rot | Akte | Rechtsweiche | Jetzt` orientieren. Ist ein bestimmtes Dokument bestellt, beginnt es nach der Unterlagensichtung unmittelbar damit. Pro Rückfragerunde werden höchstens drei echte, entscheidende Lücken gebündelt erfragt; bereits sichtbare Angaben werden nicht erneut erfragt. Antworten werden im selben Entwurf verarbeitet. Weitere Rückfragen folgen nur bei neuen entscheidenden Lücken, bis das bestellte Dokument vorliegt.

<details>
<summary><strong>Weitere Prompt- und Skill-Downloads anzeigen</strong></summary>

Die folgenden Dateien sind Alternativen für Chats ohne installiertes Plugin oder für die gezielte Einzelverwendung. `Ansehen` öffnet die Repo-Datei; `Herunterladen` liefert die aktuelle Release-Datei.

| Ziel | Ansehen | Herunterladen |
| --- | --- | --- |
| Werkstatt (Markdown) | [vergabestelle-behoerden-werkstatt.md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/vergabestelle-behoerden-werkstatt.md) | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/vergabestelle-behoerden-werkstatt.md" download="vergabestelle-behoerden-werkstatt.md">Markdown herunterladen</a> |
| Schnellstart (Markdown) | [vergabestelle-behoerden-schnellstart.md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/vergabestelle-behoerden-schnellstart.md) | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/vergabestelle-behoerden-schnellstart.md" download="vergabestelle-behoerden-schnellstart.md">Markdown herunterladen</a> |
| Plugin mit Skills, Vorlagen und Referenzen | [Plugin-Dateien](./) | [`vergabestelle-behoerden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/vergabestelle-behoerden.zip) |
| Alle Skills dieser Marktrolle | [Skill-Detailseite](../skills-index/vergabestelle-behoerden.md) | [`vergabestelle-behoerden-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden-skills-markdown.zip) |
| Autarker Vollworkflow | [Arbeitsprompt](../vergaberecht-arbeitsprompt-vergabestelle.md) | [`vergaberecht-arbeitsprompt-vergabestelle.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-arbeitsprompt-vergabestelle.md) |
| Autarker Kurzprompt mit vertiefter Fallprüfung | [Kurzprompt](../vergaberecht-kurzprompt-vergabestelle.md) | [`vergaberecht-kurzprompt-vergabestelle.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-kurzprompt-vergabestelle.md) |
| Autarker Mini-Schnellstart bis 7.500 Zeichen | [Unified Mini Prompt](../unified-mini-prompts/vergabestelle-behoerden.md) | [`vergabestelle-behoerden-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden-unified-mini-prompt.md) |

</details>

<details>
<summary><strong>Demonstrations-Akten anzeigen</strong></summary>

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Aktenübersicht | PDF ansehen | PDF herunterladen | Akten-ZIP | Einzel-PDF-ZIP |
| --- | --- | --- | --- | --- | --- |
| Testakte 01 - Reinigungsdienstleistung Grundschule Musterstadt (`01-reinigung-grundschule-musterstadt`) | [README](../testakten/01-reinigung-grundschule-musterstadt/README.md) | [Gesamt-PDF](../testakten/01-reinigung-grundschule-musterstadt/gesamt-pdf/01-reinigung-grundschule-musterstadt_gesamt.pdf) | [`01-reinigung-grundschule-musterstadt_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/01-reinigung-grundschule-musterstadt/gesamt-pdf/01-reinigung-grundschule-musterstadt_gesamt.pdf) | [`testakte-01-reinigung-grundschule-musterstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-01-reinigung-grundschule-musterstadt.zip) | [`testakte-01-reinigung-grundschule-musterstadt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-01-reinigung-grundschule-musterstadt-einzelpdfs.zip) |
| Testakte 02 - Laptopbeschaffung Landesamt Musterland (`02-laptopbeschaffung-landesamt-musterland`) | [README](../testakten/02-laptopbeschaffung-landesamt-musterland/README.md) | [Gesamt-PDF](../testakten/02-laptopbeschaffung-landesamt-musterland/gesamt-pdf/02-laptopbeschaffung-landesamt-musterland_gesamt.pdf) | [`02-laptopbeschaffung-landesamt-musterland_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/02-laptopbeschaffung-landesamt-musterland/gesamt-pdf/02-laptopbeschaffung-landesamt-musterland_gesamt.pdf) | [`testakte-02-laptopbeschaffung-landesamt-musterland.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-02-laptopbeschaffung-landesamt-musterland.zip) | [`testakte-02-laptopbeschaffung-landesamt-musterland-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-02-laptopbeschaffung-landesamt-musterland-einzelpdfs.zip) |
| Testakte 05: Insolvenz und Auftragnehmerwechsel nach § 132 GWB (`05-insolvenz-auftragnehmerwechsel-132-gwb`) | [README](../testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/README.md) | [Gesamt-PDF](../testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/gesamt-pdf/05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf) | [`05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/gesamt-pdf/05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf) | [`testakte-05-insolvenz-auftragnehmerwechsel-132-gwb.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-05-insolvenz-auftragnehmerwechsel-132-gwb.zip) | [`testakte-05-insolvenz-auftragnehmerwechsel-132-gwb-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-05-insolvenz-auftragnehmerwechsel-132-gwb-einzelpdfs.zip) |
| IT-Sicherheitsvergabe Landeshauptstadt Schwerin - Nachprüfungsverfahren (`it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung`) | [README](../testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/README.md) | [Gesamt-PDF](../testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/gesamt-pdf/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf) | [`it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/gesamt-pdf/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf) | [`testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip) | [`testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung-einzelpdfs.zip) |

</details>

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN output-format-block (autogen) -->

## Output-Format

Alle Skills, Megaprompts und Miniprompts dieses Plugins erzeugen Arbeitsprodukte in Times New Roman, Schriftgrad 11 pt, mit durchgängiger Dezimalgliederung (1, 1.1, 1.1.1, 2, 2.1). Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../references/OUTPUT-FORMAT.md).

<!-- END output-format-block (autogen) -->
Plugin für öffentliche Auftraggeber im deutschen und europäischen Vergaberecht. Zielgruppe: Vergabestellen in Bund, Ländern, Kommunen, Sektorenbereichen und anderen öffentlich-rechtlichen Auftraggebern.

## Dashboard-Arbeitsweise

Bei komplexen Vergaben oder Rügen startet das Plugin mit einem Vergabestellen-Dashboard: Startbildschirm, Antwortstandard, Schnellwahl, Fristenampel, Dokumentenmatrix, Belegmatrix, Angriff und Verteidigung, Wertungsmatrix, Upload-/Formatexport-Check, Akteneinsicht/Schwärzung, VK-/OLG-Pfad, Vergleichsfenster und nächster Behördenoutput. Die Vorlagen liegen unter `assets/templates/startbildschirm-applet-dashboard.md`, `assets/templates/vergabe-master-padlet.md`, `assets/templates/vk-olg-streitdashboard.md` und `assets/templates/ruege-und-vk-powerdraft.md`.

## Ordnerfall ohne Skillwahl

Für neue Verfahren genügt der Fallordner und dieser Satz: `Neuer Vergabestellenfall. Prüfe die beigefügten Unterlagen vollständig, sichere Fristen und Rechtsregime und erstelle den nächsten entscheidungsreifen Behördenoutput.` Das Plugin startet über `vergabe-os-master-orchestrator` und wertet die Unterlagen aus. Ein kurzer Lageüberblick hilft bei offenem Auftrag, ist aber keine Pflichtvorstufe eines bereits bestellten Dokuments. Neue Antworten führen zur gezielten Fortsetzung bis zum Entwurf; nur für externe Handlungen bleibt eine ausdrückliche Freigabe erforderlich.

## Rechtsregime

- Oberhalb EU-Schwellenwert: GWB Teil 4 (§§ 97 ff.), VgV / SektVO / KonzVgV / VSVgV. Nachprüfung vor Vergabekammer und OLG.
- Unterhalb EU-Schwellenwert: BHO/LHO § 55, UVgO (Bund) und landesrechtliche Vergaberegeln. Kein GWB-Nachprüfungsautomatismus; landesrechtliche Prüfstellen, Informations- und Wartepflichten, gerichtlicher Eilrechtsschutz, Aufsicht, Fördermittelkontrolle und Schadensersatz fallbezogen prüfen.
- Bauleistungen: VOB/A Abschnitt 1 für die Unterschwelle nach anwendbarem Haushaltsrecht, Abschnitt 2 für den allgemeinen Oberschwellenbereich und Abschnitt 3 für verteidigungs- oder sicherheitsspezifische Bauaufträge nach Paragraf 2 Absatz 2 VSVgV. Sektorenbeschaffungen nach Paragraf 1 SektVO sind nicht mit VOB/A Abschnitt 3 gleichzusetzen.
- Bund-Länder-Reform 2026: Vergabebeschleunigungsgesetz, Direktauftragsgrenzen, Landeswertgrenzen, Verkündung, Stichtag, Fördermittel, Binnenmarktrelevanz und kommunale Satzung vor jeder Unterschwellenentscheidung live prüfen.

## Skills

122 Fachmodule in 8 Skills: 30 fachliche Kernmodule in 8 Phasen plus vertiefende Bausteine für Fristen, Quellencheck, Vergabeakte, Datenformate, Wirklichkeitsdaten, Legacy-IT, Auftragnehmerinsolvenz, IT-Sicherheit, Bundeswehrbeschaffung nach dem BwBBG, Sektoren/Konzessionen, Rügeabwehr, Bestangebots-Durchsetzung und VK-/OLG-Verfahren.

- Phase A (Bedarfsermittlung und Schätzung): 01-bedarfsermittlung, 02-auftragswert-schaetzung, 03-schwellenwert-pruefung
- Phase B (Verfahrenswahl): 04-verfahrensart-waehlen, 05-bekanntmachung-erstellen, bekanntmachung-berichtigung-und-upload-routing, 06-eignungs-und-zuschlagskriterien
- Phase C (Unterlagen): 07-vergabeunterlagen-erstellen, vergabeunterlagen-lv-datenformate-bereitstellen, 08-leistungsbeschreibung, 09-eignungsformular-espd, 10-zuschlagsmatrix-aufbauen, bestangebot-durchsetzen
- Phase D (Verfahrensdurchführung): 11-eignungspruefung, 12-ausschlussgruende-pruefen, 13-angebotsoeffnung-protokoll, 14-aufklaerung-unangemessen-niedrige-preise
- Phase E (Wertung): 15-rechnerische-pruefung, 16-formelle-pruefung, 17-wertung-leistung-preis, 18-wertungsvermerk-erstellen
- Phase F (Zuschlag): 19-vorabinformation-paragraf-134, 20-zuschlagserteilung, 21-aufhebung-rechtssicher
- Phase G (Nachprüfung): 22-ruegeerwiderung, 23-stellungnahme-vergabekammer, 24-vorlage-an-den-vergabesenat
- Phase H (Dokumentation und Querschnitt): 25-vergabevermerk-paragraf-8-vgv, 26-akteneinsicht-vergabekammer, 27-selbstreinigung-paragraf-125, 28-vergabesperre, 29-ev-vorabinformation-frist, 30-datenschutz-bieterdaten, insolvenz-und-132-gwb-auftragnehmerwechsel

## Schnellwahl Spezialfälle

- Datensilos und Wirklichkeitsdaten: `legacy-systeme-integration`, danach `wirklichkeitsdaten-beschaffung-steuern` für Feldautorität, Entscheidungsbrücke, Szenario, LV, Kriterien, Aktenvermerk und Rückkanal. Arbeitsblatt: [`systemuebergabe-entscheidungsdaten.md`](assets/templates/systemuebergabe-entscheidungsdaten.md).
- Bestes Angebot statt billigstes Angebot: `bestangebot-durchsetzen`, `10-zuschlagsmatrix-aufbauen`, `17-wertung-leistung-preis`, `18-wertungsvermerk-erstellen`.
- Bieterfrage, Rüge, VK und OLG: `bieterfragen-antworten-management`, `22-ruegeerwiderung`, `23-stellungnahme-vergabekammer`, `26-akteneinsicht-vergabekammer`, `24-vorlage-an-den-vergabesenat`.
- Vorbereitung und Beschaffungsstruktur: `markterkundung-und-vorbefassung`, `losbildung-mittelstandsfoerderung`, `rahmenvereinbarung-abrufe-mini-wettbewerb`, `inhouse-interkommunal`.
- Sonderregime: `uvgo-unterschwellenvergabe`, `sektorenvergabe-sektvo`, `konzessionsvergabe-konzvgv`, `vob-a-bauvergabe`, `foerdermittelvergabe-rueckforderung`.
- Compliance, Cloud und Nachhaltigkeit: `wettbewerbsregister-abfrage-selbstreinigung`, `vergaberecht-anti-korruption-paragraf-123-gwb`, `ki-beschaffung-ai-act-daten-cloud`, `nachhaltigkeit-tariftreue-lksg-cbam`, `30-datenschutz-bieterdaten`.

## Datenformate und Veröffentlichung

- GAEB/XML/Excel/PDF/ZIP vor Bereitstellung aus Vergabestellensicht prüfen: verbindliches Format, Lesefassung, Rückgabeformat, Pflichtfelder, Dateinamen und Version.
- Bei Direktauftrag oder erleichtertem Verfahren den Bundesland-Wertgrenzencheck aus `references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md` mit Quelle, Datum und Auftraggebertyp in die Vergabeakte aufnehmen.
- Für die Akte die Vorlage `assets/templates/bund-länder-wertgrenzen-livecheck.md` nutzen.
- Bei berechtigten Einwänden zu Unterlagen, LV, Preisblatt, Bekanntmachung oder Portalfehlern sofort Berichtigung, Fristverlängerung, neue Unterlagenversion oder Aufhebung prüfen.
- Für TED/eForms, DVAL, bund.de, Landesportal oder E-Vergabe-System immer Feldliste, Uploadauftrag, Freigabecheck und Nachweis in der Vergabeakte führen.
- Systemquellen nie pauschal als Wahrheit übernehmen: SIB-/PMS-/BIM-, SAP-, AVA-, Kosten-, Portal- und Umweltdaten werden je Feld mit Originalschlüssel, Stichtag, Einheit, Transformation, Fachfreigabe und zulässigem Rechtszweck geführt.
- Historische Anbieterleistung oder Behördenfeedback nicht als verdecktes Eignungs- oder Zuschlagskriterium verwenden.

## Anker-Rechtsprechung

- EuGH 28.10.1999 — C-81/98 "Alcatel Austria" — Vorabinformationspflicht.
- EuGH 18.10.2001 — C-19/00 "SIAC Construction" — Transparenz.
- EuGH 09.01.2025 — C-578/23 "Generální finanční ředitelství" — Verfahren ohne vorherige Bekanntmachung und Lock-in.
- EuGH 16.01.2025 — C-424/23 "DYKA Plastics" — technische Spezifikationen, Produktneutralität und Gleichwertigkeit.
- EuGH 16.04.2026 — C-568/24 "Sof Medica" — detaillierte Typ-/Systemvorgaben, Unvermeidbarkeit und Gleichwertigkeitszusatz.
- EuGH 03.07.2025 — C-534/23 P und C-539/23 P "Instituto Cervantes" — EU-Eigenvergabe; in deutschen Verfahren Integritätsanker neben § 53 VgV und Portalvorgabe.
- OLG Düsseldorf 10.07.2024 — Verg 2/24 — Bestandskompatibilität, Systemsicherheit und konkrete Lock-in-Begründung.
- OLG Düsseldorf 13.05.2019 — Verg 47/18; OLG Düsseldorf 24.03.2021 — Verg 34/20 — direkter Unterlagenzugang und begründete statt bloß berechnete Wertung.
- EuGH 18.12.2025 — C-769/23 "Mara" — nationale Beschränkung der Preis-allein-Wertung unionsrechtlich zulässig; kein allgemeines Nur-Preis-Verbot.
- EuGH 16.10.2025 — C-282/24 "Polismyndigheten" — Änderung einer Rahmenvereinbarung.
- EuGH 29.04.2025 — C-452/23 "Fastned Deutschland" — Konzession und spätere Änderung.
- BGH 31.01.2017 — X ZB 10/16 — Aufklärung niedriger Angebote.
- BGH 08.12.2020 — XIII ZR 19/19 — Schadensersatz bei rechtswidriger Aufhebung.
- BVerfG 13.06.2006 — 1 BvR 1160/03 — Unterschwellenrechtsschutz.

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Ergänzender Werkstatt-Gesamtprompt

Die regulären Plugin-, Arbeits- und Schnellstartdownloads stehen bereits im Schnellzugriff am Seitenanfang. Zusätzlich liegt der ausführliche Werkstatt-Gesamtprompt als einzeln lesbare Markdown-Datei im Repo.

| Datei | Ansehen | Rohdatei |
| --- | --- | --- |
| Werkstatt-Gesamtprompt (133 KB) | [`testakten/megaprompts/vergabestelle-behoerden.md`](../testakten/megaprompts/vergabestelle-behoerden.md) | [Raw .md](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/megaprompts/vergabestelle-behoerden.md) |

<!-- END megaprompt-und-vorlagen (autogen) -->

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **8 auswählbare Skills**. Die **122 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`vergabe-os-master-orchestrator`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabe-os-master-orchestrator/SKILL.md) |
| 2. Vergabeart und Schwelle | [`vergabeart-und-schwelle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabeart-und-schwelle-bearbeiten/SKILL.md) |
| 3. Vergabeunterlagen | [`vergabeunterlagen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabeunterlagen-bearbeiten/SKILL.md) |
| 4. Rüge | [`ruege-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/ruege-bearbeiten/SKILL.md) |
| 5. Nachpruefung | [`nachpruefung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/nachpruefung-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Der vollständige Katalog enthält 8 Skills. Für die normale Fallbearbeitung genügt der rollenbezogene Startworkflow weiter oben; die Gesamtliste lässt sich bei Bedarf aufklappen.

<details>
<summary><strong>Alle 8 Skills mit Beschreibung und Rohdatei anzeigen</strong></summary>

| Skill | Beschreibung | Rohdatei |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Prüft den Behördenentwurf auf Zahlenfehler, fehlende Belege und angreifbare Wertungen. Bearbeitet Gegenargumente und dokumentiert offene Freigaben für ein entscheidungsreifes Vergabeprodukt. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Erstellt für die Vergabestelle Wertungsmatrix und Wertungsvermerk aus den festgelegten Preis- und Qualitätskriterien. Dokumentiert Ergebnisse, Belegstellen und offene Aufklärung vor der Zuschlagsentscheidung. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`nachpruefung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/nachpruefung-bearbeiten/SKILL.md) | Verteidigt und überprüft Auftraggeberentscheidungen bei Rüge, Vergabekammer und Vergabesenat. Verbindet Wertung, Vergabeakte, Akteneinsicht und begründete Stellungnahme mit möglichen Abhilfeschritten. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/nachpruefung-bearbeiten/SKILL.md) |
| [`ruege-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/ruege-bearbeiten/SKILL.md) | Bereitet für öffentliche Auftraggeber Bekanntmachungsberichtigung, Portalbereitstellung und Vorabinformation vor. Sichert Zugang und Stillhaltefrist, bevor die Vergabestelle auf den Zuschlag zusteuert. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/ruege-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Ordnet die Behördenakte, Quellen, Bieterfragen und Aufklärungsunterlagen. Sichert Datenherkunft, Nachforderung, Losbildung und Besonderheiten des Unterschwellenrechts für die Vergabestelle. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`vergabe-os-master-orchestrator`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabe-os-master-orchestrator/SKILL.md) | Übernimmt Vergabeakten als Ordner, ZIP oder Portalexport ohne Skillwahl. Führt die Vergabestelle von Bedarf und Verfahrensstand über Regime. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabe-os-master-orchestrator/SKILL.md) |
| [`vergabeart-und-schwelle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabeart-und-schwelle-bearbeiten/SKILL.md) | Plant für öffentliche Auftraggeber Bedarf, Auftragswert, Lose und Vergabeart. Ordnet Sonderregime, Bekanntmachung, Angebotsprüfung und Zuschlagsvorbereitung dem konkreten Beschaffungsverfahren zu. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabeart-und-schwelle-bearbeiten/SKILL.md) |
| [`vergabeunterlagen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabeunterlagen-bearbeiten/SKILL.md) | Erstellt für Vergabestellen neutrale Leistungsbeschreibungen, Eignungs- und Zuschlagskriterien sowie Vergabeunterlagen. Sichert Wertungslogik, vorgegebene Datenformate und dokumentierte Vertragsänderungen. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/vergabeunterlagen-bearbeiten/SKILL.md) |

</details>

## Vorlagen, Referenzen und Manifest

Alle mitgelieferten Hilfsdateien sind einzeln erreichbar und zusätzlich im Plugin-ZIP enthalten.

<details>
<summary><strong>Alle 31 Vorlagen, Referenzen und Manifestdateien anzeigen</strong></summary>

| Datei | Ansehen | Rohdatei |
| --- | --- | --- |
| `.claude-plugin/plugin.json` | [Ansehen](.claude-plugin/plugin.json) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/.claude-plugin/plugin.json) |
| `assets/templates/bund-länder-wertgrenzen-livecheck.md` | [Ansehen](assets/templates/bund-länder-wertgrenzen-livecheck.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/bund-länder-wertgrenzen-livecheck.md) |
| `assets/templates/fallkarte-output-weiche.md` | [Ansehen](assets/templates/fallkarte-output-weiche.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/fallkarte-output-weiche.md) |
| `assets/templates/ordnerfall-startprotokoll.md` | [Ansehen](assets/templates/ordnerfall-startprotokoll.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/ordnerfall-startprotokoll.md) |
| `assets/templates/ruege-und-vk-powerdraft.md` | [Ansehen](assets/templates/ruege-und-vk-powerdraft.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/ruege-und-vk-powerdraft.md) |
| `assets/templates/schwellenwert-rechner-2026-2027.md` | [Ansehen](assets/templates/schwellenwert-rechner-2026-2027.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/schwellenwert-rechner-2026-2027.md) |
| `assets/templates/startbildschirm-applet-dashboard.md` | [Ansehen](assets/templates/startbildschirm-applet-dashboard.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/startbildschirm-applet-dashboard.md) |
| `assets/templates/systemuebergabe-entscheidungsdaten.md` | [Ansehen](assets/templates/systemuebergabe-entscheidungsdaten.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/systemuebergabe-entscheidungsdaten.md) |
| `assets/templates/vergabe-master-padlet.md` | [Ansehen](assets/templates/vergabe-master-padlet.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/vergabe-master-padlet.md) |
| `assets/templates/vergabeakte-lueckenliste.md` | [Ansehen](assets/templates/vergabeakte-lueckenliste.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/vergabeakte-lueckenliste.md) |
| `assets/templates/vk-olg-streitdashboard.md` | [Ansehen](assets/templates/vk-olg-streitdashboard.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/vk-olg-streitdashboard.md) |
| `assets/templates/wertungsmatrix-preis-qualitaet.md` | [Ansehen](assets/templates/wertungsmatrix-preis-qualitaet.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/assets/templates/wertungsmatrix-preis-qualitaet.md) |
| `references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md` | [Ansehen](references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md) |
| `references/FORMATE-UND-SCHNITTSTELLEN.md` | [Ansehen](references/FORMATE-UND-SCHNITTSTELLEN.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/FORMATE-UND-SCHNITTSTELLEN.md) |
| `references/INSOLVENZ-132-GWB.md` | [Ansehen](references/INSOLVENZ-132-GWB.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/INSOLVENZ-132-GWB.md) |
| `references/LEGACY-SYSTEME-INTEGRATION.md` | [Ansehen](references/LEGACY-SYSTEME-INTEGRATION.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/LEGACY-SYSTEME-INTEGRATION.md) |
| `references/OUTPUT-FORMAT.md` | [Ansehen](references/OUTPUT-FORMAT.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/OUTPUT-FORMAT.md) |
| `references/QUELLEN-AKTUALITAET.md` | [Ansehen](references/QUELLEN-AKTUALITAET.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/QUELLEN-AKTUALITAET.md) |
| `references/WIRKLICHKEITSDATEN-BESCHAFFUNGSSTEUERUNG.md` | [Ansehen](references/WIRKLICHKEITSDATEN-BESCHAFFUNGSSTEUERUNG.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/WIRKLICHKEITSDATEN-BESCHAFFUNGSSTEUERUNG.md) |
| `references/arbeitsoberflaeche-und-visualisierung.md` | [Ansehen](references/arbeitsoberflaeche-und-visualisierung.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/arbeitsoberflaeche-und-visualisierung.md) |
| `references/bundeswehrbeschaffung-bwbbg-2026.md` | [Ansehen](references/bundeswehrbeschaffung-bwbbg-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/bundeswehrbeschaffung-bwbbg-2026.md) |
| `references/ki-normen-und-fallpruefung.md` | [Ansehen](references/ki-normen-und-fallpruefung.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/ki-normen-und-fallpruefung.md) |
| `references/hauptworkflow-entscheidungen.md` | [Ansehen](references/hauptworkflow-entscheidungen.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/hauptworkflow-entscheidungen.md) |
| `references/leitentscheidungen-anker.md` | [Ansehen](references/leitentscheidungen-anker.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/leitentscheidungen-anker.md) |
| `references/methodik-vergaberecht.md` | [Ansehen](references/methodik-vergaberecht.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/methodik-vergaberecht.md) |
| `references/netto-null-technologien-vergabe-2026.md` | [Ansehen](references/netto-null-technologien-vergabe-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/netto-null-technologien-vergabe-2026.md) |
| `references/praxisrechtsprechung-vk-2016-2026.md` | [Ansehen](references/praxisrechtsprechung-vk-2016-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/praxisrechtsprechung-vk-2016-2026.md) |
| `references/quellenhygiene.md` | [Ansehen](references/quellenhygiene.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/quellenhygiene.md) |
| `references/veroeffentlichungswege.md` | [Ansehen](references/veroeffentlichungswege.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/veroeffentlichungswege.md) |
| `references/zitierweise.md` | [Ansehen](references/zitierweise.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/zitierweise.md) |
| `references/zuschlag-nicht-nur-preis.md` | [Ansehen](references/zuschlag-nicht-nur-preis.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/vergabestelle-behoerden/references/zuschlag-nicht-nur-preis.md) |

</details>

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Lassen Sie Bieter Systemzweck, Version und konkrete Nachweise beschreiben. Ein Zertifikatsname oder allgemeines Risikokonzept ersetzt keinen überprüfbaren Leistungs- und Testgegenstand.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
