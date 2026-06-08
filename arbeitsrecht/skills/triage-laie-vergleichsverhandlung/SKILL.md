---
name: triage-laie-vergleichsverhandlung
description: "Kueschk Triage Laie Vergleichsverhandlung im Plugin Arbeitsrecht: prüft konkret KERNEINSTIEG Kündigungsschutzklage, Checkliste für Kündigungsschutz-Vergleiche, Weiterbeschaeftigungsantrag nach BAG Grosser Senat 1985, Zeugnisanspruch nach § 109 GewO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Kueschk Triage Laie Vergleichsverhandlung

## Arbeitsbereich

**Kueschk Triage Laie Vergleichsverhandlung** ordnet den Fall über die tragenden Prüfungslinien: KERNEINSTIEG Kündigungsschutzklage, Checkliste für Kündigungsschutz-Vergleiche, Weiterbeschaeftigungsantrag nach BAG Grosser Senat 1985. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `kueschk-triage-laie-oder-anwalt` | KERNEINSTIEG Kündigungsschutzklage: fragt zuerst ob Anwalt oder Verbraucher-Laie; bei Laie ständige Warnungen und dringende Empfehlung anwaltlicher Beratung; kein Mandatsverhältnis; leitet zu passenden Folge-Skills; zentraler Startpunkt für das gesamte KueschK-Workflow-Buendel. |
| `kueschk-vergleichsverhandlung-checkliste` | Checkliste für Kündigungsschutz-Vergleiche: Beendigungsdatum; Abfindung nach Faustformel; Freistellung und Urlaubsabgeltung; Zeugnisnote und -formulierung; Klageerledigung; Outplacement; Rücklage-Klausel; alle Punkte die geregelt werden sollten. |
| `kueschk-weiterbeschaeftigungsantrag-grosser-senat` | Weiterbeschaeftigungsantrag nach BAG Grosser Senat 1985: Voraussetzungen des allgemeinen Weiterbeschaeftigungsanspruchs; Vor- und Nachteile aus Arbeitnehmersicht; Vollstreckung; Unterschied zum § 102 Abs. 5 BetrVG Anspruch. |
| `kueschk-zeugnisanspruch-und-vergleich` | Zeugnisanspruch nach § 109 GewO: qualifiziertes Zeugnis; BAG-Mindestnote befriedigend bei fehlender Substantiierung; Formulierungsrisiken und geheime Negativsignale; typische Vergleichsformulierungen für Zeugnisse. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `kueschk-triage-laie-oder-anwalt`

**Fokus:** KERNEINSTIEG Kündigungsschutzklage: fragt zuerst ob Anwalt oder Verbraucher-Laie; bei Laie ständige Warnungen und dringende Empfehlung anwaltlicher Beratung; kein Mandatsverhältnis; leitet zu passenden Folge-Skills; zentraler Startpunkt für das gesamte KueschK-Workflow-Buendel.

### KüSchK-Triage: Laie oder Anwalt?

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KüSchK-Triage: Laie oder Anwalt?` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill ist der **Kerneinstieg** für das Kündigungsschutzklage-Bündel. Er klärt zunächst, wer den nutzt, und leitet dann zielgerichtet weiter. Ohne diese Triage-Frage können nachgelagerte Skills keine angemessene Risikoeinschätzung liefern.

## Eröffnungsfrage (PFLICHT, immer zuerst)

Das System stellt **als erste und wichtigste Frage**:

> "Bist du Rechtsanwältin / Rechtsanwalt oder nutzt du dieses System als Verbraucher / Laie ohne anwaltliche Zulassung?"

Es werden nur zwei Antworten akzeptiert:
- **Anwalt/Anwältin** → Weiterleitung zu anwaltlichen Bausteinen
- **Verbraucher/Laie** → Weiterleitung zu Laien-Bausteinen **mit umfassender Warnung**

## Pfad A: Anwalt / Anwältin

Für Anwältinnen und Anwälte gilt:
- Kein dauernder Warnkopf erforderlich (Berufsrecht und Haftungsbewusstsein vorausgesetzt)
- Anwaltliche Klageschrifts-Bausteine verfügbar (Skill `kueschk-klageschrift-anwalt-baustein`)
- Hinweis auf Dokumentationspflichten nach § 43a BRAO
- Fristencheck § 4 KSchG trotzdem sofort

## Pfad B: Verbraucher / Laie

Bei Angabe "Verbraucher" oder "Laie" erscheint folgender **Pflicht-Warnblock**, der in jedem Folge-Output wiederholt wird:

---

**WICHTIGE WARNUNG – BITTE GENAU LESEN**

Du bist dabei, rechtliche Schritte einzuleiten, ohne Anwalt zu sein. Das ist gesetzlich erlaubt (§ 11 Abs. 1 ArbGG: kein Anwaltszwang in erster Instanz vor dem Arbeitsgericht), birgt aber erhebliche Risiken:

1. **Drei-Wochen-Frist § 4 KSchG**: Verpasst du diese Frist, gilt die Kündigung als wirksam — ohne Ausnahme.
2. **Falsche Anspruchsgrundlage**: Wenn dein Betrieb weniger als zehn Arbeitnehmer hat oder du noch keine sechs Monate beschäftigt bist, gilt das KSchG möglicherweise gar nicht.
3. **Kein Mandatsverhältnis**: Dieses System ist kein Anwalt, übernimmt keine rechtliche Verantwortung und haftet nicht.
4. **Mechanische Prüfung**: Das System prüft nur das, was du eingibst. Falsche oder unvollständige Angaben führen zu falschen Ergebnissen.

**Dringende Empfehlung**: Suche sofort einen Rechtsanwalt oder eine Rechtsanwältin für Arbeitsrecht auf, idealerweise über den Anwaltssuchdienst der Rechtsanwaltskammern oder über Gewerkschaftsberatung (wenn gewerkschaftlich organisiert). Viele Anwältinnen bieten eine Erstberatung zu Festpreisen an.

---

## Folge-Skills nach Triage

| Nächster Schritt | Skill |
|---|---|
| Grundwarnung und Haftungsausschluss | `kueschk-grundwarnung-falsche-wiese-und-haftung` |
| KSchG-Anwendbarkeit prüfen | `kueschk-anwendbarkeit-kschg-pruefen` |
| Frist und Zugang prüfen | `kueschk-frist-und-zugang-pruefen` |
| Sonderkündigungsschutz prüfen | `kueschk-sonderkuendigungsschutz-checkliste` |
| Formfehler prüfen | `kueschk-formfehler-pruefen` |
| Klageschrift Laie | `kueschk-klageschrift-laie-baustein` |
| Klageschrift Anwalt | `kueschk-klageschrift-anwalt-baustein` |

## Zentrale Normen

- **§ 11 Abs. 1 ArbGG** — Kein Anwaltszwang vor dem Arbeitsgericht erste Instanz
- **§ 11 Abs. 4 ArbGG** — Anwaltszwang ab Berufung vor dem LAG
- **§ 4 KSchG** — Drei-Wochen-Klagefrist (absolute Ausschlussfrist)
- **§ 23 KSchG** — Geltungsbereich KSchG (über 10 Arbeitnehmer)
- **§ 1 Abs. 1 KSchG** — Wartezeit sechs Monate
- **§ 43a BRAO** — Dokumentationspflichten für Anwälte (Beratung über Risiken)
- **§ 626 BGB** — Fristlose Kündigung aus wichtigem Grund (besondere Triage: andere Fristen)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Keine Vorwegnahme des Ergebnisses

Der Skill liefert noch keine inhaltliche Prüfung der Kündigung. Er stellt ausschließlich die Weichenfrage, welche den gesamten nachfolgenden prägt.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 2. `kueschk-vergleichsverhandlung-checkliste`

**Fokus:** Checkliste für Kündigungsschutz-Vergleiche: Beendigungsdatum; Abfindung nach Faustformel; Freistellung und Urlaubsabgeltung; Zeugnisnote und -formulierung; Klageerledigung; Outplacement; Rücklage-Klausel; alle Punkte die geregelt werden sollten.

### Vergleichsverhandlung: Checkliste

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vergleichsverhandlung: Checkliste` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Ein Vergleich im Kündigungsschutzprozess ist mehr als nur eine Abfindungszahlung. Dieser Skill listet alle Punkte auf, die in einem Vergleich geregelt werden sollten — und erklärt, worauf es dabei ankommt.

## Triage zu Beginn — kläre vor Vergleichsverhandlung

1. In welchem Stadium befindet sich das Verfahren (Gütertermin / Kammertermin / nach Urteil)?
2. Liegt bereits ein Vergleichsangebot des Arbeitgebers vor? (Höhe, Beendigungsdatum, Zeugnisnote)
3. Hat der Arbeitnehmer Sonderkündigungsschutz, der den Vergleichsdruck verringert?
4. Droht ein verlorenes Urteil (Hinweisbeschluss des Gerichts zur Erfolgsaussicht bekannt)?
5. Sind alle Vergleichsthemen (Abfindung, Zeugnis, Freistellung, Wettbewerbsverbot) bekannt?

**Schrittfolge Vergleichsverhandlung:**
```
Step 1: Vergleichsangebot entgegennehmen, NICHT sofort zustimmen
Step 2: Bedenk- und Prüfzeit erbitten (mindestens eine Stunde, ggf. bis nächster Tag)
Step 3: Alle Vergleichspunkte schriftlich festhalten (diese Checkliste)
Step 4: Steuerliche und sozialversicherungsrechtliche Auswirkungen berücksichtigen
Step 5: Vergleich bei Zustimmung protokollieren lassen (§ 794 Abs. 1 Nr. 1 ZPO)
Step 6: Widerrufsvorbehalt prüfen (sofern möglich, zwei Wochen Widerrufsfrist vereinbaren)
```

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Checkliste: Was muss in den Vergleich?

### 1. Beendigungsdatum

- **Welches Datum** endet das Arbeitsverhältnis?
- Ist es das Datum der Kündigung oder ein anderes Datum (z.B. nach Verhandlung, Ende Freistellung)?
- Hinweis: Das Beendigungsdatum beeinflusst das Arbeitslosengeld (Anwartschaftszeit, Sperrzeit § 159 SGB III bei eigenem Verstoß)

### 2. Abfindung

- **Höhe** der Abfindung (Faustformel: halbes Bruttomonatsgehalt pro Beschäftigungsjahr — Skill `kueschk-abfindung-faustformel-und-spannweite`)
- **Fälligkeit**: Wann wird die Abfindung gezahlt? (Sofort nach Beendigung, oder später?)
- **Bruttoabfindung** (steuer- und sozialversicherungsrechtliche Behandlung prüfen)
- **Zahlungsweg**: Überweisung auf welches Konto?

### 3. Freistellung

- Ab wann wird der Arbeitnehmer freigestellt?
- Ist die Freistellung **widerruflich** oder unwiderruflich?
- Wird die Freistellungszeit auf den Urlaub angerechnet?
- Wichtig für Urlaubs- und Vergütungsansprüche.

### 4. Urlaubsabgeltung

- Wurden alle Urlaubstage genommen oder sind noch offene Urlaubstage vorhanden?
- § 7 Abs. 4 BUrlG: Offener Urlaub wird bei Beendigung des Arbeitsverhältnisses abgegolten.
- Auszahlungsbetrag: Tagesgehalt × Urlaubstage

### 5. Zeugnis

- Welche **Note** wird im Zeugnis erteilt? (Mindest: "zur vollen Zufriedenheit" = befriedigend)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Zeugnis **ohne qualifizierte Aussage** über Führung und Leistung ist ein Schlechzeugnis.
- Formulierung prüfen: Keine geheimen negativen Formulierungen (z.B. "bemühte sich stets" statt "erledigte stets").
- Ausstellungsdatum: Beendigungsdatum oder anderes Datum?
- Wer unterschreibt das Zeugnis?

### 6. Klageerledigung und Erledigungsklausel

- Wird die Klage durch den Vergleich erledigt?
- Gegenseitiger Verzicht auf alle weiteren Ansprüche aus dem Arbeitsverhältnis?
- Achtung: Eine pauschale Erledigungsklausel kann auch offene Lohnforderungen, Bonusansprüche oder andere Ansprüche vernichten — prüfe, ob das gewollt ist.

### 7. Outplacement / Arbeitsvermittlung

- Manche Vergleiche enthalten eine Zusage des Arbeitgebers, dem Arbeitnehmer bei der Jobsuche zu helfen (Outplacement-Beratung).
- Dieser Punkt ist verhandelbar, wird aber oft nicht angesprochen.

### 8. Wettbewerbsverbot

- Besteht bereits ein vertragliches Wettbewerbsverbot?
- Wird es im Vergleich aufgehoben oder angepasst?
- Karenzentschädigung (§ 74 Abs. 2 HGB: mindestens halbes Jahresgehalt pro Verbotsjahr)

### 9. Geheimhaltungsklausel

- Manche Arbeitgeber verlangen Geheimhaltung über Vergleichsinhalt.
- Übliche Formulierung: "Die Parteien verpflichten sich, über den Inhalt dieses Vergleichs Stillschweigen zu wahren."
- Hinweis: Geheimhaltungsklauseln sind in Vergleichen zulässig, schränken aber die freie Kommunikation ein.

## Muster-Vergleich (Kurzform)

Die Parteien schließen zur Erledigung des Rechtsstreits folgenden Vergleich:

1. Das Arbeitsverhältnis der Parteien endet auf Veranlassung der Beklagten mit Ablauf des [DATUM].
2. Die Beklagte zahlt an den Kläger eine Abfindung nach §§ 9, 10 KSchG in Höhe von [BETRAG] EUR brutto.
3. Der Kläger ist ab sofort unwiderruflich von der Arbeitspflicht freigestellt; offener Urlaub wird auf die Freistellung angerechnet.
4. Die Beklagte erteilt dem Kläger ein qualifiziertes Zeugnis mit der Gesamtnote "gut" bis zum [DATUM].
5. Damit sind alle wechselseitigen Ansprüche aus dem Arbeitsverhältnis und seiner Beendigung erledigt.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 3. `kueschk-weiterbeschaeftigungsantrag-grosser-senat`

**Fokus:** Weiterbeschaeftigungsantrag nach BAG Grosser Senat 1985: Voraussetzungen des allgemeinen Weiterbeschaeftigungsanspruchs; Vor- und Nachteile aus Arbeitnehmersicht; Vollstreckung; Unterschied zum § 102 Abs. 5 BetrVG Anspruch.

### Weiterbeschäftigungsantrag — Großer Senat BAG 1985

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Weiterbeschäftigungsantrag — Großer Senat BAG 1985` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Neben den Feststellungsanträgen kann der klagende Arbeitnehmer einen **Antrag auf tatsächliche Weiterbeschäftigung** stellen. Dieser Anspruch ist in der Rechtsprechung des Großen Senats des BAG entwickelt worden und in der Praxis wichtig — birgt aber auch Risiken.

## Rechtsprechung live prüfen

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernaussage des Großen Senats:**
Das Interesse des Arbeitnehmers an tatsächlicher Beschäftigung überwiegt in der Regel das Interesse des Arbeitgebers an der Nichtbeschäftigung, wenn:
1. Die Kündigung erstinstanzlich für unwirksam befunden wurde, **oder**
2. Die Kündigung offensichtlich unwirksam ist

## Voraussetzungen des allgemeinen Weiterbeschäftigungsanspruchs

1. **Erstinstanzlicher Erfolg:** Das Arbeitsgericht hat die Kündigung für unwirksam erklärt (oder zumindest einen offensichtlich unwirksamen Charakter festgestellt).
2. **Keine überwiegenden Gegeninteressen des Arbeitgebers:** Der Arbeitgeber kann überwiegen geltend machen, z.B. wenn Vertrauen zerstört oder Stellen abgebaut wurden.
3. **Tatsächliche Beschäftigungsmöglichkeit:** Es muss noch eine Beschäftigungsmöglichkeit bestehen.

**Wichtig:** Der Weiterbeschäftigungsanspruch entsteht erst **nach erstinstanzlichem Obsiegen**. Vor der Entscheidung des Arbeitsgerichts besteht er grundsätzlich nicht.

## Triage zu Beginn — kläre vor Beratung zum Weiterbeschaeftigungsantrag

1. Hat das Arbeitsgericht die Kündigung bereits erstinstanzlich für unwirksam erklärt?
2. Besteht ein Betriebsrat, der der Kündigung ordnungsgemäß widersprochen hat (§ 102 Abs. 5 BetrVG)?
3. Will der Arbeitnehmer tatsächlich in den Betrieb zurück (keine Stricken-Situation)?
4. Ist eine tatsächliche Beschäftigungsmöglichkeit noch vorhanden (Stelle nicht abgebaut)?

**Entscheidungsbaum Weiterbeschaeftigungsantrag:**
```
BR-Widerspruch vorhanden? → § 102 Abs. 5 BetrVG (sofort ab Klage, ohne Ersturteil)
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rueckkehr nicht gewünscht? → Kein WBA stellen; § 12 KSchG oder Vergleich prüfen
Arbeitgeber kann überwiegende Gegeninteressen darlegen? → Antrag abweisbar
```

## Aktuelle Rechtsprechung

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Unterschied: § 102 Abs. 5 BetrVG

Besteht ein Betriebsrat und hat er der Kündigung ordnungsgemäß widersprochen, hat der Arbeitnehmer nach § 102 Abs. 5 BetrVG einen gesetzlichen Weiterbeschäftigungsanspruch — **sofort ab Klageerhebung**, ohne dass er erstinstanzlich obsiegen müsste.

| | BAG GS 1985 | § 102 Abs. 5 BetrVG |
|---|---|---|
| Voraussetzung | Erstinstanzlicher Sieg | BR-Widerspruch + Klage |
| Zeitpunkt | Nach Urteil | Ab Klageerhebung |
| Geltung | Immer | Nur bei BR vorhanden |

## Vor- und Nachteile des Weiterbeschäftigungsantrags

**Vorteile:**
- Arbeitnehmer muss nicht bis Rechtskraft warten
- Beschäftigung erhält Sozialversicherungsschutz und Praxisroutine aufrecht
- Erhöht Druck auf Arbeitgeber zur Vergleichsbereitschaft

**Nachteile:**
- Risiko: Wenn Arbeitgeber im Berufungsverfahren obsiegt, muss Arbeitnehmer zurückzahlen (Annahmeverzugslohn § 615 BGB vs. tatsächliches Gehalt — Differenz kann entstehen)
- Logistik: Rückkehr in den Betrieb kann belastend sein (Konflikte, Isolation)
- Arbeitgeber kann Weiterbeschäftigung durch Vollstreckungsgegenklage abwehren

**Praxishinweis:** Den Weiterbeschäftigungsantrag sollte man nur stellen, wenn man tatsächlich zurück in den Betrieb will. Wer bereits einen neuen Job hat, sollte § 12 KSchG prüfen.

## Vollstreckung

Bei Verurteilung zur Weiterbeschäftigung: Vollstreckung nach § 888 ZPO (Zwangsgeld oder Zwangshaft), da unvertretbare Handlung.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:

## 4. `kueschk-zeugnisanspruch-und-vergleich`

**Fokus:** Zeugnisanspruch nach § 109 GewO: qualifiziertes Zeugnis; BAG-Mindestnote befriedigend bei fehlender Substantiierung; Formulierungsrisiken und geheime Negativsignale; typische Vergleichsformulierungen für Zeugnisse.

### Zeugnisanspruch und Zeugnis im Vergleich

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zeugnisanspruch und Zeugnis im Vergleich` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Das Zeugnis ist oft ein wichtiger Verhandlungspunkt im Kündigungsschutzprozess. Arbeitnehmer haben einen gesetzlichen Anspruch auf ein qualifiziertes Zeugnis — aber die Note ist verhandelbar.

## Triage zu Beginn — kläre vor Zeugnisberatung

1. Liegt bereits ein Zeugnis vor, das beanstandet werden soll?
2. Soll die Zeugnisnote im Vergleich verhandelt werden (Zielkorridor: gut oder sehr gut)?
3. Ist das Zeugnis Teil eines größeren Vergleichs oder ein eigenständiger Anspruch nach Beendigung?
4. Bestehen konkrete Negativformulierungen oder Schlüsselsatzprobleme im vorliegenden Zeugnis?

**Schrittfolge Zeugnisstrategie im Vergleich:**
```
Step 1: Ist eine bestimmte Note gewünscht? → Konkrete Formulierung vereinbaren
Step 2: Zeugnisentwurf vorliegen lassen und prüfen
Step 3: Negativsignale identifizieren (vgl. Negativsignal-Liste unten)
Step 4: Option B (vollständiger Zeugnistext im Vergleich) bei Zweifeln bevorzugen
Step 5: Ausstellungsdatum und Unterzeichner festschreiben
Step 6: Frist für Ausstellung (z.B. zwei Wochen nach Beendigung) in Vergleich aufnehmen
```

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Gesetzlicher Anspruch § 109 GewO

Nach § 109 Abs. 1 GewO hat der Arbeitnehmer bei Beendigung des Arbeitsverhältnisses Anspruch auf ein schriftliches Zeugnis. Das Zeugnis muss mindestens Angaben über Art und Dauer der Tätigkeit enthalten (einfaches Zeugnis).

**Qualifiziertes Zeugnis** (§ 109 Abs. 1 Satz 3 GewO): Der Arbeitnehmer kann verlangen, dass das Zeugnis auch Angaben über Leistung und Verhalten enthält.

## BAG-Mindeststandard: Note "befriedigend"

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Formulierung: **"zur vollen Zufriedenheit"** entspricht der Note befriedigend.

Für eine bessere Note (gut, sehr gut) muss der Arbeitnehmer dartun, dass seine Leistungen besser waren. Typische Formulierungen:

| Note | Formulierung |
|---|---|
| Sehr gut | "stets zu unserer vollsten Zufriedenheit" |
| Gut | "stets zu unserer vollen Zufriedenheit" |
| Befriedigend | "zu unserer vollen Zufriedenheit" |
| Ausreichend | "zu unserer Zufriedenheit" |
| Mangelhaft | "hat sich bemüht" o.ä. |

## Geheime Negativsignale im Zeugnis

Arbeitgeber verwenden manchmal Formulierungen, die nach außen positiv klingen, aber in der Branche als Negativsignal bekannt sind:

- "Er hat die übertragenen Aufgaben stets zu unserer Zufriedenheit erledigt" (Note 4 — mangelhaft)
- "Sie war stets bemüht" (Zeugnissprache für: hat versucht, aber nicht geschafft)
- "Er hat die ihm übertragenen Aufgaben mit großem Fleiß erledigt" (ohne Erwähnung von Erfolg = Warnsignal)
- Weglassen von Führungsverantwortung obwohl vorhanden = Negativsignal

**Im Vergleich:** Wenn eine bestimmte Note oder Formulierung vereinbart wird, diese konkret und wortwörtlich im Vergleich festschreiben. "Gut" ist besser als jede Formulierung, die interpretiert werden kann.

## Typische Vergleichsformulierungen zum Zeugnis

**Option A — Note vereinbaren:**
"Die Beklagte erteilt dem Kläger ein qualifiziertes Zeugnis mit der Gesamtnote gut (Formulierung: 'stets zu unserer vollen Zufriedenheit')."

**Option B — Zeugnisinhalt konkret vereinbaren:**
"Die Beklagte erteilt dem Kläger ein qualifiziertes Zeugnis folgenden Inhalts: [vollständiger Zeugnistext]."

Option B ist sicherer — sie verhindert spätere Streitigkeiten über die Formulierung.

## Zeugnisberichtigungsklage

Falls das ausgestellte Zeugnis von der Vereinbarung abweicht oder schlechter als angemessen ist: Zeugnisberichtigungsklage beim Arbeitsgericht. Klageziel: Ausstellung eines Zeugnisses mit bestimmter Formulierung oder bestimmter Note.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
