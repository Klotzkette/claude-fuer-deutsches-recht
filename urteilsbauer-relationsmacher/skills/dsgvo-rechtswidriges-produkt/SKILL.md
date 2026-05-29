---
name: dsgvo-rechtswidriges-produkt
description: "Produkt aus dem Ausland auf DSGVO-Rechtswidrigkeit prüfen: Richter oder Anwalt muss beurteilen ob Smartglasses oder IoT-Produkt DSGVO-konform ist. Normen: Art. 3 DSGVO (räumlicher Anwendungsbereich), Art. 5 Abs. 1 lit. c (Datensparsamkeit), Art. 6 (Rechtsgrundlage), Art. 9 (biometrische Daten), Art. 13-14 (Informationspflichten), Art. 44 ff. (Drittlandtransfer), Art. 22 (automatisierte Entscheidung). Prüfraster: Anwendbarkeit, Rechtsgrundlage, Sonderkateg. Daten, Drittlandtransfer. Output DSGVO-Prüfschema mit Ergebnis und Empfehlung. Abgrenzung: allgemeine DSGVO-Beratung siehe datenschutzrecht-Plugin; DSA siehe dsa-dma-Plugin."
---

# DSGVO-rechtswidriges Produkt

Pruefschema, wenn ein technisches Produkt aus dem Ausland nach DSGVO als rechtswidrig zu bewerten ist und der Kaeufer Rückabwicklung will.


## Triage zu Beginn

1. Unterliegt das Produkt dem räumlichen Anwendungsbereich der DSGVO (Art. 3 Abs. 1 oder Abs. 2 DSGVO)?
2. Welche Kategorien personenbezogener Daten werden verarbeitet — biometrische Daten (Art. 9 DSGVO)?
3. Werden Daten in Drittländer übermittelt ohne SCC oder anderen Mechanismus (Art. 44 ff. DSGVO)?
4. Hat der Käufer wirksame Einwilligung erteilt oder scheidet Einwilligung aus (Art. 7 DSGVO)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- Art. 3 DSGVO — räumlicher Anwendungsbereich (Niederlassungs- und Marktortprinzip)
- Art. 6 DSGVO — Rechtsgrundlagen für Verarbeitung
- Art. 7 DSGVO — wirksame Einwilligung
- Art. 9 DSGVO — besondere Kategorien (biometrische Daten, Gesundheitsdaten)
- Art. 44 ff. DSGVO — Drittlandübermittlung (SCC, Angemessenheitsbeschluss)
- Art. 82 DSGVO — Schadensersatz (materiell und immateriell)
- § 134 BGB — Nichtigkeit bei Verstoß gegen Verbotsgesetz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Anwendbarkeit DSGVO prüfen (Art. 3):** Niederlassungsprinzip oder Marktortprinzip.
2. **Verarbeitungsarten inventarisieren:** Welche Daten werden vom Produkt verarbeitet?
3. **Rechtsgrundlage prüfen (Art. 6, 7, 9):** Für jede Verarbeitungsart.
4. **Drittlandübermittlung (Art. 44 ff.):** SCC vorhanden? Angemessenheitsbeschluss?
5. **Privatrechtliche Konsequenzen:** Nichtigkeit § 134 BGB? Sachmangel § 434 BGB? CISG Art. 35?
6. **Schadensersatz (Art. 82 DSGVO):** Materiell und immateriell — konkreten Schaden darlegen.

## Output-Template

**Adressat:** Entscheidungsgründe — Tonfall: sachlich-juristisch

```
## DSGVO-Prüfung

**Anwendbarkeit Art. 3 DSGVO:** Ja, weil [Niederlassungsprinzip / Marktortprinzip: Produkt
richtet sich an Personen in der EU].

**Verarbeitungsarten:** [Produkt X] verarbeitet [DATENART, z.B. biometrische Daten nach Art. 9 DSGVO].

**Rechtsgrundlage Art. 6 DSGVO:** Keine wirksame Rechtsgrundlage, weil [BEGRÜNDUNG].

**Folge:** [Sachmangel § 434 BGB / Nichtigkeit § 134 BGB / Schadensersatz Art. 82 DSGVO].
```

## Pruefstationen

### A - Anwendbarkeit der DSGVO

- Art. 3 Abs. 1 DSGVO: Niederlassungsprinzip
- Art. 3 Abs. 2 DSGVO: Marktortprinzip - Anbieten von Waren oder Dienstleistungen an Personen in der Union ODER Verhaltensbeobachtung in der Union
- DSGVO ist Eingriffsnorm im Sinne Art. 9 Rom-I (deutsche Gerichte wenden sie auch dann an, wenn das Vertragsstatut ausländisch ist)

### B - Verstöße prüfen

1. **Art. 5 Abs. 1 DSGVO** - Grundsätze (Rechtmäßigkeit, Treu und Glauben, Transparenz, Zweckbindung, Datenminimierung, Richtigkeit, Speicherbegrenzung, Integritaet, Rechenschaftspflicht)
2. **Art. 6 DSGVO** - Rechtsgrundlage
3. **Art. 7 DSGVO** - Einwilligung (informiert, freiwillig, widerrufbar)
4. **Art. 9 DSGVO** - besondere Kategorien (Gesundheits-, biometrische Daten)
5. **Art. 13 und 14 DSGVO** - Informationspflichten
6. **Art. 22 DSGVO** - automatisierte Entscheidung im Einzelfall
7. **Art. 25 DSGVO** - privacy by design und by default
8. **Art. 32 DSGVO** - Sicherheit der Verarbeitung
9. **Art. 44 ff DSGVO** - Datenübermittlung in Drittlaender

### C - Folgen für den Privatrechtsstreit

- Verstoß gegen ein Verbotsgesetz (Art. 6 DSGVO i. V. m. nationaler Norm)? -> Nichtigkeit nach Paragraf 134 BGB?
- Sachmangel im Sinne Paragraf 434 BGB i. V. m. Art. 6 ProduktsicherheitsVO 2023?
- Mangel im Sinne Art. 35 CISG (Vertragsmaessigkeit)?

## Smartglasses und Wearables - typische Verstöße

- heimliche Aufzeichnung Dritter ohne deren Wissen (Verletzung Persönlichkeitsrecht aller in der Umgebung)
- Live-Streaming der Kameraperspektive ohne Hinweis-LED
- Gesichtserkennung in Echtzeit
- Datenübertragung in Drittlaender ohne SCC oder anderen Mechanismus

## Im Urteil

Im Tatbestand auf das Gutachten verweisen. In den Entscheidungsgründen konkret die verletzten DSGVO-Artikel benennen und subsumieren.

<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 39/20 (claimed: DSGVO-Versto\u00dfe Schadensersatz Art. 82, NJW 2021, 3041): NOT_FOUND auf dejure.org. NJW 2021, 3041 gehoert zu BGH VI ZR 40/20 (VW-Abgasskandal §826 BGB) – thematisch unverwandt. Eintrag geloescht. DSGVO-Schadensersatz wird durch bereits vorhandene EuGH-Zitate C-300/21 und C-340/21 abgedeckt. -->
