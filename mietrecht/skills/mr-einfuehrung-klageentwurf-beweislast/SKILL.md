---
name: mr-einfuehrung-klageentwurf-beweislast
description: "MR Einfuehrung Klageentwurf Beweislast: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# MR Einfuehrung Klageentwurf Beweislast

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **MR Einfuehrung Klageentwurf Beweislast** im Plugin Mietrecht (Wohnraum/Gewerbe). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mr-einfuehrung-vertragstypen` | Mietrecht einfuehrend: Wohnraum-, Gewerberaum-, Pacht-, Unter-, Index- und Staffelmiete. Schutzvorschriften pro Typ, Kuendigungsregime, typische Klauselrisiken. Entscheidungstabelle. |
| `spezial-klageentwurf-beweislast-und-darlegungslast` | Klageentwurf: Beweislast, Darlegungslast und Substantiierung im Mietrecht: fachlich vertiefter Fachmodul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begründung im Kündigungsschreiben (§ 573 Abs. 3 BGB) Kündigungsfristen nach § 573c BGB (drei sechs neun Monate je nach Mietdauer) Sperrfristen aus Landesverordnung (drei bis zehn Jahre nach Umwandlung) Sozialklausel des Mieters (§ 574 BGB) und Risiko der Vortaeuschung (Schadensersatz). Erzeugt rechtssicheres Kündigungsschreiben mit Disclaimer. |

## Arbeitsweg

Im Plugin Mietrecht (Wohnraum/Gewerbe) gilt für **MR Einfuehrung Klageentwurf Beweislast**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mr-einfuehrung-vertragstypen`

**Fokus:** Mietrecht einfuehrend: Wohnraum-, Gewerberaum-, Pacht-, Unter-, Index- und Staffelmiete. Schutzvorschriften pro Typ, Kuendigungsregime, typische Klauselrisiken. Entscheidungstabelle.

# Mietrecht: Vertragstypen

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietrecht: Vertragstypen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Mietrecht: Vertragstypen
- **Spezialgegenstand:** Mietrecht: Vertragstypen / mr einfuehrung vertragstypen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `spezial-klageentwurf-beweislast-und-darlegungslast`

**Fokus:** Klageentwurf: Beweislast, Darlegungslast und Substantiierung im Mietrecht: fachlich vertiefter Fachmodul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Klageentwurf: Beweislast, Darlegungslast und Substantiierung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Klageentwurf: Beweislast, Darlegungslast und Substantiierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Klageentwurf: Beweislast, Darlegungslast und Substantiierung
- **Spezialgegenstand:** Klageentwurf: Beweislast, Darlegungslast und Substantiierung / klageentwurf beweislast und darlegungslast. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Klageentwurf** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Klage Amtsgericht (Mietsache)
- **Zuständigkeit (§ 23 Nr. 2 lit. a GVG, § 29a ZPO):** AG am Belegenheitsort der Mietsache - sachlich und örtlich ausschließlich für Streitigkeiten aus Wohnraummietverhältnissen, unabhängig vom Streitwert.
- **Klageschriftliche Pflichtangaben (§§ 253 Abs. 2, 130, 130a ZPO):** Bezeichnung der Parteien (vollständig mit Adresse), bestimmter Klageantrag (Räumung: konkrete Wohnung, Adresse, Stockwerk, Lage), Tatsachen und Beweismittel, Unterschrift bzw. qualifizierte elektronische Signatur. Anwaltszwang vor AG nicht (§ 78 Abs. 3 ZPO), in Mietsachen aber dringend empfohlen.
- **Streitwert:** Bei Räumung (§ 41 Abs. 2 GKG) = Jahresnettokaltmiete (zwölf Monate). Bei Mieterhöhung: einjähriger Erhöhungsbetrag (§ 41 Abs. 5 GKG). Bei Mietminderung: Jahresbetrag der Minderung. Bei Mietzahlung: konkrete Forderungssumme.
- **Substantiierungspflicht:** Klage muss jedes anspruchsbegründende Tatbestandsmerkmal mit Tatsachen unterlegen. Beispiel Zahlungsverzugskündigung: Mietvertrag (Anlage), vereinbarte Miete, Fälligkeit, Höhe und Zeitraum des Rückstands monatsweise (§ 569 Abs. 4 BGB), Zugang der Kündigung, Schonfristhinweis.
- **Vollstreckungsschutz/Räumungsfrist (§ 721 ZPO):** Auf Antrag des Beklagten in Räumungssachen ist Räumungsfrist von bis zu einem Jahr zu gewähren bei Vorliegen einer besonderen Härte (Familie, Schwangerschaft, Gesundheit, fehlender Ersatzwohnraum). Antrag muss spätestens bei der mündlichen Verhandlung erfolgen.
- **Schonfristzahlung im Prozess (§ 569 Abs. 3 BGB):** Tilgt nur die fristlose Kündigung, nicht eine hilfsweise erklärte ordentliche (BGH ständige Rspr.). Klägerseite muss in der Praxis Doppelkündigung erklären, sonst Räumung scheitert.
- **Beweismittel-Bündel:** Mietvertrag, Anlagen, Kündigungsschreiben mit Zugangsnachweis, Kontoauszüge, Zustellungsnachweis, ggf. Zeugenangabe mit ladungsfähiger Adresse.

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

## 3. `eigenbedarfskuendigung-erstellen`

**Fokus:** Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begründung im Kündigungsschreiben (§ 573 Abs. 3 BGB) Kündigungsfristen nach § 573c BGB (drei sechs neun Monate je nach Mietdauer) Sperrfristen aus Landesverordnung (drei bis zehn Jahre nach Umwandlung) Sozialklausel des Mieters (§ 574 BGB) und Risiko der Vortaeuschung (Schadensersatz). Erzeugt rechtssicheres Kündigungsschreiben mit Disclaimer.

# Eigenbedarfskündigung erstellen (Vermieter / Hausverwaltung)

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eigenbedarfskündigung erstellen (Vermieter / Hausverwaltung)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Disclaimer (Schlüsselstelle, mehrfach)

Die Eigenbedarfskündigung ist eines der streitanfälligsten Felder des Mietrechts. Eine formell oder materiell fehlerhafte Kündigung ist unwirksam — der Mieter darf in der Wohnung bleiben. Bei späterem Wegfall des Eigenbedarfs vor Auszug droht **Schadensersatz** (BGH-Rspr. zur Vortaeuschung). Vor Versand ist eine fachanwaltliche Prüfung dringend empfohlen. Diese Auto-Erstellung ersetzt nicht die anwaltliche Vertretung.

## Workflow

### Schritt 1 — Berechtigtes Interesse prüfen (§ 573 Abs. 2 Nr. 2 BGB)

- **Eigennutzung** durch den Vermieter selbst.
- **Familienangehörige** — Eltern Kinder Geschwister Ehegatten eingetragene Lebenspartner.
- **Haushaltsangehörige** — Personen die mit dem Vermieter dauerhaft im Haushalt leben (z. B. Pflegekraft Lebensgefährtin).
- Eigenbedarf juristischer Personen (GmbH AG) ist nicht möglich — Kündigung wegen Eigenbedarfs setzt natürliche Person voraus.
- **Konkret** und vernuenftig nachvollziehbar — nicht bloss vorsorglich oder spekulativ.

### Schritt 2 — Begründung im Kündigungsschreiben (§ 573 Abs. 3 BGB)

Die Begründung muss im Schreiben enthalten sein und so konkret sein dass der Mieter die Schlüssigkeit prüfen kann:

- Name der begünstigten Person und Verhältnis zum Vermieter.
- Warum die Wohnung gerade für diese Person benötigt wird.
- Aktuelle Wohnsituation der begünstigten Person.
- Zeitpunkt des Bedarfs.

Pauschale Floskeln wie "wegen Eigenbedarfs" reichen nicht.

### Schritt 3 — Kündigungsfristen (§ 573c BGB)

Je nach Dauer des Mietverhältnisses beim Mieter:

- Bis fünf Jahre: **drei Monate**.
- Fünf bis acht Jahre: **sechs Monate**.
- Ab acht Jahren: **neun Monate**.

Zugang spätestens am dritten Werktag eines Monats für das Ende dieses Monats plus die jeweilige Frist.

### Schritt 4 — Sperrfristen nach Landesverordnung

Bei Umwandlung der Mietwohnung in eine Eigentumswohnung **vor** der Veräußerung an einen neuen Eigentümer gilt nach § 577a BGB eine **Sperrfrist von drei Jahren** ab Veräußerung — in Gebieten mit angespanntem Wohnungsmarkt durch Landesverordnung verlängert auf bis zu **zehn Jahre**. Prüfung in `references/mietspiegel-quellen.md` (Spalte Kündigungssperrfristverordnung).

### Schritt 5 — Sozialklausel (§ 574 BGB)

Der Mieter kann der Kündigung widersprechen wenn:

- Beendigung eine **Härte** bedeutet die auch unter Würdigung der berechtigten Interessen des Vermieters nicht zu rechtfertigen ist.
- Klassische Härtefälle: hohes Alter Krankheit Schwangerschaft fehlender Ersatzwohnraum.
- Widerspruch ist spätestens **zwei Monate vor Ende** der Mietzeit zu erklären (§ 574b Abs. 2 BGB).
- Rechtsfolge: Fortsetzung des Mietverhältnisses für angemessene Zeit (§ 574a BGB).

Der Vermieter muss im Kündigungsschreiben auf das Widerspruchsrecht hinweisen (§ 568 Abs. 2 BGB) — sonst verlängerte Widerspruchsfrist.

### Schritt 6 — Vortaeuschung und Schadensersatz (verifiziert dejure.org)

- **BGH 14.12.2016, VIII ZR 232/15**: Bei Vortaeuschung des Eigenbedarfs haftet der Vermieter dem gekuendigten Mieter auf Schadensersatz nach §§ 280 Abs. 1, 311a Abs. 2 BGB; ersatzfaehig sind Umzugskosten, Maklerkosten, Mehrkosten neuer Mietwohnung und ggf. Anwaltskosten. Quelle: dejure.org/2016,46126 / NJW 2017, 1474.
- **BGH 10.05.2017, VIII ZR 292/15**: Wegfall des Eigenbedarfs nach Ausspruch der Kuendigung — Vermieter muss den Mieter unverzueglich informieren, sonst Schadensersatzpflicht. Quelle: dejure.org/2017,15097.
- **BGH 27.06.2007, VIII ZR 271/06**: Eigenbedarf einer GbR (Aussengesellschaft) — Eigenbedarf kann fuer die Gesellschafter geltend gemacht werden, sofern die GbR Vermieter ist und der Gesellschafter Eigenbedarf hat. Quelle: dejure.org / NJW 2007, 2845.

### Schritt 7 — Formale Anforderungen (§ 568 Abs. 1 BGB)

- **Schriftform** zwingend — eigenhändige Unterschrift des Vermieters (oder aller Vermieter wenn Personenmehrheit).
- Bei juristischer Person als Vermieter: Unterschrift des organschaftlich Vertretungsberechtigten.
- **Adressierung** alle Mieter namentlich.
- **Zustellung** nachweisbar (Einschreiben mit Rückschein oder Bote mit Zustellungsprotokoll).

## Schreiben-Entwurf

Erzeuge ein Kündigungsschreiben mit:

1. Absender Vermieter mit Anschrift.
2. Adresse aller Mieter namentlich.
3. Bezugnahme auf den Mietvertrag (Datum Mietsache).
4. Kündigungserklärung mit konkretem Endtermin.
5. Begründung nach § 573 Abs. 3 BGB: begünstigte Person Verhältnis Wohnsituation Bedarfslage.
6. Hinweis auf das Widerspruchsrecht des Mieters nach § 574 BGB und die Widerspruchsfrist nach § 574b Abs. 2 BGB.
7. Eigenhaendige Unterschrift aller Vermieter.
8. **Disclaimer** — Hinweis dass der Mieter sich beraten lassen sollte (Mieterverein Fachanwalt).

## Vor Versand (Disclaimer wiederholt)

Vor Versand der Eigenbedarfskündigung: fachanwaltliche Prüfung. Risiko: Unwirksamkeit Schadensersatz strafrechtliche Verfolgung bei Vortaeuschung. Sperrfristen aus Landesverordnung prüfen.

## Aktuelle Rechtsprechung Eigenbedarfskündigung (Stand 05/2026, verifiziert dejure.org)

- BGH, Urt. v. 24.09.2025 – Az. VIII ZR 289/23 — Anforderungen an die Begruendung nach § 573 Abs. 3 BGB sind nicht ueberzogen; Eigenbedarf bleibt wirksam auch wenn der Vermieter zunaechst Eigennutzung waehrend Umbau plant und spaetere Veraeusserung beabsichtigt. Konkretisierung des Massstabs „ernsthafter, vernuenftiger, nachvollziehbarer Eigennutzungswunsch". Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=24.09.2025&Aktenzeichen=VIII+ZR+289/23
- BGH 14.12.2016, VIII ZR 232/15 — Schadensersatz bei vorgetaeuschtem Eigenbedarf (https://dejure.org/2016,46126)
- BGH 10.05.2017, VIII ZR 292/15 — Mitteilungspflicht bei Wegfall des Eigenbedarfs (https://dejure.org/2017,15097)
- BGH 22.05.2019, VIII ZR 180/18 — Haerteklausel § 574 BGB; Pflicht zur Abwaegung Vermieter-/Mieterinteressen, alters- oder krankheitsbedingte Haerten substantiiert pruefen (https://dejure.org/2019,12824)
- BGH 11.12.2019, VIII ZR 144/19 — Haerteklausel: Hochbetagtes Alter und langjaehrige Verwurzelung koennen Vertragsfortsetzung tragen; nur ausnahmsweise unbefristete Fortsetzung (https://dejure.org/2019,49075)
- BGH 09.05.2012, VIII ZR 238/11 — „Vorratskündigung"-Verbot; Eigenbedarf muss konkret-bevorstehend sein (https://dejure.org/2012,12036)

Weitere Entscheidungen vor Ausgabe per dejure.org / bundesgerichtshof.de mit Datum und Aktenzeichen verifizieren.

## Paragrafenkette Eigenbedarfskündigung

§ 573 Abs. 2 Nr. 2 BGB (berechtigtes Interesse Eigenbedarf) → § 573 Abs. 3 BGB (Begründungspflicht) → § 573c BGB (Kündigungsfristen) → § 568 Abs. 1 BGB (Schriftform) → § 568 Abs. 2 BGB (Widerspruchshinweis) → § 574 BGB (Sozialklausel Widerspruch) → § 574b BGB (Widerspruchsfrist 2 Monate) → § 577a BGB (Sperrfrist nach Umwandlung) → § 280 BGB (Schadensersatz bei vorgetäuschtem Eigenbedarf)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage vor Erstellung Eigenbedarfskündigung

Kläre vor Beginn:
1. Natürliche Person als Vermieter? (Juristische Personen können keinen Eigenbedarf geltend machen)
2. Berechtigte Person konkret benannt? (Name Verhältnis Wohnsituation Bedarfsgrund)
3. Wurde die Wohnung nach Abschluss des Mietvertrags in Wohnungseigentum umgewandelt? (Sperrfrist § 577a BGB prüfen)
4. Welche Mietdauer liegt vor? (Bestimmt Kündigungsfrist § 573c BGB)
5. Ist der Hinweis auf das Widerspruchsrecht nach § 574 BGB vorbereitet?

## Output-Template Eigenbedarfskündigungsschreiben

**Adressat:** Mieter — Tonfall sachlich-erklärend, Schriftform zwingend

```
[VERMIETER]
[ADRESSE VERMIETER]

An [ALLE MIETER MIT NAMEN]
[ADRESSE MIETWOHNUNG]

[ORT], [DATUM]

Kündigung des Mietverhältnisses wegen Eigenbedarfs

Sehr geehrte/r Herr/Frau [NAME],

hiermit kündige ich das mit Ihnen bestehende Mietverhältnis über die Wohnung
[ANSCHRIFT, LAGE, STOCKWERK, QM] vom [DATUM DES MIETVERTRAGS] gemäß § 573
Abs. 2 Nr. 2 BGB ordentlich zum [KÜNDIGUNGSTERMIN, berechnet nach § 573c BGB].

Begründung (§ 573 Abs. 3 BGB):
Ich benötige die Wohnung für [BEGÜNSTIGTE PERSON, VERHÄLTNIS].
[BEGÜNSTIGTE PERSON] lebt derzeit in [AKTUELLE WOHNSITUATION].
Die aktuelle Unterkunft ist nicht zumutbar, weil [BEDARFSGRUND: zu klein/zu weit/gesundheitliche Gründe/etc.].

Hinweis auf Widerspruchsrecht (§ 574 BGB):
Sie können der Kündigung widersprechen, wenn die Beendigung des Mietverhältnisses
für Sie eine unzumutbare Härte bedeutet. Der Widerspruch muss spätestens zwei Monate
vor Ablauf der Kündigungsfrist schriftlich erfolgen (§ 574b Abs. 2 BGB).

Mit freundlichen Grüßen
[EIGENHAENDIGE UNTERSCHRIFT ALLER VERMIETER]
```

**Hinweis:** Vor Versand fachanwaltliche Prüfung empfohlen.

<!-- AUDIT 27.05.2026
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Quelle: dejure.org. Prufer: Bundle-005-Audit.
-->
