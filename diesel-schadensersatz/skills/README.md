# Skills

[Plugin-README](../README.md) | [Repository-Start](../../README.md) | [Download-Index](../../ASSET_INDEX.md) | [Schnellstart](../diesel-schadensersatz-schnellstart.md) | [Werkstatt](../diesel-schadensersatz-werkstatt.md) | [Plugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/diesel-schadensersatz.zip)

Die 21 Skills bilden einen durchgehenden Diesel-Schadensersatz-Workflow. Bei einem neuen Fall startet das Plugin grundsätzlich mit Skill 01; nach abgeschlossenem Intake routet Skill 06 in den passenden Fachpfad. Fertige Klagen und Repliken laufen vor der tatsächlichen beA-Einreichung stets über Skill 21.

Jeder Skill beginnt sein Ergebnis mit demselben [Kanzlei-Arbeitskopf](../assets/templates/kanzlei-arbeitskopf.md). Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau ein nächster Schritt bleiben dadurch sofort sichtbar; der Kopf ist Kontrollansicht und gehört nie in Schriftsatz, Anlage oder Exportdatei.

## 1. Aktenaufnahme

| Nr. | Skill |
|---:|---|
| 01 | [Kaltstart und Aktenaufnahme](./01-kaltstart-aktenaufnahme/SKILL.md) |
| 02 | [Kaufvertrag, Zahlungen und Belege](./02-kaufvertrag-zahlungen-belege/SKILL.md) |
| 03 | [Chronologie, Rückruf und Fristen](./03-chronologie-rueckruf-fristen/SKILL.md) |
| 04 | [Betroffenheit, Motor und KBA-Rückruf](./04-betroffenheit-motor-kba-rueckruf/SKILL.md) |
| 05 | [Abschalteinrichtung, Thermofenster und Update](./05-abschalteinrichtung-thermofenster-update/SKILL.md) |

## 2. Strategie und Vorprozess

| Nr. | Skill |
|---:|---|
| 06 | [Anspruchstriage und Fallstrategie](./06-anspruchstriage-fallstrategie/SKILL.md) |
| 07 | [Verjährung und Restschadensersatz](./07-verjaehrung-restschadensersatz/SKILL.md) |
| 08 | [Schadenshöhe und Nutzungsentschädigung](./08-schadenshoehe-nutzungsentschaedigung/SKILL.md) |
| 09 | [Anspruchsschreiben und Zugangsnachweis](./09-anspruchsschreiben-zugangsnachweis/SKILL.md) |
| 10 | [Vertretung, Prozessfinanzierung und Abtretung](./10-vertretung-prozessfinanzierung-abtretung/SKILL.md) |
| 11 | [Musterfeststellung, VDuG und Kollektivklage](./11-musterfeststellung-vdug-kollektivklage/SKILL.md) |
| 12 | [Finanzierungswiderruf und verbundenes Geschäft](./12-finanzierungswiderruf-verbundgeschaeft/SKILL.md) |

## 3. Klage

| Nr. | Skill |
|---:|---|
| 13 | [Klageweg, Streitwert und Zuständigkeit](./13-klageweg-streitwert-zustaendigkeit/SKILL.md) |
| 14 | [Klage auf Rückabwicklung Zug um Zug](./14-klage-rueckabwicklung-zug-um-zug/SKILL.md) |
| 15 | [Klage auf Differenzschaden](./15-klage-differenzschaden/SKILL.md) |
| 16 | [Klage über beA/EGVP einreichen](./16-klage-einreichen-bea-egvp/SKILL.md) |

## 4. Prozess und Abschluss

| Nr. | Skill |
|---:|---|
| 17 | [Klageerwiderung, Replik und Beweis](./17-klageerwiderung-replik-beweis/SKILL.md) |
| 18 | [Vergleich, Abfindung und Nachzahlung](./18-vergleich-abfindung-nachzahlung/SKILL.md) |
| 19 | [Kosten, Vollstreckung und Monitoring](./19-kosten-vollstreckung-monitoring/SKILL.md) |

## 5. Querschnitt

| Nr. | Skill |
|---:|---|
| 20 | [E-Akte-Export und Kanzleisoftware](./20-eakte-export-kanzleisoftware/SKILL.md) |

## 6. Versandabschluss

| Nr. | Skill |
|---:|---|
| 21 | [Schriftsatz und Anlagen beA-versandfertig machen](./21-bea-versandfertig-schriftsatz-anlagen/SKILL.md) |

Standardroute für Gerichtsdokumente: Fachentwurf aus Skill 14, 15 oder 17 -> Skill 21 für Endfassung, Anlagenfolge, Stempel, Dateinamen und Paketprüfung -> Skill 16 für Signatur, tatsächliche Übermittlung und gerichtliche Eingangsbestätigung.

Die repositoryweite Gesamtübersicht aller installierbaren Skills steht in [`SKILLS.md`](../../SKILLS.md); die vollständige Dieselgate-Liste bleibt auf dieser Seite unmittelbar verfügbar.
