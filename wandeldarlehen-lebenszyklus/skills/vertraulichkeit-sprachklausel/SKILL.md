---
name: vertraulichkeit-sprachklausel
description: "Vertraulichkeit Sprachklausel: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vertraulichkeit Sprachklausel

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Vertraulichkeit Sprachklausel** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vertraulichkeit-und-sprachklausel` | Vertraulichkeits- und Sprachklauseln in Wandeldarlehensvertrag prüfen oder formulieren. §§ 307 ff. BGB AGB-Recht § 5 BDSG Datengeheimnis. Prüfraster: Geheimhaltungsumfang Ausnahmen Vertragssprache Kollisionsregel Sprachklausel. Output: Klauselentwuerfe Prüfprotokoll. Abgrenzung: nicht für gesamte Vertragserstellung (einsprachige-vertragsfassung-de). |
| `beurkundungserfordernis-pruefung` | Beurkundungserfordernis für Wandeldarlehen und Kapitalerhohung prüfen wenn Frage besteht ob Notartermin erforderlich ist. §§ 15 55 GmbHG § 311b BGB Formvorschriften. Prüfraster: Sacheinlage Kapitalerhohung GmbH-Anteil Vorratskapital Abtretungsverbot. Output: Formprüfungs-Memo mit Empfehlung. Abgrenzung: nicht für Textform-Fragen (textform-vs-schriftform-vs-notariell). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Vertraulichkeit Sprachklausel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vertraulichkeit-und-sprachklausel`

**Fokus:** Vertraulichkeits- und Sprachklauseln in Wandeldarlehensvertrag prüfen oder formulieren. §§ 307 ff. BGB AGB-Recht § 5 BDSG Datengeheimnis. Prüfraster: Geheimhaltungsumfang Ausnahmen Vertragssprache Kollisionsregel Sprachklausel. Output: Klauselentwuerfe Prüfprotokoll. Abgrenzung: nicht für gesamte Vertragserstellung (einsprachige-vertragsfassung-de).

# Vertraulichkeit und Sprachklausel

## Zweck

Dieser Skill formuliert die Vertraulichkeitsklausel (§ 8) und die Schlussbestimmungen (§ 10) des Wandeldarlehensvertrags: Sprachklausel, Gerichtsstand oder Schiedsklausel, Salvatorische Klausel, Abtretungsverbot, Textformänderung. Phase A des Lebenszyklus.

## Eingaben

- Gewünschte Vertraulichkeitsausnahmen (Standard-Set plus Investoren-Folge-Pitches?)
- Gerichtsstand oder DIS-Schiedsgerichtsklausel (Frankfurt am Main oder Berlin)?
- Schiedsklausel: DIS-Schiedsordnung, Sprache Deutsch, Ort Frankfurt am Main?
- Anwendbares Recht: Deutsches Recht (Standard), CISG ausgeschlossen?
- Abtretungsgenehmigung: Verbundene Unternehmen des Lenders freigestellt?

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform für Vertragsänderungen)
- § 139 BGB (Teilnichtigkeit – wird vollständig abbedungen durch salvatorische Klausel)
- § 398 BGB (Abtretung), § 399 BGB (Abtretungsverbot)
- § 328 BGB (Vertrag zugunsten Dritter)
- Art. 6 Abs. 1 lit. b EuGVVO (Gerichtsstand bei unternehmerischem Vertrag)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Vertraulichkeitsklausel formulieren
Alle Informationen im Zusammenhang mit dem Vertrag (Existenz, Inhalt, Verhandlungen) streng vertraulich. Ausnahmen (erforderlicher Umfang):
a) Mitarbeitende und Beraterinnen mit Verschwiegenheitspflicht (auch Berufsgeheimnis)
b) Verbundene Unternehmen und deren Organe
c) Potenzielle Investoren (Folge-Pitches) nach Unterzeichnung einer marktüblichen NDA
d) Banken und Finanzierungspartner
e) Dritte im Zusammenhang mit Unternehmensveräußerung (NDA + GF-Zustimmung)
f) Gerichte und Schiedsgerichte zu Beweiszwecken
g) Behörden soweit gesetzlich (Steuer, Aufsicht, Strafverfolgung)
h) Hinweisgeberinnen (HinSchG)

### 2. Sprachklausel formulieren
Deutsche Fassung allein verbindlich. Im Widerspruchsfall: DE geht vor EN. Englische Begriffe in Klammern sind verbindliche Bezüge auf deutsche Rechtsbegriffe.

### 3. Gerichtsstand oder Schiedsklausel auswählen
Option A – Staatliches Gericht: Ausschließlicher Gerichtsstand Berlin (oder Gesellschaftssitz).
Option B – DIS-Schiedsklausel: "Alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag werden nach der Deutschen Institution für Schiedsgerichtsbarkeit e.V. (DIS) Schiedsordnung in ihrer jeweils gültigen Fassung endgültig entschieden. Schiedsort ist Frankfurt am Main. Schiedssprache ist Deutsch. Das Schiedsgericht besteht aus einem Schiedsrichter."

### 4. Salvatorische Klausel (§ 139 BGB vollständig abbedingen)
"Es ist ausdrücklicher Wille der Parteien, dass diese salvatorische Klausel nicht lediglich eine Umkehr der Beweislast bewirkt, sondern § 139 BGB insgesamt abbedungen wird."

### 5. Textformerfordernis für Änderungen
"Änderungen und Ergänzungen bedürfen der Textform (§ 126b BGB); das gilt auch für die Änderung dieses Textformerfordernisses. Strengere gesetzliche Formerfordernisse bleiben unberührt."

### 6. Abtretungsreglung
Abtretung an Dritte nur mit vorheriger schriftlicher Zustimmung. Ausnahme: Verbundene Unternehmen und vom Lender verwaltete Fonds ohne Zustimmung.

## Beispielklausel DIS-Schiedsgericht

```
§ 10.7 Anwendbares Recht und Streitbeilegung. Dieser Vertrag unterliegt ausschließlich dem
Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts (CISG) und des
deutschen Kollisionsrechts. Alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag
werden nach der Schiedsordnung der Deutschen Institution für Schiedsgerichtsbarkeit e.V. (DIS)
in ihrer jeweils gültigen Fassung endgültig entschieden. Das Schiedsverfahren findet in
Frankfurt am Main in deutscher Sprache vor einem Einzelschiedsrichter statt.
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Vertraulichkeit ohne Investoren-Ausnahme | Lender kann nicht pitchen | Ausnahme nur mit GF-Zustimmung | Klare Ausnahme |
| Kein Gerichtsstand festgelegt | Mehrere Gerichtsstände möglich | Allgemeiner Gerichtsstand | Ausschließlicher Gerichtsstand |
| § 139 BGB nicht abbedungen | Gesamtvertrag bei Teilnichtigkeit unwirksam | Nur Teilregelung | Vollständige Abbedingung |
| CISG nicht ausgeschlossen | Internationales Kaufrecht könnte greifen | Kaufrechtsausschluss unklar | CISG ausdrücklich ausgeschlossen |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/bilinguale-vertragserstellung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/kyc-aml-geldwaesche/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. DIS-Schiedsordnung 2018. Bei Änderung BGB oder DIS-Schiedsordnung aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 280, 249 BGB (Schadensersatz bei Vertraulichkeitsverletzung) → § 307 BGB (AGB-Kontrolle pauschaler Vertraulichkeitsklauseln) → §§ 203, 204 StGB (strafrechtliche Schweigepflicht bei Berufsgeheimnisträgern) → Art. 3 Nr. 1 GeschGehG (Geheimnisschutz, Definition) → Art. 9, 10 GeschGehG (Ansprüche bei Geheimnisverletzung)

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 171/18 (NJW 2019, 2077) – WRONG_TOPIC; tatsächlich: Anforderungen Berufungsurteil/§ 313 ZPO, kein Vertraulichkeitsbezug.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Quelle: https://dejure.org/2019,11230
-->

## 2. `beurkundungserfordernis-pruefung`

**Fokus:** Beurkundungserfordernis für Wandeldarlehen und Kapitalerhohung prüfen wenn Frage besteht ob Notartermin erforderlich ist. §§ 15 55 GmbHG § 311b BGB Formvorschriften. Prüfraster: Sacheinlage Kapitalerhohung GmbH-Anteil Vorratskapital Abtretungsverbot. Output: Formprüfungs-Memo mit Empfehlung. Abgrenzung: nicht für Textform-Fragen (textform-vs-schriftform-vs-notariell).

# Beurkundungserfordernis-Prüfung

## Zweck

Dieser Skill klärt, ob der Wandeldarlehensvertrag der notariellen Beurkundung bedarf. Kernfrage: Wird bereits jetzt eine Anteilsübertragung vereinbart (beurkundungspflichtig) oder nur eine schuldrechtliche Verpflichtung auf zukünftige Kapitalerhöhung (nicht beurkundungspflichtig in zweistufiger Konstruktion)? Phase B des Lebenszyklus.

## Eingaben

- Vertragsentwurf §§ 4 und 9
- Wandlungsmechanik: einstufig (Abtretung bestehender Anteile) oder zweistufig (Kapitalerhöhung + neue Anteile)?
- Besteht bereits ein Beschluss zur Kapitalerhöhung?
- Soll die Wandlung durch Abtretung bestehender Anteile oder durch Ausgabe neuer Anteile erfolgen?
- Enthalten Term Sheet oder Nebenvereinbarungen Anteilsübertragungen?

## Rechtlicher Rahmen

### Primärnormen
- § 15 Abs. 3 GmbHG (Beurkundungspflicht Verpflichtung zur Anteilsübertragung)
- § 15 Abs. 4 GmbHG (Beurkundungspflicht Anteilsübertragung selbst)
- § 55 Abs. 1 GmbHG (Kapitalerhöhungsbeschluss – notarielle Beurkundung gemäß § 53 Abs. 2 GmbHG)
- § 53 Abs. 2 GmbHG (Satzungsänderung durch Kapitalerhöhung – notariell)
- § 2 Abs. 3 GmbHG (Online-Beurkundung Gründung; durch DiRUG 2022 eingeführt, BeurkG § 16a)
- § 53 Abs. 4 GmbHG analog / BeurkG § 16a (Online-Beurkundung Kapitalerhöhung seit 1.8.2023 zulässig)
- § 311 Abs. 1 BGB (Schuldrechtliche Verpflichtung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Konstruktion des Wandlungsmechanismus prüfen
Einstufige Konstruktion: Lender tritt in bestehende Anteile ein (Abtretung § 15 Abs. 3 GmbHG → Beurkundungspflicht für den Verpflichtungsvertrag). Zweistufige Konstruktion: Lender erhält neue Anteile durch Kapitalerhöhung → schuldrechtliche Verpflichtung im Wandeldarlehensvertrag nicht beurkundungspflichtig; Beurkundungspflicht tritt erst bei Kapitalerhöhungsbeschluss (§ 53 Abs. 2 GmbHG) und Übernahme (§ 55 Abs. 2 GmbHG) ein.

### 2. Formulierung im Vertrag prüfen
Enthält § 4 eine unbedingte oder bedingte Pflicht zur Abtretung bestehender Anteile? → Beurkundungspflichtig. Enthält § 4 nur die Verpflichtung, bei Eintritt eines Wandlungsereignisses eine Kapitalerhöhung durchzuführen und neue Anteile auszugeben? → Nicht beurkundungspflichtig (herrschende Meinung).

### 3. Term Sheet und Nebenabreden
Alle Dokumente prüfen: Term Sheet, Gesellschaftervertrag, Investorenvereinbarung. Falls dort Anteilsabtretungen vereinbart sind: Formpflicht auf diese Dokumente ausdehnen.

### 4. Heilungsklausel prüfen
§ 9.3 Standard: Falls entgegen Annahme Beurkundungspflicht entsteht, verpflichten sich Parteien zur unverzüglichen notariellen Beurkundung. Kosten trägt die Gesellschaft. Bis zur Beurkundung wirtschaftliche Gleichstellung (§ 9.4).

### 5. Ergebnis dokumentieren
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Trennungsprinzip sicherstellen
Verpflichtungs- und Verfügungsebene sauber getrennt halten. Keine Formulierungen im Wandeldarlehensvertrag, die einen Direkterwerb bestehender Anteile ohne Kapitalerhöhung vorsehen.

### 7. Online-Beurkundung als Option prüfen (DiRUG/DiREG)
- Seit DiRUG (BGBl. I 2021, 3338; in Kraft 01.08.2022) ist Online-Beurkundung der GmbH-Bargruendung moeglich (§ 2 Abs. 3 GmbHG; § 16a BeurkG).
- Durch DiREG (Gesetz zur Ergaenzung der Regelungen zur Umsetzung der Digitalisierungsrichtlinie) ist seit 01.08.2023 die Online-Beurkundung erweitert auf: GmbH-Sachgruendung, GmbH-Satzungsaenderungen einschliesslich Kapitalmassnahmen, Uebernahmeerklaerungen bei Kapitalerhoehung, sowie Online-Beglaubigung fuer Vereinsregister-Anmeldungen. Wichtig: nicht-einstimmige Mehrheitsbeschluesse sind weiter physisch zu beurkunden (kein Online-Verfahren).
- Mit Lender im Ausland: Online-Beurkundung kann Reise- und Apostille-Aufwand sparen. Voraussetzung: Notar mit Online-Verfahren der Bundesnotarkammer (BNotK); elektronische Identifizierung via eID-Funktion oder Lichtbildausweis-Abgleich.
- Quelle: BMJ-Pressemitteilung https://www.bmjv.de/SharedDocs/Pressemitteilungen/DE/2022/0729_DIREG_DIRUG.html ; § 16a BeurkG https://www.gesetze-im-internet.de/beurkg/__16a.html

## Checkliste Beurkundungserfordernis

| Kriterium | Prüfung | Ergebnis |
|---|---|---|
| Wandlung durch neue Anteile (Kapitalerhöhung)? | ja/nein | nein → nicht beurkundungspflichtig |
| Wandlung durch Abtretung bestehender Anteile? | ja/nein | ja → beurkundungspflichtig |
| Term Sheet enthält Anteilsübertragung? | ja/nein | ja → Formprüfung |
| Heilungsklausel im Vertrag vorhanden? | ja/nein | nein → ergänzen |
| Kapitalerhöhungsbeschluss später notariell? | ja/nein | ja → Standard |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Einstufige Abtretung ohne Beurkundung | Vertrag formnichtig § 125 BGB | Unsicherheit über Konstruktion | Zweistufige Kapitalerhöhung |
| Term Sheet mit Anteilsabtretung | Formverstoß | Term Sheet unklar | Term Sheet ohne Abtretung |
| Keine Heilungsklausel | Heilung unmöglich ohne Beurkundung | Klausel unvollständig | Vollständige Heilungsklausel |
| Kapitalerhöhungsbeschluss ohne Notar | Eintragung Handelsregister scheitert | Notar noch nicht beauftragt | Notar bereits beauftragt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/textform-vs-schriftform-vs-notariell/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen und Updates

Stand: 05/2026.
- § 15 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__15.html
- § 53 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__53.html
- § 55 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__55.html
- § 2 III GmbHG (Online-Bargruendung seit 01.08.2022): https://www.gesetze-im-internet.de/gmbhg/__2.html
- § 16a BeurkG: https://www.gesetze-im-internet.de/beurkg/__16a.html
- DiRUG (BGBl. I 2021, 3338): https://www.bgbl.de/xaver/bgbl/start.xav?startbk=Bundesanzeiger_BGBl&start=//*[@attr_id=%27bgbl121s3338.pdf%27]
- DiREG-Inkrafttreten 01.08.2023 (Erweiterung Online-Verfahren auf Sachgruendung, Satzungsaenderungen, Kapitalerhoehung): https://www.bmjv.de/SharedDocs/Pressemitteilungen/DE/2022/0729_DIREG_DIRUG.html
- § 19 IV GmbHG (Aufrechnung Stammeinlage gegen Gesellschafterforderung; Hinweis: Erleichterungen durch MoMiG seit 2008, Beleg fuer Wandlung als Sacheinlage wegen Konfusion ueblich): https://www.gesetze-im-internet.de/gmbhg/__19.html
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
