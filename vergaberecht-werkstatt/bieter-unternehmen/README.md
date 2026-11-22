# bieter-unternehmen

<!-- BEGIN plugin-sofort-download-section (autogen) -->
[Öffentliche Startseite](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/README.md) | [Gesamtkatalog](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/SKILLS.md) | [Öffentlicher Skill-Index](../../skills-index/bieter-unternehmen.md) | [Download-Index](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/ASSET_INDEX.md) | [Alle Testakten](../../testakten/README.md) | [Plugin-Dateien](.)

[Repo-Start](../README.md) | [Dateikatalog](../README.md#dateikatalog) | [Downloads](../README.md#sofort-downloads) | [Vergabestelle](../vergabestelle-behoerden/README.md) | [Bieter](../bieter-unternehmen/README.md) | [Konkurrent](../konkurrenten-rechtsschutz/README.md) | [Alle Skills](../SKILLS.md) | [Testakten](../testakten/README.md) | [Rechtsprechung](../references/leitentscheidungen-anker.md)

## Direkt starten

**1. Einmal installieren**

- **Claude Desktop oder Cowork:** [`bieter-unternehmen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/bieter-unternehmen.zip) herunterladen. In `Customize`, `Plugins`, `+` die Funktion zum Hochladen eines eigenen Plugins wählen.
- **Claude Code:**

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install bieter-unternehmen@klotzkette-german-legal-skills
/reload-plugins
```

Die Marketplace-Zeile ist nur beim ersten Plugin nötig. [Offizielle Installationshinweise](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

**2. Fallunterlagen anhängen**

**3. Genau diesen Satz senden**

> Neue Bewerbung. Prüfe die beigefügten Vergabeunterlagen vollständig, sichere Abgabefrist und Ausschlussrisiken und erstelle den nächsten abgabefertigen Angebotsoutput.

Kein zusätzlicher Prompt und keine manuelle Skillwahl sind nötig. Das Plugin antwortet sofort in fünf Zeilen mit `Lage | Rot | Angebot | Rechtsweiche | Jetzt`, verarbeitet den Fall danach selbstständig und stellt am Ende höchstens drei echte Blockerfragen. Bereits sichtbare Angaben werden nicht erneut erfragt.

<details>
<summary><strong>Weitere Prompt- und Skill-Downloads anzeigen</strong></summary>

Die folgenden Dateien sind Alternativen für Chats ohne installiertes Plugin oder für die gezielte Einzelverwendung. `Ansehen` öffnet die Repo-Datei; `Herunterladen` liefert die aktuelle Release-Datei.

| Ziel | Ansehen | Herunterladen |
| --- | --- | --- |
| Werkstatt (Markdown) | [bieter-unternehmen-werkstatt.md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/bieter-unternehmen-werkstatt.md) | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/bieter-unternehmen-werkstatt.md" download="bieter-unternehmen-werkstatt.md">Markdown herunterladen</a> |
| Schnellstart (Markdown) | [bieter-unternehmen-schnellstart.md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/bieter-unternehmen-schnellstart.md) | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/bieter-unternehmen-schnellstart.md" download="bieter-unternehmen-schnellstart.md">Markdown herunterladen</a> |
| Plugin mit Skills, Vorlagen und Referenzen | [Plugin-Dateien](./) | [`bieter-unternehmen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/bieter-unternehmen.zip) |
| Alle Skills dieser Marktrolle | [Skill-Detailseite](../skills-index/bieter-unternehmen.md) | [`bieter-unternehmen-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen-skills-markdown.zip) |
| Autarker Vollworkflow | [Arbeitsprompt](../vergaberecht-arbeitsprompt-bieter.md) | [`vergaberecht-arbeitsprompt-bieter.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-arbeitsprompt-bieter.md) |
| Autarker Kurzprompt mit vertiefter Fallprüfung | [Kurzprompt](../vergaberecht-kurzprompt-bieter.md) | [`vergaberecht-kurzprompt-bieter.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-kurzprompt-bieter.md) |
| Autarker Mini-Schnellstart bis 7.500 Zeichen | [Unified Mini Prompt](../unified-mini-prompts/bieter-unternehmen.md) | [`bieter-unternehmen-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen-unified-mini-prompt.md) |

</details>

<details>
<summary><strong>Demonstrations-Akten anzeigen</strong></summary>

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Aktenübersicht | PDF ansehen | PDF herunterladen | Akten-ZIP | Einzel-PDF-ZIP |
| --- | --- | --- | --- | --- | --- |
| Testakte 03 - Bauleistung Sanierung Stadthalle Musterstadt (Bieterseite) (`03-bauleistung-stadthalle-musterstadt`) | [README](../testakten/03-bauleistung-stadthalle-musterstadt/README.md) | [Gesamt-PDF](../testakten/03-bauleistung-stadthalle-musterstadt/gesamt-pdf/03-bauleistung-stadthalle-musterstadt_gesamt.pdf) | [`03-bauleistung-stadthalle-musterstadt_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/03-bauleistung-stadthalle-musterstadt/gesamt-pdf/03-bauleistung-stadthalle-musterstadt_gesamt.pdf) | [`testakte-03-bauleistung-stadthalle-musterstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-03-bauleistung-stadthalle-musterstadt.zip) | [`testakte-03-bauleistung-stadthalle-musterstadt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-03-bauleistung-stadthalle-musterstadt-einzelpdfs.zip) |
| Testakte 04 - IT-Beratung Ministerium Musterland (Bieterseite, Verhandlungsverfahren) (`04-it-beratung-ministerium-musterland`) | [README](../testakten/04-it-beratung-ministerium-musterland/README.md) | [Gesamt-PDF](../testakten/04-it-beratung-ministerium-musterland/gesamt-pdf/04-it-beratung-ministerium-musterland_gesamt.pdf) | [`04-it-beratung-ministerium-musterland_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/04-it-beratung-ministerium-musterland/gesamt-pdf/04-it-beratung-ministerium-musterland_gesamt.pdf) | [`testakte-04-it-beratung-ministerium-musterland.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-04-it-beratung-ministerium-musterland.zip) | [`testakte-04-it-beratung-ministerium-musterland-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-04-it-beratung-ministerium-musterland-einzelpdfs.zip) |
| Testakte 05: Insolvenz und Auftragnehmerwechsel nach § 132 GWB (`05-insolvenz-auftragnehmerwechsel-132-gwb`) | [README](../testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/README.md) | [Gesamt-PDF](../testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/gesamt-pdf/05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf) | [`05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/gesamt-pdf/05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf) | [`testakte-05-insolvenz-auftragnehmerwechsel-132-gwb.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-05-insolvenz-auftragnehmerwechsel-132-gwb.zip) | [`testakte-05-insolvenz-auftragnehmerwechsel-132-gwb-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-05-insolvenz-auftragnehmerwechsel-132-gwb-einzelpdfs.zip) |
| IT-Sicherheitsvergabe Landeshauptstadt Schwerin - Nachprüfungsverfahren (`it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung`) | [README](../testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/README.md) | [Gesamt-PDF](../testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/gesamt-pdf/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf) | [`it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/gesamt-pdf/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf) | [`testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip) | [`testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung-einzelpdfs.zip) |

</details>

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN output-format-block (autogen) -->

## Output-Format

Alle Skills, Megaprompts und Miniprompts dieses Plugins erzeugen Arbeitsprodukte in Times New Roman, Schriftgrad 11 pt, mit durchgängiger Dezimalgliederung (1, 1.1, 1.1.1, 2, 2.1). Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../references/OUTPUT-FORMAT.md).

<!-- END output-format-block (autogen) -->
Plugin für Unternehmen als Bieter und Bewerber im deutschen und europäischen Vergaberecht. Zielgruppe: Vertriebs- und Angebotsteams, Bid Manager, juristische Inhouse-Funktionen sowie Kanzleien auf Bieter-/Bewerberseite.

## Dashboard-Arbeitsweise

Bei komplexen Vergaben oder Streit startet das Plugin mit einem Bieter-Dashboard: Startbildschirm, Antwortstandard, Schnellwahl, Fristenampel, Dokumentenmatrix, Belegmatrix, Angriffs- und Verteidigungslinien, Wertungsmatrix, Upload-/Formatexport-Check, Akteneinsicht, VK-/OLG-Pfad, Vergleichsfenster, Kostenrisiko und nächster Output. Die Vorlagen liegen unter `assets/templates/startbildschirm-applet-dashboard.md`, `assets/templates/vergabe-master-padlet.md`, `assets/templates/vk-olg-streitdashboard.md` und `assets/templates/ruege-und-vk-powerdraft.md`.

## Ordnerfall ohne Skillwahl

Für neue Vergaben genügt der Unterlagenordner und dieser Satz: `Neue Bewerbung. Prüfe die beigefügten Vergabeunterlagen vollständig, sichere Abgabefrist und Ausschlussrisiken und erstelle den nächsten abgabefertigen Angebotsoutput.` Das Plugin startet selbstständig über `vergabe-os-master-orchestrator`, liest sichtbare Angaben aus, liefert sofort die fünf Zeilen Lage, Rot, Angebot, Rechtsweiche und Jetzt und stellt erst danach höchstens drei echte Blockerfragen gesammelt. Die technischen Skill-Slugs bleiben stabil; ihre Auswahl erfolgt intern.

## Strategie

- Unterlagen maschinenlesbar auswerten: GAEB, XML, Excel, PDF, ZIP und Portalexporte zuerst inventarisieren; LV-Positionen, Pflichtfelder, Fristen, Rügepunkte und Abgabeformate herausziehen.
- Bund-Länder-Wertgrenzen prüfen: Auftraggebertyp, Bundesland, Direktauftrag, erleichtertes Verfahren, Stichtag, Verkündung, Fördermittel und Binnenmarktrelevanz als mögliche Bieterfrage, Rüge oder Nachprüfungsangriff erfassen.
- Livecheck dokumentieren: Vorlage `assets/templates/bund-länder-wertgrenzen-livecheck.md` für Bieterfrage, Rüge oder Nachprüfung verwenden.
- Im verlangten Format liefern: bepreistes LV, Teilnahmeantrag oder Angebot als GAEB/XML/Excel/PDF/ZIP oder Portalformular vorbereiten; native Abgabedateien nur nach Format- und Roundtrip-Prüfung.
- Eignung zuerst prüfen: kein Angebot ohne ESPD-Tauglichkeit, Eigenerklärung, Präqualifikation.
- Form vor Inhalt: formgerechte Abgabe, eSignatur, fristgerechte Einreichung — Verstöße führen regelmäßig zum Ausschluss (§ 57 VgV / § 16 EU VOB/A).
- Rügeobliegenheit nach Paragraf 160 Absatz 3 GWB fallbezogen prüfen: erkannte Verstöße grundsätzlich binnen zehn Kalendertagen; aus Bekanntmachung oder Vergabeunterlagen erkennbare Verstöße spätestens bis zur jeweiligen Bewerbungs- oder Angebotsfrist. Ausnahmen gesondert prüfen.
- Nachprüfungsantrag rechtzeitig vorbereiten: grundsätzlich 15 Kalendertage ab Eingang der Nichtabhilfemitteilung. Der Antrag allein löst die Sperre nach Paragraf 169 Absatz 1 GWB nicht aus; die gesetzlich vorgesehene Unterrichtung des Auftraggebers durch die Vergabekammer ist nachzuweisen.

## Skills

113 Fachmodule in 8 Skills: 30 fachliche Kernmodule in 8 Phasen plus vertiefende Bausteine für Fristen, Quellencheck, Qualitätsvorsprung, Rüge, Nachprüfungsantrag, VK-/OLG-Verfahren, Schadensersatz, Eignung, Datenformate, Legacy-IT, Bundeswehrbeschaffung nach dem BwBBG, Auftragnehmerinsolvenz und IT-Sicherheitsvergaben.

- Phase A (Markterkundung und Strategie): 01-bekanntmachung-lesen, 02-vergabeunterlagen-pruefen, unterlagen-und-lv-datenformate-auslesen, 03-go-no-go-entscheidung
- Phase B (Eignung): 04-eignungsanforderungen-erfassen, 05-espd-ausfuellen, 06-praequalifikation-praequalifizierungsverzeichnis, 07-eignungsleihe-paragraf-47, 08-bietergemeinschaft-bildung
- Phase C (Angebot): 09-angebotskalkulation-stueckpreise, 10-leistungsverzeichnis-bepreisen, 11-nebenangebot-strategie, 12-referenzliste-aufbereiten, 13-konzeptionelle-anlagen, qualitaetsvorsprung-nachweisen, 14-eu-erklaerungen-ausschlussgruende
- Phase D (Abgabe): angebot-in-vorgegebenem-format-erstellen, 15-formgerechte-abgabe-esignatur, 16-frist-und-zustellung-pruefen, 17-bietergemeinschaftserklaerung
- Phase E (Aufklärung): 18-aufklaerung-niedriges-angebot-paragraf-60, 19-aufklaerung-inhalt-paragraf-15
- Phase F (Rüge): 20-ruegefrist-10-tage-paragraf-160, 21-ruegeschreiben-erstellen, 22-nicht-abhilfe-folgeschritt
- Phase G (Nachprüfung): 23-nachpruefungsantrag-paragraf-160, 24-eilantrag-zuschlagssperre-paragraf-169, 25-sofortige-beschwerde-olg-paragraf-171
- Phase H (Vertragsausführung und Querschnitt): 26-zuschlagsannahme-und-vertragsschluss, 27-vertragsanpassung-paragraf-132-gwb, insolvenz-und-132-gwb-auftragnehmerwechsel, 28-selbstreinigung-nach-ausschluss-paragraf-125, 29-schadensersatz-aufhebung-paragraf-181, 30-datenschutz-bieterdaten

## Schnellwahl Ereignisse

- Akte oder Portalexport zuerst ordnen: `dokumente-intake`, `unterlagen-luecken`, `workflow-unterlagen-lueckenliste`.
- LV, GAEB, XML, Excel, PDF oder Unternehmensdaten übernehmen: `unterlagen-und-lv-datenformate-auslesen`, `legacy-systeme-integration`; Angebotsfreeze, Hashliste und Portalquittung mit [`angebotsfreeze-systemuebergabe.md`](assets/templates/angebotsfreeze-systemuebergabe.md) sichern.
- Angebot trotz höherem Preis gewinnen: `qualitaetsvorsprung-nachweisen`, `13-konzeptionelle-anlagen`, `09-angebotskalkulation-stueckpreise`, `angebot-in-vorgegebenem-format-erstellen`.
- Bieterfrage statt sofortiger Rüge: `bieterfragen-antworten-management`; bei bestätigtem Vergabefehler `21-ruegeschreiben-erstellen`.
- Preisblatt, Signatur, Datei oder Angebotsöffnung: `angebotsoeffnung-formfehler-preisblatt`, `18-aufklaerung-niedriges-angebot-paragraf-60`.
- Ausschluss oder Eignungsmangel: `eignungspruefung`, `ausschluss-bieter-paragraf-124-gwb`, `14-eu-erklaerungen-ausschlussgruende`, `28-selbstreinigung-nach-ausschluss-paragraf-125`.
- Nachforderung nach § 56 VgV: `eignung-referenzen-umsatz-nachunternehmer`, `verg-eignungspruefung-leitfaden`, `angebotsoeffnung-formfehler-preisblatt`.
- Bietergemeinschaft, Steuer-/Sozialabgaben oder problematisches Mitglied: `08-bietergemeinschaft-bildung`, `17-bietergemeinschaftserklaerung`, `wettbewerbsregister-abfrage-selbstreinigung`.
- Direktauftrag, fehlende Bekanntmachung oder laufende Leistung: `de-facto-vergabe-135-gwb-fristen`, `de-facto-vergabe-klage`.
- VK-Termin, Vergleich oder Mehrparteienlage: `vergabekammer-termin-simulation`, `vergleichsverhandlung-strategie`, `verg-mehrparteien-konflikt-und-interessen`.

## Anker-Rechtsprechung

Begrenzter Normabgleich am 16.10.2026: [160 GWB](https://www.gesetze-im-internet.de/gwb/__160.html), Absatz 3, und [169 GWB](https://www.gesetze-im-internet.de/gwb/__169.html), Absatz 1, gelesen. Rügefristen nach Kenntnis und Erkennbarkeit trennen; Antragstellung und Sperrbeginn nicht gleichsetzen. Bei Obsiegen des Auftraggebers endet die Sperre nach aktueller Fassung bereits mit Bekanntgabe der Kammerentscheidung; zeitliche Anwendbarkeit und weitere Rechtsschutzwege gesondert prüfen. Keine Vollprüfung der Vergabereform oder neue Verifikation sämtlicher nachfolgender Entscheidungen.

- EuGH 28.10.1999 — C-81/98 "Alcatel Austria" — Vorabinformation.
- EuGH 02.06.2016 — C-27/15 "Pizzo" — keine überraschenden Ausschlussgründe.
- EuGH 16.01.2025 — C-424/23 "DYKA Plastics" — technische Spezifikationen, Produktneutralität und Gleichwertigkeit.
- EuGH 16.04.2026 — C-568/24 "Sof Medica" — Typ-/Systembindung, Unvermeidbarkeit und funktionale Alternative.
- EuGH 03.07.2025 — C-534/23 P und C-539/23 P "Instituto Cervantes" — EU-Eigenvergabe; in deutschen Verfahren Integritätsanker neben § 53 VgV und Portalvorgabe.
- OLG Düsseldorf 10.07.2024 — Verg 2/24 — eigene Anschluss-, Migrations-, Sicherheits- und Gewährleistungslösung gegen Bestandskompatibilität belegen.
- OLG Düsseldorf 13.05.2019 — Verg 47/18; OLG Düsseldorf 12.06.2024 — Verg 36/23 — Unterlagenzugang und substantiierter Indizienvortrag.
- EuGH 04.07.2013 — C-100/12 "Fastweb"; EuGH 05.04.2016 — C-689/13 "PFE"; EuGH 21.12.2021 — C-497/20 "Randstad Italia" — Rechtsschutz trotz Gegenangriff.
- EuGH 22.10.2024 — C-652/22 "Kolin" und EuGH 13.03.2025 — C-266/22 "CRRC Qingdao" — Drittstaatenbieter ohne reziproken Marktzugang.
- EuGH 16.10.2025 — C-282/24 "Polismyndigheten" und EuGH 29.04.2025 — C-452/23 "Fastned Deutschland" — § 132- und Konzessionsänderungen.
- EuGH 24.10.2018 — C-124/17 "Vossloh Laeis" — Selbstreinigung.
- BGH 08.12.2020 — XIII ZR 19/19 — Schadensersatz vergaberechtswidrige Aufhebung.
- OLG-Vergabesenate für 160 Abs. 3 GWB Präklusion (st. Rspr.).

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Ergänzender Werkstatt-Gesamtprompt

Die regulären Plugin-, Arbeits- und Schnellstartdownloads stehen bereits im Schnellzugriff am Seitenanfang. Zusätzlich liegt der ausführliche Werkstatt-Gesamtprompt als einzeln lesbare Markdown-Datei im Repo.

| Datei | Ansehen | Rohdatei |
| --- | --- | --- |
| Werkstatt-Gesamtprompt (125 KB) | [`testakten/megaprompts/bieter-unternehmen.md`](../testakten/megaprompts/bieter-unternehmen.md) | [Raw .md](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/testakten/megaprompts/bieter-unternehmen.md) |

<!-- END megaprompt-und-vorlagen (autogen) -->

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **8 auswählbare Skills**. Die **113 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`vergabe-os-master-orchestrator`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabe-os-master-orchestrator/SKILL.md) |
| 2. Vergabeart und Schwelle | [`vergabeart-und-schwelle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabeart-und-schwelle-bearbeiten/SKILL.md) |
| 3. Vergabeunterlagen | [`vergabeunterlagen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabeunterlagen-bearbeiten/SKILL.md) |
| 4. Rüge | [`ruege-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/ruege-bearbeiten/SKILL.md) |
| 5. Nachpruefung | [`nachpruefung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/nachpruefung-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Der vollständige Katalog enthält 8 Skills. Für die normale Fallbearbeitung genügt der rollenbezogene Startworkflow weiter oben; die Gesamtliste lässt sich bei Bedarf aufklappen.

<details>
<summary><strong>Alle 8 Skills mit Beschreibung und Rohdatei anzeigen</strong></summary>

| Skill | Beschreibung | Rohdatei |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Kontrolliert aus Bietersicht Erklärungen, Berechnungen und Qualitätsnachweise. Prüft Gegenargumente und Freigabegrenzen und vervollständigt das beauftragte Angebots- oder Verhandlungsprodukt. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Erstellt auf Bieterseite ausformulierte Rügeschreiben und Nachprüfungsanträge. Verbindet konkrete Anträge, Verletzung eigener Rechte, Belegstellen, Fristen und rechtliche Begründung. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`nachpruefung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/nachpruefung-bearbeiten/SKILL.md) | Führt den Bieter durch Nachprüfungsverfahren, Zuschlagssperre, Kammertermin und sofortige Beschwerde. Bereitet Beweise, Anträge und Vergleichsoptionen aus seiner eigenen Rechtsposition vor. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/nachpruefung-bearbeiten/SKILL.md) |
| [`ruege-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/ruege-bearbeiten/SKILL.md) | Sichert für Bieter Zugang, Rügefrist und konkrete Beanstandung vor dem Zuschlag. Prüft Nichtabhilfe und den nächsten fristwahrenden Rechtsschutzschritt anhand der tatsächlichen Korrespondenz. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/ruege-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Ordnet die Bieterakte aus Vergabeunterlagen, Portalexport, LV und Unternehmensnachweisen. Klärt Leitdateien, Beweislücken und aktuelle Quellen für Teilnahmeentscheidung, Angebot und Rechtsschutz. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`vergabe-os-master-orchestrator`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabe-os-master-orchestrator/SKILL.md) | Bearbeitet einen Angebotsfall aus Ordner, ZIP oder Portalexport ohne Skillwahl. Verbindet Abgabefrist, Eignung, Wertungslogik und Formatprüfung mit dem fertigen Angebotsschreiben, der Aufklärungsantwort oder Rüge. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabe-os-master-orchestrator/SKILL.md) |
| [`vergabeart-und-schwelle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabeart-und-schwelle-bearbeiten/SKILL.md) | Prüft für Bieter Bekanntmachung, Schwellenwert, Teilnahmefähigkeit und Angebotsstrategie. Ordnet Eignung, Kalkulation, Form und erforderlichen Rechtsschutz dem konkreten Bewerbungsziel zu. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabeart-und-schwelle-bearbeiten/SKILL.md) |
| [`vergabeunterlagen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabeunterlagen-bearbeiten/SKILL.md) | Wertet aus Bietersicht Leistungsverzeichnis, Eignungs- und Vertragsbedingungen aus. Bereitet Bepreisung, Nachweise, Eignungsleihe und zulässige Nebenangebote vor und benennt Ausschlussrisiken. | [Raw .md](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/vergabeunterlagen-bearbeiten/SKILL.md) |

</details>

## Vorlagen, Referenzen und Manifest

Alle mitgelieferten Hilfsdateien sind einzeln erreichbar und zusätzlich im Plugin-ZIP enthalten.

<details>
<summary><strong>Alle 29 Vorlagen, Referenzen und Manifestdateien anzeigen</strong></summary>

| Datei | Ansehen | Rohdatei |
| --- | --- | --- |
| `.claude-plugin/plugin.json` | [Ansehen](.claude-plugin/plugin.json) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/.claude-plugin/plugin.json) |
| `assets/templates/angebotsfreeze-systemuebergabe.md` | [Ansehen](assets/templates/angebotsfreeze-systemuebergabe.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/angebotsfreeze-systemuebergabe.md) |
| `assets/templates/bund-länder-wertgrenzen-livecheck.md` | [Ansehen](assets/templates/bund-länder-wertgrenzen-livecheck.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/bund-länder-wertgrenzen-livecheck.md) |
| `assets/templates/fallkarte-output-weiche.md` | [Ansehen](assets/templates/fallkarte-output-weiche.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/fallkarte-output-weiche.md) |
| `assets/templates/ordnerfall-startprotokoll.md` | [Ansehen](assets/templates/ordnerfall-startprotokoll.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/ordnerfall-startprotokoll.md) |
| `assets/templates/ruege-und-vk-powerdraft.md` | [Ansehen](assets/templates/ruege-und-vk-powerdraft.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/ruege-und-vk-powerdraft.md) |
| `assets/templates/schwellenwert-rechner-2026-2027.md` | [Ansehen](assets/templates/schwellenwert-rechner-2026-2027.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/schwellenwert-rechner-2026-2027.md) |
| `assets/templates/startbildschirm-applet-dashboard.md` | [Ansehen](assets/templates/startbildschirm-applet-dashboard.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/startbildschirm-applet-dashboard.md) |
| `assets/templates/vergabe-master-padlet.md` | [Ansehen](assets/templates/vergabe-master-padlet.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/vergabe-master-padlet.md) |
| `assets/templates/vergabeakte-lueckenliste.md` | [Ansehen](assets/templates/vergabeakte-lueckenliste.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/vergabeakte-lueckenliste.md) |
| `assets/templates/vk-olg-streitdashboard.md` | [Ansehen](assets/templates/vk-olg-streitdashboard.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/vk-olg-streitdashboard.md) |
| `assets/templates/wertungsmatrix-preis-qualitaet.md` | [Ansehen](assets/templates/wertungsmatrix-preis-qualitaet.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/assets/templates/wertungsmatrix-preis-qualitaet.md) |
| `references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md` | [Ansehen](references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md) |
| `references/FORMATE-UND-SCHNITTSTELLEN.md` | [Ansehen](references/FORMATE-UND-SCHNITTSTELLEN.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/FORMATE-UND-SCHNITTSTELLEN.md) |
| `references/INSOLVENZ-132-GWB.md` | [Ansehen](references/INSOLVENZ-132-GWB.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/INSOLVENZ-132-GWB.md) |
| `references/LEGACY-SYSTEME-INTEGRATION.md` | [Ansehen](references/LEGACY-SYSTEME-INTEGRATION.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/LEGACY-SYSTEME-INTEGRATION.md) |
| `references/OUTPUT-FORMAT.md` | [Ansehen](references/OUTPUT-FORMAT.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/OUTPUT-FORMAT.md) |
| `references/QUELLEN-AKTUALITAET.md` | [Ansehen](references/QUELLEN-AKTUALITAET.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/QUELLEN-AKTUALITAET.md) |
| `references/arbeitsoberflaeche-und-visualisierung.md` | [Ansehen](references/arbeitsoberflaeche-und-visualisierung.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/arbeitsoberflaeche-und-visualisierung.md) |
| `references/bundeswehrbeschaffung-bwbbg-2026.md` | [Ansehen](references/bundeswehrbeschaffung-bwbbg-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/bundeswehrbeschaffung-bwbbg-2026.md) |
| `references/hauptworkflow-entscheidungen.md` | [Ansehen](references/hauptworkflow-entscheidungen.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/hauptworkflow-entscheidungen.md) |
| `references/leitentscheidungen-anker.md` | [Ansehen](references/leitentscheidungen-anker.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/leitentscheidungen-anker.md) |
| `references/methodik-vergaberecht.md` | [Ansehen](references/methodik-vergaberecht.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/methodik-vergaberecht.md) |
| `references/netto-null-technologien-vergabe-2026.md` | [Ansehen](references/netto-null-technologien-vergabe-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/netto-null-technologien-vergabe-2026.md) |
| `references/praxisrechtsprechung-vk-2016-2026.md` | [Ansehen](references/praxisrechtsprechung-vk-2016-2026.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/praxisrechtsprechung-vk-2016-2026.md) |
| `references/quellenhygiene.md` | [Ansehen](references/quellenhygiene.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/quellenhygiene.md) |
| `references/veroeffentlichungswege.md` | [Ansehen](references/veroeffentlichungswege.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/veroeffentlichungswege.md) |
| `references/zitierweise.md` | [Ansehen](references/zitierweise.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/zitierweise.md) |
| `references/zuschlag-nicht-nur-preis.md` | [Ansehen](references/zuschlag-nicht-nur-preis.md) | [Raw](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vergaberecht-werkstatt/bieter-unternehmen/references/zuschlag-nicht-nur-preis.md) |

</details>

<!-- END SKILLS-OVERVIEW (auto-generated) -->
