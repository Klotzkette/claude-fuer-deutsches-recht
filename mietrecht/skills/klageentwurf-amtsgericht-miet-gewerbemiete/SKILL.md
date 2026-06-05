---
name: klageentwurf-amtsgericht-miet-gewerbemiete
description: "Klageentwurf Amtsgericht Miet Gewerbemiete: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klageentwurf Amtsgericht Miet Gewerbemiete

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Klageentwurf Amtsgericht Miet Gewerbemiete** im Plugin Mietrecht (Wohnraum/Gewerbe). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine AG-Grenze nach § 23 Nr. 1 GVG zehntausend Euro ab 01.01.2026 durch das Gesetz zur Stärkung der Amtsgerichte in Zivilsachen; davor fünftausend Euro. Örtliche Zuständigkeit am Belegenheitsort der Mietsache (§ 29a ZPO). Streitwertberechnung Anträge Sachverhalt rechtliche Würdigung Beweisangebote und formgerechte Anlagen. Kein Anwaltszwang vor dem Amtsgericht aber dringende Empfehlung anwaltlicher Prüfung. Disclaimer mehrfach. |
| `miet-gewerbemiete-vertragsklauseln-spezial` | Spezialfall Gewerbemiete: Wertsicherungsklauseln, Konkurrenzschutz, Schriftform § 550 BGB, Doppelschriftformklausel. Pruefraster fuer Vermieter und Mieter. |
| `miet-mietvertrag-bauleiter` | Bauleiter Wohnraum-Mietvertrag: Schoenheitsreparaturen, Kaution, Kuendigung, Mieterhoehung, Untervermietung. Pruefraster fuer Vermieter und Mieter. |

## Arbeitsweg

Im Plugin Mietrecht (Wohnraum/Gewerbe) gilt für **Klageentwurf Amtsgericht Miet Gewerbemiete**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klageentwurf-amtsgericht`

**Fokus:** Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine AG-Grenze nach § 23 Nr. 1 GVG zehntausend Euro ab 01.01.2026 durch das Gesetz zur Stärkung der Amtsgerichte in Zivilsachen; davor fünftausend Euro. Örtliche Zuständigkeit am Belegenheitsort der Mietsache (§ 29a ZPO). Streitwertberechnung Anträge Sachverhalt rechtliche Würdigung Beweisangebote und formgerechte Anlagen. Kein Anwaltszwang vor dem Amtsgericht aber dringende Empfehlung anwaltlicher Prüfung. Disclaimer mehrfach.

# Klageentwurf zum Amtsgericht (Mietsache)

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Klageentwurf zum Amtsgericht (Mietsache)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Disclaimer (Schlüsselstelle, mehrfach)

Eine Klageschrift ist ein Rechtsschriftsatz mit erheblichen Konsequenzen (Gerichtskosten, Anwaltskosten, Präklusion verspäteten Vortrags). Dieser Entwurf ist **kein Ersatz für anwaltliche Vertretung**. Vor Einreichung ist eine fachanwaltliche Prüfung dringend empfohlen. In Mietsachen vor dem Amtsgericht besteht zwar **kein Anwaltszwang** (§ 78 ZPO e contrario), die rechtlichen Risiken sind aber dennoch hoch.

## Workflow

### Schritt 1 — Sachliche Zuständigkeit

- **Wohnraummietsachen** — Amtsgericht ist nach § 23 Nr. 2a GVG zuständig für Streitigkeiten aus Mietverhältnissen über Wohnraum **ohne Rücksicht auf den Streitwert**.
- **Geschäftsraummiete** — allgemeine Streitwertgrenze des § 23 Nr. 1 GVG: AG bis **zehntausend Euro** ab dem 01.01.2026 durch das Gesetz zur Stärkung der Amtsgerichte in Zivilsachen (Bundesrat-Billigung 21.11.2025, Inkrafttreten 01.01.2026); darüber LG (§ 71 GVG). Übergangsregelung: Für vor dem 01.01.2026 anhängig gewordene Verfahren bleibt die alte Wertgrenze von fünftausend Euro maßgeblich. Quelle: BRAK-Nachrichten 24/2025 vom 26.11.2025. Anwaltszwang vor dem Landgericht greift ebenfalls erst ab zehntausend Euro Streitwert; die Berufungsbeschwer in § 511 Abs. 2 Nr. 1 ZPO wurde zugleich von 600 Euro auf 1.000 Euro angehoben.
- Streitwert ist in jedem Fall zu berechnen (für Kosten und Berufungssumme).

### Schritt 2 — Örtliche Zuständigkeit (§ 29a ZPO)

- Ausschließlich das Gericht des Ortes, an dem sich die **Mietsache befindet** (Belegenheitsort).
- Keine Abweichung durch Gerichtsstandsvereinbarung möglich (§ 40 Abs. 2 ZPO).

### Schritt 3 — Streitwertberechnung

- **Zahlungsklage** Nennbetrag der geforderten Summe.
- **Klage auf Zustimmung zur Mieterhöhung** Jahresbetrag des Erhöhungsbetrags (§ 41 Abs. 5 GKG).
- **Klage auf Mietsenkung / Mietpreisbremse** Jahresbetrag der streitigen Differenz (§ 41 Abs. 5 GKG analog).
- **Raeumungsklage** Jahresnettomiete (§ 41 Abs. 2 GKG).
- **Klage auf Belegeinsicht** Bruchteil der streitigen Abrechnung (Schätzung nach § 3 ZPO).

### Schritt 4 — Anträge formulieren

- Eindeutig, vollstreckbar.
- Hauptantrag, Hilfsanträge, Kostenantrag, Vorläufige-Vollstreckbarkeits-Antrag.

### Schritt 5 — Sachverhalt

- Parteien, Mietvertrag, Mietsache, streitiger Vorgang chronologisch.
- Belege als Anlagen (K1, K2, K3 ...).

### Schritt 6 — Rechtliche Würdigung

- Anspruchsgrundlage benennen (§§ BGB, BetrKV, HeizkostenV).
- Subsumtion knapp.
- Bei Mietspiegelfällen: Bezugnahme auf den amtlichen Mietspiegel aus `references/mietspiegel-quellen.md`.

### Schritt 7 — Beweisangebote

- Zeugen mit ladungsfähiger Anschrift.
- Sachverständigengutachten (§ 144 ZPO).
- Augenschein (§ 371 ZPO).
- Urkundenbeweis durch beigefügte Anlagen.

### Schritt 8 — Anlagen

- Mietvertrag.
- Streitige Schreiben (Mieterhöhung, Abrechnung, Ruege).
- Mietspiegelauszug (falls erforderlich).
- Lage- und Ausstattungsprotokoll.

## Gliederungsmuster der Klageschrift

1. Kopf (Gericht, Aktenzeichen, Parteien, Bevollmächtigte).
2. Anträge.
3. Begründung — Sachverhalt.
4. Begründung — Rechtliche Würdigung.
5. Beweisangebote.
6. Kostenantrag.
7. Antrag auf vorläufige Vollstreckbarkeit (§ 708 Nr. 11 ZPO).
8. Anlagen.

## Vor Einreichung (Disclaimer wiederholt)

Vor Einreichung beim Amtsgericht ist diese Klageschrift durch einen Fachanwalt für Mietrecht zu prüfen. Versäumte Tatsachen, falsche Anspruchsgrundlagen oder formale Fehler können zur Klageabweisung und Kostenlast führen. Diese Auto-Erstellung ersetzt nicht die anwaltliche Vertretung.

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Sachliche Zustaendigkeit: § 23 Nr. 2a GVG (Wohnraum), § 71 GVG (LG)
- Oertliche Zustaendigkeit: § 29a ZPO
- Streitwert: §§ 41, 48 GKG, § 3 ZPO
- Vollstreckbarkeit: §§ 708 ff. ZPO

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Audit-Hinweis

Audit durchgefuehrt am 27.05.2026. Drei halluzinierte Aktenzeichen im Abschnitt "Aktuelle Rechtsprechung" geprueft und korrigiert:
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `miet-gewerbemiete-vertragsklauseln-spezial`

**Fokus:** Spezialfall Gewerbemiete: Wertsicherungsklauseln, Konkurrenzschutz, Schriftform § 550 BGB, Doppelschriftformklausel. Pruefraster fuer Vermieter und Mieter.

# Miet: Gewerbemiete-Klauseln

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Miet: Gewerbemiete-Klauseln` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Miet: Gewerbemiete-Klauseln
- **Spezialgegenstand:** Miet: Gewerbemiete-Klauseln / miet gewerbemiete vertragsklauseln spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB.
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

## 3. `miet-mietvertrag-bauleiter`

**Fokus:** Bauleiter Wohnraum-Mietvertrag: Schoenheitsreparaturen, Kaution, Kuendigung, Mieterhoehung, Untervermietung. Pruefraster fuer Vermieter und Mieter.

# Miet: Mietvertrag Bauleiter

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Miet: Mietvertrag Bauleiter` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Miet: Mietvertrag Bauleiter
- **Spezialgegenstand:** Miet: Mietvertrag Bauleiter / miet mietvertrag bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BG.
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
