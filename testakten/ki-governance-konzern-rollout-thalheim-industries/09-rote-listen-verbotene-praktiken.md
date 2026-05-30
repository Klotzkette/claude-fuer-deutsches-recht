# Rote Liste — Verbotene KI-Praktiken nach Art. 5 KI-VO

**Aktenzeichen:** TI-KI-2026-013
**Dokumentversion:** 1.1
**Erstellungsdatum:** 20. Dezember 2025
**Verfasser:** Annegret Kühnhausen (CCO); Kanzlei Borchmann Compliance (Frankfurt)
**Geltungsbereich:** Alle Mitarbeiterinnen und Mitarbeiter, Führungskräfte, Auftragnehmer

---

## 1. Zweck und Verpflichtung

Art. 5 der Verordnung (EU) 2024/1689 (KI-VO) (https://dejure.org/gesetze/KIVO/5.html) enthält eine abschließende Liste von KI-Praktiken, die in der Europäischen Union verboten sind. Diese Verbote gelten seit dem 02. Februar 2025 (Art. 113 Abs. 1 KI-VO).

Thalheim Industries SE hat als Betreiber (Deployer) und in Teilen als Anbieter (Provider — insbesondere für intern entwickelte Systeme wie PredictMaint und ServiceBot) sicherzustellen, dass keine der nachfolgend aufgeführten verbotenen Praktiken eingesetzt oder gefördert wird. Verstöße können mit Bußgeldern von bis zu 35 Mio. EUR oder 7 % des globalen Jahresumsatzes belegt werden (Art. 99 Abs. 3 KI-VO).

Diese Rote Liste ist für alle Beschäftigten und Führungskräfte verbindlich. Sie ergänzt die KI-Governance-Leitlinie (Aktenstück 01) und ist in das AI-Literacy-Curriculum (Aktenstück 05, Modul A) integriert.

---

## 2. Verbotene Praktiken (Art. 5 KI-VO) — Vollständige Übersicht

### 2.1 Unterschwellige Beeinflussung (Art. 5 Abs. 1 lit. a KI-VO)

**Verboten:** Das Inverkehrbringen, die Inbetriebnahme oder Verwendung von KI-Systemen, die durch Techniken der unterschwelligen Beeinflussung, die von einer Person nicht wahrgenommen werden können, das Verhalten dieser Person in einer Weise beeinflussen, die dazu bestimmt ist oder die Wirkung hat, ihr oder einer anderen Person erheblichen Schaden zuzufügen.

**Praxisrelevanz Thalheim:** KEIN Thalheim-System fällt aktuell unter diesen Tatbestand. Mögliches Risiko: Marketing-Tools, die Nudging-Techniken einsetzen. Prüfpflicht bei Einführung neuer Marketing-KI.

**Merke:** Auch klassische Nudge-Algorithmen (E-Commerce-Empfehlungen) sind nur dann verboten, wenn sie unterschwellig und schädigend wirken.

---

### 2.2 Ausnutzung von Vulnerabilitäten (Art. 5 Abs. 1 lit. b KI-VO)

**Verboten:** KI-Systeme, die Vulnerabilitäten einer Person oder Gruppe ausnutzen, die auf Alter, Behinderung oder sozialer oder wirtschaftlicher Situation basieren.

**Praxisrelevanz Thalheim:** KEIN direktes Risiko bei aktuellen Systemen. Potenziales Risiko: ServiceBot — wenn er vulnerable Kundengruppen (z. B. ältere Personen, wirtschaftlich benachteiligte Kunden) gezielt ausnutzt, um Vertragsabschlüsse zu erzielen.

**Maßnahme:** ServiceBot ist auf sachliche Kundeninformation beschränkt; keine Verkaufsstrategie auf Basis Kundenvulnerabilitäten.

---

### 2.3 Social Scoring (Art. 5 Abs. 1 lit. c KI-VO)

**Verboten:** KI-Systeme, die von öffentlichen Behörden (oder in deren Auftrag) zur Bewertung natürlicher Personen auf der Grundlage des Sozialverhaltens oder persönlicher Merkmale eingesetzt werden, mit nachteiligen Folgen.

**Praxisrelevanz Thalheim:** Nicht anwendbar (Thalheim ist keine Behörde). Jedoch: interne Mitarbeiterbewertungs-KI, die systematisch Verhaltensprofile erstellt und für Personalentscheidungen nutzt, könnte dem Geist dieser Vorschrift widersprechen und nach § 87 BetrVG mitbestimmungspflichtig sein.

---

### 2.4 Vorhersagebasierte Polizeiarbeit (Art. 5 Abs. 1 lit. d KI-VO)

**Verboten:** KI-Systeme für Risikoabschätzungen natürlicher Personen hinsichtlich der Begehung einer Straftat, ausschließlich auf der Grundlage von Profiling oder Persönlichkeitsmerkmalen.

**Praxisrelevanz Thalheim:** Nicht anwendbar.

---

### 2.5 Anlasslose biometrische Massenüberwachung (Art. 5 Abs. 1 lit. e KI-VO)

**Verboten:** Echtzeit-Fernerkennung biometrischer Merkmale in öffentlich zugänglichen Räumen durch Strafverfolgungsbehörden.

**Praxisrelevanz Thalheim:** Nicht anwendbar (Thalheim ist keine Strafverfolgungsbehörde). Jedoch: Kamerasysteme im Werksgelände, die Personen erkennen, sind sorgfältig zu prüfen.

---

### 2.6 Emotionserkennung (Art. 5 Abs. 1 lit. f KI-VO)

**Verboten:** KI-Systeme zur Erkennung von Emotionen am Arbeitsplatz und in Bildungseinrichtungen, außer aus medizinischen oder Sicherheitsgründen.

**Praxisrelevanz Thalheim: HOCH.** Jedes System, das Stimmungen, Emotionen oder den emotionalen Zustand von Mitarbeitern am Arbeitsplatz analysiert (z. B. Analyse von Videomeetings, Sprachanalyse in Call-Centern), ist in Deutschland nach Art. 5 Abs. 1 lit. f KI-VO VERBOTEN. Prüfung aller Call-Center-Systeme und Meeting-Analyse-Tools erforderlich.

**Maßnahme:** CCO hat Bestandsaufnahme laufender und geplanter HR-Analytics-Systeme angeordnet (Frist: 30.04.2026).

---

### 2.7 Biometrische Kategorisierung (Art. 5 Abs. 1 lit. g KI-VO)

**Verboten:** KI-Systeme, die biometrische Daten verwenden, um natürliche Personen nach politischen Ansichten, Gewerkschaftszugehörigkeit, Religion, Weltanschauung, Rasse, Sexualleben oder sexueller Ausrichtung zu kategorisieren.

**Praxisrelevanz Thalheim: HOCH für Recruiting.** RecruitAI darf nicht direkt oder indirekt Bewerber nach solchen Merkmalen kategorisieren. Die fehlenden Bias-Tests (Strang 1) erhöhen das Risiko, dass solche Kategorisierungen unbeabsichtigt im Modell abgebildet sind.

---

### 2.8 Biometrische Fernidentifikation in Echtzeit (Art. 5 Abs. 1 lit. h KI-VO)

**Verboten:** Echtzeit-Fernidentifikation biometrischer Merkmale in öffentlich zugänglichen Räumen durch Strafverfolgungsbehörden (mit engen Ausnahmen).

**Praxisrelevanz Thalheim:** Nicht anwendbar.

---

## 3. Prüfschema für neue KI-Systeme

Für jedes neue KI-System ist vor Einführung folgendes Prüfschema zu durchlaufen:

```
Schritt 1: Fällt das System unter Art. 5 Abs. 1 KI-VO (Verbote)?
  └─ JA → Sofortiger Stopp. Keine Einführung. Meldung an CCO.
  └─ NEIN → weiter mit Schritt 2.

Schritt 2: Fällt das System unter Art. 6 / Anh. III KI-VO (Hochrisiko)?
  └─ JA → Vollständige Konformitätsprüfung vor Einsatz. KI-Clearance erforderlich.
  └─ NEIN → weiter mit Schritt 3.

Schritt 3: Fallen Transparenzpflichten nach Art. 50 KI-VO an?
  └─ JA → Hinweispflichten umsetzen. Freigabe durch CCO.
  └─ NEIN → Eintrag KI-Inventar, jährliche Überprüfung.
```

---

## 4. Meldeverpflichtung

Jede Mitarbeiterin und jeder Mitarbeiter, die/der bemerkt oder vermutet, dass ein KI-System bei Thalheim eine verbotene Praktik umsetzt oder umsetzt werden soll, ist verpflichtet, dies unverzüglich zu melden:
- Intern: ki-incident@thalheim.de oder CCO Kühnhausen direkt
- Extern: Hinweisgeberschutzgesetz (HinSchG) — externe Meldestelle (Bundesamt für Justiz)

Meldungen sind vertraulich und werden durch das Hinweisgeberschutzsystem des Unternehmens geschützt.

---

*Aktenzeichen: TI-KI-2026-013. Verfasser: A. Kühnhausen, Kanzlei Borchmann. Stand: Dezember 2025.*
