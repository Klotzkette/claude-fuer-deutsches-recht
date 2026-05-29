---
name: unterlassungsverlangen
description: "Schutzrechtsinhaber will Verletzung abmahnen oder hat selbst Abmahnung erhalten. Abmahnung Unterlassung MarkenG PatG UrhG UWG. Prüfraster: Abmahnungsentwurf modifizierte Unterlassungserklärung Streitwert Kostenansatz RVG oder Reaktions-Optionsmemo bei erhaltener Abmahnung. Output: Abmahnungsschreiben oder Optionsmemo mit Risikobewertung. Abgrenzung zu schutzschrift-eilverfuegung (Praeventiv) und verletzungs-triage (Eingangsentscheidung)."
---

# Abmahnung

Zwei Modi. Einen wählen:

- `/gewerblicher-rechtsschutz:abmahnung-urheberrecht --senden` – Abmahnungsentwurf kalibriert auf die Durchsetzungsstrategie der Kanzlei. Genehmigungsgate läuft vor Versand.
- `/gewerblicher-rechtsschutz:abmahnung-urheberrecht --empfangen` – Eingehende Abmahnung triagieren. Erzeugt ein Optionen-Memo mit Empfehlung.

## Zweck

Abmahnungen nach deutschem Recht dienen der Geltendmachung von Unterlassungsansprüchen wegen Marken- (§ 14 MarkenG), Urheber- (§ 97 Abs. 1 UrhG), Patent- (§ 139 PatG), Design- (§ 42 DesignG) oder Wettbewerbsverstößen (§ 8 UWG). Die ordnungsgemäß formulierte Abmahnung unterbricht die Wiederholungsgefahr, schafft Kostenerstattungsansprüche (§ 13 UWG; § 97a UrhG) und ist Voraussetzung für einen Antrag auf einstweilige Verfügung.

## Eingaben

- Kanzleiprofil (Durchsetzungsstrategie, Genehmigungsmatrix) – automatisch geladen
- Rechtsgrundlage des Verstoßes (Marke, Urheber, Patent, Design, UWG)
- Konkrete Verletzungshandlung mit Beschreibung und Beweisen (URLs, Screenshots, Fotos)
- Registernummer des verletzten Schutzrechts (falls eingetragen)
- Gegner: Name, Anschrift, Vertreter (falls bekannt)
- Gewünschte Frist zur Reaktion (Standard: 10–14 Tage, kürzer bei dringendem Eilbedarf)
- Streitwertvorgabe (falls vorhanden) oder Antrag auf Schätzung

## Ablauf – Sendemodus

### 1. Kanzleiprofil lesen
Durchsetzungsstrategie und Genehmigungsmatrix laden. Enthält das Profil `[PLATZHALTER]`, stoppen und auf `gewerblicher-rechtsschutz-kaltstart-interview` hinweisen.

### 2. Verletzung rechtlich einordnen

Gegenstand bestimmen:

**Markenrecht (§ 14 MarkenG):**
- Kennzeichen: eingetragene Marke, Benutzungsmarke, geschäftliche Bezeichnung
- Verletzungsform: Identität (§ 14 Abs. 2 Nr. 1), Verwechslungsgefahr (§ 14 Abs. 2 Nr. 2), Rufausnutzung/-beeinträchtigung bekannter Marken (§ 14 Abs. 2 Nr. 3)
- Prüfung: Benutzung im geschäftlichen Verkehr, für Waren/Dienstleistungen, ohne Zustimmung
- Benutzungsschonfrist: eingetragene Marke muss 5 Jahre ernsthaft benutzt sein (§ 26 MarkenG), sonst Einrede nach § 25 MarkenG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Urheberrecht (§ 97 Abs. 1 UrhG):**
- Schutzvoraussetzungen: persönliche geistige Schöpfung (§ 2 Abs. 2 UrhG); keine Neuheitsprüfung
- Verletzungshandlungen: Vervielfältigung (§ 16 UrhG), Verbreitung (§ 17 UrhG), öffentliche Zugänglichmachung (§ 19a UrhG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Wettbewerbsrecht (§ 8 Abs. 1 UWG):**
- Unlautere geschäftliche Handlung: §§ 3 ff. UWG; Beispiele: Irreführung (§ 5 UWG), Anschwärzung (§ 4 Nr. 2 UWG), vergleichende Werbung (§ 6 UWG), unzumutbare Belästigung (§ 7 UWG)
- Mitbewerber, Verbraucherverbände, qualifizierte Einrichtungen (§ 8 Abs. 3 UWG) anspruchsberechtigt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Patentrecht (§ 139 PatG):**
- Patentanspruch muss in Kraft sein, nicht nichtig
- Verletzungshandlungen: § 9 PatG (Herstellung, Anbieten, Inverkehrbringen, Gebrauch, Einfuhr)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. Abmahnschreiben formulieren

**Pflichtbestandteile einer wirksamen Abmahnung** (§ 13 Abs. 2 UWG; § 97a Abs. 2 UrhG; allg. Zivilrecht):

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. **Bezeichnung des verletzten Rechts** – einschließlich Registernummer bei eingetragenen Rechten
3. **Unterlassungsaufforderung** – klar und bestimmt (§ 253 Abs. 2 Nr. 2 ZPO analog)
4. **Beifügen einer vorformulierten modifizierten Unterlassungserklärung** mit Vertragsstrafe
5. **Fristsetzung** – in der Regel 10–14 Tage; bei Eilbedarf kürzer (3–5 Tage); starre Fristen sind problematisch wenn sie faktisch unerreichbar sind
6. **Kostenhinweis** – Ankündigung der Geltendmachung von Abmahnkosten nach §§ 13, 14 UWG; § 97a Abs. 1 UrhG; RVG

**Modifizierte Unterlassungserklärung:**
- Abgabe einer unmodifizierten strafbewehrten UE beseitigt Wiederholungsgefahr; modifizierte UE mit zu niedriger Vertragsstrafe oder eingeschränktem Umfang dagegen nicht
- Empfohlene Formulierung: "... verpflichte mich, es bei Meidung einer für jeden Fall der Zuwiderhandlung zu zahlenden angemessenen Vertragsstrafe, deren Höhe vom Gläubiger nach billigem Ermessen festgesetzt und im Streitfall vom zuständigen Gericht überprüft wird (sog. Hamburger Brauch), zu unterlassen, ..."
- Hamburger Brauch vorzugswürdig gegenüber Festbetrag, um spätere Streitigkeiten über Strafhöhe zu vermeiden
- Geografischer und sachlicher Umfang muss dem abgemahnten Verstoß entsprechen
- Frist für UE-Abgabe ausdrücklich nennen

### 4. Streitwert berechnen

Streitwert bestimmt Gerichtskostenvorschuss und RVG-Gebühren:

| Verletzungsart | Typische Streitwertbandbreite (OLG-Rspr.) |
|---|---|
| Markenrecht (eingetragene Marke, kommerziell) | 25.000 – 150.000 € |
| Markenrecht (Benutzungsmarke, lokal) | 10.000 – 50.000 € |
| Urheberrecht (professionelles Werk) | 6.000 – 50.000 € |
| Urheberrecht (Lichtbild § 72 UrhG) | 3.000 – 10.000 € |
| UWG (Wettbewerbsverstoß, mittelständisch) | 10.000 – 100.000 € |
| Patent (kommerziell bedeutend) | 250.000 – 2.000.000 € |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 5. Kostenerstattungsanspruch berechnen (RVG)

Abmahnkosten nach § 13 Abs. 3 UWG (bei UWG-Abmahnungen) oder allgemeinen Grundsätzen (§§ 683, 670 BGB) sind erstattungsfähig:

- Gegenstandswert: Streitwert der Abmahnung
- Gebühr: 1,3-fache Geschäftsgebühr (Nr. 2300 VV RVG) ggf. erhöht
- Zzgl. Auslagenpauschale (Nr. 7002 VV RVG): 20 € (max. 20 % der Gebühren)
- Zzgl. Umsatzsteuer (§ 19a UStG beachten, falls USt-pflichtig)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Pre-Delivery-Gate

Vor dem Versand prüfen:
- [ ] Verletzung ausreichend dokumentiert? (Screenshots mit Datum, URL-Angabe, Notarstaat bei Bedarf)
- [ ] Registernummer des Schutzrechts verifiziert und in Kraft?
- [ ] Benutzungsschonfrist (§ 26 MarkenG) geprüft?
- [ ] UE-Formulierung vollständig und angemessen umfangreich?
- [ ] Streitwert anwaltlich plausibilisiert?
- [ ] Genehmiger aus Kanzleiprofil informiert?
- [ ] Mandant über mögliche Gegensanktionen (§ 8c UWG: missbräuchliche Abmahnung, Schadensersatz) informiert?

**Missbrauchsprüfung (§ 8c UWG):** Indizien für missbräuchliche Abmahnung: überwiegend Gebührengenerierung; Gläubiger hat zahlreiche gleichartige Verletzungen abgemahnt; Streitwert unverhältnismäßig; Frist unangemessen kurz. Missbräuchliche Abmahnung löst Schadensersatzpflicht des Abmahnenden aus (§ 8c Abs. 2 UWG); Freistellungsanspruch des Abgemahnten.

## Ablauf – Empfangsmodus

### 1. Abmahnung aufnehmen und Frist notieren
Datum des Zugangs und gesetzte Frist sofort vermerken. Frist für UE-Abgabe und ggf. einstweilige Verfügung bestimmen (EV ohne vorherige Abmahnung üblich; nach Fristablauf droht Hauptsacheverfahren).

### 2. Formelle Wirksamkeitsprüfung
Prüfen: Ist die Abmahnung hinreichend bestimmt? Enthält sie das verletzte Recht und die konkrete Verletzungshandlung? Ist die UE beigefügt? Eine formell unwirksame Abmahnung begründet keinen Kostenerstattungsanspruch und kann Rückschlüsse auf die Durchsetzungsabsicht erlauben.

### 3. Handlungsoptionen-Memo

| Option | Beschreibung | Wann passend |
|---|---|---|
| **A) UE-Abgabe (unmodifiziert)** | Strafbewehrte UE in vorgeschlagenem Umfang abgeben | Verletzung eindeutig, Umfang angemessen, keine Gegenwehr sinnvoll |
| **B) Modifizierte UE** | Eigene UE mit eingeschränktem Umfang / niedrigerer Vertragsstrafe anbieten | Verletzung teilweise bestreitbar, Umfang zu weit, Verhandlungsspielraum |
| **C) Negative Feststellungsklage** | Rechtshängigkeitssperre durch NFL (§ 256 ZPO) | Abmahnung offensichtlich unbegründet, Zermürbungsversuch |
| **D) Widerspruch / Abweisung** | Abmahnung zurückweisen, ggf. Gegenansprüche anmelden | § 8c UWG-Missbrauch wahrscheinlich, fehlende Aktivlegitimation |
| **E) Verhandlung** | Ohne UE verhandeln, Vergleich anstreben | Starkes Interesse beider Seiten an Lösung, kommerzieller Kontext |

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

**Wichtige Normen:** §§ 8, 12, 13, 14 UWG; § 97 Abs. 1, § 97a, § 139 UrhG; §§ 14, 26 MarkenG; § 139 PatG; § 42 DesignG.

**Leitentscheidungen:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8 Rn. 1.1 ff.
- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 14 Rn. 345 ff. (vor. auf BGH-Rspr. aktualisieren).
- Dreier/Schulze, UrhG, 7. Aufl. 2022, § 97a Rn. 12 ff.

## Ausgabeformat

**Sendemodus:** Abmahnschreiben als vollständiger Briefentwurf (Briefkopf, Datum, Empfänger, Betreff, Sachverhalt, Rechtslage, Forderungen, Fristangabe, Anlagen-Verzeichnis: modifizierte UE) + separater Prüfvermerk.

**Empfangsmodus:** Optionen-Memo mit Zusammenfassung der Abmahnung, Fristnotiz, Risikoeinschätzung je Option (Ampel 🔴/🟠/🟡/🟢), Empfehlung und Entscheidungsbaum.

## Beispiel (Sendemodus – Markenrechtliche Abmahnung)

> **Sachverhalt:** Mandant ist Inhaber der deutschen Wortmarke "NORDBLATT" (DPMA-Reg.-Nr. 30 2019 012 345, eingetragen für Kl. 25), registriert seit 2019. Dritter bietet auf einer Verkaufsplattform Oberbekleidung unter der Bezeichnung "NORDBLATT" an.

**Rechtliche Einordnung (Gutachtenstil):**

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Benutzungsschonfrist:* Die Marke ist seit 2019 eingetragen; die Fünfjahresfrist (§ 26 Abs. 5 MarkenG) läuft ab 2024; ernsthafte Benutzung durch Mandant zu dokumentieren. `[prüfen]`

*Unterlassungsanspruch:* Es besteht Wiederholungsgefahr (tatsächliche Verletzungshandlung); Unterlassungsanspruch aus § 14 Abs. 5 MarkenG gegeben.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Kosten:* 1,3-Geschäftsgebühr aus 50.000 € nach Nr. 2300 VV RVG = 1.641,40 € zzgl. 20 € Auslagenpauschale = 1.661,40 € zzgl. MwSt.

## Risiken / typische Fehler

- **Zu knappe Frist:** Fristen unter 3 Tagen können als unangemessen gelten und die Wiederholungsgefahr nicht wirksam beseitigen; bei bekannter Urlaubszeit oder Auslandssitz verlängern.
- **Unklarer Unterlassungsgegenstand:** Die abgemahnte Handlung muss vollstreckungstauglich beschrieben sein; andernfalls kann ein Unterlassungstitel nicht vollstreckt werden (§ 890 ZPO).
- **Missbräuchlichkeit (§ 8c UWG):** Serielle Abmahnungen mit primärem Kostenerzielungszweck sind missbräuchlich und begründen Schadensersatzpflichten; Massenfälle vorab auf Missbrauchsrisiko prüfen.
- **Benutzungsschonfrist (§ 26 MarkenG):** Unterlassene Prüfung gefährdet das gesamte Abmahnungsverfahren, wenn der Verletzer die Einrede erhebt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Kein Versand ohne Freigabe:** Das Plugin sendet keine Abmahnung; es entwirft und wartet auf Genehmigung durch den konfigurierten Genehmiger.

## Triage-Fragen vor Unterlassungsverlangen

Bevor das Unterlassungsverlangen formuliert wird, klaere:
1. Liegt Wiederholungsgefahr (tatsaechliche Verletzung) oder nur Erstbegehungsgefahr vor?
2. Ist die abgemahnte Handlung vollstreckungstauglich beschreibbar (§ 890 ZPO — keine vagen Formulierungen)?
3. Wurde die Unterlassungserklaerung ausreichend strafbewehrt (Hamburger Brauch vs. feste Vertragsstrafe)?
4. Ist die Dringlichkeitsfrist fuer eine spaetere einstweilige Verfuegung gewahrt (BGH: max. 4-6 Wochen nach Kenntniserlangung)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- BGH I ZR 153/16 (WRONG_TOPIC: tatsaechlich "19% MwSt. GESCHENKT" — irrefuehrende Werbung, nicht Unterlassungserklaerung-Praezision): ersetzt durch verifizierte Entscheidung BGH I ZR 82/99 vom 31.05.2001 (Weit-Vor-Winter-Schluss-Verkauf), GRUR 2002, 180 (Quelle: dejure.org/2001,536)
