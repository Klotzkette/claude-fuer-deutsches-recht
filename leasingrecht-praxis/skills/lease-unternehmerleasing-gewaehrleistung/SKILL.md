---
name: lease-unternehmerleasing-gewaehrleistung
description: "Lease Unternehmerleasing Gewaehrleistung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Unternehmerleasing Gewaehrleistung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Unternehmerleasing Gewaehrleistung** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-013-unternehmerleasing-gewaehrleistung-durchgriff` | Unternehmerleasing: Gewährleistungsabtretung, Durchgriff gegen Lieferant, AGB-Besonderheiten B2B, HGB-Handelskauf und Rügeobliegenheit. |
| `lease-014-lieferant-leasinggeber-leasingnehmer-dreiecksverhaeltn` | Leasingdreieck: Rechtsverhältnisse Lieferant/Leasinggeber/Leasingnehmer, Abtretungskonstruktion, Kollisionsprobleme und Insolvenz eines Beteiligten. |
| `lease-015-mangel-am-leasingobjekt-rechte-gegen-lieferant` | Mangel am Leasingobjekt: Sachmängelrecht, abgetretene Ansprüche gegen Lieferant, Nacherfüllung, Rücktritt, Schadensersatz, Fristen und Beweislast. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Unternehmerleasing Gewaehrleistung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-013-unternehmerleasing-gewaehrleistung-durchgriff`

**Fokus:** Unternehmerleasing: Gewährleistungsabtretung, Durchgriff gegen Lieferant, AGB-Besonderheiten B2B, HGB-Handelskauf und Rügeobliegenheit.

# Unternehmerleasing: Gewährleistung und Lieferantendurchgriff

## Zweck

Im Unternehmerleasing (B2B) gelten andere Regeln als im Verbraucherleasing. Der Leasingnehmer kann keine Gewährleistungsansprüche gegen den Leasinggeber geltend machen – er muss direkt gegen den Lieferanten vorgehen (Durchgriffskonstruktion). Dieser Skill analysiert die Abtretungskonstruktion, die Rügeobliegenheit nach HGB und die Folgen bei fehlendem Durchgriff.

## Dreiecksstruktur und Abtretungskonstruktion

### Standardkonstruktion
1. LG schließt Kaufvertrag mit Lieferant
2. LG tritt Gewährleistungsansprüche gegen Lieferant an LN ab (§ 398 BGB)
3. LN kann direkt gegen Lieferant klagen (Sachmängelansprüche, §§ 437 ff. BGB)
4. LN hat keine Gewährleistungsansprüche gegen LG

### BGH, Urteil vom 13.11.2013 - VIII ZR 257/12
Die Abtretungskonstruktion ist wirksam und typisch für das Finanzierungsleasing. Der Ausschluss der Gewährleistung des LG ist AGB-rechtlich zulässig, **wenn** die Abtretung tatsächlich erfolgt und LN klagebefugt ist.

**Unwirksam**: AGB-Klausel schließt LG-Gewährleistung aus, aber Abtretung an LN erfolgt nicht oder geht ins Leere (z.B. Lieferant insolvent). Dann: LG haftet nach § 307 BGB.

## HGB-Rügeobliegenheit (§ 377 HGB)

Wenn LN Kaufmann ist (§§ 1 ff. HGB), gilt für den Kaufvertrag zwischen LG und Lieferant die Rügeobliegenheit des § 377 HGB. **Wichtig**: LN steht dem Kaufvertrag als Dritter gegenüber; die Rügeobliegenheit trifft zunächst den LG.

**Praxis-Problem**: LG nimmt das Objekt nicht selbst in Empfang; es wird direkt an LN geliefert. Rügeobliegenheit: Wer muss rügen – LG oder LN?

**Lösung durch vertragliche Regelung**: Im Leasingvertrag wird LN zur Untersuchung und Rüge an Stelle des LG verpflichtet. BGH: Solche Klauseln sind zulässig.

Fristen:
- Sofort erkennbare Mängel: Unverzügliche Rüge (§ 377 I HGB), d.h. innerhalb weniger Werktage
- Verborgende Mängel: Unverzüglich nach Entdeckung
- Unterlassene Rüge: Genehmigung der Ware gilt als erteilt; Mängelansprüche verloren

## AGB im Unternehmerleasing

### Erleichterter AGB-Maßstab (§ 310 I BGB)
Im B2B-Bereich gelten §§ 308, 309 BGB nicht direkt. Trotzdem:
- § 307 BGB (Generalklausel) gilt
- BGH nutzt §§ 308, 309 BGB als Indizien für § 307-Bewertung

### Typische AGB-Klauseln B2B-Leasing
- Gefahrtragungsklausel: Wirksam (LN trägt Zufall-Untergangsrisiko)
- Abtretungsklausel: Wirksam, wenn Abtretung tatsächlich vollzogen
- Restwertgarantie: Im Unternehmerleasing regelmäßig mehr Gestaltungsspielraum als im Verbraucherleasing, aber Transparenz, Verwertungserlös, Mehrerlösbeteiligung und § 307 BGB gesondert prüfen.
- Kündigungsklausel: Weiter als B2C; kein Abmahnungserfordernis gesetzlich, aber Treu und Glauben

## Mangel am Leasingobjekt: Prozessuale Situation

### LN klagt gegen Lieferant
- Zuständigkeit: Allgemeiner Gerichtsstand (§ 12 ZPO) oder Erfüllungsort (§ 29 ZPO)
- Klagearten: Nacherfüllung (§ 439 BGB), Rücktritt (§ 440 BGB), Schadensersatz (§ 440 BGB)
- LG muss Abtretung belegen; LN muss Kaufpreis-/Leasingvertrag vorlegen

### Parallele Leasingratenpflicht
- LN muss Leasingraten weiterhin zahlen auch wenn er Mängelansprüche gegen Lieferant verfolgt
- Ausnahme: Berechtigte Verweigerung der Abnahme (Objekt noch nicht abgenommen)
- Streitig: Kann LN Raten zurückhalten bei erheblichem Mangel? BGH tendenziell nein.

## Prüfprogramm

1. Abtretungsklausel im Leasingvertrag vorhanden? Abtretung vollzogen?
2. Lieferant noch existent und solvent? (Ansonsten: LG haftet)
3. Rügeobliegenheit § 377 HGB: Wer muss rügen, bis wann?
4. Mängel sofort erkennbar oder verborgen? Fristen beachten
5. Klagbarkeit gegen Lieferant: Kaufvertrag als Klägergrundlage vorhanden?
6. Leasingraten-Fortführung trotz Mängel: Insolvenzrisiko LN?

## Typische Fallen

- Rügeobliegenheit nach § 377 HGB versäumt → alle Mängelansprüche verwirkt
- Lieferant insolvent → LG-Haftung, wenn Abtretungsklausel ins Leere läuft
- Keine Abtretungsklausel → LN hat keine direkten Rechte gegen Lieferant
- LN hält Raten zurück (fälschlicherweise): LG kündigt Vertrag

## Normen und Quellen

- § 398 BGB (Abtretung): https://dejure.org/gesetze/BGB/398.html
- §§ 437–442 BGB (Sachmängelansprüche): https://dejure.org/gesetze/BGB/437.html
- § 377 HGB (Rügeobliegenheit): https://www.gesetze-im-internet.de/hgb/__377.html
- § 307 BGB (AGB-Generalklausel): https://dejure.org/gesetze/BGB/307.html
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12 (Abtretungskonstruktion): https://www.bgh.de
- HGB §§ 343 ff.: https://www.gesetze-im-internet.de/hgb/__343.html

## Output-Formate

- **Rüge-Checkliste**: § 377 HGB im Leasingdreieck; Fristen, Formen
- **Abtretungsklausel-Bewertung**: Wirksam/Unwirksam nach AGB-Recht
- **Muster-Mängelrüge**: LN an Lieferant (abgetretener Anspruch)
- **Prozessübersicht**: LN vs. Lieferant – Beweislast, Klagegründe

## 2. `lease-014-lieferant-leasinggeber-leasingnehmer-dreiecksverhaeltn`

**Fokus:** Leasingdreieck: Rechtsverhältnisse Lieferant/Leasinggeber/Leasingnehmer, Abtretungskonstruktion, Kollisionsprobleme und Insolvenz eines Beteiligten.

# Das Leasingdreieck: Lieferant, Leasinggeber, Leasingnehmer

## Zweck

Das Finanzierungsleasing ist typischerweise ein Dreiecksgeschäft. Die drei Rechtsverhältnisse (LG–Lieferant, LG–LN, abgeleitetes LN–Lieferant) greifen ineinander. Dieser Skill analysiert die Struktur, Kollisionsprobleme und die Folgen bei Insolvenz eines Beteiligten.

## Rechtsverhältnisse im Überblick

### 1. Kaufvertrag: Lieferant → Leasinggeber (§ 433 BGB)
- LG kauft das Objekt vom Lieferant
- LG wird zivilrechtlicher Eigentümer
- Direktlieferung an LN möglich (§ 447 BGB analog: Gefahrübergang bei Übergabe an LN)
- Gewährleistungsansprüche entstehen beim LG

### 2. Leasingvertrag: Leasinggeber → Leasingnehmer (§§ 535 ff. BGB analog)
- LG überlässt LN die Nutzung gegen Leasingraten
- LG tritt Gewährleistungsansprüche gegen Lieferant an LN ab (§ 398 BGB)
- LN trägt Gefahrtragung (Finanzierungsleasing)
- LN haftet für Raten auch bei Schlechtleistung des Lieferanten

### 3. Abgeleitetes Verhältnis: Leasingnehmer → Lieferant
- Keine direkte vertragliche Verbindung
- LN hat nur abgetretene Ansprüche aus Kaufvertrag LG–Lieferant
- Klage im eigenen Namen kraft Abtretung (§ 398 BGB)

## Kollisionsprobleme

### Gefahrtragung bei Direktlieferung
- LG kauft, LN nimmt entgegen
- § 447 BGB: Gefahrübergang bei Übergabe an Transportperson, wenn LG als Versendungskäufer auftritt
- Im Leasingvertrag muss klargestellt sein, dass Gefahrübergang mit Übergabe an LN erfolgt

### Mängelrechte: Wer kann was?
| Anspruchsinhaber | Anspruch | Gegen wen |
|---|---|---|
| LG (vor Abtretung) | Nacherfüllung, Rücktritt, Minderung | Lieferant |
| LN (nach Abtretung) | Nacherfüllung, Schadensersatz | Lieferant |
| LN | Schadensersatz wegen Mangelfolge | Lieferant (Deliktsrecht §§ 823 ff.) |
| LN gegen LG | Grundsätzlich ausgeschlossen | n/a |

### Abtretung: Wirksamkeitserfordernisse
- Bestimmtheitsgrundsatz: Abtretungsklausel muss Ansprüche hinreichend bestimmt bezeichnen
- Zeitpunkt: Abtretung soll mit Leasingvertragsschluss oder Abnahme erfolgen
- Abtretungsverbot im Kaufvertrag (§ 399 BGB): Lieferant kann Abtretbarkeit ausschließen → LN bleibt ohne Durchgriff

## Insolvenz: Dreiecksfolgen

### Insolvenz des Lieferanten
- LG verliert Gewährleistungsansprüche praktisch (Masse deckt nicht)
- LN hat abgetretene Ansprüche → ebenfalls wertlos
- **Folge**: LN bleibt auf Leasingraten sitzen ohne Mängelabhilfe
- **BGH**: LG haftet subsidiär, wenn abgetretene Ansprüche nicht realisierbar (§ 307 BGB-Wertung)

### Insolvenz des Leasinggebers
- §§ 108, 109 InsO: Leasingvertrag läuft grundsätzlich fort
- LN hat Nutzungsrecht; kann Objekt behalten, solange Raten gezahlt werden
- Aussonderungsrecht von LG-Gläubigern: Wenn LG Objekt sicherungsübereignet hat, kann Sicherungsnehmer herausverlangen; LN hat ggf. Besitzrecht

### Insolvenz des Leasingnehmers
- §§ 108, 109 InsO: Insolvenzverwalter entscheidet über Fortführung
- § 47 InsO: LG kann aussondern (Eigentumsrecht)
- LG muss Antrag stellen; Verwalter hat Wahlrecht bis zur Entscheidung
- Offene Raten vor Insolvenzeröffnung = Insolvenzforderung; Raten danach = Masseverbindlichkeit

## Prüfprogramm

1. Kaufvertrag LG–Lieferant vorhanden und wirksam?
2. Abtretungsklausel vorhanden, wirksam, keine Abtretungsverbote (§ 399 BGB)?
3. Gefahrübergang: Wann und an wen?
4. Insolvenz eines Beteiligten: Welche Ansprüche laufen ins Leere?
5. Subsidiäre Haftung des LG bei wertloser Abtretung?
6. Prozessuale Vorbereitung: LN klagt gegen Lieferant – Klagebefugnis nachgewiesen?

## Typische Fallen

- Abtretungsverbot im Kaufvertrag zwischen LG und Lieferant übersehen → LN ohne Rechte
- Direktlieferung ohne Gefahrübergangsregelung → unklar wer haftet bei Transportschaden
- Insolvenz Lieferant: LN zahlt weiter Raten für fehlerhafte Ware ohne Abhilfemöglichkeit
- Kaufvertrag nicht aufbewahrt: LN kann Klagebefugnis nicht beweisen

## Normen und Quellen

- § 433 BGB: https://dejure.org/gesetze/BGB/433.html
- § 398 BGB: https://dejure.org/gesetze/BGB/398.html
- § 399 BGB (Abtretungsverbot): https://dejure.org/gesetze/BGB/399.html
- § 447 BGB (Versendungskauf): https://dejure.org/gesetze/BGB/447.html
- §§ 108, 109 InsO: https://www.gesetze-im-internet.de/inso/__108.html
- § 47 InsO (Aussonderung): https://www.gesetze-im-internet.de/inso/__47.html
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12: https://www.bgh.de

## Output-Formate

- **Dreiecks-Diagramm**: Vertragsfluss, Abtretung, Gefahrübergang
- **Insolvenz-Matrix**: Wer fällt aus – welche Ansprüche, welche Rechte
- **Klagebefugnis-Checkliste**: LN gegen Lieferant aus abgetretenem Recht

## 3. `lease-015-mangel-am-leasingobjekt-rechte-gegen-lieferant`

**Fokus:** Mangel am Leasingobjekt: Sachmängelrecht, abgetretene Ansprüche gegen Lieferant, Nacherfüllung, Rücktritt, Schadensersatz, Fristen und Beweislast.

# Mangel am Leasingobjekt: Rechte gegen den Lieferanten

## Zweck

Wenn das Leasingobjekt mangelhaft ist, richtet der Leasingnehmer seine Ansprüche kraft Abtretung direkt gegen den Lieferanten. Dieser Skill erklärt die Sachmängelrechte, Fristen, Beweislast und praktische Durchsetzung.

## Sachmängelrecht: Grundlagen (§§ 434–442 BGB)

### Was ist ein Sachmangel? (§ 434 BGB)
- Abweichung von der vereinbarten Beschaffenheit
- Fehlen vereinbarter Eigenschaften
- Einschränkung der gewöhnlichen Verwendung
- Falschlieferung (aliud) und Unterlieferung

### Relevante Mängelarten im Leasing
- **Verborgene Mängel**: Erst nach Übergabe erkennbar (z.B. Materialfehler, Softwarefehler)
- **Arglistig verschwiegene Mängel**: Ausschluss von Verjährungsverkürzung (§ 438 III BGB)
- **Montagefehler** (§ 434 IV BGB): Fehler bei Aufstellung/Installation

## Sachmängelansprüche (§ 437 BGB)

### 1. Nacherfüllung (§ 439 BGB)
- Primäranspruch: LN wählt Nachbesserung oder Neulieferung
- Lieferant kann verweigern bei unverhältnismäßigen Kosten (§ 439 IV BGB)
- Recht des LN auf Selbstvornahme nach fruchtlosem Ablauf der Nacherfüllungsfrist

### 2. Rücktritt (§§ 440, 323 BGB)
- Voraussetzung: Fristsetzung zur Nacherfüllung; erfolglos abgelaufen
- Ausnahme: Frist entbehrlich (§ 440 BGB: Unmöglichkeit, Verweigerung, Unzumutbarkeit)
- Rücktritt im Leasingdreieck: LN tritt zurück → Kaufvertrag LG–Lieferant rückabgewickelt → Leasingvertrag läuft mangels Objekt ins Leere

**Problem**: Rücktritt berührt Kaufvertrag LG–Lieferant, nicht direkt den Leasingvertrag. LN muss ggf. Leasingvertrag separat kündigen.

### 3. Minderung (§ 441 BGB)
- Reduzierung des Kaufpreises proportional zum Minderwert
- Im Leasingkontext: Minderung → LG erhält weniger Kaufpreis → LN profitiert über Ratensenkung (komplex, da Leasingrat unabhängig von Kaufpreis ist)

### 4. Schadensersatz (§§ 440, 281, 280 BGB)
- Statt oder neben Nacherfüllung
- Mangelfolgeschäden: Schäden durch Mangel an anderen Rechtsgütern
- Voraussetzung: Vertretenmüssen des Lieferanten (§ 276 BGB); Vermutung bei Lieferung

## Verjährung (§ 438 BGB)

| Anspruch | Verjährungsfrist | Beginn |
|---|---|---|
| Sachmängelansprüche allgemein | 2 Jahre | Ab Abnahme/Übergabe |
| Bauwerke | 5 Jahre | Ab Abnahme |
| Arglistig verschwiegene Mängel | 3 Jahre (§ 195 BGB) | Ab Kenntnis |
| Dingliche Rechte Dritter | 30 Jahre | Ab Abnahme |

**Kaufmännische Rügeobliegenheit** (§ 377 HGB): Rüge unverzüglich nach Entdeckung; bei versäumter Rüge: Verjährung läuft ggf. nicht, aber Genehmigung gilt als erteilt → praktisch kein Anspruch.

## Beweislast

- LN muss beweisen: Mangel vorhanden, Mangel bei Gefahrübergang (§ 363 BGB), Kausalität
- § 477 BGB (Verbraucher): Innerhalb 1 Jahr nach Lieferung: Vermutung, dass Mangel schon bei Lieferung bestand (nicht anwendbar im B2B-Leasing)
- B2B: LN trägt volle Beweislast für Mangel bei Gefahrübergang

## Abwehrstrategie des Lieferanten

- Einwand: Mangel nach Übergabe entstanden (LN-Verschulden)
- Einwand: Rüge zu spät (§ 377 HGB)
- Einwand: AGB-Haftungsausschluss (im B2B zulässig für leichte Fahrlässigkeit)
- Einwand: Verjährung

## Prüfprogramm

1. Liegt ein Sachmangel im Sinne von § 434 BGB vor?
2. Welcher Anspruch ist vorrangig: Nacherfüllung, Rücktritt, Schadensersatz?
3. Ist Abtretung an LN wirksam vollzogen? Kaufvertrag vorhanden?
4. Rüge rechtzeitig (§ 377 HGB)? Frist? Form?
5. Verjährung nach § 438 BGB abgelaufen?
6. Beweissicherung: Fotos, Gutachten, Protokoll?

## Typische Fallen

- Rüge nach § 377 HGB versäumt → alle Ansprüche verloren
- Nacherfüllungsfrist zu kurz gesetzt → Rücktritt noch nicht fällig
- Verjährung von 2 Jahren übersehen bei spät entdecktem Mangel
- Rücktritt vom Kaufvertrag rückabgewickelt, aber Leasingvertrag weiterläuft

## Normen und Quellen

- §§ 434–442 BGB: https://dejure.org/gesetze/BGB/434.html
- § 437 BGB: https://dejure.org/gesetze/BGB/437.html
- § 438 BGB: https://dejure.org/gesetze/BGB/438.html
- § 377 HGB: https://www.gesetze-im-internet.de/hgb/__377.html
- § 398 BGB: https://dejure.org/gesetze/BGB/398.html
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12: https://www.bgh.de
- openjur.de Sachmängelrecht Leasing: https://openjur.de

## Output-Formate

- **Mängelrüge-Vorlage**: LN an Lieferant (abgetretenes Recht)
- **Anspruchsübersicht**: § 437 BGB – alle vier Ansprüche mit Voraussetzungen
- **Verjährungskalender**: Frist, Beginn, Unterbrechungsmöglichkeit
- **Beweissicherungs-Checkliste**: Fotos, Gutachten, Rügeprotokoll
