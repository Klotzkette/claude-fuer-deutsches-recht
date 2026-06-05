---
name: aktenauszug-strukturpruefung-akzg-bauleiter
description: "Strukturpruefung Akzg Bauleiter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Strukturpruefung Akzg Bauleiter

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Strukturpruefung Akzg Bauleiter** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aktenauszug-strukturpruefung` | Fertig erstellten Aktenauszug auf Vollständigkeit prüfen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprache. Normen §§ 128-134 253 ZPO. Prüfraster Bausteine-Vollständigkeit Fristen-Markierung Neutralitaets-Check Sprach-Qualitaet. Output Prüfergebnis-Bericht Lueckenliste Verbesserungshinweise. Abgrenzung zu aktenauszug-erstellen (Erstellung) und neutralitaetsprüfung (Wertungs-Check). |
| `akzg-aktenauszug-bauleiter` | Bauleiter Aktenauszug fuer Gerichtsverfahren: Sachverhalt, Streitstand, Beweisangebote, Schlussantraege. Pruefraster Vollstaendigkeit fuer Berufung und Revision. |
| `akzg-vertraulichkeit-redaction-spezial` | Spezialfall Vertraulichkeit und Redaction in Aktenauszuegen: Berufsgeheimnis, personenbezogene Daten, Konzerninterna. Pruefraster fuer Akteneinsicht durch Dritte. |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Strukturpruefung Akzg Bauleiter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aktenauszug-strukturpruefung`

**Fokus:** Fertig erstellten Aktenauszug auf Vollständigkeit prüfen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprache. Normen §§ 128-134 253 ZPO. Prüfraster Bausteine-Vollständigkeit Fristen-Markierung Neutralitaets-Check Sprach-Qualitaet. Output Prüfergebnis-Bericht Lueckenliste Verbesserungshinweise. Abgrenzung zu aktenauszug-erstellen (Erstellung) und neutralitaetsprüfung (Wertungs-Check).

# Aktenauszug — Strukturprüfung

## Zweck

Dieser Skill prüft einen erstellten Aktenauszug auf formale Vollständigkeit aller sechs Bausteine und auf die Einhaltung der Qualitätsgrundsätze (Fristen hervorgehoben, Sprache neutral). Er ist das abschließende Qualitätsgate vor der Übergabe an den Mandatsbearbeiter.

## Triage — Kläre vor der Prüfung

1. Für welche Verfahrensart wurde der Aktenauszug erstellt? (Zivil/Arbeit/Verwaltung/Sozial/Straf)
2. Ist der Aktenauszug als intern-anwaltlicher Vermerk oder als Übergabedokument konzipiert?
3. Steht ein konkreter Termin oder eine Frist bevor, die besonders zu prüfen ist?

## Zentrale Normen

- § 128 ZPO — Muendliche Verhandlung; § 128a ZPO — Ton-/Bildübertragung
- § 139 ZPO — Materielle Prozessleitung (Hinweispflicht des Gerichts)
- § 253 ZPO — Inhalt der Klageschrift (Mindestinhalt als Vergleichsmassstab)
- § 495a ZPO — Vereinfachtes Verfahren unter 600 EUR
- §§ 355-414 ZPO — Beweisaufnahme (Zeugenbeweis, Sachverständigenbeweis, Augenschein)

## Rechtsprechung zu Vollstaendigkeit und Ordnung der Akte

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfcheckliste

### Baustein 1 — Verfahrensidentifikation

- [ ] Gericht und Kammer angegeben
- [ ] Aktenzeichen angegeben
- [ ] Instanz und Verfahrensart angegeben
- [ ] Streitwert angegeben (oder als unbekannt markiert)
- [ ] Alle Parteien mit Prozessbevollmächtigten aufgeführt

### Baustein 2 — Einleitungssatz

- [ ] Ein bis zwei Sätze vorhanden
- [ ] Wer streitet mit wem worüber benannt
- [ ] Hauptnorm genannt
- [ ] Keine Wertung enthalten

### Baustein 3 — Zusammenfassung

- [ ] Acht bis zehn Sätze vorhanden
- [ ] Hintergrund dargestellt
- [ ] Aktueller Verfahrensstand benannt
- [ ] Nächste Verfahrenshandlung benannt
- [ ] Keine Wertung / Prognose enthalten

### Baustein 4 — Sachverhaltschronologie

- [ ] Chronologisch sortiert
- [ ] Datum fettgedruckt vorangestellt
- [ ] Wesentliche außerprozessuale Ereignisse vollständig
- [ ] Fundstellen angegeben
- [ ] Keine prozessualen Schritte enthalten

### Baustein 5 — Verfahrenschronologie

- [ ] Chronologisch sortiert
- [ ] Alle prozessualen Schritte erfasst
- [ ] Fristen hervorgehoben (Präfix ⚠️ FRIST)
- [ ] Fristentabelle vorhanden
- [ ] Keine außerprozessualen Ereignisse enthalten

### Baustein 6 — Tabellen

**Parteivortrag:**
- [ ] Tabelle mit zwei Spalten (Kläger / Beklagter)
- [ ] Alle wesentlichen Streitpunkte als Zeilen
- [ ] Fundstellen angegeben

**Beweismittel:**
- [ ] Alle angebotenen Beweismittel erfasst
- [ ] Beweisthema je Beweismittel angegeben
- [ ] Anlagenbezeichnung angegeben

**Rechtsargumente:**
- [ ] Anspruchsgrundlagen beider Seiten erfasst
- [ ] Einwendungen und Einreden erfasst
- [ ] Verjährungsthema behandelt (falls relevant) — §§ 195-218 BGB
- [ ] Rechtsprechung mit Aktenzeichen angegeben

## Qualitätsgrundsätze

- [ ] Neutralitätsprüfung bestanden (keine Wertungen, keine Prognosen)
- [ ] Keine verbotenen Begriffe (keine KI-Terminologie)
- [ ] Fristen an prominenter Stelle (Fristenbox oder Fristentabelle am Anfang)
- [ ] Klare Markdown-Gliederung mit Überschriften

## Ergebnis-Format

```markdown
## Strukturprüfung — Ergebnis

| Baustein | Status | Anmerkung |
|---|---|---|
| Verfahrensidentifikation | vollstaendig | — |
| Einleitungssatz | vollstaendig | — |
| Zusammenfassung | unvollstaendig | Nächste Verfahrenshandlung fehlt |
| Sachverhaltschronologie | vollstaendig | — |
| Verfahrenschronologie | vollstaendig | — |
| Parteivortrag-Tabelle | vollstaendig | — |
| Beweismittel-Tabelle | unvollstaendig | B-Anlagen nicht erfasst |
| Rechtsargumente-Tabelle | vollstaendig | — |

**Gesamtergebnis:** ÜBERARBEITUNG ERFORDERLICH
**Offene Punkte:** [Anzahl]
```

## Adressat und Tonfall

Adressat: Sachbearbeiter / Kanzleiintern — Tonfall: sachlich-juristisch, präzise Mängelangabe.

## 2. `akzg-aktenauszug-bauleiter`

**Fokus:** Bauleiter Aktenauszug fuer Gerichtsverfahren: Sachverhalt, Streitstand, Beweisangebote, Schlussantraege. Pruefraster Vollstaendigkeit fuer Berufung und Revision.

# AkzG: Aktenauszug Bauleiter

## Spezialwissen: AkzG: Aktenauszug Bauleiter
- **Spezialgegenstand:** AkzG: Aktenauszug Bauleiter / akzg aktenauszug bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AkzG.
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

## 3. `akzg-vertraulichkeit-redaction-spezial`

**Fokus:** Spezialfall Vertraulichkeit und Redaction in Aktenauszuegen: Berufsgeheimnis, personenbezogene Daten, Konzerninterna. Pruefraster fuer Akteneinsicht durch Dritte.

# AkzG: Vertraulichkeit Redaction

## Spezialwissen: AkzG: Vertraulichkeit Redaction
- **Spezialgegenstand:** AkzG: Vertraulichkeit Redaction / akzg vertraulichkeit redaction spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AkzG.
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
