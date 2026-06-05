---
name: konten-kassenfuehrung-miet-pachtverwaltung
description: "Konten Kassenfuehrung Miet Pachtverwaltung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Konten Kassenfuehrung Miet Pachtverwaltung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Konten Kassenfuehrung Miet Pachtverwaltung** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zvg-konten-kassenfuehrung` | Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten Treuhand. Prüfraster Treuhandkonto Soll Ist Einnahmen Ausgaben Belege Vorschuss Auskunft Gerichtsbericht. Output Kontenspiegel mit Saldouebersicht Belegverzeichnis und monatlichem Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-rechnungslegung. |
| `zvg-miet-und-pachtverwaltung` | Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhältnisse und muss diese weiter verwalten. Normen § 152 ZVG Mieteinzug §§ 535 ff. BGB Mietrecht § 150 ZVG Vorausverfuegungen des Schuldners. Prüfraster Mietvertraege Pachtvertraege Zahlstellen Vorausverfuegungen Kautionen Nebenkosten Nutzungsregelungen. Output Mieterliste mit Vertragsuebersicht Kautionsnachweis und Zahlungsplan für Verteilungsrechnung. Abgrenzung zu zvg-mieteinzug-rückstaende und zvg-räumung-kündigung. |
| `zvg-mieteinzug-rueckstaende` | Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rückstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose Kündigung § 286 BGB Verzug. Prüfraster Soll-Ist-Abgleich Mahnung Ratenvereinbarung Klage Zahlungseingang Kontoabgleich Dokumentation. Output Rückstandsprotokoll mit Mahnhistorie Klageprüfung und Einzugsnachweis für Rechnungslegung. Abgrenzung zu zvg-miet-und-pachtverwaltung und zvg-räumung-kündigung. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Konten Kassenfuehrung Miet Pachtverwaltung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zvg-konten-kassenfuehrung`

**Fokus:** Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten Treuhand. Prüfraster Treuhandkonto Soll Ist Einnahmen Ausgaben Belege Vorschuss Auskunft Gerichtsbericht. Output Kontenspiegel mit Saldouebersicht Belegverzeichnis und monatlichem Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-rechnungslegung.

# Konten, Kasse und Buchführung

## Aufgabe

Führt die Finanzverwaltung mit getrenntem Treuhandkonto und prüffähiger Soll-Ist-Buchführung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Treuhandkonto einzurichten ist
- Zahlungen eingehen oder Ausgaben freigegeben werden
- Jahres- oder Schlussrechnung vorbereitet wird

## Eingaben

- Kontoauszüge, Belege, Rent Roll, Ausgaben
- Vorschussanforderungen, Gerichtskosten, Vergütung
- Vorjahressaldo und offene Posten

## Workflow

1. **Konto einrichten** - gesondertes Treuhandkonto und Zahlungsregeln dokumentieren.
2. **Buchen** - Soll- und Isteinnahmen, Ausgaben, Belege und Salden erfassen.
3. **Abgleichen** - Rent Roll, Konto, Belege und Vorschuss laufend abstimmen.
4. **Auskunft** - gerichtsfeste Auskunft und Unterlagenpaket vorbereiten.

## Ausgabe

- Konto- und Kassenbuch
- Soll-Ist-Abgleich
- Belegliste

## Qualitätsgates

- Masse getrennt von Eigenbeständen
- Einzelbuchungen ausgewiesen
- Belege zu jeder Buchung

## Rote Schwellen

- privates Konto
- nicht zuordenbare Bareinnahme
- fehlende Kontoauszüge

## Interne Vorlagen

- assets/templates/konto-kassenbuch.md
- assets/templates/rechnungslegung.md

## Amtliche Erstquellen

- § 13 ZwVwV
- § 14 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Konten/Kassenführung

§ 153 ZVG (Einnahmen aus Nutzungen) → § 152 ZVG (Pflichten Verwaltung) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Jahresrechnung) → § 675 BGB (Geschäftsbesorgungsvertrag) → § 667 BGB (Herausgabe Treuhandgelder) → § 280 BGB (Schadensersatz Treuhandvermischung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Konten/Kassenführung

1. Ist das Treuhandkonto eindeutig als solches bei der Bank benannt?
2. Ist die Buchführung tagesaktuell oder bestehen Rückstände?
3. Werden Einnahmen und Ausgaben kontengetrennt nach Einnahmenarten geführt?
4. Ist ein Kassenbuch oder Buchhaltungsprogramm im Einsatz?

## Output-Template Kassenbuch-Schema (Auszug)

```
Buchungsjournal Zwangsverwaltung [ADRESSE]
AZ: [X] — Treuhandkonto: [IBAN]

Datum | Buchungstext | Einnahme | Ausgabe | Saldo | Beleg-Nr.
[D] | Miete Jan [MIETER] Einheit 1 | [BETRAG] | — | [X] | K01
[D] | Versicherungsprämie [ANBIETER] | — | [BETRAG] | [X] | A01
[D] | Grundsteuer Vorauszahlung | — | [BETRAG] | [X] | A02

Saldo per [DATUM]: [BETRAG] EUR
Rücklage laufende Kosten: [BETRAG] EUR
Ausschüttungsfähiger Betrag: [BETRAG] EUR
```

## 2. `zvg-miet-und-pachtverwaltung`

**Fokus:** Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhältnisse und muss diese weiter verwalten. Normen § 152 ZVG Mieteinzug §§ 535 ff. BGB Mietrecht § 150 ZVG Vorausverfuegungen des Schuldners. Prüfraster Mietvertraege Pachtvertraege Zahlstellen Vorausverfuegungen Kautionen Nebenkosten Nutzungsregelungen. Output Mieterliste mit Vertragsuebersicht Kautionsnachweis und Zahlungsplan für Verteilungsrechnung. Abgrenzung zu zvg-mieteinzug-rückstaende und zvg-räumung-kündigung.

# Miet- und Pachtverwaltung

## Aufgabe

Ordnet Miet- und Pachtverhältnisse im beschlagnahmten Objekt mit Kommunikation, Zahlstellen, Kautionen und Vertragsrisiken.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Mieter oder Pächter vorhanden sind
- Mietzahlungen umzuleiten sind
- Verträge, Kautionen oder Vorausverfügungen unklar sind

## Eingaben

- Miet- und Pachtverträge
- Mieterliste, Zahlungsverlauf, Kautionen
- Schreiben des Schuldners oder der Mieter

## Workflow

1. **Verträge erfassen** - Einheit, Nutzer, Miete, Nebenkosten, Laufzeit, Kaution und Sonderrechte aufnehmen.
2. **Mitteilung** - Mieter/Pächter über Zwangsverwaltung und neue Zahlstelle informieren.
3. **Vorausverfügungen** - Abtretung, Vorauszahlung, Kaution und Rückstände prüfen.
4. **Laufend verwalten** - Anpassungen, Nebenkosten, Mängel, Kündigungen und Kommunikation steuern.

## Ausgabe

- Rent Roll
- Mieterschreiben
- Vertragsrisikomatrix

## Qualitätsgates

- Soll- und Istmiete getrennt
- Kautionen nicht als freie Masse behandelt
- Vorausverfügungen geprüft

## Rote Schwellen

- Zahlung an Schuldner
- fehlender Mietvertrag
- streitiger Besitz

## Interne Vorlagen

- assets/templates/mieterliste-rent-roll.md
- assets/templates/schuldner-glaeubiger-kommunikation.md

## Amtliche Erstquellen

- §§ 4, 5, 6 ZwVwV
- § 152 ZVG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Miet-/Pachtverwaltung ZVG

§ 152 ZVG (Rechte/Pflichten Verwalter) → § 153 ZVG (Einziehung Nutzungen) → § 57 ZVG (Schutz der Mieter) → §§ 535 566 BGB (Mietrecht) → §§ 8-9 ZwVwV (laufende Verwaltung) → § 581 BGB (Pachtvertrag) → §§ 596-599 BGB (Pächterschutz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Miet-/Pachtverwaltung

1. Liegen schriftliche Mietverträge vor? (Alle Einheiten vollständig erfasst)
2. Sind Kautionen hinterlegt? (Pflicht: auf separatem Kautionskonto)
3. Bestehen Sondermietrechte (Wohnrecht Nießbrauch)? (Im Grundbuch Abt. II prüfen)
4. Sind Pachtverhältnisse vorhanden? (Sonderregeln §§ 581 ff. BGB)

## Output-Template Verwaltungsübernahme-Schreiben Miet-/Pachtverhältnis

```
[ZWANGSVERWALTER]

An [MIETER/PÄCHTER]
[ADRESSE]

Mitteilung: Übernahme der Verwaltung

Sehr geehrte/r Herr/Frau [NAME],

ich habe die Zwangsverwaltung über das Grundstück [ADRESSE] übernommen.
Ich trete damit in Ihre/Ihre bestehenden Miet-/Pachtverhältnisse ein
und führe die Verwaltung ab [DATUM] fort.

Die Miete/Pacht ist ab sofort an folgendes Konto zu zahlen:
[IBAN, BIC, BANK, VERWENDUNGSZWECK]

Ihre vertraglichen Rechte bleiben unberührt. Mängelanzeigen richten Sie bitte an:
[KONTAKTDATEN ZWANGSVERWALTER]

[UNTERSCHRIFT]
```

## 3. `zvg-mieteinzug-rueckstaende`

**Fokus:** Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rückstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose Kündigung § 286 BGB Verzug. Prüfraster Soll-Ist-Abgleich Mahnung Ratenvereinbarung Klage Zahlungseingang Kontoabgleich Dokumentation. Output Rückstandsprotokoll mit Mahnhistorie Klageprüfung und Einzugsnachweis für Rechnungslegung. Abgrenzung zu zvg-miet-und-pachtverwaltung und zvg-räumung-kündigung.

# Mieteinzug und Rückstände

## Aufgabe

Sichert laufende Nutzungen und treibt Rückstände mit sauberem Soll-Ist-Abgleich ein.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Mieteinnahmen fehlen
- Rückstände vor oder nach Beschlagnahme bestehen
- Zahlungen nicht zugeordnet werden können

## Eingaben

- Rent Roll, Kontoauszüge, Mieterkonten
- Rückstandsliste, Mahnungen, Einwendungen
- Mietverträge und Betriebskostenstände

## Workflow

1. **Soll-Ist-Abgleich** - Sollmieten je Einheit mit Zahlungseingängen und Altrückständen matchen.
2. **Rückstände trennen** - beschlagnahmte Nutzungen, Altansprüche und streitige Posten unterscheiden.
3. **Mahnen** - freundliche Zahlungserinnerung, Mahnung, Ratenplan oder Klagevorschlag erstellen.
4. **Gericht berichten** - wesentliche Rückstände und Einziehungsmaßnahmen dokumentieren.

## Ausgabe

- Rückstandsliste
- Mahn- und Klagepaket
- Zahlungsabgleich

## Qualitätsgates

- jede Zahlung einer Einheit zugeordnet
- Alt- und Neurückstände getrennt
- Einwendungen protokolliert

## Rote Schwellen

- Dauerleerstand
- Mietminderung ohne Prüfung
- Kontoauszug fehlt

## Interne Vorlagen

- assets/templates/mieteinzug-rueckstaende.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 8 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Mieteinzug/Rückstände

§ 153 ZVG (Einziehung Nutzungen) → § 535 Abs. 2 BGB (Mietzinszahlungspflicht) → § 543 Abs. 2 Nr. 3 BGB (Kündigung wegen Zahlungsverzug) → § 286 BGB (Verzug) → § 288 BGB (Verzugszinsen) → §§ 12-13 ZwVwV (Buchführung Rückstände)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Mieteinzug/Rückstände

1. Rückstand vor oder nach Beschlagnahme entstanden? (Unterschiedliche Behandlung)
2. Hat der Mieter Einwendungen gegen die Miethöhe erhoben? (Minderung § 536 BGB prüfen)
3. Liegen mehr als zwei Monatsmieten Rückstand vor? (Außerordentliche Kündigung § 543 BGB prüfen)
4. Ist Klage wirtschaftlich sinnvoll? (Insolvenzrisiko des Mieters, Vollstreckbarkeit prüfen)

## Output-Template Mahn-/Kündigungsschreiben ZVG

**Adressat:** rückständiger Mieter — Tonfall scharf-fristsetzend

```
[ZWANGSVERWALTER]
EINSCHREIBEN MIT RÜCKSCHEIN

An [MIETER NAME]
[ADRESSE]

Zwangsverwaltung [ADRESSE], AZ [X]

Mahnung und Fristsetzung / Außerordentliche Kündigung

Sehr geehrte/r Herr/Frau [NAME],

folgende Mietrückstände sind aufgelaufen:
Monat | Betrag | Status
[TABELLE]
Gesamtrückstand: [BETRAG] EUR

Ich fordere Sie auf, den Rückstand bis zum [DATUM] zu zahlen.
[Falls Kündigung: Gleichzeitig kündige ich das Mietverhältnis fristlos nach
§ 543 Abs. 2 Nr. 3 BGB wegen Zahlungsverzugs von mehr als zwei Monatsmieten.
Bitte übergeben Sie die Wohnung spätestens zum [DATUM] geräumt.]

[UNTERSCHRIFT ZWANGSVERWALTER]
```
