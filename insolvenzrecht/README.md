# Insolvenzrecht-Plugin


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akten demonstrieren dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Insolvenz- und sanierungsrechtliche Skills nach deutschem Recht (InsO, StaRUG, COVInsAG-Nachwirkungen). Zielgruppe: Insolvenzverwalter, beratende Rechtsanwälte (Insolvenz-/Sanierungsrecht), Geschäftsführer, Vorstände, Sanierungsberater, Wirtschaftsprüfer (IDW-S-11-/S-6-/S-9-Praxis).


## ⬇️ Arbeitsakte (separat)

Separate Arbeitsakte — **kein Teil des Plugins**, eigener Download:

| Akte | Direkt-Download |
| --- | --- |
| **fortbestehensprognose paragrafix gmbh** | [testakte-fortbestehensprognose-paragrafix-gmbh.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Insolvenzrecht (`insolvenzrecht`, dieses Plugin) | [insolvenzrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

### Arbeitsakte (separat)

Separate Arbeitsakte — **kein Teil des Plugins**, eigener Download:

| Akte | Direkt-Download |
| --- | --- |
| **LUMEN Studios (Insolvenz + Wirtschaftsstrafverfahren)** | [testakte-lumen-studios-insolvenz-strafverfahren.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |


### Zum Ausprobieren: Beispielakte (separat)

Separate Arbeitsakte — **kein Teil des Plugins**, eigener Download:

[testakte-beispielakte-edelholz-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beispielakte-edelholz-berlin.zip)

Fiktive Mandantsakte der Edelholz Manufaktur Berlin GmbH (Insolvenz-Schwelle) — geeignet für § 17-/§ 19-InsO-Prüfungen und Antragspflicht-Szenarien.


## Enthaltene Skills

| Skill | Zweck |
|---|---|
| `zahlungsunfaehigkeit-pruefung-17-inso` | Prüfung der Zahlungsunfähigkeit gem. § 17 InsO anhand BGH-Liquiditätsstatus (10%-/3-Wochen-Schwelle) |
| `ueberschuldung-pruefung-19-inso` | Zweistufige Überschuldungsprüfung gem. § 19 InsO: Fortbestehensprognose + insolvenzrechtlicher Überschuldungsstatus |
| `liquiditaetsvorschau-insolvenzrechtlich` | Rollierende 13-/26-/52-Wochen-Liquiditätsvorschau mit Ampel als Beweismittel für § 17 InsO und Fortbestehensprognose § 19 InsO; Excel-Export |
| `antragspflicht-15a-inso` | Höchstfrist nach § 15a InsO, Haftung bei Insolvenzverschleppung, Schutz Geschäftsführer/Vorstand |
| `glaeubigerantrag-pruefung` | Prüfung Zulässigkeit/Begründetheit eines Gläubigerantrags (§ 14 InsO), Glaubhaftmachung Forderung + Eröffnungsgrund |

## Abgrenzung zu den Schwester-Plugins

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Dieses Plugin `insolvenzrecht` ist **gerichtsfähig-formal** ausgerichtet: Es liefert die rechtlichen Subsumtionsbausteine und Beweismittel, wenn die Krise bereits eingetreten ist — Zeitpunkt der Zahlungsunfähigkeit, Überschuldungsstatus zum Stichtag, Antragspflichtfrist, Haftung Geschäftsleiter.

## Rechtlicher Rahmen (übergreifend)

- **InsO**: §§ 14, 15, 15a, 16, 17, 18, 19, 130, 131, 133, 142
- **StaRUG**: §§ 29 ff. (Restrukturierungsverfahren), § 102 (Hinweispflicht)
- **GmbHG**: § 64 a.F. (ersetzt durch § 15b InsO), § 30 (Auszahlungsverbot)
- **AktG**: § 92 Abs. 2 (Anzeigepflichten), § 93 (Sorgfaltspflicht)
- **HGB**: § 252 Abs. 1 Nr. 2 (going concern)
- **StGB**: §§ 283–283d (Bankrott, Verletzung der Buchführungspflicht), § 266a (Vorenthalten Arbeitsentgelt)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Lizenz

Doppellizenziert unter Apache License, Version 2.0 ODER MIT License, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`). Siehe `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT` und `NOTICE` im Repository-Wurzelverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 16 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Insolvenzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `anfechtungsrechte-pruefen` | Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. Prüfraster §§ 129 ff. InsO kongruente Deckung § 130 inkongruente Deckung § 131 vorsaetzliche Benachteiligung § 133 une... |
| `antragspflicht-15a-inso` | 'Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§ 823 Abs. 2 BGB iVm § 15a InsO) sowie das Zahlungsverbot nach § 15b InsO. Lädt, wenn Schlagwörter wie "Antragspflich... |
| `do-versicherung-manager-haftung` | Insolvenzverwalter verklagt Geschäftsführer und D&O-Versicherung soll Deckung prüfen oder Manager fragt nach Versicherungsschutz in der Krise. Prüfraster D&O-Versicherung Claims-made-Prinzip Schadensereignis vs. Anspruchserhebung. Insolv... |
| `forderungsanmeldung-glaeubiger-174-177-inso` | Gläubiger meldet Forderung im Insolvenzverfahren an §§ 174-177 InsO: Fristen Form Anlagen Rang § 39 InsO Vorsatz § 174 Abs. 2 InsO nachtraegliche Anmeldung § 177 InsO Prüfungstermin § 176 Bestreiten § 178 Tabelle § 179 InsO. Mit Musterte... |
| `glaeubigerantrag-pruefung` | Prüft Zulässigkeit und Begründetheit eines Gläubigerantrags auf Eröffnung des Insolvenzverfahrens nach § 14 InsO — sowohl aus Gläubigerperspektive (Antragstellung) als auch aus Schuldnerperspektive (Abwehrstrategien). Lädt, wenn ein Mand... |
| `glaeubigerausschuss-mitwirkung` | Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichten und Haftung. Prüfraster §§ 67 ff. InsO Gläubigerausschuss vorlaeufiger Gläubigerausschuss § 22a InsO Schwellenwerte... |
| `insolvenzgeld-165-sgb-iii` | Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzgeld-Anmeldungen. Prüfraster § 165 ff. SGB III Anspruchs-Voraussetzungen Arbeitsentgelt letzte drei Monate vor Insolven... |
| `insolvenzrecht-kaltstart-interview` | Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter / beratender Anwalt /... |
| `konzerninsolvenz-koordination` | Mehrere Gesellschaften eines Konzerns sind insolvent und Koordination der Verfahren muss geplant werden. Prüfraster Konzerninsolvenz §§ 269a-269i InsO Konzern-Gerichtsstand § 3a InsO Gruppen-Folgeverfahren § 3d InsO. Konzernbegriff § 18... |
| `liquiditaetsvorschau-insolvenzrechtlich` | Erstellt und bewertet die rollierende Liquiditätsvorschau als strukturierte Arbeitsgrundlage für insolvenzrechtliche Tatbestände nach § 17 InsO (Zahlungsunfähigkeit) und § 19 Abs. 2 InsO (Fortbestehensprognose). Lädt, wenn geprüft werden... |
| `mandat-triage-insolvenzrecht` | Eingangs-Abfrage für insolvenzrechtliche Mandate — Mandant ist Geschäftsführer mit Antragspflicht Gläubiger der Forderung anmelden will oder Arbeitnehmer der Insolvenzgeld beantragt. Klaert Mandantenrolle und Vorgang (Eroeffnungsantrag E... |
| `ueberschuldung-pruefung-19-inso` | Führt die zweistufige Überschuldungsprüfung gem. § 19 Abs. 2 InsO durch: Fortbestehensprognose (Stufe 1) und insolvenzrechtlicher Überschuldungsstatus auf Liquidationswertbasis (Stufe 2). Lädt, wenn Überschuldung geprüft, ein Überschuldu... |
| `uebertragende-sanierung-und-asset-deals` | Insolvenzverwalter will Geschäftsbetrieb verkaufen oder Investor kauft aus der Insolvenz und braucht Prüfung des Asset-Deals. Prüfraster uebertragende Sanierung Asset Deal im Regelverfahren Zustimmung Gläubigerausschuss § 160 InsO. Insol... |
| `vorsatzanfechtung-133-inso` | Workflow-Skill zu vorsatzanfechtung 133 inso. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `zahlungsunfaehigkeit-pruefung-17-inso` | Erstellt ein strukturiertes Prüfgutachten zum Eröffnungsgrund der Zahlungsunfähigkeit nach § 17 InsO. Berechnet den Liquiditätsstatus zum Stichtag, wendet das 10-%-/3-Wochen-Schema des BGH an und würdigt Indizien der Zahlungseinstellung.... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
