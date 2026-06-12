---
name: output-konformitaetserklaerung-eu-anhang-v
description: "Anbieter benoetigt das fertige Musterdokument für die EU-Konformitätserklärung zum Ausfuellen und Unterzeichnen. Art. 47 i.V.m. Anhang V KI-VO EU-Konformitätserklärung. Pflichtinhalt Anhang V: eindeutige Systemidentifikation Anbieter Bevollmaechtigter Verweis auf harmonisierte Normen gemeinsame S..."
---

# Output: EU-Konformitätserklärung — Art. 47 und Anhang V KI-VO

## Rechtliche Grundlage

Art. 47 KI-VO verpflichtet Anbieter, für jedes Hochrisiko-KI-System eine EU-Konformitätserklärung auszustellen. Diese Erklärung bestätigt, dass das System die Anforderungen der KI-VO erfüllt. Inhalt und Format sind in Anhang V KI-VO festgelegt.

**Wichtiger Hinweis:** Die EU-Konformitätserklärung ist nur dann rechtlich wirksam, wenn tatsächlich eine vollständige Konformitätsbewertung nach Art. 43 bis 49 KI-VO durchgeführt wurde. Die Erklärung ist kein Ersatz für die Konformitätsbewertung.

## Muster EU-Konformitätserklärung (Anhang V KI-VO)

```
EU-KONFORMITÄTSERKLÄRUNG
nach Anhang V der Verordnung (EU) 2024/1689

Nr.: [Eindeutige Erklärungsnummer]

1. Bezeichnung des KI-Systems:
 [Produktname, Modellbezeichnung, Version]

2. Name und Anschrift des Anbieters:
 [Firma]
 [Straße und Hausnummer]
 [PLZ Ort]
 [EU-Mitgliedstaat]

3. Name und Anschrift des Bevollmächtigten
 (falls außerhalb EU):
 [Name und Anschrift des Bevollmächtigten]

4. Die alleinige Verantwortung für die
 Ausstellung dieser Konformitätserklärung
 trägt der Anbieter.

5. Gegenstand der Erklärung
 (Identifikation des KI-Systems, das eine
 Rückverfolgung ermöglicht):
 [Beschreibung des KI-Systems]
 [Verwendungszweck]
 [Versionsnummer oder Seriennummer]

6. Der oben beschriebene Gegenstand der
 Erklärung entspricht den einschlägigen
 Unionsrechtsvorschriften:
 Verordnung (EU) 2024/1689 (KI-VO)

7. Angaben zu den angewandten harmonisierten
 Normen, gemeinsamen Spezifikationen oder
 sonstigen Spezifikationen, auf die sich
 die Konformitätserklärung bezieht:
 [Harmonisierte Norm nur nennen, wenn einschlaegige Fundstelle im Amtsblatt der EU veroeffentlicht ist]
 [Verweis auf gemeinsame Spezifikationen, falls einschlaegig]
 [Verweis auf sonstige technische Spezifikationen, z.B. interne Tests oder ISO/IEC-Standards ohne Vermutungswirkung]

8. Angaben zur beteiligten benannten Stelle
 (falls zutreffend):
 [Name der benannten Stelle]
 [Kennnummer der benannten Stelle]
 [Art der Konformitätsbewertung]
 [Bescheinigungsnummer und -datum]

9. Zusätzliche Informationen
 [Besondere Einsatzbedingungen,
 Einschränkungen oder Hinweise]

Unterzeichnet für und im Namen des Anbieters:

Ort: _____________________
Datum: _____________________

Name: _____________________
Funktion: _____________________
Unterschrift: _____________________
```

## Pflichtinhalt nach Anhang V KI-VO

Die Erklärung muss mindestens enthalten:
- Name und Anschrift des Anbieters und seines Bevollmächtigten
- Eine Beschreibung des Hochrisiko-KI-Systems, einschließlich seiner Bezeichnung und Version
- Eine Erklärung, dass das KI-System den Anforderungen der KI-VO und gegebenenfalls anderer einschlägiger Unionsrechtsakte entspricht
- Verweis auf die angewandten harmonisierten Normen oder gemeinsamen Spezifikationen
- Gegebenenfalls Name und Kennnummer der beteiligten benannten Stelle, Verweis auf die ausgestellten Bescheinigungen
- Ort und Datum der Ausstellung, Unterschrift

## Aufbewahrung

Die EU-Konformitätserklärung ist zehn Jahre ab dem Datum des Inverkehrbringens oder der Inbetriebnahme aufzubewahren. Marktüberwachungsbehörden müssen auf Anfrage Zugang erhalten.

## Verbindung zum Evidence-Pack

Wenn nicht nur die Erklärung, sondern eine druckreife Konformitätsbescheinigung, ein Art.-43-Nachweis, ein Evidence Index und eine Lückenliste gebraucht werden, nutze `output-konformitaetsbescheinigung-evidence-pack`. Dieser Skill verhindert, dass eine interne Readiness-Bewertung fälschlich als finale Konformität oder als Bescheinigung einer notifizierten Stelle ausgegeben wird.

## Aktualisierung

Die Erklärung ist zu aktualisieren, wenn:
- Das KI-System wesentlich verändert wurde
- Neue harmonisierte Normen auf das System angewendet werden
- Die Bescheinigung der benannten Stelle erneuert wurde

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
PRUEFERGEBNIS — OUTPUT KONFORMITAETSERKLAERUNG EU ANHANG V
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Anhang V Rn. 2]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
