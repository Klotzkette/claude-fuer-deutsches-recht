---
name: strafz-strafzumessungstatsachen
description: "Strafz Strafzumessungstatsachen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Strafz Strafzumessungstatsachen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Strafz Strafzumessungstatsachen** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafz-strafzumessungstatsachen-bauleiter` | Bauleiter Strafzumessungstatsachen § 46 StGB: Schwere der Tat, Schuld, Vorleben, Nachtatverhalten. Pruefraster fuer Plaedoyer und Urteil. |
| `strafzumessungs-tatsachen-46-ii-stgb` | Katalog der Strafzumessungstatsachen § 46 Abs. 2 StGB. Beweggruende und Ziele (auch menschenverachtende), Gesinnung und Wille, Mass der Pflichtwidrigkeit, Art der Ausfuehrung und verschuldete Auswirkungen, Vorleben, persoenliche und wirtschaftliche Verhaeltnisse, Nachtatverhalten und Wiedergutmachungsbemuehen. Anwendung in Plaedoyer, Urteilsbegruendung und Strafzumessungsruege. |
| `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` | Bestimmung der Tagessatzhoehe nach § 40 Abs. 2 StGB. Hoehe richtet sich nach Nettoeinkommen geteilt durch 30; Mindesthoehe 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Sonderfaelle Arbeitslose, Buergergeld-Empfaenger, Studierende, Selbststaendige, Unterhaltspflichtige, Rentner. Antrag auf Ratenzahlung § 42 StGB, Ersatzfreiheitsstrafe § 43 StGB. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **Strafz Strafzumessungstatsachen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafz-strafzumessungstatsachen-bauleiter`

**Fokus:** Bauleiter Strafzumessungstatsachen § 46 StGB: Schwere der Tat, Schuld, Vorleben, Nachtatverhalten. Pruefraster fuer Plaedoyer und Urteil.

# StrafZ: Tatsachen Bauleiter

## Spezialwissen: StrafZ: Tatsachen Bauleiter
- **Spezialgegenstand:** StrafZ: Tatsachen Bauleiter / strafz strafzumessungstatsachen bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH.
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

## 2. `strafzumessungs-tatsachen-46-ii-stgb`

**Fokus:** Katalog der Strafzumessungstatsachen § 46 Abs. 2 StGB. Beweggruende und Ziele (auch menschenverachtende), Gesinnung und Wille, Mass der Pflichtwidrigkeit, Art der Ausfuehrung und verschuldete Auswirkungen, Vorleben, persoenliche und wirtschaftliche Verhaeltnisse, Nachtatverhalten und Wiedergutmachungsbemuehen. Anwendung in Plaedoyer, Urteilsbegruendung und Strafzumessungsruege.

# Strafzumessungstatsachen — § 46 Abs. 2 StGB

## Worum geht es?

§ 46 Abs. 2 StGB fuehrt einen nicht abschliessenden Katalog der Tatsachen auf, die das Gericht bei der Strafzumessung gegeneinander abzuwaegen hat. Der Skill zerlegt jeden Katalogpunkt und zeigt, welche Tatsachen Verteidigung und Anklage dazu konkret vortragen.

## Wann brauchen Sie diese Skill?

- Sie bereiten den Schlussvortrag vor und brauchen ein Geruest fuer die Strafzumessungsargumentation.
- Sie schreiben oder reviewen einen Strafzumessungsabschnitt in einem Urteilsentwurf.
- Sie pruefen eine Strafzumessungsruege: Welche Tatsachen sind uebersehen, welche unzulaessig gewertet?

## Rechtliche Grundlagen

- **§ 46 Abs. 2 StGB** — Katalogvorschrift; nicht abschliessend.
- **§ 46 Abs. 3 StGB** — Doppelverwertungsverbot, vgl. `paragraph-46-stgb-grundsatz-strafzumessung`.
- **§ 267 Abs. 3 StPO** — Begruendungspflicht im Strafurteil; vgl. `267-iii-stpo-begruendungsanforderungen-strafurteil`.
- **Art. 6 EMRK** — Verfahrensdauer; rechtsstaatswidrige Verzoegerung als Kompensationsfaktor (Vollstreckungsmodell der st. Rspr.).

## Strafzumessungs-Grundsatz

Jede der genannten Tatsachen ist nur insoweit beachtlich, als sie die **Schuld** oder die zu erwartenden **Wirkungen fuer das kuenftige Leben** beeinflusst. Reines Charakter-Urteil ueber den Taeter ohne Tatbezug ist unzulaessig.

## Katalog-Aufschluesselung

### 1. Beweggruende und Ziele

- Geld-, Macht-, Rache-, Lust-, Hass-Motive haben unterschiedliches Gewicht.
- **Menschenverachtende Beweggruende** (§ 46 Abs. 2 Satz 2 StGB seit 01.08.2015) — ausdruecklich: rassistische, fremdenfeindliche, antisemitische, geschlechtsspezifische, gegen die sexuelle Orientierung gerichtete oder sonstige menschenverachtende.
- Notlage, Provokation, Affekt: Beweggrund kann strafmildernd sein.

### 2. Gesinnung und Tatwille

- Was sagt die Tat ueber die innere Haltung? Hoehe der kriminellen Energie?
- Plan oder Spontantat? Lange Tatvorbereitung deutet auf hoehere Energie hin.

### 3. Mass der Pflichtwidrigkeit

- Bei Fahrlaessigkeitsdelikten zentral: leichte, mittlere, grobe Fahrlaessigkeit.
- Verkehrsdelikt: Geschwindigkeit, Alkohol, Vorbelastung.
- Pflichtwidrigkeit bei Sonderdelikten (Amtstraeger, Arzt, Treuhaender) hoeher zu gewichten.

### 4. Art der Ausfuehrung und verschuldete Auswirkungen

- Brutalitaet, Dauer, Demuetigung, Mitwirkung mehrerer.
- Tatfolgen: Schadenshoehe, Dauerschaeden, Verletzungstiefe, psychische Folgen beim Opfer.
- Aber: **Doppelverwertungsverbot** beachten — Folgen, die schon Tatbestandsmerkmal sind, duerfen nicht erneut schaerfend wirken.

### 5. Vorleben

- Vorstrafen (BZRG-Auszug, beachten Tilgung §§ 46 ff. BZRG); je einschlaegiger und juenger, desto gewichtiger.
- **Schweigen ueber das Vorleben** darf nicht schaerfend gewertet werden.
- Erziehung, soziale Sozialisation, Lebensbruch (Drogen, Krankheit).

### 6. Persoenliche und wirtschaftliche Verhaeltnisse

- Familie, Beruf, Verschuldung, Suchtkrankheit, psychische Erkrankung.
- Auslaenderrechtliche Folgen (Ausweisung, § 53 ff. AufenthG): von der st. Rspr. nur insoweit beachtlich, als sie ueber das gesetzlich Vorgesehene hinausgehen.
- Berufsverbot, Approbationsentzug, beamtenrechtliche Disziplinarfolgen.

### 7. Nachtatverhalten

- **Gestaendnis** (besonders bei prozessoekonomischem Wert; vgl. `gestaendnis-und-strafmilderung`).
- **Reue, Einsicht, Selbstanzeige**.
- **Schadenswiedergutmachung** und **TOA** (§ 46a StGB; vgl. `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung`).
- **Hilfe bei der Aufklaerung** (§§ 31 BtMG, 46b StGB — Kronzeugenregelung).
- **Belastendes Nachtatverhalten**: Verdunkelungsversuche, Drohungen gegen Zeugen, Verleumdung des Opfers in der Hauptverhandlung.

## Schritt-fuer-Schritt-Anleitung

1. **Tatsachenmaterial sammeln**: Akte, Anhoerung, Sozialbericht, BZRG-Auszug, Einkommensdaten.
2. **Katalog durchgehen**: Jede der sieben Gruppen pruefen; nur substantiierte Tatsachen.
3. **Gewichtung**: Pro Gruppe Pluspunkte (zugunsten) und Minuspunkte (zulasten) explizit machen.
4. **Sondernormen**: § 46a StGB (TOA), § 46b StGB (Aufklaerungshilfe), § 17 StGB (Verbotsirrtum), §§ 20, 21 StGB (Schuldminderung).
5. **Doppelverwertungs-Pruefung**: Welche Tatsache ist schon Tatbestandsmerkmal?
6. **Zusammenfuegen**: Gesamtbild aus Schuld + Praevention im Schuldrahmen.

## Beispielformulierungen fuer Verteidigung

- "Der Angeklagte hat sich aus akuter wirtschaftlicher Not zur Tat hinreissen lassen; eine einschlaegige Vorbelastung fehlt vollstaendig."
- "Das Gestaendnis hat dem Gericht eine umfangreiche Beweisaufnahme erspart; in der Folge hat sich der Angeklagte aktiv um eine Ausgleichszahlung an die Geschaedigte bemueht."
- "Die berufsrechtlichen Folgen treffen den Angeklagten mit ueberdurchschnittlicher Haerte, da seine Approbation infrage steht."
- "Die Verfahrensdauer von [X] Jahren ist als rechtsstaatswidrige Verzoegerung iSv Art. 6 EMRK zu kompensieren."

## Beispielformulierungen fuer Anklage

- "Die Tat zeichnet sich durch ein hohes Mass an krimineller Energie aus; der Angeklagte hat ueber Monate hinweg geplant."
- "Die Geschaedigte leidet unter posttraumatischer Belastungsstoerung; die Tatfolgen sind ueber das Tatbestandsmerkmal der Koerperverletzung hinaus erheblich."
- "Die Tat ist von menschenverachtenden Beweggruenden iSv § 46 Abs. 2 Satz 2 StGB getragen."
- "Der Angeklagte hat in der Hauptverhandlung die Geschaedigte als unglaubwuerdig bezeichnet und damit die psychischen Tatfolgen vertieft."

## Typische Fehler

- Schweigen schaerfend gewertet. Verstoss gegen § 261 StPO i.V.m. Selbstbelastungsfreiheit.
- Vorstrafen ohne Pruefung der **Tilgungsreife** verwertet. Verstoss gegen § 51 BZRG.
- Lange Verfahrensdauer nicht kompensiert. Verstoss gegen Art. 6 EMRK.
- Auslaenderrechtliche Standard-Folgen schaerfend bei Auslaender verwertet (faktischer Sondervorwurf). Verstoss gegen Gleichheitsgrundsatz.
- Verschulden des Verteidigers / Anwalts dem Mandanten zugerechnet.
- Doppelverwertung von Tatbestandsmerkmalen (§ 46 Abs. 3 StGB).

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — Grundsatznorm.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — Spezialnorm.
- `gestaendnis-und-strafmilderung` — Detail Nachtatverhalten.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Umsetzung im Urteil.

## Quellen und Stand 05/2026

- § 46 Abs. 2 StGB in der seit 01.08.2015 geltenden Fassung.
- § 46 Abs. 3 StGB Doppelverwertungsverbot.
- §§ 46 ff. BZRG zur Verwertung von Vorstrafen.
- Art. 6 Abs. 1 EMRK; Vollstreckungsmodell zur Verfahrensdauer (Az verifizieren in juris/dejure.org).
- Quellenregel: vgl. `references/zitierweise.md`.

## 3. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst`

**Fokus:** Bestimmung der Tagessatzhoehe nach § 40 Abs. 2 StGB. Hoehe richtet sich nach Nettoeinkommen geteilt durch 30; Mindesthoehe 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Sonderfaelle Arbeitslose, Buergergeld-Empfaenger, Studierende, Selbststaendige, Unterhaltspflichtige, Rentner. Antrag auf Ratenzahlung § 42 StGB, Ersatzfreiheitsstrafe § 43 StGB.

# Tagessatzhoehe — § 40 Abs. 2 StGB

## Worum geht es?

Die **Hoehe** des einzelnen Tagessatzes bildet die wirtschaftliche Leistungsfaehigkeit des Taeters ab. Sie ist von der **Anzahl** der Tagessaetze (Schuldkomponente) zu trennen. Faustformel: monatliches Nettoeinkommen geteilt durch 30; Mindesthoehe 1 EUR (§ 40 Abs. 2 Satz 3 StGB).

## Wann brauchen Sie diese Skill?

- Sie pruefen einen Strafbefehl mit hoeherem Tagessatz, als die wirtschaftlichen Verhaeltnisse rechtfertigen.
- Sie bereiten die Hauptverhandlung vor und sammeln Einkommensnachweise fuer Ihren Mandanten.
- Sie schaetzen vor einer Verstaendigung (§ 257c StPO), welche Geldstrafe insgesamt droht.
- Sie pruefen einen Ratenzahlungsantrag nach § 42 StGB oder die drohende Ersatzfreiheitsstrafe nach § 43 StGB.

## Rechtliche Grundlagen

- **§ 40 Abs. 2 Satz 1 StGB** — Bemessung nach den persoenlichen und wirtschaftlichen Verhaeltnissen des Taeters.
- **§ 40 Abs. 2 Satz 2 StGB** — Ausgangspunkt: durchschnittliches Nettoeinkommen, das der Taeter an einem Tag hat oder haben koennte.
- **§ 40 Abs. 2 Satz 3 StGB** — Tagessatzhoehe mindestens 1, hoechstens 30 000 EUR.
- **§ 40 Abs. 3 StGB** — Schaetzungsrecht des Gerichts.
- **§ 42 StGB** — Zahlungserleichterungen, Ratenzahlung.
- **§ 43 StGB** — Ersatzfreiheitsstrafe: ein Tag Freiheitsstrafe je uneinbringlichem Tagessatz.
- **§ 459d StPO** — Vollstreckungsgericht entscheidet ueber Uneinbringlichkeit.

## Berechnungsschema

```
1. Brutto-Monatseinkommen: [BETRAG] EUR
2. Abzuege Lohnsteuer + Sozialvers.: [BETRAG] EUR
3. Netto-Monatseinkommen: [BETRAG] EUR
4. Tagessatzhoehe (Netto / 30): [BETRAG] EUR
```

### Was vom Nettoeinkommen abzuziehen ist (Standard)

- **Werbungskosten** in normaler Hoehe (Fahrtkosten zur Arbeitsstelle).
- **Unterhaltspflichten** (Kindesunterhalt, Ehegattenunterhalt) — st. Rspr.; einzelfallabhaengig; Hoehe muss belegt sein.
- **Krankenversicherungsbeitraege** Selbststaendiger.

### Was **nicht** automatisch abgezogen wird

- Konsumschulden, Kreditraten — nur ausnahmsweise und einzelfallabhaengig.
- Steuerschulden (str.; in der Praxis oft nicht abgezogen).
- Beruflich notwendige Reise- oder Repraesentationskosten ohne Beleg.

## Sonderfaelle

### Arbeitslose und Buergergeld-Empfaenger

Bei Empfaengern von Buergergeld (§§ 19 ff. SGB II) sind die Tagessaetze in der Praxis sehr niedrig anzusetzen, oft **5 bis 15 EUR**. Die Regelsaetze des SGB II bilden das Existenzminimum; ein Tagessatz nahe 1 EUR ist moeglich, wenn unterhalb des Existenzminimums geleistet wird.

### Studierende

BAfoeG-/Eltern-Unterhaltsbetraege als Ausgangsgroesse. Tagessaetze in der Regel im Bereich **5 bis 15 EUR**.

### Selbststaendige

- Gewinn laut Einkommensteuerbescheid des letzten Jahres geteilt durch 12 als Monats-Netto.
- BWA/SuSa des laufenden Jahres als ergaenzender Beleg.
- Stark schwankende Einkommen: Durchschnitt der letzten drei Jahre.

### Rentner

Rentenbescheid; ergaenzend Kapitalertraege/Mieteinkuenfte.

### Vermoegen ohne Einkommen

Bei betraechtlichem Vermoegen ist eine fiktive Einkommens-Erhoehung moeglich (st. Rspr.; Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren).

### Schwarzgeld, undeklariertes Einkommen

Strafzumessung darf an **wirklichen** Einkuenften ansetzen; das ist sensibel und sollte mit dem Mandanten besprochen werden.

## Schaetzungsrecht des Gerichts (§ 40 Abs. 3 StGB)

Wenn der Angeklagte schweigt oder keine Nachweise vorlegt, schaetzt das Gericht. Das ist haeufig zu Lasten des Mandanten. **Vorbeugung**: Einkommensnachweise rechtzeitig einreichen.

## Einkommensnachweise-Checkliste

```
[ ] Lohnabrechnung letzte drei Monate
[ ] Steuerbescheid letztes Jahr
[ ] BWA + SuSa bei Selbststaendigen
[ ] Buergergeld-/Sozialhilfe-Bescheid
[ ] Rentenbescheid
[ ] Unterhaltstitel oder Zahlungsbeleg
[ ] Mietvertrag und Nebenkostenabrechnung (Existenzminimum)
[ ] Kreditvertraege und Tilgungsplan (nur bei einzelfallrelevant)
[ ] BAfoeG-Bescheid bei Studierenden
```

## Ratenzahlungsantrag — Template

**Adressat**: Vollstreckungsgericht / Staatsanwaltschaft

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Zahlungserleichterung nach § 42 StGB

Mein Mandant ist verurteilt zu [X] Tagessaetzen a [Y] EUR,
gesamt [GESAMTBETRAG] EUR Geldstrafe.

Aufgrund [Einkommensverhaeltnisse stichwortartig] ist mein Mandant
nicht in der Lage, den Gesamtbetrag in einer Summe zu zahlen.

Wir beantragen Ratenzahlung von [RATE] EUR monatlich beginnend
ab [DATUM]. Hilfsweise: Verlaengerung der Zahlungsfrist auf
[DATUM].

Anlage: Einkommensnachweis, Kontoauszug.
```

## Ersatzfreiheitsstrafe (§ 43 StGB)

- 1 Tag Freiheitsstrafe je uneinbringlichem Tagessatz.
- Vor Vollstreckung der Ersatzfreiheitsstrafe Antrag auf gemeinnuetzige Arbeit nach **§ 293 EGStGB** und landesrechtlichen Tilgungs-/Tilgungsverordnungen pruefen (Tilgungssatz je nach Bundesland; verifizieren in der jeweils einschlaegigen Verordnung).
- Reform durch JStVollzG-Reform 2023: 2 Stunden gemeinnuetzige Arbeit = 1 Tagessatz Tilgung in vielen Bundeslaendern; konkretes Bundesland pruefen.

## Typische Fehler

- **Schaetzung ohne Aktenlage** akzeptiert: Einkommensnachweise nachreichen, Antrag auf Aenderung im Erkenntnis- oder Vollstreckungsverfahren.
- **Unterhaltspflichten nicht beachtet**: Nettoeinkommen sinkt; Anhoerungs-/Nachweispflicht des Anwalts.
- **Konsumschulden pauschal abgezogen**: nur einzelfallabhaengig.
- **Ratenzahlungsantrag spaet**: nach Beginn der Vollstreckung schwieriger durchzusetzen.
- **Ersatzfreiheitsstrafe** dem Mandanten nicht erklaert: Eskalationsrisiko unterschaetzt.

## Querverweise

- `geldstrafe-tagessatzanzahl-bestimmen` — Anzahl der Tagessaetze.
- `strafbefehl-strafzumessung-407-stpo` — im Strafbefehl.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Ersatzfreiheitsstrafe-Vollstreckung.

## Quellen und Stand 05/2026

- §§ 40-43 StGB in der geltenden Fassung.
- § 459d StPO.
- § 293 EGStGB i.V.m. landesrechtlichen Tilgungsverordnungen.
- Quellenregel: vgl. `references/zitierweise.md`.
