---
name: gesellschafterliste-aktualisieren
description: "Gesellschafterliste Aktualisieren: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gesellschafterliste Aktualisieren

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Gesellschafterliste Aktualisieren** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschafterliste-aktualisieren` | Gesellschafterliste nach Kapitalerhohung durch Wandlung aktualisieren und beim Handelsregister einreichen. § 40 GmbHG Gesellschafterliste § 16 GmbHG Legitimationswirkung. Prüfraster: neue Gesellschafter Anteile Stammnummern Notar Einreichungsfrist. Output: aktualisierte Gesellschafterliste Einreichungsschreiben. Abgrenzung: nicht für Cap-Table-Kalkulation (cap-table-update-pre-post). |
| `gesellschafterversammlung-einberufen` | Gesellschafterversammlung für Wandeldarlehensmandat einberufen und Tagesordnung aufstellen. §§ 49 51 GmbHG Ladungspflichten. Prüfraster: Ladungsfrist Form Tagesordnung Quorum Vollmachten Protokollpflicht. Output: Einberufungsschreiben Tagesordnung Vollmachtsformular. Abgrenzung: nicht für spezifische Beschlussvorbereitung (gesellschafterbeschluss-vorbereiten). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Gesellschafterliste Aktualisieren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschafterliste-aktualisieren`

**Fokus:** Gesellschafterliste nach Kapitalerhohung durch Wandlung aktualisieren und beim Handelsregister einreichen. § 40 GmbHG Gesellschafterliste § 16 GmbHG Legitimationswirkung. Prüfraster: neue Gesellschafter Anteile Stammnummern Notar Einreichungsfrist. Output: aktualisierte Gesellschafterliste Einreichungsschreiben. Abgrenzung: nicht für Cap-Table-Kalkulation (cap-table-update-pre-post).

# Gesellschafterliste aktualisieren (§ 40 GmbHG)

## Zweck

Dieser Skill erstellt die aktualisierte Gesellschafterliste nach der Kapitalerhöhung und dem Eintritt des Lenders als neuer Gesellschafter. Die Liste wird beim Handelsregister eingereicht. Phase D des Lebenszyklus.

## Eingaben

- Vorherige Gesellschafterliste (aus dem Handelsregister)
- Ergebnis der Kapitalerhöhung (neue Anteile, Nennwert, Gesellschafternummer)
- Vollständige Daten Lender (Name, Geburtsdatum, Anschrift oder Sitz und Vertreter)
- Notar (hat Kapitalerhöhung beurkundet und überreicht normalerweise aktualisierte Liste)
- Datum der Beurkundung und des vorgesehenen Einreichungsdatums

## Rechtlicher Rahmen

### Primärnormen
- § 40 Abs. 1 GmbHG (Geschäftsführerin reicht neue Gesellschafterliste bei Änderung ein; Pflichtinhalte durch DiRUG/Gesellschafterlistenverordnung erweitert: prozentuale Beteiligung am Stammkapital, ggf. Geburtsname, weitere Identifikatoren)
- § 40 Abs. 2 GmbHG (Mitwirkung eines Notars: Notar reicht Liste ein, wenn er an Änderung mitgewirkt hat)
- Gesellschafterlistenverordnung (GesLV, in Kraft 1.7.2018, modifiziert durch DiRUG) — Pflichtinhalte und Format
- § 16 GmbHG (Gutglaubenswirkung der Gesellschafterliste: nur als Gesellschafter gilt, wer eingetragen ist)
- § 15 GmbHG (Anteilsübertragung – Vollwirkung erst mit Eintragung)
- § 19 GwG (Transparenzregister – wirtschaftlich Berechtigte nach Änderung melden; Vollregister seit August 2021)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Listenentwurf erstellen
Alle Gesellschafterinnen und neuer Lender mit vollständigen Angaben gemäß § 40 Abs. 1 GmbHG i.V.m. GesLV:
- Laufende Nummer (fortlaufend, keine Lücken)
- Gesellschaftername (Vor- und Nachname oder Firma); bei natürlichen Personen ggf. Geburtsname, wenn abweichend
- Geburtsdatum (natürliche Person) oder HRB + Amtsgericht (juristische Person)
- Anschrift (Wohnanschrift oder Geschäftsanschrift Sitz)
- Anzahl der Geschäftsanteile und Nennwert (in EUR)
- Prozentuale Beteiligung am Stammkapital (Pflicht seit DiRUG)
- Datum des Erwerbs (Beurkundungsdatum Kapitalerhöhung)

### 2. Vollständigkeitsprüfung
Alle alten Gesellschafterinnen unverändert übernehmen (Anteile, Nennwert). Neuen Lender-Eintrag hinzufügen. Gesamtstammkapital prüfen: Summe aller Nennwerte = neues Stammkapital.

### 3. Einreichung durch Notar (§ 40 Abs. 2 GmbHG)
Da Notar an Kapitalerhöhung mitgewirkt hat, reicht er die neue Liste ein. Frist: unverzüglich nach Beurkundung.

### 4. Gutglaubenswirkung beachten
Ab Einreichung der neuen Liste gilt der Lender als Gesellschafter (§ 16 Abs. 1 GmbHG). Vor Einreichung: kein Stimmrecht, kein Gewinnbezugsrecht, keine HR-Legitimation.

### 5. Transparenzregister aktualisieren (§ 19 GwG)
Falls Lender nach Kapitalerhöhung wirtschaftlich Berechtigter (mehr als 25 %) wird: Meldung an Transparenzregister unverzüglich nach Eintragung ins Handelsregister.

### 6. Kopie an alle Parteien
Aktuelle Gesellschafterliste (nach HR-Eintragung) an Geschäftsführerin, alle Gesellschafterinnen, Lender, Steuerberater. Ablage in Gesellschaftsakte.

## Muster-Gesellschafterliste (Auszug)

```
Gesellschafterliste der Sonnenglas Solartechnologie UG (haftungsbeschränkt)
Berlin, HRB 123456 B, Amtsgericht Charlottenburg
Stand: [Datum nach Kapitalerhöhung]

Nr. | Name | Geburtsdatum / HRB | Anschrift | Anteile | Nennwert EUR | Erwerb
1 | Dr. Mira Schoeneck | [Datum] | [Anschrift] | 40 | 40 | [Gründungsdatum]
2 | Lina Habersaat | [Datum] | [Anschrift] | 35 | 35 | [Gründungsdatum]
3 | [Treasury GmbH] | HRB ●, AG ● | [Anschrift] | 25 | 25 | [Datum]
4 | Northstar Pre-Seed Partners GmbH & Co. KG | HRA 99999, AG Frankfurt | [Anschrift] | 7 | 7 | [Beurkundungsdatum KE]

Gesamt: 107 Anteile, Stammkapital EUR 107
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Liste nicht eingereicht | Lender hat keine Gutglaubensposition | Liste in Erarbeitung | Notar reicht sofort ein |
| Fehlerhafte Anteilszahl | HR-Liste und tatsächliche Beteiligung weichen ab | Kleiner Tippfehler | Exakt korrekt |
| Transparenzregister nicht aktualisiert | GwG-Bußgeld (§ 56 GwG) | Frist läuft | Aktualisierung bestätigt |
| Lender als Gesellschafter ohne HR-Eintragung | Stimmrechte, Gewinnrechte blockiert | Eintragung beantragt | Eintragung erfolgt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/handelsregisteranmeldung-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/post-eintragung-checkliste/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG § 40/§ 16 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, Einreichungspflicht, Haftung des GF) → § 16 GmbHG (Legitimationswirkung, gutgläubiger Erwerb) → § 15 GmbHG (Abtretung Geschäftsanteile) → § 12 HGB i.V.m. FamFG (Handelsregisteranmeldung) → § 57 GmbHG (Anmeldung Kapitalerhöhung)

## 2. `gesellschafterversammlung-einberufen`

**Fokus:** Gesellschafterversammlung für Wandeldarlehensmandat einberufen und Tagesordnung aufstellen. §§ 49 51 GmbHG Ladungspflichten. Prüfraster: Ladungsfrist Form Tagesordnung Quorum Vollmachten Protokollpflicht. Output: Einberufungsschreiben Tagesordnung Vollmachtsformular. Abgrenzung: nicht für spezifische Beschlussvorbereitung (gesellschafterbeschluss-vorbereiten).

# Gesellschafterversammlung einberufen (Kapitalerhöhung)

## Zweck

Dieser Skill leitet die Einberufung der außerordentlichen Gesellschafterversammlung zur Beschlussfassung über die Kapitalerhöhung gegen Sacheinlage (Wandlung Wandeldarlehen) ein. Phase D des Lebenszyklus.

## Eingaben

- Gesellschaft: Firma, Sitz, Geschäftsführerin
- Gesellschafterinnen: Namen, Adressen, Anteilsverhältnisse
- Tagesordnung: Kapitalerhöhung gegen Sacheinlage, Bezugsrechtsverzicht, Übernahme Lender, ggf. Satzungsänderung
- Gewünschtes Versammlungsdatum
- Einberufungsform: Einschreiben, E-Mail oder Vollversammlung ohne Einberufung?
- Notar bereits beauftragt?

## Rechtlicher Rahmen

### Primärnormen
- § 49 GmbHG (Gesellschafterversammlung – Einberufungspflicht der Geschäftsführung)
- § 50 GmbHG (Einberufungsrecht Gesellschafter mit mehr als zehn Prozent)
- § 51 GmbHG (Form und Frist: schriftlich, mindestens eine Woche)
- § 51 Abs. 3 GmbHG (Beschlussfassung ohne Einberufung bei Einverständnis aller Gesellschafter)
- § 53 Abs. 2 GmbHG (Satzungsänderungsbeschluss: notarielle Beurkundung, drei Viertel-Mehrheit)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Einberufungsform wählen
Option A – Schnellweg (§ 51 Abs. 3 GmbHG): Alle Gesellschafterinnen stimmen der Versammlung ohne Einberufung zu und verzichten auf die Ladungsfrist. Nur möglich bei einstimmigem Einverständnis. Option B – Reguläre Einberufung (§ 51): Schriftliche Einladung mindestens eine Woche vorher, Tagesordnung beifügen.

### 2. Einladungsschreiben verfassen
Absender: Geschäftsführerin. Empfänger: alle Gesellschafterinnen. Inhalt: Datum, Uhrzeit, Ort (oder Videokonferenz falls Satzung erlaubt), Tagesordnung vollständig. Hinweis: Notarielle Beurkundung des Beschlusses (§ 53 Abs. 2 GmbHG).

### 3. Tagesordnung formulieren
TOP 1: Kapitalerhöhung des Stammkapitals um EUR [Nennbetrag neue Anteile] gegen Einbringung der Forderung aus Wandeldarlehen Northstar Pre-Seed Partners GmbH & Co. KG als Sacheinlage. TOP 2: Verzicht der Altgesellschafterinnen auf Bezugsrechte. TOP 3: Zulassung des Darlehensgebers als neuer Gesellschafter. TOP 4: Änderung der Gesellschafterliste.

### 4. Notartermin koordinieren
Kapitalerhöhungsbeschluss bedarf notarieller Beurkundung (§ 53 Abs. 2 GmbHG). Notar beurkundet Beschluss und Übernahmeerklärung des Lenders (§ 55 Abs. 2 GmbHG). Termin mindestens zwei Wochen im Voraus buchen.

### 5. Versand der Einladung und Dokumentation
Versand per Einschreiben (Zugangsnachweis) oder per E-Mail wenn Satzung erlaubt. Zustellungsnachweis archivieren.

### 6. Vollmacht
Falls eine Gesellschafterin nicht persönlich erscheinen kann: schriftliche Vollmacht erforderlich (§ 47 Abs. 3 GmbHG). Bevollmächtigte müssen Beschlussfähigkeit herstellen.

## Muster-Einladung (Auszug)

```
[Gesellschaft, Datum]

Einladung zur außerordentlichen Gesellschafterversammlung
der Sonnenglas Solartechnologie UG (haftungsbeschränkt)

Datum: [Datum], [Uhrzeit] Uhr
Ort: Notariatskanzlei [Notar], [Adresse]

Tagesordnung:
TOP 1: Kapitalerhöhung gegen Sacheinlage
TOP 2: Bezugsrechtsverzicht Altgesellschafterinnen
TOP 3: Zulassung Northstar Pre-Seed Partners GmbH & Co. KG als Gesellschafter
TOP 4: Aktualisierung Gesellschafterliste

Hinweis: Die Beschlussfassung zu TOP 1 bis 3 erfordert notarielle Beurkundung.

[Unterschrift Geschäftsführerin]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Einberufungsmangel, Gesellschafterin erhebt Einwand | Beschluss anfechtbar | Heilung durch nachträgliche Zustimmung | Ordnungsgemäße Einberufung |
| Notar nicht rechtzeitig beauftragt | Versammlung ohne Beurkundung | Notar in Suche | Notar bestätigt Termin |
| Tagesordnung unvollständig | Beschluss über nicht angekündigten Punkt anfechtbar | Nachträgliche Ergänzung | Vollständige Tagesordnung |
| Quorum nicht erreicht | Beschluss nicht gefasst | Vertretung unklar | Alle Gesellschafterinnen anwesend/vertreten |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlung-kommunikation-paketverteilung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 49 ff. aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 51 GmbHG (Einberufung Gesellschafterversammlung, Frist 1 Woche) → § 51 Abs. 3 GmbHG (Vollversammlung mit Zustimmung) → § 53 GmbHG (notarielle Beurkundung, vollständige Beschlussangaben) → § 47 Abs. 1 GmbHG (Stimmrecht, Mehrheitserfordernisse)
