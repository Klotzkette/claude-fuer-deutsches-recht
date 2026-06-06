---
name: orientierung-mandatsaufnahme-praktikabilitaet
description: "Einstiegs-Skill fuer NKR-Pruefauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welchem Cluster der weitere Pruefweg liegt. Liefert sofort einen Pruefpfad-Vorschlag und verweist auf die einschlaegigen Fachmodulen im Normenkontrollrat Nkr: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# NKR-Orientierung und Mandatsaufnahme

## Arbeitsbereich

Einstiegs-Skill fuer NKR-Pruefauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welchem Cluster der weitere Pruefweg liegt. Liefert sofort einen Pruefpfad-Vorschlag und verweist auf die einschlaegigen Fachmodulen. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es konkret

Allgemein-Skill als Einstieg in jedes NKR-Pruefmandat. Er nimmt einen unvorbereiteten Posteingang (Referentenentwurf, Formulierungshilfe, AVV-Entwurf, Verordnungsentwurf, parlamentarische Aenderung) und ordnet ihn in den Pruefzyklus des Nationalen Normenkontrollrats ein.

Ziel: in zwei Minuten wissen, welche der 36 anderen Skills im Plugin als naechstes zu greifen sind.

## Wann dieses Modul hilft / Kaltstart-Fragen

Anwendungsfall: Sekretariat hat einen Vorgang weitergeleitet, der NKR-Pruefung erfordert.

Eine einzige Rueckfrage:

> **Bitte nennen Sie kurz: (1) Vorhabenstitel und federfuehrendes Ressort, (2) Art des Vorhabens (Referentenentwurf / Formulierungshilfe / Kabinettsentwurf / Verordnung / parlamentarische Aenderung), (3) Frist, bis zu der die Stellungnahme vorliegen muss.**

Sind die drei Angaben vorhanden, sofort die Pruefskizze (siehe Ausgabeformat).

## Rechtlicher und methodischer Rahmen

- **NKRG** vom 14.08.2006 (BGBl. I S. 1866) in der jeweils geltenden Fassung
- **§§ 44, 45 GGO** (Pruefung der Gesetzesfolgen, Erfuellungsaufwand-Darstellung)
- **Handbuch der Rechtsfoermlichkeit (HdR)** als Drafting-Grundlage
- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR)

## Pruefraster / Schritt fuer Schritt

1. **Eingang triagieren**: Welcher Vorhabenstyp? Was ist die NKR-Befassungspflicht (§ 4 NKRG)?
2. **Federfuehrendes Ressort identifizieren**: BMJ / BMI / BMF / BMWK etc.
3. **Pruefumfang bestimmen** (Skill `nkr-pruefumfang-was-prueft-der-nkr-nicht`):
 - Pruefen: Methodik und Vollstaendigkeit der Erfuellungsaufwand-Darstellung, Nachvollziehbarkeit, Praktikabilitaet, Digitaltauglichkeit
 - **Nicht** pruefen: politische Zweckmaessigkeit oder Zielwahl
4. **Phase im Verfahrensgang** (Skill `nkr-verfahrensgang-referentenentwurf-bis-bundestag`):
 - Referentenentwurf vor Ressortabstimmung / vor Kabinett / Formulierungshilfe / parlamentarische Aenderung
5. **Frist klaeren**: Standardfrist nach NKRG / GGO; bei Eilbeduerftigkeit gekuerzte Frist
6. **Cluster waehlen**:
 - Erfuellungsaufwand-Berechnung -> Cluster B
 - Pruefraster anwenden -> Cluster C
 - Stellungnahme entwerfen -> Cluster D
 - Spezialthema (Digital, EU, KMU) -> Cluster E

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Erfuellungsaufwand nicht oder unvollstaendig dargestellt
- Methodik nicht nachvollziehbar
- Alternativen nicht geprueft
- One-in-one-out-Bilanz fehlt
- Digitaltauglichkeit nicht thematisiert
- Mittelstandsbelastung nicht adressiert
- Evaluierungsklausel fehlt
- Praktikabilitaet im Vollzug nicht plausibel

## Trade-off-Matrix

| Befund | Folge fuer Stellungnahme |
|---|---|
| Methodik vollstaendig, Ergebnis plausibel | "Der NKR hat keine Einwaende." |
| Methodik luckenhaft, korrigierbar | Nachforderung an Ressort |
| Methodik fehlt grundlegend | Negative Stellungnahme, Mahnung |
| Politisch problematisch, methodisch sauber | NKR aeussert sich nicht zur Politik |

## Mustertexte / Stellungnahme-Bausteine

Erst-Antwort an Sekretariat (intern):

> "Vorhaben **[Titel]** des **[Ressort]** vom **[Datum]**, Frist **[TT.MM.JJJJ]**. Pruefpfad: Eingangstriage -> Erfuellungsaufwand-Berechnung -> Pruefraster -> Stellungnahme. Spezialthemen: [Digital / EU / KMU / Vollzug]. Federfuehrung in der Pruefung: [Referent/in]. Erster Stellungnahme-Entwurf bis [Datum]."

## Typische Fehler in Ressort-Entwuerfen

- "Kein nennenswerter Erfuellungsaufwand" ohne Begruendung
- Fallzahlen aus dem Lehrbuch statt aus Statistik
- Alternative "Verzicht auf Regelung" gar nicht erwogen
- One-in-one-out: "Wird im weiteren Verfahren geprueft"
- Digitaltauglichkeit: nicht erwaehnt

## Querverweise

- `nkr-aufgabe-und-kompetenz-nkrg` — rechtlicher Rahmen
- `nkr-pruefumfang-was-prueft-der-nkr-nicht` — Abgrenzung
- `nkr-verfahrensgang-referentenentwurf-bis-bundestag` — Phasen
- `nkr-stellungnahme-aufbau-und-format` — Drafting der Stellungnahme
- `legistik-werkstatt/legistik-auftragsaufnahme` — Gegenstueck aus Ressortsicht

## Quellen Stand 06/2026

- NKRG vom 14.08.2006 (BGBl. I S. 1866) in der jeweils geltenden Fassung
- §§ 44, 45 GGO
- Handbuch der Rechtsfoermlichkeit (HdR) in der jeweils geltenden Fassung
- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR)
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren ueber [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)
