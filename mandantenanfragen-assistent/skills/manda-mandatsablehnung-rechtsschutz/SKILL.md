---
name: manda-mandatsablehnung-rechtsschutz
description: "Manda Mandatsablehnung Rechtsschutz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Manda Mandatsablehnung Rechtsschutz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Manda Mandatsablehnung Rechtsschutz** im Plugin Mandantenanfragen-Assistent. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `manda-mandatsablehnung-coi-spezial` | Spezialfall Mandatsablehnung und COI-Kommunikation: berufsrechtliche Hinweise § 43a BRAO, Schweigepflicht, Ablehnungsschreiben ohne offene Konflikte. Pruefraster fuer Risk-and-Compliance. |
| `manda-rechtsschutz-eintrittsanfrage-spezial` | Spezialfall Rechtsschutzversicherung-Eintrittsanfrage: Deckungsanfrage, Stichentscheid, Mustertext fuer Auseinandersetzung mit Rechtsschutzversicherer. Pruefraster Mandant und Anwalt. |
| `mandatsverhaeltnis-hinweis` | Antwortmail muss klar machen dass noch kein Mandatsverhältnis besteht und keine Rechtsberatung erfolgt. § 43 BRAO Haftungsabgrenzung Erstanfrage. Prüfraster: Beantwortung der Anfrage = keine Rechtsberatung kein Mandatsverhältnis kein Pflichten-Begründung. Kurz- und Langform für Antwortmail und Fusszeile. Output: Disclaimer-Texte für E-Mail. Abgrenzung zu vertraulichkeit-erinnerung (Schweigepflicht) und erstantwort-generator. |

## Arbeitsweg

Im Plugin Mandantenanfragen-Assistent gilt für **Manda Mandatsablehnung Rechtsschutz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `manda-mandatsablehnung-coi-spezial`

**Fokus:** Spezialfall Mandatsablehnung und COI-Kommunikation: berufsrechtliche Hinweise § 43a BRAO, Schweigepflicht, Ablehnungsschreiben ohne offene Konflikte. Pruefraster fuer Risk-and-Compliance.

# Manda: Mandatsablehnung COI

## Spezialwissen: Manda: Mandatsablehnung COI
- **Spezialgegenstand:** Manda: Mandatsablehnung COI / manda mandatsablehnung coi spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** COI, BRAO.
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

## 2. `manda-rechtsschutz-eintrittsanfrage-spezial`

**Fokus:** Spezialfall Rechtsschutzversicherung-Eintrittsanfrage: Deckungsanfrage, Stichentscheid, Mustertext fuer Auseinandersetzung mit Rechtsschutzversicherer. Pruefraster Mandant und Anwalt.

# Manda: RS-Eintrittsanfrage

## Spezialwissen: Manda: RS-Eintrittsanfrage
- **Spezialgegenstand:** Manda: RS-Eintrittsanfrage / manda rechtsschutz eintrittsanfrage spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** RS.
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

## 3. `mandatsverhaeltnis-hinweis`

**Fokus:** Antwortmail muss klar machen dass noch kein Mandatsverhältnis besteht und keine Rechtsberatung erfolgt. § 43 BRAO Haftungsabgrenzung Erstanfrage. Prüfraster: Beantwortung der Anfrage = keine Rechtsberatung kein Mandatsverhältnis kein Pflichten-Begründung. Kurz- und Langform für Antwortmail und Fusszeile. Output: Disclaimer-Texte für E-Mail. Abgrenzung zu vertraulichkeit-erinnerung (Schweigepflicht) und erstantwort-generator.

# Mandatsverhältnis-Hinweis

Dieser Skill formuliert den rechtlich erforderlichen Hinweis, dass mit der Beantwortung einer Erstanfrage noch kein Mandatsverhältnis begründet wird und die Antwort keine Rechtsberatung darstellt.


## Triage zu Beginn
1. Enthaelt die Erstantwort inhaltliche rechtliche Hinweise, die als konkludente Rechtsberatung ausgelegt werden koennten?
2. Soll die Kurz- oder die Langform des Disclaimers verwendet werden?
3. Ist der Mandant Verbraucher (§ 13 BGB) — dann auch Widerrufsrecht und Fernkommunikationspflichten beachten?
4. Muss zusaetzlich auf die Kostenpflicht hingewiesen werden (§ 49b Abs. 5 BRAO)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 611, 675 BGB — Anwaltsvertrag: kommt durch Angebot und Annahme zustande; konkludente Entstehung moeglich
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: Hinweis auf voraussichtliche Kosten vor Mandatsannahme
- § 13 BGB — Verbraucher: erhoehtere Informationspflichten und Widerrufsrecht (§§ 355 ff. BGB) bei Fernkommunikation
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch gegenueber potenziellem Mandanten, der noch kein Mandat erteilt hat

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Rechtlicher Hintergrund

### Entstehung des Mandatsverhältnisses

Ein Anwaltsvertrag (Mandatsverhältnis) kommt durch Angebot und Annahme zustande (§§ 611 ff., 675 BGB). Die bloße Beantwortung einer eingehenden Anfrage — selbst wenn inhaltliche Einschätzungen gegeben werden — begründet noch kein Mandat, sofern kein ausdrückliches Angebot zur Mandatsübernahme unterbreitet und angenommen wurde.

### Bedeutung für die Kanzlei

Ohne Mandat:
- Keine Honorar-Ansprüche nach RVG
- Aber auch: keine vollumfängliche Berater-Haftung nach § 280 BGB (Schlechterfüllung des Anwaltsvertrags)
- Keine Verschwiegenheitspflicht nach § 43a Abs. 2 BRAO gegenüber dem konkreten Anliegen (wohl aber allgemeine Diskretion)
- Kein Zurückbehaltungsrecht an Unterlagen
- Kein Konfliktcheck-Erfordernis schon wirksam — aber: Kanzlei sollte vorab prüfen (vgl. Skill `konfliktcheck-vorab`)

### Haftungsrisiko ohne klaren Disclaimer

Wenn die Erstantwort inhaltliche Rechtshinweise enthält (z. B. "Ihre Kündigung dürfte unwirksam sein"), kann dies unter Umständen eine konkludente Rechtsberatung darstellen, für die Haftpflichtansprüche entstehen können. Der Disclaimer schützt die Kanzlei.

## Kurzform (für den Fließtext der Erstantwort)

```
Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis
begründet und keine Rechtsberatung darstellt.
```

## Mittlere Form (für den Abschluss der Erstantwort)

```
Hinweis: Diese Nachricht ist eine Eingangsbestätigung Ihrer Anfrage.
Sie begründet kein Mandatsverhältnis zwischen Ihnen und [KANZLEI-NAME].
Die Beantwortung dieser Anfrage stellt keine Rechtsberatung dar und
begründet keinerlei Pflichten der Kanzlei. Erst nach ausdrücklicher
schriftlicher Mandatserteilung und Annahme durch [KANZLEI-NAME] entsteht
ein Anwalts-Mandantenverhältnis.
```

## Langform (für die Fußzeile oder auf Anfrage)

```
RECHTLICHER HINWEIS

Es besteht noch kein Mandatsverhältnis. Die Beantwortung dieser Anfrage
stellt keine Rechtsberatung dar und begründet keine Pflichten der Kanzlei.

Ein Anwalts-Mandantenverhältnis kommt erst durch ausdrückliche
schriftliche Mandatserteilung seitens der anfragenden Person und deren
ausdrückliche Annahme durch [KANZLEI-NAME] zustande.

Bis zur Mandatserteilung übernimmt [KANZLEI-NAME] keine Haftung für
Maßnahmen oder Unterlassungen, die auf der Grundlage dieser
Eingangsbestätigung getroffen werden.

Bitte beachten Sie insbesondere: Falls Ihnen Fristen drohen, handeln Sie
nicht allein auf Basis dieser Nachricht — wenden Sie sich umgehend an
einen Rechtsanwalt Ihres Vertrauens oder rufen Sie uns unter
[SEKRETARIATS-TELEFON] an.
```

## Verwendung nach Kontext

| Kontext | Form | Platzierung |
|---|---|---|
| Standard-Erstantwort | Kurzform | Im Fließtext, erster oder letzter Absatz |
| Erstantwort mit Transkription | Mittlere Form | Vor dem Transkriptions-Abschnitt |
| Dringende Anfrage | Langform | Prominenter Hinweis; Fußzeile + Fließtext |
| Spam / Abgelehnte Anfrage | Nicht erforderlich | Entfällt |

## Zusammenspiel mit anderen Hinweisen

- **Vertraulichkeit:** Der Hinweis auf die anwaltliche Schweigepflicht (§ 43a Abs. 2 BRAO) erfolgt erst nach Mandatsbegründung — Skill `vertraulichkeit-erinnerung`.
- **Dringlichkeit:** Bei HOCH-Dringlichkeit wird die Langform mit ausdrücklichem Frist-Hinweis verwendet.
- **Keine inhaltliche Rechtsberatung in der Erstantwort:** Die Erstantwort enthält keine Einschätzung der Rechtslage. Falls versehentlich inhaltliche Aussagen in der Anfrage enthalten sind, werden diese nicht bewertet — nur die organisatorischen nächsten Schritte werden beschrieben.

## Verweise auf andere Skills

- `erstantwort-generator` — setzt Kurzform / Mittlere Form ein
- `vertraulichkeit-erinnerung` — weiterführender Hinweis nach Mandatsbegründung
- `transkriptionsdienst-erklaerung` — verwendet diesen Hinweis im Transkriptions-Abschnitt
- `dringlichkeitsmarker` — bei HOCH: Langform mit Frist-Warnung
