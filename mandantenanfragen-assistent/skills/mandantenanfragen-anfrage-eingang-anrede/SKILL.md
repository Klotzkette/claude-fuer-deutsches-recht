---
name: mandantenanfragen-anfrage-eingang-anrede
description: "Anfrage Eingang Anrede: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anfrage Eingang Anrede

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anfrage Eingang Anrede** im Plugin Mandantenanfragen-Assistent. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-mandantenanfragen-fristen-form-und-zustaendigkeit` | Mandantenanfragen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin mandantenanfragen assistent; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `anfrage-eingang-parser` | Sekretariat oder Anwalt erhielt E-Mail-Anfrage eines potentiellen Mandanten und will sie schnell strukturiert auswerten. E-Mail-Parser Kanzlei. Prüfraster: Anrede Name Absender E-Mail-Adresse Telefon Sachverhaltsfetzen Stichwörter dringliche Hinweise auf Fristen oder Haftungsrisiken. Output: strukturiertes Datenblatt mit Kontaktdaten und Sachverhalts-Extrakt. Abgrenzung zu erstantwort-generator (Antwort erstellen) und dringlichkeitsmarker (Eilbedarf). |
| `anrede-uebernehmen` | Antwort-E-Mail soll mit exakt richtiger Anrede des potentiellen Mandanten beginnen ohne Fehler bei Titeln oder Doppelnamen. Anredekonventionen Kanzlei. Prüfraster: Titel (Dr. Prof. Mag.) Doppelnamen Adelspraeifikate kirchliche Titel Komposita Ehepaare Erbengemeinschaften namenlose Anfragen. Output: korrekte formelle Anredezeile für E-Mail-Antwort. Abgrenzung zu anfrage-eingang-parser (Datenparsing) und erstantwort-generator (vollständige E-Mail). |

## Arbeitsweg

Im Plugin Mandantenanfragen-Assistent gilt für **Anfrage Eingang Anrede**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-mandantenanfragen-fristen-form-und-zustaendigkeit`

**Fokus:** Mandantenanfragen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin mandantenanfragen assistent; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Mandantenanfragen: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Mandantenanfragen: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Mandantenanfragen: Fristen, Form, Zuständigkeit und Rechtsweg / mandantenanfragen fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DSGVO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Mandantenanfragen** prüfen.
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

## 2. `anfrage-eingang-parser`

**Fokus:** Sekretariat oder Anwalt erhielt E-Mail-Anfrage eines potentiellen Mandanten und will sie schnell strukturiert auswerten. E-Mail-Parser Kanzlei. Prüfraster: Anrede Name Absender E-Mail-Adresse Telefon Sachverhaltsfetzen Stichwörter dringliche Hinweise auf Fristen oder Haftungsrisiken. Output: strukturiertes Datenblatt mit Kontaktdaten und Sachverhalts-Extrakt. Abgrenzung zu erstantwort-generator (Antwort erstellen) und dringlichkeitsmarker (Eilbedarf).

# Anfrage-Eingang-Parser

Dieser Skill extrahiert aus einer eingehenden Mandantenanfrage per E-Mail alle relevanten Informationen in strukturierter Form, damit das Sekretariat und die bearbeitende Rechtsanwältin sofort den Überblick haben.


## Triage zu Beginn
1. Ueber welchen Kanal ist die Anfrage eingegangen: E-Mail, Webformular, beA, Telefonnotiz, Messenger?
2. Gibt es eindeutige Fristen-Signale oder Eile-Marker, die sofortige Weiterleitung erfordern?
3. Kann die anfragende Person identifiziert werden (Name, E-Mail, Telefon) oder ist die Anfrage anonym?
4. Ist die Anfrage in deutscher Sprache oder in einer Fremdsprache (Weiterleitung an mehrsprachige-antwort)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. b, f DSGVO — Rechtsgrundlage fuer Verarbeitung von Erstanfrage-Daten
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: nur notwendige Daten aus der Anfrage extrahieren
- § 43 BRAO — Sorgfaltspflicht: sofortige Bearbeitung und Dokumentation eingehender Anfragen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: vor Mandatsannahme ueber voraussichtliche Kosten informieren

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Eingehende Mandantenanfragen sind oft unstrukturiert. Sie können als Fließtext, als kurze Notiz oder als ausführlicher Erlebnisbericht formuliert sein. Dieser Skill normiert die Extraktion und legt eine Grundlage für alle folgenden Skills (Anrede, Erstantwort, Dringlichkeit, Konfliktcheck, CRM-Eintrag).

## Extraktionsfelder

### 1. Anrede (Pflichtfeld für Folge-Skills)

- Vollständige Anredezeile aus der Mail, z. B. "Sehr geehrte Damen und Herren", "Guten Tag, ich heiße Maria Mustermann", "Hallo"
- Falls die Anfragende Person ihre eigene Anredeform nennt (z. B. "Meine Name ist Dr. Klaus-Dieter Müller-Strauss"), diese festhalten.
- Titel aus der Signatur, aus dem E-Mail-Header oder aus dem Fließtext extrahieren.
- Hinweis: Die exakte Anrede wird im Skill `anrede-uebernehmen` weiterverarbeitet.

### 2. Name

- Vorname, Nachname, ggf. akademischer Grad, Adelsprädikat, Doppelname
- Quellen: Signatur, Fließtext, E-Mail-Adresse (Heuristik), Betreffzeile
- Unsicherheit kennzeichnen: `[Name unklar: ...]`

### 3. E-Mail-Adresse

- Absender-Adresse aus dem Header
- Etwaige Rückantwort-Adresse (Reply-To), wenn abweichend
- Verteilerliste/CC-Adressen als Zusatz-Information

### 4. Telefonnummer und weitere Kontaktdaten

- Mobilnummer, Festnetznummer aus Signatur oder Fließtext
- Postanschrift, falls angegeben
- Fax, soweit genannt (selten, aber in manchen Branchen noch üblich)

### 5. Sachverhaltsfetzen

- Stichpunktartige Zusammenfassung des geschilderten Anliegens
- Rechtsgebiet-Zuordnung (Ersteinschätzung, nicht verbindlich): z. B. Mietrecht, Arbeitsrecht, Erbrecht, Strafrecht
- Beteiligte Parteien soweit genannt (Gegner, Behörde, Arbeitgeber, Vermieter etc.)
- Relevante Daten, Beträge, Verträge, Bescheide

### 6. Dringliche Hinweise

- Explizite Fristnennung: Datum, Fristende, Hauptverhandlung, Klagefrist
- Implizite Eile-Signale: "sofort", "dringend", "nächste Woche", "bis Ende der Woche"
- Haftungsrisiken: Versäumnisurteil, Zwangsvollstreckung, Insolvenzantrag
- Hinweis an den Skill `dringlichkeitsmarker` weitergeben

## Ausgabeformat

```
PARSED ANFRAGE
==============

Anrede (roh): [Originaltext der Anrede / Grußformel]
Name: [Vollständiger Name mit Titeln]
E-Mail: [Absenderadresse]
Telefon: [Nummer oder "nicht genannt"]
Weitere Kontakte: [Adresse, Fax, etc. — oder "keine"]

Rechtsgebiet: [Ersteinschätzung oder "unklar"]
Sachverhalt-Stichwörter:
 - [Stichwort 1]
 - [Stichwort 2]
 - [...]

Beteiligte: [Gegner/Behörde/weitere Personen oder "nicht genannt"]
Relevante Daten/Beträge: [oder "nicht genannt"]

DRINGLICHKEIT: [HOCH / MITTEL / NIEDRIG / UNBEKANNT]
Dringlichkeit-Grund: [Kurze Begründung oder "keiner erkannt"]
```

## Heuristiken und Sonderfälle

### E-Mail-Adresse als Namenquelle

Beispiel: `kd.mueller-strauss@example.de` → Hinweis: Vorname K.D., Nachname Müller-Strauss (ungesichert, nur als Interpretations-Hinweis kennzeichnen).

### Keine Anrede vorhanden

Manche Anfragen beginnen direkt mit dem Sachverhalt: "Ich habe von meinem Arbeitgeber eine Kündigung erhalten ...". In diesem Fall:
- Anrede (roh): `[nicht vorhanden]`
- Name aus Signatur oder Fließtext suchen
- Skill `anrede-uebernehmen` erhält den Hinweis, eine neutrale Höflichkeitsform zu verwenden.

### Mehrere Absender / Ehepaar / Erbengemeinschaft

Bei "Wir möchten uns melden ..." oder "Ich schreibe im Namen meiner Mutter ...":
- Alle Personen aufführen
- Hauptkontakt kennzeichnen
- Komplexere Anrede-Heuristik für Skill `anrede-uebernehmen` vormerken

### Sprache der Anfrage

- Erkannte Sprache festhalten (DE / EN / FR / IT / Sonstiges)
- Mehrsprachige Anfragen: Sprache der Hauptaussage priorisieren
- Übergabe an Skill `mehrsprachige-antwort` wenn nicht Deutsch

## Qualitätssicherung

Nach der Extraktion:
1. Vollständigkeit prüfen: Fehlen Pflichtfelder (Name, E-Mail), kennzeichnen und für manuelle Ergänzung markieren.
2. Keine Interpretation über den Wortlaut hinaus: Sachverhaltsfetzen sind Zitate oder direkte Zusammenfassungen, keine rechtliche Würdigung.
3. Keine Rechtsberatung: Dieser Skill erstellt keine rechtliche Bewertung — nur Faktenextraktion.

## Verweise auf andere Skills

- `anrede-uebernehmen` — übernimmt die rohe Anrede und konvertiert sie in die formelle Anredezeile der Antwortmail
- `dringlichkeitsmarker` — wertet die dringlichen Hinweise aus diesem Skill weiter aus
- `spam-und-massen-anfrage-filter` — prüft die geparste Anfrage auf Spam-Muster
- `konfliktcheck-vorab` — verwendet Beteiligte und Gegner aus der Extraktion
- `folgekorrespondenz-vorbereiten` — befüllt den CRM-Skeleton-Eintrag mit den hier extrahierten Daten

## 3. `anrede-uebernehmen`

**Fokus:** Antwort-E-Mail soll mit exakt richtiger Anrede des potentiellen Mandanten beginnen ohne Fehler bei Titeln oder Doppelnamen. Anredekonventionen Kanzlei. Prüfraster: Titel (Dr. Prof. Mag.) Doppelnamen Adelspraeifikate kirchliche Titel Komposita Ehepaare Erbengemeinschaften namenlose Anfragen. Output: korrekte formelle Anredezeile für E-Mail-Antwort. Abgrenzung zu anfrage-eingang-parser (Datenparsing) und erstantwort-generator (vollständige E-Mail).

# Anrede-Übernehmen

Dieser Skill übernimmt die exakte Anrede aus der eingehenden E-Mail und wandelt sie — wo nötig — in eine formelle Anredezeile für das Antwortschreiben um. Grundprinzip: Was die anfragende Person über sich selbst sagt, hat Vorrang vor jeder Heuristik.


## Triage zu Beginn
1. Wie hat sich die anfragende Person angesprochen oder bezeichnet (Titel, Nachname, Vorname, Doppelname)?
2. Gibt es Unsicherheiten bei Titel, Geschlecht oder Namensbestandteilen, die gekennzeichnet werden muessen?
3. Ist die Anfrage nicht auf Deutsch — andere Anredekonventionen (EN, FR, IT) beachten?
4. Handelt es sich um eine Erbengemeinschaft, ein Ehepaar oder eine juristische Person mit besonderer Anredeform?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 2 BORA — Gewissenhaftigkeit: korrekte Mandantenkommunikation als Grundpflicht
- Art. 2 Abs. 1 i.V.m. Art. 1 Abs. 1 GG — Allgemeines Persoenlichkeitsrecht: korrekte Namens- und Titelanrede ist Teil des Persoenlichkeitsschutzes
- § 43 BRAO — Sorgfaltspflicht: fehlerfreie Kommunikation als Bestandteil anwaltlicher Berufspflichten
- § 12 BGB — Namensrecht: Recht auf korrekte Namensnennung auch in der Korrespondenz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Grundprinzip: Exaktheit vor Heuristik

Die Anrede aus der Eingangsmail wird buchstabengenau übernommen, sofern sie bereits formal korrekt ist. Eigenhändig gewählte Anredeformen sind zu respektieren:

- "Sehr geehrte Frau Dr. Mueller-Strauss" → Antwort: "Sehr geehrte Frau Dr. Mueller-Strauss,"
- "Sehr geehrter Herr Professor Brandt-Heuwig" → Antwort: "Sehr geehrter Herr Professor Brandt-Heuwig,"
- "Hallo, mein Name ist Maria" → Antwort: "Sehr geehrte Frau Maria," (formell konvertiert; Nachname aus Signatur/Fließtext ergänzen)

## Heuristiken nach Anrede-Typ

### Typ 1: Vollständige formelle Anrede vorhanden

Beispiel in der Eingangsmail: "Sehr geehrte Damen und Herren," oder "Sehr geehrte Frau Dr. Lichtenberg-Kaufmann,"

Vorgehen: 1:1-Übernahme. Prüfe auf Tippfehler (z. B. "Sehr geerte" → korrigieren und in einer internen Notiz vermerken, dass die Korrektur vorgenommen wurde).

### Typ 2: Nur Vorname

Beispiel: "Hallo, ich bin Klaus."

Vorgehen:
1. Nachname aus Signatur, E-Mail-Adresse oder Fließtext suchen.
2. Geschlecht soweit erkennbar ermitteln; falls nicht, geschlechtsneutral: "Sehr geehrte Person," oder bei deutschem Recht am besten mit vollem Namen: "Sehr geehrter Klaus [Nachname],"
3. Falls Nachname nicht ermittelbar: "Sehr geehrte anfragende Person," als neutrale Fallback-Formulierung.

### Typ 3: Keine Anrede, nur Sachverhalt

Beispiel: "Ich habe eine Kündigung erhalten und weiß nicht weiter."

Vorgehen:
1. Signatur, Reply-To und Fließtext auf Namen durchsuchen.
2. Falls Name gefunden: Formelle Anrede aus Name konstruieren.
3. Falls kein Name: "Sehr geehrte Damen und Herren," verwenden (neutrale Sammelanrede).

### Typ 4: Akademische Titel

Hierarchie der Titelführung nach deutschem Recht:

| Titel | Anrede-Formulierung |
|---|---|
| Dr. (einmal) | "Sehr geehrter Herr Dr. Müller," |
| Dr. Dr. / Dr. med. Dr. iur. | "Sehr geehrter Herr Dr. Dr. Müller," (beide Dr. führen) |
| Prof. Dr. | "Sehr geehrter Herr Professor Dr. Müller," |
| Prof. (ohne Dr.) | "Sehr geehrter Herr Professor Müller," |
| Mag., Dipl.-Ing., Dipl.-Kfm. | In der Anrede nicht zwingend geführt; aus der Eingangsmail übernehmen, wenn die Person sie selbst verwendet |
| LL.M., MBA | In der Anrede üblicherweise nicht geführt; nur übernehmen, wenn die Person es selbst schreibt |

### Typ 5: Adelsprädikat

- "von", "von und zu", "Freiherr von", "Gräfin von": Vollständig aus der Eingangsmail übernehmen.
- Beispiel: "Sehr geehrter Herr Baron von Schwarzenberg-Kleist,"
- Kein Adelsprädikat erfinden — nur aus der Selbstdarstellung der anfragenden Person.

### Typ 6: Kirchliche und ordensbezogene Titel

- "Pater", "Bruder", "Schwester", "Diakon", "Pfarrer", "Pastor", "Rabbiner", "Imam": Vollständig aus der Eingangsmail übernehmen.
- Beispiel: "Sehr geehrter Pater Anselm Brandner,"
- Bei ordensbezogenen Kürzeln (z. B. "SJ", "OSB") nur in der Signatur führen, nicht in der Anredezeile, es sei denn, die Person tut es selbst.

### Typ 7: Doppelnamen und Bindestrichnamen

- Bindestrichnamen vollständig übernehmen: "Mueller-Strauss", "Brandt-Heuwig", "Graf-von-Kleist"
- Keine eigenständige Kürzung des Doppelnamens
- Beispiel: "Sehr geehrte Frau Dr. Mueller-Strauss-Hoffmann,"

### Typ 8: Ehepaar oder Personenmehrheit

- Bei gemeinschaftlicher Anfrage: "Sehr geehrte Frau Dr. Müller, sehr geehrter Herr Müller," (getrennt auflisten)
- Alternativ: "Sehr geehrte Eheleute Müller," (nur wenn keine akademischen Titel oder wenn Paar selbst diese Formulierung wählt)
- Erbengemeinschaft: "Sehr geehrte Mitglieder der Erbengemeinschaft [Name],"

### Typ 9: Informelle Anfrage mit Du-Siezen-Stil

- Beispiel: "Hi, ich bin Anna und hätte da mal eine Frage..."
- Antwort trotzdem formell: "Sehr geehrte Frau [Nachname]," — nicht auf den informellen Ton eingehen.
- Wenn Nachname nicht ermittelbar: "Sehr geehrte Frau Anna," (nur Vorname, besser als nichts)

### Typ 10: Geschlechtsidentität / nichtbinäre Formulierungen

- "Mx." oder "Divers" aus der Eingangsmail: "Sehr geehrte Person [Nachname]," oder die von der anfragenden Person gewünschte Formulierung übernehmen.
- Im Zweifel vollständigen Namen ohne Geschlechtsmarkierung verwenden: "Sehr geehrte[r/s] [Vollständiger Name],"

## Ausgabeformat

```
ANREDEZEILE (Erstantwort):
Sehr geehrte[r/s/e] [Titel] [Vorname] [Nachname],

INTERNE NOTIZ:
Quelle der Anrede: [Signatur / Fließtext / E-Mail-Header / Heuristik]
Angewendete Heuristik: [Typ 1-10 oder keine]
Unsicherheit: [ja/nein — wenn ja: manuell prüfen]
```

## Verweise auf andere Skills

- `anfrage-eingang-parser` — liefert die rohe Anrede und den Namen
- `erstantwort-generator` — verwendet die fertige Anredezeile aus diesem Skill
- `muster-erstantwort` — enthält Anrede-Platzhalter `[ANREDE]` die durch diesen Skill befüllt werden

<!-- AUDIT 27.05.2026 | bundle_053
Geprüft: BGH VI ZR 7/20 (NOT_FOUND auf dejure.org)
Ersatz: BGH VI ZR 246/19, NJW 2020, 3715 (verifiziert auf dejure.org)
Thema: Allgemeines Persönlichkeitsrecht — thematisch passend für Persönlichkeitsschutz-Kontext
-->
