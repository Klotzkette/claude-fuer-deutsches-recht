---
name: kollegialitaetsgebot-kompetenz-zweifel
description: "Kollegialitaetsgebot Kompetenz Zweifel: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kollegialitaetsgebot Kompetenz Zweifel

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kollegialitaetsgebot Kompetenz Zweifel** im Plugin Email Umformulierer Berufsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kollegialitaetsgebot-pruefung` | E-Mail auf Einhaltung des Kollegialitätsgebots gegenüber Kollegen und Kolleginnen prüfen. § 43a Abs. 3 BRAO § 26 BORA Kollegialität. Prüfraster: kollegiale Formulierungen fehlende Abwertungen sachliche Kritik professioneller Umgangston. Output: Kollegialitäts-Prüfprotokoll Korrekturvorschlaege. Abgrenzung: nicht für Mandantenkommunikation. |
| `kompetenz-zweifel-respektvoll` | Zweifel an Kompetenz oder Entscheidung des Gegners oder Kollegen respektvoll und sachlich aeussern. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: sachliche Kritik ohne Abwertung Begründung Quellenangabe professioneller Ton. Output: ueberarbeitete Formulierung mit Erklärung. Abgrenzung: nicht für direkten persoenlichen Angriff (persoenlichen-angriff-entschaerfen). |
| `konfliktdeeskalation-formulierungen` | Eskalierte oder hitzige Korrespondenz deeskalieren und konstruktive Kommunikationsbasis herstellen. § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Eskalationsniveau Interessenidentifikation deeskalierende Formulierungen Angebote zur Lösung. Output: deeskalierende Version Kommunikationsstrategie. Abgrenzung: nicht für allgemeine Umformulierung. |

## Arbeitsweg

Im Plugin Email Umformulierer Berufsrecht gilt für **Kollegialitaetsgebot Kompetenz Zweifel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kollegialitaetsgebot-pruefung`

**Fokus:** E-Mail auf Einhaltung des Kollegialitätsgebots gegenüber Kollegen und Kolleginnen prüfen. § 43a Abs. 3 BRAO § 26 BORA Kollegialität. Prüfraster: kollegiale Formulierungen fehlende Abwertungen sachliche Kritik professioneller Umgangston. Output: Kollegialitäts-Prüfprotokoll Korrekturvorschlaege. Abgrenzung: nicht für Mandantenkommunikation.

# Kollegialitätsgebot-Prüfung

## Fachkern: Kollegialitätsgebot-Prüfung
- **Spezialgegenstand:** Kollegialitätsgebot-Prüfung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill prüft Korrespondenz gezielt auf Einhaltung des anwaltlichen Kollegialitätsgebots nach § 25 BORA. Der kollegiale Umgang unter Rechtsanwälten ist nicht nur eine Frage des guten Tons, sondern eine berufsrechtliche Pflicht, deren Verletzung zu Rüge- oder Ahndungsverfahren führen kann.


## Triage zu Beginn
1. Wer ist Adressat des Schreibens: Kollege direkt, Mandant ueber den Kollegen oder Gericht?
2. Bezieht sich die Aeusserung auf fachliche Kritik (zulaessig) oder auf persoenliche Eigenschaften (unzulaessig)?
3. Ist die Aeusserung ueber den Kollegen notwendig fuer den sachlichen Inhalt des Schreibens?
4. Hat die Gegenseite ihrerseits das Kollegialitaetsgebot verletzt — und verleitet das zur Erwiderung?

## Aktuelle Rechtsprechung
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 25 BORA — Kollegialitaetsgebot
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot als Grundlage des Kollegialitaetsgebots
- § 12 BORA — Direktkontaktverbot: kein Schreiben an Mandanten des Kollegen ohne Einwilligung
- § 43b BRAO — Werbeverbot: keine herabsetzenden Vergleiche mit Kollegen in Aussenkommunikation

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Das Kollegialitätsgebot nach § 25 BORA

§ 25 BORA verpflichtet Rechtsanwälte zu gegenseitiger Rücksichtnahme und einem fairen Umgang auch in streitigen Situationen. Das bedeutet konkret: keine persönlichen Angriffe auf den Kollegen (auch wenn der Mandant das wünscht), keine Herabsetzung der fachlichen Leistung ohne sachliche Grundlage, keine Unterstellungen über persönliche Motive. Das Kollegialitätsgebot gilt nicht nur in der Kommunikation von Anwalt zu Anwalt, sondern auch in Mandantenanschreiben, wenn darin über den gegnerischen Kollegen gesprochen wird.

## Zulässige vs. unzulässige Kritik an Kollegen

Zulässig ist sachlich begründete Kritik: "Der Schriftsatz Ihres Kollegen enthält keine ausreichende Auseinandersetzung mit der BGH-Rechtsprechung zu XY." Unzulässig ist persönliche Herabsetzung: "Ihr unfähiger Anwalt hat die Frist versäumt." Zulässig ist die Beschreibung eines Verfahrensfehlers: "Die Klagefrist wurde nicht gewahrt." Unzulässig ist die Qualifikation als persönliches Versagen: "Ihr Anwalt hat sein Handwerk nicht gelernt."

## Besondere Problemfelder

Besonders häufige Verstöße treten auf bei: Mandantenschreiben, in denen der eigene Anwalt über den gegnerischen Kollegen urteilt; E-Mails an Gerichte, in denen der Kollege persönlich kritisiert wird; Schreiben unter Kollegen, in denen Ironie oder Sarkasmus eingesetzt werden; Reaktionen auf provokante Schreiben der Gegenseite, bei denen der Ton übernommen wird.

## Prüfschritte

Schritt 1: Kommt der Name oder die Berufsbezeichnung eines Kollegen im Schreiben vor? Schritt 2: Ist die Aussage über den Kollegen eine Tatsachenbehauptung oder ein Werturteil? Schritt 3: Ist das Werturteil sachlich begründet und notwendig für den Inhalt? Schritt 4: Ist die Formulierung geeignet, das Ansehen des Kollegen zu schädigen?

## Berufsrechtlicher Hintergrund

§ 25 BORA (Kollegialitätsgebot), ergänzend § 43a Abs. 3 BRAO (Sachlichkeitsgebot). Das OLG Frankfurt hat in mehreren Entscheidungen klargestellt, dass herabsetzende Äußerungen über Kollegen selbst dann berufsrechtlich unzulässig sind, wenn der Kollege seinerseits unsachlich kommuniziert hat. Das eigene Fehlverhalten der Gegenseite rechtfertigt keine Herabsetzung.

## Beispiele Vorher/Nachher

**Vorher:** "Ihr unfähiger Anwalt hat meine Mandantin falsch beraten."
**Nachher:** "Die Beratung Ihrer Mandantin durch den Kollegen hat nach meiner Einschätzung zu einem rechtlich nachteiligen Ergebnis geführt."

**Vorher:** "Ihr Kollege versteht offenbar nicht, was ein Erfüllungsanspruch ist."
**Nachher:** "Die rechtliche Einordnung im Schreiben des Kollegen weicht von der geltenden Dogmatik ab."

**Vorher:** "Der Herr Kollege sollte vielleicht nochmal die Grundlagen studieren."
**Nachher:** Streichen oder ersetzen durch: "Ich erlaube mir, auf folgende Rechtsprechung hinzuweisen, die für den Sachverhalt einschlägig sein dürfte..."

## Ausgabeformat

Der Skill gibt aus: (1) Zitate kollegialitätsgefährdender Aussagen. (2) Einordnung (formal/substantiell problematisch). (3) Berufsrechtliches Risiko. (4) Konforme Alternativformulierung. (5) Hinweis, ob die Aussage gänzlich gestrichen werden sollte.

## 2. `kompetenz-zweifel-respektvoll`

**Fokus:** Zweifel an Kompetenz oder Entscheidung des Gegners oder Kollegen respektvoll und sachlich aeussern. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: sachliche Kritik ohne Abwertung Begründung Quellenangabe professioneller Ton. Output: ueberarbeitete Formulierung mit Erklärung. Abgrenzung: nicht für direkten persoenlichen Angriff (persoenlichen-angriff-entschaerfen).

# Kompetenz-Zweifel respektvoll formulieren

## Fachkern: Kompetenz-Zweifel respektvoll formulieren
- **Spezialgegenstand:** Kompetenz-Zweifel respektvoll formulieren wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill hilft dabei, fachliche Kritik oder Zweifel an der Kompetenz eines Adressaten so zu formulieren, dass der sachliche Kern erhalten bleibt, die Person aber nicht angegriffen wird. Diese Unterscheidung ist im Berufsrecht zentral: Sachkritik ist erlaubt, Personenabwertung ist es nicht.


## Triage zu Beginn
1. Bezieht sich die Fachkritik auf ein konkretes Dokument/Ergebnis (Sachkritik) oder auf die Person (Personenabwertung)?
2. Wer ist der Adressat: Kollege direkt, eigener Mandant ueber den Kollegen oder Gericht?
3. Gibt es einschlaeige Rechtsprechung oder Normen, auf die die Sachkritik gestuetzt werden kann?
4. Ist die Aeusserung notwendig fuer den Inhalt des Schreibens oder kann sie weggelassen werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot: Sachkritik erlaubt, Personenabwertung verboten
- § 25 BORA — Kollegialitaetsgebot: respektvoller Umgang auch bei Fachkritik
- Art. 5 GG — Meinungsfreiheit: Schutz sachlicher Kritik
- § 824 BGB — Kreditgefaehrdung: unwahre Kompetenzabsprachen loesen Haftung aus

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Der Unterschied: Sachkritik vs. Personenabwertung

Sachkritik bezieht sich auf ein konkretes Handeln, Dokument oder Ergebnis. Sie ist nachprüfbar, begründet und verhältnismäßig. Personenabwertung bezieht sich auf die Person selbst — ihre Intelligenz, Ausbildung, Persönlichkeit — und ist nicht nachprüfbar. Die Grenze: "Dieser Schriftsatz enthält keinen Verweis auf § 278 BGB" ist Sachkritik. "Sie kennen § 278 BGB offenbar nicht" ist Personenabwertung.

## Technik: Vom Vorwurf zum Sachverhalt

Statt die Person als inkompetent zu bezeichnen, wird das konkrete Ergebnis bewertet und auf sachliche Maßstäbe (Gesetze, Rechtsprechung, anerkannte Standards) verwiesen. Dies vermeidet den Vorwurf, schafft aber denselben sachlichen Klärungsbedarf.

## Technik: Rechtsprechungsverweis statt Urteil

Die wirksamste Form respektvoller Fachkritik ist der Verweis auf einschlägige Normen oder Rechtsprechung: Nicht "Sie liegen falsch", sondern "Nach dem Urteil des BGH vom TT.MM.JJJJ (Az. XY) ist davon auszugehen, dass..." — dieser Verweis zeigt die Abweichung auf, ohne die Person anzugreifen.

## Berufsrechtlicher Hintergrund

§ 43a Abs. 3 BRAO (Sachlichkeitsgebot), § 25 BORA (Kollegialitätsgebot). Der BGH hat in Beschlüssen zum Berufsrecht klargestellt, dass sachliche Fachkritik auch dann zulässig ist, wenn sie unangenehm für den Adressaten ist — vorausgesetzt, sie bezieht sich auf nachprüfbare Tatsachen und überschreitet nicht die Schwelle zur Schmähkritik.

## Vorher-Nachher-Tabelle

| Kompetenzangriff | Respektvolle Sachkritik |
|---|---|
| "Sie haben keine Ahnung" | "Die fachliche Einordnung erscheint mir abweichend von Rechtsprechung XY" |
| "Das ist dilettantisch" | "Die Ausführung entspricht nicht dem üblichen Standard in dieser Frage" |
| "Ihr Gutachten ist wertlos" | "Das Gutachten enthält keine Auseinandersetzung mit dem einschlägigen BGH-Urteil XY" |
| "Ihr Anwalt ist überfordert" | "Die gewählte Strategie erscheint mir in Anbetracht von XY nicht optimal" |
| "Das haben Sie falsch berechnet" | "In der Berechnung ergibt sich nach meiner Prüfung ein abweichender Wert" |
| "Sie verstehen das Gesetz nicht" | "Die Norm des § XY wird in der Fachliteratur überwiegend anders ausgelegt" |

## Ausgabeformat

Der Skill gibt aus: (1) Identifizierte Kompetenzabsprache. (2) Sachlicher Kern der Kritik. (3) Respektvolle Alternativformulierung mit Sachverhaltsbezug. (4) Ggf. geeigneter Normen- oder Rechtsprechungsverweis als Ersatz für die persönliche Bewertung.

## 3. `konfliktdeeskalation-formulierungen`

**Fokus:** Eskalierte oder hitzige Korrespondenz deeskalieren und konstruktive Kommunikationsbasis herstellen. § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Eskalationsniveau Interessenidentifikation deeskalierende Formulierungen Angebote zur Lösung. Output: deeskalierende Version Kommunikationsstrategie. Abgrenzung: nicht für allgemeine Umformulierung.

# Konfliktdeeskalation: Formulierungsbausteine

## Fachkern: Konfliktdeeskalation: Formulierungsbausteine
- **Spezialgegenstand:** Konfliktdeeskalation: Formulierungsbausteine wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill stellt eine kuratierte Sammlung deeskalierender Formulierungsbausteine bereit. Ziel ist es, in angespannten Korrespondenzsituationen den Ton zu senken, ohne die eigene Position aufzugeben oder dem Adressaten nachzugeben. Deeskalation bedeutet nicht Kapitulation, sondern Steuerung des Kommunikationsklimas.


## Triage zu Beginn
1. Auf welcher Konfliktebene befindet sich die Situation: sachlich, emotional oder eskaliert?
2. Will die eigene Seite deeskalieren oder hat sie berechtigte Interessen, die klar formuliert werden muessen?
3. Steht ein Gerichtsverfahren kurz bevor oder gibt es noch Raum fuer aussergerichtliche Einigung?
4. Wer ist der Adressat der deeskalierenden Formulierung: Kollege, Mandant, Gegner oder Gericht?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 17 BORA — Aussergerichtliche Streitbeilegung als berufsrechtlich unterstuetzter Weg
- § 242 BGB — Treu und Glauben: Kooperationspflichten der Parteien
- § 278 ZPO — Gueteverhandlung: Gericht foerdert Einigung; kooperativer Ton staerkt Glaubwuerdigkeit
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot als Grundlage deeskalierender Kommunikation

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prinzipien der Deeskalation

Deeskalierende Kommunikation folgt vier Grundprinzipien: (1) Verständnis zeigen ohne zuzustimmen — man nimmt die Perspektive zur Kenntnis, ohne sie zu teilen. (2) Sachlichkeit einfordern ohne zu provozieren — man benennt das Kommunikationsproblem, ohne es dem Adressaten anzulasten. (3) Konstruktiven Ausblick geben — man zeigt einen Weg zur Klärung auf. (4) Gemeinsame Interessen betonen — man hebt hervor, was beide Seiten wollen.

## Bausteine für Verständnis ohne Zustimmung

"Es ist mir ein Anliegen, Ihren Standpunkt vollständig zu verstehen." — "Ich nehme Ihre Schilderung zur Kenntnis und möchte gerne dazu Stellung nehmen." — "Ich verstehe, dass diese Situation für Sie belastend ist." — "Ich kann nachvollziehen, dass Sie mit dem bisherigen Verlauf nicht zufrieden sind." — "Ihre Perspektive ist mir wichtig, auch wenn ich in der Sache anderer Auffassung bin."

## Bausteine für sachliche Klärung

"Im Sinne einer sachlichen Klärung schlage ich vor..." — "Ich bitte darum, die Angelegenheit auf der Sachebene zu erörtern." — "Zur Vermeidung von Missverständnissen möchte ich folgendes klarstellen..." — "Es wäre hilfreich, wenn wir uns auf die wesentlichen Punkte konzentrieren könnten." — "Ich bin gerne bereit, die Situation gemeinsam zu klären."

## Bausteine für konstruktiven Ausblick

"Ich freue mich auf eine gemeinsame Lösung." — "Ich schlage vor, dass wir..." — "Im Sinne einer einvernehmlichen Regelung..." — "Ich stehe für ein klärendes Gespräch jederzeit zur Verfügung." — "Eine Lösung, die für alle Seiten akzeptabel ist, erscheint mir erreichbar."

## Bausteine für Missverständnis-Auflösung

"Es scheint hier zu einem Missverständnis gekommen zu sein, das ich gerne aufklären möchte." — "Vielleicht habe ich mich in meinem letzten Schreiben nicht klar genug ausgedrückt." — "Ich möchte meinen Standpunkt noch einmal präzisieren." — "Es tut mir leid, wenn meine Formulierung zu Irritationen geführt hat."

## Bausteine für Entschärfung von Drohgebärden

"Ich hoffe, wir können die Angelegenheit ohne förmliche Maßnahmen regeln." — "Selbstverständlich stehen Ihnen alle rechtlichen Wege offen; gleichzeitig lade ich Sie ein, zunächst..." — "Ich bin zuversichtlich, dass eine Einigung im gemeinsamen Interesse beider Seiten liegt."

## Berufsrechtlicher Hintergrund

§ 43a Abs. 3 BRAO verlangt sachliche Kommunikation. Deeskalation ist berufsrechtlich nicht vorgeschrieben, aber strategisch klug: Sie hält die Kommunikation offen und vermeidet unnötige Eskalation, die häufig zu berufsrechtlich problematischen Reaktionen auf beiden Seiten führt. § 17 BORA (außergerichtliche Streitbeilegung) unterstreicht den Wert einvernehmlicher Lösungen.

## Ausgabeformat

Der Skill gibt aus: (1) Vorgeschlagene Deeskalations-Bausteine passend zur Situation. (2) Hinweis auf die Funktion jedes Bausteins. (3) Überarbeiteter Gesamttext mit integrierten Deeskalationselementen.
