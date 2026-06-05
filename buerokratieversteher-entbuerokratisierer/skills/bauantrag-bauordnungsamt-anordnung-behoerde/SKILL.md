---
name: bauantrag-bauordnungsamt-anordnung-behoerde
description: "Bauantrag Bauordnungsamt Anordnung Behoerde: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bauantrag Bauordnungsamt Anordnung Behoerde

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Bauantrag Bauordnungsamt Anordnung Behoerde** im Plugin Buerokratieversteher Entbuerokratisierer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bauantrag` | Erklärt Bauantrag, Bauvorbescheid, Nachbarbeteiligung, Unterlagen, Landesbauordnung und Fristen. |
| `bauordnungsamt-anordnung` | Hilft bei Nutzungsuntersagung, Beseitigungsverfügung, Baustopp, Anhörung, Sofortvollzug und Eilantrag. |
| `behoerde-oder-gericht-erkennen` | Ordnet Absender ein: Kommune, Landkreis, Landesbehörde, Bundesbehörde, Jobcenter, Jugendamt, Familiengericht, Polizei, Staatsanwaltschaft, Amtsgericht. |
| `beratungshilfe-pkh` | Erklärt Beratungshilfe, Prozesskostenhilfe/Verfahrenskostenhilfe, Unterlagen, Fristen und wann anwaltliche Hilfe nötig ist. |

## Arbeitsweg

Im Plugin Buerokratieversteher Entbuerokratisierer gilt für **Bauantrag Bauordnungsamt Anordnung Behoerde**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bauantrag`

**Fokus:** Erklärt Bauantrag, Bauvorbescheid, Nachbarbeteiligung, Unterlagen, Landesbauordnung und Fristen.

# Bauantrag

## Aufgabe
Erklärt Bauantrag, Bauvorbescheid, Nachbarbeteiligung, Unterlagen, Landesbauordnung und Fristen.

## Normfokus und Praxis
- Baurecht ist Landesrecht: Die 16 Landesbauordnungen unterscheiden sich (z. B. genehmigungsfreie Vorhaben, Abstandsflächen, Brandschutz). Immer LBO des konkreten Bundeslandes prüfen, daneben Bauplanungsrecht (§§ 29 ff. BauGB, BauNVO, ggf. Bebauungsplan oder § 34/§ 35 BauGB).
- Standard-Unterlagen: Lageplan, Bauzeichnungen, Baubeschreibung, Statik, Berechnung der Bruttogeschossfläche, Nachweis Stellplätze, Entwässerungsplan, ggf. Brandschutzkonzept; alles bauvorlageberechtigt unterzeichnet (LBO).
- Nachbarbeteiligung: Bauherr kann Nachbarunterschriften einholen (Verkürzung Klagefrist), sonst öffentliche Bekanntmachung; Widerspruchsfrist für nicht zugestimmte Nachbarn beachten.
- Bauvorbescheid (z. B. § 75 MBO): Schriftliche, verbindliche Vorabentscheidung zu Einzelfragen, drei Jahre bindend; günstig bei strittigem Maß der Nutzung.
- Praktiker-Tipp: Vor Antrag formloses Bauamtsgespräch und ggf. Vorbescheid; Genehmigungsfiktion (§ 42a VwVfG, ggf. landesrechtlich) nur bei vollständigen Unterlagen — Eingangsbestätigung mit Datum sichern.

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

## 2. `bauordnungsamt-anordnung`

**Fokus:** Hilft bei Nutzungsuntersagung, Beseitigungsverfügung, Baustopp, Anhörung, Sofortvollzug und Eilantrag.

# Bauordnungsamt-Anordnung

## Aufgabe
Hilft bei Nutzungsuntersagung, Beseitigungsverfügung, Baustopp, Anhörung, Sofortvollzug und Eilantrag.

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

## 3. `behoerde-oder-gericht-erkennen`

**Fokus:** Ordnet Absender ein: Kommune, Landkreis, Landesbehörde, Bundesbehörde, Jobcenter, Jugendamt, Familiengericht, Polizei, Staatsanwaltschaft, Amtsgericht.

# Behörde oder Gericht erkennen

## Aufgabe
Ordnet Absender ein: Kommune, Landkreis, Landesbehörde, Bundesbehörde, Jobcenter, Jugendamt, Familiengericht, Polizei, Staatsanwaltschaft, Amtsgericht.

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

## 4. `beratungshilfe-pkh`

**Fokus:** Erklärt Beratungshilfe, Prozesskostenhilfe/Verfahrenskostenhilfe, Unterlagen, Fristen und wann anwaltliche Hilfe nötig ist.

# Beratungshilfe und PKH

## Aufgabe
Erklärt Beratungshilfe, Prozesskostenhilfe/Verfahrenskostenhilfe, Unterlagen, Fristen und wann anwaltliche Hilfe nötig ist.

## Normfokus und Praxis
- Beratungshilfe nach BerHG: außergerichtliche Beratung/Vertretung, Antrag beim Amtsgericht am Wohnsitz (§ 4 BerHG); Mandantenanteil derzeit 15 Euro Eigenbeitrag, sonst staatlich getragen.
- PKH/VKH: §§ 114 ff. ZPO (Zivilprozess), § 76 FamFG (VKH Familienverfahren), § 166 VwGO (Verwaltungsgericht), § 73a SGG (Sozialgericht), § 142 FGO (Finanzgericht). Voraussetzungen: persönliche und wirtschaftliche Bedürftigkeit + hinreichende Erfolgsaussicht und nicht mutwillig (§ 114 Abs. 1 ZPO).
- Unterlagen: Formular "Erklärung über die persönlichen und wirtschaftlichen Verhältnisse" (gerichtliches Vordruck), aktuelle Einkommensnachweise, Mietvertrag, Kontoauszüge der letzten Monate, Schuldenliste.
- Ratenzahlung möglich nach § 115 Abs. 2 ZPO; Überprüfung nach vier Jahren (§ 120a ZPO), Rückforderung bei wirtschaftlicher Besserung.
- Praktiker-Tipp: PKH-Antrag immer **zusammen** mit Klage oder rechtzeitig vor Fristablauf — bei abgelehnter PKH kann unter Umständen Wiedereinsetzung in den vorigen Stand (§ 60 VwGO, § 233 ZPO) beantragt werden. Vorab Anwaltsbesuch mit Beratungshilfeschein klären.

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
