---
name: vorlageanordnung
description: "Triage einer gerichtlichen oder behördlichen Beweisanordnung — Klassifizierung, Umfangs- und Beschlagnahmeschutzanalyse, Portfolioquerverweis und Erstellung eines Einwendungsgerüsts, Mitwirkungsplans und Fristenkalenders. Lädt, wenn der Nutzer eine Vorladung, Zeugenladung, Vorlageanordnung, Durchsuchungsanordnung oder behördliche Anforderung erhalten hat und deren Reaktionsstrategie klären möchte."
---

# Triage Gerichtliche und Behördliche Beweisanordnungen

## Zweck

Beweisanordnungen und Vorladungen kommen mit Fristen. Die typischen Fehler: Frist verpassen, zu viel produzieren (Schutzrechtsverlust, unnötige Belastung), zu wenig produzieren (Ordnungsgeld, Beugehaft) oder das Fenster für eine Einwendung versäumen. Dieser Skill klassifiziert, analysiert und erstellt einen Mitwirkungsplan mit Einwendungsgerüst.

Hinweis: Ein direktes Pendant zur US-amerikanischen „Subpoena" existiert im deutschen Recht nicht. Dieser Skill behandelt die deutschen Rechtsinstitute, die vergleichbare Funktionen erfüllen: Urkundenvorlageanordnung (§ 142 ZPO), Augenscheinsanordnung (§ 144 ZPO), Zeugenladung (§§ 373 ff. ZPO), polizeiliche und staatsanwaltschaftliche Anforderungen (§ 161a StPO), Durchsuchung und Sicherstellung (§§ 102, 103 StPO) sowie behördliche Auskunftsersuchen.

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

- **BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, NJW 2005, 1917** — Kanzleidurchsuchung; Beschlagnahmeverbot des § 97 StPO ist verfassungsrechtlich in Art. 12 Abs. 1 GG und im Rechtsstaatsprinzip verankert; Verhältnismäßigkeitsmaßstab.
- **BGH, Beschl. v. 10.07.2019 – StB 23/19, NStZ 2019, 687 Rn. 14 ff.** — Reichweite des Beschlagnahmeverbots § 97 StPO bei Kanzleidurchsuchung; Verteidiger-Mandant-Gewahrsam; Beweismittelbeschlagnahme nur bei nicht-verteidigungsrelevanten Gegenständen.
- **BGH, Beschl. v. 07.11.2018 – XII ZB 2/16, NJW 2019, 374 Rn. 18 ff.** — § 142 ZPO Urkundenvorlage; richterliche Ermessensgrenzen; Verweigerung wegen anwaltlicher Verschwiegenheit wirksam.
- **EuGH, Urt. v. 08.12.2022 – C-694/20 (Orde van Vlaamse Balies u.a.), NJW 2023, 197** — Schutz anwaltlicher Kommunikation im EU-Recht; Meldepflichten aus DAC6-Richtlinie verletzen bei Rechtsanwälten den Schutz vertraulicher Kommunikation; maßgeblich für alle grenzüberschreitenden Sachverhalte mit EU-Bezug.
- **BVerwG, Urt. v. 15.02.2018 – 1 A 2/17, NVwZ 2018, 825 Rn. 20** — Auskunftsverweigerungsrecht nach § 99 VwGO; behördliches Geheimhaltungsinteresse vs. Beibringungspflicht; Abwägungsmaßstab.

### Kommentarliteratur

- `Meyer-Goßner/Schmitt, StPO, 67. Aufl. 2024, § 97 Rn. 5 ff.` — Beschlagnahmeverbot; Gewahrsam; Treuhandverhältnis; Durchsuchungsschutz in Kanzleiräumen.
- `Zöller/Greger, ZPO, 35. Aufl. 2024, § 142 Rn. 3 ff.` — Urkundenvorlageanordnung; Weigerungsrechte; Verhältnismäßigkeit und Zumutbarkeit.
- `Kopp/Schenke, VwGO, 29. Aufl. 2023, § 99 Rn. 10 ff.` — In-camera-Verfahren bei behördlichem Geheimhaltungsinteresse; Reichweite der Vorlage­pflicht.
- `BeckOK StPO/Bär, 52. Ed. (Stand 01.01.2024), § 53 Rn. 6 ff.` — Zeugnisverweigerungsrecht; Bezugnahme auf Dritte (§ 53a StPO).

## Ablauf

### Schritt 0: Anwendbares Recht bestimmen

Vor der Analyse der Beweisanordnung: Welches Verfahren und welche Normen gelten?

- **ZPO-Verfahren**: §§ 142, 144, 273 ZPO; Verweigerungsrechte nach §§ 383, 384 ZPO; Fristberechnung nach §§ 214 ff. ZPO.
- **StPO-Verfahren**: §§ 94, 97, 102, 103, 161a StPO; § 53 StPO bei Zeugnisverweigerungsrecht; sofortiger Widerspruch bei Beschlagnahme von Verteidigerunterlagen.
- **VwGO**: §§ 86, 99, 111 VwGO; behördliche Vorlagebeschlüsse; In-camera-Verfahren.
- **EU-Bezug**: EuGH C-694/20 beachten für anwaltliche Kommunikation im grenzüberschreitenden Kontext.

Quellenattribuierung: Jeden Normen- und Entscheidungshinweis mit Herkunft versehen: `[Primärquelle]`, `[Kommentar – prüfen]`, `[Trainingsdaten – prüfen]`. Vor Einreichung in Schriftsätzen oder gegenüber dem Gericht sind alle Angaben gegen eine Primärquelle (juris, beck-online) zu verifizieren.

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

**Verwandtes Mandat:** [Bezeichnung oder „keins"]
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

Jeder Normen-, Entscheidungs- und Regelhinweis in dieser Triage — einschließlich der Schritt-0-Recherchequellen, Einwendungsgrundlagen und Verweisungen auf das Vertraulichkeitsregister — ist KI-generiert und ungeprüft. Vor Verwendung in Schriftsätzen, Einwendungskorrespondenz oder Antragsstellungen ist eine Verifikation gegen eine Primärquelle (juris, beck-online, Wolters Kluwer) erforderlich: Richtigkeit, Aktualität, lokale Varianten. Fabrizierte oder fehlerhafte Zitate in eingereichten Schriftsätzen können Sanktionen auslösen.
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
- **Syndikusanwalt-Korrespondenz:** Im EU-Kartellverfahren und bei Behördenermittlungen kein Schutz (EuGH Akzo Nobel C-550/07 P) — nicht pauschal § 43a BRAO geltend machen.
- **EuGH C-694/20:** Bei grenzüberschreitenden Sachverhalten und EU-Bezug: Schutz anwaltlicher Kommunikation nach EU-Recht beachten.
- **Einwendungsfristen:** Laufen teilweise bereits ab Zustellung; kein einheitliches Datum ohne Normprüfung annehmen.
- **Quellenverifizierung:** Alle Norm- und Entscheidungshinweise sind vor Einreichung zu verifizieren.

## Quellenpflicht

- Gesetzestexte: §§ 142, 144, 273, 373 ff., 383, 384 ZPO; §§ 53, 94, 97, 102, 103, 160a, 161a, 163a StPO; §§ 86, 99 VwGO; § 43a BRAO; GeschGehG
- Rechtsprechung: BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, NJW 2005, 1917; BGH, Beschl. v. 10.07.2019 – StB 23/19, NStZ 2019, 687; EuGH, Urt. v. 08.12.2022 – C-694/20, NJW 2023, 197
- Kommentare: Meyer-Goßner/Schmitt, StPO, 67. Aufl. 2024, § 97; Zöller/Greger, ZPO, 35. Aufl. 2024, § 142; Kopp/Schenke, VwGO, 29. Aufl. 2023, § 99

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
