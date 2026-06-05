---
name: insolvenz-schnittstelle-instandhaltung
description: "Insolvenz Schnittstelle Instandhaltung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Insolvenz Schnittstelle Instandhaltung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Insolvenz Schnittstelle Instandhaltung** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zvg-insolvenz-schnittstelle` | Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz des Schuldners. Anwendungsfall Schuldner wird insolvent waehrend Zwangsverwaltung laeuft und Verwalter muss Koordination mit Insolvenzverwalter klaeren. Normen § 165 InsO Absonderungsrecht § 49 InsO Grundpfandgläubiger § 155 ZVG Einnahmen. Prüfraster Insolvenzeroeffnung Absonderung Verwalterkommunikation Forderungsanmeldung Verteilungsauswirkungen. Output Koordinationsprotokoll mit Absonderungsnachweis Forderungsanmeldungsunterlagen und Abstimmungsprotokoll Insolvenzverwalter. Abgrenzung zu zvg-verteilungsplan-155 und zvg-rechnungslegung. |
| `zvg-instandhaltung-sicherung` | Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB Verkehrssicherungspflicht BauO-Laender. Prüfraster Verkehrssicherungspflicht Notmassnahmen Reparaturen Genehmigung Budget Dokumentation Gerichtszustimmung. Output Massnahmenprotokoll mit Kosten Begründung Genehmigungsantrag und Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-versicherungen-gefahren. |
| `zvg-kommandocenter` | Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen starten. Normen §§ 146-161 ZVG Kernvorschriften. Prüfraster Bestellung Beschlagnahme Besitz Mietverwaltung Konto Bericht Rechnungslegung Verteilung freistehende Objekte Risiken. Output Routing-Übersicht mit Statusampel zu allen laufenden Zwangsverwaltungen und Tagesaufgaben. Abgrenzung zu zvg-quality-gate (Qualitaetsprüfung vor Abschluss) und zvg-simulation-training. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Insolvenz Schnittstelle Instandhaltung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zvg-insolvenz-schnittstelle`

**Fokus:** Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz des Schuldners. Anwendungsfall Schuldner wird insolvent waehrend Zwangsverwaltung laeuft und Verwalter muss Koordination mit Insolvenzverwalter klaeren. Normen § 165 InsO Absonderungsrecht § 49 InsO Grundpfandgläubiger § 155 ZVG Einnahmen. Prüfraster Insolvenzeroeffnung Absonderung Verwalterkommunikation Forderungsanmeldung Verteilungsauswirkungen. Output Koordinationsprotokoll mit Absonderungsnachweis Forderungsanmeldungsunterlagen und Abstimmungsprotokoll Insolvenzverwalter. Abgrenzung zu zvg-verteilungsplan-155 und zvg-rechnungslegung.

# Schnittstelle zur Insolvenz

## Aufgabe

Ordnet Fälle, in denen Zwangsverwaltung und Insolvenzverfahren zusammentreffen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- über das Vermögen des Schuldners Insolvenz beantragt oder eröffnet wird
- Insolvenzverwalter, Sachwalter oder Gläubiger Rechte anmelden
- § 165 InsO oder Absonderungsrechte relevant werden

## Eingaben

- Insolvenzeröffnungsbeschluss, IV-Kontakt
- ZVG-Beschluss, Forderungen, Grundbuch
- Mieten, Ausgaben und Verteilungsstand

## Workflow

1. **Verfahren koordinieren** - ZVG-Akte und Insolvenzakte mit Rollen, Daten und Sperren abgleichen.
2. **Rechte prüfen** - Absonderung, § 165 InsO, Forderungen und Massebezug markieren.
3. **Kommunikation** - Insolvenzverwalter, Gericht und betreibende Gläubiger abstimmen.
4. **Verteilung** - Rang und Auskehr unter Insolvenzschnittstelle prüfen.

## Ausgabe

- Schnittstellenvermerk
- Kommunikationsentwurf
- Verteilungsrisiko-Ampel

## Qualitätsgates

- Insolvenzverwalterrolle nicht mit Zwangsverwalterrolle vermischt
- Beschlüsse beider Gerichte geprüft
- Rang offen markiert

## Rote Schwellen

- doppelte Verwertung
- widersprechende Gerichtsanordnungen
- Zahlung an falsche Masse

## Interne Vorlagen

- assets/templates/insolvenz-schnittstelle.md
- assets/templates/verteilungsplan-155.md

## Amtliche Erstquellen

- § 165 InsO
- ZVG Gesamtfassung

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzschnittstelle

§ 152 ZVG i.V.m. §§ 80-82 InsO (Insolvenzbeschlag) → § 30 InsO (Anordnung Insolvenzeröffnung) → § 49 InsO (Absonderungsrecht Grundpfandrecht) → § 165 InsO (Zwangsversteigerung durch Insolvenzverwalter) → § 21 Abs. 2 Nr. 5 InsO (vorläufige Sicherungsmaßnahmen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Insolvenzschnittstelle

1. Ist Insolvenzantrag gestellt oder Insolvenzverfahren eröffnet?
2. Ist ein vorläufiger Insolvenzverwalter bestellt? (Abstimmung der Zuständigkeiten)
3. Welche Gläubiger haben Absonderungsrechte nach § 49 InsO?
4. Soll die Zwangsverwaltung fortgeführt oder aufgehoben werden?

## 2. `zvg-instandhaltung-sicherung`

**Fokus:** Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB Verkehrssicherungspflicht BauO-Laender. Prüfraster Verkehrssicherungspflicht Notmassnahmen Reparaturen Genehmigung Budget Dokumentation Gerichtszustimmung. Output Massnahmenprotokoll mit Kosten Begründung Genehmigungsantrag und Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-versicherungen-gefahren.

# Instandhaltung, Sicherung und Gefahrenabwehr

## Aufgabe

Steuert notwendige Maßnahmen zur Erhaltung und sicheren Nutzung des Objekts.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Schäden, Mängel oder Gefahren gemeldet werden
- Reparaturen oder Notmaßnahmen nötig sind
- Budget oder gerichtliche Zustimmung unklar ist

## Eingaben

- Mängelmeldung, Fotos, Kostenvoranschläge
- Versicherung, Mietereinwendungen, Behördenpost
- Kontostand und Vorschusslage

## Workflow

1. **Gefahr einstufen** - akute Gefahr, Substanzerhalt, Komfort oder Modernisierung trennen.
2. **Budget und Zustimmung** - Kosten, Liquidität, Vorschuss und Zustimmungsvorbehalte prüfen.
3. **Beauftragung** - Dienstleister, Leistungsumfang, Dokumentation und Abnahme vorbereiten.
4. **Bericht** - Gericht und Beteiligte über wesentliche Maßnahmen informieren.

## Ausgabe

- Gefahren- und Maßnahmenvermerk
- Beauftragungsentwurf
- Berichtsbaustein

## Qualitätsgates

- Notmaßnahme begründet
- Kosten plausibilisiert
- Fotos und Belege gesichert

## Rote Schwellen

- Verkehrssicherungsrisiko
- Brandschutzmangel
- fehlende Versicherung

## Interne Vorlagen

- assets/templates/instandhaltung-gefahrensicherung.md
- assets/templates/versicherung-und-lasten.md

## Amtliche Erstquellen

- § 1 ZwVwV
- § 9 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Instandhaltung/Sicherung

§ 152 ZVG (Pflicht ordnungsgemäße Verwaltung) → §§ 8-9 ZwVwV (Instandhaltungsmaßnahmen) → § 154 ZVG (Genehmigung größerer Maßnahmen) → § 823 Abs. 1 BGB (Verkehrssicherungspflicht) → § 836 BGB (Haftung Grundstücksbesitzer) → § 278 BGB (Erfüllungsgehilfe)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Instandhaltung/Sicherung

1. Liegen akute Gefahrenstellen vor? (Sofortmaßnahme ohne Genehmigung möglich)
2. Sind größere Maßnahmen geplant? (Gerichtsgenehmigung erforderlich ab ca. 2.000 EUR netto)
3. Ist die Gebäudeversicherung aktiv und ausreichend?
4. Wer führt die Instandhaltungsarbeiten durch? (Auftragnehmer-Vertrag mit Vergabe-Dokumentation)

## Output-Template Gerichtsantrag Instandhaltung

**Adressat:** Amtsgericht — Tonfall formell-antragend

```
An das Amtsgericht [ORT]
Vollstreckungsgericht
AZ: [X]

Antrag auf Genehmigung einer Instandhaltungsmaßnahme

Sehr geehrte Damen und Herren,

in der Zwangsverwaltung [ADRESSE] beantrage ich die Genehmigung folgender Maßnahme:

Maßnahme: [BESCHREIBUNG]
Grund: [SCHADENSURSACHE, DRINGLICHKEIT]
Kosten: [ANGEBOTE ANLIEGEND — ANLAGE 1-3]
Empfohlenes Angebot: [BIETER, BETRAG]

Die Maßnahme ist zur Abwehr weiterer Schäden und zur Erfüllung der
Verkehrssicherungspflicht unaufschiebbar.

[DATUM, UNTERSCHRIFT]
```

## 3. `zvg-kommandocenter`

**Fokus:** Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen starten. Normen §§ 146-161 ZVG Kernvorschriften. Prüfraster Bestellung Beschlagnahme Besitz Mietverwaltung Konto Bericht Rechnungslegung Verteilung freistehende Objekte Risiken. Output Routing-Übersicht mit Statusampel zu allen laufenden Zwangsverwaltungen und Tagesaufgaben. Abgrenzung zu zvg-quality-gate (Qualitaetsprüfung vor Abschluss) und zvg-simulation-training.

# Zwangsverwaltungs-Kommandocenter

## Aufgabe

Führt Zwangsverwalterinnen und Zwangsverwalter vom Bestellungsbeschluss bis zur laufenden Verwaltung und Verteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- ein Zwangsverwaltungsbeschluss eingeht
- Objekt, Mieter, Schuldner oder Gläubiger geordnet werden müssen
- unklar ist, welche Sofortmaßnahmen anstehen

## Eingaben

- Anordnungs- und Bestellungsbeschluss
- Grundstücksdaten, Gläubiger, Schuldner, Mieter
- Mietlisten, Lasten, Versicherungen, Kontoangaben

## Workflow

1. **Beschluss lesen** - Objekt, Schuldner, Gläubiger, Rang und Umfang der Beschlagnahme erfassen.
2. **Sofortplan** - Besitz, Mieterinformation, Konto, Versicherung und Lasten priorisieren.
3. **Objektcockpit** - Rent Roll, Rückstände, Ausgaben, Risiken und Gerichtswiedervorlagen anlegen.
4. **Nächste Aktion** - konkrete Schreiben, Vor-Ort-Termin oder Gerichtsanzeige ausgeben.

## Ausgabe

- Objektkarte
- Sofortmaßnahmenliste
- Kommunikationspaket

## Qualitätsgates

- Bestellung und Objekt exakt erfasst
- keine Zahlung auf Privatkonto
- Mieter und Pächter werden korrekt informiert

## Rote Schwellen

- fehlende Versicherung
- akute Gefahr am Objekt
- Mietzahlungen an Schuldner nach Beschlagnahme

## Interne Vorlagen

- assets/templates/zvg-objektkarte.md
- assets/templates/quality-gate.md

## Amtliche Erstquellen

- §§ 150, 152 ZVG
- §§ 1, 3 ZwVwV

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Kommandocenter

§ 154 ZVG (Gerichtliche Aufsicht) → § 20 ZwVwV (Vergütung und Rechenschaft) → §§ 13-15 ZwVwV (Buchführung und Berichte) → § 159 ZVG (Aufhebung Zwangsverwaltung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Checkliste Kommandocenter (Monatlich)

| Aufgabe | Fälligkeit | Erledigt |
|---|---|---|
| Sollmieten-Abgleich | Monatsanfang | [ ] |
| Rückstands-Update | Monatsmitte | [ ] |
| Ausgabenbelege gesammelt | Monatsende | [ ] |
| Kontoauszüge abgeglichen | Monatsende | [ ] |
| Gerichtsbericht erstellt (falls fällig) | Gem. Anordnung | [ ] |
| Versicherungsprämien gezahlt | Fälligkeitsdatum | [ ] |
| Grundsteuer-Vorauszahlung | 15.02./15.05./15.08./15.11. | [ ] |
| Hausgeldabrechnung WEG (falls EWZ) | Gem. WEG-Plan | [ ] |
