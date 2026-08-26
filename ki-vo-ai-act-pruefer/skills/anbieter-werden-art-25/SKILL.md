---
name: anbieter-werden-art-25
description: "Für Anbieter-Werden — Art. 25 europäischer Technikregulierungsrahmen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anbieter-Werden — Art. 25 KI-VO

## Vier Fallgruppen (Art. 25 Abs. 1 KI-VO)

### Fallgruppe 1 — Inverkehrbringen unter eigenem Namen oder eigener Marke

Wer ein Hochrisiko-KI-System oder GPAI-Modell unter seinem eigenen Namen oder seiner eigenen Marke in Verkehr bringt, wird Anbieter — unabhängig davon, ob er das System selbst entwickelt hat.

**Prüffragen:**
- Bringen Sie ein fremdes KI-System unter Ihrem eigenen Namen oder Ihrer Marke auf den Markt?
- Erscheint der ursprüngliche Anbieter im Vertrag, in der Dokumentation oder gegenüber dem Endkunden noch sichtbar?

**Wenn ja zum ersten, nein zum zweiten:** → Sie werden Anbieter nach Art. 25 Abs. 1 lit. a KI-VO.

**Konsequenz:** Sie müssen alle Anbieter-Pflichten nach Art. 16 bis 42 KI-VO erfüllen, einschließlich Konformitätsbewertung, CE-Kennzeichnung, EU-Konformitätserklärung und Registrierung in der EU-Datenbank.

### Fallgruppe 2 — Wesentliche Änderung nach dem Inverkehrbringen

Ein Betreiber oder Händler, der ein bereits in Verkehr gebrachtes Hochrisiko-KI-System wesentlich verändert, wird Anbieter.

**Was ist eine wesentliche Änderung?**

Nach Art. 3 Nr. 23 KI-VO ist eine wesentliche Änderung eine Änderung des KI-Systems nach seinem Inverkehrbringen, die die Konformität des Systems mit den Anforderungen beeinflussen kann oder die dazu führt, dass sich der Verwendungszweck, für den das KI-System bewertet wurde, verändert.

**Beispiele für wesentliche Änderungen:**
- Erneutes Training des Modells mit neuen Daten
- Änderung der Modellarchitektur
- Anpassung der Ausgaben des Systems in einer Weise, die neue Entscheidungen ermöglicht
- Erweiterung des Einsatzbereichs auf neue Nutzergruppen oder neue Entscheidungstypen
- Konfiguration, die zu einer Änderung der Systemfunktionalität führt

**Prüffragen:**
- Haben Sie technische Änderungen am System vorgenommen (Code, Modell, Parameter)?
- Haben Sie den Einsatzbereich oder die Zielgruppe verändert?
- Haben Sie Konfigurationen vorgenommen, die über die vom Anbieter vorgesehenen Optionen hinausgehen?

### Fallgruppe 3 — Änderung des bestimmungsgemäßen Verwendungszwecks

Wer das KI-System für einen anderen als den ursprünglich vorgesehenen Zweck einsetzt, wird Anbieter — auch ohne technische Änderung.

**Beispiele:**
- Ein Personalverwaltungs-Tool wird für die Bonitätsprüfung genutzt
- Ein Bildklassifikationssystem für die Qualitätskontrolle wird für die Gesichtserkennung genutzt
- Ein Text-Zusammenfassungstool wird für automatisierte Rechtsentscheidungen genutzt

**Prüffragen:**
- Ist der tatsächliche Einsatzzweck identisch mit dem in der Gebrauchsanweisung des Anbieters beschriebenen Zweck?
- Haben Sie das System für Entscheidungen genutzt, die der Anbieter nicht vorgesehen hat?

### Fallgruppe 4 — Produkthersteller (Art. 25 Abs. 1 lit. c KI-VO)

Ein Hersteller eines Produkts, das ein Hochrisiko-KI-System als Sicherheitsbauteil enthält, wird Anbieter des Hochrisiko-KI-Systems, wenn er das Produkt unter seinem eigenen Namen in Verkehr bringt.

→ Details: `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

## Informationspflicht des ursprünglichen Anbieters (Art. 25 Abs. 2 KI-VO)

Der ursprüngliche Anbieter muss dem neuen Anbieter (nach Art. 25) alle notwendigen Informationen bereitstellen, damit dieser seine Anbieter-Pflichten erfüllen kann. Dies ist vertraglich zu regeln.

## Praktische Empfehlung

Vor jeder Anpassung oder Umwidmung eines KI-Systems sollte geprüft werden:
1. Überschreitet die Maßnahme die Schwelle zur wesentlichen Änderung?
2. Liegt eine Zweckänderung vor?
3. Wenn ja: Welche Anbieter-Pflichten müssen erfüllt werden?
4. Sind die entsprechenden Ressourcen (technische Dokumentation, Konformitätsbewertung) vorhanden?

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

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
5. Ist die Maßnahme nach aktuellem Art. 113- und Digital-Omnibus-Zeitstrahl fristgerecht umgesetzt?

## Output-Template — Prüfergebnis
**Adressat:** Prüfer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — ANBIETER WERDEN ART 25
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 25 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
