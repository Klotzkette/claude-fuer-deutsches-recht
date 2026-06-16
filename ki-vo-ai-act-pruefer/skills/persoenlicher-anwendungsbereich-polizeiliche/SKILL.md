---
name: persoenlicher-anwendungsbereich-polizeiliche
description: "Erster Schritt der KI-VO-Prüfung: Wer ist betroffen? Unternehmen fragt welche Rolle es in der KI-VO einnimmt. Art. 3 KI-VO Rollendefinitionen. Prüfraster: Anbieter Art. 3 Nr. 3 Betreiber Art. 3 Nr. 4 Einführer Art. 3 Nr. 6 Haendler Art. 3 Nr. 7 Produkthersteller Art. 25 Bevollmaechtigter Art. 22"
---

# Persönlicher Anwendungsbereich — Rollen nach Art. 3 KI-VO

## Arbeitsbereich

Erster Schritt der KI-VO-Prüfung: Wer ist betroffen? Unternehmen fragt welche Rolle es in der KI-VO einnimmt. Art. 3 KI-VO Rollendefinitionen. Prüfraster: Anbieter Art. 3 Nr. 3 Betreiber Art. 3 Nr. 4 Einführer Art. 3 Nr. 6 Haendler Art. 3 Nr. 7 Produkthersteller Art. 25 Bevollmaechtigter Art. 22. Output: Rollenzuordnungsentscheidung als Einstieg für alle weiteren Pflichten-Skills. Abgrenzung zu rolle-anbieter-prüfen-art-3-nr-3 und rolle-betreiber-prüfen-art-3-nr-4 (detaillierte Rollenentscheidungsbaeume). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Art. 5 Verbote ab 02.02.2025, Art. 51-55 GPAI ab 02.08.2025, Hochrisiko Anhang III ab 02.08.2026, Hochrisiko Anhang I ab 02.08.2027, schwerwiegender Vorfall 15 Tage / 2 Tage (Tod).
- Tragende Normen verifizieren: KI-VO (EU 2024/1689) Art. 3, 5 (Verbote), 6 (Hochrisiko), 8-15 (Anforderungen), 16, 26 (Pflichten Anbieter/Betreiber), 50 (Transparenz), 51-55 (GPAI), 73, 99 (Sanktionen) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anbieter, Betreiber, Importeur, Händler, Marktüberwachungsbehörde (BNetzA/BMDV), benannte Stelle, EU-AI-Office, AI Board.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung Art. 47, technische Dokumentation Anhang IV, Risikomanagement-System Art. 9, Datengovernance Art. 10, FRIA (Fundamental Rights Impact Assessment) Art. 27, EU-Datenbank-Registrierung Art. 49 — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rollen im Überblick

### Anbieter (provider) — Art. 3 Nr. 3 KI-VO

Wer ein KI-System oder ein GPAI-Modell entwickelt oder entwickeln lässt und es unter seinem eigenen Namen oder seiner Marke in Verkehr bringt oder in Betrieb nimmt — entgeltlich oder unentgeltlich.

Detailprüfung: `rolle-anbieter-pruefen-art-3-nr-3`

### Betreiber (deployer) — Art. 3 Nr. 4 KI-VO

Wer ein KI-System in eigener Verantwortung verwendet, es sei denn, das System wird für persönliche, nicht berufliche Tätigkeiten genutzt.

Detailprüfung: `rolle-betreiber-pruefen-art-3-nr-4`

### Einführer (importer) — Art. 3 Nr. 6 KI-VO

Wer ein in einem Drittland in Verkehr gebrachtes KI-System in der EU in Verkehr bringt.

Detailprüfung: `einfuehrer-importer-pflichten-art-23`

### Händler (distributor) — Art. 3 Nr. 7 KI-VO

Wer ein KI-System in der Lieferkette zur Verfügung stellt, ohne Anbieter oder Einführer zu sein, und wer das System nicht wesentlich verändert.

Detailprüfung: `haendler-distributor-pflichten-art-24`

### Bevollmächtigter — Art. 3 Nr. 5 KI-VO

Eine in der EU ansässige natürliche oder juristische Person, die vom Anbieter eines in einem Drittland ansässigen schriftlich bevollmächtigt wurde, in seinem Namen bestimmte Aufgaben zu erfüllen.

Detailprüfung: `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

### Produkthersteller — Art. 3 in Verbindung mit Art. 25 Abs. 1 KI-VO

Wer ein KI-System als Sicherheitsbauteil in ein Produkt integriert, das unter Anhang I gelistete Unionsvorschriften fällt, und das Produkt unter eigenem Namen in Verkehr bringt.

Detailprüfung: `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

## Mehrfachrollen

In der Praxis sind Mehrfachrollen häufig:

- Wer ein fremdes KI-System wesentlich verändert und unter eigenem Namen in Verkehr bringt, wird zum Anbieter (Art. 25 KI-VO) → `anbieter-werden-art-25`
- Wer ein System selbst entwickelt und auch selbst einsetzt, ist gleichzeitig Anbieter und Betreiber.
- Einführer können unter bestimmten Bedingungen als Anbieter behandelt werden (Art. 23 Abs. 4 KI-VO).

## Routing

| Rolle | Nächster Skill |
|---|---|
| Anbieter | `rolle-anbieter-pruefen-art-3-nr-3` |
| Betreiber | `rolle-betreiber-pruefen-art-3-nr-4` |
| Einführer | `einfuehrer-importer-pflichten-art-23` |
| Händler | `haendler-distributor-pflichten-art-24` |
| Bevollmächtigter / Produkthersteller | `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25` |
| Unklare Rolle / Rollenwechsel möglich | `anbieter-werden-art-25` |

## Wichtiger Hinweis

Die Rollenzuordnung bestimmt den gesamten weiteren Prüfverlauf. Falsche Rolleneinschätzungen können dazu führen, dass wesentliche Pflichten übersehen werden. Im Zweifel sind alle in Betracht kommenden Rollen zu prüfen.

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
PRUEFERGEBNIS — PERSOENLICHER ANWENDUNGSBEREICH ROLLEN ART 3
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 3 Nr. 3/4 Rn. 12]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

