---
name: gewr-geschaeftsgeheimnisgesetz
description: "Gewr Geschaeftsgeheimnisgesetz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gewr Geschaeftsgeheimnisgesetz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gewr Geschaeftsgeheimnisgesetz** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gewr-geschaeftsgeheimnisgesetz-spezial` | Geschäftsgeheimnisschutz nach GeschGehG: Schutzvoraussetzungen, angemessene Geheimhaltungsmaßnahmen, Verletzungshandlungen, Unterlassung, Schadensersatz und einstweiliger Rechtsschutz. Abgrenzung zu UWG und Strafrecht. |
| `gewr-markenanmeldung-bauleiter` | Markenanmeldung als strukturierter Bauleiter: Recherche, Klassenwahl, Anmeldeweg (DPMA/EUIPO/Madrid), Formvoraussetzungen, Fristen und Nachverfolgung. Praxisfür Anwälte und Unternehmen, die eine Marke anmelden oder betreuen wollen. |
| `gewr-uwg-abmahnung-checkliste` | UWG-Abmahnung: vollständige Prüfcheckliste für Versand und Empfang. Voraussetzungen §§ 3 und 8 UWG, Mitbewerbereigenschaft, Spürbarkeit, Wiederholungsgefahr, Unterlassungserklärung, Streitwert, Abmahnmissbrauch § 8c UWG und typische Verteidigungsargumente. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Gewr Geschaeftsgeheimnisgesetz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gewr-geschaeftsgeheimnisgesetz-spezial`

**Fokus:** Geschäftsgeheimnisschutz nach GeschGehG: Schutzvoraussetzungen, angemessene Geheimhaltungsmaßnahmen, Verletzungshandlungen, Unterlassung, Schadensersatz und einstweiliger Rechtsschutz. Abgrenzung zu UWG und Strafrecht.

# GewR: Geschäftsgeheimnisgesetz (GeschGehG) – Spezial

## Zweck und Mandatsbezug

Dieser Skill behandelt den **Schutz von Geschäftsgeheimnissen nach dem GeschGehG** (Gesetz zum Schutz von Geschäftsgeheimnissen, in Kraft seit 26.04.2019) als eigenständigen Rechtsbaustein im gewerblichen Rechtsschutz. Das GeschGehG hat die frühere Rechtslage nach §§ 17–19 UWG a.F. abgelöst und neue Anforderungen an den Schutz eingeführt – insbesondere die Pflicht zu „angemessenen Geheimhaltungsmaßnahmen".

Mandatsbezug: Mitarbeiter verlässt Unternehmen und nimmt Kundendaten mit; Wettbewerber hat Zugang zu Produktionsrezepturen erlangt; Auftragnehmer nutzt vertrauliche Konstruktionszeichnungen ohne Erlaubnis. Oder: Unternehmen erhält Abmahnung wegen angeblicher GeschGehG-Verletzung.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 2 GeschGehG** – Definition des Geschäftsgeheimnisses: Information, die (1) geheim ist, (2) kommerziellen Wert hat und (3) angemessenen Geheimhaltungsmaßnahmen unterliegt.
- **§ 3 GeschGehG** – Erlaubte Handlungen; kein Schutz für eigenständig entwickelte Informationen, Reverse Engineering unter Voraussetzungen.
- **§ 4 GeschGehG** – Verbotene Handlungen: unbefugter Erwerb, Nutzung, Offenlegung.
- **§ 5 GeschGehG** – Ausnahmen: Aufdeckung von Rechtsverstoß (Whistleblower), Ausübung von Meinungsfreiheit.
- **§ 6 GeschGehG** – Unterlassungsanspruch.
- **§ 10 GeschGehG** – Schadensersatz.
- **§ 20 GeschGehG** – Straf- und Bußgeldvorschriften.
- **Richtlinie (EU) 2016/943** – Trade Secrets Directive; Grundlage des GeschGehG.

### Schutzvoraussetzungen nach § 2 Nr. 1 GeschGehG

| Element | Inhalt | Prüfpunkt |
|---|---|---|
| Geheimheit | Information nicht allgemein bekannt oder leicht zugänglich | Marktwissen, Fachpublikation, offene Quellen? |
| Kommerzieller Wert | Wirtschaftlicher Wert der Geheimhaltung | Wettbewerbsvorteil? Lizenzierbar? |
| Angemessene Geheimhaltungsmaßnahmen | Aktive Schritte des Inhabers | NDA, Zugangsbeschränkung, Verschlüsselung, Schulung |

## Kaltstart in 5 Fragen

1. **Informationsart:** Was soll geschützt werden? Kundenliste, Rezeptur, Quellcode, Konstruktionszeichnung, Geschäftsstrategie?
2. **Geheimhaltungsmaßnahmen:** Welche Maßnahmen wurden ergriffen? NDA, IT-Zugangsschutz, physischer Zugangsschutz, Mitarbeiterschulung?
3. **Verletzungshandlung:** Was hat der Verletzer getan? Entwendet, weitergegeben, genutzt?
4. **Beziehung zum Verletzer:** Ehemaliger Mitarbeiter, Auftragnehmer, Wettbewerber, Einbrecher?
5. **Output:** Unterlassungsantrag (EV), Schadensersatz-Memo, Checkliste Geheimhaltungsmaßnahmen oder Abmahnung?

## Prüfprogramm

### Schritt 1 – Schutzfähigkeit prüfen

**Geheimheit:**
- Information nicht in Fachzeitschriften, Patentschriften oder im Internet verfügbar?
- Kein „allgemeines Branchenwissen" der Mitarbeiter?
- Nicht durch Reverse Engineering einfach gewinnbar (§ 3 Abs. 1 Nr. 2 GeschGehG)?

**Kommerzieller Wert:**
- Unternehmen spart Kosten/erzielt Erlöse durch Geheimhaltung?
- Lizenzierungspotential vorhanden?
- Wettbewerber würde profitieren?

**Angemessene Geheimhaltungsmaßnahmen (critical!):**
- **Vertragliche Maßnahmen:** NDA mit Mitarbeitern und Vertragspartnern; Vertraulichkeitsklauseln.
- **Technische Maßnahmen:** Passwortschutz, Verschlüsselung, Zugriffsberechtigungen.
- **Organisatorische Maßnahmen:** Need-to-know-Prinzip, Schulungen, Kennzeichnung als „vertraulich".
- **Physische Maßnahmen:** Abgesicherter Serverraum, verschlossene Schränke.
- Fehlen angemessener Maßnahmen: **Kein Schutz nach § 2 GeschGehG** – auch wenn Information wertvoll war.

### Schritt 2 – Verletzungshandlung nach § 4 GeschGehG

**Verbotener Erwerb (§ 4 Abs. 1 GeschGehG):**
- Unbefugter Zugriff auf Computer, Dateien, Räumlichkeiten.
- Mitnahme von Unterlagen ohne Erlaubnis.

**Verbotene Nutzung/Offenlegung (§ 4 Abs. 2 GeschGehG):**
- Nutzung in neuem Unternehmen; Weitergabe an Wettbewerber.
- Auch: Drittperson, die weiß, dass Information unerlaubt erlangt wurde (§ 4 Abs. 3 GeschGehG).

**Ausnahmen prüfen (§ 5 GeschGehG):**
- Whistleblowing zur Aufdeckung von Rechtsverstoß: schutzlos.
- Meinungsfreiheit, Pressefreiheit: Interessenabwägung.
- Ausübung gesetzlicher Rechte (z.B. Betriebsratsinformationsrecht).

### Schritt 3 – Einstweilige Verfügung

- Verfügungsanspruch: §§ 6 ff. GeschGehG (Unterlassung, Herausgabe).
- Verfügungsgrund: Dringlichkeit, drohende irreversible Offenbarung.
- Glaubhaftmachung: Nachweis der Schutzvoraussetzungen + Verletzungshandlung + Geheimhaltungsmaßnahmen.
- Besonderheit: § 16 GeschGehG – Vertraulichkeitsschutz im Verfahren; Gericht kann Verfahren unter Ausschluss der Öffentlichkeit führen.

### Schritt 4 – Schadensersatz und Herausgabe

- § 10 GeschGehG: Schadensersatz bei vorsätzlicher oder fahrlässiger Verletzung.
- Berechnungsmethoden: Tatsächlicher Schaden, entgangener Gewinn, Lizenzanalogie.
- § 7 GeschGehG: Herausgabe des Verletzergewinns.
- § 8 GeschGehG: Vernichtung und Rückruf der verletzenden Produkte.

### Schritt 5 – Arbeitnehmer-Sonderfall

- Nachvertragliches Wettbewerbsverbot: §§ 74 ff. HGB; muss gesondert vereinbart sein.
- Mitnahme von Arbeitgeberunterlagen: § 4 Abs. 1 GeschGehG; aber: eigene Notizen, Erfahrungswissen zulässig.
- Abgrenzung: „persönliches berufliches Wissen" vs. konkrete Unternehmensgeheimnisse.
- Strafrecht: § 20 GeschGehG; parallel zu zivilrechtlichen Ansprüchen.

## Typische Fallen

- **Fehlende Geheimhaltungsmaßnahmen:** Kein NDA, keine Zugangsbeschränkung → kein GeschGehG-Schutz trotz wertvoller Information.
- **Information war öffentlich:** Patentschrift, Fachpublikation, offene Quellen → Geheimheit fehlt.
- **Whistleblower-Ausnahme übersehen:** Mitarbeiter hat Rechtsverstoß aufgedeckt; kein Anspruch.
- **Verjährung:** Ansprüche nach § 9 GeschGehG verjähren in 3 Jahren (§ 195 BGB); Fristbeginn beachten.
- **Verwechslung mit Strafrecht:** GeschGehG und § 20 GeschGehG gelten nebeneinander; Strafanzeige ≠ Abmahnung.

## Output-Module

- **Schutzfähigkeits-Checkliste:** Geheimheit, kommerzieller Wert, Geheimhaltungsmaßnahmen.
- **Maßnahmen-Audit:** Vorhandene vs. empfohlene Geheimhaltungsmaßnahmen.
- **EV-Antrag-Skizze:** Verfügungsanspruch §§ 6 ff. GeschGehG, Glaubhaftmachungspaket.
- **Abmahnung Muster GeschGehG:** Verletzungshandlung, Anspruchsgrundlage, Unterlassungsaufforderung.

## Quellenregel

- GeschGehG: [gesetze-im-internet.de/geschgehg](https://www.gesetze-im-internet.de/geschgehg/)
- Richtlinie (EU) 2016/943: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943)
- [§ 2 GeschGehG – dejure.org](https://dejure.org/gesetze/GeschGehG/2.html)
- Rechtsprechung: openjur.de, bgh.de mit Gericht, Datum, AZ.
- Keine BeckRS-Blindzitate.

## Anschluss-Skills

- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV-Antrag
- `verletzungs-triage` – Erstentscheidung
- `unterlassungsverlangen` – Unterlassungserklärung
- `spezial-rechtsschutz-tatbestand-beweis-und-belege` – Tatbestand und Beweis

## 2. `gewr-markenanmeldung-bauleiter`

**Fokus:** Markenanmeldung als strukturierter Bauleiter: Recherche, Klassenwahl, Anmeldeweg (DPMA/EUIPO/Madrid), Formvoraussetzungen, Fristen und Nachverfolgung. Praxisfür Anwälte und Unternehmen, die eine Marke anmelden oder betreuen wollen.

# GewR: Markenanmeldung – Strukturierter Bauleiter

## Zweck und Mandatsbezug

Dieser Skill führt durch den **vollständigen Prozess der Markenanmeldung** – von der Vorabrecherche über die Klassenwahl bis zur Anmeldung und Nachverfolgung. Er fungiert als strukturierter „Bauleiter": jeder Schritt ist klar definiert, Entscheidungspunkte sind markiert und Fehlerquellen werden antizipiert.

Mandatsbezug: Startup möchte Produktname schützen; etabliertes Unternehmen will neue Produktlinie unter einer Marke führen; Mandant hat gute Idee für Marke, weiß aber nicht, wo anfangen. Oder: Anwalt übernimmt Markenportfolio-Betreuung und braucht strukturierten Prozess.

## Rechtlicher Rahmen

### Zentrale Normen und Register

- **§§ 3, 7, 8 MarkenG** – Schutzfähigkeit, Antragsrecht, absolute Schutzhindernisse.
- **§§ 32–42 MarkenG** – Anmeldeverfahren beim DPMA; Form, Inhalt, Klassenangabe.
- **§ 43 MarkenG** – Widerspruchsverfahren nach Eintragung.
- **VO (EU) 2017/1001 (EUTMR)** – Unionsmarken-Verordnung; Anmeldung beim EUIPO.
- **Madrider Protokoll (MMP)** – Internationale Markenanmeldung über WIPO; Grundlage DPMA- oder EUIPO-Marke.
- **Nizza-Klassifikation** – Internationale Klassifikation für Waren und Dienstleistungen (11. Ausgabe, regelmäßig aktualisiert).

### Anmeldewege im Überblick

| Weg | Zuständigkeit | Schutzgebiet | Kosten (ca.) | Bearbeitungszeit |
|---|---|---|---|---|
| Deutsche Marke | DPMA | Deutschland | 300–900 EUR | 3–6 Monate |
| Unionsmarke | EUIPO | 27 EU-Staaten | 850–1.350 EUR | 4–8 Monate |
| IR-Marke (Madrid) | WIPO/DPMA | Wunschländer | Variabel | 12–18 Monate |
| Nationale Einzelanmeldungen | Nationale Ämter | Jeweiliges Land | Variabel | Variabel |

## Kaltstart in 5 Fragen

1. **Zeichen:** Was soll angemeldet werden? Wortmarke, Bildmarke, Wort-Bildmarke, 3D, Klangmarke, Farbmarke?
2. **Waren/Dienstleistungen:** Was bietet der Mandant an? Beschreibung in eigenen Worten für Klassifizierungsanalyse.
3. **Schutzgebiet:** Deutschland, EU, international? Prioritäten?
4. **Zeitlage:** Gibt es Gründe für Priorität (Produktlaunch, Messe, Markteintritt)?
5. **Output:** Anmeldungsformular, Recherche-Bericht, Klassenübersicht, Anmeldestrategieübersicht?

## Bauleiter: Schritt-für-Schritt-Prozess

### Baustein 1 – Vorabrecherche (vor der Anmeldung!)

**Ziel:** Kollisionsmarken identifizieren, Risiko abschätzen.

- DPMA-Markenrecherche: [dpma.de/marken](https://www.dpma.de/marken) – DPMAregister online.
- EUIPO-TMview: [tmview.org](https://www.tmview.org) – internationale Datenbank.
- Wildcardsuche, phonetische Ähnlichkeit, Bildähnlichkeit (bei Bildmarken).
- Klassen: Identische und ähnliche Klassen recherchieren.
- Ergebnis: Grün/Gelb/Rot; Empfehlung an Mandanten.
- Bei Kollision: Abgrenzungsvereinbarung, Abänderung des Zeichens oder bewusste Risikoannahme.

### Baustein 2 – Klassenwahl (Nizza-Klassifikation)

- Nizza-Klassifikation: 45 Klassen (1–34 Waren, 35–45 Dienstleistungen).
- Relevante Klassen für typische Mandate:
 - Software: Klasse 42 (SaaS) + ggf. 9 (Hardware)
 - Kleidung: Klassen 25 (Bekleidung), 35 (Einzelhandel)
 - Lebensmittel: Klassen 29, 30, 43
 - Beratungsdienstleistungen: Klasse 45 (Rechtsberatung), 35 (Unternehmensberatung)
- Warenbeschreibung: Präzise, aber nicht zu eng; DPMA-Klassifikationsdatenbank nutzen.
- Kosten: Erste Klasse im Grundbetrag; jede weitere Klasse zusätzlich.

### Baustein 3 – Zeichengestaltung

- **Unterscheidungskraft (§ 8 Abs. 2 Nr. 1 MarkenG):** Kein rein beschreibendes Zeichen.
- **Freihaltebedürfnis (§ 8 Abs. 2 Nr. 2 MarkenG):** Geografische Angaben, Gattungsbezeichnungen nicht schutzfähig.
- Empfehlung: Fantasiebegriff, modifizierter Begriff oder Kombinationszeichen mit Unterscheidungskraft.
- Bildmarke: Eintragungsformat (jpg, png, tiff); klare Darstellung.

### Baustein 4 – Anmeldung beim DPMA

- Online: [dpmaregister.dpma.de](https://dpmaregister.dpma.de) (DPMAdirekt).
- Pflichtangaben: Zeichen, Anmelder (Name, Adresse), Waren-/Dienstleistungsverzeichnis, Klassenangabe.
- Anmeldegebühr: 300 EUR für bis zu 3 Klassen; 100 EUR je weitere Klasse.
- Priorität: DPMA-Anmelde-Datum gilt als Prioritätsdatum.
- Empfangsbestätigung: DPMA sendet Aktenzeichen; notieren und in Fristenbuch eintragen.

### Baustein 5 – Anmeldung beim EUIPO (Unionsmarke)

- Online: [euipo.europa.eu](https://www.euipo.europa.eu) – TMclass und eSearch.
- Gebühren (ab 2024): 850 EUR für 1 Klasse; 50 EUR für 2. Klasse; 150 EUR für jede weitere.
- Prüfungsumfang: EUIPO prüft nur absolute Hindernisse; relative Hindernisse im Widerspruchsverfahren.
- Widerspruchsfrist: 3 Monate ab Veröffentlichung (Art. 46 EUTMR).

### Baustein 6 – IR-Marke über WIPO (Madrid)

- Grundlage: Bestehende DPMA- oder EUIPO-Marke.
- Formular MM2: Beim DPMA als Ausgangsstelle einreichen.
- Länderauswahl: WIPO-Mitgliedstaaten; Gebühren je nach Schutzklassen und Ländern.
- Gebühren: Grundgebühr + individuelle Gebühren der Bestimmungsländer.
- Nachdesignierung: Weitere Länder können nachträglich benannt werden.

### Baustein 7 – Nachverfolgung und Widerspruchsbeobachtung

- DPMA-Markenblatt: Wöchentliche Veröffentlichung; Widerspruchsfrist 3 Monate (§ 42 MarkenG).
- Markenwatch-Dienste einrichten: Kollisionsmarken überwachen.
- Bei EUIPO: EUIPO-Bulletin; Widerspruchsfrist 3 Monate.
- Verlängerung: Deutsche Marke alle 10 Jahre; EUIPO alle 10 Jahre; fristgerecht verlängern!
- Benutzungsschonfrist: 5 Jahre nach Eintragung; Marke muss ernsthaft benutzt werden.

## Typische Fallen

- **Keine Vorrecherche:** Kostspielige Anmeldung scheitert an Widerspruch.
- **Zu enger Waren-/Dienstleistungskatalog:** Spätere Erweiterung kostet neue Anmeldung.
- **Rein beschreibende Marke:** DPMA/EUIPO weist zurück (§ 8 Abs. 2 Nr. 1, 2 MarkenG / Art. 7 EUTMR).
- **Frist für Widerspruch übersehen:** Kollisionsmarke bleibt eingetragen.
- **Benutzungsschonfrist ignoriert:** Marke löschbar nach 5 Jahren Nichtbenutzung.

## Output-Module

- **Recherche-Bericht:** Kollisionsmarken, Risikobewertung, Empfehlung.
- **Klassenmatrix:** Waren/Dienstleistungen → Nizza-Klassen.
- **Anmeldecheckliste:** DPMA/EUIPO/WIPO – je nach Schutzgebiet.
- **Fristenplan:** Anmeldedatum, Veröffentlichung, Widerspruchsfrist, Eintragung, Verlängerung.

## Quellenregel

- [DPMA Markenrecht – dpma.de](https://www.dpma.de/marken/index.html)
- [EUIPO – euipo.europa.eu](https://www.euipo.europa.eu)
- [VO (EU) 2017/1001 – eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32017R1001)
- [MarkenG – gesetze-im-internet.de](https://www.gesetze-im-internet.de/markeng/)
- Keine BeckRS-Blindzitate; DPMA- und EUIPO-Webseiten für aktuelle Gebühren nutzen.

## Anschluss-Skills

- `markenrecherche` – Vertiefung der Kollisionsrecherche
- `markenanmeldung-dpma` – DPMA-Anmeldung im Detail
- `spezial-dpma-fristen-form-und-zustaendigkeit` – Fristen und Formalien
- `spezial-euipo-dokumentenmatrix-und-lueckenliste` – EUIPO-Verfahren

## 3. `gewr-uwg-abmahnung-checkliste`

**Fokus:** UWG-Abmahnung: vollständige Prüfcheckliste für Versand und Empfang. Voraussetzungen §§ 3 und 8 UWG, Mitbewerbereigenschaft, Spürbarkeit, Wiederholungsgefahr, Unterlassungserklärung, Streitwert, Abmahnmissbrauch § 8c UWG und typische Verteidigungsargumente.

# GewR: UWG-Abmahnung – Vollständige Prüfcheckliste

## Zweck und Mandatsbezug

Dieser Skill ist eine strukturierte Prüfcheckliste für **UWG-Abmahnungen** – sowohl für den Versand (Mandant ist Abmahner) als auch für den Empfang (Mandant hat Abmahnung erhalten). Der Skill erfasst alle prüfungsrelevanten Punkte: Aktivlegitimation, materieller Verstoß, formale Anforderungen, Unterlassungserklärung, Streitwert und missbräuchliche Abmahnung nach § 8c UWG (2022-Reform).

Mandatsbezug: Online-Händler erhält Abmahnung wegen fehlendem Impressum oder irreführender Werbung; Wettbewerber mahnt wegen unlauterer Nachahmung ab; Verband mahnt wegen DSGVO-Verstoß mit UWG-Anspruch ab. Oder: Mandant will selbst Wettbewerbsverletzung abmahnen.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 3 UWG** – Generalklausel: unlauter, wenn geeignet, Interessen von Verbrauchern, Mitbewerbern oder sonstigen Marktteilnehmern spürbar zu beeinträchtigen.
- **§ 3a UWG** – Rechtsbruch: Verstoß gegen Marktverhaltensnormen (z.B. DSGVO, PAngV, HWG).
- **§ 4 UWG** – Mitbewerberschutz: Herabsetzen, Anschwärzen, Nachahmung.
- **§ 5 UWG** – Irreführende geschäftliche Handlungen; § 5a UWG: Irreführung durch Unterlassen.
- **§ 8 UWG** – Unterlassungs- und Beseitigungsanspruch; Aktivlegitimation (Mitbewerber, Verbände).
- **§ 8c UWG** – Missbräuchliche Geltendmachung; Indizien für Missbrauch; Rechtsfolge.
- **§ 13 UWG** – Abmahnung als außergerichtliche Aufforderung zur Unterlassung; Kostenerstattung.
- **§ 12 UWG** – Einstweiliger Rechtsschutz; Besonderheiten Dringlichkeit.

### UWG-Reform 2022 (Umsetzung OMNIBUS-Richtlinie)

- Neue Tatbestände: Bewertungsmanipulation (§ 5b Abs. 3 UWG), Sonderangebote ohne Hinweis auf Vorpreis (§ 5a Abs. 4 UWG).
- Erweiterter Verbraucherschutz online; Dual-use-Produkte, Suchrankings.

## Checkliste Abmahnung VERSAND (Abmahner-Perspektive)

### Block A – Aktivlegitimation

- [ ] **Mitbewerber (§ 8 Abs. 3 Nr. 1 UWG):** Mandant und Abgemahnter sind Mitbewerber (gleiches Marktsegment, konkurrieren um dieselbe Kundschaft)?
- [ ] **Qualifizierter Verband (§ 8 Abs. 3 Nr. 2 UWG):** Aufnahme in Liste der qualifizierten Wirtschaftsverbände (§ 8b UWG)?
- [ ] **Kammer/Innungen (§ 8 Abs. 3 Nr. 4 UWG):** IHK, HWK?
- [ ] **Verbraucherschutzverbände (§ 8 Abs. 3 Nr. 3 UWG):** Bei Verbraucherschutzverstößen?

### Block B – Materieller Verstoß

- [ ] **Tatbestand:** Welche UWG-Norm ist verletzt? (§ 3a, 4, 5, 5a, 5b, 6, 7 UWG)
- [ ] **Spürbarkeit (§ 3 Abs. 1 UWG):** Geringfügigkeitsschwelle überschritten?
- [ ] **Beleg:** Screenschot mit Datum/URL, Kaufbeleg, eidesstattliche Versicherung?
- [ ] **Verletzungshandlung konkret beschrieben:** Wann, wo, wie?

### Block C – Wiederholungsgefahr

- [ ] Wiederholungsgefahr wird durch vorangegangene Verletzungshandlung vermutet.
- [ ] Nur durch strafbewehrte Unterlassungserklärung ausgeräumt.
- [ ] Erstbegehungsgefahr: Bei konkreten Vorbereitungshandlungen; schwerer nachzuweisen.

### Block D – Formvoraussetzungen Abmahnung (§ 13 UWG)

- [ ] Schriftform (§ 13 Abs. 1 UWG); i.d.R. Brief oder sichere E-Mail.
- [ ] Klare Bezeichnung des Abgemahnten und des Abmahnenden.
- [ ] Konkrete Bezeichnung der Verletzungshandlung.
- [ ] Aufforderung zur Unterlassung mit Fristsetzung (§ 13 Abs. 2 Nr. 3 UWG).
- [ ] Beifügung einer vorformulierten strafbewehrten Unterlassungserklärung (§ 13 Abs. 2 Nr. 2 UWG).
- [ ] Kostenhinweis.

### Block E – Unterlassungserklärung gestalten

- [ ] Strafbewehrte Unterlassungserklärung: Verpflichtung, Vertragsstrafe für jeden Verstoß.
- [ ] Vertragsstrafe: Angemessen, nicht zu hoch (Missbräuchlichkeit), nicht zu niedrig (Abschreckung).
- [ ] Räumlicher und zeitlicher Umfang: Welche Handlungen genau, wie lange?
- [ ] Keine Begrenzung auf Deutschland, wenn EU-weite Verletzung.

### Block F – Streitwert

- [ ] Orientierung: OLG-Tabellen und Gerichtspraxis des Abmahngerichts.
- [ ] Typische Streitwerte: Impressumsfehler 1.000–5.000 EUR; Wettbewerbsverletzung 10.000–100.000 EUR.
- [ ] Streitwert beeinflusst Kostenerstattung nach § 13 UWG und Gerichtskosten bei EV.

## Checkliste Abmahnung EMPFANG (Abgemahnter-Perspektive)

### Block 1 – Formale Prüfung

- [ ] Abmahner aktivlegitimiert? Mitbewerber? Verband in Liste § 8b UWG?
- [ ] Abmahnung formell vollständig? (§ 13 Abs. 2 UWG)
- [ ] Frist angemessen? (i.d.R. 1–2 Wochen; ggf. Fristverlängerung beantragen)

### Block 2 – Materieller Verstoß

- [ ] Liegt Verstoß tatsächlich vor? Welcher Tatbestand?
- [ ] Gibt es Einwendungen: Schutzbereich nicht betroffen, keine Spürbarkeit, kein Mitbewerberverhältnis?
- [ ] Ist Verletzung bereits beseitigt? Wiederholungsgefahr damit entfallen?

### Block 3 – Missbrauchsprüfung (§ 8c UWG)

- [ ] Abmahner hat offenkundig kein eigenes wirtschaftliches Interesse?
- [ ] Massenabmahnungen zu Bagatellverstößen?
- [ ] Höhe der Vertragsstrafe unverhältnismäßig?
- [ ] Abmahner selbst begeht denselben Verstoß?
- [ ] Wenn Missbrauch: Einwand nach § 8c UWG; ggf. Gegenanspruch auf Kostenerstattung.

### Block 4 – Reaktionsstrategie

| Option | Wann | Risiko |
|---|---|---|
| Unterlassungserklärung unverändert | Nie empfohlen | Zu weit, zu hohe Vertragsstrafe |
| Modifizierte Unterlassungserklärung | Bei echtem Verstoß | Akzeptiert Abmahner evtl. nicht |
| Ablehnung + Schutzschrift | Bei fehlender Aktivlegitimation / fehlendem Verstoß | EV-Risiko |
| Beseitigung ohne Erklärung | Nur wenn Erstbegehungsgefahr ohne Wiederholungsgefahr | Abmahner fordert trotzdem |

## Typische Fallen

- **Modifizierte Unterlassungserklärung nicht sorgfältig formuliert:** Deckt nicht den im Abmahntenor beschriebenen Verstoß ab; EV-Risiko bleibt.
- **Frist versäumt:** Abmahner stellt sofort EV-Antrag; Abgemahnter hatte keine Chance zu reagieren.
- **§ 8c UWG-Missbrauch nicht gerügt:** Berechtigte Einrede bleibt ungenutzt.
- **Streitwert nicht angefochten:** Zu hoher Streitwert führt zu überhöhten Anwaltskosten.

## Output-Module

- **Abmahnschreiben-Vorlage:** Vollständiger Mustertext §§ 3, 5, 8, 13 UWG.
- **Modifizierte Unterlassungserklärung:** Muster mit Vertragsstrafe, Umfangsbegrenzung.
- **Missbrauchsprüfungs-Checkliste:** § 8c UWG Indizien.
- **Streitwert-Orientierungstabelle:** Typische Verletzungsformen und Streitwerte.

## Quellenregel

- [§ 8 UWG – dejure.org](https://dejure.org/gesetze/UWG/8.html)
- [§ 8c UWG – dejure.org](https://dejure.org/gesetze/UWG/8c.html)
- [§ 13 UWG – dejure.org](https://dejure.org/gesetze/UWG/13.html)
- UWG vollständig: [gesetze-im-internet.de/uwg_2004](https://www.gesetze-im-internet.de/uwg_2004/)
- Rechtsprechung: BGH auf [bgh.de](https://www.bundesgerichtshof.de); OLG auf openjur.de.

## Anschluss-Skills

- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV nach Abmahnung
- `verletzungs-triage` – Erstentscheidung
- `unterlassungsverlangen` – Unterlassungserklärung
- `spezial-klausel-beweislast-und-darlegungslast` – Beweisfragen
