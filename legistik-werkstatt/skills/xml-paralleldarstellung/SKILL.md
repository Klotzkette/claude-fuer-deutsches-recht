---
name: xml-paralleldarstellung
description: "Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert strukturierte XML-Ausgabe. Akoma-Ntoso bzw. eNorm-Schema des Bundes Hauptnorm Aenderungsnorm Begründung Inkrafttreten. Metadaten Federführendes Ressort Aktenzeichen Stand Verfahrensstand Landesrecht analog. Schemavalidierung. Output XML-Datei Schemavalidierungs-Protokoll. Abgrenzung zu synopse-erstellen menschenlesbare Tabelle."
---

# XML-Paralleldarstellung

## Normenanker

Arbeitsfokus: **XML-Paralleldarstellung**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Schemas

### Bund

- **eNorm** des Bundes (XML-Schema des BMJ)
- **LegalDocML.de** (auf Basis Akoma Ntoso, OASIS-Standard)

### Land

Landesrecht-Portale verwenden teilweise eigene XML-Formate, teilweise LegalDocML.de.

## Mindeststruktur

```xml
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
 <act name="entwurf-paragraf-33a-hgb">
 <meta>
 <identification source="#bmj">
 <FRBRWork>
 <FRBRthis value="/akn/de/act/2026/pflichtpostfachg"/>
 <FRBRuri value="/akn/de/act/2026/pflichtpostfachg"/>
 <FRBRdate date="2026-05-23" name="Auftragsdatum"/>
 <FRBRauthor href="#bmj"/>
 <FRBRcountry value="de"/>
 </FRBRWork>
 </identification>
 </meta>
 <body>
 <article eId="art_1">
 <num>Artikel 1</num>
 <heading>Aenderung des Handelsgesetzbuchs</heading>
 <paragraph eId="art_1__para_1">
 <content>
 <p>Das Handelsgesetzbuch ... wird wie folgt geaendert: ...</p>
 </content>
 </paragraph>
 </article>
 </body>
 </act>
</akomaNtoso>
```

## Prüfung

Schema-Validierung via xmllint:

```
xmllint --schema akomaNtoso-3.0.xsd --noout entwurf.xml
```

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 1-5 eGovG (E-Government-Gesetz, Digitalisierungspflichten) — §§ 3a, 3b VwVfG (elektronisches Verwaltungshandeln) — § 2 ERVV (Dokumentenformat-Anforderungen) — ISO 8879 (SGML/XML-Standard) — LegalDocML-Standard (OASIS, Parlamentsgesetze)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

XML-Datei plus Validierungs-Protokoll. Bei Fehlern korrigieren und nochmals validieren.

## Anschluss

`folgenabschaetzung-erfuellungsaufwand`.
