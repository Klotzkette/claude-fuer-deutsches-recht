# Fachanwalt Medizinrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`fachanwalt-medizinrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/fachanwalt-medizinrecht.md) (52 KB)
- Im Repo: [`testakten/megaprompts/fachanwalt-medizinrecht.md`](../testakten/megaprompts/fachanwalt-medizinrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Befundherausgabe Paragraf 630G Bgb | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-medizinrecht/befundherausgabe-paragraf-630g-bgb.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-medizinrecht/befundherausgabe-paragraf-630g-bgb.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich prüfen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->

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

## Anwalts-Dashboard für den Schnelleinstieg

Der Skill `einstieg-routing` ist das Anwalts-Dashboard zu diesem Plugin:
Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch,
Zustaendigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs,
Norm-Radar, Leitentscheidungs-Anker und genau eine Rueckfrage - bei
klarer Faktenlage sofort zum Spezial-Skill. Der Anwalt bleibt im Driver Seat.

Konvention: [`references/anwalts-dashboard-konvention.md`](../references/anwalts-dashboard-konvention.md)
| Quellen-Anker: [`references/leitentscheidungen-anker.md`](../references/leitentscheidungen-anker.md)
| Quellenhygiene: [`references/quellenhygiene.md`](../references/quellenhygiene.md).


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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 146 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `630a-dokumentenmatrix-und-lueckenliste` | 630A: Dokumentenmatrix, Lückenliste und Nachforderung: 630A: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `aerzte-quellenkarte` | Aerzte Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `aerztewerbung-innovative-therapie` | Ärztewerbung innovative Therapie: moderner Medizinrechts-Skill für Werbung mit innovativer Methode, Heilungsversprechen, Vorher-Nachher, Studienlage und Plattformen: Ärztewerbung innovative Therapie: moderner Medizinrechts-Skill für Werb... |
| `amnog-millionen-therapie` | AMNOG und Millionen-Therapie: moderner Medizinrechts-Skill für Einmaltherapie mit sehr hohem Preis, Budgetwirkung, Erstattungsbetrag, Outcome-Based-Modelle und Regressangst: AMNOG und Millionen-Therapie: moderner Medizinrechts-Skill für... |
| `anaesthesie-hochrisiko-aufklaerung` | Anästhesie Hochrisiko-Aufklärung: moderner Medizinrechts-Skill für Narkoserisiko, ASA, Aspirationsgefahr, Blutprodukte, Aufklärungstiming und Notfallausnahme: Anästhesie Hochrisiko-Aufklärung: moderner Medizinrechts-Skill für Narkoserisi... |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Medizinrecht: wählt den nächsten Spezial-Skill nach Engpass (Verjährung 3 Jahre § 195 BGB, Behandlungsvertrag, Patientenakte, Aufklärungsbogen), dokumentiert Router-Entscheidung mit Begründung. |
| `apothekenrecht-arzneimittel-paragraf-78-amg` | Apothekenrecht Arzneimittel § 78 AMG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `apothekenrecht-mehrparteien-konflikt-und-interessen` | Apothekenrecht: Mehrparteienkonflikt und Interessenmatrix: Apothekenrecht: Mehrparteienkonflikt und Interessenmatrix. |
| `approbation-digitales-fehlverhalten` | Approbation und digitales Fehlverhalten: moderner Medizinrechts-Skill für Telemedizin-Fehlverhalten, Social Media, Abrechnungsbetrug, Unwürdigkeit/Unzuverlässigkeit: Approbation und digitales Fehlverhalten: moderner Medizinrechts-Skill f... |
| `approbations-widerspruch` | Approbationswiderruf und Berufsrecht für Aerzte Apotheker Zahnaerzte: Anwendungsfall Heilberufler erhaelt Widerrufs-Bescheid oder Ruhens-Anordnung der Approbationsbehoerde: Approbationswiderruf und Berufsrecht für Aerzte Apotheker Zahnae... |
| `arzt-anstellung-mvz` | Arztanstellung im MVZ: moderner Medizinrechts-Skill für Anstellungsgenehmigung, Versorgungsauftrag, Arbeitszeit, Nebentätigkeit und Haftungsverteilung: Arztanstellung im MVZ: moderner Medizinrechts-Skill für Anstellungsgenehmigung, Verso... |
| `arzthaftung-aufklaerung-bgb` | Arzthaftung und ärztliche Aufklärung nach §§ 630a ff. BGB: Spezial-Skill für Einwilligung, Risikoaufklärung, Dokumentation, Beweislast und prozessuales Vorgehen ohne ungeprüfte Aktenzeichen. |
| `arzthaftung-fristen-form-und-zustaendigkeit` | Arzthaftung: Fristen, Form, Zuständigkeit und Rechtsweg: Arzthaftung: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `assistierter-suizid-beratung` | Assistierter Suizid Beratung: moderner Medizinrechts-Skill für Ärztliche Beratung, Freiverantwortlichkeit, Berufsrecht, Strafrechtsgrenzen und Dokumentation: Assistierter Suizid Beratung: moderner Medizinrechts-Skill für Ärztliche Beratu... |
| `atmp-chain-of-identity` | ATMP Chain of Identity: moderner Medizinrechts-Skill für Autologe Zelltherapie: Patientenmaterial, Verwechslung, Transport, Kryokonservierung und Auditspur: ATMP Chain of Identity: moderner Medizinrechts-Skill für Autologe Zelltherapie:... |
| `atmp-classification-cat` | ATMP-Klassifizierung und CAT-Route: moderner Medizinrechts-Skill für Einordnung als Gentherapeutikum, somatische Zelltherapie, Tissue Engineering oder kombiniertes ATMP: ATMP-Klassifizierung und CAT-Route: moderner Medizinrechts-Skill fü... |
| `atmp-pharmakovigilanz-rmp` | ATMP-Pharmakovigilanz und RMP: moderner Medizinrechts-Skill für Risk-Management-Plan, Langzeit-Follow-up, Register, Safety Signals und Behördenkommunikation: ATMP-Pharmakovigilanz und RMP: moderner Medizinrechts-Skill für Risk-Management... |
| `aufklaerung-beweislast-und-darlegungslast` | Aufklaerung: Beweislast, Darlegungslast und Substantiierung: Aufklaerung: Beweislast, Darlegungslast und Substantiierung. |
| `aufklaerungsfehler` | Fachanwalt Medizinrecht Aufklaerungsfehler: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Medizinrecht Aufklaerungsfehler: ordnet Normen, Nutzerangaben, Fristen, Be... |
| `aufklaerungsfehler-beweisstrategie` | Aufklaerungsfehler Beweisstrategie: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Aufklaerungsfehler Beweisstrategie: ordnet Normen, Nutzerangaben, Fristen, Belege und verifiz... |
| `aufklaerungspflicht-paragraf-630e-bgb` | Aufklaerungspflicht § 630e BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `befundherausgabe-epa-akte` | Befundherausgabe, ePA und Akte: moderner Medizinrechts-Skill für Patient verlangt Akte, ePA-Dokumente, Rohdaten, Bilddaten und Herausgabeformat: Befundherausgabe, ePA und Akte: moderner Medizinrechts-Skill für Patient verlangt Akte, ePA-... |
| `behandlungsfehler-anspruch-pruefen` | Strukturierte Prüfung von Ansprüchen wegen Behandlungsfehler nach §§ 630a ff: BGB iVm § 823 BGB. Behandlungsvertrag Aufklärungspflicht § 630e BGB Dokumentationspflicht § 630f BGB... |
| `behandlungsfehler-paragraf-630h-bgb` | Behandlungsfehler § 630h BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `behandlungsfehler-pruefen` | Behandlungsfehler §§ 630a 630h BGB Verletzung medizinischer Standard: Diagnosefehler Therapiefehler Befunderhebungsfehler Hygienefehler. Beweisregeln § 630h BGB Vermutung Kausalität bei g... |
| `behandlungsvertrag-630a` | Behandlungsvertrag nach §§ 630a-h BGB und Patientenrechte prüfen: Anwendungsfall Patient behauptet Behandlungsfehler oder Aufklärungsmangel oder Arzt braucht Vertragsdokumentation: Behandlungsvertrag nach §§ 630a-h BGB und Patientenrecht... |
| `berufsrecht-verhandlung-vergleich-und-eskalation` | Berufsrecht: Verhandlung, Vergleich und Eskalation: Berufsrecht: Verhandlung, Vergleich und Eskalation. |
| `beweislast-hightech-medizin` | Beweislast in Hightech-Medizin: moderner Medizinrechts-Skill für Black-Box-Gerät, KI, Vektorcharge, Registerdaten und Beweisnot im Arzthaftungsprozess: Beweislast in Hightech-Medizin: moderner Medizinrechts-Skill für Black-Box-Gerät, KI,... |
| `bgb-risikoampel-und-gegenargumente` | BGB: Risikoampel, Gegenargumente und Verteidigungslinien: BGB: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `biobank-consent-withdrawal` | Biobank Consent Withdrawal: moderner Medizinrechts-Skill für Biobankprobe, Broad Consent, Widerruf, Forschungsnutzung und Rückmeldung von Zufallsbefunden: Biobank Consent Withdrawal: moderner Medizinrechts-Skill für Biobankprobe, Broad C... |
| `cannabis-medizinisch-verordnung` | Medizinisches Cannabis Verordnung: moderner Medizinrechts-Skill für Cannabis als Medizin, Verordnung, Kostenübernahme, Fahrtüchtigkeit und Berufspflichten: Medizinisches Cannabis Verordnung: moderner Medizinrechts-Skill für Cannabis als... |
| `car-t-haftung-klinik` | CAR-T-Behandlung: Klinikhaftung: moderner Medizinrechts-Skill für CAR-T-Aufklärung, Zytokinfreisetzung, Neurotoxizität, Patientenselektion und Klinikorganisation: CAR-T-Behandlung: Klinikhaftung: moderner Medizinrechts-Skill für CAR-T-Au... |
| `combined-atmp-device-mdr` | Kombiniertes ATMP mit Medizinprodukt: moderner Medizinrechts-Skill für ATMP mit Scaffold, Implantat, Katheter, Software oder Applikationsgerät und doppelter Regulierungslogik: Kombiniertes ATMP mit Medizinprodukt: moderner Medizinrechts-... |
| `companion-diagnostic-atmp` | Companion Diagnostic bei ATMP: moderner Medizinrechts-Skill für Therapieselektion durch Biomarker, Testqualität, falsche Negativ-/Positivbefunde und Erstattung: Companion Diagnostic bei ATMP: moderner Medizinrechts-Skill für Therapiesele... |
| `compassionate-use-haertefall` | Compassionate Use und Härtefall: moderner Medizinrechts-Skill für Nicht zugelassenes Arzneimittel, Härtefallprogramm, Nutzen-Risiko, Erstattung und Dokumentation: Compassionate Use und Härtefall: moderner Medizinrechts-Skill für Nicht zu... |
| `crispr-base-editing-einwilligung` | CRISPR/Base-Editing Einwilligung: moderner Medizinrechts-Skill für Genomeditierung, irreversible Risiken, Off-target-Risiken, Langzeitnachbeobachtung und Aufklärungstiefe: CRISPR/Base-Editing Einwilligung: moderner Medizinrechts-Skill fü... |
| `cybersecurity-medizinprodukt` | Cybersecurity Medizinprodukt: moderner Medizinrechts-Skill für Vernetztes Medizinprodukt, Patch, Ransomware, Manipulation, Patientenschaden und Meldeketten: Cybersecurity Medizinprodukt: moderner Medizinrechts-Skill für Vernetztes Medizi... |
| `diga-hersteller-arzt-haftung` | DiGA: Hersteller, Arzt und Haftung: moderner Medizinrechts-Skill für Digitale Gesundheitsanwendung, Verschreibung, positive Versorgungseffekte, Fehlfunktion und Verantwortungsgrenzen: DiGA: Hersteller, Arzt und Haftung: moderner Medizinr... |
| `dokumentationsaudit-630f` | Dokumentationsaudit § 630f: moderner Medizinrechts-Skill für Behandlungsakte auditieren, Lücken, nachträgliche Änderungen, Metadaten und Beweisvermutung: Dokumentationsaudit § 630f: moderner Medizinrechts-Skill für Behandlungsakte auditi... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Medizinrecht: sortiert Behandlungsvertrag, Patientenakte, Aufklärungsbogen, prüft Datum, Absender, Frist und Beweiswert (Patientenakte, SV-Gutachten Arzthaftung); markiert Lücken; berücksichtigt Mandatsgeh... |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Medizinrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Medizinrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diese... |
| `einwilligung-sonderfall-edge-case` | Einwilligung: Sonderfall und Edge-Case-Prüfung: Einwilligung: Sonderfall und Edge-Case-Prüfung. |
| `einwilligungsunfaehigkeit-ablehnung` | Einwilligungsunfähigkeit und Ablehnung: moderner Medizinrechts-Skill für Therapieablehnung, natürliche Wille, Zwangsbehandlung, Betreuungsgericht und Klinikalltag: Einwilligungsunfähigkeit und Ablehnung: moderner Medizinrechts-Skill für... |
| `epa-befuellpflicht-haftung` | ePA-Befüllpflicht und Haftung: moderner Medizinrechts-Skill für ePA für alle, Befüllungspflichten, Informationspflichten, Widerspruch und Behandlungsfehler durch Datenlücke: ePA-Befüllpflicht und Haftung: moderner Medizinrechts-Skill für... |
| `erezept-falschmedikation` | E-Rezept und Falschmedikation: moderner Medizinrechts-Skill für E-Rezept, Medikationsliste, Wechselwirkung, Apotheken-/Arztfehler und Nachweisführung: E-Rezept und Falschmedikation: moderner Medizinrechts-Skill für E-Rezept, Medikationsl... |
| `erstgespraech-mandatsannahme` | Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt meldet sich mit unstrukturiertem Sachverhalt zu Behandlungsfehler Approbationsproblem oder KV-Streit: Erstgespraeach und M... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel. |
| `experimentelle-behandlung-vertrag` | Experimentelle Behandlung Vertrag: moderner Medizinrechts-Skill für Behandlungsvertrag für innovative Methode, keine Erfolgsgarantie, Aufklärung und Abgrenzung Forschung/Heilversuch: Experimentelle Behandlung Vertrag: moderner Medizinrec... |
| `fa-medizinrecht-quellen-frist-next` | Rechtsquellen: Quellenprüfung; Fristennotiz und nächster Schritt: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert |
| `fertilitaetsmedizin-recht` | Fertilitätsmedizin Recht: moderner Medizinrechts-Skill für IVF, Samenspende, Embryonenschutz, Abstammung, Aufklärung und Haftung: Fertilitätsmedizin Recht: moderner Medizinrechts-Skill für IVF, Samenspende, Embryonenschutz, Abstammung, A... |
| `field-safety-corrective-action` | FSCA und Rückrufkommunikation: moderner Medizinrechts-Skill für Field Safety Corrective Action, Sicherheitsmitteilung, Patientennachverfolgung und Klinikpflichten: FSCA und Rückrufkommunikation: moderner Medizinrechts-Skill für Field Saf... |
| `first-in-human-riskboard` | First-in-Human Risk Board: moderner Medizinrechts-Skill für Erstgabe am Menschen, Dosissteigerung, Sentinel-Dosing, Stop-Regeln und Krisenkommunikation: First-in-Human Risk Board: moderner Medizinrechts-Skill für Erstgabe am Menschen, Do... |
| `geburtshilfe-ctg-sectio` | Geburtshilfe CTG und Sectio: moderner Medizinrechts-Skill für Pathologisches CTG, Entscheidungs-Entbindungszeit, Hebammen-/Ärzteteam und grober Fehler: Geburtshilfe CTG und Sectio: moderner Medizinrechts-Skill für Pathologisches CTG, Ent... |
| `gendg-diagnostik-einwilligung` | GenDG Diagnostik und Einwilligung: moderner Medizinrechts-Skill für Diagnostische genetische Untersuchung, Schriftlichkeit, Arztvorbehalt und Befundkommunikation: GenDG Diagnostik und Einwilligung: moderner Medizinrechts-Skill für Diagno... |
| `genomdaten-ehds-biobank` | Genomdaten, EHDS und Biobank: moderner Medizinrechts-Skill für Genomdaten für Forschung, Biobank, Secondary Use, Gesundheitsdatenzugang und Widerruf: Genomdaten, EHDS und Biobank: moderner Medizinrechts-Skill für Genomdaten für Forschung... |
| `gentherapie-dossier-gmp` | Gentherapie-Dossier und GMP-Kette: moderner Medizinrechts-Skill für Qualität, Nichtklinik, Klinik, Herstellkette, Freigabe und Chargen-/Vektorlogik bei Gentherapeutika: Gentherapie-Dossier und GMP-Kette: moderner Medizinrechts-Skill für... |
| `gentherapie-langzeit-followup` | Gentherapie Langzeit-Follow-up: moderner Medizinrechts-Skill für Nachbeobachtung über Jahre, Registerdaten, Patientenumzug, Abbruch der Nachsorge und Haftungsfolgen: Gentherapie Langzeit-Follow-up: moderner Medizinrechts-Skill für Nachbe... |
| `gesundheitsdatenpanne-klinik` | Gesundheitsdatenpanne Klinik: moderner Medizinrechts-Skill für Fehlversand Arztbrief, Portalzugriff, Ransomware, Meldung, Benachrichtigung und Schadensersatz: Gesundheitsdatenpanne Klinik: moderner Medizinrechts-Skill für Fehlversand Arz... |
| `goae-analog-innovativ` | GOÄ analog bei Innovation: moderner Medizinrechts-Skill für Neue Methode, Analogbewertung, Steigerungssatz, Begründung und Versicherungsstreit: GOÄ analog bei Innovation: moderner Medizinrechts-Skill für Neue Methode, Analogbewertung, St... |
| `grenzueberschreitende-behandlung-eu` | Grenzüberschreitende Behandlung EU: moderner Medizinrechts-Skill für Auslandsbehandlung, Richtlinie 2011/24/EU, Erstattung, Haftungsstatut und Beweis: Grenzüberschreitende Behandlung EU: moderner Medizinrechts-Skill für Auslandsbehandlun... |
| `gutachterkommission-aek-schlichtung` | Gutachterkommissionen und Schlichtungsstellen der Aerztekammern bei Arzthaftung nutzen: Anwendungsfall Patient oder Anwalt erwägt Schlichttungsverfahren vor Aerztekammer als kostenguenstige Alternative zur Klage: Gutachterkommissionen un... |
| `haemovigilanz-blutprodukt` | Hämovigilanz und Blutprodukt: moderner Medizinrechts-Skill für Transfusion, Verwechslung, Infektion, Chargenfreigabe, Rückverfolgung und PEI-Meldung: Hämovigilanz und Blutprodukt: moderner Medizinrechts-Skill für Transfusion, Verwechslun... |
| `honorarvertrag-kv` | Honorarstreitigkeiten mit Kassenärztlicher Vereinigung begleiten: Anwendungsfall Vertragsarzt erhaelt Honorar-Bescheid mit Kuestzungen oder Wirtschaftlichkeits- oder Plausibilitaetsprüfung laeuft: Honorarstreitigkeiten mit Kassenärztlich... |
| `hospital-exemption-4b-amg` | Hospital Exemption § 4b AMG: moderner Medizinrechts-Skill für Nicht routinemäßige ATMP-Anwendung im Krankenhaus, Einzelfallherstellung, Qualitätsstandards und PEI-Genehmigung: Hospital Exemption § 4b AMG: moderner Medizinrechts-Skill für... |
| `hta-jca-atmp-onkologie` | EU-HTA/JCA bei ATMP und Onkologie: moderner Medizinrechts-Skill für Gemeinsame klinische Bewertung seit 2025 für Krebsarzneimittel und ATMP, Schnittstelle zum nationalen Nutzenbewertungsweg: EU-HTA/JCA bei ATMP und Onkologie: moderner Me... |
| `igel-leistungen-paragraf-630c-bgb-bgh-vi-zr-66-15` | Igel Leistungen Paragraf 630c BGB BGH Vi Zr 66 15: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `impfschaden-arzthaftung` | Impfschaden und Arzthaftung: moderner Medizinrechts-Skill für Impfaufklärung, Chargenproblem, Versorgungsanspruch, Kausalität und Pharmakovigilanz: Impfschaden und Arzthaftung: moderner Medizinrechts-Skill für Impfaufklärung, Chargenprob... |
| `implantateregister-rueckruf` | Implantateregister und Rückruf: moderner Medizinrechts-Skill für Implantateregister, Rückruf, Field Safety Notice, Patientennachverfolgung und Beweis: Implantateregister und Rückruf: moderner Medizinrechts-Skill für Implantateregister, R... |
| `influencer-healthcare-werbung` | Influencer Healthcare Werbung: moderner Medizinrechts-Skill für Ärztliche Influencer, Klinikmarketing, Kennzeichnung, Patientengeheimnis und irreführende Claims: Influencer Healthcare Werbung: moderner Medizinrechts-Skill für Ärztliche I... |
| `ivdr-lab-developed-test` | IVDR und Lab Developed Test: moderner Medizinrechts-Skill für In-vitro-Diagnostikum, Labor-Eigenentwicklung, Companion Diagnostics und Übergangsrisiken: IVDR und Lab Developed Test: moderner Medizinrechts-Skill für In-vitro-Diagnostikum,... |
| `kanzlei-red-team-und-qualitaetskontrolle` | Kanzlei: Red-Team und Qualitätskontrolle: Kanzlei: Red-Team und Qualitätskontrolle. |
| `kassenarztrecht` | Kassenarztrecht Vertragsarztzulassung und KV-Streitigkeiten: Anwendungsfall Arzt beantragt Vertragsarztzulassung hat Zulassungsprobleme oder streitet mit KV um Honorar Berechtigung oder Zulassungsstatus: Kassenarztrecht Vertragsarztzulas... |
| `keimbahn-grenze-embryo` | Keimbahn-Grenze und Embryonenschutz: moderner Medizinrechts-Skill für Keimbahneingriff, Embryonen-/Fortpflanzungsmedizin und rote Linien bei innovativer Therapie: Keimbahn-Grenze und Embryonenschutz: moderner Medizinrechts-Skill für Keim... |
| `ki-medizinprodukt-highrisk` | KI-Medizinprodukt High-Risk: moderner Medizinrechts-Skill für KI-gestützte Diagnose/Prognose/Triage, MDR plus AI Act und ärztliche Letztverantwortung: KI-Medizinprodukt High-Risk: moderner Medizinrechts-Skill für KI-gestützte Diagnose/Pr... |
| `klinische-pruefung-ctr-amg` | Klinische Prüfung CTR/AMG: moderner Medizinrechts-Skill für Arzneimittelstudie, Sponsorpflichten, Ethik, Einwilligung, Prüfplanabweichung und SAE/SUSAR: Klinische Prüfung CTR/AMG: moderner Medizinrechts-Skill für Arzneimittelstudie, Spon... |
| `krankenhaushygiene-mrsa` | Krankenhaushygiene Mrsa: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `krankenhausreform-leistungsgruppen` | Krankenhausreform Leistungsgruppen: moderner Medizinrechts-Skill für KHVVG/KHAG, Leistungsgruppen, Qualitätskriterien, Kooperation und Haftung bei Leistungsverschiebung: Krankenhausreform Leistungsgruppen: moderner Medizinrechts-Skill fü... |
| `krankenversicherung-zahlen-schwellen-und-berechnung` | Krankenversicherung: Zahlen, Schwellenwerte und Berechnung: Krankenversicherung: Zahlen, Schwellenwerte und Berechnung. |
| `krankenversicherungsrecht-paragraf-13-sgb-v` | Krankenversicherungsrecht § 13 sgb v: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `laborwert-alarmpflicht` | Laborwert Alarmpflicht: moderner Medizinrechts-Skill für Kritischer Laborwert, Befundübermittlung, Praxisurlaub, Portalnachricht und verpasste Therapie: Laborwert Alarmpflicht: moderner Medizinrechts-Skill für Kritischer Laborwert, Befun... |
| `livecheck-abschlussprodukt-und-uebergabe` | Livecheck: Abschlussprodukt und Übergabe: Livecheck: Abschlussprodukt und Übergabe. |
| `mandat-triage-medizinrecht` | Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate: Klaert Mandantenrolle (Patient Arzt Krankenhaus Heilberufler Pharma Krankenkasse) Sachgebiet (Behandlungsfehler Aufklärungspflicht-Ve... |
| `medical-tourism-liability` | Medical Tourism Liability: moderner Medizinrechts-Skill für Ästhetik-/Zahn-/Fertilitätsbehandlung im Ausland, Vermittler, Nachbehandlung und Gerichtsstand: Medical Tourism Liability: moderner Medizinrechts-Skill für Ästhetik-/Zahn-/Ferti... |
| `medizinischer-eingriff-einwilligung` | Medizinischer Eingriff Einwilligung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `medizinprodukt-haftung-paragraf-1-prodhaftg` | Medizinprodukt Haftung § 1 ProdHaftG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `medizinrecht-tatbestand-beweis-und-belege` | Medizinrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage: Medizinrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `medr-arzthaftung-checkliste` | Checkliste Arzthaftung: Behandlungsfehler, grober Behandlungsfehler, Beweislastumkehr § 630h BGB, Befunderhebungsfehler, voll beherrschbares Risiko: Checkliste Arzthaftung: Behandlungsfehler, grober Behandlungsfehler, Beweislastumkehr §... |
| `medr-aufklaerung-einwilligung-leitfaden` | Leitfaden Aufklaerung und Einwilligung §§ 630d und 630e BGB: Grundaufklaerung, Risikoaufklaerung, Verlaufsaufklaerung: Prüfraster für Ein... |
| `medr-aufklaerung-und-einwilligung-praxis` | Aufklaerung und Einwilligung in der Praxis: § 630e BGB, Form, Zeitpunkt, Inhalt, Sprachbarrieren, Stellvertretung Minderjaehriger, Notfallausnahme: Aufklaerung und Einwilligung in der Praxis: § 630e BGB, Form, Zeitpunkt, Inhalt, Sprachba... |
| `medr-einfuehrung-themen` | Medizinrecht einfuehrend: Arzthaftung, Berufsrecht, Vertragsarztrecht, Krankenhausrecht, Arzneimittel- und Medizinprodukterecht, Heilmittelwerberecht, MVZ-Strukturen: Medizinrecht einfuehrend: Arzthaftung, Berufsrecht, Vertragsarztrecht,... |
| `medr-grundpfeiler-igel-und-aerztewerbung-spezial` | Spezialfall IGeL-Leistungen und Aerztewerbung: § 18 MBO-Aerzte, sachliche berufsbezogene Information, unsachlich-anpreisende Werbung, Preisvergleichsportale (Jameda, Doctolib), Bewertungsplattformen-Recht: Spezialfall IGeL-Leistungen und... |
| `medr-igel-leistung-spezial` | Spezialfall IGeL Individuelle Gesundheitsleistung: GOAE Abrechnung, Aufklaerung wirtschaftlich, Schriftform der Vereinbarung, Werbung: Spezialfall IGeL Individuelle Gesundheitsleistung: GOAE Abrechnung, Aufklaerung wirtschaftlich, Schrif... |
| `medr-mandantenkommunikation-entscheidungsvorlage` | Medr: Mandantenkommunikation und Entscheidungsvorlage: Medr: Mandantenkommunikation und Entscheidungsvorlage. |
| `medr-mvz-strukturierung-spezial` | Spezialfall MVZ-Strukturierung: Traegerschaft GmbH, KH, Vertragsarzt, Genossenschaft: Investorenbeteiligung, fachuebergreifend, Spezialregelung Zahnarzt-MVZ, Zulassungsaus... |
| `medr-mvz-strukturwandel-spezial` | Spezialfall MVZ-Strukturwandel: § 95 SGB V, Investor-MVZ, Anstellungsgenehmigung, Versorgungsauftrag, Konzentrationsverbot: Prüfrast... |
| `minderjaehrige-einwilligung` | Minderjährige und Einwilligung: moderner Medizinrechts-Skill für Einwilligungsfähigkeit Minderjähriger, Elternkonflikt, dringende Behandlung und Datenschutz: Minderjährige und Einwilligung: moderner Medizinrechts-Skill für Einwilligungsf... |
| `mindestmengen-zentrumsbildung` | Mindestmengen und Zentrumsbildung: moderner Medizinrechts-Skill für Komplexe Eingriffe, Mindestmengen, Zentrumsbildung, Verlegungspflicht und Patientensicherheit: Mindestmengen und Zentrumsbildung: moderner Medizinrechts-Skill für Komple... |
| `mpdg-compliance-dokumentation-und-akte` | Mpdg: Compliance-Dokumentation und Aktenvermerk: Mpdg: Compliance-Dokumentation und Aktenvermerk. |
| `mvz-investor-compliance` | Investor-MVZ Compliance: moderner Medizinrechts-Skill für MVZ-Träger, ärztliche Leitung, Weisungsfreiheit, Zuweisung, Abrechnung und Berufsrecht: Investor-MVZ Compliance: moderner Medizinrechts-Skill für MVZ-Träger, ärztliche Leitung, We... |
| `n-of-1-therapie` | N-of-1-Therapie und Heilversuch: moderner Medizinrechts-Skill für Individualisierte Therapie außerhalb Standardpfad, Erkenntnisgrenze, Einwilligung und Kostenträger: N-of-1-Therapie und Heilversuch: moderner Medizinrechts-Skill für Indiv... |
| `nosokomiale-infektion-hygiene` | Nosokomiale Infektion und Hygiene: moderner Medizinrechts-Skill für Hygienemangel, MRSA/CRE, OP-Saal, Aufbereitung, voll beherrschbares Risiko: Nosokomiale Infektion und Hygiene: moderner Medizinrechts-Skill für Hygienemangel, MRSA/CRE,... |
| `notaufnahme-triage` | Notaufnahme-Triage: moderner Medizinrechts-Skill für Triagefehler, Überlastung, Dokumentation, Wartezeit, ESI/MTS und Organisationshaftung: Notaufnahme-Triage: moderner Medizinrechts-Skill für Triagefehler, Überlastung, Dokumentation, Wa... |
| `notfall-mutmassliche-einwilligung` | Notfall und mutmaßliche Einwilligung: moderner Medizinrechts-Skill für Bewusstlosigkeit, Zeitdruck, Patientenverfügung, Stellvertreter und Dokumentation: Notfall und mutmaßliche Einwilligung: moderner Medizinrechts-Skill für Bewusstlosig... |
| `off-label-rare-disease` | Off-Label bei seltener Erkrankung: moderner Medizinrechts-Skill für Off-Label-Use, Seltenheit, Datenlage, lebensbedrohliche Erkrankung und GKV-Erstattung: Off-Label bei seltener Erkrankung: moderner Medizinrechts-Skill für Off-Label-Use,... |
| `off-label-use-erstattung-gkv-long-covid` | Off-Label-Use und GKV-Erstattungsstreitigkeiten insbesondere Long-Covid: Anwendungsfall Patient benoetigt nicht zugelassenes Medikament oder Therapie und GKV verweigert Erstattung: Off-Label-Use und GKV-Erstattungsstreitigkeiten insbeson... |
| `orientierung-mandat-fachanwaltschaft` | Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen verifizierbare Quellen: Arzthaftung §§ 630a ff. BGB (Patientenrecht... |
| `orphan-atmp-zugang` | Orphan ATMP Zugang: moderner Medizinrechts-Skill für Seltene Erkrankung, Orphan-Status, Studienzugang, Registerdaten und Kostenträgerstrategie: Orphan ATMP Zugang: moderner Medizinrechts-Skill für Seltene Erkrankung, Orphan-Status, Studi... |
| `output-waehlen` | Output-Wahl für Fachanwalt Medizinrecht: stimmt Adressat (Patient, Arzt/Krankenhaus, Krankenkasse), Frist (Verjährung 3 Jahre § 195 BGB) und Form auf den Zweck ab — typische Outputs: Arzthaftungsklage, Selbstständiges Beweisverfahren, KV... |
| `palliativmedizin-haftung` | Palliativmedizin Haftung: moderner Medizinrechts-Skill für Symptomkontrolle, Sedierung, Patientenwille, Angehörigenkonflikt und Dokumentation: Palliativmedizin Haftung: moderner Medizinrechts-Skill für Symptomkontrolle, Sedierung, Patien... |
| `paragraf-95-sgb-v-zulassung` | § 95 sgb v Zulassung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `pathologie-probenverwechslung` | Pathologie Probenverwechslung: moderner Medizinrechts-Skill für Gewebeprobe, Barcode, Präanalytik, Chain of Custody und falsche Krebsdiagnose: Pathologie Probenverwechslung: moderner Medizinrechts-Skill für Gewebeprobe, Barcode, Präanaly... |
| `patientenrechte-behoerden-gericht-und-registerweg` | Patientenrechte: Behörden-, Gerichts- oder Registerweg: Patientenrechte: Behörden-, Gerichts- oder Registerweg. |
| `patientenverfuegung-klinik` | Patientenverfügung in der Klinik: moderner Medizinrechts-Skill für Auslegung von Patientenverfügung, Vorsorgevollmacht, Ethikkomitee und Haftungsangst: Patientenverfügung in der Klinik: moderner Medizinrechts-Skill für Auslegung von Pati... |
| `praediktive-genetik-familie` | Prädiktive Genetik und Familie: moderner Medizinrechts-Skill für Prädiktiver Test, Angehörigeninformation, Recht auf Nichtwissen und Beratungsdokumentation: Prädiktive Genetik und Familie: moderner Medizinrechts-Skill für Prädiktiver Tes... |
| `praenataldiagnostik-nipt` | Pränataldiagnostik und NIPT: moderner Medizinrechts-Skill für Nichtinvasive Pränataltests, Aufklärung, Beratung, Kostenerstattung und Konfliktlagen: Pränataldiagnostik und NIPT: moderner Medizinrechts-Skill für Nichtinvasive Pränataltest... |
| `privatklinik-paketpreis` | Privatklinik Paketpreis: moderner Medizinrechts-Skill für Pauschalangebot, GOÄ, Wahlleistung, IGeL, Kostentransparenz und Rückforderung: Privatklinik Paketpreis: moderner Medizinrechts-Skill für Pauschalangebot, GOÄ, Wahlleistung, IGeL,... |
| `produkthaftung-medizinprodukt-pld` | Produkthaftung Medizinprodukt PLD 2024: moderner Medizinrechts-Skill für Defektes Medizinprodukt, Software, KI, Updatepflicht, Beweiserleichterung und Wirtschaftsakteure: Produkthaftung Medizinprodukt PLD 2024: moderner Medizinrechts-Ski... |
| `psychedelika-studie-therapie` | Psychedelika Studie und Therapie: moderner Medizinrechts-Skill für Psilocybin/MDMA-Studie, Betäubungsmittelrecht, Ethik, Off-Label-Mythen und Haftung: Psychedelika Studie und Therapie: moderner Medizinrechts-Skill für Psilocybin/MDMA-Stu... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Medizinrecht: prüft Normen (BGB §§ 630a ff. Behandlungsvertrag, AMG, MPDG, SGB V, BÄO, MBO-Ä) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt LG (Arzthaftung) und Quellenhygiene n... |
| `radiologie-ki-befund` | Radiologie-KI und Befundfehler: moderner Medizinrechts-Skill für KI-Vorschlag, ärztlicher Befund, Overreliance, Softwareupdate und verpasster Zufallsbefund: Radiologie-KI und Befundfehler: moderner Medizinrechts-Skill für KI-Vorschlag, ä... |
| `registerdaten-patientensicherheit` | Registerdaten Patientensicherheit: moderner Medizinrechts-Skill für Klinisches Register, Qualitätssicherung, Pseudonymisierung, Zweckänderung und Haftungsprävention: Registerdaten Patientensicherheit: moderner Medizinrechts-Skill für Kli... |
| `robotische-operation` | Robotische Operation: moderner Medizinrechts-Skill für Da-Vinci-/Robotik-OP, Bedienfehler, Training, Herstellerhinweis und Aufklärung: Robotische Operation: moderner Medizinrechts-Skill für Da-Vinci-/Robotik-OP, Bedienfehler, Training, H... |
| `sachverstaendiger-innovationsstandard` | Sachverständiger und Innovationsstandard: moderner Medizinrechts-Skill für Gerichtsgutachten bei neuer Methode, Leitlinienlücke, Registerdaten und Standardbildung: Sachverständiger und Innovationsstandard: moderner Medizinrechts-Skill fü... |
| `samd-zweckbestimmung` | Software as Medical Device Zweckbestimmung: moderner Medizinrechts-Skill für Softwaregrenze Wellness-App/Medizinprodukt, Zweckbestimmung, CE und ärztliche Anwendung: Software as Medical Device Zweckbestimmung: moderner Medizinrechts-Skil... |
| `schmerzensgeld-hightech-schaden` | Schmerzensgeld bei Hightech-Schaden: moderner Medizinrechts-Skill für Schwere Dauerschäden durch Medizinprodukt, Gentherapie oder Klinikfehler: Schmerzensgeld bei Hightech-Schaden: moderner Medizinrechts-Skill für Schwere Dauerschäden du... |
| `schnittstellen-internationaler-bezug-und-schnittstellen` | Schnittstellen: Internationaler Bezug und Schnittstellen: Schnittstellen: Internationaler Bezug und Schnittstellen. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Arzthaftungsklage und KV-Streit: Anwendungsfall Medizinrechts-Anwalt muss vollwertigen Schriftsatz in Arzthaftungssache Sozialgericht oder Berufsrechtsbeschwerde verfassen: Substantiierter Schriftsatzk... |
| `sedierung-ambulant-igel` | Ambulante Sedierung und IGeL: moderner Medizinrechts-Skill für Sedierung in Praxis/MVZ, Überwachung, Privatvereinbarung, GOÄ und Notfallmanagement: Ambulante Sedierung und IGeL: moderner Medizinrechts-Skill für Sedierung in Praxis/MVZ, Ü... |
| `sepsis-diagnoseverzug` | Sepsis-Diagnoseverzug: moderner Medizinrechts-Skill für Infektzeichen, Labor, Eskalation, Antibiotikagabe, SOP und Kausalitätsstreit: Sepsis-Diagnoseverzug: moderner Medizinrechts-Skill für Infektzeichen, Labor, Eskalation, Antibiotikaga... |
| `sozialrecht-formular-portal-und-einreichung` | Sozialrecht: Formular, Portal und Einreichungslogik: Sozialrecht: Formular, Portal und Einreichungslogik. |
| `sprachbarriere-einwilligung` | Sprachbarriere Einwilligung: moderner Medizinrechts-Skill für Dolmetscher, fremdsprachige Aufklärung, Angehörige, Dokumentation und Beweislast: Sprachbarriere Einwilligung: moderner Medizinrechts-Skill für Dolmetscher, fremdsprachige Auf... |
| `stammzellklinik-patientenschaden` | Stammzellklinik und Patientenschaden: moderner Medizinrechts-Skill für Haftung nach nicht zugelassener Zellbehandlung, Beweisführung, Aufklärung und deliktische Ansprüche: Stammzellklinik und Patientenschaden: moderner Medizinrechts-Skil... |
| `sterilgut-medizinprodukt` | Sterilgut und Medizinprodukt: moderner Medizinrechts-Skill für Aufbereitungsfehler, Sterilgutdokumentation, Herstellerangaben und Vorkommnismeldung: Sterilgut und Medizinprodukt: moderner Medizinrechts-Skill für Aufbereitungsfehler, Ster... |
| `telemedizin-standardhaftung` | Telemedizin Standardhaftung: moderner Medizinrechts-Skill für Fernbehandlung, Grenzen ohne körperliche Untersuchung, Triage, Videoausfall und Dokumentation: Telemedizin Standardhaftung: moderner Medizinrechts-Skill für Fernbehandlung, Gr... |
| `transplantation-allocation` | Transplantation und Allocation: moderner Medizinrechts-Skill für Warteliste, Meldedaten, Vermittlung, Aufklärung und Compliance bei Transplantationszentren: Transplantation und Allocation: moderner Medizinrechts-Skill für Warteliste, Mel... |
| `tumorboard-onkologiepflicht` | Tumorboard und Onkologiepflicht: moderner Medizinrechts-Skill für Tumorboard-Dokumentation, Leitlinienabweichung, molekulare Diagnostik und Therapieoptionen: Tumorboard und Onkologiepflicht: moderner Medizinrechts-Skill für Tumorboard-Do... |
| `unregulierte-zelltherapie-abwehr` | Unregulierte Zelltherapie abwehren: moderner Medizinrechts-Skill für Online beworbene Stammzell-/Dendriten-/Exosomenangebote, Behördenweg, Unterlassung und Patientenschutz: Unregulierte Zelltherapie abwehren: moderner Medizinrechts-Skill... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Medizinrecht: trennt fehlende Tatsachen von fehlenden Belegen (Behandlungsvertrag, Patientenakte, Aufklärungsbogen), nennt pro Lücke Beweisthema, Beschaffungsweg (LG (Arzthaftung)), Frist und... |
| `vektor-shedding-umweltrisiko` | Vektor-Shedding und Umweltrisiko: moderner Medizinrechts-Skill für AAV/Lenti-/Onkolytika-Risiken, Umweltrisikobewertung, Schutzmaßnahmen und Meldeketten: Vektor-Shedding und Umweltrisiko: moderner Medizinrechts-Skill für AAV/Lenti-/Onkol... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlung und Einigungsstrategie im Medizinrecht: Anwendungsfall Arzthaftungssache KV-Streit oder Berufsrechtsbeschwerde eignet sich für außergerichtliche Einigung: Vergleichsverhandlung und Einigungsstrategie im Medizinrecht... |
| `vertragsarztrecht-schriftsatz-brief-und-memo-bausteine` | Vertragsarztrecht: Schriftsatz-, Brief- und Memo-Bausteine: Vertragsarztrecht: Schriftsatz-, Brief- und Memo-Bausteine. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
