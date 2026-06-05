---
name: bora-konformitaetspruefung-brao-email
description: "BORA Konformitaetspruefung BRAO Email: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# BORA Konformitaetspruefung BRAO Email

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **BORA Konformitaetspruefung BRAO Email** im Plugin Email Umformulierer Berufsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bora-konformitaetspruefung` | E-Mail auf BORA-Konformität prüfen bevor sie versandt wird. §§ 6 ff. BORA allgemeine Berufspflichten § 26 BORA Werbung § 43 BORA Vertretungsverbot. Prüfraster: Sachlichkeitsgebot Werbeverbot Verschwiegenheit Interessenkonflikt unzulässige Versprechen. Output: BORA-Prüfprotokoll Beanstandungen Korrekturvorschlaege. Abgrenzung: nicht für BRAO-Prüfung (brao-konformitätsprüfung). |
| `brao-konformitaetspruefung` | E-Mail auf BRAO-Konformität prüfen bevor sie versandt wird. §§ 43 43a 43b BRAO Grundpflichten Sachlichkeitsgebot Werbung. Prüfraster: Verschwiegenheitspflicht Interessenkonflikt unabhängige Berufsausübung Werbegrenzen Mandatsbeziehung. Output: BRAO-Prüfprotokoll Beanstandungen Korrekturvorschlaege. Abgrenzung: nicht für BORA-Detailprüfung (bora-konformitätsprüfung). |
| `email-eingangsanalyse` | Eingehende E-Mail analysieren und Tonalitaet Konfliktpotenzial und Handlungsbedarf bestimmen. § 43a BRAO Berufsrecht. Prüfraster: Tonalitaet emotionale Trigger versteckte Forderungen Fristen Eskalationspotenzial. Output: Analyse-Memo Handlungsempfehlung Antwort-Strategie. Abgrenzung: nicht für die Umformulierung der Antwort (allgemeine-berufliche-korrespondenz). |

## Arbeitsweg

Im Plugin Email Umformulierer Berufsrecht gilt für **BORA Konformitaetspruefung BRAO Email**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bora-konformitaetspruefung`

**Fokus:** E-Mail auf BORA-Konformität prüfen bevor sie versandt wird. §§ 6 ff. BORA allgemeine Berufspflichten § 26 BORA Werbung § 43 BORA Vertretungsverbot. Prüfraster: Sachlichkeitsgebot Werbeverbot Verschwiegenheit Interessenkonflikt unzulässige Versprechen. Output: BORA-Prüfprotokoll Beanstandungen Korrekturvorschlaege. Abgrenzung: nicht für BRAO-Prüfung (brao-konformitätsprüfung).

# BORA-Konformitätsprüfung

## Fachkern: BORA-Konformitätsprüfung
- **Spezialgegenstand:** BORA-Konformitätsprüfung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill prüft anwaltliche Korrespondenz auf Übereinstimmung mit der Berufsordnung für Rechtsanwälte (BORA). Die BORA konkretisiert als Satzung der Bundesrechtsanwaltskammer die allgemeinen Berufspflichten der BRAO und enthält spezifische Regeln für Verschwiegenheit, Werbung und den kollegialen Umgang.


## Triage zu Beginn
1. Wer ist der Absender: Rechtsanwalt, Berufsausuebendes Gesellschafter oder Kanzleimitarbeiter?
2. Wer ist der Empfaenger: Mandant, Kollege, Gericht, Gegenseite oder Dritter?
3. Welche BORA-Norm ist primaer relevant: Verschwiegenheit (§ 2), Werbung (§ 6), Kollegialitaet (§ 25)?
4. Gibt es Hinweise auf Direktkontakt mit dem Mandanten des Kollegen (§ 12 BORA)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 2 BORA — Verschwiegenheitspflicht (Erweiterung der BRAO-Pflicht auf alle Kommunikationsmittel)
- § 6 BORA — Sachlichkeitsgebot fuer Aussenauftritt und Werbung
- § 12 BORA — Direktkontaktverbot bei anwaltlicher Vertretung der Gegenseite
- § 25 BORA — Kollegialitaetsgebot
- § 43a Abs. 2 BRAO — Grundlegende Verschwiegenheitspflicht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## § 2 BORA — Verschwiegenheit

§ 2 BORA dehnt die anwaltliche Verschwiegenheitspflicht auf alle Kommunikationsmittel aus. In E-Mails besonders relevant: Offenlegung mandatsbezogener Informationen an Dritte, Nutzung von Mandantendaten in werblichen Kontexten, unverschlüsselte Übermittlung sensibler Mandantendaten. Jede E-Mail, die Mandantendaten enthält, ist auf Verschwiegenheitskonformität zu prüfen — insbesondere bei CC-Feldern und Weiterleitungen.

## § 6 BORA — Sachlichkeit in der Außenkommunikation

§ 6 BORA konkretisiert das Werbeverbot nach § 43b BRAO für die praktische Anwendung. Erlaubt sind sachliche, berufsbezogene Informationen; verboten sind Angaben, die irreführend sind oder das Ansehen des Berufs beeinträchtigen. In E-Mails: Signaturen mit unzutreffenden Titeln oder Kompetenzclaims, Mandantenschreiben mit werblichem Überschuss.

## § 25 BORA — Umgang mit anderen Rechtsanwälten

§ 25 BORA kodifiziert das Kollegialitätsgebot. Rechtsanwälte sollen sich untereinander mit Respekt und kollegialem Verständnis begegnen. Konkret: Direktkontakt mit dem Mandanten des Kollegen ohne dessen Zustimmung ist grundsätzlich unzulässig (§ 12 BORA). Äußerungen über einen Kollegen müssen sachlich bleiben und dürfen nicht herabsetzen. Persönliche Angriffe auf den Kollegen in Schriftsätzen oder Mandatsschreiben verstoßen gegen § 25 BORA.

## Konkrete Prüfschritte

Schritt 1 (Verschwiegenheit): Werden mandatsbezogene Informationen weitergegeben? An wen? Mit welcher Grundlage? Schritt 2 (Werbung): Enthält das Schreiben Kompetenzaussagen oder Selbstdarstellungen, die nicht sachlich belegt sind? Schritt 3 (Kollegialität): Wird ein Kollege oder gegnerischer Anwalt namentlich negativ erwähnt? Ist die Kritik sachlich begründet oder reine Wertung? Schritt 4 (Direktkontakt): Wird die Gegenseite direkt angeschrieben, obwohl ein Anwalt bestellt ist?

## Berufsrechtlicher Hintergrund

Maßgebliche Normen: § 2 BORA (Verschwiegenheit), § 6 BORA (Werbung), § 12 BORA (Verbot des Direktkontakts mit Mandanten des Kollegen), § 25 BORA (Kollegialität). Die BORA hat den Rang einer Satzung der Bundesrechtsanwaltskammer und ist für alle deutschen Rechtsanwälte verbindlich.

## Beispiele Vorher/Nachher

**Vorher:** "Ich schreibe Ihnen direkt, weil Ihr Anwalt offenbar keine Zeit hat."
**Nachher (Prüfergebnis):** Verstoß gegen § 12 BORA (Direktkontaktverbot bei anwaltlicher Vertretung). Lösung: Schreiben an den Kollegen richten.

**Vorher:** "Ihr Kollege hat mir gesagt, dass er unsicher ist."
**Nachher (Prüfergebnis):** Möglicher Verstoß gegen § 25 BORA; Wiedergabe einer Äußerung des Kollegen ohne dessen Einwilligung. Formulierung: "Es wurde mündlich erörtert, ob..."

**Vorher:** "Wir sind bekannt für unsere Erfolge vor dem BGH."
**Nachher (Prüfergebnis):** Werberechtlich bedenklich nach § 6 BORA, sofern nicht durch öffentliche Informationen (Urteilslisten) belegt. Empfehlung: Konkrete, nachprüfbare Angabe.

## Ausgabeformat

Der Skill gibt aus: (1) Identifizierte BORA-Risikostellen mit Zitat. (2) Einschlägige BORA-Norm. (3) Schwere des Verstoßes (formal/substantiell). (4) Korrigierte Alternativformulierung. (5) Gesamtbewertung (konform / geringes Risiko / hohes Risiko).

## 2. `brao-konformitaetspruefung`

**Fokus:** E-Mail auf BRAO-Konformität prüfen bevor sie versandt wird. §§ 43 43a 43b BRAO Grundpflichten Sachlichkeitsgebot Werbung. Prüfraster: Verschwiegenheitspflicht Interessenkonflikt unabhängige Berufsausübung Werbegrenzen Mandatsbeziehung. Output: BRAO-Prüfprotokoll Beanstandungen Korrekturvorschlaege. Abgrenzung: nicht für BORA-Detailprüfung (bora-konformitätsprüfung).

# BRAO-Konformitätsprüfung

## Fachkern: BRAO-Konformitätsprüfung
- **Spezialgegenstand:** BRAO-Konformitätsprüfung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill prüft Ausgangsschreiben von Rechtsanwälten auf Einklang mit den Berufspflichten der Bundesrechtsanwaltsordnung. Der Fokus liegt auf § 43a BRAO (allgemeine Berufspflichten) mit dem darin enthaltenen Sachlichkeitsgebot sowie auf den Werbevorschriften des § 43b BRAO.

## § 43a BRAO — Allgemeine Berufspflichten

§ 43a Abs. 3 BRAO enthält das Sachlichkeitsgebot in seiner zentralen Form: Der Rechtsanwalt darf in Ausübung seines Berufs keine Äußerungen machen, die bewusst unwahr oder in sonstiger Weise unzulässig sind. Darunter fallen insbesondere herabsetzende Äußerungen über Personen ohne sachliche Grundlage, reine Schmähkritik und Behauptungen "ins Blaue hinein" — also ohne tatsächliche Grundlage. § 43a Abs. 1 BRAO verpflichtet zur Unabhängigkeit, § 43a Abs. 2 BRAO zur Verschwiegenheit über mandatsbezogene Tatsachen.

## § 43b BRAO — Werbung

§ 43b BRAO erlaubt sachliche, berufsbezogene Werbung, verbietet jedoch anpreisende, irreführende oder vergleichende Werbung, die das Ansehen der Rechtspflege beeinträchtigen könnte. In E-Mails relevant: Selbstdarstellungen im Briefkopf, Signaturen mit Kompetenzhinweisen sowie Mandantenschreiben, die werbliche Elemente enthalten.

## Prüfschritte

Schritt 1: Enthält das Schreiben Tatsachenbehauptungen über den Adressaten oder Dritte? Falls ja: Sind diese belegt oder belegbar? Schritt 2: Enthält das Schreiben Werturteile? Falls ja: Stützen sie sich auf einen nachvollziehbaren Sachverhalt oder sind sie reine Schmähung? Schritt 3: Wird der Adressat oder eine dritte Person in einer Weise bezeichnet, die über sachliche Kritik hinausgeht (Herabsetzung)? Schritt 4: Gibt es werbliche Aussagen im Schreiben, die sachlich nicht gedeckt sind?

## Berufsrechtlicher Hintergrund

Die relevanten Normen sind: § 43a Abs. 3 BRAO (Sachlichkeitsgebot), § 43b BRAO (Werbung), § 59b Abs. 2 Nr. 1 Buchst. d BRAO (Satzungsermächtigung für BORA-Sachlichkeitsregeln). Ergänzend: BGH-Beschluss vom 25. November 2013 (AnwZ (Brfg) 2/12) zur Abgrenzung von zulässiger Kritik und unzulässiger Herabsetzung.

## Beispiele Vorher/Nachher

**Vorher:** "Ihre Argumentation ist an Unkenntnis des geltenden Rechts kaum zu überbieten."
**Nachher (Prüfergebnis):** Unzulässig — Schmähkritik ohne sachliche Grundlage. Risiko: Berufsrechtliche Rüge, Beleidigungsklage. Empfehlung: "Die rechtliche Einordnung in Ihrem Schreiben weicht von der geltenden BGH-Rechtsprechung ab."

**Vorher:** "Wir sind die führende Kanzlei für Wirtschaftsrecht in Bayern."
**Nachher (Prüfergebnis):** Werberechtlich bedenklich nach § 43b BRAO, sofern keine objektive Grundlage (Rankings, Zertifizierungen) vorhanden. Empfehlung: Sachliche Beschreibung des Tätigkeitsschwerpunkts.

**Vorher:** "Der Gegner handelt bösgläubig und versucht, uns zu täuschen."
**Nachher (Prüfergebnis):** Tatsachenbehauptung ohne Belegbasis — Risiko gemäß § 43a Abs. 3 Satz 2 BRAO. Empfehlung: "Die Darstellung der Gegenseite weicht von den uns vorliegenden Unterlagen erheblich ab."

## Ausgabeformat

Der Skill gibt aus: (1) Liste problematischer Textstellen mit Zitat. (2) Einordnung (Sachlichkeitsverstoß / Werberechtsproblem / Tatsachenbehauptung ohne Grundlage). (3) Berufsrechtliches Risiko. (4) Vorgeschlagene konforme Alternativformulierung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `email-eingangsanalyse`

**Fokus:** Eingehende E-Mail analysieren und Tonalitaet Konfliktpotenzial und Handlungsbedarf bestimmen. § 43a BRAO Berufsrecht. Prüfraster: Tonalitaet emotionale Trigger versteckte Forderungen Fristen Eskalationspotenzial. Output: Analyse-Memo Handlungsempfehlung Antwort-Strategie. Abgrenzung: nicht für die Umformulierung der Antwort (allgemeine-berufliche-korrespondenz).

# E-Mail-Eingangsanalyse

## Fachkern: E-Mail-Eingangsanalyse
- **Spezialgegenstand:** E-Mail-Eingangsanalyse wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG, WPO, PAO, Sachlichkeitsgebot, Verschwiegenheit, Datenschutz und Deeskalationspflichten.
- **Entscheidende Weiche:** Bewahre rechtlichen Inhalt, entferne Eskalation, schütze Geheimnisse, markiere Fristen und formuliere sendefähig ohne falsches Anerkenntnis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill analysiert einen eingegangenen E-Mail-Text systematisch auf emotionale Belastung, unsachliche Formulierungen und potenzielle berufsrechtliche Risiken. Er bildet die Grundlage für alle nachfolgenden Umformulierungsschritte.


## Triage zu Beginn
1. Von wem stammt die E-Mail: Mandant, Gegner, gegnerischer Anwalt, Gericht, Behoerde oder Unbekannter?
2. Was ist der sachliche Kern der E-Mail — unabhaengig vom Tonfall?
3. Enthalt die E-Mail strafrechtlich relevante Aeusserungen (Beleidigung § 185 StGB, Bedrohung § 241 StGB)?
4. Soll die E-Mail beantwortet, weitergeleitet oder dokumentiert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot: verhindert Uebernahme aggressiven Tons aus Eingangskorrespondenz
- § 185 StGB — Beleidigung: ggf. bei strafrechtlich relevantem Inhalt Eingangs-E-Mail dokumentieren
- § 241 StGB — Bedrohung: bei Drohungen Dokumentationspflicht und ggf. Strafanzeige erwaegen
- § 823 Abs. 1 BGB — Persoenlichkeitsrecht: Gegenschreiben darf keine neuen Verletzungen setzen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Analyseebenen

Die Eingangsanalyse untersucht den Text auf vier Ebenen: sprachliche Auffälligkeiten (Schimpfwörter, Großbuchstaben, übermäßige Satzzeichen), rhetorische Stilmittel (Sarkasmus, Ironie, Übertreibung), inhaltliche Vorwürfe (Kompetenzabsprache, Unterstellungen, Drohungen) sowie strukturelle Mängel (fehlende sachliche Begründung, reine Emotionsäußerung ohne Kernbotschaft).

## Konfliktgrad-Klassifikation

Der Skill kategorisiert den Konfliktgrad in drei Stufen. Gering bedeutet: einzelne unhöfliche Formulierungen, sachlicher Kern erkennbar, kein persönlicher Angriff. Mittel bedeutet: mehrere emotionale Trigger, Vorwürfe an die Person, Drohgebärde oder Ultimatum. Hoch bedeutet: überwiegend unsachlich, persönliche Herabsetzung, Schimpfwörter oder strafrechtlich relevante Äußerungen.

## Trigger-Kategorien

Die wichtigsten emotionalen Trigger sind: Großschreibung ganzer Wörter oder Sätze (impliziert Schreien), Ausrufezeichen-Ketten (erzeugen aggressiven Ton), direkte persönliche Anreden mit Vorwurf-Charakter ("Sie haben...", "Sie sind..."), implizite oder explizite Drohungen ("Ich werde...", "Das hat Konsequenzen"), Sarkasmus und Ironie (untergraben sachliche Auseinandersetzung) sowie Pauschalurteile ohne Sachverhaltsbezug.

## Berufsrechtlicher Hintergrund

§ 43a Abs. 3 BRAO verpflichtet Rechtsanwälte zur Sachlichkeit in der beruflichen Kommunikation. Die Weiterleitung oder das Zitieren eines unsachlichen Eingangsschreibens ohne Analyse kann dazu verleiten, im eigenen Schreiben denselben Ton zu übernehmen — was berufsrechtlich problematisch ist. Die Eingangsanalyse hilft, eine bewusste Distanz zum emotionalen Gehalt herzustellen.

## Beispiele Vorher/Nachher

**Vorher:** "SIE HABEN MIR NICHT GEANTWORTET!!! Das ist eine Frechheit!!!"
**Nachher (Analyse):** Konfliktgrad hoch. Trigger: Großbuchstaben, Mehrfach-Ausrufezeichen, Vorwurf fehlender Reaktion. Kern: Bitte um Rückmeldung auf ein früheres Schreiben.

**Vorher:** "Ich erwarte sofort eine Erklärung, sonst schalte ich meinen Anwalt ein."
**Nachher (Analyse):** Konfliktgrad mittel. Trigger: Drohgebärde, Ultimatum. Kern: Bitte um Stellungnahme zu einem bestimmten Sachverhalt.

**Vorher:** "Ihre Kollegin hat mir versprochen, dass das erledigt wird. Offenbar sind dort alle unfähig."
**Nachher (Analyse):** Konfliktgrad mittel-hoch. Trigger: Pauschalurteil, Kompetenzabsprache. Kern: Unerfüllte Zusage eines Mitarbeiters; Klärungsbedarf.

## Ausgabeformat

Der Skill gibt aus: (1) Tabellarische Trigger-Liste mit Zitat, Trigger-Typ und Einordnung. (2) Konfliktgrad-Einschätzung (gering/mittel/hoch) mit Begründung. (3) Sachlicher Kerninhalt in einem Satz. (4) Empfehlung, welche weiteren Skills zur Umformulierung einzusetzen sind.
