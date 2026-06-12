# Megaprompt: verkehrsowi-verteidiger

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `verkehrsowi-verteidiger`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Verkehrs-OWi-Verteidigung: ordnet Rolle (Betroffener, Bußgeldbehörde, AG), markiert Fri…
2. **verkehrsowi-erstpruefung-und-mandatsziel** — Verkehrsowi: Erstprüfung, Rollenklärung und Mandatsziel.
3. **alkohol-drogen-beweisverwertung** — Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen…
4. **mandantenkommunikation** — Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: B…
5. **start-chronologie-fristen** — Einstieg, Schnelltriage und Fallrouting im Verkehrsowi Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risik…
6. **verkehrsowi-aktenanlage** — Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 4…
7. **verkehrsowi-anhoerung-bussgeldbescheid** — Anhörung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhörungsbogen oder Bußgeldbescheid erhalten.…
8. **verkehrsowi-fahreridentifizierung** — Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer…
9. **verkehrsowi-fristen-einspruch** — Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 O…
10. **verkehrsowi-haertefall-fahrverbot** — Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 2…
11. **verkehrsowi-hauptverhandlung-amtsgericht** — Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen…
12. **verkehrsowi-kommandocenter** — Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. No…
13. **verkehrsowi-punkte-fahrverbot** — Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führer…
14. **verkehrsowi-quality-gate** — Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: §…
15. **verkehrsowi-rechtsbeschwerde** — Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerd…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Verkehrs-OWi-Verteidigung: ordnet Rolle (Betroffener, Bußgeldbehörde, AG), markiert Frist (Einspruch 2 Wochen § 67 OWiG), wählt Norm (OWiG, StVO, StVG, BKatV) und Zuständigkeit (Bußgeldbehörde), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Verkehrsowi Verteidiger** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abstand-quellenkarte` — Abstand Quellenkarte
- `akteneinsicht-internationaler-bezug-und-schnittstellen` — Akteneinsicht Internationaler Bezug und Schnittstellen
- `alkohol-compliance-dokumentation-und-akte` — Alkohol Compliance Dokumentation und Akte
- `alkohol-drogen-beweisverwertung` — Alkohol Drogen Beweisverwertung
- `amtsgericht-drogen-interessen-einspruch` — Amtsgericht Drogen Interessen Einspruch
- `anhoerung-verkehrsowi-einspruch-messverfahren` — Anhoerung Verkehrsowi Einspruch Messverfahren
- `bussgeldbescheid-tatbestand-beweis-und-belege` — Bussgeldbescheid Tatbestand Beweis und Belege
- `drogen-mehrparteien-konflikt-und-interessen` — Drogen Mehrparteien Konflikt und Interessen
- `einspruch-dokumentenmatrix-und-lueckenliste` — Einspruch Dokumentenmatrix und Lueckenliste
- `fahrverbot-geschwindigkeit-handy` — Fahrverbot Geschwindigkeit Handy
- `geschwindigkeit-verhandlung-vergleich-und-eskalation` — Geschwindigkeit Verhandlung Vergleich und Eskalation
- `handy-zahlen-schwellen-und-berechnung` — Handy Zahlen Schwellen und Berechnung
- `hauptverhandlung-sonderfall-messakte-messung` — Hauptverhandlung Sonderfall Messakte Messung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Verkehrsowi Verteidiger sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `verkehrsowi-erstpruefung-und-mandatsziel`

_Verkehrsowi: Erstprüfung, Rollenklärung und Mandatsziel._

# Verkehrsowi: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Verkehrsowi Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Verkehrsowi Verteidiger** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Verkehrsowi: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verkehrsowi** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## OWi-Erstpruefung Mandatsziel Bausteine
- **Sofort-Triage in 5 Punkten:**
 - **(1) Zustellungsdatum** Bussgeldbescheid? § 67 OWiG 2 Wochen Einspruchsfrist.
 - **(2) Tatvorwurf-Typ** (Geschwindigkeit, Abstand, Rotlicht, Handy, Alkohol, Drogen)?
 - **(3) Sanktionsumfang** (Geldbusse, Punkte, Fahrverbot)?
 - **(4) Beruflich existenzbedrohend** (Berufskraftfahrer, Pendler, Aussendienst)?
 - **(5) Vorbelastung** (Punktestand FAER, Wiederholungstaeter § 4 II StVG, MPU-Risiko)?
- **Mandatsziele-Hierarchie:**
 - **Verfahren einstellen** § 47 OWiG (Geringfuegigkeit, öffentliches Interesse).
 - **Fahrverbot abwenden** (auch ueber Erhoehung Geldbusse als Kompensation, BGH-Linie).
 - **Punkte abwenden** (insb. bei drohender 8-Punkte-Grenze).
 - **Geldbusse senken** (oft realistisch ueber Beschraenkung).
 - **Schuldspruch beseitigen** (Messfehler, Identitaetszweifel).
- **Akteneinsicht § 49 OWiG i.V.m. § 147 StPO sofort:**
 - Messprotokoll, Lichtbild, Eichschein, Bedienerschein, Lebensakte Geraet.
 - Rohdaten (.case / .esa / etc.) - BVerfG-Linie zur fair-trial-Garantie.
 - Schulungsnachweis Messbeamter.
- **Verteidigungsstrategie-Optionen:**
 - **Messfehler** (Standardisierungsfrage, Toleranzunterschreitung, Bedienfehler).
 - **Identitaetszweifel** (Lichtbild zeigt nicht Halter; Halterauskunft § 31a StVZO trotzdem zulaessig).
 - **Verfahrensfehler** (Verjährung § 26 III StVG, Zustellungsmaengel, Anhörungspflicht § 55 OWiG).
 - **Rechtsfolgenmilderung** (Tagessatzhoehe; Fahrverbot Haerte).
- **Risikoampel:**
 - **Rot:** Fristablauf droht, Fahrverbot bei Berufskraftfahrer, drohende 8-Punkte-Grenze, MPU-Anordnung.
 - **Gelb:** Beweislage unklar, Messverfahren angreifbar.
 - **Gruen:** dokumentierte Mandantenfreigabe, Strategie klar.

## Qualitätsanker: Messdaten, Messakte und faires Verfahren

- **Verifizierter Leitanker:** BVerfG, Beschluss vom 12.11.2020 - 2 BvR 1616/18. Bei standardisierten Messverfahren darf die Verteidigung nicht mit bloßer Behördenroutine abgespeist werden; vorhandene, nicht aktenkundige Messinformationen können für ein faires Verfahren zugänglich sein, wenn sie konkret und rechtzeitig verlangt werden.
- **Praktische Übersetzung:** Niemals nur pauschal „Messung bestreiten“. Immer präzise anfordern: Falldatei/Rohmessdaten, Messreihe soweit vorhanden und relevant, Token/Passwort, Eichschein, Gebrauchsanweisung, Schulungsnachweise, Wartungs-/Reparaturhinweise, Standort-/Beschilderungsunterlagen, Statistik und Auswerteprotokoll.
- **Angriffslinie:** Standardisiertes Messverfahren ist eine Beweiserleichterung, kein Denkverbot. Der Skill muss aus Unterlagen konkrete Einwendungen machen: falsches Gerät, fehlende Eichung, fehlerhafte Bedienung, unklare Fahreridentität, unplausible Messreihe, fehlende Einsicht, Frist-/Gehörsproblem.
- **Output-Pflicht:** Immer ein kurzes Anforderungsschreiben oder einen gerichtsfesten Begründungsbaustein anbieten, wenn Akteneinsicht, Messunterlagen oder Fristwahrung Thema sind.

---

## Skill: `alkohol-drogen-beweisverwertung`

_Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 2 StVG (Wirkstoffnachweis THC/Kokain/Amphetamin), § 81a StPO (Blutprobe), § 316 StGB (Trunkenheit im Verkehr Abgrenzung). P..._

# Alkohol und Drogen — § 24a StVG

## Arbeitsbereich

Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 2 StVG (Wirkstoffnachweis THC/Kokain/Amphetamin), § 81a StPO (Blutprobe), § 316 StGB (Trunkenheit im Verkehr Abgrenzung). Prüfraster: Toleranzwerte, analytische Nachweisgrenze vs. Wirkung, Blutprobe-Anforderung ordnungsgemäß, Fahrerlaubnis-Konsequenzen § 69 StGB. Output Einspruchs-Strategie, Beweisverwertungs-Antrag. Abgrenzung: Strafrecht § 316 StGB siehe fachanwalt-strafrecht-Plugin; Fahrerlaubnisentzug VwR siehe fachanwalt-verwaltungsrecht-Plugin. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Alkohol oder Drogen?** — § 24a Abs. 1 StVG: 0,5 Promille-Grenze (Atemalkohol 0,25 mg/l); § 24a Abs. 2 StVG: Drogen-Wirkstoffnachweis.
2. **BAK-Wert oder Atemalkohol-Wert?** — Atemalkohol-Wert (AAK): 0,25 mg/l = OWi; ab 0,50 mg/l AAK oder BAK 1,1 Promille bei Ausfallerscheinungen = § 316 StGB (Strafrecht!).
3. **Blutprobe entnommen?** — Zeitpunkt der Entnahme nach Fahrtende relevant; Rueckrechnung auf Fahrzeitpunkt.
4. **Bei Drogen:** Welcher Stoff? THC, Kokain, Amphetamin — unterschiedliche analytische Grenzwerte.
5. **Fahrerlaubnis-Konsequenzen?** — § 69 Abs. 2 StGB-Regelfall bei § 316 StGB; im OWi-Bereich Fahrverbot nach § 25 StVG.

## Zentrale Normen (Stand Mai 2026)

- **§ 24a Abs. 1 StVG** — Alkohol-OWi: Atemalkohol 0.25 mg/l oder mehr; oder BAK 0.5 Promille oder mehr
- **§ 24a Abs. 1a StVG** — THC-Grenzwert 3.5 ng/ml im Blutserum (in Kraft seit 22.8.2024, BGBl. I 2024 Nr. 274)
- **§ 24a Abs. 2 StVG** — Drogen-OWi: Fahren unter Einfluss von in Anlage zu § 24a StVG genannten Substanzen (Kokain, Amphetamin, MDMA, Methamphetamin, Morphin u.a.)
- **§ 24a Abs. 3 StVG** — keine OWi wenn Drogeneinnahme nachweislich laenger zurueckliegt und keine Fahruntauglichkeit
- **§ 316 StGB** — Trunkenheitsfahrt: BAK ab 1.1 Promille (absolute Fahruntauglichkeit) oder ab 0.3 Promille mit Ausfallerscheinungen (relative Fahruntauglichkeit)
- **§ 315c StGB** — Gefährdung des Strassenverkehrs unter Alkohol
- **§ 81a StPO** — Blutentnahme durch Arzt; richterlicher Anordnungsvorbehalt
- **§ 69 Abs. 2 StGB** — Regelungeeignetheit bei § 316 StGB
- **§ 25 StVG** — Fahrverbot im OWi-Verfahren
- **KCanG** (Konsumcannabisgesetz vom 27.3.2024, BGBl. I 2024 Nr. 109) — Cannabis ab 1.4.2024 kein BtM mehr; medizinische Verwendung im MedCanG

## Aktuelle Rechtsprechung (Stand Mai 2026; offene Quellen)

- **BVerwG, Beschl. v. 8.1.2025, 3 B 2.24** — Cannabis ist seit KCanG (1.4.2024) kein BtM mehr; § 14 FeV im Lichte der neuen Gesetzeslage anzuwenden. Quelle: bverwg.de
- BGH 4. Strafsenat zu § 24a StVG und § 316 StGB: konkrete Aktenzeichen vor Versand in bundesgerichtshof.de oder dejure.org verifizieren.
- OLG-Linien zu Cannabis-Grenzwert und Trennungsfähigkeit: laufende Rechtsprechung 2025/2026 — vor Versand in openjur.de oder nrwe.de prüfen.

## Trennlinie OWi vs. Strafrecht

| Situation | Norm | Konsequenz |
|---------|------|-----------|
| AAK 0.25 bis 0.49 mg/l ohne Ausfallerscheinung | § 24a Abs. 1 StVG | OWi: Geldbusse + Fahrverbot 1-3 Monate |
| AAK ab 0.55 mg/l (BAK ab 1.1 Promille) OHNE Ausfall | § 316 StGB absolute Fahruntauglichkeit | Strafrecht: Geldstrafe + Fahrerlaubnis-Entzug |
| BAK ab 0.3 Promille MIT Ausfallerscheinung | § 316 StGB relative Fahruntauglichkeit | Strafrecht |
| BAK ab 1.6 Promille bei Wiederholung / Erstkontakt | § 316 StGB + MPU-Pflicht (§ 13 FeV) | Strafrecht, MPU-Pflicht |
| THC im Blutserum ab 3.5 ng/ml (seit 22.8.2024) | § 24a Abs. 1a StVG | OWi |
| Andere Drogen-Wirkstoffnachweis | § 24a Abs. 2 StVG | OWi |

## Schritt-für-Schritt-Workflow

1. **Sachverhalt aufnehmen:** AAK-Wert, BAK-Wert, Zeitpunkt der Atemtest/Blutentnahme, Fahrtende.
2. **Zuordnung OWi oder Strafrecht?** — Trennlinie klar definieren.
3. **Blutentnahme-Rechmaessigkeit pruefen:** Richteranordnung vorhanden? Gefahr im Verzug begruendet?
4. **Rueckrechnungspruefung:** Nachweis BAK/AAK korrekt auf Fahrzeitpunkt zurueckgerechnet?
5. **Bei Drogen:** Wirkstoff und Grenzwert pruefen; § 24a Abs. 3 StVG-Ausnahme pruefen.
6. **Fahrerlaubnis-Strategie:** Fahrverbot § 25 StVG vs. Entziehung § 69 StGB — getrennt bearbeiten.

## Harte Leitplanken

- BAK ab 1,6 Promille immer als Strafrecht behandeln — eigener Skill § 316 StGB.
- Blutentnahme-Rechtmaessigkeit aktiv pruefen — Verwertungsverbot argumentierbar.
- Rueckrechnung selbst kontrollieren; Fehler im Urteil sind Revisionsgruende.
- Anwaltliche Endkontrolle bei Abgrenzung OWi/Strafrecht.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 67 OWiG
- § 79 OWiG
- § 26 StVG
- § 31 OWiG
- § 25 StVG
- § 24a StVG
- § 55 OWiG
- § 33 OWiG
- § 77 OWiG
- § 316 StGB
- § 71 OWiG
- § 49 OWiG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `mandantenkommunikation`

_Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden, Anhörungsbogen-Empfehlung, Fahrverbot-Erklärung, Punktestand-Abfrage, Terminvorbereitun..._

# Mandantenkommunikation im OWi-Mandat

## Arbeitsbereich

Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden, Anhörungsbogen-Empfehlung, Fahrverbot-Erklärung, Punktestand-Abfrage, Terminvorbereitung HV. Output Mandantenbrief-Template, Erklärungsbausteine, Kommunikations-Protokoll. Abgrenzung: Inhaltliche Strategie siehe verkehrsowi-kommandocenter; Anhörung siehe verkehrsowi-anhoerung-bußgeldbescheid. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage-Erstgespraeches-Leitfaden

**Was zuerst klaeren:**

1. **Zustellungsdatum Bescheid?** — Frist sofort berechnen, Mandant informieren.
2. **Fahrzeug auf Mandanten-Namen?** — Halter = OWi-Adressat; wenn nicht Fahrzeugfuehrer: Fahreridentifikation.
3. **Aktueller Punktestand?** — Hat der Mandant eine FAER-Auskunft (§ 30 StVG)?
4. **Berufliche Folgen eines Fahrverbots?** — Existenzgefaehrdung? Arbeitgeber-Bescheinigung moeglich?
5. **Was ist das Ziel?** — Freispruch, Einstellung, Fahrverbot-Vermeidung, Tagessatz-Reduzierung?

## Kommentar-Warteraum Erstgespraeches-Sprache

- Nicht: "Die Messtoleranz wurde korrekt abgezogen" → Besser: "Von Ihrer gemessenen Geschwindigkeit wird ein Sicherheitsabzug von 3 km/h (bzw. 3%) vorgenommen — das ist gesetzlich vorgeschrieben."
- Nicht: "§ 67 OWiG-Frist" → Besser: "Sie haben ab dem Tag, an dem Sie den Bescheid bekommen haben, 2 Wochen Zeit, Einspruch einzulegen."
- Nicht: "Standardisiertes Messverfahren nach BGH" → Besser: "Das Gericht akzeptiert diese Art der Messung grundsaetzlich, aber wir pruefen trotzdem ob technische Fehler vorlagen."

## Zentrale Normen

- **§ 55 OWiG** — Schweigerecht des Betroffenen; keine Pflicht zur Aussage
- **§ 67 OWiG** — Einspruchsfrist 2 Wochen
- **§ 25 StVG** — Fahrverbot
- **§ 4 StVG** — Punkte in Flensburg

## Mandantenhinweis-Template nach Einspruchseinlegung

**Adressat:** Mandant — Tonfall: verstaendlich-erklaerend

```
Sehr geehrte/r Frau/Herr [NAME],

ich bestaedige, dass ich fristgerecht Einspruch gegen den
Bussgeldescheid vom [DATUM] eingelegt habe.

Wie es weitergeht:
Die Behörde prueft nun die Akte. Danach wird entweder:
a) das Verfahren eingestellt (kein Bussgeldbescheid mehr),
b) ein Verhandlungstermin am Amtsgericht angesetzt, oder
c) die Behörde den Bescheid bestaetigt (dann gehen wir
 weiter zum Amtsgericht).

Was Sie tun koennen:
- Bitte sprechen Sie NICHT mit Polizei oder Behörden
 ueber den Vorfall ohne mich zu kontaktieren.
- Wenn Sie neue Unterlagen erhalten, bitte sofort weiterleiten.
- Haben Sie ein Fahrtenbuch oder Notizbuch, das den Tatvorwurf
 betrifft? Bitte aufbewahren.

Kostenschaetzung: [RVG-Gebühren]

Mit freundlichen Gruessen
[KANZLEI]
```

## Template Anhörungsbogen-Empfehlung

**Adressat:** Mandant — Tonfall: klar und eindeutig

```
Sehr geehrte/r Frau/Herr [NAME],

Sie haben einen Anhörungsbogen erhalten. Meine Empfehlung:

BITTE DEN BOGEN NICHT AUSFULLEN UND NICHT UNTERSCHREIBEN.

Begruendung: Sie muessen nicht antworten. Das Schweigen wird
Ihnen NICHT nachteilig ausgelegt. Unterschreiben Sie den Bogen
nur, wenn er explizit nur Ihre Personalien (Name, Adresse) abfragt
— und auch dann nur nach meiner Ruecksprache.

Falls Sie sich bereits gaeussert haben: Bitte informieren Sie
mich sofort.

Mit freundlichen Gruessen [KANZLEI]
```

## Schritt-für-Schritt-Mandantenbetreuung

1. **Erstgespraech:** Sachverhalt aufnehmen, Frist sofort notieren, Vollmacht einholen.
2. **Einspruch einlegen:** Mandant sofort informieren.
3. **Akteneinsicht:** Ergebnis in verstaendlicher Sprache erklaeren.
4. **Strategie besprechen:** Erfolgsaussichten realistisch einschaetzen.
5. **Vor der HV:** Mandant ueber Ablauf informieren, Erscheinungspflicht klaeren.
6. **Nach der HV / Urteil:** Ergebnis erklaeren, Rechtsmitteloptionen darlegen.

## Harte Leitplanken

- Mandant immer ueber Kosten informieren (RVG-Gebühren schriftlich).
- Erfolgsaussichten realistisch kommunizieren — keine Garantien.
- Fristen immer in Mandantenkommunikation vermerken.
- Anwaltliche Endkontrolle bei Mandantenkorrespondenz.

---

## Skill: `start-chronologie-fristen`

_Einstieg, Schnelltriage und Fallrouting im Verkehrsowi Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenst..._

# VerkehrsOWi-Verteidiger — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verkehrsowi Verteidiger**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `verkehrsowi-aktenanlage` | Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster:… |
| `verkehrsowi-akteneinsicht-messakte` | Akteneinsicht in die Messakte beantragen und systematisch auswerten; BVerfG 2 BvR 1616/18 und 2 BvR 1167/20 zur Rohmessdatenpflicht. |
| `verkehrsowi-alkohol-drogen-24a` | Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 1a StVG (THC 3.5 ng/ml seit 22.8.2024), § 24a Abs. 2 StVG (Wirkstoffnachweis), KCanG (1.4.2024). |
| `verkehrsowi-anhoerung-bussgeldbescheid` | Anhörung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhörungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhörung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67… |
| `verkehrsowi-beweisverwertung-standardisiert` | BGHSt 39, 291 zum standardisierten Messverfahren; konkrete Angriffspunkte gegen die Verwertbarkeit. |
| `verkehrsowi-fahreridentifizierung` | Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer nicht nennen. Normen: § 31a StVG (Halter-Auskunftspflicht und Fahrtenbuchauflage), § 55 OWiG… |
| `verkehrsowi-fristen-einspruch` | Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG… |
| `verkehrsowi-haertefall-fahrverbot` | Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG… |
| `verkehrsowi-hauptverhandlung-amtsgericht` | Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG… |
| `verkehrsowi-kommandocenter` | Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf,… |
| `verkehrsowi-mandantenkommunikation` | Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden,… |
| `verkehrsowi-messverfahren-geschwindigkeit` | Standardisierte Messverfahren angreifen; Rohmessdaten anfordern; BVerfG 2 BvR 1167/20 (20.6.2023). |
| `verkehrsowi-punkte-fahrverbot-flensburg` | Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8… |
| `verkehrsowi-quality-gate` | Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: § 67 OWiG (Einspruch), § 77 OWiG (HV-Beweisanträge), BVerfG Rohmessdaten. Prüfraster: Messakte… |
| `verkehrsowi-rechtsbeschwerde` | Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG… |
| `verkehrsowi-rechtsprechungsrecherche` | Rechtsprechungsrecherche für OWi-Verkehrsmandate: Anwalt sucht OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverbot. Normen: §§ 24 StVG, 25 StVG, 4 StVG; OWiG §§ 67 und 79 und 80. Prüfraster:… |
| `verkehrsowi-rotlicht-abstand-handy` | Rotlicht-OWi, Abstand-OWi und Handy-OWi verteidigen: Mandant hat Bußgeldbescheid wegen Rotlicht, zu geringem Abstand oder Handynutzung erhalten. Normen: § 37 StVO (Rotlicht: einfach vs. qualifiziert 1 Sekunde), § 4… |
| `verkehrsowi-simulation-training` | Simulationstraining für OWi-Mandate. Uebungsszenarien Messverfahren Rotlicht Handy Alkohol Fahreridentifizierung. Rollenspiel Mandantengespraeche Hauptverhandlung. Fallvarianten mit Erwartungshorizont. Training ohne echte… |
| `verkehrsowi-verjaehrung-zustellung` | Verfolgungsverjährung im OWi-Verfahren prüfen: Anwalt will Verjährungseinwand erheben. Normen: § 26 StVG i.V.m. § 31 OWiG (Verjährungsfrist 3 Monate nach Tatende), § 33 OWiG (Unterbrechungshandlungen), absolute… |
| `verkehrsowi-zeugen-polizei-strategie` | Zeugen-Strategie gegenüber Polizeibeamten im OWi-Verfahren: Polizeibeamter als einziger Zeuge in der HV. Normen: § 240 StPO i.V.m. § 71 OWiG (Fragerecht), §§ 373 ff. StPO (Zeugenvernehmung). Prüfraster:… |

## Worum geht es?

Dieses Plugin begleitet Verkehrs-Ordnungswidrigkeitsmandate von der ersten Anhörung bis zur Rechtsbeschwerde. Es richtet sich an Rechtsanwaelte, die Mandanten bei Bussgeldbescheiden, Fahrverboten, Punkteeintragungen und Verfahren vor dem Amtsgericht vertreten. Abgedeckt werden Geschwindigkeitsmessungen, Rotlicht-OWi, Abstandsverfahren, Handyverstaesse, Alkohol und Drogen am Steuer, Fahreridentifizierung sowie die Beweisverwertung standardisierter Messverfahren.

Das Plugin folgt dem Verfahrensablauf: Anhörung → Bussgeldbescheid → Einspruch → Akteneinsicht/Messakte → Hauptverhandlung → ggf. Rechtsbeschwerde. Jede Phase hat eigene Fristen und Verteidigungsstrategien.

## Wann brauchen Sie diese Skill?

- Mandant erhaelt Anhörungsbogen oder Bussgeldbescheid wegen Geschwindigkeitsueberschreitung und braucht sofortige Beratung zu Einspruchsfrist und Strategie.
- Mandant ist auf den Fuehrerschein beruflich angewiesen und soll Fahrverbot erhalten — Haertefall-Argumentation pruefen.
- Anwalt hat Akteneinsicht beantragt und will Messakte auf Verfahrensfehler untersuchen.
- Mandant bestreitet Fahrereigenschaft — Fahreridentifizierungsstrategie entwickeln.
- OWi-Urteil des Amtsgerichts ist unbefriedigend und Rechtsbeschwerde zum OLG wird erwaogen.

## Fachbegriffe (kurz erklaert)

- **OWiG** — Gesetz ueber Ordnungswidrigkeiten; Rahmengesetz für alle Ordnungswidrigkeitsverfahren einschliesslich VerkehrsOWi.
- **StVG** — Strassenverkehrsgesetz; § 24 StVG Grundnorm für Verkehrsordnungswidrigkeiten, § 25 StVG Fahrverbot.
- **FAER** — Fahreignungsregister; Punkteregister in Flensburg beim Kraftfahrt-Bundesamt.
- **Messakte** — Vollstaendige Unterlagen zum Messvorgang: Eichschein, Rohmessdaten, Geraetefoto, Aufstellprotokoll.
- **Standardisiertes Messverfahren** — Pruefstandsgerechtes Verfahren mit amtlich anerkanntem Messgeraet; Gerichte duerfen auf Beweiswert vertrauen, solange keine konkreten Fehlerhinweise vorliegen.
- **Verfolgungsverjaehrung** — Nach §§ 26 StVG und 31 ff. OWiG: Verjaeht die Tat, kann kein Bussgeld mehr verhaengt werden.
- **Rechtsbeschwerde** — Rechtsmittel nach § 79 OWiG zum Oberlandesgericht gegen Urteil des Amtsgerichts im OWi-Verfahren.
- **Haertefall** — Ausnahme vom Fahrverbot nach § 25 StVG, wenn unverhieltnisgemäßige berufliche Folgen drohen.

## Rechtsgrundlagen

- § 24 StVG (Ordnungswidrigkeiten im Strassenverkehr)
- § 25 StVG (Fahrverbot)
- §§ 26 StVG (Verfolgungsverjaehrung)
- §§ 24a StVG (Alkohol- und Drogenfahrten)
- §§ 67 ff. OWiG (Einspruch gegen Bussgeldbescheid)
- § 79 OWiG (Rechtsbeschwerde zum OLG)
- §§ 62-66 OWiG (Akteneinsicht im OWi-Verfahren)
- BKatV (Bussgeldkatalogverordnung mit Regelbuessgeldern und Fahrverboten)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Aktenanlage und Mandat aufnehmen: Tatvorwurf, Verfahrensstadium, Fristen erfassen (`verkehrsowi-aktenanlage`).
2. Einspruchsfrist pruefen: Zwei Wochen ab Zustellung des Bussgeldbescheids — Fristwahrung hat Vorrang (`verkehrsowi-fristen-einspruch`).
3. Akteneinsicht und Messakte beantragen und auswerten (`verkehrsowi-akteneinsicht-messakte`).
4. Verteidigungsstrategie festlegen: Messverfahren angreifen, Fahreridentifizierung, Haertefall?
5. Quality-Gate vor Einspruch und vor Hauptverhandlung durchlaufen (`verkehrsowi-quality-gate`).

## Skill-Tour (was gibt es hier?)

- `verkehrsowi-kommandocenter` — Zentrales Steuerungsmodul: schnelle Orientierung für jedes OWi-Mandat vom Intake bis zur Strategie.
- `verkehrsowi-aktenanlage` — Akte im VerkehrsOWi-Mandat anlegen und strukturieren.
- `verkehrsowi-anhoerung-bussgeldbescheid` — Reaktion auf Anhörungsbogen oder Bussgeldbescheid strategisch vorbereiten.
- `verkehrsowi-fristen-einspruch` — Einspruchsfrist berechnen und wahren; Fristversaeumnis-Risiken erkennen.
- `verkehrsowi-akteneinsicht-messakte` — Vollstaendige Messakte anfordern und auf Verfahrensfehler und Eichluecken pruefen.
- `verkehrsowi-messverfahren-geschwindigkeit` — Geschwindigkeitsmessungen (TraffiStar, Riegl, ESO) auf Verwertbarkeit angreifen.
- `verkehrsowi-beweisverwertung-standardisiert` — Beweisverwertbarkeit im standardisierten Messverfahren angreifen.
- `verkehrsowi-rotlicht-abstand-handy` — Rotlicht-, Abstands- und Handy-OWi verteidigen.
- `verkehrsowi-alkohol-drogen-24a` — Alkohol- und Drogen-OWi nach § 24a StVG verteidigen (0,5-Promille, Drogennachweis).
- `verkehrsowi-fahreridentifizierung` — Fahrereigenschaft angreifen oder Fahreridentifizierung als Verteidigungsstrategieklaeren.
- `verkehrsowi-punkte-fahrverbot-flensburg` — Punkte im FAER und Fahrverbot nach § 25 StVG pruefen und Massnahmen besprechen.
- `verkehrsowi-haertefall-fahrverbot` — Haertefall-Argumentation gegen Fahrverbot bei beruflicher Angewiesenheit entwickeln.
- `verkehrsowi-verjaehrung-zustellung` — Verfolgungsverjaehrung pruefen und Zustellungsfehler identifizieren.
- `verkehrsowi-hauptverhandlung-amtsgericht` — Hauptverhandlung am Amtsgericht vorbereiten und fuehren.
- `verkehrsowi-rechtsbeschwerde` — Rechtsbeschwerde nach § 79 OWiG zum OLG einlegen.
- `verkehrsowi-zeugen-polizei-strategie` — Zeugen-Strategie gegenueber Polizeibeamten in der Hauptverhandlung entwickeln.
- `verkehrsowi-quality-gate` — Checkliste vor Einspruch, nach Akteneingang und vor Hauptverhandlung durchlaufen.
- `verkehrsowi-mandantenkommunikation` — Mandant verstaendlich ueber Verfahren, Kosten und Aussichten informieren.
- `verkehrsowi-rechtsprechungsrecherche` — OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverboten recherchieren.
- `verkehrsowi-simulation-training` — Simulationstraining für OWi-Mandate: Messverfahren, Rotlicht, Handy, Alkohol, Fahreridentifizierung.

## Worauf besonders achten

- Einspruchsfrist ist zwei Wochen ab Zustellung — keine Hemmung, kein Neubeginn bei blossem Schweigen; Fristverpassen = Rechtskraft.
- Verfolgungsverjaehrung nach § 26 StVG betraegt 3 Monate ab Tatbegehung, Unterbrechung durch behordliche Massnahmen — Zeitstrahl pruefen.
- Akteneinsicht in Messakte inklusive Rohmessdaten ist einzufordern; ohne Rohmessdaten ist effektive Verteidigung eingeschraenkt.
- Haertefall-Fahrverbot: Nicht jede berufliche Betroffenheit genuegt — wirtschaftliche Existenzgefaehrdung oder alternativlose Infrastruktur noetig.
- Rechtsbeschwerde setzt Anwaltszwang voraus (§ 79 Abs. 3 OWiG i. V. m. § 341 StPO analog).

## Typische Fehler

- Einspruch ohne gleichzeitige Akteneinsicht: Verteidigung beginnt blind ohne Kenntnis der Messumstaende.
- Schweigen im Anhörungsbogen unterlassen: Mandant macht Angaben, die spaeter als Beweismittel verwendet werden.
- Fahreridentifizierungsstrategie zu spaet entwickelt: Fotoabgleich wird im Bussgeldbescheid bereits verwendet und nicht mehr angegriffen.
- Haertefall nicht rechtzeitig vorgetragen: Amtsgericht prueft von Amts wegen nicht — Vortrag Sache des Verteidigers.
- Rechtsbeschwerde ohne Zulassungsgrund: Nur bei Verfahrensfehlern oder Rechtsfragen von grundsaetzlicher Bedeutung zulaessig.

## Quellen und Aktualitaet

- Stand: 05/2026
- StVG in der zum Stand-Datum geltenden Fassung
- OWiG in der geltenden Fassung
- BKatV (Bussgeldkatalogverordnung) in der geltenden Fassung

---

## Skill: `verkehrsowi-aktenanlage`

_Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverze..._

# Aktenanlage OWi-Mandat

## Arbeitsbereich

Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverzeichnis (Messgerät, Eichschein). Output Aktenstruktur, Fristen-Übersicht-Tabelle, Beweismittelverzeichnis. Abgrenzung: Akteneinsicht Messakte siehe verkehrsowi-akteneinsicht-messakte; Einspruchsfrist siehe verkehrsowi-fristen-einspruch. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Vollmacht vorhanden?** — Ohne Vollmacht keine Akteneinsicht.
2. **Zustellungsdatum des Bescheids dokumentiert?** — Fristbeginn.
3. **Aktenzeichen und Delikt notiert?** — Grundlage für Schriftsaetze.
4. **Mandantenziel klar?** — Einspruch, Einstellung, Fahrverbot-Vermeidung.
5. **Sofortmassnahmen eingeleitet?** — Einspruch und Akteneinsicht.

## Aktenstruktur OWi-Mandat

```
01_MANDANT
 - Vollmacht Original
 - Personalien, Kontakt
 - Mandantenziel schriftlich

02_BUSSGELDBESCHEID
 - Bussgeldbescheid Original/Kopie
 - Zustellungsurkunde
 - § 66 OWiG-Pruefungsnotiz

03_FRISTEN
 - Einspruchsfrist: Zustellungsdatum + 14 Tage
 - Rechtsbeschwerde-Frist (wenn noetig): Urteil + 7 Tage
 - Verjährungs-Check

04_SCHRIFTSAETZE_AUSGEHEND
 - Einspruch (mit Eingangsbestaetigung)
 - Akteneinsichtsantrag (mit Messakte-Aufzaehlung)

05_MESSAKTE
 - Eichschein (Gueltigkeit geprueft: Datum markiert)
 - Messprotokoll
 - Schulungsnachweis
 - Rohmessdaten (falls vorhanden)
 - Messfoto hochaufloesend

06_BEWEISMITTELVERZEICHNIS
 (s. Vorlage unten)

07_KORRESPONDENZ
 - Bussgeldbehoerde, Amtsgericht, StA
 - Chronologisch

08_HAUPTVERHANDLUNG
 - Einlassung oder Schweigen-Notiz
 - Beweisantraege
 - Plaedoyer

09_URTEIL_RECHTSBEHELFE
 - Urteil Original
 - Rechtsbeschwerde
```

## Fristen-Uebersicht OWi

| Frist | Rechtsgrundlage | Datum | Erledigt |
|-------|----------------|-------|---------|
| Einspruch | § 67 Abs. 1 OWiG | [Zustellung + 14T] | □ |
| Akteneinsicht | § 49 OWiG | Sofort | □ |
| Wiedereinsetzung (falls noetig) | § 52 OWiG | [Kenntnis + 7T] | □ |
| Rechtsbeschwerde | § 79 Abs. 1 OWiG | [Urteil + 7T] | □ |
| Rechtsbeschwerde-Begruendung | § 79 Abs. 3 OWiG | [Zustellung Urteil + 1M] | □ |
| Vier-Monats-Frist Fahrverbot | § 25 Abs. 2a StVG | [Rechtskraft + 4M] | □ |

## Beweismittelverzeichnis Messakte

| Nr. | Dokument | Datum | Geprueft | Status |
|-----|---------|-------|---------|--------|
| 1 | Eichschein | [DATUM] | □ | Gueltig bis [DATUM] |
| 2 | Messprotokoll | [DATUM] | □ | Angriffspunkte? |
| 3 | Schulungsnachweis | [DATUM] | □ | Beamter [NAME] |
| 4 | Rohmessdaten | [DATUM] | □ | Vorhanden / Fehlt |
| 5 | Messfoto | [DATUM] | □ | Fahrer identifizierbar? |

## Harte Leitplanken

- Aktenanlage unmittelbar bei Mandatsuebernahme.
- Fristen immer als Erstes eintragen.
- Messakte-Vollstaendigkeitspruefung ist Pflicht.
- Bei Aktennachlieferungen: Verzeichnis aktualisieren.

---

## Skill: `verkehrsowi-anhoerung-bussgeldbescheid`

_Anhörung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhörungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhörung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch 2-Wochen-Frist). Prüfraster: Anhörungsbogen zurücksenden oder nicht..._

# Anhörung und Bussgeldbescheid — §§ 55 und 66 OWiG

## Arbeitsbereich

Anhörung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhörungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhörung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch 2-Wochen-Frist). Prüfraster: Anhörungsbogen zurücksenden oder nicht, Schweige-Empfehlung, Frist ab Zustellung. Output Empfehlungsschreiben Mandant, Muster Schweigeerklarung, Einspruchs-Template. Abgrenzung: Einspruch und Frist siehe verkehrsowi-fristen-einspruch; Messverfahren-Angriff siehe verkehrsowi-beweisverwertung-standardisiert. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Anhörungsbogen erhalten?** — Unterschied zum Bussgeldbescheid: Anhörung ist Vorstadium; kein Bussgeldbescheid noch offen.
2. **Schweigen oder Stellungnahme?** — § 55 OWiG: Betroffener muss auf Anhörung nicht reagieren; Schweigen kann nicht nachteilig gewertet werden.
3. **Fahreridentifikation?** — Betroffener muss sich nicht als Fahrender identifizieren; Halter-Auskunft ist OWi-Pflicht (§ 31a StVG bei Halter-Anfrage), aber Fahrernennung ist freiwillig.
4. **Bussgeldbescheid bereits erlassen?** — Wenn ja: Einspruchsfrist 2 Wochen ab Zustellung (§ 67 Abs. 1 OWiG) pruefen.
5. **Zustellungsfiktion pruefen?** — § 33 Abs. 1 OWiG i.V.m. §§ 177-182 ZPO; Einwurf-Einschreiben.

## Zentrale Normen

- **§ 55 OWiG** — Anhörung des Betroffenen: Behörde muss hoeren; Betroffener muss nicht antworten
- **§ 55 Abs. 1 OWiG** — Schweigen ist nicht zu seinen Ungunsten zu verwenden
- **§ 66 OWiG** — Inhalt des Bussgeldbescheidss; Pflichtangaben nach § 66 Abs. 1 Nr. 1-7 OWiG
- **§ 67 Abs. 1 OWiG** — Einspruch: 2 Wochen ab Zustellung des Bussgeldbescheids
- **§ 67 Abs. 2 OWiG** — Beschraenkter Einspruch (nur Rechtsfolgen) moeglich
- **§ 33 OWiG i.V.m. §§ 177-182 ZPO** — Zustellungsvorschriften
- **§ 31a StVG** — Recht auf Fahrerauskunft (nur Halter-Auskunft, nicht Fahrernennung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anhörungsbogen — Strategie

```
Anhörungsbogen erhalten:
├─ EMPFEHLUNG: Nicht ausfullen, nicht zuruecksenden (Schweigen § 55 OWiG)
├─ Ausnahme: Fahreridentifikation offensichtlich aus anderen Quellen bekannt?
│ └─ Dann kann Einlassung zur Sache sinnvoll sein (selten)
└─ FALLFALLE: Unterschrift unter "Ich war der Fahrzeugfuehrer"
 → gilt als Gestaendnis der Fahrereigenschaft → nicht unterschreiben!
```

## Bussgeldbescheid — Pflichtinhalt nach § 66 OWiG

```
□ Name und Anschrift des Betroffenen (§ 66 Abs. 1 Nr. 1)
□ Tathandlung mit Zeit und Ort (§ 66 Abs. 1 Nr. 2)
□ Gesetzliche Merkmale der OWi (§ 66 Abs. 1 Nr. 3)
□ Angabe der verletzten Vorschrift (§ 66 Abs. 1 Nr. 4)
□ Hoehe der Geldbusse (§ 66 Abs. 1 Nr. 5)
□ Hinweis auf Fahrverbot wenn verhaengt (§ 66 Abs. 1 Nr. 5)
□ Belehrung ueber Einspruchsrecht (§ 66 Abs. 1 Nr. 7)

Fehlt ein Pflichtinhalt: Einspruch mit formaler Ruege!
```

## Einspruchsschrift-Template

```
An die [Bussgeldstelle] / Amtsgericht [ORT]
Az.: [AKTENZEICHEN]

Einspruch nach § 67 OWiG

Namens des Betroffenen [NAME] lege ich gegen den Bussgeldbescheid
vom [DATUM], zugestellt am [DATUM], fristgerecht

Einspruch

ein.

[Optional: Der Einspruch wird auf die Rechtsfolgen beschraenkt.]

Ich bitte um Uebersendung der vollstaendigen Verfahrensakte
einschliesslich Messakte.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Anhörungsbogen nicht selbst ausfullen lassen — Schweigerecht empfehlen.
- Einspruchsfrist 2 Wochen ab Zustellung (§ 67 OWiG) — sofort notieren.
- Bussgeldbescheid auf Pflichtinhalt nach § 66 OWiG pruefen.
- Anwaltliche Endkontrolle bei Einspruchsformulierung.

---

## Skill: `verkehrsowi-fahreridentifizierung`

_Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer nicht nennen. Normen: § 31a StVG (Halter-Auskunftspflicht und Fahrtenbuchauflage), § 55 OWiG (Aussageverweigerungsrecht). Prüfraster: Lichtbildabgleich AG, Sachverständigen-Ant..._

# Fahreridentifizierung im OWi-Verfahren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Ist der Betroffene eindeutig auf dem Messfoto identifizierbar?** — Qualitaet des Fotos entscheidend; unklares Foto = Angriffspunkt.
2. **Hat der Betroffene sich bereits als Fahrer identifiziert?** — Anhörungsbogen, Polizeivermerk, sonstige Aussagen.
3. **Ist die Halter-Auskunft (§ 31a StVG) bereits ergangen?** — Halter muss Auskunft geben; Fahrernennung ist freiwillig.
4. **Ist eine Fahrtenbuchauflage drohendes Thema?** — § 31a StVG: wenn Fahrer nicht ermittelt werden kann, kann Halter Fahrtenbuch fuehren muessen.
5. **Biometrischer Vergleich noetig?** — Sachverstaendiger wenn Foto-Identifikation streitig und für das Gericht nicht offenkundig.

## Zentrale Normen

- **§ 55 Abs. 1 OWiG** — Betroffener muss nicht zur Sache aussagen; kein Zwang zur Fahrernennung
- **§ 31a StVG** — Fahrtenbuchauflage: Halter, der Fahrerauskunft verweigert, kann Fahrtenbuchfuehrungs-Pflicht erhalten
- **§ 163b StPO i.V.m. § 46 OWiG** — Identitaetsfeststellung durch Polizei; begrenzt auf Personalien
- **§ 77 OWiG** — Beweisaufnahme: Sachverstaendiger für Lichtbild-Identifikation ist Beweisantrag
- **Art. 6 Abs. 1 EMRK** — Recht auf faires Verfahren; keine Pflicht zur Selbstbelastung
- **§ 261 StPO i.V.m. § 71 OWiG** — Freie Beweiswuerdigung; Richter darf Foto-Vergleich selbst vornehmen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Entscheidungsbaum Fahreridentifikation

```
Messfoto vorhanden?
├─ Qualitaet hoch, Fahrer eindeutig erkennbar
│ └─ Kein Angriffspunkt auf Identifikation; andere Strategie waehlen
├─ Qualitaet niedrig / Fahrer nicht eindeutig erkennbar
│ ├─ Sachverstaendigenantrag (§ 77 OWiG): "Lichtbild-Identifikation nicht moeglich"
│ └─ Bestreiten der Fahreridentitaet in der Hauptverhandlung
└─ Kein Messfoto (stationaere Anlage defekt / Video)
 └─ Fahreridentifikation durch andere Mittel pruefen (Zeugen, Protokoll)

Betroffener will nicht aussagen?
├─ § 55 OWiG: Schweigen ausdruecklich empfehlen
└─ Fahrtenbuchauflage-Risiko (§ 31a StVG) erklaeren
 └─ Halter muss abwaegen: OWi mit Fahrverbot vs. Fahrtenbuch 1-2 Jahre
```

## Fotoqualitatspruefung — Checkliste

```
□ Gesicht vollstaendig und frontal erkennbar?
□ Bildaufloesungnsstufe ausreichend?
□ Keine Ueberstrahlung / Spiegelreflektion im Bild?
□ Brillentraeger / Muetze / Maske als Identifikationshindernis?
□ Vergleichsbild für biometrischen Abgleich vorhanden?
□ Mehrere Personen im Fahrzeug — richtige Person identifiziert?
```

## Output-Template Sachverstaendigenantrag Lichtbild

```
In der Bussgeldsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Einholung eines Sachverstaendigen-Gutachtens
gemaess § 77 OWiG

Ich beantrage die Einholung eines Sachverstaendigen-Gutachtens
zur Frage, ob die auf dem Messfoto abgebildete Person identisch
ist mit dem Betroffenen [NAME].

Begruendung: Das vorliegende Messfoto weist [Bildqualitaetsmangel
beschreiben] auf. Eine laienhafte Beurteilung durch das Gericht
ist nicht ausreichend. [NAME] bestreitet, zum Tatzeitpunkt der
Fahrzeugfuehrer gewesen zu sein.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Fahreridentifikations-Zwang gibt es nicht — Schweigen ist legitim.
- Fahrtenbuchauflage dem Mandanten klar erklaeren — Konsequenz des Schweigens.
- Sachverstaendigenantrag bei schlechter Foto-Qualitaet stellen — nicht pauschal.
- Anwaltliche Endkontrolle bei Beweisantrag-Formulierung.

---

## Skill: `verkehrsowi-fristen-einspruch`

_Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG (Wiedereinsetzung), § 74 OWiG (Verwerfung bei Versaeumnis). Prüfraster: Zustellun..._

# Einspruchsfrist und Einspruch — § 67 OWiG

## Arbeitsbereich

Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG (Wiedereinsetzung), § 74 OWiG (Verwerfung bei Versaeumnis). Prüfraster: Zustellungsdatum und -art, Fristberechnung, Beschraenkter Einspruch § 67 Abs. 2 OWiG (nur Fahrverbot). Output Fristenblatt, Einspruchs-Template, ggf. Wiedereinsetzungsantrag. Abgrenzung: Inhalt des Einspruchs siehe verkehrsowi-beweisverwertung-standardisiert; Rechtsbeschwerde siehe verkehrsowi-rechtsbeschwerde. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Wann wurde der Bussgeldbescheid zugestellt?** — Ausgangspunkt der 2-Wochen-Frist § 67 Abs. 1 OWiG.
2. **Zustellungsform?** — Persoenliche Uebergabe, Einwurf-Einschreiben (§§ 33 OWiG, 180 ZPO), PZU.
3. **Mandant kennt Zugangsdatum?** — Falls unsicher: Zustellungsfiktion pruefen; für Mandanten spaetestes bekanntes Datum nehmen.
4. **Frist bereits abgelaufen?** — Wiedereinsetzungsantrag nach § 52 OWiG pruefen.
5. **Beschraenkt oder unbeschraenkt einlegen?** — § 67 Abs. 2 OWiG: Beschraenkung auf Rechtsfolgen moeglich.

## Zentrale Normen

- **§ 67 Abs. 1 OWiG** — Einspruch: 2 Wochen ab Zustellung des Bussgeldbescheids
- **§ 67 Abs. 2 OWiG** — Beschraenkter Einspruch auf Rechtsfolgen (Geldbusse, Fahrverbot)
- **§ 33 OWiG** — Zustellungsvorschriften: entsprechende Anwendung ZPO
- **§ 52 OWiG** — Wiedereinsetzung in den vorigen Stand nach § 44 StPO entsprechend
- **§ 74 OWiG** — Verwerfung des Einspruchs bei unentschuldigtem Ausbleiben
- **§ 28 OWiG** — Bekanntmachung des Bussgeldbescheids; Fristbeginn

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Fristen-Berechnungsschema

```
Zustellungsdatum: [DATUM]
+ 14 Tage: [DATUM + 14 Tage]
= Fristende: [DATUM]

Besonderheiten:
- Fristende Samstag/Sonntag/Feiertag → naechster Werktag (§ 43 StPO)
- Zustellungsfiktion § 180 ZPO: Einwurf-Einschreiben = 3 Tage nach Aufgabe
- Mandant im Urlaub/Krankenhaus → Wiedereinsetzungsgruende pruefen
```

## Entscheidungsbaum

```
Frist noch offen?
├─ Ja → Einspruch sofort formulieren und einlegen
│ ├─ Beschraenkt (nur Rechtsfolgen)? → § 67 Abs. 2 OWiG
│ └─ Unbeschraenkt → Standardvorgehen
└─ Nein (Frist abgelaufen)
 ├─ Kein Verschulden? → Wiedereinsetzung § 52 OWiG
 │ ├─ Krankheit, Urlaub, Fehler der Behörde
 │ └─ Eidesstattliche Versicherung + gleichzeitiger Einspruch
 └─ Verschulden → Bussgeldbescheid rechtskraeftig; Vollstreckung abwenden
```

## Output-Template Einspruchsschreiben

```
An die [Bussgeldstelle] / Amtsgericht [ORT]
Az.: [AKTENZEICHEN]

Einspruch nach § 67 OWiG

Namens des Betroffenen [NAME] lege ich gegen den Bussgeldbescheid
vom [DATUM DES BESCHEIDS], zugegangen am [ZUSTELLUNGSDATUM],
form- und fristgerecht

Einspruch

ein.

[Falls beschraenkt: Der Einspruch wird auf die festgesetzten
Rechtsfolgen beschraenkt. § 67 Abs. 2 OWiG.]

Ich bitte um Uebersendung der vollstaendigen Verfahrensakte
einschliesslich Messakte.

Anlage: Vollmacht [NAME]

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Frist unmittelbar nach Mandatsuebernahme berechnen und im Kalender eintragen.
- 3-Tage-Vorlauffrist-Erinnerung setzen.
- Beschraenkter Einspruch nur nach Mandantenruecksprache.
- Anwaltliche Endkontrolle vor dem Versand.

---

## Skill: `verkehrsowi-haertefall-fahrverbot`

_Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG (Geldbusse erhoehen als Alternative). Prüfraster: Berufsbedingte Angewiesenheit, Existe..._

# Haertefall-Argumentation beim Fahrverbot — § 25 StVG

## Arbeitsbereich

Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG (Geldbusse erhoehen als Alternative). Prüfraster: Berufsbedingte Angewiesenheit, Existenzgefaehrdung, OLG-Rspr Haertefall-Prüfung, Absehen vs. Verzoegerung Fahrverbot. Output Haertefall-Begründung, Antrag Absehen vom Fahrverbot oder Erhoehung Geldbusse. Abgrenzung: Punkte Flensburg siehe verkehrsowi-punkte-fahrverbot-flensburg; HV-Vorbereitung siehe verkehrsowi-hauptverhandlung-amtsgericht. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Wie hoch ist das Fahrverbot?** — § 25 StVG: 1 bis 3 Monate; Regelfahrverbot im BKat (Bussgeldkatalog) bei bestimmten Verstaessen.
2. **Ist der Mandant beruflich auf das Fahrzeug angewiesen?** — LKW-Fahrer, Vertreter, Pflegekraft, Taxi/Uber — Haertefall-Argumentation.
3. **Existenzgefaehrdung nachweisbar?** — Drohende Kuendigung, Arbeitslosenunterstuetzung nicht ausreichend, Eigentuemer Kleinstunternehmen.
4. **Gibt es mildernde Tatumstaende?** — Dringende Notsituation, techisches Versagen, minimale Ueberschreitung.
5. **Vier-Monats-Frist nutzbar?** — § 25 Abs. 2a StVG: Betroffener kann Beginn des Fahrverbots bis zu 4 Monate nach Rechtskraft hinauszogern (vorteilhaft für Urlaubszeit).

## Zentrale Normen

- **§ 25 Abs. 1 StVG** — Fahrverbot im OWi-Verfahren: 1 bis 3 Monate
- **§ 25 Abs. 2a StVG** — Vier-Monats-Frist: Betroffener kann Antritt bis 4 Monate nach Rechtskraft hinausschieben
- **§ 4 Abs. 1 BKatV** — Regelfahrverbot bei bestimmten Grenzwerten; kann unterschritten werden wenn Haertefall vorliegt
- **§ 17 Abs. 3 OWiG** — Geldbusse als Alternative; Erhoehung moeglich statt Fahrverbot
- **§ 44 StGB** — Fahrverbot als strafrechtliche Nebenstrafe (andere Regelung als § 25 StVG)

## Aktuelle Rechtsprechung

- OLG Frankfurt a.M., Beschl. v. 18.3.2021 - 2 Ss OWi 148/21 (NZV 2021, 448 — Volltext über openjur.de oder offene Justizdatenbank Hessen verifizieren): Berufsbedingte Angewiesenheit ist typischerweise kein Haertefall; der Betroffene muss zusaetzlich darlegen, dass keine Alternative zum Selbstfahren besteht und Existenzgefaehrdung nachweisbar ist.
- Weitere OLG-Linien (Bayerisches Oberstes Landesgericht, OLG Hamm, OLG Düsseldorf u.a.): konkrete Aktenzeichen vor Versand in openjur.de oder offenen Landesjustiz-Datenbanken aufrufen.
- BVerfG zum Verhältnismäßigkeitsgrundsatz bei Fahrverbot: laufende Linie; Aktenzeichen vor Versand in bundesverfassungsgericht.de verifizieren.

## Haertefall-Argumentation — Checkliste

```
BERUFLICHE ANGEWIESENHEIT (schwache Argumentation allein):
□ Berufsbezeichnung (LKW-Fahrer, Handelsvertreter, etc.)
□ Fahrzeug notwendig für Berufsausuebung
□ Keine Moeglichkeit oeff. Nahverkehr zu nutzen (Nachweis?)

EXISTENZGEFAEHRDUNG (staerkere Argumentation):
□ Drohende Kuendigung durch Arbeitgeber (Bescheinigung!)
□ Arbeitnehmerarbeitgeber-Bescheinigung: "Fahrverbot = Kuendigung"
□ Selbststaendiger: Einnahmenausfall konkret beziffert (BWA)
□ Minijobber / Sozialhilfebeziehende: Existenzminimum betroffen
□ Keine Alternative vorhanden (keine Mitfahrer, kein Taxi zu vertretbaren Kosten)

MILDERNDE TATUMSTAENDE:
□ Erstverstos (kein Vorvergehen im BZR Flensburg)
□ Minimale Geschwindigkeitsueberschreitung an der Grenze zum Fahrverbot
□ Besondere Notlage zur Tatzeit (medizinischer Notfall, etc.)
□ Ueberlange Verfahrensdauer (> 2 Jahre seit Tat)

VIER-MONATS-FRIST (§ 25 Abs. 2a StVG):
□ Antrag auf Verschiebung des Fristbeginns (z.B. auf Urlaubszeit)
□ Zustimmung des Gerichts einholen
□ Zeitplanung mit Mandant abstimmen
```

## Schritt-für-Schritt-Workflow

1. **Mandant ueber realistische Chancen aufklaeren** — Haertefall ist selten anerkannt.
2. **Beweise sammeln:** Arbeitgeber-Bescheinigung, Einkommensnachweis, Alternativennachweis (OEPNV nicht erreichbar).
3. **Vier-Monats-Frist als Alternative:** Wenn Haertefall nicht durchsetzbar, Fristverschiebung nach § 25 Abs. 2a StVG beantragen.
4. **Absehen vom Fahrverbot beantragen:** Statt Fahrverbot erhoehte Geldbusse; § 17 Abs. 3 OWiG i.V.m. § 4 Abs. 4 BKatV.
5. **In der HV:** Haertefall-Argumente konkret und mit Belegen vortragen; pauschale Berufsnotwendigkeit genuegt nicht.

## Harte Leitplanken

- Haertefall ohne Belege wird nicht anerkannt — Bescheinigungen und Nachweise zwingend.
- Vier-Monats-Frist immer als Rueckfall-Option vorbereiten.
- Mandant realistisch informieren — Fahrverbot ist die Regel, Ausnahme ist die Ausnahme.
- Anwaltliche Endkontrolle bei Haertefall-Argumentation.

---

## Skill: `verkehrsowi-hauptverhandlung-amtsgericht`

_Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG (Strafmass). Prüfraster: Beweisanträge (Sachverständiger, Zeugen), Einlassung oder Sc..._

# Hauptverhandlung OWi am Amtsgericht

## Arbeitsbereich

Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG (Strafmass). Prüfraster: Beweisanträge (Sachverständiger, Zeugen), Einlassung oder Schweigen, Strafmass-Erwaegungen, Abwesenheitsmöglichkeit § 74 OWiG. Output HV-Vorbereitungs-Checkliste, Beweisantrags-Entwuerfe. Abgrenzung: Rechtsbeschwerde danach siehe verkehrsowi-rechtsbeschwerde; Haertefall vor HV siehe verkehrsowi-haertefall-fahrverbot. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — Checkliste vor der HV

1. **Erscheinungspflicht?** — § 73 Abs. 1 OWiG: Betroffener kann von Erscheinungspflicht entbunden werden; auf Antrag. Verteidiger kann allein erscheinen (§ 73 Abs. 3 OWiG).
2. **Beweisantraege formuliert?** — § 77 OWiG: Beweisantraege moegen vorbereitet sein; konkretes Beweisthema + Beweismittel.
3. **Einlassung oder Schweigen?** — § 55 OWiG: Schweigen neutral; Einlassung nur wenn strategisch vorteilhaft.
4. **Verstaendigungsangebot gemacht?** — Informelle Gespraech mit Staatsanwalt oder Richter vor HV.
5. **Rechtsbeschwerde vorbereitbar?** — § 79 OWiG: Nur bei Geldbusse > 250 EUR oder Fahrverbot; Revisionsbegrenzt auf Rechtsfehler.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§ 71 OWiG** — Hauptverhandlung: gilt StPO entsprechend soweit OWiG nichts anderes regelt
- **§ 73 OWiG** — Erscheinungspflicht: Absehen, Entbindung; Verteidiger kann allein erscheinen
- **§ 74 OWiG** — Verwerfung des Einspruchs bei unentschuldigtem Ausbleiben
- **§ 77 OWiG** — Beweisantraege: Ablehnungsgruende eng; Sachverstaendigenrecht
- **§ 17 OWiG** — Geldbusse: Zubemassung nach Schwere und Einkommen
- **§ 79 OWiG** — Rechtsbeschwerde: zulaessig bei Geldbusse > 250 EUR oder Fahrverbot
- **§ 80 OWiG** — Zulassung der Rechtsbeschwerde bei grundsaetzlicher Bedeutung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorbererungs-Checkliste (1 Woche vor HV)

```
□ Messakte vollstaendig ausgewertet?
□ Sachverstaendigenantrag formuliert (wenn noetig)?
□ Einlassung oder Schweigen entschieden?
□ Haertefall-Argument (Fahrverbot) vorbereitet?
□ Entbindungsantrag (§ 73 OWiG) gestellt?
□ Verstaendigung mit Gericht/StA sondiert?
□ Mandant ueber HV-Ablauf informiert?
□ Rechtsbeschwerde-Strategie vorgedacht?
```

## Ablauf-Schema HV OWi

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

```
1. Aufruf der Sache (§ 243 StPO i.V.m. § 71 OWiG)
2. Feststellung Erscheinen aller Beteiligten
3. Ggf. Einspruchsverwerfungsantrag der StA? → widersprechen
4. Verlesung Anklage (Tatvorwurf)
5. Belehrung Betroffener § 55 OWiG (Schweigerecht)
6. Einlassung oder Schweigen
7. Beweisaufnahme:
 a) Zeugen (Polizeibeamte)
 b) Urkundsbeweis (Messprotokoll, Eichschein)
 c) Sachverstaendiger (wenn beantragt und zugelassen)
8. Schlussvortrag Staatsanwaltschaft
9. Plaedoyer Verteidiger
10. Letztes Wort Betroffener
11. Urteil (Freispruch / Geldbusse / Fahrverbot)
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — OWi-Hauptverhandlung am Amtsgericht fuehren | Plaedoyer nach Schema; Template unten |
| Variante A — Mandant will Einspruch zuruecknehmen vor HV | Einspruchsruecknahme statt HV; Bussgeldbescheid wird rechtskraeftig |
| Variante B — Freispruch unrealistisch Strafmass im Fokus | Strafzumessungs-Plaedoyer; Fahrverpflichtung pruefen |
| Variante C — Rechtsbeschwerde bereits im Blick | Verteidigungsstrategie HV auf Rechtsbeschwerde ausrichten; Protokollfuehrung beachten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzkern Plaedoyer OWi

```
Sehr geehrtes Gericht,

[Zusammenfassung der Beweisaufnahme aus Sicht der Verteidigung]

Die Messung ist aus folgenden Gruenden anzuzweifeln:
[Konkreter Angriffspunkt 1]
[Konkreter Angriffspunkt 2]

Strafzumessung: Bei Verurteilung beantrage ich Absehen vom
Fahrverbot / Herabsetzung der Geldbusse, weil:
[Haertefall / mildernde Umstaende / Erstverstos]

Antrag: Freispruch / Einstellung / Geldbusse von [X] EUR
ohne Fahrverbot.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Harte Leitplanken

- Sachverstaendigenantrag vor Schluss der Beweisaufnahme stellen.
- Letztes Wort des Betroffenen niemals vergessen.
- Entbindungsantrag rechtzeitig (vor HV) stellen.
- Rechtsbeschwerde nur bei Geldbusse > 250 EUR oder Fahrverbot; sonst kein Rechtsmittel.
- Anwaltliche Endkontrolle bei Plaedoyer und Antraegen.

---

## Skill: `verkehrsowi-kommandocenter`

_Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf, Frist, Fahrverbot-Risiko, Punkte), Routing auf Subskills. Output Deal-Karte OWi..._

# VerkehrsOWi-Verteidiger — Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
| Anhörung / Bussgeldbescheid-Pruefung | `verkehrsowi-anhoerung-bussgeldbescheid` |
| Haertefall Fahrverbot | `verkehrsowi-haertefall-fahrverbot` |
| Punkte in Flensburg | `verkehrsowi-punkte-fahrverbot-flensburg` |
| Hauptverhandlung Amtsgericht | `verkehrsowi-hauptverhandlung-amtsgericht` |
| Rechtsbeschwerde | `verkehrsowi-rechtsbeschwerde` |
| Zeugen Polizei Strategie | `verkehrsowi-zeugen-polizei-strategie` |
| Rotlicht Abstand Handy | `verkehrsowi-rotlicht-abstand-handy` |
| Verjährung Zustellung | `verkehrsowi-verjaehrung-zustellung` |
| Mandantenkommunikation | `verkehrsowi-mandantenkommunikation` |
| Quality Gate | `verkehrsowi-quality-gate` |

## Zentrale OWi-Normen im Ueberblick

- **§ 24 StVG** — Ordnungswidrigkeiten im Strassenverkehr allgemein
- **§ 24a StVG** — Alkohol (0,5 Promille) und Drogen
- **§ 25 StVG** — Fahrverbot 1-3 Monate
- **§ 26 StVG** — Zuständigkeit Bussgeldbehoerde
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

---

## Skill: `verkehrsowi-punkte-fahrverbot`

_Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8 Pkt), § 65 StVG (Tilgungsfristen), § 25 StVG (Fahrverbot als Denkzettel). Prüfraste..._

# Punkte und Fahrverbot — Fahreignungsregister Flensburg

## Arbeitsbereich

Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8 Pkt), § 65 StVG (Tilgungsfristen), § 25 StVG (Fahrverbot als Denkzettel). Prüfraster: Punktestand, Tilgungsfristen, freiwilliger Kurs zur Punkte-Reduzierung, Abgrenzung FAER-Punkte vs. Fahrverbot. Output Punkte-Berechnungs-Übersicht, Strategie-Empfehlung. Abgrenzung: Haertefall-Fahrverbot siehe verkehrsowi-haertefall-fahrverbot; Fahrerlaubnisentzug MPU siehe fachanwalt-verkehrsrecht-Plugin. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Aktueller Punktestand?** — Mandant soll FAER-Auskunft beim KBA beantragen (§ 30 StVG).
2. **Neue Eintragung droht?** — Nach Bussgeldbescheid oder Verurteilung: wann wird eingetragen?
3. **Wie viele Punkte nach neuer Eintragung?** — Warnstufen nach § 4 Abs. 5 StVG: bei 4 Punkten Ermahnung, bei 6 Punkten Verwarnung, bei 8 Punkten Entzug.
4. **Tilgungsfristen laufen?** — § 65 StVG: Punktetilgung nach Ablauf der Tilgungsfrist (2,5 oder 10 Jahre je nach Eintragungsart).
5. **Freiwilliger Kurs moeglich?** — Nach § 4 Abs. 7 StVG: bei Punkt-Level 1-5 kann Kurs 1 Punkt reduzieren.

## Zentrale Normen

- **§ 4 StVG** — Fahreignungs-Bewertungssystem: Eintragungen, Warnstufen, Konsequenzen
- **§ 4 Abs. 5 StVG** — Stufensystem: 1-3 Punkte (keine Massnahme), 4-5 Punkte (Ermahnung), 6-7 Punkte (Verwarnung), 8+ Punkte (Entziehung)
- **§ 4 Abs. 7 StVG** — Freiwilliger Kurs: 1 Punkt-Reduktion moeglich bei <= 5 Punkten
- **§ 30 StVG** — Recht auf Auskunft aus dem FAER
- **§ 65 StVG** — Tilgungsfristen: Grundregel 2,5 Jahre; Ausnahme (z.B. Straftaten mit Entziehung) 10 Jahre
- **§ 66 StVG** — Tilgungshemmung bei neuer Eintragung innerhalb der Tilgungsfrist
- **§ 25 StVG** — Fahrverbot (separate Sanktion, keine Punkte-Konsequenz an sich)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Punkte-Tabelle nach BKatV (Auswahl)

| Verstos | Punkte |
|---------|--------|
| Geschwindigkeit 31-40 km/h uber Erlaubnis | 1 Punkt |
| Geschwindigkeit 41-60 km/h uber Erlaubnis | 2 Punkte |
| Geschwindigkeit 61-70 km/h uber Erlaubnis | 2 Punkte + Fahrverbot |
| Rotlicht-Verstos 1 Sekunde | 1 Punkt |
| Rotlicht-Verstos qualifiziert (> 1s) | 2 Punkte + Fahrverbot |
| Abstandsunterschreitung < 4/10 Fahrbahn (> 100 km/h) | 1 Punkt |
| Handy am Steuer | 1 Punkt |
| § 316 StGB (Trunkenheitsfahrt) | 3 Punkte + Fahrerlaubnis-Entzug |

## Tilgungsfristen (§ 65 StVG)

| Eintragungsart | Tilgungsfrist |
|---------------|--------------|
| 1-Punkt-Eintragung | 2,5 Jahre |
| 2-Punkt-Eintragung | 5 Jahre |
| Straftaten (ohne Entziehung) | 5 Jahre |
| Straftaten (mit Fahrerlaubnis-Entziehung) | 10 Jahre |

## Schritt-für-Schritt-Workflow

1. **FAER-Auskunft beantragen** (§ 30 StVG) — Mandant beim KBA Flensburg (Kraftfahrtbundesamt).
2. **Punktestand berechnen** nach neuer Eintragung.
3. **Tilgungsfristen pruefen:** Laufen alte Eintragungen demnachst aus?
4. **Kursoption pruefen:** <= 5 Punkte → freiwilliger Kurs nach § 4 Abs. 7 StVG.
5. **MPU-Risiko pruefen:** Bei Alkohol- oder Drogendelikten koennen Behörden MPU anordnen.
6. **Verwaltungsrechtlichen Weg einschlagen** bei unberechtigter Eintragung (Widerspruch, VG-Klage).

## Harte Leitplanken

- Punkte koennen nicht "verhandelt" werden — Eintragung ist automatisch nach Rechtskraft.
- Tilgungshemmung durch neue Eintragung beachten.
- Freiwilliger Kurs nur bei <= 5 Punkten wirksam.
- Anwaltliche Endkontrolle bei Kursempfehlung und Verwaltungsrechtsstrategie.

---

## Skill: `verkehrsowi-quality-gate`

_Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: § 67 OWiG (Einspruch), § 77 OWiG (HV-Beweisanträge), BVerfG Rohmessdaten. Prüfraster: Messakte vollständig, Rohmessdaten vorhanden, Eichschein geprüft, Fahrverbot-Haertefall-Prüf..._

# Quality Gate — OWi-Mandat

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Gate 1: Vor Einspruch-Versand

```
□ Einspruchsfrist § 67 Abs. 1 OWiG berechnet und noch offen?
 Zustellungsdatum: [DATUM] + 14 Tage = Fristende: [DATUM]
□ Vollmacht des Betroffenen liegt vor?
□ Bussgeldbescheid auf Pflichtinhalt § 66 OWiG geprueft?
□ OWi oder Strafrecht? (Grenzwert BAK § 316 StGB vs. § 24a StVG)
□ Einspruch beschraenkt (§ 67 Abs. 2) oder unbeschraenkt?
□ Mandant hat Anhörungsbogen NICHT ausgefuellt?
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
□ Verjährung geprueft (§ 26 Abs. 3 StVG, § 33 OWiG)?
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

---

## Skill: `verkehrsowi-rechtsbeschwerde`

_Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG (Zulassungsbeschwerde), § 344 StPO i.V.m. § 79 Abs. 3 OWiG (Begründungspflicht), Frist 1 W..._

# Rechtsbeschwerde im OWi-Verfahren — § 79 OWiG

## Arbeitsbereich

Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG (Zulassungsbeschwerde), § 344 StPO i.V.m. § 79 Abs. 3 OWiG (Begründungspflicht), Frist 1 Woche ab Urteil. Prüfraster: Statthaftigkeit, Verfahrensruege vs. Sachruege, Formalanforderungen, OLG als Rechtsbeschwerdeinstanz. Output Rechtsbeschwerde-Schrift. Abgrenzung: Einspruch gegen Bußgeldbescheid siehe verkehrsowi-fristen-einspruch; HV vorher siehe verkehrsowi-hauptverhandlung-amtsgericht. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Ist Rechtsbeschwerde zulaessig?** — § 79 Abs. 1 OWiG: zulaessig bei Geldbusse > 250 EUR ODER Fahrverbot; ansonsten nur Zulassungsbeschwerde nach § 80 OWiG.
2. **Welches Gericht ist zuständig?** — OLG im jeweiligen Bundesland (Ausnahme: bei Grundsatzfragen auch BGH denkbar, sehr selten).
3. **Was soll angegriffen werden?** — Rechtsfehler (Verfahrensruege oder Sachruge); keine Tatsachenpruefung in der Rechtsbeschwerde!
4. **Frist beachten?** — 1 Woche ab Urteilsverkuendung; Begründungsfrist 1 Monat ab Urteilszustellung (§ 79 Abs. 3 OWiG i.V.m. § 345 StPO).
5. **Kostenrisiko?** — Bei erfolgloser Rechtsbeschwerde: Gebühren + ggf. Kosten der Gegenpartei.

## Zentrale Normen

- **§ 79 Abs. 1 OWiG** — Rechtsbeschwerde: Geldbusse > 250 EUR oder Fahrverbot
- **§ 79 Abs. 3 OWiG i.V.m. § 344 StPO** — Ruegeformen: Verfahrensruege und Sachruge
- **§ 79 Abs. 3 OWiG i.V.m. § 345 StPO** — Begründungsfrist 1 Monat ab Zustellung Urteilsgruende
- **§ 80 OWiG** — Zulassungsbeschwerde: bei Geldbusse <= 250 EUR; nur bei grundsaetzlicher Bedeutung oder Fortbildung des Rechts
- **§ 341 StPO i.V.m. § 79 Abs. 3 OWiG** — Einlegungsfrist 1 Woche ab Urteilsverkuendung
- **§ 338 StPO i.V.m. § 79 OWiG** — Absolute Revisionsgründe gelten auch in der Rechtsbeschwerde

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Pruefschema Rechtsbeschwerde-Zulaessigkeit

```
§ 79 Abs. 1 OWiG — Zulaessigkeit:
□ Geldbusse > 250 EUR ODER Fahrverbot? → Rechtsbeschwerde zulaessig
□ Geldbusse <= 250 EUR, kein Fahrverbot? → Nur Zulassungsbeschwerde § 80 OWiG

Fristen:
□ Einlegungsfrist: 1 Woche ab Urteilsverkuendung
□ Begründungsfrist: 1 Monat ab Zustellung der Urteilsgruende
□ Urteilszustellung abwarten (ergibt Begründungsfrist-Start)

Ruegeformen:
□ Verfahrensruege: konkreter Verfahrensverstos (Sachverstaendigenantrag, Belehrung)
□ Sachrüge: Fehler bei der Anwendung des materiellen Rechts
```

## Verfahrensruegen — typische Angriffspunkte

```
1. Ablehnung Sachverstaendigenantrag (§ 77 OWiG) ohne Begruendung
2. Verletzung rechtliches Gehoer (Art. 103 GG): Rohmessdaten verweigert
3. Keine ordnungsgemaesse Belehrung ueber Schweigerecht (§ 55 OWiG)
4. Messgeraet nicht gesetzlich geeicht (§ 6 MessEG)
5. Urteilsbegruendung widerspricht sich selbst (§ 267 StPO i.V.m. § 71 OWiG)
6. Letztes Wort verweigert (§ 258 Abs. 3 StPO i.V.m. § 71 OWiG)
```

## Output-Template Rechtsbeschwerdeschrift

```
An das OLG [ORT]
[Anschrift]

In der OWi-Sache gegen [NAME]
Az. AG: [AKTENZEICHEN]

Rechtsbeschwerde nach § 79 OWiG

Namens des Betroffenen [NAME] lege ich gegen das Urteil des
Amtsgerichts [ORT] vom [DATUM] frist- und formgerecht

Rechtsbeschwerde

ein. Die Urteilsgruende sind noch nicht zugestellt; die Begründung
erfolgt innerhalb der gesetzlichen Frist nach § 79 Abs. 3 OWiG.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Rechtsbeschwerde nur bei Rechtsfehler — keine Tatsachenpruefung!
- Begründungsfrist 1 Monat nach Urteilszustellung — nicht nach Verkuendung!
- Zulassungsbeschwerde bei Geldbusse <= 250 EUR: Grundsatzrechtsfrage benennen.
- Anwaltliche Endkontrolle bei Ruge-Formulierung.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

