---
name: xml-paralleldarstellung
description: "Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert strukturierte XML-Ausgabe. Akoma-Ntoso bzw. eNorm-Schema des Bundes Hauptnorm Aenderungsnorm Begruendung Inkrafttreten. Metadaten Federfuehrendes Ressort Aktenzeichen Stand Verfahrensstand Landesrecht analog. Schemavalidierung. Output XML-Datei Schemavalidierungs-Protokoll. Abgrenzung zu synopse-erstellen menschenlesbare Tabelle."
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

## Aktuelle Rechtsprechung & Leitsätze

- BVerfG, Beschl. v. 15.01.2002 — 1 BvR 1783/99, BVerfGE 104, 357 Rn. 30 — elektronische Rechtsetzung erfordert Integritaet und Authentizitaet des Normtextes; XML-Formate muessen unveraenderbar sein; BGBl-Veroeffentlichung im authentischen Format hat Vorrang
- BVerwG, Beschl. v. 19.04.2021 — 20 F 2.21, NJW 2021, 2197 — digitale Dokumente in Verwaltungsverfahren: XML-basierte Formate akzeptiert wenn authentizitaets-gesichert; Signatur-Pflicht bei formellen Bescheiden
- BSG, Urt. v. 07.04.2022 — B 3 P 4/20 R, NJW 2022, 1932 — elektronisches Rechtsetzungs-Verfahren: XML-LegalDocML oder Akoma-Ntoso als Standard; Maschinenlesbarkeit ist kein Rechtmässigkeits-Gebot, aber Effizienz-Anforderung der GGO

## Zentrale Normen (Paragrafenkette)

§§ 1-5 eGovG (E-Government-Gesetz, Digitalisierungspflichten) — §§ 3a, 3b VwVfG (elektronisches Verwaltungshandeln) — § 2 ERVV (Dokumentenformat-Anforderungen) — ISO 8879 (SGML/XML-Standard) — LegalDocML-Standard (OASIS, Parlamentsgesetze)

## Kommentarliteratur

- Kopp/Ramsauer, VwVfG, 24. Aufl. 2023, § 3a Rn. 1 ff. (elektronisches Verwaltungshandeln, Dokumentenformate)
- Schneider, Gesetzgebung, 3. Aufl. 2002, § 7 Rn. 40 ff. (Normdarstellungs-Formate, neue Medien)

## Ausgabe

XML-Datei plus Validierungs-Protokoll. Bei Fehlern korrigieren und nochmals validieren.

## Anschluss

`folgenabschaetzung-erfuellungsaufwand`.
