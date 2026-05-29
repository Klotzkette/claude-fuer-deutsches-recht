---
name: grosskanzlei-corporate-ma-handelsregisterabruf
description: "Handelsregister-Abruf und Registerrecherche für M&A-Transaktionen: Anwendungsfall Anwalt recherchiert offiziellen Registerstand für Zielgesellschaft, Kaeufer-Holding, Komplementaer-GmbH oder Beteiligungsketten. §§ 8-10 GmbHG, §§ 29 ff. HGB, § 15 HGB Registerpublizitaet. Prüfraster Eintragungsstand, Vertretungsmacht, Satzungsversion, Eintragungsdatum, aktuell laufende Registerverfahren. Output Registerauszug-Auswertung mit gesellschaftsrechtlichem Status und Handlungsempfehlungen. Abgrenzung zu Corporate-Housekeeping für interne Prüfung und zu Gesellschaftsrecht-Register."
---

# Handelsregister- und Registerabruf

## Zweck

Fuehrt offizielle Registerabrufe fuer Zielgesellschaft, Verkaeufer, Erwerber, Beteiligungsketten, KG und Organstellung. Prueft Registerstand, Vertretungsmacht, Satzungsversionen und Eintragungsdatum.

## Triage

1. Welche Gesellschaften sind zu recherchieren — Zielgesellschaft, Muttergesellschaft, Kaeufer-Holding, Komplementaer-GmbH?
2. Wird ein aktueller HR-Auszug benoetigt (nicht aelter als 1 Woche) oder ein historischer Registerstand?
3. Sind Beteiligungsketten mit auslaendischen Gesellschaften zu kartieren — lokale Register (UK Companies House, Niederlande KvK, Frankreich INPI)?
4. Gibt es bekannte Unstimmigkeiten zwischen Datenraum-Angaben und HR-Stand?

## Zentrale Rechtsgrundlagen

- §§ 8-10 GmbHG — Handelsregisteranmeldung der GmbH: Inhalt, notarielle Beglaubigung
- §§ 29 ff. HGB — Pflicht zur Handelsregistranmeldung; negative Publizitaet (§ 15 HGB): nicht eingetragene Tatsachen koennen Dritten nicht entgegengesetzt werden
- § 16 GmbHG — Legitimationswirkung der Gesellschafterliste: eingetragener Gesellschafter gilt als Inhaber der Rechte
- § 20 TranspRG — Transparenzregister: wirtschaftlich Berechtigter; Meldepflicht; Zugaenglichkeit
- § 40 GmbHG — Einreichung der Gesellschafterliste nach Anteilsuebertragung; Frist 1 Monat

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Abruf-Liste erstellen:** alle zu recherchierenden Gesellschaften (inkl. Komplementaer-GmbH, Holdinggesellschaften) auflisten
2. **Abruf ueber handelsregister.de:** HRB- oder HRA-Nummer eingeben; aktuellen Ausdruck und vollstaendige Urkundssammlung (Satzung, aeltere Versionen) abrufen
3. **Gesellschafterliste pruefen:** stimmt mit SPA-Parteistellung ueberein? Eintragungsdatum aktuell?
4. **Vertretungsmacht auslesen:** Einzelvertretung, Gesamtvertretung, Prokura — alle Eintragungen erfassen
5. **Transparenzregister:** Abgleich mit wirtschaftlich Berechtigten nach GwG; Abweichungen notieren
6. **Beteiligungskette kartieren:** Organigramm mit HR-belegten Beteiligungsstufen erstellen

## Output-Template: Registerabruf-Protokoll

**Adressat:** Deal-Team intern — Tonfall sachlich

```
REGISTERABRUF-PROTOKOLL
Deal: [DEALNAME] — Datum: [DATUM]

| Gesellschaft | HR-Nr. | Abruf-Datum | Aktuell? | Gesellschafter laut Liste | Vertretung | Anmerkung |
|-------------|--------|------------|----------|--------------------------|-----------|-----------|
| [ZIELGES.] | HRB XXX | [DATUM] | JA | [NAME, ANTEIL] | [NAME] GF Einzelv. | OK |
| [HOLDING] | HRB XXX | [DATUM] | JA | [NAME, 100%] | [NAME] GF | OK |
| [KOMP-GMBH] | HRB XXX | [DATUM] | JA | [NAME] | [NAME] GF | Prüfen |

TRANSPARENZREGISTER: [ ] Abgeglichen — WB: [NAME] [ANTEIL %]
OFFENE PUNKTE: [TODO Owner Datum]
```

## Rote Schwellen

- HR-Auszug aelter als 1 Woche vor Signing: aktualisieren
- Gesellschafterliste divergiert von SPA-Angaben: Red Flag; Senior-Review
- Transparenzregister nicht abgeglichen: GwG-Risiko

## Standardausgabe

- Registerabruf-Protokoll
- Beteiligungsketten-Organigramm
- Offene Punkte als `TODO`

## Uebergabe an andere Skills

- Corporate Housekeeping → `grosskanzlei-corporate-ma-gesellschaftsrecht-register`
- GwG/Transparenz → `grosskanzlei-corporate-ma-conflict-gwg-sanctions`

## Vorlagen

- assets/templates/registerabruf-protokoll.md
