---
name: verg-nachpruefungsverfahren-vergabeverfahren
description: "Verg Nachpruefungsverfahren Vergabeverfahren: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verg Nachpruefungsverfahren Vergabeverfahren

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Verg Nachpruefungsverfahren Vergabeverfahren** im Plugin Fachanwalt Vergaberecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verg-nachpruefungsverfahren-spezial` | Spezialfall Nachpruefungsverfahren §§ 155 ff. GWB: Antrag, Ruege, Eilantrag, sofortige Beschwerde. Pruefraster fuer Bieter und Vergabekammer. |
| `verg-vergabeverfahren-bauleiter` | Bauleiter Vergabeverfahren GWB / VgV: offen, beschraenkt, Verhandlungsverfahren, wettbewerblicher Dialog, Innovationspartnerschaft. Pruefraster fuer Vergabestelle. |
| `vorinformation-134-gwb-stillhaltefrist` | Vorabinformation nach Paragraph 134 GWB und Stillhaltefrist pruefen: Inhalt, Versandweg, Fristlauf, Zuschlagsverbot, Fehlerfolgen und taktische Sofortmassnahmen. |
| `vertragsaenderung-132-gwb-change-control` | Vertragsaenderungen nach Paragraph 132 GWB und Change-Control pruefen: wesentliche Aenderung, Schwellen, Optionen, Zusatzleistungen, Laufzeit, Preisrevision und Dokumentation. |

## Arbeitsweg

Im Plugin Fachanwalt Vergaberecht gilt für **Verg Nachpruefungsverfahren Vergabeverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verg-nachpruefungsverfahren-spezial`

**Fokus:** Spezialfall Nachpruefungsverfahren §§ 155 ff. GWB: Antrag, Ruege, Eilantrag, sofortige Beschwerde. Pruefraster fuer Bieter und Vergabekammer.

# Verg: Nachpruefungsverfahren

## Spezialwissen: Verg: Nachpruefungsverfahren
- **Spezialgegenstand:** Verg: Nachpruefungsverfahren / verg nachpruefungsverfahren spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** GWB, BGH, BVerfG.
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


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 2. `verg-vergabeverfahren-bauleiter`

**Fokus:** Bauleiter Vergabeverfahren GWB / VgV: offen, beschraenkt, Verhandlungsverfahren, wettbewerblicher Dialog, Innovationspartnerschaft. Pruefraster fuer Vergabestelle.

# Verg: Vergabeverfahren

## Aufgabe
Bauleiter Vergabeverfahren GWB / VgV: offen, beschraenkt, Verhandlungsverfahren, wettbewerblicher Dialog, Innovationspartnerschaft.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster Vergabeverfahren

### 1. Anwendungsbereich GWB-Vergaberecht

- **Oeffentlicher Auftraggeber** § 99 GWB (klassisch, Sektorenauftraggeber § 100, Konzessionsgeber § 101) und **oeffentlicher Auftrag** § 103 GWB.
- **EU-Schwellenwert ueberschritten** (§ 106 GWB iVm aktuellen VO-Schwellenwerten; ab 2024/2025: Bauauftraege 5.538.000 Euro, Liefer-/Dienstleistungen 221.000 Euro klassisch bzw. 443.000 Euro Sektoren; Konzessionen 5.538.000 Euro). Bei Unterschreitung: UVgO/Haushaltsvergaberecht der Laender.
- **Bereichsausnahmen** §§ 107-109 GWB (z. B. Inhouse, Interkommunal, geheim, Verteidigung).

### 2. Verfahrensart waehlen

| Verfahrensart | Norm | Voraussetzungen |
|---|---|---|
| Offenes Verfahren | § 119 II GWB, § 15 VgV | Regelverfahren oberhalb Schwellenwert; jeder kann Angebot abgeben. |
| Nicht offenes Verfahren mit Teilnahmewettbewerb | § 119 III GWB, § 16 VgV | Regelverfahren neben offenem; Auswahl nach Teilnahmewettbewerb. |
| Verhandlungsverfahren mit Teilnahmewettbewerb | § 119 IV, V GWB, § 17 VgV | Nur bei Vorliegen Voraussetzung § 14 III VgV (komplexe Leistung, Verhandlung erforderlich, etc.). |
| Verhandlungsverfahren ohne Teilnahmewettbewerb | § 14 IV VgV | Sehr enge Ausnahme (nur ein Anbieter, Dringlichkeit, Folgeauftraege etc.). |
| Wettbewerblicher Dialog | § 18 VgV | Komplexer Auftrag, dessen technische, finanzielle oder rechtliche Loesungsansaetze nicht von vornherein definiert werden koennen. |
| Innovationspartnerschaft | § 19 VgV | Entwicklung innovativer Leistung, die am Markt noch nicht verfuegbar ist. |

### 3. Verfahrensablauf

- **EU-Bekanntmachung** (TED-Datenbank, eForms ab 25.10.2023 Pflicht).
- **Vergabeunterlagen** mit Eignungs- und Zuschlagskriterien (§§ 121, 122, 127 GWB), Leistungsbeschreibung (§§ 28-29 VgV).
- **Eignungspruefung** vor Zuschlag (§ 122 GWB; siehe `verg-eignungspruefung-leitfaden`).
- **Ausschluss** (§§ 123, 124 GWB) und Selbstreinigung (§ 125 GWB).
- **Wertung** nach Zuschlagskriterien (§ 127 GWB: wirtschaftlichstes Angebot).
- **Vorabinformation** § 134 GWB: Mindestens 10 Tage (Brief) bzw. 15 Tage (Telefax/elektronisch) vor Zuschlag an unterlegene Bieter; Zuschlagsverbot.

### 4. Rechtsschutz

- **Rugeobliegenheit** § 160 III GWB (siehe `fachanwalt-vergaberecht-...` Skills).
- **Nachpruefungsverfahren** vor Vergabekammer (§§ 155 ff. GWB), sofortige Beschwerde zum OLG (§§ 171 ff. GWB).

## Praxisfallen

- **Falsche Verfahrenswahl** = ruegefaehiger Vergabeverstoss; Verhandlungsverfahren ohne TNW ist die haeufigste Falle.
- **Fristen** § 15 III, § 16 V, § 17 III VgV; bei beschleunigtem Verfahren reduzierbar.
- **De-facto-Vergabe** § 135 I Nr. 2 GWB: ohne Bekanntmachung erteilter Auftrag ist von Anfang an unwirksam.
- **Bedarfsschaetzung** § 3 VgV: alle gleichartigen Leistungen eines Haushaltsjahres addieren; Aufteilungsverbot (§ 3 II VgV).

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


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 3. `vorinformation-134-gwb-stillhaltefrist`

**Fokus:** Vorabinformation nach Paragraph 134 GWB und Stillhaltefrist pruefen: Inhalt, Versandweg, Fristlauf, Zuschlagsverbot, Fehlerfolgen und taktische Sofortmassnahmen.

# Paragraph 134 GWB Vorinformation und Stillhaltefrist

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll den letzten Zeitraum vor Zuschlag sichern und Fehler verwerten. Er arbeitet fuer Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

## Sofortmodus

1. Rolle klaeren: Auftraggeber, Bieter, Beigeladener, Foerdermittelempfaenger, Projektsteuerer oder Kanzlei.
2. Verfahrensstand klaeren: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, Paragraph 134 GWB, Zuschlag, Vertrag, Nachpruefung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg pruefen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Foerdermittel oder Sonderregime.
4. Fristen sichern: Ruge, Angebotsfrist, Stillhaltefrist, 15-Tage-Frist nach Nichtabhilfe, Beschwerdefrist, Paragraph 135 GWB-Fristen.
5. Erst danach in die materielle Pruefung gehen.

## Arbeitsweise

- Baue zuerst eine kleine Tabelle mit `Tatsache`, `Beleg`, `rechtliche Bedeutung`, `Risiko`, `naechster Schritt`.
- Trenne strikt zwischen gesicherten Tatsachen, plausiblen Annahmen und offenen Pruefpunkten.
- Wenn der Nutzer Anfaenger ist, erklaere jedes vergaberechtliche Kunstwort in einem Satz und liefere danach sofort die Handlung.
- Wenn der Nutzer erfahren ist, liefere direkt Matrix, Schriftsatzkern, Vermerk oder Entscheidungsvorlage.
- Bei schwellenwert-, formular-, TED/eForms-, Wettbewerbsregister-, Landes- oder EU-Fragen einen Live-/Aktualitaetscheck verlangen, bevor Zahlen oder Formularlogik tragend verwendet werden.

## Pflicht-Output

- Kurzbild in drei Saetzen.
- Ampel: Frist, Zustaendigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Fristenblatt, Fehlercheck, Sofortplan, Mandantenmail.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` fuer Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` fuer Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` fuer Aktenarbeit.
- `nachpruefungsantrag-powerdraft` fuer VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` fuer komplexe Mehrthemenfaelle.


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 4. `vertragsaenderung-132-gwb-change-control`

**Fokus:** Vertragsaenderungen nach Paragraph 132 GWB und Change-Control pruefen: wesentliche Aenderung, Schwellen, Optionen, Zusatzleistungen, Laufzeit, Preisrevision und Dokumentation.

# Paragraph 132 GWB Vertragsaenderung

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll Bestandsvertrag aendern, ohne Neuausschreibungspflicht zu uebersehen. Er arbeitet fuer Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

## Sofortmodus

1. Rolle klaeren: Auftraggeber, Bieter, Beigeladener, Foerdermittelempfaenger, Projektsteuerer oder Kanzlei.
2. Verfahrensstand klaeren: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, Paragraph 134 GWB, Zuschlag, Vertrag, Nachpruefung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg pruefen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Foerdermittel oder Sonderregime.
4. Fristen sichern: Ruge, Angebotsfrist, Stillhaltefrist, 15-Tage-Frist nach Nichtabhilfe, Beschwerdefrist, Paragraph 135 GWB-Fristen.
5. Erst danach in die materielle Pruefung gehen.

## Arbeitsweise

- Baue zuerst eine kleine Tabelle mit `Tatsache`, `Beleg`, `rechtliche Bedeutung`, `Risiko`, `naechster Schritt`.
- Trenne strikt zwischen gesicherten Tatsachen, plausiblen Annahmen und offenen Pruefpunkten.
- Wenn der Nutzer Anfaenger ist, erklaere jedes vergaberechtliche Kunstwort in einem Satz und liefere danach sofort die Handlung.
- Wenn der Nutzer erfahren ist, liefere direkt Matrix, Schriftsatzkern, Vermerk oder Entscheidungsvorlage.
- Bei schwellenwert-, formular-, TED/eForms-, Wettbewerbsregister-, Landes- oder EU-Fragen einen Live-/Aktualitaetscheck verlangen, bevor Zahlen oder Formularlogik tragend verwendet werden.

## Pflicht-Output

- Kurzbild in drei Saetzen.
- Ampel: Frist, Zustaendigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Aenderungsmatrix, Neuausschreibungsrisiko, Vermerk, Freigabeempfehlung.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` fuer Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` fuer Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` fuer Aktenarbeit.
- `nachpruefungsantrag-powerdraft` fuer VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` fuer komplexe Mehrthemenfaelle.


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.
