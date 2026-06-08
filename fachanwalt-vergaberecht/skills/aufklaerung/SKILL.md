---
name: aufklaerung
description: "Aufklaerung im Plugin Fachanwalt Vergaberecht: prüft konkret Schadensersatz nach § 181 GWB und BGB-Vorvertragsrecht bei, Aufklaerung, Nachforderung und Angebotsaufklaerung steuern, Vergaberechtliche Ruege nach § 160 Abs. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Aufklaerung

## Arbeitsbereich

**Aufklaerung** ordnet den Fall über die tragenden Prüfungslinien: Schadensersatz nach § 181 GWB und BGB-Vorvertragsrecht bei, Aufklaerung, Nachforderung und Angebotsaufklaerung steuern. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-vergaberecht-schadensersatz-181-gwb` | Schadensersatz nach § 181 GWB und BGB-Vorvertragsrecht bei vergaberechtswidriger Zuschlagsentscheidung geltend machen: Bieter hat Zuschlag verloren und will Vertrauensschaden oder positives Interesse einklagen. Normen: § 181 GWB (Schadensersatz), §§ 280 und 311 BGB (vorvertragliches Schuldverhaeltnis), § 124 GWB (Ausschluss). Pruefraster: Anspruchsgrundlage, Kausalitaet, Echte-Chance-Doktrin BGH X ZR 100/04, Vertrauensschaden vs. positives Interesse, Mitverschulden, Verjährung. Output Klageschrift-Geruest LG, Schadensberechnung. Abgrenzung: VK-Verfahren siehe fachanwalt-vergaberecht-nachpruefungsverfahren-vk; De-facto-Vergabe siehe fachanwalt-vergaberecht-de-facto-vergabe-klage. |
| `aufklaerung-nachforderung-56-vgv` | Aufklaerung, Nachforderung und Angebotsaufklaerung steuern: fehlende Unterlagen, unklare Preise, ungewoehnlich niedrige Angebote, Gleichbehandlung und Grenzen der Nachbesserung. |
| `fachanwalt-vergaberecht-ruege-vor-zuschlag` | Vergaberechtliche Ruege nach § 160 Abs. 3 GWB vor Zuschlag erheben: Bieter hat Vergabeverstoesse erkannt und muss rügen bevor Zuschlag erteilt wird. Normen: § 160 Abs. 3 GWB (Ruegerobliegenheit als Praeklusionsvoraussetzung). Prüfraster: Fristen (Bekanntmachungs-Verstoesse bis Angebotsabgabe, sonstige Verstoesse 10 Tage), Inhaltliche Anforderungen, Reaktionspflicht Auftraggeber (Abhilfe/Zurückweisung). Output Ruege-Schreiben mit konkretem Verstoß, Norm und Sachverhalt. Abgrenzung: Nachprüfungsantrag nach Ruege siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk; Ruegeschriftsatz-Detail siehe ruegeschriftsatz-erstellen. |
| `markterkundung-und-vorbefassung` | Markterkundung, Vorbefassung und Interessenkonflikte rechtssicher steuern: zulaessige Informationsgewinnung, Ausgleichsmassnahmen, Dokumentation und Rugeabwehr. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-vergaberecht-schadensersatz-181-gwb`

**Fokus:** Schadensersatz nach § 181 GWB und BGB-Vorvertragsrecht bei vergaberechtswidriger Zuschlagsentscheidung geltend machen: Bieter hat Zuschlag verloren und will Vertrauensschaden oder positives Interesse einklagen. Normen: § 181 GWB (Schadensersatz), §§ 280 und 311 BGB (vorvertragliches Schuldverhaeltnis), § 124 GWB (Ausschluss). Pruefraster: Anspruchsgrundlage, Kausalitaet, Echte-Chance-Doktrin BGH X ZR 100/04, Vertrauensschaden vs. positives Interesse, Mitverschulden, Verjährung. Output Klageschrift-Geruest LG, Schadensberechnung. Abgrenzung: VK-Verfahren siehe fachanwalt-vergaberecht-nachpruefungsverfahren-vk; De-facto-Vergabe siehe fachanwalt-vergaberecht-de-facto-vergabe-klage.

### Schadensersatz nach § 181 GWB

## Aufgabe
Schadensersatz nach abgeschlossenem Vergabeverfahren geltend machen oder abwehren. Anspruchsgrundlage je nach Konstellation § 181 GWB, §§ 280, 311 BGB i. V. m. § 241 Abs. 2 BGB, ggf. § 826 BGB bei Vorsatz.

## Einstieg
1. Vergabeverfahren bereits abgeschlossen (Zuschlag erteilt oder Verfahren aufgehoben)?
2. Schadensbegehren: Vertrauensschaden (negatives Interesse) oder positives Interesse?
3. Gab es VK- oder OLG-Verfahren mit Rechtsverletzungs-Feststellung?
4. Welche Pflichtverletzung des Auftraggebers ist belegbar?
5. Hatte der Bieter eine echte Zuschlagschance?
6. Verjährung im Blick (§ 195 BGB drei Jahre, Kenntnis erforderlich)?

## Anspruchsgrundlagen
### § 181 GWB
- Spezialgesetzlicher Anspruch für Oberschwellenverfahren.
- Voraussetzung: Verstoss gegen vergaberechtliche Vorschrift und kausaler Schaden.
- Umfasst regelmaessig Vertrauensschaden (Angebotskosten).
- Positives Interesse nur, wenn Bieter den Zuschlag bei rechtmäßigem Verhalten erhalten haette (echte Chance).

### §§ 280, 311 BGB
- Vorvertragliches Schuldverhaeltnis durch Teilnahme am Vergabeverfahren.
- Pflichtverletzung: Verstoss gegen Vergaberecht.
- Vor Inkrafttreten GWB-Vergabeteil oder neben § 181 GWB anwendbar (insb. Unterschwelle).

### § 826 BGB
- Bei kollusivem Zusammenwirken Auftraggeber/Bieter, Vergabesperre umgehen, schwere Korruption.

## Schadensumfang
| Position | Vertrauensschaden | Positives Interesse |
|---|---|---|
| Angebotskosten | ja | ja (im Zuge entgangenen Gewinns konsumiert) |
| Reisekosten Verhandlung | ja | ja |
| Anwaltskosten Ruege/VK | ja, soweit nicht Kostenerstattung | ja |
| Entgangener Gewinn | nein | ja (Deckungsbeitrag) |
| Folgeauftraege | nein | grundsaetzlich nein (zu spekulativ) |

## Echte-Chance-Doktrin
BGH-Linie (z. B. X ZR 100/04, X ZR 174/09): Positives Interesse nur, wenn Bieter im rechtmäßigen Verfahren mit hinreichender Wahrscheinlichkeit Zuschlag erhalten haette. Echte Chance = > 50 Prozent.

Konsequenz für die Klageschrift:
- Hypothetische Wertung darlegen.
- Mitbewerberangebote (soweit bekannt) einbeziehen.
- Wertungsfehler quantifizieren.

## Mitverschulden § 254 BGB
- Ruege unterlassen? -> Mitverschulden bis Anspruchsverlust.
- Eigene Angebotsfehler -> Quotelung.

## Verfahren
- Zuständigkeit: Landgericht (oder Amtsgericht bei niedrigem Streitwert) am Sitz des Auftraggebers, ZPO-Klage.
- Beweislast: Bieter trifft Beweislast für Pflichtverletzung, Kausalitaet, Hoehe; bei festgestellter Rechtsverletzung durch VK/OLG: Indizwirkung.
- Streitwert: Hoehe des geltend gemachten Schadens.

## Output
- Klageschriftsatz-Geruest LG mit Antraegen, Sachverhalt, rechtlicher Wuerdigung, Schadensberechnung.
- Schadensberechnungs-Tabelle (Angebotskosten, Deckungsbeitrag, Mitverschulden).
- Verjährungs-Pruefvermerk.

## Quellenregel
BGH-Entscheidungen vor Ausgabe ueber dejure.org oder bundesgerichtshof.de verifizieren (Gericht, Datum, Aktenzeichen, tragende Aussage).

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 2. `aufklaerung-nachforderung-56-vgv`

**Fokus:** Aufklaerung, Nachforderung und Angebotsaufklaerung steuern: fehlende Unterlagen, unklare Preise, ungewoehnlich niedrige Angebote, Gleichbehandlung und Grenzen der Nachbesserung.

### Aufklaerung und Nachforderung

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll Nachforderung und Aufklaerung rechtssicher einsetzen oder angreifen. Er arbeitet für Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

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
- Ampel: Frist, Zuständigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Nachforderungsschema, Aufklaerungsfragen, Risikoampel, Vermerk.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` für Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` für Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` für Aktenarbeit.
- `nachpruefungsantrag-powerdraft` für VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` für komplexe Mehrthemenfaelle.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 3. `fachanwalt-vergaberecht-ruege-vor-zuschlag`

**Fokus:** Vergaberechtliche Ruege nach § 160 Abs. 3 GWB vor Zuschlag erheben: Bieter hat Vergabeverstoesse erkannt und muss rügen bevor Zuschlag erteilt wird. Normen: § 160 Abs. 3 GWB (Ruegerobliegenheit als Praeklusionsvoraussetzung). Prüfraster: Fristen (Bekanntmachungs-Verstoesse bis Angebotsabgabe, sonstige Verstoesse 10 Tage), Inhaltliche Anforderungen, Reaktionspflicht Auftraggeber (Abhilfe/Zurückweisung). Output Ruege-Schreiben mit konkretem Verstoß, Norm und Sachverhalt. Abgrenzung: Nachprüfungsantrag nach Ruege siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk; Ruegeschriftsatz-Detail siehe ruegeschriftsatz-erstellen.

### Rüge vor Zuschlag

## Kaltstart-Rückfragen

1. Wie hat der Mandant vom Vergabeverstoß Kenntnis erlangt (Bekanntmachung, Vergabeunterlagen, Informationsschreiben § 134 GWB, sonstige Mitteilung)?
2. Zu welchem Zeitpunkt erfolgte die Kenntniserlangung (für Berechnung der 10-Tage-Frist)?
3. Steht der Auftrag oberhalb EU-Schwellenwert § 106 GWB?
4. Wurde der Verstoß bereits gerügt oder soll erstmalig gerügt werden?
5. Welche konkrete Norm wird verletzt (GWB, VgV, SektVO, KonzVgV, UVgO)?

## Anspruchsgrundlagen

- Rügeobliegenheit § 160 Abs. 3 GWB als Präklusionsvoraussetzung für Nachprüfungsantrag.
- § 160 Abs. 3 Satz 1 Nr. 1 GWB: 10 Kalendertage ab Kenntnis für sonstige Verstöße.
- § 160 Abs. 3 Satz 1 Nr. 2 GWB: erkennbare Verstöße aus Bekanntmachung bis Ablauf Angebotsfrist.
- § 160 Abs. 3 Satz 1 Nr. 3 GWB: erkennbare Verstöße aus Vergabeunterlagen bis Ablauf Angebotsfrist.
- § 160 Abs. 3 Satz 1 Nr. 4 GWB: 15 Kalendertage Antragsfrist nach Zurückweisung der Rüge.
- Inhaltsanforderungen: konkrete Bezeichnung des Verstoßes, Begründung, betroffene Norm; Beweismittel sollen genannt werden.
- Verifizierte Eckentscheidungen (curia.europa.eu): EuGH 28.10.2020, C-521/18 (Pegaso) — De-facto-Vergaben; EuGH 03.06.2022, C-376/21 (Zamestnik) — Verhaeltnismaessigkeit; EuGH 21.12.2023, C-66/22 (Infraestruturas) — Wettbewerbsverstoss. Vor Ausgabe konkrete OLG-Vergabesenat-Entscheidungen ueber olg-... bzw. openjur.de verifizieren.
- Rüge keine Formvorgabe — Textform ausreichend, Schriftform empfohlen für Dokumentation.

## Beweislast und Frist

- Antragsteller trägt Beweislast für rechtzeitige Rüge und Eingang beim Auftraggeber.
- Auftraggeber trägt Beweislast für Vorabkenntnis des Bieters bei behaupteter Präklusion.
- 10-Tage-Frist beginnt mit positiver Kenntnis — grob fahrlässige Unkenntnis genügt nicht.
- Frist endet am 10. Tag um 24:00 Uhr; Eingang beim Auftraggeber maßgeblich.

## Prüfschema vor Rügeerhebung

```
1. Kenntniszeitpunkt fixieren (Datum + Quelle)
2. Fristtyp § 160 Abs. 3 GWB bestimmen
3. Frist bis Ruegeerhebung berechnen
4. Konkrete Norm und Verstoss benennen
5. Beweismittel benennen
6. Antrag formulieren (Abhilfe + Nachpruefungsandrohung)
7. Sicheren Zugangsnachweis (Empfangsbestaetigung)
8. Kalender — 15 Tage Antragsfrist nach Zurueckweisung
```

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Schreibvorlage Rüge § 160 Abs. 3 GWB

```
An [Auftraggeber Vergabestelle Anschrift]
Per E-Mail mit Lesebestaetigung und vorab per Telefax

Az Vergabeverfahren: [...]
Bekanntmachung TED-Nr. [...]

Ruege gemaess § 160 Abs. 3 GWB

Sehr geehrte Damen und Herren,

namens und in Vollmacht unseres Mandanten — Bieter im o.g. Vergabe-
verfahren — ruegen wir folgenden Vergabeverstoss:

1. Sachverhalt:
[Verstoss konkret beschreiben — z.B. Wertung des Angebots der Beigeladenen
 entgegen § 56 VgV ohne Pruefung der ungewoehnlich niedrigen Preise]

2. Kenntnis:
Unser Mandant hat von dem Verstoss durch [Quelle, Datum] erstmals
Kenntnis erlangt. Die 10-Tage-Frist § 160 Abs. 3 Satz 1 Nr. 1 GWB ist
gewahrt.

3. Rechtsverletzung:
- Verstoss gegen § 56 VgV (Pruefung ungewoehnlich niedriger Angebote)
- Verstoss gegen § 97 Abs. 1 GWB (Wettbewerb und Transparenz)
- Verstoss gegen § 97 Abs. 2 GWB (Gleichbehandlung)

4. Beweismittel:
[Anlagen K1-K3 — Vergabeunterlagen, eigenes Angebot, oeffentlich
verfuegbare Vergleichsdaten]

5. Antrag:
Wir fordern Sie auf binnen drei Werktagen
- den Verstoss durch [Massnahme] zu beseitigen
- das Vergabeverfahren bis zur Klaerung auszusetzen

Andernfalls werden wir umgehend Nachpruefungsantrag bei der zuständigen
Vergabekammer stellen. Wir behalten uns Schadensersatzanspruechen
§ 181 GWB ausdruecklich vor.

Mit freundlichen Gruessen
```

## Übergabe

- Bei Abhilfe: Dokumentation der Korrektur, Verfahrensbeobachtung.
- Bei Zurückweisung: 15-Tage-Frist § 160 Abs. 3 Nr. 4 GWB notieren; Übergang in `fachanwalt-vergaberecht-nachpruefungsantrag-vk`.
- Bei Schweigen mehr als 10 Tage: Nachprüfungsantrag prüfen.

## Vertiefung: Leitsaetze Ruegerecht und Entscheidungsbaum

### Ergaenzende Leitsaetze Ruege § 160 GWB (Stand 05/2026)

- EuGH 28.10.2020, C-521/18 (Pegaso) — De-facto-Vergabe nichtig nach § 135 GWB / Art. 2d RL 89/665 (curia.europa.eu)
- EuGH 03.06.2022, C-376/21 (Zamestnik) — Verhaeltnismaessigkeitspruefung obligatorisch
- EuGH 21.12.2023, C-66/22 (Infraestruturas) — schwerwiegende berufliche Verfehlung Art. 57 Abs. 4 RL
- Aktuelle OLG-Vergabesenat-Rspr. zu Ruegeprueclusion (§ 160 Abs. 3 GWB) konkret per olg-duesseldorf.nrw.de / olg-karlsruhe / openjur.de verifizieren

### Entscheidungsbaum Ruege § 160 GWB

```
Schritt 1: Liegt Mandat ueber EU-Schwellenwert? (§ 106 GWB)
 → NEIN: UVgO-Bereich; keine § 160-Pflicht; aber Ruege dennoch empfohlen
 → JA: weiter zu Schritt 2

Schritt 2: Wann Kenntnis vom Verstoss?
 → Aus Bekanntmachung/Vergabeunterlagen: Ruege bis Angebotsabgabe
 → Sonstige: 10 Tage ab Kenntnis (§ 160 Abs. 3 Nr. 1 GWB)

Schritt 3: Frist noch offen?
 → JA: Ruege sofort erheben
 → NEIN: Praeklusionsrisiko; Nachpruefungsantrag unzulaessig; Schadensersatz § 181 GWB pruefen

Schritt 4: Ruege erhoben — Reaktion Auftraggeber?
 → Abhilfe: Verfahren beobachten; keine weiteren Schritte noetig
 → Zurueckweisung: 15-Tage-Frist Nachpruefungsantrag § 160 Abs. 3 Nr. 4 GWB
 → Schweigen > 10 Tage: Nachpruefungsantrag pruefen

Schritt 5: Zuschlag erteilt?
 → Vor Zuschlag: Nachpruefungsantrag + Antrag Vorabentscheidung § 169 GWB
 → Nach Zuschlag: § 135 GWB Unwirksamkeit oder § 181 GWB Schadensersatz
```

### Normen-Kette Ruegeverfahren
- § 160 Abs. 3 GWB — Ruegefristen
- § 134 GWB — Informationspflicht/Stillhaltefrist
- § 135 GWB — Unwirksamkeit Zuschlag
- § 169 GWB — Vorabentscheidung / einstweilige Massnahmen
- § 181 GWB — Schadensersatz

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 4. `markterkundung-und-vorbefassung`

**Fokus:** Markterkundung, Vorbefassung und Interessenkonflikte rechtssicher steuern: zulaessige Informationsgewinnung, Ausgleichsmassnahmen, Dokumentation und Rugeabwehr.

### Markterkundung und Vorbefassung

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll Marktinformationen nutzen, ohne Wettbewerb und Gleichbehandlung zu verletzen. Er arbeitet für Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

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
- Ampel: Frist, Zuständigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Markterkundungsplan, Vorbefassungscheck, Neutralisierungsmassnahmen, Textbausteine.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` für Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` für Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` für Aktenarbeit.
- `nachpruefungsantrag-powerdraft` für VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` für komplexe Mehrthemenfaelle.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 8a BSIG
- § 8 WRegG
- § 106 VwVfG
- § 2 BSIG
- § 8b BSIG
- § 123 VwG
- Art. 28 DSGVO
- Art. 46 DSGVO
- § 29 VwVfG
- § 5 IFG
- § 129 StGB
- § 261 StGB

### Leitentscheidungen

- EuGH C-377/17
- BGH VII ZR 174/19
- EuGH C-107/98
- EuGH C-480/06
- EuGH C-376/21

