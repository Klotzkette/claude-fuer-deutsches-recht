---
name: speditionsrecht-tio-schiedsgericht
description: "TIO Schiedsgericht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TIO Schiedsgericht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **TIO Schiedsgericht** im Plugin Fachanwalt Transport- und Speditionsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-speditionsrecht-fristen-form-und-zustaendigkeit` | Speditionsrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt transport speditionsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `fachanwalt-transport-tio-schiedsgericht-adsp-klauseln` | TIO-Schiedsgerichtsklauseln und ADSP-Bedingungen im Transport- und Speditionsrecht prüfen. Normen: ADSP 2017, §§ 1025 ff. ZPO. Prüfraster: Schiedsklausel-Wirksamkeit, AGB-Kontrolle, TIO-Schiedsprozess. Output: Klauselprüfung ADSP. Abgrenzung: nicht staatliches Gerichtsverfahren. |
| `spezial-frachtvertrag-risikoampel-und-gegenargumente` | Frachtvertrag: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin fachanwalt transport speditionsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Fachanwalt Transport- und Speditionsrecht gilt für **TIO Schiedsgericht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-speditionsrecht-fristen-form-und-zustaendigkeit`

**Fokus:** Speditionsrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt transport speditionsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Speditionsrecht: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Speditionsrecht: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Speditionsrecht: Fristen, Form, Zuständigkeit und Rechtsweg / speditionsrecht fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** HGB, CMR, COTIF, HG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Speditionsrecht** prüfen.
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

## 2. `fachanwalt-transport-tio-schiedsgericht-adsp-klauseln`

**Fokus:** TIO-Schiedsgerichtsklauseln und ADSP-Bedingungen im Transport- und Speditionsrecht prüfen. Normen: ADSP 2017, §§ 1025 ff. ZPO. Prüfraster: Schiedsklausel-Wirksamkeit, AGB-Kontrolle, TIO-Schiedsprozess. Output: Klauselprüfung ADSP. Abgrenzung: nicht staatliches Gerichtsverfahren.

# Transport-Recht — TIO / ADSp-Schiedsklauseln

## Zweck

Transport-/Spediteursstreit hat branchen-typische Schlichtungs- und Schiedsverfahren: **ADSp § 21** Schiedsklausel, **TIO** Transport Industry Tribunal, **DGI**-Branchen-Schlichtungsstelle, **CMR**-Vergleichs-Korrespondenz mit Versicherern.

## Eingaben

- Vertragstyp (Speditionsvertrag § 453 HGB, Frachtvertrag § 407 HGB, Lagervertrag)
- Anwendbares Recht (HGB, ADSp 2017 — Stand Mai 2026 weiterhin geltende Branchenfassung —, CMR, COTIF, Montreal)
- Streitgegenstand (Frachtschaden, Verlust, Lieferverzug, Spedition-Versäumnis)
- Versicherer-Beteiligung (CMR-Vers., Speditions-Vers.)
- Streitwert

## Rechtlicher Rahmen

- **§§ 407-475h HGB** — Frachtvertrag / Spedition
- **CMR-Übereinkommen** (Internationale Straße)
- **Montrealer Übereinkommen** (Luftfracht)
- **Haager-Visby-Regeln** (Seefracht)
- **COTIF** (Schiene)
- **ADSp 2017** — Stand Mai 2026 weiterhin Branchenstandard (keine konsolidierte Folgefassung verifiziert); zukünftige Anpassungen über [dslv.org](https://www.dslv.org/de/adsp) prüfen
- **§ 21 ADSp** — Schiedsklausel TIO
- **§ 1029 ff. ZPO**

## ADR-Pfade

### Pfad 1 — TIO (Transport Industry Tribunal Hamburg)

- ADSp § 21 Schiedsklausel
- Spezialisierte Schiedsrichter
- Streitwerte > 50.000 EUR
- Verfahrens-Dauer 12-18 Monate

### Pfad 2 — DGI-Schlichtungsstelle

- DSLV-Schlichtungsstelle für Spediteure
- Niedrigschwellig
- Bei Spediteur-Mitgliedschaft

### Pfad 3 — CMR-Versicherer-Verhandlung

- Bei internationalen Straßenstückgut
- 8,33 SZR/kg Höchstbetrag Art. 23 III CMR
- Direkter Versicherer-Kontakt

### Pfad 4 — Klage HG-Spezialkammer

- LG-Kammer für Handelssachen
- Bei TIO-Klausel ausgeschlossen

### Pfad 5 — ICC bei internationalen Verfahren

- Containerladung, Hafenstreit
- Bei mehrländrigem Streit

## Workflow

### Phase 1 — Schadensanzeige

- 7-Tage-Frist Anzeige Frachtführer (§ 438 HGB)
- Bei CMR: 21 Tage bei nicht-erkennbaren Schaden
- Foto-/Doku am Empfangsort

### Phase 2 — Versicherer-Korrespondenz

- Schadensformular
- Beweise (Gutachten, Lieferschein, AVB)
- Verhandlungs-Bereitschaft signalisieren

### Phase 3 — ADR-Wahl

- Bei ADSp-Klausel: TIO
- Sonst: LG-Kammer / Vergleich

### Phase 4 — Verfahren

- Schiedsverfahren-Eröffnung
- Beweisaufnahme (Sachverständige)
- Schiedsspruch

### Phase 5 — Vollstreckung

- Schiedsspruch vollstreckbar
- Bei Auslands: New Yorker Übereinkommen

## Strategie und Taktik

- **8,33 SZR/kg Cap** — bei wertvoller Ware Sondervereinbarung § 449 HGB
- **Bei Vorsatz / grober Fahrlässigkeit**: § 435 HGB; volle Haftung
- **CMR-Frist 21 Tage** kurz; sofort handeln
- **Mehrere Beteiligte**: Frachtführer + Subunternehmer + Versicherer
- **ADSp-Aktualität**: Stand 05/2026 ist die ADSp 2017 maßgeblich. Eine konsolidierte Folgefassung ist im Skill-Recherche-Stand nicht verifiziert. Im Mandat aktuellen Stand über DSLV/BGL prüfen.

## Querverweise

- `fachanwalt-transport-speditionsrecht-orientierung` — Triage
- `fachanwalt-transport-cmr-schadensregulierung` — CMR
- `fachanwalt-transport-speditionshaftung-hgb` — Speditions
- `fachanwalt-transport-autonome-lkw-konvois-haftung-1d-stvg` — Spezialfall

## Quellen und Updates

Stand: 05/2026. ADSp 2017 weiterhin als Branchenstandard. CMR 1956. Montrealer Übereinkommen 1999. Rechtsprechung im Mandat live verifizieren.

- ADSp 2017 — [dslv.org](https://www.dslv.org/de/adsp)
- CMR (UNECE) — [unece.org](https://unece.org/transport/standards/transport/road)
- HGB §§ 407 ff. — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/)
- BGH I. Zivilsenat (Transport) — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)

## 3. `spezial-frachtvertrag-risikoampel-und-gegenargumente`

**Fokus:** Frachtvertrag: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin fachanwalt transport speditionsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Frachtvertrag: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Frachtvertrag: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Frachtvertrag: Risikoampel, Gegenargumente und Verteidigungslinien / frachtvertrag risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** HGB, CMR, COTIF.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Frachtvertrag** prüfen.
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
