---
name: orientierung-mandatsaufnahme-praktikabilitaet
description: "Orientierung Mandatsaufnahme Praktikabilitaet: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Orientierung Mandatsaufnahme Praktikabilitaet

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Orientierung Mandatsaufnahme Praktikabilitaet** im Plugin Normenkontrollrat (NKR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nkr-orientierung-und-mandatsaufnahme` | Einstiegs-Skill fuer NKR-Pruefauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welchem Cluster der weitere Pruefweg liegt. Liefert sofort einen Pruefpfad-Vorschlag und verweist auf die einschlaegigen Fachmodulen. |
| `nkr-praktikabilitaet-vollzug-test` | Praktikabilitaetstest fuer den Vollzug. Prueft ob die Regelung von Behoerden und Adressaten ueberhaupt leistbar ist. Faktoren Personalbedarf IT-Voraussetzungen Datenverfuegbarkeit Schulungserfordernisse Vollzugskaskaden Konnexitaet Konfliktloesung mit Adressaten. Mit Mustertexten zur Vollzugskritik und Standardfragen an das federfuehrende Ressort. |

## Arbeitsweg

Im Plugin Normenkontrollrat (NKR) gilt für **Orientierung Mandatsaufnahme Praktikabilitaet**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nkr-orientierung-und-mandatsaufnahme`

**Fokus:** Einstiegs-Skill fuer NKR-Pruefauftraege. Klaert in einer einzigen knappen Rueckfrage was geprueft werden soll (Referentenentwurf Formulierungshilfe Verordnungsentwurf) welches Ressort federfuehrend ist welche Fristen gelten und in welchem Cluster der weitere Pruefweg liegt. Liefert sofort einen Pruefpfad-Vorschlag und verweist auf die einschlaegigen Fachmodulen.

# NKR-Orientierung und Mandatsaufnahme

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

## 2. `nkr-praktikabilitaet-vollzug-test`

**Fokus:** Praktikabilitaetstest fuer den Vollzug. Prueft ob die Regelung von Behoerden und Adressaten ueberhaupt leistbar ist. Faktoren Personalbedarf IT-Voraussetzungen Datenverfuegbarkeit Schulungserfordernisse Vollzugskaskaden Konnexitaet Konfliktloesung mit Adressaten. Mit Mustertexten zur Vollzugskritik und Standardfragen an das federfuehrende Ressort.

# NKR-Praktikabilitaet im Vollzug

## Worum geht es konkret

Eine Regelung kann methodisch sauber begruendet sein und dennoch im Vollzug **nicht praktikabel** sein: Behoerden ueberfordert, IT-Systeme nicht vorhanden, Daten nicht verfuegbar, Adressaten ueberfordert. Der NKR prueft Praktikabilitaet als Standardelement.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Vorhaben mit hohem Verwaltungsaufwand
- Vorhaben mit IT-Voraussetzungen
- Vorhaben mit Konnexitaet (Pflichten fuer Laender / Kommunen)
- Vorhaben mit komplexen Sanktionen
- Vorhaben mit kurzen Umsetzungsfristen

Rueckfrage nur wenn unklar: *"Welche Stelle vollzieht — Bundesbehoerde, Landesbehoerde, Kommune, Gericht?"*

## Rechtlicher und methodischer Rahmen

- **§ 44 GGO** — Folgen fuer Vollzug
- **NKRG** § 4 — methodische Pruefung umfasst auch Praktikabilitaet
- **Leitfaden BMI / NKR** — Praktikabilitaetspruefung
- **Art. 83-87 GG** — Vollzugskompetenzen
- **Art. 104a GG, Konnexitaetsverbot** (Verfassungen der Laender)

## Pruefraster / Schritt fuer Schritt

### 1. Vollzugskaskade

- Wer fuehrt das Gesetz aus?
- Bund / Land / Kommune / Gericht?
- Welche Behoerde konkret?
- Welche Hilfskoerperschaften?

### 2. Personalbedarf

- Stellenbedarf je Behoerde
- Qualifikation
- Schulungserfordernis
- Stellenfinanzierung

### 3. IT-Voraussetzungen

- Welche Systeme existieren?
- Welche muessen entwickelt werden?
- Schnittstellen zu bestehenden Verfahren?
- Datenschutz und Informationssicherheit

### 4. Datenverfuegbarkeit

- Welche Daten brauchen Behoerden?
- Werden sie automatisiert geliefert oder von Adressaten beigebracht?
- Was passiert, wenn Daten unvollstaendig sind?

### 5. Konfliktloesung

- Wie werden Streitigkeiten zwischen Adressat und Behoerde geloest?
- Rechtsschutz angemessen?
- Aufschiebende Wirkung sinnvoll?

### 6. Konnexitaet

- Werden Laender / Kommunen verpflichtet?
- Konnexitaetsprinzip beachtet?

### 7. Pilotierung / Inkrafttreten

- Hinreichende Umsetzungszeit?
- Stufeneinfuehrung sinnvoll?

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Vollzugskaskade nicht beschrieben
- Personalbedarf nicht beziffert
- IT-Voraussetzungen "vorhanden" ohne Pruefung
- Datenfluss nicht beschrieben
- Konnexitaet ignoriert
- Inkrafttretensfrist zu kurz fuer realistische Umsetzung
- Rechtsschutz unklar

## Trade-off-Matrix

| Praktikabilitaetsdimension | Plus | Minus |
|---|---|---|
| Personal | Bedarf beziffert | "im Rahmen vorhandener Mittel" |
| IT | bestehende Systeme genutzt | Neuentwicklung ohne Zeitplan |
| Daten | automatisierte Erhebung | manuelle Abfrage |
| Frequenz | jaehrlich | monatlich pauschal |
| Sanktion | abgestuft, dialogisch | maximal pauschal |
| Inkrafttreten | gestaffelt | Stichtag ohne Vorlauf |
| Konnexitaet | adressiert | ignoriert |

## Mustertexte / Stellungnahme-Bausteine

- "Der NKR weist darauf hin, dass der Vollzug bei [Behoerde] erheblichen Personalmehrbedarf erfordert. Die Stellenanforderung wird im Ressortentwurf nicht beziffert."
- "Der NKR haelt die vorgesehene Inkrafttretensfrist von [X] Monaten fuer zu kurz, um die notwendige IT-Anpassung bei [Behoerde] sicherzustellen. Eine Verlaengerung auf [Y] Monate erscheint angemessen."
- "Der NKR weist darauf hin, dass die Pflicht fuer Kommunen die Frage der Konnexitaet (Art. 104a Abs. 1 GG, Landesverfassungen) aufwirft. Eine ausgleichende Regelung ist im Vorhaben nicht vorgesehen."
- "Der NKR begruesst die ressortseitige Pruefung der Vollzugspraktikabilitaet und die transparente Darstellung des Personalmehrbedarfs."

## Typische Fehler in Ressort-Entwuerfen

- "Vollzug erfolgt im Rahmen vorhandener Mittel" ohne Pruefung
- "IT-Systeme sind vorhanden" ohne Konkretisierung
- Konnexitaet ignoriert
- "Inkrafttreten am Tag nach Verkuendung" trotz IT-Erfordernis
- "Vorhandene Behoerden uebernehmen" ohne Personalrechnung

## Querverweise

- `nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung`
- `nkr-verhaeltnismaessigkeit-aus-nkr-sicht`
- `nkr-digital-anschlussfaehigkeit-tauglich`
- `nkr-evaluierung-befristung-sunset-klausel`
- `legistik-werkstatt/inkrafttreten-uebergangsrecht`

## Quellen Stand 06/2026

- § 44 GGO
- Art. 83-87, 104a GG
- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4
- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR)
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren ueber [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)
