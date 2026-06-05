---
name: markenanmeldung-dpma-markenrecherche-open
description: "Markenanmeldung Dpma Markenrecherche Open: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Markenanmeldung Dpma Markenrecherche Open

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Markenanmeldung Dpma Markenrecherche Open** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `markenanmeldung-dpma` | Mandant moechte eine Marke beim DPMA anmelden oder Widerspruch gegen eine eingetragene Marke einlegen. §§ 32 ff. MarkenG Markenanmeldung. Prüfraster: Nizza-Klassifikation Anmeldegebühren absolute Eintragungshindernisse § 8 MarkenG Widerspruchsverfahren § 42 MarkenG Beschwerde BPatG § 66 MarkenG. Output: Anmeldeformular-Entwurf oder Widerspruchs-Schriftsatz. Abgrenzung zu markenrecherche (Recherche vor Anmeldung) und verletzungs-triage (Verletzung nach Eintragung). |
| `markenrecherche` | Unternehmen oder Mandant plant neue Marke oder Produktname und fragt: Bestehen Kollisionsrisiken mit aelteren Marken? Markenrecherche vor Anmeldung. Prüfraster: Identitäts- und Aehnlichkeitsprüfung DPMAregister EUIPO eSearch+ WIPO Global Brand DB Warenklassen. Ergebnis Recherchepaket für anwaltliche Entscheidung kein Freigabegutachten. Output: Recherche-Bericht mit Kollisionsrisiken. Abgrenzung zu markenanmeldung-dpma (Anmeldung nach Recherche) und verletzungs-triage. |
| `open-source-pruefung` | Unternehmen will Software ausliefern oder als Open Source veroffentlichen und fragt nach Lizenz-Compliance. Open-Source-Lizenz-Compliance. Prüfraster: Manifest SBOM Repository Copyleft-Pflichten Lizenzkompatibilitaet GPL LGPL MIT Apache genehmigungsfähige Bibliotheken. Output: Compliance-Bericht mit Handlungsempfehlungen je Abhaengigkeit. Abgrenzung zu ip-klausel-prüfung (vertragliche IP) und fto-triage (Patente). |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Markenanmeldung Dpma Markenrecherche Open**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `markenanmeldung-dpma`

**Fokus:** Mandant moechte eine Marke beim DPMA anmelden oder Widerspruch gegen eine eingetragene Marke einlegen. §§ 32 ff. MarkenG Markenanmeldung. Prüfraster: Nizza-Klassifikation Anmeldegebühren absolute Eintragungshindernisse § 8 MarkenG Widerspruchsverfahren § 42 MarkenG Beschwerde BPatG § 66 MarkenG. Output: Anmeldeformular-Entwurf oder Widerspruchs-Schriftsatz. Abgrenzung zu markenrecherche (Recherche vor Anmeldung) und verletzungs-triage (Verletzung nach Eintragung).

# Markenanmeldung beim DPMA

## Zweck

Dieser Skill führt durch das DPMA-Anmeldeverfahren für Wortmarken, Bildmarken,
Wort-/Bildmarken und sonstige Markenformen (§ 3 MarkenG). Er umfasst die
Vorbereitung der Anmeldung (§ 32 MarkenG), die Klassifikation nach dem Nizza-
Abkommen, die Berechnung der Anmeldegebühren, die Prüfung absoluter Eintragungs-
hindernisse (§ 8 MarkenG), das Widerspruchsverfahren (§ 42 MarkenG) und den
Rechtsweg zum BPatG (§ 66 MarkenG). Mandatsbezug: Unternehmen möchte Wortmarke
oder Logo schützen; DPMA erteilt Beanstandung; Wettbewerber widerspricht.

## Eingaben

1. **Markenform** – Wortmarke, Bildmarke, Wort-/Bildmarke, abstrakte Farbmarke,
 Klangmarke, 3D-Marke (§ 3 Abs. 1 MarkenG).
2. **Waren und Dienstleistungen** – Konkrete Beschreibung; Klassenzuordnung nach
 Nizza-Klassifikation (45 Klassen); je Klasse eigene Gebühr ab Klasse 4.
3. **Anmeldetag** – maßgeblich für Priorität (§ 32 Abs. 1 MarkenG); Unionsprioritä
 (§ 34 MarkenG, 6 Monate ab Auslandsanmeldung); Ausstellungspriorität (§ 35
 MarkenG, 6 Monate).
4. **Recherche-Ergebnisse** – DPMA-Datenbank (DPMAregister), EUIPO (EUTM-Suche),
 WIPO (Madrid-System); ältere identische oder ähnliche Zeichen für
 Kollisionsrisiko.
5. **Anmelder** – Name, Adresse, ggf. Markenanwalts-/Patentanwaltsvollmacht
 (§ 11 MarkenG: kein Anwaltszwang beim DPMA, wohl aber Vertretungsmöglichkeit).

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 3 MarkenG** – Markenfähige Zeichen: alle Zeichen, die grafisch darstellbar
 und geeignet sind, Waren/Dienstleistungen eines Unternehmens von denen anderer
 zu unterscheiden.
- **§ 8 MarkenG** – Absolute Eintragungshindernisse: fehlende Unterscheidungskraft
 (Abs. 2 Nr. 1), beschreibender Charakter (Abs. 2 Nr. 2), Freihaltebedürfnis
 (Abs. 2 Nr. 2), Täuschungsgefahr (Abs. 2 Nr. 4), Sittenwidrigkeit (Abs. 2
 Nr. 5); Überwindung durch Verkehrsdurchsetzung (Abs. 3).
- **§ 32 MarkenG** – Anmeldeinhalt: Angaben zum Anmelder, Wiedergabe der Marke,
 Verzeichnis der Waren und Dienstleistungen; Anmeldetag nach Abs. 2.
- **§ 36 MarkenG** – Prüfung der Anmeldung auf Eintragungshindernisse.
- **§ 37 MarkenG** – Zurückweisung der Anmeldung bei Eintragungshindernis.
- **§ 40 MarkenG** – Eintragung und Veröffentlichung.
- **§ 42 MarkenG** – Widerspruch: binnen 3 Monaten nach Veröffentlichung der
 Eintragung (§ 42 Abs. 1 Satz 1 MarkenG); Widerspruchsgrund: ältere Marke
 (§ 9 MarkenG) oder sonstiges älteres Recht (§ 13 MarkenG).
- **§ 53 MarkenG** – Verfallsantrag wegen Nichtbenutzung (5-Jahres-Frist § 26
 MarkenG); einredeweise geltend machen im Widerspruchsverfahren.
- **§ 66 MarkenG** – Beschwerde zum BPatG gegen Beschlüsse des DPMA; Frist
 1 Monat ab Zustellung (§ 66 Abs. 2 MarkenG); aufschiebende Wirkung.

### Anmeldegebühren (Stand: DPMA-Gebührenordnung 2024)

| Anmeldung | Gebühr |
|---|---|
| Bis zu 3 Nizza-Klassen | 300 € (elektronisch) / 350 € (Papier) |
| Je weitere Klasse ab Klasse 4 | 100 € |
| Widerspruch | 250 € |
| Verlängerung (10 Jahre) | 750 € (bis 3 Klassen) |

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 "Medicon-Apotheke/MediCo Apotheke": Zum Freihaltebedürfnis (§ 8 Abs. 2 Nr. 2 MarkenG):
 Beschreibende Angaben, die zur Bezeichnung von Merkmalen der angemeldeten
 Waren oder Dienstleistungen dienen können, sind auch dann von der Eintragung
 ausgeschlossen, wenn die Beschreibung mittelbar oder nur in einer möglichen
 Verwendungsweise vorliegt; Überwindung durch Verkehrsdurchsetzung
 (§ 8 Abs. 3 MarkenG) möglich, wenn der Verkehr das Zeichen als Herkunftshinweis
 versteht.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 "Langenscheidt-Gelb": Zur Schutzfähigkeit abstrakter Farbmarken; einzelne
 Farbe ohne geografische Kontur kann Unterscheidungskraft haben, wenn sie durch
 langjährige Benutzung Verkehrsdurchsetzung erlangt hat; strenger Maßstab
 wegen Freihaltebedürfnis (§ 8 Abs. 2 Nr. 1 und 2 MarkenG).

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Markenrecherche** – DPMA-Datenbank (DPMAregister.dpma.de), EUIPO TMview,
 WIPO Global Brand Database; identische und ähnliche Zeichen für identische
 und ähnliche Waren/Dienstleistungen prüfen; absolute Hindernisse vorab
 einschätzen (§ 8 MarkenG).

2. **Klassifikation** – Waren und Dienstleistungen den Nizza-Klassen zuordnen
 (aktuelle Fassung 12. Ausg. NCL 2023); TMclass (EUIPO-Tool) nutzen;
 Klassenanzahl minimieren zur Kostenoptimierung.

3. **Anmeldeformular ausfüllen** – Elektronisch über DPMAonline (Einsparung 50 €
 gegenüber Papieranmeldung); Angaben: Anmelder, Vertreter, Markenform,
 Markenwiedergabe (Bilddatei in TIF/JPG), Waren-/Dienstleistungsverzeichnis,
 Prioritätsangaben.

4. **Gebühren einzahlen** – Gleichzeitig mit Einreichung oder innerhalb von
 3 Monaten (§ 6 DPMAV); Zahlung per Banküberweisung, Lastschrift oder
 DPMA-Guthabenkonto; fehlende Zahlung = kein Anmeldetag.

5. **DPMA-Prüfung abwarten** – Prüfung auf absolute Eintragungshindernisse
 (§ 36 MarkenG); ggf. Beanstandungsbescheid; Frist zur Stellungnahme
 (i. d. R. 4 Monate, verlängerbar). Keine Prüfung auf relative Hindernisse
 (§§ 9–13 MarkenG) durch DPMA.

6. **Eintragung und Veröffentlichung** – Bei positiver Prüfung: Eintragung ins
 Markenregister (§ 40 MarkenG); Veröffentlichung im Markenblatt;
 Schutzdauer 10 Jahre ab Anmeldetag (§ 47 Abs. 1 MarkenG).

7. **Widerspruchsfrist überwachen** – 3 Monate ab Veröffentlichung (§ 42 Abs. 1
 Satz 1 MarkenG); Inhaber älterer Marken können Widerspruch einlegen; frühzeitig
 Verwechslungsgefahr-Analyse durchführen.

8. **Widerspruchsverfahren** – Widerspruchsgebühr 250 €; Benutzungseinrede
 geltend machen (§ 43 MarkenG), wenn die ältere Marke älter als 5 Jahre;
 Verhandlung beim DPMA; Beschwerde zum BPatG (§ 66 MarkenG, Frist 1 Monat).

## Ausgabeformat

- **Anmeldememo** (Gutachtenstil): Hindernisanalyse § 8 MarkenG → Waren/DL-
 Verzeichnis → Kostenübersicht → Empfehlung.
- **Klassifikationstabelle** (Tabelle): Klasse | Waren/Dienstleistungen | Gebühr.
- **Stellungnahme auf Beanstandungsbescheid** (Schriftsatz): Adressat DPMA;
 Aktenzeichen; Argumentation zur Schutzfähigkeit; ggf. Verkehrsdurchsetzung.

## Beispiel

*Sachverhalt:* Mandantin möchte die Wortmarke "FRISCHKLAR" für Mineralwasser
(Klasse 32) und Vertrieb von Getränken (Klasse 35) beim DPMA anmelden.

*Hindernisanalyse (Gutachtenstil):*

Fraglich ist, ob der Begriff "FRISCHKLAR" die erforderliche Unterscheidungskraft
besitzt (§ 8 Abs. 2 Nr. 1 MarkenG) und nicht beschreibend ist (§ 8 Abs. 2
Nr. 2 MarkenG).

"FRISCH" und "KLAR" sind für Mineralwasser beschreibende Merkmale (Frische,
Klarheit). Die Kombination könnte als Gesamtbegriff dennoch hinreichende
Unterscheidungskraft haben, wenn sie nicht lexikalisch nachweisbar ist und vom
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
MarkenG, 13. Aufl. 2021, § 8 Rn. 55). Die Prüfung beim DPMA wird kritisch sein;
eine Stellungnahme zur Verkehrswahrnehmung sollte vorbereitend erstellt werden.
Gebühren: 300 € für bis zu 3 Klassen (elektronische Anmeldung); für Klasse 35
zusätzlich 100 € = insgesamt 400 €.

## Risiken und typische Fehler

- **Frist Widerspruch:** 3 Monate ab Veröffentlichung (§ 42 Abs. 1 Satz 1
 MarkenG); Versäumnis führt zum Verlust des Widerspruchsrechts.
- **Frist Beschwerde BPatG:** 1 Monat ab Zustellung des DPMA-Beschlusses
 (§ 66 Abs. 2 MarkenG).
- **Waren-/Dienstleistungsverzeichnis zu weit:** Überschießende Klassifikation
 erhöht Angriffsfläche für Nichtbenutzungseinrede (§ 26 MarkenG); nach 5 Jahren
 Verfallsrisiko für nicht genutzte Klassen.
- **Prioritätsfrist versäumt:** Unionspriorität 6 Monate ab Erstanmeldung
 (§ 34 MarkenG); Versäumnis führt zu Verlust der rückwirkenden Priorität.
- **Benutzungseinrede vergessen:** Im Widerspruchsverfahren Benutzungsnachweis
 der älteren Marke einfordern (§ 43 MarkenG), wenn Schutzdauer > 5 Jahre.
- **Berufsrecht:** § 43a BRAO, § 3 BORA; bei gleichzeitiger Vertretung von
 Anmelder und Widersprechendem: Interessenkonflikt.

## Quellenpflicht

Alle Aussagen zu Schutzfähigkeit, Verfahrensfristen und Gebühren nach
`references/zitierweise.md`. Gebührenangaben stets auf Aktualität prüfen
(DPMA-Gebührenordnung kann geändert werden). Bei absoluten Eintragungshindernissen
EuGH-Rspr. (HABM-Rspr.) und BGH-Rspr. nebeneinander zitieren und auf etwaige
Divergenzen hinweisen.

## Triage-Fragen vor DPMA-Markenanmeldung

Bevor die Anmeldung eingereicht wird, klaere:
1. Wurde eine umfassende Vorrecherche auf kollidierende aeltere Marken und Firmennamen durchgefuehrt?
2. Sind absolute Schutzhindernisse (§ 8 II MarkenG) geprueft — insbesondere Beschreibungsnaehe und mangelnde Unterscheidungskraft?
3. Wird eine Einzel- oder Multi-Class-Anmeldung bevorzugt (3 Klassen = EUR 300; jede weitere EUR 100)?
4. Soll Prioritaet auf eine auswärtige Voranmeldung (§ 34 MarkenG — 6 Monate) beansprucht werden?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Problem: Konkrete Leitentscheidungen duerfen nur nach Live-Verifikation mit Gericht, Datum, Aktenzeichen und freier/amtlicher Quelle ausgegeben werden.
 obwohl der Inhalt (Medicon-Apotheke, Freihaltebeduerfnis § 8 II Nr. 2 MarkenG) zum
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Fallname um "/MediCo Apotheke" ergaenzt. Beide Fundstellen im Dokument korrigiert.
 Verifiziert via dejure.org.
-->

## 2. `markenrecherche`

**Fokus:** Unternehmen oder Mandant plant neue Marke oder Produktname und fragt: Bestehen Kollisionsrisiken mit aelteren Marken? Markenrecherche vor Anmeldung. Prüfraster: Identitäts- und Aehnlichkeitsprüfung DPMAregister EUIPO eSearch+ WIPO Global Brand DB Warenklassen. Ergebnis Recherchepaket für anwaltliche Entscheidung kein Freigabegutachten. Output: Recherche-Bericht mit Kollisionsrisiken. Abgrenzung zu markenanmeldung-dpma (Anmeldung nach Recherche) und verletzungs-triage.

# Markenrecherche (Clearance)

## Zweck

Erste Verwechslungsrisikoprüfung für eine geplante Marke oder Unternehmensbezeichnung. Der Skill führt einen Knockout-Scan durch, identifiziert potenziell kollidierende Voreintragungen und analysiert die relevanten Verwechslungsfaktoren. Ergebnis ist ein Recherchepaket für den beratenden Anwalt – kein Freigabe- oder Sperrurteil. Einsatzfelder: Produktneueinführungen, Rebranding, Domainregistrierungen, Unternehmensneugründungen.

## Eingaben

- Zu prüfendes Zeichen (Wort, Bildmarke, kombiniertes Zeichen, Slogan, Farbe, Form)
- Gewünschte Waren- und Dienstleistungsklassen (Nizza-Klassifikation, 12. Ausgabe)
- Zielländer / Zieljurisdiktionen (DE, EU/EUTM, international/Madrid)
- Verwendungskontext und Branche
- Geplanter Anmeldetag (relevant für Priorität)
- Ggf. bereits bekannte Voreintragungen

## Ablauf

### 1. Zeichen qualifizieren

Art des Zeichens bestimmen und Schutzfähigkeit vorprüfen:

| Zeichenart | Schutzfähigkeitshinweis |
|---|---|
| Wortmarke (Fantasiebegriff) | i. d. R. schutzfähig; Prüfung auf absolute Schutzhindernisse |
| Wortmarke (beschreibend) | Schutzhindernis § 8 Abs. 2 Nr. 2 MarkenG; Art. 7 Abs. 1 lit. c UMV; Verkehrsdurchsetzung möglich |
| Bildmarke / Logo | Schutz für bildliche Gestaltung; Wortbestandteile separat prüfen |
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Dreidimensionale Marke | Funktionale Formen vom Schutz ausgeschlossen (§ 3 Abs. 2 MarkenG) |

Absolute Schutzhindernisse prüfen (§ 8 MarkenG; Art. 7 UMV): Fehlende Unterscheidungskraft, beschreibende Angaben, täuschende Angaben, Gattungsbezeichnungen.

### 2. Datenbankrecherche durchführen

**Pflicht-Datenbanken:**

| Datenbank | URL | Zweck | Jurisdiktion |
|---|---|---|---|
| DPMAregister | register.dpma.de | Nationale DE-Marken; Wort-/Bildsuche | Deutschland |
| EUIPO eSearch+ | euipo.europa.eu/eSearch | Unionsmarken (EUTM); auch ältere IR-Marken mit EU-Wirkung | EU |
| WIPO Global Brand DB | branddb.wipo.int | Internationale Registrierungen (Madrid-System); Protokollmarken | International |

**Ergänzende Recherche:**
- Gemeinsame Datenbank EPA/DPMA (für Gemeinschaftsmarken mit nationaler Wirkung)
- Handelsregister (Unternehmensbezeichnungen als relative Schutzhindernisse)
- Domainregistrierungen (nicht Markenrecht, aber Abmahn- und Verwechslungsrisiko)
- Unregistrierte Kennzeichen / bekannte Marken (§ 4 Nr. 3 MarkenG)

**Suchstrategie:**
1. **Identitätssuche:** exaktes Zeichen suchen
2. **Phonetische Ähnlichkeit:** Klangähnliche Schreibweisen (z. B. APEXBLATT / APEX BLATT / APEXBLAT)
3. **Visuelle Ähnlichkeit:** Bei Bildmarken ähnliche Gestaltungen
4. **Konzeptionelle Ähnlichkeit:** Sinnverwandte Begriffe (z. B. BLATT / LEAF)
5. **Klassenschwerpunkt:** Identische und benachbarte Klassen

### 3. Kollidierende Zeichen analysieren – Verwechslungsfaktoren

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Faktoren der Verwechslungsgefahr (§ 9 Abs. 1 Nr. 2 MarkenG; Art. 8 Abs. 1 lit. b UMV):**

| Faktor | Erhöht Verwechslungsgefahr | Verringert Verwechslungsgefahr |
|---|---|---|
| Zeichenähnlichkeit | Klang, Schriftbild oder Bedeutung ähnlich | Deutliche Unterschiede in allen Ebenen |
| Waren-/Dienstleistungsähnlichkeit | Identische oder eng verwandte Klassen | Unterschiedliche Branchen/Zielgruppen |
| Kennzeichnungskraft | Starke inhärente oder erworbene Unterscheidungskraft | Schwache, beschreibende Marke |
| Verkehrskreis | Allgemeinheit, geringere Aufmerksamkeit | Fachkreise, hohe Aufmerksamkeit |
| Aufmerksamkeitsgrad | Niedrigpreisig, impulsiv | Hochpreisig, sorgfältige Kaufentscheidung |

**Zeichenähnlichkeit – Detailprüfung:**
- Klangliche Ähnlichkeit: Vokal- und Silbenstruktur, Akzentuierung, dominierender Bestandteil
- Schriftbildliche Ähnlichkeit: Buchstabenfolge, Länge, Groß-/Kleinschreibung
- Konzeptionelle Ähnlichkeit: Bedeutungsgehalt; bei Fantasiebegriffen ohne Bedeutung entfällt dieser Aspekt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 4. Risikobewertung erstellen

Jede kollidierende Voreintragung mit Ampelfarbe bewerten:

🔴 **Blocking (hohes Risiko):** Identische oder sehr ähnliche Marke in identischen/ähnlichen Klassen; starke Kennzeichnungskraft; anwaltliche Empfehlung: Anmeldung ohne Umgestaltung nicht empfehlenswert.

🟠 **Hoch:** Ähnliche Marke; Verwechslungsgefahr nicht ausschließbar; Abstandsvergrößerung prüfen; Anmeldeentscheidung nach anwaltlicher Würdigung.

🟡 **Mittel:** Einige Ähnlichkeiten; Verwechslungsgefahr zweifelhaft; Recherche nach weiteren Belegen; ggf. Koexistenzvereinbarung möglich.

🟢 **Niedrig:** Nur entfernte Ähnlichkeit; Klassen-/Warenabstand deutlich; geringe Risiken verbleiben; für abschließende Beurteilung Anwalt erforderlich.

### 5. Ausgabe erstellen

Recherchebericht mit:
- Zusammenfassung der verwendeten Datenbanken und Rechercheparameter
- Tabelle der gefundenen kollidierenden Zeichen (mit Registernummern, Inhabern, Klassen, Bewertung)
- Analyse der Top-3-Risikotreffer im Gutachtenstil
- Offene Fragen für Anwalt
- Entscheidungsbaum

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

**Normen:** §§ 4, 5, 8, 9, 14, 26 MarkenG; Art. 7, 8 VO (EU) 2017/1001 (UMV).

**Leitentscheidungen:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 9 Rn. 165 ff.; § 14 Rn. 345 ff. `[Modellwissen – prüfen; neuere Rspr. beachten]`
- Ströbele/Hacker/Thiering, MarkenG, 13. Aufl. 2021, § 9 Rn. 95 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

**Clearance-Report:** Tabellarische Zusammenfassung der Rechercheergebnisse (Zeichen, Inhaber, Klassen, Risikobewertung), gefolgt von Einzelanalyse der 🔴/🟠-Treffer im Gutachtenstil, Offene-Punkte-Liste, Entscheidungsbaum.

## Beispiel (Gutachtenstil)

**Geplantes Zeichen:** NORDBLATT, angemeldet für Kl. 25 (Bekleidung), Kl. 35 (Einzelhandel)

**Recherche DPMAregister:** Treffer: "NORDBLATT" (DPMA-Reg.-Nr. 30 2015 053 422), Inhaber: N.N. GmbH, Kl. 25, Status: eingetragen.

**Analyse:**

*Zeichenähnlichkeit:* Klangliche, schriftbildliche und konzeptionelle Identität (identische Wortmarke). Höchste Ähnlichkeitsstufe.

*Waren-/Dienstleistungsähnlichkeit:* Kl. 25 identisch.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

🔴 **Bewertung: Blocking.** Identische Eintragung in identischer Klasse. Anmeldung unter diesem Zeichen nicht empfehlenswert ohne Abstandsvergrößerung oder vorherige Freigabe durch Inhaber.

## Risiken / typische Fehler

- **Nur DPMA prüfen:** Unionsmarken haben automatisch Wirkung in Deutschland; EUIPO-Recherche ist Pflicht.
- **Klassen zu eng ansetzen:** Ähnliche Waren in Nachbarklassen können Verwechslungsgefahr begründen; nicht nur Wunschklassen, sondern auch benachbarte prüfen.
- **Benutzungsschonfrist ignorieren:** Ältere Marken, die nicht ernsthaft benutzt werden (§ 26 MarkenG), können auf Löschungsantrag angegriffen werden; eingetragene, aber nichtbenutzte Marken sind kein absolutes Hindernis.
- **Unregistrierte Rechte übersehen:** Firmennamen (§ 5 Abs. 2 MarkenG), Werktitel (§ 5 Abs. 3 MarkenG), bekannte Marken (§ 4 Nr. 3 MarkenG) schützen auch ohne Eintragung.
- **Dieses Ergebnis ist kein Freigabegutachten:** Die Bewertung ist eine Erste-Triage. Eine abschließende Freigabeentscheidung erfordert anwaltliche Prüfung; für wichtige Marken kommt ein formelles Gutachten in Betracht.

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `open-source-pruefung`

**Fokus:** Unternehmen will Software ausliefern oder als Open Source veroffentlichen und fragt nach Lizenz-Compliance. Open-Source-Lizenz-Compliance. Prüfraster: Manifest SBOM Repository Copyleft-Pflichten Lizenzkompatibilitaet GPL LGPL MIT Apache genehmigungsfähige Bibliotheken. Output: Compliance-Bericht mit Handlungsempfehlungen je Abhaengigkeit. Abgrenzung zu ip-klausel-prüfung (vertragliche IP) und fto-triage (Patente).

# Open-Source-Lizenz-Compliance-Prüfung

## Zweck

Diese Skill teilt mit, welche Lizenzen im Abhängigkeitsbaum enthalten sind, welche Pflichten diese Lizenzen angesichts des Einsatzmodells auslösen, und was für jede einzelne Abhängigkeit zu tun ist: Pflichten erfüllen, ersetzen, entfernen, anwaltliche Prüfung einholen oder kommerzielle Lizenz beschaffen.

Dies ist eine Erstklassifikation. Copyleft-Analysen hängen vom Einsatzmodell, der Einbindungstiefe, der Rechtsordnung und bisweilen von noch nicht gerichtlich geklärten Rechtsfragen ab (insbesondere AGPL-Netzwerktrigger, GPL-3.0-Patentklausel). Alles was als starkes Copyleft oder unklare Lizenz eingestuft wird, geht vor Auslieferung oder Veröffentlichung an einen Rechtsanwalt. Die Skill liefert den Befund; der Anwalt entscheidet.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

1. **Was wird geprüft?**
 - Abhängigkeitsliste (`package.json`, `requirements.txt`, `go.mod`, `Gemfile`, `Cargo.toml`, `pom.xml`, SBOM nach SPDX / CycloneDX, Lockfile)
 - Einzelne Bibliothek — ein konkretes Paket, das hinzugefügt werden soll
 - Eigener Code — Vorbereitung zur Open-Source-Veröffentlichung

2. **Einsatzmodell** (vor Klassifikation der Pflichten zwingend festlegen):
 - SaaS / gehosteter Dienst — Nutzer greifen über Netz zu; kein Code wird ausgeliefert
 - Distribuiertes Programm — kompilierter Code wird ausgeliefert (Desktop-App, Mobile-App, On-Prem-Server, CLI)
 - Nur intern — ausschließlich im Unternehmen genutzt, keine Auslieferung nach außen
 - Eingebettet / Firmware — ausgeliefert in Hardware oder als Closed-System-Firmware

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 69a ff. UrhG** — Urheberrechtsschutz für Computerprogramme; § 69b UrhG Arbeitnehmerprogramme
- **§ 31 Abs. 1 UrhG** — Einfaches und ausschließliches Nutzungsrecht; Copyleft-Lizenzen räumen einfache Nutzungsrechte unter Bedingungen ein
- **§ 31 Abs. 5 UrhG** — Zweckübertragungslehre: Im Zweifel nur für Vertragszweck erforderliche Rechte; Copyleft-Bedingungen müssen explizit akzeptiert werden
- **§ 97 UrhG** — Unterlassungs- und Schadensersatzanspruch bei Lizenzverletzung; Grundlage für GPL-Enforcement-Klagen
- **§§ 14, 15 UrhG** — Bearbeitungsrecht, Verwertungsrechte; Copyleft wirkt über das Bearbeitungsrecht

### Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Spindler, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 69a Rn. 1 (Softwareschutz allgemein)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Dreier, in: Dreier/Schulze, UrhG, 7. Aufl. 2022, § 31 Rn. 60 (Nutzungsrechtseinräumung, Copyleft-Mechanismus)
- Metzger/Jaeger, Open Source Software und deutsches Urheberrecht, GRUR Int. 1999, 839 (847) — Grundlagenaufsatz zur Wirksamkeit der GPL nach deutschem Recht

## Ablauf

### Schritt 1: Prüfungsumfang klären

Aus dem Übergabematerial ableiten oder fragen:

- Abhängigkeitsliste → alle Einträge klassifizieren, Pflichten aufrollen
- Einzelbibliothek → ein Paket klassifizieren, transitive Abhängigkeiten soweit verfügbar
- Ausgehender Code → Was ist eingebettet (direkt und transitiv)? Ist die gewählte Ausgangslizenz mit allen eingebetteten Lizenzen kompatibel? Sind LICENSE/NOTICE-Dateien korrekt?

### Schritt 2: Einsatzmodell festlegen

Das Einsatzmodell bestimmt, welche Copyleft-Pflichten ausgelöst werden:

| Einsatzmodell | Wesentliche Lizenzen |
|---|---|
| SaaS | AGPL-3.0 (Netzwerktrigger), Attribution bei Permissive in der UI, SSPL/BUSL/Elastic bei konkurrierendem Dienst |
| Distribuiertes Programm | GPL-2.0, GPL-3.0, LGPL, MPL, EPL (alle greifen bei Distribution); Permissive Attribution |
| Nur intern | Kein Copyleft-Auslöser bei interner Nutzung ohne Distribution. AGPL greift dennoch, wenn externe Nutzer über Netz zugreifen. Permissive Attribution gute Praxis. |
| Embedded / Firmware | GPL besonders schwer erfüllbar (Quellcodeoffenlegung + reproduzierbarer Build + Installationsinfo); vor Auslieferung planen |

Einsatzmodell im Ausgabevermerk kennzeichnen.

### Schritt 3: Jede Abhängigkeit klassifizieren

Nicht nur Metadaten lesen — tatsächlichen Lizenztext prüfen. LICENSE-Dateien können falsch sein; Package-Metadaten können veraltet sein.

Klassifikation:

| Kategorie | Beispiele | Wesentliche Pflichten |
|---|---|---|
| **Permissiv** | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC | Attribution, Lizenztextbeibehaltung; Apache-2.0 ergänzend Patentlizenz + NOTICE-Pflicht |
| **Schwaches Copyleft** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-1.0, EPL-2.0, CDDL | Datei- oder bibliotheksweite Quellcodeoffenlegung; Verlinkungsregeln variieren |
| **Starkes Copyleft** | GPL-2.0, GPL-3.0, AGPL-3.0, OSL, EUPL (je nach Version) | Breite Quellcodeoffenlegung; AGPL erstreckt sich auf Netzwerknutzung |
| **Public Domain / Widmung** | CC0, Unlicense, WTFPL | Keine Pflichten; aber: Public-Domain-Widmung nicht in allen Rechtsordnungen anerkannt (in Deutschland fraglich, §§ 29, 64 UrhG) |
| **Nicht-OSI Source-Available** | SSPL, BUSL, Commons Clause, Elastic License, Fair Source | Kein Open Source — schränken kommerzielle oder konkurrierende Nutzung ein; Lizenztext lesen |
| **Unbekannt / Proprietär** | Vendor-spezifisch, fehlendes Lizenz-File, Widerspruch File vs. Headers | Stopp — nicht als Permissiv behandeln |

Besonders kennzeichnen:

- **Dual-lizenzierte Pakete** — welche Lizenz nutzen wir? Wahl kann Pflichten ändern.
- **Veraltete Pakete** — kein aktiver Maintainer; gibt es einen gepflegten Ersatz?
- **Copyleft in transitiver Abhängigkeit** — Toplevel-Lizenz ist permissiv, aber eine transitive Abhängigkeit ist Copyleft.
- **Lizenswechsel bei bekannten Projekten** — Redis, MongoDB, Elastic, HashiCorp haben relizenziert; angepinnte Version prüfen.

### Schritt 4: Pflichten auf Einsatzmodell abbilden

Für jedes klassifizierte Paket:

```markdown
### [Paket@Version] — [Lizenz]

**Klassifikation:** [Permissiv / Schwaches Copyleft / Starkes Copyleft / Public Domain / Nicht-OSI / Unbekannt]

**Pflichten für unser Einsatzmodell ([SaaS / Distribuiert / Intern / Embedded]):**

- [ ] [Konkrete Pflicht — z. B. "Attribution in NOTICES-Datei, die mit der App ausgeliefert wird"]
- [ ] [z. B. "Bei Modifikation und Distribution: Quellcode der Änderungen veröffentlichen"]
- [ ] [z. B. "AGPL-Netzwerktrigger — wenn Nutzer über Netz auf unsere modifizierte Version zugreifen, Quellcode anbieten"]

**Risiko:** 🔴 Kritisch | 🟠 Hoch | 🟡 Mittel | 🟢 Niedrig

**Empfehlung:** [Pflichten erfüllen | Ersetzen durch [Alternative] | Entfernen | Anwaltliche Prüfung vor Auslieferung | Kommerzielle Lizenz bei [Anbieter] beschaffen]
```

**Verlinkungsbeziehung bestimmt den Schweregrad:**

- **Statische Verlinkung / gemeinsame Kompilierung:** Werke zu einem Binary vereint. Starkes Signal für Copyleft-Auslösung.
- **Dynamische Verlinkung / Shared Library:** Werke zur Laufzeit trennbar. LGPL explizit erlaubt (§ 6 LGPL — "work that uses the Library"). GPL-Position umstritten.
- **Header-Einbindung / Inline-Funktionen:** Kann abhängig von Einbindungstiefe ein abgeleitetes Werk begründen.
- **Subprozess / IPC:** Getrennte Prozesse über wohldefinierte Schnittstellen. Im Regelfall kein abgeleitetes Werk.
- **Netzwerk-API-Aufruf:** Für die meisten Lizenzen kein Auslöser. Für **AGPL-3.0**: Bereitstellung der Software über Netz gilt als Verbreitung — auch AGPL-Komponente hinter einer API triggert in einer Microservice-Architektur.
- **Dateiweises Copyleft (MPL):** Nur modifizierte Dateien tragen das Copyleft, nicht das gesamte Werk.

**Schweregrad-Kalibrierung:**

| Stufe | Bedeutung |
|---|---|
| 🔴 Kritisch | Starkes Copyleft in einem Einsatzmodell, das es auslöst (GPL in distribuiertem Binary, AGPL in SaaS). Nicht-OSI-Lizenz, die dem Geschäftsmodell widerspricht (z. B. SSPL bei gebautem verwaltetem Dienst). Lizenz nicht bestimmbar bei tragender Abhängigkeit. |
| 🟠 Hoch | Schwaches Copyleft mit Pflichten, die noch nicht eingerichtet sind (Dateilevel-Disclosure, NOTICE-Anforderungen). Dual-lizenziert mit unklarer Lizenzwahl. Lizenzdatei widerspricht File-Headern. |
| 🟡 Mittel | Permissiv mit noch nicht umgesetzten Attributionspflichten (fehlende NOTICES-Datei). Transitive Copyleft-Abhängigkeit, die je nach Einbindung greifen kann oder nicht. |
| 🟢 Niedrig | Permissiv mit bereits erfüllten Pflichten. Copyleft in einem Einsatzmodell, das es nicht auslöst (GPL-Bibliothek nur intern, keine Distribution). |

### Schritt 5: Kritische Befunde am Anfang des Vermerks kennzeichnen

- **Lizenz unbekannt** — als "Prüfung erforderlich" klassifizieren, nicht als Permissiv. Unklassifizierte Abhängigkeit sollte eine Lieferentscheidung aufhalten.
- **Lizenzdatei widerspricht File-Headern** — beide lesen und Widerspruch melden.
- **Inkompatible Kombinationen** — GPL-2.0-only + Apache-2.0 historisch bekannte Inkompatibilität; MPL / EPL / GPL-Kombinationen sorgfältig prüfen.
- **Nicht-OSI-Lizenzen als Open Source getarnt** — SSPL, BUSL, Commons Clause, Elastic License. Lizenztexte lesen; nicht dem GitHub-"Open Source"-Badge vertrauen.
- **Lizenswechsel** — wenn Vorgängerversion permissiv und aktuelle Version Source-Available ist: angepinnte Version entscheidet.

### Schritt 6: Ausgehende Prüfung (nur bei Code-Veröffentlichung als Open Source)

- Gewählte Ausgangslizenz mit jeder eingebetteten Abhängigkeitslizenz kompatibel? (Kein MIT-Release bei eingebettetem GPL-Code möglich — das kombinierte Werk muss GPL sein)
- LICENSE-Datei vorhanden und korrekt?
- NOTICE-Datei vorhanden mit erforderlichen Attributionen (Apache-2.0 u. a.)?
- Drittlizenz-Texte gebearbeitet wo erforderlich?
- Kein proprietärer oder vertraulicher Code, keine Kundendaten, keine eingebetteten Zugangsdaten in der Repository-History?
- Marken- und Markenrechtsrichtlinien für den Projektnamen geprüft (getrennt von der Urheberrechtslizenz)?

### Schritt 7: Vermerk zusammenstellen

```markdown
[ARBEITSERGEBNIS-KOPFZEILE]

# OSS-Lizenz-Prüfung: [Projekt / Abhängigkeitsliste / Paket]

**Geprüft:** [Datum]
**Umfang:** [Abhängigkeitsliste / Einzelbibliothek / Ausgehender Code]
**Einsatzmodell:** [SaaS / Distribuiert / Intern / Embedded]

---

## Ergebnis

[Zwei Sätze. Kann ausgeliefert werden? Was muss zuerst passieren?]

**Geprüfte Pakete:** [N]
**Nach Klassifikation:** [N permissiv, N schwaches Copyleft, N starkes Copyleft, N Public Domain, N Nicht-OSI, N unbekannt]
**Befunde:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Genehmigung erforderlich von:** [Name, gemäß Mandatsprofil]

---

## Kritische Anfangshinweise

[Unbekannte Lizenzen, Lizenz-Konflikte, Nicht-OSI als OSS getarnt, inkompatible Kombinationen]

---

## Nach Paket

[Blöcke aus Schritt 4, nach Schweregrad gruppiert]

---

## Rechtsordnungshinweis

OSS-Lizenz-Durchsetzbarkeit variiert: Der AGPL-Netzwerkauslöser ist in Deutschland grundsätzlich durchsetzbar (vgl. LG München I); Public-Domain-Widmungen sind im deutschen Recht problematisch (§§ 29, 64 UrhG — kein vollständiger Rechteentzug möglich, nur schuldrechtliche Abreden). Anwendbares Recht für Downstream-Distribution (z. B. bei Kunden in anderen Jurisdiktionen) und Mandatsprofil-Flaggen beachten.

---

## Ausgehende Prüfung (soweit einschlägig)

[Aus Schritt 6]

---

## Weiterleitungshinweise

[Wer genehmigt; was löst automatische Eskalation aus]
```

## Ausgabeformat

Vermerk mit Arbeitsergebnis-Kopfzeile, Gesamtbewertung, kritischen Anfangshinweisen, Paketblöcken nach Schweregrad, Rechtsordnungshinweis, ausgehende Prüfung (falls einschlägig), Weiterleitungshinweise.

## Beispiel

**Eingabe:** `requirements.txt` eines Python-SaaS-Projekts enthält `flask-login` (MIT), `celery` (BSD-3-Clause), `cryptography` (Apache-2.0/BSD), `mysqlclient` (GPL-2.0).

**Befund (Auszug):**

> ### mysqlclient@2.1.1 — GPL-2.0
>
> **Klassifikation:** Starkes Copyleft
>
> **Pflichten für unser Einsatzmodell (SaaS):**
> - [ ] Kein Distributions-Auslöser bei reiner SaaS-Nutzung — Quellcodeoffenlegungspflicht der GPL trifft grundsätzlich auf physische Distribution
> - [ ] AGPL-Auslöser gilt nicht für GPL-2.0 — jedoch: falls künftig Binary ausgeliefert wird, entsteht Pflicht
> - [ ] Kommerziell: MySQL Connector/Python (proprietäre Lizenz) oder `PyMySQL` (MIT) als Alternative prüfen
>
> **Risiko:** 🟡 Mittel (SaaS ohne Distribution) / 🔴 Kritisch (bei künftiger Binary-Distribution)
>
> **Empfehlung:** Ersetzen durch `PyMySQL` (MIT) zur Risikominimierung; alternativ anwaltliche Prüfung ob SaaS-Einsatz tatsächlich GPL-frei bleibt.

## Risiken und typische Fehler

- **GPL-Durchsetzbarkeit in Deutschland unterschätzen:** Deutsche Gerichte haben GPL-Bedingungen konsequent durchgesetzt (LG München I, BGH). Verstöße führen automatisch zum Verlust des Nutzungsrechts.
- **AGPL-Netzwerkauslöser ignorieren:** Bei SaaS-Anwendungen, die AGPL-Komponenten nutzen, muss der gesamte Quellcode den Nutzern angeboten werden — auch ohne physische Distribution.
- **Public Domain im deutschen Recht:** § 64 UrhG: Urheberrecht erlischt 70 Jahre nach Tod des Urhebers. Eine "Widmung" in die Gemeinfreiheit ist deutschrechtlich nicht vollständig möglich; CC0 ist die bestmögliche Annäherung.
- **Dynamische vs. statische Verlinkung:** Gleiche Lizenz, entgegengesetztes Ergebnis. LGPL + statisch gelinkt = 🔴; LGPL + dynamisch gelinkt = 🟢.
- **Lizenswechsel nicht erkannt:** Angepinnte Version bestimmt die Lizenz — nicht die aktuelle Upstream-Version.

## Quellenpflicht

Alle Klassifikationen und Pflichtaussagen müssen belegbar sein:

- **Gesetze:** §§ 31, 69a, 97 UrhG
- **Rechtsprechung:** mindestens eine Entscheidung zur GPL-Durchsetzbarkeit (LG München I oder BGH Afterlife)
- **Lizenztext:** direkt aus dem Repository oder SPDX; als `[Lizenztext gelesen — [Quelle]]` kennzeichnen
- **Kommentar oder Aufsatz:** Schricker/Löwenheim UrhG oder Metzger/Jaeger GRUR Int. 1999 mit Seitenangabe
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen vor Open-Source-Pruefung

Bevor die Lizenz-Compliance-Analyse beginnt, klaere:
1. Handelt es sich um statische oder dynamische Verlinkung (entscheidend fuer GPL vs. LGPL-Frage)?
2. Wird die Software als SaaS-Dienst betrieben (AGPL: Netzwerk-Austauschklausel — Quellcode-Pflicht auch ohne Distribution)?
3. Sind alle Abhaengigkeiten in der Dependency-Liste erfasst (transitive Dependencies often missed)?
4. Ist ein SBOM (Software Bill of Materials) erstellt (Compliance-Dokumentation, EU Cyber Resilience Act)?

## Aktuelle Rechtsprechung

> Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
