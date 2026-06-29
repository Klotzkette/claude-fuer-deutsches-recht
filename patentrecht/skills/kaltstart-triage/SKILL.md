---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Patentrecht-Plugin. Erkennt Patentanmeldung, Erfindungsmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch, Nichtigkeit, Register- und Fristenfragen; schlägt passende Fachmodule aus diesem Plugin und bei Bedarf das Schwesterplugin patentrecherche vor."
---

# Patentrecht — Allgemein

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Startprinzip

Beginne nicht mit einer Vorlesung. Lies die Unterlagen, sichere Fristen, ordne die Aktenart ein und wähle den passenden Arbeitsweg. Wenn Material fehlt, stelle genau die eine Rückfrage, ohne die der nächste Schritt falsch wäre.

## Stummer Upload

Wenn der Nutzer nur Dateien hochlädt:

1. **Frist zuerst:** Zustellung, Einspruch, Prüfungsbescheid, Abmahnfrist, Prioritätsjahr, Offenbarung, Messe, Launch, Lizenzdeadline.
2. **Material erkennen:** Erfindungsmeldung, Anspruchsentwurf, Beschreibung, Zeichnungen, Patentvolltext, Prüfungsbescheid, Registerauszug, Abmahnung, Claim Chart, Lizenzvertrag, Prior-Art-Liste, Term Sheet.
3. **Rechtsfrage bestimmen:** Anmeldung, Patentfähigkeit, Recherche, FTO, Verletzung, Verteidigung, Lizenz, Bestand, Register.
4. **Fachmodul routen:** zuerst einen Skill aus `patentrecht`; bei Datenbankrecherche zusätzlich `patentrecherche`.
5. **Erster Output:** Kurzbild, Risiken, fehlende Unterlagen, nächster Arbeitsschritt.

## 60-Sekunden-Intake

| Punkt | Frage |
| --- | --- |
| Ziel | Anmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch/Nichtigkeit, Portfolio? |
| Technik | Produkt, Verfahren, Vorrichtung, Software, Chemie, Biotech, Mechanik, Elektronik? |
| Material | Skizzen, Prototyp, Beschreibung, Anspruchsentwurf, Registerauszug, E-Mail, Produktdaten, Vertrag? |
| Frist | Priorität, Messe, Veröffentlichung, Abmahnung, Prüfungsbescheid, Einspruch, Closing? |
| Territory | DE, EP, Einheitspatent/UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei, Israel, China, nur DACH, weltweit? |
| Rolle | Patentanwalt, Rechtsanwalt, Unternehmen, Gründerteam, Investor, Verletzungsbeklagter? |
| Output | Memo, Claim Draft, Rückfragen, Claim Chart, Rechercheauftrag, Vertrag, Mandantenbrief? |

## Routing

| Lage | Primärskill | Ergänzung |
| --- | --- | --- |
| Rohe Erfindungsidee | `erfindungsmeldung-aufnahme-und-rueckfragen` | `patentanmeldung-anspruchsentwurf` |
| Anspruchsentwurf prüfen | `patentanmeldung-anspruchsentwurf` | `beschreibung-und-zeichnungen-pruefen` |
| Recherchebedarf | `stand-der-technik-recherche-workflow` | `patentrecherche/agentische-datenbank-recherche` |
| Neuheit/Erfindungshöhe | `neuheit-und-erfinderische-taetigkeit` | `patentrecht-redteam-qualitygate` |
| Launch/FTO | `freedom-to-operate-und-schutzbereich` | `rechtsstand-register-und-fristen` |
| Abmahnung | `abmahnung-patentverletzung-verteidigung` | `patentverletzung-claim-chart` |
| behauptete Vorbenutzung | `vorbenutzungsrecht-paragraph-12-patg` | Beweis- und Chronologiematrix |
| Lizenzvertrag | `patentlizenzvertrag-review` | `patentlizenzvertrag-de-en-drafting` |
| Erfinder-/ArbEG-Thema | `erfinderbenennung-und-arbeitnehmererfindung` | Vergütungs- und Rechtekette |
| Einspruch/Nichtigkeit | `einspruch-epa-und-nichtigkeit-bpatg` | `neuheit-und-erfinderische-taetigkeit` |
| UPC/Einheitspatent | `upc-verletzung-und-rechtsbestand` | `upc-widerruf-und-widerklage-revocation` |
| internationale Länderstrategie | `internationaler-patentrechts-und-laendercheck` | `pct-laenderstrategie-und-nationalphasen` |
| USA/UK/Kanada/Japan/Schweiz/Türkei/Israel | jeweiliger Länderskill | Local-Counsel-Fragenkatalog |
| Patentprozess/Eilverfahren | `patentprozess-einstweilige-verfuegung-de-upc` | `patentprozess-schutzschrift-und-caveat` |
| globale Revocation/Nichtigkeit | `loeschung-widerruf-nichtigkeit-global-route` | `patentprozess-kostensicherheit-und-budget` |

## Antwortformat

**Kurzbild**
- Arbeitsziel: [...]
- Frist/Risiko: [...]
- Sicherer Sachverhalt: [...]
- Offene technische Punkte: [...]

**Nächster Arbeitsweg**
1. [...]
2. [...]
3. [...]

**Passende Skills**
| Skill | Warum jetzt? | Ergebnis |
| --- | --- | --- |
| `...` | [...] | [...] |
