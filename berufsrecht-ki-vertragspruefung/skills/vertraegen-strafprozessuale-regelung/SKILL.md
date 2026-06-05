---
name: vertraegen-strafprozessuale-regelung
description: "Vertraegen Strafprozessuale Regelung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vertraegen Strafprozessuale Regelung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vertraegen Strafprozessuale Regelung** im Plugin Berufsrecht Ki Vertragspruefung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-vertraegen-dokumentenmatrix-und-lueckenliste` | Verträgen: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `strafprozessuale-regelung-pruefen` | Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei behoerdlichen Auskunftsverlangen Informationspflicht gegenüber der Kanzlei. Ergaenzung zum berufsrechtlich-strafrechtlichen Schutz. |
| `strafrechtliche-belehrung-pruefen` | Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB. Empfehlung Normtext als Vertragsanlage. Hinweis auf Sekundaerpflicht des Dienstleisters nach § 203 Absatz vier Satz zwei Nummer eins StGB. |

## Arbeitsweg

Im Plugin Berufsrecht Ki Vertragspruefung gilt für **Vertraegen Strafprozessuale Regelung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-vertraegen-dokumentenmatrix-und-lueckenliste`

**Fokus:** Verträgen: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Verträgen: Dokumentenmatrix, Lückenliste und Nachforderung

## Spezialwissen: Verträgen: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** Verträgen: Dokumentenmatrix, Lückenliste und Nachforderung / vertraegen dokumentenmatrix und lueckenliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AI, WP, BRAO, StBerG, WPO, PAO, BNotO, KI.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verträgen** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

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

## 2. `strafprozessuale-regelung-pruefen`

**Fokus:** Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei behoerdlichen Auskunftsverlangen Informationspflicht gegenüber der Kanzlei. Ergaenzung zum berufsrechtlich-strafrechtlichen Schutz.

# Strafprozessuale Regelung prüfen

## Fachkern: Strafprozessuale Regelung prüfen

- **KI-/Berufsrechtsproblem (Strafprozessuale Regelung prüfen):** Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei behoerdlichen Auskunftsverlangen Informationspflicht gegenüber der Kanzlei. Ergaenzung zum berufsrechtlich-strafrechtlichen Schutz.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Normen

### § 53a StPO — Zeugnisverweigerungsrecht der mitwirkenden Personen

§ 53a StPO erstreckt das Zeugnisverweigerungsrecht der in § 53 Abs. 1 Satz 1 Nr. 1 bis 4 StPO genannten Berufsgeheimnisträger (also Geistliche, Verteidiger, Rechtsanwälte, Patentanwälte, Notare, Steuerberater, Wirtschaftsprüfer, Ärzte etc.) auf ihre Berufshelfer und die ihnen mitwirkenden Personen. Damit auch der KI-Dienstleister, soweit er als "mitwirkende Person" im Sinne des § 203 Abs. 3 Satz 2 StGB eingebunden ist.

### § 97 StPO — Beschlagnahmeverbot

§ 97 Abs. 1 StPO normiert ein Beschlagnahmeverbot für Schriftstücke und elektronische Daten, die sich im Gewahrsam der zur Zeugnisverweigerung Berechtigten befinden, soweit das Vertrauensverhältnis betroffen ist. § 97 Abs. 2 Satz 2 StPO erstreckt dies auch auf Daten, die im Gewahrsam der mitwirkenden Personen liegen.

Praktische Konsequenz: Mandatsdaten beim KI-Dienstleister sind grundsätzlich der Beschlagnahme entzogen, soweit die Verschwiegenheitspflicht gilt.

## Vertragliche Anforderungen

Diese Schutzwirkung muss im Vertrag operationalisiert werden. Empfehlungen:

### Widerspruchspflicht des Dienstleisters

Der Dienstleister soll sich verpflichten, behördlichen Auskunftsverlangen, Beschlagnahmebeschlüssen oder Herausgabeverfügungen mit dem Hinweis auf §§ 53a, 97 StPO entgegenzutreten — und nicht widerstandslos zu kooperieren.

### Informationspflicht gegenüber der Kanzlei

Der Dienstleister muss die Kanzlei unverzüglich informieren, sobald ein Auskunftsverlangen, eine Durchsuchung oder eine Beschlagnahmeanordnung droht oder erfolgt — soweit gesetzlich zulässig (manche US-Beschlagnahmeanordnungen kommen mit Gag Order).

### Pflicht zur prozessualen Inanspruchnahme

Im Idealfall verpflichtet sich der Dienstleister, gegen unzulässige Beschlagnahmen den Rechtsweg zu beschreiten, mindestens aber Widerspruch einzulegen.

### Gerichtsstand und anwendbares Recht

Anwendbares deutsches Recht und ein deutscher Gerichtsstand sind dringend zu empfehlen, da §§ 53a, 97 StPO nur im deutschen Verfahren wirken.

## Prüfschema

| Punkt | Fundstelle | Ampel | Bemerkung |
|---|---|---|---|
| Hinweis auf §§ 53a, 97 StPO im Vertrag | | | |
| Widerspruchspflicht bei behördlichen Verlangen | | | |
| Informationspflicht gegenüber Kanzlei | | | |
| Pflicht zur prozessualen Inanspruchnahme | | | |
| Deutsches Recht und Gerichtsstand | | | |
| Gag-Order-Klausel (Information so weit zulässig) | | | |

## US-Konstellationen — CLOUD Act

Bei US-Anbietern oder US-Töchtern greift der US-CLOUD Act und kann § 97 StPO faktisch unterlaufen. Hier ist ein separates Professional Secrecy Addendum erforderlich (siehe `cloud-act-und-drittstaat-pruefen`).

## Typische Lücken

- Keine Erwähnung von §§ 53a, 97 StPO
- Klausel "wir kooperieren mit Behörden" ohne Vorbehalt
- Keine Pflicht zur Vorab-Information der Kanzlei
- Nur US-Eskalationspfad, kein deutsches Verfahren möglich

## Output

Tabellarische Bewertung. Defizite fließen in den Rückfragebrief und in die Klauselvorschläge.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- §§ 53, 53a StPO — Zeugnisverweigerungsrecht und dessen Erstreckung auf Berufshelfer
- §§ 94–98 StPO — Beschlagnahme; § 97 StPO Beschlagnahmeverbot für Mandatsunterlagen
- § 203 Abs. 4 StGB — Pflicht des Berufsgeheimnisträgers, den Dienstleister auf §§ 203/204 StGB hinzuweisen
- §§ 43e Abs. 3, 62a Abs. 3 StBerG etc. — Vertragsinhalt

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Ist im Vertrag geregelt, wie der Dienstleister mit behördlichen Auskunftsersuchen umgeht?
2. Enthält der Vertrag eine Widerstandspflicht (Pflicht zur Rechtsbehelfseinlegung)?
3. Ist eine Vorab-Informationspflicht gegenüber der Kanzlei geregelt?
4. Bei US-Anbietern: CLOUD Act Addendum vorhanden?

## Output-Template — Strafprozessuale Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Strafprozessuale Prüfvermerk [DATUM]
Anbieter: [NAME] | Vertrag: [DOKUMENT, VERSION]

Prüfpunkt 1: Zeugnisverweigerungsrecht (§ 53a StPO)
Vertrag regelt Mitwirkung als Berufshelfer: ja / nein / unklar
Fundstelle: [KLAUSEL]

Prüfpunkt 2: Widerstandspflicht bei behördlichen Auskunftsersuchen
Klausel vorhanden: ja / nein
Inhalt: [BESCHREIBUNG]
Fundstelle: [KLAUSEL]

Prüfpunkt 3: Vorab-Informationspflicht der Kanzlei
Geregelt: ja / nein
Fundstelle: [KLAUSEL]

Ergebnis
Ampel strafprozessuale Absicherung: GRUEN / GELB / ROT
Handlungsbedarf: [...]
```

## 3. `strafrechtliche-belehrung-pruefen`

**Fokus:** Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB. Empfehlung Normtext als Vertragsanlage. Hinweis auf Sekundaerpflicht des Dienstleisters nach § 203 Absatz vier Satz zwei Nummer eins StGB.

# Strafrechtliche Belehrung prüfen

## Fachkern: Strafrechtliche Belehrung prüfen

- **KI-/Berufsrechtsproblem (Strafrechtliche Belehrung prüfen):** Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB. Empfehlung Normtext als Vertragsanlage. Hinweis auf Sekundaerpflicht des Dienstleisters nach § 203 Absatz vier Satz zwei Nummer eins StGB.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm

Absatz 3 Satz 2 Nr. 1 der jeweiligen Dienstleisterregelung verlangt die Verpflichtung des Dienstleisters "unter Belehrung über die strafrechtlichen Folgen einer Pflichtverletzung". Diese Folgen ergeben sich aus § 203 StGB und § 204 StGB.

Pro Beruf identische Anforderung in:

- § 43e Abs. 3 Satz 2 Nr. 1 BRAO
- § 62a Abs. 3 Satz 2 Nr. 1 StBerG
- § 50a Abs. 3 Satz 2 Nr. 1 WPO
- § 39c Abs. 3 Satz 2 Nr. 1 PAO
- § 26a Abs. 3 Satz 2 Nr. 1 BNotO

## § 203 StGB — Architektur

### Abs. 1 — Strafbarkeit der Berufsgeheimnisträger

Wer ein fremdes Geheimnis offenbart, das ihm in seiner Eigenschaft als Angehöriger der dort genannten Berufsgruppen anvertraut oder bekanntgeworden ist. Nr. 1 erfasst unter anderem Notare; Nr. 3 erfasst Rechtsanwälte, Patentanwälte, Notare (alternativ), Steuerberater, Wirtschaftsprüfer und vergleichbare Berufsgruppen.

### Abs. 3 Satz 2 — Befugnisnorm

Die in Abs. 1 Genannten dürfen fremde Geheimnisse gegenüber sonstigen mitwirkenden Personen offenbaren, soweit dies für die Inanspruchnahme der Tätigkeit der sonstigen Personen erforderlich ist. Dies ist die strafrechtliche Befugnisnorm, die das Berufsrecht (§ 43e BRAO etc.) ergänzt.

### Abs. 4 — Strafbarkeit des Dienstleisters

**Abs. 4 Satz 1**: Die strafrechtliche Verantwortlichkeit erstreckt sich auch auf die "sonstigen mitwirkenden Personen", wenn sie das Geheimnis unbefugt offenbaren.

**Abs. 4 Satz 2 Nr. 1**: Sekundärpflicht der Berufsgeheimnisträger — sie haben die mitwirkenden Personen vertraglich zur Geheimhaltung zu verpflichten. Wer dies unterlässt, macht sich nach § 203 Abs. 4 Satz 2 Nr. 1 StGB selbst strafbar. Das ist der zentrale strafrechtliche Druckpunkt für die Sorgfalt bei der Vertragsgestaltung.

### Abs. 6 — gewerbsmäßig

Gewerbsmäßiges Handeln führt zu erhöhter Strafandrohung. Relevant insbesondere für den Dienstleister selbst, der eine Datenverwertung betreibt.

## § 204 StGB

Verwertung fremder Geheimnisse zu eigenen Zwecken. Konkurrenznorm zu § 203 StGB für Fälle, in denen das Geheimnis nicht offenbart, sondern wirtschaftlich verwertet wird (etwa Modelltraining mit Mandatsdaten zu Wettbewerbszwecken).

## Anforderungen an die Belehrung

- Ausdrücklicher Verweis auf § 203 StGB und § 204 StGB im Vertrag
- Hinweis auf Strafandrohung Freiheitsstrafe bis zu einem Jahr oder Geldstrafe (Grundtatbestand)
- Hinweis auf gewerbsmäßige Variante (höhere Strafandrohung)
- Normtext idealerweise als Vertragsanlage
- Empfänger der Belehrung: der Dienstleister selbst und alle sonstigen mitwirkenden Personen (die der Dienstleister einbindet)

## Prüfschema

| Punkt | Fundstelle | Ampel | Bemerkung |
|---|---|---|---|
| Verweis auf § 203 StGB | | | |
| Verweis auf § 204 StGB | | | |
| Belehrung im Vertragstext | | | |
| Normtext als Anlage | | | |
| Belehrung umfasst auch Subunternehmer | | | |

## Typische Lücken

- Pauschaler Hinweis "strafbewehrte Verschwiegenheit" ohne Normnennung — unzureichend
- Belehrung nur auf englisch ohne deutsche Übersetzung — bei deutschem Anbieter problematisch
- Belehrung ausschließlich auf der Subunternehmer-Ebene, nicht beim Dienstleister selbst
- Keine Belehrung in den Mitarbeiterunterlagen des Dienstleisters

## Anlage Normtext (Vorlage)

Im Skill `klauselvorschlaege` befindet sich ein Mustertext der Anlage Normtext §§ 203, 204 StGB, der direkt in den Vertrag übernommen werden kann.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- § 203 Abs. 1, Abs. 3 Satz 2, Abs. 4, Abs. 6 StGB — Verletzung von Privatgeheimnissen
- § 204 StGB — Verwertung fremder Geheimnisse
- §§ 43e Abs. 3 Nr. 1 BRAO, 62a Abs. 3 Nr. 1 StBerG, 50a Abs. 3 Nr. 1 WPO, 39c Abs. 3 Nr. 1 PAO, 26a Abs. 3 Nr. 1 BNotO — Pflicht zur Belehrung in Textform

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Enthält der Dienstleistervertrag eine explizite Belehrung über §§ 203, 204 StGB?
2. Ist die Belehrung in Textform (§ 126b BGB) dokumentiert?
3. Wurde der Normtext der §§ 203/204 StGB als Anlage beigefügt?
4. Verpflichtet der Vertrag den Dienstleister, seine Subunternehmer ebenso zu belehren?
5. Erfasst die Belehrung § 203 Abs. 6 StGB (gewerbsmäßige Variante)?

## Output-Template — Belehrungsprüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Belehrungsprüfvermerk §§ 203/204 StGB [DATUM]
Anbieter: [NAME] | Vertrag: [DOKUMENT, VERSION]

Prüfpunkt 1: Belehrung im Vertrag
Vorhanden: ja / nein
Fundstelle: [KLAUSEL, ABSCHNITT]
Deckt ab: § 203 Abs. 1 / Abs. 3 Satz 2 / Abs. 4 / Abs. 6 / § 204

Prüfpunkt 2: Normtext als Anlage
Normtext §§ 203/204 StGB als Anlage beigefügt: ja / nein

Prüfpunkt 3: Weiterverpflichtung Subunternehmer
Vertrag verpflichtet Dienstleister zur Belehrung der Subunternehmer: ja / nein
Fundstelle: [KLAUSEL]

Ergebnis
Ampel strafrechtliche Belehrung: GRUEN / GELB / ROT
Luecken: [BESCHREIBUNG]
Handlungsbedarf: [ERGAENZUNGSKLAUSEL / RUECKFRAGE AN ANBIETER]
```
