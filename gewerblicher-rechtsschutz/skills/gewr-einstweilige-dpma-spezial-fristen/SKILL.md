---
name: gewr-einstweilige-dpma-spezial-fristen
description: "Gewr Einstweilige Dpma Spezial Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gewr Einstweilige Dpma Spezial Fristen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gewr Einstweilige Dpma Spezial Fristen** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gewr-einstweilige-verfuegung-eilverfahren-spezial` | Einstweilige Verfügung im gewerblichen Rechtsschutz: Verfügungsanspruch, Verfügungsgrund, Dringlichkeit, Glaubhaftmachung und Antragsgestaltung bei Marke, Patent, UWG und Urheberrecht. Praxisfür Antragsteller und Antragsgegner. |
| `spezial-dpma-fristen-form-und-zustaendigkeit` | DPMA-Verfahren im Detail: Fristen, Formvoraussetzungen und Zuständigkeiten für Marken-, Patent-, Gebrauchsmuster- und Designanmeldung sowie Widerspruchs- und Löschungsverfahren. Einreichungswege, Gebühren und Fehlerquellen. |
| `spezial-fristen-abschlussprodukt-und-uebergabe` | Fristenverwaltung im gewerblichen Rechtsschutz: Abschlussprodukte rechtzeitig fertigstellen, Übergabe an Mandanten und Behörden sichern. Fristenmatrix für DPMA, EUIPO, EPA, Gerichtsverfahren, EV-Vollzug und Abmahnfristen. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Gewr Einstweilige Dpma Spezial Fristen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gewr-einstweilige-verfuegung-eilverfahren-spezial`

**Fokus:** Einstweilige Verfügung im gewerblichen Rechtsschutz: Verfügungsanspruch, Verfügungsgrund, Dringlichkeit, Glaubhaftmachung und Antragsgestaltung bei Marke, Patent, UWG und Urheberrecht. Praxisfür Antragsteller und Antragsgegner.

# GewR: Einstweilige Verfügung – Eilverfahren Spezial

## Zweck und Mandatsbezug

Dieser Skill behandelt das **einstweilige Verfügungsverfahren im gewerblichen Rechtsschutz** als zentrales Instrument zur schnellen Durchsetzung von Unterlassungsansprüchen bei Schutzrechtsverletzungen und Wettbewerbsverstößen. Er deckt die Antragstellerseite (Verfügungsanspruch formulieren, Dringlichkeit begründen, glaubhaft machen) und die Antragsgegnerseite (Widerspruch, Schutzschrift, Dringlichkeitsselbstwiderlegung) ab.

Mandatsbezug: Markeninhaber entdeckt Verletzung und will sofort handeln; Patentinhaber sieht konkurrierendes Produkt auf Messe; UWG-Anspruchsteller reagiert auf irreführende Werbung; Abgemahnter will EV verhindern.

## Rechtlicher Rahmen

### Zentrale Normen

- **§§ 935, 940 ZPO** – Verfügungsanspruch und Verfügungsgrund als Doppelvoraussetzung der einstweiligen Verfügung.
- **§ 937 Abs. 2 ZPO** – Beschlussverfügung ohne mündliche Verhandlung bei Dringlichkeit.
- **§ 920 ZPO** – Glaubhaftmachung; eidesstattliche Versicherung als zentrales Beweismittel.
- **§ 938 ZPO** – Ermessen des Gerichts bei Ausgestaltung des Tenors.
- **§ 14 MarkenG** – Unterlassungsanspruch bei Markenverletzung.
- **§ 139 PatG** – Unterlassungsanspruch bei Patentverletzung.
- **§ 42 DesignG** – Unterlassungsanspruch bei Designverletzung.
- **§ 97 UrhG** – Unterlassungsanspruch bei Urheberrechtsverletzung.
- **§ 8 UWG** – Unterlassungsanspruch bei unlauterem Wettbewerb.

### Die Doppelvoraussetzung im Überblick

| Element | Inhalt | Beweismittel |
|---|---|---|
| Verfügungsanspruch | Materiell-rechtlicher Anspruch (Unterlassung) | Schutzrechtsurkunde, Verletzungsnachweis |
| Verfügungsgrund | Dringlichkeit; drohende Rechtsverletzung oder Erschwerung der Rechtsbefriedigung | Zeitverlauf, Erstkenntnis, eidesstattliche Versicherung |
| Glaubhaftmachung | Überwiegende Wahrscheinlichkeit beider Elemente | Eidesstattliche Versicherung + Belege |

## Kaltstart in 6 Fragen

1. **Schutzrechtsposition:** Welches Schutzrecht (Marke, Patent, Design, Urheberrecht, UWG-Anspruch)? Eingetragen, angemeldet oder unregistriert?
2. **Verletzungshandlung:** Was genau macht der Verletzer? Seit wann? Belege vorhanden?
3. **Dringlichkeit:** Wann wurde Verletzung erstmals bekannt? (Dringlichkeit selbst widerlegt bei zu langem Zuwarten)
4. **Vorangegangene Abmahnung:** Abmahnung bereits gesendet? Reaktion erhalten oder Frist abgelaufen?
5. **Gerichtswahl:** Welches Gericht soll angerufen werden? Warum (Gerichtspraxis, Zuständigkeit)?
6. **Output:** Antragsschriftsatz-Entwurf, Glaubhaftmachungs-Checkliste, eidesstattliche Versicherung oder Strategie-Memo?

## Prüfprogramm

### Schritt 1 – Verfügungsanspruch prüfen

**Markenrecht:**
- Schutzrecht: Eingetragene Marke (DPMA/EUIPO)? Priorität? Klassen?
- Verletzungstatbestand: Identität (§ 14 Abs. 2 Nr. 1 MarkenG), Verwechslungsgefahr (Nr. 2), Bekanntheitsschutz (Nr. 3)?
- Rechteinhaber: Eigentümer oder exklusiver Lizenznehmer mit Klagerecht?

**Patentrecht:**
- Eingetragenes Patent: Patentrolle, Ansprüche geprüft?
- Patentverletzung: wortsinngemäß oder äquivalent?
- Arbeitnehmererfindung: ArbnErfG-Überleitung geprüft?

**UWG:**
- Wettbewerbshandlung, Mitbewerbereigenschaft, Spürbarkeit (§ 3 UWG)?
- Fallgruppe: Irreführung (§§ 5, 5a UWG), vergleichende Werbung (§ 6 UWG), aggressive Werbung (§ 4a UWG)?

**Urheberrecht:**
- Schutzfähiges Werk? Urheberschaft/Lizenznehmereigenschaft?
- Verletzungshandlung: § 16 (Vervielfältigung), § 17 (Verbreitung), § 19a (öffentliche Zugänglichmachung)?

### Schritt 2 – Verfügungsgrund (Dringlichkeit)

- Gesetzliche Dringlichkeitsvermutung: Im MarkenG, UWG und UrhG gibt es teils Vermutungen.
- **Dringlichkeitsfrist:** Je nach Gericht 4–8 Wochen ab Kenntnis; Hamburger Praxis: 4 Wochen; Münchner Praxis: 6–8 Wochen.
- Kenntnis-Zeitpunkt: Wenn Antragsteller von Verletzung wusste und zu lange gewartet hat → Selbstwiderlegung.
- Eidesstattliche Versicherung zur Erstkenntnis: Datum der Kenntniserlangung, wie erlangt.

### Schritt 3 – Glaubhaftmachungspaket zusammenstellen

- Eidesstattliche Versicherung des Antragstellers: Sachverhalt, Erstkenntnis, Unterlassung nicht zuzumuten.
- Anlagen: Screenshot (mit Datum), Produktfoto, Messeprotokoll, Kaufbeleg.
- Schutzrechtsurkunde oder Registerauszug (DPMA-Markenregister, Patentrolle).
- Recherche-Ergebnis: Priorität, Schutzdauer, Klassen.
- Verletzungsanalyse: Wortsinngemäß oder äquivalent (Patent); Verwechslungsgefahr-Prüfung (Marke).

### Schritt 4 – Antragsgestaltung

**Tenor-Formulierung:**
- Präzise, nicht zu weit und nicht zu eng.
- Konkrete Verletzungshandlung beschreiben; abstraktere Formulierungen nur im Rahmen des Kernbereichs.
- Ordnungsmittelandrohung im Tenor beantragen (§ 890 Abs. 2 ZPO).

**Streitwertangabe:**
- Marke: je nach Bekanntheit und Umsatz 50.000–500.000 EUR.
- Patent: oft höher; Lizenzumsatz als Orientierung.
- UWG: oft 15.000–50.000 EUR für einfachen Verstoß.

**Sicherheitsleistung:** Antrag auf Absehen von Sicherheitsleistung stellen; Gericht hat Ermessen.

### Schritt 5 – Abmahnung vor EV?

- Keine gesetzliche Pflicht zur Abmahnung vor EV-Antrag; aber Abmahnung kann Wiederholungsgefahr beseitigen.
- Wenn Abmahnung: Reaktionsfrist muss abgelaufen sein oder Abgemahnter muss abgelehnt haben.
- Ohne Abmahnung: Direkter EV-Antrag möglich; Abmahnung kann nachgeholt werden (§ 93 ZPO-Problematik beachten).

## Antragsgegnerperspektive

- **Widerspruch (§ 924 ZPO):** Erzwingt mündliche Verhandlung; Kernverteidigung.
- **Schutzschrift:** Präventiv vor EV-Antrag einreichen (→ evvollzug-neu-008).
- **Dringlichkeitsselbstwiderlegung rügen:** Wenn Antragsteller zu lange gewartet hat.
- **Verfügungsanspruch angreifen:** Schutzrecht ungültig, kein Verstoß, Erschöpfung, Verwirkung.

## Typische Fallen

- **Dringlichkeitsselbstwiderlegung:** Antragsteller weiß seit Monaten von Verletzung und wartet; EV scheitert.
- **Zu weit formulierter Tenor:** Gericht lehnt ab oder schränkt erheblich ein; Kosten des Antragstellers.
- **Falsches Gericht:** Örtliche Zuständigkeit fehlt; EV abgewiesen.
- **Eidesstattliche Versicherung unvollständig:** Keine Angabe zur Erstkenntnis; Verfügungsgrund nicht glaubhaft gemacht.
- **Kein Schutzrechtsnachweis beigefügt:** Registerauszug fehlt; EV zurückgestellt.

## Output-Module

- **Antragsschriftsatz-Vorlage:** Rubrum, Antrag mit Ordnungsmittelandrohung, Begründung, Anlagen.
- **Eidesstattliche Versicherung:** Muster mit Erstkenntnis-Angabe.
- **Glaubhaftmachungs-Checkliste:** Schutzrecht, Verletzung, Dringlichkeit, Beweismittel.
- **Tenor-Formulierungs-Beispiele:** Marke, Patent, UWG mit Mustertexten.

## Quellenregel

- [§ 935 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/935.html)
- [§ 14 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/14.html)
- [§ 139 PatG – dejure.org](https://dejure.org/gesetze/PatG/139.html)
- [§ 8 UWG – dejure.org](https://dejure.org/gesetze/UWG/8.html)
- Rechtsprechung zur Dringlichkeitsfrist: openjur.de, bgh.de; Gericht und Datum immer angeben.
- Keine BeckRS-Blindzitate.

## Anschluss-Skills

- `evvollzug-neu-001` – Vollziehung der EV
- `evvollzug-neu-008` – Schutzschrift (Gegenseite)
- `schutzschrift-eilverfuegung` – Schutzschrift-Entwurf
- `verletzungs-triage` – Erstentscheidung bei IP-Verletzung

## 2. `spezial-dpma-fristen-form-und-zustaendigkeit`

**Fokus:** DPMA-Verfahren im Detail: Fristen, Formvoraussetzungen und Zuständigkeiten für Marken-, Patent-, Gebrauchsmuster- und Designanmeldung sowie Widerspruchs- und Löschungsverfahren. Einreichungswege, Gebühren und Fehlerquellen.

# Spezial: DPMA – Fristen, Form und Zuständigkeit

## Zweck und Mandatsbezug

Dieser Skill behandelt die **verfahrensrechtlichen Details des DPMA** (Deutsches Patent- und Markenamt) für alle relevanten Schutzrechtsverfahren. Er gibt präzise Informationen zu Fristen, Formvoraussetzungen, Einreichungswegen und zuständigen Stellen innerhalb des DPMA – und zu den Konsequenzen von Formfehlern und Fristversäumnissen.

Mandatsbezug: Anwalt fragt: Wann muss ich Widerspruch einlegen? Was ist die korrekte Formvorschrift für die Patentanmeldung? Kann ich online einreichen? Was passiert, wenn die Frist versäumt wurde?

## Organisationsstruktur DPMA

- **Hauptsitz:** Zweibrückenstraße 12, 80331 München
- **Zweigstellen:** Jena (Markenabteilung), Berlin
- **Online-Portal:** [dpmaregister.dpma.de](https://dpmaregister.dpma.de) (DPMAregister), [dpma.de](https://www.dpma.de)
- **Kontakt:** DPMA-Infoservice [info@dpma.de](mailto:info@dpma.de)

## Markenverfahren beim DPMA

### Anmeldung (§§ 32–38 MarkenG)

| Element | Inhalt | Konsequenz bei Fehler |
|---|---|---|
| Antragsformular | Formular D/A 95xx oder Online | Zurückweisung oder Bearbeitungsgebühren |
| Zeichendarstellung | Klare Darstellung des Zeichens | Zurückweisung |
| Waren-/Dienstleistungsverzeichnis | Nizza-Klassifikation | DPMA schlägt Klassifizierung vor; Einwand möglich |
| Anmeldegebühr | 300 EUR (3 Klassen) + 100 EUR/Klasse | Ohne Zahlung keine Priorität |
| Anmelder | Name, Adresse, ggf. Anwalt | Fehler verzögern Eintragung |

- **Prioritätsdatum:** Eingang vollständiger Anmeldung beim DPMA; kein Prioritätsdatum ohne Mindestanforderungen.
- **Bearbeitungszeit:** 3–6 Monate bis Eintragung bei fehlerfreier Anmeldung.

### Widerspruch (§ 42 MarkenG)

- **Frist:** 3 Monate ab Veröffentlichung der Eintragung im Markenblatt (§ 42 Abs. 1 MarkenG).
- **Formen:** Schriftlich oder online über DPMAregister; Widerspruchsgebühr 250 EUR.
- **Widerspruchsgrund:** Älteres Schutzrecht (Marke, Unternehmenskennzeichen).
- **Benutzungsschonfrist:** Ältere Marke muss benutzt werden, wenn > 5 Jahre eingetragen.
- **Keine Wiedereinsetzung** bei Versäumnis der Widerspruchsfrist.

### Löschungsantrag wegen älterer Rechte (§ 51 MarkenG)

- **Frist:** Keine allgemeine Ausschlussfrist; aber: Verwirkung nach § 21 MarkenG (5 Jahre Duldung).
- **Form:** Löschungsantrag beim DPMA oder Löschungsklage vor Landgericht.
- **Gebühr:** 100 EUR beim DPMA.
- **Klage statt DPMA:** Bei komplexen Sachlagen Klage vor LG oft effizienter.

### Löschungsantrag wegen absoluter Schutzhindernisse (§ 50 MarkenG)

- **Antragsberechtigt:** Jeder.
- **Gebühr:** 100 EUR.
- **Verfahren:** DPMA prüft; gegen Entscheidung Beschwerde zum BPatG (§ 66 MarkenG).

## Patentverfahren beim DPMA

### Anmeldung (§§ 34–44 PatG)

| Element | Inhalt |
|---|---|
| Anmeldeantrag | Formular D/P 1000 oder Online |
| Beschreibung | Vollständige Offenbarung der Erfindung |
| Ansprüche | Patentansprüche als Kernstück |
| Zeichnungen | Falls zur Beschreibung nötig |
| Zusammenfassung | Kurze Inhaltsangabe |
| Anmeldegebühr | 40 EUR (bei Online-Einreichung 60 EUR Papier) |
| Prüfungsantrag | Gesondert; 350 EUR; Frist 7 Jahre ab Anmeldung |

- **Neuheitsschonfrist:** § 3 Abs. 5 PatG – Offenbarung durch Anmelder bis 6 Monate vor Anmeldung unschädlich.
- **Priorität:** Unionspriorität nach Pariser Verbandsübereinkunft (PVÜ): 12 Monate für Auslandsanmeldung.
- **Offenlegung:** 18 Monate nach Priorität (§ 31 PatG); Patent wird veröffentlicht.

### Einspruch (§ 59 PatG)

- **Frist:** 3 Monate ab Tag der Veröffentlichung der Patenterteilung im Patentblatt.
- **Form:** Schriftlich; Einspruchsgebühr 200 EUR.
- **Einspruchsabteilung:** DPMA; Einspruchsentscheidung.
- **Beschwerde:** Zum BPatG (§ 73 PatG) innerhalb 1 Monat nach Zustellung.

### Jahresgebühren (§ 17 PatG)

- Ab 3. Patentjahr fällig; Staffelung nach Patentjahr; bis 22 Jahre Höchstlaufzeit.
- Verfall bei Nichtzahlung; keine rückwirkende Wiederherstellung ohne Wiedereinsetzungsantrag (§ 123 PatG).
- Wichtig: Jahresgebührenstaffel präzise in Fristenbuch eintragen.

## Gebrauchsmusterverfahren

- **Anmeldung:** Formular D/GM 50xx oder Online; Gebühr 40 EUR.
- **Keine materielle Prüfung:** DPMA prüft nur auf Formerfordernisse; Schutz entsteht mit Eintragung.
- **Schutzdauer:** Max. 10 Jahre; Verlängerung alle 3 Jahre.
- **Abzweigung aus Patent:** Innerhalb von 2 Monaten nach Patenterteilung möglich (§ 5 GebrMG).
- **Löschungsantrag:** Beim DPMA; Schutzhindernis geltend machen.

## Designverfahren

- **Anmeldung:** Formular D/EM 10xx oder Online; Gebühr 70 EUR je Design.
- **Sammelanmeldung:** Bis zu 100 Designs je Sammelanmeldung.
- **Keine materielle Prüfung.**
- **Schutzdauer:** Max. 25 Jahre; Verlängerung alle 5 Jahre.
- **Aufschiebung der Bekanntmachung:** Bis 30 Monate möglich (§ 21 DesignG).

## Beschwerdeweg

- Gegen DPMA-Entscheidungen: Beschwerde zum BPatG (§ 73 PatG, § 66 MarkenG, § 23 DesignG).
- **Frist:** 1 Monat (Patent/Marke/Design) nach Zustellung der angefochtenen Entscheidung.
- **Beschwerdegericht:** Bundespatentgericht, München.
- Weitere Revision: BGH (Rechtsfrage); für Marken § 83 MarkenG.

## Einreichungswege

| Weg | Möglichkeit |
|---|---|
| Online (DPMAregister) | Bevorzugt; elektronische Einreichung für alle Schutzrechte |
| Post | Möglich; Poststempel = Eingang; Rückschein empfohlen |
| Fax | Bedingt möglich; Empfang beim DPMA bestätigen lassen |
| Persönlich | DPMA-Kundenzentrum München (mit Termin) |
| Anwaltlicher Vertreter | Zugelassener Rechtsanwalt oder Patentanwalt |

## Typische Fehler

- **Widerspruchsfrist 3 Monate MarkenG verpasst:** Keine Wiedereinsetzung.
- **Prüfungsantrag Patent vergessen:** Nach 7 Jahren erlischt Patent ohne Prüfungsantrag.
- **Jahresgebühr nicht bezahlt:** Patent verfällt; Wiedereinsetzung nur bei entschuldbarem Versäumnis.
- **Zeichendarstellung unzureichend:** Anmeldung zurückgestellt bis Nachbesserung.

## Quellenregel

- [DPMA – dpma.de](https://www.dpma.de)
- [MarkenG – gesetze-im-internet.de](https://www.gesetze-im-internet.de/markeng/)
- [PatG – gesetze-im-internet.de](https://www.gesetze-im-internet.de/patg/)
- [§ 42 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/42.html)
- DPMA-Gebühren: [dpma.de/service/gebuehren](https://www.dpma.de/service/gebuehren/index.html)
- Keine BeckRS-Blindzitate; Gebühren und Fristen laufend über DPMA-Website prüfen.

## Anschluss-Skills

- `spezial-anmeldung-behoerden-gericht-und-registerweg` – Behördenübersicht
- `gewr-markenanmeldung-bauleiter` – Markenanmeldung Bauleiter
- `spezial-euipo-dokumentenmatrix-und-lueckenliste` – EUIPO-Verfahren
- `markenanmeldung-dpma` – DPMA-Anmeldung im Detail

## 3. `spezial-fristen-abschlussprodukt-und-uebergabe`

**Fokus:** Fristenverwaltung im gewerblichen Rechtsschutz: Abschlussprodukte rechtzeitig fertigstellen, Übergabe an Mandanten und Behörden sichern. Fristenmatrix für DPMA, EUIPO, EPA, Gerichtsverfahren, EV-Vollzug und Abmahnfristen.

# Spezial: Fristen – Abschlussprodukt und Übergabe

## Zweck und Mandatsbezug

Dieser Skill behandelt die **systematische Fristenverwaltung** im gewerblichen Rechtsschutz – von der Erfassung über die Überwachung bis zur termingerechten Ablieferung von Abschlussprodukten. Fristversäumnisse im IP-Recht können zum Verlust von Schutzrechten, zu Kostenfolgen oder zum Scheitern von Verfahren führen. Eine strukturierte Fristenmatrix ist die Grundlage verlässlicher anwaltlicher Praxis.

Mandatsbezug: Kanzlei betreut 20 Markenanmeldungen gleichzeitig; Rechtsabteilung verwaltet globales Patentportfolio; Anwalt hat mehrere parallele EV-Verfahren mit verschiedenen Vollziehungsfristen.

## Fristenmatrix: Überblick nach Verfahren

### A – DPMA-Fristen

| Frist | Auslöser | Dauer | Konsequenz bei Versäumnis |
|---|---|---|---|
| Marken-Widerspruch | Veröffentlichung im Markenblatt | 3 Monate | Keine Wiedereinsetzung |
| Marken-Löschungsantrag (ält. Recht) | Kenntnis der Eintragung | 5 Jahre Duldungsfrist (§ 21 MarkenG) | Verwirkung |
| Patent-Einspruch | Veröffentlichung der Erteilung | 3 Monate | Unwiederbringlich verpasst |
| Patent-Prüfungsantrag | Anmeldedatum | 7 Jahre | Patent gilt als zurückgenommen |
| Patent-Jahresgebühr | Fälligkeitstag nach Anmeldung | Jährlich ab 3. Jahr | Erlöschen des Patents |
| Patent-Wiedereinsetzung | Fristversäumnis | 2 Monate ab Wegfall Hindernis | Nur bei entschuldbarem Versäumnis |
| Design-Verlängerung | Ablauf Schutzperiode (5-Jahres-Intervalle) | 6 Monate Nachfrist | Erlöschen |
| Gebrauchsmuster-Verlängerung | Ablauf Schutzperiode (3-Jahres-Intervalle) | Nachfrist | Erlöschen |

### B – EUIPO-Fristen

| Frist | Auslöser | Dauer | Konsequenz bei Versäumnis |
|---|---|---|---|
| Unionsmarken-Widerspruch | Veröffentlichung | 3 Monate | Unabänderlich |
| Widerspruchs-Substantiierung | Ende Widerspruchsfrist | 2 Monate (+Verlängerung) | Widerspruch abgelehnt |
| Benutzungsnachweis | Anforderung durch Markeninhaber | Gesetzt (2 Monate) | Zurückweisung Widerspruch |
| Beschwerde | EUIPO-Entscheidung | 2 Monate | Unanfechtbar |
| Beschwerdebegründung | EUIPO-Entscheidung | 4 Monate | Beschwerde unzulässig |
| UM-Verlängerung | Ablauf 10-Jahres-Frist | 6 Monate Nachfrist (mit Zuschlag) | Löschung |

### C – EPA-Fristen

| Frist | Auslöser | Dauer | Konsequenz bei Versäumnis |
|---|---|---|---|
| Einspruch gegen EP | Erteilungsdatum Patentblatt | 9 Monate | Unabänderlich |
| Beschwerde EPA | Einspruchsentscheidung | 2 Monate | Unanfechtbar |
| Beschwerdebegründung EPA | Beschwerdeeinlegung | 4 Monate | Beschwerde unzulässig |
| Prio (Unionspriorität) | Erstanmeldung | 12 Monate | Priorität verloren |
| PCT-Nationaleintritt | PCT-Anmeldedatum | 30 Monate (Standard) | Nationales Patent nicht beansprucht |
| Validierung EP national | Erteilung | Je nach Staat (i.d.R. 3 Monate) | Kein nationaler Schutz |

### D – Gerichtliche Fristen

| Frist | Verfahren | Dauer | Konsequenz |
|---|---|---|---|
| EV-Vollziehungsfrist | EV erlassen + zugestellt Antragsteller | 1 Monat (§ 929 Abs. 2 ZPO) | EV verliert Kraft |
| Dringlichkeitsfrist EV | Kenntnis Verletzung | 4–8 Wochen (gericht-abhängig) | Dringlichkeit selbst widerlegt |
| Berufungsfrist | Urteil zugestellt | 1 Monat (§ 517 ZPO) | Rechtskraft |
| Revisionsfrist | OLG-Urteil zugestellt | 1 Monat (§ 548 ZPO) | Rechtskraft |
| Reaktionsfrist Abmahnung | Abmahnung zugestellt | 1–2 Wochen (gesetzt) | EV-Risiko |

### E – Vertragliche und prozessuale Sonderfristen

| Frist | Grundlage | Dauer |
|---|---|---|
| Verjährung MarkenG | § 20 MarkenG | 3 Jahre ab Kenntnis |
| Verjährung UWG | § 11 UWG | 3 Jahre ab Kenntnis |
| Verjährung UrhG | § 102 UrhG | 3 Jahre (§ 195 BGB) |
| Abschlussschreiben nach EV | Praxisregel | Ca. 2–4 Wochen nach Vollzug |
| Hauptsacheklage (§ 926 ZPO) | Gerichtliche Anforderung | Gesetzt (i.d.R. 2 Wochen–1 Monat) |

## Fristenbuch-Struktur (Empfehlung)

### Pflichtfelder je Frist

```
Frist-ID: [Eindeutige Kennnummer]
Verfahren: [Marke XY / Patent Z / EV LG Hamburg]
Fristtyp: [Widerspruch / Vollziehung / Jahresgebühr]
Auslösedatum: [Datum des auslösenden Ereignisses]
Fristdauer: [z.B. 3 Monate]
Fristende: [Berechnetes Datum]
Vorwarndatum: [Fristende – 14 Tage]
Verantwortlich: [Name Anwalt / Mandant]
Status: [Offen / In Bearbeitung / Erledigt]
Abschlussprodukt: [Was muss bis wann fertig sein]
Übergabedatum: [An Mandant / DPMA / Gericht]
Anmerkungen: [Besonderheiten]
```

## Checkliste: Abschlussprodukt und Übergabe

### Vor Fristablauf

- [ ] Abschlussprodukt vollständig? (Schriftsatz, Formular, Brief, Erklärung)
- [ ] Anlagen vollständig? (Registerauszug, Vollmacht, Beweismittel)
- [ ] Unterschriften eingeholt? (Mandant, Anwalt, GV-Auftrag)
- [ ] Einreichungsweg gewählt? (Online, Post, GV, beA)
- [ ] Kosten/Gebühren bezahlt oder Zahlungsauftrag erteilt?
- [ ] Versand-/Einreichungsbestätigung erwartet und eingeplant?

### Am Übergabetag

- [ ] Einreichung/Versand dokumentiert (Datum, Uhrzeit, Empfangsvermerk)?
- [ ] Behörden- oder Gerichtseingangsbestätigung angefordert?
- [ ] Mandant über Einreichung informiert?
- [ ] Fristenbuch aktualisiert (Status: Erledigt)?
- [ ] Nächste Frist (Entscheidung, Eintragung, Reaktion) in Fristenbuch eingetragen?

## Fristverlängerung und Wiedereinsetzung

| Instrument | Anwendungsbereich | Voraussetzungen |
|---|---|---|
| Fristverlängerung EUIPO | Substantiierungsfrist, Benutzungsnachweis | Antrag; begrenzt |
| Fristverlängerung EV (§ 929 Abs. 2 ZPO) | Vollziehungsfrist bei Auslandszustellung | Antrag vor Fristablauf |
| Wiedereinsetzung DPMA (§ 123 PatG) | Jahresgebühr, Prüfungsantrag | Entschuldbares Versäumnis; 2 Monate Antragsfrist |
| Wiedereinsetzung ZPO (§ 233 ZPO) | Gerichtliche Fristen | Ohne Verschulden versäumt |

## Quellenregel

- [§ 929 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/929.html)
- [§ 42 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/42.html)
- [§ 59 PatG – dejure.org](https://dejure.org/gesetze/PatG/59.html)
- DPMA-Fristen: [dpma.de](https://www.dpma.de)
- EUIPO-Fristen: [euipo.europa.eu](https://www.euipo.europa.eu)
- Aktuelle Fristenpraxis immer über offizielle Behördenwebseiten prüfen.

## Anschluss-Skills

- `spezial-dpma-fristen-form-und-zustaendigkeit` – DPMA-Verfahren
- `spezial-euipo-dokumentenmatrix-und-lueckenliste` – EUIPO-Verfahren
- `workflow-fristen-und-risikoampel` – Fristenworkflow
- `evvollzug-neu-001` – EV-Vollziehungsfrist
