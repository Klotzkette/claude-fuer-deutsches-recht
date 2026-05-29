---
name: zvg-quality-gate
description: "Quality Gate für Zwangsverwaltung vor Versand oder Rechnungslegung. Anwendungsfall Bericht Rechnungslegung oder Verteilungsplan soll ans Gericht versandt werden und muss vorher geprüft werden. Normen § 161 ZVG Rechnungslegung § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten. Prüfraster Beschluss Objekt Konto Rent-Roll Berichte Rechnungslegung Verteilung Belege Rollen Risiken. Output Quality-Gate-Bericht mit Ampelstatus offenen Punkten und Freigabeentscheidung. Abgrenzung zu zvg-rechnungslegung und zvg-berichtswesen-gericht."
---

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
