---
name: grundbuchanalyse
description: "Für Grundbuchanalyse: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Grundbuchanalyse

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Grundbuchanalyse
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.

## Leitidee

Grundbuchdaten kommen in der Praxis als Stapel von PDF-Auszügen, oft
gescannt, mit dazwischengewürfelten Baulastenverzeichnissen, Flurkarten
und Altlastenausweisen. Der Skill normalisiert alles auf eine
Objekttabelle und ein einheitliches Risikoschema.

## Inputs

- Grundbuchauszüge (.pdf, gescannt oder digital)
- Optional: Baulastenverzeichnis-Ausdrucke
- Optional: Altlastenkataster-Auskuenfte
- Optional: Flurkarten und Lageprüfungen
- Objektliste als .xlsx oder .csv

## Methodik

1. OCR auf gescannten PDFs
2. Pro Auszug Identifikation Bestandsverzeichnis Abteilung I II III
3. Strukturierte Extraktion:
 - Bestandsverzeichnis: Gemarkung Flur Flurstück Wirtschaftsart
 Größe
 - Abteilung I: Eigentümerkette mit Erwerbsgrund
 - Abteilung II: Lasten und Beschraenkungen (Dienstbarkeiten
 Reallasten Vorkaufsrechte Nacherbenvermerk Sanierungsvermerk)
 - Abteilung III: Grundpfandrechte mit Rang Betrag Gläubiger
 Löschungserleichterung Brieftyp
4. Querverweis mit Baulastenverzeichnis (Baulasten existieren NICHT
 im Grundbuch)
5. Risikobewertung pro Objekt und Aggregation auf Portfolio
6. Generierung Risikomatrix Excel-Tabelle und Memo

## Typische Risikofelder

- Briefgrundschuld ohne Löschungsbewilligung
- Rangverhältnis Abteilung III nicht eindeutig
- Dienstbarkeit zugunsten unbekannter Dritter (Leitungsrechte
 Wegerechte)
- Vorkaufsrecht der Gemeinde nach §§ 24 ff. BauGB
- Sanierungsvermerk § 144 BauGB — Genehmigung erforderlich
- Nacherbenvermerk § 2113 BGB
- Insolvenz- oder Zwangsversteigerungsvermerk
- Baulast nicht im Grundbuch aber gegen Eigentümer wirksam
- Altlastenverdachtsfläche und mietminderungsrelevante Schadstoffe

## Beispielformulierungen

- "Werte alle Grundbuchauszüge aus diesem Ordner aus. Erzeuge
 Portfoliosicht und markiere Objekte mit Sanierungsvermerk."
- "Ich habe 87 PDF-Auszüge. Zeig mir Objekte mit offenen
 Briefgrundschulden und Baulasten."
- "Prüfe diese 15 Objekte auf Vorkaufsrechte der Gemeinde nach
 Paragraph 24 BauGB."

## Relevante Normen

| Norm | Inhalt |
|------|--------|
| §§ 873, 877, 885 BGB | Grundbucheintragung als Entstehungsvoraussetzung dinglicher Rechte |
| §§ 892, 893 BGB | Oeffentlicher Glaube des Grundbuchs — gutglaeubiger Erwerb |
| § 883 BGB | Auflassungsvormerkung — schuetzt Eigentuemsverschaffungsanspruch |
| § 1113 ff. BGB | Hypothek und Grundschuld — Unterschied prüfen |
| § 1192 BGB | Briefgrundschuld — Loeschungsbewilligung + Grundschuldbrief erforderlich |
| §§ 24 ff. BauGB | Gemeindliches Vorkaufsrecht — Ausnahmen prüfen |
| § 144 BauGB | Sanierungsvermerk — Genehmigungspflicht saemtlicher Verfuegungen |
| § 2113 BGB | Nacherbenvermerk — eingeschraenkte Verfuegungsbefugnis des Vorerben |
| GBO | Grundbuchordnung — Verfahren und Eintragungsvoraussetzungen |

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026, verifiziert dejure.org)

- **BGH 15.04.2021, V ZB 175/20**: Grundbucheintragung — Bewilligung muss bestimmten Inhalt aufweisen; bei Auflassungsvormerkung Konkretisierung des gesicherten Anspruchs erforderlich. Quelle: dejure.org/2021,14528.
- **BGH 17.09.2021, V ZR 12/21**: WEMoG-Reform; Bauliche Veraenderungen § 20 WEG; Folgen für Grundbucheintragungen bei Sondernutzungsrechten. Quelle: dejure.org/2021,30989.
- **BGH 25.02.2016, V ZR 244/14**: Loeschungsfaehiges Grundpfandrecht — Voraussetzungen § 1183 BGB. Quelle: dejure.org/2016,5478.

Konkrete Entscheidungen vor Ausgabe per dejure.org / bundesgerichtshof.de verifizieren.

## — Schritt für Schritt

1. **Grundbuchauszuege anfordern** — aktuell (ggf. amtliches Datumsstempel prüfen); bei Portfolio: Grundbuchamts-CSV abrufen
2. **Abt. I — Eigentuemerkette** — Luecken im Eigentumsuebergang? Erbfolgenachweis (Erbschein/Erbvertrag) aktuell?
3. **Abt. II — Lasten und Beschraenkungen** — Vorkaufsrechte, Dienstbarkeiten, Nacherbenvermerk, Sanierungsvermerk?
4. **Abt. III — Grundpfandrechte** — Brief- oder Buchgrundschuld? Loeschungsbewilligung beschaffbar? Zession geprueft?
5. **Baulastenverzeichnis** — separat beim Baurechtsamt anfragen (NICHT im Grundbuch)
6. **Altlastenkataster** — Umweltamt; PFAS/BTEX-Belastung?
7. **Risikomatrix erzeugen** — Ampel je Risikofeld

## Adressat und Tonfall

- **Asset-Management**: praegnante Risikomatrix, Handlungsempfehlung pro Objekt
- **Finanzierung/Bank**: Sicherheitenwertanalyse, Rangfragen Abt. III
- **Gericht/Notar**: formell, mit Grundbuchblattnummer und Eintragungsdatum

## Grenzen

Der Skill ersetzt nicht die Prüfung durch einen Immobilienjuristen.
Er liefert Vorstrukturierung und Risiko-Heatmap, damit der Mensch
seine Zeit dort einsetzt, wo es wirklich brennt.
