---
name: vowi-bussgeldbescheid-verkehrsowi-quality
description: "Vowi Bussgeldbescheid Verkehrsowi Quality: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vowi Bussgeldbescheid Verkehrsowi Quality

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vowi Bussgeldbescheid Verkehrsowi Quality** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vowi-bussgeldbescheid-pruefung-bauleiter` | Bauleiter Pruefung Bussgeldbescheid OWiG: Tatvorwurf, Beweismittel, Hoehe, Rechtsfolgen Punkte und Fahrverbot. Pruefraster fuer Verteidiger im Erstgespraech. |
| `verkehrsowi-kommandocenter` | Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf, Frist, Fahrverbot-Risiko, Punkte), Routing auf Subskills. Output Deal-Karte OWi mit Fristen-Ampel und Routing-Empfehlung. Abgrenzung: Alkohol/Drogen siehe verkehrsowi-alkohol-drogen-24a; Rotlicht/Abstand/Handy siehe verkehrsowi-rotlicht-abstand-handy. |
| `verkehrsowi-quality-gate` | Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: § 67 OWiG (Einspruch), § 77 OWiG (HV-Beweisanträge), BVerfG Rohmessdaten. Prüfraster: Messakte vollständig, Rohmessdaten vorhanden, Eichschein geprüft, Fahrverbot-Haertefall-Prüfung, Punkte-Flensburg gecheckt. Output Ampel-Checkliste, Prüfprotokoll für jede Phase. Abgrenzung: Detailprüfungen in Fachmodule; Gesamtsteuerung siehe verkehrsowi-kommandocenter. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Vowi Bussgeldbescheid Verkehrsowi Quality**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vowi-bussgeldbescheid-pruefung-bauleiter`

**Fokus:** Bauleiter Pruefung Bussgeldbescheid OWiG: Tatvorwurf, Beweismittel, Hoehe, Rechtsfolgen Punkte und Fahrverbot. Pruefraster fuer Verteidiger im Erstgespraech.

# VOWi: Bussgeldbescheid-Pruefung

## Spezialwissen: VOWi: Bussgeldbescheid-Pruefung
- **Spezialgegenstand:** VOWi: Bussgeldbescheid-Pruefung / vowi bussgeldbescheid pruefung bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** OWiG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `verkehrsowi-kommandocenter`

**Fokus:** Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf, Frist, Fahrverbot-Risiko, Punkte), Routing auf Subskills. Output Deal-Karte OWi mit Fristen-Ampel und Routing-Empfehlung. Abgrenzung: Alkohol/Drogen siehe verkehrsowi-alkohol-drogen-24a; Rotlicht/Abstand/Handy siehe verkehrsowi-rotlicht-abstand-handy.

# VerkehrsOWi-Verteidiger — Kommandocenter

## Zweck

Einstiegspunkt fuer alle OWi-Mandate im Verkehrsrecht. Erfasst Kontext, bewertet Dringlichkeit und routet zur richtigen Subskill-Anleitung.

## Sofort-Triage bei Mandatsaufnahme

**Drei kritische Fragen zuerst:**

1. **Fristlage:** Wann wurde der Bussgeldbescheid zugestellt? Einspruchsfrist § 67 Abs. 1 OWiG: 2 Wochen ab Zustellung.
 - Frist offen → Einspruch sofort, dann vertiefen
 - Frist abgelaufen → Wiedereinsetzung § 52 OWiG pruefen

2. **OWi oder Strafrecht?** — Grenzwert: § 24a Abs. 1 StVG (0,5 Promille OWi) vs. § 316 StGB (ab 1,1 Promille oder Ausfallerscheinung = Strafrecht!); Geschwindigkeit: OWi immer.

3. **Fahrverbot oder Fahrerlaubnis-Entzug?** — § 25 StVG (OWi: 1-3 Monate, bleibt Fahrerlaubnis) vs. § 69 StGB (Strafrecht: Entziehung mit Sperrfrist).

## Ampel-Schnelldiagnose

| Situation | Ampel | Massnahme |
|-----------|-------|-----------|
| Frist laeuft in < 3 Tagen | ROT | Einspruch SOFORT, dann vertiefen |
| Frist laeuft in 4-7 Tagen | GELB | Einspruch und Akteneinsicht parallel |
| Frist > 7 Tage | GRUEN | Strukturierte Bearbeitung |
| Frist abgelaufen, Wiedereinsetzungsgrund | GELB | § 52 OWiG Antrag |
| Strafrecht (§ 316 StGB) statt OWi | ROT | Subskill Strafrecht wechseln! |

## Routing-Matrix

| Aufgabe | Subskill |
|---------|---------|
| Einspruchsfrist berechnen + einlegen | `verkehrsowi-fristen-einspruch` |
| Akteneinsicht Messakte anfordern | `verkehrsowi-akteneinsicht-messakte` |
| Messverfahren-Angriffspunkte pruefen | `verkehrsowi-messverfahren-geschwindigkeit` |
| Beweisverwertung standardisiert | `verkehrsowi-beweisverwertung-standardisiert` |
| Alkohol / Drogen § 24a StVG | `verkehrsowi-alkohol-drogen-24a` |
| Fahreridentifizierung | `verkehrsowi-fahreridentifizierung` |
| Anhoerung / Bussgeldbescheid-Pruefung | `verkehrsowi-anhoerung-bussgeldbescheid` |
| Haertefall Fahrverbot | `verkehrsowi-haertefall-fahrverbot` |
| Punkte in Flensburg | `verkehrsowi-punkte-fahrverbot-flensburg` |
| Hauptverhandlung Amtsgericht | `verkehrsowi-hauptverhandlung-amtsgericht` |
| Rechtsbeschwerde | `verkehrsowi-rechtsbeschwerde` |
| Zeugen Polizei Strategie | `verkehrsowi-zeugen-polizei-strategie` |
| Rotlicht Abstand Handy | `verkehrsowi-rotlicht-abstand-handy` |
| Verjaehrung Zustellung | `verkehrsowi-verjaehrung-zustellung` |
| Mandantenkommunikation | `verkehrsowi-mandantenkommunikation` |
| Quality Gate | `verkehrsowi-quality-gate` |

## Zentrale OWi-Normen im Ueberblick

- **§ 24 StVG** — Ordnungswidrigkeiten im Strassenverkehr allgemein
- **§ 24a StVG** — Alkohol (0,5 Promille) und Drogen
- **§ 25 StVG** — Fahrverbot 1-3 Monate
- **§ 26 StVG** — Zustaendigkeit Bussgeldbehoerde
- **§ 67 OWiG** — Einspruch 2-Wochen-Frist
- **§ 77 OWiG** — Beweisaufnahme, Sachverstaendige
- **§ 79 OWiG** — Rechtsbeschwerde
- **§ 4 BKatV** — Regelfahrverbot und Abweichung bei Haertefall
- **Art. 103 Abs. 1 GG** — Rechtliches Gehoer, Rohmessdaten-Recht

## Querschnitts-Rechtsprechung

- BGH BGHSt 43, 277 — Standardisiertes Messverfahren befreit von Detailbegruendung, aber konkrete Einwaende sind aufzuklaeren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- OLG Bamberg NZV 2017, 494 — Sachverstaendigenantrag bei konkreten Messfehler-Angriffspunkten zwingend zu bescheiden.

## Harte Leitplanken

- OWi vs. Strafrecht immer zuerst klaeren — falsche Qualifikation ist schwerer Fehler.
- Frist immer zuerst sichern — kein Schritt vor Einspruch.
- Rohmessdaten grundsaetzlich anfordern.
- Anwaltliche Endkontrolle bei allen Fristen und Antraegen.

## 3. `verkehrsowi-quality-gate`

**Fokus:** Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: § 67 OWiG (Einspruch), § 77 OWiG (HV-Beweisanträge), BVerfG Rohmessdaten. Prüfraster: Messakte vollständig, Rohmessdaten vorhanden, Eichschein geprüft, Fahrverbot-Haertefall-Prüfung, Punkte-Flensburg gecheckt. Output Ampel-Checkliste, Prüfprotokoll für jede Phase. Abgrenzung: Detailprüfungen in Fachmodule; Gesamtsteuerung siehe verkehrsowi-kommandocenter.

# Quality Gate — OWi-Mandat

## Gate 1: Vor Einspruch-Versand

```
□ Einspruchsfrist § 67 Abs. 1 OWiG berechnet und noch offen?
 Zustellungsdatum: [DATUM] + 14 Tage = Fristende: [DATUM]
□ Vollmacht des Betroffenen liegt vor?
□ Bussgeldbescheid auf Pflichtinhalt § 66 OWiG geprueft?
□ OWi oder Strafrecht? (Grenzwert BAK § 316 StGB vs. § 24a StVG)
□ Einspruch beschraenkt (§ 67 Abs. 2) oder unbeschraenkt?
□ Mandant hat Anhoerungsbogen NICHT ausgefuellt?
□ Einspruchsschreiben: Name, Az., Zustellungsdatum, Datum, Unterschrift?
□ Akteneinsicht inklusive Messakte beantragt?
□ Einspruch per Fax mit EB versendet, Eingang bestaetigt?
AMPEL: GRUEN alle Punkte erfuellt / ROT Frist abgelaufen
```

## Gate 2: Nach Akteneinsicht — Vor Hauptverhandlung

```
□ Messakte vollstaendig? (Eichschein, Messprotokoll, Schulung, Rohmessdaten)
□ Toleranzabzug nachgerechnet?
□ Eichgueltigkeit zum Messzeitpunkt geprueft?
□ Rohmessdaten vorhanden oder Verweigerung dokumentiert?
□ Sachverstaendigenantrag formuliert (wenn konkrete Angriffspunkte)?
□ Fahreridentifikation geprueft (Foto-Qualitaet)?
□ Verjaehrung geprueft (§ 26 Abs. 3 StVG, § 33 OWiG)?
□ Zustellungsfehler geprueft?
□ Haertefall-Argumentation vorbereitet (wenn Fahrverbot)?
□ Punkte-Flensburg geprueft (neuer Stand nach Eintragung)?
□ Entbindungsantrag § 73 OWiG gestellt?
□ Mandant ueber HV-Ablauf informiert?
AMPEL: GRUEN vollstaendig / GELB offene Punkte / ROT kritische Luecken
```

## Gate 3: Nach Urteil

```
□ Urteil vollstaendig angehoert?
□ Rechtsbeschwerde-Option geprueft: Geldbusse > 250 EUR oder Fahrverbot?
□ Frist: 1 Woche ab Urteilsverkuendung
□ Zulassungsbeschwerde § 80 OWiG bei Geldbusse <= 250 EUR?
□ Absolute Revisionsgründe nach § 338 StPO vorhanden?
□ Tagessatz/Geldbusse korrekt berechnet?
□ Fahrverbot-Dauer und Wirkungszeitpunkt korrekt?
□ Vier-Monats-Frist § 25 Abs. 2a StVG beantragt?
□ Mandant ueber Ergebnis und naechste Schritte informiert?
AMPEL: GRUEN zufriedenstellend / GELB Rechtsbeschwerde moeglich / ROT Fehler
```

## Harte Leitplanken

- Quality Gate ist Pflichtprozess — auch bei einfachen Faellen.
- ROT-Punkte muessen unverzueglich adressiert werden.
- Mandant ueber jeden Gate-Status informieren.
- Anwaltliche Endkontrolle bei jedem Gate zwingend.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
