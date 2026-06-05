---
name: erfinderische-taetigkeit-freedom-to-ki-patent
description: "Erfinderische Taetigkeit Freedom TO KI Patent: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Erfinderische Taetigkeit Freedom TO KI Patent

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Erfinderische Taetigkeit Freedom TO KI Patent** im Plugin Patentrecherche (FTO, Validity). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `erfinderische-taetigkeit-pruefen` | Prüft erfinderische Tätigkeit nach § 4 PatG und Art. 56 EPUe mit dem Problem-Solution-Approach der EPA-Beschwerdekammern. Drei Stufen: (1) Bestimmung des naechstliegenden Stands der Technik (closest prior art) anhand technischer Naehe Zweckverwandschaft und gemeinsamer Merkmale; (2) Formulierung der objektiven technischen Aufgabe (objective technical problem) als das was die Erfindung löst und der naechstliegende Stand der Technik nicht; (3) Frage nach could-would am Tag der Anmeldung haette der Fachmann ausgehend vom naechstliegenden Stand der Technik mit Erwartung auf Erfolg die beanspruchte Lösung umgesetzt. Berücksichtigt Sekundaerindizien wie technisches Vorurteil unerwartete Wirkung lange empfundenes Bedürfnis und kommerziellen Erfolg. Disclaimer keine amtliche Prüfung. |
| `freedom-to-operate-recherche` | Freedom-to-Operate-Recherche (FTO) vor Markteintritt eines konkreten Produkts oder Verfahrens der Mandantin. Sucht **in Kraft befindliche** Patente und Gebrauchsmuster Dritter im Zielmarkt deren Schutzbereich nach § 14 PatG Art. 69 EPUe das Produkt erreichen koennte. Anders als Stand-der-Technik-Recherche: Filter auf erteilte und rechtsstandfähige Schutzrechte (DPMAregister EPO Register Status erteilt nicht erloschen), Territorium passt zum Zielmarkt, Schutzbereich passt zum Produkt. Liefert Risiko-Ampel pro Treffer rot gelb gruen mit Begründung Pinpoint auf Hauptanspruch und Empfehlung Vermeidung Lizenz Vernichtungsklage Nichtigkeitsklage. Disclaimer keine Rechtsberatung kein Ersatz für Patentanwaltsbewertung. |
| `ki-und-patent-strategie` | Spezialfall KI-Erfindungen Patent-Strategie: DABUS-Entscheidungen DPMA und EPA und BPatG, Erfinderbenennung nur natuerliche Person, Beitrag der KI in Beschreibung, Daten- und Modellrechte. Strategie fuer KI-getriebene FuE und Patent-Portfolio. Mustertexte. |

## Arbeitsweg

Im Plugin Patentrecherche (FTO, Validity) gilt für **Erfinderische Taetigkeit Freedom TO KI Patent**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `erfinderische-taetigkeit-pruefen`

**Fokus:** Prüft erfinderische Tätigkeit nach § 4 PatG und Art. 56 EPUe mit dem Problem-Solution-Approach der EPA-Beschwerdekammern. Drei Stufen: (1) Bestimmung des naechstliegenden Stands der Technik (closest prior art) anhand technischer Naehe Zweckverwandschaft und gemeinsamer Merkmale; (2) Formulierung der objektiven technischen Aufgabe (objective technical problem) als das was die Erfindung löst und der naechstliegende Stand der Technik nicht; (3) Frage nach could-would am Tag der Anmeldung haette der Fachmann ausgehend vom naechstliegenden Stand der Technik mit Erwartung auf Erfolg die beanspruchte Lösung umgesetzt. Berücksichtigt Sekundaerindizien wie technisches Vorurteil unerwartete Wirkung lange empfundenes Bedürfnis und kommerziellen Erfolg. Disclaimer keine amtliche Prüfung.

# erfinderische-tätigkeit-prüfen

## Zweck

Prüft, ob ein Anspruch — typischerweise nachdem die Neuheit bejaht wurde — auf einer **erfinderischen Tätigkeit** beruht. Im EPA-Sprachgebrauch ist die erfinderische Tätigkeit der zentrale Knackpunkt der Patentprüfung.

## Rechtsrahmen

- **§ 4 PatG.** Eine Erfindung gilt als auf einer erfinderischen Tätigkeit beruhend, wenn sie sich für den Fachmann nicht in naheliegender Weise aus dem Stand der Technik ergibt.
- **Art. 56 EPÜ.** Wortgleich für das EPA.
- **Geheime ältere Anmeldungen** (§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPÜ) sind **nicht** für die erfinderische Tätigkeit relevant — sondern nur für die Neuheit.
- **EPA-Methodik:** **Problem-Solution-Approach** (PSA). Bindend für die EPA-Prüfung und EPA-Beschwerdekammer-Rechtsprechung; in der DPMA- und BPatG-Praxis ebenfalls maßgeblich, wenn auch nicht so dogmatisch.

## Problem-Solution-Approach in drei Stufen

### Stufe 1: Nächstliegender Stand der Technik (closest prior art)

Aus den Recherche-Treffern wird **eine** Entgegenhaltung als nächstliegender Stand der Technik bestimmt. Kriterien:

- **Gleicher Zweck / gleiches technisches Gebiet** wie die Erfindung.
- **Hohe Übereinstimmung** in den Merkmalen (möglichst viele M1, M2, … sind offenbart).
- **Klare technische Lehre**, von der ausgehend der Fachmann an die Erfindung herangehen könnte.

Wenn mehrere Entgegenhaltungen in Frage kommen: zur Plausibilitätskontrolle den PSA **für jede** durchgehen — wenn ausgehend von **einer** der Anspruch naheliegend ist, fehlt die erfinderische Tätigkeit (EPA-Praxis: T 967/97, T 21/08).

### Stufe 2: Objektive technische Aufgabe

Differenz zwischen Anspruch und nächstliegendem Stand der Technik bilden — die **unterscheidenden Merkmale**. Aus diesen unterscheidenden Merkmalen wird die **technische Wirkung** abgeleitet und als "**objektive technische Aufgabe**" formuliert:

> Wie kann der nächstliegende Stand der Technik so weiterentwickelt werden, dass [technische Wirkung]?

Wichtig: Die Aufgabe wird **objektiv aus der Erfindung heraus** formuliert — nicht aus der Mandanten-Erzählung. Wenn die Mandantin ein Problem nennt, das der nächstliegende Stand der Technik schon löst, ist es nicht die objektive Aufgabe. **Verbot der rückschauenden Betrachtung** (ex-post-facto-Argumentation, T 24/81).

### Stufe 3: Could-Would-Frage

Hätte der **Fachmann** am Anmeldetag / Prioritätstag — **ausgehend vom nächstliegenden Stand der Technik** — die objektive Aufgabe so gelöst, wie der Anspruch sie löst?

Nicht: **könnte** (could). Sondern: **würde** (would). Der Fachmann muss eine **Motivation** gehabt haben, die anderen Entgegenhaltungen heranzuziehen, mit **Erwartung auf Erfolg**.

Die Frage hat zwei Teilaspekte:

1. **Steht es im Stand der Technik?** Gibt es eine andere Entgegenhaltung, die das fehlende Merkmal lehrt?
2. **Hätte der Fachmann zugegriffen?** Gibt es eine Anregung ("pointer", "teaching", "suggestion") in der Entgegenhaltung oder im allgemeinen Fachwissen, die den Fachmann von Entgegenhaltung A zu Entgegenhaltung B führt?

## Ablauf

### 1. Recherche-Treffer aus `stand-der-technik-recherche` einlesen

Mit Recherchezeichen (X, Y, A, P, E). Y-Treffer sind die wichtigsten für die erfinderische Tätigkeit.

### 2. Closest Prior Art bestimmen

Begründete Auswahl mit Erklärung, warum dieser Treffer am nächsten liegt (technisches Gebiet, gemeinsame Merkmale).

### 3. Merkmals-Differenz bilden

Tabelle der unterscheidenden Merkmale gegenüber dem Closest-Prior-Art-Dokument. Beispiel:

| Merkmal | im CPA offenbart? | Unterscheidend? |
| --- | --- | --- |
| M1 — Energieversorgungsnetz | ja | nein |
| M2 — Steuergerät | ja | nein |
| M3 — Speicher für Lastdaten | ja | nein |
| M4 — Soll-Lastpfad über Prognosemodell | ja (linear) | teilweise |
| M5 — Eingriff bei Abweichung | ja | nein |
| M6 — Neuronales Netz mit drei Schichten | **nein** | **ja** |

### 4. Technische Wirkung der unterscheidenden Merkmale

"Was bringt M6?" — z. B.: bessere Vorhersagegenauigkeit bei nicht-linearen Lastprofilen, robuster gegenüber Lastspitzen, Stabilität ohne manuelle Parameter-Tuning.

### 5. Objektive technische Aufgabe formulieren

> Wie kann das Lastmanagement-System aus EP 3 456 789 A1 so weiterentwickelt werden, dass bei nicht-linearen Lastprofilen eine genauere Prognose erzeugt wird?

### 6. Could-Would-Prüfung

Recherche-Treffer durchgehen — gibt es eine Entgegenhaltung, die neuronale Netze für Lastprognose lehrt? Wenn ja:

- **Stand der Technik:** ja, z. B. WO 2017/123 — neuronale Netze für Energieprognose.
- **Motivation:** Stand der Technik nennt explizit, dass neuronale Netze bei nicht-linearen Lastprofilen genauer sind als lineare Modelle.
- **Erwartung auf Erfolg:** ja, weil der Stand der Technik die Anwendung in vergleichbaren Energienetzen schon zeigt.

→ **Ergebnis:** Der Fachmann hätte ausgehend von EP 3 456 789 A1 mit Anregung aus WO 2017/123 mit Erwartung auf Erfolg den Weg von Anspruch 1 beschritten. **Erfinderische Tätigkeit fraglich**, Anspruch sollte engerer gefasst werden (z. B. Spezifikum des Trainingsverfahrens, Kombination mit weiteren Merkmalen).

Oder, wenn keine Anregung besteht: **Erfinderische Tätigkeit liegt vor.**

## Sekundärindizien

Wenn die Could-Would-Prüfung nahelegend ausfällt, aber dennoch Zweifel bestehen — Sekundärindizien einsetzen (EPA-Beschwerdekammern: Vorsicht, Sekundärindizien dürfen die Hauptprüfung nicht ersetzen, T 1212/01):

- **Technisches Vorurteil** überwunden — die Fachwelt hat eine bestimmte Lösung jahrelang abgelehnt.
- **Unerwartete technische Wirkung** — die Erfindung bringt ein Mehr, das der Stand der Technik nicht erwarten ließ (T 21/81).
- **Lang empfundenes Bedürfnis** — das Problem ist seit Jahren bekannt, aber unbehoben.
- **Kommerzieller Erfolg** — schwach, aber zulässig, wenn er auf den technischen Merkmalen beruht (T 270/84).
- **Scheitern anderer** — frühere Anmeldungen oder Veröffentlichungen, die das Problem nicht lösen konnten.

## Hinweise

- **EPA-Standardphrase:** "Could-would-approach." Im DPMA-/BPatG-Verfahren weniger formelhaft, aber inhaltlich gleich.
- **Mehrfach-PSA.** Wenn mehrere CPA-Kandidaten denkbar: PSA für jeden, schwächste Position für die Mandantin maßgeblich.
- **Mosaike** sind hier — anders als bei der Neuheit — **zulässig**, aber nur, wenn der Fachmann eine Verbindung gezogen hätte (Pointer aus CPA, allgemeines Fachwissen).
- **Hindsight-Verbot.** Die Argumentation darf nicht auf die Mandanten-Anmeldung zurückblicken ("wenn man weiß, wie es geht, ist es immer leicht").
- **Fachmann ist Konstrukt** — die für das technische Gebiet zuständige Fachperson mit durchschnittlichen Kenntnissen und Zugang zum gesamten Stand der Technik. Bei interdisziplinären Erfindungen: **Fachteam** (T 32/81).

## Disclaimer

> **Hinweis zur Prüfung.** Diese Prüfung der erfinderischen Tätigkeit ist eine KI-gestützte Vorprüfung und keine amtliche Prüfung durch DPMA oder EPA. Der Problem-Solution-Approach ist methodisch sensibel — die Auswahl des nächstliegenden Stands der Technik kann die Bewertung entscheidend verschieben. Die Prüfung muss durch eigene Bewertung und durch Prüfung der Recherche-Vollständigkeit abgesichert werden.

## Triage-Fragen vor Pruefung erfinderischer Taetigkeit

Bevor der Problem-Solution-Approach angewendet wird, klaere:
1. Welche Entgegenhaltung ist der naechstliegende Stand der Technik (CPA — Closest Prior Art)?
2. Welches technische Problem loest die Erfindung ausgehend vom CPA?
3. Sind Sekundaerindizien vorhanden (unerwarteter technischer Effekt, ueberwundenes technisches Vorurteil, lang empfundenes Beduerfnis)?
4. Sind alle Merkmale des Hauptanspruchs in der PSA beruecksichtigt?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Technische Beschwerdekammer, T 21/81 (Unerwarteter technischer Effekt):** Ein unerwarteter technischer Effekt, der ueber das aus dem Stand der Technik Vorhersehbare hinausgeht, ist ein Indiz fuer erfinderische Taetigkeit; er muss im Anspruch oder in der Beschreibung hinreichend offenbart sein.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `freedom-to-operate-recherche`

**Fokus:** Freedom-to-Operate-Recherche (FTO) vor Markteintritt eines konkreten Produkts oder Verfahrens der Mandantin. Sucht **in Kraft befindliche** Patente und Gebrauchsmuster Dritter im Zielmarkt deren Schutzbereich nach § 14 PatG Art. 69 EPUe das Produkt erreichen koennte. Anders als Stand-der-Technik-Recherche: Filter auf erteilte und rechtsstandfähige Schutzrechte (DPMAregister EPO Register Status erteilt nicht erloschen), Territorium passt zum Zielmarkt, Schutzbereich passt zum Produkt. Liefert Risiko-Ampel pro Treffer rot gelb gruen mit Begründung Pinpoint auf Hauptanspruch und Empfehlung Vermeidung Lizenz Vernichtungsklage Nichtigkeitsklage. Disclaimer keine Rechtsberatung kein Ersatz für Patentanwaltsbewertung.

# freedom-to-operate-recherche

## Zweck

Bevor die Mandantin ein Produkt auf den Markt bringt oder ein Verfahren einführt, muss geprüft werden, ob **fremde Patente** den Markteintritt blockieren könnten. Anders als bei der Stand-der-Technik-Recherche geht es nicht um Patentierbarkeit, sondern um **Verletzungsrisiko**.

## Abgrenzung

- **Stand-der-Technik-Recherche** — alle Veröffentlichungen, weltweit, in jeder Sprache, **auch wenn das Patent abgelaufen ist**. Zweck: Patentierbarkeit der eigenen Anmeldung.
- **FTO-Recherche** — nur **in Kraft befindliche** Schutzrechte, **im Zielmarkt**. Zweck: Vermeidung von Patentverletzung.

## Rechtsrahmen

- **§ 9 PatG / Art. 64 EPÜ.** Wirkung des Patents — Verbietungsrecht gegenüber Dritten.
- **§ 14 PatG / Art. 69 EPÜ.** Schutzbereich — bestimmt sich nach dem Inhalt der Patentansprüche, Beschreibung und Zeichnungen als Auslegungshilfe.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 24 PatG.** Zwangslizenz (in der Praxis selten relevant).
- **GebrMG.** Gebrauchsmuster (max. 10 Jahre Schutzdauer, ungeprüft eingetragen) — ist parallel zu prüfen.

## Eingaben

- **Produkt / Verfahren** der Mandantin in technischer Beschreibung — Komponenten, Funktionen, Schlüsselmerkmale.
- **Zielmarkt** — welche Staaten? (Deutschland, EU-weit, USA, Japan, China, alle G20-Staaten).
- **Markteintritts-Zeitpunkt** — Stichtag (heute / geplanter Tag).

## Ablauf

### Schritt 1: Produkt-Merkmal-Tabelle

Wie bei `klassifikation-cpc-ipc`: Produkt in technische Merkmale zerlegen. Pro Merkmal: was es **tut**, wie es **gebaut** ist, welche **Komponenten** verwendet werden, welche **Materialien**.

### Schritt 2: Klassen bestimmen

Über `klassifikation-cpc-ipc` die relevanten CPC- und IPC-Klassen identifizieren.

### Schritt 3: Datenbankrecherche mit FTO-Filtern

Über `agentische-datenbank-recherche`, aber mit folgenden zusätzlichen Filtern:

- **Status:** "granted" / "in force" / "erteilt, nicht erloschen". Anmeldungen können relevant sein (zukünftige Erteilung), werden aber gesondert markiert.
- **Territorium:** Treffer für jeden Ziel-Staat einzeln prüfen. Ein US-Patent blockiert nicht den DE-Markt. EP-Patente nur in den Validierungsstaaten — also nach Validierung in DE, FR, GB usw. einzeln prüfen.
- **Schutzdauer:** Anmeldetag plus 20 Jahre (§ 16 PatG). Treffer mit Anmeldetag > 20 Jahre sind irrelevant (außer Schutzzertifikat nach SPC für Arzneimittel oder Pflanzenschutzmittel, dann +5 Jahre).

### Schritt 4: Schutzbereich prüfen

Für jeden in Kraft befindlichen Treffer:

1. **Hauptanspruch lesen** — wortlautidentische Auslegung des Schutzbereichs nach § 14 PatG / Art. 69 EPÜ.
2. **Beschreibung und Zeichnungen** als Auslegungshilfe heranziehen (§ 14 S. 2 PatG / Protokoll zu Art. 69 EPÜ).
3. **Merkmale des Hauptanspruchs** gegen das Produkt der Mandantin prüfen — wortlautidentische Verletzung? Äquivalente Verletzung (BGH, Schneidmesser)?
4. **Rechtsstand** prüfen: ist das Patent noch in Kraft, sind Jahresgebühren bezahlt, läuft ein Einspruchs- oder Nichtigkeitsverfahren? → über `rechtsstand-pruefen`.

### Schritt 5: Risiko-Ampel

Pro Treffer eine Bewertung:

- **Rot.** Verletzungsrisiko hoch — der Hauptanspruch deckt sich wortlautidentisch oder äquivalent mit dem Produkt der Mandantin. **Markteintritt ohne Lizenz, Umgehungsdesign oder Nichtigkeitsklage gefährlich.**
- **Gelb.** Verletzungsrisiko mittel — Hauptanspruch nimmt teilweise auf das Produkt zu, aber Auslegungsspielraum besteht, oder das Produkt unterscheidet sich in einem zentralen Merkmal. **Patentanwaltsbewertung im Einzelfall erforderlich.**
- **Grün.** Verletzungsrisiko gering — Hauptanspruch deckt das Produkt offensichtlich nicht. Treffer dient nur der Dokumentation.

Pro Treffer Pinpoint auf den verletzungsrelevanten Anspruch + ein bis zwei Sätze Begründung.

### Schritt 6: Empfehlung

Bei **Rot-** oder **Gelb-Treffern**:

- **Vermeidung / Umgehungsdesign** — Produkt so umgestalten, dass ein Anspruchsmerkmal nicht mehr erfüllt ist.
- **Lizenz** — Anfrage an den Patentinhaber.
- **Nichtigkeitsklage / Einspruch** — wenn der Treffer angreifbar erscheint (in EPA-Einspruchsfrist: Art. 99 EPÜ, neun Monate ab Erteilungs-Veröffentlichung; danach: Nichtigkeitsklage zum BPatG, § 81 PatG).
- **Negative Feststellungsklage** — § 256 ZPO, Feststellung der Nichtverletzung.

### Schritt 7: Output

- **Treffertabelle** mit Spalten: Veröff.-Nr., Anmelder, Anmeldetag, Schutzdauer-Ende, Validierungsstaaten, Status, Hauptanspruch-Pinpoint, Risiko-Ampel, Begründung, Empfehlung, Link.
- **Zusammenfassung** je Zielmarkt: Anzahl Rot / Gelb / Grün, kritische Treffer hervorgehoben.
- **Disclaimer** (siehe unten).

## Hinweise

- **Schutzbereich ist Auslegungsfrage.** Die hier gezeigte Bewertung ist **strikt vorläufig** — die endgültige Auslegung erfolgt im Einzelfall durch die Patentanwältin / im Streitfall durch das Gericht.
- **Äquivalenzlehre** (BGH Schneidmesser, Okklusionsvorrichtung) — Patente erfassen auch Lösungen, die ein Anspruchsmerkmal **gleichwirkend, naheliegend und gleichwertig** ersetzen. Bei der Ampel im Zweifel **gelb** statt grün.
- **Patentfamilien.** Ein DE-Patent ist oft Teil einer EP-/US-/JP-Familie — über `patentfamilien-analyse` alle Familienmitglieder prüfen, weil im Zielmarkt nicht immer das DE-Mitglied steht.
- **Anmeldungen vs. Patente.** Eine Anmeldung gibt noch keinen Verbietungsanspruch. Aber: spätere Erteilung möglich, **§ 33 PatG** gewährt nach Veröffentlichung der Anmeldung Schadensersatzanspruch ab Anspruchsstellung (Entschädigungsanspruch).
- **SPC** (Supplementary Protection Certificate, Arzneimittel/PSM) — Schutzdauer-Verlängerung bis 5 Jahre über § 16a PatG / VO (EG) 469/2009 / VO (EG) 1610/96. Bei pharmazeutischen Mandaten zwingend mitprüfen.
- **Gebrauchsmuster** parallel zum Patent recherchieren — DPMAregister-Suche umfasst Gebrauchsmuster.

## Disclaimer

> **Hinweis zur FTO-Recherche.** Diese Freedom-to-Operate-Recherche ist eine KI-gestützte Vorrecherche und keine Rechtsberatung. Die Risiko-Ampel ist eine vorläufige Einschätzung — der Schutzbereich nach § 14 PatG / Art. 69 EPUe ist Auslegungsfrage, die nur durch die Patentanwältin im konkreten Fall verbindlich beurteilt werden kann. Treffer in nicht durchsuchten Sprachen, außerhalb der Klassen oder in nicht erfassten Datenbanken bleiben möglich. Die Recherche muss durch eigene Bewertung und gegebenenfalls durch eine zweite Patentanwaltsbewertung abgesichert werden.

## Triage-Fragen vor FTO-Recherche

Bevor die FTO-Analyse begonnen wird, klaere:
1. Welche Zielmärkte/Validierungsstaaten sind relevant (DE, EP, US, CN)?
2. Ist die eigene Produktbeschreibung hinreichend konkret fuer den Claim-Vergleich?
3. Werden Gebrauchsmuster (§ 1 GebrMG) und SPC (VO EG 469/2009) in der Analyse beruecksichtigt?
4. Sind laufende Anmeldungen (noch nicht erteilt) in den Datenbanken identifiziert (§ 33 PatG-Risiko)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `ki-und-patent-strategie`

**Fokus:** Spezialfall KI-Erfindungen Patent-Strategie: DABUS-Entscheidungen DPMA und EPA und BPatG, Erfinderbenennung nur natuerliche Person, Beitrag der KI in Beschreibung, Daten- und Modellrechte. Strategie fuer KI-getriebene FuE und Patent-Portfolio. Mustertexte.

# KI-Erfindungen: Strategie

## Spezialwissen: KI-Erfindungen: Strategie
- **Spezialgegenstand:** KI-Erfindungen: Strategie / ki und patent strategie. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, DABUS, DPMA, EPA, BPatG.
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
