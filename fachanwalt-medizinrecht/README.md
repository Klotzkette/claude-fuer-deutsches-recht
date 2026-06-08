# Fachanwalt Medizinrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-medizinrecht`) | [`fachanwalt-medizinrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-medizinrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Geburtsschaden Helene Meinhardt — Evangelisches Klinikum Bad Salzdetfurth** (`arzthaftung-geburtsschaden-meinhardt-evangelisches-klinikum`) | [Gesamt-PDF lesen](../testakten/arzthaftung-geburtsschaden-meinhardt-evangelisches-klinikum/gesamt-pdf/arzthaftung-geburtsschaden-meinhardt-evangelisches-klinikum_gesamt.pdf) | [`testakte-arzthaftung-geburtsschaden-meinhardt-evangelisches-klinikum.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arzthaftung-geburtsschaden-meinhardt-evangelisches-klinikum.zip) |
| **Mandatsbeziehung Nordstern BioTherapeutics — Kanzlei Falkenried** (`mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech`) | [Gesamt-PDF lesen](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/gesamt-pdf/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech_gesamt.pdf) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip) |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin Fachanwalt für Medizinrecht. Orientierung Arzthaftung §§ 630a ff. BGB Patientenrechte Vertragsarztrecht Berufsrecht Ärzte und Heilberufe SGB V Krankenversicherung MPDG Apothekenrecht. Schnittstellen fachanwalt-sozialrecht und kanzlei-allgemein.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-medizinrecht-orientierung` | Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Arzthaftung §§ 630a ff. BGB (Patientenrechtegesetz seit 2013) Vertragsarztrecht SGB V Berufsrecht Ärzte (Berufsord… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 56 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aerzte-quellenkarte` | Aerzte Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `aerztewerbung-innovative-amnog-millionen` | Aerztewerbung Innovative Amnog Millionen im Medizinrecht: prüft konkret Ärztewerbung innovative Therapie, AMNOG und Millionen-Therapie. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `anaesthesie-hochrisiko-approbation-digitales` | Anaesthesie Hochrisiko Approbation Digitales im Medizinrecht: prüft konkret Anästhesie Hochrisiko-Aufklärung, Approbation und digitales Fehlverhalten, Arztanstellung im MVZ, Assistierter Suizid Beratung. Liefert priorisierten Output mit... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `apothekenrecht-arzneimittel-paragraf-78-amg` | Apothekenrecht Arzneimittel § 78 AMG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `apothekenrecht-interessen-aufklaerung` | Apothekenrecht Interessen Aufklaerung im Medizinrecht: prüft konkret Apothekenrecht, Aufklaerung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `arzthaftung-aufklaerung-bgb` | Arzthaftung und ärztliche Aufklärung nach §§ 630a ff. BGB: Spezial-Skill für Einwilligung, Risikoaufklärung, Dokumentation, Beweislast und prozessuales Vorgehen ohne ungeprüfte Aktenzeichen. |
| `atmp-chain-classification` | Atmp Chain Classification im Medizinrecht: prüft konkret ATMP Chain of Identity, ATMP-Klassifizierung und CAT-Route. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `atmp-pharmakovigilanz-aufklaerungsfehler` | Atmp Pharmakovigilanz Aufklaerungsfehler im Medizinrecht: prüft konkret ATMP-Pharmakovigilanz und RMP, Prüfungslinie für aufklaerungsfehler beweisstrategie, Befundherausgabe, ePA und Akte. Liefert priorisierten Output mit Norm-Pinpoints,... |
| `aufklaerungsfehler-behandlungsfehler` | Aufklaerungsfehler Behandlungsfehler im Medizinrecht: prüft konkrete Prüfungslinie für fachanwalt medizinrecht aufklaerungsfehler, Behandlungsfehler §§ 630a 630h BGB Verletzung medizinischer. Liefert priorisierten Output mit Norm-Pinpoin... |
| `aufklaerungspflicht-paragraf-630e-bgb` | Aufklaerungspflicht § 630e BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `behandlungsfehler-paragraf-630h-bgb` | Behandlungsfehler § 630h BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `berufsrecht-bgb-einwilligung-sonderfall` | Berufsrecht BGB Einwilligung Sonderfall im Medizinrecht: prüft konkret Berufsrecht, BGB, Einwilligung, Fachanwalt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `beweislast-hightech-biobank-consent` | Beweislast Hightech Biobank Consent im Medizinrecht: prüft konkret Beweislast in Hightech-Medizin, Biobank Consent Withdrawal. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `cannabis-medizinisch-combined-atmp-companion` | Cannabis Medizinisch Combined Atmp Companion im Medizinrecht: prüft konkret Medizinisches Cannabis Verordnung, Kombiniertes ATMP mit Medizinprodukt, Companion Diagnostic bei ATMP, Compassionate Use und Härtefall. Liefert priorisierten Ou... |
| `car-t-diga-hersteller` | CAR T Diga Hersteller im Medizinrecht: prüft konkret CAR-T-Behandlung, DiGA. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `crispr-base-cybersecurity-medizinprodukt` | Crispr Base Cybersecurity Medizinprodukt im Medizinrecht: prüft konkret CRISPR/Base-Editing Einwilligung, Cybersecurity Medizinprodukt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `dokumentationsaudit-630f` | Dokumentationsaudit 630f im Medizinrecht: prüft konkret Dokumentationsaudit § 630f, Einwilligungsunfähigkeit und Ablehnung, E-Rezept und Falschmedikation, Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs-. Liefert priorisierten... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `epa-befuellpflicht-impfschaden-arzthaftung` | EPA Befuellpflicht Impfschaden Arzthaftung im Medizinrecht: prüft konkret ePA-Befüllpflicht und Haftung, Impfschaden und Arzthaftung, Checkliste Arzthaftung, Palliativmedizin Haftung. Liefert priorisierten Output mit Norm-Pinpoints, Risi... |
| `experimentelle-behandlung-fachanwalt` | Experimentelle Behandlung Fachanwalt im Medizinrecht: prüft konkret Experimentelle Behandlung Vertrag, Behandlungsvertrag nach §§ 630a-h BGB und Patientenrechte, Honorarstreitigkeiten mit Kassenärztlicher Vereinigung, Vertragsarztrecht.... |
| `fa-medizinrecht-quellen-frist-next` | Rechtsquellen: Quellenprüfung; Fristennotiz und nächster Schritt: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `fa-medizinrecht-start-belegmatrix-fristen` | FA Medizinrecht Start Belegmatrix Fristen im Medizinrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Chronologie und Belegmatrix im Plugin, Fristen- und Risikoampel im Plugin fachanwalt-medizinrecht. Liefert pr... |
| `first-human-geburtshilfe-ctg-gendg-diagnostik` | First Human Geburtshilfe CTG Gendg Diagnostik im Medizinrecht: prüft konkret First-in-Human Risk Board, Geburtshilfe CTG und Sectio, GenDG Diagnostik und Einwilligung, Genomdaten. Liefert priorisierten Output mit Norm-Pinpoints, Risikoam... |
| `gentherapie-dossier-langzeit` | Gentherapie Dossier Langzeit im Medizinrecht: prüft konkret Gentherapie-Dossier und GMP-Kette, Gentherapie Langzeit-Follow-up. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gesundheitsdatenpanne-klinik-goae-analog` | Gesundheitsdatenpanne Klinik Goae Analog im Medizinrecht: prüft konkret Gesundheitsdatenpanne Klinik, GOÄ analog bei Innovation, Grenzüberschreitende Behandlung EU, Hämovigilanz und Blutprodukt. Liefert priorisierten Output mit Norm-Pinp... |
| `gutachterkommission` | Gutachterkommission im Medizinrecht: prüft konkret Gutachterkommissionen und Schlichtungsstellen der, Kassenarztrecht Vertragsarztzulassung und KV-Streitigkeiten, Off-Label-Use und GKV-Erstattungsstreitigkeiten, Orientierung im Medizinre... |
| `hospital-exemption-hta-jca` | Hospital Exemption HTA JCA im Medizinrecht: prüft konkret Hospital Exemption § 4b AMG, EU-HTA/JCA bei ATMP und Onkologie. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `igel-leistungen-paragraf-630c-bgb-bgh-vi-zr-66-15` | IGEL-Leistungen Aufklaerungspflicht Paragraf 630c BGB. |
| `implantateregister-rueckruf-influencer` | Implantateregister Rueckruf Influencer im Medizinrecht: prüft konkret Implantateregister und Rückruf, Influencer Healthcare Werbung, IVDR und Lab Developed Test, Keimbahn-Grenze und Embryonenschutz. Liefert priorisierten Output mit Norm-... |
| `ki-medizinprodukt-klinische-ctr` | KI Medizinprodukt Klinische CTR im Medizinrecht: prüft konkret KI-Medizinprodukt High-Risk, Klinische Prüfung CTR/AMG. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `krankenhaushygiene-mrsa` | Krankenhaushygiene Mrsa: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `krankenhausreform-leistungsgruppen-laborwert` | Krankenhausreform Leistungsgruppen Laborwert im Medizinrecht: prüft konkret Krankenhausreform Leistungsgruppen, Laborwert Alarmpflicht, Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate, Medical Tourism Liability. Liefert prio... |
| `krankenversicherungsrecht-paragraf-13-sgb-v` | Krankenversicherungsrecht § 13 sgb v: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `livecheck-medizinrecht-medr-mpdg` | Livecheck Medizinrecht Medr Mpdg im Medizinrecht: prüft konkret Livecheck, Medizinrecht, Medr, Mpdg. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `medizinischer-eingriff-einwilligung` | Medizinischer Eingriff Einwilligung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `medizinprodukt-haftung-paragraf-1-prodhaftg` | Medizinprodukt Haftung § 1 ProdHaftG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `medr-aufklaerung-einwilligung` | Medr Aufklaerung Einwilligung im Medizinrecht: prüft konkret Leitfaden Aufklaerung und Einwilligung §§ 630d und 630e BGB, Aufklaerung und Einwilligung in der Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächst... |
| `medr-einfuehrung-themen-grundpfeiler-igel` | Medr Einfuehrung Themen Grundpfeiler Igel im Medizinrecht: prüft konkret Medizinrecht einfuehrend, Spezialfall IGeL-Leistungen und Aerztewerbung, Spezialfall IGeL Individuelle Gesundheitsleistung, Spezialfall MVZ-Strukturwandel. Liefert... |
| `mvz-investor-n-therapie-nosokomiale-infektion` | MVZ Investor N Therapie Nosokomiale Infektion im Medizinrecht: prüft konkret Investor-MVZ Compliance, N-of-1-Therapie und Heilversuch, Nosokomiale Infektion und Hygiene, Notaufnahme-Triage. Liefert priorisierten Output mit Norm-Pinpoints... |
| `notfall-mutmassliche-off-label` | Notfall Mutmassliche OFF Label im Medizinrecht: prüft konkret Notfall und mutmaßliche Einwilligung, Off-Label bei seltener Erkrankung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `orphan-atmp-pathologie-probenverwechslung` | Orphan Atmp Pathologie Probenverwechslung im Medizinrecht: prüft konkret Orphan ATMP Zugang, Pathologie Probenverwechslung, Patientenverfügung in der Klinik, Prädiktive Genetik und Familie. Liefert priorisierten Output mit Norm-Pinpoints... |
| `output-waehlen` | Output wählen im Medizinrecht: Diese Output-Weiche für Fachanwalt Medizinrecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `paragraf-95-sgb-v-zulassung` | § 95 sgb v Zulassung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `praenataldiagnostik-nipt-privatklinik` | Praenataldiagnostik Nipt Privatklinik im Medizinrecht: prüft konkret Pränataldiagnostik und NIPT, Privatklinik Paketpreis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `produkthaftung-medizinprodukt-schmerzensgeld` | Produkthaftung Medizinprodukt Schmerzensgeld im Medizinrecht: prüft konkret Produkthaftung Medizinprodukt PLD 2024, Schmerzensgeld bei Hightech-Schaden. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `psychedelika-studie-radiologie-ki` | Psychedelika Studie Radiologie KI im Medizinrecht: prüft konkret Psychedelika Studie und Therapie, Radiologie-KI und Befundfehler, Registerdaten Patientensicherheit, Robotische Operation. Liefert priorisierten Output mit Norm-Pinpoints,... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `sachverstaendiger-innovationsstandard-samd` | Sachverstaendiger Innovationsstandard Samd im Medizinrecht: prüft konkret Sachverständiger und Innovationsstandard, Software as Medical Device Zweckbestimmung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Sch... |
| `schriftsatzkern-substantiierung-sedierung` | Schriftsatzkern Substantiierung Sedierung im Medizinrecht: prüft konkret Substantiierter Schriftsatzkern für Arzthaftungsklage und, Ambulante Sedierung und IGeL, Sepsis-Diagnoseverzug, 630A. Liefert priorisierten Output mit Norm-Pinpoint... |
| `sozialrecht-sprachbarriere-einwilligung` | Sozialrecht Sprachbarriere Einwilligung im Medizinrecht: prüft konkret Sozialrecht, Sprachbarriere Einwilligung, Sterilgut und Medizinprodukt, Transplantation und Allocation. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel u... |
| `stammzellklinik-patientenschaden-telemedizin` | Stammzellklinik Patientenschaden Telemedizin im Medizinrecht: prüft konkret Stammzellklinik und Patientenschaden, Telemedizin Standardhaftung, Approbationswiderruf und Berufsrecht für Aerzte Apotheker, Spezialfall MVZ-Strukturierung. Lie... |
| `tumorboard-onkologiepflicht-unregulierte` | Tumorboard Onkologiepflicht Unregulierte im Medizinrecht: prüft konkret Tumorboard und Onkologiepflicht, Unregulierte Zelltherapie abwehren. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `vektor-shedding-vergleichsverhandlung` | Vektor Shedding Vergleichsverhandlung im Medizinrecht: prüft konkret Vektor-Shedding und Umweltrisiko, Vergleichsverhandlung und Einigungsstrategie im Medizinrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächste... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
