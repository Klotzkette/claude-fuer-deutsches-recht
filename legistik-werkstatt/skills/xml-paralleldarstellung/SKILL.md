---
name: xml-paralleldarstellung
description: "Erstellt eine maschinenlesbare Paralleldarstellung des Entwurfs in LegalDocML.de oder eNorm-XML. Akoma Ntoso bzw. eNorm-Schema des Bundes. Pro Bestandteil eigene XML-Knoten Hauptnorm Aenderungsnorm Begruendung Inkrafttreten. Metadaten Federfuehrendes Ressort Aktenzeichen Stand Verfahrenstand. Auch fuer Landesrecht analog. Schemavalidierung empfohlen. Endet mit XML-Datei plus Schemavalidierungs-Protokoll. Hilfreich fuer eGesetzgebung BMJ Bundesgesetzblatt online und automatisierte Weiterverarbeitung."
---

# XML-Paralleldarstellung

> Recht muss auch Maschinen lesbar sein.

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

## Ausgabe

XML-Datei plus Validierungs-Protokoll. Bei Fehlern korrigieren und nochmals validieren.

## Anschluss

`folgenabschaetzung-erfuellungsaufwand`.
