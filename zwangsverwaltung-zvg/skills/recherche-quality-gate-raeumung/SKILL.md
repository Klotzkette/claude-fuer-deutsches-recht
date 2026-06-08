---
name: recherche-quality-gate-raeumung
description: "Recherche von Zwangsversteigerungsterminen im amtlichen ZVG-Portal für Investoren und Gläubiger. Anwendungsfall Mandant sucht Versteigerungsobjekte oder Gläubiger will Terminuebersicht. Normen §§ 87 ff. ZVG Versteigerungstermin § 74a ZVG Verkehrswert. Prüfraster Suchparameter Treffer Gutachten-Downloads Exposee Terminangaben Mindestgebot. Output Recherchebericht mit Trefferprotokoll Gutachten-Links Terminliste und Recherchegrenzen. Abgrenzung zu zvg-bieterangebot-bewertung (Investorenbewertung) und zvg-versteigerungsteilnahme im Zwangsverwaltung Zvg."
---

# ZVG-Portal-Recherche

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

