---
name: vorlageanordnung-zeuge-vorbereitung
description: "Vorlageanordnung Zeuge Vorbereitung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vorlageanordnung Zeuge Vorbereitung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Vorlageanordnung Zeuge Vorbereitung** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vorlageanordnung` | Vorlageanordnung nach § 142 ZPO beantragen: Vorlage von Urkunden durch Gegner oder Dritte. Normen: §§ 142 143 ZPO. Prüfraster: urkundliche Beweise, Pflicht zur Vorlage, Sanktionen bei Weigerung. Output: Antrag auf Urkundenvorlageanordnung. Abgrenzung: nicht Beweissicherungsverfahren §§ 485 ff. ZPO. |
| `zeuge-vorbereitung` | Zeuge für Gerichtstermin vorbereiten: Aussagerecht, Zeugnisverweigerung, Vernehmungsablauf. Normen: §§ 373 ff. 383 ff. ZPO. Prüfraster: Zeugnisverweigerungsrecht, Glaubwürdigkeitsfragen, Vernehmungsthemen. Output: Zeugenvorbereitungsprotokoll. Abgrenzung: nicht Sachverständigenbestellung §§ 402 ff. ZPO. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Vorlageanordnung Zeuge Vorbereitung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vorlageanordnung`

**Fokus:** Vorlageanordnung nach § 142 ZPO beantragen: Vorlage von Urkunden durch Gegner oder Dritte. Normen: §§ 142 143 ZPO. Prüfraster: urkundliche Beweise, Pflicht zur Vorlage, Sanktionen bei Weigerung. Output: Antrag auf Urkundenvorlageanordnung. Abgrenzung: nicht Beweissicherungsverfahren §§ 485 ff. ZPO.

# Triage Gerichtliche und Behördliche Beweisanordnungen

## Zweck

Beweisanordnungen und Vorladungen kommen mit Fristen. Die typischen Fehler: Frist verpassen, zu viel produzieren (Schutzrechtsverlust, unnötige Belastung), zu wenig produzieren (Ordnungsgeld, Beugehaft) oder das Fenster für eine Einwendung versäumen. Dieser Skill klassifiziert, analysiert und erstellt einen Mitwirkungsplan mit Einwendungsgerüst.

Hinweis: Ein direktes Pendant zur US-amerikanischen "Subpoena" existiert im deutschen Recht nicht. Dieser Skill behandelt die deutschen Rechtsinstitute, die vergleichbare Funktionen erfüllen: Urkundenvorlageanordnung (§ 142 ZPO), Augenscheinsanordnung (§ 144 ZPO), Zeugenladung (§§ 373 ff. ZPO), polizeiliche und staatsanwaltschaftliche Anforderungen (§ 161a StPO), Durchsuchung und Sicherstellung (§§ 102, 103 StPO) sowie behördliche Auskunftsersuchen.

## Eingaben

- **Beweisanordnung oder Vorladungsdokument** (erforderlich): Pfad oder direktes Einlesen im Dialog
- **Mandatsbezeichnung (Slug)** (optional): Falls bereits ein Mandat existiert
- **Verfahrensart**: ZPO, StPO, VwGO, FGO, SGG
- **Stellung**: Zeuge, Dritter, Partei, Verteidiger

## Rechtlicher Rahmen

### Kernvorschriften: Urkundenvorlage und Beweiserhebung (ZPO)

- **§ 142 ZPO** — Anordnung der Urkundenvorlegung durch das Gericht; Voraussetzungen: Erheblichkeit und Zumutbarkeit; Verweigerungsrecht nach § 142 Abs. 2 ZPO i.V.m. §§ 383, 384 ZPO.
- **§ 144 ZPO** — Anordnung der Inaugenscheinnahme; analoge Schranken.
- **§§ 273, 356 ZPO** — Gerichtliche Beweisbeschlüsse; Fristbestimmungen; Folgen der Nichtbefolgung (§ 286 ZPO Beweiswürdigung, § 380 ZPO Ordnungsgeld bei Zeugnisverweigerung).
- **§§ 373–401 ZPO** — Zeugenbeweis; Ladung, Erscheinungspflicht, Zeugnisverweigerungsrecht; § 383 Nr. 6 ZPO: Zeugnisverweigerung für Rechtsanwälte.

### Kernvorschriften: Strafverfahren

- **§ 161a StPO** — Staatsanwaltliche Anforderung von Auskünften und Vorlage von Unterlagen; Erscheinens- und Aussagepflicht.
- **§§ 102, 103 StPO** — Durchsuchung bei Verdächtigen (§ 102) und bei Dritten (§ 103 StPO: erhöhte Anforderungen; Kanzleidurchsuchung nach § 103 grundsätzlich nur bei dringenden Verdachtsmomenten gegen den Anwalt selbst).
- **§ 94 StPO** — Sicherstellung als Beweismittel; sachliche Voraussetzungen.
- **§ 97 StPO** — Beschlagnahmeverbot; schützt Schriften des Verteidigers und Gegenstände im Gewahrsam von Zeugnisverweigerungsberechtigten.
- **§ 53 StPO** — Zeugnisverweigerungsrecht des Rechtsanwalts; vollständige Weigerungsbefugnis.
- **§ 160a StPO** — Schutz des Verkehrs mit Berufsgeheimnisträgern; Verbot der Umgehung durch verdeckte Ermittlungsmaßnahmen.

### Kernvorschriften: Beschlagnahmeschutz

- **§ 97 Abs. 1 Nr. 1 StPO** — Beschlagnahmeverbot für schriftliche Mitteilungen zwischen Beschuldigtem und Rechtsanwalt im Gewahrsam des Anwalts.
- **§ 97 Abs. 2 StPO** — Beschlagnahmeverbot erstreckt sich auf alle Gegenstände, auf die das Zeugnisverweigerungsrecht sich bezieht.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 0: Anwendbares Recht bestimmen

Vor der Analyse der Beweisanordnung: Welches Verfahren und welche Normen gelten?

- **ZPO-Verfahren**: §§ 142, 144, 273 ZPO; Verweigerungsrechte nach §§ 383, 384 ZPO; Fristberechnung nach §§ 214 ff. ZPO.
- **StPO-Verfahren**: §§ 94, 97, 102, 103, 161a StPO; § 53 StPO bei Zeugnisverweigerungsrecht; sofortiger Widerspruch bei Beschlagnahme von Verteidigerunterlagen.
- **VwGO**: §§ 86, 99, 111 VwGO; behördliche Vorlagebeschlüsse; In-camera-Verfahren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Quellenattribuierung: Jeden Normen- und Entscheidungshinweis mit Herkunft versehen: `[Primärquelle]`, `[Kommentar – prüfen]`, `[Trainingsdaten – prüfen]`. Vor Einreichung in Schriftsätzen oder gegenüber dem Gericht sind alle Angaben gegen eine Primärquelle (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang) zu verifizieren.

### Schritt 1: Klassifizieren

Beweisanordnungen kommen in verschiedenen Formen mit unterschiedlichen Rechtsfolgen:

- **Urkundenvorlageanordnung (§ 142 ZPO, zivil)** — Wir sind Dritter oder Partei; das Gericht verlangt unsere Unterlagen. Übliche Einwendungskategorien: Erheblichkeit, Zumutbarkeit, Beschlagnahmeschutz/Zeugnisverweigerungsrecht.
- **Zeugenladung (§§ 373 ff. ZPO; § 161a StPO)** — Ein Mitarbeiter oder der Anwalt selbst soll aussagen. Umfang, Relevanz, mögliche Einwendung; etwaige Zeugnisvorbereitung erforderlich.
- **Durchsuchungs-/Sicherstellungsanordnung (§§ 102, 103 StPO)** — Ermittlungsmaßnahme in Büro- oder Kanzleiräumen. Bei Kanzleidurchsuchung sofortige Prüfung § 97 StPO; Widerspruch zu Protokoll erklären; keine Mitwirkung über die Duldungspflicht hinaus ohne Rechtsrat.
- **Behördliches Auskunftsersuchen (z. B. BKartA, BaFin, Steuerfahndung)** — Eigene Verfahrensordnung; Auskunftsverweigerungsrechte unterschiedlich.
- **Strafrechtliche Vorladung (§ 163a StPO)** — Als Beschuldigter; sofortiger Rechtsanwalt; Aussageverweigerungsrecht.

### Schritt 2: Schlüsselfelder extrahieren

- **Anordnende Stelle** — Gericht (welches), Staatsanwaltschaft (welche), Behörde (welche)
- **Antragsteller** (bei Zivilsachen) — wer hat die Anordnung beantragt
- **Verfahrens-/Aktenzeichen** — das zugrundeliegende Verfahren
- **Verlangte Unterlagenkategorien** — nummerierte Liste
- **Aussagethemen** (bei Zeugenladung) — Themenkomplexe nach Ladung
- **Reaktionsfrist** — Zustelldatum + Berechnung der Reaktionszeit nach anwendbarem Recht
- **Vorlage-/Erscheinungsdatum** — Datum, zu dem Dokumente vorgelegt oder Aussage gemacht werden soll
- **Geographischer Umfang** — betroffene Personen, Orte, Systeme
- **Zustellungsempfänger** — wer ist Adressat

### Schritt 3: Portfolioquerverweis

- **Anordnung in Parteiverfahren:** Stimmt das Aktenzeichen mit einem Mandat in `_log.yaml` überein? Falls ja: In bestehendes Mandat eingliedern; diese Triage ist informativ.
- **Anordnung aus unbekanntem Verfahren:** Beteiligte erfassen; als eigenständige Eingangspost anlegen.
- **Mehrere Anordnungen aus demselben Verfahren:** Koordinierte Anforderung markieren; einheitliche Antwortstrategie prüfen.

### Schritt 4: Umfang, Belastung und Beschlagnahmeschutz analysieren

**Umfang / Erheblichkeit**
- Erfassen die Kategorien tatsächlich vorhandene Dokumente?
- Ist eine Kategorie überschießend (unverhältnismäßig weit, ohne erkennbaren Bezug zum Verfahrensgegenstand)?
- Geografischer Umfang / Erscheinungsort — § 142 ZPO: zumutbar; § 103 StPO: Verhältnismäßigkeit; VwGO: § 86 Abs. 1 VwGO Beibringungspflicht.

**Belastung**
- Betroffene Personen und Systeme, relevanter Zeitraum
- Geschätztes Volumen (grob: gering / mittel / groß / außergewöhnlich hoch)
- Kosten — Dritte können in bestimmten Konstellationen Kostenerstattung geltend machen; Rechtsgrundlage prüfen.

**Beschlagnahmeschutz und Zeugnisverweigerung**
- § 97 StPO-Schutz wahrscheinlich berührt? (Beinahe immer bei jeder rechtsbezogenen Anforderung; häufig auch bei Korrespondenz mit Syndikusrechtsanwälten — Einschränkung beachten)
- Weitere Weigerungsrechte: § 383 Nr. 6 ZPO, § 53 StPO Zeugnisverweigerung, § 43a BRAO Verschwiegenheit
- Schutzwürdige Geschäftsgeheimnisse nach GeschGehG
- Datenschutz — Art. 14 DSGVO: Informationspflicht bei Übermittlung personenbezogener Daten an Dritte

**Sonstige Einwendungsgründe**
- Vertraulichkeit — Schutzanordnung nach § 174 GVG oder Vereinbarung erforderlich?
- Doppelproduktion — hat die Gegenseite bereits dieselben Unterlagen aus einer anderen Quelle?
- Nicht vorhanden — wir besitzen das Verlangte nicht (mit Substanz darlegen)
- Zustellungsmangel — Voraussetzungen der §§ 171 ff. ZPO, §§ 33 ff. StPO prüfen

### Schritt 5: Einwendungsgerüst

Strukturiertes Einwendungsraster — nicht der fertige Schriftsatz, sondern das Gerüst, das Anwalt (ggf. zusammen mit externen Bevollmächtigten) ausarbeitet.

Je Einwendung:
- Rechtsgrundlage — Pinpoint-Zitat aus der Schritt-0-Recherche
- Konkrete Anwendung auf diese Anordnung (welche Kategorien, welche Personen)
- Stärke (stark / vertretbar / schwach)

### Schritt 6: Mitwirkungsplan

Selbst bei Einwendungen wird häufig ein Teil des Verlangten erfüllt:

- **Umfang der wahrscheinlichen Vorlage** — nach Einwendungen verbleibende Dokumente
- **Zu durchsuchende Personen und Systeme**
- **Zeitraum**
- **Prüfungsprotokoll** — wer prüft auf Vertraulichkeitsschutz (Kanzlei, externe Bevollmächtigte)
- **Produktionsformat** — gemäß Anordnung oder ausgehandeltem Protokoll
- **Anforderungen an das Vertraulichkeitsregister** — Format, Felder, geschätzte Einträge

### Schritt 7: Fristen

Alle Fristen aus der Schritt-0-Recherche verwenden. Einwendungsfristen können bereits mit Zustellung zu laufen beginnen — nicht auf ein einheitliches Datum vertrauen, ohne die geltende Norm und etwaige lokale Varianten zu prüfen.

- **Reaktionsfrist** — nach anwendbarer Norm; ggf. Verlängerung durch Korrespondenz mit Gericht/Staatsanwaltschaft erforderlich
- **Einwendungsfrist** — nach anwendbarer Norm (ZPO, StPO, VwGO, FGO) `[PRÜFEN]`
- **Abstimmungstermin** — falls Einschränkungen angestrebt werden, typischerweise vor Einwendungsfrist
- **Vorlagedatum** — sofern keine Einwendungen greifen

Alle Fristen sofort im Fristenkontrollsystem notieren.

## Ausgabeformat

### Schritt 8: Triage-Dokument erstellen

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

# Beweisanordnung Triage

> **KEIN ERSATZ FÜR ANWALTLICHE BERATUNG.** Dies ist eine strukturierte Klassifizierungs- und Scoping-Analyse zur Unterstützung schneller Entscheidungen zu Fristen, Beweissicherung und Mandatierung. Jeder Normenhinweis ist ein Ausgangspunkt — rechtssichere Einwendungen, Antragsstellung und Vertretung vor Gericht erfordern zugelassene Rechtsanwälte mit Kenntnis des Forums. Externe Bevollmächtigte für jede Beweisanordnung außerhalb routinemäßiger Drittvorlagen mandatieren.

**Slug:** [Bezeichnung]
**Zugestellt:** [JJJJ-MM-TT]
**Zugestellt an:** [Person / Kanzlei / eingetragener Vertreter]
**Ausgangsdokument:** [Pfad]
**Klassifizierung:** [§-142-ZPO-Vorlage / Zeugenladung / Durchsuchung/Sicherstellung / Behördenanforderung / Strafrechtliche-Vorladung]

---

## Schlüsselfelder

- **Anordnende Stelle:** [Gericht/Behörde]
- **Antragsteller:** [Name]
- **Aktenzeichen/Verfahrenskapitel:** [Bezeichnung]
- **Reaktionsfrist:** [Datum]
- **Vorlagedatum:** [Datum]
- **Einwendungsfenster:** [Zeitraum]

## Verlangte Kategorien (Zusammenfassung)

[nummerierte Liste, knapp]

## Betroffene Personen / Systeme

[Liste]

---

## Portfolioquerverweis

**Verwandtes Mandat:** [Bezeichnung oder "keins"]
**Bei Parteiverfahren:** [in bestehendes Mandat eingegliedert oder neues Mandat?]
**Bei Drittanordnung:** [eigenständige Eingangspost]

---

## Umfangs- und Belastungsanalyse

**Umfang:** [Erheblichkeitsbewertung je Kategorie]
**Belastungsschätzung:** [gering / mittel / groß / außergewöhnlich hoch — mit Begründung]
**Geografischer Umfang:** [etwaige Probleme]

## Beschlagnahmeschutz- und Zeugnisverweigerungsanalyse

*Erste Scoping-Prüfung; endgültige Entscheidung liegt beim Anwalt.*

**§ 97 StPO / § 43a BRAO / § 53 StPO wahrscheinlich berührt:** [ja/nein + welche Kategorien] `[PRÜFEN]`
**Weitere Weigerungsrechte:** [GeschGehG, Datenschutz, § 383 ZPO] `[PRÜFEN]`
**Vertraulichkeitsregister erforderlich:** [ja/nein — Format]

---

## Einwendungsgerüst

*Jede Zeile erfordert `[PRÜFEN]` vor Geltendmachung in Schriftsätzen — Normaktualität, lokale Varianten, Wirkungsrisiko.*

| Einwendung | Rechtsgrundlage | Anwendung | Stärke | Anwalt geprüft? |
|---|---|---|---|---|
| Erheblichkeit/Verhältnismäßigkeit | [Norm] | [Kategorien] | [stark/vertretbar/schwach] | [ ] |
| Belastung/Zumutbarkeit | [Norm] | [Kategorien] | | [ ] |
| § 97 StPO / § 43a BRAO | Beschlagnahmeschutz/Verschwiegenheit | [alle Schutzunterlagen] | stark | [ ] |
| Nicht vorhanden | [Norm/Grundsatz] | [falls zutreffend] | | [ ] |
| [Sonstiges] | | | | [ ] |

---

## Mitwirkungsplan (falls Reaktion erfolgt)

- **Umfang der wahrscheinlichen Vorlage:** [nach Einwendungen]
- **Personen/Systeme:** [Liste]
- **Zeitraum:** [Zeitraum]
- **Prüfungsprotokoll:** [wer, wie]
- **Produktionsformat:** [Format]
- **Vertraulichkeitsregister:** [Format, geschätzte Einträge]

---

## Fristen (sofort im Fristenkontrollsystem eintragen)

*Alle Fristen stammen aus der Schritt-0-Normenrecherche. `[PRÜFEN]` bestätigt Norm, Variante und Berechnung für dieses Forum und diese Anordnungsart.*

- **Reaktionsfrist:** [Datum] `[PRÜFEN]`
- **Einwendungsfrist:** [Datum] — Quelle: [Norm + Pinpoint] `[PRÜFEN]`
- **Abstimmungstermin:** [Datum] (typischerweise vor Einwendungsfrist) `[PRÜFEN]`
- **Vorlagedatum:** [Datum]

---

## Sofortige Maßnahmen

- [ ] Beweissicherungsanordnung — [ja/nein] — falls nein: `/prozessrecht:beweissicherung [slug] --anordnen` mit Anordnungsumfang ausführen
- [ ] Externe Bevollmächtigte mandatiert — [ja/wer/offen]
- [ ] Abstimmung mit Anordnendem geplant — [Datum]
- [ ] Mandat im Protokoll angelegt — [ja/nein/offen]
- [ ] Kostenanalyse — [falls Belastung groß]
- [ ] Interne Eskalation — [wer]

---

## Empfehlung

[Zwei Absätze: Was tun. Einwendungshaltung. Mitwirkungshaltung. Ob externe Bevollmächtigte Einwendungen übernehmen oder nicht. Ob ein Antrag auf Aufhebung/Einschränkung der Anordnung sinnvoll ist.]

---

## Quellenverifizierung

Jeder Normen-, Entscheidungs- und Regelhinweis in dieser Triage — einschließlich der Schritt-0-Recherchequellen, Einwendungsgrundlagen und Verweisungen auf das Vertraulichkeitsregister — ist KI-generiert und ungeprüft. Vor Verwendung in Schriftsätzen, Einwendungskorrespondenz oder Antragsstellungen ist eine Verifikation gegen eine Primärquelle (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, Wolters Kluwer) erforderlich: Richtigkeit, Aktualität, lokale Varianten. Fabrizierte oder fehlerhafte Zitate in eingereichten Schriftsätzen können Sanktionen auslösen.
```

### Schritt 9: Übergabe

**Vor der Reaktion gegenüber dem Gericht oder der Behörde (Einwendungen einreichen, Dokumente vorlegen, als Zeuge erscheinen, Antrag auf Aufhebung stellen — jede inhaltliche Reaktion):**

> Eine Reaktion auf Beweisanordnungen hat rechtliche Folgen — Fristversäumnis kann Ordnungsgeld oder Beugehaft auslösen, zu viel produzieren kann Schutzrechtsverlust bewirken, zu wenig produzieren kann Kostennachteile oder Beweisnachteile erzeugen. Wurde dies mit einem Anwalt besprochen? Falls ja: bitte bestätigen. Falls nein, hier ist ein Briefing für das Gespräch:
>
> [Zusammenfassung: Art der Anordnung, anordnende Stelle, Fristen, Umfang des Verlangten, Einwendungsgerüst und Stärke, Beschlagnahmeschutz und Belastungsfragen, vorgeschlagene Reaktionshaltung, was schiefgehen kann, Fragen an den Anwalt.]

Ohne ausdrückliche Bestätigung keine Weiterleitung. Triage, Scoping und internes Fristenmanagement erfordern die Schranke nicht — die Reaktion gegenüber der anordnenden Stelle schon.

- Bei **strafrechtlicher Vorladung als Beschuldigter** → sofort Verteidiger mandatieren; diese Triage endet hier.
- Bei **Kanzleidurchsuchung (§ 103 StPO)**: sofortiger Widerspruch zu Protokoll; keine freiwillige Herausgabe über Duldungspflicht hinaus ohne anwaltliche Prüfung.
- Sonst: Angebot, Mandat anzulegen (in der Regel sinnvoll — Beweisanordnungen sind fast immer bedeutend genug zur Verfolgung).
- Falls noch keine Beweissicherungsanordnung mit dem Anordnungsumfang vorliegt: sofort an `/prozessrecht:beweissicherung --anordnen` übergeben.

## Risiken und typische Fehler

- **Beschlagnahmeschutz § 97 StPO:** Bei Kanzleidurchsuchungen sofort Widerspruch erklären; jede Herausgabe ohne Prüfung kann den Schutz endgültig beseitigen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Einwendungsfristen:** Laufen teilweise bereits ab Zustellung; kein einheitliches Datum ohne Normprüfung annehmen.
- **Quellenverifizierung:** Alle Norm- und Entscheidungshinweise sind vor Einreichung zu verifizieren.

## Quellenpflicht

- Gesetzestexte: §§ 142, 144, 273, 373 ff., 383, 384 ZPO; §§ 53, 94, 97, 102, 103, 160a, 161a, 163a StPO; §§ 86, 99 VwGO; § 43a BRAO; GeschGehG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

<!-- AUDIT 27.05.2026
behandelt aber Abschiebungsanordnung nach § 58a AufenthG gegen algerischen Islamisten (WRONG_TOPIC),
nicht das behauptete Thema "Auskunftsverweigerungsrecht § 99 VwGO / behoerdliches
Geheimhaltungsinteresse". Das im Skill genannte Datum 15.02.2018 existiert auf dejure.org
ebenfalls nicht. Halluzinierte Referenz geloescht. Keine Ersatzquelle ergaenzt.
-->

## 2. `zeuge-vorbereitung`

**Fokus:** Zeuge für Gerichtstermin vorbereiten: Aussagerecht, Zeugnisverweigerung, Vernehmungsablauf. Normen: §§ 373 ff. 383 ff. ZPO. Prüfraster: Zeugnisverweigerungsrecht, Glaubwürdigkeitsfragen, Vernehmungsthemen. Output: Zeugenvorbereitungsprotokoll. Abgrenzung: nicht Sachverständigenbestellung §§ 402 ff. ZPO.

# Zeugenvernehmung-Vorbereitung

## Zweck

Vorbereitung auf eine Zeugenvernehmung im deutschen Zivil- oder Strafverfahren. Drei Perspektiven:
- **Eigener Zeuge vorbereiten** (Information des Mandanten über Ablauf, § 373 ff. ZPO; § 395 StPO)
- **Gegnerischen Zeugen befragen** (Fragenkatalog aus der Mandatstheorie entwickeln)
- **Strafverteidigung:** Vorbereitung auf Hauptverhandlung (§§ 244 ff. StPO), Pflichtverteidiger-Gespräch

> Die Zeugenvernehmung findet ausschließlich vor dem Gericht statt (§ 396 ZPO, § 238 Abs. 2 StPO). Eine vorgerichtliche anwaltliche Befragung von Zeugen kennt das deutsche Recht nicht. Eine informelle Zeugen-"Vorbefragung" durch den Anwalt ist berufsrechtlich sensibel (§ 1 BORA – Sachlichkeit; vgl. § 26 BRAO) und darf Zeugen nicht beeinflussen.

## Eingaben

- Aktives Mandat (Slug)
- Zeuge: Name, Rolle im Verfahren (Zeuge der Partei / gegnerischer Zeuge / Zeuge von Amts wegen)
- Vernehmungsmodus: `--eigener-zeuge`, `--gegnerischer-zeuge`, `--strafverfahren`
- Vorhandene Dokumente: Zeugenaussagen (Erstvernehmung, Polizeiprotokoll), Schriftverkehr des Zeugen, Anlagen, Chronologie

## Ablauf

### Modus: Eigener Zeuge vorbereiten (`--eigener-zeuge`)

1. **Ablaufbelehrung:** Dem Mandanten/Zeugen den Vernehmungsablauf erklären (§§ 395, 396, 402 ZPO): Vorführung, allgemeine Personalien, Belehrung, freie Schilderung, Befragung durch Gericht, Fragen der Parteien, Eid/eidesstattliche Versicherung (§ 391 ZPO).

2. **Zeugnisverweigerungsrecht prüfen:** §§ 383–385 ZPO (Angehörige, Berufsgeheimnisträger, Selbstbelastungsverbot); § 52 StPO; § 55 StPO (Auskunftsverweigerungsrecht).

3. **Erinnerungslücken identifizieren:** Aus Chronologie bekannte Ereignisse mit Zeugenwissen abgleichen; offene Punkte markieren.

4. **Fragenvorbereitung:** Erwartete Fragen des Gerichts und der Gegenseite vorab erarbeiten; angemessene Antworten (wahrheitsgemäß, nicht überschießend) vorbereiten.

5. **Vorhalte vorantizipieren:** Schriftstücke, E-Mails oder frühere Aussagen, die dem Zeugen vorgehalten werden könnten, identifizieren.

### Modus: Gegnerischen Zeugen befragen (`--gegnerischer-zeuge`)

1. **Zeugenprofil erstellen:** Aus Mandatsakte und Chronologie: Was weiß der Zeuge, was hat er gesagt, welche Dokumente hat er unterzeichnet?

2. **Themengliederung:**
 - Kernthemen (direkt anspruchsrelevant)
 - Glaubwürdigkeitsthemen (Widersprüche zu früheren Aussagen, Eigeninteresse)
 - Bestätigungsthemen (ungünstige Tatsachen aus Zeugen-Sicht bestätigen lassen)

3. **Fragenkatalog:** Geschlossene Kontrollfragen (auf ein Ja/Nein ausgerichtet) zuerst; offene Fragen nur bei sicherer Antwort; Fangfragen vermeiden (Prozessrisiko: Zeuge weicht aus).

4. **Vorhalte:** Dokumente, auf die vorgehalten werden soll, mit Anlage-Nr. verzeichnen.

5. **Glaubwürdigkeitsangriff:** Widersprüche zu protokollierten Aussagen, Eigeninteresse, Abhängigkeiten.

### Modus: Strafverfahren (`--strafverfahren`)

1. **Akteneinsicht § 147 StPO:** Vernehmungsprotokolle aus der Ermittlungsakte identifizieren.
2. **Belehrung § 136 StPO / § 55 StPO:** Sicherstellen, dass Auskunftsverweigerungsrecht bekannt ist.
3. **Hauptverhandlung § 244 StPO:** Beweisantragsrecht der Verteidigung (Beweisantrag auf Zeugenladung, § 244 Abs. 3, 6 StPO).

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

### Vernehmungs-Vorbereitung – Eigener Zeuge

**Zeuge:** [Name]
**Vernehmungsdatum:** TT.MM.JJJJ
**Verfahren:** [Mandat-Slug], [Gericht], Az.: [Aktenzeichen]

**Kernwissen des Zeugen (aus Chronologie):**
| Datum | Ereignis | Belegdokument | Zeugen-Relevanz |
|---|---|---|---|
| 12.03.2022 | Vertragsschluss | Anlage K1 | Zeuge anwesend |

**Fragenkatalog – erwartete Fragen:**
1. Wann wurden Sie auf das Projekt aufmerksam?
2. Waren Sie beim Vertragsschluss am 12.03.2022 anwesend?
...

**Vorhalte (antizipiert):**
- E-Mail v. 05.04.2022 (Anlage B3): Zeuge bat um Verlängerung – klären, warum.

**Zeugnisverweigerungsrecht:** Nicht einschlägig (kein Angehöriger, kein Berufsgeheimnisträger).

## Risiken / typische Fehler

- **Zeugencoaching verboten:** Der Anwalt darf den Zeugen nicht zu einer bestimmten Aussage anleiten; nur Erläuterung des Ablaufs und Erinnerungshilfe auf Basis vorhandener Dokumente zulässig (vgl. § 1 BORA).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Gegnerischer Zeuge – keine Kontaktaufnahme:** Kontaktaufnahme mit gegnerischem Zeugen außerhalb des Verfahrens ist berufsrechtlich problematisch (§ 12 BORA).
- **Vereidigung:** § 391 ZPO – Gericht entscheidet; falsche Zeugenaussage ist strafbar (§ 153 StGB); Zeuge vor Vernehmung hierüber belehren.

<!-- AUDIT 27.05.2026
einziger Treffer ist XI ZR 224/09 (06.07.2010, XI. Zivilsenat, Bankrecht/Anscheinsbeweis
Kreditkarte) - falscher Senat, falsches Thema. Behauptetes Thema "Freie Beweiswuerdigung
bei Zeugenaussagen § 286 ZPO" ist eine Halluzination. Referenz geloescht.
Keine Ersatzquelle ergaenzt.
-->
