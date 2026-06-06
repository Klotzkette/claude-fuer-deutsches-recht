---
name: anrede-uebernehmen
description: "Antwort-E-Mail soll mit exakt richtiger Anrede des potentiellen Mandanten beginnen ohne Fehler bei Titeln oder Doppelnamen. Anredekonventionen Kanzlei. Prüfraster: Titel (Dr. Prof. Mag.) Doppelnamen Adelspraeifikate kirchliche Titel Komposita Ehepaare Erbengemeinschaften namenlose Anfragen. Output: korrekte formelle Anredezeile für E-Mail-Antwort. Abgrenzung zu anfrage-eingang-parser (Datenparsing) und erstantwort-generator (vollständige E-Mail) im Mandantenanfragen Assistent: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Anrede-Übernehmen

## Arbeitsbereich

Antwort-E-Mail soll mit exakt richtiger Anrede des potentiellen Mandanten beginnen ohne Fehler bei Titeln oder Doppelnamen. Anredekonventionen Kanzlei. Prüfraster: Titel (Dr. Prof. Mag.) Doppelnamen Adelspraeifikate kirchliche Titel Komposita Ehepaare Erbengemeinschaften namenlose Anfragen. Output: korrekte formelle Anredezeile für E-Mail-Antwort. Abgrenzung zu anfrage-eingang-parser (Datenparsing) und erstantwort-generator (vollständige E-Mail). Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 44 unverzügliche Annahme/Ablehnung, RVG § 34 Erstberatung max. 190 EUR (Verbraucher), DSGVO Art. 13 Information bei Erhebung.
- Tragende Normen verifizieren: BRAO §§ 43a, 44, 49b, BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1, 4, 34 (Erstberatung), DSGVO Art. 6, 13 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anfragender (Interessent), Anwalt, Sekretariat, Compliance-Beauftragter, Mandantenbetreuer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Erstkontaktformular, Konfliktscreening, Mandatsvertrag, Vollmacht, Honorarvereinbarung, Mandantendossier, Datenschutzhinweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

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
