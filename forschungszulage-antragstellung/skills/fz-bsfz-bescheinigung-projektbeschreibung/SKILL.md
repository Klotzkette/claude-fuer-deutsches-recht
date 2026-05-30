---
name: fz-bsfz-bescheinigung-projektbeschreibung
description: "BSFZ-Antrag und FuE-Projektbeschreibung praxistauglich erstellen: Ausgangsproblem, Stand der Technik, Neuheit, technisches Risiko, systematisches Vorgehen, Arbeitspakete und verständliche Prüferlogik. Mit Mustertexten, Anti-Floskel-Regeln und Strategie Einzelantrag vs. Projektbündel."
---

# BSFZ-Bescheinigung und Projektbeschreibung

## Worum geht es

Die Bescheinigungsstelle Forschungszulage (BSFZ) prüft im ersten Verfahrensschritt, ob ein Vorhaben FuE im Sinne des FZulG ist. Sie sagt nichts zur Höhe der Förderung, nichts zur Bemessungsgrundlage, nichts zur Personalkostenberechnung. Sie sagt nur: ja, das ist Forschung — oder nein. Ohne diese Bescheinigung gibt es keine Festsetzung beim Finanzamt.

Eingang ist das Portal https://www.bescheinigung-forschungszulage.de/. Der Antrag wird elektronisch eingereicht.

## Wann brauchen Sie diesen Skill

- Sobald die FuE-Eigenschaft durch `fz-fue-definition-frascati-abgrenzung` plausibilisiert ist.
- Bei BSFZ-Rückfragen zu Inhalt oder Tiefe der Projektbeschreibung.
- Wenn mehrere verwandte Vorhaben gebündelt eingereicht werden sollen.
- Vor jedem Folgeantrag im Mehrjahresprojekt.

## Sachrahmen — was die BSFZ tatsächlich macht

- Eingangsprüfung (formal: Antragsteller, Vorhaben, Zeitraum, Zuordnung).
- Fachprüfung durch eine fachnahe Gutachterin oder einen Gutachter (Domäne, oft promoviert/habilitiert).
- Eventuell Rückfragen (Nachforderung).
- Bescheinigungsentscheid (positiv, eingeschränkt, ablehnend).

Bearbeitungszeit erfahrungsgemäß einige Monate; Q1-Einreichung beschleunigt erfahrungsgemäß den Durchlauf.

## Gliederung der Projektbeschreibung

Erfahrungsgemäß bewährte Struktur, jede Seitenangabe als Richtwert:

1. **Ausgangsproblem (ca. 1 Seite).** Konkretes technisches Problem. Keine Marketing-Sprache. Welcher Zielwert wird nicht erreicht?
2. **Stand der Technik (1 bis 2 Seiten).** Mindestens 2 bis 3 konkrete Quellen: Norm, Patent, Publikation, Wettbewerbsprodukt. Messgrößen und Werte nennen.
3. **Entwicklungsziel und Neuheit (ca. 1 Seite).** Welche Funktion, Eigenschaft, Messgröße ist neu? Worin liegt die schöpferische Eigenleistung?
4. **Technische/wissenschaftliche Unsicherheit (ca. 0.5 Seite).** Was kann scheitern? Welcher Lösungsansatz ist offen?
5. **Systematischer Lösungsweg (1 bis 2 Seiten).** Iterationen, Hypothesen, Versuchsdesign, Decision-Gates.
6. **Arbeitspakete (1 bis 2 Seiten).** Tabelle mit AP-Nummer, Inhalt, Erfolgskriterium, Personenaufwand, Meilenstein.
7. **Abgrenzung Routine (ca. 0.5 Seite).** Welche Arbeiten gehören nicht zum FuE-Vorhaben?

## Praxisleitfaden — was die Prüferin sehen will

- **Konkretes technisches Problem.** Nicht "Effizienz verbessern", sondern "Energieverbrauch von 320 Wh/Stunde auf unter 180 Wh/Stunde".
- **Konkretes Risiko.** "Versuche an Vormaterial X können wegen unbekannter Sintertemperatur scheitern" ist gut. "Risiken bestehen" reicht nicht.
- **Dokumentierter Lösungsweg.** Welche Hypothesen testen Sie? Welche Iterationen sind eingeplant?
- **Arbeitspakete in Tabellenform.** AP-1 Konzept, AP-2 Versuchsreihe, AP-3 Prototyp, AP-4 Charakterisierung. Mit Meilensteinen und Personenstunden.
- **Stand der Technik mit Quellen.** Die Prüferin ist Fachexpertin. Wer den Stand der Technik nicht zitiert, signalisiert, dass die Hausaufgaben fehlen.

### Anti-Floskel-Regeln (was bei der BSFZ sofort fliegt)

- "Innovative Plattform" — streichen.
- "KI-basiert" ohne ML-Konzept — präzisieren oder weglassen.
- "Digitalisierung", "Industrie 4.0", "Smart Factory" als Selbstzweck — streichen.
- Produktbeschreibung statt Forschungsfrage — komplett umschreiben.
- Roadmap-Stil ("Q3 wir launchen ...") — streichen, Meilensteinkriterien statt Marketingzeitlinie.
- Adjektive ohne Operationalisierung ("modern", "smart", "next-gen") — streichen.

### Anti-Pattern, die zur Ablehnung führen

- Beschreibung des Produkts statt des FuE-Vorgehens.
- Anforderungsliste statt Forschungsproblem.
- Keine Abgrenzung zu Serienpflege.
- Keine Quellen für den Stand der Technik.
- Risiken nur erwähnt, nicht spezifiziert.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Ein großes Vorhaben vs. mehrere | hohe Aufmerksamkeit der Prüfer | weniger Risiko je Antrag | Bündel bei technischer Verwandtschaft |
| Detailtief vs. übersichtlich | maximale Tiefe | knapper Antrag | mittlere Tiefe; entscheidend Klarheit |
| Frühe Einreichung vs. Stabilität | Q1 minimal beschrieben | Q3 reif | Q1 reif, früh in der Bearbeitungsschlange |
| Eigene Schreibarbeit vs. Berater | inhouse, geringere Kosten | Beraterprofile mit Track Record | Berater bei Erstantrag, intern bei Folgeanträgen |

## Schritt für Schritt

1. Frascati-Memo aus `fz-fue-definition-frascati-abgrenzung` als Basis verwenden.
2. Vorhaben-Steckbrief vorbereiten: Titel, Vorhabenzeitraum, Hauptpersonen, FuE-Kategorie.
3. Ausgangsproblem in einem präzisen Absatz fassen.
4. Stand der Technik mit 2 bis 3 Quellen.
5. Neuheit klar herausarbeiten.
6. Technische Unsicherheit konkret nennen.
7. Arbeitspakete als Tabelle.
8. Abgrenzung zur Routine als eigener Abschnitt.
9. Antrag im BSFZ-Portal eingeben, PDF-Anhänge prüfen, Plausibilitäts-Check.

## Mustertexte

**Ausgangsproblem (Vorlage):**

"Im Bereich [Domäne, z. B. Wärmetauscher für Hochtemperaturanwendungen] erreicht der derzeitige Stand der Technik (siehe [Norm/Quelle 1]; [Quelle 2]) eine [Messgröße, z. B. Wirkungsgrad] von [Wert, z. B. 72 Prozent] bei [Randbedingung, z. B. 800 Grad Celsius]. Für [Zielanwendung] ist ein Wert von mindestens [Zielwert] erforderlich. Voruntersuchungen ([eigene Quelle / Vorprojekt]) zeigen, dass dieser Wert mit bestehenden Verfahren nicht erreichbar ist."

**Neuheit (Vorlage):**

"Wir untersuchen [konkretes Verfahren / konkrete Materialkombination / konkrete Architektur]. Die Neuheit liegt in [konkrete technische Kombination, z. B. Kombination eines neuartigen Substrats mit einem bislang nur für Niedrigtemperatur eingesetzten Beschichtungsverfahren]. Nach systematischer Recherche (siehe Anlage Quellenverzeichnis) ist diese Kombination im Stand der Technik nicht beschrieben."

**Technische Unsicherheit (Vorlage):**

"Es ist offen, ob [Bedingung, z. B. die geforderte Festigkeit] unter [Randbedingung, z. B. Dauerlast bei 750 Grad Celsius] erreicht werden kann. Insbesondere [Hürde, z. B. die Diffusion an der Grenzfläche] kann zum Scheitern führen. Vergleichbare Vorhaben (siehe [Quelle]) scheiterten an [Punkt]."

**Arbeitspakete-Tabelle (Vorlage):**

| AP | Inhalt | Meilenstein | Personenstunden | Erfolgskriterium |
| --- | --- | --- | --- | --- |
| AP-1 | Literaturrecherche, Konzept | M1 Konzeptpapier | 120 | konsistentes Konzept |
| AP-2 | Versuchsreihe Variante A | M2 Datenbasis A | 400 | mindestens 8 Messreihen |
| AP-3 | Versuchsreihe Variante B | M3 Datenbasis B | 400 | mindestens 8 Messreihen |
| AP-4 | Prototyp | M4 Prototyp lauffähig | 600 | Wirkungsgrad gemessen |
| AP-5 | Charakterisierung | M5 Abschlussbericht | 200 | Bewertung gegen Zielwert |

**Mehrere Projekte:** Wenn technisch verwandt, als Vorhabenbündel mit gemeinsamer Klammer einreichen. Wenn unverbunden, je eigener Antrag.

## Typische Fehler

- Produktbeschreibung statt FuE-Beschreibung.
- Stand der Technik nicht oder oberflächlich zitiert.
- Risiken nur abstrakt.
- Arbeitspakete ohne Erfolgskriterium.
- Routine-Anteile versteckt statt offen abgegrenzt.
- BSFZ-Antrag und Finanzamt-Antrag verwechselt (BSFZ macht nur die FuE-Eigenschaft).

## Output

- BSFZ-taugliche Projektbeschreibung (ca. 6 bis 10 Seiten je Vorhaben).
- Arbeitspaket-Matrix.
- Quellenverzeichnis Stand der Technik.
- Nachforderungsvorsorge: Liste der vorbereiteten Antworten auf typische Rückfragen.
- Liste der Anlagen (Skizzen, Vorprojekt-Berichte, Patente, Publikationen).

## Querverweise

- `fz-fue-definition-frascati-abgrenzung` für die FuE-Vorprüfung.
- `fz-bemessungsgrundlage-2026` für die parallele Vorbereitung der Personalkostenrechnung.
- `fz-dokumentationspaket-betriebspruefung` für die spätere Belegfähigkeit.
- `fz-ablehnung-nachbesserung-einspruch` bei BSFZ-Rückfragen.

## Quellen Stand 05/2026

- BSFZ-Portal: https://www.bescheinigung-forschungszulage.de/
- BSFZ-Antragsverfahren: https://www.bescheinigung-forschungszulage.de/antragsverfahren/ueber-das-antragsverfahren
- BSFZ-Hilfen: https://www.bescheinigung-forschungszulage.de/hilfen-zur-antragstellung
- FZulG: https://www.gesetze-im-internet.de/fzulg/
- AGVO Art. 2 Nr. 84 bis 86 (vom Antragsteller mit konsolidierter Fassung zu prüfen).
