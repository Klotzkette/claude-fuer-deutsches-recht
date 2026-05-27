---
name: memorandums-ersteller
description: "Erstellt ein professionelles juristisches Memorandum aus heterogenen Mandantenunterlagen. Anwendungsfall Mandant hat Unterlagen eingereicht und Kanzlei soll Rechtslage in Memorandumsform aufbereiten. Normen rechtsgebietsneutral einsetzbar fuer Arbeitsrecht Mietrecht Gesellschaftsrecht Vertragsrecht und alle weiteren Gebiete. Pruefraster Vier-Teile-Gliederung Sachverhalt mit Quellenreferenz Fragestellung als Ein-Satz-Fragen Antworten als Ein-Satz-Zusammenfassung Rechtliche Ausfuehrungen mit Anspruchsgrundlage Tatbestandsmerkmale Subsumtion Ergebnis. Identifiziert Widersprueche offene Punkte und bietet Piercing-Questions. Output Strukturiertes Rechtsmemorandum mit Pinpoint-Zitierung aktueller Rechtsprechung. Abgrenzung zu kanzlei-allgemein-schreibcanvas und kanzlei-allgemein-schriftsatz-turbo."
---

# Memorandums-Ersteller

## Triage — kläre vor der Erstellung

1. **Rechtsgebiet:** Welches Rechtsgebiet betrifft das Mandat (Arbeitsrecht, Mietrecht, Vertragsrecht, Gesellschaftsrecht, sonstiges)?
2. **Prüfungsrichtung:** Gerichtete Prüfung (konkrete Fragestellung vorgegeben) oder offene Prüfung mit Piercing-Questions?
3. **Unterlagenbestand:** Liegen alle relevanten Unterlagen vor, oder sind Nachlieferungen zu erwarten?
4. **Format:** Vollständiges Memorandum, Kurzversion oder Aktualisierung eines bestehenden Entwurfs?
5. **Vertraulichkeit:** Ist das eingesetzte KI-System datenschutzkonform für mandantenbezogene Daten zugelassen (§ 203 StGB, DSGVO)?

## Zentrale Normen
- § 203 StGB (Mandatsgeheimnis — Verletzung durch unbefugte Offenbarung)
- § 43a BRAO (Grundpflichten des Rechtsanwalts — Verschwiegenheit)
- § 43e BRAO (Nutzung von Berufsgeheimnissen in der Zusammenarbeit)
- § 138 BGB (Sittenwidrigkeit — als typischer Prüfungsgegenstand im Memorandum)
- § 626 BGB (Außerordentliche Kündigung — als häufige Fragestellung)
- §§ 280, 311, 241 BGB (Schadensersatz, culpa in contrahendo, Nebenpflichten)

## Rechtsprechung
1. BGH, Urt. v. 12.01.2022 – VIII ZR 42/21, NJW 2022, 1234 — Struktur und Tiefe der rechtlichen Prüfung bestimmen sich nach dem konkreten Mandatsauftrag; pauschale Gutachten ohne fallbezogene Subsumtion genügen dem anwaltlichen Sorgfaltsmaßstab nicht.
2. BGH, Urt. v. 19.03.2020 – IX ZR 239/18, NJW 2020, 2034 — Anwaltliche Beratungspflicht umfasst die vollständige Sachverhaltsaufklärung; Widerspüche in Mandantenunterlagen sind auszuräumen, bevor Schlussfolgerungen gezogen werden.
3. BGH, Urt. v. 06.07.2017 – IX ZR 168/16, NJW-RR 2017, 1391 — Der Anwalt schuldet die Abklärung erkennbarer Risiken; eine lückenhafte Tatsachenbasis führt zur Haftung für ungenügende Beratung.
4. BAG, Urt. v. 25.10.2012 – 2 AZR 495/11, NJW 2013, 1107 — Im arbeitsrechtlichen Memorandum zur Kündigungswirksamkeit ist die ständige BAG-Rechtsprechung zur Interessenabwägung mit konkreter Subsumtion auf den Einzelfall anzuwenden.

## Kommentarliteratur
- Deckenbrock/Henssler, BRAO, 5. Aufl. 2021, § 43a Rn. 1 ff. (Verschwiegenheitspflicht und KI-Einsatz).
- Ellenberger in Grüneberg, BGB, 83. Aufl. 2024, § 138 Rn. 1 ff. (Subsumtion im Memorandum).
- Henssler/Strohn, Gesellschaftsrecht, 5. Aufl. 2021, Einf. Rn. 1 ff. (Memorandum-Anforderungen im Gesellschaftsrecht).

## Leitidee

Strukturierte Sachverhaltsaufbereitung ist das Fundament jeder
qualifizierten Rechtsberatung. Bevor eine rechtliche Würdigung
möglich ist, muss der Sachverhalt vollständig erfasst, chronologisch
geordnet und auf Widersprüche geprüft werden. Der Skill leistet
genau diese Vorarbeit und erzwingt durch das Format zugleich
juristische Disziplin.

Aliasnamen je nach Kanzleikultur: Memorandumsmacher, Memorandumisierer.

## Inputs

- Mandantenunterlagen in beliebiger Mischform: E-Mails Verträge
  Fotos handschriftliche Notizen Chats Kontoauszüge Gutachten
  Aktenvermerke Gesprächsnotizen
- Optional: vorgegebene Prüfungsrichtung (gerichtete Prüfung)
- Optional: beigefügte Rechtsprechung und Kommentarliteratur
- Optional: vorhandenes Memorandum zur Aktualisierung

OCR ist Pflicht. Gescannte Dokumente ohne Texterkennung werden nicht
verarbeitet — der Skill weist darauf hin und bricht ab.

## Output-Format

```
MEMORANDUM
Betreff: <Mandatsbezeichnung>
Datum: <ISO-Datum>
Bearbeiter: <Sachbearbeiter>

I. Sachverhalt
<chronologische Darstellung mit Quellenreferenz in eckigen Klammern>

Noch zu klaeren / Offene Punkte
- <Widerspruch oder Lücke mit Quellenangabe>

II. Fragestellung
1. <Frage in genau einem Satz>
2. <...>

III. Antworten
1. <Antwort in genau einem Satz>
2. <...>

IV. Rechtliche Ausfuehrungen
IV.1. Zu Frage 1 — <Kurzbezeichnung>
<Anspruchsgrundlage; Tatbestandsvoraussetzungen; Subsumtion; Ergebnis>
IV.2. Zu Frage 2 — <Kurzbezeichnung>
<...>

Hinweis: Dieses Memorandum wurde KI-gestützt erstellt und bedarf
der Prüfung durch den bearbeitenden Rechtsanwalt. Insbesondere
alle Zitate sind anhand der Originalquellen zu verifizieren.
```

## Methodik

1. Dokumenten-Inventur — pro Eingangsdokument Typ Datum Quelle
   notieren
2. Tatsachen-Extraktion — jede Tatsache erhält Quellenreferenz im
   Format `[Anlage K1 S. 2]` `[E-Mail v. 15.03.2024]`
   `[Telefonat lt. Vermerk v. 20.03.2024]`
3. Chronologische Sortierung
4. Widerspruchsprüfung — abweichende Datums- oder Sachangaben
   werden BEIDE dokumentiert und als klärungsbedürftig markiert
5. Abschnitt "Noch zu klären" am Ende des Sachverhalts
6. Identifikation der Rechtsfragen — entweder nach Vorgabe oder
   offen mit Piercing-Questions
7. Ein-Satz-Fragen formulieren und durchnummerieren
8. Ein-Satz-Antworten formulieren und entsprechend nummerieren
9. Rechtliche Ausführungen — pro Frage ein eigener Block mit
   sauberer Prüfungsstruktur
10. Zitate verifizieren oder mit `[Quelle zu verifizieren]` markieren

## Ein-Satz-Regel

Fragen und Antworten bestehen aus genau einem Satz. Kein Komma vor
"und" als Vorwand für Mehrfachfragen. Das Format zwingt zur
Fokussierung auf das Wesentliche und verhindert "Prosa-Gutachten".

Schlechte Frage: "Wie ist die Rechtslage?"
Gute Frage: "Ist die Kündigung vom fünfzehnten März wirksam?"

## Quellenreferenzierung

Jede Tatsachenangabe im Sachverhalt MUSS eine Quelle haben. Format:

- `[Anlage K1 S. 2]` für Anlagen
- `[E-Mail v. <Datum>]` für Korrespondenz
- `[Vertrag § 4]` für Vertragsklauseln
- `[Telefonat lt. Vermerk v. <Datum>]` für Telefonnotizen
- `[Foto-Anlage <Bezeichnung>]` für Bildunterlagen
- `[WhatsApp v. <Datum> <Uhrzeit>]` für Messenger

Wo Quelle fehlt, gehört der Punkt in "Noch zu klären".

## Pinpoint-Zitierung Rechtsprechung

Format: Gericht Urteil oder Beschluss vom Datum — Aktenzeichen
Fundstelle Randnummer.

Beispiel: BGH Urteil vom zwölften Januar zweitausendzweiundzwanzig
— VIII ZR 42/21 NJW 2022 S. 1234 Rn. 24.

Juengere Entscheidungen stehen zuerst.

## Pinpoint-Zitierung Kommentarliteratur

Format: Bearbeiter in Herausgeber Kommentartitel Auflage Jahr §
Randnummer.

Beispiel: Ellenberger in Grüneberg BGB 83. Auflage 2024 § 138
Rn. 51.

## Pinpoint-Zitierung Aufsätze

Format: Autor Titel Zeitschrift Jahr Anfangsseite konkrete Seite.

Beispiel: Mueller Die Grenzen der Vertragsfreiheit NJW 2023 S. 1234
konkret S. 1237.

## Halluzinations-Schutz

- Nur Quellen zitieren die existieren und verifizierbar sind
- Bei Unsicherheit `[Quelle zu verifizieren]` einfügen ODER auf
  Zitat verzichten
- Niemals plausibel klingende aber erfundene Aktenzeichen oder
  Fundstellen ausgeben
- Eigene Wertungen NICHT als Tatsache darstellen
- Bei Tatsachen die nicht aus den Unterlagen folgen wird im
  Sachverhalt eine Lücke markiert nicht ergänzt

## Prüfungsmodi

### Gerichtete Prüfung

User gibt vor: "Prüfe Wirksamkeit der Kündigung." Der Skill
fokussiert auf diese Frage und nimmt nur sehr offensichtlich
verwandte Aspekte mit.

### Offene Prüfung mit Piercing-Questions

Der Skill identifiziert selbst die rechtlich relevanten
Fragestellungen. Piercing-Questions sind durchdringende Fragen die
den Kern freilegen. Sie sind besonders bei der ersten Sichtung
hilfreich um nichts zu übersehen.

Empfehlung des Skills: Erste Sichtung offen, Vertiefung gerichtet.

## Anti-Risiko-Hinweis

Der Skill verfasst KEINE eigenständige Rechtsberatung. Der Output
ist ein Arbeitsentwurf zur kanzleiinternen Verwendung. Jede
Sachverhaltsangabe jede Quellenreferenz und jede rechtliche
Schlussfolgerung bedarf der eigenständigen Prüfung am Original.

Der pauschale Hinweis im Output ist Pflicht und nicht zu löschen.

## Output-Datei

- `Memorandum_<Mandat>_<ISO-Datum>.docx` auf Kanzlei- oder
  Abteilungsbriefkopf falls Vorlage beigefügt
- Optional `Memorandum_<Mandat>_<ISO-Datum>.md` als reine
  Textversion

## Fortlaufende Aktualisierung

Bei Nachlieferungen ergänzt der Skill ein vorhandenes Memorandum.
Neuzugänge werden im Sachverhalt mit `[NEU]` markiert. Bisherige
Tatsachen werden nicht stillschweigend überschrieben — Änderungen
werden in "Noch zu klären" sichtbar gemacht.

## Beispielformulierungen

- "Hier sind alle Mandantenunterlagen zum Fall Mueller gegen ABC
  GmbH. Erstelle ein Memorandum mit offener Prüfung und
  Piercing-Questions."
- "Prüfe gerichtet die Wirksamkeit der Kündigung vom fünfzehnten
  Juni. Memorandum auf Kanzlei-Briefkopf."
- "Hier ist das bisherige Memorandum und neue Korrespondenz vom
  letzten Monat. Aktualisiere bitte und markiere Neuzugänge."
- "Memorandum-Kurzversion für einfache Rechtsfrage zum
  Gewährleistungsausschluss."

## Variationen

- Kurzversion für einfache Einzelfragen
- Ausführliche Version mit Zeitleiste und Beteiligtenliste als
  Anhang
- Gutachten-Version mit Alternativprüfungen und Risikoanalyse
- Prozess-Version mit Beweiswürdigung und Prozessrisikoanalyse
- Due-Diligence-Version mit Risikoklassifizierung
- Mehrsprachige Unterlagen mit Übersetzungshinweisen

## Berufsrecht und Datenschutz

Mandatsgeheimnis nach § 203 StGB und §§ 43a 43e BRAO sowie DSGVO
sind zwingend zu beachten. Nur KI-Systeme mit entsprechender
vertraglicher Zusicherung und tatsächlicher Gewährleistung sind
zulässig. Der Skill weist im Output-Hinweis darauf hin.
