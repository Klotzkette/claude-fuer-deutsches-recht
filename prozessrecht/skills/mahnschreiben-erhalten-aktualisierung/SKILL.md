---
name: mahnschreiben-erhalten-aktualisierung
description: "Mahnschreiben Erhalten Aktualisierung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mahnschreiben Erhalten Aktualisierung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mahnschreiben Erhalten Aktualisierung** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mahnschreiben-erhalten` | Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwortschreiben auf Mahnschreiben. Abgrenzung: nicht Klageverteidigung. |
| `mandat-aktualisierung` | Laufendes Prozessmandat aktualisieren: neue Schriftsaetze, Beschluesse, Fristen eintragen. Normen: §§ 233 ff. ZPO. Prüfraster: Fristverfolgung, Sachstandsaktualisierung, offene Handlungspunkte. Output: Aktualisiertes Mandats-Protokoll. Abgrenzung: nicht Mandatseroffnung. |
| `mandat-aufnahme` | Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse. Output: Mandatsaufnahme-Protokoll. Abgrenzung: nicht inhaltliche Klageschrift. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Mahnschreiben Erhalten Aktualisierung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mahnschreiben-erhalten`

**Fokus:** Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwortschreiben auf Mahnschreiben. Abgrenzung: nicht Klageverteidigung.

# Eingehendes Mahnschreiben / Abmahnung – Triage

## Triage — kläre vor der Auswertung

1. **Schreibentyp:** Einfache Mahnung, Abmahnung (Wettbewerb/Urheberrecht), Forderungsschreiben eines Inkassos oder Klageankündigung?
2. **Frist:** Enthalt das Schreiben eine Zahlungsfrist oder Reaktionsfrist — wann läuft sie ab?
3. **Berechtigung:** Ist die behauptete Forderung dem Grunde und der Höhe nach berechtigt?
4. **Portfolio-Abgleich:** Liegt bereits ein Mandat oder ein Konflikt zu diesem Sachverhalt vor?
5. **Handlungspriorität:** Sofortige Reaktion (Unterlassung, Zahlung, Ablehnung) oder abwarten?

## Zentrale Normen
- § 286 BGB (Verzug durch Mahnung)
- § 203 BGB (Verjährungshemmung durch Verhandlungen)
- § 8 Abs. 1 UWG (Abmahnung im Wettbewerbsrecht)
- § 97a UrhG (Abmahnung im Urheberrecht)
- § 43a Abs. 1 BRAO (Interessenkonflikt bei eingehenden Forderungen)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Strukturierte Auswertung und Triage eingehender Mahnschreiben, Abmahnungen, Forderungsschreiben oder Klagedrohungen. Das Plugin extrahiert relevante Felder, prüft die Berechtigung der Forderung, gleicht mit dem Portfolio offener Mandate ab und erstellt eine priorisierte Handlungsübersicht mit Fristen.

## Eingaben

- Hochgeladenes oder einzufügendes Schreiben (Text, Scan, PDF)
- Optional: `--slug=custom-slug` für eigenes Aktenzeichen

## Ablauf

1. **Feldextraktion:**
 - Absender (Name, Kanzlei, Anschrift)
 - Empfänger (Mandant / Gesellschaft)
 - Datum des Schreibens
 - Aktenzeichen / Referenz des Absenders
 - Art des Schreibens (Mahnung, Abmahnung, Klagedrohung, Aufforderung zur Unterlassung, C&D-Äquivalent)
 - Geldforderung (Betrag, Währung, Fälligkeitsdatum)
 - Anspruchsgrundlage (soweit angegeben)
 - Gesetzte Frist (Datum extrahieren; wenn "2 Wochen ab Zugang" oder ähnlich: Frist anhand des Schreibdatums + Postlaufzeit schätzen)

2. **Portfolio-Abgleich:** Prüfen, ob zu Absender / Sachverhalt bereits ein Mandat in `mandate/_log.yaml` existiert. Wenn ja: Verknüpfung herstellen und History-Update vorschlagen.

3. **Berechtigungsprüfung (Kurzanalyse):**
 - Besteht das behauptete Schuldverhältnis dem Grunde nach?
 - Ist die Forderung bezifferbar und plausibel?
 - Sind Verjährungseinwände (§§ 195, 199 BGB) offensichtlich möglich?
 - Stehen Gegenansprüche (Aufrechnung § 387 BGB, Zurückbehaltungsrecht § 273 BGB) im Raum?
 - Besteht Verdacht auf unberechtigte Abmahnung (§ 8c UWG, § 97a Abs. 4 UrhG)?
 - Ist die Abmahnung formell vollständig (Unterlassungserklärung, Vertragsstrafe, Vollmacht)?

4. **Risikoeinschätzung:** Ampelschema:
 - 🔴 Hohe Berechtigung / akute Frist – sofortiger Handlungsbedarf
 - 🟡 Mittlere Berechtigung / prüfungsbedürftig
 - 🟢 Geringe Berechtigung / defensiv haltbar

5. **Handlungsoptionen mit Empfehlung:**
 - (a) Zahlung / Erfüllung (mit Vorbehalten)
 - (b) Modifizierte Unterlassungserklärung (bei Abmahnung)
 - (c) Abwehr / Zurückweisung mit Begründung
 - (d) Verhandlung / Vergleichsgespräch
 - (e) Schutzschrift hinterlegen (§ 945a ZPO) bei Gefahr einstweiliger Verfügung
 - (f) Mandat-Intake → neues Mandat anlegen

6. **Fristen-Alarm:**
 - Antwortfrist aus Schreiben extrahieren und als absolute Frist eintragen
 - Verjährungshemmung durch Verhandlung (§ 203 BGB) oder Mahnbescheid (§ 204 Abs. 1 Nr. 3 BGB) als Optionen nennen

7. **Datei speichern:** `inbound/[JJJJ-MM-TT]-[slug].md`

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8c Rn. 5 ff. (missbräuchliche Abmahnung).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

```
EINGEHENDES SCHREIBEN – TRIAGE-BERICHT
Slug: [automatisch generiert]
Datum Eingang: TT.MM.JJJJ
Absender: [Kanzlei / Gläubiger]
Art: [Mahnung | Abmahnung | Klagedrohung]

──────────────────────────────────────
KERNFELDER
──────────────────────────────────────
Forderungsbetrag: EUR X.XXX,XX
Anspruchsgrundlage: § 280 Abs. 1, 3, § 281 BGB
Frist gesetzt bis: TT.MM.JJJJ
Konsequenz: Klageandrohung

──────────────────────────────────────
RISIKOEINSCHÄTZUNG: 🟡 MITTEL
──────────────────────────────────────
Begründung: Forderung dem Grunde nach plausibel;
Zugang der Fristsetzung unklar; Verjährung prüfen.

──────────────────────────────────────
HANDLUNGSOPTIONEN
──────────────────────────────────────
Empfehlung: (c) Abwehr – fehlender Verjährungsverzicht
Alternativen: (d) Verhandlung, (e) Schutzschrift

──────────────────────────────────────
FRISTEN
──────────────────────────────────────
⚠️ Antwortfrist: TT.MM.JJJJ
📅 Verjährungsende: 31.12.JJJJ (§§ 195, 199 BGB)
```

## Risiken / typische Fehler

- **Fristüberschreitung:** Bei Abmahnungen im UWG/UrhG ist die Frist oft sehr kurz (3–10 Tage); plug-in markiert Schreiben mit kurzem Frist-Alert.
- **Schutzschrift vergessen:** Bei drohender einstweiliger Verfügung (z. B. Wettbewerbsrecht, Markenrecht) sofortige Schutzschrift-Hinterlegung im Zentralen Schutzschriftenregister (ZSSR, § 945a ZPO) erwägen.
- **Kostenfalle § 93 ZPO:** Wenn Berechtigung klar, Zahlung / Unterlassungserklärung vor Klagezustellung prüfen; sonst trägt Beklagter Kosten trotz sofortigem Anerkenntnis.
- **Unvollständige Vollmacht:** Abmahnung ohne beigefügte Vollmacht ist zurückweisbar (§ 174 BGB); Zurückweisung unverzüglich erklären.

## 2. `mandat-aktualisierung`

**Fokus:** Laufendes Prozessmandat aktualisieren: neue Schriftsaetze, Beschluesse, Fristen eintragen. Normen: §§ 233 ff. ZPO. Prüfraster: Fristverfolgung, Sachstandsaktualisierung, offene Handlungspunkte. Output: Aktualisiertes Mandats-Protokoll. Abgrenzung: nicht Mandatseroffnung.

# Mandats-Aktualisierung

## Zweck

Ein Prozessportfolio bleibt nur dann nützlich, wenn es aktuell ist. Dieser Skill macht das Einpflegen einer Entwicklung effizient — strukturiertes Erfassen in wenigen Minuten, ohne freien Textdrift. Lädt bei jeder Anfrage, einen neuen Vorgang in ein laufendes Prozessmandat einzutragen.

## Eingaben

- **Mandatsbezeichnung (Slug)** (erforderlich): Kurzbezeichnung des Mandats. Falls nicht angegeben, wird eine Liste zuletzt aktualisierter Mandate zur Auswahl angeboten.
- **Ereignistyp**: Auswahl aus Kategorien oder Freitext.
- **Datum**: Standardmäßig heute; kann für rückwirkende Einträge überschrieben werden.
- **Zusammenfassung**: Ein kurzer Absatz — was ist passiert, was bedeutet es, welche unmittelbaren Folgen hat es.
- **Feldupdates** (soweit durch das Ereignis berührt): Status, Verfahrensstadium, Risikoeinstufung, Wesentlichkeit, Streitwert/Exposure, nächste Frist, externe Bevollmächtigte, interne Verantwortliche.

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 214–229 ZPO** — Fristen, Versäumnis, Wiedereinsetzung; zentral für die Fristenkontrolle im Prozessmandat.
- **§§ 516, 548, 569 ZPO** — Berufungs-, Revisions- und Beschwerdebegründungsfristen (Monats- bzw. Zwei-Monats-Fristen nach Zustellung); jede Fristverlängerung ist einzutragen.
- **§ 116 VwGO** — Zustellung und Fristen im Verwaltungsgerichtsverfahren.
- **§§ 317–329 StPO** — Rechtsmittelfristen im Strafverfahren (Berufungsfrist: eine Woche ab Urteilsverkündung, § 317 StPO).
- **§ 43a Abs. 1, 4 BRAO** — Sachkundige, gewissenhafte Berufsausübung; Pflicht zur lückenlosen Aktenführung als Berufspflicht.
- **§ 11 BORA** — Sorgfaltspflicht bei Fristnotierung und Aktenführung.
- **§§ 257, 261 HGB; § 147 AO** — Aufbewahrungspflichten für Handels- und Steuerunterlagen (6–10 Jahre); relevant für den Beweissicherungsaspekt.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 0: Konfliktsschranke

Vor dem Einpflegen eines Eintrags wird geprüft, ob das Mandat in `_log.yaml` enthalten ist. Fehlt es:

> "Das Mandat [Bezeichnung] ist nicht im Mandatsprotokoll erfasst. Bitte zunächst `/prozessrecht:mandat-aufnahme` ausführen, damit die Interessenkonfliktprüfung erfolgt und die Mandatsakte angelegt wird."

### Schritt 1: Ereignistyp

Angebotene Kategorien:

- **Verfahrensrechtlich** — Schriftsatz eingereicht/erhalten, Beschluss ergangen, Termin stattgefunden, Frist gesetzt
- **Beweiserhebung** — Urkunden vorgelegt/erhalten, Zeugenvernehmung, § 142 ZPO-Anordnung
- **Sachlich** — neue Tatsachen, relevantes Dokument aufgetaucht, Entscheidung zur Sache
- **Strategie** — Positionswechsel, Vergleichsangebot gemacht/erhalten, Änderung der Vergleichskompetenz
- **Risikoneubewertung** — Schwere oder Wahrscheinlichkeit hat sich geändert
- **Beteiligte** — Neue Person einbezogen, Wechsel der externen Bevollmächtigten
- **Administrativ** — Mandatsvertrag geschlossen, Budget angepasst, Beweissicherungsanordnung erneuert

Freitext möglich, wenn keine Kategorie passt.

### Schritt 2: Datum

Standard: heute. Überschreibung möglich (z. B. für die Nacherfassung eines Ereignisses der letzten Woche).

### Schritt 3: Zusammenfassung

Ein Absatz: Was ist passiert, was bedeutet es, welche unmittelbaren Folgen sind erkennbar.

### Schritt 4: Protokollfelder aktualisieren

Nur die durch das Ereignis betroffenen Felder werden abgefragt:

- `status:` — Hat sich das Stadium verschoben (z. B. Klageerhebung → Beweisaufnahme)?
- `verfahrensstadium:` — Detailangabe zum Unterstand
- `risiko:` — Neubewertung erforderlich?
- `wesentlichkeit:` — Änderung? (neue Tatsachen können Rückstellungs- oder Offenlegungspflicht auslösen)
- `streitwert_exposure:` — Anpassen bei neuen Erkenntnissen
- `nächste_frist:` — Neues kommendes Datum, falls bekannt
- `externe_bevollmaechtigte:` — Wechsel?
- `interne_verantwortliche:` — Neu oder ausgeschieden?
- `beweissicherung:` — Erneuert, erweitert, aufgehoben?

Verfahrensrechtliche Updates berühren in der Regel nur `verfahrensstadium` und `nächste_frist`; ein Vergleichsangebot kann `wesentlichkeit`, `streitwert_exposure` und `status` berühren.

### Schritt 4a: Vergleichsannahmeschranke

Handelt es sich um eine **Vergleichsannahme** (die Partei nimmt ein Vergleichsangebot an, unterzeichnet einen Vergleich oder erteilt grundsätzlich Vollmacht zur Annahme — nicht bloßes Erfassen eines Angebots oder Gegenentwurfs):

> Ein Vergleich hat endgültige Rechtswirkungen — er beseitigt den Klagegegenstand, erfordert typischerweise eine gegenseitige Erlassklausel und kann steuerliche sowie versicherungsrechtliche Folgen haben. Wurde dies mit einem Anwalt besprochen? Falls ja: bitte bestätigen. Falls nein, hier ist ein Briefing für das Gespräch:
>
> [Zusammenfassung: Mandat, Vergleichskonditionen (Betrag, Struktur, Erlassumfang, Vertraulichkeit), gefährdetes Interesse, Stand der Vergleichskompetenz, Risiken, Fragen an den Anwalt.]

Ohne ausdrückliche Bestätigung wird die Annahme nicht eingetragen und die Wesentlichkeit nicht auf Vergleichsbasis umklassifiziert.

### Schritt 4b: Wesentlichkeitsprüfung

Bei bestimmten Ereignistypen ist eine Wesentlichkeitsprüfung obligatorisch — der Nutzer muss explizit antworten:

| Ereignistyp | Hinweistext |
|---|---|
| Sachlich (neue Tatsachen, relevantes Dokument, Entscheidung zur Sache) | "Dieses Ereignis ist sachlicher Natur. Ändert es die Wesentlichkeitseinstufung? Aktuell: [X]. Optionen: rückgestellt / offengelegt / beobachtet / keine. Änderung?" |
| Strategie (Positionswechsel, Vergleichsangebot gemacht oder erhalten) | "Vergleichsaktivität kann eine Wesentlichkeitsumstufung auslösen. Aktuell: [X]. Wenn das Angebot die Exposure verschiebt oder den Streit von 'bestritten' auf 'wahrscheinlich und schätzbar' bewegt, bitte umklassifizieren." |
| Risikoneubewertung | "Risiko hat sich verändert. Die Wesentlichkeit sollte folgen. Aktuell: [X]. Umklassifizieren?" |
| Behördliche Maßnahme | "Behördenhandeln (Durchsuchung, Vorladung, Ordnungsverfügung) löst regelmäßig eine Offenlegungsanalyse aus. Aktuell: [X]. Änderung?" |

"Keine Änderung" muss explizit bestätigt werden. Im Verlaufseintrag wird festgehalten:

```markdown
**Wesentlichkeitsprüfung:** [keine Änderung / geändert von X nach Y]
**Begründung:** [ein Satz]
```

### Schritt 5: Belegdokument (optional)

Falls das Update ein Dokument betrifft (Beschluss, Schriftsatz, Korrespondenz), wird gefragt, ob ein Pfad verlinkt werden soll.

## Ausgabeformat

### Verlaufseintrag in `verlauf.md`

Jüngster Eintrag oben, direkt unter dem `---` nach dem Header:

```markdown
## [JJJJ-MM-TT] — [Ereignistyp]: [Kurztitel]

[Zusammenfassung in einem Absatz.]

**Geänderte Felder:**
- [Feld]: [alt → neu]
- [Feld]: [alt → neu]

**Verweisung Dokument:** [Pfad, falls angegeben]
```

Falls keine Felder geändert wurden, entfällt der Block "Geänderte Felder".

### Protokolldatei `_log.yaml`

- Geänderte Felder werden übernommen.
- `zuletzt_aktualisiert:` wird auf heute gesetzt (oder das Ereignisdatum, falls überschrieben).

### Bestätigung vor dem Speichern

Der Verlaufseintrag und die Yaml-Diff werden dem Nutzer zur Freigabe vorgelegt:

> "Das ist, was ich eintragen und aktualisieren werde. Soll ich das festschreiben?"

## Beispiel

**Sachverhalt:** Im Verfahren Müller ./. Beta GmbH (ZPO-Berufungsverfahren, OLG Frankfurt) ist am 12.05.2025 die Berufungsbegründungsfrist abgelaufen. Die Begründung wurde fristgerecht eingereicht. Keine Risikoänderung.

**Eintrag:**

```markdown
## [2025-05-12] — Verfahrensrechtlich: Berufungsbegründung eingereicht

Berufungsbegründung fristgerecht beim OLG Frankfurt eingereicht (§ 520 Abs. 2 ZPO). Keine inhaltlichen Änderungen zur bisherigen Positionierung. Nächster Termin: Eingang der Berufungserwiderung der Gegenseite erwartet bis 12.07.2025.

**Geänderte Felder:**
- naechste_frist: 2025-07-12
- verfahrensstadium: Berufungsbegründung eingereicht → Berufungserwiderung ausstehend

**Wesentlichkeitsprüfung:** keine Änderung
**Begründung:** Verfahrensrechtlicher Schritt ohne neue Tatsachen oder Risikoverschiebung.
```

## Risiken und typische Fehler

- **Fristversäumnis durch verzögerten Eintrag:** Der Eintrag ersetzt kein Fristenkontrollsystem; die Kanzlei muss separate Fristenkalender nach § 11 BORA führen. Dieser Skill dokumentiert — er sichert keine Fristen.
- **Stillschweigendes Wesentlichkeitsupdating:** Unterbleibt die explizite Wesentlichkeitsprüfung, kann eine Rückstellungspflicht oder eine kapitalmarktrechtliche Offenlegungspflicht übersehen werden.
- **Einträge in nicht-aufgenommene Mandate:** Ohne vorherige Interessenkonfliktprüfung (`/prozessrecht:mandat-aufnahme`) werden keine Einträge angelegt.
- **Vergleichsannahme ohne anwaltliche Prüfung:** Die Schranke ist unüberwindbar für Nicht-Juristen; nur ein explizites Ja entsperrt den Eintrag.
- **Rückwirkende Einträge:** Das Datum kann überschrieben werden; `zuletzt_aktualisiert` in `_log.yaml` zeigt jedoch immer das Bearbeitungsdatum, nicht das Ereignisdatum.
- **Korrekturen:** Vergangene Einträge werden nicht bearbeitet. Korrekturen erfolgen als neuer Eintrag mit Verweis auf den zu korrigierenden Eintrag.

## Quellenpflicht

In der Verlaufsakte und bei Wesentlichkeitsprüfungen sind folgende Quellen heranzuziehen und, soweit angegeben, zu zitieren:

- Gesetzestexte: §§ 214 ff., 516, 520, 548, 569 ZPO; §§ 317 ff. StPO; § 116 VwGO; § 43a BRAO; § 11 BORA
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 3. `mandat-aufnahme`

**Fokus:** Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse. Output: Mandatsaufnahme-Protokoll. Abgrenzung: nicht inhaltliche Klageschrift.

# Mandat-Intake

## Triage — kläre vor der Aufnahme

1. **Mandatstyp:** Klägerseite, Beklagtenseite, Beratungsmandat oder gemischtes Mandat?
2. **Interessenkonflikt:** Besteht ein Interessenkonflikt mit laufenden oder abgeschlossenen Mandaten (§ 43a Abs. 4 BRAO, § 3 BORA)?
3. **Verfahrensart:** Zivilverfahren, arbeitsgerichtliches Verfahren, Verwaltungsverfahren, Strafverfahren?
4. **Schlüsselfristen:** Gibt es laufende Fristen (Verjährung, Rechtsmittelfrist, Klagefrist) die sofort gesichert werden müssen?
5. **Außenmandat:** Wird ein Korrespondenzanwalt oder Fachanwalt benötigt?

## Zentrale Normen
- § 43a Abs. 4 BRAO (Interessenkonflikt — Vertretungsverbot)
- § 3 BORA (Interessenkonflikt — weitere Fallgruppen)
- § 49b BRAO (Vergütungsvereinbarung)
- § 204 BGB (Verjährungshemmung durch Klage)
- § 232 ff. ZPO (Fristen und Fristenberechnung)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Vollständige und strukturierte Aufnahme eines neuen Mandats in das Portfolio. Der Skill führt ein interaktives Interview und schreibt die Ergebnisse in `mandate/[slug]/mandat.md` (Stammdaten), `mandate/[slug]/verlauf.md` (Erstem Eintrag) und hängt eine Zeile an `mandate/_log.yaml` an.

## Eingaben

- Optional: Name oder Kurzbezeichnung des Mandats
- Hochgeladene Dokumente (z. B. Klageschrift, Abmahnung, Bescheid, Vertrag)

## Ablauf

### 1. Identifikation und Aktenzeichen

- Kanzlei-Aktenzeichen und interner Slug (URL-freundlich, z. B. `mueller-gmbh-werkvertrag-2024`)
- Mandantenname (juristische oder natürliche Person), Kontaktperson
- Mandantentyp: Unternehmer (§ 14 BGB) / Verbraucher (§ 13 BGB)
- Gegenseite: Vollständiger Name, Anschrift, Verfahrensbevollmächtigter (wenn bekannt)
- Mandats-Art: Klage / Verteidigung / Beratung / Rechtsmittel / Vollstreckung

### 2. Interessenkonflikt-Check (§ 43a Abs. 4 BRAO, § 3 BORA)

- Vertritt die Kanzlei bereits die Gegenseite in irgendeinem Mandat?
- Ist ein Anwalt der Kanzlei früher für die Gegenseite tätig gewesen?
- Bestehen sonstige Interessenkonflikte (persönliche Beziehungen, Eigeninteresse)?
- **Bei positivem Befund:** Mandat ablehnen oder um Einverständnis einholen; Plugin erstellt Interessenkonflikt-Vermerk.

### 3. Sachverhaltserfassung

- Kurzbeschreibung des Sachverhalts (wer, was, wann, wie viel?)
- Anspruchsgrundlage (vorläufig, z. B. § 280 BGB, § 823 BGB, § 1 UWG)
- Rechtliches Kernproblem (streitige Tat- oder Rechtsfrage)
- Vorhandene Dokumente: Liste und Anlage-Nummern

### 4. Verfahrensart und Zuständigkeit

- Verfahrensordnung: ZPO / ArbGG / VwGO / FGO / SGG / FamFG / StPO
- Sachlich zuständiges Gericht: AG (§§ 23 ff. GVG), LG (§§ 71 ff. GVG), Spezialgerichte (ArbG, VG, FG, SG)
- Örtliche Zuständigkeit: allgemeiner Gerichtsstand (§§ 12, 13 ZPO), besonderer Gerichtsstand (§ 29 ZPO: Erfüllungsort), ausschließlicher Gerichtsstand (§ 29a ZPO: Miete)
- Streitwert (vorläufig, nach GKG/RVG)

### 5. Risikotriage

- Erfolgsaussichten: stark / mittel / schwach (mit Kurzbereg)
- Worst-Case-Szenario (maximale Exposition inkl. Kosten § 91 ZPO)
- Wichtig: Prozesskostenrisiko nach § 91 ZPO; ggf. Rechtsschutzversicherung vorhanden?
- Verjährungsrisiko prüfen: Restlaufzeit (§§ 195, 199 BGB)

### 6. Außenanwalt / Korrespondenzanwalt

- Wird die Sache vollständig intern geführt oder von externer Kanzlei?
- Externer Anwalt: Name, Kanzlei, Kontakt
- Reporting-Intervall an Mandanten

### 7. Beweissicherung

- Ist sofortige Beweissicherung erforderlich? (z. B. Baumangel, drohende Sachzustandsveränderung)
- Aufbewahrungsanordnung erstellen? → Weiterleitung an Skill `beweissicherung`

### 8. Schlüsselfristen

- Klagefrist / Antwortfrist
- Verjährungsablauf
- Nächste Prozesshandlung

### 9. mandat.md und verlauf.md schreiben

```yaml
# mandat.md
slug: ""
kanzlei_az: ""
mandant:
 name: ""
 typ: "Unternehmer / Verbraucher"
gegenseite:
 name: ""
 anwalt: ""
verfahren:
 art: ""
 gericht: ""
 az_gericht: ""
 verfahrensordnung: ""
streitwert: 0
anspruchsgrundlage: ""
risiko: "hoch / mittel / gering"
exposition_max: 0
verjaehrung: ""
aussenanwalt: ""
status: "aktiv"
beweissicherung: false
angelegt: "TT.MM.JJJJ"
naechste_frist: "TT.MM.JJJJ"
```

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BRAO § 43a Abs. 4 (Interessenkonflikt: Verbot der Vertretung widerstreitender Interessen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

Interaktiver Dialog, dann automatisches Schreiben von `mandat.md`, `verlauf.md` (erster Eintrag: "Mandat aufgenommen, TT.MM.JJJJ") und Append in `_log.yaml`.

## Risiken / typische Fehler

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Verjährung nicht geprüft:** Vor Intake stets Verjährungsablauf ermitteln; läuft die Verjährung in < 3 Monaten, sofort Hemmungsmaßnahmen (§ 204 BGB: Klageerhebung, Mahnbescheid) einleiten.
- **Zuständigkeit falsch:** Fehlerhafte sachliche Zuständigkeit führt zur Verweisung (§ 281 ZPO) und Zeitverlust; Streitwertgrenzen (AG: bis EUR 10.000; LG: über EUR 10.000, § 23 Nr. 1 GVG i. d. F. seit 1.1.2026) prüfen.
- **Mandant ist Verbraucher – besondere Pflichten:** Informationspflichten nach § 43d BRAO (Kostenmitteilung), § 13 RVG (Vergütungsvereinbarung).
