---
name: spanisch-modus-staatsangehoerigkeit-gebiet
description: "Spanisch Modus Staatsangehoerigkeit Gebiet im Migrationsrecht: prüft konkret Spanisch-Modus Migrationsrecht, Staatsangehörigkeit/Gebiet/Status. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Spanisch Modus Staatsangehoerigkeit Gebiet

## Arbeitsbereich

**Spanisch Modus Staatsangehoerigkeit Gebiet** ordnet den Fall über die tragenden Prüfungslinien: Spanisch-Modus Migrationsrecht, Staatsangehörigkeit/Gebiet/Status. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-spanisch-modus-migration` | Spanisch-Modus Migrationsrecht: Prüfungslinie für Migrationsrecht; liefert spanische Erklärungen mit deutschem Rechtskern und klarer Dokumentenliste; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-staatsangehoerigkeit-gebiet-status` | Staatsangehörigkeit/Gebiet/Status: Prüfungslinie für Migrationsrecht; klärt Staatenlosigkeit, umstrittene Gebiete, Mehrstaatigkeit und Dokumentenlage; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AsylG §§ 13-19, 24-26a, 27-30, 71-74, 77; AufenthG §§ 4, 5, 7-9, 16a-d, 18a-c, 19-21, 28-36, 53-55, 60, 81, 95; AufenthG, AsylG, FreizügG/EU, StAG; AufenthG § 18b Abs. 2, § 18g, EU-Richtlinie 2021/1883; Dublin-III-VO (EU) 604/2013 Art. 3, 7-15, 17, 21-23, 29; StAG §§ 8, 9, 10, 11, 12a, 13, 16, 17, 25, 30; AufenthG §§ 18, 18a, 18b, 18c, 18d, 18g, 19c, FachkräfteEG 2023; AufenthG §§ 27-36; EU-Asylpaket (GEAS-Reform 2024): Asylverfahrens-VO, Asylkrisen-VO, Eurodac, AMMR; Genfer Flüchtlingskonvention Art. 1A, 31, 33; StAG §§ 4, 5, 8-17, 25, 27, 30; AufenthG, AsylG, StAG, FreizügG/EU, AsylbLG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-spanisch-modus-migration`

**Fokus:** Spanisch-Modus Migrationsrecht: Prüfungslinie für Migrationsrecht; liefert spanische Erklärungen mit deutschem Rechtskern und klarer Dokumentenliste; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Spanisch-Modus Migrationsrecht

## Aufgabe
Prüfungslinie im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: liefert spanische Erklärungen mit deutschem Rechtskern und klarer Dokumentenliste.

## Einstieg
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `workflow-staatsangehoerigkeit-gebiet-status`

**Fokus:** Staatsangehörigkeit/Gebiet/Status: Prüfungslinie für Migrationsrecht; klärt Staatenlosigkeit, umstrittene Gebiete, Mehrstaatigkeit und Dokumentenlage; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Staatsangehörigkeit/Gebiet/Status

## Aufgabe
Prüfungslinie im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: klärt Staatenlosigkeit, umstrittene Gebiete, Mehrstaatigkeit und Dokumentenlage.

## Einstieg
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
