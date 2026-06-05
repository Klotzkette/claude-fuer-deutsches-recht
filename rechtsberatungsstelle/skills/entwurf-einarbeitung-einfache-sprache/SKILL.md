---
name: entwurf-einarbeitung-einfache-sprache
description: "Entwurf Einarbeitung Einfache Sprache: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Entwurf Einarbeitung Einfache Sprache

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Entwurf Einarbeitung Einfache Sprache** im Plugin Rechtsberatungsstelle (RDG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `entwurf` | Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6 RDG-konforme Formulierung, ausdrücklich als Ausgangspunkt mit anschließender Studierenden- Analyse und Supervisoren-Freigabe. Lädt, wenn ein Studierender einen ersten Entwurf eines Schriftsatzes, Briefes, Antrags oder sonstigen Schriftstücks der Klinik benötigt. |
| `einarbeitung` | Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte Handbuch und vermittelt es interaktiv. Lädt, wenn ein neuer studentischer Berater "Einarbeitung starten", "ich bin neu in der Klinik", "Einführung" sagt oder zu Semesterbeginn gestartet wird; `--karte` für die einseitige Referenzkarte. |
| `einfache-sprache-briefe` | Anwalts- und Behoerdenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behoerde Gericht oder Gegenseite verstehen. BeratungsHiG kostenfreie Beratung, BRAO niedrigschwellige Erstberatung, Leichte-Sprache-Standard. Prüfraster Hauptaussage herausarbeiten, Fachbegriffe ersetzen, kurze Saetze bildhafte Sprache, Rechte und Pflichten klar benennen. Output Brief-Übersetzung in einfacher Sprache mit Erklärung der naechsten Schritte. Abgrenzung zu Mandantenbrief für foermliche Korrespondenz und zu Einfache-Sprache-Jura-Plugin. |

## Arbeitsweg

Im Plugin Rechtsberatungsstelle (RDG) gilt für **Entwurf Einarbeitung Einfache Sprache**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `entwurf`

**Fokus:** Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6 RDG-konforme Formulierung, ausdrücklich als Ausgangspunkt mit anschließender Studierenden- Analyse und Supervisoren-Freigabe. Lädt, wenn ein Studierender einen ersten Entwurf eines Schriftsatzes, Briefes, Antrags oder sonstigen Schriftstücks der Klinik benötigt.

# Schriftsatzentwurf: Erstentwurf-Erstellung

## Zweck

Studierende wenden erhebliche Zeit auf Erstentwürfe von Schriftstücken auf, deren Bildungswert in der rechtlichen Analyse und Strategie liegt — nicht im Abtippen eines Rubrum oder im Formulieren von "Sehr geehrte Damen und Herren". Diese Skill erstellt den Erstentwurf aus Fallnotizen und Rechtsgebiet-spezifischen Mustern, damit die studentische Arbeitszeit dem eigentlichen juristischen Denken zugute kommt.

**Jeder Entwurf ist ausdrücklich ein Ausgangspunkt.** Kein fertiges Arbeitsergebnis. Der/die Studierende analysiert und überarbeitet; der Supervisor prüft, bevor das Schriftstück die Beratungsstelle verlässt.

Beachte: Rechtliche Beratungsleistungen an Einzelpersonen durch Studierende erfolgen nach § 6 Abs. 1 RDG als unentgeltliche Rechtsdienstleistung unter Aufsicht eines zur Rechtsanwaltschaft zugelassenen Supervisors (§ 6 Abs. 2 RDG). Alle nach außen gehenden Schriftstücke sind ohne Supervisoren-Freigabe nicht zu versenden.

## Eingaben

- **Schriftstücktyp** — z. B. `widerspruch`, `klageschrift-ag`, `mahnschreiben`, `beratungshilfe-antrag`, `pkh-antrag`, `mietrechtliches-kündigungsschreiben`
- **Sachverhaltsnotizen / Aktennotiz** — Fakten des Falls; fehlende Angaben werden markiert, nie erfunden
- **Rechtsgebiet** — Mietrecht, Arbeitsrecht, Verwaltungsrecht, Verbraucherrecht u. a.
- **Zuständiges Gericht / Behörde** (falls bekannt) — für Rubrum und Formvorschriften
- **Frist** — ob eine Einreichungsfrist läuft und bis wann

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 6 RDG** — Unentgeltliche Rechtsdienstleistung: zulässig durch Rechtsberatungsstellen unter anwaltlicher Aufsicht; die Aufsicht muss durch eine zur Rechtsanwaltschaft zugelassene Person ausgeübt werden.
- **§ 43a Abs. 2 BRAO** — Mandatsgeheimnis/Verschwiegenheitspflicht: gilt sinngemäß für Studierende der Beratungsstelle; keine Informationen aus dem Mandat nach außen.
- **§ 203 Abs. 3 StGB** — Strafbarkeit der Verletzung von Privatgeheimnissen; Studierende sind als "berufsmäßig tätige Gehilfen" i. S. d. § 203 Abs. 3 S. 2 StGB zu behandeln.
- **§§ 114 ff. ZPO** — Prozesskostenhilfe (PKH): Entwürfe für PKH-Anträge müssen wirtschaftliche Verhältnisse vollständig darlegen; Prüfung hinreichender Erfolgsaussichten (§ 114 Abs. 1 S. 1 ZPO).
- **§§ 1, 2 BerHG** — Beratungshilfe: Voraussetzungen, Bewilligung vor Erbringung der Leistung.
- **§§ 17, 18, 23 VwVfG** — Form von Widersprüchen und Verwaltungsverfahrensschreiben.
- **§ 70 VwGO** — Form des Widerspruchs (schriftlich oder zur Niederschrift); Einreichungsfrist nach §§ 70, 58, 74 VwGO.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1: Welches Schriftstück?

Den Anforderungstyp dem Musterbestand der Beratungsstelle zuordnen. Typischer Bestand nach Rechtsgebiet:

| Rechtsgebiet | Schriftstücke |
|---|---|
| **Mietrecht** | Widerspruch gegen Kündigung, Mängelrüge mit Fristsetzung, Klage auf Kaution, Antrag auf einstweiligen Rechtsschutz |
| **Arbeitsrecht** | Kündigungsschutzklage (AG), Abmahnungsrüge, Zeugnisverlangen, Lohnrückstandsschreiben |
| **Verwaltungsrecht** | Widerspruchsschreiben, Klage beim Verwaltungsgericht (Entwurf), Antrag auf aufschiebende Wirkung (§ 80 Abs. 4, 5 VwGO) |
| **Verbraucherrecht** | Widerrufserklärung (§ 355 BGB), Mahnschreiben, Antwort auf Inkassoschreiben, Antrag auf Lastschriftrückgabe |
| **Allgemein** | Beratungshilfe-Antrag (BerH 1), PKH-Antrag (ZPO 117), Vollmacht, Empfangsbekenntnis |

Falls das angeforderte Schriftstück nicht im Musterbestand vorhanden ist: "Der Musterbestand der Beratungsstelle enthält kein Muster für [X]. Ich kann einen Entwurf nach allgemeinen Grundsätzen versuchen, aber dieser muss besonders sorgfältig geprüft werden — er wurde nicht auf das Rechtsgebiet und die zuständige Behörde/das Gericht abgestimmt. Besser wäre, den Supervisor zu fragen, ob ein bewährtes Muster vorliegt."

### Schritt 2: Sachverhalt aufnehmen

Fallnotizen und Aktennotiz lesen. Für jeden Aspekt, den das Schriftstück benötigt: Liegt die Information vor?

| Schriftstück braucht | Vorhanden? | Quelle |
|---|---|---|
| [Tatsache] | Ja / Nein | [Aktennotiz / Mandantenunterlage / noch zu beschaffen] |

Fehlende notwendige Tatsachen → nicht erfinden. Markierung: `[TATSACHE FEHLT: Zustellungsdatum der Kündigung — aus Briefumschlag oder Postzustellungsurkunde entnehmen]`.

### Schritt 3: Zuständiges Gericht / Behörde und Formvorschriften

- **Rubrum:** Gericht, Aktenzeichen (falls vorhanden), Parteien, Bevollmächtigte/r (Studierender unter Aufsicht des Supervisors)
- **Formvorschriften:** Schriftform, Unterschrift, Einreichungsweg (post, Fax, beA, elektronisch)
- Sind örtliche Besonderheiten nicht bekannt: `[PRÜFEN: Einreichungsweg beim zuständigen Gericht / der zuständigen Behörde überprüfen]`

### Schritt 4: Entwerfen

Das Rechtsgebiet-Muster verwenden. Füllen, was aus den Fakten befüllt werden kann. Platzhalter explizit lassen — niemals mit plausibel klingendem Inhalt füllen.

**Wo immer der Entwurf eine Rechtsbehauptung aufstellt:** Diese Behauptung ist eine Hypothese, die der/die Studierende überprüft, keine Schlussfolgerung, auf die der Entwurf sich verlässt. Entsprechend markieren.

### Schritt 5: Unsicherheiten kennzeichnen

Drei Arten von Markierungen, direkt im Text:

- `[TATSACHE FEHLT: ...]` — das Schriftstück benötigt eine Tatsache, die die Fallnotizen nicht enthalten
- `[PRÜFEN: ...]` — eine Rechts- oder Tatsachenbehauptung, die vor Einreichung überprüft werden muss
- `[UNSICHER: ...]` — der Skill ist genuinely unsicher und sagt dies, anstatt zu raten

### Schritt 6: Supervisoren-Routing

Ein Schriftstück bei Gericht oder einer Behörde einzureichen ist eine folgenschwere Handlung. Das Gate ist das Supervisionsmodell der Beratungsstelle, verstärkt durch die Grundvoraussetzung, dass ein zugelassener Rechtsanwalt/eine zugelassene Rechtsanwältin die Aufsicht innehat (§ 6 Abs. 2 RDG). Gerichtliche und behördliche Einreichungen gehen immer durch die Supervisoren-Prüfung, unabhängig vom gewählten Supervisionsmodell.

- **Formelle Prüfwarteschlange:** Entwurf geht in die Warteschlange; Studierender sieht "in Warteschlange für [Supervisor]"
- **Konfigurierbare Flags:** Wenn dieser Schriftstücktyp ein Flag auslöst (gerichtliche Einreichungen in der Regel immer), enthält der Output: "VOR DER EINREICHUNG MIT [SUPERVISOR] ABSPRECHEN"
- **Leichtere Begleitung:** Standard-Sicherheitslabel; keine zusätzliche Schranke — aber gerichtliche Einreichungen gehen per Klinikverfahren dennoch an den Supervisor vor Einreichung

## Ausgabeformat

```
═══════════════════════════════════════════════════════════════════════
 KI-GESTÜTZTER ENTWURF — ERFORDERT STUDENTISCHE ANALYSE UND SUPERVISOREN-PRÜFUNG
 Dies ist ein Ausgangspunkt, kein fertiggestelltes Arbeitsergebnis.
 Jedes [PRÜFEN]- und [TATSACHE FEHLT]-Flag muss vor der Einreichung aufgelöst werden.
 § 6 Abs. 2 RDG: Einreichung erst nach Supervisoren-Freigabe.
═══════════════════════════════════════════════════════════════════════

[Das Schriftstück — im Rechtsgebiet-Musterformat, formvorschriftengerecht,
mit Flags direkt im Text]

═══════════════════════════════════════════════════════════════════════

## Prüfliste für Studierende

Vor Vorlage an [Supervisor]:

- [ ] Das Schriftstück vollständig lesen. Sagt es das, was ausgedrückt werden soll?
- [ ] Jede Tatsache: stimmt sie mit den tatsächlichen Mandantenunterlagen überein?
- [ ] Jedes [PRÜFEN]-Flag: durch Recherche aufgelöst oder gestrichen
- [ ] Jedes [TATSACHE FEHLT]-Flag: mit verifizierten Informationen gefüllt oder Abschnitt entfernt
- [ ] Rechtsgrundlage: ist dies die richtige Argumentation? Gibt es bessere Ansätze? (Das ist die Analyse des Studierenden, nicht des Entwurfs.)
- [ ] Formvorschriften: Rubrum, Einreichungsweg, Format nach aktuellen Vorschriften korrekt?
- [ ] [Supervisionsschritt per Klinik-Konfiguration]
```

## Beispiel

**Szenario:** Mandantin Erdem erhält eine fristlose Kündigung ihres Arbeitsverhältnisses. Kündigung zugestellt am 15.04.2026. Studierender Müller soll einen Entwurf der Kündigungsschutzklage beim Arbeitsgericht Berlin erstellen.

```
/entwurf kündigungsschutzklage-ag
Fall: Erdem-Arbeitsrecht-2026
Frist: 06.05.2026 (3 Wochen ab 15.04.2026, § 4 KSchG)
Arbeitgeber: Beispiel GmbH, Musterstraße 1, 10115 Berlin
```

Entwurf enthält: Rubrum (AG Berlin), Anträge, Klagebegründung mit `[PRÜFEN: Beschäftigungsdauer und Betriebsgröße für Anwendbarkeit KSchG]`, `[TATSACHE FEHLT: Datum des Arbeitsvertragsabschlusses]`.

## Risiken und typische Fehler

- **Frist nicht beachtet:** Der Entwurf weist auf erkannte Fristen hin, berechnet sie aber nicht selbst. Studierende müssen die Dreiwochenfrist des § 4 KSchG, die Widerspruchsfrist (§ 70 VwGO), Verjährungsfristen (§ 195 BGB) eigenständig prüfen und in `/fristen` eintragen.
- **Rubrum falsch:** Zuständigkeit, Parteibezeichnungen, Aktenzeichen müssen überprüft werden. Fehlerhaftes Rubrum kann zur Unzulässigkeit führen.
- **PKH-Antrag vergessen:** Wenn die Mandantin/der Mandant nicht zahlungsfähig ist, muss gleichzeitig mit der Klage ein PKH-Antrag (§ 117 ZPO) eingereicht werden.
- **Entwurf verlässt Klinik ohne Freigabe:** § 6 Abs. 2 RDG verlangt anwaltliche Aufsicht. Kein Entwurf wird dem Mandanten oder einer Behörde/einem Gericht ohne Supervisoren-Freigabe zugeleitet.
- **Falsche Rechtsgrundlagen:** Rechtsbehauptungen im Entwurf sind Hypothesen. Der/die Studierende verifiziert jede Norm und Rechtsprechung, bevor der Entwurf weitergereicht wird.

## Quellenpflicht

Jede Rechtsbehauptung im Entwurf ist mit der einschlägigen Norm oder Entscheidung zu belegen. Vorgeschlagene Quellen aus dem Modell sind mit `[Modellwissen — verifizieren]` zu kennzeichnen und vor Verwendung gegen aktuelle Datenbanken (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, dejure) zu prüfen. Niemals ohne Quellangabe und Supervisoren-Freigabe einreichen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 2. `einarbeitung`

**Fokus:** Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte Handbuch und vermittelt es interaktiv. Lädt, wenn ein neuer studentischer Berater "Einarbeitung starten", "ich bin neu in der Klinik", "Einführung" sagt oder zu Semesterbeginn gestartet wird; `--karte` für die einseitige Referenzkarte.

# Einarbeitung: Semestereinarbeitung

## Zweck

Jedes Semester verliert die Rechtsberatungsstelle ihre gesamte studentische Belegschaft und baut sie neu auf. Neue Studierende müssen Verfahrensabläufe, Mandatsverwaltung, Einreichungskonventionen und Rechtsgebiet-Grundlagen kennenlernen, bevor sie produktiv arbeiten können. Traditionell kostet das Wochen mit PDF-Lektüre und immer wiederkehrenden Fragen an den Supervisor.

Diese Skill ist der geführte Walkthrough. Sie liest, was der Supervisor beim Kalt-Start hinterlegt hat — das Handbuch, Einreichungsanleitungen, Verfahrensregeln — und vermittelt es interaktiv, mit Übungsaufgaben in einem sicheren Rahmen, bevor ein echter Mandant betroffen ist.

**Zielgruppe: Studierende.** Supervisoren nutzen `/kalt-start-interview`.

## Eingaben

Keine aktiven Eingaben — die Skill liest die Klinik-Konfiguration (CLAUDE.md) und das hinterlegte Handbuch.

Falls die Konfigurationsdatei fehlt oder noch Platzhalter enthält: "Die Beratungsstelle ist noch nicht eingerichtet. Bitten Sie [Supervisor] zuerst `/kalt-start-interview` auszuführen."

## Rechtlicher Rahmen

### Kernvorschriften für die Einarbeitung

- **§ 6 Abs. 1 RDG** — Unentgeltliche Rechtsdienstleistung: Studierende dürfen im Rahmen der Rechtsberatungsstelle Rechtsberatung erbringen, soweit sie unentgeltlich erfolgt und unter Aufsicht eines Rechtsanwalts/einer Rechtsanwältin steht.
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht des begleitenden Rechtsanwalts/der begleitenden Rechtsanwältin: Die Aufsichtsperson muss zur Rechtsanwaltschaft zugelassen sein; die Aufsicht muss inhaltlich effektiv sein (kein Formalia-Supervisor).
- **§ 43a Abs. 2 BRAO, § 203 Abs. 3 StGB** — Mandatsgeheimnis und Verschwiegenheitspflicht: Gilt sinngemäß für Studierende als berufsmäßig tätige Gehilfen. Alle Mandantendaten, Fallnotizen und Korrespondenz sind vertraulich. Kein Austausch über Mandate außerhalb der Beratungsstelle.
- **§§ 1, 2 BerHG** — Beratungshilfe: Häufig in der Mandatsarbeit relevant; Studierende müssen wissen, wann ein Beratungshilfe-Schein vor Leistungsbeginn einzuholen ist.
- **§§ 114 ff. ZPO** — Prozesskostenhilfe (PKH): Voraussetzungen und typisches Prozedere in der Mandatsarbeit.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Begrüßung

> Willkommen in der [Name der Beratungsstelle]. Ich führe Sie durch die Arbeitsweise dieser Beratungsstelle und die verfügbaren Tools — ca. zwanzig Minuten, Pause jederzeit möglich. Am Ende haben Sie eine Übungsberatung durchgeführt, einen Übungsentwurf erstellt und einen Recherchefahrplan erarbeitet.
>
> Ein wichtiger Grundsatz vorab: Alles, was ich erzeuge, ist ein Ausgangspunkt. Die rechtliche Analyse kommt von Ihnen. [Supervisor] prüft Ihre Arbeit [entsprechend dem Supervisionsmodell]. Ich übernehme die Formatierung und den Erstentwurf, damit Ihre Zeit der juristischen Denkarbeit zugute kommt.
>
> Was Sie als Studierender nach § 6 RDG dürfen und was nicht: Sie beraten unter Aufsicht und unentgeltlich. Sie erstellen keine selbständigen Rechtsprodukte ohne Supervisoren-Freigabe. Jedes nach außen gehende Schriftstück und jede Mandantenauskunft zu strittigen Rechtsfragen wird vom Supervisor freigegeben.

### Teil 1: Diese Beratungsstelle (5 Min)

Aus der Klinik-Konfiguration und dem hinterlegten Handbuch. Interaktiv abarbeiten:

- **Rechtsgebiete** — Was berät die Klinik? Was nicht? (Und wohin verweisen, wenn jemand mit einem nicht abgedeckten Problem kommt?)
- **Mandanten** — Wer kommt? Welche besonderen Umstände gibt es (Sprache, Vulnerable Gruppen, unbegleitete Minderjährige)?
- **Zuständiges Gericht / Behörden** — Welche Gerichte und Behörden sind für die Klinik regelmäßig relevant? Lokale Besonderheiten?
- **Mandatsverwaltung** — Wie werden Mandate geführt, wo liegen Akten, was ist ein gut dokumentierter Fall?
- **Supervision** — Wie läuft die Prüfung ab (entsprechend dem Supervisionsmodell). Konkret: "Bevor etwas zum Mandanten oder an ein Gericht geht, [kommt es in die Prüfwarteschlange / sprechen Sie mit Frau/Herrn X / etc.]"

Kein Monolog — Verständnis überprüfen: "Wenn ein Mandant mit einem Räumungsbegehren und gleichzeitig einem Aufenthaltsrechtsproblem kommt — was tun Sie?" (Antwort: Beide Fragen in der Aktennotiz festhalten; das Aufenthaltsrechtsproblem ggf. an spezialisierte Flüchtlingsberatung weiterleiten oder dem Supervisor flaggen, je nach Tätigkeitsbereich der Klinik.)

### Teil 2: Die Befehle (5 Min)

| Befehl | Wann verwenden | Was Sie bekommen |
|---|---|---|
| `/mandanten-aufnahme` | Beratungsgespräch | Strukturierte Fallzusammenfassung mit erkannten Rechtsfragen, Interessenkollisionsprüfung, Triage |
| `/entwurf [Schriftstücktyp]` | Erstentwurf eines häufigen Schriftstücks | Rechtsgebiet-Muster aus den Fallnotizen — *Ausgangspunkt, nicht fertig* |
| `/memo` | Interne Fallanalyse | Gutachten-Gerüst nach Gutachtenmethode mit gekennzeichneten Recherchelücken |
| `/recherche-start [Frage]` | Einstieg in Rechtsrecherche | Recherchefahrplan: Normen, Rspr.-Bereiche, Suchbegriffe — *Hinweise, keine geprüften Belege* |
| `/status [Zielgruppe]` | Jemanden über einen Fall informieren | Zusammenfassung für Mandant / Supervisor / Gericht |
| `/mandantenbrief [typ]` | Routine-Korrespondenz | Terminbestätigung, Unterlagenbitte, Statusupdate aus Mustern |

Für jeden Befehl: was er tut, was er ausdrücklich nicht tut, was der/die Studierende vor dem Verwenden prüft.

### Teil 3: Übungsaufgaben (8–10 Min)

**Ohne Risiko. Fiktiver Mandant. Echte Tools.**

**Übung 1 — Übungsaufnahme:**
> Hier ist ein fiktives Szenario: [Rechtsgebiet-angepasste Aufgabe — z. B. für eine Mietrechtsklinik: "Frau Erdem hat letzte Woche eine fristlose Kündigung erhalten. Sie ist mit zwei Monatsmieten im Rückstand, nachdem sie ihren Job verloren hat. Die Heizung ist seit November defekt. Sie hat zwei Kinder."]
>
> Führen Sie `/mandanten-aufnahme` aus und sprechen Sie mit mir wie mit Frau Erdem. Ich antworte wie Frau Erdem. Schauen Sie am Ende auf die erzeugte Fallzusammenfassung: Welche Rechtsfragen wurden erkannt? Wurde die Mängeleinrede (§ 536 BGB) als mögliche Verteidigung erkannt?

Nachbesprechung: Was die Aufnahme erfasst hat, wo der Studierende tiefer hätte bohren sollen, was dem Supervisor zu flaggen ist.

**Übung 2 — Übungsentwurf:**
> Verwenden Sie Frau Erdems Aufnahme und führen Sie `/entwurf widerspruch-kündigung` aus. Sie erhalten einen Erstentwurf.
>
> Lesen Sie ihn kritisch. Was ist richtig? Was ist falsch? Was würden Sie vor Vorlage an [Supervisor] ändern?

Ziel: Der Entwurf ist kompetent, aber nicht abschließend. Der Studierende lernt, kritisch zu lesen statt blind zu akzeptieren.

**Übung 3 — Recherchefahrplan:**
> Führen Sie `/recherche-start "Mietminderung wegen Heizungsausfall nach § 536 BGB"` aus. Sie erhalten einen Fahrplan — Normen, Rspr.-Bereiche, Suchbegriffe.
>
> Nichts davon ist geprüft. Das ist so gewollt. Nennen Sie eine Norm aus dem Fahrplan und beschreiben Sie, wie Sie deren Aktualität und Einschlägigkeit prüfen würden.

Ziel: `/recherche-start` ist ein Startpunkt, keine Quelle. Der Studierende forscht selbst.

### Teil 4: Verifikationsgewohnheiten (2 Min)

Die entscheidenden Gewohnheiten:

- **Jede Ausgabe ist ein Ausgangspunkt.** Wenn etwas den Mandanten oder ein Gericht erreicht, ohne dass Sie es kritisch gelesen haben, ist etwas schiefgelaufen.
- **Jede Quelle verifizieren**, bevor sie in ein Schriftstück fließt. `/recherche-start` gibt Hinweise, keine Belege.
- **Rechtsgebiet-spezifische Details prüfen.** Die Konfiguration kennt Ihr Bundesland; lokale Besonderheiten ändern sich — aktuell gültige Regeln gegenprüfen.
- **UNSICHER-Flags ernst nehmen.** Ein `[UNSICHER: ...]`-Flag ist ein Rechercheauftrag oder ein Thema für den Supervisor, kein zu löschender Fehler.
- **Mandatsgeheimnis immer.** Keine Fallinformationen außerhalb der Beratungsstelle weitergeben, auch nicht zum "Erklären" — § 203 StGB.
- **[Supervisionshinweis entsprechend dem Klinik-Modell]** — was wird geprüft, bevor es die Klinik verlässt, und wie.

### Abschluss

> Das war es. Sie haben eine Aufnahme durchgeführt, einen Entwurf erstellt und einen Recherchefahrplan erarbeitet. Ihr erster echter Fall wird ähnlich ablaufen — mit dem Unterschied, dass der Mandant real ist und der Supervisor Ihre Arbeit liest.
>
> Die einseitige Referenzkarte: `/einarbeitung --karte`

## `/einarbeitung --karte`

Erzeugt die einseitige Studentenreferenzkarte. Inhalt:

- Die Befehle (Tabelle aus Teil 2, komprimiert)
- Was die KI leisten kann / was nicht (Ausgangspunkte ja, fertige Arbeitsergebnisse nein, geprüfte Quellen nein)
- Verifikationsgewohnheiten (Punkte aus Teil 4)
- Wen fragen bei Unklarheiten (Supervisorenname aus CLAUDE.md)
- **RDG-Kurzhinweis:** Was Studierende nach § 6 RDG dürfen und was nicht

Druckfähig. Eine Seite. Am ersten Tag aushändigen.

## Risiken und typische Fehler

- **Einarbeitung als Formalität behandeln:** Die Übungsaufgaben sind der Kern. Studierende, die sie überspringen, gehen mit falscher Sicherheit ins erste echte Mandat.
- **RDG-Grenzen nicht verinnerlicht:** Studierende müssen wissen, dass sie nur unter Aufsicht und unentgeltlich tätig sind. Kein eigenständiges Handeln ohne Supervisoren-Rückkopplung.
- **Mandatsgeheimnis vergessen:** Bereits in der Übungsphase: Fallhypothetika enthalten keine echten Mandantendaten. In der echten Arbeit: strikte Vertraulichkeit nach § 203 StGB.
- **Supervisor nicht eingerichtet:** Wenn die CLAUDE.md Platzhalter enthält, ist die Einarbeitung zu stoppen und dem Supervisor zur Einrichtung zu übergeben.

## Quellenpflicht

Die Einarbeitung selbst enthält keine zitierpflichtigen Belege — die RDG-Normen und Grundsätze werden im Überblick vermittelt. Sobald echte Mandate bearbeitet werden, gilt die Quellenpflicht aus den jeweiligen Skills (`/memo`, `/entwurf`, `/recherche-start`).

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall und keine juristische Ausbildung. Die inhaltliche Einführung in das Rechtsgebiet übernimmt der Supervisor, nicht dieses Tool.

## Ausgabeformat

Die Einarbeitung läuft interaktiv — keine einmalige Ausgabe, sondern ein geführtes Gespräch in vier Teilen (Klinik-Kontext, Befehle, Übungsaufgaben, Verifikationsgewohnheiten). Jeder Teil schließt mit einer Verständnisfrage oder einer Übung, bevor zum nächsten Teil übergegangen wird.

`/einarbeitung --karte` erzeugt eine druckbare, einseitige Referenzkarte (Markdown, ggf. in PDF exportierbar) mit den wesentlichen Befehlen, Verifikationsgewohnheiten und dem RDG-Kurzhinweis.

## Beispiel

**Szenario:** Neue Studierende Hofer betritt die Mietrechtsklinik zu Beginn des Wintersemesters. Sie führt `/einarbeitung` aus.

Teil 1: Klinik-Konfiguration wird gelesen; Hofer erfährt, dass die Klinik Mietrecht und Verbraucherrecht abdeckt, nicht aber Strafrecht (Verweisung an Rechtsberatungsstelle der Strafrechts-Vertiefung). Supervisorin: Rechtsanwältin Dr. Weber.

Teil 2: Befehlsübersicht. Hofer fragt: "Was macht `/memo`?" → Erklärung: Gutachten-Gerüst nach Gutachtenmethode, kein fertiges Gutachten.

Teil 3, Übung 1: Fiktiver Fall "Frau Erdem — Heizung defekt seit November". Hofer führt `/mandanten-aufnahme` durch, identifiziert Mietminderung (§ 536 BGB) und Mangel (§ 535 BGB) als Fragen. Nachbesprechung: Hofer hätte nach dem Datum der Mängelanzeige fragen sollen.

Übung 2: `/entwurf widerspruch-kündigung` — Hofer liest den Entwurf kritisch: "Der Entwurf nennt die Frist als 10.05.2026, aber die Kündigung war am 09.04. zugegangen — ich muss die Dreiwochenfrist für Kündigungsschutz prüfen."

Übung 3: `/recherche-start "§ 536 BGB Mietminderung Heizungsausfall"` → Fahrplan mit ungeprüften Normen. Hofer wählt § 536c BGB und erklärt: Prüfung über juris mit Aktualitätsdatum.

Teil 4: Verifikationsgewohnheiten besprochen. Abschluss: `/einarbeitung --karte` aufgerufen.

## 3. `einfache-sprache-briefe`

**Fokus:** Anwalts- und Behoerdenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behoerde Gericht oder Gegenseite verstehen. BeratungsHiG kostenfreie Beratung, BRAO niedrigschwellige Erstberatung, Leichte-Sprache-Standard. Prüfraster Hauptaussage herausarbeiten, Fachbegriffe ersetzen, kurze Saetze bildhafte Sprache, Rechte und Pflichten klar benennen. Output Brief-Übersetzung in einfacher Sprache mit Erklärung der naechsten Schritte. Abgrenzung zu Mandantenbrief für foermliche Korrespondenz und zu Einfache-Sprache-Jura-Plugin.

# [VERALTET] Verständliche Mandantenbriefe → siehe `/mandantenbrief` und `/status mandant`

## Zweck

Diese Skill wurde im Rahmen des Umbaus auf Version 2 aufgeteilt, weil der ursprüngliche Geltungsbereich zu heterogen war: einfache Terminbestätigungen haben andere Anforderungen als inhaltlich komplexe Statusmitteilungen.

**Routine-Korrespondenz** (Terminbestätigungen, Unterlagenbitten, kurze Eingangsbestätigungen) → `skills/mandantenbrief/` — Befehl `/mandantenbrief [typ]`

**Inhaltliche Statusmitteilungen an Mandanten** (was ist passiert, was passiert als nächstes, was muss der Mandant tun) → `skills/status/` im Mandanten-Modus — Befehl `/status mandant`

Beide Nachfolge-Skills wenden die Verständlichkeitsstandards der Beratungsstelle an (Lesbarkeit Hauptschulniveau, keine nicht erläuterten Fachbegriffe, konkrete Handlungshinweise), wie sie in der Klinik-Konfiguration (CLAUDE.md) festgelegt sind.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Mandantenbriefe: `/mandantenbrief [typ]` oder `/status mandant`.

## Rechtlicher Rahmen

### Hintergrund der Aufteilung

Die Verständlichkeit von Mandantenkommunikation ist eine Rechtspflicht, keine Serviceleistung. Unverständliche Korrespondenz verletzt die anwaltliche Aufklärungspflicht (§ 43a BRAO, BGH-Rspr.) und kann zur Haftung führen. Die Aufteilung in zwei fokussierte Skills verstärkt diese Pflicht, indem sie die Standards für jeden Typ explizit macht.

### Relevante Normen für die Nachfolge-Skills

- **§ 43a Abs. 4 BRAO** — Sachlichkeitsgebot: Mandantenbriefe müssen sachlich, klar und nicht irreführend sein; gilt auch für studentische Beratungsstellen unter Aufsicht.
- **§ 11a BRAO** — Zusammenarbeit in studentischen Beratungsstellen: Briefe gehen unter Aufsicht des Supervisors heraus; vor Versand ist die Supervisoren-Freigabe einzuholen.
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Mandantenkorrespondenz ist ein nach außen gehendes Leistungsergebnis und unterliegt der inhaltlichen Supervisoren-Kontrolle.
- **Art. 13 DSGVO** — Informationspflichten: Falls ein Brief erstmals über die Verarbeitung personenbezogener Daten informiert, müssen DSGVO-Pflichtangaben enthalten sein.
- **§§ 2, 3 BerHG** — Beratungshilfe: Bei Mandanten mit Beratungshilfe-Schein muss die Korrespondenz den Leistungsrahmen einhalten; keine Erweiterung ohne neuen Schein.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

**Stattdessen verwenden:**

Für einfache Korrespondenz (Terminbestätigung, Unterlagenbitte, Eingangsbestätigung):
```
/mandantenbrief terminbestätigung
/mandantenbrief unterlagenbitte
/mandantenbrief eingangsbestätigung
```

Für inhaltliche Statusmitteilungen:
```
/status mandant
```

Vollständiger Ablauf in den jeweiligen SKILL.md-Dateien:

1. Zielgruppe festlegen (Bildungshintergrund, Sprache, besondere Umstände des Mandanten)
2. Verständlichkeitsstandards der Klinik anwenden (Klinik-Konfiguration → plain-language-standard)
3. Kein Fachjargon ohne Erläuterung; kurze Sätze; konkrete Handlungsanweisungen
4. Supervisoren-Routing nach § 6 Abs. 2 RDG vor Versand

## Ausgabeformat

Keine Ausgabe — diese Skill ist inaktiv. Weiterleitung auf `/mandantenbrief [typ]` oder `/status mandant`.

## Beispiel

Statt `/einfache-sprache-briefe`:

```
/status mandant
```

Dieser Befehl erstellt ein verständliches Statusschreiben (Zielgruppe: Mandant/-in) nach dem Hauptschulniveau-Standard, ohne Fachjargon, mit konkreten nächsten Schritten: "Was ist passiert / Was passiert als nächstes / Was müssen Sie tun / So erreichen Sie uns."

Oder für Routine-Korrespondenz:
```
/mandantenbrief terminbestätigung
```

Ergebnis: Eine klare Terminbestätigung mit Ort, Zeit, Mitnahme-Unterlagen und Kontaktdaten — ohne juristische Formulierungen.

## Risiken und typische Fehler

- **Verweis auf diese Skill in älteren Materialien:** Semesterskripte und Tutorenmaterialien auf die neuen Skills umschreiben.
- **Verständlichkeitsstandards als optional behandeln:** Die Pflicht zur verständlichen Mandantenkommunikation ergibt sich aus § 43a BRAO und BGH-Rspr. Sie gilt auch für Studierende in der Beratungsstelle unter Supervisorenaufsicht.
- **Fachbegriffe ohne Erläuterung:** Begriffe wie "Widerspruchsfrist", "Vollstreckungstitel" oder "Klagefrist" sind für viele Mandanten unverständlich. Immer in Klammern oder mit einfachem Folgesatz erläutern.
- **Versand ohne Supervisoren-Freigabe:** Kein Mandantenbrief verlässt die Beratungsstelle ohne Freigabe, auch keine kurze Terminbestätigung.

## Quellenpflicht

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben zu Mandantenbriefen: `skills/status/SKILL.md`, Sektion "Quellenpflicht", und `skills/mandantenbrief/SKILL.md`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
