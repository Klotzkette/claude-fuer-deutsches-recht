---
name: ropa-art-30-controller-deutsch-vorlage
description: "Vollvorlage für das Verzeichnis von Verarbeitungstaetigkeiten des Verantwortlichen nach Art. 30 Abs. 1 DSGVO. Tabellenstruktur mit allen sieben Mindestinhalten, ausgefuelltes Beispiel für Personalverwaltung, Mandantenakte, Kontaktformular, CRM. Direkt nutzbare Vorlage für Kanzleien und Unternehmen."
---

# RoPA-Vorlage Verantwortlicher (Controller) – Deutsch

## Wann dieses Modul hilft

- Erstaufbau eines Verarbeitungsverzeichnisses in der Kanzlei oder im Mandantenunternehmen.
- Vorlage gegenueber Aufsichtsbehoerde gemäß Art. 30 Abs. 4 DSGVO.
- Auditvorbereitung; Lueckenanalyse eines bestehenden RoPA.
- Standardisierung mehrerer Standorte oder Mandantengruppen.

## Rechtlicher Rahmen

Art. 30 Abs. 1 DSGVO – Pflichtinhalte für Verantwortliche:

a) Name und Kontaktdaten des Verantwortlichen, ggf. gemeinsam Verantwortlicher, Vertreter und Datenschutzbeauftragter;
b) Zwecke der Verarbeitung;
c) Beschreibung der Kategorien betroffener Personen und der Kategorien personenbezogener Daten;
d) Kategorien von Empfaengern, gegenueber denen die personenbezogenen Daten offengelegt worden sind oder noch offengelegt werden, einschliesslich Empfaenger in Drittlaendern oder internationalen Organisationen;
e) ggf. Uebermittlungen in ein Drittland oder an eine internationale Organisation, einschliesslich der Angabe des betreffenden Drittlands sowie bei Uebermittlungen gemäß Art. 49 Abs. 1 Unterabs. 2 DSGVO Dokumentierung der geeigneten Garantien;
f) wenn möglich, vorgesehene Fristen für die Loeschung der verschiedenen Datenkategorien;
g) wenn möglich, allgemeine Beschreibung der TOMs gemäß Art. 32 Abs. 1 DSGVO.

## Ablauf / Checkliste

1. Deckblatt mit Verantwortlicher-Stammdaten anlegen.
2. Pro Geschäftsprozess eine Zeile.
3. Spalten gemäß Vorlage befuellen.
4. Bei Drittlandtransfer Transferinstrument (SCC, DPF, BCR) eintragen.
5. Loeschfristen konkret, nicht "nach gesetzlichen Vorgaben".
6. TOMs in eigenes Anhangsdokument; im RoPA Verweis.
7. Versionierung am Fuss.
8. Jaehrlicher Review-Termin im Kalender.

## Mustertext / Template

### Deckblatt

```
Verantwortlicher: [Firmenname / Kanzleiname]
Anschrift: [...]
Vertreter (Art. 27): [falls anwendbar]
Datenschutzbeauftragter: [Name, Kontakt]
Aufsichtsbehoerde: [zuständige LDI / BfDI]
Erstellt: [Datum]
Letzte Aenderung: [Datum]
Version: [v1.0]
```

### Tabelle (Pflichtspalten)

| Nr. | Verarbeitungstaetigkeit | Zweck | Rechtsgrundlage | Kategorien Betroffene | Datenkategorien | Empfaengerkategorien | Drittland / Garantie | Loeschfrist | TOM-Verweis |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Personalverwaltung Beschäftigte | Begruendung, Durchfuehrung und Beendigung des Arbeitsverhaeltnisses | Art. 6 Abs. 1 lit. b DSGVO, § 26 BDSG | Beschäftigte, Bewerber | Stammdaten, Vertragsdaten, Lohndaten, Krankheitszeiten | Sozialversicherungstraeger, Finanzamt, Lohnbuchhaltungsdienstleister | nein | 10 Jahre nach Ausscheiden (§ 257 HGB, § 147 AO); Bewerberdaten 6 Monate | TOM-Anhang Ziff. 1, 3, 5 |
| 2 | Mandantenakte (Rechtsdienstleistung) | Anbahnung, Durchfuehrung und Abrechnung von Mandaten | Art. 6 Abs. 1 lit. b und f DSGVO; § 50 BRAO | Mandanten, Gegner, Zeugen | Stammdaten, Korrespondenz, Schriftsaetze, Honorardaten | Gerichte, Behörden, Gegenanwaelte, Versicherer | nein | 6 Jahre nach Mandatsende (§ 50 Abs. 1 BRAO); steuerlich relevante Belege 10 Jahre | TOM-Anhang Ziff. 1, 2, 4, 6 |
| 3 | Kontaktformular Website | Beantwortung von Anfragen | Art. 6 Abs. 1 lit. b oder f DSGVO | Interessenten, Mandanten | Name, E-Mail, Telefon, Anfrageinhalt | Hosting-Dienstleister (AVV) | nein | 6 Monate nach Erledigung | TOM-Anhang Ziff. 1, 5 |
| 4 | CRM Vertrieb | Kundenpflege, Akquise | Art. 6 Abs. 1 lit. b und f DSGVO | Bestandskunden, Interessenten | Stammdaten, Kontakthistorie, Umsatzdaten | CRM-SaaS-Anbieter (USA) | USA – EU-US DPF (Aktiv-Listing dokumentiert in Anhang DPF-Liste) | 3 Jahre nach letztem Kontakt | TOM-Anhang Ziff. 1, 2, 5 |

### Versionierungs-Footer

```
Version 1.0 – Erstanlage – [Datum, Bearbeiter]
Version 1.1 – [Aenderung] – [Datum, Bearbeiter]
```

## Typische Fehler

- "Zweck" und "Rechtsgrundlage" vermischt – bitte trennen.
- Empfaengerkategorien als Einzelnamen ("Frau Mueller, Steuerberater") statt Kategorie ("Steuerberatung").
- Drittland nur "USA" ohne Transferinstrument.
- Loeschfristen pauschal "10 Jahre" ohne Differenzierung nach Datenkategorie.
- TOM-Spalte mit vollem Wortlaut der Anlage 32 DSGVO – besser Verweis.
- Kein DSB-Eintrag obwohl Bestellpflicht (§ 38 BDSG) besteht.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 30 Abs. 1.
- BDSG, § 26 (Beschäftigtendaten), § 38 (DSB-Pflicht).
- BRAO § 50 (Aktenaufbewahrung).
- HGB § 257, AO § 147 (handels-/steuerrechtliche Aufbewahrung).
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).
