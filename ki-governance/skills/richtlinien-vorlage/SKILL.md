---
name: richtlinien-vorlage
description: "Entwirft eine interne KI-Nutzungsrichtlinie auf Basis veröffentlichter Musterrichtlinien und des Praxisprofils — Recherche- und Synthese-Tool, dessen Ausgabe ein Entwurf für die anwaltliche Prüfung und Freigabe ist, keine fertige Richtlinie. Lädt, wenn der Nutzer KI-Richtlinie entwerfen, wir brauchen eine KI-Richtlinie, AI-Act-konforme Richtlinie oder Ähnliches sagt im Ki Governance: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# KI-Richtlinien-Starter

## Arbeitsbereich

Entwirft eine interne KI-Nutzungsrichtlinie auf Basis veröffentlichter Musterrichtlinien und des Praxisprofils — Recherche- und Synthese-Tool, dessen Ausgabe ein Entwurf für die anwaltliche Prüfung und Freigabe ist, keine fertige Richtlinie. Lädt, wenn der Nutzer "KI-Richtlinie entwerfen", "wir brauchen eine KI-Richtlinie", "AI-Act-konforme Richtlinie" oder Ähnliches sagt. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Viele Unternehmen haben noch keine schriftliche KI-Nutzungsrichtlinie, oder
arbeiten mit einer veralteten Fassung, die den AI Act (VO (EU) 2024/1689),
DSGVO Art. 22 und den tatsächlichen Tool-Einsatz nicht abbildet.

Dieser Skill produziert einen **Entwurf** — keinen fertigen Text. Disziplin:
(1) aus veröffentlichten Musterquellen sourcing, nicht aus dem Nichts;
(2) Umfang vor Entwurf klären; (3) jeden Ermessensspielraum mit `[prüfen]`
kennzeichnen; (4) Adoptionstatus-Signale nicht abschwächen.

Dieser Skill schließt keine Richtlinie ab, verteilt sie nicht und empfiehlt
keine konkrete Position zu den schwierigen Entscheidungspunkten.

## Eingaben

- Praxisprofil aus `CLAUDE.md` (KI-Rolle, regulatorischer Fußabdruck,
 bestehendes Register, Governance-Team, ggf. bestehende Richtlinie)
- Scopegespräch: welche Abschnitte? welche Zielgruppe? welcher Kontext?

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 4 KI-VO**: KI-Kompetenzverpflichtung — Anbieter und Betreiber
 müssen hinreichende KI-Kompetenz ihres Personals sicherstellen; Richtlinie
 muss Schulungspflicht abbilden.
- **AI Act Art. 9 KI-VO**: Risikomanagementsystem für Hochrisiko-KI; interne
 Richtlinien müssen Risikoidentifikations- und Mitigationsverfahren beschreiben.
- **AI Act Art. 26/29 KI-VO**: Betreiberpflichten — menschliche Aufsicht,
 Protokollierung, Meldeobliegenheiten; müssen in der Richtlinie operationalisiert
 werden.
- **DSGVO Art. 22**: Vollautomatisierte Einzelentscheidungen nur unter Art. 22
 Abs. 2 lit. a–c zulässig; Richtlinie muss Rechtsgrundlage und
 Widerspruchsrecht klären.
- **§ 87 Abs. 1 Nr. 6 BetrVG**: Mitbestimmungsrecht des Betriebsrats bei KI-
 Tools zur Mitarbeiterüberwachung/-bewertung; vor Richtlinienabschnitt prüfen.
- **GeschGehG §§ 2, 4**: Schutz von Geschäftsgeheimnissen bei Eingabe
 vertraulicher Daten in externe KI-Systeme.
- **UrhG § 44b**: Text-und-Data-Mining-Schranke; relevant bei KI-Training.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Richtlinie muss Art. 22 Abs. 3 DSGVO-Widerspruchsrecht bei automatisierten
 Entscheidungen operationalisieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 pflicht bei technischen Überwachungssystemen; gilt auch für KI-basierte
 Mitarbeiterbewertung.

**Kommentare**

- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 4 Rn. 3 ff.
 (KI-Kompetenzverpflichtung; interne Richtliniengestaltung).
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 1 ff.
- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 87 BetrVG Rn. 32 ff.
 (Mitbestimmung bei KI-Tools).
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 100 ff. (Compliance-Anforderungen für KI-Nutzungsrichtlinien).

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Praxisprofil laden**

`CLAUDE.md` lesen. Wenn `## KI-Richtlinien-Verpflichtungen` ausgefüllt:
Update-Modus (bestehende Richtlinie als Basis). Wenn leer: Erstfassung.

**Schritt 2 — Scopegespräch (VOR dem Entwurf)**

> **Welche Abschnitte soll die KI-Richtlinie enthalten?**
> 1. Anwendungsbereich (wer, welche Tools, welche Daten)
> 2. Erlaubte und verbotene Nutzungen (inkl. Art. 5 KI-VO-Verbote)
> 3. Freigabe und Prüfung (Genehmigungsworkflow)
> 4. Offenlegung (Kunden, Mitarbeitende, Dritte; DSGVO Art. 13/14)
> 5. Datenhandhabung (vertrauliche Daten, Anbieter-Training; GeschGehG)
> 6. Schulung und Zertifizierung (Art. 4 KI-VO)
> 7. Vorfälle und Meldung (Art. 73 KI-VO Betreiber-Meldeobliegenheiten)
> 8. Durchsetzung (Verweis auf Disziplinarrahmen)
> 9. Überprüfungsrhythmus und Verantwortung (mind. jährlich)
> 10. Glossar (Hochrisiko-KI gem. Anhang III, DSGVO Art. 22, GeschGeh usw.)
>
> Empfohlenes Startpaket für Erstfassungen: 1, 2, 3, 4, 5, 9.

Dann: Zielgruppe (alle MA / Rechtsabteilung / mit Betriebsrat?) und
Anwendungskontext (Unternehmen / Konzern / Kanzlei / Behörde).

**Schritt 3 — Musterquellen recherchieren**

Aktuelle veröffentlichte Muster-KI-Richtlinien und Leitlinien suchen:
- Deutschland/EU: AI Act direkt (Art. 4, 9, 26, 29); EDPB Guidelines 01/2022
 (Art. 22 DSGVO); DSK-Orientierungshilfen; BSI-Empfehlungen; Bitkom/DAV-
 Leitlinien; veröffentlichte Unternehmensrichtlinien aus DAX-Umfeld.
- Jeden verwendeten Quellennachweis im **Quellenblock** dokumentieren:
 Name, URL, Zugriffsdatum, was der Entwurf daraus entnommen hat.

**Schritt 4 — Entwurf erstellen**

Kopfzeile:
```
ENTWURF ZUR INTERNEN RECHTLICHEN PRÜFUNG — NICHT ZUR VERTEILUNG
Erstellt für: [Unternehmensname] | Datum: [heute]
Nicht zur Beschlussfassung bis von [Syndikusrechtsanwalt / GC / Compliance
Officer] geprüft, angepasst und freigegeben.
```

Für jeden Abschnitt: materielle Regeln aus Musterquellen, inline-
Quellenattribution, jeder Schwellenwert/Tool/Anbieter/Kontakt als `[prüfen]`.

Freigabe-Checkliste am Ende:
- [ ] Syndikusrechtsanwalt / GC `[prüfen — Name]`
- [ ] IT / Informationssicherheit `[prüfen]`
- [ ] HR (für Durchsetzungs-/Schulungsabschnitte) `[prüfen]`
- [ ] Betriebsrat (§ 87 Abs. 1 Nr. 6 BetrVG) `[prüfen — erforderlich?]`
- [ ] Datenschutzbeauftragter (Art. 38 Abs. 1 DSGVO) `[prüfen]`
- [ ] Inkrafttretungsdatum und Überprüfungsrhythmus `[prüfen]`

## Ausgabeformat

Strukturiertes Markdown-Dokument: Kopfzeile, Quellenblock, Zusammenfassung
(max. 3 Abs.), gewählte Abschnitte (materielle Regeln + inline-Quellen +
offene Fragen je Abschnitt), Freigabe-Checkliste, Prüfhinweis. Sprache
klar genug für Nicht-Juristen; Präzision liegt in den `[prüfen]`-Markern.

## Beispiel

**Anfrage:** KI-Richtlinie für 200-Personen-Unternehmen mit Betriebsrat,
Abschnitte 1, 2, 3, 5 und 9. **Vorgehen:** Betreiberrolle, Deutschland;
AI Act Art. 4/26/29; EDPB Guidelines 01/2022; § 87 Abs. 1 Nr. 6 BetrVG.
Abschnitt 3 (Freigabe): Hinweis, dass neue KI-Tools ggf. Betriebsrats-
Zustimmung erfordern `[prüfen — § 87 BetrVG; anwaltliche Prüfung empfohlen]`.

## Risiken und typische Fehler

- Richtliniensprache erfinden: jede materielle Regel aus einer Quelle
 belegen oder `[prüfen — adaptiert, keine Direktquelle]` kennzeichnen.
- Schwierige Entscheidungen vorwegnehmen: das ist ein `[prüfen]`, keine
 empfohlene Position.
- § 87 BetrVG vergessen: bei Unternehmen mit Betriebsrat immer prüfen.
- Scope-Gespräch überspringen: "einfach alles" ist die Hauptfehlerquelle.

## Quellenpflicht

- **AI Act Art. 4, 9, 26/29** — VO (EU) 2024/1689.
- **DSGVO Art. 22** bei automatisierten Entscheidungen.
- **§ 87 Abs. 1 Nr. 6 BetrVG** bei Mitarbeiter-KI.
- **GeschGehG §§ 2, 4** bei Abschnitt zu vertraulichen Daten.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Entscheidungen.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 4.**
- **Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22.**
- **Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 87 BetrVG Rn. 32 ff.**

## Triage zu Beginn
1. Existiert bereits eine KI-Nutzungsrichtlinie — vollstaendig oder veraltet (vor KI-VO 2024)?
2. Welche Zielgruppe soll die Richtlinie adressieren — alle Mitarbeiter, IT, Fachabteilungen?
3. Ist ein Betriebsrat vorhanden — ist § 87 Abs. 1 Nr. 6 BetrVG-Mitbestimmung einzuholen?
4. Welche KI-Systeme sind bereits im Einsatz — Inventar aus ki-inventar-Skill vorhanden?
5. Welches regulatorische Regime ist massgeblich — KI-VO Hochrisiko, DSGVO Art. 22, DSA?

## Output-Template — KI-Nutzungsrichtlinie (Entwurf)
**Adressat:** Alle Mitarbeiter / Geschaeftsleitung — Tonfall: klar, verbindlich, anwaltlich pruefbeduerftig
```
KI-NUTZUNGSRICHTLINIE
[UNTERNEHMEN] — Version [VERSIONSNUMMER] — Stand: [DATUM]
ENTWURF — VOR EINSATZ ANWALTLICHE PRUEFUNG ERFORDERLICH

§ 1 Geltungsbereich und Zweck
Diese Richtlinie gilt für alle Mitarbeiterinnen und Mitarbeiter von
[NAME MANDANT] beim Einsatz von KI-Systemen im Rahmen ihrer Taetigkeit.
Zweck ist die Sicherstellung eines rechtssicheren, transparenten und
verantwortungsvollen KI-Einsatzes gemaess KI-VO (VO 2024/1689) und DSGVO.

§ 2 Freigegebene KI-Systeme
Folgende KI-Systeme sind für den Einsatz freigegeben:
- [SYSTEM 1]: zulaessige Verwendungszwecke
- [SYSTEM 2]: zulaessige Verwendungszwecke

§ 3 Verbotene Praktiken (Art. 5 KI-VO)
Der Einsatz von KI-Systemen für folgende Zwecke ist absolut verboten: [...]

§ 4 Menschliche Aufsicht (Art. 26 KI-VO)
Bei Hochrisiko-Anwendungen ist eine menschliche Pruefung vor jeder
Entscheidung sicherzustellen. Vollautomatisierte Entscheidungen nach
Art. 22 DSGVO sind nur nach Freigabe durch [ROLLE] zulaessig.

§ 5 Datenschutz und Vertraulichkeit
Personenbezogene und vertrauliche Daten duerfen nur in KI-Systeme
eingegeben werden, für die ein AVV nach Art. 28 DSGVO besteht.

§ 6 Meldepflichten
Sicherheitsvorfaelle und Probleme mit KI-Ausgaben sind unverzueglich
an [ANSPRECHPARTNER] zu melden.

§ 7 Schulung
Alle Mitarbeiter, die KI-Systeme einsetzen, besuchen die verpflichtende
KI-Schulung bis [DATUM] (Art. 4 KI-VO Kompetenzgebot).

Ansprechpartner KI-Governance: [NAME, EMAIL]
Datenschutzbeauftragter: [NAME, EMAIL]

[DATUM] — [UNTERSCHRIFT GESCHAEFTSFUEHRUNG]
```
