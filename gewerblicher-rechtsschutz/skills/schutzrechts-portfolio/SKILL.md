---
name: schutzrechts-portfolio
description: >
  Verwaltung des IP-Portfolios — Eintragungen, Verlängerungen, Jahresgebühren
  und Benutzungsnachweise. Lädt bei der Prüfung anstehender Fristen, dem
  Hinzufügen oder Aktualisieren eines Schutzrechts, der Erfassung einer
  Amtshandlung oder einer Portfolio-Überprüfung auf Lücken, Verfall und
  Benutzungsfragen.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - IP-Portfolio Fristen
  - Marke verlängern
  - Patentjahresgebühr
  - Schutzrechtsverwaltung
  - Portfolioübersicht
  - Markenverlängerung MarkenG
  - Patent Aufrechterhaltungsgebühr
  - DesignG Verlängerung
  - IP-Register
---

# IP-Portfolio-Verwaltung

## Zweck

Diese Skill zeigt anstehende Fristen, fügt Schutzrechte hinzu, erfasst Amtshandlungen und prüft das Register auf Gesundheit. Eine Marke, die nicht rechtzeitig verlängert wird, kann gelöscht werden. Ein Patent ohne gezahlte Jahresgebühr erlischt. Eine Domain, die abläuft, kann innerhalb von Stunden registriert werden. All das ist vermeidbar — und hängt davon ab, dass die richtige Frist der richtigen Eintragungsnummer in der richtigen Behörde zugeordnet ist.

Diese Skill reicht keine Anträge ein. Jede aufgezeigte Handlung ist vom Patentanwalt, Rechtsanwalt oder dem beauftragten Korrespondenzanwalt auszuführen.

Hinweis: Berechnete Fristen sind Referenzwerte. Jede Frist ist vor Handlung gegen DPMA DPMAdirektplus / PatReg, EUIPO eSearch, WIPO Madrid Monitor / Patentscope oder das jeweilige nationale Register zu verifizieren.

## Eingaben

Befehlsargument:

- `--bericht [--tage N]` — Fristen im Berichtsfenster (Standard: 90 Tage)
- `--hinzufuegen` — neues Schutzrecht interaktiv erfassen
- `--aktualisieren` — Amtshandlung, Gebührenzahlung oder Statusänderung erfassen
- `--pruefung` — umfassende Portfolioprüfung
- (kein Argument) — entspricht `--bericht`

## Rechtlicher Rahmen

### Kernvorschriften — Fristen und Verlängerungen

**Marken:**
- **§ 47 Abs. 1 MarkenG** — Schutzdauer: 10 Jahre ab Anmeldetag, danach jeweils weitere 10 Jahre
- **§ 47 Abs. 3 MarkenG** — Verlängerung durch Zahlung der Verlängerungsgebühr; Schonfrist 6 Monate mit Zuschlag (§ 7 PatKostG)
- **Art. 53 UMV (Unionsmarkenverordnung EU 2017/1001)** — Schutzdauer Unionsmarke 10 Jahre; Verlängerung beim EUIPO
- **Art. 7 MMA / Regel 30 GAFO** — Madrid-System: 10-jährige internationale Registrierung; Verlängerung beim WIPO; individuelle Wirkungsländer-Fristen beachten
- **§ 26 MarkenG** — Benutzungszwang; nach 5 Jahren Löschungsrisiko bei ernsthafter Nichtbenutzung (§ 49 MarkenG)

**Patente:**
- **§ 17 PatG** — Patentlaufzeit: 20 Jahre ab Anmeldetag; Aufrechterhaltung durch jährliche Jahresgebühren (§ 17 Abs. 1 i. V. m. PatKostG Anlage)
- **§ 20 Abs. 1 Nr. 3 PatG** — Erlöschen bei Nichtzahlung der Jahresgebühr
- **§ 17 Abs. 2 PatG** — Schonfrist: 6 Monate mit Zuschlag
- **Regel 51 EPÜ / Art. 86 EPÜ** — EP-Patent: Jahresgebühren beim nationalen Amt ab dem 3. Jahr nach Anmeldetag; Nationalisierung innerhalb von 31 Monaten (PCT)
- **§ 13 GebrMG** — Gebrauchsmuster: Schutzdauer 3 Jahre ab Anmeldetag, verlängerbar auf max. 10 Jahre (je +3/+2 Jahre)

**Designs:**
- **§ 27 DesignG** — Schutzdauer: 5 Jahre ab Anmeldetag, verlängerbar bis max. 25 Jahre in 5-Jahres-Schritten
- **Art. 12 GGV (Gemeinschaftsgeschmacksverordnung EU 6/2002)** — Eingetragenes Gemeinschaftsgeschmacksmuster (EGGM): 5 Jahre ab Anmeldedatum, verlängerbar bis max. 25 Jahre

**Urheberrecht:**
- **§ 64 UrhG** — Schutzfrist: 70 Jahre nach Tod des Urhebers; keine aktive Verlängerung erforderlich
- **§§ 70–72 UrhG** — Verwandte Schutzrechte: abweichende Fristen

### Leitentscheidungen

- BGH, Urt. v. 10.01.2008 – I ZR 38/05, GRUR 2008, 616 (Schmuck) — Löschungsklage wegen Nichtbenutzung (§ 49 MarkenG); Maßstab ernsthafte Benutzung; relevanter Zeitraum
- BGH, Urt. v. 17.08.2011 – I ZB 59/10, GRUR 2012, 180 (Lernfox) — Verlängerung der Markenschutzfrist; maßgeblicher Zeitpunkt der Zahlung

### Kommentare

- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 47 Rn. 1 ff. (Schutzdauer und Verlängerung), § 49 Rn. 1 ff. (Löschung wegen Nichtbenutzung)
- Benkard/Rogge, PatG, 12. Aufl. 2023, § 17 Rn. 1 ff. (Laufzeit und Jahresgebühren)
- Eichmann/Jestaedt/Fink/Meiser, DesignG, 6. Aufl. 2019, § 27 Rn. 1 ff. (Schutzdauer und Verlängerung)

## Ablauf

### Modus 1: Initialisierung (bei leerem Register oder `--neu`)

1. Quelle bestimmen: IP-Verwaltungssystem angebunden (Anaqua, Dennemeyer, Patronas, CPA Global)? Falls ja: Portfolio über Integration beziehen. Falls nein: Tabelle / Export anfordern oder interaktiv durchführen.
2. Für jedes Schutzrecht Fristen berechnen (Regeln unten). `naechste_fristen` mit den zwei bis drei nächsten Fälligkeiten befüllen.
3. Register schreiben. Zusammenfassung ausgeben:

```
Portfolio-Register initialisiert.

Schutzrechte: [N]
  Marken: [N]   ([N eingetragen] / [N angemeldet])
  Patente: [N]  ([N erteilt] / [N angemeldet])
  Designs: [N]
  Domains: [N]

Fristen berechnet: [N]
Anwaltlich verwaltet / Zuständigkeit TBD: [N] — mit Korrespondenzanwalt bestätigen
Unbekannt (Daten fehlen): [N] — vor Verlassen auf Berichte ergänzen

`--bericht` ausführen für Übersicht.
```

### Modus 2: Bericht (`--bericht [--tage N]`)

Standard: 90 Tage. Berechnete Fristen vor Berichtserstellung für jedes Schutzrecht aktualisieren.

Ausgabe (Arbeitsergebnis-Kopfzeile voranstellen):

```
IP-PORTFOLIO-FRISTENBERICHT — [Datum]
[Unternehmensname] — Fenster: nächste [N] Tage

🔴 ERLOSCHEN / IN SCHONFRIST ([N])
  [ID] / [Behörde] / [Typ] / [Bezeichnung]
    [Handlung] — ursprünglich fällig [Datum], Schonfrist endet [Datum]
    Status: [schonfrist / erloschen]

⏰ FÄLLIG INNERHALB [N] TAGE ([N])
  [ID] / [Behörde] / [Typ] / [Bezeichnung]
    [Handlung] — fällig [Datum]
    Grundlage: [z. B. „10. Jahrestag der Anmeldung, § 47 Abs. 1 MarkenG"]
    [Anwalt: Kanzlei / Aktenzeichen — falls vorhanden]

🟡 BEVORSTEHEND (über 30 Tage, innerhalb [N] Tage)
  [Liste]

🌐 ANWALTLICH VERWALTET ([N])
  [ID] / [Behörde] — verwaltet von [Korrespondenzanwalt]; direkt bestätigen
  [ID] / [Behörde] — kein Korrespondenzanwalt eingetragen; mit --aktualisieren ergänzen

❓ UNBEKANNT ([N])
  [ID] — fehlendes [Feld]; Frist nicht berechenbar
  Vor Verlassen auf diesen Bericht mit [DPMA / EUIPO / WIPO] abgleichen.

ZUSAMMENFASSUNG
  Schutzrechte gesamt: [N]
  Fristen im Fenster: [N]
  Letzte Portfolioprüfung: [Datum]
```

Schlusssatz: *„Aus Portfolio-Register berechnet. Jede Frist vor Handlung gegen DPMA DPMAdirektplus, EUIPO eSearch, WIPO Madrid Monitor oder das jeweilige Behördenregister verifizieren."*

### Modus 3: Hinzufügen (`--hinzufuegen`)

Interaktive Erfassung eines neuen Schutzrechts. Abfragen:

1. Typ (Marke / Patent / Gebrauchsmuster / Design / Urheberrecht / Domain)
2. Behörde / Jurisdiktion (DPMA, EUIPO, WIPO Madrid, EPO, national)
3. Bezeichnung / Erfindungstitel
4. Inhaber (eingetragene Rechtsperson — relevant für Validitätsprüfungen und Zuordnung)
5. Schlüsseldaten (je nach Typ: Anmelde-, Eintragungstag, Erteilungstag, Prioritätstag, Ablaufdatum)
6. Aktenzeichen(n)
7. Klassen / Ansprüche (Nizza-Klassen für Marken; IPC/CPC für Patente)
8. Quelle — wird im IP-Verwaltungssystem unter einer Aktennummer geführt?
9. Externer Patentanwalt / Korrespondenzanwalt falls vorhanden
10. Fachbereich-Zuständiger im Unternehmen

Nach Erfassung: Fristen nach den Regeln oben berechnen. Falls Jurisdiktion nicht eingebaut: `eigene_regeln`-Flow (unten).

**Eigene Regeln für unbekannte Jurisdiktionen:**

> Für [Jurisdiktion] / [Typ] sind die Aufrechterhaltungsregeln nicht eingebaut. Bitte angeben:
>
> 1. Welche Ereignisse sind fristen-relevant? (Verlängerung alle N Jahre? Jahresgebühren jährlich? Benutzungsnachweise? Sonstiges?)
> 2. Was löst das Fälligkeitsdatum aus — Anmelde-, Eintragungstag, nationaler Phase-Eintritt, etwas anderes?
> 3. Gibt es eine Schonfrist? Mit welchem Zuschlag?
> 4. Verwaltet ein Korrespondenzanwalt dieses Schutzrecht?

Unter `eigene_regeln:` speichern; auf zukünftige Schutzrechte dieser Jurisdiktion anwenden.

### Modus 4: Aktualisieren (`--aktualisieren`)

**Entscheidungs-Gate vor Statusänderung:** Bevor eine Amtshandlung oder Gebührenzahlung als „eingereicht" erfasst wird — falls der Nutzer kein Rechtsanwalt ist:

> Das Erfassen einer Marken­verlängerung, Jahresgebühr oder Gebrauchsmuster­verlängerung als „eingereicht" hat Konsequenzen. Wenn die Erfassung falsch ist — versäumtes Fristdatum, falsche Gebührenhöhe, fehlender Nachweis — verschiebt sich die Frist nicht und das Schutzrecht kann erlöschen. Haben Sie die Handlung mit dem zuständigen Patentanwalt oder Korrespondenzanwalt bestätigt (oder über DPMA DPMAdirektplus / EUIPO / WIPO überprüft)? Wenn ja: weiter. Wenn nein:
>
> - Noch nicht als eingereicht erfassen.
> - Folgendes zum Anwalt/Korrespondenzanwalt: Schutzrechts-ID, Behörde, Fristtyp, was das IP-Verwaltungssystem zeigt, was Ihrer Überzeugung nach eingereicht wurde und wann, und die Quelle dieser Überzeugung.

Kein `status: eingereicht` ohne ausdrückliches Ja über dieses Gate.

**Teilmodi:**

- **Manuelle Aktualisierung:** „Wir haben die Verlängerung von TM-DPMA-001 am 3. Juli eingereicht, Nachweis beigefügt." → Entsprechende Frist auf `status: eingereicht`, `eingereichtes_datum` setzen; nächste Frist im Lebenszyklus berechnen.
- **Statusänderung:** „Bitte TM-EUIPO-004 als aufgegeben markieren." → `status` aktualisieren, `naechste_fristen` leeren, Datum notieren.
- **IP-System-Abgleich:** Falls Anaqua / Dennemeyer / CPA Global angebunden: aktuellen Datenstand ziehen, abgleichen. Abweichungen kennzeichnen — System of Record gewinnt.

### Modus 5: Portfolioprüfung (`--pruefung`)

Umfassende Gesundheitsprüfung über die nächsten Monatsfristen hinaus:

**Fristenhygiene**
- Fristen derzeit in `schonfrist`-Status? (Handlung möglich, aber Zuschlag anfallend.)
- Erloschenene Schutzrechte, die nicht als aufgegeben / gelöscht markiert sind? Entweder wiederbeleben oder Status aktualisieren.
- Schutzrechte ohne berechnete `naechste_fristen`? Fehlende Daten oder unbekannte Jurisdiktion.

**Eintragungslücken**
- Markenanmeldungen älter als 18 Monate noch `angemeldet`? Amtsstatus prüfen — ggf. Beanstandungen zu beantworten.
- Patentanmeldungen älter als 4 Jahre noch `angemeldet`? Prüfungsstand prüfen.

**Benutzung (Marken)**
- §-49-MarkenG-Risiko: Marken, deren Verlängerung näher rückt und für die `benutzung_nachgewiesen: false` oder unklar? Die Verlängerung erfordert keine Benutzungsnachweise, aber der Löschungsanspruch Dritter entsteht nach 5 Jahren ernsthafter Nichtbenutzung. Benutzungsaudit vor Verlängerungsentscheidung empfehlen.

**Inhaberhygiene**
- Schutzrechte, bei denen `inhaber` keine aktive Gesellschaft ist (Umfirmierung, Verschmelzung, Spaltung)? Ggf. Umschreibung beim Amt (§ 28 MarkenG; § 30 PatG) erforderlich.
- Inhaberbezeichnungen inkonsistent über Schutzrechte hinweg? Für Bereinigung kennzeichnen.

**Ablaufhorizont (24 Monate)**
- Patente, die in 24 Monaten auslaufen? Auch ohne Jahresgebühr-Frist geschäftsrelevant — Produktplanung, Fortsetzungsstrategie, Lizenzierungsfenster.

**Nicht überwachte Schutzrechte**
- Eingetragene Marken, die nicht im Watch-Service des Mandatsprofils aufgeführt sind? Als Lücke für anwaltliche Entscheidung markieren.

Ausgabeformat:

```
IP-PORTFOLIOPRÜFUNG — [Datum]

FRISTENHYGIENE
  In Schonfrist: [N] — sofortige Handlung vermeidet Erlöschen
  Erloschen (nicht als aufgegeben markiert): [N] — Status bestätigen
  Fehlende Fristenberechnung: [N] — Daten ergänzen oder anwaltlich verwalten markieren

EINTRAGUNGSLÜCKEN
  Markenanmeldungen > 18 Monate anhängig: [Liste]
  Patentanmeldungen > 4 Jahre anhängig: [Liste]

BENUTZUNG (MARKEN)
  § 49 MarkenG — Löschungsrisiko bei anhängenden Verlängerungen und unklarer Benutzung: [Liste]

INHABER
  Schutzrechte mit nicht aktiver/unklarer Inhaberbezeichnung: [N]
  Inhaber-Bezeichnungsinkonsistenzen: [Liste]

ABLAUFHORIZONT (24 MONATE)
  Ablaufende Patente: [Liste]

MARKEN-WATCH
  Eingetragene Marken nicht im Watch-Service: [Liste]

EMPFOHLENE MASSNAHMEN
  1. [höchste Priorität]
  2. [etc.]
```

## Ausgabeformat

Fristen-Bericht, Prüfbericht oder Erfassungsbestätigung je nach Modus. Immer mit Verifikations-Hinweis abschließen. Arbeitsergebnis-Kopfzeile voranstellen.

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:schutzrechts-portfolio` (kein Argument)

**Ausgabe (Auszug):**

> IP-PORTFOLIO-FRISTENBERICHT — 2025-07-15
> Fenster: nächste 90 Tage
>
> ⏰ FÄLLIG INNERHALB 90 TAGE (2)
>   TM-DPMA-012 / DPMA / Marke / ALPHAWAVE
>     Verlängerung § 47 Abs. 1 MarkenG — fällig 2025-08-20
>     Grundlage: 10. Jahrestag der Eintragung
>
>   PAT-EP-003 / EPO / Patent / Verfahren zur Datenübertragung
>     Jahresgebühr Jahr 5 — fällig 2025-09-01
>     Grundlage: Art. 86 EPÜ; Zahlung beim nationalen Amt (DPMA)
>
> *Berechnungen aus Portfolio-Register. Vor Handlung gegen DPMA DPMAdirektplus / EUIPO eSearch / WIPO Madrid Monitor verifizieren.*

## Risiken und typische Fehler

- **Berechnete Frist ist nicht die amtliche Frist:** Das Register ist eine Arbeitskopie; das Behördenregister ist die Quelle der Wahrheit. Eine falsch eingetragene Frist erzeugt falsches Sicherheitsgefühl.
- **Schonfrist als Normalzustand:** Schonfristgebühren sind Zusatzkosten; regelmäßige Nutzung der Schonfrist ist Ineffizienz, nicht Praxis.
- **Benutzungszwang übersehen:** § 26 MarkenG — Marke ohne ernsthafte Benutzung nach 5 Jahren löschbar (§ 49 MarkenG). Portfolio-Verlängerung setzt keine Benutzungsprüfung voraus — aber das Löschungsrisiko entsteht trotzdem.
- **Inhaberumbenennung/-umschreibung vergessen:** Nach Umfirmierung oder Umstrukturierung müssen Schutzrechte beim Amt umgeschrieben werden, sonst entstehen Validitätsrisiken.
- **PCT-Nationale-Phase-Fristen:** 30/31-Monatsfrist (Regel 22.1 PCT) ist hart — kein Wiedereinsetzen bei Versäumnis in den meisten Ländern.

## Quellenpflicht

Alle Fristenangaben müssen auf konkreten Normen beruhen. Pflichtquellen:

- **Gesetze:** § 47 MarkenG, § 17 PatG, § 13 GebrMG, § 27 DesignG; Art. 53 UMV; Art. 12 GGV; Art. 86 EPÜ; PatKostG
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zu Markenfristen oder Jahresgebühren
- **Kommentar:** Ingerl/Rohnke MarkenG oder Benkard PatG mit § und Randnummer
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.
