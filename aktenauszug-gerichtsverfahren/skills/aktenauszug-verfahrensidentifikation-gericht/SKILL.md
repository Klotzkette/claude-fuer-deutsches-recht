---
name: aktenauszug-verfahrensidentifikation-gericht
description: "Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Kläger Beklagte Streithelfer mit Anschrift gesetzlicher Vertretung Prozessbevollmaechtigten) Instanz und Verfahrensart (Klage Eilverfahren Berufung Revision Beschwerde). Normen §§ 253 261 ZPO Klag..."
---

# Verfahrensidentifikation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Erstellung

1. Liegt die Klageschrift oder der Eröffnungsbeschluss vor? (Aktenzeichen, Parteien)
2. Sind die Prozessbevollmächtigten beider Seiten aus der Akte ersichtlich?
3. Wurde der Streitwert festgesetzt (Streitwertbeschluss) oder nur vorläufig angegeben?
4. Gibt es Streithelfer oder Nebenintervenienten?

## Zentrale Normen

- § 253 Abs. 2 Nr. 1 ZPO — Klageschrift muss Gericht, Parteien und Streitgegenstand bezeichnen
- § 261 Abs. 1 ZPO — Anhängigkeit mit Einreichung der Klage; Rechtshängigkeit mit Zustellung
- §§ 3-9 ZPO — Streitwert (Bewertung Klageantrag, Früchte, Zinsen, Kosten)
- § 63 GKG — Streitwertfestsetzung durch das Gericht; § 68 GKG — Streitwertbeschwerde
- §§ 66-74 ZPO — Streithelfer / Nebenintervention (Voraussetzungen, Rechte)

## Rechtsprechung zur Verfahrensidentifikation

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zu extrahierende Felder

### Gericht und Spruchkörper

- Gericht (vollständige Bezeichnung, z. B. Landgericht Frankfurt am Main)
- Kammer oder Senat (z. B. 3. Zivilkammer, 14. Senat)
- Aktenzeichen (z. B. 3 O 123/23)
- Instanz (Erste Instanz / Berufung / Revision / Beschwerde / Rechtsbeschwerde)

### Verfahrensart

- Ordentliches Klageverfahren (ZPO)
- Eilverfahren (einstweilige Verfügung § 935 ff. ZPO / einstweilige Anordnung)
- Berufungsverfahren (§ 511 ff. ZPO)
- Revisionsverfahren (§ 542 ff. ZPO)
- Strafverfahren (StPO)
- Verwaltungsverfahren (VwGO)
- Arbeitsgerichtsverfahren (ArbGG)
- Sozialgerichtsverfahren (SGG)
- Sonstiges (Beschwerde, PKH, Streitwertbeschwerde)

### Streitwert

- Festgesetzter Streitwert (soweit bekannt)
- Vorläufiger Streitwert (soweit Antrag gestellt)
- Gebührenstreitwert (sofern abweichend)

### Parteien

Für jede Partei:

| Feld | Inhalt |
|---|---|
| Bezeichnung | Kläger / Beklagter / Berufungskläger / Streithelfer etc. |
| Name / Firma | Vollständige Bezeichnung |
| Anschrift | Straße PLZ Ort |
| Gesetzliche Vertretung | (bei juristischen Personen) |
| Prozessbevollmächtigter | Kanzlei und Rechtsanwalt |
| Anschrift Bevollmächtigter | Straße PLZ Ort |

### Streithelfer / Nebenintervenienten

- Benennung der Partei, auf deren Seite der Streithelfer steht
- Eigene Bevollmächtigung wenn vorhanden

## Output-Vorlage

```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Verfahrensidentifikation

**Gericht:** Landgericht [Stadt]
**Kammer:** [X]. Zivilkammer
**Aktenzeichen:** [AZ]
**Instanz:** Erste Instanz
**Verfahrensart:** Ordentliches Klageverfahren (ZPO)
**Streitwert:** [EUR oder "nicht festgesetzt"]

### Parteien

| Rolle | Partei | Anschrift | Prozessbevollmächtigter |
|---|---|---|---|
| Kläger | [Name] | [Adresse] | [Kanzlei / RA] |
| Beklagter | [Name] | [Adresse] | [Kanzlei / RA] |
```

## Hinweise

- Fehlende Felder werden als "nicht aus Akte ersichtlich" gekennzeichnet, nicht geschätzt.
- Bei mehreren Klägern oder Beklagten wird jede Person separat aufgeführt.
- Streithelfer werden gesondert unter der Hauptparteitabelle gelistet.
- Keine Bewertung der Parteibezeichnung (z. B. ob Kläger wirklich klagebefugt ist).

---
