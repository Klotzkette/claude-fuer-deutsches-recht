---
name: dma-business-user-gatekeeper
description: "Business User Gatekeeper: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Business User Gatekeeper

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Business User Gatekeeper** im Plugin DSA/DMA Digitalregulierung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dma-business-user-zugang-spezial` | Spezialfall Business-User-Zugang zu Daten und Tools Art. 6 Abs. 9 ff. DMA: Datenportabilitaet in Echtzeit, FRAND-Zugang zu Schnittstellen und Funktionen, Reporting. Pruefraster fuer Drittanbieter und Verhandlung mit Gatekeeper. |
| `dma-gatekeeper-schwellen-und-kernplattformdienste` | Gatekeeper-Designation nach Art. 3 DMA prüfen: Plattform-Betreiber will wissen ob DMA-Pflichten gelten oder Kommission hat Designation eingeleitet. Normen: DMA (EU) 2022/1925 Art. 3 (Designation-Voraussetzungen), Art. 2 Nr. 2 DMA (Kernplattformdienste-Katalog), Art. 5-7 DMA (Pflichten). Prüfraster: Quantitative Schwellen (Umsatz EWR 7.5 Mrd. EUR oder Marktwert 75 Mrd. EUR, 45 Mio. Endnutzer, 10000 gewerbliche Nutzer), Kernplattformdienst-Einordnung, Gatekeeper-Pflichten. Output Designation-Prüfschema, Pflichten-Überblick. Abgrenzung: Nichtigkeitsklage gegen Designation siehe klage-gegen-vlop-einordnung-art-263-aeuv; DSA VLOP siehe dsa-vlop-vlose-einordnung-und-pflichten. |
| `dma-interoperabilitaet-messenger-art-7` | Interoperabilitaet von Messengerdiensten nach Art. 7 DMA: Pflicht der Gatekeeper (WhatsApp, iMessage), interoperable Schnittstellen anzubieten. Stufenmodell: 1:1 zuerst, dann Gruppen, dann Sprache/Video. Technische Spezifikationen, Verschluesselung, Spam-Schutz. Antrag eines Drittanbieters auf Interoperabilitaet und Vertragsgestaltung. |

## Arbeitsweg

Im Plugin DSA/DMA Digitalregulierung gilt für **Business User Gatekeeper**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dma-business-user-zugang-spezial`

**Fokus:** Spezialfall Business-User-Zugang zu Daten und Tools Art. 6 Abs. 9 ff. DMA: Datenportabilitaet in Echtzeit, FRAND-Zugang zu Schnittstellen und Funktionen, Reporting. Pruefraster fuer Drittanbieter und Verhandlung mit Gatekeeper.

# DMA: Business-User-Zugang

## Spezialwissen: DMA: Business-User-Zugang
- **Spezialgegenstand:** DMA: Business-User-Zugang / dma business user zugang spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 6, DMA, FRAND.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `dma-gatekeeper-schwellen-und-kernplattformdienste`

**Fokus:** Gatekeeper-Designation nach Art. 3 DMA prüfen: Plattform-Betreiber will wissen ob DMA-Pflichten gelten oder Kommission hat Designation eingeleitet. Normen: DMA (EU) 2022/1925 Art. 3 (Designation-Voraussetzungen), Art. 2 Nr. 2 DMA (Kernplattformdienste-Katalog), Art. 5-7 DMA (Pflichten). Prüfraster: Quantitative Schwellen (Umsatz EWR 7.5 Mrd. EUR oder Marktwert 75 Mrd. EUR, 45 Mio. Endnutzer, 10000 gewerbliche Nutzer), Kernplattformdienst-Einordnung, Gatekeeper-Pflichten. Output Designation-Prüfschema, Pflichten-Überblick. Abgrenzung: Nichtigkeitsklage gegen Designation siehe klage-gegen-vlop-einordnung-art-263-aeuv; DSA VLOP siehe dsa-vlop-vlose-einordnung-und-pflichten.

# DMA — Gatekeeper-Schwellen und Kernplattformdienste

## Drei kumulative Voraussetzungen (Art. 3 Abs. 1 DMA)

Ein Unternehmen wird als Gatekeeper benannt, wenn es bezogen auf einen Kernplattformdienst (KPD):

1. **erhebliche Auswirkungen auf den Binnenmarkt** hat (a)
2. **als wichtiges Zugangstor** für gewerbliche Nutzer zu Endnutzern dient (b)
3. **eine gefestigte und dauerhafte Position** hat oder voraussichtlich erlangen wird (c)

## Quantitative Vermutungen (Art. 3 Abs. 2 DMA)

Die drei Tatbestände werden vermutet, wenn:

| Voraussetzung | Quantitative Schwelle |
|---|---|
| a) Binnenmarkt-Auswirkung | Jahresumsatz im EWR ≥ **7.5 Mrd. EUR** in den letzten drei Geschäftsjahren **oder** durchschnittliche Marktkapitalisierung ≥ **75 Mrd. EUR**; Dienst in mindestens drei Mitgliedstaaten |
| b) Zugangstor | im letzten Geschäftsjahr ≥ **45 Mio. monatlich aktive Endnutzer** mit Sitz in der EU **und** ≥ **10000 jährlich aktive gewerbliche Nutzer** mit Sitz in der EU |
| c) Gefestigte Position | Schwellen unter b) in den **letzten drei Geschäftsjahren** erreicht |

Auch ohne Erreichen der quantitativen Schwellen kann die Kommission ein Unternehmen nach **qualitativer Marktuntersuchung** nach Art. 3 Abs. 8 DMA designieren.

## Kernplattformdienste (Art. 2 Nr. 2 DMA — abschließende Liste)

1. Online-Vermittlungsdienste
2. Online-Suchmaschinen
3. Online-Soziale-Netzwerk-Dienste
4. Video-Sharing-Plattform-Dienste
5. Nummernunabhängige interpersonelle Kommunikationsdienste
6. Betriebssysteme
7. Webbrowser
8. Virtuelle Assistenten
9. Cloud-Computing-Dienste
10. Online-Werbedienste

Designiert wird je Kernplattformdienst — ein Unternehmen kann mehrere KPDs gleichzeitig betreiben.

## Verfahren

1. Unternehmen muss bei Erreichen der quantitativen Schwellen **innerhalb von zwei Monaten** die Kommission unterrichten (Art. 3 Abs. 3 DMA)
2. Kommission designiert innerhalb von **45 Arbeitstagen** ab Erhalt der vollständigen Angaben (Art. 3 Abs. 4)
3. Pflichten greifen **sechs Monate nach Designation** (Art. 3 Abs. 10)
4. Designation wird **alle drei Jahre** überprüft (Art. 4 DMA)

Stand 2026: in den ersten Tranchen wurden mehrere Big-Tech-Konzerne als Gatekeeper für insgesamt deutlich über 20 Kernplattformdienste benannt.

## Pflichten (Art. 5 bis 7 DMA — Auswahl)

| Norm | Pflicht |
|---|---|
| Art. 5 Abs. 2 | **Kein Cross-Use von Daten** über KPDs hinweg ohne ausdrückliche Einwilligung |
| Art. 5 Abs. 3 | **Most-Favoured-Nation-Verbot** für gewerbliche Nutzer |
| Art. 5 Abs. 4 | **Anti-Steering**-Verbot (gewerbliche Nutzer dürfen Endnutzer auf alternative Angebote hinweisen) |
| Art. 5 Abs. 7 | **Browser-/Suchmaschinen-Auswahlbildschirm** beim Betriebssystem |
| Art. 6 Abs. 2 | **Verbot des Self-Preferencing** in Ranking |
| Art. 6 Abs. 3 | **Deinstallierbarkeit** vorinstallierter Apps |
| Art. 6 Abs. 4 | **Sideloading** und Interoperabilität von Drittstores auf Betriebssystemen |
| Art. 6 Abs. 7 | **Interoperabilität** mit Hardware-/Softwarefunktionen |
| Art. 7 | **Interoperabilität interpersoneller Kommunikationsdienste** (Messenger) |

## Sanktionen

- Geldbußen bis **10 % des weltweiten Jahresumsatzes**, im Wiederholungsfall **20 %** (Art. 30 DMA)
- Zwangsgelder bis 5 % des täglichen Umsatzes (Art. 31)
- Bei systematischer Nichtbefolgung: **strukturelle Maßnahmen** möglich, einschließlich Veräußerung von Unternehmensteilen (Art. 18)

## Schnittstellen

- DMA gilt **zusätzlich** zu Art. 101 / 102 AEUV (Art. 1 Abs. 6 DMA)
- Nationales Recht: § 19a GWB erfasst teilweise engere Sachverhalte
- DSGVO und DSA gelten parallel
- P2B-VO greift im Verhältnis Plattform — gewerblicher Nutzer ergänzend

## Aktuelle Rechtsprechung

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **Designation-Liste:** Aktuelle Liste der designierten Gatekeeper und ihrer Kernplattformdienste live ueber digital-markets-act.ec.europa.eu/gatekeepers_en pruefen. Stand 2026: mehrere Big-Tech-Konzerne designiert, jeweils fuer einen oder mehrere Kernplattformdienste (Suchmaschinen, App-Stores, Videoplattformen, soziale Netzwerke, Messenger, Online-Vermittlung, Werbedienste, Browser, Betriebssysteme).
- **Erste Sanktionsverfahren:** Kommission hat seit 2024 mehrere Nichteinhaltungs-Untersuchungen gegen Gatekeeper eroeffnet (insb. zu Anti-Steering Art. 5 Abs. 4, Self-Preferencing Art. 6 Abs. 2, Sideloading Art. 6 Abs. 4). Aktuelle Pressemitteilungen und Entscheidungen live ueber ec.europa.eu/competition pruefen.
- **EuG-/EuGH-Klagen Art. 263 AEUV:** Designation-Beschluesse und Compliance-Anordnungen werden von Gatekeepern angefochten. Konkrete Aktenzeichen und Verfahrensstand live ueber curia.europa.eu pruefen (Suche "DMA" / "Digital Markets Act").
- **Schnittstelle Art. 19a GWB:** § 19a GWB (besondere Missbrauchsaufsicht gegenueber Marktbeherrschern mit ueberragender marktuebergreifender Bedeutung) bleibt parallel anwendbar; BKartA-Beschluesse zu Verfuegungen nach § 19a GWB live ueber bundeskartellamt.de pruefen.

## Zentrale Normen (Paragrafenkette)

- Art. 3 DMA — Gatekeeper-Designation (quantitative Schwellen + qualitative Vermutung)
- Art. 2 Nr. 2 DMA — Kernplattformdienste-Katalog
- Art. 5–7 DMA — Per-se-Verbote und spezifizierbare Pflichten
- Art. 26 ff. DMA — Aufsicht durch Kommission

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Überschreitet der Anbieter die quantitativen Schwellen? (Umsatz EWR 7.5 Mrd. EUR / Marktwert 75 Mrd. / 45 Mio. EU-Nutzer / 10.000 Gewerbekunden)
2. Welcher Kernplattformdienst liegt vor? (Art. 2 Nr. 2 DMA: Vermittlungsdienst, Suchmaschine, SNS, Videoplattform, Messaging, Betriebssystem, Browser, Cloud, Werbedienste)
3. Ist der Anbieter bereits als Gatekeeper designiert?
4. Welche Pflichten aus Art. 5–7 DMA sind zu prüfen?

## Output-Template — Gatekeeper-Prüfvermerk

**Adressat:** Kanzlei intern / Rechtsabteilung — Tonfall: sachlich-juristisch

```
Gatekeeper-Prüfvermerk [DATUM]
Anbieter: [NAME]
Dienst: [KERNPLATTFORMDIENST, Art. 2 Nr. 2 DMA]

Quantitative Schwellen (Art. 3 Abs. 2 DMA):
Umsatz EWR: [BETRAG EUR] >= 7.5 Mrd.: ja / nein
Marktwert: [BETRAG EUR] >= 75 Mrd.: ja / nein
EU-Endnutzer: [ANZAHL] >= 45 Mio.: ja / nein
EU-Gewerbekunden: [ANZAHL] >= 10.000: ja / nein
Zeitraum (3 von 5 Jahren): ja / nein

Ergebnis: Quantitative Vermutung: JA / NEIN
Designation bereits erfolgt: ja (Beschluss vom [DATUM]) / nein / beantragt

Anwendbare Pflichten: Art. 5–7 DMA [LISTE EINSCHLAEGIGER PFLICHTEN]
Empfehlung: [BERATUNGSEMPFEHLUNG]
```

## 3. `dma-interoperabilitaet-messenger-art-7`

**Fokus:** Interoperabilitaet von Messengerdiensten nach Art. 7 DMA: Pflicht der Gatekeeper (WhatsApp, iMessage), interoperable Schnittstellen anzubieten. Stufenmodell: 1:1 zuerst, dann Gruppen, dann Sprache/Video. Technische Spezifikationen, Verschluesselung, Spam-Schutz. Antrag eines Drittanbieters auf Interoperabilitaet und Vertragsgestaltung.

# DMA: Messenger-Interoperabilitaet

## Spezialwissen: DMA: Messenger-Interoperabilitaet
- **Spezialgegenstand:** DMA: Messenger-Interoperabilitaet / dma interoperabilitaet messenger art 7. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 7, DMA.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
