---
name: agb-pruefung
description: |
  Unterstützt bei der rechtlichen Prüfung von Allgemeinen Geschäftsbedingungen (AGB) auf
  Einbeziehung, Inhaltskontrolle und Transparenzgebot nach §§ 305–310 BGB. Lädt, wenn ein
  Mandat die Prüfung, Erstellung oder Verteidigung von AGB im B2C- oder B2B-Bereich
  zum Gegenstand hat.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - AGB
  - Allgemeine Geschäftsbedingungen
  - Inhaltskontrolle
  - § 307 BGB
  - § 309 BGB
  - Transparenzgebot
  - Klauselkontrolle
  - AGB-Recht
  - B2B AGB
---

# AGB-Prüfung – Einbeziehung und Inhaltskontrolle

## Zweck

Dieser Skill begleitet die vollständige AGB-rechtliche Prüfung nach §§ 305–310 BGB. Er deckt
drei Prüfungsebenen ab: (1) wirksame Einbeziehung (§§ 305–305c BGB), (2) Auslegung
(§§ 305b, 305c Abs. 2 BGB) und (3) Inhaltskontrolle (§§ 307–309 BGB). Typische Mandate:
Gestaltung oder Revision von Online-AGB (B2C/E-Commerce), Lieferanten- und Einkaufsbedingungen
(B2B), Prüfung fremder AGB im Rahmen einer Vertragsverhandlung.

## Eingaben

Das Modell benötigt:

1. **AGB-Text**: vollständiger Wortlaut der zu prüfenden Klauseln oder des gesamten Klauselwerks
2. **Vertragstyp**: Kauf-, Werk-, Dienst-, Miet- oder sonstiger Vertrag
3. **Vertragsparteien**: B2C (Verbraucher i. S. v. § 13 BGB) oder B2B (Unternehmer § 14 BGB);
   ggf. gemischte Konstellationen
4. **Einbeziehungsmodalitäten**: Wie werden AGB einbezogen (Webshop, Bestellformular,
   Rahmenvertrag)? Liegen Hinweis und Möglichkeit zur Kenntnisnahme vor?
5. **Besondere Branchen**: Energieversorgung, Banken, Versicherungen (Sonderregelungen)

## Rechtlicher Rahmen

### Normen

- **§ 305 Abs. 1–3 BGB** – AGB-Begriff, Einbeziehungsvoraussetzungen
- **§ 305a BGB** – Einbeziehung durch besondere Umstände (Fernkommunikation etc.)
- **§ 305b BGB** – Vorrang der Individualabrede
- **§ 305c BGB** – überraschende und mehrdeutige Klauseln; Unklarheitenregel Abs. 2
- **§ 306 BGB** – Rechtsfolge der Unwirksamkeit (Restgültigkeit des Vertrags, dispositivem Recht)
- **§ 307 BGB** – Inhaltskontrolle; Abs. 1 S. 2 Transparenzgebot; Abs. 2 Nr. 1 (Abweichung
  von Grundgedanken), Nr. 2 (Gefährdung des Vertragszwecks)
- **§ 308 BGB** – Klauselverbote mit Wertungsmöglichkeit
- **§ 309 BGB** – Klauselverbote ohne Wertungsmöglichkeit (absolute Verbote)
- **§ 310 Abs. 1 BGB** – eingeschränkte Anwendung §§ 308, 309 im B2B-Verkehr; nur § 307 BGB
  vollanwendbar

### Leitentscheidungen

- BGH, Urt. v. 14.05.2014 – VIII ZR 114/13, NJW 2014, 2708 Rn. 19 ff.: Zur Einbeziehung
  von AGB im Onlinehandel; der bloße Verweis auf „unsere AGB" genügt, wenn die Klauseln vor
  Vertragsschluss klar zugänglich sind; kein Erfordernis, dass der Verbraucher die AGB
  tatsächlich liest.
- BGH, Urt. v. 18.07.2012 – VIII ZR 337/11, NJW 2013, 291 Rn. 22 f.: Transparenzgebot
  § 307 Abs. 1 S. 2 BGB; eine Preisanpassungsklausel ist unwirksam, wenn sie dem Verwender
  die einseitige Anpassung ermöglicht, ohne dass der Vertragspartner die Höhe vorhersehen kann.
- BGH, Urt. v. 09.12.2020 – XII ZR 10/19, NJW 2021, 1307 Rn. 31 ff.: Inhaltskontrolle von
  Laufzeitklauseln im B2B-Bereich; auch im B2B gilt § 307 BGB; eine übermäßig lange
  Bindungsfrist kann den Vertragspartner unangemessen benachteiligen.
- BGH, Urt. v. 05.10.2005 – VIII ZR 16/05, NJW 2006, 47 Rn. 9: Unklarheitenregel
  § 305c Abs. 2 BGB; bei zwei vertretbaren Auslegungen ist die für den Verwender ungünstigere
  maßgeblich.

### Kommentarliteratur

- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 1 ff. (Grundstruktur der Inhaltskontrolle;
  zweistufige Prüfung: Feststellung der unangemessenen Benachteiligung, dann Abwägung mit
  Interessen des Verwenders; Rn. 56 ff. zu § 307 Abs. 2 Nr. 1 BGB).
- Becker, in: BeckOK BGB, 70. Ed. (Stand 01.02.2025), § 307 Rn. 22 ff. (Transparenzgebot:
  Klauseln müssen klar, verständlich und ohne Einschränkungen für den Vertragspartner
  nachvollziehbar sein; Rn. 25 zu mehrstufigen Preisgefügen).
- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 307 Rn. 1 ff. (Überblick zur
  Inhaltskontrolle; Verhältnis zu §§ 308, 309 BGB; Anwendung im B2B nach § 310 Abs. 1 BGB).
- Basedow, in: MüKoBGB, 9. Aufl. 2022, § 305 Rn. 14 ff. (Einbeziehungsvoraussetzungen; Verweis
  auf die Klauseln muss deutlich und zumutbar sein; Kenntnisnahmemöglichkeit ausreichend).

## Ablauf

1. **Qualifikation als AGB** (§ 305 Abs. 1 BGB): Sind die Klauseln vorformuliert für eine
   Vielzahl von Verträgen? Wurde der Inhalt vom Verwender gestellt? Cave: 3-Verträge-Regel
   der Rspr.
2. **Einbeziehungsprüfung** (§§ 305 Abs. 2, 305a BGB):
   - Deutlicher Hinweis vor Vertragsschluss?
   - Zumutbare Möglichkeit der Kenntnisnahme (Link oder Aushang)?
   - Bei B2B: § 305 Abs. 2 BGB gilt nicht; konkludente Einbeziehung durch Handelsbrauch
     möglich (§ 346 HGB).
3. **Individualabrede** (§ 305b BGB): Vorrang prüfen; Individualabrede muss ernsthaft
   ausgehandelt sein (BGH: blo­ßes Textmarkieren im Formular ≠ Aushandeln).
4. **Überraschungsklauseln** (§ 305c Abs. 1 BGB): Ungewöhnlich und nicht zu erwarten?
   Klausel wird nicht Vertragsbestandteil.
5. **Auslegung** (§ 305c Abs. 2 BGB): Bei Unklarheit → kundenfreundlichste Auslegung.
6. **Inhaltskontrolle** §§ 307–309 BGB in der Prüfreihenfolge:
   a. § 309 BGB (Verbote ohne Wertungsmöglichkeit) – abschließende schwarze Liste
   b. § 308 BGB (Verbote mit Wertungsmöglichkeit) – graue Liste
   c. § 307 BGB (Generalklausel) – unangemessene Benachteiligung; Transparenzgebot
   Im B2B-Verkehr: §§ 308, 309 BGB gelten nur als Indizien für § 307 BGB
   (§ 310 Abs. 1 S. 2 BGB).
7. **Rechtsfolge** (§ 306 BGB): Unwirksame Klausel entfällt; Vertrag bleibt im Übrigen
   wirksam; dispositives Recht tritt an die Stelle (Lückenfüllung).
8. **Empfehlung**: Klausel-für-Klausel-Tabelle mit Ampelsystem (grün/gelb/rot) und
   Überarbeitungsvorschlägen.

## Ausgabeformat

- **Prüftabelle** (Klausel | Prüfungsmaßstab | Ergebnis | Überarbeitungsvorschlag)
- **Rechtliches Memo** (Gutachtenstil) für kritische Klauseln mit ausführlicher Subsumtion
- Auf Wunsch: **überarbeiteter AGB-Entwurf** mit nachverfolgbaren Änderungen

## Beispiel

**Sachverhalt**: Eine Online-Plattform (B2C) verwendet folgende Klausel: „Änderungen an den
AGB werden dem Kunden per E-Mail mitgeteilt. Widerspricht der Kunde nicht binnen 6 Wochen,
gilt seine Zustimmung als erteilt."

**Prüfung (Gutachtenstil)**:

*§ 308 Nr. 5 BGB*: Die Klausel fingiert eine Willenserklärung (Zustimmung) durch Schweigen.
Nach § 308 Nr. 5 lit. b BGB müsste der Verwender den Kunden auf die Bedeutung seines
Schweigens hinweisen. Ob ein ausreichender Hinweis in der E-Mail liegt, ist im Einzelfall zu
prüfen. Fehlt er, ist die Klausel nach § 308 Nr. 5 BGB unwirksam.

*Zusätzlich § 307 Abs. 1 S. 2 BGB (Transparenzgebot)*: Die Frist von 6 Wochen ist nach
Maßgabe des BGH (Urt. v. 18.07.2012 – VIII ZR 337/11, NJW 2013, 291 Rn. 22) unklar, wenn der
Verbraucher nicht erkennen kann, welche konkreten Änderungen gelten sollen.

**Ergebnis**: Klausel ist unwirksam. Empfohlen: Opt-in-Lösung mit aktiver Bestätigung.

## Risiken und typische Fehler

- **Einbeziehungsfehler**: AGB werden erst nach Vertragsschluss übermittelt → nicht wirksam
  einbezogen (§ 305 Abs. 2 BGB); besonders kritisch bei E-Commerce.
- **Überraschungsklauseln** (§ 305c BGB): Klauseln an unerwarteter Stelle (z. B. Haftungsaus-
  schluss in Lieferbedingungen) → unwirksam ohne Hinweis.
- **Unterschätzung des B2B-Risikos**: Auch B2B-AGB unterliegen § 307 BGB; übermäßige
  Haftungsfreizeichnungen und einseitige Preisänderungsrechte werden vom BGH kassiert.
- **Transparenzgebot** § 307 Abs. 1 S. 2 BGB: Preis­nachberechnungsklauseln ohne
  Berechnungsformel unwirksam (BGH, Urt. v. 14.05.2014 – VIII ZR 114/13, NJW 2014, 2708 Rn. 19).
- **Geltungserhaltende Reduktion**: Im deutschen AGB-Recht grundsätzlich nicht zulässig
  (BGH st. Rspr.); unwirksame Klausel entfällt ersatzlos oder wird durch dispositives Recht
  ersetzt.
- **Berufsrecht**: Keine Klauseln entwerfen, die § 43a BRAO oder berufsrechtliche Verbote
  umgehen; Verschwiegenheit § 203 StGB beachten.

## Quellenpflicht

Jede AGB-Bewertung ist nach `references/zitierweise.md` zu belegen. Für jede als unwirksam
eingestufte Klausel ist die einschlägige BGH-Entscheidung oder die herrschende Kommentarmeinung
zu zitieren (Bearbeiter, Werk, Aufl., §, Rn.). Bei abweichender Instanzrechtsprechung ist auf
den Streitstand hinzuweisen. „Die Klausel ist unwirksam" ohne Beleg ist kein ausreichendes
Ergebnis.
