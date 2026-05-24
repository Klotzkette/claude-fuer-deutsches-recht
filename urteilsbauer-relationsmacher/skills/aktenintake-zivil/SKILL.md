---
name: aktenintake-zivil
description: "Strukturiert eine eingehende Zivilakte vor der ersten Pruefung: Klagschrift mit Antraegen Streitwert Sachvortrag Beweisangeboten Anlagen Zustellnachweis Klageerwiderung Replik Duplik Schriftsatznachreichungen Beweisbeschluss Protokolle muendliche Verhandlung Sachverstaendigengutachten Zeugenaussagen. Erstellt Aktenuebersicht mit Datum Verfasser Inhalt Bezugnahmen Bewertung. Mit Tabellen-Template Pruefliste fuer Hinweispflichten Schnittstelle zur Relation."
---

# Aktenintake Zivilprozess

## Zweck

Erster, systematischer Pruefschritt nach dem Eingang einer neuen Sache — sei es bei Aktenzuteilung an einen Berichterstatter, beim Wechsel des zuständigen Richters oder bei der Vorbereitung einer Beweisaufnahme. Ziel ist eine **vollständige Aktenübersicht**, die in der nachfolgenden Relation und in den prozessleitenden Maßnahmen (Paragraf 139 ZPO Hinweise, Beweisbeschluss, Vergleichsvorschlag) tragfähig ist.

## 1) Bestandteile einer typischen Zivilakte

| Stück | Standardinhalte | Worauf zu achten |
|---|---|---|
| Klagschrift | Antrag, Streitwert, Sachvortrag, Beweisangebot, Anlagen | Antrag bestimmt? Streitwert plausibel? Beweisangebot zu jedem streitigen Tatsachenkomplex? |
| Anlagenkonvolut Kläger | K1, K2, ... | Vollständigkeit, Lesbarkeit, Bezugnahme im Schriftsatz |
| Zustellnachweis | EB, PZU | Datum, Form (elektronisch beA Paragraf 173 ZPO?), Empfangsbevollmaechtigter |
| PKH-Antrag | mit Erklärung Paragraf 117 ZPO + Belegen | Vollständigkeit, eidesstattliche Versicherung |
| Klageerwiderung | Klagabweisungsantrag, Sachvortrag, ggf. Widerklage | Substanziierung der Bestreitungen Paragraf 138 II ZPO |
| Anlagenkonvolut Beklagter | B1, B2, ... | wie Kläger |
| Replik | Erwiderung auf Klageerwiderung | neue Tatsachen vs. Vertiefung |
| Duplik | Erwiderung auf Replik | dito |
| Schriftsatznachreichungen | Schriftsatznachlass Paragraf 283 ZPO | Frist gewahrt? Bezug klar? |
| Beweisbeschlüsse | nach Paragraf 358 ZPO | Beweisthema klar, Beweismittel benannt |
| Protokolle | Paragraf 159 ZPO | Anwesenheit, Anträge, Aussagen, Vergleichsvorschlaege |
| Sachverständigengutachten | mit Beweisthema | Prüfen: Aussagekraft, Ergänzungsbedarf Paragraf 411 ZPO |
| Zeugenaussagen | als Protokollteil oder gesondert | Verwertbarkeit, Aussagekonstanz |
| Hinweisbeschlüsse | Paragraf 139 ZPO | wurden Hinweise befolgt? |

## 2) Vorgehen Schritt-für-Schritt

1. **Aktenstruktur sichten.** Welche Schriftsätze liegen vor? Vollständigkeit (auch beA-Empfangsbestätigungen) prüfen.
2. **Klagschrift lesen.** Antrag, Streitwert, Anspruchsgrundlage. Bei Mehrheit von Anträgen: Stufenklage? Eventualantrag? Teilklage?
3. **Sachvortrag herausarbeiten.** Streitige Tatsachen vs. unstreitige Tatsachen. Beweisangebot zu jeder streitigen Tatsache?
4. **Anlagen abgleichen.** Bezugnahmen in den Schriftsätzen mit dem Anlagen-Konvolut abgleichen. Bei Anlagen mit Inhaltsreichweite — kurz inhaltlich erfassen.
5. **Beklagtenvortrag lesen.** Was ist bestritten? Was ist anerkannt (Paragraf 288 ZPO)? Gibt es Widerklage / Aufrechnung?
6. **Replik und Folgeschriftsätze lesen.** Welche neuen Tatsachen sind eingeführt worden (Präklusion Paragraf 296 ZPO)?
7. **Beschlüsse und Protokolle in zeitlicher Reihenfolge.** Was hat das Gericht bereits angeordnet? Was wurde befolgt?
8. **Gutachten/Aussagen.** Hat das Gericht bereits Beweis erhoben? Mit welchem Ergebnis?
9. **Hinweis- und Aufklärungsbedarf.** Was muss nach Paragraf 139 ZPO erfragt werden? Substanziierung? Beweisangebot?

## 3) Aktenübersicht — Tabellen-Template

```
| Nr. | Datum     | Stueck                          | Verfasser     | Bezugnahme | Bewertung |
| --- | --------- | ------------------------------- | ------------- | ---------- | --------- |
| 1   | 01.03.2025| Klagschrift                     | RA Mueller    | -          | schluessig vorgetragen |
| 2   | 01.03.2025| Anlagen K1-K5                   | RA Mueller    | KS S. 3-7  | Lesbar, vollstaendig |
| 3   | 12.03.2025| EB Zustellung Klagschrift       | -             | -          | Zustellung 10.03.2025 |
| 4   | 31.03.2025| Klageerwiderung mit Widerklage  | RA Schmidt    | KS S.2     | Substanziiert; Widerklage zulaessig |
| 5   | 14.04.2025| Replik                          | RA Mueller    | KE S.4-6   | neue Tatsache S.3 -> Paragraf 296 ZPO pruefen |
| 6   | 15.05.2025| Hinweisbeschluss Paragraf 139   | Gericht       | -          | Hinweis zur Substanziierung der Hoehe |
| 7   | 14.06.2025| Schriftsatznachreichung Klaeger | RA Mueller    | HinwB      | Hinweise befolgt; Frist gewahrt |
```

## 4) Prüfliste für gerichtliche Pflichten

### Substanziierung
- [ ] Klage schlüssig? (Anspruchsgrundlage vorgetragen, Tatbestandsmerkmale dargelegt)
- [ ] Bei Bestreiten: Substanziierung des Bestreitens Paragraf 138 II ZPO?
- [ ] Hinweispflicht Paragraf 139 II ZPO bei rechtlich relevantem Aspekt?

### Präklusion
- [ ] Neuvortrag nach Schluss der muendlichen Verhandlung Paragraf 296a ZPO?
- [ ] Verspaeteter Vortrag im Vorverfahren Paragraf 296 ZPO?
- [ ] Bei Berufung: Paragraf 531 ZPO Präklusion?

### Beweisangebot
- [ ] Beweisantritt zu jeder streitigen Tatsache?
- [ ] Konkretes Beweismittel (Zeuge mit Anschrift, Urkunde mit Bezeichnung, Sachverständiger mit Beweisthema)?
- [ ] Beweisbeschluss bereits ergangen oder noch erforderlich?

### Verfahrensfragen
- [ ] Zuständigkeit (Paragraf 1 GVG, Paragraf 23, 71 GVG bei AG/LG)?
- [ ] Sachliche und oertliche Zuständigkeit?
- [ ] Postulationsfähigkeit Paragraf 78 ZPO?
- [ ] Prozessfähigkeit Paragraf 51 ZPO?

## 5) Ergebnis des Intakes

Am Ende des Aktenintakes liegt vor:

1. **Aktenübersicht** als Tabelle (siehe oben).
2. **Liste der unstreitigen Tatsachen** — gut für den Tatbestand.
3. **Liste der streitigen Tatsachen** mit Beweisangeboten — gut für den Beweisbeschluss.
4. **Liste der Rechtsfragen**, die im Streit stehen — gut für die Entscheidungsgründe.
5. **Liste offener Hinweisfragen** Paragraf 139 ZPO — gut für den nächsten Hinweisbeschluss.
6. **Streitwert-Vorschlag** mit Begründung.
7. **Vergleichschancen-Bewertung** (Indizien: hoher Streitwert + überschaubare Beweisfrage + Vergleichsoffenheit der Parteien).

## 6) Schnittstelle zu nachfolgenden Skills

- `relation-zivil` baut auf der Aktenübersicht und der Trennung streitig/unstreitig auf.
- `tenor-bauen-zivil` braucht den Antrag aus der Klagschrift und etwaige Widerklage/Hilfsanträge.
- `tatbestand-zivil-schreiben` übernimmt die Liste der unstreitigen Tatsachen.
- `beschluss-bauen-zpo` braucht die offenen Hinweisfragen (für den Paragraf 139-Beschluss) und das Beweisthema (für den Beweisbeschluss).

## 7) Typische Fehler beim Intake

1. **Anlagen nicht abgeglichen.** Bezugnahmen im Schriftsatz auf Anlagen, die fehlen oder anders nummeriert sind. Klassischer Stolperstein.
2. **Bezugnahmen überlesen.** Späterer Schriftsatz nimmt auf einen früheren Bezug — der dann inhaltlich übersehen wird.
3. **Erledigungserklärungen übersehen.** Teilrelative Erledigung in einem Schriftsatz versteckt — führt zu Mehrarbeit beim Tenor.
4. **Hilfsanträge nicht erkannt.** „Hilfsweise" wird leicht überlesen, führt zu unvollständigem Tenor.
5. **Mahnverfahrens-Stand übersehen.** Bei Eingang nach Widerspruch ist der Mahnantrag inhaltlich die Klagschrift (Paragraf 696 ZPO).
6. **Zustellnachweis falsch interpretiert.** Bei beA-Zustellung ist die Empfangsbestätigung des Empfängers massgeblich.
7. **Vergleichsvorschlaege als Schriftsätze gewertet.** Vergleichsvorschlag Paragraf 278 VI ZPO ist Gerichts-Aktivität, nicht Parteivortrag.

## 8) Praktischer Ablauf

Als Berichterstatter:
- 30-90 Minuten je nach Aktenumfang einplanen
- Aktenübersicht in einem Editor (Markdown / Excel) anlegen
- Bei sehr großen Akten: Personen-/Rollen-Glossar zusätzlich
- Bei sehr alten Akten: Chronologie der Eingaenge prüfen (Präklusion?)

## Anschluss

- `relation-zivil` baut auf der Aktenübersicht auf
- `tatbestand-zivil-schreiben` übernimmt unstreitige Tatsachen
- `beschluss-bauen-zpo` bei Hinweisbedarf oder Beweisbeschluss
