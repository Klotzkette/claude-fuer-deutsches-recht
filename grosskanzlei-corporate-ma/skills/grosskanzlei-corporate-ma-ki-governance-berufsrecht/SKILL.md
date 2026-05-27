---
name: grosskanzlei-corporate-ma-ki-governance-berufsrecht
description: "KI-Einsatz im Transaktionsmandat berufsrechtlich absichern: Anwendungsfall Anwalt moechte KI-Tools fuer Datenraumanalyse oder Vertragsentwurf nutzen und muss Mandatsgeheimnis, Datenschutz und KI-VO-Betreiberpflichten einhalten. § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz. Pruefraster Datenklassen-Kategorisierung, Need-to-know, Pseudonymisierung, AVV-Pruefung, Mandantenfreigabe, Halluzinations-Kontrolle. Output Berufsrechts-Compliance-Protokoll fuer KI-Nutzung im Mandat. Abgrenzung zu Datenqualitaet-XAI-Qualitaetskontrolle und zu Konflikt-GwG-Check."
---

# KI-Governance und Berufsrecht

## Zweck

Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe.

## Arbeitsmodus


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

- Datenklassen und erlaubte Tools erfassen.
- Need-to-know, Pseudonymisierung, AVV/TOMs und Verschwiegenheit dokumentieren.
- Ungeprüfte KI-Outputs und menschliche Validierung trennen.
- Mandantenhinweise und interne Freigaben vorbereiten.

## Rote Schwellen

- Mandatsgeheimnis im offenen Tool.
- Kein Dienstleister-/AVV-Status.
- KI-Output wird ohne Review nach außen gegeben.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — KI-Governance-Baustein fuer Kanzlei-Berufsrecht erstellen | Governance-Vorlage nach Schema; Template unten |
| Variante A — Kleinere Kanzlei keine eigene IT-Abteilung | Vereinfachte Governance ohne technische Detail-Spezifikationen |
| Variante B — Internationales Buero auslaendisches Recht relevant | Jurisdiktion-spezifische Anpassungen erfordern separate Pruefung |
| Variante C — Bestehende Richtlinie aktualisieren nicht neu erstellen | Delta-Update statt Neuerstellung; nur geaenderte Stellen anpassen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagen

- assets/templates/ai-use-disclosure-log.md
- assets/templates/confidentiality-need-to-know-log.md

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- § 43a BRAO — anwaltliche Pflichten: Sorgfalt, Vollstaendigkeit, Unabhaengigkeit
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung
- § 17 GeschGehG — Schutz von Geschaeftsgeheimnissen; gilt fuer alle Mandatsinhalte
- Art. 17 MAR — bei boersennotierten Zielobjekten: Ad-hoc-Pflicht und Vertraulichkeit

### Leitsaetze aus der Rechtsprechung
- BGH, Urt. v. 15.03.2012 - IX ZR 35/11, NJW 2012, 1800 — anwaltliche Sorgfaltspflicht: vollstaendige Information des Mandanten auch bei Zeitdruck
- BGH, Urt. v. 14.03.2003 - V ZR 64/02, NJW 2003, 1811 — Offenbarungspflicht: wesentliche Risiken sind ungefragt zu benennen
- OLG Frankfurt, Urt. v. 22.02.2021 - 23 U 70/19, NZG 2021, 680 — Beraterhaftung bei M&A: auch bei eingeschraenktem Zeitrahmen muessen wesentliche Risiken erkannt und kommuniziert werden

### Kommentarliteratur
- Picot, Unternehmenskauf, Kapitel 1 (M&A-Prozess, Transaktionsmanagement), 5. Auflage
- Schramm/Alexander, BRAO, § 43a Rn. 1-50

### Qualitaetssicherung
- Human-in-the-loop bei allen hochrisikorelevanten Ausgaben
- Dokumentation: Datum, Bearbeiter, Freigabe durch Senior
