---
name: german-agb-konforme
description: "AGB Konforme: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# AGB Konforme

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **AGB Konforme** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-german-fristen-form-und-zustaendigkeit` | German: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin word legal ai plugin and skill for german lawyers; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `agb-konforme-klauseln-305-310-bgb` | Drafting und Prüfung von Allgemeinen Geschäftsbedingungen nach §§ 305-310 BGB. Klärt den AGB-Begriff (vorformuliert, mehrfach verwendet, gestellt), Einbeziehung im Verbraucher- und Unternehmergeschäft sowie Inhaltskontrolle nach § 307 BGB Generalklausel und Transparenzgebot, § 308 BGB Klauselverbote mit Wertungsmöglichkeit und § 309 BGB Klauselverbote ohne Wertungsmöglichkeit. Behandelt die Ausstrahlungswirkung der Verbote des § 308 und § 309 BGB auf B2B-Verträge nach § 307 BGB. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **AGB Konforme**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-german-fristen-form-und-zustaendigkeit`

**Fokus:** German: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin word legal ai plugin and skill for german lawyers; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# German: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: German: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** German: Fristen, Form, Zuständigkeit und Rechtsweg / german fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AI, DE, EN, US, UK.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **German** prüfen.
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

## 2. `agb-konforme-klauseln-305-310-bgb`

**Fokus:** Drafting und Prüfung von Allgemeinen Geschäftsbedingungen nach §§ 305-310 BGB. Klärt den AGB-Begriff (vorformuliert, mehrfach verwendet, gestellt), Einbeziehung im Verbraucher- und Unternehmergeschäft sowie Inhaltskontrolle nach § 307 BGB Generalklausel und Transparenzgebot, § 308 BGB Klauselverbote mit Wertungsmöglichkeit und § 309 BGB Klauselverbote ohne Wertungsmöglichkeit. Behandelt die Ausstrahlungswirkung der Verbote des § 308 und § 309 BGB auf B2B-Verträge nach § 307 BGB.

# AGB-konforme Klauseln nach §§ 305-310 BGB

## Zweck

Dieser Skill unterstützt Sie beim Drafting und bei der Prüfung von AGB-Klauseln im Verbraucher- und Unternehmergeschäft. AGB-Recht ist Vorschaltprüfung jeder vorformulierten Klausel; Fehler hier führen zur Unwirksamkeit der Klausel und zur Geltung des dispositiven Rechts (§ 306 II BGB).

## Eingaben

- Vertragstyp und Branche.
- Vertragspartner (Verbraucher nach § 13 BGB, Unternehmer nach § 14 BGB, Kaufmann nach §§ 1 ff. HGB).
- Klauselzweck (Hauptleistung, Nebenleistung, Haftung, Beendigung).
- Bisheriger Klauseltext oder Drafting-Auftrag.
- Verwendungsumfeld (online, offline, Vertrieb durch Dritte).

## Rechtlicher und methodischer Rahmen

- **AGB-Definition § 305 I BGB:** Vorformuliert (für eine Vielzahl von Verträgen), gestellt (vom Verwender), Vereinbarung (Einbeziehung erforderlich). Auch einmalige Verwendung kann genügen, wenn vorformuliert und für mehrfache Verwendung gedacht.
- **Einbeziehung im Verbrauchergeschäft (§ 305 II BGB):** Ausdrücklicher Hinweis bei Vertragsschluss und zumutbare Möglichkeit der Kenntnisnahme; bei elektronischen AGB Online-Verfügbarkeit und Speicherbarkeit.
- **Einbeziehung im Unternehmergeschäft (§ 310 I BGB):** Erleichterte Einbeziehung; AGB werden Vertragsbestandteil bei rechtsgeschäftlicher Einbeziehung im Sinne der allgemeinen Regeln. § 305 II und III BGB gelten nicht. § 305c BGB (überraschende und mehrdeutige Klauseln) und §§ 307 bis 309 BGB sind anwendbar; § 308 und § 309 BGB jedoch nur "unter Berücksichtigung der im Handelsverkehr geltenden Gewohnheiten und Gebräuche" und mit Ausstrahlungswirkung über § 307 BGB.
- **§ 305c BGB:** Überraschende Klauseln (Überrumpelungsschutz) werden nicht Vertragsbestandteil; mehrdeutige Klauseln gehen zulasten des Verwenders.
- **§ 306 BGB:** Rechtsfolge der Unwirksamkeit. Nur die Klausel fällt weg, der Vertrag bleibt im Übrigen wirksam. Keine geltungserhaltende Reduktion (h. M.).
- **§ 306a BGB:** Umgehungsverbot.
- **§ 307 BGB:** Generalklausel. Unangemessene Benachteiligung entgegen Treu und Glauben; vermutet bei unklarer und unverständlicher Klausel (Transparenzgebot, § 307 I 2 BGB) und bei Abweichung vom wesentlichen Grundgedanken des dispositiven Rechts (§ 307 II Nr. 1 BGB).
- **§ 308 BGB:** Klauselverbote mit Wertungsmöglichkeit (Annahme- und Leistungsfristen, fingierte Erklärungen, Zugang fingiert, Rücktritt usw.). Im B2B grundsätzlich nicht direkt anwendbar, jedoch Ausstrahlung über § 307 BGB.
- **§ 309 BGB:** Klauselverbote ohne Wertungsmöglichkeit (Preiserhöhungen kurzfristig, Aufrechnungs- und Zurückbehaltungsausschluss, Haftung für grobe Fahrlässigkeit, Vertragsstrafe etc.). Im B2B nicht direkt anwendbar, Ausstrahlung über § 307 BGB ist nach BGH-Linie regelmäßig anzunehmen, im Einzelfall jedoch differenziert.
- **§ 310 BGB:** Ausnahmen vom Anwendungsbereich.

## Ablauf / Checkliste

1. AGB-Status feststellen: vorformuliert, mehrfach verwendet, gestellt? Auch Individualabrede in Teilen möglich (§ 305b BGB Vorrang).
2. Einbeziehung sicherstellen, dokumentieren, archivieren.
3. Überraschungstest (§ 305c BGB): Kein "Ausreißer" im Vertragsumfeld.
4. Transparenztest (§ 307 I 2 BGB): klar und verständlich, vgl. `transparenzgebot-307-bgb`.
5. Inhaltskontrolle gegen § 309 BGB (jede Verbotsnummer durchgehen).
6. Inhaltskontrolle gegen § 308 BGB.
7. Generalklausel § 307 BGB: wesentliche Grundgedanken, Aushöhlung zentraler Pflichten.
8. Für B2B: Ausstrahlungswirkung prüfen. Faustregel der BGH-Rechtsprechung: Wenn eine Klausel unter § 309 BGB im Verbrauchergeschäft eindeutig unzulässig wäre, ist sie auch im B2B regelmäßig nach § 307 BGB unwirksam, soweit nicht handelsbräuchliche Besonderheiten überwiegen.
9. Bei Konfliktfeldern (Haftungsbegrenzung, Verjährung, Aufrechnung, Vertragsstrafe, Beweislast) Sonderprüfung.
10. Dokumentation der Prüfung für Nachweispflichten gegenüber Mandant und ggf. Aufsichtsbehörden.

## Typische Drafting-Fehler

- "Mehrfachverwendungsabsicht ausgeschlossen": Verschleierungsversuch wirkt nicht; AGB-Status ergibt sich aus der Vorformulierung und der tatsächlichen Verwendung.
- Pauschale Haftungsausschlüsse "soweit gesetzlich zulässig": Verstoß gegen § 307 BGB Transparenzgebot.
- Aufrechnungsverbote ohne Ausnahme für unbestrittene oder rechtskräftig festgestellte Forderungen: § 309 Nr. 3 BGB.
- Pauschalierter Schadensersatz ohne Vorbehalt geringeren Schadens: § 309 Nr. 5 BGB.
- Vertragsstrafe in Verbraucher-AGB: § 309 Nr. 6 BGB.
- Geltungserhaltende Reduktion in salvatorischer Klausel: läuft leer.
- Schriftformklauseln in AGB, die strenger sind als § 126 BGB: kritisch (§ 309 Nr. 13 BGB).

## Ausgabeformat

- AGB-Set als Klauselkatalog mit Überschriften und Definitionen.
- Tabelle Klausel-Risiko-Alternative (Klausel, einschlägige Norm, Risiko, alternative Formulierung).
- Memo zur Einbeziehung, mit Hinweisen auf B2B-/B2C-Trennung (vgl. `b2b-vs-b2c-klausel-strategie`).
- Versionierung dokumentieren.

## Beispiel

Tabelle (Auszug, Haftungsbegrenzung):

| Klausel-Typ | Norm | Risiko | Alternative |
|---|---|---|---|
| "Haftung ist auf Vorsatz beschränkt" | § 309 Nr. 7 a/b BGB; § 307 BGB B2B | Unwirksam (Verletzung Leben Körper Gesundheit immer; grobe Fahrlässigkeit ebenfalls) | Haftung für Vorsatz und grobe Fahrlässigkeit unbeschränkt; für Verletzung Leben Körper Gesundheit unbeschränkt; im Übrigen bei einfacher Fahrlässigkeit nur bei Verletzung wesentlicher Vertragspflichten und der Höhe nach auf den vertragstypischen vorhersehbaren Schaden begrenzt. |
| "Aufrechnung ausgeschlossen" | § 309 Nr. 3 BGB | Unwirksam | Aufrechnung mit unbestrittenen oder rechtskräftig festgestellten Forderungen ist zulässig. |
| "Pauschalierter Schaden EUR 1000" ohne Vorbehalt | § 309 Nr. 5 BGB | Unwirksam | Pauschale Höhe; Recht des Vertragspartners zum Nachweis eines geringeren Schadens ausdrücklich vorbehalten. |

Mustertext (Einbeziehungsklausel, B2C-Onlineshop):

> Es gelten die nachfolgenden Allgemeinen Geschäftsbedingungen in der zum Zeitpunkt des Vertragsschlusses gültigen Fassung. Sie sind im Bestellprozess vor Vertragsschluss eingeblendet und können in lesbarer Form gespeichert und ausgedruckt werden. Mit Abgabe der Bestellung erklärt sich der Kunde mit der Geltung dieser Bedingungen einverstanden.

## Querverweise

- `transparenzgebot-307-bgb` – Vertiefung zur Verständlichkeit.
- `b2b-vs-b2c-klausel-strategie` – Trennung der Vertragswelten.
- `haftungsausschluss-und-haftungsbegrenzung` – AGB-Grenzen der Haftungsbegrenzung.
- `vertragsstrafe-339-bgb` – § 309 Nr. 6 BGB.
- `kuendigungsklauseln-und-vertragsbeendigung` – § 309 Nr. 9 BGB Laufzeiten in Dauerschuldverhältnissen.

## Quellen (Stand 05/2026)

- §§ 305, 305a, 305b, 305c, 306, 306a, 307, 308, 309, 310 BGB.
- §§ 13, 14 BGB (Verbraucher und Unternehmer).
- §§ 1 ff. HGB (Kaufmannseigenschaft).
- BGH-Rechtsprechung zur Ausstrahlungswirkung der §§ 308 und 309 BGB auf den B2B-Verkehr ist vom Nutzer fundstellengenau zu verifizieren.
- Zitierweise: `references/zitierweise.md`.
