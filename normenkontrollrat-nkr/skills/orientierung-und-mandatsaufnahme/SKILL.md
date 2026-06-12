---
name: orientierung-und-mandatsaufnahme
description: "Einstiegs-Skill für NKR-Prüfauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welchem Cluster der weitere Prüfweg liegt. Liefert sofort einen Pr"
---

# NKR-Orientierung und Mandatsaufnahme

## Worum geht es konkret

Allgemein-Skill als Einstieg in jedes NKR-Prüfmandat. Er nimmt einen unvorbereiteten Posteingang (Referentenentwurf, Formulierungshilfe, AVV-Entwurf, Verordnungsentwurf, parlamentarische Änderung) und ordnet ihn in den Prüfzyklus des Nationalen Normenkontrollrats ein.

Ziel: in zwei Minuten wissen, welche der 36 anderen Skills.

## Wann dieses Modul hilft / Kaltstart-Fragen

Anwendungsfall: Sekretariat hat einen Vorgang weitergeleitet, der NKR-Prüfung erfordert.

Eine einzige Rueckfrage:

> **Bitte nennen Sie kurz: (1) Vorhabenstitel und federfuehrendes Ressort, (2) Art des Vorhabens (Referentenentwurf / Formulierungshilfe / Kabinettsentwurf / Verordnung / parlamentarische Änderung), (3) Frist, bis zu der die Stellungnahme vorliegen muss.**

Sind die drei Angaben vorhanden, sofort die Prüfskizze (siehe Ausgabeformat).

## Rechtlicher und methodischer Rahmen

- **NKRG** vom 14.08.2006 (BGBl. I S. 1866) in der jeweils geltenden Fassung
- **§§ 44, 45 GGO** (Prüfung der Gesetzesfolgen, Erfuellungsaufwand-Darstellung)
- **Handbuch der Rechtsfoermlichkeit (HdR)** als Drafting-Grundlage
- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR)

## Prüfraster / Schritt für Schritt

1. **Eingang triagieren**: Welcher Vorhabenstyp? Was ist die NKR-Befassungspflicht (§ 4 NKRG)?
2. **Federfuehrendes Ressort identifizieren**: BMJ / BMI / BMF / BMWK etc.
3. **Prüfumfang bestimmen** (Skill `nkr-pruefumfang-was-prueft-der-nkr-nicht`):
 - Prüfen: Methodik und Vollstaendigkeit der Erfuellungsaufwand-Darstellung, Nachvollziehbarkeit, Praktikabilitaet, Digitaltauglichkeit
 - **Nicht** prüfen: politische Zweckmaessigkeit oder Zielwahl
4. **Phase im Verfahrensgang** (Skill `nkr-verfahrensgang-referentenentwurf-bis-bundestag`):
 - Referentenentwurf vor Ressortabstimmung / vor Kabinett / Formulierungshilfe / parlamentarische Änderung
5. **Frist klären**: Standardfrist nach NKRG / GGO; bei Eilbeduerftigkeit gekuerzte Frist
6. **Cluster waehlen**:
 - Erfuellungsaufwand-Berechnung -> Cluster B
 - Prüfraster anwenden -> Cluster C
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

| Befund | Folge für Stellungnahme |
|---|---|
| Methodik vollstaendig, Ergebnis plausibel | "Der NKR hat keine Einwaende." |
| Methodik luckenhaft, korrigierbar | Nachforderung an Ressort |
| Methodik fehlt grundlegend | Negative Stellungnahme, Mahnung |
| Politisch problematisch, methodisch sauber | NKR aeussert sich nicht zur Politik |

## Mustertexte / Stellungnahme-Bausteine

Erst-Antwort an Sekretariat (intern):

> "Vorhaben **[Titel]** des **[Ressort]** vom **[Datum]**, Frist **[TT.MM.JJJJ]**. Prüfpfad: Eingangstriage -> Erfuellungsaufwand-Berechnung -> Prüfraster -> Stellungnahme. Spezialthemen: [Digital / EU / KMU / Vollzug]. Federfuehrung in der Prüfung: [Referent/in]. Erster Stellungnahme-Entwurf bis [Datum]."

## Typische Fehler in Ressort-Entwuerfen

- "Kein nennenswerter Erfuellungsaufwand" ohne Begruendung
- Fallzahlen aus dem Lehrbuch statt aus Statistik
- Alternative "Verzicht auf Regelung" gar nicht erwogen
- One-in-one-out: "Wird im weiteren Verfahren geprueft"
- Digitaltauglichkeit: nicht erwaehnt

## Quellen Stand 06/2026

- NKRG vom 14.08.2006 (BGBl. I S. 1866) in der jeweils geltenden Fassung
- §§ 44, 45 GGO
- Handbuch der Rechtsfoermlichkeit (HdR) in der jeweils geltenden Fassung
- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR)
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren über [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)
