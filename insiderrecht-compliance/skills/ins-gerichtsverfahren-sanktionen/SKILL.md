---
name: ins-gerichtsverfahren-sanktionen
description: "Ins 027 Gerichtsverfahren, Ins 015 Sanktionen Wphg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 027 Gerichtsverfahren, Ins 015 Sanktionen Wphg

## Arbeitsbereich

Dieser Skill bündelt **Ins 027 Gerichtsverfahren, Ins 015 Sanktionen Wphg** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-027-gerichtsverfahren` | Prueft Insiderinformations-Qualitaet laufender Gerichtsverfahren und Schiedsverfahren: Kursrelevanz, Ad-hoc-Pflicht und Verteidigungsinteressen. |
| `ins-015-sanktionen-wphg` | Analysiert zivilrechtliche (§§ 97–98 WpHG), bussgeldbewehrte (§ 120 WpHG) und strafrechtliche (§ 119 WpHG) Sanktionen fuer MAR-Verstaesse. |

## Arbeitsweg

Für **Ins 027 Gerichtsverfahren, Ins 015 Sanktionen Wphg** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-027-gerichtsverfahren`

**Fokus:** Prueft Insiderinformations-Qualitaet laufender Gerichtsverfahren und Schiedsverfahren: Kursrelevanz, Ad-hoc-Pflicht und Verteidigungsinteressen.

# Gerichtsverfahren und Schiedsverfahren – Insiderrecht

## Rechtlicher Rahmen

Laufende oder drohende Gerichtsverfahren können Insiderinformationen darstellen, wenn ihr
Ausgang den Kurs wesentlich beeinflussen würde (z. B. milliardenschwere Schadensersatzklagen,
patentrechtliche Kernstreitigkeiten, Kartellbußgeldverfahren). Aufschub nach Art. 17 Abs. 4 MAR
kann greifen, wenn Veröffentlichung das Verfahren gefährdet.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- ESMA-Leitlinien Aufschub: https://www.bafin.de/dok/8252648
- § 97 WpHG: https://www.gesetze-im-internet.de/wphg/__97.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob laufende Gerichts- oder Schiedsverfahren eine Insiderinformation
darstellen, wann die Ad-hoc-Pflicht entsteht, und ob ein Aufschub zulässig ist.

## Arbeitsprogramm

### Schritt 1 – Wesentlichkeit des Verfahrens

- Was ist Gegenstand des Verfahrens?
- Wie hoch ist das mögliche Schadensersatzvolumen oder der Wert der strittigen Rechte?
- Wie wahrscheinlich ist ein nachteiliges Urteil?
- Verhältnis zum Unternehmenswert (Marktkapitalisierung)

### Schritt 2 – Insiderinformations-Prüfung (Art. 7 MAR)

- Präzision: Ist das Verfahren und sein potenzieller Ausgang präzise genug?
 (Laufendes Verfahren mit konkreten Klageanträgen ist präzise)
- Kursrelevanz: Würde ein verständiger Anleger das Verfahren bei der
 Investitionsentscheidung berücksichtigen?
- Nichtöffentlichkeit: Ist das Verfahren noch nicht öffentlich bekannt?
 (Viele Gerichtsverfahren werden öffentlich durch Pressemitteilungen oder Registereintragungen)

### Schritt 3 – Aufschub wegen Verteidigungsinteressen

- Legitimes Interesse: Beeinträchtigung der Verfahrensstrategie durch frühzeitige
 Offenlegung der Streitwerte, Beweislage oder Vergleichsbereitschaft
- Praxis: BaFin-Emittentenleitfaden erkennt dieses Interesse an, aber nur für die
 Information über die Verfahrensstrategie, nicht für das Verfahren selbst, wenn bereits bekannt
- Grenzen: Wenn Verfahren durch Kläger oder Gericht öffentlich gemacht wird → kein Aufschub

### Schritt 4 – Eskalationspunkte: Neue kursrelevante Entwicklungen

Neue Insiderinformationen entstehen ggf. bei:
- Erstinstanzlichem Urteil (besonders bei hohem Streitwert)
- Vergleichsverhandlungen (konkretes Angebot beider Seiten)
- Behördlicher Entscheidung (Kartellamt, BaFin, EuGH-Schlussanträge)
- Möglichem Aktenzeichen nach EuGH-Vorlage

### Schritt 5 – Koordination mit Rechtsabteilung

- Rechtsabteilung / externe Prozessanwälte: in Insiderliste aufnehmen
- Regelmäßiger Update-Mechanismus: Quartalsbericht der Rechtsabteilung an Compliance
 über wesentliche neue Entwicklungen in Verfahren mit Ad-hoc-Relevanz

## Red-Team-Fragen

- Sind alle wesentlichen Verfahren in der Compliance-Übersicht erfasst?
- Wird die Wesentlichkeitsschwelle regelmäßig neu beurteilt (z. B. nach Klagebegründung)?
- Werden Vergleichsverhandlungen als eigenständige Insiderinformation behandelt?
- Ist der Aufschub-Tatbestand mit der konkreten Verfahrenssituation begründet?

## Ausgabeformat

Erzeuge:
1. Verfahrensregister mit Insiderinformations-Prüfstatus
2. Wesentlichkeitsanalyse (Streitwert × Wahrscheinlichkeit × Kursrelevanz)
3. Aufschub-Begründungsmatrix je Verfahren
4. Eskalationsprotokoll für neue Entwicklungen

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## 2. `ins-015-sanktionen-wphg`

**Fokus:** Analysiert zivilrechtliche (§§ 97–98 WpHG), bussgeldbewehrte (§ 120 WpHG) und strafrechtliche (§ 119 WpHG) Sanktionen fuer MAR-Verstaesse.

# Sanktionen nach WpHG und MAR

## Rechtlicher Rahmen

Das WpHG setzt MAR-Sanktionsanforderungen in deutsches Recht um. Es unterscheidet drei Ebenen:
(1) Zivilrechtliche Haftung (§§ 97–98 WpHG), (2) Bußgeldtatbestände (§ 120 WpHG), (3) Straf-
tatbestände (§ 119 WpHG). Daneben sieht MAR Art. 30 Mindest-Höchststrafen für die Mitgliedstaaten
vor. BaFin kann zusätzlich aufsichtsrechtliche Maßnahmen (Berufsverbote, öffentliche Bekanntmachung)
verhängen.

Rechtsgrundlagen:
- §§ 97–98 WpHG: https://www.gesetze-im-internet.de/wphg/__97.html
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- § 120 WpHG: https://www.gesetze-im-internet.de/wphg/__120.html
- Art. 30 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden Sanktionen: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill analysiert das vollständige Sanktionsspektrum bei MAR-Verstößen und erstellt
für jede Sanktionsebene eine Risikomatrix mit Tatbestand, Rechtsfolge und Verteidigungsstrategie.

## Arbeitsprogramm

### Schritt 1 – Zivilrechtliche Haftung (§§ 97–98 WpHG)

§ 97 WpHG (unterlassene oder verspätete Ad-hoc-Mitteilung):
- Tatbestand: Emittent hat Insiderinformation nicht oder nicht rechtzeitig veröffentlicht
- Anspruchsberechtigte: Anleger, die Finanzinstrumente nach Entstehung der Pflicht erworben
 und nach Veröffentlichung mit Verlust veräußert haben (oder nach der Pflicht veräußert haben)
- Verschulden: Vorsatz oder grobe Fahrlässigkeit des Emittenten
- Schaden: Kursdifferenz zwischen fairem Wert (ohne Pflichtverletzung) und Kaufpreis

§ 98 WpHG (falsche Ad-hoc-Mitteilung):
- Tatbestand: Emittent hat unwahre Insiderinformation veröffentlicht
- Anspruchsberechtigte: Anleger, die aufgrund der unwahren Mitteilung gekauft oder verkauft haben

### Schritt 2 – Bußgeldtatbestände (§ 120 WpHG)

Ordnungswidrigkeiten nach § 120 WpHG:
- Verstöße gegen Art. 14 MAR (Insiderhandel, leichtfertig): bis zu 5 Mio. EUR
- Verstöße gegen Art. 17 MAR (Ad-hoc-Pflicht): bis zu 2,5 Mio. EUR (natürliche Person)
 oder 2 % des Jahresumsatzes (juristische Person), max. 5 Mio. EUR oder 15 Mio. EUR
- Verstöße gegen Art. 18 MAR (Insiderliste): bis zu 1 Mio. EUR
- Verstöße gegen Art. 19 MAR (Directors' Dealings): bis zu 1 Mio. EUR

### Schritt 3 – Straftatbestände (§ 119 WpHG)

§ 119 Abs. 1 WpHG (Insiderhandel, vorsätzlich):
- Tatbestand: Erwerb, Veräußerung, Empfehlung, Weitergabe von Insiderinformationen
- Strafe: bis zu 5 Jahre Freiheitsstrafe oder Geldstrafe
- Besonders schwerer Fall: bis zu 10 Jahre (§ 119 Abs. 2 WpHG bei gewerbsmäßigem Handeln)
§ 119 Abs. 3 WpHG (Leichtfertigkeit): Geldstrafe oder bis zu 1 Jahr Freiheitsstrafe

### Schritt 4 – Aufsichtsrechtliche Maßnahmen (Art. 30 MAR)

- BaFin kann Berufsverbot für Führungspersonen verhängen
- Öffentliche Bekanntmachung (Naming and Shaming) auf BaFin-Website
- Entzug von Lizenzen für Finanzdienstleister
- Gewinnabschöpfung

### Schritt 5 – Verteidigungsstrategie

Für zivilrechtliche Haftung:
- Nachweis fehlenden Verschuldens oder fehlender Kausalität
- Nachweis, dass Aufschub rechtmäßig war

Für Bußgeldverfahren:
- Kooperation mit BaFin, vollständige Dokumentationsvorlage
- Einrede der Verjährung (§ 31 OWiG: 3 Jahre)

Für Strafverfahren:
- Nachweis fehlenden Vorsatzes (Beratungsirrtum, fehlende Kenntnis der Insiderinformation)
- Selbstanzeige prüfen (keine formale Selbstanzeige wie im Steuerrecht, aber Kooperation)

## Red-Team-Fragen

- Ist das vollständige Sanktionsspektrum für jeden Verstoßtatbestand bekannt?
- Wurden § 97/§ 98-Klagerisiken in der Rechtsrisikoanalyse berücksichtigt?
- Gibt es einen Krisen-Ansprechpartner bei der BaFin für den Ernstfall?
- Sind D&O- und Kapitalmarkt-Haftpflichtversicherungen auf MAR-Deckung geprüft?
- Sind die Bußgeld-Obergrenzen nach aktueller WpHG-Fassung (letzte Änderung prüfen) korrekt?

## Ausgabeformat

Erzeuge:
1. Sanktionsrisiko-Matrix: Verstoß × Sanktionsebene × Strafrahmen × Verantwortlicher
2. Verteidigungsmemo-Vorlage (für BaFin-Bußgeldverfahren)
3. Versicherungscheck-Liste (D&O, Kapitalmarkthaftpflicht)
4. Krisenmanagement-Kontaktliste (BaFin, Staatsanwaltschaft, externe Kanzlei)

Belege ausschließlich mit: gesetze-im-internet.de, eur-lex.europa.eu, bafin.de, bgh.de,
dejure.org, openjur.de.
