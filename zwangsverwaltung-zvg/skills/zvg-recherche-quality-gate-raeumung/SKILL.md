---
name: zvg-recherche-quality-gate-raeumung
description: "Recherche Quality Gate Raeumung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Recherche Quality Gate Raeumung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Recherche Quality Gate Raeumung** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zvg-portal-recherche` | Recherche von Zwangsversteigerungsterminen im amtlichen ZVG-Portal für Investoren und Gläubiger. Anwendungsfall Mandant sucht Versteigerungsobjekte oder Gläubiger will Terminuebersicht. Normen §§ 87 ff. ZVG Versteigerungstermin § 74a ZVG Verkehrswert. Prüfraster Suchparameter Treffer Gutachten-Downloads Exposee Terminangaben Mindestgebot. Output Recherchebericht mit Trefferprotokoll Gutachten-Links Terminliste und Recherchegrenzen. Abgrenzung zu zvg-bieterangebot-bewertung (Investorenbewertung) und zvg-versteigerungsteilnahme. |
| `zvg-quality-gate` | Quality Gate für Zwangsverwaltung vor Versand oder Rechnungslegung. Anwendungsfall Bericht Rechnungslegung oder Verteilungsplan soll ans Gericht versandt werden und muss vorher geprüft werden. Normen § 161 ZVG Rechnungslegung § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten. Prüfraster Beschluss Objekt Konto Rent-Roll Berichte Rechnungslegung Verteilung Belege Rollen Risiken. Output Quality-Gate-Bericht mit Ampelstatus offenen Punkten und Freigabeentscheidung. Abgrenzung zu zvg-rechnungslegung und zvg-berichtswesen-gericht. |
| `zvg-raeumung-kuendigung` | Räumung Kündigung und Besitzkonflikte in der Zwangsverwaltung. Anwendungsfall Schuldner weigert sich auszuziehen oder Mieter soll nach Zwangsverwaltungsende kündigt werden. Normen § 150 ZVG Besitzrecht § 543 BGB fristlose Kündigung § 573 BGB ordentliche Kündigung § 721 ZPO Räumungsfrist. Prüfraster Schuldnerwohnrechte Mieterrechte Kündigungsgründe Zutrittsrechte gerichtlicher Klageweg Räumungsantrag. Output Kündigungsschreiben und Räumungsklage-Baustein mit Disclaimer. Abgrenzung zu zvg-mieteinzug-rückstaende und zvg-gläubiger-schuldner-kommunikation. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Recherche Quality Gate Raeumung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zvg-portal-recherche`

**Fokus:** Recherche von Zwangsversteigerungsterminen im amtlichen ZVG-Portal für Investoren und Gläubiger. Anwendungsfall Mandant sucht Versteigerungsobjekte oder Gläubiger will Terminuebersicht. Normen §§ 87 ff. ZVG Versteigerungstermin § 74a ZVG Verkehrswert. Prüfraster Suchparameter Treffer Gutachten-Downloads Exposee Terminangaben Mindestgebot. Output Recherchebericht mit Trefferprotokoll Gutachten-Links Terminliste und Recherchegrenzen. Abgrenzung zu zvg-bieterangebot-bewertung (Investorenbewertung) und zvg-versteigerungsteilnahme.

# ZVG-Portal-Recherche

## Aufgabe

Führt eine belegbare Recherche im amtlichen ZVG-Portal durch und macht daraus ein Rechercheprotokoll für Akte, Bieterprüfung oder Verwalterkommunikation.

## Startet bei

- Auftrag: "Suche im ZVG-Portal"
- Prüfung eines Aktenzeichens, Gerichts, Ortes, Ortsteils, Objekttyps oder Termins
- Abgleich, ob Gutachten, Exposee oder Fotos im Portal verfügbar sind

## Workflow

1. **Suchziel klären**: Gericht, Bundesland, Ort, Ortsteil, Straße, Aktenzeichen, Objektart, Terminfenster.
2. **Portal öffnen**: `https://www.zvg-portal.de/index.php?button=Termine%20suchen`.
3. **Parameter dokumentieren**: Bundesland, Gericht, Verfahrensart, Objektart, Straße, PLZ, Ort, Ortsteil, Termin von/bis, Sortierung.
4. **Treffer sichern**: Trefferzahl, Aktenzeichen, Gericht, Objektbeschreibung, Verkehrswert, Termin, Detail-URL, Abrufdatum.
5. **Downloads prüfen**: Gutachten, Exposee, Fotos nur vermerken; keine fremden Fotos in Test- oder Arbeitsakten übernehmen.
6. **Negativtreffer festhalten**: Auch "0 Treffer" ist ein verwertbares Rechercheergebnis.
7. **Grenzen notieren**: Portal ist Veröffentlichungsplattform. Maßgeblich bleiben Bekanntmachung, Gerichtsakte, Grundbuch und Termin.

## Ausgabe

- Rechercheprotokoll mit URL, Datum, Suchparametern, Trefferliste und offenem Nachfassbedarf
- Kurzvermerk für Akte oder Mandantenkommunikation

## Qualitätsgates

- Abrufdatum und Uhrzeit enthalten
- Suchparameter so konkret, dass die Recherche wiederholbar ist
- Treffer nicht mit materieller Rechtsprüfung verwechselt
- Bei Portalfehler oder leerem Treffer: keine Fantasie-Treffer erzeugen

## Rote Schwellen

- Behaupteter Termin ohne Treffer-/Gerichtsbeleg
- Download fremder Fotos in eine Demo- oder Testakte
- Verwechslung privater ZVG-Portale mit dem amtlichen Portal

## Interne Vorlage

- `assets/templates/zvg-portal-rechercheprotokoll.md`

## Amtliche Erstquellen

- Amtliches Portal: `https://www.zvg-portal.de/`
- Suchformular: `https://www.zvg-portal.de/index.php?button=Termine%20suchen`

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Portal-Recherche

§ 12 GBO (Einsicht Grundbuch) → § 14 GBO (berechtigtes Interesse) → § 2 ZVG (Vollstreckungsgericht) → § 750 ZPO (vollstreckbarer Titel) → §§ 899-900 BGB (Grundbucheinsicht und Wirkung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Recherche-Checkliste Zwangsverwaltung

| Quelle | Inhalt | Beschaffen |
|---|---|---|
| Grundbuch Abt. I | Eigentümer | [ ] |
| Grundbuch Abt. II | Lasten Beschränkungen Wohnrechte | [ ] |
| Grundbuch Abt. III | Grundpfandrechte Gläubiger | [ ] |
| Vollstreckungsgericht | Anordnungsbeschluss AZ | [ ] |
| ESUG/Insolvenzportal | Insolvenzantrag vorhanden? | [ ] |
| Liegenschaftskataster | Flurstücke Grundfläche | [ ] |
| Grundsteuerbescheid | Aktueller Steuermessbetrag | [ ] |
| Mietverträge | alle Einheiten vollständig | [ ] |

## 2. `zvg-quality-gate`

**Fokus:** Quality Gate für Zwangsverwaltung vor Versand oder Rechnungslegung. Anwendungsfall Bericht Rechnungslegung oder Verteilungsplan soll ans Gericht versandt werden und muss vorher geprüft werden. Normen § 161 ZVG Rechnungslegung § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten. Prüfraster Beschluss Objekt Konto Rent-Roll Berichte Rechnungslegung Verteilung Belege Rollen Risiken. Output Quality-Gate-Bericht mit Ampelstatus offenen Punkten und Freigabeentscheidung. Abgrenzung zu zvg-rechnungslegung und zvg-berichtswesen-gericht.

# Quality Gate für Zwangsverwaltung

## Aufgabe

Prüft ZVG-Arbeitsprodukte vor Versand oder Zahlung auf Rechenfehler, fehlende Belege und Rollenprobleme.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Bericht, Rechnung, Verteilungsplan oder Schreiben fertig wirkt
- Zahlung oder Auszahlung vorbereitet wird
- ein kritischer Konflikt dokumentiert werden soll

## Eingaben

- Arbeitsprodukt
- Beschluss, Rent Roll, Konto, Belege
- Adressat, Zweck und Frist

## Workflow

1. **Rollencheck** - Zwangsverwalter, Schuldner, Gläubiger, Mieter und Gericht sauber trennen.
2. **Zahlencheck** - Soll-Ist, Saldo, Rückstände, Ausgaben und Verteilung prüfen.
3. **Belegcheck** - Fotos, Kontoauszüge, Rechnungen und Beschlüsse referenzieren.
4. **Freigabe** - Freigabe, Stopp oder Rückfrage mit Priorität ausgeben.

## Ausgabe

- QA-Vermerk
- Fehlerliste
- Freigabe- oder Stopp-Empfehlung

## Qualitätsgates

- keine Zahlung ohne Kontobeleg
- keine Verteilung ohne Rücklagenprüfung
- Berichte adressatengerecht

## Rote Schwellen

- falsches Konto
- fehlende Versicherung
- unbelegte Verteilung

## Interne Vorlagen

- assets/templates/quality-gate.md
- assets/templates/rechnungslegung.md

## Amtliche Erstquellen

- §§ 13 bis 16 ZwVwV
- § 155 ZVG

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Quality-Gate

§ 154 ZVG (Gerichtliche Aufsicht) → § 20 ZwVwV (Vergütung Ordnungsmäßigkeit) → § 13-15 ZwVwV (Buchführung Berichte) → § 839 BGB (Haftung Amtspflichtverletzung) → § 280 BGB (Pflichtverletzung Schadensersatz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Quality-Gate-Checkliste (Quartalsweise)

**Pflicht-Checkpunkte:**
- [ ] Treuhandkonto-Saldo stimmt mit Buchungsjournal überein
- [ ] Alle Mieteinnahmen vollständig verbucht
- [ ] Alle Ausgabenbelege vorhanden und zugeordnet
- [ ] Grundsteuer und laufende öffentliche Lasten bezahlt
- [ ] Gebäudeversicherung aktiv und Prämie bezahlt
- [ ] Gericht-Bericht erstellt und eingereicht (falls fällig)
- [ ] Rückstandsliste aktuell (Mieter, Beträge, Mahnstufen)
- [ ] Instandhaltungsmaßnahmen dokumentiert und genehmigt (falls erforderlich)
- [ ] Keine Zahlungen an Schuldner ohne Gerichtsgenehmigung
- [ ] Aktennotizen für außergewöhnliche Vorkommnisse vorhanden

## 3. `zvg-raeumung-kuendigung`

**Fokus:** Räumung Kündigung und Besitzkonflikte in der Zwangsverwaltung. Anwendungsfall Schuldner weigert sich auszuziehen oder Mieter soll nach Zwangsverwaltungsende kündigt werden. Normen § 150 ZVG Besitzrecht § 543 BGB fristlose Kündigung § 573 BGB ordentliche Kündigung § 721 ZPO Räumungsfrist. Prüfraster Schuldnerwohnrechte Mieterrechte Kündigungsgründe Zutrittsrechte gerichtlicher Klageweg Räumungsantrag. Output Kündigungsschreiben und Räumungsklage-Baustein mit Disclaimer. Abgrenzung zu zvg-mieteinzug-rückstaende und zvg-gläubiger-schuldner-kommunikation.

# Räumung, Kündigung und Besitzkonflikte

## Aufgabe

Prüft Konflikte um Besitz, Nutzung, Kündigung und Räumung im Rahmen der Zwangsverwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Schuldner oder Dritte den Zutritt verweigern
- Mieter erheblich rückständig sind
- Kündigung, Räumung oder Nutzungsänderung erwogen wird

## Eingaben

- Mietvertrag, Rückstände, Objektstatus
- Schuldnerwohnräume, Beschluss, Kommunikation
- Gefahren, Fotos, Zeugen, Polizeikontakt

## Workflow

1. **Rechtsposition** - Schuldner, Mieter, Pächter, Dritter oder unbekannter Nutzer bestimmen.
2. **Maßnahme** - Zutritt, Abmahnung, Kündigung, Räumung oder gerichtliche Hilfe trennen.
3. **Verhältnismäßigkeit** - Masseinteresse, Kosten, Risiken und Alternativen prüfen.
4. **Schreiben/Antrag** - Kommunikation oder gerichtlichen Antrag vorbereiten.

## Ausgabe

- Konfliktvermerk
- Kündigungs- oder Zutrittsanschreiben
- Gerichtsbaustein

## Qualitätsgates

- Wohnraumschutz geprüft
- Kosten/Nutzen dokumentiert
- Beweise gesichert

## Rote Schwellen

- Selbsthilfe
- unberechtigter Schlosswechsel
- Schuldnerhausstand nicht beachtet

## Interne Vorlagen

- assets/templates/raeumung-kuendigung.md
- assets/templates/besitzuebernahme-protokoll.md

## Amtliche Erstquellen

- § 149 ZVG als Schuldnerwohnraum-Schnittstelle
- § 5 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Räumung/Kündigung ZVG

§ 543 BGB (außerordentliche Kündigung Zahlungsverzug) → § 546 BGB (Räumungsanspruch) → § 149 ZVG (Schutz Schuldnerwohnraum) → §§ 5-6 ZwVwV (Besitzkonflikte) → §§ 885-886 ZPO (Räumungsvollstreckung) → § 940a ZPO (Räumungsverfügung einstweiliger Rechtsschutz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Räumung/Kündigung

1. Wer nutzt das Objekt — Mieter oder Schuldner selbst? (§ 149 ZVG Sonderschutz für Schuldner)
2. Wie hoch ist der Rückstand? (Außerordentliche Kündigung ab 2 Monatsmieten § 543 Abs. 2 Nr. 3 BGB)
3. Liegt bereits eine Abmahnung vor? (Empfehlenswert vor Kündigung)
4. Besteht akute Gefahr für das Objekt durch den Nutzer? (Sofortmaßnahme möglich)
5. Ist gerichtliche Hilfe erforderlich? (Vollstreckungsgericht-Antrag § 154 ZVG)

## Output-Template Räumungsklage-Antrag (Auszug)

**Adressat:** Amtsgericht — Tonfall sachlich-juristisch

```
An das Amtsgericht [ORT]
Wohnungssachen / Vollstreckungsgericht
AZ Zwangsverwaltung: [X]

Räumungsklage

des Zwangsverwalters [NAME], für die Zwangsverwaltungsmasse
[ADRESSE], AZ [X]
— Kläger —
gegen
[MIETER/SCHULDNER], [ADRESSE]
— Beklagte —

Antrag:
Die Beklagte wird verurteilt, die Wohnung/das Objekt [BEZEICHNUNG] zu räumen
und geräumt an den Kläger als Zwangsverwalter herauszugeben.

Begründung:
[KÜNDIGUNG VOM DATUM, ANLAGE K1; RÜCKSTANDSNACHWEIS ANLAGE K2]
```
