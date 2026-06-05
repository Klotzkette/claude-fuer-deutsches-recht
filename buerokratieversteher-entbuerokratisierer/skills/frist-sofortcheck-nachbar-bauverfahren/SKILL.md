---
name: frist-sofortcheck-nachbar-bauverfahren
description: "Frist Sofortcheck Nachbar Bauverfahren: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Frist Sofortcheck Nachbar Bauverfahren

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Frist Sofortcheck Nachbar Bauverfahren** im Plugin Buerokratieversteher Entbuerokratisierer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `frist-sofortcheck` | Fristen-Sofortcheck bei Bescheiden: Zugangsfiktion, Monatsfrist, Rechtsbehelfsbelehrung, fehlerhafte Belehrung, Sofortmassnahmen vor Fristablauf, Berechnung nach VwVfG und ZPO. |
| `nachbar-im-bauverfahren` | Erklärt Nachbarrechte, Akteneinsicht, Einwendungen, Frist, Rücksichtnahme und Widerspruch/Klage. |
| `bussgeld-anhoerung` | Erklärt Anhörungsbogen, Betroffener, Aussageverweigerung, Fahrerfrage, Fristen und Einspruch. |
| `gewerbeanmeldung` | Hilft bei Gewerbeanmeldung, Erlaubnissen, IHK/HWK, Steuernummer, Nebengewerbe und Auflagen. |

## Arbeitsweg

Im Plugin Buerokratieversteher Entbuerokratisierer gilt für **Frist Sofortcheck Nachbar Bauverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `frist-sofortcheck`

**Fokus:** Fristen-Sofortcheck bei Bescheiden: Zugangsfiktion, Monatsfrist, Rechtsbehelfsbelehrung, fehlerhafte Belehrung, Sofortmassnahmen vor Fristablauf, Berechnung nach VwVfG und ZPO.

# Frist Sofortcheck

## Worum geht es konkret
Behoerden setzen Fristen oder lassen Fristen entstehen (Rechtsbehelf, Aeusserung, Klage, Antrag). Wer Fristen versaeumt, verliert oft den Anspruch oder den Bescheid wird bestandskraeftig. Der Skill rechnet die Frist nach und schlaegt Sofortmassnahmen vor.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welches Dokument liegt vor (Bescheid, Anhoerungsschreiben, Mahnung, Gerichtsverfuegung)?
- Ist Rechtsbehelfsbelehrung vorhanden und korrekt?
- Welches Datum traegt das Dokument, wann ist es zugegangen (Zugangsfiktion + 3 Werktage)?
- Welche Frist ist erkennbar (1 Monat, 2 Wochen, 1 Jahr bei fehlerhafter Belehrung)?
- Soll Widerspruch, Klage, Anhoerungsantwort oder Antrag abgegeben werden?

## Rechtlicher Rahmen
- **VwVfG § 31** Berechnung Fristen; § 41 Bekanntgabe; § 41 Abs. 2 Zugangsfiktion + 3 Werktage.
- **VwGO §§ 58, 70, 74** Rechtsbehelfsbelehrung, Widerspruchs-/Klagefrist; § 58 Abs. 2 Jahresfrist bei fehlender oder fehlerhafter Belehrung.
- **SGG § 66** und **AO § 356** entsprechende Vorschriften fuer Sozial-/Steuersachen.
- **ZPO §§ 222 ff., BGB §§ 187, 188** Fristenberechnung (entsprechend).
- **Wiedereinsetzung** § 60 VwGO, § 32 VwVfG.

## / Schritt fuer Schritt
1. **Dokument datieren:** Bescheiddatum, Datum Posteingang/Zustellung.
2. **Zugang ermitteln:** Bei einfachem Brief Zugangsfiktion 3 Werktage nach Absendung (§ 41 Abs. 2 VwVfG). Bei Zustellung: tatsaechlicher Tag der Zustellung.
3. **Rechtsbehelfsbelehrung pruefen:** Vorhanden? Inhaltlich korrekt (Form, Frist, Behoerde/Gericht)? Bei Fehlern Jahresfrist § 58 Abs. 2 VwGO.
4. **Fristlauf berechnen:** Monatsfrist beginnt mit dem Tag nach Zugang (§ 187 BGB); Ende mit Ablauf des entsprechenden Tages im Folgemonat (§ 188 BGB). Faellt der Ablauftag auf Sa/So/Feiertag, verschiebt sich auf naechsten Werktag (§ 31 Abs. 3 VwVfG).
5. **Sofortmassnahmen:** Fristwahrenden Widerspruch/Klage formulieren, Begruendung kann nachgereicht werden.
6. **Wiedereinsetzungspruefung** bei abgelaufener Frist: unverschuldetes Versaeumnis, Antrag binnen 2 Wochen ab Wegfall des Hindernisses.

## Trade-off-Matrix

| Lage | Massnahme | Effekt |
|---|---|---|
| Frist klar, 1 Monat | Widerspruch/Klage einlegen | Erhalt Rechtsbehelf |
| Rechtsbehelfsbelehrung fehlt/fehlerhaft | Jahresfrist nutzen, aber zuegig handeln | rechtssicher |
| Frist abgelaufen | Wiedereinsetzung pruefen | unsicher, oft scheitert |
| Anhoerungsfrist | Stellungnahme einreichen | Bescheid abwenden |
| Zustellungsfrage offen | Beweissicherung Postfach/Briefkasten | Beweisproblem |

## Praxistipps
- Drei-Tages-Fiktion gilt nur bei Brief; bei Zustellungsurkunde/Einschreiben mit Rueckschein das tatsaechliche Datum.
- Eintrifft am Wochenende: § 31 Abs. 3 VwVfG verschiebt Fristende, nicht aber den Beginn.
- E-Mail-Bescheid: § 3a VwVfG; Behoerde muss elektronischen Zugang eroeffnet haben.
- Bei Zweifeln immer fristwahrend einlegen — Begruendung kann nachgereicht werden.
- Sicherer Weg: Einwurf-Einschreiben oder elektronisches Anwaltspostfach (beA).

## Mustertexte
**Fristwahrender Widerspruch:**
> Sehr geehrte Damen und Herren, gegen Ihren Bescheid vom [Datum], Aktenzeichen [Az.], zugestellt am [Datum], lege ich hiermit fristwahrend Widerspruch ein. Eine Begruendung wird nachgereicht. Wir bitten um Eingangsbestaetigung.

**Fristen-Schnellrechner (Beispiel):**
> Bescheiddatum 03.06.2026, abgesendet 03.06., Zugang fiktiv 06.06.2026 (3 Werktage). Monatsfrist beginnt 07.06.2026. Fristablauf 06.07.2026 (Mo). Letzter Tag fuer Widerspruch: 06.07.2026 24:00 Uhr.

**Wiedereinsetzungsantrag:**
> Hilfsweise wird Wiedereinsetzung in den vorigen Stand gemaess § 60 VwGO beantragt. Begruendung: …. Wir versichern an Eides Statt, dass …. Antrag binnen 2 Wochen ab Wegfall des Hindernisses.

## Typische Fehler
- Bescheiddatum mit Zugang gleichsetzen.
- Drei-Tages-Fiktion ueber Wochenende falsch berechnet.
- Rechtsbehelfsbelehrung nicht gepruegt (Fehler → 1-Jahresfrist).
- Widerspruch bei Behoerde eingereicht, die nicht zustaendig ist (zur Niederschrift bei jeder Behoerde moeglich, aber Zustaendigkeitsweiterleitung sicherer).
- Nachts vor Mitternacht eingeworfen, ohne Zeugen — Beweisproblem.

## Querverweise
- `widerspruch-einfach`
- `eilantrag-notfall`
- `bescheid-ohne-rechtsbehelf`
- `was-will-dieses-schreiben`
- `klage-verwaltungsgericht-einfach`
- `untaetigkeit-behoerde`

## Quellen Stand 06/2026
- VwVfG §§ 31, 41.
- VwGO §§ 58, 60, 70, 74.
- SGG § 66; AO § 356.
- BGB §§ 187, 188.
- BVerwG, staend. Rspr. zu Rechtsbehelfsbelehrung und Wiedereinsetzung.

## 2. `nachbar-im-bauverfahren`

**Fokus:** Erklärt Nachbarrechte, Akteneinsicht, Einwendungen, Frist, Rücksichtnahme und Widerspruch/Klage.

# Nachbar im Bauverfahren

## Aufgabe
Erklärt Nachbarrechte, Akteneinsicht, Einwendungen, Frist, Rücksichtnahme und Widerspruch/Klage.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 3. `bussgeld-anhoerung`

**Fokus:** Erklärt Anhörungsbogen, Betroffener, Aussageverweigerung, Fahrerfrage, Fristen und Einspruch.

# Bußgeld-Anhörung

## Aufgabe
Erklärt Anhörungsbogen, Betroffener, Aussageverweigerung, Fahrerfrage, Fristen und Einspruch.

## Normfokus und Praxis
- Rechtsgrundlagen: § 55 OWiG (Anhörung Betroffener), § 46 Abs. 1 OWiG iVm §§ 136 Abs. 1 Satz 2, 163a StPO (Schweigerecht), § 67 OWiG (Einspruch gegen Bußgeldbescheid, Frist zwei Wochen).
- Anhörungsbogen vs. Zeugenfragebogen unterscheiden: Als Betroffener besteht keine Pflicht zur Selbstbelastung — Personalien (§ 111 OWiG) jedoch angeben. Als Zeuge gilt Wahrheitspflicht, aber Auskunftsverweigerungsrecht nach § 55 StPO (Selbstbelastung) und § 52 StPO (Angehörige).
- Fahrerermittlung: Bei nicht zuzuordnender Tat droht Fahrtenbuchauflage (§ 31a StVZO) — Behörde muss zuvor angemessen ermittelt haben. Foto im Bußgeldbescheid genau prüfen.
- Verjährung: regelmäßig drei Monate nach § 26 Abs. 3 StVG bei Verkehrsordnungswidrigkeiten, unterbrochen durch Anhörung (§ 33 OWiG); nach Bescheid sechs Monate.
- Praktiker-Tipp: Bei unklarer Identifikation oder Messunsicherheit keine Angaben machen; Akteneinsicht nach § 49 OWiG iVm § 147 StPO (über Anwalt). Einspruch kann ohne Begründung eingelegt werden, Beschränkung auf Rechtsfolgen möglich (§ 67 Abs. 2 OWiG).

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 4. `gewerbeanmeldung`

**Fokus:** Hilft bei Gewerbeanmeldung, Erlaubnissen, IHK/HWK, Steuernummer, Nebengewerbe und Auflagen.

# Gewerbeanmeldung

## Aufgabe
Hilft bei Gewerbeanmeldung, Erlaubnissen, IHK/HWK, Steuernummer, Nebengewerbe und Auflagen.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.
