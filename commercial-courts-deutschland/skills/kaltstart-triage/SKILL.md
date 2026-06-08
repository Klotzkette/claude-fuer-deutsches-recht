---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting für Commercial-Courts-Verfahren in Deutschland; erkennt Forum, Sprache, Streitwert, Parteivereinbarung, Case Management, Geheimnisschutz, Beweis, Transcript, Rechtsmittel und englischen Outputbedarf."
---

# Commercial Courts Deutschland — Allgemein

## Startprinzip

Beginne mit Orientierung, nicht mit Lehrbuch. Prüfe zuerst, ob der Fall überhaupt in einen deutschen Commercial Court oder eine Commercial Chamber gehört, ob Englisch wirksam gewählt werden kann und welche Prozesshandlung als nächstes ansteht.

## 90-Sekunden-Triage

| Punkt | Frage |
| --- | --- |
| Forum | Commercial Court am OLG, Commercial Chamber am LG, Schiedsgericht, normales Gericht oder Ausland? |
| Klausel | Gerichtsstand, Sprache, Eskalation, Schiedsvereinbarung, governing law, service agent? |
| Streit | M&A, Finance, Lieferkette, Joint Venture, Organhaftung, Tech, Bau/Anlage, Post-Closing? |
| Streitwert | Reicht die Schwelle nach Bundes-/Landesrecht und passt die sachliche Zuständigkeit? |
| Sprache | Englisch vollständig, teilweise, nur Schriftsätze, nur Hearing, BGH-Fortsetzung? |
| Nächster Akt | Claim, defence, CMC, evidence, confidentiality, transcript, settlement, appeal? |
| Output | Deutsch, Englisch, bilingual; Memo, pleading, order proposal, hearing script, board note? |

## Routing

| Lage | Primärskill | Ergänzung |
| --- | --- | --- |
| Unsicherheit Forum | `zustandigkeit-119b-gvg-check` | `forumwahl-commercial-court-vs-schiedsgericht` |
| Klausel für neuen Vertrag | `jurisdiction-clause-drafting-de-en` | `arbitration-clause-conflict-check` |
| Klage vorbereiten | `klageschrift-english-statement-of-claim` | `claim-intake-fakten-und-exhibits` |
| Verteidigung | `defence-answer-and-jurisdiction-objections` | `ruegelose-einlassung-und-sprache` |
| CMC/Termin | `case-management-conference` | `procedural-calendar-timetable-order` |
| Beweis/Anlagen | `evidence-map-zpo-vs-common-law` | `exhibits-translation-608-zpo` |
| Geheimnisse | `confidentiality-trade-secrets-273a-zpo` | `protective-measures-confidential-exhibits` |
| Wortprotokoll | `verbatim-transcript-613-zpo` | `hearing-script-english-advocacy` |
| Rechtsmittel | `appeal-and-revision-614-zpo` | `bgh-english-proceedings-184b-gvg` |
| Abschlusskontrolle | `redteam-commercial-court-qualitygate` | `glossary-commercial-court-de-en` |

## Antwortformat

**Short Procedural View**
- Forum: [...]
- Language: [...]
- Next procedural act: [...]
- Hard risk: [...]

**Recommended Workflow**
1. [...]
2. [...]
3. [...]

**Suggested Skills**
| Skill | Why now | Deliverable |
| --- | --- | --- |
| `...` | [...] | [...] |

## Quellenregel

Für Commercial Courts muss der aktuelle Stand des Bundesrechts und des jeweiligen Landesrechts live geprüft werden. Wenn unklar ist, ob ein Land den konkreten Commercial Court eingerichtet hat oder welche Spruchkörper zuständig sind, wird das ausdrücklich als Live-Check markiert.
