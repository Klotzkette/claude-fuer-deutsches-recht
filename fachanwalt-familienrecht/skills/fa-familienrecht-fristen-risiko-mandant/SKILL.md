---
name: fa-familienrecht-fristen-risiko-mandant
description: "FA Familienrecht Fristen Risiko Mandant im Plugin Fachanwalt Familienrecht: prüft konkret Fristen- und Risikoampel im Plugin fachanwalt-familienrecht, Mandantenkommunikation im Plugin fachanwalt-familienrecht, Red-Team Qualitygate im Plugin fachanwalt-familienrecht, zur strukturierten Aufnahme. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# FA Familienrecht Fristen Risiko Mandant

## Arbeitsbereich

**FA Familienrecht Fristen Risiko Mandant** ordnet den Fall über die tragenden Prüfungslinien: Fristen- und Risikoampel im Plugin fachanwalt-familienrecht, Mandantenkommunikation im Plugin fachanwalt-familienrecht, Red-Team Qualitygate im Plugin fachanwalt-familienrecht. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-familienrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-familienrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-familienrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `scheidungsverbund-va-fristenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Scheidungsverbund VA Fristenplan. |
| `spezial-fristen-behoerden-gericht-und-registerweg` | Fristen: Behörden-, Gerichts- oder Registerweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-familienrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fristen- und Risikoampel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin fachanwalt-familienrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Typische Fristen im Familienrecht
- Beschwerde gegen Endentscheidung: ein Monat ab schriftlicher Bekanntgabe (§ 63 Abs. 1 FamFG); bei einstweiliger Anordnung zwei Wochen (§ 63 Abs. 2 FamFG).
- Begründungsfrist Beschwerde: zwei Monate ab schriftlicher Bekanntgabe (§ 117 Abs. 1 FamFG).
- Antrag auf Anpassung Versorgungsausgleich nach § 5 VersAusglG-AnpG nach Ablauf der Trennungszeit.
- Sechs-Monats-Frist Zugewinnausgleich Auskunft Stichtag (§ 1379 BGB).
- Rückforderung Schenkung Schwiegereltern: regelmäßige Verjährung drei Jahre ab Ende des Jahres der Trennungserkenntnis (§§ 195, 199 BGB).

## Praxis-Trade-off
- Schnelle einstweilige Anordnung (§§ 49 ff. FamFG) vs. Hauptsacheantrag: einstweilige Anordnung wirkt sofort, aber begründet keinen Rechtskraftvorteil und kann durch Hauptsache überholt werden.
- Verbund (§ 137 FamFG) vs. isolierte Folgesache: Verbund spart Gebühren, verzögert aber Scheidungsausspruch.

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

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-familienrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandantenkommunikation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin fachanwalt-familienrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Besonderheiten Familienrechts-Mandate
- Hochkonfliktfälle: Trennungsschmerz, gewachsene Vorwürfe, Kinder als emotionaler Hebel. Klare Rolle als Rechtsbeistand, nicht Psycholog/Mediator.
- Mandatskonflikt: bei gemeinsamer Beratung beider Ehegatten Vorsicht; § 43a Abs. 4 BRAO. Im Zweifel nur einen Ehegatten vertreten.
- Datenschutz: bei Kindern besondere Sensibilität; Schweigepflicht gegenüber Familienangehörigen (§ 43a Abs. 2 BRAO).
- Kostenstruktur: Mandant über Kosten klar informieren. RVG-Werte: Scheidung Verfahrenswert nach § 43 FamGKG (3-fach Nettoeinkommen); Folgesachen separate Werte.
- Verfahrenskostenhilfe (§§ 76 ff. FamFG iVm § 114 ZPO) prüfen.
- Schlüsselthema im Schreiben: Frist, Empfehlung, nächste Schritte. Keine endgültige Wertung vor Beweisaufnahme.

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

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-familienrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Red-Team Qualitygate` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin fachanwalt-familienrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## 4. `scheidungsverbund-va-fristenplan`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Scheidungsverbund VA Fristenplan.

# Scheidungsverbund VA Fristenplan

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Scheidungsverbund VA Fristenplan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Scheidungsverbund VA Fristenplan
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einsatz
Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
- Was soll sofort entstehen: Kurztriage, Aktenplan, Fragenliste, Memo, Schriftsatz, Vertrag, Formular oder Mandantenbrief?
- Wo drohen Fristen, Formerfordernisse, Bußgelder, Gebührennachteile, Verfahrensfehler oder irreversible Schritte?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 5. `spezial-fristen-behoerden-gericht-und-registerweg`

**Fokus:** Fristen: Behörden-, Gerichts- oder Registerweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Fristen: Behörden-, Gerichts- oder Registerweg

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fristen: Behörden-, Gerichts- oder Registerweg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Fristen: Behörden-, Gerichts- oder Registerweg
- **Normen-/Quellenanker:** FamFG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fristen** prüfen.
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
