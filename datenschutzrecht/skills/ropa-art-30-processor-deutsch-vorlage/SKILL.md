---
name: ropa-art-30-processor-deutsch-vorlage
description: "Vollvorlage für das Verzeichnis von Verarbeitungstaetigkeiten des Auftragsverarbeiters nach Art. 30 Abs. 2 DSGVO. Vier Mindestinhalte, Auftraggeberliste, Verarbeitungskategorien, Drittlandtransfer, TOM-Verweis. Beispiele für Hosting, Steuerberatung, Lohnbuchhaltung."
---

# RoPA-Vorlage Auftragsverarbeiter (Processor) – Deutsch

## Zweck

Dieser Skill liefert eine ausfuellfertige Vorlage für das Verzeichnis des Auftragsverarbeiters gemaess Art. 30 Abs. 2 DSGVO. Im Unterschied zum Controller-Verzeichnis sind nur vier Pflichtinhalte zu erfassen – nicht sieben. Geeignet für Cloud-Anbieter, IT-Dienstleister, Steuerkanzleien, Lohnbuchhaltung, Hosting, Druckdienstleister, externe DSB.

## Wann dieses Modul hilft

- Auftragsverarbeiter baut sein RoPA erstmalig auf.
- Kanzlei taetigt für Mandanten Datenverarbeitung im Auftrag (z. B. Lohnbuchhaltung, IT-Outsourcing) und ist insoweit Processor.
- Audit eines bestehenden Processor-RoPA.
- Aufsichtsbehoerde verlangt nach Art. 30 Abs. 4 DSGVO Vorlage.

## Rechtlicher Rahmen

Art. 30 Abs. 2 DSGVO – Pflichtinhalte für Processor:

a) Name und Kontaktdaten des Auftragsverarbeiters und jedes Verantwortlichen, in dessen Auftrag er taetig ist, sowie ggf. eines Vertreters des Verantwortlichen oder des Auftragsverarbeiters und eines Datenschutzbeauftragten;
b) Kategorien der im Auftrag jedes Verantwortlichen durchgefuehrten Verarbeitungen;
c) ggf. Uebermittlungen in ein Drittland oder an eine internationale Organisation, einschliesslich Angabe des betreffenden Drittlands sowie bei Uebermittlungen gemaess Art. 49 Abs. 1 Unterabs. 2 Dokumentierung der geeigneten Garantien;
d) wenn moeglich, allgemeine Beschreibung der TOMs gemaess Art. 32 Abs. 1 DSGVO.

Wichtig: Pro Auftraggeber eine Zeile. Mehrere Verarbeitungskategorien koennen zusammengefasst werden, wenn TOMs identisch sind.

## Ablauf / Checkliste

1. Stammdaten Auftragsverarbeiter eintragen (Deckblatt).
2. Liste der Auftraggeber pflegen.
3. Pro Auftraggeber Verarbeitungskategorien beschreiben (nicht Einzelaktivitaeten).
4. Drittlandtransfers identifizieren und Garantie eintragen.
5. TOMs nicht im RoPA wiederholen, sondern auf TOM-Konzept verweisen.
6. Subverarbeiter (Art. 28 Abs. 4 DSGVO) gesondert dokumentieren, soweit ihr Einsatz mit Drittlandtransfer verbunden ist.
7. Versionierung und Review-Datum am Fuss.

## Mustertext / Template

### Deckblatt

```
Auftragsverarbeiter: [Firmenname]
Anschrift: [...]
Vertreter (Art. 27): [falls anwendbar]
Datenschutzbeauftragter: [Name, Kontakt]
Erstellt: [Datum]
Letzte Aenderung: [Datum]
Version: [v1.0]
```

### Tabelle (Pflichtspalten)

| Nr. | Auftraggeber (Verantwortlicher) | Verarbeitungskategorie | Drittland / Garantie | TOM-Verweis |
|---|---|---|---|---|
| 1 | [Mandant A GmbH] | Hosting Buchhaltungssoftware, Backup, Patch-Management | nein | TOM-Anhang A |
| 2 | [Mandant B AG] | Lohnbuchhaltung, Lohnsteueranmeldung, Sozialversicherungsmeldungen | nein | TOM-Anhang A |
| 3 | [Mandant C KG] | E-Mail-Hosting, Spam-Filterung | USA – Subprozessor (SCC + TIA in Anhang B) | TOM-Anhang A |
| 4 | [Mandant D e.V.] | Mitgliederverwaltung, Beitragsabbuchung | nein | TOM-Anhang A |

### Subverarbeiterliste (Anhang)

| Subverarbeiter | Sitz | Leistung | Transferinstrument |
|---|---|---|---|
| [Hyperscaler-Cloud] | USA | Infrastructure as a Service | EU-US DPF (Aktiv-Listing in Anhang B) |
| [E-Mail-Filterdienst] | Irland | Spam-Filter | EU/EWR – keine Garantien noetig |
| [Backup-Dienstleister] | Deutschland | Offsite-Backup | EU/EWR – keine Garantien noetig |

### Versionierungs-Footer

```
Version 1.0 – Erstanlage – [Datum, Bearbeiter]
Version 1.1 – [Aenderung] – [Datum, Bearbeiter]
```

## Typische Fehler

- "Verarbeitungskategorie" wird mit "Zweck" verwechselt – Zwecke bestimmt der Verantwortliche.
- Subverarbeiter fehlen, obwohl Drittlandtransfer ueber sie laeuft.
- Pro Auftraggeber separate TOMs dokumentiert, obwohl Mandantenbasis identisch ist – Redundanz vermeiden.
- Auftraggeber-DSB nicht erfasst.
- TOM-Spalte mit Wiederholung der Anlage 32 – besser Verweis.
- Drittlandtransfer in zweiter Stufe (Sub-Subprozessor) uebersehen.

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` für Rechtsrahmen.
- `ropa-art-30-controller-deutsch-vorlage` für Controller-Pendant.
- `avv-art-28-dsgvo-grundtatbestand` für Vertragspflichten.
- `avv-cloud-und-subverarbeitung-art-28-iv` für Subverarbeiter-Klauseln.
- `tia-template-deutsch-vollvorlage` für Transferpruefung.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 30 Abs. 2, Art. 28.
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).
- DSK-Kurzpapier Nr. 13 "Auftragsverarbeitung" (Stand 16.01.2018).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
