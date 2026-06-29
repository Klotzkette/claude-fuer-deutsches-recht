---
name: einstieg-routing
description: "Anwalts-Dashboard fuer den Lizenzvertragsersteller: Sofort-Triage (IP-Typ, Parteien, Sprache, Rechtswahl), Risiko-Ampel, Anschluss-Skill-Router, Norm-Radar, Leitentscheidungs-Anker; maximal eine Rueckfrage."
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

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

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
- **Kartellrecht TT-GVO:** 🔴 bei Marktanteil > 30 % (Wettbewerber) bzw. > 20 % (vertikal) · 🟠 bei Schranken-Klauseln (Kernbeschraenkungen) · 🟢 bei reinem KMU.
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
- **VO (EU) Nr. 316/2014 (TT-GVO)** — Technologietransfer-Gruppenfreistellung
- **Rom-I-VO** Art. 4 (Lizenzvertraege Statut)

## Genau eine Rueckfrage (nur wenn noetig)

> Welcher IP-Typ steht im Vordergrund — und ist der Mandant Lizenzgeber, Lizenznehmer oder beide (Cross-License)?

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie fuehren das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`. Konvention dieses Dashboards: `references/anwalts-dashboard-konvention.md`.
