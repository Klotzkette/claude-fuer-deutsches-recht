---
name: stellungnahme-evaluationsklausel
description: "Stellungnahme Evaluationsklausel: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Stellungnahme Evaluationsklausel

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Stellungnahme Evaluationsklausel** im Plugin Normenkontrollrat (NKR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nkr-stellungnahme-evaluationsklausel-vorschlag` | Fachmodul fuer den NKR-Empfehlungs-Baustein Evaluierungsklausel. Liefert Vorlage Klausel-Text Indikatorliste Frist-Vorschlag Berichtsadressat Konkretisierung der Pflichten und Standard-Argumentation warum die Klausel noetig ist. Mit konkreten Bausteinen fuer die Stellungnahme. |
| `nkr-stellungnahme-formulierungshilfe-vs-referentenentwurf` | Behandlung von Formulierungshilfen der Bundesregierung an Koalitionsfraktionen im Vergleich zu Referentenentwuerfen. Beschreibt die Umgehungsproblematik die faktische NKR-Befassung die methodischen Besonderheiten der Formulierungshilfe (oft kein vollstaendiger Begruendungstext) und die Stellungnahme-Konsequenzen. Mit Mahntexten und konstruktiver Vorgehensbeschreibung. |

## Arbeitsweg

Im Plugin Normenkontrollrat (NKR) gilt für **Stellungnahme Evaluationsklausel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nkr-stellungnahme-evaluationsklausel-vorschlag`

**Fokus:** Fachmodul fuer den NKR-Empfehlungs-Baustein Evaluierungsklausel. Liefert Vorlage Klausel-Text Indikatorliste Frist-Vorschlag Berichtsadressat Konkretisierung der Pflichten und Standard-Argumentation warum die Klausel noetig ist. Mit konkreten Bausteinen fuer die Stellungnahme.

# NKR-Stellungnahme — Vorschlag einer Evaluationsklausel

## Worum geht es konkret

Empfehlung einer Evaluationsklausel ist eine der haeufigsten konkreten Empfehlungen des NKR. Dieser Skill liefert die Standardformulierungen, Indikatorenkataloge und Begruendungsbausteine.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Vorhaben ohne Evaluationsklausel
- Vorhaben mit unzureichender Klausel
- Hohe Wirksamkeitsunsicherheit
- Hoher Erfuellungsaufwand (> 1 Mio EUR p.a.)

Keine Rueckfrage noetig, wenn Vorhaben vorliegt.

## Rechtlicher und methodischer Rahmen

- **§ 44 GGO** — Pflicht zur Evaluierungsbestimmung
- **NKRG** § 4, § 7
- **Konzept zur Evaluierung neuer Regelungsvorhaben** der Bundesregierung
- **Leitfaden BMI / NKR** — Evaluierungsmodul

## Pruefraster / Schritt fuer Schritt

1. **Frist** waehlen — 3, 5 oder 10 Jahre (siehe Skill `nkr-evaluierung-befristung-sunset-klausel`)
2. **Adressat** bestimmen — meist Bundestag
3. **Indikatoren** auswaehlen
4. **Berichtspflicht** (Termin, Form, Inhalt)
5. **Folgen** offen lassen oder konkretisieren

## Standard-Indikatorenliste

- **Fallzahl** tatsaechlich vs. Schaetzung
- **Erfuellungsaufwand** tatsaechlich vs. Schaetzung
- **Zielereichung** (qualitativ und quantitativ)
- **Unbeabsichtigte Folgen** (Vermeidungs- oder Ausweichverhalten)
- **Verwaltungspraxis** (Kapazitaeten, Bearbeitungszeiten)
- **Digitalisierungs-Stand** der Umsetzung
- **KMU-Belastung** tatsaechlich
- **Vollzugsdefizite**
- **Bekanntheitsgrad** der Regelung in der Adressatengruppe

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Keine Evaluationsklausel
- Klausel ohne Indikatoren ("wird zu gegebener Zeit ausgewertet")
- Klausel ohne Frist
- Klausel ohne Adressat
- Klausel mit Indikatoren ohne Methodik

## Trade-off-Matrix

| Vorhabenstyp | Empfohlene Frist |
|---|---|
| Standard mit Aufwand > 1 Mio EUR p.a. | 5 Jahre |
| Aufwand > 100 Mio EUR p.a. | 3 Jahre |
| Eingriffsregelung sensibel | 3 Jahre |
| Pilotvorhaben | 3 Jahre + Befristung |
| Foerderprogramm | nach Programmlaufzeit |

## Mustertexte / Stellungnahme-Bausteine

### Empfehlung in der Stellungnahme

> "Der NKR empfiehlt, eine Evaluierungsklausel aufzunehmen, die [3 / 5] Jahre nach Inkrafttreten dieses Gesetzes die tatsaechlichen Auswirkungen anhand der Indikatoren Fallzahl, Erfuellungsaufwand, Zielereichung und unbeabsichtigte Folgen ueberprueft. Der Bericht ist dem Bundestag vorzulegen."

### Argumentationsbausteine

- "Eine Evaluierungsklausel ist angesichts der Hoehe des Erfuellungsaufwands und der Wirksamkeitsunsicherheit aus Sicht des NKR geboten."
- "Die Evaluierung soll insbesondere belegen, ob die [angenommene] Fallzahl und der [angenommene] Erfuellungsaufwand tatsaechlich erreicht werden."
- "Die Indikatoren sollen so gewaehlt sein, dass eine spaetere Anpassung des Gesetzes auf einer methodisch tragfaehigen Datengrundlage erfolgen kann."

### Klausel-Vorlage (in Begruendung / Anlage)

> *§ [X] Evaluierung*
>
> *(1) Das Bundesministerium [Federfuehrer] berichtet dem Deutschen Bundestag bis zum [TT.MM.JJJJ] ueber die Anwendung und Wirksamkeit dieses Gesetzes.*
>
> *(2) Der Bericht enthaelt insbesondere Aussagen zu*
> *1. der tatsaechlichen Fallzahl der nach diesem Gesetz Verpflichteten,*
> *2. dem tatsaechlichen jaehrlich laufenden Erfuellungsaufwand fuer Buerger, Wirtschaft und Verwaltung sowie dem einmaligen Umstellungsaufwand,*
> *3. der Zielereichung im Sinne von [Konkretisierung des Gesetzeszwecks],*
> *4. unbeabsichtigten Folgen, insbesondere Ausweich- und Vermeidungsverhalten,*
> *5. der Vollzugspraxis bei den zustaendigen Behoerden,*
> *6. den Auswirkungen auf kleine und mittlere Unternehmen, sowie*
> *7. Vorschlaegen zur Anpassung dieses Gesetzes.*

## Typische Fehler in Ressort-Entwuerfen

- "Eine Evaluierung erfolgt nach Inkrafttreten." — kein Termin, keine Indikatoren
- Klausel mit Frist, aber ohne Berichtspflicht
- Indikatoren nur qualitativ
- Bericht "an die Bundesregierung" statt an den Bundestag

## Querverweise

- `nkr-evaluierung-befristung-sunset-klausel`
- `nkr-evaluation-und-jahresbericht`
- `nkr-stellungnahme-ergebnis-und-empfehlung`
- `nkr-fallzahlen-schaetzung-bandbreiten`
- `legistik-werkstatt/inkrafttreten-uebergangsrecht`

## Quellen Stand 06/2026

- § 44 GGO
- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4, § 7
- Konzept zur Evaluierung neuer Regelungsvorhaben der Bundesregierung (jeweils aktuelle Fassung)
- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR)
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren ueber [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)

## 2. `nkr-stellungnahme-formulierungshilfe-vs-referentenentwurf`

**Fokus:** Behandlung von Formulierungshilfen der Bundesregierung an Koalitionsfraktionen im Vergleich zu Referentenentwuerfen. Beschreibt die Umgehungsproblematik die faktische NKR-Befassung die methodischen Besonderheiten der Formulierungshilfe (oft kein vollstaendiger Begruendungstext) und die Stellungnahme-Konsequenzen. Mit Mahntexten und konstruktiver Vorgehensbeschreibung.

# NKR-Formulierungshilfe vs. Referentenentwurf

## Worum geht es konkret

Formulierungshilfen der Bundesregierung an Koalitionsfraktionen sind ein parlamentarisch eingespieltes Instrument. Sie umgehen formal die regulaere Ressortabstimmung — und damit auch die foermliche NKR-Befassungspflicht. Die Praxis hat sich aber so entwickelt, dass der NKR auch bei Formulierungshilfen befasst wird (faktisch).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Vorgang wird als "Formulierungshilfe" gekennzeichnet
- Inhaltlich entspricht es einem Referentenentwurf
- NKR wird informell oder formell um Stellungnahme gebeten
- Politisch heikles Vorhaben mit knapper Frist

Rueckfrage nur wenn unklar: *"Liegt eine Formulierungshilfe der Bundesregierung an die Koalitionsfraktionen vor oder ein formaler Referentenentwurf?"*

## Rechtlicher und methodischer Rahmen

- **NKRG** § 4 — Befassungspflicht (formal nur fuer Regierungsvorhaben)
- **GGO** § 62 — Befassungspflicht vor Kabinett
- **GO BT** §§ 75 ff. — Initiativen aus der Mitte des Bundestages
- **Praxis** — faktische NKR-Beteiligung bei Formulierungshilfen
- **NKR-Jahresbericht** — wiederholte Mahnungen zur Umgehungsproblematik

## Pruefraster / Schritt fuer Schritt

### 1. Identifikation

- Wird das Vorhaben als "Formulierungshilfe" bezeichnet?
- Wer ist der formale Initiator (Fraktionen) und materielle Initiator (Ressort)?
- Welcher Inhalt — entspricht es einem Referentenentwurf?

### 2. NKR-Befassung

- Formelle Pflicht? -> nein (Initiative aus der Mitte des BT)
- Faktische Praxis? -> ja, in der Regel wird der NKR informell oder formell befasst
- Ggf. Anhoerung im Ausschuss als formales Aequivalent

### 3. Methodische Besonderheiten

- Begruendungstext oft luckenhaft
- Erfuellungsaufwand-Darstellung haeufig unvollstaendig
- Methodik kann unklar sein

### 4. Stellungnahme-Konsequenz

- Hinweis auf Umgehung der formalen Beteiligung
- Methodischer Standard wie bei Referentenentwurf
- Empfehlung an Bundestag, Erfuellungsaufwand-Darstellung nachzuziehen

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Formulierungshilfe ohne Erfuellungsaufwand-Darstellung
- Verkuerzte Fristen
- Gezielte Umgehung der NKR-Befassung
- Politisch motivierte Eilbeduerftigkeit
- Wiederholte Umgehungspraxis (-> Jahresbericht)

## Trade-off-Matrix

| Konstellation | NKR-Position |
|---|---|
| Formulierungshilfe mit vollstaendiger Begruendung | normale Pruefung |
| Formulierungshilfe mit unvollstaendiger Begruendung | Mahnung, Empfehlung zur Nachbesserung |
| Eilfall mit sachlicher Begruendung | knappe Stellungnahme |
| Eilfall ohne sachliche Begruendung | Mahnung, Jahresbericht |

## Mustertexte / Stellungnahme-Bausteine

- "Der NKR ist mit dem Vorhaben in Form einer Formulierungshilfe der Bundesregierung an die Koalitionsfraktionen befasst worden. Die foermliche Befassungspflicht nach NKRG ist insoweit zwar nicht ausgeloest, der NKR nimmt jedoch in Wahrnehmung seiner Aufgabe Stellung."
- "Der NKR weist darauf hin, dass die mit der Formulierungshilfe vorgesehene Regelung gemaess Inhalt und Umfang einem Referentenentwurf entspricht und sich deshalb an den methodischen Anforderungen fuer Regierungsentwuerfe messen lassen muss."
- "Der NKR empfiehlt, die im Rahmen der Formulierungshilfe noch nicht vollstaendige Darstellung des Erfuellungsaufwands im weiteren Beratungsverlauf des Bundestages durch die Bundesregierung zu ergaenzen."
- "Der NKR wird auf das Phaenomen der wiederholten Inanspruchnahme von Formulierungshilfen ohne vollstaendige methodische Darstellung in seinem naechsten Jahresbericht eingehen."

## Typische Fehler in Ressort-Entwuerfen / Formulierungshilfen

- "Formal nur eine Empfehlung an die Fraktionen"
- "Erfuellungsaufwand-Darstellung erfolgt im weiteren Verfahren"
- "NKR-Befassung nicht erforderlich, da Initiative aus der Mitte"
- Begruendungstext fragmentarisch

## Querverweise

- `nkr-aufgabe-und-kompetenz-nkrg`
- `nkr-verfahrensgang-referentenentwurf-bis-bundestag`
- `nkr-stellungnahme-mahnender-charakter-grenzen`
- `nkr-stellungnahme-pressepolitik-und-jahresbericht`
- `legistik-werkstatt/legw-gesetzgebungsverfahren-bauleiter`

## Quellen Stand 06/2026

- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4
- §§ 47, 62 GGO
- GO BT §§ 75 ff.
- NKR-Jahresbericht (jeweils aktuelle Ausgabe) — wiederholt zur Umgehungsproblematik
- Live verifizieren ueber [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de) und [www.bundestag.de](https://www.bundestag.de)
