---
name: long-covid-akteneinsicht-anfordern-auswerten
description: "Long Covid Akteneinsicht Anfordern Auswerten im Plugin Fachanwalt Sozialrecht: prüft konkret Long-Covid, Krankengeld und Aussteuerung, Mandant oder Anwalt benoetigt Einsicht in die, Anwalt hat Sozialrechts-Verwaltungs- oder Gerichtsakte. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Long Covid Akteneinsicht Anfordern Auswerten

## Arbeitsbereich

**Long Covid Akteneinsicht Anfordern Auswerten** ordnet den Fall über die tragenden Prüfungslinien: Long-Covid, Krankengeld und Aussteuerung, Mandant oder Anwalt benoetigt Einsicht in die. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `long-covid-krankengeld-aussteuerung-nahtlosigkeit` | Long-Covid, Krankengeld und Aussteuerung: Arbeitsunfähigkeit, MD-Prüfung, Nahtlosigkeit, Reha-Antrag und Übergang in EM-Rente.; Normanker: SGB V §§ 44 ff.; SGB III § 145; SGB VI Reha/EM-Rente; fragt medizinische Funktionsfolgen, Beweisstand, Gutachtenangriff und sozialrechtlichen Leistungsweg konkret ab. |
| `akteneinsicht-anfordern` | Mandant oder Anwalt benoetigt Einsicht in die Verwaltungsakte oder Gerichtsakte in einem laufenden Sozialrechtsverfahren. § 25 SGB X Akteneinsicht Verwaltungsverfahren § 120 SGG gerichtliches Verfahren Art. 15 DSGVO ergaenzend. Prüfraster: Antragsgegner (Behörde oder Sozialgericht) Vorgangsbezeichnung vollständige Akte inkl. medizinische Gutachten Aktennotizen Sachverständigenstellungnahmen. Versand beA. Vorgehen bei Verweigerung oder Schwaerzung. Output: Akteneinsichtsantrag fertig zum Versand. Abgrenzung zu akteneinsicht-auswerten (nach Erhalt der Akte). |
| `akteneinsicht-auswerten` | Anwalt hat Sozialrechts-Verwaltungs- oder Gerichtsakte erhalten und muss diese systematisch für Widerspruch oder Klage auswerten. § 25 SGB X § 120 SGG. Prüfraster: chronologische Sichtung Identifikation entscheidungserheblicher Aktenstuecke Widersprueche zwischen Aktenteilen Beweislage. Output: Aktenchronik Aktenliste mit Bewertung pro Eintrag (entscheidend/hilfreich/neutral/belastend) und Prüfkatalog für Folgeschriftsatz. Abgrenzung zu akteneinsicht-anfordern (Antrag) und bescheidanalyse (Bescheid-Fokus). |
| `anlagen-erstellen` | Anwalt muss Anlagenkonvolut zu Widerspruch Klage oder Schriftsatz in korrekter juristischer Konvention erstellen. Anlagenanhaenge Sozialrecht K1/W1/A1-Konvention. Prüfraster: Sigel Bezeichnung Quelle Datum Seitenzahl Bezug im Text. Erzeugt Anlagenverzeichnis und prüft Vollständigkeit jede Anlage muss im Text zitiert sein. Output: Anlagenverzeichnis als Vorblatt mit korrekter Nummerierung. Abgrenzung zu akteneinsicht-auswerten (Aktensichtung) und normenkontrollantrag-schriftsatz in anderen Plugins. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGG §§ 51, 78, 87, 90, 130a, 144, 160, 183, 193, SGB I, II, III, V, VI, IX, X; § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch; § 84 SGG Klage; § 87 SGG Eilantrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `long-covid-krankengeld-aussteuerung-nahtlosigkeit`

**Fokus:** Long-Covid, Krankengeld und Aussteuerung: Arbeitsunfähigkeit, MD-Prüfung, Nahtlosigkeit, Reha-Antrag und Übergang in EM-Rente.; Normanker: SGB V §§ 44 ff.; SGB III § 145; SGB VI Reha/EM-Rente; fragt medizinische Funktionsfolgen, Beweisstand, Gutachtenangriff und sozialrechtlichen Leistungsweg konkret ab.

### Long-Covid, Krankengeld und Aussteuerung: Arbeitsunfähigkeit, MD-Prüfung, Nahtlosigkeit, Reha-Antrag und Übergang in EM-Rente.

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Long-Covid, Krankengeld und Aussteuerung: Arbeitsunfähigkeit, MD-Prüfung, Nahtlosigkeit, Reha-Antrag und Übergang in EM-` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Auftrag

Dieser Skill prüft Long-Covid/Post-Covid nicht als Schlagwort, sondern als sozialrechtliche Funktions- und Beweisfrage. Entscheidend sind Leistungsvermögen, Teilhabe, Kausalität, Dauer, objektivierbare Befunde, konsistente Alltagsschilderung und verwertbare ärztliche Unterlagen.

## Norm- und Quellenanker

SGB V §§ 44 ff.; SGB III § 145; SGB VI Reha/EM-Rente. Medizinisch ist der aktuelle Stand anhand frei zugänglicher Leitlinien und ärztlicher Unterlagen zu prüfen; rechtlich zählt die konkrete Funktionsbeeinträchtigung, nicht ein bloßer Diagnosezettel.

## Arbeitsfragen

1. Welches Leistungsziel: Erwerbsminderungsrente, GdB/Merkzeichen, Krankengeld, BG-Verletztenrente, Reha, Teilhabe, Hilfsmittel oder Schule?
2. Welche Symptome sind funktionell relevant: Fatigue, PEM, Belastungsintoleranz, Dyspnoe, kognitive Defizite, Schmerzen, Schlaf, Kreislauf, Geruch/Geschmack?
3. Was ist objektiv dokumentiert: Arztberichte, Reha, Labor/Bildgebung, neuropsychologische Tests, Belastungsprotokoll, Fremdanamnese?
4. Welche Gutachtenfehler liegen vor: Momentaufnahme, fehlende PEM-Prüfung, falsche psychisch/somatisch-Verengung, keine Alltagstransfers?
5. Welche Fristen laufen: Widerspruch, Klage, Eilverfahren, Nahtlosigkeit, Krankengeld-Aussteuerung?

## Ausgabe

Erzeuge eine Beweismatrix, einen Fragenkatalog für Ärztinnen/Gutachter, einen Widerspruchsbaustein, eine Klagebegründung oder eine laienverständliche Unterlagenliste.

## 2. `akteneinsicht-anfordern`

**Fokus:** Mandant oder Anwalt benoetigt Einsicht in die Verwaltungsakte oder Gerichtsakte in einem laufenden Sozialrechtsverfahren. § 25 SGB X Akteneinsicht Verwaltungsverfahren § 120 SGG gerichtliches Verfahren Art. 15 DSGVO ergaenzend. Prüfraster: Antragsgegner (Behörde oder Sozialgericht) Vorgangsbezeichnung vollständige Akte inkl. medizinische Gutachten Aktennotizen Sachverständigenstellungnahmen. Versand beA. Vorgehen bei Verweigerung oder Schwaerzung. Output: Akteneinsichtsantrag fertig zum Versand. Abgrenzung zu akteneinsicht-auswerten (nach Erhalt der Akte).

### Akteneinsicht anfordern

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Akteneinsicht anfordern` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Akteneinsicht anfordern

- **Spezialfrage (Akteneinsicht anfordern):** Antragsgegner (Behörde oder Sozialgericht) Vorgangsbezeichnung vollständige Akte inkl. medizinische Gutachten Aktennotizen Sachverständigenstellungnahmen. Versand beA. Vorgehen bei Verweigerung oder Schwaerzung. Output: Akteneinsichtsantrag fertig zum Versand. Abgrenzung zu akteneinsicht-auswerten (nach Erhalt der Akte).
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtsgrundlagen

- **§ 25 SGB X** — Akteneinsicht im Verwaltungsverfahren. Anspruch der Beteiligten in die das Verfahren betreffenden Akten.
- **§ 120 SGG** — Akteneinsicht im gerichtlichen Verfahren.
- **Art. 15 DSGVO** — Auskunftsrecht in eigene personenbezogene Daten (ergänzend).
- **§ 83 SGB X** — Auskunft des Sozialleistungsträgers an Betroffene.

## Antragsschritte

### Vor dem Bescheid (während Verfahren)

- § 25 SGB X: bei laufendem Verwaltungsverfahren. Akteneinsicht in die das Verfahren betreffenden Akten am Ort der Aktenführung oder über Abschriften.
- Bei medizinischen Gutachten in der Akte: ergänzender Anspruch aus § 25 SGB X auf vollständige Einsicht.

### Nach Widerspruch (im Vorverfahren)

- Pflichtschritt vor Widerspruchsbegründung. Ohne Akteneinsicht keine fundierte Widerspruchsbegründung.
- Vorlage der vollständigen Akte mit allen Gutachten Notizen Aktenvermerken Stellungnahmen.

### Im Klageverfahren

- § 120 SGG: Antrag beim Sozialgericht auf Beiziehung der Verwaltungsakte und Akteneinsicht in die Gerichtsakte.
- Beiziehung erfolgt regelmäßig von Amts wegen (§ 119 SGG iVm § 103 SGG Untersuchungsgrundsatz).

## Antragsmuster

```
An die Beklagte / das Sozialgericht XYZ

In dem Verfahren ...
gegen ...
Az ...

beantrage ich namens und im Auftrag des / der Klagepartei
Akteneinsicht in die vollständige Verwaltungsakte gemäß § 25 SGB X
(bzw. § 120 SGG iVm § 119 SGG) einschließlich
- aller Aktenvermerke
- saemtlicher medizinischer Gutachten und Stellungnahmen
- aller Aktenbestandteile zu vorangegangenen Verfahren soweit sie für das streitige Verfahren bedeutsam sind.

Versand der Akte digital über beA-Nachricht oder als Kopie an die Kanzleianschrift.
```

## Verweigerung oder Schwaerzung

- **Schutzwürdige Belange Dritter** (§ 25 Abs. 3 SGB X) — Behörde kann teilweise Akteneinsicht verweigern. Vertrauliche Behandlung von Drittinteressen.
- **Geheimnisse von Privatpersonen** (§ 25 Abs. 2 SGB X) — soweit erforderlich Schwaerzung.
- **Reaktion** bei umfangreicher Schwaerzung: Anforderung einer Begründung; ggf. Verfahren über § 86b SGG bei Eilbedürftigkeit.

## Frist

- Behörde soll unverzueglich Akteneinsicht gewähren — keine gesetzliche Frist.
- Im Klageverfahren: regelmäßig binnen weniger Wochen.

## Ausgabe

- `akteneinsichtsantrag-<az>-<datum>.docx`.
- Eintrag im Posteingang nach Eingang der Akte.
- Erinnerung bei Verzoegerung (zwei Wochen Nachfrage).

## Folgeschritt

Nach Eingang der Akte: Skill `akteneinsicht-auswerten`.

## 3. `akteneinsicht-auswerten`

**Fokus:** Anwalt hat Sozialrechts-Verwaltungs- oder Gerichtsakte erhalten und muss diese systematisch für Widerspruch oder Klage auswerten. § 25 SGB X § 120 SGG. Prüfraster: chronologische Sichtung Identifikation entscheidungserheblicher Aktenstuecke Widersprueche zwischen Aktenteilen Beweislage. Output: Aktenchronik Aktenliste mit Bewertung pro Eintrag (entscheidend/hilfreich/neutral/belastend) und Prüfkatalog für Folgeschriftsatz. Abgrenzung zu akteneinsicht-anfordern (Antrag) und bescheidanalyse (Bescheid-Fokus).

### Akteneinsicht auswerten

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Akteneinsicht auswerten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Akteneinsicht auswerten

- **Spezialfrage (Akteneinsicht auswerten):** chronologische Sichtung Identifikation entscheidungserheblicher Aktenstuecke Widersprueche zwischen Aktenteilen Beweislage. Output: Aktenchronik Aktenliste mit Bewertung pro Eintrag (entscheidend/hilfreich/neutral/belastend) und Prüfkatalog für Folgeschriftsatz. Abgrenzung zu akteneinsicht-anfordern (Antrag) und bescheidanalyse (Bescheid-Fokus).
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Zweck

Aus einer eingegangenen Akte rasch das Entscheidungserhebliche herausziehen. Was sagt die Akte was die Behörde im Bescheid weggelassen oder anders dargestellt hat?

## Eingabe

- Vollständige Verwaltungsakte (PDF; ggf. gescannt mit OCR).
- Bisheriges Analyseprotokoll aus `bescheidanalyse`.

## Ablauf

### 1. Inventarisierung

Jeder Aktenteil mit:
- laufender Nummer
- Datum
- Verfasser / Quelle
- Typ (Antrag / Bescheid / Gutachten / Vermerk / Stellungnahme / Schreiben Dritter / Beleg)
- Seitenanzahl
- Prüfer-Flag falls schlecht lesbar oder geschwaerzt

### 2. Chronologische Aktenchronik

Tabelle nach Datum sortiert mit Kurzinhalt — eine Zeile pro Aktenteil.

### 3. Inhaltsbewertung pro Aktenteil

Pro Aktenteil eine Klassifizierung:
- **entscheidend** — trägt das Ergebnis (entweder für oder gegen den Mandanten)
- **hilfreich** — stuetzt unsere Argumentation
- **neutral** — Sachverhaltsdokumentation ohne Wertung
- **belastend** — stuetzt die Behördenentscheidung
- **lücke** — verweist auf Vorgang der nicht in der Akte ist

### 4. Widerspruchsprüfung

- **Bescheid vs Aktenstand** — sagt der Bescheid Dinge die in der Akte anders stehen?
- **Verfahrensvermerke** — wurde die Anhörung geführt aktenkundig?
- **Medizinische Gutachten** — sind sie schlüssig nachvollziehbar? Wurden Befunde aus Arztbriefen überhaupt zur Kenntnis genommen?
- **Ermittlungsumfang** — hat die Behörde alles erhoben was sie hätte erheben müssen (§ 20 SGB X)?
- **Datenherkunft** — woher hat die Behörde Drittauskuenfte und durfte sie diese erheben?

### 5. Folge-Prüfkatalog

Für den nächsten Schriftsatz:
- Welche Aktenstücke zitieren wir mit Pinpoint (Seite Absatz)?
- Welche Aktenstücke widerlegen die Bescheidbegründung?
- Wo brauchen wir eine Stellungnahme des Mandanten?
- Wo brauchen wir ein eigenes Privatgutachten zur Untermauerung?
- Welche Beweisanträge könnten wir im Klageverfahren stellen?

## Ausgabe

- `aktenchronik-<mandat>.md` mit Chronik und Bewertung.
- `aktenpruefliste-<mandat>.md` mit Prüfer-Flags zur Klärung mit Mandant.
- Vorlage `schriftsatzbausteine-<mandat>.md` mit zitierfähigen Pinpoint-Verweisen aus der Akte für den Folgeschriftsatz.

## Hinweis zur Vertraulichkeit

Verwaltungs- und Sozialakten enthalten besonders sensible Daten (Gesundheit Sozialleistungen Vermögen). Verarbeitung nur in Tools mit AVV. Mandantenakte unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/sozialrecht-kanzlei/mandate/<az>/` ablegen.

## 4. `anlagen-erstellen`

**Fokus:** Anwalt muss Anlagenkonvolut zu Widerspruch Klage oder Schriftsatz in korrekter juristischer Konvention erstellen. Anlagenanhaenge Sozialrecht K1/W1/A1-Konvention. Prüfraster: Sigel Bezeichnung Quelle Datum Seitenzahl Bezug im Text. Erzeugt Anlagenverzeichnis und prüft Vollständigkeit jede Anlage muss im Text zitiert sein. Output: Anlagenverzeichnis als Vorblatt mit korrekter Nummerierung. Abgrenzung zu akteneinsicht-auswerten (Aktensichtung) und normenkontrollantrag-schriftsatz in anderen Plugins.

### Anlagen erstellen

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anlagen erstellen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Anlagen erstellen

- **Spezialfrage (Anlagen erstellen):** Sigel Bezeichnung Quelle Datum Seitenzahl Bezug im Text. Erzeugt Anlagenverzeichnis und prüft Vollständigkeit jede Anlage muss im Text zitiert sein. Output: Anlagenverzeichnis als Vorblatt mit korrekter Nummerierung. Abgrenzung zu akteneinsicht-auswerten (Aktensichtung) und normenkontrollantrag-schriftsatz in anderen Plugins.
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Konvention

| Verfahrensart | Sigel-Praefix |
|---|---|
| Klage zum Sozialgericht | `K1`, `K2`, ... |
| Widerspruch | `W1`, `W2`, ... |
| Eilantrag | `E1`, `E2`, ... |
| Beweisantrag im Verfahren | `B1`, `B2`, ... |
| Allgemeines Anlagenkonvolut | `A1`, `A2`, ... |

## Eingaben

- Schriftsatz im Entwurf (aus `widerspruch-formulieren` `klage-sozialgericht` `eilantrag-sozialrecht`).
- Originaldokumente (PDF Foto Scan).

## Ablauf

### 1. Anlagenliste erstellen

Pro Anlage:
- **Sigel** (K1 W1 ...)
- **Kurzbezeichnung** ("Bescheid des Jobcenters vom 12.03.2026")
- **Quelle** (Mandant Behörde Drittstelle)
- **Datum** des Originaldokuments
- **Seitenzahl** im Original
- **Fundstelle im Schriftsatz** (z. B. "Seite 4 Randnummer 12")

### 2. PDF-Anlagen vorbereiten

- Original als PDF ablegen.
- Stempel oben rechts auf erste Seite jeder Anlage: das Sigel (`K1`).
- Doppelseitige Scans prüfen.
- Persönliche Daten Dritter schwaerzen wenn nicht erforderlich (DSGVO Datenminimierung).

### 3. Anlagenverzeichnis als Vorblatt

Vorblatt zur Klage- oder Widerspruchsakte:

```
Anlagenverzeichnis

K1 Bescheid des Jobcenters XYZ vom 12.03.2026
K2 Widerspruch vom 05.04.2026
K3 Widerspruchsbescheid vom 18.07.2026
K4 Schwerbehindertenausweis vom 14.11.2024 (GdB 70)
K5 Aerztliches Attest Dr. M. vom 03.02.2026
K6 Mietvertrag mit Anlagen
```

### 4. Vollständigkeitsprüfung

- Wird jede Anlage im Schriftsatz zitiert? Andernfalls Anlage streichen oder Schriftsatz ergänzen.
- Wird jedes Sigel im Schriftsatz auf das richtige Anlagedokument verweisen?
- Reichen die Anlagen aus um die Behauptungen glaubhaft zu machen / zu beweisen?

### 5. Anlagenkonvolut zusammenstellen

- Alle Anlagen in Reihenfolge K1 K2 K3 ... in eine PDF-Datei.
- Lesezeichen pro Anlage für schnelle Navigation.
- Endgültige Dateibenennung: `klage-anlagen-<az>-<datum>.pdf`.

## Ausgabe

- `anlagenverzeichnis-<az>.md`
- `anlagenkonvolut-<az>.pdf` mit Lesezeichen und Sigel-Stempeln
- Eintrag im Postausgang verlinkt mit dem Schriftsatz

## Versand

Vor Versand der Skill `versand-vor-check` aus dem Plugin `kanzlei-allgemein`.
