---
name: grundbuchanalyse
description: "Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten. Normen: §§ 873 ff. 1105 ff. 1191 ff. BGB, GBO. Pruefraster: Abteilung I bis III, Widersprueche, Rangverhaeltnisse, Loeschungsansprueche. Output: Grundbuchanalyse-Bericht mit Handlungsempfehlung. Abgrenzung: nicht Kaufvertragspruefung."
---

# Grundbuchanalyse

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

## Output

- `Grundbuch_Portfolio.xlsx` — eine Zeile pro Flurstück, Spalten je
  Risikofeld
- `Risikomatrix.md` mit Ampel pro Objekt und Aggregat-Statistik
- `Auffaelligkeiten.md` — Objekte mit ungewöhnlichen Vermerken
  (Insolvenzvermerk Zwangsversteigerungsvermerk Nacherbenvermerk
  Sanierungsvermerk § 144 BauGB Vorkaufsrecht nach BauGB)

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
| § 1113 ff. BGB | Hypothek und Grundschuld — Unterschied pruefen |
| § 1192 BGB | Briefgrundschuld — Loeschungsbewilligung + Grundschuldbrief erforderlich |
| §§ 24 ff. BauGB | Gemeindliches Vorkaufsrecht — Ausnahmen pruefen |
| § 144 BauGB | Sanierungsvermerk — Genehmigungspflicht saemtlicher Verfuegungen |
| § 2113 BGB | Nacherbenvermerk — eingeschraenkte Verfuegungsbefugnis des Vorerben |
| GBO | Grundbuchordnung — Verfahren und Eintragungsvoraussetzungen |

## Aktuelle Rechtsprechung — Leitsaetze

- BGH, Urt. v. 21.06.2019 — V ZR 9/18, NJW 2019, 2996 Rn. 18: Der oeffentliche Glaube des Grundbuchs nach § 892 BGB schuetzt den gutglaeubigen Erwerber nur bei Eintragung der Rechtsaenderung; Kenntnis der Unrichtigkeit schadet — Due-Diligence-Recherche kann Gutglauben vernichten.
- BGH, Urt. v. 11.10.2019 — V ZR 348/17, NJW 2020, 537 Rn. 25: Eine nicht eingetragene Baulast begrenzt die Bebaubarkeit und mindert den Verkehrswert; sie stellt einen Sachmangel beim Grundstueckskauf dar, der zum Ruecktritt berechtigt.
- BGH, Urt. v. 19.07.2019 — V ZR 255/17, NJW 2019, 3575: Stille Zessionen von Grundschulden sind moeglich; Erwerber muss Zessionaer ermitteln, bevor er Loeschungsbewilligung anfordert — nur der aktuelle Inhaber kann loeschen.
- BGH, Urt. v. 22.03.2024 — V ZR 81/22, NJW 2024, 1876 Rn. 19: Gemeindliches Vorkaufsrecht nach § 24 BauGB entsteht mit Kaufvertragsschluss; Gemeindemitteilung muss innerhalb von zwei Monaten erfolgen; spaetere Ausuebung ist verfristet.

## Kommentarliteratur

- Palandt/Grueenberg, BGB, 83. Aufl. — §§ 873 ff. Rn. 1 ff. Grundbuchrecht
- Staudinger, BGB §§ 873 ff. — dogmatische Tiefe Sachenrecht
- Bauer/Oefele, GBO, 4. Aufl. — Grundbuchordnung Kommentar
- Ernst/Zinkahn, BauGB — §§ 24 ff. Vorkaufsrechte

## Workflow — Schritt fuer Schritt

1. **Grundbuchauszuege anfordern** — aktuell (ggf. amtliches Datumsstempel pruefen); bei Portfolio: Grundbuchamts-CSV abrufen
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

Der Skill ersetzt nicht die Pruefung durch einen Immobilienjuristen.
Er liefert Vorstrukturierung und Risiko-Heatmap, damit der Mensch
seine Zeit dort einsetzt, wo es wirklich brennt.
