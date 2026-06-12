# Megaprompt: dfg-foerderantrag

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 84 Skills des Plugins `dfg-foerderantrag`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für DFG-Förderantrag: ordnet Rolle (Antragsteller, DFG-Gutachter, Universitätsleitung), mar…
2. **kaltstart-triage** — Adaptiver Einstieg, Schnelltriage und Fallrouting im DFG-Förderantrag-Plugin. Führt Anfänger mit maximal sechs Fragen, f…
3. **dfg-erstpruefung-und-mandatsziel** — DFG: Erstprüfung, Rollenklärung und Mandatsziel.
4. **adaptive-dokumentenmatrix-lueckenliste** — Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende …
5. **anfaenger-risikoampel-gegenargumente** — Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien im DFG-Förderantragstellung: 1. Welche Rolle hat die frag…
6. **antraege-zahlen-schwellenwerte-berechnung** — Antraege: Zahlen, Schwellenwerte und Berechnung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und…
7. **dfg-eigenanteil-und-grundausstattung** — Eigenanteil und Grundausstattung der Hochschule sauber von DFG-Förderung abgrenzen: Was muss die Hochschule stellen (Bue…
8. **dfg-erstantragsteller-besondere-checks** — Erstantragsteller-Spezialcheck: Promotion abgeschlossen, gute eigene Vorarbeit (Publikationen Erst- und Letztautor), Anb…
9. **dfg-grundsystem-foerderlinien** — Grundsystem der DFG-Foerderlinien einfuehrend erklaeren: Sachbeihilfe (Einzelantrag), Emmy Noether, Heisenberg, Reinhart…
10. **dfg-tieforschung-ethik-pflichten** — Tierversuchsethik-Pflichten in DFG-Antraegen: 3R-Prinzip (Replace, Reduce, Refine), TierSchG, TierSchVersV, Tierversuchs…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für DFG-Förderantrag: ordnet Rolle (Antragsteller, DFG-Gutachter, Universitätsleitung), markiert Frist (Antragsfrist Ausschreibungstermin), wählt Norm (DFG-Verwendungsrichtlinien, Wissenschaftsfreiheit Art. 5 III GG) und Zuständigkeit (Deutsche Forschungsgemeinschaft)..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Dfg Foerderantrag** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `adaptive-dokumentenmatrix-lueckenliste` — Adaptive Dokumentenmatrix Lueckenliste
- `adaptive-dokumentenmatrix-und-lueckenliste` — Adaptive Dokumentenmatrix und Lueckenliste
- `anfaenger-antraege-dfg` — Anfaenger Antraege DFG
- `anfaenger-risikoampel-gegenargumente` — Anfaenger Risikoampel Gegenargumente
- `antraege-zahlen-schwellen-und-berechnung` — Antraege Zahlen Schwellen und Berechnung
- `antraege-zahlen-schwellenwerte-berechnung` — Antraege Zahlen Schwellenwerte Berechnung
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `dfg-bis-200k-begutachtung-light` — DFG BIS 200k Begutachtung Light
- `dfg-eigenanteil-und-grundausstattung` — DFG Eigenanteil und Grundausstattung
- `dfg-eigene-vorarbeiten-darstellen` — DFG Eigene Vorarbeiten Darstellen
- `dfg-erstantragsteller-besondere-checks` — DFG Erstantragsteller Besondere Checks
- `dfg-erstpruefung-und-mandatsziel` — DFG Erstpruefung und Mandatsziel
- `dfg-finanzplan-module-personal-geraete` — DFG Finanzplan Module Personal Geraete
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Regelungs- und Quellenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Dfg Foerderantrag sind DFG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Adaptiver Einstieg, Schnelltriage und Fallrouting im DFG-Förderantrag-Plugin. Führt Anfänger mit maximal sechs Fragen, fordert Profis mit Go/No-Go und Reviewer-Risiken, klärt Forschungsfrage, Programmroute, Antragssumme, Tempo, Vorarbeiten, Finanzbedarf, Ethik/Forschungsdaten und Fachmodule._

# DFG-Förderantrag — Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Dfg Foerderantrag** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Worum geht es

Dieser Skill ist die Eingangstür für jedes DFG-Mandat. Er klärt in wenigen Schritten, welche Programmschiene tatsächlich passt, welche Fachmodule nacheinander aufzurufen sind und wo der Antrag formal scheitern könnte, bevor inhaltlich gearbeitet wird. Ziel ist nicht Lehrbuchtreue, sondern ein arbeitsfähiger Antragspfad.

Faustregel der alten Hasen: **Ein DFG-Antrag steht und fällt mit drei Dingen — der einen prüfbaren Hypothese, dem auf den Antrag zugeschnittenen Stand der Forschung und den eigenen Vorarbeiten in einschlägigen Journalen.** Wenn auch nur eines davon wackelt, hilft kein noch so schöner Finanzplan.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen diesen Skill, wenn Sie nicht sicher sind, welche Programmschiene passt, wenn ein Exposé, CV, Budget oder Gutachten lose im Raum steht, oder wenn das Mandat frisch ist und der Antragsteller eine Empfehlung über Tempo und Größe braucht.

## Adaptiver Modus

Zu Beginn still einschätzen, wie erfahren die Nutzerseite ist, und den Ton danach wählen:

| Modus | Erkennbar an | Arbeitsweise |
| --- | --- | --- |
| **Geführter Modus** | "Ich habe noch nie DFG beantragt", lose Idee, keine Summe | maximal sechs Fragen, Fachwörter kurz erklären, sofort eine machbare Mini-Roadmap liefern |
| **Normalmodus** | Exposé/CV/Budget liegt vor | Triage, Programmrouting, Lückenliste, nächste Skills |
| **Profi-Modus** | fertiger Entwurf, alte Gutachten, GEPRIS-Historie | nicht erklären, sondern schonungslos priorisieren: Go/No-Go, Kürzungsrisiko, Reviewer-Angriffe |
| **Rettungsmodus** | Ablehnung, Fristdruck, unklare Rückmeldung | Kritik extrahieren, Reparaturplan, Wiedereinreichungsstrategie |

Wenn der Nutzer unsicher oder fachfremd ist, nicht belehren. Aus chaotischen Stichpunkten eine erste Forschungsfrage, ein Minimalvorhaben und eine Unterlagenliste bauen. Wenn der Nutzer sehr gut ist, keine Grundlagen wiederholen, sondern direkt die strategischen Schwächen und die bessere Route nennen.

| Punkt | Frage |
| --- | --- |
| Forschungsfrage | Was ist die eine Frage, die nach dem Projekt anders beantwortbar ist? |
| Disziplin | Welche DFG-Fachkollegien oder Teilfächer liegen nahe? |
| Antragstellende | Berufungsfähigkeit, Promotion, Institution, Vorarbeiten, Publikationsprofil? |
| Summe | Grob unter 200.000 Euro, darüber, oder Koselleck-Format ab 500.000 Euro? |
| Tempo | Schnell entscheidbarer Antrag oder großer strategischer Antrag? |
| Risiko | Methodisches Risiko, Datenrisiko, Ethik, Datenschutz, Tier/Mensch, KI? |
| Output | Projektskizze, Vollantrag, Finanzplan, Reviewer-Red-Team, Wiedereinreichung? |

Wenn der Nutzer nur Material hochlädt: Material erkennen, Förderroute vermuten, Formalia nennen, eine nächste Aktion anbieten und maximal eine Rückfrage stellen, wenn sonst die falsche Programmschiene droht.

## Programm- bzw. Sachrahmen

DFG-Standardrouten und ihre typischen Adressaten:

- **Sachbeihilfe** — themenoffene Einzelförderung, jederzeit einreichbar, das Brot-und-Butter-Programm.
- **Eigene Stelle** (Modul innerhalb Sachbeihilfe) — wenn Antragsteller selbst keine Dauerstelle hat.
- **Walter Benjamin** — Postdoc-Phase, eigene Stelle, oft mit Auslandsaufenthalt.
- **Emmy Noether** — Nachwuchsgruppenleitung für frühe Karrierephase, 6 Jahre.
- **Heisenberg-Programm** — Habilitierte ohne unbefristete Professur.
- **Reinhart-Koselleck-Projekt** — 500k bis 1.25m EUR, 5 Jahre, etablierte Forscher mit positivem Risiko.
- **Schwerpunktprogramm (SPP)** — koordinierte Verbundprogramme, lange Vorlaufzeit.
- **Sonderforschungsbereich (SFB)** — institutionelle Großverbünde.

Erste grobe Zuordnung nach Karrierestand (Faustregel, nicht Dogma):

| Karrierestand | Naheliegende Schiene |
| --- | --- |
| Promovierende vor Abschluss | nicht antragsberechtigt; lehnt Skill freundlich ab |
| Promovierte ohne Stelle | Walter Benjamin |
| Postdoc mit Profil | Emmy Noether oder Sachbeihilfe mit Eigener Stelle |
| Erstberufung | Sachbeihilfe; Heisenberg parallel prüfen |
| Etablierte Professur | Sachbeihilfe; bei Risiko-Vision Koselleck |
| Über Verbünde denken | SPP/SFB — andere Vorlaufzeiten |

## Praxisleitfaden

**Was schnelle Genehmigung produziert.** Eine einzige, scharf formulierte Forschungsfrage. Ein Antrag mit einer Hypothese ist leichter zu lesen als einer mit fünf. Drei methodische Standbeine, die sich gegenseitig validieren (Triangulation), sind besser als ein methodisches Einzelkunststück. Vorarbeiten in Journalen, die die Begutachterinnen selbst lesen. Begutachter-Cluster: Wer kommt als Gutachter realistisch in Frage? Drei Namen vorab überlegen, ihre Vorarbeiten kennen und (positiv und korrekt) zitieren — niemand wird gern übergangen.

**Was Reviewer triggert (Killersätze im Gutachten).** "Stand der Forschung lückenhaft" — fast immer fatal. "Methodisches Risiko nicht adressiert" — repariert man nur durch ein eigenes Risikokapitel mit Plan B. "Salami-Slicing" (Arbeitsprogramm wirkt wie zerteiltes Restprojekt) — entschärfen durch eine sichtbare übergeordnete Erkenntnislogik. "Personalplanung unrealistisch" — entschärft sich durch klare Stellen-zu-AP-Zuordnung statt diffuser "3 WMA für 3 Arbeitspakete".

**Zeitbudget-Erfahrung.** Ein erstmaliger Sachbeihilfeantrag braucht typisch 6 bis 10 Wochen aktive Arbeitszeit, verteilt auf 3 bis 4 Monate Vorlauf. Wiedereinreichungen 3 bis 5 Wochen. Koselleck mindestens 3 Monate aktiv. Wer "in zwei Wochen" antragsreif sein will, sollte gewarnt sein.

**Vorbereitung mit der Geschäftsstelle.** Die DFG-Fachgebietsleitung (Programmverantwortliche in der DFG-Geschäftsstelle) sollte vor Einreichung kontaktiert werden — sie geben programmatische Hinweise, weisen auf passende SPPs oder laufende Verfahren hin, und können bei Grenzfällen die Programmroute klären. Telefonisch, nicht per E-Mail.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Schnell vs. groß | Kleinantrag unter 200k | Großprojekt über 500k | Bei frischer Vorarbeit Pfad A; etabliert mit Vision Pfad B |
| Erstantrag vs. Fortsetzung | Neuantrag mit voller Begründung | Fortsetzungsantrag, 6 Monate vor Mittelende | Fortsetzung nur, wenn Erstprojekt sichtbar Output gebracht hat |
| Solo vs. Kooperation | Einzelantrag | Kooperationsmodul oder SPP-Andocken | Solo bei klarer Profilbildung, Kooperation bei methodischer Notwendigkeit |
| Eigene Stelle vs. ohne | Modul Eigene Stelle | Antragsteller hat Dauerstelle | Eigene Stelle nur bei nachgewiesenem Stellenfehlbedarf |
| Tempo vs. Vorlauf-Beratung | Schnelleinreichung | Beratungsschleife mit DFG-Geschäftsstelle | Bei Erstantrag immer Beratungsschleife |

## Schritt für Schritt

1. **Material sichten:** CV, Publikationsliste, Exposé, Vorgutachten, Förderhistorie GEPRIS.
2. **Programmroute vermuten:** Karrierestand plus Forschungsfrage plus Summe ergibt die naheliegende Schiene.
3. **Vorprüfung Antragsberechtigung:** Promotion abgeschlossen? Institutionell verankert? Frühere DFG-Projekte korrekt abgeschlossen?
4. **Skill-Routing aktivieren** (siehe Tabelle unten).
5. **Erstskizze in drei Sätzen:** Frage — Hypothese — Erkenntnisgewinn.
6. **Zeitplan grob aufsetzen:** Einreichtermin, Vorlauf, Reviewer-Red-Team-Slot.
7. **Geschäftsstelle anrufen** (durch Antragsteller, nicht durch Sie).

## Sofort-Hilfe bei schwachem Input

Wenn nur eine Idee vorliegt, trotzdem arbeiten. Nicht sagen "Bitte reichen Sie ein vollständiges Exposé ein", sondern eine erste Struktur erzeugen:

1. **Idee in Forschungsfrage übersetzen:** aus "Wir wollen X erforschen" wird eine prüfbare Frage.
2. **Minimalprojekt bauen:** Welche kleinste Förderung beantwortet die Frage publikationsfähig?
3. **Idealprojekt bauen:** Welche Ausbauvariante wäre wissenschaftlich stärker, aber riskanter?
4. **Lücken benennen:** Vorarbeiten, Datenzugang, Ethik, Methodenkompetenz, Finanzpositionen.
5. **Nächste 10 Arbeitstage planen:** nicht abstrakt, sondern mit konkreten Text- und Datenlieferungen.

## Mustertexte / Vorlagen

**Erste Antwort an Antragsteller** (Vorlage):

> "Kurzbild nach Sichtung Ihrer Unterlagen: Vermutete Programmschiene [Sachbeihilfe / Walter Benjamin / Koselleck]. Antragssumme grob [Range]. Stärken: [Vorarbeit X, Methodenprofil Y]. Risiko: [Vorarbeitenlücke, Methodenfremdheit, Stellenfrage]. Fehlende Unterlagen: [CV aktuell, GEPRIS-Auszug, Ethikvotum-Stand]. Nächster Schritt: [Skizze in drei Sätzen / Modulmix prüfen / Red-Team]. Bitte vor Einreichung mit der zuständigen DFG-Fachgebietsleitung telefonieren."

**Drei-Satz-Skizze** (Vorlage, vor jedem Antrag verlangen):

> "Forschungsfrage: [Eine Frage, falsifizierbar formuliert]. Methodischer Zugang: [Methode 1 plus Methode 2 zur Triangulation]. Erkenntnisgewinn nach 36 Monaten: [Welche These ist dann bestätigt oder widerlegt, und was wäre damit für das Feld gewonnen]."

## Typische Fehler

- "Mein Projekt ist interdisziplinär" als Selbstlob ohne methodische Konsequenz — Reviewer streichen das.
- Programmverwechslung: Walter Benjamin als "kleine Sachbeihilfe" benutzen.
- 100.000-Euro-Schwelle aus älterer DFG-Praxis weiterschreiben — aktuell ist 200.000 Euro die einschlägige Marke für die Möglichkeit der Ein-Gutachter-Begutachtung (siehe DFG-FAQ, vom Antragsteller live prüfen).
- "Vorarbeiten" durch Konferenzbeiträge belegen — Reviewer wollen referierte Volltexte.
- Antragsteller nennt sich "international vernetzt" ohne konkrete Kooperationsschreiben.

## Regelungs- und Quellenanker

Arbeitsfokus: **DFG-Förderantrag — Allgemein**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Quellen Stand 05/2026

Für Schwellen, Fristen, Vordrucke und Antragsberechtigung immer die Referenz `references/dfg-quellen-und-schwellen.md` und danach die verlinkte DFG-Quelle prüfen. Verbindlich nur:

- DFG-Programmseite Sachbeihilfe: dfg.de
- DFG-FAQ Begutachtung: dfg.de
- DFG-Hinweise Antragstellung: dfg.de
- elan-Portal: elan.dfg.de
- GEPRIS: gepris.dfg.de

Keine alten 100.000-Euro-Schwellen ungeprüft fortschreiben. Vor Empfehlung Verfahrensordnung des Antragsstichtags konsultieren.

---

## Skill: `dfg-erstpruefung-und-mandatsziel`

_DFG: Erstprüfung, Rollenklärung und Mandatsziel._

# DFG: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Dfg Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Dfg Foerderantrag** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Regelungs- und Quellenanker

Arbeitsfokus: **DFG: Erstprüfung, Rollenklärung und Mandatsziel**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DFG-Antragsfristen programmspezifisch (Sachbeihilfe rollierend, Schwerpunktprogramme stichtagsgebunden), Verwendungsnachweis 6 Monate nach Projektende, Zwischenbericht jährlich.
- Tragende Normen verifizieren: DFG-Verwendungsrichtlinien, BGB §§ 611 ff. (Drittmittelvertrag), HRG/Landeshochschulgesetze, WissZeitVG, EU-Beihilferecht (Forschung), BMBF/BMWK-Förderrichtlinien, DFG-Kodex Leitlinien zur Sicherung guter wissenschaftlicher Praxis — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Antragsteller (Principal Investigator), DFG-Fachkollegien, DFG-Geschäftsstelle, Hochschulverwaltung/Forschungsreferat, BMBF/BMWK, Gutachter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Antragsformular elan, Projektbeschreibung, Lebenslauf mit Publikationsliste, Finanzplan, Letter of Intent, Verwendungsnachweis, Zwischenbericht, Abschlussbericht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: DFG: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** DFG, KI.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **DFG** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## DFG-Programme im Schnelldurchlauf

| Programm | Zielgruppe | Volumen / Laufzeit |
|---|---|---|
| Sachbeihilfe (Einzelantrag) | etablierte Forschende, alle Stufen | typisch 3 Jahre, ein- oder mehrjährige Tranchen |
| Emmy Noether-Programm | Nachwuchs nach Promotion (2-4 J post-Promotion) | 6 Jahre, eigene Arbeitsgruppe |
| Heisenberg-Programm | habilitierte / habilitations-äquivalente | bis 5 Jahre, Stelle + Sachmittel |
| Reinhart Koselleck-Projekte | etablierte mit Hochrisiko-Forschung | bis 5 Jahre, bis ca. 1,25 Mio. EUR |
| Walter Benjamin-Programm | Postdoc-Mobilität | typisch bis 2 Jahre |
| Forschungsgruppen | Verbund, mehrere Teilprojekte | 2 x 4 Jahre |
| Schwerpunktprogramme (SPP) | thematisch bundesweit | 2 x 3 Jahre |
| Sonderforschungsbereiche (SFB) | universitärer Schwerpunkt | bis 12 Jahre (3 x 4 Jahre) |
| Graduiertenkollegs | strukturierte Promotion | bis 9 Jahre |

(Konkrete Förderhöhen und Laufzeitgrenzen vom Anwender live auf dfg.de/foerderung/programme verifizieren.)

## Erstprüfung: Förderfähigkeitscheck

1. **Persönliche Antragsberechtigung**: Promotion abgeschlossen, eigenständige Forschungstätigkeit, deutsche Forschungseinrichtung bzw. Kooperation? (Verfahrensordnung DFG, vor Ausgabe verifizieren)
2. **Programmpassung**: Welches Programm passt zur Karrierephase, zum Thema, zum Volumen?
3. **Antragsumfang**: Sachbeihilfe-Standardtext meist 20 Seiten + Anlagen (Lebenslauf, Publikationen mit DOI, Forschungsdatenmanagement-Plan, Ethikvotum).
4. **Mehrfachförderungs-Ausschluss**: Keine Förderung für Vorhaben, die anderweitig drittmittelfinanziert sind oder zu Grundausstattung gehören.
5. **Gute wissenschaftliche Praxis**: Kodex 2022 der DFG einhalten.

## Praktischer Tipp

- Vor der Einreichung: **interne Vorabstimmung mit der eigenen Forschungseinrichtung** (Drittmittelabteilung, ggf. Ethikkommission, Tierschutzbeauftragte). Die Einrichtung muss den Antrag mitzeichnen.
- Bei Erstantragstellern: Aktive Inanspruchnahme der Programm-Beratungsangebote der DFG-Geschäftsstelle (per E-Mail oder Telefon mit zuständigem Fachreferat). Senkt Ablehnungsrisiko signifikant.
- "Mandatsziel" für die Beratung präzisieren: Brauchen Sie inhaltliches Sparring (das macht die DFG nicht), formale Antragsoptimierung (das ja) oder Begleitung bei Wiedereinreichung nach Ablehnung?

## Typische Fehler

- Sachbeihilfe-Antrag wird wie Promotionsprojekt geschrieben - DFG erwartet abgeschlossene Promotion und eigenständige Forschungskonzeption.
- Mehrfacheinreichung in zwei DFG-Programmen ohne Hinweis - Ausschlusskriterium.
- Habilitationsstellen, die zur Grundausstattung gehören, werden als Personalmittel beantragt.

---

## Skill: `adaptive-dokumentenmatrix-lueckenliste`

_Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kr..._

# Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung

## Regelungs- und Quellenanker

Arbeitsfokus: **Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung
- **Normen-/Quellenanker:** DFG, KI.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Adaptive** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 48 VwVfG
- § 49 VwVfG
- § 27 BDSG
- § 7 TierSchG
- § 8 TierSchG
- § 69a UrhG
- § 28 VwVfG
- § 39 VwVfG
- § 4 AWG
- § 5 AWG
- § 18 AWG
- Art. 44 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `anfaenger-risikoampel-gegenargumente`

_Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe i..._

# Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien

## Regelungs- und Quellenanker

Arbeitsfokus: **Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien
- **Normen-/Quellenanker:** DFG, KI.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anfaenger** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 48 VwVfG
- § 49 VwVfG
- § 27 BDSG
- § 7 TierSchG
- § 8 TierSchG
- § 69a UrhG
- § 28 VwVfG
- § 39 VwVfG
- § 4 AWG
- § 5 AWG
- § 18 AWG
- Art. 44 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `antraege-zahlen-schwellenwerte-berechnung`

_Antraege: Zahlen, Schwellenwerte und Berechnung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch? 4...._

# Antraege: Zahlen, Schwellenwerte und Berechnung

## Regelungs- und Quellenanker

Arbeitsfokus: **Antraege: Zahlen, Schwellenwerte und Berechnung**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit, Sparsamkeit und plausibler Mitteleinsatz.
- `§ 23 BHO` — Zuwendungszweck und erhebliches Bundesinteresse als Förderlogik.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung von Zuwendungen.
- `§ 55 Abs. 1 BHO` — Vergabebezug bei Beschaffung aus Fördermitteln.
- `§ 58 BHO` — Änderung von Verträgen und haushaltsrechtliche Bindungen.
- `Art. 91b Abs. 1 GG` — Bund-Länder-Kooperation in der Forschungsförderung.
- `DFG-Vordruck Sachbeihilfe Finanzierungsplan` — Personal, Geräte, Verbrauchsmittel und Reisen getrennt begründen.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung auch bei Mittelverwendung und Dokumentation.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Antraege: Zahlen, Schwellenwerte und Berechnung
- **Normen-/Quellenanker:** DFG, KI.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Antraege** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## DFG-typische Schwellen / Größenordnungen (vor Ausgabe live verifizieren)

| Schwelle | Bedeutung |
|---|---|
| Geräte > 10.000 EUR netto | Einzelbegründung erforderlich |
| Geräte > 50.000 EUR netto | regelmäßig drei Vergleichsangebote erforderlich |
| Geräte > Großgerätegrenze (vor Ausgabe verifizieren) | Großgeräteantrag, ggf. Begutachtung separat |
| Sachbeihilfe-Personenanträge | regelmäßig 3 Jahre Laufzeit, ein- oder mehrjährige Tranchen |
| Koselleck-Volumen | bis ca. 1,25 Mio. EUR über 5 Jahre |
| SFB-Volumen | dreistellige Mio.-Beträge möglich über 12 Jahre |
| Programmpauschale Universitäten | 22 % auf direkte Mittel (vor Ausgabe verifizieren) |
| Open Access-Pauschale Publikationen | jährliche Pauschale je nach Programm |

## Personalmittelpauschalen (DFG-Tabelle, vor Ausgabe live auf dfg.de verifizieren)

| Stelle | Pauschalsatz |
|---|---|
| Postdoc 100 % E13 TV-L Standard | DFG-Pauschale je nach Erfahrungsstufe |
| Promovierende 65 %-Stelle | DFG-Pauschale, häufig 65 % E13 |
| Promovierende 75 %-Stelle | DFG-Pauschale, häufig 75 % E13 |
| Studentische Hilfskraft (SHK) | Stunden- oder Monatspauschale |
| Wissenschaftliche Hilfskraft mit Abschluss (WHK) | Stunden- oder Monatspauschale (höher als SHK) |

## Praktischer Tipp

- DFG akzeptiert ihre eigenen Pauschalen ohne Einzelnachweis. Eigene Berechnungen ("TV-L E13 Stufe 3 inklusive Arbeitgeberanteil zur Sozialversicherung") führen zu Rückfragen.
- Bei Mehrjahresplänen (3 Jahre): durchschnittlich + Inflation einplanen, DFG akzeptiert regelmäßig moderate Steigerungssätze.
- Reisemittel: DFG-Reisekostenrichtlinien folgen dem Bundesreisekostengesetz (BRKG); Tagespauschalen sind dort verankert (vor Ausgabe verifizieren). Konferenzkosten separat: Anmeldegebühr + Reise + Unterkunft + Tagungspauschale.

## Beispiel-Rechnung (typischer Sachbeihilfe-Antrag, 3 Jahre)

> Personalmittel: 1 Postdoc 100 % (3 Jahre): EUR [Pauschale × 36 Monate]
> Personalmittel: 1 Promo 65 % (3 Jahre): EUR [Pauschale × 36 Monate]
> SHK (40 Std./Monat, 3 Jahre): EUR [...]
> Sachmittel (Verbrauchsmaterial): EUR 12.000 (4.000 EUR p.a.)
> Reisemittel: EUR 9.000 (3.000 EUR p.a.)
> Publikationsmittel: EUR 4.500 (1.500 EUR p.a.)
> Direkt zusammen: EUR [...]
> + Programmpauschale 22 % (Universität): EUR [...]
> = Gesamtsumme: EUR [...]

## Typische Fehler

- Programmpauschale auf Programmpauschale aufgeschlagen ("Multiplikation").
- Geräte > 10.000 EUR ohne Einzelbegründung pauschal als "Sachmittel" verbucht.
- Promovierende mit 100 %-Stelle beantragt, obwohl in Geisteswissenschaften regelmäßig 65 % oder 75 % üblich sind - vermeintliche Großzügigkeit wirkt antragsschwächend.

---

## Skill: `dfg-eigenanteil-und-grundausstattung`

_Eigenanteil und Grundausstattung der Hochschule sauber von DFG-Förderung abgrenzen: Was muss die Hochschule stellen (Buero, Standardrechner, Sekretariat, Bibliothek), was darf die DFG finanzieren (projektspezifische Geraete, Personal ueber Stelleninhaber hinaus, Verbrauch). Hochschulleitung-Besta..._

# Eigenanteil und Grundausstattung

## Regelungs- und Quellenanker

Arbeitsfokus: **Eigenanteil und Grundausstattung**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit, Sparsamkeit und plausibler Mitteleinsatz.
- `§ 23 BHO` — Zuwendungszweck und erhebliches Bundesinteresse als Förderlogik.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung von Zuwendungen.
- `§ 55 Abs. 1 BHO` — Vergabebezug bei Beschaffung aus Fördermitteln.
- `§ 58 BHO` — Änderung von Verträgen und haushaltsrechtliche Bindungen.
- `Art. 91b Abs. 1 GG` — Bund-Länder-Kooperation in der Forschungsförderung.
- `DFG-Vordruck Sachbeihilfe Finanzierungsplan` — Personal, Geräte, Verbrauchsmittel und Reisen getrennt begründen.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung auch bei Mittelverwendung und Dokumentation.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Eigenanteil und Grundausstattung
- **Normen-/Quellenanker:** DFG.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `dfg-erstantragsteller-besondere-checks`

_Erstantragsteller-Spezialcheck: Promotion abgeschlossen, gute eigene Vorarbeit (Publikationen Erst- und Letztautor), Anbindung an erfahrene Person ohne Co-Antragstellung wenn moeglich, Lebenslauf mit Eltern- und Pflegezeiten transparent, Track-Record auch ohne Drittmittelhistorie. Pruefraster und..._

# Erstantragsteller-Sondercheck

## Regelungs- und Quellenanker

Arbeitsfokus: **Erstantragsteller-Sondercheck**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Erstantragsteller-Sondercheck
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `dfg-grundsystem-foerderlinien`

_Grundsystem der DFG-Foerderlinien einfuehrend erklaeren: Sachbeihilfe (Einzelantrag), Emmy Noether, Heisenberg, Reinhart Koselleck, SFB, GRK, Forschergruppen, Schwerpunktprogramme. Pro Linie: Zielgruppe, Hoehe, Dauer, Antragsweg, Begutachtungsstil. Fuer Erstantragsteller mit Entscheidungshilfe zu..._

# Grundsystem DFG-Foerderlinien

## Regelungs- und Quellenanker

Arbeitsfokus: **Grundsystem DFG-Foerderlinien**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Grundsystem DFG-Foerderlinien
- **Normen-/Quellenanker:** DFG, SFB, GRK.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `dfg-tieforschung-ethik-pflichten`

_Tierversuchsethik-Pflichten in DFG-Antraegen: 3R-Prinzip (Replace, Reduce, Refine), TierSchG, TierSchVersV, Tierversuchsantrag bei der Behörde parallel zur DFG. DFG-Senatskommission für tierexperimentelle Forschung. Ethik-Sektion im Antrag, Belastungsstufen, alternative Methoden. Routet in dfg-ki..._

# Tierforschungs-Ethikpflichten

## Regelungs- und Quellenanker

Arbeitsfokus: **Tierforschungs-Ethikpflichten**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit als Ausgangspunkt.
- `Art. 89 Abs. 1 DSGVO` — Garantien für wissenschaftliche Forschungszwecke.
- `Art. 9 Abs. 2 lit. j DSGVO` — besondere Kategorien personenbezogener Daten in Forschungskontexten.
- `§ 27 Abs. 1 BDSG` — Datenverarbeitung zu wissenschaftlichen Forschungszwecken.
- `§ 7 Abs. 1 TierSchG` — Tierversuche nur bei gesetzlich anerkanntem Zweck und Erforderlichkeit.
- `§ 8 Abs. 1 TierSchG` — Genehmigungspflichtiger Tierversuch.
- `§ 69a UrhG` — Computerprogramme als Schutzgegenstand bei Forschungssoftware.
- `DFG-Kodex Leitlinie 10` — rechtliche und ethische Rahmenbedingungen.
- `DFG-Kodex Leitlinie 13` — Herstellung von öffentlichem Zugang zu Forschungsergebnissen.
- `DFG-Kodex Leitlinie 14` — Autorschaft und Verantwortung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Tierforschungs-Ethikpflichten
- **Normen-/Quellenanker:** DFG, TierSchG, TierSchVersV, KI.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

