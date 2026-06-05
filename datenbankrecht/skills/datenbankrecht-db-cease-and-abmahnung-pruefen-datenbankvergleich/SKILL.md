---
name: datenbankrecht-db-cease-and-abmahnung-pruefen-datenbankvergleich
description: "DB Cease AND Abmahnung Pruefen Datenbankvergleich: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Cease AND Abmahnung Pruefen Datenbankvergleich

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Cease AND Abmahnung Pruefen Datenbankvergleich** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-046-cease-and-desist-letter-datenbankrecht` | Cease-and-Desist-Letter (Abmahnung) im Datenbankrecht nach § 97a UrhG: Anforderungen an wirksame Abmahnung (Verletzungshandlung, Fristsetzung, Unterlassungsforderung, Schadensersatz), Kostenerstattung und Missbrauchsprüfung. Erstellt Abmahnschreiben für §§ 87a-87e UrhG-Verletzungen und bewertet Gegendarstellung und modifizierte Unterlassungserklärung. |
| `db-047-abmahnung-pruefen-datenbankrecht` | Prüfung einer erhaltenen Datenbankrechts-Abmahnung: Berechtigungs-Check des Abmahnenden (§ 87a Abs. 2 UrhG), Verletzungstatbestand (§ 87b UrhG), Vollständigkeitscheck der Unterlassungserklärung, Verjährung, Vertragsstrafe-Angemessenheit (§ 339 BGB) und Handlungsoptionen (Unterzeichnung, Widerspruch, Schutzschrift). Erstellt Antwortschreiben und Risikoabwägung. |
| `db-049-datenbankvergleich-und-bereinigungsplan` | Datenbankvergleich und Bereinigungsplan bei Datenbankrechts-Verletzungen: Technische Methoden zum Nachweis von Datenübereinstimmungen (Fingerprinting, Fuzzy-Matching, Hash-Vergleich), Bereinigungspflicht des Verletzers nach Unterlassungsurteil und Vernichtungsanspruch (§ 98 UrhG). Erstellt Vergleichsprotokoll und Bereinigungsplan-Vorlage für Prozess und Vollstreckung. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Cease AND Abmahnung Pruefen Datenbankvergleich**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-046-cease-and-desist-letter-datenbankrecht`

**Fokus:** Cease-and-Desist-Letter (Abmahnung) im Datenbankrecht nach § 97a UrhG: Anforderungen an wirksame Abmahnung (Verletzungshandlung, Fristsetzung, Unterlassungsforderung, Schadensersatz), Kostenerstattung und Missbrauchsprüfung. Erstellt Abmahnschreiben für §§ 87a-87e UrhG-Verletzungen und bewertet Gegendarstellung und modifizierte Unterlassungserklärung.

# Cease-and-Desist-Letter (Abmahnung) im Datenbankrecht — § 97a UrhG

## Mandantenfall

- Datenbankbetreiber hat Nachweise für systematisches Scraping durch einen Wettbewerber und will eine förmliche Abmahnung mit Unterlassungsforderung senden.
- Unternehmen hat eine Abmahnung wegen behaupteter Datenbankrechts-Verletzung erhalten und muss kurzfristig entscheiden, ob es die Unterlassungserklärung unterzeichnet.
- Anwalt will überprüfen, ob eine erhaltene Abmahnung den gesetzlichen Anforderungen des § 97a UrhG entspricht und ob die Kostenerstattungspflicht besteht.

## Erste Schritte

1. Verletzungshandlung klar benennen: Welche konkreten Handlungen verletzen welche Normen (§ 87b UrhG) — Entnahme welcher Teile, durch wen, wann?
2. Unterlassungsforderung formulieren: Hinreichend bestimmt und vollständig — alle Verletzungshandlungen und Varianten erfassen.
3. Fristsetzung bestimmen: Üblicherweise kurze Frist (3-7 Tage) für Unterzeichnung der Unterlassungserklärung.
4. Kostenerstattungsanspruch prüfen: § 97a Abs. 3 UrhG — Kostenerstattung für Abmahnanwaltsgebühren bei Nicht-Verbraucher-Geschäftsbeziehung.
5. Missbrauchsprüfung vornehmen: § 97a Abs. 4 UrhG — unberechtigte Abmahnung kann Schadensersatzpflicht des Abmahnenden begründen.
6. Unterlassungserklärung entgegennehmen und prüfen: Ist sie ausreichend weit, zeitlich unbegrenzt und enthält sie eine angemessene Vertragsstrafe?

## Rechtsrahmen

- § 97a Abs. 1 UrhG: Abmahnung als Voraussetzung für Kostenerstattung — muss hinreichend deutlich sein.
- § 97a Abs. 3 UrhG: Ersatz der Rechtsanwaltsgebühren bei berechtigter Abmahnung — gilt auch im Datenbankrecht.
- § 97a Abs. 4 UrhG: Kostenerstattung für unberechtigte Abmahnung beim Abgemahnten.
- § 87b UrhG: Verletzungstatbestand — Grundlage für den Unterlassungsanspruch in der Abmahnung.
- § 97 Abs. 1 UrhG: Unterlassungsanspruch bei Datenbankherstellerrechts-Verletzung.
- § 339 BGB: Vertragsstrafe in Unterlassungserklärung — Höhe und Bestimmtheit.

## Prüfraster

- Ist die Verletzungshandlung in der Abmahnung konkret und vollständig beschrieben?
- Enthält die Abmahnung eine klare Unterlassungsforderung mit Fristsetzung?
- Ist der Abmahnende berechtigt — ist er tatsächlich Inhaber des Datenbankherstellerrechts (§ 87a Abs. 2 UrhG)?
- Entspricht der Kostenerstattungsanspruch dem § 97a Abs. 3 UrhG — liegt ein berechtigtes Interesse vor?
- Besteht Gefahr einer unberechtigten Abmahnung (§ 97a Abs. 4 UrhG) — muss der Abgemahnte Gegenabmahnung aussprechen?
- Ist die angeforderte Unterlassungserklärung ausreichend weit und zeitlich unbegrenzt?
- Ist die Vertragsstrafe in der beigefügten Unterlassungserklärung angemessen und vollstreckbar?

## Typische Fallstricke

- Zu eng gefasste Unterlassungserklärung des Abgemahnten beseitigt nicht alle Verletzungsformen — Gläubiger sollte ablehnen und klagen.
- Unberechtigte Abmahnung (kein tatsächliches Herstellerrecht) löst Kostenerstattung zugunsten des Abgemahnten aus (§ 97a Abs. 4 UrhG).
- Abmahnung zu kurzfristig (weniger als 3 Tage Frist) kann als unzumutbar angesehen werden.
- Wenn Verletzung bereits eingestellt wurde, besteht keine Wiederholungsgefahr mehr — Unterlassungsanspruch entfällt.
- Massenabmahnungen ohne konkrete Verletzungsanalyse sind rechtsmissbräuchlich nach § 8c UWG (analog).

## Output

- Abmahnschreiben-Vorlage für § 87b UrhG-Verletzung (vollständige Pflichtangaben)
- Unterlassungserklärung-Vorlage (mit Vertragsstrafe)
- Gegenabmahnung bei unberechtigter Abmahnung (§ 97a Abs. 4 UrhG)
- Abmahnung-Prüfcheckliste für Empfänger (Berechtigung, Vollständigkeit, Fristen)
- Antwortschreiben auf Abmahnung (Unterzeichnung / Widerspruch / modifizierte Erklärung)

## Quellen

- [§ 97a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 339 BGB — dejure.org](https://dejure.org/gesetze/BGB/339.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## 2. `db-047-abmahnung-pruefen-datenbankrecht`

**Fokus:** Prüfung einer erhaltenen Datenbankrechts-Abmahnung: Berechtigungs-Check des Abmahnenden (§ 87a Abs. 2 UrhG), Verletzungstatbestand (§ 87b UrhG), Vollständigkeitscheck der Unterlassungserklärung, Verjährung, Vertragsstrafe-Angemessenheit (§ 339 BGB) und Handlungsoptionen (Unterzeichnung, Widerspruch, Schutzschrift). Erstellt Antwortschreiben und Risikoabwägung.

# Abmahnung prüfen im Datenbankrecht — Checkliste und Reaktionsoptionen

## Mandantenfall

- Unternehmen hat heute Morgen eine Abmahnung wegen Datenbankrechts-Verletzung erhalten und muss innerhalb von 5 Tagen reagieren.
- Startup bezweifelt, dass der Abmahnende überhaupt Inhaber des behaupteten Datenbankherstellerrechts ist — wie prüft man das?
- Anwalt soll beurteilen, ob die geforderte Unterlassungserklärung zu weit gefasst ist und ob eine modifizierte Erklärung ausreicht.

## Erste Schritte

1. Abmahnenden identifizieren: Wer mahnt ab, und hat er Herstellerrecht am behaupteten Datenbankrecht (§ 87a Abs. 2 UrhG — Investition, Initiative, Risiko)?
2. Verletzungsvorwurf überprüfen: Welche konkrete Handlung wird als § 87b UrhG-Verletzung behauptet — ist sie tatsächlich erfolgt?
3. Unterlassungserklärung analysieren: Ist sie hinreichend bestimmt, zeitlich unbegrenzt, enthält sie eine angemessene Vertragsstrafe (§ 339 BGB)?
4. Verjährung prüfen: § 102 UrhG — ist der behauptete Verletzungszeitraum verjährt (3-Jahres-Frist)?
5. Schranken prüfen: Greift § 87c UrhG (erlaubte Handlungen), § 44b UrhG (TDM-Schranke) oder vertragliche Erlaubnis — liegt tatsächlich eine Verletzung vor?
6. Handlungsoptionen abwägen: Unterzeichnung, modifizierte Unterlassungserklärung, Widerspruch, Schutzschrift vor dem zuständigen Gericht.

## Rechtsrahmen

- § 87a Abs. 2 UrhG: Herstellereigenschaft des Abmahnenden — muss er Inhaber des Rechts sein?
- § 87b UrhG: Verletzungstatbestand — ist eine Entnahme wesentlicher Teile tatsächlich nachweisbar?
- § 87c UrhG: Erlaubte Handlungen als Einwand gegen Abmahnung (z. B. TDM-Schranke, rechtmäßige Nutzung).
- § 97a Abs. 4 UrhG: Kostenerstattung bei unberechtigter Abmahnung — Gegenanspruch des Abgemahnten.
- § 102 UrhG: Verjährung — 3 Jahre ab Kenntnis von Verletzung und Verletzer.
- § 339 BGB: Vertragsstrafe in der Unterlassungserklärung — Höhe auf Verhältnismäßigkeit prüfen.

## Prüfraster

- Ist der Abmahnende tatsächlich Inhaber des behaupteten Datenbankherstellerrechts (§ 87a Abs. 2 UrhG)?
- Liegt die behauptete Verletzungshandlung tatsächlich vor — welche Belege legt der Abmahnende vor?
- Greift eine Schranke (§ 87c UrhG, § 44b UrhG) oder liegt eine vertragliche Erlaubnis vor?
- Ist der behauptete Verletzungszeitraum verjährt (§ 102 UrhG)?
- Ist die geforderte Unterlassungserklärung zu weit gefasst — schließt sie erlaubte Nutzungen ein?
- Ist die Vertragsstrafe angemessen, oder ist sie übermäßig hoch — § 340 BGB-Herabsetzung möglich?
- Wurde die Abmahnung fristgerecht und formwirksam erteilt — greift § 97a Abs. 4 UrhG bei unberechtigter Abmahnung?

## Typische Fallstricke

- Versäumte Frist zur Abgabe der Unterlassungserklärung erzeugt keine automatische Rechtsverwirkung — aber erhöht Risiko einer einstweiligen Verfügung.
- Zu schnelles Unterzeichnen einer zu weit gefassten Unterlassungserklärung schränkt künftige erlaubte Aktivitäten ein.
- Abmahnender ohne Herstellerrecht (z. B. nur Lizenznehmer, nicht Hersteller) ist nicht abmahnberechtigt.
- Schutzschrift beim vermuteten Gericht einreichen, bevor die einstweilige Verfügung beantragt wird — Gericht muss sie berücksichtigen.
- TDM-Schranke (§ 44b UrhG) kann als Einwand gegen den Verletzungsvorwurf wirken — wurde Opt-out wirksam erklärt?

## Output

- Abmahnungs-Prüf-Checkliste (Berechtigung, Verletzung, Verjährung, Schranken)
- Antwortschreiben-Optionen (Unterzeichnung / Widerspruch / modifizierte Erklärung)
- Schutzschrift-Muster für das zuständige Landgericht
- Gegenanspruch-Bewertung bei unberechtigter Abmahnung (§ 97a Abs. 4 UrhG)
- Risikoabwägungsmatrix (Unterzeichnen vs. Prozessrisiko)

## Quellen

- [§ 97a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [§ 102 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/102.html)
- [§ 339 BGB — dejure.org](https://dejure.org/gesetze/BGB/339.html)

## 3. `db-049-datenbankvergleich-und-bereinigungsplan`

**Fokus:** Datenbankvergleich und Bereinigungsplan bei Datenbankrechts-Verletzungen: Technische Methoden zum Nachweis von Datenübereinstimmungen (Fingerprinting, Fuzzy-Matching, Hash-Vergleich), Bereinigungspflicht des Verletzers nach Unterlassungsurteil und Vernichtungsanspruch (§ 98 UrhG). Erstellt Vergleichsprotokoll und Bereinigungsplan-Vorlage für Prozess und Vollstreckung.

# Datenbankvergleich und Bereinigungsplan — Technischer Nachweis und Vollstreckung

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
