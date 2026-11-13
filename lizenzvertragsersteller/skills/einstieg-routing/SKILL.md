---
name: einstieg-routing
description: "Für Anwalts-Dashboard Lizenzvertragsersteller: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anwalts-Dashboard Lizenzvertragsersteller

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

> Sie sehen die Sofort-Triage. Keine Rueckfragen, bis die Tabelle steht. Bei klarer Faktenlage gehen wir sofort zum Baukasten — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellpruefung | Standardquelle |
| --- | --- | --- |
| IP-Typ | Urheberrecht/Software · Patent · Marke · Design (GeschmacksmusterG) · Gebrauchsmuster · Geschäftsgeheimnis/Know-how | Schutzrechtsregister (DPMA, EUIPO, EPA), Vertragsunterlagen |
| Rolle Mandant | Lizenzgeber · Lizenznehmer · Sicherheitengeber · Sicherheitennehmer · Verwahrer (Escrow) · Beide (cross-license) | Mandatsmail, Vollmacht |
| Lizenzumfang | Territorium · Zeit · Anwendungsfeld · exklusiv/non-exklusiv/sole | Geschäftsmodell, Roadmap |
| Vertragssprache | DE · EN · Bilingual mit Massgebbung | Mandantenwunsch, Gegenseite |
| Rechtswahl | Deutsches Recht · Schweiz · EN&W · NY · Rom-I-VO bei Mehrlaender | Standortverteilung, Vollstreckungsstrategie |
| Vorbefassung | NDA, LOI, MOU schon unterschrieben? | Aktenlage |

## Risiko-Ampel

- **Insolvenz-Risiko Lizenzgeber:** 🔴 bei Software-Abhaengigkeit ohne Escrow · 🟠 bei mittelgrosser Lizenzgeberin · 🟢 etablierter Konzern.
- Kartellrecht TTBER: Kritisch bei einem gemeinsamen Marktanteil der Wettbewerber über 20 Prozent oder einem Anteil einer Partei unter Nichtwettbewerbern über 30 Prozent sowie bei Kernbeschränkungen oder ausgeschlossenen Klauseln. Auch unterhalb der Schwelle ist der konkrete Klauselinhalt zu prüfen.
- **Steuern/Quellensteuer:** 🔴 bei Cross-Border ohne DBA-Prüfung · 🟠 bei DBA mit Quellensteuer-Reduktion · 🟢 bei rein nationaler Lizenz.

## Anschluss-Skills (Router)

| Wenn der Fall traegt … | dann Skill | Erwartung |
| --- | --- | --- |
| IP-Identifikation noch offen | `ip-identifikation-und-bestandsaufnahme` | IP-Inventarliste, Schutzstatus, Belastungen |
| Parteienrollen noch nicht klar | `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer` | Rollenmatrix |
| Software-Lizenz | `lizenz-urheberrecht-und-software-urhg` | UrhG-Bausteine, Source-Code-Escrow Hinweis |
| Patent-Lizenz | `lizenz-patent-patg` | PatG-Bausteine, Marktanteils-Check TT-GVO |
| Marke-Lizenz | `lizenz-marke-markeng` | MarkenG, Qualitaetskontrolle, Eintrag DPMA |
| Insolvenzfeste Gestaltung | `insolvenz-fortbestand-paragraf-103-inso-lizenz` + `escrow-quellcode-verwahrer-vereinbarung` | Klausel + Escrow-Mustertext |

**Vorrang:** Wenn IP nicht identifiziert ist, zuerst Skill 2 (Identifikation). Erst danach Klausel-Baukasten.

## Norm-Radar

- **UrhG** §§ 31, 32, 32a (Urheberrechtslizenzen, angemessene Vergütung); § 69a ff. (Software); § 137l UrhG (unbekannte Nutzungsarten)
- **PatG** §§ 9, 15 (Lizenz); § 24 (Zwangslizenz)
- **MarkenG** §§ 30 (Lizenz), 27 (Uebertragung)
- **DesignG** §§ 31 ff.; **GebrMG** §§ 22 ff.
- **GeschGehG** §§ 1-12 (Schutz von Geschäftsgeheimnissen; Lizenz nach § 3)
- **InsO** § 103 (Wahlrecht des Verwalters bei gegenseitigen Vertraegen)
- Verordnung (EU) 2026/877 und Leitlinien C/2026/2323 - seit 1. Mai 2026 geltender Rahmen für Technologietransfervereinbarungen
- **Rom-I-VO** Art. 4 (Lizenzvertraege Statut)

## Genau eine Rueckfrage (nur wenn noetig)

> Welcher IP-Typ steht im Vordergrund — und ist der Mandant Lizenzgeber, Lizenznehmer oder beide (Cross-License)?

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie fuehren das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`. Konvention dieses Dashboards: `references/anwalts-dashboard-konvention.md`.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für IP-Lizenzverträge und Technologieverwertung:** Welche Formulierung erfüllt das Geschäftsziel und was ändert die Alternative?

**Erste Ansicht:** Stelle betroffene Klauseln nebeneinander: vorhandene Fassung, vorgeschlagener Text, konkrete Rechts- oder Kostenfolge und offener Verhandlungspunkt.

**Sinnvolle Interaktion:** Lasse eine tatsächlich angebotene Klauselvariante auswählen; übernimm die Wahl in den fortgeführten Entwurf und prüfe Verweisungen, Definitionen und Folgeklauseln. Eine Risikofarbe ersetzt keine Erläuterung.

**Datengrundlage:** Dokumentversion, Klauselnummer, Wortlaut, Geschäftsziel, Beleg für die Sachannahme und Rechtsquelle. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** vollständig ausformulierte Vertragsfassung oder Verhandlungsantwort mit gesonderter Änderungsübersicht. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
