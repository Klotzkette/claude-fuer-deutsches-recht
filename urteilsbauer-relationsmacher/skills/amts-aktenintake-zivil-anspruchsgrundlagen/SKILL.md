---
name: amts-aktenintake-zivil-anspruchsgrundlagen
description: "Amts Aktenintake Zivil Anspruchsgrundlagen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Amts Aktenintake Zivil Anspruchsgrundlagen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Amts Aktenintake Zivil Anspruchsgrundlagen** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-amts-fristen-form-und-zustaendigkeit` | Amts: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `aktenintake-zivil` | Eingehende Zivilakte vor erster Prüfung strukturieren: Richter oder Referendar erhalt neue Akte und muss Überblick gewinnen. Normen: § 313 ZPO (Urteilsinhalt), § 286 ZPO (freie Beweiswürdigung), § 139 ZPO (richterliche Hinweispflicht). Prüfraster: Klagschrift mit Anträgen, Streitwert, Sachvortrag, Beweisangebote, Anlagen, Zustellung, Klageerwiderung, Replik, Beweisbeschluss, Protokolle, Gutachten. Output Aktenuebersicht-Tabelle, Prüfliste Hinweispflichten, Schnittstelle zur Relation. Abgrenzung: Detailprüfung Zulässigkeit siehe zulässigkeit-prüfen; Relationserstattung siehe relation-zivil. |
| `anspruchsgrundlagen-pruefen` | Anspruchsgrundlagen identifizieren und Prüfungsreihenfolge bestimmen: Richter oder Kandidat muss Anspruchskonkurrenz lösen. Normen: §§ 433 ff., 280 ff., 812 ff., 823 ff. BGB; HGB; CISG; GmbHG; StVG; ProdHG; IPR Rom-I/II. Prüfraster: Reihenfolge vertraglich, quasi-vertraglich, dinglich, deliktisch, bereicherungsrechtlich; Tatbestandsmerkmale, Rechtsfolge, Einwendungen, Einreden, Verjährung. Output Anspruchsgrundlagen-Baum mit Prüfungsschema. Abgrenzung: CISG-spezifisch siehe cisg-prüfen; IPR siehe internationales-privatrecht; Tenorierung siehe tenor-bauen-zivil. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Amts Aktenintake Zivil Anspruchsgrundlagen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-amts-fristen-form-und-zustaendigkeit`

**Fokus:** Amts: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Amts: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Amts: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Amts: Fristen, Form, Zuständigkeit und Rechtsweg / amts fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DOCX und PDF sind Dateiformate, keine Rechtsquellen. Je nach Modul ZPO §§ 313 (Tatbestand/Entscheidungsgründe), 308, 322 (Tenor und Rechtskraft), 139 (richterlicher Hinweis), 78a (Rechtspfleger), 495a (vereinfachtes Verfahren), 511 ff. (Berufung) sowie GVG §§ 23, 71 (Zuständigkeit AG/LG), Aktenordnung des Landes und einschlägiges materielles Recht live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Amts** prüfen.
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

## 2. `aktenintake-zivil`

**Fokus:** Eingehende Zivilakte vor erster Prüfung strukturieren: Richter oder Referendar erhalt neue Akte und muss Überblick gewinnen. Normen: § 313 ZPO (Urteilsinhalt), § 286 ZPO (freie Beweiswürdigung), § 139 ZPO (richterliche Hinweispflicht). Prüfraster: Klagschrift mit Anträgen, Streitwert, Sachvortrag, Beweisangebote, Anlagen, Zustellung, Klageerwiderung, Replik, Beweisbeschluss, Protokolle, Gutachten. Output Aktenuebersicht-Tabelle, Prüfliste Hinweispflichten, Schnittstelle zur Relation. Abgrenzung: Detailprüfung Zulässigkeit siehe zulässigkeit-prüfen; Relationserstattung siehe relation-zivil.

# Aktenintake Zivilprozess


## Triage zu Beginn

1. Welche Schriftsätze liegen vor — Klagschrift, Klageerwiderung, Replik, Duplik, Nachreichungen?
2. Ist der Streitwert plausibel (Paragraf 3 ZPO, Anlage 1 GKG)? Sachliche Zuständigkeit AG oder LG?
3. Gibt es Beweisbeschlüsse oder Protokolle früherer Verhandlungen?
4. Liegen Sachverständigengutachten oder Zeugenaussagen vor, die auszuwerten sind?
5. Sind Erledigungserklärungen, Widerklagen oder Aufrechnung im Akt?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 139 ZPO — richterliche Hinweis- und Aufklärungspflicht
- § 296 ZPO — Zurückweisung verspäteten Vorbringens
- § 313 ZPO — Form und Inhalt des Urteils
- § 358 ff. ZPO — Beweisbeschluss und Beweisaufnahme
- § 286 ZPO — freie Beweiswürdigung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
| Nr. | Datum | Stueck | Verfasser | Bezugnahme | Bewertung |
| --- | --------- | ------------------------------- | ------------- | ---------- | --------- |
| 1 | 01.03.2025| Klagschrift | RA Mueller | - | schluessig vorgetragen |
| 2 | 01.03.2025| Anlagen K1-K5 | RA Mueller | KS S. 3-7 | Lesbar, vollstaendig |
| 3 | 12.03.2025| EB Zustellung Klagschrift | - | - | Zustellung 10.03.2025 |
| 4 | 31.03.2025| Klageerwiderung mit Widerklage | RA Schmidt | KS S.2 | Substanziiert; Widerklage zulaessig |
| 5 | 14.04.2025| Replik | RA Mueller | KE S.4-6 | neue Tatsache S.3 -> Paragraf 296 ZPO pruefen |
| 6 | 15.05.2025| Hinweisbeschluss Paragraf 139 | Gericht | - | Hinweis zur Substanziierung der Hoehe |
| 7 | 14.06.2025| Schriftsatznachreichung Klaeger | RA Mueller | HinwB | Hinweise befolgt; Frist gewahrt |
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
4. **Hilfsanträge nicht erkannt.** "Hilfsweise" wird leicht überlesen, führt zu unvollständigem Tenor.
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

## 3. `anspruchsgrundlagen-pruefen`

**Fokus:** Anspruchsgrundlagen identifizieren und Prüfungsreihenfolge bestimmen: Richter oder Kandidat muss Anspruchskonkurrenz lösen. Normen: §§ 433 ff., 280 ff., 812 ff., 823 ff. BGB; HGB; CISG; GmbHG; StVG; ProdHG; IPR Rom-I/II. Prüfraster: Reihenfolge vertraglich, quasi-vertraglich, dinglich, deliktisch, bereicherungsrechtlich; Tatbestandsmerkmale, Rechtsfolge, Einwendungen, Einreden, Verjährung. Output Anspruchsgrundlagen-Baum mit Prüfungsschema. Abgrenzung: CISG-spezifisch siehe cisg-prüfen; IPR siehe internationales-privatrecht; Tenorierung siehe tenor-bauen-zivil.

# Anspruchsgrundlagen-Prüfung

Identifiziert alle in Betracht kommenden Anspruchsgrundlagen und prüft sie schemamaessig.


## Triage zu Beginn

1. Welches Schuldverhältnis liegt zugrunde — Vertrag, Gesetz, Bereicherung, Delikt?
2. Besteht Auslandsbezug — Rom-I, Rom-II, CISG anwendbar?
3. Welche Partei trägt die Beweislast für die streitigsten Tatbestandsmerkmale?
4. Droht Verjährung (§§ 195, 199 BGB — regelmäßig 3 Jahre ab Jahresende Kenntnis)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 195, 199 BGB — Verjährung (regelmäßig 3 Jahre, Beginn mit Schluss des Jahres der Kenntnis)
- § 280 BGB — Schadensersatz wegen Pflichtverletzung
- § 812 BGB — ungerechtfertigte Bereicherung
- § 823 BGB — deliktische Haftung
- § 985, 1004 BGB — dingliche Ansprüche
- Art. 1 ff. Rom-I, Art. 4 ff. Rom-II — IPR-Kollisionsrecht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Sachverhalt scannen:** Welche Parteien, welche Rechtsbeziehung, welches Ziel des Klägers?
2. **Anspruchsgrundlagen auflisten:** alle in Betracht kommenden in der Reihenfolge: vertraglich → quasivertraglich → dinglich → deliktisch → bereicherungsrechtlich.
3. **Für jede AG Prüfschema:** Anwendbarkeit → Tatbestandsmerkmale (mit Beweislastverteilung) → Rechtsfolge → Einwendungen/Einreden → Verjährung.
4. **IPR prüfen:** Falls Auslandsbezug, erst Kollisionsrecht klären, dann CISG prüfen.
5. **Konkurrenzfragen:** Wenn mehrere AG durchgreifen, Günstigkeitsprinzip anwenden.

## Output-Template

**Adressat:** Richter/Berichterstatter — Tonfall: sachlich-juristisch

```
## Anspruchsgrundlagen-Übersicht

| Anspruchsgrundlage | Ergebnis | Hauptproblem |
|---|---|---|
| § 433 I BGB (Kaufpreis) | (+) | — |
| § 823 I BGB (Körperverletzung) | prüfen | Kausalität str. |
| § 812 I 1 BGB (Bereicherung) | (-) | Rechtsgrund vorhanden |

### 1. § [AG] [Norm]
- **Tatbestandsmerkmale:** ...
- **Beweislast Kläger:** ...
- **Einwendungen Beklagter:** ...
- **Verjährung:** 3 Jahre ab [DATUM], läuft am [DATUM] ab.
- **Ergebnis:** Anspruch besteht / besteht nicht.
```

## Reihenfolge

1. **Vertraglich** (Paragraf 433 BGB, Paragraf 535 BGB, Paragraf 631 BGB usw. - CISG bei internationalem Warenkauf)
2. **Quasivertraglich** (Paragraf 311 II BGB - culpa in contrahendo, Paragraf 280 BGB)
3. **Dinglich** (Paragraf 985 BGB, Paragraf 1004 BGB)
4. **Deliktisch** (Paragraf 823 ff BGB, Paragraf 7 StVG, ProdHG)
5. **Bereicherungsrechtlich** (Paragraf 812 ff BGB)
6. **Familien- / erbrechtlich** soweit einschlaegig

## Pruefschema für jede Anspruchsgrundlage

1. Anwendbarkeit (sachlich, persönlich, raeumlich, zeitlich)
2. Tatbestandsmerkmale - bei jedem: Wer hat die Beweislast?
3. Rechtsfolge
4. Einwendungen (rechtshindernd, rechtsvernichtend)
5. Einreden (durchsetzbarkeitshemmend)
6. Verjaehrung (Paragraf 195 BGB, Paragraf 199 BGB, Paragraf 438 BGB usw.)

## IPR

Bei Auslandsbezug immer prüfen:
- Rom-I-Verordnung (vertragliche Schuldverhältnisse)
- Rom-II-Verordnung (außervertragliche Schuldverhältnisse)
- CISG (Wiener UN-Kaufrecht) als materielles Einheitsrecht - geht IPR vor, soweit sachlicher Anwendungsbereich eroeffnet
- Eingriffsnormen Artikel 9 Rom-I (Pflichtanwendung deutscher Vorschriften, z. B. DSGVO als Eingriffsnorm)

## Ausgabe

Pro Anspruchsgrundlage eine eigene Tabelle mit allen Tatbestandsmerkmalen.

<!-- AUDIT 27.05.2026
Geprüfte AZ (task_286):
- BGH VI ZR 373/18 (behauptet NJW 2020, 466): NOT FOUND auf dejure.org — ersetzt durch BGH VII ZR 158/03, NJW 2005, 1423 (verifiziert auf dejure.org)
- BGH VI ZR 395/16 (behauptet NJW 2018, 386): NOT FOUND auf dejure.org — ersetzt durch BGH VI ZR 107/08, NJW 2009, 2952 (verifiziert auf dejure.org)
- BGH VII ZR 101/14 (behauptet NJW 2016, 560): NOT FOUND auf dejure.org — ersetzt durch BGH VII ZR 184/04, NJW 2005, 1356 (verifiziert auf dejure.org)
Alle drei Ersatz-AZ wurden über dejure.org-Direktabfrage verifiziert.
-->
