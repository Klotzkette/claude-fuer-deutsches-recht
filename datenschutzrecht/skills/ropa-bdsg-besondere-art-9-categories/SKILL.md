---
name: ropa-bdsg-besondere-art-9-categories
description: "RoPA-Besonderheiten bei besonderen Datenkategorien nach Art. 9 DSGVO (Gesundheit, biometrische Daten, Religion, Gewerkschaftszugehoerigkeit), bei Beschaeftigtendaten § 26 BDSG und strafrechtlichen Verurteilungen Art. 10 DSGVO. Erhoehte Anforderungen an Zweckbestimmung, Erforderlichkeit, Rechtsgrundlage und TOMs."
---

# RoPA bei besonderen Datenkategorien – Art. 9 DSGVO, § 26 BDSG, Art. 10 DSGVO

## Zweck

Dieser Skill behandelt die erhoehten Dokumentationsanforderungen im Verzeichnis von Verarbeitungstaetigkeiten bei besonderen Datenkategorien nach Art. 9 DSGVO (sensitive Daten), Beschaeftigtendaten nach § 26 BDSG und Daten ueber strafrechtliche Verurteilungen oder Straftaten nach Art. 10 DSGVO. Solche Verarbeitungen brechen die KMU-Ausnahme nach Art. 30 Abs. 5 DSGVO und ziehen ueblicherweise eine DSFA-Pflicht (Art. 35 DSGVO) nach sich.

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

Verarbeitung zulaessig u. a. bei: ausdruecklicher Einwilligung (lit. a), Arbeitsrecht und Sozialrecht (lit. b), lebenswichtigem Interesse (lit. c), Vereinen und Religionsgemeinschaften (lit. d), oeffentlich gemachten Daten (lit. e), Rechtsanspruechen (lit. f), erhebliches öffentliches Interesse (lit. g), Gesundheits- und Sozialfürsorge (lit. h), öffentliche Gesundheit (lit. i), Archiv-/Forschungs-/Statistikzwecke (lit. j).

### § 26 BDSG – Beschaeftigtendaten

§ 26 BDSG bleibt nach Aufhebung durch BVerfG-Rechtsprechung und nachfolgende Gesetzgebung als Rechtsgrundlage praeskriptiv relevant; daneben kommen Kollektivvereinbarungen (§ 26 Abs. 4 BDSG) und Einwilligung (§ 26 Abs. 2 BDSG) in Betracht.

### § 22 BDSG

§ 22 BDSG regelt die Verarbeitung besonderer Datenkategorien zu im öffentlichen Interesse liegenden Zwecken, für Beschaeftigungszwecke, für praeventive Medizin u. a.; § 22 Abs. 2 BDSG verlangt **spezifische TOMs**, die im RoPA dokumentiert werden muessen.

### Art. 10 DSGVO

Daten ueber strafrechtliche Verurteilungen und Straftaten duerfen nur unter behoerdlicher Aufsicht oder aufgrund nationalen Rechts verarbeitet werden.

## Ablauf / Checkliste

1. **Identifikation:** Welche der oben genannten Kategorien faellt an? Pruefe sowohl direkte Erhebung als auch Rueckschluss (z. B. Fotos koennen ethnische oder gesundheitliche Hinweise enthalten).
2. **Rechtsgrundlage:** Doppelte Rechtsgrundlage erforderlich – Art. 6 Abs. 1 DSGVO **und** Art. 9 Abs. 2 DSGVO bzw. § 26 oder § 22 BDSG.
3. **Erforderlichkeit:** strenger Massstab; pruefe Alternativen (Pseudonymisierung, Aggregation).
4. **DSFA-Pruefung:** Art. 35 Abs. 3 lit. b DSGVO – DSFA in der Regel obligatorisch bei umfangreicher Verarbeitung besonderer Kategorien.
5. **TOMs:** § 22 Abs. 2 BDSG fordert spezifische Massnahmen (Pseudonymisierung, Zugriffsbeschraenkung, Auditing, Schulung).
6. **RoPA-Eintrag:** zusaetzliche Spalte oder Markierung "Art. 9 DSGVO" mit Verweis auf Rechtsgrundlage und DSFA.
7. **Loeschfristen:** restriktiv; Gesundheitsdaten oft 10 Jahre (§ 630f Abs. 3 BGB Patientenakte), aber nicht laenger.

## Mustertext / Template

### Zusatzspalten für besondere Datenkategorien

| Verarbeitung | Datenkategorie (Art. 9) | Doppelte Rechtsgrundlage | DSFA-Verweis | Spezifische TOMs (§ 22 Abs. 2 BDSG) |
|---|---|---|---|---|
| Patientenakte | Gesundheitsdaten | Art. 6 Abs. 1 lit. b + Art. 9 Abs. 2 lit. h DSGVO; § 22 Abs. 1 Nr. 1 lit. b BDSG | DSFA-Ziff. 3 | Rollenbasierter Zugriff, Pseudonymisierung Forschungsdatensatz, Verschluesselung at-rest |
| BEM-Verfahren | Gesundheitsdaten Beschaeftigte | Art. 6 Abs. 1 lit. c + Art. 9 Abs. 2 lit. b DSGVO; § 26 Abs. 3 BDSG | DSFA-Ziff. 7 | Getrennte Akte, eingeschraenkter Personenkreis, dokumentierter Zugriff |
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

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` für Basis.
- `ropa-art-30-controller-deutsch-vorlage` für Basisvorlage.
- `dsfa-erstellung` für Art. 35 DSGVO.
- `mitarbeiter-datenschutz-26-bdsg` (falls vorhanden) für Beschaeftigtenkontext.
- `avv-tom-art-32-dsgvo-anlage` für TOM-Anhang.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 9, Art. 10, Art. 30, Art. 35.
- BDSG, §§ 22, 26.
- BGB § 630f (Patientenakte).
- EStG § 39 (Lohnsteuermerkmale).
- EDSA: Leitlinien 03/2019 zur Verarbeitung personenbezogener Daten durch Videoeinrichtungen (Version 2.0 vom 29.01.2020).
- BVerfG, Beschluss vom 11.11.2020 – 1 BvR 3214/15 (Antiterrordatei-Folgeentscheidung) – bei Anpassung des § 22 BDSG sinngemaess beachten; vor Zitierung amtliche Fundstelle pruefen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
