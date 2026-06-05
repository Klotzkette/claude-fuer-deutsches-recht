---
name: ki-governance-fristen-risikoampel-mandantenkommunikation
description: "Fristen Risikoampel Mandantenkommunikation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Fristen Risikoampel Mandantenkommunikation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Fristen Risikoampel Mandantenkommunikation** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin ki-governance: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin ki-governance: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin ki-governance: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **Fristen Risikoampel Mandantenkommunikation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin ki-governance: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin ki-governance: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## KI-Governance-typische Fristen
- **Datenpanne**: Art. 33 Abs. 1 DSGVO – Meldung an die Aufsichtsbehörde binnen **72 Stunden** ab Kenntnis.
- **Betroffenenbenachrichtigung**: Art. 34 DSGVO – unverzüglich bei hohem Risiko.
- **KI-VO-Vorfall (Hochrisiko)**: Art. 73 KI-VO – Meldung an Marktüberwachungsbehörde innerhalb von 15 Tagen, bei schwerwiegenden Vorfällen oder breit angelegten Verstößen innerhalb von 2 Tagen, bei Tod sofort.
- **Geltungsbeginn KI-VO**: Art. 5 (Verbote) seit 02.02.2025, Art. 51 ff. (GPAI) seit 02.08.2025, Art. 6 ff. (Hochrisiko) ab 02.08.2026.

## Ampelkriterien
- **Rot**: laufende Frist < 72h, Aufsichtsbehörde involviert, mögliche Verbotene-Praktik-Lage (Art. 5 KI-VO), § 203 StGB-Berührung.
- **Gelb**: Klassifizierung offen (Hochrisiko vs. Begrenzt), AVV/Drittlandstransfer ungeklärt, Dokumentationslücken.
- **Grün**: gesicherte Klassifizierung, Doku vollständig, Schulung erfolgt, AVV/SCC vorhanden.

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

## 2. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin ki-governance: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin ki-governance: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Mandantenkommunikation KI-Governance
- **Anrede + Bezug:** "In Sachen [Mandant] / Ihre KI-Compliance"
- **Sachstand kurz:** welche KI-Systeme erfasst, welche Risiken erkannt, welche Klassifizierung.
- **Empfehlung in 2-3 Sätzen:** zentral umsetzbarer nächster Schritt (z. B. "AVV mit Anbieter X nachverhandeln, US-Transfer-TIA dokumentieren, Schulungsnachweis Art. 4 KI-VO erbringen").
- **Risikoampel:** Rot/Gelb/Grün mit knapper Begründung.
- **Nächste Schritte mit Frist und Verantwortlichkeit:** wer macht was bis wann.
- **Kostenhinweis:** RVG/Honorarvereinbarung.
- **Schweigepflicht-Hinweis bei externer KI-Nutzung:** falls Mandantendaten verarbeitet werden, Information über § 203 StGB-Aspekte (transparent, ohne Verharmlosung).

## Praxis-Tipp
Vermeiden Sie technische Doppelbegriffe ohne Erklärung ("DPF", "SCC", "GPAI"). Erläutern Sie die Begriffe in einer Fußnote oder kurz im Text — sonst entsteht der Eindruck eines abgehobenen Berichts, der nicht entschieden werden kann.

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

## 3. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin ki-governance: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin ki-governance: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Red-Team-Prüfpunkte KI-Governance
1. **Klassifizierung:** Wurde die KI-VO-Risikoklasse begründet (Anhang III geprüft, nicht nur abgelehnt)?
2. **Rolle:** Anbieter (Art. 3 Nr. 3) vs. Betreiber (Art. 3 Nr. 4) vs. Importeur (Art. 3 Nr. 6) — wurde der unterschiedliche Pflichtenkanon adressiert?
3. **DSGVO-Schnittstelle:** Rechtsgrundlage Art. 6 / Art. 9 DSGVO benannt? Bei automatisierten Entscheidungen Art. 22 DSGVO geprüft?
4. **AVV:** Vollständig nach Art. 28 Abs. 3 DSGVO, mit TOM (Art. 32) und Unterauftragsverarbeiterliste?
5. **Drittlandstransfer:** DPF-Status (aktuell?), SCC-Modul richtig, TIA dokumentiert?
6. **Halluzinations-Check:** Wurden Erwägungsgründe / Aktenzeichen / Behördenseiten ohne Live-Quelle zitiert?
7. **Geltungsbeginn:** Wurden die gestaffelten Geltungstermine (Art. 113 KI-VO) berücksichtigt?

## Praxis-Tipp
Häufiger Fehler: Pauschalsubsumtion "kein Hochrisiko" ohne Anhang-III-Prüfung. Im Output stets sichtbar machen: welche Anhang-III-Ziffer geprüft, mit welcher Begründung ausgeschlossen — sonst trägt die Klassifizierung im Audit nicht.

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
