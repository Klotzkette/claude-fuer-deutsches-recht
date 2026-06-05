---
name: richtlinien-monitor-vorlage-anbieter
description: "Richtlinien Monitor Vorlage Anbieter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Richtlinien Monitor Vorlage Anbieter

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Richtlinien Monitor Vorlage Anbieter** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `richtlinien-monitor` | Überwacht die interne KI-Richtlinie auf Abweichungen von der gelebten Praxis — wöchentlicher Abgleich gespeicherter Folgenabschätzungen, Triage-Ergebnisse und Anbieterprüfungen, oder direkte Prüfung einer geplanten neuen KI-Praxis. Lädt, wenn der Nutzer "Richtlinien-Sweep", "KI-Richtlinie prüfen", "deckt unsere Richtlinie das ab", "wir wollen X einführen — brauchen wir eine Richtlinienänderung" oder "Policy-Monitor starten" sagt. |
| `richtlinien-vorlage` | Entwirft eine interne KI-Nutzungsrichtlinie auf Basis veröffentlichter Musterrichtlinien und des Praxisprofils — Recherche- und Synthese-Tool, dessen Ausgabe ein Entwurf für die anwaltliche Prüfung und Freigabe ist, keine fertige Richtlinie. Lädt, wenn der Nutzer "KI-Richtlinie entwerfen", "wir brauchen eine KI-Richtlinie", "AI-Act-konforme Richtlinie" oder Ähnliches sagt. |
| `spezial-anbieter-mehrparteien-konflikt-und-interessen` | Anbieter: Mehrparteienkonflikt und Interessenmatrix im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **Richtlinien Monitor Vorlage Anbieter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `richtlinien-monitor`

**Fokus:** Überwacht die interne KI-Richtlinie auf Abweichungen von der gelebten Praxis — wöchentlicher Abgleich gespeicherter Folgenabschätzungen, Triage-Ergebnisse und Anbieterprüfungen, oder direkte Prüfung einer geplanten neuen KI-Praxis. Lädt, wenn der Nutzer "Richtlinien-Sweep", "KI-Richtlinie prüfen", "deckt unsere Richtlinie das ab", "wir wollen X einführen — brauchen wir eine Richtlinienänderung" oder "Policy-Monitor starten" sagt.

# KI-Richtlinien-Monitor

## Zweck

KI-Richtlinien laufen der Praxis schneller hinterher als fast jedes andere
Richtliniendokument — Anwendungsfälle multiplizieren sich, jede freigegebene
Folgenabschätzung begründet neue Verpflichtungen, die die Richtlinie noch
nicht aufgegriffen hat.

Zwei Modi: (1) **Sweep-Modus** — wöchentlicher Abgleich des Ausgabeordners
auf Policy-Drift; (2) **Direktanfrage-Modus** — direkte Antwort auf
"Wir wollen X einführen — was bedeutet das für unsere KI-Richtlinie?"

Ausgabe ist immer: Hier ist die Lücke — ERFORDERLICH (Richtlinie wider-
spricht Praxis) oder EMPFOHLEN (Richtlinie schweigt) — plus Formulierungsvorschlag.

## Eingaben

**Sweep-Modus:** `CLAUDE.md` (Ausgabeordner-Pfad, Richtlinienstandort,
letztes Sweep-Datum); alle Ausgabedateien seit letztem Sweep.

**Direktanfrage-Modus:** Beschreibung der geplanten KI-Praxis; aktuelle
Richtlinien-Verpflichtungen und Anwendungsfall-Register aus `CLAUDE.md`.

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 17 KI-VO**: Anbieter von Hochrisiko-KI müssen ein Qualitäts-
 managementsystem unterhalten inkl. laufender Überprüfung. Für Betreiber:
 Art. 29 Abs. 1–4 KI-VO (Überwachungs- und Meldepflichten).
- **DSGVO Art. 5 Abs. 2 (Rechenschaftspflicht)**: Verantwortliche müssen
 Einhaltung der Grundsätze nachweisen; Richtlinie und gelebte Praxis
 müssen übereinstimmen.
- **DSGVO Art. 22 i.V.m. Art. 13/14**: Betroffene müssen über automatisierte
 Entscheidungen informiert werden; Richtlinie muss Offenlegungspflichten
 widerspiegeln.
- **DSA Art. 27, 38 (VO (EU) 2022/2065)**: Transparenzpflichten für
 algorithmische Empfehlungssysteme sehr großer Plattformen.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 KI-Richtlinie ohne Adressierung von Scoring-Systemen schafft materielle
 Lücke, wenn entsprechende Systeme operativ eingesetzt werden.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Vergessen I): Grundrechtliche Schutzpflichten gegenüber algorithmischen
 Systemen; Transparenzgebot beim KI-Einsatz.

**Kommentare**

- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 17 Rn. 8 ff.
 (Qualitätsmanagementsystem; laufende Richtlinienüberprüfung).
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 5 Rn. 62 ff.
 (Rechenschaftspflicht; Dokumentation der Verarbeitungspolitik).
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 95 ff. (Transparenzpflichten bei Algorithmen).
- Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 89 ff.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Modus-Erkennung:** kein Argument oder `--sweep` → Sweep-Modus;
Beschreibung einer Praxis → Direktanfrage-Modus.

### Sweep-Modus

1. `CLAUDE.md` laden: `## KI-Richtlinien-Verpflichtungen`, `## KI-Anwendungsfall-
 Register`, `## Ausgaben` (Ordner-Pfad, Richtlinienstandort, letztes Sweep-Datum).
2. Ausgabedateien seit letztem Sweep scannen. Bei keinen neuen Dateien:
 "Keine neuen Ausgaben seit [Datum]. Nächster Sweep: [Datum]."
3. Aus jeder Ausgabe extrahieren: freigegebener Anwendungsfall, Einsatzmodus
 (assistiv/automatisiert), Auflagen, betroffene Parteien, Anbieter-Datennutzung.
4. Kennzeichnen: neue Anwendungsfälle ohne Richtlinienabdeckung; automatisierte
 Entscheidungen wo Richtlinie menschliche Aufsicht impliziert; Anbieter-
 Datennutzung die Richtlinie referenzieren sollte.
5. Lücken klassifizieren: **ERFORDERLICH** (Richtlinie widerspricht Praxis,
 Nicht-Aktualisierung = materielle Falschdarstellung) oder **EMPFOHLEN**
 (Richtlinie schweigt, Praxis vertretbar aber klarer mit Aktualisierung).
6. Ergebnisse vorlegen; erst nach Bestätigung durch den Nutzer:
 `Letztes Sweep-Datum` und `gefundene_Lücken` in `CLAUDE.md` aktualisieren.

### Direktanfrage-Modus

Aus der Beschreibung extrahieren: KI-System; Funktion (assistiv/automatisiert/
Inhaltsgenerierung); Betroffene; Anbieter; menschliche Überprüfung?; Offenlegung?;
unerwartete Datenweitergabe? — bei vager Beschreibung eine Rückfrage.

Abgleich gegen Richtlinie und Register:

| Prüfpunkt | Aktuelle Richtlinie / Register | Geplante Praxis | Ergebnis |
|---|---|---|---|
| Anwendungsfall-Kategorie | [Register-Eintrag] | [neu] | ✅/⚠️/❌ |
| Automatisierte Entscheidung | [DSGVO Art. 22 Position] | [automatisiert?] | |
| Offenlegung ggü. Betroffenen | [Richtlinien-Zusage] | [erforderlich?] | |
| Anbieter-Datennutzung | [Playbook-Position] | [Anbieter-Bedingungen] | |

## Ausgabeformat

**Sweep-Bericht:**
```
# KI-Richtlinien-Monitor — Sweep-Bericht
Datum: [Datum] | Gescannte Ausgaben: [N] | Neu: [N]
Gefundene Lücken: [N] ERFORDERLICH | [N] EMPFOHLEN

## ERFORDERLICHE Änderungen
### [Lücke]
Quelle: [Datei] | Was geschieht: [Beschreibung]
Aktuelle Richtlinie: [Zitat oder "Keine Abdeckung"]
Lücke: [was fehlt]
Formulierungsvorschlag: "[Richtlinientext]" — ergänzen in [Abschnitt]

## EMPFOHLENE Änderungen [gleiche Struktur]

## Kein Handlungsbedarf [Liste]
## Anwendungsfall-Register-Abgleich [neue Einträge vorschlagen]
```

**Direktanfrage-Ausgabe:**
```
# KI-Richtlinienprüfung: [Praxis]
Ergebnis: [RICHTLINIENÄNDERUNG ERFORDERLICH / EMPFOHLEN / KEINE ÄNDERUNG]

## Was abgedeckt ist | ## Was fehlt | ## Was im Widerspruch steht
## Anwendungsfall-Register [Vorschlag falls neu]
## Zeitplan [vor Inbetriebnahme / beim nächsten Update]
```

## Beispiel

**Direktanfrage:** "Wir wollen KI-gestützte Zusammenfassungen von
Kundenbeschwerden einführen. Ein Mitarbeiter überprüft sie vor Weiterleitung."

**Ausgabe:** Register-Eintrag "Kundenseitige KI-Assistenz" → bedingt →
Offenlegung erforderlich. Richtlinie schweigt zur KI-gestützten Beschwerde-
bearbeitung. EMPFOHLENE Ergänzung: Abschnitt zu assistierter Kunden-
kommunikation. DSGVO Art. 13/14: Datenschutzinformation muss KI-Einsatz
nennen. Ergebnis: RICHTLINIENÄNDERUNG EMPFOHLEN.

## Risiken und typische Fehler

- Sweep-Datum vor Bestätigung aktualisieren: unterdrückt beim nächsten Lauf
 die Aufmerksamkeit für dieselben Lücken.
- Zu vage Formulierungsvorschläge: "KI-gestützt" bevorzugen statt
 konkreter Modellnamen; keine Zusagen formulieren, die das Team nicht
 einhalten kann.
- Richtlinie selbst aktualisieren: nur nach menschlicher Prüfung und Freigabe.
- Eingehende Regelungsänderungen: das ist `regulierungs-luecken-analyse`. Dieser Skill
 überwacht nur interne Praxis-Abweichungen.

## Quellenpflicht

- **AI Act Art. 17** (Qualitätsmanagement) bei Hochrisiko-Anwendungsfällen.
- **AI Act Art. 29** (Betreiberpflichten, Überwachung).
- **DSGVO Art. 5 Abs. 2** (Rechenschaftspflicht) bei Richtlinien-Dokumentation.
- **DSGVO Art. 22** bei automatisierten Entscheidungen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 17.**
- **Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 5 Rn. 62 ff.**

## Triage zu Beginn
1. Sweep-Modus oder Direktanfrage — neue Praxis oder regelmäßiger Policy-Abgleich?
2. Wann war der letzte Sweep — sind neue Anwendungsfaelle oder Folgenabschaetzungen seit dann dazugekommen?
3. Gibt es bereits bekannte Richtlinien-Praxis-Kluft (z.B. Anwendungsfall ohne Richtlinien-Deckung)?
4. Betrifft die neue Praxis einen Hochrisiko-Bereich (Art. 9 KI-VO Qualitaetsmanagement)?
5. Ist eine Betriebsrats-Beteiligung nach § 87 Abs. 1 Nr. 6 BetrVG relevant?

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template — Richtlinien-Monitor-Bericht
**Adressat:** KI-Governance-Verantwortlicher — Tonfall: sachlich-strukturiert
```
RICHTLINIEN-MONITOR-BERICHT
[DATUM] — Modus: [SWEEP / DIREKTANFRAGE] — Zeitraum: [DATUM BIS DATUM]

BEFUNDE:
| Nr. | Thema | Richtlinien-Position | Gelebte Praxis | Status | Empfehlung |
|---|---|---|---|---|---|
| 1 | [THEMA] | [RICHTLINIENTEXT] | [PRAXIS] | ERFORDERLICH/EMPFOHLEN | [FORMULIERUNGSVORSCHLAG] |

ZUSAMMENFASSUNG: [N] ERFORDERLICH / [N] EMPFOHLEN / [N] konform

NAECHSTE SCHRITTE:
1. Richtlinienaktualisierung: [ABSCHNITT] — Verantwortlicher: [NAME] — bis: [DATUM]
2. [WEITERE MASSNAHME]

Naechster Sweep: [DATUM]
Erstellt: [NAME], [DATUM]
```

## 2. `richtlinien-vorlage`

**Fokus:** Entwirft eine interne KI-Nutzungsrichtlinie auf Basis veröffentlichter Musterrichtlinien und des Praxisprofils — Recherche- und Synthese-Tool, dessen Ausgabe ein Entwurf für die anwaltliche Prüfung und Freigabe ist, keine fertige Richtlinie. Lädt, wenn der Nutzer "KI-Richtlinie entwerfen", "wir brauchen eine KI-Richtlinie", "AI-Act-konforme Richtlinie" oder Ähnliches sagt.

# KI-Richtlinien-Starter

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
Diese Richtlinie gilt fuer alle Mitarbeiterinnen und Mitarbeiter von
[NAME MANDANT] beim Einsatz von KI-Systemen im Rahmen ihrer Taetigkeit.
Zweck ist die Sicherstellung eines rechtssicheren, transparenten und
verantwortungsvollen KI-Einsatzes gemaess KI-VO (VO 2024/1689) und DSGVO.

§ 2 Freigegebene KI-Systeme
Folgende KI-Systeme sind fuer den Einsatz freigegeben:
- [SYSTEM 1]: zulaessige Verwendungszwecke
- [SYSTEM 2]: zulaessige Verwendungszwecke

§ 3 Verbotene Praktiken (Art. 5 KI-VO)
Der Einsatz von KI-Systemen fuer folgende Zwecke ist absolut verboten: [...]

§ 4 Menschliche Aufsicht (Art. 26 KI-VO)
Bei Hochrisiko-Anwendungen ist eine menschliche Pruefung vor jeder
Entscheidung sicherzustellen. Vollautomatisierte Entscheidungen nach
Art. 22 DSGVO sind nur nach Freigabe durch [ROLLE] zulaessig.

§ 5 Datenschutz und Vertraulichkeit
Personenbezogene und vertrauliche Daten duerfen nur in KI-Systeme
eingegeben werden, fuer die ein AVV nach Art. 28 DSGVO besteht.

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

## 3. `spezial-anbieter-mehrparteien-konflikt-und-interessen`

**Fokus:** Anbieter: Mehrparteienkonflikt und Interessenmatrix im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Anbieter: Mehrparteienkonflikt und Interessenmatrix

## Spezialwissen: Anbieter: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Anbieter: Mehrparteienkonflikt und Interessenmatrix / anbieter mehrparteien konflikt und interessen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, KI, VO, DSGVO, AIA, DPIA.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anbieter** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
