---
name: erzeugung-leitfaden-erstellen-mandanten
description: "Erzeugung Leitfaden Erstellen Mandanten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Erzeugung Leitfaden Erstellen Mandanten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Erzeugung Leitfaden Erstellen Mandanten** im Plugin Rechtsberatungsstelle (RDG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `formular-erzeugung` | Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behoerde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozialrecht Mietrecht Arbeitsrecht. Prüfraster Formular-Typ bestimmen, Pflichtfelder ermitteln, Rückfragen minimal halten, Fristen beachten. Output ausgefuelltes Formular oder Antragsentwurf mit Einreichungshinweisen. Abgrenzung zu Entwurf für individuelle Schriftsaetze und zu Mandantenbrief. |
| `leitfaden-erstellen` | Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache. BeratungsHiG niedrigschwellige Beratung, Verbraucherrecht Mietrecht Arbeitsrecht. Prüfraster Zielgruppe und Sprachniveau, Rechtsgebiet und Kern-Probleme, Checkliste Handlungsschritte, Fristen und Risiken. Output Leitfaden in verstaendlicher Sprache mit Schritt-fuer-Schritt-Anleitung und Norm-Referenzen. Abgrenzung zu Einarbeitung-Skill für Ausbilder-Training und zu Recherche-Start. |
| `mandanten-kommunikations-log` | Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO Datenschutz studentische Rechtsberatung, § 43a BRAO Vertraulichkeit, BDSG. Prüfraster Gespraeach-Datum Inhalt Ergebnis und Naechste Schritte protokollieren, Datenschutz beachten, Übergabe an anderen Berater sicherstellen. Output Kommunikations-Log mit strukturiertem Protokoll und Weiterleitungshinweisen. Abgrenzung zu Semester-Übergabe für Mandats-Übergabe und zu Status-Skill. |

## Arbeitsweg

Im Plugin Rechtsberatungsstelle (RDG) gilt für **Erzeugung Leitfaden Erstellen Mandanten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `formular-erzeugung`

**Fokus:** Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behoerde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozialrecht Mietrecht Arbeitsrecht. Prüfraster Formular-Typ bestimmen, Pflichtfelder ermitteln, Rückfragen minimal halten, Fristen beachten. Output ausgefuelltes Formular oder Antragsentwurf mit Einreichungshinweisen. Abgrenzung zu Entwurf für individuelle Schriftsaetze und zu Mandantenbrief.

# [VERALTET] Formularerstellung → siehe `/entwurf`

## Zweck

Diese Skill wurde im Rahmen des Umbaus auf Version 2 vollständig in `skills/entwurf/` überführt. Der Befehl `/entwurf` übernimmt alle Aufgaben, die zuvor hier lagen: Erstellung von Erstentwürfen für Antragsformulare (Beratungshilfe-Antrag BerH 1, PKH-Antrag nach § 117 ZPO, Widerspruchsvordrucke, Behördenformulare), Ausfüllen aus Fallnotizen, Rechtsgebiet-spezifische Muster und formvorschriftengerechte Formatierung.

Die Skill nimmt keine Eingaben mehr entgegen und erzeugt keine Ausgaben. Sie verbleibt im Dateisystem als Migrationshinweis für ältere Dokumentationen und Semesterskripte.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Formular- und Schriftstückaufgaben: `/entwurf [Schriftstücktyp]`.

## Rechtlicher Rahmen

### Hintergrund der Zusammenführung

Die Trennung zwischen "Formularerstellung" und "Schriftsatzerstellung" war in der Praxis studentischer Rechtsberatungsstellen künstlich: Ein Beratungshilfe-Antrag (BerH 1) ist juristisch kein anderes Arbeitsergebnis als ein Widerspruchsschreiben — beide erfordern Sachverhaltsaufnahme, Normprüfung und Supervisoren-Freigabe nach § 6 Abs. 2 RDG.

### Relevante Normen für die Nachfolge-Skill `/entwurf`

- **§ 1 BerHG** — Voraussetzungen der Beratungshilfe: BerH 1-Antrag ist vor Leistungserbringung beim Amtsgericht einzureichen; Studierende müssen die Voraussetzungen (Bedürftigkeit, keine anderweitige Beratungsmöglichkeit) prüfen.
- **§ 117 ZPO** — PKH-Antrag: Einreichung mit Klage oder gesondertem Schriftsatz; wirtschaftliche Verhältnisse vollständig darlegen (Erklärung über persönliche und wirtschaftliche Verhältnisse, Formular bewilligen PKH-Schein).
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Ausgefüllte Formulare, die Rechtspositionen des Mandanten begründen oder geltend machen, sind keine formale Routineaufgabe — sie erfordern inhaltliche Supervisoren-Prüfung.
- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht: Formulare enthalten sensitive Mandantendaten; strenge Vertraulichkeit.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

**Stattdessen `/entwurf [Schriftstücktyp]` verwenden.**

```
/entwurf beratungshilfe-antrag
/entwurf pkh-antrag
/entwurf widerspruch-nebenkostenabrechnung
/entwurf mahnschreiben
```

Vollständiger Ablauf in `skills/entwurf/SKILL.md`:

1. Schriftstücktyp identifizieren und dem Musterbestand zuordnen
2. Sachverhalt aufnehmen; fehlende Angaben kennzeichnen (`[TATSACHE FEHLT: ...]`)
3. Formvorschriften und Einreichungsweg prüfen
4. Entwurf erstellen mit `[PRÜFEN]`- und `[UNSICHER]`-Flags
5. Supervisoren-Routing nach § 6 Abs. 2 RDG

## Ausgabeformat

Keine Ausgabe — diese Skill ist inaktiv. Weiterleitung auf `/entwurf`.

## Beispiel

Statt `/formular-erzeugung beratungshilfeantrag`:

```
/entwurf beratungshilfe-antrag
```

Der Befehl `/entwurf` füllt das Formular BerH 1 aus den Fallnotizen, kennzeichnet fehlende Pflichtangaben mit `[TATSACHE FEHLT: ...]` (z. B. Kontonummer für Bedürftigkeitsnachweis), und leitet nach Fertigstellung in die Supervisoren-Prüfung.

## Risiken und typische Fehler

- **Verweis auf diese Skill in älteren Unterlagen:** Bestehende Handreichungen, Semesterskripte oder Tutorenmaterialien, die auf `/formular-erzeugung` verweisen, auf `/entwurf` umschreiben.
- **Formularausfüllung als Routineaufgabe unterschätzen:** Formulare, die Rechtspositionen des Mandanten geltend machen (PKH, Beratungshilfe, Widerspruch), sind rechtliche Arbeitsergebnisse und unterliegen der Supervisoren-Prüfpflicht nach § 6 Abs. 2 RDG.
- **Falsche Angaben im BerH 1-Antrag:** Unvollständige oder unrichtige Angaben zur Bedürftigkeit können zu Ablehnung und ggf. zur Rückforderung bereits gewährter Beratungshilfe führen (§ 9 BerHG).

## Quellenpflicht

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben bei konkreten Schriftstücken und Formularen: `skills/entwurf/SKILL.md`, Sektion "Quellenpflicht".

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund: GELOESCHT. Echtes Datum 22.10.2015 (Skill hatte 14.01.2016); echtes Thema Streitwert der Vollstreckungsgegenklage (§§ 3, 4 ZPO) — kein Bezug zu Beratungshilfe oder anwaltlicher Antragspruefungspflicht. Quelle: dejure.org/2015,32471. Ersatz: kein passender Beleg gefunden; Zeile entfernt.
-->

## 2. `leitfaden-erstellen`

**Fokus:** Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache. BeratungsHiG niedrigschwellige Beratung, Verbraucherrecht Mietrecht Arbeitsrecht. Prüfraster Zielgruppe und Sprachniveau, Rechtsgebiet und Kern-Probleme, Checkliste Handlungsschritte, Fristen und Risiken. Output Leitfaden in verstaendlicher Sprache mit Schritt-fuer-Schritt-Anleitung und Norm-Referenzen. Abgrenzung zu Einarbeitung-Skill für Ausbilder-Training und zu Recherche-Start.

# /leitfaden-erstellen

1. Lade `CLAUDE.md` → Rolle (muss Anleitender Volljurist sein), Fachbereiche, Rechtsgrundlage.
2. Nutze den untenstehenden Ablauf.
3. Wenn der Nutzer kein Anleitender Volljurist ist: Stopp und weiterleiten (Studierende → `/rechtsberatungsstelle:einarbeitung`).
4. Durchlaufe: Fachbereich → Intake-Fragen → Pädagogikhaltung → Prüfungsgates → Querprüfungen → örtliche Besonderheiten.
5. Schreibe `guides/<fachbereich>.md`. Erstelle das Verzeichnis `guides/` bei Bedarf.
6. Biete einen Testlauf an: `/rechtsberatungsstelle:entwurf` unter der konfigurierten Haltung ausführen, damit der Anleiter sieht, was Studierende sehen.

---

# Build Guide: Anleitungsgeführter Fachbereichsleitfaden


## Triage zu Beginn
1. Fuer welchen Fachbereich soll der Leitfaden erstellt werden (Mietrecht, Sozialrecht, Aufenthaltsrecht, Strafrecht)?
2. Welche Paedagogikhaltung soll der Leitfaden vorgeben: ausfuehren, anleiten oder lehren?
3. Gibt es einen bestehenden Leitfaden, der ueberarbeitet werden soll, oder wird er neu erstellt?
4. Welche spezifischen Prüfungsgates und RDG-Grenzen sollen fuer diesen Fachbereich konfiguriert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Erlaubnisfreie Rechtsberatung in Beratungsstellen unter Anleitung eines Volljuristen; Leitfaden konfiguriert den Anleitungsrahmen
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des anleitenden Anwalts: gilt auch fuer Leitfaden-Inhalte und Mandatsdaten
- § 203 Abs. 4 StGB — Einbeziehung Dritter (Studierende) erfordert vertragliche Absicherung der Verschwiegenheit
- § 43a Abs. 4 BRAO i.V.m. § 3 BORA — Interessenkonflikt-Regeln muessen im Leitfaden fuer jeden Fachbereich verankert sein

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Der Anleiter-Leitfaden ist der Regler, der studierendengerichtete Skills von "Arbeit erledigen" auf "Studierenden die Arbeit lehren" umstellt. Jeder studierendengerichtete Skill liest den Leitfaden, bevor er eine Ausgabe produziert: Intake stellt die Fragen, die der Anleiter gewünscht hat; Entwurfs-Skills wählen eine Pädagogikhaltung (ausführen / anleiten / lehren); Prüfungsgates leiten zu den Punkten weiter, die dem Anleiter wichtig sind.

**Zielgruppe: der anleitende Volljurist.** Nicht Studierende. Studierende starten mit `/rechtsberatungsstelle:einarbeitung`.

## Berufsrechtlicher Rahmen

Dieser Leitfaden ist ein internes Konfigurationsdokument. Er legt fest, wie die Beratungsstelle nach § 6 Abs. 2 Nr. 2 RDG betrieben wird:

- **§ 6 Abs. 2 Nr. 2 RDG:** Unentgeltlichkeit und Anleiterpflicht sind in jedem Leitfaden zu verankern.
- **§ 43a Abs. 2 BRAO:** Verschwiegenheit des Anleiters erstreckt sich auf alle im Rahmen der Beratungsstelle erlangten Informationen.
- **§ 43a Abs. 4 BRAO / BORA § 3:** Der Leitfaden muss Konfliktprüfungsregeln für den Fachbereich enthalten.
- **Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 44–52:** Anforderungen an die Anleitungsorganisation.

## Schlüsselinhalte des Leitfadens

Biete dies als Checkliste an, die der Anleiter durcharbeiten oder als Inhaltsverzeichnis nutzen kann:

- Was müssen Studierende wissen, bevor sie einen Fall berühren? (Verschwiegenheit nach § 43a BRAO analog / § 203 StGB; RDG-Grenzen; Umfang ihrer Befugnisse)
- Was sind die 3–5 häufigsten Fehler von Studierenden in diesem Fachbereich, und wie soll der Skill sie erkennen?
- Wann muss der Studierende pausieren und Rücksprache halten? (Einreichung, Versand, Strategieentscheidung, Vergleich)
- Welches Sprachniveau ist für Mandantenmitteilungen anzustreben? (Leichte Sprache Niveau B1/B2 als Ziel bei Mandanten ohne juristische Vorbildung; ggf. mehrsprachig bei Geflüchteten)
- Welche örtlichen Sonderregeln, Formulare oder Fristen muss jede Studierende kennen?
- Wann soll der Skill lehren statt tun? (Je Dokumenttyp – Default und Ausnahmen festlegen)

## Ablauf

### Schritt 1: Rollenprüfung

Dies ist ein Anleiter-Skill. Lies `CLAUDE.md` → `Rolle`. Wenn die Rolle nicht "Anleitender Volljurist" ist:

> Dieser Skill ist für Anleiter – er konfiguriert das Verhalten der studierendengerichteten Skills. Wenn Sie der Anleiter sind, stellen Sie sicher, dass Ihre Rolle in `/rechtsberatungsstelle:rechtsberatungsstelle-kaltstart-interview` auf "Anleitender Volljurist" gesetzt ist. Wenn Sie Studierende/r sind, ist dies nicht der richtige Skill für Sie – starten Sie mit `/rechtsberatungsstelle:einarbeitung`.

Stopp, wenn Rolle nicht Anleiter.

### Schritt 2: Fachbereich?

> Für welchen Fachbereich soll dieser Leitfaden gelten? (Asyl/Aufenthaltsrecht | SGB II/Bürgergeld | Mietrecht | Verbraucherrecht | Familienrecht | SGB IX/Eingliederungshilfe | Sonstiges)

Falls "Sonstiges": Kurzname erfragen → wird zum Dateinamen (Kleinbuchstaben, Bindestriche: `asyl.md`, `sgbii.md`, `mietrecht.md`).

Prüfe die in `CLAUDE.md` → `Fachbereiche` eingetragenen Bereiche. Wenn der gewählte Bereich dort nicht aufgeführt ist, hinweisen.

Falls ein Leitfaden für diesen Bereich bereits existiert: "Möchten Sie (a) abschnittsweise überarbeiten, (b) neu aufbauen und überschreiben, oder (c) zunächst den bestehenden Leitfaden sehen?"

### Schritt 3: Intake-Fragen

> Was sollten Studierende eine neue Mandantin/einen neuen Mandanten für diesen Fachbereich fragen? Ich starte mit einem generischen Intake für [Fachbereich] – sagen Sie mir, was hinzugefügt, entfernt oder geändert werden soll. Welche Warnsignale sollten Studierende erkennen? Welche Fälle passen gut zur Beratungsstelle, welche sollten weitervermittelt werden?

Fachbereichs-Defaults (wenn keine Angaben vorhanden):

**Asyl/Aufenthaltsrecht:**
- Aktueller Status und Einreisezeitpunkt (Datum für Jahresfrist § 74 AsylG wichtig!)
- Laufende Verfahren: BAMF-Bescheid erhalten? Klage eingereicht?
- Besondere Vulnerabilität: Minderjährigkeit, Traumatisierung, Behinderung (§ 76b SGB IX)
- Familienangehörige und deren Status
- Vorstrafen (mit Sensibilität erfragen – § 3 AsylG, § 60 AufenthG prüfen)
- Sprachkenntnisse / Dolmetscherbedarf
- Dringlichkeit: Zustellungsdatum des Bescheids? Klagefrist (§ 74 AsylG: 2 Wochen bei § 36-Bescheid!)?

**SGB II / Bürgergeld:**
- Aktueller Leistungsbezug / zuletzt erhaltener Bescheid
- Anlass: Bewilligungs-, Änderungs- oder Ablehnungsbescheid? Sanktionsbescheid?
- Einkommensverhältnisse, Vermögen (§§ 11–12 SGB II)
- Unterkunftskosten (§ 22 SGB II – Angemessenheit prüfen)
- Widerspruchsfrist: 1 Monat ab Bekanntgabe (§ 84 SGG)
- Vorherige Kontakte mit dem Jobcenter (Widersprüche, Klagen)

**Mietrecht:**
- Art des Mietverhältnisses (privat, sozial, öffentlich-gefördert)
- Anlassfall: Kündigung, Mieterhöhung, Mängel, Kaution, Modernisierung?
- Mietvertrag und Mietdauer
- Dokumentation vorhandener Mängel (Fotos, Schriftverkehr)
- Mietspiegel des Ortes verfügbar? (z. B. Berliner Mietspiegel 2023/2024)
- Dringlichkeit: Räumungsklage? Gerichtstermin?

### Schritt 4: Pädagogikhaltung

Drei Stufen – Anleiter wählt Default und kann je Dokumenttyp übersteuern:

| Haltung | Was der Skill tut | Geeignet für |
|---|---|---|
| **Ausführen** | Entwurf vollständig ausarbeiten; Studierende analysieren und übergeben | Routineschriftsätze im 3. Semester+ |
| **Anleiten** | Gliederung und Schlüsselpunkte ausgeben; Studierende füllen aus | Memos, neue Fachbereiche |
| **Lehren** | Nur Fragen stellen; Studierenden zur Lösung führen | 1. Semester, neue Fachbereiche, komplexe Rechtsfragen |

### Schritt 5: Prüfungsgates

> Welche Arten von Dokumenten oder Entscheidungen müssen zwingend zu Ihnen? Ich schlage vor: Klageerhebung, Widerspruch (bei kurzfristigen Rechtsbehelfsfristen sofort), alle Schriftsätze an Gericht, alle Mitteilungen an Mandanten mit konkretem Rechtsrat.

Anleiter kann die Gate-Liste erweitern, einschränken oder beibehalten.

### Schritt 6: Querprüfungen

Welche anderen Fachbereiche überschneiden sich regelmäßig?

- Asylmandate → fast immer SGB II/XII-Fragen (§ 7 Abs. 1 Satz 2 Nr. 1 SGB II: Leistungsausschluss für bestimmte Ausländer beachten!)
- Mietmandate → ggf. Sozialhilfe (§ 22 SGB II Unterkunftskosten), ggf. Familienrecht
- SGB II → Arbeitsrecht (Eingliederungsvereinbarung, Sanktionen bei Ablehnung von Arbeit)

### Schritt 7: Örtliche Besonderheiten

> Gibt es örtliche Regeln, Sonderformulare oder Fristen, die jede Studierende kennen muss? Welche lokalen Anlaufstellen (Gerichte, Behörden, Dolmetscherdienste, Kooperationspartner) sind wichtig?

**Berlin-Beispiele:**
- Berliner Mietspiegel 2023/2024 (qualifiziert nach § 558d BGB)
- Jobcenter-Bezirke Berlin (11 Bezirke) – Formulare und Zuständigkeiten
- BAMF-Außenstellen Berlin, Eisenhüttenstadt
- Pro Bono Berlin e. V. als Weitervermittlungspartner
- Berliner Beratungszentrum für Migration und Qualifizierung (BBZ)

**Bremen-Beispiele:**
- Jobcenter Bremen (zentral)
- BAMF Bremen
- Refugee Law Clinic Bremen (Uni Bremen) – Kooperationen möglich
- Caritasverband Bremen – Migrationsberatung
- Verbraucherzentrale Bremen

### Schritt 8: Leitfaden schreiben

Ausgabe: `guides/<fachbereich>.md` mit den Sektionen:
1. Fachbereichsüberblick und RDG-Grenzen
2. Intake-Fragen (Standard und Warnsignale)
3. Pädagogikhaltung (Default + Ausnahmen)
4. Prüfungsgates
5. Querprüfungen
6. Örtliche Besonderheiten und Weitervermittlung
7. Wichtige Fristen auf einen Blick
8. Empfohlene Quellen und Datenbanken

## Ausgabeformat

Supervisor-gerichtetes Konfigurationsdokument in Markdown. Kein `[KI-GESTÜTZTER ENTWURF]`-Vermerk – dies ist kein Studierenden-Output, sondern Anleiter-Konfiguration. Länge: 80–150 Zeilen pro Leitfaden.

## Risiken / typische Fehler

- **Fristenversäumnis:** Der Leitfaden muss für jeden Fachbereich die kritischsten Fristen explizit benennen. Besonders gefährlich: § 36 AsylG (1 Woche), § 74 AsylG (2 Wochen bei beschleunigtem Verfahren), § 4 KSchG (3 Wochen).
- **RDG-Grenzen nicht klar kommuniziert:** Studierende ohne klare Anleitungsstruktur überschreiten versehentlich § 3 RDG.
- **Fehlende Konfliktprüfung:** Ohne explizite Gate-Regel übersehen Studierende, wann sie den Anleiter einschalten müssen.
- **Sprachbarrieren bei Geflüchteten:** Leitfaden sollte Dolmetscherressourcen und Sprach-Level-Anforderungen an Mandantenbriefe festlegen.

## 3. `mandanten-kommunikations-log`

**Fokus:** Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO Datenschutz studentische Rechtsberatung, § 43a BRAO Vertraulichkeit, BDSG. Prüfraster Gespraeach-Datum Inhalt Ergebnis und Naechste Schritte protokollieren, Datenschutz beachten, Übergabe an anderen Berater sicherstellen. Output Kommunikations-Log mit strukturiertem Protokoll und Weiterleitungshinweisen. Abgrenzung zu Semester-Übergabe für Mandats-Übergabe und zu Status-Skill.

# /mandanten-kommunikations-log

1. Lade `CLAUDE.md` → Fachbereich, Aufsichtsmodell, Verschwiegenheitspflichten.
2. Prüfe: Handelt es sich um eine neue Kommunikation (→ Eintrag hinzufügen) oder um Abruf/Export (→ strukturierte Übersicht ausgeben)?
3. Erfasse alle relevanten Metadaten (Datum, Art, Beteiligte, Inhalt, Ergebnis, nächste Schritte).
4. Gib den neuen Logeintrag formatiert aus.
5. Weise auf offene Fristen und ausstehende Antworten hin.

---

# Mandantenkommunikations-Logbuch

## Zweck

Lückenlose Dokumentation aller Kontakte in einem Mandat ist aus mehreren Gründen unverzichtbar:

1. **Semesterübergabe:** Nachfolgende Studierende müssen den Stand des Mandats vollständig nachvollziehen können (`/rechtsberatungsstelle:semester-übergabe`).
2. **Haftungssicherung:** Im Streitfall muss nachgewiesen werden können, wann welche Mitteilung erging (§ 127 BGB analog für Fristwahrung).
3. **Qualitätssicherung:** Der anleitende Volljurist prüft, ob der Mandant korrekt informiert und keine unzulässige Rechtsberatung erteilt wurde.
4. **Verschwiegenheit:** Das Logbuch enthält personenbezogene Daten und fällt unter § 43a Abs. 2 BRAO (Anleiter), § 203 StGB (alle Beteiligten), DSGVO Art. 5, 9. Kein Zugang für Dritte ohne Freigabe.

## Berufsrechtlicher Rahmen

- § 43a Abs. 2 BRAO: Verschwiegenheitspflicht des anleitenden Anwalts.
- § 203 Abs. 1 Nr. 3 StGB: Unbefugte Offenbarung von Mandantengeheimnissen.
- § 50 BRAO: Aufbewahrungspflicht Mandantenakte mindestens 5 Jahre.
- DSGVO Art. 5 Abs. 1 lit. e: Speicherbegrenzung – keine unnötig langen Aufbewahrungszeiten.
- DSGVO Art. 9: Besondere Kategorien (Asylstatus, Gesundheitsdaten) – erhöhte Sorgfalt.

**Intern bleiben:** Logeinträge werden nicht an den Mandanten weitergegeben. Sie sind interne Arbeitsdokumentation.

## Eingaben

- Aktenzeichen oder anonyme Mandantenkennung (z. B. "M-2024-17")
- Datum und Uhrzeit des Kontakts
- Art des Kontakts: persönlich | telefonisch | schriftlich (Brief/E-Mail/Fax) | durch Dritte (Dolmetscher)
- Beteiligte: Studierender, Anleiter, Mandant, Behörde/Gericht, Dolmetscher
- Inhalt: Was wurde mitgeteilt / besprochen / vereinbart?
- Ergebnis: Was ist entschieden, was bleibt offen?
- Nächste Schritte und Fristen

## Logstruktur (Standardformat)

```
### Eintrag [Nummer] – [Datum] [Uhrzeit]

**Art:** [persönlich | telefonisch | schriftlich]
**Beteiligte:** [Studierender: Name/Kürzel] | [Anleiter: ✓ anwesend / – nicht anwesend] | [Mandant: ✓] | [Dolmetscher: Name/Sprache oder –]
**Gegenüber:** [Jobcenter Mitte Berlin | BAMF Bremen | VG Berlin | Mandant direkt | Sonstiges: ]
**Thema:** [Kurzbeschreibung, 1–2 Sätze]

**Inhalt:**
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

**Ergebnis / Stand:**
[Was ist beschlossen? Was wurde mitgeteilt? Was bleibt offen?]

**Offene Fristen:**
| Frist | Datum | Status |
|---|---|---|
| [z. B. Widerspruch SGB II] | [TT.MM.JJJJ] | [offen] |

**Nächste Schritte:**
1. [Aktion – verantwortlich: Studierender / Anleiter – bis: TT.MM.JJJJ]
2. …

**Verschwiegenheitshinweis:** Dieser Eintrag enthält vertrauliche Mandantendaten (§ 203 StGB, § 43a BRAO). Kein Zugang für Externe.
```

## Typische Kontaktarten und besondere Hinweise

### Erstgespräch / Intake
- Immer das Datum festhalten → Ausgangspunkt für Fristen (z. B. Jahresfrist AsylG § 74: Klagefrist läuft ab Bescheidzustellung, nicht ab Erstgespräch).
- Dokumentieren, ob Dolmetscher anwesend war und ob dieser selbst Verständlichkeit bestätigt hat.
- Datenschutz-Einwilligung des Mandanten nach Art. 13 DSGVO eingeholt?

### Behördenkontakt (Jobcenter, BAMF, Ausländerbehörde)
- Aktenzeichen der Behörde notieren.
- Bei telefonischen Auskünften: Name des Sachbearbeiters, Uhrzeit, Inhalt – wegen späterer Beweisbarkeit.
- Schriftliche Bestätigung mündlicher Auskünfte anfordern (Schreiben / E-Mail als Nachbeweis).

### Gerichtskontakt
- Geschäftsnummer des Gerichts notieren.
- Fristen aus dem Beschluss/Urteil sofort in `/rechtsberatungsstelle:fristen` eintragen.
- Termin für nächste Sitzung festhalten.

### Mandantenbrief / Schriftsatz
- Versanddatum und -weg (Brief mit Einschreiben / Fax mit Sendebericht / E-Mail mit Lesebestätigung) notieren.
- Anlagen auflisten.
- Freigabe durch Anleiter vor Versand? → Status "Freigabe erteilt von [Name/Kürzel] am [Datum]".

## Ablauf

### Schritt 1: Neuer Eintrag oder Abruf?

- Neue Kommunikation dokumentieren → Eingaben abfragen (Datum, Art, Beteiligte, Inhalt, Fristen).
- Bestehendes Log abrufen → Alle Einträge chronologisch ausgeben; Summary der offenen Fristen und nächsten Schritte.
- Log für Semesterübergabe exportieren → `/rechtsberatungsstelle:semester-übergabe` aufrufen.

### Schritt 2: Fristen prüfen

Nach jedem Eintrag automatisch prüfen:
- Gibt es neue Fristen aus diesem Kontakt?
- Sind bestehende Fristen durch diesen Kontakt beeinflusst (Hemmung, Verlängerung, Verkürzung)?
- Liegt eine kritische Frist innerhalb der nächsten 14 Tage?

Wenn ja: sofortige Benachrichtigung des Anleiters empfehlen.

### Schritt 3: Ausgabe

Strukturierter Logeintrag nach obigem Format. Immer mit Verschwiegenheitshinweis. Immer mit offenem Fristenstatus.

## Ausgabeformat

Markdown-Tabellen für Fristen. Bullet-Lists für Inhalt. Standardformat wie oben. Kein Fließtext-Protokoll – Bullets und Tabellen sind beim Semesterübergabe-Scan leichter zu lesen.

Jede Ausgabe trägt:
> **[INTERNES DOKUMENT – Vertraulich nach § 43a BRAO / § 203 StGB. Nicht für Mandanten oder Dritte bestimmt.]**

## Beispiel

### Eintrag 3 – 14.01.2025 14:30

**Art:** telefonisch
**Beteiligte:** Studierende: AS | Anleiter: – | Mandant: ✓ | Dolmetscher: Hamid Y. (Dari)
**Gegenüber:** Mandant direkt
**Thema:** Besprechung Widerspruchsergebnis Jobcenter – Bescheid vom 10.01.2025 erhalten

**Inhalt:**
- Mandant hat Bescheid vom Jobcenter Mitte Berlin (Az. 012345/24) am 12.01.2025 erhalten.
- Leistungen für Februar 2025 um 30 % abgesenkt (Sanktionsbescheid § 31a SGB II).
- Mandant versteht Bescheid nicht; Dolmetscher erklärt Inhalt auf Dari.
- Widerspruch soll eingelegt werden.

**Ergebnis / Stand:**
Mandant wünscht Widerspruch. Kopie des Bescheids wird per Post zugesandt. Frist läuft bis 12.02.2025 (1 Monat ab Bekanntgabe, § 84 SGG).

**Offene Fristen:**
| Frist | Datum | Status |
|---|---|---|
| Widerspruch SGB II § 84 SGG | 12.02.2025 | offen – dringend |

**Nächste Schritte:**
1. Entwurf Widerspruchsschreiben – verantwortlich: AS – bis: 20.01.2025
2. Freigabe durch Anleiter – bis: 28.01.2025
3. Versand per Einschreiben – bis: 10.02.2025 (Puffer)

**Verschwiegenheitshinweis:** Dieser Eintrag enthält vertrauliche Mandantendaten (§ 203 StGB, § 43a BRAO). Kein Zugang für Externe.

## Risiken / typische Fehler

- **Kein Versanddatum notiert:** Im Nachhinein nicht mehr beweisbar, ob eine Frist gewahrt wurde. Immer Einschreibebeleg aufbewahren und im Log festhalten.
- **Dolmetscher nicht dokumentiert:** Bei Sprachbarrieren ist der Nachweis, dass der Mandant den Inhalt verstanden hat, entscheidend (Aufklärungspflicht).
- **Offene Fristen nicht weitergegeben:** Beim Semesterwechsel sind nicht übergebene Fristen das größte Haftungsrisiko. Das Log ist die Grundlage für `/rechtsberatungsstelle:semester-übergabe`.
- **Personenbezogene Daten unverschlüsselt gespeichert:** DSGVO Art. 9 verlangt erhöhten Schutz für Asylstatus, Gesundheitsdaten. Kein Upload in unkonfigurierte Cloud-Systeme ohne Auftragsverarbeitungsvertrag (Art. 28 DSGVO).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
