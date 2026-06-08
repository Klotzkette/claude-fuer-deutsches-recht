---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Patentrecht-Plugin. Erkennt Patentanmeldung, Erfindungsmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch, Nichtigkeit, Register- und Fristenfragen; schlägt passende Fachmodule aus diesem Plugin und bei Bedarf das Schwesterplugin patentrecherche vor."
---

# Patentrecht — Allgemein

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

## Qualitätsregel

Keine ungeprüften Registerstände und keine erfundenen Fundstellen. Wenn ein Ergebnis an Patentstatus, Jahresgebühr, Einspruch, nationaler Validierung oder UPC-Zuständigkeit hängt, live über amtliche Register oder frei zugängliche Quellen prüfen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
