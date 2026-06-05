---
name: gesellschafterbeschluss-kapitalerhoehung
description: "Gesellschafterbeschluss Kapitalerhoehung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gesellschafterbeschluss Kapitalerhoehung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Gesellschafterbeschluss Kapitalerhoehung** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschafterbeschluss-kapitalerhoehung` | Gesellschafterbeschluss für Kapitalerhohung nach Wandlung vorbereiten. §§ 53 55 56 GmbHG Kapitalerhohung. Prüfraster: Beschlussinhalt Mehrheitserfordernisse notarielle Form neues Stammkapital Einlagepflicht Handelsregistereintrag. Output: Beschlussentwurf Ladungsunterlagen. Abgrenzung: nicht für allgemeine Gesellschafterversammlung (gesellschafterversammlung-einberufen). |
| `gesellschafterbeschluss-vorbereiten` | Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten. §§ 46 53 GmbHG Gesellschafterbeschluesse. Prüfraster: Beschlussgegenstand Mehrheiten Ladungspflicht Form Anlagen. Output: Beschlussentwurf Sitzungsprotokoll. Abgrenzung: nicht für Beschluss zur Kapitalerhohung nach Wandlung (gesellschafterbeschluss-kapitalerhoehung). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Gesellschafterbeschluss Kapitalerhoehung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschafterbeschluss-kapitalerhoehung`

**Fokus:** Gesellschafterbeschluss für Kapitalerhohung nach Wandlung vorbereiten. §§ 53 55 56 GmbHG Kapitalerhohung. Prüfraster: Beschlussinhalt Mehrheitserfordernisse notarielle Form neues Stammkapital Einlagepflicht Handelsregistereintrag. Output: Beschlussentwurf Ladungsunterlagen. Abgrenzung: nicht für allgemeine Gesellschafterversammlung (gesellschafterversammlung-einberufen).

# Gesellschafterbeschluss – Kapitalerhöhung gegen Sacheinlage

## Zweck

Dieser Skill erstellt den notariell beurkundungspflichtigen Gesellschafterbeschluss über die Kapitalerhöhung gegen Sacheinlage (Wandlung des Wandeldarlehens). Phase D des Lebenszyklus.

## Eingaben

- Wandlungsberechnung (neue Anteile, Nennbetrag, Wandlungssumme) aus `wandlungspreis-berechnung`
- Lender (Name, Anschrift, Vertreter)
- Stammkapital vor und nach Kapitalerhöhung
- Sacheinlage: Forderung aus Wandeldarlehen (Betrag gesamt)
- Notar: Name, Amtssitz
- Sacheinlagebericht (Entwurf, aus `sacheinlagebericht-werthaltigkeit`)

## Rechtlicher Rahmen

### Primärnormen
- § 53 Abs. 2 GmbHG (Satzungsänderung durch Gesellschafterbeschluss – drei Viertel-Mehrheit, notarielle Beurkundung)
- § 55 Abs. 1 GmbHG (Kapitalerhöhungsbeschluss – Zulassung neuer Gesellschafter)
- § 55 Abs. 2 GmbHG (Übernahmeerklärung des neuen Gesellschafters – notarielle Beurkundung)
- § 56 GmbHG (Sacheinlage: Leistung vor Anmeldung zum Handelsregister)
- § 56a GmbHG (Sachgründungsbericht / Sacheinlagebericht)
- § 9 GmbHG (Differenzhaftung bei Überbewertung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Beschlussstruktur festlegen
Notarielle Beurkundung (§ 53 Abs. 2 GmbHG) zwingend. Beschlussinhalt: (a) Kapitalerhöhung, (b) Ausschluss Bezugsrecht, (c) Zulassung Lender, (d) Satzungsänderung. Gleichzeitig: Übernahmeerklärung des Lenders (§ 55 Abs. 2 GmbHG) – auch notariell.

### 2. Beschlusstext ausarbeiten
"Die Gesellschafterinnen beschließen mit der erforderlichen Mehrheit von drei Vierteln der abgegebenen Stimmen die Erhöhung des Stammkapitals der Gesellschaft von EUR [alt] um EUR [Erhöhungsbetrag] auf EUR [neu] durch Ausgabe von [Anzahl] neuen Geschäftsanteilen mit einem Nennbetrag von je EUR 1,00 gegen Einbringung der Forderung aus dem Wandeldarlehensvertrag vom [Datum] in Höhe von EUR [Wandlungssumme] als Sacheinlage."

### 3. Bezugsrechtsverzicht formulieren
"Die Altgesellschafterinnen verzichten hiermit auf ihr Bezugsrecht an den neuen Geschäftsanteilen und stimmen der Zulassung von [Lender] zur Übernahme der neuen Geschäftsanteile zu."

### 4. Übernahmeerklärung Lender (§ 55 Abs. 2 GmbHG)
Lender erklärt notariell die Übernahme der neuen Geschäftsanteile gegen Einbringung der Forderung. Gleichzeitig: Abtretung der Forderung an die Gesellschaft (Konfusion) oder Verzicht (§ 4.8 WDV).

### 5. Sacheinlagebericht beifügen
Werthaltigkeitsnachweis der einzubringenden Forderung (aus `sacheinlagebericht-werthaltigkeit`). Bewertungsgrundlage, Bilanzwert, ggf. Gutachten.

### 6. Anmeldung zum Handelsregister vorbereiten
Notar erstellt Anmeldung der Kapitalerhöhung (§ 57 GmbHG). Unterlagen: Beschluss, Übernahmeerklärung, Sacheinlagebericht, neue Gesellschafterliste, Leistungsnachweis (§ 56 GmbHG).

## Muster-Beschluss (Kern)

```
TOP 1: Kapitalerhöhung gegen Sacheinlage

Die Gesellschafterversammlung der Sonnenglas Solartechnologie UG (haftungsbeschränkt)
beschließt einstimmig:

1. Das Stammkapital der Gesellschaft wird von EUR 100 um EUR 7 auf EUR 107 erhöht
 durch Ausgabe von 7 neuen Geschäftsanteilen mit einem Nennbetrag von je EUR 1,00.

2. Die neuen Geschäftsanteile werden gegen Einbringung der Forderung der Northstar
 Pre-Seed Partners GmbH & Co. KG aus dem Wandeldarlehensvertrag vom [Datum]
 in Höhe von EUR 275694 als Sacheinlage ausgegeben.

3. Die Altgesellschafterinnen verzichten auf ihr Bezugsrecht.

4. Northstar Pre-Seed Partners GmbH & Co. KG wird zur Übernahme der 7 neuen
 Geschäftsanteile zugelassen.

[Notarielle Beurkundung durch Notar [●], [Datum]]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Keine notarielle Beurkundung | Beschluss unwirksam, HR-Eintragung scheitert | Notar noch nicht beauftragt | Notar bestätigt Beurkundung |
| Bezugsrechtsverzicht fehlt | Altgesellschafterinnen könnten neue Anteile beanspruchen | Verzicht nachzureichen | Verzicht im Beschluss |
| Sacheinlagebericht fehlt | Differenzhaftungsrisiko § 9 GmbHG | Bericht in Erarbeitung | Bericht vollständig |
| Wandlungssumme fehlerhaft | Beschluss und Kapitalerhöhung inkonsistent | Kleiner Rechenfehler | Exakter Betrag |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/sacheinlagebericht-werthaltigkeit/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterliste-aktualisieren/SKILL.md`

## Quellen und Updates

Stand: 05/2026.
- § 53 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__53.html
- § 55 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__55.html
- § 56 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__56.html
- § 56a GmbHG: https://www.gesetze-im-internet.de/gmbhg/__56a.html
- § 57 GmbHG (Anmeldung): https://www.gesetze-im-internet.de/gmbhg/__57.html
- § 57a GmbHG (i.V.m. § 9c GmbHG): https://www.gesetze-im-internet.de/gmbhg/__57a.html
- § 9 GmbHG (Differenzhaftung): https://www.gesetze-im-internet.de/gmbhg/__9.html
- DiREG-Inkrafttreten 01.08.2023 (Online-Beurkundung GmbH-Kapitalerhoehung und Uebernahmeerklaerung): https://www.bmjv.de/SharedDocs/Pressemitteilungen/DE/2022/0729_DIREG_DIRUG.html — Vorbehalt: nur bei einstimmigem Gesellschafterbeschluss; bei Mehrheitsentscheid Praesenzbeurkundung.
- Bei Aenderung GmbHG §§ 53 ff. aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 53, 54 GmbHG (Satzungsänderung, notarielle Beurkundung) → § 55 GmbHG (Kapitalerhöhung durch Gesellschafterbeschluss) → § 56 GmbHG (Sacheinlage, Werthaltigkeitsprüfung) → § 57 GmbHG (Anmeldung zum Handelsregister) → § 57a GmbHG (vereinfachte Kapitalerhöhung) → § 47 GmbHG (Mehrheitserfordernisse, Stimmverbote)

## 2. `gesellschafterbeschluss-vorbereiten`

**Fokus:** Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten. §§ 46 53 GmbHG Gesellschafterbeschluesse. Prüfraster: Beschlussgegenstand Mehrheiten Ladungspflicht Form Anlagen. Output: Beschlussentwurf Sitzungsprotokoll. Abgrenzung: nicht für Beschluss zur Kapitalerhohung nach Wandlung (gesellschafterbeschluss-kapitalerhoehung).

# Gesellschafterbeschluss vorbereiten (vor Unterzeichnung)

## Zweck

Dieser Skill erstellt einen vorbereitenden Gesellschafterbeschluss, mit dem die Gesellschafterinnen ihre grundsätzliche Bereitschaft bekunden, im Wandlungsfall eine Kapitalerhöhung durchzuführen und den neuen Gesellschafter aufzunehmen. Phase B des Lebenszyklus.

## Eingaben

- Gesellschaft: Firma, HRB, Stammkapital, Gesellschafterinnen mit Anteilen
- Beschlussthema: Grundsatzbeschluss Wandeldarlehen + Bereitschaft Kapitalerhöhung
- Abstimmungsquorum: einstimmig oder Mehrheitsbeschluss nach Satzung?
- Einberufungsform: schriftlich, E-Mail oder Vollversammlung ohne Einberufung?
- Datum der Beschlussfassung

## Rechtlicher Rahmen

### Primärnormen
- § 46 Nr. 5 GmbHG (Gesellschafterversammlung zur Aufnahme neuer Gesellschafter)
- § 51 GmbHG (Einberufung, Ladungsfrist mindestens eine Woche)
- § 51 Abs. 3 GmbHG (Beschlussfassung ohne Einberufung bei Anwesenheit / Einverständnis aller)
- § 47 GmbHG (Abstimmung, Mehrheitserfordernisse)
- § 53 GmbHG (Satzungsänderung bedarf drei Viertel der abgegebenen Stimmen und notarieller Beurkundung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Art des Beschlusses klären
Option A – Vollversammlung ohne Einberufung (§ 51 Abs. 3 GmbHG): Alle Gesellschafterinnen anwesend und einverstanden. Schnellste Variante. Option B – Einberufung mit einer Woche Frist: Schriftliche Einladung mit Tagesordnung. Option C – Umlaufbeschluss: Schriftliche Zustimmung aller Gesellschafterinnen.

### 2. Tagesordnungspunkt formulieren
"TOP 1: Grundsatzbeschluss zur Bereitschaft der Gesellschafterinnen zur Durchführung einer Kapitalerhöhung gegen Sacheinlage (Forderung aus Wandeldarlehen) im Wandlungsfall gemäß § 4 des Wandeldarlehensvertrags vom [Datum]."

### 3. Beschlusstext entwerfen
"Die Gesellschafterinnen erklären einvernehmlich ihre Bereitschaft, im Falle der wirksamen Ausübung der Wandlungsoption durch den Darlehensgeber gemäß § 4 des Wandeldarlehensvertrags alle erforderlichen gesellschaftsrechtlichen Maßnahmen zur Durchführung der Kapitalerhöhung gegen Sacheinlage, zur Zulassung des Darlehensgebers als neuer Gesellschafter und zum Verzicht auf Bezugsrechte zu ergreifen."

### 4. Protokoll erstellen
Unterschriebenes Protokoll mit Datum, Ort, Anwesende, Abstimmungsergebnis, Fassung des Beschlusstexts. Aufbewahrung in Gesellschaftsakte.

### 5. Abstimmungsergebnis dokumentieren
Einstimmig oder Mehrheitsabstimmung nach Quorum (§ 47 GmbHG). Bei Satzungsänderung: drei Viertel der Stimmen + notarielle Beurkundung (§ 53 GmbHG).

### 6. Verhältnis zum späteren Kapitalerhöhungsbeschluss
Dieser Beschluss ist kein Kapitalerhöhungsbeschluss i.S.d. § 55 GmbHG (der muss notariell beurkundet werden). Er dokumentiert nur die Absichtsbekundung. Der eigentliche Kapitalerhöhungsbeschluss folgt unter `gesellschafterbeschluss-kapitalerhoehung`.

## Beispiel-Protokoll

```
Protokoll der Gesellschafterversammlung der
Sonnenglas Solartechnologie UG (haftungsbeschränkt)
Berlin, [Datum]

Anwesend:
- Dr. Mira Schoeneck (40 Anteile, 40 %)
- Lina Habersaat (35 Anteile, 35 %)
(Treasury-Anteile: 25 Anteile, nicht abstimmend)

TOP 1: Grundsatzbeschluss Wandeldarlehen Northstar
Die Gesellschafterinnen erklären einvernehmlich ihre Bereitschaft ...
[Beschlusstext vollständig]

Abstimmung: einstimmig angenommen.

[Unterschriften Dr. Schoeneck, Habersaat]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Protokoll fehlt | Beweislosigkeit Beschlussfassung | Protokoll nachgereicht | Protokoll sofort vorhanden |
| Ladungsfrist nicht eingehalten, Einwände | Beschluss anfechtbar | Nachträgliche Zustimmung | Ladungsfrist gewahrt oder Verzicht |
| Gesellschafterin verweigert Mitwirkung | Wandlungsblockade | Gesellschafterin unentschlossen | Alle bereit |
| Grundsatzbeschluss als Kapitalerhöhungsbeschluss fehlverstanden | Notarielle Beurkundung irrtümlich unterlassen | Unklare Beschlussfassung | Eindeutige Unterscheidung |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterversammlung-einberufen/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandelereignis-eingang/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 46 ff. aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 51 GmbHG (Einberufung Gesellschafterversammlung, Ladungsfrist eine Woche) → § 47 GmbHG (Beschlussfassung, Mehrheitserfordernisse) → § 53 GmbHG (Satzungsänderung, notarielle Form) → § 43 GmbHG (Geschäftsführerhaftung bei Pflichtverletzung) → § 56 Abs. 2 GmbHG (Sacheinlagebericht, Werthaltigkeit)
