---
name: migr-asylverfahren-aufenthaltsstatus-frist
description: "Migr Asylverfahren Aufenthaltsstatus Frist: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Migr Asylverfahren Aufenthaltsstatus Frist

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Migr Asylverfahren Aufenthaltsstatus Frist** im Plugin Fachanwalt Migrationsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `migr-asylverfahren-anhoerung-leitfaden` | Leitfaden Asylverfahren und Anhoerung BAMF: Vorbereitung Mandantengespraech, dolmetscherische Pflichten, Niederschriftpruefung. Pruefraster Glaubhaftigkeit und Fluchtgrund. |
| `spezial-aufenthaltsstatus-frist-und-rechtsmittel` | Aufenthaltsstatus, Frist und Rechtsmittel als Erstweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-aufenthaltstitel-fristennotiz-und-naechster-schritt` | Aufenthaltstitel: Fristennotiz und nächster Schritt im Plugin fachanwalt migrationsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-aufenthg-fristen-form-und-zustaendigkeit` | Aufenthg: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt migrationsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Fachanwalt Migrationsrecht gilt für **Migr Asylverfahren Aufenthaltsstatus Frist**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `migr-asylverfahren-anhoerung-leitfaden`

**Fokus:** Leitfaden Asylverfahren und Anhoerung BAMF: Vorbereitung Mandantengespraech, dolmetscherische Pflichten, Niederschriftpruefung. Pruefraster Glaubhaftigkeit und Fluchtgrund.


# Migr: Asyl Anhoerung

## Aufgabe
Leitfaden Asylverfahren und Anhoerung BAMF: Vorbereitung Mandantengespraech, dolmetscherische Pflichten, Niederschriftpruefung.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster Asylverfahren und Anhoerung

### 1. Asylverfahren beim BAMF (§§ 14 ff. AsylG)

- **Antragstellung** § 13 AsylG; Asylgesuch loest § 55 AsylG Aufenthaltsgestattung aus.
- **Aussenstelle / Anhoerung** § 24 AsylG: persoenliche Anhoerung ist Pflicht (Ausnahmen § 25 IV-VI AsylG).
- **Dublin-Verfahren** VO (EU) 604/2013 (Dublin III) — Zustaendigkeitsbestimmung; Selbsteintrittsrecht Art. 17.
- **Pruefungsreihenfolge** § 13 II AsylG: zuerst Asylberechtigung Art. 16a GG, dann Fluechtlingseigenschaft (§ 3 AsylG), dann subsidiaerer Schutz (§ 4 AsylG), dann nationale Abschiebungsverbote (§ 60 V, VII AufenthG).

### 2. Rechtsgrundlagen Schutzformen

| Schutzform | Rechtsgrundlage | Voraussetzungen |
|---|---|---|
| Asylberechtigung Art. 16a GG | Politische Verfolgung; subjektives Recht; staatlich (nicht von nicht-staatlichen Akteuren); enger als § 3 AsylG |
| Fluechtlingseigenschaft | § 3 AsylG; GFK 1951 | Verfolgung wegen Rasse, Religion, Nationalitaet, politischer Ueberzeugung, Zugehoerigkeit zu sozialer Gruppe; auch nicht-staatliche Akteure (§ 3c AsylG) |
| Subsidiaerer Schutz | § 4 AsylG; Art. 15 Anerkennungs-RL 2011/95/EU | Drohende ernsthafte Schaeden: Todesstrafe, Folter, willkuerliche Gewalt in bewaffnetem Konflikt |
| Abschiebungsverbot § 60 V AufenthG | Verstoss gegen EMRK (insbes. Art. 3 EMRK) |
| Abschiebungsverbot § 60 VII AufenthG | Konkrete erhebliche Gefahr fuer Leib, Leben, Freiheit |

### 3. Glaubhaftigkeitspruefung

- **Substanziiertheit, Detailreichtum, Konstanz, Plausibilitaet** der Angaben.
- **Allgemeine Lage** im Herkunftsland (Auswaertiges Amt-Berichte, EASO/EUAA, UNHCR).
- **Individuelle Verfolgungsfurcht** (objektive plus subjektive Komponente; BVerwG 1 C 16.78).
- **Nachfluchtgruende** § 28 AsylG.
- **Inlandsfluchtalternative** § 3e AsylG (Schutz in Teilen des Herkunftslandes zumutbar?).

### 4. Anhoerungs-Praxis BAMF

- **Vorbereitung** mit Mandanten: Chronologie, Fluchtweg, persoenliche Daten der Familienangehoerigen, dokumentierte Verfolgungshandlungen, religioese/politische Aktivitaeten.
- **Dolmetscher** § 17 AsylG; Recht auf Dolmetscher in einer Sprache, die Antragsteller versteht; Pruefung der Qualifikation.
- **Pflichten des Antragstellers** § 15 AsylG: persoenliche Erscheinen, wahrheitsgemaesse Angaben, Mitwirkung an Identitaetsklaerung.
- **Vertrauensanwalt** bei Anhoerung kein Recht auf Beistand (str.; nach BVerwG-Linie zugelassen, aber keine eigenstaendige Rolle).
- **Niederschrift** § 25 VII AsylG: Rueckuebersetzung; Pruefung auf Vollstaendigkeit und Korrektheit; Ergaenzungsantrag noch waehrend Anhoerung moeglich.

### 5. Bescheid und Rechtsschutz

- **Ablehnungsbescheid** § 31 AsylG.
- **Klage zum VG** § 74 AsylG: zwei Wochen ab Zustellung (bei einfacher Ablehnung); eine Woche bei offensichtlich unbegruendet (§ 36 AsylG) und Dublin-Faellen (§ 34a AsylG).
- **Eilantrag** § 80 V VwGO; aufschiebende Wirkung der Klage besteht bei Asylklage nicht automatisch — § 75 I AsylG.

## Praxisfallen

- **Sieben-Tages-Frist** bei "offensichtlich unbegruendet" wird oft uebersehen.
- **Dublin-Frist** sechs Monate Art. 29 Dublin III; Verlaengerung bei Untertauchen.
- **Aenderungen Anhoerung** muessen sofort moniert werden; sonst Bestandskraft der Niederschrift.
- **Asylfolgeantrag** § 71 AsylG nur bei neuer Sach- oder Rechtslage; Frist drei Monate.
- **Familienasyl** § 26 AsylG (Ehegatte, minderjaehrige ledige Kinder).
- **Sichere Herkunftsstaaten** § 29a AsylG i.V.m. Anlage II AsylG (z. B. Albanien, Bosnien, Ghana, Kosovo, Mazedonien, Senegal, Serbien, Moldau, Georgien).

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

## 2. `spezial-aufenthaltsstatus-frist-und-rechtsmittel`

**Fokus:** Aufenthaltsstatus, Frist und Rechtsmittel als Erstweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.


# Aufenthaltsstatus, Frist und Rechtsmittel als Erstweiche

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `fachanwalt-migrationsrecht`. Kontext des Plugins: Plugin Fachanwalt für Migrationsrecht. AufenthG AsylG GFK Dublin-VO Verfahrens-RL Qualifikations-RL StAG. Einbürgerung Familiennachzug Notfrist § 36 AsylG eine Woche. Schnittstellen Plugin rechtsberatungsstelle.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Aufenthaltsstatus, Frist und Rechtsmittel als Erstweiche** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-aufenthaltstitel-fristennotiz-und-naechster-schritt`

**Fokus:** Aufenthaltstitel: Fristennotiz und nächster Schritt im Plugin fachanwalt migrationsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.


# Aufenthaltstitel: Fristennotiz und nächster Schritt

## Spezialwissen: Aufenthaltstitel: Fristennotiz und nächster Schritt
- **Spezialgegenstand:** Aufenthaltstitel: Fristennotiz und nächster Schritt / aufenthaltstitel fristennotiz und naechster schritt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AufenthG, AsylG, GFK, VO, RL, StAG, EU.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aufenthaltstitel** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Qualitätsanker: Identität, Schutzstatus und aktuelle Lageprüfung

- **Verifizierte Rechtsprechungsanker:** BVerwG, Urteil vom 13.12.2023 - 1 C 34.22 und BVerwG, Urteil vom 18.12.2025 - 1 C 27.24 zur Identitätsklärung/Stufenmodell im Einbürgerungsrecht; BVerwG, Urteil vom 16.04.2025 - 1 C 18.24 zur Tatsachenrevision und Art. 4 GRCh/Art. 3 EMRK bei anerkannten Schutzberechtigten in Griechenland.
- **Prüfdisziplin:** Aufenthaltsrecht, Asylrecht, Staatsangehörigkeitsrecht, Freizügigkeit/EU, Dublin/GEAS, Abschiebungsschutz, Familiennachzug und Arbeit/Beschäftigung strikt trennen. Keine Auskunft „nach Gefühl“ über Länderpraxis oder Behördenlaufzeiten.
- **Aktualitätsfilter:** Herkunftsland, Schutzstatus, Dokumentenlage, Identität, Passbeschaffung, Zumutbarkeit, Vulnerabilität und aktuelle Lageberichte/live verfügbare Gerichtsquellen sind tragend; bei Lagefragen immer Datum und Erkenntnisbasis nennen.
- **Output-Pflicht:** Entscheidungsbaum mit Sofortfrist, zuständiger Behörde/Gericht, benötigten Unterlagen, Beweisnot-/Zumutbarkeitsargumenten und nächstem rechtssicheren Schritt.

## 4. `spezial-aufenthg-fristen-form-und-zustaendigkeit`

**Fokus:** Aufenthg: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt migrationsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.


# Aufenthg: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Aufenthg: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Aufenthg: Fristen, Form, Zuständigkeit und Rechtsweg / aufenthg fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AufenthG, AsylG, GFK, VO, RL, StAG, EU.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aufenthg** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Qualitätsanker: Identität, Schutzstatus und aktuelle Lageprüfung

- **Verifizierte Rechtsprechungsanker:** BVerwG, Urteil vom 13.12.2023 - 1 C 34.22 und BVerwG, Urteil vom 18.12.2025 - 1 C 27.24 zur Identitätsklärung/Stufenmodell im Einbürgerungsrecht; BVerwG, Urteil vom 16.04.2025 - 1 C 18.24 zur Tatsachenrevision und Art. 4 GRCh/Art. 3 EMRK bei anerkannten Schutzberechtigten in Griechenland.
- **Prüfdisziplin:** Aufenthaltsrecht, Asylrecht, Staatsangehörigkeitsrecht, Freizügigkeit/EU, Dublin/GEAS, Abschiebungsschutz, Familiennachzug und Arbeit/Beschäftigung strikt trennen. Keine Auskunft „nach Gefühl“ über Länderpraxis oder Behördenlaufzeiten.
- **Aktualitätsfilter:** Herkunftsland, Schutzstatus, Dokumentenlage, Identität, Passbeschaffung, Zumutbarkeit, Vulnerabilität und aktuelle Lageberichte/live verfügbare Gerichtsquellen sind tragend; bei Lagefragen immer Datum und Erkenntnisbasis nennen.
- **Output-Pflicht:** Entscheidungsbaum mit Sofortfrist, zuständiger Behörde/Gericht, benötigten Unterlagen, Beweisnot-/Zumutbarkeitsargumenten und nächstem rechtssicheren Schritt.
