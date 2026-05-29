---
name: mittelstand-corporate-ma-gesellschaftsrecht-register
description: "Corporate Housekeeping und Register: prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschluesse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals für M&A."
---

# Corporate Housekeeping und Register

## Zweck

Prueft HRB/HRA, Gesellschafterlisten, Satzungen, Beschluesse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals im Rahmen von M&A-Transaktionen. Erkennt Defizite und leitet Closing-Deliverables ab.

## Triage — klaere vor Beginn

1. Welche Gesellschaftsformen sind beteiligt — GmbH, AG, KGaA, GmbH & Co. KG, SE?
2. Liegt ein aktueller HR-Auszug (nicht aelter als 1 Woche) fuer Zielgesellschaft, Kaeufer und Verkaeufer vor?
3. Stimmt die Gesellschafterliste im HR-Auszug mit der SPA-Parteistellung ueberein?
4. Liegen die massgeblichen Beschluesse (Gesellschafterversammlung, AR-Beschluss, Hauptversammlungsbeschluss) fuer die Transaktion vor?
5. Sind Vertretungsbefugnisse (Einzelvertretung, Gesamtvertretung, Prokura) geklart und aktuell?
6. Transparenzregister geprueft — stimmt der eingetragene wirtschaftlich Berechtigte mit Datenraum und Signing-Parteien ueberein?

## Zentrale Rechtsgrundlagen

- § 8 GmbHG — Inhalt der Handelsregisteranmeldung; Notarielle Beurkundungspflicht
- § 10 GmbHG — Bekanntmachung im Handelsregister; Wirksamkeit nach Eintragung
- § 15 Abs. 3 GmbHG — Abtretung von GmbH-Anteilen: notarielle Beurkundungspflicht; bei Verstoß Nichtigkeit
- § 16 GmbHG — Legitimation des Gesellschafters: massgeblich ist Gesellschafterliste; gutglaeubiger Erwerb moeglich
- § 40 GmbHG — Gesellschafterliste nach Anteilsuebertragung: Einreichung durch Notar oder Geschaeftsfuehrer binnen eines Monats
- § 76 AktG — Vertretungsmacht des Vorstands; Prokura §§ 48-53 HGB
- § 19 GwG i.V.m. § 20 TranspRG — Transparenzregisterpflicht; Meldung des wirtschaftlich Berechtigten
- § 2 GmbHG — Beurkundungspflicht des Gesellschaftsvertrags
- §§ 53, 54 GmbHG — Satzungsaenderung: Gesellschafterbeschluss mit Dreiviertelmehrheit und notarielle Beurkundung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **HR-Auszug abrufen:** aktuellen Handelsregisterauszug HRB/HRA fuer alle beteiligten Gesellschaften (nicht aelter als 1 Woche vor Signing); Abgleich mit SPA-Parteibezeichnungen
2. **Gesellschafterliste pruefen:** Eintrag im HR mit Datenraum-Gesellschafterliste, SPA-Garantien und Transaktionsstruktur abgleichen; Divergenzen → Red Flag
3. **Satzungscheck:** aktuell geltende Satzung im Datenraum; Genehmigungspflichten (Vinkulierung, Zustimmungsvorbehalte AR, § 111 Abs. 4 AktG) pruefen
4. **Beschluesse pruefen:** alle fuer die Transaktion relevanten Beschluesse (Gesellschafterversammlungs-Protokoll, AR-Beschluss, Board-Resolution) auf Beschlussfaehigkeit, Mehrheitserfordernis und Form pruefen
5. **Vertretungsmacht klaren:** Zeichnungsberechtigung, Prokura-Eintrag, In-sich-Geschaeft-Befreiung (§ 181 BGB), Gesamtvertretung
6. **Transparenzregister:** wirtschaftlich Berechtigte gemaess § 3 GwG pruefen; Eintrag aktuell? Nach Closing-Meldepflicht innerhalb 2 Wochen (§ 20 TranspRG)
7. **Closing Deliverables ableiten:** Gesellschafterliste neu (§ 40 GmbHG), HR-Anmeldungen, Notartermin, Beglaubigungen
8. **Corporate-Approval-Tabelle erstellen:** je Partei: Gremium, Beschlussdatum, Mehrheit, Form, Vollmacht

## Entscheidungsbaum

- GmbH-Anteilsuebertragung → § 15 Abs. 3 GmbHG Notarpflicht → ohne Notar: nichtig
- Vinkulierung in Satzung → Zustimmungspflicht pruefen → fehlt: Unwirksamkeit der Uebertragung
- AR-Genehmigungsvorbehalt § 111 Abs. 4 AktG → Board Resolution ausreichend? → ggf. AR-Sonderbeschluss erforderlich
- Transparenzregisterdivergenz → Meldepflicht § 20 TranspRG nach Closing → Frist 2 Wochen

## Output-Template: Corporate Approval Tabelle

**Adressat:** Deal-Team intern — Tonfall sachlich-strukturiert

```
CORPORATE APPROVALS REGISTER
Deal: [DEALNAME] — Datum: [DATUM]

| Partei | Gremium | Beschlussdatum | Mehrheit | Form | Vollmacht | Status |
|--------|---------|---------------|---------|------|----------|--------|
| [KAEUFER] | GF/Vorstand | [DATUM] | Einfach | Intern | [NAME] | OK |
| [VERKAEUFER] | GV | [DATUM] | 3/4 | Notariell | [NOTAR] | OK |
| [ZIELGES.] | AR | [DATUM] | Einfach | Schriftlich | [NAME] | TODO |
```

## Rote Schwellen

- Gesellschafterliste nicht eingereicht: Stimmrechte des Erwerbers nach § 16 Abs. 1 GmbHG nicht durchsetzbar
- Vertretungsmacht unklar: Signing-Vollmacht ungueltig; Transaktion angreifbar
- Transparenzregister veraltet: Bussgeld bis 100.000 EUR nach § 56 GwG
- Beschluss mit unzureichender Mehrheit: Satzungsaenderung oder Anteilsabtretung nichtig

## Standardausgabe

- Corporate Approval Tabelle
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe
- Belegkette: Dokument, Datum, Version, Fundstelle

## Uebergabe an andere Skills

- Registerabruf → `mittelstand-corporate-ma-handelsregisterabruf`
- Closing Deliverables → `mittelstand-corporate-ma-closing-bible-archiv`
- Transparenzregister/GwG → `mittelstand-corporate-ma-conflict-gwg-sanctions`

## Vorlagen

- assets/templates/handelsregister-corporate-housekeeping.md
- assets/templates/closing-deliverables-register.md
