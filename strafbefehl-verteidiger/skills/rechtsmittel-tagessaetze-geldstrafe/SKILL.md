---
name: rechtsmittel-tagessaetze-geldstrafe
description: "Rechtsmittel Tagessaetze Geldstrafe: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsmittel Tagessaetze Geldstrafe

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Rechtsmittel Tagessaetze Geldstrafe** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafbefehl-rechtsmittel-nach-urteil` | Rechtsmittel nach Urteil in der Hauptverhandlung nach Strafbefehl-Einspruch. Berufung § 312 StPO (Frist 1 Woche schriftlich). Revision § 333 StPO (Frist 1 Woche Rechtsfehler). Revisionsbegründung § 345 StPO 1 Monat. Absolute Revisionsgründe § 338 StPO. Beschränkung auf Strafe. |
| `strafbefehl-tagessaetze-geldstrafe` | Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Einkommensnachweise. Ratenzahlungsantrag § 42 StGB. Ersatzfreiheitsstrafe § 43 StGB. |
| `strafbefehl-wiedereinsetzung` | Wiedereinsetzung in den vorigen Stand nach § 44 StPO bei versaeumter Einspruchsfrist. Voraussetzungen: kein Verschulden. Antragsfrist 1 Woche. Glaubhaftmachung § 45 StPO. Zustellungsfiktion entgegnen. Eidesstattliche Versicherung. Wiedereinsetzung und gleichzeitiger Einspruch. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Rechtsmittel Tagessaetze Geldstrafe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafbefehl-rechtsmittel-nach-urteil`

**Fokus:** Rechtsmittel nach Urteil in der Hauptverhandlung nach Strafbefehl-Einspruch. Berufung § 312 StPO (Frist 1 Woche schriftlich). Revision § 333 StPO (Frist 1 Woche Rechtsfehler). Revisionsbegründung § 345 StPO 1 Monat. Absolute Revisionsgründe § 338 StPO. Beschränkung auf Strafe.

# Rechtsmittel nach Urteil im Strafbefehlsverfahren

## Triage zu Beginn

1. **Welches Gericht hat verurteilt?** — Amtsgericht (Strafrichter): Berufung zum LG oder Revision zum OLG (§§ 312, 335 StPO); LG: nur Revision zum BGH.
2. **Was soll angegriffen werden?** — Tatsachenfeststellung → Berufung; Rechtsfehler → Revision; Strafmass → wahlweise beides.
3. **Frist:** Berufung und Revision: 1 Woche ab Urteilsverkuendung, schriftlich oder protokollarisch (§§ 314, 341 StPO).
4. **Revision oder Berufung?** — Berufung ist neue Verhandlung in der Tatsache; Revision prueft nur Rechtsfehler. Sprung-Revision (§ 335 StPO) direkt vom AG zum OLG moeglich.
5. **Beschraenkung auf Strafmass?** — Berufung kann auf Rechtsfolgen beschraenkt werden wenn Schuldfeststellung unstreitig ist.

## Zentrale Normen

- **§ 312 StPO** — Berufung gegen Urteile des Strafrichters und Schoeffengerichts; Frist 1 Woche
- **§ 313 StPO** — Annahme-Berufung bei Urteilen mit Geldstrafe bis 15 Tagessaetze oder Freiheitsstrafe bis 3 Monate; LG kann Annahme verweigern
- **§ 314 StPO** — Einlegung der Berufung: schriftlich oder zu Protokoll
- **§ 317 StPO** — Berufungsbegründung (keine Pflicht aber empfehlenswert)
- **§ 333 StPO** — Revision gegen Urteile
- **§ 335 StPO** — Sprung-Revision direkt zum OLG
- **§ 341 StPO** — Einlegung der Revision: 1 Woche, schriftlich oder zu Protokoll
- **§ 344 StPO** — Revisionsbegründung: Erklaerung, welche gesetzlichen Vorschriften verletzt sind
- **§ 345 StPO** — Revisionsbegründungsfrist: 1 Monat nach Zustellung der Urteilsgruende
- **§ 338 StPO** — Absolute Revisionsgründe (z.B. Verletzung letztes Wort, Verletzung gesetzlicher Richter)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Rechtsmittelwahl

```
Urteil des Amtsgerichts:
├─ Tatsachen falsch festgestellt? → Berufung (§ 312 StPO)
│ ├─ Nur Strafmass zu hoch? → Beschraenkte Berufung auf Rechtsfolgen
│ └─ Vollstaendige Neuverhandlung gewollt? → Unbeschraenkte Berufung
├─ Rechtsfehler (Verfahrens- oder Sachfehler)? → Revision (§ 333 StPO)
│ ├─ Absoluter Revisionsgrund (§ 338 StPO)? → Revision fast immer erfolgversprechend
│ └─ Sachruege (Rechtsfehler bei Strafzumessung, Tatbestand)? → Revision mit Begruendung
└─ Sprung-Revision (§ 335 StPO)?
 └─ Wenn Berufung wenig Aussicht und Rechtsfrage klar → direkt zu OLG

Fristenkontrolle:
□ 1 Woche Rechtsmittelfrist (§§ 314, 341 StPO)
□ 1 Monat Revisionsbegründungsfrist ab Urteilszustellung (§ 345 StPO)
□ Fristverlängerung moeglich?
```

## Output-Template Berufungsschrift

```
An das Landgericht [ORT]
— Berufungskammer —
[Anschrift]

In der Strafsache gegen [NAME]
Az. AG: [AKTENZEICHEN]

Berufung nach § 312 StPO

Namens des Angeklagten lege ich gegen das Urteil des Amtsgerichts
[ORT] vom [DATUM] frist- und formgerecht

Berufung

ein. Die Berufung wird [auf die Rechtsfolgen beschraenkt /
vollumfaenglich] erhoben.

Ich bitte um Mitteilung des Termins zur Berufungsverhandlung.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Rechtsmittelfrist 1 Woche — sofort nach Urteil eintragen, keine Ausnahmen.
- Revisionsbegründungsfrist 1 Monat — nach Zustellung der Urteilsgruende; nicht ab Verkuendung.
- Annahme-Berufung (§ 313 StPO): Erfolgsaussichten darlegen.
- Anwaltliche Endkontrolle vor Einlegung und vor Begründung.

## 2. `strafbefehl-tagessaetze-geldstrafe`

**Fokus:** Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Einkommensnachweise. Ratenzahlungsantrag § 42 StGB. Ersatzfreiheitsstrafe § 43 StGB.

# Tagessaetze und Geldstrafe — §§ 40 bis 43 StGB

## Triage zu Beginn

1. **Wie viele Tagessaetze sind im Strafbefehl festgesetzt?** — Anzahl bestimmt Schuldgewicht, Hoehe das Nettoeinkommen.
2. **Tagessatzhoehe korrekt?** — Nettoeinkommen / 30 = Tagessatz (§ 40 Abs. 2 StGB); zu hoch wenn Einkommen ueberschaetzt.
3. **Liegt Einkommensnachweis vor?** — Lohnabrechnung, Steuerbescheid, BWA bei Selbststaendigen.
4. **Ratenzahlung noetig?** — § 42 StGB: Gericht kann Ratenzahlung gestatten; Antrag bei Zahlungsunfaehigkeit.
5. **Kann Geldstrafe nicht bezahlt werden?** — Ersatzfreiheitsstrafe droht (§ 43 StGB: 1 Tag Freiheitsstrafe pro uneinbringlichem Tagessatz).

## Zentrale Normen

- **§ 40 Abs. 1 StGB** — Geldstrafe: 5 bis 360 Tagessaetze (bei Mehrfachverstoss bis 720)
- **§ 40 Abs. 2 StGB** — Tagessatz: Dreissigstel des monatlichen Nettoeinkommens; Mindest 1 EUR
- **§ 40 Abs. 2 Satz 3 StGB** — Schaetzungsrecht des Gerichts wenn genaues Einkommen nicht feststellbar
- **§ 41 StGB** — Geldstrafe neben Freiheitsstrafe moeglich
- **§ 42 StGB** — Zahlungserleichterungen, Ratenzahlung
- **§ 43 StGB** — Ersatzfreiheitsstrafe: 1 Tag pro Tagessatz, mind. 1 Tag
- **§ 459d StPO** — Uneinbringlichkeit der Geldstrafe: Vollstreckungsgericht entscheidet

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BGH 15.07.2025 — 2 StR 644/24: KCanG-Strafzumessung — die gesetzliche Wertung des § 1 Nr. 8 ff. KCanG ist als bestimmender Strafzumessungsgrund zu beruecksichtigen; das wirkt auch auf die Tagessatzhoehe und die Anzahl der Tagessaetze bei Cannabisvorwurf. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+StR+644/24
- BGH (GSSt) 03.02.2025 — GSSt 1/24: Sanktionsfreie Eigenkonsummengen sind aus der Einziehung herauszunehmen — relevant fuer die Bemessung in KCanG-Strafbefehlen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- Hinweis: Eine aktuelle BGH-Leitentscheidung 2025/2026 zu § 40 StGB / Tagessatzbemessung im Strafbefehl ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 40 StGB Tagessatzhoehe Nettoeinkommen" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berechnungsschema Tagessatz

```
1. Bruttoeinkommen monatlich: [BETRAG] EUR
2. Abzuege (Lohnsteuer, SV-Beitraege): [BETRAG] EUR
3. Nettoeinkommen: [BETRAG] EUR
4. Tagessatz (Netto / 30): [BETRAG] EUR

Besonderheiten:
- Fahrtkosten / Werbungskosten: koennen abgezogen werden
- Unterhaltspflichten: mindern verfuegbares Einkommen (§ 40 Abs. 2 Satz 2)
- Schulden / Verbindlichkeiten: einzelfallabhaengig, kein automatischer Abzug
- Selbststaendige: Gewinn lt. Steuerbescheid / 12 als Monats-"Netto"
```

## Einkommensnachweise-Checkliste

```
□ Lohnabrechnung letzter 3 Monate
□ Steuerbescheid letztes Jahr
□ Rentennachweis (bei Rentnern)
□ Buchfuehrungs-Zusammenfassung / BWA (bei Selbststaendigen)
□ ALG-II-/Buergergeld-Bescheid (bei ALG-II-Empfaengern: ca. 1-2 EUR Tagessatz)
□ Unterhaltsnachweis (belegt Verbindlichkeiten)
□ Kreditvertraege (monatliche Belastungen)
```

## Antrag auf Ratenzahlung — Template

**Adressat:** Vollstreckungsgericht / Staatsanwaltschaft — Tonfall: sachlich, Daten belegt

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Zahlungserleichterung nach § 42 StGB

Mein Mandant ist verurteilt zu [X] Tagessaetzen a [Y] EUR,
gesamt [X*Y] EUR Geldstrafe.

Er ist aufgrund [Einkommensverhaeltnisse beschreiben] derzeit nicht in
der Lage, den Gesamtbetrag in einer Summe zu zahlen.

Wir beantragen Ratenzahlung von [RATE] EUR monatlich beginnend
ab [DATUM].

Anlage: Einkommensnachweis / Kontoauszug
```

## Harte Leitplanken

- Tagessatz nie ohne Einkommensnachweis bestimmen — Schaetzung zu Mandantenungunsten moglich.
- Ratenzahlungsantrag fruehzeitig stellen — vor Vollstreckungsbeginn.
- Ersatzfreiheitsstrafe (§ 43 StGB) dem Mandanten klar erklaeren.
- Anwaltliche Endkontrolle bei Berechnungen.

## 3. `strafbefehl-wiedereinsetzung`

**Fokus:** Wiedereinsetzung in den vorigen Stand nach § 44 StPO bei versaeumter Einspruchsfrist. Voraussetzungen: kein Verschulden. Antragsfrist 1 Woche. Glaubhaftmachung § 45 StPO. Zustellungsfiktion entgegnen. Eidesstattliche Versicherung. Wiedereinsetzung und gleichzeitiger Einspruch.

# Wiedereinsetzung nach versaeumter Einspruchsfrist — § 44 StPO

## Triage zu Beginn

1. **Warum wurde die Frist versaeumt?** — Kein Verschulden erforderlich (§ 44 Satz 1 StPO): kein schuldhaftes Versaeumnis des Mandanten oder seines Verteidigers.
2. **Wann wurde die Fristversaeumnis bekannt?** — Antragsfrist: 1 Woche ab Kenntnis des Hindernisses (§ 45 Abs. 1 StPO); nicht ab Zustellungsdatum.
3. **Zustellungsfiktion widerlegen?** — Bei Einwurf-Einschreiben (§ 180 ZPO) gilt Zustellung als bewirkt; Mandant kann spaetere Kenntnisnahme nachweisen.
4. **Verschulden des Verteidigers?** — Anwaltliches Verschulden wird dem Mandanten zugerechnet (§ 44 Satz 2 i.V.m. § 85 ZPO analoge Anwendung); aber: bei Verschulden des Gerichts (fehlerhafte Belehrung) kein Verschulden.
5. **Gleichzeitiger Einspruch:** Wiedereinsetzungsantrag immer mit gleichzeitigem Einspruch verbinden (§ 45 Abs. 2 Satz 2 StPO).

## Zentrale Normen

- **§ 44 StPO** — Wiedereinsetzung in den vorigen Stand: kein Verschulden, Antrag binnen 1 Woche nach Kenntnis
- **§ 45 StPO** — Form und Frist des Wiedereinsetzungsantrags: schriftlich oder protokollarisch, 1-Wochen-Frist
- **§ 45 Abs. 2 Satz 2 StPO** — gleichzeitig mit Antrag muss die versaeumte Handlung (Einspruch) nachgeholt werden
- **§ 46 StPO** — Entscheidung ueber den Antrag; Beschluss
- **§ 180 ZPO** — Zustellungsfiktion bei Einwurf-Einschreiben
- **§ 409 Abs. 1 Nr. 7 StPO** — fehlerhafte Belehrung = Frist laeuft nicht an; kein Wiedereinsetzungsbedarf

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Wiedereinsetzung

```
Einspruchsfrist versaeumt?
├─ Belehrung in Strafbefehl fehlerhaft (§ 409 Abs. 1 Nr. 7)?
│ └─ Frist hat nie begonnen → kein Wiedereinsetzungsbedarf, Einspruch nachholen
├─ Kein Verschulden (§ 44 StPO)?
│ ├─ Krankheit/Unfall des Mandanten → Attest + eidestattliche Versicherung
│ ├─ Urlaub/Abwesenheit → Bescheinigung + eidesstattliche Versicherung
│ ├─ Zustellungsfiktion § 180 ZPO widerlegen (spaetere Kenntnisnahme) → Briefkasten-Nachweis
│ ├─ Kanzleifehler ohne Verschulden → intern klaeren; Mandant haftet nicht fuer Kanzleifehler
│ └─ Gericht hat Frist falsch berechnet → BGH-Rechtsprechung zitieren
└─ Verschulden vorhanden → Wiedereinsetzung abgelehnt; Strafbefehl rechtskraeftig

Wenn Wiedereinsetzung moeglich:
1. Antrag binnen 1 Woche ab Kenntnis (§ 45 Abs. 1 StPO)
2. Gleichzeitig Einspruch einlegen (§ 45 Abs. 2 Satz 2 StPO)
3. Glaubhaftmachung durch eidesstattliche Versicherung
```

## Output-Template Wiedereinsetzungsantrag

**Adressat:** Amtsgericht — Tonfall: sachlich-foermlich, Sachverhalt praezise

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Wiedereinsetzung in den vorigen Stand nach § 44 StPO
sowie Einspruch nach § 410 StPO

Sehr geehrte Damen und Herren,

mein Mandant hat den Strafbefehl vom [DATUM] am [DATUM] erhalten.
Die Einspruchsfrist lief am [DATUM] ab. Die Frist wurde aus
folgendem Grund versaeumt:

[SACHVERHALT: z.B. Mandant war vom [DATUM] bis [DATUM] im
Krankenhaus / im Ausland / postalisch nicht erreichbar; Strafbefehl
wurde am [DATUM] tatsaechlich zur Kenntnis genommen]

Mein Mandant trifft kein Verschulden an der Fristversaeuumnis
(§ 44 Satz 1 StPO). Ich mache dies glaublhaft durch die beigefuegte
eidesstattliche Versicherung meines Mandanten.

Gleichzeitig lege ich namens meines Mandanten

Einspruch

gegen den Strafbefehl vom [DATUM] ein.

Anlage: Eidesstattliche Versicherung des [NAME]

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Wiedereinsetzungsantrag IMMER mit gleichzeitigem Einspruch verbinden.
- Eidesstattliche Versicherung des Mandanten zwingend (§ 45 Abs. 2 StPO: Glaubhaftmachung).
- 1-Wochen-Frist des § 45 StPO ab Kenntnisnahme einhalten.
- Verschulden des Verteidigers wird dem Mandanten zugerechnet — intern aufklaeren, aber Mandanten nicht schlechterstelllen.
