---
name: kanzlei-allgemein-handelsregisterabruf
description: "Handelsregisterabruf ueber offizielle Quellen fuer Unternehmenspruefung in Mandaten. Anwendungsfall Mandant oder Gegner ist eine GmbH und Vertretung Gesellschafterstruktur und Prokura muessen geprueft werden. Normen §§ 15 17 HGB Registerrecht § 10 GwG wirtschaftlich Berechtigte. Pruefraster Firma Sitz Registergericht Vertretung Prokura Gesellschafterliste Gesellschaftsvertrag Zeitstempel Quellenprotokoll. Output Handelsregisterauszug-Zusammenfassung mit Vertretungsnachweis Gesellschafterstruktur und GwG-Dokumentation. Abgrenzung zu kanzlei-allgemein-mandatsannahme-gwg und kanzlei-allgemein-akte."
---

# Handelsregisterabruf


## Triage zu Beginn
1. Was ist der Zweck des Abrufs: Vertretungspruefung, KYC/GwG, Zustellungsanschrift, Vertragspartei-Identifikation?
2. Ist der Eintrag beim Handelsregister aktuell (letzter Abruf-Zeitstempel noetig fuer Nachweis)?
3. Gibt es Verdachtsmomente fuer Sitzverlegung, Geschaeftsfuehreraenderung oder Insolvenzen?
4. Ist eine Gesellschafterliste (GmbH) oder Prokura-Eintragung relevant?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 17.01.2012 - II ZR 197/10, NJW 2012, 1570 — Registerpublizitaet nach § 15 HGB: Eintragungen wirken fuer und gegen jeden; fehlende Kenntnisnahme schutzt nicht bei Vertragsschluss.
- BGH, Urt. v. 14.02.2012 - II ZR 268/10, NJW 2012, 2180 — Vertretungsmacht: bei Zweifeln an der Geschaeftsfuehrerbefugnis ist Handelsregisterauszug als Nachweis zu verlangen.
- BGH, Urt. v. 26.06.2018 - II ZR 92/17, NJW 2018, 3243 — Gesellschafterliste als Nachweis der Mitgliedschaft: massgebend ist die zum Zeitpunkt des Handelns im Register hinterlegte Liste.
- OLG Frankfurt, Urt. v. 25.01.2021 - 19 U 65/20, NZG 2021, 567 — Zeitstempel des Registerabrufs als Beweis fuer Gutglaeubigkeit bei Vertragsschluss; Abruf muss zeitnah zum Vertragsschluss erfolgen.

## Zentrale Normen
- § 15 HGB — Registerpublizitaet: Eintragungen und deren Wirkung
- § 8 HGB — Inhalt und Pflichtangaben des Handelsregisters
- § 40 GmbHG — Gesellschafterliste: Hinterlegung und Wirkung als Nachweis der Mitgliedschaft
- § 3 GwG — Sorgfaltspflichten fuer risikobasierte KYC-Pruefung (Handelsregister als Beleg)

## Kommentarliteratur
- Baumbach/Hopt HGB § 15 Rn. 1-40 (Registerpublizitaet: Wirkungen und Gutglaeubigkeitsschutz)
- MüKo GmbHG/Heidinger § 40 Rn. 1-50 (Gesellschafterliste: Anforderungen und Haftung)

## Zweck

Dieser Skill führt durch einen Handelsregisterabruf und macht daraus ein verwertbares Registerprotokoll für Klage, Vertrag, Mandatsanlage, KYC, Rechnungsadresse oder Zustellung. Er nutzt offizielle Quellen und dokumentiert Quelle, Zeitstempel und Unsicherheiten.

## Offizielle Quellen

- Gemeinsames Registerportal der Länder: `https://www.handelsregister.de`.
- Unternehmensregister: `https://www.unternehmensregister.de`.
- Nicht auf Drittanbieter verlassen, wenn es um Vertretung, Registerstand oder aktuelle Dokumente geht.

Wenn kein Browser- oder Registerzugang vorhanden ist, einen Simulationsmodus anbieten. Im Simulationsmodus müssen alle Registerdaten als fiktiv oder ungeprüft gekennzeichnet werden.

## Abrufziel klären

1. Firma oder Name.
2. Rechtsform.
3. Sitz.
4. Registergericht.
5. Registernummer.
6. Zweck: Klage, Zustellung, Vertrag, Vollmacht, Rechnung, KYC, Due Diligence.
7. Benötigte Dokumente: aktueller Abdruck, chronologischer Abdruck, Gesellschafterliste, Gesellschaftsvertrag, Registerbekanntmachung.

## Prüfprogramm

- Firma exakt übernehmen.
- Rechtsform und Sitz prüfen.
- Registergericht und Registernummer festhalten.
- Vertretungsberechtigung prüfen.
- Einzel- oder Gesamtvertretung prüfen.
- Prokura prüfen.
- Liquidation, Insolvenz, Löschung oder Umwandlung prüfen.
- Zustellfähige Anschrift nicht blind aus Handelsregister ableiten, wenn Zustellung kritisch ist.
- Dokumentdatum und Abrufzeitpunkt protokollieren.

## Such- und Trefferlogik

- Schreibvarianten, alte Firma, Sitzverlegung und Rechtsformzusatz prüfen.
- Mehrere Treffer nicht zusammenführen, sondern getrennt darstellen.
- Bei UG, GmbH, AG, KG, OHG, PartG und e. K. Rechtsform exakt übernehmen.
- Bei Zweigniederlassungen Hauptniederlassung und Vertretung gesondert prüfen.
- Bei Konzernnamen nicht automatisch die richtige Vertragspartnerin annehmen.

## Verwendung

Für Klage:

- Parteibezeichnung und Vertretung prüfen.
- Zustelladresse gesondert validieren.
- Anlagenbezeichnung für Registerauszug vergeben.

Für Vertrag:

- Parteibezeichnung.
- Vertretung und Zeichnungsberechtigung.
- Handelsregisterdaten in Rubrum oder Präambel.

Für Rechnung und Buchhaltung:

- Rechnungsempfänger mit Firma, Rechtsform und Anschrift abgleichen.
- Debitorenstamm aktualisieren.
- Zahlungszuordnung nicht allein aus Registerdaten ableiten.

## Warnlogik

`STOPP` ausgeben, wenn:

- Firma oder Rechtsform unklar ist.
- Vertretung nicht geprüft ist.
- der Registerstatus Liquidation, Löschung, Insolvenz oder Umwandlung nahelegt.
- die Anschrift für Zustellung oder Vertrag nicht belastbar ist.

`WARNUNG` ausgeben, wenn:

- nur eine Simulation vorliegt.
- Dokumente älter sind als der aktuelle Entscheidungsbedarf.
- Gesellschafterliste, Satzung oder Prokura relevant sein könnten, aber fehlen.

## Ausgabe

`assets/templates/handelsregisterabruf-protokoll.md` verwenden.
