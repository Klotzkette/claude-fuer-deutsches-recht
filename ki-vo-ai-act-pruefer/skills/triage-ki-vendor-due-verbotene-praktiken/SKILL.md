---
name: triage-ki-vendor-due-verbotene-praktiken
description: "Nutzer kommt mit unklarer KI-VO-Frage oder möglicherweise betroffener Software und fragt: Wie starte ich die KI-VO-Prüfung? Eingangs-Triage-Skill. Prüfraster: Erfassung ob eigene Softwareentwicklung fremder Dienst Produktintegration oder Beratungsanfrage. Eingangsfragen zu Systemart Branche Einsa"
---

# Triage: KI-VO-Vorprüfung — Was prüft der Nutzer?

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Art. 5 Verbote ab 02.02.2025, Art. 51-55 GPAI ab 02.08.2025, Hochrisiko Anhang III ab 02.08.2026, Hochrisiko Anhang I ab 02.08.2027, schwerwiegender Vorfall 15 Tage / 2 Tage (Tod).
- Tragende Normen verifizieren: KI-VO (EU 2024/1689) Art. 3, 5 (Verbote), 6 (Hochrisiko), 8-15 (Anforderungen), 16, 26 (Pflichten Anbieter/Betreiber), 50 (Transparenz), 51-55 (GPAI), 73, 99 (Sanktionen) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anbieter, Betreiber, Importeur, Händler, Marktüberwachungsbehörde (BNetzA/BMDV), benannte Stelle, EU-AI-Office, AI Board.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung Art. 47, technische Dokumentation Anhang IV, Risikomanagement-System Art. 9, Datengovernance Art. 10, FRIA (Fundamental Rights Impact Assessment) Art. 27, EU-Datenbank-Registrierung Art. 49 — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingangsfragen

Das System stellt folgende Fragen der Reihe nach:

**Frage 1 — Art des Gegenstands**

Was wird geprüft?
- (A) Ich habe selbst eine Software oder ein System entwickelt oder lasse es entwickeln.
- (B) Ich nutze einen fremden KI-Dienst (Cloud-Dienst, Drittanbieter-Produkt, API) in meinem Betrieb.
- (C) Ich integriere ein KI-System oder KI-Komponente in ein eigenes Produkt.
- (D) Ich berate Mandanten zu einem KI-System oder einer KI-VO-Fragestellung.
- (E) Ich weiß noch nicht genau — bitte führe mich.

**Frage 2 — Beschreibung des Systems**

Bitte beschreiben Sie in Stichpunkten:
- Was tut das System? (Beispiele: Bilderkennung, Textgenerierung, Scoring, Empfehlung, Entscheidungsunterstützung)
- In welchem Bereich wird es eingesetzt? (Beispiele: Personalwesen, Medizin, Kredit, Strafverfolgung, Bildung, allgemeine Nutzung)
- Wer sind die betroffenen Personen? (Beispiele: Bewerber, Patienten, Kreditnehmer, Bürger)

**Frage 3 — Standort und Markt**

- Wo soll das System eingesetzt werden? (EU / außerhalb EU / unklar)
- Werden Ausgaben des Systems in der EU verwendet, auch wenn das System außerhalb betrieben wird?

## Plausibilitätsprüfung

Das System prüft auf Basis der Eingaben:
- Handelt es sich möglicherweise gar nicht um ein KI-System im Sinne von Art. 3 Nr. 1 KI-VO? → Weiterleitung zu `liegt-ki-system-vor-art-3-nr-1`
- Liegt ein offensichtlicher Ausschluss nach Art. 2 Abs. 3 bis 12 vor (Militär, rein persönliche Nutzung)? → Weiterleitung zu `sachlicher-ausschluss-art-2-abs-3-bis-12`
- Verwechselt der Nutzer die KI-VO mit einem anderen Rechtsgebiet (DSGVO, Produkthaftung)? → Weiterleitung zu `falsche-wiese-warnung-ki-vo`

## Routing-Logik

| Antwort | Nächster Skill |
|---|---|
| Variante A oder C | `liegt-ki-system-vor-art-3-nr-1` → `rolle-anbieter-pruefen-art-3-nr-3` |
| Variante B | `liegt-ki-system-vor-art-3-nr-1` → `rolle-betreiber-pruefen-art-3-nr-4` |
| Variante D | `mandatsabbruch-empfehlung-komplexe-faelle` (Hinweis auf Grenzen des Mechanik-Workflows) |
| Variante E | Rückfragen zu Beschreibung, dann Routing nach Sachverhalt |

## Wichtige Einschränkungen

- Das System akzeptiert keine fiktiven Testdaten oder Mustersachverhalte.
- Unvollständige Sachverhalte führen zu unvollständigen Ergebnissen — das System weist ausdrücklich darauf hin.
- Dieser ist ein mechanisches Prüfinstrument, kein juristisches Gutachten.

## Warnblock

**Achtung — Keine Rechtsberatung:**
Dieser Skill erfasst nur, was der Nutzer mitteilt. Er kann nicht prüfen, ob die Sachverhaltsdarstellung vollständig oder korrekt ist. Alle Ergebnisse stehen unter dem Vorbehalt der vom Nutzer behaupteten Tatsachen.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Maßnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Prüfergebnis
**Adressat:** Prüfer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — TRIAGE KI VO VORPRUEFUNG
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 2 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
