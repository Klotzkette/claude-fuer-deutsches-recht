---
name: cas-dis
description: "CAS DIS im Sportrecht: prüft konkret Mandantenkommunikation im Plugin fachanwalt-sportrecht, Red-Team Qualitygate im Plugin fachanwalt-sportrecht, Sportler Verein oder Verband wird in Schiedsverfahren vor. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# CAS DIS

## Arbeitsbereich

**CAS DIS** ordnet den Fall über die tragenden Prüfungslinien: Mandantenkommunikation im Plugin fachanwalt-sportrecht, Red-Team Qualitygate im Plugin fachanwalt-sportrecht, Sportler Verein oder Verband wird in Schiedsverfahren vor. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-sportrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-sportrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `fachanwalt-sportrecht-cas-dis-sport-verbands-schiedsverfahren` | Sportler Verein oder Verband wird in Schiedsverfahren vor CAS DIS oder Verbands-Schiedsgericht involviert. WADA-Code Anti-Doping FIFA Players Status Committee. Normen CAS Code Art. R27 ff. DIS-Sportschiedsgerichtsordnung FIFA RSTP Art. 17. Prüfraster Schiedsklausel-Prüfung Frist-Check Verfahrensart Beweis. Output Schiedsklage-Entwurf Strategie-Memo. Abgrenzung zu cas-berufung-vorbereiten (Berufung) und fachanwalt-sportrecht-doping-verfahren (Doping). |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: WADC Art. 17 Verfolgungsverjährung 10 Jahre, CAS-Anrufung 21 Tage, DFB-RVO 7-Tage-Berufung, FAO § 5 36 Monate Praxiszeit.
- Tragende Normen verifizieren: FAO § 14n (Sportrecht), AntiDopG, NADC, WADC, BGB §§ 25 ff. (Verein), 705 ff., DFB-Satzung/Rechts- und Verfahrensordnung, FIFA-Statuten, CAS-Code, ArbGG (Spielerverträge) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verein, Spieler, Verband (DFB/DFL/DOSB), Bundessportgericht, CAS (Lausanne), NADA, ArbG/LAG, Schiedsgericht.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Spielervertrag, Lizenzantrag, Sportgerichtsentscheidung, Schiedsspruch CAS, Anti-Doping-Protokoll, Verbandsstatut, Transferanmeldung TMS — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-sportrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

### Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin fachanwalt-sportrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-sportrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

### Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin fachanwalt-sportrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `fachanwalt-sportrecht-cas-dis-sport-verbands-schiedsverfahren`

**Fokus:** Sportler Verein oder Verband wird in Schiedsverfahren vor CAS DIS oder Verbands-Schiedsgericht involviert. WADA-Code Anti-Doping FIFA Players Status Committee. Normen CAS Code Art. R27 ff. DIS-Sportschiedsgerichtsordnung FIFA RSTP Art. 17. Prüfraster Schiedsklausel-Prüfung Frist-Check Verfahrensart Beweis. Output Schiedsklage-Entwurf Strategie-Memo. Abgrenzung zu cas-berufung-vorbereiten (Berufung) und fachanwalt-sportrecht-doping-verfahren (Doping).

### Sport-Schiedsgerichtsbarkeit — CAS / DIS-Sport / Verbände

## Zweck

Sportrecht ist überwiegend Schiedsrecht. **CAS Lausanne** als oberste Instanz, **DIS-Sport** in DE, **Verbands-Schiedsgerichte** DFB/FIFA/UEFA. Klassische Klage zum LG/OLG meist ausgeschlossen durch Schiedsklauseln (Pechstein-Linie).

## Eingaben

- Sportart + Verband
- Streitgegenstand (Transfer, Doping, Disziplinar, Vertrag)
- Schiedsklausel in Spielervertrag / Verbandsstatuten
- Streitwert
- Internationale Komponente

## Rechtlicher Rahmen

- **CAS Code** (Lausanne)
- **WADA-Code** (Doping)
- **NADA-Code** (DE)
- **DIS-Sportschiedsgerichtsordnung**
- **FIFA Statutes** Art. 56-62 (Schiedsgerichtsbarkeit)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## ADR-Pfade

### Pfad 1 — Verbands-Schiedsgericht (DFB, DEB, DHB)

- Erste Instanz
- Verbandsrechtliche Disziplinarverfahren
- Schiedsrichter aus Verbandskreis

### Pfad 2 — DIS-Sportschiedsgerichtsbarkeit

- Bei nationaler Sport-Sache
- Unabhängige Schiedsrichter
- Schiedsspruch endgültig (außer CAS-Berufung)

### Pfad 3 — CAS Lausanne (international)

- Endgültige Instanz bei IOC / Welt-Verband
- Berufung gegen nationale Schiedsentscheidungen
- Verfahrenssprache Englisch / Französisch
- Verfahrens-Dauer 6-18 Monate

### Pfad 4 — FIFA Players' Status Committee

- Spielervertrag-Streit international
- FIFA-DRC (Dispute Resolution Chamber)
- Berufung CAS

### Pfad 5 — Anti-Doping-Verfahren NADA / CAS

- Disziplinar-Verfahren
- Atypisch lange Verfahren
- Sperren bis 4 Jahre

## Doping-Verteidigung

### Phase 1 — Erstinformation

- Notification AAF (Adverse Analytical Finding) Mandant
- 14 Tage zur Stellungnahme

### Phase 2 — A-Probe-Analyse

- B-Probe-Analyse beantragen
- Kette of Custody prüfen
- Labor-Akkreditierung WADA

### Phase 3 — NADA-Verfahren

- Schriftliche Stellungnahme
- Anhörung NADA-Disziplinar-Kommission
- Entscheidung

### Phase 4 — CAS-Berufung

- 21-Tage-Frist nach NADA-Entscheidung
- CAS-Sekretariat
- Schiedsrichter-Auswahl
- Anhörung in Lausanne

### Phase 5 — Schweizerisches Bundesgericht

- Letzte Instanz
- Nur Verfahrens-Fragen (kein zweiter Sachvortrag)

## Strategie und Taktik

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **CAS-Erfahrung Schiedsrichter**: aus CAS-Liste auswählen
- **Doping-Verteidigung**: kontaminierte Nahrungsergänzungs-Mittel als gängiger Verteidigungs-Anker (BGH-Linie zu Cannabis-Verseuchung)
- **B-Probe**: immer beantragen (Chain of Custody)
- **Transfer-Streit**: FIFA-DRC ist Schwerpunkt; CAS als 2. Instanz

## Querverweise

- `fachanwalt-sportrecht-orientierung` — Triage
- `fachanwalt-sportrecht-doping-cas-berufung` — Vertiefung Doping
- `fachanwalt-sportrecht-transferklausel` — Transfer
- `fachanwalt-sportrecht-esports-vereinsrecht-dosb-anerkennung` — eSports

## Quellen und Updates

Stand 05/2026. **Strukturwandel CAS-Endgültigkeit:** EuGH, Urt. v. 01.08.2025 — C-600/23 (RFC Seraing) — Nationale Gerichte der EU-Mitgliedstaaten dürfen CAS-Schiedssprüche auf Vereinbarkeit mit Unionsrecht (insbesondere Grundfreiheiten, Wettbewerbsrecht, Grundrechtecharta) inhaltlich überprüfen; die Vermutung der Endgültigkeit von CAS-Sprüchen ist innerhalb der EU eingeschränkt. Verifikation [curia.europa.eu](https://curia.europa.eu/) zu C-600/23.

Strategische Folge für Mandate: Nach CAS-Entscheidung kann je nach Konstellation neben/statt Anfechtung am Schweizerischen Bundesgericht (Art. 190 IPRG) auch ein Vorgehen vor mitgliedstaatlichen Gerichten geprüft werden (Anerkennung/Vollstreckung mit ordre-public-Vorbehalt; selbständige Klage auf Schadensersatz wegen unionsrechtswidriger Sanktion; einstweiliger Rechtsschutz gegen drohende Vollstreckungswirkungen).

- CAS Code — [tas-cas.org](https://www.tas-cas.org)
- DIS-Sportschiedsgerichtsordnung — [disarb.org](https://www.disarb.org)
- WADA-Code — [wada-ama.org](https://www.wada-ama.org)
- Rechtsprechung im Mandat live verifizieren; keine Aktenzeichen aus Modellwissen.
