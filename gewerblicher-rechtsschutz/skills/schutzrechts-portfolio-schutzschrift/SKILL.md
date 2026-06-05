---
name: schutzrechts-portfolio-schutzschrift
description: "Schutzrechts Portfolio Schutzschrift: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schutzrechts Portfolio Schutzschrift

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Schutzrechts Portfolio Schutzschrift** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schutzrechts-portfolio` | Unternehmen oder Kanzlei muss IP-Portfolio verwalten und anstehende Fristen im Blick behalten. Schutzrechtsportfolio-Verwaltung. Prüfraster: Eintragungen Verlaengerungen Jahresgebühren Benutzungsnachweise Fristkalender. Output: Fristenkalender und Portfolio-Audit mit Luecken Verfall und Benutzungsfragen. Abgrenzung zu schutzschrift-eilverfuegung (Verletzungsverteidigung) und markenanmeldung-dpma. |
| `schutzschrift-eilverfuegung` | Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befuerchtet einstweilige Verfuegung ohne Anhoerung. § 945a ZPO Schutzschrift ZSER. Prüfraster: Hinterlegung zentrales elektronisches Schutzschriftenregister § 945a ZPO Sachverhalt Gegenrede Glaubhaftmachung eidesstattliche Versicherung Wertangabe Senatsauswahl. Output: Schutzschrift-Entwurf für sofortige Hinterlegung. Abgrenzung zu unterlassungsverlangen (Abwehr der Abmahnung selbst) und verletzungs-triage. |
| `spezial-abmahnung-compliance-dokumentation-und-akte` | Abmahnung im gewerblichen Rechtsschutz: Compliance-Dokumentation und Aktenführung. Wie Abmahnvorgänge vollständig dokumentiert, Fristen gesichert und Entscheidungen nachvollziehbar gemacht werden – für Anwaltskanzlei und Unternehmens-Rechtsabteilung. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Schutzrechts Portfolio Schutzschrift**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schutzrechts-portfolio`

**Fokus:** Unternehmen oder Kanzlei muss IP-Portfolio verwalten und anstehende Fristen im Blick behalten. Schutzrechtsportfolio-Verwaltung. Prüfraster: Eintragungen Verlaengerungen Jahresgebühren Benutzungsnachweise Fristkalender. Output: Fristenkalender und Portfolio-Audit mit Luecken Verfall und Benutzungsfragen. Abgrenzung zu schutzschrift-eilverfuegung (Verletzungsverteidigung) und markenanmeldung-dpma.

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
- `--prüfung` — umfassende Portfolioprüfung
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 47 Rn. 1 ff. (Schutzdauer und Verlängerung), § 49 Rn. 1 ff. (Löschung wegen Nichtbenutzung)
- Benkard/Rogge, PatG, 12. Aufl. 2023, § 17 Rn. 1 ff. (Laufzeit und Jahresgebühren)
- Eichmann/Jestaedt/Fink/Meiser, DesignG, 6. Aufl. 2019, § 27 Rn. 1 ff. (Schutzdauer und Verlängerung)

## Ablauf

### Modus 1: Initialisierung (bei leerem Register oder `--neu`)

1. Quelle bestimmen: IP-Verwaltungssystem angebunden (Anaqua, Dennemeyer, Patronas, CPA Global)? Falls ja: Portfolio über Integration beziehen. Falls nein: Tabelle / Export anfordern oder interaktiv durchführen.
2. Für jedes Schutzrecht Fristen berechnen (Regeln unten). `nächste_fristen` mit den zwei bis drei nächsten Fälligkeiten befüllen.
3. Register schreiben. Zusammenfassung ausgeben:

```
Portfolio-Register initialisiert.

Schutzrechte: [N]
 Marken: [N] ([N eingetragen] / [N angemeldet])
 Patente: [N] ([N erteilt] / [N angemeldet])
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
 Grundlage: [z. B. "10. Jahrestag der Anmeldung, § 47 Abs. 1 MarkenG"]
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

Schlusssatz: *"Aus Portfolio-Register berechnet. Jede Frist vor Handlung gegen DPMA DPMAdirektplus, EUIPO eSearch, WIPO Madrid Monitor oder das jeweilige Behördenregister verifizieren."*

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

**Entscheidungs-Gate vor Statusänderung:** Bevor eine Amtshandlung oder Gebührenzahlung als "eingereicht" erfasst wird — falls der Nutzer kein Rechtsanwalt ist:

> Das Erfassen einer Marken­verlängerung, Jahresgebühr oder Gebrauchsmuster­verlängerung als "eingereicht" hat Konsequenzen. Wenn die Erfassung falsch ist — versäumtes Fristdatum, falsche Gebührenhöhe, fehlender Nachweis — verschiebt sich die Frist nicht und das Schutzrecht kann erlöschen. Haben Sie die Handlung mit dem zuständigen Patentanwalt oder Korrespondenzanwalt bestätigt (oder über DPMA DPMAdirektplus / EUIPO / WIPO überprüft)? Wenn ja: weiter. Wenn nein:
>
> - Noch nicht als eingereicht erfassen.
> - Folgendes zum Anwalt/Korrespondenzanwalt: Schutzrechts-ID, Behörde, Fristtyp, was das IP-Verwaltungssystem zeigt, was Ihrer Überzeugung nach eingereicht wurde und wann, und die Quelle dieser Überzeugung.

Kein `status: eingereicht` ohne ausdrückliches Ja über dieses Gate.

**Teilmodi:**

- **Manuelle Aktualisierung:** "Wir haben die Verlängerung von TM-DPMA-001 am 3. Juli eingereicht, Nachweis beigefügt." → Entsprechende Frist auf `status: eingereicht`, `eingereichtes_datum` setzen; nächste Frist im Lebenszyklus berechnen.
- **Statusänderung:** "Bitte TM-EUIPO-004 als aufgegeben markieren." → `status` aktualisieren, `nächste_fristen` leeren, Datum notieren.
- **IP-System-Abgleich:** Falls Anaqua / Dennemeyer / CPA Global angebunden: aktuellen Datenstand ziehen, abgleichen. Abweichungen kennzeichnen — System of Record gewinnt.

### Modus 5: Portfolioprüfung (`--prüfung`)

Umfassende Gesundheitsprüfung über die nächsten Monatsfristen hinaus:

**Fristenhygiene**
- Fristen derzeit in `schonfrist`-Status? (Handlung möglich, aber Zuschlag anfallend.)
- Erloschenene Schutzrechte, die nicht als aufgegeben / gelöscht markiert sind? Entweder wiederbeleben oder Status aktualisieren.
- Schutzrechte ohne berechnete `nächste_fristen`? Fehlende Daten oder unbekannte Jurisdiktion.

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
> TM-DPMA-012 / DPMA / Marke / ALPHAWAVE
> Verlängerung § 47 Abs. 1 MarkenG — fällig 2025-08-20
> Grundlage: 10. Jahrestag der Eintragung
>
> PAT-EP-003 / EPO / Patent / Verfahren zur Datenübertragung
> Jahresgebühr Jahr 5 — fällig 2025-09-01
> Grundlage: Art. 86 EPÜ; Zahlung beim nationalen Amt (DPMA)
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

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `schutzschrift-eilverfuegung`

**Fokus:** Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befuerchtet einstweilige Verfuegung ohne Anhoerung. § 945a ZPO Schutzschrift ZSER. Prüfraster: Hinterlegung zentrales elektronisches Schutzschriftenregister § 945a ZPO Sachverhalt Gegenrede Glaubhaftmachung eidesstattliche Versicherung Wertangabe Senatsauswahl. Output: Schutzschrift-Entwurf für sofortige Hinterlegung. Abgrenzung zu unterlassungsverlangen (Abwehr der Abmahnung selbst) und verletzungs-triage.

# Schutzschrift gegen Eilverfügung

## Zweck

Wenn eine einstweilige Verfügung droht, kann eine Schutzschrift im zentralen elektronischen Schutzschriftenregister hinterlegt werden — das Gericht muss sie bei jeder EV-Prüfung berücksichtigen.

## Schritt 1 — Anwendungsbereich

### Wann sinnvoll?

- **Nach Abmahnung** Schadensersatz oder Unterlassungs-Forderung mit Frist
- **Nach Schreiben eines Mitbewerbers** mit Drohung
- **Vor einem Branchen-Event** wo Mitbewerber EV beantragen könnte
- **Bei Marken-Wechsel-Strategie** mit erwartetem Widerstand

### Wann nicht sinnvoll?

- Bei eindeutig zugestandenem Verstoß — kontraproduktiv
- Bei rein theoretischem Risiko — Aufwand verschwendet
- Bei bereits eingereichtem EV-Antrag

## Schritt 2 — Schutzschrift-Register § 945a ZPO

### Zentralregister

- **Bundes-Elektronisches Schutzschriftenregister** (BESR)
- Alle Gerichte greifen darauf zu
- Bei EV-Antrag prüft das Gericht das Register

### Hinterlegung

- Pflicht-Hinterlegung im Register § 945a Abs. 2 ZPO
- Anwalts-Einreichung per beA möglich
- Kosten-Begründung — keine Gebühr für Hinterlegung selbst, aber Bearbeitungs-Aufwand

### Gültigkeit

- **Sechs Monate**
- Verlängerungs-Möglichkeit bei fortbestehender Bedrohung

## Schritt 3 — Aufbau

### Briefkopf

- Mandant als potenziell Antragsgegner
- Bevollmächtigter Anwalt

### Empfänger

- "An die Gerichte" (typisch)
- Konkrete Gerichte können benannt werden

### Betreff

- "Schutzschrift gemäß § 945a ZPO"
- Bezug auf erwarteten Antragsteller und Streitgegenstand

### Sachverhalt

- Aus Mandanten-Sicht erläutert
- Vorzeit-Geschehen
- Bisheriger Schriftwechsel mit potenziellem Antragsteller
- Eigene Bewertung der Sach- und Rechtslage

### Rechtliche Gegenrede

- Erwartete Anträge des Antragstellers
- Argumentation gegen Anspruchsgrundlage
- Argumentation gegen Eilbedürftigkeit
- Argumentation gegen Sicherungs-Anspruch

### Antrag

```
Es wird beantragt:

1. Der Antrag der [potenzielle Antragstellerin] wird abgelehnt.

2. Hilfsweise: Über den Antrag wird mündlich verhandelt
 und der Anhörung der Schutzschrift-Einreicherin
 Gelegenheit gegeben.

3. Höchst hilfsweise: Bei Erlass einer einstweiligen
 Verfügung wird Sicherheit Leistung in angemessener
 Höhe angeordnet.
```

## Schritt 4 — Glaubhaftmachung

### Eidesstattliche Versicherung

- Mandanten-eidesstattliche Versicherung zu Sachverhalts-Komponenten
- Inhaltlich auf Tatsachen beschränken nicht Wertung
- Vor-Anwalt-Beglaubigung

### Urkunds-Beweis

- Vertragsunterlagen
- Schriftverkehr
- Lieferungs-Belege

### Sachverständige

- Sachverständigen-Gutachten beifügen wenn vorhanden

## Schritt 5 — Argumentations-Linien

### Bei Marken-Streit

- Eigene Marken-Rechte
- Verbraucher-Verständnis konkret-bezogen
- Keine Verwechslungs-Gefahr
- Erschöpfungs-Grundsatz § 24 MarkenG

### Bei UWG-Streit

- Aussage nicht irreführend
- Vergleichende Werbung zulässig § 6 UWG
- Keine Marktverhaltens-Verstöße

### Bei Patent-Streit

- Patent möglicherweise nicht rechtsbeständig
- Nichtigkeits-Klage parallel
- Keine Verletzung — kein wortgleich gleichwertig

### Bei Persönlichkeitsrecht-Streit

- Meinungsfreiheit Art. 5 GG
- Tatsachenbehauptung wahr
- Berechtigtes Interesse

## Schritt 6 — Senatsauswahl

### Bei Konkurrenzzuständigkeit

- Mehrere Gerichte können zuständig sein
- Strategische Senatswahl
- Antragsteller wählt das für ihn günstigste Gericht

### Schutzschrift-Strategie

- Schutzschriften bei allen plausiblen Gerichten hinterlegen
- BESR macht das einheitlich möglich

## Schritt 7 — Eilbedürftigkeit angreifen

### Dringlichkeits-Indizien

- **Zeitablauf** zwischen Kenntnisnahme des Verstoßes und EV-Antrag
- München: typisch ein Monat
- Hamburg / Berlin: zwei Monate
- Frankfurt: ein bis zwei Monate
- Düsseldorf: länger toleriert

### Argument bei Eilbedürftigkeits-Verstoß

- Schutzschrift dokumentiert Verzögerung
- Bei Verfahrens-Beginn vorzeigen

## Schritt 8 — Antrag auf Sicherheitsleistung

### § 921 ZPO

- Bei EV-Erlass Sicherheitsleistung anordnen
- Höhe nach Ermessen typisch erheblicher Bruchteil des Streit-Volumens
- Schutz vor missbräuchlicher EV

### Begründung

- Wirtschaftliche Folgen Mandant
- Mögliche Schadensersatz-Rückforderung bei Aufhebung

## Schritt 9 — Praktische Schritte

1. **Drohungs-Analyse** — wer könnte EV beantragen wann wofür?
2. **Sachverhalts-Aufnahme** mit Mandant
3. **Argumentations-Linie** rechtlich
4. **Eidesstattliche Versicherung** vorbereiten
5. **Schutzschrift-Entwurf**
6. **Mandanten-Freigabe**
7. **Hinterlegung beim BESR** per beA

## Schritt 10 — Gegen-Schutzschrift / Reaktion auf Schutzschrift

### Wenn Schutzschrift des Mitbewerbers vorliegt

- Bei eigenem EV-Antrag bedacht reagieren
- Argumente entgegnen
- Ggf. Antrag direkt mit mündlicher Verhandlung

## Schritt 11 — Form-Anforderungen

- **Elektronisch** über beA
- **PDF/A-Format**
- **Anlagen** als separate Dokumente

## Schritt 12 — Kostenrisiko

### Bei nicht-Eintreten EV-Antrag

- Aufwand vergeblich aber häufig sinnvoll als Vorsichtsmaßnahme

### Bei Eintreten EV-Antrag mit Schutzschrift-Erfolg

- Kosten typisch dem Antragsteller
- Eigene Anwaltskosten kann Mandant erstatten erhalten

## Ausgabe

- `schutzschrift-{az}.md` strukturiert
- Eidesstattliche Versicherung Vorlage
- Argumentations-Linie sortiert
- Hinterlegungs-Dokumentation BESR
- Frist im Fristenbuch (sechs Monate Gültigkeit)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Quellen

- ZPO §§ 921 935 945a
- MarkenG § 24
- UWG § 6
- BGH I. Zivilsenat
- Koehler/Bornkamm/Feddersen UWG
- Ingerl/Rohnke MarkenG

<!-- AUDIT 27.05.2026: Bundle 032 Halluzinations-Reparatur
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

## 3. `spezial-abmahnung-compliance-dokumentation-und-akte`

**Fokus:** Abmahnung im gewerblichen Rechtsschutz: Compliance-Dokumentation und Aktenführung. Wie Abmahnvorgänge vollständig dokumentiert, Fristen gesichert und Entscheidungen nachvollziehbar gemacht werden – für Anwaltskanzlei und Unternehmens-Rechtsabteilung.

# Spezial: Abmahnung – Compliance-Dokumentation und Aktenführung

## Zweck und Mandatsbezug

Dieser Skill behandelt die **Compliance-konforme Dokumentation von Abmahnvorgängen** im gewerblichen Rechtsschutz. Kanzleien und Rechtsabteilungen, die regelmäßig Abmahnungen versenden oder empfangen, müssen eine vollständige, revisionssichere Akte führen – für interne Qualitätssicherung, spätere Verfahren, Beweissicherung und ggf. Haftungsvermeidung.

Mandatsbezug: Kanzlei versendet im Auftrag einer Mandantin monatlich Dutzende Abmahnungen. Rechtsabteilung eines Unternehmens empfängt Abmahnungen und muss Reaktionen nachvollziehbar entscheiden und dokumentieren. Anwalt muss im Nachhinein nachweisen, dass eine Abmahnung korrekt formuliert und fristgerecht versandt wurde.

## Aktenstruktur für Abmahnvorgänge

### Standardgliederung einer Abmahnakte

```
Abmahnakte [Mandant] ./. [Gegner] – [Datum]
│
├── 1. Basisdokumente
│ ├── Sachverhaltsprotokoll (Erstgespräch)
│ ├── Vollmacht des Mandanten
│ └── Mandate-Acceptance-Check (Interessenkonflikt, Honorarvereinbarung)
│
├── 2. Schutzrechtsnachweis
│ ├── Registerauszug (DPMA/EUIPO/Patentrolle)
│ └── Schutzrechtsübersicht (Klassen, Laufzeit, Lizenzsituation)
│
├── 3. Verletzungsnachweis
│ ├── Screenshot mit Datum, URL, Metadaten
│ ├── Kaufbeleg oder Liefernachweis
│ └── Eidesstattliche Versicherung des Mandanten
│
├── 4. Abmahnschreiben
│ ├── Entwurf v1 mit Revisionsverlauf
│ ├── Freigegebene Fassung
│ └── Zustellungsnachweis (Einschreiben, GV-Urkunde, beA-Protokoll)
│
├── 5. Reaktion der Gegenseite
│ ├── Eingehende Unterlassungserklärung
│ ├── Modifizierte UE oder Ablehnungsschreiben
│ └── Korrespondenz
│
├── 6. Folgeentscheidungen
│ ├── Entscheidungsvorlage (UE angenommen / abgelehnt / EV)
│ └── EV-Antrag (falls gestellt)
│
└── 7. Fristendokumentation
 ├── Reaktionsfrist an Gegner
 ├── Dringlichkeitsfrist (EV)
 └── Verjährungsfrist (Schadensersatz)
```

## Compliance-Checkliste Abmahnung VERSAND

### Vorab-Compliance

- [ ] **Mandatsprüfung:** Aktivlegitimation des Mandanten bestätigt?
- [ ] **Interessenkonfliktprüfung:** Kein Konflikt mit anderen Mandanten?
- [ ] **Schutzrecht valide:** Registerauszug aktuell? Keine Löschungsklage anhängig?
- [ ] **Verletzungshandlung belegt:** Beweissicherung vor Abmahnung abgeschlossen?
- [ ] **Abmahnmissbrauch ausgeschlossen:** § 8c UWG-Indizien geprüft?

### Abmahnung selbst

- [ ] Formvoraussetzungen §§ 13 UWG / 97a UrhG / 14 MarkenG erfüllt?
- [ ] Unterlassungserklärung beigefügt und vollständig?
- [ ] Frist angemessen (Minimum 7 Tage, Standard 2 Wochen)?
- [ ] Streitwert angegeben?
- [ ] Kosten korrekt berechnet?

### Zustellung

- [ ] Zustellungsweg dokumentiert (Post, GV, beA, E-Mail mit Lese-/Empfangsbestätigung)?
- [ ] Datum der Zustellung in Akte und Fristenbuch eingetragen?
- [ ] Zustellungsnachweis gesichert?

## Compliance-Checkliste Abmahnung EMPFANG

### Eingangserfassung

- [ ] Datum des Eingangs notiert (Poststempel, E-Mail-Timestamp)?
- [ ] Reaktionsfrist berechnet und in Fristenbuch eingetragen?
- [ ] Vorlage beim zuständigen Anwalt am selben Tag?
- [ ] Mandant informiert?

### Sachprüfung

- [ ] Aktivlegitimation des Abmahners geprüft?
- [ ] Materieller Verstoß bejaht, verneint oder unklar?
- [ ] Missbräuchlichkeit nach § 8c UWG geprüft?
- [ ] Streitwert und Kosten geprüft?

### Reaktionsdokumentation

- [ ] Entscheidung dokumentiert: UE angenommen / modifiziert / abgelehnt?
- [ ] Begründung der Entscheidung in Aktennotiz?
- [ ] Reaktionsschreiben entwurf erstellt und freigegeben?
- [ ] Zustellung der Antwort dokumentiert?

## Fristenmanagement

| Frist | Auslöser | Dauer | Konsequenz bei Versäumnis |
|---|---|---|---|
| Reaktionsfrist an Gegner | Versand Abmahnung | 7–14 Tage | EV-Antrag möglich |
| Dringlichkeitsfrist EV | Kenntnis Verletzung | Gericht-abhängig (4–8 Wochen) | Dringlichkeit selbst widerlegt |
| Vollziehungsfrist | EV erlassen, Zustellung Antragsteller | 1 Monat (§ 929 Abs. 2 ZPO) | EV verliert Kraft |
| Widerspruchsfrist | keine gesetzliche | – | Jederzeit möglich |
| Verjährung (UWG) | Kenntnis von Verletzung und Schuldner | 3 Jahre (§ 11 UWG) | Anspruch verjährt |
| Verjährung (MarkenG) | Kenntnis | 3 Jahre (§ 20 MarkenG) | Anspruch verjährt |

## Dokumentation im Mandantenverhältnis

### Informationspflichten

- Mandant über jede relevante Reaktion der Gegenseite informieren.
- Entscheidungsvorlagen mit Handlungsoptionen, Kosten und Risiken.
- Schriftliche Bestätigung mandantlicher Entscheidungen (UE annehmen/ablehnen, EV beantragen).

### Aktenabschluss

- Abmahnvorgang abgeschlossen, wenn: UE akzeptiert + Kostenfrage geklärt, oder Hauptsacheverfahren eingeleitet.
- Akte 10 Jahre aufbewahren (Rechtsanwaltskammer-Vorgaben; § 50 BRAO).
- Elektronische Akte: Sicherungskopie, Integrität der Dokumente sichern.

## Qualitätssicherung

- Stichprobenartige Überprüfung von Abmahnvorgängen auf formale Vollständigkeit.
- Checkliste bei jeder Abmahnung vollständig ausfüllen lassen.
- Bei Serienabmahnungen: Vorlage-Prüfung durch Partneranwalt.
- § 8c UWG-Risiko: Bei Musterabmahnungen Mandanteninteresse konkret prüfen.

## Quellenregel

- [§ 13 UWG – dejure.org](https://dejure.org/gesetze/UWG/13.html)
- [§ 97a UrhG – dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 8c UWG – dejure.org](https://dejure.org/gesetze/UWG/8c.html)
- BRAO § 50 (Aktenführung): [gesetze-im-internet.de/brao](https://www.gesetze-im-internet.de/brao/__50.html)
- Keine BeckRS-Blindzitate; Fristenpraxis aktuell über Gerichtspraxis prüfen.

## Anschluss-Skills

- `gewr-uwg-abmahnung-checkliste` – UWG-Abmahnung Prüfcheckliste
- `unterlassungsverlangen` – Unterlassungserklärung
- `workflow-dokumentenintake` – Dokumentenaufnahme
- `spezial-fristen-abschlussprodukt-und-uebergabe` – Fristenverwaltung
