---
name: aktenintake-zivil
description: "Strukturiert eine eingehende Zivilakte vor der ersten Pruefung: Klagschrift mit Antraegen Streitwert Sachvortrag Beweisangeboten Anlagen Zustellnachweis Klageerwiderung Replik Duplik Schriftsatznachreichungen Beweisbeschluss Protokolle muendliche Verhandlung Sachverstaendigengutachten Zeugenaussagen. Erstellt Aktenuebersicht mit Datum Verfasser Inhalt Bezugnahmen Bewertung. Mit Tabellen-Template Pruefliste fuer Hinweispflichten Schnittstelle zur Relation."
---

# Aktenintake Zivilprozess

## Zweck

Erster, systematischer Pruefschritt nach dem Eingang einer neuen Sache — sei es bei Aktenzuteilung an einen Berichterstatter, beim Wechsel des zustaendigen Richters oder bei der Vorbereitung einer Beweisaufnahme. Ziel ist eine **vollstaendige Aktenuebersicht**, die in der nachfolgenden Relation und in den prozessleitenden Massnahmen (Paragraf 139 ZPO Hinweise, Beweisbeschluss, Vergleichsvorschlag) tragfaehig ist.

## 1) Bestandteile einer typischen Zivilakte

| Stueck | Standardinhalte | Worauf zu achten |
|---|---|---|
| Klagschrift | Antrag, Streitwert, Sachvortrag, Beweisangebot, Anlagen | Antrag bestimmt? Streitwert plausibel? Beweisangebot zu jedem streitigen Tatsachenkomplex? |
| Anlagenkonvolut Klaeger | K1, K2, ... | Vollstaendigkeit, Lesbarkeit, Bezugnahme im Schriftsatz |
| Zustellnachweis | EB, PZU | Datum, Form (elektronisch beA Paragraf 173 ZPO?), Empfangsbevollmaechtigter |
| PKH-Antrag | mit Erklaerung Paragraf 117 ZPO + Belegen | Vollstaendigkeit, eidesstattliche Versicherung |
| Klageerwiderung | Klagabweisungsantrag, Sachvortrag, ggf. Widerklage | Substanziierung der Bestreitungen Paragraf 138 II ZPO |
| Anlagenkonvolut Beklagter | B1, B2, ... | wie Klaeger |
| Replik | Erwiderung auf Klageerwiderung | neue Tatsachen vs. Vertiefung |
| Duplik | Erwiderung auf Replik | dito |
| Schriftsatznachreichungen | Schriftsatznachlass Paragraf 283 ZPO | Frist gewahrt? Bezug klar? |
| Beweisbeschluesse | nach Paragraf 358 ZPO | Beweisthema klar, Beweismittel benannt |
| Protokolle | Paragraf 159 ZPO | Anwesenheit, Antraege, Aussagen, Vergleichsvorschlaege |
| Sachverstaendigengutachten | mit Beweisthema | Pruefen: Aussagekraft, Ergaenzungsbedarf Paragraf 411 ZPO |
| Zeugenaussagen | als Protokollteil oder gesondert | Verwertbarkeit, Aussagekonstanz |
| Hinweisbeschluesse | Paragraf 139 ZPO | wurden Hinweise befolgt? |

## 2) Vorgehen Schritt-fuer-Schritt

1. **Aktenstruktur sichten.** Welche Schriftsaetze liegen vor? Vollstaendigkeit (auch beA-Empfangsbestaetigungen) pruefen.
2. **Klagschrift lesen.** Antrag, Streitwert, Anspruchsgrundlage. Bei Mehrheit von Antraegen: Stufenklage? Eventualantrag? Teilklage?
3. **Sachvortrag herausarbeiten.** Streitige Tatsachen vs. unstreitige Tatsachen. Beweisangebot zu jeder streitigen Tatsache?
4. **Anlagen abgleichen.** Bezugnahmen in den Schriftsaetzen mit dem Anlagen-Konvolut abgleichen. Bei Anlagen mit Inhaltsreichweite — kurz inhaltlich erfassen.
5. **Beklagtenvortrag lesen.** Was ist bestritten? Was ist anerkannt (Paragraf 288 ZPO)? Gibt es Widerklage / Aufrechnung?
6. **Replik und Folgeschriftsaetze lesen.** Welche neuen Tatsachen sind eingefuehrt worden (Praeklusion Paragraf 296 ZPO)?
7. **Beschluesse und Protokolle in zeitlicher Reihenfolge.** Was hat das Gericht bereits angeordnet? Was wurde befolgt?
8. **Gutachten/Aussagen.** Hat das Gericht bereits Beweis erhoben? Mit welchem Ergebnis?
9. **Hinweis- und Aufklaerungsbedarf.** Was muss nach Paragraf 139 ZPO erfragt werden? Substanziierung? Beweisangebot?

## 3) Aktenuebersicht — Tabellen-Template

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

## 4) Pruefliste fuer gerichtliche Pflichten

### Substanziierung
- [ ] Klage schluessig? (Anspruchsgrundlage vorgetragen, Tatbestandsmerkmale dargelegt)
- [ ] Bei Bestreiten: Substanziierung des Bestreitens Paragraf 138 II ZPO?
- [ ] Hinweispflicht Paragraf 139 II ZPO bei rechtlich relevantem Aspekt?

### Praeklusion
- [ ] Neuvortrag nach Schluss der muendlichen Verhandlung Paragraf 296a ZPO?
- [ ] Verspaeteter Vortrag im Vorverfahren Paragraf 296 ZPO?
- [ ] Bei Berufung: Paragraf 531 ZPO Praeklusion?

### Beweisangebot
- [ ] Beweisantritt zu jeder streitigen Tatsache?
- [ ] Konkretes Beweismittel (Zeuge mit Anschrift, Urkunde mit Bezeichnung, Sachverstaendiger mit Beweisthema)?
- [ ] Beweisbeschluss bereits ergangen oder noch erforderlich?

### Verfahrensfragen
- [ ] Zustaendigkeit (Paragraf 1 GVG, Paragraf 23, 71 GVG bei AG/LG)?
- [ ] Sachliche und oertliche Zustaendigkeit?
- [ ] Postulationsfaehigkeit Paragraf 78 ZPO?
- [ ] Prozessfaehigkeit Paragraf 51 ZPO?

## 5) Ergebnis des Intakes

Am Ende des Aktenintakes liegt vor:

1. **Aktenuebersicht** als Tabelle (siehe oben).
2. **Liste der unstreitigen Tatsachen** — gut fuer den Tatbestand.
3. **Liste der streitigen Tatsachen** mit Beweisangeboten — gut fuer den Beweisbeschluss.
4. **Liste der Rechtsfragen**, die im Streit stehen — gut fuer die Entscheidungsgruende.
5. **Liste offener Hinweisfragen** Paragraf 139 ZPO — gut fuer den naechsten Hinweisbeschluss.
6. **Streitwert-Vorschlag** mit Begruendung.
7. **Vergleichschancen-Bewertung** (Indizien: hoher Streitwert + ueberschaubare Beweisfrage + Vergleichsoffenheit der Parteien).

## 6) Schnittstelle zu nachfolgenden Skills

- `relation-zivil` baut auf der Aktenuebersicht und der Trennung streitig/unstreitig auf.
- `tenor-bauen-zivil` braucht den Antrag aus der Klagschrift und etwaige Widerklage/Hilfsantraege.
- `tatbestand-zivil-schreiben` uebernimmt die Liste der unstreitigen Tatsachen.
- `beschluss-bauen-zpo` braucht die offenen Hinweisfragen (fuer den Paragraf 139-Beschluss) und das Beweisthema (fuer den Beweisbeschluss).

## 7) Typische Fehler beim Intake

1. **Anlagen nicht abgeglichen.** Bezugnahmen im Schriftsatz auf Anlagen, die fehlen oder anders nummeriert sind. Klassischer Stolperstein.
2. **Bezugnahmen ueberlesen.** Spaeterer Schriftsatz nimmt auf einen frueheren Bezug — der dann inhaltlich uebersehen wird.
3. **Erledigungserklaerungen uebersehen.** Teilrelative Erledigung in einem Schriftsatz versteckt — fuehrt zu Mehrarbeit beim Tenor.
4. **Hilfsantraege nicht erkannt.** „Hilfsweise" wird leicht ueberlesen, fuehrt zu unvollstaendigem Tenor.
5. **Mahnverfahrens-Stand uebersehen.** Bei Eingang nach Widerspruch ist der Mahnantrag inhaltlich die Klagschrift (Paragraf 696 ZPO).
6. **Zustellnachweis falsch interpretiert.** Bei beA-Zustellung ist die Empfangsbestaetigung des Empfaengers massgeblich.
7. **Vergleichsvorschlaege als Schriftsaetze gewertet.** Vergleichsvorschlag Paragraf 278 VI ZPO ist Gerichts-Aktivitaet, nicht Parteivortrag.

## 8) Praktischer Ablauf

Als Berichterstatter:
- 30-90 Minuten je nach Aktenumfang einplanen
- Aktenuebersicht in einem Editor (Markdown / Excel) anlegen
- Bei sehr grossen Akten: Personen-/Rollen-Glossar zusaetzlich
- Bei sehr alten Akten: Chronologie der Eingaenge pruefen (Praeklusion?)

## Anschluss

- `relation-zivil` baut auf der Aktenuebersicht auf
- `tatbestand-zivil-schreiben` uebernimmt unstreitige Tatsachen
- `beschluss-bauen-zpo` bei Hinweisbedarf oder Beweisbeschluss
