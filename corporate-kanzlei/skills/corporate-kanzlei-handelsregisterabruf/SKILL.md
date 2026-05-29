---
name: corporate-kanzlei-handelsregisterabruf
description: "Handelsregister-Daten abrufen und analysieren: Anwalt oder Mandant benoetigt Gesellschaftsstruktur, Haftungsverhältnisse, Offenlegungspflichten aus HRA/HRB, Bundesanzeiger und Transparenzregister. Normen: §§ 8-15 HGB, § 9 GmbHG, §§ 67-68 AktG, GwG §§ 18-20 (Transparenzregister). Prüfraster: Gesellschafterliste, Jahresabschluesse, Prokura, Eintragungsketten, UBO-Identifikation. Output Registerauszug-Analyse, Struktur-Memo, Risikobewertung Offenlegung. Abgrenzung: Anmeldungen siehe gesellschaftsrecht-register; Zielunternehmen-Screening siehe outside-in-target-screening."
---

# Handelsregisterabruf und -analyse

## Triage — klaere vor Beginn

1. Handelsregister-Abteilung: HRA (Einzelkaufleute, Personengesellschaften) oder HRB (Kapitalgesellschaften)?
2. Vollstaendiger Abruf (Chronologischer Ausdruck) oder nur aktueller Stand?
3. Transparenzregister-Abfrage erforderlich (UBO-Identifizierung)?
4. Bundesanzeiger: Jahresabschluesse hinterlegt? (Pflicht nach § 325 HGB ab einer bestimmten Groesse)
5. Auslaendische Gesellschaften: Welches Register? (UK: Companies House; FR: RCS; NL: KVK)
6. Zweck: M&A-DD, GwG-CDD, Kreditpruefung, Lieferanten-Compliance?

## Zentrale Normen

- **§§ 8-10 HGB** — Handelsregister; Eintragungsrecht und -pflicht; Oeffentlichkeit des Registers
- **§ 15 HGB** — negative Publizitaet; Dritte koennen auf den eingetragenen Inhalt vertrauen; nicht eingetragene Tatsachen koennen Dritten nicht entgegengehalten werden
- **§ 16 GmbHG** — Gesellschafterliste; eingetragener Gesellschafter gilt als legitimiert; gutglaeubiger Erwerb
- **§ 325 HGB** — Offenlegungspflicht Jahresabschluss; Fristen; Ordnungsgeldbescheid (§ 335 HGB) bei Versaeum.
- **§§ 18-20 GwG** — Transparenzregister; wirtschaftlich Berechtigter; UBO-Fiktionsfiktion (§ 20 II GwG) wenn Handelsregister-Eintragung
- **§ 9 GwG** — Abfragepflicht aus Transparenzregister bei bestimmten Pflichtigen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## HR-Ausdruck: Analysepunkte

### Fuer GmbH (HRB)
- **Gruendung:** Datum, Gruender, Stammkapital
- **Satzung/Gesellschaftsvertrag:** Aktuelle Fassung; Aenderungschronologie
- **Geschaeftsfuehrer:** Aktuelle und historische GF; Vertretungsbefugnis; § 181 BGB-Befreiung
- **Stammkapital:** Nominal; Veraenderungen (Erhoehungen, Herabsetzungen)
- **Gesellschafterliste:** Aktuell eingetragene Gesellschafter; Anteilsgroessen; Aenderungen
- **Prokuristen / Vollmachten:** Erteilte und erloeschene Prokuren
- **Satzungsaenderungen:** Chronologie; wesentliche Aenderungen

### Fuer AG (HRB)
- **Grundkapital:** Nominal; Aktienarten (Inhaber, Namenaktie, vinkuliert)
- **Vorstand:** Aktuelle Mitglieder; Einzelvertretung vs. Gesamtvertretung
- **Aufsichtsrat:** Mitglieder; Vorsitzender
- **Hauptversammlung:** Zuletzt genehmigte KE; Genehm. Kapital; Genehmigungen
- **Bekanntmachungen:** Kapitalerhoehungen; Satzungsaenderungen; HV-Beschluesse

### Red Flags im HR-Ausdruck

| Signal | Bedeutung |
|---|---|
| Haeufige GF-Wechsel (> 2x in 3 Jahren) | Managementkrise; Gesellschafterstreit |
| Kapitalherabsetzung ohne sichtbaren Grund | Verluste; Reorganisation |
| Eintragungsloeschungen | Insolvenzen, Aufloesung in Vergangenheit |
| Pfandrechte auf Anteile eingetragen | Kreditbesicherung; finanzielle Schwierigkeiten |
| Gesellschafterliste alt (> 1 Jahr) | Aenderungen nicht angemeldet; CoC-Risiko |

## Schritt-fuer-Schritt-Workflow

1. **Vollstaendigen HR-Auszug abrufen** — elektronisch via www.handelsregister.de oder beA; Kosten ca. EUR 4.50
2. **Chronologischen Ausdruck anfordern** — alle historischen Eintragungen (nicht nur aktuell)
3. **Gesellschafterliste pruefen** — aktuell? Widersprueche mit Transaktionsunterlagen?
4. **Transparenzregister abfragen** — UBO identifizieren; Fiktionswirkung pruefen (§ 20 II GwG)
5. **Bundesanzeiger-Recherche** — Jahresabschluesse; Kapitalmarktmitteilungen; Insolvenzen
6. **Prokuren-Check** — wer ist handlungsbevollmaechtig; relevant fuer Vertragsunterschriften
7. **Red Flags dokumentieren** — strukturierter Kommentar mit Handlungsempfehlungen
8. **In DD-Report einfliessen lassen** — Corporate-Workstream aufbauen

## Output-Template HR-Analyse

```
HANDELSREGISTER-ANALYSE
Gesellschaft: [FIRMA GmbH / AG]
HRB-Nummer: [Nr.] — Amtsgericht [Ort]
Abruf-Datum: [DATUM]
Chronologischer Ausdruck: [Ja / Nein]

1. BASISINFORMATIONEN
   Rechtsform: [GmbH / AG]
   Gruendungsdatum: [DATUM]
   Sitz: [ADRESSE]
   Stammkapital/Grundkapital: EUR [BETRAG]

2. AKTUELLE ORGANE
   Geschaeftsfuehrer / Vorstand:
   - [NAME, Geburtsdatum, Vertretungsbefugnis, Befreiung § 181 BGB]
   Aufsichtsrat (falls vorhanden):
   - [NAMEN]

3. GESELLSCHAFTERSTRUKTUR
   [QUELLE: Gesellschafterliste; Stand: Datum]
   - [Gesellschafter 1]: [Anteile, %]
   - [Gesellschafter 2]: [Anteile, %]

4. JAHRESABSCHLUESSE (BUNDESANZEIGER)
   Veroeffentlicht: [Jahre]
   Nicht veroeffentlicht: [Jahren] — RISIKO: § 335 HGB Ordnungsgeld

5. RED FLAGS
   [Liste; Keine wenn keine vorhanden]

6. TRANSPARENZREGISTER
   UBO: [NAME, Nationalitaet, %-Anteil oder Fiktionswirkung]

7. EMPFEHLUNG
   [Ggf. Nachforschung; GwG-Enhanced Sorgfalt; Korrekte Gesellschafterliste einfordern]
```

## Rote Schwellen

- HR-Auszug veraltet → aktuelle Eintragungslage unbekannt; Vollmachtspruefung fehlerhaft
- Gesellschafterliste nicht aktuell → UBO unklar; GwG-CDD unvollstaendig
- Keine Jahresabschluesse veroeffentlicht → § 335 HGB-Verstos; finanzielle Intransparenz
- Gesellschafterliste in den Haenden einer anderen Person als GF → Verdacht auf Treuhander-Struktur

## Quellen

- §§ 8-15 HGB; § 16 GmbHG; § 325 HGB; §§ 18-20 GwG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
