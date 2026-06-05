---
name: strukturierter-strafprozess-modus
description: "Strukturierter Strafprozess Modus: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Strukturierter Strafprozess Modus

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Strukturierter Strafprozess Modus** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-strukturierter-erstpruefung-und-mandatsziel` | Strukturierter: Erstprüfung, Rollenklärung und Mandatsziel im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `strafprozess-modus` | Aktenauszug für StPO-Verfahren erstellen: Anklage Hauptverhandlung Revision §§ 333 ff. StPO Wiederaufnahme. Anklageschrift Eroeffnungsbeschluss Beweisantragsrecht Rechtsmittelfristen. Normen StPO §§ 200 203 333 359 BGH-Leitsaetze StPO. Prüfraster StPO-spezifische Besonderheiten Verfahrenschronologie Rechtsmittel. Output StPO-spezifischer Aktenauszug. Abgrenzung zu zivilprozess-modus (ZPO) und verwaltungsprozess-modus (VwGO). |
| `verwaltungsprozess-modus` | Aktenauszug für VwGO-Verfahren erstellen: Anfechtungs- Verpflichtungsklage Berufung § 124 VwGO Revision § 132 VwGO Eilrechtsschutz §§ 80 123 VwGO. Normen VwGO §§ 40 42 80 113 124 132. Prüfraster VwGO-spezifische Fristen Vorverfahren Widerspruchsbescheid. Output VwGO-spezifischer Aktenauszug. Abgrenzung zu zivilprozess-modus (ZPO) und strafprozess-modus (StPO). |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Strukturierter Strafprozess Modus**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-strukturierter-erstpruefung-und-mandatsziel`

**Fokus:** Strukturierter: Erstprüfung, Rollenklärung und Mandatsziel im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Strukturierter: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Strukturierter: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Strukturierter: Erstprüfung, Rollenklärung und Mandatsziel / strukturierter erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Strukturierter** prüfen.
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

## 2. `strafprozess-modus`

**Fokus:** Aktenauszug für StPO-Verfahren erstellen: Anklage Hauptverhandlung Revision §§ 333 ff. StPO Wiederaufnahme. Anklageschrift Eroeffnungsbeschluss Beweisantragsrecht Rechtsmittelfristen. Normen StPO §§ 200 203 333 359 BGH-Leitsaetze StPO. Prüfraster StPO-spezifische Besonderheiten Verfahrenschronologie Rechtsmittel. Output StPO-spezifischer Aktenauszug. Abgrenzung zu zivilprozess-modus (ZPO) und verwaltungsprozess-modus (VwGO).

# Strafprozess-Modus (StPO)

## Zweck

Dieser Modus-Skill aktiviert die verfahrensspezifischen Einstellungen für Strafverfahren nach der Strafprozessordnung (StPO). Strafakten haben eine andere Struktur als Zivilakten — Ermittlungsakte, Anklageschrift, Hauptverhandlungsprotokoll und Urteil sind die zentralen Dokumente.

## Triage — kläre vor Aktivierung des Modus

1. Stadium: Ermittlungsverfahren / Zwischenverfahren / Hauptverhandlung / Rechtsmittelverfahren?
2. Ist der Mandant Beschuldigter / Angeklagter / Nebenkläger / Zeuge?
3. Besteht Untersuchungshaft? (Haftverlängerungsbeschlüsse und Haftdauer hervorheben!)
4. Welche Revisionsrügen sind geplant oder bereits erhoben?
5. Liegt ein Beweisantrag nach § 244 StPO vor oder ist einer geplant?

## Zentrale Normen (StPO)

- §§ 160-170 StPO — Ermittlungsverfahren (Ermittlungsauftrag der StA, Einstellung, Anklage)
- § 200 StPO — Inhalt der Anklageschrift (wesentliches Ergebnis der Ermittlungen)
- §§ 226-275 StPO — Hauptverhandlung (Eröffnung, Vernehmung, Beweisaufnahme, Schluss)
- § 244 Abs. 2 StPO — Aufklärungspflicht des Gerichts; § 244 Abs. 3-6 StPO — Beweisantragsrecht
- §§ 333-358 StPO — Revision; § 341 StPO — Revisionsfrist 1 Woche; § 345 — Begründungsfrist 1 Monat
- §§ 314-332 StPO — Berufung (Landgericht als Berufungsgericht)
- §§ 112-130 StPO — Untersuchungshaft (Haftgründe, Haftprüfung, Haftverschonung)

## Rechtsprechung (BGH — Leitsätze Strafprozessrecht)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Typischer Verfahrensablauf

1. Ermittlungsverfahren (Staatsanwaltschaft / Polizei)
2. Anklageschrift der Staatsanwaltschaft
3. Zwischenverfahren — Eröffnungsbeschluss (§ 207 StPO)
4. Terminsladung zur Hauptverhandlung
5. Hauptverhandlung (§§ 226 ff. StPO)
6. Urteilsverkündung
7. Rechtsmittel (Berufung oder Revision)

## Besonderheiten der Strafakte

### Ermittlungsakte

Die Ermittlungsakte umfasst Vernehmungsprotokolle, Observationsberichte, Beschlagnahmeverzeichnisse, Gutachten der Ermittlungsbehörden und sonstige Beweismittel. Sie bildet die Grundlage der Anklage.

**Im Aktenauszug:**

- Umfang der Ermittlungsakte (Bände und Blätter)
- Wesentliche Ermittlungsschritte (Durchsuchungen, Festnahmen, TKÜ)
- Sachverständigengutachten der Ermittlungsbehörden

### Anklageschrift

**Zu erfassen:**

- Anklagebehörde und Datum
- Angeklagte mit vollständigen Personalien
- Vorgeworfene Taten mit Tatzeit Tatort und Norm
- Wesentliches Ergebnis der Ermittlungen (§ 200 Abs. 2 StPO)

### Hauptverhandlung

- Termine mit Verhandlungsdauer und wesentlichem Inhalt
- Beweisanträge der Verteidigung (§ 244 StPO)
- Ablehnungsbeschlüsse des Gerichts
- Zeugenaussagen (kurze Zusammenfassung)
- Sachverständige in der Hauptverhandlung

## Kritische Fristen (StPO)

| Frist | Norm | Dauer |
|---|---|---|
| Revisionsfrist | § 341 StPO | 1 Woche ab Urteilsverkündung |
| Revisionsbegründungsfrist | § 345 StPO | 1 Monat ab Zustellung Urteil |
| Berufungsfrist | § 314 StPO | 1 Woche ab Urteilsverkündung |
| Haftprüfungsantrag | § 117 StPO | jederzeit |

**Besondere Hervorhebung:** Die Revisionsfrist von einer Woche ab Urteilsverkündung ist eine der kürzesten Fristen im deutschen Prozessrecht und wird im Aktenauszug besonders prominent hervorgehoben.

## Wiederaufnahme (§§ 359 ff. StPO)

Gesondert darzustellen:
- Wiederaufnahmegrund (§ 359 Nrn. 1 bis 6 StPO)
- Neue Tatsachen oder Beweismittel
- Vorheriger Verfahrensverlauf

## Besonderheiten im Aktenauszug

- Parteibezeichnungen: "Angeklagter", "Staatsanwaltschaft", "Nebenkläger"
- Keine Schuldvermutung im Aktenauszug
- Freispruch und Verurteilung neutral darstellen
- Bei laufender Untersuchungshaft: Haftverlängerungsbeschlüsse und Haftdauer hervorheben

## 3. `verwaltungsprozess-modus`

**Fokus:** Aktenauszug für VwGO-Verfahren erstellen: Anfechtungs- Verpflichtungsklage Berufung § 124 VwGO Revision § 132 VwGO Eilrechtsschutz §§ 80 123 VwGO. Normen VwGO §§ 40 42 80 113 124 132. Prüfraster VwGO-spezifische Fristen Vorverfahren Widerspruchsbescheid. Output VwGO-spezifischer Aktenauszug. Abgrenzung zu zivilprozess-modus (ZPO) und strafprozess-modus (StPO).

# Verwaltungsprozess-Modus (VwGO)

## Zweck

Dieser Modus-Skill aktiviert die verfahrensspezifischen Einstellungen für Verwaltungsgerichtsverfahren nach der Verwaltungsgerichtsordnung (VwGO). Verwaltungsverfahren sind durch das obligatorische Vorverfahren und die besondere Stellung der Behörde als Beklagte geprägt.

## Triage — kläre vor Aktivierung des Modus

1. Liegt ein Widerspruchsbescheid vor? (Klagefrist 1 Monat ab Zustellung — § 74 VwGO!)
2. Welche Klageart ist einschlägig? (Anfechtung, Verpflichtung, Feststellung, allgemeine Leistungsklage)
3. Hat die Klage aufschiebende Wirkung oder besteht sofortige Vollziehbarkeit? (§ 80 VwGO)
4. Eilrechtsschutz erforderlich? (§ 80 Abs. 5 VwGO oder § 123 VwGO)
5. Ist Berufungszulassung erforderlich und welcher Zulassungsgrund liegt vor (§ 124 VwGO)?

## Zentrale Normen (VwGO)

- §§ 42-43 VwGO — Anfechtungs-, Verpflichtungs- und Feststellungsklage; Klagebefugnis
- §§ 68-70 VwGO — Widerspruchsverfahren; Widerspruchsfrist 1 Monat
- § 74 VwGO — Klagefrist 1 Monat ab Zustellung Widerspruchsbescheid
- § 80 VwGO — Aufschiebende Wirkung; § 80 Abs. 5 VwGO — Antrag auf Anordnung / Wiederherstellung
- § 123 VwGO — Einstweilige Anordnung bei Verpflichtungs- und Leistungsklagen
- §§ 124-124a VwGO — Berufungszulassung und Berufungsbegründung
- § 132 VwGO — Revisionszulassung (Divergenz, Grundsatzbedeutung, Verfahrensmangel)
- § 58 Abs. 2 VwGO — Jahresfrist bei fehlerhafter Rechtsbehelfsbelehrung

## Rechtsprechung (BVerwG — Leitsätze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Klagenarten (§ 42 VwGO)

| Klageart | Ziel | Voraussetzung |
|---|---|---|
| Anfechtungsklage | Aufhebung eines VA | § 42 Abs. 1 Alt. 1 VwGO |
| Verpflichtungsklage | Erlass eines VA | § 42 Abs. 1 Alt. 2 VwGO |
| Allgemeine Leistungsklage | Sonstiges Verwaltungshandeln | analog |
| Feststellungsklage | Feststellung eines Rechtsverhältnisses | § 43 VwGO |

## Vorverfahren (§§ 68 ff. VwGO)

Das Vorverfahren (Widerspruchsverfahren) ist grundsätzlich Klagevoraussetzung.

**Im Aktenauszug erfassen:**

- Datum des angefochtenen Verwaltungsakts
- Datum der Widerspruchseinlegung
- Datum des Widerspruchsbescheids (Fristbeginn für Klage!)
- Behörde, die den Widerspruchsbescheid erlassen hat

## Kritische Fristen (VwGO)

| Frist | Norm | Dauer |
|---|---|---|
| Widerspruchsfrist | § 70 VwGO | 1 Monat ab Bekanntgabe VA |
| Klagefrist | § 74 VwGO | 1 Monat ab Zustellung Widerspruchsbescheid |
| Berufungsfrist | § 124a Abs. 1 VwGO | 1 Monat ab Zustellung Urteil |
| Zulassungsantragsfrist | § 124a Abs. 4 VwGO | 1 Monat ab Zustellung Urteil |
| Revisionsfrist | § 139 VwGO | 1 Monat ab Zustellung Urteil |

**Besonderheit:** Fehlerhafter Beginn der Klagefrist durch fehlende oder fehlerhafte Rechtsbehelfsbelehrung führt zu Jahresfrist (§ 58 Abs. 2 VwGO).

## Aufschiebende Wirkung (§ 80 VwGO)

**Im Aktenauszug besonders hervorheben:**

- Hat die Klage aufschiebende Wirkung? (Grundsatz § 80 Abs. 1 VwGO)
- Ist die aufschiebende Wirkung kraft Gesetzes ausgeschlossen (§ 80 Abs. 2 VwGO)?
- Hat die Behörde die sofortige Vollziehung angeordnet (§ 80 Abs. 2 Nr. 4 VwGO)?
- Wurde ein Antrag nach § 80 Abs. 5 VwGO gestellt?

## Eilrechtsschutz (§ 123 VwGO)

Für Verpflichtungs- und sonstige Leistungsklagen: einstweilige Anordnung zur Regelung des vorläufigen Zustands.

## Berufungszulassung (§ 124 VwGO)

Berufung bedarf der Zulassung durch das Oberverwaltungsgericht. Zulassungsgründe:
- Ernstliche Zweifel an der Richtigkeit des Urteils (Nr. 1)
- Besondere tatsächliche oder rechtliche Schwierigkeiten (Nr. 2)
- Grundsätzliche Bedeutung (Nr. 3)
- Divergenz (Nr. 4)
- Verfahrensmangel (Nr. 5)

**Im Aktenauszug:** Welchen Zulassungsgrund trägt die Berufungsklägerin vor?

## Besonderheiten im Aktenauszug

- Beklagte ist regelmäßig eine Behörde (Bund / Land / Gemeinde)
- Verwaltungsakt mit vollständigem Inhalt und Datum erfassen
- Widerspruchsbescheid als eigenes Dokument in der Sachverhaltschronologie
- Behördliche Aktenzeichen neben Gerichtsaktenzeichen angeben
