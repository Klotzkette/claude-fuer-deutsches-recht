---
name: ropa-bdsg-besondere-art-9-categories
description: "Für RoPA bei besonderen Datenkategorien – Art. 9 DSGVO, Paragraf 26 BDSG, Art. 10 DSGVO: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# RoPA bei besonderen Datenkategorien – Art. 9 DSGVO, § 26 BDSG, Art. 10 DSGVO

## Zweck

Behandelt die erhoehten Dokumentationsanforderungen im Verzeichnis von Verarbeitungstaetigkeiten bei besonderen Datenkategorien nach Art. 9 DSGVO (sensitive Daten), Beschäftigtendaten nach § 26 BDSG und Daten über strafrechtliche Verurteilungen oder Straftaten nach Art. 10 DSGVO. Solche Verarbeitungen brechen die KMU-Ausnahme nach Art. 30 Abs. 5 DSGVO und ziehen ueblicherweise eine DSFA-Pflicht (Art. 35 DSGVO) nach sich.

## Wann dieses Modul hilft

- Arztpraxis, Krankenhaus, Pflegedienst, Apotheke baut RoPA auf.
- Personalabteilung dokumentiert Krankheitstage, BEM-Daten, Schwerbehindertenstatus.
- Kanzlei verarbeitet Mandantendaten mit Bezug zu Gesundheit, Religion, sexueller Orientierung, Strafverfahren.
- Versicherer dokumentiert Gesundheits- oder Schadendaten.
- Verein dokumentiert religioese oder gewerkschaftliche Zugehoerigkeit der Mitglieder.
- Biometrische Verfahren (Fingerprint-Login, Gesichtserkennung) im Einsatz.

## Rechtlicher Rahmen

### Art. 9 Abs. 1 DSGVO – Verbotsprinzip

Verarbeitung ist verboten, soweit sie ergibt:

- rassische und ethnische Herkunft,
- politische Meinungen,
- religioese oder weltanschauliche Ueberzeugungen,
- Gewerkschaftszugehoerigkeit,
- genetische Daten,
- biometrische Daten zur eindeutigen Identifizierung,
- Gesundheitsdaten,
- Daten zum Sexualleben oder der sexuellen Orientierung.

### Art. 9 Abs. 2 DSGVO – Ausnahmen

Verarbeitung zulässig u. a. bei: ausdruecklicher Einwilligung (lit. a), Arbeitsrecht und Sozialrecht (lit. b), lebenswichtigem Interesse (lit. c), Vereinen und Religionsgemeinschaften (lit. d), öffentlich gemachten Daten (lit. e), Rechtsanspruechen (lit. f), erhebliches öffentliches Interesse (lit. g), Gesundheits- und Sozialfürsorge (lit. h), öffentliche Gesundheit (lit. i), Archiv-/Forschungs-/Statistikzwecke (lit. j).

### § 26 BDSG – Beschäftigtendaten

Prüfe § 26 BDSG absatz- und zweckbezogen. Die Entscheidung zur hessischen Beschäftigtendatennorm gibt den Prüfmaßstab für die Anwendbarkeit nationaler Vorschriften vor. Prüfe die spezifischen Garantien nach Art. 88 Abs. 2 DSGVO und die eigenständig einschlägige Grundlage nach Art. 6 DSGVO. Bei besonderen Datenkategorien kommt Art. 9 DSGVO hinzu, etwa Art. 9 Abs. 2 lit. b in Verbindung mit § 26 Abs. 3 BDSG. [EuGH, Urteil vom 30.03.2023 – C-34/21, Rn. 65–89](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0034).

### § 22 BDSG

§ 22 Abs. 1 BDSG enthält zweck- und stellenbezogene Erlaubnisse, etwa für die Gesundheitsvorsorge oder Beurteilung der Arbeitsfähigkeit unter den dortigen Geheimhaltungsvoraussetzungen. Erfasst der Vorgang § 22 Abs. 1 BDSG, sind die angemessenen und spezifischen Maßnahmen nach § 22 Abs. 2 BDSG zu bestimmen und nachvollziehbar zu dokumentieren. Für das RoPA den Verweis auf das Schutzkonzept aufnehmen. [§ 22 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__22.html).

### Art. 10 DSGVO

Daten über strafrechtliche Verurteilungen und Straftaten dürfen nur unter behoerdlicher Aufsicht oder aufgrund nationalen Rechts verarbeitet werden.

## Ablauf / Checkliste

1. **Identifikation:** Welche der oben genannten Kategorien faellt an? Prüfe sowohl direkte Erhebung als auch Rueckschluss (z. B. Fotos können ethnische oder gesundheitliche Hinweise enthalten).
2. **Rechtsgrundlage:** Doppelte Rechtsgrundlage erforderlich – Art. 6 Abs. 1 DSGVO **und** Art. 9 Abs. 2 DSGVO bzw. § 26 oder § 22 BDSG.
3. **Erforderlichkeit:** strenger Maßstab; prüfe Alternativen (Pseudonymisierung, Aggregation).
4. **DSFA-Prüfung:** Art. 35 Abs. 3 lit. b DSGVO – DSFA in der Regel obligatorisch bei umfangreicher Verarbeitung besonderer Kategorien.
5. **TOMs:** § 22 Abs. 2 BDSG fordert spezifische Maßnahmen (Pseudonymisierung, Zugriffsbeschraenkung, Auditing, Schulung).
6. **RoPA-Eintrag:** zusaetzliche Spalte oder Markierung "Art. 9 DSGVO" mit Verweis auf Rechtsgrundlage und DSFA.
7. **Loeschfristen:** restriktiv; Gesundheitsdaten oft 10 Jahre (§ 630f Abs. 3 BGB Patientenakte), aber nicht laenger.

## Mustertext / Template

### Zusatzspalten für besondere Datenkategorien

| Verarbeitung | Datenkategorie (Art. 9) | Doppelte Rechtsgrundlage | DSFA-Verweis | Spezifische TOMs (§ 22 Abs. 2 BDSG) |
|---|---|---|---|---|
| Patientenakte | Gesundheitsdaten | Art. 6 Abs. 1 lit. b + Art. 9 Abs. 2 lit. h DSGVO; § 22 Abs. 1 Nr. 1 lit. b BDSG | DSFA-Ziff. 3 | Rollenbasierter Zugriff, Pseudonymisierung Forschungsdatensatz, Verschluesselung at-rest |
| BEM-Verfahren | Gesundheitsdaten Beschäftigte | Art. 6 Abs. 1 lit. c + Art. 9 Abs. 2 lit. b DSGVO; § 26 Abs. 3 BDSG | DSFA-Ziff. 7 | Getrennte Akte, eingeschraenkter Personenkreis, dokumentierter Zugriff |
| Glaubensbekenntnis Lohnsteuer | Religioese Ueberzeugung | Art. 6 Abs. 1 lit. c + Art. 9 Abs. 2 lit. b DSGVO; § 39 EStG | DSFA-Ziff. 9 | Zugriff nur Lohnbuchhaltung, kein CRM-Sync |
| Biometrischer Zutritt | Biometrische Daten | Art. 6 Abs. 1 lit. f + Art. 9 Abs. 2 lit. a DSGVO (Einwilligung) | DSFA-Ziff. 11 | Lokale Speicherung Template, kein Bild, Loeschung bei Austritt |

### Erweiterung Versionierungs-Footer

Zusatzhinweis: "Diese Verarbeitung beinhaltet besondere Kategorien personenbezogener Daten. DSFA-Pflicht und § 22 Abs. 2 BDSG sind beachtet."

## Typische Fehler

- Nur Art. 6 DSGVO geprueft, Art. 9 DSGVO uebersehen.
- Schwerbehindertenstatus aus dem Personalstammdatensatz ohne gesonderte Markierung als Gesundheitsdatum gefuehrt.
- Biometrie-Login ohne ausdrueckliche Einwilligung und ohne Alternative.
- Keine DSFA, obwohl umfangreiche Gesundheitsdatenverarbeitung.
- "Sensible Daten" pauschal eingetragen ohne konkrete Kategorie.
- TOMs nach Art. 32 statt nach § 22 Abs. 2 BDSG (zusaetzliche Anforderungen).
- Religionszugehoerigkeit aus Lohnsteuerklasse abgeleitet und ungesichert im allgemeinen HR-System.

## Quellen Stand 11/2026

- VO (EU) 2016/679 (DSGVO), Art. 9, Art. 10, Art. 30, Art. 35.
- BDSG, §§ 22, 26.
- BGB § 630f (Patientenakte).
- EStG § 39 (Lohnsteuermerkmale).
- EDSA: Leitlinien 03/2019 zur Verarbeitung personenbezogener Daten durch Videoeinrichtungen (Version 2.0 vom 29.01.2020).
- Ein Medizinischer Dienst kann auch die Arbeitsfähigkeit eigener Beschäftigter begutachten, wenn er in der Rolle des Medizinischen Dienstes handelt. Art. 9 Abs. 2 lit. h und Abs. 3 DSGVO, die einschlägigen Anforderungen an die Vertraulichkeit und mindestens eine Rechtsgrundlage nach Art. 6 Abs. 1 DSGVO getrennt prüfen. [EuGH, Urteil vom 21.12.2023 – C-667/21, Rn. 43–55, 61–70 und 71–79](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0667).
