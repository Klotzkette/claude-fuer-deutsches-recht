---
name: persoenlichen-angriff-sachlichkeitsgebot
description: "Persoenlichen Angriff Sachlichkeitsgebot: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Persoenlichen Angriff Sachlichkeitsgebot

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Persoenlichen Angriff Sachlichkeitsgebot** im Plugin Email Umformulierer Berufsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `persoenlichen-angriff-entschaerfen` | Persoenliche Angriffe und Beleidigungen in Anwaltskorrespondenz erkennen und durch sachliche Formulierungen ersetzen. § 43a BRAO § 26 BORA Sachlichkeitsgebot. Prüfraster: persoenliche Angriffe Beleidigungen herabsetzende Formulierungen. Output: entschaerfte sachliche Version mit Erklärung. Abgrenzung: nicht für Ironie und Sarkasmus (ironie-und-sarkasmus-eliminieren). |
| `sachlichkeitsgebot-anwendung` | Sachlichkeitsgebot nach § 26 BORA auf konkrete Korrespondenz anwenden und Verbesserungen vornehmen. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: unsachliche Formulierungen Emotionalisierung Abwertungen Versachlichungspotenzial. Output: Prüfprotokoll ueberarbeitete sachliche Version. Abgrenzung: systematischer Sachlichkeits-Skill; nicht für spezifische Situationen wie Ironie oder Angriffe. |
| `sachverhalt-neutral-darstellen` | Sachverhalt in Anwaltskorrespondenz neutral und ohne wertende Parteinahme darstellen. § 43a BRAO Sachlichkeit §§ 86 ff. ZPO Sachverhaltspflicht. Prüfraster: Parteinahme Wertungen Auslassungen Einseitigkeit neutrale Formulierungen. Output: neutral formulierte Sachverhaltsdarstellung. Abgrenzung: nicht für rechtliche Stellungnahmen. |

## Arbeitsweg

Im Plugin Email Umformulierer Berufsrecht gilt für **Persoenlichen Angriff Sachlichkeitsgebot**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `persoenlichen-angriff-entschaerfen`

**Fokus:** Persoenliche Angriffe und Beleidigungen in Anwaltskorrespondenz erkennen und durch sachliche Formulierungen ersetzen. § 43a BRAO § 26 BORA Sachlichkeitsgebot. Prüfraster: persoenliche Angriffe Beleidigungen herabsetzende Formulierungen. Output: entschaerfte sachliche Version mit Erklärung. Abgrenzung: nicht für Ironie und Sarkasmus (ironie-und-sarkasmus-eliminieren).

# Persönlichen Angriff entschärfen

## Fachkern: Persönlichen Angriff entschärfen
- **Spezialgegenstand:** Persönlichen Angriff entschärfen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill vermittelt konkrete Techniken zur Entschärfung persönlicher Angriffe in beruflichen Texten. Persönliche Angriffe sind häufig das größte Hindernis für sachliche Kommunikation — sie verleiten den Empfänger zur Gegenreaktion und verhärten Fronten. Die systematische Umformulierung löst dieses Problem.


## Triage zu Beginn
1. Kommt der Angriff aus eingehendem Schreiben (neutralisieren im Antwortschreiben) oder aus eigenem Entwurf (entfernen)?
2. Welche Technik ist am besten geeignet: Beobachtung statt Vorwurf, Frage statt Urteil, Ich-Botschaft, Sachverhaltsbezug?
3. Gibt es zivilrechtlich oder strafrechtlich relevante Inhalte im Angriff (§ 185 StGB, § 823 BGB)?
4. Muss der Angriff vollstaendig entfernt oder kann der sachliche Kern erhalten werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot: persoenliche Angriffe unzulaessig
- § 185 StGB — Beleidigung: persoenliche Angriffe koennen strafbar sein
- § 823 Abs. 1 BGB — Persoenlichkeitsrecht: Schadenersatz bei Persoenlichkeitsverletzung
- § 1004 BGB — Unterlassungsanspruch bei andauernden persoenlichen Angriffen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Technik 1: Vom Vorwurf zur Beobachtung

Ein Vorwurf bewertet und verletzt: "Sie haben X getan." Eine Beobachtung beschreibt neutral: "X ist eingetreten." Statt: "Sie haben meine E-Mail ignoriert." → "Auf meine E-Mail vom TT.MM.JJJJ ist bisher keine Antwort eingegangen." Diese Technik ist die wirksamste Einzelmaßnahme zur Entschärfung.

## Technik 2: Vom Urteil zur Frage

Urteile provozieren Widerstand; Fragen öffnen Kommunikation. Statt: "Das ist falsch." → "Worauf stützen Sie diese Einschätzung?" Statt: "Das macht keinen Sinn." → "Könnten Sie das näher erläutern?" Statt: "Sie verstehen das offensichtlich nicht." → "Ich würde gerne sichergehen, dass wir dasselbe meinen."

## Technik 3: Vom Angriff zur Ich-Botschaft

Ich-Botschaften beschreiben die eigene Perspektive ohne Angriff auf den anderen. Statt: "Sie haben mich enttäuscht." → "Ich hatte eine andere Erwartung und möchte das klären." Statt: "Sie handeln unverantwortlich." → "Ich sehe die Situation anders und bitte um Gelegenheit zur Erläuterung."

## Technik 4: Distanzierung und Sachverhaltsbezug

Den persönlichen Angriff durch Sachverhaltsbezug ersetzen: Statt "Sie" als handelnde Person tritt das Dokument, die Frist oder die Vereinbarung in den Vordergrund. Statt: "Sie haben die Frist verpasst." → "Die Frist vom TT.MM.JJJJ ist verstrichen."

## Berufsrechtlicher Hintergrund

§ 43a Abs. 3 BRAO (Sachlichkeitsgebot), § 25 BORA (Kollegialitätsgebot). Persönliche Angriffe können — je nach Inhalt — auch zivilrechtliche Konsequenzen haben: Ansprüche aus §§ 823 Abs. 1 BGB (Persönlichkeitsrechtsverletzung), 824 BGB (Kreditgefährdung) oder 826 BGB (sittenwidrige Schädigung).

## Vorher-Nachher-Tabelle

| Angriff | Entschärft |
|---|---|
| "Sie lügen mich an" | "Ihre Darstellung weicht von meinen Unterlagen ab" |
| "Das ist Ihre Schuld" | "Die Ursache liegt im Bereich von X" |
| "Sie handeln skrupellos" | "Die Vorgehensweise erscheint mir rechtlich problematisch" |
| "Sie sind unzuverlässig" | "Die vereinbarten Fristen wurden bislang nicht eingehalten" |
| "Das können Sie nicht" | "Ich bezweifle, ob dafür die rechtliche Grundlage besteht" |
| "Sie machen alles falsch" | "Es bestehen Korrekturbedarf in mehreren Punkten" |
| "Sie kümmern sich nicht" | "Das Anliegen scheint bislang keine vorrangige Bearbeitung erhalten zu haben" |

## Ausgabeformat

Der Skill gibt aus: (1) Identifizierte persönliche Angriffe im Text. (2) Eingesetzte Entschärfungstechnik. (3) Neutralisierte Alternativformulierung. (4) Überarbeiteter Gesamttext ohne persönliche Angriffe.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `sachlichkeitsgebot-anwendung`

**Fokus:** Sachlichkeitsgebot nach § 26 BORA auf konkrete Korrespondenz anwenden und Verbesserungen vornehmen. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: unsachliche Formulierungen Emotionalisierung Abwertungen Versachlichungspotenzial. Output: Prüfprotokoll ueberarbeitete sachliche Version. Abgrenzung: systematischer Sachlichkeits-Skill; nicht für spezifische Situationen wie Ironie oder Angriffe.

# Sachlichkeitsgebot-Anwendung

## Fachkern: Sachlichkeitsgebot-Anwendung
- **Spezialgegenstand:** Sachlichkeitsgebot-Anwendung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill erläutert das anwaltliche Sachlichkeitsgebot in seiner normativen Tiefe und wendet es auf konkrete Formulierungen an. Das Sachlichkeitsgebot ist einer der wichtigsten berufsrechtlichen Standards und gleichzeitig einer der am häufigsten missverstandenen.

## § 43a Abs. 3 BRAO — Norminhalt

§ 43a Abs. 3 BRAO enthält das Sachlichkeitsgebot für Rechtsanwälte. Es verbietet: (a) bewusst unwahre Tatsachenbehauptungen, (b) herabsetzende Äußerungen, für die kein sachlicher Anlass besteht, (c) reine Schmähkritik ohne sachliche Auseinandersetzung. Das Sachlichkeitsgebot gilt für alle Äußerungen im Rahmen der Berufsausübung — also nicht nur gegenüber Mandanten, sondern auch gegenüber Kollegen, Gerichten, Behörden und der Öffentlichkeit.

## Abgrenzung: Kritik vs. Schmähkritik

Erlaubte Kritik ist sachbezogen, bezieht sich auf nachprüfbare Tatsachen oder klar kenntliche Werturteile und ist verhältnismäßig. Schmähkritik ist dagegen primär darauf ausgerichtet, den Adressaten zu verletzen oder herabzusetzen, ohne dass ein sachlicher Bezug zum Streitgegenstand besteht. Die Grenze ist fließend: Eine deutliche Kritik an einem Schriftsatz ist erlaubt; die persönliche Abwertung des Verfassers ist es nicht.

## Tatsachenbehauptungen vs. Werturteile

Tatsachenbehauptungen sind einer Wahrheitsprüfung zugänglich und müssen wahr sein oder zumindest auf ausreichenden tatsächlichen Anhaltspunkten beruhen. Werturteile sind Meinungsäußerungen, die verfassungsrechtlich durch Art. 5 Abs. 1 GG geschützt sind — aber auch Werturteile können in Schmähkritik umschlagen. Die Aussage "Ihr Schriftsatz enthält keine Auseinandersetzung mit § 284 BGB" ist eine prüfbare Tatsachenbehauptung. Die Aussage "Ihr Schriftsatz ist eine Frechheit" ist ein Werturteil, das keine sachliche Auseinandersetzung enthält.

## BVerfG-Rechtsprechung

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Berufsrechtlicher Hintergrund

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beispiele Vorher/Nachher

**Vorher:** "Das Gericht hat offensichtlich nicht einmal die Klageschrift gelesen."
**Nachher:** Werturteil mit sachlichem Bezug zulässig, wenn begründet. Besser: "Die Urteilsbegründung geht auf den Vortrag unter Ziffer 3 der Klageschrift nicht ein."

**Vorher:** "Die Gegenpartei handelt rechtsmissbräuchlich und verwerflich."
**Nachher:** Tatsachenbehauptung; Rechtsmissbrauch muss konkret belegt werden. Konform: "Es bestehen Anhaltspunkte für rechtsmissbräuchliches Verhalten, insbesondere aufgrund von X."

**Vorher:** "Ich erwarte von einem Richter, dass er das Gesetz kennt."
**Nachher:** Herabsetzend. Konform: "Ich bitte das Gericht, die Ausführungen zu § 284 BGB in der Berufungsbegründung zu berücksichtigen."

## Ausgabeformat

Der Skill gibt aus: (1) Einordnung der Äußerung (Tatsache / Werturteil / Schmähkritik). (2) Berufsrechtliche Bewertung. (3) Einschlägige Norm und ggf. Rechtsprechung. (4) Konforme Alternativformulierung.

## 3. `sachverhalt-neutral-darstellen`

**Fokus:** Sachverhalt in Anwaltskorrespondenz neutral und ohne wertende Parteinahme darstellen. § 43a BRAO Sachlichkeit §§ 86 ff. ZPO Sachverhaltspflicht. Prüfraster: Parteinahme Wertungen Auslassungen Einseitigkeit neutrale Formulierungen. Output: neutral formulierte Sachverhaltsdarstellung. Abgrenzung: nicht für rechtliche Stellungnahmen.

# Sachverhalt neutral darstellen

## Fachkern: Sachverhalt neutral darstellen
- **Spezialgegenstand:** Sachverhalt neutral darstellen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill transformiert subjektiv gefärbte, vorwurfsvolle oder emotionale Sachverhaltsschilderungen in sachliche, objektive Darstellungen. Ziel ist nicht die Verschleierung des Problems, sondern seine nüchterne und präzise Beschreibung — so wie es ein guter Schriftsatz erfordert.


## Triage zu Beginn
1. Welcher Abschnitt des Textes enthaelt subjektive Wertungen, die in neutrale Darstellung umgewandelt werden muessen?
2. Muss der Sachverhalt vollstaendig erhalten bleiben oder darf er kondensiert werden?
3. Fuer welchen Adressaten: Gericht (maximale Sachlichkeit), Mandant (erklaerend), Gegner (zurueckhaltend)?
4. Gibt es Passagen, bei denen die Distanzierungsformel ("nach Ihrer Darstellung") benoetigt wird?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot und Wahrheitspflicht bei Sachverhaltsschilderungen
- § 138 ZPO — Wahrheitspflicht der Parteien im Prozess (Sachverhalt muss wahrheitsgemaess dargestellt werden)
- § 823 Abs. 1 BGB — Persoenlichkeitsrecht: neutrale Schilderung schutzt vor Haftung
- § 193 StGB — Wahrnehmung berechtigter Interessen: Schutzbereich bei wahrheitsgemaesser sachlicher Darstellung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Grundprinzipien der neutralen Darstellung

Die wichtigsten Werkzeuge sind: Passivkonstruktionen (nicht "Sie haben versäumt" sondern "die Frist ist verstrichen"), Datumsbezüge statt unbestimmter Zeitangaben (nicht "seit Wochen" sondern "seit dem TT.MM.JJJJ"), unpersönliche Pronomen (nicht "Sie ignorieren" sondern "eine Rückmeldung steht noch aus"), Distanzierungsformeln (nicht "Sie behaupten" sondern "nach Ihrer Darstellung" oder "ausweislich Ihres Schreibens") sowie Trennung von Sachverhalt und Wertung.

## Passiv vs. Aktiv

Die Entscheidung zwischen Passiv und Aktiv hat im juristischen Kontext erhebliche Bedeutung. Passivkonstruktionen entlasten den Text von Schuldzuweisungen: "Eine Frist wurde bislang nicht gewährt" statt "Sie haben keine Frist gesetzt". Aktiv ist angebracht, wenn die handelnde Person bewusst benannt werden soll: "Mit Schreiben vom TT.MM.JJJJ hat die Gegenseite mitgeteilt...". Aktivkonstruktionen mit klarem Subjektbezug auf Dokumente oder Daten (nicht auf Personen) sind besonders effektiv.

## Distanzierungsformeln

Für die Wiedergabe fremder Darstellungen ohne eigene Wertung gelten folgende Formeln: "nach Ihrer Darstellung", "ausweislich Ihrer E-Mail vom TT.MM.JJJJ", "wie Sie mitteilen", "soweit ich Ihrem Schreiben entnehme", "nach dem mir vorliegenden Sachstand". Diese Formeln signalisieren, dass der Schreiber die Aussage zitiert, ohne sie zu bestätigen oder abzulehnen.

## Berufsrechtlicher Hintergrund

§ 43a Abs. 3 BRAO fordert Sachlichkeit. Das Sachlichkeitsgebot verlangt nicht nur die Vermeidung von Beleidigungen, sondern auch eine wahrheitsgemäße, nicht verzerrende Darstellung. Die neutrale Sachverhaltsschilderung schützt auch vor dem Vorwurf, bewusst falsche Tatsachen zu behaupten (§ 43a Abs. 3 Satz 2 BRAO).

## Beispiele Vorher/Nachher

**Vorher:** "Sie ignorieren mich seit Wochen."
**Nachher:** "Eine Rückmeldung auf das Schreiben vom TT.MM.JJJJ steht bislang aus."

**Vorher:** "Sie haben einfach die Frist verstreichen lassen, ohne mich zu informieren."
**Nachher:** "Die Frist vom TT.MM.JJJJ ist verstrichen. Eine vorherige Mitteilung ist nicht erfolgt."

**Vorher:** "Ihre Mandantin behauptet frech, sie habe nie zugestimmt."
**Nachher:** "Nach der Darstellung Ihrer Mandantin liegt eine Zustimmung nicht vor."

**Vorher:** "Anscheinend ist Ihnen die Vertragstreue nicht wichtig."
**Nachher:** "Die vereinbarte Leistung ist bis zum TT.MM.JJJJ nicht erbracht worden."

## Ausgabeformat

Der Skill gibt für jeden umzuformulierenden Satz aus: (1) Original. (2) Neutrale Fassung. (3) Erläuterung des eingesetzten Mittels (Passiv, Datumsbezug, Distanzierungsformel). (4) Optionaler Hinweis auf berufsrechtliche Relevanz.
