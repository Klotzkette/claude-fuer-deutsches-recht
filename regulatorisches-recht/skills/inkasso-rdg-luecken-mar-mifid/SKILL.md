---
name: inkasso-rdg-luecken-mar-mifid
description: "Inkasso RDG Luecken MAR Mifid: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inkasso RDG Luecken MAR Mifid

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Inkasso RDG Luecken MAR Mifid** im Plugin Regulatorisches Recht (Sektoren). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `inkasso-rdg` | Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg Inkassoerlaubnis Zulassung Aufsicht Kundenschutz. Output: RDG-Prüfmemo Erlaubnis-Empfehlung. Abgrenzung: nicht für anwaltliche Forderungseinziehung. |
| `luecken` | Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: nicht für Lueckenaufzeiger-Perspektive nach aussen (luecken-aufzeiger). |
| `mar-mifid-eltif-uebergreifend` | MAR-MiFID-ELTIF uebergreifend: Insiderhandel, Marktmanipulation, Geeignetheit, ELTIF 2.0 Retail-Vertrieb. Pruefraster ueber alle drei Regelwerke fuer einen typischen Produktentwicklungsfall. Schnittstellen und Konfliktpunkte. |

## Arbeitsweg

Im Plugin Regulatorisches Recht (Sektoren) gilt für **Inkasso RDG Luecken MAR Mifid**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `inkasso-rdg`

**Fokus:** Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg Inkassoerlaubnis Zulassung Aufsicht Kundenschutz. Output: RDG-Prüfmemo Erlaubnis-Empfehlung. Abgrenzung: nicht für anwaltliche Forderungseinziehung.

# Inkassodienstleistungen (RDG)

## Zweck

Dieser Skill begleitet die rechtskonforme Durchführung von Inkassodienstleistungen durch registrierte Inkassounternehmen (§ 10 Abs. 1 Nr. 1 RDG) und Rechtsanwälte (§ 43d BRAO). Er deckt Registrierungsvoraussetzungen, erlaubten Tätigkeitsumfang, Hinweispflichten gegenüber Schuldnern, Vergütungsfragen (§ 4 RDGEG) und die datenschutzkonforme Verarbeitung von Schuldnerdaten (Art. 6 Abs. 1 lit. f DSGVO) ab. Relevanz insb. für Legal-Tech-Geschäftsmodelle nach dem "LexFox"-Urteil des BGH. Anwendungsfälle: Mietpreisbremse-Durchsetzung durch Inkassounternehmen, Consumer-Inkasso-Modelle, Forderungsinkasso im B2C-Bereich, anwaltliches Inkasso.

## Eingaben

Das Modell benötigt:

- **Art des Akteurs**: Registriertes Inkassounternehmen (§ 10 RDG) oder Rechtsanwalt (§ 43d BRAO)?
- **Registrierungsstatus**: RDG-Registrierung vorhanden (§ 13 RDG)? Welche Behörde?
- **Forderungsart**: Mietforderung, Kaufpreisforderung, Schadenersatz, Verbraucherrechte-Ansprüche?
- **Schuldner**: Verbraucher (§ 13 BGB) oder Unternehmer?
- **Geschäftsmodell**: Klassisches Inkasso (Abtretung oder Einzugsermächtigung) oder Legal-Tech-Modell (Schuldner zahlt Erfolgsprovision)?
- **Vergütungsstruktur**: Wie wird die Vergütung berechnet? Auf Basis RVG, RDGEG oder abweichend?
- **Datenlage**: Welche Schuldnerdaten werden verarbeitet? Von wem bezogen (Gläubiger, Auskunfteien)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 10 Abs. 1 Nr. 1 RDG**: Natürliche und juristische Personen, die nicht als Rechtsanwalt zugelassen sind, dürfen Inkassodienstleistungen erbringen, wenn sie bei der zuständigen Behörde registriert sind.
- **§ 2 Abs. 2 Satz 1 RDG**: Inkassodienstleistung = Einziehung fremder oder zum Zweck der Einziehung auf eigene Rechnung abgetretener Forderungen, wenn die Forderungseinziehung als eigenständiges Geschäft betrieben wird.
- **§ 13 Abs. 1 RDG**: Registrierungspflicht; zuständig: Oberlandesgericht des Sitzes; Voraussetzungen: Sachkunde, Zuverlässigkeit, Berufshaftpflichtversicherung.
- **§ 13c RDG**: Pflichten registrierter Personen: Hinweispflichten gegenüber Auftraggebern und Schuldnern, Dokumentationspflichten, Treuhandpflichten.
- **§ 43d BRAO**: Rechtsanwälte dürfen Inkassodienstleistungen erbringen; keine gesonderte RDG-Registrierung erforderlich; aber: Einhaltung von § 43d BRAO-Anforderungen (Transparenz, Hinweis auf anwaltliche Stellung, Trennung von sonstigem Mandat).
- **§ 4 RDGEG (Vergütung)**: Vergütung für Inkassodienstleistungen registrierter Personen richtet sich nach den Vorschriften des RVG (analog); abweichende Vereinbarungen nur unter bestimmten Voraussetzungen zulässig; Verbraucher: keine Belastung mit überhöhten Kosten.
- **§ 13d RDG**: Hinweispflicht gegenüber Schuldnern: Mitteilung, wer Forderungsinhaber/Einzugsermächtiger ist, Hinweis auf Möglichkeit, Forderung zu bestreiten, Rechtsbehelfsbelehrung.
- **Art. 6 Abs. 1 lit. f DSGVO**: Berechtigtes Interesse als Rechtsgrundlage für Verarbeitung von Schuldnerdaten im Inkasso; Interessenabwägung: Inkasso-Interesse vs. Rechte der Schuldner; ErwGr. 47 DSGVO: Forderungseinzug als anerkanntes berechtigtes Interesse.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

**Schritt 1 – Zulässigkeitsprüfung: Inkassodienstleistung i.S.d. RDG**
- Liegt Einziehung fremder oder abgetretener Forderungen als eigenständiges Geschäft vor (§ 2 Abs. 2 Satz 1 RDG)?
- Abgrenzung zu unerlaubter Rechtsberatung: Geht die Tätigkeit über Forderungseinziehung hinaus (umfassende Rechtsberatung)? → Unzulässig ohne Anwaltszulassung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 2 – Registrierung prüfen (§ 13 RDG)**
- Registrierung beim zuständigen OLG (§ 13 Abs. 1 RDG) vorhanden?
- Sachkunde nachgewiesen? Berufshaftpflichtversicherung abgeschlossen?
- Laufende Pflichten: Meldung von Änderungen, Jahresabschlüsse, Kundengeldtreuhandkonto.
- Rechtsanwalt: Keine Registrierung erforderlich; stattdessen § 43d BRAO beachten.

**Schritt 3 – Hinweispflichten gegenüber Schuldnern (§ 13d RDG)**
- Erstes Anschreiben muss enthalten:
 - Identität des Inkassounternehmens (vollständiger Name, Anschrift, Registrierungsnummer).
 - Forderungsinhaber und Rechtsgrund der Forderung.
 - Forderungsbetrag mit Aufschlüsselung (Hauptforderung, Zinsen, Kosten).
 - Hinweis auf Recht des Schuldners, die Forderung zu bestreiten.
 - Kontaktmöglichkeit für Rückfragen.
- Irrleitende oder einschüchternde Kommunikation ist unzulässig (§ 4 UWG, Lauterkeitsrecht).

**Schritt 4 – Vergütung (§ 4 RDGEG)**
- Vergütung nach RVG-Grundsätzen analog (Inkassovergütungsverordnung außer Kraft, nunmehr § 4 RDGEG).
- Verbraucher-Schuldner: Inkassokosten nur in Höhe der nach RVG erstattungsfähigen Kosten (§ 4 Abs. 5 RDGEG); keine Kostenwälzung oberhalb RVG-Niveau auf Schuldner.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 5 – Datenschutz (Art. 6 Abs. 1 lit. f DSGVO)**
- Rechtsgrundlage für Verarbeitung von Schuldnerdaten: berechtigtes Interesse des Forderungsgläubigers/Inkassounternehmens (Art. 6 Abs. 1 lit. f DSGVO; ErwGr. 47).
- Interessenabwägung dokumentieren: Forderungseinziehungsinteresse vs. Datenschutzinteressen des Schuldners.
- Informationspflicht nach Art. 14 DSGVO beim ersten Kontakt mit Schuldner (Datenherkunft: Gläubiger).
- Auskunfteien-Meldung (SCHUFA): Nur bei erheblicher Forderung, nach Mahnung, keine unverhältnismäßige Beeinträchtigung (Berechtigungsinteresse nach § 31 BDSG i.V.m. Art. 6 Abs. 1 lit. f DSGVO).

## Ausgabeformat

- **Erstmahnung/Inkassoschreiben** (Vorlage nach § 13d RDG): Vollständige Hinweispflichten, Kostenaufschlüsselung.
- **Zulässigkeits-Prüfmemo**: Inkassotätigkeit vs. unerlaubte Rechtsberatung, Registrierungsstatus.
- **Kostenrechnung** (Tabelle): Hauptforderung, Zinsen, RVG-Inkassogebühr, Gesamtbetrag.
- **Datenschutz-Checkliste**: Rechtsgrundlage, Art-14-Information, Auskunftei-Meldung.

## Beispiel

**Sachverhalt**: Legal-Tech-Startup L (RDG-registriert) zieht für Mieter M Ansprüche aus der Mietpreisbremse ein. L lässt sich die Forderung abtreten und nimmt 30 % Erfolgsprovision vom Erstattungsbetrag. L sendet Schreiben an Vermieter V ohne Hinweis auf M's Widerspruchsmöglichkeit.

**Gutachtenstil**:

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Hinweispflicht (§ 13d RDG)*: Das Schreiben an V muss V auf sein Recht hinweisen, die Forderung zu bestreiten. Das Fehlen dieses Hinweises verletzt § 13d RDG und kann als irreführende Geschäftspraxis nach § 5 UWG abgemahnt werden.

*Datenschutz*: L verarbeitet Schuldner-V's Daten auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an Forderungseinziehung). V ist nach Art. 14 DSGVO beim ersten Kontakt über die Datenherkunft (Mandant M) zu informieren.

## Risiken und typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Fehlende Hinweispflichten (§ 13d RDG)**: Erstes Schreiben ohne vollständige Pflichtangaben ist abmahn- und bußgeldfähig; v.a. fehlender Widerspruchshinweis.
- **Überhöhte Inkassokosten**: Verbraucher-Schuldnern dürfen über RVG-Niveau hinausgehende Kosten nicht auferlegt werden (§ 4 Abs. 5 RDGEG); Überschreitung → Rückforderungsanspruch.
- **Datenschutzverletzung bei Auskunftei-Meldung**: SCHUFA-Meldung ohne vorherige Mahnung und ohne Verhältnismäßigkeit ist ein eigenständiger DSGVO-Verstoß.
- **Fehlende RDG-Registrierung**: Tätigkeit ohne Registrierung ist gemäß § 3 RDG verboten; Verträge können nach § 134 BGB nichtig sein; Abtretung von Forderungen zu Inkassozwecken an nicht registrierte Person: unwirksam.
- **Treuhandpflichten verletzt**: Vereinnahmte Schuldnerzahlungen müssen unverzüglich an Gläubiger weitergeleitet werden (§ 13c RDG); Vermischung mit Eigengeldern ist strafbar (§ 246 StGB).

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `luecken`

**Fokus:** Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: nicht für Lueckenaufzeiger-Perspektive nach aussen (luecken-aufzeiger).

# Gap-Tracker

## Zweck

Dieser Skill liest und aktualisiert den Gap-Tracker. Er zeigt alle offenen, in Bearbeitung befindlichen und geschlossenen Compliance-Lücken aus dem letzten `luecken-aufzeiger`-Lauf an. Er ermöglicht das Setzen von Eigentümern, das Aktualisieren des Status und das Eskalieren von Gaps mit Fristüberschreitung.

## Eingaben

- Gap-Tracker-Datei: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/gap-tracker.yaml`
- Optional: Filter (nach Schweregrad, Frist, Eigentümer, Status)
- Optional: Gap-ID zum gezielten Aktualisieren

## Ablauf

### 1. Tracker lesen

Gap-Tracker lesen. Falls nicht vorhanden:
```
Noch keine Gaps erfasst. Starten Sie mit /regulatorisches-recht:lücken-aufzeiger,
um eine Gap-Analyse gegen eine Aufsichtsverlautbarung durchzuführen.
```

### 2. Status-Übersicht ausgeben

```
Gap-Übersicht – Stand: TT.MM.JJJJ

Gesamt: N | 🔴 Blockierend: N | 🟠 Hoch: N | 🟡 Mittel: N | 🟢 Gering: N
Offen: N | In Bearbeitung: N | Geschlossen: N | Überfällig: N
```

### 3. Sortierte Gap-Tabelle ausgeben

| Gap-ID | Verlautbarung | Anforderung (Kurzfassung) | Schwere | Frist | Eigentümer | Status |
|---|---|---|---|---|---|---|
| GAP-2025-001 | MaRisk AT 4.3.2 | Datenhaltung 10 Jahre | 🔴 | 31.12.2025 | Compliance | offen |

Sortierung: zuerst 🔴, dann nach Frist aufsteigend.

### 4. Aktionen anbieten

Nach der Übersicht:
```
Was möchten Sie tun?
a) Gap schließen (Gap-ID angeben)
b) Eigentümer setzen / ändern
c) Status aktualisieren (offen → in Bearbeitung → geschlossen)
d) Richtlinienneufassung für einen Gap starten → /richtlinien-neufassung
e) Eskalationsnotiz für überfällige Gaps erstellen
f) Alle geschlossenen Gaps archivieren
```

### 5. Tracker aktualisieren

Änderungen in der YAML-Datei speichern und Änderungszeitpunkt vermerken.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Bindung an Gesetz und Recht, Rechtsluecken-Klaerung) — §§ 133, 157 BGB (Auslegungsgrundsaetze) — § 5 EGBGB (Analogie bei Rechtsluecken im Privatrecht) — §§ 13, 31 EnWG (Luecken in Regulierungs-Normen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Dieser Skill liest und schreibt ausschließlich interne Tracking-Daten; keine normspezifische Zitierung erforderlich. Gap-Inhalte enthalten Normverweise aus dem erzeugenden `luecken-aufzeiger`-Lauf.

## Ausgabeformat

- **Übersichtskarte:** Kennzahlen oben
- **Gap-Tabelle:** Sortiert nach Priorität und Frist
- **Aktionsmenü:** Konkrete nächste Schritte

## Beispiel

**Eingabe:** `/regulatorisches-recht:lücken`

**Ausgabe:**
```
Gap-Übersicht – Stand: 01.06.2025

Gesamt: 7 | 🔴 2 | 🟠 3 | 🟡 2 | 🟢 0
Offen: 5 | In Bearbeitung: 2 | Geschlossen: 0 | Überfällig: 0

| Gap-ID | Verlautbarung | Anforderung | Schwere | Frist | Eigentümer | Status |
|-------------|----------------------|---------------------|---------|------------|-------------|---------------|
| GAP-2025-001| MaRisk AT 4.3.2 | Datenhaltung 10 J. | 🔴 | 31.12.2025 | Compliance | offen |
| GAP-2025-002| MaRisk BTR 3.2 | ESG-Integration | 🔴 | 31.03.2026 | Risiko | in Bearbeitung|
| GAP-2025-003| MaRisk BTO 1.2.4 | Kreditvergabe | 🟠 | 30.06.2026 | Kredit | offen |
```

## Risiken / typische Fehler

- **Veralteter Tracker:** Ohne regelmäßige `luecken-aufzeiger`-Läufe veraltet der Tracker. Hinweis anzeigen, wenn der letzte Lauf > 90 Tage zurückliegt.
- **Eigentümer nicht gesetzt:** Gaps ohne Eigentümer werden nicht umgesetzt. Unzugeordnete Gaps explizit markieren.
- **Fristüberschreitung ohne Eskalation:** Für überfällige Gaps automatisch Eskalationsnotiz-Option hervorheben.

## 3. `mar-mifid-eltif-uebergreifend`

**Fokus:** MAR-MiFID-ELTIF uebergreifend: Insiderhandel, Marktmanipulation, Geeignetheit, ELTIF 2.0 Retail-Vertrieb. Pruefraster ueber alle drei Regelwerke fuer einen typischen Produktentwicklungsfall. Schnittstellen und Konfliktpunkte.

# MAR und MiFID und ELTIF

## Spezialwissen: MAR und MiFID und ELTIF
- **Spezialgegenstand:** MAR und MiFID und ELTIF / mar mifid eltif uebergreifend. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** MAR, ELTIF.
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
