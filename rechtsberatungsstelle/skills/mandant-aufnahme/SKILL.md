---
name: mandant-aufnahme
description: "Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und muss Sachverhalt strukturiert erfassen Rechtsgebiet einordnen und naechste Schritte bestimmen. BeratungsHiG § 2 Beratungsberechtigung, BRAO § 43a Interessenkonflikte, niedrigschwellige Erstberatung. Prüfraster Sachverhalt aufnehmen, Dringlichkeit und Fristen erfassen, Interessenkonflikt prüfen, Beratungsschein-Berechtigungen klaeren. Output Mandantenaufnahme-Protokoll mit Sachverhalts-Zusammenfassung und Sofortmassnahmen. Abgrenzung zu Kaltstart-Interview für Plugin-Konfiguration und zu Memo für rechtliche Analyse."
---

# /mandant-aufnahme

1. Lade `CLAUDE.md` → Fachbereiche, Intake-Vorlagen, Aufsichtsmodell, Konfliktprüfungsregeln.
2. Nutze den Ablauf unten.
3. Route zum fachbereichsspezifischen Template; achte auf fachübergreifende Probleme.
4. Konfliktprüfung, RDG-Plausibilitätsprüfung, Triage.
5. Ausgabe: formatierte Fallzusammenfassung mit KI-Label, Verifikationshinweisen, Aufsichtsrouting.

---

# Mandantenintake

## Zweck

Intake ist einer der größten Engpässe in Beratungsstellen. Eine Studierende könnte 45 Minuten im Gespräch verbringen, eine weitere Stunde mit dem Protokoll, noch mehr Zeit mit der Problemerkennung. In dieser Zeit wächst die Warteliste.

Dieser Skill strukturiert das Gespräch, erstellt das Protokoll, erkennt fachübergreifende Fragen und prüft Interessenkonflikte – damit die Zeit der Studierenden der juristischen Analyse gilt, nicht dem Abtippen.

**Was dieser Skill nicht tut:** entscheiden, ob das Mandat angenommen wird. Das ist Sache der Analyse der Studierenden und der Entscheidung des Anleiters.

## RDG-Besonderheiten beim Intake

- § 6 Abs. 2 Nr. 2 RDG: Das Intake-Gespräch ist eine Rechtsdienstleistung – es darf nur unentgeltlich und unter Anleitungsstruktur stattfinden.
- § 43a Abs. 4 BRAO / BORA § 3: **Vor jedem Intake Interessenkonflikt prüfen.** Hat die Beratungsstelle oder der Anleiter bereits die Gegenseite vertreten?
- § 203 StGB: Alles, was im Intake erfährt wird, ist Mandantengeheimnis – ab dem ersten Wort des Gesprächs.
- DSGVO Art. 13: Der Mandant ist zu Beginn über die Verarbeitung seiner Daten zu informieren (Name, Zweck, Speicherdauer, Rechte).

## Interessenkonflikt-Check (zwingend vor jedem Intake)

Bevor das Gespräch beginnt:
1. Name des Mandanten und aller beteiligten Parteien (Vermieter, Jobcenter-Sachbearbeiter o. Ä.) erfassen.
2. Gegen bestehende Mandate und Mandantenregister abgleichen.
3. Wenn Konflikt erkannt: Intake sofort stoppen; Mandant höflich über Hindernis informieren; keine Rechtsauskünfte mehr erteilen; an alternative Beratungsstelle verweisen.

> Prüffrage: "Hat unsere Beratungsstelle oder unser Anleiter je die Gegenseite dieses Verfahrens beraten?" – wenn ja: Konflikt.

## Datenschutz-Hinweis zu Beginn (Pflicht)

Vor Beginn des Gesprächs vorlesen oder übersetzen (ggf. mit Dolmetscher):

> "Wir sind eine studentische Rechtsberatungsstelle. Ihre Daten werden nur für Ihre Beratung genutzt und nach Abschluss des Mandats mindestens 5 Jahre aufbewahrt (§ 50 BRAO). Sie können jederzeit Auskunft, Berichtigung oder Löschung verlangen (DSGVO Art. 15–17). Ihre Angaben sind vertraulich (§ 203 StGB)."

## Fachbereichsspezifisches Intake

### Asyl / Aufenthaltsrecht
- **Personalien:** Vollständiger Name (mit Schreibweise lt. Reisepass/Ausweis), Geburtsdatum, Staatsangehörigkeit.
- **Status:** Aktueller aufenthaltsrechtlicher Status (Asylantragsteller, GFK-Schutz, subsidiärer Schutz, Duldung, humanitärer Aufenthaltstitel § 25 AufenthG)?
- **Verfahrensstand:** BAMF-Bescheid erhalten? Datum der Zustellung? → **Fristencheck sofort!** Bei § 36-Bescheid: Klage binnen 1 Woche (§ 74 Abs. 1 i. V. m. § 36 AsylG)!
- **Einreise:** Datum und Einreiseweg (relevant für Dublin III, Jahresfrist § 74 AsylG).
- **Vorverfahren:** Frühere Asylanträge, Abschiebungen, EURODAC-Treffer?
- **Vulnerabilität:** Minderjährigkeit (§ 12 AsylG: Bestellung Vormund), Schwangerschaft, Trauma, Behinderung (→ § 76b SGB IX prüfen).
- **Familie:** Familienangehörige, deren Status, Familiennachzug?
- **Strafrecht:** Vorstrafen (§ 3 Abs. 2 AsylG Ausschluss, § 25 Abs. 3 AufenthG Sperrung)?
- **Sprache:** Welche Sprachen spricht der Mandant? Dolmetscher notwendig?
- **Dringlichkeit:** Abschiebung angekündigt? Ankündigungsschreiben der Ausländerbehörde?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### SGB II / Bürgergeld
- **Bescheid:** Art des Bescheids (Bewilligung, Änderung, Ablehnung, Sanktion) und Datum der Bekanntgabe → **Widerspruchsfrist: 1 Monat ab Bekanntgabe (§ 84 SGG)**.
- **Leistungen:** Aktuell bewilligte Bedarfe (Regelbedarf, Unterkunft § 22 SGB II, Mehrbedarfe §§ 20 ff. SGB II)?
- **Anlass:** Sanktion (§ 31 SGB II – Pflichtverletzung, Höhe, Dauer)? Einkommensanrechnung (§§ 11–11b SGB II)? Unterkunftskosten unangemessen (§ 22 SGB II)?
- **Haushaltsgemeinschaft:** Wer lebt im Haushalt?
- **Einkommen und Vermögen:** Erwerbseinkommen, Kindergeld, Unterhalt; Vermögen (Schonvermögen § 12 SGB II beachten).
- **Vorherige Rechtsmittel:** Frühere Widersprüche oder Klagen?
- **Dringlichkeit:** Droht Obdachlosigkeit? Einstweiliger Rechtsschutz (§ 86b SGG) nötig?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Mietrecht
- **Mietverhältnis:** Privat, sozial gefördert (WoBindG), Genossenschaft?
- **Anlassfall:** Kündigung (fristlos § 543 BGB, ordentlich § 573 BGB), Mieterhöhung (§§ 558 ff. BGB), Mängel (§ 536 BGB Minderung), Kaution (§ 551 BGB), Modernisierung (§§ 559 ff. BGB)?
- **Dokumente:** Mietvertrag, Kündigungsschreiben, Mieterhöhungsverlangen, Mietspiegel vorhanden?
- **Fristen:** Datum des Kündigungsschreibens / Mieterhöhungsverlangens? Gerichtstermin?
- **Mietspiegel:** Liegt ein qualifizierter Mietspiegel i. S. v. § 558d BGB vor? (Berlin: Berliner Mietspiegel 2023/2024)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Sozialklausel:** § 574 BGB – Widerspruch des Mieters gegen Kündigung? Härtegründe?
- **Dringlichkeit:** Räumungsklage anhängig? Vollstreckungsankündigung?

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

### Verbraucherrecht
- **Vertragsart:** Fernabsatz (§§ 312 ff. BGB), Energielieferung, Mobilfunk, Versicherung, Finanzierung?
- **Problem:** Widerrufsrecht abgelaufen? AGB-Klausel unwirksam (§§ 305–310 BGB)? Schuldnerberatung (kein RDG – an anerkannte Schuldnerberatung verweisen)?
- **Fristen:** Widerrufsfrist 14 Tage (§ 355 BGB); bei fehlender Belehrung: 12 Monate + 14 Tage.

### Familienrecht / SGB IX
- **Thema:** Unterhalt (§§ 1601 ff. BGB), Sorgerecht (§§ 1626 ff. BGB), Trennungsunterhalt (§ 1361 BGB), Gewalt (Gewaltschutzgesetz §§ 1–2 GewSchG)?
- **Kinder:** Minderjährige Kinder, Umgangsregelung, Kindeswohlgefährdung (§ 8a SGB VIII – Meldepflichten prüfen)?
- **SGB IX:** Eingliederungshilfe nach § 76b SGB IX (bes. für Geflüchtete mit Behinderung)?

## Triage-Klassifikation

| Klasse | Kriterium | Empfehlung |
|---|---|---|
| **Dringend** | Frist in ≤ 14 Tagen; drohende Abschiebung; Räumungsklage | Sofortige Rücksprache mit Anleiter; ggf. einstweiliger Rechtsschutz |
| **Regulär** | Frist > 14 Tage; Beratungsmandat ohne unmittelbaren Handlungsdruck | Normaler Ablauf |
| **Weitervermittlung** | Außerhalb RDG-Erlaubnis; Interessenkonflikt; zu komplex für Beratungsstelle | Verweis auf RAK-Vermittlung, Pro Bono Berlin/Bremen, VB-Zentrale |
| **Schuldnerberatung** | Überschuldung als Hauptthema | An anerkannte Schuldnerberatungsstelle (§ 305 Abs. 1 Nr. 1 InsO) verweisen |

## Ausgabeformat

Strukturiertes Fallprotokoll:

```
[KI-GESTÜTZTER ENTWURF – Analyse durch Studierenden und Freigabe durch
anleitenden Volljuristen erforderlich. Kein Versand ohne Prüfung.]

## Fallprotokoll [Datum]

**Mandantenkennung:** [anonymisiert – z. B. M-2024-17]
**Fachbereich:** [Asylrecht | SGB II | Mietrecht | ...]
**Dringlichkeitsklasse:** [Dringend | Regulär | Weitervermittlung]
**Bearbeitende/r:** [Kürzel]

### Sachverhalt
[Knapper Fließtext, sachlich, keine Wertung]

### Rechtliche Fragestellungen (vorläufig)
1. ...
2. ...

### Konfliktprüfung
☑ Keine Interessenkonflikte festgestellt / ☐ Konflikt: [Beschreibung]

### Relevante Fristen
| Frist | Datum | Norm |
|---|---|---|
| ... | TT.MM.JJJJ | § ... |

### Empfohlene nächste Schritte (Entwurf)
1. ...

### Anleiterhinweis
[Punkte, die zwingend mit dem Anleiter besprochen werden müssen]
```

## Risiken / typische Fehler

- **Fristvergessenheit:** Datum der Zustellung sofort prüfen – nicht erst beim nächsten Termin. Bei § 36-Bescheid AsylG 1 Woche, bei § 74 AsylG sonst 2 Wochen oder 1 Monat – immer konkret berechnen.
- **Fehlende Konfliktprüfung:** Ohne Check kann § 43a Abs. 4 BRAO verletzt sein. Dann keine weiteren Informationen mehr entgegennehmen.
- **Sprachbarriere nicht dokumentiert:** Wenn der Mandant die Erläuterungen nicht verstanden hat, ist die Aufklärungspflicht nicht erfüllt.
- **Falsche Rechtsbereichszuordnung:** Asylmandat schlägt fast immer auf SGB II durch (§ 7 Abs. 1 Satz 2 SGB II: Leistungsausschluss für bestimmte Ausländer – prüfen!).
- **Entgeltlichkeit:** Kein Entgelt entgegennehmen – auch kein "freiwilliges Geschenk". Verletzt § 6 Abs. 2 Nr. 2 RDG (Unentgeltlichkeitspflicht) und ist bußgeldbewehrt (§ 20 RDG).
