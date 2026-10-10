# 1. Reinigungsvergabe nach Verfahrensstand

Die Schrittcodes verbinden die unveränderte externe Workflow-Vorlage mit den installierbaren Skills. Nur den aktuell benötigten Skill öffnen; nicht alle zehn vollständig in denselben Arbeitskontext laden.

| Schritt | Skill | Ergebnis und Anschluss |
| --- | --- | --- |
| A1 | [a1-reinigungsauftrag-und-vergabeverfahren](../skills/a1-reinigungsauftrag-und-vergabeverfahren/SKILL.md) | Vergabeweg und Lose; weiter A2 |
| A2 | [a2-reinigungsleistung-und-mengen](../skills/a2-reinigungsleistung-und-mengen/SKILL.md) | Leistungsbeschreibung und LV; weiter A3 |
| A3 | [a3-eignung-wertung-reinigungsvertrag](../skills/a3-eignung-wertung-reinigungsvertrag/SKILL.md) | Eignung, Wertung, Vertrag; weiter A4 |
| A4 | [a4-unterlagen-und-preisblatt-abgleichen](../skills/a4-unterlagen-und-preisblatt-abgleichen/SKILL.md) | Geprüfte Unterlagen; weiter A5 |
| A5 | [a5-bekanntmachung-fristen-veroeffentlichen](../skills/a5-bekanntmachung-fristen-veroeffentlichen/SKILL.md) | Bekanntmachungsentwurf und Termine; weiter B1 |
| B1 | [b1-bewerbungen-angebote-nachfordern](../skills/b1-bewerbungen-angebote-nachfordern/SKILL.md) | Bewerberauswahl oder Angebotsprüfung; B1 erneut nach Angebotseingang, danach B3 |
| B2 | [b2-bieterfragen-ruegen-berichtigen](../skills/b2-bieterfragen-ruegen-berichtigen/SKILL.md) | Antwort oder Berichtigung; zurück zum betroffenen Schritt |
| B3 | [b3-angebote-verhandeln-werten-preispruefen](../skills/b3-angebote-verhandeln-werten-preispruefen/SKILL.md) | Verhandlung, Wertung, Preisaufklärung; weiter B4 |
| B4 | [b4-vorabinformation-zuschlag-uebergabe](../skills/b4-vorabinformation-zuschlag-uebergabe/SKILL.md) | Vorabinformation und Zuschlag; Übergabe an Betrieb erst nach Freigabe |
| B5 | [b5-nachpruefung-berlin-fortsetzen](../skills/b5-nachpruefung-berlin-fortsetzen/SKILL.md) | Erwiderung und Aktenvorlage; nach Entscheidung gezielt B2, B3 oder B4 |

## 2. Kein erneuter Kaltstart

Bei bekannter Rolle und vorhandenem Auftrag unmittelbar in dessen Fachschritt einsteigen. Eine Kammermitteilung führt direkt zu B5, eine Rüge zu B2, ein vorhandenes LV zur Prüfung A4. Bei einem Einzelaufruf nur die vorgelagerten Festlegungen nachziehen, die für das Arbeitsergebnis erforderlich sind.

## 3. Kontrollierte Übergaben

Ein Folgeschritt liest den übergebenen Stand und nur die dafür nötigen Belege. RUECKFRAGE bedeutet: Frage mit zuständiger Person, betroffener Entscheidung und Frist ausgeben, dann auf Antwort warten. Keine automatische Wiederholung. Nach Antwort nur abhängige Dokumente neu bearbeiten. UEBERGABEBEREIT ist keine Zeichnungs-, Versand- oder Zuschlagsfreigabe. Jede externe Handlung benötigt eine gesonderte bestätigte Befugnis.

Dateien müssen tatsächlich zugänglich sein. Ist der Export nicht möglich, vollständigen kopierbaren Text liefern. Nach zwei gescheiterten Abrufwegen offene Quelle benennen und unabhängige Teile fortsetzen. Eine Plattformstörung nicht durch heimlichen Wechsel des Einreichungskanals umgehen.

## 4. Übertragbare Vorlage

Die zehn eigenständigen Markdown-Assistenten bleiben unter [GVB Berlin](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/weitere-unterlagen/sektorenvergabe-gvb-berlin) unverändert verfügbar. Das Muster für andere Arbeitsabläufe ist die Trennung von Eingangsdaten, fachlicher Entscheidung, konkretem Dokument, offenen Punkten und nächstem Schritt. Nicht übertragbar ohne Neubearbeitung sind Vergabefristen, Rechtsquellen, Tarifvorgaben und Reinigungsanforderungen.
