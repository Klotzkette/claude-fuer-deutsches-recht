---
name: jveg-quality-gate
description: "Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht JVEG. Abgrenzung: nicht Einzelberechnungs-Skill."
---

# JVEG-Quality-Gate

## Aufgabe
Führe eine abschließende Qualitätsprüfung aller JVEG-Dokumente durch, bevor sie versandt oder eingereicht werden.

## Triage — kläre vor der Prüfung

1. **Dokumenttyp:** Welches Dokument wird geprüft — Antrag, Rechenblatt, Beschwerdeschrift oder Antwortschreiben?
2. **Mathcheck:** Sind alle Rechenoperationen (Summen, Teilbeträge) nachvollziehbar und korrekt?
3. **Belegcheck:** Sind alle zitierten Belege tatsächlich als Anlage beigefügt?
4. **Doppelposten:** Wird dieselbe Position doppelt abgerechnet (z.B. Reisezeit und Wartezeit überschneidend)?
5. **Ton und Antrag:** Ist der Antragssatz eindeutig formuliert, ohne missverständliche Alternativen?

## Speziallogik: Stopp bei roten Punkten
Das Quality Gate stoppt den Prozess, wenn folgende rote Punkte erkannt werden:
- Rechenfehlerin der Summenzeile.
- Fehlender Pflichtbeleg (§ 5, § 11, § 16 JVEG).
- Überschreitung der Dreimonatsfrist ohne Wiedereinsetzungsantrag.
- Doppelabrechnung einer Position.
- Unklar formulierter oder fehlender Antrag.

## Zentrale Normen
- § 4 JVEG (Festsetzungsantrag — Formerfordernis)
- § 23 JVEG (Dreimonatsfrist)
- § 8 JVEG (Sachverständigenvergütung — Berechnung)
- § 5 JVEG (Fahrtkosten — Belegpflicht)
- § 16 JVEG (Übersetzer — Zeilennachweise)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Jedes fertiggestellte JVEG-Dokument vor Versand.

## Arbeitsweise
1. Mathcheck: Alle Summen nachrechnen.
2. Belegcheck: Anlagenliste mit Belegen abgleichen.
3. Doppelpostencheck: Jede Position auf Überschneidung prüfen.
4. Fristcheck: § 23 JVEG-Frist bestätigen.
5. Antragssatz prüfen: eindeutig, vollständig, mit Betrag.
6. Bei rotem Punkt: Prozess stoppen und Fehler benennen.

## Output-Template

| Prüfpunkt | Status | Befund |
|---|---|---|
| Mathcheck | Gruen / Rot | [Befund] |
| Belegcheck | Gruen / Rot | [Befund] |
| Doppelposten | Gruen / Rot | [Befund] |
| Fristcheck § 23 JVEG | Gruen / Rot | [Befund] |
| Antragssatz | Gruen / Rot | [Befund] |
| **Gesamtergebnis** | **Gruen / Rot** | [Freigabe / Stopp] |

## Ausgabe
Qualitätsbericht mit Ampelstatus; roter Punkt hält Dokument zurück.

## Leitplanken
- Freigabe erst nach vollständig grünem Prüfbericht.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
