---
name: protokoll-sonderumlage-weg
description: "Protokoll Sonderumlage WEG: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Protokoll Sonderumlage WEG

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Protokoll Sonderumlage WEG** im Plugin WEG / Hausverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-protokoll-behoerden-gericht-und-registerweg` | Protokoll: Behörden-, Gerichts- oder Registerweg im WEG- und Hausverwaltungsrecht: fachlich vertiefter Fachmodul mit Normenradar (WEG/BGB/BetrKV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-sonderumlage-compliance-dokumentation-und-akte` | Sonderumlage: Compliance-Dokumentation und Aktenvermerk im WEG- und Hausverwaltungsrecht: fachlich vertiefter Fachmodul mit Normenradar (WEG/BGB/BetrKV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-weg-tatbestand-beweis-und-belege` | WEG: Tatbestandsmerkmale, Beweisfragen und Beleglage im WEG- und Hausverwaltungsrecht: fachlich vertiefter Fachmodul mit Normenradar (WEG/BGB/BetrKV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin WEG / Hausverwaltung gilt für **Protokoll Sonderumlage WEG**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-protokoll-behoerden-gericht-und-registerweg`

**Fokus:** Protokoll: Behörden-, Gerichts- oder Registerweg im WEG- und Hausverwaltungsrecht: fachlich vertiefter Fachmodul mit Normenradar (WEG/BGB/BetrKV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Protokoll: Behörden-, Gerichts- oder Registerweg

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Protokoll: Behörden-, Gerichts- oder Registerweg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Protokoll: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Protokoll: Behörden-, Gerichts- oder Registerweg wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Protokoll** prüfen.
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

## Qualitätsanker: WEG-Reform, Beschlussgegenstand und Abrechnungsspitze

- **Verifizierte Rechtsprechungsanker:** BGH, Urteil vom 20.09.2024 - V ZR 195/23: Fehler der Jahresabrechnung tragen die Ungültigerklärung nur, wenn sie sich auf Abrechnungsspitze und Zahlungspflicht auswirken. BGH, Urteil vom 14.02.2025 - V ZR 236/23 und V ZR 128/23: Kostenverteilung nach § 16 Abs. 2 WEG verlangt Beschlusskompetenz, Sachgrund und saubere Belastungslogik. Bei jeder Ausgabe vor Zitat freie Quelle erneut prüfen.
- **Reformlogik:** Seit der WEG-Reform ist nicht „die Jahresabrechnung als Zahlenwerk“ der Beschlussgegenstand, sondern Nachschüsse und Anpassung der Vorschüsse nach § 28 Abs. 2 WEG. Das ist die zentrale Weiche für Anfechtung, Bestimmtheit und Fehlerrelevanz.
- **Praktische Prüfung:** Beschlusskompetenz, Bestimmtheit, Ladung/Tagesordnung, Stimmrecht, Verteilungsschlüssel, Belegprüfung, Rücklage/Vermögensbericht, HeizKV, Umsatzsteuer/Vorsteuer und Anfechtungsfrist getrennt prüfen.
- **Output-Pflicht:** Für Verwaltung/Eigentümer immer eine Beschluss- oder Anfechtungsmatrix liefern: Beschlusswortlaut, Rechtsgrundlage, Fehler, Zahlungsrelevanz, Beleg, Frist, Heilungs- oder Neufassungsoption.

## 2. `spezial-sonderumlage-compliance-dokumentation-und-akte`

**Fokus:** Sonderumlage: Compliance-Dokumentation und Aktenvermerk im WEG- und Hausverwaltungsrecht: fachlich vertiefter Fachmodul mit Normenradar (WEG/BGB/BetrKV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Sonderumlage: Compliance-Dokumentation und Aktenvermerk

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sonderumlage: Compliance-Dokumentation und Aktenvermerk` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Sonderumlage: Compliance-Dokumentation und Aktenvermerk
- **Spezialgegenstand:** Sonderumlage: Compliance-Dokumentation und Aktenvermerk wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Sonderumlage** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Sonderumlage
- **Rechtsgrundlage:** Sonderumlage ist eine außerordentliche Vorschusserhebung über den Wirtschaftsplan hinaus, fußend auf § 28 Abs. 1 WEG analog (Vorschusspflicht). Anspruchsinhaberin: GdWE (§ 9a WEG).
- **Beschlusserfordernis:** Einfache Mehrheit (§ 25 Abs. 1 WEG). Die Sonderumlage muss in der Tagesordnung konkret benannt sein (Zweck, Höhe, Verteilungsschlüssel, Fälligkeit), sonst Anfechtbarkeit.
- **Bestimmtheit:** Beschluss muss enthalten: Gesamtbetrag, Verteilungsmaßstab (in der Regel MEA gem. § 16 Abs. 2 WEG, abweichend nur bei vorhandener Beschlusskompetenz), Fälligkeit pro Eigentümer, Zweckbindung. BGH ständige Rspr.: unbestimmter Sonderumlagebeschluss ist nichtig (nicht nur anfechtbar).
- **Erhaltungsrücklage vs. Sonderumlage:** Bei ausreichender Rücklage ist Sonderumlage nur subsidiär ordnungsgemäße Verwaltung (§ 19 WEG). Bei kurzfristigem Liquiditätsbedarf zur Vermeidung von Schäden zulässig auch wenn Rücklage rechnerisch ausreicht (Notfallargument).
- **Verteilungsmaßstab bei baulicher Veränderung:** § 21 WEG (kostentragende Mehrheit; Kostenverteilung nur auf Zustimmende, außer Ausnahmen § 21 Abs. 2 WEG).
- **Anfechtungsrisiko:** § 45 WEG (ein Monat). Bei Anfechtung bleibt die Forderung bis zur Rechtskraft fällig (§ 23 Abs. 4 WEG; vorläufige Vollstreckbarkeit möglich).
- **Stolperfalle:** Sonderumlage darf nicht zur Auffüllung der Erhaltungsrücklage zweckentfremdet werden; das ist gesonderter Beschlussgegenstand.

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

## Qualitätsanker: WEG-Reform, Beschlussgegenstand und Abrechnungsspitze

- **Verifizierte Rechtsprechungsanker:** BGH, Urteil vom 20.09.2024 - V ZR 195/23: Fehler der Jahresabrechnung tragen die Ungültigerklärung nur, wenn sie sich auf Abrechnungsspitze und Zahlungspflicht auswirken. BGH, Urteil vom 14.02.2025 - V ZR 236/23 und V ZR 128/23: Kostenverteilung nach § 16 Abs. 2 WEG verlangt Beschlusskompetenz, Sachgrund und saubere Belastungslogik. Bei jeder Ausgabe vor Zitat freie Quelle erneut prüfen.
- **Reformlogik:** Seit der WEG-Reform ist nicht „die Jahresabrechnung als Zahlenwerk“ der Beschlussgegenstand, sondern Nachschüsse und Anpassung der Vorschüsse nach § 28 Abs. 2 WEG. Das ist die zentrale Weiche für Anfechtung, Bestimmtheit und Fehlerrelevanz.
- **Praktische Prüfung:** Beschlusskompetenz, Bestimmtheit, Ladung/Tagesordnung, Stimmrecht, Verteilungsschlüssel, Belegprüfung, Rücklage/Vermögensbericht, HeizKV, Umsatzsteuer/Vorsteuer und Anfechtungsfrist getrennt prüfen.
- **Output-Pflicht:** Für Verwaltung/Eigentümer immer eine Beschluss- oder Anfechtungsmatrix liefern: Beschlusswortlaut, Rechtsgrundlage, Fehler, Zahlungsrelevanz, Beleg, Frist, Heilungs- oder Neufassungsoption.

## 3. `spezial-weg-tatbestand-beweis-und-belege`

**Fokus:** WEG: Tatbestandsmerkmale, Beweisfragen und Beleglage im WEG- und Hausverwaltungsrecht: fachlich vertiefter Fachmodul mit Normenradar (WEG/BGB/BetrKV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# WEG: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `WEG: Tatbestandsmerkmale, Beweisfragen und Beleglage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: WEG: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** WEG: Tatbestandsmerkmale, Beweisfragen und Beleglage wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **WEG** prüfen.
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

## Qualitätsanker: WEG-Reform, Beschlussgegenstand und Abrechnungsspitze

- **Verifizierte Rechtsprechungsanker:** BGH, Urteil vom 20.09.2024 - V ZR 195/23: Fehler der Jahresabrechnung tragen die Ungültigerklärung nur, wenn sie sich auf Abrechnungsspitze und Zahlungspflicht auswirken. BGH, Urteil vom 14.02.2025 - V ZR 236/23 und V ZR 128/23: Kostenverteilung nach § 16 Abs. 2 WEG verlangt Beschlusskompetenz, Sachgrund und saubere Belastungslogik. Bei jeder Ausgabe vor Zitat freie Quelle erneut prüfen.
- **Reformlogik:** Seit der WEG-Reform ist nicht „die Jahresabrechnung als Zahlenwerk“ der Beschlussgegenstand, sondern Nachschüsse und Anpassung der Vorschüsse nach § 28 Abs. 2 WEG. Das ist die zentrale Weiche für Anfechtung, Bestimmtheit und Fehlerrelevanz.
- **Praktische Prüfung:** Beschlusskompetenz, Bestimmtheit, Ladung/Tagesordnung, Stimmrecht, Verteilungsschlüssel, Belegprüfung, Rücklage/Vermögensbericht, HeizKV, Umsatzsteuer/Vorsteuer und Anfechtungsfrist getrennt prüfen.
- **Output-Pflicht:** Für Verwaltung/Eigentümer immer eine Beschluss- oder Anfechtungsmatrix liefern: Beschlusswortlaut, Rechtsgrundlage, Fehler, Zahlungsrelevanz, Beleg, Frist, Heilungs- oder Neufassungsoption.
