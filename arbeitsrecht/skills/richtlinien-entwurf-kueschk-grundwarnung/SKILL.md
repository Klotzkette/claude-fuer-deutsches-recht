---
name: richtlinien-entwurf-kueschk-grundwarnung
description: "Richtlinien Entwurf Kueschk Grundwarnung im Plugin Arbeitsrecht: prüft konkret Entwirft eine betriebliche Regelung (Richtlinie, Betriebsordnung, Policy) mit st, Pflichtkopf für jeden Kündigungsschutzklage-Schriftsatz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Richtlinien Entwurf Kueschk Grundwarnung

## Arbeitsbereich

**Richtlinien Entwurf Kueschk Grundwarnung** ordnet den Fall über die tragenden Prüfungslinien: Entwirft eine betriebliche Regelung (Richtlinie, Betriebsordnung, Policy) mit st. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `richtlinien-entwurf` | Entwirft eine betriebliche Regelung (Richtlinie, Betriebsordnung, Policy) mit standortspezifischen Ergänzungen, wo das Recht oder Tarifverträge abweichende Regeln erfordern. Prüft Mitbestimmungsrechte des Betriebsrats und ob bestehende Leistungsversprechen berührt werden. Lädt, wenn jemand sagt "Richtlinie entwerfen zu [Thema]", "wir brauchen eine Regelung zu" oder eine Regelungslücke benennt. |
| `kueschk-grundwarnung-falsche-wiese-und-haftung` | Pflichtkopf für jeden Kündigungsschutzklage-Schriftsatz: Hinweis auf falsche Wiese und Haftungsausschluss; zentraler Warnblock mit Drei-Wochen-Frist nach § 4 KSchG; wird in jeden Laien-Output eingefuegt. |
| `internationale-expansion` | Referenz-Skill: Implementierungsplanungs-Framework für internationale Einstellungen — Entscheidungsrahmen AÜG-Modell/EOR vs. eigene Gesellschaft, abteilungsübergreifende Trigger für Steuer/Finance/HR, strukturierter Briefing-Request an externe Arbeitsrechtler und persistenter Lücken-Tracker. Wird von /expansion-auftakt und /expansion-aktualisierung geladen; nicht direkt aufzurufen. |
| `kueschk-abfindung-faustformel-und-spannweite` | Abfindung Kündigungsschutzklage: Faustformel halbes Bruttomonatsgehalt pro Beschaeftigungsjahr; Spannweite von einem Viertel bis zu einem ganzen Bruttomonatsgehalt; Einflussfaktoren; steuerliche Behandlung Fuenftel-Regelung § 34 EStG; keine gesetzliche Abfindungspflicht außer §§ 1a und 9 KSchG. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `richtlinien-entwurf`

**Fokus:** Entwirft eine betriebliche Regelung (Richtlinie, Betriebsordnung, Policy) mit standortspezifischen Ergänzungen, wo das Recht oder Tarifverträge abweichende Regeln erfordern. Prüft Mitbestimmungsrechte des Betriebsrats und ob bestehende Leistungsversprechen berührt werden. Lädt, wenn jemand sagt "Richtlinie entwerfen zu [Thema]", "wir brauchen eine Regelung zu" oder eine Regelungslücke benennt.

### Richtlinien-Entwurf (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Richtlinien-Entwurf (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Eine Regelung, die für München passt, kann in Frankfurt falsch sein — nicht
wegen des Landes, sondern wegen des Tarifvertrags, der Betriebsvereinbarung
oder der Konzernstruktur. Diese Skill entwirft eine Kernregelung und erstellt
standortspezifische Ergänzungen, wo der Betrieb, ein Tarifvertrag oder eine
bestehende Betriebsvereinbarung abweichende Anforderungen stellt.

Lädt, wenn eine neue oder geänderte Arbeitsregelung für ein oder mehrere
Unternehmen / Standorte benötigt wird und die Folgewirkungen auf Betriebsrat,
Tarifvertrag und bestehende Zusagen geprüft werden sollen.

## Eingaben

- Thema der Regelung (z. B. Mobile Arbeit, Elternzeit-Ergänzung, Spesen,
 Social Media, Datenschutz am Arbeitsplatz)
- Anlass (gesetzliche Anforderung, Unternehmensinitiative, Regelungslücke)
- Geltungsbereich (alle Arbeitnehmer / bestimmte Rollen / bestimmte Standorte)
- Bestehende Betriebsvereinbarungen und Tarifbindung (falls bekannt)
- Jurisdiktioneller Fußabdruck (Standorte und Länder)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 87 BetrVG: Erzwingbares Mitbestimmungsrecht des Betriebsrats —
 Regelungen in den Bereichen § 87 Abs. 1 Nr. 1–13 (u. a. Ordnung des
 Betriebs, Arbeitszeit, Urlaub, Datenschutz, Vergütungsgrundsätze)
 können nicht ohne Zustimmung des Betriebsrats eingeführt werden
- § 77 BetrVG: Betriebsvereinbarungen — Vorrang und Ablöseprinzip;
 Nachwirkung (§ 77 Abs. 6 BetrVG); günstigerer Tarifvertrag geht vor
- §§ 305 ff. BGB: AGB-Kontrolle für vorformulierte Arbeitsbedingungen;
 § 305c Abs. 1 BGB: Verbot überraschender Klauseln; § 307 BGB:
 Inhaltskontrolle; Transparenzgebot
- § 2 NachwG: Schriftliche Mitteilung wesentlicher Arbeitsbedingungen
 bei erstmaliger Vereinbarung und bei Änderungen
- §§ 3 ff. AGG: Diskriminierungsverbote — Regelungen dürfen keine
 unmittelbaren oder mittelbaren Benachteiligungen wegen geschützter
 Merkmale enthalten oder bewirken
- ArbZG: Arbeitszeitgesetz — Regelungen zur Arbeitszeit dürfen
 gesetzliche Höchstgrenzen (§ 3 ArbZG: 8 Stunden täglich, maximal
 10 Stunden) und Ruhezeiten (§ 5 ArbZG) nicht unterschreiten
- § 26 BDSG / Art. 88 DSGVO: Beschäftigtendatenschutz — Regelungen zur
 Überwachung, Zugriffsrechten oder Kommunikation erfordern
 Datenschutzprüfung und ggf. Betriebsvereinbarung nach § 26 BDSG

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Betriebliche Übung als Anspruchsgrundlage; einseitige Verschlechterung
 einer durch betriebliche Übung entstandenen Leistungspflicht unwirksam;
 Änderungskündigung als erforderliches Instrument
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Mitbestimmungspflicht bei einseitiger Änderung betrieblicher Regelungen
 in § 87 BetrVG-Bereichen; Einigungsstellenverfahren bei Scheitern der
 Einigung

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Katalog der erzwingbaren Mitbestimmungsrechte; Reichweite bei einzelnen
 Themenfeldern (Homeoffice, Datenschutz, Zeiterfassung)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 AGB-Kontrolle vorformulierter Arbeitsbedingungen; Inhaltskontrolle;
 Transparenzgebot im Arbeitsrecht
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Nachweispflicht; schriftliche Mitteilung bei Änderungen; Folgen

## Ablauf

**Schritt 1 — Kontext laden**

Lese `CLAUDE.md` im Plugin-Verzeichnis → jurisdiktioneller Fußabdruck,
Handbuch-Standort, Tarifbindungen, bestehende Betriebsvereinbarungen.

**Schritt 2 — Regelung scopen**

- Welches Thema? (Mobile Arbeit, Elternzeit, Social Media, Spesen, etc.)
- Warum jetzt? (Gesetzliche Anforderung, Unternehmensinitiative, Regelungslücke)
- Für wen gilt sie? (Alle Arbeitnehmer, bestimmte Rollen, bestimmte Standorte)

**Schritt 3 — Mitbestimmungsprüfung**

Prüfe, ob die geplante Regelung in einen Mitbestimmungstatbestand des
§ 87 Abs. 1 BetrVG fällt:

| Regelungsthema | Mitbestimmungstatbestand |
|---|---|
| Ordnung des Betriebs, Verhaltensregeln | § 87 Abs. 1 Nr. 1 BetrVG |
| Beginn/Ende der täglichen Arbeitszeit, Pausen | § 87 Abs. 1 Nr. 2, 3 BetrVG |
| Urlaubsplanung, -grundsätze | § 87 Abs. 1 Nr. 5 BetrVG |
| Einführung von Überwachungstechnik (IT, Zeiterfassung) | § 87 Abs. 1 Nr. 6 BetrVG |
| Unfallverhütung, Gesundheitsschutz | § 87 Abs. 1 Nr. 7 BetrVG |
| Grundsätze des betrieblichen Lohngestaltung | § 87 Abs. 1 Nr. 10 BetrVG |
| Mobile Arbeit / Homeoffice | § 87 Abs. 1 Nr. 1, 2, 6 BetrVG |

Falls Mitbestimmung ausgelöst: explizit flaggen und empfohlenes Vorgehen
angeben (Einholung Betriebsratszustimmung oder Einigungsstellenverfahren
nach § 76 BetrVG).

**Schritt 4 — Jurisdiktioneller Scan**

Für jeden Standort / jede tarifvertragliche Bindung im Fußabdruck prüfen:
Gibt es abweichende gesetzliche, tarifvertragliche oder
betriebsvereinbarungsbasierte Anforderungen zu diesem Thema?

**Häufige Themen mit Varianz:**

| Thema | Varianzquelle |
|---|---|
| Arbeitszeitregelungen | ArbZG-Mindestanforderungen; Branchentarifverträge (z. B. BAP/iGZ für Zeitarbeit) |
| Urlaubsansprüche | Tarifvertragliche Mehrurlaubs-Ansprüche; BUrlG-Mindest |
| Mobiles Arbeiten | Betriebsvereinbarungen; § 87 Abs. 1 Nr. 1, 2, 6 BetrVG |
| Überstundenregelungen | ArbZG-Grenzen; TV-Mehrarbeitszuschläge |
| Datenschutz am Arbeitsplatz | § 26 BDSG; Betriebsvereinbarung als Rechtsgrundlage |
| Außertarifliche Zulagen | Gleichbehandlungsgrundsatz; AGG |
| Kündigung / Abfindung | KSchG; TV-Abfindungsregelungen |

Falls das Thema keine standortspezifische Varianz aufweist (z. B. reines
Verhaltensgebot ohne Vergütungsrelevanz): diesen Schritt überspringen.

**Schritt 5 — Kernregelung entwerfen**

Eine Regelung. Gilt für alle erfassten Arbeitnehmer. Klar und verständlich —
Arbeitnehmer sollen sie ohne juristische Vorkenntnisse verstehen.

Struktur:
- Zweck (ein Satz — warum diese Regelung besteht)
- Geltungsbereich (wer ist erfasst)
- Die Regel (was ist geboten / erlaubt / untersagt)
- Verfahren (wie beantragen, wer genehmigt, was passiert bei Verstoß)
- Ansprechpartner (an wen wenden bei Fragen)

Vermeiden: "unbeschadet", "vorbehaltlich", verschachtelte Ausnahmen.
Das ist eine Betriebsregelung, kein Vertrag.

**Datenschutzprüfung:** Falls die Regelung die Verarbeitung von
Beschäftigtendaten vorsieht oder ermöglicht (z. B. IT-Monitoring,
Zeiterfassung, Zugangskontrolle): Rechtsgrundlage nach § 26 BDSG und
ggf. DSFA nach Art. 35 DSGVO prüfen. Bei automatisierter Überwachung
ist eine Betriebsvereinbarung als Rechtsgrundlage nach § 26 Abs. 4 BDSG
der sichere Weg.

**Schritt 6 — Standortspezifische Ergänzungen**

Für jeden Standort, an dem die Regel abweicht:

```markdown
### [Standort]-Ergänzung

Für Arbeitnehmer am Standort [Standort] gilt abweichend bzw. ergänzend:

- [Spezifische Abweichung]
- [Rechtsgrundlage oder Tarifvertragsbezug]
```

Ergänzungen knapp halten — nur Abweichendes; Kernregelung nicht wiederholen.

**Schritt 7 — Quercheck**

- Kollidiert diese Regelung mit einer bestehenden Regelung im Handbuch?
- Verspricht sie mehr, als das Unternehmen liefern will? (Eine Regelung ist
 ein Versprechen — Gerichte halten Arbeitgeber an Handbuchzusagen.)
- Enthält sie unabsichtlich eine vertragliche Bindung? (Betriebliche Übung
 nach drei gleichförmigen Wiederholungen — Disclaimer-Klausel wenn nötig,
 aber als eigenständigen Abschnitt, nicht als Fußnote.)
- AGG-Konformität: Enthält die Regelung mittelbare Benachteiligungen wegen
 geschützter Merkmale nach § 1 AGG?

## Ausgabeformat

```markdown
### [Regelungsname]

## Kernregelung

**Geltung:** [alle Arbeitnehmer / bestimmte Gruppen / Standorte]

**Zweck**
[Ein Satz]

**Geltungsbereich**
[Wer ist erfasst]

**Die Regelung**
[Was ist geboten / erlaubt / untersagt]

**Verfahren**
[Wie beantragen, Genehmigung, Konsequenzen bei Verstoß]

**Ansprechpartner**
[HR-Kontakt / Vorgesetzte]

---

## Standortspezifische Ergänzungen

### [Standort 1]
[Ergänzung]

### [Standort 2]
[Ergänzung]

---

## Entwurfsnotizen (intern — vor Einpflegen ins Handbuch entfernen)

- **Mitbestimmung:** [Tatbestand § 87 BetrVG — betroffene Nr. / nicht betroffen]
- **Betriebsrat-Vorgehen:** [Zustimmung erforderlich / Einigungsstellenverfahren]
- **Datenschutz:** [§ 26 BDSG-Prüfung, DSFA erforderlich ja/nein]
- **Jurisdiktioneller Scan:** [welche Standorte geprüft, wo Varianz]
- **Kollisionen mit bestehendem Handbuch:** [keine | Liste]
- **Recht derzeit im Wandel:** [Themen, die in Bewegung sind]
- **Review-Turnus:** [jährlich / bei Änderung von Gesetz/TV]
```

## Beispiel

Szenario: Entwurf einer Mobile-Work-Regelung für ein Unternehmen mit
Standorten in Hamburg und München, Tarifbindung nach TV Gesamtmetall.

Ausgabe (Auszug Entwurfsnotizen):

> Mitbestimmung: Mobile-Arbeit-Regelung berührt § 87 Abs. 1 Nr. 1 BetrVG
> (Ordnung des Betriebs), Nr. 2 BetrVG (Beginn/Ende der Arbeitszeit) und
> Nr. 6 BetrVG (IT-Überwachung bei Homeoffice-Zeiterfassung).
> Betriebsrat-Zustimmung oder Abschluss einer Betriebsvereinbarung ist
> vor Einführung zwingend.
>
> TV Gesamtmetall: Prüfen, ob der einschlägige ERA-TV Regelungen zur
> mobilen Arbeit enthält, die von der Kernregelung abweichen.
>
> Datenschutz: Falls die Regelung IT-Monitoring im Homeoffice vorsieht
> (z. B. Aktivitätstracking), ist eine Betriebsvereinbarung als
> Rechtsgrundlage nach § 26 Abs. 4 BDSG erforderlich und eine DSFA
> nach Art. 35 DSGVO zu prüfen.

## Risiken und typische Fehler

- **Mitbestimmung übergangen**: Eine in § 87 BetrVG-Bereichen eingeführte
 Regelung ohne Betriebsratszustimmung ist unwirksam, auch wenn der Inhalt
 sachlich gerechtfertigt ist.
- **Betriebliche Übung**: Was dreimal gleichförmig gewährt wurde, kann
 bindend werden. Neuregelungen, die bisher praxisübliche Leistungen
 einschränken, brauchen entweder individuelle Zustimmung oder
 Änderungskündigung.
- **AGB-Falle**: Vorformulierte Arbeitsbedingungen unterliegen § 307 BGB.
 Überraschende oder unverhältnismäßig belastende Klauseln sind unwirksam.
- **NachwG versäumt**: Wenn die Regelung wesentliche Arbeitsbedingungen
 ändert, ist schriftliche Mitteilung an die betroffenen Arbeitnehmer
 nach § 2 NachwG erforderlich.
- **AGG-Konformität nicht geprüft**: Regelungen können mittelbar
 diskriminierend wirken (z. B. Teilzeitausschlüsse, die überwiegend
 Frauen treffen). § 3 Abs. 2 AGG beachten.
- **Datenschutz nicht eingeplant**: Technische Überwachungsmaßnahmen
 ohne Betriebsvereinbarung und DSFA können nach § 26 BDSG und
 § 87 Abs. 1 Nr. 6 BetrVG unzulässig sein.

## Quellenpflicht

Jede Ausgabe dieser Skill zitiert je nach Relevanz:

- § 87 BetrVG (Mitbestimmung), § 77 BetrVG (Betriebsvereinbarung)
- §§ 305 ff. BGB (AGB-Kontrolle), § 307 BGB (Inhaltskontrolle)
- § 2 NachwG (Nachweispflicht)
- § 26 BDSG, Art. 88 DSGVO (Beschäftigtendatenschutz)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen Überwachungseinrichtungen; Rechtsprechung nur frei verifiziert zitieren.

> **Entwurf, keine geltende Regelung.** Dieser Entwurf ist ein Arbeitsdokument
> für die anwaltliche Überprüfung. Eine Betriebsregelung oder Richtlinie, die
> tatsächlich gilt, hat arbeitsrechtliche Bindungswirkung — in bestimmten
> Bereichen als vertragliche Vereinbarung, durch betriebliche Übung oder
> als Betriebsvereinbarung. Ein in der jeweiligen Jurisdiktion zugelassener
> Rechtsanwalt oder Syndikusrechtsanwalt (§ 46 BRAO) prüft, überarbeitet
> und trägt die fachliche Verantwortung, bevor die Regelung in Kraft tritt.
> Nicht ohne Freigabe verteilen oder einführen.

## Übergabe an handbuch-aktualisierung

Wenn diese Regelung genehmigt ist: `handbuch-aktualisierung`-Skill prüft die
Auswirkung auf das bestehende Handbuch und benennt Querverweise und
Anpassungsbedarf.

## Was diese Skill nicht tut

- Regelungen genehmigen — das ist Aufgabe von HR-Leitung und Rechtsabteilung.
- Regelungen kommunizieren — Mitarbeiterinformation ist HR-Aufgabe.
- Alle denkbaren Jurisdiktionen abdecken — nur den konfigurierten Fußabdruck.
 Bei Erweiterung des Fußabdrucks neu prüfen.

## Ergänzende Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Halluzinations-Reparatur Bundle 014:
-->

## 2. `kueschk-grundwarnung-falsche-wiese-und-haftung`

**Fokus:** Pflichtkopf für jeden Kündigungsschutzklage-Schriftsatz: Hinweis auf falsche Wiese und Haftungsausschluss; zentraler Warnblock mit Drei-Wochen-Frist nach § 4 KSchG; wird in jeden Laien-Output eingefuegt.

### Grundwarnung: Falsche Wiese und Haftung

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundwarnung: Falsche Wiese und Haftung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill liefert den Pflicht-Warnkopf, der jedem Schriftsatz und jeder inhaltlichen Ausgabe vorangestellt wird, die im Rahmen des KüSchK-Laien-Workflows erzeugt wird. Er ist kein eigenständiger Workflow, sondern ein einzufügender Baustein.

## Pflicht-Disclaimer-Kopf (in jeden Laien-Output einfügen)

---

**HAFTUNGSAUSSCHLUSS UND WARNUNG**

Dieses Dokument wurde mit Hilfe eines KI-gestützten Systems erstellt. Es handelt sich um einen **Entwurf zur eigenständigen Verwendung auf eigenes Risiko**. Das System übernimmt keine rechtliche Verantwortung.

**Du könntest auf der falschen Wiese unterwegs sein.**

Das bedeutet: Möglicherweise ist das Kündigungsschutzgesetz (KSchG) auf deinen Fall gar nicht anwendbar — weil dein Betrieb zu klein ist (§ 23 KSchG: weniger als zehn Arbeitnehmer) oder weil du noch keine sechs Monate beschäftigt bist (§ 1 Abs. 1 KSchG). In diesem Fall wäre eine Kündigungsschutzklage nach § 4 KSchG nicht das richtige Rechtsmittel. Das System kann das nicht selbst feststellen.

**Drei-Wochen-Frist — absolute Ausschlussfrist:**

> § 4 KSchG: Will ein Arbeitnehmer geltend machen, dass eine Kündigung sozial ungerechtfertigt oder aus anderen Gründen rechtsunwirksam ist, so muss er innerhalb von **drei Wochen nach Zugang der schriftlichen Kündigung** Klage beim Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis durch die Kündigung nicht aufgelöst ist.

Die Frist beginnt mit dem Tag des **Zugangs** der Kündigung (nicht dem Datum auf dem Schreiben). Sie kann grundsätzlich nicht verlängert werden. Ein Versäumnis führt nach § 7 KSchG dazu, dass die Kündigung als wirksam gilt — auch wenn sie rechtswidrig war.

**Ausnahme:** Nachträgliche Klagezulassung nach § 5 KSchG bei unverschuldeter Versäumung (z.B. schwere Erkrankung, Abwesenheit ohne Verschulden). Die Frist für den Zulassungsantrag beträgt zwei Wochen nach Wegfall des Hindernisses.

---

## Triage zu Beginn — kläre vor Einbettung des Warnbausteins

1. Handelt es sich um einen Laien-Output (nicht anwaltlicher Nutzer)?
2. Wurde der KSchG-Anwendbarkeitscheck bereits durchgeführt (`kueschk-anwendbarkeit-kschg-pruefen`)?
3. Ist die Drei-Wochen-Frist bereits einkalkuliert (Zugangsdatum bekannt)?

Nur wenn Frage 1 = ja: Warnbaustein zwingend einbetten. Bei Anwält:innen entfällt der Pflicht-Disclaimer-Kopf.

## Zentrale Normen

- **§ 4 KSchG** — Klagefrist drei Wochen ab Zugang der schriftlichen Kündigung
- **§ 5 KSchG** — Nachträgliche Zulassung der Klage bei unverschuldeter Fristversäumung (Antragsfrist: zwei Wochen nach Wegfall des Hindernisses)
- **§ 7 KSchG** — Fiktion der Wirksamkeit bei Fristversäumung
- **§ 23 KSchG** — Betrieblicher Geltungsbereich KSchG (Schwellenwert > 10 Arbeitnehmer)
- **§ 1 Abs. 1 KSchG** — Wartezeit sechs Monate
- **§ 11 Abs. 1 ArbGG** — Kein Anwaltszwang erste Instanz

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wo dieser Baustein erscheint

- Vor jedem Klageschrift-Entwurf (Skill `kueschk-klageschrift-laie-baustein`)
- Vor jedem Schriftsatz-Entwurf für Laien
- In der Ausgabe von `kueschk-output-warnschriftsatz-laie`

## Mechanik des Warnbausteins

Der Warnblock ist kein optionaler Hinweis, sondern Pflichtbestandteil. Er darf weder weggelassen noch verkürzt werden. Anwältinnen und Anwälte erhalten diesen Kopf nicht — für sie gilt der Hinweis in `kueschk-triage-laie-oder-anwalt`.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 3. `internationale-expansion`

**Fokus:** Referenz-Skill: Implementierungsplanungs-Framework für internationale Einstellungen — Entscheidungsrahmen AÜG-Modell/EOR vs. eigene Gesellschaft, abteilungsübergreifende Trigger für Steuer/Finance/HR, strukturierter Briefing-Request an externe Arbeitsrechtler und persistenter Lücken-Tracker. Wird von /expansion-auftakt und /expansion-aktualisierung geladen; nicht direkt aufzurufen.

### Internationale Expansion — Referenz-Skill (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Internationale Expansion — Referenz-Skill (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Internationale Einstellungen werden bei wachsenden Unternehmen regelmäßig
unstrukturiert behandelt, weil niemand das Gesamtbild überblickt. Legal kennt
die arbeitsrechtlichen Fragen, aber nicht das Betriebsstättenrisiko. Finance
kennt das Kostenmodell, aber nicht die Schwellenwerte für Arbeitnehmervertretungen.
HR kennt die Gehaltsmarktdaten, aber nicht die Tag-1-Compliance-Anforderungen.

Diese Skill ersetzt keine dieser Funktionen. Sie kartiert das Terrain, formuliert
die richtigen Fragen für jeden Stakeholder, erstellt einen Briefing-Request
für externe Arbeitsrechtler im Zielland und legt einen Tracker an, der das
Projekt sitzungsübergreifend voranbringt.

Die Skill setzt voraus, dass die Expansionsentscheidung gefallen ist. Sie ist
kein Rahmen für "sollen wir expandieren?".

Diese Skill enthält kein länderspezifisches Arbeitsrecht. Die materiellen
Regelungen ändern sich häufig und variieren nach Rolle, Headcount und Branche —
jedes Zielland wird über einen Briefing-Request an externe Arbeitsrechtler geleitet,
nicht über eine interne Referenztabelle.

## Rechtlicher Rahmen

**Kernvorschriften:**

- §§ 1–19 AÜG: Arbeitnehmerüberlassungsgesetz — Erlaubnispflicht, 18-Monats-Grenze
 (§ 1 Abs. 1b AÜG), Equal-Pay (§ 8 AÜG); relevant wenn EOR als Struktur gewählt wird
- § 7 SGB IV: Beschäftigungsverhältnis; Scheinselbständigkeit — bei Freelancer- oder
 Contractor-Konstellationen zu prüfen
- § 611a BGB: Arbeitnehmerbegriff; Abgrenzung zu selbständiger Tätigkeit
- Art. 8 Rom I-VO (VO EG 593/2008): Arbeitsvertragsstatut — Rechtswahl darf nicht zum
 Entzug zwingender Schutzvorschriften des Beschäftigungsstaats führen
- Art. 45 AEUV, RL 96/71/EG (Entsenderichtlinie), RL 2018/957/EU: Arbeitnehmerfreizügigkeit,
 Entsendung innerhalb der EU
- DSGVO / § 26 BDSG: Beschäftigtendatenschutz; Datentransfer in Drittstaaten
 (Art. 44 ff. DSGVO) bei Daten über EU-Arbeitnehmer an nicht-EU-Muttergesellschaft

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Arbeitnehmerbegriff bei grenzüberschreitenden Tätigkeiten; Indizien für
 Weisungsgebundenheit — maßgeblich für Contractor- vs. Arbeitnehmerstatus
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rechtsfolgen fehlender AÜG-Erlaubnis; Fiktionswirkung nach § 10 Abs. 1 AÜG
 bei unerlaubter Arbeitnehmerüberlassung

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- AÜG: Erlaubnispflicht, Höchstüberlassungsdauer und Equal Pay nach Gesetz, Tariftext und frei verifizierter Rechtsprechung prüfen.
- Arbeitnehmerstatus: § 611a BGB, § 7a SGB IV und frei verifizierte BAG-/BSG-Rechtsprechung; keine Kommentarzitate aus Modellwissen.
- Grenzüberschreitende Arbeitsverhältnisse: Art. 8 Rom I-VO, AÜG, Entsende-/SV-Regeln und amtliche Quellen prüfen; keine Handbuchzitate aus Modellwissen.

## Ablauf

### Schritt 1 — Informationserhebung

Alle folgenden Fragen in einem einzigen Block stellen:

> Zur Erstellung des Expansionsplans werden folgende Angaben benötigt.
> Beantworte, was bekannt ist — Informationslücken sind selbst nützliche Daten:
>
> **Die Expansion**
> - Welches Land?
> - Welche Rollen werden eingestellt? (Stellenprofil ist entscheidend —
> ein Vertriebsmitarbeiter mit Abschlussvollmacht erzeugt anderes
> Betriebsstättenrisiko als eine reine Entwicklerstelle)
> - Wie viele Einstellungen im 12-Monats-Horizont?
> - Wann soll die erste Person starten?
>
> **Ausgangssituation**
> - Besteht bereits eine rechtliche Einheit im Zielland?
> - Wird ein EOR-Anbieter erwogen oder bereits genutzt?
> - Sind Steuerberatung und Finance bereits eingebunden?
> - Gibt es externe Arbeitsrechtler im Zielland?
>
> **Strategischer Kontext**
> - Langfristiger Aufbau (echtes Team aufbauen) oder Markttest
> (ein bis zwei Einstellungen, dann bewerten)?
> - Wer ist der Entscheidungsträger für die Strukturentscheidung?

Auf Antworten warten, bevor fortgefahren wird.

### Schritt 2 — Entscheidungsrahmen: AÜG-Modell/EOR vs. eigene Gesellschaft

Diese Entscheidung nicht treffen. Rahmen mit ausreichender Präzision aufstellen,
damit CFO und Steuerberater sie treffen können.

Folgende Faktoren gegen die erhobenen Angaben prüfen und ein strukturiertes
Rahmendokument erstellen:

**Grundsätzliche Abwägung:**

| Faktor | Spricht für EOR/AÜG-Modell | Spricht für eigene Gesellschaft |
|---|---|---|
| Headcount (12 Monate) | Weniger Einstellungen | Mehr Einstellungen |
| Timeline bis zur ersten Einstellung | Kurze Vorlaufzeit | Längere Vorlaufzeit möglich |
| Strategische Ausrichtung | Markttest | Langfristige Präsenz |
| Kostensensitivität | EOR-Aufschlag akzeptabel | Skalierung macht Gesellschaft effizienter |
| Kontrollbedarf | Gering — EOR übernimmt lokale HR | Hoch — direktes Arbeitgeberverhältnis gewünscht |
| IP-Sensitivität | Geringer | Höher — Gesellschaftsstruktur klarer |

Konkrete Break-even-Headcounts, EOR-Aufschläge, Gründungskosten und Timelines
variieren je Land und Anbieter — nicht hardcoden. An Steuer/Finance und EOR-Anbieter
leiten.

**AÜG-Compliance-Hinweis (bei EOR-Konstellationen zwingend prüfen):**
Wenn der EOR im Verhältnis zur deutschen Muttergesellschaft als Verleiher
fungiert, kann die AÜG-Erlaubnispflicht (§ 1 AÜG) ausgelöst werden.
18-Monats-Grenze (§ 1 Abs. 1b AÜG) und Equal-Pay-Gebot (§ 8 AÜG nach 9 Monaten)
laufen auch bei EOR-Strukturen.

**Betriebsstättenrisiko-Flag (an Steuerberatung leiten):**
Falls Rollen Vertrieb, Business Development, Account Management oder sonstige
Vertragsabschlussbefugnis umfassen — explizit flaggen:

> Betriebsstättenrisiko: [Rollentyp] kann auch ohne rechtliche Einheit im
> Zielland eine steuerliche Betriebsstätte begründen. Dies ist eine Steuerfrage,
> keine Arbeitsrechtsfrage. Steuerberatung muss vor der ersten Einstellung prüfen.

**Fragen für CFO/Steuerberatung:**

> - Bei [N] Einstellungen über 12 Monate: Ab welchem Headcount wird eine
> eigene Gesellschaft kosteneffizienter als EOR (einschließlich EOR-Aufschlag,
> Gründungskosten, laufender Compliance-Aufwand)?
> - [Falls Betriebsstättenrisiko:] Begründen diese Rollen im Zielland eine
> steuerliche Betriebsstätte? Falls ja — ändert das die Gründungs-Timeline?
> - Falls mit EOR gestartet und später Gesellschaft gegründet wird: Was sind die
> Übergangsrisiken für die bereits beim EOR beschäftigten Mitarbeiter?
> - Wer ist unser bevorzugter EOR-Anbieter für dieses Land und ist seine lokale
> Compliance-Bilanz geprüft worden?

### Schritt 3 — Abteilungsübergreifende Trigger

Für jede einzubeziehende Funktion: was ist zu tun und welche konkreten Fragen
sollte Legal stellen. Nicht nur "Finance einbinden" — die Anfrage formulieren.

**Steuerberatung** (immer vor der ersten Einstellung erforderlich)

Aufgabe: Betriebsstättenrisikoanalyse, Prüfung ob Gesellschaft steuerlich
erforderlich ist, Beratung zur Eigenkapitalvergütungsbesteuerung im Zielland.

Fragen von Legal:
- Begründet ein [Rollentyp] in [Land] eine Betriebsstätte oder steuerliche
 Nexus vor Gründung einer Gesellschaft?
- Wie lange ist das Expositionsfenster, wenn vor Klärung der Betriebsstättenfrage
 eingestellt wird?
- Wie werden unsere Beteiligungsprogramme (Optionen/Phantom Shares/RSU-Äquivalente)
 in [Land] besteuert? Brauchen Mitarbeiter lokale Steuerberatung bei Gewährung
 und Ausübung?
- Falls Gesellschaft gegründet wird: Welche Dienstleistungsvereinbarung
 (Intragroup Service Agreement) wird zwischen Tochter und Mutter benötigt?

**Finance / Lohnbuchhaltung** (vor dem ersten Gehaltslauf erforderlich)

Aufgabe: Lokalen Lohnbuchhaltungsanbieter identifizieren (oder EOR-Deckung
bestätigen), Pflichtarbeitgeberanteile budgetieren, lokales Bankkonto bei
Gesellschaftsmodell einrichten.

Fragen von Legal:
- Haben wir einen lokalen Lohnbuchhaltungsanbieter identifiziert? (Bei EOR:
 bestätigen, dass EOR Payroll inkl. lokaler Sozialabgaben übernimmt)
- Welche Pflichtarbeitgeberanteile bestehen in [Land] — Rente, Kranken-,
 Sozialversicherung — und sind diese im Vergütungsmodell budgetiert?
- Wie werden Beteiligungsprogramme für Mitarbeiter in [Land] administriert?
 Hat jemand die arbeitgeberseitigen Quellensteueranteile bei Ausübung modelliert?

**HR / Compensation & Benefits** (vor der ersten Angebotsmachung erforderlich)

Aufgabe: Benchmarking Vergütung und Benefits gegen den lokalen Markt,
Pflicht- vs. freiwillige Benefits klären.

Fragen von Legal:
- Welche Benefits sind in [Land] gesetzlich Pflicht vs. marktüblich? (Vermeiden:
 versehentlich mehr oder weniger als Marktstandard versprechen)
- Ist unser Beteiligungspaket in diesem Markt wettbewerbsfähig oder weicht
 die lokale Praxis erheblich ab?
- Wer ist die direkte Führungskraft dieser Person — lokal oder remote aus dem
 Inland? (Beeinflusst Arbeitnehmervertretungsanalyse und Arbeitsvertragsbedingungen
 in einigen Jurisdiktionen)

**Externe Arbeitsrechtler** (zwingend erforderlich — nicht überspringen)

Aufgabe: Lokales Arbeitsrechtsrahmenwerk für diese Rolle und diesen Headcount
recherchieren und beratend begleiten, lokalen Arbeitsvertrag prüfen/entwerfen,
strukturelle Probleme mit der geplanten Konstruktion flaggen.

Der Briefing-Request in Schritt 4 ist die Agenda für dieses Mandat.
Am Anfang vollständig übersenden — nicht scheibchenweise.

### Schritt 4 — Länderspezifischer Briefing-Request

Statt einer internen Ländertabelle erstellt diese Skill einen strukturierten
Briefing-Request an externe Arbeitsrechtler. Materielles Lokalrecht (Gesellschafts-
anforderungen, Pflichtleistungen und Beiträge, Kündigungsschutz, Kündigungsfristen,
Arbeitnehmervertretungen/Betriebsrat/Tarifbindung, Pflichtfreistellungen, Wettbewerbs-
verbote, Datenschutz, Arbeitserlaubnis) variiert nach Land, Rolle, Headcount und
Branche und ändert sich regelmäßig. Jedes Land als Verifizierungsfall behandeln —
nicht auf das eigene Wissen der Skill vertrauen.

Briefing-Request, zugeschnitten auf die erhobenen Angaben:

**Briefing-Request an externe Arbeitsrechtler — [Land]**

> Wir planen die Einstellung von [N] Mitarbeitern in [Land] ab [Datum] in
> folgenden Rollen: [Rollen]. Angestrebter Headcount über 12 Monate: [N].
> Bevorzugte Struktur (vorbehaltlich Ihrer Beratung und steuerlicher Klärung):
> [EOR / Gesellschaft / offen]. Wir bitten um ein Briefing zu folgenden Punkten.
> Bitte antworten Sie mit Quellenangaben zu primärem Recht, nicht als
> Referenztabelle — wir möchten Änderungen im Zeitverlauf verfolgen können.
>
> 1. **Einstellungsstruktur** — Welche Optionen bestehen (Direktanstellung
> über Gesellschaft, EOR, Freier Mitarbeiter) und was sind die rechtlichen
> und praktischen Abwägungen für diesen Headcount und diese Rollen?
>
> 2. **Arbeitsvertragsanforderungen** — Welche Form ist vorgeschrieben oder
> üblich? Was muss enthalten sein? Was kann nicht wirksam vereinbart werden?
> Welche Sprach- oder Übersetzungsanforderungen bestehen?
>
> 3. **Kündigung** — Welche Kündigungsfristen und Abfindungspflichten bestehen?
> Wie schwierig ist eine Kündigung in der Praxis (Kündigungsschutz,
> Sozialauswahlregeln bei Massenentlassung, Sonderkündigungsschutz)?
> Welchen Dokumentationsstandard sollten wir von Tag 1 an etablieren?
>
> 4. **Pflichtleistungen und Arbeitgeberanteile** — Was muss gesetzlich
> geleistet werden (Rente, Kranken-, Sozialversicherung, bezahlter Urlaub,
> Boni)? Welche aktuellen Arbeitgeberbeitragssätze sind zu budgetieren?
> Bitte einschlägige Gesetzesnorm angeben und Aktualität bestätigen.
>
> 5. **Wettbewerbsverbote / Geheimhaltung** — Sind nachvertragliche
> Wettbewerbsverbote durchsetzbar? Unter welchen Bedingungen und gegen
> welche Karenzentschädigung? Welche Geheimhaltungs- und
> IP-Übertragungsklauseln halten stand?
>
> 6. **Arbeitnehmervertretung** — Bestehen Betriebsrats-, Arbeitnehmervertretungs-,
> Gewerkschafts- oder Tarifbindungsanforderungen? Ab welchem Headcount
> greifen sie? Welche Anhörungs- oder Mitbestimmungsrechte bestehen?
> Sind wir durch einen Branchentarifvertrag gebunden, auch ohne Gewerkschafts-
> mitgliedschaft?
>
> 7. **Datenschutz** — Welche Pflichten bestehen für Beschäftigtendaten?
> Ist ein Datentransfermechanismus für Beschäftigtendaten in die EU oder
> ins Inland erforderlich?
>
> 8. **Arbeitserlaubnis** — Welche Aufenthaltstitel oder Visa sind für
> ausländische Staatsangehörige erforderlich? Wie sind die Bearbeitungszeiten?
>
> 9. **Branchenspezifische Regeln** — Gibt es Branchenregeln, Tarifverträge
> oder kollektive Vereinbarungen, die unabhängig von einer Gewerkschafts-
> zugehörigkeit für unsere Branche gelten?
>
> 10. **Contractor-Risiko / Scheinselbständigkeit** — Welches Prüfungsmaßstab
> gilt für die Statusfeststellung und welche Reklassifizierungsrisiken
> bestehen für etwaige Freelancer-Konstellationen?
>
> 11. **Beteiligungsvergütung** — Gibt es lokale Steuer-, Kapitalmarkt- oder
> arbeitsrechtliche Regeln für Optionen, Phantom Shares oder andere
> Beteiligungsprogramme?
>
> 12. **Tag-1-Compliance** — Was muss vor dem ersten Arbeitstag des ersten
> Mitarbeiters in Ordnung sein? Anmeldungen, Aushangpflichten, Meldungen?
>
> 13. **Die 2–3 Dinge, die ausländische Unternehmen am häufigsten überraschen** —
> Was wünschen Sie sich, hätten Mandanten früher gefragt? Was hat sich
> **jüngst geändert**, was ein Team aus dem Inland möglicherweise verpasst hat?

Diesen Briefing-Request als einzelnen offenen Punkt in den Expansions-Tracker aufnehmen:
Verantwortung = Externe Arbeitsrechtler, Status = offen, vollständige Briefing-Agenda
im Fragenfeld. Auch wenn die Jurisdiktion früher schon angefragt wurde, neuen
Briefing-Request senden — dies ist eine Aktualitätsprüfung, kein erstes Mandat.

### Schritt 5 — Expansions-Tracker anlegen

Neue Datei `expansion-[land-slug].yaml` mit allen in Schritten 2–4 identifizierten
offenen Punkten erstellen. Diese Datei persistiert sitzungsübergreifend.

Format:

```yaml
### VERTRAULICH — EXPANSIONSPLANUNG — [Datum]
land: [Ländername]
land_slug: [kleinbuchstaben-bindestrich]
kickoff_datum: [ISO-Datum]
erste_einstellung_angestrebt: [ISO-Datum oder "offen"]
headcount_12mo: [N]
rollen: [Liste]
strategische_ausrichtung: [markttest / langfristig]
eor_oder_gesellschaft: [EOR / Gesellschaft / offen]
externe_ar_beauftragt: [true / false]
betriebsstaette_geflaggt: [true / false]
zuletzt_aktualisiert: [ISO-Datum]

offene_punkte:
 - id: 1
 kategorie: [struktur / steuer / finance / hr / externe-ar / compliance]
 punkt: "[was zu tun ist]"
 verantwortung: "[Funktion oder Person]"
 status: [offen / in-bearbeitung / erledigt / blockiert]
 faellig: [ISO-Datum oder null]
 fragen:
 - "[spezifische Frage aus Schritten 2–4]"
 notizen: ""

 - id: 2
 [etc.]
```

Pro identifizierter Maßnahme aus Schritten 2–4 einen eigenen Punkt — nicht
mehrere Maßnahmen zusammenfassen; jeder Punkt soll einer einzelnen
Verantwortlichkeit zuordenbar sein.

### Schritt 6 — Ausgabe

> **Jurisdiktionshinweis.** Dieser Plan betrifft ausschließlich das in der
> Erhebung genannte Land. Lokales Arbeitsrecht, Steuerregeln, Arbeitnehmervertretungs-
> anforderungen und Datenschutzpflichten variieren erheblich nach Land, Branche und
> Headcount und ändern sich regelmäßig. Jede materielle Rechtsantwort kommt aus
> dem Briefing-Request an externe Arbeitsrechtler, nicht aus dieser Skill. Für
> ein anderes Land: neuen Briefing-Request und neuen Kickoff-Lauf durchführen.

```markdown
## Internationale Expansion: [Land] — [Datum]

Erste Einstellung angestrebt: [Datum]
Headcount (12 Monate): [N]
Rollen: [Liste]
Tracker: expansion-[slug].yaml

---

### EOR vs. Gesellschaft

[Rahmen aus Schritt 2 — Tabelle, Betriebsstättenrisiko-Flag falls zutreffend,
Fragen für CFO/Steuerberatung]

---

### Wer einzubinden ist — und was zu fragen ist

**Steuerberatung** — [N] Fragen
[Fragen aus Schritt 3]

**Finance / Lohnbuchhaltung** — [N] Fragen
[Fragen aus Schritt 3]

**HR / Compensation & Benefits** — [N] Fragen
[Fragen aus Schritt 3]

**Externe Arbeitsrechtler** — siehe Briefing-Request
[Vollständiger Briefing-Request aus Schritt 4]

---

### Offene Punkte ([N] gesamt)

| # | Punkt | Verantwortung | Status |
|---|---|---|---|
| 1 | [Punkt] | [Funktion] | Offen |

---

`/arbeitsrecht:expansion-aktualisierung [Land]` ausführen, wenn Punkte geschlossen werden.
```

## Was diese Skill nicht tut

- Länderspezifisches Arbeitsrecht inhaltlich beantworten — das ist Aufgabe
 der externen Arbeitsrechtler.
- Die EOR-vs.-Gesellschaft-Entscheidung treffen — sie rahmt sie für die
 richtigen Entscheidungsträger.
- Den lokalen Arbeitsvertrag entwerfen — das muss außen Counsel erledigen.
- Länderspezifische Regeln aus eigenem Wissen wiedergeben — jedes Land wird
 durch den Briefing-Request verifiziert.
- Externes Arbeitsrechtsmandat ersetzen — jedes neue Land erfordert lokalen
 Rechtsbeistand, keine Ausnahme.

## Quellenpflicht

Jede Ausgabe zu AÜG-Konstellationen zitiert:
- §§ 1, 8, 10 AÜG, § 7 SGB IV, Art. 8 Rom I-VO
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- AÜG: Erlaubnispflicht, Höchstüberlassungsdauer und Equal Pay nach Gesetz, Tariftext und frei verifizierter Rechtsprechung prüfen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

<!-- AUDIT 27.05.2026 | Bundle 012 | Task 5
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund WRONG_TOPIC + falsches Datum + falsche Zeitschrift → Eintrag gelöscht.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Statusfeststellungsverfahren nach § 7a SGB IV; Gesamtbetrachtung aller Beschäftigungsmerkmale"
Tatsächliche Entscheidung (dejure.org):
 Datum: 29.06.2021 (nicht 29.03.2022)
 Thema: Krankenversicherung — Familienversicherung — Gesamteinkommen (§ 10 SGB V)
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Kein Bezug zu § 7a SGB IV / Statusfeststellung.
Eintrag vollständig entfernt; bei Bedarf passendes Statusfeststellungs-AZ recherchieren.
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=29.06.2021&Aktenzeichen=B+12+KR+2%2F20+R
-->

## 4. `kueschk-abfindung-faustformel-und-spannweite`

**Fokus:** Abfindung Kündigungsschutzklage: Faustformel halbes Bruttomonatsgehalt pro Beschaeftigungsjahr; Spannweite von einem Viertel bis zu einem ganzen Bruttomonatsgehalt; Einflussfaktoren; steuerliche Behandlung Fuenftel-Regelung § 34 EStG; keine gesetzliche Abfindungspflicht außer §§ 1a und 9 KSchG.

### Abfindung: Faustformel und Spannweite

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Abfindung: Faustformel und Spannweite` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre vor der Abfindungsberechnung

1. Besteht ein gesetzlicher Abfindungsanspruch? (nur § 1a KSchG bei Verzicht auf Klage; § 9 KSchG bei Auflösungsantrag — selten)
2. Wie stark ist die Rechtsposition des Arbeitnehmers? (Fehler bei BR-Anhörung / Sozialauswahl / Sonderkündigungsschutz?)
3. Wie viele volle Beschäftigungsjahre liegen vor? (Halbjahre werden aufgerundet bei § 10 Abs. 3 KSchG)
4. Wie hoch ist das monatliche Bruttogehalt? (inklusive regelmäßiger Zulagen)
5. Sperrzeit-Risiko: Auf wessen Veranlassung wird das AV beendet? (§ 159 SGB III)

## Zentrale Normen

- § 9 KSchG — Auflösungsantrag mit Abfindung (Arbeitnehmer oder Arbeitgeber; selten praktiziert)
- § 10 KSchG — Abfindungshöhe: max. 12 Monatsverdienste (18 bei > 50 Jahren + > 15 Jahren; 15 bei > 55 Jahren + > 20 Jahren)
- § 1a KSchG — Abfindungsangebot bei Verzicht auf Klage: 0.5 Monatsverdienste × Beschäftigungsjahre
- § 34 EStG — Fünftel-Regelung für außerordentliche Einkünfte (Abfindungen)
- § 158 SGB III — Ruhenszeitraum bei Abfindung und vorzeitiger Beendigung (Sperrzeit-ähnlicher Effekt)
- § 159 SGB III — Sperrzeit bei Eigenkündigung oder Aufhebungsvertrag auf eigene Veranlassung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Die Faustformel

Die in der Praxis häufig verwendete Faustformel lautet:

> **Halbes Bruttomonatsgehalt pro vollem Beschäftigungsjahr**

**Beispiel:**
- Beschäftigungszeit: 8 Jahre
- Bruttomonatsgehalt: 3500 Euro
- Faustformel-Abfindung: 8 × 0.5 × 3500 = **14000 Euro brutto**

**Was zählt als Bruttomonatsgehalt?**
Alle regelmäßigen Entgeltbestandteile: Grundgehalt + Zulagen + 1/12 Jahressonderzahlungen (soweit regelmäßig).

## Spannweite in der Praxis

Die Faustformel ist kein Gesetz — sie ist ein Verhandlungsausgangspunkt:

| Situation | Typische Spannweite pro Beschäftigungsjahr |
|---|---|
| Starke Arbeitgeberposition (KSchG kaum anwendbar) | 0.25 bis 0.5 Bruttomonatsgehälter |
| Ausgewogene Situation (Kündigung angreifbar) | 0.5 bis 0.75 Bruttomonatsgehälter |
| Starke Arbeitnehmerposition (klare Fehler, Sonderschutz) | 0.75 bis 1.0 Bruttomonatsgehälter |
| Sonderkündigungsschutz-Fälle (§ 15 KSchG, MuSchG, SGB IX) | Kann deutlich über 1.0 liegen |

**Einflussfaktoren auf die Abfindungshöhe:**
- Stärke der rechtlichen Position (je klarer die Unwirksamkeit, desto höher)
- Dauer der Betriebszugehörigkeit und Lebensalter
- Sonderkündigungsschutz
- Annahmeverzugslohn-Risiko für den Arbeitgeber (je länger Prozess, desto höher)
- Arbeitsmarktlage und Vermögenslage des Arbeitgebers

## Steuerbehandlung der Abfindung

### Einkommensteuer

Abfindungen sind grundsätzlich **steuerpflichtig** (kein Steuerfreibetrag mehr seit 2006).

**Fünftel-Regelung § 34 EStG:**
Die Abfindung wird als außerordentliche Einkunft behandelt: Steuerlast berechnet sich so, als wäre die Abfindung auf 5 Jahre verteilt (fiktive Verteilung). In der Praxis führt dies oft zu spürbarer Steuerersparnis.

> Wichtig: Fünftel-Regelung gilt nur wenn Abfindung als Entschädigung für entgangene Einnahmen geleistet wird (§ 24 Nr. 1 EStG i.V.m. § 34 EStG). Steuerberater einbinden!

### Sozialversicherung

Abfindungen sind grundsätzlich **nicht sozialversicherungspflichtig** — sofern sie als Entschädigungsleistung für Arbeitsplatzverlust gezahlt werden.

**Achtung § 158 SGB III (Ruhenszeitraum):** Bei Zahlung einer Abfindung und Beendigung des AV vor Ablauf der Kündigungsfrist kann das ALG-I ruhen. Mandant über Sperrzeit-Risiko informieren.

## Output-Template — Abfindungsberechnung

**Adressat:** Mandant — Tonfall: erklärend, konkret

```
ABFINDUNGSBERECHNUNG (Schätzung)
Mandant: [NAME]
Beschäftigungsbeginn: [DATUM]
Kündigungsdatum: [DATUM]
Beschäftigungsjahre: [ZAHL] (volle Jahre)
Bruttomonatsgehalt: [BETRAG] Euro (inkl. regelmäßiger Zulagen)

Faustformel (0.5 × Monatslohn × Dienstjahre):
[ZAHL] × 0.5 × [BETRAG] = [ERGEBNIS] Euro brutto

Empfohlene Verhandlungsspanne:
 Untere Grenze (0.25): [BETRAG] Euro brutto
 Faustformel (0.50): [BETRAG] Euro brutto
 Obere Grenze (0.75): [BETRAG] Euro brutto
 (falls starke Rechtsposition: bis [BETRAG] Euro brutto)

Steuerhinweis: Fünftel-Regelung § 34 EStG prüfen (Steuerberater einbinden)
Sperrzeit-Hinweis: § 158-159 SGB III prüfen (Agentur für Arbeit informieren)
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
