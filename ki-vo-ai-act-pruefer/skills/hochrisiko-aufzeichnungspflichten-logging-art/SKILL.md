---
name: hochrisiko-aufzeichnungspflichten-logging-art
description: "Anbieter von Hochrisiko-KI fragt: Was muss unser System automatisch aufzeichnen und wie lange muessen wir die Logs aufbewahren? Art. 12 KI-VO Logging-Pflichten. Prüfraster: Mindestinhalte der Logs Zeitstempel Eingabedaten Ausgaben Fehlermeldungen Aufbewahrungsfrist drei Jahre bzw. Vertragsdauer V..."
---

# Aufzeichnungspflichten und Logging — Art. 12 KI-VO

## Grundanforderung: Automatische Protokollierung (Art. 12 Abs. 1 KI-VO)

Hochrisiko-KI-Systeme müssen automatisch Ereignisse protokollieren, die für die Kontrolle des Systembetriebs und die Ermittlung von Risiken nach dem Inverkehrbringen relevant sind.

**Grundsatz:** Die Protokollierung muss technisch in das System integriert sein — manuelle Nacherfassung genügt nicht.

## Mindestinhalt der Logs (Art. 12 Abs. 2 KI-VO)

Die Protokolle müssen mindestens enthalten:
- Zeitstempel jedes Ereignisses
- Referenzdatenbankeinträge (wenn das System mit Datenbanken arbeitet)
- Eingabedaten (soweit relevant für die Nachvollziehbarkeit)
- Identität der natürlichen Personen, die an der Überprüfung der Ergebnisse beteiligt sind (wo zutreffend)
- Datum, Uhrzeit und Ort des Betriebs des Systems

**Prüffragen:**
- Protokolliert das System automatisch alle relevanten Ereignisse?
- Sind Zeitstempel, Eingaben und Ausgaben nachvollziehbar erfasst?
- Werden Identitäten der beteiligten Personen (wo relevant) erfasst?

## Besondere Anforderungen — Biometrische Fernidentifikation

Für biometrische Echtzeit-Fernidentifikationssysteme (die nur unter den engen Ausnahmen von Art. 5 Abs. 2 KI-VO zulässig sind) gelten besonders strenge Protokollierungsanforderungen. Jeder Einsatz ist zu protokollieren, und die Protokolle müssen der Datenschutzbehörde auf Anfrage zugänglich gemacht werden.

## Verantwortungsverteilung zwischen Anbieter und Betreiber

**Anbieter:** Muss sicherstellen, dass das System technisch in der Lage ist, die erforderlichen Logs zu erstellen. Die Protokollierungsfähigkeit ist Teil der technischen Spezifikation.

**Betreiber:** Muss sicherstellen, dass die Protokolle tatsächlich erstellt, gespeichert und aufbewahrt werden. Betreiber sind nach Art. 26 Abs. 6 KI-VO verpflichtet, die Protokolle sechs Monate aufzubewahren, es sei denn, andere Vorschriften (z.B. DSGVO, nationales Recht) sehen kürzere oder längere Fristen vor.

**Prüffragen:**
- Welche Partei ist für die Protokollierung verantwortlich — Anbieter, Betreiber oder beide?
- Gibt es vertragliche Regelungen zwischen Anbieter und Betreiber zur Protokollierung (Art. 25 Abs. 4 KI-VO)?

## Aufbewahrungsfristen

- **Betreiber allgemein:** Sechs Monate Aufbewahrungspflicht (Art. 26 Abs. 6 KI-VO)
- **Biometrische Identifikation:** Besondere Fristen nach nationalem Recht oder Behördenanforderungen
- **Anbieter (technische Dokumentation):** Zehn Jahre (Art. 18 KI-VO)
- **Widerspruch mit DSGVO:** Protokolle, die personenbezogene Daten enthalten, müssen datenschutzkonform aufbewahrt und nach Ablauf der Frist gelöscht werden

## Verhältnis zu Post-Market-Monitoring

Die nach Art. 12 KI-VO erstellten Protokolle sind ein wesentliches Instrument für das Post-Market-Monitoring nach Art. 72 KI-VO. Ohne Protokolle kann ein ernsthafter Vorfall nicht aufgeklärt werden.

## Typische Lücken

- Protokollierung ist nicht automatisiert und basiert auf manuellen Einträgen.
- Logs werden nach kurzer Zeit automatisch gelöscht (z.B. für Datensparsamkeit), ohne Berücksichtigung der Aufbewahrungspflichten.
- Kein klarer Verantwortlicher für die Aufbewahrung der Logs.
- Logs enthalten keine ausreichenden Zeitstempel oder Kontextinformationen für die Rekonstruktion von Vorfällen.

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
PRUEFERGEBNIS — HOCHRISIKO AUFZEICHNUNGSPFLICHTEN LOGGING ART 12
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 12 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
