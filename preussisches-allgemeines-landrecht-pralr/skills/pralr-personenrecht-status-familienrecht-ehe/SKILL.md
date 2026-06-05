---
name: pralr-personenrecht-status-familienrecht-ehe
description: "Personenrecht Status Familienrecht EHE: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Personenrecht Status Familienrecht EHE

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Personenrecht Status Familienrecht EHE** im Plugin Preußisches Allgemeines Landrecht (PrALR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pralr-010-personenrecht-status` | PrALR: Personenrecht, Rechtsfähigkeit, Statusgruppen, Hausverband und gesellschaftliche Zuordnung analysieren. |
| `pralr-011-familienrecht-ehe-und-vormundschaft` | PrALR: Ehe, Elterngewalt, Vormundschaft, Familiengerichtlichkeit und historische Schutz-/Kontrolllogik prüfen. |
| `pralr-012-erbrecht-und-testierfreiheit` | PrALR: Erbrecht, Testierfreiheit, Familienbindung, Pflichtteile und ständische Vermögensordnung strukturieren. |
| `pralr-013-sachenrecht-eigentum-besitz` | PrALR: Eigentum, Besitz, dingliche Rechte, Nutzungen, Nachbarrechte und Eigentumsbindungen historisch prüfen. |
| `pralr-014-nachbarrecht-und-pommern-fortwirkung` | PrALR: Nachbarrechtliche Fortwirkung, lokale Rechtsräume, Pommern-Bezüge und heutige Anwendungsrisiken prüfen. |

## Arbeitsweg

Im Plugin Preußisches Allgemeines Landrecht (PrALR) gilt für **Personenrecht Status Familienrecht EHE**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pralr-010-personenrecht-status`

**Fokus:** PrALR: Personenrecht, Rechtsfähigkeit, Statusgruppen, Hausverband und gesellschaftliche Zuordnung analysieren.

# Personenrecht und Status

## Aufgabe

Beginne mit Status und Rechtsfähigkeit, dann Befugnisse, Vertretung, Schutz- oder Unterordnungsverhältnisse.

Dieser Skill arbeitet mit dem Allgemeinen Landrecht für die Preußischen Staaten als historischer Normquelle. Er behandelt das PrALR nicht als dekorativen Alttext, sondern als konkrete Quelle mit Ausgabejahr, Textzeugen, Geltungsraum, systematischem Ort und möglicher heutiger Fortwirkung.

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

## Meat on the Bone — Konkreter ALR-Stoff

### Schluesselparagraphen
- **ALR I 1 § 1**: "Der Mensch wird, in so fern er gewisse Rechte in der buergerlichen Gesellschaft geniesst, eine Person genannt."
- **ALR I 1 §§ 13-14**: Lebendgeburt erforderlich fuer Rechtsfaehigkeit; "Schrei oder ander Lebenszeichen" Anforderung.
- **ALR I 1 §§ 25-30**: Verschollenheit; nach 80. Lebensjahr Todvermutung mit Verschollensregel (vor Zitat verifizieren).
- **ALR I 1 §§ 50-70**: Stand als rechtlicher Begriff; Verweis auf die staendischen Titel ALR II 7-9.
- **ALR I 4 §§ 1 ff.**: Geschaeftsfaehigkeit; Minderjaehrige bis 14 voellig geschaeftsunfaehig, bis 25 beschraenkt.

### Subsumtionsbeispiel: Erbfaehigkeit eines Nasciturus
Sachverhalt: Schwangere Witwe; Kind wird tot geboren; Erbschaft des verstorbenen Vaters.
ALR-Loesung: ALR I 1 §§ 13-14 — Lebendgeburt erforderlich; Totgeborenes hat nie Rechtsfaehigkeit erlangt; die Erbschaft faellt nach Intestaterbfolge an die naechsten Verwandten (Naechstmoegliche Erben nach ALR I 17). Vergleich BGB: § 1923 Abs. 2 BGB schuetzt den Nasciturus identisch.

### Subsumtionsbeispiel: Adelsfuehrung
Sachverhalt: Familie behauptet Adelszugehoerigkeit.
ALR-Loesung: ALR II 9 §§ — Pruefung des Adelsbriefs; Adelsfuehrung nur bei Nachweis. Heute: Art. 109 III WRV / Art. 123 I GG, Adel nur als Namensbestandteil.

### Heutige Fortwirkung
- § 1 BGB hat ALR I 1 § 1 abgeloest — Rechtsfaehigkeit beginnt mit Vollendung der Geburt.
- BVerfG zur Adelsfuehrung als Namensbestandteil — staendige Rspr., Az im Mandat verifizieren.

## Ausgabeformat

- **Kurzbefund:** Was sagt die Quelle sicher?
- **Textzeugenstand:** Welche Fassung wurde benutzt und wo ist sie unsicher?
- **Historische Einordnung:** Systemstelle, Geltungsraum, gesellschaftliche Funktion.
- **Heutiger Anschluss:** Fortwirkung, Gewohnheitsrecht, bloße Dogmengeschichte oder keine heutige Relevanz.
- **Nächster Schritt:** zweite Quelle, Scan-Gegenprobe, aktuelles Landesrecht oder Rechtsprechungsrecherche.

## 2. `pralr-011-familienrecht-ehe-und-vormundschaft`

**Fokus:** PrALR: Ehe, Elterngewalt, Vormundschaft, Familiengerichtlichkeit und historische Schutz-/Kontrolllogik prüfen.

# Familienrecht

## Aufgabe

Arbeite mit historischer Distanz: nicht moderne Gleichberechtigung hineinlesen, aber Modernisierungstendenzen benennen.

Dieser Skill arbeitet mit dem Allgemeinen Landrecht für die Preußischen Staaten als historischer Normquelle. Er behandelt das PrALR nicht als dekorativen Alttext, sondern als konkrete Quelle mit Ausgabejahr, Textzeugen, Geltungsraum, systematischem Ort und möglicher heutiger Fortwirkung.

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

## Meat on the Bone — Konkreter ALR-Stoff

### Schluesselparagraphen
- **ALR II 1 §§ 1 ff.**: Allgemeine Wirkung der Ehe; Eheschliessung nur vor Pfarrer (vor reichseinheitlicher Zivilehe 1875).
- **ALR II 1 §§ 174-200**: Pflichten der Ehegatten; Pflicht zur ehelichen Beiwohnung; Pflicht der Frau zur Befolgung im Haushalt; Schutzpflicht des Mannes.
- **ALR II 1 §§ 205-300**: Gueterrechtlich — Verwaltungsgemeinschaft, Mann als Verwalter des Frauenvermoegens.
- **ALR II 1 §§ 670-750**: Scheidung; Scheidungsgruende kasuistisch (Ehebruch, boeswilliges Verlassen, Krankheit).
- **ALR II 2 §§ 1 ff.**: Eltern-Kind-Verhaeltnis; vaeterliche Gewalt.
- **ALR II 18 §§ 1 ff.**: Vormundschaft fuer Unmuendige und Verschwender.

### Subsumtionsbeispiel: Ehescheidung wegen Ehebruchs (1850)
Sachverhalt: Ehemann betrueben mit Magd, Ehebruch nachgewiesen.
ALR-Loesung: ALR II 1 §§ 670-680 — Scheidung gewaehrt; schuldiger Mann verliert Anspruch auf gemeinsame Wohnung; Frau erhaelt Unterhalt nach ihrem Stand. Vermoegenstrennung nach ALR II 1 §§ 205 ff. Kinder bleiben in vaeterlicher Gewalt nur wenn unschuldig.

### Subsumtionsbeispiel: Vormundschaft fuer Minderjaehrigen mit Vermoegen
Sachverhalt: Waisen 12 Jahre mit Erbschaft 10000 Taler.
ALR-Loesung: ALR II 18 — Vormund bestellt durch das Vormundschaftsgericht; Pflicht zur jaehrlichen Rechnungslegung; ALR II 18 §§ — Eigengeschaefte des Vormunds mit dem Muendelvermoegen verboten; bei Verlust Schadenshaftung.

### Heutige Fortwirkung
- BGB §§ 1297-1588 haben das ALR-Eherecht abgeloest.
- Reichsehegesetz 1875 fuehrte staatliche Eheschliessung ein — wirkt bis heute (§ 1310 BGB Zivilehe).
- §§ 1773 ff. BGB Vormundschaft als Nachfolger ALR II 18.

## Ausgabeformat

- **Kurzbefund:** Was sagt die Quelle sicher?
- **Textzeugenstand:** Welche Fassung wurde benutzt und wo ist sie unsicher?
- **Historische Einordnung:** Systemstelle, Geltungsraum, gesellschaftliche Funktion.
- **Heutiger Anschluss:** Fortwirkung, Gewohnheitsrecht, bloße Dogmengeschichte oder keine heutige Relevanz.
- **Nächster Schritt:** zweite Quelle, Scan-Gegenprobe, aktuelles Landesrecht oder Rechtsprechungsrecherche.

## 3. `pralr-012-erbrecht-und-testierfreiheit`

**Fokus:** PrALR: Erbrecht, Testierfreiheit, Familienbindung, Pflichtteile und ständische Vermögensordnung strukturieren.

# Erbrecht

## Aufgabe

Trenne gesetzliche Erbfolge, Verfügung, Familienbindung, Lehns-/Fideikommissnähe und spätere BGB-Ablösung.

Dieser Skill arbeitet mit dem Allgemeinen Landrecht für die Preußischen Staaten als historischer Normquelle. Er behandelt das PrALR nicht als dekorativen Alttext, sondern als konkrete Quelle mit Ausgabejahr, Textzeugen, Geltungsraum, systematischem Ort und möglicher heutiger Fortwirkung.

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

## Meat on the Bone — Konkreter ALR-Stoff

### Schluesselparagraphen
- **ALR I 12 §§ 1-100**: Allgemeines Erbrecht; Anfall der Erbschaft mit dem Tod (delatio); Anspruch auf "ungetheilte Erbschaft".
- **ALR I 12 §§ 200-300**: Testament; oeffentlich (vor Gericht) oder privatschriftlich mit Zeugen.
- **ALR I 12 §§ 380-440**: Pflichtteilsrecht — kasuistisch nach Verwandtschaftsgrad gestaffelt.
- **ALR I 17**: Intestaterbfolge; sechs Parentelen-Modell wie im Roemisch-rechtlichen Anschluss.
- **ALR II 4**: Familienfideikommiss — Adelsgut mit Unteilbarkeit ("Hausgut"); abgeschafft 1919/1938.

### Subsumtionsbeispiel: Testament 1820
Sachverhalt: Wohlhabender Buerger setzt zugunsten der Magd Erbe ein; pflichtteilsberechtigte Kinder.
ALR-Loesung: Pflichtteilsrecht ALR I 12 §§ 380 ff. — Pflichtteil 1/3 des Intestaterbteils; Testament insoweit unwirksam (querela inofficiosi testamenti analog); Magd erhaelt nur den freien Teil; Kinder klagen erfolgreich Pflichtteil.

### Subsumtionsbeispiel: Fideikommiss-Streit
Sachverhalt: Adelsfamilie; Stammgut mit Fideikommiss aus 1750.
ALR-Loesung: Bis 1919/1938 ALR II 4 — Stammgut unteilbar; geht an aeltesten Sohn (Primogenitur); juengere Geschwister erhalten Abfindung. Nach Auflösung der Fideikommisse: Vermoegen wird Sondervermoegen, fortgesetzt mit Ablösung.

### Heutige Fortwirkung
- BGB §§ 1922 ff. ueberlagern ALR-Erbrecht ab 01.01.1900.
- Pflichtteil heute 1/2 des Intestaterbteils (§ 2303 BGB).
- Fideikommisse: Aufloesungsgesetz 26.01.1938 / Kontrollratsgesetz Nr. 45 Berlin — heute keine neuen Fideikommisse moeglich.
- ALR-Erbfaelle vor 1900 noch heute relevant fuer Stammbaum- und Eigentumsstreitigkeiten an alten Gueteen.

## Ausgabeformat

- **Kurzbefund:** Was sagt die Quelle sicher?
- **Textzeugenstand:** Welche Fassung wurde benutzt und wo ist sie unsicher?
- **Historische Einordnung:** Systemstelle, Geltungsraum, gesellschaftliche Funktion.
- **Heutiger Anschluss:** Fortwirkung, Gewohnheitsrecht, bloße Dogmengeschichte oder keine heutige Relevanz.
- **Nächster Schritt:** zweite Quelle, Scan-Gegenprobe, aktuelles Landesrecht oder Rechtsprechungsrecherche.

## 4. `pralr-013-sachenrecht-eigentum-besitz`

**Fokus:** PrALR: Eigentum, Besitz, dingliche Rechte, Nutzungen, Nachbarrechte und Eigentumsbindungen historisch prüfen.

# Sachenrecht

## Aufgabe

Baue eine Matrix: Sache, Recht, Erwerb, Beschränkung, Schutz, Durchsetzung, heutiger Anschluss.

Dieser Skill arbeitet mit dem Allgemeinen Landrecht für die Preußischen Staaten als historischer Normquelle. Er behandelt das PrALR nicht als dekorativen Alttext, sondern als konkrete Quelle mit Ausgabejahr, Textzeugen, Geltungsraum, systematischem Ort und möglicher heutiger Fortwirkung.

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

## Meat on the Bone — Konkreter ALR-Stoff

### Schluesselparagraphen
- **ALR I 8 § 1**: "Eigenthuemer heisst derjenige, welcher befugt ist, ueber die Substanz einer Sache, oder eines Rechts, mit Ausschliessung Anderer, aus eigener Macht, durch sich selbst oder einen Dritten, zu verfuegen."
- **ALR I 8 §§ 26-50**: Schranken — Aufopferung fuer Gemeinwohl, Notrechte Dritter.
- **ALR I 9 §§ 1-100**: Besitz; corpus + animus aus roemischer Tradition; mittelbarer Besitz uebergeben.
- **ALR I 10**: Grundeigentum; Aufflassung vor Behoerde plus Eintragung im Hypothekenbuch.
- **ALR I 21**: Dienstbarkeiten und Reallasten; Wegerecht, Wasserlauf, Hutung, Mast, Triftrecht.
- **ALR I 22**: Erbpacht und Erbenzinsguter.

### Subsumtionsbeispiel: Vindikation gestohlener Kuh
Sachverhalt: Bauer A; Kuh gestohlen; bei Bauer B in einem anderen Dorf entdeckt; B hat sie redlich auf dem Markt gekauft.
ALR-Loesung: ALR I 9 — A bleibt Eigentuemer; Markterwerb in Treu und Glauben schuetzt B nicht voll bei Verlust (anders als § 935 BGB heute Gutglaeubigkeitsausschluss bei gestohlenen Sachen). A kann vindizieren; B muss Kuh herausgeben; Mehrkosten der Aufzucht ersatzfaehig nach ALR I 9 §§.

### Subsumtionsbeispiel: Hutungsrecht in Brandenburg 1880
Sachverhalt: Dorfgemeinschaft hat seit Generationen Hutungsrecht (Weiderecht) auf Adelsgut; Eigentuemer will Recht aufheben.
ALR-Loesung: ALR I 21 — Hutungsrecht als Dienstbarkeit; Ablösung gegen Entschaedigung nach Gemeinheitsteilungsordnung 1821 und Ablösungsordnung 1850 moeglich. Wert der Servitut wird in Geld umgerechnet.

### Heutige Fortwirkung
- § 903 BGB (Eigentumsdefinition) — fast wortlich aus ALR I 8 § 1.
- §§ 854-872 BGB Besitz.
- §§ 873, 925 BGB Auflassung als Nachfolger ALR I 10.
- § 184 ff. EGBGB schuetzt vor BGB-Inkrafttreten begruendete Altrechte (Hutungsrecht, Erbenzinsguter): bis heute teils noch in Grundbuchblaettern vermerkt — relevant in Brandenburg, Mecklenburg-Vorpommern, Sachsen-Anhalt!
- Sachenrechtsbereinigungsgesetz 1994 fuer Ostdeutschland.

## Ausgabeformat

- **Kurzbefund:** Was sagt die Quelle sicher?
- **Textzeugenstand:** Welche Fassung wurde benutzt und wo ist sie unsicher?
- **Historische Einordnung:** Systemstelle, Geltungsraum, gesellschaftliche Funktion.
- **Heutiger Anschluss:** Fortwirkung, Gewohnheitsrecht, bloße Dogmengeschichte oder keine heutige Relevanz.
- **Nächster Schritt:** zweite Quelle, Scan-Gegenprobe, aktuelles Landesrecht oder Rechtsprechungsrecherche.

## 5. `pralr-014-nachbarrecht-und-pommern-fortwirkung`

**Fokus:** PrALR: Nachbarrechtliche Fortwirkung, lokale Rechtsräume, Pommern-Bezüge und heutige Anwendungsrisiken prüfen.

# Nachbarrechtliche Fortwirkung

## Aufgabe

Prüfe erst Landesrecht und lokale Fortgeltung. Wenn PrALR als Altrecht denkbar ist, Fundstelle und heutige Rechtsprechung live verifizieren.

Dieser Skill arbeitet mit dem Allgemeinen Landrecht für die Preußischen Staaten als historischer Normquelle. Er behandelt das PrALR nicht als dekorativen Alttext, sondern als konkrete Quelle mit Ausgabejahr, Textzeugen, Geltungsraum, systematischem Ort und möglicher heutiger Fortwirkung.

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

## Meat on the Bone — Konkreter ALR-Stoff

### Schluesselparagraphen
- **ALR I 23 §§ 1-30**: Allgemeine Nachbarrechte; Grenzbaeume, Grenzhecken (Grenzbaum gehoert beiden Nachbarn anteilig).
- **ALR I 23 §§ 35-50**: Immissionen — Rauch, Geruch, Gewerbedaempfe; Untersagung nur, wenn "uebermaessige Beeintraechtigung".
- **ALR I 23 §§ 80 ff.**: Notweg ueber Nachbarsgrundstueck bei eingeschlossener Lage; Entschaedigung.
- **ALR I 23 §§**: Traufrecht — Wasser darf von Hausdach auf Nachbarsgrundstueck fliessen, sofern keine wesentliche Schaedigung.

### Subsumtionsbeispiel: Eingeschlossenes Grundstueck in Pommern 1900
Sachverhalt: Bauer X hat Acker ohne Wegezugang; Nachbar Y verweigert Durchgang.
ALR-Loesung: ALR I 23 §§ 80 ff. — Notwegrecht; Pflicht des Nachbarn zur Duldung; Entschaedigung in Geld nach Wert. Heutige Fortwirkung: § 917 BGB Notweg.

### Subsumtionsbeispiel: Rauchimmissionen einer Schmiede 1850
Sachverhalt: Schmiede in einem Dorf; Nachbarn beklagen sich.
ALR-Loesung: ALR I 23 §§ 35-50 — Beurteilung nach Ortsueblichkeit; bei "uebermaessiger Beeintraechtigung" Untersagungsanspruch oder Entschaedigung. Vorlaeufer § 906 BGB.

### Pommern-Spezifikum
- Pommersche Gueter mit jahrhundertelangen Servituten waren bis 1945 Hauptanwendungsfall.
- Nach 1945 in der DDR Bodenreform; nach Wiedervereinigung Eigentumsfragen ueber das Vermoegensgesetz und Sachenrechtsbereinigungsgesetz.

### Heutige Fortwirkung
- § 906 BGB Immissionen.
- § 910 BGB Ueberhang.
- § 912 BGB Ueberbau.
- § 917 BGB Notweg.
- Landesnachbarrechtsgesetze (NachbG NRW, Bdb, MV, ST).

## Ausgabeformat

- **Kurzbefund:** Was sagt die Quelle sicher?
- **Textzeugenstand:** Welche Fassung wurde benutzt und wo ist sie unsicher?
- **Historische Einordnung:** Systemstelle, Geltungsraum, gesellschaftliche Funktion.
- **Heutiger Anschluss:** Fortwirkung, Gewohnheitsrecht, bloße Dogmengeschichte oder keine heutige Relevanz.
- **Nächster Schritt:** zweite Quelle, Scan-Gegenprobe, aktuelles Landesrecht oder Rechtsprechungsrecherche.
