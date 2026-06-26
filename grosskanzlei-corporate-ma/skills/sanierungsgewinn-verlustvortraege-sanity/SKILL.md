---
name: sanierungsgewinn-verlustvortraege-sanity
description: "Sanity-Check der Verlustvorträge im Distressed-Due-Diligence-Prozess. Modelliert den Verbrauch von körperschaft- und gewerbesteuerlichen Verlustvorträgen, Zinsvorträgen und EBITDA-Vorträgen durch einen prognostizierten Sanierungsertrag (Paragraf 3a Abs. 3 EStG / Paragraf 7b GewStG). Liefert ein DD-Modul mit Ve..."
---

# Sanierungsgewinn – Verlustvorträge Sanity im DD-Prozess

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten; BGH, 20.11.2018 - II ZR 12/17 für Gesellschafterlisten. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Sanierungsgewinn – Verlustvorträge Sanity im DD-Prozess
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Worum geht es

Verlustvorträge sind in Distressed-Transaktionen kein Buchungsposten, sondern Verhandlungsmasse. Paragraf 3a Abs. 3 EStG ordnet ihren zwingenden Verbrauch durch den späteren Sanierungsertrag an. Wer im Due-Diligence-Bericht den Verlustvortrag mit dem Wert aus dem Steuerbescheid übernimmt, ohne den prognostizierten Verbrauch zu modellieren, liefert einen unbrauchbaren DD-Bericht.

Liefert das Modul, das dem Käufer und dem Sell-side-Team zeigt, **wie viel vom Verlustvortrag nach Restrukturierung tatsächlich übrig bleibt**.

## Wann dieses Modul hilft

- Buy-side-DD eines Targets mit erheblichen kumulierten Verlustvorträgen und absehbarem Sanierungsbedarf.
- Sell-side-DD bzw. Vendor-DD für einen Verkäufer, der mit dem Argument „Verlustvortrag = 200 Mio. EUR" in die Verhandlung geht.
- Restructuring-Beratung, in der die steuerliche Wirkung des Plans noch nicht modelliert ist.
- Konzern-Spin-offs oder Carve-outs mit gleichzeitigem Forderungsverzicht innerhalb des Konzerns.

Nicht dieser Skill ist primär, wenn lediglich eine Standard-Tax-DD ohne Sanierungsbezug gefragt ist; dann genügt das allgemeine M&A-DD-Modul. Hier geht es um den Sonderfall Sanierungsertrag.

## Rechtlicher Rahmen

- **Paragraf 3a EStG** – Steuerbefreiung des Sanierungsertrags; setzt vier Voraussetzungen voraus: Sanierungsbedürftigkeit, Sanierungsfähigkeit, Sanierungseignung des Schulderlasses, Sanierungsabsicht der Gläubiger.
- **Paragraf 3a Abs. 3 EStG** – die **zwingende Verrechnungsreihenfolge**: Sanierungsertrag verbraucht zunächst (i) den laufenden Verlust des Sanierungsjahres, (ii) verbleibende Verlustvorträge des Vorjahres, (iii) den verbleibenden Verlustvortrag, (iv) den Zinsvortrag nach Paragraf 4h EStG, (v) den EBITDA-Vortrag, (vi) Steuerpositionen weiterer Vorschriften. Erst danach greift die Steuerbefreiung auf einen etwaigen Rest.
- **Paragraf 7b GewStG i. V. m. Paragraf 36 Abs. 2c GewStG** – gewerbesteuerliche Parallelregelung; gewerbesteuerliche Verlustvorträge werden separat verbraucht.
- **Paragraf 8c KStG** – Anteilseignerwechsel über 50 % zerstört den Verlustvortrag im Grundsatz. Wird ein DD-Befund mit hohem Verlustvortrag dadurch entwertet, dass der Erwerbsvorgang selbst Paragraf 8c KStG auslöst? Dieses Spannungsfeld ist zwingend zu prüfen.
- **Paragraf 8d KStG** – fortführungsgebundener Verlustvortrag als Rettungsanker; erfordert Antragstellung und strenge Fortführungsbindung.
- **Paragraf 10d EStG** – Verlustvortrag mit Mindestbesteuerung; ab 1 Mio. EUR nur noch 60 % verrechenbar.
- **Paragraf 4h EStG** – Zinsschranke; Zinsvortrag.

## / Schritt für Schritt

1. **Verlustvortrag-Inventur.** Steuerbescheide der letzten fünf Veranlagungszeiträume sichten, einschließlich Feststellungsbescheide nach Paragraf 10d EStG und nach Paragraf 10a GewStG. Achtung auf vorläufige Veranlagungen.
2. **Vortragsmappe vervollständigen.** Zinsvortrag Paragraf 4h EStG, EBITDA-Vortrag, ggf. verbleibende Steuerguthaben aus Organschaft. Zinsvortrag und EBITDA-Vortrag werden in der Praxis häufig vergessen.
3. **Sanierungsertrag prognostizieren.** Aus dem Sanierungsplan oder den geplanten Forderungsverzichten den voraussichtlichen Sanierungsertrag ermitteln. Schuldverzichte unter Besserungsschein gesondert behandeln.
4. **Verbrauchssimulation.** Drei Stufen modellieren: vor Steuern, nach Verbrauch der Vorträge, nach Anwendung Paragraf 3a EStG. Ergebnis ist eine Tabelle, die zeigt, was vom Verlustvortrag übrig bleibt.
5. **Mindestbesteuerung berücksichtigen.** Paragraf 10d EStG begrenzt die Verlustnutzung auf 1 Mio. EUR Sockelbetrag plus 60 % des darüber hinausgehenden Gewinns. Achtung: nach herrschender Auffassung gilt diese Begrenzung im Rahmen des Paragraf 3a Abs. 3 EStG nicht, weil der Sanierungsertrag dort verbraucht wird, bevor Paragraf 10d EStG eingreift. Dieser Punkt ist Streitfeld; im DD ausdrücklich als „streitig, Verlautbarung der Finanzverwaltung Stand 06/2026 zu prüfen" kennzeichnen.
6. **Paragraf 8c KStG-Test.** Erwerb über 50 % der Anteile? Dann Verlustvortrag im Grundsatz untergegangen. Prüfen, ob Paragraf 8d KStG-Antrag möglich ist und ob die stille-Reserven-Klausel des Paragraf 8c Abs. 4 KStG greift.
7. **Disclosure-Red-Flags.** Verlustvorträge in Streit (Außenprüfung läuft, Einspruch gegen Feststellungsbescheid)? Verlustvortrag gefährdet durch Organschaft, Anteilseignerwechsel oder Strukturmaßnahmen?
8. **DD-Bericht-Modul schreiben.** Ergebnisdarstellung als Tabelle, Annahmen explizit, Quellen je Verlustvortrag-Position.

## Trade-off-Matrix

| DD-Stilfrage | Aggressive Sicht (Buy-side) | Konservative Sicht | Empfehlung Großkanzlei |
|---|---|---|---|
| Anwendbarkeit Paragraf 10d EStG-Begrenzung auf Sanierungsertrag | Begrenzung gilt nicht, voller Verbrauch | Begrenzung gilt, Sockelbetrag bleibt | Beide Szenarien rechnen |
| Sanierungseignung Schulderlass | Vereinbarung reicht | Wirtschaftliche Tragfähigkeit beweisen | Konservativ ansetzen |
| Paragraf 8d KStG Antrag | Sicherer Verlustvortrag-Schutz | Strenge Fortführungsbindung | Im DD als Option markieren |
| Verbindliche Auskunft | nicht erforderlich | unbedingt erforderlich | Erforderlich im Distressed-Deal |

## Praxistipps der alten Hasen

Erfahrene Tax-Partner schauen im Distressed-DD zuerst auf drei Zahlen: kumulierter Verlustvortrag laut letztem Feststellungsbescheid, prognostizierter Sanierungsertrag aus dem IDW-S6-Gutachten, und Differenz aus beidem. Der Rest ist Folge dieser Differenz. Drei weitere Beobachtungen aus der Praxis:

- **Der Zinsvortrag wird unterschätzt.** Bei einer fremdfinanzierten Holding kann der Zinsvortrag nach Paragraf 4h EStG im hohen siebenstelligen Bereich liegen und durch den Sanierungsertrag mitverzehrt werden.
- **Die Mindestbesteuerung-Frage ist Verhandlungsmasse.** Solange die Finanzverwaltung diese Frage nicht abschließend geklärt hat, lässt sich im SPA mit der Tax-Indemnity arbeiten.
- **Der Feststellungsbescheid ist oft nicht final.** Eine laufende Außenprüfung kann den Verlustvortrag noch deutlich verändern; diese Schwebephase gehört explizit in den DD-Bericht.

## SPA-/Plan-Klausel Mustertexte

**Vendor Warranty re Verlustvortrag (Auszug):**

> Verkäufergarantie Steuern: Der Verkäufer garantiert, dass die in Anlage X aufgeführten körperschaft- und gewerbesteuerlichen Verlustvorträge der Zielgesellschaft zum Stichtag in der dort genannten Höhe bestandskräftig festgestellt sind. Eine Garantie für den steuerlichen Bestand dieser Verlustvorträge nach Wirksamwerden der in diesem Vertrag vorgesehenen Sanierungsmaßnahmen wird nicht übernommen; insoweit verweisen die Parteien auf die Indemnity-Regelung gemäß Ziffer Y.

**Indemnity-Klausel zum Verbrauch durch Sanierungsertrag:**

> Tax Indemnity Sanierungsertrag: Der Verkäufer stellt den Käufer frei von steuerlichen Nachteilen, die daraus entstehen, dass die nach Paragraf 3a Abs. 3 EStG zwingende Verrechnungsreihenfolge zu einem höheren Verbrauch der Verlustvorträge führt als in dem Tax-Modell gemäß Anlage X angenommen, soweit der Abweichungsbetrag eine Schwelle von [Betrag] übersteigt.

## Typische Fehler in komplexer Transaktion

- Verlustvortrag mit dem Wert aus dem letzten Feststellungsbescheid übernommen, ohne die laufende Außenprüfung zu prüfen.
- Zinsvortrag Paragraf 4h EStG und EBITDA-Vortrag aus dem Sanity-Check vergessen.
- Paragraf 10d EStG-Mindestbesteuerung doppelt angewendet (in der Sanierungsmechanik und in der Verlustvortragsmodellierung), obwohl streitig ist, ob sie im Rahmen Paragraf 3a Abs. 3 EStG überhaupt greift.
- Paragraf 8c KStG-Test übersprungen, weil „nur 49,9 % erworben werden"; Hinzurechnungen von Stimmrechten oder nahestehenden Personen werden übersehen.
- DD-Bericht enthält keinen Hinweis auf die Notwendigkeit einer verbindlichen Auskunft nach Paragraf 89 AO.

## Querverweise

- Plugin `steuerrecht-anwalt-und-berater`: Skill zu Paragraf 8c und Paragraf 8d KStG; Skill zu Paragraf 89 AO.
- Plugin `insolvenzrecht`: Wirkung des Insolvenzplans auf Verlustvorträge.
- Plugin `grosskanzlei-corporate-ma`:
 - `grosskanzlei-corporate-ma-due-diligence-legal`
 - `gk-sanierungsgewinn-fruehe-mandantsteuerung-q-minus-zwoelf`
 - `gk-sanierungsgewinn-tax-warranty-und-tax-indemnity-im-spa`
 - `gk-sanierungsgewinn-stille-reserven-klausel-8c-iv-kstg`

## Quellen Stand 06/2026

- Paragraf 3a EStG; Paragraf 3a Abs. 3 EStG; Paragraf 7b GewStG i. V. m. Paragraf 36 Abs. 2c GewStG; Paragraf 8c KStG; Paragraf 8d KStG; Paragraf 10d EStG; Paragraf 4h EStG – jeweils aktuelle Fassung, prüfbar über gesetze-im-internet.de.
- BMF-Schreiben vom 27.04.2017 – Verifizierung im Bundessteuerblatt Stand 06/2026.
- FG Köln, Urteil vom 04.11.2025 – 12 K 1413/25 – prüfbar über dejure.org und NWB.
- FG Köln, Urteil vom 06.03.2012 – 13 K 3006/11, GmbHR 2012, 977 (vorgehend zu BFH I R 34/12) – verifizierte Fundstelle für die DD-Bewertung von Targets, die statt einer Sanierung in die Liquidation laufen (nachrangige Gesellschafterdarlehen, Erlöschen von Verbindlichkeiten und Verlustvorträgen mit Löschung).
- BFH (Großer Senat), Beschluss vom 28.11.2016 – GrS 1/15 – prüfbar über bundesfinanzhof.de.
- Sonstige BFH-Rspr. zu Paragraf 10d EStG und Paragraf 4h EStG als „ständige Rspr." formulieren; Verifizierung über bundesfinanzhof.de.
