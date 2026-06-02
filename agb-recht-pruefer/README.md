# AGB-Recht-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`agb-recht-pruefer`) | [`agb-recht-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/agb-recht-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Gigantisches Plugin für deutsches AGB-Recht: Prüfen, Entwerfen, Redlinen, Verhandeln, Rollout und Streitverteidigung von Allgemeinen Geschäftsbedingungen in allen praktischen Varianten.

Das Plugin ist bewusst zweigleisig gebaut:

- **AGB prüfen:** Klauseln zerlegen, Einbeziehung und Transparenz prüfen, §§ 305 bis 310 BGB sauber anwenden, Risiko bewerten, bessere Fassung vorschlagen.
- **AGB entwerfen:** Geschäftsmodell verstehen, Klauselfamilien auswählen, sichere oder bewusst risikobehaftete Fassungen erzeugen, Rollout und Nachweisfähigkeit mitdenken.

## Start

```text
/agb-recht-prüfer:allgemein
```

Der Einstieg fragt zürst nicht zwanzig Dinge ab, sondern klärt die wichtigste Weiche: **prüfen oder entwerfen?** Danach routet er in passende Spezialskills, etwa Verbraucher-AGB, B2B-AGB, Online-Checkout, Preisanpassung, Haftung, Laufzeit, UKlaG, Redline oder konkrete Branchenbedingungen.

## Arbeitsweise

1. Klausel und Vertragstyp erfassen.
2. AGB-Eigenschaft und Einbeziehung prüfen.
3. Überraschung, Mehrdeutigkeit und Transparenz klären.
4. Inhaltskontrolle nach §§ 307 bis 309 BGB und Besonderheiten nach § 310 BGB.
5. Rechtsfolge, Rückabwicklung, UKlaG-/Prozessrisiko prüfen.
6. Bessere Klausel entwerfen: sicher, balanced oder aggressiv mit Warnlabel.
7. Rollout, Versionierung, Nachweisbarkeit und Fachbereichskommunikation erledigen.

## Live-Quellen

Das Plugin soll bei tragenden Aussagen immer die aktülle amtliche Fassung auf **Gesetze im Internet** prüfen, insbesondere BGB §§ 305 bis 310 und UKlaG. Siehe [`references/QUELLEN.md`](./references/QUELLEN.md).

## Typische Ergebnisse

| Bedarf | Ergebnis |
| --- | --- |
| Fremde AGB schnell prüfen | Klauselampel, Risikobegründung, Redline-Kommentar |
| Eigene AGB neu entwerfen | Klauselarchitektur, sichere Fassungen, Fallbacks |
| B2C-Rollout vorbereiten | Checkout-/Einbeziehungscheck, Versionierung, Kundenkommunikation |
| B2B-Verhandlung führen | Playbook mit Must-have, Fallback, No-Go und Argumenten |
| Abmahnung erhalten | Fristenscan, UKlaG-Risiko, modifizierte Unterlassungserklärung |
| Management informieren | kurze Legal Note mit Risiko, Optionen und Empfehlung |

## Enthaltene Skills

Die vollständige Skill-Liste wird automatisch am Ende dieser README aktualisiert.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 200 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-reagieren` | Output- und Streit-Skill für Abmahnung Reagieren: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `abnahme-testing` | Klausel-Spezialskill für Abnahme Testing: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `abtretung` | Klausel-Spezialskill für Abtretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `adversarial-test-agb` | Output- und Streit-Skill für Adversarial Test AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `aenderungsvorbehalt-308` | Norm- und Dogmatik-Skill für Änderungsvorbehalt 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `agb-begriff-vorformuliert-305` | Norm- und Dogmatik-Skill für AGB Begriff Vorformuliert 305: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `agb-entwurf-kaltstart` | Einstiegs- und Workflow-Skill für AGB Entwurf Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-pruefung-kaltstart` | Einstiegs- und Workflow-Skill für AGB Prüfung Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-risikoklassifizierung-ampel` | Einstiegs- und Workflow-Skill für AGB Risikoklassifizierung Ampel: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-versionierung-aenderungshistorie` | Einstiegs- und Workflow-Skill für AGB Versionierung Änderungshistorie: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agentur-marketing-agb` | Branchen-Spezialskill für Agentur Marketing AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `allgemein` | Einstiegs- und Workflow-Skill für Allgemein: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `annahmefrist-leistungsfrist-308` | Norm- und Dogmatik-Skill für Annahmefrist Leistungsfrist 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `app-agb` | Branchen-Spezialskill für App AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `arbeitsrecht-agb-310-abs4` | Norm- und Dogmatik-Skill für Arbeitsrecht AGB 310 Abs. 4: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `architekten-ingenieur-agb` | Branchen-Spezialskill für Architekten Ingenieur AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `auditrechte` | Klausel-Spezialskill für Auditrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `aufrechnung-zurueckbehaltung-309` | Norm- und Dogmatik-Skill für Aufrechnung Zurückbehaltung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `automatische-verlaengerung` | Klausel-Spezialskill für Automatische Verlängerung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `avv-und-agb-schnittstelle` | Branchen-Spezialskill für AVV und AGB Schnittstelle: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `b2b-harte-fassung` | Output- und Streit-Skill für B2B Harte Fassung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `b2c-b2b-b2b2c-rollencheck` | Einstiegs- und Workflow-Skill für B2C B2B B2B2C Rollencheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `backup-datenverlust` | Klausel-Spezialskill für Backup Datenverlust: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bank-agb` | Branchen-Spezialskill für Bank AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `battle-of-forms-agb-kollision` | Norm- und Dogmatik-Skill für Battle of Forms AGB Kollision: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `bau-vob-agb` | Branchen-Spezialskill für Bau VOB/B AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `beweislast-und-zugang-309` | Norm- und Dogmatik-Skill für Beweislast und Zugang 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `bewertung-rezensionen` | Klausel-Spezialskill für Bewertung Rezensionen: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bildungs-kurs-agb` | Branchen-Spezialskill für Bildungs Kurs AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `board-brief-agb` | Output- und Streit-Skill für Board Brief AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `bonitaetspruefung` | Klausel-Spezialskill für Bonitätsprüfung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bonus-rabatt` | Klausel-Spezialskill für Bonus Rabatt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `business-summary-agb` | Output- und Streit-Skill für Business Summary AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `change-request` | Klausel-Spezialskill für Change Reqüst: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `clickwrap-beweisakte` | Output- und Streit-Skill für Clickwrap Beweisakte: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `cloud-hosting-agb` | Branchen-Spezialskill für Cloud Hosting AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `compliance-sanktionen` | Klausel-Spezialskill für Compliance Sanktionen: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `consulting-agb` | Branchen-Spezialskill für Consulting AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crowdfunding-agb` | Branchen-Spezialskill für Crowdfunding AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crypto-exchange-agb` | Branchen-Spezialskill für Crypto Exchange AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `darlehen-finanzierung-agb` | Branchen-Spezialskill für Darlehen Finanzierung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `datenexport-portabilitaet` | Klausel-Spezialskill für Datenexport Portabilität: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `datenschutzverweise-agb` | Klausel-Spezialskill für Datenschutzverweise AGB: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `definitionen-glossar-agb` | Output- und Streit-Skill für Definitionen Glossar AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `deutsch-englisch-agb` | Output- und Streit-Skill für Deutsch Englisch AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `digitale-inhalte-services` | Branchen-Spezialskill für Digitale Inhalte Services: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `dokumentation-handbuch` | Klausel-Spezialskill für Dokumentation Handbuch: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `dokumentenfamilie-rangfolge` | Einstiegs- und Workflow-Skill für Dokumentenfamilie Rangfolge: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `ecommerce-shop-agb` | Branchen-Spezialskill für Ecommerce Shop AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `eigentumsvorbehalt` | Klausel-Spezialskill für Eigentumsvorbehalt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `einbeziehung-hinweis-kenntnisnahme-305` | Norm- und Dogmatik-Skill für Einbeziehung Hinweis Kenntnisnahme 305: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `einbeziehung-online-clickwrap-browsewrap` | Norm- und Dogmatik-Skill für Einbeziehung Online Clickwrap Browsewrap: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `einkaufsbedingungen-b2b` | Branchen-Spezialskill für Einkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `einstweilige-verfuegung-agb` | Output- und Streit-Skill für Einstweilige Verfügung AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `energieversorgung-agb` | Branchen-Spezialskill für Energieversorgung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `entgelt-nebenkosten-service-fees` | Klausel-Spezialskill für Entgelt Nebenkosten Service Fees: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `erganzende-vertragsauslegung-agb-luecke` | Norm- und Dogmatik-Skill für Erganzende Vertragsauslegung AGB Lücke: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `exklusivitaet` | Klausel-Spezialskill für Exklusivität: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `factoring-agb` | Branchen-Spezialskill für Factoring AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `feedback-rechte` | Klausel-Spezialskill für Feedback Rechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `fiktive-erklaerung-zustimmung-308` | Norm- und Dogmatik-Skill für Fiktive Erklärung Zustimmung 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `fitnessstudio-agb` | Branchen-Spezialskill für Fitnessstudio AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `force-majeure-hoehere-gewalt` | Klausel-Spezialskill für Force Majeure Höhere Gewalt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `formulararbeitsvertrag` | Branchen-Spezialskill für Formulararbeitsvertrag: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `formvorgaben-anzeigen-erklaerungen-309` | Norm- und Dogmatik-Skill für Formvorgaben Anzeigen Erklärungen 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `forschung-entwicklung-agb` | Branchen-Spezialskill für Forschung Entwicklung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `fragebogen-agb-automation` | Output- und Streit-Skill für Fragebogen AGB Automation: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `franchise-agb` | Branchen-Spezialskill für Franchise AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `gaming-agb` | Branchen-Spezialskill für Gaming AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `garantie-beschaffenheit` | Klausel-Spezialskill für Garantie Beschaffenheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gerichtsstand` | Klausel-Spezialskill für Gerichtsstand: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gesellschaftsrechtliche-satzungen-agb-abgrenzung` | Norm- und Dogmatik-Skill für Gesellschaftsrechtliche Satzungen AGB Abgrenzung: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `gesetzliches-leitbild-abweichung-307` | Norm- und Dogmatik-Skill für Gesetzliches Leitbild Abweichung 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `gewahrleistung-ausschluss` | Klausel-Spezialskill für Gewährleistung Ausschluss: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gewerbemiete-agb` | Branchen-Spezialskill für Gewerbemiete AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `haendlervertrag-agb` | Branchen-Spezialskill für Haendlervertrag AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `haftung-grobe-fahrlaessigkeit-vorsatz` | Klausel-Spezialskill für Haftung Grobe Fahrlaessigkeit Vorsatz: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `haftung-indirekte-schaeden` | Klausel-Spezialskill für Haftung Indirekte Schaeden: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `haftung-leben-koerper-gesundheit-309` | Norm- und Dogmatik-Skill für Haftung Leben Koerper Gesundheit 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `haftungscap-summe` | Klausel-Spezialskill für Haftungscap Summe: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `handelsvertreter-agb` | Branchen-Spezialskill für Handelsvertreter AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `indexierung` | Klausel-Spezialskill für Indexierung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `individualabrede-305b` | Norm- und Dogmatik-Skill für Individualabrede 305b: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `individualklage-verteidigung` | Output- und Streit-Skill für Individualklage Verteidigung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `inhaltskontrolle-307-generalklausel` | Norm- und Dogmatik-Skill für Inhaltskontrolle 307 Generalklausel: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `insolvenzverkauf-agb` | Branchen-Spezialskill für Insolvenzverkauf AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `ip-nutzungsrechte` | Klausel-Spezialskill für IP Nutzungsrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kardinalpflichten` | Klausel-Spezialskill für Kardinalpflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ki-output-nutzung` | Klausel-Spezialskill für KI Output Nutzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ki-service-agb` | Branchen-Spezialskill für KI Service AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `klausel-checkliste-self-service` | Output- und Streit-Skill für Klausel Checkliste Self Service: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-aggressiv` | Output- und Streit-Skill für Klausel Entwerfen Aggressiv: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-balanced` | Output- und Streit-Skill für Klausel Entwerfen Balanced: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-low-risk` | Output- und Streit-Skill für Klausel Entwerfen Low Risk: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klauselbibliothek-aufbau` | Einstiegs- und Workflow-Skill für Klauselbibliothek Aufbau: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `klauselinventar-und-scope` | Einstiegs- und Workflow-Skill für Klauselinventar und Scope: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `klauselvarianten-vergleich` | Output- und Streit-Skill für Klauselvarianten Vergleich: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klauselverbote-308-systematik` | Norm- und Dogmatik-Skill für Klauselverbote 308 Systematik: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `klauselverbote-309-systematik` | Norm- und Dogmatik-Skill für Klauselverbote 309 Systematik: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `kollisionsrecht-ipr-agb` | Einstiegs- und Workflow-Skill für Kollisionsrecht IPR AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `konto-kuendigung-sperre` | Klausel-Spezialskill für Konto Kündigung Sperre: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `konzernklausel` | Klausel-Spezialskill für Konzernklausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigung-aus-wichtigem-grund` | Klausel-Spezialskill für Kündigung Aus Wichtigem Grund: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigung-ordentlich` | Klausel-Spezialskill für Kündigung Ordentlich: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigungsfiktion-und-nachfrist-308` | Norm- und Dogmatik-Skill für Kündigungsfiktion und Nachfrist 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `kurzfristige-preiserhoehung-309` | Norm- und Dogmatik-Skill für Kurzfristige Preiserhöhung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `lagerbedingungen` | Branchen-Spezialskill für Lagerbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `laufzeit-verlaengerung-309` | Norm- und Dogmatik-Skill für Laufzeit Verlängerung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `leasing-agb` | Branchen-Spezialskill für Leasing AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `legal-note-redline-output` | Einstiegs- und Workflow-Skill für Legal Note Redline Output: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `leistungsaenderung-produktupdate` | Klausel-Spezialskill für Leistungsänderung Produktupdate: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `lieferfrist-teillieferung` | Klausel-Spezialskill für Lieferfrist Teillieferung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `liquidated-damages` | Klausel-Spezialskill für Liquidated Damages: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `logistik-spedition-agb` | Branchen-Spezialskill für Logistik Spedition AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `maengelrechte-309` | Norm- und Dogmatik-Skill für Mängelrechte 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `mandanteninterview-agb` | Einstiegs- und Workflow-Skill für Mandanteninterview AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `mandantenmail-agb` | Output- und Streit-Skill für Mandantenmail AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `marketplace-agb` | Branchen-Spezialskill für Marketplace AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `massenschaden-datenmodell` | Output- und Streit-Skill für Massenschaden Datenmodell: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `mediation-escalation` | Klausel-Spezialskill für Mediation Escalation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `medizinische-leistungen-agb` | Branchen-Spezialskill für Medizinische Leistungen AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `mehrdeutigkeit-305c2` | Norm- und Dogmatik-Skill für Mehrdeutigkeit 305c2: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `mehrsprachige-agb-check` | Einstiegs- und Workflow-Skill für Mehrsprachige AGB Check: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `mindestabnahme` | Klausel-Spezialskill für Mindestabnahme: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `mitwirkungspflichten` | Klausel-Spezialskill für Mitwirkungspflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `msa-rahmenvertrag` | Branchen-Spezialskill für MSA Rahmenvertrag: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `nacherfuellung-vorrang` | Klausel-Spezialskill für Nacherfüllung Vorrang: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `nda-standardbedingungen` | Branchen-Spezialskill für NDA Standardbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `negative-feststellung-agb` | Output- und Streit-Skill für Negative Feststellung AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `non-solicitation` | Klausel-Spezialskill für Non Solicitation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `norm-live-check-gesetze-im-internet` | Einstiegs- und Workflow-Skill für Norm Live Check Gesetze Im Internet: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `open-source-komponenten` | Klausel-Spezialskill für Open Source Komponenten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `parking-mobility-agb` | Branchen-Spezialskill für Parking Mobility AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `plain-language-politur` | Output- und Streit-Skill für Plain Language Politur: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `plattform-und-online-checkout` | Einstiegs- und Workflow-Skill für Plattform und Online Checkout: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `preisanpassung-klausel` | Klausel-Spezialskill für Preisanpassung Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `product-counsel-workflow` | Output- und Streit-Skill für Product Counsel Workflow: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `quality-gate-vor-rollout` | Output- und Streit-Skill für Quality Gate Vor Rollout: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rangfolge-sprache` | Klausel-Spezialskill für Rangfolge Sprache: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `rechtsfolge-306-kein-blue-pencil` | Norm- und Dogmatik-Skill für Rechtsfolge 306 Kein Blü Pencil: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `rechtsfolgen-rueckabwicklung-agb` | Norm- und Dogmatik-Skill für Rechtsfolgen Rückabwicklung AGB: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `rechtswahl` | Klausel-Spezialskill für Rechtswahl: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `red-team-gegneransicht-agb` | Einstiegs- und Workflow-Skill für Red Team Gegneransicht AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `redline-kommentar-agb` | Output- und Streit-Skill für Redline Kommentar AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `referenznennung` | Klausel-Spezialskill für Referenznennung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `reisebedingungen` | Branchen-Spezialskill für Reisebedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `reseller-agb` | Branchen-Spezialskill für Reseller AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `risk-acceptance-memo` | Output- und Streit-Skill für Risk Acceptance Memo: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rollout-mail-bestandskunden` | Output- und Streit-Skill für Rollout Mail Bestandskunden: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rollout-monitoring-agb` | Einstiegs- und Workflow-Skill für Rollout Monitoring AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `ruegeobliegenheit` | Klausel-Spezialskill für Rügeobliegenheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `saas-agb` | Branchen-Spezialskill für SaaS AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `salvatorische-klausel` | Klausel-Spezialskill für Salvatorische Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `schadenspauschale-309` | Norm- und Dogmatik-Skill für Schadenspauschale 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `schiedsgericht` | Klausel-Spezialskill für Schiedsgericht: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `schriftform-textform` | Klausel-Spezialskill für Schriftform Textform: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `security-incidents` | Klausel-Spezialskill für Security Incidents: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `sicherungsrechte` | Klausel-Spezialskill für Sicherungsrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `sla-service-credits` | Klausel-Spezialskill für SLA Service Credits: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `social-media-agb` | Branchen-Spezialskill für Social Media AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `softwarelizenz-agb` | Branchen-Spezialskill für Softwarelizenz AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `sperrung-suspendierung` | Klausel-Spezialskill für Sperrung Suspendierung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `steuern-umsatzsteuer` | Klausel-Spezialskill für Steürn Umsatzsteür: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `stummer-upload-agb-dokumente` | Einstiegs- und Workflow-Skill für Stummer Upload AGB Dokumente: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `subscription-abonnement` | Branchen-Spezialskill für Subscription Abonnement: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `subscription-box-agb` | Branchen-Spezialskill für Subscription Box AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `subunternehmer` | Klausel-Spezialskill für Subunternehmer: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `support-response-times` | Klausel-Spezialskill für Support Response Times: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `telekommunikation-agb` | Branchen-Spezialskill für Telekommunikation AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `transparenzgebot-307` | Norm- und Dogmatik-Skill für Transparenzgebot 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `ueberraschende-klausel-305c` | Norm- und Dogmatik-Skill für Überraschende Klausel 305c: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `uklag-unterlassung-verbandsklage` | Norm- und Dogmatik-Skill für UKlaG Unterlassung Verbandsklage: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `unterlassungserklaerung-modifizieren` | Output- und Streit-Skill für Unterlassungserklärung Modifizieren: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `unternehmerverkehr-310-abs1` | Norm- und Dogmatik-Skill für Unternehmerverkehr 310 Abs. 1: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `unternehmerverkehr-schnellcheck` | Einstiegs- und Workflow-Skill für Unternehmerverkehr Schnellcheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `user-content-moderation` | Klausel-Spezialskill für User Content Moderation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vdug-abhilfeklage-agb-schnittstelle` | Norm- und Dogmatik-Skill für VDuG Abhilfeklage AGB Schnittstelle: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `verbraucherbesonderheiten-310-abs3` | Norm- und Dogmatik-Skill für Verbraucherbesonderheiten 310 Abs. 3: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `verbraucherfreundliche-fassung` | Output- und Streit-Skill für Verbraucherfreundliche Fassung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `verbraucherschutz-schnellcheck` | Einstiegs- und Workflow-Skill für Verbraucherschutz Schnellcheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `vereinsbedingungen` | Branchen-Spezialskill für Vereinsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `verfuegbarkeit-wartungsfenster` | Klausel-Spezialskill für Verfügbarkeit Wartungsfenster: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vergaberechtliche-vertragsbedingungen` | Branchen-Spezialskill für Vergaberechtliche Vertragsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `verhandlungs-playbook-agb` | Output- und Streit-Skill für Verhandlungs Playbook AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `verjaehrungsverkuerzung` | Klausel-Spezialskill für Verjaehrungsverkürzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `verkaufsbedingungen-b2b` | Branchen-Spezialskill für Verkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versicherung-avb` | Branchen-Spezialskill für Versicherung Avb: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versionsdiff-agb` | Output- und Streit-Skill für Versionsdiff AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `vertragsstrafe-309` | Norm- und Dogmatik-Skill für Vertragsstrafe 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `vertraulichkeit-klausel` | Klausel-Spezialskill für Vertraulichkeit Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vollmacht-vertretung` | Klausel-Spezialskill für Vollmacht Vertretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vorkasse-abschlag-sicherheit` | Klausel-Spezialskill für Vorkasse Abschlag Sicherheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `wartung-maintenance` | Branchen-Spezialskill für Wartung Maintenance: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `website-update-check` | Output- und Streit-Skill für Website Update Check: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `wesentliche-rechte-pflichten-307` | Norm- und Dogmatik-Skill für Wesentliche Rechte Pflichten 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `widerruf-umfeld-agb` | Klausel-Spezialskill für Widerruf Umfeld AGB: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `wohnraummiete-agb` | Branchen-Spezialskill für Wohnraummiete AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `zahlungsdienste-agb` | Branchen-Spezialskill für Zahlungsdienste AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `zahlungsmittel-chargeback` | Klausel-Spezialskill für Zahlungsmittel Chargeback: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `zahlungsverzug-mahnkosten` | Klausel-Spezialskill für Zahlungsverzug Mahnkosten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
