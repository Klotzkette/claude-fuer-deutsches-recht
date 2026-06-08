---
name: aktenstripper
description: "JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter Datensatz für Kostenprüfung. Abgrenzung: nicht Kostenberechnung im Jveg Kostenpruefer."
---

# JVEG-Aktenstripper

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: JVEG-Aktenstripper
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Triage — kläre vor dem Ausstreifen

1. **Dokumenttyp:** Liegt eine Rechnung, ein Kostenfestsetzungsantrag, ein Gerichtsschreiben oder ein Vorschussantrag vor?
2. **Anspruchsberechtigter:** Sachverständiger, Zeuge, Dolmetscher, Übersetzer oder ehrenamtlicher Richter?
3. **Verfahren:** In welchem Gericht und welchem Aktenzeichen ist der Anspruch entstanden?
4. **Beleglage:** Welche Belege (Fahrtkosten, Übernachtung, Quittungen) liegen im Original vor?
5. **Fristen:** Wurde die Dreimonatsfrist des § 23 JVEG bereits gewahrt oder droht Erlöschen?

## Zentrale Normen
- § 1 JVEG (Anwendungsbereich)
- § 2 JVEG (Anspruchsberechtigte)
- § 3 JVEG (Vorschuss)
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
Erhalt von Gerichtsschreiben, Rechnung oder Antrag im JVEG-Kontext.

## Output-Template

| Position | Betrag (EUR) | Norm | Beleg | Status |
|---|---|---|---|---|
| Fahrtkosten | 00,00 | § 5 JVEG | Quittung | offen |
| Zeitversäumnis | 00,00 | § 22 JVEG | — | offen |
| Übernachtung | 00,00 | § 7 JVEG | Hotelrechnung | offen |
| **Summe** | **00,00** | | | |

**Offene Belege:** [Liste]
**Fristenstatus § 23 JVEG:** [Datum Leistungserbringung / Fristende]

## Ausgabe
Strukturierte JVEG-Datenmatrix; jede Position mit Norm, Betrag und Belegnummer.

## Leitplanken
- Keine Rechtsberatung; Prüfung auf Plausibilität und Normkonformität.
- Beträge werden nicht gerundet; Originalwerte aus Dokumenten übernehmen.
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

