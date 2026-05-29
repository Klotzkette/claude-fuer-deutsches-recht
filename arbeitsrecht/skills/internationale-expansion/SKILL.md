---
name: internationale-expansion
description: "Referenz-Skill: Implementierungsplanungs-Framework für internationale Einstellungen — Entscheidungsrahmen AÜG-Modell/EOR vs. eigene Gesellschaft, abteilungsübergreifende Trigger für Steuer/Finance/HR, strukturierter Briefing-Request an externe Arbeitsrechtler und persistenter Lücken-Tracker. Wird von /expansion-auftakt und /expansion-aktualisierung geladen; nicht direkt aufzurufen."
---

# Internationale Expansion — Referenz-Skill (Arbeitsrecht)

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

- Schüren/Hamann, AÜG, 5. Aufl. 2022, § 1 Rn. 1 ff., § 8 Rn. 1 ff.:
  Grundkonzeption des AÜG, Equal-Pay und Ausnahmen durch Tarifvertrag
- Erfurter Kommentar/Wank, 24. Aufl. 2024, § 611a BGB Rn. 1 ff.:
  Arbeitnehmerbegriff — zentrales Merkmal Weisungsgebundenheit; Scheinselbständigkeit
- Rieble/Junker (Hrsg.), Münchener Handbuch zum Arbeitsrecht, Bd. 1,
  5. Aufl. 2021, § 17 Rn. 1 ff.: Grenzüberschreitende Arbeitsverhältnisse;
  Anknüpfung und Rechtswahl nach Art. 8 Rom I-VO

## Ablauf

### Schritt 1 — Informationserhebung

Alle folgenden Fragen in einem einzigen Block stellen:

> Zur Erstellung des Expansionsplans werden folgende Angaben benötigt.
> Beantworte, was bekannt ist — Informationslücken sind selbst nützliche Daten:
>
> **Die Expansion**
> - Welches Land?
> - Welche Rollen werden eingestellt? (Stellenprofil ist entscheidend —
>   ein Vertriebsmitarbeiter mit Abschlussvollmacht erzeugt anderes
>   Betriebsstättenrisiko als eine reine Entwicklerstelle)
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
>   (ein bis zwei Einstellungen, dann bewerten)?
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
>   eigene Gesellschaft kosteneffizienter als EOR (einschließlich EOR-Aufschlag,
>   Gründungskosten, laufender Compliance-Aufwand)?
> - [Falls Betriebsstättenrisiko:] Begründen diese Rollen im Zielland eine
>   steuerliche Betriebsstätte? Falls ja — ändert das die Gründungs-Timeline?
> - Falls mit EOR gestartet und später Gesellschaft gegründet wird: Was sind die
>   Übergangsrisiken für die bereits beim EOR beschäftigten Mitarbeiter?
> - Wer ist unser bevorzugter EOR-Anbieter für dieses Land und ist seine lokale
>   Compliance-Bilanz geprüft worden?

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
>    über Gesellschaft, EOR, Freier Mitarbeiter) und was sind die rechtlichen
>    und praktischen Abwägungen für diesen Headcount und diese Rollen?
>
> 2. **Arbeitsvertragsanforderungen** — Welche Form ist vorgeschrieben oder
>    üblich? Was muss enthalten sein? Was kann nicht wirksam vereinbart werden?
>    Welche Sprach- oder Übersetzungsanforderungen bestehen?
>
> 3. **Kündigung** — Welche Kündigungsfristen und Abfindungspflichten bestehen?
>    Wie schwierig ist eine Kündigung in der Praxis (Kündigungsschutz,
>    Sozialauswahlregeln bei Massenentlassung, Sonderkündigungsschutz)?
>    Welchen Dokumentationsstandard sollten wir von Tag 1 an etablieren?
>
> 4. **Pflichtleistungen und Arbeitgeberanteile** — Was muss gesetzlich
>    geleistet werden (Rente, Kranken-, Sozialversicherung, bezahlter Urlaub,
>    Boni)? Welche aktuellen Arbeitgeberbeitragssätze sind zu budgetieren?
>    Bitte einschlägige Gesetzesnorm angeben und Aktualität bestätigen.
>
> 5. **Wettbewerbsverbote / Geheimhaltung** — Sind nachvertragliche
>    Wettbewerbsverbote durchsetzbar? Unter welchen Bedingungen und gegen
>    welche Karenzentschädigung? Welche Geheimhaltungs- und
>    IP-Übertragungsklauseln halten stand?
>
> 6. **Arbeitnehmervertretung** — Bestehen Betriebsrats-, Arbeitnehmervertretungs-,
>    Gewerkschafts- oder Tarifbindungsanforderungen? Ab welchem Headcount
>    greifen sie? Welche Anhörungs- oder Mitbestimmungsrechte bestehen?
>    Sind wir durch einen Branchentarifvertrag gebunden, auch ohne Gewerkschafts-
>    mitgliedschaft?
>
> 7. **Datenschutz** — Welche Pflichten bestehen für Beschäftigtendaten?
>    Ist ein Datentransfermechanismus für Beschäftigtendaten in die EU oder
>    ins Inland erforderlich?
>
> 8. **Arbeitserlaubnis** — Welche Aufenthaltstitel oder Visa sind für
>    ausländische Staatsangehörige erforderlich? Wie sind die Bearbeitungszeiten?
>
> 9. **Branchenspezifische Regeln** — Gibt es Branchenregeln, Tarifverträge
>    oder kollektive Vereinbarungen, die unabhängig von einer Gewerkschafts-
>    zugehörigkeit für unsere Branche gelten?
>
> 10. **Contractor-Risiko / Scheinselbständigkeit** — Welches Prüfungsmaßstab
>     gilt für die Statusfeststellung und welche Reklassifizierungsrisiken
>     bestehen für etwaige Freelancer-Konstellationen?
>
> 11. **Beteiligungsvergütung** — Gibt es lokale Steuer-, Kapitalmarkt- oder
>     arbeitsrechtliche Regeln für Optionen, Phantom Shares oder andere
>     Beteiligungsprogramme?
>
> 12. **Tag-1-Compliance** — Was muss vor dem ersten Arbeitstag des ersten
>     Mitarbeiters in Ordnung sein? Anmeldungen, Aushangpflichten, Meldungen?
>
> 13. **Die 2–3 Dinge, die ausländische Unternehmen am häufigsten überraschen** —
>     Was wünschen Sie sich, hätten Mandanten früher gefragt? Was hat sich
>     **jüngst geändert**, was ein Team aus dem Inland möglicherweise verpasst hat?

Diesen Briefing-Request als einzelnen offenen Punkt in den Expansions-Tracker aufnehmen:
Verantwortung = Externe Arbeitsrechtler, Status = offen, vollständige Briefing-Agenda
im Fragenfeld. Auch wenn die Jurisdiktion früher schon angefragt wurde, neuen
Briefing-Request senden — dies ist eine Aktualitätsprüfung, kein erstes Mandat.

### Schritt 5 — Expansions-Tracker anlegen

Neue Datei `expansion-[land-slug].yaml` mit allen in Schritten 2–4 identifizierten
offenen Punkten erstellen. Diese Datei persistiert sitzungsübergreifend.

Format:

```yaml
# VERTRAULICH — EXPANSIONSPLANUNG — [Datum]
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
- Schüren/Hamann, AÜG, 5. Aufl. 2022

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
