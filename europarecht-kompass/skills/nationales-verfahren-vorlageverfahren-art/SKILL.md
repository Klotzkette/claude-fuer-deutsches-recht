---
name: nationales-verfahren-vorlageverfahren-art
description: "Nationales Verfahren Vorlageverfahren ART: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nationales Verfahren Vorlageverfahren ART

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Nationales Verfahren Vorlageverfahren ART** im Plugin Europarecht (EuGH, EU-Kommission). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `europarecht-nationales-verfahren-effektivitaet` | EU-Rechtsvorgaben zum effektiven nationalen Rechtsschutz prüfen wenn nationales Verfahren EU-Rechte beeintraechtigt. Art. 47 GRC Art. 19 EUV Effektivitaetsprinzip. Prüfraster: Effektivitaetsgrundsatz Aequivalenzgrundsatz effektiver Rechtsschutz Staatshaftung Francovich. Output: Effektivitaets-Prüfmemo Klageoptionen. Abgrenzung: nicht für allgemeines Verfahrensrecht. |
| `europarecht-vorlageverfahren-art-267` | Vorabentscheidungsersuchen nach Art. 267 AEUV vorbereiten oder Vorlagepflicht eines nationalen Gerichts prüfen. Art. 267 AEUV Vorabentscheidungsverfahren. Prüfraster: Vorlagepflicht acte-clair-Doktrin Vorlagefrage Formulierung Aussetzung nationale Verfahrensposition. Output: Vorlagefragentwurf Vorlage-Memo. Abgrenzung: nicht für Klagen unmittelbar beim EuGH (europarecht-klagearten-eugh). |
| `spezial-denkfehler-fristen-form-und-zustaendigkeit` | Denkfehler: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin europarecht kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Europarecht (EuGH, EU-Kommission) gilt für **Nationales Verfahren Vorlageverfahren ART**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `europarecht-nationales-verfahren-effektivitaet`

**Fokus:** EU-Rechtsvorgaben zum effektiven nationalen Rechtsschutz prüfen wenn nationales Verfahren EU-Rechte beeintraechtigt. Art. 47 GRC Art. 19 EUV Effektivitaetsprinzip. Prüfraster: Effektivitaetsgrundsatz Aequivalenzgrundsatz effektiver Rechtsschutz Staatshaftung Francovich. Output: Effektivitaets-Prüfmemo Klageoptionen. Abgrenzung: nicht für allgemeines Verfahrensrecht.

# Nationales Verfahren und Effektivität

## Zweck

Fristen, Präklusion, Beweislast, Bestandskraft und Eilrechtsschutz werden auf EU-Effektivität geprüft.

## Wann verwenden

- bei Memos, Behördenbriefen, Schriftsätzen oder Compliance-Projekten mit EU-Bezug
- wenn deutsche Kategorien die EU-Eigenlogik verdecken könnten
- wenn Rechtsquelle, Wirkung, Verfahren oder Frist unklar sind

## Arbeitsweise

1. **Rechtsquelle fixieren.** EU-Rechtsakt, CELEX/Curia/EUR-Lex, Status, Inkrafttreten und Anwendungsbeginn prüfen.
2. **Wirkung bestimmen.** Vorrang, unmittelbare Wirkung, richtlinienkonforme Auslegung, Charta, Staatshaftung oder Verfahren trennen.
3. **Deutsche Denkfehler markieren.** Nationale Kategorien nur nutzen, wenn sie unionsrechtlich passen.
4. **Verfahrensweg planen.** Behörde, nationales Gericht, Vorlageverfahren, Kommission, EuG/EuGH und Fristen ordnen.
5. **Qualitätstor setzen.** Quellenstand, nationale Umsetzung, offene Vorlagefrage und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Vorrang nicht mit Nichtigkeit der nationalen Norm gleichsetzen.
- Richtlinie, Verordnung, Beschluss und Soft Law nicht vermischen.
- Charta nicht ohne Durchführung von Unionsrecht anwenden.
- Keine CELEX- oder EuGH-Fundstelle erfinden.

## Ton

Europarecht-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Triage vor Pruefung Effektivitaetsgrundsatz

Bevor losgelegt wird, klaere:
1. Macht der Mandant ein EU-Recht vor einem nationalen Gericht geltend?
2. Haelt das nationale Verfahrensrecht die Durchsetzung dieses Rechts praktisch unmoeglich oder uebermäßig erschwert (Effektivitaetsgrundsatz)?
3. Sind nationale Verfahrensregeln diskriminierend im Vergleich zu rein nationalen Anspruechen (Aequivalenzgrundsatz)?
4. Besteht ein Anspruch auf einstweiligen Rechtsschutz bis zur EuGH-Entscheidung (Zuckerfabrik-Doktrin)?

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette

- **Art. 47 GRCh** — Recht auf wirksamen Rechtsbehelf; effectivite-Grundsatz
- **Art. 4 Abs. 3 EUV** — Kooperationspflicht; effektive Durchsetzung EU-Recht
- **Art. 19 Abs. 1 EUV** — Mitgliedstaatliche Gerichte als EU-Gerichte erster Instanz
- **§§ 33 ff. GWB** — Schadensersatz im Kartellrecht (Umsetzung Richtlinie 2014/104)

## Output-Template: Verfahrensrechtliche Ruege

**Adressat:** Nationales Gericht
**Tonfall:** Argumentativ; Effektivitaet-Argument klar herausgestellt

```
VERFAHRENSRECHTLICHE RUEGE (EFFEKTIVITAET EU-RECHT)
In der Sache: [PARTEIEN AZ]

Rechtliche Ruege:
Die [VERFAHRENSREGEL / FRISTEN-/BEWEISREGEL] des nationalen Rechts
macht die Durchsetzung des EU-Rechts-Anspruchs aus [Art. X AEUV /
VO / RL] praktisch unmoeglich im Sinne des Effektivitaetsgrundsatzes.

Begruendung:
[Vergleich: gleichartiger nationaler Anspruch haette gueanstigere
Verfahrensregel — Aequivalenz verletzt / ODER Verfahrensregel
erschwert EU-Recht-Durchsetzung unverhältnismaessig]

Folge:
Das Gericht ist verpflichtet, die nationale Verfahrensregel unangewendet
zu lassen (EuGH Rewe; Costa/ENEL) oder vorlaeufigen Rechtsschutz zu
gewaehren (Zuckerfabrik).

Vorlage Art. 267 AEUV:
Falls Zweifel an der Vereinbarkeit bestehen, regen wir Vorlage an den
EuGH an. Vorlagefrage: [FORMULIERUNG]

[KANZLEI], [ORT], [DATUM]
```

## 2. `europarecht-vorlageverfahren-art-267`

**Fokus:** Vorabentscheidungsersuchen nach Art. 267 AEUV vorbereiten oder Vorlagepflicht eines nationalen Gerichts prüfen. Art. 267 AEUV Vorabentscheidungsverfahren. Prüfraster: Vorlagepflicht acte-clair-Doktrin Vorlagefrage Formulierung Aussetzung nationale Verfahrensposition. Output: Vorlagefragentwurf Vorlage-Memo. Abgrenzung: nicht für Klagen unmittelbar beim EuGH (europarecht-klagearten-eugh).

# Vorlageverfahren Art. 267 AEUV

## Zweck

Vorlagefragen werden nicht als getarnte Subsumtion formuliert, sondern als echte EU-Auslegungs- oder Gültigkeitsfragen.

## Wann verwenden

- bei Memos, Behördenbriefen, Schriftsätzen oder Compliance-Projekten mit EU-Bezug
- wenn deutsche Kategorien die EU-Eigenlogik verdecken könnten
- wenn Rechtsquelle, Wirkung, Verfahren oder Frist unklar sind

## Arbeitsweise

1. **Rechtsquelle fixieren.** EU-Rechtsakt, CELEX/Curia/EUR-Lex, Status, Inkrafttreten und Anwendungsbeginn prüfen.
2. **Wirkung bestimmen.** Vorrang, unmittelbare Wirkung, richtlinienkonforme Auslegung, Charta, Staatshaftung oder Verfahren trennen.
3. **Deutsche Denkfehler markieren.** Nationale Kategorien nur nutzen, wenn sie unionsrechtlich passen.
4. **Verfahrensweg planen.** Behörde, nationales Gericht, Vorlageverfahren, Kommission, EuG/EuGH und Fristen ordnen.
5. **Qualitätstor setzen.** Quellenstand, nationale Umsetzung, offene Vorlagefrage und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Vorrang nicht mit Nichtigkeit der nationalen Norm gleichsetzen.
- Richtlinie, Verordnung, Beschluss und Soft Law nicht vermischen.
- Charta nicht ohne Durchführung von Unionsrecht anwenden.
- Keine CELEX- oder EuGH-Fundstelle erfinden.

## Ton

Europarecht-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Triage vor Vorlage-Entscheidung

Bevor losgelegt wird, klaere:
1. Besteht eine Frage zur Gueltigkeit oder Auslegung von EU-Recht, die fuer den Ausgang des Verfahrens entscheidend ist?
2. Ist das nationale Gericht letztinstanzlich (Vorlagepflicht) oder nicht-letztinstanzlich (Vorlagemaessen)?
3. Hat der EuGH die Frage bereits eindeutig geklart (Acte clair) oder ist sie offenkundig eindeutig (Acte eclaire)?
4. Kann Vorlage die Verfahrensdauer akzeptabel verlaengern (EuGH: ca. 12-18 Monate)?
5. Welche Fragestellung ist am ehesten geeignet fuer das Vorlageurteil?

## Vertiefung: Rechtsprechung und Leitsaetze

Klassische Anker zur Vorlagedogmatik (vor Verwendung über [curia.europa.eu](https://curia.europa.eu/) im Volltext nachschlagen):

- EuGH, Urt. v. 06.10.1982 — Rs. 283/81 (CILFIT) — Acte-clair-Doktrin; Voraussetzungen für Verzicht auf Vorlage durch letztinstanzliches Gericht.
- EuGH, Urt. v. 06.10.2021 — C-561/19 (Consorzio Italian Management) — Präzisierung CILFIT; strenge Begründungsanforderung.
- EuGH, Urt. v. 09.09.2015 — C-160/14 (Ferreira da Silva) — Vorlagepflicht trotz innerstaatlich divergierender Entscheidungen.
- Aktuelle Linie 2025/2026 zu Vorlagepflicht und Staatshaftung wegen Vorlageverstoßes im Mandat live verifizieren.

## Normen-Kette Vorlageverfahren

- **Art. 267 AEUV** — Vorlagerecht (Abs. 2) und Vorlagepflicht (Abs. 3) bei Letztinstanzgerichten
- **Art. 19 EUV** — Effektiver Rechtsschutz; Vorlage als Instrument
- **EuGH-Satzung Art. 23** — Beteiligte im Vorabentscheidungsverfahren
- **EuGH-Verfahrensordnung Art. 93-118** — Ablauf Vorabentscheidungsverfahren
- **Eiliges Vorabentscheidungsverfahren (PPU)** Art. 107 EuGH-VerfO — fuer Freiheits-/Haftfragen; Frist ca. 2 Monate

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Vorlagebeschluss-Entwurf (Kurzform)

**Adressat:** EuGH / zu erstellendes Vorlage-Gericht
**Tonfall:** Formal-juristisch; klare Vorlagefrage

```
VORLAGEBESCHLUSS (ENTWURF)
Vorlegendes Gericht: [GERICHT, LAND]
Az.: [AZ]

Parteien:
[KLAEGER / BEKLAGTER]

Sachverhalt (Kurzfassung):
[3-5 Saetze zum entscheidungserheblichen Sachverhalt]

Anzuwendende EU-Rechtsnormen:
[Art. X VO (EU) / Richtlinie / AEUV]

Vorlagefrage(n) an den EuGH (Art. 267 AEUV):

1. Ist Art. [X] der [VO / Richtlinie] dahingehend auszulegen, dass
 [KONKRETE FRAGE]?

[2. Falls ja / Hilfsfrage: ...]

Begruendung der Erheblichkeit:
Die Frage ist entscheidungserheblich, weil bei Bejahung [RECHTSFOLGE A]
und bei Verneinung [RECHTSFOLGE B] eintreten würde.

Begruendung keine Acte clair:
Der EuGH hat diese Frage noch nicht entschieden / Die Entscheidung [CELEX]
klaert die Frage nicht vollstaendig fuer den vorliegenden Sachverhalt.

[GERICHT], [ORT], [DATUM]
[RICHTER-NAME]
```

## 3. `spezial-denkfehler-fristen-form-und-zustaendigkeit`

**Fokus:** Denkfehler: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin europarecht kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Denkfehler: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Denkfehler: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Denkfehler: Fristen, Form, Zuständigkeit und Rechtsweg / denkfehler fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Denkfehler** prüfen.
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
