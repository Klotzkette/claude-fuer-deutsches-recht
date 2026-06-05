---
name: airline-standardausreden-annullierung
description: "Airline Standardausreden Annullierung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Airline Standardausreden Annullierung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Airline Standardausreden Annullierung** im Plugin Fluggastrechte (VO 261/2004). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstruktionsfehler vorheriger Flugausfall Wetter Slot-Verschiebung Vogelschlag Versaeumung der Meldefrist Akzeptanz der Umbuchung Voucher als Erfuellung Zuständigkeitseinrede. Für Reaktion auf Airline-Ablehnungsschreiben in Skill `forderungsschreiben-mahnung` oder Klage. |
| `annullierung-oder-verspaetung-einordnen` | Prüffeld für annullierung oder verspaetung einordnen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `anschlussflug-und-reiseplan` | Prüffeld für anschlussflug und reiseplan: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Fluggastrechte (VO 261/2004) gilt für **Airline Standardausreden Annullierung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `airline-standardausreden-pruefen`

**Fokus:** Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstruktionsfehler vorheriger Flugausfall Wetter Slot-Verschiebung Vogelschlag Versaeumung der Meldefrist Akzeptanz der Umbuchung Voucher als Erfuellung Zuständigkeitseinrede. Für Reaktion auf Airline-Ablehnungsschreiben in Skill `forderungsschreiben-mahnung` oder Klage.

# Airline-Standardausreden — Katalog und Gegenargumente

## Beweislast

**Generell**: Beweislast für außergewöhnliche Umstände und für die Ergreifung aller zumutbaren Maßnahmen liegt bei der **Airline** (Art. 5 Abs. 3 VO 261/2004 — Wortlaut "nachweisen kann"). Pauschale Behauptungen ohne Belege reichen nicht.

## Katalog

### 1. "Technischer Defekt am Flugzeug"

**Airline-Argument**: technischer Defekt sei außergewöhnlich. Hilft uns nicht.

**Gegenargument**:

> EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — technische Defekte sind grundsaetzlich Teil der normalen Tätigkeit eines Luftfahrtunternehmens und kein außergewöhnlicher Umstand. Volltext auf curia.europa.eu vor Versand aufrufen und Randnummer (typisch Rn. 24 ff.) einsetzen.
>
> Ausnahme: versteckter Konstruktionsfehler des Herstellers — EuGH, Urt. v. 13.6.2025, C-411/23 (curia.europa.eu) — kann ausnahmsweise außergewöhnlich sein, auch wenn die Airline Monate vor dem Flug informiert war.

Nur ausnahmsweise gilt etwas anderes wenn zB ein vom Hersteller bekannt gegebener Fehler kurz vor dem Flug entdeckt wird oder Sabotage durch Dritte vorliegt.

### 2. "Wilder Streik unserer Mitarbeiter"

**Gegenargument**:

> Streiks der eigenen Mitarbeiter (auch "wilde Streiks") gehören zum betrieblichen Risikobereich der Airline. EuGH-Linie zum Personalmangel beziehungsweise Streik der eigenen Belegschaft konkret anhand offener Quelle (curia.europa.eu) und konkretem Aktenzeichen zitieren — nicht aus Modellwissen.

### 3. "Streik einer Gewerkschaft mit ordentlichem Aufruf"

**Differenziertes Bild**:

> Auch Streiks mit ordentlichem Gewerkschaftsaufruf liegen typischerweise im betrieblichen Risikobereich, soweit sie das eigene Personal betreffen. EuGH-Linie konkret aus curia.europa.eu mit Aktenzeichen und Randnummer einsetzen; nicht aus Modellwissen pauschalisieren.

Praktisch: oft im Detail strittig — Airlines berufen sich pauschal; aber zumutbare Maßnahmen sind regelmäßig nicht hinreichend dargelegt.

### 4. "Crew-Engpass — Crew nicht verfügbar"

**Gegenargument**:

> Crew-Mangel gehört zu den **typischen Betriebsrisiken** einer Airline. Reserve-Crews vorzuhalten ist ureigene Aufgabe; eine fehlende Reserve-Crew ist kein außergewöhnlicher Umstand.

### 5. "Vorheriger Flug verspätet — Kettenreaktion"

**Gegenargument**:

> EuGH ständige Rechtsprechung: Verspätungen die aus einer Kette der gleichen Maschine resultieren sind nur dann außergewöhnlich wenn der **erste** Vorgang in der Kette selbst außergewöhnlich war und die späteren Verspätungen sich daraus zwingend ergeben. Wenn der erste Vorflug aus Routine-Gründen verspätet war ist die Kette nicht außergewöhnlich.

### 6. "Wetterverhältnisse"

**Differenziert**:

> Extreme Wetterverhältnisse (Vulkanasche Hurrikan Schneesturm in untypischen Gebieten) sind außergewöhnlich. Normaler Schneefall im Winter in mitteleuropaeischen Regionen ist regelmäßig kein außergewöhnlicher Umstand — Schneeraeumung und Enteisung gehören zum normalen Betrieb.

### 7. "Slot-Verschiebung durch die Flugverkehrsleitung"

**Differenziert**:

> Wenn der Slot wegen kapazitätsbedingter Überlastung verschoben wird ist das **regelmäßig kein außergewöhnlicher Umstand** (Teil normalen Flugbetriebs). Bei Sicherheits- oder Wetterrücksichten kann die Bewertung anders ausfallen.

### 8. "Vogelschlag"

**Außergewöhnlich aber**:

> EuGH, Urt. v. 4.5.2017, C-315/15 (Pesková) — Vogelschlag ist grundsaetzlich außergewöhnlicher Umstand i.S.v. Art. 5 Abs. 3 VO 261/2004 (curia.europa.eu). Vor Versand Volltext aufrufen und Randnummer einsetzen.
>
> ABER: die Airline muss zusätzlich nachweisen dass alle **zumutbaren Maßnahmen** ergriffen wurden — z. B. zuegige technische Prüfung schnellstmögliche Wiederinbetriebnahme Umbuchung auf anderen Flug.

### 16. "Blitzschlag in das Flugzeug"

**Außergewöhnlich aber**:

> EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag mit nachfolgender sicherheitsbedingter Pruefung kann außergewöhnlicher Umstand sein (curia.europa.eu).
>
> ABER: zumutbare Maßnahmen sind weiterhin nachzuweisen (Ersatzflugzeug, Umbuchung, Information).

### 17. "Flug vorverlegt — keine Entschädigung"

**Gegenargument**:

> EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung eines Fluges um mehr als eine Stunde ist einer Annullierung gleichzusetzen. Ausgleichsanspruch nach Art. 7 VO 261/2004 entsteht (curia.europa.eu).

### 9. "Sie haben die Störung nicht binnen X Tagen gemeldet"

**Gegenargument**:

> Die VO 261/2004 sieht **keine** Anzeigefrist für die Geltendmachung des Anspruchs vor. Es gilt allein die **gesetzliche Verjährung** drei Jahre nach § 195 BGB iVm § 199 Abs. 1 BGB ab Schluss des Jahres in dem Anspruch entstand und Kenntnis vorlag.

### 10. "Sie haben die Umbuchung / Voucher akzeptiert"

**Gegenargument**:

> Akzeptanz einer Ersatzbeförderung schließt den Ausgleichsanspruch nach Art. 7 VO 261/2004 nicht aus. Anspruchsgrundlage Art. 7 ist eigenständig und greift parallel zur Erstattung oder Ersatzbeförderung (Art. 8 VO 261/2004).
>
> Voucher können Ausgleichsanspruch nur dann ersetzen wenn der Fluggast **schriftlich und ausdrücklich** auf seinen Ausgleichsanspruch verzichtet hat. Ein blosser Voucher-Erhalt ohne Verzichtserklärung ist kein Anspruchsverzicht.

### 11. "Wir sind nicht zuständig (Codeshare)"

**Gegenargument**:

> Nach Art. 2 lit. b VO 261/2004 ist Anspruchsgegner das **ausführende Luftfahrtunternehmen** (operating carrier) — nicht das vermarktende. Die ausführende Airline kann sich nicht auf Codeshare-Konstruktionen berufen um ihre Verpflichtung zu vermeiden.

### 12. "Sie haben uns die Daten nicht binnen 24 Stunden gegeben"

**Gegenargument**:

> Die VO 261/2004 enthält keine Frist für Verbraucher zur Geltendmachung. Auch interne Service-Richtlinien der Airline binden den Verbraucher nicht.

### 13. "Konzern-Beleg / Mitversorgung"

**Differenziert**: Wenn der Verbraucher kostenfreie Mahlzeit Hotel und Transport tatsächlich erhalten hat sind die Auslagenanspruechen nach Art. 9 VO 261/2004 erfüllt. Anspruch nach Art. 7 (Ausgleich) bleibt davon **unberuehrt**.

### 14. "Sie haben aus Komforterwägungen das Hotel selbst gebucht"

**Gegenargument**:

> Wenn die Airline kein Hotel angeboten hat oder das angebotene nicht akzeptabel war ist der Verbraucher zu eigenem Vorgehen berechtigt und die Airline schuldet Erstattung der **erforderlichen** Auslagen (Art. 9 VO 261/2004 — angemessenes Hotel inkl. Transfer).

### 15. "Sie waren nicht puenktlich am Check-in"

**Gegenargument**:

> Wer rechtzeitig am Check-in war (in der Regel 45 Minuten vor planmäßigem Abflug oder gemäß Airline-AGB) hat den Anspruch behalten. Beweis durch Boardingpass oder Check-in-Bestätigung.

## Versand-Hinweis

Diesen Katalog vor jedem Mahnungsschreiben durchgehen — Standardausreden mit Pinpoint kontern. Den entsprechenden Punkt **wortlautnah** zitieren mit Az der EuGH-Entscheidung.

## Ausgabe

- `airline-ausreden-gegenargumente.md` zur Vorbereitung von Mahnung oder Klage.
- Verweis auf entsprechenden Pinpoint im EuGH-Rspr-Katalog (`references/eugh-rechtsprechung-fluggastrechte.md`).

## 2. `annullierung-oder-verspaetung-einordnen`

**Fokus:** Prüffeld für annullierung oder verspaetung einordnen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Annullierung Verspätung oder Nichtbeförderung einordnen

## Drei Hauptkategorien

### 1. Annullierung (Art. 5 VO 261/2004)

Der **geplante Flug findet nicht statt** — die Airline streicht ihn. Indikatoren:

- Mitteilung der Airline "Flug annulliert / cancelled".
- Kein Flug mit der konkreten **Flugnummer und Datum** ist abgehoben.
- Passagiere werden auf einen anderen Flug umgebucht oder bekommen die Erstattung.

**Auch Annullierung** auch wenn der Flug am **nächsten Tag mit gleicher Flugnummer** stattfindet:

- EuGH, Urt. v. 13.10.2011, C-83/10 (Sousa Rodríguez) — eine Umkehr nach Start ohne Erreichen des Zielflughafens ist Annullierung (curia.europa.eu).
- EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung um mehr als eine Stunde ist Annullierung (curia.europa.eu).

### 2. Verspätung (Art. 6 VO 261/2004; Sturgeon-Linie)

Der **geplante Flug findet statt**, aber:

- **Mehr als zwei Stunden Verspätung** bei kurzen Strecken oder **mehr als drei Stunden** bei langen Strecken bei Abflug = Betreuungsleistungen Art. 9 VO 261/2004 (Verpflegung Telefon Hotel etc.).
- **Ankunftsverspätung am Endziel ≥ 3 Stunden** = Ausgleichsanspruch wie bei Annullierung (EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07, Sturgeon u.a. — curia.europa.eu; bestätigt EuGH, Urt. v. 23.10.2012, C-581/10 und C-629/10, Nelson u.a.).

**Wichtig**: Maßgeblich ist die **Ankunftsverspätung am Endziel** — nicht die Abflugverspätung.

### 3. Nichtbeförderung (Art. 4 VO 261/2004)

- Klassisch **Overbooking** — die Airline bucht mehr Plätze als verfügbar.
- Die Airline verweigert die Beförderung gegen den Willen des Passagiers.
- Voraussetzung: rechtzeitiges Erscheinen am Check-in (in der Regel 45 Minuten vor Abflug).
- Folge: Ausgleichsanspruch wie bei Annullierung + Wahl Erstattung oder anderweitige Beförderung.

**Nicht Nichtbeförderung** wenn Passagier ausgeschlossen wird wegen:
- Fehlender Reisedokumente (Pass Visum).
- Sicherheitsbedenken.
- Fluguntauglichkeit (medizinisch).

## Sonderfälle

### Anschlussflug ohne Anschluss

Wenn der **erste Flug innerhalb der EU mit derselben Buchung** verspätet ist und der **Anschlussflug verpasst** wird:

- EuGH, Urt. v. 31.5.2018, C-537/17 (Wegener / Royal Air Maroc) und EuGH, Urt. v. 11.7.2019, C-502/18 (CS Flug) — bei einheitlicher Buchung von Anschlussflügen kommt es für den Ausgleichsanspruch auf die Endziel-Ankunftsverspätung an (curia.europa.eu).
- Anspruch besteht auch wenn der erste Flug innerhalb der drei-Stunden-Schwelle landete, der Anschlussflug aber verpasst wurde und Endziel mit mehr als drei Stunden Verspätung erreicht wird.

### Ersatzflug am nächsten Tag

- **Annullierung** wenn Ersatzflug eine andere Flugnummer hat oder gravierende Änderungen aufweist.
- **Verspätung** wenn derselbe Flug nur verschoben und die Identität bewahrt ist (z. B. gleiches Flugzeug gleiche Crew gleiche Strecke).
- Konkrete Abgrenzungskriterien aus EuGH-Rechtsprechung (Volltext in curia.europa.eu vor Versand verifizieren).

### Vorverlegung des Flugs

- EuGH, Urt. v. 21.12.2021, C-146/20, C-188/20, C-196/20 — Vorverlegung um mehr als eine Stunde ist einer Annullierung gleichzustellen (curia.europa.eu).
- Bestätigt: EuGH, Urt. v. 9.1.2025, C-394/23 (curia.europa.eu).

### Umbuchung auf anderen Flug ohne Zustimmung des Passagiers

- Falls die Airline den Passagier auf einen anderen Flug umbucht (Codeshare anderen Tag andere Stadt): prüfen ob das wesentliche Änderung ist und damit als Annullierung gewertet wird.

## Prüfraster

```
1. Hat der geplante Flug exakt wie geplant stattgefunden?
 - Ja → keine Annullierung; Verspätung prüfen (Schritt 2)
 - Nein → Schritt 3

2. Welche Ankunftsverspätung am Endziel?
 - 0 bis unter 3 Stunden → keinen Ausgleichsanspruch nach VO 261;
 Betreuungsleistungen Art. 9 ggf. bei Abflugverspätung
 - 3 Stunden oder mehr → Ausgleichsanspruch wie bei Annullierung
 (EuGH Sturgeon)

3. Wie wurde der Flug geändert?
 - komplett ausgefallen → Annullierung
 - durchgeführt aber gravierend abweichend (Datum Flugnummer
 Zeitpunkt mehr als drei Stunden) → Annullierung
 - durchgeführt mit geringerer Verspätung → Verspätung prüfen
 - Passagier wurde am Gate abgewiesen trotz gültigem Ticket
 → Nichtbefoerderung

4. Stehen außergewöhnliche Umstaende entgegen?
 → Skill `ausnahmen-aussergewoehnliche-umstaende-pruefen`
```

## Ausgabe

- `einordnung.md` mit:
 - rechtlicher Kategorie (Annullierung / Verspätung / Nichtbeförderung)
 - Begründung mit Verweis auf Norm und EuGH-Rechtsprechung
 - Höhe der voraussichtlichen Ausgleichszahlung (verweist auf Skill `distanz-und-ausgleich-berechnen`)
 - offenen Fragen zur Klärung mit dem Mandanten
- Hinweis auf Skill `ausnahmen-aussergewoehnliche-umstaende-pruefen` zur Prüfung der Ausnahmen.

## 3. `anschlussflug-und-reiseplan`

**Fokus:** Prüffeld für anschlussflug und reiseplan: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Anschlussflug und Reiseplan

## Grundregel — Endziel zählt

Maßgeblich ist die st. Rspr. des EuGH (Volltext jeweils auf curia.europa.eu vor Versand aufrufen):

- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — bei einheitlicher Buchung mit Anschlussflug ist die Verspätung am Endziel maßgeblich.
- EuGH, Urt. v. 31.5.2018, C-537/17 (Wegener) — auch bei Anschlussflügen mit teilweisem Abflug außerhalb der EU.
- EuGH, Urt. v. 11.7.2019, C-502/18 (CS Flug) — bestätigend.

- Bei einer **einheitlichen Buchung** mit Anschlussflug ist maßgeblich die **Verspätung am Endziel** — nicht am Anschlussflughafen.
- Anspruch besteht auch wenn der erste Flug puenktlich war aber der Anschlussflug ausfällt und das Endziel mehr als drei Stunden verspätet erreicht wird.
- Umgekehrt: erster Flug verspätet aber kurz vor der Drei-Stunden-Schwelle aber Anschluss noch erreicht — kein Anspruch.

## Prüfraster

### 1. Wie ist gebucht?

- **Eine Buchung** (ein PNR mit allen Strecken) → Reise als ein Vorgang. Anspruch nach Endzielverspätung.
- **Separate Buchungen** (verschiedene PNRs gebucht z. B. weil mit verschiedenen Plattformen) → jeder Flug für sich; bei Verpassen des Anschlusses wegen Verspätung des ersten Flugs **keine Mitversicherung** im VO 261-Sinn. Anspruch nur für den **konkret betroffenen** Flug.

### 2. Wer ist Vertragspartner?

- **Operating Carrier** (ausführendes Luftfahrtunternehmen) ist Anspruchsgegner nach VO 261/2004.
- Bei Codeshare ist das ausführende Luftfahrtunternehmen anspruchsverpflichtet (Art. 2 lit. b VO 261/2004).
- **Vermarktendes Luftfahrtunternehmen** (Marketing Carrier) ist im Allgemeinen NICHT der Anspruchsgegner nach VO 261/2004 — auch wenn der Vertrag aus dem PNR mit ihm besteht.
- Bei Streit kann der Passagier **wahlweise** auch das vermarktende Luftfahrtunternehmen nach BGB-Vertragsregeln in Anspruch nehmen — anderer Anspruch (Reisevertrag).

### 3. Wo wird die Distanz gemessen?

- Bei Anschlussflug mit einheitlicher Buchung: Distanz vom Abgangsort bis zum Endziel auf Großkreis-Linie (Art. 7 Abs. 1 i.V.m. Art. 5 ff. VO 261/2004).
- Konkretisierende EuGH-Linie: EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) und EuGH, Urt. v. 7.9.2017, C-559/16 — Volltext auf curia.europa.eu prüfen.

### Beispiel

- **Berlin BER — Madrid MAD — Buenos Aires EZE** mit einheitlicher Buchung.
- Erster Flug BER-MAD puenktlich. Anschlussflug MAD-EZE annulliert. Ersatz am nächsten Tag.
- Endzielverspätung 28 Stunden.
- Distanz BER-EZE auf Großkreis 11.940 km nicht-innergemeinschaftlich.
- Stufe 3 — 600 EUR pro Passagier.

## Reiseverträge über Reiseveranstalter

- Bei **Pauschalreise** (§§ 651a ff. BGB) zusätzliche Ansprueche gegen den Reiseveranstalter (Minderung Schadensersatz nach BGB).
- VO 261/2004 Anspruch bleibt davon unberuehrt; Anspruchsgegner bleibt operating carrier.
- Doppelanspruch (Reiseveranstalter und Airline) — Vorteilsausgleich prüfen.

## Sonderfall Umsteigen über Drittstaat

Wenn die Reise innerhalb der EU mit Umsteigen in einem **Drittstaat** stattfindet (z. B. BER-IST-VIE bei Turkish Airlines):

- VO 261/2004 gilt nach Art. 3 für den **Abflug aus der EU** auch mit Nicht-EU-Carrier.
- Anschlussflug ab Drittstaat zurück in die EU mit Nicht-EU-Carrier: **VO 261 gilt NICHT**.
- Konsequenz: nur Anspruch für Abflug-Etappe ab EU.

## Eingaben

- Buchungsbestätigung mit allen Etappen.
- PNR-Kennung pro Etappe.
- IATA-Codes der drei oder mehr Flughaefen.
- Tatsächliche Abflug- und Ankunftszeiten je Etappe.

## Ausgabe

```
Anschlussflug-Analyse
Buchung: eine PNR (ABC123) über Lufthansa
Etappen:
 1. BER 12.05.2026 08:00 → MAD 12.05.2026 11:30 (LH 1234)
 2. MAD 12.05.2026 13:00 → EZE 13.05.2026 06:00 (LH 5678)

Stoerung:
 Etappe 2 annulliert
 Ersatz: EZE Ankunft 14.05.2026 10:00

Endzielverspätung: 28 Stunden
Distanz BER-EZE (Endziel): 11.940 km nicht-innergemeinschaftlich
Stufe: 3 → 600 EUR pro Passagier

Anspruchsgegner: Lufthansa (operating carrier Etappe 2)
```

## Leitentscheidungen Anschlussflug (Stand Mai 2026)

Verifiziert mit Quelle curia.europa.eu (Volltext jeweils vor Versand aufrufen):

- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — Endziel-Verspätung maßgeblich; auch wenn Hauptflug pünktlich war.
- EuGH, Urt. v. 31.5.2018, C-537/17 (Wegener) — einheitliche Buchung Anschluss in Drittstaat.
- EuGH, Urt. v. 11.7.2019, C-502/18 (CS Flug) — Anschlussflug-Konstellationen.
- EuGH, Urt. v. 21.12.2021, C-146/20, C-188/20, C-196/20 — Vorverlegung als Annullierung.
- EuGH, Urt. v. 9.1.2025, C-394/23 — bestätigend für Vorverlegung.
- EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag als außergewöhnlicher Umstand.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Hinweise

- Bei einheitlicher Buchung lohnt eine sorgfaeltige Prüfung — viele Airlines berechnen falsch.
- Bei separaten Buchungen Verlust des Anschlusses regelmäßig nicht erstattungsfähig nach VO 261 — daher bei Buchung auf Einheits-PNR achten.
