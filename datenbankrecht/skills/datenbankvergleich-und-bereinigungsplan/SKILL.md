---
name: datenbankvergleich-und-bereinigungsplan
description: "Datenbankvergleich und Bereinigungsplan bei Datenbankrechts-Verletzungen: Technische Methoden zum Nachweis von Datenübereinstimmungen (Fingerprinting, Fuzzy-Matching, Hash-Vergleich), Bereinigungspflicht des Verletzers nach Unterlassungsurteil und Vernichtungsanspruch (§ 98 UrhG). Erstellt Vergleichsprotokoll und Bereinigungsplan-Vorlage für Prozess und Vollstreckung im Datenbankrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Datenbankvergleich und Bereinigungsplan — Technischer Nachweis und Vollstreckung

## Arbeitsbereich

Datenbankvergleich und Bereinigungsplan bei Datenbankrechts-Verletzungen: Technische Methoden zum Nachweis von Datenübereinstimmungen (Fingerprinting, Fuzzy-Matching, Hash-Vergleich), Bereinigungspflicht des Verletzers nach Unterlassungsurteil und Vernichtungsanspruch (§ 98 UrhG). Erstellt Vergleichsprotokoll und Bereinigungsplan-Vorlage für Prozess und Vollstreckung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber hat eine Unterlassungsverpflichtung erwirkt und muss nun sicherstellen, dass der Verletzer die entnommenen Daten tatsächlich löscht und nicht mehr nutzt.
- Verletzer bestreitet, dass die bei ihm gefundenen Daten aus der Kläger-Datenbank stammen — technischer Nachweis der Übereinstimmung ist erforderlich.
- IT-Abteilung soll einen Datenbankvergleich durchführen, der vor Gericht als Sachverständigengutachten verwendet werden kann.

## Erste Schritte

1. Vergleichsmethodik festlegen: Fingerprinting (eindeutige Kennung je Datensatz), Hash-Vergleich (kryptographische Übereinstimmung), Fuzzy-Matching (nahezu identische Einträge trotz geringfügiger Änderungen).
2. Datenbankzustand dokumentieren: Snapshot der eigenen Datenbank mit Zeitstempel als Referenzpunkt für den Vergleich.
3. Wettbewerber-Daten sichern: Öffentlich zugängliche Daten des Verletzers aus seinem Portal/API erfassen und speichern.
4. Übereinstimmungsanalyse: Automatischer Vergleich der Datensätze — Anzahl der Übereinstimmungen, Honey-Pot-Treffer, strukturelle Ähnlichkeiten.
5. Bereinigungsplan erstellen: Welche Daten muss der Verletzer löschen, in welcher Frist und wie wird die Löschung nachgewiesen?
6. Vernichtungsanspruch geltend machen: § 98 UrhG — Vernichtung von widerrechtlich hergestellten Vervielfältigungsstücken der Datenbank.

## Rechtsrahmen

- § 97 Abs. 1 UrhG: Unterlassungs- und Beseitigungsanspruch — Verletzer muss Verletzungszustand beenden.
- § 98 UrhG: Vernichtungsanspruch — rechtswidrig hergestellte Vervielfältigungsstücke müssen vernichtet werden.
- § 890 ZPO: Vollstreckung des Unterlassungsurteils — Ordnungsgeld bei Nichterfüllung.
- § 286 ZPO: Freie Beweiswürdigung — technische Datenbankvergleiche als Beweismittel; Sachverständigengutachten.
- § 887 ZPO: Vollstreckung vertretbarer Handlungen (Datenlöschung) — Ersatzvornahme durch das Gericht.
- Art. 10 RL 96/9/EG: Rechtsfolgen bei Verletzung des sui-generis-Datenbankrechts — Mitgliedstaaten müssen wirksame Rechtsbehelfe vorsehen.

## Prüfraster

- Welche Vergleichsmethodik (Fingerprinting, Hash, Fuzzy) ist für den konkreten Datenbanktyp am besten geeignet?
- Sind Honey-Pot-Datensätze in der eigenen Datenbank vorhanden, die beim Verletzer aufgetaucht sind?
- Kann der Zeitpunkt der Übernahme durch den Verletzer technisch eingegrenzt werden?
- Wurde ein Bereinigungsplan mit konkreten Fristen und Löschnachweis vereinbart oder durch Gericht angeordnet?
- Greift § 98 UrhG — muss der Verletzer die entnommenen Datensätze vernichten, oder reicht Löschung?
- Kann die Bereinigung durch Ersatzvornahme (§ 887 ZPO) vollstreckt werden, wenn der Verletzer nicht kooperiert?
- Ist ein Sachverständigengutachten für den Datenbankvergleich erforderlich, um die Beweiskraft zu stärken?

## Typische Fallstricke

- Verletzer kann Daten geringfügig verändern (Schreibweisen, Formatierungen), um Hash-Vergleiche zu umgehen — Fuzzy-Matching erforderlich.
- Bereinigungsplan ohne Nachweis-Mechanismus (Löschprotokoll, Audit) ist nicht vollstreckbar.
- § 98 UrhG-Vernichtungsanspruch ist verhältnismäßig zu prüfen — kann bei geringer Verletzung unverhältnismäßig sein.
- Backup-Kopien des Verletzers enthalten möglicherweise noch die gestohlenen Daten — Bereinigung muss explizit alle Systeme umfassen.
- Ohne Sachverständigengutachten kann das Gericht die technische Vergleichsmethodik nicht ausreichend würdigen.

## Output

- Datenbankvergleichs-Protokollvorlage (Methodik, Ergebnis, Statistik)
- Bereinigungsplan-Vorlage (Fristen, Systeme, Nachweispflichten)
- Vernichtungsantrag nach § 98 UrhG
- Vollstreckungsantrag bei Nichterfüllung (§§ 887-890 ZPO)
- Sachverständigen-Briefing für technischen Datenbankvergleich

## Quellen

- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 98 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/98.html)
- [§ 890 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/890.html)
- [§ 887 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/887.html)
- [§ 286 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/286.html)
- [Art. 10 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
