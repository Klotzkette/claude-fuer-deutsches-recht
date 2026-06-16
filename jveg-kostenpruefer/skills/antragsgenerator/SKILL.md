---
name: antragsgenerator
description: "Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach JVEG. Abgrenzung: nicht Beschwerde gegen Festsetzung im Jveg Kostenpruefer."
---

# JVEG-Antragsgenerator

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: JVEG-Antragsgenerator
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Triage — kläre vor der Erstellung

1. **Antragsart:** Vorschuss (§ 3 JVEG), Nachzahlung, Festsetzungsantrag (§ 4 JVEG) oder Ergänzungsantrag?
2. **Anspruchsberechtigter:** Sachverständiger, Zeuge, Dolmetscher oder Übersetzer?
3. **Fristen:** Ist die Dreimonatsfrist des § 23 JVEG noch nicht abgelaufen?
4. **Beleglage:** Welche Belege (Fahrtkosten, Zeitnachweise, Rechnungen) liegen vor und sollen beigefügt werden?
5. **Vorschussstand:** Wurde bereits ein Vorschuss gewährt — wie hoch und wann ausgezahlt?

## Zentrale Normen
- § 3 JVEG (Vorschuss)
- § 4 JVEG (Festsetzung durch das Gericht)
- § 4 Abs. 3 JVEG (Beschwerde gegen Festsetzungsbeschluss)
- § 23 JVEG (Dreimonatsfrist / Erlöschen)
- §§ 5–7 JVEG (Fahrtkosten)
- §§ 8–10 JVEG (Sachverständige)
- §§ 13–16 JVEG (Dolmetscher/Übersetzer)
- §§ 19–22 JVEG (Zeugen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Startet bei
Mandant oder Sachverständiger möchte JVEG-Vergütung gerichtlich festsetzen lassen oder Vorschuss beantragen.

## Output-Template

**[Gericht / Kostenbeamter]**
**Az.:** [Aktenzeichen]
**Datum:** [TT.MM.JJJJ]

**Antrag auf [Festsetzung / Vorschuss / Nachzahlung] nach JVEG**

Ich beantrage die Festsetzung folgender Vergütung:

| Position | Betrag (EUR) | Norm | Anlage |
|---|---|---|---|
| [Position] | 00,00 | § X JVEG | Anlage [Nr.] |
| **Gesamtbetrag** | **00,00** | | |

Belege: [Liste der Anlagen]
Fristwahrung § 23 JVEG: Leistung erbracht am [Datum]; Antrag fristgerecht.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Ausgabe
Druckfertiges Antragsschreiben mit Positionsliste, Normenbezug und Anlagenliste.

## Leitplanken
- Kein Schreiben ohne geprüfte Fristen (§ 23 JVEG).
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 5 JVEG
- § 23 JVEG
- § 4 JVEG
- § 8a JVEG
- § 2 JVEG
- § 3 JVEG
- § 7 JVEG
- § 9 JVEG
- § 6 JVEG
- § 12 JVEG
- § 8 JVEG
- § 22 JVEG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
