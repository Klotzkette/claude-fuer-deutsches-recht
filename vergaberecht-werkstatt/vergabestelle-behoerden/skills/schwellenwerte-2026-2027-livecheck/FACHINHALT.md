---
name: schwellenwerte-2026-2027-livecheck
description: Prüft EU-Schwellenwerte 2026/2027, Bundes- und Landeswertgrenzen, Auftraggebertyp, Auftragsart, Losregeln, Reformstand, Direktauftrag, Verfahrenswahl und Dokumentation vor tragenden Aussagen.
---

# EU-Schwellenwerte und Bund-Länder-Wertgrenzen 2026/2027 sicher prüfen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->



## Normenanker

Beginne mit den Spezialnormen des konkreten Vergaberegimes und den im folgenden Workflow genannten Tatbeständen. BGB- oder ZPO-Normen nur ergänzen, wenn ein eigenständiger Sekundäranspruch oder Gerichtsweg geprüft wird; sie ersetzen keine vergaberechtliche Voraussetzung.

## Arbeitsweg

- Auftraggebertyp, Auftragsart, Schätzstichtag, Nettoauftragswert, Optionen, Laufzeit und Lose aus der Vergabeakte übernehmen.
- Rechenweg nach § 3 VgV oder dem einschlägigen Spezialregime vollständig nachbauen.
- Auftraggeberkategorie des § 106 Abs. 2 GWB bestimmen; den zentralen Schwellenwert nur Bundeskanzleramt und Bundesministerien zuordnen.
- Für 2026/2027 die richtige Quelle am Stichtag öffnen: Delegierte Verordnung (EU) 2025/2152 für klassische Vergaben, 2025/2150 für Sektoren, 2025/2151 für Konzessionen und 2025/2487 für Verteidigungs- und Sicherheitsvergaben.
- Unterhalb der Schwelle Bundesland, Auftraggebertyp, Leistungsart, Fördermittel und Inkrafttreten anhand `references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md` und amtlicher Landesquelle abgleichen.

Fokus: EU-Schwellenwerte, neue Bundesreform, Landeswertgrenzen, Direktauftrag, Auftragsart, Auftraggebertyp, Sektor, Konzession, Verteidigung/Sicherheit, Nettoauftragswert, Losregeln und Dokumentationsvermerk.

### Schwellenwerte 2026/2027 Livecheck

## Sofortmodus

1. Rechenlücke oder falsche Kategorie als Stoppsignal markieren.
2. EU-, Bundes- oder Landesregime mit Norm, Quelle und Stichtag festlegen.
3. Zulässige Verfahrensarten und Veröffentlichungsweg daraus ableiten.
4. Bei bereits gestarteter Vergabe Berichtigung, Rückversetzung oder Fortführung mit Risiko entscheiden.
5. Schwellenwert- und Verfahrensvermerk vollständig ausgeben.

## Pflicht-Output

- Entscheidungssatz mit Go, Go unter Auflage oder Stop.
- Fristen-, Akten- und Freigabeampel.
- Prüfmatrix aus Tatsache, Norm, Aktenbeleg, Gegenargument und Rechtsfolge.
- Vollständiges Arbeitsprodukt plus verantwortlicher nächster Schritt.

## Typische Outputs

Schwellenwerttabelle, Bundesland-Wertgrenzencheck, Direktauftragsvermerk, Rechenweg, Los-/Zusammenrechnungsprüfung, Rechtswegempfehlung.

## Qualitätsgates

- Nur veröffentlichte Maßstäbe und nachweisbare Tatsachen verwenden.
- Rechtsstand, Fristen und tragende Entscheidungen gegen prüfbare Quellen absichern.
- Gleichbehandlung und dokumentierte Vergleichsgruppe kontrollieren.
- Freigabe erst bei reproduzierbarer Entscheidung und vollständigem Rückkanal.

## Weiterleitung

- `02-auftragswert-schaetzung` für die detaillierte Rechenakte.
- `03-schwellenwert-pruefung` für die Regimeentscheidung.
- `04-verfahrensart-waehlen` für die daraus folgende Verfahrenswahl.
