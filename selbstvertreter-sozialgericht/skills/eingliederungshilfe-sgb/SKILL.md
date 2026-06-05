---
name: eingliederungshilfe-sgb
description: "Eingliederungshilfe SGB: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Eingliederungshilfe SGB

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Eingliederungshilfe SGB** im Plugin Selbstvertretung vor dem Sozialgericht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `eingliederungshilfe-sgb-ix-rehabilitation` | Eingliederungshilfe nach SGB IX Teil 2. Skill klaert die Leistungen zur Teilhabe am Arbeitsleben (Reha) zur sozialen Teilhabe und zur Bildung Antragsverfahren beim zustaendigen Reha-Traeger. Liefert Pruefraster. |
| `eingliederungsvereinbarung-15-sgb-ii` | Eingliederungsvereinbarung nach § 15 SGB II / nach Reform 2023 Kooperationsplan. Skill erklaert den Kooperationsplan zwischen Buergergeldbeziehenden und Jobcenter Vorgehen Pflichten Verhandlungsmoeglichkeiten und Verweigerungsfolgen. Liefert Pruefraster. |
| `einreichung-fax-und-grenzen-sozialgericht` | Fax beim SG einreichen Vorteile und Grenzen. Sendebericht als Beweis Telefax-Nummer prüfen Frist halten. Hinweis Fax wird abgeschafft Alternativen vorhanden. |
| `einreichung-mein-justizpostfach-mjp-sozialgericht` | Mein Justizpostfach (MJP) für Buerger seit 2024. Online-Einreichung von Klagen und Schriftsaetzen beim Sozialgericht. Anmeldung Identifikation PDF-Anlagen Sicherheit. |
| `einreichung-papierform-sozialgericht-mit-abschriften` | Klage und Schriftsatz per Post beim SG einreichen. Abschriften für Gegner und Akte. Adressierung Einschreiben Empfangsbestätigung. Praktischer Versandweg für Buerger. |

## Arbeitsweg

Im Plugin Selbstvertretung vor dem Sozialgericht gilt für **Eingliederungshilfe SGB**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `eingliederungshilfe-sgb-ix-rehabilitation`

**Fokus:** Eingliederungshilfe nach SGB IX Teil 2. Skill klaert die Leistungen zur Teilhabe am Arbeitsleben (Reha) zur sozialen Teilhabe und zur Bildung Antragsverfahren beim zustaendigen Reha-Traeger. Liefert Pruefraster.

# Eingliederungshilfe Sgb Ix Rehabilitation

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eingliederungshilfe Sgb Ix Rehabilitation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Eingliederungshilfe — Wer ist zustaendig

- Land/Kommune ueber das jeweilige Land (Sozialamt Bezirksregierung).
- Spezialisierte Traeger fuer Komplexleistungen.

## Reha-Traeger nach § 6 SGB IX

- Krankenkasse.
- Rentenversicherung.
- BG / UV.
- Jobcenter.
- BA.
- Versorgungsverwaltung.
- Eingliederungshilfe.

## Leistungen

### § 90 SGB IX — Teilhabe am Arbeitsleben
- Berufliche Foerderung.
- Werkstaetten fuer behinderte Menschen.
- Budget fuer Arbeit.

### § 75 SGB IX — soziale Teilhabe
- Assistenz.
- Bildung.
- Mobilitaet.

### § 112 SGB IX — Leistungen zur Bildung
- Bildung im Schulkontext.

## Persoenliches Budget § 29 SGB IX

- Geldleistung statt Sachleistung.
- Selbstbestimmtes Einkaufen von Leistungen.

## Pruefraster

1. Welche Teilhabe?
2. Welcher Reha-Traeger?
3. Persoenliches Budget?
4. Antragspfad?

## 2. `eingliederungsvereinbarung-15-sgb-ii`

**Fokus:** Eingliederungsvereinbarung nach § 15 SGB II / nach Reform 2023 Kooperationsplan. Skill erklaert den Kooperationsplan zwischen Buergergeldbeziehenden und Jobcenter Vorgehen Pflichten Verhandlungsmoeglichkeiten und Verweigerungsfolgen. Liefert Pruefraster.

# Eingliederungsvereinbarung 15 Sgb Ii

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eingliederungsvereinbarung 15 Sgb Ii` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Reform 2023

- Vorher Eingliederungsvereinbarung § 15 SGB II — oft als VA erlassen.
- Seit 2023: Kooperationsplan auf Augenhoehe, ohne VA-Charakter.
- Normanker: SGB II § 15 Kooperationsplan; SGB II §§ 31 ff. Leistungsminderungen/Pflichtverletzungen; SGB X für Anhörung/Bescheid, SGG für Widerspruch/Klage.
- Immer aktuellen Bescheid, Einladung, Rechtsfolgenbelehrung und Protokoll des Jobcenters lesen; nicht aus alten EGV-Mustern arbeiten.

## Inhalt Kooperationsplan

- Beidseits zu erfuellende Schritte.
- Aktivitaeten Bewerbungen Bildungsmassnahmen.
- Beruf der den Buerger interessiert.

## Verhandlungsspielraum

- Buerger kann mit Argumenten Anpassungen verlangen.
- Bei Streit kein VA — keine Sanktion direkt aus Plan.
- Sanktion nur bei nachweisbaren Pflichtverletzungen (Arbeitsangebot ablehnen).
- Eigene gesundheitliche, familiäre, sprachliche, betreuungs- oder schulische Hindernisse konkret belegen.
- Qualifizierung, Bewerbungsstrategie, Fahrtkosten, Kinderbetreuung und digitale Bewerbungsmöglichkeiten aktiv hineinverhandeln.

## Pflichtverletzungen

- Termin nicht halten.
- Bewerbungsbemuehungen nicht nachweisen.
- Arbeitsangebot nicht annehmen.
- Sanktion setzt normalerweise konkrete Pflicht, Belehrung und Anhörung voraus; Kooperationsplan allein ersetzt das nicht.
- Bei Krankheit/Überforderung sofort Nachweis und neuen Termin anbieten, nicht schweigen.

## Pruefraster

1. Kooperationsplan vorgelegt?
2. Inhaltliche Pruefung?
3. Verhandlungsspielraum genutzt?
4. Sanktionsrisiko realistisch?
5. Gibt es eine konkrete Rechtsfolgenbelehrung oder nur allgemeinen Druck?
6. Widerspruch gegen Minderungsbescheid und einstweiliger Rechtsschutz nötig?

## Output

Kooperationsplan-Redline, Gesprächsvorbereitung, Nachweisliste, Änderungswunsch und Widerspruchs-/Eilantragsampel.

## 3. `einreichung-fax-und-grenzen-sozialgericht`

**Fokus:** Fax beim SG einreichen Vorteile und Grenzen. Sendebericht als Beweis Telefax-Nummer prüfen Frist halten. Hinweis Fax wird abgeschafft Alternativen vorhanden.

# Klage per Fax beim SG — Grenzen und Tipps

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Klage per Fax beim SG — Grenzen und Tipps` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Fax ist immer noch ein anerkannter Weg, eine Klage einzureichen. Vorteil: Sie haben einen Beweis fuer den Eingang am selben Tag. Nachteil: Fax wird zunehmend abgeschafft. Diese Skill zeigt, wann Fax sinnvoll ist und worauf Sie achten muessen.

## In einfacher Sprache

Sie koennen die Klage auch per Fax schicken. Das geht schnell. Sie haben einen Beweis. Aber: nicht jedes Gericht hat noch ein Fax. Pruefen Sie das vorher.

## Wann brauchen Sie diese Skill?

- Sie wollen am letzten Tag der Frist noch sicher einreichen.
- Sie haben keinen Computer fuer MJP.
- Sie wollen eine Sofort-Bestaetigung.

## Fachbegriffe (kurz erklaert)

- **Sendebericht**: Der Ausdruck nach dem Faxen — zeigt "OK" oder "Fehler".
- **Telefax-Nummer**: Die Faxnummer; muss aktuell sein.
- **OK-Vermerk**: Bestaetigung, dass das Fax durchgekommen ist.

## Rechtsgrundlagen

- **§ 90 SGG i.V.m. § 130 ZPO analog** — Fax ist Schriftform (BGH gefestigt).
- **§ 65a SGG** — Elektronische Alternativen.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Aktuelle Faxnummer pruefen

- Auf www.sozialgerichtsbarkeit.de
- Oder bei der Geschaeftsstelle anrufen.

Achtung: Einige SG haben das Fax abgeschafft oder umgestellt. Pruefen Sie immer aktuell.

### Schritt 2 — Schriftsatz vorbereiten

- Sauberen Ausdruck am Computer
- Unterschrift drauf
- Anlagen ggf. ebenso

### Schritt 3 — Faxgeraet finden

- Eigenes Geraet (wenn vorhanden)
- Im Copy-Shop oder Schreibwarenladen (ca. 1 bis 3 EUR pro Seite)
- Beim Steuerberater / VdK / Sozialberatung (Anfrage)
- Online-Faxdienst (z.B. www.fax.de, kostet aber Geld)

### Schritt 4 — Faxen und Sendebericht aufheben

- Nummer waehlen mit fuehrender Null.
- Nach dem Senden: Sendebericht ausdrucken.
- Pruefen, dass "OK" oder "Erfolg" dasteht.

### Schritt 5 — Aufheben

- Sendebericht zur Sicherheit aufheben.
- Bei "Fehler" sofort nochmal senden oder Alternative nutzen.

### Schritt 6 — Bei Versand am letzten Tag

- Frueh am Tag senden (nicht 23:55).
- Wenn das Fax voll ist, koennte es bei spaeter Sendung nicht durchgehen.
- Im Notfall mehrere Versuche; jeden Sendebericht aufheben.

## Worauf Sie besonders achten muessen

- **Fax verschwindet**: Justizverwaltung baut Fax allmaehlich ab. Pruefen Sie vor jedem Einsatz.
- **Sendebericht ist ENTSCHEIDEND**: ohne OK-Sendebericht haben Sie keinen Beweis.
- **Quality**: Fax-Vorlage muss lesbar sein. Dunkler Text auf hellem Grund.
- **Anlagen mit vielen Seiten**: dauert lange; Geraet kann waehrenddessen abbrechen.

## Typische Fehler

- "Fax geschickt, aber kein Sendebericht" → ohne Beweis verloren
- Falsche Faxnummer → an die Falsche geschickt; ungueltig
- Sehr lange Anhaenge per Fax → besser splitten oder MJP / Post
- Letzter Tag, Geraet besetzt → schon morgens versuchen

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `einreichung-mein-justizpostfach-mjp-sozialgericht` — digitale Alternative
- `einreichung-papierform-sozialgericht-mit-abschriften` — Post
- `klage-zusammenstellen-bundle-sozialgericht` — Komplett-Versand
- `versand-selbst-zurechnung-laien-sozialgericht` — Versand-Beweis

## Quellen und Aktualitaet

Stand: 05/2026. BGH und BSG haben Fax-Schriftform vielfach bestaetigt. Fax in der Justiz wird mittelfristig abgeschafft. Pruefen Sie bei Ihrem SG aktuell, ob noch verfuegbar.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `einreichung-mein-justizpostfach-mjp-sozialgericht`

**Fokus:** Mein Justizpostfach (MJP) für Buerger seit 2024. Online-Einreichung von Klagen und Schriftsaetzen beim Sozialgericht. Anmeldung Identifikation PDF-Anlagen Sicherheit.

# Mein Justizpostfach — digitale Einreichung beim SG

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mein Justizpostfach — digitale Einreichung beim SG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Seit 2024 koennen Buerger ueber "Mein Justizpostfach" (MJP) digital mit Gerichten und Behoerden kommunizieren. Sicher, schnell, kostenfrei. Diese Skill zeigt, wie Sie damit Ihre Klage oder Schriftsaetze beim SG einreichen.

## In einfacher Sprache

Es gibt ein sicheres Online-Postfach fuer Buerger. Es heisst Mein Justizpostfach. Damit koennen Sie Klagen direkt ans Gericht schicken. Schnell, sicher, gratis.

## Wann brauchen Sie diese Skill?

- Sie wollen ohne Brief und Fax beim SG einreichen.
- Sie haben einen Online-Personalausweis.
- Sie wollen einen sicheren Versandweg.

## Fachbegriffe (kurz erklaert)

- **Mein Justizpostfach (MJP)**: Sicheres digitales Postfach fuer Buerger.
- **eID-Funktion**: Online-Funktion des Personalausweises.
- **ELSTER-Zertifikat**: Steuer-Identifikation, alternativ nutzbar.
- **OZG**: Onlinezugangsgesetz, schreibt digitale Verwaltung vor.

## Rechtsgrundlagen

- **§ 65a SGG** — Elektronische Einreichung beim Gericht.
- **§ 36a SGB I** — Elektronische Kommunikation mit Behoerden.
- **Onlinezugangsgesetz (OZG)** — rechtlicher Rahmen fuer digitale Verwaltung.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Voraussetzungen pruefen

Sie brauchen:

- **Computer** oder Smartphone mit Internet
- Eine **Identifikation**, eine der drei:
 - Personalausweis mit Online-Funktion (eID) + PIN + Lesegeraet oder Smartphone-App "AusweisApp"
 - ELSTER-Zertifikat (von Ihrer Steuererklaerung)
 - DE-Mail-Account (auslaufend, lieber andere Wege)

### Schritt 2 — Konto anlegen

1. Gehen Sie auf www.mein-justizpostfach.de.
2. Klicken Sie auf "Registrieren".
3. Identifizieren Sie sich mit einer der Methoden.
4. Postfach wird angelegt.

Die Registrierung dauert 10 bis 20 Minuten.

### Schritt 3 — Empfaenger waehlen

- Suchen Sie nach "Sozialgericht [Ort]".
- Pruefen Sie, dass Sie den richtigen Empfaenger ausgewaehlt haben.

### Schritt 4 — Schriftsatz vorbereiten

Ihre Klage / Ihr Widerspruch als PDF:

- Word-Datei → "Speichern unter" → PDF
- Oder Foto mit Smartphone → in PDF umwandeln (gratis-Apps oder www.smallpdf.com)

Anlagen ebenfalls als PDF.

### Schritt 5 — Versenden

1. Loggen Sie sich in MJP ein.
2. "Neue Nachricht" → Empfaenger auswaehlen.
3. Betreff: kurz, klar (z.B. "Klage; Az: ...")
4. Text: kurze Anrede + Hinweis auf Anhang.
5. Anhaenge anfuegen (PDF).
6. Senden.

### Schritt 6 — Quittung speichern

Nach Versand erhalten Sie eine elektronische Quittung. Speichern Sie diese (PDF herunterladen). Das ist Ihr Beweis.

### Schritt 7 — Antworten erhalten

Das Gericht antwortet im MJP. Sie bekommen Email-Benachrichtigung. Loggen Sie sich ein und lesen Sie. Speichern Sie Antworten lokal.

## Worauf Sie besonders achten muessen

- **Dateigroesse**: meist max. 30 MB pro Nachricht. Bei vielen Anhaengen aufteilen.
- **Dateiformate**: PDF, manchmal TIFF. KEIN Word oder JPG direkt.
- **Achten Sie auf Bestaetigung**: keine Bestaetigung = nicht gesendet.
- **Anwendung ist neu**: bei technischen Problemen Hotline 030 oder Mailadresse aus MJP-FAQ.

## Typische Fehler

- Falscher Empfaenger (Sozialgericht der Behoerde statt Wohnort) → Wohnort-SG waehlen
- Datei ohne PDF gesendet → in PDF konvertieren
- Quittung nicht gespeichert → immer speichern als Beweis
- Identifikation klappt nicht → Hotline oder ELSTER-Alternative

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `einreichung-papierform-sozialgericht-mit-abschriften` — Papierform-Alternative
- `einreichung-fax-und-grenzen-sozialgericht` — Fax-Alternative
- `dokumenten-erzeugung-pdf-laien-sozialgericht` — wie PDFs machen
- `klage-zusammenstellen-bundle-sozialgericht` — Schriftsatz mit Anlagen
- `versand-selbst-zurechnung-laien-sozialgericht` — Versand-Beweise

## Quellen und Aktualitaet

Stand: 05/2026. MJP seit 2024 fuer alle Buerger oeffentlich. § 65a SGG fuer elektronische Klage. Bei technischen Problemen: www.mein-justizpostfach.de/hilfe. Funktionalitaet variiert je Bundesland.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `einreichung-papierform-sozialgericht-mit-abschriften`

**Fokus:** Klage und Schriftsatz per Post beim SG einreichen. Abschriften für Gegner und Akte. Adressierung Einschreiben Empfangsbestätigung. Praktischer Versandweg für Buerger.

# Klage per Post einreichen — mit Abschriften

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Klage per Post einreichen — mit Abschriften` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Auch ohne Internet und Fax koennen Sie klagen. Per Post. Dabei muessen Sie aber an Abschriften denken, damit das Gericht den Schriftsatz auch der Gegenseite schicken kann.

## In einfacher Sprache

Sie koennen Ihre Klage per Brief schicken. Das ist immer noch ok. Wichtig: das Gericht braucht den Brief mehrfach. Einmal fuer sich, einmal fuer den Gegner.

## Wann brauchen Sie diese Skill?

- Sie wollen klassisch per Post einreichen.
- Sie haben kein MJP-Konto.
- Sie wollen einen Brief, den Sie anfassen koennen.

## Fachbegriffe (kurz erklaert)

- **Abschrift**: Kopie eines Schriftsatzes fuer die Gegenseite.
- **Original**: Mit Unterschrift versehenes Exemplar fuer das Gericht.
- **Einschreiben mit Rueckschein**: Brief, Empfaenger unterschreibt; Sie bekommen Beleg.
- **Einwurf-Einschreiben**: Brief, Auslieferung wird dokumentiert.

## Rechtsgrundlagen

- **§ 90 SGG** — Klage schriftlich.
- **§ 92 SGG** — Inhalt der Klage.
- **§ 93 SGG** — Abschriften.
- **§ 65a SGG** — Elektronische Alternative (siehe MJP).

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Schriftsatz fertigstellen

Erstellen Sie die Klage am Computer oder schreiben sie sauber per Hand. Unterzeichnen Sie das Original.

### Schritt 2 — Abschriften anfertigen

Pro Beklagter eine Abschrift, plus eine fuer das Gericht (Akte), plus eine fuer Sie:

- Bei 1 beklagter Behoerde: 3 Exemplare (1 Original + 1 fuer Behoerde + 1 fuer Sie)
- Bei 2 beklagten Behoerden: 4 Exemplare

Das Gericht braucht: 1 mit Originalunterschrift + Abschriften zur Zustellung an die Behoerde(n).

Sie machen einfach Kopien (kein Notar oder so noetig). Auf den Abschriften "Abschrift" oben drueber schreiben.

### Schritt 3 — Anlagen ebenfalls in Abschrift

Alle Anlagen einmal fuer das Gericht (Original-Kopie reicht) und einmal je Beklagter.

### Schritt 4 — Versand vorbereiten

- Adresse aus www.sozialgerichtsbarkeit.de
- Umschlag entsprechend gross
- Fragen Sie in der Post nach dem Porto fuer Maxibrief / Paketchen, je nach Umfang.

### Schritt 5 — Versandweg waehlen

- **Einschreiben mit Rueckschein**: sichers, ca. 5,50 EUR
- **Einwurf-Einschreiben**: ca. 4 EUR
- **Persoenliche Abgabe** mit Empfangsstempel: gratis, sicherster Weg
- **Normaler Brief**: vermeiden, kein Beweis

### Schritt 6 — Quittung aufheben

- Einlieferungsschein (mit Sendungsnummer)
- Rueckschein (wenn er zurueckkommt)
- Empfangsstempel auf Ihrer Kopie

Aufheben min. 5 Jahre.

## Worauf Sie besonders achten muessen

- **Original mit Unterschrift** ist Pflicht. Eine Kopie der Unterschrift reicht meist nicht.
- **Abschriften nicht vergessen**: ohne Abschriften kann das Gericht nicht zustellen — und fragt erst nach, was Zeit kostet.
- **Frist sichern**: Bei letzter Tag Versand: pruefen, ob Briefkasten-Leerung am selben Tag erfolgt.

## Typische Fehler

- Nur ein Exemplar geschickt → Gericht muss nachfordern
- Keine Unterschrift auf dem Original → unzulaessig
- Falsche Adresse (LSG statt SG) → Verweisung; Zeitverlust
- Normaler Brief am letzten Tag → riskant

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `einreichung-mein-justizpostfach-mjp-sozialgericht` — digitale Alternative
- `einreichung-fax-und-grenzen-sozialgericht` — Fax
- `anlagen-bezeichnen-und-sortieren-sozialgericht` — Anlagen
- `klage-zusammenstellen-bundle-sozialgericht` — Komplett-Versand
- `versand-selbst-zurechnung-laien-sozialgericht` — Versand-Beweis

## Quellen und Aktualitaet

Stand: 05/2026. § 93 SGG zu Abschriften. Postpreise variieren, aktuell pruefen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
