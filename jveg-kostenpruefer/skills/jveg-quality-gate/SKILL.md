---
name: jveg-quality-gate
description: "Qualitaets-Gate fuer JVEG-Kostenberechnungen: Vollstaendigkeits- und Konsistenzpruefung aller Positionen. Normen: JVEG. Pruefraster: Vollstaendigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Pruefbericht JVEG. Abgrenzung: nicht Einzelberechnungs-Skill."
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
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Ein unvollständig belegter Vergütungsantrag kann nur für die belegten Positionen festgesetzt werden; fehlende Belege gehen zu Lasten des Antragstellers.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Die Überschreitung der Dreimonatsfrist führt zum Anspruchserlöschen; eine nachträgliche Korrektur im Beschwerdeverfahren ist nicht möglich.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Doppelte Abrechnung von Fahrt- und Reisezeiten ist offensichtlich unzulässig; das Gericht kürzt von Amts wegen.
4. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — Ein unklar formulierter Antrag ohne eindeutigen Zahlungsbetrag kann nicht festgesetzt werden; Nachbesserung erfordert neuen Antrag.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, § 4 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG § 4 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 4 Rn. 1 ff.

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
